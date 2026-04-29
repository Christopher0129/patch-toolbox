from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_website_reads_generated_static_data_files():
    content_lib = (ROOT / 'website' / 'src' / 'lib' / 'content.ts').read_text(encoding='utf-8')
    assert '/data/categories.json' in content_lib
    assert '/data/entries.json' in content_lib
    assert '/data/stats.json' in content_lib
    assert '/data/search-index.json' in content_lib
