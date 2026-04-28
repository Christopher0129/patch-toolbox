#!/usr/bin/env python3
"""
验证项目目录结构和必要文件是否存在。
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_DIRS = [
    "db",
    "scripts",
    "network-security",
    "system-vulnerabilities",
    "system-troubleshooting",
]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    ".gitignore",
    "scripts/utils.py",
    "scripts/sync_network_security.py",
    "scripts/sync_system_vulnerabilities.py",
    "scripts/sync_system_troubleshooting.py",
    "scripts/sync_publisher.py",
]

def main():
    errors = []
    for d in REQUIRED_DIRS:
        path = PROJECT_ROOT / d
        if not path.exists():
            errors.append(f"❌ 缺失目录: {d}")
        else:
            print(f"✅ 目录存在: {d}")
    
    for f in REQUIRED_FILES:
        path = PROJECT_ROOT / f
        if not path.exists():
            errors.append(f"❌ 缺失文件: {f}")
        else:
            print(f"✅ 文件存在: {f}")
    
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("✅ 项目结构完整")

if __name__ == "__main__":
    main()
