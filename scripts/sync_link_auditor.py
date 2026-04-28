#!/usr/bin/env python3
"""
Agent: Link Auditor (拓扑链接梳理)
每12小时检查所有md文件的内部链接拓扑，自动修复缺失的交叉链接。
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

from utils import log_sync, write_report, git_push

SYNC_NAME = "agent-link-auditor"
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 预期的链接拓扑: 文件 -> 应该包含的链接目标
EXPECTED_LINKS: Dict[str, List[str]] = {
    "README.md": [
        "network-security/index.md",
        "system-vulnerabilities/index.md",
        "system-troubleshooting/index.md",
    ],
    "network-security/index.md": [
        "../README.md",
    ],
    "system-vulnerabilities/index.md": [
        "../README.md",
        "windows.md",
        "linux.md",
        "macos.md",
    ],
    "system-vulnerabilities/windows.md": [
        "index.md",
    ],
    "system-vulnerabilities/linux.md": [
        "index.md",
    ],
    "system-vulnerabilities/macos.md": [
        "index.md",
    ],
    "system-troubleshooting/index.md": [
        "../README.md",
        "windows.md",
        "linux.md",
        "macos.md",
    ],
    "system-troubleshooting/windows.md": [
        "index.md",
    ],
    "system-troubleshooting/linux.md": [
        "index.md",
    ],
    "system-troubleshooting/macos.md": [
        "index.md",
    ],
}

NAV_BLOCK_ZH = """
---

**🔗 导航 / Navigation**

"""

NAV_BLOCK_EN = """
---

**🔗 Navigation**

"""


def extract_links(md_content: str) -> Set[str]:
    """提取md文件中的所有相对链接"""
    # 匹配 [text](path) 和 [text](../path)
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    links = set()
    for _, href in pattern.findall(md_content):
        # 只关心相对链接（非http）
        if not href.startswith("http") and not href.startswith("#"):
            links.add(href)
    return links


def find_nav_position(content: str) -> int:
    """找到文件末尾合适位置插入导航（在最后一个heading之后）"""
    # 在文件最后插入
    return len(content)


def build_nav_section(links: List[str], file_dir: Path) -> str:
    """为缺失的链接构建导航块"""
    lines = ["---", "", "**🔗 导航 / Navigation**", ""]
    for link in links:
        # 根据链接路径生成友好名称
        name = link.replace("../", "").replace(".md", "").replace("/", " / ")
        if name == "README":
            name_zh = "返回首页"
            name_en = "Back to Home"
        elif name.endswith("index"):
            name_zh = "返回目录"
            name_en = "Back to Index"
        elif "windows" in name.lower():
            name_zh = "Windows"
            name_en = "Windows"
        elif "linux" in name.lower():
            name_zh = "Linux"
            name_en = "Linux"
        elif "macos" in name.lower():
            name_zh = "macOS"
            name_en = "macOS"
        else:
            name_zh = name
            name_en = name
        lines.append(f"- [{name_zh} / {name_en}]({link})")
    lines.append("")
    return "\n".join(lines)


def check_and_fix() -> Tuple[int, int, List[str]]:
    """检查并修复链接，返回(检查文件数, 修复文件数, 修复详情)"""
    checked = 0
    fixed = 0
    details: List[str] = []

    for rel_path, expected in EXPECTED_LINKS.items():
        file_path = PROJECT_ROOT / rel_path
        if not file_path.exists():
            details.append(f"MISSING_FILE: {rel_path}")
            continue

        checked += 1
        content = file_path.read_text(encoding="utf-8")
        actual_links = extract_links(content)

        # 检查每个预期链接是否存在
        missing = []
        for expected_link in expected:
            # 检查多种可能的形式
            possible_forms = {expected_link}
            if expected_link.endswith(".md"):
                possible_forms.add(expected_link[:-3])  # 不带.md
            
            found = any(form in actual_links for form in possible_forms)
            if not found:
                missing.append(expected_link)

        if missing:
            nav = build_nav_section(missing, file_path.parent)
            # 检查是否已有导航块
            nav_start = -1
            lines = content.split("\n")
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped == "**🔗 导航 / Navigation**" or stripped == "**🔗 Navigation**":
                    nav_start = i
                    break

            if nav_start == -1:
                # 没有导航块，直接追加完整导航
                new_content = content.rstrip() + "\n\n" + nav
            else:
                # 已有导航块，只补充缺失的链接行
                # 找到导航块结束位置（下一个 --- 或文件末尾）
                nav_end = len(lines)
                for i in range(nav_start + 1, len(lines)):
                    if lines[i].strip() == "---":
                        nav_end = i
                        break
                # 提取当前导航块中的链接
                existing_links = set()
                for line in lines[nav_start:nav_end]:
                    m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
                    if m:
                        existing_links.add(m.group(2))
                # 过滤掉已有链接，只取缺失的
                nav_lines = nav.split("\n")
                new_link_lines = []
                for line in nav_lines:
                    m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
                    if m and m.group(2) not in existing_links:
                        new_link_lines.append(line)
                if new_link_lines:
                    # 在导航块结束前插入新链接
                    updated = lines[:nav_end]
                    if updated and updated[-1].strip():
                        updated.append("")
                    updated.extend(new_link_lines)
                    if nav_end < len(lines) and lines[nav_end].strip() == "---":
                        updated.append("")
                    updated.extend(lines[nav_end:])
                    new_content = "\n".join(updated)
                else:
                    # 无新增链接，不改动
                    new_content = content

            if new_content != content:
                file_path.write_text(new_content, encoding="utf-8")
            fixed += 1
            details.append(f"FIXED {rel_path}: added links to {missing}")
            log_sync(SYNC_NAME, f"Fixed {rel_path}: added {len(missing)} missing links")
        else:
            log_sync(SYNC_NAME, f"OK {rel_path}: all links present")

    return checked, fixed, details


def run():
    log_sync(SYNC_NAME, "=" * 40)
    log_sync(SYNC_NAME, "Starting link audit")

    checked, fixed, details = check_and_fix()

    # 直接写自定义报告（link-auditor 场景特殊，用自定义结构）
    report_file = PROJECT_ROOT / "agents" / f"{SYNC_NAME}_report.json"
    custom_report = {
        "sync": SYNC_NAME,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "files_checked": checked,
        "files_fixed": fixed,
        "fixes": details,
    }
    with open(report_file, "w", encoding="utf-8") as f:
        import json
        json.dump(custom_report, f, ensure_ascii=False, indent=2)

    log_sync(SYNC_NAME, f"Checked {checked} files, fixed {fixed} files")
    
    # 如果修复了文件，推送到远端仓库
    if fixed > 0:
        push_ok = git_push(f"link-audit: fixed {fixed} files with missing navigation links")
        if isinstance(push_ok, dict):
            github_ok = bool(push_ok.get("github", False))
            gitee_ok = bool(push_ok.get("gitee", False))
        else:
            github_ok = bool(push_ok)
            gitee_ok = False
        log_sync(SYNC_NAME, f"GitHub push: {'OK' if github_ok else 'FAIL'}; Gitee push: {'OK' if gitee_ok else 'FAIL'}")
    
    log_sync(SYNC_NAME, "Link audit complete")
    return custom_report


if __name__ == "__main__":
    run()
