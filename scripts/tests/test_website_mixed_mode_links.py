from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_website_mentions_markdown_and_sqlite_access_paths():
    home = (ROOT / 'website' / 'src' / 'pages' / 'Home.tsx').read_text(encoding='utf-8')
    about = (ROOT / 'website' / 'src' / 'pages' / 'About.tsx').read_text(encoding='utf-8')
    assert 'Markdown' in home
    assert 'SQLite' in home
    assert 'markdown_path' in about or '原文' in about


def test_home_uses_generated_stats_and_categories_instead_of_legacy_hardcoded_counts():
    home = (ROOT / 'website' / 'src' / 'pages' / 'Home.tsx').read_text(encoding='utf-8')
    assert 'loadStats' in home
    assert 'loadCategories' in home
    assert '3154' not in home
    assert '452' not in home
    assert '3000+' not in home


def test_about_does_not_keep_legacy_entries_fallback():
    about = (ROOT / 'website' / 'src' / 'pages' / 'About.tsx').read_text(encoding='utf-8')
    assert 'loadStats' in about
    assert 'entries: 3154' not in about
    assert '3,154+' not in about
