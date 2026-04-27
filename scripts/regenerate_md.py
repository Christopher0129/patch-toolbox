#!/usr/bin/env python3
"""
重新生成所有 MD 文件（从 SQLite 数据库）。
纯资源风格，无自动化痕迹，双语标签。
"""
import os, re, sqlite3, json
from pathlib import Path

REPO = Path("/root/.openclaw/workspace/patch-toolbox")
DB_DIR = REPO / "db"

def _is_empty(val):
    """判断字段是否为空/N/A/无意义值。"""
    if val is None:
        return True
    if isinstance(val, str):
        val = val.strip()
        return val == "" or val.upper() == "N/A"
    if isinstance(val, (list, dict)):
        return len(val) == 0
    return False


def generate_ns_md(conn, out_path: Path):
    c = conn.cursor()
    c.execute("SELECT title, description, solution, severity, cvss_score, source_url, refs FROM entries ORDER BY id")
    rows = c.fetchall()
    
    lines = [
        "# 网络安全漏洞知识库 | Network Security Vulnerability Knowledge Base",
        "",
        "> 本知识库汇总公开披露的网络安全漏洞信息，包含 CVE 编号、严重程度、漏洞描述及缓解方案。",
        "> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。",
        "> This knowledge base aggregates publicly disclosed network security vulnerabilities. Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.",
        "",
        f"**总计条目 / Total entries: {len(rows)}**",
        "",
        "---",
        "",
    ]
    
    for i, (title, desc, sol, sev, cvss, url, refs_json) in enumerate(rows, 1):
        sev_display = f"{sev or 'N/A'} | CVSS: {cvss}" if cvss else (sev or 'N/A')
        lines.append(f"#### {i}. {title}")
        lines.append("")
        lines.append(f"**严重程度 / Severity**: {sev_display}")
        lines.append("")
        lines.append("**漏洞描述 / Description**:")
        lines.append(desc or "N/A")
        lines.append("")
        if not _is_empty(sol):
            lines.append("**缓解方案 / Mitigation**:")
            lines.append(sol)
            lines.append("")
        ref_list = json.loads(refs_json) if refs_json else []
        has_refs = ref_list and not _is_empty(ref_list)
        if not _is_empty(url) or has_refs:
            lines.append("**参考链接 / References**:")
            if has_refs:
                for r in ref_list[:5]:
                    lines.append(f"- {r}")
            elif not _is_empty(url):
                lines.append(f"- {url}")
            lines.append("")
        lines.append("---")
        lines.append("")
    
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Written: {out_path} ({len(lines)} lines)")

def generate_sv_md(conn, out_dir: Path):
    c = conn.cursor()
    
    # Index
    lines = [
        "# 系统漏洞知识库总索引 | System Vulnerability Knowledge Base Index",
        "",
        "**🔗 导航 / Navigation**",
        "",
        "- [返回首页 / Back to Home](../README.md)",
        "- [Windows 漏洞 / Windows Vulns](windows.md)",
        "- [Linux 漏洞 / Linux Vulns](linux.md)",
        "- [macOS 漏洞 / macOS Vulns](macos.md)",
        "",
        "| 平台 / Platform | 条目数 / Entries | 链接 / Link |",
        "|---|---|---|",
    ]
    
    for platform in ["windows", "linux", "macos"]:
        c.execute("SELECT COUNT(*) FROM entries WHERE platform=?", (platform,))
        count = c.fetchone()[0]
        lines.append(f"| {platform.title()} | {count} | [{platform}.md]({platform}.md) |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  Written: {out_dir / 'index.md'}")
    
    # Platform files
    for platform in ["windows", "linux", "macos"]:
        c.execute("SELECT title, description, solution, severity, cvss_score, source_url, refs, affected_products FROM entries WHERE platform=? ORDER BY id", (platform,))
        rows = c.fetchall()
        
        plines = [
            f"# {platform.title()} 系统漏洞知识库 | {platform.title()} System Vulnerabilities",
            "",
            f"**🔙 [返回总索引](index.md) | [Back to Index](index.md)**",
            "",
            f"**总计条目 / Total entries: {len(rows)}**",
            "",
            "> 技术细节（漏洞描述、补丁信息等）保留原始语言以确保准确性，结构性文本提供中英双语。",
            "> Technical details (descriptions, patch info) remain in original language for accuracy; structural text is bilingual.",
            "",
            "---",
            "",
        ]
        
        for i, (title, desc, sol, sev, cvss, url, refs_json, prods_json) in enumerate(rows, 1):
            sev_display = f"{sev or 'N/A'} | CVSS: {cvss}" if cvss else (sev or 'N/A')
            plines.append(f"#### {i}. {title}")
            plines.append("")
            plines.append(f"**严重程度 / Severity**: {sev_display}")
            if prods_json:
                try:
                    prod_list = json.loads(prods_json)
                    if prod_list and not _is_empty(prod_list):
                        plines.append(f"**受影响产品 / Affected Products**: {', '.join(prod_list[:5])}")
                except:
                    pass
            plines.append("")
            plines.append("**漏洞描述 / Description**:")
            plines.append(desc or "N/A")
            plines.append("")
            if not _is_empty(sol):
                plines.append("**补丁信息 / Patch Info**:")
                plines.append(sol)
                plines.append("")
            ref_list = json.loads(refs_json) if refs_json else []
            has_refs = ref_list and not _is_empty(ref_list)
            if not _is_empty(url) or has_refs:
                plines.append("**参考链接 / References**:")
                if has_refs:
                    for r in ref_list[:5]:
                        plines.append(f"- {r}")
                elif not _is_empty(url):
                    plines.append(f"- {url}")
                plines.append("")
            plines.append("---")
            plines.append("")
        
        (out_dir / f"{platform}.md").write_text("\n".join(plines), encoding="utf-8")
        print(f"  Written: {out_dir / f'{platform}.md'} ({len(rows)} entries)")

def generate_st_md(conn, out_dir: Path):
    c = conn.cursor()
    
    # Index
    lines = [
        "# 系统故障知识库总索引 | System Troubleshooting Knowledge Base Index",
        "",
        "**🔗 导航 / Navigation**",
        "",
        "- [返回首页 / Back to Home](../README.md)",
        "- [Windows 故障 / Windows Issues](windows.md)",
        "- [Linux 故障 / Linux Issues](linux.md)",
        "- [macOS 故障 / macOS Issues](macos.md)",
        "",
        "| 平台 / Platform | 条目数 / Entries | 链接 / Link |",
        "|---|---|---|",
    ]
    
    for platform in ["windows", "linux", "macos"]:
        c.execute("SELECT COUNT(*) FROM entries WHERE platform=?", (platform,))
        count = c.fetchone()[0]
        lines.append(f"| {platform.title()} | {count} | [{platform}.md]({platform}.md) |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  Written: {out_dir / 'index.md'}")
    
    # Platform files
    for platform in ["windows", "linux", "macos"]:
        c.execute("SELECT title, description, solution, source_url FROM entries WHERE platform=? ORDER BY id", (platform,))
        rows = c.fetchall()
        
        plines = [
            f"# {platform.title()} 系统故障知识库 | {platform.title()} Troubleshooting",
            "",
            f"**🔙 [返回总索引](index.md) | [Back to Index](index.md)**",
            "",
            f"**总计条目 / Total entries: {len(rows)}**",
            "",
            "> 技术细节（问题描述、解决方案等）保留原始语言以确保准确性，结构性文本提供中英双语。",
            "> Technical details (descriptions, solutions) remain in original language for accuracy; structural text is bilingual.",
            "",
            "---",
            "",
        ]
        
        for i, (title, desc, sol, url) in enumerate(rows, 1):
            plines.append(f"#### {i}. {title}")
            plines.append("")
            plines.append("**问题描述 / Problem Description**:")
            plines.append(desc or "N/A")
            plines.append("")
            if not _is_empty(sol):
                plines.append("**解决方案 / Solution**:")
                plines.append(sol)
                plines.append("")
            if not _is_empty(url):
                plines.append("**参考链接 / References**:")
                plines.append(f"- {url}")
                plines.append("")
            plines.append("---")
            plines.append("")
        
        (out_dir / f"{platform}.md").write_text("\n".join(plines), encoding="utf-8")
        print(f"  Written: {out_dir / f'{platform}.md'} ({len(rows)} entries)")

def main():
    print("[1/3] Generating network-security/index.md ...")
    conn_ns = sqlite3.connect(DB_DIR / "network-security.db")
    generate_ns_md(conn_ns, REPO / "network-security" / "index.md")
    conn_ns.close()
    
    print("[2/3] Generating system-vulnerabilities/ ...")
    conn_sv = sqlite3.connect(DB_DIR / "system-vulnerabilities.db")
    generate_sv_md(conn_sv, REPO / "system-vulnerabilities")
    conn_sv.close()
    
    print("[3/3] Generating system-troubleshooting/ ...")
    conn_st = sqlite3.connect(DB_DIR / "system-troubleshooting.db")
    generate_st_md(conn_st, REPO / "system-troubleshooting")
    conn_st.close()
    
    print("\n✅ All MD files regenerated from SQLite.")

if __name__ == "__main__":
    main()
