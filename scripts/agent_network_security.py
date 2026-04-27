#!/usr/bin/env python3
"""
Agent: Network Security Vulnerabilities
每小时抓取网络安全漏洞及应对措施，增量更新。
数据源: NVD API, CISA KEV, CVE Details
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
from datetime import datetime, timezone, timedelta
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

        # 提取 CVSS 分数
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

        # 提取参考链接
        refs = cve.get("references", [])
        ref_urls = [r.get("url", "") for r in refs[:5] if r.get("url")]

        # 提取 CWE
        weaknesses = cve.get("weaknesses", [])
        cwes = []
        for w in weaknesses:
            for d in w.get("description", []):
                if d.get("value", "").startswith("CWE-"):
                    cwes.append(d["value"])

        item = {
            "cve_id": cve_id,
            "title": f"{cve_id}",
            "description": en_desc,
            "cvss_score": cvss_score,
            "severity": severity,
            "cwes": cwes,
            "references": ref_urls,
            "published": cve.get("published", ""),
            "last_modified": cve.get("lastModified", ""),
        }
        items.append(item)

    log_agent(AGENT_NAME, f"NVD fetched {len(items)} CVEs")
    return items


def fetch_cisa_kev() -> List[Dict[str, Any]]:
    """从 CISA KEV 抓取已知被利用漏洞"""
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    data = fetch_json(url, timeout=30)
    if not data or "vulnerabilities" not in data:
        return []

    items = []
    # 只取最近更新的前 N 条
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
        notes = v.get("notes", "")

        item = {
            "cve_id": cve_id,
            "title": f"{cve_id} - {desc}",
            "description": f"Vendor: {vendor}, Product: {product}. {desc}. Due date: {due_date}. Notes: {notes}",
            "cvss_score": None,
            "severity": "KEV",
            "cwes": [],
            "references": [f"https://nvd.nist.gov/vuln/detail/{cve_id}"] if cve_id.startswith("CVE-") else [],
            "published": v.get("dateAdded", ""),
            "last_modified": v.get("dateAdded", ""),
            "solution": f"Apply vendor patch before {due_date}. CISA directive enforcement required.",
        }
        items.append(item)

    log_agent(AGENT_NAME, f"CISA KEV fetched {len(items)} items")
    return items


# ---------------------------------------------------------------------------
# 格式化与输出
# ---------------------------------------------------------------------------

def build_md_items(items: List[dict]) -> List[Dict[str, Any]]:
    """将原始 items 转为双语 MD 结构"""
    sections = []
    section_items = []

    for item in items:
        cve_id = item.get("cve_id", "N/A")
        desc = item.get("description", "")
        severity = item.get("severity", "N/A")
        cvss = item.get("cvss_score")
        cwes = item.get("cwes", [])
        refs = item.get("references", [])
        solution = item.get("solution", "Refer to vendor security advisory for patch and mitigation guidance.")

        cvss_str = f"CVSS: {cvss}" if cvss is not None else "CVSS: N/A"
        cwes_str = f"CWE: {', '.join(cwes)}" if cwes else ""
        refs_str = "\n".join([f"- {r}" for r in refs]) if refs else ""

        zh_content = f"""**CVE编号**: {cve_id}
**严重程度**: {severity} | {cvss_str}
{cwes_str}

**漏洞描述**:
{desc}

**应对措施 / 缓解方案**:
{solution}

**参考链接**:
{refs_str}"""

        en_content = f"""**CVE ID**: {cve_id}
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
                "source": refs[0] if refs else "NVD",
            },
            "en": {
                "title": f"{cve_id} ({severity})",
                "content": en_content,
                "source": refs[0] if refs else "NVD",
            },
        })

    sections.append({
        "heading_zh": "最新漏洞列表",
        "heading_en": "Latest Vulnerabilities",
        "items": section_items,
    })
    return sections


def run():
    log_agent(AGENT_NAME, "=" * 40)
    log_agent(AGENT_NAME, "Starting scheduled run")

    all_items = []
    errors = []

    # 1. NVD
    try:
        nvd_items = fetch_nvd_cves(limit=50)
        all_items.extend(nvd_items)
    except Exception as e:
        errors.append(f"NVD: {e}")
        log_agent(AGENT_NAME, f"NVD error: {e}")

    # 2. CISA KEV
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

    # 如果新条目不足50，尝试补充（从历史中加载已有条目合并）
    state = __import__("utils").load_state()
    all_stored = list(state.get("network-security", {}).values())
    # 合并新+已有用于展示，但只写新条目到增量文件
    display_items = new_items
    if len(new_items) < MIN_ITEMS:
        # 从历史中补充到50条用于显示
        stored_items = [s["data"] for s in all_stored[:MIN_ITEMS]]
        # 去重
        seen_ids = {__import__("utils").dedup_key(i) for i in new_items}
        for s in stored_items:
            if __import__("utils").dedup_key(s) not in seen_ids:
                display_items.append(s)
                seen_ids.add(__import__("utils").dedup_key(s))
            if len(display_items) >= MIN_ITEMS:
                break
        log_agent(AGENT_NAME, f"Padded to {len(display_items)} items from history")

    # 生成主索引文件
    sections = build_md_items(display_items[:max(50, len(display_items))])
    md_content = make_bilingual_md(
        title_zh="网络安全漏洞知识库",
        title_en="Network Security Vulnerability Knowledge Base",
        intro_zh="本页面每小时自动从 NVD、CISA KEV 等平台抓取最新网络安全漏洞及应对措施，自动去重并增量更新。",
        intro_en="This page is auto-updated hourly from NVD, CISA KEV, and other platforms. Deduplicated and incrementally maintained.",
        sections=sections,
        nav_links=[{"text_zh": "返回首页", "text_en": "Back to Home", "href": "../README.md"}],
    )
    write_md_file(OUTPUT_DIR / "index.md", md_content)

    # 汇报
    state = __import__("utils").load_state()
    total = len(state.get("network-security", {}))
    report = write_report(AGENT_NAME, len(new_items), total, errors)
    log_agent(AGENT_NAME, f"Report: new={report['new_items']}, total={report['total_items']}, errors={len(errors)}")
    log_agent(AGENT_NAME, "Run complete")
    return report


if __name__ == "__main__":
    run()
