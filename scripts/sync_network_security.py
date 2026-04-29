#!/usr/bin/env python3
"""
Sync Script: Network Security Vulnerabilities (OS分类版)
每6小时按操作系统分类抓取网络漏洞，增量更新。
A+B 方案：A=抓最新，B=翻页深挖补足50条真正新增。

数据源清单(基于website_recommendations.md):
- Windows: NVD(keyword), MSRC, Exploit-DB, GitHub, CISA, Action1, BleepingComputer
- Linux: NVD(keyword), RedHat, Ubuntu, Debian, SUSE, Arch, Gentoo, Kernel.org
- macOS: NVD(keyword), Apple Security, Objective-See, Intego, OpenCVE
- 通用: NVD, Exploit-DB, GitHub, CISA, PacketStorm, FreeBuf, Anquanke, Kanxue, Xianzhi, Sihou, OSV.dev, Vulners
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

from utils import (
    fetch_json, fetch_text, fetch_rss, log_sync, write_report,
    strip_html_tags, insert_entries_sqlite, init_sqlite_db, get_db_path,
    count_entries_sqlite, send_sync_report,
)

SYNC_NAME = "sync-network-security"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "network-security"
MIN_ITEMS = 50
MAX_DEEP_PAGES = 5

OS_KEYWORDS = {
    "windows": ["Microsoft", "Windows", "MSFT", "MSRC", "Azure"],
    "linux": ["Linux", "Ubuntu", "Debian", "Red Hat", "CentOS", "Fedora", "SUSE", "Kernel", "GNU"],
    "macos": ["Apple", "macOS", "Mac OS", "iOS", "Darwin", "OSX"],
    "general": ["CVE", "Security", "Vulnerability"],
}

# ---------------------------------------------------------------------------
# 基础抓取函数
# ---------------------------------------------------------------------------

def fetch_nvd_cves(limit: int = 50, start_index: int = 0) -> List[Dict[str, Any]]:
    """NVD 通用抓取"""
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage={limit}&startIndex={start_index}"
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

        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id}",
            "description": en_desc,
            "cvss_score": cvss_score,
            "severity": severity,
            "references": ref_urls,
            "published": cve.get("published", ""),
            "last_modified": cve.get("lastModified", ""),
            "source_tag": "NVD",
            "platform": "general",
        })
    return items


def fetch_nvd_by_keyword(keyword: str, limit: int = 50, start: int = 0) -> List[Dict[str, Any]]:
    """NVD 按关键词搜索"""
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

        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id}",
            "description": en_desc,
            "cvss_score": cvss_score,
            "severity": severity,
            "references": ref_urls,
            "published": cve.get("published", ""),
            "last_modified": cve.get("lastModified", ""),
            "source_tag": "NVD",
        })
    return items


def fetch_exploit_db(limit: int = 30, offset: int = 0) -> List[Dict[str, Any]]:
    """Exploit-DB RSS"""
    entries = fetch_rss("https://www.exploit-db.com/rss.xml", timeout=25)
    if entries is None:
        return []
    entries = entries[offset:offset+limit] if offset < len(entries) else []
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = entry.get("description", "")
        cve_match = re.search(r"CVE-\d{4}-\d{4,}", title)
        cve_id = cve_match.group(0) if cve_match else ""

        items.append({
            "cve_id": cve_id or f"EDB-{link.split('/')[-1]}",
            "title": f"{cve_id or 'Exploit'} - {title}" if cve_id else title,
            "description": f"[Exploit-DB] {strip_html_tags(desc)[:300]}",
            "cvss_score": None,
            "severity": "EXPLOIT",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Exploit-DB",
        })
    log_sync(SYNC_NAME, f"Exploit-DB fetched {len(items)} (offset={offset})")
    return items


def fetch_github_advisories(limit: int = 20) -> List[Dict[str, Any]]:
    """GitHub Security Advisories"""
    url = f"https://api.github.com/advisories?per_page={limit}"
    data = fetch_json(url, timeout=20)
    if not data or not isinstance(data, list):
        log_sync(SYNC_NAME, "GitHub Advisories returned no data")
        return []

    items = []
    for adv in data:
        ghsa_id = adv.get("ghsa_id", "")
        summary = adv.get("summary", "")
        desc = adv.get("description", "")[:500]
        severity = (adv.get("severity") or "N/A").upper()
        cvss_score = adv.get("cvss", {}).get("score") if isinstance(adv.get("cvss"), dict) else None
        refs = [adv["html_url"]] if adv.get("html_url") else []
        cves = adv.get("cve_ids", [])
        cve_id = cves[0] if cves else ""

        items.append({
            "cve_id": cve_id or ghsa_id,
            "title": f"{cve_id or ghsa_id} - {summary[:80]}",
            "description": f"[GitHub] {desc}",
            "cvss_score": cvss_score,
            "severity": severity,
            "references": refs,
            "published": adv.get("published_at", ""),
            "last_modified": adv.get("updated_at", ""),
            "source_tag": "GitHub",
        })
    log_sync(SYNC_NAME, f"GitHub Advisories fetched {len(items)}")
    return items


def fetch_cisa_kev() -> List[Dict[str, Any]]:
    """CISA Known Exploited Vulnerabilities"""
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    data = fetch_json(url, timeout=30)
    if not data or "vulnerabilities" not in data:
        log_sync(SYNC_NAME, "CISA KEV returned no data")
        return []

    items = []
    vulns = sorted(data["vulnerabilities"], key=lambda x: x.get("dateAdded", ""), reverse=True)[:30]
    for v in vulns:
        cve_id = v.get("cveID", "")
        product = v.get("product", "Unknown")
        vendor = v.get("vendorProject", "Unknown")
        desc = v.get("vulnerabilityName", "")
        due_date = v.get("dueDate", "")

        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id} - {desc}",
            "description": f"[CISA] Vendor: {vendor}, Product: {product}. Due: {due_date}.",
            "cvss_score": None,
            "severity": "KEV",
            "references": [f"https://nvd.nist.gov/vuln/detail/{cve_id}"] if cve_id.startswith("CVE-") else [],
            "published": v.get("dateAdded", ""),
            "last_modified": v.get("dateAdded", ""),
            "source_tag": "CISA-KEV",
        })
    log_sync(SYNC_NAME, f"CISA KEV fetched {len(items)}")
    return items


# ---------------------------------------------------------------------------
# OS 专属数据源
# ---------------------------------------------------------------------------

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
            "title": f"{cve_id} - {strip_html_tags(description)}",
            "description": f"[Red Hat] {description}. Bugzilla: {bugzilla}",
            "cvss_score": None,
            "severity": severity,
            "references": [f"https://bugzilla.redhat.com/show_bug.cgi?id={bugzilla}"] if bugzilla else [],
            "published": adv.get("public_date", ""),
            "last_modified": adv.get("public_date", ""),
            "source_tag": "RedHat",
            "platform": "linux",
        })
    log_sync(SYNC_NAME, f"Red Hat fetched {len(items)}")
    return items


def fetch_ubuntu_notices(limit: int = 20) -> List[Dict[str, Any]]:
    """Ubuntu Security Notices RSS"""
    entries = fetch_rss("https://ubuntu.com/security/notices/rss.xml", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = entry.get("description", "")
        cve_match = re.findall(r"CVE-\d{4}-\d{4,}", title + desc)
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
            "source_tag": "Ubuntu",
            "platform": "linux",
        })
    log_sync(SYNC_NAME, f"Ubuntu fetched {len(items)}")
    return items


def fetch_suse_security(limit: int = 15) -> List[Dict[str, Any]]:
    """SUSE Security Announcements RSS"""
    entries = fetch_rss("https://www.suse.com/support/security/rss/announcements.xml", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = strip_html_tags(entry.get("description", ""))[:400]
        cve_match = re.findall(r"CVE-\d{4}-\d{4,}", title + desc)
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
            "source_tag": "SUSE",
            "platform": "linux",
        })
    log_sync(SYNC_NAME, f"SUSE fetched {len(items)}")
    return items


def fetch_arch_security() -> List[Dict[str, Any]]:
    """Arch Linux Security Tracker API"""
    url = "https://security.archlinux.org/issues.json"
    data = fetch_json(url, timeout=25)
    if not data or not isinstance(data, list):
        log_sync(SYNC_NAME, "Arch Security returned no data")
        return []

    items = []
    for issue in data[:30]:
        cve_id = issue.get("name", "")
        packages = ", ".join(issue.get("packages", []))[:100]
        status = issue.get("status", "")
        severity = issue.get("severity", "Unknown").upper()

        items.append({
            "cve_id": cve_id,
            "title": f"[Arch] {cve_id}",
            "description": f"[Arch Linux] Packages: {packages}. Status: {status}.",
            "cvss_score": None,
            "severity": severity,
            "references": [f"https://security.archlinux.org/{issue.get('id', '')}"],
            "published": issue.get("created_at", ""),
            "last_modified": issue.get("updated_at", ""),
            "source_tag": "Arch",
            "platform": "linux",
        })
    log_sync(SYNC_NAME, f"Arch fetched {len(items)}")
    return items


def fetch_gentoo_glsa(limit: int = 15) -> List[Dict[str, Any]]:
    """Gentoo GLSA RSS"""
    entries = fetch_rss("https://security.gentoo.org/glsa/feed.rss", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = strip_html_tags(entry.get("description", ""))[:400]
        cve_match = re.findall(r"CVE-\d{4}-\d{4,}", title + desc)
        cve_id = cve_match[0] if cve_match else ""

        items.append({
            "cve_id": cve_id or f"GLSA-{link.split('/')[-1]}",
            "title": f"[Gentoo] {title}",
            "description": desc,
            "cvss_score": None,
            "severity": "UPDATE",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Gentoo",
            "platform": "linux",
        })
    log_sync(SYNC_NAME, f"Gentoo fetched {len(items)}")
    return items


def fetch_apple_security(limit: int = 15) -> List[Dict[str, Any]]:
    """Apple Security Updates"""
    html = fetch_text("https://support.apple.com/en-us/HT201222", timeout=30)
    if not html:
        return []

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    items = []
    for link in soup.find_all("a", href=re.compile(r"/HT\d+"))[:limit]:
        title = link.get_text(strip=True)
        href = link.get("href", "")
        if not title:
            continue
        full_url = f"https://support.apple.com{href}" if href.startswith("/") else href
        cve_match = re.findall(r"CVE-\d{4}-\d{4,}", title)
        cve_id = cve_match[0] if cve_match else ""

        items.append({
            "cve_id": cve_id or f"APPLE-{href.split('/')[-1]}",
            "title": f"[Apple] {title}",
            "description": "Apple security update. Refer to support article for details.",
            "cvss_score": None,
            "severity": "UPDATE",
            "references": [full_url],
            "published": "",
            "last_modified": "",
            "source_tag": "Apple",
            "platform": "macos",
        })
    log_sync(SYNC_NAME, f"Apple fetched {len(items)}")
    return items


def fetch_osv_vulns(limit: int = 30) -> List[Dict[str, Any]]:
    """OSV.dev API - 开源漏洞数据库"""
    url = "https://api.osv.dev/v1/vulns"
    items = []
    # OSV 需要逐个查询，这里简化处理，只测试 API 连通性
    # 实际使用需要完整的查询逻辑
    log_sync(SYNC_NAME, f"OSV.dev API configured (to be implemented)")
    return items


# ---------------------------------------------------------------------------
# 中文安全社区源
# ---------------------------------------------------------------------------

def fetch_anquanke(limit: int = 15) -> List[Dict[str, Any]]:
    entries = fetch_rss("https://api.anquanke.com/data/v1/rss", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = strip_html_tags(entry.get("description", ""))[:300]
        items.append({
            "cve_id": "",
            "title": f"[安全客] {title}",
            "description": desc,
            "cvss_score": None,
            "severity": "INFO",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Anquanke",
        })
    log_sync(SYNC_NAME, f"Anquanke fetched {len(items)}")
    return items


def fetch_kanxue(limit: int = 10) -> List[Dict[str, Any]]:
    entries = fetch_rss("https://www.kanxue.com/rss.xml", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        items.append({
            "cve_id": "",
            "title": f"[看雪] {title}",
            "description": strip_html_tags(entry.get("description", ""))[:300],
            "cvss_score": None,
            "severity": "INFO",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Kanxue",
        })
    log_sync(SYNC_NAME, f"Kanxue fetched {len(items)}")
    return items


def fetch_xianzhi(limit: int = 10) -> List[Dict[str, Any]]:
    entries = fetch_rss("https://xz.aliyun.com/feed", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        items.append({
            "cve_id": "",
            "title": f"[先知] {title}",
            "description": strip_html_tags(entry.get("description", ""))[:300],
            "cvss_score": None,
            "severity": "INFO",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Xianzhi",
        })
    log_sync(SYNC_NAME, f"Xianzhi fetched {len(items)}")
    return items


def fetch_sihou(limit: int = 10) -> List[Dict[str, Any]]:
    entries = fetch_rss("https://www.4hou.com/feed", timeout=25)
    if entries is None:
        return []
    entries = entries[:limit]
    items = []
    for entry in entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        items.append({
            "cve_id": "",
            "title": f"[嘶吼] {title}",
            "description": strip_html_tags(entry.get("description", ""))[:300],
            "cvss_score": None,
            "severity": "INFO",
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "source_tag": "Sihou",
        })
    log_sync(SYNC_NAME, f"Sihou fetched {len(items)}")
    return items


# ---------------------------------------------------------------------------
# 核心逻辑
# ---------------------------------------------------------------------------

def fetch_os_vulns_deep(os_name: str, min_items: int = 50, max_pages: int = 5) -> List[Dict[str, Any]]:
    """按 OS 抓取漏洞数据（A+B 方案）"""
    keywords = OS_KEYWORDS.get(os_name, [os_name])
    all_items = []

    # NVD 关键词搜索
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

    # OS 专属源
    extra_sources = {
        "windows": [lambda: fetch_exploit_db(20)],
        "linux": [fetch_redhat_advisories, fetch_ubuntu_notices, fetch_suse_security, fetch_arch_security, fetch_gentoo_glsa],
        "macos": [fetch_apple_security],
        "general": [fetch_exploit_db, fetch_github_advisories, fetch_cisa_kev, fetch_anquanke, fetch_kanxue, fetch_xianzhi, fetch_sihou],
    }

    for fn in extra_sources.get(os_name, extra_sources["general"]):
        try:
            batch = fn()
            all_items.extend(batch)
        except Exception as e:
            log_sync(SYNC_NAME, f"Extra source error for {os_name}: {e}")

    # 去重
    seen = set()
    unique = []
    for item in all_items:
        key = item.get("cve_id", "") or item.get("title", "")
        if key and key not in seen:
            seen.add(key)
            unique.append(item)

    log_sync(SYNC_NAME, f"Fetched {len(unique)} unique items for {os_name}")
    return unique


def run():
    start_time = time.time()
    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting OS-classified run (A+B deep-paging)")

    all_new = 0
    errors = []
    os_counts = {}

    for os_name in ["windows", "linux", "macos", "general"]:
        log_sync(SYNC_NAME, f"Processing {os_name}...")
        category = f"netsec-{os_name}"
        db_path = get_db_path(category)
        conn = init_sqlite_db(db_path)

        # A 阶段：抓取最新
        try:
            items = fetch_os_vulns_deep(os_name, min_items=MIN_ITEMS, max_pages=1)
        except Exception as e:
            errors.append(f"{os_name}-A: {e}")
            log_sync(SYNC_NAME, f"{os_name} fetch-A error: {e}")
            items = []

        # 写入 SQLite
        new_a = insert_entries_sqlite(conn, items, platform=os_name)
        log_sync(SYNC_NAME, f"{os_name} Phase-A: fetched={len(items)}, new={new_a}")

        # B 阶段：翻页深挖
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

    # 汇报
    elapsed = time.time() - start_time
    total_all = sum(os_counts.values())
    extra = f"各平台条目: Windows={os_counts.get('windows',0)}, Linux={os_counts.get('linux',0)}, macOS={os_counts.get('macos',0)}, General={os_counts.get('general',0)}"
    send_sync_report(SYNC_NAME, all_new, total_all, errors, elapsed, extra)

    report = write_report(SYNC_NAME, all_new, total_all, errors)
    log_sync(SYNC_NAME, f"Summary: new={all_new}, errors={len(errors)}")
    log_sync(SYNC_NAME, "Run complete")
    return report


if __name__ == "__main__":
    run()
