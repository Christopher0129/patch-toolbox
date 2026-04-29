#!/usr/bin/env python3
"""
通用工具库 - 去重、SQLite 数据层、Markdown 生成、GitHub/Gitee 推送、日志记录
"""
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = PROJECT_ROOT / "state.json"
AGENTS_DIR = PROJECT_ROOT / "agents"
AGENTS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 去重状态管理（legacy，兼容旧 agent）
# ---------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state: dict):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def dedup_key(item: dict) -> str:
    """生成去重键：优先用明确ID，否则用URL+标题哈希"""
    key_fields = ["cve_id", "id", "guid", "url", "link", "title"]
    parts = []
    for field in key_fields:
        if field in item and item[field]:
            parts.append(str(item[field]).strip())
    if parts:
        raw = "|".join(parts)
    else:
        raw = json.dumps(item, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def filter_new_items(category: str, items: List[dict], keep_old_methods: bool = True) -> List[dict]:
    """
    增量过滤：保留全新条目，同一key的不同方法追加记录。
    category 示例: "network-security", "sys-vuln-windows", "sys-trouble-linux"
    """
    state = load_state()
    seen = state.get(category, {})
    new_items = []
    updated = False

    for item in items:
        key = dedup_key(item)
        if key not in seen:
            seen[key] = {
                "first_seen": datetime.now(timezone.utc).isoformat(),
                "last_updated": datetime.now(timezone.utc).isoformat(),
                "methods": [],
                "data": item,
            }
            seen[key]["methods"].append(item.get("solution", item.get("mitigation", "N/A")))
            new_items.append(item)
            updated = True
        elif keep_old_methods:
            method = item.get("solution", item.get("mitigation", "N/A"))
            if method not in seen[key]["methods"]:
                seen[key]["methods"].append(method)
                seen[key]["last_updated"] = datetime.now(timezone.utc).isoformat()
                new_items.append(item)
                updated = True

    if updated:
        state[category] = seen
        save_state(state)
    return new_items


# =========================================================================
# SQLite 数据层（新版核心）
# =========================================================================

DB_DIR = PROJECT_ROOT / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)


def get_db_path(category: str) -> Path:
    """根据分类返回 SQLite 数据库路径"""
    mapping = {
        "network-security": DB_DIR / "network-security.db",
        "netsec-windows": DB_DIR / "network-security.db",
        "netsec-linux": DB_DIR / "network-security.db",
        "netsec-macos": DB_DIR / "network-security.db",
        "netsec-general": DB_DIR / "network-security.db",
        "sys-vuln-windows": DB_DIR / "system-vulnerabilities.db",
        "sys-vuln-linux": DB_DIR / "system-vulnerabilities.db",
        "sys-vuln-macos": DB_DIR / "system-vulnerabilities.db",
        "sys-trouble-windows": DB_DIR / "system-troubleshooting.db",
        "sys-trouble-linux": DB_DIR / "system-troubleshooting.db",
        "sys-trouble-macos": DB_DIR / "system-troubleshooting.db",
    }
    return mapping.get(category, DB_DIR / f"{category}.db")


def init_sqlite_db(db_path: Path) -> sqlite3.Connection:
    """初始化 SQLite 数据库（如果不存在则创建表）"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            hash TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            solution TEXT,
            severity TEXT,
            cvss_score REAL,
            source TEXT,
            source_url TEXT,
            refs TEXT,
            platform TEXT,
            tags TEXT,
            affected_products TEXT,
            published TEXT,
            last_modified TEXT,
            first_seen TEXT,
            last_updated TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()
    return conn


def insert_entries_sqlite(
    conn: sqlite3.Connection,
    items: List[dict],
    platform: Optional[str] = None,
) -> int:
    """
    批量插入条目到 SQLite，自动去重。
    返回实际插入的新条目数。
    """
    c = conn.cursor()
    inserted = 0
    now = datetime.now(timezone.utc).isoformat()

    for item in items:
        h = dedup_key(item)
        title = item.get("title", "")
        if not title:
            continue

        c.execute("SELECT 1 FROM entries WHERE hash = ?", (h,))
        if c.fetchone():
            continue

        desc = item.get("description", "")
        sol = item.get("solution", item.get("mitigation", "N/A"))
        sev = item.get("severity", "")
        cvss = item.get("cvss_score")
        source = item.get("source_tag") or item.get("source") or "NVD"
        url = item.get("source_url", item.get("link", item.get("url", "")))
        refs = json.dumps(item.get("references", []), ensure_ascii=False)
        tags = json.dumps(item.get("tags", []), ensure_ascii=False)
        prods = json.dumps(item.get("affected_products", []), ensure_ascii=False)
        published = item.get("published", "")
        last_mod = item.get("last_modified", "")

        c.execute("""
            INSERT INTO entries (hash, title, description, solution, severity, cvss_score,
                source, source_url, refs, platform, tags, affected_products,
                published, last_modified, first_seen, last_updated)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            h, title, desc, sol, sev, cvss,
            source, url, refs, platform, tags, prods,
            published, last_mod, now, now
        ))
        inserted += 1

    conn.commit()
    return inserted


def count_entries_sqlite(conn: sqlite3.Connection, platform: Optional[str] = None) -> int:
    """统计条目数"""
    c = conn.cursor()
    if platform:
        c.execute("SELECT COUNT(*) FROM entries WHERE platform = ?", (platform,))
    else:
        c.execute("SELECT COUNT(*) FROM entries")
    return c.fetchone()[0]


def regenerate_all_md():
    """调用 regenerate_md.py 重新生成所有 MD 文件"""
    regen_script = PROJECT_ROOT / "scripts" / "regenerate_md.py"
    if regen_script.exists():
        result = subprocess.run([sys.executable, str(regen_script)], capture_output=True, text=True)
        log_agent("utils", f"MD regeneration: {result.stdout.strip()}")
        if result.returncode != 0:
            log_agent("utils", f"MD regeneration error: {result.stderr.strip()}")
        return result.returncode == 0
    log_agent("utils", f"regenerate_md.py not found at {regen_script}")
    return False


# ---------------------------------------------------------------------------
# Markdown 生成器（内置中英双语切换）
# ---------------------------------------------------------------------------

MD_LANG_SWITCHER = """<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#english-en">English 🇺🇸</a>
</p>

---
"""


def make_bilingual_md(
    title_zh: str,
    title_en: str,
    intro_zh: str,
    intro_en: str,
    sections: List[Dict[str, Any]],
    update_time: str = None,
    nav_links: List[Dict[str, str]] = None,
) -> str:
    """
    生成带双语切换锚点的 Markdown。
    sections 格式：
    [
      {
        "heading_zh": "高危漏洞",
        "heading_en": "Critical Vulnerabilities",
        "items": [
          {
            "zh": { "title": "...", "content": "..." },
            "en": { "title": "...", "content": "..." },
          }
        ]
      }
    ]
    """
    if update_time is None:
        update_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append(f"# {title_zh} | {title_en}")
    lines.append("")
    lines.append(MD_LANG_SWITCHER)
    lines.append(f"_自动更新于 / Auto-updated: {update_time}_")
    lines.append("")

    # 中文部分
    lines.append('<a id="中文-zh"></a>')
    lines.append(f"## 中文 🇨🇳")
    lines.append(f"**{title_zh}**")
    lines.append("")
    lines.append(intro_zh)
    lines.append("")

    for sec in sections:
        lines.append(f"### {sec['heading_zh']}")
        lines.append("")
        for idx, item in enumerate(sec["items"], 1):
            zh = item["zh"]
            title = zh.get("title", "Untitled")
            content = zh.get("content", "")
            source = zh.get("source", "")
            lines.append(f"#### {idx}. {title}")
            lines.append("")
            lines.append(content)
            if source:
                lines.append(f"\n> 📎 来源 / Source: {source}")
            lines.append("")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 英文部分
    lines.append('<a id="english-en"></a>')
    lines.append(f"## English 🇺🇸")
    lines.append(f"**{title_en}**")
    lines.append("")
    lines.append(intro_en)
    lines.append("")

    for sec in sections:
        lines.append(f"### {sec['heading_en']}")
        lines.append("")
        for idx, item in enumerate(sec["items"], 1):
            en = item["en"]
            title = en.get("title", "Untitled")
            content = en.get("content", "")
            source = en.get("source", "")
            lines.append(f"#### {idx}. {title}")
            lines.append("")
            lines.append(content)
            if source:
                lines.append(f"\n> 📎 Source: {source}")
            lines.append("")
        lines.append("")

    # 导航链接
    if nav_links:
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("**🔗 导航 / Navigation**")
        lines.append("")
        for link in nav_links:
            text_zh = link.get("text_zh", "")
            text_en = link.get("text_en", "")
            href = link.get("href", "#")
            lines.append(f"- [{text_zh} / {text_en}]({href})")
        lines.append("")

    return "\n".join(lines)


def write_md_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# 日志与汇报
# ---------------------------------------------------------------------------

def log_sync(sync_name: str, message: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{sync_name}] {message}\n"
    log_file = AGENTS_DIR / f"{sync_name}.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())


# 兼容性别名（旧脚本迁移用）
log_agent = log_sync


def _git_push_secure(remote: str, branch: str, token: str, env: dict) -> bool:
    """安全推送：token 不出现在 git remote URL，仅在 push 命令中通过 auth URL 传递。
    通过临时 GIT_ASKPASS 脚本向 git 注入凭据，避免把 token 暴露在 push URL 或命令行参数里。
    """
    # 获取当前 remote 的干净 URL
    r = subprocess.run(["git", "remote", "get-url", remote], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        return False
    url = r.stdout.strip()

    askpass = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", prefix="patch-toolbox-askpass-", suffix=".sh", delete=False) as tmp:
            tmp.write('#!/bin/sh\ncase "$1" in\n  *Username*) echo "oauth2" ;;\n  *Password*) echo "$PATCH_TOOLBOX_TOKEN" ;;\n  *) echo "" ;;\nesac\n')
            askpass = Path(tmp.name)
        askpass.chmod(0o700)
        env_auth = env.copy()
        env_auth["GIT_ASKPASS"] = str(askpass)
        env_auth["PATCH_TOOLBOX_TOKEN"] = token
        env_auth["GIT_TERMINAL_PROMPT"] = "0"
        push_url = url
        if "gitee.com" in url:
            push_url = url.replace("https://gitee.com/", "https://oauth2@gitee.com/", 1) if url.startswith("https://gitee.com/") else url
        result = subprocess.run(
            ["git", "push", push_url, f"HEAD:{branch}"],
            capture_output=True, text=True, env=env_auth,
        )
        return result.returncode == 0
    finally:
        if askpass and askpass.exists():
            askpass.unlink()


def write_report(sync_name: str, new_count: int, total_count: int, errors: List[str] = None):
    report = {
        "sync": sync_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "new_items": new_count,
        "total_items": total_count,
        "errors": errors or [],
    }
    report_file = AGENTS_DIR / f"{sync_name}_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    return report


# ---------------------------------------------------------------------------
# GitHub 推送
# ---------------------------------------------------------------------------

def ensure_git_identity(env: dict) -> bool:
    """确保当前仓库具备可提交的本地 git 身份；缺失时写入兜底值。"""
    name = subprocess.run(["git", "config", "--get", "user.name"], capture_output=True, text=True, env=env)
    email = subprocess.run(["git", "config", "--get", "user.email"], capture_output=True, text=True, env=env)
    current_name = name.stdout.strip() if name.returncode == 0 else ""
    current_email = email.stdout.strip() if email.returncode == 0 else ""

    fallback_name = os.environ.get("PATCH_TOOLBOX_GIT_NAME", "patch-toolbox-bot")
    fallback_email = os.environ.get("PATCH_TOOLBOX_GIT_EMAIL", "patch-toolbox-bot@local")

    if not current_name:
        subprocess.run(["git", "config", "user.name", fallback_name], capture_output=True, text=True, env=env)
        log_agent("publisher", f"git user.name missing; set local fallback: {fallback_name}")
    if not current_email:
        subprocess.run(["git", "config", "user.email", fallback_email], capture_output=True, text=True, env=env)
        log_agent("publisher", f"git user.email missing; set local fallback: {fallback_email}")

    verify_name = subprocess.run(["git", "config", "--get", "user.name"], capture_output=True, text=True, env=env)
    verify_email = subprocess.run(["git", "config", "--get", "user.email"], capture_output=True, text=True, env=env)
    return bool(verify_name.stdout.strip() and verify_email.stdout.strip())

def git_push(msg: str = None) -> dict:
    """推送至 GitHub 与 Gitee，返回 {github: bool, gitee: bool}

    GitHub 操作不走代理（proxy IP 被风控），Git 环境变量自动处理。
    Token 通过 GIT_ASKPASS 临时脚本注入，避免出现在命令行或 remote URL。
    """
    if msg is None:
        msg = f"auto-update: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"

    # 清除代理环境变量，Git 操作走直连
    env_clean = os.environ.copy()
    env_clean.pop("HTTP_PROXY", None)
    env_clean.pop("HTTPS_PROXY", None)
    env_clean.pop("http_proxy", None)
    env_clean.pop("https_proxy", None)

    token_gh = os.environ.get("GITHUB_TOKEN") or _read_token_from_script()
    token_gt = os.environ.get("GITEE_TOKEN") or _read_gitee_token_from_script()

    os.chdir(PROJECT_ROOT)
    subprocess.run(["git", "branch", "-M", "main"], capture_output=True, env=env_clean)

    # 先尝试 fetch 避免冲突（公开仓库 fetch 无需认证）
    subprocess.run(["git", "fetch", "origin", "main"], capture_output=True, env=env_clean)

    # git add
    result = subprocess.run(["git", "add", "."], capture_output=True, text=True, env=env_clean)
    log_agent("publisher", "Git add OK")

    if not ensure_git_identity(env_clean):
        log_agent("publisher", "Git identity missing and fallback setup failed")
        return {"github": False, "gitee": False}

    # git commit
    result = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True, env=env_clean)
    if result.returncode != 0:
        if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
            log_agent("publisher", "Nothing to commit")
            return {"github": True, "gitee": True}
        log_agent("publisher", f"Git commit failed: {result.stderr}")
        return {"github": False, "gitee": False}

    # ---- GitHub push ----
    github_ok = False
    if _git_push_secure("origin", "main", token_gh, env_clean):
        github_ok = True
        log_agent("publisher", "GitHub push OK")
    else:
        # retry with pull --rebase
        log_agent("publisher", "GitHub push failed, trying pull --rebase")
        subprocess.run(["git", "pull", "origin", "main", "--rebase"], capture_output=True, env=env_clean)
        if _git_push_secure("origin", "main", token_gh, env_clean):
            github_ok = True
            log_agent("publisher", "GitHub push OK (after rebase)")
        else:
            log_agent("publisher", "GitHub push failed")

    # ---- Gitee push ----
    gitee_ok = False
    if github_ok:
        if _git_push_secure("gitee", "main", token_gt, env_clean):
            gitee_ok = True
            log_agent("publisher", "Gitee push OK")
        else:
            log_agent("publisher", "Gitee push failed")

    return {"github": github_ok, "gitee": gitee_ok}


def _read_token_from_script() -> str:
    script = Path.home() / ".github" / "get-token.sh"
    if script.exists():
        result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
        return result.stdout.strip()
    raise RuntimeError("GITHUB_TOKEN not found")


def _read_gitee_token_from_script() -> str:
    """优先读取 ~/.openclaw/secrets/get-secret.sh，兼容旧路径 ~/.gitee/get-token.sh"""
    script_new = Path.home() / ".openclaw" / "secrets" / "get-secret.sh"
    if script_new.exists():
        result = subprocess.run(["bash", str(script_new), "gitee_token"], capture_output=True, text=True)
        token = result.stdout.strip()
        if token:
            return token
    # 兼容旧路径
    script_old = Path.home() / ".gitee" / "get-token.sh"
    if script_old.exists():
        result = subprocess.run(["bash", str(script_old)], capture_output=True, text=True)
        return result.stdout.strip()
    raise RuntimeError("GITEE_TOKEN not found")

# ---- Restored helper functions required by sync scripts ----

def fetch_json(url: str, timeout: int = 30, retries: int = 3, verify: bool = True) -> Optional[dict]:
    """使用 curl_cffi 抓取 JSON（模拟浏览器指纹，绕过 Cloudflare/反爬）
    
    GitHub API 不走代理（datacenter IP 被风控）。
    Reddit 必须走代理 + 完整浏览器 headers。
    """
    try:
        from curl_cffi import requests
    except ImportError:
        log_agent("utils", f"fetch_json skip: curl_cffi not installed: {url}")
        return None
    
    is_github = "api.github.com" in url or "github.com" in url
    is_reddit = "reddit.com" in url
    
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    
    kwargs = {
        "timeout": timeout,
        "verify": verify,
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
        },
    }
    
    if is_reddit:
        if not proxy:
            log_agent("utils", f"fetch_json skip: no proxy for Reddit: {url}")
            return None
        # Reddit 用更强的 headers 轮换
        _REDDIT_UAS = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        ]
        kwargs["headers"] = {
            "User-Agent": _REDDIT_UAS[0],
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
            "DNT": "1",
        }
        kwargs["proxies"] = {"http": proxy, "https": proxy}
    elif not is_github and proxy:
        # 非 GitHub 非 Reddit，有代理就用
        kwargs["proxies"] = {"http": proxy, "https": proxy}
    
    if not is_reddit:
        kwargs["impersonate"] = "chrome120"
    
    for attempt in range(retries):
        try:
            if is_reddit:
                kwargs["headers"]["User-Agent"] = _REDDIT_UAS[attempt % len(_REDDIT_UAS)]
                time.sleep(1.5 * attempt)
            r = requests.get(url, **kwargs)
            if r.status_code == 429:
                wait = 5 + (2 ** attempt)
                log_agent("utils", f"Rate limit 429, waiting {wait}s...")
                time.sleep(wait)
                continue
            if is_reddit and r.status_code in (403, 429):
                wait = 5 + (3 ** attempt)
                log_agent("utils", f"Reddit {r.status_code}, waiting {wait}s...")
                time.sleep(wait)
                continue
            r.raise_for_status()
            log_agent("utils", f"fetch_json OK: {url} (HTTP {r.status_code})")
            return r.json()
        except Exception as e:
            time.sleep(2 ** attempt)
            if attempt == retries - 1:
                log_agent("utils", f"fetch_json failed: {url} | {e}")
    return None

def fetch_text(url: str, timeout: int = 30, retries: int = 3, verify: bool = True) -> Optional[str]:
    """使用 curl_cffi 抓取文本/HTML（模拟浏览器指纹）
    
    Reddit 特殊处理：使用完整浏览器 headers 绕过风控。
    关键 headers：User-Agent、Accept、Accept-Language、Referer、Connection。
    """
    try:
        from curl_cffi import requests
    except ImportError:
        log_agent("utils", f"fetch_text skip: curl_cffi not installed: {url}")
        return None
    
    is_reddit = "reddit.com" in url
    
    # Reddit 专用完整浏览器请求头轮换（绕过风控）
    _REDDIT_UAS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    ]
    
    def _reddit_headers(idx: int = 0):
        return {
            "User-Agent": _REDDIT_UAS[idx % len(_REDDIT_UAS)],
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
            "DNT": "1",
        }
    
    # 代理配置：Reddit 必须走代理（国内被墙），其他看情况
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    if is_reddit and not proxy:
        log_agent("utils", f"fetch_text skip: no proxy for Reddit: {url}")
        return None
    
    kwargs = {
        "timeout": timeout,
        "verify": verify,
        "headers": _reddit_headers() if is_reddit else {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    }
    if proxy:
        kwargs["proxies"] = {"http": proxy, "https": proxy}
    
    if not is_reddit:
        kwargs["impersonate"] = "chrome120"
    
    for attempt in range(retries):
        try:
            if is_reddit:
                # Reddit 轮换 UA + 增加延迟
                kwargs["headers"] = _reddit_headers(attempt)
                time.sleep(1.5 * attempt)  # Reddit 增加退避
            r = requests.get(url, **kwargs)
            if is_reddit and r.status_code in (403, 429):
                wait = 5 + (3 ** attempt)
                log_agent("utils", f"Reddit {r.status_code}, waiting {wait}s...")
                time.sleep(wait)
                continue
            r.raise_for_status()
            log_agent("utils", f"fetch_text OK: {url} (HTTP {r.status_code})")
            return r.text
        except Exception as e:
            time.sleep(2 ** attempt)
            if attempt == retries - 1:
                log_agent("utils", f"fetch_text failed: {url} | {e}")
    return None

def fetch_rss(url: str, timeout: int = 30, retries: int = 3, verify: bool = True) -> Optional[list]:
    """使用 curl_cffi 抓取 RSS/Atom feed，返回 feedparser entries"""
    try:
        import feedparser
    except ImportError:
        log_agent("utils", f"fetch_rss skip: feedparser not installed: {url}")
        return None
    text = fetch_text(url, timeout=timeout, retries=retries, verify=verify)
    if not text:
        return None
    try:
        feed = feedparser.parse(text)
        return feed.entries
    except Exception as e:
        log_agent("utils", f"fetch_rss parse failed: {url} | {e}")
    return None


# ---------------------------------------------------------------------------
# 通用格式化
# ---------------------------------------------------------------------------

def strip_html_tags(text: str) -> str:
    if not text:
        return ""
    import html
    clean = re.sub(r"<[^>]+>", "", text)
    clean = html.unescape(clean)
    return clean.strip()



def summarize_title(text: str, limit: int = 80) -> str:
    text = strip_html_tags(text)
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit(' ', 1)[0].strip()
    if not clipped:
        clipped = text[:limit].strip()
    return clipped + '…'

def send_sync_report(sync_name: str, new_items: int, total_items: int, errors: list, elapsed_sec: float = None, extra_info: str = "") -> None:
    """
    同步脚本执行完成后自动汇报。
    1. 写入汇报文件 agents/daily_summary.md
    2. 若配置了 WEIXIN_TARGET 环境变量，发送微信消息
    3. 若配置了 KIMI_TARGET 环境变量，发送 Kimi Claw 消息
    """
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    elapsed = f" | 耗时: {elapsed_sec:.1f}s" if elapsed_sec else ""
    err_count = len(errors)
    err_text = "\n".join(f"  - {e}" for e in errors[:5]) if errors else "  无"

    report = f"""
## [{sync_name}] {ts}
- **新增**: {new_items} 条
- **累计**: {total_items} 条
- **错误**: {err_count} 个{elapsed}
{extra_info}
**错误详情**:
{err_text}
---
"""
    # 追加写入汇报文件
    summary_path = AGENTS_DIR / "daily_summary.md"
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write(report)

    # 微信推送（若配置了 target）
    weixin_target = os.environ.get("WEIXIN_TARGET", "")
    if weixin_target:
        msg = f"📋 {sync_name} 执行汇报\n⏰ {ts}\n🆕 新增: {new_items} 条\n📦 累计: {total_items} 条\n❌ 错误: {err_count} 个{elapsed}\n{extra_info.strip()}"
        try:
            subprocess.run(
                ["openclaw", "message", "send", "--channel", "openclaw-weixin", "--target", weixin_target, "--message", msg],
                capture_output=True, text=True, timeout=15, check=False
            )
        except Exception as e:
            log_agent("utils", f"Weixin report send failed: {e}")

    # Kimi Claw 推送（当前会话）
    kimi_target = os.environ.get("KIMI_TARGET", "")
    if kimi_target:
        msg = f"📋 {sync_name} 执行汇报\n⏰ {ts}\n🆕 新增: {new_items} 条\n📦 累计: {total_items} 条\n❌ 错误: {err_count} 个{elapsed}\n{extra_info.strip()}"
        try:
            subprocess.run(
                ["openclaw", "message", "send", "--channel", "kimi-claw", "--target", kimi_target, "--message", msg],
                capture_output=True, text=True, timeout=15, check=False
            )
        except Exception as e:
            log_agent("utils", f"Kimi Claw report send failed: {e}")

