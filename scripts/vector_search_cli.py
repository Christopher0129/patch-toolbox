#!/usr/bin/env python3
"""
向量搜索命令行工具

用法：
    python3 scripts/vector_search_cli.py index [--db path] [--platform windows]
    python3 scripts/vector_search_cli.py search "电脑黑屏没反应" [--db path] [--k 10]
    python3 scripts/vector_search_cli.py status [--db path]
    python3 scripts/vector_search_cli.py rebuild [--db path]

依赖：config.json 中 vector_search.enabled = true
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vector_search import VectorSearch


def get_db_path(args) -> Path:
    if args.db:
        return Path(args.db)
    # 默认 system-troubleshooting 数据库（自然语言查询价值最高）
    project_root = Path(__file__).resolve().parent.parent
    return project_root / "db" / "system-troubleshooting.db"


def cmd_index(args):
    db = get_db_path(args)
    vs = VectorSearch(db)
    result = vs.ensure_indexed(platform=args.platform)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_search(args):
    db = get_db_path(args)
    vs = VectorSearch(db)
    vs.ensure_indexed(platform=args.platform)
    results = vs.search(
        query=args.query,
        k=args.k,
        platform=args.platform,
        use_rrf=not args.no_rrf,
    )
    print(f"\n🔍 查询: {args.query} | 返回 {len(results)} 条\n")
    for i, r in enumerate(results, 1):
        score = r.get("rrf_score", "")
        score_str = f" (RRF={score})" if score else ""
        print(f"--- [{i}]{score_str} ---")
        print(f"ID:     {r['id']}")
        print(f"Title:  {r.get('title', 'N/A')}")
        print(f"Source: {r.get('source_url', 'N/A')}")
        print(f"Desc:   {r.get('description', 'N/A')[:200]}...")
        print()


def cmd_status(args):
    db = get_db_path(args)
    vs = VectorSearch(db)
    health = vs.health()
    print(json.dumps(health, indent=2, ensure_ascii=False))


def cmd_rebuild(args):
    db = get_db_path(args)
    vs = VectorSearch(db)
    result = vs.rebuild_index(platform=args.platform)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Vector search CLI for patch-toolbox")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # index
    p_index = sub.add_parser("index", help="增量建立向量索引")
    p_index.add_argument("--db", help="SQLite 数据库路径")
    p_index.add_argument("--platform", help="限定平台 (windows/linux/macos)")
    p_index.set_defaults(func=cmd_index)

    # search
    p_search = sub.add_parser("search", help="混合语义搜索")
    p_search.add_argument("query", help="自然语言查询")
    p_search.add_argument("--db", help="SQLite 数据库路径")
    p_search.add_argument("--k", type=int, default=10, help="返回结果数")
    p_search.add_argument("--platform", help="限定平台")
    p_search.add_argument("--no-rrf", action="store_true", help="禁用 RRF，仅走向量+关键词拼接")
    p_search.set_defaults(func=cmd_search)

    # status
    p_status = sub.add_parser("status", help="查看模块健康状态")
    p_status.add_argument("--db", help="SQLite 数据库路径")
    p_status.set_defaults(func=cmd_status)

    # rebuild
    p_rebuild = sub.add_parser("rebuild", help="全量重建索引")
    p_rebuild.add_argument("--db", help="SQLite 数据库路径")
    p_rebuild.add_argument("--platform", help="限定平台")
    p_rebuild.set_defaults(func=cmd_rebuild)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
