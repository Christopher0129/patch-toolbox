"""
向量搜索模块 - 配置驱动、条件启用
为 system-troubleshooting 等自然语言查询场景提供语义检索能力。

使用方法：
    from scripts.vector_search import VectorSearch
    vs = VectorSearch(db_path)
    vs.ensure_indexed()          # 增量生成向量索引
    results = vs.search("电脑黑屏没反应", k=10)  # 混合检索

配置：顶层 config.json 的 vector_search 字段。未配置或 enabled=false 时模块不工作。
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import VectorConfig
from .embedder import get_embedder
from .indexer import VectorIndexer
from .search import HybridSearcher

__all__ = ["VectorSearch", "VectorConfig"]


class VectorSearch:
    """
    向量搜索门面类。管理索引建立和混合查询。
    """

    def __init__(self, db_path: Path, config_override: Optional[Dict[str, Any]] = None):
        self.db_path = Path(db_path)
        self.config = VectorConfig.load(config_override)
        if not self.config.enabled:
            raise RuntimeError(
                "Vector search is disabled. Set 'vector_search.enabled' to true in config.json."
            )

        self.embedder = get_embedder(self.config)
        self.indexer = VectorIndexer(self.db_path, self.config, self.embedder)
        self.searcher = HybridSearcher(self.db_path, self.config)

    # ------------------------------------------------------------------
    # 索引管理
    # ------------------------------------------------------------------

    def ensure_indexed(self, platform: Optional[str] = None) -> Dict[str, int]:
        """
        检查并增量建立向量索引。只给尚未索引的条目生成嵌入。
        platform: 只索引指定平台的条目（如 'windows'），None 表示全部。
        返回: {'indexed': 新索引数, 'total': 索引表总条目数}
        """
        return self.indexer.incremental_index(platform=platform)

    def rebuild_index(self, platform: Optional[str] = None) -> Dict[str, int]:
        """全量重建索引。慎用（会删除旧向量）。"""
        return self.indexer.rebuild(platform=platform)

    def index_count(self) -> int:
        """当前索引表中的向量数量。"""
        return self.indexer.count()

    # ------------------------------------------------------------------
    # 查询
    # ------------------------------------------------------------------

    def search(
        self,
        query: str,
        k: int = 10,
        platform: Optional[str] = None,
        keywords: Optional[str] = None,
        use_rrf: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        混合搜索。默认同时走 FTS5 关键词 + 向量语义，RRF 融合排名。

        query:      自然语言查询（会被嵌入成向量）
        k:          返回结果数
        platform:   限定平台过滤（如 'windows'）
        keywords:   额外关键词（若为空则自动从 query 提取）
        use_rrf:    是否启用 RRF 融合（False 则只走向量）

        返回: 列表，每项包含 entry 的全部字段 + score / rank
        """
        # 1. 生成查询向量
        query_vec = self.embedder.embed([query])[0]

        # 2. 执行混合搜索
        return self.searcher.hybrid_search(
            query_text=query,
            query_vector=query_vec,
            k=k,
            platform=platform,
            keywords=keywords,
            use_rrf=use_rrf,
        )

    def vector_search_only(
        self,
        query: str,
        k: int = 10,
        platform: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """纯向量搜索（不融合 FTS5）。"""
        query_vec = self.embedder.embed([query])[0]
        return self.searcher.vector_search(
            query_vector=query_vec,
            k=k,
            platform=platform,
        )

    def keyword_search_only(
        self,
        keywords: str,
        k: int = 10,
        platform: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """纯关键词搜索（FTS5）。"""
        return self.searcher.keyword_search(
            keywords=keywords,
            k=k,
            platform=platform,
        )

    # ------------------------------------------------------------------
    # 诊断
    # ------------------------------------------------------------------

    def health(self) -> Dict[str, Any]:
        """返回模块健康状态（用于调试/汇报）。"""
        return {
            "enabled": self.config.enabled,
            "provider": self.config.provider,
            "model": self.config.model_name,
            "dimension": self.config.dimension,
            "db_path": str(self.db_path),
            "index_count": self.index_count(),
            "embedder_ok": self.embedder.is_available(),
        }
