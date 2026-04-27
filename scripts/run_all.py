#!/usr/bin/env python3
"""
Master Scheduler: 串行运行三个抓取agent + publisher
用法: python scripts/run_all.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import subprocess
import time

SCRIPTS_DIR = Path(__file__).resolve().parent

AGENTS = [
    ("网络安全漏洞", "agent_network_security.py"),
    ("系统漏洞", "agent_system_vulnerabilities.py"),
    ("系统故障", "agent_system_troubleshooting.py"),
]

PUBLISHER = "agent_publisher.py"
VENV_PYTHON = Path("/root/.openclaw/workspace/.venv/bin/python")


def run_script(name: str, script: str) -> int:
    print(f"\n{'='*60}")
    print(f"🚀 启动 Agent: {name}")
    print(f"{'='*60}")
    cmd = [str(VENV_PYTHON), str(SCRIPTS_DIR / script)]
    result = subprocess.run(cmd)
    print(f"✅ Agent {name} 退出码: {result.returncode}")
    return result.returncode


def main():
    print("=" * 60)
    print("🔁 Security Knowledge Base - 主调度器启动")
    print("=" * 60)

    for name, script in AGENTS:
        run_script(name, script)
        time.sleep(2)  # 短暂间隔，避免API rate limit

    # Publisher
    print(f"\n{'='*60}")
    print("📤 启动 Publisher Agent")
    print(f"{'='*60}")
    result = subprocess.run([str(VENV_PYTHON), str(SCRIPTS_DIR / PUBLISHER)])
    print(f"✅ Publisher 退出码: {result.returncode}")

    print("\n" + "=" * 60)
    print("🏁 全部任务完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
