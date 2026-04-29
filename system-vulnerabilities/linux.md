# Linux 系统漏洞知识库 | Linux System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 326**

> 技术细节（漏洞描述、补丁信息等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, patch info) remain in original language for accuracy; structural text is bilingual.

---

#### 1. CVE-2000-0508

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux, mandrakesoft:mandrake_linux, redhat:linux

**漏洞描述 / Description**:
rpc.lockd in Red Hat Linux 6.1 and 6.2 allows remote attackers to cause a denial of service via a malformed request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0073.html.

---

#### 2. CVE-1999-0242

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
Remote attackers can access mail files via POP3 in some Linux systems that are using shadow passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0242.

---

#### 3. CVE-1999-0245

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Some configurations of NIS+ in Linux allowed attackers to log in as the user "+".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0245.

---

#### 4. CVE-1999-0123

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
Race condition in Linux mailx command allows local users to read user files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0123.

---

#### 5. CVE-1999-0316

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: sam_lantinga:splitvt

**漏洞描述 / Description**:
Buffer overflow in Linux splitvt command gives root access to local users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0316.

---

#### 6. CVE-1999-1186

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, slackware:slackware_linux, rxvt:rxvt

**漏洞描述 / Description**:
rxvt, when compiled with the PRINT_PIPE option in various Linux operating systems including Linux Slackware 3.0 and RedHat 2.1, allows local users to gain root privileges by specifying a malicious program using the -print-pipe command line parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602167418966&w=2.

---

#### 7. CVE-1999-0137

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: fred_n._van_kempen:dip

**漏洞描述 / Description**:
The dip program on many Linux systems allows local users to gain root access via a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0137.

---

#### 8. CVE-1999-0032

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: sgi:irix, bsdi:bsd_os, freebsd:freebsd, sun:sunos, next:nextstep

**漏洞描述 / Description**:
Buffer overflow in lpr, as used in BSD-based systems including Linux, allows local users to execute arbitrary code as root via a long -C (classification) command line option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/19980402-01-PX.

---

#### 9. CVE-1999-1299

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: slackware:slackware_linux, redhat:linux

**漏洞描述 / Description**:
rcp on various Linux systems including Red Hat 4.0 allows a "nobody" user or other user with UID of 65535 to overwrite arbitrary files, since 65535 is interpreted as -1 by chown and other system calls, which causes the calls to fail to modify the ownership of the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602167420509&w=2.

---

#### 10. CVE-1999-0298

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:sunos, slackware:slackware_linux

**漏洞描述 / Description**:
ypbind with -ypset and -ypsetme options activated in Linux Slackware and SunOS allows local and remote attackers to overwrite files via a .. (dot dot) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.nai.com/nai_labs/asp_set/advisory/06_ypbindsetme_adv.asp.

---

#### 11. CVE-1999-1489

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
Buffer overflow in TestChip function in XFree86 SuperProbe in Slackware Linux 3.1 allows local users to gain root privileges via a long -nopr argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/6384.

---

#### 12. CVE-1999-1387

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 SP2 allows remote attackers to cause a denial of service (crash), possibly via malformed inputs or packets, such as those generated by a Linux smbmount command that was compiled on the Linux 2.0.29 kernel but executed on Linux 2.0.25.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602167420731&w=2.

---

#### 13. CVE-1999-1182

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: caldera:openlinux_lite, delix:dld, lst:lst_power_linux, suse:suse_linux, debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in run-time linkers (1) ld.so or (2) ld-linux.so for Linux systems allows local users to gain privileges by calling a setuid program with a long program name (argv[0]) and forcing ld.so/ld-linux.so to report an error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602661419318&w=2.

---

#### 14. CVE-1999-1225

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: openbsd:openbsd, digital:ultrix, linux:linux_kernel, sun:solaris, netbsd:netbsd

**漏洞描述 / Description**:
rpc.mountd on Linux, Ultrix, and possibly other operating systems, allows remote attackers to determine the existence of a file on the server by attempting to mount that file, which generates different error messages depending on whether the file exists or not.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/7526.

---

#### 15. CVE-1999-0183

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: tftp:tftp, linux:linux_kernel

**漏洞描述 / Description**:
Linux implementations of TFTP would allow access to files outside the restricted directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0183.

---

#### 16. CVE-1999-0216

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: gnu:inet, linux:linux_kernel, hp:hp-ux

**漏洞描述 / Description**:
Denial of service of inetd on Linux through SYN and RST packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0216.

---

#### 17. CVE-1999-0340

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
Buffer overflow in Linux Slackware crond program allows local users to gain root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0340.

---

#### 18. CVE-1999-0341

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux, slackware:slackware_linux

**漏洞描述 / Description**:
Buffer overflow in the Linux mail program "deliver" allows local users to gain root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0341.

---

#### 19. CVE-1999-1229

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: id_software:quake_2_server

**漏洞描述 / Description**:
Quake 2 server 3.13 on Linux does not properly check file permissions for the config.cfg configuration file, which allows local users to read arbitrary files via a symlink from config.cfg to the target file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/8590.

---

#### 20. CVE-1999-0330

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux bdash game has a buffer overflow that allows local users to gain root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://marc.info/?l=bugtraq&m=87602558319119&w=2.

---

#### 21. CVE-1999-1407

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
ifdhcpc-done script for configuring DHCP on Red Hat Linux 5 allows local users to append text to arbitrary files via a symlink attack on the dhcplog file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=88950856416985&w=2.

---

#### 22. CVE-1999-1498

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
Slackware Linux 3.4 pkgtool allows local attacker to read and write to arbitrary files via a symlink attack on the reply file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/82.

---

#### 23. CVE-1999-1442

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Bug in AMD K6 processor on Linux 2.0.x and 2.1.x kernels allows local users to cause a denial of service (crash) via a particular sequence of instructions, possibly related to accessing addresses outside of segments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://uwsg.iu.edu/hypermail/linux/kernel/9805.3/0855.html.

---

#### 24. CVE-1999-1441

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux 2.0.34 does not properly prevent users from sending SIGIO signals to arbitrary processes, which allows local users to cause a denial of service by sending SIGIO to processes that do not catch it.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221103126047&w=2.

---

#### 25. CVE-1999-1434

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
login in Slackware Linux 3.2 through 3.5 does not properly check for an error when the /etc/group file is missing, which prevents it from dropping privileges, causing it to assign root privileges to any local user who logs on to the server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221104525951&w=2.

---

#### 26. CVE-1999-1406

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
dumpreg in Red Hat Linux 5.1 opens /dev/mem with O_RDWR access, which allows local users to cause a denial of service (crash) by redirecting fd 1 (stdout) to the kernel.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221104526185&w=2.

---

#### 27. CVE-1999-0262

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: renaud_deraison:faxsurvey

**漏洞描述 / Description**:
Hylafax faxsurvey CGI script on Linux allows remote attackers to execute arbitrary commands via shell metacharacters in the query string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2056.

---

#### 28. CVE-1999-1381

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: dbadmin:dbadmin

**漏洞描述 / Description**:
Buffer overflow in dbadmin CGI program 1.0.1 on Linux allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90786656409618&w=2.

---

#### 29. CVE-1999-0002

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: caldera:openlinux, bsdi:bsd_os, redhat:linux

**漏洞描述 / Description**:
Buffer overflow in NFS mountd gives root access to remote attackers, mostly in Linux systems.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/19981006-01-I.

---

#### 30. CVE-1999-0342

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: pam:pam

**漏洞描述 / Description**:
Linux PAM modules allow local users to gain root access using temporary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0342.

---

#### 31. CVE-1999-0798

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sco:internet_faststart, openbsd:openbsd, bsdi:bsd_os, freebsd:freebsd, sco:unixware

**漏洞描述 / Description**:
Buffer overflow in bootpd on OpenBSD, FreeBSD, and Linux systems via a malformed header type.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91278867118128&w=2.

---

#### 32. CVE-1999-1173

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: corel:wordperfect

**漏洞描述 / Description**:
Corel Word Perfect 8 for Linux creates a temporary working directory with world-writable permissions, which allows local users to (1) modify Word Perfect behavior by modifying files in the working directory, or (2) modify files of other users via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91404045014047&w=2.

---

#### 33. CVE-1999-1285

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux 2.1.132 and earlier allows local users to cause a denial of service (resource exhaustion) by reading a large buffer from a random device (e.g. /dev/urandom), which cannot be interrupted until the read has completed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91495921611500&w=2.

---

#### 34. CVE-1999-0243

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Linux cfingerd could be exploited to gain root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.geocrawler.com/archives/3/92/1996/9/0/2217716/.

---

#### 35. CVE-1999-0398

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: ssh:ssh2, ssh:ssh

**漏洞描述 / Description**:
In some instances of SSH 1.2.27 and 2.0.11 on Linux systems, SSH will allow users with expired accounts to login.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0398.

---

#### 36. CVE-1999-0401

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
A race condition in Linux 2.2.1 allows local users to read arbitrary memory from /proc files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0401.

---

#### 37. CVE-1999-0698

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Denial of service in IP protocol logger (ippl) on Red Hat and Debian Linux.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0698.

---

#### 38. CVE-1999-0389

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in the bootp server in the Debian Linux netstd package.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/324.

---

#### 39. CVE-1999-0390

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: suse:suse_linux, redhat:linux

**漏洞描述 / Description**:
Buffer overflow in Dosemu Slang library in Linux.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-006.1.txt.

---

#### 40. CVE-1999-0457

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Linux ftpwatch program allows local users to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/317.

---

#### 41. CVE-1999-0451

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Denial of service in Linux 2.0.36 allows local users to prevent any server from listening on any non-privileged port.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/343.

---

#### 42. CVE-1999-0400

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Denial of service in Linux 2.2.0 running the ldd command on a core file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/344.

---

#### 43. CVE-1999-0461

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sgi:irix, linux:linux_kernel

**漏洞描述 / Description**:
Versions of rpcbind including Linux, IRIX, and Wietse Venema's rpcbind allow a remote attacker to insert and delete entries by spoofing a source address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0461.

---

#### 44. CVE-2000-0370

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: caldera:openlinux

**漏洞描述 / Description**:
The debug option in Caldera Linux smail allows remote attackers to execute commands via shell metacharacters in the -D option for the rmail command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-001.0.txt.

---

#### 45. CVE-1999-0403

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cyrix:linux

**漏洞描述 / Description**:
A bug in Cyrix CPUs on Linux allows local users to perform a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91821080015725&w=2.

---

#### 46. CVE-1999-0459

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Local users can perform a denial of service in Alpha Linux, using MILO to force a reboot.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0459.

---

#### 47. CVE-1999-1495

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
xtvscreen in SuSE Linux 6.0 allows local users to overwrite arbitrary files via a symlink attack on the pic000.pnm file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12580.

---

#### 48. CVE-1999-0460

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Buffer overflow in Linux autofs module through long directory names allows local users to perform a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/312.

---

#### 49. CVE-1999-1168

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: iss:internet_security_scanner

**漏洞描述 / Description**:
install.iss installation script for Internet Security Scanner (ISS) for Linux, version 5.3, allows local users to change the permissions of arbitrary files via a symlink attack on a temporary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12640.

---

#### 50. CVE-1999-0414

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
In Linux before version 2.0.36, remote attackers can spoof a TCP connection and pass data to the application layer before fully establishing the connection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0414.

---

#### 51. CVE-1999-0426

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
The default permissions of /dev/kmem in Linux versions before 2.0.36 allows IP spoofing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0426.

---

#### 52. CVE-1999-0431

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux 2.2.3 and earlier allow a remote attacker to perform an IP fragmentation attack, causing a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0431.

---

#### 53. CVE-1999-0409

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in gnuplot in Linux version 3.5 allows local users to obtain root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/319.

---

#### 54. CVE-1999-0421

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: slackware:slackware_linux

**漏洞描述 / Description**:
During a reboot after an installation of Linux Slackware 3.6, a remote attacker can obtain root access by logging in to the root account without a password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/981.

---

#### 55. CVE-1999-0462

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
suidperl in Linux Perl does not check the nosuid mount option on file systems, allowing local users to gain root access by placing a setuid script in a mountable file system, e.g. a CD-ROM or floppy disk.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/339.

---

#### 56. CVE-1999-0804

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux, linux:linux_kernel, redhat:linux, suse:suse_linux

**漏洞描述 / Description**:
Denial of service in Linux 2.2.x kernels via malformed ICMP packets containing unusual types, codes, and IP header lengths.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/302.

---

#### 57. CVE-2000-0364

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
screen and rxvt in Red Hat Linux 6.0 do not properly set the modes of tty devices, which allows local users to write to other ttys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92877527701347&w=2.

---

#### 58. CVE-2000-0365

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Red Hat Linux 6.0 installs the /dev/pts file system with insecure modes, which allows local users to write to other tty devices.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92877527701347&w=2.

---

#### 59. CVE-1999-1496

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux, redhat:linux, todd_miller:sudo

**漏洞描述 / Description**:
Sudo 1.5 in Debian Linux 2.1 and Red Hat 6.0 allows local users to determine the existence of arbitrary files by attempting to execute the target filename as a program, which generates a different error message when the file does not exist.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/14665.

---

#### 60. CVE-2000-0118

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, sun:solaris, sun:sunos

**漏洞描述 / Description**:
The Red Hat Linux su program does not log failed password guesses if the su process is killed before it times out, which allows local attackers to conduct brute force password guessing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94935300520617&w=2.

---

#### 61. CVE-1999-0733

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: vmware:workstation

**漏洞描述 / Description**:
Buffer overflow in VMWare 1.0.1 for Linux via a long HOME environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/490.

---

#### 62. CVE-1999-1348

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Linuxconf on Red Hat Linux 6.0 and earlier does not properly disable PAM-based access to the shutdown command, which could allow local users to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93220073515880&w=2.

---

#### 63. CVE-1999-1166

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux 2.0.37 does not properly encode the Custom segment limit, which allows local users to gain root privileges by accessing and modifying kernel memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/18156.

---

#### 64. CVE-1999-0710

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The Squid package in Red Hat Linux 5.2 and 6.0, and other distributions, installs cachemgr.cgi in a public web directory, which allows remote attackers to use it as an intermediary to connect to other systems.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://fedoranews.org/updates/FEDORA--.shtml.

---

#### 65. CVE-1999-1018

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
IPChains in Linux kernels 2.2.10 and earlier does not reassemble IP fragments before checking the header information, which allows a remote attacker to bypass the filtering rules using several fragments with 0 offsets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93312523904591&w=2.

---

#### 66. CVE-1999-0746

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: suse:suse_linux, slackware:slackware_linux

**漏洞描述 / Description**:
A default configuration of in.identd in SuSE Linux waits 120 seconds between requests, allowing a remote attacker to conduct a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/587.

---

#### 67. CVE-1999-0740

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Remote attackers can cause a denial of service on Linux in.telnetd telnet daemon through a malformed TERM environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/594.

---

#### 68. CVE-2000-0374

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: caldera:openlinux

**漏洞描述 / Description**:
The default configuration of kdm in Caldera and Mandrake Linux, and possibly other distributions, allows XDMCP connections from any host, which allows remote attackers to obtain sensitive information or bypass additional access restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-021.0.txt.

---

#### 69. CVE-1999-0720

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The pt_chown command in Linux allows local users to modify TTY terminal devices that belong to other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/597.

---

#### 70. CVE-1999-0769

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux, redhat:linux, caldera:openlinux, paul_vixie:vixie_cron

**漏洞描述 / Description**:
Vixie Cron on Linux systems allows local users to set parameters of sendmail commands via the MAILTO environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/611.

---

#### 71. CVE-1999-0704

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: redhat:linux, freebsd:freebsd, bsdi:bsd_os

**漏洞描述 / Description**:
Buffer overflow in Berkeley automounter daemon (amd) logging facility provided in the Linux am-utils package and others.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/614.

---

#### 72. CVE-1999-1352

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
mknod in Linux 2.2 follows symbolic links, which could allow local users to overwrite files or gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93855134409747&w=2.

---

#### 73. CVE-1999-1346

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
PAM configuration file for rlogin in Red Hat Linux 6.1 and earlier includes a less restrictive rule before a more restrictive one, which allows users to access the host via rlogin even if rlogin has been explicitly disabled using the /etc/nologin file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93942774609925&w=2.

---

#### 74. CVE-1999-1347

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Xsession in Red Hat Linux 6.1 and earlier can allow local users with restricted accounts to bypass execution of the .xsession file by starting kde, gnome or anotherlevel from kdm.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93942774609925&w=2.

---

#### 75. CVE-2000-0369

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: caldera:openlinux

**漏洞描述 / Description**:
The IDENT server in Caldera Linux 2.3 creates multiple threads for each IDENT request, which allows remote attackers to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-029.1.txt.

---

#### 76. CVE-2000-0356

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Pluggable Authentication Modules (PAM) in Red Hat Linux 6.1 does not properly lock access to disabled NIS accounts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/697.

---

#### 77. CVE-1999-1341

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel before 2.3.18 or 2.2.13pre15, with SLIP and PPP options, allows local unprivileged users to forge IP packets via the TIOCSETD option on tty devices.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94061108411308&w=2.

---

#### 78. CVE-2000-0362

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Buffer overflows in Linux cdwtools 093 and earlier allows local users to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.novell.com/linux/security/advisories/suse_security_announce_25.html.

---

#### 79. CVE-2000-0363

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Linux cdwtools 093 and earlier allows local users to gain root privileges via the /tmp directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.novell.com/linux/security/advisories/suse_security_announce_25.html.

---

#### 80. CVE-1999-0832

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: debian:debian_linux, redhat:linux

**漏洞描述 / Description**:
Buffer overflow in NFS server on Linux allows attackers to execute commands via a long pathname.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-1999-033.0.txt.

---

#### 81. CVE-1999-0831

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux, suse:suse_linux, sun:cobalt_raq_2, sun:cobalt_raq_3i, cobalt:qube

**漏洞描述 / Description**:
Denial of service in Linux syslogd via a large number of connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-1999-035.0.txt.

---

#### 82. CVE-2000-0531

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux, caldera:openlinux_eserver, caldera:openlinux

**漏洞描述 / Description**:
Linux gpm program allows local users to cause a denial of service by flooding the /dev/gpmctl device with STREAM sockets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0409.html.

---

#### 83. CVE-1999-0317

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Buffer overflow in Linux su command gives root access to local users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0317.

---

#### 84. CVE-2000-0357

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
ORBit and esound in Red Hat Linux 6.1 do not use sufficiently random numbers, which allows local users to guess the authentication keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/corp/support/errata/RHSA1999058-01.html.

---

#### 85. CVE-2000-0358

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
ORBit and gnome-session in Red Hat Linux 6.1 allows remote attackers to crash a program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/corp/support/errata/RHSA1999058-01.html.

---

#### 86. CVE-1999-0986

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux, linux:linux_kernel, redhat:linux

**漏洞描述 / Description**:
The ping command in Linux 2.0.3x allows local users to cause a denial of service by sending large packets with the -R (record route) option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/870.

---

#### 87. CVE-2000-0017

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Buffer overflow in Linux linuxconf package allows remote attackers to gain root privileges via a long parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://marc.info/?l=bugtraq&m=94580196627059&w=2.

---

#### 88. CVE-1999-1327

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Buffer overflow in linuxconf 1.11r11-rh2 on Red Hat Linux 5.1 allows local users to gain root privileges via a long LANG environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221103125826&w=2.

---

#### 89. CVE-1999-1328

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
linuxconf before 1.11.r11-rh3 on Red Hat Linux 5.1 allows local users to overwrite arbitrary files and gain root access via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90383955231511&w=2.

---

#### 90. CVE-1999-1329

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Buffer overflow in SysVInit in Red Hat Linux 5.1 and earlier allows local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7250.php.

---

#### 91. CVE-1999-1331

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
netcfg 2.16-1 in Red Hat Linux 4.2 allows the Ethernet interface to be controlled by users on reboot when an option is set, which allows local users to cause a denial of service by shutting down the interface.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7245.php.

---

#### 92. CVE-1999-1332

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
gzexe in the gzip package on Red Hat Linux 5.0 and earlier allows local users to overwrite files of other users via a symlink attack on a temporary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=88603844115233&w=2.

---

#### 93. CVE-1999-1333

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
automatic download option in ncftp 2.4.2 FTP client in Red Hat Linux 5.0 and earlier allows remote attackers to execute arbitrary commands via shell metacharacters in the names of files that are to be downloaded.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89042322924057&w=2.

---

#### 94. CVE-1999-1335

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
snmpd server in cmu-snmp SNMP package before 3.3-1 in Red Hat Linux 4.0 is configured to allow remote attackers to read and write sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/rh40-errata-general.html#cmu-snmp.

---

#### 95. CVE-1999-1339

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: freebsd:freebsd, linux:linux_kernel

**漏洞描述 / Description**:
Vulnerability when Network Address Translation (NAT) is enabled in Linux 2.2.10 and earlier with ipchains, or FreeBSD 3.2 with ipfw, allows remote attackers to cause a denial of service (kernel panic) via a ping -R (record route) command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93277426802802&w=2.

---

#### 96. CVE-1999-0894

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Red Hat Linux screen program does not use Unix98 ptys, allowing local users to write to other terminals.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0894.

---

#### 97. CVE-2000-1220

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux, sgi:irix

**漏洞描述 / Description**:
The line printer daemon (lpd) in the lpr package in multiple Linux operating systems allows local users to gain root privileges by causing sendmail to execute with arbitrary command line arguments, as demonstrated using the -C option to specify a configuration file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/20021104-01-P.

---

#### 98. CVE-2000-1221

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: debian:debian_linux, redhat:linux, sgi:irix

**漏洞描述 / Description**:
The line printer daemon (lpd) in the lpr package in multiple Linux operating systems authenticates by comparing the reverse-resolved hostname of the local machine to the hostname of the print server as returned by gethostname, which allows remote attackers to bypass intended access controls by modifying the DNS for the attacking IP.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/20021104-01-P.

---

#### 99. CVE-2000-0048

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: corel:linux

**漏洞描述 / Description**:
get_it program in Corel Linux Update allows local users to gain root access by specifying an alternate PATH for the cp program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://linux.corel.com/support/clos_patch1.htm.

---

#### 100. CVE-2000-0107

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Linux apcd program allows local attackers to modify arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2000/20000201.

---

#### 101. CVE-2000-0218

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: caldera:openlinux, suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in Linux mount and umount allows local users to gain root privileges via a long relative pathname.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-002.0.txt.

---

#### 102. CVE-2000-0194

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: corel:linux

**漏洞描述 / Description**:
buildxconf in Corel Linux allows local users to modify or create arbitrary files via the -x or -f parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html.

---

#### 103. CVE-2000-0195

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: corel:linux

**漏洞描述 / Description**:
setxconf in Corel Linux allows local users to gain root access via the -T parameter, which executes the user's .xserverrc file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-02/0323.html.

---

#### 104. CVE-2000-0170

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, turbolinux:turbolinux

**漏洞描述 / Description**:
Buffer overflow in the man program in Linux allows local users to gain privileges via the MANPAGER environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1011.

---

#### 105. CVE-2000-0186

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, redhat:linux, freebsd:freebsd, turbolinux:turbolinux

**漏洞描述 / Description**:
Buffer overflow in the dump utility in the Linux ext2fs backup package allows local users to gain privileges via a long command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-100.html.

---

#### 106. CVE-2000-0196

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: nmh:nmh, redhat:linux, turbolinux:turbolinux

**漏洞描述 / Description**:
Buffer overflow in mhshow in the Linux nmh package allows remote attackers to execute commands via malformed MIME headers in an email message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-006.html.

---

#### 107. CVE-2000-0193

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: corel:linux

**漏洞描述 / Description**:
The default configuration of Dosemu in Corel Linux 1.0 allows local users to execute the system.com program and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1030.

---

#### 108. CVE-2000-0206

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: oracle:oracle8i

**漏洞描述 / Description**:
The installation of Oracle 8.1.5.x on Linux follows symlinks and creates the orainstRoot.sh file with world-writeable permissions, which allows local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0023.html.

---

#### 109. CVE-2000-0184

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, redhat:linux

**漏洞描述 / Description**:
Linux printtool sets the permissions of printer configuration files to be world-readable, which allows local attackers to obtain printer share passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0082.html.

---

#### 110. CVE-2000-0171

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: at_computing:atsar_linux

**漏洞描述 / Description**:
atsadc in the atsar package for Linux does not properly check the permissions of an output file, which allows local users to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0102.html.

---

#### 111. CVE-2000-0233

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: suse:suse_linux_imap_server

**漏洞描述 / Description**:
SuSE Linux IMAP server allows remote attackers to bypass IMAP authentication and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vendor/2000-q1/0035.html.

---

#### 112. CVE-2000-0231

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: halloween:halloween_linux, suse:suse_linux

**漏洞描述 / Description**:
Linux kreatecd trusts a user-supplied path that is used to find the cdrecord program, allowing local users to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0162.html.

---

#### 113. CVE-2000-0227

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The Linux 2.2.x kernel does not restrict the number of Unix domain sockets as defined by the wmem_max parameter, which allows local users to cause a denial of service by requesting a large number of sockets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0254.html.

---

#### 114. CVE-2000-0289

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel, debian:debian_linux, redhat:linux

**漏洞描述 / Description**:
IP masquerading in Linux 2.2.x allows remote attackers to route UDP packets through the internal interface by modifying the external source IP address and port number to match those of an established connection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0284.html.

---

#### 115. CVE-2000-0274

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: bray_systems:linux_trustees

**漏洞描述 / Description**:
The Linux trustees kernel patch allows attackers to cause a denial of service by accessing a file or directory with a long name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-04/0035.html.

---

#### 116. CVE-2000-0263

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The X font server xfs in Red Hat Linux 6.x allows an attacker to cause a denial of service via a malformed request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-04/0079.html.

---

#### 117. CVE-2000-0336

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, redhat:linux, openldap:openldap, turbolinux:turbolinux

**漏洞描述 / Description**:
Linux OpenLDAP server allows local users to modify arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.calderasystems.com/pub/OpenLinux/security/CSSA-2000-009.0.txt.

---

#### 118. CVE-2000-0248

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The web GUI for the Linux Virtual Server (LVS) software in the Red Hat Linux Piranha package has a backdoor password that allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://xforce.iss.net/alerts/advise46.php3.

---

#### 119. CVE-1999-0706

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux, isc:inn

**漏洞描述 / Description**:
Linux xmonisdn package allows local users to gain root privileges by modifying the IFS or PATH environmental variables.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/583.

---

#### 120. CVE-2000-0340

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in Gnomelib in SuSE Linux 6.3 allows local users to execute arbitrary commands via the DISPLAY environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1155.

---

#### 121. CVE-2000-0344

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The knfsd NFS server in Linux kernel 2.2.x allows remote attackers to cause a denial of service via a negative size value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1160.

---

#### 122. CVE-2000-0293

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
aaa_base in SuSE Linux 6.3, and cron.daily in earlier versions, allow local users to delete arbitrary files by creating files whose names include spaces, which are then incorrectly interpreted by aaa_base when it deletes expired files from the /tmp directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1130.

---

#### 123. CVE-2000-0378

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The pam_console PAM module in Linux systems performs a chown on various devices upon a user login, but an open file descriptor for those devices can be maintained after the user logs out, which allows that user to sniff activity on these devices when subsequent users log in.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-05/0023.html.

---

#### 124. CVE-2000-0438

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: slackware:slackware_linux, caldera:openlinux, turbolinux:turbolinux, suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in fdmount on Linux systems allows local users in the "floppy" group to execute arbitrary commands via a long mountpoint parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-05/0245.html.

---

#### 125. CVE-2000-0460

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: kde:kde

**漏洞描述 / Description**:
Buffer overflow in KDE kdesud on Linux allows local uses to gain privileges via a long DISPLAY environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-05/0353.html.

---

#### 126. CVE-2000-0454

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Buffer overflow in Linux cdrecord allows local users to gain privileges via the dev parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-05/0367.html.

---

#### 127. CVE-2000-0467

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: sam_lantinga:splitvt

**漏洞描述 / Description**:
Buffer overflow in Linux splitvt 1.6.3 and earlier allows local users to gain root privileges via a long password in the screen locking function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0125.html.

---

#### 128. CVE-2000-0506

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The "capabilities" feature in Linux before 2.2.16 allows local users to cause a denial of service or gain privileges by setting the capabilities to prevent a setuid program from dropping privileges, aka the "Linux kernel setuid/setcap vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://sgigate.sgi.com/security/20000802-01-P.

---

#### 129. CVE-2000-0602

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: kevin_lindsay:secure_locate

**漏洞描述 / Description**:
Secure Locate (slocate) in Red Hat Linux allows local users to gain privileges via a malformed configuration file that is specified in the LOCATE_PATH environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1385.

---

#### 130. CVE-2000-0604

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
gkermit in Red Hat Linux is improperly installed with setgid uucp, which allows local users to modify files owned by uucp.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1383.

---

#### 131. CVE-2000-0606

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, debian:debian_linux, redhat:linux

**漏洞描述 / Description**:
Buffer overflow in kon program in Kanji on Console (KON) package on Linux may allow local users to gain root privileges via a long -StartupMessage parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1371.

---

#### 132. CVE-2000-0607

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, debian:debian_linux, redhat:linux

**漏洞描述 / Description**:
Buffer overflow in fld program in Kanji on Console (KON) package on Linux may allow local users to gain root privileges via an input file containing long CHARSET_REGISTRY or CHARSET_ENCODING settings.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1371.

---

#### 133. CVE-2000-0617

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: stanley_t._shebs:xconq

**漏洞描述 / Description**:
Buffer overflow in xconq and cconq game programs on Red Hat Linux allows local users to gain additional privileges via long USER environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html.

---

#### 134. CVE-2000-0618

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: stanley_t._shebs:xconq

**漏洞描述 / Description**:
Buffer overflow in xconq and cconq game programs on Red Hat Linux allows local users to gain additional privileges via long DISPLAY environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0222.html.

---

#### 135. CVE-2000-0566

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, redhat:linux, caldera:openlinux

**漏洞描述 / Description**:
makewhatis in Linux man package allows local users to overwrite files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-021.0.txt.

---

#### 136. CVE-2000-0614

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Tnef program in Linux systems allows remote attackers to overwrite arbitrary files via TNEF encoded compressed attachments which specify absolute path names for the decompressed output.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vendor/2000-q3/0002.html.

---

#### 137. CVE-2000-0666

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux, trustix:secure_linux, suse:suse_linux, conectiva:linux, debian:debian_linux

**漏洞描述 / Description**:
rpc.statd in the nfs-utils package in various Linux distributions does not properly cleanse untrusted format strings, which allows remote attackers to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0206.html.

---

#### 138. CVE-2000-0633

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, redhat:linux, conectiva:linux

**漏洞描述 / Description**:
Vulnerability in Mandrake Linux usermode package allows local users to to reboot or halt the system.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0251.html.

---

#### 139. CVE-2000-0667

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: conectiva:linux

**漏洞描述 / Description**:
Vulnerability in gpm in Caldera Linux allows local users to delete arbitrary files or conduct a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0273.html.

---

#### 140. CVE-2000-0668

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: michael_k._johnson:pam_console, redhat:linux, conectiva:linux

**漏洞描述 / Description**:
pam_console PAM module in Linux systems allows a user to access the system console and reboot the system when a display manager such as gdm or kdm has XDMCP enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0398.html.

---

#### 141. CVE-2000-0545

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: sgi:mailx

**漏洞描述 / Description**:
Buffer overflow in mailx mail command (aka Mail) on Linux systems allows local users to gain privileges via a long -c (carbon copy) parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-05/0435.html.

---

#### 142. CVE-2000-0354

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: lee_mcloughlin:mirror

**漏洞描述 / Description**:
mirror 2.8.x in Linux systems allows remote attackers to create files one level above the local target directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/1999/19991018.

---

#### 143. CVE-2000-1207

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
userhelper in the usermode package on Red Hat Linux executes non-setuid programs as root, which does not activate the security measures in glibc and allows the programs to be exploited via format string vulnerabilities in glibc via the LANG or LC_ALL environment variables (CVE-2000-0844).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97034397026473&w=2.

---

#### 144. CVE-2000-0816

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Linux tmpwatch --fuser option allows local users to execute arbitrary commands by creating files whose names contain shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/MDKSA-2000-056.php3?dis=7.1.

---

#### 145. CVE-2000-1213

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux, iputils:iputils, immunix:immunix

**漏洞描述 / Description**:
ping in iputils before 20001010, as distributed on Red Hat Linux 6.2 through 7J and other operating systems, does not drop privileges after acquiring a raw socket, which increases ping's exposure to bugs that otherwise would occur at lower privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-10/0429.html.

---

#### 146. CVE-2000-1214

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux, iputils:iputils, immunix:immunix

**漏洞描述 / Description**:
Buffer overflows in the (1) outpack or (2) buf variables of ping in iputils before 20001010, as distributed on Red Hat Linux 6.2 through 7J and other operating systems, may allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-10/0429.html.

---

#### 147. CVE-2000-0031

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The initscripts package in Red Hat Linux allows local users to gain privileges via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0031.

---

#### 148. CVE-2000-0698

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: minicom:minicom

**漏洞描述 / Description**:
Minicom 1.82.1 and earlier on some Linux systems allows local users to create arbitrary files owned by the uucp user via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/77361.

---

#### 149. CVE-2000-0712

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: lids:lids

**漏洞描述 / Description**:
Linux Intrusion Detection System (LIDS) 0.9.7 allows local users to gain root privileges when LIDS is disabled via the security=0 boot option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0486.html.

---

#### 150. CVE-2000-0714

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: university_of_massachusetts:scheme

**漏洞描述 / Description**:
umb-scheme 3.2-11 for Red Hat Linux is installed with world-writeable files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-047.html.

---

#### 151. CVE-2000-0715

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: conectiva:linux, kirk_bauer:diskcheck

**漏洞描述 / Description**:
DiskCheck script diskcheck.pl in Red Hat Linux 6.2 allows local users to create or overwrite arbitrary files via a symlink attack on a temporary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://seclists.org/bugtraq/2000/Aug/0082.html.

---

#### 152. CVE-2000-0747

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: conectiva:linux

**漏洞描述 / Description**:
The logrotate script for OpenLDAP before 1.2.11 in Conectiva Linux sends an improper signal to the kernel log daemon (klogd) and kills it.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-07/0379.html.

---

#### 153. CVE-2000-0749

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: freebsd:freebsd

**漏洞描述 / Description**:
Buffer overflow in the Linux binary compatibility module in FreeBSD 3.x through 5.x allows local users to gain root privileges via long filenames in the linux shadow file system.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/freebsd/2000-08/0338.html.

---

#### 154. CVE-2000-0800

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
String parsing error in rpc.kstatd in the linuxnfs or knfsd packages in SuSE and possibly other Linux systems allows remote attackers to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.novell.com/linux/security/advisories/suse_security_announce_58.html.

---

#### 155. CVE-2000-0829

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:tmpwatch, redhat:linux

**漏洞描述 / Description**:
The tmpwatch utility in Red Hat Linux forks a new process for each directory level, which allows local users to cause a denial of service by creating deeply nested directories in /tmp or /var/tmp/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-080.html.

---

#### 156. CVE-2000-0866

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: borland_software:interbase_superserver

**漏洞描述 / Description**:
Interbase 6 SuperServer for Linux allows an attacker to cause a denial of service via a query containing 0 bytes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-09/0027.html.

---

#### 157. CVE-2000-0867

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, debian:debian_linux, trustix:secure_linux, slackware:slackware_linux, mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Kernel logging daemon (klogd) in Linux does not properly cleanse user-injected format strings, which allows local users to gain root privileges by triggering malformed kernel messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2000-032.0.txt.

---

#### 158. CVE-2000-0868

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server, suse:suse_linux

**漏洞描述 / Description**:
The default configuration of Apache 1.3.12 in SuSE Linux 6.4 allows remote attackers to read source code for CGI scripts by replacing the /cgi-bin/ in the requested URL with /cgi-bin-sdb/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html.

---

#### 159. CVE-2000-0869

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server, suse:suse_linux

**漏洞描述 / Description**:
The default configuration of Apache 1.3.12 in SuSE Linux 6.4 enables WebDAV, which allows remote attackers to list arbitrary directories via the PROPFIND HTTP request method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/linux/suse/2000-q3/0906.html.

---

#### 160. CVE-2000-0883

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
The default configuration of mod_perl for Apache as installed on Mandrake Linux 6.1 through 7.1 sets the /perl/ directory to be browseable, which allows remote attackers to list the contents of that directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-09/0111.html.

---

#### 161. CVE-2000-1009

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, trustix:secure_linux

**漏洞描述 / Description**:
dump in Red Hat Linux 6.2 trusts the pathname specified by the RSH environmental variable, which allows local users to obtain root privileges by modifying the RSH variable to point to a Trojan horse program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-10/0438.html.

---

#### 162. CVE-2000-1042

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Buffer overflow in ypserv in Mandrake Linux 7.1 and earlier, and possibly other Linux operating systems, allows an attacker to gain root privileges when ypserv is built without a vsyslog() function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1.

---

#### 163. CVE-2000-1043

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Format string vulnerability in ypserv in Mandrake Linux 7.1 and earlier, and possibly other Linux operating systems, allows an attacker to gain root privileges when ypserv is built without a vsyslog() function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/MDKSA-2000-064.php3?dis=7.1.

---

#### 164. CVE-2000-1044

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Format string vulnerability in ypbind-mt in SuSE SuSE-6.2, and possibly other Linux operating systems, allows an attacker to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/linux/suse/2000-q4/0262.html.

---

#### 165. CVE-2000-1059

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
The default configuration of the Xsession file in Mandrake Linux 7.1 and 7.0 bypasses the Xauthority access control mechanism with an "xhost + localhost" command, which allows local users to sniff X Windows events and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/MDKSA-2000-052.php3.

---

#### 166. CVE-2000-0934

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Glint in Red Hat Linux 5.2 allows local users to overwrite arbitrary files and cause a denial of service via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-062.html.

---

#### 167. CVE-2000-0956

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: carnegie_mellon_university:cyrus-sasl

**漏洞描述 / Description**:
cyrus-sasl before 1.5.24 in Red Hat Linux 7.0 does not properly verify the authorization for a local user, which could allow the users to bypass specified access restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-094.html.

---

#### 168. CVE-2000-1095

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, conectiva:linux, suse:suse_linux, mandrakesoft:mandrake_linux, immunix:immunix

**漏洞描述 / Description**:
modprobe in the modutils 2.3.x package on Linux systems allows a local user to execute arbitrary commands via shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-11/0179.html.

---

#### 169. CVE-2000-1107

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
in.identd ident server in SuSE Linux 6.x and 7.0 allows remote attackers to cause a denial of service via a long request, which causes the server to access a NULL pointer and crash.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-11/0387.html.

---

#### 170. CVE-2000-1125

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
restore 0.4b15 and earlier in Red Hat Linux 6.2 trusts the pathname specified by the RSH environmental variable, which allows local users to obtain root privileges by modifying the RSH variable to point to a Trojan horse program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97336034309944&w=2.

---

#### 171. CVE-2000-1136

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: debian:elvis_tiny

**漏洞描述 / Description**:
elvis-tiny before 1.4-10 in Debian GNU/Linux, and possibly other Linux operating systems, allows local users to overwrite files of other users via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97502995616099&w=2.

---

#### 172. CVE-2000-1183

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: nec:socks_5

**漏洞描述 / Description**:
Buffer overflow in socks5 server on Linux allows attackers to execute arbitrary commands via a long connection request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-11/0219.html.

---

#### 173. CVE-2000-1189

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Buffer overflow in pam_localuser PAM module in Red Hat Linux 7.x and 6.x allows attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000358.

---

#### 174. CVE-2001-0073

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: nsa:security-enhanced_linux

**漏洞描述 / Description**:
Buffer overflow in the find_default_type function in libsecure in NSA Security-enhanced Linux, which may allow attackers to modify critical data in memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/153188.

---

#### 175. CVE-2001-1273

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The "mxcsr P4" vulnerability in the Linux kernel before 2.2.17-14, when running on certain Intel CPUs, allows local users to cause a denial of service (system halt).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-045.shtml.

---

#### 176. CVE-2000-0314

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux, debian:debian_linux, slackware:slackware_linux, netbsd:netbsd, digital:unix

**漏洞描述 / Description**:
traceroute in NetBSD 1.3.3 and Linux systems allows local users to flood other systems by providing traceroute with a large waittime (-w) option, which is not parsed properly and sets the time delay for sending packets to zero.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc.

---

#### 177. CVE-2000-0315

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux, debian:debian_linux, slackware:slackware_linux, netbsd:netbsd, digital:unix

**漏洞描述 / Description**:
traceroute in NetBSD 1.3.3 and Linux systems allows local unprivileged users to modify the source address of the packets, which could be used in spoofing attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.NetBSD.ORG/pub/NetBSD/misc/security/advisories/NetBSD-SA1999-004.txt.asc.

---

#### 178. CVE-2001-0107

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: symantec_veritas:backup

**漏洞描述 / Description**:
Veritas Backup agent on Linux allows remote attackers to cause a denial of service by establishing a connection without sending any data, which causes the process to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97958921407182&w=2.

---

#### 179. CVE-2001-0143

**严重程度 / Severity**: N/A | CVSS: 1.2
**受影响产品 / Affected Products**: redhat:linux, immunix:immunix

**漏洞描述 / Description**:
vpop3d program in linuxconf 1.23r and earlier allows local users to overwrite arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97916374410647&w=2.

---

#### 180. CVE-2001-0172

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: hans_reiser:reiserfs, suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in ReiserFS 3.5.28 in SuSE Linux allows local users to cause a denial of service and possibly execute arbitrary commands by via a long directory name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-01/0127.html.

---

#### 181. CVE-2001-0181

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: caldera:openlinux_eserver, caldera:openlinux_desktop, caldera:openlinux_edesktop

**漏洞描述 / Description**:
Format string vulnerability in the error logging code of DHCP server and client in Caldera Linux allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.calderasystems.com/support/security/advisories/CSSA-2001-003.0.txt.

---

#### 182. CVE-2001-1467

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: don_libes:expect

**漏洞描述 / Description**:
mkpasswd in expect 5.2.8, as used by Red Hat Linux 6.2 through 7.0, seeds its random number generator with its process ID, which limits the space of possible seeds and makes it easier for attackers to conduct brute force password attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-04/0173.html.

---

#### 183. CVE-2001-1390

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unknown vulnerability in binfmt_misc in the Linux kernel before 2.2.19, related to user pages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 184. CVE-2001-1391

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Off-by-one vulnerability in CPIA driver of Linux kernel before 2.2.19 allows users to modify kernel memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 185. CVE-2001-1392

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The Linux kernel before 2.2.19 does not have unregister calls for (1) CPUID and (2) MSR drivers, which could cause a DoS (crash) by unloading and reloading the drivers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 186. CVE-2001-1393

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unknown vulnerability in classifier code for Linux kernel before 2.2.19 could result in denial of service (hang).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 187. CVE-2001-1394

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Signedness error in (1) getsockopt and (2) setsockopt for Linux kernel before 2.2.19 allows local users to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 188. CVE-2001-1395

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unknown vulnerability in sockfilter for Linux kernel before 2.2.19 related to "boundary cases," with unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 189. CVE-2001-1396

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unknown vulnerabilities in strnlen_user for Linux kernel before 2.2.19, with unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 190. CVE-2001-1397

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The System V (SYS5) shared memory implementation for Linux kernel before 2.2.19 could allow attackers to modify recently freed memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 191. CVE-2001-1398

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Masquerading code for Linux kernel before 2.2.19 does not fully check packet lengths in certain cases, which may lead to a vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 192. CVE-2001-1399

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Certain operations in Linux kernel before 2.2.19 on the x86 architecture copy the wrong number of bytes, which might allow attackers to modify memory, aka "User access asm bug on x86."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 193. CVE-2001-1400

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unknown vulnerabilities in the UDP port allocation for Linux kernel before 2.2.19 could allow local users to cause a denial of service (deadlock).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98575345009963&w=2.

---

#### 194. CVE-2001-0193

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux, suse:suse_linux

**漏洞描述 / Description**:
Format string vulnerability in man in some Linux distributions allows local users to gain privileges via a malformed -l parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98096782126481&w=2.

---

#### 195. CVE-2001-0229

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: sun:chilisoft

**漏洞描述 / Description**:
Chili!Soft ASP for Linux before 3.6 does not properly set group privileges when running in inherited mode, which could allow attackers to gain privileges via malicious scripts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-02/0112.html.

---

#### 196. CVE-2001-0316

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.4 and 2.2 allows local users to read kernel memory and possibly gain privileges via a negative argument to the sysctl call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-02/0267.html.

---

#### 197. CVE-2001-0317

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Race condition in ptrace in Linux kernel 2.4 and 2.2 allows local users to gain privileges by using ptrace to track and modify a running setuid process.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-02/0267.html.

---

#### 198. CVE-2001-1332

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: easy_software_products:cups

**漏洞描述 / Description**:
Buffer overflows in Linux CUPS before 1.1.6 may allow remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384.

---

#### 199. CVE-2001-1333

**严重程度 / Severity**: N/A | CVSS: 1.2
**受影响产品 / Affected Products**: easy_software_products:cups

**漏洞描述 / Description**:
Linux CUPS before 1.1.6 does not securely handle temporary files, possibly due to a symlink vulnerability that could allow local users to overwrite files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000384.

---

#### 200. CVE-2001-0474

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: brian_paul:mesa, mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Utah-glx in Mesa before 3.3-14 on Mandrake Linux 7.2 allows local users to overwrite arbitrary files via a symlink attack on the /tmp/glxmemory file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-029.php3.

---

#### 201. CVE-2001-0481

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Vulnerability in rpmdrake in Mandrake Linux 8.0 related to insecure temporary file handling.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-043.php3.

---

#### 202. CVE-2001-0405

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
ip_conntrack_ftp in the IPTables firewall for Linux 2.4 allows remote attackers to bypass access restrictions for an FTP server via a PORT command that lists an arbitrary IP address and port number, which is added to the RELATED table and allowed by the firewall.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-04/0271.html.

---

#### 203. CVE-2001-1245

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: opera_software:opera_web_browser

**漏洞描述 / Description**:
Opera 5.0 for Linux does not properly handle malformed HTTP headers, which allows remote attackers to cause a denial of service, possibly with a header whose value is the same as a MIME header name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/196980.

---

#### 204. CVE-2001-1146

**严重程度 / Severity**: N/A | CVSS: 1.2
**受影响产品 / Affected Products**: lee_herron:allcommerce

**漏洞描述 / Description**:
AllCommerce with debugging enabled in EnGarde Secure Linux 1.0.1 creates temporary files with predictable names, which allows local users to modify files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linuxsecurity.com/advisories/other_advisory-1492.html.

---

#### 205. CVE-2001-1240

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: engardelinux:secure_linux

**漏洞描述 / Description**:
The default configuration of sudo in Engarde Secure Linux 1.0.1 allows any user in the admin group to run certain commands that could be leveraged to gain full root access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linuxsecurity.com/advisories/other_advisory-1493.html.

---

#### 206. CVE-2001-0623

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: sendfile:sendfile

**漏洞描述 / Description**:
sendfiled, as included with Simple Asynchronous File Transfer (SAFT), on various Linux systems does not properly drop privileges when sending notification emails, which allows local attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2001/dsa-050.

---

#### 207. CVE-2001-1130

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Sdbsearch.cgi in SuSE Linux 6.0-7.2 could allow remote attackers to execute arbitrary commands by uploading a keylist.txt file that contains filenames with shell metacharacters, then causing the file to be searched using a .. in the HTTP referer (from the HTTP_REFERER variable) to point to the directory that contains the keylist.txt file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.novell.com/linux/security/advisories/2001_027_sdb_txt.html.

---

#### 208. CVE-2001-1119

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: ti_kan:xmcd

**漏洞描述 / Description**:
cda in xmcd 3.0.2 and 2.6 in SuSE Linux allows local users to overwrite arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/105347.

---

#### 209. CVE-2001-0525

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in dsh in dqs 3.2.7 in SuSE Linux 7.0 and earlier, and possibly other operating systems, allows local users to gain privileges via a long first command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-05/0193.html.

---

#### 210. CVE-2001-0635

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Red Hat Linux 7.1 sets insecure permissions on swap files created during installation, which can allow a local attacker to gain additional privileges by reading sensitive information from the swap file, such as passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5564.

---

#### 211. CVE-2001-0632

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:chilisoft

**漏洞描述 / Description**:
Sun Chili!Soft 3.5.2 on Linux and 3.6 on AIX creates a default admin username and password in the default installation, which can allow a remote attacker to gain additional privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-02/0378.html.

---

#### 212. CVE-2000-1195

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: caldera:openlinux_edesktop, caldera:openlinux_eserver

**漏洞描述 / Description**:
telnet daemon (telnetd) from the Linux netkit package before netkit-telnet-0.16 allows remote attackers to bypass authentication when telnetd is running with the -L command line option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.caldera.com/support/security/advisories/CSSA-2000-008.0.txt.

---

#### 213. CVE-2001-1002

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The default configuration of the DVI print filter (dvips) in Red Hat Linux 7.0 and earlier does not run dvips in secure mode when dvips is executed by lpd, which could allow remote attackers to gain privileges by printing a DVI file that contains malicious commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99892644616749&w=2.

---

#### 214. CVE-2001-1069

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: adobe:acrobat_reader

**漏洞描述 / Description**:
libCoolType library as used in Adobe Acrobat (acroread) on Linux creates the AdobeFnt.lst file with world-writable permissions, which allows local users to modify the file and possibly modify acroread's behavior.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.debian.org/debian-security/2001/debian-security-200101/msg00085.html.

---

#### 215. CVE-2001-1013

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Apache on Red Hat Linux with with the UserDir directive enabled generates different error codes when a username exists and there is no public_html directory and when the username does not exist, which could allow remote attackers to determine valid usernames on the server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vuln-dev/2000-q3/0083.html.

---

#### 216. CVE-2001-0641

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux, suse:suse_linux, immunix:immunix

**漏洞描述 / Description**:
Buffer overflow in man program in various distributions of Linux allows local user to execute arbitrary code as group man via a long -S option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-05/0087.html.

---

#### 217. CVE-2001-0738

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: immunix:immunix, debian:debian_linux

**漏洞描述 / Description**:
LogLine function in klogd in sysklogd 1.3 in various Linux distributions allows an attacker to cause a denial of service (hang) by causing null bytes to be placed in log messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://download.immunix.org/ImmunixOS/7.0/updates/IMNX-2001-70-026-01.

---

#### 218. CVE-2001-0739

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: engardelinux:secure_linux

**漏洞描述 / Description**:
Guardian Digital WebTool in EnGarde Secure Linux 1.0.1 allows restarted services to inherit some environmental variables, which could allow local users to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linuxsecurity.com/advisories/other_advisory-1404.html.

---

#### 219. CVE-2001-0763

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: suse:suse_linux, debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in Linux xinetd 2.1.8.9pre11-1 and earlier may allow remote attackers to execute arbitrary code via a long ident response, which is not properly handled by the svc_logprint function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-06/0064.html.

---

#### 220. CVE-2001-0775

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: xli:xli, xloadimage:xloadimage

**漏洞描述 / Description**:
Buffer overflow in xloadimage 4.1 (aka xli 1.16 and 1.17) in Linux allows remote attackers to execute arbitrary code via a FACES format image containing a long (1) Firstname or (2) Lastname field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2001/dsa-069.

---

#### 221. CVE-2001-0787

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
LPRng in Red Hat Linux 7.0 and 7.1 does not properly drop memberships in supplemental groups when lowering privileges, which could allow a local user to elevate privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-096.shtml.

---

#### 222. CVE-2001-0907

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.2.1 through 2.2.19, and 2.4.1 through 2.4.10, allows local users to cause a denial of service via a series of deeply nested symlinks, which causes the kernel to spend extra time when trying to access the link.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2001-036.0.txt.

---

#### 223. CVE-2001-1384

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
ptrace in Linux 2.2.x through 2.2.19, and 2.4.x through 2.4.9, allows local users to gain root privileges by running ptrace on a setuid or setgid program that itself calls an unprivileged program, such as newgrp.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2001-036.0.txt.

---

#### 224. CVE-2001-0914

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: suse:suse_linux, linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel before 2.4.11pre3 in multiple Linux distributions allows local users to cause a denial of service (crash) by starting the core vmlinux kernel, possibly related to poor error checking during ELF loading.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100638584813349&w=2.

---

#### 225. CVE-2001-1449

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux_corporate_server, apache:http_server, mandrakesoft:mandrake_linux, mandrakesoft:mandrake_single_network_firewall

**漏洞描述 / Description**:
The default installation of Apache before 1.3.19 on Mandrake Linux 7.1 through 8.0 and Linux Corporate Server 1.0.1 allows remote attackers to list the directory index of arbitrary web directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/913704.

---

#### 226. CVE-2001-0912

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
Packaging error for expect 8.3.3 in Mandrake Linux 8.1 causes expect to search for its libraries in the /home/snailtalk directory before other directories, which could allow a local user to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-087.php3?dis=8.1.

---

#### 227. CVE-2001-0819

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: fetchmail:fetchmail

**漏洞描述 / Description**:
A buffer overflow in Linux fetchmail before 5.8.6 allows remote attackers to execute arbitrary code via a large 'To:' field in an email header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-01:43.fetchmail.asc.

---

#### 228. CVE-2001-0851

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: suse:suse_linux, linux:linux_kernel, caldera:openlinux_edesktop, caldera:openlinux_server, caldera:openlinux_workstation

**漏洞描述 / Description**:
Linux kernel 2.0, 2.2 and 2.4 with syncookies enabled allows remote attackers to bypass firewall rules by brute force guessing the cookie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000432.

---

#### 229. CVE-2001-0852

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
TUX HTTP server 2.1.0-2 in Red Hat Linux allows remote attackers to cause a denial of service via a long Host: header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100498100112191&w=2.

---

#### 230. CVE-2001-0859

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
2.4.3-12 kernel in Red Hat Linux 7.1 Korean installation program sets the setting default umask for init to 000, which installs files with world-writeable permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/advisories/3725.

---

#### 231. CVE-2001-1190

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux

**漏洞描述 / Description**:
The default PAM files included with passwd in Mandrake Linux 8.1 do not support MD5 passwords, which could result in a lower level of password security than intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7706.php.

---

#### 232. CVE-2001-1506

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: hp:secure_os

**漏洞描述 / Description**:
Unknown vulnerability in the file system protection subsystem in HP Secure OS Software for Linux 1.0 allows additional user privileges on some files beyond what is specified in the file system protection rules, which allows local users to conduct unauthorized operations on restricted files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/advisories/3618.

---

#### 233. CVE-2001-1551

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.2.19 enables CAP_SYS_RESOURCE for setuid processes, which allows local users to exceed disk quota restrictions during execution of setuid programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-10/0179.html.

---

#### 234. CVE-2001-1561

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: john_bovey:xvt, debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in Xvt 2.1 in Debian Linux 2.2 allows local users to execute arbitrary code via long (1) -name and (2) -T arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-07/0024.html.

---

#### 235. CVE-2001-1563

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apache:tomcat, hp:secure_os

**漏洞描述 / Description**:
Unknown vulnerability in Tomcat 3.2.1 running on HP Secure OS for Linux 1.0 allows attackers to access servlet resources.  NOTE: due to the vagueness of the vendor advisory, it is not clear whether this issue is already covered by other CVE identifiers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/hp/2001-q4/0062.html.

---

#### 236. CVE-2001-1572

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The MAC module in Netfilter in Linux kernel 2.4.1 through 2.4.11, when configured to filter based on MAC addresses, allows remote attackers to bypass packet filters via small packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-10/0057.html.

---

#### 237. CVE-2002-0046

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel, and possibly other operating systems, allows remote attackers to read portions of memory via a series of fragmented ICMP packets that generate an ICMP TTL Exceeded response, which includes portions of the memory in the response packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5394.

---

#### 238. CVE-2002-0060

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
IRC connection tracking helper module in the netfilter subsystem for Linux 2.4.18-pre9 and earlier does not properly set the mask for conntrack expectations for incoming DCC connections, which could allow remote attackers to bypass intended firewall restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://frontal2.mandriva.com/security/advisories?name=MDKSA-2002:041.

---

#### 239. CVE-2002-0062

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux, suse:suse_linux, debian:debian_linux, freebsd:freebsd, gnu:ncurses

**漏洞描述 / Description**:
Buffer overflow in ncurses 5.0, and the ncurses4 compatibility package as used in Red Hat Linux, allows local users to gain privileges, related to "routines for moving the physical cursor and scrolling."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2002/dsa-113.

---

#### 240. CVE-2002-0086

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ibm:lotus_domino

**漏洞描述 / Description**:
Buffer overflow in bindsock in Lotus Domino 5.0.4 and 5.0.7 on Linux allows local users to gain root privileges via a long (1) Notes_ExecDirectory or (2) PATH environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www-1.ibm.com/support/docview.wss?uid=swg21095569.

---

#### 241. CVE-2002-0164

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: caldera:openlinux_server, caldera:openlinux_workstation

**漏洞描述 / Description**:
Vulnerability in the MIT-SHM extension of the X server on Linux (XFree86) 4.2.1 and earlier allows local users to read and write arbitrary shared memory, possibly to cause a denial of service or gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/20021001-01-P.

---

#### 242. CVE-2002-0203

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: tarantella:tarantella_enterprise

**漏洞描述 / Description**:
ttawebtop.cgi in Tarantella Enterprise 3.20 on SPARC Solaris and Linux, and 3.1x and 3.0x including 3.11.903, allows remote attackers to view directory contents via an empty pg parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101190195430376&w=2.

---

#### 243. CVE-2002-0169

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: redhat:docbook_utils, redhat:docbook_stylesheets

**漏洞描述 / Description**:
The default stylesheet for DocBook on Red Hat Linux 6.2 through 7.2 is installed with an insecure option enabled, which could allow users to overwrite files outside of the current directory from an untrusted document by using a full pathname as an element identifier.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/advisories/4095.

---

#### 244. CVE-2002-0378

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: astart_technologies:lprng

**漏洞描述 / Description**:
The default configuration of LPRng print spooler in Red Hat Linux 7.0 through 7.3, Mandrake 8.1 and 8.2, and other operating systems, accepts print jobs from arbitrary remote hosts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/advisories/4205.

---

#### 245. CVE-2002-0570

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The encrypted loop device in Linux kernel 2.4.10 and earlier does not authenticate the entity that is encrypting data, which allows local users to modify encrypted data without knowing the key.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-01/0010.html.

---

#### 246. CVE-2002-0429

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The iBCS routines in arch/i386/kernel/traps.c for Linux kernels 2.4.18 and earlier on x86 systems allow local users to kill arbitrary processes via a a binary compatibility interface (lcall).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101561298818888&w=2.

---

#### 247. CVE-2002-0488

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: linux_directory_penguin:linux_directory_penguin_traceroute

**漏洞描述 / Description**:
Linux Directory Penguin traceroute.pl CGI script 1.0 allows remote attackers to execute arbitrary code via shell metacharacters in the host parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8600.php.

---

#### 248. CVE-2002-0489

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: linux_directory_penguin:nslookup

**漏洞描述 / Description**:
Linux Directory Penguin NsLookup CGI script (nslookup.pl) 1.0 allows remote attackers to execute arbitrary code via shell metacharacters in the (1) query or (2) type parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101684215209558&w=2.

---

#### 249. CVE-2002-0499

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The d_path function in Linux kernel 2.2.20 and earlier, and 2.4.18 and earlier, truncates long pathnames without generating an error, which could allow local users to force programs to perform inappropriate operations on the wrong directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q1/0074.html.

---

#### 250. CVE-2002-0510

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The UDP implementation in Linux 2.4.x kernels keeps the IP Identification field at 0 for all non-fragmented packets, which could allow remote attackers to determine that a target system is running Linux.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8588.php.

---

#### 251. CVE-2002-0638

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_single_network_firewall, hp:secure_os, mandrakesoft:mandrake_linux, mandrakesoft:mandrake_linux_corporate_server, redhat:linux

**漏洞描述 / Description**:
setpwnam.c in the util-linux package, as included in Red Hat Linux 7.3 and earlier, and other operating systems, does not properly lock a temporary file when modifying /etc/passwd, which may allow local users to gain privileges via a complex race condition that uses an open file descriptor in utility programs such as chfn and chsh.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2002-043.0.txt.

---

#### 252. CVE-2002-0767

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: richard_gooch:simpleinit

**漏洞描述 / Description**:
simpleinit on Linux systems does not close a read/write FIFO file descriptor before creating a child process, which allows the child process to cause simpleinit to execute arbitrary programs with root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/276739.

---

#### 253. CVE-2002-0817

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: william_deich:super

**漏洞描述 / Description**:
Format string vulnerability in super for Linux allows local users to gain root privileges via a long command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q3/0045.html.

---

#### 254. CVE-2002-0849

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: cisco:iscsi_driver

**漏洞描述 / Description**:
Linux-iSCSI iSCSI implementation installs the iscsi.conf file with world-readable permissions on some operating systems, including Red Hat Linux Limbo Beta #1, which could allow local users to gain privileges by reading the cleartext CHAP password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102882056105806&w=2.

---

#### 255. CVE-2002-0910

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:netstd

**漏洞描述 / Description**:
Buffer overflows in netstd 3.07-17 package allows remote DNS servers to execute arbitrary code via a long FQDN reply, as observed in the utilities (1) linux-ftpd, (2) pcnfsd, (3) tftp, (4) traceroute, or (5) from/to.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/273987.

---

#### 256. CVE-2002-0915

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: harald_hoyer:xandros_desktop_os, harald_hoyer:autorun

**漏洞描述 / Description**:
autorun in Xandros based Linux distributions allows local users to read the first line of arbitrary files via the -c parameter, which causes autorun to print the first line of the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-05/0260.html.

---

#### 257. CVE-2002-1278

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: jacques_gelinas:linuxconf

**漏洞描述 / Description**:
The mailconf module in Linuxconf 1.24, and other versions before 1.28, on Conectiva Linux 6.0 through 8, and possibly other distributions, generates the Sendmail configuration file (sendmail.cf) in a way that configures Sendmail to run as an open mail relay, which allows remote attackers to send Spam email.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000544.

---

#### 258. CVE-2002-1319

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: trustix:secure_linux, linux:linux_kernel

**漏洞描述 / Description**:
The Linux kernel 2.4.20 and earlier, and 2.5.x, when running on x86 systems, allows local users to cause a denial of service (hang) via the emulation mode, which does not properly clear TF and NT EFLAGs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000553.

---

#### 259. CVE-2002-1380

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.2.x allows local users to cause a denial of service (crash) by using the mmap() function with a PROT_READ parameter to access non-readable memory pages through the /proc/pid/mem interface.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-336.

---

#### 260. CVE-2002-1571

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The linux 2.4 kernel before 2.4.19 assumes that the fninit instruction clears all registers, which could lead to an information leak on processors that do not clear all relevant SSE registers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://linux.bkbits.net:8080/linux-2.4/diffs/arch/i386/kernel/i387.c%401.6.

---

#### 261. CVE-2002-1572

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Signed integer overflow in the bttv_read function in the bttv driver (bttv-driver.c) in Linux kernel before 2.4.20 has unknown impact and attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://linux.bkbits.net:8080/linux-2.4/cset%403d6badc0mxsPaOTT_GuPVxCp1_ormw.

---

#### 262. CVE-2002-1573

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Unspecified vulnerability in the pcilynx ieee1394 firewire driver (pcilynx.c) in Linux kernel before 2.4.20 has unknown impact and attack vectors, related to "wrap handling."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://linux.bkbits.net:8080/linux-2.4/cset%403d6aadcbBIDX67Zl6zZnVKRcsilCVQ.

---

#### 263. CVE-2002-1737

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: astaro:security_linux

**漏洞描述 / Description**:
Astaro Security Linux 2.016 creates world-writable files and directories, which allows local users to overwrite arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/256124.

---

#### 264. CVE-2002-1764

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: adobe:acrobat_reader

**漏洞描述 / Description**:
acroread in Adobe Acrobat Reader 4.05 on Linux allows local users to overwrite arbitrary files via a symlink attack on temporary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/277932.

---

#### 265. CVE-2002-1767

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: oracle:database_server

**漏洞描述 / Description**:
Buffer overflow in tnslsnr of Oracle 8i Database Server 8.1.5 for Linux allows local users to execute arbitrary code as the oracle user via a long command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/265452.

---

#### 266. CVE-2002-1826

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: grsecurity:grsecurity_kernel_patch

**漏洞描述 / Description**:
grsecurity 1.9.4 for Linux kernel 2.4.18 allows local users to bypass read-only permissions by using mmap to directly map /dev/mem or /dev/kmem to kernel memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/273002.

---

#### 267. CVE-2002-1890

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:rhmask

**漏洞描述 / Description**:
rhmask 1.0-9 in Red Hat Linux 7.1 allows local users to overwrite arbitrary files via a symlink attack on the mask file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/276317.

---

#### 268. CVE-2002-1963

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.4.1 through 2.4.19 sets root's NR_RESERVED_FILES limit to 10 files, which allows local users to cause a denial of service (resource exhaustion) by opening 10 setuid binaries.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/281100.

---

#### 269. CVE-2002-1976

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
ifconfig, when used on the Linux kernel 2.2 and later, does not report when the network interface is in promiscuous mode if it was put in promiscuous mode using PACKET_MR_PROMISC, which could allow attackers to sniff the network without detection, as demonstrated using libpcap.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-07/0279.html.

---

#### 270. CVE-2002-2012

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server

**漏洞描述 / Description**:
Unknown vulnerability in Apache 1.3.19 running on HP Secure OS for Linux 1.0 allows remote attackers to cause "unexpected results" via an HTTP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7810.php.

---

#### 271. CVE-2002-2016

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: user-mode_linux:user-mode_linux

**漏洞描述 / Description**:
User-mode Linux (UML) 2.4.17-8 does not restrict access to kernel address space, which allows local users to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-01/0338.html.

---

#### 272. CVE-2002-2254

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The experimental IP packet queuing feature in Netfilter / IPTables in Linux kernel 2.4 up to 2.4.19 and 2.5 up to 2.5.31, when a privileged process exits and network traffic is not being queued, may allow a later process with the same Process ID (PID) to access certain network traffic that would otherwise be restricted.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-12/0025.html.

---

#### 273. CVE-2002-2259

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: gnuplot:gnuplot, suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in the French documentation patch for Gnuplot 3.7 in SuSE Linux before 8.0 allows local users to execute arbitrary code as root via unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6329.

---

#### 274. CVE-2002-2394

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: trend_micro:interscan_viruswall

**漏洞描述 / Description**:
InterScan VirusWall 3.6 for Linux and 3.52 for Windows allows remote attackers to bypass virus protection and possibly execute arbitrary code via HTTP 1.1 chunked transfer encoding.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10106.php.

---

#### 275. CVE-2003-0034

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: jean-jacques_sarton:mtink

**漏洞描述 / Description**:
Buffer overflow in the mtink status monitor, as included in the printer-drivers package in Mandrake Linux, allows local users to execute arbitrary code via a long HOME environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html.

---

#### 276. CVE-2003-0035

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: robert_krawitz:escputil

**漏洞描述 / Description**:
Buffer overflow in escputil, as included in the printer-drivers package in Mandrake Linux, allows local users to execute arbitrary code via a long printer-name command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html.

---

#### 277. CVE-2003-0036

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: rildo_pragana:ml85p

**漏洞描述 / Description**:
ml85p, as included in the printer-drivers package for Mandrake Linux, allows local users to overwrite arbitrary files via a symlink attack on temporary files with predictable filenames of the form "mlg85p%d".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0029.html.

---

#### 278. CVE-2003-0018

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Linux kernel 2.4.10 through 2.4.21-pre4 does not properly handle the O_DIRECT feature, which allows local attackers with write privileges to read portions of previously deleted files, or cause file system corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://linux.bkbits.net:8080/linux-2.4/cset%403e2f193drGJDBg9SG6JwaDQwCBnAMQ.

---

#### 279. CVE-2003-0019

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
uml_net in the kernel-utils package for Red Hat Linux 8.0 has incorrect setuid root privileges, which allows local users to modify network interfaces, e.g. by modifying ARP entries or placing interfaces into promiscuous mode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-044.shtml.

---

#### 280. CVE-2003-0076

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: qt-dcgui:qt-dcgui, dcgui:dcgui

**漏洞描述 / Description**:
Unknown vulnerability in the directory parser for Direct Connect 4 Linux (dcgui) before 0.2.2 allows remote attackers to read files outside the sharelist.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://dc.ketelhot.de/pipermail/dc/2003-January/000094.html.

---

#### 281. CVE-2003-0094

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: andries_brouwer:util-linux

**漏洞描述 / Description**:
A patch for mcookie in the util-linux package for Mandrake Linux 8.2 and 9.0 uses /dev/urandom instead of /dev/random, which causes mcookie to use an entropy source that is more predictable than expected, which may make it easier for certain types of attacks to succeed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.mandrakesoft.com/security/advisories?name=MDKSA-2003:016.

---

#### 282. CVE-2003-0156

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cross_referencer:lxr

**漏洞描述 / Description**:
Directory traversal vulnerability in Cross-Referencing Linux (LXR) allows remote attackers to read arbitrary files via .. (dot dot) sequences in the v parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=104739747222492&w=2.

---

#### 283. CVE-2003-0080

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: gnome:gnome-lokkit

**漏洞描述 / Description**:
The iptables ruleset in Gnome-lokkit in Red Hat Linux 8.0 does not include any rules in the FORWARD chain, which could allow attackers to bypass intended access restrictions if packet forwarding is enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/4400.

---

#### 284. CVE-2003-0127

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The kernel module loader in Linux kernel 2.2.x before 2.2.25, and 2.4.x before 2.4.21, allows local users to gain root privileges by using ptrace to attach to a child process that is spawned by the kernel.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.caldera.com/pub/security/OpenLinux/CSSA-2003-020.0.txt.

---

#### 285. CVE-2002-1492

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: cisco:vpn_5000_client

**漏洞描述 / Description**:
Buffer overflows in the Cisco VPN 5000 Client before 5.2.7 for Linux, and VPN 5000 Client before 5.2.8 for Solaris, allow local users to gain root privileges via (1) close_tunnel and (2) open_tunnel.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml.

---

#### 286. CVE-2002-1506

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: jacques_gelinas:linuxconf

**漏洞描述 / Description**:
Buffer overflow in Linuxconf before 1.28r4 allows local users to execute arbitrary code via a long LINUXCONF_LANG environment variable, which overflows an error string that is generated.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-08/0304.html.

---

#### 287. CVE-2003-0135

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
vsftpd FTP daemon in Red Hat Linux 9 is not compiled against TCP wrappers (tcp_wrappers) but is installed as a standalone service, which inadvertently prevents vsftpd from restricting access as intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2003-084.html.

---

#### 288. CVE-2003-0084

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: mod_auth_any:mod_auth_any

**漏洞描述 / Description**:
mod_auth_any package in Red Hat Enterprise Linux 2.1 and other operating systems does not properly escape arguments when calling other programs, which allows attackers to execute arbitrary commands via shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://rhn.redhat.com/errata/RHSA-2003-114.html.

---

#### 289. CVE-2003-0244

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The route cache implementation in Linux 2.4, and the Netfilter IP conntrack module, allows remote attackers to cause a denial of service (CPU consumption) via packets with forged source addresses that cause a large number of hash table collisions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q2/0073.html.

---

#### 290. CVE-2003-0246

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The ioperm system call in Linux kernel 2.4.20 and earlier does not properly restrict privileges, which allows local users to gain read or write access to certain I/O ports.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q2/0076.html.

---

#### 291. CVE-2003-0247

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Unknown vulnerability in the TTY layer of the Linux kernel 2.4 allows attackers to cause a denial of service ("kernel oops").

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-311.

---

#### 292. CVE-2003-0248

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The mxcsr code in Linux kernel 2.4 allows attackers to modify CPU state registers via a malformed address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-311.

---

#### 293. CVE-2003-0364

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The TCP/IP fragment reassembly handling in the Linux kernel 2.4 allows remote attackers to cause a denial of service (CPU consumption) via certain packets that cause a large number of hash table collisions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-311.

---

#### 294. CVE-2003-0396

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: linux-atm:linux-atm

**漏洞描述 / Description**:
Buffer overflow in les for ATM on Linux (linux-atm) before 2.4.1, if used setuid, allows local users to gain privileges via a long -f command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105154433926396&w=2.

---

#### 295. CVE-2003-0388

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: andrew_morgan:linux_pam

**漏洞描述 / Description**:
pam_wheel in Linux-PAM 0.78, with the trust option enabled and the use_uid option disabled, allows local users to spoof log entries and gain privileges by causing getlogin() to return a spoofed user name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105577915506761&w=2.

---

#### 296. CVE-2003-0418

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The Linux 2.0 kernel IP stack does not properly calculate the size of an ICMP citation, which causes it to include portions of unauthorized memory in ICMP error responses.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105519179005065&w=2.

---

#### 297. CVE-2003-0643

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
Integer signedness error in the Linux Socket Filter implementation (filter.c) in Linux 2.4.3-pre3 to 2.4.22-pre10 allows attackers to cause a denial of service (crash).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ftp.belnet.be/linux/gentoo-portage/sys-kernel/gentoo-sources/files/gentoo-sources-2.4.CAN-2003-0643.patch.

---

#### 298. CVE-2003-0476

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The execve system call in Linux 2.4.x records the file descriptor of the executable process in the file table of the calling process, which allows local users to gain read access to restricted file descriptors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105664924024009&w=2.

---

#### 299. CVE-2003-0480

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: vmware:workstation

**漏洞描述 / Description**:
VMware Workstation 4.0 for Linux allows local users to overwrite arbitrary files and gain privileges via "symlink manipulation."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105673688529147&w=2.

---

#### 300. CVE-2003-0501

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The /proc filesystem in Linux allows local users to obtain sensitive information by opening various entries in /proc/self before executing a setuid program, which causes the program to fail to change the ownership and permissions of those entries.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105621758104242.

---

#### 301. CVE-2026-3006 - winfsp: winfsp: Local privilege escalation via race condition and kernel heap overflow

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] winfsp: winfsp: Local privilege escalation via race condition and kernel heap overflow. Bugzilla: 2463150

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463150

---

#### 302. CVE-2026-31673 - kernel: af_unix: read UNIX_DIAG_VFS data under unix_state_lock

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: af_unix: read UNIX_DIAG_VFS data under unix_state_lock. Bugzilla: 2461752

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461752

---

#### 303. CVE-2026-31681 - kernel: netfilter: xt_multiport: validate range encoding in checkentry

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: netfilter: xt_multiport: validate range encoding in checkentry. Bugzilla: 2461753

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461753

---

#### 304. CVE-2026-31682 - kernel: bridge: br_nd_send: linearize skb before parsing ND options

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: bridge: br_nd_send: linearize skb before parsing ND options. Bugzilla: 2461754

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461754

---

#### 305. CVE-2026-31676 - kernel: rxrpc: only handle RESPONSE during service challenge

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: rxrpc: only handle RESPONSE during service challenge. Bugzilla: 2461755

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461755

---

#### 306. CVE-2026-31683 - kernel: batman-adv: avoid OGM aggregation when skb tailroom is insufficient

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: batman-adv: avoid OGM aggregation when skb tailroom is insufficient. Bugzilla: 2461756

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461756

---

#### 307. CVE-2026-31684 - kernel: net: sched: act_csum: validate nested VLAN headers

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: net: sched: act_csum: validate nested VLAN headers. Bugzilla: 2461757

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461757

---

#### 308. CVE-2026-31674 - kernel: netfilter: ip6t_rt: reject oversized addrnr in rt_mt6_check()

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: netfilter: ip6t_rt: reject oversized addrnr in rt_mt6_check(). Bugzilla: 2461758

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461758

---

#### 309. CVE-2026-31685 - kernel: netfilter: ip6t_eui64: reject invalid MAC header for all packets

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: netfilter: ip6t_eui64: reject invalid MAC header for all packets. Bugzilla: 2461759

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461759

---

#### 310. CVE-2026-31675 - kernel: net/sched: sch_netem: fix out-of-bounds access in packet corruption

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: net/sched: sch_netem: fix out-of-bounds access in packet corruption. Bugzilla: 2461760

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461760

---

#### 311. CVE-2026-31678 - kernel: openvswitch: defer tunnel netdev_put to RCU release

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: openvswitch: defer tunnel netdev_put to RCU release. Bugzilla: 2461761

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461761

---

#### 312. CVE-2026-31679 - kernel: openvswitch: validate MPLS set/set_masked payload length

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: openvswitch: validate MPLS set/set_masked payload length. Bugzilla: 2461762

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461762

---

#### 313. CVE-2026-31677 - kernel: crypto: af_alg - limit RX SG extraction by receive buffer budget

**严重程度 / Severity**: LOW
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: crypto: af_alg - limit RX SG extraction by receive buffer budget. Bugzilla: 2461763

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461763

---

#### 314. CVE-2026-31680 - kernel: net: ipv6: flowlabel: defer exclusive option free until RCU teardown

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: net: ipv6: flowlabel: defer exclusive option free until RCU teardown. Bugzilla: 2461764

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461764

---

#### 315. CVE-2026-41140 - poetry: python: Poetry: Path traversal vulnerability allows arbitrary file write via malicious package extraction

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] poetry: python: Poetry: Path traversal vulnerability allows arbitrary file write via malicious package extraction. Bugzilla: 2461604

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461604

---

#### 316. CVE-2026-41324 - basic-ftp: basic-ftp: Denial of Service via unbounded memory growth from malicious directory listings

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] basic-ftp: basic-ftp: Denial of Service via unbounded memory growth from malicious directory listings. Bugzilla: 2461380

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461380

---

#### 317. CVE-2026-41316 - erb: ERB: Arbitrary code execution via deserialization bypass

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] erb: ERB: Arbitrary code execution via deserialization bypass. Bugzilla: 2461369

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461369

---

#### 318. CVE-2026-41305 - postcss: PostCSS: Cross-Site Scripting (XSS) via improper escaping of style closing tags

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] postcss: PostCSS: Cross-Site Scripting (XSS) via improper escaping of style closing tags. Bugzilla: 2461366

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461366

---

#### 319. CVE-2026-40254 - FreeRDP: FreeRDP: Information disclosure and arbitrary file modification via path traversal

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] FreeRDP: FreeRDP: Information disclosure and arbitrary file modification via path traversal. Bugzilla: 2461368

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461368

---

#### 320. CVE-2026-31584 - kernel: media: mediatek: vcodec: fix use-after-free in encoder release path

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] kernel: media: mediatek: vcodec: fix use-after-free in encoder release path. Bugzilla: 2461436

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461436

---

#### 321. [Ubuntu] USN-8180-5: Linux kernel (IBM) vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Several security issues were discovered in the Linux kernel.
An attacker could possibly use these to compromise the system.
This update corrects flaws in the following subsystems:
  - ARM64 architecture;
  - Block layer subsystem;
  - Drivers core;
  - Bluetooth drivers;
  - DMA engine subsystem;
  - GPU drivers;
  - HID subsystem;
  - Intel Trace Hub HW tracing drivers;
  - IIO ADC drivers;
  - I

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8180-5

---

#### 322. [Ubuntu] USN-8206-1: OpenMPT vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Antonio Morales Maldonado discovered that OpenMPT did not properly limit
the length of strings in certain cases, leading to a buffer overflow.
An attacker could possibly use this issue to cause OpenMPT to crash,
resulting in a denial of service.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8206-1

---

#### 323. [Ubuntu] USN-8205-1: GStreamer Bad Plugins vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that multiple plugins in GStreamer contained arithmetic
overflows. An attacker could possibly use this issue to cause applications
using the plugins to crash, resulting in a denial of service, or possibly
execute arbitrary code. (CVE-2023-37329, CVE-2023-40474, CVE-2023-40475,
CVE-2023-40476)

It was discovered that the MXF demuxer plugin in GStreamer did not
properly manage memo

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8205-1

---

#### 324. [Ubuntu] USN-8204-1: Linux kernel (Raspberry Pi Real-time) vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Josh Eads, Kristoffer Janke, Eduardo Vela Nava, Tavis Ormandy, and Matteo
Rizzo discovered that some AMD Zen processors did not properly verify the
signature of CPU microcode. This flaw is known as EntrySign. A privileged
attacker could possibly use this issue to cause load malicious CPU
microcode causing loss of integrity and confidentiality.
(CVE-2024-36347)

Several security issues were discove

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8204-1

---

#### 325. [Ubuntu] USN-8202-1: jq vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that jq did not correctly handle certain string
concatenations. An attacker could possibly use this issue to cause a denial
of service or execute arbitrary code. This issue was addressed in Ubuntu
16.04 LTS, Ubuntu 18.04 LTS, Ubuntu 20.04 LTS, Ubuntu 22.04 LTS, Ubuntu
24.04 LTS and Ubuntu 25.10. (CVE-2026-32316)

It was discovered that jq did not correctly handle recursion in cer

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8202-1

---

#### 326. [Ubuntu] USN-8212-1: authd vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that authd incorrectly assigned the primary group ID to
users under certain conditions. A local attacker could possibly use this
issue to achieve privilege escalation, or gain unauthorized access to files
belonging to other users.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8212-1

---
