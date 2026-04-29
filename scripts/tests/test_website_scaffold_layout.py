from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_website_scaffold_files_exist():
    expected = [
        ROOT / 'website' / 'package.json',
        ROOT / 'website' / 'vite.config.ts',
        ROOT / 'website' / 'index.html',
        ROOT / 'website' / 'src' / 'main.tsx',
        ROOT / 'website' / 'src' / 'App.tsx',
        ROOT / 'website' / 'src' / 'index.css',
    ]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.exists()]
    assert not missing, f'missing website scaffold files: {missing}'
