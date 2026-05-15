"""Tests for sync_publisher.py structured PipelineReport generation.

Tests that the publisher emits a valid PipelineReport JSON file
with correct stage states and aggregated metadata.
"""

import json
import sys
import subprocess
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
AGENTS_DIR = PROJECT_ROOT / "agents"


class TestPublisherStructuredReport:
    """Test that sync_publisher's structured report output is valid and public-safe."""

    def test_pipeline_report_latest_exists(self):
        """If publisher has ever run, pipeline_report_latest.json should be valid JSON."""
        report_path = AGENTS_DIR / "pipeline_report_latest.json"
        if not report_path.exists():
            pytest.skip("pipeline_report_latest.json not found — publisher hasn't run")
        with open(report_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert "pipeline" in data
        assert "stages" in data
        assert isinstance(data["stages"], list)
        # All stages must have required fields
        for stage in data["stages"]:
            assert "name" in stage
            assert "status" in stage
            assert stage["status"] in ("ok", "warning", "error")
            assert "duration_ms" in stage
            assert isinstance(stage["duration_ms"], (int, float))
        assert "aggregated" in data
        assert "total_new" in data["aggregated"]
        assert isinstance(data["aggregated"]["total_new"], int)

    def test_report_public_safety(self):
        """Ensure no private runtime details leak into the structured report."""
        report_path = AGENTS_DIR / "pipeline_report_latest.json"
        if not report_path.exists():
            pytest.skip("report not available")

        raw = report_path.read_text(encoding="utf-8")
        private_patterns = [
            "GITHUB_TOKEN", "PATCH_TOOLBOX_TOKEN", "VECTOR_API_KEY",
            "PATCH_TOOLBOX_GIT_NAME", "PATCH_TOOLBOX_GIT_EMAIL",
            "api_key", "password", "secret", "token",
        ]
        for pattern in private_patterns:
            assert pattern not in raw, f"Private token pattern {pattern!r} leaked into report"

    def test_report_safe_default_fields(self):
        """Check that the aggregated dict has all expected safe fields."""
        report_path = AGENTS_DIR / "pipeline_report_latest.json"
        if not report_path.exists():
            pytest.skip("report not available")

        data = json.loads(report_path.read_text(encoding="utf-8"))
        agg = data.get("aggregated", {})
        for field in ("total_new", "total_all", "upstream_errors", "pipeline_all_ok"):
            assert field in agg, f"aggregated.{field} missing from structured report"

    def test_pipeline_report_has_version(self):
        """Schema version field should be present."""
        report_path = AGENTS_DIR / "pipeline_report_latest.json"
        if not report_path.exists():
            pytest.skip("report not available")

        data = json.loads(report_path.read_text(encoding="utf-8"))
        assert "version" in data, "PipelineReport must have version field"
        assert data["version"] >= 1, "version must be >= 1"

    def test_stage_state_files_exist_for_all_syncs(self):
        """Verify each sync script writes a _stages.json alongside its legacy report.

        This test requires a prior run to produce the files; it is informational.
        """
        sync_names = [
            "sync-network-security",
            "sync-system-vulnerabilities",
            "sync-system-troubleshooting",
            "sync-link-auditor",
            "sync-publisher",
        ]
        existing = []
        for name in sync_names:
            stages_file = AGENTS_DIR / f"{name}_stages.json"
            if stages_file.exists():
                existing.append(name)
                with open(stages_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                assert "pipeline" in data
                assert data["pipeline"] == name
                assert "stages" in data
                assert isinstance(data["stages"], list)
        if not existing:
            pytest.skip("No _stages.json files found — run a sync first then re-run this test")
        assert len(existing) > 0, "Expected at least one _stages.json"
        # Verify version field on at least one report
        for name in existing:
            with open(AGENTS_DIR / f"{name}_stages.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            assert "version" in data, f"{name}_stages.json missing version field"
