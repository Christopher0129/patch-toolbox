# macOS 系统漏洞 | macOS System Vulnerabilities

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 03:00:21 UTC_

## 中文 🇨🇳
**macOS 系统漏洞**

本页面每小时自动抓取 MACOS 平台最新系统漏洞及应对措施。

### MACOS 漏洞列表

#### 1. CVE-1999-0142 (N/A)

**CVE编号**: CVE-1999-0142
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:java, netscape:navigator

**漏洞描述**:
The Java Applet Security Manager implementation in Netscape Navigator 2.0 and Java Developer's Kit 1.0 allows an applet to connect to arbitrary hosts.

**应对措施**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142.

**参考链接**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142

> 📎 来源 / Source: https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142

#### 2. CVE-1999-0141 (N/A)

**CVE编号**: CVE-1999-0141
**严重程度**: N/A CVSS: 3.7
受影响产品: netscape:navigator

**漏洞描述**:
Java Bytecode Verifier allows malicious applets to execute arbitrary commands as the user of the applet.

**应对措施**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134.

**参考链接**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134

> 📎 来源 / Source: http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134

#### 3. CVE-1999-1262 (N/A)

**CVE编号**: CVE-1999-1262
**严重程度**: N/A CVSS: 5.1
受影响产品: netscape:communicator

**漏洞描述**:
Java in Netscape 4.5 does not properly restrict applets from connecting to other hosts besides the one from which the applet was loaded, which violates the Java security model and could allow remote attackers to conduct unauthorized activities.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12231.

**参考链接**:
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727

> 📎 来源 / Source: http://www.securityfocus.com/archive/1/12231

#### 4. CVE-1999-1015 (N/A)

**CVE编号**: CVE-1999-1015
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:appleshare_mail_server

**漏洞描述**:
Buffer overflow in Apple AppleShare Mail Server 5.0.3 on MacOS 8.1 and earlier allows a remote attacker to cause a denial of service (crash) via a long HELO command.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89200657216213&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=89200657216213&w=2

#### 5. CVE-1999-1393 (N/A)

**CVE编号**: CVE-1999-1393
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:macos

**漏洞描述**:
Control Panel "Password Security" option for Apple Powerbooks allows attackers with physical access to the machine to bypass the security by booting it with an emergency startup disk and using a disk editor to modify the on/off toggle or password in the aaaaaaaAPWD file, which is normally inaccessible.

**应对措施**:
Apply patch from vendor. Monitor http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html.

**参考链接**:
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532

> 📎 来源 / Source: http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html

#### 6. CVE-1999-1412 (N/A)

**CVE编号**: CVE-1999-1412
**严重程度**: N/A CVSS: 5.0
受影响产品: apache:http_server, apple:macos

**漏洞描述**:
A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/14215.

**参考链接**:
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306

> 📎 来源 / Source: http://www.securityfocus.com/archive/1/14215

#### 7. CVE-1999-0766 (N/A)

**CVE编号**: CVE-1999-0766
**严重程度**: N/A CVSS: 9.3
受影响产品: microsoft:internet_explorer, microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**应对措施**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346.

**参考链接**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-031
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600

> 📎 来源 / Source: http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346

#### 8. CVE-2000-0327 (N/A)

**CVE编号**: CVE-2000-0327
**严重程度**: N/A CVSS: 7.6
受影响产品: microsoft:virtual_machine

**漏洞描述**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93993545118416&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=93993545118416&w=2

#### 9. CVE-1999-0793 (N/A)

**CVE编号**: CVE-1999-0793
**严重程度**: N/A CVSS: 2.6
受影响产品: microsoft:internet_explorer

**漏洞描述**:
Internet Explorer allows remote attackers to read files by redirecting data to a Javascript applet.

**应对措施**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043.

**参考链接**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043

> 📎 来源 / Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043

#### 10. CVE-2000-0162 (N/A)

**CVE编号**: CVE-2000-0162
**严重程度**: N/A CVSS: 5.1
受影响产品: microsoft:visual_studio, microsoft:internet_explorer, microsoft:ie

**漏洞描述**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011.

**参考链接**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

> 📎 来源 / Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

#### 11. CVE-2000-0237 (N/A)

**CVE编号**: CVE-2000-0237
**严重程度**: N/A CVSS: 6.4
受影响产品: netscape:enterprise_server

**漏洞描述**:
Netscape Enterprise Server with Web Publishing enabled allows remote attackers to list arbitrary directories via a GET request for the /publisher directory, which provides a Java applet that allows the attacker to browse the directories.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1075.

**参考链接**:
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1

> 📎 来源 / Source: http://www.securityfocus.com/bid/1075

#### 12. CVE-2000-0265 (N/A)

**CVE编号**: CVE-2000-0265
**严重程度**: N/A CVSS: 4.6
受影响产品: panda:panda_security

**漏洞描述**:
Panda Security 3.0 allows users to uninstall the Panda software via its Add/Remove Programs applet.

**应对措施**:
Apply patch from vendor. Monitor http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip.

**参考链接**:
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FB45F2.550EA000%40teleline.es
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119

> 📎 来源 / Source: http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip

#### 13. CVE-2000-0266 (N/A)

**CVE编号**: CVE-2000-0266
**严重程度**: N/A CVSS: 2.6
受影响产品: microsoft:internet_explorer

**漏洞描述**:
Internet Explorer 5.01 allows remote attackers to bypass the cross frame security policy via a malicious applet that interacts with the Java JSObject to modify the DOM properties to set the IFRAME to an arbitrary Javascript URL.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1121.

**参考链接**:
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg

> 📎 来源 / Source: http://www.securityfocus.com/bid/1121

#### 14. CVE-2000-0346 (N/A)

**CVE编号**: CVE-2000-0346
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:appleshare

**漏洞描述**:
AppleShare IP 6.1 and later allows a remote attacker to read potentially sensitive information via an invalid range request to the web server.

**应对措施**:
Apply patch from vendor. Monitor http://asu.info.apple.com/swupdates.nsf/artnum/n11670.

**参考链接**:
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000502133240.21807.qmail%40securityfocus.com
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162

> 📎 来源 / Source: http://asu.info.apple.com/swupdates.nsf/artnum/n11670

#### 15. CVE-2000-0676 (N/A)

**CVE编号**: CVE-2000-0676
**严重程度**: N/A CVSS: 5.0
受影响产品: netscape:communicator

**漏洞描述**:
Netscape Communicator and Navigator 4.04 through 4.74 allows remote attackers to read arbitrary files by using a Java applet to open a connection to a URL using the "file", "http", "https", and "ftp" protocols, as demonstrated by Brown Orifice.

**应对措施**:
Apply patch from vendor. Monitor ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc.

**参考链接**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0019.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0115.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0236.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0265.html

> 📎 来源 / Source: ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc

#### 16. CVE-2000-0711 (N/A)

**CVE编号**: CVE-2000-0711
**严重程度**: N/A CVSS: 7.5
受影响产品: netscape:communicator, microsoft:virtual_machine

**漏洞描述**:
Netscape Communicator does not properly prevent a ServerSocket object from being created by untrusted entities, which allows remote attackers to create a server on the victim's system via a malicious applet, as demonstrated by Brown Orifice.

**应对措施**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-15.html.

**参考链接**:
- http://www.cert.org/advisories/CA-2000-15.html
- http://www.securityfocus.com/bid/1545
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000805020429.11774.qmail%40securityfocus.com
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3999922128E.EE84TAKAGI%40java-house.etl.go.jp
- http://www.cert.org/advisories/CA-2000-15.html

> 📎 来源 / Source: http://www.cert.org/advisories/CA-2000-15.html

#### 17. CVE-2000-1061 (N/A)

**CVE编号**: CVE-2000-1061
**严重程度**: N/A CVSS: 5.1
受影响产品: microsoft:ie

**漏洞描述**:
Microsoft Virtual Machine (VM) in Internet Explorer 4.x and 5.x allows an unsigned applet to create and use ActiveX controls, which allows a remote attacker to bypass Internet Explorer's security settings and execute arbitrary commands via a malicious web page or email, aka the "Microsoft VM ActiveX Component" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075.

**参考链接**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127

> 📎 来源 / Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075

#### 18. CVE-2000-0889 (N/A)

**CVE编号**: CVE-2000-0889
**严重程度**: N/A CVSS: 5.1


**漏洞描述**:
Two Sun security certificates have been compromised, which could allow attackers to insert malicious code such as applets and make it appear that it is signed by Sun.

**应对措施**:
Apply patch from vendor. Monitor http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba.

**参考链接**:
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html

> 📎 来源 / Source: http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba

#### 19. CVE-2001-0068 (N/A)

**CVE编号**: CVE-2001-0068
**严重程度**: N/A CVSS: 2.6
受影响产品: apple:mac_os_runtime_for_java

**漏洞描述**:
Mac OS Runtime for Java (MRJ) 2.2.3 allows remote attackers to use malicious applets to read files outside of the CODEBASE context via the ARCHIVE applet parameter.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html

#### 20. CVE-2001-0137 (N/A)

**CVE编号**: CVE-2001-0137
**严重程度**: N/A CVSS: 5.1
受影响产品: microsoft:windows_media_player

**漏洞描述**:
Windows Media Player 7 allows remote attackers to execute malicious Java applets in Internet Explorer clients by enclosing the applet in a skin file named skin.wmz, then referencing that skin in the codebase parameter to an applet tag, aka the Windows Media Player Skins File Download" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97958100816503&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=97958100816503&w=2
- http://www.securityfocus.com/bid/2203
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-010
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5937
- http://marc.info/?l=bugtraq&m=97958100816503&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=97958100816503&w=2

#### 21. CVE-2001-0324 (N/A)

**CVE编号**: CVE-2001-0324
**严重程度**: N/A CVSS: 2.6
受影响产品: microsoft:windows_98, microsoft:windows_2000

**漏洞描述**:
Windows 98 and Windows 2000 Java clients allow remote attackers to cause a denial of service via a Java applet that opens a large number of UDP sockets, which prevents the host from establishing any additional UDP connections, and possibly causes a crash.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html.

**参考链接**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340

> 📎 来源 / Source: http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html

#### 22. CVE-2001-1026 (N/A)

**CVE编号**: CVE-2001-1026
**严重程度**: N/A CVSS: 7.5
受影响产品: trend_micro:interscan_applettrap

**漏洞描述**:
Trend Micro InterScan AppletTrap 2.0 does not properly filter URLs when they are modified in certain ways such as (1) using a double slash (//) instead of a single slash, (2) URL-encoded characters, (3) requesting the IP address instead of the domain name, or (4) using a leading 0 in an octet of an IP address.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html
- http://www.securityfocus.com/bid/2996
- http://www.securityfocus.com/bid/2998
- http://www.securityfocus.com/bid/3000
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6816

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html

#### 23. CVE-2001-1008 (N/A)

**CVE编号**: CVE-2001-1008
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:java_plug-in, sun:jre

**漏洞描述**:
Java Plugin 1.4 for JRE 1.3 executes signed applets even if the certificate is expired, which could allow remote attackers to conduct unauthorized activities via an applet that has been signed by an expired certificate.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php
- http://www.securityfocus.com/bid/3245
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html

#### 24. CVE-2001-1254 (N/A)

**CVE编号**: CVE-2001-1254
**严重程度**: N/A CVSS: 7.5
受影响产品: com2001:alexis_server

**漏洞描述**:
Web Access component for COM2001 Alexis 2.0 and 2.1 in InternetPBX sends username and voice mail passwords in the clear via a Java applet that sends the information to port 8888 of the server, which could allow remote attackers to steal the passwords via sniffing.

**应对措施**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/217200.

**参考链接**:
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373

> 📎 来源 / Source: http://online.securityfocus.com/archive/1/217200

#### 25. CVE-2001-0806 (N/A)

**CVE编号**: CVE-2001-0806
**严重程度**: N/A CVSS: 3.6
受影响产品: apple:mac_os_x

**漏洞描述**:
Apple MacOS X 10.0 and 10.1 allow a local user to read and write to a user's desktop folder via insecure default permissions for the Desktop when it is created in some languages.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99358249631139&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=99358249631139&w=2
- http://marc.info/?l=bugtraq&m=99436289015729&w=2
- http://online.securityfocus.com/archive/1/219166
- http://www.osvdb.org/1882
- http://www.securityfocus.com/bid/2930

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=99358249631139&w=2

#### 26. CVE-2001-1480 (N/A)

**CVE编号**: CVE-2001-1480
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:jdk, sun:jre, apple:mac_os_runtime_for_java, sun:sdk

**漏洞描述**:
Java Runtime Environment (JRE) and SDK 1.2 through 1.3.0_04 allows untrusted applets to access the system clipboard.

**应对措施**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html.

**参考链接**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/208&type=0&nav=sec.sba
- http://www.securityfocus.com/advisories/3617
- http://www.securityfocus.com/bid/3441
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7333

> 📎 来源 / Source: http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html

#### 27. CVE-2001-1575 (N/A)

**CVE编号**: CVE-2001-1575
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:personal_web_sharing

**漏洞描述**:
Apple Personal Web Sharing (PWS) 1.1, 1.5, and 1.5.5, when Web Sharing authentication is enabled, allows remote attackers to cause a denial of service via a long password, possibly due to a buffer overflow.

**应对措施**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html.

**参考链接**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6759
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945

> 📎 来源 / Source: http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html

#### 28. CVE-2002-1601 (N/A)

**CVE编号**: CVE-2002-1601
**严重程度**: N/A CVSS: 5.1
受影响产品: adobe:photodeluxe

**漏洞描述**:
The Connectables feature in Adobe PhotoDeluxe 3.1 prepends the Adobe directory to the CLASSPATH environment variable, which allows applets to run with higher privileges and remote attackers to gain privileges via an HTML e-mail message or a web page.

**应对措施**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/116875.

**参考链接**:
- http://www.kb.cert.org/vuls/id/116875
- http://www.kb.cert.org/vuls/id/AAMN-56LQ2J
- http://www.securityfocus.com/bid/4106
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8210
- http://www.kb.cert.org/vuls/id/116875

> 📎 来源 / Source: http://www.kb.cert.org/vuls/id/116875

#### 29. CVE-2002-0058 (N/A)

**CVE编号**: CVE-2002-0058
**严重程度**: N/A CVSS: 5.0
受影响产品: sun:jdk, sun:jre, microsoft:virtual_machine, sun:sdk

**漏洞描述**:
Vulnerability in Java Runtime Environment (JRE) allows remote malicious web sites to hijack or sniff a web client's sessions, when an HTTP proxy is being used, via a Java applet that redirects the session to another server, as seen in (1) Netscape 6.0 through 6.1 and 4.79 and earlier, (2) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, and possibly other implementations that use vulnerable versions of SDK or JDK.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101534535304228&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=101534535304228&w=2

#### 30. CVE-2002-0076 (N/A)

**CVE编号**: CVE-2002-0076
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:jre, sun:jdk, sun:sdk, hp:java_jre-jdk, microsoft:virtual_machine

**漏洞描述**:
Java Runtime Environment (JRE) Bytecode Verifier allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, as seen in (1) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, (2) Netscape 6.2.1 and earlier, and possibly other implementations that use vulnerable versions of SDK or JDK, aka a variant of the "Virtual Machine Verifier" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218.

**参考链接**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218
- http://www.iss.net/security_center/static/8480.php
- http://www.securityfocus.com/bid/4313
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218

> 📎 来源 / Source: http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218

#### 31. CVE-2002-0120 (N/A)

**CVE编号**: CVE-2002-0120
**严重程度**: N/A CVSS: 2.1
受影响产品: palm:palm_desktop

**漏洞描述**:
Apple Palm Desktop 4.0b76 and 4.0b77 creates world-readable backup files and folders when a hotsync is performed, which could allow a local user to obtain sensitive information.

**应对措施**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250093.

**参考链接**:
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php
- http://www.securityfocus.com/bid/3863
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php

> 📎 来源 / Source: http://online.securityfocus.com/archive/1/250093

#### 32. CVE-2002-0153 (N/A)

**CVE编号**: CVE-2002-0153
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:ie

**漏洞描述**:
Internet Explorer 5.1 for Macintosh allows remote attackers to bypass security checks and invoke local AppleScripts within a specific HTML element, aka the "Local Applescript Invocation" vulnerability.

**应对措施**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8851.php.

**参考链接**:
- http://www.iss.net/security_center/static/8851.php
- http://www.osvdb.org/5356
- http://www.securityfocus.com/archive/1/251805
- http://www.securityfocus.com/bid/3935
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-019

> 📎 来源 / Source: http://www.iss.net/security_center/static/8851.php

#### 33. CVE-2002-0252 (N/A)

**CVE编号**: CVE-2002-0252
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Buffer overflow in Apple QuickTime Player 5.01 and 5.02 allows remote web servers to execute arbitrary code via a response containing a long Content-Type MIME header.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101320742616105&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=101320742616105&w=2
- http://www.iss.net/security_center/static/8126.php
- http://www.securityfocus.com/bid/4064
- https://www.exploit-db.com/exploits/4673
- http://marc.info/?l=bugtraq&m=101320742616105&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=101320742616105&w=2

#### 34. CVE-2002-0676 (N/A)

**CVE编号**: CVE-2002-0676
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x

**漏洞描述**:
SoftwareUpdate for MacOS 10.1.x does not use authentication when downloading a software update, which could allow remote attackers to execute arbitrary code by posing as the Apple update server via techniques such as DNS spoofing or cache poisoning, and supplying Trojan Horse updates.

**应对措施**:
Apply patch from vendor. Monitor http://www.cunap.com/~hardingr/projects/osx/exploit.html.

**参考链接**:
- http://www.cunap.com/~hardingr/projects/osx/exploit.html
- http://www.iss.net/security_center/static/9502.php
- http://www.osvdb.org/5137
- http://www.securityfocus.com/bid/5176
- http://www.cunap.com/~hardingr/projects/osx/exploit.html

> 📎 来源 / Source: http://www.cunap.com/~hardingr/projects/osx/exploit.html

#### 35. CVE-2002-0376 (N/A)

**CVE编号**: CVE-2002-0376
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Buffer overflow in Apple QuickTime 5.0 ActiveX component allows remote attackers to execute arbitrary code via a long pluginspage field.

**应对措施**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293095.

**参考链接**:
- http://online.securityfocus.com/archive/1/293095
- http://www.atstake.com/research/advisories/2002/a091002-1.txt
- http://www.iss.net/security_center/static/10077.php
- http://www.securityfocus.com/bid/5685
- http://online.securityfocus.com/archive/1/293095

> 📎 来源 / Source: http://online.securityfocus.com/archive/1/293095

#### 36. CVE-2002-0976 (N/A)

**CVE编号**: CVE-2002-0976
**严重程度**: N/A CVSS: 6.4
受影响产品: microsoft:internet_explorer

**漏洞描述**:
Internet Explorer 4.0 and later allows remote attackers to read arbitrary files via a web page that accesses a legacy XML Datasource applet (com.ms.xml.dso.XMLDSO.class) and modifies the base URL to point to the local system, which is trusted by the applet.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102960731805373&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php
- http://www.securityfocus.com/bid/5490
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=102960731805373&w=2

#### 37. CVE-2002-0865 (N/A)

**CVE编号**: CVE-2002-0865
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:virtual_machine

**漏洞描述**:
A certain class that supports XML (Extensible Markup Language) in Microsoft Virtual Machine (VM) 5.0.3805 and earlier, probably com.ms.osp.ospmrshl, exposes certain unsafe methods, which allows remote attackers to execute unsafe code via a Java applet, aka "Inappropriate Methods Exposed in XML Support Classes."

**应对措施**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10135.php.

**参考链接**:
- http://www.iss.net/security_center/static/10135.php
- http://www.kb.cert.org/vuls/id/140898
- http://www.securityfocus.com/bid/5752
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10135.php

> 📎 来源 / Source: http://www.iss.net/security_center/static/10135.php

#### 38. CVE-2002-0866 (N/A)

**CVE编号**: CVE-2002-0866
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:virtual_machine

**漏洞描述**:
Java Database Connectivity (JDBC) classes in Microsoft Virtual Machine (VM) up to and including 5.0.3805 allow remote attackers to load and execute DLLs (dynamic link libraries) via a Java applet that calls the constructor for com.ms.jdbc.odbc.JdbcOdbc with the desired DLL terminated by a null string, aka "DLL Execution via JDBC Classes."

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html
- http://www.iss.net/security_center/static/10133.php
- http://www.kb.cert.org/vuls/id/307306
- http://www.securityfocus.com/bid/5751
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html

#### 39. CVE-2002-0867 (N/A)

**CVE编号**: CVE-2002-0867
**严重程度**: N/A CVSS: 5.0
受影响产品: microsoft:virtual_machine

**漏洞描述**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to cause a denial of service (crash) in Internet Explorer via invalid handle data in a Java applet, aka "Handle Validation Flaw."

**应对措施**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10134.php.

**参考链接**:
- http://www.iss.net/security_center/static/10134.php
- http://www.kb.cert.org/vuls/id/792881
- http://www.securityfocus.com/bid/5750
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10134.php

> 📎 来源 / Source: http://www.iss.net/security_center/static/10134.php

#### 40. CVE-2002-1286 (N/A)

**CVE编号**: CVE-2002-1286
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to steal cookies and execute script in a different security context via a URL that contains a colon in the domain portion, which is not properly parsed and loads an applet from a malicious site within the security context of the site that is being visited by the user.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/657625
- http://www.securityfocus.com/bid/6142
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10579

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 41. CVE-2002-1290 (N/A)

**CVE编号**: CVE-2002-1290
**严重程度**: N/A CVSS: 6.4
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read and modify the contents of the Clipboard via an applet that accesses the (1) ClipBoardGetText and (2) ClipBoardSetText methods of the INativeServices class.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10583.php
- http://www.securityfocus.com/bid/6132
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 42. CVE-2002-1291 (N/A)

**CVE编号**: CVE-2002-1291
**严重程度**: N/A CVSS: 5.0
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read arbitrary local files and network shares via an applet tag with a codebase set to a "file://%00" (null character) URL.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10584.php
- http://www.securityfocus.com/bid/6138
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 43. CVE-2002-1292 (N/A)

**CVE编号**: CVE-2002-1292
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java virtual machine (VM) build 5.0.3805 and earlier, as used in Internet Explorer, allows remote attackers to extend the Standard Security Manager (SSM) class (com.ms.security.StandardSecurityManager) and bypass intended StandardSecurityManager restrictions by modifying the (1) deniedDefinitionPackages or (2) deniedAccessPackages settings, causing a denial of service by adding Java applets to the list of applets that are prevented from running.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/237777
- http://www.securityfocus.com/bid/6133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 44. CVE-2002-1294 (N/A)

**CVE编号**: CVE-2002-1294
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java implementation, as used in Internet Explorer, can provide HTML object references to applets via Javascript, which allows remote attackers to cause a denial of service (crash due to illegal memory accesses) and possibly conduct other unauthorized activities via an applet that uses those references to access proprietary Microsoft methods.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10587.php
- http://www.securityfocus.com/bid/6135
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 45. CVE-2002-1295 (N/A)

**CVE编号**: CVE-2002-1295
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service (crash) and possibly conduct other unauthorized activities via applet tags in HTML that bypass Java class restrictions (such as private constructors) by providing the class name in the code parameter, aka "Incomplete Java Object Instantiation Vulnerability."

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10588.php
- http://www.securityfocus.com/bid/6136
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 46. CVE-2002-1257 (N/A)

**CVE编号**: CVE-2002-1257
**严重程度**: N/A CVSS: 10.0
受影响产品: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**漏洞描述**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to execute arbitrary code by including a Java applet that invokes COM (Component Object Model) objects in a web site or an HTML mail.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6371.

**参考链接**:
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 来源 / Source: http://www.securityfocus.com/bid/6371

#### 47. CVE-2002-1258 (N/A)

**CVE编号**: CVE-2002-1258
**严重程度**: N/A CVSS: 5.0
受影响产品: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**漏洞描述**:
Two vulnerabilities in Microsoft Virtual Machine (VM) up to and including build 5.0.3805, as used in Internet Explorer and other applications, allow remote attackers to read files via a Java applet with a spoofed location in the CODEBASE parameter in the APPLET tag, possibly due to a parsing error.

**应对措施**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069.

**参考链接**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582

> 📎 来源 / Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

#### 48. CVE-2002-1260 (N/A)

**CVE编号**: CVE-2002-1260
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**漏洞描述**:
The Java Database Connectivity (JDBC) APIs in Microsoft Virtual Machine (VM) 5.0.3805 and earlier allow remote attackers to bypass security checks and access database contents via an untrusted Java applet.

**应对措施**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-026.shtml.

**参考链接**:
- http://www.ciac.org/ciac/bulletins/n-026.shtml
- http://www.securityfocus.com/bid/6379
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10833
- http://www.ciac.org/ciac/bulletins/n-026.shtml

> 📎 来源 / Source: http://www.ciac.org/ciac/bulletins/n-026.shtml

#### 49. CVE-2002-1325 (N/A)

**CVE编号**: CVE-2002-1325
**严重程度**: N/A CVSS: 5.0
受影响产品: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**漏洞描述**:
Microsoft Virtual Machine (VM) build 5.0.3805 and earlier allows remote attackers to determine a local user's username via a Java applet that accesses the user.dir system property, aka "User.dir Exposure Vulnerability."

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6380.

**参考链接**:
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 来源 / Source: http://www.securityfocus.com/bid/6380

#### 50. CVE-2002-1898 (N/A)

**CVE编号**: CVE-2002-1898
**严重程度**: N/A CVSS: 7.2
受影响产品: apple:mac_os_x, apple:terminal

**漏洞描述**:
Terminal 1.3 in Apple Mac OS X 10.2 allows remote attackers to execute arbitrary commands via shell metacharacters in a telnet:// link, which is executed by Terminal.app window.

**应对措施**:
Apply patch from vendor. Monitor http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172.

**参考链接**:
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172
- http://lists.apple.com/archives/security-announce/2002/Sep/msg00001.html
- http://www.iss.net/security_center/static/10156.php
- http://www.securityfocus.com/bid/5768
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172

> 📎 来源 / Source: http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172


---

## English 🇺🇸
**macOS System Vulnerabilities**

Auto-updated hourly: latest MACOS system vulnerabilities and mitigations.

### MACOS Vulnerability List

#### 1. CVE-1999-0142 (N/A)

**CVE ID**: CVE-1999-0142
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:java, netscape:navigator

**Description**:
The Java Applet Security Manager implementation in Netscape Navigator 2.0 and Java Developer's Kit 1.0 allows an applet to connect to arbitrary hosts.

**Mitigation**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142.

**References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142

> 📎 Source: https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142

#### 2. CVE-1999-0141 (N/A)

**CVE ID**: CVE-1999-0141
**Severity**: N/A CVSS: 3.7
**Affected Products**: netscape:navigator

**Description**:
Java Bytecode Verifier allows malicious applets to execute arbitrary commands as the user of the applet.

**Mitigation**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134.

**References**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134

> 📎 Source: http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134

#### 3. CVE-1999-1262 (N/A)

**CVE ID**: CVE-1999-1262
**Severity**: N/A CVSS: 5.1
**Affected Products**: netscape:communicator

**Description**:
Java in Netscape 4.5 does not properly restrict applets from connecting to other hosts besides the one from which the applet was loaded, which violates the Java security model and could allow remote attackers to conduct unauthorized activities.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12231.

**References**:
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727
- http://www.securityfocus.com/archive/1/12231
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1727

> 📎 Source: http://www.securityfocus.com/archive/1/12231

#### 4. CVE-1999-1015 (N/A)

**CVE ID**: CVE-1999-1015
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:appleshare_mail_server

**Description**:
Buffer overflow in Apple AppleShare Mail Server 5.0.3 on MacOS 8.1 and earlier allows a remote attacker to cause a denial of service (crash) via a long HELO command.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89200657216213&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61
- http://marc.info/?l=bugtraq&m=89200657216213&w=2
- http://www.securityfocus.com/bid/61

> 📎 Source: http://marc.info/?l=bugtraq&m=89200657216213&w=2

#### 5. CVE-1999-1393 (N/A)

**CVE ID**: CVE-1999-1393
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:macos

**Description**:
Control Panel "Password Security" option for Apple Powerbooks allows attackers with physical access to the machine to bypass the security by booting it with an emergency startup disk and using a disk editor to modify the on/off toggle or password in the aaaaaaaAPWD file, which is normally inaccessible.

**Mitigation**:
Apply patch from vendor. Monitor http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html.

**References**:
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532
- http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html
- http://www.securityfocus.com/bid/532

> 📎 Source: http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html

#### 6. CVE-1999-1412 (N/A)

**CVE ID**: CVE-1999-1412
**Severity**: N/A CVSS: 5.0
**Affected Products**: apache:http_server, apple:macos

**Description**:
A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/14215.

**References**:
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306
- http://www.securityfocus.com/archive/1/14215
- http://www.securityfocus.com/bid/306

> 📎 Source: http://www.securityfocus.com/archive/1/14215

#### 7. CVE-1999-0766 (N/A)

**CVE ID**: CVE-1999-0766
**Severity**: N/A CVSS: 9.3
**Affected Products**: microsoft:internet_explorer, microsoft:java_virtual_machine

**Description**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**Mitigation**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346.

**References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-031
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600

> 📎 Source: http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346

#### 8. CVE-2000-0327 (N/A)

**CVE ID**: CVE-2000-0327
**Severity**: N/A CVSS: 7.6
**Affected Products**: microsoft:virtual_machine

**Description**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93993545118416&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045

> 📎 Source: http://marc.info/?l=bugtraq&m=93993545118416&w=2

#### 9. CVE-1999-0793 (N/A)

**CVE ID**: CVE-1999-0793
**Severity**: N/A CVSS: 2.6
**Affected Products**: microsoft:internet_explorer

**Description**:
Internet Explorer allows remote attackers to read files by redirecting data to a Javascript applet.

**Mitigation**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043.

**References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043

> 📎 Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043

#### 10. CVE-2000-0162 (N/A)

**CVE ID**: CVE-2000-0162
**Severity**: N/A CVSS: 5.1
**Affected Products**: microsoft:visual_studio, microsoft:internet_explorer, microsoft:ie

**Description**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011.

**References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

> 📎 Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

#### 11. CVE-2000-0237 (N/A)

**CVE ID**: CVE-2000-0237
**Severity**: N/A CVSS: 6.4
**Affected Products**: netscape:enterprise_server

**Description**:
Netscape Enterprise Server with Web Publishing enabled allows remote attackers to list arbitrary directories via a GET request for the /publisher directory, which provides a Java applet that allows the attacker to browse the directories.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1075.

**References**:
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1
- http://www.securityfocus.com/bid/1075
- http://zsh.stupidphat.com/advisory.cgi?000311-1

> 📎 Source: http://www.securityfocus.com/bid/1075

#### 12. CVE-2000-0265 (N/A)

**CVE ID**: CVE-2000-0265
**Severity**: N/A CVSS: 4.6
**Affected Products**: panda:panda_security

**Description**:
Panda Security 3.0 allows users to uninstall the Panda software via its Add/Remove Programs applet.

**Mitigation**:
Apply patch from vendor. Monitor http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip.

**References**:
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FB45F2.550EA000%40teleline.es
- http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip
- http://www.securityfocus.com/bid/1119

> 📎 Source: http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip

#### 13. CVE-2000-0266 (N/A)

**CVE ID**: CVE-2000-0266
**Severity**: N/A CVSS: 2.6
**Affected Products**: microsoft:internet_explorer

**Description**:
Internet Explorer 5.01 allows remote attackers to bypass the cross frame security policy via a malicious applet that interacts with the Java JSObject to modify the DOM properties to set the IFRAME to an arbitrary Javascript URL.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1121.

**References**:
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg
- http://www.securityfocus.com/bid/1121
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=38FC6130.D6D178FD%40nat.bg

> 📎 Source: http://www.securityfocus.com/bid/1121

#### 14. CVE-2000-0346 (N/A)

**CVE ID**: CVE-2000-0346
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:appleshare

**Description**:
AppleShare IP 6.1 and later allows a remote attacker to read potentially sensitive information via an invalid range request to the web server.

**Mitigation**:
Apply patch from vendor. Monitor http://asu.info.apple.com/swupdates.nsf/artnum/n11670.

**References**:
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000502133240.21807.qmail%40securityfocus.com
- http://asu.info.apple.com/swupdates.nsf/artnum/n11670
- http://www.securityfocus.com/bid/1162

> 📎 Source: http://asu.info.apple.com/swupdates.nsf/artnum/n11670

#### 15. CVE-2000-0676 (N/A)

**CVE ID**: CVE-2000-0676
**Severity**: N/A CVSS: 5.0
**Affected Products**: netscape:communicator

**Description**:
Netscape Communicator and Navigator 4.04 through 4.74 allows remote attackers to read arbitrary files by using a Java applet to open a connection to a URL using the "file", "http", "https", and "ftp" protocols, as demonstrated by Brown Orifice.

**Mitigation**:
Apply patch from vendor. Monitor ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc.

**References**:
- ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0019.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0115.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0236.html
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0265.html

> 📎 Source: ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc

#### 16. CVE-2000-0711 (N/A)

**CVE ID**: CVE-2000-0711
**Severity**: N/A CVSS: 7.5
**Affected Products**: netscape:communicator, microsoft:virtual_machine

**Description**:
Netscape Communicator does not properly prevent a ServerSocket object from being created by untrusted entities, which allows remote attackers to create a server on the victim's system via a malicious applet, as demonstrated by Brown Orifice.

**Mitigation**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-15.html.

**References**:
- http://www.cert.org/advisories/CA-2000-15.html
- http://www.securityfocus.com/bid/1545
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000805020429.11774.qmail%40securityfocus.com
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3999922128E.EE84TAKAGI%40java-house.etl.go.jp
- http://www.cert.org/advisories/CA-2000-15.html

> 📎 Source: http://www.cert.org/advisories/CA-2000-15.html

#### 17. CVE-2000-1061 (N/A)

**CVE ID**: CVE-2000-1061
**Severity**: N/A CVSS: 5.1
**Affected Products**: microsoft:ie

**Description**:
Microsoft Virtual Machine (VM) in Internet Explorer 4.x and 5.x allows an unsigned applet to create and use ActiveX controls, which allows a remote attacker to bypass Internet Explorer's security settings and execute arbitrary commands via a malicious web page or email, aka the "Microsoft VM ActiveX Component" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075.

**References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5127

> 📎 Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075

#### 18. CVE-2000-0889 (N/A)

**CVE ID**: CVE-2000-0889
**Severity**: N/A CVSS: 5.1
**Affected Products**: N/A

**Description**:
Two Sun security certificates have been compromised, which could allow attackers to insert malicious code such as applets and make it appear that it is signed by Sun.

**Mitigation**:
Apply patch from vendor. Monitor http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba.

**References**:
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html
- http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba
- http://www.cert.org/advisories/CA-2000-19.html

> 📎 Source: http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba

#### 19. CVE-2001-0068 (N/A)

**CVE ID**: CVE-2001-0068
**Severity**: N/A CVSS: 2.6
**Affected Products**: apple:mac_os_runtime_for_java

**Description**:
Mac OS Runtime for Java (MRJ) 2.2.3 allows remote attackers to use malicious applets to read files outside of the CODEBASE context via the ARCHIVE applet parameter.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5784

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html

#### 20. CVE-2001-0137 (N/A)

**CVE ID**: CVE-2001-0137
**Severity**: N/A CVSS: 5.1
**Affected Products**: microsoft:windows_media_player

**Description**:
Windows Media Player 7 allows remote attackers to execute malicious Java applets in Internet Explorer clients by enclosing the applet in a skin file named skin.wmz, then referencing that skin in the codebase parameter to an applet tag, aka the Windows Media Player Skins File Download" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97958100816503&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=97958100816503&w=2
- http://www.securityfocus.com/bid/2203
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-010
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5937
- http://marc.info/?l=bugtraq&m=97958100816503&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=97958100816503&w=2

#### 21. CVE-2001-0324 (N/A)

**CVE ID**: CVE-2001-0324
**Severity**: N/A CVSS: 2.6
**Affected Products**: microsoft:windows_98, microsoft:windows_2000

**Description**:
Windows 98 and Windows 2000 Java clients allow remote attackers to cause a denial of service via a Java applet that opens a large number of UDP sockets, which prevents the host from establishing any additional UDP connections, and possibly causes a crash.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html.

**References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340
- http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html
- http://www.securityfocus.com/bid/2340

> 📎 Source: http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html

#### 22. CVE-2001-1026 (N/A)

**CVE ID**: CVE-2001-1026
**Severity**: N/A CVSS: 7.5
**Affected Products**: trend_micro:interscan_applettrap

**Description**:
Trend Micro InterScan AppletTrap 2.0 does not properly filter URLs when they are modified in certain ways such as (1) using a double slash (//) instead of a single slash, (2) URL-encoded characters, (3) requesting the IP address instead of the domain name, or (4) using a leading 0 in an octet of an IP address.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html
- http://www.securityfocus.com/bid/2996
- http://www.securityfocus.com/bid/2998
- http://www.securityfocus.com/bid/3000
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6816

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html

#### 23. CVE-2001-1008 (N/A)

**CVE ID**: CVE-2001-1008
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:java_plug-in, sun:jre

**Description**:
Java Plugin 1.4 for JRE 1.3 executes signed applets even if the certificate is expired, which could allow remote attackers to conduct unauthorized activities via an applet that has been signed by an expired certificate.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php
- http://www.securityfocus.com/bid/3245
- http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html
- http://www.iss.net/security_center/static/7048.php

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html

#### 24. CVE-2001-1254 (N/A)

**CVE ID**: CVE-2001-1254
**Severity**: N/A CVSS: 7.5
**Affected Products**: com2001:alexis_server

**Description**:
Web Access component for COM2001 Alexis 2.0 and 2.1 in InternetPBX sends username and voice mail passwords in the clear via a Java applet that sends the information to port 8888 of the server, which could allow remote attackers to steal the passwords via sniffing.

**Mitigation**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/217200.

**References**:
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373
- http://online.securityfocus.com/archive/1/217200
- http://www.securityfocus.com/bid/3373

> 📎 Source: http://online.securityfocus.com/archive/1/217200

#### 25. CVE-2001-0806 (N/A)

**CVE ID**: CVE-2001-0806
**Severity**: N/A CVSS: 3.6
**Affected Products**: apple:mac_os_x

**Description**:
Apple MacOS X 10.0 and 10.1 allow a local user to read and write to a user's desktop folder via insecure default permissions for the Desktop when it is created in some languages.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99358249631139&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=99358249631139&w=2
- http://marc.info/?l=bugtraq&m=99436289015729&w=2
- http://online.securityfocus.com/archive/1/219166
- http://www.osvdb.org/1882
- http://www.securityfocus.com/bid/2930

> 📎 Source: http://marc.info/?l=bugtraq&m=99358249631139&w=2

#### 26. CVE-2001-1480 (N/A)

**CVE ID**: CVE-2001-1480
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:jdk, sun:jre, apple:mac_os_runtime_for_java, sun:sdk

**Description**:
Java Runtime Environment (JRE) and SDK 1.2 through 1.3.0_04 allows untrusted applets to access the system clipboard.

**Mitigation**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html.

**References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/208&type=0&nav=sec.sba
- http://www.securityfocus.com/advisories/3617
- http://www.securityfocus.com/bid/3441
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7333

> 📎 Source: http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html

#### 27. CVE-2001-1575 (N/A)

**CVE ID**: CVE-2001-1575
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:personal_web_sharing

**Description**:
Apple Personal Web Sharing (PWS) 1.1, 1.5, and 1.5.5, when Web Sharing authentication is enabled, allows remote attackers to cause a denial of service via a long password, possibly due to a buffer overflow.

**Mitigation**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html.

**References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6759
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html
- http://www.securityfocus.com/bid/2945

> 📎 Source: http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html

#### 28. CVE-2002-1601 (N/A)

**CVE ID**: CVE-2002-1601
**Severity**: N/A CVSS: 5.1
**Affected Products**: adobe:photodeluxe

**Description**:
The Connectables feature in Adobe PhotoDeluxe 3.1 prepends the Adobe directory to the CLASSPATH environment variable, which allows applets to run with higher privileges and remote attackers to gain privileges via an HTML e-mail message or a web page.

**Mitigation**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/116875.

**References**:
- http://www.kb.cert.org/vuls/id/116875
- http://www.kb.cert.org/vuls/id/AAMN-56LQ2J
- http://www.securityfocus.com/bid/4106
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8210
- http://www.kb.cert.org/vuls/id/116875

> 📎 Source: http://www.kb.cert.org/vuls/id/116875

#### 29. CVE-2002-0058 (N/A)

**CVE ID**: CVE-2002-0058
**Severity**: N/A CVSS: 5.0
**Affected Products**: sun:jdk, sun:jre, microsoft:virtual_machine, sun:sdk

**Description**:
Vulnerability in Java Runtime Environment (JRE) allows remote malicious web sites to hijack or sniff a web client's sessions, when an HTTP proxy is being used, via a Java applet that redirects the session to another server, as seen in (1) Netscape 6.0 through 6.1 and 4.79 and earlier, (2) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, and possibly other implementations that use vulnerable versions of SDK or JDK.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101534535304228&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://marc.info/?l=bugtraq&m=101534535304228&w=2
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/216

> 📎 Source: http://marc.info/?l=bugtraq&m=101534535304228&w=2

#### 30. CVE-2002-0076 (N/A)

**CVE ID**: CVE-2002-0076
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:jre, sun:jdk, sun:sdk, hp:java_jre-jdk, microsoft:virtual_machine

**Description**:
Java Runtime Environment (JRE) Bytecode Verifier allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, as seen in (1) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, (2) Netscape 6.2.1 and earlier, and possibly other implementations that use vulnerable versions of SDK or JDK, aka a variant of the "Virtual Machine Verifier" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218.

**References**:
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218
- http://www.iss.net/security_center/static/8480.php
- http://www.securityfocus.com/bid/4313
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-013
- http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218

> 📎 Source: http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218

#### 31. CVE-2002-0120 (N/A)

**CVE ID**: CVE-2002-0120
**Severity**: N/A CVSS: 2.1
**Affected Products**: palm:palm_desktop

**Description**:
Apple Palm Desktop 4.0b76 and 4.0b77 creates world-readable backup files and folders when a hotsync is performed, which could allow a local user to obtain sensitive information.

**Mitigation**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250093.

**References**:
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php
- http://www.securityfocus.com/bid/3863
- http://online.securityfocus.com/archive/1/250093
- http://www.iss.net/security_center/static/7937.php

> 📎 Source: http://online.securityfocus.com/archive/1/250093

#### 32. CVE-2002-0153 (N/A)

**CVE ID**: CVE-2002-0153
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:ie

**Description**:
Internet Explorer 5.1 for Macintosh allows remote attackers to bypass security checks and invoke local AppleScripts within a specific HTML element, aka the "Local Applescript Invocation" vulnerability.

**Mitigation**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8851.php.

**References**:
- http://www.iss.net/security_center/static/8851.php
- http://www.osvdb.org/5356
- http://www.securityfocus.com/archive/1/251805
- http://www.securityfocus.com/bid/3935
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-019

> 📎 Source: http://www.iss.net/security_center/static/8851.php

#### 33. CVE-2002-0252 (N/A)

**CVE ID**: CVE-2002-0252
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Buffer overflow in Apple QuickTime Player 5.01 and 5.02 allows remote web servers to execute arbitrary code via a response containing a long Content-Type MIME header.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101320742616105&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=101320742616105&w=2
- http://www.iss.net/security_center/static/8126.php
- http://www.securityfocus.com/bid/4064
- https://www.exploit-db.com/exploits/4673
- http://marc.info/?l=bugtraq&m=101320742616105&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=101320742616105&w=2

#### 34. CVE-2002-0676 (N/A)

**CVE ID**: CVE-2002-0676
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x

**Description**:
SoftwareUpdate for MacOS 10.1.x does not use authentication when downloading a software update, which could allow remote attackers to execute arbitrary code by posing as the Apple update server via techniques such as DNS spoofing or cache poisoning, and supplying Trojan Horse updates.

**Mitigation**:
Apply patch from vendor. Monitor http://www.cunap.com/~hardingr/projects/osx/exploit.html.

**References**:
- http://www.cunap.com/~hardingr/projects/osx/exploit.html
- http://www.iss.net/security_center/static/9502.php
- http://www.osvdb.org/5137
- http://www.securityfocus.com/bid/5176
- http://www.cunap.com/~hardingr/projects/osx/exploit.html

> 📎 Source: http://www.cunap.com/~hardingr/projects/osx/exploit.html

#### 35. CVE-2002-0376 (N/A)

**CVE ID**: CVE-2002-0376
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Buffer overflow in Apple QuickTime 5.0 ActiveX component allows remote attackers to execute arbitrary code via a long pluginspage field.

**Mitigation**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293095.

**References**:
- http://online.securityfocus.com/archive/1/293095
- http://www.atstake.com/research/advisories/2002/a091002-1.txt
- http://www.iss.net/security_center/static/10077.php
- http://www.securityfocus.com/bid/5685
- http://online.securityfocus.com/archive/1/293095

> 📎 Source: http://online.securityfocus.com/archive/1/293095

#### 36. CVE-2002-0976 (N/A)

**CVE ID**: CVE-2002-0976
**Severity**: N/A CVSS: 6.4
**Affected Products**: microsoft:internet_explorer

**Description**:
Internet Explorer 4.0 and later allows remote attackers to read arbitrary files via a web page that accesses a legacy XML Datasource applet (com.ms.xml.dso.XMLDSO.class) and modifies the base URL to point to the local system, which is trusted by the applet.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102960731805373&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php
- http://www.securityfocus.com/bid/5490
- http://marc.info/?l=bugtraq&m=102960731805373&w=2
- http://www.iss.net/security_center/static/9885.php

> 📎 Source: http://marc.info/?l=bugtraq&m=102960731805373&w=2

#### 37. CVE-2002-0865 (N/A)

**CVE ID**: CVE-2002-0865
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:virtual_machine

**Description**:
A certain class that supports XML (Extensible Markup Language) in Microsoft Virtual Machine (VM) 5.0.3805 and earlier, probably com.ms.osp.ospmrshl, exposes certain unsafe methods, which allows remote attackers to execute unsafe code via a Java applet, aka "Inappropriate Methods Exposed in XML Support Classes."

**Mitigation**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10135.php.

**References**:
- http://www.iss.net/security_center/static/10135.php
- http://www.kb.cert.org/vuls/id/140898
- http://www.securityfocus.com/bid/5752
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10135.php

> 📎 Source: http://www.iss.net/security_center/static/10135.php

#### 38. CVE-2002-0866 (N/A)

**CVE ID**: CVE-2002-0866
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:virtual_machine

**Description**:
Java Database Connectivity (JDBC) classes in Microsoft Virtual Machine (VM) up to and including 5.0.3805 allow remote attackers to load and execute DLLs (dynamic link libraries) via a Java applet that calls the constructor for com.ms.jdbc.odbc.JdbcOdbc with the desired DLL terminated by a null string, aka "DLL Execution via JDBC Classes."

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html
- http://www.iss.net/security_center/static/10133.php
- http://www.kb.cert.org/vuls/id/307306
- http://www.securityfocus.com/bid/5751
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html

#### 39. CVE-2002-0867 (N/A)

**CVE ID**: CVE-2002-0867
**Severity**: N/A CVSS: 5.0
**Affected Products**: microsoft:virtual_machine

**Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to cause a denial of service (crash) in Internet Explorer via invalid handle data in a Java applet, aka "Handle Validation Flaw."

**Mitigation**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10134.php.

**References**:
- http://www.iss.net/security_center/static/10134.php
- http://www.kb.cert.org/vuls/id/792881
- http://www.securityfocus.com/bid/5750
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-052
- http://www.iss.net/security_center/static/10134.php

> 📎 Source: http://www.iss.net/security_center/static/10134.php

#### 40. CVE-2002-1286 (N/A)

**CVE ID**: CVE-2002-1286
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to steal cookies and execute script in a different security context via a URL that contains a colon in the domain portion, which is not properly parsed and loads an applet from a malicious site within the security context of the site that is being visited by the user.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/657625
- http://www.securityfocus.com/bid/6142
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10579

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 41. CVE-2002-1290 (N/A)

**CVE ID**: CVE-2002-1290
**Severity**: N/A CVSS: 6.4
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read and modify the contents of the Clipboard via an applet that accesses the (1) ClipBoardGetText and (2) ClipBoardSetText methods of the INativeServices class.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10583.php
- http://www.securityfocus.com/bid/6132
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 42. CVE-2002-1291 (N/A)

**CVE ID**: CVE-2002-1291
**Severity**: N/A CVSS: 5.0
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read arbitrary local files and network shares via an applet tag with a codebase set to a "file://%00" (null character) URL.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10584.php
- http://www.securityfocus.com/bid/6138
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 43. CVE-2002-1292 (N/A)

**CVE ID**: CVE-2002-1292
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java virtual machine (VM) build 5.0.3805 and earlier, as used in Internet Explorer, allows remote attackers to extend the Standard Security Manager (SSM) class (com.ms.security.StandardSecurityManager) and bypass intended StandardSecurityManager restrictions by modifying the (1) deniedDefinitionPackages or (2) deniedAccessPackages settings, causing a denial of service by adding Java applets to the list of applets that are prevented from running.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.kb.cert.org/vuls/id/237777
- http://www.securityfocus.com/bid/6133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 44. CVE-2002-1294 (N/A)

**CVE ID**: CVE-2002-1294
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java implementation, as used in Internet Explorer, can provide HTML object references to applets via Javascript, which allows remote attackers to cause a denial of service (crash due to illegal memory accesses) and possibly conduct other unauthorized activities via an applet that uses those references to access proprietary Microsoft methods.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10587.php
- http://www.securityfocus.com/bid/6135
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 45. CVE-2002-1295 (N/A)

**CVE ID**: CVE-2002-1295
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:java_virtual_machine

**Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service (crash) and possibly conduct other unauthorized activities via applet tags in HTML that bypass Java class restrictions (such as private constructors) by providing the class name in the code parameter, aka "Incomplete Java Object Instantiation Vulnerability."

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10588.php
- http://www.securityfocus.com/bid/6136
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 Source: http://marc.info/?l=bugtraq&m=103682630823080&w=2

#### 46. CVE-2002-1257 (N/A)

**CVE ID**: CVE-2002-1257
**Severity**: N/A CVSS: 10.0
**Affected Products**: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to execute arbitrary code by including a Java applet that invokes COM (Component Object Model) objects in a web site or an HTML mail.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6371.

**References**:
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6371
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 Source: http://www.securityfocus.com/bid/6371

#### 47. CVE-2002-1258 (N/A)

**CVE ID**: CVE-2002-1258
**Severity**: N/A CVSS: 5.0
**Affected Products**: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**Description**:
Two vulnerabilities in Microsoft Virtual Machine (VM) up to and including build 5.0.3805, as used in Internet Explorer and other applications, allow remote attackers to read files via a Java applet with a spoofed location in the CODEBASE parameter in the APPLET tag, possibly due to a parsing error.

**Mitigation**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069.

**References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A582

> 📎 Source: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

#### 48. CVE-2002-1260 (N/A)

**CVE ID**: CVE-2002-1260
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**Description**:
The Java Database Connectivity (JDBC) APIs in Microsoft Virtual Machine (VM) 5.0.3805 and earlier allow remote attackers to bypass security checks and access database contents via an untrusted Java applet.

**Mitigation**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-026.shtml.

**References**:
- http://www.ciac.org/ciac/bulletins/n-026.shtml
- http://www.securityfocus.com/bid/6379
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10833
- http://www.ciac.org/ciac/bulletins/n-026.shtml

> 📎 Source: http://www.ciac.org/ciac/bulletins/n-026.shtml

#### 49. CVE-2002-1325 (N/A)

**CVE ID**: CVE-2002-1325
**Severity**: N/A CVSS: 5.0
**Affected Products**: microsoft:windows_me, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_98se

**Description**:
Microsoft Virtual Machine (VM) build 5.0.3805 and earlier allows remote attackers to determine a local user's username via a Java applet that accesses the user.dir system property, aka "User.dir Exposure Vulnerability."

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6380.

**References**:
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069
- http://www.securityfocus.com/bid/6380
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069

> 📎 Source: http://www.securityfocus.com/bid/6380

#### 50. CVE-2002-1898 (N/A)

**CVE ID**: CVE-2002-1898
**Severity**: N/A CVSS: 7.2
**Affected Products**: apple:mac_os_x, apple:terminal

**Description**:
Terminal 1.3 in Apple Mac OS X 10.2 allows remote attackers to execute arbitrary commands via shell metacharacters in a telnet:// link, which is executed by Terminal.app window.

**Mitigation**:
Apply patch from vendor. Monitor http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172.

**References**:
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172
- http://lists.apple.com/archives/security-announce/2002/Sep/msg00001.html
- http://www.iss.net/security_center/static/10156.php
- http://www.securityfocus.com/bid/5768
- http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172

> 📎 Source: http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
