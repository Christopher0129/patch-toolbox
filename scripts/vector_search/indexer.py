"""
索引管理 - sqlite-vec 虚拟表创建、增量索引、全量重建
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .config import VectorConfig
from .embedder import Embedder


class VectorIndexer:
    """
    负责维护 sqlite-vec 虚拟表，增量/全量生成嵌入。
    """

    def __init__(self, db_path: Path, config: VectorConfig, embedder: Embedder):
        self.db_path = Path(db_path)
        self.config = config
        self.embedder = embedder
        self.dimension = config.dimension
        self.distance_metric = config.distance_metric  # cosine | l2

    # ------------------------------------------------------------------
    # 初始化
    # ------------------------------------------------------------------

    def _load_extension(self, conn: sqlite3.Connection):
        """加载 sqlite-vec 扩展。"""
        try:
            import sqlite_vec
            sqlite_vec.load(conn)
        except Exception:
            # 备用：尝试直接 .load 命令（若扩展文件在系统路径）
            try:
                conn.enable_load_extension(True)
                conn.execute("SELECT load_extension('vec')")
            except Exception as e:
                raise RuntimeError(
                    "Failed to load sqlite-vec extension. "
                    "Install: pip install sqlite-vec"
                ) from e

    def _ensure_vec_table(self, conn: sqlite3.Connection):
        """确保 vec_entries 虚拟表存在。"""
        self._load_extension(conn)
        metric = self.distance_metric  # cosine | l2
        # sqlite-vec 虚拟表语法
        conn.execute(f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS vec_entries USING vec0(
                entry_id INTEGER PRIMARY KEY,
                embedding float[{self.dimension}] distance_metric={metric}
            )
        """)
        conn.commit()

    # ------------------------------------------------------------------
    # 索引统计
    # ------------------------------------------------------------------

    def count(self) -> int:
        with sqlite3.connect(self.db_path) as conn:
            try:
                self._load_extension(conn)
                c = conn.execute("SELECT COUNT(*) FROM vec_entries")
                return c.fetchone()[0]
            except Exception:
                return 0

    def _get_unindexed_ids(self, conn: sqlite3.Connection, platform: Optional[str] = None) -> List[int]:
        """获取还没有向量的 entry id 列表。"""
        sql = """
            SELECT e.id FROM entries e
            LEFT JOIN vec_entries v ON e.id = v.entry_id
            WHERE v.entry_id IS NULL
        """
        params: Tuple = ()
        if platform:
            sql += " AND e.platform = ?"
            params = (platform,)
        sql += " ORDER BY e.id"
        c = conn.execute(sql, params)
        return [row[0] for row in c.fetchall()]

    # ------------------------------------------------------------------
    # 增量索引
    # ------------------------------------------------------------------

    def incremental_index(self, platform: Optional[str] = None) -> Dict[str, int]:
        """
        只给尚未索引的条目生成向量并插入。
        返回 {'indexed': 新增数, 'total': 总数}
        """
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_vec_table(conn)
            unindexed = self._get_unindexed_ids(conn, platform=platform)

            if not unindexed:
                return {"indexed": 0, "total": self.count()}

            batch_size = self.config.index_batch_size
            total_new = 0

            for i in range(0, len(unindexed), batch_size):
                batch_ids = unindexed[i : i + batch_size]
                # 拉取这批条目的文本
                placeholders = ",".join("?" * len(batch_ids))
                c = conn.execute(
                    f"SELECT id, title, description, solution FROM entries WHERE id IN ({placeholders})",
                    tuple(batch_ids),
                )
                rows = c.fetchall()

                # 组合文本
                texts = []
                ids = []
                for row_id, title, desc, sol in rows:
                    text = f"{title or ''}\n{desc or ''}\n{sol or ''}".strip()
                    if not text:
                        text = title or desc or sol or ""
                    texts.append(text)
                    ids.append(row_id)

                if not texts:
                    continue

                # 生成向量
                vectors = self.embedder.embed(texts)

                # 插入 vec_entries
                for row_id, vec in zip(ids, vectors):
                    vec_json = json.dumps(vec)
                    conn.execute(
                        "INSERT INTO vec_entries(entry_id, embedding) VALUES (?, ?)",
                        (row_id, vec_json),
                    )
                conn.commit()
                total_new += len(ids)

            total = self.count()
            return {"indexed": total_new, "total": total}

    # ------------------------------------------------------------------
    # 全量重建
    # ------------------------------------------------------------------

    def rebuild(self, platform: Optional[str] = None) -> Dict[str, int]:
        """删除旧向量，重新全量生成。"""
        with sqlite3.connect(self.db_path) as conn:
            self._load_extension(conn)
            # 删除旧虚拟表
            conn.execute("DROP TABLE IF EXISTS vec_entries")
            conn.commit()

        # 重新走增量逻辑（此时全部条目都是 "未索引"）
        return self.incremental_index(platform=platform)
