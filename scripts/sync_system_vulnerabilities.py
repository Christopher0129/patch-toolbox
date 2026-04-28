#!/usr/bin/env python3
"""
Agent: System Vulnerabilities (Windows / Linux / macOS)
每6小时按操作系统分类抓取系统漏洞及应对措施，增量更新。
A+B 方案：A=抓最新，B=翻页深挖补足50条真正新增。
数据源: NVD API (关键词过滤),
        Red Hat Security Advisories,
        Ubuntu Security Notices,
        SUSE Security,
        Microsoft Security Update Guide,
        Apple Security Updates
全部走 scrapling
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

from utils import (
    fetch_json, fetch_text, fetch_rss, log_sync, write_report,
    filter_new_items, make_bilingual_md, write_md_file,
    init_sqlite_db, get_db_path, insert_entries_sqlite, count_entries_sqlite,
    strip_html_tags, send_sync_report,
)

SYNC_NAME = "agent-system-vulnerabilities"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "system-vulnerabilities"
MIN_ITEMS = 50
MAX_DEEP_PAGES = 5

OS_KEYWORDS = {
    "windows": ["Microsoft", "Windows", "MSFT"],
    "linux": ["Linux", "Ubuntu", "Debian", "Red Hat", "CentOS", "Fedora", "SUSE", "Kernel"],
    "macos": ["Apple", "macOS", "Mac OS", "iOS"],
}


def fetch_nvd_by_keyword(keyword: str, limit: int = 50, start: int = 0) -> List[Dict[str, Any]]:
    url = (
        f"https://services.nvd.nist.gov/rest/json/cves/2.0"
        f"?keywordSearch={keyword.replace(' ', '%20')}"
        f"&resultsPerPage={limit}&startIndex={start}"
    )
    data = fetch_json(url, timeout=45)
    if not data or "vulnerabilities" not in data:
        return []

    items = []
    for v in data.get("vulnerabilities", []):
        cve = v.get("cve", {})
        cve_id = cve.get("id", "")
        descriptions = cve.get("descriptions", [])
        en_desc = ""
        for d in descriptions:
            if d.get("lang") == "en":
                en_desc = d.get("value", "")
                break
        if not en_desc and descriptions:
            en_desc = descriptions[0].get("value", "")

        cvss_score = None
        severity = "N/A"
        metrics = cve.get("metrics", {})
        for metric_type in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
            if metric_type in metrics and metrics[metric_type]:
                cvss_data = metrics[metric_type][0].get("cvssData", {})
                if "baseScore" in cvss_data:
                    cvss_score = cvss_data["baseScore"]
                    severity = cvss_data.get("baseSeverity", "N/A")
                    break

        refs = cve.get("references", [])
        ref_urls = [r.get("url", "") for r in refs[:5] if r.get("url")]

        configurations = cve.get("configurations", [])
        products = []
        for cfg in configurations:
            for node in cfg.get("nodes", []):
                for cpe in node.get("cpeMatch", []):
                    criteria = cpe.get("criteria", "")
                    if criteria:
                        parts = criteria.split(":")
                        if len(parts) >= 5:
                            vendor = parts[3]
                            product = parts[4]
                            if vendor and product:
                                products.append(f"{vendor}:{product}")
        products = list(set(products))[:5]

        items.append({
            "cve_id": cve_id,
            "title": cve_id,
            "description": en_desc,
            "cvss_score": cvss_score,
            "severity": severity,
            "references": ref_urls,
            "published": cve.get("published", ""),
            "last_modified": cve.get("lastModified", ""),
            "affected_products": products,
            "solution": f"Apply patch from vendor. Monitor {ref_urls[0] if ref_urls else 'vendor advisory'}.",
            "source_tag": "NVD",
        })
    return items


def fetch_redhat_advisories(limit: int = 20) -> List[Dict[str, Any]]:
    """Red Hat Security Advisories API"""
    url = f"https://access.redhat.com/hydra/rest/securitydata/cve.json?per_page={limit}"
    data = fetch_json(url, timeout=30)
    if not data or not isinstance(data, list):
        log_sync(SYNC_NAME, "Red Hat API returned no data")
        return []

    items = []
    for adv in data[:limit]:
        cve_id = adv.get("CVE", "")
        severity = (adv.get("severity") or "N/A").upper()
        bugzilla = adv.get("bugzilla", "")
        description = adv.get("bugzilla_description", "")
        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id} - {description[:60]}",
            "description": f"[Red Hat] {description}. Bugzilla: {bugzilla}",
            "cvss_score": None,
            "severity": severity,
            "references": [f"https://bugzilla.redhat.com/show_bug.cgi?id={bugzilla}"] if bugzilla else [],
            "published": adv.get("public_date", ""),
            "last_modified": adv.get("public_date", ""),
            "affected_products": ["Red Hat Enterprise Linux"],
            "solution": "Apply Red Hat security advisory patch via yum/dnf update.",
            "source_tag": "RedHat",
        })

    log_sync(SYNC_NAME, f"Red Hat fetched {len(items)}")
    return items


def fetch_ubuntu_notices(limit: int = 20) -> List[Dict[str, Any]]:
    """Ubuntu Security Notices RSS"""
    entries = fetch_rss("https://ubuntu.com/security/notices/rss.xml", timeout=25)
    if entries is None:
        log_sync(SYNC_NAME, "Ubuntu notices fetch returned None")
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = entry.get("description", "")
        cve_match = __import__("re").findall(r"CVE-\d{4}-\d{4,}", title + desc)
        cve_id = cve_match[0] if cve_match else ""

        items.append({
            "cve_id": cve_id or f"USN-{link.split('/')[-1]}",
            "title": f"[Ubuntu] {title}",
            "description": strip_html_tags(desc)[:400],
            "cvss_score": None,
            "severity": "UPDATE",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "affected_products": ["Ubuntu"],
            "solution": "Run 'apt update && apt upgrade' to apply security patches.",
            "source_tag": "Ubuntu",
        })

    log_sync(SYNC_NAME, f"Ubuntu fetched {len(items)}")
    return items


def fetch_suse_security(limit: int = 15) -> List[Dict[str, Any]]:
    """SUSE Security Announcements RSS"""
    entries = fetch_rss("https://www.suse.com/support/security/rss/announcements.xml", timeout=25)
    if entries is None:
        log_sync(SYNC_NAME, "SUSE security fetch returned None")
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = strip_html_tags(entry.get("description", ""))[:400]
        cve_match = __import__("re").findall(r"CVE-\d{4}-\d{4,}", title + desc)
        cve_id = cve_match[0] if cve_match else ""

        items.append({
            "cve_id": cve_id or f"SUSE-{link.split('/')[-1]}",
            "title": f"[SUSE] {title}",
            "description": desc,
            "cvss_score": None,
            "severity": "UPDATE",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "affected_products": ["SUSE Linux Enterprise"],
            "solution": "Apply SUSE security patch via zypper or YaST Online Update.",
            "source_tag": "SUSE",
        })

    log_sync(SYNC_NAME, f"SUSE fetched {len(items)}")
    return items


def fetch_microsoft_security(limit: int = 20) -> List[Dict[str, Any]]:
    """Microsoft Security Update Guide API"""
    url = "https://api.msrc.microsoft.com/update-guide/v1.0/updates"
    data = fetch_json(url, timeout=30)
    if not data or not isinstance(data, list):
        log_sync(SYNC_NAME, "Microsoft Security API returned no data")
        return []

    items = []
    for update in data[:limit]:
        cve_id = update.get("cveNumber", "")
        title = update.get("cveTitle", "")
        severity = (update.get("severity") or "N/A").upper()
        description = update.get("cveDescription", "")
        kb_articles = update.get("kbArticles", [])
        refs = [f"https://support.microsoft.com/kb/{kb.get('kbNumber', '')}" for kb in kb_articles if kb.get("kbNumber")]

        items.append({
            "cve_id": cve_id,
            "title": f"[Microsoft] {cve_id} - {title}",
            "description": f"[Microsoft] {description[:400]}",
            "cvss_score": None,
            "severity": severity,
            "references": refs,
            "published": update.get("releaseDate", ""),
            "last_modified": update.get("releaseDate", ""),
            "affected_products": [update.get("product", "Microsoft Windows")],
            "solution": f"Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.",
            "source_tag": "Microsoft",
        })

    log_sync(SYNC_NAME, f"Microsoft fetched {len(items)}")
    return items


def fetch_apple_security(limit: int = 15) -> List[Dict[str, Any]]:
    """Apple Security Updates page (scrapling headless)"""
    html = fetch_text("https://support.apple.com/en-us/HT201222", timeout=30)
    if not html:
        log_sync(SYNC_NAME, "Apple security fetch returned None")
        return []

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    items = []
    # Apple security page has article links
    for link in soup.find_all("a", href=re.compile(r"/HT\d+"))[:limit]:
        title = link.get_text(strip=True)
        href = link.get("href", "")
        if not title:
            continue
        full_url = f"https://support.apple.com{href}" if href.startswith("/") else href
        cve_match = __import__("re").findall(r"CVE-\d{4}-\d{4,}", title)
        cve_id = cve_match[0] if cve_match else ""

        items.append({
            "cve_id": cve_id or f"APPLE-{href.split('/')[-1]}",
            "title": f"[Apple] {title}",
            "description": f"Apple security update. Refer to support article for affected products and patch instructions.",
            "cvss_score": None,
            "severity": "UPDATE",
            "references": [full_url],
            "published": "",
            "last_modified": "",
            "affected_products": ["macOS", "iOS", "iPadOS", "watchOS", "tvOS"],
            "solution": "Update to the latest Apple software version via System Settings > Software Update.",
            "source_tag": "Apple",
        })

    log_sync(SYNC_NAME, f"Apple fetched {len(items)}")
    return items


def fetch_os_vulns_deep(os_name: str, min_items: int = 50, max_pages: int = 5) -> List[Dict[str, Any]]:
    keywords = OS_KEYWORDS.get(os_name, [os_name])
    all_items = []

    for keyword in keywords:
        start = 0
        for page in range(max_pages):
            batch = fetch_nvd_by_keyword(keyword, limit=50, start=start)
            if not batch:
                break
            all_items.extend(batch)
            start += 50
            if len(all_items) >= min_items:
                break
        if len(all_items) >= min_items:
            break

    # 补充 OS 专属源
    extra_sources = {
        "windows": [lambda: fetch_microsoft_security(20)],
        "linux": [fetch_redhat_advisories, fetch_ubuntu_notices, fetch_suse_security],
        "macos": [fetch_apple_security],
    }
    for fn in extra_sources.get(os_name, []):
        try:
            batch = fn()
            all_items.extend(batch)
        except Exception as e:
            log_sync(SYNC_NAME, f"Extra source error for {os_name}: {e}")

    seen = set()
    unique = []
    for item in all_items:
        key = item.get("cve_id", "")
        if key and key not in seen:
            seen.add(key)
            unique.append(item)

    log_sync(SYNC_NAME, f"Fetched {len(unique)} unique items for {os_name}")
    return unique


def build_os_md_items(items: List[dict], os_name: str) -> List[Dict[str, Any]]:
    section_items = []
    for item in items:
        cve_id = item.get("cve_id", "N/A")
        desc = item.get("description", "")
        severity = item.get("severity", "N/A")
        cvss = item.get("cvss_score")
        products = item.get("affected_products", [])
        refs = item.get("references", [])
        solution = item.get("solution", "")
        source_tag = item.get("source_tag", "NVD")

        cvss_str = f"CVSS: {cvss}" if cvss is not None else ""
        products_str = f"受影响产品: {', '.join(products)}" if products else ""
        refs_str = "\n".join([f"- {r}" for r in refs]) if refs else ""

        zh = f"""**CVE编号**: {cve_id} [{source_tag}]
**严重程度**: {severity} {cvss_str}
{products_str}

**漏洞描述**:
{desc}

**应对措施**:
{solution}

**参考链接**:
{refs_str}"""

        en = f"""**CVE ID**: {cve_id} [{source_tag}]
**Severity**: {severity} {cvss_str}
**Affected Products**: {', '.join(products) if products else 'N/A'}

**Description**:
{desc}

**Mitigation**:
{solution}

**References**:
{refs_str}"""

        section_items.append({
            "zh": {"title": f"{cve_id} ({severity})", "content": zh, "source": refs[0] if refs else source_tag},
            "en": {"title": f"{cve_id} ({severity})", "content": en, "source": refs[0] if refs else source_tag},
        })

    return [{
        "heading_zh": f"{os_name.upper()} 漏洞列表",
        "heading_en": f"{os_name.upper()} Vulnerability List",
        "items": section_items,
    }]


def run():
    start_time = __import__("time").time()
    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting scheduled run (A+B deep-paging)")

    all_new = 0
    errors = []
    os_counts = {}

    for os_name in ["windows", "linux", "macos"]:
        log_sync(SYNC_NAME, f"Processing {os_name}...")
        category = f"sys-vuln-{os_name}"
        db_path = get_db_path(category)
        conn = init_sqlite_db(db_path)

        # ---- A: 先抓最新（第1页） ----
        try:
            items = fetch_os_vulns_deep(os_name, min_items=MIN_ITEMS, max_pages=1)
        except Exception as e:
            errors.append(f"{os_name}-A: {e}")
            log_sync(SYNC_NAME, f"{os_name} fetch-A error: {e}")
            items = []

        # ---- 写入 SQLite（A阶段） ----
        new_a = insert_entries_sqlite(conn, items, platform=os_name)
        log_sync(SYNC_NAME, f"{os_name} Phase-A: fetched={len(items)}, new={new_a}")

        # ---- B: 翻页深挖 ----
        total_new = new_a
        if total_new < MIN_ITEMS:
            log_sync(SYNC_NAME, f"{os_name} A-phase new ({total_new}) < {MIN_ITEMS}, start deep-paging")
            for page in range(1, MAX_DEEP_PAGES + 1):
                if total_new >= MIN_ITEMS:
                    break
                try:
                    batch = fetch_os_vulns_deep(os_name, min_items=MIN_ITEMS * (page + 1), max_pages=page + 1)
                    batch_new = insert_entries_sqlite(conn, batch, platform=os_name)
                    total_new += batch_new
                    log_sync(SYNC_NAME, f"{os_name} Phase-B page={page}: batch_new={batch_new}, total_new={total_new}")
                except Exception as e:
                    errors.append(f"{os_name}-B-{page}: {e}")
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
