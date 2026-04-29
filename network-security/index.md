# 网络安全漏洞知识库 | Network Security Vulnerability Knowledge Base

> 本知识库汇总公开披露的网络安全漏洞信息，包含 CVE 编号、严重程度、漏洞描述及缓解方案。
> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> This knowledge base aggregates publicly disclosed network security vulnerabilities. Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.

**总计条目 / Total entries: 1120**

---

#### 1. CVE-1999-0095

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The debug command in Sendmail is enabled, allowing attackers to execute commands as root.

---

#### 2. CVE-1999-0082

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
CWD ~root command in ftpd allows root access.

---

#### 3. CVE-1999-1471

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in passwd in BSD based operating systems 4.3 and earlier allows local users to gain root privileges by specifying a long shell or GECOS field.

---

#### 4. CVE-1999-1122

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in restore in SunOS 4.0.3 and earlier allows local users to gain privileges.

---

#### 5. CVE-1999-1467

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in rcp on SunOS 4.0.x allows remote attackers from trusted hosts to execute arbitrary commands as root, possibly related to the configuration of the nobody user.

---

#### 6. CVE-1999-1506

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in SMI Sendmail 4.0 and earlier, on SunOS up to 4.0.3, allows remote attackers to access user bin.

---

#### 7. CVE-1999-0084

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
Certain NFS servers allow users to use mknod to gain privileges by creating a writable kmem device and setting the UID to 0.

---

#### 8. CVE-2000-0388

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in FreeBSD libmytinfo library allows local users to execute commands via a long TERMCAP environmental variable.

---

#### 9. CVE-1999-0209

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The SunView (SunTools) selection_svc facility allows remote users to read files.

---

#### 10. CVE-1999-1198

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
BuildDisk program on NeXT systems before 2.0 does not prompt users for the root password, which allows local users to gain root privileges.

---

#### 11. CVE-1999-1391

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in NeXT 1.0a and 1.0 with publicly accessible printers allows local users to gain privileges via a combination of the npd program and weak directory permissions.

---

#### 12. CVE-1999-1392

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in restore0.9 installation script in NeXT 1.0a and 1.0 allows local users to gain root privileges.

---

#### 13. CVE-1999-1057

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
VMS 4.0 through 5.3 allows local users to gain privileges via the ANALYZE/PROCESS_DUMP dcl command.

---

#### 14. CVE-1999-1554

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
/usr/sbin/Mail on SGI IRIX 3.3 and 3.3.1 does not properly set the group ID to the group ID of the user who started Mail, which allows local users to read the mail of other users.

---

#### 15. CVE-1999-1197

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
TIOCCONS in SunOS 4.1.1 does not properly check the permissions of a user who tries to redirect console output and input, which could allow a local user to gain privileges.

---

#### 16. CVE-1999-1115

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in the /etc/suid_exec program in HP Apollo Domain/OS sr10.2 and sr10.3 beta, related to the Korn Shell (ksh).

---

#### 17. CVE-1999-1258

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
rpc.pwdauthd in SunOS 4.1.1 and earlier does not properly prevent remote access to the daemon, which allows remote attackers to obtain sensitive system information.

---

#### 18. CVE-1999-1438

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in /bin/mail in SunOS 4.1.1 and earlier allows local users to gain root privileges via certain command line arguments.

---

#### 19. CVE-1999-1211

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in in.telnetd in SunOS 4.1.1 and earlier allows local users to gain root privileges.

---

#### 20. CVE-1999-1212

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in in.rlogind in SunOS 4.0.3 and 4.0.3c allows local users to gain root privileges.

---

#### 21. CVE-1999-1194

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
chroot in Digital Ultrix 4.1 and 4.0 is insecurely installed, which allows local users to gain privileges.

---

#### 22. CVE-1999-1193

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The "me" user in NeXT NeXTstep 2.1 and earlier has wheel group privileges, which could allow the me user to use the su command to become root.

---

#### 23. CVE-1999-1123

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The installation of Sun Source (sunsrc) tapes allows local users to gain root privileges via setuid root programs (1) makeinstall or (2) winstall.

---

#### 24. CVE-1999-1034

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in login in AT&T System V Release 4 allows local users to gain privileges.

---

#### 25. CVE-1999-1415

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in /usr/bin/mail in DEC ULTRIX before 4.2 allows local users to gain privileges.

---

#### 26. CVE-1999-1090

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default configuration of NCSA Telnet package for Macintosh and PC enables FTP, even though it does not include an "ftp=yes" line, which allows remote attackers to read and modify arbitrary files.

---

#### 27. CVE-1999-0498

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
TFTP is not running in a restricted directory, allowing a remote attacker to access sensitive information such as password files.

---

#### 28. CVE-1999-1468

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
rdist in various UNIX systems uses popen to execute sendmail, which allows local users to gain root privileges by modifying the IFS (Internal Field Separator) variable.

---

#### 29. CVE-1999-0167

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
In SunOS, NFS file handles could be guessed, giving unauthorized access to the exported file system.

---

#### 30. CVE-1999-1493

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in crp in Hewlett Packard Apollo Domain OS SR10 through SR10.3 allows remote attackers to gain root privileges via insecure system calls, (1) pad_$dm_cmd and (2) pad_$def_pfk().

---

#### 31. CVE-1999-1032

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in LAT/Telnet Gateway (lattelnet) on Ultrix 4.1 and 4.2 allows attackers to gain root privileges.

---

#### 32. CVE-1999-1059

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in rexec daemon (rexecd) in AT&T TCP/IP 4.0 for various SVR4 systems allows remote attackers to execute arbitrary commands.

---

#### 33. CVE-1999-0627

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
The rexd service is running, which uses weak authentication that can allow an attacker to execute commands.

---

#### 34. CVE-1999-1121

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configuration for UUCP in AIX before 3.2 allows local users to gain root privileges.

---

#### 35. CVE-1999-0117

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
AIX passwd allows local users to gain root access.

---

#### 36. CVE-1999-1119

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
FTP installation script anon.ftp in AIX insecurely configures anonymous FTP, which allows remote attackers to execute arbitrary commands.

---

#### 37. CVE-1999-1142

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
SunOS 4.1.2 and earlier allows local users to gain privileges via "LD_*" environmental variables to certain dynamically linked setuid or setgid programs such as (1) login, (2) su, or (3) sendmail, that change the real and effective user ids to the same user.

---

#### 38. CVE-1999-0168

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The portmapper may act as a proxy and redirect service requests from an attacker, making the request appear to come from the local host, possibly bypassing authentication that would otherwise have taken place.  For example, NFS file systems could be mounted through the portmapper despite export restrictions.

---

#### 39. CVE-1999-0214

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Denial of service by sending forged ICMP unreachable packets.

---

#### 40. CVE-1999-1396

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in integer multiplication emulation code on SPARC architectures for SunOS 4.1 through 4.1.2 allows local users to gain root access or cause a denial of service (crash).

---

#### 41. CVE-1999-1395

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in Monitor utility (SYS$SHARE:SPISHR.EXE) in VMS 5.0 through 5.4-2 allows local users to gain privileges.

---

#### 42. CVE-1999-1306

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Cisco IOS 9.1 and earlier does not properly handle extended IP access lists when the IP route cache is enabled and the "established" keyword is set, which could allow attackers to bypass filters.

---

#### 43. CVE-1999-1466

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in Cisco routers versions 8.2 through 9.1 allows remote attackers to bypass access control lists when extended IP access lists are used on certain interfaces, the IP route cache is enabled, and the access list uses the "established" keyword.

---

#### 44. CVE-1999-1021

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
NFS on SunOS 4.1 through 4.1.2 ignores the high order 16 bits in a 32 bit UID, which allows a local user to gain root access if the lower 16 bits are set to 0, as fixed by the NFS jumbo patch upgrade.

---

#### 45. CVE-1999-1056

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: CVE-1999-1395.  Reason: This candidate is a duplicate of CVE-1999-1395.  Notes: All CVE users should reference CVE-1999-1395 instead of this candidate.  All references and descriptions in this candidate have been removed to prevent accidental usage

---

#### 46. CVE-1999-0312

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
HP ypbind allows attackers with root privileges to modify NIS data.

---

#### 47. CVE-1999-1507

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Sun SunOS 4.1 through 4.1.3 allows local attackers to gain root access via insecure permissions on files and directories such as crash.

---

#### 48. CVE-1999-1218

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in finger in Commodore Amiga UNIX 2.1p2a and earlier allows local users to read arbitrary files.

---

#### 49. CVE-1999-1312

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in DEC OpenVMS VAX 5.5-2 through 5.0, and OpenVMS AXP 1.0, allows local users to gain system privileges.

---

#### 50. CVE-1999-1216

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Cisco routers 9.17 and earlier allow remote attackers to bypass security restrictions via certain IP source routed packets that should normally be denied using the "no ip source-route" command.

---

#### 51. GHSA-7jm2-g593-4qrc - OpenClaw: Agent gateway config mutations could change protected operator setting

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

The agent-facing `gateway config.patch` / `config.apply` guard did not cover several operator-trusted settings, including sandbox policy, plugin enablement, gateway auth/TLS, hook routing, MCP server configuration, SSRF policy, and filesystem hardening. A prompt-injected model with access to the owner-only gateway tool could persist changes to those settings.

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-7jm2-g593-4qrc for affected packages and patched versions.

---

#### 52. GHSA-qrp5-gfw2-gxv4 - OpenClaw: Bundled MCP/LSP tools could bypass configured tool policy

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Bundled MCP and LSP tools could be appended to the agent's effective tool set after the normal tool-policy pipeline had already filtered core tools. If an operator configured a restrictive policy, such as a tool profile, explicit allow/deny list, owner-only tool restriction, sandbox tool policy, or subagent tool policy, a bundled MCP/LSP tool could remain ava

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-qrp5-gfw2-gxv4 for affected packages and patched versions.

---

#### 53. GHSA-h2vw-ph2c-jvwf - OpenClaw: Workspace dotenv MiniMax host override could redirect credentialed req

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `>= 2026.4.5, < 2026.4.20`
- Patched version: `2026.4.20`

## Impact

A malicious workspace `.env` could set `MINIMAX_API_HOST` and redirect credentialed MiniMax requests to an attacker-controlled origin, exposing the MiniMax API key in the outbound `Authorization` header.

This requires running OpenClaw from an attacker-controlled workspace. Severity is medium.

## Fix

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-h2vw-ph2c-jvwf for affected packages and patched versions.

---

#### 54. GHSA-j4c5-89f5-f3pm - OpenClaw: Browser CDP profile creation skipped strict-mode SSRF checks

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Browser profile creation normalized `cdpUrl` values before persisting them, but did not apply the configured browser SSRF policy at creation time. In deployments that explicitly disabled private-network CDP targets, a stored profile could still point at a private-network or metadata endpoint and later be probed by normal profile status flows.

Default trusted

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-j4c5-89f5-f3pm for affected packages and patched versions.

---

#### 55. GHSA-xrq9-jm7v-g9h7 - OpenClaw: Paired-device pairing actions were not limited to the caller device

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

A paired device session with limited pairing scope could enumerate global pairing state and act on pairing requests that belonged to another device within the same gateway scope ceiling.

This is a same-gateway paired-device authorization bug, not a remote unauthenticated issue. Severity is low.

## Fix

Pairing management actions are now limited to the calle

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-xrq9-jm7v-g9h7 for affected packages and patched versions.

---

#### 56. GHSA-c4qg-j8jg-42q5 - OpenClaw: QQBot direct media upload skipped URL SSRF validation

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

The QQBot direct-upload media path could forward attacker-controlled image URLs without applying the SSRF validation used by the local download path. This could make configured QQBot media delivery request or relay URLs the operator did not intend to allow.

The affected path is limited to QQBot outbound media handling and does not expose arbitrary local file

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-c4qg-j8jg-42q5 for affected packages and patched versions.

---

#### 57. GHSA-mj59-h3q9-ghfh - OpenClaw: MCP stdio server env could load dangerous startup variables from works

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Workspace MCP stdio configuration could pass dangerous process-startup environment variables such as `NODE_OPTIONS`, `LD_PRELOAD`, or `BASH_ENV` to the spawned MCP server process. In a malicious workspace, this could make the MCP child load attacker-controlled code when the operator starts a session that uses that MCP server.

The impact is limited to local/w

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-mj59-h3q9-ghfh for affected packages and patched versions.

---

#### 58. GHSA-57r2-h2wj-g887 - OpenClaw: Isolated cron awareness events were recorded as trusted system events

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Output from webhook-triggered isolated cron agent runs could be queued into the main session awareness stream without `trusted: false`. That made the event render as a trusted `System:` event instead of an untrusted system event.

This is a trust-labeling issue that can strengthen prompt-injection impact, but it does not directly bypass gateway auth, tool pol

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-57r2-h2wj-g887 for affected packages and patched versions.

---

#### 59. GHSA-hxvm-xjvf-93f3 - OpenClaw: Workspace dotenv could override runtime-control environment variables

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Workspace `.env` loading did not reserve the `OPENCLAW_` runtime-control namespace broadly enough. A malicious workspace could set variables such as `OPENCLAW_GIT_DIR` before source-update or installer flows, potentially steering trusted OpenClaw runtime behavior.

This requires running OpenClaw from an attacker-controlled workspace. Severity is medium.

## F

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-hxvm-xjvf-93f3 for affected packages and patched versions.

---

#### 60. GHSA-72q8-jcmc-97wx - OpenClaw: Feishu card actions could misclassify DMs and skip dmPolicy

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Feishu card-action callbacks could synthesize a message event with DM conversations classified as group conversations. That skipped `dmPolicy` enforcement for card actions, so a sender in a Feishu DM could trigger card-action flows that should have been blocked by a restrictive DM policy.

The issue is limited to Feishu card-action handling. Severity is mediu

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-72q8-jcmc-97wx for affected packages and patched versions.

---

#### 61. GHSA-v8qf-fr4g-28p2 - OpenClaw: Assistant media route missed scope enforcement for trusted-proxy autho

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

The Control UI assistant-media route authenticated trusted-proxy callers but did not enforce the declared operator scopes for identity-bearing HTTP auth paths. A trusted-proxy caller without `operator.read` could access assistant-media files and metadata that were otherwise inside allowed media roots.

The route still required successful gateway authenticatio

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-v8qf-fr4g-28p2 for affected packages and patched versions.

---

#### 62. GHSA-2xcp-x87w-q377 - OpenClaw: Hook mapping templates could bypass hook session-key opt-in

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub Advisory] ## Affected Packages / Versions

- Package: `openclaw` (npm)
- Affected versions: `< 2026.4.20`
- Patched version: `2026.4.20`

## Impact

Templated hook mapping `sessionKey` values were treated differently from request-supplied session keys. A hook mapping could render an externally influenced session key even when `hooks.allowRequestSessionKey` was disabled, bypassing the intended routing opt-in for hook callers.

This affects webhook routing isolation. It does not grant host execution by itse

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-2xcp-x87w-q377 for affected packages and patched versions.

---

#### 63. GHSA-rpm5-65cw-6hj4 - GitPython has Command Injection via Git options bypass

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
[GitHub Advisory] ### Summary
GitPython blocks dangerous Git options such as `--upload-pack` and `--receive-pack` by default, but the equivalent Python kwargs `upload_pack` and `receive_pack` bypass that check. If an application passes attacker-controlled kwargs into `Repo.clone_from()`, `Remote.fetch()`, `Remote.pull()`, or `Remote.push()`, this leads to arbitrary command execution even when `allow_unsafe_options` is left at its default value of `False`.

### Details
GitPython explicitly treats helper-command op

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-rpm5-65cw-6hj4 for affected packages and patched versions.

---

#### 64. GHSA-x2qx-6953-8485 - GitPython: Unsafe option check validates multi_options before shlex.split transf

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
[GitHub Advisory] ### Summary

`_clone()` validates `multi_options` as the original list, then executes `shlex.split(" ".join(multi_options))`. A string like `"--branch main --config core.hooksPath=/x"` passes validation (starts with `--branch`), but after split becomes `["--branch", "main", "--config", "core.hooksPath=/x"]`. Git applies the config and executes attacker hooks during clone.

### Details

The vulnerable code is in [`git/repo/base.py` line 1383](https://github.com/gitpython-developers/GitPython/blob

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-x2qx-6953-8485 for affected packages and patched versions.

---

#### 65. GHSA-3gr9-485j-v4xf - Note Mark: Unauthenticated read of notes and assets in soft-deleted public books

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
[GitHub Advisory] ## Summary

After a note-mark owner soft-deletes a public book, its notes and uploaded assets stay readable at `/api/notes/{id}`, `/api/notes/{id}/content`, the slug URL, and the asset endpoints. Unauthenticated callers who hold the note ID or the slug path retain access. GORM's soft-delete scope does not reach the raw `JOIN books ...` clauses used by the note and asset queries.

## Details

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-3gr9-485j-v4xf for affected packages and patched versions.

---

#### 66. GHSA-pxf8-6wqm-r6hh - Note Mark: OIDC-registered users authenticated by submitting password "null"

**严重程度 / Severity**: CRITICAL | CVSS: 9.4

**漏洞描述 / Description**:
[GitHub Advisory] ## Summary

`IsPasswordMatch` in `backend/db/models.go` falls back to a hard-coded `bcrypt("null")` placeholder whenever a user has no stored password. OIDC-registered users are created with an empty password, so anyone who submits `password: "null"` to the internal login endpoint receives a valid session for that user. The bypass is unauthenticated and requires no user interaction.

## Details

`backend/db/models.go:36` defines the placeholder hash used by the timing-attack mitigation inside `I

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-pxf8-6wqm-r6hh for affected packages and patched versions.

---

#### 67. GHSA-gj49-89wh-h4gj - Cillium exposes sensitive information included in the cilium-bugtool debug archi

**严重程度 / Severity**: HIGH | CVSS: 7.9

**漏洞描述 / Description**:
[GitHub Advisory] ### Impact
The output of `cilium-bugtool` can contain sensitive data when the tool is run against Cilium deployments with WireGuard encryption enabled.

Users of [WireGuard Transparent Encryption](https://docs.cilium.io/en/stable/security/network/encryption-wireguard/) are affected.
The sensitive data is  the WireGuard private key (`cilium_wg0.key`) used for node-to-node encrypted communication

`cilium-bugtool` is a debugging tool that is typically invoked manually and does not run during the n

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-gj49-89wh-h4gj for affected packages and patched versions.

---

#### 68. GHSA-wg4g-395p-mqv3 - n8n-MCP: Sensitive MCP tool-call arguments logged on authenticated requests in H

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
[GitHub Advisory] ### Impact

When `n8n-mcp` runs in HTTP transport mode, authenticated MCP `tools/call` requests had their full arguments and JSON-RPC params written to server logs by the request dispatcher and several sibling code paths before any redaction. When a tool call carries credential material — most notably `n8n_manage_credentials.data` — the raw values can be persisted in logs.

In deployments where logs are collected, forwarded to external systems, or viewable outside the request trust boundary (sha

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-wg4g-395p-mqv3 for affected packages and patched versions.

---

#### 69. GHSA-74m3-9qvm-rp9h - zrok: WebDAV drive backend follows symlinks outside DriveRoot, enabling host fil

**严重程度 / Severity**: HIGH | CVSS: 8.7

**漏洞描述 / Description**:
[GitHub Advisory] **Summary**
The zrok WebDAV drive backend (davServer.Dir) restricts path traversal through lexical normalization but does not prevent symlink following. When a symbolic link inside the shared DriveRoot points to a location outside that root, remote WebDAV consumers can read files and—on shares without OS-level permission restrictions—write or overwrite files anywhere on the host filesystem accessible to the zrok process.

- Attack Vector: Network — exploitation is performed entirely over the Web

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-74m3-9qvm-rp9h for affected packages and patched versions.

---

#### 70. GHSA-3q34-rx83-r6mq - Heimdall has an authorization bypass via path normalization mismatch

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[GitHub Advisory] ### Summary

Heimdall performs rule matching on the raw (non-normalized) request path, while downstream components may normalize dot-segments according to [RFC 3986, Section 6.2.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-6.2.2.3). This discrepancy can result in heimdall authorizing a request for one path (e.g., `/user/../admin`, or URL-encoded variants such as `/user/%2e%2e/admin` or `/user/%2e%2e%2fadmin`. The latter would require the `allow_encoded_slashes` option to be set to `on` or

**缓解方案 / Mitigation**:
See GitHub Security Advisory GHSA-3q34-rx83-r6mq for affected packages and patched versions.

---

#### 71. [local] Throttlestop Kernel Driver - Kernel Out-of-Bounds Write Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Throttlestop Kernel Driver - Kernel Out-of-Bounds Write Privilege Escalation

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 72. [webapps] WordPress Plugin  5.2.0 - Broken Access Control

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WordPress Plugin  5.2.0 - Broken Access Control

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 73. [local] AVAST Antivirus 25.11 - Unquoted Service Path

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] AVAST Antivirus 25.11 - Unquoted Service Path

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 74. [local] NetBT e-Fatura - Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] NetBT e-Fatura - Privilege Escalation

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 75. [webapps] D-Link DIR-650IN - Authenticated Command Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] D-Link DIR-650IN - Authenticated Command Injection

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 76. [webapps] React Server 19.2.0 - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] React Server 19.2.0 - Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 77. [webapps] RomM  4.4.0 -  XSS_CSRF Chain

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] RomM  4.4.0 -  XSS_CSRF Chain

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 78. [webapps] Jumbo Website Manager  - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Jumbo Website Manager  - Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 79. [local] ZSH 5.9 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] ZSH 5.9 - RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 80. [webapps] FortiWeb  8.0.2 - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FortiWeb  8.0.2 - Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 81. [local] 7-Zip 24.00 - Directory Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] 7-Zip 24.00 - Directory Traversal

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 82. [webapps] xibocms 3.3.4 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] xibocms 3.3.4 - RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 83. [local] SQLite 3.50.1 - Heap Overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] SQLite 3.50.1 - Heap Overflow

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 84. [local] Microsoft MMC MSC EvilTwin - Local Admin Creation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Microsoft MMC MSC EvilTwin - Local Admin Creation

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 85. [webapps] Horilla v1.3 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Horilla v1.3 - RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 86. [local] is-localhost-ip 2.0.0 - SSRF

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] is-localhost-ip 2.0.0 - SSRF

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 87. [webapps] Fortinet FortiWeb v8.0.1 - Auth Bypass

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Fortinet FortiWeb v8.0.1 - Auth Bypass

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 88. [local] Windows Kernel - Elevation of Privilege

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Windows Kernel - Elevation of Privilege

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 89. [local] Desktop Window Manager Core Library 10.0.10240.0 - Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Desktop Window Manager Core Library 10.0.10240.0 - Privilege Escalation

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 90. [webapps] ASP.net  8.0.10 - Bypass

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] ASP.net  8.0.10 - Bypass

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 91. [webapps] Grafana 11.6.0 - SSRF

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Grafana 11.6.0 - SSRF

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 92. [webapps] Zhiyuan OA - arbitrary file upload leading

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Zhiyuan OA - arbitrary file upload leading

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 93. [webapps] WBCE CMS 1.6.4 - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WBCE CMS 1.6.4 - Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 94. [webapps] RiteCMS 3.1.0 - Authenticated Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] RiteCMS 3.1.0 - Authenticated Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 95. [webapps] WordPress  Madara - Local File Inclusion

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WordPress  Madara - Local File Inclusion

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 96. [webapps] WordPress Backup Migration 1.3.7 - Remote Command Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WordPress Backup Migration 1.3.7 - Remote Command Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 97. [webapps] mailcow 2025-01a - Host Header Password Reset Poisoning

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] mailcow 2025-01a - Host Header Password Reset Poisoning

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 98. [webapps] Easy File Sharing Web Server v7.2 - Buffer Overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Easy File Sharing Web Server v7.2 - Buffer Overflow

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 99. [webapps] WeGIA 3.5.0 - SQL Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WeGIA 3.5.0 - SQL Injection

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 100. [webapps] Boss Mini v1.4.0 - Local File Inclusion (LFI)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Boss Mini v1.4.0 - Local File Inclusion (LFI)

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 101. CVE-1999-1162

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Vulnerability in passwd in SCO UNIX 4.0 and earlier allows attackers to cause a denial of service by preventing users from being able to log into the system.

---

#### 102. CVE-1999-0124

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerabilities in UMN gopher and gopher+ versions 1.12 and 2.0x allow an intruder to read any files that can be accessed by the gopher daemon.

---

#### 103. CVE-1999-1215

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
LOGIN.EXE program in Novell Netware 4.0 and 4.01 temporarily writes user name and password information to disk, which could allow local users to gain privileges.

---

#### 104. CVE-1999-1138

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
SCO UNIX System V/386 Release 3.2, and other SCO products, installs the home directories (1) /tmp for the dos user, and (2) /usr/tmp for the asg user, which allows other users to gain access to those accounts since /tmp and /usr/tmp are world-writable.

---

#### 105. CVE-1999-1318

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
/usr/5bin/su in SunOS 4.1.3 and earlier uses a search path that includes the current working directory (.), which allows local users to gain privileges via Trojan horse programs.

---

#### 106. CVE-1999-0145

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Sendmail WIZ command enabled, allowing root access.

---

#### 107. CVE-1999-1137

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The permissions for the /dev/audio device on Solaris 2.2 and earlier, and SunOS 4.1.x, allow any local user to read from the device, which could be used by an attacker to monitor conversations happening near a machine that has a microphone.

---

#### 108. CVE-1999-0334

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
In Solaris 2.2 and 2.3, when fsck fails on startup, it allows a local user with physical access to obtain root access.

---

#### 109. CVE-1999-0181

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The wall daemon can be used for denial of service, social engineering attacks, or to execute remote commands.

---

#### 110. CVE-1999-1242

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in subnetconfig in HP-UX 9.01 and 9.0 allows local users to gain privileges.

---

#### 111. CVE-1999-0211

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Extra long export lists over 256 characters in some mount daemons allows NFS directories to be mounted by anyone.

---

#### 112. CVE-1999-0338

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
AIX Licensed Program Product performance tools allow local users to gain root access.

---

#### 113. CVE-1999-0120

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Sun/Solaris utmp file allows local users to gain root access if it is writable by users other than root.

---

#### 114. CVE-1999-1135

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in VUE 3.0 in HP 9.x allows local users to gain root privileges, as fixed by PHSS_4994 and PHSS_5438.

---

#### 115. CVE-1999-1146

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in Glance and gpm programs in GlancePlus for HP-UX 9.x and earlier allows local users to access arbitrary files and gain privileges.

---

#### 116. CVE-1999-1388

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
passwd in SunOS 4.1.x allows local users to overwrite arbitrary files via a symlink attack and the -F command line argument.

---

#### 117. CVE-1999-1134

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in Vue 3.0 in HP 9.x allows local users to gain root privileges, as fixed by PHSS_4038, PHSS_4055, and PHSS_4066.

---

#### 118. CVE-1999-0113

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Some implementations of rlogin allow root access if given a -froot parameter.

---

#### 119. CVE-1999-0423

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in hpterm on HP-UX 10.20 allows local users to gain additional privileges.

---

#### 120. CVE-1999-0337

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
AIX batch queue (bsh) allows local and remote users to gain additional privileges when network printing is enabled.

---

#### 121. CVE-1999-0207

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Remote attacker can execute commands through Majordomo using the Reply-To field and a "lists" command.

---

#### 122. CVE-1999-1239

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
HP-UX 9.x does not properly enable the Xauthority mechanism in certain conditions, which could allow local users to access the X display even when they have not explicitly been authorized to do so.

---

#### 123. CVE-1999-1552

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
dpsexec (DPS Server) when running under XDM in IBM AIX 3.2.5 and earlier does not properly check privileges, which allows local users to overwrite arbitrary files and gain privileges.

---

#### 124. CVE-1999-1494

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
colorview in Silicon Graphics IRIX 5.1, 5.2, and 6.0 allows local attackers to read arbitrary files via the -text argument.

---

#### 125. CVE-1999-1219

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in sgihelp in the SGI help system and print manager in IRIX 5.2 and earlier allows local users to gain root privileges, possibly through the clogin command.

---

#### 126. CVE-1999-1238

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in CORE-DIAG fileset in HP message catalog in HP-UX 9.05 and earlier allows local users to gain privileges.

---

#### 127. CVE-1999-1022

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
serial_ports administrative program in IRIX 4.x and 5.x trusts the user's PATH environmental variable to find and execute the ls program, which allows local users to gain root privileges via a Trojan horse ls program.

---

#### 128. CVE-1999-1310

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: CVE-1999-1022.  Reason: This candidate is a duplicate of CVE-1999-1022.  Notes: All CVE users should reference CVE-1999-1022 instead of this candidate.  All references and descriptions in this candidate have been removed to prevent accidental usage

---

#### 129. CVE-1999-1248

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in Support Watch (aka SupportWatch) in HP-UX 8.0 through 9.0 allows local users to gain privileges.

---

#### 130. CVE-1999-1302

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Unspecified vulnerability in pt_chmod in SCO UNIX 4.2 and earlier allows local users to gain root access.

---

#### 131. CVE-1999-1303

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in prwarn in SCO UNIX 4.2 and earlier allows local users to gain root access.

---

#### 132. CVE-1999-1304

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in login in SCO UNIX 4.2 and earlier allows local users to gain root access.

---

#### 133. CVE-1999-1305

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in "at" program in SCO UNIX 4.2 and earlier allows local users to gain root access.

---

#### 134. CVE-2000-0508

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
rpc.lockd in Red Hat Linux 6.1 and 6.2 allows remote attackers to cause a denial of service via a malformed request.

---

#### 135. CVE-1999-0077

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Predictable TCP sequence numbers allow spoofing.

---

#### 136. CVE-1999-0232

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in NCSA WebServer (version 1.5c) gives remote access.

---

#### 137. CVE-1999-0235

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in NCSA WebServer (1.4.1 and below) gives remote access.

---

#### 138. CVE-1999-0242

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Remote attackers can access mail files via POP3 in some Linux systems that are using shadow passwords.

---

#### 139. CVE-1999-1098

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerability in BSD Telnet client with encryption and Kerberos 4 authentication allows remote attackers to decrypt the session via sniffing.

---

#### 140. CVE-1999-1243

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
SGI Desktop Permissions Tool in IRIX 6.0.1 and earlier allows local users to modify permissions for arbitrary files and gain privileges.

---

#### 141. CVE-1999-0151

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The SATAN session key may be disclosed if the user points the web browser to other sites, possibly allowing root access.

---

#### 142. CVE-1999-1080

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
rmmount in SunOS 5.7 may mount file systems without the nosuid flag set, contrary to the documentation and its use in previous versions of SunOS, which could allow local users with physical access to gain root privileges by mounting a floppy or CD-ROM that contains a setuid program and running volcheck, when the file systems do not have the nosuid option specified in rmmount.conf.

---

#### 143. CVE-1999-0066

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
AnyForm CGI remote execution.

---

#### 144. CVE-1999-0161

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
In Cisco IOS 10.3, with the tacacs-ds or tacacs keyword, an extended IP access control list could bypass filtering.

---

#### 145. CVE-1999-0172

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
FormMail CGI program allows remote execution of commands.

---

#### 146. CVE-1999-0203

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
In Sendmail, attackers can gain root privileges via SMTP by specifying an improper "mail from" address and an invalid "rcpt to" address that would cause the mail to bounce to a program.

---

#### 147. CVE-1999-1580

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
SunOS sendmail 5.59 through 5.65 uses popen to process a forwarding host argument, which allows local users to gain root privileges by modifying the IFS (Internal Field Separator) variable and passing crafted values to the -oR option.

---

#### 148. CVE-1999-0164

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
A race condition in the Solaris ps command allows an attacker to overwrite critical files.

---

#### 149. CVE-1999-0155

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The ghostscript command with the -dSAFER option allows remote attackers to execute commands.

---

#### 150. CVE-1999-0245

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Some configurations of NIS+ in Linux allowed attackers to log in as the user "+".

---

#### 151. CVE-1999-0218

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Livingston portmaster machines could be rebooted via a series of commands.

---

#### 152. CVE-1999-0073

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Telnet allows a remote client to specify environment variables including LD_LIBRARY_PATH, allowing an attacker to bypass the normal system libraries and gain root access.

---

#### 153. CVE-1999-0099

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in syslog utility allows local or remote attackers to gain root privileges.

---

#### 154. CVE-1999-0241

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Guessable magic cookies in X Windows allows remote attackers to execute commands, e.g. through xterm.

---

#### 155. CVE-1999-0080

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Certain configurations of wu-ftp FTP server 2.4 use a _PATH_EXECPATH setting to a directory with dangerous commands, such as /bin, which allows remote authenticated users to gain root access via the "site exec" command.

---

#### 156. CVE-1999-0123

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
Race condition in Linux mailx command allows local users to read user files.

---

#### 157. CVE-1999-0316

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux splitvt command gives root access to local users.

---

#### 158. CVE-1999-0325

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
vhe_u_mnt program in HP-UX allows local users to create root files through symlinks.

---

#### 159. CVE-1999-0208

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
rpc.ypupdated (NIS) allows remote users to execute arbitrary commands.

---

#### 160. CVE-1999-1186

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
rxvt, when compiled with the PRINT_PIPE option in various Linux operating systems including Linux Slackware 3.0 and RedHat 2.1, allows local users to gain root privileges by specifying a malicious program using the -print-pipe command line parameter.

---

#### 161. CVE-1999-1319

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in object server program in SGI IRIX 5.2 through 6.1 allows remote attackers to gain root privileges in certain configurations.

---

#### 162. CVE-1999-1491

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
abuse.console in Red Hat 2.1 uses relative pathnames to find and execute the undrv program, which allows local users to execute arbitrary commands via a path that points to a Trojan horse program.

---

#### 163. CVE-1999-0103

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Echo and chargen, or other combinations of UDP services, can be used in tandem to flood the server, a.k.a. UDP bomb or UDP packet storm.

---

#### 164. CVE-1999-0143

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Kerberos 4 key servers allow a user to masquerade as another by breaking and generating session keys.

---

#### 165. CVE-1999-0233

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
IIS 1.0 allows users to execute arbitrary commands using .bat or .cmd files.

---

#### 166. CVE-1999-0142

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Java Applet Security Manager implementation in Netscape Navigator 2.0 and Java Developer's Kit 1.0 allows an applet to connect to arbitrary hosts.

---

#### 167. CVE-1999-0067

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
phf CGI program allows remote command execution through shell metacharacters.

---

#### 168. CVE-1999-0141

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
Java Bytecode Verifier allows malicious applets to execute arbitrary commands as the user of the applet.

---

#### 169. CVE-1999-0070

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
test-cgi program allows an attacker to list files on the server.

---

#### 170. CVE-1999-1103

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
dxconsole in DEC OSF/1 3.2C and earlier allows local users to read arbitrary files by specifying the file with the -file parameter.

---

#### 171. CVE-1999-0078

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
pcnfsd (aka rpc.pcnfsd) allows local users to change file permissions, or execute arbitrary commands through arguments in the RPC call.

---

#### 172. CVE-1999-0019

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Delete or create a file via rpc.statd, due to invalid information.

---

#### 173. CVE-1999-1314

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in union file system in FreeBSD 2.2 and earlier, and possibly other operating systems, allows local users to cause a denial of service (system reload) via a series of certain mount_union commands.

---

#### 174. CVE-1999-1313

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Manual page reader (man) in FreeBSD 2.2 and earlier allows local users to gain privileges via a sequence of commands.

---

#### 175. CVE-1999-0522

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The permissions for a system-critical NIS+ table (e.g. passwd) are inappropriate.

---

#### 176. CVE-1999-0509

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Perl, sh, csh, or other shell interpreters are installed in the cgi-bin directory on a WWW site, which allows remote attackers to execute arbitrary commands.

---

#### 177. CVE-1999-1205

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
nettune in HP-UX 10.01 and 10.00 is installed setuid root, which allows local users to cause a denial of service by modifying critical networking configuration information.

---

#### 178. CVE-1999-1253

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in a kernel error handling routine in SCO OpenServer 5.0.2 and earlier, and SCO Internet FastStart 1.0, allows local users to gain root privileges.

---

#### 179. CVE-1999-0138

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The suidperl and sperl program do not give up root privileges when changing UIDs back to the original users, allowing root access.

---

#### 180. CVE-1999-0175

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The convert.bas program in the Novell web server allows a remote attackers to read any file on the system that is internally accessible by the web server.

---

#### 181. CVE-1999-0022

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Local user gains root privileges via buffer overflow in rdist, via expstr() function.

---

#### 182. CVE-1999-0137

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The dip program on many Linux systems allows local users to gain root access via a buffer overflow.

---

#### 183. CVE-1999-1301

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A design flaw in the Z-Modem protocol allows the remote sender of a file to execute arbitrary programs on the client, as implemented in rz in the rzsz module of FreeBSD before 2.1.5, and possibly other programs.

---

#### 184. CVE-1999-1572

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
cpio on FreeBSD 2.1.0, Debian GNU/Linux 3.0, and possibly other operating systems, uses a 0 umask when creating files using the -O (archive) or -F options, which creates the files with mode 0666 and allows local users to read or overwrite those files.

---

#### 185. CVE-1999-0023

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Local user gains root privileges via buffer overflow in rdist, via lookup() function.

---

#### 186. CVE-1999-0135

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
admintool in Solaris allows a local user to write to arbitrary files and gain root access.

---

#### 187. CVE-1999-0136

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Kodak Color Management System (KCMS) on Solaris allows a local user to write to arbitrary files and gain root access.

---

#### 188. CVE-1999-0335

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-1999-0032. Reason: This candidate is a duplicate of CVE-1999-0032. Notes: All CVE users should reference CVE-1999-0032 instead of this candidate. All references and descriptions in this candidate have been removed to prevent accidental usage

---

#### 189. CVE-1999-1413

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Solaris 2.4 before kernel jumbo patch -35 allows set-gid programs to dump core even if the real user id is not in the set-gid group, which allows local users to overwrite or create files at higher privileges by causing a core dump, e.g. through dmesg.

---

#### 190. CVE-1999-0134

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
vold in Solaris 2.x allows local users to gain root access.

---

#### 191. CVE-1999-0133

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
fm_fls license server for Adobe Framemaker allows local users to overwrite arbitrary files and gain root access.

---

#### 192. CVE-1999-0132

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Expreserve, as used in vi and ex, allows local users to overwrite arbitrary files and gain root access.

---

#### 193. CVE-1999-0085

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in rwhod on AIX and other operating systems allows remote attackers to execute arbitrary code via a UDP packet with a long hostname.

---

#### 194. CVE-1999-1187

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Pine before version 3.94 allows local users to gain privileges via a symlink attack on a lockfile that is created when a user receives new mail.

---

#### 195. CVE-1999-1309

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Sendmail before 8.6.7 allows local users to gain root access via a large value in the debug (-d) command line option.

---

#### 196. CVE-1999-0324

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
ppl program in HP-UX allows local users to create root files through symlinks.

---

#### 197. CVE-1999-1252

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in a certain system call in SCO UnixWare 2.0.x and 2.1.0 allows local users to access arbitrary files and gain root privileges.

---

#### 198. CVE-1999-0131

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow and denial of service in Sendmail 8.7.5 and earlier through GECOS field gives root access to local users.

---

#### 199. CVE-1999-1383

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
(1) bash before 1.14.7, and (2) tcsh 6.05 allow local users to gain privileges via directory names that contain shell metacharacters (` back-tick), which can cause the commands enclosed in the directory name to be executed when the shell expands filenames using the \w option in the PS1 variable.

---

#### 200. CVE-1999-1295

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Transarc DCE Distributed File System (DFS) 1.1 for Solaris 2.4 and 2.5 does not properly initialize the grouplist for users who belong to a large number of groups, which could allow those users to gain access to resources that are protected by DFS.

---

#### 201. CVE-1999-0116

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service when an attacker sends many SYN packets to create multiple connections without ever sending an ACK to complete the connection, aka SYN flood.

---

#### 202. CVE-1999-0961

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
HPUX sysdiag allows local users to gain root privileges via a symlink attack during log file creation.

---

#### 203. CVE-1999-0206

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
MIME buffer overflow in Sendmail 8.8.0 and 8.8.1 gives root access.

---

#### 204. CVE-1999-0246

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
HP Remote Watch allows a remote user to gain root access.

---

#### 205. CVE-1999-0308

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
HP-UX gwind program allows users to modify arbitrary files.

---

#### 206. CVE-1999-0319

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in xmcd 2.1 allows local users to gain access through a user resource setting.

---

#### 207. CVE-1999-0234

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Bash treats any character with a value of 255 as a command separator.

---

#### 208. CVE-1999-0075

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
PASV core dump in wu-ftpd daemon when attacker uses a QUOTE PASV command after specifying a username and password.

---

#### 209. CVE-1999-0032

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in lpr, as used in BSD-based systems including Linux, allows local users to execute arbitrary code as root via a long -C (classification) command line option.

---

#### 210. CVE-1999-0277

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The WorkMan program can be used to overwrite any file to get root access.

---

#### 211. CVE-1999-1384

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Indigo Magic System Tour in the SGI system tour package (systour) for IRIX 5.x through 6.3 allows local users to gain root privileges via a Trojan horse .exitops program, which is called by the inst command that is executed by the RemoveSystemTour program.

---

#### 212. CVE-1999-0311

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
fpkg2swpk in HP-UX allows local users to gain root access.

---

#### 213. CVE-1999-0336

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in mstm in HP-UX allows local users to gain root access.

---

#### 214. CVE-1999-1161

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in ppl in HP-UX 10.x and earlier allows local users to gain root privileges by forcing ppl to core dump.

---

#### 215. CVE-1999-0130

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Local users can start Sendmail in daemon mode and gain root privileges.

---

#### 216. CVE-1999-1221

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dxchpwd in Digital Unix (OSF/1) 3.x allows local users to modify arbitrary files via a symlink attack on the dxchpwd.log file.

---

#### 217. CVE-1999-1099

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Kerberos 4 allows remote attackers to obtain sensitive information via a malformed UDP packet that generates an error string that inadvertently includes the realm name and the last user.

---

#### 218. CVE-1999-1240

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in cddbd CD database server allows remote attackers to execute arbitrary commands via a long log message.

---

#### 219. CVE-1999-0050

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in HP-UX newgrp program.

---

#### 220. CVE-1999-0044

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
fsdump command in IRIX allows local users to obtain root access by modifying sensitive files.

---

#### 221. CVE-1999-0129

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Sendmail allows local users to write to a file and gain group permissions via a .forward or :include: file.

---

#### 222. CVE-1999-0043

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Command execution via shell metachars in INN daemon (innd) 1.5 using "newgroup" and "rmgroup" control messages, and others.

---

#### 223. CVE-1999-1401

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in Desktop searchbook program in IRIX 5.0.x through 6.2 sets insecure permissions for certain user files (iconbook and searchbook).

---

#### 224. CVE-1999-0045

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
List of arbitrary files on Web host via nph-test-cgi script.

---

#### 225. CVE-1999-0096

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Sendmail decode alias can be used to overwrite sensitive files.

---

#### 226. CVE-1999-0101

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in AIX and Solaris "gethostbyname" library call allows root access through corrupt DNS host names.

---

#### 227. CVE-1999-0297

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Vixie Cron library up to version 3.0 allows local users to obtain root access via a long environmental variable.

---

#### 228. CVE-1999-1089

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in chfn command in HP-UX 9.X through 10.20 allows local users to gain privileges via a long command line argument.

---

#### 229. CVE-1999-0128

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Oversized ICMP ping packets can result in a denial of service, aka Ping o' Death.

---

#### 230. CVE-1999-0127

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
swinstall and swmodify commands in SD-UX package in HP-UX systems allow local users to create or overwrite arbitrary files to gain root access.

---

#### 231. CVE-1999-1385

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in ppp program in FreeBSD 2.1 and earlier allows local users to gain privileges via a long HOME environment variable.

---

#### 232. CVE-1999-1026

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
aspppd on Solaris 2.5 x86 allows local users to modify arbitrary files and gain root privileges via a symlink attack on the /tmp/.asppp.fifo file.

---

#### 233. CVE-1999-0260

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The jj CGI program allows command execution via shell metacharacters.

---

#### 234. CVE-1999-1251

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in direct audio user space code on HP-UX 10.20 and 10.10 allows local users to cause a denial of service.

---

#### 235. CVE-1999-0100

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Remote access in AIX innd 1.5.1, using control messages.

---

#### 236. CVE-1999-0163

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
In older versions of Sendmail, an attacker could use a pipe character to execute root commands.

---

#### 237. CVE-1999-0166

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
NFS allows users to use a "cd .." command to access other directories besides the exported file system.

---

#### 238. CVE-1999-0170

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Remote attackers can mount an NFS file system in Ultrix or OSF, even if it is denied on the access list.

---

#### 239. CVE-1999-0171

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Denial of service in syslog by sending it a large number of superfluous messages.

---

#### 240. CVE-1999-0173

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
FormMail CGI program can be used by web servers other than the host server that the program resides on.

---

#### 241. CVE-1999-0178

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the win-c-sample program (win-c-sample.exe) in the WebSite web server 1.1e allows remote attackers to execute arbitrary code via a long query string.

---

#### 242. CVE-1999-0179

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT crashes or locks up when a Samba client executes a "cd .." command on a file share.

---

#### 243. CVE-1999-0180

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
in.rshd allows users to login with a NULL username and execute commands.

---

#### 244. CVE-1999-0201

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
A quote cwd command on FTP servers can reveal the full path of the home directory of the "ftp" user.

---

#### 245. CVE-1999-0202

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The GNU tar command, when used in FTP sessions, may allow an attacker to execute arbitrary commands.

---

#### 246. CVE-1999-0204

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Sendmail 8.6.9 allows remote attackers to execute root commands, using ident.

---

#### 247. CVE-1999-0217

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Malicious option settings in UDP packets could force a reboot in SunOS 4.1.3 systems.

---

#### 248. CVE-1999-0236

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
ScriptAlias directory in NCSA and Apache httpd allowed attackers to read CGI programs.

---

#### 249. CVE-1999-0249

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Windows NT RSHSVC program allows remote users to execute arbitrary commands.

---

#### 250. CVE-1999-0251

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in talk program allows remote attackers to disrupt a user's display.

---

#### 251. CVE-1999-0252

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in listserv allows arbitrary command execution.

---

#### 252. CVE-1999-0253

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
IIS 3.0 with the iis-fix hotfix installed allows remote intruders to read source code for ASP programs by using a %2e instead of a . (dot) in the URL.

---

#### 253. CVE-1999-0265

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ICMP redirect messages may crash or lock up a host.

---

#### 254. CVE-1999-0274

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Windows NT DNS servers through malicious packet which contains a response to a query that wasn't made.

---

#### 255. CVE-1999-0345

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Jolt ICMP attack causes a denial of service in Windows 95 and Windows NT systems.

---

#### 256. CVE-1999-0496

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
A Windows NT 4.0 user can gain administrative rights by forcing NtOpenProcessToken to succeed regardless of the user's permissions, aka GetAdmin.

---

#### 257. CVE-1999-0499

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
NETBIOS share information may be published through SNMP registry keys in NT.

---

#### 258. CVE-1999-0503

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
A Windows NT local user or administrator account has a guessable password.

---

#### 259. CVE-1999-0504

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A Windows NT local user or administrator account has a default, null, blank, or missing password.

---

#### 260. CVE-1999-0510

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A router or firewall allows source routed packets from arbitrary hosts.

---

#### 261. CVE-1999-0511

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
IP forwarding is enabled on a machine which is not a router or firewall.

---

#### 262. CVE-1999-0517

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
An SNMP community name is the default (e.g. public), null, or missing.

---

#### 263. CVE-1999-0518

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A NETBIOS/SMB share password is guessable.

---

#### 264. CVE-1999-0519

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A NETBIOS/SMB share password is the default, null, or missing.

---

#### 265. CVE-1999-0521

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
An NIS domain name is easily guessable.

---

#### 266. CVE-1999-0525

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
IP traceroute is allowed from arbitrary hosts.

---

#### 267. CVE-1999-0534

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
A Windows NT user has inappropriate rights or privileges, e.g. Act as System, Add Workstation, Backup, Change System Time, Create Pagefile, Create Permanent Object, Create Token Name, Debug, Generate Security Audit, Increase Priority, Increase Quota, Load Driver, Lock Memory, Profile Single Process, Remote Shutdown, Replace Process Token, Restore, System Environment, Take Ownership, or Unsolicited Input.

---

#### 268. CVE-1999-0535

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT account policy for passwords has inappropriate, security-critical settings, e.g. for password length, password age, or uniqueness.

---

#### 269. CVE-1999-0550

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A router's routing tables can be obtained from arbitrary hosts.

---

#### 270. CVE-1999-0562

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The registry in Windows NT can be accessed remotely by users who are not administrators.

---

#### 271. CVE-1999-0572

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
.reg files are associated with the Windows NT registry editor (regedit), making the registry susceptible to Trojan Horse attacks.

---

#### 272. CVE-1999-0575

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A Windows NT system's user audit policy does not log an event success or failure, e.g. for Logon and Logoff, File and Object Access, Use of User Rights, User and Group Management, Security Policy Changes, Restart, Shutdown, and System, and Process Tracking.

---

#### 273. CVE-1999-0576

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A Windows NT system's file audit policy does not log an event success or failure for security-critical files or directories.

---

#### 274. CVE-1999-0582

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A Windows NT account policy has inappropriate, security-critical settings for lockout, e.g. lockout duration, lockout after bad logon attempts, etc.

---

#### 275. CVE-1999-0626

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
A version of rusers is running that exposes valid user information to any entity on the network.

---

#### 276. CVE-1999-1120

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
netprint in SGI IRIX 6.4 and earlier trusts the PATH environmental variable for finding and executing the disable program, which allows local users to gain privileges.

---

#### 277. CVE-1999-0051

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Arbitrary file creation and program execution using FLEXlm LicenseManager, from versions 4.0 to 5.0, in IRIX.

---

#### 278. CVE-1999-1249

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
movemail in HP-UX 10.20 has insecure permissions, which allows local users to gain privileges.

---

#### 279. CVE-1999-1145

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in Glance programs in GlancePlus for HP-UX 10.20 and earlier allows local users to access arbitrary files and gain privileges.

---

#### 280. CVE-1999-1311

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in dtlogin and dtsession in HP-UX 10.20 and 10.10 allows local users to bypass authentication and gain privileges.

---

#### 281. CVE-1999-0049

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Csetup under IRIX allows arbitrary file creation or overwriting.

---

#### 282. CVE-1999-1088

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in chsh command in HP-UX 9.X through 10.20 allows local users to gain privileges.

---

#### 283. CVE-1999-0081

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
wu-ftp allows files to be overwritten via the rnfr command.

---

#### 284. CVE-1999-0048

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Talkd, when given corrupt DNS information, can be used to execute arbitrary commands with root privileges.

---

#### 285. CVE-1999-0966

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Solaris getopt in libc allows local users to gain root privileges via a long argv[0].

---

#### 286. CVE-1999-0047

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
MIME conversion buffer overflow in sendmail versions 8.8.3 and 8.8.4.

---

#### 287. CVE-1999-1144

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Certain files in MPower in HP-UX 10.x are installed with insecure permissions, which allows local users to gain privileges.

---

#### 288. CVE-1999-0174

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
The view-source CGI program allows remote attackers to read arbitrary files via a .. (dot dot) attack.

---

#### 289. CVE-1999-0309

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
HP-UX vgdisplay program gives root access to local users.

---

#### 290. CVE-1999-0369

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Sun sdtcm_convert calendar utility for OpenWindows has a buffer overflow which can gain root access.

---

#### 291. CVE-1999-0959

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
IRIX startmidi program allows local users to modify arbitrary files via a symlink attack.

---

#### 292. CVE-1999-1160

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Vulnerability in ftpd/kftpd in HP-UX 10.x and 9.x allows local and possibly remote users to gain root privileges.

---

#### 293. CVE-1999-1299

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
rcp on various Linux systems including Red Hat 4.0 allows a "nobody" user or other user with UID of 65535 to overwrite arbitrary files, since 65535 is interpreted as -1 by chown and other system calls, which causes the calls to fail to modify the ownership of the file.

---

#### 294. CVE-1999-0298

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ypbind with -ypset and -ypsetme options activated in Linux Slackware and SunOS allows local and remote attackers to overwrite files via a .. (dot dot) attack.

---

#### 295. CVE-1999-0046

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow of rlogin program using TERM environmental variable.

---

#### 296. CVE-1999-0228

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in RPCSS.EXE program (RPC Locator) in Windows NT.

---

#### 297. CVE-1999-0109

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in ffbconfig in Solaris 2.5.1.

---

#### 298. CVE-1999-0041

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in NLS (Natural Language Service).

---

#### 299. CVE-1999-0868

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
ucbmail allows remote attackers to execute commands via shell metacharacters that are passed to it from INN.

---

#### 300. CVE-1999-0105

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
finger allows recursive searches by using a long string of @ symbols.

---

#### 301. CVE-1999-0106

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Finger redirection allows finger bombs.

---

#### 302. CVE-1999-0165

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
NFS cache poisoning.

---

#### 303. CVE-1999-0318

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in xmcd 2.0p12 allows local users to gain access through an environmental variable.

---

#### 304. CVE-1999-0612

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
A version of finger is running that exposes valid user information to any entity on the network.

---

#### 305. CVE-1999-1128

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Internet Explorer 3.01 on Windows 95 allows remote malicious web sites to execute arbitrary commands via a .isp file, which is automatically downloaded and executed without prompting the user.

---

#### 306. CVE-1999-1489

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in TestChip function in XFree86 SuperProbe in Slackware Linux 3.1 allows local users to gain root privileges via a long -nopr argument.

---

#### 307. CVE-1999-0299

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Buffer overflow in FreeBSD lpd through long DNS hostnames.

---

#### 308. CVE-1999-1408

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in AIX 4.1.4 and HP-UX 10.01 and 9.05 allows local users to cause a denial of service (crash) by using a socket to connect to a port on the localhost, calling shutdown to clear the socket, then using the same socket to connect to a different port on localhost.

---

#### 309. CVE-1999-1525

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Macromedia Shockwave before 6.0 allows a malicious webmaster to read a user's mail box and possibly access internal web servers via the GetNextText command on a Shockwave movie.

---

#### 310. CVE-1999-0280

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Remote command execution in Microsoft Internet Explorer using .lnk and .url files.

---

#### 311. CVE-1999-0292

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service through Winpopup using large user names.

---

#### 312. CVE-1999-0315

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Solaris fdformat command gives root access to local users.

---

#### 313. CVE-1999-1387

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 SP2 allows remote attackers to cause a denial of service (crash), possibly via malformed inputs or packets, such as those generated by a Linux smbmount command that was compiled on the Linux 2.0.29 kernel but executed on Linux 2.0.25.

---

#### 314. CVE-1999-0042

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in University of Washington's implementation of IMAP and POP servers.

---

#### 315. CVE-1999-1298

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sysinstall in FreeBSD 2.2.1 and earlier, when configuring anonymous FTP, creates the ftp user without a password and with /bin/date as the shell, which could allow attackers to gain access to certain system resources.

---

#### 316. CVE-1999-0058

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in PHP cgi program, php.cgi allows shell access.

---

#### 317. CVE-1999-0149

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The wrap CGI program in IRIX allows remote attackers to view arbitrary directory listings via a .. (dot dot) attack.

---

#### 318. CVE-1999-0038

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
Buffer overflow in xlock program allows local users to execute commands as root.

---

#### 319. CVE-1999-1296

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Kerberos IV compatibility libraries as used in Kerberos V allows local users to gain root privileges via a long line in a kerberos configuration file, which can be specified via the KRB_CONF environmental variable.

---

#### 320. CVE-1999-0040

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Xt library of X Windowing System allows local users to execute commands with root privileges.

---

#### 321. CVE-1999-0112

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in AIX dtterm program for the CDE.

---

#### 322. CVE-1999-1116

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in runpriv in Indigo Magic System Administration subsystem of SGI IRIX 6.3 and 6.4 allows local users to gain root privileges.

---

#### 323. CVE-1999-1380

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Symantec Norton Utilities 2.0 for Windows 95 marks the TUNEOCX.OCX ActiveX control as safe for scripting, which allows remote attackers to execute arbitrary commands via the run option through malicious web pages that are accessed by browsers such as Internet Explorer 3.0.

---

#### 324. CVE-1999-1267

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
KDE file manager (kfm) uses a TCP server for certain file operations, which allows remote attackers to modify arbitrary files by sending a copy command to the server.

---

#### 325. CVE-1999-0039

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
webdist CGI program (webdist.cgi) in SGI IRIX allows remote attackers to execute arbitrary commands via shell metacharacters in the distloc parameter.

---

#### 326. CVE-1999-1067

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
SGI MachineInfo CGI program, installed by default on some web servers, prints potentially sensitive system status information, which could be used by remote attackers for information gathering activities.

---

#### 327. CVE-1999-1398

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Vulnerability in xfsdump in SGI IRIX may allow local users to obtain root privileges via the bck.log log file, possibly via a symlink attack.

---

#### 328. CVE-1999-1461

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
inpview in InPerson on IRIX 5.3 through IRIX 6.5.10 trusts the PATH environmental variable to find and execute the ttsession program, which allows local users to obtain root access by modifying the PATH to point to a Trojan horse ttsession program.

---

#### 329. CVE-1999-1286

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
addnetpr in SGI IRIX 6.2 and earlier allows local users to modify arbitrary files and possibly gain root access via a symlink attack on a temporary file.

---

#### 330. CVE-1999-1410

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
addnetpr in IRIX 5.3 and 6.2 allows local users to overwrite arbitrary files and possibly gain root privileges via a symlink attack on the printers temporary file.

---

#### 331. CVE-1999-1158

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in (1) pluggable authentication module (PAM) on Solaris 2.5.1 and 2.5 and (2) unix_scheme in Solaris 2.4 and 2.3 allows local users to gain root privileges via programs that use these modules such as passwd, yppasswd, and nispasswd.

---

#### 332. CVE-1999-1184

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in Elm 2.4 and earlier allows local users to gain privileges via a long TERM environmental variable.

---

#### 333. CVE-1999-0962

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in HPUX passwd command allows local users to gain root privileges via a command line option.

---

#### 334. CVE-1999-1141

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Ascom Timeplex router allows remote attackers to obtain sensitive information or conduct unauthorized activities by entering debug mode through a sequence of CTRL-D characters.

---

#### 335. CVE-1999-1232

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Untrusted search path vulnerability in day5datacopier in SGI IRIX 6.2 allows local users to execute arbitrary commands via a modified PATH environment variable that points to a malicious cp program.

---

#### 336. CVE-1999-1402

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The access permissions for a UNIX domain socket are ignored in Solaris 2.x and SunOS 4.x, and other BSD-based operating systems before 4.4, which could allow local users to connect to the socket and possibly disrupt or control the operations of the program using that socket.

---

#### 337. CVE-1999-1191

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in chkey in Solaris 2.5.1 and earlier allows local users to gain root privileges via a long command line argument.

---

#### 338. CVE-1999-1449

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
SunOS 4.1.4 on a Sparc 20 machine allows local users to cause a denial of service (kernel panic) by reading from the /dev/tcx0 TCX device.

---

#### 339. CVE-1999-0037

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Arbitrary command execution via metamail package using message headers, when user processes attacker's message using metamail.

---

#### 340. CVE-1999-0259

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
cfingerd lists all users on a system via search.**@target.

---

#### 341. CVE-1999-0036

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
IRIX login program with a nonzero LOCKOUT parameter allows creation or damage to files.

---

#### 342. CVE-1999-0064

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in AIX lquerylv program gives root access to local users.

---

#### 343. CVE-1999-1143

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in runtime linker program rld in SGI IRIX 6.x and earlier allows local users to gain privileges via setuid and setgid programs.

---

#### 344. CVE-1999-0034

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in suidperl (sperl), Perl 4.x and 5.x.

---

#### 345. CVE-1999-0035

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
Race condition in signal handling routine in ftpd, allowing read/write arbitrary files.

---

#### 346. CVE-1999-0144

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Denial of service in Qmail by specifying a large number of recipients with the RCPT command.

---

#### 347. CVE-1999-0227

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Access violation in LSASS.EXE (LSA/LSARPC) program in Windows NT allows a denial of service.

---

#### 348. CVE-1999-0281

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in IIS using long URLs.

---

#### 349. CVE-1999-0799

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in bootpd 2.4.3 and earlier via a long boot file location.

---

#### 350. CVE-1999-0189

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Solaris rpcbind listens on a high numbered UDP port, which may not be filtered since the standard port number is 111.

---

#### 351. [webapps] motionEye 0.43.1b4 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] motionEye 0.43.1b4 - RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 352. [remote] Windows 10.0.17763.7009 - spoofing vulnerability

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Windows 10.0.17763.7009 - spoofing vulnerability

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 353. [local] glibc 2.38 - Buffer Overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] glibc 2.38 - Buffer Overflow

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 354. [remote] windows 10/11 - NTLM Hash Disclosure Spoofing

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] windows 10/11 - NTLM Hash Disclosure Spoofing

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 355. [remote] Redis 8.0.2 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Redis 8.0.2 - RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 356. [webapps] OctoPrint 1.11.2 - File Upload

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] OctoPrint 1.11.2 - File Upload

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 357. [remote] Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 358. [webapps] aiohttp 3.9.1 - directory traversal PoC

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] aiohttp 3.9.1 - directory traversal PoC

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 359. [webapps] FortiWeb Fabric Connector 7.6.x - SQL Injection to Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FortiWeb Fabric Connector 7.6.x - SQL Injection to Remote Code Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 360. [local] Docker Desktop 4.44.3 - Unauthenticated  API Exposure

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Docker Desktop 4.44.3 - Unauthenticated  API Exposure

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 361. [webapps] Piranha CMS 12.0 - Stored XSS in Text Block

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Piranha CMS 12.0 - Stored XSS in Text Block

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 362. [webapps] RPi-Jukebox-RFID 2.8.0 - Stored Cross-Site Scripting (XSS)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] RPi-Jukebox-RFID 2.8.0 - Stored Cross-Site Scripting (XSS)

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 363. [hardware] D-Link DIR-825 Rev.B 2.10 - Stack Buffer Overflow (DoS)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] D-Link DIR-825 Rev.B 2.10 - Stack Buffer Overflow (DoS)

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 364. [webapps] RPi-Jukebox-RFID 2.8.0 - Remote Command Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] RPi-Jukebox-RFID 2.8.0 - Remote Command Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 365. [webapps] Siklu EtherHaul Series EH-8010 - Arbitrary File Upload

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Siklu EtherHaul Series EH-8010 - Arbitrary File Upload

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 366. [webapps] Siklu EtherHaul Series EH-8010 - Remote Command Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Siklu EtherHaul Series EH-8010 - Remote Command Execution

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 367. [webapps] WordPress Quiz Maker 6.7.0.56 - SQL Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] WordPress Quiz Maker 6.7.0.56 - SQL Injection

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 368. [webapps] Chained Quiz  1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Chained Quiz  1.3.5 - Unauthenticated Insecure Direct Object Reference via Cookie

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 369. [webapps] FreeBSD rtsold 15.x - Remote Code Execution via DNSSL

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FreeBSD rtsold 15.x - Remote Code Execution via DNSSL

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 370. [webapps] Summar Employee Portal  3.98.0 - Authenticated SQL Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Summar Employee Portal  3.98.0 - Authenticated SQL Injection

**缓解方案 / Mitigation**:
Review and apply vendor patch immediately. Verify exploit applicability in your environment.

---

#### 371. CVE-2025-29635 - D-Link DIR-823X Command Injection Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: D-Link, Product: DIR-823X. D-Link DIR-823X Command Injection Vulnerability. Due date: 2026-05-08.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-08. CISA directive enforcement required.

---

#### 372. CVE-2024-7399 - Samsung MagicINFO 9 Server Path Traversal Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Samsung, Product: MagicINFO 9 Server. Samsung MagicINFO 9 Server Path Traversal Vulnerability. Due date: 2026-05-08.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-08. CISA directive enforcement required.

---

#### 373. CVE-2024-57728 - SimpleHelp Path Traversal Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: SimpleHelp , Product: SimpleHelp. SimpleHelp Path Traversal Vulnerability. Due date: 2026-05-08.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-08. CISA directive enforcement required.

---

#### 374. CVE-2024-57726 - SimpleHelp Missing Authorization Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: SimpleHelp , Product: SimpleHelp. SimpleHelp Missing Authorization Vulnerability. Due date: 2026-05-08.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-08. CISA directive enforcement required.

---

#### 375. CVE-2026-39987 - Marimo Remote Code Execution Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Marimo, Product: Marimo. Marimo Remote Code Execution Vulnerability. Due date: 2026-05-07.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-07. CISA directive enforcement required.

---

#### 376. CVE-2026-33825 - Microsoft Defender Insufficient Granularity of Access Control Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Defender. Microsoft Defender Insufficient Granularity of Access Control Vulnerability. Due date: 2026-05-06.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-06. CISA directive enforcement required.

---

#### 377. CVE-2026-20122 - Cisco Catalyst SD-WAN Manager Incorrect Use of Privileged APIs Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Cisco, Product: Catalyst SD-WAN Manger. Cisco Catalyst SD-WAN Manager Incorrect Use of Privileged APIs Vulnerability. Due date: 2026-04-23.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-23. CISA directive enforcement required.

---

#### 378. CVE-2026-20133 - Cisco Catalyst SD-WAN Manager Exposure of Sensitive Information to an Unauthorized Actor Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Cisco, Product: Catalyst SD-WAN Manager. Cisco Catalyst SD-WAN Manager Exposure of Sensitive Information to an Unauthorized Actor Vulnerability. Due date: 2026-04-23.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-23. CISA directive enforcement required.

---

#### 379. CVE-2025-2749 - Kentico Xperience Path Traversal Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Kentico, Product: Kentico Xperience. Kentico Xperience Path Traversal Vulnerability. Due date: 2026-05-04.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-04. CISA directive enforcement required.

---

#### 380. CVE-2023-27351 - PaperCut NG/MF Improper Authentication Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: PaperCut, Product: NG/MF. PaperCut NG/MF Improper Authentication Vulnerability. Due date: 2026-05-04.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-04. CISA directive enforcement required.

---

#### 381. CVE-2025-48700 - Synacor Zimbra Collaboration Suite (ZCS) Cross-site Scripting Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Synacor, Product: Zimbra Collaboration Suite (ZCS). Synacor Zimbra Collaboration Suite (ZCS) Cross-site Scripting Vulnerability. Due date: 2026-04-23.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-23. CISA directive enforcement required.

---

#### 382. CVE-2026-20128 - Cisco Catalyst SD-WAN Manager Storing Passwords in a Recoverable Format Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Cisco, Product: Catalyst SD-WAN Manager. Cisco Catalyst SD-WAN Manager Storing Passwords in a Recoverable Format Vulnerability. Due date: 2026-04-23.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-23. CISA directive enforcement required.

---

#### 383. CVE-2025-32975 - Quest KACE Systems Management Appliance (SMA) Improper Authentication Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Quest, Product: KACE Systems Management Appliance (SMA). Quest KACE Systems Management Appliance (SMA) Improper Authentication Vulnerability. Due date: 2026-05-04.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-04. CISA directive enforcement required.

---

#### 384. CVE-2024-27199 - JetBrains TeamCity Relative Path Traversal Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: JetBrains, Product: TeamCity. JetBrains TeamCity Relative Path Traversal Vulnerability. Due date: 2026-05-04.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-05-04. CISA directive enforcement required.

---

#### 385. CVE-2026-34197 - Apache ActiveMQ Improper Input Validation Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Apache, Product: ActiveMQ. Apache ActiveMQ Improper Input Validation Vulnerability. Due date: 2026-04-30.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-30. CISA directive enforcement required.

---

#### 386. CVE-2009-0238 - Microsoft Office Remote Code Execution

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Office. Microsoft Office Remote Code Execution. Due date: 2026-04-28.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-28. CISA directive enforcement required.

---

#### 387. CVE-2026-32201 - Microsoft SharePoint Server Improper Input Validation Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: SharePoint Server. Microsoft SharePoint Server Improper Input Validation Vulnerability. Due date: 2026-04-28.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-28. CISA directive enforcement required.

---

#### 388. CVE-2012-1854 - Microsoft Visual Basic for Applications Insecure Library Loading Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Visual Basic for Applications (VBA). Microsoft Visual Basic for Applications Insecure Library Loading Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 389. CVE-2025-60710 - Microsoft Windows Link Following Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Windows. Microsoft Windows Link Following Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 390. CVE-2023-21529 - Microsoft Exchange Server Deserialization of Untrusted Data Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Exchange Server. Microsoft Exchange Server Deserialization of Untrusted Data Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 391. CVE-2023-36424 - Microsoft Windows Out-of-Bounds Read Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Microsoft, Product: Windows. Microsoft Windows Out-of-Bounds Read Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 392. CVE-2020-9715 - Adobe Acrobat Use-After-Free Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Adobe, Product: Acrobat. Adobe Acrobat Use-After-Free Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 393. CVE-2026-21643 - Fortinet FortiClient EMS SQL Injection Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Fortinet, Product: FortiClient EMS. Fortinet FortiClient EMS SQL Injection Vulnerability. Due date: 2026-04-16.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-16. CISA directive enforcement required.

---

#### 394. CVE-2026-34621 - Adobe Acrobat and Reader Prototype Pollution Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Adobe, Product: Acrobat and Reader. Adobe Acrobat and Reader Prototype Pollution Vulnerability. Due date: 2026-04-27.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-27. CISA directive enforcement required.

---

#### 395. CVE-2026-1340 - Ivanti Endpoint Manager Mobile (EPMM) Code Injection Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Ivanti, Product: Endpoint Manager Mobile (EPMM). Ivanti Endpoint Manager Mobile (EPMM) Code Injection Vulnerability. Due date: 2026-04-11.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-11. CISA directive enforcement required.

---

#### 396. CVE-2026-35616 - Fortinet FortiClient EMS Improper Access Control Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Fortinet, Product: FortiClient EMS. Fortinet FortiClient EMS Improper Access Control Vulnerability. Due date: 2026-04-09.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-09. CISA directive enforcement required.

---

#### 397. CVE-2026-3502 - TrueConf Client Download of Code Without Integrity Check Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: TrueConf, Product: Client. TrueConf Client Download of Code Without Integrity Check Vulnerability. Due date: 2026-04-16.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-16. CISA directive enforcement required.

---

#### 398. CVE-2026-5281 - Google Dawn Use-After-Free Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Google, Product: Dawn. Google Dawn Use-After-Free Vulnerability. Due date: 2026-04-15.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-15. CISA directive enforcement required.

---

#### 399. CVE-2026-3055 - Citrix NetScaler Out-of-Bounds Read Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: Citrix, Product: NetScaler. Citrix NetScaler Out-of-Bounds Read Vulnerability. Due date: 2026-04-02.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-04-02. CISA directive enforcement required.

---

#### 400. CVE-2025-53521 - F5 BIG-IP Stack-Based Buffer Overflow Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA KEV] Vendor: F5, Product: BIG-IP. F5 BIG-IP Stack-Based Buffer Overflow Vulnerability. Due date: 2026-03-30.

**缓解方案 / Mitigation**:
Apply vendor patch before 2026-03-30. CISA directive enforcement required.

---

#### 401. [安全客] 科技云报到：当AI闯入特教行业，一场颠覆变革正在发生！

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 402. [安全客] 科技云报到：AI云，逻辑变了吗？

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 403. [安全客] 工程化实战思维在红队技战术中的应用

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 404. [安全客] 鸿蒙NEXT应用一键加固——AI Agent助力安全开发

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 405. [安全客] 科技云报到：AI算力革命，终结云计算20年降价史

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 406. [安全客] 科技云报到：“龙虾”入笼：为何金融行业不敢“养”？

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 407. [安全客] 科技云报到：“龙虾”OpenClaw狂欢之下，需要一针清醒剂

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 408. [安全客] 瑞数信息入选IDC两大AI安全报告，防御OpenClaw小龙虾裸奔危机

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 409. [安全客] 2026首届汽车安全白帽黑客大会圆满收官，共筑车联网安全新生态

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 410. [安全客] Ally WordPress插件高危SQL注入漏洞 威胁40万个网站

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 411. [安全客] OpenAI战略调整Sora视频AI将直接接入ChatGPT

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 412. [安全客] HPE发布Aruba OS高危漏洞预警 可未授权重置密码

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 413. [安全客] 能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 414. [安全客] GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 415. [安全客] Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation steps and vendor patches.

---

#### 416. [看雪] Google DeepMind：AI 智能体陷阱

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Matija Franklin, Nenad Tomašev等 译者：知道创宇404实验室翻译组 原文链接：https://blog.qiaomu.ai/api/images/document/2026/04/603f0cae8cd8ab94-ai-agent-trap.pdf 摘要 自主AI智能体日益在网络中自主行动，它们面临一种全新挑战：信息环境本身。由此产生了一个关键安全漏洞，我们称之...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 417. [看雪] 合法终端管理软件遭滥用：疑似银狐攻击事件分析与溯源

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：知道创宇高级威胁情报团队 一、事件概述 近期，我们在客户现场应急响应中排查到一起新型攻击事件。攻击者伪造常用工具安装包诱导执行，随即部署一款带有合法数字签名的终端管理软件。经技术溯源确认，该程序具备主机信息收集、远程控制等完整恶意能力，其 C2 基础设施与 “银狐” 高度关联。由于合法数字签名的天然 “免杀” 特性，该恶意程序可轻易绕过主流杀毒软件检测，实现隐蔽入侵与长期控制。 银狐简介 银...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 418. [看雪] SkillTrojan：针对基于技能的智能体系统的后门攻击

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Yunhao Feng, Yifan Ding, Yingshui Tan等 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2604.06811v1/https://arxiv.org/html/2604.06811v1 摘要 基于技能的智能体系统通过组合可复用技能完成复杂任务，在提升模块化与可扩展性的同时，引入了尚未被充分研究的安全攻击面。本文提...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 419. [看雪] GUARD‑SLM：面向小语言模型、基于令牌激活的越狱攻击防御方法

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Md. Jueal Mia1, Joaquin Molto1, Yanzhao Wu1, M. Hadi Amini 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2603.28817v1/https://arxiv.org/html/2603.28817v1 摘要 小语言模型（SLM）正成为大语言模型（LLM）高效且经济可行的替代方案，在计算成本...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 420. [看雪] 静默颠覆：通过卫星系统供应链植入物实施的传感器欺骗攻击

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Jack Vanlyssel, Gruia-Catalin Roman, Afsah Anwar 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2603.10388v1/https://arxiv.org/html/2603.10388v1 摘要 欺骗攻击是地面系统最具破坏性的网络威胁之一，而在太空中这类威胁愈发危险——卫星难以在轨维修，且运营方依...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 421. [看雪] 增强网络入侵检测系统：一种抵御对抗攻击的多层集成方法

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Nasim Soltani, Shayan Nejadshamsi等 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2603.10413v1/https://arxiv.org/html/2603.10413v1 摘要 对抗样本会对机器学习（ML）算法构成严重威胁。若被用于操控基于机器学习的网络入侵检测系统（NIDS）行为，将危及网络安全。本研究旨...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 422. [看雪] CUDA Agent：面向高性能 CUDA 内核生成的大规模智能体强化学习

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Weinan Dai, Hanlin Wu, Qiying Yu等 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2602.24286v1/https://arxiv.org/html/2602.24286v1 摘要 GPU内核优化是现代深度学习的基础，但仍是一项高度专业化的任务，需要深厚的硬件专业知识。尽管大语言模型（LLM）在通用编程任务中表现...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 423. [看雪] Unmasking SilverFox’s New Trends: Decoding Evasion Tactics, Domain Impersonation, and Mass-Generated Fake Software

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
Author: Knownsec 404 Advanced Threat Intelligence Team I. Introduction SilverFox has become one of the most active cyber threats in recent years, targeting managerial and finance staff in organization...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 424. [看雪] 基于图像的提示注入：通过视觉嵌入的对抗性指令劫持多模态大语言模型

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Neha Nagaraja, Lan Zhang, Zhilong Wang 译者：知道创宇404实验室翻译组 原文链接：https://arxiv.org/html/2603.03637v1/https://arxiv.org/html/2603.03637v1 摘要：多模态大语言模型（MLLMs）融合视觉与文本能力赋能各类应用，但这种融合也引入了新的安全漏洞。本文研究基于图像的提示注入（...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 425. [看雪] 虚假 OpenClaw 安装程序如何传播 GhostSocks 恶意软件

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
作者：Jai Minton, Ryan Dowd 原文链接：https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer/https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer 摘要 信息窃取型恶意软件是针对面向公众系统发起严重攻击的初始访问...

**缓解方案 / Mitigation**:
Review technical analysis and apply vendor patches accordingly.

---

#### 426. [先知] 用魔法打败魔法：自动化越狱提示词的生成

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
自动化越狱提示词的生成

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 427. [先知] qemu虚拟化逃逸

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
第一次做这种类型的，大体记录一下过程

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 428. [先知] 2025ccb决赛interpreter

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
一个自定义的序列化的题目

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 429. [先知] 在野利用CVE-2026-34621漏洞PDF样本深度分析

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
模拟构建漏洞 PDF 响应载荷后发现，该载荷可异常驻留并嵌入 Adobe Acrobat Reader 内部，即便关闭 PDF、重启软件乃至操作系统，仍能持续触发恶意代码执行。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 430. [先知] 2025ciscn决赛ez_orw

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
这个题目考了花指令，魔改rc4，protobuf，纯字符shellcode，考的很多，这里借此简单的总结一下各个部分

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 431. [先知] 2026软件安全赛半决赛PWN Robo_admin WP fix&break

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
2026软件安全赛半决赛PWN Robo_admin WP fix&break

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 432. [先知] 软件系统安全赛2026分区赛 Web NodeJs

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
该文章介绍了一道 Node.js CTF 题目的解题思路：攻击者首先利用 /changepassword 接口的 merge() 函数原型链污染漏洞，注入 isAdmin: true 提权为管理员；随后通过 CVE-2026-22709 绕过 vm2 沙箱执行任意命令；最后利用 root 权限的 /backup.sh 定时脚本，将 /flag 内容写入静态目录实现读取。核心链：原型污染提权 → v

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 433. [先知] 记edusrc的几个未授权案例的挖掘

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
在遇到vue框架的时候,使用相关插件进行接口相关的测试，往往更容易找到突破口。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 434. [先知] PWN核心利用手法归纳总结

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
结合简单模型实验，直指漏洞利用

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 435. [先知] CVE-2026-1207: Django raster lookups on PostGIS SQL注入漏洞

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
Django 框架在使用 PostGIS 查询地理栅格（raster）数据时，若将未经验证的用户输入直接作为 band index（波段索引）参数，会引发 SQL 注入

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

---

#### 436. [嘶吼] 纵横网络靶场社区正式发布 以虚实融合技术构建工业信息安全实战生态

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
当前，工业互联网深度融合发展，关键信息基础设施安全防护需求持续攀升，实战型工业信息安全人才短缺、训练场景稀缺、理论与实践脱节等制约行业发展的核心痛点日益凸显。在此背景下，烽台科技打造的聚焦工业信息安全人才培养与生态共建的纵横网络靶场社区正式发布。该平台依托烽台科技十余年工业靶场技术沉淀，以“虚实融合”技术为核心，整合AI智能体、数字孪生等前沿能力，旨在打造工业安全领域“理论+实战+生态”三位一体的服务体系，为高校、企业、科研院所提供专业化的工业安全实训与技术交流空间。从“竞赛工具”到“生态平台”：网络靶场社区的迭代之路回溯烽台科技网络靶场社区的发展历程，其起点可追溯至2015年——公司成立后其核心产品便是工控网络靶场，由此开启了工业安全领域的深耕之路。早期社区更像“竞赛工具”，聚焦赛事聚人气，而此次全新发布的纵横网络靶场社区则进行了针对性升级：不仅保留竞赛模块，还新增实训专区，计划陆续开放

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 437. [嘶吼] 梆梆安全发布《2026年Q1移动应用安全风险报告》：超八成APP存隐私违规，数据境外外发风险需高度警惕

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
梆梆安全发布《2026年Q1移动应用安全风险报告》。本报告基于梆梆安全移动应用监管平台在2026年一季度的威胁监测数据与深度安全分析成果，系统梳理当前国内移动应用面临的新型攻击技术演进与安全趋势变化，聚焦盗版仿冒、境外数据传输、高危漏洞、个人隐私违规等多个维度，为移动应用安全建设工作提供参考与实践指引。
当前，我国数字经济与实体经济融合持续深入，移动互联网已演进为支撑社会数字化转型的关键基础设施。根据中国互联网络信息中心（CNNIC）第57次《中国互联网络发展状况统计报告》，截至2025年12月，我国网民规模达11.25亿，互联网普及率突破80%，其中手机网民规模达11.21亿，占比高达99.6%，移动终端在数字接入生态中的核心地位进一步巩固。
与此同时，用户对移动应用的依赖程度持续加深。数据显示，我国网民人均每周上网时长已达32.5小时，人均使用APP数量接近30款，移动互联网接入流量全

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 438. [嘶吼] 公安部通报37款违规应用，电商类占比超七成，小程序不再是 “法外之地”

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
依据《网络安全法》《个人信息保护法》等法律法规，经公安部计算机信息系统安全产品质量监督检验中心检测，37款移动应用存在违法违规收集使用个人信息情况，具体通报如下：1、未公开收集使用规则。涉及21款移动应用如下：《奇峰商城》（支付宝小程序）、《聚优商城》（微信小程序）、《亿秀分期商城》（支付宝小程序）、《鲜范商城》（微信小程序）、《京机数码手机商城》（支付宝小程序）、《创维官方商城》（支付宝小程序）、《万事商城》（支付宝小程序）、《尚至然商城》（支付宝小程序）、《知墨商城》（支付宝小程序）、《领充充电桩商城》（支付宝小程序）、《世有品商城》（支付宝小程序）、《阿京妈会员》（微信小程序）、《仲盛世界SKYMALL》（支付宝小程序）、《衣恋集团商城》（微信小程序）、《快贷分期》（版本4.0.1，应用宝）、《百师商城》（微信小程序）、《松下商城》（微信小程序）、《意尔康官方商城》（微信小程序）、《

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 439. [嘶吼] Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
最新发现，企业级安全文件传输解决方案 Progress ShareFile 存在两处漏洞，攻击者可将其组合利用，在无需身份认证的情况下从受影响环境中窃取文件。Progress ShareFile 是一款文档共享与协作产品，广泛应用于大中型企业。此类文件传输平台历来是勒索软件团伙的重点攻击目标，此前 Clop 勒索组织就曾利用 Accellion FTA、SolarWinds Serv-U、Gladinet CentreStack、GoAnywhere MFT、MOVEit Transfer、Cleo 等产品中的漏洞实施大规模数据窃取攻击。 watchTowr 的研究人员在 Progress ShareFile 5.x 分支的 Storage Zones Controller（SZC，存储区域控制器）组件中，发现了一处认证绕过漏洞（CVE-2026-2699）和一处远程代码执行漏洞

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 440. [嘶吼] 嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
嘶吼安全动态|【国内新闻】八部门联合发布《科技数据安全管理暂行规定》，4月10日起实施摘要：明确科技数据分类分级、算法备案、跨境管控等要求，强化科研与算力设施安全。原文链接：http://m.toutiao.com/group/7626936382984700451/腾讯QClaw V2上线“龙虾管家”，全流程防护AI操作安全摘要：默认开启安全防护，覆盖Prompt、技能与脚本执行，实时拦截恶意指令、技能投毒、文件误删等风险。原文链接：https://www.sohu.com/a/1007377777_115060?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334新型底层木马NoVoice爆发，全球230万设备中招，格式化无法清除摘要：Rootkit级恶意程序深度感染安卓与iOS，国内90万台设备中招，重置后仍复活，窃取隐私并远程控制。原文链接：http

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 441. [嘶吼] 新型CrystalRAT恶意软件新增远程控制、数据窃取等功能

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
一款名为CrystalRAT的新型远程控制木马正在Telegram上以恶意软件即服务（MaaS）模式推广，提供远程控制、数据窃取、键盘记录与剪贴板劫持等核心功能。 该恶意软件于今年1月现身，采用分级订阅模式运营。除Telegram频道外，运营者还在YouTube开设专门营销账号，通过功能演示视频进行推广。 卡巴斯基研究人员在最近发布的报告中指出，这款木马与WebRAT（Salat窃密木马）高度相似，二者拥有相同的控制面板设计、均使用Go语言编写，且采用类似的机器人销售系统。 CrystalX还内置了大量恶作剧功能，用于骚扰用户或干扰其正常工作。尽管带有“娱乐化”外观，该木马仍具备全面且强大的数据窃取能力。Telegram频道推广CrystaX RATCrystalX RAT功能详情卡巴斯基表示，该恶意软件配备了易用的管理后台与自动化生成工具，支持多项自定义配置

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 442. [嘶吼] 嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
嘶吼安全动态【国内新闻】上海人工智能实验室发布“珠穆朗玛计划”，打造AI4S全国中枢摘要：上海AI实验室重磅发布“AGI4S 珠穆朗玛计划”，同步推出DeepLink融合算力平台。该计划旨在通过全维度合作打破算力与数据壁垒，为高能物理、疾病诊断等关键科学领域提供自主受控的智能底座。原文链接：https://www.news.cn/tech/20260408/fe5a61186ceb4582bdcf019c9abe0733/c.html中央网信办召开全国网络法治工作会议，部署 “十五五” 依法治网重点任务摘要：会议明确完善网络法律体系、强化App/SDK个人信息治理、加强网络司法惩戒等五大任务，推进依法治网全面落地。原文链接：https://www.cac.gov.cn/2026-04/08/c_1777384058981550.htm上海警方侦破AI黑稿工厂案，2人操控4000账号抹黑车企

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 443. [嘶吼] “龙虾”来袭，绿盟科技三位一体防御体系，让网络告别 “裸奔” 风险

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
2026年开年，OpenClaw（俗称“龙虾”）这款本地优先的 AI Agent 自动化平台以燎原之势席卷全球，凭借自然语言指令实现 PC 全功能自动化的能力，成为开发者追捧的工具。其支持15+通信平台、多模型调用、自主任务执行等特性，让效率提升的同时，也埋下了巨大的安全隐患。工信部于2026年3月8日正式发布openclaw安全风险预警通报。这款看似便捷的工具，正成为企业网络安全的“特洛伊木马”，筑牢其安全防护防线已成为企业的迫切需求。一、OpenClaw 五大核心安全痛点，直击企业网络软肋OpenClaw 的安全风险并非单一漏洞引发的局部问题，而是贯穿系统架构、权限模型、供应链和数据流转的系统性危机，五大核心痛点直指企业网络安全的薄弱环节，带来全方位的威胁。痛点一：高危漏洞频发，远程代码执行（RCE）风险一触即发OpenClaw 从2025年11月发布到首个高危 CVE 漏洞出现仅耗时

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 444. [嘶吼] 当“小龙虾”潜入内网，如何解决“影子AI”的隐匿危机

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
近期，OpenClaw（俗称“小龙虾”）这一开源AI智能体因其强大的自主执行能力而迅速爆火，成为众多企业与开发者的效率神器。然而，就在热度持续攀升之际，国家及行业权威机构接连发布重磅预警：这个看似能干的“AI助手”，正因其模糊的信任边界和脆弱的默认安全配置，成为潜伏在企业内网中的高危风险源。从已披露的CVE-2026-25253、CVE-2026-25157到最新的多个供应链投毒事件，多个已知漏洞正威胁着从个人隐私到关键基础设施的安全防线。面对来势汹汹的“龙虾”漏洞潮，传统“只扫不治”的扫描模式已然失效。企业需要的不是一份简单的风险清单，而是一套可管、可控、可追溯的漏洞治理方案。一、治理之困：为何你的网络成了“坏虾”的养殖场？在与众多企业的交流中，我们听到了两种典型的声音：  “影子AI”的恐慌：“员工偷偷部署了OpenClaw，我连它们在哪里都不知道，更别提管控了。这

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 445. [嘶吼] 绿盟NF防火墙：筑牢OpenClaw安全防线，构筑AI时代安全基石

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
2026年2月至3月，国家工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）连续两次发布关于OpenClaw（俗称“龙虾”）的安全预警，明确指出其“信任边界模糊”“配置缺陷易引发网络攻击、信息泄露”，并首次提出针对AI智能体应用的 “六要六不要” 安全建议。紧接着，国家安全部也发布《“龙虾”安全养殖手册》，警示主机被接管、数据被窃取、供应链投毒等原生风险。官方密集发声的背后，是一组触目惊心的数据：·258个已披露漏洞，其中近期发现的82个漏洞里就有12个超危以及21个高危；·46.9万个公网暴露实例，27.2%的实例存在高危漏洞，面临被直接接管风险；·22% 受监控企业存在员工私自部署的“影子AI”；·超820个恶意插件潜伏在ClawHub，伪装成实用工具窃取API密钥、执行任意命令。面对这一新型AI工具带来的系统性风险，企业急需一套既能精准发现、又能深

**缓解方案 / Mitigation**:
Follow security vendor guidance. Apply recommended patches.

---

#### 446. [先知] 【漏洞分析】Node-tar Hardlink边界绕过问题深度分析

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
以 Node-tar 的 CVE-2026-24842 为例，分析 hardlink path traversal 是如何绕过提取目录边界的，以及在常见业务场景下，如何一步步演变成任意文件读取、文件覆盖，甚至进一步的代码执行风险

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92025

---

#### 447. [先知] Slopsquatting供应链投毒

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
Slopsquatting——由 slop（对 AI 低质量输出的俗称）和 squatting（域名/包名抢注）组合而成。大语言模型（LLM）在生成代码时会「幻觉」出实际不存在的第三方包名，而攻击者只需提前在 PyPI、npm 等公共包仓库中注册这些幻觉名称，植入恶意载荷，然后静待开发者按照 AI 的建议执行 pip install。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92021

---

#### 448. [先知] 【AI赋能】六阶段AI流水线赋能APP安全分析实战

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
面向移动安全分析场景的 6 阶段总控 Skill。用于统一调度 APK 静态侦察、流量与代码对齐、SO/JNI 深度分析、加密与漏洞综合分析、验证设计与报告交付流程。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92020

---

#### 449. [先知] Letta AI 最新版未修复漏洞

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
该漏洞允许攻击者通过 REST API 提供了一个 /v1/tools/run端点，利用任意 payload 在目标服务器上执行任意 Python 代码或系统命令。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92018

---

#### 450. [先知] SGLang GGUF 投毒致 RCE 漏洞（CVE-2026-5760）

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
该漏洞存在于大模型推理引擎 SGLang 中（影响 v0.5.9 及以下版本）。其核心逻辑非常直接：SGLang 在处理 /v1/rerank 请求时，会读取 GGUF 模型文件中的 tokenizer.chat_template 字段，并将其放入一个无沙箱限制的 Jinja2 环境中进行渲染。

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92017

---

#### 451. [先知] 结合代码分析CVE-2026-33439 OpenAM 反序列化漏洞

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
结合代码分析CVE-2026-33439 OpenAM 反序列化漏洞

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92015

---

#### 452. [先知] js原型链污染原理及绕过

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
一文讲明js原型链污染原理及概念误区，包含常见绕过思路

**缓解方案 / Mitigation**:
Refer to original article for detailed remediation and PoC analysis.

**参考链接 / References**:
- https://xz.aliyun.com/news/92013

---

#### 453. CVE-1999-0012

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Some web servers under Microsoft Windows allow remote attackers to bypass access restrictions for files with long file names.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012

---

#### 454. CVE-1999-1556

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft SQL Server 6.5 uses weak encryption for the password for the SQLExecutiveCmdExec account and stores it in an accessible portion of the registry, which could allow local users to gain privileges by reading and decrypting the CmdExecAccount value.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=90222453431645&w=2
- http://www.securityfocus.com/bid/109
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7354
- http://marc.info/?l=ntbugtraq&m=90222453431645&w=2
- http://www.securityfocus.com/bid/109

---

#### 455. CVE-1999-0288

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The WINS server in Microsoft Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service (process termination) via invalid UDP frames to port 137 (NETBIOS Name Service), as demonstrated via a flood of random packets.

**参考链接 / References**:
- http://safenetworks.com/Windows/wins.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1233
- http://safenetworks.com/Windows/wins.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1233

---

#### 456. CVE-1999-1291

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
TCP/IP implementation in Microsoft Windows 95, Windows NT 4.0, and possibly others, allows remote attackers to reset connections by forcing a reset (RST) via a PSH ACK or other means, obtaining the target's last sequence number from the resulting packet, then spoofing a reset to the target.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/10789
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1383
- http://www.securityfocus.com/archive/1/10789
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1383

---

#### 457. CVE-1999-0364

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Access 97 stores a database password as plaintext in a foreign mdb, allowing access to data.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91816470220259&w=2
- http://marc.info/?l=bugtraq&m=91816470220259&w=2

---

#### 458. CVE-1999-1544

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in FTP server in Microsoft IIS 3.0 and 4.0 allows local and sometimes remote attackers to cause a denial of service via a long NLST (ls) command.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91722115016183&w=2
- http://marc.info/?l=bugtraq&m=91722115016183&w=2

---

#### 459. CVE-1999-0379

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Taskpads allows remote web sites to execute commands on the visiting user's machine via certain methods that are marked as Safe for Scripting.

**参考链接 / References**:
- http://www.osvdb.org/1019
- http://www.securityfocus.com/bid/498
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-007
- http://www.osvdb.org/1019
- http://www.securityfocus.com/bid/498

---

#### 460. CVE-1999-0386

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Personal Web Server and FrontPage Personal Web Server in some Windows systems allows a remote attacker to read files on the server by using a nonstandard URL.

**参考链接 / References**:
- http://www.osvdb.org/111
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-010
- http://www.osvdb.org/111
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-010

---

#### 461. CVE-1999-0419

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
When the Microsoft SMTP service attempts to send a message to a server and receives a 4xx error code, it quickly and repeatedly attempts to redeliver the message, causing a denial of service.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419

---

#### 462. CVE-1999-0468

**严重程度 / Severity**: HIGH | CVSS: 8.2

**漏洞描述 / Description**:
Internet Explorer 5.0 allows a remote server to read arbitrary files on the client's file system using the Microsoft Scriptlet Component.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012

---

#### 463. CVE-1999-1097

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Microsoft NetMeeting 2.1 allows one client to read the contents of another client's clipboard via a CTRL-C in the chat box when the box is empty.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92586457816446&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2187
- http://marc.info/?l=bugtraq&m=92586457816446&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2187

---

#### 464. CVE-1999-0717

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
A remote attacker can disable the virus warning mechanism in Microsoft Excel 97.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-014
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-014

---

#### 465. CVE-1999-1033

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook Express before 4.72.3612.1700 allows a malicious user to send a message that contains a .., which can inadvertently cause Outlook to re-enter POP3 command mode and cause the POP3 session to hang.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92647407427342&w=2
- http://marc.info/?l=bugtraq&m=92663402004275&w=2
- http://www.securityfocus.com/bid/252
- http://marc.info/?l=bugtraq&m=92647407427342&w=2
- http://marc.info/?l=bugtraq&m=92663402004275&w=2

---

#### 466. CVE-1999-1520

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A configuration problem in the Ad Server Sample directory (AdSamples) in Microsoft Site Server 3.0 allows an attacker to obtain the SITE.CSC file, which exposes sensitive SQL database information.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92647407227303&w=2
- http://www.securityfocus.com/bid/256
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2270
- http://marc.info/?l=bugtraq&m=92647407227303&w=2
- http://www.securityfocus.com/bid/256

---

#### 467. CVE-1999-1368

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
AV Option for MS Exchange Server option for InoculateIT 4.53, and possibly other versions, only scans the Inbox folder tree of a Microsoft Exchange server, which could allow viruses to escape detection if a user's rules cause the message to be moved to a different mailbox.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92652152723629&w=2
- http://marc.info/?l=ntbugtraq&m=97439568517355&w=2
- http://marc.info/?l=ntbugtraq&m=92652152723629&w=2
- http://marc.info/?l=ntbugtraq&m=97439568517355&w=2

---

#### 468. CVE-1999-1164

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook client allows remote attackers to cause a denial of service by sending multiple email messages with the same X-UIDL headers, which causes Outlook to hang.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93041631215856&w=2
- http://marc.info/?l=bugtraq&m=93041631215856&w=2

---

#### 469. CVE-1999-1011

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Remote Data Service (RDS) DataFactory component of Microsoft Data Access Components (MDAC) in IIS 3.x and 4.x exposes unsafe methods, which allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/j-054.shtml
- http://www.osvdb.org/272
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-004
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-025
- https://www.securityfocus.com/bid/529

---

#### 470. CVE-2000-0323

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to modify text files via a database query, aka the "Text I-ISAM" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030
- https://web.archive.org/web/20000819203059/http://xforce.iss.net:80/alerts/vol-4_num-7.php#jet-text-isam
- https://www.securityfocus.com/bid/595
- http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org

---

#### 471. CVE-1999-0700

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Dialer (dialer.exe), via a malformed dialer entry in the dialer.ini file.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-026
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-026

---

#### 472. CVE-1999-0682

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange 5.5 allows a remote attacker to relay email (i.e. spam) using encapsulated SMTP addresses, even if the anti-relaying features are enabled.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927
- http://www.ciac.org/ciac/bulletins/j-056.shtml
- http://www.securityfocus.com/bid/567
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-027
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927

---

#### 473. CVE-1999-0749

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Buffer overflow in Microsoft Telnet client in Windows 95 and Windows 98 via a malformed Telnet argument.

**参考链接 / References**:
- http://www.securityfocus.com/bid/586
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-033
- http://www.securityfocus.com/bid/586
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-033

---

#### 474. CVE-2000-0325

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to execute commands via a database query, aka the "VBA Shell" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/548
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3155
- http://www.securityfocus.com/bid/548
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030

---

#### 475. CVE-1999-1052

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft FrontPage stores form results in a default location in /_private/form_results.txt, which is world-readable and accessible in the document root, which allows remote attackers to read possibly sensitive information submitted by other users.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93582550911564&w=2
- http://marc.info/?l=bugtraq&m=93582550911564&w=2

---

#### 476. CVE-1999-1016

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft HTML control as used in (1) Internet Explorer 5.0, (2) FrontPage Express, (3) Outlook Express 5, and (4) Eudora, and possibly others, allows remote malicious web site or HTML emails to cause a denial of service (100% CPU consumption) via large HTML form fields such as text inputs in a table cell.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=93578772920970&w=2
- http://www.securityfocus.com/bid/606
- http://marc.info/?l=ntbugtraq&m=93578772920970&w=2
- http://www.securityfocus.com/bid/606

---

#### 477. CVE-1999-0910

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Site Server and Commercial Internet System (MCIS) do not set an expiration for a cookie, which could then be cached by a proxy and inadvertently used by a different user.

**参考链接 / References**:
- http://www.securityfocus.com/bid/625
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-035
- http://www.securityfocus.com/bid/625
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-035

---

#### 478. CVE-1999-0794

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Excel does not warn a user when a macro is present in a Symbolic Link (SYLK) format file.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241901
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241902
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-044
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900

---

#### 479. CVE-1999-0766

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-031
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600

---

#### 480. CVE-2000-0327

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045

---

#### 481. CVE-2000-0329

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
A Microsoft ActiveX control allows a remote attacker to execute a malicious cabinet file via an attachment and an embedded script in an HTML mail, aka the "Active Setup Control" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048

---

#### 482. CVE-2000-0073

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Rich Text Format (RTF) reader allows attackers to cause a denial of service via a malformed control word.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973
- http://xforce.iss.net/search.php3?type=2&pattern=win-malformed-rtf-control-word
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-005
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973
- http://xforce.iss.net/search.php3?type=2&pattern=win-malformed-rtf-control-word

---

#### 483. CVE-1999-0999

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Microsoft SQL 7.0 server allows a remote attacker to cause a denial of service via a malformed TDS packet.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749
- http://www.securityfocus.com/bid/817
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-059
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749
- http://www.securityfocus.com/bid/817

---

#### 484. CVE-1999-0993

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Modifications to ACLs (Access Control Lists) in Microsoft Exchange  5.5 do not take effect until the directory store cache is refreshed.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993

---

#### 485. CVE-1999-1043

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 and 5.0 does not properly handle (1) malformed NNTP data, or (2) malformed SMTP data, which allows remote attackers to cause a denial of service (application error).

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007

---

#### 486. CVE-1999-1055

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Excel 97 does not warn the user before executing worksheet functions, which could allow attackers to execute arbitrary commands by using the CALL function to execute a malicious DLL, aka the Excel "CALL Vulnerability."

**参考链接 / References**:
- http://www.securityfocus.com/bid/179
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-018
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1737
- http://www.securityfocus.com/bid/179
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-018

---

#### 487. CVE-1999-1246

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Direct Mailer feature in Microsoft Site Server 3.0 saves user domain names and passwords in plaintext in the TMLBQueue network share, which has insecure default permissions, allowing remote attackers to read the passwords and gain privileges.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q229/9/72.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2068
- http://support.microsoft.com/support/kb/articles/Q229/9/72.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2068

---

#### 488. CVE-1999-1259

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Office 98, Macintosh Edition, does not properly initialize the disk space used by Office 98 files and effectively inserts data from previously deleted files into the Office file, which could allow attackers to obtain sensitive information.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q189/5/29.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1780
- http://support.microsoft.com/support/kb/articles/q189/5/29.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1780

---

#### 489. CVE-1999-1279

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
An interaction between the AS/400 shared folders feature and Microsoft SNA Server 3.0 and earlier allows users to view each other's folders when the users share the same Local APPC LU.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q138/0/01.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1548
- http://support.microsoft.com/support/kb/articles/q138/0/01.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1548

---

#### 490. CVE-1999-1591

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Information Services (IIS) server 4.0 SP4, without certain hotfixes released for SP4, does not require authentication credentials under certain conditions, which allows remote attackers to bypass authentication requirements, as demonstrated by connecting via Microsoft Visual InterDev 6.0.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00277.html
- http://www.securityfocus.com/bid/190
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00277.html

---

#### 491. CVE-2000-0053

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Commercial Internet System (MCIS) IMAP server allows remote attackers to cause a denial of service via a malformed IMAP request.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731
- http://www.securityfocus.com/bid/912
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-001
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731
- http://www.securityfocus.com/bid/912

---

#### 492. CVE-2000-0097

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The WebHits ISAPI filter in Microsoft Index Server allows remote attackers to read arbitrary files, aka the "Malformed Hit-Highlighting Argument" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/1210
- http://www.securityfocus.com/bid/950
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- http://www.osvdb.org/1210
- http://www.securityfocus.com/bid/950

---

#### 493. CVE-2000-0098

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to determine the real path for a web directory via a request to an Internet Data Query file that does not exist.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006

---

#### 494. CVE-2000-0132

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Microsoft Java Virtual Machine allows remote attackers to read files via the getSystemResourceAsStream function.

**参考链接 / References**:
- http://www.securityfocus.com/bid/957
- http://www.securityfocus.com/bid/957

---

#### 495. CVE-2000-0089

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The rdisk utility in Microsoft Terminal Server Edition and Windows NT 4.0 stores registry hive information in a temporary file with permissions that allow local users to read it, aka the "RDISK Registry Enumeration File" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108
- http://www.securityfocus.com/bid/947
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-004
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108
- http://www.securityfocus.com/bid/947

---

#### 496. CVE-2000-0161

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sample web sites on Microsoft Site Server 3.0 Commerce Edition do not validate an identification number, which allows remote attackers to execute SQL commands.

**参考链接 / References**:
- http://www.securityfocus.com/bid/994
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-010
- http://www.securityfocus.com/bid/994
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-010

---

#### 497. CVE-2000-0162

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

---

#### 498. CVE-2000-0160

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The Microsoft Active Setup ActiveX component in Internet Explorer 4.x and 5.x allows a remote attacker to install software components without prompting the user by stating that the software's manufacturer is Microsoft.

**参考链接 / References**:
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com

---

#### 499. CVE-2000-0216

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft email clients in Outlook, Exchange, and Windows Messaging automatically respond to Read Receipt and Delivery Receipt tags, which could allow an attacker to flood a mail system with responses by forging a Read Receipt request that is redirected to a large distribution list.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html

---

#### 500. CVE-2000-0201

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The window.showHelp() method in Internet Explorer 5.x does not restrict HTML help files (.chm) to be executed from the local host, which allows remote attackers to execute arbitrary commands via Microsoft Networking.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1033
- http://www.securityfocus.com/bid/1033

---

#### 501. CVE-2000-0168

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 9x operating systems allow an attacker to cause a denial of service via a pathname that includes file device names, aka the "DOS Device in Path Name" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1043
- http://www.securityfocus.com/templates/advisory.html?id=2126
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=NCBBKFKDOLAGKIAPMILPCENECCAA.labs%40ussrback.com
- http://www.securityfocus.com/bid/1043
- http://www.securityfocus.com/templates/advisory.html?id=2126

---

#### 502. [webapps] HAX CMS 24.x - Stored Cross-Site Scripting (XSS)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] HAX CMS 24.x - Stored Cross-Site Scripting (XSS)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52526

---

#### 503. [webapps] Craft CMS 5.6.16 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Craft CMS 5.6.16 - RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52525

---

#### 504. [local] GNU InetUtils 2.6 - Telnetd Remote Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GNU InetUtils 2.6 - Telnetd Remote Privilege Escalation

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52524

---

#### 505. [webapps] phpMyFAQ  4.0.16 - Improper Authorization

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] phpMyFAQ 4.0.16 - Improper Authorization

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52523

---

#### 506. [webapps] GeographicLib v2.5.1 - stack buffer overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GeographicLib v2.5.1 - stack buffer overflow

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52522

---

#### 507. [local] OpenWrt 23.05 - Authenticated Remote Code Execution (RCE)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] OpenWrt 23.05 - Authenticated Remote Code Execution (RCE)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52521

---

#### 508. [webapps] OpenKM 6.3.12 - Multiple

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] OpenKM 6.3.12 - Multiple

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52520

---

#### 509. [webapps] GUnet OpenEclass E-learning platform < 4.2 - Remote Code Execution (RCE)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GUnet OpenEclass E-learning platform < 4.2 - Remote Code Execution (RCE)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52519

---

#### 510. [webapps] JuzaWeb CMS 3.4.2 - Authenticated Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] JuzaWeb CMS 3.4.2 - Authenticated Remote Code Execution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52518

---

#### 511. [webapps] FacturaScripts 2025.43 - XSS

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FacturaScripts 2025.43 - XSS

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52517

---

#### 512. [webapps] Xibo CMS  4.3.0 - RCE via SSTI

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Xibo CMS 4.3.0 - RCE via SSTI

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52516

---

#### 513. [local] Fedora - Local Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Fedora - Local Privilege Escalation

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52515

---

#### 514. [webapps] LangChain Core 1.2.4 - SSTI/RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] LangChain Core 1.2.4 - SSTI/RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52514

---

#### 515. [local] Atlona ATOMERX21 - Authenticated Command Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Atlona ATOMERX21 - Authenticated Command Injection

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52513

---

#### 516. CVE-1999-1182

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in run-time linkers (1) ld.so or (2) ld-linux.so for Linux systems allows local users to gain privileges by calling a setuid program with a long program name (argv[0]) and forcing ld.so/ld-linux.so to report an error.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602661419318&w=2
- http://marc.info/?l=bugtraq&m=87602661419351&w=2
- http://marc.info/?l=bugtraq&m=88661732807795&w=2
- http://marc.info/?l=bugtraq&m=87602661419318&w=2
- http://marc.info/?l=bugtraq&m=87602661419351&w=2

---

#### 517. CVE-1999-1225

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
rpc.mountd on Linux, Ultrix, and possibly other operating systems, allows remote attackers to determine the existence of a file on the server by attempting to mount that file, which generates different error messages depending on whether the file exists or not.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/7526
- https://exchange.xforce.ibmcloud.com/vulnerabilities/347
- http://www.securityfocus.com/archive/1/7526
- https://exchange.xforce.ibmcloud.com/vulnerabilities/347

---

#### 518. CVE-1999-0183

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Linux implementations of TFTP would allow access to files outside the restricted directory.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0183
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0183

---

#### 519. CVE-1999-0216

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service of inetd on Linux through SYN and RST packets.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0216
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0216

---

#### 520. CVE-1999-0340

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux Slackware crond program allows local users to gain root access.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0340
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0340

---

#### 521. CVE-1999-0341

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the Linux mail program "deliver" allows local users to gain root access.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0341
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0341

---

#### 522. CVE-1999-1229

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Quake 2 server 3.13 on Linux does not properly check file permissions for the config.cfg configuration file, which allows local users to read arbitrary files via a symlink from config.cfg to the target file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/8590
- https://exchange.xforce.ibmcloud.com/vulnerabilities/733
- http://www.securityfocus.com/archive/1/8590
- https://exchange.xforce.ibmcloud.com/vulnerabilities/733

---

#### 523. CVE-1999-0330

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux bdash game has a buffer overflow that allows local users to gain root access.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=87602558319119&w=2
- https://marc.info/?l=bugtraq&m=87602558319119&w=2

---

#### 524. CVE-1999-1407

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
ifdhcpc-done script for configuring DHCP on Red Hat Linux 5 allows local users to append text to arbitrary files via a symlink attack on the dhcplog file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=88950856416985&w=2
- http://www.iss.net/security_center/static/7294.php
- http://www.redhat.com/support/errata/rh50-errata-general.html#initscripts
- http://www.securityfocus.com/bid/368
- http://marc.info/?l=bugtraq&m=88950856416985&w=2

---

#### 525. CVE-1999-1498

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Slackware Linux 3.4 pkgtool allows local attacker to read and write to arbitrary files via a symlink attack on the reply file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/82
- http://www.securityfocus.com/bid/82

---

#### 526. CVE-1999-1442

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Bug in AMD K6 processor on Linux 2.0.x and 2.1.x kernels allows local users to cause a denial of service (crash) via a particular sequence of instructions, possibly related to accessing addresses outside of segments.

**参考链接 / References**:
- http://uwsg.iu.edu/hypermail/linux/kernel/9805.3/0855.html
- http://www.cs.helsinki.fi/linux/linux-kernel/Year-1998/1998-25/0816.html
- http://www.securityfocus.com/bid/105
- http://uwsg.iu.edu/hypermail/linux/kernel/9805.3/0855.html
- http://www.cs.helsinki.fi/linux/linux-kernel/Year-1998/1998-25/0816.html

---

#### 527. CVE-1999-1441

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux 2.0.34 does not properly prevent users from sending SIGIO signals to arbitrary processes, which allows local users to cause a denial of service by sending SIGIO to processes that do not catch it.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221103126047&w=2
- http://www.securityfocus.com/bid/111
- http://marc.info/?l=bugtraq&m=90221103126047&w=2
- http://www.securityfocus.com/bid/111

---

#### 528. CVE-1999-1434

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
login in Slackware Linux 3.2 through 3.5 does not properly check for an error when the /etc/group file is missing, which prevents it from dropping privileges, causing it to assign root privileges to any local user who logs on to the server.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221104525951&w=2
- http://www.securityfocus.com/bid/155
- http://marc.info/?l=bugtraq&m=90221104525951&w=2
- http://www.securityfocus.com/bid/155

---

#### 529. CVE-1999-1406

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dumpreg in Red Hat Linux 5.1 opens /dev/mem with O_RDWR access, which allows local users to cause a denial of service (crash) by redirecting fd 1 (stdout) to the kernel.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221104526185&w=2
- http://marc.info/?l=bugtraq&m=90221104526192&w=2
- http://www.securityfocus.com/bid/372
- http://marc.info/?l=bugtraq&m=90221104526185&w=2
- http://marc.info/?l=bugtraq&m=90221104526192&w=2

---

#### 530. CVE-1999-0262

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Hylafax faxsurvey CGI script on Linux allows remote attackers to execute arbitrary commands via shell metacharacters in the query string.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2056
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1532
- http://www.securityfocus.com/bid/2056
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1532

---

#### 531. CVE-1999-1381

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in dbadmin CGI program 1.0.1 on Linux allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90786656409618&w=2
- http://marc.info/?l=bugtraq&m=90786656409618&w=2

---

#### 532. CVE-1999-0002

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in NFS mountd gives root access to remote attackers, mostly in Linux systems.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/19981006-01-I
- http://www.ciac.org/ciac/bulletins/j-006.shtml
- http://www.securityfocus.com/bid/121
- ftp://patches.sgi.com/support/free/security/advisories/19981006-01-I
- http://www.ciac.org/ciac/bulletins/j-006.shtml

---

#### 533. CVE-1999-0342

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Linux PAM modules allow local users to gain root access using temporary files.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0342
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0342

---

#### 534. CVE-1999-0798

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in bootpd on OpenBSD, FreeBSD, and Linux systems via a malformed header type.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91278867118128&w=2
- http://marc.info/?l=bugtraq&m=91278867118128&w=2

---

#### 535. CVE-1999-1173

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Corel Word Perfect 8 for Linux creates a temporary working directory with world-writable permissions, which allows local users to (1) modify Word Perfect behavior by modifying files in the working directory, or (2) modify files of other users via a symlink attack.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91404045014047&w=2
- http://marc.info/?l=bugtraq&m=91404045014047&w=2

---

#### 536. CVE-1999-1285

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux 2.1.132 and earlier allows local users to cause a denial of service (resource exhaustion) by reading a large buffer from a random device (e.g. /dev/urandom), which cannot be interrupted until the read has completed.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91495921611500&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1472
- http://marc.info/?l=bugtraq&m=91495921611500&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1472

---

#### 537. CVE-1999-0243

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Linux cfingerd could be exploited to gain root access.

**参考链接 / References**:
- http://www.geocrawler.com/archives/3/92/1996/9/0/2217716/
- http://www.geocrawler.com/archives/3/92/1996/9/0/2217716/

---

#### 538. CVE-1999-0398

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
In some instances of SSH 1.2.27 and 2.0.11 on Linux systems, SSH will allow users with expired accounts to login.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0398
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0398

---

#### 539. CVE-1999-0401

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
A race condition in Linux 2.2.1 allows local users to read arbitrary memory from /proc files.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0401
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0401

---

#### 540. CVE-1999-0698

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Denial of service in IP protocol logger (ippl) on Red Hat and Debian Linux.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0698
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0698

---

#### 541. CVE-1999-0389

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the bootp server in the Debian Linux netstd package.

**参考链接 / References**:
- http://www.securityfocus.com/bid/324
- http://www.securityfocus.com/bid/324

---

#### 542. CVE-1999-0390

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Dosemu Slang library in Linux.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-006.1.txt
- http://www.securityfocus.com/bid/187
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-006.1.txt
- http://www.securityfocus.com/bid/187

---

#### 543. CVE-1999-0457

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux ftpwatch program allows local users to gain root privileges.

**参考链接 / References**:
- http://www.securityfocus.com/bid/317
- http://www.securityfocus.com/bid/317

---

#### 544. CVE-1999-0451

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Denial of service in Linux 2.0.36 allows local users to prevent any server from listening on any non-privileged port.

**参考链接 / References**:
- http://www.securityfocus.com/bid/343
- http://www.securityfocus.com/bid/343

---

#### 545. CVE-1999-0400

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Denial of service in Linux 2.2.0 running the ldd command on a core file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/344
- http://www.securityfocus.com/bid/344

---

#### 546. CVE-1999-0461

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Versions of rpcbind including Linux, IRIX, and Wietse Venema's rpcbind allow a remote attacker to insert and delete entries by spoofing a source address.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0461
- https://www.cve.org/CVERecord?id=CVE-1999-0461

---

#### 547. CVE-2000-0370

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The debug option in Caldera Linux smail allows remote attackers to execute commands via shell metacharacters in the -D option for the rmail command.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-001.0.txt
- http://www.securityfocus.com/bid/1268
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-001.0.txt
- http://www.securityfocus.com/bid/1268

---

#### 548. CVE-1999-0403

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A bug in Cyrix CPUs on Linux allows local users to perform a denial of service.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91821080015725&w=2
- http://marc.info/?l=bugtraq&m=91821080015725&w=2

---

#### 549. CVE-1999-0459

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Local users can perform a denial of service in Alpha Linux, using MILO to force a reboot.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0459
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0459

---

#### 550. CVE-1999-1495

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
xtvscreen in SuSE Linux 6.0 allows local users to overwrite arbitrary files via a symlink attack on the pic000.pnm file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/12580
- http://www.securityfocus.com/bid/325
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1792
- http://www.securityfocus.com/archive/1/12580
- http://www.securityfocus.com/bid/325

---

#### 551. CVE-1999-0460

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Buffer overflow in Linux autofs module through long directory names allows local users to perform a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/312
- http://www.securityfocus.com/bid/312

---

#### 552. CVE-1999-1168

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
install.iss installation script for Internet Security Scanner (ISS) for Linux, version 5.3, allows local users to change the permissions of arbitrary files via a symlink attack on a temporary file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/12640
- http://www.securityfocus.com/archive/1/12640

---

#### 553. CVE-1999-0414

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
In Linux before version 2.0.36, remote attackers can spoof a TCP connection and pass data to the application layer before fully establishing the connection.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0414
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0414

---

#### 554. CVE-2026-5435 - glibc: glibc: Out-of-bounds write via TSIG record processing

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] glibc: glibc: Out-of-bounds write via TSIG record processing. Bugzilla: 2463465

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463465

---

#### 555. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 556. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 557. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 558. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 559. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 560. CVE-2026-7351 - chromium-browser: Race in MHTML

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Race in MHTML. Bugzilla: 2463656

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463656

---

#### 561. CVE-2026-7353 - chromium-browser: Heap buffer overflow in Skia

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in Skia. Bugzilla: 2463657

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463657

---

#### 562. CVE-2026-7339 - chromium-browser: Heap buffer overflow in WebRTC

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in WebRTC. Bugzilla: 2463658

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463658

---

#### 563. CVE-2026-7341 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463659

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463659

---

#### 564. CVE-2026-7338 - chromium-browser: Use after free in Cast

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Cast. Bugzilla: 2463660

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463660

---

#### 565. CVE-2026-7334 - chromium-browser: Use after free in Views

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Views. Bugzilla: 2463663

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463663

---

#### 566. CVE-2026-7340 - chromium-browser: Integer overflow in ANGLE

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Integer overflow in ANGLE. Bugzilla: 2463664

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463664

---

#### 567. CVE-2026-7358 - chromium-browser: Use after free in Animation

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Animation. Bugzilla: 2463665

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463665

---

#### 568. CVE-2026-7356 - chromium-browser: Use after free in Navigation

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Navigation. Bugzilla: 2463667

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463667

---

#### 569. CVE-2026-7352 - chromium-browser: Use after free in Media

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Media. Bugzilla: 2463669

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463669

---

#### 570. CVE-2026-7359 - chromium-browser: Use after free in ANGLE

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in ANGLE. Bugzilla: 2463670

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463670

---

#### 571. CVE-2026-7348 - chromium-browser: Use after free in Codecs

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Codecs. Bugzilla: 2463671

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463671

---

#### 572. CVE-2026-7336 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463676

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463676

---

#### 573. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 574. [Ubuntu] USN-8223-1: Roundcube Webmail vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that Roundcube Webmail mishandled Punycode xn-- domain names. An attacker could possibly use this issue to cause a homograph attack. (CVE-2019-15237) It was discovered that Roundcube Webmail did not properly sanitize certain attributes when handling CSS within HTML messages and certain SVG attributes. An attacker could possibly use this issue to cause a cross-site scripting attac

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8223-1

---

#### 575. [Ubuntu] USN-8224-1: Linux kernel (BlueField) vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Qualys discovered that several vulnerabilities existed in the AppArmor Linux kernel Security Module (LSM). An unprivileged local attacker could use these issues to load, replace, and remove arbitrary AppArmor profiles causing denial of service, exposure of sensitive information (kernel memory), local privilege escalation, or possibly escape a container. (LP: #2143853, CVE-2026-23268, CVE-2026-2326

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8224-1

---

#### 576. [Ubuntu] USN-8222-1: OpenSSH vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Christos Papakonstantinou discovered that the OpenSSH scp tool incorrectly handled the legacy scp protocol (-O) option. This could result in certain files being installed setuid or setgid, contrary to expectations. (CVE-2026-35385) Florian Kohnhäuser discovered that OpenSSH incorrectly handled shell metacharacters in usernames within a command line. When untrusted usernames and non-default configu

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8222-1

---

#### 577. [Ubuntu] USN-8195-3: PackageKit vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8195-1 fixed a vulnerability in PackageKit. This update provides the corresponding fix to Ubuntu 16.04 LTS, Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. Original advisory details: It was discovered that PackageKit incorrectly handled certain transactions. A local attacker could use this issue to install arbitrary packages as root, possibly resulting in privilege escalation.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8195-3

---

#### 578. [Ubuntu] USN-8221-1: wheel vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that wheel did not correctly handle certain file paths. If a user or automated system were tricked into opening a specially crafted file, an attacker could possibly use this issue to execute arbitrary code.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8221-1

---

#### 579. [Ubuntu] USN-8198-2: Tornado vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8198-1 fixed vulnerabilities in Tornado. This update provides the corresponding updates for Ubuntu 26.04 LTS. Original advisory details: It was discovered that Tornado incorrectly handled parsing of large multipart request bodies. An attacker could possibly use this issue to cause a denial of service. (CVE-2026-31958) It was discovered that Tornado did not properly validate characters in cooki

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8198-2

---

#### 580. [Ubuntu] USN-8219-1: UltraJSON vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Cameron Criswell discovered that UltraJSON contained a memory leak that would occur when parsing large integers. An attacker could possibly use this issue to cause UltraJSON to crash, resulting in a denial of service. This issue only affected Ubuntu 24.04 LTS, Ubuntu 25.10, and Ubuntu 26.04 LTS. (CVE-2026-32874) It was discovered that UltraJSON contained integer overflow/underflow issues when calc

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8219-1

---

#### 581. [Ubuntu] USN-8185-2: Linux kernel (Low Latency NVIDIA) vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Josh Eads, Kristoffer Janke, Eduardo Vela Nava, Tavis Ormandy, and Matteo Rizzo discovered that some AMD Zen processors did not properly verify the signature of CPU microcode. This flaw is known as EntrySign. A privileged attacker could possibly use this issue to cause load malicious CPU microcode causing loss of integrity and confidentiality. (CVE-2024-36347) Several security issues were discover

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8185-2

---

#### 582. [Ubuntu] USN-8217-1: follow-redirects vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that follow-redirects did not properly protect sensitive user information during redirects. An attacker could possibly use this issue to expose sensitive information. This issue only affected Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. (CVE-2022-0155) It was discovered that follow-redirects did not properly remove sensitive information before storage or transfer. An attacker could pos

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8217-1

---

#### 583. [Ubuntu] USN-8190-2: Rack::Session vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8190-1 fixed a vulnerability in Rack::Session. This update provides the corresponding update for Ubuntu 26.04 LTS. Original advisory details: SeungMyung Lee discovered that Rack::Session did not properly reject cookies upon decryption failure. A remote attacker could use this issue to manipulate session contents and possibly gain unauthorized access.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8190-2

---

#### 584. [Arch] AVG-2843

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: vim. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 585. [Arch] AVG-2842

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: libtiff. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 586. [Arch] AVG-2827

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: grunt-cli. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 587. [Arch] AVG-2820

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: wpewebkit. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 588. [Arch] AVG-2818

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: connman. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 589. [Arch] AVG-2816

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: squid. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 590. [Arch] AVG-2809

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: python-django. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 591. [Arch] AVG-2799

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: blender. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 592. [Arch] AVG-2781

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: python-pyjwt. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 593. [Arch] AVG-2780

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: wpewebkit. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 594. [Arch] AVG-2725

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: containerd. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 595. [Arch] AVG-2836

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-zen. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 596. [Arch] AVG-2835

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-hardened. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 597. [Arch] AVG-2834

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-lts. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 598. [Arch] AVG-2764

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: ruby-puma. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 599. [Arch] AVG-2907

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: djvulibre. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 600. [Arch] AVG-2901

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: pam. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 601. [Arch] AVG-2898

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: libxml2. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 602. [Arch] AVG-2889

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: tomcat9. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 603. [Arch] AVG-2888

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: tomcat10. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 604. [Arch] AVG-2886

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: kea. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 605. [Arch] AVG-2762

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: grub. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 606. [Arch] AVG-2701

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-lts. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 607. [Arch] AVG-2275

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: nim. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 608. [Arch] AVG-2272

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: exim. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 609. [Arch] AVG-2190

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: jre8-openjdk-headless, jdk8-openjdk. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 610. [Arch] AVG-2893

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: systemd. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 611. [Arch] AVG-2885

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: coreutils. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 612. [Arch] AVG-2884

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: grafana. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 613. [Arch] AVG-2875

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: postgresql. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 614. [Gentoo] GLSA 202604-04: DTrace: Arbitrary file creation via dtprobed

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A DTrace component, dtprobed, allows arbitrary file creation through crafted USDT provider names.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202604-04

---

#### 615. [Gentoo] GLSA 202604-03: FUSE: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been found in FUSE, the worst of which can lead to code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202604-03

---

#### 616. [Gentoo] GLSA 202603-01: Exiv2: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been found in Exiv2, the worst of which can lead to a crash via Denial of Service.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202603-01

---

#### 617. [Gentoo] GLSA 202601-05: Commons-BeanUtils: Arbitary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in Commons-BeanUtils, which can lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-05

---

#### 618. [Gentoo] GLSA 202601-04: Asterisk: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Asterisk, the worst of which can lead to arbitrary code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-04

---

#### 619. [Gentoo] GLSA 202601-03: GIMP: Arbitrary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in GIMP, which can lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-03

---

#### 620. [Gentoo] GLSA 202601-02: Vim, gVim: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Vim and gVim, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-02

---

#### 621. [Gentoo] GLSA 202601-01: inetutils: Remote Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in the telnetd module of inetutils, which allows remote code execution as root.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-01

---

#### 622. [Gentoo] GLSA 202512-01: GnuPG: Arbitrary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in GnuPG, which can lead to arbitrary code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202512-01

---

#### 623. [Gentoo] GLSA 202511-07: librnp: Weak random number generation

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
librnp uses weak random number generation such that generated keys can be easily cracked.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-07

---

#### 624. [Gentoo] GLSA 202511-06: libpng: Multiple vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in libpng, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-06

---

#### 625. [Gentoo] GLSA 202511-05: redict, redis: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in redis and redict, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-05

---

#### 626. [Gentoo] GLSA 202511-04: Chromium, Google Chrome, Microsoft Edge. Opera: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Chromium and its derivatives, the worst of which can lead to remote code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-04

---

#### 627. [Gentoo] GLSA 202511-03: qtsvg: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in qtsvg, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-03

---

#### 628. [Gentoo] GLSA 202511-02: WebKitGTK+: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in WebKitGTK+, the worst of which can lead to execution of arbitary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-02

---

#### 629. CVE-1999-1262

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Java in Netscape 4.5 does not properly restrict applets from connecting to other hosts besides the one from which the applet was loaded, which violates the Java security model and could allow remote attackers to conduct unauthorized activities.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727

---

#### 630. CVE-1999-1015

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Apple AppleShare Mail Server 5.0.3 on MacOS 8.1 and earlier allows a remote attacker to cause a denial of service (crash) via a long HELO command.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61

---

#### 631. CVE-1999-1393

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Control Panel "Password Security" option for Apple Powerbooks allows attackers with physical access to the machine to bypass the security by booting it with an emergency startup disk and using a disk editor to modify the on/off toggle or password in the aaaaaaaAPWD file, which is normally inaccessible.

**参考链接 / References**:
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532

---

#### 632. CVE-1999-1412

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306

---

#### 633. CVE-1999-0793

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Internet Explorer allows remote attackers to read files by redirecting data to a Javascript applet.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043

---

#### 634. CVE-2000-0237

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Netscape Enterprise Server with Web Publishing enabled allows remote attackers to list arbitrary directories via a GET request for the /publisher directory, which provides a Java applet that allows the attacker to browse the directories.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1

---

#### 635. CVE-2000-0265

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Panda Security 3.0 allows users to uninstall the Panda software via its Add/Remove Programs applet.

**参考链接 / References**:
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FB45F2.550EA000%40teleline.es
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119

---

#### 636. CVE-2000-0266

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Internet Explorer 5.01 allows remote attackers to bypass the cross frame security policy via a malicious applet that interacts with the Java JSObject to modify the DOM properties to set the IFRAME to an arbitrary Javascript URL.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg

---

#### 637. CVE-2000-0346

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
AppleShare IP 6.1 and later allows a remote attacker to read potentially sensitive information via an invalid range request to the web server.

**参考链接 / References**:
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000502133240.21807.qmail%40securityfocus.com
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162

---

#### 638. CVE-2000-0676

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Netscape Communicator and Navigator 4.04 through 4.74 allows remote attackers to read arbitrary files by using a Java applet to open a connection to a URL using the "file", "http", "https", and "ftp" protocols, as demonstrated by Brown Orifice.

**参考链接 / References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0019.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0115.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0236.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0265.html

---

#### 639. CVE-2000-0711

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Netscape Communicator does not properly prevent a ServerSocket object from being created by untrusted entities, which allows remote attackers to create a server on the victim's system via a malicious applet, as demonstrated by Brown Orifice.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2000-15.html
- http://www.securityfocus.com/bid/1545
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000805020429.11774.qmail%40securityfocus.com
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3999922128E.EE84TAKAGI%40java-house.etl.go.jp
- http://www.cert.org/advisories/CA-2000-15.html

---

#### 640. CVE-2000-1061

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) in Internet Explorer 4.x and 5.x allows an unsigned applet to create and use ActiveX controls, which allows a remote attacker to bypass Internet Explorer's security settings and execute arbitrary commands via a malicious web page or email, aka the "Microsoft VM ActiveX Component" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127

---

#### 641. CVE-2000-0889

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Two Sun security certificates have been compromised, which could allow attackers to insert malicious code such as applets and make it appear that it is signed by Sun.

**参考链接 / References**:
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html

---

#### 642. CVE-2001-0068

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Mac OS Runtime for Java (MRJ) 2.2.3 allows remote attackers to use malicious applets to read files outside of the CODEBASE context via the ARCHIVE applet parameter.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784

---

#### 643. CVE-2001-0137

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Windows Media Player 7 allows remote attackers to execute malicious Java applets in Internet Explorer clients by enclosing the applet in a skin file named skin.wmz, then referencing that skin in the codebase parameter to an applet tag, aka the Windows Media Player Skins File Download" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97958100816503&w=2
- http://www.securityfocus.com/bid/2203
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-010
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5937
- http://marc.info/?l=bugtraq&m=97958100816503&w=2

---

#### 644. CVE-2001-0324

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Windows 98 and Windows 2000 Java clients allow remote attackers to cause a denial of service via a Java applet that opens a large number of UDP sockets, which prevents the host from establishing any additional UDP connections, and possibly causes a crash.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340

---

#### 645. CVE-2001-1026

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Trend Micro InterScan AppletTrap 2.0 does not properly filter URLs when they are modified in certain ways such as (1) using a double slash (//) instead of a single slash, (2) URL-encoded characters, (3) requesting the IP address instead of the domain name, or (4) using a leading 0 in an octet of an IP address.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html
- http://www.securityfocus.com/bid/2996
- http://www.securityfocus.com/bid/2998
- http://www.securityfocus.com/bid/3000
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6816

---

#### 646. CVE-2001-1008

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Java Plugin 1.4 for JRE 1.3 executes signed applets even if the certificate is expired, which could allow remote attackers to conduct unauthorized activities via an applet that has been signed by an expired certificate.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php
- http://www.securityfocus.com/bid/3245
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php

---

#### 647. CVE-2001-1254

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Web Access component for COM2001 Alexis 2.0 and 2.1 in InternetPBX sends username and voice mail passwords in the clear via a Java applet that sends the information to port 8888 of the server, which could allow remote attackers to steal the passwords via sniffing.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373

---

#### 648. CVE-2001-0806

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Apple MacOS X 10.0 and 10.1 allow a local user to read and write to a user's desktop folder via insecure default permissions for the Desktop when it is created in some languages.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99358249631139&w=2
- http://marc.info/?l=bugtraq&m=99436289015729&w=2
- http://online.securityfocus.com/archive/1/219166
- http://www.osvdb.org/1882
- http://www.securityfocus.com/bid/2930

---

#### 649. CVE-2001-1480

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Java Runtime Environment (JRE) and SDK 1.2 through 1.3.0_04 allows untrusted applets to access the system clipboard.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/208&type=0&nav=sec.sba
- http://www.securityfocus.com/advisories/3617
- http://www.securityfocus.com/bid/3441
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7333

---

#### 650. CVE-2001-1575

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apple Personal Web Sharing (PWS) 1.1, 1.5, and 1.5.5, when Web Sharing authentication is enabled, allows remote attackers to cause a denial of service via a long password, possibly due to a buffer overflow.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6759
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945

---

#### 651. CVE-2002-1601

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The Connectables feature in Adobe PhotoDeluxe 3.1 prepends the Adobe directory to the CLASSPATH environment variable, which allows applets to run with higher privileges and remote attackers to gain privileges via an HTML e-mail message or a web page.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/116875
- http://www.kb.cert.org/vuls/id/AAMN-56LQ2J
- http://www.securityfocus.com/bid/4106
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8210
- http://www.kb.cert.org/vuls/id/116875

---

#### 652. CVE-2002-0058

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerability in Java Runtime Environment (JRE) allows remote malicious web sites to hijack or sniff a web client's sessions, when an HTTP proxy is being used, via a Java applet that redirects the session to another server, as seen in (1) Netscape 6.0 through 6.1 and 4.79 and earlier, (2) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, and possibly other implementations that use vulnerable versions of SDK or JDK.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216

---

#### 653. CVE-2002-0076

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Java Runtime Environment (JRE) Bytecode Verifier allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, as seen in (1) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, (2) Netscape 6.2.1 and earlier, and possibly other implementations that use vulnerable versions of SDK or JDK, aka a variant of the "Virtual Machine Verifier" vulnerability.

**参考链接 / References**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218
- http://www.iss.net/security_center/static/8480.php
- http://www.securityfocus.com/bid/4313
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218

---

#### 654. CVE-2002-0120

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Apple Palm Desktop 4.0b76 and 4.0b77 creates world-readable backup files and folders when a hotsync is performed, which could allow a local user to obtain sensitive information.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php
- http://www.securityfocus.com/bid/3863
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php

---

#### 655. CVE-2002-0153

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.1 for Macintosh allows remote attackers to bypass security checks and invoke local AppleScripts within a specific HTML element, aka the "Local Applescript Invocation" vulnerability.

**参考链接 / References**:
- http://www.iss.net/security_center/static/8851.php
- http://www.osvdb.org/5356
- http://www.securityfocus.com/archive/1/251805
- http://www.securityfocus.com/bid/3935
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-019

---

#### 656. CVE-2002-0252

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.01 and 5.02 allows remote web servers to execute arbitrary code via a response containing a long Content-Type MIME header.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101320742616105&w=2
- http://www.iss.net/security_center/static/8126.php
- http://www.securityfocus.com/bid/4064
- https://www.exploit-db.com/exploits/4673
- http://marc.info/?l=bugtraq&m=101320742616105&w=2

---

#### 657. CVE-2002-0676

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SoftwareUpdate for MacOS 10.1.x does not use authentication when downloading a software update, which could allow remote attackers to execute arbitrary code by posing as the Apple update server via techniques such as DNS spoofing or cache poisoning, and supplying Trojan Horse updates.

**参考链接 / References**:
- http://www.cunap.com/~hardingr/projects/osx/exploit.html
- http://www.iss.net/security_center/static/9502.php
- http://www.osvdb.org/5137
- http://www.securityfocus.com/bid/5176
- http://www.cunap.com/~hardingr/projects/osx/exploit.html

---

#### 658. CVE-2002-0376

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime 5.0 ActiveX component allows remote attackers to execute arbitrary code via a long pluginspage field.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/293095
- http://www.atstake.com/research/advisories/2002/a091002-1.txt
- http://www.iss.net/security_center/static/10077.php
- http://www.securityfocus.com/bid/5685
- http://online.securityfocus.com/archive/1/293095

---

#### 659. CVE-2002-0976

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Internet Explorer 4.0 and later allows remote attackers to read arbitrary files via a web page that accesses a legacy XML Datasource applet (com.ms.xml.dso.XMLDSO.class) and modifies the base URL to point to the local system, which is trusted by the applet.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php
- http://www.securityfocus.com/bid/5490
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php

---

#### 660. CVE-2002-0865

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A certain class that supports XML (Extensible Markup Language) in Microsoft Virtual Machine (VM) 5.0.3805 and earlier, probably com.ms.osp.ospmrshl, exposes certain unsafe methods, which allows remote attackers to execute unsafe code via a Java applet, aka "Inappropriate Methods Exposed in XML Support Classes."

**参考链接 / References**:
- http://www.iss.net/security_center/static/10135.php
- http://www.kb.cert.org/vuls/id/140898
- http://www.securityfocus.com/bid/5752
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10135.php

---

#### 661. CVE-2002-0866

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Java Database Connectivity (JDBC) classes in Microsoft Virtual Machine (VM) up to and including 5.0.3805 allow remote attackers to load and execute DLLs (dynamic link libraries) via a Java applet that calls the constructor for com.ms.jdbc.odbc.JdbcOdbc with the desired DLL terminated by a null string, aka "DLL Execution via JDBC Classes."

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html
- http://www.iss.net/security_center/static/10133.php
- http://www.kb.cert.org/vuls/id/307306
- http://www.securityfocus.com/bid/5751
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052

---

#### 662. CVE-2002-0867

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to cause a denial of service (crash) in Internet Explorer via invalid handle data in a Java applet, aka "Handle Validation Flaw."

**参考链接 / References**:
- http://www.iss.net/security_center/static/10134.php
- http://www.kb.cert.org/vuls/id/792881
- http://www.securityfocus.com/bid/5750
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10134.php

---

#### 663. CVE-2002-1286

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to steal cookies and execute script in a different security context via a URL that contains a colon in the domain portion, which is not properly parsed and loads an applet from a malicious site within the security context of the site that is being visited by the user.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/657625
- http://www.securityfocus.com/bid/6142
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10579

---

#### 664. CVE-2002-1290

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read and modify the contents of the Clipboard via an applet that accesses the (1) ClipBoardGetText and (2) ClipBoardSetText methods of the INativeServices class.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10583.php
- http://www.securityfocus.com/bid/6132
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

---

#### 665. CVE-2002-1291

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read arbitrary local files and network shares via an applet tag with a codebase set to a "file://%00" (null character) URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10584.php
- http://www.securityfocus.com/bid/6138
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

---

#### 666. CVE-2002-1292

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Java virtual machine (VM) build 5.0.3805 and earlier, as used in Internet Explorer, allows remote attackers to extend the Standard Security Manager (SSM) class (com.ms.security.StandardSecurityManager) and bypass intended StandardSecurityManager restrictions by modifying the (1) deniedDefinitionPackages or (2) deniedAccessPackages settings, causing a denial of service by adding Java applets to the list of applets that are prevented from running.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/237777
- http://www.securityfocus.com/bid/6133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

---

#### 667. CVE-2002-1294

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, can provide HTML object references to applets via Javascript, which allows remote attackers to cause a denial of service (crash due to illegal memory accesses) and possibly conduct other unauthorized activities via an applet that uses those references to access proprietary Microsoft methods.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10587.php
- http://www.securityfocus.com/bid/6135
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

---

#### 668. CVE-2002-1295

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service (crash) and possibly conduct other unauthorized activities via applet tags in HTML that bypass Java class restrictions (such as private constructors) by providing the class name in the code parameter, aka "Incomplete Java Object Instantiation Vulnerability."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10588.php
- http://www.securityfocus.com/bid/6136
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

---

#### 669. CVE-2002-1257

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to execute arbitrary code by including a Java applet that invokes COM (Component Object Model) objects in a web site or an HTML mail.

**参考链接 / References**:
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

---

#### 670. CVE-2002-1258

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Two vulnerabilities in Microsoft Virtual Machine (VM) up to and including build 5.0.3805, as used in Internet Explorer and other applications, allow remote attackers to read files via a Java applet with a spoofed location in the CODEBASE parameter in the APPLET tag, possibly due to a parsing error.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582

---

#### 671. CVE-2002-1260

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Java Database Connectivity (JDBC) APIs in Microsoft Virtual Machine (VM) 5.0.3805 and earlier allow remote attackers to bypass security checks and access database contents via an untrusted Java applet.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/n-026.shtml
- http://www.securityfocus.com/bid/6379
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10833
- http://www.ciac.org/ciac/bulletins/n-026.shtml

---

#### 672. CVE-2002-1325

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) build 5.0.3805 and earlier allows remote attackers to determine a local user's username via a Java applet that accesses the user.dir system property, aka "User.dir Exposure Vulnerability."

**参考链接 / References**:
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

---

#### 673. CVE-2002-1898

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Terminal 1.3 in Apple Mac OS X 10.2 allows remote attackers to execute arbitrary commands via shell metacharacters in a telnet:// link, which is executed by Terminal.app window.

**参考链接 / References**:
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172
- http://lists.apple.com/archives/security-announce/2002/Sep/msg00001.html
- http://www.iss.net/security_center/static/10156.php
- http://www.securityfocus.com/bid/5768
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172

---

#### 674. CVE-1999-1113

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Eudora Internet Mail Server (EIMS) 2.01 and earlier on MacOS systems allows remote attackers to cause a denial of service via a long USER command to port 106.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=89258194718577&w=2
- http://www.securityfocus.com/bid/75
- http://marc.info/?l=bugtraq&m=89258194718577&w=2
- http://www.securityfocus.com/bid/75

---

#### 675. CVE-1999-1543

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
MacOS uses weak encryption for passwords that are stored in the Users & Groups Data File.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93188174906513&w=2
- http://marc.info/?l=bugtraq&m=93736667813924&w=2
- http://www.securityfocus.com/bid/519
- http://marc.info/?l=bugtraq&m=93188174906513&w=2
- http://marc.info/?l=bugtraq&m=93736667813924&w=2

---

#### 676. CVE-1999-1076

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local users to bypass the password protection of idled sessions by selecting the "Log Out" option and selecting a "Cancel" option in the dialog box for an application that attempts to verify that the user wants to log out, which returns the attacker into the locked session.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94096348604173&w=2
- http://www.securityfocus.com/bid/745
- http://marc.info/?l=bugtraq&m=94096348604173&w=2
- http://www.securityfocus.com/bid/745

---

#### 677. CVE-1999-1077

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local attackers to bypass the password protection of idled sessions via the programmer's switch or CMD-PWR keyboard sequence, which brings up a debugger that the attacker can use to disable the lock.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94149318124548&w=2
- http://www.securityfocus.com/bid/756
- http://marc.info/?l=bugtraq&m=94149318124548&w=2
- http://www.securityfocus.com/bid/756

---

#### 678. CVE-1999-1528

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
ProSoft Netware Client 5.12 on Macintosh MacOS 9 does not automatically log a user out of the NDS tree when the user logs off the system, which allows other users of the same system access to the unprotected NDS session.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94261444428430&w=2
- http://www.securityfocus.com/bid/794
- http://marc.info/?l=bugtraq&m=94261444428430&w=2
- http://www.securityfocus.com/bid/794

---

#### 679. CVE-2000-0563

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The URLConnection function in MacOS Runtime Java (MRJ) 2.1 and earlier and the Microsoft virtual machine (VM) for MacOS allows a malicious web site operator to connect to arbitrary hosts using a HTTP redirection, in violation of the Java security model.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0056.html
- http://www.securityfocus.com/bid/1336
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-05-8&msg=391C95DE2DA.5E3BTAKAGI%40java-house.etl.go.jp
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0056.html
- http://www.securityfocus.com/bid/1336

---

#### 680. CVE-2001-0766

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Apache on MacOS X Client 10.0.3 with the HFS+ file system allows remote attackers to bypass access restrictions via a URL that contains some characters whose case is not matched by Apache's filters.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-06/0090.html
- http://www.securityfocus.com/bid/2852
- http://archives.neohapsis.com/archives/bugtraq/2001-06/0090.html
- http://www.securityfocus.com/bid/2852

---

#### 681. CVE-2001-0921

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Netscape 4.79 and earlier for MacOS allows an attacker with access to the browser to obtain passwords from form fields by printing the document into which the password has been typed, which is printed in cleartext.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100638816318705&w=2
- http://www.osvdb.org/5524
- http://www.securityfocus.com/bid/3565
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7593
- http://marc.info/?l=bugtraq&m=100638816318705&w=2

---

#### 682. CVE-2001-1565

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Point to Point Protocol daemon (pppd) in MacOS x 10.0 and 10.1 through 10.1.5 provides the username and password on the command line, which allows local users to obtain authentication information via the ps command.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7750.php
- http://www.macsecurity.org/pipermail/macsec/2001-December/000299.html
- http://www.securityfocus.com/bid/3753
- http://www.iss.net/security_center/static/7750.php
- http://www.macsecurity.org/pipermail/macsec/2001-December/000299.html

---

#### 683. CVE-2002-1773

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in ICQ 2.6x for MacOS X 10.0 through 10.1.2 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long request.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/254133
- http://online.securityfocus.com/archive/1/254141
- http://www.securityfocus.com/bid/4031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8085
- http://online.securityfocus.com/archive/1/254133

---

#### 684. CVE-2002-2169

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Cross-site scripting vulnerability AOL Instant Messenger (AIM) 4.5 and 4.7 for MacOS and Windows allows remote attackers to conduct unauthorized activities, such as adding buddies and groups to a user's buddy list, via a URL with a META HTTP-EQUIV="refresh" tag to an aim: URL.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/282443
- http://www.iss.net/security_center/static/9616.php
- http://www.mindflip.org/aim.html
- http://www.securityfocus.com/bid/5246
- http://online.securityfocus.com/archive/1/282443

---

#### 685. CVE-2003-0088

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
TruBlueEnvironment for MacOS 10.2.3 and earlier allows local users to overwrite or create arbitrary files and gain root privileges by setting a certain environment variable that is used to write debugging information.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://www.atstake.com/research/advisories/2003/a021403-1.txt
- http://www.iss.net/security_center/static/11332.php
- http://www.securityfocus.com/bid/6859

---

#### 686. CVE-2002-1491

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Cisco VPN 5000 Client for MacOS before 5.2.2 records the most recently used login password in plaintext when saving "Default Connection" settings, which could allow local users to gain privileges.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml
- http://www.iss.net/security_center/static/10129.php
- http://www.osvdb.org/7041
- http://www.securityfocus.com/bid/5736
- http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml

---

#### 687. CVE-2003-0171

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
DirectoryServices in MacOS X trusts the PATH environment variable to locate and execute the touch command, which allows local users to execute arbitrary commands by modifying the PATH to point to a directory containing a malicious touch program.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00028.html
- http://www.atstake.com/research/advisories/2003/a041003-1.txt
- http://lists.apple.com/mhonarc/security-announce/msg00028.html
- http://www.atstake.com/research/advisories/2003/a041003-1.txt

---

#### 688. CVE-2003-0490

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The installation of Dantz Retrospect Client 5.0.540 on MacOS X 10.2.6, and possibly other versions, creates critical directories and files with world-writable permissions, which allows local users to gain privileges as other users by replacing programs with malicious code.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105579526026992&w=2
- http://marc.info/?l=bugtraq&m=105579526026992&w=2

---

#### 689. CVE-2003-0518

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The screen saver in MacOS X allows users with physical access to cause the screen saver to crash and gain access to the underlying session via a large number of characters in the password field, possibly triggering a buffer overflow.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2003-07/0034.html
- http://archives.neohapsis.com/archives/bugtraq/2003-07/0187.html
- http://docs.info.apple.com/article.html?artnum=120232
- http://archives.neohapsis.com/archives/bugtraq/2003-07/0034.html
- http://archives.neohapsis.com/archives/bugtraq/2003-07/0187.html

---

#### 690. CVE-2001-1412

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
nidump on MacOS X before 10.3 allows local users to read the encrypted passwords from the password file by specifying passwd as a command line argument.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://lists.insecure.org/lists/bugtraq/2002/Sep/0128.html
- http://marc.info/?l=bugtraq&m=99953038722104&w=2
- http://securitytracker.com/id?1001946
- http://www.securemac.com/macosxnidump.php

---

#### 691. CVE-2004-0169

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
QuickTime Streaming Server in MacOS X 10.2.8 and 10.3.2 allows remote attackers to cause a denial of service (crash) via DESCRIBE requests with long User-Agent fields, which causes an Assert error to be triggered in the BufferIsFull function.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://www.idefense.com/application/poi/display?id=75&type=vulnerabilities
- http://www.kb.cert.org/vuls/id/460350
- http://www.osvdb.org/6826
- http://www.osvdb.org/6837

---

#### 692. CVE-2004-1753

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
The Apple Java plugin, as used in Netscape 7.1 and 7.2, Mozilla 1.7.2, and Firefox 0.9.3 on MacOS X 10.3.5, when tabbed browsing is enabled, does not properly handle SetWindow(NULL) calls, which allows Java applets from one tab to draw to other tabs and facilitates phishing attacks that spoof tabs.

**参考链接 / References**:
- http://bugzilla.mozilla.org/show_bug.cgi?id=162134
- http://secunia.com/advisories/12392
- http://www.securityfocus.com/archive/1/373080
- http://www.securityfocus.com/archive/1/373232
- http://www.securityfocus.com/archive/1/373309

---

#### 693. CVE-2007-3184

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Cisco Trust Agent (CTA) before 2.1.104.0, when running on MacOS X, allows attackers with physical access to bypass authentication and modify System Preferences, including passwords, by invoking the Apple Menu when the Access Control Server (ACS) produces a user notification message after posture validation.

**参考链接 / References**:
- http://secunia.com/advisories/25598
- http://securityreason.com/securityalert/2796
- http://www.cisco.com/en/US/products/products_security_response09186a008085d645.html
- http://www.osvdb.org/35340
- http://www.securityfocus.com/archive/1/471041/100/0/threaded

---

#### 694. CVE-2007-6456

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in OpenOffice.org code in Planamesa NeoOffice 2.2.2 before Patch 4 has unknown impact and attack vectors related to MacOS 10.3.9 .odb files.  NOTE: it is not clear whether this issue is a vulnerability.

**参考链接 / References**:
- http://neowiki.neooffice.org/index.php/NeoOffice_Release_Notes
- http://secunia.com/advisories/28093
- http://www.securityfocus.com/bid/26878
- https://exchange.xforce.ibmcloud.com/vulnerabilities/39040
- http://neowiki.neooffice.org/index.php/NeoOffice_Release_Notes

---

#### 695. CVE-2016-4617

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves a sandbox escape related to launchctl process spawning in the "libxpc" component.

**参考链接 / References**:
- http://www.securityfocus.com/bid/96329
- https://support.apple.com/HT207170
- http://www.securityfocus.com/bid/96329
- https://support.apple.com/HT207170

---

#### 696. CVE-2016-4660

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "FontParser" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93849
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271

---

#### 697. CVE-2016-4661

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ntfs" component, which misparses disk images and allows attackers to cause a denial of service via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 698. CVE-2016-4662

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleGraphicsControl" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 699. CVE-2016-4663

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "NVIDIA Graphics Drivers" component. It allows attackers to cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 700. CVE-2016-4667

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 701. CVE-2016-4669

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (MIG code mishandling and system crash) via unspecified vectors.

**参考链接 / References**:
- http://packetstormsecurity.com/files/158874/Safari-Webkit-For-iOS-7.1.2-JIT-Optimization-Bug.html
- http://www.securityfocus.com/bid/93849
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270

---

#### 702. CVE-2016-4670

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "Security" component. It allows local users to discover lengths of arbitrary passwords by reading a log.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94433
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/94433
- https://support.apple.com/HT207271

---

#### 703. CVE-2016-4671

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds write and application crash) via a crafted PDF file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 704. CVE-2016-4673

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "CoreGraphics" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93849
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271

---

#### 705. CVE-2016-4674

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows local users to gain privileges or cause a denial of service (memory corruption and application crash) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 706. CVE-2016-4675

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libxpc" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93849
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271

---

#### 707. CVE-2016-4678

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleSMC" component. It allows local users to gain privileges or cause a denial of service (NULL pointer dereference) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086

---

#### 708. CVE-2016-4679

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libarchive" component, which allows remote attackers to write to arbitrary files via a crafted archive containing a symlink.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93849
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271

---

#### 709. CVE-2016-4681

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Core Image" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94431
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/94431
- https://support.apple.com/HT207275

---

#### 710. CVE-2016-4682

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted SGI file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93852
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207170
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/93852

---

#### 711. CVE-2016-4683

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds memory access and application crash) via a crafted SGI file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94431
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/94431
- https://support.apple.com/HT207275

---

#### 712. CVE-2016-4688

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94572
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271

---

#### 713. CVE-2016-4691

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 714. CVE-2016-4693

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which makes it easier for attackers to bypass cryptographic protection mechanisms by leveraging use of the 3DES cipher.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 715. CVE-2016-4721

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "IDS - Connectivity" component, which allows man-in-the-middle attackers to spoof calls via a "switch caller" notification.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94429
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/94429
- https://support.apple.com/HT207271

---

#### 716. CVE-2016-4780

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Thunderbolt" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (NULL pointer dereference) via a crafted app.

**参考链接 / References**:
- https://support.apple.com/HT207275
- https://support.apple.com/HT207275

---

#### 717. CVE-2016-7577

**严重程度 / Severity**: LOW | CVSS: 3.7

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "FaceTime" component, which allows remote attackers to trigger memory corruption and obtain audio data from a call that appeared to have ended.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94429
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275
- http://www.securityfocus.com/bid/94429
- https://support.apple.com/HT207271

---

#### 718. CVE-2016-7579

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. The issue involves the "CFNetwork Proxies" component, which allows man-in-the-middle attackers to spoof a proxy password authentication requirement and obtain sensitive information.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93856
- http://www.securitytracker.com/id/1037086
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275

---

#### 719. CVE-2016-7580

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Mail" component, which allows remote web servers to cause a denial of service via a crafted URL.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94434
- https://support.apple.com/HT207170
- http://www.securityfocus.com/bid/94434
- https://support.apple.com/HT207170

---

#### 720. CVE-2016-7582

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94435
- https://support.apple.com/HT207170
- http://www.securityfocus.com/bid/94435
- https://support.apple.com/HT207170

---

#### 721. CVE-2016-7584

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "AppleMobileFileIntegrity" component, which allows remote attackers to spoof signed code by using a matching team ID.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94571
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275

---

#### 722. CVE-2016-7588

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreMedia Playback" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted MP4 file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 723. CVE-2016-7591

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOHIDFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 724. CVE-2016-7594

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ICU" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 725. CVE-2016-7595

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreText" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 726. CVE-2016-7596

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 727. CVE-2016-7600

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "OpenPAM" component, which allows local users to obtain sensitive information by leveraging mishandling of failed PAM authentication by a sandboxed app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 728. CVE-2016-7602

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 729. CVE-2016-7603

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreStorage" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 730. CVE-2016-7604

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreCapture" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 731. CVE-2016-7605

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to cause a denial of service (NULL pointer dereference) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 732. CVE-2016-7606

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 733. CVE-2016-7607

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows attackers to obtain sensitive information from kernel memory via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 734. CVE-2016-7608

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOFireWireFamily" component, which allows local users to obtain sensitive information from kernel memory via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 735. CVE-2016-7609

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "AppleGraphicsPowerManagement" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 736. CVE-2016-7612

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 737. CVE-2016-7613

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app that leverages object-lifetime mishandling during process spawning.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94116
- https://support.apple.com/HT207269
- https://support.apple.com/HT207270
- https://support.apple.com/HT207271
- https://support.apple.com/HT207275

---

#### 738. CVE-2016-7615

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows local users to cause a denial of service via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 739. CVE-2016-7616

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Disk Images" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 740. CVE-2016-7617

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (type confusion) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- https://www.exploit-db.com/exploits/40952/
- http://www.securityfocus.com/bid/94903

---

#### 741. CVE-2016-7618

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Foundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 742. CVE-2016-7619

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "libarchive" component, which allows local users to write to arbitrary files via vectors related to symlinks.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 743. CVE-2016-7620

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOSurface" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 744. CVE-2016-7621

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 745. CVE-2016-7622

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Grapher" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 746. CVE-2016-7624

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOAcceleratorFamily" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 747. CVE-2016-7625

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 748. CVE-2016-7627

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreGraphics" component. It allows attackers to cause a denial of service (NULL pointer dereference and application crash) via a crafted font.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 749. CVE-2016-7628

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Assets" component, which allows local users to bypass intended permission restrictions and change a downloaded mobile asset via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 750. CVE-2016-7629

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "kext tools" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469

---

#### 751. CVE-2016-7633

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Directory Services" component. It allows local users to gain privileges or cause a denial of service (use-after-free) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94903
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207423
- https://www.exploit-db.com/exploits/40954/
- http://www.securityfocus.com/bid/94903

---

#### 752. CVE-2016-7636

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows man-in-the-middle attackers to cause a denial of service (application crash) via vectors related to OCSP responder URLs.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 753. CVE-2016-7637

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to gain privileges or cause a denial of service (memory corruption) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 754. CVE-2016-7643

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information from process memory or cause a denial of service (out-of-bounds read and application crash) via a crafted web site.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 755. CVE-2016-7644

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94904
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 756. CVE-2016-7655

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreMedia External Displays" component. It allows local users to gain privileges or cause a denial of service (type confusion) via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94906
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- http://www.securityfocus.com/bid/94906

---

#### 757. CVE-2016-7657

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows attackers to obtain sensitive information from kernel memory via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 758. CVE-2016-7658

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 759. CVE-2016-7659

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 760. CVE-2016-7660

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "syslog" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 761. CVE-2016-7661

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "Power Management" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94906
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://www.exploit-db.com/exploits/40931/

---

#### 762. CVE-2016-7662

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows remote attackers to spoof certificates via unspecified vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 763. CVE-2016-7663

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreFoundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted string.

**参考链接 / References**:
- http://www.securityfocus.com/bid/94905
- http://www.securitytracker.com/id/1037469
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487

---

#### 764. CVE-2016-7667

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to cause a denial of service via a crafted string.

**参考链接 / References**:
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423

---

#### 765. CVE-2016-7714

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**参考链接 / References**:
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423
- https://support.apple.com/HT207487
- https://support.apple.com/HT207422
- https://support.apple.com/HT207423

---

#### 766. CVE-2016-7742

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "xar" component, which allows remote attackers to execute arbitrary code via a crafted archive that triggers use of uninitialized memory locations.

**参考链接 / References**:
- https://support.apple.com/HT207423
- https://support.apple.com/HT207423

---

#### 767. CVE-2016-7761

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "WiFi" component, which allows local users to obtain sensitive network-configuration information by leveraging global storage.

**参考链接 / References**:
- https://support.apple.com/HT207423
- https://support.apple.com/HT207423

---

#### 768. CVE-2017-2353

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/95723
- http://www.securitytracker.com/id/1037671
- https://support.apple.com/HT207483
- https://www.exploit-db.com/exploits/41164/
- http://www.securityfocus.com/bid/95723

---

#### 769. CVE-2017-2357

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "IOAudioFamily" component. It allows attackers to obtain sensitive kernel memory-layout information via a crafted app.

**参考链接 / References**:
- http://www.securityfocus.com/bid/95723
- http://www.securitytracker.com/id/1037671
- https://support.apple.com/HT207483
- http://www.securityfocus.com/bid/95723
- http://www.securitytracker.com/id/1037671

---

#### 770. CVE-1999-1131

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in OSF Distributed Computing Environment (DCE) security demon (secd) in IRIX 6.4 and earlier allows attackers to cause a denial of service via a long principal, group, or organization.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/19980601-01-PX
- http://ciac.llnl.gov/ciac/bulletins/i-060.shtml
- http://www.cert.org/vendor_bulletins/VB-97.12.opengroup
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1123
- ftp://patches.sgi.com/support/free/security/advisories/19980601-01-PX

---

#### 771. CVE-1999-0871

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Internet Explorer 4.0 and 4.01 allow a remote attacker to read files via IE's cross frame security, aka the "Cross Frame Navigate" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/7837
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-013
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3668
- http://www.osvdb.org/7837
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-013

---

#### 772. CVE-1999-0531

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "An SMTP service supports EXPN, VRFY, HELP, ESMTP, and/or EHLO.

---

#### 773. CVE-1999-0578

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
A Windows NT system's registry audit policy does not log an event success or failure for security-critical registry keys.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228

---

#### 774. CVE-1999-0614

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The FTP service is running.

---

#### 775. CVE-1999-0615

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The SNMP service is running.

---

#### 776. CVE-1999-0616

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The TFTP service is running.

---

#### 777. CVE-1999-0617

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The SMTP service is running.

---

#### 778. CVE-1999-0619

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The Telnet service is running.

---

#### 779. CVE-1999-0620

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A component service related to NIS is running.

---

#### 780. CVE-1999-0621

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A component service related to NETBIOS is running.

---

#### 781. CVE-1999-0622

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A component service related to DNS service is running.

---

#### 782. CVE-1999-0623

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The X Windows service is running.

---

#### 783. CVE-1999-0631

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The NFS service is running.

---

#### 784. CVE-1999-0633

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The HTTP/WWW service is running.

---

#### 785. CVE-1999-0634

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The SSH service is running.

---

#### 786. CVE-1999-0642

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A POP service is running.

---

#### 787. CVE-1999-0643

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The IMAP service is running.

---

#### 788. CVE-1999-0644

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The NNTP news service is running.

---

#### 789. CVE-1999-0645

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The IRC service is running.

---

#### 790. CVE-1999-0646

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The LDAP service is running.

---

#### 791. CVE-1999-0647

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The bootparam (bootparamd) service is running.

---

#### 792. CVE-1999-0648

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The X25 service is running.

---

#### 793. CVE-1999-0649

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The FSP service is running.

---

#### 794. CVE-1999-0652

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A database service is running, e.g. a SQL server, Oracle, or mySQL.

---

#### 795. CVE-1999-0658

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "DCOM is running.

---

#### 796. CVE-1999-0659

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A Windows NT Primary Domain Controller (PDC) or Backup Domain Controller (BDC) is present.

---

#### 797. CVE-1999-0382

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The screen saver in Windows NT does not verify that its security context has been changed properly, allowing attackers to run programs with elevated privileges.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-008
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-008

---

#### 798. CVE-1999-1370

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The setup wizard (ie5setup.exe) for Internet Explorer 5.0 disables (1) the screen saver, which could leave the system open to users with physical access if a failure occurs during an unattended installation, and (2) the Task Scheduler Service, which might prevent the scheduled execution of security-critical programs.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92220197414799&w=2
- http://marc.info/?l=ntbugtraq&m=92220197414799&w=2

---

#### 799. CVE-1999-0488

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 4.0 and 5.0 allows a remote attacker to execute security scripts in a different security context using malicious URLs, a variant of the "cross frame" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012

---

#### 800. CVE-1999-1241

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Internet Explorer, with a security setting below Medium, allows remote attackers to execute arbitrary commands via a malicious web page that uses the FileSystemObject ActiveX object.

**参考链接 / References**:
- http://oliver.efri.hr/~crv/security/bugs/NT/activex4.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2173
- http://oliver.efri.hr/~crv/security/bugs/NT/activex4.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2173

---

#### 801. CVE-1999-1394

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
BSD 4.4 based operating systems, when running at security level 1, allow the root user to clear the immutable and append-only flags for files by unmounting the file system and using a file system editor such as fsdb to directly modify the file through a device.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93094058620450&w=2
- http://www.securityfocus.com/bid/510
- http://marc.info/?l=bugtraq&m=93094058620450&w=2
- http://www.securityfocus.com/bid/510

---

#### 802. CVE-1999-0721

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Denial of service in Windows NT Local Security Authority (LSA) through a malformed LSA request.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231457
- http://www.ciac.org/ciac/bulletins/j-049.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-020
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231457
- http://www.ciac.org/ciac/bulletins/j-049.shtml

---

#### 803. CVE-1999-1356

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Compaq Integration Maintenance Utility as used in Compaq Insight Manager agent before SmartStart 4.50 modifies the legal notice caption (LegalNoticeCaption) and text (LegalNoticeText) in Windows NT, which could produce a legal notice that is in violation of the security policy.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93646669500991&w=2
- http://marc.info/?l=ntbugtraq&m=93637792706047&w=2
- http://marc.info/?l=ntbugtraq&m=93759822830815&w=2
- http://www.iss.net/security_center/static/7763.php
- http://marc.info/?l=bugtraq&m=93646669500991&w=2

---

#### 804. CVE-1999-0886

**严重程度 / Severity**: N/A | CVSS: 9.0

**漏洞描述 / Description**:
The security descriptor for RASMAN allows users to point to an alternate location via the Windows NT Service Control Manager.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ242294
- http://www.securityfocus.com/bid/645
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-041
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ242294
- http://www.securityfocus.com/bid/645

---

#### 805. CVE-1999-1111

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in StackGuard before 1.21 allows remote attackers to bypass the Random and Terminator Canary security mechanisms by using a non-linear attack which directly modifies a pointer to a return address instead of using a buffer overflow to reach the return address entry itself.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94218618329838&w=2
- http://www.securityfocus.com/bid/786
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3524
- http://marc.info/?l=bugtraq&m=94218618329838&w=2
- http://www.securityfocus.com/bid/786

---

#### 806. CVE-1999-0995

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Windows NT Local Security Authority (LSA) allows remote attackers to cause a denial of service via malformed arguments to the LsaLookupSids function which looks up the SID, aka "Malformed Security Identifier Request."

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248185
- http://www.securityfocus.com/bid/875
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-057
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248185
- http://www.securityfocus.com/bid/875

---

#### 807. CVE-2000-0028

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Internet Explorer 5.0 and 5.01 allows remote attackers to bypass the cross frame security policy and read files via the external.NavigateAndFind function.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0028
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0028

---

#### 808. CVE-1999-1094

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Internet Explorer 4.01 and earlier allows remote attackers to execute arbitrary commands via a long URL with the "mk:" protocol, aka the "MK Overrun security issue."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=88480839506155&w=2
- http://support.microsoft.com/support/kb/articles/q176/6/97.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/917
- http://marc.info/?l=bugtraq&m=88480839506155&w=2
- http://support.microsoft.com/support/kb/articles/q176/6/97.asp

---

#### 809. CVE-2000-0061

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Internet Explorer 5 does not modify the security zone for a document that is being loaded into a window until after the document has been loaded, which could allow remote attackers to execute Javascript in a different security context while the document is loading.

**参考链接 / References**:
- http://www.securityfocus.com/bid/923
- http://www.securityfocus.com/bid/923

---

#### 810. GHSA-88hf-wf7h-7w4m - OpenTelemetry's Zipkin remote endpoint cache could grow without bounds and incre

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
[GitHub] ### Summary

The Zipkin exporter remote endpoint cache accepted unbounded key growth derived from span attributes. In high-cardinality scenarios, this could increase process memory usage over time and degrade availability.

### Details

- Introduce a bounded, thread-safe LRU cache for remote endpoints.
- Enforce fixed maximum size to prevent unbounded growth.

### Impact

- A process using Zipkin export for client/producer spans could experience avoidable memory growth under sustained unique rem

**参考链接 / References**:
- https://github.com/advisories/GHSA-88hf-wf7h-7w4m

---

#### 811. GHSA-hrmw-qprp-wgmc - PhpSpreadsheet has XSS via number format code with @ text placeholder bypasses h

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
[GitHub] It was discovered that there is a way to bypass HTML escaping in the HTML writer using custom number format codes.

## The Problem

In `Writer/Html.php` around line 1592, the code checks if the formatted cell data equals the original data to decide whether to apply `htmlspecialchars()`:

```php
if ($cellData === $origData) {
    $cellData = htmlspecialchars($cellData, ...);
}
```

When a cell has a custom number format containing `@` (text placeholder) with any additional literal characters, the

**参考链接 / References**:
- https://github.com/advisories/GHSA-hrmw-qprp-wgmc

---

#### 812. GHSA-vp29-5652-4fw9 - CoreDNS has TSIG authentication bypass on gRPC and QUIC transports

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ### Summary

The gRPC, QUIC, DoH, and DoH3 transports in CoreDNS incorrectly handle TSIG authentication.

For gRPC and QUIC, CoreDNS checks whether the TSIG key name exists in the config, but does not actually verify the TSIG HMAC. If the key name matches, `tsigStatus` remains nil and the tsig plugin treats the request as "verified".

For DoH and DoH3, the issue is worse: TSIG is not verified at all. The DoH response writer has `TsigStatus()` hardcoded to return nil, so any request containing a

**参考链接 / References**:
- https://github.com/advisories/GHSA-vp29-5652-4fw9

---

#### 813. GHSA-6wpp-88cp-7q68 - PhpSpreadsheet has XSS via NumberFormat @ Text Substitution in HTML Writer

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub] ### Summary
The HTML Writer in PhpSpreadsheet bypasses `htmlspecialchars()` output escaping when a cell uses a custom number format containing the `@` text placeholder with additional literal text (e.g., `@ "items"` or `"Total: "@`). This allows an attacker to inject arbitrary HTML and JavaScript into the generated HTML output by crafting a malicious XLSX file.

### Details


#### 1. Conditional escaping in `Html.php:1586-1594`

```php
$cellData = NumberFormat::toFormattedString(
    $origData2,

**参考链接 / References**:
- https://github.com/advisories/GHSA-6wpp-88cp-7q68

---

#### 814. GHSA-qhmp-q7xh-99rh - CoreDNS has TSIG authentication bypass on DoT, DoH, DoH3, DoQ, and gRPC

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ### Summary
CoreDNS' tsig plugin can be bypassed on non-plain-DNS transports because it trusts the transport writer's TsigStatus() instead of performing verification itself. In the attached PoC, plain DNS/TCP correctly rejects an invalid TSIG (NOTAUTH), while the same invalid-TSIG request is accepted over DoT (tls://) and DoH (https://), allowing a client without the shared secret to satisfy require all. The same bug class affects DoH3, DoQ, and gRPC.

### Details
The tsig plugin decides whether

**参考链接 / References**:
- https://github.com/advisories/GHSA-qhmp-q7xh-99rh

---

#### 815. GHSA-h8mm-c463-wjq3 - CoreDNS' transfer stanza selection uses lexicographic compare (subzone ACL bypas

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ### Summary
CoreDNS' transfer plugin can select the wrong ACL stanza when both a parent zone and a more-specific subzone are configured. A permissive parent-zone transfer rule can override a restrictive subzone rule (name-dependent), allowing an unauthorized client to perform AXFR/IXFR for the subzone and retrieve its zone contents.

### Details
In plugin/transfer/transfer.go, stanza selection is implemented by longestMatch(), which is documented as "longest zone match wins", but it actually cho

**参考链接 / References**:
- https://github.com/advisories/GHSA-h8mm-c463-wjq3

---

#### 816. GHSA-63cw-r7xf-jmwr - CoreDNS DoH GET oversized dns= query parameter causes pre-validation CPU and mem

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ### Summary

CoreDNS's DNS-over-HTTPS (DoH) GET path accepts oversized `dns=` query values and performs substantial request parsing, query unescaping, base64 decoding, and message unpacking work before returning `400 Bad Request`.

A remote, unauthenticated attacker can repeatedly send oversized DoH GET requests to `/dns-query?dns=...` and force high CPU usage, large transient allocations, elevated garbage-collection pressure, and increased resident memory consumption even though the requests ar

**参考链接 / References**:
- https://github.com/advisories/GHSA-63cw-r7xf-jmwr

---

#### 817. GHSA-2wpx-qpw2-g5h5 - CoreDNS' DoQ worker pool does not bound stream backlog

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ### Summary
CoreDNS' DNS-over-QUIC (DoQ) server can be driven into large goroutine and memory growth by a remote client that opens many QUIC streams and stalls after sending only 1 byte. Even with a small configured quic { worker_pool_size ... }, CoreDNS still spawns a goroutine per accepted stream (workers + waiters) and active workers can block indefinitely in io.ReadFull() with no per-stream read deadline, enabling unauthenticated remote DoS via memory exhaustion/OOM-kill.

### Details
CoreDN

**参考链接 / References**:
- https://github.com/advisories/GHSA-2wpx-qpw2-g5h5

---

#### 818. GHSA-pp79-hqv6-vmc3 - FacturaScripts has Insecure Parameter Handling: Unauthorized Modification of Imm

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
[GitHub] ### Summary
The application fails to validate the ```nick``` parameter during a ```POST``` request to the ```EditUser``` controller. Although the UI prevents editing this field, a user can bypass this restriction using a proxy to rename any account (including the Administrator). This leads to Broken Access Control and potential Audit Log Corruption.

### Details
The vulnerability exists in the user update logic. When a ```POST``` request is sent to ```/EditUser```, the backend processes the ```n

**参考链接 / References**:
- https://github.com/advisories/GHSA-pp79-hqv6-vmc3

---

#### 819. GHSA-35hp-hqmv-8qg8 - Fiber's cache middleware default key generator ignores query string, causing res

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
[GitHub] ### Summary
Fiber cache middleware's default key generator uses only `c.Path()` and does not include the query string.
As a result, requests like `/?id=1` and `/?id=2` can map to the same cache key and share the same cached response.

This can cause response mix-up (cache poisoning-like behavior) for endpoints where response content depends on query parameters.

### Details
Default configuration in cache middleware:

- `KeyGenerator: func(c fiber.Ctx) string { return utils.CopyString(c.Path()) }

**参考链接 / References**:
- https://github.com/advisories/GHSA-35hp-hqmv-8qg8

---

#### 820. CVE-2024-1708 - ConnectWise ScreenConnect Path Traversal Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA] Vendor: ConnectWise, Product: ScreenConnect. Due: 2026-05-12.

**参考链接 / References**:
- https://nvd.nist.gov/vuln/detail/CVE-2024-1708

---

#### 821. CVE-2026-32202 - Microsoft Windows Protection Mechanism Failure Vulnerability

**严重程度 / Severity**: KEV

**漏洞描述 / Description**:
[CISA] Vendor: Microsoft, Product: Windows. Due: 2026-05-12.

**参考链接 / References**:
- https://nvd.nist.gov/vuln/detail/CVE-2026-32202

---

#### 822. [安全客] 安全进入“AI自主攻击”时代，瑞数信息如何用AI对抗AI

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315417

---

#### 823. [安全客] 智能体关键年：Agent扎根业务流，AI生产力正在形成

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315419

---

#### 824. [安全客] 深度分析Sorry勒索软件的加密实现与行为特征

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315390

---

#### 825. [安全客] 科技云报到：当AI闯入特教行业，一场颠覆变革正在发生！

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315341

---

#### 826. [安全客] 科技云报到：AI云，逻辑变了吗？

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315337

---

#### 827. [安全客] 工程化实战思维在红队技战术中的应用

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315292

---

#### 828. [安全客] 鸿蒙NEXT应用一键加固——AI Agent助力安全开发

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315277

---

#### 829. [安全客] 科技云报到：AI算力革命，终结云计算20年降价史

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315253

---

#### 830. [安全客] 科技云报到：“龙虾”入笼：为何金融行业不敢“养”？

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315234

---

#### 831. [安全客] 科技云报到：“龙虾”OpenClaw狂欢之下，需要一针清醒剂

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315195

---

#### 832. [安全客] 瑞数信息入选IDC两大AI安全报告，防御OpenClaw小龙虾裸奔危机

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315209

---

#### 833. [安全客] 2026首届汽车安全白帽黑客大会圆满收官，共筑车联网安全新生态

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315197

---

#### 834. [安全客] Ally WordPress插件高危SQL注入漏洞 威胁40万个网站

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315140

---

#### 835. [安全客] OpenAI战略调整Sora视频AI将直接接入ChatGPT

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315145

---

#### 836. [安全客] HPE发布Aruba OS高危漏洞预警 可未授权重置密码

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
N/A

**参考链接 / References**:
- https://www.anquanke.com/post/id/315148

---

#### 837. [先知] 面向大模型隐私推理的安全协议-MPC与ZK的角色分工

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
面向大模型隐私推理的安全协议-MPC与ZK的角色分工

**参考链接 / References**:
- https://xz.aliyun.com/news/92061

---

#### 838. [先知] Agentic / Context

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
Agentic / Context

**参考链接 / References**:
- https://xz.aliyun.com/news/92060

---

#### 839. [先知] AI洪流下的防守对抗新范式

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
AI洪流下的防守对抗新范式

**参考链接 / References**:
- https://xz.aliyun.com/news/92059

---

#### 840. [先知] LLM 能帮一个安全工程师干些什么

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
LLM 能帮一个安全工程师干些什么

**参考链接 / References**:
- https://xz.aliyun.com/news/92058

---

#### 841. [先知] AI For Security：AI在云产品安全建设中能做什么？

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
AI For Security：AI在云产品安全建设中能做什么？

**参考链接 / References**:
- https://xz.aliyun.com/news/92056

---

#### 842. [先知] 2026DCIC数字中国创新大赛网安赛道初赛部分题解

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
比赛部分题解

**参考链接 / References**:
- https://xz.aliyun.com/news/92044

---

#### 843. [先知] interactive-process-mcp：让 AI Agent 拥有交互式终端能力

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
当我们在终端里工作时，大量操作本质上是多轮交互的过程——SSH 登录服务器需要先输入密码，再执行命令；Python REPL 中逐行调试代码，每一步都依赖上一步的结果；交互式安装程序不时弹出 [Y/n] 提示等待回应。这些场景对人类来说稀松平常，但对于 AI Agent 而言却是一道难题：它们原生只能执行一次性命令，运行完毕立刻返回结果，无法在多个对话轮次中持续地读写同一个进程。 intera

**参考链接 / References**:
- https://xz.aliyun.com/news/92043

---

#### 844. [先知] 内网渗透靶场之春秋云镜-Brute4Road【详细解析】

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
靶标介绍： Brute4Road是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有4个flag，分布于不同的靶机。

**参考链接 / References**:
- https://xz.aliyun.com/news/92042

---

#### 845. [先知] 我做了一个用自然语言挖漏洞的 AI 渗透工具：VulnClaw

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
记得以前做渗透，信息收集要开一堆工具，漏洞利用要自己找 POC，报告写完一天没了。 最近写了一个 CLI 工具 VulnClaw，把这个流程串起来了： 自然语言输入 → AI 理解意图 → MCP 工具链 → 全自动渗透 → 自动出报告。 GitHub 开源，MIT 协议，欢迎试用。

**参考链接 / References**:
- https://xz.aliyun.com/news/92040

---

#### 846. [先知] 中转钓鱼攻击劫持 opencode，claudecode，openclaw

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
通过构造恶意的中转站来劫持 opencode，claudecode，openclaw 从而实现命令执行，乃至于上线 c2

**参考链接 / References**:
- https://xz.aliyun.com/news/92038

---

#### 847. [嘶吼] 纵横网络靶场社区正式发布 以虚实融合技术构建工业信息安全实战生态

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
当前，工业互联网深度融合发展，关键信息基础设施安全防护需求持续攀升，实战型工业信息安全人才短缺、训练场景稀缺、理论与实践脱节等制约行业发展的核心痛点日益凸显。 在此背景下，烽台科技打造的聚焦工业信息安全人才培养与生态共建的纵横网络靶场社区正式发布。该平台依托烽台科技十余年工业靶场技术沉淀，以“虚实融合”技术为核心，整合AI智能体、数字孪生等前沿能力，旨在打造工业安全领域“理论+实战+生态”三位一体的服务体系，为高校、企业、科研院所提供专业化的工业安全实训与技术交流空间。 从“竞赛工具”到“生态平台”：网络靶场社区的迭代之路 回溯烽台科技网络靶场社区的发展历程，其起点可追溯至2015年——公司成

**参考链接 / References**:
- https://www.4hou.com/posts/nXQ5

---

#### 848. [嘶吼] 梆梆安全发布《2026年Q1移动应用安全风险报告》：超八成APP存隐私违规，数据境外外发风险需高度警惕

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
梆梆安全发布《2026年Q1移动应用安全风险报告》。本报告基于梆梆安全移动应用监管平台在2026年一季度的威胁监测数据与深度安全分析成果，系统梳理当前国内移动应用面临的新型攻击技术演进与安全趋势变化，聚焦盗版仿冒、境外数据传输、高危漏洞、个人隐私违规等多个维度，为移动应用安全建设工作提供参考与实践指引。 当前，我国数字经济与实体经济融合持续深入，移动互联网已演进为支撑社会数字化转型的关键基础设施。根据中国互联网络信息中心（CNNIC）第57次《中国互联网络发展状况统计报告》，截至2025年12月，我国网民规模达11.25亿，互联网普及率突破80%，其中手机网民规模达11.21亿，占比高达99.

**参考链接 / References**:
- https://www.4hou.com/posts/pKwQ

---

#### 849. [嘶吼] 公安部通报37款违规应用，电商类占比超七成，小程序不再是 “法外之地”

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
依据《网络安全法》《个人信息保护法》等法律法规，经公安部计算机信息系统安全产品质量监督检验中心检测，37款移动应用存在违法违规收集使用个人信息情况，具体通报如下： 1、未公开收集使用规则。涉及21款移动应用如下： 《奇峰商城》（支付宝小程序）、《聚优商城》（微信小程序）、《亿秀分期商城》（支付宝小程序）、《鲜范商城》（微信小程序）、《京机数码手机商城》（支付宝小程序）、《创维官方商城》（支付宝小程序）、《万事商城》（支付宝小程序）、《尚至然商城》（支付宝小程序）、《知墨商城》（支付宝小程序）、《领充充电桩商城》（支付宝小程序）、《世有品商城》（支付宝小程序）、《阿京妈会员》（微信小程序）、《仲

**参考链接 / References**:
- https://www.4hou.com/posts/PGXA

---

#### 850. [嘶吼] Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
最新发现，企业级安全文件传输解决方案 Progress ShareFile 存在两处漏洞，攻击者可将其组合利用，在无需身份认证的情况下从受影响环境中窃取文件。Progress ShareFile 是一款文档共享与协作产品，广泛应用于大中型企业。 此类文件传输平台历来是勒索软件团伙的重点攻击目标，此前 Clop 勒索组织就曾利用 Accellion FTA、SolarWinds Serv-U、Gladinet CentreStack、GoAnywhere MFT、MOVEit Transfer、Cleo 等产品中的漏洞实施大规模数据窃取攻击。 watchTowr 的研究人员在 Progress

**参考链接 / References**:
- https://www.4hou.com/posts/MXOm

---

#### 851. [嘶吼] 嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
嘶吼安全动态| 【国内新闻】 八部门联合发布《科技数据安全管理暂行规定》，4月10日起实施 摘要：明确科技数据分类分级、算法备案、跨境管控等要求，强化科研与算力设施安全。 原文链接： http://m.toutiao.com/group/7626936382984700451/ 腾讯QClaw V2上线“龙虾管家”，全流程防护AI操作安全 摘要：默认开启安全防护，覆盖Prompt、技能与脚本执行，实时拦截恶意指令、技能投毒、文件误删等风险。 原文链接： https://www.sohu.com/a/1007377777_115060?scm=10001.325_13-325_13.0.0-0-

**参考链接 / References**:
- https://www.4hou.com/posts/8gPj

---

#### 852. [嘶吼] 新型CrystalRAT恶意软件新增远程控制、数据窃取等功能

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
一款名为CrystalRAT的新型远程控制木马正在Telegram上以恶意软件即服务（MaaS）模式推广，提供远程控制、数据窃取、键盘记录与剪贴板劫持等核心功能。 该恶意软件于今年1月现身，采用分级订阅模式运营。除Telegram频道外，运营者还在YouTube开设专门营销账号，通过功能演示视频进行推广。 卡巴斯基研究人员在最近发布的报告中指出，这款木马与WebRAT（Salat窃密木马）高度相似，二者拥有相同的控制面板设计、均使用Go语言编写，且采用类似的机器人销售系统。 CrystalX还内置了大量恶作剧功能，用于骚扰用户或干扰其正常工作。尽管带有“娱乐化”外观，该木马仍具备全面且强大的数

**参考链接 / References**:
- https://www.4hou.com/posts/LGMD

---

#### 853. [嘶吼] 嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
嘶吼安全动态 【国内新闻】 上海人工智能实验室发布“珠穆朗玛计划”，打造AI4S全国中枢 摘要：上海AI实验室重磅发布“AGI4S 珠穆朗玛计划”，同步推出DeepLink融合算力平台。该计划旨在通过全维度合作打破算力与数据壁垒，为高能物理、疾病诊断等关键科学领域提供自主受控的智能底座。 原文链接： https://www.news.cn/tech/20260408/fe5a61186ceb4582bdcf019c9abe0733/c.html 中央网信办召开全国网络法治工作会议，部署 “十五五” 依法治网重点任务 摘要：会议明确完善网络法律体系、强化App/SDK个人信息治理、加强网络司法惩

**参考链接 / References**:
- https://www.4hou.com/posts/6MLO

---

#### 854. [嘶吼] “龙虾”来袭，绿盟科技三位一体防御体系，让网络告别 “裸奔” 风险

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
2026年开年，OpenClaw（俗称“龙虾”）这款本地优先的 AI Agent 自动化平台以燎原之势席卷全球，凭借自然语言指令实现 PC 全功能自动化的能力，成为开发者追捧的工具。其支持15+通信平台、多模型调用、自主任务执行等特性，让效率提升的同时，也埋下了巨大的安全隐患。工信部于2026年3月8日正式发布openclaw安全风险预警通报。这款看似便捷的工具，正成为企业网络安全的“特洛伊木马”，筑牢其安全防护防线已成为企业的迫切需求。 一、OpenClaw 五大核心安全痛点，直击企业网络软肋 OpenClaw 的安全风险并非单一漏洞引发的局部问题，而是贯穿系统架构、权限模型、供应链和数据流

**参考链接 / References**:
- https://www.4hou.com/posts/5MJY

---

#### 855. [嘶吼] 当“小龙虾”潜入内网，如何解决“影子AI”的隐匿危机

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
近期，OpenClaw（俗称“小龙虾”）这一开源AI智能体因其强大的自主执行能力而迅速爆火，成为众多企业与开发者的效率神器。然而，就在热度持续攀升之际，国家及行业权威机构接连发布重磅预警：这个看似能干的“AI助手”，正因其模糊的信任边界和脆弱的默认安全配置，成为潜伏在企业内网中的高危风险源。 从已披露的CVE-2026-25253、CVE-2026-25157到最新的多个供应链投毒事件，多个已知漏洞正威胁着从个人隐私到关键基础设施的安全防线。面对来势汹汹的“龙虾”漏洞潮，传统“只扫不治”的扫描模式已然失效。企业需要的不是一份简单的风险清单，而是一套可管、可控、可追溯的漏洞治理方案。 一、治理之

**参考链接 / References**:
- https://www.4hou.com/posts/42E7

---

#### 856. [嘶吼] 绿盟NF防火墙：筑牢OpenClaw安全防线，构筑AI时代安全基石

**严重程度 / Severity**: INFO

**漏洞描述 / Description**:
2026年2月至3月，国家工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）连续两次发布关于OpenClaw（俗称“龙虾”）的安全预警，明确指出其“信任边界模糊”“配置缺陷易引发网络攻击、信息泄露”，并首次提出针对AI智能体应用的 “六要六不要” 安全建议。紧接着，国家安全部也发布《“龙虾”安全养殖手册》，警示主机被接管、数据被窃取、供应链投毒等原生风险。 官方密集发声的背后，是一组触目惊心的数据： · 258个已披露漏洞，其中近期发现的82个漏洞里就有12个超危以及21个高危； · 46.9万个公网暴露实例，27.2%的实例存在高危漏洞，面临被直接接管风险； · 22% 受监控企业存在

**参考链接 / References**:
- https://www.4hou.com/posts/33BA

---

#### 857. CVE-2000-0200

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Buffer overflow in Microsoft Clip Art Gallery allows remote attackers to cause a denial of service or execute commands via a malformed CIL (clip art library) file, aka the "Clip Art Buffer Overrun" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1034
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-015
- http://www.securityfocus.com/bid/1034
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-015

---

#### 858. CVE-2000-0202

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and Microsoft Data Engine (MSDE) 1.0 allow remote attackers to gain privileges via a malformed Select statement in an SQL query.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-014
- http://www.securityfocus.com/bid/1041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-014

---

#### 859. CVE-2000-0199

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
When a new SQL Server is registered in Enterprise Manager for Microsoft SQL Server 7.0 and the "Always prompt for login name and password" option is not set, then the Enterprise Manager uses weak encryption to store the login ID and password.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1055
- http://www.securityfocus.com/bid/1055

---

#### 860. CVE-2000-0228

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media License Manager allows remote attackers to cause a denial of service by sending a malformed request that causes the manager to halt, aka the "Malformed Media License Request" Vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1058
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-016
- http://www.securityfocus.com/bid/1058
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-016

---

#### 861. CVE-2000-0232

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft TCP/IP Printing Services, aka Print Services for Unix, allows an attacker to cause a denial of service via a malformed TCP/IP print request.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html
- http://www.securityfocus.com/bid/1082
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-021
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html
- http://www.securityfocus.com/bid/1082

---

#### 862. CVE-2000-0302

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to view the source code of ASP files by appending a %20 to the filename in the CiWebHitsFile argument to the null.htw URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=95453598317340&w=2
- http://www.osvdb.org/271
- http://www.securityfocus.com/bid/1084
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- http://marc.info/?l=bugtraq&m=95453598317340&w=2

---

#### 863. CVE-2000-0277

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 does not warn the user when executing Excel Macro Language (XLM) macros in external text files, which could allow an attacker to execute a macro virus, aka the "XLM Text Macro" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/1272
- http://www.securityfocus.com/bid/1087
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-022
- http://www.osvdb.org/1272
- http://www.securityfocus.com/bid/1087

---

#### 864. CVE-2000-0260

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the dvwssr.dll DLL in Microsoft Visual Interdev 1.0 allows users to cause a denial of service or execute commands, aka the "Link View Server-Side Component" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/282
- http://www.securityfocus.com/bid/1109
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-025
- http://www.osvdb.org/282
- http://www.securityfocus.com/bid/1109

---

#### 865. CVE-2000-1218

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The default configuration for the domain name resolver for Microsoft Windows 98, NT 4.0, 2000, and XP sets the QueryIpMatching parameter to 0, which causes Windows to accept DNS updates from hosts that it did not query, which allows remote attackers to poison the DNS cache.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/458659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4280
- http://www.kb.cert.org/vuls/id/458659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4280

---

#### 866. CVE-2000-0331

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft command processor (CMD.EXE) for Windows NT and Windows 2000 allows a local user to cause a denial of service via a long environment variable, aka the "Malformed Environment Variable" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html
- http://www.securityfocus.com/bid/1135
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-027
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html
- http://www.securityfocus.com/bid/1135

---

#### 867. CVE-2000-0304

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS 4.0 and 5.0 with the IISADMPWD virtual directory installed allows a remote attacker to cause a denial of service via a malformed request to the inetinfo.exe program, aka the "Undelimited .HTR Request" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1191
- http://xforce.iss.net/alerts/advise52.php3
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-031
- http://www.securityfocus.com/bid/1191
- http://xforce.iss.net/alerts/advise52.php3

---

#### 868. CVE-2000-0400

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Active Movie ActiveX Control in Internet Explorer 5 does not restrict which file types can be downloaded, which allows an attacker to download any type of file to a user's system by encoding it within an email message or news post.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=95868514521257&w=2
- http://www.securityfocus.com/bid/1221
- http://marc.info/?l=bugtraq&m=95868514521257&w=2
- http://www.securityfocus.com/bid/1221

---

#### 869. CVE-2000-0402

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Mixed Mode authentication capability in Microsoft SQL Server 7.0 stores the System Administrator (sa) account in plaintext in a log file which is readable by any user, aka the "SQL Server 7.0 Service Pack Password" vulnerability.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=263968
- http://www.securityfocus.com/bid/1281
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-035
- http://www.microsoft.com/technet/support/kb.asp?ID=263968
- http://www.securityfocus.com/bid/1281

---

#### 870. CVE-2000-0485

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft SQL Server allows local users to obtain database passwords via the Data Transformation Service (DTS) package Properties dialog, aka the "DTS Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/62771
- http://www.securityfocus.com/bid/1292
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4582
- http://www.securityfocus.com/archive/1/62771

---

#### 871. CVE-2000-0495

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media Encoder allows remote attackers to cause a denial of service via a malformed request, aka the "Malformed Windows Media Encoder Request" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1282
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-038
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4585
- http://www.securityfocus.com/bid/1282
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-038

---

#### 872. CVE-2000-0524

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook and Outlook Express allow remote attackers to cause a denial of service by sending email messages with blank fields such as BCC, Reply-To, Return-Path, or From.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html
- http://www.securityfocus.com/bid/1333
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html
- http://www.securityfocus.com/bid/1333

---

#### 873. CVE-2000-0596

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.x does not warn a user before opening a Microsoft Access database file that is referenced within ActiveX OBJECT tags in an HTML document, which could allow remote attackers to execute arbitrary commands, aka the "IE Script" vulnerability.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2000-16.html
- http://www.securityfocus.com/bid/1398
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=000d01bfe0fb%24418f59b0%2496217aa8%40src.bu.edu
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589359.762392DB%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-049

---

#### 874. CVE-2000-0597

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Office 2000 (Excel and PowerPoint) and PowerPoint 97 are marked as safe for scripting, which allows remote attackers to force Internet Explorer or some email clients to save files to arbitrary locations via the Visual Basic for Applications (VBA) SaveAs function, aka the "Office HTML Script" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1399
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589349.ED9DBCAB%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-049
- http://www.securityfocus.com/bid/1399
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589349.ED9DBCAB%40nat.bg

---

#### 875. CVE-2000-0603

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 allows a local user to bypass permissions for stored procedures by referencing them via a temporary stored procedure, aka the "Stored Procedure Permissions" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1444
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-048
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4921
- http://www.securityfocus.com/bid/1444
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-048

---

#### 876. CVE-2000-0654

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Enterprise Manager allows local users to obtain database passwords via the Data Transformation Service (DTS) package Registered Servers Dialog dialog, aka a variant of the "DTS Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1466
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4582
- http://www.securityfocus.com/bid/1466
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041

---

#### 877. CVE-2000-0662

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Internet Explorer 5.x and Microsoft Outlook allows remote attackers to read arbitrary files by redirecting the contents of an IFRAME using the DHTML Edit Control (DHTMLED).

**参考链接 / References**:
- http://www.securityfocus.com/bid/1474
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396EF9D5.62EEC625%40nat.bg
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5107
- http://www.securityfocus.com/bid/1474
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396EF9D5.62EEC625%40nat.bg

---

#### 878. CVE-2000-0567

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Outlook and Outlook Express allows remote attackers to execute arbitrary commands via a long Date field in an email header, aka the "Malformed E-mail Header" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1481
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-043
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4953
- http://www.securityfocus.com/bid/1481
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-043

---

#### 879. CVE-2000-0621

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Outlook 98 and 2000, and Outlook Express 4.0x and 5.0x, allow remote attackers to read files on the client's system via a malformed HTML message that stores files outside of the cache, aka the "Cache Bypass" vulnerability.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2000-14.html
- http://www.securityfocus.com/bid/1501
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-046
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5013
- http://www.cert.org/advisories/CA-2000-14.html

---

#### 880. CVE-2000-0653

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook Express allows remote attackers to monitor a user's email by creating a persistent browser link to the Outlook Express windows, aka the "Persistent Mail-Browser Link" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1502
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-045
- http://www.securityfocus.com/bid/1502
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-045

---

#### 881. CVE-2000-0637

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 allows an attacker to execute arbitrary commands by specifying a malicious .dll using the Register.ID function, aka the "Excel REGISTER.ID Function" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1451
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396B3F8F.9244D290%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-051
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5016
- http://www.securityfocus.com/bid/1451

---

#### 882. CVE-2000-1079

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Interactions between the CIFS Browser Protocol and NetBIOS as implemented in Microsoft Windows 95, 98, NT, and 2000 allow remote attackers to modify dynamic NetBIOS name cache entries via a spoofed Browse Frame Request in a unicast or UDP broadcast datagram.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0116.html
- http://www.nai.com/research/covert/advisories/045.asp
- http://www.securityfocus.com/bid/1620
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5168
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1079

---

#### 883. CVE-2000-0709

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to cause a denial of service in some components by requesting a URL whose name includes a standard DOS device name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp
- http://www.securityfocus.com/bid/1608
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp

---

#### 884. CVE-2000-0710

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to determine the physical path of the server components by requesting an invalid URL whose name includes a standard DOS device name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp
- http://www.securityfocus.com/bid/1608
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp

---

#### 885. CVE-2000-0742

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The IPX protocol implementation in Microsoft Windows 95 and 98 allows remote attackers to cause a denial of service by sending a ping packet with a source IP address that is a broadcast address, aka the "Malformed IPX Ping Packet" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1544
- http://www.securityfocus.com/templates/archive.pike?list=1&mid=63120
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-054
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5079
- http://www.securityfocus.com/bid/1544

---

#### 886. CVE-2000-0753

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Outlook mail client identifies the physical path of the sender's machine within a winmail.dat attachment to Rich Text Format (RTF) files.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/201422
- http://www.securityfocus.com/archive/1/78240
- http://www.securityfocus.com/bid/1631
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5508
- http://www.securityfocus.com/archive/1/201422

---

#### 887. CVE-2000-0756

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook 2000 does not properly process long or malformed fields in vCard (.vcf) files, which allows attackers to cause a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1633
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Springmail.105.967737080.0.16997300%40www.springmail.com
- http://www.securityfocus.com/bid/1633
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Springmail.105.967737080.0.16997300%40www.springmail.com

---

#### 888. CVE-2000-0765

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Buffer overflow in the HTML interpreter in Microsoft Office 2000 allows an attacker to execute arbitrary commands via a long embedded object tag, aka the "Microsoft Office HTML Object Tag" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1561
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-056
- http://www.securityfocus.com/bid/1561
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-056

---

#### 889. CVE-2000-0771

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to cause a denial of service by corrupting the local security policy via malformed RPC traffic, aka the "Local Security Policy Corruption" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1613
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-062
- http://www.securityfocus.com/bid/1613
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-062

---

#### 890. CVE-2000-0777

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The password protection feature of Microsoft Money can store the password in plaintext, which allows attackers with physical access to the system to obtain the password, aka the "Money Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1615
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-061
- http://www.securityfocus.com/bid/1615
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-061

---

#### 891. CVE-2000-0788

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Mail Merge tool in Microsoft Word does not prompt the user before executing Visual Basic (VBA) scripts in an Access database, which could allow an attacker to execute arbitrary commands.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1566
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=398EB9CA.27E03A9C%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-071
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5322
- http://www.securityfocus.com/bid/1566

---

#### 892. CVE-2000-0790

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The web-based folder display capability in Microsoft Internet Explorer 5.5 on Windows 98 allows local users to insert Trojan horse programs by modifying the Folder.htt file and using the InvokeVerb method in the ShellDefView ActiveX control to specify a default execute option for the first file that is listed in the folder.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1571
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3998370D.732A03F1%40nat.bg
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5097
- http://www.securityfocus.com/bid/1571
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3998370D.732A03F1%40nat.bg

---

#### 893. CVE-2000-0849

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Race condition in Microsoft Windows Media server allows remote attackers to cause a denial of service in the Windows Media Unicast Service via a malformed request, aka the "Unicast Service Race Condition" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1655
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-064
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5193
- http://www.securityfocus.com/bid/1655
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-064

---

#### 894. CVE-2000-0854

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
When a Microsoft Office 2000 document is launched, the directory of that document is first used to locate DLL's such as riched20.dll and msi.dll, which could allow an attacker to execute arbitrary commands by inserting a Trojan Horse DLL into the same directory as the document.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0277.html
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0155.html
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q3/0117.html
- http://www.securityfocus.com/bid/1699
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5263

---

#### 895. CVE-2000-0858

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerability in Microsoft Windows NT 4.0 allows remote attackers to cause a denial of service in IIS by sending it a series of malformed requests which cause INETINFO.EXE to fail, aka the "Invalid URL" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html
- http://www.securityfocus.com/archive/1/80413
- http://www.securityfocus.com/bid/1642
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5202
- http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html

---

#### 896. CVE-2000-1217

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows 2000 before Service Pack 2 (SP2), when running in a non-Windows 2000 domain and using NTLM authentication, and when credentials of an account are locally cached, allows local users to bypass account lockout policies and make an unlimited number of login attempts, aka the "Domain Account Lockout" vulnerability.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/818496
- http://www.securityfocus.com/bid/1973
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-089
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5585
- http://www.kb.cert.org/vuls/id/818496

---

#### 897. CVE-2000-1006

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 does not properly handle a MIME header with a blank charset specified, which allows remote attackers to cause a denial of service via a charset="" command, aka the "Malformed MIME Header" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1869
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-082
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5448
- http://www.securityfocus.com/bid/1869
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-082

---

#### 898. CVE-2000-0817

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the HTTP protocol parser for Microsoft Network Monitor (Netmon) allows remote attackers to execute arbitrary commands via malformed data, aka the "Netmon Protocol Parsing" vulnerability.

**参考链接 / References**:
- http://xforce.iss.net/alerts/index.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399
- http://xforce.iss.net/alerts/index.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083

---

#### 899. CVE-2000-0885

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Microsoft Network Monitor (Netmon) allow remote attackers to execute arbitrary commands via a long Browser Name in a CIFS Browse Frame, a long SNMP community name, or a long username or filename in an SMB session, aka the "Netmon Protocol Parsing" vulnerability.  NOTE: It is highly likely that this candidate will be split into multiple candidates.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399

---

#### 900. CVE-2000-0929

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 allows attackers to cause a denial of service in RTF-enabled email clients via an embedded OCX control that is not closed properly, aka the "OCX Attachment" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97024839222747&w=2
- http://www.securityfocus.com/bid/1714
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-068
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5309
- http://marc.info/?l=bugtraq&m=97024839222747&w=2

---

#### 901. CVE-2000-0942

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The CiWebHitsFile component in Microsoft Indexing Services for Windows 2000 allows remote attackers to conduct a cross site scripting (CSS) attack via a CiRestriction parameter in a .htw request, aka the "Indexing Services Cross Site Scripting" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/141903
- http://www.securityfocus.com/bid/1861
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-084
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5441
- http://www.securityfocus.com/archive/1/141903

---

#### 902. CVE-2000-0980

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
NMPI (Name Management Protocol on IPX) listener in Microsoft NWLink does not properly filter packets from a broadcast address, which allows remote attackers to cause a broadcast storm and flood the network.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1781
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-073
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5357
- http://www.securityfocus.com/bid/1781
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-073

---

#### 903. CVE-2000-0983

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft NetMeeting with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service (CPU utilization) via a sequence of null bytes to the NetMeeting port, aka the "NetMeeting Desktop Sharing" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ273854
- http://www.securityfocus.com/archive/1/140341
- http://www.securityfocus.com/bid/1798
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-077
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5368

---

#### 904. CVE-2000-1081

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_displayparamstmt function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2030
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A231
- http://marc.info/?l=bugtraq&m=97570878710037&w=2

---

#### 905. CVE-2000-1082

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_enumresultset function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2031
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2031

---

#### 906. CVE-2000-1083

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The xp_showcolv function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2038
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2038

---

#### 907. CVE-2000-1084

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_updatecolvbm function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2039
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2039

---

#### 908. CVE-2000-1085

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_peekqueue function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2040
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2040

---

#### 909. CVE-2000-1086

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_printstatements function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2041

---

#### 910. CVE-2000-1087

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_proxiedmetadata function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2042
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2042

---

#### 911. CVE-2000-1088

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_SetSQLSecurity function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2043
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2043

---

#### 912. CVE-2000-1089

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Book Service allows local users to execute arbitrary commands, aka the "Phone Book Service Buffer Overflow" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2048
- http://www.stake.com/research/advisories/2000/a120400-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-094
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5623
- http://www.securityfocus.com/bid/2048

---

#### 913. CVE-2000-1112

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 executes scripts in custom skin (.WMS) files, which could allow remote attackers to gain privileges via a skin that contains a malicious script, aka the ".WMS Script Execution" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1976
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5575
- http://www.securityfocus.com/bid/1976
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090

---

#### 914. CVE-2000-1113

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player allows remote attackers to execute arbitrary commands via a malformed Active Stream Redirector (.ASX) file, aka the ".ASX Buffer Overrun" vulnerability.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a112300-1.txt
- http://www.securityfocus.com/bid/1980
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5574
- http://www.atstake.com/research/advisories/2000/a112300-1.txt

---

#### 915. CVE-2000-1139

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The installation of Microsoft Exchange 2000 before Rev. A creates a user account with a known password, which could allow attackers to gain privileges, aka the "Exchange User Account" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1958
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-088
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5537
- http://www.securityfocus.com/bid/1958
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-088

---

#### 916. CVE-2000-1090

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS for Far East editions 4.0 and 5.0 allows remote attackers to read source code for parsed pages via a malformed URL that uses the lead-byte of a double-byte character.

**参考链接 / References**:
- http://www.nsfocus.com/english/homepage/sa_08.htm
- http://www.securityfocus.com/bid/2100
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5729
- http://www.nsfocus.com/english/homepage/sa_08.htm
- http://www.securityfocus.com/bid/2100

---

#### 917. CVE-2001-0003

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Web Extender Client (WEC) in Microsoft Office 2000, Windows 2000, and Windows Me does not properly process Internet Explorer security settings for NTLM authentication, which allows attackers to obtain NTLM credentials and possibly obtain the password, aka the "Web Client NTLM Authentication" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2199
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-001
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5920
- http://www.securityfocus.com/bid/2199
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-001

---

#### 918. CVE-2001-0005

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Buffer overflow in the parsing mechanism of the file loader in Microsoft PowerPoint 2000 allows attackers to execute arbitrary commands.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2001/a012301-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-002
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5996
- http://www.atstake.com/research/advisories/2001/a012301-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-002

---

#### 919. CVE-2001-0048

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The "Configure Your Server" tool in Microsoft 2000 domain controllers installs a blank password for the Directory Service Restore Mode, which allows attackers with physical access to the controller to install malicious programs, aka the "Directory Service Restore Mode Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-099
- http://www.securityfocus.com/bid/2133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-099

---

#### 920. CVE-2001-0047

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default permissions for the MTS Package Administration registry key in Windows NT 4.0 allows local users to install or modify arbitrary Microsoft Transaction Server (MTS) packages and gain privileges, aka one of the "Registry Permissions" vulnerabilities.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2065
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5673
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A140
- http://www.securityfocus.com/bid/2065

---

#### 921. CVE-1999-0681

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft FrontPage Server Extensions (PWS) 3.0.2.926 on Windows 95, and possibly other versions, allows remote attackers to cause a denial of service via a long URL.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html
- http://www.securityfocus.com/bid/568
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3117
- http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html
- http://www.securityfocus.com/bid/568

---

#### 922. CVE-1999-0945

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Service (IMS) for Microsoft Exchange 5.5 and 5.0 allows remote attackers to conduct a denial of service via AUTH or AUTHINFO commands.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174
- http://www.ciac.org/ciac/bulletins/i-080.shtml
- http://xforce.iss.net/alerts/advise4.php
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1223
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174

---

#### 923. CVE-2001-1450

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.0 through 6.0 allows attackers to cause a denial of service (browser crash) via a crafted FTP URL such as "/.#./".

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html
- http://www.kb.cert.org/vuls/id/199408
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10117
- http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html
- http://www.kb.cert.org/vuls/id/199408

---

#### 924. CVE-2001-1326

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Eudora 5.1 allows remote attackers to execute arbitrary code when the "Use Microsoft Viewer" option is enabled and the "allow executables in HTML content" option is disabled, via an HTML email with a form that is activated from an image that the attacker spoofs as a link, which causes the user to execute the form and access embedded attachments.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/187128
- http://www.securityfocus.com/bid/2796
- http://www.securityfocus.com/archive/1/187128
- http://www.securityfocus.com/bid/2796

---

#### 925. CVE-2001-0146

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
IIS 5.0 and Microsoft Exchange 2000 allow remote attackers to cause a denial of service (memory allocation error) by repeatedly sending a series of specially formatted URL's.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/796584
- http://www.securityfocus.com/bid/2440
- http://www.securityfocus.com/bid/2441
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-014
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6171

---

#### 926. CVE-2001-0261

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 Encrypted File System does not properly destroy backups of files that are encrypted, which allows a local attacker to recover the text of encrypted files.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97992179925715&w=2
- http://marc.info/?l=bugtraq&m=98027311214976&w=2
- http://www.securityfocus.com/bid/2243
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5973
- http://marc.info/?l=bugtraq&m=97992179925715&w=2

---

#### 927. CVE-2001-1088

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Outlook 8.5 and earlier, and Outlook Express 5 and earlier, with the "Automatically put people I reply to in my address book" option enabled, do not notify the user when the "Reply-To" address is different than the "From" address, which could allow an untrusted remote attacker to spoof legitimate addresses and intercept email from the client that is intended for another user.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241
- http://www.securityfocus.com/archive/1/188752
- http://www.securityfocus.com/bid/2823
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6655
- http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241

---

#### 928. CVE-2001-0237

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in Microsoft 2000 domain controller allows remote attackers to cause a denial of service by repeatedly connecting to the Kerberos service and then disconnecting without sending any data.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-079.shtml
- http://marc.info/?l=bugtraq&m=98942093221908&w=2
- http://www.securityfocus.com/bid/2707
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-024
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6506

---

#### 929. CVE-2001-0240

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Word before Word 2002 allows attackers to automatically execute macros without warning the user via a Rich Text Format (RTF) document that links to a template with the embedded macro.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2753
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-028
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6571
- http://www.securityfocus.com/bid/2753
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-028

---

#### 930. CVE-2001-0242

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Microsoft Windows Media Player 7 and earlier allow remote attackers to execute arbitrary commands via (1) a long version tag in an .ASX file, or (2) a long banner tag, a variant of the ".ASX Buffer Overrun" vulnerability as discussed in MS:MS00-090.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/187528
- http://www.securityfocus.com/archive/1/181419
- http://www.securityfocus.com/archive/1/183906
- http://www.securityfocus.com/bid/2677
- http://www.securityfocus.com/bid/2686

---

#### 931. CVE-2001-0244

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Index Server 2.0 allows remote attackers to execute arbitrary commands via a long search parameter.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2709
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6517
- http://www.securityfocus.com/bid/2709
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025

---

#### 932. CVE-2001-0245

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server 2.0 in Windows NT 4.0, and Indexing Service in Windows 2000, allows remote attackers to read server-side include files via a malformed search request, aka a new variant of the "Malformed Hit-Highlighting" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6518
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6518

---

#### 933. CVE-2001-0336

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft MS00-060 patch for IIS 5.0 and earlier introduces an error which allows attackers to cause a denial of service via a malformed request.

**参考链接 / References**:
- http://www.osvdb.org/5693
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6858
- http://www.osvdb.org/5693
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026

---

#### 934. CVE-2001-0337

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft MS01-014 and MS01-016 patches for IIS 5.0 and earlier introduce a memory leak which allows attackers to cause a denial of service via a series of requests.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026

---

#### 935. CVE-2001-0365

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Eudora before 5.1 allows a remote attacker to execute arbitrary code, when the 'Use Microsoft Viewer' and 'allow executables in HTML content' options are enabled, via an HTML email message containing Javascript, with ActiveX controls and malicious code within IMG tags.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98503741910995&w=2
- http://www.securityfocus.com/bid/2490
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6262
- http://marc.info/?l=bugtraq&m=98503741910995&w=2
- http://www.securityfocus.com/bid/2490

---

#### 936. CVE-2001-0238

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Data Access Component Internet Publishing Provider 8.103.2519.0 and earlier allows remote attackers to bypass Security Zone restrictions via WebDAV requests.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-074.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-022
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6405
- http://www.ciac.org/ciac/bulletins/l-074.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-022

---

#### 937. CVE-2001-0239

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 Web Proxy allows remote attackers to cause a denial of service via a long web request with a specific type.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-073.shtml
- http://www.securityfocus.com/archive/1/176912
- http://www.securityfocus.com/archive/1/177160
- http://www.securityfocus.com/archive/1/179986
- http://www.securityfocus.com/bid/2600

---

#### 938. CVE-2001-1243

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Scripting.FileSystemObject in asp.dll for Microsoft IIS 4.0 and 5.0 allows local or remote attackers to cause a denial of service (crash) via (1) creating an ASP program that uses Scripting.FileSystemObject to open a file with an MS-DOS device name, or (2) remotely injecting the device name into ASP programs that internally use Scripting.FileSystemObject.

**参考链接 / References**:
- http://www.iss.net/security_center/static/6800.php
- http://www.securityfocus.com/archive/1/194919
- http://www.securityfocus.com/bid/2973
- http://www.iss.net/security_center/static/6800.php
- http://www.securityfocus.com/archive/1/194919

---

#### 939. CVE-2001-1319

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange 5.5 2000 allows remote attackers to cause a denial of service (hang) via exceptional BER encodings for the LDAP filter type field, as demonstrated by the PROTOS LDAPv3 test suite.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-116.shtml
- http://www.cert.org/advisories/CA-2001-18.html
- http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/ldapv3/
- http://www.kb.cert.org/vuls/id/763400
- http://www.kb.cert.org/vuls/id/CFCN-4YAQC7

---

#### 940. CVE-2001-0340

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
An interaction between the Outlook Web Access (OWA) service in Microsoft Exchange 2000 Server and Internet Explorer allows attackers to execute malicious script code against a user's mailbox via a message attachment that contains HTML code, which is executed automatically.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-091.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6652
- http://www.ciac.org/ciac/bulletins/l-091.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-030

---

#### 941. CVE-2001-0341

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Visual Studio RAD Support sub-component of FrontPage Server Extensions allows remote attackers to execute arbitrary commands via a long registration request (URL) to fp30reg.dll.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99348216322147&w=2
- http://www.osvdb.org/577
- http://www.securityfocus.com/bid/2906
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-035
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6730

---

#### 942. CVE-2001-0344

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
An SQL query method in Microsoft SQL Server 2000 Gold and 7.0 using Mixed Mode allows local database users to gain privileges by reusing a cached connection of the sa administrator account.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-095.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6684
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A71
- http://www.ciac.org/ciac/bulletins/l-095.shtml

---

#### 943. CVE-2001-0345

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to prevent idle Telnet sessions from timing out, causing a denial of service by creating a large number of idle sessions.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2843
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6667
- http://www.securityfocus.com/bid/2843
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031

---

#### 944. CVE-2001-0346

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Handle leak in Microsoft Windows 2000 telnet service allows attackers to cause a denial of service by starting a large number of sessions and terminating them.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6668
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6668

---

#### 945. CVE-2001-0347

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Information disclosure vulnerability in Microsoft Windows 2000 telnet service allows remote attackers to determine the existence of user accounts such as Guest, or log in to the server without specifying the domain name, via a malformed userid.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.osvdb.org/5686
- http://www.securityfocus.com/bid/2847
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6665

---

#### 946. CVE-2001-0348

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to cause a denial of service (crash) via a long logon command that contains a backspace.

**参考链接 / References**:
- http://razor.bindview.com/publish/advisories/adv_mstelnet.html
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.securityfocus.com/bid/2838
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6666

---

#### 947. CVE-2001-0349

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the first of two variants of this vulnerability.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/587587
- http://www.securityfocus.com/bid/2849
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664
- http://www.kb.cert.org/vuls/id/587587

---

#### 948. CVE-2001-0350

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the second of two variants of this vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664

---

#### 949. CVE-2001-0351

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows a local user to make a certain system call that allows the user to terminate a Telnet session and cause a denial of service.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.securityfocus.com/bid/2846
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6669
- http://www.ciac.org/ciac/bulletins/l-092.shtml

---

#### 950. CVE-2001-0501

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Word 2002 and earlier allows attackers to automatically execute macros without warning the user by embedding the macros in a manner that escapes detection by the security scanner.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99325144322224&w=2
- http://www.securityfocus.com/bid/2876
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-034
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6732
- http://marc.info/?l=bugtraq&m=99325144322224&w=2

---

#### 951. CVE-2001-0503

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft NetMeeting 3.01 with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service via a malformed string to the NetMeeting service port, aka a variant of the "NetMeeting Desktop Sharing" vulnerability.

**参考链接 / References**:
- http://www.iss.net/security_center/static/5368.php
- http://www.osvdb.org/5608
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-077
- http://www.iss.net/security_center/static/5368.php
- http://www.osvdb.org/5608

---

#### 952. CVE-2001-1055

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Windows network stack allows remote attackers to cause a denial of service (CPU consumption) via a flood of malformed ARP request packets with random source IP and MAC addresses, as demonstrated by ARPNuke.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/200323
- http://www.securityfocus.com/bid/3113
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6924
- http://www.securityfocus.com/archive/1/200323
- http://www.securityfocus.com/bid/3113

---

#### 953. CVE-2001-0504

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in authentication process for SMTP service in Microsoft Windows 2000 allows remote attackers to use incorrect credentials to gain privileges and conduct activities such as mail relaying.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-107.shtml
- http://www.kb.cert.org/vuls/id/435963
- http://www.securityfocus.com/bid/2988
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-037
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6803

---

#### 954. CVE-2001-0538

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Outlook View ActiveX Control in Microsoft Outlook 2002 and earlier allows remote attackers to execute arbitrary commands via a malicious HTML e-mail message or web page.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99496431214078&w=2
- http://www.ciac.org/ciac/bulletins/l-113.shtml
- http://www.kb.cert.org/vuls/id/131569
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind0107&L=ntbugtraq&F=P&S=&P=862
- http://www.securityfocus.com/bid/3025

---

#### 955. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 956. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 957. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 958. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 959. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 960. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 961. CVE-1999-0426

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The default permissions of /dev/kmem in Linux versions before 2.0.36 allows IP spoofing.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0426
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0426

---

#### 962. CVE-1999-0431

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Linux 2.2.3 and earlier allow a remote attacker to perform an IP fragmentation attack, causing a denial of service.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0431
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0431

---

#### 963. CVE-1999-0409

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in gnuplot in Linux version 3.5 allows local users to obtain root access.

**参考链接 / References**:
- http://www.securityfocus.com/bid/319
- http://www.securityfocus.com/bid/319

---

#### 964. CVE-1999-0421

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
During a reboot after an installation of Linux Slackware 3.6, a remote attacker can obtain root access by logging in to the root account without a password.

**参考链接 / References**:
- http://www.osvdb.org/981
- http://www.securityfocus.com/bid/338
- http://www.osvdb.org/981
- http://www.securityfocus.com/bid/338

---

#### 965. CVE-1999-0462

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
suidperl in Linux Perl does not check the nosuid mount option on file systems, allowing local users to gain root access by placing a setuid script in a mountable file system, e.g. a CD-ROM or floppy disk.

**参考链接 / References**:
- http://www.securityfocus.com/bid/339
- http://www.securityfocus.com/bid/339

---

#### 966. CVE-1999-0804

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Linux 2.2.x kernels via malformed ICMP packets containing unusual types, codes, and IP header lengths.

**参考链接 / References**:
- http://www.securityfocus.com/bid/302
- http://www.securityfocus.com/bid/302

---

#### 967. CVE-2000-0364

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
screen and rxvt in Red Hat Linux 6.0 do not properly set the modes of tty devices, which allows local users to write to other ttys.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92877527701347&w=2
- http://marc.info/?l=bugtraq&m=92886009012161&w=2
- http://www.redhat.com/corp/support/errata/RHSA1999014_01.html
- http://www.securityfocus.com/bid/309
- http://marc.info/?l=bugtraq&m=92877527701347&w=2

---

#### 968. CVE-2000-0365

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Red Hat Linux 6.0 installs the /dev/pts file system with insecure modes, which allows local users to write to other tty devices.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92877527701347&w=2
- http://marc.info/?l=bugtraq&m=92886009012161&w=2
- http://www.redhat.com/corp/support/errata/RHSA1999014_01.html
- http://www.securityfocus.com/bid/308
- http://marc.info/?l=bugtraq&m=92877527701347&w=2

---

#### 969. CVE-1999-1496

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Sudo 1.5 in Debian Linux 2.1 and Red Hat 6.0 allows local users to determine the existence of arbitrary files by attempting to execute the target filename as a program, which generates a different error message when the file does not exist.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/14665
- http://www.securityfocus.com/bid/321
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2277
- http://www.securityfocus.com/archive/1/14665
- http://www.securityfocus.com/bid/321

---

#### 970. CVE-2000-0118

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Red Hat Linux su program does not log failed password guesses if the su process is killed before it times out, which allows local attackers to conduct brute force password guessing.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94935300520617&w=2
- http://marc.info/?l=bugtraq&m=94935300520617&w=2

---

#### 971. CVE-1999-0733

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in VMWare 1.0.1 for Linux via a long HOME environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/490
- http://www.securityfocus.com/bid/490

---

#### 972. CVE-1999-1348

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linuxconf on Red Hat Linux 6.0 and earlier does not properly disable PAM-based access to the shutdown command, which could allow local users to cause a denial of service.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93220073515880&w=2
- http://marc.info/?l=bugtraq&m=93220073515880&w=2

---

#### 973. CVE-1999-1166

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux 2.0.37 does not properly encode the Custom segment limit, which allows local users to gain root privileges by accessing and modifying kernel memory.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/18156
- http://www.securityfocus.com/bid/523
- http://www.securityfocus.com/archive/1/18156
- http://www.securityfocus.com/bid/523

---

#### 974. CVE-1999-0710

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Squid package in Red Hat Linux 5.2 and 6.0, and other distributions, installs cachemgr.cgi in a public web directory, which allows remote attackers to use it as an intermediary to connect to other systems.

**参考链接 / References**:
- http://fedoranews.org/updates/FEDORA--.shtml
- http://www.debian.org/security/2004/dsa-576
- http://www.redhat.com/archives/fedora-announce-list/2005-May/msg00025.html
- http://www.redhat.com/support/errata/RHSA-1999-025.html
- http://www.redhat.com/support/errata/RHSA-2005-489.html

---

#### 975. CVE-1999-1018

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
IPChains in Linux kernels 2.2.10 and earlier does not reassemble IP fragments before checking the header information, which allows a remote attacker to bypass the filtering rules using several fragments with 0 offsets.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93312523904591&w=2
- http://www.securityfocus.com/bid/543
- http://marc.info/?l=bugtraq&m=93312523904591&w=2
- http://www.securityfocus.com/bid/543

---

#### 976. CVE-1999-0746

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A default configuration of in.identd in SuSE Linux waits 120 seconds between requests, allowing a remote attacker to conduct a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/587
- http://www.securityfocus.com/bid/587

---

#### 977. CVE-1999-0740

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Remote attackers can cause a denial of service on Linux in.telnetd telnet daemon through a malformed TERM environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/594
- http://www.securityfocus.com/bid/594

---

#### 978. CVE-2000-0374

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The default configuration of kdm in Caldera and Mandrake Linux, and possibly other distributions, allows XDMCP connections from any host, which allows remote attackers to obtain sensitive information or bypass additional access restrictions.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-021.0.txt
- http://frontal2.mandriva.com/security/advisories?name=MDKSA-2002:025
- http://www.securityfocus.com/bid/1446
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4856
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-021.0.txt

---

#### 979. CVE-1999-0720

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The pt_chown command in Linux allows local users to modify TTY terminal devices that belong to other users.

**参考链接 / References**:
- http://www.securityfocus.com/bid/597
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=lcamtuf.4.05.9907041223290.355-300000%40nimue.ids.pl
- http://www.securityfocus.com/bid/597
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=lcamtuf.4.05.9907041223290.355-300000%40nimue.ids.pl

---

#### 980. CVE-1999-0769

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vixie Cron on Linux systems allows local users to set parameters of sendmail commands via the MAILTO environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/611
- http://www.securityfocus.com/bid/611

---

#### 981. CVE-1999-0704

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Buffer overflow in Berkeley automounter daemon (amd) logging facility provided in the Linux am-utils package and others.

**参考链接 / References**:
- http://www.securityfocus.com/bid/614
- http://www.securityfocus.com/bid/614

---

#### 982. CVE-1999-1352

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
mknod in Linux 2.2 follows symbolic links, which could allow local users to overwrite files or gain privileges.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93855134409747&w=2
- http://marc.info/?l=bugtraq&m=93855134409747&w=2

---

#### 983. CVE-1999-1346

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
PAM configuration file for rlogin in Red Hat Linux 6.1 and earlier includes a less restrictive rule before a more restrictive one, which allows users to access the host via rlogin even if rlogin has been explicitly disabled using the /etc/nologin file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93942774609925&w=2
- http://marc.info/?l=bugtraq&m=93942774609925&w=2

---

#### 984. CVE-1999-1347

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Xsession in Red Hat Linux 6.1 and earlier can allow local users with restricted accounts to bypass execution of the .xsession file by starting kde, gnome or anotherlevel from kdm.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93942774609925&w=2
- http://marc.info/?l=bugtraq&m=93942774609925&w=2

---

#### 985. CVE-2000-0369

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The IDENT server in Caldera Linux 2.3 creates multiple threads for each IDENT request, which allows remote attackers to cause a denial of service.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-029.1.txt
- http://www.securityfocus.com/bid/1266
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-029.1.txt
- http://www.securityfocus.com/bid/1266

---

#### 986. CVE-2000-0356

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Pluggable Authentication Modules (PAM) in Red Hat Linux 6.1 does not properly lock access to disabled NIS accounts.

**参考链接 / References**:
- http://www.securityfocus.com/bid/697
- http://www.securityfocus.com/templates/advisory.html?id=1789
- http://www.securityfocus.com/bid/697
- http://www.securityfocus.com/templates/advisory.html?id=1789

---

#### 987. CVE-1999-1341

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Linux kernel before 2.3.18 or 2.2.13pre15, with SLIP and PPP options, allows local unprivileged users to forge IP packets via the TIOCSETD option on tty devices.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94061108411308&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7858
- http://marc.info/?l=bugtraq&m=94061108411308&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7858

---

#### 988. CVE-2000-0362

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflows in Linux cdwtools 093 and earlier allows local users to gain root privileges.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738

---

#### 989. CVE-2000-0363

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Linux cdwtools 093 and earlier allows local users to gain root privileges via the /tmp directory.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738

---

#### 990. CVE-1999-0832

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in NFS server on Linux allows attackers to execute commands via a long pathname.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-033.0.txt
- http://www.debian.org/security/1999/19991111
- http://www.novell.com/linux/security/advisories/suse_security_announce_29.html
- http://www.redhat.com/support/errata/rh42-errata-general.html#NFS
- http://www.securityfocus.com/bid/782

---

#### 991. CVE-1999-0831

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Linux syslogd via a large number of connections.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-035.0.txt
- http://www.securityfocus.com/bid/809
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-035.0.txt
- http://www.securityfocus.com/bid/809

---

#### 992. CVE-2000-0531

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux gpm program allows local users to cause a denial of service by flooding the /dev/gpmctl device with STREAM sockets.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0409.html
- http://www.redhat.com/support/errata/RHSA-2000-045.html
- http://www.securityfocus.com/bid/1377
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.10.10006201453090.1812-200000%40apollo.aci.com.pl
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5010

---

#### 993. CVE-1999-0317

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux su command gives root access to local users.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0317
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0317

---

#### 994. CVE-2000-0357

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ORBit and esound in Red Hat Linux 6.1 do not use sufficiently random numbers, which allows local users to guess the authentication keys.

**参考链接 / References**:
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html

---

#### 995. CVE-2000-0358

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ORBit and gnome-session in Red Hat Linux 6.1 allows remote attackers to crash a program.

**参考链接 / References**:
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html

---

#### 996. CVE-1999-0986

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The ping command in Linux 2.0.3x allows local users to cause a denial of service by sending large packets with the -R (record route) option.

**参考链接 / References**:
- http://www.securityfocus.com/bid/870
- http://www.securityfocus.com/bid/870

---

#### 997. CVE-2000-0017

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Linux linuxconf package allows remote attackers to gain root privileges via a long parameter.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=94580196627059&w=2
- https://marc.info/?l=bugtraq&m=94580196627059&w=2

---

#### 998. CVE-1999-1327

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in linuxconf 1.11r11-rh2 on Red Hat Linux 5.1 allows local users to gain root privileges via a long LANG environmental variable.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221103125826&w=2
- http://www.iss.net/security_center/static/7239.php
- http://www.osvdb.org/6065
- http://www.redhat.com/support/errata/rh51-errata-general.html#linuxconf
- http://marc.info/?l=bugtraq&m=90221103125826&w=2

---

#### 999. CVE-1999-1328

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
linuxconf before 1.11.r11-rh3 on Red Hat Linux 5.1 allows local users to overwrite arbitrary files and gain root access via a symlink attack.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90383955231511&w=2
- http://www.iss.net/security_center/static/7232.php
- http://www.osvdb.org/6068
- http://www.redhat.com/support/errata/rh51-errata-general.html#linuxconf
- http://marc.info/?l=bugtraq&m=90383955231511&w=2

---

#### 1000. CVE-1999-1329

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in SysVInit in Red Hat Linux 5.1 and earlier allows local users to gain privileges.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7250.php
- http://www.redhat.com/support/errata/rh50-errata-general.html#SysVinit
- http://www.iss.net/security_center/static/7250.php
- http://www.redhat.com/support/errata/rh50-errata-general.html#SysVinit

---

#### 1001. CVE-1999-1331

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
netcfg 2.16-1 in Red Hat Linux 4.2 allows the Ethernet interface to be controlled by users on reboot when an option is set, which allows local users to cause a denial of service by shutting down the interface.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7245.php
- http://www.redhat.com/support/errata/rh42-errata-general.html#netcfg
- http://www.iss.net/security_center/static/7245.php
- http://www.redhat.com/support/errata/rh42-errata-general.html#netcfg

---

#### 1002. CVE-1999-1332

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
gzexe in the gzip package on Red Hat Linux 5.0 and earlier allows local users to overwrite files of other users via a symlink attack on a temporary file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=88603844115233&w=2
- http://www.debian.org/security/2003/dsa-308
- http://www.iss.net/security_center/static/7241.php
- http://www.osvdb.org/3812
- http://www.redhat.com/support/errata/rh50-errata-general.html#gzip

---

#### 1003. CVE-1999-1333

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
automatic download option in ncftp 2.4.2 FTP client in Red Hat Linux 5.0 and earlier allows remote attackers to execute arbitrary commands via shell metacharacters in the names of files that are to be downloaded.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=89042322924057&w=2
- http://www.iss.net/security_center/static/7240.php
- http://www.osvdb.org/6111
- http://www.redhat.com/support/errata/rh50-errata-general.html#ncftp
- http://marc.info/?l=bugtraq&m=89042322924057&w=2

---

#### 1004. CVE-1999-1335

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
snmpd server in cmu-snmp SNMP package before 3.3-1 in Red Hat Linux 4.0 is configured to allow remote attackers to read and write sensitive information.

**参考链接 / References**:
- http://www.redhat.com/support/errata/rh40-errata-general.html#cmu-snmp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7251
- http://www.redhat.com/support/errata/rh40-errata-general.html#cmu-snmp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7251

---

#### 1005. CVE-1999-1339

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerability when Network Address Translation (NAT) is enabled in Linux 2.2.10 and earlier with ipchains, or FreeBSD 3.2 with ipfw, allows remote attackers to cause a denial of service (kernel panic) via a ping -R (record route) command.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93277426802802&w=2
- http://marc.info/?l=bugtraq&m=93277766505061&w=2
- http://www.iss.net/security_center/static/7257.php
- http://www.kernel.org/pub/linux/kernel/v2.2/patch-2.2.11.gz
- http://www.osvdb.org/6105

---

#### 1006. CVE-1999-0894

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Red Hat Linux screen program does not use Unix98 ptys, allowing local users to write to other terminals.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0894
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0894

---

#### 1007. CVE-2000-1220

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The line printer daemon (lpd) in the lpr package in multiple Linux operating systems allows local users to gain root privileges by causing sendmail to execute with arbitrary command line arguments, as demonstrated using the -C option to specify a configuration file.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20021104-01-P
- http://seclists.org/lists/bugtraq/2000/Jan/0116.html
- http://www.atstake.com/research/advisories/2000/lpd_advisory.txt
- http://www.debian.org/security/2000/20000109
- http://www.kb.cert.org/vuls/id/39001

---

#### 1008. CVE-2000-1221

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The line printer daemon (lpd) in the lpr package in multiple Linux operating systems authenticates by comparing the reverse-resolved hostname of the local machine to the hostname of the print server as returned by gethostname, which allows remote attackers to bypass intended access controls by modifying the DNS for the attacking IP.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20021104-01-P
- http://rhn.redhat.com/errata/RHSA-2000-002.html
- http://www.atstake.com/research/advisories/2000/lpd_advisory.txt
- http://www.debian.org/security/2000/20000109
- http://www.kb.cert.org/vuls/id/30308

---

#### 1009. CVE-2000-0048

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
get_it program in Corel Linux Update allows local users to gain root access by specifying an alternate PATH for the cp program.

**参考链接 / References**:
- http://linux.corel.com/support/clos_patch1.htm
- http://www.securityfocus.com/bid/928
- http://linux.corel.com/support/clos_patch1.htm
- http://www.securityfocus.com/bid/928

---

#### 1010. CVE-2000-0107

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux apcd program allows local attackers to modify arbitrary files via a symlink attack.

**参考链接 / References**:
- http://www.debian.org/security/2000/20000201
- http://www.securityfocus.com/bid/958
- http://www.debian.org/security/2000/20000201
- http://www.securityfocus.com/bid/958

---

#### 1011. CVE-2002-2184

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Digi-Net Technologies DigiChat 3.5 allows chat users to obtain the IP addresses of other chat users via a "Showip" parameter in the chat applet.

**参考链接 / References**:
- http://www.securityfocus.com/bid/5019
- http://www.securityfocus.com/bid/5019

---

#### 1012. CVE-2002-2242

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
The Apple Package Manager in KisMAC 0.02a and earlier modifies file permissions of sensitive files after installation, which could allow attackers to conduct unauthorized activities on those files.

**参考链接 / References**:
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10813
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336

---

#### 1013. CVE-2002-2248

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in the sun.awt.windows.WDefaultFontCharset Java class implementation in Netscape 4.0 allows remote attackers to execute arbitrary code via an applet that calls the WDefaultFontCharset constructor with a long string and invokes the canConvert method.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10706
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256

---

#### 1014. CVE-2002-2281

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Symantec Java! JIT (Just-In-Time) Compiler for Netscape Communicator 4.0 through 4.8 allows remote attackers to execute arbitrary Java commands via an applet that uses a jump call, which is not correctly compiled by the JIT compiler.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6222
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10711
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

---

#### 1015. CVE-2002-2284

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Netscape Communicator 4.0 through 4.79 allows remote attackers to bypass JVM security and execute arbitrary Java code via an applet that loads user-supplied Java classes.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6223
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10714
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

---

#### 1016. CVE-2002-2292

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Directory traversal vulnerability in Remote Console Applet in Halycon Software iASP 1.0.9 allows remote attackers to read arbitrary files via a .. (dot dot) in the HTTP request to port 9095.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10860
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394

---

#### 1017. CVE-2002-2373

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default configuration of the TCP/IP printer configuration utility in Apple LaserWriter 12/640 PS printer contains a blank Telnet password, which allows remote attackers to gain access.

**参考链接 / References**:
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250
- http://www.securityfocus.com/bid/6052
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250

---

#### 1018. CVE-2003-0049

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Apple File Protocol (AFP) in Mac OS X before 10.2.4 allows administrators to log in as other users by using the administrator password.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://securitytracker.com/id?1006107
- http://www.iss.net/security_center/static/11333.php
- http://www.securityfocus.com/bid/6860

---

#### 1019. CVE-2003-0050

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via shell metacharacters.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11401.php
- http://www.securityfocus.com/bid/6954
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1020. CVE-2003-0051

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to obtain the physical path of the server's installation path via a NULL file parameter.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11402.php
- http://www.securityfocus.com/bid/6956
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1021. CVE-2003-0052

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to list arbitrary directories.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11403.php
- http://www.securityfocus.com/bid/6955
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1022. CVE-2003-0053

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to insert arbitrary script via the filename parameter, which is inserted into an error message.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11404.php
- http://www.securityfocus.com/bid/6958
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1023. CVE-2003-0054

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute certain code via a request to port 7070 with the script in an argument to the rtsp DESCRIBE method, which is inserted into a log file and executed when the log is viewed using a browser.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11405.php
- http://www.securityfocus.com/bid/6960
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1024. CVE-2003-0055

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the MP3 broadcasting module of Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via a long filename.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11406.php
- http://www.securityfocus.com/bid/6957
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

---

#### 1025. CVE-2003-0168

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.x and 6.0 for Windows allows remote attackers to execute arbitrary code via a long QuickTime URL.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html
- http://lists.apple.com/mhonarc/security-announce/msg00027.html
- http://www.idefense.com/advisory/03.31.03.txt
- http://www.kb.cert.org/vuls/id/112553
- http://www.osvdb.org/10561

---

#### 1026. CVE-2003-0111

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The ByteCode Verifier component of Microsoft Virtual Machine (VM) build 5.0.3809 and earlier, as used in Windows and Internet Explorer, allows remote attackers to bypass security checks and execute arbitrary code via a malicious Java applet, aka "Flaw in Microsoft VM Could Enable System Compromise."

**参考链接 / References**:
- http://www.iss.net/security_center/static/11751.php
- http://www.kb.cert.org/vuls/id/447569
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-011
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A136
- http://www.iss.net/security_center/static/11751.php

---

#### 1027. CVE-2003-0420

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Information leak in dsimportexport for Apple Macintosh OS X Server 10.2.6 allows local users to obtain the username and password of the account running the tool.

**参考链接 / References**:
- http://secunia.com/advisories/9025/
- http://www.auscert.org.au/render.html?it=3165
- http://www.kb.cert.org/vuls/id/JPLA-5NTL8E
- http://www.securityfocus.com/bid/7894
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12342

---

#### 1028. CVE-2003-0270

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The administration capability for Apple AirPort 802.11 wireless access point devices uses weak encryption (XOR with a fixed key) for protecting authentication credentials, which could allow remote attackers to obtain administrative access via sniffing when the capability is available via Ethernet or non-WEP connections.

**参考链接 / References**:
- http://secunia.com/advisories/8773
- http://securitytracker.com/id?1006742
- http://www.atstake.com/research/advisories/2003/a051203-1.txt
- http://www.securityfocus.com/bid/7554
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11980

---

#### 1029. CVE-2003-0379

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Unknown vulnerability in Apple File Service (AFP Server) for Mac OS X Server, when sharing files on a UFS or re-shared NFS volume, allows remote attackers to overwrite arbitrary files.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00030.html
- http://lists.apple.com/mhonarc/security-announce/msg00030.html

---

#### 1030. CVE-2003-0421

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1031. CVE-2003-0422

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via a request to view_broadcast.cgi that does not contain the required parameters.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1032. CVE-2003-0423

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
parse_xml.cgi in Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to obtain the source code for parseable files via the filename parameter.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1033. CVE-2003-0424

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to obtain the source code for scripts by appending encoded space (%20) or . (%2e) characters to an HTTP request for the script, e.g. view_broadcast.cgi.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1034. CVE-2003-0425

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Directory traversal vulnerability in Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to read arbitrary files via a ... (triple dot) in an HTTP request.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1035. CVE-2003-0426

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The installation of Apple QuickTime / Darwin Streaming Server before 4.1.3f starts the administration server with a "Setup Assistant" page that allows remote attackers to set the administrator password and gain privileges before the real administrator.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1036. CVE-2003-0502

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

---

#### 1037. CVE-2003-0975

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.1 on Mac OS X 10.3.1 and Mac OS X 10.2.8 allows remote attackers to steal user cookies from another domain via a link with a hex-encoded null character (%00) followed by the target domain.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00042.html
- http://marc.info/?l=bugtraq&m=106917674428552&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7973
- http://docs.info.apple.com/article.html?artnum=61798

---

#### 1038. CVE-2003-0885

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.

**参考链接 / References**:
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286

---

#### 1039. CVE-2003-1091

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Integer overflow in MP3Broadcaster for Apple QuickTime/Darwin Streaming Server 4.1.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via malformed ID3 tags in MP3 files.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html
- http://securitytracker.com/id?1006822
- http://www.kb.cert.org/vuls/id/148564
- http://www.securityfocus.com/bid/7660
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12054

---

#### 1040. CVE-2003-1123

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sun Java Runtime Environment (JRE) and SDK 1.4.0_01 and earlier allows untrusted applets to access certain information within trusted applets, which allows attackers to bypass the restrictions of the Java security model.

**参考链接 / References**:
- http://secunia.com/advisories/8958
- http://securitytracker.com/id?1006935
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-55100-1
- http://www.kb.cert.org/vuls/id/393292
- http://www.securityfocus.com/bid/7824

---

#### 1041. CVE-2003-1413

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Server 4.1.1 allows remote attackers to determine the existence of arbitrary files by using ".." sequences in the filename parameter and comparing the resulting error messages.

**参考链接 / References**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6992
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11445
- http://securityreason.com/securityalert/3260

---

#### 1042. CVE-2003-1414

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Directory traversal vulnerability in parse_xml.cg Apple Darwin Streaming Server 4.1.2 and Apple Quicktime Streaming Server 4.1.1 allows remote attackers to read arbitrary files via a ... (triple dot) in the filename parameter.

**参考链接 / References**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6990
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11446
- http://securityreason.com/securityalert/3260

---

#### 1043. CVE-2003-1516

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The org.apache.xalan.processor.XSLProcessorVersion class in Java Plug-in 1.4.2_01 allows signed and unsigned applets to share variables, which violates the Java security model and could allow remote attackers to read or write data belonging to a signed applet.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857

---

#### 1044. CVE-2003-0601

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Workgroup Manager in Apple Mac OS X Server 10.2 through 10.2.6 does not disable a password for a new account before it is saved for the first time, which allows remote attackers to gain unauthorized access via the new account before it is saved.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12728
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266

---

#### 1045. CVE-2003-1006

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in cd9660.util in Apple Mac OS X 10.0 through 10.3.2 and Apple Mac OS X Server 10.0 through 10.3.2 may allow local users to execute arbitrary code via a long command line parameter.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.kb.cert.org/vuls/id/878526
- http://www.securityfocus.com/archive/1/347578
- http://www.securityfocus.com/archive/1/347707
- http://www.securityfocus.com/archive/1/348097

---

#### 1046. CVE-2003-1007

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
AppleFileServer (AFS) in Apple Mac OS X 10.2.8 and 10.3.2 does not properly handle certain malformed requests, with unknown impact.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://securitytracker.com/id?1008532
- http://www.securityfocus.com/bid/9264
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14051
- http://docs.info.apple.com/article.html?artnum=61798

---

#### 1047. CVE-2003-1009

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Directory Services in Apple Mac OS X 10.0.2, 10.0.3, 10.2.8, 10.3.2 and Apple Mac OS X Server 10.2 through 10.3.2 accepts authentication server information from unknown LDAP or NetInfo sources as provided by a malicious DHCP server, which allows remote attackers to gain privileges.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=32478
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.carrel.org/dhcp-vuln.html
- http://www.securityfocus.com/bid/9110
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13874

---

#### 1048. CVE-2003-1011

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Apple Mac OS X 10.0 through 10.2.8 allows local users with a USB keyboard to gain unauthorized access by holding down the CTRL and C keys when the system is booting, which crashes the init process and leaves the user in a root shell.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.securityfocus.com/archive/1/343087
- http://www.securityfocus.com/bid/8945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13573
- http://docs.info.apple.com/article.html?artnum=61798

---

#### 1049. CVE-2003-0514

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Apple Safari allows remote attackers to bypass intended cookie access restrictions on a web application via "%2e%2e" (encoded dot dot) directory traversal sequences in a URL, which causes Safari to send the cookie outside the specified URL subsets, e.g. to a vulnerable application that runs on the same server as the target application.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html

---

#### 1050. CVE-2004-0430

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Stack-based buffer overflow in AppleFileServer for Mac OS X 10.3.3 and earlier allows remote attackers to execute arbitrary code via a LoginExt packet for a Cleartext Password User Authentication Method (UAM) request with a PathName argument that includes an AFPName type string that is longer than the associated length field.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00049.html
- http://secunia.com/advisories/11539
- http://securitytracker.com/id?1010039
- http://www.atstake.com/research/advisories/2004/a050304-1.txt
- http://www.kb.cert.org/vuls/id/648406

---

#### 1051. CVE-2004-0431

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime (QuickTime.qts) before 6.5.1 allows attackers to execute arbitrary code via a large "number of entries" field in the sample-to-chunk table data for a .mov movie file, which leads to a heap-based buffer overflow.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00048.html
- http://marc.info/?l=bugtraq&m=108360110618389&w=2
- http://marc.info/?l=ntbugtraq&m=108356485013237&w=2
- http://www.kb.cert.org/vuls/id/782958
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16026

---

#### 1052. CVE-2004-0723

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Microsoft Java virtual machine (VM) 5.0.0.3810 allows remote attackers to bypass sandbox restrictions to read or write certain data between applets from different domains via the "GET/Key" and "PUT/Key/Value" commands, aka "cross-site Java."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16666
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688

---

#### 1053. CVE-2004-0518

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unknown vulnerability in AppleFileServer for Mac OS X 10.3.4, related to "the use of SSH and reporting errors," has unknown impact and attack vectors.

**参考链接 / References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16288
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333

---

#### 1054. CVE-2004-0823

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
OpenLDAP 1.0 through 2.1.19, as used in Apple Mac OS 10.3.4 and 10.3.5 and possibly other operating systems, may allow certain authentication schemes to use hashed (crypt) passwords in the userPassword attribute as if they were plaintext passwords, which allows remote attackers to re-use hashed passwords without decrypting them.

**参考链接 / References**:
- http://secunia.com/advisories/12491/
- http://secunia.com/advisories/17233
- http://secunia.com/advisories/21520
- http://support.avaya.com/elmodocs2/security/ASA-2006-157.htm
- http://www.auscert.org.au/render.html?it=4363

---

#### 1055. CVE-2004-0831

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
McAfee VirusScan 4.5.1 does not drop SYSTEM privileges before allowing users to browse for files via the "System Scan" properties of the System Tray applet, which could allow local users to gain privileges.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17367
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities

---

#### 1056. CVE-2004-1121

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.2.3 allows remote attackers to spoof the URL displayed in the status bar via TABLE tags.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13047/
- http://www.kb.cert.org/vuls/id/925430
- http://www.securityfocus.com/bid/11573
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17909

---

#### 1057. CVE-2004-1081

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Application Framework (AppKit) for Apple Mac OS X 10.2.8 and 10.3.6 does not properly restrict access to a secure text input field, which allows local users to read keyboard input from other applications within the same window session.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18350

---

#### 1058. CVE-2004-1084

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+, which bypass Apache file handles.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml

---

#### 1059. CVE-2004-1085

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Human Interface Toolbox (HIToolBox) for Apple Mac 0S X 10.3.6 allows local users to exit applications via the force-quit key combination, even when the system is running in kiosk mode.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18352

---

#### 1060. CVE-2004-1086

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in PSNormalizer for Apple Mac OS X 10.3.6 allows remote attackers to execute arbitrary code via a crafted PostScript input file.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18354

---

#### 1061. GHSA-9xx5-cv6j-x533 - Admidio: OIDC Token Introspection Endpoint Returns Active for All Tokens Without

**严重程度 / Severity**: MEDIUM | CVSS: 6.8

**漏洞描述 / Description**:
[GitHub] ## Summary

The OIDC token introspection endpoint (`/modules/sso/index.php/oidc/introspect`) always returns `{"active": true}` for every request, regardless of whether a valid token is provided, whether the token is expired, revoked, or completely fabricated. The endpoint performs no authentication of the calling resource server and no validation of the submitted token. Any resource server that relies on this introspection endpoint to validate access tokens will accept all requests as authorized

**参考链接 / References**:
- https://github.com/advisories/GHSA-9xx5-cv6j-x533

---

#### 1062. GHSA-p9w9-87c8-m235 - Admidio Sends SAML Response to Unvalidated Assertion Consumer Service URL from A

**严重程度 / Severity**: HIGH | CVSS: 8.2

**漏洞描述 / Description**:
[GitHub] ## Summary

The SAML IdP implementation in Admidio's SSO module uses the `AssertionConsumerServiceURL` value directly from incoming SAML AuthnRequest messages as the destination for the SAML response, without validating it against the registered ACS URL (`smc_acs_url`) stored in the database for the corresponding service provider client. An attacker who knows the Entity ID of a registered SP client can craft a SAML AuthnRequest with an arbitrary `AssertionConsumerServiceURL`, causing the IdP to

**参考链接 / References**:
- https://github.com/advisories/GHSA-p9w9-87c8-m235

---

#### 1063. GHSA-25cw-98hg-g3cg - Admidio Ignores SAML Signature Validation Result, Processes Forged AuthnRequests

**严重程度 / Severity**: HIGH | CVSS: 8.2

**漏洞描述 / Description**:
[GitHub] ## Summary

The Admidio SAML Identity Provider implementation discards the return value of its `validateSignature()` method at both call sites (`handleSSORequest()` line 418 and `handleSLORequest()` line 613). The method returns error strings on failure rather than throwing exceptions, but the developer believed it would throw (per comments on lines 416 and 611). This means the `smc_require_auth_signed` configuration option is completely ineffective — unsigned or invalidly-signed SAML AuthnReque

**参考链接 / References**:
- https://github.com/advisories/GHSA-25cw-98hg-g3cg

---

#### 1064. GHSA-rw74-vc9h-534j - Admidio has CSRF on Admin Preferences that Triggers Unauthorized Backup, .htacce

**严重程度 / Severity**: LOW | CVSS: 3.5

**漏洞描述 / Description**:
[GitHub] ## Summary

Several administrative operations in Admidio's preferences module (database backup, test email, htaccess generation) fire via GET requests with no CSRF token validation. Because `SameSite=Lax` cookies travel with top-level GET navigations, an attacker forces an authenticated admin to trigger these actions from a malicious page.

## Details

In `modules/preferences.php`, the `backup`, `test_email`, and `htaccess` modes accept GET parameters with no CSRF token check:

```php
// modules

**参考链接 / References**:
- https://github.com/advisories/GHSA-rw74-vc9h-534j

---

#### 1065. GHSA-c7xm-r6vj-8vg6 - Admidio Missing Minimum Administrator Check in Role Membership Removal

**严重程度 / Severity**: MEDIUM | CVSS: 5.2

**漏洞描述 / Description**:
[GitHub] ## Summary

`Role::stopMembership()` does not verify whether removing a user from the administrator role leaves zero administrators. The deprecated `Membership::stopMembership()` contains this safety check, but the current code path bypasses it. Any administrator can remove the last remaining other administrator, locking the entire system out of administrative access. The exploit does not require concurrent requests; sequential removals produce the same result.

## Details

`Role::stopMembership

**参考链接 / References**:
- https://github.com/advisories/GHSA-c7xm-r6vj-8vg6

---

#### 1066. GHSA-gq27-fc8w-vcmp - Admidio vulnerable to reflected XSS in msg_window.php via Square Bracket to HTML

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
[GitHub] ## Summary

An unauthenticated attacker can execute arbitrary JavaScript in any Admidio user's browser through a reflected XSS in `system/msg_window.php`. The endpoint passes user input through `htmlspecialchars()`, which does not encode square brackets. A subsequent call to `Language::prepareTextPlaceholders()` converts those brackets into HTML angle brackets, producing executable markup.

## Details

The `msg_window.php` endpoint accepts `message_id` and `message_var1` as GET parameters. At li

**参考链接 / References**:
- https://github.com/advisories/GHSA-gq27-fc8w-vcmp

---

#### 1067. GHSA-rh3w-4ccx-prf9 - Admidio has Inverted 2FA Reset Authorization Check that Lets Group Leaders Strip

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
[GitHub] ## Summary

A logic error in Admidio's two-factor authentication reset inverts the authorization check. Non-admin users cannot remove their own TOTP configuration, but they can remove other users' TOTP, including administrators. A group leader with profile edit rights on an admin account can strip that admin's 2FA.

## Details

In `modules/profile/two_factor_authentication.php` at line 84, the authorization check uses an inverted condition:

```php
// modules/profile/two_factor_authentication.ph

**参考链接 / References**:
- https://github.com/advisories/GHSA-rh3w-4ccx-prf9

---

#### 1068. GHSA-68pr-7prh-mpv4 - Admidio Leaks Hidden Profile Field Values via Blind Search Oracle in Member Assi

**严重程度 / Severity**: LOW | CVSS: 2.7

**漏洞描述 / Description**:
[GitHub] ## Summary

The member assignment DataTables endpoint (`members_assignment_data.php`) includes hidden profile fields (BIRTHDAY, STREET, CITY, POSTCODE, COUNTRY) in its SQL search condition regardless of field visibility settings. While the JSON output correctly suppresses hidden columns via `isVisible()` checks, the server-side search operates at the SQL level before any visibility filtering. This allows a role leader with assign-only permissions to infer hidden PII values by observing which use

**参考链接 / References**:
- https://github.com/advisories/GHSA-68pr-7prh-mpv4

---

#### 1069. GHSA-xqv4-xm7h-52cv - Admidio's Missing Authorization on Inventory Module Destructive Endpoints Allows

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
[GitHub] ## Summary

The Admidio inventory module enforces authorization for destructive operations (delete, retire, reinstate) only in the UI layer by conditionally rendering buttons. The backend POST handlers at `modules/inventory.php` for `item_delete`, `item_retire`, `item_reinstate`, `item_picture_upload`, `item_picture_save`, and `item_picture_delete` perform CSRF validation but never check whether the requesting user is an inventory administrator. Any authenticated user who can access the inventor

**参考链接 / References**:
- https://github.com/advisories/GHSA-xqv4-xm7h-52cv

---

#### 1070. GHSA-g8p8-94f2-28gr - Admidio Exposes Cross-Organization Member Data via Permission Check Mismatch in

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
[GitHub] ## Summary

The `contacts_data.php` endpoint uses a weaker permission check (`isAdministratorUsers()`, requiring only `rol_edit_user=true`) than the frontend UI (`contacts.php`) which correctly requires the stronger `isAdministrator()` (requiring `rol_administrator=true`) and the `contacts_show_all` system setting. A user manager who is not a full administrator can directly request `contacts_data.php?mem_show_filter=3` to retrieve all user records across all organizations in the Admidio instance

**参考链接 / References**:
- https://github.com/advisories/GHSA-g8p8-94f2-28gr

---

#### 1071. GHSA-m9h6-8pqm-xrhf - Admidio has Path Traversal via Unvalidated `name` Parameter in Document Add Mode

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
[GitHub] ## Summary

The `add` mode in `modules/documents-files.php` accepts a `name` parameter validated only as `'string'` type (HTML encoding), allowing path traversal characters (`../`) to pass through unfiltered. Combined with the absence of CSRF protection on this endpoint and `SameSite=Lax` session cookies, a low-privileged attacker can trick a documents administrator into clicking a crafted link that registers an arbitrary server file (e.g., `install/config.php` containing database credentials) i

**参考链接 / References**:
- https://github.com/advisories/GHSA-m9h6-8pqm-xrhf

---

#### 1072. GHSA-m3vp-3jjm-gpmx - Admidio has Path Traversal in ECard Preview that Allows Reading Arbitrary Server

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
[GitHub] ## Summary

The `ecard_preview.php` endpoint does not validate that the `ecard_template` POST parameter is a safe filename before passing it to `ECard::getEcardTemplate()`. An authenticated user can supply a path traversal payload (e.g., `../config.php`) to read arbitrary files accessible to the web server process, including `adm_my_files/config.php` which contains database credentials.

## Details

**Root Cause:** The `ecard_template` parameter is a select box whose value is only sanitized via

**参考链接 / References**:
- https://github.com/advisories/GHSA-m3vp-3jjm-gpmx

---

#### 1073. GHSA-gfg9-5357-hv4c - OpenClaw: Webchat audio embedding could read local files without local-root cont

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub] ## Impact

OpenClaw deployments before `2026.4.15` could embed host-local audio files into webchat responses without applying the local media root containment check used by other media-serving paths.

If an attacker could influence an agent or tool-produced `ReplyPayload.mediaUrl`, the webchat audio embedding helper could resolve an absolute local path or `file:` URL, read an audio-like file under the size cap, and base64-encode it into the webchat media response. This crossed the model/tool-out

**参考链接 / References**:
- https://github.com/advisories/GHSA-gfg9-5357-hv4c

---

#### 1074. GHSA-c28g-vh7m-fm7v - OpenClaw: Owner-enforced commands could accept wildcard channel senders as comma

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[GitHub] ## Impact

OpenClaw deployments before `2026.4.21` could treat a non-owner sender as authorized for owner-enforced slash commands when all of the following were true:

- a channel plugin declared `commands.enforceOwnerForCommands: true`;
- the channel accepted wildcard inbound senders with `allowFrom: ["*"]`;
- no explicit `commands.ownerAllowFrom` was configured.

In that state, `src/auto-reply/command-auth.ts` reused the channel inbound wildcard as part of the command-owner decision. A sender

**参考链接 / References**:
- https://github.com/advisories/GHSA-c28g-vh7m-fm7v

---

#### 1075. GHSA-hqr4-h3xv-9m3r - n8n has XML Node Prototype Pollution that to RCE

**严重程度 / Severity**: CRITICAL | CVSS: 10.0

**漏洞描述 / Description**:
[GitHub] ## Impact
An authenticated user with permission to create or modify workflows could achieve global prototype pollution via the XML Node leading to RCE when combined with other nodes exploiting the prototype pollution.

## Patches
The issue has been fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1. Users should upgrade to one of these versions or later to remediate the vulnerability.

## Workarounds
If upgrading is not immediately possible, administrators should consider the following temporary

**参考链接 / References**:
- https://github.com/advisories/GHSA-hqr4-h3xv-9m3r

---

#### 1076. GHSA-q5f4-99jv-pgg5 - n8n has Prototype Pollution in XML Webhook Body Parser that Leads to RCE

**严重程度 / Severity**: CRITICAL | CVSS: 10.0

**漏洞描述 / Description**:
[GitHub] ## Impact
A flaw in the `xml2js` library used to parse XML request bodies in n8n's webhook handler allowed prototype pollution via a crafted XML payload. An authenticated user with permission to create or modify workflows could exploit this to pollute the JavaScript object prototype and, by chaining the pollution with the Git node's SSH operations, achieve remote code execution on the n8n host.

## Patches
The issue has been fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1. Users should upgrad

**参考链接 / References**:
- https://github.com/advisories/GHSA-q5f4-99jv-pgg5

---

#### 1077. GHSA-537j-gqpc-p7fq - n8n Vulnerable to XSS via MCP OAuth client

**严重程度 / Severity**: HIGH | CVSS: 8.2

**漏洞描述 / Description**:
[GitHub] ## Impact
An unauthenticated attacker could register a malicious MCP OAuth client with a crafted `client_name`. If a victim user authorized the OAuth consent dialog and a second user subsequently revoked that access, a toast notification would render the injected script. Clicking the link would execute arbitrary JavaScript in the victim's authenticated n8n browser session, enabling credential and session token theft, workflow manipulation, or privilege escalation.

## Patches
This issue has been

**参考链接 / References**:
- https://github.com/advisories/GHSA-537j-gqpc-p7fq

---

#### 1078. GHSA-r4v6-9fqc-w5jr - n8n's Credential Authorization Bypass in dynamic-node-parameters Allows Foreign

**严重程度 / Severity**: HIGH | CVSS: 8.5

**漏洞描述 / Description**:
[GitHub] ## Impact
The `dynamic-node-parameters` endpoints did not verify whether the authenticated caller was authorized to use a supplied credential reference. An authenticated user with access to a shared workflow could supply a foreign credential ID in the request body, causing the backend to decrypt and use that credential in a helper execution path where the caller also controls the destination URL. This allowed the caller to force the backend to authenticate against attacker-controlled infrastruct

**参考链接 / References**:
- https://github.com/advisories/GHSA-r4v6-9fqc-w5jr

---

#### 1079. GHSA-44v6-jhgm-p3m4 - n8n has a Python Task Runner Sandbox Escape Vulnerability

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
[GitHub] ## Impact
An authenticated user with permission to create or modify workflows containing a Python Code Node could escape the sandbox and achieve arbitrary code execution on the task runner container.

- This issue only affects instances where the Python Task Runner is enabled.

## Patches
The issue has been fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1. Users should upgrade to one of these versions or later to remediate the vulnerability.

## Workarounds
If upgrading is not immediately poss

**参考链接 / References**:
- https://github.com/advisories/GHSA-44v6-jhgm-p3m4

---

#### 1080. GHSA-756q-gq9h-fp22 - n8n has Public API Variables IDOR that Allows Cross-Project Secret Disclosure

**严重程度 / Severity**: MEDIUM | CVSS: 7.7

**漏洞描述 / Description**:
[GitHub] ## Impact
An authenticated user with a valid API key scoped to `variable:list` could read variables from projects they are not a member of by supplying an arbitrary `projectId` query parameter to the public API variables endpoint. The handler queried the variables repository directly without enforcing project membership checks, bypassing the authorization-aware service layer used by the internal enterprise controller. 

If variables were misused to store sensitive information such as credentials

**参考链接 / References**:
- https://github.com/advisories/GHSA-756q-gq9h-fp22

---

#### 1081. CVE-2000-0156

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Internet Explorer 4.x and 5.x allows remote web servers to access files on the client that are outside of its security domain, aka the "Image Source Redirect" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/7827
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-009
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3996
- http://www.osvdb.org/7827
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-009

---

#### 1082. CVE-2000-0264

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Panda Security 3.0 with registry editing disabled allows users to edit the registry and gain privileges by directly executing a .reg file or using other methods.

**参考链接 / References**:
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FB45F2.550EA000%40teleline.es
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119

---

#### 1083. CVE-2000-0083

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
HP asecure creates the Audio Security File audio.sec with insecure permissions, which allows local users to cause a denial of service or gain additional privileges.

**参考链接 / References**:
- http://www.securityfocus.com/templates/advisory.html?id=2031
- http://www.securityfocus.com/templates/advisory.html?id=2031

---

#### 1084. CVE-2000-0334

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Allaire Spectra container editor preview tool does not properly enforce object security, which allows an attacker to conduct unauthorized activities via an object-method that is added to the container object with a publishing rule.

**参考链接 / References**:
- http://www.allaire.com/handlers/index.cfm?ID=15411&Method=Full
- http://www.securityfocus.com/bid/1181
- http://www.allaire.com/handlers/index.cfm?ID=15411&Method=Full
- http://www.securityfocus.com/bid/1181

---

#### 1085. CVE-2000-0385

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
FileMaker Pro 5 Web Companion allows remote attackers to bypass Field-Level database security restrictions via the XML publishing or email capabilities.

**参考链接 / References**:
- http://www.blueworld.com/blueworld/news/05.01.00-FM5_Security.html
- http://www.filemaker.com/support/webcompanion.html
- http://www.blueworld.com/blueworld/news/05.01.00-FM5_Security.html
- http://www.filemaker.com/support/webcompanion.html

---

#### 1086. CVE-2000-0503

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
The IFRAME of the WebBrowser control in Internet Explorer 5.01 allows a remote attacker to violate the cross frame security policy via the NavigateComplete2 event.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q2/0154.html
- http://www.securityfocus.com/bid/1311
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q2/0154.html
- http://www.securityfocus.com/bid/1311

---

#### 1087. CVE-2000-0562

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
BlackIce Defender 2.1 and earlier, and BlackIce Pro 2.0.23 and earlier, do not properly block Back Orifice traffic when the security setting is Nervous or lower.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0190.html
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0190.html

---

#### 1088. CVE-2000-0582

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Check Point FireWall-1 4.0 and 4.1 allows remote attackers to cause a denial of service by sending a stream of invalid commands (such as binary zeros) to the SMTP Security Server proxy.

**参考链接 / References**:
- http://www.checkpoint.com/techsupport/alerts/list_vun.html#SMTP_Security
- http://www.osvdb.org/1438
- http://www.securityfocus.com/bid/1416
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630162106.4619C-100000%40fjord.fscinternet.com
- http://www.checkpoint.com/techsupport/alerts/list_vun.html#SMTP_Security

---

#### 1089. CVE-2000-1207

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
userhelper in the usermode package on Red Hat Linux executes non-setuid programs as root, which does not activate the security measures in glibc and allows the programs to be exploited via format string vulnerabilities in glibc via the LANG or LC_ALL environment variables (CVE-2000-0844).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97034397026473&w=2
- http://marc.info/?l=bugtraq&m=97063854808796&w=2
- http://www.linux-mandrake.com/en/security/2000/MDKSA-2000-059.php3
- http://www.redhat.com/support/errata/RHSA-2000-075.html
- http://marc.info/?l=bugtraq&m=97034397026473&w=2

---

#### 1090. CVE-2000-0712

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux Intrusion Detection System (LIDS) 0.9.7 allows local users to gain root privileges when LIDS is disabled via the security=0 boot option.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0486.html
- http://www.egroups.com/message/lids/1038
- http://www.lids.org/changelog.html
- http://www.osvdb.org/1495
- http://www.securityfocus.com/bid/1549

---

#### 1091. CVE-2000-1211

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Zope 2.2.0 through 2.2.4 does not properly perform security registration for legacy names of object constructors such as DTML method objects, which could allow attackers to perform unauthorized activities.

**参考链接 / References**:
- http://www.iss.net/security_center/static/5824.php
- http://www.linux-mandrake.com/en/security/2000/MDKSA-2000-083.php3
- http://www.osvdb.org/6282
- http://www.redhat.com/support/errata/RHSA-2000-125.html
- http://www.zope.org/Products/Zope/Hotfix_2000-12-08/security_alert

---

#### 1092. CVE-2000-1241

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in Haakon Nilsen simple, integrated publishing system (SIPS) before 0.2.4 has an unknown impact and attack vectors, related to a "grave security fault."

**参考链接 / References**:
- http://sourceforge.net/forum/forum.php?forum_id=25971
- http://sourceforge.net/forum/forum.php?forum_id=25971

---

#### 1093. CVE-2000-1039

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Various TCP/IP stacks and network applications allow remote attackers to cause a denial of service by flooding a target host with TCP connection attempts and completing the TCP/IP handshake without maintaining the connection state on the attacker host, aka the "NAPTHA" class of vulnerabilities.  NOTE: this candidate may change significantly as the security community discusses the technical nature of NAPTHA and learns more about the affected applications. This candidate is at a higher level of abstraction than is typical for CVE.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0105.html
- http://razor.bindview.com/publish/advisories/adv_NAPTHA.html
- http://www.cert.org/advisories/CA-2000-21.html
- http://www.securityfocus.com/bid/2022
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-091

---

#### 1094. CVE-2001-0073

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Buffer overflow in the find_default_type function in libsecure in NSA Security-enhanced Linux, which may allow attackers to modify critical data in memory.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/153188
- http://www.securityfocus.com/bid/2154
- http://www.securityfocus.com/archive/1/153188
- http://www.securityfocus.com/bid/2154

---

#### 1095. CVE-2001-0104

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
MDaemon Pro 3.5.1 and earlier allows local users to bypass the "lock server" security setting by pressing the Cancel button at the password prompt, then pressing the enter key.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/151156
- http://www.securityfocus.com/bid/2115
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5763
- http://www.securityfocus.com/archive/1/151156
- http://www.securityfocus.com/bid/2115

---

#### 1096. CVE-1999-0756

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ColdFusion Administrator with Advanced Security enabled allows remote users to stop the ColdFusion server via the Start/Stop utility.

**参考链接 / References**:
- http://www.allaire.com/handlers/index.cfm?ID=10968&Method=Full
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2207
- http://www.allaire.com/handlers/index.cfm?ID=10968&Method=Full
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2207

---

#### 1097. CVE-2001-0016

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
NTLM Security Support Provider (NTLMSSP) service does not properly check the function number in an LPC request, which could allow local users to gain administrator level access.

**参考链接 / References**:
- http://razor.bindview.com/publish/advisories/adv_NTLMSSP.html
- http://www.securityfocus.com/bid/2348
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-008
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6076
- http://razor.bindview.com/publish/advisories/adv_NTLMSSP.html

---

#### 1098. CVE-2001-0310

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
sort in FreeBSD 4.1.1 and earlier, and possibly other operating systems, uses predictable temporary file names and does not properly handle when the temporary file already exists, which causes sort to crash and possibly impacts security-sensitive scripts.

**参考链接 / References**:
- ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:13.sort.asc
- http://www.securityfocus.com/bid/3960
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6038
- ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:13.sort.asc
- http://www.securityfocus.com/bid/3960

---

#### 1099. CVE-2001-0364

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
SSH Communications Security sshd 2.4 for Windows allows remote attackers to create a denial of service via a large number of simultaneous connections.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98467799732241&w=2
- http://www.securityfocus.com/bid/2477
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6241
- http://marc.info/?l=bugtraq&m=98467799732241&w=2
- http://www.securityfocus.com/bid/2477

---

#### 1100. CVE-2001-1182

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in login in HP-UX 11.00, 11.11, and 10.20 allows restricted shell users to bypass certain security checks and gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/hp/2001-q3/0014.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5657
- http://archives.neohapsis.com/archives/hp/2001-q3/0014.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5657

---

#### 1101. CVE-2001-1302

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The change password option in the Windows Security interface for Windows 2000 allows attackers to use the option to attempt to change passwords of other users on other systems or identify valid accounts by monitoring error messages, possibly due to a problem in the NetuserChangePassword function.

**参考链接 / References**:
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind0107&L=ntbugtraq&F=P&S=&P=1911
- http://www.securityfocus.com/bid/3063
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6876
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind0107&L=ntbugtraq&F=P&S=&P=1911
- http://www.securityfocus.com/bid/3063

---

#### 1102. CVE-2001-1361

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in The Web Information Gateway (TWIG) 2.7.1, possibly related to incorrect security rights and/or the generation of mailto links.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2001-q3/0005.html
- http://twig.screwdriver.net/file.php3?file=CHANGELOG
- http://archives.neohapsis.com/archives/vulnwatch/2001-q3/0005.html
- http://twig.screwdriver.net/file.php3?file=CHANGELOG

---

#### 1103. CVE-2001-1016

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
PGP Corporate Desktop before 7.1, Personal Security before 7.0.3, Freeware before 7.0.3, and E-Business Server before 7.1 does not properly display when invalid userID's are used to sign a message, which could allow an attacker to make the user believe that the document has been signed by a trusted third party by adding a second, invalid user ID to a key which has already been signed by the third party, aka the "PGPsdk Key Validity Vulnerability."

**参考链接 / References**:
- http://www.osvdb.org/1946
- http://www.pgp.com/support/product-advisories/pgpsdk.asp
- http://www.securityfocus.com/archive/1/211806
- http://www.securityfocus.com/bid/3280
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7081

---

#### 1104. CVE-2001-1407

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Bugzilla before 2.14 allows Bugzilla users to bypass group security checks by marking a bug as the duplicate of a restricted bug, which adds the user to the CC list of the restricted bug and allows the user to view the bug.

**参考链接 / References**:
- http://bugzilla.mozilla.org/show_bug.cgi?id=96085
- http://marc.info/?l=bugtraq&m=99912899900567
- http://www.iss.net/security_center/static/10479.php
- http://www.redhat.com/support/errata/RHSA-2001-107.html
- http://bugzilla.mozilla.org/show_bug.cgi?id=96085

---

#### 1105. CVE-2001-0546

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in H.323 Gatekeeper Service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service (resource exhaustion) via a large amount of malformed H.323 data.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3196
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6989
- http://www.securityfocus.com/bid/3196
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045

---

#### 1106. CVE-2001-0547

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Memory leak in the proxy service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows local attackers to cause a denial of service (resource exhaustion).

**参考链接 / References**:
- http://www.securityfocus.com/bid/3197
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6990
- http://www.securityfocus.com/bid/3197
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045

---

#### 1107. CVE-2001-0658

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Cross-site scripting (CSS) vulnerability in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause other clients to execute certain script or read cookies via malicious script in an invalid URL that is not properly quoted in an error message.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3198
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6991
- http://www.securityfocus.com/bid/3198
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-045

---

#### 1108. CVE-2001-1414

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Basic Security Module (BSM) for Solaris 2.5.1, 2.6, 7, and 8 does not log anonymous FTP access, which allows remote attackers to hide their activities, possibly when certain BSM audit files are not present under the FTP root.

**参考链接 / References**:
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-40521-1
- http://www.securityfocus.com/bid/7396
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11841
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-40521-1
- http://www.securityfocus.com/bid/7396

---

#### 1109. CVE-2001-1227

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Zope before 2.2.4 allows partially trusted users to bypass security controls for certain methods by accessing the methods through the fmt attribute of dtml-var tags.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-080.php3
- http://www.redhat.com/support/errata/RHSA-2001-072.html
- http://www.redhat.com/support/errata/RHSA-2001-115.html
- http://www.securityfocus.com/bid/3425
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7271

---

#### 1110. CVE-2001-1278

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Zope before 2.2.4 allows partially trusted users to bypass security controls for certain methods by accessing the methods through the fmt attribute of dtml-var tags.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-080.php3
- http://www.redhat.com/support/errata/RHSA-2001-115.html
- http://www.securityfocus.com/bid/3425
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-080.php3
- http://www.redhat.com/support/errata/RHSA-2001-115.html

---

#### 1111. CVE-2001-1461

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Directory traversal vulnerability in WebID in RSA Security SecurID 5.0 as used by ACE/Agent for Windows, Windows NT and Windows 2000 allows attackers to access restricted resources via URL-encoded (1) /.. or (2) \.. sequences.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/348040
- http://www.securityfocus.com/bid/3461
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7397
- http://www.kb.cert.org/vuls/id/348040
- http://www.securityfocus.com/bid/3461

---

#### 1112. CVE-2001-1462

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
WebID in RSA Security SecurID 5.0 as used by ACE/Agent for Windows, Windows NT and Windows 2000 allows attackers to cause the WebID agent to enter debug mode via a URL containing null characters, which may allow attackers to obtain sensitive information.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/609840
- http://www.securityfocus.com/bid/3462
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7399
- http://www.kb.cert.org/vuls/id/609840
- http://www.securityfocus.com/bid/3462

---

#### 1113. CVE-2001-0664

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.5 and 5.01 allows remote attackers to bypass security restrictions via malformed URLs that contain dotless IP addresses, which causes Internet Explorer to process the page in the Intranet Zone, which may have fewer security restrictions, aka the "Zone Spoofing vulnerability."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100281551611595&w=2
- http://morph3us.org/blog/?p=31
- http://www.osvdb.org/1971
- http://www.securityfocus.com/bid/3420
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-051

---

#### 1114. CVE-2001-0724

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.5 allows remote attackers to bypass security restrictions via malformed URLs that contain dotless IP addresses, which causes Internet Explorer to process the page in the Intranet Zone, which may have fewer security restrictions, aka the "Zone Spoofing Vulnerability variant" of CVE-2001-0664.

**参考链接 / References**:
- http://www.osvdb.org/5556
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-055
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8471
- http://www.osvdb.org/5556
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-055

---

#### 1115. CVE-2001-0831

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Unknown vulnerability in Oracle Label Security in Oracle 8.1.7 and 9.0.1, when audit functionality, SET_LABEL, or SQL*Predicate is being used, allows local users to gain additional access.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100386756715645&w=2
- http://otn.oracle.com/deploy/security/pdf/OLS817alert.pdf
- http://www.iss.net/security_center/static/7344.php
- http://www.securityfocus.com/bid/3465
- http://marc.info/?l=bugtraq&m=100386756715645&w=2

---

#### 1116. CVE-2001-0832

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in Oracle 8.0.x through 9.0.1 on Unix allows local users to overwrite arbitrary files, possibly via a symlink attack or incorrect file permissions in (1) the ORACLE_HOME/rdbms/log directory or (2) an alternate directory as specified in the ORACLE_HOME environmental variable, aka the "Oracle File Overwrite Security Vulnerability."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100386756715645&w=2
- http://otn.oracle.com/deploy/security/pdf/oracle_race.pdf
- http://marc.info/?l=bugtraq&m=100386756715645&w=2
- http://otn.oracle.com/deploy/security/pdf/oracle_race.pdf

---

#### 1117. CVE-2001-0833

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in otrcrep in Oracle 8.0.x through 9.0.1 allows local users to execute arbitrary code via a long ORACLE_HOME environment variable, aka the "Oracle Trace Collection Security Vulnerability."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100386756715645&w=2
- http://online.securityfocus.com/archive/1/201295
- http://online.securityfocus.com/archive/1/222612
- http://otn.oracle.com/deploy/security/pdf/otrcrep.pdf
- http://www.ciac.org/ciac/bulletins/m-011.shtml

---

#### 1118. CVE-2001-1190

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The default PAM files included with passwd in Mandrake Linux 8.1 do not support MD5 passwords, which could result in a lower level of password security than intended.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7706.php
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-091.php3
- http://www.securityfocus.com/bid/3683
- http://www.iss.net/security_center/static/7706.php
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-091.php3

---

#### 1119. CVE-2001-1514

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
ColdFusion 4.5 and 5, when running on Windows with the advanced security sandbox type set to "operating system," does not properly pass security context to (1) child processes created with <CFEXECUTE> and (2) child processes that call the CreateProcess function and are executed with <CFOBJECT> or end with the CFX extension, which allows attackers to execute programs with the permissions of the System account.

**参考链接 / References**:
- http://www.macromedia.com/v1/Handlers/index.cfm?ID=22263
- http://www.macromedia.com/v1/Handlers/index.cfm?ID=22263

---

#### 1120. CVE-2001-1533

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service via a flood of fragmented UDP packets.  NOTE: the vendor disputes this issue, saying that it requires high bandwidth to exploit, and the server does not experience any instability.  Therefore this "laws of physics" issue might not be included in CVE

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00018.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00031.html
- http://www.iss.net/security_center/static/7446.php
- http://www.securityfocus.com/bid/3501
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00018.html

---
