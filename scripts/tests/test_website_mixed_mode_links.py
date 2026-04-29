from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_website_mentions_markdown_and_sqlite_access_paths():
    home = (ROOT / 'website' / 'src' / 'pages' / 'Home.tsx').read_text(encoding='utf-8')
    about = (ROOT / 'website' / 'src' / 'pages' / 'About.tsx').read_text(encoding='utf-8')
    assert 'Markdown' in home
    assert 'SQLite' in home
    assert 'markdown_path' in about or '原文' in about
