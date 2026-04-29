# Contributing to Patch-Toolbox / 贡献指南

> **语言**: 中文 | English below

## 快速开始 / Quick Start

1. Fork 本仓库
2. 创建分支: `git checkout -b feature/your-feature`
3. 提交更改: `git commit -am 'Add: 新增内容'`
4. 推送分支: `git push origin feature/your-feature`
5. 提交 Pull Request

## 内容规范 / Content Standards

### 双语要求 / Bilingual Requirement

所有新增条目必须包含 **中文和英文** 内容：

```markdown
### 中文版 / Chinese Version

[中文内容]

### 英文版 / English Version

[English content]
```

### 术语规范 / Terminology

| 中文 | English | 备注 |
|------|---------|------|
| 安全漏洞 | Security Vulnerability | 正式用语 |
| 漏洞披露 | Vulnerability Disclosure | 行业术语 |
| 修复方案 | Remediation / Fix | 两者皆可 |
| 缓解措施 | Mitigation | 临时修复 |
| 影响版本 | Affected Versions | 固定搭配 |
| 参考来源 | References | 固定搭配 |

## 提交规范 / Commit Convention

```
Add: 新增 [分类] [CVE-ID/标题]
Update: 更新 [分类] [CVE-ID/标题]
Fix: 修正 [分类] [CVE-ID/标题] 的 [字段]
Docs: 更新文档/说明
```

## 安全注意事项 / Security Notes

- **禁止提交密钥**: API Key、Token、密码等通过环境变量注入
- **禁止泄露敏感信息**: 内部系统信息、个人隐私数据
- **链接验证**: 确保所有外部链接可访问

## 本地验证 / Local Verification

```bash
# 验证双语结构
python scripts/validate_bilingual.py

# 验证数据库同步
python scripts/verify_db_sync.py

# 验证链接可访问性（当前无专门脚本；新增外链时请手动验证）
```

## 联系方式 / Contact

- GitHub Issues: [提交问题](../../issues)
- Discussions: [参与讨论](../../discussions)

---

## English Version

### Quick Start

1. Fork this repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add: new content'`
4. Push branch: `git push origin feature/your-feature`
5. Submit a Pull Request

### Content Standards

#### Bilingual Requirement

All new entries must contain **Chinese and English** content:

```markdown
### 中文版 / Chinese Version

[Chinese content]

### 英文版 / English Version

[English content]
```

#### Terminology

| English | 中文 | Notes |
|---------|------|-------|
| Security Vulnerability | 安全漏洞 | Formal term |
| Vulnerability Disclosure | 漏洞披露 | Industry term |
| Remediation / Fix | 修复方案 | Either is acceptable |
| Mitigation | 缓解措施 | Temporary fix |
| Affected Versions | 影响版本 | Fixed phrase |
| References | 参考来源 | Fixed phrase |

### Commit Convention

```
Add: [category] [CVE-ID/title]
Update: [category] [CVE-ID/title]
Fix: [category] [CVE-ID/title] field
Docs: documentation update
```

### Security Notes

- **Do not commit secrets**: API keys, tokens, passwords via environment variables only
- **Do not leak sensitive info**: Internal system details, personal data
- **Link validation**: Ensure all external links are accessible

### Local Verification

```bash
# Validate bilingual structure
python scripts/validate_bilingual.py

# Verify database sync
python scripts/verify_db_sync.py

# External links: no dedicated script currently, validate manually when adding new links
```

### Contact

- GitHub Issues: [Submit issue](../../issues)
- Discussions: [Join discussion](../../discussions)

## License

By contributing, you agree to license your contributions under MIT License.
