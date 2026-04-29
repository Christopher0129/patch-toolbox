# 网络安全漏洞知识库 | Network Security Vulnerability Knowledge Base

> 本知识库汇总公开披露的网络安全漏洞信息，包含 CVE 编号、严重程度、漏洞描述及缓解方案。
> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> This knowledge base aggregates publicly disclosed network security vulnerabilities. Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.

**总计条目 / Total entries: 452**

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

OpenClaw now blocks `MINIMAX_API_HOST` from

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

`DELETE /api/books/{bookID}` sets `books.deleted_at` to the current time. The book-level endpoint starts

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
