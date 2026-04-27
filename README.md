# 安全漏洞与系统故障知识库 | Security Vulnerability & System Troubleshooting Knowledge Base

<p align="center">
  <a href="#中文介绍">中文</a> | <a href="#english-introduction">English</a>
</p>

---

## 中文介绍

这是一个**自动化维护**的安全知识库，每小时从各大平台抓取最新的网络安全漏洞、系统漏洞及常见故障信息，自动去重、增量更新，并以中英双语 Markdown 形式归档。

### 📁 目录结构

```
security-knowledge-base/
├── network-security/           # 网络安全漏洞与应对措施
│   ├── index.md                # 总索引（中英双语）
│   └── YYYY-MM-DD.md           # 按日期归档
├── system-vulnerabilities/     # 系统漏洞（按 OS 分类）
│   ├── windows.md
│   ├── linux.md
│   ├── macos.md
│   └── index.md
├── system-troubleshooting/     # 系统故障与解决方法（按 OS 分类）
│   ├── windows.md
│   ├── linux.md
│   ├── macos.md
│   └── index.md
├── scripts/                    # 抓取与生成脚本
└── agents/                     # Agent 定义与日志
```

### 🤖 自动化工作流

| Agent | 职责 | 频率 |
|-------|------|------|
| `agent-network-security` | 抓取网络安全漏洞及应对措施 | 每小时 |
| `agent-system-vulnerabilities` | 抓取系统漏洞（区分 Win/Linux/Mac） | 每小时 |
| `agent-system-troubleshooting` | 抓取系统故障及解决方法 | 每小时 |
| `agent-publisher` | 中英双语配置更新、GitHub 推送、汇报 | 每小时（三任务完成后） |

### 🔄 更新策略

- **增量更新**：新内容追加，已有内容保留历史方法
- **去重机制**：同一漏洞/故障保留最新信息，不同方法追加记录
- **每次更新**：每个分类不少于 50 条新内容
- **中英双语**：所有 Markdown 文件内置语言切换

### 📡 数据来源

- [NVD - National Vulnerability Database](https://nvd.nist.gov/)
- [CISA KEV - Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Microsoft Security Response Center](https://msrc.microsoft.com/)
- [Ubuntu Security Notices](https://ubuntu.com/security/notices)
- [Apple Security Updates](https://support.apple.com/en-us/HT201222)
- [Red Hat Security Advisories](https://access.redhat.com/security/)
- [Server Fault / Stack Exchange](https://serverfault.com/)
- [Ask Ubuntu](https://askubuntu.com/)
- [Apple Communities](https://discussions.apple.com/)

---

## English Introduction

An **auto-maintained** security knowledge base that scrapes the latest network security vulnerabilities, system vulnerabilities, and common troubleshooting info from major platforms every hour — deduplicated, incrementally updated, and archived in bilingual (CN/EN) Markdown.

### 📁 Directory Structure

```
security-knowledge-base/
├── network-security/           # Network security vulnerabilities & countermeasures
│   ├── index.md                # Master index (bilingual)
│   └── YYYY-MM-DD.md           # Date-based archives
├── system-vulnerabilities/     # System vulnerabilities by OS
│   ├── windows.md
│   ├── linux.md
│   ├── macos.md
│   └── index.md
├── system-troubleshooting/     # System troubleshooting by OS
│   ├── windows.md
│   ├── linux.md
│   ├── macos.md
│   └── index.md
├── scripts/                    # Scraping & generation scripts
└── agents/                     # Agent definitions & logs
```

### 🤖 Automation Workflow

| Agent | Duty | Frequency |
|-------|------|-----------|
| `agent-network-security` | Scrape network security vulnerabilities & fixes | Hourly |
| `agent-system-vulnerabilities` | Scrape OS vulnerabilities (Win/Linux/Mac) | Hourly |
| `agent-system-troubleshooting` | Scrape system issues & solutions | Hourly |
| `agent-publisher` | Bilingual config update, GitHub push, report | Hourly (after 3 tasks) |

### 🔄 Update Strategy

- **Incremental**: Append new content, keep historical entries
- **Deduplication**: Same vuln/issue keeps latest info; different methods are appended
- **Minimum batch**: ≥50 new entries per category per update
- **Bilingual**: All Markdown files have built-in language toggle

### 📡 Data Sources

- [NVD - National Vulnerability Database](https://nvd.nist.gov/)
- [CISA KEV - Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Microsoft Security Response Center](https://msrc.microsoft.com/)
- [Ubuntu Security Notices](https://ubuntu.com/security/notices)
- [Apple Security Updates](https://support.apple.com/en-us/HT201222)
- [Red Hat Security Advisories](https://access.redhat.com/security/)
- [Server Fault / Stack Exchange](https://serverfault.com/)
- [Ask Ubuntu](https://askubuntu.com/)
- [Apple Communities](https://discussions.apple.com/)

---

## ⚡ 快速开始 / Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Christopher0129/security-knowledge-base.git
cd security-knowledge-base

# 2. Install dependencies (Python 3.12+)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Run a single agent manually
python scripts/agent_network_security.py
python scripts/agent_system_vulnerabilities.py
python scripts/agent_system_troubleshooting.py

# 4. Run the publisher (pushes to GitHub)
python scripts/agent_publisher.py
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  由 OpenClaw Agent 自动维护 | Auto-maintained by OpenClaw Agent
</p>

---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](network-security/index.md)
- [返回目录 / Back to Index](system-vulnerabilities/index.md)
- [返回目录 / Back to Index](system-troubleshooting/index.md)
