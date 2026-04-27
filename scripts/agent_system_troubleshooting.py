#!/usr/bin/env python3
"""
Agent: System Troubleshooting (Windows / Linux / macOS)
每小时按操作系统分类抓取系统常见故障及解决方法，增量更新。
数据源: Stack Exchange API (Super User, Ask Ubuntu, Ask Different, Server Fault)
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

import requests
from bs4 import BeautifulSoup

from utils import (
    fetch_json, log_agent, write_report,
    filter_new_items, make_bilingual_md, write_md_file, strip_html_tags,
)

AGENT_NAME = "agent-system-troubleshooting"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "system-troubleshooting"
MIN_ITEMS = 50

# OS 对应的 Stack Exchange 站点和标签
OS_CONFIG = {
    "windows": {
        "sites": ["superuser", "serverfault"],
        "tags": ["windows", "windows-10", "windows-11", "windows-server"],
    },
    "linux": {
        "sites": ["unix", "askubuntu", "superuser", "serverfault"],
        "tags": ["linux", "ubuntu", "debian", "centos", "fedora", "bash", "shell"],
    },
    "macos": {
        "sites": ["apple", "superuser"],
        "tags": ["macos", "macbook", "terminal", "brew"],
    },
}

SE_API_KEY = ""  # Stack Exchange 可选 API key，提高配额


# ---------------------------------------------------------------------------
# Stack Exchange API 抓取
# ---------------------------------------------------------------------------

def se_fetch_questions(site: str, tag: str, pagesize: int = 50) -> List[Dict[str, Any]]:
    """获取问题列表（含body需要filter，先取基础信息）"""
    url = (
        f"https://api.stackexchange.com/2.3/questions"
        f"?order=desc&sort=votes"
        f"&tagged={tag}"
        f"&site={site}"
        f"&pagesize={pagesize}"
    )
    if SE_API_KEY:
        url += f"&key={SE_API_KEY}"

    data = fetch_json(url, timeout=30)
    if not data or "items" not in data:
        return []
    return data["items"]


def se_fetch_answers(question_ids: List[int], site: str) -> Dict[int, List[Dict]]:
    """批量获取问题的答案（取最高票答案）"""
    if not question_ids:
        return {}
    ids_str = ";".join(str(i) for i in question_ids)
    url = (
        f"https://api.stackexchange.com/2.3/questions/{ids_str}/answers"
        f"?order=desc&sort=votes"
        f"&site={site}"
        f"&pagesize=100"
        f"&filter=withbody"
    )
    if SE_API_KEY:
        url += f"&key={SE_API_KEY}"

    data = fetch_json(url, timeout=30)
    if not data or "items" not in data:
        return {}

    result: Dict[int, List[Dict]] = {}
    for ans in data["items"]:
        qid = ans.get("question_id")
        if qid not in result:
            result[qid] = []
        result[qid].append(ans)
    return result


def fetch_page_html(url: str, retries: int = 3) -> Optional[str]:
    """用 requests 直接拉取页面 HTML（Stack Exchange 是服务端渲染的）"""
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=20, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
            r.raise_for_status()
            return r.text
        except Exception as e:
            time.sleep(2 ** attempt)
            if attempt == retries - 1:
                log_agent(AGENT_NAME, f"fetch_page failed: {url} | {e}")
    return None


def extract_answer_from_html(html: str) -> str:
    """从 Stack Exchange 问题页面提取最高票答案内容"""
    soup = BeautifulSoup(html, "lxml")
    # 找答案区域
    answers = soup.find_all("div", class_=re.compile(r"answer"))
    if not answers:
        return ""
    # 通常第一个是最高票的（页面上已排序）
    best = answers[0]
    body = best.find("div", class_=re.compile(r"post-layout|answercell"))
    if not body:
        body = best
    text = body.get_text(separator="\n", strip=True)
    # 截断
    if len(text) > 2000:
        text = text[:2000] + "... [truncated]"
    return text


# ---------------------------------------------------------------------------
# 按 OS 抓取
# ---------------------------------------------------------------------------

def fetch_troubleshooting(os_name: str, min_items: int = 50) -> List[Dict[str, Any]]:
    """为指定 OS 抓取系统故障及解决方法"""
    config = OS_CONFIG[os_name]
    all_items = []
    errors = []

    for site in config["sites"]:
        for tag in config["tags"]:
            if len(all_items) >= min_items * 2:  # 多抓一些用于去重后保留
                break
            try:
                questions = se_fetch_questions(site, tag, pagesize=50)
                log_agent(AGENT_NAME, f"Site={site} tag={tag}: got {len(questions)} questions")
            except Exception as e:
                errors.append(f"{site}/{tag}: {e}")
                continue

            if not questions:
                continue

            # 只取有答案的问题
            with_answers = [q for q in questions if q.get("answer_count", 0) > 0]
            qids = [q["question_id"] for q in with_answers]

            # 批量获取答案
            answers_map = {}
            if qids:
                try:
                    answers_map = se_fetch_answers(qids[:100], site)
                except Exception as e:
                    log_agent(AGENT_NAME, f"Answers fetch error for {site}/{tag}: {e}")

            for q in with_answers:
                qid = q["question_id"]
                title = strip_html_tags(q.get("title", ""))
                link = q.get("link", "")
                tags = q.get("tags", [])
                score = q.get("score", 0)
                answer_count = q.get("answer_count", 0)
                view_count = q.get("view_count", 0)

                # 获取答案内容
                answer_text = ""
                ans_list = answers_map.get(qid, [])
                if ans_list:
                    # API withbody filter 可能不总是包含body，回退到网页抓取
                    answer_text = strip_html_tags(ans_list[0].get("body", ""))
                    if not answer_text or len(answer_text) < 50:
                        # 尝试网页抓取补充
                        html = fetch_page_html(link)
                        if html:
                            answer_text = extract_answer_from_html(html)
                else:
                    # 没有API答案，尝试网页抓取
                    html = fetch_page_html(link)
                    if html:
                        answer_text = extract_answer_from_html(html)

                if not answer_text:
                    answer_text = "Refer to the original page for detailed solutions and community answers."

                item = {
                    "id": f"se-{site}-{qid}",
                    "title": title,
                    "description": f"Tags: {', '.join(tags)} | Score: {score} | Views: {view_count} | Answers: {answer_count}",
                    "solution": answer_text,
                    "source_url": link,
                    "site": site,
                    "tags": tags,
                    "score": score,
                    "answer_count": answer_count,
                }
                all_items.append(item)

            if len(all_items) >= min_items * 2:
                break
        if len(all_items) >= min_items * 2:
            break

    # 按分数排序去重
    seen_titles = set()
    unique = []
    for item in sorted(all_items, key=lambda x: x.get("score", 0), reverse=True):
        t = item.get("title", "").lower().strip()
        if t and t not in seen_titles:
            seen_titles.add(t)
            unique.append(item)
        if len(unique) >= min_items:
            break

    log_agent(AGENT_NAME, f"{os_name}: final unique items={len(unique)}")
    return unique


# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------

def build_trouble_md_items(items: List[dict], os_name: str) -> List[Dict[str, Any]]:
    section_items = []
    for item in items:
        title = item.get("title", "Untitled")
        desc = item.get("description", "")
        solution = item.get("solution", "")
        url = item.get("source_url", "")
        tags = item.get("tags", [])
        score = item.get("score", 0)
        ans_count = item.get("answer_count", 0)
        site = item.get("site", "")

        tags_str = f"Tags: {', '.join(tags)}" if tags else ""

        zh = f"""**故障现象**: {title}
**标签 / 来源**: {tags_str} | {site} | 👍 {score} | 💬 {ans_count} answers

**问题描述**:
{desc}

**解决方法 / 社区答案**:
{solution}

**参考链接**: {url}"""

        en = f"""**Issue**: {title}
**Tags / Source**: {tags_str} | {site} | 👍 {score} | 💬 {ans_count} answers

**Description**:
{desc}

**Solution / Community Answer**:
{solution}

**Reference**: {url}"""

        section_items.append({
            "zh": {"title": title, "content": zh, "source": url},
            "en": {"title": title, "content": en, "source": url},
        })

    return [{
        "heading_zh": f"{os_name.upper()} 常见故障及解决方法",
        "heading_en": f"{os_name.upper()} Common Issues & Solutions",
        "items": section_items,
    }]


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def run():
    log_agent(AGENT_NAME, "=" * 40)
    log_agent(AGENT_NAME, "Starting scheduled run")

    all_new = 0
    all_total = 0
    errors = []

    for os_name in ["windows", "linux", "macos"]:
        log_agent(AGENT_NAME, f"Processing {os_name}...")
        category = f"sys-trouble-{os_name}"

        try:
            items = fetch_troubleshooting(os_name, min_items=MIN_ITEMS)
        except Exception as e:
            errors.append(f"{os_name}: {e}")
            log_agent(AGENT_NAME, f"{os_name} fetch error: {e}")
            items = []

        new_items = filter_new_items(category, items, keep_old_methods=True)
        log_agent(AGENT_NAME, f"{os_name}: fetched={len(items)}, new={len(new_items)}")

        # 补充到展示数量
        state = __import__("utils").load_state()
        stored = list(state.get(category, {}).values())
        display_items = list(new_items)
        if len(display_items) < MIN_ITEMS:
            seen_keys = {__import__("utils").dedup_key(i) for i in new_items}
            for s in stored:
                d = s["data"]
                if __import__("utils").dedup_key(d) not in seen_keys:
                    display_items.append(d)
                    seen_keys.add(__import__("utils").dedup_key(d))
                if len(display_items) >= MIN_ITEMS:
                    break

        # 生成分类文件
        os_titles = {
            "windows": ("Windows 常见故障及解决方法", "Windows Common Issues & Solutions"),
            "linux": ("Linux 常见故障及解决方法", "Linux Common Issues & Solutions"),
            "macos": ("macOS 常见故障及解决方法", "macOS Common Issues & Solutions"),
        }
        zh_title, en_title = os_titles[os_name]

        sections = build_trouble_md_items(display_items[:max(50, len(display_items))], os_name)
        md_content = make_bilingual_md(
            title_zh=zh_title,
            title_en=en_title,
            intro_zh=f"本页面每小时自动从 Stack Exchange 社区抓取 {os_name.upper()} 平台常见故障及解决方法。",
            intro_en=f"Auto-updated hourly from Stack Exchange: common {os_name.upper()} issues and community-verified solutions.",
            sections=sections,
        )
        write_md_file(OUTPUT_DIR / f"{os_name}.md", md_content)

        all_new += len(new_items)
        all_total += len(stored)

    # 总索引
    index_lines = ["# 系统故障知识库总索引 | System Troubleshooting Knowledge Base Index", "", "| 分类 | 最新更新 | 条目数 |", "|------|----------|--------|"]
    for os_name in ["windows", "linux", "macos"]:
        cat = f"sys-trouble-{os_name}"
        state = __import__("utils").load_state()
        count = len(state.get(cat, {}))
        index_lines.append(f"| [{os_name.upper()}]({os_name}.md) | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} | {count} |")
    index_lines.extend(["", "---", "", "_自动维护 | Auto-maintained_"])
    write_md_file(OUTPUT_DIR / "index.md", "\n".join(index_lines))

    report = write_report(AGENT_NAME, all_new, all_total, errors)
    log_agent(AGENT_NAME, f"Summary: new={all_new}, total={all_total}, errors={len(errors)}")
    log_agent(AGENT_NAME, "Run complete")
    return report


if __name__ == "__main__":
    run()
