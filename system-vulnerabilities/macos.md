# macOS 系统漏洞 | macOS System Vulnerabilities

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 04:27:26 UTC_

## 中文 🇨🇳
**macOS 系统漏洞**

本页面每小时自动抓取 MACOS 平台最新系统漏洞及应对措施。

### MACOS 漏洞列表

#### 1. CVE-1999-0142 (N/A)

**CVE编号**: CVE-1999-0142
**严重程度**: N/A CVSS: 7.5
受影响产品: netscape:navigator, sun:java

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
受影响产品: apple:macos, apache:http_server

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
受影响产品: microsoft:internet_explorer, microsoft:visual_studio, microsoft:ie

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
受影响产品: sun:jre, sun:sdk, apple:mac_os_runtime_for_java, sun:jdk

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
受影响产品: sun:jre, microsoft:virtual_machine, sun:sdk, sun:jdk

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
受影响产品: sun:jre, hp:java_jre-jdk, sun:sdk, microsoft:virtual_machine, sun:jdk

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
受影响产品: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
受影响产品: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
受影响产品: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
受影响产品: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
受影响产品: apple:terminal, apple:mac_os_x

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

#### 51. CVE-2002-2184 (N/A)

**CVE编号**: CVE-2002-2184
**严重程度**: N/A CVSS: 5.0
受影响产品: digi-net_technologies:digichat

**漏洞描述**:
Digi-Net Technologies DigiChat 3.5 allows chat users to obtain the IP addresses of other chat users via a "Showip" parameter in the chat applet.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5019.

**参考链接**:
- http://www.securityfocus.com/bid/5019
- http://www.securityfocus.com/bid/5019

> 📎 来源 / Source: http://www.securityfocus.com/bid/5019

#### 52. CVE-2002-2242 (N/A)

**CVE编号**: CVE-2002-2242
**严重程度**: N/A CVSS: 6.4
受影响产品: kismac:kismac

**漏洞描述**:
The Apple Package Manager in KisMAC 0.02a and earlier modifies file permissions of sensitive files after installation, which could allow attackers to conduct unauthorized activities on those files.

**应对措施**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1005764.

**参考链接**:
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10813
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336

> 📎 来源 / Source: http://securitytracker.com/id?1005764

#### 53. CVE-2002-2248 (N/A)

**CVE编号**: CVE-2002-2248
**严重程度**: N/A CVSS: 10.0
受影响产品: netscape:communicator

**漏洞描述**:
Buffer overflow in the sun.awt.windows.WDefaultFontCharset Java class implementation in Netscape 4.0 allows remote attackers to execute arbitrary code via an applet that calls the WDefaultFontCharset constructor with a long string and invokes the canConvert method.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103834439321292&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10706
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103834439321292&w=2

#### 54. CVE-2002-2281 (N/A)

**CVE编号**: CVE-2002-2281
**严重程度**: N/A CVSS: 10.0
受影响产品: symantec:java

**漏洞描述**:
Symantec Java! JIT (Just-In-Time) Compiler for Netscape Communicator 4.0 through 4.8 allows remote attackers to execute arbitrary Java commands via an applet that uses a jump call, which is not correctly compiled by the JIT compiler.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6222
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10711
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103798147613151&w=2

#### 55. CVE-2002-2284 (N/A)

**CVE编号**: CVE-2002-2284
**严重程度**: N/A CVSS: 6.4
受影响产品: netscape:communicator

**漏洞描述**:
Netscape Communicator 4.0 through 4.79 allows remote attackers to bypass JVM security and execute arbitrary Java code via an applet that loads user-supplied Java classes.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6223
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10714
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=103798147613151&w=2

#### 56. CVE-2002-2292 (N/A)

**CVE编号**: CVE-2002-2292
**严重程度**: N/A CVSS: 5.0
受影响产品: halycon_software:iasp

**漏洞描述**:
Directory traversal vulnerability in Remote Console Applet in Halycon Software iASP 1.0.9 allows remote attackers to read arbitrary files via a .. (dot dot) in the HTTP request to port 9095.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10860
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html

#### 57. CVE-2002-2373 (N/A)

**CVE编号**: CVE-2002-2373
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:tcp_ip_configuration_utility, apple:apple_laserwriter

**漏洞描述**:
The default configuration of the TCP/IP printer configuration utility in Apple LaserWriter 12/640 PS printer contains a blank Telnet password, which allows remote attackers to gain access.

**应对措施**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10476.php.

**参考链接**:
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250
- http://www.securityfocus.com/bid/6052
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250

> 📎 来源 / Source: http://www.iss.net/security_center/static/10476.php

#### 58. CVE-2003-0049 (N/A)

**CVE编号**: CVE-2003-0049
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
Apple File Protocol (AFP) in Mac OS X before 10.2.4 allows administrators to log in as other users by using the administrator password.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://securitytracker.com/id?1006107
- http://www.iss.net/security_center/static/11333.php
- http://www.securityfocus.com/bid/6860

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=61798

#### 59. CVE-2003-0050 (N/A)

**CVE编号**: CVE-2003-0050
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via shell metacharacters.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11401.php
- http://www.securityfocus.com/bid/6954
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 60. CVE-2003-0051 (N/A)

**CVE编号**: CVE-2003-0051
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to obtain the physical path of the server's installation path via a NULL file parameter.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11402.php
- http://www.securityfocus.com/bid/6956
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 61. CVE-2003-0052 (N/A)

**CVE编号**: CVE-2003-0052
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to list arbitrary directories.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11403.php
- http://www.securityfocus.com/bid/6955
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 62. CVE-2003-0053 (N/A)

**CVE编号**: CVE-2003-0053
**严重程度**: N/A CVSS: 4.3
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
Cross-site scripting (XSS) vulnerability in parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to insert arbitrary script via the filename parameter, which is inserted into an error message.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11404.php
- http://www.securityfocus.com/bid/6958
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 63. CVE-2003-0054 (N/A)

**CVE编号**: CVE-2003-0054
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute certain code via a request to port 7070 with the script in an argument to the rtsp DESCRIBE method, which is inserted into a log file and executed when the log is viewed using a browser.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11405.php
- http://www.securityfocus.com/bid/6960
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 64. CVE-2003-0055 (N/A)

**CVE编号**: CVE-2003-0055
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime_darwin_mp3_broadcaster

**漏洞描述**:
Buffer overflow in the MP3 broadcasting module of Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via a long filename.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11406.php
- http://www.securityfocus.com/bid/6957
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 65. CVE-2003-0168 (N/A)

**CVE编号**: CVE-2003-0168
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Buffer overflow in Apple QuickTime Player 5.x and 6.0 for Windows allows remote attackers to execute arbitrary code via a long QuickTime URL.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html
- http://lists.apple.com/mhonarc/security-announce/msg00027.html
- http://www.idefense.com/advisory/03.31.03.txt
- http://www.kb.cert.org/vuls/id/112553
- http://www.osvdb.org/10561

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html

#### 66. CVE-2003-0111 (N/A)

**CVE编号**: CVE-2003-0111
**严重程度**: N/A CVSS: 7.5
受影响产品: microsoft:virtual_machine, microsoft:windows_2000_terminal_services, microsoft:windows_2000

**漏洞描述**:
The ByteCode Verifier component of Microsoft Virtual Machine (VM) build 5.0.3809 and earlier, as used in Windows and Internet Explorer, allows remote attackers to bypass security checks and execute arbitrary code via a malicious Java applet, aka "Flaw in Microsoft VM Could Enable System Compromise."

**应对措施**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/11751.php.

**参考链接**:
- http://www.iss.net/security_center/static/11751.php
- http://www.kb.cert.org/vuls/id/447569
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-011
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A136
- http://www.iss.net/security_center/static/11751.php

> 📎 来源 / Source: http://www.iss.net/security_center/static/11751.php

#### 67. CVE-2003-0420 (N/A)

**CVE编号**: CVE-2003-0420
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:mac_os_x_server

**漏洞描述**:
Information leak in dsimportexport for Apple Macintosh OS X Server 10.2.6 allows local users to obtain the username and password of the account running the tool.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/9025/.

**参考链接**:
- http://secunia.com/advisories/9025/
- http://www.auscert.org.au/render.html?it=3165
- http://www.kb.cert.org/vuls/id/JPLA-5NTL8E
- http://www.securityfocus.com/bid/7894
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12342

> 📎 来源 / Source: http://secunia.com/advisories/9025/

#### 68. CVE-2003-0270 (N/A)

**CVE编号**: CVE-2003-0270
**严重程度**: N/A CVSS: 7.6
受影响产品: apple:802.11n

**漏洞描述**:
The administration capability for Apple AirPort 802.11 wireless access point devices uses weak encryption (XOR with a fixed key) for protecting authentication credentials, which could allow remote attackers to obtain administrative access via sniffing when the capability is available via Ethernet or non-WEP connections.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8773.

**参考链接**:
- http://secunia.com/advisories/8773
- http://securitytracker.com/id?1006742
- http://www.atstake.com/research/advisories/2003/a051203-1.txt
- http://www.securityfocus.com/bid/7554
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11980

> 📎 来源 / Source: http://secunia.com/advisories/8773

#### 69. CVE-2003-0379 (N/A)

**CVE编号**: CVE-2003-0379
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:afp_server

**漏洞描述**:
Unknown vulnerability in Apple File Service (AFP Server) for Mac OS X Server, when sharing files on a UFS or re-shared NFS volume, allows remote attackers to overwrite arbitrary files.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00030.html.

**参考链接**:
- http://lists.apple.com/mhonarc/security-announce/msg00030.html
- http://lists.apple.com/mhonarc/security-announce/msg00030.html

> 📎 来源 / Source: http://lists.apple.com/mhonarc/security-announce/msg00030.html

#### 70. CVE-2003-0421 (N/A)

**CVE编号**: CVE-2003-0421
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 71. CVE-2003-0422 (N/A)

**CVE编号**: CVE-2003-0422
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via a request to view_broadcast.cgi that does not contain the required parameters.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 72. CVE-2003-0423 (N/A)

**CVE编号**: CVE-2003-0423
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
parse_xml.cgi in Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to obtain the source code for parseable files via the filename parameter.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 73. CVE-2003-0424 (N/A)

**CVE编号**: CVE-2003-0424
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to obtain the source code for scripts by appending encoded space (%20) or . (%2e) characters to an HTTP request for the script, e.g. view_broadcast.cgi.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 74. CVE-2003-0425 (N/A)

**CVE编号**: CVE-2003-0425
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Directory traversal vulnerability in Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to read arbitrary files via a ... (triple dot) in an HTTP request.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 75. CVE-2003-0426 (N/A)

**CVE编号**: CVE-2003-0426
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
The installation of Apple QuickTime / Darwin Streaming Server before 4.1.3f starts the administration server with a "Setup Assistant" page that allows remote attackers to set the administrator password and gain privileges before the real administrator.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 76. CVE-2003-0502 (N/A)

**CVE编号**: CVE-2003-0502
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 77. CVE-2003-0975 (N/A)

**CVE编号**: CVE-2003-0975
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x, apple:safari, apple:mac_os_x_server

**漏洞描述**:
Apple Safari 1.0 through 1.1 on Mac OS X 10.3.1 and Mac OS X 10.2.8 allows remote attackers to steal user cookies from another domain via a link with a hex-encoded null character (%00) followed by the target domain.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00042.html
- http://marc.info/?l=bugtraq&m=106917674428552&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7973
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=61798

#### 78. CVE-2003-0885 (N/A)

**CVE编号**: CVE-2003-0885
**严重程度**: N/A CVSS: 6.4
受影响产品: xscreensaver:xscreensaver

**漏洞描述**:
Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.

**应对措施**:
Apply patch from vendor. Monitor http://bugs.gentoo.org/show_bug.cgi?id=41253.

**参考链接**:
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286

> 📎 来源 / Source: http://bugs.gentoo.org/show_bug.cgi?id=41253

#### 79. CVE-2003-1091 (N/A)

**CVE编号**: CVE-2003-1091
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime_broadcaster

**漏洞描述**:
Integer overflow in MP3Broadcaster for Apple QuickTime/Darwin Streaming Server 4.1.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via malformed ID3 tags in MP3 files.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html.

**参考链接**:
- http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html
- http://securitytracker.com/id?1006822
- http://www.kb.cert.org/vuls/id/148564
- http://www.securityfocus.com/bid/7660
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12054

> 📎 来源 / Source: http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html

#### 80. CVE-2003-1123 (N/A)

**CVE编号**: CVE-2003-1123
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:jre, sun:jdk

**漏洞描述**:
Sun Java Runtime Environment (JRE) and SDK 1.4.0_01 and earlier allows untrusted applets to access certain information within trusted applets, which allows attackers to bypass the restrictions of the Java security model.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8958.

**参考链接**:
- http://secunia.com/advisories/8958
- http://securitytracker.com/id?1006935
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-55100-1
- http://www.kb.cert.org/vuls/id/393292
- http://www.securityfocus.com/bid/7824

> 📎 来源 / Source: http://secunia.com/advisories/8958

#### 81. CVE-2003-1413 (N/A)

**CVE编号**: CVE-2003-1413
**严重程度**: N/A CVSS: 4.3
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
parse_xml.cgi in Apple Darwin Streaming Server 4.1.1 allows remote attackers to determine the existence of arbitrary files by using ".." sequences in the filename parameter and comparing the resulting error messages.

**应对措施**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**参考链接**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6992
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11445
- http://securityreason.com/securityalert/3260

> 📎 来源 / Source: http://securityreason.com/securityalert/3260

#### 82. CVE-2003-1414 (N/A)

**CVE编号**: CVE-2003-1414
**严重程度**: N/A CVSS: 4.3
受影响产品: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述**:
Directory traversal vulnerability in parse_xml.cg Apple Darwin Streaming Server 4.1.2 and Apple Quicktime Streaming Server 4.1.1 allows remote attackers to read arbitrary files via a ... (triple dot) in the filename parameter.

**应对措施**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**参考链接**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6990
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11446
- http://securityreason.com/securityalert/3260

> 📎 来源 / Source: http://securityreason.com/securityalert/3260

#### 83. CVE-2003-1516 (N/A)

**CVE编号**: CVE-2003-1516
**严重程度**: N/A CVSS: 6.8
受影响产品: sun:java_plug-in

**漏洞描述**:
The org.apache.xalan.processor.XSLProcessorVersion class in Java Plug-in 1.4.2_01 allows signed and unsigned applets to share variables, which violates the Java security model and could allow remote attackers to read or write data belonging to a signed applet.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/341815.

**参考链接**:
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857

> 📎 来源 / Source: http://www.securityfocus.com/archive/1/341815

#### 84. CVE-2003-0601 (N/A)

**CVE编号**: CVE-2003-0601
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server

**漏洞描述**:
Workgroup Manager in Apple Mac OS X Server 10.2 through 10.2.6 does not disable a password for a new account before it is saved for the first time, which allows remote attackers to gain unauthorized access via the new account before it is saved.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25631.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12728
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=25631

#### 85. CVE-2003-1006 (N/A)

**CVE编号**: CVE-2003-1006
**严重程度**: N/A CVSS: 7.2
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
Buffer overflow in cd9660.util in Apple Mac OS X 10.0 through 10.3.2 and Apple Mac OS X Server 10.0 through 10.3.2 may allow local users to execute arbitrary code via a long command line parameter.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.kb.cert.org/vuls/id/878526
- http://www.securityfocus.com/archive/1/347578
- http://www.securityfocus.com/archive/1/347707
- http://www.securityfocus.com/archive/1/348097

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=61798

#### 86. CVE-2003-1007 (N/A)

**CVE编号**: CVE-2003-1007
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
AppleFileServer (AFS) in Apple Mac OS X 10.2.8 and 10.3.2 does not properly handle certain malformed requests, with unknown impact.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://securitytracker.com/id?1008532
- http://www.securityfocus.com/bid/9264
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14051
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=61798

#### 87. CVE-2003-1009 (N/A)

**CVE编号**: CVE-2003-1009
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
Directory Services in Apple Mac OS X 10.0.2, 10.0.3, 10.2.8, 10.3.2 and Apple Mac OS X Server 10.2 through 10.3.2 accepts authentication server information from unknown LDAP or NetInfo sources as provided by a malicious DHCP server, which allows remote attackers to gain privileges.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=32478.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=32478
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.carrel.org/dhcp-vuln.html
- http://www.securityfocus.com/bid/9110
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13874

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=32478

#### 88. CVE-2003-1011 (N/A)

**CVE编号**: CVE-2003-1011
**严重程度**: N/A CVSS: 7.2
受影响产品: apple:mac_os_x

**漏洞描述**:
Apple Mac OS X 10.0 through 10.2.8 allows local users with a USB keyboard to gain unauthorized access by holding down the CTRL and C keys when the system is booting, which crashes the init process and leaves the user in a root shell.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.securityfocus.com/archive/1/343087
- http://www.securityfocus.com/bid/8945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13573
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=61798

#### 89. CVE-2003-0514 (N/A)

**CVE编号**: CVE-2003-0514
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:safari

**漏洞描述**:
Apple Safari allows remote attackers to bypass intended cookie access restrictions on a web application via "%2e%2e" (encoded dot dot) directory traversal sequences in a URL, which causes Safari to send the cookie outside the specified URL subsets, e.g. to a vulnerable application that runs on the same server as the target application.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html

#### 90. CVE-2004-0430 (N/A)

**CVE编号**: CVE-2004-0430
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
Stack-based buffer overflow in AppleFileServer for Mac OS X 10.3.3 and earlier allows remote attackers to execute arbitrary code via a LoginExt packet for a Cleartext Password User Authentication Method (UAM) request with a PathName argument that includes an AFPName type string that is longer than the associated length field.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00049.html.

**参考链接**:
- http://lists.apple.com/mhonarc/security-announce/msg00049.html
- http://secunia.com/advisories/11539
- http://securitytracker.com/id?1010039
- http://www.atstake.com/research/advisories/2004/a050304-1.txt
- http://www.kb.cert.org/vuls/id/648406

> 📎 来源 / Source: http://lists.apple.com/mhonarc/security-announce/msg00049.html

#### 91. CVE-2004-0431 (N/A)

**CVE编号**: CVE-2004-0431
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple QuickTime (QuickTime.qts) before 6.5.1 allows attackers to execute arbitrary code via a large "number of entries" field in the sample-to-chunk table data for a .mov movie file, which leads to a heap-based buffer overflow.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00048.html.

**参考链接**:
- http://lists.apple.com/mhonarc/security-announce/msg00048.html
- http://marc.info/?l=bugtraq&m=108360110618389&w=2
- http://marc.info/?l=ntbugtraq&m=108356485013237&w=2
- http://www.kb.cert.org/vuls/id/782958
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16026

> 📎 来源 / Source: http://lists.apple.com/mhonarc/security-announce/msg00048.html

#### 92. CVE-2004-0723 (N/A)

**CVE编号**: CVE-2004-0723
**严重程度**: N/A CVSS: 6.4
受影响产品: microsoft:java_virtual_machine

**漏洞描述**:
Microsoft Java virtual machine (VM) 5.0.0.3810 allows remote attackers to bypass sandbox restrictions to read or write certain data between applets from different domains via the "GET/Key" and "PUT/Key/Value" commands, aka "cross-site Java."

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=108948405808522&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16666
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=108948405808522&w=2

#### 93. CVE-2004-0518 (N/A)

**CVE编号**: CVE-2004-0518
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述**:
Unknown vulnerability in AppleFileServer for Mac OS X 10.3.4, related to "the use of SSH and reporting errors," has unknown impact and attack vectors.

**应对措施**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16288
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333

> 📎 来源 / Source: http://lists.seifried.org/pipermail/security/2004-May/003743.html

#### 94. CVE-2004-0823 (N/A)

**CVE编号**: CVE-2004-0823
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x, openldap:openldap, apple:mac_os_x_server

**漏洞描述**:
OpenLDAP 1.0 through 2.1.19, as used in Apple Mac OS 10.3.4 and 10.3.5 and possibly other operating systems, may allow certain authentication schemes to use hashed (crypt) passwords in the userPassword attribute as if they were plaintext passwords, which allows remote attackers to re-use hashed passwords without decrypting them.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

**参考链接**:
- http://secunia.com/advisories/12491/
- http://secunia.com/advisories/17233
- http://secunia.com/advisories/21520
- http://support.avaya.com/elmodocs2/security/ASA-2006-157.htm
- http://www.auscert.org.au/render.html?it=4363

> 📎 来源 / Source: http://secunia.com/advisories/12491/

#### 95. CVE-2004-0831 (N/A)

**CVE编号**: CVE-2004-0831
**严重程度**: N/A CVSS: 7.2
受影响产品: mcafee:virusscan

**漏洞描述**:
McAfee VirusScan 4.5.1 does not drop SYSTEM privileges before allowing users to browse for files via the "System Scan" properties of the System Tray applet, which could allow local users to gain privileges.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=109526269429728&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17367
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=109526269429728&w=2

#### 96. CVE-2004-1121 (N/A)

**CVE编号**: CVE-2004-1121
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 1.0 through 1.2.3 allows remote attackers to spoof the URL displayed in the status bar via TABLE tags.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13047/
- http://www.kb.cert.org/vuls/id/925430
- http://www.securityfocus.com/bid/11573
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17909

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 97. CVE-2004-1081 (N/A)

**CVE编号**: CVE-2004-1081
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述**:
The Application Framework (AppKit) for Apple Mac OS X 10.2.8 and 10.3.6 does not properly restrict access to a secure text input field, which allows local users to read keyboard input from other applications within the same window session.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18350

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 98. CVE-2004-1084 (N/A)

**CVE编号**: CVE-2004-1084
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+, which bypass Apache file handles.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 99. CVE-2004-1085 (N/A)

**CVE编号**: CVE-2004-1085
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述**:
Human Interface Toolbox (HIToolBox) for Apple Mac 0S X 10.3.6 allows local users to exit applications via the force-quit key combination, even when the system is running in kiosk mode.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18352

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 100. CVE-2004-1086 (N/A)

**CVE编号**: CVE-2004-1086
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述**:
Buffer overflow in PSNormalizer for Apple Mac OS X 10.3.6 allows remote attackers to execute arbitrary code via a crafted PostScript input file.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18354

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html


---

## English 🇺🇸
**macOS System Vulnerabilities**

Auto-updated hourly: latest MACOS system vulnerabilities and mitigations.

### MACOS Vulnerability List

#### 1. CVE-1999-0142 (N/A)

**CVE ID**: CVE-1999-0142
**Severity**: N/A CVSS: 7.5
**Affected Products**: netscape:navigator, sun:java

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
**Affected Products**: apple:macos, apache:http_server

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
**Affected Products**: microsoft:internet_explorer, microsoft:visual_studio, microsoft:ie

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
**Affected Products**: sun:jre, sun:sdk, apple:mac_os_runtime_for_java, sun:jdk

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
**Affected Products**: sun:jre, microsoft:virtual_machine, sun:sdk, sun:jdk

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
**Affected Products**: sun:jre, hp:java_jre-jdk, sun:sdk, microsoft:virtual_machine, sun:jdk

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
**Affected Products**: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
**Affected Products**: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
**Affected Products**: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
**Affected Products**: microsoft:windows_98se, microsoft:windows_me, microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_98

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
**Affected Products**: apple:terminal, apple:mac_os_x

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

#### 51. CVE-2002-2184 (N/A)

**CVE ID**: CVE-2002-2184
**Severity**: N/A CVSS: 5.0
**Affected Products**: digi-net_technologies:digichat

**Description**:
Digi-Net Technologies DigiChat 3.5 allows chat users to obtain the IP addresses of other chat users via a "Showip" parameter in the chat applet.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5019.

**References**:
- http://www.securityfocus.com/bid/5019
- http://www.securityfocus.com/bid/5019

> 📎 Source: http://www.securityfocus.com/bid/5019

#### 52. CVE-2002-2242 (N/A)

**CVE ID**: CVE-2002-2242
**Severity**: N/A CVSS: 6.4
**Affected Products**: kismac:kismac

**Description**:
The Apple Package Manager in KisMAC 0.02a and earlier modifies file permissions of sensitive files after installation, which could allow attackers to conduct unauthorized activities on those files.

**Mitigation**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1005764.

**References**:
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10813
- http://securitytracker.com/id?1005764
- http://www.securityfocus.com/bid/6336

> 📎 Source: http://securitytracker.com/id?1005764

#### 53. CVE-2002-2248 (N/A)

**CVE ID**: CVE-2002-2248
**Severity**: N/A CVSS: 10.0
**Affected Products**: netscape:communicator

**Description**:
Buffer overflow in the sun.awt.windows.WDefaultFontCharset Java class implementation in Netscape 4.0 allows remote attackers to execute arbitrary code via an applet that calls the WDefaultFontCharset constructor with a long string and invokes the canConvert method.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103834439321292&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10706
- http://marc.info/?l=bugtraq&m=103834439321292&w=2
- http://www.securityfocus.com/bid/6256

> 📎 Source: http://marc.info/?l=bugtraq&m=103834439321292&w=2

#### 54. CVE-2002-2281 (N/A)

**CVE ID**: CVE-2002-2281
**Severity**: N/A CVSS: 10.0
**Affected Products**: symantec:java

**Description**:
Symantec Java! JIT (Just-In-Time) Compiler for Netscape Communicator 4.0 through 4.8 allows remote attackers to execute arbitrary Java commands via an applet that uses a jump call, which is not correctly compiled by the JIT compiler.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6222
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10711
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=103798147613151&w=2

#### 55. CVE-2002-2284 (N/A)

**CVE ID**: CVE-2002-2284
**Severity**: N/A CVSS: 6.4
**Affected Products**: netscape:communicator

**Description**:
Netscape Communicator 4.0 through 4.79 allows remote attackers to bypass JVM security and execute arbitrary Java code via an applet that loads user-supplied Java classes.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=103798147613151&w=2
- http://www.lsd-pl.net/documents/javasecurity-1.0.0.pdf
- http://www.securityfocus.com/bid/6223
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10714
- http://marc.info/?l=bugtraq&m=103798147613151&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=103798147613151&w=2

#### 56. CVE-2002-2292 (N/A)

**CVE ID**: CVE-2002-2292
**Severity**: N/A CVSS: 5.0
**Affected Products**: halycon_software:iasp

**Description**:
Directory traversal vulnerability in Remote Console Applet in Halycon Software iASP 1.0.9 allows remote attackers to read arbitrary files via a .. (dot dot) in the HTTP request to port 9095.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10860
- http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html
- http://www.securityfocus.com/bid/6394

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html

#### 57. CVE-2002-2373 (N/A)

**CVE ID**: CVE-2002-2373
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:tcp_ip_configuration_utility, apple:apple_laserwriter

**Description**:
The default configuration of the TCP/IP printer configuration utility in Apple LaserWriter 12/640 PS printer contains a blank Telnet password, which allows remote attackers to gain access.

**Mitigation**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10476.php.

**References**:
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250
- http://www.securityfocus.com/bid/6052
- http://www.iss.net/security_center/static/10476.php
- http://www.securityfocus.com/archive/1/297250

> 📎 Source: http://www.iss.net/security_center/static/10476.php

#### 58. CVE-2003-0049 (N/A)

**CVE ID**: CVE-2003-0049
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
Apple File Protocol (AFP) in Mac OS X before 10.2.4 allows administrators to log in as other users by using the administrator password.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://securitytracker.com/id?1006107
- http://www.iss.net/security_center/static/11333.php
- http://www.securityfocus.com/bid/6860

> 📎 Source: http://docs.info.apple.com/article.html?artnum=61798

#### 59. CVE-2003-0050 (N/A)

**CVE ID**: CVE-2003-0050
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via shell metacharacters.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11401.php
- http://www.securityfocus.com/bid/6954
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 60. CVE-2003-0051 (N/A)

**CVE ID**: CVE-2003-0051
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to obtain the physical path of the server's installation path via a NULL file parameter.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11402.php
- http://www.securityfocus.com/bid/6956
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 61. CVE-2003-0052 (N/A)

**CVE ID**: CVE-2003-0052
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to list arbitrary directories.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11403.php
- http://www.securityfocus.com/bid/6955
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 62. CVE-2003-0053 (N/A)

**CVE ID**: CVE-2003-0053
**Severity**: N/A CVSS: 4.3
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
Cross-site scripting (XSS) vulnerability in parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to insert arbitrary script via the filename parameter, which is inserted into an error message.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11404.php
- http://www.securityfocus.com/bid/6958
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 63. CVE-2003-0054 (N/A)

**CVE ID**: CVE-2003-0054
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute certain code via a request to port 7070 with the script in an argument to the rtsp DESCRIBE method, which is inserted into a log file and executed when the log is viewed using a browser.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11405.php
- http://www.securityfocus.com/bid/6960
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 64. CVE-2003-0055 (N/A)

**CVE ID**: CVE-2003-0055
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime_darwin_mp3_broadcaster

**Description**:
Buffer overflow in the MP3 broadcasting module of Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via a long filename.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**References**:
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt
- http://marc.info/?l=bugtraq&m=104618904330226&w=2
- http://www.iss.net/security_center/static/11406.php
- http://www.securityfocus.com/bid/6957
- http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

> 📎 Source: http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt

#### 65. CVE-2003-0168 (N/A)

**CVE ID**: CVE-2003-0168
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Buffer overflow in Apple QuickTime Player 5.x and 6.0 for Windows allows remote attackers to execute arbitrary code via a long QuickTime URL.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html
- http://lists.apple.com/mhonarc/security-announce/msg00027.html
- http://www.idefense.com/advisory/03.31.03.txt
- http://www.kb.cert.org/vuls/id/112553
- http://www.osvdb.org/10561

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html

#### 66. CVE-2003-0111 (N/A)

**CVE ID**: CVE-2003-0111
**Severity**: N/A CVSS: 7.5
**Affected Products**: microsoft:virtual_machine, microsoft:windows_2000_terminal_services, microsoft:windows_2000

**Description**:
The ByteCode Verifier component of Microsoft Virtual Machine (VM) build 5.0.3809 and earlier, as used in Windows and Internet Explorer, allows remote attackers to bypass security checks and execute arbitrary code via a malicious Java applet, aka "Flaw in Microsoft VM Could Enable System Compromise."

**Mitigation**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/11751.php.

**References**:
- http://www.iss.net/security_center/static/11751.php
- http://www.kb.cert.org/vuls/id/447569
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-011
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A136
- http://www.iss.net/security_center/static/11751.php

> 📎 Source: http://www.iss.net/security_center/static/11751.php

#### 67. CVE-2003-0420 (N/A)

**CVE ID**: CVE-2003-0420
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:mac_os_x_server

**Description**:
Information leak in dsimportexport for Apple Macintosh OS X Server 10.2.6 allows local users to obtain the username and password of the account running the tool.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/9025/.

**References**:
- http://secunia.com/advisories/9025/
- http://www.auscert.org.au/render.html?it=3165
- http://www.kb.cert.org/vuls/id/JPLA-5NTL8E
- http://www.securityfocus.com/bid/7894
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12342

> 📎 Source: http://secunia.com/advisories/9025/

#### 68. CVE-2003-0270 (N/A)

**CVE ID**: CVE-2003-0270
**Severity**: N/A CVSS: 7.6
**Affected Products**: apple:802.11n

**Description**:
The administration capability for Apple AirPort 802.11 wireless access point devices uses weak encryption (XOR with a fixed key) for protecting authentication credentials, which could allow remote attackers to obtain administrative access via sniffing when the capability is available via Ethernet or non-WEP connections.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8773.

**References**:
- http://secunia.com/advisories/8773
- http://securitytracker.com/id?1006742
- http://www.atstake.com/research/advisories/2003/a051203-1.txt
- http://www.securityfocus.com/bid/7554
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11980

> 📎 Source: http://secunia.com/advisories/8773

#### 69. CVE-2003-0379 (N/A)

**CVE ID**: CVE-2003-0379
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:afp_server

**Description**:
Unknown vulnerability in Apple File Service (AFP Server) for Mac OS X Server, when sharing files on a UFS or re-shared NFS volume, allows remote attackers to overwrite arbitrary files.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00030.html.

**References**:
- http://lists.apple.com/mhonarc/security-announce/msg00030.html
- http://lists.apple.com/mhonarc/security-announce/msg00030.html

> 📎 Source: http://lists.apple.com/mhonarc/security-announce/msg00030.html

#### 70. CVE-2003-0421 (N/A)

**CVE ID**: CVE-2003-0421
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 71. CVE-2003-0422 (N/A)

**CVE ID**: CVE-2003-0422
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via a request to view_broadcast.cgi that does not contain the required parameters.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 72. CVE-2003-0423 (N/A)

**CVE ID**: CVE-2003-0423
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
parse_xml.cgi in Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to obtain the source code for parseable files via the filename parameter.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 73. CVE-2003-0424 (N/A)

**CVE ID**: CVE-2003-0424
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to obtain the source code for scripts by appending encoded space (%20) or . (%2e) characters to an HTTP request for the script, e.g. view_broadcast.cgi.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 74. CVE-2003-0425 (N/A)

**CVE ID**: CVE-2003-0425
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Directory traversal vulnerability in Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to read arbitrary files via a ... (triple dot) in an HTTP request.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 75. CVE-2003-0426 (N/A)

**CVE ID**: CVE-2003-0426
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
The installation of Apple QuickTime / Darwin Streaming Server before 4.1.3f starts the administration server with a "Setup Assistant" page that allows remote attackers to set the administrator password and gain privileges before the real administrator.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 76. CVE-2003-0502 (N/A)

**CVE ID**: CVE-2003-0502
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html
- http://www.rapid7.com/advisories/R7-0015.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html

#### 77. CVE-2003-0975 (N/A)

**CVE ID**: CVE-2003-0975
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x, apple:safari, apple:mac_os_x_server

**Description**:
Apple Safari 1.0 through 1.1 on Mac OS X 10.3.1 and Mac OS X 10.2.8 allows remote attackers to steal user cookies from another domain via a link with a hex-encoded null character (%00) followed by the target domain.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00042.html
- http://marc.info/?l=bugtraq&m=106917674428552&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7973
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 Source: http://docs.info.apple.com/article.html?artnum=61798

#### 78. CVE-2003-0885 (N/A)

**CVE ID**: CVE-2003-0885
**Severity**: N/A CVSS: 6.4
**Affected Products**: xscreensaver:xscreensaver

**Description**:
Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.

**Mitigation**:
Apply patch from vendor. Monitor http://bugs.gentoo.org/show_bug.cgi?id=41253.

**References**:
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286
- http://bugs.gentoo.org/show_bug.cgi?id=41253
- http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=182286

> 📎 Source: http://bugs.gentoo.org/show_bug.cgi?id=41253

#### 79. CVE-2003-1091 (N/A)

**CVE ID**: CVE-2003-1091
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime_broadcaster

**Description**:
Integer overflow in MP3Broadcaster for Apple QuickTime/Darwin Streaming Server 4.1.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via malformed ID3 tags in MP3 files.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html.

**References**:
- http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html
- http://securitytracker.com/id?1006822
- http://www.kb.cert.org/vuls/id/148564
- http://www.securityfocus.com/bid/7660
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12054

> 📎 Source: http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html

#### 80. CVE-2003-1123 (N/A)

**CVE ID**: CVE-2003-1123
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:jre, sun:jdk

**Description**:
Sun Java Runtime Environment (JRE) and SDK 1.4.0_01 and earlier allows untrusted applets to access certain information within trusted applets, which allows attackers to bypass the restrictions of the Java security model.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8958.

**References**:
- http://secunia.com/advisories/8958
- http://securitytracker.com/id?1006935
- http://sunsolve.sun.com/search/document.do?assetkey=1-26-55100-1
- http://www.kb.cert.org/vuls/id/393292
- http://www.securityfocus.com/bid/7824

> 📎 Source: http://secunia.com/advisories/8958

#### 81. CVE-2003-1413 (N/A)

**CVE ID**: CVE-2003-1413
**Severity**: N/A CVSS: 4.3
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
parse_xml.cgi in Apple Darwin Streaming Server 4.1.1 allows remote attackers to determine the existence of arbitrary files by using ".." sequences in the filename parameter and comparing the resulting error messages.

**Mitigation**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**References**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6992
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11445
- http://securityreason.com/securityalert/3260

> 📎 Source: http://securityreason.com/securityalert/3260

#### 82. CVE-2003-1414 (N/A)

**CVE ID**: CVE-2003-1414
**Severity**: N/A CVSS: 4.3
**Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**Description**:
Directory traversal vulnerability in parse_xml.cg Apple Darwin Streaming Server 4.1.2 and Apple Quicktime Streaming Server 4.1.1 allows remote attackers to read arbitrary files via a ... (triple dot) in the filename parameter.

**Mitigation**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**References**:
- http://securityreason.com/securityalert/3260
- http://www.securityfocus.com/archive/1/313517
- http://www.securityfocus.com/bid/6990
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11446
- http://securityreason.com/securityalert/3260

> 📎 Source: http://securityreason.com/securityalert/3260

#### 83. CVE-2003-1516 (N/A)

**CVE ID**: CVE-2003-1516
**Severity**: N/A CVSS: 6.8
**Affected Products**: sun:java_plug-in

**Description**:
The org.apache.xalan.processor.XSLProcessorVersion class in Java Plug-in 1.4.2_01 allows signed and unsigned applets to share variables, which violates the Java security model and could allow remote attackers to read or write data belonging to a signed applet.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/341815.

**References**:
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857
- http://www.securityfocus.com/archive/1/341815
- http://www.securityfocus.com/bid/8857

> 📎 Source: http://www.securityfocus.com/archive/1/341815

#### 84. CVE-2003-0601 (N/A)

**CVE ID**: CVE-2003-0601
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server

**Description**:
Workgroup Manager in Apple Mac OS X Server 10.2 through 10.2.6 does not disable a password for a new account before it is saved for the first time, which allows remote attackers to gain unauthorized access via the new account before it is saved.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25631.

**References**:
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266
- https://exchange.xforce.ibmcloud.com/vulnerabilities/12728
- http://docs.info.apple.com/article.html?artnum=25631
- http://www.securityfocus.com/bid/8266

> 📎 Source: http://docs.info.apple.com/article.html?artnum=25631

#### 85. CVE-2003-1006 (N/A)

**CVE ID**: CVE-2003-1006
**Severity**: N/A CVSS: 7.2
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
Buffer overflow in cd9660.util in Apple Mac OS X 10.0 through 10.3.2 and Apple Mac OS X Server 10.0 through 10.3.2 may allow local users to execute arbitrary code via a long command line parameter.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.kb.cert.org/vuls/id/878526
- http://www.securityfocus.com/archive/1/347578
- http://www.securityfocus.com/archive/1/347707
- http://www.securityfocus.com/archive/1/348097

> 📎 Source: http://docs.info.apple.com/article.html?artnum=61798

#### 86. CVE-2003-1007 (N/A)

**CVE ID**: CVE-2003-1007
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
AppleFileServer (AFS) in Apple Mac OS X 10.2.8 and 10.3.2 does not properly handle certain malformed requests, with unknown impact.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://securitytracker.com/id?1008532
- http://www.securityfocus.com/bid/9264
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14051
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 Source: http://docs.info.apple.com/article.html?artnum=61798

#### 87. CVE-2003-1009 (N/A)

**CVE ID**: CVE-2003-1009
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
Directory Services in Apple Mac OS X 10.0.2, 10.0.3, 10.2.8, 10.3.2 and Apple Mac OS X Server 10.2 through 10.3.2 accepts authentication server information from unknown LDAP or NetInfo sources as provided by a malicious DHCP server, which allows remote attackers to gain privileges.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=32478.

**References**:
- http://docs.info.apple.com/article.html?artnum=32478
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.carrel.org/dhcp-vuln.html
- http://www.securityfocus.com/bid/9110
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13874

> 📎 Source: http://docs.info.apple.com/article.html?artnum=32478

#### 88. CVE-2003-1011 (N/A)

**CVE ID**: CVE-2003-1011
**Severity**: N/A CVSS: 7.2
**Affected Products**: apple:mac_os_x

**Description**:
Apple Mac OS X 10.0 through 10.2.8 allows local users with a USB keyboard to gain unauthorized access by holding down the CTRL and C keys when the system is booting, which crashes the init process and leaves the user in a root shell.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.securityfocus.com/archive/1/343087
- http://www.securityfocus.com/bid/8945
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13573
- http://docs.info.apple.com/article.html?artnum=61798

> 📎 Source: http://docs.info.apple.com/article.html?artnum=61798

#### 89. CVE-2003-0514 (N/A)

**CVE ID**: CVE-2003-0514
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:safari

**Description**:
Apple Safari allows remote attackers to bypass intended cookie access restrictions on a web application via "%2e%2e" (encoded dot dot) directory traversal sequences in a URL, which causes Safari to send the cookie outside the specified URL subsets, e.g. to a vulnerable application that runs on the same server as the target application.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-March/018475.html

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html

#### 90. CVE-2004-0430 (N/A)

**CVE ID**: CVE-2004-0430
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
Stack-based buffer overflow in AppleFileServer for Mac OS X 10.3.3 and earlier allows remote attackers to execute arbitrary code via a LoginExt packet for a Cleartext Password User Authentication Method (UAM) request with a PathName argument that includes an AFPName type string that is longer than the associated length field.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00049.html.

**References**:
- http://lists.apple.com/mhonarc/security-announce/msg00049.html
- http://secunia.com/advisories/11539
- http://securitytracker.com/id?1010039
- http://www.atstake.com/research/advisories/2004/a050304-1.txt
- http://www.kb.cert.org/vuls/id/648406

> 📎 Source: http://lists.apple.com/mhonarc/security-announce/msg00049.html

#### 91. CVE-2004-0431 (N/A)

**CVE ID**: CVE-2004-0431
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple QuickTime (QuickTime.qts) before 6.5.1 allows attackers to execute arbitrary code via a large "number of entries" field in the sample-to-chunk table data for a .mov movie file, which leads to a heap-based buffer overflow.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00048.html.

**References**:
- http://lists.apple.com/mhonarc/security-announce/msg00048.html
- http://marc.info/?l=bugtraq&m=108360110618389&w=2
- http://marc.info/?l=ntbugtraq&m=108356485013237&w=2
- http://www.kb.cert.org/vuls/id/782958
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16026

> 📎 Source: http://lists.apple.com/mhonarc/security-announce/msg00048.html

#### 92. CVE-2004-0723 (N/A)

**CVE ID**: CVE-2004-0723
**Severity**: N/A CVSS: 6.4
**Affected Products**: microsoft:java_virtual_machine

**Description**:
Microsoft Java virtual machine (VM) 5.0.0.3810 allows remote attackers to bypass sandbox restrictions to read or write certain data between applets from different domains via the "GET/Key" and "PUT/Key/Value" commands, aka "cross-site Java."

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=108948405808522&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16666
- http://marc.info/?l=bugtraq&m=108948405808522&w=2
- http://www.securityfocus.com/bid/10688

> 📎 Source: http://marc.info/?l=bugtraq&m=108948405808522&w=2

#### 93. CVE-2004-0518 (N/A)

**CVE ID**: CVE-2004-0518
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**Description**:
Unknown vulnerability in AppleFileServer for Mac OS X 10.3.4, related to "the use of SSH and reporting errors," has unknown impact and attack vectors.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16288
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010333

> 📎 Source: http://lists.seifried.org/pipermail/security/2004-May/003743.html

#### 94. CVE-2004-0823 (N/A)

**CVE ID**: CVE-2004-0823
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x, openldap:openldap, apple:mac_os_x_server

**Description**:
OpenLDAP 1.0 through 2.1.19, as used in Apple Mac OS 10.3.4 and 10.3.5 and possibly other operating systems, may allow certain authentication schemes to use hashed (crypt) passwords in the userPassword attribute as if they were plaintext passwords, which allows remote attackers to re-use hashed passwords without decrypting them.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

**References**:
- http://secunia.com/advisories/12491/
- http://secunia.com/advisories/17233
- http://secunia.com/advisories/21520
- http://support.avaya.com/elmodocs2/security/ASA-2006-157.htm
- http://www.auscert.org.au/render.html?it=4363

> 📎 Source: http://secunia.com/advisories/12491/

#### 95. CVE-2004-0831 (N/A)

**CVE ID**: CVE-2004-0831
**Severity**: N/A CVSS: 7.2
**Affected Products**: mcafee:virusscan

**Description**:
McAfee VirusScan 4.5.1 does not drop SYSTEM privileges before allowing users to browse for files via the "System Scan" properties of the System Tray applet, which could allow local users to gain privileges.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=109526269429728&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17367
- http://marc.info/?l=bugtraq&m=109526269429728&w=2
- http://www.idefense.com/application/poi/display?id=140&type=vulnerabilities

> 📎 Source: http://marc.info/?l=bugtraq&m=109526269429728&w=2

#### 96. CVE-2004-1121 (N/A)

**CVE ID**: CVE-2004-1121
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
Apple Safari 1.0 through 1.2.3 allows remote attackers to spoof the URL displayed in the status bar via TABLE tags.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13047/
- http://www.kb.cert.org/vuls/id/925430
- http://www.securityfocus.com/bid/11573
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17909

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 97. CVE-2004-1081 (N/A)

**CVE ID**: CVE-2004-1081
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**Description**:
The Application Framework (AppKit) for Apple Mac OS X 10.2.8 and 10.3.6 does not properly restrict access to a secure text input field, which allows local users to read keyboard input from other applications within the same window session.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18350

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 98. CVE-2004-1084 (N/A)

**CVE ID**: CVE-2004-1084
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+, which bypass Apache file handles.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 99. CVE-2004-1085 (N/A)

**CVE ID**: CVE-2004-1085
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**Description**:
Human Interface Toolbox (HIToolBox) for Apple Mac 0S X 10.3.6 allows local users to exit applications via the force-quit key combination, even when the system is running in kiosk mode.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18352

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 100. CVE-2004-1086 (N/A)

**CVE ID**: CVE-2004-1086
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**Description**:
Buffer overflow in PSNormalizer for Apple Mac OS X 10.3.6 allows remote attackers to execute arbitrary code via a crafted PostScript input file.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18354

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
