#!/bin/bash
# Link Auditor 定时任务包装器
# 每12小时由 cron 调用

set -e

export GITHUB_TOKEN=$(bash ~/.github/get-token.sh)
PROJECT_DIR="/root/.openclaw/workspace/patch-toolbox"
cd "$PROJECT_DIR"

PYTHON="/root/.openclaw/workspace/.venv/bin/python"
$PYTHON scripts/agent_link_auditor.py >> "$PROJECT_DIR/agents/cron.log" 2>&1
