"""Tests for sync_publisher.py — stage boundaries, preflight, verify handoff"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils import log_stage_start, log_stage_end, preflight_check
from sync_publisher import read_report, _fallback_sync_name, count_from_sqlite


def test_log_stage_start_does_not_raise():
    # Should write to log file without error
    log_stage_start("TEST_STAGE")
    log_stage_start("Another_STAGE_123")


def test_log_stage_end_does_not_raise():
    log_stage_end("TEST_STAGE", "OK", "details here")
    log_stage_end("TEST_STAGE", "FAIL")


def test_read_report_missing_file():
    fake = Path("/tmp/nonexistent_report_xyz.json")
    result = read_report(fake)
    assert isinstance(result, dict)
    assert result["new_items"] == 0
    assert result["total_items"] == 0
    assert result["errors"] == []
    assert "timestamp" in result


def test_fallback_sync_name():
    assert _fallback_sync_name(Path("/tmp/sync-network-security_report.json")) == "sync-network-security"
    assert _fallback_sync_name(Path("/tmp/foo_report.json")) == "foo"


def test_count_from_sqlite_returns_dict():
    counts = count_from_sqlite()
    assert isinstance(counts, dict)
    for key in ("network-security", "system-vulnerabilities", "system-troubleshooting"):
        assert key in counts
        assert isinstance(counts[key], int)


def test_preflight_check_returns_dict():
    result = preflight_check()
    assert isinstance(result, dict)
    assert "ok" in result
    assert "checks" in result
    assert "summary" in result
    assert isinstance(result["checks"], list)


def test_preflight_check_has_core_checks():
    result = preflight_check(require_agents_dir=False)
    check_names = [c["name"] for c in result["checks"]]
    assert "db/network-security" in check_names
    assert "db/system-vulnerabilities" in check_names
    assert "db/system-troubleshooting" in check_names
    assert "git_repo" in check_names


def test_preflight_check_agents_dir():
    result = preflight_check(require_agents_dir=True)
    check_names = [c["name"] for c in result["checks"]]
    assert "agents_dir" in check_names


def test_preflight_check_produces_countable_checks():
    result = preflight_check()
    ok_count = sum(1 for c in result["checks"] if c["ok"])
    assert result["summary"].startswith(f"{ok_count}/")
    assert "checks passed" in result["summary"]
