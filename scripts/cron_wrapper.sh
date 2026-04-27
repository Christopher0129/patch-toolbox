#!/bin/bash
# Security KB 自动化工作流 Wrapper
# 每小时由 cron 调用

set -e

# GitHub Token
export GITHUB_TOKEN=$(bash ~/.github/get-token.sh)

# 项目目录
PROJECT_DIR="/root/.openclaw/workspace/patch-toolbox"
cd "$PROJECT_DIR"

# Python 环境
PYTHON="/root/.openclaw/workspace/.venv/bin/python"

# 运行主调度器
$PYTHON scripts/run_all.py >> "$PROJECT_DIR/agents/cron.log" 2>&1
