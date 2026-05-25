from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def test_ci_check_builds_preview_artifact_for_pull_requests():
    workflow = (ROOT / '.github' / 'workflows' / 'ci-check.yml').read_text(encoding='utf-8')
    assert 'npm ci --legacy-peer-deps' in workflow
    assert 'npm test' in workflow or 'npm run test' in workflow
    assert 'npm run build' in workflow
    assert 'actions/upload-artifact' in workflow
    assert 'patch-toolbox-preview' in workflow


def test_ci_check_writes_review_summary():
    workflow = (ROOT / '.github' / 'workflows' / 'ci-check.yml').read_text(encoding='utf-8')
    assert 'GITHUB_STEP_SUMMARY' in workflow
    assert 'stats.json' in workflow
    assert 'categories.json' in workflow


def test_generated_website_data_is_not_tracked_source_input():
    result = subprocess.run(
        ['git', 'ls-files', 'website/public/data'],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == ''
