"""
Tests for network-security markdown generation from SQLite DB.

The current generate_ns_md() writes a single file (network-security/index.md).
These tests assert the desired 4-file split (index.md + windows.md + linux.md + macos.md)
and will fail until the implementation is updated.
"""
import sqlite3
from pathlib import Path
from scripts.regenerate_md import generate_ns_md


def _create_ns_db(db_path: Path) -> sqlite3.Connection:
    """Create an in-memory-like temp network-security DB matching the real schema."""
    conn = sqlite3.connect(str(db_path))
    conn.execute(
        """
        CREATE TABLE entries (
            id INTEGER PRIMARY KEY,
            hash TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            solution TEXT,
            severity TEXT,
            cvss_score REAL,
            source TEXT,
            source_url TEXT,
            refs TEXT,
            platform TEXT,
            tags TEXT,
            affected_products TEXT,
            published TEXT,
            last_modified TEXT,
            first_seen TEXT,
            last_updated TEXT
        )
        """
    )
    return conn


def _insert_entry(
    conn,
    hash_val: str,
    title: str,
    description: str = "",
    solution: str = "",
    severity: str = "HIGH",
    cvss_score: float = 7.5,
    source: str = "NVD",
    source_url: str = "",
    refs: str = "[]",
    platform: str = "",
    tags: str = '["cve","network"]',
    affected_products: str = "[]",
    published: str = "2026-04-30",
):
    conn.execute(
        """
        INSERT INTO entries
            (hash, title, description, solution, severity, cvss_score,
             source, source_url, refs, platform, tags, affected_products,
             published, last_modified, first_seen, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            hash_val,
            title,
            description,
            solution,
            severity,
            cvss_score,
            source,
            source_url,
            refs,
            platform,
            tags,
            affected_products,
            published,
            published,
            published,
            published,
        ),
    )
    conn.commit()


def test_generate_ns_md_writes_index_and_three_platform_files(tmp_path: Path):
    """
    Assert that generate_ns_md() writes 4 files: index.md, windows.md, linux.md, macos.md.

    Currently it writes only a single file, so this test is expected to FAIL
    until the implementation is updated to produce the 4-file split.
    """
    db_path = tmp_path / "network-security.db"
    conn = _create_ns_db(db_path)

    _insert_entry(conn, "hash-win-1", "Windows TCP/IP RCE", platform="windows")
    _insert_entry(conn, "hash-linux-1", "OpenSSH Remote Issue", platform="linux")
    _insert_entry(conn, "hash-macos-1", "Safari Network Stack Bug", platform="macos")

    out_dir = tmp_path / "network-security"
    out_dir.mkdir()

    # Current signature: generate_ns_md(conn, out_path: Path)
    # It expects a FILE path, not a directory.
    # After Task 2, it should accept a directory and write 4 files.
    generate_ns_md(conn, out_dir)

    assert (out_dir / "index.md").exists(), "index.md should be generated"
    assert (out_dir / "windows.md").exists(), "windows.md should be generated"
    assert (out_dir / "linux.md").exists(), "linux.md should be generated"
    assert (out_dir / "macos.md").exists(), "macos.md should be generated"


def test_generate_ns_md_index_links_to_three_platform_files(tmp_path: Path):
    """
    Assert that the generated index.md contains navigation links to all
    three platform files: windows.md, linux.md, macos.md.
    """
    db_path = tmp_path / "network-security.db"
    conn = _create_ns_db(db_path)

    _insert_entry(conn, "hash-win-1", "Windows TCP/IP RCE", platform="windows")

    out_dir = tmp_path / "network-security"
    out_dir.mkdir()

    generate_ns_md(conn, out_dir)

    index_text = (out_dir / "index.md").read_text(encoding="utf-8")
    assert "windows.md" in index_text, "index.md should link to windows.md"
    assert "linux.md" in index_text, "index.md should link to linux.md"
    assert "macos.md" in index_text, "index.md should link to macos.md"


def test_generate_ns_md_platform_files_contain_backlinks(tmp_path: Path):
    """
    Assert that each platform file contains a backlink to index.md.
    """
    db_path = tmp_path / "network-security.db"
    conn = _create_ns_db(db_path)

    _insert_entry(conn, "hash-win-1", "Windows TCP/IP RCE", platform="windows")
    _insert_entry(conn, "hash-linux-1", "OpenSSH Remote Issue", platform="linux")
    _insert_entry(conn, "hash-macos-1", "Safari Network Stack Bug", platform="macos")

    out_dir = tmp_path / "network-security"
    out_dir.mkdir()

    generate_ns_md(conn, out_dir)

    for platform in ("windows", "linux", "macos"):
        pf_path = out_dir / f"{platform}.md"
        assert pf_path.exists(), f"{platform}.md should exist"
        text = pf_path.read_text(encoding="utf-8")
        assert "index.md" in text, f"{platform}.md should contain backlink to index.md"


def test_generate_ns_md_index_total_includes_general_and_legacy_entries(tmp_path: Path):
    db_path = tmp_path / "network-security.db"
    conn = _create_ns_db(db_path)

    _insert_entry(conn, "hash-win-1", "Windows TCP/IP RCE", platform="windows")
    _insert_entry(conn, "hash-linux-1", "OpenSSH Remote Issue", platform="linux")
    _insert_entry(conn, "hash-macos-1", "Safari Network Stack Bug", platform="macos")
    _insert_entry(conn, "hash-general-1", "Generic Advisory", platform="general")
    _insert_entry(conn, "hash-legacy-1", "Legacy Imported Item", platform=None)

    out_dir = tmp_path / "network-security"
    out_dir.mkdir()

    generate_ns_md(conn, out_dir)

    index_text = (out_dir / "index.md").read_text(encoding="utf-8")
    assert "**总计条目 / Total entries: 5**" in index_text
