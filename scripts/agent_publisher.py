#!/usr/bin/env python3
"""
Agent: Publisher
汇总三个抓取agent的结果，更新配置，推送GitHub，生成汇报。
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from utils import (
    log_agent, git_push, write_md_file, make_bilingual_md,
)

AGENT_NAME = "agent-publisher"
AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"
REPORTS = {
    "network-security": AGENTS_DIR / "agent-network-security_report.json",
    "system-vulnerabilities": AGENTS_DIR / "agent-system-vulnerabilities_report.json",
    "system-troubleshooting": AGENTS_DIR / "agent-system-troubleshooting_report.json",
}


def read_report(path: Path) -> dict:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"agent": path.stem, "new_items": 0, "total_items": 0, "errors": [], "timestamp": None}


def run():
    log_agent(AGENT_NAME, "=" * 40)
    log_agent(AGENT_NAME, "Starting publisher run")

    # 1. 读取三个agent报告
    reports = {}
    for key, path in REPORTS.items():
        reports[key] = read_report(path)
        log_agent(AGENT_NAME, f"Read report for {key}: new={reports[key]['new_items']}, total={reports[key]['total_items']}")

    total_new = sum(r["new_items"] for r in reports.values())
    total_all = sum(r["total_items"] for r in reports.values())
    all_errors = []
    for r in reports.values():
        all_errors.extend(r.get("errors", []))

    # 2. 更新汇报文件 (中英双语)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    report_sections = [
        {
            "heading_zh": "本次更新概况",
            "heading_en": "Update Summary",
            "items": [
                {
                    "zh": {
                        "title": "网络安全漏洞",
                        "content": f"新增: {reports['network-security']['new_items']} | 累计: {reports['network-security']['total_items']}",
                        "source": "NVD / CISA",
                    },
                    "en": {
                        "title": "Network Security",
                        "content": f"New: {reports['network-security']['new_items']} | Total: {reports['network-security']['total_items']}",
                        "source": "NVD / CISA",
                    },
                },
                {
                    "zh": {
                        "title": "系统漏洞 (Win/Linux/Mac)",
                        "content": f"新增: {reports['system-vulnerabilities']['new_items']} | 累计: {reports['system-vulnerabilities']['total_items']}",
                        "source": "NVD",
                    },
                    "en": {
                        "title": "System Vulnerabilities (Win/Linux/Mac)",
                        "content": f"New: {reports['system-vulnerabilities']['new_items']} | Total: {reports['system-vulnerabilities']['total_items']}",
                        "source": "NVD",
                    },
                },
                {
                    "zh": {
                        "title": "系统故障及解决",
                        "content": f"新增: {reports['system-troubleshooting']['new_items']} | 累计: {reports['system-troubleshooting']['total_items']}",
                        "source": "Stack Exchange",
                    },
                    "en": {
                        "title": "System Troubleshooting",
                        "content": f"New: {reports['system-troubleshooting']['new_items']} | Total: {reports['system-troubleshooting']['total_items']}",
                        "source": "Stack Exchange",
                    },
                },
            ],
        }
    ]

    if all_errors:
        error_items = []
        for i, e in enumerate(all_errors[:10], 1):
            error_items.append({
                "zh": {"title": f"错误 {i}", "content": str(e), "source": "agent"},
                "en": {"title": f"Error {i}", "content": str(e), "source": "agent"},
            })
        report_sections.append({
            "heading_zh": "错误日志",
            "heading_en": "Error Log",
            "items": error_items,
        })

    report_md = make_bilingual_md(
        title_zh="自动化更新汇报",
        title_en="Automated Update Report",
        intro_zh=f"本次汇报生成于 {ts}。三个agent已完成抓取与增量更新。",
        intro_en=f"Report generated at {ts}. All three agents completed scraping and incremental updates.",
        sections=report_sections,
    )
    write_md_file(AGENTS_DIR / "report_latest.md", report_md)
    log_agent(AGENT_NAME, "Report markdown generated")

    # 3. 更新当日汇报
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    write_md_file(AGENTS_DIR / f"report_{today}.md", report_md)

    # 4. GitHub 推送
    push_ok = git_push(f"auto: {today} update — {total_new} new items, {total_all} total")
    if push_ok:
        log_agent(AGENT_NAME, "GitHub push successful")
    else:
        log_agent(AGENT_NAME, "GitHub push failed or nothing to commit")

    # 5. 简短文字汇报
    summary = f"""📋 Agent 汇报 | Report
━━━━━━━━━━━━━━━━━━━━━
🛡️ 网络安全漏洞: +{reports['network-security']['new_items']} (累计 {reports['network-security']['total_items']})
🔒 系统漏洞: +{reports['system-vulnerabilities']['new_items']} (累计 {reports['system-vulnerabilities']['total_items']})
🔧 系统故障: +{reports['system-troubleshooting']['new_items']} (累计 {reports['system-troubleshooting']['total_items']})
━━━━━━━━━━━━━━━━━━━━━
总计新增: {total_new} | 总计累计: {total_all}
错误数: {len(all_errors)}
推送状态: {'✅ 成功' if push_ok else '❌ 失败'}
━━━━━━━━━━━━━━━━━━━━━"""

    log_agent(AGENT_NAME, summary)
    with open(AGENTS_DIR / "summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    log_agent(AGENT_NAME, "Publisher run complete")
    return {"total_new": total_new, "total_all": total_all, "push_ok": push_ok, "errors": len(all_errors)}


if __name__ == "__main__":
    run()
