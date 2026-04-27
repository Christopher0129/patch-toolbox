# patch-toolbox 仓库架构总览

## 🗂️ 文件树（实际）

```
patch-toolbox/
│
├── 📄 README.md                      # 中英双语项目说明
├── 📄 LICENSE                        # MIT 许可证
├── 📄 requirements.txt               # Python 依赖清单
├── 📄 .gitignore                     # 排除 logs/state 不上传
│
├── 📁 agents/                        # Agent 运行时日志 & 报告（不上传GitHub）
│   ├── agent-network-security.log
│   ├── agent-network-security_report.json
│   ├── agent-system-vulnerabilities.log
│   ├── agent-system-vulnerabilities_report.json
│   ├── agent-system-troubleshooting.log
│   ├── agent-system-troubleshooting_report.json
│   ├── agent-publisher.log
│   ├── agent-link-auditor.log
│   ├── agent-link-auditor_report.json
│   ├── report_latest.md              # 最新一次汇总汇报（中英双语）
│   ├── summary.txt                   # 简短文字汇报
│   └── cron.log                      # cron 运行日志
│
├── 📁 network-security/              # 网络安全漏洞知识库
│   └── index.md                      # 总索引（中英双语，按来源分组）
│                                       # - CVE 漏洞库 (NVD)
│                                       # - 公开利用代码 / 0-Day (Exploit-DB)
│                                       # - GitHub 安全公告
│                                       # - CISA 已知被利用漏洞
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
│   ├── agent_network_security.py     # 🤖 Agent 1: 网络安全漏洞
│   │                                   #   数据源: NVD API, Exploit-DB RSS,
│   │                                   #           GitHub Security Advisories, CISA KEV
│   │
│   ├── agent_system_vulnerabilities.py  # 🤖 Agent 2: 系统漏洞
│   │                                      #   数据源: NVD API（按厂商关键词过滤）
│   │                                      #   分类: Windows / Linux / macOS
│   │
│   ├── agent_system_troubleshooting.py  # 🤖 Agent 3: 系统故障
│   │                                      #   数据源: Stack Exchange API
│   │                                      #   站点: Super User, Ask Ubuntu, Ask Different
│   │                                      #   分类: Windows / Linux / macOS
│   │
│   ├── agent_publisher.py            # 🤖 Agent 4: 汇总推送
│   │                                   #   - 读取三个agent报告
│   │                                   #   - 生成中英双语汇报
│   │                                   #   - GitHub 推送
│   │
│   ├── agent_link_auditor.py         # 🤖 Agent 5: 链接拓扑梳理（每12小时）
│   │                                   #   - 检查所有md的交叉链接
│   │                                   #   - 自动修复缺失导航
│   │
│   ├── run_all.py                    # 🔁 主调度器（串行运行3+1 agent）
│   ├── cron_wrapper.sh               # 🕐 Cron包装器（每小时）
│   └── cron_link_auditor.sh          # 🕐 Cron包装器（每12小时）
│
└── 📄 state.json                     # 去重数据库（本地，不上传GitHub）
```

---

## 🔗 链接拓扑（MD文件间导航）

```
README.md
    │
    ├──► network-security/index.md  ──► ../README.md (返回首页)
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
│  Agent 1        Agent 1           Agent 1         Agent 2 & 3          │
│  50条CVE        30条Exploit      20条Advisory    各50条/系统           │
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
│  network-security/index.md                                              │
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

## ⏰ 定时任务

| 频率 | 执行内容 | Cron |
|------|---------|------|
| 每小时整点 | 运行 `run_all.py` (3抓取agent + publisher) | `0 * * * *` |
| 每12小时 | 运行 `agent_link_auditor.py` (链接梳理) | `0 */12 * * *` |

---

## 📦 GitHub 仓库状态

- **仓库**: https://github.com/Christopher0129/patch-toolbox
- **协议**: MIT
- **公开/私有**: 公开
- **本地路径**: `/root/.openclaw/workspace/patch-toolbox`
