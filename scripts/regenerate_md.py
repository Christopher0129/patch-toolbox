#!/usr/bin/env python3
"""
重新生成所有 MD 文件（从 SQLite 数据库）。
纯资源风格，无自动化痕迹，双语标签。
"""
import os, re, sqlite3, json, html
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_ROOT / "db"

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




def clean_text(val):
    if val is None:
        return ""
    if not isinstance(val, str):
        return val
    return html.unescape(val).strip()





def summarize_title(title: str, limit: int = 100) -> str:
    title = clean_text(title)
    if not limit or len(title) <= limit:
        return title
    clipped = title[:limit].rsplit(' ', 1)[0].strip()
    if not clipped:
        clipped = title[:limit].strip()
    return clipped + '…'

def trim_dangling_bullets(val: str) -> str:
    val = clean_text(val)
    lines = val.splitlines()
    while lines:
        last = lines[-1].rstrip()
        if re.match(r'^\s*[-*]\s+[A-Za-z]?$' , last):
            lines.pop()
            continue
        break
    return '\n'.join(lines).strip()



def sanitize_advisory_block(val: str) -> str:
    val = trim_dangling_bullets(val)
    known_truncated_lines = {
        'OpenClaw now blocks `MINIMAX_API_HOST` from',
        '`DELETE /api/books/{bookID}` sets `books.deleted_at` to the current time. The book-level endpoint starts',
    }
    lines = []
    for line in val.splitlines():
        stripped = line.strip()
        if stripped in known_truncated_lines:
            continue
        lines.append(line)
    return '\n'.join(lines).strip()

def display_title(title: str, desc: str = "", limit: int = 100) -> str:
    title = clean_text(title)
    desc = clean_text(desc)
    display = title
    repaired = False
    if desc.startswith('[Red Hat] '):
        redhat_desc = desc[len('[Red Hat] '):].split('. Bugzilla:', 1)[0].strip()
        if title.startswith('CVE-') and ' - ' in title:
            cve, rest = title.split(' - ', 1)
            looks_truncated = title.endswith(' ') or title.endswith('…') or rest.endswith(' ') or len(rest) < len(redhat_desc)
            if looks_truncated:
                display = f"{cve} - {redhat_desc}"
                repaired = True
    if repaired and limit and len(display) > limit:
        return summarize_title(display, limit)
    return display

def generate_ns_md(conn, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    c = conn.cursor()
    c.execute("SELECT title, description, solution, severity, cvss_score, source_url, refs, platform FROM entries ORDER BY id")
    rows = c.fetchall()
    
    all_rows = rows

    # Bucket by platform
    buckets = {"windows": [], "linux": [], "macos": []}
    for row in all_rows:
        title, desc, sol, sev, cvss, url, refs_json, platform = row
        pf = (platform or "").strip().lower()
        if pf in buckets:
            buckets[pf].append((title, desc, sol, sev, cvss, url, refs_json))

    visible_total = len(all_rows)
    
    # --- index.md ---
    index_lines = [
        "# 网络安全漏洞知识库 | Network Security Vulnerability Knowledge Base",
        "",
        "> 本知识库汇总公开披露的网络安全漏洞信息，包含 CVE 编号、严重程度、漏洞描述及缓解方案。",
        "> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。",
        "> This knowledge base aggregates publicly disclosed network security vulnerabilities. Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.",
        "",
        f"**总计条目 / Total entries: {visible_total}**",
        "",
        "**🔗 导航 / Navigation**",
        "",
        "| 平台 / Platform | 条目数 / Entries | 链接 / Link |",
        "|---|---|---|",
    ]
    for platform in ["windows", "linux", "macos"]:
        count = len(buckets[platform])
        index_lines.append(f"| {platform.title()} | {count} | [{platform}.md]({platform}.md) |")
    index_lines.append("")
    index_lines.append("---")
    index_lines.append("")
    
    (out_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"  Written: {out_dir / 'index.md'} ({visible_total} total entries)")
    
    # --- Platform files ---
    for platform in ["windows", "linux", "macos"]:
        rows_platform = buckets[platform]
        plines = [
            f"# {platform.title()} 网络安全漏洞 | {platform.title()} Network Security",
            "",
            f"**🔙 [返回总索引](index.md) | [Back to Index](index.md)**",
            "",
            f"**总计条目 / Total entries: {len(rows_platform)}**",
            "",
            "> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。",
            "> Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.",
            "",
            "---",
            "",
        ]
        for i, (title, desc, sol, sev, cvss, url, refs_json) in enumerate(rows_platform, 1):
            sev_display = f"{sev or 'N/A'} | CVSS: {cvss}" if cvss else (sev or 'N/A')
            plines.append(f"#### {i}. {display_title(title, desc)}")
            plines.append("")
            plines.append(f"**严重程度 / Severity**: {sev_display}")
            plines.append("")
            plines.append("**漏洞描述 / Description**:")
            plines.append(sanitize_advisory_block(desc) or "N/A")
            plines.append("")
            if not _is_empty(sol):
                plines.append("**缓解方案 / Mitigation**:")
                plines.append(clean_text(sol))
                plines.append("")
            ref_list = json.loads(refs_json) if refs_json else []
            has_refs = ref_list and not _is_empty(ref_list)
            if not _is_empty(url) or has_refs:
                plines.append("**参考链接 / References**:")
                if has_refs:
                    for r in ref_list[:5]:
                        plines.append(f"- {clean_text(r)}")
                elif not _is_empty(url):
                    plines.append(f"- {clean_text(url)}")
                plines.append("")
            plines.append("---")
            plines.append("")
        (out_dir / f"{platform}.md").write_text("\n".join(plines), encoding="utf-8")
        print(f"  Written: {out_dir / f'{platform}.md'} ({len(rows_platform)} entries)")

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
            plines.append(f"#### {i}. {display_title(title, desc)}")
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
            plines.append(sanitize_advisory_block(desc) or "N/A")
            plines.append("")
            if not _is_empty(sol):
                plines.append("**补丁信息 / Patch Info**:")
                plines.append(clean_text(sol))
                plines.append("")
            ref_list = json.loads(refs_json) if refs_json else []
            has_refs = ref_list and not _is_empty(ref_list)
            if not _is_empty(url) or has_refs:
                plines.append("**参考链接 / References**:")
                if has_refs:
                    for r in ref_list[:5]:
                        plines.append(f"- {clean_text(r)}")
                elif not _is_empty(url):
                    plines.append(f"- {clean_text(url)}")
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
            plines.append(f"#### {i}. {display_title(title, desc)}")
            plines.append("")
            plines.append("**问题描述 / Problem Description**:")
            plines.append(sanitize_advisory_block(desc) or "N/A")
            plines.append("")
            if not _is_empty(sol):
                plines.append("**解决方案 / Solution**:")
                plines.append(clean_text(sol))
                plines.append("")
            if not _is_empty(url):
                plines.append("**参考链接 / References**:")
                plines.append(f"- {clean_text(url)}")
                plines.append("")
            plines.append("---")
            plines.append("")
        
        (out_dir / f"{platform}.md").write_text("\n".join(plines), encoding="utf-8")
        print(f"  Written: {out_dir / f'{platform}.md'} ({len(rows)} entries)")

def main():
    print("[1/3] Generating network-security/ ...")
    conn_ns = sqlite3.connect(DB_DIR / "network-security.db")
    generate_ns_md(conn_ns, PROJECT_ROOT / "network-security")
    conn_ns.close()
    
    print("[2/3] Generating system-vulnerabilities/ ...")
    conn_sv = sqlite3.connect(DB_DIR / "system-vulnerabilities.db")
    generate_sv_md(conn_sv, PROJECT_ROOT / "system-vulnerabilities")
    conn_sv.close()
    
    print("[3/3] Generating system-troubleshooting/ ...")
    conn_st = sqlite3.connect(DB_DIR / "system-troubleshooting.db")
    generate_st_md(conn_st, PROJECT_ROOT / "system-troubleshooting")
    conn_st.close()
    
    print("\n✅ All MD files regenerated from SQLite.")

if __name__ == "__main__":
    main()
