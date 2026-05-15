#!/usr/bin/env python3
"""
Sync Script: Publisher
汇总同步结果，从SQLite重新生成MD，推送GitHub。

Stage boundaries (explicit):
  1. READ_REPORTS    — 读取各分类 sync 报告
  2. PREFLIGHT       — 验证 DB、git 等前置条件
  3. SQLITE_COUNT    — 统计当前 SQLite 条目数
  4. REGENERATE_MD   — 从 SQLite 重新生成 MD 文件
  5. VECTOR_INDEX    — 向量索引增量更新（可选）
  6. GENERATE_REPORT — 生成汇报文件（人类可读 + 机器可读）
  7. VERIFY          — 验证生成结果完整性
  8. GIT_PUSH        — 提交并推送至 GitHub

Produces both human-readable and machine-readable (structured StageState) reports.
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
from stage_state import (
    StageTimer, StageRecord, PipelineReport,
    pipeline_report_to_dict,
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


def _record_stage(pipeline_stages: list[StageRecord], stage_name: str, timer: StageTimer, status: str, detail: str = "", count=None, count_label=None, error_detail=None):
    pipeline_stages.append(timer.to_record(
        name=stage_name,
        status=status,
        detail=detail,
        count=count,
        count_label=count_label,
        error_detail=error_detail,
    ))


def _vec_index_stages() -> list[StageRecord]:
    """Run vector index update and return StageRecord list."""
    stages = []
    if not _VEC_AVAILABLE:
        stages.append(StageRecord(
            name="vec-index",
            status="ok",
            duration_ms=0.0,
            detail="Vector search module not available — skipped",
        ))
        return stages

    try:
        from vector_search.config import VectorConfig
        cfg = VectorConfig.load()
        if not cfg.enabled:
            stages.append(StageRecord(
                name="vec-index",
                status="ok",
                duration_ms=0.0,
                detail="Vector search disabled in config — skipped",
            ))
            return stages

        dbs = {
            "network-security": DB_DIR / "network-security.db",
            "system-vulnerabilities": DB_DIR / "system-vulnerabilities.db",
            "system-troubleshooting": DB_DIR / "system-troubleshooting.db",
        }
        for name, db_path in dbs.items():
            if db_path.exists():
                timer = StageTimer()
                with timer:
                    vs = VectorSearch(db_path)
                    result = vs.ensure_indexed()
                stages.append(timer.to_record(
                    name=f"vec-index-{name}",
                    status="ok",
                    detail=f"+{result['indexed']} new, total {result['total']}",
                    count=result["indexed"],
                    count_label="vec_indexed",
                ))
            else:
                stages.append(StageRecord(
                    name=f"vec-index-{name}",
                    status="warning",
                    duration_ms=0.0,
                    detail="DB not found — skipped",
                ))
    except Exception as e:
        stages.append(StageRecord(
            name="vec-index",
            status="error",
            duration_ms=0.0,
            detail=f"Vector index update error: {e}",
            error_detail=str(e)[:300],
        ))
    return stages


def _build_structured_report(pipeline_start: datetime, pipeline_stages: list[StageRecord], total_new: int, total_all: int, all_errors: list[str]) -> dict:
    pipeline_finish = datetime.now(timezone.utc)
    pipeline_report = PipelineReport(
        pipeline=SYNC_NAME,
        started_at=pipeline_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        finished_at=pipeline_finish.strftime("%Y-%m-%dT%H:%M:%SZ"),
        stages=pipeline_stages,
    )
    struct_report = pipeline_report_to_dict(pipeline_report)
    struct_report["aggregated"] = {
        "total_new": total_new,
        "total_all": total_all,
        "upstream_errors": len(all_errors),
        "pipeline_all_ok": pipeline_report.all_ok,
    }
    return struct_report


def _write_structured_reports(struct_report: dict, today: str):
    struct_path = AGENTS_DIR / "pipeline_report_latest.json"
    with open(struct_path, "w", encoding="utf-8") as f:
        json.dump(struct_report, f, ensure_ascii=False, indent=2)
    struct_path_date = AGENTS_DIR / f"pipeline_report_{today}.json"
    with open(struct_path_date, "w", encoding="utf-8") as f:
        json.dump(struct_report, f, ensure_ascii=False, indent=2)
    log_sync(SYNC_NAME, f"Structured pipeline report written: {struct_path}")


def run():
    pipeline_start = datetime.now(timezone.utc)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting publisher run")

    pipeline_stages: list[StageRecord] = []
    pipeline_summary_lines = []

    # ── Stage 1: READ_REPORTS ──────────────────────────────────────────
    log_stage_start("READ_REPORTS")
    with StageTimer() as t_read:
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
    _record_stage(pipeline_stages, "read-reports", t_read, "ok", f"read {len(REPORTS)} report files", count=total_new, count_label="new_items")

    # ── Stage 2: PREFLIGHT ─────────────────────────────────────────────
    log_stage_start("PREFLIGHT")
    with StageTimer() as t_preflight:
        pf = preflight_check(require_agents_dir=True)
    pf_failures = [c for c in pf["checks"] if not c["ok"]]
    for c in pf_failures:
        log_sync(SYNC_NAME, f"  ⚠ Preflight failure: {c['name']} — {c['detail']}")
    if pf["ok"]:
        log_sync(SYNC_NAME, f"  Preflight: {pf['summary']}")
        log_stage_end("PREFLIGHT", "OK", pf["summary"])
        _record_stage(pipeline_stages, "preflight", t_preflight, "ok", pf["summary"])
    else:
        log_sync(SYNC_NAME, f"  Preflight FAILED: {pf['summary']}")
        log_stage_end("PREFLIGHT", "FAIL", pf["summary"])
        _record_stage(pipeline_stages, "preflight", t_preflight, "error", pf["summary"], error_detail=pf["summary"])
        struct_report = _build_structured_report(pipeline_start, pipeline_stages, total_new, 0, all_errors)
        _write_structured_reports(struct_report, today)
        log_sync(SYNC_NAME, "Aborting: preflight checks failed")
        return {"total_new": total_new, "total_all": 0, "github_ok": False, "errors": len(all_errors), "preflight_failures": len(pf_failures)}

    # ── Stage 3: SQLITE_COUNT ──────────────────────────────────────────
    log_stage_start("SQLITE_COUNT")
    with StageTimer() as t_sql:
        sqlite_counts = count_from_sqlite()
    total_all = sum(sqlite_counts.values())
    log_sync(SYNC_NAME, f"  SQLite total count: {total_all}")
    log_stage_end("SQLITE_COUNT", "OK", f"{total_all} total")
    _record_stage(pipeline_stages, "sqlite-count", t_sql, "ok", f"counted {total_all} entries across {len(sqlite_counts)} DBs", count=total_all, count_label="total_entries")

    # ── Stage 4: REGENERATE_MD ─────────────────────────────────────────
    log_stage_start("REGENERATE_MD")
    with StageTimer() as t_md:
        log_sync(SYNC_NAME, "Regenerating MD files from SQLite...")
        md_ok = regenerate_all_md()
    md_status = "ok" if md_ok else "warning"
    md_detail = "MD files regenerated from SQLite" if md_ok else "MD regeneration may have partially failed"
    if not md_ok:
        pipeline_summary_lines.append("WARNING: MD regeneration may have failed")
    log_stage_end("REGENERATE_MD", "WARN" if not md_ok else "OK")
    _record_stage(pipeline_stages, "md-regen", t_md, md_status, md_detail)

    # ── Stage 5: VECTOR_INDEX ──────────────────────────────────────────
    log_stage_start("VECTOR_INDEX")
    vec_stages = _vec_index_stages()
    pipeline_stages.extend(vec_stages)
    vec_has_error = any(s.status == "error" for s in vec_stages)
    vec_has_warning = any(s.status == "warning" for s in vec_stages)
    log_stage_end("VECTOR_INDEX", "FAIL" if vec_has_error else ("WARN" if vec_has_warning else "OK"))

    # ── Stage 6: GENERATE_REPORT ───────────────────────────────────────
    log_stage_start("GENERATE_REPORT")
    with StageTimer() as t_report:
        stage_rows = []
        for s in pipeline_stages:
            icon = {"ok": "✅", "warning": "⚠️", "error": "❌"}.get(s.status, "❓")
            dur_str = f"{s.duration_ms:.0f}ms" if s.duration_ms >= 1 else ""
            cnt_str = f" | {s.count_label}={s.count}" if s.count is not None else ""
            stage_rows.append(f"| {icon} {s.name} | {dur_str} | {s.detail}{cnt_str} |")
        stage_table = "\n".join(stage_rows)

        report_md = f"""# 更新汇报 | Update Report

> 汇报生成于 {ts}

## 各分类更新情况

| 分类 | 新增条目 | 累计条目 |
|---|---|---|
| 网络安全漏洞 | {reports['network-security']['new_items']} | {sqlite_counts.get('network-security', 0)} |
| 系统漏洞 | {reports['system-vulnerabilities']['new_items']} | {sqlite_counts.get('system-vulnerabilities', 0)} |
| 系统故障 | {reports['system-troubleshooting']['new_items']} | {sqlite_counts.get('system-troubleshooting', 0)} |

## Pipeline 阶段状态

| 阶段 | 耗时 | 详情 |
|---|---|---|
{stage_table}

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

        struct_report = _build_structured_report(pipeline_start, pipeline_stages, total_new, total_all, all_errors)
        _write_structured_reports(struct_report, today)
    log_sync(SYNC_NAME, "Report generated")
    log_stage_end("GENERATE_REPORT", "OK", f"{total_new} new, {total_all} total")
    _record_stage(pipeline_stages, "generate-report", t_report, "ok", f"{total_new} new, {total_all} total")

    # ── Stage 7: VERIFY ────────────────────────────────────────────────
    log_stage_start("VERIFY")
    with StageTimer() as t_verify:
        verify_result = verify_sync_state()
    log_sync(SYNC_NAME, f"  Verify: {verify_result['summary']}")
    if verify_result["ok"]:
        log_stage_end("VERIFY", "OK", verify_result["summary"])
        _record_stage(pipeline_stages, "verify", t_verify, "ok", verify_result["summary"])
    else:
        log_sync(SYNC_NAME, f"  Verify FAILED: {verify_result['summary']}")
        log_stage_end("VERIFY", "FAIL", verify_result["summary"])
        _record_stage(pipeline_stages, "verify", t_verify, "error", verify_result["summary"], error_detail=verify_result["summary"])
        struct_report = _build_structured_report(pipeline_start, pipeline_stages, total_new, total_all, all_errors)
        _write_structured_reports(struct_report, today)
        log_sync(SYNC_NAME, "Aborting: post-regeneration verification failed")
        return {"total_new": total_new, "total_all": total_all, "github_ok": False, "errors": len(all_errors), "verify_ok": False}

    # ── Stage 8: GIT_PUSH ──────────────────────────────────────────────
    log_stage_start("GIT_PUSH")
    with StageTimer() as t_push:
        push_result = git_push(f"update: {today} — {total_new} new, {total_all} total")
    gh_ok = push_result.get("github", False)
    if gh_ok:
        log_sync(SYNC_NAME, "GitHub push successful")
    else:
        log_sync(SYNC_NAME, "GitHub push failed or nothing to commit")
    log_stage_end("GIT_PUSH", "OK" if gh_ok else "FAIL")
    _record_stage(
        pipeline_stages,
        "git-push",
        t_push,
        "ok" if gh_ok else "error",
        "GitHub push successful" if gh_ok else "GitHub push failed or nothing to commit",
        error_detail=None if gh_ok else "push returned False",
    )

    # Final structured report refresh after push
    struct_report = _build_structured_report(pipeline_start, pipeline_stages, total_new, total_all, all_errors)
    _write_structured_reports(struct_report, today)

    # ── Final summary ──────────────────────────────────────────────────
    push_status = "✅ GitHub" if gh_ok else "❌ GitHub"
    stage_status_icons = "".join("✅" if s.status == "ok" else ("⚠️" if s.status == "warning" else "❌") for s in pipeline_stages)
    summary = f"""📋 汇报 | Report
━━━━━━━━━━━━━━━━━━━━━
🛡️ 网络安全漏洞: +{reports['network-security']['new_items']} (累计 {sqlite_counts.get('network-security', 0)})
🔒 系统漏洞: +{reports['system-vulnerabilities']['new_items']} (累计 {sqlite_counts.get('system-vulnerabilities', 0)})
🔧 系统故障: +{reports['system-troubleshooting']['new_items']} (累计 {sqlite_counts.get('system-troubleshooting', 0)})
━━━━━━━━━━━━━━━━━━━━━
总计新增: {total_new} | 总计累计: {total_all}
阶段状态: {stage_status_icons}
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
