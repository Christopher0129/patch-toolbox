from pathlib import Path
import json
import sqlite3

from scripts.export_website_data import load_entries


def test_load_entries_includes_platform_and_platform_markdown_path(tmp_path: Path):
    db_path = tmp_path / "network-security.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE entries (id INTEGER PRIMARY KEY, title TEXT, description TEXT, source_url TEXT)")
    conn.execute(
        "INSERT INTO entries (title, description, source_url) VALUES (?, ?, ?)",
        ("Windows TCP/IP RCE", "desc", "https://example.com/windows-rce"),
    )
    conn.commit()
    conn.close()

    markdown_path = tmp_path / "windows.md"
    markdown_path.write_text("# Windows 网络漏洞\n", encoding="utf-8")

    entries = load_entries("network-security", db_path, markdown_path, platform="windows")

    assert entries[0]["category"] == "network-security"
    assert entries[0]["platform"] == "windows"
    assert entries[0]["markdown_path"].endswith("windows.md")


def test_network_security_export_can_merge_multiple_platform_files(tmp_path: Path):
    db_path = tmp_path / "network-security.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE entries (id INTEGER PRIMARY KEY, title TEXT, description TEXT, source_url TEXT)")
    conn.execute("INSERT INTO entries (title, description, source_url) VALUES ('Entry A', 'desc a', 'https://example.com/a')")
    conn.execute("INSERT INTO entries (title, description, source_url) VALUES ('Entry B', 'desc b', 'https://example.com/b')")
    conn.commit()
    conn.close()

    windows_entries = load_entries("network-security", db_path, tmp_path / "windows.md", platform="windows")
    linux_entries = load_entries("network-security", db_path, tmp_path / "linux.md", platform="linux")

    assert all(item["platform"] == "windows" for item in windows_entries)
    assert all(item["platform"] == "linux" for item in linux_entries)
