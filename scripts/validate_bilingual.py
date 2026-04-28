#!/usr/bin/env python3
"""
验证 Markdown 文件的双语结构。
检查每个条目文件是否包含 "### 中文版 / Chinese Version" 和 "### 英文版 / English Version" 标记。
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
errors = []

def validate_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    has_zh = "### 中文版" in content or "### Chinese Version" in content
    has_en = "### 英文版" in content or "### English Version" in content
    if not has_zh and not has_en:
        return True  # 非条目文件（如 index.md）跳过
    if has_zh and has_en:
        return True
    missing = []
    if not has_zh:
        missing.append("中文版")
    if not has_en:
        missing.append("英文版")
    errors.append(f"{path.relative_to(PROJECT_ROOT)}: 缺少 {', '.join(missing)} 标记")
    return False

def main():
    md_files = list(PROJECT_ROOT.glob("**/*.md"))
    total = len(md_files)
    valid = 0
    for f in md_files:
        # 跳过根目录的 README, CONTRIBUTING 等
        if f.parent == PROJECT_ROOT:
            continue
        if validate_file(f):
            valid += 1

    print(f"双语检查: {valid}/{total} 文件通过")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("✅ 所有 Markdown 文件双语结构正确")

if __name__ == "__main__":
    main()
