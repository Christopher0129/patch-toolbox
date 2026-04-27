#!/usr/bin/env python3
"""
Agent: Network Security Vulnerabilities
每小时抓取网络安全漏洞及应对措施，增量更新。
数据源: NVD API, Exploit-DB RSS, GitHub Security Advisories, CISA KEV
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import feedparser
import requests
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

from utils import (
    fetch_json, fetch_text, log_agent, write_report,
    filter_new_items, make_bilingual_md, write_md_file, strip_html_tags,
)

AGENT_NAME = "agent-network-security"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "network-security"
MIN_ITEMS = 50

# ---------------------------------------------------------------------------
# 数据源抓取
# ---------------------------------------------------------------------------

def fetch_nvd_cves(limit: int = 50) -> List[Dict[str, Any]]:
    """从 NVD API 抓取最新 CVE"""
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage={limit}&startIndex=0"
    data = fetch_json(url, timeout=45)
    if not data or "vulnerabilities" not in data:
        log_agent(AGENT_NAME, "NVD API returned no data")
        return []

    items = []
    for v in data["vulnerabilities"]:
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

        weaknesses = cve.get("weaknesses", [])
        cwes = []
        for w in weaknesses:
            for d in w.get("description", []):
                if d.get("value", "").startswith("CWE-"):
                    cwes.append(d["value"])

        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id}",
            "description": en_desc,
            "cvss_score": cvss_score,
            "severity": severity,
            "cwes": cwes,
            "references": ref_urls,
            "published": cve.get("published", ""),
            "last_modified": cve.get("lastModified", ""),
            "source_tag": "NVD",
        })

    log_agent(AGENT_NAME, f"NVD fetched {len(items)} CVEs")
    return items


def fetch_exploit_db(limit: int = 30) -> List[Dict[str, Any]]:
    """从 Exploit-DB RSS 抓取最新 exploit/0-day"""
    try:
        r = requests.get("https://www.exploit-db.com/rss.xml", timeout=25, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/rss+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        r.raise_for_status()
    except Exception as e:
        log_agent(AGENT_NAME, f"Exploit-DB fetch error: {e}")
        return []

    feed = feedparser.parse(r.text)
    items = []
    for entry in feed.entries[:limit]:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = entry.get("description", "")
        # 提取CVE号（如果标题中有）
        cve_match = __import__("re").search(r"CVE-\d{4}-\d{4,}", title)
        cve_id = cve_match.group(0) if cve_match else ""

        items.append({
            "cve_id": cve_id or f"EDB-{link.split('/')[-1]}" if link else "EDB-UNKNOWN",
            "title": f"{cve_id or 'Exploit'} - {title}" if cve_id else title,
            "description": f"[Exploit-DB] {strip_html_tags(desc)[:300]}",
            "cvss_score": None,
            "severity": "EXPLOIT",
            "cwes": [],
            "references": [link] if link else [],
            "published": entry.get("published", ""),
            "last_modified": entry.get("updated", ""),
            "solution": "Review and apply vendor patch immediately. Verify exploit applicability in your environment.",
            "source_tag": "Exploit-DB",
        })

    log_agent(AGENT_NAME, f"Exploit-DB fetched {len(items)} items")
    return items


def fetch_github_advisories(limit: int = 20) -> List[Dict[str, Any]]:
    """从 GitHub Security Advisories API 抓取最新安全公告"""
    url = f"https://api.github.com/advisories?per_page={limit}"
    data = fetch_json(url, timeout=20)
    if not data or not isinstance(data, list):
        log_agent(AGENT_NAME, "GitHub Advisories returned no data")
        return []

    items = []
    for adv in data:
        ghsa_id = adv.get("ghsa_id", "")
        summary = adv.get("summary", "")
        desc = adv.get("description", "")[:500]
        severity = adv.get("severity", "N/A").upper()
        cvss_score = adv.get("cvss", {}).get("score") if isinstance(adv.get("cvss"), dict) else None
        refs = []
        if adv.get("html_url"):
            refs.append(adv["html_url"])

        # 提取关联的CVE
        cves = adv.get("cve_ids", [])
        cve_id = cves[0] if cves else ""

        items.append({
            "cve_id": cve_id or ghsa_id,
            "title": f"{cve_id or ghsa_id} - {summary[:80]}",
            "description": f"[GitHub Advisory] {desc}",
            "cvss_score": cvss_score,
            "severity": severity,
            "cwes": [],
            "references": refs,
            "published": adv.get("published_at", ""),
            "last_modified": adv.get("updated_at", ""),
            "solution": f"See GitHub Security Advisory {ghsa_id} for affected packages and patched versions.",
            "source_tag": "GitHub-Advisory",
        })

    log_agent(AGENT_NAME, f"GitHub Advisories fetched {len(items)} items")
    return items


def fetch_cisa_kev() -> List[Dict[str, Any]]:
    """从 CISA KEV 抓取已知被利用漏洞（网络受限时可能失败）"""
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    data = fetch_json(url, timeout=30)
    if not data or "vulnerabilities" not in data:
        return []

    items = []
    vulns = sorted(
        data["vulnerabilities"],
        key=lambda x: x.get("dateAdded", ""),
        reverse=True
    )[:30]

    for v in vulns:
        cve_id = v.get("cveID", "")
        product = v.get("product", "Unknown")
        vendor = v.get("vendorProject", "Unknown")
        desc = v.get("vulnerabilityName", "")
        due_date = v.get("dueDate", "")

        items.append({
            "cve_id": cve_id,
            "title": f"{cve_id} - {desc}",
            "description": f"[CISA KEV] Vendor: {vendor}, Product: {product}. {desc}. Due date: {due_date}.",
            "cvss_score": None,
            "severity": "KEV",
            "cwes": [],
            "references": [f"https://nvd.nist.gov/vuln/detail/{cve_id}"] if cve_id.startswith("CVE-") else [],
            "published": v.get("dateAdded", ""),
            "last_modified": v.get("dateAdded", ""),
            "solution": f"Apply vendor patch before {due_date}. CISA directive enforcement required.",
            "source_tag": "CISA-KEV",
        })

    log_agent(AGENT_NAME, f"CISA KEV fetched {len(items)} items")
    return items


# ---------------------------------------------------------------------------
# 格式化与输出
# ---------------------------------------------------------------------------

def build_md_items(items: List[dict]) -> List[Dict[str, Any]]:
    """将原始 items 转为双语 MD 结构，按 source_tag 分组"""
    # 分组
    groups: Dict[str, List[dict]] = {"NVD": [], "Exploit-DB": [], "GitHub-Advisory": [], "CISA-KEV": [], "other": []}
    for item in items:
        tag = item.get("source_tag", "other")
        groups.setdefault(tag, []).append(item)

    sections = []
    group_titles = {
        "NVD": ("CVE 漏洞库 (NVD)", "CVE Database (NVD)"),
        "Exploit-DB": ("公开利用代码 / 0-Day (Exploit-DB)", "Public Exploits / 0-Day (Exploit-DB)"),
        "GitHub-Advisory": ("GitHub 安全公告", "GitHub Security Advisories"),
        "CISA-KEV": ("CISA 已知被利用漏洞", "CISA Known Exploited Vulnerabilities"),
        "other": ("其他来源", "Other Sources"),
    }

    for tag, group_items in groups.items():
        if not group_items:
            continue
        section_items = []
        for item in group_items:
            cve_id = item.get("cve_id", "N/A")
            desc = item.get("description", "")
            severity = item.get("severity", "N/A")
            cvss = item.get("cvss_score")
            cwes = item.get("cwes", [])
            refs = item.get("references", [])
            solution = item.get("solution", "Refer to vendor security advisory for patch and mitigation guidance.")
            source_tag = item.get("source_tag", "")

            cvss_str = f"CVSS: {cvss}" if cvss is not None else ""
            cwes_str = f"CWE: {', '.join(cwes)}" if cwes else ""
            refs_str = "\n".join([f"- {r}" for r in refs]) if refs else ""
            src_badge = f"[{source_tag}]" if source_tag else ""

            zh_content = f"""**CVE/编号**: {cve_id} {src_badge}
**严重程度**: {severity} | {cvss_str}
{cwes_str}

**漏洞描述**:
{desc}

**应对措施 / 缓解方案**:
{solution}

**参考链接**:
{refs_str}"""

            en_content = f"""**CVE/ID**: {cve_id} {src_badge}
**Severity**: {severity} | {cvss_str}
{cwes_str}

**Description**:
{desc}

**Mitigation / Countermeasure**:
{solution}

**References**:
{refs_str}"""

            section_items.append({
                "zh": {
                    "title": f"{cve_id} ({severity})",
                    "content": zh_content,
                    "source": refs[0] if refs else source_tag,
                },
                "en": {
                    "title": f"{cve_id} ({severity})",
                    "content": en_content,
                    "source": refs[0] if refs else source_tag,
                },
            })

        zh_heading, en_heading = group_titles.get(tag, (tag, tag))
        sections.append({
            "heading_zh": zh_heading,
            "heading_en": en_heading,
            "items": section_items,
        })

    return sections


def run():
    log_agent(AGENT_NAME, "=" * 40)
    log_agent(AGENT_NAME, "Starting scheduled run")

    all_items = []
    errors = []

    # 1. NVD (基础源，稳定50条)
    try:
        nvd_items = fetch_nvd_cves(limit=50)
        all_items.extend(nvd_items)
    except Exception as e:
        errors.append(f"NVD: {e}")
        log_agent(AGENT_NAME, f"NVD error: {e}")

    # 2. Exploit-DB (0-day / 公开利用)
    try:
        edb_items = fetch_exploit_db(limit=30)
        all_items.extend(edb_items)
    except Exception as e:
        errors.append(f"Exploit-DB: {e}")
        log_agent(AGENT_NAME, f"Exploit-DB error: {e}")

    # 3. GitHub Advisories (最新安全公告)
    try:
        gh_items = fetch_github_advisories(limit=20)
        all_items.extend(gh_items)
    except Exception as e:
        errors.append(f"GitHub-Advisories: {e}")
        log_agent(AGENT_NAME, f"GitHub-Advisories error: {e}")

    # 4. CISA KEV (网络受限时可能失败)
    try:
        cisa_items = fetch_cisa_kev()
        all_items.extend(cisa_items)
    except Exception as e:
        errors.append(f"CISA: {e}")
        log_agent(AGENT_NAME, f"CISA error: {e}")

    log_agent(AGENT_NAME, f"Total fetched: {len(all_items)}")

    # 去重过滤
    new_items = filter_new_items("network-security", all_items, keep_old_methods=True)
    log_agent(AGENT_NAME, f"New items after dedup: {len(new_items)}")

    # 补充到展示数量
    state = __import__("utils").load_state()
    all_stored = list(state.get("network-security", {}).values())
    display_items = list(new_items)
    if len(display_items) < MIN_ITEMS:
        seen_ids = {__import__("utils").dedup_key(i) for i in new_items}
        for s in all_stored:
            d = s["data"]
            if __import__("utils").dedup_key(d) not in seen_ids:
                display_items.append(d)
                seen_ids.add(__import__("utils").dedup_key(d))
            if len(display_items) >= MIN_ITEMS:
                break
        log_agent(AGENT_NAME, f"Padded to {len(display_items)} items from history")

    # 生成主索引文件
    sections = build_md_items(display_items[:max(50, len(display_items))])
    md_content = make_bilingual_md(
        title_zh="网络安全漏洞知识库",
        title_en="Network Security Vulnerability Knowledge Base",
        intro_zh="本页面每小时自动从 NVD、Exploit-DB、GitHub Security Advisories、CISA KEV 等平台抓取最新网络安全漏洞（含0-Day公开利用）、应对措施及补丁信息，自动去重并增量更新。",
        intro_en="Auto-updated hourly from NVD, Exploit-DB, GitHub Security Advisories, CISA KEV. Covers CVEs, public exploits (0-Day), and mitigation guidance. Deduplicated and incrementally maintained.",
        sections=sections,
        nav_links=[{"text_zh": "返回首页", "text_en": "Back to Home", "href": "../README.md"}],
    )
    write_md_file(OUTPUT_DIR / "index.md", md_content)

    # 汇报
    total = len(state.get("network-security", {}))
    report = write_report(AGENT_NAME, len(new_items), total, errors)
    log_agent(AGENT_NAME, f"Report: new={report['new_items']}, total={report['total_items']}, errors={len(errors)}")
    log_agent(AGENT_NAME, "Run complete")
    return report


if __name__ == "__main__":
    run()
