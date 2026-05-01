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
        'platforms': {
            'windows': {
                'db': ROOT / 'db' / 'netsec-windows.db',
                'markdown': ROOT / 'network-security' / 'windows.md',
            },
            'linux': {
                'db': ROOT / 'db' / 'netsec-linux.db',
                'markdown': ROOT / 'network-security' / 'linux.md',
            },
            'macos': {
                'db': ROOT / 'db' / 'netsec-macos.db',
                'markdown': ROOT / 'network-security' / 'macos.md',
            },
        },
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


def _friendly_md_path(markdown_path: Path) -> str:
    try:
        return str(markdown_path.relative_to(ROOT))
    except ValueError:
        return str(markdown_path)


def load_entries(category_key: str, db_path: Path, markdown_path: Path, platform: str | None = None):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT title, description, source_url FROM entries ORDER BY id DESC LIMIT 50')
    rows = cur.fetchall()
    conn.close()
    entries = []
    for idx, (title, description, source_url) in enumerate(rows, start=1):
        entry = {
            'slug': f'{category_key}-{idx}-{slugify(title)}',
            'title': title,
            'description': description or '',
            'category': category_key,
            'markdown_path': _friendly_md_path(markdown_path),
            'source_url': source_url or '',
        }
        if platform:
            entry['platform'] = platform
        entries.append(entry)
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
        platforms_cfg = cfg.get('platforms')
        if platforms_cfg:
            platform_labels = []
            for plat_key, plat_cfg in platforms_cfg.items():
                entries = load_entries(key, plat_cfg['db'], plat_cfg['markdown'], platform=plat_key)
                platform_labels.append(plat_key)
                all_entries.extend(entries)
            categories.append({
                'key': key,
                'label': cfg['label'],
                'entry_count': len(all_entries),
                'markdown_path': str(cfg['markdown'].relative_to(ROOT)),
                'platforms': platform_labels,
            })
        else:
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
