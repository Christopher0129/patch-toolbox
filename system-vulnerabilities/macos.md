# Macos 系统漏洞知识库 | Macos System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 425**

> 技术细节（漏洞描述、补丁信息等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, patch info) remain in original language for accuracy; structural text is bilingual.

---

#### 1. CVE-1999-0142

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:java, netscape:navigator

**漏洞描述 / Description**:
The Java Applet Security Manager implementation in Netscape Navigator 2.0 and Java Developer's Kit 1.0 allows an applet to connect to arbitrary hosts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0142.

**参考链接 / References**:
- N/A

---

#### 2. CVE-1999-0141

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: netscape:navigator

**漏洞描述 / Description**:
Java Bytecode Verifier allows malicious applets to execute arbitrary commands as the user of the applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134.

**参考链接 / References**:
- N/A

---

#### 3. CVE-1999-1262

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Java in Netscape 4.5 does not properly restrict applets from connecting to other hosts besides the one from which the applet was loaded, which violates the Java security model and could allow remote attackers to conduct unauthorized activities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12231.

**参考链接 / References**:
- N/A

---

#### 4. CVE-1999-1015

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:appleshare_mail_server

**漏洞描述 / Description**:
Buffer overflow in Apple AppleShare Mail Server 5.0.3 on MacOS 8.1 and earlier allows a remote attacker to cause a denial of service (crash) via a long HELO command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89200657216213&w=2.

**参考链接 / References**:
- N/A

---

#### 5. CVE-1999-1393

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Control Panel "Password Security" option for Apple Powerbooks allows attackers with physical access to the machine to bypass the security by booting it with an emergency startup disk and using a disk editor to modify the on/off toggle or password in the aaaaaaaAPWD file, which is normally inaccessible.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html.

**参考链接 / References**:
- N/A

---

#### 6. CVE-1999-1412

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server, apple:macos

**漏洞描述 / Description**:
A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/14215.

**参考链接 / References**:
- N/A

---

#### 7. CVE-1999-0793

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer allows remote attackers to read files by redirecting data to a Javascript applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043.

**参考链接 / References**:
- N/A

---

#### 8. CVE-2000-0237

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: netscape:enterprise_server

**漏洞描述 / Description**:
Netscape Enterprise Server with Web Publishing enabled allows remote attackers to list arbitrary directories via a GET request for the /publisher directory, which provides a Java applet that allows the attacker to browse the directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1075.

**参考链接 / References**:
- N/A

---

#### 9. CVE-2000-0265

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: panda:panda_security

**漏洞描述 / Description**:
Panda Security 3.0 allows users to uninstall the Panda software via its Add/Remove Programs applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip.

**参考链接 / References**:
- N/A

---

#### 10. CVE-2000-0266

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.01 allows remote attackers to bypass the cross frame security policy via a malicious applet that interacts with the Java JSObject to modify the DOM properties to set the IFRAME to an arbitrary Javascript URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1121.

**参考链接 / References**:
- N/A

---

#### 11. CVE-2000-0346

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:appleshare

**漏洞描述 / Description**:
AppleShare IP 6.1 and later allows a remote attacker to read potentially sensitive information via an invalid range request to the web server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://asu.info.apple.com/swupdates.nsf/artnum/n11670.

**参考链接 / References**:
- N/A

---

#### 12. CVE-2000-0676

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape Communicator and Navigator 4.04 through 4.74 allows remote attackers to read arbitrary files by using a Java applet to open a connection to a URL using the "file", "http", "https", and "ftp" protocols, as demonstrated by Brown Orifice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc.

**参考链接 / References**:
- N/A

---

#### 13. CVE-2000-0711

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: netscape:communicator, microsoft:virtual_machine

**漏洞描述 / Description**:
Netscape Communicator does not properly prevent a ServerSocket object from being created by untrusted entities, which allows remote attackers to create a server on the victim's system via a malicious applet, as demonstrated by Brown Orifice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-15.html.

**参考链接 / References**:
- N/A

---

#### 14. CVE-2000-0889

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Two Sun security certificates have been compromised, which could allow attackers to insert malicious code such as applets and make it appear that it is signed by Sun.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba.

**参考链接 / References**:
- N/A

---

#### 15. CVE-2001-0068

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_runtime_for_java

**漏洞描述 / Description**:
Mac OS Runtime for Java (MRJ) 2.2.3 allows remote attackers to use malicious applets to read files outside of the CODEBASE context via the ARCHIVE applet parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html.

**参考链接 / References**:
- N/A

---

#### 16. CVE-2001-0137

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Windows Media Player 7 allows remote attackers to execute malicious Java applets in Internet Explorer clients by enclosing the applet in a skin file named skin.wmz, then referencing that skin in the codebase parameter to an applet tag, aka the Windows Media Player Skins File Download" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97958100816503&w=2.

**参考链接 / References**:
- N/A

---

#### 17. CVE-2001-0324

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_2000

**漏洞描述 / Description**:
Windows 98 and Windows 2000 Java clients allow remote attackers to cause a denial of service via a Java applet that opens a large number of UDP sockets, which prevents the host from establishing any additional UDP connections, and possibly causes a crash.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html.

**参考链接 / References**:
- N/A

---

#### 18. CVE-2001-1026

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: trend_micro:interscan_applettrap

**漏洞描述 / Description**:
Trend Micro InterScan AppletTrap 2.0 does not properly filter URLs when they are modified in certain ways such as (1) using a double slash (//) instead of a single slash, (2) URL-encoded characters, (3) requesting the IP address instead of the domain name, or (4) using a leading 0 in an octet of an IP address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html.

**参考链接 / References**:
- N/A

---

#### 19. CVE-2001-1008

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:java_plug-in, sun:jre

**漏洞描述 / Description**:
Java Plugin 1.4 for JRE 1.3 executes signed applets even if the certificate is expired, which could allow remote attackers to conduct unauthorized activities via an applet that has been signed by an expired certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html.

**参考链接 / References**:
- N/A

---

#### 20. CVE-2001-1254

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: com2001:alexis_server

**漏洞描述 / Description**:
Web Access component for COM2001 Alexis 2.0 and 2.1 in InternetPBX sends username and voice mail passwords in the clear via a Java applet that sends the information to port 8888 of the server, which could allow remote attackers to steal the passwords via sniffing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/217200.

**参考链接 / References**:
- N/A

---

#### 21. CVE-2001-0806

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple MacOS X 10.0 and 10.1 allow a local user to read and write to a user's desktop folder via insecure default permissions for the Desktop when it is created in some languages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99358249631139&w=2.

**参考链接 / References**:
- N/A

---

#### 22. CVE-2001-1480

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jdk, sun:jre, apple:mac_os_runtime_for_java, sun:sdk

**漏洞描述 / Description**:
Java Runtime Environment (JRE) and SDK 1.2 through 1.3.0_04 allows untrusted applets to access the system clipboard.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html.

**参考链接 / References**:
- N/A

---

#### 23. CVE-2001-1575

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:personal_web_sharing

**漏洞描述 / Description**:
Apple Personal Web Sharing (PWS) 1.1, 1.5, and 1.5.5, when Web Sharing authentication is enabled, allows remote attackers to cause a denial of service via a long password, possibly due to a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html.

**参考链接 / References**:
- N/A

---

#### 24. CVE-2002-1601

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: adobe:photodeluxe

**漏洞描述 / Description**:
The Connectables feature in Adobe PhotoDeluxe 3.1 prepends the Adobe directory to the CLASSPATH environment variable, which allows applets to run with higher privileges and remote attackers to gain privileges via an HTML e-mail message or a web page.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/116875.

**参考链接 / References**:
- N/A

---

#### 25. CVE-2002-0120

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: palm:palm_desktop

**漏洞描述 / Description**:
Apple Palm Desktop 4.0b76 and 4.0b77 creates world-readable backup files and folders when a hotsync is performed, which could allow a local user to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250093.

**参考链接 / References**:
- N/A

---

#### 26. CVE-2002-0153

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Internet Explorer 5.1 for Macintosh allows remote attackers to bypass security checks and invoke local AppleScripts within a specific HTML element, aka the "Local Applescript Invocation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8851.php.

**参考链接 / References**:
- N/A

---

#### 27. CVE-2002-0252

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.01 and 5.02 allows remote web servers to execute arbitrary code via a response containing a long Content-Type MIME header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101320742616105&w=2.

**参考链接 / References**:
- N/A

---

#### 28. CVE-2002-0676

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
SoftwareUpdate for MacOS 10.1.x does not use authentication when downloading a software update, which could allow remote attackers to execute arbitrary code by posing as the Apple update server via techniques such as DNS spoofing or cache poisoning, and supplying Trojan Horse updates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cunap.com/~hardingr/projects/osx/exploit.html.

**参考链接 / References**:
- N/A

---

#### 29. CVE-2002-0376

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime 5.0 ActiveX component allows remote attackers to execute arbitrary code via a long pluginspage field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293095.

**参考链接 / References**:
- N/A

---

#### 30. CVE-2002-0976

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 4.0 and later allows remote attackers to read arbitrary files via a web page that accesses a legacy XML Datasource applet (com.ms.xml.dso.XMLDSO.class) and modifies the base URL to point to the local system, which is trusted by the applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102960731805373&w=2.

**参考链接 / References**:
- N/A

---

#### 31. CVE-2002-1898

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal

**漏洞描述 / Description**:
Terminal 1.3 in Apple Mac OS X 10.2 allows remote attackers to execute arbitrary commands via shell metacharacters in a telnet:// link, which is executed by Terminal.app window.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172.

**参考链接 / References**:
- N/A

---

#### 32. CVE-2002-2184

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: digi-net_technologies:digichat

**漏洞描述 / Description**:
Digi-Net Technologies DigiChat 3.5 allows chat users to obtain the IP addresses of other chat users via a "Showip" parameter in the chat applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5019.

**参考链接 / References**:
- N/A

---

#### 33. CVE-2002-2242

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: kismac:kismac

**漏洞描述 / Description**:
The Apple Package Manager in KisMAC 0.02a and earlier modifies file permissions of sensitive files after installation, which could allow attackers to conduct unauthorized activities on those files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1005764.

**参考链接 / References**:
- N/A

---

#### 34. CVE-2002-2248

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Buffer overflow in the sun.awt.windows.WDefaultFontCharset Java class implementation in Netscape 4.0 allows remote attackers to execute arbitrary code via an applet that calls the WDefaultFontCharset constructor with a long string and invokes the canConvert method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103834439321292&w=2.

**参考链接 / References**:
- N/A

---

#### 35. CVE-2002-2281

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: symantec:java

**漏洞描述 / Description**:
Symantec Java! JIT (Just-In-Time) Compiler for Netscape Communicator 4.0 through 4.8 allows remote attackers to execute arbitrary Java commands via an applet that uses a jump call, which is not correctly compiled by the JIT compiler.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**参考链接 / References**:
- N/A

---

#### 36. CVE-2002-2284

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape Communicator 4.0 through 4.79 allows remote attackers to bypass JVM security and execute arbitrary Java code via an applet that loads user-supplied Java classes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

**参考链接 / References**:
- N/A

---

#### 37. CVE-2002-2292

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: halycon_software:iasp

**漏洞描述 / Description**:
Directory traversal vulnerability in Remote Console Applet in Halycon Software iASP 1.0.9 allows remote attackers to read arbitrary files via a .. (dot dot) in the HTTP request to port 9095.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html.

**参考链接 / References**:
- N/A

---

#### 38. CVE-2002-2373

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:tcp_ip_configuration_utility, apple:apple_laserwriter

**漏洞描述 / Description**:
The default configuration of the TCP/IP printer configuration utility in Apple LaserWriter 12/640 PS printer contains a blank Telnet password, which allows remote attackers to gain access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10476.php.

**参考链接 / References**:
- N/A

---

#### 39. CVE-2003-0049

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple File Protocol (AFP) in Mac OS X before 10.2.4 allows administrators to log in as other users by using the administrator password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 40. CVE-2003-0050

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 41. CVE-2003-0051

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to obtain the physical path of the server's installation path via a NULL file parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 42. CVE-2003-0052

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to list arbitrary directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 43. CVE-2003-0053

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to insert arbitrary script via the filename parameter, which is inserted into an error message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 44. CVE-2003-0054

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute certain code via a request to port 7070 with the script in an argument to the rtsp DESCRIBE method, which is inserted into a log file and executed when the log is viewed using a browser.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 45. CVE-2003-0055

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime_darwin_mp3_broadcaster

**漏洞描述 / Description**:
Buffer overflow in the MP3 broadcasting module of Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via a long filename.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

**参考链接 / References**:
- N/A

---

#### 46. CVE-2003-0168

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.x and 6.0 for Windows allows remote attackers to execute arbitrary code via a long QuickTime URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html.

**参考链接 / References**:
- N/A

---

#### 47. CVE-2003-0111

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine, microsoft:windows_2000_terminal_services, microsoft:windows_2000

**漏洞描述 / Description**:
The ByteCode Verifier component of Microsoft Virtual Machine (VM) build 5.0.3809 and earlier, as used in Windows and Internet Explorer, allows remote attackers to bypass security checks and execute arbitrary code via a malicious Java applet, aka "Flaw in Microsoft VM Could Enable System Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/11751.php.

**参考链接 / References**:
- N/A

---

#### 48. CVE-2003-0420

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Information leak in dsimportexport for Apple Macintosh OS X Server 10.2.6 allows local users to obtain the username and password of the account running the tool.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/9025/.

**参考链接 / References**:
- N/A

---

#### 49. CVE-2003-0270

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:802.11n

**漏洞描述 / Description**:
The administration capability for Apple AirPort 802.11 wireless access point devices uses weak encryption (XOR with a fixed key) for protecting authentication credentials, which could allow remote attackers to obtain administrative access via sniffing when the capability is available via Ethernet or non-WEP connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8773.

**参考链接 / References**:
- N/A

---

#### 50. CVE-2003-0379

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
Unknown vulnerability in Apple File Service (AFP Server) for Mac OS X Server, when sharing files on a UFS or re-shared NFS volume, allows remote attackers to overwrite arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00030.html.

**参考链接 / References**:
- N/A

---

#### 51. CVE-2003-0421

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 52. CVE-2003-0422

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via a request to view_broadcast.cgi that does not contain the required parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 53. CVE-2003-0423

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to obtain the source code for parseable files via the filename parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 54. CVE-2003-0424

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to obtain the source code for scripts by appending encoded space (%20) or . (%2e) characters to an HTTP request for the script, e.g. view_broadcast.cgi.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 55. CVE-2003-0425

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Directory traversal vulnerability in Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to read arbitrary files via a ... (triple dot) in an HTTP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 56. CVE-2003-0426

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
The installation of Apple QuickTime / Darwin Streaming Server before 4.1.3f starts the administration server with a "Setup Assistant" page that allows remote attackers to set the administrator password and gain privileges before the real administrator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 57. CVE-2003-0502

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

**参考链接 / References**:
- N/A

---

#### 58. CVE-2003-0975

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:safari, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.1 on Mac OS X 10.3.1 and Mac OS X 10.2.8 allows remote attackers to steal user cookies from another domain via a link with a hex-encoded null character (%00) followed by the target domain.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 59. CVE-2003-0885

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: xscreensaver:xscreensaver

**漏洞描述 / Description**:
Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.gentoo.org/show_bug.cgi?id=41253.

**参考链接 / References**:
- N/A

---

#### 60. CVE-2003-1091

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime_broadcaster

**漏洞描述 / Description**:
Integer overflow in MP3Broadcaster for Apple QuickTime/Darwin Streaming Server 4.1.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via malformed ID3 tags in MP3 files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html.

**参考链接 / References**:
- N/A

---

#### 61. CVE-2003-1123

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jre, sun:jdk

**漏洞描述 / Description**:
Sun Java Runtime Environment (JRE) and SDK 1.4.0_01 and earlier allows untrusted applets to access certain information within trusted applets, which allows attackers to bypass the restrictions of the Java security model.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8958.

**参考链接 / References**:
- N/A

---

#### 62. CVE-2003-1413

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Server 4.1.1 allows remote attackers to determine the existence of arbitrary files by using ".." sequences in the filename parameter and comparing the resulting error messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**参考链接 / References**:
- N/A

---

#### 63. CVE-2003-1414

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Directory traversal vulnerability in parse_xml.cg Apple Darwin Streaming Server 4.1.2 and Apple Quicktime Streaming Server 4.1.1 allows remote attackers to read arbitrary files via a ... (triple dot) in the filename parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

**参考链接 / References**:
- N/A

---

#### 64. CVE-2003-1516

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: sun:java_plug-in

**漏洞描述 / Description**:
The org.apache.xalan.processor.XSLProcessorVersion class in Java Plug-in 1.4.2_01 allows signed and unsigned applets to share variables, which violates the Java security model and could allow remote attackers to read or write data belonging to a signed applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/341815.

**参考链接 / References**:
- N/A

---

#### 65. CVE-2003-0601

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Workgroup Manager in Apple Mac OS X Server 10.2 through 10.2.6 does not disable a password for a new account before it is saved for the first time, which allows remote attackers to gain unauthorized access via the new account before it is saved.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25631.

**参考链接 / References**:
- N/A

---

#### 66. CVE-2003-1006

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in cd9660.util in Apple Mac OS X 10.0 through 10.3.2 and Apple Mac OS X Server 10.0 through 10.3.2 may allow local users to execute arbitrary code via a long command line parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 67. CVE-2003-1007

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AppleFileServer (AFS) in Apple Mac OS X 10.2.8 and 10.3.2 does not properly handle certain malformed requests, with unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 68. CVE-2003-1009

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Directory Services in Apple Mac OS X 10.0.2, 10.0.3, 10.2.8, 10.3.2 and Apple Mac OS X Server 10.2 through 10.3.2 accepts authentication server information from unknown LDAP or NetInfo sources as provided by a malicious DHCP server, which allows remote attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=32478.

**参考链接 / References**:
- N/A

---

#### 69. CVE-2003-1011

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.0 through 10.2.8 allows local users with a USB keyboard to gain unauthorized access by holding down the CTRL and C keys when the system is booting, which crashes the init process and leaves the user in a root shell.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 70. CVE-2003-0514

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari allows remote attackers to bypass intended cookie access restrictions on a web application via "%2e%2e" (encoded dot dot) directory traversal sequences in a URL, which causes Safari to send the cookie outside the specified URL subsets, e.g. to a vulnerable application that runs on the same server as the target application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html.

**参考链接 / References**:
- N/A

---

#### 71. CVE-2004-0430

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in AppleFileServer for Mac OS X 10.3.3 and earlier allows remote attackers to execute arbitrary code via a LoginExt packet for a Cleartext Password User Authentication Method (UAM) request with a PathName argument that includes an AFPName type string that is longer than the associated length field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00049.html.

**参考链接 / References**:
- N/A

---

#### 72. CVE-2004-0431

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime (QuickTime.qts) before 6.5.1 allows attackers to execute arbitrary code via a large "number of entries" field in the sample-to-chunk table data for a .mov movie file, which leads to a heap-based buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00048.html.

**参考链接 / References**:
- N/A

---

#### 73. CVE-2004-0723

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
Microsoft Java virtual machine (VM) 5.0.0.3810 allows remote attackers to bypass sandbox restrictions to read or write certain data between applets from different domains via the "GET/Key" and "PUT/Key/Value" commands, aka "cross-site Java."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=108948405808522&w=2.

**参考链接 / References**:
- N/A

---

#### 74. CVE-2004-0518

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in AppleFileServer for Mac OS X 10.3.4, related to "the use of SSH and reporting errors," has unknown impact and attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接 / References**:
- N/A

---

#### 75. CVE-2004-0823

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, openldap:openldap, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenLDAP 1.0 through 2.1.19, as used in Apple Mac OS 10.3.4 and 10.3.5 and possibly other operating systems, may allow certain authentication schemes to use hashed (crypt) passwords in the userPassword attribute as if they were plaintext passwords, which allows remote attackers to re-use hashed passwords without decrypting them.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

**参考链接 / References**:
- N/A

---

#### 76. CVE-2004-0831

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mcafee:virusscan

**漏洞描述 / Description**:
McAfee VirusScan 4.5.1 does not drop SYSTEM privileges before allowing users to browse for files via the "System Scan" properties of the System Tray applet, which could allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=109526269429728&w=2.

**参考链接 / References**:
- N/A

---

#### 77. CVE-2004-1121

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.2.3 allows remote attackers to spoof the URL displayed in the status bar via TABLE tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 78. CVE-2004-1081

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
The Application Framework (AppKit) for Apple Mac OS X 10.2.8 and 10.3.6 does not properly restrict access to a secure text input field, which allows local users to read keyboard input from other applications within the same window session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 79. CVE-2004-1084

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+, which bypass Apache file handles.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 80. CVE-2004-1085

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Human Interface Toolbox (HIToolBox) for Apple Mac 0S X 10.3.6 allows local users to exit applications via the force-quit key combination, even when the system is running in kiosk mode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 81. CVE-2004-1086

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Buffer overflow in PSNormalizer for Apple Mac OS X 10.3.6 allows remote attackers to execute arbitrary code via a crafted PostScript input file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 82. CVE-2004-1087

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Terminal for Apple Mac OS X 10.3.6 may indicate that "Secure Keyboard Entry" is enabled even when it is not, which could result in a false sense of security for the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 83. CVE-2004-1088

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Postfix server for Apple Mac OS X 10.3.6, when using CRAM-MD5, allows remote attackers to send mail without authentication by replaying authentication information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 84. CVE-2004-1089

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Apple Mac OS X 10.3.6 server, when using Kerberos authentication and Cyrus IMAP allows local users to access mailboxes of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 85. CVE-2004-1083

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 restricts access to files in a case sensitive manner, but the Apple HFS+ filesystem accesses files in a case insensitive manner, which allows remote attackers to read .DS_Store files and files beginning with ".ht" using alternate capitalization.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 86. CVE-2004-0622

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.3.4, 10.4, 10.5, and possibly other versions does not properly clear memory for login (aka Loginwindow.app), Keychain, or FileVault passwords, which could allow the root user or an attacker with physical access to obtain sensitive information by reading memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://citp.princeton.edu/pub/coldboot.pdf.

**参考链接 / References**:
- N/A

---

#### 87. CVE-2004-1145

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ethereal_group:ethereal, suse:suse_linux, redhat:enterprise_linux, sgi:propack, redhat:enterprise_linux_desktop

**漏洞描述 / Description**:
Multiple vulnerabilities in Konqueror in KDE 3.3.1 and earlier (1) allow access to restricted Java classes via JavaScript and (2) do not properly restrict access to certain Java classes from the Java applet, which allows remote attackers to bypass sandbox restrictions and read or write arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110356286722875&w=2.

**参考链接 / References**:
- N/A

---

#### 88. CVE-2004-0873

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:ichat_av, apple:ichat

**漏洞描述 / Description**:
Apple iChat AV 2.1, AV 2.0, and 1.0.1 allows remote attackers to execute arbitrary programs via a "link" that references the program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 89. CVE-2004-0429

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability related to "the handling of large requests" in RAdmin for Apple Mac OS X 10.3.3 and Mac OS X 10.2.8 may allow attackers to have unknown impact via unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/May/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 90. CVE-2004-1398

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: roxio:toast

**漏洞描述 / Description**:
Format string vulnerability in prelink.c in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via format string specifiers in the extension argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

**参考链接 / References**:
- N/A

---

#### 91. CVE-2004-1489

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: opera:opera_browser

**漏洞描述 / Description**:
Opera 7.54 and earlier does not properly limit an applet's access to internal Java packages from Sun, which allows remote attackers to gain sensitive information, such as user names and the installation directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html.

**参考链接 / References**:
- N/A

---

#### 92. CVE-2004-1753

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: mozilla:mozilla, mozilla:firefox, netscape:navigator

**漏洞描述 / Description**:
The Apple Java plugin, as used in Netscape 7.1 and 7.2, Mozilla 1.7.2, and Firefox 0.9.3 on MacOS X 10.3.5, when tabbed browsing is enabled, does not properly handle SetWindow(NULL) calls, which allows Java applets from one tab to draw to other tabs and facilitates phishing attacks that spoof tabs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.mozilla.org/show_bug.cgi?id=162134.

**参考链接 / References**:
- N/A

---

#### 93. CVE-2004-2280

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ibm:lotus_notes

**漏洞描述 / Description**:
Buffer overflow in IBM Lotus Notes 6.5.x before 6.5.3 and 6.0.x before 6.0.5 allows remote attackers to cause a denial of service (crash) via unknown vectors related to Java applets, as identified by KSPR62F4KN.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**参考链接 / References**:
- N/A

---

#### 94. CVE-2004-2281

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: ibm:lotus_notes

**漏洞描述 / Description**:
Multiple unknown vulnerabilities in IBM Lotus Notes 6.5.x before 6.5.4 and 6.0.x before 6.0.5 have unknown impact and attack vectors, related to Java applets, as identified by (1) KSPR5YS6GR and (2) KSPR62F4D3.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

**参考链接 / References**:
- N/A

---

#### 95. CVE-2004-2359

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: dell:truemobile_1300_wlan_mini-pci_card_util_trayapplet

**漏洞描述 / Description**:
Dell TrueMobile 1300 WLAN Mini-PCI Card Util TrayApplet 3.10.39.0 does not properly drop SYSTEM privileges when started from the systray applet, which allows local users to gain privileges by accessing the Help functionality.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html.

**参考链接 / References**:
- N/A

---

#### 96. CVE-2004-2367

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: texas_imperial_software:wftpd, texas_imperial_software:wftpd_pro

**漏洞描述 / Description**:
The Control Panel applet in WFTPD and WFTPD Pro 3.21 R1 and R2 allows remote authenticated users to cause a denial of service (crash) via a long FTP command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/11160/.

**参考链接 / References**:
- N/A

---

#### 97. CVE-2004-0926

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server, easy_software_products:cups

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime on Mac OS 10.2.8 through 10.3.5 may allow remote attackers to execute arbitrary code via a certain BMP image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 98. CVE-2004-0962

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:apple_remote_desktop

**漏洞描述 / Description**:
Apple Remote Desktop Client 1.2.4 executes a GUI application as root when it is started by an Apple Remote Desktop Administrator application, which allows remote authenticated users to execute arbitrary code when loginwindow is active via Fast User Switching.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 99. CVE-2004-0988

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow on Apple QuickTime before 6.5.2, when running on Windows systems, allows remote attackers to cause a denial of service (memory consumption) via certain inputs that cause a large memory operation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 100. CVE-2004-1029

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: symantec:enterprise_firewall, gentoo:linux, sun:jre, hp:java_sdk-rte, sun:jdk

**漏洞描述 / Description**:
The Sun Java Plugin capability in Java 2 Runtime Environment (JRE) 1.4.2_01, 1.4.2_04, and possibly earlier versions, does not properly restrict access between Javascript and Java applets during data transfer, which allows remote attackers to load unsafe classes and execute arbitrary code by using the reflection API to access private Java packages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jouko.iki.fi/adv/javaplugin.html.

**参考链接 / References**:
- N/A

---

#### 101. CVE-2005-0043

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Buffer overflow in Apple iTunes 4.7 allows remote attackers to execute arbitrary code via a long URL in (1) .m3u or (2) .pls playlist files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 102. CVE-2005-0289

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:airport_extreme, apple:airport_express

**漏洞描述 / Description**:
Apple AirPort Express prior to 6.1.1 and Extreme prior to 5.5.1, configured as a Wireless Data Service (WDS), allows remote attackers to cause a denial of service (device freeze) by connecting to UDP port 161 and before link-state change occurs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html.

**参考链接 / References**:
- N/A

---

#### 103. CVE-2005-0340

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
Integer signedness error in Apple File Service (AFP Server) allows remote attackers to cause a denial of service (application crash) via a negative UAM string length in a FPLoginExt packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 104. CVE-2005-0341

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.2.4 does not obey the Content-type field in the HTTP header and renders text as HTML, which allows remote attackers to inject arbitrary web script or HTML and perform cross-site scripting (XSS) attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110756965213819&w=2.

**参考链接 / References**:
- N/A

---

#### 105. CVE-2005-0976

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, hmdt:shiira, omnigroup:omniweb

**漏洞描述 / Description**:
AppleWebKit (WebCore and WebKit), as used in multiple products such as Safari 1.2 and OmniGroup OmniWeb 5.1, allows remote attackers to read arbitrary files via the XMLHttpRequest Javascript component, as demonstrated using automatically mounted disk images and file:// URLs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 106. CVE-2005-1331

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:applescript, apple:mac_os_x_server

**漏洞描述 / Description**:
The AppleScript Editor in Mac OS X 10.3.9 does not properly display script code for an applescript: URI, which can result in code that is different than the actual code that would be run, which could allow remote attackers to trick users into executing malicious code via certain URI characters such as NULL, control characters, and homographs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 107. CVE-2005-1337

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Help Viewer 2.0.7 and 3.0.0 in Mac OS X 10.3.9 allows remote attackers to read and execute arbitrary scrpts with less restrictive privileges via a help:// URI.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 108. CVE-2005-1341

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Terminal 1.4.4 allows attackers to execute arbitrary commands via terminal escape sequences.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 109. CVE-2005-1342

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal

**漏洞描述 / Description**:
The x-man-page: URI handler for Apple Terminal 1.4.4 in Mac OS X 10.3.9 does not cleanse terminal escape sequences, which allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 110. CVE-2005-1579

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime Player 7.0 on Mac OS X 10.4 allows remote attackers to obtain sensitive information via a .mov file with a Quartz Composer composition (.qtz) file that uses certain patches to read local information, then other patches to send the information to the attacker.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html.

**参考链接 / References**:
- N/A

---

#### 111. CVE-2005-1193

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: phpbb_group:phpbb

**漏洞描述 / Description**:
The bbencode_second_pass and make_clickable functions in bbcode.php for phpBB before 2.0.15, as used in viewtopic.php, privmsg.php, and other scripts, allow remote attackers to execute arbitrary script via a BBcode tag with a (1) javascript:, (2) applet:, (3) about:, (4) activex:, (5) chrome:, or (6) script: URI scheme, as demonstrated using the URL tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://castlecops.com/t123194-.html.

**参考链接 / References**:
- N/A

---

#### 112. CVE-2005-1248

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Buffer overflow in Apple iTunes before 4.8 allows remote attackers to execute arbitrary code via a crafted MPEG4 file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301596.

**参考链接 / References**:
- N/A

---

#### 113. CVE-2005-1472

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Certain system calls in Apple Mac OS X 10.4.1 do not properly enforce the permissions of certain directories without the POSIX read bit set, but with the execute bits set for group or other, which allows local users to list files in otherwise restricted directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接 / References**:
- N/A

---

#### 114. CVE-2005-1408

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:keynote

**漏洞描述 / Description**:
Apple Keynote 2.0 and 2.0.1 allows remote attackers to read arbitrary files via the keynote: URI handler in a crafted Keynote presentation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00005.html.

**参考链接 / References**:
- N/A

---

#### 115. CVE-2005-1723

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
LaunchServices in Apple Mac OS X 10.4.x up to 10.4.1 does not properly mark file extensions and MIME types as unsafe if an Apple Uniform Type Identifier (UTI) is not created when the type is added to the database of unsafe types, which could allow attackers to bypass intended restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 116. CVE-2005-1724

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
NFS on Apple Mac OS X 10.4.x up to 10.4.1 does not properly obey the -network or -mask flags for a filesystem and exports it to everyone, which allows remote attackers to bypass intended access restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 117. CVE-2005-1725

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
launchd 106 in Apple Mac OS X 10.4.x up to 10.4.1 allows local users to overwrite arbitrary files via a symlink attack on the socket file in an insecure temporary directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 118. CVE-2005-1727

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Mac OS X 10.4.x up to 10.4.1 sets insecure world- and group-writable permissions for the (1) system cache folder and (2) Dashboard system widgets, which allows local users to conduct unauthorized file operations via "file race conditions."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 119. CVE-2005-1728

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
MCX Client for Apple Mac OS X 10.4.x up to 10.4.1 insecurely logs Portable Home Directory credentials, which allows local users to obtain the credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 120. CVE-2005-1473

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
SecurityAgent in Apple Mac OS X 10.4.1 allows attackers with physical access to bypass the locked screensaver and launch background applications by opening a URL from a text input field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接 / References**:
- N/A

---

#### 121. CVE-2005-1474

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Dashboard in Apple Mac OS X 10.4.1 allows remote attackers to install widgets via Safari without prompting the user, a different vulnerability than CVE-2005-1933.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

**参考链接 / References**:
- N/A

---

#### 122. CVE-2005-1933

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Dashboard in Apple Mac OS X Tiger 10.4 allows attackers to execute arbitrary commands by overriding the behavior of system widgets via a user widget with the same bundle identifier (CFBundleIdentifier), a different vulnerability than CVE-2005-1474.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/983429.

**参考链接 / References**:
- N/A

---

#### 123. CVE-2005-2195

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple Darwin Streaming Server 5.5 and earlier allows remote attackers to cause a denial of service (application crash) via a URL with a filename containing a .cgi extension and an MS-DOS device name such as AUX, CON, PRN, COM1, or LPT1, a different vulnerability than CVE-2003-0421 and CVE-2003-0502.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112126999514361&w=2.

**参考链接 / References**:
- N/A

---

#### 124. CVE-2005-2196

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:airport_card

**漏洞描述 / Description**:
The Apple AirPort card uses a default WEP key when not connected to a known or trusted network, which can cause it to automatically connect to a malicious network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1014522.

**参考链接 / References**:
- N/A

---

#### 125. CVE-2005-2594

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.3 (132) on Mac OS X 1.3.9 allows remote attackers to cause a denial of service (crash) via certain Javascript, possibly involving a function that defines a handler for itself within the function body.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/407702.

**参考链接 / References**:
- N/A

---

#### 126. CVE-2005-3018

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari allows remote attackers to cause a denial of service (application crash) via a crafted data:// URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112715234411672&w=2.

**参考链接 / References**:
- N/A

---

#### 127. CVE-2005-2744

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in QuickDraw Manager for Apple OS X 10.3.9 and 10.4.2, as used by applications such as Safari, Mail, and Finder, allows remote attackers to execute arbitrary code via a crafted PICT file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 128. CVE-2005-2747

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in ImageIO for Apple Mac OS X 10.4.2, as used by applications such as WebCore and Safari, allows remote attackers to execute arbitrary code via a crafted GIF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 129. CVE-2005-2748

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The malloc function in the libSystem library in Apple Mac OS X 10.3.9 and 10.4.2 allows local users to overwrite arbitrary files by setting the MallocLogFile environment variable to the target file before running a setuid application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 130. CVE-2005-2524

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Safari after 2.0 in Apple Mac OS X 10.3.9 allows remote attackers to bypass domain restrictions via crafted web archives that cause Safari to render them as if they came from a different site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 131. CVE-2005-2741

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, perry_kiehtreiber:securityd, apple:mac_os_x_server

**漏洞描述 / Description**:
Authorization Services in securityd for Apple Mac OS X 10.3.9 allows local users to gain privileges by granting themselves certain rights that should be restricted to administrators.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 132. CVE-2005-2742

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
SecurityAgent in Apple Mac OS X 10.4.2, under certain circumstances, can cause the "Switch User..." button to appear even though the "Enable fast user switching" setting is disabled, which can allow attackers with physical access to gain access to the desktop and bypass the "Require password to wake this computer from sleep or screen saver" setting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 133. CVE-2005-2743

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x, apple:quicktime

**漏洞描述 / Description**:
The Java extensions for QuickTime 6.52 and earlier in Apple Mac OS X 10.3.9 allow untrusted applets to call arbitrary functions in system libraries, which allows remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 134. CVE-2005-2745

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9, when using Kerberos 5 for SMTP authentication, can include uninitialized memory in a message, which might allow remote attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 135. CVE-2005-2746

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9 and 10.4.2 includes message contents when using auto-reply rules, which could cause Mail.app to include decrypted message contents for encrypted messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 136. CVE-2005-2753

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file that causes a sign extension of the length element in a Pascal style string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接 / References**:
- N/A

---

#### 137. CVE-2005-2754

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file with "Improper movie attributes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接 / References**:
- N/A

---

#### 138. CVE-2005-2755

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime Player before 7.0.3 allows user-assisted attackers to cause a denial of service (crash) via a crafted file with a missing movie attribute, which leads to a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html.

**参考链接 / References**:
- N/A

---

#### 139. CVE-2005-2756

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime before 7.0.3 allows user-assisted attackers to overwrite memory and execute arbitrary code via a crafted PICT file that triggers an overflow during expansion.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

**参考链接 / References**:
- N/A

---

#### 140. CVE-2005-3897

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.2 allows remote attackers to cause a denial of service (system slowdown) via a Javascript BODY onload event that calls the window function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=113278010907401&w=2.

**参考链接 / References**:
- N/A

---

#### 141. CVE-2005-3907

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jdk, sun:jre

**漏洞描述 / Description**:
Unspecified vulnerability in Java Runtime Environment in Java JDK and JRE 5.0 Update 3 and earlier allows remote attackers to escape the Java sandbox and access arbitrary files or execute arbitrary applications via unknown attack vectors involving untrusted Java applets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html.

**参考链接 / References**:
- N/A

---

#### 142. CVE-2005-3946

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: opera:opera_browser

**漏洞描述 / Description**:
Opera 8.50 allows remote attackers to cause a denial of service (crash) via a Java applet with a large string argument to the removeMember JNI method for the com.opera.JSObject class.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.illegalaccess.org/exploit/opera85/OperaApplet.html.

**参考链接 / References**:
- N/A

---

#### 143. CVE-2005-4092

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes, apple:quicktime

**漏洞描述 / Description**:
Multiple heap-based buffer overflows in QuickTime.qts in Apple QuickTime Player 7.0.3 and iTunes 6.0.1 (3) and earlier allow remote attackers to cause a denial of service (crash) and execute arbitrary code via a .mov file with (1) a Movie Resource atom with a large size value, or (2) an stsd atom with a modified Sample Description Table size value, and possibly other vectors involving media files.  NOTE: item 1 was originally identified by CVE-2005-4127 for a pre-patch announcement, and item 2 was originally identified by CVE-2005-4128 for a pre-patch announcement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**参考链接 / References**:
- N/A

---

#### 144. CVE-2005-4197

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: nortel:ssl_vpn

**漏洞描述 / Description**:
tunnelform.yaws in Nortel SSL VPN 4.2.1.6 allows remote attackers to execute arbitrary commands via a link in the a parameter, which is executed with extra privileges in a cryptographically signed Java Applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17974.

**参考链接 / References**:
- N/A

---

#### 145. CVE-2005-4217

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Perl in Apple Mac OS X Server 10.3.9 does not properly drop privileges when using the "$<" variable to set uid, which allows attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接 / References**:
- N/A

---

#### 146. CVE-2005-4504

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:safari, apple:textedit, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
The khtml::RenderTableSection::ensureRows function in KHTMLParser in Apple Mac OS X 10.4.3 and earlier, as used by Safari and TextEdit, allows remote attackers to cause a denial of service (memory consumption and application crash) via HTML files with a large ROWSPAN attribute in a TD tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接 / References**:
- N/A

---

#### 147. CVE-2005-2194

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in the Apple Mac OS X kernel before 10.4.2 allows remote attackers to cause a denial of service (kernel panic) via a crafted TCP packet, possibly related to source routing or loose source routing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301948.

**参考链接 / References**:
- N/A

---

#### 148. CVE-2005-2340

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a crafted (1) QuickTime Image File (QTIF), (2) PICT, or (3) JPEG format image with a long data field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html.

**参考链接 / References**:
- N/A

---

#### 149. CVE-2005-2527

**严重程度 / Severity**: N/A | CVSS: 1.2
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Race condition in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to corrupt files or create arbitrary files via unspecified attack vectors related to a temporary directory, possibly due to a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**参考链接 / References**:
- N/A

---

#### 150. CVE-2005-2529

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Unspecified vulnerability in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to gain privileges via unspecified attack vectors relating to "the utility used to update Java shared archives."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

**参考链接 / References**:
- N/A

---

#### 151. CVE-2005-2530

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Unspecified vulnerability in Java 1.3.1 before 1.3.1_16 on Apple Mac OS X allows an untrusted applet to gain privileges, related to "Mac OS X specific extensions."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**参考链接 / References**:
- N/A

---

#### 152. CVE-2005-2738

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X does not prevent multiple programs from opening the same port as a Java ServerSocket, which allows local users to operate a Java program that intercepts network data intended for the ServerSocket of a different Java program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

**参考链接 / References**:
- N/A

---

#### 153. CVE-2005-3707

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html.

**参考链接 / References**:
- N/A

---

#### 154. CVE-2005-3708

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

**参考链接 / References**:
- N/A

---

#### 155. CVE-2005-3709

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer underflow in Apple Quicktime before 7.0.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via the Color Map Entry Size in a TGA image file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html.

**参考链接 / References**:
- N/A

---

#### 156. CVE-2005-3710

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified image height and width (ImageWidth) tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html.

**参考链接 / References**:
- N/A

---

#### 157. CVE-2005-3711

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified (1) "strips" (StripByteCounts) or (2) "bands" (StripOffsets) values.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html.

**参考链接 / References**:
- N/A

---

#### 158. CVE-2005-3713

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a GIF image file with a crafted Netscape Navigator Application Extension Block that modifies the heap in the Picture Modifier block.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html.

**参考链接 / References**:
- N/A

---

#### 159. CVE-2005-3714

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:airport_extreme, apple:airport_express

**漏洞描述 / Description**:
The network interface for Apple AirPort Express 6.x before Firmware Update 6.3, and AirPort Extreme 5.x before Firmware Update 5.7, allows remote attackers to cause a denial of service (unresponsive interface) via malformed packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 160. CVE-2005-4678

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.2 (aka 416.12) allows remote attackers to spoof the URL in the status bar via the title in an image in a link to a trusted site within a form to the malicious site.  NOTE: the provenance of this information is unknown; the details are obtained solely from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17618.

**参考链接 / References**:
- N/A

---

#### 161. CVE-2005-4866

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: ibm:db2_universal_database

**漏洞描述 / Description**:
Stack-based buffer overflow in JDBC Applet Server in IBM DB2 8.1 allows remote attackers to execute arbitrary by connecting and sending a long username, then disconnecting gracefully and reconnecting and sending a short username and an unexpected db2java.zip version, which causes a null terminator to be removed and leads to the overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110495251101381&w=2.

**参考链接 / References**:
- N/A

---

#### 162. CVE-2006-0382

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.4.5 and allows local users to cause a denial of service (crash) via an undocumented system call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 163. CVE-2006-0848

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
The "Open 'safe' files after downloading" option in Safari on Apple Mac OS X allows remote user-assisted attackers to execute arbitrary commands by tricking a user into downloading a __MACOSX folder that contains metadata (resource fork) that invokes the Terminal, which automatically interprets the script using bash, as demonstrated using a ZIP file that contains a script with a safe file extension.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

**参考链接 / References**:
- N/A

---

#### 164. CVE-2006-0396

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in Mail in Apple Mac OS X 10.4 up to 10.4.5, when patched with Security Update 2006-001, allows remote attackers to execute arbitrary code via a long Real Name value in an e-mail attachment sent in AppleDouble format, which triggers the overflow when the user double-clicks on an attachment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接 / References**:
- N/A

---

#### 165. CVE-2006-0397

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接 / References**:
- N/A

---

#### 166. CVE-2006-0398

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接 / References**:
- N/A

---

#### 167. CVE-2006-0399

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接 / References**:
- N/A

---

#### 168. CVE-2006-0400

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to bypass the same-origin policy and execute Javascript in other domains via unknown vectors involving "crafted archives."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

**参考链接 / References**:
- N/A

---

#### 169. CVE-2006-1249

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:itunes, apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime Player 7.0.3 and 7.0.4 and iTunes 6.0.1 and 6.0.2 allows remote attackers to execute arbitrary code via a FlashPix (FPX) image that contains a field that specifies a large number of blocks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 170. CVE-2006-1552

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, apple:mac_os_x_server, apple:mac_os_x, apple:imageio

**漏洞描述 / Description**:
Integer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to cause a denial of service (crash) via a crafted JPEG image with malformed JPEG metadata, as demonstrated using Safari, aka "Deja-Doom".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://drunkenblog.com/drunkenblog-archives/000760.html.

**参考链接 / References**:
- N/A

---

#### 171. CVE-2006-1986

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via a large CELLSPACING attribute in a TABLE tag, which triggers an error in KWQListIteratorImpl::KWQListIteratorImpl.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接 / References**:
- N/A

---

#### 172. CVE-2006-1987

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via an invalid FRAME tag, possibly due to (1) multiple SCROLLING attributes with no values, or (2) a SRC attribute with no value.  NOTE: due to lack of diagnosis by the researcher, it is unclear which vector is responsible.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接 / References**:
- N/A

---

#### 173. CVE-2006-1988

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
The WebTextRenderer(WebInternal) _CG_drawRun:style:geometry: function in Apple Safari 2.0.3 allows remote attackers to cause a denial of service (application crash) via an HTML LI tag with a large VALUE attribute (list item number), which triggers a null dereference in QPainter::drawText, probably due to a failed memory allocation that uses the VALUE.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

**参考链接 / References**:
- N/A

---

#### 174. CVE-2006-2019

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Mac OS X Safari 2.0.3, 1.3.1, and possibly other versions allows remote attackers to cause a denial of service (CPU consumption and crash) via a TD element with a large number in the rowspan attribute.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html.

**参考链接 / References**:
- N/A

---

#### 175. CVE-2006-2277

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Multiple Apple Mac OS X 10.4 applications might allow context-dependent attackers to cause a denial of service (application crash) via a crafted OpenEXR (.exr) image file, which triggers the crash when opening a folder using Finder, displaying the image in Safari, or using Preview to open the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/27780.

**参考链接 / References**:
- N/A

---

#### 176. CVE-2006-1453

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Stack-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file containing malformed font information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 177. CVE-2006-1454

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file with malformed image data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 178. CVE-2006-1458

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime Player before 7.1 allows remote attackers to execute arbitrary code via a crafted JPEG image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 179. CVE-2006-1459

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to cause a denial of service or execute arbitrary code via a crafted QuickTime movie (.MOV).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 180. CVE-2006-1460

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime movie (.MOV), as demonstrated via a large size for a udta Atom.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 181. CVE-2006-1461

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime Flash (SWF) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 182. CVE-2006-1462

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime H.264 (M4V) video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 183. CVE-2006-1463

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a H.264 (M4V) video format file with a certain modified size value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 184. CVE-2006-1464

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickTime MPEG4 (M4P) video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 185. CVE-2006-1465

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickTime AVI video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 186. CVE-2006-1439

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
NSSecureTextField in AppKit in Apple Mac OS X 10.4.6 does not re-enable secure event input under certain circumstances, which could allow other applications in the window session to monitor input characters and keyboard events.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 187. CVE-2006-1440

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
BOM in Apple Mac OS X 10.3.9 and 10.4.6 allows attackers to overwrite arbitrary files via an archive that contains symbolic links.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 188. CVE-2006-1441

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in CFNetwork in Apple Mac OS X 10.4.6 allows remote attackers to execute arbitrary code via crafted chunked transfer encoding.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 189. CVE-2006-1442

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The bundle API in CoreFoundation in Apple Mac OS X 10.3.9 and 10.4.6 loads dynamic libraries even if the client application has not directly requested it, which allows attackers to execute arbitrary code from an untrusted bundle.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 190. CVE-2006-1443

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer underflow in CoreFoundation in Apple Mac OS X 10.3.9 and 10.4.6 allows context-dependent attackers to execute arbitrary code via unspecified vectors involving conversions from string to file system representation within (1) CFStringGetFileSystemRepresentation or (2) getFileSystemRepresentation:maxLength:withPath in NSFileManager, and possibly other similar API functions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 191. CVE-2006-1444

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
CoreGraphics in Apple Mac OS X 10.4.6, when "Enable access for assistive devices" is on, allows an application to bypass restrictions for secure event input and read certain events from other applications in the same window session by using Quartz Event Services.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 192. CVE-2006-1445

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the FTP server (FTPServer) in Apple Mac OS X 10.3.9 and 10.4.6 allows remote authenticated users to execute arbitrary code via vectors related to "FTP server path name handling."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 193. CVE-2006-1446

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Keychain in Apple Mac OS X 10.3.9 and 10.4.6 might allow an application to bypass a locked Keychain by first obtaining a reference to the Keychain when it is unlocked, then reusing that reference after the Keychain has been locked.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 194. CVE-2006-1447

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
LaunchServices in Apple Mac OS X 10.4.6 allows remote attackers to cause Safari to launch unsafe content via long file name extensions, which prevents Download Validation from determining which application will be used to open the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 195. CVE-2006-1448

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Finder in Apple Mac OS X 10.3.9 and 10.4.6 allows user-assisted attackers to execute arbitrary code by tricking a user into launching an Internet Location item that appears to use a safe URL scheme, but which actually has a different and more risky scheme.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 196. CVE-2006-1449

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in Mail in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via a crafted MacMIME encapsulated attachment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 197. CVE-2006-1450

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mail in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via an enriched text e-mail message with "invalid color information" that causes Mail to allocate and initialize arbitrary classes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 198. CVE-2006-1451

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
MySQL Manager in Apple Mac OS X 10.3.9 and 10.4.6, when setting up a new MySQL database server, does not use the "New MySQL root password" that is provided, which causes the MySQL root password to be blank and allows local users to gain full privileges to that database.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 199. CVE-2006-1452

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Stack-based buffer overflow in Preview in Apple Mac OS 10.4 up to 10.4.6 allows local users to execute arbitrary code via a deep directory hierarchy.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 200. CVE-2006-1455

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
QuickTime Streaming Server in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to cause a denial of service (crash and connection interruption) via a QuickTime movie with a missing track, which triggers a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 201. CVE-2006-1456

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in QuickTime Streaming Server in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via a crafted RTSP request, which is not properly handled during message logging.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 202. CVE-2006-1457

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Safari on Apple Mac OS X 10.4.6, when "Open `safe' files after downloading" is enabled, will automatically expand archives, which could allow remote attackers to overwrite arbitrary files via an archive that contains a symlink.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

**参考链接 / References**:
- N/A

---

#### 203. CVE-2006-2238

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted BMP file that triggers the overflow in the ReadBMP function.  NOTE: this issue was originally included as item 3 in CVE-2006-1983, but it has been given a separate identifier because it is a distinct issue.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 204. CVE-2006-3224

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 (417.9.3) on Mac OS X 10.4.6 allows remote attackers to cause a denial of service (CPU consumption) via Javascript with an infinite for loop.  NOTE: it could be argued that this is not a vulnerability, unless it interferes with the operation of the system outside of the scope of Safari itself.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-May/046150.html.

**参考链接 / References**:
- N/A

---

#### 205. CVE-2006-1468

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Apple File Protocol (AFP) server in Apple Mac OS X 10.4 up to 10.4.6 includes the names of restricted files and folders within search results, which might allow remote attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 206. CVE-2006-1469

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.6 allows attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted TIFF image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 207. CVE-2006-1470

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenLDAP in Apple Mac OS X 10.4 up to 10.4.6 allows remote attackers to cause a denial of service (crash) via an invalid LDAP request that triggers an assert error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 208. CVE-2006-1471

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Format string vulnerability in the CF_syslog function launchd in Apple Mac OS X 10.4 up to 10.4.6 allows local users to execute arbitrary code via format string specifiers that are not properly handled in a syslog call in the logging facility, as demonstrated by using a crafted plist file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 209. CVE-2006-1467

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Integer overflow in the AAC file parsing code in Apple iTunes before 6.0.5 on Mac OS X 10.2.8 or later, and Windows XP and 2000, allows remote user-assisted attackers to execute arbitrary code via an AAC (M4P, M4A, or M4B) file with a sample table size (STSZ) atom with a "malformed" sample_size_table value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303952.

**参考链接 / References**:
- N/A

---

#### 210. CVE-2006-2199

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: openoffice:openoffice, sun:staroffice

**漏洞描述 / Description**:
Unspecified vulnerability in Java Applets in OpenOffice.org 1.1.x (aka StarOffice) up to 1.1.5 and 2.0.x before 2.0.3 allows user-assisted attackers to escape the Java sandbox and conduct unauthorized activities via certain applets in OpenOffice documents.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://fedoranews.org/cms/node/2343.

**参考链接 / References**:
- N/A

---

#### 211. CVE-2006-3356

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The TIFFFetchAnyArray function in ImageIO in Apple OS X 10.4.7 and earlier allows remote user-assisted attackers to cause a denial of service (application crash) via an invalid tag value in a TIFF image, possibly triggering a null dereference.  NOTE: This is a different issue than CVE-2006-1469.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.security-protocols.com/sp-x31-advisory.php.

**参考链接 / References**:
- N/A

---

#### 212. CVE-2006-3372

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.4/419.3 allows remote attackers to cause a denial of service (application crash) via a DHTML setAttributeNode function call with zero arguments, which triggers a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://browserfun.blogspot.com/2006/07/mobb-5-dhtml-setattributenode.html.

**参考链接 / References**:
- N/A

---

#### 213. CVE-2006-3413

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: tor:tor

**漏洞描述 / Description**:
The privoxy configuration file in Tor before 0.1.1.20, when run on Apple OS X, logs all data via the "logfile", which allows attackers to obtain potentially sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/20514.

**参考链接 / References**:
- N/A

---

#### 214. CVE-2006-3545

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 7.0 Beta allows remote attackers to cause a denial of service (application crash) via a web page with multiple empty APPLET start tags.  NOTE: a third party has disputed this issue, stating that the crash does not occur with Microsoft Internet Explorer 7.0 Beta3

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/438754/100/0/threaded.

**参考链接 / References**:
- N/A

---

#### 215. CVE-2006-3946

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:safari

**漏洞描述 / Description**:
WebCore in Apple Mac OS X 10.3.9 and 10.4 through 10.4.7 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via crafted HTML that triggers a "memory management error" in WebKit, possibly due to a buffer overflow, as originally reported for the KHTMLParser::popOneBlock function in Apple Safari 2.0.4 using Javascript that changes document.body.innerHTML within a DIV tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://browserfun.blogspot.com/2006/07/mobb-31-safari-khtmlparserpoponeblock.html.

**参考链接 / References**:
- N/A

---

#### 216. CVE-2006-1472

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in AFP Server in Apple Mac OS X 10.3.9 allows remote attackers to determine names of unauthorized files and folders via unknown vectors related to the search results.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 217. CVE-2006-1473

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in AFP Server for Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause a denial of service (crash) and execute arbitrary code via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 218. CVE-2006-3495

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server in Apple Mac OS X 10.3.9 and 10.4.7 stores reconnect keys in a world-readable file, which allows local users to obtain the keys and access files and folders of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 219. CVE-2006-3496

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server in Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause denial of service (crash) via an invalid AFP request that triggers an unchecked error condition.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 220. CVE-2006-3497

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in the "compression state handling" in Bom for Apple Mac OS X 10.3.9 and 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Zip archive.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 221. CVE-2006-3498

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in bootpd in the DHCP component for Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to execute arbitrary code via a crafted BOOTP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 222. CVE-2006-0392

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Canon RAW image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 223. CVE-2006-0393

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenSSH in Apple Mac OS X 10.4.7 allows remote attackers to cause a denial of service or determine account existence by attempting to log in using an invalid user, which causes the server to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 224. CVE-2006-3499

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The dynamic linker (dyld) in Apple Mac OS X 10.3.9 allows local users to obtain sensitive information via unspecified dynamic linker options that affect the use of standard error (stderr) by privileged applications.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 225. CVE-2006-3500

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The dynamic linker (dyld) in Apple Mac OS X 10.4.7 allows local users to execute arbitrary code via an "improperly handled condition" that leads to use of "dangerous paths," probably related to an untrusted search path vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 226. CVE-2006-3501

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in ImageIO for Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Radiance image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 227. CVE-2006-3502

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in ImageIO in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted GIF image that triggers a memory allocation failure that is not properly handled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 228. CVE-2006-3503

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in ImageIO in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (crash) and possibly execute arbitrary code via a malformed GIF image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 229. CVE-2006-3504

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The Download Validation in LaunchServices for Apple Mac OS X 10.4.7 can identify certain HTML as "safe", which could allow attackers to execute Javascript code in local context when the "Open 'safe' files after downloading" option is enabled in Safari.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 230. CVE-2006-3505

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
WebKit in Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted HTML document that causes WebKit to access an object that has already been deallocated.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 231. CVE-2006-4381

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted H.264 movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 232. CVE-2006-4382

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1.3 allow user-assisted remote attackers to execute arbitrary code via a crafted QuickTime movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 233. CVE-2006-4384

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via the COLOR_64 chunk in a FLIC (FLC) movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 234. CVE-2006-4385

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted SGI image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 235. CVE-2006-4386

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted H.264 movie, a different issue than CVE-2006-4381.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 236. CVE-2006-4388

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted FlashPix file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 237. CVE-2006-4389

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted FlashPix (FPX) file, which triggers an exception that leads to an operation on an uninitialized object.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

**参考链接 / References**:
- N/A

---

#### 238. CVE-2006-4866

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via a long extension argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

**参考链接 / References**:
- N/A

---

#### 239. CVE-2006-4887

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:apple_remote_desktop, apple:mac_os_x

**漏洞描述 / Description**:
Apple Remote Desktop (ARD) for Mac OS X 10.2.8 and later does not drop privileges on the remote machine while installing certain applications, which allows local users to bypass authentication and gain privileges by selecting the icon during installation.  NOTE: it could be argued that the issue is not in Remote Desktop itself, but in applications that are installed while using it.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/32260.

**参考链接 / References**:
- N/A

---

#### 240. CVE-2006-3507

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Multiple stack-based buffer overflows in the AirPort wireless driver on Apple Mac OS X 10.3.9 and 10.4.7 allow physically proximate attackers to execute arbitrary code by injecting crafted frames into a wireless network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 241. CVE-2006-3508

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Heap-based buffer overflow in the AirPort wireless driver on Apple Mac OS X 10.4.7 allows physically proximate attackers to cause a denial of service (crash), gain privileges, and execute arbitrary code via a crafted frame that is not properly handled during scan cache updates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 242. CVE-2006-3509

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in the API for the AirPort wireless driver on Apple Mac OS X 10.4.7 might allow physically proximate attackers to cause a denial of service (crash) or execute arbitrary code in third-party wireless software that uses the API via crafted frames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 243. CVE-2006-4965

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime 7.1.3 Player and Plug-In allows remote attackers to execute arbitrary JavaScript code and possibly conduct other attacks via a QuickTime Media Link (QTL) file with an embed XML element and a qtnext parameter that identifies resources outside of the original domain.  NOTE: as of 20070912, this issue has been demonstrated by using instances of Components.interfaces.nsILocalFile and Components.interfaces.nsIProcess to execute arbitrary local files within Firefox and possibly Internet Explorer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305149.

**参考链接 / References**:
- N/A

---

#### 244. CVE-2006-4387

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.4 through 10.4.7, when the administrator clears the "Allow user to administer this computer" checkbox in System Preferences for a user, does not remove the user's account from the appserveradm or appserverusr groups, which still allows the user to manage WebObjects applications.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 245. CVE-2006-4390

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
CFNetwork in Apple Mac OS X 10.4 through 10.4.7 and 10.3.9 allows remote SSL sites to appear as trusted sites by using encryption without authentication, which can cause the lock icon in Safari to be displayed even when the site's identity cannot be trusted.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 246. CVE-2006-4391

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in Apple ImageIO on Apple Mac OS X 10.4 through 10.4.7 allows remote attackers to execute arbitrary code via a malformed JPEG2000 image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 247. CVE-2006-4393

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in LoginWindow in Apple Mac OS X 10.4 through 10.4.7, when Fast User Switching is enabled, allows local users to gain access to Kerberos tickets of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 248. CVE-2006-4394

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
A logic error in LoginWindow in Apple Mac OS X 10.4 through 10.4.7, allows network accounts without GUIds to bypass service access controls and log into the system using loginwindow via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 249. CVE-2006-4395

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in QuickDraw Manager in Apple Mac OS X 10.3.9 and 10.4 through 10.4.7 allows context-dependent attackers to cause a denial of service ("memory corruption" and crash) via a crafted PICT image that is not properly handled by a certain "unsupported QuickDraw operation."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 250. CVE-2006-4397

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unchecked error condition in LoginWindow in Apple Mac OS X 10.4 through 10.4.7 prevents Kerberos tickets from being destroyed if a user does not successfully log on to a network account from the login window, which might allow later users to gain access to the original user's Kerberos tickets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 251. CVE-2006-4399

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
User interface inconsistency in Workgroup Manager in Apple Mac OS X 10.4 through 10.4.7 appears to allow administrators to change the authentication type from crypt to ShadowHash passwords for accounts in a NetInfo parent, when such an operation is not actually supported, which could result in less secure password management than intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

**参考链接 / References**:
- N/A

---

#### 252. CVE-2006-5327

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: openbase_international_ltd:openbase, apple:xcode

**漏洞描述 / Description**:
Untrusted search path vulnerability in OpenBase SQL 10.0 and earlier, as used in Apple Xcode 2.2 2.2 and earlier and possibly other products, allows local users to execute arbitrary code via a modified PATH that references a malicious gzip program, which is executed by gnutar with certain TAR_OPTIONS environment variable settings, when gnutar is invoked by OpenBase.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2007/Oct/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 253. CVE-2006-5328

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: openbase_international_ltd:openbase, apple:xcode

**漏洞描述 / Description**:
OpenBase SQL 10.0 and earlier, as used in Apple Xcode 2.2 2.2 and earlier and possibly other products, allows local users to create arbitrary files via a symlink attack on the simulation.sql file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2007/Oct/msg00001.html.

**参考链接 / References**:
- N/A

---

#### 254. CVE-2006-5710

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: opendarwin:darwin_kernel, apple:mac_os_x

**漏洞描述 / Description**:
The Airport driver for certain Orinoco based Airport cards in Darwin kernel 8.8.0 in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to execute arbitrary code via an 802.11 probe response frame without any valid information element (IE) fields after the header, which triggers a heap-based buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 255. CVE-2006-5836

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: opendarwin:darwin_kernel

**漏洞描述 / Description**:
The fpathconf syscall function in bsd/kern/kern_descrip.c in the Darwin kernel (XNU) 8.8.1 in Apple Mac OS X allows local users to cause a denial of service (kernel panic) and possibly execute arbitrary code via a file descriptor with an unrecognized file type.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

**参考链接 / References**:
- N/A

---

#### 256. CVE-2006-4413

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:remote_desktop

**漏洞描述 / Description**:
Apple Remote Desktop before 3.1 uses insecure permissions for certain built-in packages, which allows local users on an Apple Remote Desktop administration system to modify the packages and gain root privileges on client systems that use the packages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Nov/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 257. CVE-2006-6009

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:jre, sun:jdk

**漏洞描述 / Description**:
Unspecified vulnerability in the Java Runtime Environment (JRE) Swing library in JDK and JRE 5.0 Update 7 and earlier allows attackers to obtain certain information via unknown attack vectors, related to an untrusted applet accessing data in other applets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/22910.

**参考链接 / References**:
- N/A

---

#### 258. CVE-2006-6015

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the JavaScript implementation in Safari on Apple Mac OS X 10.4 allows remote attackers to cause a denial of service (application crash) via a long argument to the exec method of a regular expression.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/451542/100/0/threaded.

**参考链接 / References**:
- N/A

---

#### 259. CVE-2006-6061

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
com.apple.AppleDiskImageController in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to execute arbitrary code via a malformed DMG image that triggers memory corruption.  NOTE: the severity of this issue has been disputed by a third party, who states that the impact is limited to a denial of service (kernel panic) due to a vm_fault call with a non-aligned address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://alastairs-place.net/2006/11/dmg-vulnerability/.

**参考链接 / References**:
- N/A

---

#### 260. CVE-2006-6062

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to cause a denial of service (crash) via a malformed UDTO HFS+ disk image, such as with "bad sectors," which triggers memory corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

**参考链接 / References**:
- N/A

---

#### 261. CVE-2006-6126

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X allows local users to cause a denial of service (memory corruption) via a crafted Mach-O binary with a malformed load_command data structure.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://projects.info-pull.com/mokb/MOKB-23-11-2006.html.

**参考链接 / References**:
- N/A

---

#### 262. CVE-2006-6127

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X kernel allows local users to cause a denial of service via a process that uses kevent to register a queue and an event, then fork a child process that uses kevent to register an event for the same queue as the parent.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=307041.

**参考链接 / References**:
- N/A

---

#### 263. CVE-2006-6129

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in the fatfile_getarch2 in Apple Mac OS X allows local users to cause a denial of service and possibly execute arbitrary code via a crafted Mach-O Universal program that triggers memory corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

**参考链接 / References**:
- N/A

---

#### 264. CVE-2006-6130

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X AppleTalk allows local users to cause a denial of service (kernel panic) by calling the AIOCREGLOCALZN ioctl command with a crafted data structure on an AppleTalk socket.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

**参考链接 / References**:
- N/A

---

#### 265. CVE-2006-4396

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Apple Type Services (ATS) server in Mac OS X 10.4.8 and earlier does not securely create log files, which allows local users to create and modify arbitrary files via unspecified vectors, possibly relating to a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 266. CVE-2006-4398

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Multiple buffer overflows in the Apple Type Services (ATS) server in Mac OS X 10.4 through 10.4.8 allow local users to execute arbitrary code via crafted service requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 267. CVE-2006-4400

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Stack-based buffer overflow in the Apple Type Services (ATS) server in Mac OS 10.4.8 and earlier allow user-assisted attackers to execute arbitrary code via crafted font files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 268. CVE-2006-4402

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Heap-based buffer overflow in the Finder in Apple Mac OS X 10.4.8 and earlier allows user-assisted remote attackers to execute arbitrary code by browsing directories containing crafted .DS_Store files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 269. CVE-2006-4403

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The FTP server in Apple Mac OS X 10.4.8 and earlier, when FTP Access is enabled, will crash when a login failure occurs with a valid user name, which allows remote attackers to cause a denial of service (crash) and enumerate valid usernames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 270. CVE-2006-4404

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Installer application in Apple Mac OS X 10.4.8 and earlier, when used by a user with Admin credentials, does not authenticate the user before installing certain software requiring system privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 271. CVE-2006-4406

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in PPP on Apple Mac OS X 10.4.x up to 10.4.8 and 10.3.x up to 10.3.9, when PPPoE is enabled, allows remote attackers to execute arbitrary code via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 272. CVE-2006-4407

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.3.x up to 10.3.9 does not properly prioritize encryption ciphers when negotiating the strongest shared cipher, which causes Secure Transport to user a weaker cipher that makes it easier for remote attackers to decrypt traffic.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 273. CVE-2006-4408

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.4 through 10.4.8 allows remote attackers to cause a denial of service (resource consumption) via certain public key values in an X.509 certificate that requires extra resources during signature verification.  NOTE: this issue may be similar to CVE-2006-2940.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 274. CVE-2006-4409

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Online Certificate Status Protocol (OCSP) service in the Security Framework in Apple Mac OS X 10.4 through 10.4.8 retrieve certificate revocation lists (CRL) when an HTTP proxy is in use, which could cause the system to accept certificates that have been revoked.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 275. CVE-2006-4410

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.3.9, and 10.4.x before 10.4.7, does not properly search certificate revocation lists (CRL), which allows remote attackers to access systems by using revoked certificates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 276. CVE-2006-4411

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The VPN service in Apple Mac OS X 10.3.x through 10.3.9 and 10.4.x through 10.4.8 does not properly clean the environment when executing commands, which allows local users to gain privileges via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 277. CVE-2006-4412

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
WebKit in Apple Mac OS X 10.3.x through 10.3.9 and 10.4 through 10.4.8 allows remote attackers to execute arbitrary code via a crafted HTML file, which accesses previously deallocated objects.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

**参考链接 / References**:
- N/A

---

#### 278. CVE-2006-6238

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
The AutoFill feature in Apple Safari 2.0.4 does not properly verify that all automatically populated form fields are visible to the user, which allows remote attackers to obtain sensitive information, such as usernames and passwords, via input fields of zero width, a variant of CVE-2006-6077.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/23066.

**参考链接 / References**:
- N/A

---

#### 279. CVE-2006-6292

**严重程度 / Severity**: N/A | CVSS: 5.7
**受影响产品 / Affected Products**: apple:airport_extreme, apple:mac_os_x

**漏洞描述 / Description**:
Apple Airport Extreme firmware 0.1.27 in Mac OS X 10.4.8 on Mac mini, MacBook, and MacBook Pro with Core Duo hardware allows remote attackers to cause a denial of service (out-of-bounds memory access and kernel panic) and have possibly other security-related impact via certain beacon frames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305031.

**参考链接 / References**:
- N/A

---

#### 280. CVE-2006-5681

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
QuickTime for Java on Mac OS X 10.4 through 10.4.8, when used with Quartz Composer, allows remote attackers to obtain sensitive information (screen images) via a Java applet that accesses images that are being rendered by other embedded QuickTime objects.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304916.

**参考链接 / References**:
- N/A

---

#### 281. CVE-2006-6652

**严重程度 / Severity**: N/A | CVSS: 9.0
**受影响产品 / Affected Products**: netbsd:netbsd, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the glob implementation (glob.c) in libc in NetBSD-current before 20050914, NetBSD 2.* and 3.* before 20061203, and Apple Mac OS X before 2007-004, as used by the FTP daemon and tnftpd, allows remote authenticated users to execute arbitrary code via a long pathname that results from path expansion.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305391.

**参考链接 / References**:
- N/A

---

#### 282. CVE-1999-1113

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: eudora:internet_mail_server

**漏洞描述 / Description**:
Buffer overflow in Eudora Internet Mail Server (EIMS) 2.01 and earlier on MacOS systems allows remote attackers to cause a denial of service via a long USER command to port 106.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89258194718577&w=2.

**参考链接 / References**:
- N/A

---

#### 283. CVE-1999-1543

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
MacOS uses weak encryption for passwords that are stored in the Users & Groups Data File.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93188174906513&w=2.

**参考链接 / References**:
- N/A

---

#### 284. CVE-1999-1076

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local users to bypass the password protection of idled sessions by selecting the "Log Out" option and selecting a "Cancel" option in the dialog box for an application that attempts to verify that the user wants to log out, which returns the attacker into the locked session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94096348604173&w=2.

**参考链接 / References**:
- N/A

---

#### 285. CVE-1999-1077

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local attackers to bypass the password protection of idled sessions via the programmer's switch or CMD-PWR keyboard sequence, which brings up a debugger that the attacker can use to disable the lock.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94149318124548&w=2.

**参考链接 / References**:
- N/A

---

#### 286. CVE-1999-1528

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: prosoft_engineering:netware_client

**漏洞描述 / Description**:
ProSoft Netware Client 5.12 on Macintosh MacOS 9 does not automatically log a user out of the NDS tree when the user logs off the system, which allows other users of the same system access to the unprotected NDS session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94261444428430&w=2.

**参考链接 / References**:
- N/A

---

#### 287. CVE-2001-0766

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apache:http_server

**漏洞描述 / Description**:
Apache on MacOS X Client 10.0.3 with the HFS+ file system allows remote attackers to bypass access restrictions via a URL that contains some characters whose case is not matched by Apache's filters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-06/0090.html.

**参考链接 / References**:
- N/A

---

#### 288. CVE-2001-0921

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape 4.79 and earlier for MacOS allows an attacker with access to the browser to obtain passwords from form fields by printing the document into which the password has been typed, which is printed in cleartext.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100638816318705&w=2.

**参考链接 / References**:
- N/A

---

#### 289. CVE-2001-1565

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Point to Point Protocol daemon (pppd) in MacOS x 10.0 and 10.1 through 10.1.5 provides the username and password on the command line, which allows local users to obtain authentication information via the ps command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7750.php.

**参考链接 / References**:
- N/A

---

#### 290. CVE-2002-1773

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: mirabilis:icq_for_macos_x

**漏洞描述 / Description**:
Buffer overflow in ICQ 2.6x for MacOS X 10.0 through 10.1.2 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/254133.

**参考链接 / References**:
- N/A

---

#### 291. CVE-2002-2169

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: aol:instant_messenger

**漏洞描述 / Description**:
Cross-site scripting vulnerability AOL Instant Messenger (AIM) 4.5 and 4.7 for MacOS and Windows allows remote attackers to conduct unauthorized activities, such as adding buddies and groups to a user's buddy list, via a URL with a META HTTP-EQUIV="refresh" tag to an aim: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/282443.

**参考链接 / References**:
- N/A

---

#### 292. CVE-2003-0088

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
TruBlueEnvironment for MacOS 10.2.3 and earlier allows local users to overwrite or create arbitrary files and gain root privileges by setting a certain environment variable that is used to write debugging information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- N/A

---

#### 293. CVE-2002-1491

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:vpn_5000_client

**漏洞描述 / Description**:
The Cisco VPN 5000 Client for MacOS before 5.2.2 records the most recently used login password in plaintext when saving "Default Connection" settings, which could allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml.

**参考链接 / References**:
- N/A

---

#### 294. CVE-2003-0171

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
DirectoryServices in MacOS X trusts the PATH environment variable to locate and execute the touch command, which allows local users to execute arbitrary commands by modifying the PATH to point to a directory containing a malicious touch program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00028.html.

**参考链接 / References**:
- N/A

---

#### 295. CVE-2003-0490

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: dantz:retrospect_client

**漏洞描述 / Description**:
The installation of Dantz Retrospect Client 5.0.540 on MacOS X 10.2.6, and possibly other versions, creates critical directories and files with world-writable permissions, which allows local users to gain privileges as other users by replacing programs with malicious code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105579526026992&w=2.

**参考链接 / References**:
- N/A

---

#### 296. CVE-2003-0518

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The screen saver in MacOS X allows users with physical access to cause the screen saver to crash and gain access to the underlying session via a large number of characters in the password field, possibly triggering a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-07/0034.html.

**参考链接 / References**:
- N/A

---

#### 297. CVE-2001-1412

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
nidump on MacOS X before 10.3 allows local users to read the encrypted passwords from the password file by specifying passwd as a command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00038.html.

**参考链接 / References**:
- N/A

---

#### 298. CVE-2004-0169

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
QuickTime Streaming Server in MacOS X 10.2.8 and 10.3.2 allows remote attackers to cause a denial of service (crash) via DESCRIBE requests with long User-Agent fields, which causes an Assert error to be triggered in the BufferIsFull function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

**参考链接 / References**:
- N/A

---

#### 299. CVE-2007-3184

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: cisco:trust_agent, apple:mac_os_x

**漏洞描述 / Description**:
Cisco Trust Agent (CTA) before 2.1.104.0, when running on MacOS X, allows attackers with physical access to bypass authentication and modify System Preferences, including passwords, by invoking the Apple Menu when the Access Control Server (ACS) produces a user notification message after posture validation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/25598.

**参考链接 / References**:
- N/A

---

#### 300. CVE-2007-6456

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: planamesa:neooffice

**漏洞描述 / Description**:
Unspecified vulnerability in OpenOffice.org code in Planamesa NeoOffice 2.2.2 before Patch 4 has unknown impact and attack vectors related to MacOS 10.3.9 .odb files.  NOTE: it is not clear whether this issue is a vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://neowiki.neooffice.org/index.php/NeoOffice_Release_Notes.

**参考链接 / References**:
- N/A

---

#### 301. CVE-2016-4617

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves a sandbox escape related to launchctl process spawning in the "libxpc" component.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/96329.

**参考链接 / References**:
- N/A

---

#### 302. CVE-2016-4660

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "FontParser" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

**参考链接 / References**:
- N/A

---

#### 303. CVE-2016-4661

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ntfs" component, which misparses disk images and allows attackers to cause a denial of service via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 304. CVE-2016-4662

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleGraphicsControl" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 305. CVE-2016-4663

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "NVIDIA Graphics Drivers" component. It allows attackers to cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 306. CVE-2016-4667

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 307. CVE-2016-4669

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (MIG code mishandling and system crash) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/158874/Safari-Webkit-For-iOS-7.1.2-JIT-Optimization-Bug.html.

**参考链接 / References**:
- N/A

---

#### 308. CVE-2016-4670

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "Security" component. It allows local users to discover lengths of arbitrary passwords by reading a log.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94433.

**参考链接 / References**:
- N/A

---

#### 309. CVE-2016-4671

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds write and application crash) via a crafted PDF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 310. CVE-2016-4673

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "CoreGraphics" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

**参考链接 / References**:
- N/A

---

#### 311. CVE-2016-4674

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows local users to gain privileges or cause a denial of service (memory corruption and application crash) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 312. CVE-2016-4675

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libxpc" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

**参考链接 / References**:
- N/A

---

#### 313. CVE-2016-4678

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleSMC" component. It allows local users to gain privileges or cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 314. CVE-2016-4679

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libarchive" component, which allows remote attackers to write to arbitrary files via a crafted archive containing a symlink.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

**参考链接 / References**:
- N/A

---

#### 315. CVE-2016-4681

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Core Image" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94431.

**参考链接 / References**:
- N/A

---

#### 316. CVE-2016-4682

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted SGI file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

**参考链接 / References**:
- N/A

---

#### 317. CVE-2016-4683

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds memory access and application crash) via a crafted SGI file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94431.

**参考链接 / References**:
- N/A

---

#### 318. CVE-2016-4688

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:tvos, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94572.

**参考链接 / References**:
- N/A

---

#### 319. CVE-2016-4691

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 320. CVE-2016-4693

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which makes it easier for attackers to bypass cryptographic protection mechanisms by leveraging use of the 3DES cipher.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 321. CVE-2016-4721

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "IDS - Connectivity" component, which allows man-in-the-middle attackers to spoof calls via a "switch caller" notification.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94429.

**参考链接 / References**:
- N/A

---

#### 322. CVE-2016-4780

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Thunderbolt" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207275.

**参考链接 / References**:
- N/A

---

#### 323. CVE-2016-7577

**严重程度 / Severity**: LOW | CVSS: 3.7
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "FaceTime" component, which allows remote attackers to trigger memory corruption and obtain audio data from a call that appeared to have ended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94429.

**参考链接 / References**:
- N/A

---

#### 324. CVE-2016-7579

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. The issue involves the "CFNetwork Proxies" component, which allows man-in-the-middle attackers to spoof a proxy password authentication requirement and obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93856.

**参考链接 / References**:
- N/A

---

#### 325. CVE-2016-7580

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Mail" component, which allows remote web servers to cause a denial of service via a crafted URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94434.

**参考链接 / References**:
- N/A

---

#### 326. CVE-2016-7582

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94435.

**参考链接 / References**:
- N/A

---

#### 327. CVE-2016-7584

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "AppleMobileFileIntegrity" component, which allows remote attackers to spoof signed code by using a matching team ID.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94571.

**参考链接 / References**:
- N/A

---

#### 328. CVE-2016-7588

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreMedia Playback" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted MP4 file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 329. CVE-2016-7591

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOHIDFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 330. CVE-2016-7594

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ICU" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 331. CVE-2016-7595

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreText" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 332. CVE-2016-7596

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 333. CVE-2016-7600

**严重程度 / Severity**: MEDIUM | CVSS: 6.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "OpenPAM" component, which allows local users to obtain sensitive information by leveraging mishandling of failed PAM authentication by a sandboxed app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 334. CVE-2016-7602

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 335. CVE-2016-7603

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreStorage" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 336. CVE-2016-7604

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreCapture" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 337. CVE-2016-7605

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 338. CVE-2016-7606

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 339. CVE-2016-7607

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows attackers to obtain sensitive information from kernel memory via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 340. CVE-2016-7608

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOFireWireFamily" component, which allows local users to obtain sensitive information from kernel memory via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 341. CVE-2016-7609

**严重程度 / Severity**: MEDIUM | CVSS: 6.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "AppleGraphicsPowerManagement" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 342. CVE-2016-7612

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 343. CVE-2016-7613

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x, apple:safari

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app that leverages object-lifetime mishandling during process spawning.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94116.

**参考链接 / References**:
- N/A

---

#### 344. CVE-2016-7615

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows local users to cause a denial of service via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 345. CVE-2016-7616

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Disk Images" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 346. CVE-2016-7617

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (type confusion) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 347. CVE-2016-7618

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Foundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 348. CVE-2016-7619

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "libarchive" component, which allows local users to write to arbitrary files via vectors related to symlinks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 349. CVE-2016-7620

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOSurface" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 350. CVE-2016-7621

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:watchos, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 351. CVE-2016-7622

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Grapher" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 352. CVE-2016-7624

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOAcceleratorFamily" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 353. CVE-2016-7625

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 354. CVE-2016-7627

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreGraphics" component. It allows attackers to cause a denial of service (NULL pointer dereference and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 355. CVE-2016-7628

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Assets" component, which allows local users to bypass intended permission restrictions and change a downloaded mobile asset via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 356. CVE-2016-7629

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "kext tools" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 357. CVE-2016-7633

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Directory Services" component. It allows local users to gain privileges or cause a denial of service (use-after-free) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

**参考链接 / References**:
- N/A

---

#### 358. CVE-2016-7636

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows man-in-the-middle attackers to cause a denial of service (application crash) via vectors related to OCSP responder URLs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 359. CVE-2016-7637

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to gain privileges or cause a denial of service (memory corruption) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 360. CVE-2016-7643

**严重程度 / Severity**: HIGH | CVSS: 8.1
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information from process memory or cause a denial of service (out-of-bounds read and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 361. CVE-2016-7644

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94904.

**参考链接 / References**:
- N/A

---

#### 362. CVE-2016-7655

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreMedia External Displays" component. It allows local users to gain privileges or cause a denial of service (type confusion) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94906.

**参考链接 / References**:
- N/A

---

#### 363. CVE-2016-7657

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows attackers to obtain sensitive information from kernel memory via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 364. CVE-2016-7658

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 365. CVE-2016-7659

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 366. CVE-2016-7660

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "syslog" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 367. CVE-2016-7661

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "Power Management" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94906.

**参考链接 / References**:
- N/A

---

#### 368. CVE-2016-7662

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows remote attackers to spoof certificates via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 369. CVE-2016-7663

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreFoundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

**参考链接 / References**:
- N/A

---

#### 370. CVE-2016-7667

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to cause a denial of service via a crafted string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207422.

**参考链接 / References**:
- N/A

---

#### 371. CVE-2016-7714

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207422.

**参考链接 / References**:
- N/A

---

#### 372. CVE-2016-7742

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "xar" component, which allows remote attackers to execute arbitrary code via a crafted archive that triggers use of uninitialized memory locations.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207423.

**参考链接 / References**:
- N/A

---

#### 373. CVE-2016-7761

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "WiFi" component, which allows local users to obtain sensitive network-configuration information by leveraging global storage.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207423.

**参考链接 / References**:
- N/A

---

#### 374. CVE-2017-2353

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

**参考链接 / References**:
- N/A

---

#### 375. CVE-2017-2357

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "IOAudioFamily" component. It allows attackers to obtain sensitive kernel memory-layout information via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

**参考链接 / References**:
- N/A

---

#### 376. CVE-2017-2358

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Graphics Drivers" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

**参考链接 / References**:
- N/A

---

#### 377. CVE-2017-2360

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, webkitgtk:webkitgtk\+, apple:tvos, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2.1 is affected. macOS before 10.12.3 is affected. tvOS before 10.1.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95729.

**参考链接 / References**:
- N/A

---

#### 378. CVE-2017-2361

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Help Viewer" component, which allows XSS attacks via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

**参考链接 / References**:
- N/A

---

#### 379. CVE-2017-2370

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2.1 is affected. macOS before 10.12.3 is affected. tvOS before 10.1.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (buffer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95731.

**参考链接 / References**:
- N/A

---

#### 380. CVE-2016-9892

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: eset:endpoint_antivirus, eset:endpoint_security

**漏洞描述 / Description**:
The esets_daemon service in ESET Endpoint Antivirus for macOS before 6.4.168.0 and Endpoint Security for macOS before 6.4.168.0 does not properly verify X.509 certificates from the edf.eset.com SSL server, which allows man-in-the-middle attackers to spoof this server and provide crafted responses to license activation requests via a self-signed certificate.  NOTE: this issue can be combined with CVE-2016-0718 to execute arbitrary code remotely as root.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/141350/ESET-Endpoint-Antivirus-6-Remote-Code-Execution.html.

**参考链接 / References**:
- N/A

---

#### 381. CVE-2016-7585

**严重程度 / Severity**: MEDIUM | CVSS: 6.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves mishandling of DMA in the "EFI" component. It allows physically proximate attackers to discover the FileVault 2 encryption password via a crafted Thunderbolt adapter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 382. CVE-2017-2379

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Carbon" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted .dfont file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 383. CVE-2017-2381

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "sudo" component. It allows remote authenticated users to gain privileges by leveraging membership in the admin group on a network directory server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 384. CVE-2017-2382

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_server

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS Server before 5.3 is affected. The issue involves the "Wiki Server" component. It allows remote attackers to enumerate user accounts via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97128.

**参考链接 / References**:
- N/A

---

#### 385. CVE-2017-2388

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireFamily" component. It allows attackers to cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 386. CVE-2017-2390

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves symlink mishandling in the "libarchive" component. It allows local users to change arbitrary directory permissions via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 387. CVE-2017-2391

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: apple:pages, apple:keynote, apple:numbers

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. Pages before 6.1, Numbers before 4.1, and Keynote before 7.1 on macOS and Pages before 3.1, Numbers before 3.1, and Keynote before 3.1 on iOS are affected. The issue involves the "Export" component. It allows users to bypass iWork PDF password protection by leveraging use of 40-bit RC4.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97126.

**参考链接 / References**:
- N/A

---

#### 388. CVE-2017-2398

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97147.

**参考链接 / References**:
- N/A

---

#### 389. CVE-2017-2401

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 390. CVE-2017-2402

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves mishandling of profile uninstall actions in the "MCX Client" component when a profile has multiple payloads. It allows remote attackers to bypass intended access restrictions by leveraging Active Directory certificate trust that should not have remained.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 391. CVE-2017-2403

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Printing" component. A format-string vulnerability allows remote attackers to execute arbitrary code via a crafted ipp: or ipps: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 392. CVE-2017-2406

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 393. CVE-2017-2407

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 394. CVE-2017-2408

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOATAFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 395. CVE-2017-2409

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Menus" component. It allows attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 396. CVE-2017-2410

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 397. CVE-2017-2413

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "QuickTime" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted media file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 398. CVE-2017-2416

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted image file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 399. CVE-2017-2417

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreGraphics" component. It allows remote attackers to cause a denial of service (infinite recursion) via a crafted image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 400. CVE-2017-2418

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Hypervisor" component. It allows guest OS users to obtain sensitive information from the CR8 control register via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 401. CVE-2017-2420

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 402. CVE-2017-2421

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "AppleGraphicsPowerManagement" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 403. CVE-2017-2422

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Multi-Touch" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 404. CVE-2017-2423

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. The issue involves the "Security" component. It allows remote attackers to bypass intended access restrictions by leveraging a successful result from a SecKeyRawVerify API call with an empty signature.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97147.

**参考链接 / References**:
- N/A

---

#### 405. CVE-2017-2425

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "SecurityFoundation" component. A double free vulnerability allows remote attackers to execute arbitrary code via a crafted certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 406. CVE-2017-2426

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "iBooks" component. It allows remote attackers to obtain sensitive information from local files via a file: URL in an iBooks file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 407. CVE-2017-2427

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 408. CVE-2017-2428

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves nghttp2 before 1.17.0 in the "HTTPProtocol" component. It allows remote HTTP/2 servers to have an unspecified impact via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97146.

**参考链接 / References**:
- N/A

---

#### 409. CVE-2017-2429

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "FinderKit" component. It allows remote attackers to bypass intended access restrictions in opportunistic circumstances by leveraging unexpected permission changes during an iCloud Sharing Send Link action.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 410. CVE-2017-2430

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 411. CVE-2017-2431

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "CoreMedia" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .mov file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 412. CVE-2017-2432

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 413. CVE-2017-2435

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 414. CVE-2017-2436

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireAVC" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 415. CVE-2017-2437

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireAVC" component. It allows local users to gain privileges or cause a denial of service (memory corruption) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 416. CVE-2017-2438

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "AppleRAID" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 417. CVE-2017-2439

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 418. CVE-2017-2440

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (integer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 419. CVE-2017-2441

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "libc++abi" component. A use-after-free vulnerability allows remote attackers to execute arbitrary code via a crafted C++ app that is mishandled during demangling.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 420. CVE-2017-2443

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 421. CVE-2017-2448

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. The issue involves the "Keychain" component. It allows man-in-the-middle attackers to bypass an iCloud Keychain secret protection mechanism by leveraging lack of authentication for OTR packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97134.

**参考链接 / References**:
- N/A

---

#### 422. CVE-2017-2449

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- N/A

---

#### 423. CVE-2017-2450

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 424. CVE-2017-2451

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Security" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (buffer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---

#### 425. CVE-2017-2456

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- N/A

---
