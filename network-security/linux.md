# Linux 网络安全漏洞 | Linux Network Security

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 1098**

> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.

---

#### 1. CVE-1999-1182

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

#### 2. CVE-1999-1225

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
rpc.mountd on Linux, Ultrix, and possibly other operating systems, allows remote attackers to determine the existence of a file on the server by attempting to mount that file, which generates different error messages depending on whether the file exists or not.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/7526
- https://exchange.xforce.ibmcloud.com/vulnerabilities/347
- http://www.securityfocus.com/archive/1/7526
- https://exchange.xforce.ibmcloud.com/vulnerabilities/347

---

#### 3. CVE-1999-0183

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Linux implementations of TFTP would allow access to files outside the restricted directory.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0183
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0183

---

#### 4. CVE-1999-0216

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service of inetd on Linux through SYN and RST packets.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0216
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0216

---

#### 5. CVE-1999-0340

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux Slackware crond program allows local users to gain root access.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0340
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0340

---

#### 6. CVE-1999-0341

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the Linux mail program "deliver" allows local users to gain root access.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0341
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0341

---

#### 7. CVE-1999-1229

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Quake 2 server 3.13 on Linux does not properly check file permissions for the config.cfg configuration file, which allows local users to read arbitrary files via a symlink from config.cfg to the target file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/8590
- https://exchange.xforce.ibmcloud.com/vulnerabilities/733
- http://www.securityfocus.com/archive/1/8590
- https://exchange.xforce.ibmcloud.com/vulnerabilities/733

---

#### 8. CVE-1999-0330

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux bdash game has a buffer overflow that allows local users to gain root access.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=87602558319119&w=2
- https://marc.info/?l=bugtraq&m=87602558319119&w=2

---

#### 9. CVE-1999-1407

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

#### 10. CVE-1999-1498

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Slackware Linux 3.4 pkgtool allows local attacker to read and write to arbitrary files via a symlink attack on the reply file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/82
- http://www.securityfocus.com/bid/82

---

#### 11. CVE-1999-1442

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

#### 12. CVE-1999-1441

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux 2.0.34 does not properly prevent users from sending SIGIO signals to arbitrary processes, which allows local users to cause a denial of service by sending SIGIO to processes that do not catch it.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221103126047&w=2
- http://www.securityfocus.com/bid/111
- http://marc.info/?l=bugtraq&m=90221103126047&w=2
- http://www.securityfocus.com/bid/111

---

#### 13. CVE-1999-1434

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
login in Slackware Linux 3.2 through 3.5 does not properly check for an error when the /etc/group file is missing, which prevents it from dropping privileges, causing it to assign root privileges to any local user who logs on to the server.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221104525951&w=2
- http://www.securityfocus.com/bid/155
- http://marc.info/?l=bugtraq&m=90221104525951&w=2
- http://www.securityfocus.com/bid/155

---

#### 14. CVE-1999-1406

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

#### 15. CVE-1999-0262

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Hylafax faxsurvey CGI script on Linux allows remote attackers to execute arbitrary commands via shell metacharacters in the query string.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2056
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1532
- http://www.securityfocus.com/bid/2056
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1532

---

#### 16. CVE-1999-1381

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in dbadmin CGI program 1.0.1 on Linux allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90786656409618&w=2
- http://marc.info/?l=bugtraq&m=90786656409618&w=2

---

#### 17. CVE-1999-0002

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

#### 18. CVE-1999-0342

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Linux PAM modules allow local users to gain root access using temporary files.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0342
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0342

---

#### 19. CVE-1999-0798

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in bootpd on OpenBSD, FreeBSD, and Linux systems via a malformed header type.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91278867118128&w=2
- http://marc.info/?l=bugtraq&m=91278867118128&w=2

---

#### 20. CVE-1999-1173

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Corel Word Perfect 8 for Linux creates a temporary working directory with world-writable permissions, which allows local users to (1) modify Word Perfect behavior by modifying files in the working directory, or (2) modify files of other users via a symlink attack.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91404045014047&w=2
- http://marc.info/?l=bugtraq&m=91404045014047&w=2

---

#### 21. CVE-1999-1285

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux 2.1.132 and earlier allows local users to cause a denial of service (resource exhaustion) by reading a large buffer from a random device (e.g. /dev/urandom), which cannot be interrupted until the read has completed.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91495921611500&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1472
- http://marc.info/?l=bugtraq&m=91495921611500&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1472

---

#### 22. CVE-1999-0243

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Linux cfingerd could be exploited to gain root access.

**参考链接 / References**:
- http://www.geocrawler.com/archives/3/92/1996/9/0/2217716/
- http://www.geocrawler.com/archives/3/92/1996/9/0/2217716/

---

#### 23. CVE-1999-0398

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
In some instances of SSH 1.2.27 and 2.0.11 on Linux systems, SSH will allow users with expired accounts to login.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0398
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0398

---

#### 24. CVE-1999-0401

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
A race condition in Linux 2.2.1 allows local users to read arbitrary memory from /proc files.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0401
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0401

---

#### 25. CVE-1999-0698

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Denial of service in IP protocol logger (ippl) on Red Hat and Debian Linux.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0698
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0698

---

#### 26. CVE-1999-0389

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the bootp server in the Debian Linux netstd package.

**参考链接 / References**:
- http://www.securityfocus.com/bid/324
- http://www.securityfocus.com/bid/324

---

#### 27. CVE-1999-0390

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Dosemu Slang library in Linux.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-006.1.txt
- http://www.securityfocus.com/bid/187
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-006.1.txt
- http://www.securityfocus.com/bid/187

---

#### 28. CVE-1999-0457

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux ftpwatch program allows local users to gain root privileges.

**参考链接 / References**:
- http://www.securityfocus.com/bid/317
- http://www.securityfocus.com/bid/317

---

#### 29. CVE-1999-0451

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Denial of service in Linux 2.0.36 allows local users to prevent any server from listening on any non-privileged port.

**参考链接 / References**:
- http://www.securityfocus.com/bid/343
- http://www.securityfocus.com/bid/343

---

#### 30. CVE-1999-0400

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Denial of service in Linux 2.2.0 running the ldd command on a core file.

**参考链接 / References**:
- http://www.securityfocus.com/bid/344
- http://www.securityfocus.com/bid/344

---

#### 31. CVE-1999-0461

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Versions of rpcbind including Linux, IRIX, and Wietse Venema's rpcbind allow a remote attacker to insert and delete entries by spoofing a source address.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0461
- https://www.cve.org/CVERecord?id=CVE-1999-0461

---

#### 32. CVE-2000-0370

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The debug option in Caldera Linux smail allows remote attackers to execute commands via shell metacharacters in the -D option for the rmail command.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-001.0.txt
- http://www.securityfocus.com/bid/1268
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-001.0.txt
- http://www.securityfocus.com/bid/1268

---

#### 33. CVE-1999-0403

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A bug in Cyrix CPUs on Linux allows local users to perform a denial of service.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91821080015725&w=2
- http://marc.info/?l=bugtraq&m=91821080015725&w=2

---

#### 34. CVE-1999-0459

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Local users can perform a denial of service in Alpha Linux, using MILO to force a reboot.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0459
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0459

---

#### 35. CVE-1999-1495

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

#### 36. CVE-1999-0460

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Buffer overflow in Linux autofs module through long directory names allows local users to perform a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/312
- http://www.securityfocus.com/bid/312

---

#### 37. CVE-1999-1168

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
install.iss installation script for Internet Security Scanner (ISS) for Linux, version 5.3, allows local users to change the permissions of arbitrary files via a symlink attack on a temporary file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/12640
- http://www.securityfocus.com/archive/1/12640

---

#### 38. CVE-1999-0414

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
In Linux before version 2.0.36, remote attackers can spoof a TCP connection and pass data to the application layer before fully establishing the connection.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0414
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0414

---

#### 39. CVE-2026-5435 - glibc: glibc: Out-of-bounds write via TSIG record processing

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] glibc: glibc: Out-of-bounds write via TSIG record processing. Bugzilla: 2463465

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463465

---

#### 40. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 41. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 42. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 43. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 44. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 45. CVE-2026-7351 - chromium-browser: Race in MHTML

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Race in MHTML. Bugzilla: 2463656

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463656

---

#### 46. CVE-2026-7353 - chromium-browser: Heap buffer overflow in Skia

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in Skia. Bugzilla: 2463657

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463657

---

#### 47. CVE-2026-7339 - chromium-browser: Heap buffer overflow in WebRTC

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in WebRTC. Bugzilla: 2463658

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463658

---

#### 48. CVE-2026-7341 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463659

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463659

---

#### 49. CVE-2026-7338 - chromium-browser: Use after free in Cast

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Cast. Bugzilla: 2463660

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463660

---

#### 50. CVE-2026-7334 - chromium-browser: Use after free in Views

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Views. Bugzilla: 2463663

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463663

---

#### 51. CVE-2026-7340 - chromium-browser: Integer overflow in ANGLE

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Integer overflow in ANGLE. Bugzilla: 2463664

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463664

---

#### 52. CVE-2026-7358 - chromium-browser: Use after free in Animation

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Animation. Bugzilla: 2463665

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463665

---

#### 53. CVE-2026-7356 - chromium-browser: Use after free in Navigation

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Navigation. Bugzilla: 2463667

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463667

---

#### 54. CVE-2026-7352 - chromium-browser: Use after free in Media

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Media. Bugzilla: 2463669

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463669

---

#### 55. CVE-2026-7359 - chromium-browser: Use after free in ANGLE

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in ANGLE. Bugzilla: 2463670

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463670

---

#### 56. CVE-2026-7348 - chromium-browser: Use after free in Codecs

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Codecs. Bugzilla: 2463671

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463671

---

#### 57. CVE-2026-7336 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463676

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463676

---

#### 58. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 59. [Ubuntu] USN-8223-1: Roundcube Webmail vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that Roundcube Webmail mishandled Punycode xn-- domain names. An attacker could possibly use this issue to cause a homograph attack. (CVE-2019-15237) It was discovered that Roundcube Webmail did not properly sanitize certain attributes when handling CSS within HTML messages and certain SVG attributes. An attacker could possibly use this issue to cause a cross-site scripting attac

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8223-1

---

#### 60. [Ubuntu] USN-8224-1: Linux kernel (BlueField) vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Qualys discovered that several vulnerabilities existed in the AppArmor Linux kernel Security Module (LSM). An unprivileged local attacker could use these issues to load, replace, and remove arbitrary AppArmor profiles causing denial of service, exposure of sensitive information (kernel memory), local privilege escalation, or possibly escape a container. (LP: #2143853, CVE-2026-23268, CVE-2026-2326

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8224-1

---

#### 61. [Ubuntu] USN-8222-1: OpenSSH vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Christos Papakonstantinou discovered that the OpenSSH scp tool incorrectly handled the legacy scp protocol (-O) option. This could result in certain files being installed setuid or setgid, contrary to expectations. (CVE-2026-35385) Florian Kohnhäuser discovered that OpenSSH incorrectly handled shell metacharacters in usernames within a command line. When untrusted usernames and non-default configu

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8222-1

---

#### 62. [Ubuntu] USN-8195-3: PackageKit vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8195-1 fixed a vulnerability in PackageKit. This update provides the corresponding fix to Ubuntu 16.04 LTS, Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. Original advisory details: It was discovered that PackageKit incorrectly handled certain transactions. A local attacker could use this issue to install arbitrary packages as root, possibly resulting in privilege escalation.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8195-3

---

#### 63. [Ubuntu] USN-8221-1: wheel vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that wheel did not correctly handle certain file paths. If a user or automated system were tricked into opening a specially crafted file, an attacker could possibly use this issue to execute arbitrary code.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8221-1

---

#### 64. [Ubuntu] USN-8198-2: Tornado vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8198-1 fixed vulnerabilities in Tornado. This update provides the corresponding updates for Ubuntu 26.04 LTS. Original advisory details: It was discovered that Tornado incorrectly handled parsing of large multipart request bodies. An attacker could possibly use this issue to cause a denial of service. (CVE-2026-31958) It was discovered that Tornado did not properly validate characters in cooki

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8198-2

---

#### 65. [Ubuntu] USN-8219-1: UltraJSON vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Cameron Criswell discovered that UltraJSON contained a memory leak that would occur when parsing large integers. An attacker could possibly use this issue to cause UltraJSON to crash, resulting in a denial of service. This issue only affected Ubuntu 24.04 LTS, Ubuntu 25.10, and Ubuntu 26.04 LTS. (CVE-2026-32874) It was discovered that UltraJSON contained integer overflow/underflow issues when calc

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8219-1

---

#### 66. [Ubuntu] USN-8185-2: Linux kernel (Low Latency NVIDIA) vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Josh Eads, Kristoffer Janke, Eduardo Vela Nava, Tavis Ormandy, and Matteo Rizzo discovered that some AMD Zen processors did not properly verify the signature of CPU microcode. This flaw is known as EntrySign. A privileged attacker could possibly use this issue to cause load malicious CPU microcode causing loss of integrity and confidentiality. (CVE-2024-36347) Several security issues were discover

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8185-2

---

#### 67. [Ubuntu] USN-8217-1: follow-redirects vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that follow-redirects did not properly protect sensitive user information during redirects. An attacker could possibly use this issue to expose sensitive information. This issue only affected Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. (CVE-2022-0155) It was discovered that follow-redirects did not properly remove sensitive information before storage or transfer. An attacker could pos

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8217-1

---

#### 68. [Ubuntu] USN-8190-2: Rack::Session vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8190-1 fixed a vulnerability in Rack::Session. This update provides the corresponding update for Ubuntu 26.04 LTS. Original advisory details: SeungMyung Lee discovered that Rack::Session did not properly reject cookies upon decryption failure. A remote attacker could use this issue to manipulate session contents and possibly gain unauthorized access.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8190-2

---

#### 69. [Arch] AVG-2843

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: vim. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 70. [Arch] AVG-2842

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: libtiff. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 71. [Arch] AVG-2827

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: grunt-cli. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 72. [Arch] AVG-2820

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: wpewebkit. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 73. [Arch] AVG-2818

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: connman. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 74. [Arch] AVG-2816

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: squid. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 75. [Arch] AVG-2809

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: python-django. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 76. [Arch] AVG-2799

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: blender. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 77. [Arch] AVG-2781

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: python-pyjwt. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 78. [Arch] AVG-2780

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: wpewebkit. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 79. [Arch] AVG-2725

**严重程度 / Severity**: UNKNOWN

**漏洞描述 / Description**:
[Arch Linux] Packages: containerd. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 80. [Arch] AVG-2836

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-zen. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 81. [Arch] AVG-2835

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-hardened. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 82. [Arch] AVG-2834

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-lts. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 83. [Arch] AVG-2764

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: ruby-puma. Status: Unknown.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 84. [Arch] AVG-2907

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: djvulibre. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 85. [Arch] AVG-2901

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: pam. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 86. [Arch] AVG-2898

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: libxml2. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 87. [Arch] AVG-2889

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: tomcat9. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 88. [Arch] AVG-2888

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: tomcat10. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 89. [Arch] AVG-2886

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: kea. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 90. [Arch] AVG-2762

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: grub. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 91. [Arch] AVG-2701

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: linux-lts. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 92. [Arch] AVG-2275

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: nim. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 93. [Arch] AVG-2272

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: exim. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 94. [Arch] AVG-2190

**严重程度 / Severity**: HIGH

**漏洞描述 / Description**:
[Arch Linux] Packages: jre8-openjdk-headless, jdk8-openjdk. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 95. [Arch] AVG-2893

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: systemd. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 96. [Arch] AVG-2885

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: coreutils. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 97. [Arch] AVG-2884

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: grafana. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 98. [Arch] AVG-2875

**严重程度 / Severity**: MEDIUM

**漏洞描述 / Description**:
[Arch Linux] Packages: postgresql. Status: Vulnerable.

**参考链接 / References**:
- https://security.archlinux.org/

---

#### 99. [Gentoo] GLSA 202604-04: DTrace: Arbitrary file creation via dtprobed

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A DTrace component, dtprobed, allows arbitrary file creation through crafted USDT provider names.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202604-04

---

#### 100. [Gentoo] GLSA 202604-03: FUSE: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been found in FUSE, the worst of which can lead to code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202604-03

---

#### 101. [Gentoo] GLSA 202603-01: Exiv2: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been found in Exiv2, the worst of which can lead to a crash via Denial of Service.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202603-01

---

#### 102. [Gentoo] GLSA 202601-05: Commons-BeanUtils: Arbitary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in Commons-BeanUtils, which can lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-05

---

#### 103. [Gentoo] GLSA 202601-04: Asterisk: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Asterisk, the worst of which can lead to arbitrary code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-04

---

#### 104. [Gentoo] GLSA 202601-03: GIMP: Arbitrary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in GIMP, which can lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-03

---

#### 105. [Gentoo] GLSA 202601-02: Vim, gVim: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Vim and gVim, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-02

---

#### 106. [Gentoo] GLSA 202601-01: inetutils: Remote Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in the telnetd module of inetutils, which allows remote code execution as root.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202601-01

---

#### 107. [Gentoo] GLSA 202512-01: GnuPG: Arbitrary Code Execution

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
A vulnerability has been discovered in GnuPG, which can lead to arbitrary code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202512-01

---

#### 108. [Gentoo] GLSA 202511-07: librnp: Weak random number generation

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
librnp uses weak random number generation such that generated keys can be easily cracked.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-07

---

#### 109. [Gentoo] GLSA 202511-06: libpng: Multiple vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in libpng, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-06

---

#### 110. [Gentoo] GLSA 202511-05: redict, redis: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in redis and redict, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-05

---

#### 111. [Gentoo] GLSA 202511-04: Chromium, Google Chrome, Microsoft Edge. Opera: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in Chromium and its derivatives, the worst of which can lead to remote code execution.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-04

---

#### 112. [Gentoo] GLSA 202511-03: qtsvg: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in qtsvg, the worst of which could lead to execution of arbitrary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-03

---

#### 113. [Gentoo] GLSA 202511-02: WebKitGTK+: Multiple Vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Multiple vulnerabilities have been discovered in WebKitGTK+, the worst of which can lead to execution of arbitary code.

**参考链接 / References**:
- https://security.gentoo.org/glsa/202511-02

---

#### 114. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 115. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 116. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 117. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 118. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 119. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 120. CVE-1999-0426

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The default permissions of /dev/kmem in Linux versions before 2.0.36 allows IP spoofing.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0426
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0426

---

#### 121. CVE-1999-0431

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Linux 2.2.3 and earlier allow a remote attacker to perform an IP fragmentation attack, causing a denial of service.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0431
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0431

---

#### 122. CVE-1999-0409

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in gnuplot in Linux version 3.5 allows local users to obtain root access.

**参考链接 / References**:
- http://www.securityfocus.com/bid/319
- http://www.securityfocus.com/bid/319

---

#### 123. CVE-1999-0421

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
During a reboot after an installation of Linux Slackware 3.6, a remote attacker can obtain root access by logging in to the root account without a password.

**参考链接 / References**:
- http://www.osvdb.org/981
- http://www.securityfocus.com/bid/338
- http://www.osvdb.org/981
- http://www.securityfocus.com/bid/338

---

#### 124. CVE-1999-0462

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
suidperl in Linux Perl does not check the nosuid mount option on file systems, allowing local users to gain root access by placing a setuid script in a mountable file system, e.g. a CD-ROM or floppy disk.

**参考链接 / References**:
- http://www.securityfocus.com/bid/339
- http://www.securityfocus.com/bid/339

---

#### 125. CVE-1999-0804

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Linux 2.2.x kernels via malformed ICMP packets containing unusual types, codes, and IP header lengths.

**参考链接 / References**:
- http://www.securityfocus.com/bid/302
- http://www.securityfocus.com/bid/302

---

#### 126. CVE-2000-0364

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

#### 127. CVE-2000-0365

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

#### 128. CVE-1999-1496

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

#### 129. CVE-2000-0118

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Red Hat Linux su program does not log failed password guesses if the su process is killed before it times out, which allows local attackers to conduct brute force password guessing.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94935300520617&w=2
- http://marc.info/?l=bugtraq&m=94935300520617&w=2

---

#### 130. CVE-1999-0733

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in VMWare 1.0.1 for Linux via a long HOME environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/490
- http://www.securityfocus.com/bid/490

---

#### 131. CVE-1999-1348

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linuxconf on Red Hat Linux 6.0 and earlier does not properly disable PAM-based access to the shutdown command, which could allow local users to cause a denial of service.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93220073515880&w=2
- http://marc.info/?l=bugtraq&m=93220073515880&w=2

---

#### 132. CVE-1999-1166

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux 2.0.37 does not properly encode the Custom segment limit, which allows local users to gain root privileges by accessing and modifying kernel memory.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/18156
- http://www.securityfocus.com/bid/523
- http://www.securityfocus.com/archive/1/18156
- http://www.securityfocus.com/bid/523

---

#### 133. CVE-1999-0710

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

#### 134. CVE-1999-1018

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
IPChains in Linux kernels 2.2.10 and earlier does not reassemble IP fragments before checking the header information, which allows a remote attacker to bypass the filtering rules using several fragments with 0 offsets.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93312523904591&w=2
- http://www.securityfocus.com/bid/543
- http://marc.info/?l=bugtraq&m=93312523904591&w=2
- http://www.securityfocus.com/bid/543

---

#### 135. CVE-1999-0746

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A default configuration of in.identd in SuSE Linux waits 120 seconds between requests, allowing a remote attacker to conduct a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/587
- http://www.securityfocus.com/bid/587

---

#### 136. CVE-1999-0740

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Remote attackers can cause a denial of service on Linux in.telnetd telnet daemon through a malformed TERM environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/594
- http://www.securityfocus.com/bid/594

---

#### 137. CVE-2000-0374

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

#### 138. CVE-1999-0720

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The pt_chown command in Linux allows local users to modify TTY terminal devices that belong to other users.

**参考链接 / References**:
- http://www.securityfocus.com/bid/597
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=lcamtuf.4.05.9907041223290.355-300000%40nimue.ids.pl
- http://www.securityfocus.com/bid/597
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=lcamtuf.4.05.9907041223290.355-300000%40nimue.ids.pl

---

#### 139. CVE-1999-0769

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vixie Cron on Linux systems allows local users to set parameters of sendmail commands via the MAILTO environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/611
- http://www.securityfocus.com/bid/611

---

#### 140. CVE-1999-0704

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Buffer overflow in Berkeley automounter daemon (amd) logging facility provided in the Linux am-utils package and others.

**参考链接 / References**:
- http://www.securityfocus.com/bid/614
- http://www.securityfocus.com/bid/614

---

#### 141. CVE-1999-1352

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
mknod in Linux 2.2 follows symbolic links, which could allow local users to overwrite files or gain privileges.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93855134409747&w=2
- http://marc.info/?l=bugtraq&m=93855134409747&w=2

---

#### 142. CVE-1999-1346

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
PAM configuration file for rlogin in Red Hat Linux 6.1 and earlier includes a less restrictive rule before a more restrictive one, which allows users to access the host via rlogin even if rlogin has been explicitly disabled using the /etc/nologin file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93942774609925&w=2
- http://marc.info/?l=bugtraq&m=93942774609925&w=2

---

#### 143. CVE-1999-1347

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Xsession in Red Hat Linux 6.1 and earlier can allow local users with restricted accounts to bypass execution of the .xsession file by starting kde, gnome or anotherlevel from kdm.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93942774609925&w=2
- http://marc.info/?l=bugtraq&m=93942774609925&w=2

---

#### 144. CVE-2000-0369

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The IDENT server in Caldera Linux 2.3 creates multiple threads for each IDENT request, which allows remote attackers to cause a denial of service.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-029.1.txt
- http://www.securityfocus.com/bid/1266
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-029.1.txt
- http://www.securityfocus.com/bid/1266

---

#### 145. CVE-2000-0356

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Pluggable Authentication Modules (PAM) in Red Hat Linux 6.1 does not properly lock access to disabled NIS accounts.

**参考链接 / References**:
- http://www.securityfocus.com/bid/697
- http://www.securityfocus.com/templates/advisory.html?id=1789
- http://www.securityfocus.com/bid/697
- http://www.securityfocus.com/templates/advisory.html?id=1789

---

#### 146. CVE-1999-1341

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Linux kernel before 2.3.18 or 2.2.13pre15, with SLIP and PPP options, allows local unprivileged users to forge IP packets via the TIOCSETD option on tty devices.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94061108411308&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7858
- http://marc.info/?l=bugtraq&m=94061108411308&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7858

---

#### 147. CVE-2000-0362

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflows in Linux cdwtools 093 and earlier allows local users to gain root privileges.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738

---

#### 148. CVE-2000-0363

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Linux cdwtools 093 and earlier allows local users to gain root privileges via the /tmp directory.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738
- http://www.novell.com/linux/security/advisories/suse_security_announce_25.html
- http://www.securityfocus.com/bid/738

---

#### 149. CVE-1999-0832

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

#### 150. CVE-1999-0831

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Linux syslogd via a large number of connections.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-035.0.txt
- http://www.securityfocus.com/bid/809
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-035.0.txt
- http://www.securityfocus.com/bid/809

---

#### 151. CVE-2000-0531

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

#### 152. CVE-1999-0317

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux su command gives root access to local users.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0317
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0317

---

#### 153. CVE-2000-0357

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ORBit and esound in Red Hat Linux 6.1 do not use sufficiently random numbers, which allows local users to guess the authentication keys.

**参考链接 / References**:
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html

---

#### 154. CVE-2000-0358

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ORBit and gnome-session in Red Hat Linux 6.1 allows remote attackers to crash a program.

**参考链接 / References**:
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html
- http://www.redhat.com/corp/support/errata/RHSA1999058-01.html

---

#### 155. CVE-1999-0986

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The ping command in Linux 2.0.3x allows local users to cause a denial of service by sending large packets with the -R (record route) option.

**参考链接 / References**:
- http://www.securityfocus.com/bid/870
- http://www.securityfocus.com/bid/870

---

#### 156. CVE-2000-0017

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Linux linuxconf package allows remote attackers to gain root privileges via a long parameter.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=94580196627059&w=2
- https://marc.info/?l=bugtraq&m=94580196627059&w=2

---

#### 157. CVE-1999-1327

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

#### 158. CVE-1999-1328

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

#### 159. CVE-1999-1329

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in SysVInit in Red Hat Linux 5.1 and earlier allows local users to gain privileges.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7250.php
- http://www.redhat.com/support/errata/rh50-errata-general.html#SysVinit
- http://www.iss.net/security_center/static/7250.php
- http://www.redhat.com/support/errata/rh50-errata-general.html#SysVinit

---

#### 160. CVE-1999-1331

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
netcfg 2.16-1 in Red Hat Linux 4.2 allows the Ethernet interface to be controlled by users on reboot when an option is set, which allows local users to cause a denial of service by shutting down the interface.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7245.php
- http://www.redhat.com/support/errata/rh42-errata-general.html#netcfg
- http://www.iss.net/security_center/static/7245.php
- http://www.redhat.com/support/errata/rh42-errata-general.html#netcfg

---

#### 161. CVE-1999-1332

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

#### 162. CVE-1999-1333

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

#### 163. CVE-1999-1335

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
snmpd server in cmu-snmp SNMP package before 3.3-1 in Red Hat Linux 4.0 is configured to allow remote attackers to read and write sensitive information.

**参考链接 / References**:
- http://www.redhat.com/support/errata/rh40-errata-general.html#cmu-snmp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7251
- http://www.redhat.com/support/errata/rh40-errata-general.html#cmu-snmp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7251

---

#### 164. CVE-1999-1339

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

#### 165. CVE-1999-0894

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Red Hat Linux screen program does not use Unix98 ptys, allowing local users to write to other terminals.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0894
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0894

---

#### 166. CVE-2000-1220

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

#### 167. CVE-2000-1221

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

#### 168. CVE-2000-0048

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
get_it program in Corel Linux Update allows local users to gain root access by specifying an alternate PATH for the cp program.

**参考链接 / References**:
- http://linux.corel.com/support/clos_patch1.htm
- http://www.securityfocus.com/bid/928
- http://linux.corel.com/support/clos_patch1.htm
- http://www.securityfocus.com/bid/928

---

#### 169. CVE-2000-0107

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux apcd program allows local attackers to modify arbitrary files via a symlink attack.

**参考链接 / References**:
- http://www.debian.org/security/2000/20000201
- http://www.securityfocus.com/bid/958
- http://www.debian.org/security/2000/20000201
- http://www.securityfocus.com/bid/958

---

#### 170. CVE-2005-0080

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The 55_options_traceback.dpatch patch for mailman 2.1.5 in Ubuntu 4.10 displays a different error message depending on whether the e-mail address is subscribed to a private list, which allows remote attackers to determine the list membership for a given e-mail address.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285839
- http://marc.info/?l=bugtraq&m=110549296126351&w=2
- http://qa.debian.org/bts-security.html
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285839
- http://marc.info/?l=bugtraq&m=110549296126351&w=2

---

#### 171. CVE-2006-0176

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in certain functions in src/fileio.c and src/unix/fileio.c in xmame before 11 January 2006 may allow local users to gain privileges via a long (1) -lang, (2) -ctrlr, (3) -pb, or (4) -rec argument on many operating systems, and via a long (5) -jdev argument on Ubuntu Linux.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0353.html
- http://www.securityfocus.com/archive/1/421849/100/0/threaded
- http://www.securityfocus.com/bid/16203
- http://x.mame.net/changes-unix.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24102

---

#### 172. CVE-2006-0458

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The DCC ACCEPT command handler in irssi before 0.8.9+0.8.10rc5-0ubuntu4.1 in Ubuntu Linux, and possibly other distributions, allows remote attackers to cause a denial of service (application crash) via certain crafted arguments in a DCC command.

**参考链接 / References**:
- http://secunia.com/advisories/19090
- http://www.securityfocus.com/bid/16913
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25147
- https://usn.ubuntu.com/259-1/
- http://secunia.com/advisories/19090

---

#### 173. CVE-2006-1183

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Ubuntu 5.10 installer does not properly clear passwords from the installer log file (questions.dat), and leaves the log file with world-readable permissions, which allows local users to gain privileges.

**参考链接 / References**:
- http://secunia.com/advisories/19200
- http://securitytracker.com/id?1015761
- http://www.osvdb.org/23868
- http://www.securityfocus.com/bid/17086
- http://www.vupen.com/english/advisories/2006/0927

---

#### 174. CVE-2006-3378

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
passwd command in shadow in Ubuntu 5.04 through 6.06 LTS, when called with the -f, -g, or -s flag, does not check the return code of a setuid call, which might allow local users to gain root privileges if setuid fails in cases such as PAM failures or resource limits.

**参考链接 / References**:
- http://secunia.com/advisories/20950
- http://secunia.com/advisories/20966
- http://secunia.com/advisories/21480
- http://www.debian.org/security/2006/dsa-1150
- http://www.osvdb.org/26995

---

#### 175. CVE-2006-3597

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
passwd before 1:4.0.13 on Ubuntu 6.06 LTS leaves the root password blank instead of locking it when the administrator selects the "Go Back" option after the final "Installation complete" message and uses the main menu, which causes the password to be zeroed out in the installer's memory.

**参考链接 / References**:
- http://secunia.com/advisories/21022
- http://www.osvdb.org/27091
- http://www.ubuntu.com/usn/usn-316-1
- http://secunia.com/advisories/21022
- http://www.osvdb.org/27091

---

#### 176. CVE-2006-5648

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Ubuntu Linux 6.10 for the PowerPC (PPC) allows local users to cause a denial of service (resource consumption) by using the (1) sys_get_robust_list and (2) sys_set_robust_list functions to create processes that cannot be killed.

**参考链接 / References**:
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/23474
- http://www.novell.com/linux/security/advisories/2006_79_kernel.html
- http://www.securityfocus.com/bid/21582

---

#### 177. CVE-2006-5649

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Unspecified vulnerability in the "alignment check exception handling" in Ubuntu 5.10, 6.06 LTS, and 6.10 for the PowerPC (PPC) allows local users to cause a denial of service (kernel panic) via unspecified vectors.

**参考链接 / References**:
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23370
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/23395
- http://secunia.com/advisories/23474

---

#### 178. CVE-2007-5159

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The ntfs-3g package before 1.913-2.fc7 in Fedora 7, and an ntfs-3g package in Ubuntu 7.10/Gutsy, assign incorrect permissions (setuid root) to mount.ntfs-3g, which allows local users with fuse group membership to read from and write to arbitrary block devices, possibly involving a file descriptor leak.

**参考链接 / References**:
- http://secunia.com/advisories/26938
- https://bugzilla.redhat.com/show_bug.cgi?id=298651
- https://www.redhat.com/archives/fedora-desktop-list/2007-September/msg00163.html
- https://www.redhat.com/archives/fedora-package-announce/2007-September/msg00368.html
- http://secunia.com/advisories/26938

---

#### 179. CVE-2007-3920

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
GNOME screensaver 2.20 in Ubuntu 7.10, when used with Compiz, does not properly reserve input focus, which allows attackers with physical access to take control of the session after entering an Alt-Tab sequence, a related issue to CVE-2007-3069.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-06/msg00002.html
- http://secunia.com/advisories/27381
- http://secunia.com/advisories/28627
- http://secunia.com/advisories/30329
- http://secunia.com/advisories/30715

---

#### 180. CVE-2006-7229

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
The skge driver 1.5 in Linux kernel 2.6.15 on Ubuntu does not properly use the spin_lock and spin_unlock functions, which allows remote attackers to cause a denial of service (machine crash) via a flood of network traffic.

**参考链接 / References**:
- http://secunia.com/advisories/28971
- http://www.securityfocus.com/bid/26511
- http://www.ubuntu.com/usn/usn-578-1
- https://bugs.launchpad.net/ubuntu/+source/linux-source-2.6.15/+bug/65631
- http://secunia.com/advisories/28971

---

#### 181. CVE-2007-6178

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Multiple PHP remote file inclusion vulnerabilities in Easy Hosting Control Panel for Ubuntu (EHCP) 0.22.8 and earlier allow remote attackers to execute arbitrary PHP code via a URL in the confdir parameter to (1) dbutil.bck.php and (2) dbutil.php in config/.

**参考链接 / References**:
- http://www.securityfocus.com/bid/26623
- https://exchange.xforce.ibmcloud.com/vulnerabilities/38698
- https://www.exploit-db.com/exploits/4671
- http://www.securityfocus.com/bid/26623
- https://exchange.xforce.ibmcloud.com/vulnerabilities/38698

---

#### 182. CVE-2008-0420

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
modules/libpr0n/decoders/bmp/nsBMPDecoder.cpp in Mozilla Firefox before 2.0.0.12, Thunderbird before 2.0.0.12, and SeaMonkey before 1.1.8 does not properly perform certain calculations related to the mColors table, which allows remote attackers to read portions of memory uninitialized via a crafted 8-bit bitmap (BMP) file that triggers an out-of-bounds read within the heap, as demonstrated using a CANVAS element; or cause a denial of service (application crash) via a crafted 8-bit bitmap file that triggers an out-of-bounds read. NOTE: the initial public reports stated that this affected Firefox in Ubuntu 6.06 through 7.10.

**参考链接 / References**:
- http://browser.netscape.com/releasenotes/
- http://secunia.com/advisories/28758
- http://secunia.com/advisories/28839
- http://secunia.com/advisories/29049
- http://secunia.com/advisories/29098

---

#### 183. CVE-2008-1072

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
The TFTP dissector in Wireshark (formerly Ethereal) 0.6.0 through 0.99.7, when running on Ubuntu 7.10, allows remote attackers to cause a denial of service (crash or memory consumption) via a malformed packet, possibly related to a Cairo library bug.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-03/msg00001.html
- http://secunia.com/advisories/29156
- http://secunia.com/advisories/29188
- http://secunia.com/advisories/29223
- http://secunia.com/advisories/29242

---

#### 184. CVE-2008-2285

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The ssh-vulnkey tool on Ubuntu Linux 7.04, 7.10, and 8.04 LTS does not recognize authorized_keys lines that contain options, which makes it easier for remote attackers to exploit CVE-2008-0166 by guessing a key that was not identified by this tool.

**参考链接 / References**:
- http://www.ubuntu.com/usn/usn-612-5
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42568
- http://www.ubuntu.com/usn/usn-612-5
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42568

---

#### 185. CVE-2008-5103

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The (1) python-vm-builder and (2) ubuntu-vm-builder implementations in VMBuilder 0.9 in Ubuntu 8.10 omit the -e option when invoking chpasswd with a root:! argument, which configures the root account with a cleartext password of ! (exclamation point) and allows attackers to bypass intended login restrictions.

**参考链接 / References**:
- http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff
- http://osvdb.org/49996
- http://secunia.com/advisories/32697
- http://www.securityfocus.com/bid/32292
- http://www.ubuntu.com/usn/usn-670-1

---

#### 186. CVE-2008-5104

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Ubuntu 6.06 LTS, 7.10, 8.04 LTS, and 8.10, when installed as a virtual machine by (1) python-vm-builder or (2) ubuntu-vm-builder in VMBuilder 0.9 in Ubuntu 8.10, have ! (exclamation point) as the default root password, which allows attackers to bypass intended login restrictions.

**参考链接 / References**:
- http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff
- http://secunia.com/advisories/32697
- http://www.securityfocus.com/bid/32292
- http://www.ubuntu.com/usn/usn-670-1
- https://bugs.launchpad.net/ubuntu/+source/vm-builder/+bug/296841

---

#### 187. CVE-2008-5393

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
UPR-Kernel in Ubuntu Privacy Remix (UPR) before 8.04_r1 includes kernel support for mounting RAID arrays, which might allow remote attackers to bypass intended isolation mechanisms by (1) reading from or (2) writing to these arrays.

**参考链接 / References**:
- http://securityreason.com/securityalert/4696
- http://www.securityfocus.com/archive/1/498905/100/0/threaded
- http://www.securityfocus.com/bid/32629
- https://bugs.launchpad.net/bugs/301285
- https://exchange.xforce.ibmcloud.com/vulnerabilities/47082

---

#### 188. CVE-2008-4539

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Heap-based buffer overflow in the Cirrus VGA implementation in (1) KVM before kvm-82 and (2) QEMU on Debian GNU/Linux and Ubuntu might allow local users to gain privileges by using the VNC console for a connection, aka the LGD-54XX "bitblt" heap overflow.  NOTE: this issue exists because of an incorrect fix for CVE-2007-1320.

**参考链接 / References**:
- http://git.kernel.dk/?p=qemu.git%3Ba=commitdiff%3Bh=65d35a09979e63541afc5bfc595b9f1b1b4ae069
- http://groups.google.com/group/linux.debian.changes.devel/msg/9e0dc008572f2867?dmode=source
- http://lists.opensuse.org/opensuse-security-announce/2009-04/msg00003.html
- http://secunia.com/advisories/25073
- http://secunia.com/advisories/29129

---

#### 189. CVE-2006-7236

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
The default configuration of xterm on Debian GNU/Linux sid and possibly Ubuntu enables the allowWindowOps resource, which allows user-assisted attackers to execute arbitrary code or have unspecified other impact via escape sequences.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=384593
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=510030
- http://secunia.com/advisories/33388
- https://usn.ubuntu.com/703-1/
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=384593

---

#### 190. CVE-2009-0122

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
hplip.postinst in HP Linux Imaging and Printing (HPLIP) 2.7.7 and 2.8.2 on Ubuntu allows local users to change the ownership of arbitrary files via unspecified manipulations in advance of an HPLIP installation or upgrade by an administrator, related to the product's attempt to correct the ownership of its configuration files within home directories.

**参考链接 / References**:
- http://secunia.com/advisories/33539
- http://www.securityfocus.com/bid/33249
- http://www.ubuntu.com/usn/usn-708-1
- https://launchpad.net/bugs/191299
- http://secunia.com/advisories/33539

---

#### 191. CVE-2009-1295

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
Apport before 0.108.4 on Ubuntu 8.04 LTS, before 0.119.2 on Ubuntu 8.10, and before 1.0-0ubuntu5.2 on Ubuntu 9.04 does not properly remove files from the application's crash-report directory, which allows local users to delete arbitrary files via unspecified vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-05/msg00000.html
- http://secunia.com/advisories/34947
- http://secunia.com/advisories/34952
- http://secunia.com/advisories/35065
- http://www.securityfocus.com/bid/34776

---

#### 192. CVE-2009-1573

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
xvfb-run 1.6.1 in Debian GNU/Linux, Ubuntu, Fedora 10, and possibly other operating systems place the magic cookie (MCOOKIE) on the command line, which allows local users to gain privileges by listing the process and its arguments.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=526678
- http://secunia.com/advisories/39834
- http://www.openwall.com/lists/oss-security/2009/05/05/2
- http://www.openwall.com/lists/oss-security/2009/05/05/4
- http://www.securityfocus.com/bid/34828

---

#### 193. CVE-2008-6792

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
system-tools-backends before 2.6.0-1ubuntu1.1 in Ubuntu 8.10, as used by "Users and Groups" in GNOME System Tools, hashes account passwords with 3DES and consequently limits effective password lengths to eight characters, which makes it easier for context-dependent attackers to successfully conduct brute-force password attacks.

**参考链接 / References**:
- http://osvdb.org/50037
- http://secunia.com/advisories/32566
- http://www.ubuntu.com/usn/usn-663-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50435
- https://launchpad.net/bugs/287134

---

#### 194. CVE-2009-1601

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The Ubuntu clamav-milter.init script in clamav-milter before 0.95.1+dfsg-1ubuntu1.2 in Ubuntu 9.04 sets the ownership of the current working directory to the clamav account, which might allow local users to bypass intended access restrictions via read or write operations involving this directory.

**参考链接 / References**:
- http://secunia.com/advisories/35000
- http://www.securityfocus.com/bid/34818
- http://www.ubuntu.com/usn/USN-770-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50311
- https://launchpad.net/bugs/365823

---

#### 195. CVE-2009-1296

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The eCryptfs support utilities (ecryptfs-utils) 73-0ubuntu6.1 on Ubuntu 9.04 stores the mount passphrase in installation logs, which might allow local users to obtain access to the filesystem by reading the log files from disk.  NOTE: the log files are only readable by root.

**参考链接 / References**:
- http://secunia.com/advisories/35383
- http://www.securitytracker.com/id?1022347
- http://www.ubuntu.com/usn/usn-783-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/51191
- http://secunia.com/advisories/35383

---

#### 196. CVE-2009-3232

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
pam-auth-update for PAM, as used in Ubuntu 8.10 and 9.4, and Debian GNU/Linux, does not properly handle an "empty selection" for system authentication modules in certain rare configurations, which causes any attempt to be successful and allows remote attackers to bypass authentication.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=519927
- http://secunia.com/advisories/36620
- http://www.openwall.com/lists/oss-security/2009/09/08/7
- http://www.securityfocus.com/bid/36306
- https://launchpad.net/bugs/410171

---

#### 197. CVE-2009-2939

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The postfix.postinst script in the Debian GNU/Linux and Ubuntu postfix 2.5.5 package grants the postfix user write access to /var/spool/postfix/pid, which might allow local users to conduct symlink attacks that overwrite arbitrary files.

**参考链接 / References**:
- http://www.debian.org/security/2011/dsa-2233
- http://www.openwall.com/lists/oss-security/2009/09/18/6
- http://www.debian.org/security/2011/dsa-2233
- http://www.openwall.com/lists/oss-security/2009/09/18/6

---

#### 198. CVE-2010-0832

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
pam_motd (aka the MOTD module) in libpam-modules before 1.1.0-2ubuntu1.1 in PAM on Ubuntu 9.10 and libpam-modules before 1.1.1-2ubuntu5 in PAM on Ubuntu 10.04 LTS allows local users to change the ownership of arbitrary files via a symlink attack on .cache in a user's home directory, related to "user file stamps" and the motd.legal-notice file.

**参考链接 / References**:
- http://secunia.com/advisories/40512
- http://twitter.com/jonoberheide/statuses/18009527979
- http://www.exploit-db.com/exploits/14273
- http://www.h-online.com/security/news/item/Ubuntu-closes-root-hole-1034618.html
- http://www.osvdb.org/66116

---

#### 199. CVE-2010-0834

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
The base-files package before 5.0.0ubuntu7.1 on Ubuntu 9.10 and before 5.0.0ubuntu20.10.04.2 on Ubuntu 10.04 LTS, as shipped on Dell Latitude 2110 netbooks, does not require authentication for package installation, which allows remote archive servers and man-in-the-middle attackers to execute arbitrary code via a crafted package.

**参考链接 / References**:
- http://secunia.com/advisories/40889
- http://www.securityfocus.com/bid/42280
- http://www.ubuntu.com/usn/usn-968-1
- http://www.vupen.com/english/advisories/2010/2015
- http://secunia.com/advisories/40889

---

#### 200. CVE-2011-0725

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Absolute path traversal vulnerability in the org.debian.apt.UpdateCachePartially method in worker.py in Aptdaemon 0.40 in Ubuntu 10.10 and 11.04 allows local users to read arbitrary files via a full pathname in the sources_list argument, related to the D-Bus interface.

**参考链接 / References**:
- http://www.securityfocus.com/bid/46490
- http://www.securitytracker.com/id?1025107
- http://www.ubuntu.com/usn/USN-1068-1
- http://www.vupen.com/english/advisories/2011/0459
- https://bugs.launchpad.net/bugs/722228

---

#### 201. CVE-2011-1400

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The default configuration of the shell_escape_commands directive in conf/texmf.d/95NonPath.cnf in the tex-common package before 2.08.1 in Debian GNU/Linux squeeze, Ubuntu 10.10 and 10.04 LTS, and possibly other operating systems lists certain programs, which might allow remote attackers to execute arbitrary code via a crafted TeX document.

**参考链接 / References**:
- http://secunia.com/advisories/43816
- http://secunia.com/advisories/43973
- http://svn.debian.org/wsvn/debian-tex/?op=comp&compare%5B%5D=%2Ftex-common%2Ftrunk%404781&compare%5B%5D=%2Ftex-common%2Ftrunk%404812
- http://svn.debian.org/wsvn/debian-tex/tex-common/trunk/?op=log
- http://www.debian.org/security/2011/dsa-2198

---

#### 202. CVE-2011-0730

**严重程度 / Severity**: N/A | CVSS: 6.5

**漏洞描述 / Description**:
Eucalyptus before 2.0.3 and Eucalyptus EE before 2.0.2, as used in Ubuntu Enterprise Cloud (UEC) and other products, do not properly interpret signed elements in SOAP requests, which allows man-in-the-middle attackers to execute arbitrary commands by modifying a request, related to an "XML Signature Element Wrapping" or a "SOAP signature replay" issue.

**参考链接 / References**:
- http://launchpadlibrarian.net/72472626/eucalyptus_2.0.1%2Bbzr1256-0ubuntu5_2.0.1%2Bbzr1256-0ubuntu6.diff.gz
- http://open.eucalyptus.com/wiki/esa-02
- http://secunia.com/advisories/44705
- http://www.securityfocus.com/bid/48000
- http://www.ubuntu.com/usn/USN-1137-1

---

#### 203. CVE-2011-3150

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Software Center in Ubuntu 11.10, 11.04 10.10 does not properly validate server certificates, which allows remote attackers to execute arbitrary code or obtain sensitive information via a man-in-the-middle (MITM) attack.

**参考链接 / References**:
- http://secunia.com/advisories/46950
- http://www.securityfocus.com/bid/50754
- http://www.ubuntu.com/usn/USN-1270-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/71430
- http://secunia.com/advisories/46950

---

#### 204. CVE-2011-4405

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The cupshelpers scripts in system-config-printer in Ubuntu 11.04 and 11.10, as used by the automatic printer driver download service, uses an "insecure connection" for queries to the OpenPrinting database, which allows remote attackers to execute arbitrary code via a man-in-the-middle (MITM) attack that modifies packages or repositories.

**参考链接 / References**:
- http://osvdb.org/77214
- http://secunia.com/advisories/46909
- http://www.securityfocus.com/bid/50721
- http://www.ubuntu.com/usn/USN-1265-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/71394

---

#### 205. CVE-2012-0949

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Apport hook in Update Manager as used by Ubuntu 12.04 LTS, 11.10, and 11.04 uploads certain system state archive files when reporting bugs to Launchpad, which allows remote attackers to read repository credentials by viewing a public bug report.

**参考链接 / References**:
- http://osvdb.org/82020
- http://secunia.com/advisories/49230
- http://www.securityfocus.com/bid/53605
- http://www.ubuntu.com/usn/USN-1443-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/75728

---

#### 206. CVE-2012-0944

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Aptdaemon 0.43 and earlier in Ubuntu 11.04, 11.10, and 12.04 LTS does not authenticate packages when the transaction is not simulated, which allows remote attackers to install arbitrary packages via a man-in-the-middle attack.

**参考链接 / References**:
- http://secunia.com/advisories/48688
- http://ubuntu.com/usn/usn-1414-1
- http://www.osvdb.org/80887
- http://www.securityfocus.com/bid/52855
- https://bugs.launchpad.net/ubuntu/%2Bsource/aptdaemon/%2Bbug/959131

---

#### 207. CVE-2012-0948

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
DistUpgrade/DistUpgradeMain.py in Update Manager, as used by Ubuntu 12.04 LTS, 11.10, and 11.04, uses weak permissions for (1) apt-clone_system_state.tar.gz and (2) system_state.tar.gz, which allows local users to obtain repository credentials.

**参考链接 / References**:
- http://launchpadlibrarian.net/105380733/update-manager_1%3A0.156.14.3_1%3A0.156.14.4.diff.gz
- http://osvdb.org/82019
- http://secunia.com/advisories/49230
- http://www.securityfocus.com/bid/53604
- http://www.ubuntu.com/usn/USN-1443-1

---

#### 208. CVE-2011-4408

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The Single Sign On Client (ubuntu-sso-client) for Ubuntu 11.04 and 11.10 does not properly validate SSL certificates when using HTTPS, which allows remote attackers to spoof a server and modify or read sensitive data via a man-in-the-middle (MITM) attack.

**参考链接 / References**:
- http://osvdb.org/82747
- http://secunia.com/advisories/49448
- http://www.securityfocus.com/bid/53829
- http://www.ubuntu.com/usn/USN-1464-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/76112

---

#### 209. CVE-2011-4409

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Ubuntu One Client for Ubuntu 10.04 LTS, 11.04, 11.10, and 12.04 LTS does not properly validate SSL certificates, which allows remote attackers to spoof a server and modify or read sensitive information via a man-in-the-middle (MITM) attack.

**参考链接 / References**:
- http://secunia.com/advisories/49442
- http://ubuntu.com/usn/usn-1465-1
- http://ubuntu.com/usn/usn-1465-2
- http://ubuntu.com/usn/usn-1465-3
- http://www.osvdb.org/82748

---

#### 210. CVE-2012-0950

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Apport hook (DistUpgradeApport.py) in Update Manager, as used by Ubuntu 12.04 LTS, 11.10, and 11.04, uploads the /var/log/dist-upgrade directory when reporting bugs to Launchpad, which allows remote attackers to read repository credentials by viewing a public bug report.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2012-0949.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1443-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/1004503
- http://www.ubuntu.com/usn/USN-1443-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/1004503

---

#### 211. CVE-2012-2317

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The Debian php_crypt_revamped.patch patch for PHP 5.3.x, as used in the php5 package before 5.3.3-7+squeeze4 in Debian GNU/Linux squeeze, the php5 package before 5.3.2-1ubuntu4.17 in Ubuntu 10.04 LTS, and the php5 package before 5.3.5-1ubuntu7.10 in Ubuntu 11.04, does not properly handle an empty salt string, which might allow remote attackers to bypass authentication by leveraging an application that relies on the PHP crypt function to choose a salt for password hashing.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=581170
- http://www.openwall.com/lists/oss-security/2012/05/04/7
- http://www.openwall.com/lists/oss-security/2012/05/05/2
- http://www.ubuntu.com/usn/USN-1481-1
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=581170

---

#### 212. CVE-2012-5356

**严重程度 / Severity**: N/A | CVSS: 5.8

**漏洞描述 / Description**:
The apt-add-repository tool in Ubuntu Software Properties 0.75.x before 0.75.10.3, 0.80.x before 0.80.9.2, 0.81.x before 0.81.13.5, 0.82.x before 0.82.7.3, and 0.92.x before 0.92.8 does not properly check PPA GPG keys imported from a keyserver, which allows remote attackers to install arbitrary package repository GPG keys via a man-in-the-middle (MITM) attack.

**参考链接 / References**:
- http://www.securityfocus.com/bid/55736
- http://www.ubuntu.com/usn/USN-1588-1
- https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1016643
- https://exchange.xforce.ibmcloud.com/vulnerabilities/78990
- http://www.securityfocus.com/bid/55736

---

#### 213. CVE-2012-0961

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Apt 0.8.16~exp5ubuntu13.x before 0.8.16~exp5ubuntu13.6, 0.8.16~exp12ubuntu10.x before 0.8.16~exp12ubuntu10.7, and 0.9.7.5ubuntu5.x before 0.9.7.5ubuntu5.2, as used in Ubuntu, uses world-readable permissions for /var/log/apt/term.log, which allows local users to obtain sensitive shell information by reading the log file.

**参考链接 / References**:
- http://osvdb.org/88380
- http://secunia.com/advisories/51568
- http://www.securityfocus.com/bid/56917
- http://www.ubuntu.com/usn/USN-1662-1
- http://osvdb.org/88380

---

#### 214. CVE-2012-0962

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Aptdaemon 0.43 in Ubuntu 11.10 and 12.04 LTS uses short IDs when importing PPA GPG keys from a keyserver, which allows remote attackers to install arbitrary package repository GPG keys via a man-in-the-middle (MITM) attack.

**参考链接 / References**:
- http://secunia.com/advisories/51627
- http://www.securityfocus.com/bid/56959
- http://www.securitytracker.com/id?1027891
- http://www.ubuntu.com/usn/USN-1666-1
- https://bugs.launchpad.net/software-center-agent/%2Bbug/1052789

---

#### 215. CVE-2013-1052

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
pam-xdg-support, as used in Ubuntu 12.10, does not properly handle the PATH environment variable, which allows local users to gain privileges via unspecified vectors related to sudo.

**参考链接 / References**:
- http://www.securityfocus.com/bid/58550
- http://www.ubuntu.com/usn/USN-1766-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/82918
- http://www.securityfocus.com/bid/58550
- http://www.ubuntu.com/usn/USN-1766-1

---

#### 216. CVE-2013-2162

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
Race condition in the post-installation script (mysql-server-5.5.postinst) for MySQL Server 5.5 for Debian GNU/Linux and Ubuntu Linux creates a configuration file with world-readable permissions before restricting the permissions, which allows local users to read the file and obtain sensitive information such as credentials.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=711600
- http://seclists.org/oss-sec/2013/q2/528
- http://secunia.com/advisories/54300
- http://ubuntu.com/usn/usn-1909-1
- http://www.debian.org/security/2013/dsa-2818

---

#### 217. CVE-2013-1060

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
A certain Ubuntu build procedure for perf, as distributed in the Linux kernel packages in Ubuntu 10.04 LTS, 12.04 LTS, 12.10, 13.04, and 13.10, sets the HOME environment variable to the ~buildd directory and consequently reads the system configuration file from the ~buildd directory, which allows local users to gain privileges by leveraging control over the buildd account.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2013/CVE-2013-1060.html
- http://www.ubuntu.com/usn/USN-1938-1
- http://www.ubuntu.com/usn/USN-1939-1
- http://www.ubuntu.com/usn/USN-1941-1
- http://www.ubuntu.com/usn/USN-1942-1

---

#### 218. CVE-2013-1062

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
ubuntu-system-service 0.2.4 before 0.2.4.1. 0.2.3 before 0.2.3.1, and 0.2.2 before 0.2.2.1 does not properly use D-Bus for communication with a polkit authority, which allows local users to bypass intended access restrictions by leveraging a PolkitUnixProcess PolkitSubject race condition via a (1) setuid process or (2) pkexec process, a related issue to CVE-2013-4288.

**参考链接 / References**:
- http://secunia.com/advisories/54907
- http://www.ubuntu.com/usn/USN-1962-1
- http://secunia.com/advisories/54907
- http://www.ubuntu.com/usn/USN-1962-1

---

#### 219. CVE-2011-4613

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The X.Org X wrapper (xserver-wrapper.c) in Debian GNU/Linux and Ubuntu Linux does not properly verify the TTY of a user who is starting X, which allows local users to bypass intended access restrictions by associating stdin with a file that is misinterpreted as the console TTY.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=652249
- http://www.debian.org/security/2011/dsa-2364
- http://www.ubuntu.com/usn/USN-1349-1
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=652249
- http://www.debian.org/security/2011/dsa-2364

---

#### 220. [Ubuntu] USN-8225-1: Python marshmallow vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Jared Deckard discovered that Python marshmallow did not correctly handle hiding certain fields. An attacker could possibly use this issue to leak sensitive information. This issue only affected Ubuntu 18.04 LTS. (CVE-2018-17175) It was discovered that Python marshmallow did not efficiently handle merging certain objects. An attacker could possibly use this issue to cause a denial of service. This

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8225-1

---

#### 221. CVE-2000-0218

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux mount and umount allows local users to gain root privileges via a long relative pathname.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-002.0.txt
- http://www.osvdb.org/6980
- http://www.osvdb.org/7004
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-002.0.txt
- http://www.osvdb.org/6980

---

#### 222. CVE-2000-0194

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
buildxconf in Corel Linux allows local users to modify or create arbitrary files via the -x or -f parameters.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html
- http://www.securityfocus.com/bid/1007
- http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html
- http://www.securityfocus.com/bid/1007

---

#### 223. CVE-2000-0195

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
setxconf in Corel Linux allows local users to gain root access via the -T parameter, which executes the user's .xserverrc file.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html
- http://www.securityfocus.com/bid/1008
- http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html
- http://www.securityfocus.com/bid/1008

---

#### 224. CVE-2000-0170

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the man program in Linux allows local users to gain privileges via the MANPAGER environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1011
- http://www.securityfocus.com/bid/1011

---

#### 225. CVE-2000-0186

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the dump utility in the Linux ext2fs backup package allows local users to gain privileges via a long command line argument.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-100.html
- http://www.securityfocus.com/bid/1020
- http://www.redhat.com/support/errata/RHSA-2000-100.html
- http://www.securityfocus.com/bid/1020

---

#### 226. CVE-2000-0196

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in mhshow in the Linux nmh package allows remote attackers to execute commands via malformed MIME headers in an email message.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-006.html
- http://www.securityfocus.com/bid/1018
- http://www.redhat.com/support/errata/RHSA-2000-006.html
- http://www.securityfocus.com/bid/1018

---

#### 227. CVE-2000-0193

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configuration of Dosemu in Corel Linux 1.0 allows local users to execute the system.com program and gain privileges.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1030
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200003020436.PAA20168%40jawa.chilli.net.au
- http://www.securityfocus.com/bid/1030
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200003020436.PAA20168%40jawa.chilli.net.au

---

#### 228. CVE-2000-0206

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
The installation of Oracle 8.1.5.x on Linux follows symlinks and creates the orainstRoot.sh file with world-writeable permissions, which allows local users to gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0023.html
- http://www.securityfocus.com/bid/1035
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0023.html
- http://www.securityfocus.com/bid/1035

---

#### 229. CVE-2000-0184

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux printtool sets the permissions of printer configuration files to be world-readable, which allows local attackers to obtain printer share passwords.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0082.html
- http://www.securityfocus.com/bid/1037
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0082.html
- http://www.securityfocus.com/bid/1037

---

#### 230. CVE-2000-0171

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
atsadc in the atsar package for Linux does not properly check the permissions of an output file, which allows local users to gain root privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0102.html
- http://www.securityfocus.com/bid/1048
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0102.html
- http://www.securityfocus.com/bid/1048

---

#### 231. CVE-2000-0233

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
SuSE Linux IMAP server allows remote attackers to bypass IMAP authentication and gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vendor/2000-q1/0035.html
- http://archives.neohapsis.com/archives/vendor/2000-q1/0035.html

---

#### 232. CVE-2000-0231

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Linux kreatecd trusts a user-supplied path that is used to find the cdrecord program, allowing local users to gain root privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0162.html
- http://www.securityfocus.com/bid/1061
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0162.html
- http://www.securityfocus.com/bid/1061

---

#### 233. CVE-2000-0227

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Linux 2.2.x kernel does not restrict the number of Unix domain sockets as defined by the wmem_max parameter, which allows local users to cause a denial of service by requesting a large number of sockets.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0254.html
- http://marc.info/?l=bugtraq&m=95421263519558&w=2
- http://www.securityfocus.com/bid/1072
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4186
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0254.html

---

#### 234. CVE-2000-0289

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
IP masquerading in Linux 2.2.x allows remote attackers to route UDP packets through the internal interface by modifying the external source IP address and port number to match those of an established connection.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0284.html
- http://www.novell.com/linux/security/advisories/suse_security_announce_48.html
- http://www.securityfocus.com/bid/1078
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0284.html
- http://www.novell.com/linux/security/advisories/suse_security_announce_48.html

---

#### 235. CVE-2000-0274

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Linux trustees kernel patch allows attackers to cause a denial of service by accessing a file or directory with a long name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0035.html
- http://www.braysystems.com/linux/trustees.html
- http://www.securityfocus.com/bid/1096
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0035.html
- http://www.braysystems.com/linux/trustees.html

---

#### 236. CVE-2000-0263

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The X font server xfs in Red Hat Linux 6.x allows an attacker to cause a denial of service via a malformed request.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0079.html
- http://www.securityfocus.com/bid/1111
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0079.html
- http://www.securityfocus.com/bid/1111

---

#### 237. CVE-2000-0336

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux OpenLDAP server allows local users to modify arbitrary files via a symlink attack.

**参考链接 / References**:
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-2000-009.0.txt
- http://www.redhat.com/support/errata/RHSA-2000-012.html
- http://www.securityfocus.com/bid/1232
- http://www.turbolinux.com/pipermail/tl-security-announce/2000-May/000009.html
- ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-2000-009.0.txt

---

#### 238. CVE-2000-0248

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The web GUI for the Linux Virtual Server (LVS) software in the Red Hat Linux Piranha package has a backdoor password that allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://xforce.iss.net/alerts/advise46.php3
- http://xforce.iss.net/alerts/advise46.php3

---

#### 239. CVE-1999-0706

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Linux xmonisdn package allows local users to gain root privileges by modifying the IFS or PATH environmental variables.

**参考链接 / References**:
- http://www.securityfocus.com/bid/583
- http://www.securityfocus.com/bid/583

---

#### 240. CVE-2000-0340

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Gnomelib in SuSE Linux 6.3 allows local users to execute arbitrary commands via the DISPLAY environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1155
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=00042902575201.09597%40wintermute-pub
- http://www.suse.com/us/support/download/updates/axp_63.html
- http://www.securityfocus.com/bid/1155
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=00042902575201.09597%40wintermute-pub

---

#### 241. CVE-2000-0344

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The knfsd NFS server in Linux kernel 2.2.x allows remote attackers to cause a denial of service via a negative size value.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1160
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0005012042550.6419-100000%40ferret.lmh.ox.ac.uk
- http://www.securityfocus.com/bid/1160
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0005012042550.6419-100000%40ferret.lmh.ox.ac.uk

---

#### 242. CVE-2000-0293

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
aaa_base in SuSE Linux 6.3, and cron.daily in earlier versions, allow local users to delete arbitrary files by creating files whose names include spaces, which are then incorrectly interpreted by aaa_base when it deletes expired files from the /tmp directory.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1130
- http://www.securityfocus.com/bid/1130

---

#### 243. CVE-2000-0378

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The pam_console PAM module in Linux systems performs a chown on various devices upon a user login, but an open file descriptor for those devices can be maintained after the user logs out, which allows that user to sniff activity on these devices when subsequent users log in.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0023.html
- http://www.securityfocus.com/bid/1176
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0023.html
- http://www.securityfocus.com/bid/1176

---

#### 244. CVE-2000-0438

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in fdmount on Linux systems allows local users in the "floppy" group to execute arbitrary commands via a long mountpoint parameter.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0245.html
- http://www.securityfocus.com/bid/1239
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0245.html
- http://www.securityfocus.com/bid/1239

---

#### 245. CVE-2000-0460

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in KDE kdesud on Linux allows local uses to gain privileges via a long DISPLAY environmental variable.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0353.html
- http://www.securityfocus.com/bid/1274
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0353.html
- http://www.securityfocus.com/bid/1274

---

#### 246. CVE-2000-0454

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux cdrecord allows local users to gain privileges via the dev parameter.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0367.html
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0434.html
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0019.html
- http://www.securityfocus.com/bid/1265
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0367.html

---

#### 247. CVE-2000-0467

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linux splitvt 1.6.3 and earlier allows local users to gain root privileges via a long password in the screen locking function.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0125.html
- http://www.securityfocus.com/bid/1346
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0125.html
- http://www.securityfocus.com/bid/1346

---

#### 248. CVE-2000-0506

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The "capabilities" feature in Linux before 2.2.16 allows local users to cause a denial of service or gain privileges by setting the capabilities to prevent a setuid program from dropping privileges, aka the "Linux kernel setuid/setcap vulnerability."

**参考链接 / References**:
- ftp://sgigate.sgi.com/security/20000802-01-P
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0062.html
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0063.html
- http://www.redhat.com/support/errata/RHSA-2000-037.html
- http://www.securityfocus.com/bid/1322

---

#### 249. CVE-2000-0602

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Secure Locate (slocate) in Red Hat Linux allows local users to gain privileges via a malformed configuration file that is specified in the LOCATE_PATH environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1385
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006211209500.22969-100000%40nimue.tpi.pl
- http://www.securityfocus.com/bid/1385
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006211209500.22969-100000%40nimue.tpi.pl

---

#### 250. CVE-2000-0604

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
gkermit in Red Hat Linux is improperly installed with setgid uucp, which allows local users to modify files owned by uucp.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1383
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006211209500.22969-100000%40nimue.tpi.pl
- http://www.securityfocus.com/bid/1383
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006211209500.22969-100000%40nimue.tpi.pl

---

#### 251. CVE-2000-0606

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in kon program in Kanji on Console (KON) package on Linux may allow local users to gain root privileges via a long -StartupMessage parameter.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1371
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006192340340.19998-100000%40ferret.lmh.ox.ac.uk
- http://www.securityfocus.com/bid/1371
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006192340340.19998-100000%40ferret.lmh.ox.ac.uk

---

#### 252. CVE-2000-0607

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in fld program in Kanji on Console (KON) package on Linux may allow local users to gain root privileges via an input file containing long CHARSET_REGISTRY or CHARSET_ENCODING settings.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1371
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006192340340.19998-100000%40ferret.lmh.ox.ac.uk
- http://www.securityfocus.com/bid/1371
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.4.21.0006192340340.19998-100000%40ferret.lmh.ox.ac.uk

---

#### 253. CVE-2000-0617

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in xconq and cconq game programs on Red Hat Linux allows local users to gain additional privileges via long USER environmental variable.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html

---

#### 254. CVE-2000-0618

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in xconq and cconq game programs on Red Hat Linux allows local users to gain additional privileges via long DISPLAY environmental variable.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html

---

#### 255. CVE-2000-0566

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
makewhatis in Linux man package allows local users to overwrite files via a symlink attack.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-021.0.txt
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0390.html
- http://frontal2.mandriva.com/security/advisories?name=MDKSA-2000:015
- http://www.redhat.com/support/errata/RHSA-2000-041.html
- http://www.securityfocus.com/bid/1434

---

#### 256. CVE-2000-0614

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Tnef program in Linux systems allows remote attackers to overwrite arbitrary files via TNEF encoded compressed attachments which specify absolute path names for the decompressed output.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vendor/2000-q3/0002.html
- http://www.securityfocus.com/bid/1450
- http://archives.neohapsis.com/archives/vendor/2000-q3/0002.html
- http://www.securityfocus.com/bid/1450

---

#### 257. CVE-2000-0666

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
rpc.statd in the nfs-utils package in various Linux distributions does not properly cleanse untrusted format strings, which allows remote attackers to gain root privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0206.html
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0230.html
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0236.html
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0260.html
- http://www.calderasystems.com/support/security/advisories/CSSA-2000-025.0.txt

---

#### 258. CVE-2000-0633

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in Mandrake Linux usermode package allows local users to to reboot or halt the system.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0251.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0117.html
- http://www.redhat.com/support/errata/RHSA-2000-053.html
- http://www.securityfocus.com/bid/1489
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4944

---

#### 259. CVE-2000-0667

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Vulnerability in gpm in Caldera Linux allows local users to delete arbitrary files or conduct a denial of service.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0273.html
- http://www.securityfocus.com/bid/1512
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0273.html
- http://www.securityfocus.com/bid/1512

---

#### 260. CVE-2000-0668

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
pam_console PAM module in Linux systems allows a user to access the system console and reboot the system when a display manager such as gdm or kdm has XDMCP enabled.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0398.html
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0455.html
- http://www.redhat.com/support/errata/RHSA-2000-044.html
- http://www.securityfocus.com/bid/1513
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5001

---

#### 261. CVE-2000-0545

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in mailx mail command (aka Mail) on Linux systems allows local users to gain privileges via a long -c (carbon copy) parameter.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0435.html
- http://www.debian.org/security/2000/20000605
- http://www.securityfocus.com/bid/1305
- http://archives.neohapsis.com/archives/bugtraq/2000-05/0435.html
- http://www.debian.org/security/2000/20000605

---

#### 262. CVE-2000-0354

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
mirror 2.8.x in Linux systems allows remote attackers to create files one level above the local target directory.

**参考链接 / References**:
- http://www.debian.org/security/1999/19991018
- http://www.novell.com/linux/security/advisories/suse_security_announce_22.html
- http://www.securityfocus.com/bid/681
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=15769.990928%40tomcat.ru
- http://www.debian.org/security/1999/19991018

---

#### 263. CVE-2000-0816

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux tmpwatch --fuser option allows local users to execute arbitrary commands by creating files whose names contain shell metacharacters.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/MDKSA-2000-056.php3?dis=7.1
- http://www.redhat.com/support/errata/RHSA-2000-080.html
- http://www.securityfocus.com/bid/1785
- http://xforce.iss.net/alerts/advise64.php
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5320

---

#### 264. CVE-2000-1213

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ping in iputils before 20001010, as distributed on Red Hat Linux 6.2 through 7J and other operating systems, does not drop privileges after acquiring a raw socket, which increases ping's exposure to bugs that otherwise would occur at lower privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0429.html
- http://marc.info/?l=bugtraq&m=97249980727834&w=2
- http://www.redhat.com/support/errata/RHSA-2000-087.html
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0429.html
- http://marc.info/?l=bugtraq&m=97249980727834&w=2

---

#### 265. CVE-2000-1214

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflows in the (1) outpack or (2) buf variables of ping in iputils before 20001010, as distributed on Red Hat Linux 6.2 through 7J and other operating systems, may allow local users to gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0429.html
- http://marc.info/?l=bugtraq&m=97208562830613&w=2
- http://marc.info/?l=bugtraq&m=97249980727834&w=2
- http://www.iss.net/security_center/static/5431.php
- http://www.redhat.com/support/errata/RHSA-2000-087.html

---

#### 266. CVE-2000-0031

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
The initscripts package in Red Hat Linux allows local users to gain privileges via a symlink attack.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0031

---

#### 267. CVE-2000-0698

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Minicom 1.82.1 and earlier on some Linux systems allows local users to create arbitrary files owned by the uucp user via a symlink attack.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/77361
- http://www.securityfocus.com/bid/1599
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5151
- http://www.securityfocus.com/archive/1/77361
- http://www.securityfocus.com/bid/1599

---

#### 268. CVE-2000-0714

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
umb-scheme 3.2-11 for Red Hat Linux is installed with world-writeable files.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-047.html
- http://www.securityfocus.com/bid/1551
- http://www.redhat.com/support/errata/RHSA-2000-047.html
- http://www.securityfocus.com/bid/1551

---

#### 269. CVE-2000-0715

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
DiskCheck script diskcheck.pl in Red Hat Linux 6.2 allows local users to create or overwrite arbitrary files via a symlink attack on a temporary file.

**参考链接 / References**:
- http://seclists.org/bugtraq/2000/Aug/0082.html
- http://seclists.org/bugtraq/2000/Aug/0096.html
- http://seclists.org/bugtraq/2000/Jun/0298.html
- http://www.securityfocus.com/bid/1552
- http://seclists.org/bugtraq/2000/Aug/0082.html

---

#### 270. CVE-2000-0747

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The logrotate script for OpenLDAP before 1.2.11 in Conectiva Linux sends an improper signal to the kernel log daemon (klogd) and kills it.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0379.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5036
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0379.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5036

---

#### 271. CVE-2000-0749

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the Linux binary compatibility module in FreeBSD 3.x through 5.x allows local users to gain root privileges via long filenames in the linux shadow file system.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/freebsd/2000-08/0338.html
- http://www.osvdb.org/1536
- http://www.securityfocus.com/bid/1628
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5968
- http://archives.neohapsis.com/archives/freebsd/2000-08/0338.html

---

#### 272. CVE-2000-0800

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
String parsing error in rpc.kstatd in the linuxnfs or knfsd packages in SuSE and possibly other Linux systems allows remote attackers to gain root privileges.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_58.html
- http://www.novell.com/linux/security/advisories/suse_security_announce_58.html

---

#### 273. CVE-2000-0829

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The tmpwatch utility in Red Hat Linux forks a new process for each directory level, which allows local users to cause a denial of service by creating deeply nested directories in /tmp or /var/tmp/.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-080.html
- http://www.securityfocus.com/archive/1/81364
- http://www.securityfocus.com/bid/1664
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5217
- http://www.redhat.com/support/errata/RHSA-2000-080.html

---

#### 274. CVE-2000-0866

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Interbase 6 SuperServer for Linux allows an attacker to cause a denial of service via a query containing 0 bytes.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0027.html
- http://www.securityfocus.com/bid/1654
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5205
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0027.html
- http://www.securityfocus.com/bid/1654

---

#### 275. CVE-2000-0867

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Kernel logging daemon (klogd) in Linux does not properly cleanse user-injected format strings, which allows local users to gain root privileges by triggering malformed kernel messages.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-032.0.txt
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0193.html
- http://frontal2.mandriva.com/security/advisories?name=MDKSA-2000:050
- http://marc.info/?l=bugtraq&m=97726239017741&w=2
- http://www.novell.com/linux/security/advisories/adv9_draht_syslogd_txt.html

---

#### 276. CVE-2000-0868

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Apache 1.3.12 in SuSE Linux 6.4 allows remote attackers to read source code for CGI scripts by replacing the /cgi-bin/ in the requested URL with /cgi-bin-sdb/.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html
- http://www.atstake.com/research/advisories/2000/a090700-2.txt
- http://www.securityfocus.com/bid/1658
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5197
- http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html

---

#### 277. CVE-2000-0869

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Apache 1.3.12 in SuSE Linux 6.4 enables WebDAV, which allows remote attackers to list arbitrary directories via the PROPFIND HTTP request method.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html
- http://www.atstake.com/research/advisories/2000/a090700-3.txt
- http://www.securityfocus.com/bid/1656
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5204
- http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html

---

#### 278. CVE-2000-0883

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of mod_perl for Apache as installed on Mandrake Linux 6.1 through 7.1 sets the /perl/ directory to be browseable, which allows remote attackers to list the contents of that directory.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0111.html
- http://www.securityfocus.com/bid/1678
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5257
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0111.html
- http://www.securityfocus.com/bid/1678

---

#### 279. CVE-2000-1009

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
dump in Red Hat Linux 6.2 trusts the pathname specified by the RSH environmental variable, which allows local users to obtain root privileges by modifying the RSH variable to point to a Trojan horse program.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0438.html
- http://www.securityfocus.com/bid/1871
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5437
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0438.html
- http://www.securityfocus.com/bid/1871

---

#### 280. CVE-2000-1042

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in ypserv in Mandrake Linux 7.1 and earlier, and possibly other Linux operating systems, allows an attacker to gain root privileges when ypserv is built without a vsyslog() function.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5730
- http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5730

---

#### 281. CVE-2000-1043

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Format string vulnerability in ypserv in Mandrake Linux 7.1 and earlier, and possibly other Linux operating systems, allows an attacker to gain root privileges when ypserv is built without a vsyslog() function.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5731
- http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5731

---

#### 282. CVE-2000-1044

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Format string vulnerability in ypbind-mt in SuSE SuSE-6.2, and possibly other Linux operating systems, allows an attacker to gain root privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/linux/suse/2000-q4/0262.html
- http://www.securityfocus.com/bid/1820
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5394
- http://archives.neohapsis.com/archives/linux/suse/2000-q4/0262.html
- http://www.securityfocus.com/bid/1820

---

#### 283. CVE-2000-1059

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configuration of the Xsession file in Mandrake Linux 7.1 and 7.0 bypasses the Xauthority access control mechanism with an "xhost + localhost" command, which allows local users to sniff X Windows events and gain privileges.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/MDKSA-2000-052.php3
- http://www.securityfocus.com/archive/1/136495
- http://www.securityfocus.com/bid/1735
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5305
- http://www.linux-mandrake.com/en/security/MDKSA-2000-052.php3

---

#### 284. CVE-2000-0934

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Glint in Red Hat Linux 5.2 allows local users to overwrite arbitrary files and cause a denial of service via a symlink attack.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-062.html
- http://www.securityfocus.com/bid/1703
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5271
- http://www.redhat.com/support/errata/RHSA-2000-062.html
- http://www.securityfocus.com/bid/1703

---

#### 285. CVE-2000-0956

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
cyrus-sasl before 1.5.24 in Red Hat Linux 7.0 does not properly verify the authorization for a local user, which could allow the users to bypass specified access restrictions.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-094.html
- http://www.securityfocus.com/bid/1875
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5427
- http://www.redhat.com/support/errata/RHSA-2000-094.html
- http://www.securityfocus.com/bid/1875

---

#### 286. CVE-2000-1095

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
modprobe in the modutils 2.3.x package on Linux systems allows a local user to execute arbitrary commands via shell metacharacters.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0179.html
- http://archives.neohapsis.com/archives/linux/suse/2000-q4/0596.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000340
- http://www.debian.org/security/2000/20001120
- http://www.linux-mandrake.com/en/security/MDKSA-2000-071-1.php3?dis=7.1

---

#### 287. CVE-2000-1107

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
in.identd ident server in SuSE Linux 6.x and 7.0 allows remote attackers to cause a denial of service via a long request, which causes the server to access a NULL pointer and crash.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0387.html
- http://www.securityfocus.com/bid/2015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5590
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0387.html
- http://www.securityfocus.com/bid/2015

---

#### 288. CVE-2000-1125

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
restore 0.4b15 and earlier in Red Hat Linux 6.2 trusts the pathname specified by the RSH environmental variable, which allows local users to obtain root privileges by modifying the RSH variable to point to a Trojan horse program.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97336034309944&w=2
- http://www.securityfocus.com/bid/1914
- http://marc.info/?l=bugtraq&m=97336034309944&w=2
- http://www.securityfocus.com/bid/1914

---

#### 289. CVE-2000-1136

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
elvis-tiny before 1.4-10 in Debian GNU/Linux, and possibly other Linux operating systems, allows local users to overwrite files of other users via a symlink attack.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97502995616099&w=2
- http://www.securityfocus.com/bid/1984
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5632
- http://marc.info/?l=bugtraq&m=97502995616099&w=2
- http://www.securityfocus.com/bid/1984

---

#### 290. CVE-2000-1183

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in socks5 server on Linux allows attackers to execute arbitrary commands via a long connection request.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0219.html
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0219.html

---

#### 291. CVE-2000-1189

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in pam_localuser PAM module in Red Hat Linux 7.x and 6.x allows attackers to gain privileges.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000358
- http://www.linux-mandrake.com/en/security/MDKSA-2000-082.php3
- http://www.redhat.com/support/errata/RHSA-2000-120.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5747
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000358

---

#### 292. CVE-2001-1273

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The "mxcsr P4" vulnerability in the Linux kernel before 2.2.17-14, when running on certain Intel CPUs, allows local users to cause a denial of service (system halt).

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-045.shtml
- http://www.redhat.com/support/errata/RHSA-2001-013.html
- http://ciac.llnl.gov/ciac/bulletins/l-045.shtml
- http://www.redhat.com/support/errata/RHSA-2001-013.html

---

#### 293. CVE-2000-0314

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
traceroute in NetBSD 1.3.3 and Linux systems allows local users to flood other systems by providing traceroute with a large waittime (-w) option, which is not parsed properly and sets the time delay for sending packets to zero.

**参考链接 / References**:
- ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc
- http://marc.info/?l=bugtraq&m=91893782027835&w=2
- http://www.osvdb.org/7574
- ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc
- http://marc.info/?l=bugtraq&m=91893782027835&w=2

---

#### 294. CVE-2000-0315

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
traceroute in NetBSD 1.3.3 and Linux systems allows local unprivileged users to modify the source address of the packets, which could be used in spoofing attacks.

**参考链接 / References**:
- ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc
- http://marc.info/?l=bugtraq&m=91893782027835&w=2
- http://www.osvdb.org/7575
- ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc
- http://marc.info/?l=bugtraq&m=91893782027835&w=2

---

#### 295. CVE-2001-0107

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Veritas Backup agent on Linux allows remote attackers to cause a denial of service by establishing a connection without sending any data, which causes the process to hang.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97958921407182&w=2
- http://www.securityfocus.com/bid/2204
- http://marc.info/?l=bugtraq&m=97958921407182&w=2
- http://www.securityfocus.com/bid/2204

---

#### 296. CVE-2001-0143

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
vpop3d program in linuxconf 1.23r and earlier allows local users to overwrite arbitrary files via a symlink attack.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97916374410647&w=2
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-011.php3
- http://www.securityfocus.com/bid/2186
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5923
- http://marc.info/?l=bugtraq&m=97916374410647&w=2

---

#### 297. CVE-2001-0172

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in ReiserFS 3.5.28 in SuSE Linux allows local users to cause a denial of service and possibly execute arbitrary commands by via a long directory name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0127.html
- http://www.securityfocus.com/bid/2180
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5910
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0127.html
- http://www.securityfocus.com/bid/2180

---

#### 298. CVE-2001-0181

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Format string vulnerability in the error logging code of DHCP server and client in Caldera Linux allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://www.calderasystems.com/support/security/advisories/CSSA-2001-003.0.txt
- http://www.securityfocus.com/bid/2215
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5953
- http://www.calderasystems.com/support/security/advisories/CSSA-2001-003.0.txt
- http://www.securityfocus.com/bid/2215

---

#### 299. CVE-2001-1467

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
mkpasswd in expect 5.2.8, as used by Red Hat Linux 6.2 through 7.0, seeds its random number generator with its process ID, which limits the space of possible seeds and makes it easier for attackers to conduct brute force password attacks.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0173.html
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0192.html
- http://securitytracker.com/id?1001303
- http://www.kb.cert.org/vuls/id/527736
- http://www.securityfocus.com/bid/2632

---

#### 300. CVE-2001-1390

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Unknown vulnerability in binfmt_misc in the Linux kernel before 2.2.19, related to user pages.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 301. CVE-2001-1391

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Off-by-one vulnerability in CPIA driver of Linux kernel before 2.2.19 allows users to modify kernel memory.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 302. CVE-2001-1392

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Linux kernel before 2.2.19 does not have unregister calls for (1) CPUID and (2) MSR drivers, which could cause a DoS (crash) by unloading and reloading the drivers.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 303. CVE-2001-1393

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unknown vulnerability in classifier code for Linux kernel before 2.2.19 could result in denial of service (hang).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 304. CVE-2001-1394

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Signedness error in (1) getsockopt and (2) setsockopt for Linux kernel before 2.2.19 allows local users to cause a denial of service.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 305. CVE-2001-1395

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Unknown vulnerability in sockfilter for Linux kernel before 2.2.19 related to "boundary cases," with unknown impact.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 306. CVE-2001-1396

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Unknown vulnerabilities in strnlen_user for Linux kernel before 2.2.19, with unknown impact.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 307. CVE-2001-1397

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The System V (SYS5) shared memory implementation for Linux kernel before 2.2.19 could allow attackers to modify recently freed memory.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 308. CVE-2001-1398

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Masquerading code for Linux kernel before 2.2.19 does not fully check packet lengths in certain cases, which may lead to a vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 309. CVE-2001-1399

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Certain operations in Linux kernel before 2.2.19 on the x86 architecture copy the wrong number of bytes, which might allow attackers to modify memory, aka "User access asm bug on x86."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 310. CVE-2001-1400

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unknown vulnerabilities in the UDP port allocation for Linux kernel before 2.2.19 could allow local users to cause a denial of service (deadlock).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98575345009963&w=2
- http://marc.info/?l=bugtraq&m=98637996127004&w=2
- http://marc.info/?l=bugtraq&m=98653252326445&w=2
- http://marc.info/?l=bugtraq&m=98684172109474&w=2
- http://marc.info/?l=bugtraq&m=98759029811377&w=2

---

#### 311. CVE-2001-0193

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Format string vulnerability in man in some Linux distributions allows local users to gain privileges via a malformed -l parameter.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98096782126481&w=2
- http://www.debian.org/security/2001/dsa-028
- http://www.securityfocus.com/bid/2327
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6059
- http://marc.info/?l=bugtraq&m=98096782126481&w=2

---

#### 312. CVE-2001-0229

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Chili!Soft ASP for Linux before 3.6 does not properly set group privileges when running in inherited mode, which could allow attackers to gain privileges via malicious scripts.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0112.html
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0112.html

---

#### 313. CVE-2001-0316

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Linux kernel 2.4 and 2.2 allows local users to read kernel memory and possibly gain privileges via a negative argument to the sysctl call.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0267.html
- http://www.caldera.com/support/security/advisories/CSSA-2001-009.0.txt
- http://www.osvdb.org/6017
- http://www.redhat.com/support/errata/RHSA-2001-013.html
- http://www.securityfocus.com/bid/2364

---

#### 314. CVE-2001-0317

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
Race condition in ptrace in Linux kernel 2.4 and 2.2 allows local users to gain privileges by using ptrace to track and modify a running setuid process.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0267.html
- http://www.caldera.com/support/security/advisories/CSSA-2001-009.0.txt
- http://www.redhat.com/support/errata/RHSA-2001-013.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6080
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0267.html

---

#### 315. CVE-2001-1332

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Linux CUPS before 1.1.6 may allow remote attackers to execute arbitrary code.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000386
- http://lists2.suse.com/archive/suse-security-announce/2001-Mar/0000.html
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-048.php3
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384

---

#### 316. CVE-2001-1333

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
Linux CUPS before 1.1.6 does not securely handle temporary files, possibly due to a symlink vulnerability that could allow local users to overwrite files.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000386
- http://lists2.suse.com/archive/suse-security-announce/2001-Mar/0000.html
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-048.php3
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384

---

#### 317. CVE-2001-0474

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Utah-glx in Mesa before 3.3-14 on Mandrake Linux 7.2 allows local users to overwrite arbitrary files via a symlink attack on the /tmp/glxmemory file.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-029.php3
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6231
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-029.php3
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6231

---

#### 318. CVE-2001-0481

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in rpmdrake in Mandrake Linux 8.0 related to insecure temporary file handling.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-043.php3
- http://www.osvdb.org/5612
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6494
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-043.php3
- http://www.osvdb.org/5612

---

#### 319. CVE-2001-0405

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ip_conntrack_ftp in the IPTables firewall for Linux 2.4 allows remote attackers to bypass access restrictions for an FTP server via a PORT command that lists an arbitrary IP address and port number, which is added to the RELATED table and allowed by the firewall.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0271.html
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-071.php3
- http://www.redhat.com/support/errata/RHSA-2001-052.html
- http://www.redhat.com/support/errata/RHSA-2001-084.html
- http://www.securityfocus.com/bid/2602

---

#### 320. CVE-2001-1245

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Opera 5.0 for Linux does not properly handle malformed HTTP headers, which allows remote attackers to cause a denial of service, possibly with a header whose value is the same as a MIME header name.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/196980
- http://www.iss.net/security_center/static/6838.php
- http://www.securityfocus.com/bid/3012
- http://online.securityfocus.com/archive/1/196980
- http://www.iss.net/security_center/static/6838.php

---

#### 321. CVE-2001-1146

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
AllCommerce with debugging enabled in EnGarde Secure Linux 1.0.1 creates temporary files with predictable names, which allows local users to modify files via a symlink attack.

**参考链接 / References**:
- http://www.linuxsecurity.com/advisories/other_advisory-1492.html
- http://www.securityfocus.com/bid/3016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6830
- http://www.linuxsecurity.com/advisories/other_advisory-1492.html
- http://www.securityfocus.com/bid/3016

---

#### 322. CVE-2001-1240

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The default configuration of sudo in Engarde Secure Linux 1.0.1 allows any user in the admin group to run certain commands that could be leveraged to gain full root access.

**参考链接 / References**:
- http://www.linuxsecurity.com/advisories/other_advisory-1493.html
- http://www.linuxsecurity.com/advisories/other_advisory-1493.html

---

#### 323. CVE-2001-0623

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
sendfiled, as included with Simple Asynchronous File Transfer (SAFT), on various Linux systems does not properly drop privileges when sending notification emails, which allows local attackers to gain privileges.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-050
- http://www.debian.org/security/2001/dsa-052
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6430
- http://www.debian.org/security/2001/dsa-050
- http://www.debian.org/security/2001/dsa-052

---

#### 324. CVE-2001-1130

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sdbsearch.cgi in SuSE Linux 6.0-7.2 could allow remote attackers to execute arbitrary commands by uploading a keylist.txt file that contains filenames with shell metacharacters, then causing the file to be searched using a .. in the HTTP referer (from the HTTP_REFERER variable) to point to the directory that contains the keylist.txt file.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2001_027_sdb_txt.html
- http://www.securityfocus.com/archive/1/201216
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7003
- http://www.novell.com/linux/security/advisories/2001_027_sdb_txt.html
- http://www.securityfocus.com/archive/1/201216

---

#### 325. CVE-2001-1119

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
cda in xmcd 3.0.2 and 2.6 in SuSE Linux allows local users to overwrite arbitrary files via a symlink attack.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/105347
- http://www.novell.com/linux/security/advisories/2001_025_xmcd_txt.html
- http://www.securityfocus.com/bid/3148
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6941
- http://www.kb.cert.org/vuls/id/105347

---

#### 326. CVE-2001-0525

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in dsh in dqs 3.2.7 in SuSE Linux 7.0 and earlier, and possibly other operating systems, allows local users to gain privileges via a long first command line argument.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0193.html
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0195.html
- http://www.securityfocus.com/bid/2749
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6577
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0193.html

---

#### 327. CVE-2001-0635

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Red Hat Linux 7.1 sets insecure permissions on swap files created during installation, which can allow a local attacker to gain additional privileges by reading sensitive information from the swap file, such as passwords.

**参考链接 / References**:
- http://www.osvdb.org/5564
- http://www.redhat.com/support/errata/RHSA-2001-058.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6493
- http://www.osvdb.org/5564
- http://www.redhat.com/support/errata/RHSA-2001-058.html

---

#### 328. CVE-2001-0632

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sun Chili!Soft 3.5.2 on Linux and 3.6 on AIX creates a default admin username and password in the default installation, which can allow a remote attacker to gain additional privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0378.html
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0443.html
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0378.html
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0443.html

---

#### 329. CVE-2000-1195

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
telnet daemon (telnetd) from the Linux netkit package before netkit-telnet-0.16 allows remote attackers to bypass authentication when telnetd is running with the -L command line option.

**参考链接 / References**:
- http://www.caldera.com/support/security/advisories/CSSA-2000-008.0.txt
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4225
- http://www.caldera.com/support/security/advisories/CSSA-2000-008.0.txt
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4225

---

#### 330. CVE-2001-1002

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default configuration of the DVI print filter (dvips) in Red Hat Linux 7.0 and earlier does not run dvips in secure mode when dvips is executed by lpd, which could allow remote attackers to gain privileges by printing a DVI file that contains malicious commands.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99892644616749&w=2
- http://www.redhat.com/support/errata/RHSA-2001-102.html
- http://www.securityfocus.com/bid/3241
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16509
- http://marc.info/?l=bugtraq&m=99892644616749&w=2

---

#### 331. CVE-2001-1069

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
libCoolType library as used in Adobe Acrobat (acroread) on Linux creates the AdobeFnt.lst file with world-writable permissions, which allows local users to modify the file and possibly modify acroread's behavior.

**参考链接 / References**:
- http://lists.debian.org/debian-security/2001/debian-security-200101/msg00085.html
- http://marc.info/?l=bugtraq&m=99849121502399&w=2
- http://www.securityfocus.com/bid/3225
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7024
- http://lists.debian.org/debian-security/2001/debian-security-200101/msg00085.html

---

#### 332. CVE-2001-1013

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apache on Red Hat Linux with with the UserDir directive enabled generates different error codes when a username exists and there is no public_html directory and when the username does not exist, which could allow remote attackers to determine valid usernames on the server.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vuln-dev/2000-q3/0083.html
- http://archives.neohapsis.com/archives/vuln-dev/2000-q3/0087.html
- http://archives.neohapsis.com/archives/vuln-dev/2000-q3/0094.html
- http://www.securityfocus.com/archive/1/213667
- http://www.securityfocus.com/bid/3335

---

#### 333. CVE-2001-0641

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in man program in various distributions of Linux allows local user to execute arbitrary code as group man via a long -S option.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0087.html
- http://www.novell.com/linux/security/advisories/2001_019_man_txt.html
- http://www.redhat.com/support/errata/RHSA-2001-069.html
- http://www.securityfocus.com/archive/1/190136
- http://www.securityfocus.com/bid/2711

---

#### 334. CVE-2001-0738

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
LogLine function in klogd in sysklogd 1.3 in various Linux distributions allows an attacker to cause a denial of service (hang) by causing null bytes to be placed in log messages.

**参考链接 / References**:
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-026-01
- http://marc.info/?l=bugtraq&m=99258618906506&w=2
- http://www.kb.cert.org/vuls/id/249579
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7098
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-026-01

---

#### 335. CVE-2001-0739

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Guardian Digital WebTool in EnGarde Secure Linux 1.0.1 allows restarted services to inherit some environmental variables, which could allow local users to gain root privileges.

**参考链接 / References**:
- http://www.linuxsecurity.com/advisories/other_advisory-1404.html
- http://www.redhat.com/support/errata/RHSA-2001-126.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7404
- http://www.linuxsecurity.com/advisories/other_advisory-1404.html
- http://www.redhat.com/support/errata/RHSA-2001-126.html

---

#### 336. CVE-2001-0763

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Linux xinetd 2.1.8.9pre11-1 and earlier may allow remote attackers to execute arbitrary code via a long ident response, which is not properly handled by the svc_logprint function.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-06/0064.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000404
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-024-01
- http://www.ciac.org/ciac/bulletins/l-104.shtml
- http://www.debian.org/security/2001/dsa-063

---

#### 337. CVE-2001-0775

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in xloadimage 4.1 (aka xli 1.16 and 1.17) in Linux allows remote attackers to execute arbitrary code via a FACES format image containing a long (1) Firstname or (2) Lastname field.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-069
- http://www.debian.org/security/2005/dsa-695
- http://www.gentoo.org/security/en/glsa/glsa-200503-05.xml
- http://www.iss.net/security_center/static/6821.php
- http://www.novell.com/linux/security/advisories/2001_024_xli_txt.html

---

#### 338. CVE-2001-0787

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
LPRng in Red Hat Linux 7.0 and 7.1 does not properly drop memberships in supplemental groups when lowering privileges, which could allow a local user to elevate privileges.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-096.shtml
- http://www.redhat.com/support/errata/RHSA-2001-077.html
- http://www.securityfocus.com/bid/2865
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6703
- http://www.ciac.org/ciac/bulletins/l-096.shtml

---

#### 339. CVE-2001-0907

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux kernel 2.2.1 through 2.2.19, and 2.4.1 through 2.4.10, allows local users to cause a denial of service via a series of deeply nested symlinks, which causes the kernel to spend extra time when trying to access the link.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2001-036.0.txt
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-035-01
- http://frontal2.mandriva.com/security/advisories?name=MDKSA-2001:079
- http://marc.info/?l=bugtraq&m=100343090106914&w=2
- http://marc.info/?l=bugtraq&m=100350685431610&w=2

---

#### 340. CVE-2001-1384

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
ptrace in Linux 2.2.x through 2.2.19, and 2.4.x through 2.4.9, allows local users to gain root privileges by running ptrace on a setuid or setgid program that itself calls an unprivileged program, such as newgrp.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2001-036.0.txt
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-035-01
- http://marc.info/?l=bugtraq&m=100343090106914&w=2
- http://marc.info/?l=bugtraq&m=100350685431610&w=2
- http://online.securityfocus.com/advisories/3713

---

#### 341. CVE-2001-0914

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux kernel before 2.4.11pre3 in multiple Linux distributions allows local users to cause a denial of service (crash) by starting the core vmlinux kernel, possibly related to poor error checking during ELF loading.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100638584813349&w=2
- http://marc.info/?l=bugtraq&m=100654787226869&w=2L:2
- http://www.securityfocus.com/bid/3570
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7591
- http://marc.info/?l=bugtraq&m=100638584813349&w=2

---

#### 342. CVE-2001-1449

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default installation of Apache before 1.3.19 on Mandrake Linux 7.1 through 8.0 and Linux Corporate Server 1.0.1 allows remote attackers to list the directory index of arbitrary web directories.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/913704
- http://www.mandriva.com/security/advisories?name=MDKSA-2001:077-2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8029
- http://www.kb.cert.org/vuls/id/913704
- http://www.mandriva.com/security/advisories?name=MDKSA-2001:077-2

---

#### 343. CVE-2001-0912

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Packaging error for expect 8.3.3 in Mandrake Linux 8.1 causes expect to search for its libraries in the /home/snailtalk directory before other directories, which could allow a local user to gain root privileges.

**参考链接 / References**:
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-087.php3?dis=8.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7604
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-087.php3?dis=8.1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7604

---

#### 344. CVE-2001-0819

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A buffer overflow in Linux fetchmail before 5.8.6 allows remote attackers to execute arbitrary code via a large 'To:' field in an email header.

**参考链接 / References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:43.fetchmail.asc
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000403
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-025-01
- http://www.caldera.com/support/security/advisories/CSSA-2001-022.1.txt
- http://www.debian.org/security/2001/dsa-060

---

#### 345. CVE-2001-0851

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Linux kernel 2.0, 2.2 and 2.4 with syncookies enabled allows remote attackers to bypass firewall rules by brute force guessing the cookie.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000432
- http://www.caldera.com/support/security/advisories/CSSA-2001-038.0.txt
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-082.php3
- http://www.linuxsecurity.com/advisories/other_advisory-1683.html
- http://www.novell.com/linux/security/advisories/2001_039_kernel2_txt.html

---

#### 346. CVE-2001-0852

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
TUX HTTP server 2.1.0-2 in Red Hat Linux allows remote attackers to cause a denial of service via a long Host: header.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100498100112191&w=2
- http://marc.info/?l=tux-list&m=100584714702328&w=2
- http://www.redhat.com/support/errata/RHSA-2001-142.html
- http://www.securityfocus.com/bid/3506
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7464

---

#### 347. CVE-2001-0859

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
2.4.3-12 kernel in Red Hat Linux 7.1 Korean installation program sets the setting default umask for init to 000, which installs files with world-writeable permissions.

**参考链接 / References**:
- http://online.securityfocus.com/advisories/3725
- http://www.redhat.com/support/errata/RHSA-2001-148.html
- http://www.securityfocus.com/bid/3527
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7549
- http://online.securityfocus.com/advisories/3725

---

#### 348. CVE-2001-1506

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Unknown vulnerability in the file system protection subsystem in HP Secure OS Software for Linux 1.0 allows additional user privileges on some files beyond what is specified in the file system protection rules, which allows local users to conduct unauthorized operations on restricted files.

**参考链接 / References**:
- http://online.securityfocus.com/advisories/3618
- http://www.securityfocus.com/bid/3468
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7342
- http://online.securityfocus.com/advisories/3618
- http://www.securityfocus.com/bid/3468

---

#### 349. CVE-2001-1551

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux kernel 2.2.19 enables CAP_SYS_RESOURCE for setuid processes, which allows local users to exceed disk quota restrictions during execution of setuid programs.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0179.html
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0179.html

---

#### 350. CVE-2001-1561

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Xvt 2.1 in Debian Linux 2.2 allows local users to execute arbitrary code via long (1) -name and (2) -T arguments.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-07/0024.html
- http://www.debian.org/security/2001/dsa-082
- http://www.iss.net/security_center/static/6781.php
- http://www.securityfocus.com/bid/2955
- http://www.securityfocus.com/bid/2964

---

#### 351. CVE-2001-1563

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unknown vulnerability in Tomcat 3.2.1 running on HP Secure OS for Linux 1.0 allows attackers to access servlet resources.  NOTE: due to the vagueness of the vendor advisory, it is not clear whether this issue is already covered by other CVE identifiers.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/hp/2001-q4/0062.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42892
- http://archives.neohapsis.com/archives/hp/2001-q4/0062.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42892

---

#### 352. CVE-2001-1572

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The MAC module in Netfilter in Linux kernel 2.4.1 through 2.4.11, when configured to filter based on MAC addresses, allows remote attackers to bypass packet filters via small packets.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0057.html
- http://www.iss.net/security_center/static/7267.php
- http://www.securityfocus.com/bid/3418
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0057.html
- http://www.iss.net/security_center/static/7267.php

---

#### 353. CVE-2002-0046

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Linux kernel, and possibly other operating systems, allows remote attackers to read portions of memory via a series of fragmented ICMP packets that generate an ICMP TTL Exceeded response, which includes portions of the memory in the response packet.

**参考链接 / References**:
- http://www.osvdb.org/5394
- http://www.redhat.com/support/errata/RHSA-2002-007.html
- http://www.securityfocus.com/archive/1/251418
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7998
- http://www.osvdb.org/5394

---

#### 354. CVE-2002-0060

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
IRC connection tracking helper module in the netfilter subsystem for Linux 2.4.18-pre9 and earlier does not properly set the mask for conntrack expectations for incoming DCC connections, which could allow remote attackers to bypass intended firewall restrictions.

**参考链接 / References**:
- http://frontal2.mandriva.com/security/advisories?name=MDKSA-2002:041
- http://marc.info/?l=bugtraq&m=101483396412051&w=2
- http://marc.info/?l=vuln-dev&m=101486352429653&w=2
- http://www.kb.cert.org/vuls/id/230307
- http://www.netfilter.org/security/2002-02-25-irc-dcc-mask.html

---

#### 355. CVE-2002-0062

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in ncurses 5.0, and the ncurses4 compatibility package as used in Red Hat Linux, allows local users to gain privileges, related to "routines for moving the physical cursor and scrolling."

**参考链接 / References**:
- http://www.debian.org/security/2002/dsa-113
- http://www.iss.net/security_center/static/8222.php
- http://www.redhat.com/support/errata/RHSA-2002-020.html
- http://www.securityfocus.com/bid/2116
- http://www.debian.org/security/2002/dsa-113

---

#### 356. CVE-2002-0086

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in bindsock in Lotus Domino 5.0.4 and 5.0.7 on Linux allows local users to gain root privileges via a long (1) Notes_ExecDirectory or (2) PATH environment variable.

**参考链接 / References**:
- http://www-1.ibm.com/support/docview.wss?uid=swg21095569
- http://www-1.ibm.com/support/docview.wss?uid=swg21100441
- http://www.esecurityonline.com/advisories/eSO4124.asp
- http://www.esecurityonline.com/advisories/eSO4126.asp
- http://www.securityfocus.com/bid/4317

---

#### 357. CVE-2002-0164

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Vulnerability in the MIT-SHM extension of the X server on Linux (XFree86) 4.2.1 and earlier allows local users to read and write arbitrary shared memory, possibly to cause a denial of service or gain privileges.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20021001-01-P
- ftp://stage.caldera.com/pub/security/openunix/CSSA-2002-SCO.14/CSSA-2002-SCO.14.txt
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000529
- http://marc.info/?l=bugtraq&m=103547625009363&w=2
- http://sunsolve.sun.com/search/document.do?assetkey=1-66-228529-1

---

#### 358. CVE-2002-0203

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ttawebtop.cgi in Tarantella Enterprise 3.20 on SPARC Solaris and Linux, and 3.1x and 3.0x including 3.11.903, allows remote attackers to view directory contents via an empty pg parameter.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101190195430376&w=2
- http://www.tarantella.com/security/bulletin-03.html
- http://marc.info/?l=bugtraq&m=101190195430376&w=2
- http://www.tarantella.com/security/bulletin-03.html

---

#### 359. CVE-2002-0169

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The default stylesheet for DocBook on Red Hat Linux 6.2 through 7.2 is installed with an insecure option enabled, which could allow users to overwrite files outside of the current directory from an untrusted document by using a full pathname as an element identifier.

**参考链接 / References**:
- http://online.securityfocus.com/advisories/4095
- http://www.iss.net/security_center/static/8983.php
- http://www.osvdb.org/5349
- http://www.redhat.com/support/errata/RHSA-2002-062.html
- http://www.securityfocus.com/bid/4654

---

#### 360. CVE-2002-0378

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default configuration of LPRng print spooler in Red Hat Linux 7.0 through 7.3, Mandrake 8.1 and 8.2, and other operating systems, accepts print jobs from arbitrary remote hosts.

**参考链接 / References**:
- http://online.securityfocus.com/advisories/4205
- http://www.iss.net/security_center/static/9322.php
- http://www.linux-mandrake.com/en/security/2002/MDKSA-2002-042.php
- http://www.redhat.com/support/errata/RHSA-2002-089.html
- http://www.securityfocus.com/bid/4980

---

#### 361. CVE-2002-0570

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The encrypted loop device in Linux kernel 2.4.10 and earlier does not authenticate the entity that is encrypting data, which allows local users to modify encrypted data without knowing the key.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-01/0010.html
- http://www.securityfocus.com/bid/3775
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7769
- http://archives.neohapsis.com/archives/bugtraq/2002-01/0010.html
- http://www.securityfocus.com/bid/3775

---

#### 362. CVE-2002-0429

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
The iBCS routines in arch/i386/kernel/traps.c for Linux kernels 2.4.18 and earlier on x86 systems allow local users to kill arbitrary processes via a a binary compatibility interface (lcall).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101561298818888&w=2
- http://www.debian.org/security/2003/dsa-311
- http://www.debian.org/security/2003/dsa-312
- http://www.debian.org/security/2003/dsa-332
- http://www.debian.org/security/2003/dsa-336

---

#### 363. CVE-2002-0488

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Linux Directory Penguin traceroute.pl CGI script 1.0 allows remote attackers to execute arbitrary code via shell metacharacters in the host parameter.

**参考链接 / References**:
- http://www.iss.net/security_center/static/8600.php
- http://www.linux-directory.com/scripts/traceroute.pl
- http://www.securityfocus.com/archive/1/263285
- http://www.securityfocus.com/bid/4332
- http://www.iss.net/security_center/static/8600.php

---

#### 364. CVE-2002-0489

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Linux Directory Penguin NsLookup CGI script (nslookup.pl) 1.0 allows remote attackers to execute arbitrary code via shell metacharacters in the (1) query or (2) type parameters.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101684215209558&w=2
- http://www.iss.net/security_center/static/8601.php
- http://www.securityfocus.com/bid/4353
- http://marc.info/?l=bugtraq&m=101684215209558&w=2
- http://www.iss.net/security_center/static/8601.php

---

#### 365. CVE-2002-0499

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The d_path function in Linux kernel 2.2.20 and earlier, and 2.4.18 and earlier, truncates long pathnames without generating an error, which could allow local users to force programs to perform inappropriate operations on the wrong directories.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q1/0074.html
- http://www.cs.helsinki.fi/linux/linux-kernel/2002-13/0054.html
- http://www.iss.net/security_center/static/8634.php
- http://www.securityfocus.com/archive/1/264117
- http://www.securityfocus.com/bid/4367

---

#### 366. CVE-2002-0510

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The UDP implementation in Linux 2.4.x kernels keeps the IP Identification field at 0 for all non-fragmented packets, which could allow remote attackers to determine that a target system is running Linux.

**参考链接 / References**:
- http://www.iss.net/security_center/static/8588.php
- http://www.securityfocus.com/archive/1/262840
- http://www.securityfocus.com/bid/4314
- http://www.iss.net/security_center/static/8588.php
- http://www.securityfocus.com/archive/1/262840

---

#### 367. CVE-2002-0638

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
setpwnam.c in the util-linux package, as included in Red Hat Linux 7.3 and earlier, and other operating systems, does not properly lock a temporary file when modifying /etc/passwd, which may allow local users to gain privileges via a complex race condition that uses an open file descriptor in utility programs such as chfn and chsh.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2002-043.0.txt
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0357.html
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0396.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000523
- http://marc.info/?l=bugtraq&m=102795787713996&w=2

---

#### 368. CVE-2002-0767

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
simpleinit on Linux systems does not close a read/write FIFO file descriptor before creating a child process, which allows the child process to cause simpleinit to execute arbitrary programs with root privileges.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/276739
- http://www.iss.net/security_center/static/9357.php
- http://www.securityfocus.com/bid/5001
- http://online.securityfocus.com/archive/1/276739
- http://www.iss.net/security_center/static/9357.php

---

#### 369. CVE-2002-0817

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Format string vulnerability in super for Linux allows local users to gain root privileges via a long command line argument.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q3/0045.html
- http://marc.info/?l=bugtraq&m=102812622416695&w=2
- http://www.debian.org/security/2002/dsa-139
- http://www.iss.net/security_center/static/9741.php
- http://www.securityfocus.com/bid/5367

---

#### 370. CVE-2002-0849

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Linux-iSCSI iSCSI implementation installs the iscsi.conf file with world-readable permissions on some operating systems, including Red Hat Linux Limbo Beta #1, which could allow local users to gain privileges by reading the cleartext CHAP password.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102882056105806&w=2
- http://marc.info/?l=bugtraq&m=102891036424424&w=2
- http://www.iss.net/security_center/static/9792.php
- http://www.securityfocus.com/bid/5423
- http://marc.info/?l=bugtraq&m=102882056105806&w=2

---

#### 371. CVE-2002-0910

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in netstd 3.07-17 package allows remote DNS servers to execute arbitrary code via a long FQDN reply, as observed in the utilities (1) linux-ftpd, (2) pcnfsd, (3) tftp, (4) traceroute, or (5) from/to.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/273987
- http://online.securityfocus.com/archive/1/274143
- http://www.iss.net/security_center/static/9164.php
- http://www.securityfocus.com/bid/4816
- http://online.securityfocus.com/archive/1/273987

---

#### 372. CVE-2002-0915

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
autorun in Xandros based Linux distributions allows local users to read the first line of arbitrary files via the -c parameter, which causes autorun to print the first line of the file.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-05/0260.html
- http://www.iss.net/security_center/static/9211.php
- http://www.securityfocus.com/bid/4884
- http://archives.neohapsis.com/archives/bugtraq/2002-05/0260.html
- http://www.iss.net/security_center/static/9211.php

---

#### 373. CVE-2002-1278

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The mailconf module in Linuxconf 1.24, and other versions before 1.28, on Conectiva Linux 6.0 through 8, and possibly other distributions, generates the Sendmail configuration file (sendmail.cf) in a way that configures Sendmail to run as an open mail relay, which allows remote attackers to send Spam email.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000544
- http://www.iss.net/security_center/static/10554.php
- http://www.osvdb.org/6066
- http://www.securityfocus.com/bid/6118
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000544

---

#### 374. CVE-2002-1319

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Linux kernel 2.4.20 and earlier, and 2.5.x, when running on x86 systems, allows local users to cause a denial of service (hang) via the emulation mode, which does not properly clear TF and NT EFLAGs.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000553
- http://marc.info/?l=bugtraq&m=103714004623587&w=2
- http://marc.info/?l=bugtraq&m=103737292709297&w=2
- http://rhn.redhat.com/errata/RHSA-2002-262.html
- http://rhn.redhat.com/errata/RHSA-2002-264.html

---

#### 375. CVE-2002-1380

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux kernel 2.2.x allows local users to cause a denial of service (crash) by using the mmap() function with a PROT_READ parameter to access non-readable memory pages through the /proc/pid/mem interface.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-336
- http://www.linuxsecurity.com/advisories/engarde_advisory-2976.html
- http://www.mandrakesoft.com/security/advisories?name=MDKSA-2003:039
- http://www.redhat.com/support/errata/RHSA-2003-088.html
- http://www.securityfocus.com/bid/6420

---

#### 376. CVE-2002-1571

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The linux 2.4 kernel before 2.4.19 assumes that the fninit instruction clears all registers, which could lead to an information leak on processors that do not clear all relevant SSE registers.

**参考链接 / References**:
- http://linux.bkbits.net:8080/linux-2.4/diffs/arch/i386/kernel/i387.c%401.6
- http://search.luky.org/linux-kernel.2002/msg24003.html
- http://search.luky.org/linux-kernel.2002/msg24992.html
- http://www.cs.helsinki.fi/linux/linux-kernel/2002-15/0628.html
- http://www.cs.helsinki.fi/linux/linux-kernel/2002-15/0760.html

---

#### 377. CVE-2002-1572

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Signed integer overflow in the bttv_read function in the bttv driver (bttv-driver.c) in Linux kernel before 2.4.20 has unknown impact and attack vectors.

**参考链接 / References**:
- http://linux.bkbits.net:8080/linux-2.4/cset%403d6badc0mxsPaOTT_GuPVxCp1_ormw
- http://www.redhat.com/support/errata/RHSA-2002-205.html
- http://www.redhat.com/support/errata/RHSA-2002-206.html
- http://linux.bkbits.net:8080/linux-2.4/cset%403d6badc0mxsPaOTT_GuPVxCp1_ormw
- http://www.redhat.com/support/errata/RHSA-2002-205.html

---

#### 378. CVE-2002-1573

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in the pcilynx ieee1394 firewire driver (pcilynx.c) in Linux kernel before 2.4.20 has unknown impact and attack vectors, related to "wrap handling."

**参考链接 / References**:
- http://linux.bkbits.net:8080/linux-2.4/cset%403d6aadcbBIDX67Zl6zZnVKRcsilCVQ
- http://www.redhat.com/support/errata/RHSA-2002-205.html
- http://www.redhat.com/support/errata/RHSA-2002-206.html
- http://linux.bkbits.net:8080/linux-2.4/cset%403d6aadcbBIDX67Zl6zZnVKRcsilCVQ
- http://www.redhat.com/support/errata/RHSA-2002-205.html

---

#### 379. CVE-2002-1764

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
acroread in Adobe Acrobat Reader 4.05 on Linux allows local users to overwrite arbitrary files via a symlink attack on temporary files.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/277932
- http://www.securityfocus.com/bid/5068
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9407
- http://online.securityfocus.com/archive/1/277932
- http://www.securityfocus.com/bid/5068

---

#### 380. CVE-2002-1767

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in tnslsnr of Oracle 8i Database Server 8.1.5 for Linux allows local users to execute arbitrary code as the oracle user via a long command line argument.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/265452
- http://www.securityfocus.com/bid/4413
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8772
- http://online.securityfocus.com/archive/1/265452
- http://www.securityfocus.com/bid/4413

---

#### 381. CVE-2002-1826

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
grsecurity 1.9.4 for Linux kernel 2.4.18 allows local users to bypass read-only permissions by using mmap to directly map /dev/mem or /dev/kmem to kernel memory.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/273002
- http://www.iss.net/security_center/static/9109.php
- http://www.securityfocus.com/bid/4762
- http://online.securityfocus.com/archive/1/273002
- http://www.iss.net/security_center/static/9109.php

---

#### 382. CVE-2002-1890

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
rhmask 1.0-9 in Red Hat Linux 7.1 allows local users to overwrite arbitrary files via a symlink attack on the mask file.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/276317
- http://www.iss.net/security_center/static/9335.php
- http://www.securityfocus.com/bid/4984
- http://online.securityfocus.com/archive/1/276317
- http://www.iss.net/security_center/static/9335.php

---

#### 383. CVE-2002-1963

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Linux kernel 2.4.1 through 2.4.19 sets root's NR_RESERVED_FILES limit to 10 files, which allows local users to cause a denial of service (resource exhaustion) by opening 10 setuid binaries.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/281100
- http://www.iss.net/security_center/static/9515.php
- http://www.securityfocus.com/archive/1/281359
- http://www.securityfocus.com/bid/5178
- http://online.securityfocus.com/archive/1/281100

---

#### 384. CVE-2002-1976

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
ifconfig, when used on the Linux kernel 2.2 and later, does not report when the network interface is in promiscuous mode if it was put in promiscuous mode using PACKET_MR_PROMISC, which could allow attackers to sniff the network without detection, as demonstrated using libpcap.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0279.html
- http://online.securityfocus.com/archive/1/284142
- http://online.securityfocus.com/archive/1/284257
- http://www.iss.net/security_center/static/9676.php
- http://www.securityfocus.com/bid/5304

---

#### 385. CVE-2002-2012

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Unknown vulnerability in Apache 1.3.19 running on HP Secure OS for Linux 1.0 allows remote attackers to cause "unexpected results" via an HTTP request.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7810.php
- http://www.securityfocus.com/advisories/3761
- http://www.securityfocus.com/bid/3796
- http://www.iss.net/security_center/static/7810.php
- http://www.securityfocus.com/advisories/3761

---

#### 386. CVE-2002-2016

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
User-mode Linux (UML) 2.4.17-8 does not restrict access to kernel address space, which allows local users to execute arbitrary code.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-01/0338.html
- http://www.iss.net/security_center/static/8005.php
- http://www.securityfocus.com/bid/3973
- http://archives.neohapsis.com/archives/bugtraq/2002-01/0338.html
- http://www.iss.net/security_center/static/8005.php

---

#### 387. CVE-2002-2254

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The experimental IP packet queuing feature in Netfilter / IPTables in Linux kernel 2.4 up to 2.4.19 and 2.5 up to 2.5.31, when a privileged process exits and network traffic is not being queued, may allow a later process with the same Process ID (PID) to access certain network traffic that would otherwise be restricted.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0025.html
- http://www.securityfocus.com/bid/6305
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10756
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0025.html
- http://www.securityfocus.com/bid/6305

---

#### 388. CVE-2002-2259

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the French documentation patch for Gnuplot 3.7 in SuSE Linux before 8.0 allows local users to execute arbitrary code as root via unknown attack vectors.

**参考链接 / References**:
- http://www.securityfocus.com/bid/6329
- http://www.suse.com/de/security/2002_047_openldap2.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10801
- http://www.securityfocus.com/bid/6329
- http://www.suse.com/de/security/2002_047_openldap2.html

---

#### 389. CVE-2002-2394

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
InterScan VirusWall 3.6 for Linux and 3.52 for Windows allows remote attackers to bypass virus protection and possibly execute arbitrary code via HTTP 1.1 chunked transfer encoding.

**参考链接 / References**:
- http://www.iss.net/security_center/static/10106.php
- http://www.securityfocus.com/archive/1/291538
- http://www.securityfocus.com/bid/5697
- http://www.iss.net/security_center/static/10106.php
- http://www.securityfocus.com/archive/1/291538

---

#### 390. CVE-2003-0034

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the mtink status monitor, as included in the printer-drivers package in Mandrake Linux, allows local users to execute arbitrary code via a long HOME environment variable.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html
- http://www.idefense.com/advisory/01.21.03.txt
- http://www.mandriva.com/security/advisories?name=MDKSA-2003:010
- http://www.securityfocus.com/bid/6656
- http://www.securitytracker.com/id?1005959

---

#### 391. CVE-2003-0035

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in escputil, as included in the printer-drivers package in Mandrake Linux, allows local users to execute arbitrary code via a long printer-name command line argument.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html
- http://www.idefense.com/advisory/01.21.03.txt
- http://www.mandriva.com/security/advisories?name=MDKSA-2003:010
- http://www.securityfocus.com/archive/1/307608/30/26270/threaded
- http://www.securityfocus.com/bid/6658

---

#### 392. CVE-2003-0036

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
ml85p, as included in the printer-drivers package for Mandrake Linux, allows local users to overwrite arbitrary files via a symlink attack on temporary files with predictable filenames of the form "mlg85p%d".

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html
- http://www.idefense.com/advisory/01.21.03.txt
- http://www.mandriva.com/security/advisories?name=MDKSA-2003:010
- http://www.securityfocus.com/archive/1/307608/30/26270/threaded
- http://www.securitytracker.com/id?1005959

---

#### 393. CVE-2003-0018

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Linux kernel 2.4.10 through 2.4.21-pre4 does not properly handle the O_DIRECT feature, which allows local attackers with write privileges to read portions of previously deleted files, or cause file system corruption.

**参考链接 / References**:
- http://linux.bkbits.net:8080/linux-2.4/cset%403e2f193drGJDBg9SG6JwaDQwCBnAMQ
- http://www.debian.org/security/2003/dsa-358
- http://www.debian.org/security/2004/dsa-423
- http://www.iss.net/security_center/static/11249.php
- http://www.mandrakesoft.com/security/advisories?name=MDKSA-2003:014

---

#### 394. CVE-2003-0019

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
uml_net in the kernel-utils package for Red Hat Linux 8.0 has incorrect setuid root privileges, which allows local users to modify network interfaces, e.g. by modifying ARP entries or placing interfaces into promiscuous mode.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/n-044.shtml
- http://www.iss.net/security_center/static/11276.php
- http://www.kb.cert.org/vuls/id/134025
- http://www.redhat.com/support/errata/RHSA-2003-056.html
- http://www.securityfocus.com/bid/6801

---

#### 395. CVE-2003-0076

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Unknown vulnerability in the directory parser for Direct Connect 4 Linux (dcgui) before 0.2.2 allows remote attackers to read files outside the sharelist.

**参考链接 / References**:
- http://dc.ketelhot.de/pipermail/dc/2003-January/000094.html
- http://marc.info/?l=bugtraq&m=104437720116243&w=2
- http://www.iss.net/security_center/static/11246.php
- http://dc.ketelhot.de/pipermail/dc/2003-January/000094.html
- http://marc.info/?l=bugtraq&m=104437720116243&w=2

---

#### 396. CVE-2003-0094

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A patch for mcookie in the util-linux package for Mandrake Linux 8.2 and 9.0 uses /dev/urandom instead of /dev/random, which causes mcookie to use an entropy source that is more predictable than expected, which may make it easier for certain types of attacks to succeed.

**参考链接 / References**:
- http://www.mandrakesoft.com/security/advisories?name=MDKSA-2003:016
- http://www.securityfocus.com/bid/6855
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11318
- http://www.mandrakesoft.com/security/advisories?name=MDKSA-2003:016
- http://www.securityfocus.com/bid/6855

---

#### 397. CVE-2003-0156

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Directory traversal vulnerability in Cross-Referencing Linux (LXR) allows remote attackers to read arbitrary files via .. (dot dot) sequences in the v parameter.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=104739747222492&w=2
- http://www.debian.org/security/2003/dsa-264
- http://www.securityfocus.com/bid/7062
- http://marc.info/?l=bugtraq&m=104739747222492&w=2
- http://www.debian.org/security/2003/dsa-264

---

#### 398. CVE-2003-0080

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The iptables ruleset in Gnome-lokkit in Red Hat Linux 8.0 does not include any rules in the FORWARD chain, which could allow attackers to bypass intended access restrictions if packet forwarding is enabled.

**参考链接 / References**:
- http://www.osvdb.org/4400
- http://www.redhat.com/support/errata/RHSA-2003-072.html
- http://www.securityfocus.com/bid/7128
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11552
- http://www.osvdb.org/4400

---

#### 399. CVE-2003-0127

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The kernel module loader in Linux kernel 2.2.x before 2.2.25, and 2.4.x before 2.4.21, allows local users to gain root privileges by using ptrace to attach to a child process that is spawned by the kernel.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2003-020.0.txt
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0134.html
- http://marc.info/?l=bugtraq&m=105301461726555&w=2
- http://rhn.redhat.com/errata/RHSA-2003-088.html
- http://rhn.redhat.com/errata/RHSA-2003-098.html

---

#### 400. CVE-2002-1492

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflows in the Cisco VPN 5000 Client before 5.2.7 for Linux, and VPN 5000 Client before 5.2.8 for Solaris, allow local users to gain root privileges via (1) close_tunnel and (2) open_tunnel.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml
- http://www.iss.net/security_center/static/10131.php
- http://www.securityfocus.com/bid/5734
- http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml
- http://www.iss.net/security_center/static/10131.php

---

#### 401. CVE-2002-1506

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Linuxconf before 1.28r4 allows local users to execute arbitrary code via a long LINUXCONF_LANG environment variable, which overflows an error string that is generated.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-08/0304.html
- http://archives.neohapsis.com/archives/vulnwatch/2002-q3/0093.html
- http://www.iss.net/security_center/static/9980.php
- http://www.securityfocus.com/bid/5585
- http://www.solucorp.qc.ca/changes.hc?projet=linuxconf&version=1.28r4

---

#### 402. CVE-2003-0135

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
vsftpd FTP daemon in Red Hat Linux 9 is not compiled against TCP wrappers (tcp_wrappers) but is installed as a standalone service, which inadvertently prevents vsftpd from restricting access as intended.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2003-084.html
- http://www.securityfocus.com/bid/7253
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A634
- http://www.redhat.com/support/errata/RHSA-2003-084.html
- http://www.securityfocus.com/bid/7253

---

#### 403. CVE-2003-0084

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
mod_auth_any package in Red Hat Enterprise Linux 2.1 and other operating systems does not properly escape arguments when calling other programs, which allows attackers to execute arbitrary commands via shell metacharacters.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2003-114.html
- http://www.ciac.org/ciac/bulletins/n-090.shtml
- http://www.itlab.musc.edu/webNIS/mod_auth_any.html
- http://www.redhat.com/support/errata/RHSA-2003-113.html
- http://www.securityfocus.com/bid/7448

---

#### 404. CVE-2003-0244

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The route cache implementation in Linux 2.4, and the Netfilter IP conntrack module, allows remote attackers to cause a denial of service (CPU consumption) via packets with forged source addresses that cause a large number of hash table collisions.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q2/0073.html
- http://marc.info/?l=bugtraq&m=105301461726555&w=2
- http://marc.info/?l=bugtraq&m=105595901923063&w=2
- http://marc.info/?l=linux-kernel&m=104956079213417
- http://www.debian.org/security/2003/dsa-311

---

#### 405. CVE-2003-0246

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
The ioperm system call in Linux kernel 2.4.20 and earlier does not properly restrict privileges, which allows local users to gain read or write access to certain I/O ports.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q2/0076.html
- http://marc.info/?l=bugtraq&m=105301461726555&w=2
- http://www.debian.org/security/2003/dsa-311
- http://www.debian.org/security/2003/dsa-312
- http://www.debian.org/security/2003/dsa-332

---

#### 406. CVE-2003-0247

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Unknown vulnerability in the TTY layer of the Linux kernel 2.4 allows attackers to cause a denial of service ("kernel oops").

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-311
- http://www.debian.org/security/2003/dsa-312
- http://www.debian.org/security/2003/dsa-332
- http://www.debian.org/security/2003/dsa-336
- http://www.debian.org/security/2004/dsa-442

---

#### 407. CVE-2003-0248

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The mxcsr code in Linux kernel 2.4 allows attackers to modify CPU state registers via a malformed address.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-311
- http://www.debian.org/security/2003/dsa-312
- http://www.debian.org/security/2003/dsa-332
- http://www.debian.org/security/2003/dsa-336
- http://www.debian.org/security/2004/dsa-442

---

#### 408. CVE-2003-0364

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The TCP/IP fragment reassembly handling in the Linux kernel 2.4 allows remote attackers to cause a denial of service (CPU consumption) via certain packets that cause a large number of hash table collisions.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-311
- http://www.debian.org/security/2003/dsa-312
- http://www.debian.org/security/2003/dsa-332
- http://www.debian.org/security/2003/dsa-336
- http://www.debian.org/security/2004/dsa-442

---

#### 409. CVE-2003-0396

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in les for ATM on Linux (linux-atm) before 2.4.1, if used setuid, allows local users to gain privileges via a long -f command line argument.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105154433926396&w=2
- http://marc.info/?l=bugtraq&m=105405560021979&w=2
- http://sourceforge.net/project/shownotes.php?release_id=156242
- http://www.securiteam.com/exploits/5EP0M1P9PO.html
- http://www.securityfocus.com/bid/7437

---

#### 410. CVE-2003-0388

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
pam_wheel in Linux-PAM 0.78, with the trust option enabled and the use_uid option disabled, allows local users to spoof log entries and gain privileges by causing getlogin() to return a spoofed user name.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105577915506761&w=2
- http://www.idefense.com/advisory/06.16.03.txt
- http://www.redhat.com/support/errata/RHSA-2004-304.html
- http://marc.info/?l=bugtraq&m=105577915506761&w=2
- http://www.idefense.com/advisory/06.16.03.txt

---

#### 411. CVE-2003-0418

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Linux 2.0 kernel IP stack does not properly calculate the size of an ICMP citation, which causes it to include portions of unauthorized memory in ICMP error responses.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105519179005065&w=2
- http://www.cartel-securite.fr/pbiondi/adv/CARTSA-20030314-icmpleak.txt
- http://www.kb.cert.org/vuls/id/471084
- http://marc.info/?l=bugtraq&m=105519179005065&w=2
- http://www.cartel-securite.fr/pbiondi/adv/CARTSA-20030314-icmpleak.txt

---

#### 412. CVE-2003-0643

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Integer signedness error in the Linux Socket Filter implementation (filter.c) in Linux 2.4.3-pre3 to 2.4.22-pre10 allows attackers to cause a denial of service (crash).

**参考链接 / References**:
- http://ftp.belnet.be/linux/gentoo-portage/sys-kernel/gentoo-sources/files/gentoo-sources-2.4.CAN-2003-0643.patch
- http://gentoo.kems.net/gentoo-x86-portage/sys-kernel/gentoo-sources/ChangeLog
- http://mirror.clarkson.edu/pub/distributions/gentoo-portage/sys-kernel/wolk-sources/ChangeLog
- http://secunia.com/advisories/23265
- http://www.ultramonkey.org/bugs/cve-patch/CAN-2003-0643.patch

---

#### 413. CVE-2003-0476

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The execve system call in Linux 2.4.x records the file descriptor of the executable process in the file table of the calling process, which allows local users to gain read access to restricted file descriptors.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105664924024009&w=2
- http://www.debian.org/security/2004/dsa-358
- http://www.debian.org/security/2004/dsa-423
- http://www.mandriva.com/security/advisories?name=MDKSA-2003:074
- http://www.redhat.com/support/errata/RHSA-2003-238.html

---

#### 414. CVE-2003-0480

**严重程度 / Severity**: N/A | CVSS: 3.7

**漏洞描述 / Description**:
VMware Workstation 4.0 for Linux allows local users to overwrite arbitrary files and gain privileges via "symlink manipulation."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105673688529147&w=2
- http://www.vmware.com/support/kb/enduser/std_adp.php?p_faqid=1019
- http://marc.info/?l=bugtraq&m=105673688529147&w=2
- http://www.vmware.com/support/kb/enduser/std_adp.php?p_faqid=1019

---

#### 415. CVE-2003-0501

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The /proc filesystem in Linux allows local users to obtain sensitive information by opening various entries in /proc/self before executing a setuid program, which causes the program to fail to change the ownership and permissions of those entries.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=105621758104242
- http://www.debian.org/security/2004/dsa-358
- http://www.debian.org/security/2004/dsa-423
- http://www.redhat.com/support/errata/RHSA-2003-198.html
- http://www.redhat.com/support/errata/RHSA-2003-238.html

---

#### 416. CVE-2026-6868 - wireshark: Wireshark: Denial of Service via malicious network capture file

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] wireshark: Wireshark: Denial of Service via malicious network capture file. Bugzilla: 2464010

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464010

---

#### 417. CVE-2026-7378 - Wireshark: sharkd: Wireshark sharkd: Denial of Service via crash vulnerability

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] Wireshark: sharkd: Wireshark sharkd: Denial of Service via crash vulnerability. Bugzilla: 2464005

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464005

---

#### 418. CVE-2026-7375 - Wireshark: Wireshark: Denial of Service via UDS protocol dissector infinite loop

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] Wireshark: Wireshark: Denial of Service via UDS protocol dissector infinite loop. Bugzilla: 2464007

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464007

---

#### 419. CVE-2026-7376 - Wireshark: sharkd: Wireshark sharkd: Denial of Service due to crash

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] Wireshark: sharkd: Wireshark sharkd: Denial of Service due to crash. Bugzilla: 2464008

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464008

---

#### 420. CVE-2026-41636 - apache.com/apache/thrift: Apache Thrift: Node.js skip() recursion

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] apache.com/apache/thrift: Apache Thrift: Node.js skip() recursion. Bugzilla: 2463404

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463404

---

#### 421. CVE-2026-41607 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read vulnerability. Bugzilla: 2463412

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463412

---

#### 422. CVE-2026-41606 - Apache Thrift: Apache Thrift: Denial of Service via uncontrolled recursion

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: Apache Thrift: Denial of Service via uncontrolled recursion. Bugzilla: 2463408

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463408

---

#### 423. CVE-2026-41605 - Apache Thrift: Apache Thrift: Integer Overflow or Wraparound Vulnerability

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: Apache Thrift: Integer Overflow or Wraparound Vulnerability. Bugzilla: 2463418

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463418

---

#### 424. CVE-2026-41604 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read vulnerability. Bugzilla: 2463416

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463416

---

#### 425. CVE-2026-41603 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Security Bypass via…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Security Bypass via Improper Certificate Hostname Validation. Bugzilla: 2463411

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463411

---

#### 426. CVE-2026-41602 - github.com/apache/thrift: Apache Thrift: Integer Overflow in TFramedTransport Go…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] github.com/apache/thrift: Apache Thrift: Integer Overflow in TFramedTransport Go implementation. Bugzilla: 2463407

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463407

---

#### 427. [Ubuntu] USN-8226-1: kmod update

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disables loading the algif_aead module as a measure to mitigate the issue until kernel updates are made available. See the following URL for more information https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-1

---

#### 428. [Ubuntu] USN-8218-1: zuluCrypt vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Aaron Rainbolt discovered that zuluCrypt used insecure PolicyKit settings in zuluPolkit. An attacker could possibly use this issue to cause local privilege escalation to root. (CVE-2025-53391)

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8218-1

---

#### 429. CVE-2013-1069

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Ubuntu Metal as a Service (MaaS) 1.2 and 1.4 uses world-readable permissions for txlongpoll.yaml, which allows local users to obtain RabbitMQ authentication credentials by reading the file.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/maas/%2Bbug/1254034
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/maas/%2Bbug/1254034

---

#### 430. CVE-2013-1070

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in the API in Ubuntu Metal as a Service (MaaS) 1.2 and 1.4 allows remote attackers to inject arbitrary web script or HTML via the op parameter to nodes/.

**参考链接 / References**:
- http://www.securityfocus.com/bid/65575
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/maas/%2Bbug/1251336
- http://www.securityfocus.com/bid/65575
- http://www.ubuntu.com/usn/USN-2105-1

---

#### 431. CVE-2011-3628

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
Untrusted search path vulnerability in pam_motd (aka the MOTD module) in libpam-modules before 1.1.3-2ubuntu2.1 on Ubuntu 11.10, before 1.1.2-2ubuntu8.4 on Ubuntu 11.04, before 1.1.1-4ubuntu2.4 on Ubuntu 10.10, before 1.1.1-2ubuntu5.4 on Ubuntu 10.04 LTS, and before 0.99.7.1-5ubuntu6.5 on Ubuntu 8.04 LTS, when using certain configurations such as "session optional pam_motd.so", allows local users to gain privileges by modifying the PATH environment variable to reference a malicious command, as demonstrated via uname.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1237-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/pam/%2Bbug/610125
- http://www.ubuntu.com/usn/USN-1237-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/pam/%2Bbug/610125

---

#### 432. CVE-2011-4406

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
The Ubuntu AccountsService package before 0.6.14-1git1ubuntu1.1 does not properly drop privileges when changing language settings, which allows local users to modify arbitrary files via unspecified vectors.

**参考链接 / References**:
- http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/oneiric/accountsservice/oneiric-updates/revision/21
- http://people.canonical.com/~ubuntu-security/cve/2011/CVE-2011-4406.html
- http://www.ubuntu.com/usn/USN-1351-1
- http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/oneiric/accountsservice/oneiric-updates/revision/21
- http://people.canonical.com/~ubuntu-security/cve/2011/CVE-2011-4406.html

---

#### 433. CVE-2011-3152

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
DistUpgrade/DistUpgradeFetcherCore.py in Update Manager before 1:0.87.31.1, 1:0.134.x before 1:0.134.11.1, 1:0.142.x before 1:0.142.23.1, 1:0.150.x before 1:0.150.5.1, and 1:0.152.x before 1:0.152.25.5 on Ubuntu 8.04 through 11.10 does not verify the GPG signature before extracting an upgrade tarball, which allows man-in-the-middle attackers to (1) create or overwrite arbitrary files via a directory traversal attack using a crafted tar file, or (2) bypass authentication via a crafted meta-release file.

**参考链接 / References**:
- http://secunia.com/advisories/47024
- http://www.osvdb.org/77642
- http://www.securityfocus.com/bid/50833
- http://www.ubuntu.com/usn/USN-1284-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/881548

---

#### 434. CVE-2013-7374

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Ubuntu Date and Time Indicator (aka indicator-datetime) 13.10.0+13.10.x before 13.10.0+13.10.20131023.2-0ubuntu1.1 does not properly restrict access to Evolution, which allows local users to bypass the greeter screen restrictions by clicking the date.

**参考链接 / References**:
- http://bazaar.launchpad.net/~indicator-applet-developers/indicator-datetime/trunk.13.10/revision/282
- http://www.openwall.com/lists/oss-security/2014/04/29/3
- http://www.openwall.com/lists/oss-security/2014/04/30/1
- http://www.ubuntu.com/usn/USN-2186-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/indicator-datetime/%2Bbug/1246812

---

#### 435. CVE-2014-3203

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
Unity before 7.2.1, as used in Ubuntu 14.04, does not properly restrict access to the Dash when the lock screen is active, which allows physically proximate attackers to bypass the lock screen and execute arbitrary commands, as demonstrated by pressing the SUPER key before the screen auto-locks.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2184-1
- http://www.openwall.com/lists/oss-security/2014/04/29/2
- http://www.openwall.com/lists/oss-security/2014/05/03/1
- https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1308850
- http://ubuntu.com/usn/usn-2184-1

---

#### 436. CVE-2014-3204

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
Unity before 7.2.1, as used in Ubuntu 14.04, does not properly handle keyboard shortcuts, which allows physically proximate attackers to bypass the lock screen and execute arbitrary commands, as demonstrated by right-clicking on the indicator bar and then pressing the ALT and F2 keys.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2184-1
- http://www.openwall.com/lists/oss-security/2014/04/29/2
- http://www.openwall.com/lists/oss-security/2014/05/03/1
- http://www.securityfocus.com/bid/67117
- https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1313885

---

#### 437. CVE-2014-0462

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in OpenJDK 6 before 6b31 on Debian GNU/Linux and Ubuntu 12.04 LTS and 10.04 LTS has unknown impact and attack vectors, a different vulnerability than CVE-2014-2405.

**参考链接 / References**:
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912
- http://www.ubuntu.com/usn/USN-2191-1
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912

---

#### 438. CVE-2014-2405

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in OpenJDK 6 before 6b31 on Debian GNU/Linux and Ubuntu 12.04 LTS and 10.04 LTS has unknown impact and attack vectors, a different vulnerability than CVE-2014-0462.

**参考链接 / References**:
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912
- http://www.ubuntu.com/usn/USN-2191-1
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912

---

#### 439. CVE-2012-0943

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
debian/guest-account in Light Display Manager (lightdm) 1.0.x before 1.0.6 and 1.1.x before 1.1.7, as used in Ubuntu Linux 11.10, allows local users to delete arbitrary files via a space in the name of a file in /tmp.  NOTE: this identifier was SPLIT per ADT1/ADT2 due to different codebases and affected versions. CVE-2012-6648 has been assigned for the gdm-guest-session issue.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1399-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044
- https://launchpadlibrarian.net/96471251/lightdm.secure-cleanup.debdiff
- http://www.ubuntu.com/usn/USN-1399-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044

---

#### 440. CVE-2012-6648

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
gdm/guest-session-cleanup.sh in gdm-guest-session 0.24 and earlier, as used in Ubuntu Linux 10.04 LTS, 10.10, and 11.04, allows local users to delete arbitrary files via a space in the name of a file in /tmp. NOTE: this identifier was SPLIT from CVE-2012-0943 per ADT1/ADT2 due to different codebases and affected versions. CVE-2012-0943 is used for the guest-account issue.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-1399-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044
- https://launchpadlibrarian.net/96474113/gdm-guest-session.secure-cleanup.debdiff
- http://ubuntu.com/usn/usn-1399-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044

---

#### 441. CVE-2013-1068

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The OpenStack Nova (python-nova) package 1:2013.2.3-0 before 1:2013.2.3-0ubuntu1.2 and 1:2014.1-0 before 1:2014.1-0ubuntu1.2 and Openstack Cinder (python-cinder) package 1:2013.2.3-0 before 1:2013.2.3-0ubuntu1.1 and 1:2014.1-0 before 1:2014.1-0ubuntu1.1 for Ubuntu 13.10 and 14.04 LTS does not properly set the sudo configuration, which makes it easier for attackers to gain privileges by leveraging another vulnerability.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2248-1
- http://www.ubuntu.com/usn/USN-2247-1
- http://ubuntu.com/usn/usn-2248-1
- http://www.ubuntu.com/usn/USN-2247-1

---

#### 442. CVE-2014-5195

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Unity before 7.2.3 and 7.3.x before 7.3.1, as used in Ubuntu, does not properly take focus of the keyboard when switching to the lock screen, which allows physically proximate attackers to bypass the lock screen by (1) leveraging a machine that had text selected when locking or (2) resuming from a suspension.

**参考链接 / References**:
- http://www.osvdb.org/109788
- http://www.securityfocus.com/bid/68987
- http://www.ubuntu.com/usn/USN-2303-1
- https://bugs.launchpad.net/unity/7.2/+bug/1349128
- https://exchange.xforce.ibmcloud.com/vulnerabilities/95199

---

#### 443. CVE-2014-1424

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
apparmor_parser in the apparmor package before 2.8.95~2430-0ubuntu5.1 in Ubuntu 14.04 allows attackers to bypass AppArmor policies via unspecified vectors, related to a "miscompilation flaw."

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2413-1
- http://www.ubuntu.com/usn/USN-2413-1

---

#### 444. CVE-2014-1421

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
mountall 1.54, as used in Ubuntu 14.10, does not properly handle the umask when using the mount utility, which allows local users to bypass intended access restrictions via unspecified vectors.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2411-1
- http://www.ubuntu.com/usn/USN-2411-1

---

#### 445. CVE-2015-2285

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The logrotation script (/etc/cron.daily/upstart) in the Ubuntu Upstart package before 1.13.2-0ubuntu9, as used in Ubuntu Vivid 15.04, allows local users to execute arbitrary commands and gain privileges via a crafted file in /run/user/*/upstart/sessions/.

**参考链接 / References**:
- http://packetstormsecurity.com/files/130587/Ubuntu-Vivid-Upstart-Privilege-Escalation.html
- http://seclists.org/fulldisclosure/2015/Mar/7
- http://www.halfdog.net/Security/2015/UpstartLogrotationPrivilegeEscalation/
- https://bugs.launchpad.net/ubuntu/+source/upstart/+bug/1425685
- http://packetstormsecurity.com/files/130587/Ubuntu-Vivid-Upstart-Privilege-Escalation.html

---

#### 446. CVE-2015-1322

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Directory traversal vulnerability in the Ubuntu network-manager package for Ubuntu (vivid) before 0.9.10.0-4ubuntu15.1, Ubuntu 14.10 before 0.9.8.8-0ubuntu28.1, and Ubuntu 14.04 LTS before 0.9.8.8-0ubuntu7.1 allows local users to change the modem device configuration or read arbitrary files via a .. (dot dot) in the file name in a request to read modem device contexts (com.canonical.NMOfono.ReadImsiContexts).

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2581-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/network-manager/%2Bbug/1449245
- http://www.ubuntu.com/usn/USN-2581-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/network-manager/%2Bbug/1449245

---

#### 447. CVE-2015-8222

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The lxd-unix.socket systemd unit file in the Ubuntu lxd package before 0.20-0ubuntu4.1 uses world-readable permissions for /var/lib/lxd/unix.socket, which allows local users to gain privileges via unspecified vectors.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2809-1
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1515689
- https://github.com/lxc/lxd/issues/1307
- http://www.ubuntu.com/usn/USN-2809-1
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1515689

---

#### 448. CVE-2016-2856

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
pt_chown in the glibc package before 2.19-18+deb8u4 on Debian jessie; the elibc package before 2.15-0ubuntu10.14 on Ubuntu 12.04 LTS and before 2.19-0ubuntu6.8 on Ubuntu 14.04 LTS; and the glibc package before 2.21-0ubuntu4.2 on Ubuntu 15.10 and before 2.23-0ubuntu1 on Ubuntu 16.04 LTS and 16.10 lacks a namespace check associated with file-descriptor passing, which allows local users to capture keystrokes and spoof data, and possibly gain privileges, via pts read and write operations, related to debian/sysdeps/linux.mk.  NOTE: this is not considered a vulnerability in the upstream GNU C Library because the upstream documentation has a clear security recommendation against the --enable-pt_chown option.

**参考链接 / References**:
- http://anonscm.debian.org/cgit/pkg-glibc/glibc.git/commit/?h=jessie&id=09f7764882a81e13e7b5d87d715412283a6ce403
- http://anonscm.debian.org/cgit/pkg-glibc/glibc.git/commit/?h=jessie&id=11475c083282c1582c4dd72eecfcb2b7d308c958
- http://people.canonical.com/~ubuntu-security/cve/2016/CVE-2016-2856.html
- http://www.halfdog.net/Security/2015/PtChownArbitraryPtsAccessViaUserNamespace/
- http://www.openwall.com/lists/oss-security/2016/02/23/3

---

#### 449. CVE-2016-1580

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The setup_snappy_os_mounts function in the ubuntu-core-launcher package before 1.0.27.1 improperly determines the mount point of bind mounts when using snaps, which might allow remote attackers to obtain sensitive information or gain privileges via a snap with a name starting with "ubuntu-core."

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2956-1
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-core-launcher/+bug/1576699
- http://www.ubuntu.com/usn/USN-2956-1
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-core-launcher/+bug/1576699

---

#### 450. CVE-2016-1240

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The Tomcat init script in the tomcat7 package before 7.0.56-3+deb8u4 and tomcat8 package before 8.0.14-1+deb8u3 on Debian jessie and the tomcat6 and libtomcat6-java packages before 6.0.35-1ubuntu3.8 on Ubuntu 12.04 LTS, the tomcat7 and libtomcat7-java packages before 7.0.52-1ubuntu0.7 on Ubuntu 14.04 LTS, and tomcat8 and libtomcat8-java packages before 8.0.32-1ubuntu1.2 on Ubuntu 16.04 LTS allows local users with access to the tomcat account to gain root privileges via a symlink attack on the Catalina log file, as demonstrated by /var/log/tomcat7/catalina.out.

**参考链接 / References**:
- http://legalhackers.com/advisories/Tomcat-DebPkgs-Root-Privilege-Escalation-Exploit-CVE-2016-1240.html
- http://packetstormsecurity.com/files/170857/Apache-Tomcat-On-Ubuntu-Log-Init-Privilege-Escalation.html
- http://rhn.redhat.com/errata/RHSA-2017-0457.html
- http://www.debian.org/security/2016/dsa-3669
- http://www.debian.org/security/2016/dsa-3670

---

#### 451. CVE-2015-1328

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The overlayfs implementation in the linux (aka Linux kernel) package before 3.19.0-21.21 in Ubuntu through 15.04 does not properly check permissions for file creation in the upper filesystem directory, which allows local users to obtain root access by leveraging a configuration in which overlayfs is permitted in an arbitrary mount namespace.

**参考链接 / References**:
- http://seclists.org/oss-sec/2015/q2/717
- http://www.exploit-db.com/exploits/40688/
- http://www.securityfocus.com/bid/75206
- https://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1328.html
- https://security-tracker.debian.org/tracker/CVE-2015-1328

---

#### 452. CVE-2016-1247

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The nginx package before 1.6.2-5+deb8u3 on Debian jessie, the nginx packages before 1.4.6-1ubuntu3.6 on Ubuntu 14.04 LTS, before 1.10.0-0ubuntu0.16.04.3 on Ubuntu 16.04 LTS, and before 1.10.1-0ubuntu1.1 on Ubuntu 16.10, and the nginx ebuild before 1.10.2-r3 on Gentoo allow local users with access to the web server user account to gain root privileges via a symlink attack on the error log.

**参考链接 / References**:
- http://packetstormsecurity.com/files/139750/Nginx-Debian-Based-Distros-Root-Privilege-Escalation.html
- http://seclists.org/fulldisclosure/2016/Nov/78
- http://seclists.org/fulldisclosure/2017/Jan/33
- http://www.debian.org/security/2016/dsa-3701
- http://www.securityfocus.com/archive/1/539796/100/0/threaded

---

#### 453. CVE-2015-8768

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
click/install.py in click does not require files in package filesystem tarballs to start with ./ (dot slash), which allows remote attackers to install an alternate security policy and gain privileges via a crafted package, as demonstrated by the test.mmrow app for Ubuntu phone.

**参考链接 / References**:
- http://bazaar.launchpad.net/~click-hackers/click/devel/revision/587
- http://ubuntu.com/usn/usn-2771-1
- http://www.openwall.com/lists/oss-security/2016/01/12/8
- http://www.securityfocus.com/bid/96386
- https://bugs.launchpad.net/ubuntu/+source/click/+bug/1506467

---

#### 454. CVE-2017-6056

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
It was discovered that a programming error in the processing of HTTPS requests in the Apache Tomcat servlet and JSP engine may result in denial of service via an infinite loop. The denial of service is easily achievable as a consequence of backporting a CVE-2016-6816 fix but not backporting the fix for Tomcat bug 57544. Distributions affected by this backporting issue include Debian (before 7.0.56-3+deb8u8 and 8.0.14-1+deb8u7 in jessie) and Ubuntu.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2017-0517.html
- http://rhn.redhat.com/errata/RHSA-2017-0826.html
- http://rhn.redhat.com/errata/RHSA-2017-0827.html
- http://rhn.redhat.com/errata/RHSA-2017-0828.html
- http://rhn.redhat.com/errata/RHSA-2017-0829.html

---

#### 455. CVE-2017-6590

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
An issue was discovered in network-manager-applet (aka network-manager-gnome) in Ubuntu 12.04 LTS, 14.04 LTS, 16.04 LTS, and 16.10. A local attacker could use this issue at the default Ubuntu login screen to access local files and execute arbitrary commands as the lightdm user. The exploitation requires physical access to the locked computer and the Wi-Fi must be turned on. An access point that lets you use a certificate to login is required as well, but it's easy to create one. Then, it's possible to open a nautilus window and browse directories. One also can open some applications such as Firefox, which is useful for downloading malicious binaries.

**参考链接 / References**:
- http://www.securitytracker.com/id/1037977
- https://bugs.launchpad.net/ubuntu/+source/network-manager-applet/+bug/1668321
- https://security.gentoo.org/glsa/201707-09
- https://www.ubuntu.com/usn/usn-3217-1/
- https://www.youtube.com/watch?v=Fp2lwRVg0l0

---

#### 456. CVE-2017-7184

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The xfrm_replay_verify_len function in net/xfrm/xfrm_user.c in the Linux kernel through 4.10.6 does not validate certain size data after an XFRM_MSG_NEWAE update, which allows local users to obtain root privileges or cause a denial of service (heap-based out-of-bounds access) by leveraging the CAP_NET_ADMIN capability, as demonstrated during a Pwn2Own competition at CanSecWest 2017 for the Ubuntu 16.10 linux-image-* package 4.8.0.41.52.

**参考链接 / References**:
- http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=677e806da4d916052585301785d847c3b3e6186a
- http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=f843ee6dd019bcece3e74e76ad9df0155655d0df
- http://openwall.com/lists/oss-security/2017/03/29/2
- http://www.eweek.com/security/ubuntu-linux-falls-on-day-1-of-pwn2own-hacking-competition
- http://www.securityfocus.com/bid/97018

---

#### 457. CVE-2016-9774

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The postinst script in the tomcat6 package before 6.0.45+dfsg-1~deb7u4 on Debian wheezy, before 6.0.35-1ubuntu3.9 on Ubuntu 12.04 LTS and on Ubuntu 14.04 LTS; the tomcat7 package before 7.0.28-4+deb7u8 on Debian wheezy, before 7.0.56-3+deb8u6 on Debian jessie, before 7.0.52-1ubuntu0.8 on Ubuntu 14.04 LTS, and on Ubuntu 12.04 LTS, 16.04 LTS, and 16.10; and the tomcat8 package before 8.0.14-1+deb8u5 on Debian jessie, before 8.0.32-1ubuntu1.3 on Ubuntu 16.04 LTS, before 8.0.37-1ubuntu0.1 on Ubuntu 16.10, and before 8.0.38-2ubuntu1 on Ubuntu 17.04 might allow local users with access to the tomcat account to obtain sensitive information or gain root privileges via a symlink attack on the Catalina localhost directory.

**参考链接 / References**:
- http://www.debian.org/security/2016/dsa-3738
- http://www.debian.org/security/2016/dsa-3739
- http://www.openwall.com/lists/oss-security/2016/12/02/10
- http://www.openwall.com/lists/oss-security/2016/12/02/5
- http://www.securityfocus.com/bid/94643

---

#### 458. CVE-2016-9775

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The postrm script in the tomcat6 package before 6.0.45+dfsg-1~deb7u3 on Debian wheezy, before 6.0.45+dfsg-1~deb8u1 on Debian jessie, before 6.0.35-1ubuntu3.9 on Ubuntu 12.04 LTS and on Ubuntu 14.04 LTS; the tomcat7 package before 7.0.28-4+deb7u7 on Debian wheezy, before 7.0.56-3+deb8u6 on Debian jessie, before 7.0.52-1ubuntu0.8 on Ubuntu 14.04 LTS, and on Ubuntu 12.04 LTS, 16.04 LTS, and 16.10; and the tomcat8 package before 8.0.14-1+deb8u5 on Debian jessie, before 8.0.32-1ubuntu1.3 on Ubuntu 16.04 LTS, before 8.0.37-1ubuntu0.1 on Ubuntu 16.10, and before 8.0.38-2ubuntu1 on Ubuntu 17.04 might allow local users with access to the tomcat account to gain root privileges via a setgid program in the Catalina directory, as demonstrated by /etc/tomcat8/Catalina/attack.

**参考链接 / References**:
- http://www.debian.org/security/2016/dsa-3738
- http://www.debian.org/security/2016/dsa-3739
- http://www.openwall.com/lists/oss-security/2016/12/02/10
- http://www.openwall.com/lists/oss-security/2016/12/02/5
- http://www.securityfocus.com/bid/94643

---

#### 459. CVE-2017-6964

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
dmcrypt-get-device, as shipped in the eject package of Debian and Ubuntu, does not check the return value of the (1) setuid or (2) setgid function, which might cause dmcrypt-get-device to execute code, which was intended to run as an unprivileged user, as root. This affects eject through 2.1.5+deb1+cvs20081104-13.1 on Debian, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.16.10.1 on Ubuntu 16.10, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.16.04.1 on Ubuntu 16.04 LTS, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.14.04.1 on Ubuntu 14.04 LTS, and eject before 2.1.5+deb1+cvs20081104-9ubuntu0.1 on Ubuntu 12.04 LTS.

**参考链接 / References**:
- http://www.debian.org/security/2017/dsa-3823
- http://www.securityfocus.com/bid/97154
- https://launchpad.net/bugs/1673627
- https://www.ubuntu.com/usn/usn-3246-1/
- https://www.debian.org/security/2017/dsa-3823

---

#### 460. CVE-2016-0727

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The crontab script in the ntp package before 1:4.2.6.p3+dfsg-1ubuntu3.11 on Ubuntu 12.04 LTS, before 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10 on Ubuntu 14.04 LTS, on Ubuntu Wily, and before 1:4.2.8p4+dfsg-3ubuntu5.3 on Ubuntu 16.04 LTS allows local users with access to the ntp account to write to arbitrary files and consequently gain privileges via vectors involving statistics directory cleanup.

**参考链接 / References**:
- http://packetstormsecurity.com/files/141913/NTP-Privilege-Escalation.html
- http://www.securityfocus.com/bid/81552
- http://www.securitytracker.com/id/1034808
- http://www.ubuntu.com/usn/USN-3096-1
- https://bugs.launchpad.net/ubuntu/+source/ntp/+bug/1528050

---

#### 461. CVE-2017-8900

**严重程度 / Severity**: MEDIUM | CVSS: 4.6

**漏洞描述 / Description**:
LightDM through 1.22.0, when systemd is used in Ubuntu 16.10 and 17.x, allows physically proximate attackers to bypass intended AppArmor restrictions and visit the home directories of arbitrary users by establishing a guest session.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98554
- https://launchpad.net/bugs/1663157
- https://people.canonical.com/~ubuntu-security/cve/2017/CVE-2017-8900.html
- https://www.ubuntu.com/usn/usn-3285-1/
- http://www.securityfocus.com/bid/98554

---

#### 462. CVE-2017-9525

**严重程度 / Severity**: MEDIUM | CVSS: 6.7

**漏洞描述 / Description**:
In the cron package through 3.0pl1-128 on Debian, and through 3.0pl1-128ubuntu2 on Ubuntu, the postinst maintainer script allows for group-crontab-to-root privilege escalation via symlink attacks against unsafe usage of the chown and chmod programs.

**参考链接 / References**:
- http://bugs.debian.org/864466
- http://www.openwall.com/lists/oss-security/2017/06/08/3
- http://www.securitytracker.com/id/1038651
- https://lists.debian.org/debian-lts-announce/2019/03/msg00025.html
- https://lists.debian.org/debian-lts-announce/2021/10/msg00029.html

---

#### 463. CVE-2017-10600

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
ubuntu-image 1.0 before 2017-07-07, when invoked as non-root, creates files in the resulting image with the uid of the invoking user. When the resulting image is booted, a local attacker with the same uid as the image creator has unintended access to cloud-init and snapd directories.

**参考链接 / References**:
- https://forum.snapcraft.io/t/ownership-bug-in-ubuntu-image/1285
- https://forum.snapcraft.io/t/ownership-bug-in-ubuntu-image/1285

---

#### 464. CVE-2015-1323

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The simulate dbus method in aptdaemon before 1.1.1+bzr982-0ubuntu3.1 as packaged in Ubuntu 15.04, before 1.1.1+bzr980-0ubuntu1.1 as packaged in Ubuntu 14.10, before 1.1.1-1ubuntu5.2 as packaged in Ubuntu 14.04 LTS, before 0.43+bzr805-0ubuntu10 as packaged in Ubuntu 12.04 LTS allows local users to obtain sensitive information, or access files with root permissions.

**参考链接 / References**:
- http://www.securityfocus.com/bid/75221
- http://www.ubuntu.com/usn/USN-2648-1
- http://www.securityfocus.com/bid/75221
- http://www.ubuntu.com/usn/USN-2648-1

---

#### 465. CVE-2015-1332

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The oxide::JavaScriptDialogManager function in oxide-qt before 1.9.1 as packaged in Ubuntu 15.04 and Ubuntu 14.04 allows remote attackers to cause a denial of service (application crash) or execute arbitrary code via a crafted website.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1332.html
- http://www.securityfocus.com/bid/76710
- http://www.ubuntu.com/usn/USN-2735-1
- https://launchpad.net/ubuntu/+source/oxide-qt/1.9.1-0ubuntu0.15.04.1
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1332.html

---

#### 466. CVE-2015-1324

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Apport before 2.17.2-0ubuntu1.1 as packaged in Ubuntu 15.04, before 2.14.70ubuntu8.5 as packaged in Ubuntu 14.10, before 2.14.1-0ubuntu3.11 as packaged in Ubuntu 14.04 LTS, and before 2.0.1-0ubuntu17.9 as packaged in Ubuntu 12.04 LTS allow local users to write to arbitrary files and gain root privileges by leveraging incorrect handling of permissions when generating core dumps for setuid binaries.

**参考链接 / References**:
- http://www.securityfocus.com/bid/74767
- http://www.ubuntu.com/usn/USN-2609-1
- https://bugs.launchpad.net/ubuntu/+source/apport/+bug/1452239
- http://www.securityfocus.com/bid/74767
- http://www.ubuntu.com/usn/USN-2609-1

---

#### 467. CVE-2015-1325

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Race condition in Apport before 2.17.2-0ubuntu1.1 as packaged in Ubuntu 15.04, before 2.14.70ubuntu8.5 as packaged in Ubuntu 14.10, before 2.14.1-0ubuntu3.11 as packaged in Ubuntu 14.04 LTS, and before 2.0.1-0ubuntu17.9 as packaged in Ubuntu 12.04 LTS allow local users to write to arbitrary files and gain root privileges.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/05/21/10
- http://www.securityfocus.com/bid/74769
- http://www.ubuntu.com/usn/USN-2609-1
- https://www.exploit-db.com/exploits/37088/
- http://seclists.org/fulldisclosure/2025/Jun/9

---

#### 468. CVE-2015-1329

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Use-after-free vulnerability in oxide::qt::URLRequestDelegatedJob in oxide-qt in Ubuntu 15.04 and 14.04 LTS might allow remote attackers to execute arbitrary code.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1329.html
- http://www.securityfocus.com/bid/76174
- http://www.ubuntu.com/usn/USN-2677-1
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1329.html
- http://www.securityfocus.com/bid/76174

---

#### 469. CVE-2014-8156

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The D-Bus security policy files in /etc/dbus-1/system.d/*.conf in fso-gsmd 0.12.0-3, fso-frameworkd 0.9.5.9+git20110512-4, and fso-usaged 0.12.0-2 as packaged in Debian, the upstream cornucopia.git (fsoaudiod, fsodatad, fsodeviced, fsogsmd, fsonetworkd, fsotdld, fsousaged) git master on 2015-01-19, the upstream framework.git 0.10.1 and git master on 2015-01-19, phonefsod 0.1+git20121018-1 as packaged in Debian, Ubuntu and potentially other packages, and potentially other fso modules do not properly filter D-Bus message paths, which might allow local users to cause a denial of service (dbus-daemon memory consumption), or execute arbitrary code as root by sending a crafted D-Bus message to any D-Bus system service.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/01/27/25
- http://www.securityfocus.com/bid/72363
- https://exchange.xforce.ibmcloud.com/vulnerabilities/100488
- http://www.openwall.com/lists/oss-security/2015/01/27/25
- http://www.securityfocus.com/bid/72363

---

#### 470. CVE-2015-1336

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The daily mandb cleanup job in Man-db before 2.7.6.1-1 as packaged in Ubuntu and Debian allows local users with access to the man account to gain privileges via vectors involving insecure chown use.

**参考链接 / References**:
- http://packetstormsecurity.com/files/140759/Man-db-2.6.7.1-Privilege-Escalation.html
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1336.html
- http://www.halfdog.net/Security/2015/MandbSymlinkLocalRootPrivilegeEscalation/
- http://www.openwall.com/lists/oss-security/2015/12/14/11
- http://www.securityfocus.com/bid/79723

---

#### 471. CVE-2015-3643

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
usb-creator before 0.2.38.3ubuntu0.1 on Ubuntu 12.04 LTS, before 0.2.56.3ubuntu0.1 on Ubuntu 14.04 LTS, before 0.2.62ubuntu0.3 on Ubuntu 14.10, and before 0.2.67ubuntu0.1 on Ubuntu 15.04 allows local users to gain privileges by leveraging a missing call check_polkit for the KVMTest method.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/04/22/12
- http://www.openwall.com/lists/oss-security/2015/05/04/3
- http://www.securityfocus.com/bid/74304
- https://bazaar.launchpad.net/~usb-creator-hackers/usb-creator/trunk/revision/470
- https://usn.ubuntu.com/usn/usn-2576-1/

---

#### 472. CVE-2011-2684

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
foo2zjs before 20110722dfsg-3ubuntu1 as packaged in Ubuntu, 20110722dfsg-1 as packaged in Debian unstable, and 20090908dfsg-5.1+squeeze0 as packaged in Debian squeeze create temporary files insecurely, which allows local users to write over arbitrary files via a symlink attack on /tmp/foo2zjs.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2011/07/06/10
- http://www.openwall.com/lists/oss-security/2014/02/08/5
- https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=633870
- https://bugs.launchpad.net/ubuntu/+source/foo2zjs/+bug/805370
- https://security-tracker.debian.org/tracker/CVE-2011-2684/

---

#### 473. CVE-2017-8806

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The Debian pg_ctlcluster, pg_createcluster, and pg_upgradecluster scripts, as distributed in the Debian postgresql-common package before 181+deb9u1 for PostgreSQL (and other packages related to Debian and Ubuntu), handled symbolic links insecurely, which could result in local denial of service by overwriting arbitrary files.

**参考链接 / References**:
- http://metadata.ftp-master.debian.org/changelogs/main/p/postgresql-common/postgresql-common_181+deb9u1_changelog
- http://www.securityfocus.com/bid/101810
- https://usn.ubuntu.com/usn/usn-3476-1/
- https://www.debian.org/security/2017/dsa-4029
- http://metadata.ftp-master.debian.org/changelogs/main/p/postgresql-common/postgresql-common_181+deb9u1_changelog

---

#### 474. CVE-2017-14388

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Cloud Foundry Foundation GrootFS release 0.3.x versions prior to 0.30.0 do not validate DiffIDs, allowing specially crafted images to poison the grootfs volume cache. For example, this could allow an attacker to provide an image layer that GrootFS would consider to be the Ubuntu base layer.

**参考链接 / References**:
- https://www.cloudfoundry.org/cve-2017-14388/
- https://www.cloudfoundry.org/cve-2017-14388/

---

#### 475. CVE-2016-1252

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
The apt package in Debian jessie before 1.0.9.8.4, in Debian unstable before 1.4~beta2, in Ubuntu 14.04 LTS before 1.0.1ubuntu2.17, in Ubuntu 16.04 LTS before 1.2.15ubuntu0.2, and in Ubuntu 16.10 before 1.3.2ubuntu0.1 allows man-in-the-middle attackers to bypass a repository-signing protection mechanism by leveraging improper error handling when validating InRelease file signatures.

**参考链接 / References**:
- http://packetstormsecurity.com/files/140145/apt-Repository-Signing-Bypass.html
- http://www.ubuntu.com/usn/USN-3156-1
- https://bugs.chromium.org/p/project-zero/issues/detail?id=1020
- https://bugs.launchpad.net/ubuntu/+source/apt/+bug/1647467
- https://www.debian.org/security/2016/dsa-3733

---

#### 476. CVE-2016-1255

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The pg_ctlcluster script in postgresql-common package in Debian wheezy before 134wheezy5, in Debian jessie before 165+deb8u2, in Debian unstable before 178, in Ubuntu 12.04 LTS before 129ubuntu1.2, in Ubuntu 14.04 LTS before 154ubuntu1.1, in Ubuntu 16.04 LTS before 173ubuntu0.1, in Ubuntu 17.04 before 179ubuntu0.1, and in Ubuntu 17.10 before 184ubuntu1.1 allows local users to gain root privileges via a symlink attack on a logfile in /var/log/postgresql.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-3476-1
- http://www.ubuntu.com/usn/USN-3476-2
- https://anonscm.debian.org/cgit/pkg-postgresql/postgresql-common.git/commit/?id=c8989206ec360f199400c74f129f7b4cb878c1ee
- https://lists.debian.org/debian-lts-announce/2017/01/msg00002.html
- http://www.ubuntu.com/usn/USN-3476-1

---

#### 477. CVE-2018-1000135

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
GNOME NetworkManager version 1.10.2 and earlier contains a Information Exposure (CWE-200) vulnerability in DNS resolver that can result in Private DNS queries leaked to local network's DNS servers, while on VPN. This vulnerability appears to have been fixed in Some Ubuntu 16.04 packages were fixed, but later updates removed the fix. cf. https://bugs.launchpad.net/ubuntu/+bug/1754671 an upstream fix does not appear to be available at this time.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00005.html
- http://www.securityfocus.com/bid/103478
- https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/1754671
- https://bugzilla.gnome.org/show_bug.cgi?id=746422
- https://bugzilla.redhat.com/show_bug.cgi?id=1553634

---

#### 478. CVE-2018-10768

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
There is a NULL pointer dereference in the AnnotPath::getCoordsLength function in Annot.h in an Ubuntu package for Poppler 0.24.5. A crafted input will lead to a remote denial of service attack. Later Ubuntu packages such as for Poppler 0.41.0 are not affected.

**参考链接 / References**:
- https://access.redhat.com/errata/RHBA-2019:0327
- https://access.redhat.com/errata/RHSA-2018:3140
- https://access.redhat.com/errata/RHSA-2018:3505
- https://bugs.freedesktop.org/show_bug.cgi?id=106408
- https://lists.debian.org/debian-lts-announce/2018/10/msg00024.html

---

#### 479. CVE-2018-4220

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. Swift before 4.1.1 Security Update 2018-001 is affected. The issue involves the "Swift for Ubuntu" component. It allows attackers to execute arbitrary code in a privileged context because write and execute permissions are enabled during library loading.

**参考链接 / References**:
- http://www.securityfocus.com/bid/104085
- https://support.apple.com/HT208804
- http://www.securityfocus.com/bid/104085
- https://support.apple.com/HT208804

---

#### 480. CVE-2018-6553

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The CUPS AppArmor profile incorrectly confined the dnssd backend due to use of hard links. A local attacker could possibly use this issue to escape confinement. This flaw affects versions prior to 2.2.7-1ubuntu2.1 in Ubuntu 18.04 LTS, prior to 2.2.4-7ubuntu3.1 in Ubuntu 17.10, prior to 2.1.3-4ubuntu0.5 in Ubuntu 16.04 LTS, and prior to 1.7.2-0ubuntu1.10 in Ubuntu 14.04 LTS.

**参考链接 / References**:
- https://lists.debian.org/debian-lts-announce/2018/07/msg00014.html
- https://security.gentoo.org/glsa/201908-08
- https://usn.ubuntu.com/usn/usn-3713-1
- https://www.debian.org/security/2018/dsa-4243
- https://lists.debian.org/debian-lts-announce/2018/07/msg00014.html

---

#### 481. CVE-2018-6557

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
The MOTD update script in the base-files package in Ubuntu 18.04 LTS before 10.1ubuntu2.2, and Ubuntu 18.10 before 10.1ubuntu6 incorrectly handled temporary files. A local attacker could use this issue to cause a denial of service, or possibly escalate privileges if kernel symlink restrictions were disabled.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105148
- http://www.securitytracker.com/id/1041530
- https://usn.ubuntu.com/3748-1/
- http://www.securityfocus.com/bid/105148
- http://www.securitytracker.com/id/1041530

---

#### 482. CVE-2018-0643

**严重程度 / Severity**: MEDIUM | CVSS: 6.6

**漏洞描述 / Description**:
Ubuntu14.04 ORCA (Online Receipt Computer Advantage) 4.8.0 (panda-server) 1:1.4.9+p41-u4jma1 and earlier allows attacker with administrator rights to execute arbitrary OS commands via unspecified vectors.

**参考链接 / References**:
- http://jvn.jp/en/jp/JVN37376131/index.html
- https://www.orca.med.or.jp/news/vulnerability_2018-07-18-1.html
- http://jvn.jp/en/jp/JVN37376131/index.html
- https://www.orca.med.or.jp/news/vulnerability_2018-07-18-1.html

---

#### 483. CVE-2018-0644

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Buffer overflow in Ubuntu14.04 ORCA (Online Receipt Computer Advantage) 4.8.0 (panda-client2) 1:1.4.9+p41-u4jma1 and earlier, Ubuntu14.04 ORCA (Online Receipt Computer Advantage) 5.0.0 (panda-client2) 1:2.0.0+p48-u4jma1 and earlier, and Ubuntu16.04 ORCA (Online Receipt Computer Advantage) 5.0.0 (panda-client2) 1:2.0.0+p48-u5jma1 and earlier allows authenticated attackers to cause denial-of-service (DoS) condition via unspecified vectors.

**参考链接 / References**:
- http://jvn.jp/en/jp/JVN37376131/index.html
- https://www.orca.med.or.jp/news/vulnerability_2018-07-18-1.html
- http://jvn.jp/en/jp/JVN37376131/index.html
- https://www.orca.med.or.jp/news/vulnerability_2018-07-18-1.html

---

#### 484. CVE-2018-18653

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The Linux kernel, as used in Ubuntu 18.10 and when booted with UEFI Secure Boot enabled, allows privileged local users to bypass intended Secure Boot restrictions and execute untrusted code by loading arbitrary kernel modules. This occurs because a modified kernel/module.c, in conjunction with certain configuration options, leads to mishandling of the result of signature verification.

**参考链接 / References**:
- https://launchpad.net/bugs/1798863
- https://usn.ubuntu.com/3832-1/
- https://usn.ubuntu.com/3835-1/
- https://launchpad.net/bugs/1798863
- https://usn.ubuntu.com/3832-1/

---

#### 485. CVE-2018-6559

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
The Linux kernel, as used in Ubuntu 18.04 LTS and Ubuntu 18.10, allows local users to obtain names of files in which they would not normally be able to access via an overlayfs mount inside of a user namespace.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105752
- https://launchpad.net/bugs/1793458
- https://lists.ubuntu.com/archives/kernel-team/2018-October/096172.html
- https://people.canonical.com/~ubuntu-security/cve/2018/CVE-2018-6559.html
- https://usn.ubuntu.com/3832-1/

---

#### 486. CVE-2018-19518

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
University of Washington IMAP Toolkit 2007f on UNIX, as used in imap_open() in PHP and other products, launches an rsh command (by means of the imap_rimap function in c-client/imap4r1.c and the tcp_aopen function in osdep/unix/tcp_unix.c) without preventing argument injection, which might allow remote attackers to execute arbitrary OS commands if the IMAP server name is untrusted input (e.g., entered by a user of a web application) and if rsh has been replaced by a program with different argument semantics. For example, if rsh is a link to ssh (as seen on Debian and Ubuntu systems), then the attack can use an IMAP server name containing a "-oProxyCommand" argument.

**参考链接 / References**:
- http://www.securityfocus.com/bid/106018
- http://www.securitytracker.com/id/1042157
- https://antichat.com/threads/463395/#post-4254681
- https://bugs.debian.org/913775
- https://bugs.debian.org/913835

---

#### 487. CVE-2017-12447

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
GdkPixBuf (aka gdk-pixbuf), possibly 2.32.2, as used by GNOME Nautilus 3.14.3 on Ubuntu 16.04, allows attackers to cause a denial of service (stack corruption) or possibly have unspecified other impact via a crafted file folder.

**参考链接 / References**:
- https://bugzilla.gnome.org/show_bug.cgi?id=785979
- https://github.com/hackerlib/hackerlib-vul/tree/master/gnome
- https://usn.ubuntu.com/3912-1/
- https://bugzilla.gnome.org/show_bug.cgi?id=785979
- https://github.com/hackerlib/hackerlib-vul/tree/master/gnome

---

#### 488. CVE-2018-3979

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
A remote denial-of-service vulnerability exists in the way the Nouveau Display Driver (the default Ubuntu Nvidia display driver) handles GPU shader execution. A specially crafted pixel shader can cause remote denial-of-service issues. An attacker can provide a specially crafted website to trigger this vulnerability. This vulnerability can be triggered remotely after the user visits a malformed website. No further user interaction is required. Vulnerable versions include Ubuntu 18.04 LTS (linux 4.15.0-29-generic x86_64), Nouveau Display Driver NV117 (vermagic: 4.15.0-29-generic SMP mod_unload).

**参考链接 / References**:
- https://talosintelligence.com/vulnerability_reports/TALOS-2018-0647
- https://talosintelligence.com/vulnerability_reports/TALOS-2018-0647

---

#### 489. CVE-2011-3151

**严重程度 / Severity**: MEDIUM | CVSS: 5.2

**漏洞描述 / Description**:
The Ubuntu SELinux initscript before version 1:0.10 used touch to create a lockfile in a world-writable directory. If the OS kernel does not have symlink protections then an attacker can cause a zero byte file to be allocated on any writable filesystem.

**参考链接 / References**:
- https://launchpadlibrarian.net/88098106/selinux_0.10~10.04.1.debdiff
- https://launchpadlibrarian.net/88098106/selinux_0.10~10.04.1.debdiff

---

#### 490. CVE-2014-1426

**严重程度 / Severity**: HIGH | CVSS: 8.6

**漏洞描述 / Description**:
A vulnerability in maasserver.api.get_file_by_name of Ubuntu MAAS allows unauthenticated network clients to download any file. This issue affects: Ubuntu MAAS versions prior to 1.9.2.

**参考链接 / References**:
- https://launchpad.net/maas/+milestone/1.9.2
- https://launchpad.net/maas/+milestone/1.9.2

---

#### 491. CVE-2014-1427

**严重程度 / Severity**: CRITICAL | CVSS: 9.6

**漏洞描述 / Description**:
A vulnerability in the REST API of Ubuntu MAAS allows an attacker to cause a logged-in user to execute commands via cross-site scripting. This issue affects MAAS versions prior to 1.9.2.

**参考链接 / References**:
- https://launchpad.net/maas/+milestone/1.9.2
- https://launchpad.net/maas/+milestone/1.9.2

---

#### 492. CVE-2014-1428

**严重程度 / Severity**: LOW | CVSS: 2.0

**漏洞描述 / Description**:
A vulnerability in generate_filestorage_key of Ubuntu MAAS allows an attacker to brute-force filenames. This issue affects Ubuntu MAAS versions prior to 1.9.2.

**参考链接 / References**:
- https://launchpad.net/maas/+milestone/1.9.2
- https://launchpad.net/maas/+milestone/1.9.2

---

#### 493. CVE-2015-1320

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The SeaMicro provisioning of Ubuntu MAAS logs credentials, including username and password, for the management interface. This issue affects Ubuntu MAAS versions prior to 1.9.2.

**参考链接 / References**:
- https://launchpad.net/maas/+milestone/1.9.2
- https://launchpad.net/maas/+milestone/1.9.2

---

#### 494. CVE-2018-6634

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
A vulnerability in Parsec Windows 142-0 and Parsec 'Linux Ubuntu 16.04 LTS Desktop' Build 142-1 allows unauthorized users to maintain access to an account.

**参考链接 / References**:
- https://twitter.com/VixusFoxy/status/1125697484498583553
- https://twitter.com/VixusFoxy/status/1125697484498583553

---

#### 495. CVE-2019-12301

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The Percona Server 5.6.44-85.0-1 packages for Debian and Ubuntu suffered an issue where the server would reset the root password to a blank value upon an upgrade. This was fixed in 5.6.44-85.0-2.

**参考链接 / References**:
- https://jira.percona.com/browse/PS-5640
- https://www.percona.com/blog/2019/05/17/percona-server-for-mysql-5-6-44-85-0-is-now-available/
- https://jira.percona.com/browse/PS-5640
- https://www.percona.com/blog/2019/05/17/percona-server-for-mysql-5-6-44-85-0-is-now-available/

---

#### 496. CVE-2019-12749

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
dbus before 1.10.28, 1.12.x before 1.12.16, and 1.13.x before 1.13.12, as used in DBusServer in Canonical Upstart in Ubuntu 14.04 (and in some, less common, uses of dbus-daemon), allows cookie spoofing because of symlink mishandling in the reference implementation of DBUS_COOKIE_SHA1 in the libdbus library. (This only affects the DBUS_COOKIE_SHA1 authentication mechanism.) A malicious client with write access to its own home directory could manipulate a ~/.dbus-keyrings symlink to cause a DBusServer with a different uid to read and write in unintended locations. In the worst case, this could result in the DBusServer reusing a cookie that is known to the malicious client, and treating that cookie as evidence that a subsequent client connection came from an attacker-chosen uid, allowing authentication bypass.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00059.html
- http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00092.html
- http://lists.opensuse.org/opensuse-security-announce/2019-07/msg00026.html
- http://www.openwall.com/lists/oss-security/2019/06/11/2
- http://www.securityfocus.com/bid/108751

---

#### 497. CVE-2019-12881

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
i915_gem_userptr_get_pages in drivers/gpu/drm/i915/i915_gem_userptr.c in the Linux kernel 4.15.0 on Ubuntu 18.04.2 allows local users to cause a denial of service (NULL pointer dereference and BUG) or possibly have unspecified other impact via crafted ioctl calls to /dev/dri/card0.

**参考链接 / References**:
- http://www.securityfocus.com/bid/108873
- https://gist.github.com/oxagast/472866fb2c3d439e10499d7141d0a520
- https://security.netapp.com/advisory/ntap-20190710-0002/
- http://www.securityfocus.com/bid/108873
- https://gist.github.com/oxagast/472866fb2c3d439e10499d7141d0a520

---

#### 498. CVE-2019-12164

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
ubuntu-server.js in Status React Native Desktop before v0.57.8_mobile_ui allows Remote Code Execution.

**参考链接 / References**:
- https://github.com/status-im/react-native-desktop/compare/e77167f...7477eef
- https://github.com/status-im/react-native-desktop/pull/475
- https://github.com/status-im/react-native-desktop/pull/475/commits/f6945f1e4b157c69e414cd94fe5cde1876aabcc1
- https://github.com/status-im/react-native-desktop/compare/e77167f...7477eef
- https://github.com/status-im/react-native-desktop/pull/475

---

#### 499. CVE-2012-2092

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
A Security Bypass vulnerability exists in Ubuntu Cobbler before 2,2,2 in the cobbler-ubuntu-import script due to an error when verifying the GPG signature.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2012/04/10/14
- http://www.securityfocus.com/bid/52971
- https://exchange.xforce.ibmcloud.com/vulnerabilities/74789
- https://security-tracker.debian.org/tracker/CVE-2012-2092
- http://www.openwall.com/lists/oss-security/2012/04/10/14

---

#### 500. CVE-2019-19141

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The Camera Upload functionality in Plex Media Server through 1.18.2.2029 allows remote authenticated users to write files anywhere the user account running the Plex Media Server has permissions. This allows remote code execution via a variety of methods, such as (on a default Ubuntu installation) creating a .ssh folder in the plex user's home directory via directory traversal, uploading an SSH authorized_keys file there, and logging into the host as the Plex user via SSH.

**参考链接 / References**:
- https://forums.plex.tv/t/security-camera-upload/507289
- https://forums.plex.tv/t/security-camera-upload/507289

---

#### 501. CVE-2019-19927

**严重程度 / Severity**: MEDIUM | CVSS: 6.0

**漏洞描述 / Description**:
In the Linux kernel 5.0.0-rc7 (as distributed in ubuntu/linux.git on kernel.ubuntu.com), mounting a crafted f2fs filesystem image and performing some operations can lead to slab-out-of-bounds read access in ttm_put_pages in drivers/gpu/drm/ttm/ttm_page_alloc.c. This is related to the vmwgfx or ttm module.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2020-03/msg00021.html
- https://github.com/bobfuzzer/CVE/tree/master/CVE-2019-19927
- https://github.com/torvalds/linux/commit/453393369dc9806d2455151e329c599684762428
- https://github.com/torvalds/linux/commit/a66477b0efe511d98dde3e4aaeb189790e6f0a39
- https://github.com/torvalds/linux/commit/ac1e516d5a4c56bf0cb4a3dfc0672f689131cfd4

---

#### 502. CVE-2012-0055

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
OverlayFS in the Linux kernel before 3.0.0-16.28, as used in Ubuntu 10.0.4 LTS and 11.10, is missing inode security checks which could allow attackers to bypass security restrictions and perform unauthorized actions.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2012/01/17/11
- http://www.ubuntu.com/usn/USN-1363-1
- http://www.ubuntu.com/usn/USN-1364-1
- http://www.ubuntu.com/usn/USN-1384-1
- https://access.redhat.com/security/cve/cve-2012-0055

---

#### 503. CVE-2019-7305

**严重程度 / Severity**: MEDIUM | CVSS: 5.8

**漏洞描述 / Description**:
Information Exposure vulnerability in eXtplorer makes the /usr/ and /etc/extplorer/ system directories world-accessible over HTTP. Introduced in the Makefile patch file debian/patches/debian-changes-2.1.0b6+dfsg-1 or debian/patches/adds-a-makefile.patch, this can lead to data leakage, information disclosure and potentially remote code execution on the web server. This issue affects all versions of eXtplorer in Ubuntu and Debian

**参考链接 / References**:
- https://launchpad.net/bugs/1822013
- https://launchpad.net/bugs/1822013

---

#### 504. CVE-2020-8832

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The fix for the Linux kernel in Ubuntu 18.04 LTS for CVE-2019-14615 ("The Linux kernel did not properly clear data structures on context switches for certain Intel graphics processors.") was discovered to be incomplete, meaning that in versions of the kernel before 4.15.0-91.92, an attacker could use this vulnerability to expose sensitive information.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1862840
- https://security.netapp.com/advisory/ntap-20200430-0004/
- https://usn.ubuntu.com/usn/usn-4302-1
- https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1862840
- https://security.netapp.com/advisory/ntap-20200430-0004/

---

#### 505. CVE-2019-11480

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
The pc-kernel snap build process hardcoded the --allow-insecure-repositories and --allow-unauthenticated apt options when creating the build chroot environment. This could allow an attacker who is able to perform a MITM attack between the build environment and the Ubuntu archive to install a malicious package within the build chroot. This issue affects pc-kernel versions prior to and including 2019-07-16

**参考链接 / References**:
- https://bugs.launchpad.net/bugs/1836041
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11480
- https://bugs.launchpad.net/bugs/1836041
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11480

---

#### 506. CVE-2019-15791

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
In shiftfs, a non-upstream patch to the Linux kernel included in the Ubuntu 5.0 and 5.3 kernel series, shiftfs_btrfs_ioctl_fd_replace() installs an fd referencing a file from the lower filesystem without taking an additional reference to that file. After the btrfs ioctl completes this fd is closed, which then puts a reference to that file, leading to a refcount underflow.

**参考链接 / References**:
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=601a64857b3d7040ca15c39c929e6b9db3373ec1
- https://usn.ubuntu.com/usn/usn-4183-1
- https://usn.ubuntu.com/usn/usn-4184-1
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=601a64857b3d7040ca15c39c929e6b9db3373ec1
- https://usn.ubuntu.com/usn/usn-4183-1

---

#### 507. CVE-2019-15792

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
In shiftfs, a non-upstream patch to the Linux kernel included in the Ubuntu 5.0 and 5.3 kernel series, shiftfs_btrfs_ioctl_fd_replace() calls fdget(oldfd), then without further checks passes the resulting file* into shiftfs_real_fdget(), which casts file->private_data, a void* that points to a filesystem-dependent type, to a "struct shiftfs_file_info *". As the private_data is not required to be a pointer, an attacker can use this to cause a denial of service or possibly execute arbitrary code.

**参考链接 / References**:
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=5df147c8140efc71ac0879ae3b0057f577226d4c
- https://usn.ubuntu.com/usn/usn-4183-1
- https://usn.ubuntu.com/usn/usn-4184-1
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=5df147c8140efc71ac0879ae3b0057f577226d4c
- https://usn.ubuntu.com/usn/usn-4183-1

---

#### 508. CVE-2019-15793

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
In shiftfs, a non-upstream patch to the Linux kernel included in the Ubuntu 5.0 and 5.3 kernel series, several locations which shift ids translate user/group ids before performing operations in the lower filesystem were translating them into init_user_ns, whereas they should have been translated into the s_user_ns for the lower filesystem. This resulted in using ids other than the intended ones in the lower fs, which likely did not map into the shifts s_user_ns. A local attacker could use this to possibly bypass discretionary access control permissions.

**参考链接 / References**:
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=3644b9d5688da86f18e017c9c580b75cf52927bb
- https://usn.ubuntu.com/usn/usn-4183-1
- https://usn.ubuntu.com/usn/usn-4184-1
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=3644b9d5688da86f18e017c9c580b75cf52927bb
- https://usn.ubuntu.com/usn/usn-4183-1

---

#### 509. CVE-2019-15794

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
Overlayfs in the Linux kernel and shiftfs, a non-upstream patch to the Linux kernel included in the Ubuntu 5.0 and 5.3 kernel series, both replace vma->vm_file in their mmap handlers. On error the original value is not restored, and the reference is put for the file to which vm_file points. On upstream kernels this is not an issue, as no callers dereference vm_file following after call_mmap() returns an error. However, the aufs patchs change mmap_region() to replace the fput() using a local variable with vma_fput(), which will fput() vm_file, leading to a refcount underflow.

**参考链接 / References**:
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=270d16ae48a4dbf1c7e25e94cc3e38b4bea37635
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=ef81780548d20a786cc77ed4203fca146fd81ce3
- https://usn.ubuntu.com/usn/usn-4208-1
- https://usn.ubuntu.com/usn/usn-4209-1
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/eoan/commit/?id=270d16ae48a4dbf1c7e25e94cc3e38b4bea37635

---

#### 510. CVE-2014-1423

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
signond before 8.57+15.04.20141127.1-0ubuntu1, as used in Ubuntu Touch, did not properly restrict applications from querying oath tokens due to incorrect checks and the missing installation of the signon-apparmor-extension. An attacker could use this create a malicious click app that collects oauth tokens for other applications, exposing sensitive information.

**参考链接 / References**:
- http://bazaar.launchpad.net/~online-accounts/signon/upstream/revision/644
- http://bazaar.launchpad.net/~online-accounts/signon/upstream/revision/645
- https://bugs.launchpad.net/ubuntu/+source/signon/+bug/1392380
- http://bazaar.launchpad.net/~online-accounts/signon/upstream/revision/644
- http://bazaar.launchpad.net/~online-accounts/signon/upstream/revision/645

---

#### 511. CVE-2015-7946

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
Information Exposure vulnerability in Unity8 as used on the Ubuntu phone and possibly also in Unity8 shipped elsewhere. This allows an attacker to enable the MTP service by opening the emergency dialer. Fixed in 8.11+16.04.20160111.1-0ubuntu1 and 8.11+15.04.20160122-0ubuntu1.

**参考链接 / References**:
- https://launchpad.net/bugs/1525981
- https://launchpad.net/bugs/1525981

---

#### 512. CVE-2020-11932

**严重程度 / Severity**: LOW | CVSS: 2.3

**漏洞描述 / Description**:
It was discovered that the Subiquity installer for Ubuntu Server logged the LUKS full disk encryption password if one was entered.

**参考链接 / References**:
- https://aliceandbob.company/the-human-factor-in-an-economy-of-scale/
- https://github.com/CanonicalLtd/subiquity/commit/7db70650feaf513d7fb6f1ca07f2d670a0890613
- https://aliceandbob.company/the-human-factor-in-an-economy-of-scale/
- https://github.com/CanonicalLtd/subiquity/commit/7db70650feaf513d7fb6f1ca07f2d670a0890613

---

#### 513. CVE-2020-11931

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An Ubuntu-specific modification to Pulseaudio to provide security mediation for Snap-packaged applications was found to have a bypass of intended access restriction for snaps which plugs any of pulseaudio, audio-playback or audio-record via unloading the pulseaudio snap policy module. This issue affects: pulseaudio 1:8.0 versions prior to 1:8.0-0ubuntu3.12; 1:11.1 versions prior to 1:11.1-1ubuntu7.7; 1:13.0 versions prior to 1:13.0-1ubuntu1.2; 1:13.99.1 versions prior to 1:13.99.1-1ubuntu3.2;

**参考链接 / References**:
- https://forum.snapcraft.io/t/audio-switcher-pulseaudio-interface-auto-connect-request/16648/3
- https://usn.ubuntu.com/4355-1/
- https://forum.snapcraft.io/t/audio-switcher-pulseaudio-interface-auto-connect-request/16648/3
- https://usn.ubuntu.com/4355-1/

---

#### 514. CVE-2020-10279

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
MiR robot controllers (central computation unit) makes use of Ubuntu 16.04.2 an operating system, Thought for desktop uses, this operating system presents insecure defaults for robots. These insecurities include a way for users to escalate their access beyond what they were granted via file creation, access race conditions, insecure home directory configurations and defaults that facilitate Denial of Service (DoS) attacks.

**参考链接 / References**:
- https://github.com/aliasrobotics/RVD/issues/2569
- https://github.com/aliasrobotics/RVD/issues/2569

---

#### 515. CVE-2014-1422

**严重程度 / Severity**: MEDIUM | CVSS: 5.0

**漏洞描述 / Description**:
In Ubuntu's trust-store, if a user revokes location access from an application, the location is still available to the application because the application will honour incorrect, cached permissions. This is because the cache was not ordered by creation time by the Select struct in src/core/trust/impl/sqlite3/store.cpp. Fixed in trust-store (Ubuntu) version 1.1.0+15.04.20150123-0ubuntu1 and trust-store (Ubuntu RTM) version 1.1.0+15.04.20150123~rtm-0ubuntu1.

**参考链接 / References**:
- https://bazaar.launchpad.net/~phablet-team/trust-store/trunk/revision/82
- https://launchpad.net/bugs/1387734
- https://bazaar.launchpad.net/~phablet-team/trust-store/trunk/revision/82
- https://launchpad.net/bugs/1387734

---

#### 516. CVE-2020-11933

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
cloud-init as managed by snapd on Ubuntu Core 16 and Ubuntu Core 18 devices was run without restrictions on every boot, which a physical attacker could exploit by crafting cloud-init user-data/meta-data via external media to perform arbitrary changes on the device to bypass intended security mechanisms such as full disk encryption. This issue did not affect traditional Ubuntu systems. Fixed in snapd version 2.45.2, revision 8539 and core version 2.45.2, revision 9659.

**参考链接 / References**:
- https://launchpad.net/bugs/1879530
- https://ubuntu.com/USN-4424-1
- https://launchpad.net/bugs/1879530
- https://ubuntu.com/USN-4424-1

---

#### 517. CVE-2020-11934

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
It was discovered that snapctl user-open allowed altering the $XDG_DATA_DIRS environment variable when calling the system xdg-open. OpenURL() in usersession/userd/launcher.go would alter $XDG_DATA_DIRS to append a path to a directory controlled by the calling snap. A malicious snap could exploit this to bypass intended access restrictions to control how the host system xdg-open script opens the URL and, for example, execute a script shipped with the snap without confinement. This issue did not affect Ubuntu Core systems. Fixed in snapd versions 2.45.1ubuntu0.2, 2.45.1+18.04.2 and 2.45.1+20.04.2.

**参考链接 / References**:
- https://launchpad.net/bugs/1880085
- https://ubuntu.com/USN-4424-1
- https://launchpad.net/bugs/1880085
- https://ubuntu.com/USN-4424-1

---

#### 518. CVE-2020-15707

**严重程度 / Severity**: MEDIUM | CVSS: 5.7

**漏洞描述 / Description**:
Integer overflows were discovered in the functions grub_cmd_initrd and grub_initrd_init in the efilinux component of GRUB2, as shipped in Debian, Red Hat, and Ubuntu (the functionality is not included in GRUB2 upstream), leading to a heap-based buffer overflow. These could be triggered by an extremely large number of arguments to the initrd command on 32-bit architectures, or a crafted filesystem with very large files on any architecture. An attacker could use this to execute arbitrary code and bypass UEFI Secure Boot restrictions. This issue affects GRUB2 version 2.04 and prior versions.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2020-08/msg00016.html
- http://lists.opensuse.org/opensuse-security-announce/2020-08/msg00017.html
- http://ubuntu.com/security/notices/USN-4432-1
- http://www.openwall.com/lists/oss-security/2020/07/29/3
- https://access.redhat.com/security/vulnerabilities/grub2bootloader

---

#### 519. CVE-2014-1420

**严重程度 / Severity**: LOW | CVSS: 3.8

**漏洞描述 / Description**:
On desktop, Ubuntu UI Toolkit's StateSaver would serialise data on tmp/ files which an attacker could use to expose potentially sensitive data. StateSaver would also open files without the O_EXCL flag. An attacker could exploit this to launch a symlink attack, though this is partially mitigated by symlink and hardlink restrictions in Ubuntu. Fixed in 1.1.1188+14.10.20140813.4-0ubuntu1.

**参考链接 / References**:
- http://bazaar.launchpad.net/~ubuntu-sdk-team/ubuntu-ui-toolkit/staging/revision/1182
- https://launchpad.net/bugs/1348241
- http://bazaar.launchpad.net/~ubuntu-sdk-team/ubuntu-ui-toolkit/staging/revision/1182
- https://launchpad.net/bugs/1348241

---

#### 520. CVE-2019-8790

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
This issue was addresses by updating incorrect URLSession file descriptors management logic to match Swift 5.0. This issue is fixed in Swift 5.1.1 for Ubuntu. Incorrect management of file descriptors in URLSession could lead to inadvertent data disclosure.

**参考链接 / References**:
- https://support.apple.com/en-us/HT210647
- https://support.apple.com/en-us/HT210647

---

#### 521. CVE-2020-15708

**严重程度 / Severity**: CRITICAL | CVSS: 9.3

**漏洞描述 / Description**:
Ubuntu's packaging of libvirt in 20.04 LTS created a control socket with world read and write permissions. An attacker could use this to overwrite arbitrary files or execute arbitrary code.

**参考链接 / References**:
- https://usn.ubuntu.com/usn/usn-4452-1
- https://usn.ubuntu.com/usn/usn-4452-1

---

#### 522. CVE-2020-16125

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
gdm3 versions before 3.36.2 or 3.38.2 would start gnome-initial-setup if gdm3 can't contact the accountservice service via dbus in a timely manner; on Ubuntu (and potentially derivatives) this could be be chained with an additional issue that could allow a local user to create a new privileged account.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/1900314
- https://gitlab.gnome.org/GNOME/gdm/-/issues/642
- https://securitylab.github.com/advisories/GHSL-2020-202-gdm3-LPE-unresponsive-accounts-daemon
- https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/1900314
- https://gitlab.gnome.org/GNOME/gdm/-/issues/642

---

#### 523. CVE-2020-16126

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
An Ubuntu-specific modification to AccountsService in versions before 0.6.55-0ubuntu13.2, among other earlier versions, improperly dropped the ruid, allowing untrusted users to send signals to AccountService, thus stopping it from handling D-Bus messages in a timely fashion.

**参考链接 / References**:
- https://securitylab.github.com/advisories/GHSL-2020-187-accountsservice-drop-privs-DOS
- https://securitylab.github.com/advisories/GHSL-2020-187-accountsservice-drop-privs-DOS

---

#### 524. CVE-2020-16127

**严重程度 / Severity**: LOW | CVSS: 2.8

**漏洞描述 / Description**:
An Ubuntu-specific modification to AccountsService in versions before 0.6.55-0ubuntu13.2, among other earlier versions, would perform unbounded read operations on user-controlled ~/.pam_environment files, allowing an infinite loop if /dev/zero is symlinked to this location.

**参考链接 / References**:
- https://securitylab.github.com/advisories/GHSL-2020-187-accountsservice-drop-privs-DOS
- https://securitylab.github.com/advisories/GHSL-2020-187-accountsservice-drop-privs-DOS

---

#### 525. CVE-2020-16123

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
An Ubuntu-specific patch in PulseAudio created a race condition where the snap policy module would fail to identify a client connection from a snap as coming from a snap if SCM_CREDENTIALS were missing, allowing the snap to connect to PulseAudio without proper confinement. This could be exploited by an attacker to expose sensitive information. Fixed in 1:13.99.3-1ubuntu2, 1:13.99.2-1ubuntu2.1, 1:13.99.1-1ubuntu3.8, 1:11.1-1ubuntu7.11, and 1:8.0-0ubuntu3.15.

**参考链接 / References**:
- https://launchpad.net/bugs/1895928
- https://ubuntu.com/USN-4640-1
- https://launchpad.net/bugs/1895928
- https://ubuntu.com/USN-4640-1

---

#### 526. CVE-2020-16119

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
Use-after-free vulnerability in the Linux kernel exploitable by a local attacker due to reuse of a DCCP socket with an attached dccps_hc_tx_ccid object as a listener after being released. Fixed in Ubuntu Linux kernel 5.4.0-51.56, 5.3.0-68.63, 4.15.0-121.123, 4.4.0-193.224, 3.13.0.182.191 and 3.2.0-149.196.

**参考链接 / References**:
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/focal/commit/?id=01872cb896c76cedeabe93a08456976ab55ad695
- https://launchpad.net/bugs/1883840
- https://lists.debian.org/debian-lts-announce/2021/10/msg00010.html
- https://lists.debian.org/debian-lts-announce/2021/12/msg00012.html
- https://lore.kernel.org/netdev/20201013171849.236025-1-kleber.souza%40canonical.com/T/

---

#### 527. CVE-2021-3492

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Shiftfs, an out-of-tree stacking file system included in Ubuntu Linux kernels, did not properly handle faults occurring during copy_from_user() correctly. These could lead to either a double-free situation or memory not being freed at all. An attacker could use this to cause a denial of service (kernel memory exhaustion) or gain privileges via executing arbitrary code. AKA ZDI-CAN-13562.

**参考链接 / References**:
- http://packetstormsecurity.com/files/162614/Kernel-Live-Patch-Security-Notice-LSN-0077-1.html
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/focal/commit/?id=25c891a949bf918b59cbc6e4932015ba4c35c333
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/focal/commit/?id=8fee52ab9da87d82bc6de9ebb3480fff9b4d53e6
- https://ubuntu.com/security/notices/USN-4917-1
- https://www.openwall.com/lists/oss-security/2021/04/16/2

---

#### 528. CVE-2021-3493

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The overlayfs implementation in the linux kernel did not properly validate with respect to user namespaces the setting of file capabilities on files in an underlying file system. Due to the combination of unprivileged user namespaces along with a patch carried in the Ubuntu kernel to allow unprivileged overlay mounts, an attacker could use this to gain elevated privileges.

**参考链接 / References**:
- http://packetstormsecurity.com/files/162434/Kernel-Live-Patch-Security-Notice-LSN-0076-1.html
- http://packetstormsecurity.com/files/162866/Ubuntu-OverlayFS-Local-Privilege-Escalation.html
- http://packetstormsecurity.com/files/165151/Ubuntu-Overlayfs-Local-Privilege-Escalation.html
- https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7c03e2cda4a584cadc398e8f6641ca9988a39d52
- https://ubuntu.com/security/notices/USN-4917-1

---

#### 529. CVE-1999-1390

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
suidexec in suidmanager 0.18 on Debian 2.0 allows local users to gain root privileges by specifying a malicious program on the command line.

**参考链接 / References**:
- http://darwin.bio.uci.edu/~mcoogan/bugtraq/msg00890.html
- http://www.securityfocus.com/bid/94
- http://darwin.bio.uci.edu/~mcoogan/bugtraq/msg00890.html
- http://www.securityfocus.com/bid/94

---

#### 530. CVE-1999-1411

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The installation of the fsp package 2.71-10 in Debian GNU/Linux 2.0 adds the anonymous FTP user without notifying the administrator, which could automatically enable anonymous FTP on some servers such as wu-ftp.

**参考链接 / References**:
- http://lists.debian.org/debian-security-announce/debian-security-announce-1998/msg00033.html
- http://marc.info/?l=bugtraq&m=91228908407679&w=2
- http://marc.info/?l=bugtraq&m=91244712808780&w=2
- http://marc.info/?l=bugtraq&m=91936850009861&w=2
- http://www.iss.net/security_center/static/7574.php

---

#### 531. CVE-1999-0914

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the FTP client in the Debian GNU/Linux netstd package.

**参考链接 / References**:
- http://www.securityfocus.com/bid/324
- http://www.securityfocus.com/bid/324

---

#### 532. CVE-1999-0678

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A default configuration of Apache on Debian GNU/Linux sets the ServerRoot to /usr/doc, which allows remote users to read documentation files for the entire server.

**参考链接 / References**:
- http://www.securityfocus.com/bid/318
- http://www.securityfocus.com/bid/318

---

#### 533. CVE-1999-0373

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the "Super" utility in Debian GNU/Linux, and other operating systems, allows local users to execute commands as root.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0373
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0373

---

#### 534. CVE-1999-0374

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Debian GNU/Linux cfengine package is susceptible to a symlink attack.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0374
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0374

---

#### 535. CVE-2000-0367

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Vulnerability in eterm 0.8.8 in Debian GNU/Linux allows an attacker to gain root privileges.

**参考链接 / References**:
- http://www.debian.org/security/1999/19990218
- http://www.debian.org/security/1999/19990218

---

#### 536. CVE-1999-0730

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The zsoelim program in the Debian man-db package allows local users to overwrite files via a symlink attack.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0730
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0730

---

#### 537. CVE-1999-0742

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Debian mailman package uses weak authentication, which allows attackers to gain privileges.

**参考链接 / References**:
- http://www.securityfocus.com/bid/480
- http://www.securityfocus.com/bid/480

---

#### 538. CVE-1999-0732

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The logging facility of the Debian smtp-refuser package allows local users to delete arbitrary files using symbolic links.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0732
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0732

---

#### 539. CVE-1999-0939

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Debian IRC Epic/epic4 client via a long string.

**参考链接 / References**:
- http://www.securityfocus.com/bid/605
- http://www.securityfocus.com/bid/605

---

#### 540. CVE-2000-0366

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dump in Debian GNU/Linux 2.1 does not properly restore symlinks, which allows a local user to modify the ownership of arbitrary files.

**参考链接 / References**:
- http://www.debian.org/security/1999/19991202
- http://www.securityfocus.com/bid/1442
- http://www.debian.org/security/1999/19991202
- http://www.securityfocus.com/bid/1442

---

#### 541. CVE-2000-0076

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
nviboot boot script in the Debian nvi package allows local users to delete files via malformed entries in vi.recover.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94709988232618&w=2
- http://www.securityfocus.com/bid/1439
- http://marc.info/?l=bugtraq&m=94709988232618&w=2
- http://www.securityfocus.com/bid/1439

---

#### 542. CVE-2000-0112

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default installation of Debian GNU/Linux uses an insecure Master Boot Record (MBR) which allows a local user to boot from a floppy disk during the installation.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94973075614088&w=2
- http://www.securityfocus.com/bid/960
- http://marc.info/?l=bugtraq&m=94973075614088&w=2
- http://www.securityfocus.com/bid/960

---

#### 543. CVE-2000-0145

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The libguile.so library file used by gnucash in Debian GNU/Linux is installed with world-writable permissions.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0145
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0145

---

#### 544. CVE-2000-1135

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
fshd (fsh daemon) in Debian GNU/Linux allows local users to overwrite files of other users via a symlink attack.

**参考链接 / References**:
- http://www.debian.org/security/2000/20001130
- http://www.osvdb.org/7208
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5633
- http://www.debian.org/security/2000/20001130
- http://www.osvdb.org/7208

---

#### 545. CVE-2001-0069

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dialog before 0.9a-20000118-3bis in Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack.

**参考链接 / References**:
- http://www.debian.org/security/2000/20001225
- http://www.securityfocus.com/bid/2151
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5809
- http://www.debian.org/security/2000/20001225
- http://www.securityfocus.com/bid/2151

---

#### 546. CVE-2001-0195

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
sash before 3.4-4 in Debian GNU/Linux does not properly clone /etc/shadow, which makes it world-readable and could allow local users to gain privileges via password cracking.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5994
- http://www.debian.org/security/2001/dsa-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5994

---

#### 547. CVE-2001-0456

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
postinst installation script for Proftpd in Debian 2.2 does not properly change the "run as uid/gid root" configuration when the user enables anonymous access, which causes the server to run at a higher privilege than intended.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6208
- http://www.debian.org/security/2001/dsa-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6208

---

#### 548. CVE-2001-0690

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Format string vulnerability in exim (3.22-10 in Red Hat, 3.12 in Debian and 3.16 in Conectiva) in batched SMTP mode allows a remote attacker to execute arbitrary code via format strings in SMTP mail headers.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-06/0041.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000402
- http://www.debian.org/security/2001/dsa-058
- http://www.redhat.com/support/errata/RHSA-2001-078.html
- http://www.securityfocus.com/bid/2828

---

#### 549. CVE-2001-0755

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in ftp daemon (ftpd) 6.2 in Debian GNU/Linux allows attackers to cause a denial of service and possibly execute arbitrary code via a long SITE command.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0188.html
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0188.html

---

#### 550. CVE-2002-0660

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in libpng 1.0.12-3.woody.2 and libpng3 1.2.1-1.1.woody.2 on Debian GNU/Linux 3.0, and other operating systems, may allow attackers to cause a denial of service and possibly execute arbitrary code, a different vulnerability than CVE-2002-0728.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2002-151.html
- http://rhn.redhat.com/errata/RHSA-2002-152.html
- https://www.debian.org/security/2002/dsa-140
- http://rhn.redhat.com/errata/RHSA-2002-151.html
- http://rhn.redhat.com/errata/RHSA-2002-152.html

---

#### 551. CVE-2002-0912

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
in.uucpd UUCP server in Debian GNU/Linux 2.2, and possibly other operating systems, does not properly terminate long strings, which allows remote attackers to cause a denial of service, possibly due to a buffer overflow.

**参考链接 / References**:
- http://www.debian.org/security/2002/dsa-129
- http://www.iss.net/security_center/static/9230.php
- http://www.securityfocus.com/bid/4910
- http://www.debian.org/security/2002/dsa-129
- http://www.iss.net/security_center/static/9230.php

---

#### 552. CVE-2002-1233

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
A regression error in the Debian distributions of the apache-ssl package (before 1.3.9 on Debian 2.2, and before 1.3.26 on Debian 3.0), for Apache 1.3.27 and earlier, allows local users to read or modify the Apache password file via a symlink attack on temporary files when the administrator runs (1) htpasswd or (2) htdigest, a re-introduction of a vulnerability that was originally identified and addressed by CVE-2001-0131.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103480856102007&w=2
- http://www.debian.org/security/2002/dsa-187
- http://www.debian.org/security/2002/dsa-188
- http://www.debian.org/security/2002/dsa-195
- http://www.iss.net/security_center/static/10412.php

---

#### 553. CVE-2003-0308

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Sendmail 8.12.3 package in Debian GNU/Linux 3.0 does not securely create temporary files, which could allow local users to gain additional privileges via (1) expn, (2) checksendmail, or (3) doublebounce.pl.

**参考链接 / References**:
- http://bugs.debian.org/496408
- http://dev.gentoo.org/~rbu/security/debiantemp/sendmail-base
- http://www.debian.org/security/2003/dsa-305
- http://www.openwall.com/lists/oss-security/2008/10/30/2
- https://bugs.gentoo.org/show_bug.cgi?id=235770

---

#### 554. CVE-2003-0262

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
leksbot 1.2.3 in Debian GNU/Linux installs the KATAXWR as setuid root, which allows local users to gain root privileges by exploiting unknown vulnerabilities related to the escalated privileges, which KATAXWR is not designed to have.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-299
- http://www.securityfocus.com/bid/7505
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11945
- http://www.debian.org/security/2003/dsa-299
- http://www.securityfocus.com/bid/7505

---

#### 555. CVE-2003-0828

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in freesweep in Debian GNU/Linux 3.0 allows local users to gain "games" group privileges when processing environment variables.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-391
- http://www.securityfocus.com/bid/8716
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13301
- http://www.debian.org/security/2003/dsa-391
- http://www.securityfocus.com/bid/8716

---

#### 556. CVE-2004-0911

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
telnetd for netkit 0.17 and earlier, and possibly other versions, on Debian GNU/Linux allows remote attackers to cause a denial of service (free of an invalid pointer), a different vulnerability than CVE-2001-0554.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=273694
- http://www.debian.org/security/2004/dsa-556
- http://www.securityfocus.com/archive/1/375743
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17540
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=273694

---

#### 557. CVE-2004-0563

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The tspc.conf configuration file in freenet6 before 0.9.6 and before 1.0 on Debian Linux has world readable permissions, which could allow local users to gain sensitive information, such as a username and password.

**参考链接 / References**:
- http://secunia.com/advisories/12705/
- http://securitytracker.com/id?1011460
- http://www.debian.org/security/2004/dsa-555
- http://www.securityfocus.com/bid/11280
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17544

---

#### 558. CVE-2004-0833

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sendmail before 8.12.3 on Debian GNU/Linux, when using sasl and sasl-bin, uses a Sendmail configuration script with a fixed username and password, which could allow remote attackers to use Sendmail as an open mail relay and send spam messages.

**参考链接 / References**:
- http://secunia.com/advisories/12667
- http://www.debian.org/security/2004/dsa-554
- http://www.securityfocus.com/bid/11262
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17531
- http://secunia.com/advisories/12667

---

#### 559. CVE-2004-0984

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Unknown vulnerability in the dotlock implementation in mailutils before 1:0.5-4 on Debian GNU/Linux allows attackers to gain privileges.

**参考链接 / References**:
- http://packages.debian.org/changelogs/pool/main/m/mailutils/mailutils_0.6-2/changelog
- http://packages.debian.org/changelogs/pool/main/m/mailutils/mailutils_0.6-2/changelog

---

#### 560. CVE-2004-1343

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
CVS 1.12 and earlier on Debian GNU/Linux does not properly handle when a mapping for the current repository does not exist in the cvs-repouids file, which allows remote attackers to cause a denial of service (server crash).

**参考链接 / References**:
- http://www.debian.org/security/2005/dsa-715
- http://www.debian.org/security/2005/dsa-715

---

#### 561. CVE-2004-2569

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
ipmenu 0.0.3 before Debian GNU/Linux ipmenu_0.0.3-5 allows local users to overwrite arbitrary files via a symlink attack on the ipmenu.log temporary file.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=244709
- http://secunia.com/advisories/11526
- http://secunia.com/advisories/17682
- http://securitytracker.com/id?1010064
- http://www.debian.org/security/2005/dsa-907

---

#### 562. CVE-2004-1340

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Debian GNU/Linux 3.0 installs the libpam-radius-auth package with the pam_radius_auth.conf set to be world-readable, which allows local users to obtain sensitive information.

**参考链接 / References**:
- http://secunia.com/advisories/14046
- http://securitytracker.com/id?1013030
- http://www.debian.org/security/2005/dsa-659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19087
- http://secunia.com/advisories/14046

---

#### 563. CVE-2004-1342

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
CVS 1.12 and earlier on Debian GNU/Linux, when using the repouid patch, allows remote attackers to bypass authentication via the pserver access method.

**参考链接 / References**:
- http://www.debian.org/security/2005/dsa-715
- http://www.debian.org/security/2005/dsa-715

---

#### 564. CVE-2005-0159

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The tpkg-* scripts in the toolchain-source 3.0.4 package on Debian GNU/Linux 3.0 allow local users to overwrite arbitrary files via a symlink attack on temporary files.

**参考链接 / References**:
- http://secunia.com/advisories/14277
- http://www.debian.org/security/2005/dsa-679
- http://www.securityfocus.com/bid/12540
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19317
- http://secunia.com/advisories/14277

---

#### 565. CVE-2005-2214

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
apt-setup in Debian GNU/Linux installs the apt.conf file with insecure permissions, which allows local users to obtain sensitive information such as passwords.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=305142
- http://secunia.com/advisories/15955
- http://www.securityfocus.com/bid/14173
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=305142
- http://secunia.com/advisories/15955

---

#### 566. CVE-2005-1854

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unknown vulnerability in apt-cacher in Debian 3.1, related to "missing input sanitising," allows remote attackers to execute arbitrary commands on the caching server.

**参考链接 / References**:
- http://secunia.com/advisories/16327
- http://www.debian.org/security/2005/dsa-772
- http://www.securityfocus.com/bid/14459
- https://exchange.xforce.ibmcloud.com/vulnerabilities/21664
- http://secunia.com/advisories/16327

---

#### 567. CVE-2005-3254

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The CGIwrap program before 3.9 on Debian GNU/Linux uses an incorrect minimum value of 100 for a UID to determine whether it can perform a seteuid operation, which could allow attackers to execute code as other system UIDs that are greater than the minimum value, which should be 1000 on Debian systems.

**参考链接 / References**:
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html

---

#### 568. CVE-2005-3255

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The (1) cgiwrap and (2) php-cgiwrap packages before 3.9 in Debian GNU/Linux provide access to debugging CGIs under the web document root, which allows remote attackers to obtain sensitive information via direct requests to those CGIs.

**参考链接 / References**:
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html

---

#### 569. CVE-2005-3268

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
yiff server (yiff-server) 2.14.2 on Debian GNU/Linux runs as root and does not properly verify ownership of files that it opens, which allows local users to read arbitrary files.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=334616
- http://secunia.com/advisories/17242
- http://www.osvdb.org/20074
- http://www.securityfocus.com/bid/15140
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=334616

---

#### 570. CVE-2005-4347

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Linux 2.4 kernel patch in kernel-patch-vserver before 1.9.5.5 and 2.x before 2.3 for Debian GNU/Linux does not correctly set the "chroot barrier" with util-vserver, which allows attackers to access files on the host system that are outside of the vserver.

**参考链接 / References**:
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25406
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011

---

#### 571. CVE-2005-4418

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
util-vserver before 0.30.208-1 with kernel-patch-vserver before 1.9.5.5 and 2.x before 2.3 for Debian GNU/Linux sets a default policy that trusts unknown capabilities, which could allow local users to conduct unauthorized activities.

**参考链接 / References**:
- http://secunia.com/advisories/19333
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011
- http://www.securityfocus.com/bid/17180
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25407

---

#### 572. CVE-2005-4693

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Gaim-Encryption 2.38-1 on Debian Linux allows remote attackers to cause a denial of service (crash) via a crafted message from an ICQ buddy, possibly involving the GE_received_key function in keys.c.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337127
- http://secunia.com/advisories/17739
- http://www.osvdb.org/21233
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337127
- http://secunia.com/advisories/17739

---

#### 573. [Ubuntu] USN-8226-2: kmod update

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8226-1 added a mitigation to kmod to disable loading the algif_aead module. This update adds the same mitigation to Ubuntu 14.04 LTS, Ubuntu 16.04 LTS, Ubuntu 18.04 LTS, and Ubuntu 20.04 LTS. Original advisory details: It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disabl

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-2

---

#### 574. CVE-1999-1490

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
xosview 1.5.1 in Red Hat 5.1 allows local users to gain root access via a long HOME environmental variable.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221101926021&w=2
- http://marc.info/?l=bugtraq&m=90221101926034&w=2
- http://www.iss.net/security_center/static/8787.php
- http://www.securityfocus.com/bid/362
- http://marc.info/?l=bugtraq&m=90221101926021&w=2

---

#### 575. CVE-1999-0748

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Red Hat net-tools package.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA1999017_01.html
- http://www.redhat.com/support/errata/RHSA1999017_01.html

---

#### 576. CVE-1999-0814

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Red Hat pump DHCP client allows remote attackers to gain root access in some configurations.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-1999-027.html
- http://www.redhat.com/support/errata/RHSA-1999-027.html

---

#### 577. CVE-1999-0768

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Vixie Cron on Red Hat systems via the MAILTO environmental variable.

**参考链接 / References**:
- http://www.securityfocus.com/bid/602
- http://www.securityfocus.com/bid/602

---

#### 578. CVE-2000-0052

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Red Hat userhelper program in the usermode package allows local users to gain root access via PAM and a .. (dot dot) attack.

**参考链接 / References**:
- http://www.l0pht.com/advisories/pam_advisory
- http://www.redhat.com/support/errata/RHSA-2000-001.html
- http://www.securityfocus.com/bid/913
- http://xforce.iss.net/search.php3?type=2&pattern=linux-pam-userhelper
- http://www.l0pht.com/advisories/pam_advisory

---

#### 579. CVE-2000-0093

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An installation of Red Hat uses DES password encryption with crypt() for the initial password, instead of md5.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0093
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0093

---

#### 580. CVE-2000-0219

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Red Hat 6.0 allows local users to gain root access by booting single user and hitting ^C at the password prompt.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1005
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200002230248.NAA19185%40cairo.anu.edu.au
- https://kc.mcafee.com/corporate/index?page=content&id=SB10053
- http://www.securityfocus.com/bid/1005
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200002230248.NAA19185%40cairo.anu.edu.au

---

#### 581. CVE-2000-0322

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The passwd.php3 CGI script in the Red Hat Piranha Virtual Server Package allows local users to execute arbitrary commands via shell metacharacters.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-014.html
- http://www.securityfocus.com/bid/1149
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Enip.BSO.23.0004241601140.28851-100000%40www.whitehats.com
- http://www.redhat.com/support/errata/RHSA-2000-014.html
- http://www.securityfocus.com/bid/1149

---

#### 582. CVE-2001-0309

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
inetd in Red Hat 6.2 does not properly close sockets for internal services such as chargen, daytime, echo, etc., which allows remote attackers to cause a denial of service via a series of connections to the internal services.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2001-006.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6380
- http://www.redhat.com/support/errata/RHSA-2001-006.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6380

---

#### 583. CVE-2001-1068

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
qpopper 4.01 with PAM based authentication on Red Hat systems generates different error messages when an invalid username is provided instead of a valid name, which allows remote attackers to determine valid usernames on the system.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0363.html
- http://www.securityfocus.com/bid/3242
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7047
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0363.html
- http://www.securityfocus.com/bid/3242

---

#### 584. CVE-2001-0868

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Red Hat Stronghold 2.3 to 3.0 allows remote attackers to retrieve system information via an HTTP GET request to (1) stronghold-info or (2) stronghold-status.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100654958131854&w=2
- http://www.securityfocus.com/bid/3577
- https://exchange.xforce.ibmcloud.com/vulnerabilities/51950
- https://exchange.xforce.ibmcloud.com/vulnerabilities/51951
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7582

---

#### 585. CVE-2001-0946

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
apmscript in Apmd in Red Hat 7.2 "Enigma" allows local users to create or change the modification dates of arbitrary files via a symlink attack on the LOW_POWER temporary file, which could be used to cause a denial of service, e.g. by creating /etc/nologin and disabling logins.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100743394701962&w=2
- http://www.osvdb.org/5493
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=56389
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8268
- http://marc.info/?l=bugtraq&m=100743394701962&w=2

---

#### 586. CVE-2003-0546

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
up2date 3.0.7 and 3.1.23 does not properly verify RPM GPG signatures, which could allow remote attackers to cause unsigned packages to be installed from the Red Hat Network, if that network is compromised.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=106036724315539&w=2
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A631
- http://marc.info/?l=bugtraq&m=106036724315539&w=2
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A631

---

#### 587. CVE-2003-1138

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Apache 2.0.40, as shipped with Red Hat Linux 9.0, allows remote attackers to list directory contents, even if auto indexing is turned off and there is a default web page configured, via a GET request containing a double slash (//).

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/342578
- http://www.securityfocus.com/bid/8898
- http://www.securityfocus.com/archive/1/342578
- http://www.securityfocus.com/bid/8898

---

#### 588. CVE-2004-0217

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
The LiveUpdate capability (liveupdate.sh) in Symantec AntiVirus Scan Engine 4.0 and 4.3 for Red Hat Linux allows local users to create or append to arbitrary files via a symlink attack on /tmp/LiveUpdate.log.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=107694800908164&w=2
- http://www.securityfocus.com/bid/9662
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15215
- http://marc.info/?l=bugtraq&m=107694800908164&w=2
- http://www.securityfocus.com/bid/9662

---

#### 589. CVE-2004-0491

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The linux-2.4.21-mlock.patch in Red Hat Enterprise Linux 3 does not properly maintain the mlock page count when one process unlocks pages that belong to another process, which allows local users to mlock more memory than specified by the rlimit.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060402-01-U
- http://marc.info/?l=linux-kernel&m=108087017610947&w=2
- http://secunia.com/advisories/19607
- http://www.redhat.com/support/errata/RHSA-2005-472.html
- http://www.securityfocus.com/bid/13769

---

#### 590. CVE-2005-0092

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unknown vulnerability in the Red Hat Enterprise Linux 4 kernel 4GB/4GB split patch, when running on x86 with the hugemem kernel, allows local users to cause a denial of service (crash).

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-092.html
- http://www.securityfocus.com/bid/12599
- https://exchange.xforce.ibmcloud.com/vulnerabilities/20620
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11647
- http://www.redhat.com/support/errata/RHSA-2005-092.html

---

#### 591. CVE-2004-1237

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unknown vulnerability in the system call filtering code in the audit subsystem for Red Hat Enterprise Linux 3 allows local users to cause a denial of service (system crash) via unknown vectors.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-043.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11282
- http://www.redhat.com/support/errata/RHSA-2005-043.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11282

---

#### 592. CVE-2005-0087

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The alsa-lib package in Red Hat Linux 4 disables stack protection for the libasound.so library, which makes it easier for attackers to execute arbitrary code if there are other vulnerabilities in the library.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-033.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A10355
- http://www.redhat.com/support/errata/RHSA-2005-033.html
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A10355

---

#### 593. CVE-2005-0206

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The patch for integer overflow vulnerabilities in Xpdf 2.0 and 3.0 (CVE-2004-0888) is incomplete for 64-bit architectures on certain Linux distributions such as Red Hat, which could leave Xpdf users exposed to the original vulnerabilities.

**参考链接 / References**:
- http://www.mandriva.com/security/advisories?name=MDKSA-2005:041
- http://www.mandriva.com/security/advisories?name=MDKSA-2005:042
- http://www.mandriva.com/security/advisories?name=MDKSA-2005:043
- http://www.mandriva.com/security/advisories?name=MDKSA-2005:044
- http://www.mandriva.com/security/advisories?name=MDKSA-2005:052

---

#### 594. CVE-2005-0086

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Heap-based buffer overflow in less in Red Hat Enterprise Linux 3 allows attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted file, as demonstrated using the UTF-8 locale.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-068.html
- https://bugzilla.fedora.us/show_bug.cgi?id=2404
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=145527
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19131
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11027

---

#### 595. CVE-2005-0090

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
A regression error in the Red Hat Enterprise Linux 4 kernel 4GB/4GB split patch omits an "access check," which allows local users to cause a denial of service (crash).

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-092.html
- http://www.securityfocus.com/bid/12599
- https://exchange.xforce.ibmcloud.com/vulnerabilities/20618
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A10425
- http://www.redhat.com/support/errata/RHSA-2005-092.html

---

#### 596. CVE-2005-0091

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Unknown vulnerability in the Red Hat Enterprise Linux 4 kernel 4GB/4GB split patch, when using the hugemem kernel, allows local users to read and write to arbitrary kernel memory and gain privileges via certain syscalls.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-092.html
- http://www.securityfocus.com/bid/12599
- https://exchange.xforce.ibmcloud.com/vulnerabilities/20619
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11249
- http://www.redhat.com/support/errata/RHSA-2005-092.html

---

#### 597. CVE-2005-0757

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The xattr file system code, as backported in Red Hat Enterprise Linux 3 on 64-bit systems, does not properly handle certain offsets, which allows local users to cause a denial of service (system crash) via certain actions on an ext3 file system with extended attributes enabled.

**参考链接 / References**:
- http://secunia.com/advisories/18056
- http://secunia.com/advisories/18059
- http://www.debian.org/security/2005/dsa-921
- http://www.debian.org/security/2005/dsa-922
- http://www.redhat.com/support/errata/RHSA-2005-294.html

---

#### 598. CVE-2005-0403

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
init_dev in tty_io.c in the Red Hat backport of NPTL to Red Hat Enterprise Linux 3 does not properly clear controlling tty's in multi-threaded applications, which allows local users to cause a denial of service (crash) and possibly gain tty access via unknown attack vectors that trigger an access of a pointer to a freed structure.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2005-293.html
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=144059
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A9435
- http://www.redhat.com/support/errata/RHSA-2005-293.html
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=144059

---

#### 599. CVE-2005-3269

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Stack-based buffer overflow in help.cgi in the HTTP administrative interface for (1) Sun Java System Directory Server 5.2 2003Q4, 2004Q2, and 2005Q1, (2) Red Hat Directory Server and (3) Certificate Server before 7.1 SP1, (4) Sun ONE Directory Server 5.1 SP4 and earlier, and (5) Sun ONE Administration Server 5.2 allows remote attackers to cause a denial of service (admin server crash), or local users to gain root privileges.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=112862037500012&w=2
- http://marc.info/?l=bugtraq&m=113815459026080&w=2
- http://secunia.com/advisories/17092
- http://secunia.com/advisories/18590
- http://securityreason.com/securityalert/367

---

#### 600. CVE-2005-2100

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The rw_vm function in usercopy.c in the 4GB split patch for the Linux kernel in Red Hat Enterprise Linux 4 does not perform proper bounds checking, which allows local users to cause a denial of service (crash).

**参考链接 / References**:
- http://secunia.com/advisories/17073
- http://www.redhat.com/support/errata/RHSA-2005-514.html
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=165547
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11556
- http://secunia.com/advisories/17073

---

#### 601. CVE-2005-1918

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
The original patch for a GNU tar directory traversal vulnerability (CVE-2002-0399) in Red Hat Enterprise Linux 3 and 2.1 uses an "incorrect optimization" that allows user-assisted attackers to overwrite arbitrary files via a crafted tar file, probably involving "/../" sequences with a leading "/".

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060301-01.U.asc
- http://secunia.com/advisories/18988
- http://secunia.com/advisories/19130
- http://secunia.com/advisories/19183
- http://secunia.com/advisories/20397

---

#### 602. CVE-2005-3629

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
initscripts in Red Hat Enterprise Linux 4 does not properly handle certain environment variables when /sbin/service is executed, which allows local users with sudo permissions for /sbin/service to gain root privileges via unknown vectors.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060401-01-U
- http://secunia.com/advisories/19162
- http://secunia.com/advisories/19532
- http://securitytracker.com/id?1015732
- http://www.redhat.com/support/errata/RHSA-2006-0015.html

---

#### 603. CVE-2006-1273

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Mozilla Firefox 1.0.7 and 1.5.0.1 allows remote attackers to cause a denial of service (crash) via an HTML tag with a large number of script action handlers such as onload and onmouseover, which triggers the crash when the user views the page source.  NOTE: Red Hat has disputed this issue, suggesting that "It is likely the reporter was running the IE Tab extension," and Mozilla also confirmed that this is not an issue in Firefox itself

**参考链接 / References**:
- http://osvdb.org/31833
- http://securityreason.com/securityalert/593
- http://www.securityfocus.com/archive/1/427977/100/0/threaded
- http://www.securityfocus.com/archive/1/428159/100/0/threaded
- http://osvdb.org/31833

---

#### 604. CVE-2006-3467

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Integer overflow in FreeType before 2.2 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted PCF file, as demonstrated by the Red Hat bad1.pcf test file, due to a partial fix of CVE-2006-1861.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060701-01-U
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=190593
- http://lists.apple.com/archives/security-announce/2009/Feb/msg00000.html
- http://lists.opensuse.org/opensuse-security-announce/2007-10/msg00006.html
- http://lists.suse.com/archive/suse-security-announce/2006-Aug/0002.html

---

#### 605. CVE-2006-2933

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
kdesktop_lock in kdebase before 3.1.3-5.11 for KDE in Red Hat Enterprise Linux (RHEL) 3 does not properly terminate, which can prevent the screensaver from activating or prevent users from manually locking the desktop.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=177755
- http://secunia.com/advisories/21203
- http://securitytracker.com/id?1016571
- http://www.redhat.com/support/errata/RHSA-2006-0576.html
- http://www.securityfocus.com/bid/19152

---

#### 606. CVE-2006-3813

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
A regression error in the Perl package for Red Hat Enterprise Linux 4 omits the patch for CVE-2005-0155, which allows local users to overwrite arbitrary files with debugging information.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2006-0605.html
- http://secunia.com/advisories/21646
- http://support.avaya.com/elmodocs2/security/ASA-2006-163.htm
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A9456
- http://rhn.redhat.com/errata/RHSA-2006-0605.html

---

#### 607. CVE-2006-2932

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
A regression error in the restore_all code path of the 4/4GB split support for non-hugemem Linux kernels on Red Hat Linux Desktop and Enterprise Linux 4 allows local users to cause a denial of service (panic) via unspecified vectors.

**参考链接 / References**:
- http://secunia.com/advisories/21605
- http://secunia.com/advisories/22174
- http://support.avaya.com/elmodocs2/security/ASA-2006-203.htm
- http://www.osvdb.org/28120
- http://www.redhat.com/support/errata/RHSA-2006-0617.html

---

#### 608. CVE-2006-5170

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
pam_ldap in nss_ldap on Red Hat Enterprise Linux 4, Fedora Core 3 and earlier, and possibly other distributions does not return an error condition when an LDAP directory server responds with a PasswordPolicyResponse control response, which causes the pam_authenticate function to return a success code even if authentication has failed, as originally reported for xscreensaver.

**参考链接 / References**:
- http://bugzilla.padl.com/show_bug.cgi?id=291
- http://rhn.redhat.com/errata/RHSA-2006-0719.html
- http://secunia.com/advisories/22682
- http://secunia.com/advisories/22685
- http://secunia.com/advisories/22694

---

#### 609. CVE-2006-4342

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The kernel in Red Hat Enterprise Linux 3, when running on SMP systems, allows local users to cause a denial of service (deadlock) by running the shmat function on an shm at the same time that shmctl is removing that shm (IPC_RMID), which prevents a spinlock from being unlocked.

**参考链接 / References**:
- http://secunia.com/advisories/22497
- http://secunia.com/advisories/23064
- http://support.avaya.com/elmodocs2/security/ASA-2006-254.htm
- http://www.kb.cert.org/vuls/id/245984
- http://www.redhat.com/support/errata/RHSA-2006-0710.html

---

#### 610. CVE-2007-0980

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unspecified vulnerability in HP Serviceguard for Linux; packaged for SuSE SLES8 and United Linux 1.0 before SG A.11.15.07, SuSE SLES9 and SLES10 before SG A.11.16.10, and Red Hat Enterprise Linux (RHEL) before SG A.11.16.10; allows remote attackers to obtain unauthorized access via unspecified vectors.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c00860750
- http://osvdb.org/33201
- http://secunia.com/advisories/24134
- http://www.securityfocus.com/bid/22574
- http://www.securitytracker.com/id?1017655

---

#### 611. CVE-2007-0001

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
The file watch implementation in the audit subsystem (auditctl -w) in the Red Hat Enterprise Linux (RHEL) 4 kernel 2.6.9 allows local users to cause a denial of service (kernel panic) by replacing a watched file, which does not cause the watch on the old inode to be dropped.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=223129
- http://osvdb.org/33031
- http://secunia.com/advisories/24300
- http://www.redhat.com/support/errata/RHSA-2007-0085.html
- http://www.securityfocus.com/bid/22737

---

#### 612. CVE-2006-7175

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The version of Sendmail 8.13.1-2 on Red Hat Enterprise Linux 4 Update 4 and earlier does not allow the administrator to disable SSLv2 encryption, which could cause less secure channels to be used than desired.

**参考链接 / References**:
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=172352
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=172352

---

#### 613. CVE-2006-7176

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The version of Sendmail 8.13.1-2 on Red Hat Enterprise Linux 4 Update 4 and earlier does not reject the "localhost.localdomain" domain name for e-mail messages that come from external hosts, which might allow remote attackers to spoof messages.

**参考链接 / References**:
- http://secunia.com/advisories/25098
- http://secunia.com/advisories/25743
- http://support.avaya.com/elmodocs2/security/ASA-2007-248.htm
- http://www.redhat.com/support/errata/RHSA-2007-0252.html
- http://www.securityfocus.com/bid/23742

---

#### 614. CVE-2007-0773

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Linux kernel before 2.6.9-42.0.8 in Red Hat 4.4 allows local users to cause a denial of service (kernel OOPS from null dereference) via fput in a 32-bit ioctl on 64-bit x86 systems, an incomplete fix of CVE-2005-3044.1.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=243252
- http://osvdb.org/37128
- http://rhn.redhat.com/errata/RHSA-2007-0488.html
- http://secunia.com/advisories/25838
- http://secunia.com/advisories/26289

---

#### 615. CVE-2007-3104

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
The sysfs_readdir function in the Linux kernel 2.6, as used in Red Hat Enterprise Linux (RHEL) 4.5 and other distributions, allows users to cause a denial of service (kernel OOPS) by dereferencing a null pointer to an inode in a dentry.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=242558
- http://lists.opensuse.org/opensuse-security-announce/2007-12/msg00001.html
- http://osvdb.org/37115
- http://rhn.redhat.com/errata/RHSA-2007-0488.html
- http://secunia.com/advisories/25771

---

#### 616. CVE-2007-3908

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Unspecified vulnerability in HP ServiceGuard for Linux for Red Hat Enterprise Linux (RHEL) 2.1 SG A.11.14.04 through A.11.14.06; RHEL 3.0 SG A.11.16.04 through A.11.16.10; and ServiceGuard Cluster Object Manager B.03.01.02 allows local users to gain privileges via unspecified vectors, a different vulnerability than CVE-2007-0980.

**参考链接 / References**:
- http://osvdb.org/38159
- http://secunia.com/advisories/26051
- http://securityreason.com/securityalert/2907
- http://www.securityfocus.com/archive/1/473783/100/0/threaded
- http://www.securityfocus.com/bid/24920

---

#### 617. CVE-2007-4044

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: The MS-RPC functionality in smbd in Samba 3 on SUSE Linux before 20070720 does not include "one character in the shell escape handling."  NOTE: this issue was originally characterized as a shell metacharacter issue due to an incomplete fix for CVE-2007-2447, which was interpreted by CVE to be security relevant.  However, SUSE and Red Hat have disputed the problem, stating that the only impact is that scripts will not be executed if they have a "c" in their name, but even this limitation might not exist.  This does not have security implications, so should not be included in CVE

---

#### 618. CVE-2007-2797

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
xterm, including 192-7.el4 in Red Hat Enterprise Linux and 208-3.1 in Debian GNU/Linux, sets the wrong group ownership of tty devices, which allows local users to write data to other users' terminals.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=349924
- http://secunia.com/advisories/26562
- http://secunia.com/advisories/27617
- http://secunia.com/advisories/27921
- http://securityreason.com/securityalert/3066

---

#### 619. CVE-2007-4132

**严重程度 / Severity**: N/A | CVSS: 6.5

**漏洞描述 / Description**:
Unspecified vulnerability in Red Hat Network Satellite Server 5.0.0 allows remote authenticated users to execute arbitrary code via unknown vectors in a "back-end XMLRPC handler."

**参考链接 / References**:
- http://osvdb.org/40438
- http://secunia.com/advisories/26687
- http://www.redhat.com/support/errata/RHSA-2007-0868.html
- http://www.securityfocus.com/bid/25490
- http://www.securitytracker.com/id?1018626

---

#### 620. CVE-2007-3849

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
Red Hat Enterprise Linux (RHEL) 5 ships the rpm for the Advanced Intrusion Detection Environment (AIDE) before 0.13.1 with a database that lacks checksum information, which allows context-dependent attackers to bypass file integrity checks and modify certain files.

**参考链接 / References**:
- http://osvdb.org/40439
- http://secunia.com/advisories/26711
- http://www.redhat.com/support/errata/RHSA-2007-0539.html
- http://www.securityfocus.com/bid/25542
- http://www.securitytracker.com/id?1018652

---

#### 621. CVE-2007-3379

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unspecified vulnerability in the kernel in Red Hat Enterprise Linux (RHEL) 4 on the x86_64 platform allows local users to cause a denial of service (OOPS) via unspecified vectors related to the get_gate_vma function and the fuser command.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHBA-2007-0304.html
- https://bugzilla.redhat.com/show_bug.cgi?id=178981
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A10426
- http://rhn.redhat.com/errata/RHBA-2007-0304.html
- https://bugzilla.redhat.com/show_bug.cgi?id=178981

---

#### 622. CVE-2007-0004

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The NFS client implementation in the kernel in Red Hat Enterprise Linux (RHEL) 3, when a filesystem is mounted with the noacl option, checks permissions for the open system call via vfs_permission (mode bits) data rather than an NFS ACCESS call to the server, which allows local client processes to obtain a false success status from open calls that the server would deny, and possibly obtain sensitive information about file permissions on the server, as demonstrated in a root_squash environment.  NOTE: it is uncertain whether any scenarios involving this issue cross privilege boundaries.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=199715
- https://bugzilla.redhat.com/show_bug.cgi?id=199715

---

#### 623. CVE-2007-1865

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The ipv6_getsockopt_sticky function in the kernel in Red Hat Enterprise Linux (RHEL) Beta 5.1.0 allows local users to obtain sensitive information (kernel memory contents) via a negative value of the len parameter.  NOTE: this issue has been disputed in a bug comment, stating that "len is ignored when copying header info to the user's buffer.

**参考链接 / References**:
- http://osvdb.org/45909
- https://bugzilla.redhat.com/show_bug.cgi?id=232045
- http://osvdb.org/45909
- https://bugzilla.redhat.com/show_bug.cgi?id=232045

---

#### 624. CVE-2007-5079

**严重程度 / Severity**: N/A | CVSS: 6.0

**漏洞描述 / Description**:
Red Hat Enterprise Linux 4 does not properly compile and link gdm with tcp_wrappers on x86_64 platforms, which might allow remote attackers to bypass intended access restrictions.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2010-0657.html
- https://bugzilla.redhat.com/show_bug.cgi?id=181302
- https://exchange.xforce.ibmcloud.com/vulnerabilities/36791
- http://www.redhat.com/support/errata/RHSA-2010-0657.html
- https://bugzilla.redhat.com/show_bug.cgi?id=181302

---

#### 625. CVE-2007-4574

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
Unspecified vulnerability in the "stack unwinder fixes" in kernel in Red Hat Enterprise Linux 5, when running on AMD64 and Intel 64, allows local users to cause a denial of service via unknown vectors.

**参考链接 / References**:
- http://osvdb.org/45489
- http://secunia.com/advisories/27322
- http://securitytracker.com/id?1018844
- http://www.redhat.com/support/errata/RHSA-2007-0940.html
- http://www.securityfocus.com/bid/26158

---

#### 626. CVE-2007-4994

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Certificate Server 7.2 in Red Hat Certificate System (RHCS) does not properly handle new revocations that occur while a Certificate Revocation List (CRL) is being generated, which might prevent certain revoked certificates from appearing on the CRL quickly and allow users with revoked certificates to bypass the intended CRL.

**参考链接 / References**:
- http://osvdb.org/40440
- http://secunia.com/advisories/27557
- http://www.redhat.com/support/errata/RHSA-2007-0934.html
- http://www.securityfocus.com/bid/26377
- http://www.securitytracker.com/id?1020532

---

#### 627. CVE-2007-4136

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The ricci daemon in Red Hat Conga 0.10.0 allows remote attackers to cause a denial of service (loss of new connections) by repeatedly sending data or attempting connections.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2007-0640.html
- http://secunia.com/advisories/27611
- http://securitytracker.com/id?1018921
- http://www.securityfocus.com/bid/26393
- https://bugzilla.redhat.com/show_bug.cgi?id=336101

---

#### 628. CVE-2007-5494

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Memory leak in the Red Hat Content Accelerator kernel patch in Red Hat Enterprise Linux (RHEL) 4 and 5 allows local users to cause a denial of service (memory consumption) via a large number of open requests involving O_ATOMICLOOKUP.

**参考链接 / References**:
- http://osvdb.org/44153
- http://secunia.com/advisories/27824
- http://secunia.com/advisories/28162
- http://www.redhat.com/support/errata/RHSA-2007-0993.html
- http://www.redhat.com/support/errata/RHSA-2007-1104.html

---

#### 629. CVE-2007-5964

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The default configuration of autofs 5 in some Linux distributions, such as Red Hat Enterprise Linux (RHEL) 5, omits the nosuid option for the hosts (/net filesystem) map, which allows local users to gain privileges via a setuid program on a remote NFS server.

**参考链接 / References**:
- http://osvdb.org/40441
- http://secunia.com/advisories/28052
- http://secunia.com/advisories/28097
- http://secunia.com/advisories/28456
- http://securitytracker.com/id?1019087

---

#### 630. CVE-2007-6283

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Red Hat Enterprise Linux 5 and Fedora install the Bind /etc/rndc.key file with world-readable permissions, which allows local users to perform unauthorized named commands, such as causing a denial of service by stopping named.

**参考链接 / References**:
- http://secunia.com/advisories/28180
- http://secunia.com/advisories/30313
- http://www.redhat.com/support/errata/RHSA-2008-0300.html
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2007-6283
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A9977

---

#### 631. CVE-2007-6285

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
The default configuration for autofs 5 (autofs5) in some Linux distributions, such as Red Hat Enterprise Linux (RHEL) 4 and 5, does not specify the nodev mount option for the -hosts map, which allows local users to access "important devices" by operating a remote NFS server and creating special device files on that server, as demonstrated by the /dev/mem device.

**参考链接 / References**:
- http://osvdb.org/40442
- http://rhn.redhat.com/errata/RHSA-2007-1176.html
- http://rhn.redhat.com/errata/RHSA-2007-1177.html
- http://secunia.com/advisories/28156
- http://secunia.com/advisories/28168

---

#### 632. CVE-2007-4130

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Linux kernel 2.6.9 before 2.6.9-67 in Red Hat Enterprise Linux (RHEL) 4 on Itanium (ia64) does not properly handle page faults during NUMA memory access, which allows local users to cause a denial of service (panic) via invalid arguments to set_mempolicy in an MPOL_BIND operation.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2008-0055.html
- http://secunia.com/advisories/28748
- http://www.securityfocus.com/bid/27556
- https://bugzilla.redhat.com/show_bug.cgi?id=179665
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A11437

---

#### 633. CVE-2008-1198

**严重程度 / Severity**: N/A | CVSS: 7.1

**漏洞描述 / Description**:
The default IPSec ifup script in Red Hat Enterprise Linux 3 through 5 configures racoon to use aggressive IKE mode instead of main IKE mode, which makes it easier for remote attackers to conduct brute force attacks by sniffing an unencrypted preshared key (PSK) hash.

**参考链接 / References**:
- http://secunia.com/advisories/48045
- http://www.ernw.de/download/pskattack.pdf
- http://www.securitytracker.com/id?1019563
- https://bugzilla.redhat.com/show_bug.cgi?id=435274
- https://exchange.xforce.ibmcloud.com/vulnerabilities/41053

---

#### 634. CVE-2008-0890

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Red Hat Directory Server 7.1 before SP4 uses insecure permissions for certain directories, which allows local users to modify JAR files and execute arbitrary code via unknown vectors.

**参考链接 / References**:
- http://secunia.com/advisories/29350
- http://www.redhat.com/support/errata/RHSA-2008-0173.html
- http://www.securityfocus.com/bid/28204
- http://www.securitytracker.com/id?1019577
- https://exchange.xforce.ibmcloud.com/vulnerabilities/41152

---

#### 635. CVE-2008-0889

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Red Hat Directory Server 8.0, when running on Red Hat Enterprise Linux, uses insecure permissions for the redhat-idm-console script, which allows local users to execute arbitrary code by modifying the script.

**参考链接 / References**:
- http://secunia.com/advisories/29482
- http://www.redhat.com/support/errata/RHSA-2008-0191.html
- http://www.securityfocus.com/bid/28327
- http://www.securitytracker.com/id?1019677
- http://secunia.com/advisories/29482

---

#### 636. CVE-2008-0884

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The Replace function in the capp-lspp-config script in the (1) lspp-eal4-config-ibm and (2) capp-lspp-eal4-config-hp packages before 0.65-2 in Red Hat Enterprise Linux (RHEL) 5 uses lstat instead of stat to determine the /etc/pam.d/system-auth file permissions, leading to a change to world-writable permissions for the /etc/pam.d/system-auth-ac file, which allows local users to gain privileges by modifying this file.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2008-0193.html
- http://secunia.com/advisories/29642
- http://securitytracker.com/id?1019740
- http://www.securityfocus.com/bid/28557
- https://bugzilla.redhat.com/show_bug.cgi?id=435442

---

#### 637. CVE-2008-1374

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Integer overflow in pdftops filter in CUPS in Red Hat Enterprise Linux 3 and 4, when running on 64-bit platforms, allows remote attackers to execute arbitrary code via a crafted PDF file.  NOTE: this issue is due to an incomplete fix for CVE-2004-0888.

**参考链接 / References**:
- http://secunia.com/advisories/29630
- http://secunia.com/advisories/31388
- http://wiki.rpath.com/wiki/Advisories:rPSA-2008-0245
- http://www.redhat.com/support/errata/RHSA-2008-0206.html
- http://www.securityfocus.com/archive/1/495164/100/0/threaded

---

#### 638. CVE-2008-0892

**严重程度 / Severity**: N/A | CVSS: 9.0

**漏洞描述 / Description**:
The replication monitor CGI script (repl-monitor-cgi.pl) in Red Hat Administration Server, as used by Red Hat Directory Server 8.0 EL4 and EL5, allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01433676
- http://secunia.com/advisories/29761
- http://secunia.com/advisories/29826
- http://secunia.com/advisories/30114
- http://www.redhat.com/support/errata/RHSA-2008-0199.html

---

#### 639. CVE-2008-0893

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Red Hat Administration Server, as used by Red Hat Directory Server 8.0 EL4 and EL5, does not properly restrict access to CGI scripts, which allows remote attackers to perform administrative actions.

**参考链接 / References**:
- http://secunia.com/advisories/29761
- http://secunia.com/advisories/29826
- http://www.redhat.com/support/errata/RHSA-2008-0201.html
- http://www.securityfocus.com/bid/28802
- http://www.securitytracker.com/id?1019857

---

#### 640. CVE-2008-1677

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the regular expression handler in Red Hat Directory Server 8.0 and 7.1 before SP6 allows remote attackers to cause a denial of service (slapd crash) and possibly execute arbitrary code via a crafted LDAP query that triggers the overflow during translation to a regular expression.

**参考链接 / References**:
- http://secunia.com/advisories/30181
- http://secunia.com/advisories/30185
- http://www.redhat.com/support/errata/RHSA-2008-0268.html
- http://www.redhat.com/support/errata/RHSA-2008-0269.html
- http://www.securityfocus.com/bid/29126

---

#### 641. CVE-2007-5962

**严重程度 / Severity**: N/A | CVSS: 7.1

**漏洞描述 / Description**:
Memory leak in a certain Red Hat patch, applied to vsftpd 2.0.5 on Red Hat Enterprise Linux (RHEL) 5 and Fedora 6 through 8, and on Foresight Linux and rPath appliances, allows remote attackers to cause a denial of service (memory consumption) via a large number of CWD commands, as demonstrated by an attack on a daemon with the deny_file configuration option.

**参考链接 / References**:
- http://secunia.com/advisories/30341
- http://secunia.com/advisories/30354
- http://securitytracker.com/id?1020079
- http://wiki.rpath.com/wiki/Advisories:rPSA-2008-0185
- http://www.openwall.com/lists/oss-security/2008/05/21/10

---

#### 642. CVE-2007-5961

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in the Red Hat Network channel search feature, as used in RHN and Red Hat Network Satellite before 5.0.2, allows remote attackers to inject arbitrary web script or HTML via unknown vectors.

**参考链接 / References**:
- http://osvdb.org/45765
- http://www.redhat.com/support/errata/RHSA-2008-0261.html
- http://www.securitytracker.com/id?1020051
- https://bugzilla.redhat.com/show_bug.cgi?id=396641
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42559

---

#### 643. CVE-2008-1036

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The International Components for Unicode (ICU) library in Apple Mac OS X before 10.5.3, Red Hat Enterprise Linux 5, and other operating systems omits some invalid character sequences during conversion of some character encodings, which might allow remote attackers to conduct cross-site scripting (XSS) attacks.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2008//May/msg00001.html
- http://secunia.com/advisories/30430
- http://secunia.com/advisories/34290
- http://secunia.com/advisories/34777
- http://securitytracker.com/id?1020139

---

#### 644. CVE-2008-2366

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
Untrusted search path vulnerability in a certain Red Hat build script for OpenOffice.org (OOo) 1.1.x on Red Hat Enterprise Linux (RHEL) 3 and 4 allows local users to gain privileges via a malicious library in the current working directory, related to incorrect quoting of the ORIGIN symbol for use in the RPATH library path.

**参考链接 / References**:
- http://secunia.com/advisories/30633
- http://securitytracker.com/id?1020278
- http://www.redhat.com/support/errata/RHSA-2008-0538.html
- http://www.securityfocus.com/bid/29695
- https://bugzilla.redhat.com/show_bug.cgi?id=450532

---

#### 645. CVE-2008-1951

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in a certain Red Hat build script for Standards Based Linux Instrumentation for Manageability (sblim) libraries before 1-13a.el4_6.1 in Red Hat Enterprise Linux (RHEL) 4, and before 1-31.el5_2.1 in RHEL 5, allows local users to gain privileges via a malicious library in a certain subdirectory of /var/tmp, related to an incorrect RPATH setting, as demonstrated by a malicious libc.so library for tog-pegasus.

**参考链接 / References**:
- http://secunia.com/advisories/30803
- http://www.securityfocus.com/bid/29913
- http://www.securitytracker.com/id?1020354
- https://bugzilla.redhat.com/show_bug.cgi?id=447705
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43315

---

#### 646. CVE-2008-2365

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
Race condition in the ptrace and utrace support in the Linux kernel 2.6.9 through 2.6.25, as used in Red Hat Enterprise Linux (RHEL) 4, allows local users to cause a denial of service (oops) via a long series of PTRACE_ATTACH ptrace calls to another user's process that trigger a conflict between utrace_detach and report_quiescent, related to "late ptrace_may_attach() check" and "race around &dead_engine_ops setting," a different vulnerability than CVE-2007-0771 and CVE-2008-1514.  NOTE: this issue might only affect kernel versions before 2.6.16.x.

**参考链接 / References**:
- http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.25.y.git%3Ba=commit%3Bh=5ecfbae093f0c37311e89b29bfc0c9d586eace87
- http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.25.y.git%3Ba=commit%3Bh=f358166a9405e4f1d8e50d8f415c26d95505b6de
- http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.25.y.git%3Ba=commit%3Bh=f5b40e363ad6041a96e3da32281d8faa191597b9
- http://marc.info/?l=linux-kernel&m=117863520707703&w=2
- http://rhn.redhat.com/errata/RHSA-2008-0508.html

---

#### 647. CVE-2008-2944

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Double free vulnerability in the utrace support in the Linux kernel, probably 2.6.18, in Red Hat Enterprise Linux (RHEL) 5 and Fedora Core 6 (FC6) allows local users to cause a denial of service (oops), as demonstrated by a crash when running the GNU GDB testsuite, a different vulnerability than CVE-2008-2365.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=207002
- https://bugzilla.redhat.com/show_bug.cgi?id=449359
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43556
- https://bugzilla.redhat.com/show_bug.cgi?id=207002
- https://bugzilla.redhat.com/show_bug.cgi?id=449359

---

#### 648. CVE-2008-1676

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Red Hat PKI Common Framework (rhpki-common) in Red Hat Certificate System (aka Certificate Server or RHCS) 7.1 through 7.3, and Netscape Certificate Management System 6.x, does not recognize Certificate Authority profile constraints on Extensions, which might allow remote attackers to bypass intended restrictions and conduct man-in-the-middle attacks by submitting a certificate signing request (CSR) and using the resulting certificate.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2008-0500.html
- http://rhn.redhat.com/errata/RHSA-2008-0577.html
- http://secunia.com/advisories/30929
- http://www.securityfocus.com/bid/30062
- http://www.securitytracker.com/id?1020427

---

#### 649. CVE-2008-2375

**严重程度 / Severity**: N/A | CVSS: 7.1

**漏洞描述 / Description**:
Memory leak in a certain Red Hat deployment of vsftpd before 2.0.5 on Red Hat Enterprise Linux (RHEL) 3 and 4, when PAM is used, allows remote attackers to cause a denial of service (memory consumption) via a large number of invalid authentication attempts within the same session, a different vulnerability than CVE-2007-5962.

**参考链接 / References**:
- http://secunia.com/advisories/31007
- http://secunia.com/advisories/31223
- http://secunia.com/advisories/32263
- http://support.avaya.com/elmodocs2/security/ASA-2008-398.htm
- http://wiki.rpath.com/Advisories:rPSA-2008-0217

---

#### 650. CVE-2008-1376

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
A certain Red Hat build script for nfs-utils before 1.0.9-35z.el5_2 on Red Hat Enterprise Linux (RHEL) 5 omits TCP wrappers support, which might allow remote attackers to bypass intended access restrictions.

**参考链接 / References**:
- http://secunia.com/advisories/31322
- http://secunia.com/advisories/35162
- http://www.redhat.com/support/errata/RHSA-2008-0486.html
- http://www.redhat.com/support/errata/RHSA-2009-0955.html
- http://www.securityfocus.com/bid/30466

---

#### 651. CVE-2008-2369

**严重程度 / Severity**: CRITICAL | CVSS: 9.1

**漏洞描述 / Description**:
manzier.pxt in Red Hat Network Satellite Server before 5.1.1 has a hard-coded authentication key, which allows remote attackers to connect to the server and obtain sensitive information about user accounts and entitlements.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2008-0630.html
- http://secunia.com/advisories/31493
- http://securitytracker.com/id?1020694
- http://www.securityfocus.com/bid/30679
- https://exchange.xforce.ibmcloud.com/vulnerabilities/44452

---

#### 652. CVE-2008-3270

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
yum-rhn-plugin in Red Hat Enterprise Linux (RHEL) 5 does not verify the SSL certificate for a file download from a Red Hat Network (RHN) server, which makes it easier for remote man-in-the-middle attackers to cause a denial of service (loss of updates) or force the download and installation of official Red Hat packages that were not requested.

**参考链接 / References**:
- http://secunia.com/advisories/31472
- http://securitytracker.com/id?1020698
- http://www.redhat.com/support/errata/RHSA-2008-0815.html
- http://www.securityfocus.com/bid/30695
- https://bugzilla.redhat.com/show_bug.cgi?id=457113

---

#### 653. CVE-2008-3844

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Certain Red Hat Enterprise Linux (RHEL) 4 and 5 packages for OpenSSH, as signed in August 2008 using a legitimate Red Hat GPG key, contain an externally introduced modification (Trojan Horse) that allows the package authors to have an unknown impact.  NOTE: since the malicious packages were not distributed from any official Red Hat sources, the scope of this issue is restricted to users who may have obtained these packages through unofficial distribution points.  As of 20080827, no unofficial distributions of this software are known.

**参考链接 / References**:
- http://secunia.com/advisories/31575
- http://secunia.com/advisories/32241
- http://securitytracker.com/id?1020730
- http://support.avaya.com/elmodocs2/security/ASA-2008-399.htm
- http://www.redhat.com/security/data/openssh-blacklist.html

---

#### 654. CVE-2008-2928

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Multiple buffer overflows in the adminutil library in CGI applications in Red Hat Directory Server 7.1 before SP7 allow remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a crafted Accept-Language HTTP header.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31777
- http://securitytracker.com/id?1020771

---

#### 655. CVE-2008-2929

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the adminutil library in the Directory Server Administration Express and Directory Server Gateway (DSGW) web interface in Red Hat Directory Server 7.1 before SP7 and 8 EL4 and EL5, and Fedora Directory Server, allow remote attackers to inject arbitrary web script or HTML via input values that use % (percent) escaping.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31612
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31777

---

#### 656. CVE-2008-2930

**严重程度 / Severity**: N/A | CVSS: 7.1

**漏洞描述 / Description**:
Red Hat Directory Server 7.1 before SP7, Red Hat Directory Server 8, and Fedora Directory Server 1.1.1 allow remote attackers to cause a denial of service (CPU consumption and search outage) via crafted LDAP search requests with patterns, related to a single-threaded regular-expression subsystem.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31627
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31867

---

#### 657. CVE-2008-3283

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Multiple memory leaks in Red Hat Directory Server 7.1 before SP7, Red Hat Directory Server 8, and Fedora Directory Server 1.1.1 and earlier allow remote attackers to cause a denial of service (memory consumption) via vectors involving (1) the authentication / bind phase and (2) anonymous LDAP search requests.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31627
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31867

---

#### 658. CVE-2008-2932

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Heap-based buffer overflow in Red Hat adminutil 1.1.6 allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via % (percent) encoded HTTP input to unspecified CGI scripts in Fedora Directory Server.  NOTE: this vulnerability exists because of an incorrect fix for CVE-2008-2929.

**参考链接 / References**:
- http://secunia.com/advisories/31777
- http://www.securityfocus.com/bid/31106
- https://bugzilla.redhat.com/show_bug.cgi?id=454662
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45203
- https://www.redhat.com/archives/fedora-package-announce/2008-September/msg00218.html

---

#### 659. CVE-2008-3274

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Red Hat Enterprise IPA 1.0.0 and FreeIPA before 1.1.1 places ldap:///anyone on the read ACL for the krbMKey attribute, which allows remote attackers to obtain the Kerberos master key via an anonymous LDAP query.

**参考链接 / References**:
- http://git.fedorahosted.org/git/freeipa.git/?p=freeipa.git%3Ba=commit%3Bh=9932887f2af38b9701efec27707648c026ec445c
- http://rhn.redhat.com/errata/RHSA-2008-0860.html
- http://secunia.com/advisories/31861
- http://www.freeipa.org/page/CVE-2008-3274
- http://www.freeipa.org/page/Downloads

---

#### 660. CVE-2008-3519

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The default configuration of the JBossAs component in Red Hat JBoss Enterprise Application Platform (aka JBossEAP or EAP), possibly 4.2 before CP04 and 4.3 before CP02, when a production environment is enabled, sets the DownloadServerClasses property to true, which allows remote attackers to obtain sensitive information (non-EJB classes) via a download request, a different vulnerability than CVE-2008-3273.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=458823
- http://www.redhat.com/docs/en-US/JBoss_Enterprise_Application_Platform/4.2.0.cp04/html-single/readme/index.html
- http://www.redhat.com/docs/en-US/JBoss_Enterprise_Application_Platform/4.3.0.cp02/html-single/readme/index.html
- http://www.redhat.com/support/errata/RHSA-2008-0831.html
- http://www.redhat.com/support/errata/RHSA-2008-0832.html

---

#### 661. CVE-2008-3825

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
pam_krb5 2.2.14 in Red Hat Enterprise Linux (RHEL) 5 and earlier, when the existing_ticket option is enabled, uses incorrect privileges when reading a Kerberos credential cache, which allows local users to gain privileges by setting the KRB5CCNAME environment variable to an arbitrary cache filename and running the (1) su or (2) sudo program. NOTE: there may be a related vector involving sshd that has limited relevance.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-12/msg00002.html
- http://secunia.com/advisories/32119
- http://secunia.com/advisories/32135
- http://secunia.com/advisories/32174
- http://secunia.com/advisories/43314

---

#### 662. CVE-2008-4870

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dovecot 1.0.7 in Red Hat Enterprise Linux (RHEL) 5, and possibly Fedora, uses world-readable permissions for dovecot.conf, which allows local users to obtain the ssl_key_password parameter value.

**参考链接 / References**:
- http://secunia.com/advisories/32164
- http://secunia.com/advisories/33149
- http://secunia.com/advisories/33624
- http://security.gentoo.org/glsa/glsa-200812-16.xml
- http://www.openwall.com/lists/oss-security/2008/10/29/10

---

#### 663. CVE-2021-34419

**严重程度 / Severity**: LOW | CVSS: 3.7

**漏洞描述 / Description**:
In the Zoom Client for Meetings for Ubuntu Linux before version 5.1.0, there is an HTML injection flaw when sending a remote control request to a user in the process of in-meeting screen sharing. This could allow meeting participants to be targeted for social engineering attacks.

**参考链接 / References**:
- https://explore.zoom.us/en/trust/security/security-bulletin
- https://explore.zoom.us/en/trust/security/security-bulletin

---

#### 664. CVE-2021-3939

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Ubuntu-specific modifications to accountsservice (in patch file debian/patches/0010-set-language.patch) caused the fallback_locale variable, pointing to static storage, to be freed, in the user_change_language_authorized_cb function. This is reachable via the SetLanguage dbus function. This is fixed in versions 0.6.55-0ubuntu12~20.04.5, 0.6.55-0ubuntu13.3, 0.6.55-0ubuntu14.1.

**参考链接 / References**:
- http://packetstormsecurity.com/files/172848/Ubuntu-accountsservice-Double-Free-Memory-Corruption.html
- https://bugs.launchpad.net/ubuntu/+source/accountsservice/+bug/1950149
- https://ubuntu.com/security/notices/USN-5149-1
- http://packetstormsecurity.com/files/172848/Ubuntu-accountsservice-Double-Free-Memory-Corruption.html
- https://bugs.launchpad.net/ubuntu/+source/accountsservice/+bug/1950149

---

#### 665. CVE-2022-23220

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
USBView 2.1 before 2.2 allows some local users (e.g., ones logged in via SSH) to execute arbitrary code as root because certain Polkit settings (e.g., allow_any=yes) for pkexec disable the authentication requirement. Code execution can, for example, use the --gtk-module option. This affects Ubuntu, Debian, and Gentoo.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2022/01/22/1
- https://github.com/gregkh/usbview/commit/bf374fa4e5b9a756789dfd88efa93806a395463b
- https://security.gentoo.org/glsa/202310-15
- https://www.debian.org/security/2022/dsa-5052
- https://www.openwall.com/lists/oss-security/2022/01/21/1

---

#### 666. CVE-2022-40297

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
UBports Ubuntu Touch 16.04 allows the screen-unlock passcode to be used for a privileged shell via Sudo. This passcode is only four digits, far below typical length/complexity for a user account's password. NOTE: a third party states "The described attack cannot be executed as demonstrated.

**参考链接 / References**:
- https://github.com/filipkarc/PoC-ubuntutouch-pin-privesc
- https://github.com/filipkarc/PoC-ubuntutouch-pin-privesc

---

#### 667. CVE-2022-41352

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
An issue was discovered in Zimbra Collaboration (ZCS) 8.8.15 and 9.0. An attacker can upload arbitrary files through amavis via a cpio loophole (extraction to /opt/zimbra/jetty/webapps/zimbra/public) that can lead to incorrect access to any other user accounts. Zimbra recommends pax over cpio. Also, pax is in the prerequisites of Zimbra on Ubuntu; however, pax is no longer part of a default Red Hat installation after RHEL 6 (or CentOS 6). Once pax is installed, amavis automatically prefers it over cpio.

**参考链接 / References**:
- http://packetstormsecurity.com/files/169458/Zimbra-Collaboration-Suite-TAR-Path-Traversal.html
- https://forums.zimbra.org/viewtopic.php?t=71153&p=306532
- https://wiki.zimbra.com/wiki/Security_Center
- https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories
- https://www.secpod.com/blog/unpatched-rce-bug-in-zimbra-collaboration-suite-exploited-in-wild/

---

#### 668. CVE-2022-44544

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Mahara 21.04 before 21.04.7, 21.10 before 21.10.5, 22.04 before 22.04.3, and 22.10 before 22.10.0 potentially allow a PDF export to trigger a remote shell if the site is running on Ubuntu and the flag -dSAFER is not set with Ghostscript.

**参考链接 / References**:
- https://bugs.launchpad.net/mahara/+bug/1979575
- https://mahara.org/interaction/forum/topic.php?id=9198
- https://bugs.launchpad.net/mahara/+bug/1979575
- https://mahara.org/interaction/forum/topic.php?id=9198

---

#### 669. CVE-2023-1277

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
A vulnerability, which was classified as critical, was found in kylin-system-updater up to 1.4.20kord on Ubuntu Kylin. Affected is the function InstallSnap of the component Update Handler. The manipulation leads to command injection. The attack needs to be approached locally. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-222600.

**参考链接 / References**:
- https://github.com/cn-lwj/vuldb/blob/master/kylin-system-updater_vuln.md
- https://vuldb.com/?ctiid.222600
- https://vuldb.com/?id.222600
- https://github.com/cn-lwj/vuldb/blob/master/kylin-system-updater_vuln.md
- https://vuldb.com/?ctiid.222600

---

#### 670. CVE-2023-25595

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
A vulnerability exists in the ClearPass OnGuard Ubuntu agent that allows for an attacker with local Ubuntu instance access to potentially obtain sensitive information. Successful Exploitation of this vulnerability allows an attacker to retrieve information that is of a sensitive nature to the ClearPass/OnGuard environment.

**参考链接 / References**:
- https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2023-003.txt
- https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2023-003.txt

---

#### 671. CVE-2023-30549

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
Apptainer is an open source container platform for Linux. There is an ext4 use-after-free flaw that is exploitable through versions of Apptainer < 1.1.0 and installations that include apptainer-suid < 1.1.8 on older operating systems where that CVE has not been patched. That includes Red Hat Enterprise Linux 7, Debian 10 buster (unless the linux-5.10 package is installed), Ubuntu 18.04 bionic and Ubuntu 20.04 focal. Use-after-free flaws in the kernel can be used to attack the kernel for denial of service and potentially for privilege escalation.

Apptainer 1.1.8 includes a patch that by default disables mounting of extfs filesystem types in setuid-root mode, while continuing to allow mounting of extfs filesystems in non-setuid "rootless" mode using fuse2fs.

Some workarounds are possible. Either do not install apptainer-suid (for versions 1.1.0 through 1.1.7) or set `allow setuid = no` in apptainer.conf.  This requires having unprivileged user namespaces enabled and except for apptainer 1.1.x versions will disallow mounting of sif files, extfs files, and squashfs files in addition to other, less significant impacts.  (Encrypted sif files are also not supported unprivileged in apptainer 1.1.x.). Alternatively, use the `limit containers` options in apptainer.conf/singularity.conf to limit sif files to trusted users, groups, and/or paths, and set `allow container extfs = no` to disallow mounting of extfs overlay files.  The latter option by itself does not disallow mounting of extfs overlay partitions inside SIF files, so that's why the former options are also needed.

**参考链接 / References**:
- https://access.redhat.com/security/cve/cve-2022-1184
- https://github.com/apptainer/apptainer/commit/5a4964f5ba9c8d89a0e353b97f51fd607670a9f7
- https://github.com/apptainer/apptainer/releases/tag/v1.1.8
- https://github.com/apptainer/apptainer/security/advisories/GHSA-j4rf-7357-f4cg
- https://github.com/torvalds/linux/commit/2220eaf90992c11d888fe771055d4de3303

---

#### 672. CVE-2023-2612

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Jean-Baptiste Cayrou discovered that the shiftfs file system in the Ubuntu Linux kernel contained a race condition when handling inode locking in some situations. A local attacker could use this to cause a denial of service (kernel deadlock).

**参考链接 / References**:
- http://packetstormsecurity.com/files/173087/Kernel-Live-Patch-Security-Notice-LSN-0095-1.html
- https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/kinetic/commit/?id=02b47547824b1cd0d55c6744f91886f04de8947e
- https://ubuntu.com/security/CVE-2023-2612
- https://ubuntu.com/security/notices/USN-6122-1
- https://ubuntu.com/security/notices/USN-6123-1

---

#### 673. CVE-2023-24492

**严重程度 / Severity**: CRITICAL | CVSS: 9.6

**漏洞描述 / Description**:
A vulnerability has been discovered in the Citrix Secure Access client for Ubuntu which, if exploited, could allow an attacker to remotely execute code if a victim user opens an attacker-crafted link and accepts further prompts.

**参考链接 / References**:
- https://support.citrix.com/article/CTX564169/citrix-secure-access-client-for-ubuntu-security-bulletin-for-cve202324492
- https://support.citrix.com/article/CTX564169/citrix-secure-access-client-for-ubuntu-security-bulletin-for-cve202324492

---

#### 674. CVE-2023-2640

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
On Ubuntu kernels carrying both c914c0e27eb0 and "UBUNTU: SAUCE: overlayfs: Skip permission checking for trusted.overlayfs.* xattrs", an unprivileged user may set privileged extended attributes on the mounted files, leading them to be set on the upper files without the appropriate security checks.

**参考链接 / References**:
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2640
- https://lists.ubuntu.com/archives/kernel-team/2023-July/140923.html
- https://ubuntu.com/security/notices/USN-6250-1
- https://wiz.io/blog/ubuntu-overlayfs-vulnerability
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2640

---

#### 675. CVE-2023-32629

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Local privilege escalation vulnerability in Ubuntu Kernels overlayfs ovl_copy_up_meta_inode_data skip permission checks when calling ovl_do_setxattr on Ubuntu kernels

**参考链接 / References**:
- http://packetstormsecurity.com/files/174577/Kernel-Live-Patch-Security-Notice-LSN-0097-1.html
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32629
- https://lists.ubuntu.com/archives/kernel-team/2023-July/140920.html
- https://ubuntu.com/security/notices/USN-6250-1
- https://wiz.io/blog/ubuntu-overlayfs-vulnerability

---

#### 676. CVE-2023-3297

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
In Ubuntu's accountsservice an unprivileged local attacker can trigger a use-after-free vulnerability in accountsservice by sending a D-Bus message to the accounts-daemon process.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/accountsservice/+bug/2024182
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3297
- https://securitylab.github.com/advisories/GHSL-2023-139_accountsservice/
- https://ubuntu.com/security/notices/USN-6190-1
- https://bugs.launchpad.net/ubuntu/+source/accountsservice/+bug/2024182

---

#### 677. CVE-2023-45866

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
Bluetooth HID Hosts in BlueZ may permit an unauthenticated Peripheral role HID Device to initiate and establish an encrypted connection, and accept HID keyboard reports, potentially permitting injection of HID messages when no user interaction has occurred in the Central role to authorize such access. An example affected package is bluez 5.64-0ubuntu1 in Ubuntu 22.04LTS. NOTE: in some cases, a CVE-2020-0556 mitigation would have already addressed this Bluetooth HID Hosts issue.

**参考链接 / References**:
- http://changelogs.ubuntu.com/changelogs/pool/main/b/bluez/bluez_5.64-0ubuntu1/changelog
- http://seclists.org/fulldisclosure/2023/Dec/7
- http://seclists.org/fulldisclosure/2023/Dec/9
- https://bluetooth.com
- https://git.kernel.org/pub/scm/bluetooth/bluez.git/commit/profiles/input?id=25a471a83e02e1effb15d5a488b3f0085eaeb675

---

#### 678. CVE-2023-5536

**严重程度 / Severity**: MEDIUM | CVSS: 5.0

**漏洞描述 / Description**:
A feature in LXD (LP#1829071), affects the default configuration of Ubuntu Server which allows privileged users in the lxd group to escalate their privilege to root without requiring a sudo password.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5536
- https://discourse.ubuntu.com/t/easy-multi-user-lxd-setup/26215/4
- https://ubuntu.com/security/CVE-2023-5536
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071

---

#### 679. CVE-2022-4964

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Ubuntu's pipewire-pulse in snap grants microphone access even when the snap interface for audio-record is not set.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/pipewire/+bug/1995707/
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4964
- https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/1779
- https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/567
- https://bugs.launchpad.net/ubuntu/+source/pipewire/+bug/1995707/

---

#### 680. CVE-2023-48733

**严重程度 / Severity**: MEDIUM | CVSS: 6.7

**漏洞描述 / Description**:
An insecure default to allow UEFI Shell in EDK2 was left enabled in Ubuntu's EDK2. This allows an OS-resident attacker to bypass Secure Boot.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/edk2/+bug/2040137
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/2040139
- https://lists.debian.org/debian-lts-announce/2024/06/msg00028.html
- https://nvd.nist.gov/vuln/detail/CVE-2023-48733
- https://www.openwall.com/lists/oss-security/2024/02/14/4

---

#### 681. CVE-2024-0081

**严重程度 / Severity**: HIGH | CVSS: 8.6

**漏洞描述 / Description**:
NVIDIA NeMo framework for Ubuntu contains a vulnerability in tools/asr_webapp where an attacker may cause an allocation of resources without limits or throttling. A successful exploit of this vulnerability may lead to a server-side denial of service.

**参考链接 / References**:
- https://github.com/NVIDIA/NeMo/security/advisories/GHSA-x392-p65g-4rxx
- https://github.com/NVIDIA/NeMo/security/advisories/GHSA-x392-p65g-4rxx

---

#### 682. CVE-2024-35235

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
OpenPrinting CUPS is an open source printing system for Linux and other Unix-like operating systems. In versions 2.4.8 and earlier, when starting the cupsd server with a Listen configuration item pointing to a symbolic link, the cupsd process can be caused to perform an arbitrary chmod of the provided argument, providing world-writable access to the target. Given that cupsd is often running as root, this can result in the change of permission of any user or system files to be world writable. Given the aforementioned Ubuntu AppArmor context, on such systems this vulnerability is limited to those files modifiable by the cupsd process. In that specific case it was found to be possible to turn the configuration of the Listen argument into full control over the cupsd.conf and cups-files.conf configuration files. By later setting the User and Group arguments in cups-files.conf, and printing with a printer configured by PPD with a `FoomaticRIPCommandLine` argument, arbitrary user and group (not root) command execution could be achieved, which can further be used on Ubuntu systems to achieve full root command execution. Commit ff1f8a623e090dee8a8aadf12a6a4b25efac143d contains a patch for the issue.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2024/06/11/1
- http://www.openwall.com/lists/oss-security/2024/06/12/4
- http://www.openwall.com/lists/oss-security/2024/06/12/5
- https://git.launchpad.net/ubuntu/+source/apparmor/tree/profiles/apparmor.d/abstractions/user-tmp#n21
- https://github.com/OpenPrinting/cups/blob/aba917003c8de55e5bf85010f0ecf1f1ddd1408e/cups/http-addr.c#L229-L240

---

#### 683. CVE-2024-6388

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
Marco Trevisan discovered that the Ubuntu Advantage Desktop Daemon, before version 1.12, leaks the Pro token to unprivileged users by passing the token as an argument in plaintext.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-advantage-tools/+bug/2068944
- https://github.com/canonical/ubuntu-advantage-desktop-daemon/pull/24
- https://www.cve.org/CVERecord?id=CVE-2024-6388
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-advantage-tools/+bug/2068944
- https://github.com/canonical/ubuntu-advantage-desktop-daemon/pull/24

---

#### 684. CVE-2024-1724

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
In snapd versions prior to 2.62, when using AppArmor for enforcement of 
sandbox permissions, snapd failed to restrict writes to the $HOME/bin
path. In Ubuntu, when this path exists, it is automatically added to
the users PATH. An attacker who could convince a user to install a
malicious snap which used the 'home' plug could use this vulnerability
to install arbitrary scripts into the users PATH which may then be run
by the user outside of the expected snap sandbox and hence allow them
to escape confinement.

**参考链接 / References**:
- https://github.com/snapcore/snapd/commit/aa191f97713de8dc3ce3ac818539f0b976eb8ef6
- https://github.com/snapcore/snapd/pull/13689
- https://gld.mcphail.uk/posts/explaining-cve-2024-1724/
- https://github.com/snapcore/snapd/commit/aa191f97713de8dc3ce3ac818539f0b976eb8ef6
- https://github.com/snapcore/snapd/pull/13689

---

#### 685. CVE-2024-5290

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An issue was discovered in Ubuntu wpa_supplicant that resulted in loading of arbitrary shared objects, which allows a local unprivileged attacker to escalate privileges to the user that wpa_supplicant runs as (usually root).




Membership in the netdev group or access to the dbus interface of wpa_supplicant allow an unprivileged user to specify an arbitrary path to a module to be loaded by the wpa_supplicant process; other escalation paths might exist.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/wpa/+bug/2067613
- https://snyk.io/blog/abusing-ubuntu-root-privilege-escalation/
- https://ubuntu.com/security/notices/USN-6945-1

---

#### 686. CVE-2024-0115

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
NVIDIA CV-CUDA for Ubuntu 20.04, Ubuntu 22.04, and Jetpack contains a vulnerability in Python APIs where a user may cause an uncontrolled resource consumption issue by a long running CV-CUDA Python process. A successful exploit of this vulnerability may lead to denial of service and data loss.

**参考链接 / References**:
- https://nvidia.custhelp.com/app/answers/detail/a_id/5560

---

#### 687. CVE-2024-47684

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

tcp: check skb is non-NULL in tcp_rto_delta_us()

We have some machines running stock Ubuntu 20.04.6 which is their 5.4.0-174-generic
kernel that are running ceph and recently hit a null ptr dereference in
tcp_rearm_rto(). Initially hitting it from the TLP path, but then later we also
saw it getting hit from the RACK case as well. Here are examples of the oops
messages we saw in each of those cases:

Jul 26 15:05:02 rx [11061395.780353] BUG: kernel NULL pointer dereference, address: 0000000000000020
Jul 26 15:05:02 rx [11061395.787572] #PF: supervisor read access in kernel mode
Jul 26 15:05:02 rx [11061395.792971] #PF: error_code(0x0000) - not-present page
Jul 26 15:05:02 rx [11061395.798362] PGD 0 P4D 0
Jul 26 15:05:02 rx [11061395.801164] Oops: 0000 [#1] SMP NOPTI
Jul 26 15:05:02 rx [11061395.805091] CPU: 0 PID: 9180 Comm: msgr-worker-1 Tainted: G W 5.4.0-174-generic #193-Ubuntu
Jul 26 15:05:02 rx [11061395.814996] Hardware name: Supermicro SMC 2x26 os-gen8 64C NVME-Y 256G/H12SSW-NTR, BIOS 2.5.V1.2U.NVMe.UEFI 05/09/2023
Jul 26 15:05:02 rx [11061395.825952] RIP: 0010:tcp_rearm_rto+0xe4/0x160
Jul 26 15:05:02 rx [11061395.830656] Code: 87 ca 04 00 00 00 5b 41 5c 41 5d 5d c3 c3 49 8b bc 24 40 06 00 00 eb 8d 48 bb cf f7 53 e3 a5 9b c4 20 4c 89 ef e8 0c fe 0e 00 <48> 8b 78 20 48 c1 ef 03 48 89 f8 41 8b bc 24 80 04 00 00 48 f7 e3
Jul 26 15:05:02 rx [11061395.849665] RSP: 0018:ffffb75d40003e08 EFLAGS: 00010246
Jul 26 15:05:02 rx [11061395.855149] RAX: 0000000000000000 RBX: 20c49ba5e353f7cf RCX: 0000000000000000
Jul 26 15:05:02 rx [11061395.862542] RDX: 0000000062177c30 RSI: 000000000000231c RDI: ffff9874ad283a60
Jul 26 15:05:02 rx [11061395.869933] RBP: ffffb75d40003e20 R08: 0000000000000000 R09: ffff987605e20aa8
Jul 26 15:05:02 rx [11061395.877318] R10: ffffb75d40003f00 R11: ffffb75d4460f740 R12: ffff9874ad283900
Jul 26 15:05:02 rx [11061395.884710] R13: ffff9874ad283a60 R14: ffff9874ad283980 R15: ffff9874ad283d30
Jul 26 15:05:02 rx [11061395.892095] FS: 00007f1ef4a2e700(0000) GS:ffff987605e00000(0000) knlGS:0000000000000000
Jul 26 15:05:02 rx [11061395.900438] CS: 0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jul 26 15:05:02 rx [11061395.906435] CR2: 0000000000000020 CR3: 0000003e450ba003 CR4: 0000000000760ef0
Jul 26 15:05:02 rx [11061395.913822] PKRU: 55555554
Jul 26 15:05:02 rx [11061395.916786] Call Trace:
Jul 26 15:05:02 rx [11061395.919488]
Jul 26 15:05:02 rx [11061395.921765] ? show_regs.cold+0x1a/0x1f
Jul 26 15:05:02 rx [11061395.925859] ? __die+0x90/0xd9
Jul 26 15:05:02 rx [11061395.929169] ? no_context+0x196/0x380
Jul 26 15:05:02 rx [11061395.933088] ? ip6_protocol_deliver_rcu+0x4e0/0x4e0
Jul 26 15:05:02 rx [11061395.938216] ? ip6_sublist_rcv_finish+0x3d/0x50
Jul 26 15:05:02 rx [11061395.943000] ? __bad_area_nosemaphore+0x50/0x1a0
Jul 26 15:05:02 rx [11061395.947873] ? bad_area_nosemaphore+0x16/0x20
Jul 26 15:05:02 rx [11061395.952486] ? do_user_addr_fault+0x267/0x450
Jul 26 15:05:02 rx [11061395.957104] ? ipv6_list_rcv+0x112/0x140
Jul 26 15:05:02 rx [11061395.961279] ? __do_page_fault+0x58/0x90
Jul 26 15:05:02 rx [11061395.965458] ? do_page_fault+0x2c/0xe0
Jul 26 15:05:02 rx [11061395.969465] ? page_fault+0x34/0x40
Jul 26 15:05:02 rx [11061395.973217] ? tcp_rearm_rto+0xe4/0x160
Jul 26 15:05:02 rx [11061395.977313] ? tcp_rearm_rto+0xe4/0x160
Jul 26 15:05:02 rx [11061395.981408] tcp_send_loss_probe+0x10b/0x220
Jul 26 15:05:02 rx [11061395.985937] tcp_write_timer_handler+0x1b4/0x240
Jul 26 15:05:02 rx [11061395.990809] tcp_write_timer+0x9e/0xe0
Jul 26 15:05:02 rx [11061395.994814] ? tcp_write_timer_handler+0x240/0x240
Jul 26 15:05:02 rx [11061395.999866] call_timer_fn+0x32/0x130
Jul 26 15:05:02 rx [11061396.003782] __run_timers.part.0+0x180/0x280
Jul 26 15:05:02 rx [11061396.008309] ? recalibrate_cpu_khz+0x10/0x10
Jul 26 15:05:02 rx [11061396.012841] ? native_x2apic_icr_write+0x30/0x30
Jul 26 15:05:02 rx [11061396.017718] ? lapic_next_even
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/09aea49fbc7e755a915c405644f347137cdb62b0
- https://git.kernel.org/stable/c/16e0387d87fc858e34449fdf2b14ed5837f761db
- https://git.kernel.org/stable/c/570f7d8c9bf14f041152ba8353d4330ef7575915
- https://git.kernel.org/stable/c/5c4c03288a4aea705e36aa44119c13d7ee4dce99
- https://git.kernel.org/stable/c/81d18c152e3f82bacadf83bc0a471b2363b9cc18

---

#### 688. CVE-2024-49863

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

vhost/scsi: null-ptr-dereference in vhost_scsi_get_req()

Since commit 3f8ca2e115e5 ("vhost/scsi: Extract common handling code
from control queue handler") a null pointer dereference bug can be
triggered when guest sends an SCSI AN request.

In vhost_scsi_ctl_handle_vq(), `vc.target` is assigned with
`&v_req.tmf.lun[1]` within a switch-case block and is then passed to
vhost_scsi_get_req() which extracts `vc->req` and `tpg`. However, for
a `VIRTIO_SCSI_T_AN_*` request, tpg is not required, so `vc.target` is
set to NULL in this branch. Later, in vhost_scsi_get_req(),
`vc->target` is dereferenced without being checked, leading to a null
pointer dereference bug. This bug can be triggered from guest.

When this bug occurs, the vhost_worker process is killed while holding
`vq->mutex` and the corresponding tpg will remain occupied
indefinitely.

Below is the KASAN report:
Oops: general protection fault, probably for non-canonical address
0xdffffc0000000000: 0000 [#1] PREEMPT SMP KASAN NOPTI
KASAN: null-ptr-deref in range [0x0000000000000000-0x0000000000000007]
CPU: 1 PID: 840 Comm: poc Not tainted 6.10.0+ #1
Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS
1.16.3-debian-1.16.3-2 04/01/2014
RIP: 0010:vhost_scsi_get_req+0x165/0x3a0
Code: 00 fc ff df 48 89 fa 48 c1 ea 03 80 3c 02 00 0f 85 2b 02 00 00
48 b8 00 00 00 00 00 fc ff df 4d 8b 65 30 4c 89 e2 48 c1 ea 03 <0f> b6
04 02 4c 89 e2 83 e2 07 38 d0 7f 08 84 c0 0f 85 be 01 00 00
RSP: 0018:ffff888017affb50 EFLAGS: 00010246
RAX: dffffc0000000000 RBX: ffff88801b000000 RCX: 0000000000000000
RDX: 0000000000000000 RSI: 0000000000000000 RDI: ffff888017affcb8
RBP: ffff888017affb80 R08: 0000000000000000 R09: 0000000000000000
R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000
R13: ffff888017affc88 R14: ffff888017affd1c R15: ffff888017993000
FS:  000055556e076500(0000) GS:ffff88806b100000(0000) knlGS:0000000000000000
CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
CR2: 00000000200027c0 CR3: 0000000010ed0004 CR4: 0000000000370ef0
Call Trace:
 <TASK>
 ? show_regs+0x86/0xa0
 ? die_addr+0x4b/0xd0
 ? exc_general_protection+0x163/0x260
 ? asm_exc_general_protection+0x27/0x30
 ? vhost_scsi_get_req+0x165/0x3a0
 vhost_scsi_ctl_handle_vq+0x2a4/0xca0
 ? __pfx_vhost_scsi_ctl_handle_vq+0x10/0x10
 ? __switch_to+0x721/0xeb0
 ? __schedule+0xda5/0x5710
 ? __kasan_check_write+0x14/0x30
 ? _raw_spin_lock+0x82/0xf0
 vhost_scsi_ctl_handle_kick+0x52/0x90
 vhost_run_work_list+0x134/0x1b0
 vhost_task_fn+0x121/0x350
...
 </TASK>
---[ end trace 0000000000000000 ]---

Let's add a check in vhost_scsi_get_req.

[whitespace fixes]

**参考链接 / References**:
- https://git.kernel.org/stable/c/00fb5b23e1c9cdbe496f5cd6b40367cb895f6c93
- https://git.kernel.org/stable/c/221af82f606d928ccef19a16d35633c63026f1be
- https://git.kernel.org/stable/c/25613e6d9841a1f9fb985be90df921fa99f800de
- https://git.kernel.org/stable/c/46128370a72c431df733af5ebb065c4d48c9ad39
- https://git.kernel.org/stable/c/61517f33e76d2c5247c1e61e668693afe5b67e6f

---

#### 689. CVE-2024-11586

**严重程度 / Severity**: MEDIUM | CVSS: 4.0

**漏洞描述 / Description**:
Ubuntu's implementation of pulseaudio can be crashed by a malicious program if a bluetooth headset is connected.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/2078822
- https://www.cve.org/CVERecord?id=CVE-2024-11586

---

#### 690. CVE-2022-1736

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Ubuntu's configuration of gnome-control-center allowed Remote Desktop Sharing to be enabled by default.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/gnome-remote-desktop/+bug/1973028
- https://ubuntu.com/security/CVE-2022-1736
- https://ubuntu.com/security/notices/USN-5430-1

---

#### 691. CVE-2022-49666

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

powerpc/memhotplug: Add add_pages override for PPC

With commit ffa0b64e3be5 ("powerpc: Fix virt_addr_valid() for 64-bit Book3E & 32-bit")
the kernel now validate the addr against high_memory value. This results
in the below BUG_ON with dax pfns.

[  635.798741][T26531] kernel BUG at mm/page_alloc.c:5521!
1:mon> e
cpu 0x1: Vector: 700 (Program Check) at [c000000007287630]
    pc: c00000000055ed48: free_pages.part.0+0x48/0x110
    lr: c00000000053ca70: tlb_finish_mmu+0x80/0xd0
    sp: c0000000072878d0
   msr: 800000000282b033
  current = 0xc00000000afabe00
  paca    = 0xc00000037ffff300   irqmask: 0x03   irq_happened: 0x05
    pid   = 26531, comm = 50-landscape-sy
kernel BUG at :5521!
Linux version 5.19.0-rc3-14659-g4ec05be7c2e1 (kvaneesh@ltc-boston8) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #625 SMP Thu Jun 23 00:35:43 CDT 2022
1:mon> t
[link register   ] c00000000053ca70 tlb_finish_mmu+0x80/0xd0
[c0000000072878d0] c00000000053ca54 tlb_finish_mmu+0x64/0xd0 (unreliable)
[c000000007287900] c000000000539424 exit_mmap+0xe4/0x2a0
[c0000000072879e0] c00000000019fc1c mmput+0xcc/0x210
[c000000007287a20] c000000000629230 begin_new_exec+0x5e0/0xf40
[c000000007287ae0] c00000000070b3cc load_elf_binary+0x3ac/0x1e00
[c000000007287c10] c000000000627af0 bprm_execve+0x3b0/0xaf0
[c000000007287cd0] c000000000628414 do_execveat_common.isra.0+0x1e4/0x310
[c000000007287d80] c00000000062858c sys_execve+0x4c/0x60
[c000000007287db0] c00000000002c1b0 system_call_exception+0x160/0x2c0
[c000000007287e10] c00000000000c53c system_call_common+0xec/0x250

The fix is to make sure we update high_memory on memory hotplug.
This is similar to what x86 does in commit 3072e413e305 ("mm/memory_hotplug: introduce add_pages")

**参考链接 / References**:
- https://git.kernel.org/stable/c/84d146fd35a01b08e9515041de60f0f915a417d5
- https://git.kernel.org/stable/c/89296ac435e2cf8a5101f7fab8f0c7b754b92052
- https://git.kernel.org/stable/c/ac790d09885d36143076e7e02825c541e8eee899

---

#### 692. CVE-2023-5616

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
In Ubuntu, gnome-control-center did not properly reflect SSH remote login status when the system was configured to use systemd socket activation for openssh-server. This could unknowingly leave the local machine exposed to remote SSH access contrary to expectation of the user.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/gnome-control-center/+bug/2039577
- https://ubuntu.com/security/CVE-2023-5616
- https://ubuntu.com/security/notices/USN-6554-1

---

#### 693. CVE-2025-37904

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

btrfs: fix the inode leak in btrfs_iget()

[BUG]
There is a bug report that a syzbot reproducer can lead to the following
busy inode at unmount time:

  BTRFS info (device loop1): last unmount of filesystem 1680000e-3c1e-4c46-84b6-56bd3909af50
  VFS: Busy inodes after unmount of loop1 (btrfs)
  ------------[ cut here ]------------
  kernel BUG at fs/super.c:650!
  Oops: invalid opcode: 0000 [#1] SMP KASAN NOPTI
  CPU: 0 UID: 0 PID: 48168 Comm: syz-executor Not tainted 6.15.0-rc2-00471-g119009db2674 #2 PREEMPT(full)
  Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
  RIP: 0010:generic_shutdown_super+0x2e9/0x390 fs/super.c:650
  Call Trace:
   <TASK>
   kill_anon_super+0x3a/0x60 fs/super.c:1237
   btrfs_kill_super+0x3b/0x50 fs/btrfs/super.c:2099
   deactivate_locked_super+0xbe/0x1a0 fs/super.c:473
   deactivate_super fs/super.c:506 [inline]
   deactivate_super+0xe2/0x100 fs/super.c:502
   cleanup_mnt+0x21f/0x440 fs/namespace.c:1435
   task_work_run+0x14d/0x240 kernel/task_work.c:227
   resume_user_mode_work include/linux/resume_user_mode.h:50 [inline]
   exit_to_user_mode_loop kernel/entry/common.c:114 [inline]
   exit_to_user_mode_prepare include/linux/entry-common.h:329 [inline]
   __syscall_exit_to_user_mode_work kernel/entry/common.c:207 [inline]
   syscall_exit_to_user_mode+0x269/0x290 kernel/entry/common.c:218
   do_syscall_64+0xd4/0x250 arch/x86/entry/syscall_64.c:100
   entry_SYSCALL_64_after_hwframe+0x77/0x7f
   </TASK>

[CAUSE]
When btrfs_alloc_path() failed, btrfs_iget() directly returned without
releasing the inode already allocated by btrfs_iget_locked().

This results the above busy inode and trigger the kernel BUG.

[FIX]
Fix it by calling iget_failed() if btrfs_alloc_path() failed.

If we hit error inside btrfs_read_locked_inode(), it will properly call
iget_failed(), so nothing to worry about.

Although the iget_failed() cleanup inside btrfs_read_locked_inode() is a
break of the normal error handling scheme, let's fix the obvious bug
and backport first, then rework the error handling later.

**参考链接 / References**:
- https://git.kernel.org/stable/c/30a339bece3a44ab0a821477139e84fb86af9761
- https://git.kernel.org/stable/c/48c1d1bb525b1c44b8bdc8e7ec5629cb6c2b9fc4

---

#### 694. CVE-2025-38032

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

mr: consolidate the ipmr_can_free_table() checks.

Guoyu Yin reported a splat in the ipmr netns cleanup path:

WARNING: CPU: 2 PID: 14564 at net/ipv4/ipmr.c:440 ipmr_free_table net/ipv4/ipmr.c:440 [inline]
WARNING: CPU: 2 PID: 14564 at net/ipv4/ipmr.c:440 ipmr_rules_exit+0x135/0x1c0 net/ipv4/ipmr.c:361
Modules linked in:
CPU: 2 UID: 0 PID: 14564 Comm: syz.4.838 Not tainted 6.14.0 #1
Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
RIP: 0010:ipmr_free_table net/ipv4/ipmr.c:440 [inline]
RIP: 0010:ipmr_rules_exit+0x135/0x1c0 net/ipv4/ipmr.c:361
Code: ff df 48 c1 ea 03 80 3c 02 00 75 7d 48 c7 83 60 05 00 00 00 00 00 00 5b 5d 41 5c 41 5d 41 5e e9 71 67 7f 00 e8 4c 2d 8a fd 90 <0f> 0b 90 eb 93 e8 41 2d 8a fd 0f b6 2d 80 54 ea 01 31 ff 89 ee e8
RSP: 0018:ffff888109547c58 EFLAGS: 00010293
RAX: 0000000000000000 RBX: ffff888108c12dc0 RCX: ffffffff83e09868
RDX: ffff8881022b3300 RSI: ffffffff83e098d4 RDI: 0000000000000005
RBP: ffff888104288000 R08: 0000000000000000 R09: ffffed10211825c9
R10: 0000000000000001 R11: ffff88801816c4a0 R12: 0000000000000001
R13: ffff888108c13320 R14: ffff888108c12dc0 R15: fffffbfff0b74058
FS:  00007f84f39316c0(0000) GS:ffff88811b100000(0000) knlGS:0000000000000000
CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
CR2: 00007f84f3930f98 CR3: 0000000113b56000 CR4: 0000000000350ef0
Call Trace:
 <TASK>
 ipmr_net_exit_batch+0x50/0x90 net/ipv4/ipmr.c:3160
 ops_exit_list+0x10c/0x160 net/core/net_namespace.c:177
 setup_net+0x47d/0x8e0 net/core/net_namespace.c:394
 copy_net_ns+0x25d/0x410 net/core/net_namespace.c:516
 create_new_namespaces+0x3f6/0xaf0 kernel/nsproxy.c:110
 unshare_nsproxy_namespaces+0xc3/0x180 kernel/nsproxy.c:228
 ksys_unshare+0x78d/0x9a0 kernel/fork.c:3342
 __do_sys_unshare kernel/fork.c:3413 [inline]
 __se_sys_unshare kernel/fork.c:3411 [inline]
 __x64_sys_unshare+0x31/0x40 kernel/fork.c:3411
 do_syscall_x64 arch/x86/entry/common.c:52 [inline]
 do_syscall_64+0xa6/0x1a0 arch/x86/entry/common.c:83
 entry_SYSCALL_64_after_hwframe+0x77/0x7f
RIP: 0033:0x7f84f532cc29
Code: ff ff c3 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 40 00 48 89 f8 48 89 f7 48 89 d6 48 89 ca 4d 89 c2 4d 89 c8 4c 8b 4c 24 08 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 c7 c1 a8 ff ff ff f7 d8 64 89 01 48
RSP: 002b:00007f84f3931038 EFLAGS: 00000246 ORIG_RAX: 0000000000000110
RAX: ffffffffffffffda RBX: 00007f84f5615fa0 RCX: 00007f84f532cc29
RDX: 0000000000000000 RSI: 0000000000000000 RDI: 0000000040000400
RBP: 00007f84f53fba18 R08: 0000000000000000 R09: 0000000000000000
R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
R13: 0000000000000000 R14: 00007f84f5615fa0 R15: 00007fff51c5f328
 </TASK>

The running kernel has CONFIG_IP_MROUTE_MULTIPLE_TABLES disabled, and
the sanity check for such build is still too loose.

Address the issue consolidating the relevant sanity check in a single
helper regardless of the kernel configuration. Also share it between
the ipv4 and ipv6 code.

**参考链接 / References**:
- https://git.kernel.org/stable/c/1c518ae98302ab37786d5ba5d43e9ac6d6f894e3
- https://git.kernel.org/stable/c/c46286fdd6aa1d0e33c245bcffe9ff2428a777bd

---

#### 695. CVE-2025-38106

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

io_uring: fix use-after-free of sq->thread in __io_uring_show_fdinfo()

syzbot reports:

BUG: KASAN: slab-use-after-free in getrusage+0x1109/0x1a60
Read of size 8 at addr ffff88810de2d2c8 by task a.out/304

CPU: 0 UID: 0 PID: 304 Comm: a.out Not tainted 6.16.0-rc1 #1 PREEMPT(voluntary)
Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
Call Trace:
 <TASK>
 dump_stack_lvl+0x53/0x70
 print_report+0xd0/0x670
 ? __pfx__raw_spin_lock_irqsave+0x10/0x10
 ? getrusage+0x1109/0x1a60
 kasan_report+0xce/0x100
 ? getrusage+0x1109/0x1a60
 getrusage+0x1109/0x1a60
 ? __pfx_getrusage+0x10/0x10
 __io_uring_show_fdinfo+0x9fe/0x1790
 ? ksys_read+0xf7/0x1c0
 ? do_syscall_64+0xa4/0x260
 ? vsnprintf+0x591/0x1100
 ? __pfx___io_uring_show_fdinfo+0x10/0x10
 ? __pfx_vsnprintf+0x10/0x10
 ? mutex_trylock+0xcf/0x130
 ? __pfx_mutex_trylock+0x10/0x10
 ? __pfx_show_fd_locks+0x10/0x10
 ? io_uring_show_fdinfo+0x57/0x80
 io_uring_show_fdinfo+0x57/0x80
 seq_show+0x38c/0x690
 seq_read_iter+0x3f7/0x1180
 ? inode_set_ctime_current+0x160/0x4b0
 seq_read+0x271/0x3e0
 ? __pfx_seq_read+0x10/0x10
 ? __pfx__raw_spin_lock+0x10/0x10
 ? __mark_inode_dirty+0x402/0x810
 ? selinux_file_permission+0x368/0x500
 ? file_update_time+0x10f/0x160
 vfs_read+0x177/0xa40
 ? __pfx___handle_mm_fault+0x10/0x10
 ? __pfx_vfs_read+0x10/0x10
 ? mutex_lock+0x81/0xe0
 ? __pfx_mutex_lock+0x10/0x10
 ? fdget_pos+0x24d/0x4b0
 ksys_read+0xf7/0x1c0
 ? __pfx_ksys_read+0x10/0x10
 ? do_user_addr_fault+0x43b/0x9c0
 do_syscall_64+0xa4/0x260
 entry_SYSCALL_64_after_hwframe+0x77/0x7f
RIP: 0033:0x7f0f74170fc9
Code: 00 c3 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 44 00 00 48 89 f8 48 89 f7 48 89 d6 48 89 ca 4d 89 c2 4d 89 c8 4c 8b 4c 24 08 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 8
RSP: 002b:00007fffece049e8 EFLAGS: 00000206 ORIG_RAX: 0000000000000000
RAX: ffffffffffffffda RBX: 0000000000000000 RCX: 00007f0f74170fc9
RDX: 0000000000001000 RSI: 00007fffece049f0 RDI: 0000000000000004
RBP: 00007fffece05ad0 R08: 0000000000000000 R09: 00007fffece04d90
R10: 0000000000000000 R11: 0000000000000206 R12: 00005651720a1100
R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000000
 </TASK>

Allocated by task 298:
 kasan_save_stack+0x33/0x60
 kasan_save_track+0x14/0x30
 __kasan_slab_alloc+0x6e/0x70
 kmem_cache_alloc_node_noprof+0xe8/0x330
 copy_process+0x376/0x5e00
 create_io_thread+0xab/0xf0
 io_sq_offload_create+0x9ed/0xf20
 io_uring_setup+0x12b0/0x1cc0
 do_syscall_64+0xa4/0x260
 entry_SYSCALL_64_after_hwframe+0x77/0x7f

Freed by task 22:
 kasan_save_stack+0x33/0x60
 kasan_save_track+0x14/0x30
 kasan_save_free_info+0x3b/0x60
 __kasan_slab_free+0x37/0x50
 kmem_cache_free+0xc4/0x360
 rcu_core+0x5ff/0x19f0
 handle_softirqs+0x18c/0x530
 run_ksoftirqd+0x20/0x30
 smpboot_thread_fn+0x287/0x6c0
 kthread+0x30d/0x630
 ret_from_fork+0xef/0x1a0
 ret_from_fork_asm+0x1a/0x30

Last potentially related work creation:
 kasan_save_stack+0x33/0x60
 kasan_record_aux_stack+0x8c/0xa0
 __call_rcu_common.constprop.0+0x68/0x940
 __schedule+0xff2/0x2930
 __cond_resched+0x4c/0x80
 mutex_lock+0x5c/0xe0
 io_uring_del_tctx_node+0xe1/0x2b0
 io_uring_clean_tctx+0xb7/0x160
 io_uring_cancel_generic+0x34e/0x760
 do_exit+0x240/0x2350
 do_group_exit+0xab/0x220
 __x64_sys_exit_group+0x39/0x40
 x64_sys_call+0x1243/0x1840
 do_syscall_64+0xa4/0x260
 entry_SYSCALL_64_after_hwframe+0x77/0x7f

The buggy address belongs to the object at ffff88810de2cb00
 which belongs to the cache task_struct of size 3712
The buggy address is located 1992 bytes inside of
 freed 3712-byte region [ffff88810de2cb00, ffff88810de2d980)

which is caused by the task_struct pointed to by sq->thread being
released while it is being used in the function
__io_uring_show_fdinfo(). Holding ctx->uring_lock does not prevent ehre
relase or exit of sq->thread.

Fix this by assigning and looking up ->thread under RCU, and grabbing a
reference to the task_struct. This e
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/ac0b8b327a5677dc6fecdf353d808161525b1ff0
- https://git.kernel.org/stable/c/af8c13f9ee040b9a287ba246cf0055f7c77b7cc8
- https://git.kernel.org/stable/c/d0932758a0a77b38ba1b39564f3b7aba12407061

---

#### 696. CVE-2025-38184

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

tipc: fix null-ptr-deref when acquiring remote ip of ethernet bearer

The reproduction steps:
1. create a tun interface
2. enable l2 bearer
3. TIPC_NL_UDP_GET_REMOTEIP with media name set to tun

tipc: Started in network mode
tipc: Node identity 8af312d38a21, cluster identity 4711
tipc: Enabled bearer <eth:syz_tun>, priority 1
Oops: general protection fault
KASAN: null-ptr-deref in range
CPU: 1 UID: 1000 PID: 559 Comm: poc Not tainted 6.16.0-rc1+ #117 PREEMPT
Hardware name: QEMU Ubuntu 24.04 PC
RIP: 0010:tipc_udp_nl_dump_remoteip+0x4a4/0x8f0

the ub was in fact a struct dev.

when bid != 0 && skip_cnt != 0, bearer_list[bid] may be NULL or
other media when other thread changes it.

fix this by checking media_id.

**参考链接 / References**:
- https://git.kernel.org/stable/c/05d332ba075753d569d66333d62d60fff5f57ad8
- https://git.kernel.org/stable/c/0d3d91c3500f0c480e016faa4e2259c588616e59
- https://git.kernel.org/stable/c/0f4a72fb266e48dbe928e1d936eab149e4ac3e1b
- https://git.kernel.org/stable/c/3998283e4c32c0fe69edd59b0876c193f50abce6
- https://git.kernel.org/stable/c/8595350615f952fcf8bc861464a6bf6b1129af50

---

#### 697. CVE-2025-38491

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

mptcp: make fallback action and fallback decision atomic

Syzkaller reported the following splat:

  WARNING: CPU: 1 PID: 7704 at net/mptcp/protocol.h:1223 __mptcp_do_fallback net/mptcp/protocol.h:1223 [inline]
  WARNING: CPU: 1 PID: 7704 at net/mptcp/protocol.h:1223 mptcp_do_fallback net/mptcp/protocol.h:1244 [inline]
  WARNING: CPU: 1 PID: 7704 at net/mptcp/protocol.h:1223 check_fully_established net/mptcp/options.c:982 [inline]
  WARNING: CPU: 1 PID: 7704 at net/mptcp/protocol.h:1223 mptcp_incoming_options+0x21a8/0x2510 net/mptcp/options.c:1153
  Modules linked in:
  CPU: 1 UID: 0 PID: 7704 Comm: syz.3.1419 Not tainted 6.16.0-rc3-gbd5ce2324dba #20 PREEMPT(voluntary)
  Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
  RIP: 0010:__mptcp_do_fallback net/mptcp/protocol.h:1223 [inline]
  RIP: 0010:mptcp_do_fallback net/mptcp/protocol.h:1244 [inline]
  RIP: 0010:check_fully_established net/mptcp/options.c:982 [inline]
  RIP: 0010:mptcp_incoming_options+0x21a8/0x2510 net/mptcp/options.c:1153
  Code: 24 18 e8 bb 2a 00 fd e9 1b df ff ff e8 b1 21 0f 00 e8 ec 5f c4 fc 44 0f b7 ac 24 b0 00 00 00 e9 54 f1 ff ff e8 d9 5f c4 fc 90 <0f> 0b 90 e9 b8 f4 ff ff e8 8b 2a 00 fd e9 8d e6 ff ff e8 81 2a 00
  RSP: 0018:ffff8880a3f08448 EFLAGS: 00010246
  RAX: 0000000000000000 RBX: ffff8880180a8000 RCX: ffffffff84afcf45
  RDX: ffff888090223700 RSI: ffffffff84afdaa7 RDI: 0000000000000001
  RBP: ffff888017955780 R08: 0000000000000001 R09: 0000000000000000
  R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000
  R13: ffff8880180a8910 R14: ffff8880a3e9d058 R15: 0000000000000000
  FS:  00005555791b8500(0000) GS:ffff88811c495000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 000000110c2800b7 CR3: 0000000058e44000 CR4: 0000000000350ef0
  Call Trace:
   <IRQ>
   tcp_reset+0x26f/0x2b0 net/ipv4/tcp_input.c:4432
   tcp_validate_incoming+0x1057/0x1b60 net/ipv4/tcp_input.c:5975
   tcp_rcv_established+0x5b5/0x21f0 net/ipv4/tcp_input.c:6166
   tcp_v4_do_rcv+0x5dc/0xa70 net/ipv4/tcp_ipv4.c:1925
   tcp_v4_rcv+0x3473/0x44a0 net/ipv4/tcp_ipv4.c:2363
   ip_protocol_deliver_rcu+0xba/0x480 net/ipv4/ip_input.c:205
   ip_local_deliver_finish+0x2f1/0x500 net/ipv4/ip_input.c:233
   NF_HOOK include/linux/netfilter.h:317 [inline]
   NF_HOOK include/linux/netfilter.h:311 [inline]
   ip_local_deliver+0x1be/0x560 net/ipv4/ip_input.c:254
   dst_input include/net/dst.h:469 [inline]
   ip_rcv_finish net/ipv4/ip_input.c:447 [inline]
   NF_HOOK include/linux/netfilter.h:317 [inline]
   NF_HOOK include/linux/netfilter.h:311 [inline]
   ip_rcv+0x514/0x810 net/ipv4/ip_input.c:567
   __netif_receive_skb_one_core+0x197/0x1e0 net/core/dev.c:5975
   __netif_receive_skb+0x1f/0x120 net/core/dev.c:6088
   process_backlog+0x301/0x1360 net/core/dev.c:6440
   __napi_poll.constprop.0+0xba/0x550 net/core/dev.c:7453
   napi_poll net/core/dev.c:7517 [inline]
   net_rx_action+0xb44/0x1010 net/core/dev.c:7644
   handle_softirqs+0x1d0/0x770 kernel/softirq.c:579
   do_softirq+0x3f/0x90 kernel/softirq.c:480
   </IRQ>
   <TASK>
   __local_bh_enable_ip+0xed/0x110 kernel/softirq.c:407
   local_bh_enable include/linux/bottom_half.h:33 [inline]
   inet_csk_listen_stop+0x2c5/0x1070 net/ipv4/inet_connection_sock.c:1524
   mptcp_check_listen_stop.part.0+0x1cc/0x220 net/mptcp/protocol.c:2985
   mptcp_check_listen_stop net/mptcp/mib.h:118 [inline]
   __mptcp_close+0x9b9/0xbd0 net/mptcp/protocol.c:3000
   mptcp_close+0x2f/0x140 net/mptcp/protocol.c:3066
   inet_release+0xed/0x200 net/ipv4/af_inet.c:435
   inet6_release+0x4f/0x70 net/ipv6/af_inet6.c:487
   __sock_release+0xb3/0x270 net/socket.c:649
   sock_close+0x1c/0x30 net/socket.c:1439
   __fput+0x402/0xb70 fs/file_table.c:465
   task_work_run+0x150/0x240 kernel/task_work.c:227
   resume_user_mode_work include/linux/resume_user_mode.h:50 [inline]
   exit_to_user_mode_loop+0xd4
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/1d82a8fe6ee4afdc92f4e8808c9dad2a6095bbc5
- https://git.kernel.org/stable/c/54999dea879fecb761225e28f274b40662918c30
- https://git.kernel.org/stable/c/5586518bec27666c747cd52aabb62d485686d0bf
- https://git.kernel.org/stable/c/75a4c9ab8a7af0d76b31ccd1188ed178c38b35d2
- https://git.kernel.org/stable/c/f8a1d9b18c5efc76784f5a326e905f641f839894

---

#### 698. CVE-2025-38500

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

xfrm: interface: fix use-after-free after changing collect_md xfrm interface

collect_md property on xfrm interfaces can only be set on device creation,
thus xfrmi_changelink() should fail when called on such interfaces.

The check to enforce this was done only in the case where the xi was
returned from xfrmi_locate() which doesn't look for the collect_md
interface, and thus the validation was never reached.

Calling changelink would thus errornously place the special interface xi
in the xfrmi_net->xfrmi hash, but since it also exists in the
xfrmi_net->collect_md_xfrmi pointer it would lead to a double free when
the net namespace was taken down [1].

Change the check to use the xi from netdev_priv which is available earlier
in the function to prevent changes in xfrm collect_md interfaces.

[1] resulting oops:
[    8.516540] kernel BUG at net/core/dev.c:12029!
[    8.516552] Oops: invalid opcode: 0000 [#1] SMP NOPTI
[    8.516559] CPU: 0 UID: 0 PID: 12 Comm: kworker/u80:0 Not tainted 6.15.0-virtme #5 PREEMPT(voluntary)
[    8.516565] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[    8.516569] Workqueue: netns cleanup_net
[    8.516579] RIP: 0010:unregister_netdevice_many_notify+0x101/0xab0
[    8.516590] Code: 90 0f 0b 90 48 8b b0 78 01 00 00 48 8b 90 80 01 00 00 48 89 56 08 48 89 32 4c 89 80 78 01 00 00 48 89 b8 80 01 00 00 eb ac 90 <0f> 0b 48 8b 45 00 4c 8d a0 88 fe ff ff 48 39 c5 74 5c 41 80 bc 24
[    8.516593] RSP: 0018:ffffa93b8006bd30 EFLAGS: 00010206
[    8.516598] RAX: ffff98fe4226e000 RBX: ffffa93b8006bd58 RCX: ffffa93b8006bc60
[    8.516601] RDX: 0000000000000004 RSI: 0000000000000000 RDI: dead000000000122
[    8.516603] RBP: ffffa93b8006bdd8 R08: dead000000000100 R09: ffff98fe4133c100
[    8.516605] R10: 0000000000000000 R11: 00000000000003d2 R12: ffffa93b8006be00
[    8.516608] R13: ffffffff96c1a510 R14: ffffffff96c1a510 R15: ffffa93b8006be00
[    8.516615] FS:  0000000000000000(0000) GS:ffff98fee73b7000(0000) knlGS:0000000000000000
[    8.516619] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[    8.516622] CR2: 00007fcd2abd0700 CR3: 000000003aa40000 CR4: 0000000000752ef0
[    8.516625] PKRU: 55555554
[    8.516627] Call Trace:
[    8.516632]  <TASK>
[    8.516635]  ? rtnl_is_locked+0x15/0x20
[    8.516641]  ? unregister_netdevice_queue+0x29/0xf0
[    8.516650]  ops_undo_list+0x1f2/0x220
[    8.516659]  cleanup_net+0x1ad/0x2e0
[    8.516664]  process_one_work+0x160/0x380
[    8.516673]  worker_thread+0x2aa/0x3c0
[    8.516679]  ? __pfx_worker_thread+0x10/0x10
[    8.516686]  kthread+0xfb/0x200
[    8.516690]  ? __pfx_kthread+0x10/0x10
[    8.516693]  ? __pfx_kthread+0x10/0x10
[    8.516697]  ret_from_fork+0x82/0xf0
[    8.516705]  ? __pfx_kthread+0x10/0x10
[    8.516709]  ret_from_fork_asm+0x1a/0x30
[    8.516718]  </TASK>

**参考链接 / References**:
- https://git.kernel.org/stable/c/5918c3f4800a3aef2173865e5903370f21e24f47
- https://git.kernel.org/stable/c/69a31f7a6a81f5ffd3812c442e09ff0be22960f1
- https://git.kernel.org/stable/c/a8d4748b954584ab7bd800f1a4e46d5b0eeb5ce4
- https://git.kernel.org/stable/c/a90b2a1aaacbcf0f91d7e4868ad6c51c5dee814b
- https://git.kernel.org/stable/c/bfebdb85496e1da21d3cf05de099210915c3e706

---

#### 699. CVE-2025-38713

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfsplus: fix slab-out-of-bounds read in hfsplus_uni2asc()

The hfsplus_readdir() method is capable to crash by calling
hfsplus_uni2asc():

[  667.121659][ T9805] ==================================================================
[  667.122651][ T9805] BUG: KASAN: slab-out-of-bounds in hfsplus_uni2asc+0x902/0xa10
[  667.123627][ T9805] Read of size 2 at addr ffff88802592f40c by task repro/9805
[  667.124578][ T9805]
[  667.124876][ T9805] CPU: 3 UID: 0 PID: 9805 Comm: repro Not tainted 6.16.0-rc3 #1 PREEMPT(full)
[  667.124886][ T9805] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[  667.124890][ T9805] Call Trace:
[  667.124893][ T9805]  <TASK>
[  667.124896][ T9805]  dump_stack_lvl+0x10e/0x1f0
[  667.124911][ T9805]  print_report+0xd0/0x660
[  667.124920][ T9805]  ? __virt_addr_valid+0x81/0x610
[  667.124928][ T9805]  ? __phys_addr+0xe8/0x180
[  667.124934][ T9805]  ? hfsplus_uni2asc+0x902/0xa10
[  667.124942][ T9805]  kasan_report+0xc6/0x100
[  667.124950][ T9805]  ? hfsplus_uni2asc+0x902/0xa10
[  667.124959][ T9805]  hfsplus_uni2asc+0x902/0xa10
[  667.124966][ T9805]  ? hfsplus_bnode_read+0x14b/0x360
[  667.124974][ T9805]  hfsplus_readdir+0x845/0xfc0
[  667.124984][ T9805]  ? __pfx_hfsplus_readdir+0x10/0x10
[  667.124994][ T9805]  ? stack_trace_save+0x8e/0xc0
[  667.125008][ T9805]  ? iterate_dir+0x18b/0xb20
[  667.125015][ T9805]  ? trace_lock_acquire+0x85/0xd0
[  667.125022][ T9805]  ? lock_acquire+0x30/0x80
[  667.125029][ T9805]  ? iterate_dir+0x18b/0xb20
[  667.125037][ T9805]  ? down_read_killable+0x1ed/0x4c0
[  667.125044][ T9805]  ? putname+0x154/0x1a0
[  667.125051][ T9805]  ? __pfx_down_read_killable+0x10/0x10
[  667.125058][ T9805]  ? apparmor_file_permission+0x239/0x3e0
[  667.125069][ T9805]  iterate_dir+0x296/0xb20
[  667.125076][ T9805]  __x64_sys_getdents64+0x13c/0x2c0
[  667.125084][ T9805]  ? __pfx___x64_sys_getdents64+0x10/0x10
[  667.125091][ T9805]  ? __x64_sys_openat+0x141/0x200
[  667.125126][ T9805]  ? __pfx_filldir64+0x10/0x10
[  667.125134][ T9805]  ? do_user_addr_fault+0x7fe/0x12f0
[  667.125143][ T9805]  do_syscall_64+0xc9/0x480
[  667.125151][ T9805]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  667.125158][ T9805] RIP: 0033:0x7fa8753b2fc9
[  667.125164][ T9805] Code: 00 c3 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 44 00 00 48 89 f8 48 89 f7 48 89 d6 48 89 ca 4d 89 c2 48
[  667.125172][ T9805] RSP: 002b:00007ffe96f8e0f8 EFLAGS: 00000217 ORIG_RAX: 00000000000000d9
[  667.125181][ T9805] RAX: ffffffffffffffda RBX: 0000000000000000 RCX: 00007fa8753b2fc9
[  667.125185][ T9805] RDX: 0000000000000400 RSI: 00002000000063c0 RDI: 0000000000000004
[  667.125190][ T9805] RBP: 00007ffe96f8e110 R08: 00007ffe96f8e110 R09: 00007ffe96f8e110
[  667.125195][ T9805] R10: 0000000000000000 R11: 0000000000000217 R12: 0000556b1e3b4260
[  667.125199][ T9805] R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000000
[  667.125207][ T9805]  </TASK>
[  667.125210][ T9805]
[  667.145632][ T9805] Allocated by task 9805:
[  667.145991][ T9805]  kasan_save_stack+0x20/0x40
[  667.146352][ T9805]  kasan_save_track+0x14/0x30
[  667.146717][ T9805]  __kasan_kmalloc+0xaa/0xb0
[  667.147065][ T9805]  __kmalloc_noprof+0x205/0x550
[  667.147448][ T9805]  hfsplus_find_init+0x95/0x1f0
[  667.147813][ T9805]  hfsplus_readdir+0x220/0xfc0
[  667.148174][ T9805]  iterate_dir+0x296/0xb20
[  667.148549][ T9805]  __x64_sys_getdents64+0x13c/0x2c0
[  667.148937][ T9805]  do_syscall_64+0xc9/0x480
[  667.149291][ T9805]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  667.149809][ T9805]
[  667.150030][ T9805] The buggy address belongs to the object at ffff88802592f000
[  667.150030][ T9805]  which belongs to the cache kmalloc-2k of size 2048
[  667.151282][ T9805] The buggy address is located 0 bytes to the right of
[  667.151282][ T9805]  allocated 1036-byte region [ffff88802592f000, ffff88802592f40c)
[  667.1
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/13604b1d7e7b125fb428cddbec6b8d92baad25d5
- https://git.kernel.org/stable/c/1ca69007e52a73bd8b84b988b61b319816ca8b01
- https://git.kernel.org/stable/c/291bb5d931c6f3cd7227b913302a17be21cf53b0
- https://git.kernel.org/stable/c/6f93694bcbc2c2ab3e01cd8fba2f296faf34e6b9
- https://git.kernel.org/stable/c/73f7da507d787b489761a0fa280716f84fa32b2f

---

#### 700. CVE-2025-38714

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfsplus: fix slab-out-of-bounds in hfsplus_bnode_read()

The hfsplus_bnode_read() method can trigger the issue:

[  174.852007][ T9784] ==================================================================
[  174.852709][ T9784] BUG: KASAN: slab-out-of-bounds in hfsplus_bnode_read+0x2f4/0x360
[  174.853412][ T9784] Read of size 8 at addr ffff88810b5fc6c0 by task repro/9784
[  174.854059][ T9784]
[  174.854272][ T9784] CPU: 1 UID: 0 PID: 9784 Comm: repro Not tainted 6.16.0-rc3 #7 PREEMPT(full)
[  174.854281][ T9784] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[  174.854286][ T9784] Call Trace:
[  174.854289][ T9784]  <TASK>
[  174.854292][ T9784]  dump_stack_lvl+0x10e/0x1f0
[  174.854305][ T9784]  print_report+0xd0/0x660
[  174.854315][ T9784]  ? __virt_addr_valid+0x81/0x610
[  174.854323][ T9784]  ? __phys_addr+0xe8/0x180
[  174.854330][ T9784]  ? hfsplus_bnode_read+0x2f4/0x360
[  174.854337][ T9784]  kasan_report+0xc6/0x100
[  174.854346][ T9784]  ? hfsplus_bnode_read+0x2f4/0x360
[  174.854354][ T9784]  hfsplus_bnode_read+0x2f4/0x360
[  174.854362][ T9784]  hfsplus_bnode_dump+0x2ec/0x380
[  174.854370][ T9784]  ? __pfx_hfsplus_bnode_dump+0x10/0x10
[  174.854377][ T9784]  ? hfsplus_bnode_write_u16+0x83/0xb0
[  174.854385][ T9784]  ? srcu_gp_start+0xd0/0x310
[  174.854393][ T9784]  ? __mark_inode_dirty+0x29e/0xe40
[  174.854402][ T9784]  hfsplus_brec_remove+0x3d2/0x4e0
[  174.854411][ T9784]  __hfsplus_delete_attr+0x290/0x3a0
[  174.854419][ T9784]  ? __pfx_hfs_find_1st_rec_by_cnid+0x10/0x10
[  174.854427][ T9784]  ? __pfx___hfsplus_delete_attr+0x10/0x10
[  174.854436][ T9784]  ? __asan_memset+0x23/0x50
[  174.854450][ T9784]  hfsplus_delete_all_attrs+0x262/0x320
[  174.854459][ T9784]  ? __pfx_hfsplus_delete_all_attrs+0x10/0x10
[  174.854469][ T9784]  ? rcu_is_watching+0x12/0xc0
[  174.854476][ T9784]  ? __mark_inode_dirty+0x29e/0xe40
[  174.854483][ T9784]  hfsplus_delete_cat+0x845/0xde0
[  174.854493][ T9784]  ? __pfx_hfsplus_delete_cat+0x10/0x10
[  174.854507][ T9784]  hfsplus_unlink+0x1ca/0x7c0
[  174.854516][ T9784]  ? __pfx_hfsplus_unlink+0x10/0x10
[  174.854525][ T9784]  ? down_write+0x148/0x200
[  174.854532][ T9784]  ? __pfx_down_write+0x10/0x10
[  174.854540][ T9784]  vfs_unlink+0x2fe/0x9b0
[  174.854549][ T9784]  do_unlinkat+0x490/0x670
[  174.854557][ T9784]  ? __pfx_do_unlinkat+0x10/0x10
[  174.854565][ T9784]  ? __might_fault+0xbc/0x130
[  174.854576][ T9784]  ? getname_flags.part.0+0x1c5/0x550
[  174.854584][ T9784]  __x64_sys_unlink+0xc5/0x110
[  174.854592][ T9784]  do_syscall_64+0xc9/0x480
[  174.854600][ T9784]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  174.854608][ T9784] RIP: 0033:0x7f6fdf4c3167
[  174.854614][ T9784] Code: f0 ff ff 73 01 c3 48 8b 0d 26 0d 0e 00 f7 d8 64 89 01 48 83 c8 ff c3 66 2e 0f 1f 84 00 00 00 00 08
[  174.854622][ T9784] RSP: 002b:00007ffcb948bca8 EFLAGS: 00000206 ORIG_RAX: 0000000000000057
[  174.854630][ T9784] RAX: ffffffffffffffda RBX: 0000000000000000 RCX: 00007f6fdf4c3167
[  174.854636][ T9784] RDX: 00007ffcb948bcc0 RSI: 00007ffcb948bcc0 RDI: 00007ffcb948bd50
[  174.854641][ T9784] RBP: 00007ffcb948cd90 R08: 0000000000000001 R09: 00007ffcb948bb40
[  174.854645][ T9784] R10: 00007f6fdf564fc0 R11: 0000000000000206 R12: 0000561e1bc9c2d0
[  174.854650][ T9784] R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000000
[  174.854658][ T9784]  </TASK>
[  174.854661][ T9784]
[  174.879281][ T9784] Allocated by task 9784:
[  174.879664][ T9784]  kasan_save_stack+0x20/0x40
[  174.880082][ T9784]  kasan_save_track+0x14/0x30
[  174.880500][ T9784]  __kasan_kmalloc+0xaa/0xb0
[  174.880908][ T9784]  __kmalloc_noprof+0x205/0x550
[  174.881337][ T9784]  __hfs_bnode_create+0x107/0x890
[  174.881779][ T9784]  hfsplus_bnode_find+0x2d0/0xd10
[  174.882222][ T9784]  hfsplus_brec_find+0x2b0/0x520
[  174.882659][ T9784]  hfsplus_delete_all_attrs+0x23b/0x3
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/032f7ed6717a4cd3714f9801be39fdfc7f1c7644
- https://git.kernel.org/stable/c/291b7f2538920aa229500dbdd6c5f0927a51bc8b
- https://git.kernel.org/stable/c/475d770c19929082aab43337e6c077d0e2043df3
- https://git.kernel.org/stable/c/5ab59229bef6063edf3a6fc2e3e3fd7cd2181b29
- https://git.kernel.org/stable/c/7fa4cef8ea13b37811287ef60674c5fd1dd02ee6

---

#### 701. CVE-2025-38716

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfs: fix general protection fault in hfs_find_init()

The hfs_find_init() method can trigger the crash
if tree pointer is NULL:

[   45.746290][ T9787] Oops: general protection fault, probably for non-canonical address 0xdffffc0000000008: 0000 [#1] SMP KAI
[   45.747287][ T9787] KASAN: null-ptr-deref in range [0x0000000000000040-0x0000000000000047]
[   45.748716][ T9787] CPU: 2 UID: 0 PID: 9787 Comm: repro Not tainted 6.16.0-rc3 #10 PREEMPT(full)
[   45.750250][ T9787] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   45.751983][ T9787] RIP: 0010:hfs_find_init+0x86/0x230
[   45.752834][ T9787] Code: c1 ea 03 80 3c 02 00 0f 85 9a 01 00 00 4c 8d 6b 40 48 c7 45 18 00 00 00 00 48 b8 00 00 00 00 00 fc
[   45.755574][ T9787] RSP: 0018:ffffc90015157668 EFLAGS: 00010202
[   45.756432][ T9787] RAX: dffffc0000000000 RBX: 0000000000000000 RCX: ffffffff819a4d09
[   45.757457][ T9787] RDX: 0000000000000008 RSI: ffffffff819acd3a RDI: ffffc900151576e8
[   45.758282][ T9787] RBP: ffffc900151576d0 R08: 0000000000000005 R09: 0000000000000000
[   45.758943][ T9787] R10: 0000000080000000 R11: 0000000000000001 R12: 0000000000000004
[   45.759619][ T9787] R13: 0000000000000040 R14: ffff88802c50814a R15: 0000000000000000
[   45.760293][ T9787] FS:  00007ffb72734540(0000) GS:ffff8880cec64000(0000) knlGS:0000000000000000
[   45.761050][ T9787] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   45.761606][ T9787] CR2: 00007f9bd8225000 CR3: 000000010979a000 CR4: 00000000000006f0
[   45.762286][ T9787] Call Trace:
[   45.762570][ T9787]  <TASK>
[   45.762824][ T9787]  hfs_ext_read_extent+0x190/0x9d0
[   45.763269][ T9787]  ? submit_bio_noacct_nocheck+0x2dd/0xce0
[   45.763766][ T9787]  ? __pfx_hfs_ext_read_extent+0x10/0x10
[   45.764250][ T9787]  hfs_get_block+0x55f/0x830
[   45.764646][ T9787]  block_read_full_folio+0x36d/0x850
[   45.765105][ T9787]  ? __pfx_hfs_get_block+0x10/0x10
[   45.765541][ T9787]  ? const_folio_flags+0x5b/0x100
[   45.765972][ T9787]  ? __pfx_hfs_read_folio+0x10/0x10
[   45.766415][ T9787]  filemap_read_folio+0xbe/0x290
[   45.766840][ T9787]  ? __pfx_filemap_read_folio+0x10/0x10
[   45.767325][ T9787]  ? __filemap_get_folio+0x32b/0xbf0
[   45.767780][ T9787]  do_read_cache_folio+0x263/0x5c0
[   45.768223][ T9787]  ? __pfx_hfs_read_folio+0x10/0x10
[   45.768666][ T9787]  read_cache_page+0x5b/0x160
[   45.769070][ T9787]  hfs_btree_open+0x491/0x1740
[   45.769481][ T9787]  hfs_mdb_get+0x15e2/0x1fb0
[   45.769877][ T9787]  ? __pfx_hfs_mdb_get+0x10/0x10
[   45.770316][ T9787]  ? find_held_lock+0x2b/0x80
[   45.770731][ T9787]  ? lockdep_init_map_type+0x5c/0x280
[   45.771200][ T9787]  ? lockdep_init_map_type+0x5c/0x280
[   45.771674][ T9787]  hfs_fill_super+0x38e/0x720
[   45.772092][ T9787]  ? __pfx_hfs_fill_super+0x10/0x10
[   45.772549][ T9787]  ? snprintf+0xbe/0x100
[   45.772931][ T9787]  ? __pfx_snprintf+0x10/0x10
[   45.773350][ T9787]  ? do_raw_spin_lock+0x129/0x2b0
[   45.773796][ T9787]  ? find_held_lock+0x2b/0x80
[   45.774215][ T9787]  ? set_blocksize+0x40a/0x510
[   45.774636][ T9787]  ? sb_set_blocksize+0x176/0x1d0
[   45.775087][ T9787]  ? setup_bdev_super+0x369/0x730
[   45.775533][ T9787]  get_tree_bdev_flags+0x384/0x620
[   45.775985][ T9787]  ? __pfx_hfs_fill_super+0x10/0x10
[   45.776453][ T9787]  ? __pfx_get_tree_bdev_flags+0x10/0x10
[   45.776950][ T9787]  ? bpf_lsm_capable+0x9/0x10
[   45.777365][ T9787]  ? security_capable+0x80/0x260
[   45.777803][ T9787]  vfs_get_tree+0x8e/0x340
[   45.778203][ T9787]  path_mount+0x13de/0x2010
[   45.778604][ T9787]  ? kmem_cache_free+0x2b0/0x4c0
[   45.779052][ T9787]  ? __pfx_path_mount+0x10/0x10
[   45.779480][ T9787]  ? getname_flags.part.0+0x1c5/0x550
[   45.779954][ T9787]  ? putname+0x154/0x1a0
[   45.780335][ T9787]  __x64_sys_mount+0x27b/0x300
[   45.780758][ T9787]  ? __pfx___x64_sys_mount+0x10/0x10
[   45.781232][ T9787] 
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/4f032979b63ad52e08aadf0faeac34ed35133ec0
- https://git.kernel.org/stable/c/5d8b249527362e0ccafcaf76b3bec2a0d2aa1498
- https://git.kernel.org/stable/c/6e20e10064fdc43231636fca519c15c013a8e3d6
- https://git.kernel.org/stable/c/736a0516a16268995f4898eded49bfef077af709
- https://git.kernel.org/stable/c/b918c17a1934ac6309b0083f41d4e9d8fb3bb46c

---

#### 702. CVE-2025-38734

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

net/smc: fix UAF on smcsk after smc_listen_out()

BPF CI testing report a UAF issue:

  [   16.446633] BUG: kernel NULL pointer dereference, address: 000000000000003  0
  [   16.447134] #PF: supervisor read access in kernel mod  e
  [   16.447516] #PF: error_code(0x0000) - not-present pag  e
  [   16.447878] PGD 0 P4D   0
  [   16.448063] Oops: Oops: 0000 [#1] PREEMPT SMP NOPT  I
  [   16.448409] CPU: 0 UID: 0 PID: 9 Comm: kworker/0:1 Tainted: G           OE      6.13.0-rc3-g89e8a75fda73-dirty #4  2
  [   16.449124] Tainted: [O]=OOT_MODULE, [E]=UNSIGNED_MODUL  E
  [   16.449502] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/201  4
  [   16.450201] Workqueue: smc_hs_wq smc_listen_wor  k
  [   16.450531] RIP: 0010:smc_listen_work+0xc02/0x159  0
  [   16.452158] RSP: 0018:ffffb5ab40053d98 EFLAGS: 0001024  6
  [   16.452526] RAX: 0000000000000001 RBX: 0000000000000002 RCX: 000000000000030  0
  [   16.452994] RDX: 0000000000000280 RSI: 00003513840053f0 RDI: 000000000000000  0
  [   16.453492] RBP: ffffa097808e3800 R08: ffffa09782dba1e0 R09: 000000000000000  5
  [   16.453987] R10: 0000000000000000 R11: 0000000000000000 R12: ffffa0978274640  0
  [   16.454497] R13: 0000000000000000 R14: 0000000000000000 R15: ffffa09782d4092  0
  [   16.454996] FS:  0000000000000000(0000) GS:ffffa097bbc00000(0000) knlGS:000000000000000  0
  [   16.455557] CS:  0010 DS: 0000 ES: 0000 CR0: 000000008005003  3
  [   16.455961] CR2: 0000000000000030 CR3: 0000000102788004 CR4: 0000000000770ef  0
  [   16.456459] PKRU: 5555555  4
  [   16.456654] Call Trace  :
  [   16.456832]  <TASK  >
  [   16.456989]  ? __die+0x23/0x7  0
  [   16.457215]  ? page_fault_oops+0x180/0x4c  0
  [   16.457508]  ? __lock_acquire+0x3e6/0x249  0
  [   16.457801]  ? exc_page_fault+0x68/0x20  0
  [   16.458080]  ? asm_exc_page_fault+0x26/0x3  0
  [   16.458389]  ? smc_listen_work+0xc02/0x159  0
  [   16.458689]  ? smc_listen_work+0xc02/0x159  0
  [   16.458987]  ? lock_is_held_type+0x8f/0x10  0
  [   16.459284]  process_one_work+0x1ea/0x6d  0
  [   16.459570]  worker_thread+0x1c3/0x38  0
  [   16.459839]  ? __pfx_worker_thread+0x10/0x1  0
  [   16.460144]  kthread+0xe0/0x11  0
  [   16.460372]  ? __pfx_kthread+0x10/0x1  0
  [   16.460640]  ret_from_fork+0x31/0x5  0
  [   16.460896]  ? __pfx_kthread+0x10/0x1  0
  [   16.461166]  ret_from_fork_asm+0x1a/0x3  0
  [   16.461453]  </TASK  >
  [   16.461616] Modules linked in: bpf_testmod(OE) [last unloaded: bpf_testmod(OE)  ]
  [   16.462134] CR2: 000000000000003  0
  [   16.462380] ---[ end trace 0000000000000000 ]---
  [   16.462710] RIP: 0010:smc_listen_work+0xc02/0x1590

The direct cause of this issue is that after smc_listen_out_connected(),
newclcsock->sk may be NULL since it will releases the smcsk. Therefore,
if the application closes the socket immediately after accept,
newclcsock->sk can be NULL. A possible execution order could be as
follows:

smc_listen_work                                 | userspace
-----------------------------------------------------------------
lock_sock(sk)                                   |
smc_listen_out_connected()                      |
| \- smc_listen_out                             |
|    | \- release_sock                          |
     | |- sk->sk_data_ready()                   |
                                                | fd = accept();
                                                | close(fd);
                                                |  \- socket->sk = NULL;
/* newclcsock->sk is NULL now */
SMC_STAT_SERV_SUCC_INC(sock_net(newclcsock->sk))

Since smc_listen_out_connected() will not fail, simply swapping the order
of the code can easily fix this issue.

**参考链接 / References**:
- https://git.kernel.org/stable/c/070b4af44c4b6e4c35fb1ca7001a6a88fd2d318f
- https://git.kernel.org/stable/c/2e765ba0ee0eae35688b443e97108308a716773e
- https://git.kernel.org/stable/c/85545f1525f9fa9bf44fec77ba011024f15da342
- https://git.kernel.org/stable/c/d9cef55ed49117bd63695446fb84b4b91815c0b4

---

#### 703. CVE-2025-39833

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

mISDN: hfcpci: Fix warning when deleting uninitialized timer

With CONFIG_DEBUG_OBJECTS_TIMERS unloading hfcpci module leads
to the following splat:

[  250.215892] ODEBUG: assert_init not available (active state 0) object: ffffffffc01a3dc0 object type: timer_list hint: 0x0
[  250.217520] WARNING: CPU: 0 PID: 233 at lib/debugobjects.c:612 debug_print_object+0x1b6/0x2c0
[  250.218775] Modules linked in: hfcpci(-) mISDN_core
[  250.219537] CPU: 0 UID: 0 PID: 233 Comm: rmmod Not tainted 6.17.0-rc2-g6f713187ac98 #2 PREEMPT(voluntary)
[  250.220940] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[  250.222377] RIP: 0010:debug_print_object+0x1b6/0x2c0
[  250.223131] Code: fc ff df 48 89 fa 48 c1 ea 03 80 3c 02 00 75 4f 41 56 48 8b 14 dd a0 4e 01 9f 48 89 ee 48 c7 c7 20 46 01 9f e8 cb 84d
[  250.225805] RSP: 0018:ffff888015ea7c08 EFLAGS: 00010286
[  250.226608] RAX: 0000000000000000 RBX: 0000000000000005 RCX: ffffffff9be93a95
[  250.227708] RDX: 1ffff1100d945138 RSI: 0000000000000008 RDI: ffff88806ca289c0
[  250.228993] RBP: ffffffff9f014a00 R08: 0000000000000001 R09: ffffed1002bd4f39
[  250.230043] R10: ffff888015ea79cf R11: 0000000000000001 R12: 0000000000000001
[  250.231185] R13: ffffffff9eea0520 R14: 0000000000000000 R15: ffff888015ea7cc8
[  250.232454] FS:  00007f3208f01540(0000) GS:ffff8880caf5a000(0000) knlGS:0000000000000000
[  250.233851] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  250.234856] CR2: 00007f32090a7421 CR3: 0000000004d63000 CR4: 00000000000006f0
[  250.236117] Call Trace:
[  250.236599]  <TASK>
[  250.236967]  ? trace_irq_enable.constprop.0+0xd4/0x130
[  250.237920]  debug_object_assert_init+0x1f6/0x310
[  250.238762]  ? __pfx_debug_object_assert_init+0x10/0x10
[  250.239658]  ? __lock_acquire+0xdea/0x1c70
[  250.240369]  __try_to_del_timer_sync+0x69/0x140
[  250.241172]  ? __pfx___try_to_del_timer_sync+0x10/0x10
[  250.242058]  ? __timer_delete_sync+0xc6/0x120
[  250.242842]  ? lock_acquire+0x30/0x80
[  250.243474]  ? __timer_delete_sync+0xc6/0x120
[  250.244262]  __timer_delete_sync+0x98/0x120
[  250.245015]  HFC_cleanup+0x10/0x20 [hfcpci]
[  250.245704]  __do_sys_delete_module+0x348/0x510
[  250.246461]  ? __pfx___do_sys_delete_module+0x10/0x10
[  250.247338]  do_syscall_64+0xc1/0x360
[  250.247924]  entry_SYSCALL_64_after_hwframe+0x77/0x7f

Fix this by initializing hfc_tl timer with DEFINE_TIMER macro.
Also, use mod_timer instead of manual timeout update.

**参考链接 / References**:
- https://git.kernel.org/stable/c/43fc5da8133badf17f5df250ba03b9d882254845
- https://git.kernel.org/stable/c/97766512a9951b9fd6fc97f1b93211642bb0b220

---

#### 704. CVE-2025-34197

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Vasion Print (formerly PrinterLogic) Virtual Appliance Host versions prior to 22.0.951, Application prior to 20.0.2368 (VA and SaaS deployments) contain an undocumented local user account named ubuntu with a preset password and a sudoers entry granting that account passwordless root privileges (ubuntu ALL=(ALL) NOPASSWD: ALL). Anyone who knows the hardcoded password can obtain root privileges via local console or equivalent administrative access, enabling local privilege escalation. This vulnerability has been identified by the vendor as: V-2024-010 — Hardcoded Linux Password. NOTE: The patch for this vulnerability is reported to be incomplete: /etc/shadow was remediated but /etc/sudoers remains vulnerable.

**参考链接 / References**:
- https://help.printerlogic.com/saas/Print/Security/Security-Bulletins.htm
- https://help.printerlogic.com/va/Print/Security/Security-Bulletins.htm
- https://pierrekim.github.io/blog/2025-04-08-vasion-printerlogic-83-vulnerabilities.html#va-hardcoded-password-ubuntu
- https://www.vulncheck.com/advisories/vasion-print-printerlogic-undocumented-local-account-with-hardcoded-password-and-passwordless-sudo

---

#### 705. CVE-2025-43914

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Dell PowerProtect Data Domain BoostFS for Linux Ubuntu systems of Feature Release versions 7.7.1.0 through 8.3.0.15, LTS2025 release version 8.3.1.0, LTS2024 release versions 7.13.1.0 through 7.13.1.30, LTS 2023 release versions 7.10.1.0 through 7.10.1.60, contain an Incorrect Privilege Assignment vulnerability. A low privileged attacker with local access could potentially exploit this vulnerability, leading to Unauthorized access.

**参考链接 / References**:
- https://www.dell.com/support/kbdoc/en-us/000376224/dsa-2025-333-security-update-for-dell-powerprotect-data-domain-multiple-vulnerabilities

---

#### 706. CVE-2025-40006

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

mm/hugetlb: fix folio is still mapped when deleted

Migration may be raced with fallocating hole.  remove_inode_single_folio
will unmap the folio if the folio is still mapped.  However, it's called
without folio lock.  If the folio is migrated and the mapped pte has been
converted to migration entry, folio_mapped() returns false, and won't
unmap it.  Due to extra refcount held by remove_inode_single_folio,
migration fails, restores migration entry to normal pte, and the folio is
mapped again.  As a result, we triggered BUG in filemap_unaccount_folio.

The log is as follows:
 BUG: Bad page cache in process hugetlb  pfn:156c00
 page: refcount:515 mapcount:0 mapping:0000000099fef6e1 index:0x0 pfn:0x156c00
 head: order:9 mapcount:1 entire_mapcount:1 nr_pages_mapped:0 pincount:0
 aops:hugetlbfs_aops ino:dcc dentry name(?):"my_hugepage_file"
 flags: 0x17ffffc00000c1(locked|waiters|head|node=0|zone=2|lastcpupid=0x1fffff)
 page_type: f4(hugetlb)
 page dumped because: still mapped when deleted
 CPU: 1 UID: 0 PID: 395 Comm: hugetlb Not tainted 6.17.0-rc5-00044-g7aac71907bde-dirty #484 NONE
 Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 0.0.0 02/06/2015
 Call Trace:
  <TASK>
  dump_stack_lvl+0x4f/0x70
  filemap_unaccount_folio+0xc4/0x1c0
  __filemap_remove_folio+0x38/0x1c0
  filemap_remove_folio+0x41/0xd0
  remove_inode_hugepages+0x142/0x250
  hugetlbfs_fallocate+0x471/0x5a0
  vfs_fallocate+0x149/0x380

Hold folio lock before checking if the folio is mapped to avold race with
migration.

**参考链接 / References**:
- https://git.kernel.org/stable/c/21ee79ce938127f88fe07e409c1817f477dbe7ea
- https://git.kernel.org/stable/c/3e851448078f5b01f6264915df3cfef75e323a12
- https://git.kernel.org/stable/c/7b7387650dcf2881fd8bb55bcf3c8bd6c9542dd7
- https://git.kernel.org/stable/c/910d7749346c4b0acdc6e4adfdc4a9984281a206
- https://git.kernel.org/stable/c/91f548e920fbf8be3f285bfa3fa045ae017e836d

---

#### 707. CVE-2025-40088

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfsplus: fix slab-out-of-bounds read in hfsplus_strcasecmp()

The hfsplus_strcasecmp() logic can trigger the issue:

[  117.317703][ T9855] ==================================================================
[  117.318353][ T9855] BUG: KASAN: slab-out-of-bounds in hfsplus_strcasecmp+0x1bc/0x490
[  117.318991][ T9855] Read of size 2 at addr ffff88802160f40c by task repro/9855
[  117.319577][ T9855]
[  117.319773][ T9855] CPU: 0 UID: 0 PID: 9855 Comm: repro Not tainted 6.17.0-rc6 #33 PREEMPT(full)
[  117.319780][ T9855] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[  117.319783][ T9855] Call Trace:
[  117.319785][ T9855]  <TASK>
[  117.319788][ T9855]  dump_stack_lvl+0x1c1/0x2a0
[  117.319795][ T9855]  ? __virt_addr_valid+0x1c8/0x5c0
[  117.319803][ T9855]  ? __pfx_dump_stack_lvl+0x10/0x10
[  117.319808][ T9855]  ? rcu_is_watching+0x15/0xb0
[  117.319816][ T9855]  ? lock_release+0x4b/0x3e0
[  117.319821][ T9855]  ? __kasan_check_byte+0x12/0x40
[  117.319828][ T9855]  ? __virt_addr_valid+0x1c8/0x5c0
[  117.319835][ T9855]  ? __virt_addr_valid+0x4a5/0x5c0
[  117.319842][ T9855]  print_report+0x17e/0x7e0
[  117.319848][ T9855]  ? __virt_addr_valid+0x1c8/0x5c0
[  117.319855][ T9855]  ? __virt_addr_valid+0x4a5/0x5c0
[  117.319862][ T9855]  ? __phys_addr+0xd3/0x180
[  117.319869][ T9855]  ? hfsplus_strcasecmp+0x1bc/0x490
[  117.319876][ T9855]  kasan_report+0x147/0x180
[  117.319882][ T9855]  ? hfsplus_strcasecmp+0x1bc/0x490
[  117.319891][ T9855]  hfsplus_strcasecmp+0x1bc/0x490
[  117.319900][ T9855]  ? __pfx_hfsplus_cat_case_cmp_key+0x10/0x10
[  117.319906][ T9855]  hfs_find_rec_by_key+0xa9/0x1e0
[  117.319913][ T9855]  __hfsplus_brec_find+0x18e/0x470
[  117.319920][ T9855]  ? __pfx_hfsplus_bnode_find+0x10/0x10
[  117.319926][ T9855]  ? __pfx_hfs_find_rec_by_key+0x10/0x10
[  117.319933][ T9855]  ? __pfx___hfsplus_brec_find+0x10/0x10
[  117.319942][ T9855]  hfsplus_brec_find+0x28f/0x510
[  117.319949][ T9855]  ? __pfx_hfs_find_rec_by_key+0x10/0x10
[  117.319956][ T9855]  ? __pfx_hfsplus_brec_find+0x10/0x10
[  117.319963][ T9855]  ? __kmalloc_noprof+0x2a9/0x510
[  117.319969][ T9855]  ? hfsplus_find_init+0x8c/0x1d0
[  117.319976][ T9855]  hfsplus_brec_read+0x2b/0x120
[  117.319983][ T9855]  hfsplus_lookup+0x2aa/0x890
[  117.319990][ T9855]  ? __pfx_hfsplus_lookup+0x10/0x10
[  117.320003][ T9855]  ? d_alloc_parallel+0x2f0/0x15e0
[  117.320008][ T9855]  ? __lock_acquire+0xaec/0xd80
[  117.320013][ T9855]  ? __pfx_d_alloc_parallel+0x10/0x10
[  117.320019][ T9855]  ? __raw_spin_lock_init+0x45/0x100
[  117.320026][ T9855]  ? __init_waitqueue_head+0xa9/0x150
[  117.320034][ T9855]  __lookup_slow+0x297/0x3d0
[  117.320039][ T9855]  ? __pfx___lookup_slow+0x10/0x10
[  117.320045][ T9855]  ? down_read+0x1ad/0x2e0
[  117.320055][ T9855]  lookup_slow+0x53/0x70
[  117.320065][ T9855]  walk_component+0x2f0/0x430
[  117.320073][ T9855]  path_lookupat+0x169/0x440
[  117.320081][ T9855]  filename_lookup+0x212/0x590
[  117.320089][ T9855]  ? __pfx_filename_lookup+0x10/0x10
[  117.320098][ T9855]  ? strncpy_from_user+0x150/0x290
[  117.320105][ T9855]  ? getname_flags+0x1e5/0x540
[  117.320112][ T9855]  user_path_at+0x3a/0x60
[  117.320117][ T9855]  __x64_sys_umount+0xee/0x160
[  117.320123][ T9855]  ? __pfx___x64_sys_umount+0x10/0x10
[  117.320129][ T9855]  ? do_syscall_64+0xb7/0x3a0
[  117.320135][ T9855]  ? entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  117.320141][ T9855]  ? entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  117.320145][ T9855]  do_syscall_64+0xf3/0x3a0
[  117.320150][ T9855]  ? exc_page_fault+0x9f/0xf0
[  117.320154][ T9855]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[  117.320158][ T9855] RIP: 0033:0x7f7dd7908b07
[  117.320163][ T9855] Code: 23 0d 00 f7 d8 64 89 01 48 83 c8 ff c3 66 0f 1f 44 00 00 31 f6 e9 09 00 00 00 66 0f 1f 84 00 00 08
[  117.320167][ T9855] RSP: 002b:00007ffd5ebd9698 EFLAGS: 00000202 
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/42520df65bf67189541a425f7d36b0b3e7bd7844
- https://git.kernel.org/stable/c/4bc081ba6c52b0c88c92701e3fbc33c7e2277afb
- https://git.kernel.org/stable/c/4f5ab4a9c6abd8b0d713cc2b7b041bc10d70f241
- https://git.kernel.org/stable/c/586c75dfd1d265c4150f6529debb85c9d62e101f
- https://git.kernel.org/stable/c/603158d4efa98a13a746bd586c20f194f4a31ec8

---

#### 708. CVE-2025-2486

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The Ubuntu edk2 UEFI firmware packages accidentally allowed the UEFI Shell to be accessed in Secure Boot environments, possibly allowing bypass of Secure Boot constraints. Versions 2024.05-2ubuntu0.3 and 2024.02-2ubuntu0.3 disable the Shell. Some previous versions inserted a secure-boot-based decision to continue running inside the Shell itself, which is believed to be sufficient to enforce Secure Boot restrictions. This is an additional repair on top of the incomplete fix for CVE-2023-48733.

**参考链接 / References**:
- https://bugs.launchpad.net/ubuntu/+source/edk2/+bug/2101797

---

#### 709. CVE-2025-40244

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfsplus: fix KMSAN uninit-value issue in __hfsplus_ext_cache_extent()

The syzbot reported issue in __hfsplus_ext_cache_extent():

[   70.194323][ T9350] BUG: KMSAN: uninit-value in __hfsplus_ext_cache_extent+0x7d0/0x990
[   70.195022][ T9350]  __hfsplus_ext_cache_extent+0x7d0/0x990
[   70.195530][ T9350]  hfsplus_file_extend+0x74f/0x1cf0
[   70.195998][ T9350]  hfsplus_get_block+0xe16/0x17b0
[   70.196458][ T9350]  __block_write_begin_int+0x962/0x2ce0
[   70.196959][ T9350]  cont_write_begin+0x1000/0x1950
[   70.197416][ T9350]  hfsplus_write_begin+0x85/0x130
[   70.197873][ T9350]  generic_perform_write+0x3e8/0x1060
[   70.198374][ T9350]  __generic_file_write_iter+0x215/0x460
[   70.198892][ T9350]  generic_file_write_iter+0x109/0x5e0
[   70.199393][ T9350]  vfs_write+0xb0f/0x14e0
[   70.199771][ T9350]  ksys_write+0x23e/0x490
[   70.200149][ T9350]  __x64_sys_write+0x97/0xf0
[   70.200570][ T9350]  x64_sys_call+0x3015/0x3cf0
[   70.201065][ T9350]  do_syscall_64+0xd9/0x1d0
[   70.201506][ T9350]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[   70.202054][ T9350]
[   70.202279][ T9350] Uninit was created at:
[   70.202693][ T9350]  __kmalloc_noprof+0x621/0xf80
[   70.203149][ T9350]  hfsplus_find_init+0x8d/0x1d0
[   70.203602][ T9350]  hfsplus_file_extend+0x6ca/0x1cf0
[   70.204087][ T9350]  hfsplus_get_block+0xe16/0x17b0
[   70.204561][ T9350]  __block_write_begin_int+0x962/0x2ce0
[   70.205074][ T9350]  cont_write_begin+0x1000/0x1950
[   70.205547][ T9350]  hfsplus_write_begin+0x85/0x130
[   70.206017][ T9350]  generic_perform_write+0x3e8/0x1060
[   70.206519][ T9350]  __generic_file_write_iter+0x215/0x460
[   70.207042][ T9350]  generic_file_write_iter+0x109/0x5e0
[   70.207552][ T9350]  vfs_write+0xb0f/0x14e0
[   70.207961][ T9350]  ksys_write+0x23e/0x490
[   70.208375][ T9350]  __x64_sys_write+0x97/0xf0
[   70.208810][ T9350]  x64_sys_call+0x3015/0x3cf0
[   70.209255][ T9350]  do_syscall_64+0xd9/0x1d0
[   70.209680][ T9350]  entry_SYSCALL_64_after_hwframe+0x77/0x7f
[   70.210230][ T9350]
[   70.210454][ T9350] CPU: 2 UID: 0 PID: 9350 Comm: repro Not tainted 6.12.0-rc5 #5
[   70.211174][ T9350] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   70.212115][ T9350] =====================================================
[   70.212734][ T9350] Disabling lock debugging due to kernel taint
[   70.213284][ T9350] Kernel panic - not syncing: kmsan.panic set ...
[   70.213858][ T9350] CPU: 2 UID: 0 PID: 9350 Comm: repro Tainted: G    B              6.12.0-rc5 #5
[   70.214679][ T9350] Tainted: [B]=BAD_PAGE
[   70.215057][ T9350] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   70.215999][ T9350] Call Trace:
[   70.216309][ T9350]  <TASK>
[   70.216585][ T9350]  dump_stack_lvl+0x1fd/0x2b0
[   70.217025][ T9350]  dump_stack+0x1e/0x30
[   70.217421][ T9350]  panic+0x502/0xca0
[   70.217803][ T9350]  ? kmsan_get_metadata+0x13e/0x1c0

[   70.218294][ Message fromT sy9350]  kmsan_report+0x296/slogd@syzkaller 0x2aat Aug 18 22:11:058 ...
 kernel
:[   70.213284][ T9350] Kernel panic - not syncing: kmsan.panic [   70.220179][ T9350]  ? kmsan_get_metadata+0x13e/0x1c0
set ...
[   70.221254][ T9350]  ? __msan_warning+0x96/0x120
[   70.222066][ T9350]  ? __hfsplus_ext_cache_extent+0x7d0/0x990
[   70.223023][ T9350]  ? hfsplus_file_extend+0x74f/0x1cf0
[   70.224120][ T9350]  ? hfsplus_get_block+0xe16/0x17b0
[   70.224946][ T9350]  ? __block_write_begin_int+0x962/0x2ce0
[   70.225756][ T9350]  ? cont_write_begin+0x1000/0x1950
[   70.226337][ T9350]  ? hfsplus_write_begin+0x85/0x130
[   70.226852][ T9350]  ? generic_perform_write+0x3e8/0x1060
[   70.227405][ T9350]  ? __generic_file_write_iter+0x215/0x460
[   70.227979][ T9350]  ? generic_file_write_iter+0x109/0x5e0
[   70.228540][ T9350]  ? vfs_write+0xb0f/0x14e0
[   70.228997][ T9350]  ? ksys_write+0x23e/0x490
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/14c673a2f3ecf650b694a52a88688f1d71849899
- https://git.kernel.org/stable/c/4840ceadef4290c56cc422f0fc697655f3cbf070
- https://git.kernel.org/stable/c/99202d94909d323a30d154ab0261c0a07166daec
- https://git.kernel.org/stable/c/a5bfb13b4f406aef1a450f99d22d3e48df01528c
- https://git.kernel.org/stable/c/b8a72692aa42b7dcd179a96b90bc2763ac74576a

---

#### 710. CVE-2025-40349

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

hfs: validate record offset in hfsplus_bmap_alloc

hfsplus_bmap_alloc can trigger a crash if a
record offset or length is larger than node_size

[   15.264282] BUG: KASAN: slab-out-of-bounds in hfsplus_bmap_alloc+0x887/0x8b0
[   15.265192] Read of size 8 at addr ffff8881085ca188 by task test/183
[   15.265949]
[   15.266163] CPU: 0 UID: 0 PID: 183 Comm: test Not tainted 6.17.0-rc2-gc17b750b3ad9 #14 PREEMPT(voluntary)
[   15.266165] Hardware name: QEMU Ubuntu 24.04 PC (i440FX + PIIX, 1996), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   15.266167] Call Trace:
[   15.266168]  <TASK>
[   15.266169]  dump_stack_lvl+0x53/0x70
[   15.266173]  print_report+0xd0/0x660
[   15.266181]  kasan_report+0xce/0x100
[   15.266185]  hfsplus_bmap_alloc+0x887/0x8b0
[   15.266208]  hfs_btree_inc_height.isra.0+0xd5/0x7c0
[   15.266217]  hfsplus_brec_insert+0x870/0xb00
[   15.266222]  __hfsplus_ext_write_extent+0x428/0x570
[   15.266225]  __hfsplus_ext_cache_extent+0x5e/0x910
[   15.266227]  hfsplus_ext_read_extent+0x1b2/0x200
[   15.266233]  hfsplus_file_extend+0x5a7/0x1000
[   15.266237]  hfsplus_get_block+0x12b/0x8c0
[   15.266238]  __block_write_begin_int+0x36b/0x12c0
[   15.266251]  block_write_begin+0x77/0x110
[   15.266252]  cont_write_begin+0x428/0x720
[   15.266259]  hfsplus_write_begin+0x51/0x100
[   15.266262]  cont_write_begin+0x272/0x720
[   15.266270]  hfsplus_write_begin+0x51/0x100
[   15.266274]  generic_perform_write+0x321/0x750
[   15.266285]  generic_file_write_iter+0xc3/0x310
[   15.266289]  __kernel_write_iter+0x2fd/0x800
[   15.266296]  dump_user_range+0x2ea/0x910
[   15.266301]  elf_core_dump+0x2a94/0x2ed0
[   15.266320]  vfs_coredump+0x1d85/0x45e0
[   15.266349]  get_signal+0x12e3/0x1990
[   15.266357]  arch_do_signal_or_restart+0x89/0x580
[   15.266362]  irqentry_exit_to_user_mode+0xab/0x110
[   15.266364]  asm_exc_page_fault+0x26/0x30
[   15.266366] RIP: 0033:0x41bd35
[   15.266367] Code: bc d1 f3 0f 7f 27 f3 0f 7f 6f 10 f3 0f 7f 77 20 f3 0f 7f 7f 30 49 83 c0 0f 49 29 d0 48 8d 7c 17 31 e9 9f 0b 00 00 66 0f ef c0 <f3> 0f 6f 0e f3 0f 6f 56 10 66 0f 74 c1 66 0f d7 d0 49 83 f8f
[   15.266369] RSP: 002b:00007ffc9e62d078 EFLAGS: 00010283
[   15.266371] RAX: 00007ffc9e62d100 RBX: 0000000000000000 RCX: 0000000000000000
[   15.266372] RDX: 00000000000000e0 RSI: 0000000000000000 RDI: 00007ffc9e62d100
[   15.266373] RBP: 0000400000000040 R08: 00000000000000e0 R09: 0000000000000000
[   15.266374] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[   15.266375] R13: 0000000000000000 R14: 0000000000000000 R15: 0000400000000000
[   15.266376]  </TASK>

When calling hfsplus_bmap_alloc to allocate a free node, this function
first retrieves the bitmap from header node and map node using node->page
together with the offset and length from hfs_brec_lenoff

```
len = hfs_brec_lenoff(node, 2, &off16);
off = off16;

off += node->page_offset;
pagep = node->page + (off >> PAGE_SHIFT);
data = kmap_local_page(*pagep);
```

However, if the retrieved offset or length is invalid(i.e. exceeds
node_size), the code may end up accessing pages outside the allocated
range for this node.

This patch adds proper validation of both offset and length before use,
preventing out-of-bounds page access. Move is_bnode_offset_valid and
check_and_correct_requested_length to hfsplus_fs.h, as they may be
required by other functions.

**参考链接 / References**:
- https://git.kernel.org/stable/c/0058d20d76182861dbdd8fd6e2dd8d18d6d3becf
- https://git.kernel.org/stable/c/068a46df3e6acc68fb9db0a6313ab379a11ecd6f
- https://git.kernel.org/stable/c/17ed51cfce6c62cffb97059ef392ad2e0245806e
- https://git.kernel.org/stable/c/40dfe7a4215a1f20842561ffaf5a6f83a987e75b
- https://git.kernel.org/stable/c/418e48cab99c52c1760636a4dbe464bf6db2018b

---

#### 711. CVE-2026-3832 - gnutls: gnutls: Security bypass allows acceptance of revoked server certificates…

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] gnutls: gnutls: Security bypass allows acceptance of revoked server certificates via crafted OCSP response. Bugzilla: 2445762

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2445762

---

#### 712. CVE-2026-33845 - gnutls: GnuTLS: Denial of Service via DTLS zero-length fragment

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] gnutls: GnuTLS: Denial of Service via DTLS zero-length fragment. Bugzilla: 2450624

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2450624

---

#### 713. CVE-2026-3833 - gnutls: GnuTLS: Policy bypass due to case-sensitive nameConstraints comparison

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] gnutls: GnuTLS: Policy bypass due to case-sensitive nameConstraints comparison. Bugzilla: 2445763

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2445763

---

#### 714. CVE-2026-7163 - assisted-service: assisted-service: Authenticated users can gain administrative…

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] assisted-service: assisted-service: Authenticated users can gain administrative access to OpenShift clusters via credential disclosure. Bugzilla: 2463152

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463152

---

#### 715. CVE-2026-7500 - org.keycloak.keycloak-services: Improper Access Control on Keycloak Server when the…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] org.keycloak.keycloak-services: Improper Access Control on Keycloak Server when the account Account API feature is disabled. Bugzilla: 2464126

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464126

---

#### 716. CVE-2026-4873 - curl: curl: Information disclosure due to incorrect TLS connection reuse

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] curl: curl: Information disclosure due to incorrect TLS connection reuse. Bugzilla: 2461200

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461200

---

#### 717. CVE-2026-5773 - curl: libcurl: Wrong file transfer due to incorrect SMB connection reuse

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Wrong file transfer due to incorrect SMB connection reuse. Bugzilla: 2461201

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461201

---

#### 718. CVE-2026-6253 - curl: curl: Proxy credential disclosure via redirects to unauthenticated proxies

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] curl: curl: Proxy credential disclosure via redirects to unauthenticated proxies. Bugzilla: 2461202

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461202

---

#### 719. CVE-2026-6276 - curl: libcurl: Information disclosure due to cookie leak when reusing connections…

**严重程度 / Severity**: LOW

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Information disclosure due to cookie leak when reusing connections with custom Host headers. Bugzilla: 2461203

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461203

---

#### 720. CVE-2026-5545 - curl: libcurl: Authentication bypass due to incorrect HTTP Negotiate connection…

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Authentication bypass due to incorrect HTTP Negotiate connection reuse. Bugzilla: 2461204

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461204

---

#### 721. CVE-2026-6429 - curl: libcurl: Credential leak via reused proxy connection during HTTP redirects

**严重程度 / Severity**: MODERATE

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Credential leak via reused proxy connection during HTTP redirects. Bugzilla: 2461205

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461205

---

#### 722. CVE-2026-38993 - Cockpit: Cockpit: Arbitrary file write via directory traversal in Buckets component

**严重程度 / Severity**: IMPORTANT

**漏洞描述 / Description**:
[Red Hat] Cockpit: Cockpit: Arbitrary file write via directory traversal in Buckets component. Bugzilla: 2463843

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463843

---

#### 723. CVE-2008-4946

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
convirt 0.8.2 allows local users to overwrite arbitrary files via a symlink attack on the /tmp/set_output temporary file, related to the (1) _template_/provision.sh, (2) Linux_CD_Install/provision.sh, (3) Fedora_PV_Install/provision.sh, (4) CentOS_PV_Install/provision.sh, (5) common/provision.sh, (6) example/provision.sh, and (7) Windows_CD_Install/provision.sh scripts in image_store/.

**参考链接 / References**:
- http://bugs.debian.org/496419
- http://dev.gentoo.org/~rbu/security/debiantemp/convirt
- http://www.openwall.com/lists/oss-security/2008/10/30/2
- https://bugs.gentoo.org/show_bug.cgi?id=235770
- http://bugs.debian.org/496419

---

#### 724. CVE-2016-5425

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The Tomcat package on Red Hat Enterprise Linux (RHEL) 7, Fedora, CentOS, Oracle Linux, and possibly other Linux distributions uses weak permissions for /usr/lib/tmpfiles.d/tomcat.conf, which allows local users to gain root privileges by leveraging membership in the tomcat group.

**参考链接 / References**:
- http://legalhackers.com/advisories/Tomcat-RedHat-Pkgs-Root-PrivEsc-Exploit-CVE-2016-5425.html
- http://packetstormsecurity.com/files/139041/Apache-Tomcat-8-7-6-Privilege-Escalation.html
- http://rhn.redhat.com/errata/RHSA-2016-2046.html
- http://www.openwall.com/lists/oss-security/2016/10/10/2
- http://www.oracle.com/technetwork/topics/security/linuxbulletinoct2016-3090545.html

---

#### 725. CVE-2017-5972

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
The TCP stack in the Linux kernel 3.x does not properly implement a SYN cookie protection mechanism for the case of a fast network connection, which allows remote attackers to cause a denial of service (CPU consumption) by sending many TCP SYN packets, as demonstrated by an attack against the kernel-3.10.0 package in CentOS Linux 7. NOTE: third parties have been unable to discern any relationship between the GitHub Engineering finding and the Trigemini.c attack code.

**参考链接 / References**:
- http://seclists.org/oss-sec/2017/q1/573
- http://www.securityfocus.com/bid/96231
- https://access.redhat.com/security/cve/cve-2017-5972
- https://bugzilla.redhat.com/show_bug.cgi?id=1422081
- https://cxsecurity.com/issue/WLB-2017020112

---

#### 726. CVE-2018-5961

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through v0.9.8.12 has XSS via the `module` value of the `index.php` file.

**参考链接 / References**:
- https://www.vulnerability-lab.com/get_content.php?id=1835
- https://www.vulnerability-lab.com/get_content.php?id=1835

---

#### 727. CVE-2018-5962

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
index.php in CentOS-WebPanel.com (aka CWP) CentOS Web Panel through v0.9.8.12 has XSS via the id parameter to the phpini_editor module or the email_address parameter to the mail_add-new module.

**参考链接 / References**:
- https://www.vulnerability-lab.com/get_content.php?id=1836
- https://www.vulnerability-lab.com/get_content.php?id=1836

---

#### 728. CVE-2018-6926

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
In app/Controller/ServersController.php in MISP 2.4.87, a server setting permitted the override of a path variable on certain Red Hed Enterprise Linux and CentOS systems (where rh_shell_fix was enabled), and consequently allowed site admins to inject arbitrary OS commands. The impact is limited by the setting being only accessible to the site administrator.

**参考链接 / References**:
- https://github.com/MISP/MISP/commit/0a2aa9d52492d960b9a161160acedbe9caaa4126
- https://github.com/MISP/MISP/commit/0a2aa9d52492d960b9a161160acedbe9caaa4126

---

#### 729. CVE-2018-17977

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
The Linux kernel 4.14.67 mishandles certain interaction among XFRM Netlink messages, IPPROTO_AH packets, and IPPROTO_IP packets, which allows local users to cause a denial of service (memory consumption and system hang) by leveraging root access to execute crafted applications, as demonstrated on CentOS 7.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105539
- https://www.openwall.com/lists/oss-security/2018/10/05/5
- http://www.securityfocus.com/bid/105539
- https://www.openwall.com/lists/oss-security/2018/10/05/5

---

#### 730. CVE-2018-18322

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has Command Injection via shell metacharacters in the admin/index.php service_start, service_restart, service_fullstatus, or service_stop parameter.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 731. CVE-2018-18323

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has Local File Inclusion via directory traversal with an admin/index.php?module=file_editor&file=/../ URI.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 732. CVE-2018-18324

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has XSS via the admin/fileManager2.php fm_current_dir parameter, or the admin/index.php module, service_start, service_fullstatus, service_restart, service_stop, or file (within the file_editor) parameter.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 733. CVE-2018-18772

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows CSRF via admin/index.php?module=send_ssh, as demonstrated by executing an arbitrary OS command.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 734. CVE-2018-18773

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows CSRF via admin/index.php?module=rootpwd, as demonstrated by changing the root password.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 735. CVE-2018-18774

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows XSS via the admin/index.php module parameter.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 736. CVE-2019-7646

**严重程度 / Severity**: MEDIUM | CVSS: 4.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.763 is vulnerable to Stored/Persistent XSS for the "Package Name" field via the add_package module parameter.

**参考链接 / References**:
- http://packetstormsecurity.com/files/151630/CentOS-Web-Panel-0.9.8.763-Cross-Site-Scripting.html
- https://www.dineshmohanty.com/centos-web-panel-xss
- https://www.exploit-db.com/exploits/46349/
- http://packetstormsecurity.com/files/151630/CentOS-Web-Panel-0.9.8.763-Cross-Site-Scripting.html
- https://www.dineshmohanty.com/centos-web-panel-xss

---

#### 737. CVE-2019-10261

**严重程度 / Severity**: MEDIUM | CVSS: 4.8

**漏洞描述 / Description**:
CentOS Web Panel (CWP) 0.9.8.789 is vulnerable to Stored/Persistent XSS for the "Name Server 1" and "Name Server 2" fields via a "DNS Functions" "Edit Nameservers IPs" action.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107769
- https://packetstormsecurity.com/files/152303/CentOS-Web-Panel-0.9.8.789-Cross-Site-Scripting.html
- https://www.exploit-db.com/exploits/46629
- http://www.securityfocus.com/bid/107769
- https://packetstormsecurity.com/files/152303/CentOS-Web-Panel-0.9.8.789-Cross-Site-Scripting.html

---

#### 738. CVE-2019-10893

**严重程度 / Severity**: MEDIUM | CVSS: 4.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.793 (Free/Open Source Version) and 0.9.8.753 (Pro) is vulnerable to Stored/Persistent XSS for Admin Email fields on the "CWP Settings > "Edit Settings" screen. By changing the email ID to any XSS Payload and clicking on Save Changes, the XSS Payload will execute.

**参考链接 / References**:
- http://forum.centos-webpanel.com/informations/
- http://packetstormsecurity.com/files/152437/CentOS-Web-Panel-0.9.8.793-Free-0.9.8.753-Pro-Cross-Site-Scripting.html
- http://www.securityfocus.com/bid/108035
- https://packetstormsecurity.com/files/152437/centoswp098email-xss.txt
- https://www.exploit-db.com/exploits/46669

---

#### 739. CVE-2019-11429

**严重程度 / Severity**: MEDIUM | CVSS: 4.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.793 (Free/Open Source Version), 0.9.8.753 (Pro) and 0.9.8.807 (Pro) is vulnerable to Reflected XSS for the "Domain" field on the "DNS Functions > "Add DNS Zone" screen.

**参考链接 / References**:
- http://packetstormsecurity.com/files/152696/CentOS-Web-Panel-Domain-Field-Cross-Site-Scripting.html
- https://CentOS-WebPanel.com
- https://www.exploit-db.com/exploits/46784/
- http://packetstormsecurity.com/files/152696/CentOS-Web-Panel-Domain-Field-Cross-Site-Scripting.html
- https://CentOS-WebPanel.com

---

#### 740. CVE-2019-12190

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
XSS was discovered in CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.747 via the testacc/fileManager2.php fm_current_dir or filename parameter.

**参考链接 / References**:
- https://github.com/tuyenhva/CVE-2019-12190
- https://github.com/tuyenhva/CVE-2019-12190

---

#### 741. CVE-2019-13360

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.836, remote attackers can bypass authentication in the login process by leveraging knowledge of a valid username.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13360.md
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13360.md

---

#### 742. CVE-2019-13383

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, the Login process allows attackers to check whether a username is valid by reading the HTTP response.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153667/CentOS-Control-Web-Panel-0.9.8.838-User-Enumeration.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13383.md
- https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2019-0010
- http://packetstormsecurity.com/files/153667/CentOS-Control-Web-Panel-0.9.8.838-User-Enumeration.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13383.md

---

#### 743. CVE-2019-13605

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.838 to 0.9.8.846, remote attackers can bypass authentication in the login process by leveraging the knowledge of a valid username. The attacker must defeat an encoding that is not equivalent to base64, and thus this is different from CVE-2019-13360.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13605.md
- https://www.exploit-db.com/exploits/47123
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13605.md

---

#### 744. CVE-2019-13359

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.836, a cwpsrv-xxx cookie allows a normal user to craft and upload a session file to the /tmp directory, and use it to become the root user.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153666/CentOS-Control-Web-Panel-0.9.8.836-Privilege-Escalation.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13359.md
- http://packetstormsecurity.com/files/153666/CentOS-Control-Web-Panel-0.9.8.836-Privilege-Escalation.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13359.md

---

#### 745. CVE-2019-13385

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.840, File and Directory Information Exposure in filemanager allows attackers to enumerate users and check for active users of the application by reading /tmp/login.log.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153877/CentOS-Control-Web-Panel-0.9.8.840-User-Enumeration.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13385.md
- http://packetstormsecurity.com/files/153877/CentOS-Control-Web-Panel-0.9.8.840-User-Enumeration.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 746. CVE-2019-13386

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, a hidden action=9 feature in filemanager2.php allows attackers to execute a shell command, i.e., obtain a reverse shell with user privilege.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153876/CentOS-Control-Web-Panel-0.9.8.836-Remote-Command-Execution.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13386.md
- http://packetstormsecurity.com/files/153876/CentOS-Control-Web-Panel-0.9.8.836-Remote-Command-Execution.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 747. CVE-2019-13387

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, Reflected XSS in filemanager2.php (parameter fm_current_dir) allows attackers to steal a cookie or session, or redirect to a phishing website.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153878/CentOS-Control-Web-Panel-0.9.8.846-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13387.md
- http://packetstormsecurity.com/files/153878/CentOS-Control-Web-Panel-0.9.8.846-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 748. CVE-2019-13477

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.837, CSRF in the forgot password function allows an attacker to change the password for the root account.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154217/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Request-Forgery.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13477.md
- http://packetstormsecurity.com/files/154217/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Request-Forgery.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13477.md

---

#### 749. CVE-2019-13599

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.848, the Login process allows attackers to check whether a username is valid by comparing response times.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154164/CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html

---

#### 750. CVE-2019-14245

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete databases (such as oauthv2) from the server via an attacker account.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154155/CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- http://packetstormsecurity.com/files/154155/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- http://packetstormsecurity.com/files/154155/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154155/CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html

---

#### 751. CVE-2019-14246

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to discover phpMyAdmin passwords (of any user in /etc/passwd) via an attacker account.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154156/CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- http://packetstormsecurity.com/files/154156/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- http://packetstormsecurity.com/files/154156/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154156/CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html

---

#### 752. CVE-2019-13476

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.837, XSS in the domain parameter allows a low-privilege user to achieve root access via the email list page.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154216/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Scripting.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13476.md
- http://packetstormsecurity.com/files/154216/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Scripting.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13476.md

---

#### 753. CVE-2019-14721

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to remove a target user from phpMyAdmin via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14721.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14721.md

---

#### 754. CVE-2019-14722

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete an e-mail forwarding destination from a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14722.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14722.md

---

#### 755. CVE-2019-14723

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a victim's e-mail account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14723.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14723.md

---

#### 756. CVE-2019-14726

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to access and delete DNS records of a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14726.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14726.md

---

#### 757. CVE-2019-14727

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to change the e-mail password of a victim account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14727.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14727.md

---

#### 758. CVE-2019-14728

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to add an e-mail forwarding destination to a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14728.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14728.md

---

#### 759. CVE-2019-14729

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a sub-domain from a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14729.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14729.md

---

#### 760. CVE-2019-14730

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a domain from a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14730.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14730.md

---

#### 761. CVE-2019-14724

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to edit an e-mail forwarding destination of a victim's account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14724.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14724.md

---

#### 762. CVE-2019-14725

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to change the e-mail usage value of a victim account via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14725.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14725.md

---

#### 763. CVE-2019-16295

**严重程度 / Severity**: MEDIUM | CVSS: 4.6

**漏洞描述 / Description**:
Stored XSS in filemanager2.php in CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.885 exists via the cmd_arg parameter. This can be exploited by a local attacker who supplies a crafted filename within a directory visited by the victim.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154990/CWP-0.9.8.885-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154990/CWP-0.9.8.885-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 764. CVE-2019-14782

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.856 through 0.9.8.864 allows an attacker to get a victim's session file name from the /tmp directory, and the victim's token value from /usr/local/cwpsrv/logs/access_log, then use them to make a request to extract the victim's password (for the OS and phpMyAdmin) via an attacker account.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html

---

#### 765. CVE-2019-15235

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.864 allows an attacker to get a victim's session file name from /home/[USERNAME]/tmp/session/sess_xxxxxx, and the victim's token value from /usr/local/cwpsrv/logs/access_log, then use them to gain access to the victim's password (for the OS and phpMyAdmin) via an attacker account. This is different from CVE-2019-14782.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html

---

#### 766. CVE-2020-10230

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel (for CentOS 6 and 7) allows SQL Injection via the /cwp_{SESSION_HASH}/admin/loader_ajax.php term parameter.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://www.exploit-db.com/exploits/48212
- https://centos-webpanel.com/changelog-cwp7
- https://www.exploit-db.com/exploits/48212

---

#### 767. CVE-2020-5291

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Bubblewrap (bwrap) before version 0.4.1, if installed in setuid mode and the kernel supports unprivileged user namespaces, then the `bwrap --userns2` option can be used to make the setuid process keep running as root while being traceable. This can in turn be used to gain root permissions. Note that this only affects the combination of bubblewrap in setuid mode (which is typically used when unprivileged user namespaces are not supported) and the support of unprivileged user namespaces. Known to be affected are: * Debian testing/unstable, if unprivileged user namespaces enabled (not default) * Debian buster-backports, if unprivileged user namespaces enabled (not default) * Arch if using `linux-hardened`, if unprivileged user namespaces enabled (not default) * Centos 7 flatpak COPR, if unprivileged user namespaces enabled (not default) This has been fixed in the 0.4.1 release, and all affected users should update.

**参考链接 / References**:
- https://github.com/containers/bubblewrap/commit/1f7e2ad948c051054b683461885a0215f1806240
- https://github.com/containers/bubblewrap/security/advisories/GHSA-j2qp-rvxj-43vj
- https://github.com/containers/bubblewrap/commit/1f7e2ad948c051054b683461885a0215f1806240
- https://github.com/containers/bubblewrap/security/advisories/GHSA-j2qp-rvxj-43vj

---

#### 768. CVE-2020-15420

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-el7-0.9.8.891. Authentication is not required to exploit this vulnerability. The specific flaw exists within loader_ajax.php. When parsing the line parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9259.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-737/
- https://www.zerodayinitiative.com/advisories/ZDI-20-737/

---

#### 769. CVE-2020-15421

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the check_ip parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9707.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-738/
- https://www.zerodayinitiative.com/advisories/ZDI-20-738/

---

#### 770. CVE-2020-15422

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the archivo parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9731.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-739/
- https://www.zerodayinitiative.com/advisories/ZDI-20-739/

---

#### 771. CVE-2020-15423

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the dominio parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9732.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-740/
- https://www.zerodayinitiative.com/advisories/ZDI-20-740/

---

#### 772. CVE-2020-15424

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the domain parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9735.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-741/
- https://www.zerodayinitiative.com/advisories/ZDI-20-741/

---

#### 773. CVE-2005-4728

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability (RPATH) in amaya 9.2.1 on Debian GNU/Linux allows local users to gain privileges via a malicious Mesa library in the /home/anand directory.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=341424
- http://www.securityfocus.com/bid/16945
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=341424
- http://www.securityfocus.com/bid/16945

---

#### 774. CVE-2006-1244

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
Unspecified vulnerability in certain versions of xpdf after 3.00, as used in various products including (a) pdfkit.framework, (b) gpdf, (c) pdftohtml, and (d) libextractor, has unknown impact and user-assisted attack vectors, possibly involving errors in (1) gmem.c, (2) SplashXPathScanner.cc, (3) JBIG2Stream.cc, (4) JPXStream.cc, and/or (5) Stream.cc.  NOTE: this description is based on Debian advisory DSA 979, which is based on changes that were made after other vulnerabilities such as CVE-2006-0301 and CVE-2005-3624 through CVE-2005-3628 were fixed.  Some of these newer fixes appear to be security-relevant, although it is not clear if they fix specific issues or are defensive in nature.

**参考链接 / References**:
- http://secunia.com/advisories/18948
- http://secunia.com/advisories/19021
- http://secunia.com/advisories/19065
- http://secunia.com/advisories/19091
- http://secunia.com/advisories/19164

---

#### 775. CVE-2006-1319

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
chpst in runit 1.3.3-1 for Debian GNU/Linux, when compiled on little endian i386 machines against dietlibc, does not properly handle when multiple groups are specified in the -u option, which causes chpst to assign permissions for the root group due to inconsistent bit sizes for the gid_t type.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=356016
- http://secunia.com/advisories/19323
- http://www.securityfocus.com/bid/17179
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25419
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=356016

---

#### 776. CVE-2006-1320

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
util.c in rssh 2.3.0 in Debian GNU/Linux does not use braces to make a block, which causes a check for CVS to always succeed and allows rsync and rdist to bypass intended access restrictions in rssh.conf.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=346322
- http://secunia.com/advisories/21087
- http://www.debian.org/security/2006/dsa-1109
- http://www.securityfocus.com/bid/18999
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25424

---

#### 777. CVE-2006-0050

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
snmptrapfmt in Debian 3.0 allows local users to overwrite arbitrary files via a symlink attack on a temporary log file.

**参考链接 / References**:
- http://secunia.com/advisories/19318
- http://www.debian.org/security/2006/dsa-1013
- http://www.securityfocus.com/bid/17182
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25442
- http://secunia.com/advisories/19318

---

#### 778. CVE-2006-1376

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The installation of Debian GNU/Linux 3.1r1 from the network install CD creates /var/log/debian-installer/cdebconf with world writable permissions, which allows local users to cause a denial of service (disk consumption).

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=358210
- http://secunia.com/advisories/19331
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25526
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=358210
- http://secunia.com/advisories/19331

---

#### 779. CVE-2006-1564

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in libapache2-svn 1.3.0-4 for Subversion in Debian GNU/Linux includes RPATH values under the /tmp/svn directory for the (1) mod_authz_svn.so and (2) mod_dav_svn.so modules, which might allow local users to gain privileges by installing malicious libraries in that directory.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359234
- http://www.securityfocus.com/bid/17288
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25680
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359234
- http://www.securityfocus.com/bid/17288

---

#### 780. CVE-2006-1565

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in libgpib-perl 3.2.06-2 in Debian GNU/Linux includes an RPATH value under the /tmp/buildd directory for the LinuxGpib.so module, which might allow local users to gain privileges by installing malicious libraries in that directory.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359239
- http://www.securityfocus.com/bid/17288
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25681
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359239
- http://www.securityfocus.com/bid/17288

---

#### 781. CVE-2006-1566

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in libtunepimp-perl 0.4.2-1 in Debian GNU/Linux includes an RPATH value under the /tmp/buildd directory for the tunepimp.so module, which might allow local users to gain privileges by installing malicious libraries in that directory.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359241
- http://www.securityfocus.com/bid/17288
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25682
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=359241
- http://www.securityfocus.com/bid/17288

---

#### 782. CVE-2006-1772

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
debconf in Debian GNU/Linux, when configuring mnogosearch in the mnogosearch-common 3.2.31-1 package, uses the world-readable config.dat file instead of the restricted passwords.dat for storing the cleartext database administrator password in the mnogosearch-common/database_admin_pass record, which allows local users to view the password.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=361775
- http://secunia.com/advisories/19589
- http://www.securityfocus.com/bid/17477
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=361775
- http://secunia.com/advisories/19589

---

#### 783. CVE-2006-1844

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Debian installer for the (1) shadow 4.0.14 and (2) base-config 2.53.10 packages includes sensitive information in world-readable log files, including preseeded passwords and pppoeconf passwords, which might allow local users to gain privileges.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=356939
- http://secunia.com/advisories/19170
- http://www.osvdb.org/23922
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=356939
- http://secunia.com/advisories/19170

---

#### 784. CVE-2006-2443

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Debian package of knowledgetree 2.0.7 creates environment.php with world-readable permissions, which allows local users to obtain sensitive information such as the username and password for the KnowledgeTree database.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=348306
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=348306

---

#### 785. CVE-2006-2542

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
xmcdconfig in xmcd for Debian GNU/Linux 2.6-17.1 creates /var/lib/cddb and /var/lib/xmcd/discog with world writable permissions, which allows local users to cause a denial of service (disk consumption).

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=366816
- http://secunia.com/advisories/20078
- http://www.debian.org/security/2006/dsa-1086
- https://exchange.xforce.ibmcloud.com/vulnerabilities/26452
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=366816

---

#### 786. CVE-2006-3123

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Multiple integer overflows in the (1) dodecrypt and (2) doencrypt functions in cfs_fh.c in cfsd in Matt Blaze Cryptographic File System (CFS) 1.4.1 before Debian GNU/Linux package 1.4.1-17 allow local users to cause a denial of service (daemon crash) by appending data to a file that is larger than 2 Gb.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=371076
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=371076
- http://secunia.com/advisories/21310
- http://secunia.com/advisories/21341
- http://www.debian.org/security/2006/dsa-1138

---

#### 787. CVE-2006-4248

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
thttpd on Debian GNU/Linux, and possibly other distributions, allows local users to create or touch arbitrary files via a symlink attack on the start_thttpd temporary file.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=396277
- http://secunia.com/advisories/22712
- http://www.debian.org/security/2006/dsa-1205
- http://www.securityfocus.com/bid/20891
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=396277

---

#### 788. CVE-2006-7094

**严重程度 / Severity**: N/A | CVSS: 8.5

**漏洞描述 / Description**:
ftpd, as used by Gentoo and Debian Linux, sets the gid to the effective uid instead of the effective group id before executing /bin/ls, which allows remote authenticated users to list arbitrary directories with the privileges of gid 0 and possibly enable additional attack vectors.

**参考链接 / References**:
- http://bugs.debian.org/384454
- http://bugs.gentoo.org/show_bug.cgi?id=155317
- http://osvdb.org/34242
- http://packages.qa.debian.org/l/linux-ftpd/news/20061125T181702Z.html
- http://securityreason.com/securityalert/2330

---

#### 789. CVE-2006-7098

**严重程度 / Severity**: N/A | CVSS: 6.6

**漏洞描述 / Description**:
The Debian GNU/Linux 033_-F_NO_SETSID patch for the Apache HTTP Server 1.3.34-4 does not properly disassociate httpd from a controlling tty when httpd is started interactively, which allows local users to gain privileges to that tty via a CGI program that calls the TIOCSTI ioctl.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2007-02/0579.html
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=357561
- http://osvdb.org/33816
- http://secunia.com/advisories/24324
- http://www.securityfocus.com/bid/22732

---

#### 790. CVE-2007-2524

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in index.pl in Open Ticket Request System (OTRS) 2.0.x allows remote attackers to inject arbitrary web script or HTML via the Subaction parameter in an AgentTicketMailbox Action.  NOTE: DEBIAN:DSA-1299 originally used this identifier for an ipsec-tools issue, but the proper identifier for the ipsec-tools issue is CVE-2007-1841.

**参考链接 / References**:
- http://osvdb.org/35821
- http://osvdb.org/35822
- http://secunia.com/advisories/25205
- http://secunia.com/advisories/25419
- http://secunia.com/advisories/25787

---

#### 791. CVE-2007-1663

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in the image message functionality in ekg before 1:1.7~rc2-1etch1 on Debian GNU/Linux Etch allows remote attackers to cause a denial of service.

**参考链接 / References**:
- http://osvdb.org/45377
- http://www.debian.org/security/2007/dsa-1318
- http://www.securityfocus.com/bid/24600
- https://exchange.xforce.ibmcloud.com/vulnerabilities/35134
- http://osvdb.org/45377

---

#### 792. CVE-2007-1664

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ekg before 1:1.7~rc2-1etch1 on Debian GNU/Linux Etch allows remote attackers to cause a denial of service (NULL pointer dereference) via a vector related to the token OCR functionality.

**参考链接 / References**:
- http://osvdb.org/45378
- http://www.debian.org/security/2007/dsa-1318
- http://www.securityfocus.com/bid/24600
- https://exchange.xforce.ibmcloud.com/vulnerabilities/35135
- http://osvdb.org/45378

---

#### 793. CVE-2007-1665

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in the token OCR functionality in ekg before 1:1.7~rc2-1etch1 on Debian GNU/Linux Etch allows remote attackers to cause a denial of service.

**参考链接 / References**:
- http://osvdb.org/45379
- http://www.debian.org/security/2007/dsa-1318
- http://www.securityfocus.com/bid/24600
- https://exchange.xforce.ibmcloud.com/vulnerabilities/35136
- http://osvdb.org/45379

---

#### 794. CVE-2007-3912

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
checkrestart in debian-goodies before 0.34 allows local users to gain privileges via shell metacharacters in the name of the executable file for a running process.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=440411
- http://osvdb.org/40483
- http://secunia.com/advisories/26675
- http://secunia.com/advisories/27079
- http://www.debian.org/security/2008/dsa-1527

---

#### 795. CVE-2007-5193

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration for twiki 4.1.2 on Debian GNU/Linux, and possibly other operating systems, specifies the work area directory (cfg{RCS}{WorkAreaDir}) under the web document root, which might allow remote attackers to obtain sensitive information when .htaccess restrictions are not applied.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=444982
- http://osvdb.org/42338
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=444982
- http://osvdb.org/42338

---

#### 796. CVE-2007-5469

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
OpenSER 1.2.2 does not verify the Digest authentication header URI against the Request URI in SIP messages, which allows remote attackers to use sniffed Digest authentication credentials to call arbitrary telephone numbers or spoof caller ID (aka "toll fraud and authentication forward attack").  NOTE: Debian disputes this issue, stating that "having the two URIs mismatch is allowed by the standard and happens in some setups for valid reasons.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=446956
- http://lists.grok.org.uk/pipermail/full-disclosure/2007-October/066581.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2007-October/066691.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2007-October/066694.html
- http://secunia.com/advisories/27204

---

#### 797. CVE-2007-5828

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Cross-site request forgery (CSRF) vulnerability in the admin panel in Django 0.96 allows remote attackers to change passwords of arbitrary users via a request to admin/auth/user/1/password/.  NOTE: this issue has been disputed by Debian, since product documentation includes a recommendation for a CSRF protection module that is included with the product.  However, CVE considers this an issue because the default configuration does not use this module

**参考链接 / References**:
- http://osvdb.org/45285
- http://securityreason.com/securityalert/3338
- http://www.securityfocus.com/archive/1/482983/100/0/threaded
- http://osvdb.org/45285
- http://securityreason.com/securityalert/3338

---

#### 798. CVE-2007-6211

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Send ICMP Nasty Garbage (sing) on Debian GNU/Linux allows local users to append to arbitrary files and gain privileges via the -L (output log file) option.  NOTE: this issue is only a vulnerability in limited environments, since sing is not installed setuid, and the administrator would need to override a non-setuid default during installation.

**参考链接 / References**:
- http://osvdb.org/44157
- http://securityreason.com/securityalert/3412
- http://www.securityfocus.com/archive/1/484472/100/0/threaded
- http://www.securityfocus.com/archive/1/484591/100/200/threaded
- http://www.securityfocus.com/bid/26679

---

#### 799. CVE-2007-6418

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The libdspam7-drv-mysql cron job in Debian GNU/Linux includes the MySQL dspam database password in a command line argument, which might allow local users to read the password by listing the process and its arguments.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=448519
- http://osvdb.org/44138
- http://secunia.com/advisories/29059
- http://www.debian.org/security/2008/dsa-1501
- http://www.securityfocus.com/bid/27938

---

#### 800. CVE-2008-0930

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
w_editeur.c in XWine 1.0.1 for Debian GNU/Linux allows local users to overwrite or print arbitrary files via a symlink attack on the temporaire temporary file.  NOTE: some of these details are obtained from third party information.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=468050
- http://secunia.com/advisories/29125
- http://secunia.com/advisories/29452
- http://www.debian.org/security/2008/dsa-1526
- http://www.securityfocus.com/bid/28049

---

#### 801. CVE-2008-0931

**严重程度 / Severity**: N/A | CVSS: 6.3

**漏洞描述 / Description**:
w_export.c in XWine 1.0.1 on Debian GNU/Linux sets insecure permissions (0666) for /etc/wine/config, which might allow local users to execute arbitrary commands or cause a denial of service by modifying the file.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=468050
- http://secunia.com/advisories/29125
- http://secunia.com/advisories/29452
- http://www.debian.org/security/2008/dsa-1526
- http://www.securityfocus.com/bid/28369

---

#### 802. CVE-2008-1771

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Integer overflow in the ws_getpostvars function in Firefly Media Server (formerly mt-daapd) 0.2.4.1 (0.9~r1696-1.2 on Debian) allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP POST request with a large Content-Length.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=476241
- http://secunia.com/advisories/29917
- http://secunia.com/advisories/29919
- http://secunia.com/advisories/30661
- http://sourceforge.net/project/shownotes.php?release_id=593465&group_id=98211

---

#### 803. CVE-2008-0166

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
OpenSSL 0.9.8c-1 up to versions before 0.9.8g-9 on Debian-based operating systems uses a random number generator that generates predictable numbers, which makes it easier for remote attackers to conduct brute force guessing attacks against cryptographic keys.

**参考链接 / References**:
- http://metasploit.com/users/hdm/tools/debian-openssl/
- http://secunia.com/advisories/30136
- http://secunia.com/advisories/30220
- http://secunia.com/advisories/30221
- http://secunia.com/advisories/30231

---

#### 804. CVE-2008-3234

**严重程度 / Severity**: N/A | CVSS: 6.5

**漏洞描述 / Description**:
sshd in OpenSSH 4 on Debian GNU/Linux, and the 20070303 OpenSSH snapshot, allows remote authenticated users to obtain access to arbitrary SELinux roles by appending a :/ (colon slash) sequence, followed by the role name, to the username.

**参考链接 / References**:
- http://www.securityfocus.com/bid/30276
- https://exchange.xforce.ibmcloud.com/vulnerabilities/44037
- https://www.exploit-db.com/exploits/6094
- http://www.securityfocus.com/bid/30276
- https://exchange.xforce.ibmcloud.com/vulnerabilities/44037

---

#### 805. CVE-2008-4109

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A certain Debian patch for OpenSSH before 4.3p2-9etch3 on etch; before 4.6p1-1 on sid and lenny; and on other distributions such as SUSE uses functions that are not async-signal-safe in the signal handler for login timeouts, which allows remote attackers to cause a denial of service (connection slot exhaustion) via multiple login attempts. NOTE: this issue exists because of an incorrect fix for CVE-2006-5051.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=498678
- http://lists.opensuse.org/opensuse-security-announce/2008-10/msg00004.html
- http://secunia.com/advisories/31885
- http://secunia.com/advisories/32080
- http://secunia.com/advisories/32181

---

#### 806. CVE-2008-4099

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
PyDNS (aka python-dns) before 2.3.1-4 in Debian GNU/Linux does not use random source ports or transaction IDs for DNS requests, which makes it easier for remote attackers to spoof DNS responses, a different vulnerability than CVE-2008-1447.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=490217
- http://packages.debian.org/changelogs/pool/main/p/python-dns/python-dns_2.3.3-1/changelog
- http://www.openwall.com/lists/oss-security/2008/09/11/1
- http://www.openwall.com/lists/oss-security/2008/09/16/4
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=490217

---

#### 807. CVE-2008-4126

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
PyDNS (aka python-dns) before 2.3.1-5 in Debian GNU/Linux does not use random source ports for DNS requests and does not use random transaction IDs for DNS retries, which makes it easier for remote attackers to spoof DNS responses, a different vulnerability than CVE-2008-1447.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2008-4099.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=490217
- http://packages.debian.org/changelogs/pool/main/p/python-dns/python-dns_2.3.3-1/changelog
- http://www.openwall.com/lists/oss-security/2008/09/11/1
- http://www.openwall.com/lists/oss-security/2008/09/16/4
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=490217

---

#### 808. CVE-2008-4406

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
A certain Debian patch to the run scripts for sabre (aka xsabre) 0.2.4b allows local users to delete or overwrite arbitrary files via a symlink attack on unspecified .tmp files.

**参考链接 / References**:
- http://bugs.debian.org/433996
- http://openwall.com/lists/oss-security/2008/10/01/1
- http://osvdb.org/48895
- http://www.securityfocus.com/bid/31512
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45609

---

#### 809. CVE-2008-4553

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
qemu-make-debian-root in qemu 0.9.1-5 on Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack on temporary files and directories.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=496394
- http://dev.gentoo.org/~rbu/security/debiantemp/qemu
- http://secunia.com/advisories/32335
- http://uvw.ru/report.lenny.txt
- http://www.debian.org/security/2008/dsa-1657

---

#### 810. CVE-2008-3831

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
The i915 driver in (1) drivers/char/drm/i915_dma.c in the Linux kernel 2.6.24 on Debian GNU/Linux and (2) sys/dev/pci/drm/i915_drv.c in OpenBSD does not restrict the DRM_I915_HWS_ADDR ioctl to the Direct Rendering Manager (DRM) master, which allows local users to cause a denial of service (memory corruption) via a crafted ioctl call, related to absence of the DRM_MASTER and DRM_ROOT_ONLY flags in the ioctl's configuration.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/openbsd/cvs/2008-10/0365.html
- http://secunia.com/advisories/32315
- http://secunia.com/advisories/32386
- http://secunia.com/advisories/32709
- http://secunia.com/advisories/32918

---

#### 811. CVE-2008-5142

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
sendbug in freebsd-sendpr 3.113+5.3 on Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack on a /tmp/pr.##### temporary file.

**参考链接 / References**:
- http://lists.debian.org/debian-devel/2008/08/msg00285.html
- http://www.securityfocus.com/bid/32381
- http://lists.debian.org/debian-devel/2008/08/msg00285.html
- http://www.securityfocus.com/bid/32381

---

#### 812. CVE-2008-5366

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The postinst script in ppp 2.4.4rel on Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack on the (1) /tmp/probe-finished or (2) /tmp/ppp-errors temporary file.

**参考链接 / References**:
- http://lists.debian.org/debian-devel/2008/08/msg00283.html
- http://www.securityfocus.com/bid/32740
- http://lists.debian.org/debian-devel/2008/08/msg00283.html
- http://www.securityfocus.com/bid/32740

---

#### 813. CVE-2008-5367

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
ip-up in ppp-udeb 2.4.4rel on Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack on the /tmp/resolv.conf.tmp temporary file.

**参考链接 / References**:
- http://lists.debian.org/debian-devel/2008/08/msg00283.html
- http://lists.debian.org/debian-devel/2008/08/msg00283.html

---

#### 814. CVE-2008-5394

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
/bin/login in shadow 4.0.18.1 in Debian GNU/Linux, and probably other Linux distributions, allows local users in the utmp group to overwrite arbitrary files via a symlink attack on a temporary file referenced in a line (aka ut_line) field in a utmp entry.

**参考链接 / References**:
- http://bugs.debian.org/332198
- http://bugs.debian.org/505071
- http://bugs.debian.org/505271
- http://osvdb.org/52200
- http://security.gentoo.org/glsa/glsa-200903-24.xml

---

#### 815. CVE-2009-1381

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The map_yp_alias function in functions/imap_general.php in SquirrelMail before 1.4.19-1 on Debian GNU/Linux, and possibly other operating systems and versions, allows remote attackers to execute arbitrary commands via shell metacharacters in a username string that is used by the ypmatch program.  NOTE: this issue exists because of an incomplete fix for CVE-2009-1579.

**参考链接 / References**:
- http://release.debian.org/proposed-updates/stable_diffs/squirrelmail_1.4.15-4+lenny2.debdiff
- http://secunia.com/advisories/35140
- http://www.debian.org/security/2009/dsa-1802
- http://www.mandriva.com/security/advisories?name=MDVSA-2009:122
- http://www.securityfocus.com/archive/1/503718/100/0/threaded

---

#### 816. CVE-2009-2946

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Eval injection vulnerability in scripts/uscan.pl before Rev 1984 in devscripts allows remote attackers to execute arbitrary Perl code via crafted pathnames on distribution servers for upstream source code used in Debian GNU/Linux packages.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=515209
- http://svn.debian.org/wsvn/devscripts/trunk/scripts/uscan.pl?op=diff&rev=1984&sc=1
- http://svn.debian.org/wsvn/devscripts/trunk/scripts/uscan.pl?op=log&rev=0&sc=1&isdir=0
- http://www.debian.org/security/2009/dsa-1878
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=515209

---

#### 817. [Ubuntu] USN-8226-2: kmod update

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
USN-8226-1 added a mitigation to kmod to disable loading the algif_aead module. This update adds the same mitigation to Ubuntu 14.04 LTS, Ubuntu 16.04 LTS, Ubuntu 18.04 LTS, and Ubuntu 20.04 LTS. Original advisory details: It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disabl

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-2

---

#### 818. [Ubuntu] USN-8225-1: Python marshmallow vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Jared Deckard discovered that Python marshmallow did not correctly handle hiding certain fields. An attacker could possibly use this issue to leak sensitive information. This issue only affected Ubuntu 18.04 LTS. (CVE-2018-17175) It was discovered that Python marshmallow did not efficiently handle merging certain objects. An attacker could possibly use this issue to cause a denial of service. This

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8225-1

---

#### 819. [Ubuntu] USN-8224-1: Linux kernel (BlueField) vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Qualys discovered that several vulnerabilities existed in the AppArmor Linux kernel Security Module (LSM). An unprivileged local attacker could use these issues to load, replace, and remove arbitrary AppArmor profiles causing denial of service, exposure of sensitive information (kernel memory), local privilege escalation, or possibly escape a container. (LP: #2143853, CVE-2026-23268, CVE-2026-2326

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8224-1

---

#### 820. [Ubuntu] USN-8223-1: Roundcube Webmail vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that Roundcube Webmail mishandled Punycode xn-- domain names. An attacker could possibly use this issue to cause a homograph attack. (CVE-2019-15237) It was discovered that Roundcube Webmail did not properly sanitize certain attributes when handling CSS within HTML messages and certain SVG attributes. An attacker could possibly use this issue to cause a cross-site scripting attac

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8223-1

---

#### 821. [Ubuntu] USN-8222-1: OpenSSH vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Christos Papakonstantinou discovered that the OpenSSH scp tool incorrectly handled the legacy scp protocol (-O) option. This could result in certain files being installed setuid or setgid, contrary to expectations. (CVE-2026-35385) Florian Kohnhäuser discovered that OpenSSH incorrectly handled shell metacharacters in usernames within a command line. When untrusted usernames and non-default configu

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8222-1

---

#### 822. [Ubuntu] USN-8221-1: wheel vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that wheel did not correctly handle certain file paths. If a user or automated system were tricked into opening a specially crafted file, an attacker could possibly use this issue to execute arbitrary code.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8221-1

---

#### 823. [Ubuntu] USN-8219-1: UltraJSON vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Cameron Criswell discovered that UltraJSON contained a memory leak that would occur when parsing large integers. An attacker could possibly use this issue to cause UltraJSON to crash, resulting in a denial of service. This issue only affected Ubuntu 24.04 LTS, Ubuntu 25.10, and Ubuntu 26.04 LTS. (CVE-2026-32874) It was discovered that UltraJSON contained integer overflow/underflow issues when calc

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8219-1

---

#### 824. [Ubuntu] USN-8216-1: .NET vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Ludvig Pedersen discovered that the System.Security.Cryptography.Xml library in .NET incorrectly handled certain XML inputs. An attacker could possibly use this issue to consume excessive resources, resulting in a denial of service. (CVE-2026-33116, CVE-2026-26171) Ludvig Pedersen and Kevin Jones discovered that the System.Security.Cryptography.Xml library in .NET incorrectly handled certain XML i

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8216-1

---

#### 825. [Ubuntu] USN-8215-1: .NET vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that the Microsoft.AspNetCore.DataProtection library in .NET did not properly verify cryptographic signatures under certain conditions. A remote attacker could possibly use this issue to elevate privileges.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8215-1

---

#### 826. [Ubuntu] USN-8214-1: NLTK vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that NLTK incorrectly handled file extraction when opening a maliciously crafted zip file. An attacker could possibly use this issue to create or overwrite files on the system and execute arbitrary code.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8214-1

---

#### 827. [Ubuntu] USN-8213-1: Vim vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Michał Majchrowicz discovered that Vim's zip plugin could overwrite arbitrary files. An attacker could possibly use this issue to delete sensitive data or execute arbitrary code. This issue only affected Ubuntu 24.04 LTS and Ubuntu 25.10. (CVE-2026-35177) It was discovered that Vim's netbeans interface did not properly sanitize certain strings. An attacker could possibly use this issue to execute

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8213-1

---

#### 828. [Ubuntu] USN-8212-1: authd vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that authd incorrectly assigned the primary group ID to users under certain conditions. A local attacker could possibly use this issue to achieve privilege escalation, or gain unauthorized access to files belonging to other users.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8212-1

---

#### 829. [Ubuntu] USN-8211-1: Pillow vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that Pillow incorrectly handled certain FITS images. An attacker could possibly use this issue to cause Pillow to consume resources, leading to a denial of service.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8211-1

---

#### 830. [Ubuntu] USN-8210-1: nginx vulnerabilities

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that the nginx ngx_mail_auth_http_module module incorrectly handled certain requests. An attacker could possibly use this issue to cause nginx to crash, resulting in a denial of service. (CVE-2026-27651) It was discovered that the nginx ngx_http_dav_module module incorrectly handled certain destination URIs. An attacker could use this issue to cause nginx to crash, resulting in a

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8210-1

---

#### 831. [Ubuntu] USN-8209-1: Little CMS vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that Little CMS incorrectly handled certain malformed ICC profiles. An attacker could use this issue to cause Little CMS to crash, resulting in a denial of service, or possibly execute arbitrary code.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8209-1

---

#### 832. [Ubuntu] USN-8208-1: HAProxy vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
Martino Spagnuolo discovered that HAProxy did not check received body lengths in the HTTP/3 parser. A remote attacker could possibly use this issue to perform a request smuggling attack and obtain sensitive information.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8208-1

---

#### 833. [Ubuntu] USN-8207-1: ClamAV vulnerability

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
It was discovered that ClamAV incorrectly handled certain HTML files. A remote attacker could possibly use this issue to cause ClamAV to crash, resulting in a denial of service.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8207-1

---

#### 834. [SUSE] SUSE-SU-2026:1667-1: low: Security update for python-Pygments

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for python-Pygments Announcement ID: SUSE-SU-2026:1667-1 Release Date: 2026-04-30T17:22:44Z Rating: low References: * bsc#1260796 Cross-References: * CVE-2026-4539 CVSS scores: * CVE-2026-4539 ( SUSE ): 3.3 CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L * CVE-2026-4539 ( NVD ): 1.9 CVSS:4.0/AV:L/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N/E:P/CR:X/IR:X/AR:X/MAV:X/MAC:X/MAT:X/

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-May.txt

---

#### 835. [SUSE] SUSE-SU-2026:1668-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for the Linux Kernel Announcement ID: SUSE-SU-2026:1668-1 Release Date: 2026-05-01T08:37:57Z Rating: important References: * bsc#1220186 * bsc#1228031 * bsc#1246057 * bsc#1249522 * bsc#1257221 * bsc#1257773 * bsc#1258280 * bsc#1259770 * bsc#1259797 * bsc#1259865 * bsc#1259870 * bsc#1259889 * bsc#1259997 * bsc#1260009 * bsc#1260489 * bsc#1260536 * bsc#1260551 * bsc#1260730 * bsc#1

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-May.txt

---

#### 836. [SUSE] SUSE-SU-2026:20947-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 2 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20947-1 Release Date: 2026-03-25T18:17:14Z Rating: important References: * bsc#1255052 * bsc#1255053 * bsc#1255378 * bsc#1255402 * bsc#1255895 * bsc#1256624 * bsc#1256644 * bsc#1257669 Cross-References: * CVE-2025-40214 * CVE-2025-40258 * CVE-2025-40284 * CVE-2025-40297 * CVE-2025-68284

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 837. [SUSE] SUSE-SU-2026:20946-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 0 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20946-1 Release Date: 2026-03-25T18:09:48Z Rating: important References: * bsc#1247240 * bsc#1255052 * bsc#1255053 * bsc#1255378 * bsc#1255402 * bsc#1255895 * bsc#1256624 * bsc#1256644 * bsc#1257669 Cross-References: * CVE-2025-38488 * CVE-2025-40214 * CVE-2025-40258 * CVE-2025-40284 *

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 838. [SUSE] SUSE-SU-2026:20943-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 4 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20943-1 Release Date: 2026-03-25T05:42:56Z Rating: important References: * bsc#1256624 * bsc#1256644 Cross-References: * CVE-2025-68813 * CVE-2025-71085 CVSS scores: * CVE-2025-68813 ( SUSE ): 8.7 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N * CVE-2025-68813 ( SUSE ):

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 839. [SUSE] SUSE-SU-2026:20942-1: important: Security update for the initial

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for the initial kernel livepatch Announcement ID: SUSE-SU-2026:20942-1 Release Date: 2026-03-24T20:14:20Z Rating: important References: Affected Products: * SUSE Linux Enterprise Server - BCI 16.0 An update that can now be installed. ## Description: This update contains initial livepatches for the SUSE Linux Enterprise Server 16.0 and SUSE Linux Micro 6.2 kernel update. ## Specia

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 840. [SUSE] SUSE-SU-2026:20941-1: moderate: Security update for ucode-intel

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for ucode-intel Announcement ID: SUSE-SU-2026:20941-1 Release Date: 2026-03-19T09:31:38Z Rating: moderate References: * bsc#1229129 * bsc#1230400 * bsc#1249138 * bsc#1253319 * bsc#1258046 Cross-References: * CVE-2024-24853 * CVE-2025-31648 CVSS scores: * CVE-2024-24853 ( SUSE ): 7.3 CVSS:4.0/AV:L/AC:H/AT:P/PR:H/UI:P/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H * CVE-2024-24853 ( SUSE ): 7.2 CVS

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 841. [SUSE] SUSE-SU-2026:20940-1: moderate: Security update for net-tools

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for net-tools Announcement ID: SUSE-SU-2026:20940-1 Release Date: 2026-03-26T15:12:43Z Rating: moderate References: * bsc#1243581 * bsc#1248410 * bsc#1248687 * bsc#142461 * bsc#430864 * bsc#544339 Cross-References: * CVE-2025-46836 CVSS scores: * CVE-2025-46836 ( SUSE ): 5.8 CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N * CVE-2025-46836 ( SUSE ): 6.6 CVSS:3.1/AV

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 842. [SUSE] SUSE-SU-2026:20936-1: important: Security update for openexr

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for openexr Announcement ID: SUSE-SU-2026:20936-1 Release Date: 2026-03-26T10:03:06Z Rating: important References: * bsc#1259177 Cross-References: * CVE-2026-27622 CVSS scores: * CVE-2026-27622 ( SUSE ): 8.4 CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N * CVE-2026-27622 ( SUSE ): 7.8 CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H * CVE-2026-27622 ( NVD ): 8.4 CVSS

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 843. [SUSE] SUSE-SU-2026:20935-1: moderate: Security update for fetchmail

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for fetchmail Announcement ID: SUSE-SU-2026:20935-1 Release Date: 2026-03-26T09:57:56Z Rating: moderate References: * bsc#1251194 Cross-References: * CVE-2025-61962 CVSS scores: * CVE-2025-61962 ( SUSE ): 5.9 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H * CVE-2025-61962 ( NVD ): 5.9 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H Affected Products: * SUSE Linux Enterprise Server - B

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 844. [SUSE] SUSE-SU-2026:20934-1: important: Security update for python-PyJWT

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for python-PyJWT Announcement ID: SUSE-SU-2026:20934-1 Release Date: 2026-03-25T18:08:48Z Rating: important References: * bsc#1259616 Cross-References: * CVE-2026-32597 CVSS scores: * CVE-2026-32597 ( SUSE ): 8.7 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N * CVE-2026-32597 ( SUSE ): 7.5 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N * CVE-2026-32597 ( NVD ): 7.5

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 845. [SUSE] SUSE-SU-2026:20933-1: moderate: Security update for python-ldap

**严重程度 / Severity**: UPDATE

**漏洞描述 / Description**:
# Security update for python-ldap Announcement ID: SUSE-SU-2026:20933-1 Release Date: 2026-03-25T10:40:32Z Rating: moderate References: * bsc#1251912 * bsc#1251913 Cross-References: * CVE-2025-61911 * CVE-2025-61912 CVSS scores: * CVE-2025-61911 ( SUSE ): 5.5 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N/E:P/CR:X/IR:X/AR:X/MAV:X/MAC:X/MAT:X/MPR:X/MUI:X/MVC:X/MVI:X/MVA:X/MSC:X/MSI

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 846. CVE-2003-0900

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Perl 5.8.1 on Fedora Core does not properly initialize the random number generator when forking, which makes it easier for attackers to predict random numbers.

**参考链接 / References**:
- https://bugzilla.redhat.com/bugzilla/long_list.cgi?buglist=108711
- https://bugzilla.redhat.com/bugzilla/long_list.cgi?buglist=108711

---

#### 847. CVE-2004-2502

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
im-switch before 11.4-46.1 in Fedora Core 2 allows local users to overwrite arbitrary files via a symlink attack on the imswitcher[PID] temporary file.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=126940
- http://packetstormsecurity.org/0407-advisories/fedora_im-switch_tempfile_race.txt
- http://secunia.com/advisories/12037
- http://www.osvdb.org/7772
- http://www.securityfocus.com/bid/10717

---

#### 848. CVE-2004-2655

**严重程度 / Severity**: N/A | CVSS: 5.4

**漏洞描述 / Description**:
rdesktop 1.3.1 with xscreensaver 4.14, and possibly other versions, when running on Fedora and possibly other platforms, does not release the keyboard focus when xscreensaver starts, which causes the password to be entered into the active window when the user unlocks the screen.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060602-01-U.asc
- http://secunia.com/advisories/20226
- http://secunia.com/advisories/20456
- http://secunia.com/advisories/20782
- http://secunia.com/advisories/22080

---

#### 849. CVE-2005-3630

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Fedora Directory Server before 10 allows remote attackers to obtain sensitive information, such as the password from adm.conf via an IFRAME element, probably involving an Apache httpd.conf configuration that orders "allow" directives before "deny" directives.

**参考链接 / References**:
- http://directory.fedora.redhat.com/wiki/FDS10Announcement
- http://secunia.com/advisories/18939
- http://www.securityfocus.com/bid/16729
- https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=121994
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=174837

---

#### 850. CVE-2006-0451

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Multiple memory leaks in the LDAP component in Fedora Directory Server 1.0 allow remote attackers to cause a denial of service (memory consumption) via invalid BER packets that trigger an error, which might prevent memory from being freed if it was allocated during the ber_scanf call, as demonstrated using the ProtoVer LDAP test suite.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24794
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135

---

#### 851. CVE-2006-0452

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
dn2ancestor in the LDAP component in Fedora Directory Server 1.0 allows remote attackers to cause a denial of service (CPU and memory consumption) via a ModDN operation with a DN that contains a large number of "," (comma) characters, which results in a large amount of recursion, as demonstrated using the ProtoVer LDAP test suite.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179137
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24796
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179137

---

#### 852. CVE-2006-0453

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
The LDAP component in Fedora Directory Server 1.0 allow remote attackers to cause a denial of service (crash) via a certain "bad BER sequence" that results in a free of uninitialized memory, as demonstrated using the ProtoVer LDAP test suite.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24795
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135

---

#### 853. CVE-2006-3742

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The KDE PAM configuration shipped with Fedora Core 5 causes KDM passwords to be cached, which allows attackers to login without a password by attempting to log in multiple times.

**参考链接 / References**:
- http://lwn.net/Alerts/197302/
- http://lwn.net/Alerts/197302/

---

#### 854. CVE-2006-5701

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Double free vulnerability in squashfs module in the Linux kernel 2.6.x, as used in Fedora Core 5 and possibly other distributions, allows local users to cause a denial of service by mounting a crafted squashfs filesystem.

**参考链接 / References**:
- http://projects.info-pull.com/mokb/MOKB-02-11-2006.html
- http://secunia.com/advisories/22655
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/24259

---

#### 855. CVE-2006-6057

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
The Linux kernel 2.6.x up to 2.6.18, and possibly other versions, on Fedora Core 6 and possibly other operating systems, allows local users to cause a denial of service (crash) via a malformed gfs2 file stream that triggers a NULL pointer dereference in the init_journal function.

**参考链接 / References**:
- http://projects.info-pull.com/mokb/MOKB-15-11-2006.html
- http://secunia.com/advisories/22886
- http://secunia.com/advisories/24098
- http://www.ubuntu.com/usn/usn-416-1
- http://www.vupen.com/english/advisories/2006/4556

---

#### 856. CVE-2006-7151

**严重程度 / Severity**: N/A | CVSS: 6.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in the libtool-ltdl library (libltdl.so) 1.5.22-2.3 in Fedora Core 5 might allow local users to execute arbitrary code via a malicious library in the (1) hwcap, (2) 0, and (3) nosegneg subdirectories.

**参考链接 / References**:
- http://securityreason.com/securityalert/2378
- http://www.securityfocus.com/archive/1/448153/100/0/threaded
- http://www.securityfocus.com/bid/20434
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=209930
- http://securityreason.com/securityalert/2378

---

#### 857. CVE-2007-2874

**严重程度 / Severity**: N/A | CVSS: 5.8

**漏洞描述 / Description**:
Buffer overflow in the wpa_printf function in the debugging code in wpa_supplicant in the Fedora NetworkManager package before 0.6.5-3.fc7 allows user-assisted remote attackers to execute arbitrary code via malformed frames on a WPA2 network.  NOTE: some of these details are obtained from third party information.

**参考链接 / References**:
- http://fedoraproject.org/wiki/FSA/F7/FEDORA-2007-0186
- http://osvdb.org/46833
- http://www.redhat.com/archives/fedora-package-announce/2007-June/msg00032.html
- http://www.vupen.com/english/advisories/2007/2053
- http://fedoraproject.org/wiki/FSA/F7/FEDORA-2007-0186

---

#### 858. CVE-2007-4364

**严重程度 / Severity**: N/A | CVSS: 8.5

**漏洞描述 / Description**:
Fedora Commons before 2.2.1 does not properly handle certain authentication requests involving Java Naming and Directory Interface (JNDI), related to (1) a nonexistent account name in combination with an empty password, which allows remote attackers to trigger a certain "unexpected / strange response" from an LDAP server, and (2) a reauthentication attempt that throws an exception, which allows remote attackers to trigger use of a cached authentication decision.  NOTE: authentication can be bypassed by using vector 1 followed by vector 2, and possibly can be bypassed by using a single vector.

**参考链接 / References**:
- http://osvdb.org/39548
- http://secunia.com/advisories/26445
- http://sourceforge.net/project/shownotes.php?release_id=531870
- http://sourceforge.net/tracker/index.php?func=detail&aid=1731608&group_id=177054&atid=879703
- http://www.securityfocus.com/bid/25317

---

#### 859. CVE-2007-4904

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
RealNetworks RealPlayer 10.1.0.3114 and earlier, and Helix Player 1.0.6.778 on Fedora Core 6 (FC6) and possibly other platforms, allow user-assisted remote attackers to cause a denial of service (application crash) via a malformed .au file that triggers a divide-by-zero error.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2007-09/0154.html
- http://osvdb.org/39904
- http://www.securityfocus.com/archive/1/479081/100/0/threaded
- http://www.securityfocus.com/bid/25627
- https://exchange.xforce.ibmcloud.com/vulnerabilities/36545

---

#### 860. CVE-2007-3102

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Unspecified vulnerability in the linux_audit_record_event function in OpenSSH 4.3p2, as used on Fedora Core 6 and possibly other systems, allows remote attackers to write arbitrary characters to an audit log via a crafted username.  NOTE: some of these details are obtained from third party information.

**参考链接 / References**:
- http://osvdb.org/39214
- http://secunia.com/advisories/27235
- http://secunia.com/advisories/27588
- http://secunia.com/advisories/27590
- http://secunia.com/advisories/28319

---

#### 861. CVE-2008-2359

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configuration of consolehelper in system-config-network before 1.5.10-1 on Fedora 8 lacks the USER=root directive, which allows local users of the workstation console to gain privileges and change the network configuration.

**参考链接 / References**:
- http://secunia.com/advisories/30399
- https://bugzilla.redhat.com/show_bug.cgi?id=448557
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42867
- https://www.redhat.com/archives/fedora-package-announce/2008-May/msg00974.html
- http://secunia.com/advisories/30399

---

#### 862. CVE-2008-3524

**严重程度 / Severity**: N/A | CVSS: 4.7

**漏洞描述 / Description**:
rc.sysinit in initscripts before 8.76.3-1 on Fedora 9 and other Linux platforms allows local users to delete arbitrary files via a symlink attack on a file or directory under (1) /var/lock or (2) /var/run.

**参考链接 / References**:
- http://secunia.com/advisories/32037
- http://secunia.com/advisories/32710
- http://wiki.rpath.com/wiki/Advisories:rPSA-2008-0318
- http://www.securityfocus.com/bid/31385
- https://bugzilla.redhat.com/show_bug.cgi?id=458504

---

#### 863. CVE-2008-3832

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
A certain Fedora patch for the utrace subsystem in the Linux kernel before 2.6.26.5-28 on Fedora 8, and before 2.6.26.5-45 on Fedora 9, allows local users to cause a denial of service (NULL pointer dereference and system crash or hang) via a call to the utrace_control function.

**参考链接 / References**:
- http://kerneloops.org/oops.php?number=56705
- http://www.openwall.com/lists/oss-security/2008/10/02/1
- http://www.securityfocus.com/bid/31536
- https://bugzilla.redhat.com/show_bug.cgi?id=464883
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45644

---

#### 864. CVE-2008-4315

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
tog-pegasus in OpenGroup Pegasus 2.7.0 on Red Hat Enterprise Linux (RHEL) 5, Fedora 9, and Fedora 10 does not log failed authentication attempts to the OpenPegasus CIM server, which makes it easier for remote attackers to avoid detection of password guessing attacks.

**参考链接 / References**:
- http://osvdb.org/50278
- http://secunia.com/advisories/32862
- http://www.redhat.com/support/errata/RHSA-2008-1001.html
- http://www.securitytracker.com/id?1021281
- https://admin.fedoraproject.org/updates/tog-pegasus-2.7.0-7.fc9

---

#### 865. CVE-2009-0180

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Certain Fedora build scripts for nfs-utils before 1.1.2-9.fc9 on Fedora 9, and before 1.1.4-6.fc10 on Fedora 10, omit TCP Wrapper support, which might allow remote attackers to bypass intended access restrictions, possibly a related issue to CVE-2008-1376.

**参考链接 / References**:
- http://secunia.com/advisories/33545
- http://www.securityfocus.com/bid/33294
- https://bugzilla.redhat.com/show_bug.cgi?id=477864
- https://exchange.xforce.ibmcloud.com/vulnerabilities/48058
- https://www.redhat.com/archives/fedora-package-announce/2009-January/msg00376.html

---

#### 866. CVE-2008-6552

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
Red Hat Cluster Project 2.x allows local users to modify or overwrite arbitrary files via symlink attacks on files in /tmp, involving unspecified components in Resource Group Manager (aka rgmanager) before 2.03.09-1, gfs2-utils before 2.03.09-1, and CMAN - The Cluster Manager before 2.03.09-1 on Fedora 9.

**参考链接 / References**:
- http://osvdb.org/50299
- http://osvdb.org/50300
- http://osvdb.org/50301
- http://rhn.redhat.com/errata/RHSA-2009-1337.html
- http://secunia.com/advisories/32602

---

#### 867. CVE-2009-0115

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
The Device Mapper multipathing driver (aka multipath-tools or device-mapper-multipath) 0.4.8, as used in SUSE openSUSE, SUSE Linux Enterprise Server (SLES), Fedora, and possibly other operating systems, uses world-writable permissions for the socket file (aka /var/run/multipathd.sock), which allows local users to send arbitrary commands to the multipath daemon.

**参考链接 / References**:
- http://download.opensuse.org/update/10.3-test/repodata/patch-kpartx-6082.xml
- http://kb.juniper.net/InfoCenter/index?page=content&id=JSA10691
- http://kb.juniper.net/InfoCenter/index?page=content&id=JSA10705
- http://launchpad.net/bugs/cve/2009-0115
- http://lists.opensuse.org/opensuse-security-announce/2009-03/msg00004.html

---

#### 868. CVE-2008-6560

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Buffer overflow in CMAN - The Cluster Manager before 2.03.09-1 on Fedora 9 and Red Hat Enterprise Linux (RHEL) 5 allows attackers to cause a denial of service (CPU consumption and memory corruption) via a cluster.conf file with many lines.  NOTE: it is not clear whether this issue crosses privilege boundaries in realistic uses of the product.

**参考链接 / References**:
- http://git.fedorahosted.org/git/cluster.git?p=cluster.git%3Ba=commitdiff%3Bh=67fee9128e54c6c3fc3eae306b5b501f3029c3be
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00163.html
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00164.html
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00165.html
- http://www.ubuntu.com/usn/USN-875-1

---

#### 869. CVE-2008-6755

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ZoneMinder 1.23.3 on Fedora 10 sets the ownership of /etc/zm.conf to the apache user account, and sets the permissions to 0600, which makes it easier for remote attackers to modify this file by accessing it through a (1) PHP or (2) CGI script.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=476529
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50324
- https://www.redhat.com/archives/fedora-package-announce/2009-January/msg00204.html
- https://bugzilla.redhat.com/show_bug.cgi?id=476529
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50324

---

#### 870. CVE-2009-0153

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
International Components for Unicode (ICU) 4.0, 3.6, and other 3.x versions, as used in Apple Mac OS X 10.5 before 10.5.7, iPhone OS 1.0 through 2.2.1, iPhone OS for iPod touch 1.1 through 2.2.1, Fedora 9 and 10, and possibly other operating systems, does not properly handle invalid byte sequences during Unicode conversion, which might allow remote attackers to conduct cross-site scripting (XSS) attacks.

**参考链接 / References**:
- http://bugs.icu-project.org/trac/ticket/5691
- http://lists.apple.com/archives/security-announce/2009/Jun/msg00005.html
- http://lists.apple.com/archives/security-announce/2009/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2009/jun/msg00002.html
- http://secunia.com/advisories/35074

---

#### 871. CVE-2009-1896

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Java Web Start framework in IcedTea in OpenJDK before 1.6.0.0-20.b16.fc10 on Fedora 10, and before 1.6.0.0-27.b16.fc11 on Fedora 11, trusts an entire application when at least one of the listed jar files is trusted, which allows context-dependent attackers to execute arbitrary code without the untrusted-code restrictions via a crafted application, related to NetX.

**参考链接 / References**:
- http://secunia.com/advisories/36162
- http://www.mandriva.com/security/advisories?name=MDVSA-2009:209
- https://bugzilla.redhat.com/show_bug.cgi?id=512101
- https://www.redhat.com/archives/fedora-package-announce/2009-August/msg00310.html
- https://www.redhat.com/archives/fedora-package-announce/2009-August/msg00325.html

---

#### 872. CVE-2009-2813

**严重程度 / Severity**: N/A | CVSS: 6.0

**漏洞描述 / Description**:
Samba 3.4 before 3.4.2, 3.3 before 3.3.8, 3.2 before 3.2.15, and 3.0.12 through 3.0.36, as used in the SMB subsystem in Apple Mac OS X 10.5.8 when Windows File Sharing is enabled, Fedora 11, and other operating systems, does not properly handle errors in resolving pathnames, which allows remote authenticated users to bypass intended sharing restrictions, and read, create, or modify files, in certain circumstances involving user accounts that lack home directories.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2009/Sep/msg00004.html
- http://lists.opensuse.org/opensuse-security-announce/2009-10/msg00004.html
- http://marc.info/?l=bugtraq&m=126514298313071&w=2
- http://news.samba.org/releases/3.0.37/
- http://news.samba.org/releases/3.2.15/

---

#### 873. CVE-2009-2904

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
A certain Red Hat modification to the ChrootDirectory feature in OpenSSH 4.8, as used in sshd in OpenSSH 4.3 in Red Hat Enterprise Linux (RHEL) 5.4 and Fedora 11, allows local users to gain privileges via hard links to setuid programs that use configuration files within the chroot directory, related to requirements for directory ownership.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2010-March/038214.html
- http://lists.vmware.com/pipermail/security-announce/2010/000082.html
- http://osvdb.org/58495
- http://secunia.com/advisories/38794
- http://secunia.com/advisories/38834

---

#### 874. CVE-2010-1439

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
yum-rhn-plugin in Red Hat Network Client Tools (aka rhn-client-tools) on Red Hat Enterprise Linux (RHEL) 5 and Fedora uses world-readable permissions for the /var/spool/up2date/loginAuth.pkl file, which allows local users to access the Red Hat Network profile, and possibly prevent future security updates, by leveraging authentication data from this file.

**参考链接 / References**:
- http://secunia.com/advisories/39996
- http://securitytracker.com/id?1024049
- http://www.osvdb.org/65063
- http://www.redhat.com/support/errata/RHSA-2010-0449.html
- http://www.securityfocus.com/bid/40492

---

#### 875. CVE-2010-4176

**严重程度 / Severity**: N/A | CVSS: 4.0

**漏洞描述 / Description**:
plymouth-pretrigger.sh in dracut and udev, when running on Fedora 13 and 14, sets weak permissions for the /dev/systty device file, which allows remote authenticated users to read terminal data from tty0 for local users.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2010-December/051755.html
- http://lists.fedoraproject.org/pipermail/package-announce/2010-November/051418.html
- http://secunia.com/advisories/42342
- http://secunia.com/advisories/42451
- http://www.securityfocus.com/bid/45046

---

#### 876. CVE-2010-4695

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A certain Fedora patch for gif2png.c in gif2png 2.5.1 and 2.5.2, as distributed in gif2png-2.5.1-1200.fc12 on Fedora 12 and gif2png_2.5.2-1 on Debian GNU/Linux, truncates a GIF pathname specified on the command line, which might allow remote attackers to create PNG files in unintended directories via a crafted command-line argument, as demonstrated by a CGI program that launches gif2png, a different vulnerability than CVE-2009-5018.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=550978
- http://cvs.fedoraproject.org/viewvc/rpms/gif2png/devel/gif2png-overflow.patch?root=extras&r1=1.1&r2=1.2
- http://cvs.fedoraproject.org/viewvc/rpms/gif2png/devel/gif2png-overflow.patch?root=extras&view=log
- http://lists.fedoraproject.org/pipermail/package-announce/2010-November/051229.html
- http://security.gentoo.org/glsa/glsa-201203-15.xml

---

#### 877. CVE-2011-0008

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
A certain Fedora patch for parse.c in sudo before 1.7.4p5-1.fc14 on Fedora 14 does not properly interpret a system group (aka %group) in the sudoers file during authorization decisions for a user who belongs to that group, which allows local users to leverage an applicable sudoers file and gain root privileges via a sudo command.  NOTE: this vulnerability exists because of a CVE-2009-0034 regression.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2011-January/053263.html
- http://lists.fedoraproject.org/pipermail/package-announce/2011-January/053341.html
- http://secunia.com/advisories/42968
- http://www.mandriva.com/security/advisories?name=MDVSA-2011:018
- http://www.vupen.com/english/advisories/2011/0195

---

#### 878. CVE-2011-1011

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The seunshare_mount function in sandbox/seunshare.c in seunshare in certain Red Hat packages of policycoreutils 2.0.83 and earlier in Red Hat Enterprise Linux (RHEL) 6 and earlier, and Fedora 14 and earlier, mounts a new directory on top of /tmp without assigning root ownership and the sticky bit to this new directory, which allows local users to replace or delete arbitrary /tmp files, and consequently cause a denial of service or possibly gain privileges, by running a setuid application that relies on /tmp, as demonstrated by the ksu application.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2011-02/0585.html
- http://lists.fedoraproject.org/pipermail/package-announce/2011-March/056227.html
- http://openwall.com/lists/oss-security/2011/02/23/1
- http://openwall.com/lists/oss-security/2011/02/23/2
- http://pkgs.fedoraproject.org/gitweb/?p=policycoreutils.git%3Ba=blob%3Bf=policycoreutils-rhat.patch%3Bh=d4db5bc06027de23d12a4b3f18fa6f9b1517df27%3Bhb=HEAD#l2197

---

#### 879. CVE-2011-1943

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The destroy_one_secret function in nm-setting-vpn.c in libnm-util in the NetworkManager package 0.8.999-3.git20110526 in Fedora 15 creates a log entry containing a certificate password, which allows local users to obtain sensitive information by reading a log file.

**参考链接 / References**:
- http://cgit.freedesktop.org/NetworkManager/NetworkManager/commit/?id=78ce088843d59d4494965bfc40b30a2e63d065f6
- http://lists.fedoraproject.org/pipermail/package-announce/2011-June/061329.html
- http://www.openwall.com/lists/oss-security/2011/05/31/6
- http://www.openwall.com/lists/oss-security/2011/05/31/7
- https://bugzilla.redhat.com/show_bug.cgi?id=708876

---

#### 880. CVE-2011-4339

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
ipmievd (aka the IPMI event daemon) in OpenIPMI, as used in the ipmitool package 1.8.11 in Red Hat Enterprise Linux (RHEL) 6, Debian GNU/Linux, Fedora 16, and other products uses 0666 permissions for its ipmievd.pid PID file, which allows local users to kill arbitrary processes by writing to this file.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-January/071575.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-January/071580.html
- http://openwall.com/lists/oss-security/2011/12/13/1
- http://rhn.redhat.com/errata/RHSA-2013-0123.html
- http://secunia.com/advisories/47173

---

#### 881. CVE-2012-2653

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
arpwatch 2.1a15, as used by Red Hat, Debian, Fedora, and possibly others, does not properly drop supplementary groups, which might allow attackers to gain root privileges by leveraging other vulnerabilities in the daemon.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082553.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082565.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082569.html
- http://www.debian.org/security/2012/dsa-2481
- http://www.mandriva.com/security/advisories?name=MDVSA-2012:113

---

#### 882. CVE-2012-4453

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
dracut.sh in dracut, as used in Red Hat Enterprise Linux 6, Fedora 16 and 17, and possibly other products, creates initramfs images with world-readable permissions, which might allow local users to obtain sensitive information.

**参考链接 / References**:
- http://git.kernel.org/?p=boot/dracut/dracut.git%3Ba=commit%3Bh=e1b48995c26c4f06d1a71
- http://rhn.redhat.com/errata/RHSA-2013-1674.html
- http://www.openwall.com/lists/oss-security/2012/09/27/3
- http://www.openwall.com/lists/oss-security/2012/09/27/4
- http://www.openwall.com/lists/oss-security/2012/09/27/6

---

#### 883. CVE-2012-3354

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
doku.php in DokuWiki, as used in Fedora 16, 17, and 18, when certain PHP error levels are set, allows remote attackers to obtain sensitive information via the prefix parameter, which reveals the installation path in an error message.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090755.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090899.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090938.html
- http://www.freelists.org/post/dokuwiki/Fwd-DokuWiki-Full-path-disclosure
- http://www.mandriva.com/security/advisories?name=MDVSA-2013:073

---

#### 884. CVE-1999-0363

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
SuSE 5.2 PLP lpc program has a buffer overflow that leads to root compromise.

**参考链接 / References**:
- http://www.securityfocus.com/bid/328
- http://www.securityfocus.com/bid/328

---

#### 885. CVE-2000-0355

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
pg and pb in SuSE pbpg 1.x package allows an attacker to read arbitrary files.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_21.html
- http://www.novell.com/linux/security/advisories/suse_security_announce_21.html

---

#### 886. CVE-2000-0433

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The SuSE aaa_base package installs some system accounts with home directories set to /tmp, which allows local users to gain privileges to those accounts by creating standard user startup scripts such as profiles.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/suse_security_announce_47.html
- http://www.novell.com/linux/security/advisories/suse_security_announce_47.html

---

#### 887. CVE-2000-1016

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Apache (httpd.conf) on SuSE 6.4 includes an alias for the /usr/doc directory, which allows remote attackers to read package documentation and obtain system configuration information via an HTTP request for the /doc/packages URL.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/84360
- http://www.securityfocus.com/bid/1707
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5276
- http://www.securityfocus.com/archive/1/84360
- http://www.securityfocus.com/bid/1707

---

#### 888. CVE-2001-0109

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
rctab in SuSE 7.0 and earlier allows local users to create or overwrite arbitrary files via a symlink attack on the rctmp temporary file.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0226.html
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0272.html
- http://www.securityfocus.com/bid/2207
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5945
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0226.html

---

#### 889. CVE-2001-0918

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Vulnerabilities in CGI scripts in susehelp in SuSE 7.2 and 7.3 allow remote attackers to execute arbitrary commands by not opening files securely.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2001_041_susehelp_txt.html
- http://www.securityfocus.com/bid/3576
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7583
- http://www.novell.com/linux/security/advisories/2001_041_susehelp_txt.html
- http://www.securityfocus.com/bid/3576

---

#### 890. CVE-2002-0758

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ifup-dhcp script in the sysconfig package for SuSE 8.0 allows remote attackers to execute arbitrary commands via spoofed DHCP responses, which are stored and executed in a file.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9040.php
- http://www.novell.com/linux/security/advisories/2002_016_sysconfig_txt.html
- http://www.securityfocus.com/bid/4695
- http://www.iss.net/security_center/static/9040.php
- http://www.novell.com/linux/security/advisories/2002_016_sysconfig_txt.html

---

#### 891. CVE-2002-0762

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
shadow package in SuSE 8.0 allows local users to destroy the /etc/passwd and /etc/shadow files or assign extra group privileges to some users by changing filesize limits before calling programs that modify the files.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9102.php
- http://www.novell.com/linux/security/advisories/2002_17_shadow.html
- http://www.securityfocus.com/bid/4757
- http://www.iss.net/security_center/static/9102.php
- http://www.novell.com/linux/security/advisories/2002_17_shadow.html

---

#### 892. CVE-2002-0768

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in lukemftp FTP client in SuSE 6.4 through 8.0, and possibly other operating systems, allows a malicious FTP server to execute arbitrary code via a long PASV command.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9130.php
- http://www.novell.com/linux/security/advisories/2002_18_lukemftp.html
- http://www.iss.net/security_center/static/9130.php
- http://www.novell.com/linux/security/advisories/2002_18_lukemftp.html

---

#### 893. CVE-2002-0854

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflows in ISDN Point to Point Protocol (PPP) daemon (ipppd) in the i4l package on SuSE 7.3, 8.0, and possibly other operating systems, may allow local users to gain privileges.

**参考链接 / References**:
- https://lists.opensuse.org/opensuse-security-announce/2002-08/msg00006.html
- https://lists.opensuse.org/opensuse-security-announce/2002-08/msg00006.html

---

#### 894. CVE-2003-0144

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the lprm command in the lprold lpr package on SuSE 7.1 through 7.3, OpenBSD 3.2 and earlier, and possibly other operating systems, allows local users to gain root privileges via long command line arguments such as (1) request ID or (2) user name.

**参考链接 / References**:
- ftp://ftp.openbsd.org/pub/OpenBSD/patches/3.2/common/010_lprm.patch
- ftp://patches.sgi.com/support/free/security/advisories/20030406-02-P
- http://marc.info/?l=bugtraq&m=104690434504429&w=2
- http://marc.info/?l=bugtraq&m=104714441925019&w=2
- http://secunia.com/advisories/8293

---

#### 895. CVE-2003-0846

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
SuSEconfig.javarunt in the javarunt package on SuSE Linux 7.3Pro allows local users to overwrite arbitrary files via a symlink attack on the .java_wrapper temporary file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=106546177518140&w=2
- http://marc.info/?l=bugtraq&m=106546531922379&w=2
- http://marc.info/?l=bugtraq&m=106546177518140&w=2
- http://marc.info/?l=bugtraq&m=106546531922379&w=2

---

#### 896. CVE-2003-0847

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
SuSEconfig.susewm in the susewm package on SuSE Linux 8.2Pro allows local users to overwrite arbitrary files via a symlink attack on the susewm.$$ temporary file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=106545972615578&w=2
- http://marc.info/?l=bugtraq&m=106546531922379&w=2
- http://marc.info/?l=bugtraq&m=106545972615578&w=2
- http://marc.info/?l=bugtraq&m=106546531922379&w=2

---

#### 897. CVE-2003-1399

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
eject 2.0.10, when installed setuid on systems such as SuSE Linux 7.3, generates different error messages depending on whether a specified file exists or not, which allows local users to obtain sensitive information.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2003-02/0278.html
- http://www.securityfocus.com/bid/6914
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11380
- http://archives.neohapsis.com/archives/bugtraq/2003-02/0278.html
- http://www.securityfocus.com/bid/6914

---

#### 898. CVE-2003-1538

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
susehelp in SuSE Linux 8.1, Enterprise Server 8, Office Server, and Openexchange Server 4 does not properly filter shell metacharacters, which allows remote attackers to execute arbitrary commands via CGI queries.

**参考链接 / References**:
- http://secunia.com/advisories/7906
- http://www.novell.com/linux/security/advisories/2003_005_susehelp.html
- http://www.securitytracker.com/id?1005954
- http://secunia.com/advisories/7906
- http://www.novell.com/linux/security/advisories/2003_005_susehelp.html

---

#### 899. CVE-2004-2133

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Certain third-party packages for CVSup 16.1h, such as SuSE Linux, contain untrusted paths in the ELF RPATH fields of certain executables, which could allow local users to execute arbitrary code by causing cvsup to link against malicious libraries that are created in world-writable directories such as /usr/src/packages.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0025.html
- http://marc.info/?l=bugtraq&m=107539776002450&w=2
- http://www.securityfocus.com/bid/9523
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14994
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0025.html

---

#### 900. CVE-2004-0064

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The SuSEconfig.gnome-filesystem script for YaST in SuSE 9.0 allows local users to overwrite arbitrary files via a symlink attack on files within the tmp.SuSEconfig.gnome-filesystem.$RANDOM temporary directory.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=107402658600437&w=2
- http://secunia.com/advisories/10623
- http://www.osvdb.org/3460
- http://www.securityfocus.com/bid/9411
- http://www.securitytracker.com/id?1008703

---

#### 901. CVE-2004-2004

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Live CD in SUSE LINUX 9.1 Personal edition is configured without a password for root, which allows remote attackers to gain privileges via SSH.

**参考链接 / References**:
- http://www.securityfocus.com/bid/10297
- http://www.suse.de/de/security/2004_11_live_cd_91.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16084
- http://www.securityfocus.com/bid/10297
- http://www.suse.de/de/security/2004_11_live_cd_91.html

---

#### 902. CVE-2004-0592

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The tcp_find_option function of the netfilter subsystem for IPv6 in the SUSE Linux 2.6.5 kernel with USAGI patches, when using iptables and TCP options rules, allows remote attackers to cause a denial of service (CPU consumption by infinite loop) via a large option length that produces a negative integer after a casting operation to the char type, a similar flaw to CVE-2004-0626.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-July/023408.html
- http://www.novell.com/linux/security/advisories/2004_20_kernel.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43137
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-July/023408.html
- http://www.novell.com/linux/security/advisories/2004_20_kernel.html

---

#### 903. CVE-2004-1895

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
YaST Online Update (YOU) in SuSE 8.2 and 9.0 allows local users to overwrite arbitrary files via a symlink attack on you-$USER/cookies.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2004-04/0058.html
- http://marc.info/?l=bugtraq&m=108118395519164&w=2
- http://secunia.com/advisories/11300
- http://securitytracker.com/id?1009668
- http://www.osvdb.org/4985

---

#### 904. CVE-2004-2097

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Multiple scripts on SuSE Linux 9.0 allow local users to overwrite arbitrary files via a symlink attack on (1) /tmp/fvwm-bug created by fvwm-bug, (2) /tmp/wmmenu created by wm-oldmenu2new, (3) /tmp/rates created by x11perfcomp, (4) /tmp/xf86debug.1.log created by xf86debug, (5) /tmp/.winpopup-new created by winpopup-send.sh, or (6) /tmp/initrd created by lvmcreate_initrd.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=107461582413923&w=2
- http://marc.info/?l=bugtraq&m=107478920006258&w=2
- http://securitytracker.com/id?1008781
- http://www.securityfocus.com/bid/9457
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14963

---

#### 905. CVE-2004-2658

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
resmgr in SUSE CORE 9 does not properly identify terminal names, which allows local users to spoof terminals and login types.

**参考链接 / References**:
- http://support.novell.com/techcenter/psdb/fa6c6a3e792bf79b1d85821c689ea578.html
- http://support.novell.com/techcenter/psdb/fa6c6a3e792bf79b1d85821c689ea578.html

---

#### 906. CVE-2004-1190

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
SUSE Linux before 9.1 and SUSE Linux Enterprise Server before 9 do not properly check commands sent to CD devices that have been opened read-only, which could allow local users to conduct unauthorized write activities to modify the firmware of associated SCSI devices.

**参考链接 / References**:
- http://secunia.com/advisories/18510
- http://www.novell.com/linux/security/advisories/2004_42_kernel.html
- http://www.redhat.com/support/errata/RHSA-2006-0101.html
- http://www.securityfocus.com/bid/11784
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18370

---

#### 907. CVE-2004-1191

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
Race condition in SuSE Linux 8.1 through 9.2, when run on SMP systems that have more than 4GB of memory, could allow local users to read unauthorized memory from "foreign memory pages."

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2004_42_kernel.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18137
- http://www.novell.com/linux/security/advisories/2004_42_kernel.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18137

---

#### 908. CVE-2004-0887

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
SUSE Linux Enterprise Server 9 on the S/390 platform does not properly handle a certain privileged instruction, which allows local users to gain root privileges.

**参考链接 / References**:
- http://secunia.com/advisories/19369
- http://www.debian.org/security/2006/dsa-1018
- http://www.novell.com/linux/security/advisories/2004_37_kernel.html
- http://www.securityfocus.com/bid/11489
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17801

---

#### 909. CVE-2005-1831

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
Sudo 1.6.8p7 on SuSE Linux 9.3, and possibly other Linux distributions, allows local users to gain privileges by using sudo to call su, then entering a blank password and hitting CTRL-C. NOTE: SuSE and multiple third-party researchers have not been able to replicate this issue, stating "Sudo catches SIGINT and returns an empty string for the password so I don't see how this could happen unless the user's actual password was empty.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2005-05/0349.html
- http://archives.neohapsis.com/archives/bugtraq/2005-05/0359.html
- http://marc.info/?l=bugtraq&m=111755694008928&w=2
- http://www.osvdb.org/20417
- http://archives.neohapsis.com/archives/bugtraq/2005-05/0349.html

---

#### 910. CVE-2005-0488

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Certain BSD-based Telnet clients, including those used on Solaris and SuSE Linux, allow remote malicious Telnet servers to read sensitive environment variables via the NEW-ENVIRON option with a SEND ENV_USERVAR command.

**参考链接 / References**:
- http://idefense.com/application/poi/display?id=260&type=vulnerabilities
- http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html
- http://secunia.com/advisories/17135
- http://secunia.com/advisories/21253
- http://securitytracker.com/id?1014203

---

#### 911. CVE-2005-2023

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The send_pinentry_environment function in asshelp.c in gpg2 on SUSE Linux 9.3 does not properly handle certain options, which can prevent pinentry from being found and causes S/MIME signing to fail.

**参考链接 / References**:
- http://lists.gnupg.org/pipermail/gpa-dev/2005-June/002291.html
- http://lists.gnupg.org/pipermail/gpa-dev/2005-June/002294.html
- http://www.novell.com/linux/security/advisories/2005_16_sr.html
- https://lists.gnupg.org/pipermail/gpa-dev/2005-May/002284.html
- http://lists.gnupg.org/pipermail/gpa-dev/2005-June/002291.html

---

#### 912. CVE-2005-2500

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the xdr_xcode_array2 function in xdr.c in Linux kernel 2.6.12, as used in SuSE Linux Enterprise Server 9, might allow remote attackers to cause a denial of service and possibly execute arbitrary code via crafted XDR data for the nfsacl protocol.

**参考链接 / References**:
- http://linux.bkbits.net:8080/linux-2.6/cset%4042b9c4fdYUuaq0joRUZi8W0Q-2hA1A
- http://lkml.org/lkml/2005/6/23/126
- http://lkml.org/lkml/2005/6/23/19
- http://secunia.com/advisories/16406
- http://www.novell.com/linux/security/advisories/2005_44_kernel.html

---

#### 913. CVE-2005-3013

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in liby2util in Yet another Setup Tool (YaST) for SuSE Linux 9.3 allows local users to execute arbitrary code via a long Loc entry.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/14861
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24323
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/14861

---

#### 914. CVE-2005-3297

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Multiple integer overflows in OpenWBEM on SuSE Linux 9 allow remote attackers to execute arbitrary code via unknown vectors.

**参考链接 / References**:
- http://secunia.com/advisories/17176
- http://secunia.com/advisories/17244
- http://www.novell.com/linux/security/advisories/2005_60_OpenWBEM.html
- http://www.osvdb.org/20062
- http://www.securityfocus.com/bid/15121

---

#### 915. CVE-2005-3298

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Multiple buffer overflows in OpenWBEM on SuSE Linux 9 allow remote attackers to execute arbitrary code via unknown vectors.

**参考链接 / References**:
- http://secunia.com/advisories/17176
- http://secunia.com/advisories/17244
- http://www.novell.com/linux/security/advisories/2005_60_OpenWBEM.html
- http://www.osvdb.org/20062
- http://www.securityfocus.com/bid/15121

---

#### 916. CVE-2005-3321

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
chkstat in SuSE Linux 9.0 through 10.0 allows local users to modify permissions of files by creating a hardlink to a file from a world-writable directory, which can cause the link count to drop to 1 when the file is deleted or replaced, which is then modified by chkstat to use weaker permissions.

**参考链接 / References**:
- http://secunia.com/advisories/17290/
- http://www.novell.com/linux/security/advisories/2005_62_permissions.html
- http://www.osvdb.org/20263
- http://www.securityfocus.com/bid/15182
- https://exchange.xforce.ibmcloud.com/vulnerabilities/22853

---

#### 917. CVE-2005-3322

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Unspecified vulnerability in Squid on SUSE Linux 9.0 allows remote attackers to cause a denial of service (crash) via HTTPs (SSL).

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2005_24_sr.html
- http://www.novell.com/linux/security/advisories/2005_28_sr.html
- http://www.securityfocus.com/bid/15165
- http://www.novell.com/linux/security/advisories/2005_24_sr.html
- http://www.novell.com/linux/security/advisories/2005_28_sr.html

---

#### 918. CVE-2005-3503

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
chfn in pwdutils 3.0.4 and earlier on SuSE Linux, and possibly other operating systems, does not properly check arguments for the GECOS field, which allows local users to gain privileges.

**参考链接 / References**:
- http://secunia.com/advisories/17469
- http://www.osvdb.org/20525
- http://www.securityfocus.com/archive/1/415725/30/0/threaded
- http://www.securityfocus.com/bid/15314
- http://secunia.com/advisories/17469

---

#### 919. CVE-1999-1165

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
GNU fingerd 1.37 does not properly drop privileges before accessing user information, which could allow local users to (1) gain root privileges via a malicious program in the .fingerrc file, or (2) read arbitrary files via symbolic links from .plan, .forward, or .project files.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93268249021561&w=2
- http://www.securityfocus.com/archive/1/2478
- http://www.securityfocus.com/bid/535
- http://marc.info/?l=bugtraq&m=93268249021561&w=2
- http://www.securityfocus.com/archive/1/2478

---

#### 920. CVE-1999-0719

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Guile plugin for the Gnumeric spreadsheet package allows attackers to execute arbitrary code.

**参考链接 / References**:
- http://www.securityfocus.com/bid/563
- http://www.securityfocus.com/bid/563

---

#### 921. CVE-2000-0151

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
GNU make follows symlinks when it reads a Makefile from stdin, which allows other local users to execute commands.

**参考链接 / References**:
- http://www.securityfocus.com/bid/981
- http://www.securityfocus.com/bid/981

---

#### 922. CVE-2000-0786

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
GNU userv 1.0.0 and earlier does not properly perform file descriptor swapping, which can corrupt the USERV_GROUPS and USERV_GIDS environmental variables and allow local users to bypass some access restrictions.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0389.html
- http://marc.info/?l=bugtraq&m=96473640717095&w=2
- http://www.debian.org/security/2000/20000727
- http://www.securityfocus.com/bid/1516
- http://archives.neohapsis.com/archives/bugtraq/2000-07/0389.html

---

#### 923. CVE-2000-0803

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
GNU Groff uses the current working directory to find a device description file, which allows a local user to gain additional privileges by including a malicious postpro directive in the description file, which is executed when another user runs groff.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5280
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5280

---

#### 924. CVE-2000-0974

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
GnuPG (gpg) 1.0.3 does not properly check all signatures of a file containing multiple documents, which allows an attacker to modify contents of all documents but the first without detection.

**参考链接 / References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:67.gnupg.asc
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-038.0.txt
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0201.html
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0361.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000334

---

#### 925. CVE-2000-1137

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
GNU ed before 0.2-18.1 allows local users to overwrite the files of other users via a symlink attack.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000359
- http://www.debian.org/security/2000/20001129
- http://www.linux-mandrake.com/en/security/MDKSA-2000-076.php3
- http://www.osvdb.org/6491
- http://www.redhat.com/support/errata/RHSA-2000-123.html

---

#### 926. CVE-2001-0071

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
gpg (aka GnuPG) 1.0.4 and other versions does not properly verify detached signatures, which allows attackers to modify the contents of a file without detection.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000368
- http://www.debian.org/security/2000/20001225b
- http://www.linux-mandrake.com/en/updates/2000/MDKSA-2000-087.php3
- http://www.osvdb.org/1699
- http://www.redhat.com/support/errata/RHSA-2000-131.html

---

#### 927. CVE-2001-0072

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
gpg (aka GnuPG) 1.0.4 and other versions imports both public and private keys from public key servers without notifying the user about the private keys, which could allow an attacker to break the web of trust.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000368
- http://www.debian.org/security/2000/20001225b
- http://www.linux-mandrake.com/en/updates/2000/MDKSA-2000-087.php3
- http://www.osvdb.org/1702
- http://www.redhat.com/support/errata/RHSA-2000-131.html

---

#### 928. CVE-2001-0273

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
pgp4pine Pine/PGP interface version 1.75-6 does not properly check to see if a public key has expired when obtaining the keys via Gnu Privacy Guard (GnuPG), which causes the message to be sent in cleartext.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0367.html
- http://www.kb.cert.org/vuls/id/566640
- http://www.securityfocus.com/bid/2405
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6135
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0367.html

---

#### 929. CVE-2001-1267

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Directory traversal vulnerability in GNU tar 1.13.19 and earlier allows local users to overwrite arbitrary files during archive extraction via a tar file whose filenames contain a .. (dot dot).

**参考链接 / References**:
- ftp://alpha.gnu.org/gnu/tar/tar-1.13.25.tar.gz
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000538
- http://online.securityfocus.com/advisories/4514
- http://online.securityfocus.com/archive/1/196445
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-47800-1

---

#### 930. CVE-2001-0522

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Format string vulnerability in Gnu Privacy Guard (aka GnuPG or gpg) 1.05 and earlier can allow an attacker to gain privileges via format strings in the original filename that is stored in an encrypted file.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000399
- http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-023-01
- http://online.securityfocus.com/archive/1/188218
- http://www.calderasystems.com/support/security/advisories/CSSA-2001-020.0.txt
- http://www.debian.org/security/2001/dsa-061

---

#### 931. CVE-2001-1004

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Cross-site scripting (CSS) vulnerability in gnut Gnutella client before 0.4.27 allows remote attackers to execute arbitrary script on other clients by sharing a file whose name contains the script tags.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0415.html
- http://www.gnutelliums.com/linux_unix/gnut/ChangeLog.txt
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0415.html
- http://www.gnutelliums.com/linux_unix/gnut/ChangeLog.txt

---

#### 932. CVE-2001-1036

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
GNU locate in findutils 4.1 on Slackware 7.1 and 8.0 allows local users to gain privileges via an old formatted filename database (locatedb) that contains an entry with an out-of-range offset, which causes locate to write to arbitrary process memory.

**参考链接 / References**:
- http://www.osvdb.org/5477
- http://www.securityfocus.com/archive/1/200991
- http://www.securityfocus.com/bid/3127
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6932
- http://www.osvdb.org/5477

---

#### 933. CVE-2002-0044

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
GNU Enscript 1.6.1 and earlier allows local users to overwrite arbitrary files of the Enscript user via a symlink attack on temporary files.

**参考链接 / References**:
- http://www.debian.org/security/2002/dsa-105
- http://www.linux-mandrake.com/en/security/2002/MDKSA-2002-010.php3
- http://www.redhat.com/support/errata/RHSA-2002-012.html
- http://www.securityfocus.com/advisories/3818
- http://www.securityfocus.com/bid/3920

---

#### 934. CVE-2002-1602

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in the Braille module for GNU screen 3.9.11, when HAVE_BRAILLE is defined, allows local users to execute arbitrary code.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/524227
- http://www.securityfocus.com/archive/1/268998
- http://www.securityfocus.com/bid/4578
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8929
- http://www.kb.cert.org/vuls/id/524227

---

#### 935. CVE-2002-0204

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in GNU Chess (gnuchess) 5.02 and earlier, if modified or used in a networked capacity contrary to its own design as a single-user application, may allow local or remote attackers to execute arbitrary code via a long command.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101189688815514&w=2
- http://www.iss.net/security_center/static/7991.php
- http://www.securityfocus.com/bid/3949
- http://marc.info/?l=bugtraq&m=101189688815514&w=2
- http://www.iss.net/security_center/static/7991.php

---

#### 936. CVE-2002-0271

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
Runtime library in GNU Ada compiler (GNAT) 3.12p through 3.14p allows local users to modify files of other users via a symlink attack on temporary files.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101353440624007&w=2
- http://www.securityfocus.com/bid/4086
- http://marc.info/?l=bugtraq&m=101353440624007&w=2
- http://www.securityfocus.com/bid/4086

---

#### 937. CVE-2002-0300

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
gnujsp 1.0.0 and 1.0.1 allows remote attackers to list directories, read source code of certain scripts, and bypass access restrictions by directly requesting the target file from the gnujsp servlet, which does not work around a limitation of JServ and does not process the requested file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101415804625292&w=2
- http://marc.info/?l=bugtraq&m=101422432123898&w=2
- http://www.debian.org/security/2002/dsa-114
- http://www.iss.net/security_center/static/8240.php
- http://www.securityfocus.com/bid/4125

---

#### 938. CVE-2002-0435

**严重程度 / Severity**: N/A | CVSS: 1.2

**漏洞描述 / Description**:
Race condition in the recursive (1) directory deletion and (2) directory move in GNU File Utilities (fileutils) 4.1 and earlier allows local users to delete directories as the user running fileutils by moving a low-level directory to a higher level as it is being deleted, which causes fileutils to chdir to a ".." directory that is higher than expected, possibly up to the root file system.

**参考链接 / References**:
- ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2002-018.1.txt
- http://mail.gnu.org/archive/html/bug-fileutils/2002-03/msg00028.html
- http://www.iss.net/security_center/static/8432.php
- http://www.linux-mandrake.com/en/security/2002/MDKSA-2002-031.php
- http://www.redhat.com/support/errata/RHSA-2003-015.html

---

#### 939. CVE-2002-0399

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Directory traversal vulnerability in GNU tar 1.13.19 through 1.13.25, and possibly later versions, allows attackers to overwrite arbitrary files during archive extraction via a (1) "/.." or (2) "./.." string, which removes the leading slash but leaves the "..", a variant of CVE-2001-1267.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000538
- http://marc.info/?l=bugtraq&m=103419290219680&w=2
- http://secunia.com/advisories/19130
- http://secunia.com/advisories/26604
- http://secunia.com/advisories/26673

---

#### 940. CVE-2002-0029

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in the DNS stub resolver library in ISC BIND 4.9.2 through 4.9.10, and other derived libraries such as BSD libc and GNU glibc, allow remote attackers to execute arbitrary code via DNS server responses that trigger the overflow in the (1) getnetbyname, or (2) getnetbyaddr functions, aka "LIBRESOLV: buffer overrun" and a different vulnerability than CVE-2002-0684.

**参考链接 / References**:
- ftp://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2002-028.txt.asc
- ftp://patches.sgi.com/support/free/security/advisories/20021201-01-P
- http://lists.apple.com/archives/Security-announce/2002/Nov/msg00000.html
- http://www.cert.org/advisories/CA-2002-31.html
- http://www.isc.org/products/BIND/bind-security.html

---

#### 941. CVE-2002-2099

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in the GNU DataDisplay Debugger (DDD) 3.3.1 allows local users to execute arbitrary code and possibly gain privileges via a long HOME environment variable.  NOTE: since DDD is not installed setuid or setgid, perhaps this issue should not be included in CVE.

**参考链接 / References**:
- http://securitytracker.com/id?1003241
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7979
- http://securitytracker.com/id?1003241
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7979

---

#### 942. CVE-2003-0255

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The key validation code in GnuPG before 1.2.2 does not properly determine the validity of keys with multiple user IDs and assigns the greatest validity of the most valid user ID, which prevents GnuPG from warning the encrypting user when a user ID does not have a trusted path.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000694
- http://marc.info/?l=bugtraq&m=105215110111174&w=2
- http://marc.info/?l=bugtraq&m=105301357425157&w=2
- http://marc.info/?l=bugtraq&m=105311804129104&w=2
- http://marc.info/?l=bugtraq&m=105362224514081&w=2

---

#### 943. CVE-2003-0256

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The GnuPG plugin in kopete before 0.6.2 does not properly cleanse the command line when executing gpg, which allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000665
- http://kopete.kde.org/index.php?page=newsstory&news=Kopete_releases_version_0.6.2
- http://www.mandriva.com/security/advisories?name=MDKSA-2003:055
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000665
- http://kopete.kde.org/index.php?page=newsstory&news=Kopete_releases_version_0.6.2

---

#### 944. CVE-1999-1214

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The asynchronous I/O facility in 4.4 BSD kernel does not check user credentials when setting the recipient of I/O notification, which allows local users to cause a denial of service by using certain ioctl and fcntl calls to cause the signal to be sent to an arbitrary process ID.

**参考链接 / References**:
- http://www.openbsd.com/advisories/signals.txt
- http://www.openbsd.com/advisories/signals.txt
- http://www.osvdb.org/11062
- https://exchange.xforce.ibmcloud.com/vulnerabilities/556
- http://www.openbsd.com/advisories/signals.txt

---

#### 945. CVE-1999-0295

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Solaris sysdef command allows local users to read kernel memory, potentially leading to root privileges.

**参考链接 / References**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/157
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/157

---

#### 946. CVE-1999-0367

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
NetBSD netstat command allows local users to access kernel memory.

**参考链接 / References**:
- http://www.osvdb.org/7571
- http://www.osvdb.org/7571

---

#### 947. CVE-1999-0482

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
OpenBSD kernel crash through TSS handling, as caused by the crashme program.

**参考链接 / References**:
- http://www.osvdb.org/7557
- http://www.osvdb.org/7557

---

#### 948. CVE-1999-0727

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A kernel leak in the OpenBSD kernel allows IPsec packets to be sent unencrypted.

**参考链接 / References**:
- http://www.osvdb.org/6127
- http://www.osvdb.org/6127

---

#### 949. CVE-2000-0182

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
iPlanet Web Server 4.1 allows remote attackers to cause a denial of service via a large number of GET commands, which consumes memory and causes a kernel panic.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0182
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0182

---

#### 950. CVE-2000-0456

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
NetBSD 1.4.2 and earlier allows local users to cause a denial of service by repeatedly running certain system calls in the kernel which do not yield the CPU, aka "cpu-hog".

**参考链接 / References**:
- ftp://ftp.netbsd.org/pub/NetBSD/misc/security/advisories/NetBSD-SA2000-005.txt.asc
- http://www.osvdb.org/1365
- http://www.securityfocus.com/bid/1272
- ftp://ftp.netbsd.org/pub/NetBSD/misc/security/advisories/NetBSD-SA2000-005.txt.asc
- http://www.osvdb.org/1365

---

#### 951. CVE-2000-1141

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Recourse ManTrap 1.6 modifies the kernel so that ".." does not appear in the /proc listing, which allows attackers to determine that they are in a honeypot system.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0041.html
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0100.html
- http://marc.info/?l=bugtraq&m=97349791405580&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5473
- http://archives.neohapsis.com/archives/bugtraq/2000-11/0041.html

---

#### 952. CVE-2001-0062

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
procfs in FreeBSD and possibly other operating systems allows local users to cause a denial of service by calling mmap on the process' own mem file, which causes the kernel to hang.

**参考链接 / References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:77.procfs.v1.1.asc
- http://www.osvdb.org/1698
- http://www.osvdb.org/6082
- http://www.securityfocus.com/bid/2131
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6107

---

#### 953. CVE-2000-0375

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The kernel in FreeBSD 3.2 follows symbolic links when it creates core dump files, which allows local attackers to modify arbitrary files.

**参考链接 / References**:
- http://www.osvdb.org/6084
- http://www.osvdb.org/6084

---

#### 954. CVE-2001-0122

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Kernel leak in AfpaCache module of the Fast Response Cache Accelerator (FRCA) component of IBM HTTP Server 1.3.x and Websphere 3.52 allows remote attackers to cause a denial of service via a series of malformed HTTP requests that generate a "bad request" error.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0079.html
- http://archives.neohapsis.com/archives/bugtraq/2001-03/0061.html
- http://www-4.ibm.com/software/webservers/security.html
- http://www.securityfocus.com/bid/2175
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5900

---

#### 955. CVE-2001-0268

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The i386_set_ldt system call in NetBSD 1.5 and earlier, and OpenBSD 2.8 and earlier, when the USER_LDT kernel option is enabled, does not validate a call gate target, which allows local users to gain root privileges by creating a segment call gate in the Local Descriptor Table (LDT) with a target that specifies an arbitrary kernel address.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0353.html
- http://archives.neohapsis.com/archives/linux/caldera/2001-q4/0014.html
- http://archives.neohapsis.com/archives/netbsd/2001-q1/0093.html
- http://www.kb.cert.org/vuls/id/358960
- http://www.openbsd.org/errata.html#userldt

---

#### 956. CVE-2001-0482

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Configuration error in Argus PitBull LX allows root users to bypass specified access control restrictions and cause a denial of service or execute arbitrary commands by modifying kernel variables such as MaxFiles, MaxInodes, and ModProbePath in /proc/sys via calls to sysctl.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-03/0475.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6623
- http://archives.neohapsis.com/archives/bugtraq/2001-03/0475.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6623

---

#### 957. CVE-2001-1181

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Dynamically Loadable Kernel Module (dlkm) static kernel symbol table in HP-UX 11.11 is not properly configured, which allows local users to gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/hp/2001-q3/0013.html
- http://ciac.llnl.gov/ciac/bulletins/l-115.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6861
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5479
- http://archives.neohapsis.com/archives/hp/2001-q3/0013.html

---

#### 958. CVE-2001-0592

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Watchguard Firebox II prior to 4.6 allows a remote attacker to create a denial of service in the kernel via a large stream (>10,000) of malformed ICMP or TCP packets.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0054.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6327
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0054.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6327

---

#### 959. CVE-2001-1133

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Vulnerability in a system call in BSDI 3.0 and 3.1 allows local users to cause a denial of service (reboot) in the kernel via a particular sequence of instructions.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7023.php
- http://www.securityfocus.com/archive/1/209192
- http://www.securityfocus.com/bid/3220
- http://www.iss.net/security_center/static/7023.php
- http://www.securityfocus.com/archive/1/209192

---

#### 960. CVE-2001-1166

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
linprocfs on FreeBSD 4.3 and earlier does not properly restrict access to kernel memory, which allows one process with debugging rights on a privileged process to read restricted memory from that process.

**参考链接 / References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:55.procfs.asc
- http://www.iss.net/security_center/static/7017.php
- http://www.osvdb.org/1938
- http://www.securityfocus.com/bid/3217
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:55.procfs.asc

---

#### 961. CVE-2001-0734

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Hitachi Super-H architecture in NetBSD 1.5 and 1.4.1 allows a local user to gain privileges via modified Status Register contents, which are not properly handled by (1) the sigreturn system call or (2) the process_write_regs kernel routine.

**参考链接 / References**:
- ftp://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2001-008.txt.asc
- http://www.securityfocus.com/bid/2810
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6637
- ftp://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2001-008.txt.asc
- http://www.securityfocus.com/bid/2810

---

#### 962. CVE-2012-2251

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
rssh 2.3.2, as used by Debian, Fedora, and others, when the rsync protocol is enabled, allows local users to bypass intended restricted shell access via a (1) "-e" or (2) "--" command line option.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2012-11/0101.html
- http://secunia.com/advisories/51307
- http://www.debian.org/security/2012/dsa-2578
- http://www.openwall.com/lists/oss-security/2012/11/27/15
- http://www.securityfocus.com/bid/56708

---

#### 963. CVE-2012-5536

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
A certain Red Hat build of the pam_ssh_agent_auth module on Red Hat Enterprise Linux (RHEL) 6 and Fedora Rawhide calls the glibc error function instead of the error function in the OpenSSH codebase, which allows local users to obtain sensitive information from process memory or possibly gain privileges via crafted use of an application that relies on this module, as demonstrated by su and sudo.

**参考链接 / References**:
- http://pkgs.fedoraproject.org/cgit/openssh.git/commit/?id=4f4687ce8045418f678c323bb22c837f35d7b9fa
- http://rhn.redhat.com/errata/RHSA-2013-0519.html
- https://bugzilla.redhat.com/show_bug.cgi?id=834618
- http://pkgs.fedoraproject.org/cgit/openssh.git/commit/?id=4f4687ce8045418f678c323bb22c837f35d7b9fa
- http://rhn.redhat.com/errata/RHSA-2013-0519.html

---

#### 964. CVE-2012-1568

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The ExecShield feature in a certain Red Hat patch for the Linux kernel in Red Hat Enterprise Linux (RHEL) 5 and 6 and Fedora 15 and 16 does not properly handle use of many shared libraries by a 32-bit executable file, which makes it easier for context-dependent attackers to bypass the ASLR protection mechanism by leveraging a predictable base address for one of these libraries.

**参考链接 / References**:
- http://openwall.com/lists/oss-security/2012/03/21/3
- http://scarybeastsecurity.blogspot.com/2012/03/some-random-observations-on-linux-aslr.html
- http://www.openwall.com/lists/oss-security/2012/03/20/4
- https://bugzilla.redhat.com/show_bug.cgi?id=804947
- https://oss.oracle.com/git/?p=redpatch.git%3Ba=commit%3Bh=302a4fc15aebf202b6dffd6c804377c6058ee6e4

---

#### 965. CVE-2013-2030

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
keystone/middleware/auth_token.py in OpenStack Nova Folsom, Grizzly, and Havana uses an insecure temporary directory for storing signing certificates, which allows local users to spoof servers by pre-creating this directory, which is reused by Nova, as demonstrated using /tmp/keystone-signing-nova on Fedora.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2013-May/105916.html
- http://lists.openstack.org/pipermail/openstack-announce/2013-May/000098.html
- http://www.openwall.com/lists/oss-security/2013/05/09/2
- https://bugs.launchpad.net/nova/+bug/1174608
- https://bugzilla.redhat.com/show_bug.cgi?id=958285

---

#### 966. CVE-2013-7283

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Race condition in the libreswan.spec files for Red Hat Enterprise Linux (RHEL) and Fedora packages in libreswan 3.6 has unspecified impact and attack vectors, involving the /var/tmp/libreswan-nss-pwd temporary file.

**参考链接 / References**:
- http://secunia.com/advisories/56276
- http://www.osvdb.org/101575
- https://github.com/libreswan/libreswan/commit/ef2d756e73a188401c36133c2e2f7ce4f3c6ae55
- https://lists.libreswan.org/pipermail/swan-announce/2013/000007.html
- http://secunia.com/advisories/56276

---

#### 967. CVE-2010-0746

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Directory traversal vulnerability in DeviceKit-disks in DeviceKit, as used in Fedora 11 and 12 and possibly other operating systems, allows local users to gain privileges via .. (dot dot) sequences in the label for a pluggable storage device.

**参考链接 / References**:
- http://seclists.org/oss-sec/2010/q2/5
- http://stealth.openwall.net/xSports/devshit.pl
- http://xorl.wordpress.com/2010/04/06/cve-2010-0746-devicekit-local-privilege-escalation/
- https://bugs.freedesktop.org/show_bug.cgi?id=23235
- https://bugzilla.redhat.com/show_bug.cgi?id=523178

---

#### 968. CVE-2014-2094

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in Catfish through 0.4.0.3, when a Fedora package such as 0.4.0.2-2 is not used, allows local users to gain privileges via a Trojan horse catfish.pyc in the current working directory.

**参考链接 / References**:
- http://openwall.com/lists/oss-security/2014/02/25/2
- http://openwall.com/lists/oss-security/2014/02/25/4
- https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=739958
- https://bugzilla.redhat.com/show_bug.cgi?id=1069396
- http://openwall.com/lists/oss-security/2014/02/25/2

---

#### 969. CVE-2014-2095

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in Catfish 0.6.0 through 1.0.0, when a Fedora package such as 0.8.2-1 is not used, allows local users to gain privileges via a Trojan horse bin/catfish.pyc under the current working directory.

**参考链接 / References**:
- http://openwall.com/lists/oss-security/2014/02/25/2
- http://openwall.com/lists/oss-security/2014/02/25/4
- https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=739958
- https://bugzilla.redhat.com/show_bug.cgi?id=1069396
- http://openwall.com/lists/oss-security/2014/02/25/2

---

#### 970. CVE-2013-6494

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
fedup 0.9.0 in Fedora 19, 20, and 21 uses a temporary directory with a static name for its download cache, which allows local users to cause a denial of service (prevention of system updates).

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2014-November/141698.html
- http://lists.fedoraproject.org/pipermail/package-announce/2014-November/142698.html
- http://lists.fedoraproject.org/pipermail/package-announce/2014-November/142933.html
- http://www.securityfocus.com/bid/70874
- https://bugzilla.redhat.com/show_bug.cgi?id=1066679

---

#### 971. CVE-2014-9278

**严重程度 / Severity**: N/A | CVSS: 4.0

**漏洞描述 / Description**:
The OpenSSH server, as used in Fedora and Red Hat Enterprise Linux 7 and when running in a Kerberos environment, allows remote authenticated users to log in as another user when they are listed in the .k5users file of that user, which might bypass intended authentication requirements that would force a local login.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2015-0425.html
- http://thread.gmane.org/gmane.comp.encryption.kerberos.general/15855
- http://www.openwall.com/lists/oss-security/2014/12/02/3
- http://www.openwall.com/lists/oss-security/2014/12/04/17
- http://www.securityfocus.com/bid/71420

---

#### 972. CVE-2015-3230

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
389 Directory Server (formerly Fedora Directory Server) before 1.3.3.12 does not enforce the nsSSL3Ciphers preference when creating an sslSocket, which allows remote attackers to have unspecified impact by requesting to use a disabled cipher.

**参考链接 / References**:
- http://directory.fedoraproject.org/docs/389ds/releases/release-1-3-3-12.html
- http://lists.fedoraproject.org/pipermail/package-announce/2015-October/168985.html
- https://bugzilla.redhat.com/show_bug.cgi?id=1230996
- https://fedorahosted.org/389/ticket/48194
- http://directory.fedoraproject.org/docs/389ds/releases/release-1-3-3-12.html

---

#### 973. CVE-2016-0741

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
slapd/connection.c in 389 Directory Server (formerly Fedora Directory Server) 1.3.4.x before 1.3.4.7 allows remote attackers to cause a denial of service (infinite loop and connection blocking) by leveraging an abnormally closed connection.

**参考链接 / References**:
- http://directory.fedoraproject.org/docs/389ds/releases/release-1-3-4-7.html
- http://rhn.redhat.com/errata/RHSA-2016-0204.html
- http://www.oracle.com/technetwork/topics/security/linuxbulletinjan2016-2867209.html
- http://www.securityfocus.com/bid/82343
- https://fedorahosted.org/389/changeset/cd45d032421b0ecf76d8cbb9b1c3aeef7680d9a2/

---

#### 974. CVE-2016-0726

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The Fedora Nagios package uses "nagiosadmin" as the default password for the "nagiosadmin" administrator account, which makes it easier for remote attackers to obtain access by leveraging knowledge of the credentials.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1295446
- https://bugzilla.redhat.com/show_bug.cgi?id=1295446

---

#### 975. CVE-2017-7496

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
fedora-arm-installer up to and including 1.99.16 is vulnerable to local privilege escalation due to lack of checking the error condition of mount operation failure on unsafely created temporary directories.

**参考链接 / References**:
- https://pagure.io/arm-image-installer/pull-request/10
- https://pagure.io/arm-image-installer/pull-request/10

---

#### 976. CVE-2015-3277

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
The mod_nss module before 1.0.11 in Fedora allows remote attackers to obtain cipher lists due to incorrect parsing of multi-keyword cipherstring.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2015-November/170607.html
- https://bugzilla.redhat.com/show_bug.cgi?id=1238324
- https://bugzilla.redhat.com/show_bug.cgi?id=1243518
- http://lists.fedoraproject.org/pipermail/package-announce/2015-November/170607.html
- https://bugzilla.redhat.com/show_bug.cgi?id=1238324

---

#### 977. CVE-2017-12170

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Downstream version 1.0.46-1 of pure-ftpd as shipped in Fedora was vulnerable to packaging error due to which the original configuration was ignored after update and service started running with default configuration. This has security implications because of overriding security-related configuration. This issue doesn't affect upstream version of pure-ftpd.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1493114
- https://bugzilla.redhat.com/show_bug.cgi?id=1493114

---

#### 978. CVE-2015-0296

**严重程度 / Severity**: MEDIUM | CVSS: 4.7

**漏洞描述 / Description**:
The pre-install script in texlive 3.1.20140525_r34255.fc21 as packaged in Fedora 21 and rpm, and texlive 6.20131226_r32488.fc20 and rpm allows local users to delete arbitrary files via a crafted file in the user's home directory.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2015-April/154198.html
- http://lists.fedoraproject.org/pipermail/package-announce/2015-April/154424.html
- http://www.openwall.com/lists/oss-security/2015/02/27/6
- http://www.securityfocus.com/bid/72826
- https://bugzilla.redhat.com/show_bug.cgi?id=1197082

---

#### 979. CVE-2015-3229

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
fedora-cloud-atomic.ks in spin-kickstarts allows remote attackers to conduct man-in-the-middle attacks by leveraging use of HTTP to download Fedora Atomic updates.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/06/12/8
- http://www.securityfocus.com/bid/75185
- https://bugzilla.redhat.com/show_bug.cgi?id=1231800
- https://lists.fedoraproject.org/archives/list/spins%40lists.fedoraproject.org/thread/L3GSGM5JS2EAJJAGEHR7U4ATNM4ILFKK/
- http://www.openwall.com/lists/oss-security/2015/06/12/8

---

#### 980. CVE-2013-0159

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
The fedora-business-cards package before 1-0.1.beta1.fc17 on Fedora 17 and before 1-0.1.beta1.fc18 on Fedora 18 allows local users to cause a denial of service or write to arbitrary files via a symlink attack on /tmp/fedora-business-cards-buffer.svg.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=892299
- https://bugzilla.redhat.com/show_bug.cgi?id=892815
- https://bugzilla.redhat.com/show_bug.cgi?id=892299
- https://bugzilla.redhat.com/show_bug.cgi?id=892815

---

#### 981. CVE-2018-1111

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
DHCP packages in Red Hat Enterprise Linux 6 and 7, Fedora 28, and earlier are vulnerable to a command injection flaw in the NetworkManager integration script included in the DHCP client. A malicious DHCP server, or an attacker on the local network able to spoof DHCP responses, could use this flaw to execute arbitrary commands with root privileges on systems using NetworkManager and configured to obtain network configuration using the DHCP protocol.

**参考链接 / References**:
- http://www.securityfocus.com/bid/104195
- http://www.securitytracker.com/id/1040912
- https://access.redhat.com/errata/RHSA-2018:1453
- https://access.redhat.com/errata/RHSA-2018:1454
- https://access.redhat.com/errata/RHSA-2018:1455

---

#### 982. CVE-2018-1125

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
procps-ng before version 3.3.15 is vulnerable to a stack buffer overflow in pgrep. This vulnerability is mitigated by FORTIFY, as it involves strncat() to a stack-allocated string. When pgrep is compiled with FORTIFY (as on Red Hat Enterprise Linux and Fedora), the impact is limited to a crash.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2019-10/msg00058.html
- http://lists.opensuse.org/opensuse-security-announce/2019-10/msg00059.html
- http://seclists.org/oss-sec/2018/q2/122
- http://www.securityfocus.com/bid/104214
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2018-1125

---

#### 983. CVE-2018-1113

**严重程度 / Severity**: MEDIUM | CVSS: 4.8

**漏洞描述 / Description**:
setup before version 2.11.4-1.fc28 in Fedora and Red Hat Enterprise Linux added /sbin/nologin and /usr/sbin/nologin to /etc/shells. This violates security assumptions made by pam_shells and some daemons which allow access based on a user's shell being listed in /etc/shells. Under some circumstances, users which had their shell changed to /sbin/nologin could still access the system.

**参考链接 / References**:
- https://access.redhat.com/errata/RHBA-2019:0327
- https://access.redhat.com/errata/RHSA-2018:3249
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2018-1113
- https://access.redhat.com/errata/RHBA-2019:0327
- https://access.redhat.com/errata/RHSA-2018:3249

---

#### 984. CVE-2019-7639

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
An issue was discovered in gsi-openssh-server 7.9p1 on Fedora 29. If PermitPAMUserChange is set to yes in the /etc/gsissh/sshd_config file, logins succeed with a valid username and an incorrect password, even though a failure entry is recorded in the /var/log/messages file.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1673802
- https://bugzilla.redhat.com/show_bug.cgi?id=1673802

---

#### 985. CVE-2019-14844

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
A flaw was found in, Fedora versions of krb5 from 1.16.1 to, including 1.17.x, in the way a Kerberos client could crash the KDC by sending one of the RFC 4556 "enctypes". A remote unauthenticated user could use this flaw to crash the KDC.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2019-14844
- https://github.com/krb5/krb5/pull/981
- https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/54ZYKEJZ77BXZWGF4NEVKC33ESVROEYC/
- https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/N4LS5PIJOCNOUZGLO2OBT6GY334PUOSW/
- https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/TDE2QOKK4I4TV4WV74ZQWICZ4HJN2MOK/

---

#### 986. CVE-2012-1615

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
A Privilege Escalation vulnerability exits in Fedoraproject Sectool due to an incorrect DBus file.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-April/076873.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-May/081113.html
- http://www.openwall.com/lists/oss-security/2012/04/04/2
- http://www.securityfocus.com/bid/52884
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2012-1615

---

#### 987. CVE-2020-14312

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
A flaw was found in the default configuration of dnsmasq, as shipped with Fedora versions prior to 31 and in all versions Red Hat Enterprise Linux, where it listens on any interface and accepts queries from addresses outside of its local subnet. In particular, the option `local-service` is not enabled. Running dnsmasq in this manner may inadvertently make it an open resolver accessible from any address on the internet. This flaw allows an attacker to conduct a Distributed Denial of Service (DDoS) against other systems.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1851342
- https://bugzilla.redhat.com/show_bug.cgi?id=1851342

---

#### 988. CVE-2021-41583

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
vpn-user-portal (aka eduVPN or Let's Connect!) before 2.3.14, as packaged for Debian 10, Debian 11, and Fedora, allows remote authenticated users to obtain OS filesystem access, because of the interaction of QR codes with an exec that uses the -r option. This can be leveraged to obtain additional VPN access.

**参考链接 / References**:
- https://list.surfnet.nl/pipermail/eduvpn-deploy/2021-September/000352.html
- https://github.com/eduvpn/vpn-user-portal/releases
- https://list.surfnet.nl/pipermail/eduvpn-deploy/2021-September/000352.html

---

#### 989. CVE-2021-43816

**严重程度 / Severity**: HIGH | CVSS: 8.0

**漏洞描述 / Description**:
containerd is an open source container runtime. On installations using SELinux, such as EL8 (CentOS, RHEL), Fedora, or SUSE MicroOS, with containerd since v1.5.0-beta.0 as the backing container runtime interface (CRI), an unprivileged pod scheduled to the node may bind mount, via hostPath volume, any privileged, regular file on disk for complete read/write access (sans delete). Such is achieved by placing the in-container location of the hostPath volume mount at either `/etc/hosts`, `/etc/hostname`, or `/etc/resolv.conf`. These locations are being relabeled indiscriminately to match the container process-label which effectively elevates permissions for savvy containers that would not normally be able to access privileged host files. This issue has been resolved in version 1.5.9. Users are advised to upgrade as soon as possible.

**参考链接 / References**:
- https://github.com/containerd/containerd/commit/a731039238c62be081eb8c31525b988415745eea
- https://github.com/containerd/containerd/issues/6194
- https://github.com/containerd/containerd/security/advisories/GHSA-mvff-h3cj-wj9c
- https://github.com/dweomer/containerd/commit/f7f08f0e34fb97392b0d382e58916d6865100299
- https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/GD5GH7NMK5VJMA2Y5CYB5O5GTPYMWMLX/

---

#### 990. CVE-2021-20269

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
A flaw was found in the permissions of a log file created by kexec-tools. This flaw allows a local unprivileged user to read this file and leak kernel internal information from a previous panic. The highest threat from this vulnerability is to confidentiality. This flaw affects kexec-tools shipped by Fedora versions prior to 2.0.21-8 and RHEL versions prior to 2.0.20-47.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1934261
- https://bugzilla.redhat.com/show_bug.cgi?id=1934261

---

#### 991. CVE-2022-3675

**严重程度 / Severity**: LOW | CVSS: 2.6

**漏洞描述 / Description**:
Fedora CoreOS supports setting a GRUB bootloader password
using a Butane config. When this feature is enabled, GRUB requires a password to access the
GRUB command-line, modify kernel command-line arguments, or boot
non-default OSTree deployments.  Recent Fedora CoreOS releases have a
misconfiguration which allows booting non-default OSTree deployments
without entering a password.  This allows someone with access to the
GRUB menu to boot into an older version of Fedora CoreOS, reverting
any security fixes that have recently been applied to the machine.  A
password is still required to modify kernel command-line arguments and
to access the GRUB command line.

**参考链接 / References**:
- https://docs.fedoraproject.org/en-US/fedora-coreos/grub-password/
- https://github.com/coreos/fedora-coreos-tracker/issues/1333
- https://lists.fedoraproject.org/archives/list/coreos-status@lists.fedoraproject.org/thread/NHUCNH5Y4UH5DPUCXISYXXVA563TLFEJ/
- https://docs.fedoraproject.org/en-US/fedora-coreos/grub-password/
- https://github.com/coreos/fedora-coreos-tracker/issues/1333

---

#### 992. CVE-2020-27418

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
A Use After Free vulnerability in Fedora Linux kernel 5.9.0-rc9 allows attackers to obatin sensitive information via vgacon_invert_region() function.

**参考链接 / References**:
- http://fedora.com
- https://patchwork.freedesktop.org/patch/356372/
- http://fedora.com
- https://patchwork.freedesktop.org/patch/356372/

---

#### 993. CVE-2022-3874

**严重程度 / Severity**: HIGH | CVSS: 8.0

**漏洞描述 / Description**:
A command injection flaw was found in foreman. This flaw allows an authenticated user with admin privileges on the foreman instance to transpile commands through CoreOS and Fedora CoreOS configurations in templates, possibly resulting in arbitrary command execution on the underlying operating system.

**参考链接 / References**:
- https://access.redhat.com/security/cve/CVE-2022-3874
- https://bugzilla.redhat.com/show_bug.cgi?id=2140577
- https://access.redhat.com/security/cve/CVE-2022-3874
- https://bugzilla.redhat.com/show_bug.cgi?id=2140577

---

#### 994. CVE-2025-23011

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Fedora Repository 3.8.1 allows path traversal when extracting uploaded archives ("Zip Slip"). A remote, authenticated attacker can upload a specially crafted archive that will extract an arbitrary JSP file to a location that can be executed by an unauthenticated GET request. Fedora Repository 3.8.1 was released on 2015-06-11 and is no longer maintained. Migrate to a currently supported version (6.5.1 as of 2025-01-23).

**参考链接 / References**:
- https://github.com/fcrepo-exts/migration-utils
- https://github.com/fcrepo/fcrepo/releases
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2025/va-25-021-01.json

---

#### 995. CVE-2025-23012

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Fedora Repository 3.8.x includes a service account (fedoraIntCallUser) with default credentials and privileges to read read local files by manipulating datastreams. Fedora Repository 3.8.1 was released on 2015-06-11 and is no longer maintained. Migrate to a currently supported version (6.5.1 as of 2025-01-23).

**参考链接 / References**:
- https://github.com/fcrepo-exts/migration-utils
- https://github.com/fcrepo/fcrepo/releases
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2025/va-25-021-01.json
- https://wiki.lyrasis.org/display/FEDORA38/XACML+Policy+Enforcement#XACMLPolicyEnforcement-4.1fedora-usersattributes

---

#### 996. CVE-2025-21710

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

tcp: correct handling of extreme memory squeeze

Testing with iperf3 using the "pasta" protocol splicer has revealed
a problem in the way tcp handles window advertising in extreme memory
squeeze situations.

Under memory pressure, a socket endpoint may temporarily advertise
a zero-sized window, but this is not stored as part of the socket data.
The reasoning behind this is that it is considered a temporary setting
which shouldn't influence any further calculations.

However, if we happen to stall at an unfortunate value of the current
window size, the algorithm selecting a new value will consistently fail
to advertise a non-zero window once we have freed up enough memory.
This means that this side's notion of the current window size is
different from the one last advertised to the peer, causing the latter
to not send any data to resolve the sitution.

The problem occurs on the iperf3 server side, and the socket in question
is a completely regular socket with the default settings for the
fedora40 kernel. We do not use SO_PEEK or SO_RCVBUF on the socket.

The following excerpt of a logging session, with own comments added,
shows more in detail what is happening:

//              tcp_v4_rcv(->)
//                tcp_rcv_established(->)
[5201<->39222]:     ==== Activating log @ net/ipv4/tcp_input.c/tcp_data_queue()/5257 ====
[5201<->39222]:     tcp_data_queue(->)
[5201<->39222]:        DROPPING skb [265600160..265665640], reason: SKB_DROP_REASON_PROTO_MEM
                       [rcv_nxt 265600160, rcv_wnd 262144, snt_ack 265469200, win_now 131184]
                       [copied_seq 259909392->260034360 (124968), unread 5565800, qlen 85, ofoq 0]
                       [OFO queue: gap: 65480, len: 0]
[5201<->39222]:     tcp_data_queue(<-)
[5201<->39222]:     __tcp_transmit_skb(->)
                        [tp->rcv_wup: 265469200, tp->rcv_wnd: 262144, tp->rcv_nxt 265600160]
[5201<->39222]:       tcp_select_window(->)
[5201<->39222]:         (inet_csk(sk)->icsk_ack.pending & ICSK_ACK_NOMEM) ? --> TRUE
                        [tp->rcv_wup: 265469200, tp->rcv_wnd: 262144, tp->rcv_nxt 265600160]
                        returning 0
[5201<->39222]:       tcp_select_window(<-)
[5201<->39222]:       ADVERTISING WIN 0, ACK_SEQ: 265600160
[5201<->39222]:     [__tcp_transmit_skb(<-)
[5201<->39222]:   tcp_rcv_established(<-)
[5201<->39222]: tcp_v4_rcv(<-)

// Receive queue is at 85 buffers and we are out of memory.
// We drop the incoming buffer, although it is in sequence, and decide
// to send an advertisement with a window of zero.
// We don't update tp->rcv_wnd and tp->rcv_wup accordingly, which means
// we unconditionally shrink the window.

[5201<->39222]: tcp_recvmsg_locked(->)
[5201<->39222]:   __tcp_cleanup_rbuf(->) tp->rcv_wup: 265469200, tp->rcv_wnd: 262144, tp->rcv_nxt 265600160
[5201<->39222]:     [new_win = 0, win_now = 131184, 2 * win_now = 262368]
[5201<->39222]:     [new_win >= (2 * win_now) ? --> time_to_ack = 0]
[5201<->39222]:     NOT calling tcp_send_ack()
                    [tp->rcv_wup: 265469200, tp->rcv_wnd: 262144, tp->rcv_nxt 265600160]
[5201<->39222]:   __tcp_cleanup_rbuf(<-)
                  [rcv_nxt 265600160, rcv_wnd 262144, snt_ack 265469200, win_now 131184]
                  [copied_seq 260040464->260040464 (0), unread 5559696, qlen 85, ofoq 0]
                  returning 6104 bytes
[5201<->39222]: tcp_recvmsg_locked(<-)

// After each read, the algorithm for calculating the new receive
// window in __tcp_cleanup_rbuf() finds it is too small to advertise
// or to update tp->rcv_wnd.
// Meanwhile, the peer thinks the window is zero, and will not send
// any more data to trigger an update from the interrupt mode side.

[5201<->39222]: tcp_recvmsg_locked(->)
[5201<->39222]:   __tcp_cleanup_rbuf(->) tp->rcv_wup: 265469200, tp->rcv_wnd: 262144, tp->rcv_nxt 265600160
[5201<->39222]:     [new_win = 262144, win_now = 131184, 2 * win_n
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/1dd823a46e25ffde1492c391934f69a9e5eb574f
- https://git.kernel.org/stable/c/8c670bdfa58e48abad1d5b6ca1ee843ca91f7303
- https://git.kernel.org/stable/c/b01e7ceb35dcb7ffad413da657b78c3340a09039
- https://git.kernel.org/stable/c/b4055e2fe96f4ef101d8af0feb056d78d77514ff

---

#### 997. CVE-2025-27512

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Zincati is an auto-update agent for Fedora CoreOS hosts. Zincati ships a polkit rule which allows the `zincati` system user to use the actions `org.projectatomic.rpmostree1.deploy` to deploy updates to the system and `org.projectatomic.rpmostree1.finalize-deployment` to reboot the system into the deployed update. Since Zincati v0.0.24, this polkit rule contains a logic error which broadens access of those polkit actions to any unprivileged user rather than just the `zincati` system user. In practice, this means that any unprivileged user with access to the system D-Bus socket is able to deploy older Fedora CoreOS versions (which may have other known vulnerabilities). Note that rpm-ostree enforces that the selected version must be from the same branch the system is currently on so this cannot directly be used to deploy an attacker-controlled update payload. This primarily impacts users running untrusted workloads with access to the system D-Bus socket. Note that in general, untrusted workloads should not be given this access, whether containerized or not. By default, containers do not have access to the system D-Bus socket. The logic error is fixed in Zincati v0.0.30. A workaround is to manually add a following polkit rule, instructions for which are available in the GitHub Security Advisory.

**参考链接 / References**:
- https://github.com/coreos/zincati/commit/01d8e89f799e6ba21bdf7dc668abce23bd0d8f78
- https://github.com/coreos/zincati/commit/28a43aa2c1edda091ba659677d73c13e6e3ea99d
- https://github.com/coreos/zincati/releases/tag/v0.0.24
- https://github.com/coreos/zincati/releases/tag/v0.0.30
- https://github.com/coreos/zincati/security/advisories/GHSA-w6fv-6gcc-x825

---

#### 998. CVE-2025-38181

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

calipso: Fix null-ptr-deref in calipso_req_{set,del}attr().

syzkaller reported a null-ptr-deref in sock_omalloc() while allocating
a CALIPSO option.  [0]

The NULL is of struct sock, which was fetched by sk_to_full_sk() in
calipso_req_setattr().

Since commit a1a5344ddbe8 ("tcp: avoid two atomic ops for syncookies"),
reqsk->rsk_listener could be NULL when SYN Cookie is returned to its
client, as hinted by the leading SYN Cookie log.

Here are 3 options to fix the bug:

  1) Return 0 in calipso_req_setattr()
  2) Return an error in calipso_req_setattr()
  3) Alaways set rsk_listener

1) is no go as it bypasses LSM, but 2) effectively disables SYN Cookie
for CALIPSO.  3) is also no go as there have been many efforts to reduce
atomic ops and make TCP robust against DDoS.  See also commit 3b24d854cb35
("tcp/dccp: do not touch listener sk_refcnt under synflood").

As of the blamed commit, SYN Cookie already did not need refcounting,
and no one has stumbled on the bug for 9 years, so no CALIPSO user will
care about SYN Cookie.

Let's return an error in calipso_req_setattr() and calipso_req_delattr()
in the SYN Cookie case.

This can be reproduced by [1] on Fedora and now connect() of nc times out.

[0]:
TCP: request_sock_TCPv6: Possible SYN flooding on port [::]:20002. Sending cookies.
Oops: general protection fault, probably for non-canonical address 0xdffffc0000000006: 0000 [#1] PREEMPT SMP KASAN NOPTI
KASAN: null-ptr-deref in range [0x0000000000000030-0x0000000000000037]
CPU: 3 UID: 0 PID: 12262 Comm: syz.1.2611 Not tainted 6.14.0 #2
Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS rel-1.16.3-0-ga6ed6b701f0a-prebuilt.qemu.org 04/01/2014
RIP: 0010:read_pnet include/net/net_namespace.h:406 [inline]
RIP: 0010:sock_net include/net/sock.h:655 [inline]
RIP: 0010:sock_kmalloc+0x35/0x170 net/core/sock.c:2806
Code: 89 d5 41 54 55 89 f5 53 48 89 fb e8 25 e3 c6 fd e8 f0 91 e3 00 48 8d 7b 30 48 b8 00 00 00 00 00 fc ff df 48 89 fa 48 c1 ea 03 <80> 3c 02 00 0f 85 26 01 00 00 48 b8 00 00 00 00 00 fc ff df 4c 8b
RSP: 0018:ffff88811af89038 EFLAGS: 00010216
RAX: dffffc0000000000 RBX: 0000000000000000 RCX: ffff888105266400
RDX: 0000000000000006 RSI: ffff88800c890000 RDI: 0000000000000030
RBP: 0000000000000050 R08: 0000000000000000 R09: ffff88810526640e
R10: ffffed1020a4cc81 R11: ffff88810526640f R12: 0000000000000000
R13: 0000000000000820 R14: ffff888105266400 R15: 0000000000000050
FS:  00007f0653a07640(0000) GS:ffff88811af80000(0000) knlGS:0000000000000000
CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
CR2: 00007f863ba096f4 CR3: 00000000163c0005 CR4: 0000000000770ef0
PKRU: 80000000
Call Trace:
 <IRQ>
 ipv6_renew_options+0x279/0x950 net/ipv6/exthdrs.c:1288
 calipso_req_setattr+0x181/0x340 net/ipv6/calipso.c:1204
 calipso_req_setattr+0x56/0x80 net/netlabel/netlabel_calipso.c:597
 netlbl_req_setattr+0x18a/0x440 net/netlabel/netlabel_kapi.c:1249
 selinux_netlbl_inet_conn_request+0x1fb/0x320 security/selinux/netlabel.c:342
 selinux_inet_conn_request+0x1eb/0x2c0 security/selinux/hooks.c:5551
 security_inet_conn_request+0x50/0xa0 security/security.c:4945
 tcp_v6_route_req+0x22c/0x550 net/ipv6/tcp_ipv6.c:825
 tcp_conn_request+0xec8/0x2b70 net/ipv4/tcp_input.c:7275
 tcp_v6_conn_request+0x1e3/0x440 net/ipv6/tcp_ipv6.c:1328
 tcp_rcv_state_process+0xafa/0x52b0 net/ipv4/tcp_input.c:6781
 tcp_v6_do_rcv+0x8a6/0x1a40 net/ipv6/tcp_ipv6.c:1667
 tcp_v6_rcv+0x505e/0x5b50 net/ipv6/tcp_ipv6.c:1904
 ip6_protocol_deliver_rcu+0x17c/0x1da0 net/ipv6/ip6_input.c:436
 ip6_input_finish+0x103/0x180 net/ipv6/ip6_input.c:480
 NF_HOOK include/linux/netfilter.h:314 [inline]
 NF_HOOK include/linux/netfilter.h:308 [inline]
 ip6_input+0x13c/0x6b0 net/ipv6/ip6_input.c:491
 dst_input include/net/dst.h:469 [inline]
 ip6_rcv_finish net/ipv6/ip6_input.c:79 [inline]
 ip6_rcv_finish+0xb6/0x490 net/ipv6/ip6_input.c:69
 NF_HOOK include/linux/netfilter.h:314 [inline]
 NF_HOOK include/linux/netf
---truncated---

**参考链接 / References**:
- https://git.kernel.org/stable/c/058dd4a370f23a5553a9449f2db53d5bfa88d45e
- https://git.kernel.org/stable/c/10876da918fa1aec0227fb4c67647513447f53a9
- https://git.kernel.org/stable/c/956f1499412ed0953f6a116df7fdb855e9f1fc66
- https://git.kernel.org/stable/c/988edde4d52d5c02ea4dd95d7619372a5e2fb7b7
- https://git.kernel.org/stable/c/bde8833eb075ba8e8674de88e32de6b669966451

---

#### 999. CVE-2023-5342

**严重程度 / Severity**: MEDIUM | CVSS: 4.1

**漏洞描述 / Description**:
The Fedora Secure Boot CA certificate shipped with shim in Fedora was expired which could lead to old or invalid signed boot components being loaded.

**参考链接 / References**:
- https://access.redhat.com/security/cve/CVE-2023-5342
- https://bodhi.fedoraproject.org/updates/FEDORA-2024-2aa28a4cfc
- https://bugzilla.redhat.com/show_bug.cgi?id=2198977
- https://bugzilla.redhat.com/show_bug.cgi?id=2388707

---

#### 1000. CVE-2025-68183

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

ima: don't clear IMA_DIGSIG flag when setting or removing non-IMA xattr

Currently when both IMA and EVM are in fix mode, the IMA signature will
be reset to IMA hash if a program first stores IMA signature in
security.ima and then writes/removes some other security xattr for the
file.

For example, on Fedora, after booting the kernel with "ima_appraise=fix
evm=fix ima_policy=appraise_tcb" and installing rpm-plugin-ima,
installing/reinstalling a package will not make good reference IMA
signature generated. Instead IMA hash is generated,

    # getfattr -m - -d -e hex /usr/bin/bash
    # file: usr/bin/bash
    security.ima=0x0404...

This happens because when setting security.selinux, the IMA_DIGSIG flag
that had been set early was cleared. As a result, IMA hash is generated
when the file is closed.

Similarly, IMA signature can be cleared on file close after removing
security xattr like security.evm or setting/removing ACL.

Prevent replacing the IMA file signature with a file hash, by preventing
the IMA_DIGSIG flag from being reset.

Here's a minimal C reproducer which sets security.selinux as the last
step which can also replaced by removing security.evm or setting ACL,

    #include <stdio.h>
    #include <sys/xattr.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <string.h>
    #include <stdlib.h>

    int main() {
        const char* file_path = "/usr/sbin/test_binary";
        const char* hex_string = "030204d33204490066306402304";
        int length = strlen(hex_string);
        char* ima_attr_value;
        int fd;

        fd = open(file_path, O_WRONLY|O_CREAT|O_EXCL, 0644);
        if (fd == -1) {
            perror("Error opening file");
            return 1;
        }

        ima_attr_value = (char*)malloc(length / 2 );
        for (int i = 0, j = 0; i < length; i += 2, j++) {
            sscanf(hex_string + i, "%2hhx", &ima_attr_value[j]);
        }

        if (fsetxattr(fd, "security.ima", ima_attr_value, length/2, 0) == -1) {
            perror("Error setting extended attribute");
            close(fd);
            return 1;
        }

        const char* selinux_value= "system_u:object_r:bin_t:s0";
        if (fsetxattr(fd, "security.selinux", selinux_value, strlen(selinux_value), 0) == -1) {
            perror("Error setting extended attribute");
            close(fd);
            return 1;
        }

        close(fd);

        return 0;
    }

**参考链接 / References**:
- https://git.kernel.org/stable/c/02aa671c08a4834bef5166743a7b88686fbfa023
- https://git.kernel.org/stable/c/88b4cbcf6b041ae0f2fc8a34554a5b6a83a2b7cd
- https://git.kernel.org/stable/c/d2993a7e98eb70c737c6f5365a190e79c72b8407
- https://git.kernel.org/stable/c/edd824eb45e4f7e05ad3ab090dab6dbdb79cd292

---

#### 1001. CVE-2026-23215

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

x86/vmware: Fix hypercall clobbers

Fedora QA reported the following panic:

  BUG: unable to handle page fault for address: 0000000040003e54
  #PF: supervisor write access in kernel mode
  #PF: error_code(0x0002) - not-present page
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS edk2-20251119-3.fc43 11/19/2025
  RIP: 0010:vmware_hypercall4.constprop.0+0x52/0x90
  ..
  Call Trace:
   vmmouse_report_events+0x13e/0x1b0
   psmouse_handle_byte+0x15/0x60
   ps2_interrupt+0x8a/0xd0
   ...

because the QEMU VMware mouse emulation is buggy, and clears the top 32
bits of %rdi that the kernel kept a pointer in.

The QEMU vmmouse driver saves and restores the register state in a
"uint32_t data[6];" and as a result restores the state with the high
bits all cleared.

RDI originally contained the value of a valid kernel stack address
(0xff5eeb3240003e54).  After the vmware hypercall it now contains
0x40003e54, and we get a page fault as a result when it is dereferenced.

The proper fix would be in QEMU, but this works around the issue in the
kernel to keep old setups working, when old kernels had not happened to
keep any state in %rdi over the hypercall.

In theory this same issue exists for all the hypercalls in the vmmouse
driver; in practice it has only been seen with vmware_hypercall3() and
vmware_hypercall4().  For now, just mark RDI/RSI as clobbered for those
two calls.  This should have a minimal effect on code generation overall
as it should be rare for the compiler to want to make RDI/RSI live
across hypercalls.

**参考链接 / References**:
- https://git.kernel.org/stable/c/2687c848e57820651b9f69d30c4710f4219f7dbf
- https://git.kernel.org/stable/c/2f467a92df61eb516a4ec36ee16234dd4e5ccf00
- https://git.kernel.org/stable/c/feb603a69f830acb58f78d604f0c29e63cd38f87

---

#### 1002. CVE-2025-1272

**严重程度 / Severity**: HIGH | CVSS: 7.7

**漏洞描述 / Description**:
The Linux Kernel lockdown mode for kernel versions starting on 6.12 and above for Fedora Linux has the lockdown mode disabled without any warning. This may allow an attacker to gain access to sensitive information such kernel memory mappings, I/O ports, BPF and kprobes. Additionally unsigned modules can be loaded, leading to execution of untrusted code breaking breaking any Secure Boot protection. This vulnerability affects only Fedora Linux.

**参考链接 / References**:
- https://access.redhat.com/errata/RHSA-2025:6966
- https://access.redhat.com/security/cve/CVE-2025-1272
- https://bugzilla.redhat.com/show_bug.cgi?id=2345615

---

#### 1003. CVE-2005-3671

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
The Internet Key Exchange version 1 (IKEv1) implementation in Openswan 2 (openswan-2) before 2.4.4, and freeswan in SUSE LINUX 9.1 before 2.04_1.5.4-1.23, allow remote attackers to cause a denial of service via (1) a crafted packet using 3DES with an invalid key length, or (2) unspecified inputs when Aggressive Mode is enabled and the PSK is known, as demonstrated by the PROTOS ISAKMP Test Suite for IKEv1.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2005-12/0138.html
- http://archives.neohapsis.com/archives/bugtraq/2005-12/0161.html
- http://jvn.jp/niscc/NISCC-273756/index.html
- http://secunia.com/advisories/17581
- http://secunia.com/advisories/17680

---

#### 1004. CVE-2005-3655

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Heap-based buffer overflow in Novell Open Enterprise Server Remote Manager (novell-nrm) in Novell SUSE Linux Enterprise Server 9 allows remote attackers to execute arbitrary code via an HTTP POST request with a negative Content-Length parameter.

**参考链接 / References**:
- http://secunia.com/advisories/18484
- http://securityreason.com/securityalert/348
- http://securitytracker.com/id?1015487
- http://www.idefense.com/intelligence/vulnerabilities/display.php?id=371
- http://www.novell.com/linux/security/advisories/2006_02_novellnrm.html

---

#### 1005. CVE-2005-4744

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Off-by-one error in the sql_error function in sql_unixodbc.c in FreeRADIUS 1.0.2.5-5, and possibly other versions including 1.0.4, might allow remote attackers to cause a denial of service (crash) and possibly execute arbitrary code by causing the external database query to fail.  NOTE: this single issue is part of a larger-scale disclosure, originally by SUSE, which reported multiple issues that were disputed by FreeRADIUS.  Disputed issues included file descriptor leaks, memory disclosure, LDAP injection, and other issues.  Without additional information, the most recent FreeRADIUS report is being regarded as the authoritative source for this CVE identifier.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060404-01-U.asc
- http://rhn.redhat.com/errata/RHSA-2006-0271.html
- http://secunia.com/advisories/16712
- http://secunia.com/advisories/19497
- http://secunia.com/advisories/19518

---

#### 1006. CVE-2005-4772

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
liby2util in Yet another Setup Tool (YaST) in SUSE Linux before 20051007 preserves permissions and ownerships when copying a remote repository, which might allow local users to read or modify sensitive files, possibly giving local users the ability to exploit CVE-2005-3013.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15026
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15026

---

#### 1007. CVE-2005-4778

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The powersave daemon in SUSE Linux 10.0 before 20051007 has an unspecified "configuration problem," which allows local users to suspend the computer and possibly perform certain other unauthorized actions.

**参考链接 / References**:
- http://lists.suse.com/archive/suse-security-announce/2005-Oct/0002.html
- http://www.securityfocus.com/bid/15042
- http://lists.suse.com/archive/suse-security-announce/2005-Oct/0002.html
- http://www.securityfocus.com/bid/15042

---

#### 1008. CVE-2005-4788

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
resmgr in SUSE Linux 9.2 and 9.3, and possibly other distributions, allows local users to bypass access control rules for USB devices via "alternate syntax for specifying USB devices."

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15037
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15037

---

#### 1009. CVE-2005-4789

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
resmgr in SUSE Linux 9.2 and 9.3, and possibly other distributions, does not properly enforce class-specific exclude rules in some situations, which allows local users to bypass intended access restrictions for USB devices that set their class ID at the interface level.

**参考链接 / References**:
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15037
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15037

---

#### 1010. CVE-2005-4790

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
Multiple untrusted search path vulnerabilities in SUSE Linux 9.3 and 10.0, and possibly other distributions, cause the working directory to be added to LD_LIBRARY_PATH, which might allow local users to execute arbitrary code via (1) beagle, (2) tomboy, or (3) blam.  NOTE: in August 2007, the tomboy vector was reported for other distributions.

**参考链接 / References**:
- http://bugs.gentoo.org/show_bug.cgi?id=188806
- http://bugs.gentoo.org/show_bug.cgi?id=189249
- http://bugs.gentoo.org/show_bug.cgi?id=199841
- http://osvdb.org/39577
- http://osvdb.org/39578

---

#### 1011. CVE-2005-4791

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Multiple untrusted search path vulnerabilities in SUSE Linux 10.0 cause the working directory to be added to LD_LIBRARY_PATH, which might allow local users to execute arbitrary code via (1) liferea or (2) banshee.

**参考链接 / References**:
- http://osvdb.org/39580
- http://secunia.com/advisories/27771
- http://sourceforge.net/project/shownotes.php?release_id=555823&group_id=87005
- http://www.novell.com/linux/security/advisories/2005_22_sr.html
- http://www.securityfocus.com/bid/15040

---

#### 1012. CVE-2006-0043

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in the realpath function in nfs-server rpc.mountd, as used in SUSE Linux 9.1 through 10.0, allows local users to execute arbitrary code via unspecified vectors involving mount requests and symlinks.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=350020
- http://lists.suse.com/archive/suse-security-announce/2006-Jan/0007.html
- http://secunia.com/advisories/18614
- http://secunia.com/advisories/18638
- http://secunia.com/advisories/18889

---

#### 1013. CVE-2006-0646

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
ld in SUSE Linux 9.1 through 10.0, and SLES 9, in certain circumstances when linking binaries, can leave an empty RPATH or RUNPATH, which allows local attackers to execute arbitrary code as other users via by running an ld-linked application from the current directory, which could contain an attacker-controlled library file.

**参考链接 / References**:
- http://lists.suse.com/archive/suse-security-announce/2006-Feb/0003.html
- http://secunia.com/advisories/18811
- http://www.securityfocus.com/bid/16581
- http://lists.suse.com/archive/suse-security-announce/2006-Feb/0003.html
- http://secunia.com/advisories/18811

---

#### 1014. CVE-2006-2147

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
resmgrd in resmgr for SUSE Linux and other distributions does not properly handle when access to a USB device is granted by using "usb:<bus>,<dev>" notation, which grants access to all USB devices and allows local users to bypass intended restrictions.  NOTE: this is a different vulnerability than CVE-2005-4788.

**参考链接 / References**:
- http://lists.suse.com/archive/suse-security-announce/2006-Feb/0008.html
- http://secunia.com/advisories/19887
- http://secunia.com/advisories/19898
- http://www.debian.org/security/2006/dsa-1047
- http://www.securityfocus.com/bid/17752

---

#### 1015. CVE-2006-2752

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
The RedCarpet /etc/ximian/rcd.conf configuration file in Novell Linux Desktop 9 and SUSE SLES 9 has world-readable permissions, which allows attackers to obtain the rc (RedCarpet) password.

**参考链接 / References**:
- http://secunia.com/advisories/20396
- http://www.securityfocus.com/archive/1/435491/100/0/threaded
- http://secunia.com/advisories/20396
- http://www.securityfocus.com/archive/1/435491/100/0/threaded

---

#### 1016. CVE-2006-2658

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Directory traversal vulnerability in the xsp component in mod_mono in Mono/C# web server, as used in SUSE Open-Enterprise-Server 1 and SUSE Linux 9.2 through 10.0, allows remote attackers to read arbitrary files via a .. (dot dot) sequence in an HTTP request.

**参考链接 / References**:
- http://lists.suse.com/archive/suse-security-announce/2006-Sep/0005.html
- http://secunia.com/advisories/21840
- http://secunia.com/advisories/21847
- http://securitytracker.com/id?1016821
- http://www.securityfocus.com/bid/19929

---

#### 1017. CVE-2006-4884

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in IDevSpot iSupport 1.8 allow remote attackers to inject arbitrary web script or HTML via (1) the suser parameter in support/rightbar.php, (2) the ticket_id parameter in support/open_tickets.php, and (3) the cons_page_title parameter in index.php.  NOTE: the provenance of this information is unknown; the details are obtained from third party information.

**参考链接 / References**:
- http://www.securityfocus.com/bid/19963
- http://www.securityfocus.com/bid/19963

---

#### 1018. CVE-2006-5111

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The libksba library 0.9.12 and possibly other versions, as used by gpgsm in the newpg package on SUSE LINUX, allows attackers to cause a denial of service (application crash) via a malformed X.509 certificate in a signature.

**参考链接 / References**:
- http://secunia.com/advisories/22423
- http://secunia.com/advisories/22445
- http://secunia.com/advisories/22473
- http://www.mandriva.com/security/advisories?name=MDKSA-2006:183
- http://www.novell.com/linux/download/updates/101_x86_64.html

---

#### 1019. CVE-2006-5229

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
OpenSSH portable 4.1 on SUSE Linux, and possibly other platforms and versions, and possibly under limited configurations, allows remote attackers to determine valid usernames via timing discrepancies in which responses take longer for valid usernames than invalid ones, as demonstrated by sshtime.  NOTE: as of 20061014, it appears that this issue is dependent on the use of manually-set passwords that causes delays when processing /etc/shadow due to an increased number of rounds.

**参考链接 / References**:
- http://secunia.com/advisories/25979
- http://www.osvdb.org/32721
- http://www.securityfocus.com/archive/1/448025/100/0/threaded
- http://www.securityfocus.com/archive/1/448108/100/0/threaded
- http://www.securityfocus.com/archive/1/448156/100/0/threaded

---

#### 1020. CVE-2006-5616

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Multiple unspecified vulnerabilities in OpenPBS, as used in SUSE Linux 9.2 through 10.1, allow attackers to execute arbitrary code via unspecified vectors.

**参考链接 / References**:
- http://lists.suse.com/archive/suse-security-announce/2006-Oct/0007.html
- http://secunia.com/advisories/22637
- http://secunia.com/advisories/24716
- http://security.gentoo.org/glsa/glsa-200704-04.xml
- http://www.securityfocus.com/bid/20776

---

#### 1021. CVE-2006-6662

**严重程度 / Severity**: N/A | CVSS: 4.1

**漏洞描述 / Description**:
Unspecified vulnerability in Linux User Management (novell-lum) on SUSE Linux Enterprise Desktop 10 and Open Enterprise Server 9, under unspecified conditions, allows local users to log in to the console without a password.

**参考链接 / References**:
- http://secunia.com/advisories/23409
- http://www.novell.com/linux/security/advisories/2006_29_sr.html
- http://secunia.com/advisories/23409
- http://www.novell.com/linux/security/advisories/2006_29_sr.html

---

#### 1022. CVE-2007-0460

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Multiple buffer overflows in ulogd for SUSE Linux 9.3 up to 10.1, and possibly other distributions, have unknown impact and attack vectors related to "improper string length calculations."

**参考链接 / References**:
- http://osvdb.org/32939
- http://secunia.com/advisories/23863
- http://secunia.com/advisories/24524
- http://security.gentoo.org/glsa/glsa-200703-17.xml
- http://www.mandriva.com/security/advisories?name=MDKSA-2007:028

---

#### 1023. CVE-2007-4045

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The CUPS service, as used in SUSE Linux before 20070720 and other Linux distributions, allows remote attackers to cause a denial of service via unspecified vectors related to an incomplete fix for CVE-2007-0720 that introduced a different denial of service problem in SSL negotiation.

**参考链接 / References**:
- http://bugs.gentoo.org/show_bug.cgi?id=199195
- http://secunia.com/advisories/27577
- http://secunia.com/advisories/27615
- http://secunia.com/advisories/28113
- http://support.avaya.com/elmodocs2/security/ASA-2007-476.htm

---

#### 1024. CVE-2007-4074

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The default configuration of Centre for Speech Technology Research (CSTR) Festival 1.95 beta (aka 2.0 beta) on Gentoo Linux, SUSE Linux, and possibly other distributions, is run locally with elevated privileges without requiring authentication, which allows local and remote attackers to execute arbitrary commands via the local daemon on port 1314, a different vulnerability than CVE-2001-0956.  NOTE: this issue is local in some environments, but remote on others.

**参考链接 / References**:
- http://bugs.gentoo.org/show_bug.cgi?id=170477
- http://lists.opensuse.org/opensuse-security-announce/2007-10/msg00006.html
- http://secunia.com/advisories/26229
- http://secunia.com/advisories/27271
- http://security.gentoo.org/glsa/glsa-200707-10.xml

---

#### 1025. CVE-2007-4393

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The installation script for orarun on SUSE Linux before 20070810 places the oracle user into the disk group, which allows the local oracle user to read or write raw disk partitions.

**参考链接 / References**:
- http://osvdb.org/46403
- http://secunia.com/advisories/26395
- http://www.novell.com/linux/security/advisories/2007_16_sr.html
- http://osvdb.org/46403
- http://secunia.com/advisories/26395

---

#### 1026. CVE-2007-4394

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Unspecified vulnerability in a "core clean" cron job created by the findutils-locate package on SUSE Linux 10.0 and 10.1 and Enterprise Server 9 and 10 before 20070810 allows local users to delete of arbitrary files via unknown vectors.

**参考链接 / References**:
- http://osvdb.org/46404
- http://secunia.com/advisories/26395
- http://www.novell.com/linux/security/advisories/2007_16_sr.html
- http://osvdb.org/46404
- http://secunia.com/advisories/26395

---

#### 1027. CVE-2007-4432

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Untrusted search path vulnerability in the wrapper scripts for the (1) rug, (2) zen-updater, (3) zen-installer, and (4) zen-remover programs on SUSE Linux 10.1 and Enterprise 10 allows local users to gain privileges via modified (a) LD_LIBRARY_PATH and (b) MONO_GAC_PREFIX environment variables.

**参考链接 / References**:
- http://osvdb.org/46781
- http://osvdb.org/46782
- http://osvdb.org/46783
- http://osvdb.org/46784
- http://secunia.com/advisories/26543

---

#### 1028. CVE-2007-5195

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Unspecified vulnerability in the SSL implementation in Groupwise client system in the novell-groupwise-client package in SUSE Linux Enterprise Desktop 10 allows remote attackers to obtain credentials via a man-in-the-middle attack, a different vulnerability than CVE-2007-5196.

**参考链接 / References**:
- http://osvdb.org/45492
- http://secunia.com/advisories/27229
- http://www.novell.com/linux/security/advisories/2007_20_sr.html
- http://osvdb.org/45492
- http://secunia.com/advisories/27229

---

#### 1029. CVE-2007-5196

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in the SSL implementation in Groupwise client system in the novell-groupwise-client package in SUSE Linux Enterprise Desktop 10 allows remote attackers to obtain credentials via a man-in-the-middle attack, a different vulnerability than CVE-2007-5195.

**参考链接 / References**:
- http://osvdb.org/45491
- http://secunia.com/advisories/27229
- http://www.novell.com/linux/security/advisories/2007_20_sr.html
- http://osvdb.org/45491
- http://secunia.com/advisories/27229

---

#### 1030. CVE-2007-5200

**严重程度 / Severity**: N/A | CVSS: 3.3

**漏洞描述 / Description**:
hugin, as used on various operating systems including SUSE openSUSE 10.2 and 10.3, allows local users to overwrite arbitrary files via a symlink attack on the hugin_debug_optim_results.txt temporary file.

**参考链接 / References**:
- http://osvdb.org/42224
- http://secunia.com/advisories/27229
- http://secunia.com/advisories/27623
- http://secunia.com/advisories/27653
- http://secunia.com/advisories/27952

---

#### 1031. CVE-2007-5471

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
libgssapi before 0.6-13.7, as used by the ISC BIND named daemon in SUSE Linux Enterprise Server 10 SP 1, terminates upon an initialization error, which allows remote attackers to cause a denial of service (daemon exit) via a GSS-TSIG request.  NOTE: this issue probably affects other daemons that attempt to initialize this library within a chroot configuration or other invalid configuration.

**参考链接 / References**:
- http://osvdb.org/40935
- http://secunia.com/advisories/27189
- http://www.securityfocus.com/bid/26076
- https://exchange.xforce.ibmcloud.com/vulnerabilities/37233
- https://secure-support.novell.com/KanisaPlatform/Publishing/936/3665923_f.SAL_Public.html

---

#### 1032. CVE-2007-6167

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Untrusted search path vulnerability in yast2-core in SUSE Linux might allow local users to execute arbitrary code by creating a malicious yast2 module in the current working directory.

**参考链接 / References**:
- http://osvdb.org/44158
- http://secunia.com/advisories/27756
- http://www.novell.com/linux/security/advisories/2007_24_sr.html
- http://www.securityfocus.com/bid/26634
- http://osvdb.org/44158

---

#### 1033. CVE-2008-0731

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Linux kernel before 2.6.18.8-0.8 in SUSE openSUSE 10.2 does not properly handle failure of an AppArmor change_hat system call, which might allow attackers to trigger the unconfining of an apparmored task.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-02/msg00002.html
- http://secunia.com/advisories/28806
- http://lists.opensuse.org/opensuse-security-announce/2008-02/msg00002.html
- http://secunia.com/advisories/28806

---

#### 1034. CVE-2008-0732

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The init script for Apache Geronimo on SUSE Linux follows symlinks when performing a chown operation, which might allow local users to obtain access to unspecified files or directories.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-02/msg00003.html
- http://secunia.com/advisories/28838
- http://lists.opensuse.org/opensuse-security-announce/2008-02/msg00003.html
- http://secunia.com/advisories/28838

---

#### 1035. CVE-2008-2667

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
SQL injection vulnerability in the Courier Authentication Library (aka courier-authlib) before 0.60.6 on SUSE openSUSE 10.3 and 11.0, and other platforms, when MySQL and a non-Latin character set are used, allows remote attackers to execute arbitrary SQL commands via the username and unspecified other vectors.

**参考链接 / References**:
- http://bugs.gentoo.org/show_bug.cgi?id=225407
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00001.html
- http://secunia.com/advisories/30591
- http://secunia.com/advisories/30967
- http://security.gentoo.org/glsa/glsa-200809-05.xml

---

#### 1036. CVE-2008-3067

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
sudo in SUSE openSUSE 10.3 does not clear the stdin buffer when password entry times out, which might allow local users to obtain a password by reading stdin from the parent process after a sudo child process exits.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43618
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43618

---

#### 1037. CVE-2008-3187

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
zypp-refresh-patches in zypper in SUSE openSUSE 10.2, 10.3, and 11.0 does not ask the user before accepting repository keys, which allows remote repositories to cause a denial of service (package data corruption) via a spoofed key.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00006.html
- http://secunia.com/advisories/31167
- http://www.securityfocus.com/bid/30293
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43922
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00006.html

---

#### 1038. CVE-2008-3188

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
libxcrypt in SUSE openSUSE 11.0 uses the DES algorithm when the configuration specifies the MD5 algorithm, which makes it easier for attackers to conduct brute-force attacks against hashed passwords.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-07/msg00008.html
- http://lists.opensuse.org/opensuse-security-announce/2008-08/msg00001.html
- http://secunia.com/advisories/31096
- http://secunia.com/advisories/31339
- http://www.securityfocus.com/bid/30301

---

#### 1039. CVE-2008-4636

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
yast2-backup 2.14.2 through 2.16.6 on SUSE Linux and Novell Linux allows local users to gain privileges via shell metacharacters in filenames used by the backup process.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-11/msg00003.html
- http://osvdb.org/50284
- http://secunia.com/advisories/32832
- http://www.securityfocus.com/bid/32464
- https://exchange.xforce.ibmcloud.com/vulnerabilities/46879

---

#### 1040. CVE-2009-0310

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in SUSE blinux (aka sbl) in SUSE openSUSE 10.3 through 11.0 has unknown impact and attack vectors related to "incoming data and authentication-strings."

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-02/msg00002.html
- http://www.securityfocus.com/bid/33794
- https://exchange.xforce.ibmcloud.com/vulnerabilities/48797
- http://lists.opensuse.org/opensuse-security-announce/2009-02/msg00002.html
- http://www.securityfocus.com/bid/33794

---

#### 1041. CVE-2008-2025

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Apache Struts before 1.2.9-162.31.1 on SUSE Linux Enterprise (SLE) 11, before 1.2.9-108.2 on SUSE openSUSE 10.3, before 1.2.9-198.2 on SUSE openSUSE 11.0, and before 1.2.9-162.163.2 on SUSE openSUSE 11.1 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors related to "insufficient quoting of parameters."

**参考链接 / References**:
- http://download.opensuse.org/update/10.3-test/repodata/patch-struts-5872.xml
- http://lists.opensuse.org/opensuse-security-announce/2009-04/msg00003.html
- http://osvdb.org/53380
- http://secunia.com/advisories/34567
- http://secunia.com/advisories/34642

---

#### 1042. CVE-2009-1648

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The YaST2 LDAP module in yast2-ldap-server on SUSE Linux Enterprise Server 11 (aka SLE11) does not enable the firewall in certain circumstances involving reboots during online updates, which makes it easier for remote attackers to access network services.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-07/msg00002.html
- http://secunia.com/advisories/35685
- http://lists.opensuse.org/opensuse-security-announce/2009-07/msg00002.html
- http://secunia.com/advisories/35685

---

#### 1043. CVE-2009-2707

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
Unspecified vulnerability in ia32el (aka the IA 32 emulation functionality) before 7042_7022-0.4.2 in SUSE Linux Enterprise (SLE) 10 SP2 on Itanium IA64 machines allows local users to cause a denial of service (system crash) via a 32-bit x86 application.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-09/msg00001.html
- http://support.novell.com/security/cve/CVE-2009-2707.html
- http://www.securityfocus.com/bid/36393
- https://bugs.launchpad.net/bugs/cve/2009-2707
- https://bugzilla.novell.com/show_bug.cgi?id=521524

---

#### 1044. CVE-2009-1297

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
iscsi_discovery in open-iscsi in SUSE openSUSE 10.3 through 11.1 and SUSE Linux Enterprise (SLE) 10 SP2 and 11, and other operating systems, allows local users to overwrite arbitrary files via a symlink attack on an unspecified temporary file that has a predictable name.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-10/msg00001.html
- http://www.mandriva.com/security/advisories?name=MDVSA-2013:109
- https://wiki.mageia.org/en/Support/Advisories/MGASA-2012-0241
- http://lists.opensuse.org/opensuse-security-announce/2009-10/msg00001.html
- http://www.mandriva.com/security/advisories?name=MDVSA-2013:109

---

#### 1045. CVE-2010-0230

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SUSE Linux Enterprise 10 SP3 (SLE10-SP3) and openSUSE 11.2 configures postfix to listen on all network interfaces, which might allow remote attackers to bypass intended access restrictions.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2010-01/msg00007.html
- http://lists.opensuse.org/opensuse-security-announce/2010-02/msg00004.html
- http://lists.opensuse.org/opensuse-security-announce/2010-01/msg00007.html
- http://lists.opensuse.org/opensuse-security-announce/2010-02/msg00004.html

---

#### 1046. CVE-2010-1325

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site request forgery (CSRF) vulnerability in the apache2-slms package in SUSE Lifecycle Management Server (SLMS) 1.0 on SUSE Linux Enterprise (SLE) 11 allows remote attackers to hijack the authentication of unspecified victims via vectors related to improper parameter quoting.  NOTE: some sources report that this is a vulnerability in a product named "Apache SLMS," but that is incorrect.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2010-08/msg00001.html
- http://support.novell.com/security/cve/CVE-2010-1325.html
- http://www.securityfocus.com/bid/42121
- https://bugzilla.novell.com/show_bug.cgi?id=588284
- https://exchange.xforce.ibmcloud.com/vulnerabilities/61006

---

#### 1047. CVE-2010-1507

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
WebYaST in yast2-webclient in SUSE Linux Enterprise (SLE) 11 on the WebYaST appliance uses a fixed secret key that is embedded in the appliance's image, which allows remote attackers to spoof session cookies by leveraging knowledge of this key.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2010-08/msg00001.html
- http://support.novell.com/security/cve/CVE-2010-1507.html
- http://www.securityfocus.com/bid/42128
- https://bugzilla.novell.com/show_bug.cgi?id=591345
- https://bugzilla.novell.com/show_bug.cgi?id=598834

---

#### 1048. CVE-2010-2532

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
lxsession-logout in lxsession in LXDE, as used on SUSE openSUSE 11.3 and other platforms, does not lock the screen when the Suspend or Hibernate button is pressed, which might make it easier for physically proximate attackers to access an unattended laptop via a resume action. NOTE: there is no general agreement that this is a vulnerability, because separate control over locking can be an equally secure, or more secure, behavior in some threat environments.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2010-08/msg00001.html
- http://www.openwall.com/lists/oss-security/2010/07/15/1
- http://www.openwall.com/lists/oss-security/2010/07/16/4
- https://bugzilla.novell.com/show_bug.cgi?id=622083
- https://bugzilla.redhat.com/show_bug.cgi?id=614608

---

#### 1049. CVE-2010-3087

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
LibTIFF before 3.9.2-5.2.1 in SUSE openSUSE 11.3 allows remote attackers to cause a denial of service (memory corruption) or possibly execute arbitrary code via a crafted TIFF image.

**参考链接 / References**:
- http://blackberry.com/btsc/KB27244
- http://lists.opensuse.org/opensuse-security-announce/2010-09/msg00006.html
- http://secunia.com/advisories/50726
- http://security.gentoo.org/glsa/glsa-201209-02.xml
- http://support.novell.com/security/cve/CVE-2010-3087.html

---

#### 1050. CVE-2010-3110

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Multiple buffer overflows in the Novell Client novfs module for the Linux kernel in SUSE Linux Enterprise 11 SP1 and openSUSE 11.3 allow local users to gain privileges via unspecified vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2010-08/msg00000.html
- http://lists.opensuse.org/opensuse-security-announce/2010-08/msg00000.html

---

#### 1051. CVE-2010-3912

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The supportconfig script in supportutils in SUSE Linux Enterprise 11 SP1 and 10 SP3 does not "disguise passwords" in configuration files, which has unknown impact and attack vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00003.html
- http://osvdb.org/70405
- http://secunia.com/advisories/42877
- http://www.vupen.com/english/advisories/2011/0076
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64690

---

#### 1052. CVE-2011-1550

**严重程度 / Severity**: N/A | CVSS: 6.3

**漏洞描述 / Description**:
The default configuration of logrotate on SUSE openSUSE Factory uses root privileges to process files in directories that permit non-root write access, which allows local users to conduct symlink and hard link attacks by leveraging logrotate's lack of support for untrusted directories, as demonstrated by directories for the (1) cobbler, (2) inn, (3) safte-monitor, and (4) uucp packages.

**参考链接 / References**:
- http://openwall.com/lists/oss-security/2011/03/04/16
- http://openwall.com/lists/oss-security/2011/03/04/17
- http://openwall.com/lists/oss-security/2011/03/04/18
- http://openwall.com/lists/oss-security/2011/03/04/19
- http://openwall.com/lists/oss-security/2011/03/04/22

---

#### 1053. CVE-2011-1551

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
SUSE openSUSE Factory assigns ownership of the /var/log/cobbler/ directory tree to the web-service user account, which might allow local users to gain privileges by leveraging access to this account during root filesystem operations by the Cobbler daemon.

**参考链接 / References**:
- http://openwall.com/lists/oss-security/2011/03/23/11
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66487
- http://openwall.com/lists/oss-security/2011/03/23/11
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66487

---

#### 1054. CVE-2011-0461

**严重程度 / Severity**: N/A | CVSS: 6.3

**漏洞描述 / Description**:
/etc/init.d/boot.localfs in the aaa_base package before 11.2-43.48.1 in SUSE openSUSE 11.2, and before 11.3-8.7.1 in openSUSE 11.3, allows local users to overwrite arbitrary files via a symlink attack on /dev/shm/mtab.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-04/msg00000.html
- http://lists.opensuse.org/opensuse-security-announce/2011-05/msg00005.html
- http://lists.opensuse.org/opensuse-updates/2011-03/msg00007.html
- http://support.novell.com/security/cve/CVE-2011-0461.html
- https://bugzilla.novell.com/665479

---

#### 1055. CVE-2011-0468

**严重程度 / Severity**: N/A | CVSS: 6.9

**漏洞描述 / Description**:
The aaa_base package before 11.3-8.9.1 in SUSE openSUSE 11.3, and before 11.4-54.62.1 in openSUSE 11.4, allows local users to gain privileges via shell metacharacters in a filename, related to tab expansion.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-04/msg00000.html
- http://lists.opensuse.org/opensuse-updates/2011-03/msg00010.html
- http://secunia.com/advisories/43825
- http://support.novell.com/security/cve/CVE-2011-0468.html
- http://www.osvdb.org/71253

---

#### 1056. CVE-2011-0462

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the login page in the webui component in SUSE openSUSE Build Service (OBS) before 2.1.6 allow remote attackers to inject arbitrary web script or HTML via unspecified vectors.

**参考链接 / References**:
- http://news.opensuse.org/2011/03/02/build-service-team-releases-new-versions-fixing-security-problems/
- https://bugzilla.novell.com/show_bug.cgi?id=669909
- http://news.opensuse.org/2011/03/02/build-service-team-releases-new-versions-fixing-security-problems/
- https://bugzilla.novell.com/show_bug.cgi?id=669909

---

#### 1057. CVE-2011-0466

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
The API in SUSE openSUSE Build Service (OBS) 2.0.x before 2.0.8 and 2.1.x before 2.1.6 allows attackers to bypass intended write-access restrictions and modify a (1) package or (2) project via unspecified vectors.

**参考链接 / References**:
- http://news.opensuse.org/2011/03/02/build-service-team-releases-new-versions-fixing-security-problems/
- http://news.opensuse.org/2011/03/02/build-service-team-releases-new-versions-fixing-security-problems/

---

#### 1058. CVE-2011-0988

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
pure-ftpd 1.0.22, as used in SUSE Linux Enterprise Server 10 SP3 and SP4, and Enterprise Desktop 10 SP3 and SP4, when running OES Netware extensions, creates a world-writeable directory, which allows local users to overwrite arbitrary files and gain privileges via unspecified vectors.

**参考链接 / References**:
- http://secunia.com/advisories/44039
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66618
- https://hermes.opensuse.org/messages/7849430
- http://secunia.com/advisories/44039
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66618

---

#### 1059. CVE-2011-0995

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The sqlite3-ruby gem in the rubygem-sqlite3 package before 1.2.4-0.5.1 in SUSE Linux Enterprise (SLE) 11 SP1 uses weak permissions for unspecified files, which allows local users to gain privileges via unknown vectors.

**参考链接 / References**:
- http://secunia.com/advisories/44418
- http://support.novell.com/security/cve/CVE-2011-0995.html
- http://www.osvdb.org/72180
- http://www.securityfocus.com/bid/47694
- https://bugzilla.novell.com/show_bug.cgi?id=685928

---

#### 1060. CVE-2011-2225

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
Unspecified vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows attackers to have an unknown impact via a crafted directory pathname that is inserted into config.sh.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2225.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=709572
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69277

---

#### 1061. CVE-2011-2226

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to inject arbitrary web script or HTML via unspecified vectors, related to a pattern listing.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2226.html
- http://www.securityfocus.com/bid/49236
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69278
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html

---

#### 1062. CVE-2011-2644

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to inject arbitrary web script or HTML via unspecified vectors, related to an RPM info display.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2644.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=700591
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69279

---

#### 1063. CVE-2011-2645

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to execute arbitrary code via a crafted filename for a custom RPM.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2645.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=700948
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69280

---

#### 1064. CVE-2011-2646

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to execute arbitrary code via a crafted filename in the list of testdrive modified files.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2646.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=700588
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69281

---

#### 1065. CVE-2011-2647

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to execute arbitrary code via a crafted archive name in the list of testdrive modified files.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2647.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=700589
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69282

---

#### 1066. CVE-2011-2648

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to execute arbitrary code via a filter in a modified file.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2648.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=701814
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69283

---

#### 1067. CVE-2011-2649

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows attackers to execute arbitrary commands via shell metacharacters in an unspecified FileUtils function call.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2649.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=701815
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69284

---

#### 1068. CVE-2011-2650

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to inject arbitrary web script or HTML via a crafted pattern name that is included in an RPM info display.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2650.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=701816
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69285

---

#### 1069. CVE-2011-2651

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unspecified vulnerability in the file browser in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to execute arbitrary code via a crafted filename.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2651.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=702041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69286

---

#### 1070. CVE-2011-2652

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Kiwi before 3.74.2, as used in SUSE Studio 1.1 before 1.1.4, allows remote attackers to inject arbitrary web script or HTML via a crafted archive file list that is used in an overlay file.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00013.html
- http://support.novell.com/security/cve/CVE-2011-2652.html
- http://www.securityfocus.com/bid/49236
- https://bugzilla.novell.com/show_bug.cgi?id=702320
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69287

---

#### 1071. CVE-2011-2660

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The modify_resolvconf_suse script in the vpnc package before 0.5.1-55.10.1 in SUSE Linux Enterprise Desktop 11 SP1 might allow remote attackers to execute arbitrary commands via a crafted DNS domain name.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00028.html
- http://lists.opensuse.org/opensuse-security-announce/2011-08/msg00029.html
- http://www.securityfocus.com/bid/49391
- https://bugzilla.novell.com/651577
- https://bugzilla.novell.com/708656

---

#### 1072. CVE-2011-3171

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
Directory traversal vulnerability in pure-FTPd 1.0.22 and possibly other versions, when running on SUSE Linux Enterprise Server and possibly other operating systems, when the Netware OES remote server feature is enabled, allows local users to overwrite arbitrary files via unknown vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-09/msg00015.html
- http://lists.opensuse.org/opensuse-security-announce/2011-09/msg00016.html
- http://www.securityfocus.com/bid/49541
- https://exchange.xforce.ibmcloud.com/vulnerabilities/69686
- http://lists.opensuse.org/opensuse-security-announce/2011-09/msg00015.html

---

#### 1073. CVE-2012-0421

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The SUSE Audit Log Keeper daemon before 0.2.1-0.4.6.1 for SUSE Manager and Spacewalk uses world-readable permissions for /etc/auditlog-keeper.conf, which allows local users to obtain passwords by reading this file.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2012-08/msg00001.html
- https://bugzilla.novell.com/771335
- http://lists.opensuse.org/opensuse-security-announce/2012-08/msg00001.html
- https://bugzilla.novell.com/771335

---

#### 1074. CVE-2012-0435

**严重程度 / Severity**: N/A | CVSS: 5.8

**漏洞描述 / Description**:
SUSE WebYaST before 1.2 0.2.63-0.6.1 allows remote attackers to modify the hosts list, and subsequently conduct man-in-the-middle attacks, via a crafted /host request on TCP port 4984.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2013-01/msg00008.html
- http://support.novell.com/security/cve/CVE-2012-0435.html
- http://www.kb.cert.org/vuls/id/806908
- https://bugzilla.novell.com/show_bug.cgi?id=792712
- http://lists.opensuse.org/opensuse-security-announce/2013-01/msg00008.html

---

#### 1075. CVE-2013-0221

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The SUSE coreutils-i18n.patch for GNU coreutils allows context-dependent attackers to cause a denial of service (segmentation fault and crash) via a long string to the sort command, when using the (1) -d or (2) -M switch, which triggers a stack-based buffer overflow in the alloca function.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2013-1652.html
- https://bugzilla.novell.com/show_bug.cgi?id=798538
- https://bugzilla.redhat.com/show_bug.cgi?id=903464
- https://build.opensuse.org/request/show/149348#diff_headline_coreutils-i18n-patch_diff_action_0_submit_0_19
- http://rhn.redhat.com/errata/RHSA-2013-1652.html

---

#### 1076. CVE-2013-0222

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The SUSE coreutils-i18n.patch for GNU coreutils allows context-dependent attackers to cause a denial of service (segmentation fault and crash) via a long string to the uniq command, which triggers a stack-based buffer overflow in the alloca function.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2013-1652.html
- https://bugzilla.novell.com/show_bug.cgi?id=796243
- https://bugzilla.redhat.com/show_bug.cgi?id=903465
- https://build.opensuse.org/request/show/149348#diff_headline_coreutils-i18n-patch_diff_action_0_submit_0_19
- http://rhn.redhat.com/errata/RHSA-2013-1652.html

---

#### 1077. CVE-2013-0223

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The SUSE coreutils-i18n.patch for GNU coreutils allows context-dependent attackers to cause a denial of service (segmentation fault and crash) via a long string to the join command, when using the -i switch, which triggers a stack-based buffer overflow in the alloca function.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2013-1652.html
- https://bugzilla.novell.com/show_bug.cgi?id=798541
- https://bugzilla.redhat.com/show_bug.cgi?id=903466
- https://build.opensuse.org/request/show/149348#diff_headline_coreutils-i18n-patch_diff_action_0_submit_0_19
- http://rhn.redhat.com/errata/RHSA-2013-1652.html

---

#### 1078. CVE-2012-0414

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in the Spacewalk service in SUSE Manager 1.2 for SUSE Linux Enterprise (SLE) 11 SP1 allows remote attackers to inject arbitrary web script or HTML via an image name.

**参考链接 / References**:
- http://support.novell.com/docs/Readmes/InfoDocument/patchbuilder/readme_5145796.html
- https://bugzilla.novell.com/show_bug.cgi?id=761165
- https://support.novell.com/security/cve/CVE-2012-0414.html
- http://support.novell.com/docs/Readmes/InfoDocument/patchbuilder/readme_5145796.html
- https://bugzilla.novell.com/show_bug.cgi?id=761165

---

#### 1079. CVE-2012-0420

**严重程度 / Severity**: N/A | CVSS: 4.4

**漏洞描述 / Description**:
zypp-refresh-wrapper in SUSE Zypper before 1.3.20 and 1.6.x before 1.6.166 allows local users to create files in arbitrary directories, or possibly have unspecified other impact, via a pathname in the ZYPP_LOCKFILE_ROOT environment variable.

**参考链接 / References**:
- https://bugzilla.novell.com/show_bug.cgi?id=770630
- https://support.novell.com/security/cve/CVE-2012-0420.html
- https://bugzilla.novell.com/show_bug.cgi?id=770630
- https://support.novell.com/security/cve/CVE-2012-0420.html

---

#### 1080. CVE-2012-0425

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
LanItems.ycp in save_y2logs in yast2-network before 2.24.4 in SUSE YaST writes cleartext Wi-Fi credentials to the y2log log file, which allows context-dependent attackers to obtain sensitive information by reading the (1) WIRELESS_WPA_PASSWORD or (2) WIRELESS_CLIENT_KEY_PASSWORD field.

**参考链接 / References**:
- https://bugzilla.novell.com/show_bug.cgi?id=752464
- https://support.novell.com/security/cve/CVE-2012-0425.html
- https://bugzilla.novell.com/show_bug.cgi?id=752464
- https://support.novell.com/security/cve/CVE-2012-0425.html

---

#### 1081. CVE-2012-0426

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Race condition in sap_suse_cluster_connector before 1.0.0-0.8.1 in SUSE Linux Enterprise for SAP Applications 11 SP2 allows local users to have an unspecified impact via vectors related to a tmp/ directory.

**参考链接 / References**:
- http://download.novell.com/Download?buildid=DshQViDsMLE~
- https://bugzilla.novell.com/show_bug.cgi?id=763793
- https://bugzilla.novell.com/show_bug.cgi?id=777453
- https://bugzilla.novell.com/show_bug.cgi?id=778273
- https://bugzilla.novell.com/show_bug.cgi?id=778293

---

#### 1082. CVE-2012-0427

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
yast2-add-on-creator in SUSE inst-source-utils 2008.11.26 before 2008.11.26-0.9.1 and 2012.9.13 before 2012.9.13-0.8.1 allows local users to gain privileges via a crafted (1) file name or (2) directory name.

**参考链接 / References**:
- http://download.novell.com/Download?buildid=tGCXHQR48E4~
- https://bugzilla.novell.com/show_bug.cgi?id=604730
- https://support.novell.com/security/cve/CVE-2012-0427.html
- http://download.novell.com/Download?buildid=tGCXHQR48E4~
- https://bugzilla.novell.com/show_bug.cgi?id=604730

---

#### 1083. CVE-2012-0434

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The server in Crowbar, as used in SUSE Cloud 1.0, uses weak permissions for the production.log file, which has unspecified impact and attack vectors.

**参考链接 / References**:
- https://bugzilla.novell.com/show_bug.cgi?id=784857
- https://support.novell.com/security/cve/CVE-2012-0434.html
- https://www.suse.com/support/update/announcement/2013/suse-ru-20130020-1.html
- https://bugzilla.novell.com/show_bug.cgi?id=784857
- https://support.novell.com/security/cve/CVE-2012-0434.html

---

#### 1084. CVE-2013-1090

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The SUSE horde5 package before 5.0.2-2.4.1 sets incorrect ownership for certain configuration files and directories including /etc/apache2/vhosts.d, which allows local wwwrun users to gain privileges via unspecified vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-updates/2013-12/msg00025.html
- https://bugzilla.novell.com/show_bug.cgi?id=811369
- http://lists.opensuse.org/opensuse-updates/2013-12/msg00025.html
- https://bugzilla.novell.com/show_bug.cgi?id=811369

---

#### 1085. CVE-2013-3710

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
SUSE Lifecycle Management Server (SLMS) before 1.3.7 does not generate a new secret key when the service starts, which allows remote attackers to defeat intended cryptographic protection mechanisms by leveraging knowledge of this key from a product installation elsewhere.

**参考链接 / References**:
- http://osvdb.org/100653
- https://bugzilla.novell.com/show_bug.cgi?id=852101
- https://www.suse.com/support/update/announcement/2013/suse-su-20131813-1.html
- http://osvdb.org/100653
- https://bugzilla.novell.com/show_bug.cgi?id=852101

---

#### 1086. CVE-2013-7042

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
SUSE Lifecycle Management Server (SLMS) before 1.3.7 uses world-readable permissions for the secret keys, which allows local users to gain privileges via unspecified vectors.

**参考链接 / References**:
- http://osvdb.org/100652
- https://bugzilla.novell.com/show_bug.cgi?id=852101
- https://exchange.xforce.ibmcloud.com/vulnerabilities/89897
- https://www.suse.com/support/update/announcement/2013/suse-su-20131813-1.html
- http://osvdb.org/100652

---

#### 1087. CVE-2013-3712

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
SUSE Studio Onsite 1.3.x before 1.3.6 and SUSE Studio Extension for System z 1.3 uses "static" secret tokens, which has unspecified impact and vectors.

**参考链接 / References**:
- http://secunia.com/advisories/57050
- https://www.suse.com/support/update/announcement/2014/suse-su-20140254-1.html
- http://secunia.com/advisories/57050
- https://www.suse.com/support/update/announcement/2014/suse-su-20140254-1.html

---

#### 1088. CVE-2014-0592

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Barclamp (aka barclamp-network) 1.7 for the Crowbar Framework, as used in SUSE Cloud 3, does not enable netfilter on bridges when creating new instances, which allows remote attackers to bypass security group restrictions via unspecified vectors, related to floating IPs.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2014-03/msg00025.html
- http://secunia.com/advisories/57509
- http://www.securityfocus.com/bid/66519
- https://bugzilla.novell.com/show_bug.cgi?id=864183
- https://github.com/crowbar/barclamp-network/pull/269

---

#### 1089. CVE-2011-0993

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
SUSE Lifecycle Management Server before 1.1 uses world readable postgres credentials, which allows local users to obtain sensitive information via unspecified vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-04/msg00005.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/95697
- http://lists.opensuse.org/opensuse-security-announce/2011-04/msg00005.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/95697

---

#### 1090. CVE-2011-3180

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
kiwi before 4.98.08, as used in SUSE Studio Onsite 1.2 before 1.2.1 and SUSE Studio Extension for System z 1.2 before 1.2.1, allows attackers to execute arbitrary commands via shell metacharacters in the path of an overlay file, related to chown.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://www.openwall.com/lists/oss-security/2011/11/02/4
- https://github.com/openSUSE/kiwi/commit/f0f74b3f6ac6d47f7919aa9db380c0ad41ffe55f#
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://www.openwall.com/lists/oss-security/2011/11/02/4

---

#### 1091. CVE-2011-4192

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
kiwi before 4.85.1, as used in SUSE Studio Onsite 1.2 before 1.2.1 and SUSE Studio Extension for System z 1.2 before 1.2.1, allows attackers to execute arbitrary commands as demonstrated by "double quotes in kiwi_oemtitle of .profile."

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html

---

#### 1092. CVE-2011-4193

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in the overlay files tab in SUSE Studio Onsite 1.2 before 1.2.1 and SUSE Studio Extension for System z 1.2 before 1.2.1 allows remote attackers to inject arbitrary web script or HTML via a crafted application, related to cloning.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html

---

#### 1093. CVE-2011-4195

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
kiwi before 4.98.05, as used in SUSE Studio Onsite 1.2 before 1.2.1 and SUSE Studio Extension for System z 1.2 before 1.2.1, allows attackers to execute arbitrary commands via shell metacharacters in an image name.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://www.openwall.com/lists/oss-security/2011/11/02/4
- https://github.com/openSUSE/kiwi/commit/88bf491d16942766016c606e4210b4e072c1019f
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00015.html
- http://www.openwall.com/lists/oss-security/2011/11/02/4

---

#### 1094. CVE-2015-0777

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
drivers/xen/usbback/usbback.c in linux-2.6.18-xen-3.4.0 (aka the Xen 3.4.x support patches for the Linux kernel 2.6.18), as used in the Linux kernel 2.6.x and 3.x in SUSE Linux distributions, allows guest OS users to obtain sensitive information from uninitialized locations in host OS kernel memory via unspecified vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2015-04/msg00001.html
- http://lists.opensuse.org/opensuse-security-announce/2015-09/msg00004.html
- http://lists.opensuse.org/opensuse-security-announce/2015-09/msg00018.html
- http://lists.opensuse.org/opensuse-security-announce/2015-09/msg00021.html
- http://www.securityfocus.com/bid/73921

---

#### 1095. CVE-2015-5969

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
The mysql-systemd-helper script in the mysql-community-server package before 5.6.28-2.17.1 in openSUSE 13.2 and before 5.6.28-13.1 in openSUSE Leap 42.1 and the mariadb package before 10.0.22-2.21.2 in openSUSE 13.2 and before 10.0.22-3.1 in SUSE Linux Enterprise (SLE) 12.1 and openSUSE Leap 42.1 allows local users to discover database credentials by listing a process and its arguments.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2016-02/msg00015.html
- http://lists.opensuse.org/opensuse-updates/2016-02/msg00039.html
- http://lists.opensuse.org/opensuse-updates/2016-02/msg00050.html
- https://bugzilla.suse.com/957174
- https://www.suse.com/support/update/announcement/2016/suse-su-20160296-1.html

---

#### 1096. CVE-2016-4036

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
The quagga package before 0.99.23-2.6.1 in openSUSE and SUSE Linux Enterprise Server 11 SP 1 uses weak permissions for /etc/quagga, which allows local users to obtain sensitive information by reading files in the directory.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-updates/2016-04/msg00040.html
- http://www.debian.org/security/2016/dsa-3654
- http://www.securityfocus.com/bid/87324
- https://bugzilla.suse.com/show_bug.cgi?id=770619
- http://lists.opensuse.org/opensuse-updates/2016-04/msg00040.html

---

#### 1097. CVE-2016-1601

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
yast2-users before 3.1.47, as used in SUSE Linux Enterprise 12 SP1, does not properly set empty password fields in /etc/shadow during an AutoYaST installation when the profile does not contain inst-sys users, which might allow attackers to have unspecified impact via unknown vectors.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2016-04/msg00051.html
- http://lists.opensuse.org/opensuse-security-announce/2016-05/msg00007.html
- https://bugzilla.suse.com/show_bug.cgi?id=974220
- https://build.opensuse.org/request/show/388020
- http://lists.opensuse.org/opensuse-security-announce/2016-04/msg00051.html

---

#### 1098. CVE-2016-1602

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
A code injection in the supportconfig data collection tool in supportutils in SUSE Linux Enterprise Server 12 and 12-SP1 and SUSE Linux Enterprise Desktop 12 and 12-SP1 could be used by local attackers to execute code as the user running supportconfig (usually root).

**参考链接 / References**:
- http://lists.suse.com/pipermail/sle-security-updates/2016-June/002096.html
- http://lists.suse.com/pipermail/sle-security-updates/2016-June/002096.html

---
