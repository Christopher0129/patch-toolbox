#!/usr/bin/env python3
import argparse
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DBS = {
    'network_security': [
        ROOT / 'db' / 'netsec-windows.db',
        ROOT / 'db' / 'netsec-linux.db',
        ROOT / 'db' / 'netsec-macos.db',
    ],
    'system_vulnerabilities': [ROOT / 'db' / 'system-vulnerabilities.db'],
    'system_troubleshooting': [ROOT / 'db' / 'system-troubleshooting.db'],
}


def count_rows(db_path: Path) -> int:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM entries')
    value = cur.fetchone()[0]
    conn.close()
    return value


def count_rows_many(db_paths: list[Path]) -> int:
    return sum(count_rows(path) for path in db_paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    categories = {key: count_rows_many(paths) for key, paths in DBS.items()}
    payload = {
        'total_entries': sum(categories.values()),
        'categories': categories,
    }
    out_file = Path(args.output)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(out_file)


if __name__ == '__main__':
    main()
