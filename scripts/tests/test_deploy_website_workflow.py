from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_deploy_workflow_exists_and_runs_build_transform_steps():
    workflow = (ROOT / '.github' / 'workflows' / 'deploy-website.yml').read_text(encoding='utf-8')
    assert 'export_website_data.py' in workflow
    assert 'build_website_stats.py' in workflow
    assert 'build_search_index.py' in workflow
    assert 'npm ci' in workflow
    assert 'npm run build' in workflow
    assert 'actions/deploy-pages' in workflow
