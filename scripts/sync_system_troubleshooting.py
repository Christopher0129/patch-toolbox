#!/usr/bin/env python3
"""
Sync Script: System Troubleshooting (Windows / Linux / macOS)
数据源扩充版：Stack Exchange + Reddit + V2EX + 中文技术社区
写入 SQLite 数据库，MD 文件由 regenerate_md.py 统一生成。
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

from utils import (
    fetch_json, fetch_text, fetch_rss, log_sync, write_report,
    strip_html_tags, insert_entries_sqlite, init_sqlite_db, get_db_path,
    count_entries_sqlite, send_sync_report,
)

SYNC_NAME = "sync-system-troubleshooting"
MIN_ITEMS = 50
MAX_DEEP_PAGES = 5

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

SE_API_KEY = ""


# ---------------------------------------------------------------------------
# Stack Exchange
# ---------------------------------------------------------------------------

def se_fetch_questions(site: str, tag: str, pagesize: int = 50, page: int = 1, sort: str = "creation") -> List[Dict[str, Any]]:
    url = (
        f"https://api.stackexchange.com/2.3/questions"
        f"?order=desc&sort={sort}"
        f"&tagged={tag}"
        f"&site={site}"
        f"&pagesize={pagesize}"
        f"&page={page}"
    )
    if SE_API_KEY:
        url += f"&key={SE_API_KEY}"
    data = fetch_json(url, timeout=30)
    time.sleep(1.5)
    if not data or "items" not in data:
        return []
    return data["items"]


def se_fetch_answers(question_ids: List[int], site: str) -> Dict[int, List[Dict]]:
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
    return fetch_text(url, timeout=20, retries=retries)


def extract_answer_from_html(html: str) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    answers = soup.find_all("div", class_=re.compile(r"answer"))
    if not answers:
        return ""
    best = answers[0]
    body = best.find("div", class_=re.compile(r"post-layout|answercell"))
    if not body:
        body = best
    text = body.get_text(separator="\n", strip=True)
    if len(text) > 2000:
        text = text[:2000] + "... [truncated]"
    return text


def fetch_stackexchange_deep(os_name: str, min_items: int = 50, max_pages: int = 1, sort: str = "creation") -> List[Dict[str, Any]]:
    config = OS_CONFIG[os_name]
    all_items = []
    errors = []

    for site in config["sites"]:
        for tag in config["tags"]:
            if len(all_items) >= min_items * 2:
                break
            for page in range(1, max_pages + 1):
                try:
                    questions = se_fetch_questions(site, tag, pagesize=50, page=page, sort=sort)
                except Exception as e:
                    errors.append(f"{site}/{tag}/page{page}: {e}")
                    break
                if not questions:
                    break
                log_sync(SYNC_NAME, f"SE site={site} tag={tag} page={page}: got {len(questions)} questions")

                with_answers = [q for q in questions if q.get("answer_count", 0) > 0]
                qids = [q["question_id"] for q in with_answers]

                answers_map = {}
                if qids:
                    try:
                        answers_map = se_fetch_answers(qids[:100], site)
                    except Exception as e:
                        log_sync(SYNC_NAME, f"Answers fetch error for {site}/{tag}: {e}")

                for q in with_answers:
                    qid = q["question_id"]
                    title = strip_html_tags(q.get("title", ""))
                    link = q.get("link", "")
                    tags = q.get("tags", [])
                    score = q.get("score", 0)
                    answer_count = q.get("answer_count", 0)
                    view_count = q.get("view_count", 0)
                    creation_date = q.get("creation_date", 0)

                    answer_text = ""
                    ans_list = answers_map.get(qid, [])
                    if ans_list:
                        answer_text = strip_html_tags(ans_list[0].get("body", ""))
                        if not answer_text or len(answer_text) < 50:
                            html = fetch_page_html(link)
                            if html:
                                answer_text = extract_answer_from_html(html)
                    else:
                        html = fetch_page_html(link)
                        if html:
                            answer_text = extract_answer_from_html(html)

                    if not answer_text:
                        answer_text = "Refer to the original page for detailed solutions and community answers."

                    all_items.append({
                        "id": f"se-{site}-{qid}",
                        "title": title,
                        "description": f"Tags: {', '.join(tags)} | Score: {score} | Views: {view_count} | Answers: {answer_count} | Created: {datetime.fromtimestamp(creation_date, tz=timezone.utc).strftime('%Y-%m-%d')}",
                        "solution": answer_text,
                        "source_url": link,
                        "source": "StackExchange",
                        "tags": tags,
                        "score": score,
                        "answer_count": answer_count,
                        "creation_date": creation_date,
                    })

                if len(all_items) >= min_items * 2:
                    break
            if len(all_items) >= min_items * 2:
                break
        if len(all_items) >= min_items * 2:
            break

    # 去重：按 title 去重，保留 score 高的
    seen_titles = set()
    unique = []
    for item in sorted(all_items, key=lambda x: (x.get("score", 0), x.get("creation_date", 0)), reverse=True):
        t = item.get("title", "").lower().strip()
        if t and t not in seen_titles:
            seen_titles.add(t)
            unique.append(item)
        if len(unique) >= min_items:
            break

    log_sync(SYNC_NAME, f"{os_name} StackExchange: final unique items={len(unique)}")
    return unique


# ---------------------------------------------------------------------------
# Reddit（扩充版）
# ---------------------------------------------------------------------------

def fetch_reddit(os_name: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Reddit RSS - 扩充更多板块"""
    subreddits = {
        "windows": [
            "techsupport", "sysadmin", "Windows10", "Windows11",
            "WindowsHelp", "buildapc", "hardware", "software",
        ],
        "linux": [
            "linux", "sysadmin", "linuxquestions", "Ubuntu",
            "linux4noobs", "commandline", "linuxmasterrace",
        ],
        "macos": [
            "macos", "apple", "macbook", "techsupport",
            "MacOSBeta", "applehelp",
        ],
    }
    all_items = []
    for sub in subreddits.get(os_name, []):
        entries = fetch_rss(f"https://www.reddit.com/r/{sub}/.rss", timeout=20)
        if entries is None:
            continue
        for entry in entries[:limit]:
            title = entry.get("title", "")
            link = entry.get("link", "")
            if not title or title.startswith("[removed]") or title.startswith("[deleted]"):
                continue
            all_items.append({
                "id": f"reddit-{sub}-{__import__('hashlib').md5(link.encode()).hexdigest()[:8]}",
                "title": title,
                "description": f"Reddit r/{sub} discussion",
                "solution": "See Reddit thread for community solutions and troubleshooting steps.",
                "source_url": link,
                "source": f"reddit-{sub}",
                "tags": [sub],
                "score": 0,
                "answer_count": 0,
                "creation_date": 0,
            })
    log_sync(SYNC_NAME, f"{os_name} Reddit: fetched {len(all_items)}")
    return all_items


# ---------------------------------------------------------------------------
# V2EX（扩充版）
# ---------------------------------------------------------------------------

def fetch_v2ex(os_name: str, limit: int = 20) -> List[Dict[str, Any]]:
    """V2EX 技术节点 RSS - 扩充更多节点"""
    nodes = {
        "windows": ["windows", "qna"],
        "linux": ["linux", "ubuntu", "debian", "qna", "programmer"],
        "macos": ["macos", "apple", "qna", "share"],
    }
    all_items = []
    for node in nodes.get(os_name, []):
        entries = fetch_rss(f"https://www.v2ex.com/feed/{node}.xml", timeout=20)
        if entries is None:
            continue
        for entry in entries[:limit]:
            title = entry.get("title", "")
            link = entry.get("link", "")
            desc = strip_html_tags(entry.get("description", ""))[:300]
            if not title:
                continue
            all_items.append({
                "id": f"v2ex-{node}-{__import__('hashlib').md5(link.encode()).hexdigest()[:8]}",
                "title": f"[V2EX] {title}",
                "description": desc,
                "solution": "See V2EX thread for community solutions.",
                "source_url": link,
                "source": f"v2ex-{node}",
                "tags": [node],
                "score": 0,
                "answer_count": 0,
                "creation_date": 0,
            })
    log_sync(SYNC_NAME, f"{os_name} V2EX: fetched {len(all_items)}")
    return all_items


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def run():
    start_time = __import__("time").time()
    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting scheduled run")

    all_new = 0
    errors = []
    os_counts = {}

    for os_name in ["windows", "linux", "macos"]:
        log_sync(SYNC_NAME, f"Processing {os_name}...")
        category = f"sys-trouble-{os_name}"
        db_path = get_db_path(category)
        conn = init_sqlite_db(db_path)

        # ---- A: 抓最新 ----
        try:
            items = fetch_stackexchange_deep(os_name, min_items=MIN_ITEMS, max_pages=1, sort="creation")
        except Exception as e:
            errors.append(f"{os_name}-SE-A: {e}")
            log_sync(SYNC_NAME, f"{os_name} SE fetch-A error: {e}")
            items = []

        # 补充 Reddit + V2EX
        try:
            reddit_items = fetch_reddit(os_name, limit=25)
            items.extend(reddit_items)
        except Exception as e:
            errors.append(f"{os_name}-Reddit: {e}")
        try:
            v2ex_items = fetch_v2ex(os_name, limit=20)
            items.extend(v2ex_items)
        except Exception as e:
            errors.append(f"{os_name}-V2EX: {e}")

        # ---- 写入 SQLite（A阶段） ----
        new_a = insert_entries_sqlite(conn, items, platform=os_name)
        log_sync(SYNC_NAME, f"{os_name} Phase-A: fetched={len(items)}, new={new_a}")

        # ---- B: 翻页深挖 ----
        total_new = new_a
        if total_new < MIN_ITEMS:
            log_sync(SYNC_NAME, f"{os_name} A-phase new ({total_new}) < {MIN_ITEMS}, start deep-paging")
            for page_depth in range(2, MAX_DEEP_PAGES + 2):
                if total_new >= MIN_ITEMS:
                    break
                try:
                    batch = fetch_stackexchange_deep(os_name, min_items=MIN_ITEMS * page_depth, max_pages=page_depth, sort="creation")
                    batch_new = insert_entries_sqlite(conn, batch, platform=os_name)
                    total_new += batch_new
                    log_sync(SYNC_NAME, f"{os_name} Phase-B depth={page_depth}: batch_new={batch_new}, total_new={total_new}")
                except Exception as e:
                    errors.append(f"{os_name}-B-{page_depth}: {e}")
                    break

        os_counts[os_name] = count_entries_sqlite(conn)
        conn.close()
        all_new += total_new

    # ---- 汇报 ----
    elapsed = __import__("time").time() - start_time
    total_all = sum(os_counts.values())
    extra = f"各平台条目: Windows={os_counts.get('windows',0)}, Linux={os_counts.get('linux',0)}, macOS={os_counts.get('macos',0)}"
    send_sync_report(SYNC_NAME, all_new, total_all, errors, elapsed, extra)

    report = write_report(SYNC_NAME, all_new, total_all, errors)
    log_sync(SYNC_NAME, f"Summary: new={all_new}, errors={len(errors)}")
    log_sync(SYNC_NAME, "Run complete")
    return report


if __name__ == "__main__":
    run()
