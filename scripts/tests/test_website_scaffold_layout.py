import subprocess
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
        ROOT / 'website' / 'src' / 'lib' / 'utils.ts',
    ]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.exists()]
    assert not missing, f'missing website scaffold files: {missing}'


def test_website_utils_is_tracked_in_git():
    result = subprocess.run(
        ['git', 'ls-files', '--error-unmatch', 'website/src/lib/utils.ts'],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, 'website/src/lib/utils.ts must be committed, not left untracked'
