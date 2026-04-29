#!/usr/bin/env python3
"""
验证 Markdown 文件的双语结构。
条目文件采用字段级双语标记（如 "严重程度 / Severity"），
index 与根目录文档采用段落级双语。
"""
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
errors = []

# 字段级双语常见模式（至少出现一处才算通过）
_BILINGUAL_PATTERNS = [
    r'\*\*[^*]+/\s*Severity\*\*',
    r'\*\*[^*]+/\s*Description\*\*',
    r'\*\*[^*]+/\s*Solution\*\*',
    r'\*\*[^*]+/\s*Problem\*\*',
    r'\*\*[^*]+/\s*Patch\*\*',
    r'\*\*[^*]+/\s*Mitigation\*\*',
    r'\*\*[^*]+/\s*Affected\*\*',
    r'\*\*[^*]+/\s*Total\s*entries\*\*',
    r'\*\*[^*]+/\s*References\*\*',
    r'总计条目\s*/\s*Total entries',
    r'返回总索引\s*/\s*Back to Index',
]

def _has_bilingual_fields(content: str) -> bool:
    return any(re.search(p, content) for p in _BILINGUAL_PATTERNS)

def _has_bilingual_paragraphs(content: str) -> bool:
    """段落级双语：同时含中文字符与连续英文段落"""
    has_chinese = bool(re.search(r'[\u4e00-\u9fff]', content))
    has_english = bool(re.search(r'[a-zA-Z]{4,}', content))
    return has_chinese and has_english

def validate_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")

    # 根目录文档：README / CONTRIBUTING 等，段落级宽松检查
    if path.parent == PROJECT_ROOT:
        if _has_bilingual_paragraphs(content):
            return True
        errors.append(f"{path.relative_to(PROJECT_ROOT)}: 缺少中英双语段落")
        return False

    # index.md：段落级 + 字段级均可
    if path.name == "index.md":
        if _has_bilingual_paragraphs(content) or _has_bilingual_fields(content):
            return True
        errors.append(f"{path.relative_to(PROJECT_ROOT)}: 缺少中英双语内容")
        return False

    # 条目文件：字段级双语
    if _has_bilingual_fields(content):
        return True

    errors.append(f"{path.relative_to(PROJECT_ROOT)}: 未检测到字段级双语标记（如 '严重程度 / Severity'）")
    return False

def main():
    # 先过滤出需要检查的文件
    candidates = []
    skip_dirs = {".git", "agents", "scripts", "db", "__pycache__"}
    for f in PROJECT_ROOT.glob("**/*.md"):
        # 仅检查仓库内容目录与根目录文档
        try:
            rel = f.relative_to(PROJECT_ROOT)
        except ValueError:
            continue
        # 跳过子目录里的隐藏文件 / 第三方文件 / 内部目录
        if any(part.startswith('.') for part in rel.parts):
            continue
        if any(part in skip_dirs for part in rel.parts):
            continue
        candidates.append(f)

    total = len(candidates)
    valid = 0
    for f in candidates:
        if validate_file(f):
            valid += 1

    print(f"双语检查: {valid}/{total} 文件通过")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("✅ 所有 Markdown 文件双语结构正确")

if __name__ == "__main__":
    main()
