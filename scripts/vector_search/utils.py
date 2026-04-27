"""
向量搜索模块工具函数
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List


def vec_to_json(vec: List[float]) -> str:
    """将向量转为 sqlite-vec 接受的 JSON 字符串。"""
    return json.dumps(vec)


def vec_to_blob(vec: List[float]) -> bytes:
    """将向量转为二进制 blob（float32）。"""
    import struct
    return struct.pack(f"<{len(vec)}f", *vec)


def ensure_entries_fts(conn: sqlite3.Connection):
    """确保 entries_fts (FTS5) 虚拟表存在。"""
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
            title, description, solution,
            content='entries', content_rowid='id'
        )
    """)
    conn.commit()


def sync_entries_fts_incremental(conn: sqlite3.Connection, entry_ids: List[int]):
    """
    将指定 entries 同步到 FTS5 索引。用于增量更新。
    先删后插（幂等）。
    """
    if not entry_ids:
        return
    ensure_entries_fts(conn)
    placeholders = ",".join("?" * len(entry_ids))
    # 删除旧索引
    conn.execute(f"DELETE FROM entries_fts WHERE rowid IN ({placeholders})", tuple(entry_ids))
    # 插入新索引
    c = conn.execute(
        f"SELECT id, title, description, solution FROM entries WHERE id IN ({placeholders})",
        tuple(entry_ids),
    )
    for row in c.fetchall():
        conn.execute(
            "INSERT INTO entries_fts(rowid, title, description, solution) VALUES (?, ?, ?, ?)",
            row,
        )
    conn.commit()


def rebuild_entries_fts(conn: sqlite3.Connection):
    """全量重建 FTS5 索引。"""
    conn.execute("DROP TABLE IF EXISTS entries_fts")
    conn.commit()
    ensure_entries_fts(conn)
    c = conn.execute("SELECT id, title, description, solution FROM entries")
    for row in c.fetchall():
        conn.execute(
            "INSERT INTO entries_fts(rowid, title, description, solution) VALUES (?, ?, ?, ?)",
            row,
        )
    conn.commit()
