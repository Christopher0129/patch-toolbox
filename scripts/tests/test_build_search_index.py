import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts' / 'build_search_index.py'


def test_build_search_index_outputs_searchable_records(tmp_path: Path):
    out_file = tmp_path / 'search-index.json'
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--output', str(out_file)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(out_file.read_text(encoding='utf-8'))
    assert isinstance(payload, list) and payload
    first = payload[0]
    assert 'title' in first
    assert 'category' in first
    assert 'keywords' in first
    assert 'slug' in first
