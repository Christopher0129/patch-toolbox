#!/usr/bin/env python3
"""
向量搜索模块集成测试 - 不依赖网络/模型下载
使用固定随机向量作为假 embedder，验证 sqlite-vec + FTS5 + RRF 全链路。
"""
import sys
import tempfile
from pathlib import Path

# 插入 scripts/ 目录到路径
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import sqlite3


class FakeEmbedder:
    """假嵌入器：根据文本长度生成确定性伪向量。"""
    def __init__(self, dim=512):
        self.dim = dim

    def embed(self, texts):
        import random, hashlib
        results = []
        for t in texts:
            seed = int(hashlib.md5(t.encode()).hexdigest(), 16)
            rng = random.Random(seed)
            vec = [rng.uniform(-1, 1) for _ in range(self.dim)]
            # 归一化
            norm = sum(x*x for x in vec) ** 0.5
            vec = [x / norm for x in vec]
            results.append(vec)
        return results

    def is_available(self):
        return True


def test_full_pipeline():
    from vector_search.indexer import VectorIndexer
    from vector_search.search import HybridSearcher
    from vector_search.config import VectorConfig

    # 1. 创建临时数据库 + 插入测试数据
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    db_path = Path(tmp.name)
    tmp.close()

    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE entries (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            solution TEXT,
            platform TEXT,
            source_url TEXT
        )
    """)
    test_data = [
        (1, "电脑开机黑屏", "开机后显示器无信号", "检查显卡和内存", "windows", "http://a"),
        (2, "笔记本屏幕不亮", "按电源键后屏幕没反应", "外接显示器测试", "windows", "http://b"),
        (3, "Linux SSH连接失败", "ssh: connection refused", "检查22端口和防火墙", "linux", "http://c"),
        (4, "MacBook无法充电", "插上充电器没反应", "重置SMC", "macos", "http://d"),
        (5, "Windows蓝屏", "BSOD错误代码", "查看dump文件", "windows", "http://e"),
    ]
    conn.executemany(
        "INSERT INTO entries(id, title, description, solution, platform, source_url) VALUES (?,?,?,?,?,?)",
        test_data
    )
    conn.commit()
    conn.close()

    # 2. 配置
    config = VectorConfig.load({
        "enabled": True,
        "provider": "local",
        "local": {"dimension": 512},
        "index": {"index_batch_size": 10, "distance_metric": "cosine"},
        "search": {"rrf_k": 60},
    })

    embedder = FakeEmbedder(dim=512)

    # 3. 建索引
    indexer = VectorIndexer(db_path, config, embedder)
    result = indexer.incremental_index()
    print("[INDEX]", result)
    assert result["indexed"] == 5
    assert result["total"] == 5

    # 4. 搜索测试
    searcher = HybridSearcher(db_path, config)

    # 4a 关键词搜索
    kw_results = searcher.keyword_search("黑屏", k=10)
    print("[KEYWORD] found:", len(kw_results), "ids:", [r["id"] for r in kw_results])
    assert any(r["id"] == 1 for r in kw_results)

    # 4b 向量搜索
    query_vec = embedder.embed(["电脑黑屏"])[0]
    vec_results = searcher.vector_search(query_vec, k=10)
    print("[VECTOR] found:", len(vec_results), "ids:", [r["id"] for r in vec_results])
    assert len(vec_results) > 0

    # 4c 混合搜索 (RRF)
    hybrid = searcher.hybrid_search(
        query_text="电脑黑屏",
        query_vector=query_vec,
        k=3,
        use_rrf=True,
    )
    print("[HYBRID RRF] top-3 ids:", [r["id"] for r in hybrid])
    assert len(hybrid) <= 3
    assert hybrid[0].get("rrf_score") is not None

    # 4d 平台过滤
    win_results = searcher.hybrid_search(
        query_text="黑屏",
        query_vector=query_vec,
        k=10,
        platform="windows",
        use_rrf=True,
    )
    print("[HYBRID windows] ids:", [r["id"] for r in win_results])
    assert all(r["platform"] == "windows" for r in win_results)

    # 清理
    db_path.unlink(missing_ok=True)
    print("\n✅ ALL TESTS PASSED")


if __name__ == "__main__":
    test_full_pipeline()
