"""Tests for stage_state.py — machine-readable Stage State for pipeline monitoring."""

import json
import time
from pathlib import Path

from scripts.stage_state import (
    StageRecord,
    StageTimer,
    PipelineReport,
    pipeline_report_to_dict,
    pipeline_report_to_json,
    stage_state_from_report_json,
    detect_anomalies,
    summarize_pipeline_set,
    run_timed,
)


class TestStageRecord:
    def test_minimal_record(self):
        r = StageRecord(name="fetch-A", status="ok", duration_ms=42.5)
        assert r.name == "fetch-A"
        assert r.status == "ok"
        assert r.duration_ms == 42.5
        assert r.detail == ""
        assert r.count is None
        assert r.count_label == ""
        assert r.error_detail is None

    def test_full_record(self):
        r = StageRecord(
            name="git-push",
            status="error",
            duration_ms=1234.0,
            detail="Push failed",
            count=3,
            count_label="retries",
            error_detail="timeout connecting to github.com",
        )
        assert r.name == "git-push"
        assert r.status == "error"
        assert r.count == 3
        assert r.error_detail == "timeout connecting to github.com"


class TestStageTimer:
    def test_timing_basic(self):
        timer = StageTimer()
        with timer:
            time.sleep(0.01)  # ~10ms
        elapsed = timer.elapsed_ms
        assert elapsed >= 5.0, f"Expected >=5ms, got {elapsed}ms"

    def test_to_record(self):
        timer = StageTimer()
        with timer:
            pass
        rec = timer.to_record("test", "ok", detail="done", count=5, count_label="items")
        assert rec.name == "test"
        assert rec.status == "ok"
        assert rec.detail == "done"
        assert rec.count == 5
        assert rec.count_label == "items"


class TestPipelineReport:
    def test_empty_report(self):
        r = PipelineReport(
            pipeline="sync-test",
            started_at="2026-01-01T00:00:00Z",
            finished_at="2026-01-01T00:01:00Z",
        )
        assert r.pipeline == "sync-test"
        assert r.stages == []
        assert r.total_duration_ms == 0.0
        assert r.all_ok is True
        assert r.error_count == 0
        assert r.warning_count == 0

    def test_with_stages(self):
        stages = [
            StageRecord(name="fetch", status="ok", duration_ms=1000),
            StageRecord(name="insert", status="ok", duration_ms=500),
            StageRecord(name="push", status="error", duration_ms=200, error_detail="auth failed"),
        ]
        r = PipelineReport(
            pipeline="sync-test",
            started_at="2026-01-01T00:00:00Z",
            finished_at="2026-01-01T00:01:00Z",
            stages=stages,
        )
        assert not r.all_ok
        assert r.error_count == 1
        assert r.warning_count == 0
        assert r.stages[0].name == "fetch"

    def test_to_dict(self):
        stages = [StageRecord(name="stage1", status="ok", duration_ms=100)]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        d = pipeline_report_to_dict(r)
        assert d["pipeline"] == "sync-test"
        assert len(d["stages"]) == 1
        assert d["stages"][0]["name"] == "stage1"
        assert d["version"] == 1

    def test_to_json(self):
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2",
            stages=[StageRecord(name="s1", status="ok", duration_ms=50)],
        )
        j = pipeline_report_to_json(r)
        loaded = json.loads(j)
        assert loaded["pipeline"] == "sync-test"
        assert loaded["stages"][0]["name"] == "s1"


class TestStageStateFromReportJson:
    def test_parses_legacy_report(self, tmp_path):
        report = {
            "sync": "sync-network-security",
            "timestamp": "2026-01-15T10:00:00Z",
            "new_items": 42,
            "total_items": 1000,
            "errors": ["fetch timeout", "parse error"],
        }
        p = tmp_path / "report.json"
        with open(p, "w") as f:
            json.dump(report, f)

        stages = stage_state_from_report_json(p)
        assert stages is not None
        assert len(stages) == 2
        assert stages[0].name == "sync-insert"
        assert stages[0].count == 42
        assert stages[0].count_label == "new_items"
        assert stages[1].name == "errors"
        assert stages[1].status == "error"
        assert stages[1].count == 2

    def test_returns_none_on_missing_file(self, tmp_path):
        p = tmp_path / "nonexistent.json"
        assert stage_state_from_report_json(p) is None

    def test_empty_report(self, tmp_path):
        report = {"sync": "empty", "timestamp": "T"}
        p = tmp_path / "empty.json"
        with open(p, "w") as f:
            json.dump(report, f)
        stages = stage_state_from_report_json(p)
        assert stages == []  # no new_items key


class TestDetectAnomalies:
    def test_no_anomalies_clean(self):
        stages = [
            StageRecord(name="fetch", status="ok", duration_ms=100),
            StageRecord(name="insert", status="ok", duration_ms=50),
        ]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        assert detect_anomalies(r) == []

    def test_duration_anomaly(self):
        stages = [
            StageRecord(name="slow-stage", status="ok", duration_ms=600_000),
        ]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        alerts = detect_anomalies(r)
        assert len(alerts) == 1
        assert "slow-stage" in alerts[0]

    def test_error_anomaly(self):
        stages = [
            StageRecord(name="fetch", status="error", duration_ms=100, error_detail="boom"),
        ]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        alerts = detect_anomalies(r)
        assert any("error(s)" in a for a in alerts)

    def test_warning_threshold(self):
        stages = [
            StageRecord(name=f"w{i}", status="warning", duration_ms=10)
            for i in range(5)
        ]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        alerts = detect_anomalies(r)
        assert any("warning(s)" in a for a in alerts)

    def test_custom_thresholds(self):
        stages = [
            StageRecord(name="s1", status="ok", duration_ms=500),
            StageRecord(name="s2", status="warning", duration_ms=0),
        ]
        r = PipelineReport(
            pipeline="sync-test", started_at="T1", finished_at="T2", stages=stages,
        )
        alerts = detect_anomalies(r, {"max_stage_duration_ms": 100, "max_warnings": 0})
        assert len(alerts) >= 2


class TestSummarizePipelineSet:
    def test_single_report(self):
        r = PipelineReport(
            pipeline="sync-a", started_at="T1", finished_at="T2",
            stages=[StageRecord(name="s1", status="ok", duration_ms=100)],
        )
        summary = summarize_pipeline_set([r])
        assert summary["pipelines"] == ["sync-a"]
        assert summary["total_stages"] == 1
        assert summary["error_count"] == 0
        assert summary["anomalies"] == []

    def test_mixed_reports(self):
        r1 = PipelineReport(
            pipeline="sync-a", started_at="T1", finished_at="T2",
            stages=[StageRecord(name="s1", status="ok", duration_ms=100)],
        )
        r2 = PipelineReport(
            pipeline="sync-b", started_at="T3", finished_at="T4",
            stages=[
                StageRecord(name="s1", status="error", duration_ms=500, error_detail="err"),
                StageRecord(name="s2", status="ok", duration_ms=300),
            ],
        )
        summary = summarize_pipeline_set([r1, r2])
        assert len(summary["pipelines"]) == 2
        assert summary["total_stages"] == 3
        assert summary["error_count"] == 1
        assert len(summary["anomalies"]) >= 1


class TestRunTimed:
    def test_basic(self):
        r = run_timed("check", "ok", "all good", count=7, count_label="items")
        assert r.name == "check"
        assert r.status == "ok"
        assert r.detail == "all good"
        assert r.count == 7
        assert r.duration_ms == 0.0
