"""
混合搜索 - FTS5 关键词 + sqlite-vec 语义 + RRF 融合排名
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import VectorConfig


class HybridSearcher:
    """
    提供三种搜索模式：
    1. keyword_search   — FTS5 / LIKE 关键词
    2. vector_search    — sqlite-vec 语义相似度
    3. hybrid_search    — RRF 融合关键词 + 向量
    """

    def __init__(self, db_path: Path, config: VectorConfig):
        self.db_path = Path(db_path)
        self.config = config

    # ------------------------------------------------------------------
    # 公共：加载扩展并确保辅助表存在
    # ------------------------------------------------------------------

    def _load_vec_extension(self, conn: sqlite3.Connection):
        try:
            import sqlite_vec
            sqlite_vec.load(conn)
        except Exception:
            try:
                conn.enable_load_extension(True)
                conn.execute("SELECT load_extension('vec')")
            except Exception as e:
                raise RuntimeError("sqlite-vec extension not available") from e

    def _ensure_fts(self, conn: sqlite3.Connection):
        """确保 entries_fts (FTS5) 虚拟表存在。"""
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
                title, description, solution,
                content='entries', content_rowid='id'
            )
        """)
        conn.commit()

    # ------------------------------------------------------------------
    # 1. 关键词搜索
    # ------------------------------------------------------------------

    def keyword_search(
        self,
        keywords: str,
        k: int = 10,
        platform: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        基于 FTS5 的关键词搜索。若 FTS5 未就绪则回退到 LIKE。
        返回带 rank 的条目列表。
        """
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_fts(conn)

            # 先尝试 FTS5
            try:
                # FTS5 自动 rank，越相关 rank 越小（负值绝对值越大越相关）
                sql = """
                    SELECT e.*, rank as fts_rank
                    FROM entries_fts
                    JOIN entries e ON entries_fts.rowid = e.id
                    WHERE entries_fts MATCH ?
                """
                params: List = [keywords]
                if platform:
                    sql += " AND e.platform = ?"
                    params.append(platform)
                sql += " ORDER BY rank LIMIT ?"
                params.append(k)

                c = conn.execute(sql, params)
                rows = c.fetchall()
                if rows:
                    return self._rows_to_dicts(c, rows)
            except Exception:
                pass  # 回退到 LIKE

            # LIKE 回退
            like_pat = f"%{keywords}%"
            sql = """
                SELECT * FROM entries
                WHERE (title LIKE ? OR description LIKE ? OR solution LIKE ?)
            """
            params = [like_pat, like_pat, like_pat]
            if platform:
                sql += " AND platform = ?"
                params.append(platform)
            sql += " LIMIT ?"
            params.append(k)

            c = conn.execute(sql, params)
            return self._rows_to_dicts(c, c.fetchall())

    # ------------------------------------------------------------------
    # 2. 向量搜索
    # ------------------------------------------------------------------

    def vector_search(
        self,
        query_vector: List[float],
        k: int = 10,
        platform: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        纯向量搜索。返回 k 条最近邻。
        """
        with sqlite3.connect(self.db_path) as conn:
            self._load_vec_extension(conn)

            vec_json = json.dumps(query_vector)
            # sqlite-vec KNN 查询语法
            sql = """
                SELECT e.*, v.distance
                FROM vec_entries v
                JOIN entries e ON v.entry_id = e.id
                WHERE v.embedding MATCH ? AND k = ?
            """
            params: List = [vec_json, k]

            if platform:
                sql += " AND e.platform = ?"
                params.append(platform)

            sql += " ORDER BY v.distance"

            c = conn.execute(sql, params)
            return self._rows_to_dicts(c, c.fetchall())

    # ------------------------------------------------------------------
    # 3. 混合搜索 (RRF)
    # ------------------------------------------------------------------

    def hybrid_search(
        self,
        query_text: str,
        query_vector: List[float],
        k: int = 10,
        platform: Optional[str] = None,
        keywords: Optional[str] = None,
        use_rrf: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        混合搜索：先分别走关键词和向量，再用 RRF (Reciprocal Rank Fusion) 融合排名。
        RRF 公式: score = Σ 1 / (k + rank)，其中 k 默认为 60。
        """
        kw = keywords or query_text
        k_fetch = max(k * 3, 50)  # 多取一些做融合

        # 分别搜索
        keyword_results = self.keyword_search(kw, k=k_fetch, platform=platform)
        vector_results = self.vector_search(query_vector, k=k_fetch, platform=platform)

        if not use_rrf:
            # 简单加权：按配置比例取两组结果的上半部分
            n_kw = int(k * self.config.hybrid_weight_keywords)
            n_vec = k - n_kw
            merged = keyword_results[:n_kw] + vector_results[:n_vec]
            # 去重（按 id）
            seen = set()
            out = []
            for r in merged:
                if r["id"] not in seen:
                    seen.add(r["id"])
                    out.append(r)
            return out[:k]

        # RRF 融合
        rrf_k = self.config.rrf_k
        scores: Dict[int, float] = {}
        info: Dict[int, Dict[str, Any]] = {}

        for rank, item in enumerate(keyword_results, start=1):
            rid = item["id"]
            scores[rid] = scores.get(rid, 0.0) + 1.0 / (rrf_k + rank)
            info[rid] = item

        for rank, item in enumerate(vector_results, start=1):
            rid = item["id"]
            scores[rid] = scores.get(rid, 0.0) + 1.0 / (rrf_k + rank)
            if rid not in info:
                info[rid] = item

        # 按 RRF 分数降序排列
        sorted_ids = sorted(scores.keys(), key=lambda rid: scores[rid], reverse=True)

        results = []
        for rid in sorted_ids[:k]:
            row = dict(info[rid])
            row["rrf_score"] = round(scores[rid], 6)
            results.append(row)

        return results

    # ------------------------------------------------------------------
    # 工具
    # ------------------------------------------------------------------

    @staticmethod
    def _rows_to_dicts(cursor, rows) -> List[Dict[str, Any]]:
        """将 sqlite3 结果转为字典列表。"""
        if not rows:
            return []
        cols = [desc[0] for desc in cursor.description]
        out = []
        for row in rows:
            out.append({k: row[i] for i, k in enumerate(cols)})
        return out
