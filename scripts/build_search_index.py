#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORT_SCRIPT = ROOT / 'scripts' / 'export_website_data.py'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    tmp_dir = ROOT / 'website' / 'public' / 'data' / '_tmp-export'
    tmp_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(EXPORT_SCRIPT), '--output-dir', str(tmp_dir)], check=True)
    entries = json.loads((tmp_dir / 'entries.json').read_text(encoding='utf-8'))

    payload = []
    for item in entries:
        payload.append({
            'slug': item['slug'],
            'title': item['title'],
            'category': item['category'],
            'keywords': f"{item['title']} {item['description']} {item['category']}",
        })

    out_file = Path(args.output)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(out_file)


if __name__ == '__main__':
    main()
