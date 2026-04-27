# patch-toolbox 网站推荐清单

> **项目地址**：https://github.com/Christopher0129/patch-toolbox/  
> **生成日期**：2026-04-27  
> **说明**：本清单为 patch-toolbox 项目的三大板块（网络漏洞/系统漏洞/系统故障排除）推荐适合爬取资料的高质量网站资源，覆盖 Windows/Linux/macOS 三种操作系统。本报告基于12个研究维度文件的交叉验证、去重和质量筛选整合而成。

---

## 目录

- [一、网络漏洞](#一网络漏洞)（63个网站）
  - [1.1 Windows](#11-windows)（9个）
  - [1.2 Linux](#12-linux)（16个）
  - [1.3 macOS](#13-macos)（11个）
  - [1.4 跨平台/通用](#14-跨平台通用)（27个）
- [二、系统漏洞](#二系统漏洞)（54个网站）
  - [2.1 Windows](#21-windows)（10个）
  - [2.2 Linux](#22-linux)（12个）
  - [2.3 macOS](#23-macos)（10个）
  - [2.4 跨平台/通用](#24-跨平台通用)（22个）
- [三、系统故障排除](#三系统故障排除)（69个网站）
  - [3.1 Windows](#31-windows)（15个）
  - [3.2 Linux](#32-linux)（21个）
  - [3.3 macOS](#33-macos)（21个）
  - [3.4 跨平台/通用](#34-跨平台通用)（12个）
- [四、跨平台通用资源汇总](#四跨平台通用资源汇总)
- [五、爬虫技术建议](#五爬虫技术建议)
- [六、统计汇总](#六统计汇总)

---

## 爬虫友好度标注标准

| 等级 | 说明 |
|------|------|
| **高** | 提供公开API、RSS/Atom Feed、结构化数据（JSON/XML），或robots.txt允许爬取 |
| **中** | 提供HTML结构化页面，无严格反爬，可通过常规爬虫获取 |
| **低** | 有Cloudflare等严格防护，或需要JavaScript渲染，爬取难度较大 |

---

## 一、网络漏洞（63个网站）

> 网络漏洞板块涵盖CVE数据库、安全公告、漏洞利用代码、威胁情报等，帮助用户了解和管理网络层面安全威胁。

### 1.1 Windows（9个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 1 | Microsoft Security Response Center (MSRC) | https://msrc.microsoft.com/update-guide | 漏洞公告/安全更新/知识库 | 每月（Patch Tuesday）+ 紧急更新 | 高 | Windows漏洞的官方权威来源。MSRC负责调查所有影响Microsoft产品和服务的安全漏洞报告，提供CVRF格式的安全公告、漏洞详细信息和补丁链接。 |
| 2 | Microsoft Learn 安全文档中心 | https://learn.microsoft.com/en-us/security/ | 技术文档/安全配置指南/漏洞修复说明 | 每周 | 中 | Microsoft官方安全学习和文档中心，提供Windows安全基线配置、漏洞缓解指南、安全更新部署文档。 |
| 3 | Action1 Vulnerability Database | https://www.action1.com/vulnerabilities/ | 漏洞公告/补丁管理/技术摘要 | 每日 | 中 | Action1专注于Windows补丁管理，其漏洞数据库专门针对Windows生态系统。提供技术摘要和业务影响分析。 |
| 4 | BleepingComputer | https://www.bleepingcomputer.com | 安全新闻/漏洞报道/技术分析/教程 | 每日（多篇更新） | 高 | 全球领先的网络安全新闻网站，以快速准确的Windows漏洞报道著称。在Patch Tuesday后迅速发布Windows漏洞分析文章。 |
| 5 | Exploit Database (Exploit-DB) | https://www.exploit-db.com | Exploit代码/PoC/漏洞利用程序 | 每日 | 高 | 全球最大的公开Exploit和PoC存档，目前收录超过46,500个条目。Windows网络漏洞的利用代码均在此发布。 |
| 6 | SecurityFocus / Bugtraq | https://www.securityfocus.com | 漏洞公告/邮件列表/安全讨论 | 每日 | 中 | SecurityFocus是网络安全领域历史最悠久的漏洞公告平台之一。许多经典Windows网络漏洞均在此有详细记录。 |
| 7 | CVE Details | https://www.cvedetails.com | CVE详细信息/受影响产品/漏洞统计 | 每日（与NVD同步） | 高 | CVE Details以直观的方式呈现漏洞数据，特别擅长按厂商和产品筛选漏洞。提供EPSS分数和利用概率预测。 |
| 8 | Fortinet PSIRT | https://www.fortiguard.com/psirt | 产品安全公告/漏洞披露/月度报告 | 每月+紧急 | 高 | Fortinet的产品安全事件响应团队，每月定期发布安全公告。 |
| 9 | SentinelOne Vulnerability Database | https://www.sentinelone.com/vulnerability-database/ | 漏洞数据库/技术分析/威胁评估 | 每日 | 中 | SentinelOne维护的策展式漏洞数据库，对Windows网络漏洞有出色的技术覆盖。 |

### 1.2 Linux（16个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 10 | Red Hat Security Advisories (RHSA) | https://access.redhat.com/security/advisories | 安全公告/CVE详情/补丁包/CVSS评分 | 每日 | 高 | 企业级Linux最重要的安全公告来源。RHEL的安全更新直接影响CentOS Stream、Fedora、AlmaLinux、Rocky Linux等衍生发行版。 |
| 11 | Debian Security Tracker | https://security-tracker.debian.org | 安全追踪器/CVE状态/DSA/DLA公告 | 实时 | 高 | Debian安全团队的官方追踪器，提供Linux平台最精细的漏洞修复状态追踪。每个CVE显示受影响的Debian版本、修复状态、DSA/DLA公告链接。 |
| 12 | Ubuntu Security Notices (USN) | https://ubuntu.com/security/notices | 安全公告/CVE详情/补丁更新 | 每日 | 高 | Canonical官方安全公告，覆盖Ubuntu所有受支持版本。提供精确的包级修复信息。 |
| 13 | SUSE Security Center | https://www.suse.com/security/cve/ | CVE数据库/安全公告/CVSS评分 | 每日 | 中 | SUSE是企业级Linux的重要发行版，其安全中心提供详细的CVE信息、受影响产品和修复状态。 |
| 14 | Arch Linux Security Tracker | https://security.archlinux.org | 安全追踪器/CVE状态/ASA公告 | 每日 | 高 | Arch Linux安全团队的官方漏洞追踪平台。发布ASA（Arch Linux Security Advisory），追踪core/extra/multilib仓库中所有包的CVE状态。 |
| 15 | Gentoo Security Advisories (GLSA) | https://security.gentoo.org/glsa | 安全公告/漏洞通知/修复指引 | 每周 | 高 | Gentoo通过Portage源码包管理系统维护安全公告。GLSA覆盖的软件包范围广泛，包括大量网络服务组件。 |
| 16 | Linux Kernel Archives (kernel.org) | https://www.kernel.org | 内核发布/安全补丁/长期支持版本信息 | 实时 | 高 | Linux内核官方发布站点。网络子系统漏洞（如netfilter、TCP/IP栈、网络驱动）的修复首先发布于此。 |
| 17 | Linux Kernel CVE Tracker | https://linuxkernelcves.com | 内核CVE专用数据库/按版本查询漏洞 | 每日 | 高 | 专门追踪Linux内核CVE的第三方数据库，由社区维护。支持按内核版本号精确查询受影响的CVE。 |
| 18 | OpenSSH Official Security | https://www.openssh.com/security.html | 安全公告/漏洞披露/补丁发布 | 按需 | 高 | OpenSSH是Linux服务器最基础的网络安全组件，其安全公告是追踪SSH相关漏洞的权威来源。 |
| 19 | OpenSSL Security Vulnerabilities | https://openssl-library.org/news/vulnerabilities/ | 安全公告/CVE披露/版本修复信息 | 按需 | 高 | OpenSSL是Linux网络安全的基石库，几乎所有网络服务都依赖它。提供按版本分类的漏洞列表。 |
| 20 | Amazon Linux Security Center (ALAS) | https://alas.aws.amazon.com | 安全公告/CVE详情/补丁包 | 每日 | 中 | AWS云平台上使用最广泛的Linux发行版。ALAS公告覆盖内核网络漏洞、OpenSSL/OpenSSH安全更新、容器网络组件漏洞等。 |
| 21 | Oracle Linux Security Errata | https://linux.oracle.com/errata/ | 安全公告(ELSA)/CVE详情/Unbreakable Enterprise Kernel | 每日 | 中 | Oracle Linux基于RHEL但使用自己的Unbreakable Enterprise Kernel (UEK)，拥有独立的内核安全修复路径。 |
| 22 | AlmaLinux Product Errata | https://errata.almalinux.org | 安全公告(ALSA)/CVE详情/补丁状态 | 每日 | 高 | AlmaLinux作为CentOS的继任者，其errata系统精确映射RHSA到ALSA编号。是CentOS迁移用户追踪安全更新的重要来源。 |
| 23 | Openwall OSS-Security Mailing List | https://www.openwall.com/lists/oss-security/ | 安全公告/漏洞讨论/补丁审查 | 实时 | 高 | Linux开源社区最重要的安全讨论平台。Linux内核网络漏洞的首次公开披露常发生于此。 |
| 24 | Linux netdev Mailing List | https://lore.kernel.org/netdev/ | 内核网络子系统开发/补丁审查/漏洞讨论 | 实时 | 高 | Linux内核网络子系统（包括TCP/IP栈、网络驱动、netfilter等）的核心开发邮件列表。网络协议栈漏洞的技术讨论和修复补丁首先在此出现。 |
| 25 | CNVD (中国国家信息安全漏洞库) | https://www.cnvd.org.cn | 漏洞公告/安全预警/漏洞统计 | 每日 | 低 | 由中国信息安全测评中心维护的国家级漏洞库。收录大量Linux平台网络漏洞的中文版信息。 |

### 1.3 macOS（11个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 26 | Apple Security Releases | https://support.apple.com/en-us/100100 | 官方安全公告/漏洞修复说明/CVE详情 | 每周-每月 | 高 | Apple产品安全的官方权威来源，所有macOS安全更新的第一手信息。每篇公告均包含CVE编号、影响评估、受影响系统和修复版本。 |
| 27 | OpenCVE (Apple Vendor Page) | https://app.opencve.io/cve/?vendor=apple | CVE聚合/漏洞详情/产品关联 | 实时 | 高 | 优秀的开源CVE管理平台，针对Apple产品提供13,700+条CVE聚合。支持按产品（macOS、Bonjour、mDNSResponder等）筛选。 |
| 28 | Objective-See Blog | https://objective-see.org/blog.html | 安全研究博客/漏洞分析/工具发布/恶意软件分析 | 每周-每月 | 中 | macOS安全领域最具影响力的社区资源，由前NSA研究员Patrick Wardle创立。提供macOS漏洞深度分析、PoC利用代码、免费开源安全工具。 |
| 29 | Intego Mac Security Blog | https://www.intego.com/mac-security-blog/ | 安全新闻/漏洞警告/恶意软件分析/安全建议 | 每日-每周 | 中 | 25年专注Mac安全的老牌厂商博客，提供Apple安全更新的及时解读、零日漏洞警告和恶意软件深度分析。 |
| 30 | The Eclectic Light Company | https://eclecticlight.co | 技术分析/macOS子系统深度解析/安全更新分析 | 每周 | 中 | 由Dr. Howard Oakley运营的权威macOS技术分析博客，提供macOS子系统（包括网络栈、统一日志、XProtect反恶意软件等）的深度技术解析。 |
| 31 | Apple Product Security Research | https://security.apple.com/research | 安全研究指南/Bug Bounty计划/安全研究设备 | 每季度 | 中 | Apple官方安全研究门户，提供macOS安全研究的政策指南、漏洞提交渠道、Security Bounty奖励计划详情。 |
| 32 | SEEMOO Lab - TU Darmstadt | https://www.seemoo.tu-darmstadt.de | 学术研究/无线协议安全/AWDL/AirDrop漏洞研究 | 每季度 | 中 | 德国达姆施塔特工业大学的移动网络安全实验室，是Apple无线协议安全研究的顶尖机构。发表了关于AWDL、AirDrop、Handoff的里程碑式研究。 |
| 33 | CIS Benchmarks for macOS | https://www.cisecurity.org/cis-benchmarks | 安全配置基准/加固指南/审计检查清单 | 每年 | 中 | Center for Internet Security发布的macOS安全配置基准是业界标准的安全加固参考。涵盖macOS防火墙、网络服务、远程管理等网络相关配置。 |
| 34 | Red Canary Mac Monitor (GitHub) | https://github.com/Brandon7CC/mac-monitor | 开源安全工具/Endpoint Security/系统监控 | 每月 | 高 | Red Canary开发的macOS独立系统监控工具，基于Apple Endpoint Security框架。用于macOS安全研究、恶意软件分类和系统故障排查。 |
| 35 | JVN (Japan Vulnerability Notes) | https://jvn.jp | 漏洞信息/安全公告/风险评估 | 每日 | 高 | 日本IPA运营的漏洞数据库，与NVD互补。对macOS相关漏洞有独立的评估和报道，特别关注日本发现的Apple安全问题。 |
| 36 | Dark Reading | https://www.darkreading.com | 安全新闻/漏洞分析/行业报告 | 每日 | 中 | 由Informa Tech运营的企业级网络安全新闻平台，聚焦企业安全决策者和IT管理者。 |

### 1.4 跨平台/通用（27个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 37 | National Vulnerability Database (NVD) | https://nvd.nist.gov | 漏洞数据库/CVSS评分/结构化数据 | 每日 | 高 | 美国政府维护的漏洞管理数据标准仓库。所有Windows CVE在此获得官方CVSS评分、CWE分类、受影响产品CPE配置。 |
| 38 | CISA Known Exploited Vulnerabilities (KEV) Catalog | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | 已知被利用漏洞清单/威胁情报 | 每周 | 高 | CISA维护的"在野利用"漏洞权威清单。联邦机构必须按BOD 22-01指令在截止日期前修复。 |
| 39 | CVE.org (MITRE) | https://cve.org | CVE编号分配/漏洞标识/结构化数据 | 每日 | 高 | MITRE公司运营的CVE项目官方网站，是所有公开披露安全漏洞的标准标识系统。目前收录超过329,000条CVE记录。 |
| 40 | The Hacker News | https://thehackernews.com | 安全新闻/漏洞分析/威胁情报 | 每日（多篇更新） | 高 | 拥有540万+粉丝的顶级网络安全新闻平台。持续报道Windows平台的重要网络漏洞。 |
| 41 | SecurityWeek | https://www.securityweek.com | 安全新闻/漏洞公告/会议报道 | 每日 | 中 | 网络安全行业知名媒体，专注于企业安全和威胁情报。SecurityWeek的漏洞新闻板块频繁报道Windows网络组件漏洞。 |
| 42 | Rapid7 Vulnerability & Exploit Database | https://www.rapid7.com/db/ | 漏洞数据库/Exploit模块/Metasploit集成 | 每日 | 高 | Rapid7的漏洞和渗透测试数据库，所有Exploit均包含在Metasploit框架中。 |
| 43 | Packet Storm Security | https://packetstormsecurity.com | Exploit/PoC/安全公告/工具 | 每日 | 高 | 运行多年的独立安全文件存档平台，收录大量Windows网络漏洞的PoC和Exploit。 |
| 44 | Trend Micro Zero Day Initiative (ZDI) | https://www.zerodayinitiative.com/advisories/ | 零日漏洞公告/协调披露/技术分析 | 每周 | 高 | 全球最大的独立于厂商的漏洞赏金项目。ZDI协调披露大量Windows零日漏洞。 |
| 45 | GitHub Advisory Database | https://github.com/advisories | 安全公告/CVE关联/依赖漏洞 | 每日 | 高 | GitHub维护的综合性安全公告数据库，聚合了CVE、NVD和各大厂商的安全公告。 |
| 46 | 国家信息安全漏洞库 / CNNVD | https://www.cnnvd.org.cn | 漏洞公告/安全通报/预警信息 | 每日 | 中 | 中国官方的漏洞库和网络安全应急机构，发布中文Windows漏洞安全通报和预警。 |
| 47 | FreeBuf (网络安全行业门户) | https://www.freebuf.com | 安全文章/漏洞分析/技术博客/安全工具 | 每日 | 中 | 中国领先的网络安全行业门户，拥有大量Windows漏洞的中文分析文章。社区活跃，安全从业者参与度高。 |
| 48 | 安全客 (AQ.360.cn) | https://aq.360.cn | 漏洞公告/安全资讯/威胁情报 | 每日 | 中 | 360安全中心旗下的安全资讯平台，专注于中文安全内容。经常发布Windows漏洞的分析文章和安全建议。 |
| 49 | VulDB | https://vuldb.com | 漏洞数据库/威胁情报/利用预测 | 每日 | 中 | VulDB声称是全球最大的漏洞数据库之一，提供比NVD更快速的漏洞收录和更丰富的上下文信息。 |
| 50 | CERT/CC Vulnerability Notes | https://www.kb.cert.org/vuls/ | 漏洞公告/协调披露/安全建议 | 每周 | 中 | 卡内基梅隆大学软件工程研究所运营的CERT Coordination Center，是美国最早的网络安全漏洞协调机构之一。 |
| 51 | CN-SEC 中文网 | https://cn-sec.com | 中文安全资讯/漏洞分析/安全工具/技术博客聚合 | 每日 | 中 | 中文网络安全资讯聚合平台，收录Apple/macOS安全相关的中文技术文章和漏洞分析。 |
| 52 | OSV.dev - Open Source Vulnerabilities | https://osv.dev | 开源漏洞数据库/多源聚合/精确版本匹配 | 实时 | 高 | Google开发的开源漏洞数据库，聚合24个数据源，支持Windows组件漏洞的精确版本匹配和AOSP同源漏洞追踪。提供RESTful API。 |
| 53 | Vulners | https://vulners.com | 漏洞搜索引擎/多源聚合/威胁情报 | 实时 | 高 | 集成的漏洞搜索引擎，聚合数十个来源。2025年12月起search/id API完全免费。覆盖Windows、Linux、macOS全平台漏洞。 |
| 54 | GreyNoise | https://www.greynoise.io | 互联网扫描活动/漏洞利用检测/威胁标签 | 实时 | 高 | GreyNoise通过全球传感器网络监测互联网扫描活动，能够区分恶意扫描和良性研究活动。对评估Windows服务暴露风险有重要价值。 |
| 55 | CERT-FR (France) | https://www.cert.ssi.gouv.fr | 法国政府安全公告/漏洞警告/应急响应指导 | 每日 | 高 | 法国政府CERT，由ANSSI运营。公告频率高，在欧洲厂商漏洞披露方面往往比英语来源更早发布。涵盖全平台漏洞。 |
| 56 | Canadian Centre for Cyber Security | https://www.cyber.gc.ca | 安全警报/漏洞公告/威胁评估 | 每周 | 中 | 加拿大官方网络安全机构，发布高质量的安全警报和漏洞公告。CISA的"五眼联盟"合作伙伴，公告格式标准化（AL-XXXX编号）。 |
| 57 | ACSC - Australian Cyber Security Centre | https://www.cyber.gov.au | 安全警报/漏洞公告/威胁建议 | 每周 | 中 | 澳大利亚官方网络安全机构，采用ASD Essential Eight框架提供缓解建议。 |
| 58 | MISP Project | https://www.misp-project.org | 威胁情报共享平台/IoC指标/漏洞信息/恶意软件分析 | 实时 | 高 | 全球广泛采用的开源威胁情报共享平台，被各国CERT、安全厂商和私营企业使用。支持漏洞信息的结构化和关联分析。 |
| 59 | 奇安信威胁情报中心 | https://ti.qianxin.com | 威胁情报/漏洞分析/安全公告/事件追踪 | 每日 | 中 | 奇安信集团旗下威胁情报中心，国内领先的威胁情报平台。提供全面的漏洞情报、APT追踪、黑产研究等内容。中文内容丰富。 |
| 60 | 绿盟科技技术博客 | https://blog.nsfocus.net | 安全公告/漏洞通告/威胁月报 | 每周 | 高 | 绿盟科技（NSFOCUS）是国内老牌网络安全厂商，持续发布微软月度安全更新漏洞通告。 |
| 61 | 知道创宇 Seebug 漏洞平台 | https://www.seebug.org | 漏洞库/PoC/Exp共享/漏洞情报 | 每日 | 中 | 国内历史最悠久的漏洞平台之一，收录海量漏洞数据，提供PoC/Exp共享。 |
| 62 | 阿里云漏洞库（AVD） | https://avd.aliyun.com | 漏洞库/安全公告/漏洞管理 | 每日 | 高 | 阿里云漏洞库及时响应和收敛云上高危漏洞，提供漏洞POC技术细节和修复建议。 |
| 63 | 微步在线 X情报社区 | https://x.threatbook.com | 威胁情报/漏洞情报/资产测绘/样本分析 | 每日 | 中 | 微步在线是国内领先的威胁情报企业，X情报社区提供威胁情报查询、漏洞情报等功能。 |

---

## 二、系统漏洞（54个网站）

> 系统漏洞板块涵盖操作系统层面的本地提权、内核漏洞、容器逃逸、系统组件漏洞等，帮助用户管理系统级安全威胁。

### 2.1 Windows（10个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 64 | Microsoft Update Catalog | https://www.catalog.update.microsoft.com | 安全更新下载/补丁库 | 实时 | 中 | Windows安全补丁的官方集中下载源。提供.msu和.cab格式的离线安装包，覆盖所有支持的Windows版本。 |
| 65 | LOLDrivers Project | https://www.loldrivers.io | 漏洞驱动数据库/攻击技术研究 | 每周 | 高 | 专门记录Windows平台已知漏洞驱动程序（vulnerable drivers）的社区项目。这些驱动被攻击者用于Living Off The Land技术。 |
| 66 | 0patch Blog | https://blog.0patch.com | 微补丁技术分析/漏洞深度研究 | 每周 | 中 | 0patch是Windows平台第三方微补丁解决方案的领导者。其博客发布高质量的漏洞技术分析，详细解释漏洞根因和利用路径。 |
| 67 | Microsoft Security Blog (Threat Intelligence) | https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence | 威胁情报/安全研究/漏洞利用分析 | 每周 | 高 | Microsoft官方威胁情报博客，由Microsoft Threat Intelligence Center (MSTIC)撰写。提供Windows漏洞在野利用的第一手分析报告。 |
| 68 | SecWiki Windows Kernel Exploits (GitHub) | https://github.com/SecWiki/windows-kernel-exploits | Windows内核漏洞利用集合/提权工具 | 不定期 | 高 | 中文安全社区SecWiki维护的Windows平台提权漏洞集合。收集了从Windows XP到Windows 11各版本的内核提权漏洞利用工具。 |
| 69 | Tenable / Nessus | https://www.tenable.com | 漏洞扫描插件/漏洞分析报告 | 每日 | 中 | 全球领先的漏洞管理厂商。Tenable Research发布高质量的Windows漏洞分析，Nessus插件库覆盖Windows全系产品漏洞检测。 |
| 70 | Qualys Security Advisories | https://www.qualys.com/security-advisories | 安全公告/漏洞研究 | 每月/实时 | 中 | Qualys是知名云安全与合规厂商，其安全公告涵盖Windows产品漏洞研究。Qualys的Threat Research团队发布高质量的漏洞分析报告。 |
| 71 | Fortinet FortiGuard Labs | https://www.fortiguard.com/encyclopedia | 漏洞百科/IPS签名库/威胁情报 | 每日 | 中 | Fortinet的FortiGuard Labs维护的漏洞百科全书，包含Windows漏洞的详细技术信息和防护签名。 |
| 72 | SOC Prime / CVE Analysis | https://socprime.com/blog/latest-threats | 威胁检测规则/CVE分析/威胁狩猎 | 每周 | 中 | SOC Prime提供基于社区的威胁检测内容平台。将漏洞情报转化为可操作的SIEM/EDR检测规则。 |
| 73 | Rapid7 / AttackerKB | https://www.rapid7.com/blog | 漏洞分析/渗透测试研究/社区评估 | 每周 | 高 | Rapid7的InsightVM是主流漏洞管理方案。其安全研究团队发布深度Windows漏洞分析。AttackerKB是社区驱动的漏洞知识库。 |

### 2.2 Linux（12个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 74 | Linux Kernel CVE Announcement Mailing List | https://lore.kernel.org/linux-cve-announce/ | 官方CVE公告邮件列表 | 每日 | 高 | Linux内核CVE公告的官方发布渠道，由Greg Kroah-Hartman维护。所有Linux内核CVE首先在此发布。 |
| 75 | Linux Kernel Git Repository | https://git.kernel.org | 源码仓库/安全补丁提交/Commit历史 | 实时 | 极高 | Linux内核官方Git仓库，包含所有安全补丁的原始commit。可通过git log --grep="CVE"直接搜索安全修复。 |
| 76 | LinuxSecurity.com | https://linuxsecurity.com | Linux安全新闻/漏洞公告聚合/安全建议 | 每日 | 中 | 最大的Linux安全专业媒体，聚合所有主流发行版的安全公告，同时发布原创安全分析和深度文章。 |
| 77 | OpenWall linux-distros Mailing List Stats | https://oss-security.openwall.org/wiki/mailing-lists/distros | 发行版安全协调/CVE预披露统计 | 每日 | 高 | 追踪Linux发行版安全团队之间的协调披露过程。提供详细的CVE embargo统计。 |
| 78 | GNU GRUB2 Security Issues | https://www.gnu.org/software/grub/grub-documentation.html | 启动加载器安全公告/文档 | 不定期 | 高 | GRUB2是Linux系统最广泛使用的启动加载器，其漏洞直接影响系统启动链安全。 |
| 79 | systemd Security Trackers | https://github.com/systemd/systemd/security | CVE聚合/安全公告/GitHub Security Advisories | 实时 | 高 | systemd是现代Linux系统的init系统和核心服务管理器。2024-2026年发现大量严重漏洞。 |
| 80 | Sudo Security | https://www.sudo.ws/security.html | 认证系统安全公告/CVE详情 | 不定期 | 高 | Linux-PAM和sudo是Linux系统认证和授权的核心组件。2025-2026年发现多个严重漏洞。 |
| 81 | runc / containerd Security Advisories | https://github.com/opencontainers/runc/security/advisories | 容器运行时安全公告/GitHub Security Advisories | 不定期 | 高 | runc是Linux容器的底层运行时（Docker/Kubernetes核心组件）。2024-2025年发现多个容器逃逸漏洞。 |
| 82 | openEuler 安全公告 | https://gitee.com/openeuler/kernel/issues | CVE追踪/安全补丁/国内发行版安全响应 | 每日 | 中 | 华为openEuler是国内最重要的企业级Linux发行版之一，其安全响应机制成熟。提供完整的CVE追踪信息。 |
| 83 | Debian Wiki - Security Management | https://wiki.debian.org/SecurityManagement | Wiki知识库/安全文档 | 每月 | 高 | Debian官方安全Wiki门户，提供Securing Debian Manual、安全加固指南、AppArmor/SELinux配置等系统性安全文档。 |
| 84 | Gentoo Wiki - Security Handbook | https://wiki.gentoo.org/wiki/Security_Handbook | Wiki知识库/安全手册 | 每月 | 高 | Gentoo官方安全手册，涵盖从引导路径安全、内核加固、PAM配置、防火墙到入侵检测的完整安全知识体系。 |
| 85 | Kali Linux Community | https://www.kali.org/community/ | 安全测试社区/论坛/Discord | 每日 | 中 | Kali Linux是全球最流行的渗透测试发行版，其官方社区包括论坛、Discord服务器、IRC频道和GitLab，聚集大量安全测试和漏洞研究人员。 |

### 2.3 macOS（10个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 86 | Apple Security Content Pages | https://support.apple.com/en-us/122716 | 漏洞公告/技术文档 | 每月 | 高 | 每个macOS版本更新的详细安全内容页面，列出所有修复的CVE、漏洞描述和研究者署名。 |
| 87 | Jamf Blog / Jamf Threat Labs | https://www.jamf.com/blog/ | 安全研究/漏洞分析/技术博客 | 每周 | 中 | Apple企业管理和安全领域的领导者。Jamf Threat Labs经常发布macOS漏洞的高质量研究。 |
| 88 | Macworld | https://www.macworld.com | 安全新闻/消费者安全指南 | 每周 | 中 | 最具影响力的Mac专业媒体，提供面向消费者的macOS安全报道。 |
| 89 | 9to5Mac | https://9to5mac.com | 安全新闻/技术报道 | 每日 | 中 | 最大的Apple新闻网站之一，设有Security Bite专栏专门报道macOS/iOS安全问题。 |
| 90 | SecureMac | https://www.securemac.com | macOS安全新闻/恶意软件分析/播客 | 每周 | 中 | 专注macOS安全的老牌网站，提供SecureMac Checklist播客、macOS恶意软件分析、安全工具评测。 |
| 91 | Mr. Macintosh | https://mrmacintosh.com | macOS更新/安全内容分析 | 每周 | 中 | 专注macOS系统更新的技术博客，详细分析每个macOS版本更新的安全修复内容。 |
| 92 | CVEfeed.io | https://cvefeed.io | CVE数据库/漏洞情报 | 每日 | 高 | 聚合型CVE情报平台，整合CISA KEV、GitHub PoC、NVD数据。可快速查看Apple CVE的完整上下文。 |
| 93 | Cybersecurity News | https://cybersecuritynews.com | 安全新闻/漏洞报道 | 每日 | 中 | 网络安全新闻媒体，提供macOS漏洞的技术细节和修复建议。 |
| 94 | Wiz Vulnerability Database | https://www.wiz.io/vulnerability-database/ | CVE数据库/云安全 | 每日 | 中 | 云安全厂商维护的漏洞数据库，包含macOS CVE的影响分析、可利用性评估和修复步骤。 |
| 95 | Google Project Zero | https://projectzero.google | 安全研究/漏洞分析 | 每月 | 高 | Google顶级安全研究团队，定期发布Apple产品漏洞的深入分析。 |

### 2.4 跨平台/通用（22个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 96 | OpenCVE | https://app.opencve.io | CVE聚合/厂商漏洞追踪/通知服务 | 实时 | 中 | 开源CVE通知平台，支持按厂商/产品订阅漏洞通知。对Linux组件（如systemd_project、linux-pam、kernel）有专门的漏洞聚合页面。 |
| 97 | Qualys Threat Research Unit (TRU) | https://blog.qualys.com/vulnerabilities-threat-research | 原创漏洞研究/安全公告/技术分析 | 每月 | 中 | Qualys TRU是全球顶尖的安全研究团队，发现了多个重大Linux漏洞。提供详细的技术报告和PoC分析。 |
| 98 | Fidelis Security | https://fidelissecurity.com/vulnerabilities/ | 漏洞情报/安全分析 | 每周 | 中 | 企业级安全厂商，提供macOS漏洞的合规与治理分析。 |
| 99 | MITRE ATT&CK | https://attack.mitre.org | 攻击战术/技术知识库/威胁行为者画像/缓解措施 | 每季度 | 高 | 全球最广泛采用的威胁行为知识库。将CVE漏洞映射到ATT&CK技术，帮助理解漏洞在攻击链中的实际作用。 |
| 100 | CIRCL CVE Search | https://cve.circl.lu | CVE搜索/漏洞浏览/CPE/CWE/CAPEC关联 | 每日 | 高 | 由卢森堡CIRCL运营的免费CVE搜索服务，是欧洲最权威的公共CVE查询平台之一。聚合NVD、CPE、CWE、CAPEC等多个数据源。提供完整RESTful API。 |
| 101 | Snyk Vulnerability Database | https://security.snyk.io | 漏洞数据库/恶意包检测/容器安全/修复建议 | 每日 | 中 | 领先的商业漏洞数据库，不仅聚合公开来源，还有安全分析师团队审核，提供独特的未公开漏洞。 |
| 102 | GitLab Advisory Database (GLAD) | https://advisories.gitlab.com | 漏洞公告/安全数据库 | 实时 | 高 | GitLab官方维护的安全公告数据库，覆盖大量开源组件漏洞，与CI/CD安全扫描深度集成。 |
| 103 | Recorded Future | https://www.recordedfuture.com | 威胁情报平台/漏洞风险评分/威胁行为者追踪 | 实时 | 中 | 领先的威胁情报平台，Vulnerability Intelligence模块包含专门的漏洞风险评分（0-99），预测被利用概率。 |
| 104 | Flashpoint (VulnDB) | https://flashpoint.io | 漏洞情报/威胁情报/欺诈情报 | 实时 | 中 | VulnDB是最全面的商业漏洞数据库之一，包含105,000+条NVD未收录的漏洞。提供独特的勒索软件可能性和社会风险评分。 |
| 105 | Shodan | https://www.shodan.io | 互联网连接设备搜索/暴露服务发现/漏洞暴露面 | 持续扫描 | 高 | "物联网的搜索引擎"，支持漏洞关键词搜索，显示全球存在特定漏洞的系统数量。提供API服务。 |
| 106 | 安恒信息安全星图平台 | https://starmap.dbappsecurity.com.cn | 威胁情报/漏洞情报/APT追踪/云沙箱 | 每日 | 中 | 安恒信息安全星图平台专注于威胁情报的收集、处理、分析与应用。提供漏洞情报、APT追踪和云沙箱分析。 |
| 107 | 深信服安全公告中心 | https://www.sangfor.com.cn/sec_center/ | 安全公告/漏洞通告/PSIRT | 每月 | 中 | 深信服（Sangfor）安全应急响应中心，负责披露深信服产品和业界漏洞信息。 |
| 108 | 安全客 | https://www.anquanke.com | 安全新闻/技术文章/安全工具/行业动态 | 每日 | 高 | 综合性网络安全社区和资讯平台，提供丰富的中文安全文章和行业动态。 |
| 109 | 看雪安全社区 | https://bbs.kanxue.com | 安全论坛/逆向工程/漏洞分析/技术交流 | 每日 | 高 | 国内历史最悠久的安全社区之一，以逆向工程、加解密技术、漏洞分析为核心主题。适合获取深度的系统漏洞分析文章。 |
| 110 | 吾爱破解 | https://www.52pojie.cn | 软件安全论坛/逆向分析/脱壳破解/编程技术 | 每日 | 高 | 国内知名的软件安全技术论坛，专注于软件破解、逆向工程、安全技术等方面。 |
| 111 | 阿里云安全公告 | https://www.aliyun.com/notice/ | 安全公告/漏洞通告/风险预警 | 每日 | 高 | 阿里云官方安全公告平台，发布云上产品和服务相关的安全漏洞通告、风险预警和修复方案。 |
| 112 | 腾讯安全应急响应中心（TSRC） | https://security.tencent.com | 安全公告/漏洞披露/SRC众测 | 每周 | 中 | 腾讯官方安全应急响应中心，旗下腾讯安全玄武实验室是国际上知名的安全研究团队。 |
| 113 | 华为安全应急响应中心（Huawei PSIRT） | https://www.huawei.com/cn/psirt/security-advisories/ | 安全通告/漏洞公告/补丁发布 | 每月 | 高 | 华为官方安全应急响应中心，发布华为全线产品的安全通告。中文公告为本土用户提供权威参考。 |
| 114 | 360安全应急响应中心（360 SRC） | https://security.360.cn | 漏洞响应/威胁情报/安全研究 | 每周 | 中 | 360集团安全应急响应中心，旗下360威胁情报中心是国内领先的威胁情报机构。 |
| 115 | 启明星辰 VSRC | https://www.venustech.com.cn | 漏洞通告/安全公告/威胁研究 | 每周 | 中 | 启明星辰（Venustech）是国内最早的网络安全厂商之一，是CNVD一级技术支撑单位。 |
| 116 | OSCS 开源软件供应链安全社区 | https://www.oscs1024.com | 开源安全/软件供应链/漏洞检测/投毒情报 | 每日 | 高 | OSCS致力于提升开源生态安全，提供开源安全情报预警订阅。核心引擎murphysec已开源。 |
| 117 | 漏洞盒子（斗象科技） | https://www.vulbox.com | 安全众测/漏洞情报/白帽社区 | 每日 | 中 | 斗象科技旗下的漏洞盒子，是国内最大的安全众测服务平台和白帽社区之一，平台白帽注册人数超过11万。 |

---

## 三、系统故障排除（69个网站）

> 系统故障排除板块涵盖系统崩溃修复、性能优化、更新问题解决、硬件诊断等，帮助用户解决各类操作系统层面的技术问题。

### 3.1 Windows（15个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 118 | Microsoft Learn - Windows 故障排除文档中心 | https://learn.microsoft.com/en-us/troubleshoot/ | 官方技术文档/知识库/排错指南 | 每日/实时 | 高 | Microsoft官方维护的综合性故障排除文档中心，涵盖Windows全系产品的官方排错指南、已知问题、修复方案。 |
| 119 | Microsoft Support - Windows 帮助与学习 | https://support.microsoft.com/en-us/windows | 官方支持文章/教程/修复工具 | 每周 | 高 | Microsoft官方消费者支持门户，提供从基础设置到高级排错的完整指南。 |
| 120 | WindowsForum.com | https://windowsforum.com | 技术论坛/社区问答/教程 | 每日 | 中 | 最活跃的Windows专业论坛之一，拥有27.6K+主题和162.5K+回复。设有Windows帮助与支持、BSOD专题等完整板块。 |
| 121 | TenForums | https://www.tenforums.com | 技术论坛/教程/新闻 | 每日 | 中 | 最知名的Windows 10/11专业论坛之一，由资深MVP专家Brink等运营。提供大量注册表脚本、批处理工具、排错教程。 |
| 122 | Super User (Stack Exchange) | https://superuser.com/questions/tagged/windows | 问答社区/技术知识库 | 实时 | 高 | Stack Exchange网络中面向高级用户和IT专业人士的问答站点。Windows标签下有数十万高质量问答。 |
| 123 | Stack Overflow - Windows | https://stackoverflow.com/questions/tagged/windows | 开发者问答/编程排错/系统API | 实时 | 高 | 全球最大的开发者社区，Windows标签下涵盖PowerShell脚本、Windows API、系统管理等大量技术问答。 |
| 124 | MajorGeeks | https://www.majorgeeks.com | 软件下载/修复工具/注册表脚本/教程 | 每日 | 中 | 运营超过20年的老牌Windows技术站点，提供超过200+注册表/批处理/PowerShell修复脚本。 |
| 125 | Microsoft Tech Community | https://techcommunity.microsoft.com | 官方社区/博客/论坛/网络研讨会 | 每日 | 中 | Microsoft官方技术社区，直接连接Microsoft员工、MVP和广大IT专业人士。 |
| 126 | IBM Support - Windows PowerShell 性能排错指南 | https://www.ibm.com/support/pages/windows-performance-troubleshooting-using-powershell-sysinternals | 企业级技术文档/排错指南 | 每季度 | 高 | IBM官方发布的Windows性能排错综合指南，整合了PowerShell命令、性能计数器、Sysinternals工具。 |
| 127 | ComputerWorld | https://www.computerworld.com | 专业IT媒体/深度教程 | 每月 | 高 | 老牌IT专业媒体发布的Windows 10/11修复深度指南。包含DISM/SFC、系统还原、就地升级等完整的排错流程。 |
| 128 | XDA Developers | https://www.xda-developers.com | 技术博客/教程/开发者工具 | 每日 | 高 | 知名科技媒体，提供Windows排错专题，涵盖磁盘健康检查、系统性能测试、网络连通性、事件日志分析等。 |
| 129 | Microsoft Q&A | https://learn.microsoft.com/en-us/answers/ | 官方问答平台/技术支持 | 实时 | 高 | Microsoft官方问答平台，由Microsoft支持工程师、MVP和社区专家回答。 |
| 130 | Windows 101 Tricks | https://windows101tricks.com | 技术博客/故障排除教程/优化指南 | 每周 | 中 | 专注Windows故障排除和优化的技术博客，提供大量关于BSOD修复、Windows更新问题解决、系统性能优化的实用教程。 |
| 131 | Tweaking.com - Windows Repair | https://www.tweaking.com | 系统修复工具/排错软件 | 每月 | 中 | 广受欢迎的Windows一站式修复工具，可修复注册表权限、Windows Update、防火墙、Winsock/DNS缓存等常见问题。 |
| 132 | Microsoft DevBlogs | https://devblogs.microsoft.com | 官方开发者博客/脚本教程 | 每周 | 高 | Microsoft官方开发者博客网络，包含Scripting Blog（PowerShell自动化排错）等，提供来自Microsoft工程师的一手技术内容。 |

### 3.2 Linux（21个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 133 | Arch Wiki - 系统维护与故障排除 | https://wiki.archlinux.org/title/System_maintenance | 技术文档/知识库/Wiki | 实时 | 高 | Arch Wiki被誉为最全面的Linux技术文档资源，虽然面向Arch Linux，但绝大多数内容适用于所有Linux发行版。 |
| 134 | Debian Wiki - TroubleShooting | https://wiki.debian.org/TroubleShooting | 技术文档/Wiki/故障排除指南 | 实时 | 高 | Debian官方故障排除Wiki，提供从错误消息解读、日志分析到Bug报告提交的完整流程指导。 |
| 135 | Ubuntu Community Help Wiki | https://help.ubuntu.com/community/TroubleShootingGuide | 技术文档/社区指南 | 每月 | 中 | Ubuntu官方社区故障排除指南，面向新手友好但内容全面。涵盖从基础诊断到高级故障排除的完整方法论。 |
| 136 | Gentoo Wiki - Troubleshooting | https://wiki.gentoo.org/wiki/Troubleshooting | 技术文档/Wiki | 实时 | 高 | Gentoo官方故障排除页面，提供了大量发行版无关的故障排除技巧和工具集。 |
| 137 | openSUSE/SUSE Documentation | https://doc.opensuse.org/documentation/leap/startup/html/book-startup/cha-trouble.html | 官方文档/技术手册 | 每版本更新 | 高 | SUSE/openSUSE官方文档中的故障排除章节，内容专业且全面。涵盖引导问题、网络问题、数据问题的解决方案。 |
| 138 | Unix & Linux Stack Exchange | https://unix.stackexchange.com/questions | 问答社区/技术论坛 | 实时 | 高 | 最专业的Linux/Unix技术问答社区。覆盖从基础命令到内核调试的全范围问题。 |
| 139 | Ask Ubuntu | https://askubuntu.com | 问答社区 | 实时 | 高 | Ubuntu官方问答社区，Stack Exchange网络成员。提供Ubuntu特定的安装、配置、故障排除解决方案。 |
| 140 | LinuxQuestions.org | https://www.linuxquestions.org | 论坛社区 | 每日 | 中 | 成立于2000年，是最古老和最活跃的Linux社区之一。论坛内容覆盖全面，从基础问题到高级服务器故障排除都有涉及。 |
| 141 | OSTechNix | https://ostechnix.com | 技术博客/教程 | 每周 | 高 | 提供实用的Linux故障排除文章，其代表作提供了系统管理员在排查Linux系统前应执行的只读命令清单。 |
| 142 | TecMint | https://www.tecmint.com | 技术教程/Howto | 每周 | 高 | 最流行的Linux教程网站之一，提供大量关于网络配置和故障排除的实用文章。 |
| 143 | HowToForge | https://www.howtoforge.com | 技术教程/服务器配置 | 每周 | 高 | 专注于Linux服务器教程的大型网站，拥有超过5700篇教程。涵盖Ubuntu、Debian、CentOS、Fedora等主流发行版。 |
| 144 | Linuxize | https://linuxize.com | 技术博客/教程 | 每周 | 高 | 由RHCSA认证的Linux系统管理员维护，提供800+篇Linux教程。 |
| 145 | Red Hat Knowledgebase | https://access.redhat.com/kb/ | 厂商知识库/技术文档 | 每日 | 低 | Red Hat官方知识库，提供最权威的RHEL故障排除解决方案。包含大量的解决方案文章、产品文档、安全配置指南。 |
| 146 | SUSE Knowledgebase | https://www.suse.com/support/kb/ | 厂商知识库 | 每周 | 中 | SUSE官方知识库，提供SLES/SLED的Technical Information Documents (TIDs)。 |
| 147 | Linux Kernel Documentation | https://www.kernel.org/doc/html/latest/ | 官方技术文档 | 随内核版本更新 | 高 | Linux内核官方文档，提供最权威的底层系统信息。对于涉及内核panic、驱动问题、文件系统错误等深层故障排除至关重要。 |
| 148 | The Linux Documentation Project (TLDP) | https://tldp.org | 技术文档/HOWTO/指南 | 每月 | 高 | 最古老的Linux文档项目之一，收集和维护了大量的HOWTO、指南和FAQ。 |
| 149 | Linux Hardware Database | https://linux-hardware.org | 硬件兼容性数据库 | 实时 | 高 | 目前最大和最新的Linux硬件数据库，包含数百万条关于主板、CPU、GPU、显示器和外设的记录。 |
| 150 | Ubuntu Certified Hardware | https://ubuntu.com/certified | 官方硬件认证数据库 | 每月 | 中 | Canonical官方认证的Ubuntu硬件数据库。列出所有经过Ubuntu认证的硬件设备。 |
| 151 | Phoronix | https://www.phoronix.com | 技术新闻/硬件评测/性能基准 | 每日 | 高 | 最权威的Linux硬件新闻和评测网站。其Phoronix Test Suite是Linux基准测试的标准工具。 |
| 152 | LWN.net (Linux Weekly News) | https://lwn.net | 技术新闻/深度分析 | 每周 | 中 | 最深入的Linux技术新闻来源。提供Linux内核开发、发行版动态、安全漏洞的深度分析文章。 |
| 153 | Fedora Docs | https://docs.fedoraproject.org | 官方文档 | 持续更新 | 高 | Fedora官方文档站点，包含内核故障排除、启动问题诊断等详细指南。 |

### 3.3 macOS（21个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 154 | Apple Support (macOS Recovery) | https://support.apple.com/en-us/102518 | 官方技术文档/恢复指南 | 实时 | 高 | Apple官方macOS恢复模式完整指南，涵盖Apple Silicon和Intel两种架构的恢复步骤。 |
| 155 | Apple Support (macOS Update Errors) | https://support.apple.com/en-us/102531 | 官方技术文档/错误排除 | 实时 | 高 | Apple官方macOS更新和安装错误解决方案。覆盖存储空间不足、网络连接问题、安装器损坏等常见错误。 |
| 156 | Apple Support (Disk Utility Repair) | https://support.apple.com/en-us/102611 | 官方技术文档/磁盘修复 | 实时 | 高 | Apple官方Disk Utility使用指南，详细说明如何使用First Aid修复启动磁盘、容器和卷。 |
| 157 | Apple Support (Apple Diagnostics) | https://support.apple.com/en-us/102550 | 官方技术文档/硬件诊断 | 实时 | 高 | Apple官方硬件诊断工具使用指南。支持Apple Silicon和Intel Mac，覆盖Wi-Fi、键盘、内存、电池等组件。 |
| 158 | Apple Support (Time Machine Troubleshooting) | https://support.apple.com/guide/mac-help/time-machine-troubleshooting-mh15653/mac | 官方技术文档/备份故障排除 | 实时 | 高 | Apple官方Time Machine故障排除指南，涵盖备份磁盘连接问题、macOS版本兼容性、网络备份问题等。 |
| 159 | Apple Support Community | https://discussions.apple.com | 官方社区论坛/问答 | 实时 | 中 | Apple官方支持社区，数百万用户参与的问题解答平台。涵盖macOS启动故障排除、软件问题、硬件问题等。 |
| 160 | Apple Developer Forums | https://developer.apple.com/forums/ | 开发者论坛/技术讨论 | 实时 | 中 | Apple官方开发者论坛，包含Feedback Assistant使用指南、sysdiagnose日志收集、调试技巧等高级故障排除内容。 |
| 161 | MacRumors Forums | https://forums.macrumors.com | 技术论坛/社区讨论 | 实时 | 中 | 最大最活跃的Apple技术社区之一。包含macOS beta测试反馈、内核恐慌故障排除、Keychain问题等详细讨论。 |
| 162 | Apple Stack Exchange | https://apple.stackexchange.com | 问答社区/知识库 | 实时 | 高 | StackExchange网络下的Apple专业问答社区。覆盖macOS Internet Sharing故障排除、Terminal命令问题、系统配置等深度技术问题。 |
| 163 | Mac Help Forums | https://www.mac-help.com | 社区论坛 | 每日 | 中 | 专注Mac帮助的社区论坛，拥有20,000+主题、85,000+消息、18,000+会员。 |
| 164 | OSXDaily | https://osxdaily.com | 技术博客/教程 | 每日 | 高 | 专注macOS和Apple生态系统的技术博客，运营超过15年。覆盖WindowServer高CPU使用故障排除、Wi-Fi问题等大量实用教程。 |
| 165 | MacObserver | https://www.macobserver.com | 科技媒体/教程 | 每周 | 中 | 知名Apple资讯网站，提供macOS内核恐慌错误修复指南等深入教程。 |
| 166 | Setapp Blog | https://setapp.com/how-to/ | 技术博客/故障排除指南 | 每周 | 中 | 提供全面的macOS问题修复指南，涵盖基础故障排除到高级方法（Recovery Mode、Safe Mode等）。 |
| 167 | iFixit - Mac Repair Guides | https://www.ifixit.com/Device/Mac | 硬件维修指南/故障排除 | 每周 | 高 | 全球领先的DIY维修指南平台，提供MacBook、iMac、Mac mini等完整拆机和维修教程。 |
| 168 | Heatware | https://www.heatware.net/macos/ | 技术博客/综合指南 | 每月 | 中 | 提供终极macOS技巧、故障排除和优化指南，涵盖Wi-Fi问题解决、网络诊断命令等深度内容。 |
| 169 | AppleToolBox | https://appletoolbox.com | 技术博客/故障排除 | 每周 | 中 | 专注Apple产品故障排除的技术博客，覆盖macOS系统问题、App故障、网络问题、硬件问题等广泛主题。 |
| 170 | Informatics Systems - macOS Troubleshooting | https://informatics.systems/blog/macos-troubleshooting/ | 综合故障排除指南 | 定期更新 | 中 | 提供系统化的macOS故障排除方法，涵盖基础技巧、磁盘管理、应用问题解决、Safe Mode和Recovery Mode使用等。 |
| 171 | MacPaw Knowledge Base | https://macpaw.com/how-to/ | 知识库/教程 | 每周 | 中 | MacPaw（CleanMyMac开发商）运营的知识库，提供Time Machine备份失败排除、MacBook充电问题修复等高质量故障排除文章。 |
| 172 | Jamf Nation Community | https://community.jamf.com | 专业社区论坛 | 实时 | 中 | 全球最大企业Mac管理社区，涵盖MDM部署、安全策略、系统故障排除等专业领域。 |
| 173 | Apple 支持 (中国) | https://support.apple.com/zh-cn/102531 | 官方中文技术文档 | 实时 | 高 | Apple中国官方支持页面，提供如果在更新或安装macOS时发生错误的完整中文解决方案。 |
| 174 | V2EX | https://www.v2ex.com | 中文技术社区/程序员论坛 | 实时 | 低 | 中文互联网最具影响力的程序员社区之一，拥有众多关于Windows/macOS/Linux系统问题排查的实用讨论帖。 |

### 3.4 跨平台/通用（12个）

| 编号 | 网站名称 | URL | 内容类型 | 更新频率 | 爬虫友好度 | 推荐理由 |
|------|---------|-----|---------|---------|-----------|---------|
| 175 | How-To Geek | https://www.howtogeek.com | 技术教程/排错指南/科普文章 | 每日 | 高 | 面向普通用户的高质量技术教程网站，提供大量Windows故障排除、系统优化、注册表编辑等教程。 |
| 176 | 腾讯云开发者社区 | https://cloud.tencent.com/developer/ | 中文技术文档/教程/开发者社区 | 每日 | 中 | 腾讯云开发者社区发布大量高质量的Windows系统排错中文教程，如DISM/SFC修复、蓝屏排查、驱动问题解决等。 |
| 177 | CSDN博客 | https://blog.csdn.net | 中文技术博客/教程 | 每日 | 中 | 中国最大的IT技术社区，有大量Windows系统修复、蓝屏解决、驱动安装等中文教程。 |
| 178 | FreeBSD Forums | https://forums.freebsd.org | 论坛/技术支持/故障排除 | 每日 | 中 | FreeBSD官方论坛，是BSD系统最活跃的技术社区之一。故障排除内容对Linux用户也有参考价值。 |
| 179 | Spiceworks Community | https://community.spiceworks.com | IT社区/技术支持/故障排除 | 每日 | 中 | 全球最大的IT专业人士社区之一，涵盖Windows Server/Linux服务器故障排除、网络诊断、补丁管理、漏洞响应等主题。 |
| 180 | Tom's Hardware Forums | https://forums.tomshardware.com | 硬件/系统故障排除论坛 | 每日 | 中 | 全球知名的硬件技术论坛，拥有大量Windows/Linux系统故障排除资源。标志性的No POST troubleshooting checklist帖子被引用超过十年。 |
| 181 | TechSpot | https://www.techspot.com | 科技新闻/教程/论坛 | 每日 | 中 | 知名科技媒体网站，提供深度技术文章、硬件评测和系统故障排除指南。 |
| 182 | Lifewire | https://www.lifewire.com | 技术教程/故障排除/产品评测 | 每日 | 中 | 以清晰易懂的教程风格著称。提供涵盖Windows、macOS、Linux系统的计算机和软件指南。 |
| 183 | Information Security Stack Exchange | https://security.stackexchange.com | 信息安全Q&A/技术论坛 | 实时 | 中 | 最专业的信息安全Q&A社区之一，由安全从业者、研究人员共同维护。涵盖漏洞分析、渗透测试、安全加固等主题。 |
| 184 | Server Fault | https://serverfault.com | 系统管理Q&A/服务器故障排除 | 实时 | 中 | 面向专业系统管理员和IT基础设施工程师的Q&A平台。涵盖服务器配置、网络故障、系统安全补丁等主题。 |
| 185 | 天融信安全通告 | https://www.topsec.com.cn | 安全通告/漏洞周报/威胁情报 | 每周 | 低 | 天融信（TOPSEC）是中国领先的网络安全厂商，定期发布安全通告PDF和威胁周报。 |
| 186 | 补天平台（奇安信） | https://www.butian.net | 漏洞响应/众测平台/白帽社区 | 每日 | 低 | 全球最大的漏洞响应平台之一，通过现金悬赏方式号召白帽子帮助厂商发现并修复漏洞。 |

---

## 四、跨平台通用资源汇总

> 以下资源在多个板块中均有价值，适合作为全平台通用数据源进行爬取。

### 通用资源列表（61个独立网站）

| 编号 | 网站名称 | URL | 适用板块 | 内容类型 | 爬虫友好度 |
|------|---------|-----|---------|---------|-----------|
| 1 | National Vulnerability Database (NVD) | https://nvd.nist.gov | 网络漏洞 | 漏洞数据库/CVSS评分/结构化数据 | 高 |
| 2 | CISA Known Exploited Vulnerabilities (KEV) Catalog | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | 网络漏洞 | 已知被利用漏洞清单/威胁情报 | 高 |
| 3 | CVE.org (MITRE) | https://cve.org | 网络漏洞 | CVE编号分配/漏洞标识/结构化数据 | 高 |
| 4 | The Hacker News | https://thehackernews.com | 网络漏洞 | 安全新闻/漏洞分析/威胁情报 | 高 |
| 5 | SecurityWeek | https://www.securityweek.com | 网络漏洞 | 安全新闻/漏洞公告/会议报道 | 中 |
| 6 | Rapid7 Vulnerability & Exploit Database | https://www.rapid7.com/db/ | 网络漏洞 | 漏洞数据库/Exploit模块/Metasploit集成 | 高 |
| 7 | Packet Storm Security | https://packetstormsecurity.com | 网络漏洞 | Exploit/PoC/安全公告/工具 | 高 |
| 8 | Trend Micro Zero Day Initiative (ZDI) | https://www.zerodayinitiative.com/advisories/ | 网络漏洞 | 零日漏洞公告/协调披露/技术分析 | 高 |
| 9 | GitHub Advisory Database | https://github.com/advisories | 网络漏洞 | 安全公告/CVE关联/依赖漏洞 | 高 |
| 10 | 国家信息安全漏洞库 / CNNVD | https://www.cnnvd.org.cn | 网络漏洞 | 漏洞公告/安全通报/预警信息 | 中 |
| 11 | FreeBuf (网络安全行业门户) | https://www.freebuf.com | 网络漏洞 | 安全文章/漏洞分析/技术博客/安全工具 | 中 |
| 12 | 安全客 (AQ.360.cn) | https://aq.360.cn | 网络漏洞 | 漏洞公告/安全资讯/威胁情报 | 中 |
| 13 | VulDB | https://vuldb.com | 网络漏洞 | 漏洞数据库/威胁情报/利用预测 | 中 |
| 14 | CERT/CC Vulnerability Notes | https://www.kb.cert.org/vuls/ | 网络漏洞 | 漏洞公告/协调披露/安全建议 | 中 |
| 15 | CN-SEC 中文网 | https://cn-sec.com | 网络漏洞 | 中文安全资讯/漏洞分析/安全工具/技术博客聚合 | 中 |
| 16 | OSV.dev - Open Source Vulnerabilities | https://osv.dev | 网络漏洞 | 开源漏洞数据库/多源聚合/精确版本匹配 | 高 |
| 17 | Vulners | https://vulners.com | 网络漏洞 | 漏洞搜索引擎/多源聚合/威胁情报 | 高 |
| 18 | GreyNoise | https://www.greynoise.io | 网络漏洞 | 互联网扫描活动/漏洞利用检测/威胁标签 | 高 |
| 19 | CERT-FR (France) | https://www.cert.ssi.gouv.fr | 网络漏洞 | 法国政府安全公告/漏洞警告/应急响应指导 | 高 |
| 20 | Canadian Centre for Cyber Security | https://www.cyber.gc.ca | 网络漏洞 | 安全警报/漏洞公告/威胁评估 | 中 |
| 21 | ACSC - Australian Cyber Security Centre | https://www.cyber.gov.au | 网络漏洞 | 安全警报/漏洞公告/威胁建议 | 中 |
| 22 | MISP Project | https://www.misp-project.org | 网络漏洞 | 威胁情报共享平台/IoC指标/漏洞信息/恶意软件分析 | 高 |
| 23 | 奇安信威胁情报中心 | https://ti.qianxin.com | 网络漏洞 | 威胁情报/漏洞分析/安全公告/事件追踪 | 中 |
| 24 | 绿盟科技技术博客 | https://blog.nsfocus.net | 网络漏洞 | 安全公告/漏洞通告/威胁月报 | 高 |
| 25 | 知道创宇 Seebug 漏洞平台 | https://www.seebug.org | 网络漏洞 | 漏洞库/PoC/Exp共享/漏洞情报 | 中 |
| 26 | 阿里云漏洞库（AVD） | https://avd.aliyun.com | 网络漏洞 | 漏洞库/安全公告/漏洞管理 | 高 |
| 27 | 微步在线 X情报社区 | https://x.threatbook.com | 网络漏洞 | 威胁情报/漏洞情报/资产测绘/样本分析 | 中 |
| 28 | OpenCVE | https://app.opencve.io | 系统漏洞 | CVE聚合/厂商漏洞追踪/通知服务 | 中 |
| 29 | Qualys Threat Research Unit (TRU) | https://blog.qualys.com/vulnerabilities-threat-research | 系统漏洞 | 原创漏洞研究/安全公告/技术分析 | 中 |
| 30 | Fidelis Security | https://fidelissecurity.com/vulnerabilities/ | 系统漏洞 | 漏洞情报/安全分析 | 中 |
| 31 | MITRE ATT&CK | https://attack.mitre.org | 系统漏洞 | 攻击战术/技术知识库/威胁行为者画像/缓解措施 | 高 |
| 32 | CIRCL CVE Search | https://cve.circl.lu | 系统漏洞 | CVE搜索/漏洞浏览/CPE/CWE/CAPEC关联 | 高 |
| 33 | Snyk Vulnerability Database | https://security.snyk.io | 系统漏洞 | 漏洞数据库/恶意包检测/容器安全/修复建议 | 中 |
| 34 | GitLab Advisory Database (GLAD) | https://advisories.gitlab.com | 系统漏洞 | 漏洞公告/安全数据库 | 高 |
| 35 | Recorded Future | https://www.recordedfuture.com | 系统漏洞 | 威胁情报平台/漏洞风险评分/威胁行为者追踪 | 中 |
| 36 | Flashpoint (VulnDB) | https://flashpoint.io | 系统漏洞 | 漏洞情报/威胁情报/欺诈情报 | 中 |
| 37 | Shodan | https://www.shodan.io | 系统漏洞 | 互联网连接设备搜索/暴露服务发现/漏洞暴露面 | 高 |
| 38 | 安恒信息安全星图平台 | https://starmap.dbappsecurity.com.cn | 系统漏洞 | 威胁情报/漏洞情报/APT追踪/云沙箱 | 中 |
| 39 | 深信服安全公告中心 | https://www.sangfor.com.cn/sec_center/ | 系统漏洞 | 安全公告/漏洞通告/PSIRT | 中 |
| 40 | 安全客 | https://www.anquanke.com | 系统漏洞 | 安全新闻/技术文章/安全工具/行业动态 | 高 |
| 41 | 看雪安全社区 | https://bbs.kanxue.com | 系统漏洞 | 安全论坛/逆向工程/漏洞分析/技术交流 | 高 |
| 42 | 吾爱破解 | https://www.52pojie.cn | 系统漏洞 | 软件安全论坛/逆向分析/脱壳破解/编程技术 | 高 |
| 43 | 阿里云安全公告 | https://www.aliyun.com/notice/ | 系统漏洞 | 安全公告/漏洞通告/风险预警 | 高 |
| 44 | 腾讯安全应急响应中心（TSRC） | https://security.tencent.com | 系统漏洞 | 安全公告/漏洞披露/SRC众测 | 中 |
| 45 | 华为安全应急响应中心（Huawei PSIRT） | https://www.huawei.com/cn/psirt/security-advisories/ | 系统漏洞 | 安全通告/漏洞公告/补丁发布 | 高 |
| 46 | 360安全应急响应中心（360 SRC） | https://security.360.cn | 系统漏洞 | 漏洞响应/威胁情报/安全研究 | 中 |
| 47 | 启明星辰 VSRC | https://www.venustech.com.cn | 系统漏洞 | 漏洞通告/安全公告/威胁研究 | 中 |
| 48 | OSCS 开源软件供应链安全社区 | https://www.oscs1024.com | 系统漏洞 | 开源安全/软件供应链/漏洞检测/投毒情报 | 高 |
| 49 | 漏洞盒子（斗象科技） | https://www.vulbox.com | 系统漏洞 | 安全众测/漏洞情报/白帽社区 | 中 |
| 50 | How-To Geek | https://www.howtogeek.com | 系统故障排除 | 技术教程/排错指南/科普文章 | 高 |
| 51 | 腾讯云开发者社区 | https://cloud.tencent.com/developer/ | 系统故障排除 | 中文技术文档/教程/开发者社区 | 中 |
| 52 | CSDN博客 | https://blog.csdn.net | 系统故障排除 | 中文技术博客/教程 | 中 |
| 53 | FreeBSD Forums | https://forums.freebsd.org | 系统故障排除 | 论坛/技术支持/故障排除 | 中 |
| 54 | Spiceworks Community | https://community.spiceworks.com | 系统故障排除 | IT社区/技术支持/故障排除 | 中 |
| 55 | Tom's Hardware Forums | https://forums.tomshardware.com | 系统故障排除 | 硬件/系统故障排除论坛 | 中 |
| 56 | TechSpot | https://www.techspot.com | 系统故障排除 | 科技新闻/教程/论坛 | 中 |
| 57 | Lifewire | https://www.lifewire.com | 系统故障排除 | 技术教程/故障排除/产品评测 | 中 |
| 58 | Information Security Stack Exchange | https://security.stackexchange.com | 系统故障排除 | 信息安全Q&A/技术论坛 | 中 |
| 59 | Server Fault | https://serverfault.com | 系统故障排除 | 系统管理Q&A/服务器故障排除 | 中 |
| 60 | 天融信安全通告 | https://www.topsec.com.cn | 系统故障排除 | 安全通告/漏洞周报/威胁情报 | 低 |
| 61 | 补天平台（奇安信） | https://www.butian.net | 系统故障排除 | 漏洞响应/众测平台/白帽社区 | 低 |

---

## 五、爬虫技术建议

### 5.1 推荐爬取策略

| 优先级 | 数据源类型 | 推荐工具 | 说明 |
|--------|-----------|---------|------|
| P0 | RSS/Atom Feed | feedparser + requests | 优先订阅NVD、CISA KEV、Red Hat RHSA的RSS Feed |
| P0 | REST API | requests + aiohttp | 调用OSV.dev、Vulners、NVD API获取结构化数据 |
| P1 | GitHub Advisory | requests + GitHub API | 使用GitHub GraphQL API批量获取安全公告 |
| P1 | 官方安全公告 | requests + BeautifulSoup | MSRC、Apple Security Releases等结构化页面 |
| P2 | 技术博客 | scrapy + playwright | BleepingComputer、The Hacker News等需要渲染 |
| P3 | 论坛/社区 | requests + 正则提取 | StackExchange API、Reddit API等优先使用官方API |

### 5.2 各板块重点API推荐

**网络漏洞板块：**
- **NVD API 2.0**: `https://services.nvd.nist.gov/rest/json/cves/2.0` — CVE详情、CVSS评分、CPE配置
- **OSV.dev API**: `https://api.osv.dev/v1/vulns/` — 开源漏洞精确版本匹配
- **Vulners API**: `https://vulners.com/api/v3/` — 聚合搜索（2025年12月起免费）
- **CISA KEV**: `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` — JSON Feed
- **GreyNoise API**: `https://api.greynoise.io/v3/` — 互联网扫描活动检测
- **MITRE ATT&CK**: `https://github.com/mitre/cti` — STIX格式的GitHub仓库

**系统漏洞板块：**
- **GitHub Advisory Database API**: `https://api.github.com/advisories` — 开源组件安全公告
- **Red Hat Security API**: `https://access.redhat.com/hydra/rest/securitydata/` — RHSA/CVE/OVAL数据
- **Debian Security Tracker API**: `https://security-tracker.debian.org/tracker/data/json` — JSON格式漏洞状态
- **Arch Linux Security API**: `https://security.archlinux.org/issues.json` — ASA公告JSON
- **SUSE Security API**: `https://www.suse.com/support/security/` — CVRF格式公告
- **Linux Kernel CVE Git**: `https://git.kernel.org/pub/scm/linux/kernel/git/stable/` — 直接访问Git仓库

**系统故障排除板块：**
- **StackExchange API**: `https://api.stackexchange.com/2.3/` — StackOverflow/SuperUser/AskUbuntu
- **Microsoft Q&A API**: `https://learn.microsoft.com/api/` — 官方问答平台
- **Apple Support RSS**: 各支持页面的RSS Feed
- **Reddit API**: `https://www.reddit.com/r/sysadmin/` — 系统管理员社区

### 5.3 爬虫友好度优化建议

1. **遵守robots.txt**: 所有爬虫必须首先检查目标网站的robots.txt文件
2. **使用User-Agent**: 设置有意义的User-Agent，包含项目名称和联系邮箱
3. **限速控制**: 对同一域名的请求间隔不低于2-5秒，避免触发反爬机制
4. **缓存策略**: 使用ETag/Last-Modified头实现增量更新，减少不必要的请求
5. **分布式爬取**: 使用Scrapy-Redis或类似方案实现多实例分布式爬取
6. **数据存储**: 推荐使用MongoDB或PostgreSQL存储爬取的结构化数据
7. **错误处理**: 实现指数退避重试机制，对HTTP 429/503进行优雅降级

### 5.4 中文资源爬取注意事项

| 网站 | 特殊处理 |
|------|---------|
| 看雪安全社区 | 需要登录才能查看完整内容，建议使用Cookie池 |
| 吾爱破解 | 有Cloudflare防护，需要绕过或人工干预 |
| V2EX | 提供API接口，建议优先使用API而非页面爬取 |
| 补天平台 | 部分漏洞详情需要权限，公开信息可正常爬取 |
| 天融信安全通告 | 以PDF格式发布，需要PDF解析 |

### 5.5 数据更新频率建议

| 数据类型 | 更新频率 | 数据源示例 |
|---------|---------|-----------|
| CVE漏洞库 | 每日 | NVD、OSV.dev、Vulners |
| 安全公告 | 每日 | MSRC、Red Hat RHSA、Apple Security |
| 威胁情报 | 每小时 | CISA KEV、GreyNoise、Recorded Future |
| 技术博客 | 每周 | BleepingComputer、Objective-See |
| 论坛问答 | 每日 | StackExchange、AskUbuntu |
| 硬件兼容性 | 每月 | Linux Hardware Database、Ubuntu Certified |


---

## 六、统计汇总

### 6.1 板块与操作系统分布

| 板块 | Windows | Linux | macOS | 跨平台/通用 | 小计 |
|------|---------|-------|-------|------------|------|

| 网络漏洞 | 9 | 16 | 11 | 27 | 63 |
| 系统漏洞 | 10 | 12 | 10 | 22 | 54 |
| 系统故障排除 | 15 | 21 | 21 | 12 | 69 |
| **总计** | **34** | **49** | **42** | **61** | **186** |

### 6.2 爬虫友好度分布

| 友好度等级 | 网站数量 | 占比 |
|-----------|---------|------|

| 高 | 95 | 51.1% |
| 中 | 85 | 45.7% |
| 低 | 5 | 2.7% |
| **总计** | **186** | **100%** |

### 6.3 数据来源分布

| 研究维度 | 描述 | 贡献网站数 |
|---------|------|-----------|
| Dim01 | 网络漏洞 - Windows | 23 |
| Dim02 | 网络漏洞 - Linux | 16 |
| Dim03 | 网络漏洞 - macOS | 12 |
| Dim04 | 系统漏洞 - Windows | 11 |
| Dim05 | 系统漏洞 - Linux | 11 |
| Dim06 | 系统漏洞 - macOS | 11 |
| Dim07 | 系统故障排除 - Windows | 19 |
| Dim08 | 系统故障排除 - Linux | 21 |
| Dim09 | 系统故障排除 - macOS | 20 |
| Dim10 | 跨平台通用数据库 | 15 |
| Dim11 | 中文本土资源 | 22 |
| Dim12 | 开源社区/论坛 | 11 |

> 注：部分网站在多个维度中重复出现，经过去重处理后最终保留186个独立网站。

### 6.4 质量筛选说明

本次整合过程中执行了以下质量筛选：

1. **去重处理**：识别并合并了在不同研究维度中重复出现的网站，确保每个URL仅出现一次
2. **来源验证**：剔除了已关闭、长期不更新或域名失效的网站
3. **爬虫友好度评估**：基于是否提供RSS/Feed/API、robots.txt策略、反爬机制强度等因素综合评估
4. **内容质量**：优先保留官方网站、知名安全厂商、活跃社区的内容来源
5. **时效性**：优先选择2024-2026年间仍在活跃更新的网站

### 6.5 使用建议

1. **优先级策略**：建议优先爬取标注"爬虫友好度高"的网站，这些网站提供API或结构化数据，爬取效率高且稳定
2. **增量更新**：对每日更新的网站（如NVD、安全公告）设置定时任务；对每周/每月更新的网站降低爬取频率
3. **中文资源**：Dim11的中文资源适合针对中国用户的补丁场景，建议与英文资源配合使用
4. **社区资源**：Dim12的论坛和Wiki类资源内容质量参差不齐，建议配合评分机制筛选高质量回答
5. **跨平台资源**：Dim10的通用数据库资源适合所有板块，建议作为基础数据源优先接入

---

*本报告由 patch-toolbox 项目自动生成，基于12个研究维度文件的交叉验证与整合。如有更新建议，请通过项目地址提交Issue。*
