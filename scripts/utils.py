#!/usr/bin/env python3
"""
通用工具库 - 去重、Markdown生成、双语模板、GitHub推送、日志记录
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = PROJECT_ROOT / "state.json"
AGENTS_DIR = PROJECT_ROOT / "agents"
AGENTS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 去重状态管理
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
            # 同一漏洞/故障，新方法则增量记录
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


# ---------------------------------------------------------------------------
# Markdown 生成器（内置中英双语切换）
# ---------------------------------------------------------------------------

MD_LANG_SWITCHER = """<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---

"""


def make_bilingual_md(
    title_zh: str,
    title_en: str,
    intro_zh: str,
    intro_en: str,
    sections: List[Dict[str, Any]],  # 每个元素含 zh / en 子结构
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

def log_agent(agent_name: str, message: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{agent_name}] {message}\n"
    log_file = AGENTS_DIR / f"{agent_name}.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())


def write_report(agent_name: str, new_count: int, total_count: int, errors: List[str] = None):
    report = {
        "agent": agent_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "new_items": new_count,
        "total_items": total_count,
        "errors": errors or [],
    }
    report_file = AGENTS_DIR / f"{agent_name}_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    return report


# ---------------------------------------------------------------------------
# GitHub 推送
# ---------------------------------------------------------------------------

def git_push(msg: str = None):
    if msg is None:
        msg = f"auto-update: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"
    token = os.environ.get("GITHUB_TOKEN") or _read_token_from_script()
    repo = "https://github.com/Christopher0129/security-knowledge-base.git"
    # 使用 token 嵌入 remote URL
    auth_repo = repo.replace("https://", f"https://{token}@")

    cmds = [
        ["git", "add", "."],
        ["git", "commit", "-m", msg],
        ["git", "push", auth_repo, "HEAD:main"],
    ]

    os.chdir(PROJECT_ROOT)
    # 确保分支是 main
    subprocess.run(["git", "branch", "-M", "main"], capture_output=True)
    # 先尝试 fetch 避免冲突
    subprocess.run(["git", "fetch", auth_repo, "main"], capture_output=True)

    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            # commit 可能 nothing to commit
            if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
                continue
            if cmd[0] == "git" and cmd[1] == "push":
                # 尝试 pull --rebase 再 push
                subprocess.run(["git", "pull", auth_repo, "main", "--rebase"], capture_output=True)
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    log_agent("publisher", f"Git push failed: {result.stderr}")
                    return False
        log_agent("publisher", f"Git cmd OK: {' '.join(cmd[:3])}...")
    return True


def _read_token_from_script() -> str:
    script = Path.home() / ".github" / "get-token.sh"
    if script.exists():
        result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
        return result.stdout.strip()
    raise RuntimeError("GITHUB_TOKEN not found")


# ---------------------------------------------------------------------------
# 网络请求辅助
# ---------------------------------------------------------------------------

def fetch_json(url: str, timeout: int = 30, retries: int = 3) -> Optional[dict]:
    import requests
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=timeout, headers={
                "User-Agent": "Mozilla/5.0 (compatible; SecurityKB-Bot/1.0)"
            })
            r.raise_for_status()
            return r.json()
        except Exception as e:
            time.sleep(2 ** attempt)
            if attempt == retries - 1:
                log_agent("utils", f"fetch_json failed after {retries} attempts: {url} | {e}")
    return None


def fetch_text(url: str, timeout: int = 30, retries: int = 3) -> Optional[str]:
    import requests
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=timeout, headers={
                "User-Agent": "Mozilla/5.0 (compatible; SecurityKB-Bot/1.0)"
            })
            r.raise_for_status()
            return r.text
        except Exception as e:
            time.sleep(2 ** attempt)
            if attempt == retries - 1:
                log_agent("utils", f"fetch_text failed after {retries} attempts: {url} | {e}")
    return None


# ---------------------------------------------------------------------------
# 通用格式化
# ---------------------------------------------------------------------------

def strip_html_tags(text: str) -> str:
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", "", text)
    return clean.strip()


def safe_filename(text: str) -> str:
    return re.sub(r"[^\w\-\.]", "_", text)[:80]


if __name__ == "__main__":
    print("utils.py - common utilities for security-knowledge-base")
