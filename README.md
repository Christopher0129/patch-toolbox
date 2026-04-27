<p align="center">
  <a href="#中文介绍">中文</a> | <a href="#english-introduction">English</a>
</p>

---

## 中文介绍

这是一个**持续自动维护**的安全知识库，每小时从 NVD、Exploit-DB、GitHub Security Advisories、Stack Exchange 等平台聚合最新的网络安全漏洞（含 0-Day 公开利用）、系统漏洞及常见故障信息，去重后以中英双语 Markdown 形式归档。

> 本仓库**仅包含知识内容**，自动化脚本在本地运行，不随仓库发布。

### 📚 知识库目录

| 分类 | 入口 | 说明 |
|------|------|------|
| **网络安全漏洞** | [network-security/index.md](network-security/index.md) | CVE 漏洞库、0-Day 公开利用、GitHub 安全公告、CISA 紧急漏洞 |
| **系统漏洞** | [system-vulnerabilities/index.md](system-vulnerabilities/index.md) | Windows / Linux / macOS 系统级漏洞及补丁信息 |
| **系统故障排障** | [system-troubleshooting/index.md](system-troubleshooting/index.md) | Windows / Linux / macOS 常见故障及社区验证解决方案 |

### 🔄 更新策略

- **增量更新**：新内容追加，历史条目保留
- **去重机制**：同一漏洞保留最新信息，不同缓解方法追加记录
- **每次更新**：每个分类不少于 50 条新内容
- **中英双语**：所有页面内置语言切换

### 📡 数据来源

- [NVD - National Vulnerability Database](https://nvd.nist.gov/)
- [Exploit-DB](https://www.exploit-db.com/)
- [GitHub Security Advisories](https://github.com/advisories)
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Stack Exchange](https://serverfault.com/) / [Ask Ubuntu](https://askubuntu.com/) / [Ask Different](https://apple.stackexchange.com/)

---

## English Introduction

An **auto-maintained** security knowledge base that aggregates the latest network security vulnerabilities (including public 0-Day exploits), system vulnerabilities, and common troubleshooting info from NVD, Exploit-DB, GitHub Security Advisories, Stack Exchange, and other platforms every hour — deduplicated, incrementally updated, and archived in bilingual (CN/EN) Markdown.

> This repo **contains knowledge content only**. Automation scripts run locally and are not published with the repo.

### 📚 Knowledge Base Index

| Category | Entry | Description |
|----------|-------|-------------|
| **Network Security** | [network-security/index.md](network-security/index.md) | CVE database, 0-Day public exploits, GitHub security advisories, CISA emergency vulnerabilities |
| **System Vulnerabilities** | [system-vulnerabilities/index.md](system-vulnerabilities/index.md) | OS-level vulnerabilities and patch info for Windows / Linux / macOS |
| **System Troubleshooting** | [system-troubleshooting/index.md](system-troubleshooting/index.md) | Common system issues and community-verified solutions for Windows / Linux / macOS |

### 🔄 Update Strategy

- **Incremental**: New content appended, historical entries preserved
- **Deduplication**: Same vulnerability keeps latest info; different mitigations are appended
- **Minimum batch**: ≥50 new entries per category per update
- **Bilingual**: All pages have built-in language toggle

### 📡 Data Sources

- [NVD - National Vulnerability Database](https://nvd.nist.gov/)
- [Exploit-DB](https://www.exploit-db.com/)
- [GitHub Security Advisories](https://github.com/advisories)
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Stack Exchange](https://serverfault.com/) / [Ask Ubuntu](https://askubuntu.com/) / [Ask Different](https://apple.stackexchange.com/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  由 OpenClaw Agent 自动维护 | Auto-maintained by OpenClaw Agent
</p>
