# patch-toolbox 仓库架构总览

## 🗂️ 文件树（实际）

```
patch-toolbox/
│
├── 📄 README.md                      # 中英双语项目说明
├── 📄 LICENSE                        # MIT 许可证
├── 📄 CONTRIBUTING.md                # 贡献指南
├── 📄 .gitignore                     # 排除 logs/state 不上传
│
├── 📁 network-security/              # 网络安全漏洞（按 OS 分类）
│   ├── index.md                      # 总索引 + 导航到三个子文件
│   ├── windows.md                    # Windows 网络漏洞
│   ├── linux.md                      # Linux 网络漏洞
│   └── macos.md                      # macOS 网络漏洞
│
├── 📁 system-vulnerabilities/        # 系统漏洞（按 OS 分类）
│   ├── index.md                      # 总索引 + 导航到三个子文件
│   ├── windows.md                    # Windows 漏洞（50+条，中英双语）
│   ├── linux.md                      # Linux 漏洞（50+条，中英双语）
│   └── macos.md                      # macOS 漏洞（50+条，中英双语）
│
├── 📁 system-troubleshooting/        # 系统故障与解决（按 OS 分类）
│   ├── index.md                      # 总索引 + 导航到三个子文件
│   ├── windows.md                    # Windows 故障（50+条，中英双语）
│   ├── linux.md                      # Linux 故障（50+条，中英双语）
│   └── macos.md                      # macOS 故障（50+条，中英双语）
│
├── 📁 scripts/                       # [本地脚本，不上传GitHub] 全部 Python 自动化脚本
│   ├── utils.py                      # 🔧 通用工具库
│   │                                   #   - 去重状态管理 (state.json)
│   │                                   #   - 中英双语 Markdown 生成器
│   │                                   #   - GitHub 推送封装
│   │                                   #   - 日志 & 汇报
│   │
│   ├── sync_network_security.py     # 🔄 Sync 1: 网络安全漏洞同步脚本
│   │                                   #   数据源: NVD API, Exploit-DB RSS,
│   │                                   #           GitHub Security Advisories, CISA KEV
│   │
│   ├── sync_system_vulnerabilities.py  # 🔄 Sync 2: 系统漏洞同步脚本
│   │                                      #   数据源: NVD API（按厂商关键词过滤）
│   │                                      #   分类: Windows / Linux / macOS
│   │
│   ├── sync_system_troubleshooting.py  # 🔄 Sync 3: 系统故障同步脚本
│   │                                      #   数据源: Stack Exchange API
│   │                                      #   站点: Super User, Ask Ubuntu, Ask Different
│   │                                      #   分类: Windows / Linux / macOS
│   │
│   ├── sync_publisher.py            # 🔄 Sync 4: 汇总发布脚本
│   │                                   #   - 读取三个 sync 报告
│   │                                   #   - 生成中英双语汇报
│   │                                   #   - GitHub 推送
│   │
│   ├── sync_link_auditor.py         # 🔄 Sync 5: 链接拓扑梳理（每12小时）
│   │                                   #   - 检查所有md的交叉链接
│   │                                   #   - 自动修复缺失导航
│   │
│
├── 📁 agents/                        # Sync 运行时日志与报告目录
│   ├── sync-network-security.log
│   ├── sync-network-security_report.json
│   ├── sync-system-vulnerabilities.log
│   ├── sync-system-vulnerabilities_report.json
│   ├── sync-system-troubleshooting.log
│   ├── sync-system-troubleshooting_report.json
│   ├── sync-publisher.log
│   ├── sync-link-auditor.log
│   ├── sync-link-auditor_report.json
│   ├── report_latest.md              # 最新一次汇总汇报（中英双语）
│   ├── summary.txt                   # 简短文字汇报
│   └── cron.log                      # cron 运行日志
│
├── 📁 db/                            # SQLite 数据文件
│   ├── network-security.db
│   ├── system-vulnerabilities.db
│   └── system-troubleshooting.db
│
├── 📁 .github/
│   └── workflows/
│       └── ci-check.yml
│
└── 📄 state.json                     # 去重数据库（本地，不上传GitHub）
```

---

## 🔗 链接拓扑（MD文件间导航）

```
README.md
    │
    ├──► network-security/index.md  ──► ../README.md
    │       │
    │       ├──► windows.md  ──► index.md
    │       ├──► linux.md    ──► index.md
    │       └──► macos.md    ──► index.md
    │
    ├──► system-vulnerabilities/index.md  ──► ../README.md
    │       │
    │       ├──► windows.md  ──► index.md
    │       ├──► linux.md    ──► index.md
    │       └──► macos.md    ──► index.md
    │
    └──► system-troubleshooting/index.md  ──► ../README.md
            │
            ├──► windows.md  ──► index.md
            ├──► linux.md    ──► index.md
            └──► macos.md    ──► index.md
```

每个 `.md` 文件底部自带 **🔗 导航 / Navigation** 区块。

---

## 🔄 数据流向

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            外部数据源                                    │
├─────────────┬─────────────────┬─────────────────────┬───────────────────┤
│ NVD API     │ Exploit-DB RSS  │ GitHub Advisories   │ Stack Exchange    │
│ (CVE库)     │ (0-Day/Exploit) │ (安全公告)           │ (故障问答)        │
└──────┬──────┴────────┬────────┴──────────┬──────────┴─────────┬─────────┘
       │               │                   │                    │
       ▼               ▼                   ▼                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Sync 1         Sync 1            Sync 1          Sync 2 & 3            │
│  50条CVE        30条Exploit      20条Advisory    各50条/系统同步           │
└──────┬──────────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         去重过滤 (state.json)                            │
│  - SHA256哈希键 (CVE ID / URL + 标题)                                    │
│  - 同一漏洞保留最新，不同方法增量追加                                     │
└──────┬──────────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         生成中英双语 MD                                   │
│  network-security/{index,windows,linux,macos}.md                        │
│  system-vulnerabilities/{windows,linux,macos}.md                        │
│  system-troubleshooting/{windows,linux,macos}.md                        │
└──────┬──────────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Agent 4 (Publisher)                                                    │
│  - 读取报告 → 生成 report_latest.md → GitHub Push                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 分类体系

所有公开内容严格按照 **Windows / Linux / macOS** 三分栏组织：

| 分类 | Windows | Linux | macOS |
|------|---------|-------|-------|
| 网络安全漏洞 | network-security/windows.md | network-security/linux.md | network-security/macos.md |
| 系统漏洞 | system-vulnerabilities/windows.md | system-vulnerabilities/linux.md | system-vulnerabilities/macos.md |
| 系统故障排障 | system-troubleshooting/windows.md | system-troubleshooting/linux.md | system-troubleshooting/macos.md |

- **跨平台条目**：可明确归类到多个 OS 的条目，重复写入对应多个栏目。
- **无法归类条目**：不进入公开三分栏，转人工确认处理。

---

## 📦 GitHub 仓库状态

- **仓库**: https://github.com/Christopher0129/patch-toolbox
- **协议**: MIT
- **公开/私有**: 公开
- **本地路径**: `/root/.openclaw/workspace/patch-toolbox`
