#!/usr/bin/env python3
"""
Agent: System Vulnerabilities (Windows / Linux / macOS)
每小时按操作系统分类抓取系统漏洞及应对措施，增量更新。
数据源: NVD API (按厂商关键词过滤), CISA KEV, 安全公告
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

from utils import (
    fetch_json, log_agent, write_report,
    filter_new_items, make_bilingual_md, write_md_file,
)

AGENT_NAME = "agent-system-vulnerabilities"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "system-vulnerabilities"
MIN_ITEMS = 50

# 分类关键词映射
OS_KEYWORDS = {
    "windows": ["Microsoft", "Windows", "MSFT"],
    "linux": ["Linux", "Ubuntu", "Debian", "Red Hat", "CentOS", "Fedora", "SUSE", "Kernel"],
    "macos": ["Apple", "macOS", "Mac OS", "iOS"],
}

# ---------------------------------------------------------------------------
# 数据抓取
# ---------------------------------------------------------------------------

def fetch_nvd_by_keyword(keyword: str, limit: int = 50, start: int = 0) -> List[Dict[str, Any]]:
    """从 NVD 按关键词抓取 CVE"""
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

        # CVSS
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

        # 提取受影响产品（从configurations中粗略提取）
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

        item = {
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
        }
        items.append(item)
    return items


def fetch_os_vulns(os_name: str, min_items: int = 50) -> List[Dict[str, Any]]:
    """为指定 OS 抓取足够数量的漏洞"""
    keywords = OS_KEYWORDS.get(os_name, [os_name])
    all_items = []
    start = 0
    max_pages = 5  # 最多翻5页

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

    # 去重（同一CVE可能被多个关键词命中）
    seen = set()
    unique = []
    for item in all_items:
        key = item.get("cve_id", "")
        if key and key not in seen:
            seen.add(key)
            unique.append(item)

    log_agent(AGENT_NAME, f"Fetched {len(unique)} unique items for {os_name}")
    return unique


# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------

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

        cvss_str = f"CVSS: {cvss}" if cvss is not None else ""
        products_str = f"受影响产品: {', '.join(products)}" if products else ""
        refs_str = "\n".join([f"- {r}" for r in refs]) if refs else ""

        zh = f"""**CVE编号**: {cve_id}
**严重程度**: {severity} {cvss_str}
{products_str}

**漏洞描述**:
{desc}

**应对措施**:
{solution}

**参考链接**:
{refs_str}"""

        en = f"""**CVE ID**: {cve_id}
**Severity**: {severity} {cvss_str}
**Affected Products**: {', '.join(products) if products else 'N/A'}

**Description**:
{desc}

**Mitigation**:
{solution}

**References**:
{refs_str}"""

        section_items.append({
            "zh": {"title": f"{cve_id} ({severity})", "content": zh, "source": refs[0] if refs else "NVD"},
            "en": {"title": f"{cve_id} ({severity})", "content": en, "source": refs[0] if refs else "NVD"},
        })

    return [{
        "heading_zh": f"{os_name.upper()} 漏洞列表",
        "heading_en": f"{os_name.upper()} Vulnerability List",
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
    reports = {}

    for os_name in ["windows", "linux", "macos"]:
        log_agent(AGENT_NAME, f"Processing {os_name}...")
        category = f"sys-vuln-{os_name}"

        try:
            items = fetch_os_vulns(os_name, min_items=MIN_ITEMS)
        except Exception as e:
            errors.append(f"{os_name}: {e}")
            log_agent(AGENT_NAME, f"{os_name} fetch error: {e}")
            items = []

        new_items = filter_new_items(category, items, keep_old_methods=True)
        log_agent(AGENT_NAME, f"{os_name}: fetched={len(items)}, new={len(new_items)}")

        # 合并到展示数量
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

        # 生成各 OS 分类文件
        os_titles = {
            "windows": ("Windows 系统漏洞", "Windows System Vulnerabilities"),
            "linux": ("Linux 系统漏洞", "Linux System Vulnerabilities"),
            "macos": ("macOS 系统漏洞", "macOS System Vulnerabilities"),
        }
        zh_title, en_title = os_titles[os_name]

        sections = build_os_md_items(display_items[:max(50, len(display_items))], os_name)
        md_content = make_bilingual_md(
            title_zh=zh_title,
            title_en=en_title,
            intro_zh=f"本页面每小时自动抓取 {os_name.upper()} 平台最新系统漏洞及应对措施。",
            intro_en=f"Auto-updated hourly: latest {os_name.upper()} system vulnerabilities and mitigations.",
            sections=sections,
        )
        write_md_file(OUTPUT_DIR / f"{os_name}.md", md_content)

        all_new += len(new_items)
        all_total += len(stored)
        reports[os_name] = {"new": len(new_items), "total": len(stored)}

    # 生成总索引
    index_lines = ["# 系统漏洞知识库总索引 | System Vulnerability Knowledge Base Index", "", "| 分类 | 最新更新 | 条目数 |", "|------|----------|--------|"]
    for os_name in ["windows", "linux", "macos"]:
        cat = f"sys-vuln-{os_name}"
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
