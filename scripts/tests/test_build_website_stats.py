import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts' / 'build_website_stats.py'
EXPORT_SCRIPT = ROOT / 'scripts' / 'export_website_data.py'


def test_build_website_stats_outputs_summary_payload(tmp_path: Path):
    out_file = tmp_path / 'stats.json'
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--output', str(out_file)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(out_file.read_text(encoding='utf-8'))
    assert payload['total_entries'] > 0
    assert 'network_security' in payload['categories']
    assert 'system_vulnerabilities' in payload['categories']
    assert 'system_troubleshooting' in payload['categories']


def test_build_website_stats_matches_exported_public_counts(tmp_path: Path):
    stats_file = tmp_path / 'stats.json'
    export_dir = tmp_path / 'website-data'

    stats_result = subprocess.run(
        [sys.executable, str(SCRIPT), '--output', str(stats_file)],
        capture_output=True,
        text=True,
    )
    assert stats_result.returncode == 0, stats_result.stderr

    export_result = subprocess.run(
        [sys.executable, str(EXPORT_SCRIPT), '--output-dir', str(export_dir)],
        capture_output=True,
        text=True,
    )
    assert export_result.returncode == 0, export_result.stderr

    stats = json.loads(stats_file.read_text(encoding='utf-8'))
    categories = json.loads((export_dir / 'categories.json').read_text(encoding='utf-8'))
    entries = json.loads((export_dir / 'entries.json').read_text(encoding='utf-8'))

    exported_counts = {item['key'].replace('-', '_'): item['entry_count'] for item in categories}
    assert stats['categories'] == exported_counts
    assert stats['total_entries'] == len(entries)
