#!/usr/bin/env python3
"""
验证 SQLite 数据库与 Markdown 文件的同步状态。
检查数据库文件是否存在且包含数据。

提供:
- verify_sync_state() -> dict: 可复用的验证函数，供 publisher/preflight 使用
- main(): CLI 入口，保持向后兼容
"""
import sys
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_ROOT / "db"

DB_CHECKS = [
    ("network-security.db", "网络安全漏洞"),
    ("system-vulnerabilities.db", "系统漏洞"),
    ("system-troubleshooting.db", "系统故障排障"),
]


def check_db(db_name: str) -> tuple:
    """返回 (文件存在, 查询成功, 记录数)"""
    db_path = DB_DIR / db_name
    if not db_path.exists():
        return False, False, 0
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM entries")
        count = cur.fetchone()[0]
        conn.close()
        return True, True, count
    except Exception as e:
        print(f"⚠️ {db_name} 查询失败: {e}")
        if conn:
            conn.close()
        return True, False, 0


def verify_sync_state() -> dict:
    """可复用的验证函数，返回详细的状态字典。
    
    返回格式:
    {
        "ok": bool,           # 所有检查通过
        "databases": [
            {"name": str, "label": str, "exists": bool, "query_ok": bool, "count": int}
        ],
        "summary": str,       # 人类可读摘要
        "total_entries": int,  # 所有 DB 合计
    }
    """
    results = []
    total_entries = 0
    all_ok = True

    for db_name, label in DB_CHECKS:
        exists, ok, count = check_db(db_name)
        results.append({
            "name": db_name,
            "label": label,
            "exists": exists,
            "query_ok": ok,
            "count": count,
        })
        if not exists:
            all_ok = False
        elif not ok:
            all_ok = False
        elif count == 0:
            all_ok = False
        total_entries += count

    summary_parts = []
    for r in results:
        if not r["exists"]:
            summary_parts.append(f"❌ {r['label']}: 文件不存在")
        elif not r["query_ok"]:
            summary_parts.append(f"❌ {r['label']}: 查询失败")
        elif r["count"] == 0:
            summary_parts.append(f"⚠️ {r['label']}: 为空")
        else:
            summary_parts.append(f"✅ {r['label']}: {r['count']} 条")

    return {
        "ok": all_ok,
        "databases": results,
        "summary": " | ".join(summary_parts),
        "total_entries": total_entries,
    }


def main():
    result = verify_sync_state()
    print(result["summary"])
    if not result["ok"]:
        sys.exit(1)
    print(f"✅ 所有数据库同步状态正常（合计 {result['total_entries']} 条）")


if __name__ == "__main__":
    main()
