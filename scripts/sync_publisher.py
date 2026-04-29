#!/usr/bin/env python3
"""
Sync Script: Publisher
汇总同步结果，从SQLite重新生成MD，推送GitHub+Gitee。
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import os
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from utils import (
    log_sync, git_push, write_md_file,
    regenerate_all_md, DB_DIR,
)

# 向量搜索可选集成
try:
    from vector_search import VectorSearch
    _VEC_AVAILABLE = True
except Exception:
    _VEC_AVAILABLE = False

SYNC_NAME = "sync-publisher"
AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"
REPORTS = {
    "network-security": AGENTS_DIR / "sync-network-security_report.json",
    "system-vulnerabilities": AGENTS_DIR / "sync-system-vulnerabilities_report.json",
    "system-troubleshooting": AGENTS_DIR / "sync-system-troubleshooting_report.json",
}


def read_report(path: Path) -> dict:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"sync": path.stem, "new_items": 0, "total_items": 0, "errors": [], "timestamp": None}


def count_from_sqlite() -> dict:
    """从 SQLite 数据库统计各分类条目数"""
    counts = {}
    dbs = {
        "network-security": DB_DIR / "network-security.db",
        "system-vulnerabilities": DB_DIR / "system-vulnerabilities.db",
        "system-troubleshooting": DB_DIR / "system-troubleshooting.db",
    }
    for name, db_path in dbs.items():
        if db_path.exists():
            try:
                with sqlite3.connect(db_path) as conn:
                    c = conn.cursor()
                    c.execute("SELECT COUNT(*) FROM entries")
                    counts[name] = c.fetchone()[0]
            except Exception as e:
                log_sync(SYNC_NAME, f"SQLite count error for {name}: {e}")
                counts[name] = 0
        else:
            counts[name] = 0
    return counts


def run():
    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting publisher run")

    # 1. 读取三个 sync 报告
    reports = {}
    for key, path in REPORTS.items():
        reports[key] = read_report(path)
        log_sync(SYNC_NAME, f"Read report for {key}: new={reports[key]['new_items']}")

    total_new = sum(r["new_items"] for r in reports.values())
    all_errors = []
    for r in reports.values():
        all_errors.extend(r.get("errors", []))

    # 2. 从 SQLite 统计总条目数
    sqlite_counts = count_from_sqlite()
    total_all = sum(sqlite_counts.values())

    # 3. 重新生成 MD 文件
    log_sync(SYNC_NAME, "Regenerating MD files from SQLite...")
    md_ok = regenerate_all_md()
    if not md_ok:
        log_sync(SYNC_NAME, "WARNING: MD regeneration may have failed")

    # 3.5 向量索引增量更新（若配置启用）
    if _VEC_AVAILABLE:
        try:
            from vector_search.config import VectorConfig
            cfg = VectorConfig.load()
            if cfg.enabled:
                log_sync(SYNC_NAME, "Vector search enabled — updating indices...")
                dbs = {
                    "network-security": DB_DIR / "network-security.db",
                    "system-vulnerabilities": DB_DIR / "system-vulnerabilities.db",
                    "system-troubleshooting": DB_DIR / "system-troubleshooting.db",
                }
                for name, db_path in dbs.items():
                    if db_path.exists():
                        try:
                            vs = VectorSearch(db_path)
                            result = vs.ensure_indexed()
                            log_sync(SYNC_NAME, f"  vec-index [{name}]: +{result['indexed']} new, total {result['total']}")
                        except Exception as e:
                            log_sync(SYNC_NAME, f"  vec-index [{name}] error: {e}")
            else:
                log_sync(SYNC_NAME, "Vector search disabled in config.json — skipping vec-index update")
        except Exception as e:
            log_sync(SYNC_NAME, f"Vector index update skipped: {e}")
    else:
        log_sync(SYNC_NAME, "Vector search module not available — skipping vec-index update")

    # 4. 生成汇报文件
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    report_md = f"""# 更新汇报 | Update Report

> 汇报生成于 {ts}

## 各分类更新情况

| 分类 | 新增条目 | 累计条目 |
|---|---|---|
| 网络安全漏洞 | {reports['network-security']['new_items']} | {sqlite_counts.get('network-security', 0)} |
| 系统漏洞 | {reports['system-vulnerabilities']['new_items']} | {sqlite_counts.get('system-vulnerabilities', 0)} |
| 系统故障 | {reports['system-troubleshooting']['new_items']} | {sqlite_counts.get('system-troubleshooting', 0)} |

## 错误日志

共 {len(all_errors)} 个错误。
"""
    if all_errors:
        for i, e in enumerate(all_errors[:10], 1):
            report_md += f"\n{i}. {e}"
    else:
        report_md += "\n无错误 / No errors."

    write_md_file(AGENTS_DIR / "report_latest.md", report_md)
    write_md_file(AGENTS_DIR / f"report_{today}.md", report_md)
    log_sync(SYNC_NAME, "Report generated")

    # 5. GitHub + Gitee 双推
    push_result = git_push(f"update: {today} — {total_new} new, {total_all} total")
    gh_ok = push_result.get("github", False)
    gt_ok = push_result.get("gitee", False)
    if gh_ok:
        log_sync(SYNC_NAME, "GitHub push successful")
    else:
        log_sync(SYNC_NAME, "GitHub push failed or nothing to commit")
    if gt_ok:
        log_sync(SYNC_NAME, "Gitee push successful")
    else:
        log_sync(SYNC_NAME, "Gitee push failed")

    # 6. 简短文字汇报
    push_status = "✅ GitHub+Gitee" if (gh_ok and gt_ok) else ("✅ GitHub ❌ Gitee" if gh_ok else ("❌ GitHub ✅ Gitee" if gt_ok else "❌ 全部失败"))
    summary = f"""📋 汇报 | Report
━━━━━━━━━━━━━━━━━━━━━
🛡️ 网络安全漏洞: +{reports['network-security']['new_items']} (累计 {sqlite_counts.get('network-security', 0)})
🔒 系统漏洞: +{reports['system-vulnerabilities']['new_items']} (累计 {sqlite_counts.get('system-vulnerabilities', 0)})
🔧 系统故障: +{reports['system-troubleshooting']['new_items']} (累计 {sqlite_counts.get('system-troubleshooting', 0)})
━━━━━━━━━━━━━━━━━━━━━
总计新增: {total_new} | 总计累计: {total_all}
错误数: {len(all_errors)}
推送状态: {push_status}
━━━━━━━━━━━━━━━━━━━━━"""

    log_sync(SYNC_NAME, summary)
    with open(AGENTS_DIR / "summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    log_sync(SYNC_NAME, "Publisher run complete")
    return {"total_new": total_new, "total_all": total_all, "github_ok": gh_ok, "gitee_ok": gt_ok, "errors": len(all_errors)}


if __name__ == "__main__":
    run()
