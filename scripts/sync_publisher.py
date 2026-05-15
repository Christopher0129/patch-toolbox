#!/usr/bin/env python3
"""
Sync Script: Publisher
汇总同步结果，从SQLite重新生成MD，推送GitHub。

Stage boundaries (explicit):
  1. READ_REPORTS   — 读取各分类 sync 报告
  2. PREFLIGHT      — 验证 DB、git 等前置条件
  3. REGENERATE_MD  — 从 SQLite 重新生成 MD 文件
  4. VECTOR_INDEX   — 向量索引增量更新（可选）
  5. GENERATE_REPORT— 生成汇报文件
  6. VERIFY         — 验证生成结果完整性
  7. GIT_PUSH       — 提交并推送至 GitHub
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from utils import (
    log_sync, log_stage_start, log_stage_end,
    git_push, write_md_file,
    regenerate_all_md, preflight_check, DB_DIR,
)
from verify_db_sync import verify_sync_state

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


def _fallback_sync_name(path: Path) -> str:
    stem = path.stem
    if stem.endswith("_report"):
        stem = stem[:-7]
    return stem


def read_report(path: Path) -> dict:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"sync": _fallback_sync_name(path), "new_items": 0, "total_items": 0, "errors": [], "timestamp": None}


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

    # ── Stage 1: READ_REPORTS ──────────────────────────────────────────
    log_stage_start("READ_REPORTS")

    reports = {}
    for key, path in REPORTS.items():
        reports[key] = read_report(path)
        log_sync(SYNC_NAME, f"Read report for {key}: new={reports[key]['new_items']}")

    total_new = sum(r["new_items"] for r in reports.values())
    all_errors = []
    for r in reports.values():
        all_errors.extend(r.get("errors", []))

    log_sync(SYNC_NAME, f"  Total new items across reports: {total_new}")
    log_sync(SYNC_NAME, f"  Total errors across reports: {len(all_errors)}")
    log_stage_end("READ_REPORTS", "OK", f"{total_new} new, {len(all_errors)} errors")

    # ── Stage 2: PREFLIGHT ─────────────────────────────────────────────
    log_stage_start("PREFLIGHT")

    pf = preflight_check(require_agents_dir=True)
    pf_failures = [c for c in pf["checks"] if not c["ok"]]
    for c in pf_failures:
        log_sync(SYNC_NAME, f"  ⚠ Preflight failure: {c['name']} — {c['detail']}")
    if pf["ok"]:
        log_sync(SYNC_NAME, f"  Preflight: {pf['summary']}")
        log_stage_end("PREFLIGHT", "OK", pf["summary"])
    else:
        log_sync(SYNC_NAME, f"  Preflight FAILED: {pf['summary']}")
        log_stage_end("PREFLIGHT", "FAIL", pf["summary"])
        log_sync(SYNC_NAME, "Aborting: preflight checks failed")
        return {"total_new": total_new, "total_all": 0, "github_ok": False, "errors": len(all_errors), "preflight_failures": len(pf_failures)}

    # ── Stage 3: REGENERATE_MD ─────────────────────────────────────────
    log_stage_start("REGENERATE_MD")

    log_sync(SYNC_NAME, "Regenerating MD files from SQLite...")
    md_ok = regenerate_all_md()
    if not md_ok:
        log_sync(SYNC_NAME, "WARNING: MD regeneration may have failed")

    log_stage_end("REGENERATE_MD", "WARN" if not md_ok else "OK")

    # ── Stage 4: VECTOR_INDEX ──────────────────────────────────────────
    log_stage_start("VECTOR_INDEX")

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

    log_stage_end("VECTOR_INDEX", "OK")

    # ── Stage 5: GENERATE_REPORT ───────────────────────────────────────
    log_stage_start("GENERATE_REPORT")

    sqlite_counts = count_from_sqlite()
    total_all = sum(sqlite_counts.values())
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

    log_stage_end("GENERATE_REPORT", "OK", f"{total_new} new, {total_all} total")

    # ── Stage 6: VERIFY ────────────────────────────────────────────────
    log_stage_start("VERIFY")

    verify_result = verify_sync_state()
    log_sync(SYNC_NAME, f"  Verify: {verify_result['summary']}")
    if verify_result["ok"]:
        log_stage_end("VERIFY", "OK", verify_result["summary"])
    else:
        log_sync(SYNC_NAME, f"  Verify FAILED: {verify_result['summary']}")
        log_stage_end("VERIFY", "FAIL", verify_result["summary"])
        log_sync(SYNC_NAME, "Aborting: post-regeneration verification failed")
        return {"total_new": total_new, "total_all": total_all, "github_ok": False, "errors": len(all_errors), "verify_ok": False}

    # ── Stage 7: GIT_PUSH ──────────────────────────────────────────────
    log_stage_start("GIT_PUSH")

    push_result = git_push(f"update: {today} — {total_new} new, {total_all} total")
    gh_ok = push_result.get("github", False)
    if gh_ok:
        log_sync(SYNC_NAME, "GitHub push successful")
    else:
        log_sync(SYNC_NAME, "GitHub push failed or nothing to commit")

    log_stage_end("GIT_PUSH", "OK" if gh_ok else "FAIL")

    # ── Final summary ──────────────────────────────────────────────────
    push_status = "✅ GitHub" if gh_ok else "❌ GitHub"
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
    return {"total_new": total_new, "total_all": total_all, "github_ok": gh_ok, "errors": len(all_errors)}


if __name__ == "__main__":
    run()
