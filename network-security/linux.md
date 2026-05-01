# Linux 网络安全漏洞 | Linux Network Security

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 169**

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
