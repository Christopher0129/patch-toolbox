# macOS 系统漏洞 | macOS System Vulnerabilities

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 06:02:20 UTC_

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
受影响产品: microsoft:java_virtual_machine, microsoft:internet_explorer

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
受影响产品: microsoft:ie, microsoft:internet_explorer, microsoft:visual_studio

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
受影响产品: sun:jre, sun:sdk, sun:jdk, apple:mac_os_runtime_for_java

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
受影响产品: sun:sdk, sun:jdk, microsoft:virtual_machine, sun:jre

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
受影响产品: sun:sdk, sun:jre, sun:jdk, microsoft:virtual_machine, hp:java_jre-jdk

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
受影响产品: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
受影响产品: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
受影响产品: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
受影响产品: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
受影响产品: apple:apple_laserwriter, apple:tcp_ip_configuration_utility

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: microsoft:windows_2000, microsoft:virtual_machine, microsoft:windows_2000_terminal_services

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
受影响产品: apple:safari, apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: sun:jdk, sun:jre

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: openldap:openldap, apple:mac_os_x_server, apple:mac_os_x

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
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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

#### 101. CVE-2004-1087 (N/A)

**CVE编号**: CVE-2004-1087
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**漏洞描述**:
Terminal for Apple Mac OS X 10.3.6 may indicate that "Secure Keyboard Entry" is enabled even when it is not, which could result in a false sense of security for the user.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18355

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 102. CVE-2004-1088 (N/A)

**CVE编号**: CVE-2004-1088
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**漏洞描述**:
Postfix server for Apple Mac OS X 10.3.6, when using CRAM-MD5, allows remote attackers to send mail without authentication by replaying authentication information.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18353

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 103. CVE-2004-1089 (N/A)

**CVE编号**: CVE-2004-1089
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**漏洞描述**:
Unknown vulnerability in Apple Mac OS X 10.3.6 server, when using Kerberos authentication and Cyrus IMAP allows local users to access mailboxes of other users.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18351

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 104. CVE-2004-1083 (HIGH)

**CVE编号**: CVE-2004-1083
**严重程度**: HIGH CVSS: 7.5
受影响产品: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**漏洞描述**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 restricts access to files in a case sensitive manner, but the Apple HFS+ filesystem accesses files in a case insensitive manner, which allows remote attackers to read .DS_Store files and files beginning with ".ht" using alternate capitalization.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 105. CVE-2004-0622 (N/A)

**CVE编号**: CVE-2004-0622
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:mac_os_x

**漏洞描述**:
Apple Mac OS X 10.3.4, 10.4, 10.5, and possibly other versions does not properly clear memory for login (aka Loginwindow.app), Keychain, or FileVault passwords, which could allow the root user or an attacker with physical access to obtain sensitive information by reading memory.

**应对措施**:
Apply patch from vendor. Monitor http://citp.princeton.edu/pub/coldboot.pdf.

**参考链接**:
- http://citp.princeton.edu/pub/coldboot.pdf
- http://marc.info/?l=bugtraq&m=108819559925981&w=2
- http://www.securityfocus.com/archive/1/488930/100/100/threaded
- http://www.securityfocus.com/archive/1/488948/100/100/threaded
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16557

> 📎 来源 / Source: http://citp.princeton.edu/pub/coldboot.pdf

#### 106. CVE-2004-1145 (N/A)

**CVE编号**: CVE-2004-1145
**严重程度**: N/A CVSS: 5.0
受影响产品: redhat:enterprise_linux_desktop, ethereal_group:ethereal, debian:debian_linux, altlinux:alt_linux, conectiva:linux

**漏洞描述**:
Multiple vulnerabilities in Konqueror in KDE 3.3.1 and earlier (1) allow access to restricted Java classes via JavaScript and (2) do not properly restrict access to certain Java classes from the Java applet, which allows remote attackers to bypass sandbox restrictions and read or write arbitrary files.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110356286722875&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=110356286722875&w=2
- http://secunia.com/advisories/13586
- http://www.gentoo.org/security/en/glsa/glsa-200501-16.xml
- http://www.heise.de/security/dienste/browsercheck/tests/java.shtml
- http://www.kb.cert.org/vuls/id/420222

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=110356286722875&w=2

#### 107. CVE-2004-0873 (N/A)

**CVE编号**: CVE-2004-0873
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:ichat, apple:ichat_av

**漏洞描述**:
Apple iChat AV 2.1, AV 2.0, and 1.0.1 allows remote attackers to execute arbitrary programs via a "link" that references the program.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17420
- http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17420

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html

#### 108. CVE-2004-0429 (N/A)

**CVE编号**: CVE-2004-0429
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:mac_os_x

**漏洞描述**:
Unknown vulnerability related to "the handling of large requests" in RAdmin for Apple Mac OS X 10.3.3 and Mac OS X 10.2.8 may allow attackers to have unknown impact via unknown attack vectors.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/May/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/May/msg00000.html
- http://marc.info/?l=bugtraq&m=108369640424244&w=2
- http://secunia.com/advisories/11539/
- http://securitytracker.com/id?1010045
- http://www.auscert.org.au/render.html?it=4070

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/May/msg00000.html

#### 109. CVE-2004-1398 (N/A)

**CVE编号**: CVE-2004-1398
**严重程度**: N/A CVSS: 4.6
受影响产品: roxio:toast

**漏洞描述**:
Format string vulnerability in prelink.c in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via format string specifiers in the extension argument.

**应对措施**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

**参考链接**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html
- http://marc.info/?l=bugtraq&m=110305083706943&w=2
- http://www.netragard.com/pdfs/research/apple-kext-tools-20060822.txt
- http://www.securityfocus.com/bid/11926
- http://www.securityfocus.com/bid/20031

> 📎 来源 / Source: http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html

#### 110. CVE-2004-1489 (N/A)

**CVE编号**: CVE-2004-1489
**严重程度**: N/A CVSS: 2.6
受影响产品: opera:opera_browser

**漏洞描述**:
Opera 7.54 and earlier does not properly limit an applet's access to internal Java packages from Sun, which allows remote attackers to gain sensitive information, such as user names and the installation directory.

**应对措施**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html.

**参考链接**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html
- http://www.gentoo.org/security/en/glsa/glsa-200502-17.xml
- http://www.opera.com/linux/changelogs/754u1/
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html
- http://www.gentoo.org/security/en/glsa/glsa-200502-17.xml

> 📎 来源 / Source: http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html

#### 111. CVE-2004-1753 (N/A)

**CVE编号**: CVE-2004-1753
**严重程度**: N/A CVSS: 2.6
受影响产品: mozilla:mozilla, mozilla:firefox, netscape:navigator

**漏洞描述**:
The Apple Java plugin, as used in Netscape 7.1 and 7.2, Mozilla 1.7.2, and Firefox 0.9.3 on MacOS X 10.3.5, when tabbed browsing is enabled, does not properly handle SetWindow(NULL) calls, which allows Java applets from one tab to draw to other tabs and facilitates phishing attacks that spoof tabs.

**应对措施**:
Apply patch from vendor. Monitor http://bugzilla.mozilla.org/show_bug.cgi?id=162134.

**参考链接**:
- http://bugzilla.mozilla.org/show_bug.cgi?id=162134
- http://secunia.com/advisories/12392
- http://www.securityfocus.com/archive/1/373080
- http://www.securityfocus.com/archive/1/373232
- http://www.securityfocus.com/archive/1/373309

> 📎 来源 / Source: http://bugzilla.mozilla.org/show_bug.cgi?id=162134

#### 112. CVE-2004-2280 (N/A)

**CVE编号**: CVE-2004-2280
**严重程度**: N/A CVSS: 5.0
受影响产品: ibm:lotus_notes

**漏洞描述**:
Buffer overflow in IBM Lotus Notes 6.5.x before 6.5.3 and 6.0.x before 6.0.5 allows remote attackers to cause a denial of service (crash) via unknown vectors related to Java applets, as identified by KSPR62F4KN.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**参考链接**:
- http://secunia.com/advisories/12046
- http://www-1.ibm.com/support/docview.wss?rs=475&context=SSKTWP&q1=Java&uid=swg21173910&loc=en_US&cs=utf-8&lang=en
- http://www.osvdb.org/8418
- http://www.securityfocus.com/bid/10704
- http://secunia.com/advisories/12046

> 📎 来源 / Source: http://secunia.com/advisories/12046

#### 113. CVE-2004-2281 (N/A)

**CVE编号**: CVE-2004-2281
**严重程度**: N/A CVSS: 10.0
受影响产品: ibm:lotus_notes

**漏洞描述**:
Multiple unknown vulnerabilities in IBM Lotus Notes 6.5.x before 6.5.4 and 6.0.x before 6.0.5 have unknown impact and attack vectors, related to Java applets, as identified by (1) KSPR5YS6GR and (2) KSPR62F4D3.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**参考链接**:
- http://secunia.com/advisories/12046
- http://www-1.ibm.com/support/docview.wss?rs=475&context=SSKTWP&q1=Java&uid=swg21173910&loc=en_US&cs=utf-8&lang=en
- http://www.osvdb.org/8416
- http://www.osvdb.org/8417
- http://www.securityfocus.com/bid/10704

> 📎 来源 / Source: http://secunia.com/advisories/12046

#### 114. CVE-2004-2359 (N/A)

**CVE编号**: CVE-2004-2359
**严重程度**: N/A CVSS: 10.0
受影响产品: dell:truemobile_1300_wlan_mini-pci_card_util_trayapplet

**漏洞描述**:
Dell TrueMobile 1300 WLAN Mini-PCI Card Util TrayApplet 3.10.39.0 does not properly drop SYSTEM privileges when started from the systray applet, which allows local users to gain privileges by accessing the Help functionality.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html.

**参考链接**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html
- http://secunia.com/advisories/10949
- http://securitytracker.com/id?1009174
- http://www.securityfocus.com/bid/9714
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15285

> 📎 来源 / Source: http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html

#### 115. CVE-2004-2367 (N/A)

**CVE编号**: CVE-2004-2367
**严重程度**: N/A CVSS: 5.0
受影响产品: texas_imperial_software:wftpd_pro, texas_imperial_software:wftpd

**漏洞描述**:
The Control Panel applet in WFTPD and WFTPD Pro 3.21 R1 and R2 allows remote authenticated users to cause a denial of service (crash) via a long FTP command.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/11160/.

**参考链接**:
- http://secunia.com/advisories/11160/
- http://www.securiteam.com/windowsntfocus/5JP0B20CAY.html
- http://www.securityfocus.com/bid/9908
- http://www.wftpd.com/bug_gpf.htm
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15510

> 📎 来源 / Source: http://secunia.com/advisories/11160/

#### 116. CVE-2004-0926 (N/A)

**CVE编号**: CVE-2004-0926
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:mac_os_x_server, apple:mac_os_x, easy_software_products:cups

**漏洞描述**:
Heap-based buffer overflow in Apple QuickTime on Mac OS 10.2.8 through 10.3.5 may allow remote attackers to execute arbitrary code via a certain BMP image.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html

#### 117. CVE-2004-0962 (N/A)

**CVE编号**: CVE-2004-0962
**严重程度**: N/A CVSS: 10.0
受影响产品: apple:apple_remote_desktop

**漏洞描述**:
Apple Remote Desktop Client 1.2.4 executes a GUI application as root when it is started by an Apple Remote Desktop Administrator application, which allows remote authenticated users to execute arbitrary code when loginwindow is active via Fast User Switching.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html

#### 118. CVE-2004-0988 (N/A)

**CVE编号**: CVE-2004-0988
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow on Apple QuickTime before 6.5.2, when running on Windows systems, allows remote attackers to cause a denial of service (memory consumption) via certain inputs that cause a large memory operation.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

#### 119. CVE-2004-1029 (N/A)

**CVE编号**: CVE-2004-1029
**严重程度**: N/A CVSS: 9.3
受影响产品: hp:java_sdk-rte, sun:jre, conectiva:linux, gentoo:linux, symantec:gateway_security_5400

**漏洞描述**:
The Sun Java Plugin capability in Java 2 Runtime Environment (JRE) 1.4.2_01, 1.4.2_04, and possibly earlier versions, does not properly restrict access between Javascript and Java applets during data transfer, which allows remote attackers to load unsafe classes and execute arbitrary code by using the reflection API to access private Java packages.

**应对措施**:
Apply patch from vendor. Monitor http://jouko.iki.fi/adv/javaplugin.html.

**参考链接**:
- http://jouko.iki.fi/adv/javaplugin.html
- http://lists.apple.com/archives/security-announce/2005/Feb/msg00000.html
- http://rpmfind.net/linux/RPM/suse/updates/9.3/i386/rpm/i586/java-1_4_2-sun-src-1.4.2.08-0.1.i586.html
- http://secunia.com/advisories/13271
- http://secunia.com/advisories/29035

> 📎 来源 / Source: http://jouko.iki.fi/adv/javaplugin.html

#### 120. CVE-2005-0043 (N/A)

**CVE编号**: CVE-2005-0043
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:itunes

**漏洞描述**:
Buffer overflow in Apple iTunes 4.7 allows remote attackers to execute arbitrary code via a long URL in (1) .m3u or (2) .pls playlist files.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html
- http://secunia.com/advisories/13804
- http://securitytracker.com/id?1012839
- http://www.idefense.com/application/poi/display?id=180&type=vulnerabilities
- http://www.kb.cert.org/vuls/id/377368

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html

#### 121. CVE-2005-0289 (N/A)

**CVE编号**: CVE-2005-0289
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:airport_extreme, apple:airport_express

**漏洞描述**:
Apple AirPort Express prior to 6.1.1 and Extreme prior to 5.5.1, configured as a Wireless Data Service (WDS), allows remote attackers to cause a denial of service (device freeze) by connecting to UDP port 161 and before link-state change occurs.

**应对措施**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html.

**参考链接**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html
- http://marc.info/?l=bugtraq&m=110582124528867&w=2
- http://secunia.com/advisories/13753
- http://www.securityfocus.com/bid/12152
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18865

> 📎 来源 / Source: http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html

#### 122. CVE-2005-0340 (N/A)

**CVE编号**: CVE-2005-0340
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:afp_server

**漏洞描述**:
Integer signedness error in Apple File Service (AFP Server) allows remote attackers to cause a denial of service (application crash) via a negative UAM string length in a FPLoginExt packet.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://marc.info/?l=bugtraq&m=110791369419784&w=2
- http://www.securityfocus.com/bid/12478
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19263
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

#### 123. CVE-2005-0341 (N/A)

**CVE编号**: CVE-2005-0341
**严重程度**: N/A CVSS: 4.3
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 1.2.4 does not obey the Content-type field in the HTTP header and renders text as HTML, which allows remote attackers to inject arbitrary web script or HTML and perform cross-site scripting (XSS) attacks.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110756965213819&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=110756965213819&w=2
- http://securitytracker.com/id?1013087
- http://tigger.uic.edu/~jrockw2/safari_20050204.txt
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19227
- http://marc.info/?l=bugtraq&m=110756965213819&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=110756965213819&w=2

#### 124. CVE-2005-0976 (N/A)

**CVE编号**: CVE-2005-0976
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari, omnigroup:omniweb, hmdt:shiira

**漏洞描述**:
AppleWebKit (WebCore and WebKit), as used in multiple products such as Safari 1.2 and OmniGroup OmniWeb 5.1, allows remote attackers to read arbitrary files via the XMLHttpRequest Javascript component, as demonstrated using automatically mounted disk images and file:// URLs.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://remahl.se/david/vuln/001/
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://remahl.se/david/vuln/001/

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html

#### 125. CVE-2005-1331 (N/A)

**CVE编号**: CVE-2005-1331
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:mac_os_x_server, apple:mac_os_x, apple:applescript

**漏洞描述**:
The AppleScript Editor in Mac OS X 10.3.9 does not properly display script code for an applescript: URI, which can result in code that is different than the actual code that would be run, which could allow remote attackers to trick users into executing malicious code via certain URI characters such as NULL, control characters, and homographs.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/010/
- http://secunia.com/advisories/15227
- http://www.securityfocus.com/bid/13480
- http://www.vupen.com/english/advisories/2005/0455

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 126. CVE-2005-1337 (N/A)

**CVE编号**: CVE-2005-1337
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Apple Help Viewer 2.0.7 and 3.0.0 in Mac OS X 10.3.9 allows remote attackers to read and execute arbitrary scrpts with less restrictive privileges via a help:// URI.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/004/
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/004/

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 127. CVE-2005-1341 (N/A)

**CVE编号**: CVE-2005-1341
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:terminal, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Apple Terminal 1.4.4 allows attackers to execute arbitrary commands via terminal escape sequences.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/012/
- http://secunia.com/advisories/15227
- http://securitytracker.com/id?1013882
- http://www.kb.cert.org/vuls/id/994510

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 128. CVE-2005-1342 (N/A)

**CVE编号**: CVE-2005-1342
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:terminal, apple:mac_os_x

**漏洞描述**:
The x-man-page: URI handler for Apple Terminal 1.4.4 in Mac OS X 10.3.9 does not cleanse terminal escape sequences, which allows remote attackers to execute arbitrary commands.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/011/
- http://secunia.com/advisories/15227
- http://www.kb.cert.org/vuls/id/356070
- http://www.osvdb.org/16084

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 129. CVE-2005-1579 (N/A)

**CVE编号**: CVE-2005-1579
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:quicktime

**漏洞描述**:
Apple QuickTime Player 7.0 on Mac OS X 10.4 allows remote attackers to obtain sensitive information via a .mov file with a Quartz Composer composition (.qtz) file that uses certain patches to read local information, then other patches to send the information to the attacker.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html
- http://docs.info.apple.com/article.html?artnum=301714
- http://lists.apple.com/archives/quartzcomposer-dev/2005/May/msg00250.html
- http://lists.apple.com/archives/quartzcomposer-dev/2005/May/msg00263.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00006.html

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html

#### 130. CVE-2005-1193 (N/A)

**CVE编号**: CVE-2005-1193
**严重程度**: N/A CVSS: 7.5
受影响产品: phpbb_group:phpbb

**漏洞描述**:
The bbencode_second_pass and make_clickable functions in bbcode.php for phpBB before 2.0.15, as used in viewtopic.php, privmsg.php, and other scripts, allow remote attackers to execute arbitrary script via a BBcode tag with a (1) javascript:, (2) applet:, (3) about:, (4) activex:, (5) chrome:, or (6) script: URI scheme, as demonstrated using the URL tag.

**应对措施**:
Apply patch from vendor. Monitor http://castlecops.com/t123194-.html.

**参考链接**:
- http://castlecops.com/t123194-.html
- http://marc.info/?l=full-disclosure&m=111552510000088&w=2
- http://seclists.org/lists/bugtraq/2005/May/0098.html
- http://secunia.com/advisories/15298
- http://securitytracker.com/id?1013918

> 📎 来源 / Source: http://castlecops.com/t123194-.html

#### 131. CVE-2005-1248 (N/A)

**CVE编号**: CVE-2005-1248
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:itunes

**漏洞描述**:
Buffer overflow in Apple iTunes before 4.8 allows remote attackers to execute arbitrary code via a crafted MPEG4 file.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301596.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=301596
- http://lists.apple.com/archives/security-announce/2005/May/msg00003.html
- http://secunia.com/advisories/15310
- http://securitytracker.com/id?1013927
- http://www.ngssoftware.com/advisories/itunes.txt

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=301596

#### 132. CVE-2005-1472 (N/A)

**CVE编号**: CVE-2005-1472
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:mac_os_x

**漏洞描述**:
Certain system calls in Apple Mac OS X 10.4.1 do not properly enforce the permissions of certain directories without the POSIX read bit set, but with the execute bits set for group or other, which allows local users to list files in otherwise restricted directories.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 133. CVE-2005-1408 (N/A)

**CVE编号**: CVE-2005-1408
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:keynote

**漏洞描述**:
Apple Keynote 2.0 and 2.0.1 allows remote attackers to read arbitrary files via the keynote: URI handler in a crafted Keynote presentation.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00005.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00005.html
- http://remahl.se/david/vuln/016/
- http://secunia.com/advisories/15508
- http://securitytracker.com/id?1014053
- http://lists.apple.com/archives/security-announce/2005/May/msg00005.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00005.html

#### 134. CVE-2005-1723 (N/A)

**CVE编号**: CVE-2005-1723
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server

**漏洞描述**:
LaunchServices in Apple Mac OS X 10.4.x up to 10.4.1 does not properly mark file extensions and MIME types as unsafe if an Apple Uniform Type Identifier (UTI) is not created when the type is added to the database of unsafe types, which could allow attackers to bypass intended restrictions.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014141
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014141

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 135. CVE-2005-1724 (N/A)

**CVE编号**: CVE-2005-1724
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server

**漏洞描述**:
NFS on Apple Mac OS X 10.4.x up to 10.4.1 does not properly obey the -network or -mask flags for a filesystem and exports it to everyone, which allows remote attackers to bypass intended access restrictions.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014142
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014142

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 136. CVE-2005-1725 (N/A)

**CVE编号**: CVE-2005-1725
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:mac_os_x_server

**漏洞描述**:
launchd 106 in Apple Mac OS X 10.4.x up to 10.4.1 allows local users to overwrite arbitrary files via a symlink attack on the socket file in an insecure temporary directory.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://marc.info/?l=bugtraq&m=111833509424379&w=2
- http://www.suresec.org/advisories/adv3.pdf
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://marc.info/?l=bugtraq&m=111833509424379&w=2

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 137. CVE-2005-1727 (N/A)

**CVE编号**: CVE-2005-1727
**严重程度**: N/A CVSS: 3.7
受影响产品: apple:mac_os_x_server

**漏洞描述**:
Apple Mac OS X 10.4.x up to 10.4.1 sets insecure world- and group-writable permissions for the (1) system cache folder and (2) Dashboard system widgets, which allows local users to conduct unauthorized file operations via "file race conditions."

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 138. CVE-2005-1728 (N/A)

**CVE编号**: CVE-2005-1728
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:mac_os_x

**漏洞描述**:
MCX Client for Apple Mac OS X 10.4.x up to 10.4.1 insecurely logs Portable Home Directory credentials, which allows local users to obtain the credentials.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014148
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014148

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 139. CVE-2005-1473 (N/A)

**CVE编号**: CVE-2005-1473
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:mac_os_x

**漏洞描述**:
SecurityAgent in Apple Mac OS X 10.4.1 allows attackers with physical access to bypass the locked screensaver and launch background applications by opening a URL from a text input field.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 140. CVE-2005-1474 (N/A)

**CVE编号**: CVE-2005-1474
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Dashboard in Apple Mac OS X 10.4.1 allows remote attackers to install widgets via Safari without prompting the user, a different vulnerability than CVE-2005-1933.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://www.securityfocus.com/bid/13694
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://www.securityfocus.com/bid/13694

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 141. CVE-2005-1933 (N/A)

**CVE编号**: CVE-2005-1933
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x

**漏洞描述**:
Dashboard in Apple Mac OS X Tiger 10.4 allows attackers to execute arbitrary commands by overriding the behavior of system widgets via a user widget with the same bundle identifier (CFBundleIdentifier), a different vulnerability than CVE-2005-1474.

**应对措施**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/983429.

**参考链接**:
- http://www.kb.cert.org/vuls/id/983429
- http://www1.cs.columbia.edu/~aaron/files/widgets/
- http://www.kb.cert.org/vuls/id/983429
- http://www1.cs.columbia.edu/~aaron/files/widgets/

> 📎 来源 / Source: http://www.kb.cert.org/vuls/id/983429

#### 142. CVE-2005-2195 (N/A)

**CVE编号**: CVE-2005-2195
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:darwin_streaming_server

**漏洞描述**:
Apple Darwin Streaming Server 5.5 and earlier allows remote attackers to cause a denial of service (application crash) via a URL with a filename containing a .cgi extension and an MS-DOS device name such as AUX, CON, PRN, COM1, or LPT1, a different vulnerability than CVE-2003-0421 and CVE-2003-0502.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112126999514361&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=112126999514361&w=2
- http://secunia.com/advisories/16056
- http://securitytracker.com/id?1014474
- http://secway.org/Advisory/AD20050713.txt
- http://marc.info/?l=bugtraq&m=112126999514361&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=112126999514361&w=2

#### 143. CVE-2005-2196 (N/A)

**CVE编号**: CVE-2005-2196
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:airport_card

**漏洞描述**:
The Apple AirPort card uses a default WEP key when not connected to a known or trusted network, which can cause it to automatically connect to a malicious network.

**应对措施**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1014522.

**参考链接**:
- http://securitytracker.com/id?1014522
- http://www.securityfocus.com/bid/14321
- http://securitytracker.com/id?1014522
- http://www.securityfocus.com/bid/14321

> 📎 来源 / Source: http://securitytracker.com/id?1014522

#### 144. CVE-2005-2594 (N/A)

**CVE编号**: CVE-2005-2594
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 1.3 (132) on Mac OS X 1.3.9 allows remote attackers to cause a denial of service (crash) via certain Javascript, possibly involving a function that defines a handler for itself within the function body.

**应对措施**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/407702.

**参考链接**:
- http://www.securityfocus.com/archive/1/407702
- http://www.securityfocus.com/bid/14528
- http://www.securityfocus.com/archive/1/407702
- http://www.securityfocus.com/bid/14528

> 📎 来源 / Source: http://www.securityfocus.com/archive/1/407702

#### 145. CVE-2005-3018 (N/A)

**CVE编号**: CVE-2005-3018
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
Apple Safari allows remote attackers to cause a denial of service (application crash) via a crafted data:// URL.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112715234411672&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=112715234411672&w=2
- http://secunia.com/advisories/16875/
- http://www.osvdb.org/19569
- http://www.securityfocus.com/bid/14868
- https://exchange.xforce.ibmcloud.com/vulnerabilities/22331

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=112715234411672&w=2

#### 146. CVE-2005-2744 (N/A)

**CVE编号**: CVE-2005-2744
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Buffer overflow in QuickDraw Manager for Apple OS X 10.3.9 and 10.4.2, as used by applications such as Safari, Mail, and Finder, allows remote attackers to execute arbitrary code via a crafted PICT file.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://securitytracker.com/alerts/2005/Sep/1014961.html
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 147. CVE-2005-2747 (N/A)

**CVE编号**: CVE-2005-2747
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Buffer overflow in ImageIO for Apple Mac OS X 10.4.2, as used by applications such as WebCore and Safari, allows remote attackers to execute arbitrary code via a crafted GIF file.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://securitytracker.com/alerts/2005/Sep/1014958.html
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 148. CVE-2005-2748 (N/A)

**CVE编号**: CVE-2005-2748
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
The malloc function in the libSystem library in Apple Mac OS X 10.3.9 and 10.4.2 allows local users to overwrite arbitrary files by setting the MallocLogFile environment variable to the target file before running a setuid application.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://www.suresec.org/advisories/adv7.pdf

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 149. CVE-2005-2524 (N/A)

**CVE编号**: CVE-2005-2524
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Safari after 2.0 in Apple Mac OS X 10.3.9 allows remote attackers to bypass domain restrictions via crafted web archives that cause Safari to render them as if they came from a different site.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 150. CVE-2005-2741 (N/A)

**CVE编号**: CVE-2005-2741
**严重程度**: N/A CVSS: 7.2
受影响产品: perry_kiehtreiber:securityd, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Authorization Services in securityd for Apple Mac OS X 10.3.9 allows local users to gain privileges by granting themselves certain rights that should be restricted to administrators.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 151. CVE-2005-2742 (N/A)

**CVE编号**: CVE-2005-2742
**严重程度**: N/A CVSS: 4.6
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
SecurityAgent in Apple Mac OS X 10.4.2, under certain circumstances, can cause the "Switch User..." button to appear even though the "Enable fast user switching" setting is disabled, which can allow attackers with physical access to gain access to the desktop and bypass the "Require password to wake this computer from sleep or screen saver" setting.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 152. CVE-2005-2743 (N/A)

**CVE编号**: CVE-2005-2743
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x, apple:quicktime

**漏洞描述**:
The Java extensions for QuickTime 6.52 and earlier in Apple Mac OS X 10.3.9 allow untrusted applets to call arbitrary functions in system libraries, which allows remote attackers to execute arbitrary code.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 153. CVE-2005-2745 (N/A)

**CVE编号**: CVE-2005-2745
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Mail.app in Mail for Apple Mac OS X 10.3.9, when using Kerberos 5 for SMTP authentication, can include uninitialized memory in a message, which might allow remote attackers to obtain sensitive information.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 154. CVE-2005-2746 (N/A)

**CVE编号**: CVE-2005-2746
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Mail.app in Mail for Apple Mac OS X 10.3.9 and 10.4.2 includes message contents when using auto-reply rules, which could cause Mail.app to include decrypted message contents for encrypted messages.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 155. CVE-2005-2753 (N/A)

**CVE编号**: CVE-2005-2753
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file that causes a sign extension of the length element in a Pascal style string.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-io1-adv.txt
- http://secunia.com/advisories/17428
- http://securitytracker.com/id?1015152
- http://www.osvdb.org/20475

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302772

#### 156. CVE-2005-2754 (N/A)

**CVE编号**: CVE-2005-2754
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file with "Improper movie attributes."

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-io2-adv.txt
- http://secunia.com/advisories/17428
- http://securitytracker.com/id?1015152
- http://www.osvdb.org/20476

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302772

#### 157. CVE-2005-2755 (N/A)

**CVE编号**: CVE-2005-2755
**严重程度**: N/A CVSS: 2.6
受影响产品: apple:quicktime

**漏洞描述**:
Apple QuickTime Player before 7.0.3 allows user-assisted attackers to cause a denial of service (crash) via a crafted file with a missing movie attribute, which leads to a null dereference.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-dos-adv.txt
- http://secunia.com/advisories/17428
- http://securityreason.com/securityalert/145

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html

#### 158. CVE-2005-2756 (N/A)

**CVE编号**: CVE-2005-2756
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Apple QuickTime before 7.0.3 allows user-assisted attackers to overwrite memory and execute arbitrary code via a crafted PICT file that triggers an overflow during expansion.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-pict-adv.txt
- http://secunia.com/advisories/17428
- http://securityreason.com/securityalert/144
- http://securitytracker.com/id?1015152

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302772

#### 159. CVE-2005-3897 (N/A)

**CVE编号**: CVE-2005-3897
**严重程度**: N/A CVSS: 7.8
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 2.0.2 allows remote attackers to cause a denial of service (system slowdown) via a Javascript BODY onload event that calls the window function.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=113278010907401&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=113278010907401&w=2
- http://marc.info/?l=bugtraq&m=113278010907401&w=2

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=113278010907401&w=2

#### 160. CVE-2005-3907 (N/A)

**CVE编号**: CVE-2005-3907
**严重程度**: N/A CVSS: 7.5
受影响产品: sun:jdk, sun:jre

**漏洞描述**:
Unspecified vulnerability in Java Runtime Environment in Java JDK and JRE 5.0 Update 3 and earlier allows remote attackers to escape the Java sandbox and access arbitrary files or execute arbitrary applications via unknown attack vectors involving untrusted Java applets.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html
- http://secunia.com/advisories/17748
- http://secunia.com/advisories/17847
- http://secunia.com/advisories/18092
- http://securitytracker.com/id?1015282

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html

#### 161. CVE-2005-3946 (N/A)

**CVE编号**: CVE-2005-3946
**严重程度**: N/A CVSS: 5.0
受影响产品: opera:opera_browser

**漏洞描述**:
Opera 8.50 allows remote attackers to cause a denial of service (crash) via a Java applet with a large string argument to the removeMember JNI method for the com.opera.JSObject class.

**应对措施**:
Apply patch from vendor. Monitor http://www.illegalaccess.org/exploit/opera85/OperaApplet.html.

**参考链接**:
- http://www.illegalaccess.org/exploit/opera85/OperaApplet.html
- http://www.securityfocus.com/archive/1/418201/100/0/threaded
- http://www.securityfocus.com/archive/1/418274/100/0/threaded
- http://www.securityfocus.com/bid/15648
- http://www.illegalaccess.org/exploit/opera85/OperaApplet.html

> 📎 来源 / Source: http://www.illegalaccess.org/exploit/opera85/OperaApplet.html

#### 162. CVE-2005-4092 (N/A)

**CVE编号**: CVE-2005-4092
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:itunes, apple:quicktime

**漏洞描述**:
Multiple heap-based buffer overflows in QuickTime.qts in Apple QuickTime Player 7.0.3 and iTunes 6.0.1 (3) and earlier allow remote attackers to cause a denial of service (crash) and execute arbitrary code via a .mov file with (1) a Movie Resource atom with a large size value, or (2) an stsd atom with a modified Sample Description Table size value, and possibly other vectors involving media files.  NOTE: item 1 was originally identified by CVE-2005-4127 for a pre-patch announcement, and item 2 was originally identified by CVE-2005-4128 for a pre-patch announcement.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18149
- http://secunia.com/advisories/18370
- http://security-protocols.com/advisory/sp-x21-advisory.txt
- http://securityreason.com/securityalert/334

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303101

#### 163. CVE-2005-4197 (N/A)

**CVE编号**: CVE-2005-4197
**严重程度**: N/A CVSS: 7.5
受影响产品: nortel:ssl_vpn

**漏洞描述**:
tunnelform.yaws in Nortel SSL VPN 4.2.1.6 allows remote attackers to execute arbitrary commands via a link in the a parameter, which is executed with extra privileges in a cryptographically signed Java Applet.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17974.

**参考链接**:
- http://secunia.com/advisories/17974
- http://securitytracker.com/id?1015341
- http://www.sec-consult.com/247.html
- http://www.securityfocus.com/archive/1/419263/100/0/threaded
- http://www.securityfocus.com/bid/15798

> 📎 来源 / Source: http://secunia.com/advisories/17974

#### 164. CVE-2005-4217 (N/A)

**CVE编号**: CVE-2005-4217
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server

**漏洞描述**:
Perl in Apple Mac OS X Server 10.3.9 does not properly drop privileges when using the "$<" variable to set uid, which allows attackers to gain privileges.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00000.html
- http://secunia.com/advisories/17922
- http://secunia.com/advisories/19064
- http://www.osvdb.org/21800

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303382

#### 165. CVE-2005-4504 (N/A)

**CVE编号**: CVE-2005-4504
**严重程度**: N/A CVSS: 7.8
受影响产品: apple:safari, apple:textedit, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
The khtml::RenderTableSection::ensureRows function in KHTMLParser in Apple Mac OS X 10.4.3 and earlier, as used by Safari and TextEdit, allows remote attackers to cause a denial of service (memory consumption and application crash) via HTML files with a large ROWSPAN attribute in a TD tag.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://docs.info.apple.com/jarticle.html?artnum=303382-en
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00000.html
- http://secunia.com/advisories/18220
- http://secunia.com/advisories/19064

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303382

#### 166. CVE-2005-2194 (N/A)

**CVE编号**: CVE-2005-2194
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x

**漏洞描述**:
Unspecified vulnerability in the Apple Mac OS X kernel before 10.4.2 allows remote attackers to cause a denial of service (kernel panic) via a crafted TCP packet, possibly related to source routing or loose source routing.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301948.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=301948
- http://lists.apple.com/archives/Security-announce/2005/Jul/msg00000.html
- http://secunia.com/advisories/16047
- http://securitytracker.com/id?1014464
- http://www.osvdb.org/17880

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=301948

#### 167. CVE-2005-2340 (N/A)

**CVE编号**: CVE-2005-2340
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a crafted (1) QuickTime Image File (QTIF), (2) PICT, or (3) JPEG format image with a long data field.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0398.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0402.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html

#### 168. CVE-2005-2527 (N/A)

**CVE编号**: CVE-2005-2527
**严重程度**: N/A CVSS: 1.2
受影响产品: sun:java

**漏洞描述**:
Race condition in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to corrupt files or create arbitrary files via unspecified attack vectors related to a temporary directory, possibly due to a symlink attack.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302266
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.securityfocus.com/bid/14825

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302266

#### 169. CVE-2005-2529 (N/A)

**CVE编号**: CVE-2005-2529
**严重程度**: N/A CVSS: 10.0
受影响产品: sun:java

**漏洞描述**:
Unspecified vulnerability in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to gain privileges via unspecified attack vectors relating to "the utility used to update Java shared archives."

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302266
- http://lists.apple.com/archives/Security-announce/2005/Sep/msg00000.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.vupen.com/english/advisories/2005/1734

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302266

#### 170. CVE-2005-2530 (N/A)

**CVE编号**: CVE-2005-2530
**严重程度**: N/A CVSS: 10.0
受影响产品: sun:java

**漏洞描述**:
Unspecified vulnerability in Java 1.3.1 before 1.3.1_16 on Apple Mac OS X allows an untrusted applet to gain privileges, related to "Mac OS X specific extensions."

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302265
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.securityfocus.com/bid/14826

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302265

#### 171. CVE-2005-2738 (N/A)

**CVE编号**: CVE-2005-2738
**严重程度**: N/A CVSS: 5.0
受影响产品: sun:java

**漏洞描述**:
Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X does not prevent multiple programs from opening the same port as a Java ServerSocket, which allows local users to operate a Java program that intercepts network data intended for the ServerSocket of a different Java program.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=302265
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.osvdb.org/19397

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=302265

#### 172. CVE-2005-3707 (N/A)

**CVE编号**: CVE-2005-3707
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.kb.cert.org/vuls/id/115729

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html

#### 173. CVE-2005-3708 (N/A)

**CVE编号**: CVE-2005-3708
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.osvdb.org/22336
- http://www.securityfocus.com/bid/16202

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303101

#### 174. CVE-2005-3709 (N/A)

**CVE编号**: CVE-2005-3709
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Integer underflow in Apple Quicktime before 7.0.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via the Color Map Entry Size in a TGA image file.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.osvdb.org/22336

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html

#### 175. CVE-2005-3710 (N/A)

**CVE编号**: CVE-2005-3710
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified image height and width (ImageWidth) tags.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securityreason.com/securityalert/347
- http://securitytracker.com/id?1015465

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html

#### 176. CVE-2005-3711 (N/A)

**CVE编号**: CVE-2005-3711
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified (1) "strips" (StripByteCounts) or (2) "bands" (StripOffsets) values.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015465
- http://www.osvdb.org/22337

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html

#### 177. CVE-2005-3713 (N/A)

**CVE编号**: CVE-2005-3713
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:quicktime

**漏洞描述**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a GIF image file with a crafted Netscape Navigator Application Extension Block that modifies the heap in the Picture Modifier block.

**应对措施**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html.

**参考链接**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0402.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securityreason.com/securityalert/333

> 📎 来源 / Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html

#### 178. CVE-2005-3714 (N/A)

**CVE编号**: CVE-2005-3714
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:airport_extreme, apple:airport_express

**漏洞描述**:
The network interface for Apple AirPort Express 6.x before Firmware Update 6.3, and AirPort Extreme 5.x before Firmware Update 5.7, allows remote attackers to cause a denial of service (unresponsive interface) via malformed packets.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html
- http://secunia.com/advisories/18319
- http://securitytracker.com/id?1015443
- http://www.osvdb.org/22244
- http://www.securityfocus.com/bid/16146

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html

#### 179. CVE-2005-4678 (N/A)

**CVE编号**: CVE-2005-4678
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 2.0.2 (aka 416.12) allows remote attackers to spoof the URL in the status bar via the title in an image in a link to a trusted site within a form to the malicious site.  NOTE: the provenance of this information is unknown; the details are obtained solely from third party information.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17618.

**参考链接**:
- http://secunia.com/advisories/17618
- http://secunia.com/advisories/17618

> 📎 来源 / Source: http://secunia.com/advisories/17618

#### 180. CVE-2005-4866 (N/A)

**CVE编号**: CVE-2005-4866
**严重程度**: N/A CVSS: 6.8
受影响产品: ibm:db2_universal_database

**漏洞描述**:
Stack-based buffer overflow in JDBC Applet Server in IBM DB2 8.1 allows remote attackers to execute arbitrary by connecting and sending a long username, then disconnecting gracefully and reconnecting and sending a short username and an unexpected db2java.zip version, which causes a null terminator to be removed and leads to the overflow.

**应对措施**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110495251101381&w=2.

**参考链接**:
- http://marc.info/?l=bugtraq&m=110495251101381&w=2
- http://secunia.com/advisories/12733/
- http://www-1.ibm.com/support/docview.wss?uid=swg1IY61492
- http://www.nextgenss.com/advisories/db205012005D.txt
- http://www.securityfocus.com/bid/11401

> 📎 来源 / Source: http://marc.info/?l=bugtraq&m=110495251101381&w=2

#### 181. CVE-2006-0382 (N/A)

**CVE编号**: CVE-2006-0382
**严重程度**: N/A CVSS: 2.1
受影响产品: apple:mac_os_x

**漏洞描述**:
Apple Mac OS X 10.4.5 and allows local users to cause a denial of service (crash) via an undocumented system call.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html
- http://secunia.com/advisories/18907
- http://securitytracker.com/id?1015634
- http://www.osvdb.org/23190
- http://www.securityfocus.com/bid/16654

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html

#### 182. CVE-2006-0848 (N/A)

**CVE编号**: CVE-2006-0848
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
The "Open 'safe' files after downloading" option in Safari on Apple Mac OS X allows remote user-assisted attackers to execute arbitrary commands by tricking a user into downloading a __MACOSX folder that contains metadata (resource fork) that invokes the Terminal, which automatically interprets the script using bash, as demonstrated using a ZIP file that contains a script with a safe file extension.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://secunia.com/advisories/18963
- http://securitytracker.com/id?1015652
- http://www.frsirt.com/exploits/20060222.safari_safefiles_exec.pm.php
- http://www.heise.de/english/newsticker/news/69862

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303382

#### 183. CVE-2006-0396 (N/A)

**CVE编号**: CVE-2006-0396
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Buffer overflow in Mail in Apple Mac OS X 10.4 up to 10.4.5, when patched with Security Update 2006-001, allows remote attackers to execute arbitrary code via a long Real Name value in an e-mail attachment sent in AppleDouble format, which triggers the overflow when the user double-clicks on an attachment.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015762
- http://www.digitalmunition.com/DMA%5B2006-0313a%5D.txt

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303453

#### 184. CVE-2006-0397 (N/A)

**CVE编号**: CVE-2006-0397
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23869

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303453

#### 185. CVE-2006-0398 (N/A)

**CVE编号**: CVE-2006-0398
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23870

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303453

#### 186. CVE-2006-0399 (N/A)

**CVE编号**: CVE-2006-0399
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23871

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303453

#### 187. CVE-2006-0400 (N/A)

**CVE编号**: CVE-2006-0400
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述**:
CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to bypass the same-origin policy and execute Javascript in other domains via unknown vectors involving "crafted archives."

**应对措施**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015763
- http://www.osvdb.org/23873

> 📎 来源 / Source: http://docs.info.apple.com/article.html?artnum=303453

#### 188. CVE-2006-1249 (N/A)

**CVE编号**: CVE-2006-1249
**严重程度**: N/A CVSS: 6.8
受影响产品: apple:itunes, apple:quicktime

**漏洞描述**:
Integer overflow in Apple QuickTime Player 7.0.3 and 7.0.4 and iTunes 6.0.1 and 6.0.2 allows remote attackers to execute arbitrary code via a FlashPix (FPX) image that contains a field that specifies a large number of blocks.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securitytracker.com/id?1016067
- http://www.eeye.com/html/research/upcoming/20060307b.html
- http://www.kb.cert.org/vuls/id/570689

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 189. CVE-2006-1552 (N/A)

**CVE编号**: CVE-2006-1552
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari, apple:mac_os_x_server, apple:mac_os_x, apple:imageio

**漏洞描述**:
Integer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to cause a denial of service (crash) via a crafted JPEG image with malformed JPEG metadata, as demonstrated using Safari, aka "Deja-Doom".

**应对措施**:
Apply patch from vendor. Monitor http://drunkenblog.com/drunkenblog-archives/000760.html.

**参考链接**:
- http://drunkenblog.com/drunkenblog-archives/000760.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20077
- http://www.osvdb.org/25597
- http://www.securityfocus.com/bid/17321

> 📎 来源 / Source: http://drunkenblog.com/drunkenblog-archives/000760.html

#### 190. CVE-2006-1986 (N/A)

**CVE编号**: CVE-2006-1986
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via a large CELLSPACING attribute in a TABLE tag, which triggers an error in KWQListIteratorImpl::KWQListIteratorImpl.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-1.html
- http://www.osvdb.org/24823
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634

> 📎 来源 / Source: http://secunia.com/advisories/19686

#### 191. CVE-2006-1987 (N/A)

**CVE编号**: CVE-2006-1987
**严重程度**: N/A CVSS: 7.5
受影响产品: apple:safari

**漏洞描述**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via an invalid FRAME tag, possibly due to (1) multiple SCROLLING attributes with no values, or (2) a SRC attribute with no value.  NOTE: due to lack of diagnosis by the researcher, it is unclear which vector is responsible.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-4.html
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634
- http://www.vupen.com/english/advisories/2006/1452

> 📎 来源 / Source: http://secunia.com/advisories/19686

#### 192. CVE-2006-1988 (N/A)

**CVE编号**: CVE-2006-1988
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
The WebTextRenderer(WebInternal) _CG_drawRun:style:geometry: function in Apple Safari 2.0.3 allows remote attackers to cause a denial of service (application crash) via an HTML LI tag with a large VALUE attribute (list item number), which triggers a null dereference in QPainter::drawText, probably due to a failed memory allocation that uses the VALUE.

**应对措施**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-2.html
- http://www.osvdb.org/24823
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634

> 📎 来源 / Source: http://secunia.com/advisories/19686

#### 193. CVE-2006-2019 (N/A)

**CVE编号**: CVE-2006-2019
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:safari

**漏洞描述**:
Apple Mac OS X Safari 2.0.3, 1.3.1, and possibly other versions allows remote attackers to cause a denial of service (CPU consumption and crash) via a TD element with a large number in the rowspan attribute.

**应对措施**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html.

**参考链接**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html
- http://secunia.com/advisories/19763
- http://securitytracker.com/id?1015982
- http://www.securityfocus.com/archive/1/431874/100/0/threaded
- http://www.securityfocus.com/archive/1/431944/100/0/threaded

> 📎 来源 / Source: http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html

#### 194. CVE-2006-2277 (N/A)

**CVE编号**: CVE-2006-2277
**严重程度**: N/A CVSS: 5.0
受影响产品: apple:mac_os_x

**漏洞描述**:
Multiple Apple Mac OS X 10.4 applications might allow context-dependent attackers to cause a denial of service (application crash) via a crafted OpenEXR (.exr) image file, which triggers the crash when opening a folder using Finder, displaying the image in Safari, or using Preview to open the file.

**应对措施**:
Apply patch from vendor. Monitor http://www.osvdb.org/27780.

**参考链接**:
- http://www.osvdb.org/27780
- http://www.securityfocus.com/archive/1/432587/100/0/threaded
- http://www.securityfocus.com/bid/17768
- https://github.com/openexr/openexr/issues/564
- http://www.osvdb.org/27780

> 📎 来源 / Source: http://www.osvdb.org/27780

#### 195. CVE-2006-1453 (N/A)

**CVE编号**: CVE-2006-1453
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Stack-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file containing malformed font information.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20069
- http://secunia.com/advisories/20077
- http://securityreason.com/securityalert/887

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 196. CVE-2006-1454 (N/A)

**CVE编号**: CVE-2006-1454
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file with malformed image data.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20069
- http://secunia.com/advisories/20077
- http://securityreason.com/securityalert/887

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 197. CVE-2006-1458 (N/A)

**CVE编号**: CVE-2006-1458
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Integer overflow in Apple QuickTime Player before 7.1 allows remote attackers to execute arbitrary code via a crafted JPEG image.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securitytracker.com/id?1016067
- http://www.kb.cert.org/vuls/id/289705
- http://www.securityfocus.com/bid/17953

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 198. CVE-2006-1459 (N/A)

**CVE编号**: CVE-2006-1459
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to cause a denial of service or execute arbitrary code via a crafted QuickTime movie (.MOV).

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067
- http://www.securityfocus.com/archive/1/433831/100/0/threaded

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 199. CVE-2006-1460 (N/A)

**CVE编号**: CVE-2006-1460
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime movie (.MOV), as demonstrated via a large size for a udta Atom.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-May/045987.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 200. CVE-2006-1461 (N/A)

**CVE编号**: CVE-2006-1461
**严重程度**: N/A CVSS: 5.1
受影响产品: apple:quicktime

**漏洞描述**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime Flash (SWF) file.

**应对措施**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067
- http://www.securityfocus.com/archive/1/433831/100/0/threaded

> 📎 来源 / Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html


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
**Affected Products**: microsoft:java_virtual_machine, microsoft:internet_explorer

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
**Affected Products**: microsoft:ie, microsoft:internet_explorer, microsoft:visual_studio

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
**Affected Products**: sun:jre, sun:sdk, sun:jdk, apple:mac_os_runtime_for_java

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
**Affected Products**: sun:sdk, sun:jdk, microsoft:virtual_machine, sun:jre

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
**Affected Products**: sun:sdk, sun:jre, sun:jdk, microsoft:virtual_machine, hp:java_jre-jdk

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
**Affected Products**: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
**Affected Products**: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
**Affected Products**: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
**Affected Products**: microsoft:windows_95, microsoft:windows_xp, microsoft:windows_me, microsoft:windows_98, microsoft:windows_98se

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
**Affected Products**: apple:apple_laserwriter, apple:tcp_ip_configuration_utility

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: microsoft:windows_2000, microsoft:virtual_machine, microsoft:windows_2000_terminal_services

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
**Affected Products**: apple:safari, apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: sun:jdk, sun:jre

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:darwin_streaming_server

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: openldap:openldap, apple:mac_os_x_server, apple:mac_os_x

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
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

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

#### 101. CVE-2004-1087 (N/A)

**CVE ID**: CVE-2004-1087
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**Description**:
Terminal for Apple Mac OS X 10.3.6 may indicate that "Secure Keyboard Entry" is enabled even when it is not, which could result in a false sense of security for the user.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18355

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 102. CVE-2004-1088 (N/A)

**CVE ID**: CVE-2004-1088
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**Description**:
Postfix server for Apple Mac OS X 10.3.6, when using CRAM-MD5, allows remote attackers to send mail without authentication by replaying authentication information.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18353

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 103. CVE-2004-1089 (N/A)

**CVE ID**: CVE-2004-1089
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**Description**:
Unknown vulnerability in Apple Mac OS X 10.3.6 server, when using Kerberos authentication and Cyrus IMAP allows local users to access mailboxes of other users.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/11802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18351

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 104. CVE-2004-1083 (HIGH)

**CVE ID**: CVE-2004-1083
**Severity**: HIGH CVSS: 7.5
**Affected Products**: apple:quicktime_streaming_server, apple:mac_os_x_server, apple:mac_os_x, apple:darwin_streaming_server

**Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 restricts access to files in a case sensitive manner, but the Apple HFS+ filesystem accesses files in a case insensitive manner, which allows remote attackers to read .DS_Store files and files beginning with ".ht" using alternate capitalization.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://secunia.com/advisories/13362/
- http://www.ciac.org/ciac/bulletins/p-049.shtml

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html

#### 105. CVE-2004-0622 (N/A)

**CVE ID**: CVE-2004-0622
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:mac_os_x

**Description**:
Apple Mac OS X 10.3.4, 10.4, 10.5, and possibly other versions does not properly clear memory for login (aka Loginwindow.app), Keychain, or FileVault passwords, which could allow the root user or an attacker with physical access to obtain sensitive information by reading memory.

**Mitigation**:
Apply patch from vendor. Monitor http://citp.princeton.edu/pub/coldboot.pdf.

**References**:
- http://citp.princeton.edu/pub/coldboot.pdf
- http://marc.info/?l=bugtraq&m=108819559925981&w=2
- http://www.securityfocus.com/archive/1/488930/100/100/threaded
- http://www.securityfocus.com/archive/1/488948/100/100/threaded
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16557

> 📎 Source: http://citp.princeton.edu/pub/coldboot.pdf

#### 106. CVE-2004-1145 (N/A)

**CVE ID**: CVE-2004-1145
**Severity**: N/A CVSS: 5.0
**Affected Products**: redhat:enterprise_linux_desktop, ethereal_group:ethereal, debian:debian_linux, altlinux:alt_linux, conectiva:linux

**Description**:
Multiple vulnerabilities in Konqueror in KDE 3.3.1 and earlier (1) allow access to restricted Java classes via JavaScript and (2) do not properly restrict access to certain Java classes from the Java applet, which allows remote attackers to bypass sandbox restrictions and read or write arbitrary files.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110356286722875&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=110356286722875&w=2
- http://secunia.com/advisories/13586
- http://www.gentoo.org/security/en/glsa/glsa-200501-16.xml
- http://www.heise.de/security/dienste/browsercheck/tests/java.shtml
- http://www.kb.cert.org/vuls/id/420222

> 📎 Source: http://marc.info/?l=bugtraq&m=110356286722875&w=2

#### 107. CVE-2004-0873 (N/A)

**CVE ID**: CVE-2004-0873
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:ichat, apple:ichat_av

**Description**:
Apple iChat AV 2.1, AV 2.0, and 1.0.1 allows remote attackers to execute arbitrary programs via a "link" that references the program.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17420
- http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17420

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html

#### 108. CVE-2004-0429 (N/A)

**CVE ID**: CVE-2004-0429
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:mac_os_x

**Description**:
Unknown vulnerability related to "the handling of large requests" in RAdmin for Apple Mac OS X 10.3.3 and Mac OS X 10.2.8 may allow attackers to have unknown impact via unknown attack vectors.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/May/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/May/msg00000.html
- http://marc.info/?l=bugtraq&m=108369640424244&w=2
- http://secunia.com/advisories/11539/
- http://securitytracker.com/id?1010045
- http://www.auscert.org.au/render.html?it=4070

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/May/msg00000.html

#### 109. CVE-2004-1398 (N/A)

**CVE ID**: CVE-2004-1398
**Severity**: N/A CVSS: 4.6
**Affected Products**: roxio:toast

**Description**:
Format string vulnerability in prelink.c in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via format string specifiers in the extension argument.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

**References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html
- http://marc.info/?l=bugtraq&m=110305083706943&w=2
- http://www.netragard.com/pdfs/research/apple-kext-tools-20060822.txt
- http://www.securityfocus.com/bid/11926
- http://www.securityfocus.com/bid/20031

> 📎 Source: http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html

#### 110. CVE-2004-1489 (N/A)

**CVE ID**: CVE-2004-1489
**Severity**: N/A CVSS: 2.6
**Affected Products**: opera:opera_browser

**Description**:
Opera 7.54 and earlier does not properly limit an applet's access to internal Java packages from Sun, which allows remote attackers to gain sensitive information, such as user names and the installation directory.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html.

**References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html
- http://www.gentoo.org/security/en/glsa/glsa-200502-17.xml
- http://www.opera.com/linux/changelogs/754u1/
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html
- http://www.gentoo.org/security/en/glsa/glsa-200502-17.xml

> 📎 Source: http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html

#### 111. CVE-2004-1753 (N/A)

**CVE ID**: CVE-2004-1753
**Severity**: N/A CVSS: 2.6
**Affected Products**: mozilla:mozilla, mozilla:firefox, netscape:navigator

**Description**:
The Apple Java plugin, as used in Netscape 7.1 and 7.2, Mozilla 1.7.2, and Firefox 0.9.3 on MacOS X 10.3.5, when tabbed browsing is enabled, does not properly handle SetWindow(NULL) calls, which allows Java applets from one tab to draw to other tabs and facilitates phishing attacks that spoof tabs.

**Mitigation**:
Apply patch from vendor. Monitor http://bugzilla.mozilla.org/show_bug.cgi?id=162134.

**References**:
- http://bugzilla.mozilla.org/show_bug.cgi?id=162134
- http://secunia.com/advisories/12392
- http://www.securityfocus.com/archive/1/373080
- http://www.securityfocus.com/archive/1/373232
- http://www.securityfocus.com/archive/1/373309

> 📎 Source: http://bugzilla.mozilla.org/show_bug.cgi?id=162134

#### 112. CVE-2004-2280 (N/A)

**CVE ID**: CVE-2004-2280
**Severity**: N/A CVSS: 5.0
**Affected Products**: ibm:lotus_notes

**Description**:
Buffer overflow in IBM Lotus Notes 6.5.x before 6.5.3 and 6.0.x before 6.0.5 allows remote attackers to cause a denial of service (crash) via unknown vectors related to Java applets, as identified by KSPR62F4KN.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**References**:
- http://secunia.com/advisories/12046
- http://www-1.ibm.com/support/docview.wss?rs=475&context=SSKTWP&q1=Java&uid=swg21173910&loc=en_US&cs=utf-8&lang=en
- http://www.osvdb.org/8418
- http://www.securityfocus.com/bid/10704
- http://secunia.com/advisories/12046

> 📎 Source: http://secunia.com/advisories/12046

#### 113. CVE-2004-2281 (N/A)

**CVE ID**: CVE-2004-2281
**Severity**: N/A CVSS: 10.0
**Affected Products**: ibm:lotus_notes

**Description**:
Multiple unknown vulnerabilities in IBM Lotus Notes 6.5.x before 6.5.4 and 6.0.x before 6.0.5 have unknown impact and attack vectors, related to Java applets, as identified by (1) KSPR5YS6GR and (2) KSPR62F4D3.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**References**:
- http://secunia.com/advisories/12046
- http://www-1.ibm.com/support/docview.wss?rs=475&context=SSKTWP&q1=Java&uid=swg21173910&loc=en_US&cs=utf-8&lang=en
- http://www.osvdb.org/8416
- http://www.osvdb.org/8417
- http://www.securityfocus.com/bid/10704

> 📎 Source: http://secunia.com/advisories/12046

#### 114. CVE-2004-2359 (N/A)

**CVE ID**: CVE-2004-2359
**Severity**: N/A CVSS: 10.0
**Affected Products**: dell:truemobile_1300_wlan_mini-pci_card_util_trayapplet

**Description**:
Dell TrueMobile 1300 WLAN Mini-PCI Card Util TrayApplet 3.10.39.0 does not properly drop SYSTEM privileges when started from the systray applet, which allows local users to gain privileges by accessing the Help functionality.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html.

**References**:
- http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html
- http://secunia.com/advisories/10949
- http://securitytracker.com/id?1009174
- http://www.securityfocus.com/bid/9714
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15285

> 📎 Source: http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html

#### 115. CVE-2004-2367 (N/A)

**CVE ID**: CVE-2004-2367
**Severity**: N/A CVSS: 5.0
**Affected Products**: texas_imperial_software:wftpd_pro, texas_imperial_software:wftpd

**Description**:
The Control Panel applet in WFTPD and WFTPD Pro 3.21 R1 and R2 allows remote authenticated users to cause a denial of service (crash) via a long FTP command.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/11160/.

**References**:
- http://secunia.com/advisories/11160/
- http://www.securiteam.com/windowsntfocus/5JP0B20CAY.html
- http://www.securityfocus.com/bid/9908
- http://www.wftpd.com/bug_gpf.htm
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15510

> 📎 Source: http://secunia.com/advisories/11160/

#### 116. CVE-2004-0926 (N/A)

**CVE ID**: CVE-2004-0926
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x, easy_software_products:cups

**Description**:
Heap-based buffer overflow in Apple QuickTime on Mac OS 10.2.8 through 10.3.5 may allow remote attackers to execute arbitrary code via a certain BMP image.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html

#### 117. CVE-2004-0962 (N/A)

**CVE ID**: CVE-2004-0962
**Severity**: N/A CVSS: 10.0
**Affected Products**: apple:apple_remote_desktop

**Description**:
Apple Remote Desktop Client 1.2.4 executes a GUI application as root when it is started by an Apple Remote Desktop Administrator application, which allows remote authenticated users to execute arbitrary code when loginwindow is active via Fast User Switching.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html

#### 118. CVE-2004-0988 (N/A)

**CVE ID**: CVE-2004-0988
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:quicktime

**Description**:
Integer overflow on Apple QuickTime before 6.5.2, when running on Windows systems, allows remote attackers to cause a denial of service (memory consumption) via certain inputs that cause a large memory operation.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html

#### 119. CVE-2004-1029 (N/A)

**CVE ID**: CVE-2004-1029
**Severity**: N/A CVSS: 9.3
**Affected Products**: hp:java_sdk-rte, sun:jre, conectiva:linux, gentoo:linux, symantec:gateway_security_5400

**Description**:
The Sun Java Plugin capability in Java 2 Runtime Environment (JRE) 1.4.2_01, 1.4.2_04, and possibly earlier versions, does not properly restrict access between Javascript and Java applets during data transfer, which allows remote attackers to load unsafe classes and execute arbitrary code by using the reflection API to access private Java packages.

**Mitigation**:
Apply patch from vendor. Monitor http://jouko.iki.fi/adv/javaplugin.html.

**References**:
- http://jouko.iki.fi/adv/javaplugin.html
- http://lists.apple.com/archives/security-announce/2005/Feb/msg00000.html
- http://rpmfind.net/linux/RPM/suse/updates/9.3/i386/rpm/i586/java-1_4_2-sun-src-1.4.2.08-0.1.i586.html
- http://secunia.com/advisories/13271
- http://secunia.com/advisories/29035

> 📎 Source: http://jouko.iki.fi/adv/javaplugin.html

#### 120. CVE-2005-0043 (N/A)

**CVE ID**: CVE-2005-0043
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:itunes

**Description**:
Buffer overflow in Apple iTunes 4.7 allows remote attackers to execute arbitrary code via a long URL in (1) .m3u or (2) .pls playlist files.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html
- http://secunia.com/advisories/13804
- http://securitytracker.com/id?1012839
- http://www.idefense.com/application/poi/display?id=180&type=vulnerabilities
- http://www.kb.cert.org/vuls/id/377368

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html

#### 121. CVE-2005-0289 (N/A)

**CVE ID**: CVE-2005-0289
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:airport_extreme, apple:airport_express

**Description**:
Apple AirPort Express prior to 6.1.1 and Extreme prior to 5.5.1, configured as a Wireless Data Service (WDS), allows remote attackers to cause a denial of service (device freeze) by connecting to UDP port 161 and before link-state change occurs.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html.

**References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html
- http://marc.info/?l=bugtraq&m=110582124528867&w=2
- http://secunia.com/advisories/13753
- http://www.securityfocus.com/bid/12152
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18865

> 📎 Source: http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html

#### 122. CVE-2005-0340 (N/A)

**CVE ID**: CVE-2005-0340
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:afp_server

**Description**:
Integer signedness error in Apple File Service (AFP Server) allows remote attackers to cause a denial of service (application crash) via a negative UAM string length in a FPLoginExt packet.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://marc.info/?l=bugtraq&m=110791369419784&w=2
- http://www.securityfocus.com/bid/12478
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19263
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

#### 123. CVE-2005-0341 (N/A)

**CVE ID**: CVE-2005-0341
**Severity**: N/A CVSS: 4.3
**Affected Products**: apple:safari

**Description**:
Apple Safari 1.2.4 does not obey the Content-type field in the HTTP header and renders text as HTML, which allows remote attackers to inject arbitrary web script or HTML and perform cross-site scripting (XSS) attacks.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110756965213819&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=110756965213819&w=2
- http://securitytracker.com/id?1013087
- http://tigger.uic.edu/~jrockw2/safari_20050204.txt
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19227
- http://marc.info/?l=bugtraq&m=110756965213819&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=110756965213819&w=2

#### 124. CVE-2005-0976 (N/A)

**CVE ID**: CVE-2005-0976
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari, omnigroup:omniweb, hmdt:shiira

**Description**:
AppleWebKit (WebCore and WebKit), as used in multiple products such as Safari 1.2 and OmniGroup OmniWeb 5.1, allows remote attackers to read arbitrary files via the XMLHttpRequest Javascript component, as demonstrated using automatically mounted disk images and file:// URLs.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://remahl.se/david/vuln/001/
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://remahl.se/david/vuln/001/

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html

#### 125. CVE-2005-1331 (N/A)

**CVE ID**: CVE-2005-1331
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x, apple:applescript

**Description**:
The AppleScript Editor in Mac OS X 10.3.9 does not properly display script code for an applescript: URI, which can result in code that is different than the actual code that would be run, which could allow remote attackers to trick users into executing malicious code via certain URI characters such as NULL, control characters, and homographs.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/010/
- http://secunia.com/advisories/15227
- http://www.securityfocus.com/bid/13480
- http://www.vupen.com/english/advisories/2005/0455

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 126. CVE-2005-1337 (N/A)

**CVE ID**: CVE-2005-1337
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Apple Help Viewer 2.0.7 and 3.0.0 in Mac OS X 10.3.9 allows remote attackers to read and execute arbitrary scrpts with less restrictive privileges via a help:// URI.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/004/
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/004/

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 127. CVE-2005-1341 (N/A)

**CVE ID**: CVE-2005-1341
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:terminal, apple:mac_os_x_server, apple:mac_os_x

**Description**:
Apple Terminal 1.4.4 allows attackers to execute arbitrary commands via terminal escape sequences.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/012/
- http://secunia.com/advisories/15227
- http://securitytracker.com/id?1013882
- http://www.kb.cert.org/vuls/id/994510

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 128. CVE-2005-1342 (N/A)

**CVE ID**: CVE-2005-1342
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:terminal, apple:mac_os_x

**Description**:
The x-man-page: URI handler for Apple Terminal 1.4.4 in Mac OS X 10.3.9 does not cleanse terminal escape sequences, which allows remote attackers to execute arbitrary commands.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://remahl.se/david/vuln/011/
- http://secunia.com/advisories/15227
- http://www.kb.cert.org/vuls/id/356070
- http://www.osvdb.org/16084

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

#### 129. CVE-2005-1579 (N/A)

**CVE ID**: CVE-2005-1579
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:quicktime

**Description**:
Apple QuickTime Player 7.0 on Mac OS X 10.4 allows remote attackers to obtain sensitive information via a .mov file with a Quartz Composer composition (.qtz) file that uses certain patches to read local information, then other patches to send the information to the attacker.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html
- http://docs.info.apple.com/article.html?artnum=301714
- http://lists.apple.com/archives/quartzcomposer-dev/2005/May/msg00250.html
- http://lists.apple.com/archives/quartzcomposer-dev/2005/May/msg00263.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00006.html

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html

#### 130. CVE-2005-1193 (N/A)

**CVE ID**: CVE-2005-1193
**Severity**: N/A CVSS: 7.5
**Affected Products**: phpbb_group:phpbb

**Description**:
The bbencode_second_pass and make_clickable functions in bbcode.php for phpBB before 2.0.15, as used in viewtopic.php, privmsg.php, and other scripts, allow remote attackers to execute arbitrary script via a BBcode tag with a (1) javascript:, (2) applet:, (3) about:, (4) activex:, (5) chrome:, or (6) script: URI scheme, as demonstrated using the URL tag.

**Mitigation**:
Apply patch from vendor. Monitor http://castlecops.com/t123194-.html.

**References**:
- http://castlecops.com/t123194-.html
- http://marc.info/?l=full-disclosure&m=111552510000088&w=2
- http://seclists.org/lists/bugtraq/2005/May/0098.html
- http://secunia.com/advisories/15298
- http://securitytracker.com/id?1013918

> 📎 Source: http://castlecops.com/t123194-.html

#### 131. CVE-2005-1248 (N/A)

**CVE ID**: CVE-2005-1248
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:itunes

**Description**:
Buffer overflow in Apple iTunes before 4.8 allows remote attackers to execute arbitrary code via a crafted MPEG4 file.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301596.

**References**:
- http://docs.info.apple.com/article.html?artnum=301596
- http://lists.apple.com/archives/security-announce/2005/May/msg00003.html
- http://secunia.com/advisories/15310
- http://securitytracker.com/id?1013927
- http://www.ngssoftware.com/advisories/itunes.txt

> 📎 Source: http://docs.info.apple.com/article.html?artnum=301596

#### 132. CVE-2005-1472 (N/A)

**CVE ID**: CVE-2005-1472
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:mac_os_x

**Description**:
Certain system calls in Apple Mac OS X 10.4.1 do not properly enforce the permissions of certain directories without the POSIX read bit set, but with the execute bits set for group or other, which allows local users to list files in otherwise restricted directories.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 133. CVE-2005-1408 (N/A)

**CVE ID**: CVE-2005-1408
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:keynote

**Description**:
Apple Keynote 2.0 and 2.0.1 allows remote attackers to read arbitrary files via the keynote: URI handler in a crafted Keynote presentation.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00005.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00005.html
- http://remahl.se/david/vuln/016/
- http://secunia.com/advisories/15508
- http://securitytracker.com/id?1014053
- http://lists.apple.com/archives/security-announce/2005/May/msg00005.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00005.html

#### 134. CVE-2005-1723 (N/A)

**CVE ID**: CVE-2005-1723
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server

**Description**:
LaunchServices in Apple Mac OS X 10.4.x up to 10.4.1 does not properly mark file extensions and MIME types as unsafe if an Apple Uniform Type Identifier (UTI) is not created when the type is added to the database of unsafe types, which could allow attackers to bypass intended restrictions.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014141
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014141

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 135. CVE-2005-1724 (N/A)

**CVE ID**: CVE-2005-1724
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server

**Description**:
NFS on Apple Mac OS X 10.4.x up to 10.4.1 does not properly obey the -network or -mask flags for a filesystem and exports it to everyone, which allows remote attackers to bypass intended access restrictions.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014142
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014142

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 136. CVE-2005-1725 (N/A)

**CVE ID**: CVE-2005-1725
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:mac_os_x_server

**Description**:
launchd 106 in Apple Mac OS X 10.4.x up to 10.4.1 allows local users to overwrite arbitrary files via a symlink attack on the socket file in an insecure temporary directory.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://marc.info/?l=bugtraq&m=111833509424379&w=2
- http://www.suresec.org/advisories/adv3.pdf
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://marc.info/?l=bugtraq&m=111833509424379&w=2

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 137. CVE-2005-1727 (N/A)

**CVE ID**: CVE-2005-1727
**Severity**: N/A CVSS: 3.7
**Affected Products**: apple:mac_os_x_server

**Description**:
Apple Mac OS X 10.4.x up to 10.4.1 sets insecure world- and group-writable permissions for the (1) system cache folder and (2) Dashboard system widgets, which allows local users to conduct unauthorized file operations via "file race conditions."

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 138. CVE-2005-1728 (N/A)

**CVE ID**: CVE-2005-1728
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:mac_os_x

**Description**:
MCX Client for Apple Mac OS X 10.4.x up to 10.4.1 insecurely logs Portable Home Directory credentials, which allows local users to obtain the credentials.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014148
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014148

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

#### 139. CVE-2005-1473 (N/A)

**CVE ID**: CVE-2005-1473
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:mac_os_x

**Description**:
SecurityAgent in Apple Mac OS X 10.4.1 allows attackers with physical access to bypass the locked screensaver and launch background applications by opening a URL from a text input field.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 140. CVE-2005-1474 (N/A)

**CVE ID**: CVE-2005-1474
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Dashboard in Apple Mac OS X 10.4.1 allows remote attackers to install widgets via Safari without prompting the user, a different vulnerability than CVE-2005-1933.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://www.securityfocus.com/bid/13694
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://www.securityfocus.com/bid/13694

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

#### 141. CVE-2005-1933 (N/A)

**CVE ID**: CVE-2005-1933
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x

**Description**:
Dashboard in Apple Mac OS X Tiger 10.4 allows attackers to execute arbitrary commands by overriding the behavior of system widgets via a user widget with the same bundle identifier (CFBundleIdentifier), a different vulnerability than CVE-2005-1474.

**Mitigation**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/983429.

**References**:
- http://www.kb.cert.org/vuls/id/983429
- http://www1.cs.columbia.edu/~aaron/files/widgets/
- http://www.kb.cert.org/vuls/id/983429
- http://www1.cs.columbia.edu/~aaron/files/widgets/

> 📎 Source: http://www.kb.cert.org/vuls/id/983429

#### 142. CVE-2005-2195 (N/A)

**CVE ID**: CVE-2005-2195
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:darwin_streaming_server

**Description**:
Apple Darwin Streaming Server 5.5 and earlier allows remote attackers to cause a denial of service (application crash) via a URL with a filename containing a .cgi extension and an MS-DOS device name such as AUX, CON, PRN, COM1, or LPT1, a different vulnerability than CVE-2003-0421 and CVE-2003-0502.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112126999514361&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=112126999514361&w=2
- http://secunia.com/advisories/16056
- http://securitytracker.com/id?1014474
- http://secway.org/Advisory/AD20050713.txt
- http://marc.info/?l=bugtraq&m=112126999514361&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=112126999514361&w=2

#### 143. CVE-2005-2196 (N/A)

**CVE ID**: CVE-2005-2196
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:airport_card

**Description**:
The Apple AirPort card uses a default WEP key when not connected to a known or trusted network, which can cause it to automatically connect to a malicious network.

**Mitigation**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1014522.

**References**:
- http://securitytracker.com/id?1014522
- http://www.securityfocus.com/bid/14321
- http://securitytracker.com/id?1014522
- http://www.securityfocus.com/bid/14321

> 📎 Source: http://securitytracker.com/id?1014522

#### 144. CVE-2005-2594 (N/A)

**CVE ID**: CVE-2005-2594
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
Apple Safari 1.3 (132) on Mac OS X 1.3.9 allows remote attackers to cause a denial of service (crash) via certain Javascript, possibly involving a function that defines a handler for itself within the function body.

**Mitigation**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/407702.

**References**:
- http://www.securityfocus.com/archive/1/407702
- http://www.securityfocus.com/bid/14528
- http://www.securityfocus.com/archive/1/407702
- http://www.securityfocus.com/bid/14528

> 📎 Source: http://www.securityfocus.com/archive/1/407702

#### 145. CVE-2005-3018 (N/A)

**CVE ID**: CVE-2005-3018
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
Apple Safari allows remote attackers to cause a denial of service (application crash) via a crafted data:// URL.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112715234411672&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=112715234411672&w=2
- http://secunia.com/advisories/16875/
- http://www.osvdb.org/19569
- http://www.securityfocus.com/bid/14868
- https://exchange.xforce.ibmcloud.com/vulnerabilities/22331

> 📎 Source: http://marc.info/?l=bugtraq&m=112715234411672&w=2

#### 146. CVE-2005-2744 (N/A)

**CVE ID**: CVE-2005-2744
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Buffer overflow in QuickDraw Manager for Apple OS X 10.3.9 and 10.4.2, as used by applications such as Safari, Mail, and Finder, allows remote attackers to execute arbitrary code via a crafted PICT file.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://securitytracker.com/alerts/2005/Sep/1014961.html
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 147. CVE-2005-2747 (N/A)

**CVE ID**: CVE-2005-2747
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Buffer overflow in ImageIO for Apple Mac OS X 10.4.2, as used by applications such as WebCore and Safari, allows remote attackers to execute arbitrary code via a crafted GIF file.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://securitytracker.com/alerts/2005/Sep/1014958.html
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 148. CVE-2005-2748 (N/A)

**CVE ID**: CVE-2005-2748
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
The malloc function in the libSystem library in Apple Mac OS X 10.3.9 and 10.4.2 allows local users to overwrite arbitrary files by setting the MallocLogFile environment variable to the target file before running a setuid application.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://www.suresec.org/advisories/adv7.pdf

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 149. CVE-2005-2524 (N/A)

**CVE ID**: CVE-2005-2524
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari, apple:mac_os_x_server, apple:mac_os_x

**Description**:
Safari after 2.0 in Apple Mac OS X 10.3.9 allows remote attackers to bypass domain restrictions via crafted web archives that cause Safari to render them as if they came from a different site.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 150. CVE-2005-2741 (N/A)

**CVE ID**: CVE-2005-2741
**Severity**: N/A CVSS: 7.2
**Affected Products**: perry_kiehtreiber:securityd, apple:mac_os_x_server, apple:mac_os_x

**Description**:
Authorization Services in securityd for Apple Mac OS X 10.3.9 allows local users to gain privileges by granting themselves certain rights that should be restricted to administrators.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 151. CVE-2005-2742 (N/A)

**CVE ID**: CVE-2005-2742
**Severity**: N/A CVSS: 4.6
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
SecurityAgent in Apple Mac OS X 10.4.2, under certain circumstances, can cause the "Switch User..." button to appear even though the "Enable fast user switching" setting is disabled, which can allow attackers with physical access to gain access to the desktop and bypass the "Require password to wake this computer from sleep or screen saver" setting.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 152. CVE-2005-2743 (N/A)

**CVE ID**: CVE-2005-2743
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x, apple:quicktime

**Description**:
The Java extensions for QuickTime 6.52 and earlier in Apple Mac OS X 10.3.9 allow untrusted applets to call arbitrary functions in system libraries, which allows remote attackers to execute arbitrary code.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 153. CVE-2005-2745 (N/A)

**CVE ID**: CVE-2005-2745
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9, when using Kerberos 5 for SMTP authentication, can include uninitialized memory in a message, which might allow remote attackers to obtain sensitive information.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 154. CVE-2005-2746 (N/A)

**CVE ID**: CVE-2005-2746
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9 and 10.4.2 includes message contents when using auto-reply rules, which could cause Mail.app to include decrypted message contents for encrypted messages.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html
- http://secunia.com/advisories/16920/
- http://www.auscert.org.au/5509
- http://www.ciac.org/ciac/bulletins/p-312.shtml
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html

#### 155. CVE-2005-2753 (N/A)

**CVE ID**: CVE-2005-2753
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file that causes a sign extension of the length element in a Pascal style string.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**References**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-io1-adv.txt
- http://secunia.com/advisories/17428
- http://securitytracker.com/id?1015152
- http://www.osvdb.org/20475

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302772

#### 156. CVE-2005-2754 (N/A)

**CVE ID**: CVE-2005-2754
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file with "Improper movie attributes."

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**References**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-io2-adv.txt
- http://secunia.com/advisories/17428
- http://securitytracker.com/id?1015152
- http://www.osvdb.org/20476

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302772

#### 157. CVE-2005-2755 (N/A)

**CVE ID**: CVE-2005-2755
**Severity**: N/A CVSS: 2.6
**Affected Products**: apple:quicktime

**Description**:
Apple QuickTime Player before 7.0.3 allows user-assisted attackers to cause a denial of service (crash) via a crafted file with a missing movie attribute, which leads to a null dereference.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-mov-dos-adv.txt
- http://secunia.com/advisories/17428
- http://securityreason.com/securityalert/145

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html

#### 158. CVE-2005-2756 (N/A)

**CVE ID**: CVE-2005-2756
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Apple QuickTime before 7.0.3 allows user-assisted attackers to overwrite memory and execute arbitrary code via a crafted PICT file that triggers an overflow during expansion.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**References**:
- http://docs.info.apple.com/article.html?artnum=302772
- http://pb.specialised.info/all/adv/quicktime-pict-adv.txt
- http://secunia.com/advisories/17428
- http://securityreason.com/securityalert/144
- http://securitytracker.com/id?1015152

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302772

#### 159. CVE-2005-3897 (N/A)

**CVE ID**: CVE-2005-3897
**Severity**: N/A CVSS: 7.8
**Affected Products**: apple:safari

**Description**:
Apple Safari 2.0.2 allows remote attackers to cause a denial of service (system slowdown) via a Javascript BODY onload event that calls the window function.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=113278010907401&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=113278010907401&w=2
- http://marc.info/?l=bugtraq&m=113278010907401&w=2

> 📎 Source: http://marc.info/?l=bugtraq&m=113278010907401&w=2

#### 160. CVE-2005-3907 (N/A)

**CVE ID**: CVE-2005-3907
**Severity**: N/A CVSS: 7.5
**Affected Products**: sun:jdk, sun:jre

**Description**:
Unspecified vulnerability in Java Runtime Environment in Java JDK and JRE 5.0 Update 3 and earlier allows remote attackers to escape the Java sandbox and access arbitrary files or execute arbitrary applications via unknown attack vectors involving untrusted Java applets.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html.

**References**:
- http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html
- http://secunia.com/advisories/17748
- http://secunia.com/advisories/17847
- http://secunia.com/advisories/18092
- http://securitytracker.com/id?1015282

> 📎 Source: http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html

#### 161. CVE-2005-3946 (N/A)

**CVE ID**: CVE-2005-3946
**Severity**: N/A CVSS: 5.0
**Affected Products**: opera:opera_browser

**Description**:
Opera 8.50 allows remote attackers to cause a denial of service (crash) via a Java applet with a large string argument to the removeMember JNI method for the com.opera.JSObject class.

**Mitigation**:
Apply patch from vendor. Monitor http://www.illegalaccess.org/exploit/opera85/OperaApplet.html.

**References**:
- http://www.illegalaccess.org/exploit/opera85/OperaApplet.html
- http://www.securityfocus.com/archive/1/418201/100/0/threaded
- http://www.securityfocus.com/archive/1/418274/100/0/threaded
- http://www.securityfocus.com/bid/15648
- http://www.illegalaccess.org/exploit/opera85/OperaApplet.html

> 📎 Source: http://www.illegalaccess.org/exploit/opera85/OperaApplet.html

#### 162. CVE-2005-4092 (N/A)

**CVE ID**: CVE-2005-4092
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:itunes, apple:quicktime

**Description**:
Multiple heap-based buffer overflows in QuickTime.qts in Apple QuickTime Player 7.0.3 and iTunes 6.0.1 (3) and earlier allow remote attackers to cause a denial of service (crash) and execute arbitrary code via a .mov file with (1) a Movie Resource atom with a large size value, or (2) an stsd atom with a modified Sample Description Table size value, and possibly other vectors involving media files.  NOTE: item 1 was originally identified by CVE-2005-4127 for a pre-patch announcement, and item 2 was originally identified by CVE-2005-4128 for a pre-patch announcement.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**References**:
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18149
- http://secunia.com/advisories/18370
- http://security-protocols.com/advisory/sp-x21-advisory.txt
- http://securityreason.com/securityalert/334

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303101

#### 163. CVE-2005-4197 (N/A)

**CVE ID**: CVE-2005-4197
**Severity**: N/A CVSS: 7.5
**Affected Products**: nortel:ssl_vpn

**Description**:
tunnelform.yaws in Nortel SSL VPN 4.2.1.6 allows remote attackers to execute arbitrary commands via a link in the a parameter, which is executed with extra privileges in a cryptographically signed Java Applet.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17974.

**References**:
- http://secunia.com/advisories/17974
- http://securitytracker.com/id?1015341
- http://www.sec-consult.com/247.html
- http://www.securityfocus.com/archive/1/419263/100/0/threaded
- http://www.securityfocus.com/bid/15798

> 📎 Source: http://secunia.com/advisories/17974

#### 164. CVE-2005-4217 (N/A)

**CVE ID**: CVE-2005-4217
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server

**Description**:
Perl in Apple Mac OS X Server 10.3.9 does not properly drop privileges when using the "$<" variable to set uid, which allows attackers to gain privileges.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**References**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00000.html
- http://secunia.com/advisories/17922
- http://secunia.com/advisories/19064
- http://www.osvdb.org/21800

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303382

#### 165. CVE-2005-4504 (N/A)

**CVE ID**: CVE-2005-4504
**Severity**: N/A CVSS: 7.8
**Affected Products**: apple:safari, apple:textedit, apple:mac_os_x_server, apple:mac_os_x

**Description**:
The khtml::RenderTableSection::ensureRows function in KHTMLParser in Apple Mac OS X 10.4.3 and earlier, as used by Safari and TextEdit, allows remote attackers to cause a denial of service (memory consumption and application crash) via HTML files with a large ROWSPAN attribute in a TD tag.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**References**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://docs.info.apple.com/jarticle.html?artnum=303382-en
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00000.html
- http://secunia.com/advisories/18220
- http://secunia.com/advisories/19064

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303382

#### 166. CVE-2005-2194 (N/A)

**CVE ID**: CVE-2005-2194
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x

**Description**:
Unspecified vulnerability in the Apple Mac OS X kernel before 10.4.2 allows remote attackers to cause a denial of service (kernel panic) via a crafted TCP packet, possibly related to source routing or loose source routing.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301948.

**References**:
- http://docs.info.apple.com/article.html?artnum=301948
- http://lists.apple.com/archives/Security-announce/2005/Jul/msg00000.html
- http://secunia.com/advisories/16047
- http://securitytracker.com/id?1014464
- http://www.osvdb.org/17880

> 📎 Source: http://docs.info.apple.com/article.html?artnum=301948

#### 167. CVE-2005-2340 (N/A)

**CVE ID**: CVE-2005-2340
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a crafted (1) QuickTime Image File (QTIF), (2) PICT, or (3) JPEG format image with a long data field.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0398.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0402.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html

#### 168. CVE-2005-2527 (N/A)

**CVE ID**: CVE-2005-2527
**Severity**: N/A CVSS: 1.2
**Affected Products**: sun:java

**Description**:
Race condition in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to corrupt files or create arbitrary files via unspecified attack vectors related to a temporary directory, possibly due to a symlink attack.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**References**:
- http://docs.info.apple.com/article.html?artnum=302266
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.securityfocus.com/bid/14825

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302266

#### 169. CVE-2005-2529 (N/A)

**CVE ID**: CVE-2005-2529
**Severity**: N/A CVSS: 10.0
**Affected Products**: sun:java

**Description**:
Unspecified vulnerability in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to gain privileges via unspecified attack vectors relating to "the utility used to update Java shared archives."

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**References**:
- http://docs.info.apple.com/article.html?artnum=302266
- http://lists.apple.com/archives/Security-announce/2005/Sep/msg00000.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.vupen.com/english/advisories/2005/1734

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302266

#### 170. CVE-2005-2530 (N/A)

**CVE ID**: CVE-2005-2530
**Severity**: N/A CVSS: 10.0
**Affected Products**: sun:java

**Description**:
Unspecified vulnerability in Java 1.3.1 before 1.3.1_16 on Apple Mac OS X allows an untrusted applet to gain privileges, related to "Mac OS X specific extensions."

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**References**:
- http://docs.info.apple.com/article.html?artnum=302265
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.securityfocus.com/bid/14826

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302265

#### 171. CVE-2005-2738 (N/A)

**CVE ID**: CVE-2005-2738
**Severity**: N/A CVSS: 5.0
**Affected Products**: sun:java

**Description**:
Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X does not prevent multiple programs from opening the same port as a Java ServerSocket, which allows local users to operate a Java program that intercepts network data intended for the ServerSocket of a different Java program.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**References**:
- http://docs.info.apple.com/article.html?artnum=302265
- http://lists.apple.com/archives/security-announce/2005/Sep/msg00001.html
- http://secunia.com/advisories/16808
- http://www.ciac.org/ciac/bulletins/p-306.shtml
- http://www.osvdb.org/19397

> 📎 Source: http://docs.info.apple.com/article.html?artnum=302265

#### 172. CVE-2005-3707 (N/A)

**CVE ID**: CVE-2005-3707
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.kb.cert.org/vuls/id/115729

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html

#### 173. CVE-2005-3708 (N/A)

**CVE ID**: CVE-2005-3708
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**References**:
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.osvdb.org/22336
- http://www.securityfocus.com/bid/16202

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303101

#### 174. CVE-2005-3709 (N/A)

**CVE ID**: CVE-2005-3709
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Integer underflow in Apple Quicktime before 7.0.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via the Color Map Entry Size in a TGA image file.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015464
- http://www.osvdb.org/22336

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html

#### 175. CVE-2005-3710 (N/A)

**CVE ID**: CVE-2005-3710
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified image height and width (ImageWidth) tags.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securityreason.com/securityalert/347
- http://securitytracker.com/id?1015465

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html

#### 176. CVE-2005-3711 (N/A)

**CVE ID**: CVE-2005-3711
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified (1) "strips" (StripByteCounts) or (2) "bands" (StripOffsets) values.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securitytracker.com/id?1015465
- http://www.osvdb.org/22337

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html

#### 177. CVE-2005-3713 (N/A)

**CVE ID**: CVE-2005-3713
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:quicktime

**Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a GIF image file with a crafted Netscape Navigator Application Extension Block that modifies the heap in the Picture Modifier block.

**Mitigation**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html.

**References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html
- http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0402.html
- http://docs.info.apple.com/article.html?artnum=303101
- http://secunia.com/advisories/18370
- http://securityreason.com/securityalert/333

> 📎 Source: http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html

#### 178. CVE-2005-3714 (N/A)

**CVE ID**: CVE-2005-3714
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:airport_extreme, apple:airport_express

**Description**:
The network interface for Apple AirPort Express 6.x before Firmware Update 6.3, and AirPort Extreme 5.x before Firmware Update 5.7, allows remote attackers to cause a denial of service (unresponsive interface) via malformed packets.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html
- http://secunia.com/advisories/18319
- http://securitytracker.com/id?1015443
- http://www.osvdb.org/22244
- http://www.securityfocus.com/bid/16146

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html

#### 179. CVE-2005-4678 (N/A)

**CVE ID**: CVE-2005-4678
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
Apple Safari 2.0.2 (aka 416.12) allows remote attackers to spoof the URL in the status bar via the title in an image in a link to a trusted site within a form to the malicious site.  NOTE: the provenance of this information is unknown; the details are obtained solely from third party information.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17618.

**References**:
- http://secunia.com/advisories/17618
- http://secunia.com/advisories/17618

> 📎 Source: http://secunia.com/advisories/17618

#### 180. CVE-2005-4866 (N/A)

**CVE ID**: CVE-2005-4866
**Severity**: N/A CVSS: 6.8
**Affected Products**: ibm:db2_universal_database

**Description**:
Stack-based buffer overflow in JDBC Applet Server in IBM DB2 8.1 allows remote attackers to execute arbitrary by connecting and sending a long username, then disconnecting gracefully and reconnecting and sending a short username and an unexpected db2java.zip version, which causes a null terminator to be removed and leads to the overflow.

**Mitigation**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110495251101381&w=2.

**References**:
- http://marc.info/?l=bugtraq&m=110495251101381&w=2
- http://secunia.com/advisories/12733/
- http://www-1.ibm.com/support/docview.wss?uid=swg1IY61492
- http://www.nextgenss.com/advisories/db205012005D.txt
- http://www.securityfocus.com/bid/11401

> 📎 Source: http://marc.info/?l=bugtraq&m=110495251101381&w=2

#### 181. CVE-2006-0382 (N/A)

**CVE ID**: CVE-2006-0382
**Severity**: N/A CVSS: 2.1
**Affected Products**: apple:mac_os_x

**Description**:
Apple Mac OS X 10.4.5 and allows local users to cause a denial of service (crash) via an undocumented system call.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html
- http://secunia.com/advisories/18907
- http://securitytracker.com/id?1015634
- http://www.osvdb.org/23190
- http://www.securityfocus.com/bid/16654

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html

#### 182. CVE-2006-0848 (N/A)

**CVE ID**: CVE-2006-0848
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
The "Open 'safe' files after downloading" option in Safari on Apple Mac OS X allows remote user-assisted attackers to execute arbitrary commands by tricking a user into downloading a __MACOSX folder that contains metadata (resource fork) that invokes the Terminal, which automatically interprets the script using bash, as demonstrated using a ZIP file that contains a script with a safe file extension.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**References**:
- http://docs.info.apple.com/article.html?artnum=303382
- http://secunia.com/advisories/18963
- http://securitytracker.com/id?1015652
- http://www.frsirt.com/exploits/20060222.safari_safefiles_exec.pm.php
- http://www.heise.de/english/newsticker/news/69862

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303382

#### 183. CVE-2006-0396 (N/A)

**CVE ID**: CVE-2006-0396
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Buffer overflow in Mail in Apple Mac OS X 10.4 up to 10.4.5, when patched with Security Update 2006-001, allows remote attackers to execute arbitrary code via a long Real Name value in an e-mail attachment sent in AppleDouble format, which triggers the overflow when the user double-clicks on an attachment.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**References**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015762
- http://www.digitalmunition.com/DMA%5B2006-0313a%5D.txt

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303453

#### 184. CVE-2006-0397 (N/A)

**CVE ID**: CVE-2006-0397
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**References**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23869

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303453

#### 185. CVE-2006-0398 (N/A)

**CVE ID**: CVE-2006-0398
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**References**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23870

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303453

#### 186. CVE-2006-0399 (N/A)

**CVE ID**: CVE-2006-0399
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**References**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015760
- http://www.osvdb.org/23871

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303453

#### 187. CVE-2006-0400 (N/A)

**CVE ID**: CVE-2006-0400
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**Description**:
CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to bypass the same-origin policy and execute Javascript in other domains via unknown vectors involving "crafted archives."

**Mitigation**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**References**:
- http://docs.info.apple.com/article.html?artnum=303453
- http://lists.apple.com/archives/security-announce/2006/Mar/msg00001.html
- http://secunia.com/advisories/19129
- http://securitytracker.com/id?1015763
- http://www.osvdb.org/23873

> 📎 Source: http://docs.info.apple.com/article.html?artnum=303453

#### 188. CVE-2006-1249 (N/A)

**CVE ID**: CVE-2006-1249
**Severity**: N/A CVSS: 6.8
**Affected Products**: apple:itunes, apple:quicktime

**Description**:
Integer overflow in Apple QuickTime Player 7.0.3 and 7.0.4 and iTunes 6.0.1 and 6.0.2 allows remote attackers to execute arbitrary code via a FlashPix (FPX) image that contains a field that specifies a large number of blocks.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securitytracker.com/id?1016067
- http://www.eeye.com/html/research/upcoming/20060307b.html
- http://www.kb.cert.org/vuls/id/570689

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 189. CVE-2006-1552 (N/A)

**CVE ID**: CVE-2006-1552
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari, apple:mac_os_x_server, apple:mac_os_x, apple:imageio

**Description**:
Integer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to cause a denial of service (crash) via a crafted JPEG image with malformed JPEG metadata, as demonstrated using Safari, aka "Deja-Doom".

**Mitigation**:
Apply patch from vendor. Monitor http://drunkenblog.com/drunkenblog-archives/000760.html.

**References**:
- http://drunkenblog.com/drunkenblog-archives/000760.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20077
- http://www.osvdb.org/25597
- http://www.securityfocus.com/bid/17321

> 📎 Source: http://drunkenblog.com/drunkenblog-archives/000760.html

#### 190. CVE-2006-1986 (N/A)

**CVE ID**: CVE-2006-1986
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:safari

**Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via a large CELLSPACING attribute in a TABLE tag, which triggers an error in KWQListIteratorImpl::KWQListIteratorImpl.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**References**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-1.html
- http://www.osvdb.org/24823
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634

> 📎 Source: http://secunia.com/advisories/19686

#### 191. CVE-2006-1987 (N/A)

**CVE ID**: CVE-2006-1987
**Severity**: N/A CVSS: 7.5
**Affected Products**: apple:safari

**Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via an invalid FRAME tag, possibly due to (1) multiple SCROLLING attributes with no values, or (2) a SRC attribute with no value.  NOTE: due to lack of diagnosis by the researcher, it is unclear which vector is responsible.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**References**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-4.html
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634
- http://www.vupen.com/english/advisories/2006/1452

> 📎 Source: http://secunia.com/advisories/19686

#### 192. CVE-2006-1988 (N/A)

**CVE ID**: CVE-2006-1988
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
The WebTextRenderer(WebInternal) _CG_drawRun:style:geometry: function in Apple Safari 2.0.3 allows remote attackers to cause a denial of service (application crash) via an HTML LI tag with a large VALUE attribute (list item number), which triggers a null dereference in QPainter::drawText, probably due to a failed memory allocation that uses the VALUE.

**Mitigation**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**References**:
- http://secunia.com/advisories/19686
- http://security-protocols.com/poc/sp-x26-2.html
- http://www.osvdb.org/24823
- http://www.security-protocols.com/sp-x26-advisory.php
- http://www.securityfocus.com/bid/17634

> 📎 Source: http://secunia.com/advisories/19686

#### 193. CVE-2006-2019 (N/A)

**CVE ID**: CVE-2006-2019
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:safari

**Description**:
Apple Mac OS X Safari 2.0.3, 1.3.1, and possibly other versions allows remote attackers to cause a denial of service (CPU consumption and crash) via a TD element with a large number in the rowspan attribute.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html.

**References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html
- http://secunia.com/advisories/19763
- http://securitytracker.com/id?1015982
- http://www.securityfocus.com/archive/1/431874/100/0/threaded
- http://www.securityfocus.com/archive/1/431944/100/0/threaded

> 📎 Source: http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html

#### 194. CVE-2006-2277 (N/A)

**CVE ID**: CVE-2006-2277
**Severity**: N/A CVSS: 5.0
**Affected Products**: apple:mac_os_x

**Description**:
Multiple Apple Mac OS X 10.4 applications might allow context-dependent attackers to cause a denial of service (application crash) via a crafted OpenEXR (.exr) image file, which triggers the crash when opening a folder using Finder, displaying the image in Safari, or using Preview to open the file.

**Mitigation**:
Apply patch from vendor. Monitor http://www.osvdb.org/27780.

**References**:
- http://www.osvdb.org/27780
- http://www.securityfocus.com/archive/1/432587/100/0/threaded
- http://www.securityfocus.com/bid/17768
- https://github.com/openexr/openexr/issues/564
- http://www.osvdb.org/27780

> 📎 Source: http://www.osvdb.org/27780

#### 195. CVE-2006-1453 (N/A)

**CVE ID**: CVE-2006-1453
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Stack-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file containing malformed font information.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20069
- http://secunia.com/advisories/20077
- http://securityreason.com/securityalert/887

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 196. CVE-2006-1454 (N/A)

**CVE ID**: CVE-2006-1454
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file with malformed image data.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.apple.com/archives/security-announce/2006/May/msg00003.html
- http://secunia.com/advisories/20069
- http://secunia.com/advisories/20077
- http://securityreason.com/securityalert/887

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 197. CVE-2006-1458 (N/A)

**CVE ID**: CVE-2006-1458
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Integer overflow in Apple QuickTime Player before 7.1 allows remote attackers to execute arbitrary code via a crafted JPEG image.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securitytracker.com/id?1016067
- http://www.kb.cert.org/vuls/id/289705
- http://www.securityfocus.com/bid/17953

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 198. CVE-2006-1459 (N/A)

**CVE ID**: CVE-2006-1459
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to cause a denial of service or execute arbitrary code via a crafted QuickTime movie (.MOV).

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067
- http://www.securityfocus.com/archive/1/433831/100/0/threaded

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 199. CVE-2006-1460 (N/A)

**CVE ID**: CVE-2006-1460
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime movie (.MOV), as demonstrated via a large size for a udta Atom.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://lists.grok.org.uk/pipermail/full-disclosure/2006-May/045987.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html

#### 200. CVE-2006-1461 (N/A)

**CVE ID**: CVE-2006-1461
**Severity**: N/A CVSS: 5.1
**Affected Products**: apple:quicktime

**Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime Flash (SWF) file.

**Mitigation**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**References**:
- http://lists.apple.com/archives/security-announce/2006/May/msg00002.html
- http://secunia.com/advisories/20069
- http://securityreason.com/securityalert/887
- http://securitytracker.com/id?1016067
- http://www.securityfocus.com/archive/1/433831/100/0/threaded

> 📎 Source: http://lists.apple.com/archives/security-announce/2006/May/msg00002.html



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
