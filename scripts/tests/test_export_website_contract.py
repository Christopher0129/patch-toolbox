import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts' / 'export_website_data.py'


def test_export_website_data_outputs_expected_contract(tmp_path: Path):
    out_dir = tmp_path / 'website-data'
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--output-dir', str(out_dir)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr

    categories = json.loads((out_dir / 'categories.json').read_text(encoding='utf-8'))
    details = json.loads((out_dir / 'entries.json').read_text(encoding='utf-8'))

    assert isinstance(categories, list) and categories, 'categories.json should contain items'
    assert isinstance(details, list) and details, 'entries.json should contain items'
    first = details[0]
    assert 'slug' in first
    assert 'title' in first
    assert 'category' in first
    assert 'markdown_path' in first
    assert 'source_url' in first


def test_export_website_data_exposes_full_public_db_counts(tmp_path: Path):
    out_dir = tmp_path / 'website-data'
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--output-dir', str(out_dir)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr

    categories = json.loads((out_dir / 'categories.json').read_text(encoding='utf-8'))
    details = json.loads((out_dir / 'entries.json').read_text(encoding='utf-8'))

    total_from_categories = sum(item['entry_count'] for item in categories)
    assert len(details) == total_from_categories
    assert len(details) > 150
