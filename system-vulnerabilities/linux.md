# Linux 系统漏洞知识库 | Linux System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 669**

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

#### 301. CVE-2026-3006 - winfsp: winfsp: Local privilege escalation via race condition and kernel heap…

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

#### 315. CVE-2026-41140 - poetry: python: Poetry: Path traversal vulnerability allows arbitrary file write…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] poetry: python: Poetry: Path traversal vulnerability allows arbitrary file write via malicious package extraction. Bugzilla: 2461604

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461604

---

#### 316. CVE-2026-41324 - basic-ftp: basic-ftp: Denial of Service via unbounded memory growth from malicious…

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

#### 318. CVE-2026-41305 - postcss: PostCSS: Cross-Site Scripting (XSS) via improper escaping of style…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] postcss: PostCSS: Cross-Site Scripting (XSS) via improper escaping of style closing tags. Bugzilla: 2461366

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461366

---

#### 319. CVE-2026-40254 - FreeRDP: FreeRDP: Information disclosure and arbitrary file modification via path…

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

#### 327. CVE-2026-5435 - glibc: glibc: Out-of-bounds write via TSIG record processing

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] glibc: glibc: Out-of-bounds write via TSIG record processing. Bugzilla: 2463465

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463465

---

#### 328. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 329. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 330. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 331. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 332. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 333. CVE-2026-7351 - chromium-browser: Race in MHTML

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Race in MHTML. Bugzilla: 2463656

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463656

---

#### 334. CVE-2026-7353 - chromium-browser: Heap buffer overflow in Skia

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in Skia. Bugzilla: 2463657

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463657

---

#### 335. CVE-2026-7339 - chromium-browser: Heap buffer overflow in WebRTC

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Heap buffer overflow in WebRTC. Bugzilla: 2463658

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463658

---

#### 336. CVE-2026-7341 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463659

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463659

---

#### 337. CVE-2026-7338 - chromium-browser: Use after free in Cast

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Cast. Bugzilla: 2463660

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463660

---

#### 338. CVE-2026-7334 - chromium-browser: Use after free in Views

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Views. Bugzilla: 2463663

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463663

---

#### 339. CVE-2026-7340 - chromium-browser: Integer overflow in ANGLE

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Integer overflow in ANGLE. Bugzilla: 2463664

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463664

---

#### 340. CVE-2026-7358 - chromium-browser: Use after free in Animation

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Animation. Bugzilla: 2463665

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463665

---

#### 341. CVE-2026-7356 - chromium-browser: Use after free in Navigation

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Navigation. Bugzilla: 2463667

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463667

---

#### 342. CVE-2026-7352 - chromium-browser: Use after free in Media

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Media. Bugzilla: 2463669

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463669

---

#### 343. CVE-2026-7359 - chromium-browser: Use after free in ANGLE

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in ANGLE. Bugzilla: 2463670

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463670

---

#### 344. CVE-2026-7348 - chromium-browser: Use after free in Codecs

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in Codecs. Bugzilla: 2463671

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463671

---

#### 345. CVE-2026-7336 - chromium-browser: Use after free in WebRTC

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Use after free in WebRTC. Bugzilla: 2463676

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463676

---

#### 346. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 347. [Ubuntu] USN-8223-1: Roundcube Webmail vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that Roundcube Webmail mishandled Punycode xn-- domain names. An attacker could possibly use this issue to cause a homograph attack. (CVE-2019-15237) It was discovered that Roundcube Webmail did not properly sanitize certain attributes when handling CSS within HTML messages and certain SVG attributes. An attacker could possibly use this issue to cause a cross-site scripting attac

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8223-1

---

#### 348. [Ubuntu] USN-8224-1: Linux kernel (BlueField) vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Qualys discovered that several vulnerabilities existed in the AppArmor Linux kernel Security Module (LSM). An unprivileged local attacker could use these issues to load, replace, and remove arbitrary AppArmor profiles causing denial of service, exposure of sensitive information (kernel memory), local privilege escalation, or possibly escape a container. (LP: #2143853, CVE-2026-23268, CVE-2026-2326

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8224-1

---

#### 349. [Ubuntu] USN-8222-1: OpenSSH vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Christos Papakonstantinou discovered that the OpenSSH scp tool incorrectly handled the legacy scp protocol (-O) option. This could result in certain files being installed setuid or setgid, contrary to expectations. (CVE-2026-35385) Florian Kohnhäuser discovered that OpenSSH incorrectly handled shell metacharacters in usernames within a command line. When untrusted usernames and non-default configu

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8222-1

---

#### 350. [Ubuntu] USN-8195-3: PackageKit vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
USN-8195-1 fixed a vulnerability in PackageKit. This update provides the corresponding fix to Ubuntu 16.04 LTS, Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. Original advisory details: It was discovered that PackageKit incorrectly handled certain transactions. A local attacker could use this issue to install arbitrary packages as root, possibly resulting in privilege escalation.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8195-3

---

#### 351. [Ubuntu] USN-8221-1: wheel vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that wheel did not correctly handle certain file paths. If a user or automated system were tricked into opening a specially crafted file, an attacker could possibly use this issue to execute arbitrary code.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8221-1

---

#### 352. [Ubuntu] USN-8198-2: Tornado vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
USN-8198-1 fixed vulnerabilities in Tornado. This update provides the corresponding updates for Ubuntu 26.04 LTS. Original advisory details: It was discovered that Tornado incorrectly handled parsing of large multipart request bodies. An attacker could possibly use this issue to cause a denial of service. (CVE-2026-31958) It was discovered that Tornado did not properly validate characters in cooki

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8198-2

---

#### 353. [Ubuntu] USN-8219-1: UltraJSON vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Cameron Criswell discovered that UltraJSON contained a memory leak that would occur when parsing large integers. An attacker could possibly use this issue to cause UltraJSON to crash, resulting in a denial of service. This issue only affected Ubuntu 24.04 LTS, Ubuntu 25.10, and Ubuntu 26.04 LTS. (CVE-2026-32874) It was discovered that UltraJSON contained integer overflow/underflow issues when calc

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8219-1

---

#### 354. [Ubuntu] USN-8185-2: Linux kernel (Low Latency NVIDIA) vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Josh Eads, Kristoffer Janke, Eduardo Vela Nava, Tavis Ormandy, and Matteo Rizzo discovered that some AMD Zen processors did not properly verify the signature of CPU microcode. This flaw is known as EntrySign. A privileged attacker could possibly use this issue to cause load malicious CPU microcode causing loss of integrity and confidentiality. (CVE-2024-36347) Several security issues were discover

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8185-2

---

#### 355. [Ubuntu] USN-8217-1: follow-redirects vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that follow-redirects did not properly protect sensitive user information during redirects. An attacker could possibly use this issue to expose sensitive information. This issue only affected Ubuntu 18.04 LTS and Ubuntu 20.04 LTS. (CVE-2022-0155) It was discovered that follow-redirects did not properly remove sensitive information before storage or transfer. An attacker could pos

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8217-1

---

#### 356. [Ubuntu] USN-8190-2: Rack::Session vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
USN-8190-1 fixed a vulnerability in Rack::Session. This update provides the corresponding update for Ubuntu 26.04 LTS. Original advisory details: SeungMyung Lee discovered that Rack::Session did not properly reject cookies upon decryption failure. A remote attacker could use this issue to manipulate session contents and possibly gain unauthorized access.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8190-2

---

#### 357. CVE-2026-7233 - mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read

**严重程度 / Severity**: LOW
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] mupdf: Artifex MuPDF: Information disclosure due to out-of-bounds read. Bugzilla: 2463367

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463367

---

#### 358. CVE-2026-42510 - OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] OpenStack Ironic: ipmitool: OpenStack Ironic: Arbitrary Code Execution via Remote Hardware Management. Bugzilla: 2463371

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463371

---

#### 359. CVE-2026-40356 - krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5 (krb5): Denial of Service via integer underflow and out-of-bounds read. Bugzilla: 2463368

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463368

---

#### 360. CVE-2026-40355 - krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] krb5: MIT Kerberos 5: Denial of Service via NULL pointer dereference in NegoEx mechanism. Bugzilla: 2463370

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463370

---

#### 361. CVE-2026-7309 - openshift-controller-manager: OpenShift Container Platform: Information disclosure…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] openshift-controller-manager: OpenShift Container Platform: Information disclosure via environment variable injection. Bugzilla: 2463451

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463451

---

#### 362. CVE-2026-7360 - chromium-browser: Insufficient validation of untrusted input in Compositing

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] chromium-browser: Insufficient validation of untrusted input in Compositing. Bugzilla: 2463677

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463677

---

#### 363. [Ubuntu] USN-8225-1: Python marshmallow vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Jared Deckard discovered that Python marshmallow did not correctly handle hiding certain fields. An attacker could possibly use this issue to leak sensitive information. This issue only affected Ubuntu 18.04 LTS. (CVE-2018-17175) It was discovered that Python marshmallow did not efficiently handle merging certain objects. An attacker could possibly use this issue to cause a denial of service. This

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8225-1

---

#### 364. CVE-2026-6868 - wireshark: Wireshark: Denial of Service via malicious network capture file

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] wireshark: Wireshark: Denial of Service via malicious network capture file. Bugzilla: 2464010

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464010

---

#### 365. CVE-2026-7378 - Wireshark: sharkd: Wireshark sharkd: Denial of Service via crash vulnerability

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Wireshark: sharkd: Wireshark sharkd: Denial of Service via crash vulnerability. Bugzilla: 2464005

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464005

---

#### 366. CVE-2026-7375 - Wireshark: Wireshark: Denial of Service via UDS protocol dissector infinite loop

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Wireshark: Wireshark: Denial of Service via UDS protocol dissector infinite loop. Bugzilla: 2464007

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464007

---

#### 367. CVE-2026-7376 - Wireshark: sharkd: Wireshark sharkd: Denial of Service due to crash

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Wireshark: sharkd: Wireshark sharkd: Denial of Service due to crash. Bugzilla: 2464008

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464008

---

#### 368. CVE-2026-41636 - apache.com/apache/thrift: Apache Thrift: Node.js skip() recursion

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] apache.com/apache/thrift: Apache Thrift: Node.js skip() recursion. Bugzilla: 2463404

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463404

---

#### 369. CVE-2026-41607 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read vulnerability. Bugzilla: 2463412

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463412

---

#### 370. CVE-2026-41606 - Apache Thrift: Apache Thrift: Denial of Service via uncontrolled recursion

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: Apache Thrift: Denial of Service via uncontrolled recursion. Bugzilla: 2463408

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463408

---

#### 371. CVE-2026-41605 - Apache Thrift: Apache Thrift: Integer Overflow or Wraparound Vulnerability

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: Apache Thrift: Integer Overflow or Wraparound Vulnerability. Bugzilla: 2463418

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463418

---

#### 372. CVE-2026-41604 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Out-of-bounds Read vulnerability. Bugzilla: 2463416

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463416

---

#### 373. CVE-2026-41603 - Apache Thrift: apache.com/apache/thrift: Apache Thrift: Security Bypass via…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Apache Thrift: apache.com/apache/thrift: Apache Thrift: Security Bypass via Improper Certificate Hostname Validation. Bugzilla: 2463411

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463411

---

#### 374. CVE-2026-41602 - github.com/apache/thrift: Apache Thrift: Integer Overflow in TFramedTransport Go…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] github.com/apache/thrift: Apache Thrift: Integer Overflow in TFramedTransport Go implementation. Bugzilla: 2463407

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463407

---

#### 375. [Ubuntu] USN-8226-1: kmod update

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disables loading the algif_aead module as a measure to mitigate the issue until kernel updates are made available. See the following URL for more information https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-1

---

#### 376. [Ubuntu] USN-8218-1: zuluCrypt vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Aaron Rainbolt discovered that zuluCrypt used insecure PolicyKit settings in zuluPolkit. An attacker could possibly use this issue to cause local privilege escalation to root. (CVE-2025-53391)

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8218-1

---

#### 377. [Ubuntu] USN-8226-2: kmod update

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
USN-8226-1 added a mitigation to kmod to disable loading the algif_aead module. This update adds the same mitigation to Ubuntu 14.04 LTS, Ubuntu 16.04 LTS, Ubuntu 18.04 LTS, and Ubuntu 20.04 LTS. Original advisory details: It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disabl

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-2

---

#### 378. CVE-2026-3832 - gnutls: gnutls: Security bypass allows acceptance of revoked server certificates…

**严重程度 / Severity**: LOW
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] gnutls: gnutls: Security bypass allows acceptance of revoked server certificates via crafted OCSP response. Bugzilla: 2445762

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2445762

---

#### 379. CVE-2026-33845 - gnutls: GnuTLS: Denial of Service via DTLS zero-length fragment

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] gnutls: GnuTLS: Denial of Service via DTLS zero-length fragment. Bugzilla: 2450624

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2450624

---

#### 380. CVE-2026-3833 - gnutls: GnuTLS: Policy bypass due to case-sensitive nameConstraints comparison

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] gnutls: GnuTLS: Policy bypass due to case-sensitive nameConstraints comparison. Bugzilla: 2445763

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2445763

---

#### 381. CVE-2026-7163 - assisted-service: assisted-service: Authenticated users can gain administrative…

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] assisted-service: assisted-service: Authenticated users can gain administrative access to OpenShift clusters via credential disclosure. Bugzilla: 2463152

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463152

---

#### 382. CVE-2026-7500 - org.keycloak.keycloak-services: Improper Access Control on Keycloak Server when the…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] org.keycloak.keycloak-services: Improper Access Control on Keycloak Server when the account Account API feature is disabled. Bugzilla: 2464126

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2464126

---

#### 383. CVE-2026-4873 - curl: curl: Information disclosure due to incorrect TLS connection reuse

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: curl: Information disclosure due to incorrect TLS connection reuse. Bugzilla: 2461200

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461200

---

#### 384. CVE-2026-5773 - curl: libcurl: Wrong file transfer due to incorrect SMB connection reuse

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Wrong file transfer due to incorrect SMB connection reuse. Bugzilla: 2461201

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461201

---

#### 385. CVE-2026-6253 - curl: curl: Proxy credential disclosure via redirects to unauthenticated proxies

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: curl: Proxy credential disclosure via redirects to unauthenticated proxies. Bugzilla: 2461202

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461202

---

#### 386. CVE-2026-6276 - curl: libcurl: Information disclosure due to cookie leak when reusing connections…

**严重程度 / Severity**: LOW
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Information disclosure due to cookie leak when reusing connections with custom Host headers. Bugzilla: 2461203

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461203

---

#### 387. CVE-2026-5545 - curl: libcurl: Authentication bypass due to incorrect HTTP Negotiate connection…

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Authentication bypass due to incorrect HTTP Negotiate connection reuse. Bugzilla: 2461204

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461204

---

#### 388. CVE-2026-6429 - curl: libcurl: Credential leak via reused proxy connection during HTTP redirects

**严重程度 / Severity**: MODERATE
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] curl: libcurl: Credential leak via reused proxy connection during HTTP redirects. Bugzilla: 2461205

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2461205

---

#### 389. CVE-2026-38993 - Cockpit: Cockpit: Arbitrary file write via directory traversal in Buckets component

**严重程度 / Severity**: IMPORTANT
**受影响产品 / Affected Products**: Red Hat Enterprise Linux

**漏洞描述 / Description**:
[Red Hat] Cockpit: Cockpit: Arbitrary file write via directory traversal in Buckets component. Bugzilla: 2463843

**补丁信息 / Patch Info**:
Apply Red Hat security advisory patch via yum/dnf update.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=2463843

---

#### 390. CVE-2005-0080

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: gnu:mailman, ubuntu:ubuntu_linux

**漏洞描述 / Description**:
The 55_options_traceback.dpatch patch for mailman 2.1.5 in Ubuntu 4.10 displays a different error message depending on whether the e-mail address is subscribed to a private list, which allows remote attackers to determine the list membership for a given e-mail address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285839.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285839
- http://marc.info/?l=bugtraq&m=110549296126351&w=2
- http://qa.debian.org/bts-security.html
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285839
- http://marc.info/?l=bugtraq&m=110549296126351&w=2

---

#### 391. CVE-2006-0176

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: xmame:xmame

**漏洞描述 / Description**:
Buffer overflow in certain functions in src/fileio.c and src/unix/fileio.c in xmame before 11 January 2006 may allow local users to gain privileges via a long (1) -lang, (2) -ctrlr, (3) -pb, or (4) -rec argument on many operating systems, and via a long (5) -jdev argument on Ubuntu Linux.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0353.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0353.html
- http://www.securityfocus.com/archive/1/421849/100/0/threaded
- http://www.securityfocus.com/bid/16203
- http://x.mame.net/changes-unix.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24102

---

#### 392. CVE-2006-0458

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: irssi:irssi

**漏洞描述 / Description**:
The DCC ACCEPT command handler in irssi before 0.8.9+0.8.10rc5-0ubuntu4.1 in Ubuntu Linux, and possibly other distributions, allows remote attackers to cause a denial of service (application crash) via certain crafted arguments in a DCC command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19090.

**参考链接 / References**:
- http://secunia.com/advisories/19090
- http://www.securityfocus.com/bid/16913
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25147
- https://usn.ubuntu.com/259-1/
- http://secunia.com/advisories/19090

---

#### 393. CVE-2006-1183

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux

**漏洞描述 / Description**:
The Ubuntu 5.10 installer does not properly clear passwords from the installer log file (questions.dat), and leaves the log file with world-readable permissions, which allows local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19200.

**参考链接 / References**:
- http://secunia.com/advisories/19200
- http://securitytracker.com/id?1015761
- http://www.osvdb.org/23868
- http://www.securityfocus.com/bid/17086
- http://www.vupen.com/english/advisories/2006/0927

---

#### 394. CVE-2006-3378

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux

**漏洞描述 / Description**:
passwd command in shadow in Ubuntu 5.04 through 6.06 LTS, when called with the -f, -g, or -s flag, does not check the return code of a setuid call, which might allow local users to gain root privileges if setuid fails in cases such as PAM failures or resource limits.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/20950.

**参考链接 / References**:
- http://secunia.com/advisories/20950
- http://secunia.com/advisories/20966
- http://secunia.com/advisories/21480
- http://www.debian.org/security/2006/dsa-1150
- http://www.osvdb.org/26995

---

#### 395. CVE-2006-3597

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux

**漏洞描述 / Description**:
passwd before 1:4.0.13 on Ubuntu 6.06 LTS leaves the root password blank instead of locking it when the administrator selects the "Go Back" option after the final "Installation complete" message and uses the main menu, which causes the password to be zeroed out in the installer's memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21022.

**参考链接 / References**:
- http://secunia.com/advisories/21022
- http://www.osvdb.org/27091
- http://www.ubuntu.com/usn/usn-316-1
- http://secunia.com/advisories/21022
- http://www.osvdb.org/27091

---

#### 396. CVE-2006-5648

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux

**漏洞描述 / Description**:
Ubuntu Linux 6.10 for the PowerPC (PPC) allows local users to cause a denial of service (resource consumption) by using the (1) sys_get_robust_list and (2) sys_set_robust_list functions to create processes that cannot be killed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/23361.

**参考链接 / References**:
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/23474
- http://www.novell.com/linux/security/advisories/2006_79_kernel.html
- http://www.securityfocus.com/bid/21582

---

#### 397. CVE-2006-5649

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux

**漏洞描述 / Description**:
Unspecified vulnerability in the "alignment check exception handling" in Ubuntu 5.10, 6.06 LTS, and 6.10 for the PowerPC (PPC) allows local users to cause a denial of service (kernel panic) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/23361.

**参考链接 / References**:
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23370
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/23395
- http://secunia.com/advisories/23474

---

#### 398. CVE-2007-5159

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: ntfs-3g:ntfs-3g, redhat:fedora, ubuntu:ubuntu_linux

**漏洞描述 / Description**:
The ntfs-3g package before 1.913-2.fc7 in Fedora 7, and an ntfs-3g package in Ubuntu 7.10/Gutsy, assign incorrect permissions (setuid root) to mount.ntfs-3g, which allows local users with fuse group membership to read from and write to arbitrary block devices, possibly involving a file descriptor leak.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/26938.

**参考链接 / References**:
- http://secunia.com/advisories/26938
- https://bugzilla.redhat.com/show_bug.cgi?id=298651
- https://www.redhat.com/archives/fedora-desktop-list/2007-September/msg00163.html
- https://www.redhat.com/archives/fedora-package-announce/2007-September/msg00368.html
- http://secunia.com/advisories/26938

---

#### 399. CVE-2007-3920

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux, gnome:screensaver, compiz:compiz

**漏洞描述 / Description**:
GNOME screensaver 2.20 in Ubuntu 7.10, when used with Compiz, does not properly reserve input focus, which allows attackers with physical access to take control of the session after entering an Alt-Tab sequence, a related issue to CVE-2007-3069.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.opensuse.org/opensuse-security-announce/2008-06/msg00002.html.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-06/msg00002.html
- http://secunia.com/advisories/27381
- http://secunia.com/advisories/28627
- http://secunia.com/advisories/30329
- http://secunia.com/advisories/30715

---

#### 400. CVE-2006-7229

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: ubuntu:linux_kernel

**漏洞描述 / Description**:
The skge driver 1.5 in Linux kernel 2.6.15 on Ubuntu does not properly use the spin_lock and spin_unlock functions, which allows remote attackers to cause a denial of service (machine crash) via a flood of network traffic.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/28971.

**参考链接 / References**:
- http://secunia.com/advisories/28971
- http://www.securityfocus.com/bid/26511
- http://www.ubuntu.com/usn/usn-578-1
- https://bugs.launchpad.net/ubuntu/+source/linux-source-2.6.15/+bug/65631
- http://secunia.com/advisories/28971

---

#### 401. CVE-2007-6178

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: easy_hosting_control_panel:easy_hosting_control_panel

**漏洞描述 / Description**:
Multiple PHP remote file inclusion vulnerabilities in Easy Hosting Control Panel for Ubuntu (EHCP) 0.22.8 and earlier allow remote attackers to execute arbitrary PHP code via a URL in the confdir parameter to (1) dbutil.bck.php and (2) dbutil.php in config/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/26623.

**参考链接 / References**:
- http://www.securityfocus.com/bid/26623
- https://exchange.xforce.ibmcloud.com/vulnerabilities/38698
- https://www.exploit-db.com/exploits/4671
- http://www.securityfocus.com/bid/26623
- https://exchange.xforce.ibmcloud.com/vulnerabilities/38698

---

#### 402. CVE-2008-0420

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: mozilla:seamonkey, mozilla:firefox, mozilla:thunderbird

**漏洞描述 / Description**:
modules/libpr0n/decoders/bmp/nsBMPDecoder.cpp in Mozilla Firefox before 2.0.0.12, Thunderbird before 2.0.0.12, and SeaMonkey before 1.1.8 does not properly perform certain calculations related to the mColors table, which allows remote attackers to read portions of memory uninitialized via a crafted 8-bit bitmap (BMP) file that triggers an out-of-bounds read within the heap, as demonstrated using a CANVAS element; or cause a denial of service (application crash) via a crafted 8-bit bitmap file that triggers an out-of-bounds read. NOTE: the initial public reports stated that this affected Firefox in Ubuntu 6.06 through 7.10.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://browser.netscape.com/releasenotes/.

**参考链接 / References**:
- http://browser.netscape.com/releasenotes/
- http://secunia.com/advisories/28758
- http://secunia.com/advisories/28839
- http://secunia.com/advisories/29049
- http://secunia.com/advisories/29098

---

#### 403. CVE-2008-1072

**严重程度 / Severity**: N/A | CVSS: 4.7
**受影响产品 / Affected Products**: wireshark:wireshark

**漏洞描述 / Description**:
The TFTP dissector in Wireshark (formerly Ethereal) 0.6.0 through 0.99.7, when running on Ubuntu 7.10, allows remote attackers to cause a denial of service (crash or memory consumption) via a malformed packet, possibly related to a Cairo library bug.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.opensuse.org/opensuse-security-announce/2008-03/msg00001.html.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2008-03/msg00001.html
- http://secunia.com/advisories/29156
- http://secunia.com/advisories/29188
- http://secunia.com/advisories/29223
- http://secunia.com/advisories/29242

---

#### 404. CVE-2008-2285

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ubuntu:linux

**漏洞描述 / Description**:
The ssh-vulnkey tool on Ubuntu Linux 7.04, 7.10, and 8.04 LTS does not recognize authorized_keys lines that contain options, which makes it easier for remote attackers to exploit CVE-2008-0166 by guessing a key that was not identified by this tool.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/usn-612-5.

**参考链接 / References**:
- http://www.ubuntu.com/usn/usn-612-5
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42568
- http://www.ubuntu.com/usn/usn-612-5
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42568

---

#### 405. CVE-2008-5103

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux, dcgrendel:vmbuilder

**漏洞描述 / Description**:
The (1) python-vm-builder and (2) ubuntu-vm-builder implementations in VMBuilder 0.9 in Ubuntu 8.10 omit the -e option when invoking chpasswd with a root:! argument, which configures the root account with a cleartext password of ! (exclamation point) and allows attackers to bypass intended login restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff.

**参考链接 / References**:
- http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff
- http://osvdb.org/49996
- http://secunia.com/advisories/32697
- http://www.securityfocus.com/bid/32292
- http://www.ubuntu.com/usn/usn-670-1

---

#### 406. CVE-2008-5104

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:ubuntu_linux, dcgrendel:vmbuilder

**漏洞描述 / Description**:
Ubuntu 6.06 LTS, 7.10, 8.04 LTS, and 8.10, when installed as a virtual machine by (1) python-vm-builder or (2) ubuntu-vm-builder in VMBuilder 0.9 in Ubuntu 8.10, have ! (exclamation point) as the default root password, which allows attackers to bypass intended login restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff.

**参考链接 / References**:
- http://launchpadlibrarian.net/19619929/vm-builder_0.9-0ubuntu3.1.debdiff
- http://secunia.com/advisories/32697
- http://www.securityfocus.com/bid/32292
- http://www.ubuntu.com/usn/usn-670-1
- https://bugs.launchpad.net/ubuntu/+source/vm-builder/+bug/296841

---

#### 407. CVE-2008-5393

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: privacy-cd:unbuntu_privacy_remix

**漏洞描述 / Description**:
UPR-Kernel in Ubuntu Privacy Remix (UPR) before 8.04_r1 includes kernel support for mounting RAID arrays, which might allow remote attackers to bypass intended isolation mechanisms by (1) reading from or (2) writing to these arrays.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/4696.

**参考链接 / References**:
- http://securityreason.com/securityalert/4696
- http://www.securityfocus.com/archive/1/498905/100/0/threaded
- http://www.securityfocus.com/bid/32629
- https://bugs.launchpad.net/bugs/301285
- https://exchange.xforce.ibmcloud.com/vulnerabilities/47082

---

#### 408. CVE-2008-4539

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: kvm_qumranet:kvm, debian:debian_linux, canonical:ubuntu_linux, qemu:qemu

**漏洞描述 / Description**:
Heap-based buffer overflow in the Cirrus VGA implementation in (1) KVM before kvm-82 and (2) QEMU on Debian GNU/Linux and Ubuntu might allow local users to gain privileges by using the VNC console for a connection, aka the LGD-54XX "bitblt" heap overflow.  NOTE: this issue exists because of an incorrect fix for CVE-2007-1320.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://git.kernel.dk/?p=qemu.git%3Ba=commitdiff%3Bh=65d35a09979e63541afc5bfc595b9f1b1b4ae069.

**参考链接 / References**:
- http://git.kernel.dk/?p=qemu.git%3Ba=commitdiff%3Bh=65d35a09979e63541afc5bfc595b9f1b1b4ae069
- http://groups.google.com/group/linux.debian.changes.devel/msg/9e0dc008572f2867?dmode=source
- http://lists.opensuse.org/opensuse-security-announce/2009-04/msg00003.html
- http://secunia.com/advisories/25073
- http://secunia.com/advisories/29129

---

#### 409. CVE-2006-7236

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: ubuntu:linux, debian:debian_linux, invisible-island:xterm

**漏洞描述 / Description**:
The default configuration of xterm on Debian GNU/Linux sid and possibly Ubuntu enables the allowWindowOps resource, which allows user-assisted attackers to execute arbitrary code or have unspecified other impact via escape sequences.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=384593.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=384593
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=510030
- http://secunia.com/advisories/33388
- https://usn.ubuntu.com/703-1/
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=384593

---

#### 410. CVE-2009-0122

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: hp:hplip

**漏洞描述 / Description**:
hplip.postinst in HP Linux Imaging and Printing (HPLIP) 2.7.7 and 2.8.2 on Ubuntu allows local users to change the ownership of arbitrary files via unspecified manipulations in advance of an HPLIP installation or upgrade by an administrator, related to the product's attempt to correct the ownership of its configuration files within home directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/33539.

**参考链接 / References**:
- http://secunia.com/advisories/33539
- http://www.securityfocus.com/bid/33249
- http://www.ubuntu.com/usn/usn-708-1
- https://launchpad.net/bugs/191299
- http://secunia.com/advisories/33539

---

#### 411. CVE-2009-1295

**严重程度 / Severity**: N/A | CVSS: 1.9
**受影响产品 / Affected Products**: ubuntu:ubuntu, apport:apport

**漏洞描述 / Description**:
Apport before 0.108.4 on Ubuntu 8.04 LTS, before 0.119.2 on Ubuntu 8.10, and before 1.0-0ubuntu5.2 on Ubuntu 9.04 does not properly remove files from the application's crash-report directory, which allows local users to delete arbitrary files via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.opensuse.org/opensuse-security-announce/2009-05/msg00000.html.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2009-05/msg00000.html
- http://secunia.com/advisories/34947
- http://secunia.com/advisories/34952
- http://secunia.com/advisories/35065
- http://www.securityfocus.com/bid/34776

---

#### 412. CVE-2009-1573

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: ubuntu:linux, debian:debian_linux, redhat:fedora, branden_robinson:xvfb-run

**漏洞描述 / Description**:
xvfb-run 1.6.1 in Debian GNU/Linux, Ubuntu, Fedora 10, and possibly other operating systems place the magic cookie (MCOOKIE) on the command line, which allows local users to gain privileges by listing the process and its arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=526678.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=526678
- http://secunia.com/advisories/39834
- http://www.openwall.com/lists/oss-security/2009/05/05/2
- http://www.openwall.com/lists/oss-security/2009/05/05/4
- http://www.securityfocus.com/bid/34828

---

#### 413. CVE-2008-6792

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ubuntu:linux

**漏洞描述 / Description**:
system-tools-backends before 2.6.0-1ubuntu1.1 in Ubuntu 8.10, as used by "Users and Groups" in GNOME System Tools, hashes account passwords with 3DES and consequently limits effective password lengths to eight characters, which makes it easier for context-dependent attackers to successfully conduct brute-force password attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/50037.

**参考链接 / References**:
- http://osvdb.org/50037
- http://secunia.com/advisories/32566
- http://www.ubuntu.com/usn/usn-663-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50435
- https://launchpad.net/bugs/287134

---

#### 414. CVE-2009-1601

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: ubuntu:linux

**漏洞描述 / Description**:
The Ubuntu clamav-milter.init script in clamav-milter before 0.95.1+dfsg-1ubuntu1.2 in Ubuntu 9.04 sets the ownership of the current working directory to the clamav account, which might allow local users to bypass intended access restrictions via read or write operations involving this directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/35000.

**参考链接 / References**:
- http://secunia.com/advisories/35000
- http://www.securityfocus.com/bid/34818
- http://www.ubuntu.com/usn/USN-770-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50311
- https://launchpad.net/bugs/365823

---

#### 415. CVE-2009-1296

**严重程度 / Severity**: N/A | CVSS: 1.9
**受影响产品 / Affected Products**: ubuntu:73-oubuntu, ubuntu:ubuntu

**漏洞描述 / Description**:
The eCryptfs support utilities (ecryptfs-utils) 73-0ubuntu6.1 on Ubuntu 9.04 stores the mount passphrase in installation logs, which might allow local users to obtain access to the filesystem by reading the log files from disk.  NOTE: the log files are only readable by root.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/35383.

**参考链接 / References**:
- http://secunia.com/advisories/35383
- http://www.securitytracker.com/id?1022347
- http://www.ubuntu.com/usn/usn-783-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/51191
- http://secunia.com/advisories/35383

---

#### 416. CVE-2009-3232

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
pam-auth-update for PAM, as used in Ubuntu 8.10 and 9.4, and Debian GNU/Linux, does not properly handle an "empty selection" for system authentication modules in certain rare configurations, which causes any attempt to be successful and allows remote attackers to bypass authentication.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=519927.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=519927
- http://secunia.com/advisories/36620
- http://www.openwall.com/lists/oss-security/2009/09/08/7
- http://www.securityfocus.com/bid/36306
- https://launchpad.net/bugs/410171

---

#### 417. CVE-2009-2939

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: debian:debian_linux, ubuntu:ubuntu_linux, postfix:postfix

**漏洞描述 / Description**:
The postfix.postinst script in the Debian GNU/Linux and Ubuntu postfix 2.5.5 package grants the postfix user write access to /var/spool/postfix/pid, which might allow local users to conduct symlink attacks that overwrite arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2011/dsa-2233.

**参考链接 / References**:
- http://www.debian.org/security/2011/dsa-2233
- http://www.openwall.com/lists/oss-security/2009/09/18/6
- http://www.debian.org/security/2011/dsa-2233
- http://www.openwall.com/lists/oss-security/2009/09/18/6

---

#### 418. CVE-2010-0832

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
pam_motd (aka the MOTD module) in libpam-modules before 1.1.0-2ubuntu1.1 in PAM on Ubuntu 9.10 and libpam-modules before 1.1.1-2ubuntu5 in PAM on Ubuntu 10.04 LTS allows local users to change the ownership of arbitrary files via a symlink attack on .cache in a user's home directory, related to "user file stamps" and the motd.legal-notice file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/40512.

**参考链接 / References**:
- http://secunia.com/advisories/40512
- http://twitter.com/jonoberheide/statuses/18009527979
- http://www.exploit-db.com/exploits/14273
- http://www.h-online.com/security/news/item/Ubuntu-closes-root-hole-1034618.html
- http://www.osvdb.org/66116

---

#### 419. CVE-2010-0834

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: dell:latitude_2110_netbook, ubuntu:ubuntu_linux

**漏洞描述 / Description**:
The base-files package before 5.0.0ubuntu7.1 on Ubuntu 9.10 and before 5.0.0ubuntu20.10.04.2 on Ubuntu 10.04 LTS, as shipped on Dell Latitude 2110 netbooks, does not require authentication for package installation, which allows remote archive servers and man-in-the-middle attackers to execute arbitrary code via a crafted package.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/40889.

**参考链接 / References**:
- http://secunia.com/advisories/40889
- http://www.securityfocus.com/bid/42280
- http://www.ubuntu.com/usn/usn-968-1
- http://www.vupen.com/english/advisories/2010/2015
- http://secunia.com/advisories/40889

---

#### 420. CVE-2011-0725

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux, sebastian_heinlein:aptdaemon

**漏洞描述 / Description**:
Absolute path traversal vulnerability in the org.debian.apt.UpdateCachePartially method in worker.py in Aptdaemon 0.40 in Ubuntu 10.10 and 11.04 allows local users to read arbitrary files via a full pathname in the sources_list argument, related to the D-Bus interface.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/46490.

**参考链接 / References**:
- http://www.securityfocus.com/bid/46490
- http://www.securitytracker.com/id?1025107
- http://www.ubuntu.com/usn/USN-1068-1
- http://www.vupen.com/english/advisories/2011/0459
- https://bugs.launchpad.net/bugs/722228

---

#### 421. CVE-2011-1400

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: debian:debian_linux, canonical:ubuntu_linux, debian:tex-common

**漏洞描述 / Description**:
The default configuration of the shell_escape_commands directive in conf/texmf.d/95NonPath.cnf in the tex-common package before 2.08.1 in Debian GNU/Linux squeeze, Ubuntu 10.10 and 10.04 LTS, and possibly other operating systems lists certain programs, which might allow remote attackers to execute arbitrary code via a crafted TeX document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/43816.

**参考链接 / References**:
- http://secunia.com/advisories/43816
- http://secunia.com/advisories/43973
- http://svn.debian.org/wsvn/debian-tex/?op=comp&compare%5B%5D=%2Ftex-common%2Ftrunk%404781&compare%5B%5D=%2Ftex-common%2Ftrunk%404812
- http://svn.debian.org/wsvn/debian-tex/tex-common/trunk/?op=log
- http://www.debian.org/security/2011/dsa-2198

---

#### 422. CVE-2011-0730

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux, eucalyptus:eucalyptus

**漏洞描述 / Description**:
Eucalyptus before 2.0.3 and Eucalyptus EE before 2.0.2, as used in Ubuntu Enterprise Cloud (UEC) and other products, do not properly interpret signed elements in SOAP requests, which allows man-in-the-middle attackers to execute arbitrary commands by modifying a request, related to an "XML Signature Element Wrapping" or a "SOAP signature replay" issue.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://launchpadlibrarian.net/72472626/eucalyptus_2.0.1%2Bbzr1256-0ubuntu5_2.0.1%2Bbzr1256-0ubuntu6.diff.gz.

**参考链接 / References**:
- http://launchpadlibrarian.net/72472626/eucalyptus_2.0.1%2Bbzr1256-0ubuntu5_2.0.1%2Bbzr1256-0ubuntu6.diff.gz
- http://open.eucalyptus.com/wiki/esa-02
- http://secunia.com/advisories/44705
- http://www.securityfocus.com/bid/48000
- http://www.ubuntu.com/usn/USN-1137-1

---

#### 423. CVE-2011-3150

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
Software Center in Ubuntu 11.10, 11.04 10.10 does not properly validate server certificates, which allows remote attackers to execute arbitrary code or obtain sensitive information via a man-in-the-middle (MITM) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/46950.

**参考链接 / References**:
- http://secunia.com/advisories/46950
- http://www.securityfocus.com/bid/50754
- http://www.ubuntu.com/usn/USN-1270-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/71430
- http://secunia.com/advisories/46950

---

#### 424. CVE-2011-4405

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The cupshelpers scripts in system-config-printer in Ubuntu 11.04 and 11.10, as used by the automatic printer driver download service, uses an "insecure connection" for queries to the OpenPrinting database, which allows remote attackers to execute arbitrary code via a man-in-the-middle (MITM) attack that modifies packages or repositories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/77214.

**参考链接 / References**:
- http://osvdb.org/77214
- http://secunia.com/advisories/46909
- http://www.securityfocus.com/bid/50721
- http://www.ubuntu.com/usn/USN-1265-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/71394

---

#### 425. CVE-2012-0949

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The Apport hook in Update Manager as used by Ubuntu 12.04 LTS, 11.10, and 11.04 uploads certain system state archive files when reporting bugs to Launchpad, which allows remote attackers to read repository credentials by viewing a public bug report.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/82020.

**参考链接 / References**:
- http://osvdb.org/82020
- http://secunia.com/advisories/49230
- http://www.securityfocus.com/bid/53605
- http://www.ubuntu.com/usn/USN-1443-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/75728

---

#### 426. CVE-2012-0944

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: canonical:ubuntu_linux, sebastian_heinlein:aptdaemon

**漏洞描述 / Description**:
Aptdaemon 0.43 and earlier in Ubuntu 11.04, 11.10, and 12.04 LTS does not authenticate packages when the transaction is not simulated, which allows remote attackers to install arbitrary packages via a man-in-the-middle attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/48688.

**参考链接 / References**:
- http://secunia.com/advisories/48688
- http://ubuntu.com/usn/usn-1414-1
- http://www.osvdb.org/80887
- http://www.securityfocus.com/bid/52855
- https://bugs.launchpad.net/ubuntu/%2Bsource/aptdaemon/%2Bbug/959131

---

#### 427. CVE-2012-0948

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: canonical:ubuntu_linux, gnome:update-manager-core

**漏洞描述 / Description**:
DistUpgrade/DistUpgradeMain.py in Update Manager, as used by Ubuntu 12.04 LTS, 11.10, and 11.04, uses weak permissions for (1) apt-clone_system_state.tar.gz and (2) system_state.tar.gz, which allows local users to obtain repository credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://launchpadlibrarian.net/105380733/update-manager_1%3A0.156.14.3_1%3A0.156.14.4.diff.gz.

**参考链接 / References**:
- http://launchpadlibrarian.net/105380733/update-manager_1%3A0.156.14.3_1%3A0.156.14.4.diff.gz
- http://osvdb.org/82019
- http://secunia.com/advisories/49230
- http://www.securityfocus.com/bid/53604
- http://www.ubuntu.com/usn/USN-1443-1

---

#### 428. CVE-2011-4408

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The Single Sign On Client (ubuntu-sso-client) for Ubuntu 11.04 and 11.10 does not properly validate SSL certificates when using HTTPS, which allows remote attackers to spoof a server and modify or read sensitive data via a man-in-the-middle (MITM) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/82747.

**参考链接 / References**:
- http://osvdb.org/82747
- http://secunia.com/advisories/49448
- http://www.securityfocus.com/bid/53829
- http://www.ubuntu.com/usn/USN-1464-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/76112

---

#### 429. CVE-2011-4409

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The Ubuntu One Client for Ubuntu 10.04 LTS, 11.04, 11.10, and 12.04 LTS does not properly validate SSL certificates, which allows remote attackers to spoof a server and modify or read sensitive information via a man-in-the-middle (MITM) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/49442.

**参考链接 / References**:
- http://secunia.com/advisories/49442
- http://ubuntu.com/usn/usn-1465-1
- http://ubuntu.com/usn/usn-1465-2
- http://ubuntu.com/usn/usn-1465-3
- http://www.osvdb.org/82748

---

#### 430. CVE-2012-0950

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The Apport hook (DistUpgradeApport.py) in Update Manager, as used by Ubuntu 12.04 LTS, 11.10, and 11.04, uploads the /var/log/dist-upgrade directory when reporting bugs to Launchpad, which allows remote attackers to read repository credentials by viewing a public bug report.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2012-0949.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-1443-2.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1443-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/1004503
- http://www.ubuntu.com/usn/USN-1443-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/1004503

---

#### 431. CVE-2012-2317

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: debian:debian_linux, canonical:ubuntu_linux, canonical:php5, debian:php5-common

**漏洞描述 / Description**:
The Debian php_crypt_revamped.patch patch for PHP 5.3.x, as used in the php5 package before 5.3.3-7+squeeze4 in Debian GNU/Linux squeeze, the php5 package before 5.3.2-1ubuntu4.17 in Ubuntu 10.04 LTS, and the php5 package before 5.3.5-1ubuntu7.10 in Ubuntu 11.04, does not properly handle an empty salt string, which might allow remote attackers to bypass authentication by leveraging an application that relies on the PHP crypt function to choose a salt for password hashing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=581170.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=581170
- http://www.openwall.com/lists/oss-security/2012/05/04/7
- http://www.openwall.com/lists/oss-security/2012/05/05/2
- http://www.ubuntu.com/usn/USN-1481-1
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=581170

---

#### 432. CVE-2012-5356

**严重程度 / Severity**: N/A | CVSS: 5.8
**受影响产品 / Affected Products**: canonical:ubuntu_software_properties

**漏洞描述 / Description**:
The apt-add-repository tool in Ubuntu Software Properties 0.75.x before 0.75.10.3, 0.80.x before 0.80.9.2, 0.81.x before 0.81.13.5, 0.82.x before 0.82.7.3, and 0.92.x before 0.92.8 does not properly check PPA GPG keys imported from a keyserver, which allows remote attackers to install arbitrary package repository GPG keys via a man-in-the-middle (MITM) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/55736.

**参考链接 / References**:
- http://www.securityfocus.com/bid/55736
- http://www.ubuntu.com/usn/USN-1588-1
- https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1016643
- https://exchange.xforce.ibmcloud.com/vulnerabilities/78990
- http://www.securityfocus.com/bid/55736

---

#### 433. CVE-2012-0961

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:advanced_package_tool, debian:apt

**漏洞描述 / Description**:
Apt 0.8.16~exp5ubuntu13.x before 0.8.16~exp5ubuntu13.6, 0.8.16~exp12ubuntu10.x before 0.8.16~exp12ubuntu10.7, and 0.9.7.5ubuntu5.x before 0.9.7.5ubuntu5.2, as used in Ubuntu, uses world-readable permissions for /var/log/apt/term.log, which allows local users to obtain sensitive shell information by reading the log file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/88380.

**参考链接 / References**:
- http://osvdb.org/88380
- http://secunia.com/advisories/51568
- http://www.securityfocus.com/bid/56917
- http://www.ubuntu.com/usn/USN-1662-1
- http://osvdb.org/88380

---

#### 434. CVE-2012-0962

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: canonical:ubuntu_linux, sebastian_heinlein:aptdaemon

**漏洞描述 / Description**:
Aptdaemon 0.43 in Ubuntu 11.10 and 12.04 LTS uses short IDs when importing PPA GPG keys from a keyserver, which allows remote attackers to install arbitrary package repository GPG keys via a man-in-the-middle (MITM) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/51627.

**参考链接 / References**:
- http://secunia.com/advisories/51627
- http://www.securityfocus.com/bid/56959
- http://www.securitytracker.com/id?1027891
- http://www.ubuntu.com/usn/USN-1666-1
- https://bugs.launchpad.net/software-center-agent/%2Bbug/1052789

---

#### 435. CVE-2013-1052

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
pam-xdg-support, as used in Ubuntu 12.10, does not properly handle the PATH environment variable, which allows local users to gain privileges via unspecified vectors related to sudo.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/58550.

**参考链接 / References**:
- http://www.securityfocus.com/bid/58550
- http://www.ubuntu.com/usn/USN-1766-1
- https://exchange.xforce.ibmcloud.com/vulnerabilities/82918
- http://www.securityfocus.com/bid/58550
- http://www.ubuntu.com/usn/USN-1766-1

---

#### 436. CVE-2013-2162

**严重程度 / Severity**: N/A | CVSS: 1.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
Race condition in the post-installation script (mysql-server-5.5.postinst) for MySQL Server 5.5 for Debian GNU/Linux and Ubuntu Linux creates a configuration file with world-readable permissions before restricting the permissions, which allows local users to read the file and obtain sensitive information such as credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=711600.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=711600
- http://seclists.org/oss-sec/2013/q2/528
- http://secunia.com/advisories/54300
- http://ubuntu.com/usn/usn-1909-1
- http://www.debian.org/security/2013/dsa-2818

---

#### 437. CVE-2013-1060

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
A certain Ubuntu build procedure for perf, as distributed in the Linux kernel packages in Ubuntu 10.04 LTS, 12.04 LTS, 12.10, 13.04, and 13.10, sets the HOME environment variable to the ~buildd directory and consequently reads the system configuration file from the ~buildd directory, which allows local users to gain privileges by leveraging control over the buildd account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://people.canonical.com/~ubuntu-security/cve/2013/CVE-2013-1060.html.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2013/CVE-2013-1060.html
- http://www.ubuntu.com/usn/USN-1938-1
- http://www.ubuntu.com/usn/USN-1939-1
- http://www.ubuntu.com/usn/USN-1941-1
- http://www.ubuntu.com/usn/USN-1942-1

---

#### 438. CVE-2013-1062

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: michael_vogt:ubuntu-system-service, canonical:ubuntu_linux

**漏洞描述 / Description**:
ubuntu-system-service 0.2.4 before 0.2.4.1. 0.2.3 before 0.2.3.1, and 0.2.2 before 0.2.2.1 does not properly use D-Bus for communication with a polkit authority, which allows local users to bypass intended access restrictions by leveraging a PolkitUnixProcess PolkitSubject race condition via a (1) setuid process or (2) pkexec process, a related issue to CVE-2013-4288.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/54907.

**参考链接 / References**:
- http://secunia.com/advisories/54907
- http://www.ubuntu.com/usn/USN-1962-1
- http://secunia.com/advisories/54907
- http://www.ubuntu.com/usn/USN-1962-1

---

#### 439. CVE-2011-4613

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: ubuntu:linux, debian:debian_linux, canonical:ubuntu_linux, x.org:x_server

**漏洞描述 / Description**:
The X.Org X wrapper (xserver-wrapper.c) in Debian GNU/Linux and Ubuntu Linux does not properly verify the TTY of a user who is starting X, which allows local users to bypass intended access restrictions by associating stdin with a file that is misinterpreted as the console TTY.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=652249.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=652249
- http://www.debian.org/security/2011/dsa-2364
- http://www.ubuntu.com/usn/USN-1349-1
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=652249
- http://www.debian.org/security/2011/dsa-2364

---

#### 440. CVE-2013-1069

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: ubuntu:metal_as_a_service

**漏洞描述 / Description**:
Ubuntu Metal as a Service (MaaS) 1.2 and 1.4 uses world-readable permissions for txlongpoll.yaml, which allows local users to obtain RabbitMQ authentication credentials by reading the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2105-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/maas/%2Bbug/1254034
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/maas/%2Bbug/1254034

---

#### 441. CVE-2013-1070

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: ubuntu:metal_as_a_service

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in the API in Ubuntu Metal as a Service (MaaS) 1.2 and 1.4 allows remote attackers to inject arbitrary web script or HTML via the op parameter to nodes/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/65575.

**参考链接 / References**:
- http://www.securityfocus.com/bid/65575
- http://www.ubuntu.com/usn/USN-2105-1
- https://bugs.launchpad.net/maas/%2Bbug/1251336
- http://www.securityfocus.com/bid/65575
- http://www.ubuntu.com/usn/USN-2105-1

---

#### 442. CVE-2011-3628

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux, canonical:libpam-modules

**漏洞描述 / Description**:
Untrusted search path vulnerability in pam_motd (aka the MOTD module) in libpam-modules before 1.1.3-2ubuntu2.1 on Ubuntu 11.10, before 1.1.2-2ubuntu8.4 on Ubuntu 11.04, before 1.1.1-4ubuntu2.4 on Ubuntu 10.10, before 1.1.1-2ubuntu5.4 on Ubuntu 10.04 LTS, and before 0.99.7.1-5ubuntu6.5 on Ubuntu 8.04 LTS, when using certain configurations such as "session optional pam_motd.so", allows local users to gain privileges by modifying the PATH environment variable to reference a malicious command, as demonstrated via uname.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-1237-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1237-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/pam/%2Bbug/610125
- http://www.ubuntu.com/usn/USN-1237-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/pam/%2Bbug/610125

---

#### 443. CVE-2011-4406

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: canonical:ubuntu_linux, canonical:accountsservice

**漏洞描述 / Description**:
The Ubuntu AccountsService package before 0.6.14-1git1ubuntu1.1 does not properly drop privileges when changing language settings, which allows local users to modify arbitrary files via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/oneiric/accountsservice/oneiric-updates/revision/21.

**参考链接 / References**:
- http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/oneiric/accountsservice/oneiric-updates/revision/21
- http://people.canonical.com/~ubuntu-security/cve/2011/CVE-2011-4406.html
- http://www.ubuntu.com/usn/USN-1351-1
- http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/oneiric/accountsservice/oneiric-updates/revision/21
- http://people.canonical.com/~ubuntu-security/cve/2011/CVE-2011-4406.html

---

#### 444. CVE-2011-3152

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: canonical:ubuntu_linux, canonical:update-manager

**漏洞描述 / Description**:
DistUpgrade/DistUpgradeFetcherCore.py in Update Manager before 1:0.87.31.1, 1:0.134.x before 1:0.134.11.1, 1:0.142.x before 1:0.142.23.1, 1:0.150.x before 1:0.150.5.1, and 1:0.152.x before 1:0.152.25.5 on Ubuntu 8.04 through 11.10 does not verify the GPG signature before extracting an upgrade tarball, which allows man-in-the-middle attackers to (1) create or overwrite arbitrary files via a directory traversal attack using a crafted tar file, or (2) bypass authentication via a crafted meta-release file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/47024.

**参考链接 / References**:
- http://secunia.com/advisories/47024
- http://www.osvdb.org/77642
- http://www.securityfocus.com/bid/50833
- http://www.ubuntu.com/usn/USN-1284-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/update-manager/%2Bbug/881548

---

#### 445. CVE-2013-7374

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The Ubuntu Date and Time Indicator (aka indicator-datetime) 13.10.0+13.10.x before 13.10.0+13.10.20131023.2-0ubuntu1.1 does not properly restrict access to Evolution, which allows local users to bypass the greeter screen restrictions by clicking the date.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bazaar.launchpad.net/~indicator-applet-developers/indicator-datetime/trunk.13.10/revision/282.

**参考链接 / References**:
- http://bazaar.launchpad.net/~indicator-applet-developers/indicator-datetime/trunk.13.10/revision/282
- http://www.openwall.com/lists/oss-security/2014/04/29/3
- http://www.openwall.com/lists/oss-security/2014/04/30/1
- http://www.ubuntu.com/usn/USN-2186-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/indicator-datetime/%2Bbug/1246812

---

#### 446. CVE-2014-3203

**严重程度 / Severity**: N/A | CVSS: 4.4
**受影响产品 / Affected Products**: canonical:ubuntu_linux, ayatana_project:unity

**漏洞描述 / Description**:
Unity before 7.2.1, as used in Ubuntu 14.04, does not properly restrict access to the Dash when the lock screen is active, which allows physically proximate attackers to bypass the lock screen and execute arbitrary commands, as demonstrated by pressing the SUPER key before the screen auto-locks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ubuntu.com/usn/usn-2184-1.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2184-1
- http://www.openwall.com/lists/oss-security/2014/04/29/2
- http://www.openwall.com/lists/oss-security/2014/05/03/1
- https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1308850
- http://ubuntu.com/usn/usn-2184-1

---

#### 447. CVE-2014-3204

**严重程度 / Severity**: N/A | CVSS: 4.4
**受影响产品 / Affected Products**: canonical:ubuntu_linux, ayatana_project:unity

**漏洞描述 / Description**:
Unity before 7.2.1, as used in Ubuntu 14.04, does not properly handle keyboard shortcuts, which allows physically proximate attackers to bypass the lock screen and execute arbitrary commands, as demonstrated by right-clicking on the indicator bar and then pressing the ALT and F2 keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ubuntu.com/usn/usn-2184-1.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2184-1
- http://www.openwall.com/lists/oss-security/2014/04/29/2
- http://www.openwall.com/lists/oss-security/2014/05/03/1
- http://www.securityfocus.com/bid/67117
- https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1313885

---

#### 448. CVE-2014-0462

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux, oracle:openjdk

**漏洞描述 / Description**:
Unspecified vulnerability in OpenJDK 6 before 6b31 on Debian GNU/Linux and Ubuntu 12.04 LTS and 10.04 LTS has unknown impact and attack vectors, a different vulnerability than CVE-2014-2405.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/58415.

**参考链接 / References**:
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912
- http://www.ubuntu.com/usn/USN-2191-1
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912

---

#### 449. CVE-2014-2405

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux, oracle:openjdk

**漏洞描述 / Description**:
Unspecified vulnerability in OpenJDK 6 before 6b31 on Debian GNU/Linux and Ubuntu 12.04 LTS and 10.04 LTS has unknown impact and attack vectors, a different vulnerability than CVE-2014-0462.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/58415.

**参考链接 / References**:
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912
- http://www.ubuntu.com/usn/USN-2191-1
- http://secunia.com/advisories/58415
- http://www.debian.org/security/2014/dsa-2912

---

#### 450. CVE-2012-0943

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: canonical:ubuntu_linux, robert_ancell:lightdm

**漏洞描述 / Description**:
debian/guest-account in Light Display Manager (lightdm) 1.0.x before 1.0.6 and 1.1.x before 1.1.7, as used in Ubuntu Linux 11.10, allows local users to delete arbitrary files via a space in the name of a file in /tmp.  NOTE: this identifier was SPLIT per ADT1/ADT2 due to different codebases and affected versions. CVE-2012-6648 has been assigned for the gdm-guest-session issue.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-1399-2.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-1399-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044
- https://launchpadlibrarian.net/96471251/lightdm.secure-cleanup.debdiff
- http://www.ubuntu.com/usn/USN-1399-2
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044

---

#### 451. CVE-2012-6648

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: canonical:ubuntu_linux, gdm-guest-session_project:gdm-guest-session

**漏洞描述 / Description**:
gdm/guest-session-cleanup.sh in gdm-guest-session 0.24 and earlier, as used in Ubuntu Linux 10.04 LTS, 10.10, and 11.04, allows local users to delete arbitrary files via a space in the name of a file in /tmp. NOTE: this identifier was SPLIT from CVE-2012-0943 per ADT1/ADT2 due to different codebases and affected versions. CVE-2012-0943 is used for the guest-account issue.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ubuntu.com/usn/usn-1399-1.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-1399-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044
- https://launchpadlibrarian.net/96474113/gdm-guest-session.secure-cleanup.debdiff
- http://ubuntu.com/usn/usn-1399-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/lightdm/%2Bbug/953044

---

#### 452. CVE-2013-1068

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The OpenStack Nova (python-nova) package 1:2013.2.3-0 before 1:2013.2.3-0ubuntu1.2 and 1:2014.1-0 before 1:2014.1-0ubuntu1.2 and Openstack Cinder (python-cinder) package 1:2013.2.3-0 before 1:2013.2.3-0ubuntu1.1 and 1:2014.1-0 before 1:2014.1-0ubuntu1.1 for Ubuntu 13.10 and 14.04 LTS does not properly set the sudo configuration, which makes it easier for attackers to gain privileges by leveraging another vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ubuntu.com/usn/usn-2248-1.

**参考链接 / References**:
- http://ubuntu.com/usn/usn-2248-1
- http://www.ubuntu.com/usn/USN-2247-1
- http://ubuntu.com/usn/usn-2248-1
- http://www.ubuntu.com/usn/USN-2247-1

---

#### 453. CVE-2014-5195

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: canonical:ubuntu_linux, ayatana_project:unity

**漏洞描述 / Description**:
Unity before 7.2.3 and 7.3.x before 7.3.1, as used in Ubuntu, does not properly take focus of the keyboard when switching to the lock screen, which allows physically proximate attackers to bypass the lock screen by (1) leveraging a machine that had text selected when locking or (2) resuming from a suspension.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/109788.

**参考链接 / References**:
- http://www.osvdb.org/109788
- http://www.securityfocus.com/bid/68987
- http://www.ubuntu.com/usn/USN-2303-1
- https://bugs.launchpad.net/unity/7.2/+bug/1349128
- https://exchange.xforce.ibmcloud.com/vulnerabilities/95199

---

#### 454. CVE-2014-1424

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: ubuntu:apparmor, canonical:ubuntu

**漏洞描述 / Description**:
apparmor_parser in the apparmor package before 2.8.95~2430-0ubuntu5.1 in Ubuntu 14.04 allows attackers to bypass AppArmor policies via unspecified vectors, related to a "miscompilation flaw."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2413-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2413-1
- http://www.ubuntu.com/usn/USN-2413-1

---

#### 455. CVE-2014-1421

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
mountall 1.54, as used in Ubuntu 14.10, does not properly handle the umask when using the mount utility, which allows local users to bypass intended access restrictions via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2411-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2411-1
- http://www.ubuntu.com/usn/USN-2411-1

---

#### 456. CVE-2015-2285

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ubuntu:vivid, ubuntu:upstart

**漏洞描述 / Description**:
The logrotation script (/etc/cron.daily/upstart) in the Ubuntu Upstart package before 1.13.2-0ubuntu9, as used in Ubuntu Vivid 15.04, allows local users to execute arbitrary commands and gain privileges via a crafted file in /run/user/*/upstart/sessions/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/130587/Ubuntu-Vivid-Upstart-Privilege-Escalation.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/130587/Ubuntu-Vivid-Upstart-Privilege-Escalation.html
- http://seclists.org/fulldisclosure/2015/Mar/7
- http://www.halfdog.net/Security/2015/UpstartLogrotationPrivilegeEscalation/
- https://bugs.launchpad.net/ubuntu/+source/upstart/+bug/1425685
- http://packetstormsecurity.com/files/130587/Ubuntu-Vivid-Upstart-Privilege-Escalation.html

---

#### 457. CVE-2015-1322

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: canonical:ubuntu_linux, ubuntu:network-manager

**漏洞描述 / Description**:
Directory traversal vulnerability in the Ubuntu network-manager package for Ubuntu (vivid) before 0.9.10.0-4ubuntu15.1, Ubuntu 14.10 before 0.9.8.8-0ubuntu28.1, and Ubuntu 14.04 LTS before 0.9.8.8-0ubuntu7.1 allows local users to change the modem device configuration or read arbitrary files via a .. (dot dot) in the file name in a request to read modem device contexts (com.canonical.NMOfono.ReadImsiContexts).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2581-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2581-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/network-manager/%2Bbug/1449245
- http://www.ubuntu.com/usn/USN-2581-1
- https://bugs.launchpad.net/ubuntu/%2Bsource/network-manager/%2Bbug/1449245

---

#### 458. CVE-2015-8222

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The lxd-unix.socket systemd unit file in the Ubuntu lxd package before 0.20-0ubuntu4.1 uses world-readable permissions for /var/lib/lxd/unix.socket, which allows local users to gain privileges via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2809-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2809-1
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1515689
- https://github.com/lxc/lxd/issues/1307
- http://www.ubuntu.com/usn/USN-2809-1
- https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1515689

---

#### 459. CVE-2016-2856

**严重程度 / Severity**: HIGH | CVSS: 8.4
**受影响产品 / Affected Products**: canonical:ubuntu_linux, gnu:glibc, debian:debian_linux

**漏洞描述 / Description**:
pt_chown in the glibc package before 2.19-18+deb8u4 on Debian jessie; the elibc package before 2.15-0ubuntu10.14 on Ubuntu 12.04 LTS and before 2.19-0ubuntu6.8 on Ubuntu 14.04 LTS; and the glibc package before 2.21-0ubuntu4.2 on Ubuntu 15.10 and before 2.23-0ubuntu1 on Ubuntu 16.04 LTS and 16.10 lacks a namespace check associated with file-descriptor passing, which allows local users to capture keystrokes and spoof data, and possibly gain privileges, via pts read and write operations, related to debian/sysdeps/linux.mk.  NOTE: this is not considered a vulnerability in the upstream GNU C Library because the upstream documentation has a clear security recommendation against the --enable-pt_chown option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://anonscm.debian.org/cgit/pkg-glibc/glibc.git/commit/?h=jessie&id=09f7764882a81e13e7b5d87d715412283a6ce403.

**参考链接 / References**:
- http://anonscm.debian.org/cgit/pkg-glibc/glibc.git/commit/?h=jessie&id=09f7764882a81e13e7b5d87d715412283a6ce403
- http://anonscm.debian.org/cgit/pkg-glibc/glibc.git/commit/?h=jessie&id=11475c083282c1582c4dd72eecfcb2b7d308c958
- http://people.canonical.com/~ubuntu-security/cve/2016/CVE-2016-2856.html
- http://www.halfdog.net/Security/2015/PtChownArbitraryPtsAccessViaUserNamespace/
- http://www.openwall.com/lists/oss-security/2016/02/23/3

---

#### 460. CVE-2016-1580

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, canonical:ubuntu-core-launcher

**漏洞描述 / Description**:
The setup_snappy_os_mounts function in the ubuntu-core-launcher package before 1.0.27.1 improperly determines the mount point of bind mounts when using snaps, which might allow remote attackers to obtain sensitive information or gain privileges via a snap with a name starting with "ubuntu-core."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-2956-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-2956-1
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-core-launcher/+bug/1576699
- http://www.ubuntu.com/usn/USN-2956-1
- https://bugs.launchpad.net/ubuntu/+source/ubuntu-core-launcher/+bug/1576699

---

#### 461. CVE-2016-1240

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, apache:tomcat, debian:debian_linux

**漏洞描述 / Description**:
The Tomcat init script in the tomcat7 package before 7.0.56-3+deb8u4 and tomcat8 package before 8.0.14-1+deb8u3 on Debian jessie and the tomcat6 and libtomcat6-java packages before 6.0.35-1ubuntu3.8 on Ubuntu 12.04 LTS, the tomcat7 and libtomcat7-java packages before 7.0.52-1ubuntu0.7 on Ubuntu 14.04 LTS, and tomcat8 and libtomcat8-java packages before 8.0.32-1ubuntu1.2 on Ubuntu 16.04 LTS allows local users with access to the tomcat account to gain root privileges via a symlink attack on the Catalina log file, as demonstrated by /var/log/tomcat7/catalina.out.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://legalhackers.com/advisories/Tomcat-DebPkgs-Root-Privilege-Escalation-Exploit-CVE-2016-1240.html.

**参考链接 / References**:
- http://legalhackers.com/advisories/Tomcat-DebPkgs-Root-Privilege-Escalation-Exploit-CVE-2016-1240.html
- http://packetstormsecurity.com/files/170857/Apache-Tomcat-On-Ubuntu-Log-Init-Privilege-Escalation.html
- http://rhn.redhat.com/errata/RHSA-2017-0457.html
- http://www.debian.org/security/2016/dsa-3669
- http://www.debian.org/security/2016/dsa-3670

---

#### 462. CVE-2015-1328

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, linux:linux_kernel

**漏洞描述 / Description**:
The overlayfs implementation in the linux (aka Linux kernel) package before 3.19.0-21.21 in Ubuntu through 15.04 does not properly check permissions for file creation in the upper filesystem directory, which allows local users to obtain root access by leveraging a configuration in which overlayfs is permitted in an arbitrary mount namespace.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://seclists.org/oss-sec/2015/q2/717.

**参考链接 / References**:
- http://seclists.org/oss-sec/2015/q2/717
- http://www.exploit-db.com/exploits/40688/
- http://www.securityfocus.com/bid/75206
- https://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1328.html
- https://security-tracker.debian.org/tracker/CVE-2015-1328

---

#### 463. CVE-2016-1247

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, fedoraproject:fedora, debian:debian_linux, f5:nginx

**漏洞描述 / Description**:
The nginx package before 1.6.2-5+deb8u3 on Debian jessie, the nginx packages before 1.4.6-1ubuntu3.6 on Ubuntu 14.04 LTS, before 1.10.0-0ubuntu0.16.04.3 on Ubuntu 16.04 LTS, and before 1.10.1-0ubuntu1.1 on Ubuntu 16.10, and the nginx ebuild before 1.10.2-r3 on Gentoo allow local users with access to the web server user account to gain root privileges via a symlink attack on the error log.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/139750/Nginx-Debian-Based-Distros-Root-Privilege-Escalation.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/139750/Nginx-Debian-Based-Distros-Root-Privilege-Escalation.html
- http://seclists.org/fulldisclosure/2016/Nov/78
- http://seclists.org/fulldisclosure/2017/Jan/33
- http://www.debian.org/security/2016/dsa-3701
- http://www.securityfocus.com/archive/1/539796/100/0/threaded

---

#### 464. CVE-2015-8768

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: click_project:click, canonical:ubuntu_linux

**漏洞描述 / Description**:
click/install.py in click does not require files in package filesystem tarballs to start with ./ (dot slash), which allows remote attackers to install an alternate security policy and gain privileges via a crafted package, as demonstrated by the test.mmrow app for Ubuntu phone.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bazaar.launchpad.net/~click-hackers/click/devel/revision/587.

**参考链接 / References**:
- http://bazaar.launchpad.net/~click-hackers/click/devel/revision/587
- http://ubuntu.com/usn/usn-2771-1
- http://www.openwall.com/lists/oss-security/2016/01/12/8
- http://www.securityfocus.com/bid/96386
- https://bugs.launchpad.net/ubuntu/+source/click/+bug/1506467

---

#### 465. CVE-2017-6056

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux

**漏洞描述 / Description**:
It was discovered that a programming error in the processing of HTTPS requests in the Apache Tomcat servlet and JSP engine may result in denial of service via an infinite loop. The denial of service is easily achievable as a consequence of backporting a CVE-2016-6816 fix but not backporting the fix for Tomcat bug 57544. Distributions affected by this backporting issue include Debian (before 7.0.56-3+deb8u8 and 8.0.14-1+deb8u7 in jessie) and Ubuntu.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://rhn.redhat.com/errata/RHSA-2017-0517.html.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2017-0517.html
- http://rhn.redhat.com/errata/RHSA-2017-0826.html
- http://rhn.redhat.com/errata/RHSA-2017-0827.html
- http://rhn.redhat.com/errata/RHSA-2017-0828.html
- http://rhn.redhat.com/errata/RHSA-2017-0829.html

---

#### 466. CVE-2017-6590

**严重程度 / Severity**: MEDIUM | CVSS: 6.3
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
An issue was discovered in network-manager-applet (aka network-manager-gnome) in Ubuntu 12.04 LTS, 14.04 LTS, 16.04 LTS, and 16.10. A local attacker could use this issue at the default Ubuntu login screen to access local files and execute arbitrary commands as the lightdm user. The exploitation requires physical access to the locked computer and the Wi-Fi must be turned on. An access point that lets you use a certificate to login is required as well, but it's easy to create one. Then, it's possible to open a nautilus window and browse directories. One also can open some applications such as Firefox, which is useful for downloading malicious binaries.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1037977.

**参考链接 / References**:
- http://www.securitytracker.com/id/1037977
- https://bugs.launchpad.net/ubuntu/+source/network-manager-applet/+bug/1668321
- https://security.gentoo.org/glsa/201707-09
- https://www.ubuntu.com/usn/usn-3217-1/
- https://www.youtube.com/watch?v=Fp2lwRVg0l0

---

#### 467. CVE-2017-7184

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, linux:linux_kernel

**漏洞描述 / Description**:
The xfrm_replay_verify_len function in net/xfrm/xfrm_user.c in the Linux kernel through 4.10.6 does not validate certain size data after an XFRM_MSG_NEWAE update, which allows local users to obtain root privileges or cause a denial of service (heap-based out-of-bounds access) by leveraging the CAP_NET_ADMIN capability, as demonstrated during a Pwn2Own competition at CanSecWest 2017 for the Ubuntu 16.10 linux-image-* package 4.8.0.41.52.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=677e806da4d916052585301785d847c3b3e6186a.

**参考链接 / References**:
- http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=677e806da4d916052585301785d847c3b3e6186a
- http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=f843ee6dd019bcece3e74e76ad9df0155655d0df
- http://openwall.com/lists/oss-security/2017/03/29/2
- http://www.eweek.com/security/ubuntu-linux-falls-on-day-1-of-pwn2own-hacking-competition
- http://www.securityfocus.com/bid/97018

---

#### 468. CVE-2016-9774

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, apache:tomcat, debian:debian_linux

**漏洞描述 / Description**:
The postinst script in the tomcat6 package before 6.0.45+dfsg-1~deb7u4 on Debian wheezy, before 6.0.35-1ubuntu3.9 on Ubuntu 12.04 LTS and on Ubuntu 14.04 LTS; the tomcat7 package before 7.0.28-4+deb7u8 on Debian wheezy, before 7.0.56-3+deb8u6 on Debian jessie, before 7.0.52-1ubuntu0.8 on Ubuntu 14.04 LTS, and on Ubuntu 12.04 LTS, 16.04 LTS, and 16.10; and the tomcat8 package before 8.0.14-1+deb8u5 on Debian jessie, before 8.0.32-1ubuntu1.3 on Ubuntu 16.04 LTS, before 8.0.37-1ubuntu0.1 on Ubuntu 16.10, and before 8.0.38-2ubuntu1 on Ubuntu 17.04 might allow local users with access to the tomcat account to obtain sensitive information or gain root privileges via a symlink attack on the Catalina localhost directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2016/dsa-3738.

**参考链接 / References**:
- http://www.debian.org/security/2016/dsa-3738
- http://www.debian.org/security/2016/dsa-3739
- http://www.openwall.com/lists/oss-security/2016/12/02/10
- http://www.openwall.com/lists/oss-security/2016/12/02/5
- http://www.securityfocus.com/bid/94643

---

#### 469. CVE-2016-9775

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, apache:tomcat, debian:debian_linux

**漏洞描述 / Description**:
The postrm script in the tomcat6 package before 6.0.45+dfsg-1~deb7u3 on Debian wheezy, before 6.0.45+dfsg-1~deb8u1 on Debian jessie, before 6.0.35-1ubuntu3.9 on Ubuntu 12.04 LTS and on Ubuntu 14.04 LTS; the tomcat7 package before 7.0.28-4+deb7u7 on Debian wheezy, before 7.0.56-3+deb8u6 on Debian jessie, before 7.0.52-1ubuntu0.8 on Ubuntu 14.04 LTS, and on Ubuntu 12.04 LTS, 16.04 LTS, and 16.10; and the tomcat8 package before 8.0.14-1+deb8u5 on Debian jessie, before 8.0.32-1ubuntu1.3 on Ubuntu 16.04 LTS, before 8.0.37-1ubuntu0.1 on Ubuntu 16.10, and before 8.0.38-2ubuntu1 on Ubuntu 17.04 might allow local users with access to the tomcat account to gain root privileges via a setgid program in the Catalina directory, as demonstrated by /etc/tomcat8/Catalina/attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2016/dsa-3738.

**参考链接 / References**:
- http://www.debian.org/security/2016/dsa-3738
- http://www.debian.org/security/2016/dsa-3739
- http://www.openwall.com/lists/oss-security/2016/12/02/10
- http://www.openwall.com/lists/oss-security/2016/12/02/5
- http://www.securityfocus.com/bid/94643

---

#### 470. CVE-2017-6964

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux

**漏洞描述 / Description**:
dmcrypt-get-device, as shipped in the eject package of Debian and Ubuntu, does not check the return value of the (1) setuid or (2) setgid function, which might cause dmcrypt-get-device to execute code, which was intended to run as an unprivileged user, as root. This affects eject through 2.1.5+deb1+cvs20081104-13.1 on Debian, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.16.10.1 on Ubuntu 16.10, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.16.04.1 on Ubuntu 16.04 LTS, eject before 2.1.5+deb1+cvs20081104-13.1ubuntu0.14.04.1 on Ubuntu 14.04 LTS, and eject before 2.1.5+deb1+cvs20081104-9ubuntu0.1 on Ubuntu 12.04 LTS.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2017/dsa-3823.

**参考链接 / References**:
- http://www.debian.org/security/2017/dsa-3823
- http://www.securityfocus.com/bid/97154
- https://launchpad.net/bugs/1673627
- https://www.ubuntu.com/usn/usn-3246-1/
- https://www.debian.org/security/2017/dsa-3823

---

#### 471. CVE-2016-0727

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The crontab script in the ntp package before 1:4.2.6.p3+dfsg-1ubuntu3.11 on Ubuntu 12.04 LTS, before 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10 on Ubuntu 14.04 LTS, on Ubuntu Wily, and before 1:4.2.8p4+dfsg-3ubuntu5.3 on Ubuntu 16.04 LTS allows local users with access to the ntp account to write to arbitrary files and consequently gain privileges via vectors involving statistics directory cleanup.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/141913/NTP-Privilege-Escalation.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/141913/NTP-Privilege-Escalation.html
- http://www.securityfocus.com/bid/81552
- http://www.securitytracker.com/id/1034808
- http://www.ubuntu.com/usn/USN-3096-1
- https://bugs.launchpad.net/ubuntu/+source/ntp/+bug/1528050

---

#### 472. CVE-2017-8900

**严重程度 / Severity**: MEDIUM | CVSS: 4.6
**受影响产品 / Affected Products**: canonical:ubuntu_linux, lightdm_project:lightdm

**漏洞描述 / Description**:
LightDM through 1.22.0, when systemd is used in Ubuntu 16.10 and 17.x, allows physically proximate attackers to bypass intended AppArmor restrictions and visit the home directories of arbitrary users by establishing a guest session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98554.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98554
- https://launchpad.net/bugs/1663157
- https://people.canonical.com/~ubuntu-security/cve/2017/CVE-2017-8900.html
- https://www.ubuntu.com/usn/usn-3285-1/
- http://www.securityfocus.com/bid/98554

---

#### 473. CVE-2017-9525

**严重程度 / Severity**: MEDIUM | CVSS: 6.7
**受影响产品 / Affected Products**: canonical:ubuntu_linux, cron_project:cron, debian:debian_linux

**漏洞描述 / Description**:
In the cron package through 3.0pl1-128 on Debian, and through 3.0pl1-128ubuntu2 on Ubuntu, the postinst maintainer script allows for group-crontab-to-root privilege escalation via symlink attacks against unsafe usage of the chown and chmod programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/864466.

**参考链接 / References**:
- http://bugs.debian.org/864466
- http://www.openwall.com/lists/oss-security/2017/06/08/3
- http://www.securitytracker.com/id/1038651
- https://lists.debian.org/debian-lts-announce/2019/03/msg00025.html
- https://lists.debian.org/debian-lts-announce/2021/10/msg00029.html

---

#### 474. CVE-2017-10600

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: canonical:ubuntu-image

**漏洞描述 / Description**:
ubuntu-image 1.0 before 2017-07-07, when invoked as non-root, creates files in the resulting image with the uid of the invoking user. When the resulting image is booted, a local attacker with the same uid as the image creator has unintended access to cloud-init and snapd directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://forum.snapcraft.io/t/ownership-bug-in-ubuntu-image/1285.

**参考链接 / References**:
- https://forum.snapcraft.io/t/ownership-bug-in-ubuntu-image/1285
- https://forum.snapcraft.io/t/ownership-bug-in-ubuntu-image/1285

---

#### 475. CVE-2015-1323

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
The simulate dbus method in aptdaemon before 1.1.1+bzr982-0ubuntu3.1 as packaged in Ubuntu 15.04, before 1.1.1+bzr980-0ubuntu1.1 as packaged in Ubuntu 14.10, before 1.1.1-1ubuntu5.2 as packaged in Ubuntu 14.04 LTS, before 0.43+bzr805-0ubuntu10 as packaged in Ubuntu 12.04 LTS allows local users to obtain sensitive information, or access files with root permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/75221.

**参考链接 / References**:
- http://www.securityfocus.com/bid/75221
- http://www.ubuntu.com/usn/USN-2648-1
- http://www.securityfocus.com/bid/75221
- http://www.ubuntu.com/usn/USN-2648-1

---

#### 476. CVE-2015-1332

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, oxide_project:oxide

**漏洞描述 / Description**:
The oxide::JavaScriptDialogManager function in oxide-qt before 1.9.1 as packaged in Ubuntu 15.04 and Ubuntu 14.04 allows remote attackers to cause a denial of service (application crash) or execute arbitrary code via a crafted website.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1332.html.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1332.html
- http://www.securityfocus.com/bid/76710
- http://www.ubuntu.com/usn/USN-2735-1
- https://launchpad.net/ubuntu/+source/oxide-qt/1.9.1-0ubuntu0.15.04.1
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1332.html

---

#### 477. CVE-2015-1324

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
Apport before 2.17.2-0ubuntu1.1 as packaged in Ubuntu 15.04, before 2.14.70ubuntu8.5 as packaged in Ubuntu 14.10, before 2.14.1-0ubuntu3.11 as packaged in Ubuntu 14.04 LTS, and before 2.0.1-0ubuntu17.9 as packaged in Ubuntu 12.04 LTS allow local users to write to arbitrary files and gain root privileges by leveraging incorrect handling of permissions when generating core dumps for setuid binaries.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/74767.

**参考链接 / References**:
- http://www.securityfocus.com/bid/74767
- http://www.ubuntu.com/usn/USN-2609-1
- https://bugs.launchpad.net/ubuntu/+source/apport/+bug/1452239
- http://www.securityfocus.com/bid/74767
- http://www.ubuntu.com/usn/USN-2609-1

---

#### 478. CVE-2015-1325

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
Race condition in Apport before 2.17.2-0ubuntu1.1 as packaged in Ubuntu 15.04, before 2.14.70ubuntu8.5 as packaged in Ubuntu 14.10, before 2.14.1-0ubuntu3.11 as packaged in Ubuntu 14.04 LTS, and before 2.0.1-0ubuntu17.9 as packaged in Ubuntu 12.04 LTS allow local users to write to arbitrary files and gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.openwall.com/lists/oss-security/2015/05/21/10.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/05/21/10
- http://www.securityfocus.com/bid/74769
- http://www.ubuntu.com/usn/USN-2609-1
- https://www.exploit-db.com/exploits/37088/
- http://seclists.org/fulldisclosure/2025/Jun/9

---

#### 479. CVE-2015-1329

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux

**漏洞描述 / Description**:
Use-after-free vulnerability in oxide::qt::URLRequestDelegatedJob in oxide-qt in Ubuntu 15.04 and 14.04 LTS might allow remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1329.html.

**参考链接 / References**:
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1329.html
- http://www.securityfocus.com/bid/76174
- http://www.ubuntu.com/usn/USN-2677-1
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1329.html
- http://www.securityfocus.com/bid/76174

---

#### 480. CVE-2014-8156

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: fso-gsmd_project:fso-gsmd, fso-frameworkd_project:fso-frameworkd, phonefsod_project:phonefsod, debian:debian_linux, fso-usaged_project:fso-usaged

**漏洞描述 / Description**:
The D-Bus security policy files in /etc/dbus-1/system.d/*.conf in fso-gsmd 0.12.0-3, fso-frameworkd 0.9.5.9+git20110512-4, and fso-usaged 0.12.0-2 as packaged in Debian, the upstream cornucopia.git (fsoaudiod, fsodatad, fsodeviced, fsogsmd, fsonetworkd, fsotdld, fsousaged) git master on 2015-01-19, the upstream framework.git 0.10.1 and git master on 2015-01-19, phonefsod 0.1+git20121018-1 as packaged in Debian, Ubuntu and potentially other packages, and potentially other fso modules do not properly filter D-Bus message paths, which might allow local users to cause a denial of service (dbus-daemon memory consumption), or execute arbitrary code as root by sending a crafted D-Bus message to any D-Bus system service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.openwall.com/lists/oss-security/2015/01/27/25.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/01/27/25
- http://www.securityfocus.com/bid/72363
- https://exchange.xforce.ibmcloud.com/vulnerabilities/100488
- http://www.openwall.com/lists/oss-security/2015/01/27/25
- http://www.securityfocus.com/bid/72363

---

#### 481. CVE-2015-1336

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux, man-db_project:man-db

**漏洞描述 / Description**:
The daily mandb cleanup job in Man-db before 2.7.6.1-1 as packaged in Ubuntu and Debian allows local users with access to the man account to gain privileges via vectors involving insecure chown use.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/140759/Man-db-2.6.7.1-Privilege-Escalation.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/140759/Man-db-2.6.7.1-Privilege-Escalation.html
- http://people.canonical.com/~ubuntu-security/cve/2015/CVE-2015-1336.html
- http://www.halfdog.net/Security/2015/MandbSymlinkLocalRootPrivilegeEscalation/
- http://www.openwall.com/lists/oss-security/2015/12/14/11
- http://www.securityfocus.com/bid/79723

---

#### 482. CVE-2015-3643

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: usb-creator_project:usb-creator, canonical:ubuntu_linux

**漏洞描述 / Description**:
usb-creator before 0.2.38.3ubuntu0.1 on Ubuntu 12.04 LTS, before 0.2.56.3ubuntu0.1 on Ubuntu 14.04 LTS, before 0.2.62ubuntu0.3 on Ubuntu 14.10, and before 0.2.67ubuntu0.1 on Ubuntu 15.04 allows local users to gain privileges by leveraging a missing call check_polkit for the KVMTest method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.openwall.com/lists/oss-security/2015/04/22/12.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2015/04/22/12
- http://www.openwall.com/lists/oss-security/2015/05/04/3
- http://www.securityfocus.com/bid/74304
- https://bazaar.launchpad.net/~usb-creator-hackers/usb-creator/trunk/revision/470
- https://usn.ubuntu.com/usn/usn-2576-1/

---

#### 483. CVE-2011-2684

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: rkkda:foo2zjs

**漏洞描述 / Description**:
foo2zjs before 20110722dfsg-3ubuntu1 as packaged in Ubuntu, 20110722dfsg-1 as packaged in Debian unstable, and 20090908dfsg-5.1+squeeze0 as packaged in Debian squeeze create temporary files insecurely, which allows local users to write over arbitrary files via a symlink attack on /tmp/foo2zjs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.openwall.com/lists/oss-security/2011/07/06/10.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2011/07/06/10
- http://www.openwall.com/lists/oss-security/2014/02/08/5
- https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=633870
- https://bugs.launchpad.net/ubuntu/+source/foo2zjs/+bug/805370
- https://security-tracker.debian.org/tracker/CVE-2011-2684/

---

#### 484. CVE-2017-8806

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: postgresql:postgresql, debian:debian_linux, canonical:ubuntu_linux

**漏洞描述 / Description**:
The Debian pg_ctlcluster, pg_createcluster, and pg_upgradecluster scripts, as distributed in the Debian postgresql-common package before 181+deb9u1 for PostgreSQL (and other packages related to Debian and Ubuntu), handled symbolic links insecurely, which could result in local denial of service by overwriting arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://metadata.ftp-master.debian.org/changelogs/main/p/postgresql-common/postgresql-common_181+deb9u1_changelog.

**参考链接 / References**:
- http://metadata.ftp-master.debian.org/changelogs/main/p/postgresql-common/postgresql-common_181+deb9u1_changelog
- http://www.securityfocus.com/bid/101810
- https://usn.ubuntu.com/usn/usn-3476-1/
- https://www.debian.org/security/2017/dsa-4029
- http://metadata.ftp-master.debian.org/changelogs/main/p/postgresql-common/postgresql-common_181+deb9u1_changelog

---

#### 485. CVE-2017-14388

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: pivotal_software:grootfs

**漏洞描述 / Description**:
Cloud Foundry Foundation GrootFS release 0.3.x versions prior to 0.30.0 do not validate DiffIDs, allowing specially crafted images to poison the grootfs volume cache. For example, this could allow an attacker to provide an image layer that GrootFS would consider to be the Ubuntu base layer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cloudfoundry.org/cve-2017-14388/.

**参考链接 / References**:
- https://www.cloudfoundry.org/cve-2017-14388/
- https://www.cloudfoundry.org/cve-2017-14388/

---

#### 486. CVE-2016-1252

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:debian_linux, debian:advanced_package_tool

**漏洞描述 / Description**:
The apt package in Debian jessie before 1.0.9.8.4, in Debian unstable before 1.4~beta2, in Ubuntu 14.04 LTS before 1.0.1ubuntu2.17, in Ubuntu 16.04 LTS before 1.2.15ubuntu0.2, and in Ubuntu 16.10 before 1.3.2ubuntu0.1 allows man-in-the-middle attackers to bypass a repository-signing protection mechanism by leveraging improper error handling when validating InRelease file signatures.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/140145/apt-Repository-Signing-Bypass.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/140145/apt-Repository-Signing-Bypass.html
- http://www.ubuntu.com/usn/USN-3156-1
- https://bugs.chromium.org/p/project-zero/issues/detail?id=1020
- https://bugs.launchpad.net/ubuntu/+source/apt/+bug/1647467
- https://www.debian.org/security/2016/dsa-3733

---

#### 487. CVE-2016-1255

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: canonical:ubuntu_linux, debian:postgresql-common, debian:debian_linux

**漏洞描述 / Description**:
The pg_ctlcluster script in postgresql-common package in Debian wheezy before 134wheezy5, in Debian jessie before 165+deb8u2, in Debian unstable before 178, in Ubuntu 12.04 LTS before 129ubuntu1.2, in Ubuntu 14.04 LTS before 154ubuntu1.1, in Ubuntu 16.04 LTS before 173ubuntu0.1, in Ubuntu 17.04 before 179ubuntu0.1, and in Ubuntu 17.10 before 184ubuntu1.1 allows local users to gain root privileges via a symlink attack on a logfile in /var/log/postgresql.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ubuntu.com/usn/USN-3476-1.

**参考链接 / References**:
- http://www.ubuntu.com/usn/USN-3476-1
- http://www.ubuntu.com/usn/USN-3476-2
- https://anonscm.debian.org/cgit/pkg-postgresql/postgresql-common.git/commit/?id=c8989206ec360f199400c74f129f7b4cb878c1ee
- https://lists.debian.org/debian-lts-announce/2017/01/msg00002.html
- http://www.ubuntu.com/usn/USN-3476-1

---

#### 488. CVE-2018-1000135

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux, gnome:networkmanager

**漏洞描述 / Description**:
GNOME NetworkManager version 1.10.2 and earlier contains a Information Exposure (CWE-200) vulnerability in DNS resolver that can result in Private DNS queries leaked to local network's DNS servers, while on VPN. This vulnerability appears to have been fixed in Some Ubuntu 16.04 packages were fixed, but later updates removed the fix. cf. https://bugs.launchpad.net/ubuntu/+bug/1754671 an upstream fix does not appear to be available at this time.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00005.html.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00005.html
- http://www.securityfocus.com/bid/103478
- https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/1754671
- https://bugzilla.gnome.org/show_bug.cgi?id=746422
- https://bugzilla.redhat.com/show_bug.cgi?id=1553634

---

#### 489. CVE-2018-10768

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: canonical:ubuntu_linux, redhat:enterprise_linux_workstation, freedesktop:poppler, redhat:enterprise_linux_desktop, redhat:enterprise_linux_server

**漏洞描述 / Description**:
There is a NULL pointer dereference in the AnnotPath::getCoordsLength function in Annot.h in an Ubuntu package for Poppler 0.24.5. A crafted input will lead to a remote denial of service attack. Later Ubuntu packages such as for Poppler 0.41.0 are not affected.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://access.redhat.com/errata/RHBA-2019:0327.

**参考链接 / References**:
- https://access.redhat.com/errata/RHBA-2019:0327
- https://access.redhat.com/errata/RHSA-2018:3140
- https://access.redhat.com/errata/RHSA-2018:3505
- https://bugs.freedesktop.org/show_bug.cgi?id=106408
- https://lists.debian.org/debian-lts-announce/2018/10/msg00024.html

---

#### 490. CVE-1999-1572

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:enterprise_linux, freebsd:freebsd, mandrakesoft:mandrake_linux, redhat:enterprise_linux_desktop, debian:debian_linux

**漏洞描述 / Description**:
cpio on FreeBSD 2.1.0, Debian GNU/Linux 3.0, and possibly other operating systems, uses a 0 umask when creating files using the -O (archive) or -F options, which creates the files with mode 0666 and allows local users to read or overwrite those files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110763404701519&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=110763404701519&w=2
- http://secunia.com/advisories/14357
- http://secunia.com/advisories/17063
- http://secunia.com/advisories/17532
- http://support.avaya.com/elmodocs2/security/ASA-2005-212.pdf

---

#### 491. CVE-1999-1390

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
suidexec in suidmanager 0.18 on Debian 2.0 allows local users to gain root privileges by specifying a malicious program on the command line.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://darwin.bio.uci.edu/~mcoogan/bugtraq/msg00890.html.

**参考链接 / References**:
- http://darwin.bio.uci.edu/~mcoogan/bugtraq/msg00890.html
- http://www.securityfocus.com/bid/94
- http://darwin.bio.uci.edu/~mcoogan/bugtraq/msg00890.html
- http://www.securityfocus.com/bid/94

---

#### 492. CVE-1999-1411

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The installation of the fsp package 2.71-10 in Debian GNU/Linux 2.0 adds the anonymous FTP user without notifying the administrator, which could automatically enable anonymous FTP on some servers such as wu-ftp.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.debian.org/debian-security-announce/debian-security-announce-1998/msg00033.html.

**参考链接 / References**:
- http://lists.debian.org/debian-security-announce/debian-security-announce-1998/msg00033.html
- http://marc.info/?l=bugtraq&m=91228908407679&w=2
- http://marc.info/?l=bugtraq&m=91244712808780&w=2
- http://marc.info/?l=bugtraq&m=91936850009861&w=2
- http://www.iss.net/security_center/static/7574.php

---

#### 493. CVE-1999-0914

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in the FTP client in the Debian GNU/Linux netstd package.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/324.

**参考链接 / References**:
- http://www.securityfocus.com/bid/324
- http://www.securityfocus.com/bid/324

---

#### 494. CVE-1999-0678

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server, debian:debian_linux

**漏洞描述 / Description**:
A default configuration of Apache on Debian GNU/Linux sets the ServerRoot to /usr/doc, which allows remote users to read documentation files for the entire server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/318.

**参考链接 / References**:
- http://www.securityfocus.com/bid/318
- http://www.securityfocus.com/bid/318

---

#### 495. CVE-1999-0373

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in the "Super" utility in Debian GNU/Linux, and other operating systems, allows local users to execute commands as root.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0373.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0373
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0373

---

#### 496. CVE-1999-0374

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Debian GNU/Linux cfengine package is susceptible to a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0374.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0374
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0374

---

#### 497. CVE-2000-0367

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: michael_jennings:eterm

**漏洞描述 / Description**:
Vulnerability in eterm 0.8.8 in Debian GNU/Linux allows an attacker to gain root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/1999/19990218.

**参考链接 / References**:
- http://www.debian.org/security/1999/19990218
- http://www.debian.org/security/1999/19990218

---

#### 498. CVE-1999-0730

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The zsoelim program in the Debian man-db package allows local users to overwrite files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0730.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0730
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0730

---

#### 499. CVE-1999-0742

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The Debian mailman package uses weak authentication, which allows attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/480.

**参考链接 / References**:
- http://www.securityfocus.com/bid/480
- http://www.securityfocus.com/bid/480

---

#### 500. CVE-1999-0732

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The logging facility of the Debian smtp-refuser package allows local users to delete arbitrary files using symbolic links.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0732.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0732
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0732

---

#### 501. CVE-1999-0939

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Denial of service in Debian IRC Epic/epic4 client via a long string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/605.

**参考链接 / References**:
- http://www.securityfocus.com/bid/605
- http://www.securityfocus.com/bid/605

---

#### 502. CVE-2000-0366

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
dump in Debian GNU/Linux 2.1 does not properly restore symlinks, which allows a local user to modify the ownership of arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/1999/19991202.

**参考链接 / References**:
- http://www.debian.org/security/1999/19991202
- http://www.securityfocus.com/bid/1442
- http://www.debian.org/security/1999/19991202
- http://www.securityfocus.com/bid/1442

---

#### 503. CVE-2000-0076

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux, berkeley:nvi

**漏洞描述 / Description**:
nviboot boot script in the Debian nvi package allows local users to delete files via malformed entries in vi.recover.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94709988232618&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94709988232618&w=2
- http://www.securityfocus.com/bid/1439
- http://marc.info/?l=bugtraq&m=94709988232618&w=2
- http://www.securityfocus.com/bid/1439

---

#### 504. CVE-2000-0112

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The default installation of Debian GNU/Linux uses an insecure Master Boot Record (MBR) which allows a local user to boot from a floppy disk during the installation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94973075614088&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94973075614088&w=2
- http://www.securityfocus.com/bid/960
- http://marc.info/?l=bugtraq&m=94973075614088&w=2
- http://www.securityfocus.com/bid/960

---

#### 505. CVE-2000-0145

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
The libguile.so library file used by gnucash in Debian GNU/Linux is installed with world-writable permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0145.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0145
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0145

---

#### 506. CVE-2000-1135

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
fshd (fsh daemon) in Debian GNU/Linux allows local users to overwrite files of other users via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2000/20001130.

**参考链接 / References**:
- http://www.debian.org/security/2000/20001130
- http://www.osvdb.org/7208
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5633
- http://www.debian.org/security/2000/20001130
- http://www.osvdb.org/7208

---

#### 507. CVE-2001-0069

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
dialog before 0.9a-20000118-3bis in Debian GNU/Linux allows local users to overwrite arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2000/20001225.

**参考链接 / References**:
- http://www.debian.org/security/2000/20001225
- http://www.securityfocus.com/bid/2151
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5809
- http://www.debian.org/security/2000/20001225
- http://www.securityfocus.com/bid/2151

---

#### 508. CVE-2001-0195

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
sash before 3.4-4 in Debian GNU/Linux does not properly clone /etc/shadow, which makes it world-readable and could allow local users to gain privileges via password cracking.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2001/dsa-015.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5994
- http://www.debian.org/security/2001/dsa-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5994

---

#### 509. CVE-2001-0456

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
postinst installation script for Proftpd in Debian 2.2 does not properly change the "run as uid/gid root" configuration when the user enables anonymous access, which causes the server to run at a higher privilege than intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2001/dsa-032.

**参考链接 / References**:
- http://www.debian.org/security/2001/dsa-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6208
- http://www.debian.org/security/2001/dsa-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6208

---

#### 510. CVE-2001-0690

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: university_of_cambridge:exim, conectiva:linux, debian:debian_linux, redhat:linux

**漏洞描述 / Description**:
Format string vulnerability in exim (3.22-10 in Red Hat, 3.12 in Debian and 3.16 in Conectiva) in batched SMTP mode allows a remote attacker to execute arbitrary code via format strings in SMTP mail headers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-06/0041.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-06/0041.html
- http://distro.conectiva.com.br/atualizacoes/?id=a&anuncio=000402
- http://www.debian.org/security/2001/dsa-058
- http://www.redhat.com/support/errata/RHSA-2001-078.html
- http://www.securityfocus.com/bid/2828

---

#### 511. CVE-2001-0755

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Buffer overflow in ftp daemon (ftpd) 6.2 in Debian GNU/Linux allows attackers to cause a denial of service and possibly execute arbitrary code via a long SITE command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-05/0188.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0188.html
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0188.html

---

#### 512. CVE-2002-0660

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: greg_roelofs:libpng, greg_roelofs:libpng3

**漏洞描述 / Description**:
Buffer overflow in libpng 1.0.12-3.woody.2 and libpng3 1.2.1-1.1.woody.2 on Debian GNU/Linux 3.0, and other operating systems, may allow attackers to cause a denial of service and possibly execute arbitrary code, a different vulnerability than CVE-2002-0728.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://rhn.redhat.com/errata/RHSA-2002-151.html.

**参考链接 / References**:
- http://rhn.redhat.com/errata/RHSA-2002-151.html
- http://rhn.redhat.com/errata/RHSA-2002-152.html
- https://www.debian.org/security/2002/dsa-140
- http://rhn.redhat.com/errata/RHSA-2002-151.html
- http://rhn.redhat.com/errata/RHSA-2002-152.html

---

#### 513. CVE-2002-0912

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
in.uucpd UUCP server in Debian GNU/Linux 2.2, and possibly other operating systems, does not properly terminate long strings, which allows remote attackers to cause a denial of service, possibly due to a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2002/dsa-129.

**参考链接 / References**:
- http://www.debian.org/security/2002/dsa-129
- http://www.iss.net/security_center/static/9230.php
- http://www.securityfocus.com/bid/4910
- http://www.debian.org/security/2002/dsa-129
- http://www.iss.net/security_center/static/9230.php

---

#### 514. CVE-2002-1233

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apache:http_server

**漏洞描述 / Description**:
A regression error in the Debian distributions of the apache-ssl package (before 1.3.9 on Debian 2.2, and before 1.3.26 on Debian 3.0), for Apache 1.3.27 and earlier, allows local users to read or modify the Apache password file via a symlink attack on temporary files when the administrator runs (1) htpasswd or (2) htdigest, a re-introduction of a vulnerability that was originally identified and addressed by CVE-2001-0131.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103480856102007&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103480856102007&w=2
- http://www.debian.org/security/2002/dsa-187
- http://www.debian.org/security/2002/dsa-188
- http://www.debian.org/security/2002/dsa-195
- http://www.iss.net/security_center/static/10412.php

---

#### 515. CVE-2003-0308

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: sendmail:sendmail, debian:debian_linux

**漏洞描述 / Description**:
The Sendmail 8.12.3 package in Debian GNU/Linux 3.0 does not securely create temporary files, which could allow local users to gain additional privileges via (1) expn, (2) checksendmail, or (3) doublebounce.pl.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/496408.

**参考链接 / References**:
- http://bugs.debian.org/496408
- http://dev.gentoo.org/~rbu/security/debiantemp/sendmail-base
- http://www.debian.org/security/2003/dsa-305
- http://www.openwall.com/lists/oss-security/2008/10/30/2
- https://bugs.gentoo.org/show_bug.cgi?id=235770

---

#### 516. CVE-2003-0262

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: leksbot:leksbot

**漏洞描述 / Description**:
leksbot 1.2.3 in Debian GNU/Linux installs the KATAXWR as setuid root, which allows local users to gain root privileges by exploiting unknown vulnerabilities related to the escalated privileges, which KATAXWR is not designed to have.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-299.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-299
- http://www.securityfocus.com/bid/7505
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11945
- http://www.debian.org/security/2003/dsa-299
- http://www.securityfocus.com/bid/7505

---

#### 517. CVE-2003-0828

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: gus_and_psilord:freesweep

**漏洞描述 / Description**:
Buffer overflow in freesweep in Debian GNU/Linux 3.0 allows local users to gain "games" group privileges when processing environment variables.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2003/dsa-391.

**参考链接 / References**:
- http://www.debian.org/security/2003/dsa-391
- http://www.securityfocus.com/bid/8716
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13301
- http://www.debian.org/security/2003/dsa-391
- http://www.securityfocus.com/bid/8716

---

#### 518. CVE-2004-0911

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:netkit

**漏洞描述 / Description**:
telnetd for netkit 0.17 and earlier, and possibly other versions, on Debian GNU/Linux allows remote attackers to cause a denial of service (free of an invalid pointer), a different vulnerability than CVE-2001-0554.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=273694.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=273694
- http://www.debian.org/security/2004/dsa-556
- http://www.securityfocus.com/archive/1/375743
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17540
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=273694

---

#### 519. CVE-2004-0563

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: freenet6:freenet6

**漏洞描述 / Description**:
The tspc.conf configuration file in freenet6 before 0.9.6 and before 1.0 on Debian Linux has world readable permissions, which could allow local users to gain sensitive information, such as a username and password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12705/.

**参考链接 / References**:
- http://secunia.com/advisories/12705/
- http://securitytracker.com/id?1011460
- http://www.debian.org/security/2004/dsa-555
- http://www.securityfocus.com/bid/11280
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17544

---

#### 520. CVE-2004-0833

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Sendmail before 8.12.3 on Debian GNU/Linux, when using sasl and sasl-bin, uses a Sendmail configuration script with a fixed username and password, which could allow remote attackers to use Sendmail as an open mail relay and send spam messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12667.

**参考链接 / References**:
- http://secunia.com/advisories/12667
- http://www.debian.org/security/2004/dsa-554
- http://www.securityfocus.com/bid/11262
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17531
- http://secunia.com/advisories/12667

---

#### 521. CVE-2004-0984

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: gnu:mailutils

**漏洞描述 / Description**:
Unknown vulnerability in the dotlock implementation in mailutils before 1:0.5-4 on Debian GNU/Linux allows attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packages.debian.org/changelogs/pool/main/m/mailutils/mailutils_0.6-2/changelog.

**参考链接 / References**:
- http://packages.debian.org/changelogs/pool/main/m/mailutils/mailutils_0.6-2/changelog
- http://packages.debian.org/changelogs/pool/main/m/mailutils/mailutils_0.6-2/changelog

---

#### 522. CVE-2004-1343

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cvs:cvs

**漏洞描述 / Description**:
CVS 1.12 and earlier on Debian GNU/Linux does not properly handle when a mapping for the current repository does not exist in the cvs-repouids file, which allows remote attackers to cause a denial of service (server crash).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2005/dsa-715.

**参考链接 / References**:
- http://www.debian.org/security/2005/dsa-715
- http://www.debian.org/security/2005/dsa-715

---

#### 523. CVE-2004-2569

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: david_stes:ipmenu

**漏洞描述 / Description**:
ipmenu 0.0.3 before Debian GNU/Linux ipmenu_0.0.3-5 allows local users to overwrite arbitrary files via a symlink attack on the ipmenu.log temporary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=244709.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=244709
- http://secunia.com/advisories/11526
- http://secunia.com/advisories/17682
- http://securitytracker.com/id?1010064
- http://www.debian.org/security/2005/dsa-907

---

#### 524. CVE-2004-1340

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: debian:debian_linux

**漏洞描述 / Description**:
Debian GNU/Linux 3.0 installs the libpam-radius-auth package with the pam_radius_auth.conf set to be world-readable, which allows local users to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14046.

**参考链接 / References**:
- http://secunia.com/advisories/14046
- http://securitytracker.com/id?1013030
- http://www.debian.org/security/2005/dsa-659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19087
- http://secunia.com/advisories/14046

---

#### 525. CVE-2004-1342

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cvs:cvs

**漏洞描述 / Description**:
CVS 1.12 and earlier on Debian GNU/Linux, when using the repouid patch, allows remote attackers to bypass authentication via the pserver access method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.debian.org/security/2005/dsa-715.

**参考链接 / References**:
- http://www.debian.org/security/2005/dsa-715
- http://www.debian.org/security/2005/dsa-715

---

#### 526. CVE-2005-0159

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: debian:debian_linux, debian:toolchain-source

**漏洞描述 / Description**:
The tpkg-* scripts in the toolchain-source 3.0.4 package on Debian GNU/Linux 3.0 allow local users to overwrite arbitrary files via a symlink attack on temporary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14277.

**参考链接 / References**:
- http://secunia.com/advisories/14277
- http://www.debian.org/security/2005/dsa-679
- http://www.securityfocus.com/bid/12540
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19317
- http://secunia.com/advisories/14277

---

#### 527. CVE-2005-2214

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: debian:apt-setup

**漏洞描述 / Description**:
apt-setup in Debian GNU/Linux installs the apt.conf file with insecure permissions, which allows local users to obtain sensitive information such as passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=305142.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=305142
- http://secunia.com/advisories/15955
- http://www.securityfocus.com/bid/14173
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=305142
- http://secunia.com/advisories/15955

---

#### 528. CVE-2005-1854

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: debian:apt-cacher

**漏洞描述 / Description**:
Unknown vulnerability in apt-cacher in Debian 3.1, related to "missing input sanitising," allows remote attackers to execute arbitrary commands on the caching server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/16327.

**参考链接 / References**:
- http://secunia.com/advisories/16327
- http://www.debian.org/security/2005/dsa-772
- http://www.securityfocus.com/bid/14459
- https://exchange.xforce.ibmcloud.com/vulnerabilities/21664
- http://secunia.com/advisories/16327

---

#### 529. CVE-2005-3254

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: nathan_neulinger:cgiwrap

**漏洞描述 / Description**:
The CGIwrap program before 3.9 on Debian GNU/Linux uses an incorrect minimum value of 100 for a UID to determine whether it can perform a seteuid operation, which could allow attackers to execute code as other system UIDs that are greater than the minimum value, which should be 1000 on Debian systems.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html.

**参考链接 / References**:
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html

---

#### 530. CVE-2005-3255

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: nathan_neulinger:cgiwrap

**漏洞描述 / Description**:
The (1) cgiwrap and (2) php-cgiwrap packages before 3.9 in Debian GNU/Linux provide access to debugging CGIs under the web document root, which allows remote attackers to obtain sensitive information via direct requests to those CGIs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html.

**参考链接 / References**:
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html
- http://lists.alioth.debian.org/pipermail/secure-testing-announce/2005-August/000003.html

---

#### 531. CVE-2005-3268

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: raphael_bossek:yiff_server

**漏洞描述 / Description**:
yiff server (yiff-server) 2.14.2 on Debian GNU/Linux runs as root and does not properly verify ownership of files that it opens, which allows local users to read arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=334616.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=334616
- http://secunia.com/advisories/17242
- http://www.osvdb.org/20074
- http://www.securityfocus.com/bid/15140
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=334616

---

#### 532. CVE-2005-4347

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:kernel-patch-vserver, debian:debian_linux

**漏洞描述 / Description**:
The Linux 2.4 kernel patch in kernel-patch-vserver before 1.9.5.5 and 2.x before 2.3 for Debian GNU/Linux does not correctly set the "chroot barrier" with util-vserver, which allows attackers to access files on the host system that are outside of the vserver.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19339.

**参考链接 / References**:
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25406
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011

---

#### 533. CVE-2005-4418

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: vserver:util-vserver

**漏洞描述 / Description**:
util-vserver before 0.30.208-1 with kernel-patch-vserver before 1.9.5.5 and 2.x before 2.3 for Debian GNU/Linux sets a default policy that trusts unknown capabilities, which could allow local users to conduct unauthorized activities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19333.

**参考链接 / References**:
- http://secunia.com/advisories/19333
- http://secunia.com/advisories/19339
- http://www.debian.org/security/2006/dsa-1011
- http://www.securityfocus.com/bid/17180
- https://exchange.xforce.ibmcloud.com/vulnerabilities/25407

---

#### 534. CVE-2005-4693

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: gaim-encryption:gaim-encryption

**漏洞描述 / Description**:
Gaim-Encryption 2.38-1 on Debian Linux allows remote attackers to cause a denial of service (crash) via a crafted message from an ICQ buddy, possibly involving the GE_received_key function in keys.c.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337127.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337127
- http://secunia.com/advisories/17739
- http://www.osvdb.org/21233
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337127
- http://secunia.com/advisories/17739

---

#### 535. CVE-1999-1491

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
abuse.console in Red Hat 2.1 uses relative pathnames to find and execute the undrv program, which allows local users to execute arbitrary commands via a path that points to a Trojan horse program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602167418994&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602167418994&w=2
- http://www.securityfocus.com/bid/354
- http://marc.info/?l=bugtraq&m=87602167418994&w=2
- http://www.securityfocus.com/bid/354

---

#### 536. CVE-1999-1490

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
xosview 1.5.1 in Red Hat 5.1 allows local users to gain root access via a long HOME environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221101926021&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221101926021&w=2
- http://marc.info/?l=bugtraq&m=90221101926034&w=2
- http://www.iss.net/security_center/static/8787.php
- http://www.securityfocus.com/bid/362
- http://marc.info/?l=bugtraq&m=90221101926021&w=2

---

#### 537. CVE-1999-0748

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Buffer overflows in Red Hat net-tools package.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA1999017_01.html.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA1999017_01.html
- http://www.redhat.com/support/errata/RHSA1999017_01.html

---

#### 538. CVE-1999-0814

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Red Hat pump DHCP client allows remote attackers to gain root access in some configurations.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-1999-027.html.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-1999-027.html
- http://www.redhat.com/support/errata/RHSA-1999-027.html

---

#### 539. CVE-1999-0768

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:linux, suse:suse_linux

**漏洞描述 / Description**:
Buffer overflow in Vixie Cron on Red Hat systems via the MAILTO environmental variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/602.

**参考链接 / References**:
- http://www.securityfocus.com/bid/602
- http://www.securityfocus.com/bid/602

---

#### 540. CVE-2000-0052

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mandrakesoft:mandrake_linux, turbolinux:turbolinux, redhat:linux

**漏洞描述 / Description**:
Red Hat userhelper program in the usermode package allows local users to gain root access via PAM and a .. (dot dot) attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.l0pht.com/advisories/pam_advisory.

**参考链接 / References**:
- http://www.l0pht.com/advisories/pam_advisory
- http://www.redhat.com/support/errata/RHSA-2000-001.html
- http://www.securityfocus.com/bid/913
- http://xforce.iss.net/search.php3?type=2&pattern=linux-pam-userhelper
- http://www.l0pht.com/advisories/pam_advisory

---

#### 541. CVE-2000-0093

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
An installation of Red Hat uses DES password encryption with crypt() for the initial password, instead of md5.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0093.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0093
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-2000-0093

---

#### 542. CVE-2000-0219

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
Red Hat 6.0 allows local users to gain root access by booting single user and hitting ^C at the password prompt.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1005.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1005
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200002230248.NAA19185%40cairo.anu.edu.au
- https://kc.mcafee.com/corporate/index?page=content&id=SB10053
- http://www.securityfocus.com/bid/1005
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=200002230248.NAA19185%40cairo.anu.edu.au

---

#### 543. CVE-2000-0322

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: redhat:linux

**漏洞描述 / Description**:
The passwd.php3 CGI script in the Red Hat Piranha Virtual Server Package allows local users to execute arbitrary commands via shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.redhat.com/support/errata/RHSA-2000-014.html.

**参考链接 / References**:
- http://www.redhat.com/support/errata/RHSA-2000-014.html
- http://www.securityfocus.com/bid/1149
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Enip.BSO.23.0004241601140.28851-100000%40www.whitehats.com
- http://www.redhat.com/support/errata/RHSA-2000-014.html
- http://www.securityfocus.com/bid/1149

---

#### 544. [SUSE] SUSE-SU-2026:1667-1: low: Security update for python-Pygments

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for python-Pygments Announcement ID: SUSE-SU-2026:1667-1 Release Date: 2026-04-30T17:22:44Z Rating: low References: * bsc#1260796 Cross-References: * CVE-2026-4539 CVSS scores: * CVE-2026-4539 ( SUSE ): 3.3 CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L * CVE-2026-4539 ( NVD ): 1.9 CVSS:4.0/AV:L/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N/E:P/CR:X/IR:X/AR:X/MAV:X/MAC:X/MAT:X/

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-May.txt

---

#### 545. [SUSE] SUSE-SU-2026:1668-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for the Linux Kernel Announcement ID: SUSE-SU-2026:1668-1 Release Date: 2026-05-01T08:37:57Z Rating: important References: * bsc#1220186 * bsc#1228031 * bsc#1246057 * bsc#1249522 * bsc#1257221 * bsc#1257773 * bsc#1258280 * bsc#1259770 * bsc#1259797 * bsc#1259865 * bsc#1259870 * bsc#1259889 * bsc#1259997 * bsc#1260009 * bsc#1260489 * bsc#1260536 * bsc#1260551 * bsc#1260730 * bsc#1

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-May.txt

---

#### 546. [SUSE] SUSE-SU-2026:20947-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 2 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20947-1 Release Date: 2026-03-25T18:17:14Z Rating: important References: * bsc#1255052 * bsc#1255053 * bsc#1255378 * bsc#1255402 * bsc#1255895 * bsc#1256624 * bsc#1256644 * bsc#1257669 Cross-References: * CVE-2025-40214 * CVE-2025-40258 * CVE-2025-40284 * CVE-2025-40297 * CVE-2025-68284

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 547. [SUSE] SUSE-SU-2026:20946-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 0 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20946-1 Release Date: 2026-03-25T18:09:48Z Rating: important References: * bsc#1247240 * bsc#1255052 * bsc#1255053 * bsc#1255378 * bsc#1255402 * bsc#1255895 * bsc#1256624 * bsc#1256644 * bsc#1257669 Cross-References: * CVE-2025-38488 * CVE-2025-40214 * CVE-2025-40258 * CVE-2025-40284 *

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 548. [SUSE] SUSE-SU-2026:20943-1: important: Security update for the Linux Kernel

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for the Linux Kernel (Live Patch 4 for SUSE Linux Enterprise 16) Announcement ID: SUSE-SU-2026:20943-1 Release Date: 2026-03-25T05:42:56Z Rating: important References: * bsc#1256624 * bsc#1256644 Cross-References: * CVE-2025-68813 * CVE-2025-71085 CVSS scores: * CVE-2025-68813 ( SUSE ): 8.7 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N * CVE-2025-68813 ( SUSE ):

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 549. [SUSE] SUSE-SU-2026:20942-1: important: Security update for the initial

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for the initial kernel livepatch Announcement ID: SUSE-SU-2026:20942-1 Release Date: 2026-03-24T20:14:20Z Rating: important References: Affected Products: * SUSE Linux Enterprise Server - BCI 16.0 An update that can now be installed. ## Description: This update contains initial livepatches for the SUSE Linux Enterprise Server 16.0 and SUSE Linux Micro 6.2 kernel update. ## Specia

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 550. [SUSE] SUSE-SU-2026:20941-1: moderate: Security update for ucode-intel

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for ucode-intel Announcement ID: SUSE-SU-2026:20941-1 Release Date: 2026-03-19T09:31:38Z Rating: moderate References: * bsc#1229129 * bsc#1230400 * bsc#1249138 * bsc#1253319 * bsc#1258046 Cross-References: * CVE-2024-24853 * CVE-2025-31648 CVSS scores: * CVE-2024-24853 ( SUSE ): 7.3 CVSS:4.0/AV:L/AC:H/AT:P/PR:H/UI:P/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H * CVE-2024-24853 ( SUSE ): 7.2 CVS

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 551. [SUSE] SUSE-SU-2026:20940-1: moderate: Security update for net-tools

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for net-tools Announcement ID: SUSE-SU-2026:20940-1 Release Date: 2026-03-26T15:12:43Z Rating: moderate References: * bsc#1243581 * bsc#1248410 * bsc#1248687 * bsc#142461 * bsc#430864 * bsc#544339 Cross-References: * CVE-2025-46836 CVSS scores: * CVE-2025-46836 ( SUSE ): 5.8 CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N * CVE-2025-46836 ( SUSE ): 6.6 CVSS:3.1/AV

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 552. [SUSE] SUSE-SU-2026:20936-1: important: Security update for openexr

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for openexr Announcement ID: SUSE-SU-2026:20936-1 Release Date: 2026-03-26T10:03:06Z Rating: important References: * bsc#1259177 Cross-References: * CVE-2026-27622 CVSS scores: * CVE-2026-27622 ( SUSE ): 8.4 CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N * CVE-2026-27622 ( SUSE ): 7.8 CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H * CVE-2026-27622 ( NVD ): 8.4 CVSS

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 553. [SUSE] SUSE-SU-2026:20935-1: moderate: Security update for fetchmail

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for fetchmail Announcement ID: SUSE-SU-2026:20935-1 Release Date: 2026-03-26T09:57:56Z Rating: moderate References: * bsc#1251194 Cross-References: * CVE-2025-61962 CVSS scores: * CVE-2025-61962 ( SUSE ): 5.9 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H * CVE-2025-61962 ( NVD ): 5.9 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H Affected Products: * SUSE Linux Enterprise Server - B

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 554. [SUSE] SUSE-SU-2026:20934-1: important: Security update for python-PyJWT

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for python-PyJWT Announcement ID: SUSE-SU-2026:20934-1 Release Date: 2026-03-25T18:08:48Z Rating: important References: * bsc#1259616 Cross-References: * CVE-2026-32597 CVSS scores: * CVE-2026-32597 ( SUSE ): 8.7 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N * CVE-2026-32597 ( SUSE ): 7.5 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N * CVE-2026-32597 ( NVD ): 7.5

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 555. [SUSE] SUSE-SU-2026:20933-1: moderate: Security update for python-ldap

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: SUSE Linux Enterprise

**漏洞描述 / Description**:
# Security update for python-ldap Announcement ID: SUSE-SU-2026:20933-1 Release Date: 2026-03-25T10:40:32Z Rating: moderate References: * bsc#1251912 * bsc#1251913 Cross-References: * CVE-2025-61911 * CVE-2025-61912 CVSS scores: * CVE-2025-61911 ( SUSE ): 5.5 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N/E:P/CR:X/IR:X/AR:X/MAV:X/MAC:X/MAT:X/MPR:X/MUI:X/MVC:X/MVI:X/MVA:X/MSC:X/MSI

**补丁信息 / Patch Info**:
Apply SUSE security patch via zypper or YaST Online Update.

**参考链接 / References**:
- https://lists.suse.com/pipermail/sle-security-updates/2026-April.txt

---

#### 556. [Ubuntu] USN-8226-2: kmod update

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
USN-8226-1 added a mitigation to kmod to disable loading the algif_aead module. This update adds the same mitigation to Ubuntu 14.04 LTS, Ubuntu 16.04 LTS, Ubuntu 18.04 LTS, and Ubuntu 20.04 LTS. Original advisory details: It was discovered that the Linux kernel algif_aead module contained a logic flaw allowing a local attacker to escalate privileges to root. This update to the kmod package disabl

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8226-2

---

#### 557. [Ubuntu] USN-8225-1: Python marshmallow vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Jared Deckard discovered that Python marshmallow did not correctly handle hiding certain fields. An attacker could possibly use this issue to leak sensitive information. This issue only affected Ubuntu 18.04 LTS. (CVE-2018-17175) It was discovered that Python marshmallow did not efficiently handle merging certain objects. An attacker could possibly use this issue to cause a denial of service. This

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8225-1

---

#### 558. [Ubuntu] USN-8224-1: Linux kernel (BlueField) vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Qualys discovered that several vulnerabilities existed in the AppArmor Linux kernel Security Module (LSM). An unprivileged local attacker could use these issues to load, replace, and remove arbitrary AppArmor profiles causing denial of service, exposure of sensitive information (kernel memory), local privilege escalation, or possibly escape a container. (LP: #2143853, CVE-2026-23268, CVE-2026-2326

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8224-1

---

#### 559. [Ubuntu] USN-8223-1: Roundcube Webmail vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that Roundcube Webmail mishandled Punycode xn-- domain names. An attacker could possibly use this issue to cause a homograph attack. (CVE-2019-15237) It was discovered that Roundcube Webmail did not properly sanitize certain attributes when handling CSS within HTML messages and certain SVG attributes. An attacker could possibly use this issue to cause a cross-site scripting attac

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8223-1

---

#### 560. [Ubuntu] USN-8222-1: OpenSSH vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Christos Papakonstantinou discovered that the OpenSSH scp tool incorrectly handled the legacy scp protocol (-O) option. This could result in certain files being installed setuid or setgid, contrary to expectations. (CVE-2026-35385) Florian Kohnhäuser discovered that OpenSSH incorrectly handled shell metacharacters in usernames within a command line. When untrusted usernames and non-default configu

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8222-1

---

#### 561. [Ubuntu] USN-8221-1: wheel vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that wheel did not correctly handle certain file paths. If a user or automated system were tricked into opening a specially crafted file, an attacker could possibly use this issue to execute arbitrary code.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8221-1

---

#### 562. [Ubuntu] USN-8219-1: UltraJSON vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Cameron Criswell discovered that UltraJSON contained a memory leak that would occur when parsing large integers. An attacker could possibly use this issue to cause UltraJSON to crash, resulting in a denial of service. This issue only affected Ubuntu 24.04 LTS, Ubuntu 25.10, and Ubuntu 26.04 LTS. (CVE-2026-32874) It was discovered that UltraJSON contained integer overflow/underflow issues when calc

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8219-1

---

#### 563. [Ubuntu] USN-8216-1: .NET vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Ludvig Pedersen discovered that the System.Security.Cryptography.Xml library in .NET incorrectly handled certain XML inputs. An attacker could possibly use this issue to consume excessive resources, resulting in a denial of service. (CVE-2026-33116, CVE-2026-26171) Ludvig Pedersen and Kevin Jones discovered that the System.Security.Cryptography.Xml library in .NET incorrectly handled certain XML i

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8216-1

---

#### 564. [Ubuntu] USN-8215-1: .NET vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that the Microsoft.AspNetCore.DataProtection library in .NET did not properly verify cryptographic signatures under certain conditions. A remote attacker could possibly use this issue to elevate privileges.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8215-1

---

#### 565. [Ubuntu] USN-8214-1: NLTK vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that NLTK incorrectly handled file extraction when opening a maliciously crafted zip file. An attacker could possibly use this issue to create or overwrite files on the system and execute arbitrary code.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8214-1

---

#### 566. [Ubuntu] USN-8213-1: Vim vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Michał Majchrowicz discovered that Vim's zip plugin could overwrite arbitrary files. An attacker could possibly use this issue to delete sensitive data or execute arbitrary code. This issue only affected Ubuntu 24.04 LTS and Ubuntu 25.10. (CVE-2026-35177) It was discovered that Vim's netbeans interface did not properly sanitize certain strings. An attacker could possibly use this issue to execute

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8213-1

---

#### 567. [Ubuntu] USN-8212-1: authd vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that authd incorrectly assigned the primary group ID to users under certain conditions. A local attacker could possibly use this issue to achieve privilege escalation, or gain unauthorized access to files belonging to other users.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8212-1

---

#### 568. [Ubuntu] USN-8211-1: Pillow vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that Pillow incorrectly handled certain FITS images. An attacker could possibly use this issue to cause Pillow to consume resources, leading to a denial of service.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8211-1

---

#### 569. [Ubuntu] USN-8210-1: nginx vulnerabilities

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that the nginx ngx_mail_auth_http_module module incorrectly handled certain requests. An attacker could possibly use this issue to cause nginx to crash, resulting in a denial of service. (CVE-2026-27651) It was discovered that the nginx ngx_http_dav_module module incorrectly handled certain destination URIs. An attacker could use this issue to cause nginx to crash, resulting in a

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8210-1

---

#### 570. [Ubuntu] USN-8209-1: Little CMS vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that Little CMS incorrectly handled certain malformed ICC profiles. An attacker could use this issue to cause Little CMS to crash, resulting in a denial of service, or possibly execute arbitrary code.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8209-1

---

#### 571. [Ubuntu] USN-8208-1: HAProxy vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
Martino Spagnuolo discovered that HAProxy did not check received body lengths in the HTTP/3 parser. A remote attacker could possibly use this issue to perform a request smuggling attack and obtain sensitive information.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8208-1

---

#### 572. [Ubuntu] USN-8207-1: ClamAV vulnerability

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: Ubuntu

**漏洞描述 / Description**:
It was discovered that ClamAV incorrectly handled certain HTML files. A remote attacker could possibly use this issue to cause ClamAV to crash, resulting in a denial of service.

**补丁信息 / Patch Info**:
Run 'apt update && apt upgrade' to apply security patches.

**参考链接 / References**:
- https://ubuntu.com/security/notices/USN-8207-1

---

#### 573. CVE-2003-0900

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: larry_wall:perl

**漏洞描述 / Description**:
Perl 5.8.1 on Fedora Core does not properly initialize the random number generator when forking, which makes it easier for attackers to predict random numbers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://bugzilla.redhat.com/bugzilla/long_list.cgi?buglist=108711.

**参考链接 / References**:
- https://bugzilla.redhat.com/bugzilla/long_list.cgi?buglist=108711
- https://bugzilla.redhat.com/bugzilla/long_list.cgi?buglist=108711

---

#### 574. CVE-2004-2502

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: im-switch:im-switch

**漏洞描述 / Description**:
im-switch before 11.4-46.1 in Fedora Core 2 allows local users to overwrite arbitrary files via a symlink attack on the imswitcher[PID] temporary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=126940.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=126940
- http://packetstormsecurity.org/0407-advisories/fedora_im-switch_tempfile_race.txt
- http://secunia.com/advisories/12037
- http://www.osvdb.org/7772
- http://www.securityfocus.com/bid/10717

---

#### 575. CVE-2004-2655

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: xscreensaver:xscreensaver

**漏洞描述 / Description**:
rdesktop 1.3.1 with xscreensaver 4.14, and possibly other versions, when running on Fedora and possibly other platforms, does not release the keyboard focus when xscreensaver starts, which causes the password to be entered into the active window when the user unlocks the screen.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://patches.sgi.com/support/free/security/advisories/20060602-01-U.asc.

**参考链接 / References**:
- ftp://patches.sgi.com/support/free/security/advisories/20060602-01-U.asc
- http://secunia.com/advisories/20226
- http://secunia.com/advisories/20456
- http://secunia.com/advisories/20782
- http://secunia.com/advisories/22080

---

#### 576. CVE-2005-3630

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:fedora_core

**漏洞描述 / Description**:
Fedora Directory Server before 10 allows remote attackers to obtain sensitive information, such as the password from adm.conf via an IFRAME element, probably involving an Apache httpd.conf configuration that orders "allow" directives before "deny" directives.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://directory.fedora.redhat.com/wiki/FDS10Announcement.

**参考链接 / References**:
- http://directory.fedora.redhat.com/wiki/FDS10Announcement
- http://secunia.com/advisories/18939
- http://www.securityfocus.com/bid/16729
- https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=121994
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=174837

---

#### 577. CVE-2006-0451

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:fedora_core

**漏洞描述 / Description**:
Multiple memory leaks in the LDAP component in Fedora Directory Server 1.0 allow remote attackers to cause a denial of service (memory consumption) via invalid BER packets that trigger an error, which might prevent memory from being freed if it was allocated during the ber_scanf call, as demonstrated using the ProtoVer LDAP test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24794
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135

---

#### 578. CVE-2006-0452

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: redhat:fedora_core

**漏洞描述 / Description**:
dn2ancestor in the LDAP component in Fedora Directory Server 1.0 allows remote attackers to cause a denial of service (CPU and memory consumption) via a ModDN operation with a DN that contains a large number of "," (comma) characters, which results in a large amount of recursion, as demonstrated using the ProtoVer LDAP test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179137.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179137
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24796
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179137

---

#### 579. CVE-2006-0453

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: redhat:fedora_core

**漏洞描述 / Description**:
The LDAP component in Fedora Directory Server 1.0 allow remote attackers to cause a denial of service (crash) via a certain "bad BER sequence" that results in a free of uninitialized memory, as demonstrated using the ProtoVer LDAP test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135.

**参考链接 / References**:
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135
- http://secunia.com/advisories/18960
- http://www.securityfocus.com/bid/16677
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24795
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179135

---

#### 580. CVE-2006-3742

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: kde:kdebase

**漏洞描述 / Description**:
The KDE PAM configuration shipped with Fedora Core 5 causes KDM passwords to be cached, which allows attackers to login without a password by attempting to log in multiple times.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lwn.net/Alerts/197302/.

**参考链接 / References**:
- http://lwn.net/Alerts/197302/
- http://lwn.net/Alerts/197302/

---

#### 581. CVE-2006-5170

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:enterprise_linux_for_ibm_z_systems, redhat:enterprise_linux, redhat:enterprise_linux_for_power_big_endian, redhat:enterprise_linux_workstation, debian:debian_linux

**漏洞描述 / Description**:
pam_ldap in nss_ldap on Red Hat Enterprise Linux 4, Fedora Core 3 and earlier, and possibly other distributions does not return an error condition when an LDAP directory server responds with a PasswordPolicyResponse control response, which causes the pam_authenticate function to return a success code even if authentication has failed, as originally reported for xscreensaver.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.padl.com/show_bug.cgi?id=291.

**参考链接 / References**:
- http://bugzilla.padl.com/show_bug.cgi?id=291
- http://rhn.redhat.com/errata/RHSA-2006-0719.html
- http://secunia.com/advisories/22682
- http://secunia.com/advisories/22685
- http://secunia.com/advisories/22694

---

#### 582. CVE-2006-5701

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: linux:linux_kernel, redhat:fedora_core

**漏洞描述 / Description**:
Double free vulnerability in squashfs module in the Linux kernel 2.6.x, as used in Fedora Core 5 and possibly other distributions, allows local users to cause a denial of service by mounting a crafted squashfs filesystem.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://projects.info-pull.com/mokb/MOKB-02-11-2006.html.

**参考链接 / References**:
- http://projects.info-pull.com/mokb/MOKB-02-11-2006.html
- http://secunia.com/advisories/22655
- http://secunia.com/advisories/23361
- http://secunia.com/advisories/23384
- http://secunia.com/advisories/24259

---

#### 583. CVE-2006-6057

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The Linux kernel 2.6.x up to 2.6.18, and possibly other versions, on Fedora Core 6 and possibly other operating systems, allows local users to cause a denial of service (crash) via a malformed gfs2 file stream that triggers a NULL pointer dereference in the init_journal function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://projects.info-pull.com/mokb/MOKB-15-11-2006.html.

**参考链接 / References**:
- http://projects.info-pull.com/mokb/MOKB-15-11-2006.html
- http://secunia.com/advisories/22886
- http://secunia.com/advisories/24098
- http://www.ubuntu.com/usn/usn-416-1
- http://www.vupen.com/english/advisories/2006/4556

---

#### 584. CVE-2006-7151

**严重程度 / Severity**: N/A | CVSS: 6.6
**受影响产品 / Affected Products**: redhat:fedora_core, gnu:libtool-ltdl

**漏洞描述 / Description**:
Untrusted search path vulnerability in the libtool-ltdl library (libltdl.so) 1.5.22-2.3 in Fedora Core 5 might allow local users to execute arbitrary code via a malicious library in the (1) hwcap, (2) 0, and (3) nosegneg subdirectories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/2378.

**参考链接 / References**:
- http://securityreason.com/securityalert/2378
- http://www.securityfocus.com/archive/1/448153/100/0/threaded
- http://www.securityfocus.com/bid/20434
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=209930
- http://securityreason.com/securityalert/2378

---

#### 585. CVE-2007-2874

**严重程度 / Severity**: N/A | CVSS: 5.8
**受影响产品 / Affected Products**: redhat:fedora_core

**漏洞描述 / Description**:
Buffer overflow in the wpa_printf function in the debugging code in wpa_supplicant in the Fedora NetworkManager package before 0.6.5-3.fc7 allows user-assisted remote attackers to execute arbitrary code via malformed frames on a WPA2 network.  NOTE: some of these details are obtained from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://fedoraproject.org/wiki/FSA/F7/FEDORA-2007-0186.

**参考链接 / References**:
- http://fedoraproject.org/wiki/FSA/F7/FEDORA-2007-0186
- http://osvdb.org/46833
- http://www.redhat.com/archives/fedora-package-announce/2007-June/msg00032.html
- http://www.vupen.com/english/advisories/2007/2053
- http://fedoraproject.org/wiki/FSA/F7/FEDORA-2007-0186

---

#### 586. CVE-2007-4364

**严重程度 / Severity**: N/A | CVSS: 8.5
**受影响产品 / Affected Products**: fedoraproject:commons

**漏洞描述 / Description**:
Fedora Commons before 2.2.1 does not properly handle certain authentication requests involving Java Naming and Directory Interface (JNDI), related to (1) a nonexistent account name in combination with an empty password, which allows remote attackers to trigger a certain "unexpected / strange response" from an LDAP server, and (2) a reauthentication attempt that throws an exception, which allows remote attackers to trigger use of a cached authentication decision.  NOTE: authentication can be bypassed by using vector 1 followed by vector 2, and possibly can be bypassed by using a single vector.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/39548.

**参考链接 / References**:
- http://osvdb.org/39548
- http://secunia.com/advisories/26445
- http://sourceforge.net/project/shownotes.php?release_id=531870
- http://sourceforge.net/tracker/index.php?func=detail&aid=1731608&group_id=177054&atid=879703
- http://www.securityfocus.com/bid/25317

---

#### 587. CVE-2007-4904

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: realnetworks:helix_player, realnetworks:realplayer

**漏洞描述 / Description**:
RealNetworks RealPlayer 10.1.0.3114 and earlier, and Helix Player 1.0.6.778 on Fedora Core 6 (FC6) and possibly other platforms, allow user-assisted remote attackers to cause a denial of service (application crash) via a malformed .au file that triggers a divide-by-zero error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2007-09/0154.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2007-09/0154.html
- http://osvdb.org/39904
- http://www.securityfocus.com/archive/1/479081/100/0/threaded
- http://www.securityfocus.com/bid/25627
- https://exchange.xforce.ibmcloud.com/vulnerabilities/36545

---

#### 588. CVE-2007-3102

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: fedora_project:fedora_core, openbsd:openssh

**漏洞描述 / Description**:
Unspecified vulnerability in the linux_audit_record_event function in OpenSSH 4.3p2, as used on Fedora Core 6 and possibly other systems, allows remote attackers to write arbitrary characters to an audit log via a crafted username.  NOTE: some of these details are obtained from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/39214.

**参考链接 / References**:
- http://osvdb.org/39214
- http://secunia.com/advisories/27235
- http://secunia.com/advisories/27588
- http://secunia.com/advisories/27590
- http://secunia.com/advisories/28319

---

#### 589. CVE-2007-6283

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: oracle:linux, redhat:enterprise_linux_for_ibm_z_systems, centos:centos, redhat:enterprise_linux, redhat:enterprise_linux_for_power_big_endian

**漏洞描述 / Description**:
Red Hat Enterprise Linux 5 and Fedora install the Bind /etc/rndc.key file with world-readable permissions, which allows local users to perform unauthorized named commands, such as causing a denial of service by stopping named.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/28180.

**参考链接 / References**:
- http://secunia.com/advisories/28180
- http://secunia.com/advisories/30313
- http://www.redhat.com/support/errata/RHSA-2008-0300.html
- https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2007-6283
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A9977

---

#### 590. CVE-2007-5962

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: redhat:fedora, foresight_linux:appliances, rpath:appliance_platform_agent, redhat:enterprise_linux

**漏洞描述 / Description**:
Memory leak in a certain Red Hat patch, applied to vsftpd 2.0.5 on Red Hat Enterprise Linux (RHEL) 5 and Fedora 6 through 8, and on Foresight Linux and rPath appliances, allows remote attackers to cause a denial of service (memory consumption) via a large number of CWD commands, as demonstrated by an attack on a daemon with the deny_file configuration option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/30341.

**参考链接 / References**:
- http://secunia.com/advisories/30341
- http://secunia.com/advisories/30354
- http://securitytracker.com/id?1020079
- http://wiki.rpath.com/wiki/Advisories:rPSA-2008-0185
- http://www.openwall.com/lists/oss-security/2008/05/21/10

---

#### 591. CVE-2008-2359

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: fedora_8:consolehelper, redhat:fedora_8

**漏洞描述 / Description**:
The default configuration of consolehelper in system-config-network before 1.5.10-1 on Fedora 8 lacks the USER=root directive, which allows local users of the workstation console to gain privileges and change the network configuration.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/30399.

**参考链接 / References**:
- http://secunia.com/advisories/30399
- https://bugzilla.redhat.com/show_bug.cgi?id=448557
- https://exchange.xforce.ibmcloud.com/vulnerabilities/42867
- https://www.redhat.com/archives/fedora-package-announce/2008-May/msg00974.html
- http://secunia.com/advisories/30399

---

#### 592. CVE-2008-2944

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: linux:linux_kernel, fedoraproject:fedora_core, redhat:enterprise_linux

**漏洞描述 / Description**:
Double free vulnerability in the utrace support in the Linux kernel, probably 2.6.18, in Red Hat Enterprise Linux (RHEL) 5 and Fedora Core 6 (FC6) allows local users to cause a denial of service (oops), as demonstrated by a crash when running the GNU GDB testsuite, a different vulnerability than CVE-2008-2365.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://bugzilla.redhat.com/show_bug.cgi?id=207002.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=207002
- https://bugzilla.redhat.com/show_bug.cgi?id=449359
- https://exchange.xforce.ibmcloud.com/vulnerabilities/43556
- https://bugzilla.redhat.com/show_bug.cgi?id=207002
- https://bugzilla.redhat.com/show_bug.cgi?id=449359

---

#### 593. CVE-2008-2929

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: fedora:directory_server, redhat:directory_server

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the adminutil library in the Directory Server Administration Express and Directory Server Gateway (DSGW) web interface in Red Hat Directory Server 7.1 before SP7 and 8 EL4 and EL5, and Fedora Directory Server, allow remote attackers to inject arbitrary web script or HTML via input values that use % (percent) escaping.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31612
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31777

---

#### 594. CVE-2008-2930

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: fedora:directory_server, redhat:directory_server

**漏洞描述 / Description**:
Red Hat Directory Server 7.1 before SP7, Red Hat Directory Server 8, and Fedora Directory Server 1.1.1 allow remote attackers to cause a denial of service (CPU consumption and search outage) via crafted LDAP search requests with patterns, related to a single-threaded regular-expression subsystem.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31627
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31867

---

#### 595. CVE-2008-3283

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: fedora:directory_server, redhat:directory_server

**漏洞描述 / Description**:
Multiple memory leaks in Red Hat Directory Server 7.1 before SP7, Red Hat Directory Server 8, and Fedora Directory Server 1.1.1 and earlier allow remote attackers to cause a denial of service (memory consumption) via vectors involving (1) the authentication / bind phase and (2) anonymous LDAP search requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861.

**参考链接 / References**:
- http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01532861
- http://secunia.com/advisories/31565
- http://secunia.com/advisories/31627
- http://secunia.com/advisories/31702
- http://secunia.com/advisories/31867

---

#### 596. CVE-2008-2932

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: redhat:adminutil

**漏洞描述 / Description**:
Heap-based buffer overflow in Red Hat adminutil 1.1.6 allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via % (percent) encoded HTTP input to unspecified CGI scripts in Fedora Directory Server.  NOTE: this vulnerability exists because of an incorrect fix for CVE-2008-2929.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31777.

**参考链接 / References**:
- http://secunia.com/advisories/31777
- http://www.securityfocus.com/bid/31106
- https://bugzilla.redhat.com/show_bug.cgi?id=454662
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45203
- https://www.redhat.com/archives/fedora-package-announce/2008-September/msg00218.html

---

#### 597. CVE-2008-3524

**严重程度 / Severity**: N/A | CVSS: 4.7
**受影响产品 / Affected Products**: redhat:initscripts, redhat:fedora

**漏洞描述 / Description**:
rc.sysinit in initscripts before 8.76.3-1 on Fedora 9 and other Linux platforms allows local users to delete arbitrary files via a symlink attack on a file or directory under (1) /var/lock or (2) /var/run.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/32037.

**参考链接 / References**:
- http://secunia.com/advisories/32037
- http://secunia.com/advisories/32710
- http://wiki.rpath.com/wiki/Advisories:rPSA-2008-0318
- http://www.securityfocus.com/bid/31385
- https://bugzilla.redhat.com/show_bug.cgi?id=458504

---

#### 598. CVE-2008-3832

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: linux:linux_kernel, redhat:fedora

**漏洞描述 / Description**:
A certain Fedora patch for the utrace subsystem in the Linux kernel before 2.6.26.5-28 on Fedora 8, and before 2.6.26.5-45 on Fedora 9, allows local users to cause a denial of service (NULL pointer dereference and system crash or hang) via a call to the utrace_control function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://kerneloops.org/oops.php?number=56705.

**参考链接 / References**:
- http://kerneloops.org/oops.php?number=56705
- http://www.openwall.com/lists/oss-security/2008/10/02/1
- http://www.securityfocus.com/bid/31536
- https://bugzilla.redhat.com/show_bug.cgi?id=464883
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45644

---

#### 599. CVE-2008-4870

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: dovecot:dovecot, redhat:enterprise_linux

**漏洞描述 / Description**:
dovecot 1.0.7 in Red Hat Enterprise Linux (RHEL) 5, and possibly Fedora, uses world-readable permissions for dovecot.conf, which allows local users to obtain the ssl_key_password parameter value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/32164.

**参考链接 / References**:
- http://secunia.com/advisories/32164
- http://secunia.com/advisories/33149
- http://secunia.com/advisories/33624
- http://security.gentoo.org/glsa/glsa-200812-16.xml
- http://www.openwall.com/lists/oss-security/2008/10/29/10

---

#### 600. CVE-2008-4946

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: convirture:convirt

**漏洞描述 / Description**:
convirt 0.8.2 allows local users to overwrite arbitrary files via a symlink attack on the /tmp/set_output temporary file, related to the (1) _template_/provision.sh, (2) Linux_CD_Install/provision.sh, (3) Fedora_PV_Install/provision.sh, (4) CentOS_PV_Install/provision.sh, (5) common/provision.sh, (6) example/provision.sh, and (7) Windows_CD_Install/provision.sh scripts in image_store/.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/496419.

**参考链接 / References**:
- http://bugs.debian.org/496419
- http://dev.gentoo.org/~rbu/security/debiantemp/convirt
- http://www.openwall.com/lists/oss-security/2008/10/30/2
- https://bugs.gentoo.org/show_bug.cgi?id=235770
- http://bugs.debian.org/496419

---

#### 601. CVE-2008-4315

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: openpegasus:openpegasus_wbem, redhat:enterprise_linux_desktop, redhat:enterprise_linux

**漏洞描述 / Description**:
tog-pegasus in OpenGroup Pegasus 2.7.0 on Red Hat Enterprise Linux (RHEL) 5, Fedora 9, and Fedora 10 does not log failed authentication attempts to the OpenPegasus CIM server, which makes it easier for remote attackers to avoid detection of password guessing attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/50278.

**参考链接 / References**:
- http://osvdb.org/50278
- http://secunia.com/advisories/32862
- http://www.redhat.com/support/errata/RHSA-2008-1001.html
- http://www.securitytracker.com/id?1021281
- https://admin.fedoraproject.org/updates/tog-pegasus-2.7.0-7.fc9

---

#### 602. CVE-2009-0180

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: nfs:nfs-utils, redhat:fedora

**漏洞描述 / Description**:
Certain Fedora build scripts for nfs-utils before 1.1.2-9.fc9 on Fedora 9, and before 1.1.4-6.fc10 on Fedora 10, omit TCP Wrapper support, which might allow remote attackers to bypass intended access restrictions, possibly a related issue to CVE-2008-1376.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/33545.

**参考链接 / References**:
- http://secunia.com/advisories/33545
- http://www.securityfocus.com/bid/33294
- https://bugzilla.redhat.com/show_bug.cgi?id=477864
- https://exchange.xforce.ibmcloud.com/vulnerabilities/48058
- https://www.redhat.com/archives/fedora-package-announce/2009-January/msg00376.html

---

#### 603. CVE-2008-6552

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: redhat:gfs2-utils, redhat:cman, redhat:cluster_project, redhat:rgmanager, fedoraproject:fedora

**漏洞描述 / Description**:
Red Hat Cluster Project 2.x allows local users to modify or overwrite arbitrary files via symlink attacks on files in /tmp, involving unspecified components in Resource Group Manager (aka rgmanager) before 2.03.09-1, gfs2-utils before 2.03.09-1, and CMAN - The Cluster Manager before 2.03.09-1 on Fedora 9.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/50299.

**参考链接 / References**:
- http://osvdb.org/50299
- http://osvdb.org/50300
- http://osvdb.org/50301
- http://rhn.redhat.com/errata/RHSA-2009-1337.html
- http://secunia.com/advisories/32602

---

#### 604. CVE-2009-0115

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: avaya:intuity_audix_lx, suse:linux_enterprise_server, avaya:message_networking, novell:open_enterprise_server, christophe.varoqui:multipath-tools

**漏洞描述 / Description**:
The Device Mapper multipathing driver (aka multipath-tools or device-mapper-multipath) 0.4.8, as used in SUSE openSUSE, SUSE Linux Enterprise Server (SLES), Fedora, and possibly other operating systems, uses world-writable permissions for the socket file (aka /var/run/multipathd.sock), which allows local users to send arbitrary commands to the multipath daemon.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://download.opensuse.org/update/10.3-test/repodata/patch-kpartx-6082.xml.

**参考链接 / References**:
- http://download.opensuse.org/update/10.3-test/repodata/patch-kpartx-6082.xml
- http://kb.juniper.net/InfoCenter/index?page=content&id=JSA10691
- http://kb.juniper.net/InfoCenter/index?page=content&id=JSA10705
- http://launchpad.net/bugs/cve/2009-0115
- http://lists.opensuse.org/opensuse-security-announce/2009-03/msg00004.html

---

#### 605. CVE-2008-6560

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: redhat:linux, redhat:fedora, redhat:cman

**漏洞描述 / Description**:
Buffer overflow in CMAN - The Cluster Manager before 2.03.09-1 on Fedora 9 and Red Hat Enterprise Linux (RHEL) 5 allows attackers to cause a denial of service (CPU consumption and memory corruption) via a cluster.conf file with many lines.  NOTE: it is not clear whether this issue crosses privilege boundaries in realistic uses of the product.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://git.fedorahosted.org/git/cluster.git?p=cluster.git%3Ba=commitdiff%3Bh=67fee9128e54c6c3fc3eae306b5b501f3029c3be.

**参考链接 / References**:
- http://git.fedorahosted.org/git/cluster.git?p=cluster.git%3Ba=commitdiff%3Bh=67fee9128e54c6c3fc3eae306b5b501f3029c3be
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00163.html
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00164.html
- http://www.redhat.com/archives/fedora-package-announce/2008-November/msg00165.html
- http://www.ubuntu.com/usn/USN-875-1

---

#### 606. CVE-2008-6755

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: zoneminder:zoneminder, redhat:fedora

**漏洞描述 / Description**:
ZoneMinder 1.23.3 on Fedora 10 sets the ownership of /etc/zm.conf to the apache user account, and sets the permissions to 0600, which makes it easier for remote attackers to modify this file by accessing it through a (1) PHP or (2) CGI script.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://bugzilla.redhat.com/show_bug.cgi?id=476529.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=476529
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50324
- https://www.redhat.com/archives/fedora-package-announce/2009-January/msg00204.html
- https://bugzilla.redhat.com/show_bug.cgi?id=476529
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50324

---

#### 607. CVE-2009-0153

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
International Components for Unicode (ICU) 4.0, 3.6, and other 3.x versions, as used in Apple Mac OS X 10.5 before 10.5.7, iPhone OS 1.0 through 2.2.1, iPhone OS for iPod touch 1.1 through 2.2.1, Fedora 9 and 10, and possibly other operating systems, does not properly handle invalid byte sequences during Unicode conversion, which might allow remote attackers to conduct cross-site scripting (XSS) attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.icu-project.org/trac/ticket/5691.

**参考链接 / References**:
- http://bugs.icu-project.org/trac/ticket/5691
- http://lists.apple.com/archives/security-announce/2009/Jun/msg00005.html
- http://lists.apple.com/archives/security-announce/2009/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2009/jun/msg00002.html
- http://secunia.com/advisories/35074

---

#### 608. CVE-2009-1896

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:openjdk, fedoraproject:fedora

**漏洞描述 / Description**:
The Java Web Start framework in IcedTea in OpenJDK before 1.6.0.0-20.b16.fc10 on Fedora 10, and before 1.6.0.0-27.b16.fc11 on Fedora 11, trusts an entire application when at least one of the listed jar files is trusted, which allows context-dependent attackers to execute arbitrary code without the untrusted-code restrictions via a crafted application, related to NetX.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/36162.

**参考链接 / References**:
- http://secunia.com/advisories/36162
- http://www.mandriva.com/security/advisories?name=MDVSA-2009:209
- https://bugzilla.redhat.com/show_bug.cgi?id=512101
- https://www.redhat.com/archives/fedora-package-announce/2009-August/msg00310.html
- https://www.redhat.com/archives/fedora-package-announce/2009-August/msg00325.html

---

#### 609. CVE-2009-2813

**严重程度 / Severity**: N/A | CVSS: 6.0
**受影响产品 / Affected Products**: samba:samba, apple:mac_os_x_server, apple:mac_os_x, fedoraproject:fedora

**漏洞描述 / Description**:
Samba 3.4 before 3.4.2, 3.3 before 3.3.8, 3.2 before 3.2.15, and 3.0.12 through 3.0.36, as used in the SMB subsystem in Apple Mac OS X 10.5.8 when Windows File Sharing is enabled, Fedora 11, and other operating systems, does not properly handle errors in resolving pathnames, which allows remote authenticated users to bypass intended sharing restrictions, and read, create, or modify files, in certain circumstances involving user accounts that lack home directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2009/Sep/msg00004.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2009/Sep/msg00004.html
- http://lists.opensuse.org/opensuse-security-announce/2009-10/msg00004.html
- http://marc.info/?l=bugtraq&m=126514298313071&w=2
- http://news.samba.org/releases/3.0.37/
- http://news.samba.org/releases/3.2.15/

---

#### 610. CVE-2009-2904

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: redhat:enterprise_linux_eus, redhat:enterprise_linux, redhat:enterprise_linux_desktop, fedoraproject:fedora, openbsd:openssh

**漏洞描述 / Description**:
A certain Red Hat modification to the ChrootDirectory feature in OpenSSH 4.8, as used in sshd in OpenSSH 4.3 in Red Hat Enterprise Linux (RHEL) 5.4 and Fedora 11, allows local users to gain privileges via hard links to setuid programs that use configuration files within the chroot directory, related to requirements for directory ownership.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2010-March/038214.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2010-March/038214.html
- http://lists.vmware.com/pipermail/security-announce/2010/000082.html
- http://osvdb.org/58495
- http://secunia.com/advisories/38794
- http://secunia.com/advisories/38834

---

#### 611. CVE-2010-1439

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: fedoraproject:fedora, redhat:yum-rhn-plugin, redhat:enterprise_linux, redhat:rhn-client-tools

**漏洞描述 / Description**:
yum-rhn-plugin in Red Hat Network Client Tools (aka rhn-client-tools) on Red Hat Enterprise Linux (RHEL) 5 and Fedora uses world-readable permissions for the /var/spool/up2date/loginAuth.pkl file, which allows local users to access the Red Hat Network profile, and possibly prevent future security updates, by leveraging authentication data from this file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39996.

**参考链接 / References**:
- http://secunia.com/advisories/39996
- http://securitytracker.com/id?1024049
- http://www.osvdb.org/65063
- http://www.redhat.com/support/errata/RHSA-2010-0449.html
- http://www.securityfocus.com/bid/40492

---

#### 612. CVE-2010-4176

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: dracut_project:dracut, udev_project:udev, fedoraproject:fedora

**漏洞描述 / Description**:
plymouth-pretrigger.sh in dracut and udev, when running on Fedora 13 and 14, sets weak permissions for the /dev/systty device file, which allows remote authenticated users to read terminal data from tty0 for local users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2010-December/051755.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2010-December/051755.html
- http://lists.fedoraproject.org/pipermail/package-announce/2010-November/051418.html
- http://secunia.com/advisories/42342
- http://secunia.com/advisories/42451
- http://www.securityfocus.com/bid/45046

---

#### 613. CVE-2010-4695

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: debian:linux, catb:gif2png, redhat:fedora

**漏洞描述 / Description**:
A certain Fedora patch for gif2png.c in gif2png 2.5.1 and 2.5.2, as distributed in gif2png-2.5.1-1200.fc12 on Fedora 12 and gif2png_2.5.2-1 on Debian GNU/Linux, truncates a GIF pathname specified on the command line, which might allow remote attackers to create PNG files in unintended directories via a crafted command-line argument, as demonstrated by a CGI program that launches gif2png, a different vulnerability than CVE-2009-5018.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=550978.

**参考链接 / References**:
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=550978
- http://cvs.fedoraproject.org/viewvc/rpms/gif2png/devel/gif2png-overflow.patch?root=extras&r1=1.1&r2=1.2
- http://cvs.fedoraproject.org/viewvc/rpms/gif2png/devel/gif2png-overflow.patch?root=extras&view=log
- http://lists.fedoraproject.org/pipermail/package-announce/2010-November/051229.html
- http://security.gentoo.org/glsa/glsa-201203-15.xml

---

#### 614. CVE-2011-0008

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: redhat:fedora, todd_miller:sudo

**漏洞描述 / Description**:
A certain Fedora patch for parse.c in sudo before 1.7.4p5-1.fc14 on Fedora 14 does not properly interpret a system group (aka %group) in the sudoers file during authorization decisions for a user who belongs to that group, which allows local users to leverage an applicable sudoers file and gain root privileges via a sudo command.  NOTE: this vulnerability exists because of a CVE-2009-0034 regression.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2011-January/053263.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2011-January/053263.html
- http://lists.fedoraproject.org/pipermail/package-announce/2011-January/053341.html
- http://secunia.com/advisories/42968
- http://www.mandriva.com/security/advisories?name=MDVSA-2011:018
- http://www.vupen.com/english/advisories/2011/0195

---

#### 615. CVE-2011-1011

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: redhat:fedora, redhat:enterprise_linux, redhat:policycoreutils

**漏洞描述 / Description**:
The seunshare_mount function in sandbox/seunshare.c in seunshare in certain Red Hat packages of policycoreutils 2.0.83 and earlier in Red Hat Enterprise Linux (RHEL) 6 and earlier, and Fedora 14 and earlier, mounts a new directory on top of /tmp without assigning root ownership and the sticky bit to this new directory, which allows local users to replace or delete arbitrary /tmp files, and consequently cause a denial of service or possibly gain privileges, by running a setuid application that relies on /tmp, as demonstrated by the ksu application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2011-02/0585.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2011-02/0585.html
- http://lists.fedoraproject.org/pipermail/package-announce/2011-March/056227.html
- http://openwall.com/lists/oss-security/2011/02/23/1
- http://openwall.com/lists/oss-security/2011/02/23/2
- http://pkgs.fedoraproject.org/gitweb/?p=policycoreutils.git%3Ba=blob%3Bf=policycoreutils-rhat.patch%3Bh=d4db5bc06027de23d12a4b3f18fa6f9b1517df27%3Bhb=HEAD#l2197

---

#### 616. CVE-2011-1943

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: fedoraproject:fedora, gnome:networkmanager

**漏洞描述 / Description**:
The destroy_one_secret function in nm-setting-vpn.c in libnm-util in the NetworkManager package 0.8.999-3.git20110526 in Fedora 15 creates a log entry containing a certificate password, which allows local users to obtain sensitive information by reading a log file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cgit.freedesktop.org/NetworkManager/NetworkManager/commit/?id=78ce088843d59d4494965bfc40b30a2e63d065f6.

**参考链接 / References**:
- http://cgit.freedesktop.org/NetworkManager/NetworkManager/commit/?id=78ce088843d59d4494965bfc40b30a2e63d065f6
- http://lists.fedoraproject.org/pipermail/package-announce/2011-June/061329.html
- http://www.openwall.com/lists/oss-security/2011/05/31/6
- http://www.openwall.com/lists/oss-security/2011/05/31/7
- https://bugzilla.redhat.com/show_bug.cgi?id=708876

---

#### 617. CVE-2011-4339

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: ipmitool_project:ipmitool, redhat:enterprise_linux

**漏洞描述 / Description**:
ipmievd (aka the IPMI event daemon) in OpenIPMI, as used in the ipmitool package 1.8.11 in Red Hat Enterprise Linux (RHEL) 6, Debian GNU/Linux, Fedora 16, and other products uses 0666 permissions for its ipmievd.pid PID file, which allows local users to kill arbitrary processes by writing to this file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2012-January/071575.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-January/071575.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-January/071580.html
- http://openwall.com/lists/oss-security/2011/12/13/1
- http://rhn.redhat.com/errata/RHSA-2013-0123.html
- http://secunia.com/advisories/47173

---

#### 618. CVE-2012-2653

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: lawrence_berkeley_national_laboratory:arpwatch

**漏洞描述 / Description**:
arpwatch 2.1a15, as used by Red Hat, Debian, Fedora, and possibly others, does not properly drop supplementary groups, which might allow attackers to gain root privileges by leveraging other vulnerabilities in the daemon.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082553.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082553.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082565.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-June/082569.html
- http://www.debian.org/security/2012/dsa-2481
- http://www.mandriva.com/security/advisories?name=MDVSA-2012:113

---

#### 619. CVE-2012-4453

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: redhat:enterprise_linux_workstation, dracut_project:dracut, redhat:enterprise_linux_desktop, fedoraproject:fedora, redhat:enterprise_linux_server

**漏洞描述 / Description**:
dracut.sh in dracut, as used in Red Hat Enterprise Linux 6, Fedora 16 and 17, and possibly other products, creates initramfs images with world-readable permissions, which might allow local users to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://git.kernel.org/?p=boot/dracut/dracut.git%3Ba=commit%3Bh=e1b48995c26c4f06d1a71.

**参考链接 / References**:
- http://git.kernel.org/?p=boot/dracut/dracut.git%3Ba=commit%3Bh=e1b48995c26c4f06d1a71
- http://rhn.redhat.com/errata/RHSA-2013-1674.html
- http://www.openwall.com/lists/oss-security/2012/09/27/3
- http://www.openwall.com/lists/oss-security/2012/09/27/4
- http://www.openwall.com/lists/oss-security/2012/09/27/6

---

#### 620. CVE-2012-3354

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: dokuwiki:dokuwiki, fedoraproject:fedora

**漏洞描述 / Description**:
doku.php in DokuWiki, as used in Fedora 16, 17, and 18, when certain PHP error levels are set, allows remote attackers to obtain sensitive information via the prefix parameter, which reveals the installation path in an error message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090755.html.

**参考链接 / References**:
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090755.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090899.html
- http://lists.fedoraproject.org/pipermail/package-announce/2012-October/090938.html
- http://www.freelists.org/post/dokuwiki/Fwd-DokuWiki-Full-path-disclosure
- http://www.mandriva.com/security/advisories?name=MDVSA-2013:073

---

#### 621. CVE-2016-5425

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: oracle:linux, redhat:enterprise_linux_server, redhat:enterprise_linux_workstation, redhat:enterprise_linux_desktop, apache:tomcat

**漏洞描述 / Description**:
The Tomcat package on Red Hat Enterprise Linux (RHEL) 7, Fedora, CentOS, Oracle Linux, and possibly other Linux distributions uses weak permissions for /usr/lib/tmpfiles.d/tomcat.conf, which allows local users to gain root privileges by leveraging membership in the tomcat group.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://legalhackers.com/advisories/Tomcat-RedHat-Pkgs-Root-PrivEsc-Exploit-CVE-2016-5425.html.

**参考链接 / References**:
- http://legalhackers.com/advisories/Tomcat-RedHat-Pkgs-Root-PrivEsc-Exploit-CVE-2016-5425.html
- http://packetstormsecurity.com/files/139041/Apache-Tomcat-8-7-6-Privilege-Escalation.html
- http://rhn.redhat.com/errata/RHSA-2016-2046.html
- http://www.openwall.com/lists/oss-security/2016/10/10/2
- http://www.oracle.com/technetwork/topics/security/linuxbulletinoct2016-3090545.html

---

#### 622. CVE-2017-5972

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The TCP stack in the Linux kernel 3.x does not properly implement a SYN cookie protection mechanism for the case of a fast network connection, which allows remote attackers to cause a denial of service (CPU consumption) by sending many TCP SYN packets, as demonstrated by an attack against the kernel-3.10.0 package in CentOS Linux 7. NOTE: third parties have been unable to discern any relationship between the GitHub Engineering finding and the Trigemini.c attack code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://seclists.org/oss-sec/2017/q1/573.

**参考链接 / References**:
- http://seclists.org/oss-sec/2017/q1/573
- http://www.securityfocus.com/bid/96231
- https://access.redhat.com/security/cve/cve-2017-5972
- https://bugzilla.redhat.com/show_bug.cgi?id=1422081
- https://cxsecurity.com/issue/WLB-2017020112

---

#### 623. CVE-2018-5961

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through v0.9.8.12 has XSS via the `module` value of the `index.php` file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.vulnerability-lab.com/get_content.php?id=1835.

**参考链接 / References**:
- https://www.vulnerability-lab.com/get_content.php?id=1835
- https://www.vulnerability-lab.com/get_content.php?id=1835

---

#### 624. CVE-2018-5962

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
index.php in CentOS-WebPanel.com (aka CWP) CentOS Web Panel through v0.9.8.12 has XSS via the id parameter to the phpini_editor module or the email_address parameter to the mail_add-new module.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.vulnerability-lab.com/get_content.php?id=1836.

**参考链接 / References**:
- https://www.vulnerability-lab.com/get_content.php?id=1836
- https://www.vulnerability-lab.com/get_content.php?id=1836

---

#### 625. CVE-2018-6926

**严重程度 / Severity**: HIGH | CVSS: 7.2
**受影响产品 / Affected Products**: misp:misp

**漏洞描述 / Description**:
In app/Controller/ServersController.php in MISP 2.4.87, a server setting permitted the override of a path variable on certain Red Hed Enterprise Linux and CentOS systems (where rh_shell_fix was enabled), and consequently allowed site admins to inject arbitrary OS commands. The impact is limited by the setting being only accessible to the site administrator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://github.com/MISP/MISP/commit/0a2aa9d52492d960b9a161160acedbe9caaa4126.

**参考链接 / References**:
- https://github.com/MISP/MISP/commit/0a2aa9d52492d960b9a161160acedbe9caaa4126
- https://github.com/MISP/MISP/commit/0a2aa9d52492d960b9a161160acedbe9caaa4126

---

#### 626. CVE-2018-17977

**严重程度 / Severity**: MEDIUM | CVSS: 4.4
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
The Linux kernel 4.14.67 mishandles certain interaction among XFRM Netlink messages, IPPROTO_AH packets, and IPPROTO_IP packets, which allows local users to cause a denial of service (memory consumption and system hang) by leveraging root access to execute crafted applications, as demonstrated on CentOS 7.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/105539.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105539
- https://www.openwall.com/lists/oss-security/2018/10/05/5
- http://www.securityfocus.com/bid/105539
- https://www.openwall.com/lists/oss-security/2018/10/05/5

---

#### 627. CVE-2018-18322

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has Command Injection via shell metacharacters in the admin/index.php service_start, service_restart, service_fullstatus, or service_stop parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://0day.today/exploit/31304.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 628. CVE-2018-18323

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has Local File Inclusion via directory traversal with an admin/index.php?module=file_editor&file=/../ URI.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://0day.today/exploit/31304.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 629. CVE-2018-18324

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.480 has XSS via the admin/fileManager2.php fm_current_dir parameter, or the admin/index.php module, service_start, service_fullstatus, service_restart, service_stop, or file (within the file_editor) parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://0day.today/exploit/31304.

**参考链接 / References**:
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/
- https://www.exploit-db.com/exploits/45610/
- https://0day.today/exploit/31304
- https://seccops.com/centos-web-panel-0-9-8-480-multiple-vulnerabilities/

---

#### 630. CVE-2018-18772

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows CSRF via admin/index.php?module=send_ssh, as demonstrated by executing an arbitrary OS command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 631. CVE-2018-18773

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows CSRF via admin/index.php?module=rootpwd, as demonstrated by changing the root password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 632. CVE-2018-18774

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.740 allows XSS via the admin/index.php module parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html
- https://www.exploit-db.com/exploits/45822/
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-Root-Account-Takeover-Command-Execution.html
- http://packetstormsecurity.com/files/150169/CentOS-Web-Panel-0.9.8.740-XSS-CSRF-Code-Execution.html

---

#### 633. CVE-2019-7646

**严重程度 / Severity**: MEDIUM | CVSS: 4.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.763 is vulnerable to Stored/Persistent XSS for the "Package Name" field via the add_package module parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/151630/CentOS-Web-Panel-0.9.8.763-Cross-Site-Scripting.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/151630/CentOS-Web-Panel-0.9.8.763-Cross-Site-Scripting.html
- https://www.dineshmohanty.com/centos-web-panel-xss
- https://www.exploit-db.com/exploits/46349/
- http://packetstormsecurity.com/files/151630/CentOS-Web-Panel-0.9.8.763-Cross-Site-Scripting.html
- https://www.dineshmohanty.com/centos-web-panel-xss

---

#### 634. CVE-2019-10261

**严重程度 / Severity**: MEDIUM | CVSS: 4.8
**受影响产品 / Affected Products**: centos-webpanel:centos_web_panel

**漏洞描述 / Description**:
CentOS Web Panel (CWP) 0.9.8.789 is vulnerable to Stored/Persistent XSS for the "Name Server 1" and "Name Server 2" fields via a "DNS Functions" "Edit Nameservers IPs" action.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/107769.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107769
- https://packetstormsecurity.com/files/152303/CentOS-Web-Panel-0.9.8.789-Cross-Site-Scripting.html
- https://www.exploit-db.com/exploits/46629
- http://www.securityfocus.com/bid/107769
- https://packetstormsecurity.com/files/152303/CentOS-Web-Panel-0.9.8.789-Cross-Site-Scripting.html

---

#### 635. CVE-2019-10893

**严重程度 / Severity**: MEDIUM | CVSS: 4.8
**受影响产品 / Affected Products**: centos-webpanel:centos_web_panel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.793 (Free/Open Source Version) and 0.9.8.753 (Pro) is vulnerable to Stored/Persistent XSS for Admin Email fields on the "CWP Settings > "Edit Settings" screen. By changing the email ID to any XSS Payload and clicking on Save Changes, the XSS Payload will execute.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://forum.centos-webpanel.com/informations/.

**参考链接 / References**:
- http://forum.centos-webpanel.com/informations/
- http://packetstormsecurity.com/files/152437/CentOS-Web-Panel-0.9.8.793-Free-0.9.8.753-Pro-Cross-Site-Scripting.html
- http://www.securityfocus.com/bid/108035
- https://packetstormsecurity.com/files/152437/centoswp098email-xss.txt
- https://www.exploit-db.com/exploits/46669

---

#### 636. CVE-2019-11429

**严重程度 / Severity**: MEDIUM | CVSS: 4.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.793 (Free/Open Source Version), 0.9.8.753 (Pro) and 0.9.8.807 (Pro) is vulnerable to Reflected XSS for the "Domain" field on the "DNS Functions > "Add DNS Zone" screen.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/152696/CentOS-Web-Panel-Domain-Field-Cross-Site-Scripting.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/152696/CentOS-Web-Panel-Domain-Field-Cross-Site-Scripting.html
- https://CentOS-WebPanel.com
- https://www.exploit-db.com/exploits/46784/
- http://packetstormsecurity.com/files/152696/CentOS-Web-Panel-Domain-Field-Cross-Site-Scripting.html
- https://CentOS-WebPanel.com

---

#### 637. CVE-2019-12190

**严重程度 / Severity**: MEDIUM | CVSS: 5.4
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
XSS was discovered in CentOS-WebPanel.com (aka CWP) CentOS Web Panel through 0.9.8.747 via the testacc/fileManager2.php fm_current_dir or filename parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://github.com/tuyenhva/CVE-2019-12190.

**参考链接 / References**:
- https://github.com/tuyenhva/CVE-2019-12190
- https://github.com/tuyenhva/CVE-2019-12190

---

#### 638. CVE-2019-13360

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.836, remote attackers can bypass authentication in the login process by leveraging knowledge of a valid username.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13360.md
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13360.md

---

#### 639. CVE-2019-13383

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, the Login process allows attackers to check whether a username is valid by reading the HTTP response.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153667/CentOS-Control-Web-Panel-0.9.8.838-User-Enumeration.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153667/CentOS-Control-Web-Panel-0.9.8.838-User-Enumeration.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13383.md
- https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2019-0010
- http://packetstormsecurity.com/files/153667/CentOS-Control-Web-Panel-0.9.8.838-User-Enumeration.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13383.md

---

#### 640. CVE-2019-13605

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.838 to 0.9.8.846, remote attackers can bypass authentication in the login process by leveraging the knowledge of a valid username. The attacker must defeat an encoding that is not equivalent to base64, and thus this is different from CVE-2019-13360.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13605.md
- https://www.exploit-db.com/exploits/47123
- http://packetstormsecurity.com/files/153665/CentOS-Control-Web-Panel-0.9.8.836-Authentication-Bypass.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13605.md

---

#### 641. CVE-2019-13359

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.836, a cwpsrv-xxx cookie allows a normal user to craft and upload a session file to the /tmp directory, and use it to become the root user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153666/CentOS-Control-Web-Panel-0.9.8.836-Privilege-Escalation.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153666/CentOS-Control-Web-Panel-0.9.8.836-Privilege-Escalation.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13359.md
- http://packetstormsecurity.com/files/153666/CentOS-Control-Web-Panel-0.9.8.836-Privilege-Escalation.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13359.md

---

#### 642. CVE-2019-13385

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.840, File and Directory Information Exposure in filemanager allows attackers to enumerate users and check for active users of the application by reading /tmp/login.log.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153877/CentOS-Control-Web-Panel-0.9.8.840-User-Enumeration.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153877/CentOS-Control-Web-Panel-0.9.8.840-User-Enumeration.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13385.md
- http://packetstormsecurity.com/files/153877/CentOS-Control-Web-Panel-0.9.8.840-User-Enumeration.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 643. CVE-2019-13386

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: centos-webpanel:centos_web_panel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, a hidden action=9 feature in filemanager2.php allows attackers to execute a shell command, i.e., obtain a reverse shell with user privilege.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153876/CentOS-Control-Web-Panel-0.9.8.836-Remote-Command-Execution.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153876/CentOS-Control-Web-Panel-0.9.8.836-Remote-Command-Execution.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13386.md
- http://packetstormsecurity.com/files/153876/CentOS-Control-Web-Panel-0.9.8.836-Remote-Command-Execution.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 644. CVE-2019-13387

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.846, Reflected XSS in filemanager2.php (parameter fm_current_dir) allows attackers to steal a cookie or session, or redirect to a phishing website.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/153878/CentOS-Control-Web-Panel-0.9.8.846-Cross-Site-Scripting.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/153878/CentOS-Control-Web-Panel-0.9.8.846-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13387.md
- http://packetstormsecurity.com/files/153878/CentOS-Control-Web-Panel-0.9.8.846-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 645. CVE-2019-13477

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.837, CSRF in the forgot password function allows an attacker to change the password for the root account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154217/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Request-Forgery.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154217/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Request-Forgery.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13477.md
- http://packetstormsecurity.com/files/154217/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Request-Forgery.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13477.md

---

#### 646. CVE-2019-13599

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.848, the Login process allows attackers to check whether a username is valid by comparing response times.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154164/CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154164/CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html
- http://packetstormsecurity.com/files/154164/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.848-User-Enumeration.html

---

#### 647. CVE-2019-14245

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: centos-webpanel:centos_web_panel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete databases (such as oauthv2) from the server via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154155/CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154155/CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- http://packetstormsecurity.com/files/154155/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- http://packetstormsecurity.com/files/154155/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154155/CentOS-Control-Web-Panel-CWP-0.9.8.851-Arbitrary-Database-Drop.html

---

#### 648. CVE-2019-14246

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: centos-webpanel:centos_web_panel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to discover phpMyAdmin passwords (of any user in /etc/passwd) via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154156/CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154156/CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- http://packetstormsecurity.com/files/154156/CentOS-WebPanel.com-CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- http://packetstormsecurity.com/files/154156/CentOS-WebPanel.com-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154156/CentOS-Control-Web-Panel-CWP-0.9.8.851-phpMyAdmin-Password-Change.html

---

#### 649. CVE-2019-13476

**严重程度 / Severity**: MEDIUM | CVSS: 5.4
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.837, XSS in the domain parameter allows a low-privilege user to achieve root access via the email list page.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154216/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Scripting.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154216/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Scripting.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13476.md
- http://packetstormsecurity.com/files/154216/CentOS-7.6.1810-Control-Web-Panel-0.9.8.837-Cross-Site-Scripting.html
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-13476.md

---

#### 650. CVE-2019-14721

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to remove a target user from phpMyAdmin via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14721.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14721.md

---

#### 651. CVE-2019-14722

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete an e-mail forwarding destination from a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14722.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14722.md

---

#### 652. CVE-2019-14723

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a victim's e-mail account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14723.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14723.md

---

#### 653. CVE-2019-14726

**严重程度 / Severity**: MEDIUM | CVSS: 5.4
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to access and delete DNS records of a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14726.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14726.md

---

#### 654. CVE-2019-14727

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to change the e-mail password of a victim account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14727.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14727.md

---

#### 655. CVE-2019-14728

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to add an e-mail forwarding destination to a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14728.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14728.md

---

#### 656. CVE-2019-14729

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a sub-domain from a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14729.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14729.md

---

#### 657. CVE-2019-14730

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to delete a domain from a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14730.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14730.md

---

#### 658. CVE-2019-14724

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to edit an e-mail forwarding destination of a victim's account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14724.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14724.md

---

#### 659. CVE-2019-14725

**严重程度 / Severity**: MEDIUM | CVSS: 4.3
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
In CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.851, an insecure object reference allows an attacker to change the e-mail usage value of a victim account via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14725.md
- https://packetstormsecurity.com/files/154404/Control-Web-Panel-0.9.8.851-Privilege-Escalation.html
- https://centos-webpanel.com/changelog-cwp7
- https://github.com/i3umi3iei3ii/CentOS-Control-Web-Panel-CVE/blob/master/CVE-2019-14725.md

---

#### 660. CVE-2019-16295

**严重程度 / Severity**: MEDIUM | CVSS: 4.6
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
Stored XSS in filemanager2.php in CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.885 exists via the cmd_arg parameter. This can be exploited by a local attacker who supplies a crafted filename within a directory visited by the victim.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/154990/CWP-0.9.8.885-Cross-Site-Scripting.html.

**参考链接 / References**:
- http://packetstormsecurity.com/files/154990/CWP-0.9.8.885-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7
- http://packetstormsecurity.com/files/154990/CWP-0.9.8.885-Cross-Site-Scripting.html
- https://centos-webpanel.com/changelog-cwp7

---

#### 661. CVE-2019-14782

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.856 through 0.9.8.864 allows an attacker to get a victim's session file name from the /tmp directory, and the victim's token value from /usr/local/cwpsrv/logs/access_log, then use them to make a request to extract the victim's password (for the OS and phpMyAdmin) via an attacker account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html

---

#### 662. CVE-2019-15235

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel 0.9.8.864 allows an attacker to get a victim's session file name from /home/[USERNAME]/tmp/session/sess_xxxxxx, and the victim's token value from /usr/local/cwpsrv/logs/access_log, then use them to gain access to the victim's password (for the OS and phpMyAdmin) via an attacker account. This is different from CVE-2019-14782.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html
- https://centos-webpanel.com/changelog-cwp7
- https://packetstormsecurity.com/files/155676/Control-Web-Panel-0.9.8.864-phpMyAdmin-Password-Disclosure.html

---

#### 663. CVE-2020-10230

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
CentOS-WebPanel.com (aka CWP) CentOS Web Panel (for CentOS 6 and 7) allows SQL Injection via the /cwp_{SESSION_HASH}/admin/loader_ajax.php term parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://centos-webpanel.com/changelog-cwp7.

**参考链接 / References**:
- https://centos-webpanel.com/changelog-cwp7
- https://www.exploit-db.com/exploits/48212
- https://centos-webpanel.com/changelog-cwp7
- https://www.exploit-db.com/exploits/48212

---

#### 664. CVE-2020-5291

**严重程度 / Severity**: HIGH | CVSS: 7.2
**受影响产品 / Affected Products**: projectatomic:bubblewrap, archlinux:arch_linux, debian:debian_linux, centos:centos

**漏洞描述 / Description**:
Bubblewrap (bwrap) before version 0.4.1, if installed in setuid mode and the kernel supports unprivileged user namespaces, then the `bwrap --userns2` option can be used to make the setuid process keep running as root while being traceable. This can in turn be used to gain root permissions. Note that this only affects the combination of bubblewrap in setuid mode (which is typically used when unprivileged user namespaces are not supported) and the support of unprivileged user namespaces. Known to be affected are: * Debian testing/unstable, if unprivileged user namespaces enabled (not default) * Debian buster-backports, if unprivileged user namespaces enabled (not default) * Arch if using `linux-hardened`, if unprivileged user namespaces enabled (not default) * Centos 7 flatpak COPR, if unprivileged user namespaces enabled (not default) This has been fixed in the 0.4.1 release, and all affected users should update.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://github.com/containers/bubblewrap/commit/1f7e2ad948c051054b683461885a0215f1806240.

**参考链接 / References**:
- https://github.com/containers/bubblewrap/commit/1f7e2ad948c051054b683461885a0215f1806240
- https://github.com/containers/bubblewrap/security/advisories/GHSA-j2qp-rvxj-43vj
- https://github.com/containers/bubblewrap/commit/1f7e2ad948c051054b683461885a0215f1806240
- https://github.com/containers/bubblewrap/security/advisories/GHSA-j2qp-rvxj-43vj

---

#### 665. CVE-2020-15420

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-el7-0.9.8.891. Authentication is not required to exploit this vulnerability. The specific flaw exists within loader_ajax.php. When parsing the line parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9259.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.zerodayinitiative.com/advisories/ZDI-20-737/.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-737/
- https://www.zerodayinitiative.com/advisories/ZDI-20-737/

---

#### 666. CVE-2020-15421

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the check_ip parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9707.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.zerodayinitiative.com/advisories/ZDI-20-738/.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-738/
- https://www.zerodayinitiative.com/advisories/ZDI-20-738/

---

#### 667. CVE-2020-15422

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the archivo parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9731.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.zerodayinitiative.com/advisories/ZDI-20-739/.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-739/
- https://www.zerodayinitiative.com/advisories/ZDI-20-739/

---

#### 668. CVE-2020-15423

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the dominio parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9732.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.zerodayinitiative.com/advisories/ZDI-20-740/.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-740/
- https://www.zerodayinitiative.com/advisories/ZDI-20-740/

---

#### 669. CVE-2020-15424

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: control-webpanel:webpanel

**漏洞描述 / Description**:
This vulnerability allows remote attackers to execute arbitrary code on affected installations of CentOS Web Panel cwp-e17.0.9.8.923. Authentication is not required to exploit this vulnerability. The specific flaw exists within ajax_mod_security.php. When parsing the domain parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-9735.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.zerodayinitiative.com/advisories/ZDI-20-741/.

**参考链接 / References**:
- https://www.zerodayinitiative.com/advisories/ZDI-20-741/
- https://www.zerodayinitiative.com/advisories/ZDI-20-741/

---
