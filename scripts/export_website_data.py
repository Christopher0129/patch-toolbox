#!/usr/bin/env python3
import argparse
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CATEGORY_MAP = {
    'network-security': {
        'db': ROOT / 'db' / 'network-security.db',
        'markdown': ROOT / 'network-security' / 'index.md',
        'label': 'Network Security',
    },
    'system-vulnerabilities': {
        'db': ROOT / 'db' / 'system-vulnerabilities.db',
        'markdown': ROOT / 'system-vulnerabilities' / 'index.md',
        'label': 'System Vulnerabilities',
    },
    'system-troubleshooting': {
        'db': ROOT / 'db' / 'system-troubleshooting.db',
        'markdown': ROOT / 'system-troubleshooting' / 'index.md',
        'label': 'System Troubleshooting',
    },
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '-', text)
    return text.strip('-') or 'entry'


def load_entries(category_key: str, db_path: Path, markdown_path: Path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT title, description, source_url FROM entries ORDER BY id DESC LIMIT 50')
    rows = cur.fetchall()
    conn.close()
    entries = []
    for idx, (title, description, source_url) in enumerate(rows, start=1):
        entries.append({
            'slug': f'{category_key}-{idx}-{slugify(title)}',
            'title': title,
            'description': description or '',
            'category': category_key,
            'markdown_path': str(markdown_path.relative_to(ROOT)),
            'source_url': source_url or '',
        })
    return entries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    categories = []
    all_entries = []
    for key, cfg in CATEGORY_MAP.items():
        entries = load_entries(key, cfg['db'], cfg['markdown'])
        categories.append({
            'key': key,
            'label': cfg['label'],
            'entry_count': len(entries),
            'markdown_path': str(cfg['markdown'].relative_to(ROOT)),
        })
        all_entries.extend(entries)

    (out_dir / 'categories.json').write_text(
        json.dumps(categories, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    (out_dir / 'entries.json').write_text(
        json.dumps(all_entries, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    print(out_dir)


if __name__ == '__main__':
    main()
