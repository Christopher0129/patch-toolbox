"""
Regression test for sync_network_security.py — verify automation handoff rules
reference the correct platform file targets and no single-file assumption remains.
"""

from pathlib import Path
import ast
import sys


def test_sync_network_security_docstring_refers_to_platform_files():
    """The docstring must explicitly reference windows.md / linux.md / macos.md
    and state that index.md is navigation-only."""
    script_path = Path(__file__).resolve().parent.parent / "sync_network_security.py"
    assert script_path.exists(), f"sync_network_security.py not found at {script_path}"

    text = script_path.read_text(encoding="utf-8")

    # The docstring section after "Automation Handoff Rules" must contain
    # the platform output target rules.
    assert "network-security/windows.md" in text, (
        "sync_network_security.py docstring must reference network-security/windows.md"
    )
    assert "network-security/linux.md" in text, (
        "sync_network_security.py docstring must reference network-security/linux.md"
    )
    assert "network-security/macos.md" in text, (
        "sync_network_security.py docstring must reference network-security/macos.md"
    )
    assert "network-security/index.md" in text, (
        "sync_network_security.py docstring must reference network-security/index.md"
    )

    # Confirm the pure-3-platform split (no "general" bucket in the output rules)
    assert "windows.md" in text
    assert "linux.md" in text
    assert "macos.md" in text
    # There should be no reference to a "general" output file
    assert "general.md" not in text, "Pure 3-platform split: no general.md in output rules"


def test_sync_network_security_pure_three_platform_run_loop():
    """The run() function iterates over exactly ['windows', 'linux', 'macos']"""
    script_path = Path(__file__).resolve().parent.parent / "sync_network_security.py"
    text = script_path.read_text(encoding="utf-8")

    assert 'for os_name in ["windows", "linux", "macos"]:' in text, (
        "run() must iterate exactly ['windows', 'linux', 'macos']"
    )
    # Check that the run loop does NOT iterate over 'general'
    lines = text.split('\n')
    for_loop_line = None
    for line in lines:
        if 'for os_name in' in line and 'window' in line.lower():
            for_loop_line = line
            break
    assert for_loop_line is not None, "Could not find the os_name for-loop"
    assert '"general"' not in for_loop_line, "Run loop must not include 'general'"


def test_sync_network_security_output_dir_is_network_security():
    """OUTPUT_DIR should point to the network-security directory"""
    script_path = Path(__file__).resolve().parent.parent / "sync_network_security.py"
    text = script_path.read_text(encoding="utf-8")
    assert 'OUTPUT_DIR = Path(__file__).resolve().parent.parent / "network-security"' in text, (
        "OUTPUT_DIR must be network-security/"
    )
