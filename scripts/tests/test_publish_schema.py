"""
Tests for the publish artifact contract enforcement (publish_schema.py).

Validates that:
- The schema definitions correctly accept/reject payload variants
- The verify_artifacts() function detects missing files, schema violations, and cross-count mismatches
- The CLI tool works end-to-end
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest
from scripts.publish_schema import (
    ARTIFACT_SCHEMAS,
    REQUIRED_ARTIFACTS,
    validate_single,
    verify_artifacts,
    STATS_SCHEMA,
    CATEGORIES_ITEM_SCHEMA,
    ENTRY_ITEM_SCHEMA,
    SEARCH_INDEX_ITEM_SCHEMA,
)


# ── Schema definitions exist ────────────────────────────────────────────

class TestSchemaDefinitions:
    def test_all_required_artifacts_have_schemas(self):
        assert set(ARTIFACT_SCHEMAS.keys()) == set(REQUIRED_ARTIFACTS)

    def test_stats_schema_requires_total_entries_and_categories(self):
        required = STATS_SCHEMA.get("required", [])
        assert "total_entries" in required
        assert "categories" in required

    def test_categories_item_schema_requires_key_label_entry_count_markdown_path(self):
        required = CATEGORIES_ITEM_SCHEMA.get("required", [])
        assert "key" in required
        assert "label" in required
        assert "entry_count" in required
        assert "markdown_path" in required

    def test_entry_item_schema_requires_slug_title_category_markdown_path_source_url(self):
        required = ENTRY_ITEM_SCHEMA.get("required", [])
        assert "slug" in required
        assert "title" in required
        assert "category" in required
        assert "markdown_path" in required
        assert "source_url" in required

    def test_search_index_item_schema_requires_slug_title_category_keywords(self):
        required = SEARCH_INDEX_ITEM_SCHEMA.get("required", [])
        assert "slug" in required
        assert "title" in required
        assert "category" in required
        assert "keywords" in required


# ── validate_single ─────────────────────────────────────────────────────

class TestValidateSingle:
    def test_valid_stats_payload(self):
        payload = {
            "total_entries": 12000,
            "categories": {
                "network_security": 4000,
                "system_vulnerabilities": 5000,
                "system_troubleshooting": 3000,
            },
        }
        violations = validate_single(payload, "stats.json")
        assert violations == []

    def test_valid_stats_with_negative_total(self):
        payload = {
            "total_entries": -1,
            "categories": {
                "network_security": 0,
                "system_vulnerabilities": 0,
                "system_troubleshooting": 0,
            },
        }
        violations = validate_single(payload, "stats.json")
        assert any("total_entries" in v and "minimum" in v for v in violations)

    def test_stats_missing_categories(self):
        payload = {"total_entries": 100}
        violations = validate_single(payload, "stats.json")
        assert any("missing required field" in v and "'categories'" in v for v in violations)

    def test_stats_wrong_type_list(self):
        violations = validate_single([], "stats.json")
        assert any("expected object" in v for v in violations)

    def test_valid_entries_payload(self):
        payload = [
            {
                "slug": "network-security-1-test-entry",
                "title": "Test Entry",
                "description": "A description",
                "category": "network-security",
                "markdown_path": "network-security/windows.md",
                "source_url": "https://example.com",
            },
            {
                "slug": "system-vulnerabilities-2-another",
                "title": "Another Entry",
                "description": "",
                "category": "system-vulnerabilities",
                "markdown_path": "system-vulnerabilities/index.md",
                "source_url": "",
            },
        ]
        violations = validate_single(payload, "entries.json")
        assert violations == []

    def test_entries_missing_required_field(self):
        payload = [{"slug": "x", "title": "y", "category": "z"}]
        violations = validate_single(payload, "entries.json")
        # Missing markdown_path and source_url
        missing = [v for v in violations if "missing required field" in v]
        assert len(missing) == 2

    def test_entries_invalid_field_types(self):
        payload = [
            {
                "slug": 123,
                "title": "title",
                "description": "",
                "category": "netsec",
                "markdown_path": "path",
                "source_url": "url",
            }
        ]
        violations = validate_single(payload, "entries.json")
        assert any("slug" in v and "string" in v for v in violations)

    def test_empty_entries_list(self):
        violations = validate_single([], "entries.json")
        assert any("empty list" in v for v in violations)

    def test_entries_wrong_type_dict(self):
        violations = validate_single({}, "entries.json")
        assert any("expected list" in v for v in violations)

    def test_valid_categories_payload(self):
        payload = [
            {
                "key": "network-security",
                "label": "Network Security",
                "entry_count": 100,
                "markdown_path": "network-security/index.md",
            },
            {
                "key": "system-vulnerabilities",
                "label": "System Vulnerabilities",
                "entry_count": 200,
                "markdown_path": "system-vulnerabilities/index.md",
            },
        ]
        violations = validate_single(payload, "categories.json")
        assert violations == []

    def test_categories_entry_count_must_be_int(self):
        payload = [
            {
                "key": "network-security",
                "label": "Network Security",
                "entry_count": "100",
                "markdown_path": "network-security/index.md",
            }
        ]
        violations = validate_single(payload, "categories.json")
        assert any("entry_count" in v and "int" in v for v in violations)

    def test_categories_key_must_match_pattern(self):
        payload = [
            {
                "key": "Network Security",
                "label": "Network Security",
                "entry_count": 100,
                "markdown_path": "network-security/index.md",
            }
        ]
        violations = validate_single(payload, "categories.json")
        assert any("pattern" in v for v in violations)

    def test_valid_search_index_payload(self):
        payload = [
            {"slug": "a", "title": "Title", "category": "netsec", "keywords": "title title netsec"},
        ]
        violations = validate_single(payload, "search-index.json")
        assert violations == []

    def test_search_index_missing_keywords(self):
        payload = [{"slug": "a", "title": "Title", "category": "netsec"}]
        violations = validate_single(payload, "search-index.json")
        assert any("keywords" in v for v in violations)


# ── verify_artifacts ────────────────────────────────────────────────────

class TestVerifyArtifacts:
    def test_missing_artifacts_detected(self, tmp_path: Path):
        result = verify_artifacts(tmp_path)
        assert result["valid"] is False
        assert len(result["missing"]) == len(REQUIRED_ARTIFACTS)

    def test_all_valid_artifacts_pass(self, tmp_path: Path):
        _write_valid_artifacts(tmp_path)
        result = verify_artifacts(tmp_path)
        if not result["valid"]:
            pytest.fail(f"Expected valid artifacts, got: {result['violations']}")
        assert result["valid"] is True

    def test_cross_count_mismatch_detected(self, tmp_path: Path):
        _write_valid_artifacts(tmp_path)
        # Mutate stats.json to have wrong total
        stats = json.loads((tmp_path / "stats.json").read_text(encoding="utf-8"))
        stats["total_entries"] = 99999
        (tmp_path / "stats.json").write_text(json.dumps(stats), encoding="utf-8")

        result = verify_artifacts(tmp_path)
        assert result["valid"] is False
        assert any("stats.json vs entries.json" in pair[0] for pair in result["violations"])

    def test_corrupt_json_detected(self, tmp_path: Path):
        (tmp_path / "stats.json").write_text("not json", encoding="utf-8")
        # Write other files valid
        _write_valid_categories(tmp_path)
        _write_valid_entries(tmp_path)
        _write_valid_search_index(tmp_path)

        result = verify_artifacts(tmp_path)
        assert result["valid"] is False
        assert any("JSON parse error" in v[1] for v in result["violations"])

    def test_categories_entry_count_sum_mismatch(self, tmp_path: Path):
        _write_valid_artifacts(tmp_path)
        # Mutate categories sum to differ from entries count
        categories = json.loads((tmp_path / "categories.json").read_text(encoding="utf-8"))
        categories[0]["entry_count"] = 0
        (tmp_path / "categories.json").write_text(json.dumps(categories), encoding="utf-8")

        result = verify_artifacts(tmp_path)
        assert result["valid"] is False
        assert any("categories.json vs entries.json" in pair[0] for pair in result["violations"])

    def test_counts_in_result(self, tmp_path: Path):
        _write_valid_artifacts(tmp_path)
        result = verify_artifacts(tmp_path)
        assert "entries.json" in result["counts"]
        assert result["counts"]["entries.json"] > 0
        assert result["counts"]["stats.json"] > 0


# ── CLI ─────────────────────────────────────────────────────────────────

class TestCLI:
    def test_verify_valid_artifacts_via_cli(self, tmp_path: Path):
        _write_valid_artifacts(tmp_path)
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "publish_schema.py"),
             "verify", "--artifacts-dir", str(tmp_path)],
            capture_output=True, text=True,
        )
        assert result.returncode == 0, result.stderr
        assert "All artifacts valid" in result.stdout

    def test_verify_missing_artifacts_via_cli(self, tmp_path: Path):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "publish_schema.py"),
             "verify", "--artifacts-dir", str(tmp_path)],
            capture_output=True, text=True,
        )
        assert result.returncode == 1
        assert "Missing artifacts" in result.stdout

    def test_verify_nonexistent_directory(self, tmp_path: Path):
        nonexistent = tmp_path / "does-not-exist"
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "publish_schema.py"),
             "verify", "--artifacts-dir", str(nonexistent)],
            capture_output=True, text=True,
        )
        assert result.returncode == 1
        assert "Directory not found" in result.stdout

    def test_schema_subcommand(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "publish_schema.py"),
             "schema", "--artifact-type", "stats.json"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "total_entries" in result.stdout

    def test_schema_all_subcommand(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "publish_schema.py"),
             "schema", "--artifact-type", "all"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "stats.json" in result.stdout
        assert "entries.json" in result.stdout


# ── Helpers ─────────────────────────────────────────────────────────────

def _write_valid_artifacts(tmp_path: Path):
    """Write a full set of valid artifacts to tmp_path."""
    _write_valid_stats(tmp_path)
    _write_valid_categories(tmp_path)
    _write_valid_entries(tmp_path)
    _write_valid_search_index(tmp_path)


def _write_valid_stats(tmp_path: Path, total: int = 6):
    (tmp_path / "stats.json").write_text(json.dumps({
        "total_entries": total,
        "categories": {
            "network_security": 3,
            "system_vulnerabilities": 2,
            "system_troubleshooting": 1,
        },
    }), encoding="utf-8")


def _write_valid_categories(tmp_path: Path):
    (tmp_path / "categories.json").write_text(json.dumps([
        {"key": "network-security", "label": "Network Security",
         "entry_count": 3, "markdown_path": "network-security/index.md",
         "platforms": ["windows", "linux", "macos"]},
        {"key": "system-vulnerabilities", "label": "System Vulnerabilities",
         "entry_count": 2, "markdown_path": "system-vulnerabilities/index.md"},
        {"key": "system-troubleshooting", "label": "System Troubleshooting",
         "entry_count": 1, "markdown_path": "system-troubleshooting/index.md"},
    ]), encoding="utf-8")


def _write_valid_entries(tmp_path: Path):
    (tmp_path / "entries.json").write_text(json.dumps([
        {
            "slug": "network-security-1-win-entry",
            "title": "Windows TCP/IP RCE",
            "description": "A critical RCE",
            "category": "network-security",
            "markdown_path": "network-security/windows.md",
            "source_url": "https://example.com/1",
            "platform": "windows",
        },
        {
            "slug": "network-security-2-linux-entry",
            "title": "OpenSSH Issue",
            "description": "",
            "category": "network-security",
            "markdown_path": "network-security/linux.md",
            "source_url": "https://example.com/2",
            "platform": "linux",
        },
        {
            "slug": "network-security-3-macos-entry",
            "title": "Safari Bug",
            "description": "",
            "category": "network-security",
            "markdown_path": "network-security/macos.md",
            "source_url": "",
            "platform": "macos",
        },
        {
            "slug": "system-vulnerabilities-1-win-vuln",
            "title": "Win32k EoP",
            "description": "",
            "category": "system-vulnerabilities",
            "markdown_path": "system-vulnerabilities/windows.md",
            "source_url": "https://example.com/4",
        },
        {
            "slug": "system-vulnerabilities-2-linux-vuln",
            "title": "Kernel Bug",
            "description": "",
            "category": "system-vulnerabilities",
            "markdown_path": "system-vulnerabilities/linux.md",
            "source_url": "",
        },
        {
            "slug": "system-troubleshooting-1-win-trouble",
            "title": "BSOD Guide",
            "description": "",
            "category": "system-troubleshooting",
            "markdown_path": "system-troubleshooting/index.md",
            "source_url": "",
        },
    ]), encoding="utf-8")


def _write_valid_search_index(tmp_path: Path):
    (tmp_path / "search-index.json").write_text(json.dumps([
        {"slug": "ns-1", "title": "Windows TCP/IP RCE",
         "category": "network-security",
         "keywords": "Windows TCP/IP RCE A critical RCE network-security"},
        {"slug": "ns-2", "title": "OpenSSH Issue",
         "category": "network-security",
         "keywords": "OpenSSH Issue network-security"},
        {"slug": "sv-1", "title": "Win32k EoP",
         "category": "system-vulnerabilities",
         "keywords": "Win32k EoP system-vulnerabilities"},
    ]), encoding="utf-8")
