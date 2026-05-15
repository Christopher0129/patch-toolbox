"""
Machine-readable Stage State for monitoring run results.

Each pipeline run (sync-network-security, sync-system-vulnerabilities,
sync-system-troubleshooting, sync-publisher) produces a list of Stage records.
A Stage represents one logical step: e.g. "fetch-A", "insert-A", "fetch-B",
"insert-B", "md-regen", "vec-index", "git-push".

Operator tools can aggregate these across runs to detect anomalous durations,
repeated failures, or zero-new-item cycles.
"""
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import List, Optional


@dataclass
class StageRecord:
    """One recorded step in a sync pipeline.

    Fields:
        name: short slug, e.g. "fetch-A", "insert-A", "fetch-B-windows", "md-regen", "vec-index", "git-push"
        status: "ok" | "warning" | "error"
        duration_ms: elapsed wall-clock time in milliseconds
        detail: human-readable one-liner summary of outcome
        count: optional count of items affected (new rows inserted, files checked, etc.)
        count_label: label for the count field, e.g. "new_items", "files_fixed"
        error_detail: when status == "error", a short error detail; None otherwise
    """
    name: str
    status: str  # "ok" | "warning" | "error"
    duration_ms: float
    detail: str = ""
    count: Optional[int] = None
    count_label: str = ""
    error_detail: Optional[str] = None


@dataclass
class PipelineReport:
    """Structured report for one pipeline run.

    Fields:
        pipeline: pipeline name e.g. "sync-network-security"
        started_at: ISO-8601 UTC timestamp when the pipeline started
        finished_at: ISO-8601 UTC timestamp when the pipeline finished
        stages: list of StageRecord entries in execution order
        summary: aggregated summary string
        version: report schema version (bump on breaking changes)
    """
    pipeline: str
    started_at: str
    finished_at: str
    stages: List[StageRecord] = field(default_factory=list)
    summary: str = ""
    version: int = 1

    @property
    def total_duration_ms(self) -> float:
        if not self.stages:
            return 0.0
        return self.stages[-1].duration_ms  # last stage cumulative, or sum below

    @property
    def all_ok(self) -> bool:
        return all(s.status == "ok" for s in self.stages)

    @property
    def error_count(self) -> int:
        return sum(1 for s in self.stages if s.status == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for s in self.stages if s.status == "warning")


# ---------------------------------------------------------------------------
# Timer helper: context-manager style timing
# ---------------------------------------------------------------------------

class StageTimer:
    """Simple timer for measuring duration of pipeline stages.

    Usage:
        with StageTimer() as timer:
            do_work()
        record = timer.to_record("fetch-A", "ok", detail="fetched 50 items", count=50)
    """
    def __init__(self):
        self.start: Optional[float] = None
        self.end: Optional[float] = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()

    @property
    def elapsed_ms(self) -> float:
        if self.start is None:
            return 0.0
        end = self.end or time.perf_counter()
        return round((end - self.start) * 1000, 1)

    def to_record(
        self,
        name: str,
        status: str = "ok",
        detail: str = "",
        count: Optional[int] = None,
        count_label: str = "",
        error_detail: Optional[str] = None,
    ) -> StageRecord:
        return StageRecord(
            name=name,
            status=status,
            duration_ms=self.elapsed_ms,
            detail=detail,
            count=count,
            count_label=count_label,
            error_detail=error_detail,
        )


def run_timed(name: str, status: str = "ok", detail: str = "", count: Optional[int] = None,
              count_label: str = "", error_detail: Optional[str] = None) -> StageRecord:
    """Synchronous helper when you just want a StageRecord with no timing.

    For untimed or pre-timed steps; uses duration_ms=0.
    """
    return StageRecord(
        name=name,
        status=status,
        duration_ms=0.0,
        detail=detail,
        count=count,
        count_label=count_label,
        error_detail=error_detail,
    )


def pipeline_report_to_dict(report: PipelineReport) -> dict:
    """Serialize a PipelineReport into a plain dict (JSON-safe)."""
    return asdict(report)


def pipeline_report_to_json(report: PipelineReport, indent: int = 2) -> str:
    """Serialize a PipelineReport to JSON string."""
    return __import__("json").dumps(asdict(report), ensure_ascii=False, indent=indent)


def stage_state_from_report_json(report_path) -> Optional[List[StageRecord]]:
    """Parse legacy sync report JSON back into StageRecord list.

    Legacy reports have shape:
        {"sync": "...", "timestamp": "...", "new_items": N, "total_items": N, "errors": [...]}
    We synthesize a minimal StageRecord list for compatibility.
    """
    import json
    from pathlib import Path
    p = Path(report_path)
    if not p.exists():
        return None
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    stages = []
    if "new_items" in data:
        stages.append(StageRecord(
            name="sync-insert",
            status="ok" if not data.get("errors") else "warning",
            duration_ms=0.0,
            detail=f"{data.get('new_items', 0)} new, {data.get('total_items', 0)} total",
            count=data.get("new_items", 0),
            count_label="new_items",
            error_detail=data["errors"][0] if data.get("errors") else None,
        ))
    if data.get("errors"):
        stages.append(StageRecord(
            name="errors",
            status="error",
            duration_ms=0.0,
            detail=f"{len(data['errors'])} error(s)",
            count=len(data["errors"]),
            count_label="error_count",
            error_detail=data["errors"][0][:200],
        ))
    return stages


# ---------------------------------------------------------------------------
# Anomaly detection helpers
# ---------------------------------------------------------------------------

def detect_anomalies(report: PipelineReport, thresholds: dict = None) -> List[str]:
    """Simple rule-based anomaly detection over a single PipelineReport.

    Returns a list of human-readable anomaly descriptions (empty = clean).
    """
    if thresholds is None:
        thresholds = {
            "zero_new_after_first_run": False,   # only meaningful with history
            "max_stage_duration_ms": 300_000,    # 5 minutes per stage
            "max_warnings": 3,
        }
    alerts = []

    # Stage-level duration anomalies
    for s in report.stages:
        max_dur = thresholds.get("max_stage_duration_ms", 300_000)
        if s.duration_ms > max_dur:
            alerts.append(
                f"Stage '{s.name}' took {s.duration_ms:.0f}ms "
                f"(threshold {max_dur}ms)"
            )

    # Warning / error count anomalies
    if report.warning_count > thresholds.get("max_warnings", 3):
        alerts.append(
            f"{report.warning_count} warning(s) in pipeline '{report.pipeline}' "
            f"(threshold {thresholds.get('max_warnings')})"
        )
    if report.error_count > 0:
        alerts.append(
            f"{report.error_count} error(s) in pipeline '{report.pipeline}'"
        )

    return alerts


def summarize_pipeline_set(reports: List[PipelineReport]) -> dict:
    """Summarize a set of pipeline reports (e.g. all 3 sync runs + publisher).

    Returns a dict with keys:
        pipelines: list of pipeline names
        total_stages: int
        error_count: int
        warning_count: int
        total_duration_ms: float
        anomalies: list of strings
    """
    total_stages = sum(len(r.stages) for r in reports)
    error_count = sum(r.error_count for r in reports)
    warning_count = sum(r.warning_count for r in reports)
    total_duration = sum(r.total_duration_ms for r in reports)
    all_anomalies = []
    for r in reports:
        all_anomalies.extend(detect_anomalies(r))
    return {
        "pipelines": [r.pipeline for r in reports],
        "total_stages": total_stages,
        "error_count": error_count,
        "warning_count": warning_count,
        "total_duration_ms": round(total_duration, 1),
        "anomalies": all_anomalies,
    }
