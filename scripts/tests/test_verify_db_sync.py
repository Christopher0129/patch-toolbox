"""Tests for verify_db_sync.py — reusable verify_sync_state()"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from verify_db_sync import verify_sync_state, check_db


def test_verify_sync_state_returns_dict():
    result = verify_sync_state()
    assert isinstance(result, dict)
    assert "ok" in result
    assert "databases" in result
    assert "summary" in result
    assert "total_entries" in result


def test_verify_sync_state_has_expected_databases():
    result = verify_sync_state()
    db_names = [d["name"] for d in result["databases"]]
    assert "network-security.db" in db_names
    assert "system-vulnerabilities.db" in db_names
    assert "system-troubleshooting.db" in db_names


def test_verify_sync_state_entries_are_counted():
    result = verify_sync_state()
    assert result["total_entries"] >= 0
    # Each db entry should have a count >= 0
    for d in result["databases"]:
        assert d["count"] >= 0


def test_check_db_returns_tuple():
    exists, ok, count = check_db("network-security.db")
    assert isinstance(exists, bool)
    assert isinstance(ok, bool)
    assert isinstance(count, int)


def test_check_db_nonexistent():
    exists, ok, count = check_db("nonexistent.db")
    assert exists is False
    assert ok is False
    assert count == 0


def test_verify_state_summary_contains_all_labels():
    result = verify_sync_state()
    for d in result["databases"]:
        assert d["label"] in result["summary"] or d["name"] in result["summary"]
