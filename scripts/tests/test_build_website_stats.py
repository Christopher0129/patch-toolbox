import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts' / 'build_website_stats.py'


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
