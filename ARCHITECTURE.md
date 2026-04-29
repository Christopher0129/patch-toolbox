# patch-toolbox Architecture

## Overview

`patch-toolbox` is a public security knowledge repository.

Its public-facing responsibility is to provide:
- curated security and troubleshooting content
- SQLite datasets for programmatic use
- Markdown documents for direct reading
- lightweight repository-local validation/build helpers

This document describes the repository itself.
It does **not** define private automation, host-local paths, cron wiring, mirror publishing, or operations workflows.

---

## Repository Scope

The repository is organized around three content domains:
- `network-security/`
- `system-vulnerabilities/`
- `system-troubleshooting/`

Those domains are published in two parallel forms:
- **SQLite databases** in `db/`
- **Markdown documents** in the category directories

The goal is simple:
- humans can browse Markdown directly
- tools can query SQLite directly

---

## Top-Level Structure

```text
patch-toolbox/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── ARCHITECTURE.md
├── db/
│   ├── network-security.db
│   ├── system-vulnerabilities.db
│   └── system-troubleshooting.db
├── network-security/
│   └── index.md
├── system-vulnerabilities/
│   ├── index.md
│   ├── windows.md
│   ├── linux.md
│   └── macos.md
├── system-troubleshooting/
│   ├── index.md
│   ├── windows.md
│   ├── linux.md
│   └── macos.md
├── scripts/
│   ├── regenerate_md.py
│   ├── validate_structure.py
│   ├── validate_bilingual.py
│   ├── verify_db_sync.py
│   └── ...
└── .github/
    └── workflows/
        └── ci-check.yml
```

---

## Content Layers

### 1. SQLite layer

The `db/` directory stores the structured datasets.
These databases are the canonical machine-readable form used for querying, verification, and regeneration.

### 2. Markdown layer

The category directories provide the reader-facing form.
They preserve repository readability, Git diff visibility, and direct browsing on code hosting platforms.

### 3. Repository-local helper scripts

The `scripts/` directory contains helper scripts for tasks such as:
- Markdown regeneration
- structure validation
- bilingual format validation
- dataset consistency checks

These scripts support repository maintenance, but they are not the public architecture themselves.

---

## Category Model

### `network-security/`
General network and ecosystem security advisories, exploit references, and related security disclosures.

### `system-vulnerabilities/`
OS-level vulnerability content grouped by platform:
- Windows
- Linux
- macOS

### `system-troubleshooting/`
Operational troubleshooting knowledge grouped by platform:
- Windows
- Linux
- macOS

---

## Data and Document Relationship

The expected relationship is:

```text
SQLite data -> generated/maintained Markdown views -> repository readers/tools
```

In practice:
- SQLite stores structured entries
- Markdown exposes stable, readable category pages
- validation scripts help keep both representations aligned

---

## Documentation Conventions

The repository uses a bilingual structural style:
- headings and field labels are presented in Chinese / English form when appropriate
- source technical content may remain in its original language for accuracy

Examples include fields such as:
- `严重程度 / Severity`
- `漏洞描述 / Description`
- `缓解方案 / Mitigation`
- `参考链接 / References`

This keeps the repository readable for both Chinese-speaking and English-speaking readers without rewriting source technical details unnecessarily.

---

## What This Document Intentionally Excludes

The following are intentionally **out of scope** for this public architecture document:
- host-local absolute paths
- cron schedules and runner topology
- mirror publishing strategy between hosting platforms
- private deployment or operations notes
- local agent/session orchestration details
- internal review or maintenance playbooks

If such automation exists, it belongs to external or private operations material rather than the public repository definition.
