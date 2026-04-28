#!/usr/bin/env python3
"""
验证 SQLite 数据库与 Markdown 文件的同步状态。
检查数据库文件是否存在且包含数据。
"""
import sys
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_ROOT / "db"

def check_db(db_name: str) -> tuple[bool, int]:
    db_path = DB_DIR / db_name
    if not db_path.exists():
        return False, 0
    try:
        conn = sqlite3.connect(str(db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM entries")
        count = cur.fetchone()[0]
        conn.close()
        return True, count
    except Exception as e:
        print(f"⚠️ {db_name} 检查失败: {e}")
        return False, 0

def main():
    dbs = [
        ("network-security.db", "网络安全漏洞"),
        ("system-vulnerabilities.db", "系统漏洞"),
        ("system-troubleshooting.db", "系统故障排障"),
    ]
    all_ok = True
    for db_name, label in dbs:
        exists, count = check_db(db_name)
        if not exists:
            print(f"❌ {label} ({db_name}): 数据库不存在")
            all_ok = False
        elif count == 0:
            print(f"⚠️ {label} ({db_name}): 数据库为空")
            all_ok = False
        else:
            print(f"✅ {label} ({db_name}): {count} 条记录")
    
    if not all_ok:
        sys.exit(1)
    print("✅ 所有数据库同步状态正常")

if __name__ == "__main__":
    main()
