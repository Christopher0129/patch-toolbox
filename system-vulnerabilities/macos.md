# Macos 系统漏洞知识库 | Macos System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 952**

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

---

#### 2. CVE-1999-0141

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: netscape:navigator

**漏洞描述 / Description**:
Java Bytecode Verifier allows malicious applets to execute arbitrary commands as the user of the applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/134.

---

#### 3. CVE-1999-1262

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Java in Netscape 4.5 does not properly restrict applets from connecting to other hosts besides the one from which the applet was loaded, which violates the Java security model and could allow remote attackers to conduct unauthorized activities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/12231.

---

#### 4. CVE-1999-1015

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:appleshare_mail_server

**漏洞描述 / Description**:
Buffer overflow in Apple AppleShare Mail Server 5.0.3 on MacOS 8.1 and earlier allows a remote attacker to cause a denial of service (crash) via a long HELO command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89200657216213&w=2.

---

#### 5. CVE-1999-1393

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Control Panel "Password Security" option for Apple Powerbooks allows attackers with physical access to the machine to bypass the security by booting it with an emergency startup disk and using a disk editor to modify the on/off toggle or password in the aaaaaaaAPWD file, which is normally inaccessible.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://freaky.staticusers.net/macsec/data/powerbooksecurity-data.html.

---

#### 6. CVE-1999-1412

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apache:http_server, apple:macos

**漏洞描述 / Description**:
A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/14215.

---

#### 7. CVE-1999-0793

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer allows remote attackers to read files by redirecting data to a Javascript applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-043.

---

#### 8. CVE-2000-0237

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: netscape:enterprise_server

**漏洞描述 / Description**:
Netscape Enterprise Server with Web Publishing enabled allows remote attackers to list arbitrary directories via a GET request for the /publisher directory, which provides a Java applet that allows the attacker to browse the directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1075.

---

#### 9. CVE-2000-0265

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: panda:panda_security

**漏洞描述 / Description**:
Panda Security 3.0 allows users to uninstall the Panda software via its Add/Remove Programs applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://updates.pandasoftware.com/docs/us/Avoidvulnerability.zip.

---

#### 10. CVE-2000-0266

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.01 allows remote attackers to bypass the cross frame security policy via a malicious applet that interacts with the Java JSObject to modify the DOM properties to set the IFRAME to an arbitrary Javascript URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1121.

---

#### 11. CVE-2000-0346

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:appleshare

**漏洞描述 / Description**:
AppleShare IP 6.1 and later allows a remote attacker to read potentially sensitive information via an invalid range request to the web server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://asu.info.apple.com/swupdates.nsf/artnum/n11670.

---

#### 12. CVE-2000-0676

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape Communicator and Navigator 4.04 through 4.74 allows remote attackers to read arbitrary files by using a Java applet to open a connection to a URL using the "file", "http", "https", and "ftp" protocols, as demonstrated by Brown Orifice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.FreeBSD.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00:39.netscape.asc.

---

#### 13. CVE-2000-0711

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: netscape:communicator, microsoft:virtual_machine

**漏洞描述 / Description**:
Netscape Communicator does not properly prevent a ServerSocket object from being created by untrusted entities, which allows remote attackers to create a server on the victim's system via a malicious applet, as demonstrated by Brown Orifice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-15.html.

---

#### 14. CVE-2000-0889

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Two Sun security certificates have been compromised, which could allow attackers to insert malicious code such as applets and make it appear that it is signed by Sun.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.Sun.COM/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/198&type=0&nav=sec.sba.

---

#### 15. CVE-2001-0068

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_runtime_for_java

**漏洞描述 / Description**:
Mac OS Runtime for Java (MRJ) 2.2.3 allows remote attackers to use malicious applets to read files outside of the CODEBASE context via the ARCHIVE applet parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-12/0241.html.

---

#### 16. CVE-2001-0137

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Windows Media Player 7 allows remote attackers to execute malicious Java applets in Internet Explorer clients by enclosing the applet in a skin file named skin.wmz, then referencing that skin in the codebase parameter to an applet tag, aka the Windows Media Player Skins File Download" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97958100816503&w=2.

---

#### 17. CVE-2001-0324

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_2000

**漏洞描述 / Description**:
Windows 98 and Windows 2000 Java clients allow remote attackers to cause a denial of service via a Java applet that opens a large number of UDP sockets, which prevents the host from establishing any additional UDP connections, and possibly causes a crash.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/win2ksecadvice/2001-q1/0060.html.

---

#### 18. CVE-2001-1026

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: trend_micro:interscan_applettrap

**漏洞描述 / Description**:
Trend Micro InterScan AppletTrap 2.0 does not properly filter URLs when they are modified in certain ways such as (1) using a double slash (//) instead of a single slash, (2) URL-encoded characters, (3) requesting the IP address instead of the domain name, or (4) using a leading 0 in an octet of an IP address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-07/0129.html.

---

#### 19. CVE-2001-1008

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:java_plug-in, sun:jre

**漏洞描述 / Description**:
Java Plugin 1.4 for JRE 1.3 executes signed applets even if the certificate is expired, which could allow remote attackers to conduct unauthorized activities via an applet that has been signed by an expired certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-08/0359.html.

---

#### 20. CVE-2001-1254

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: com2001:alexis_server

**漏洞描述 / Description**:
Web Access component for COM2001 Alexis 2.0 and 2.1 in InternetPBX sends username and voice mail passwords in the clear via a Java applet that sends the information to port 8888 of the server, which could allow remote attackers to steal the passwords via sniffing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/217200.

---

#### 21. CVE-2001-0806

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple MacOS X 10.0 and 10.1 allow a local user to read and write to a user's desktop folder via insecure default permissions for the Desktop when it is created in some languages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99358249631139&w=2.

---

#### 22. CVE-2001-1480

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jdk, sun:jre, apple:mac_os_runtime_for_java, sun:sdk

**漏洞描述 / Description**:
Java Runtime Environment (JRE) and SDK 1.2 through 1.3.0_04 allows untrusted applets to access the system clipboard.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/10/msg00120.html.

---

#### 23. CVE-2001-1575

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:personal_web_sharing

**漏洞描述 / Description**:
Apple Personal Web Sharing (PWS) 1.1, 1.5, and 1.5.5, when Web Sharing authentication is enabled, allows remote attackers to cause a denial of service via a long password, possibly due to a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00409.html.

---

#### 24. CVE-2002-1601

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: adobe:photodeluxe

**漏洞描述 / Description**:
The Connectables feature in Adobe PhotoDeluxe 3.1 prepends the Adobe directory to the CLASSPATH environment variable, which allows applets to run with higher privileges and remote attackers to gain privileges via an HTML e-mail message or a web page.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/116875.

---

#### 25. CVE-2002-0120

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: palm:palm_desktop

**漏洞描述 / Description**:
Apple Palm Desktop 4.0b76 and 4.0b77 creates world-readable backup files and folders when a hotsync is performed, which could allow a local user to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250093.

---

#### 26. CVE-2002-0153

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Internet Explorer 5.1 for Macintosh allows remote attackers to bypass security checks and invoke local AppleScripts within a specific HTML element, aka the "Local Applescript Invocation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8851.php.

---

#### 27. CVE-2002-0252

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.01 and 5.02 allows remote web servers to execute arbitrary code via a response containing a long Content-Type MIME header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101320742616105&w=2.

---

#### 28. CVE-2002-0676

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
SoftwareUpdate for MacOS 10.1.x does not use authentication when downloading a software update, which could allow remote attackers to execute arbitrary code by posing as the Apple update server via techniques such as DNS spoofing or cache poisoning, and supplying Trojan Horse updates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cunap.com/~hardingr/projects/osx/exploit.html.

---

#### 29. CVE-2002-0376

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime 5.0 ActiveX component allows remote attackers to execute arbitrary code via a long pluginspage field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293095.

---

#### 30. CVE-2002-0976

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 4.0 and later allows remote attackers to read arbitrary files via a web page that accesses a legacy XML Datasource applet (com.ms.xml.dso.XMLDSO.class) and modifies the base URL to point to the local system, which is trusted by the applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102960731805373&w=2.

---

#### 31. CVE-2002-1898

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal

**漏洞描述 / Description**:
Terminal 1.3 in Apple Mac OS X 10.2 allows remote attackers to execute arbitrary commands via shell metacharacters in a telnet:// link, which is executed by Terminal.app window.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://apple.slashdot.org/apple/02/09/21/122236.shtml?tid=172.

---

#### 32. CVE-2002-2184

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: digi-net_technologies:digichat

**漏洞描述 / Description**:
Digi-Net Technologies DigiChat 3.5 allows chat users to obtain the IP addresses of other chat users via a "Showip" parameter in the chat applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5019.

---

#### 33. CVE-2002-2242

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: kismac:kismac

**漏洞描述 / Description**:
The Apple Package Manager in KisMAC 0.02a and earlier modifies file permissions of sensitive files after installation, which could allow attackers to conduct unauthorized activities on those files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1005764.

---

#### 34. CVE-2002-2248

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Buffer overflow in the sun.awt.windows.WDefaultFontCharset Java class implementation in Netscape 4.0 allows remote attackers to execute arbitrary code via an applet that calls the WDefaultFontCharset constructor with a long string and invokes the canConvert method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103834439321292&w=2.

---

#### 35. CVE-2002-2281

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: symantec:java

**漏洞描述 / Description**:
Symantec Java! JIT (Just-In-Time) Compiler for Netscape Communicator 4.0 through 4.8 allows remote attackers to execute arbitrary Java commands via an applet that uses a jump call, which is not correctly compiled by the JIT compiler.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

---

#### 36. CVE-2002-2284

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape Communicator 4.0 through 4.79 allows remote attackers to bypass JVM security and execute arbitrary Java code via an applet that loads user-supplied Java classes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103798147613151&w=2.

---

#### 37. CVE-2002-2292

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: halycon_software:iasp

**漏洞描述 / Description**:
Directory traversal vulnerability in Remote Console Applet in Halycon Software iASP 1.0.9 allows remote attackers to read arbitrary files via a .. (dot dot) in the HTTP request to port 9095.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-12/0126.html.

---

#### 38. CVE-2002-2373

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:tcp_ip_configuration_utility, apple:apple_laserwriter

**漏洞描述 / Description**:
The default configuration of the TCP/IP printer configuration utility in Apple LaserWriter 12/640 PS printer contains a blank Telnet password, which allows remote attackers to gain access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10476.php.

---

#### 39. CVE-2003-0049

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple File Protocol (AFP) in Mac OS X before 10.2.4 allows administrators to log in as other users by using the administrator password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 40. CVE-2003-0050

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via shell metacharacters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 41. CVE-2003-0051

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to obtain the physical path of the server's installation path via a NULL file parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 42. CVE-2003-0052

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to list arbitrary directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 43. CVE-2003-0053

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in parse_xml.cgi in Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to insert arbitrary script via the filename parameter, which is inserted into an error message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 44. CVE-2003-0054

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute certain code via a request to port 7070 with the script in an argument to the rtsp DESCRIBE method, which is inserted into a log file and executed when the log is viewed using a browser.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 45. CVE-2003-0055

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime_darwin_mp3_broadcaster

**漏洞描述 / Description**:
Buffer overflow in the MP3 broadcasting module of Apple Darwin Streaming Administration Server 4.1.2 and QuickTime Streaming Server 4.1.1 allows remote attackers to execute arbitrary code via a long filename.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Feb/25/applesa20030225macosx102.txt.

---

#### 46. CVE-2003-0168

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime Player 5.x and 6.0 for Windows allows remote attackers to execute arbitrary code via a long QuickTime URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q1/0166.html.

---

#### 47. CVE-2003-0111

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine, microsoft:windows_2000_terminal_services, microsoft:windows_2000

**漏洞描述 / Description**:
The ByteCode Verifier component of Microsoft Virtual Machine (VM) build 5.0.3809 and earlier, as used in Windows and Internet Explorer, allows remote attackers to bypass security checks and execute arbitrary code via a malicious Java applet, aka "Flaw in Microsoft VM Could Enable System Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/11751.php.

---

#### 48. CVE-2003-0420

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Information leak in dsimportexport for Apple Macintosh OS X Server 10.2.6 allows local users to obtain the username and password of the account running the tool.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/9025/.

---

#### 49. CVE-2003-0270

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:802.11n

**漏洞描述 / Description**:
The administration capability for Apple AirPort 802.11 wireless access point devices uses weak encryption (XOR with a fixed key) for protecting authentication credentials, which could allow remote attackers to obtain administrative access via sniffing when the capability is available via Ethernet or non-WEP connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8773.

---

#### 50. CVE-2003-0379

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
Unknown vulnerability in Apple File Service (AFP Server) for Mac OS X Server, when sharing files on a UFS or re-shared NFS volume, allows remote attackers to overwrite arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00030.html.

---

#### 51. CVE-2003-0421

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 52. CVE-2003-0422

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via a request to view_broadcast.cgi that does not contain the required parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 53. CVE-2003-0423

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to obtain the source code for parseable files via the filename parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 54. CVE-2003-0424

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to obtain the source code for scripts by appending encoded space (%20) or . (%2e) characters to an HTTP request for the script, e.g. view_broadcast.cgi.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 55. CVE-2003-0425

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Directory traversal vulnerability in Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to read arbitrary files via a ... (triple dot) in an HTTP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 56. CVE-2003-0426

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
The installation of Apple QuickTime / Darwin Streaming Server before 4.1.3f starts the administration server with a "Setup Assistant" page that allows remote attackers to set the administrator password and gain privileges before the real administrator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 57. CVE-2003-0502

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0040.html.

---

#### 58. CVE-2003-0975

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:safari, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.1 on Mac OS X 10.3.1 and Mac OS X 10.2.8 allows remote attackers to steal user cookies from another domain via a link with a hex-encoded null character (%00) followed by the target domain.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 59. CVE-2003-0885

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: xscreensaver:xscreensaver

**漏洞描述 / Description**:
Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugs.gentoo.org/show_bug.cgi?id=41253.

---

#### 60. CVE-2003-1091

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime_broadcaster

**漏洞描述 / Description**:
Integer overflow in MP3Broadcaster for Apple QuickTime/Darwin Streaming Server 4.1.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via malformed ID3 tags in MP3 files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-05/0245.html.

---

#### 61. CVE-2003-1123

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jre, sun:jdk

**漏洞描述 / Description**:
Sun Java Runtime Environment (JRE) and SDK 1.4.0_01 and earlier allows untrusted applets to access certain information within trusted applets, which allows attackers to bypass the restrictions of the Java security model.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/8958.

---

#### 62. CVE-2003-1413

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
parse_xml.cgi in Apple Darwin Streaming Server 4.1.1 allows remote attackers to determine the existence of arbitrary files by using ".." sequences in the filename parameter and comparing the resulting error messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

---

#### 63. CVE-2003-1414

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Directory traversal vulnerability in parse_xml.cg Apple Darwin Streaming Server 4.1.2 and Apple Quicktime Streaming Server 4.1.1 allows remote attackers to read arbitrary files via a ... (triple dot) in the filename parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securityreason.com/securityalert/3260.

---

#### 64. CVE-2003-1516

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: sun:java_plug-in

**漏洞描述 / Description**:
The org.apache.xalan.processor.XSLProcessorVersion class in Java Plug-in 1.4.2_01 allows signed and unsigned applets to share variables, which violates the Java security model and could allow remote attackers to read or write data belonging to a signed applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/341815.

---

#### 65. CVE-2003-0601

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Workgroup Manager in Apple Mac OS X Server 10.2 through 10.2.6 does not disable a password for a new account before it is saved for the first time, which allows remote attackers to gain unauthorized access via the new account before it is saved.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25631.

---

#### 66. CVE-2003-1006

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in cd9660.util in Apple Mac OS X 10.0 through 10.3.2 and Apple Mac OS X Server 10.0 through 10.3.2 may allow local users to execute arbitrary code via a long command line parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 67. CVE-2003-1007

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AppleFileServer (AFS) in Apple Mac OS X 10.2.8 and 10.3.2 does not properly handle certain malformed requests, with unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 68. CVE-2003-1009

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Directory Services in Apple Mac OS X 10.0.2, 10.0.3, 10.2.8, 10.3.2 and Apple Mac OS X Server 10.2 through 10.3.2 accepts authentication server information from unknown LDAP or NetInfo sources as provided by a malicious DHCP server, which allows remote attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=32478.

---

#### 69. CVE-2003-1011

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.0 through 10.2.8 allows local users with a USB keyboard to gain unauthorized access by holding down the CTRL and C keys when the system is booting, which crashes the init process and leaves the user in a root shell.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 70. CVE-2003-0514

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari allows remote attackers to bypass intended cookie access restrictions on a web application via "%2e%2e" (encoded dot dot) directory traversal sequences in a URL, which causes Safari to send the cookie outside the specified URL subsets, e.g. to a vulnerable application that runs on the same server as the target application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0056.html.

---

#### 71. CVE-2004-0430

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in AppleFileServer for Mac OS X 10.3.3 and earlier allows remote attackers to execute arbitrary code via a LoginExt packet for a Cleartext Password User Authentication Method (UAM) request with a PathName argument that includes an AFPName type string that is longer than the associated length field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00049.html.

---

#### 72. CVE-2004-0431

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime (QuickTime.qts) before 6.5.1 allows attackers to execute arbitrary code via a large "number of entries" field in the sample-to-chunk table data for a .mov movie file, which leads to a heap-based buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00048.html.

---

#### 73. CVE-2004-0723

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
Microsoft Java virtual machine (VM) 5.0.0.3810 allows remote attackers to bypass sandbox restrictions to read or write certain data between applets from different domains via the "GET/Key" and "PUT/Key/Value" commands, aka "cross-site Java."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=108948405808522&w=2.

---

#### 74. CVE-2004-0518

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in AppleFileServer for Mac OS X 10.3.4, related to "the use of SSH and reporting errors," has unknown impact and attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

---

#### 75. CVE-2004-0823

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, openldap:openldap, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenLDAP 1.0 through 2.1.19, as used in Apple Mac OS 10.3.4 and 10.3.5 and possibly other operating systems, may allow certain authentication schemes to use hashed (crypt) passwords in the userPassword attribute as if they were plaintext passwords, which allows remote attackers to re-use hashed passwords without decrypting them.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

---

#### 76. CVE-2004-0831

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mcafee:virusscan

**漏洞描述 / Description**:
McAfee VirusScan 4.5.1 does not drop SYSTEM privileges before allowing users to browse for files via the "System Scan" properties of the System Tray applet, which could allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=109526269429728&w=2.

---

#### 77. CVE-2004-1121

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.0 through 1.2.3 allows remote attackers to spoof the URL displayed in the status bar via TABLE tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 78. CVE-2004-1081

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
The Application Framework (AppKit) for Apple Mac OS X 10.2.8 and 10.3.6 does not properly restrict access to a secure text input field, which allows local users to read keyboard input from other applications within the same window session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 79. CVE-2004-1084

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+, which bypass Apache file handles.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 80. CVE-2004-1085

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Human Interface Toolbox (HIToolBox) for Apple Mac 0S X 10.3.6 allows local users to exit applications via the force-quit key combination, even when the system is running in kiosk mode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 81. CVE-2004-1086

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:mac_os_x, apple:mac_os_x_server, apple:quicktime_streaming_server

**漏洞描述 / Description**:
Buffer overflow in PSNormalizer for Apple Mac OS X 10.3.6 allows remote attackers to execute arbitrary code via a crafted PostScript input file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 82. CVE-2004-1087

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Terminal for Apple Mac OS X 10.3.6 may indicate that "Secure Keyboard Entry" is enabled even when it is not, which could result in a false sense of security for the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 83. CVE-2004-1088

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Postfix server for Apple Mac OS X 10.3.6, when using CRAM-MD5, allows remote attackers to send mail without authentication by replaying authentication information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 84. CVE-2004-1089

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Apple Mac OS X 10.3.6 server, when using Kerberos authentication and Cyrus IMAP allows local users to access mailboxes of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 85. CVE-2004-1083

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:darwin_streaming_server, apple:quicktime_streaming_server, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apache for Apple Mac OS X 10.2.8 and 10.3.6 restricts access to files in a case sensitive manner, but the Apple HFS+ filesystem accesses files in a case insensitive manner, which allows remote attackers to read .DS_Store files and files beginning with ".ht" using alternate capitalization.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

---

#### 86. CVE-2004-0622

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.3.4, 10.4, 10.5, and possibly other versions does not properly clear memory for login (aka Loginwindow.app), Keychain, or FileVault passwords, which could allow the root user or an attacker with physical access to obtain sensitive information by reading memory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://citp.princeton.edu/pub/coldboot.pdf.

---

#### 87. CVE-2004-1145

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ethereal_group:ethereal, suse:suse_linux, redhat:enterprise_linux, sgi:propack, redhat:enterprise_linux_desktop

**漏洞描述 / Description**:
Multiple vulnerabilities in Konqueror in KDE 3.3.1 and earlier (1) allow access to restricted Java classes via JavaScript and (2) do not properly restrict access to certain Java classes from the Java applet, which allows remote attackers to bypass sandbox restrictions and read or write arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110356286722875&w=2.

---

#### 88. CVE-2004-0873

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:ichat_av, apple:ichat

**漏洞描述 / Description**:
Apple iChat AV 2.1, AV 2.0, and 1.0.1 allows remote attackers to execute arbitrary programs via a "link" that references the program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Sep/msg00001.html.

---

#### 89. CVE-2004-0429

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability related to "the handling of large requests" in RAdmin for Apple Mac OS X 10.3.3 and Mac OS X 10.2.8 may allow attackers to have unknown impact via unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/May/msg00000.html.

---

#### 90. CVE-2004-1398

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: roxio:toast

**漏洞描述 / Description**:
Format string vulnerability in prelink.c in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via format string specifiers in the extension argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

---

#### 91. CVE-2004-1489

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: opera:opera_browser

**漏洞描述 / Description**:
Opera 7.54 and earlier does not properly limit an applet's access to internal Java packages from Sun, which allows remote attackers to gain sensitive information, such as user names and the installation directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029044.html.

---

#### 92. CVE-2004-1753

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: mozilla:mozilla, mozilla:firefox, netscape:navigator

**漏洞描述 / Description**:
The Apple Java plugin, as used in Netscape 7.1 and 7.2, Mozilla 1.7.2, and Firefox 0.9.3 on MacOS X 10.3.5, when tabbed browsing is enabled, does not properly handle SetWindow(NULL) calls, which allows Java applets from one tab to draw to other tabs and facilitates phishing attacks that spoof tabs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bugzilla.mozilla.org/show_bug.cgi?id=162134.

---

#### 93. CVE-2004-2280

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ibm:lotus_notes

**漏洞描述 / Description**:
Buffer overflow in IBM Lotus Notes 6.5.x before 6.5.3 and 6.0.x before 6.0.5 allows remote attackers to cause a denial of service (crash) via unknown vectors related to Java applets, as identified by KSPR62F4KN.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

---

#### 94. CVE-2004-2281

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: ibm:lotus_notes

**漏洞描述 / Description**:
Multiple unknown vulnerabilities in IBM Lotus Notes 6.5.x before 6.5.4 and 6.0.x before 6.0.5 have unknown impact and attack vectors, related to Java applets, as identified by (1) KSPR5YS6GR and (2) KSPR62F4D3.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12046.

---

#### 95. CVE-2004-2359

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: dell:truemobile_1300_wlan_mini-pci_card_util_trayapplet

**漏洞描述 / Description**:
Dell TrueMobile 1300 WLAN Mini-PCI Card Util TrayApplet 3.10.39.0 does not properly drop SYSTEM privileges when started from the systray applet, which allows local users to gain privileges by accessing the Help functionality.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2004-q1/0042.html.

---

#### 96. CVE-2004-2367

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: texas_imperial_software:wftpd, texas_imperial_software:wftpd_pro

**漏洞描述 / Description**:
The Control Panel applet in WFTPD and WFTPD Pro 3.21 R1 and R2 allows remote authenticated users to cause a denial of service (crash) via a long FTP command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/11160/.

---

#### 97. CVE-2004-0926

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server, easy_software_products:cups

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime on Mac OS 10.2.8 through 10.3.5 may allow remote attackers to execute arbitrary code via a certain BMP image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

---

#### 98. CVE-2004-0962

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:apple_remote_desktop

**漏洞描述 / Description**:
Apple Remote Desktop Client 1.2.4 executes a GUI application as root when it is started by an Apple Remote Desktop Administrator application, which allows remote authenticated users to execute arbitrary code when loginwindow is active via Fast User Switching.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00002.html.

---

#### 99. CVE-2004-0988

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow on Apple QuickTime before 6.5.2, when running on Windows systems, allows remote attackers to cause a denial of service (memory consumption) via certain inputs that cause a large memory operation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00001.html.

---

#### 100. CVE-2004-1029

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: symantec:enterprise_firewall, gentoo:linux, sun:jre, hp:java_sdk-rte, sun:jdk

**漏洞描述 / Description**:
The Sun Java Plugin capability in Java 2 Runtime Environment (JRE) 1.4.2_01, 1.4.2_04, and possibly earlier versions, does not properly restrict access between Javascript and Java applets during data transfer, which allows remote attackers to load unsafe classes and execute arbitrary code by using the reflection API to access private Java packages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jouko.iki.fi/adv/javaplugin.html.

---

#### 101. CVE-2005-0043

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Buffer overflow in Apple iTunes 4.7 allows remote attackers to execute arbitrary code via a long URL in (1) .m3u or (2) .pls playlist files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00000.html.

---

#### 102. CVE-2005-0289

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:airport_extreme, apple:airport_express

**漏洞描述 / Description**:
Apple AirPort Express prior to 6.1.1 and Extreme prior to 5.5.1, configured as a Wireless Data Service (WDS), allows remote attackers to cause a denial of service (device freeze) by connecting to UDP port 161 and before link-state change occurs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-January/030832.html.

---

#### 103. CVE-2005-0340

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
Integer signedness error in Apple File Service (AFP Server) allows remote attackers to cause a denial of service (application crash) via a negative UAM string length in a FPLoginExt packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

---

#### 104. CVE-2005-0341

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.2.4 does not obey the Content-type field in the HTTP header and renders text as HTML, which allows remote attackers to inject arbitrary web script or HTML and perform cross-site scripting (XSS) attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110756965213819&w=2.

---

#### 105. CVE-2005-0976

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, hmdt:shiira, omnigroup:omniweb

**漏洞描述 / Description**:
AppleWebKit (WebCore and WebKit), as used in multiple products such as Safari 1.2 and OmniGroup OmniWeb 5.1, allows remote attackers to read arbitrary files via the XMLHttpRequest Javascript component, as demonstrated using automatically mounted disk images and file:// URLs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

---

#### 106. CVE-2005-1331

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:applescript, apple:mac_os_x_server

**漏洞描述 / Description**:
The AppleScript Editor in Mac OS X 10.3.9 does not properly display script code for an applescript: URI, which can result in code that is different than the actual code that would be run, which could allow remote attackers to trick users into executing malicious code via certain URI characters such as NULL, control characters, and homographs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

---

#### 107. CVE-2005-1337

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Help Viewer 2.0.7 and 3.0.0 in Mac OS X 10.3.9 allows remote attackers to read and execute arbitrary scrpts with less restrictive privileges via a help:// URI.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

---

#### 108. CVE-2005-1341

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal, apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Terminal 1.4.4 allows attackers to execute arbitrary commands via terminal escape sequences.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

---

#### 109. CVE-2005-1342

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:terminal

**漏洞描述 / Description**:
The x-man-page: URI handler for Apple Terminal 1.4.4 in Mac OS X 10.3.9 does not cleanse terminal escape sequences, which allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

---

#### 110. CVE-2005-1579

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime Player 7.0 on Mac OS X 10.4 allows remote attackers to obtain sensitive information via a .mov file with a Quartz Composer composition (.qtz) file that uses certain patches to read local information, then other patches to send the information to the attacker.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-05/0265.html.

---

#### 111. CVE-2005-1193

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: phpbb_group:phpbb

**漏洞描述 / Description**:
The bbencode_second_pass and make_clickable functions in bbcode.php for phpBB before 2.0.15, as used in viewtopic.php, privmsg.php, and other scripts, allow remote attackers to execute arbitrary script via a BBcode tag with a (1) javascript:, (2) applet:, (3) about:, (4) activex:, (5) chrome:, or (6) script: URI scheme, as demonstrated using the URL tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://castlecops.com/t123194-.html.

---

#### 112. CVE-2005-1248

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Buffer overflow in Apple iTunes before 4.8 allows remote attackers to execute arbitrary code via a crafted MPEG4 file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301596.

---

#### 113. CVE-2005-1472

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Certain system calls in Apple Mac OS X 10.4.1 do not properly enforce the permissions of certain directories without the POSIX read bit set, but with the execute bits set for group or other, which allows local users to list files in otherwise restricted directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

---

#### 114. CVE-2005-1408

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:keynote

**漏洞描述 / Description**:
Apple Keynote 2.0 and 2.0.1 allows remote attackers to read arbitrary files via the keynote: URI handler in a crafted Keynote presentation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00005.html.

---

#### 115. CVE-2005-1723

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
LaunchServices in Apple Mac OS X 10.4.x up to 10.4.1 does not properly mark file extensions and MIME types as unsafe if an Apple Uniform Type Identifier (UTI) is not created when the type is added to the database of unsafe types, which could allow attackers to bypass intended restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

---

#### 116. CVE-2005-1724

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
NFS on Apple Mac OS X 10.4.x up to 10.4.1 does not properly obey the -network or -mask flags for a filesystem and exports it to everyone, which allows remote attackers to bypass intended access restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

---

#### 117. CVE-2005-1725

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
launchd 106 in Apple Mac OS X 10.4.x up to 10.4.1 allows local users to overwrite arbitrary files via a symlink attack on the socket file in an insecure temporary directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

---

#### 118. CVE-2005-1727

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Apple Mac OS X 10.4.x up to 10.4.1 sets insecure world- and group-writable permissions for the (1) system cache folder and (2) Dashboard system widgets, which allows local users to conduct unauthorized file operations via "file race conditions."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

---

#### 119. CVE-2005-1728

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
MCX Client for Apple Mac OS X 10.4.x up to 10.4.1 insecurely logs Portable Home Directory credentials, which allows local users to obtain the credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

---

#### 120. CVE-2005-1473

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
SecurityAgent in Apple Mac OS X 10.4.1 allows attackers with physical access to bypass the locked screensaver and launch background applications by opening a URL from a text input field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

---

#### 121. CVE-2005-1474

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Dashboard in Apple Mac OS X 10.4.1 allows remote attackers to install widgets via Safari without prompting the user, a different vulnerability than CVE-2005-1933.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00004.html.

---

#### 122. CVE-2005-1933

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Dashboard in Apple Mac OS X Tiger 10.4 allows attackers to execute arbitrary commands by overriding the behavior of system widgets via a user widget with the same bundle identifier (CFBundleIdentifier), a different vulnerability than CVE-2005-1474.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/983429.

---

#### 123. CVE-2005-2195

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
Apple Darwin Streaming Server 5.5 and earlier allows remote attackers to cause a denial of service (application crash) via a URL with a filename containing a .cgi extension and an MS-DOS device name such as AUX, CON, PRN, COM1, or LPT1, a different vulnerability than CVE-2003-0421 and CVE-2003-0502.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112126999514361&w=2.

---

#### 124. CVE-2005-2196

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:airport_card

**漏洞描述 / Description**:
The Apple AirPort card uses a default WEP key when not connected to a known or trusted network, which can cause it to automatically connect to a malicious network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1014522.

---

#### 125. CVE-2005-2594

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 1.3 (132) on Mac OS X 1.3.9 allows remote attackers to cause a denial of service (crash) via certain Javascript, possibly involving a function that defines a handler for itself within the function body.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/407702.

---

#### 126. CVE-2005-3018

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari allows remote attackers to cause a denial of service (application crash) via a crafted data:// URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=112715234411672&w=2.

---

#### 127. CVE-2005-2744

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in QuickDraw Manager for Apple OS X 10.3.9 and 10.4.2, as used by applications such as Safari, Mail, and Finder, allows remote attackers to execute arbitrary code via a crafted PICT file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 128. CVE-2005-2747

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in ImageIO for Apple Mac OS X 10.4.2, as used by applications such as WebCore and Safari, allows remote attackers to execute arbitrary code via a crafted GIF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 129. CVE-2005-2748

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The malloc function in the libSystem library in Apple Mac OS X 10.3.9 and 10.4.2 allows local users to overwrite arbitrary files by setting the MallocLogFile environment variable to the target file before running a setuid application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 130. CVE-2005-2524

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Safari after 2.0 in Apple Mac OS X 10.3.9 allows remote attackers to bypass domain restrictions via crafted web archives that cause Safari to render them as if they came from a different site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 131. CVE-2005-2741

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, perry_kiehtreiber:securityd, apple:mac_os_x_server

**漏洞描述 / Description**:
Authorization Services in securityd for Apple Mac OS X 10.3.9 allows local users to gain privileges by granting themselves certain rights that should be restricted to administrators.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 132. CVE-2005-2742

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
SecurityAgent in Apple Mac OS X 10.4.2, under certain circumstances, can cause the "Switch User..." button to appear even though the "Enable fast user switching" setting is disabled, which can allow attackers with physical access to gain access to the desktop and bypass the "Require password to wake this computer from sleep or screen saver" setting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 133. CVE-2005-2743

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x, apple:quicktime

**漏洞描述 / Description**:
The Java extensions for QuickTime 6.52 and earlier in Apple Mac OS X 10.3.9 allow untrusted applets to call arbitrary functions in system libraries, which allows remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 134. CVE-2005-2745

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9, when using Kerberos 5 for SMTP authentication, can include uninitialized memory in a message, which might allow remote attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 135. CVE-2005-2746

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Mail.app in Mail for Apple Mac OS X 10.3.9 and 10.4.2 includes message contents when using auto-reply rules, which could cause Mail.app to include decrypted message contents for encrypted messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Sep/msg00002.html.

---

#### 136. CVE-2005-2753

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file that causes a sign extension of the length element in a Pascal style string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

---

#### 137. CVE-2005-2754

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.0.3 allows user-assisted attackers to execute arbitrary code via a crafted MOV file with "Improper movie attributes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

---

#### 138. CVE-2005-2755

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime Player before 7.0.3 allows user-assisted attackers to cause a denial of service (crash) via a crafted file with a missing movie attribute, which leads to a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-11/0102.html.

---

#### 139. CVE-2005-2756

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime before 7.0.3 allows user-assisted attackers to overwrite memory and execute arbitrary code via a crafted PICT file that triggers an overflow during expansion.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302772.

---

#### 140. CVE-2005-3897

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.2 allows remote attackers to cause a denial of service (system slowdown) via a Javascript BODY onload event that calls the window function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=113278010907401&w=2.

---

#### 141. CVE-2005-3907

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:jdk, sun:jre

**漏洞描述 / Description**:
Unspecified vulnerability in Java Runtime Environment in Java JDK and JRE 5.0 Update 3 and earlier allows remote attackers to escape the Java sandbox and access arbitrary files or execute arbitrary applications via unknown attack vectors involving untrusted Java applets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Nov/msg00004.html.

---

#### 142. CVE-2005-3946

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: opera:opera_browser

**漏洞描述 / Description**:
Opera 8.50 allows remote attackers to cause a denial of service (crash) via a Java applet with a large string argument to the removeMember JNI method for the com.opera.JSObject class.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.illegalaccess.org/exploit/opera85/OperaApplet.html.

---

#### 143. CVE-2005-4092

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:itunes, apple:quicktime

**漏洞描述 / Description**:
Multiple heap-based buffer overflows in QuickTime.qts in Apple QuickTime Player 7.0.3 and iTunes 6.0.1 (3) and earlier allow remote attackers to cause a denial of service (crash) and execute arbitrary code via a .mov file with (1) a Movie Resource atom with a large size value, or (2) an stsd atom with a modified Sample Description Table size value, and possibly other vectors involving media files.  NOTE: item 1 was originally identified by CVE-2005-4127 for a pre-patch announcement, and item 2 was originally identified by CVE-2005-4128 for a pre-patch announcement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

---

#### 144. CVE-2005-4197

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: nortel:ssl_vpn

**漏洞描述 / Description**:
tunnelform.yaws in Nortel SSL VPN 4.2.1.6 allows remote attackers to execute arbitrary commands via a link in the a parameter, which is executed with extra privileges in a cryptographically signed Java Applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17974.

---

#### 145. CVE-2005-4217

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Perl in Apple Mac OS X Server 10.3.9 does not properly drop privileges when using the "$<" variable to set uid, which allows attackers to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

---

#### 146. CVE-2005-4504

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:safari, apple:textedit, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
The khtml::RenderTableSection::ensureRows function in KHTMLParser in Apple Mac OS X 10.4.3 and earlier, as used by Safari and TextEdit, allows remote attackers to cause a denial of service (memory consumption and application crash) via HTML files with a large ROWSPAN attribute in a TD tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

---

#### 147. CVE-2005-2194

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in the Apple Mac OS X kernel before 10.4.2 allows remote attackers to cause a denial of service (kernel panic) via a crafted TCP packet, possibly related to source routing or loose source routing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301948.

---

#### 148. CVE-2005-2340

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a crafted (1) QuickTime Image File (QTIF), (2) PICT, or (3) JPEG format image with a long data field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0392.html.

---

#### 149. CVE-2005-2527

**严重程度 / Severity**: N/A | CVSS: 1.2
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Race condition in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to corrupt files or create arbitrary files via unspecified attack vectors related to a temporary directory, possibly due to a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

---

#### 150. CVE-2005-2529

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Unspecified vulnerability in Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X allows local users to gain privileges via unspecified attack vectors relating to "the utility used to update Java shared archives."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302266.

---

#### 151. CVE-2005-2530

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Unspecified vulnerability in Java 1.3.1 before 1.3.1_16 on Apple Mac OS X allows an untrusted applet to gain privileges, related to "Mac OS X specific extensions."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

---

#### 152. CVE-2005-2738

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:java

**漏洞描述 / Description**:
Java 1.4.2 before 1.4.2 Release 2 on Apple Mac OS X does not prevent multiple programs from opening the same port as a Java ServerSocket, which allows local users to operate a Java program that intercepts network data intended for the ServerSocket of a different Java program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=302265.

---

#### 153. CVE-2005-3707

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0445.html.

---

#### 154. CVE-2005-3708

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via crafted TGA image files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303101.

---

#### 155. CVE-2005-3709

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer underflow in Apple Quicktime before 7.0.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via the Color Map Entry Size in a TGA image file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0447.html.

---

#### 156. CVE-2005-3710

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified image height and width (ImageWidth) tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0440.html.

---

#### 157. CVE-2005-3711

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a TIFF image file with modified (1) "strips" (StripByteCounts) or (2) "bands" (StripOffsets) values.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0442.html.

---

#### 158. CVE-2005-3713

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple Quicktime before 7.0.4 allows remote attackers to execute arbitrary code via a GIF image file with a crafted Netscape Navigator Application Extension Block that modifies the heap in the Picture Modifier block.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2006-01/0401.html.

---

#### 159. CVE-2005-3714

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:airport_extreme, apple:airport_express

**漏洞描述 / Description**:
The network interface for Apple AirPort Express 6.x before Firmware Update 6.3, and AirPort Extreme 5.x before Firmware Update 5.7, allows remote attackers to cause a denial of service (unresponsive interface) via malformed packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jan/msg00000.html.

---

#### 160. CVE-2005-4678

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.2 (aka 416.12) allows remote attackers to spoof the URL in the status bar via the title in an image in a link to a trusted site within a form to the malicious site.  NOTE: the provenance of this information is unknown; the details are obtained solely from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17618.

---

#### 161. CVE-2005-4866

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: ibm:db2_universal_database

**漏洞描述 / Description**:
Stack-based buffer overflow in JDBC Applet Server in IBM DB2 8.1 allows remote attackers to execute arbitrary by connecting and sending a long username, then disconnecting gracefully and reconnecting and sending a short username and an unexpected db2java.zip version, which causes a null terminator to be removed and leads to the overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=110495251101381&w=2.

---

#### 162. CVE-2006-0382

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.4.5 and allows local users to cause a denial of service (crash) via an undocumented system call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Feb/msg00000.html.

---

#### 163. CVE-2006-0848

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
The "Open 'safe' files after downloading" option in Safari on Apple Mac OS X allows remote user-assisted attackers to execute arbitrary commands by tricking a user into downloading a __MACOSX folder that contains metadata (resource fork) that invokes the Terminal, which automatically interprets the script using bash, as demonstrated using a ZIP file that contains a script with a safe file extension.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303382.

---

#### 164. CVE-2006-0396

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in Mail in Apple Mac OS X 10.4 up to 10.4.5, when patched with Security Update 2006-001, allows remote attackers to execute arbitrary code via a long Real Name value in an e-mail attachment sent in AppleDouble format, which triggers the overflow when the user double-clicks on an attachment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

---

#### 165. CVE-2006-0397

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

---

#### 166. CVE-2006-0398

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

---

#### 167. CVE-2006-0399

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Safari, LaunchServices, and/or CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows attackers to trick a user into opening an application that appears to be a safe file type. NOTE: due to the lack of specific information in the vendor advisory, it is not clear how CVE-2006-0397, CVE-2006-0398, and CVE-2006-0399 are different.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

---

#### 168. CVE-2006-0400

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
CoreTypes in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to bypass the same-origin policy and execute Javascript in other domains via unknown vectors involving "crafted archives."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303453.

---

#### 169. CVE-2006-1249

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:itunes, apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime Player 7.0.3 and 7.0.4 and iTunes 6.0.1 and 6.0.2 allows remote attackers to execute arbitrary code via a FlashPix (FPX) image that contains a field that specifies a large number of blocks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 170. CVE-2006-1552

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari, apple:mac_os_x_server, apple:mac_os_x, apple:imageio

**漏洞描述 / Description**:
Integer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.5 allows remote attackers to cause a denial of service (crash) via a crafted JPEG image with malformed JPEG metadata, as demonstrated using Safari, aka "Deja-Doom".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://drunkenblog.com/drunkenblog-archives/000760.html.

---

#### 171. CVE-2006-1986

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via a large CELLSPACING attribute in a TABLE tag, which triggers an error in KWQListIteratorImpl::KWQListIteratorImpl.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

---

#### 172. CVE-2006-1987

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 allows remote attackers to cause a denial of service and possibly execute code via an invalid FRAME tag, possibly due to (1) multiple SCROLLING attributes with no values, or (2) a SRC attribute with no value.  NOTE: due to lack of diagnosis by the researcher, it is unclear which vector is responsible.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

---

#### 173. CVE-2006-1988

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
The WebTextRenderer(WebInternal) _CG_drawRun:style:geometry: function in Apple Safari 2.0.3 allows remote attackers to cause a denial of service (application crash) via an HTML LI tag with a large VALUE attribute (list item number), which triggers a null dereference in QPainter::drawText, probably due to a failed memory allocation that uses the VALUE.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19686.

---

#### 174. CVE-2006-2019

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Mac OS X Safari 2.0.3, 1.3.1, and possibly other versions allows remote attackers to cause a denial of service (CPU consumption and crash) via a TD element with a large number in the rowspan attribute.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-April/045472.html.

---

#### 175. CVE-2006-2277

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Multiple Apple Mac OS X 10.4 applications might allow context-dependent attackers to cause a denial of service (application crash) via a crafted OpenEXR (.exr) image file, which triggers the crash when opening a folder using Finder, displaying the image in Safari, or using Preview to open the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/27780.

---

#### 176. CVE-2006-1453

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Stack-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file containing malformed font information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 177. CVE-2006-1454

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickDraw PICT image format file with malformed image data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 178. CVE-2006-1458

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime Player before 7.1 allows remote attackers to execute arbitrary code via a crafted JPEG image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 179. CVE-2006-1459

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to cause a denial of service or execute arbitrary code via a crafted QuickTime movie (.MOV).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 180. CVE-2006-1460

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime movie (.MOV), as demonstrated via a large size for a udta Atom.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 181. CVE-2006-1461

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime Flash (SWF) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 182. CVE-2006-1462

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple integer overflows in Apple QuickTime before 7.1 allow remote attackers to execute arbitrary code via a crafted QuickTime H.264 (M4V) video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 183. CVE-2006-1463

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a H.264 (M4V) video format file with a certain modified size value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 184. CVE-2006-1464

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickTime MPEG4 (M4P) video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 185. CVE-2006-1465

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted QuickTime AVI video format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 186. CVE-2006-1439

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
NSSecureTextField in AppKit in Apple Mac OS X 10.4.6 does not re-enable secure event input under certain circumstances, which could allow other applications in the window session to monitor input characters and keyboard events.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 187. CVE-2006-1440

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
BOM in Apple Mac OS X 10.3.9 and 10.4.6 allows attackers to overwrite arbitrary files via an archive that contains symbolic links.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 188. CVE-2006-1441

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in CFNetwork in Apple Mac OS X 10.4.6 allows remote attackers to execute arbitrary code via crafted chunked transfer encoding.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 189. CVE-2006-1442

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The bundle API in CoreFoundation in Apple Mac OS X 10.3.9 and 10.4.6 loads dynamic libraries even if the client application has not directly requested it, which allows attackers to execute arbitrary code from an untrusted bundle.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 190. CVE-2006-1443

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer underflow in CoreFoundation in Apple Mac OS X 10.3.9 and 10.4.6 allows context-dependent attackers to execute arbitrary code via unspecified vectors involving conversions from string to file system representation within (1) CFStringGetFileSystemRepresentation or (2) getFileSystemRepresentation:maxLength:withPath in NSFileManager, and possibly other similar API functions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 191. CVE-2006-1444

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
CoreGraphics in Apple Mac OS X 10.4.6, when "Enable access for assistive devices" is on, allows an application to bypass restrictions for secure event input and read certain events from other applications in the same window session by using Quartz Event Services.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 192. CVE-2006-1445

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the FTP server (FTPServer) in Apple Mac OS X 10.3.9 and 10.4.6 allows remote authenticated users to execute arbitrary code via vectors related to "FTP server path name handling."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 193. CVE-2006-1446

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Keychain in Apple Mac OS X 10.3.9 and 10.4.6 might allow an application to bypass a locked Keychain by first obtaining a reference to the Keychain when it is unlocked, then reusing that reference after the Keychain has been locked.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 194. CVE-2006-1447

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
LaunchServices in Apple Mac OS X 10.4.6 allows remote attackers to cause Safari to launch unsafe content via long file name extensions, which prevents Download Validation from determining which application will be used to open the file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 195. CVE-2006-1448

**严重程度 / Severity**: N/A | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Finder in Apple Mac OS X 10.3.9 and 10.4.6 allows user-assisted attackers to execute arbitrary code by tricking a user into launching an Internet Location item that appears to use a safe URL scheme, but which actually has a different and more risky scheme.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 196. CVE-2006-1449

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in Mail in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via a crafted MacMIME encapsulated attachment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 197. CVE-2006-1450

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mail in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via an enriched text e-mail message with "invalid color information" that causes Mail to allocate and initialize arbitrary classes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 198. CVE-2006-1451

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
MySQL Manager in Apple Mac OS X 10.3.9 and 10.4.6, when setting up a new MySQL database server, does not use the "New MySQL root password" that is provided, which causes the MySQL root password to be blank and allows local users to gain full privileges to that database.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 199. CVE-2006-1452

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Stack-based buffer overflow in Preview in Apple Mac OS 10.4 up to 10.4.6 allows local users to execute arbitrary code via a deep directory hierarchy.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 200. CVE-2006-1455

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
QuickTime Streaming Server in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to cause a denial of service (crash and connection interruption) via a QuickTime movie with a missing track, which triggers a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 201. CVE-2006-1456

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in QuickTime Streaming Server in Apple Mac OS X 10.3.9 and 10.4.6 allows remote attackers to execute arbitrary code via a crafted RTSP request, which is not properly handled during message logging.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 202. CVE-2006-1457

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Safari on Apple Mac OS X 10.4.6, when "Open `safe' files after downloading" is enabled, will automatically expand archives, which could allow remote attackers to overwrite arbitrary files via an archive that contains a symlink.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00003.html.

---

#### 203. CVE-2006-2238

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1 allows remote attackers to execute arbitrary code via a crafted BMP file that triggers the overflow in the ReadBMP function.  NOTE: this issue was originally included as item 3 in CVE-2006-1983, but it has been given a separate identifier because it is a distinct issue.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/May/msg00002.html.

---

#### 204. CVE-2006-3224

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.3 (417.9.3) on Mac OS X 10.4.6 allows remote attackers to cause a denial of service (CPU consumption) via Javascript with an infinite for loop.  NOTE: it could be argued that this is not a vulnerability, unless it interferes with the operation of the system outside of the scope of Safari itself.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-May/046150.html.

---

#### 205. CVE-2006-1468

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Apple File Protocol (AFP) server in Apple Mac OS X 10.4 up to 10.4.6 includes the names of restricted files and folders within search results, which might allow remote attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

---

#### 206. CVE-2006-1469

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in ImageIO in Apple Mac OS X 10.4 up to 10.4.6 allows attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted TIFF image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

---

#### 207. CVE-2006-1470

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenLDAP in Apple Mac OS X 10.4 up to 10.4.6 allows remote attackers to cause a denial of service (crash) via an invalid LDAP request that triggers an assert error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

---

#### 208. CVE-2006-1471

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Format string vulnerability in the CF_syslog function launchd in Apple Mac OS X 10.4 up to 10.4.6 allows local users to execute arbitrary code via format string specifiers that are not properly handled in a syslog call in the logging facility, as demonstrated by using a crafted plist file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Jun/msg00000.html.

---

#### 209. CVE-2006-1467

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:itunes

**漏洞描述 / Description**:
Integer overflow in the AAC file parsing code in Apple iTunes before 6.0.5 on Mac OS X 10.2.8 or later, and Windows XP and 2000, allows remote user-assisted attackers to execute arbitrary code via an AAC (M4P, M4A, or M4B) file with a sample table size (STSZ) atom with a "malformed" sample_size_table value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=303952.

---

#### 210. CVE-2006-2199

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: openoffice:openoffice, sun:staroffice

**漏洞描述 / Description**:
Unspecified vulnerability in Java Applets in OpenOffice.org 1.1.x (aka StarOffice) up to 1.1.5 and 2.0.x before 2.0.3 allows user-assisted attackers to escape the Java sandbox and conduct unauthorized activities via certain applets in OpenOffice documents.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://fedoranews.org/cms/node/2343.

---

#### 211. CVE-2006-3356

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The TIFFFetchAnyArray function in ImageIO in Apple OS X 10.4.7 and earlier allows remote user-assisted attackers to cause a denial of service (application crash) via an invalid tag value in a TIFF image, possibly triggering a null dereference.  NOTE: This is a different issue than CVE-2006-1469.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.security-protocols.com/sp-x31-advisory.php.

---

#### 212. CVE-2006-3372

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Apple Safari 2.0.4/419.3 allows remote attackers to cause a denial of service (application crash) via a DHTML setAttributeNode function call with zero arguments, which triggers a null dereference.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://browserfun.blogspot.com/2006/07/mobb-5-dhtml-setattributenode.html.

---

#### 213. CVE-2006-3413

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: tor:tor

**漏洞描述 / Description**:
The privoxy configuration file in Tor before 0.1.1.20, when run on Apple OS X, logs all data via the "logfile", which allows attackers to obtain potentially sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/20514.

---

#### 214. CVE-2006-3545

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 7.0 Beta allows remote attackers to cause a denial of service (application crash) via a web page with multiple empty APPLET start tags.  NOTE: a third party has disputed this issue, stating that the crash does not occur with Microsoft Internet Explorer 7.0 Beta3

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/438754/100/0/threaded.

---

#### 215. CVE-2006-3946

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:safari

**漏洞描述 / Description**:
WebCore in Apple Mac OS X 10.3.9 and 10.4 through 10.4.7 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via crafted HTML that triggers a "memory management error" in WebKit, possibly due to a buffer overflow, as originally reported for the KHTMLParser::popOneBlock function in Apple Safari 2.0.4 using Javascript that changes document.body.innerHTML within a DIV tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://browserfun.blogspot.com/2006/07/mobb-31-safari-khtmlparserpoponeblock.html.

---

#### 216. CVE-2006-1472

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in AFP Server in Apple Mac OS X 10.3.9 allows remote attackers to determine names of unauthorized files and folders via unknown vectors related to the search results.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 217. CVE-2006-1473

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in AFP Server for Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause a denial of service (crash) and execute arbitrary code via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 218. CVE-2006-3495

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server in Apple Mac OS X 10.3.9 and 10.4.7 stores reconnect keys in a world-readable file, which allows local users to obtain the keys and access files and folders of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 219. CVE-2006-3496

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server in Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause denial of service (crash) via an invalid AFP request that triggers an unchecked error condition.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 220. CVE-2006-3497

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in the "compression state handling" in Bom for Apple Mac OS X 10.3.9 and 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Zip archive.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 221. CVE-2006-3498

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in bootpd in the DHCP component for Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to execute arbitrary code via a crafted BOOTP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 222. CVE-2006-0392

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Canon RAW image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 223. CVE-2006-0393

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
OpenSSH in Apple Mac OS X 10.4.7 allows remote attackers to cause a denial of service or determine account existence by attempting to log in using an invalid user, which causes the server to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 224. CVE-2006-3499

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The dynamic linker (dyld) in Apple Mac OS X 10.3.9 allows local users to obtain sensitive information via unspecified dynamic linker options that affect the use of standard error (stderr) by privileged applications.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 225. CVE-2006-3500

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The dynamic linker (dyld) in Apple Mac OS X 10.4.7 allows local users to execute arbitrary code via an "improperly handled condition" that leads to use of "dangerous paths," probably related to an untrusted search path vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 226. CVE-2006-3501

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in ImageIO for Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a crafted Radiance image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 227. CVE-2006-3502

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unspecified vulnerability in ImageIO in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted GIF image that triggers a memory allocation failure that is not properly handled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 228. CVE-2006-3503

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in ImageIO in Apple Mac OS X 10.4.7 allows user-assisted attackers to cause a denial of service (crash) and possibly execute arbitrary code via a malformed GIF image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 229. CVE-2006-3504

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The Download Validation in LaunchServices for Apple Mac OS X 10.4.7 can identify certain HTML as "safe", which could allow attackers to execute Javascript code in local context when the "Open 'safe' files after downloading" option is enabled in Safari.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 230. CVE-2006-3505

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
WebKit in Apple Mac OS X 10.3.9 and 10.4.7 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted HTML document that causes WebKit to access an object that has already been deallocated.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006//Aug/msg00000.html.

---

#### 231. CVE-2006-4381

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted H.264 movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 232. CVE-2006-4382

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Multiple buffer overflows in Apple QuickTime before 7.1.3 allow user-assisted remote attackers to execute arbitrary code via a crafted QuickTime movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 233. CVE-2006-4384

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Heap-based buffer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via the COLOR_64 chunk in a FLIC (FLC) movie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 234. CVE-2006-4385

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Buffer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted SGI image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 235. CVE-2006-4386

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted H.264 movie, a different issue than CVE-2006-4381.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 236. CVE-2006-4388

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Integer overflow in Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted FlashPix file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 237. CVE-2006-4389

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime before 7.1.3 allows user-assisted remote attackers to execute arbitrary code via a crafted FlashPix (FPX) file, which triggers an exception that leads to an operation on an uninitialized object.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304357.

---

#### 238. CVE-2006-4866

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in kextload in Apple OS X, as used by TDIXSupport in Roxio Toast Titanium and possibly other products, allows local users to execute arbitrary code via a long extension argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2006-September/049452.html.

---

#### 239. CVE-2006-4887

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:apple_remote_desktop, apple:mac_os_x

**漏洞描述 / Description**:
Apple Remote Desktop (ARD) for Mac OS X 10.2.8 and later does not drop privileges on the remote machine while installing certain applications, which allows local users to bypass authentication and gain privileges by selecting the icon during installation.  NOTE: it could be argued that the issue is not in Remote Desktop itself, but in applications that are installed while using it.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/32260.

---

#### 240. CVE-2006-3507

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Multiple stack-based buffer overflows in the AirPort wireless driver on Apple Mac OS X 10.3.9 and 10.4.7 allow physically proximate attackers to execute arbitrary code by injecting crafted frames into a wireless network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

---

#### 241. CVE-2006-3508

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Heap-based buffer overflow in the AirPort wireless driver on Apple Mac OS X 10.4.7 allows physically proximate attackers to cause a denial of service (crash), gain privileges, and execute arbitrary code via a crafted frame that is not properly handled during scan cache updates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

---

#### 242. CVE-2006-3509

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in the API for the AirPort wireless driver on Apple Mac OS X 10.4.7 might allow physically proximate attackers to cause a denial of service (crash) or execute arbitrary code in third-party wireless software that uses the API via crafted frames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2006/Sep/msg00001.html.

---

#### 243. CVE-2006-4965

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:quicktime

**漏洞描述 / Description**:
Apple QuickTime 7.1.3 Player and Plug-In allows remote attackers to execute arbitrary JavaScript code and possibly conduct other attacks via a QuickTime Media Link (QTL) file with an embed XML element and a qtnext parameter that identifies resources outside of the original domain.  NOTE: as of 20070912, this issue has been demonstrated by using instances of Components.interfaces.nsILocalFile and Components.interfaces.nsIProcess to execute arbitrary local files within Firefox and possibly Internet Explorer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305149.

---

#### 244. CVE-2006-4387

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X 10.4 through 10.4.7, when the administrator clears the "Allow user to administer this computer" checkbox in System Preferences for a user, does not remove the user's account from the appserveradm or appserverusr groups, which still allows the user to manage WebObjects applications.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 245. CVE-2006-4390

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
CFNetwork in Apple Mac OS X 10.4 through 10.4.7 and 10.3.9 allows remote SSL sites to appear as trusted sites by using encryption without authentication, which can cause the lock icon in Safari to be displayed even when the site's identity cannot be trusted.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 246. CVE-2006-4391

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in Apple ImageIO on Apple Mac OS X 10.4 through 10.4.7 allows remote attackers to execute arbitrary code via a malformed JPEG2000 image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 247. CVE-2006-4393

**严重程度 / Severity**: N/A | CVSS: 3.7
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in LoginWindow in Apple Mac OS X 10.4 through 10.4.7, when Fast User Switching is enabled, allows local users to gain access to Kerberos tickets of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 248. CVE-2006-4394

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
A logic error in LoginWindow in Apple Mac OS X 10.4 through 10.4.7, allows network accounts without GUIds to bypass service access controls and log into the system using loginwindow via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 249. CVE-2006-4395

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in QuickDraw Manager in Apple Mac OS X 10.3.9 and 10.4 through 10.4.7 allows context-dependent attackers to cause a denial of service ("memory corruption" and crash) via a crafted PICT image that is not properly handled by a certain "unsupported QuickDraw operation."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 250. CVE-2006-4397

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unchecked error condition in LoginWindow in Apple Mac OS X 10.4 through 10.4.7 prevents Kerberos tickets from being destroyed if a user does not successfully log on to a network account from the login window, which might allow later users to gain access to the original user's Kerberos tickets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 251. CVE-2006-4399

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
User interface inconsistency in Workgroup Manager in Apple Mac OS X 10.4 through 10.4.7 appears to allow administrators to change the authentication type from crypt to ShadowHash passwords for accounts in a NetInfo parent, when such an operation is not actually supported, which could result in less secure password management than intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Sep/msg00002.html.

---

#### 252. CVE-2006-5327

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: openbase_international_ltd:openbase, apple:xcode

**漏洞描述 / Description**:
Untrusted search path vulnerability in OpenBase SQL 10.0 and earlier, as used in Apple Xcode 2.2 2.2 and earlier and possibly other products, allows local users to execute arbitrary code via a modified PATH that references a malicious gzip program, which is executed by gnutar with certain TAR_OPTIONS environment variable settings, when gnutar is invoked by OpenBase.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2007/Oct/msg00001.html.

---

#### 253. CVE-2006-5328

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: openbase_international_ltd:openbase, apple:xcode

**漏洞描述 / Description**:
OpenBase SQL 10.0 and earlier, as used in Apple Xcode 2.2 2.2 and earlier and possibly other products, allows local users to create arbitrary files via a symlink attack on the simulation.sql file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2007/Oct/msg00001.html.

---

#### 254. CVE-2006-5710

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: opendarwin:darwin_kernel, apple:mac_os_x

**漏洞描述 / Description**:
The Airport driver for certain Orinoco based Airport cards in Darwin kernel 8.8.0 in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to execute arbitrary code via an 802.11 probe response frame without any valid information element (IE) fields after the header, which triggers a heap-based buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 255. CVE-2006-5836

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: opendarwin:darwin_kernel

**漏洞描述 / Description**:
The fpathconf syscall function in bsd/kern/kern_descrip.c in the Darwin kernel (XNU) 8.8.1 in Apple Mac OS X allows local users to cause a denial of service (kernel panic) and possibly execute arbitrary code via a file descriptor with an unrecognized file type.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

---

#### 256. CVE-2006-4413

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:remote_desktop

**漏洞描述 / Description**:
Apple Remote Desktop before 3.1 uses insecure permissions for certain built-in packages, which allows local users on an Apple Remote Desktop administration system to modify the packages and gain root privileges on client systems that use the packages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2006/Nov/msg00000.html.

---

#### 257. CVE-2006-6009

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:jre, sun:jdk

**漏洞描述 / Description**:
Unspecified vulnerability in the Java Runtime Environment (JRE) Swing library in JDK and JRE 5.0 Update 7 and earlier allows attackers to obtain certain information via unknown attack vectors, related to an untrusted applet accessing data in other applets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/22910.

---

#### 258. CVE-2006-6015

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the JavaScript implementation in Safari on Apple Mac OS X 10.4 allows remote attackers to cause a denial of service (application crash) via a long argument to the exec method of a regular expression.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/451542/100/0/threaded.

---

#### 259. CVE-2006-6061

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
com.apple.AppleDiskImageController in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to execute arbitrary code via a malformed DMG image that triggers memory corruption.  NOTE: the severity of this issue has been disputed by a third party, who states that the impact is limited to a denial of service (kernel panic) due to a vm_fault call with a non-aligned address.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://alastairs-place.net/2006/11/dmg-vulnerability/.

---

#### 260. CVE-2006-6062

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Apple Mac OS X 10.4.8, and possibly other versions, allows remote attackers to cause a denial of service (crash) via a malformed UDTO HFS+ disk image, such as with "bad sectors," which triggers memory corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

---

#### 261. CVE-2006-6126

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X allows local users to cause a denial of service (memory corruption) via a crafted Mach-O binary with a malformed load_command data structure.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://projects.info-pull.com/mokb/MOKB-23-11-2006.html.

---

#### 262. CVE-2006-6127

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X kernel allows local users to cause a denial of service via a process that uses kevent to register a queue and an event, then fork a child process that uses kevent to register an event for the same queue as the parent.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=307041.

---

#### 263. CVE-2006-6129

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Integer overflow in the fatfile_getarch2 in Apple Mac OS X allows local users to cause a denial of service and possibly execute arbitrary code via a crafted Mach-O Universal program that triggers memory corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

---

#### 264. CVE-2006-6130

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Apple Mac OS X AppleTalk allows local users to cause a denial of service (kernel panic) by calling the AIOCREGLOCALZN ioctl command with a crafted data structure on an AppleTalk socket.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305214.

---

#### 265. CVE-2006-4396

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Apple Type Services (ATS) server in Mac OS X 10.4.8 and earlier does not securely create log files, which allows local users to create and modify arbitrary files via unspecified vectors, possibly relating to a symlink attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 266. CVE-2006-4398

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Multiple buffer overflows in the Apple Type Services (ATS) server in Mac OS X 10.4 through 10.4.8 allow local users to execute arbitrary code via crafted service requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 267. CVE-2006-4400

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Stack-based buffer overflow in the Apple Type Services (ATS) server in Mac OS 10.4.8 and earlier allow user-assisted attackers to execute arbitrary code via crafted font files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 268. CVE-2006-4402

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Heap-based buffer overflow in the Finder in Apple Mac OS X 10.4.8 and earlier allows user-assisted remote attackers to execute arbitrary code by browsing directories containing crafted .DS_Store files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 269. CVE-2006-4403

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The FTP server in Apple Mac OS X 10.4.8 and earlier, when FTP Access is enabled, will crash when a login failure occurs with a valid user name, which allows remote attackers to cause a denial of service (crash) and enumerate valid usernames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 270. CVE-2006-4404

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Installer application in Apple Mac OS X 10.4.8 and earlier, when used by a user with Admin credentials, does not authenticate the user before installing certain software requiring system privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 271. CVE-2006-4406

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in PPP on Apple Mac OS X 10.4.x up to 10.4.8 and 10.3.x up to 10.3.9, when PPPoE is enabled, allows remote attackers to execute arbitrary code via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 272. CVE-2006-4407

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.3.x up to 10.3.9 does not properly prioritize encryption ciphers when negotiating the strongest shared cipher, which causes Secure Transport to user a weaker cipher that makes it easier for remote attackers to decrypt traffic.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 273. CVE-2006-4408

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.4 through 10.4.8 allows remote attackers to cause a denial of service (resource consumption) via certain public key values in an X.509 certificate that requires extra resources during signature verification.  NOTE: this issue may be similar to CVE-2006-2940.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 274. CVE-2006-4409

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Online Certificate Status Protocol (OCSP) service in the Security Framework in Apple Mac OS X 10.4 through 10.4.8 retrieve certificate revocation lists (CRL) when an HTTP proxy is in use, which could cause the system to accept certificates that have been revoked.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 275. CVE-2006-4410

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Security Framework in Apple Mac OS X 10.3.9, and 10.4.x before 10.4.7, does not properly search certificate revocation lists (CRL), which allows remote attackers to access systems by using revoked certificates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 276. CVE-2006-4411

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The VPN service in Apple Mac OS X 10.3.x through 10.3.9 and 10.4.x through 10.4.8 does not properly clean the environment when executing commands, which allows local users to gain privileges via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 277. CVE-2006-4412

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
WebKit in Apple Mac OS X 10.3.x through 10.3.9 and 10.4 through 10.4.8 allows remote attackers to execute arbitrary code via a crafted HTML file, which accesses previously deallocated objects.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304829.

---

#### 278. CVE-2006-6238

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
The AutoFill feature in Apple Safari 2.0.4 does not properly verify that all automatically populated form fields are visible to the user, which allows remote attackers to obtain sensitive information, such as usernames and passwords, via input fields of zero width, a variant of CVE-2006-6077.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/23066.

---

#### 279. CVE-2006-6292

**严重程度 / Severity**: N/A | CVSS: 5.7
**受影响产品 / Affected Products**: apple:airport_extreme, apple:mac_os_x

**漏洞描述 / Description**:
Apple Airport Extreme firmware 0.1.27 in Mac OS X 10.4.8 on Mac mini, MacBook, and MacBook Pro with Core Duo hardware allows remote attackers to cause a denial of service (out-of-bounds memory access and kernel panic) and have possibly other security-related impact via certain beacon frames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305031.

---

#### 280. CVE-2006-5681

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
QuickTime for Java on Mac OS X 10.4 through 10.4.8, when used with Quartz Composer, allows remote attackers to obtain sensitive information (screen images) via a Java applet that accesses images that are being rendered by other embedded QuickTime objects.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=304916.

---

#### 281. CVE-2006-6652

**严重程度 / Severity**: N/A | CVSS: 9.0
**受影响产品 / Affected Products**: netbsd:netbsd, apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the glob implementation (glob.c) in libc in NetBSD-current before 20050914, NetBSD 2.* and 3.* before 20061203, and Apple Mac OS X before 2007-004, as used by the FTP daemon and tnftpd, allows remote authenticated users to execute arbitrary code via a long pathname that results from path expansion.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=305391.

---

#### 282. CVE-1999-1113

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: eudora:internet_mail_server

**漏洞描述 / Description**:
Buffer overflow in Eudora Internet Mail Server (EIMS) 2.01 and earlier on MacOS systems allows remote attackers to cause a denial of service via a long USER command to port 106.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=89258194718577&w=2.

---

#### 283. CVE-1999-1543

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
MacOS uses weak encryption for passwords that are stored in the Users & Groups Data File.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93188174906513&w=2.

---

#### 284. CVE-1999-1076

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local users to bypass the password protection of idled sessions by selecting the "Log Out" option and selecting a "Cancel" option in the dialog box for an application that attempts to verify that the user wants to log out, which returns the attacker into the locked session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94096348604173&w=2.

---

#### 285. CVE-1999-1077

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
Idle locking function in MacOS 9 allows local attackers to bypass the password protection of idled sessions via the programmer's switch or CMD-PWR keyboard sequence, which brings up a debugger that the attacker can use to disable the lock.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94149318124548&w=2.

---

#### 286. CVE-1999-1528

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: prosoft_engineering:netware_client

**漏洞描述 / Description**:
ProSoft Netware Client 5.12 on Macintosh MacOS 9 does not automatically log a user out of the NDS tree when the user logs off the system, which allows other users of the same system access to the unprotected NDS session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94261444428430&w=2.

---

#### 287. CVE-2001-0766

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apache:http_server

**漏洞描述 / Description**:
Apache on MacOS X Client 10.0.3 with the HFS+ file system allows remote attackers to bypass access restrictions via a URL that contains some characters whose case is not matched by Apache's filters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-06/0090.html.

---

#### 288. CVE-2001-0921

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: netscape:communicator

**漏洞描述 / Description**:
Netscape 4.79 and earlier for MacOS allows an attacker with access to the browser to obtain passwords from form fields by printing the document into which the password has been typed, which is printed in cleartext.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100638816318705&w=2.

---

#### 289. CVE-2001-1565

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Point to Point Protocol daemon (pppd) in MacOS x 10.0 and 10.1 through 10.1.5 provides the username and password on the command line, which allows local users to obtain authentication information via the ps command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7750.php.

---

#### 290. CVE-2002-1773

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: mirabilis:icq_for_macos_x

**漏洞描述 / Description**:
Buffer overflow in ICQ 2.6x for MacOS X 10.0 through 10.1.2 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/254133.

---

#### 291. CVE-2002-2169

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: aol:instant_messenger

**漏洞描述 / Description**:
Cross-site scripting vulnerability AOL Instant Messenger (AIM) 4.5 and 4.7 for MacOS and Windows allows remote attackers to conduct unauthorized activities, such as adding buddies and groups to a user's buddy list, via a URL with a META HTTP-EQUIV="refresh" tag to an aim: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/282443.

---

#### 292. CVE-2003-0088

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
TruBlueEnvironment for MacOS 10.2.3 and earlier allows local users to overwrite or create arbitrary files and gain root privileges by setting a certain environment variable that is used to write debugging information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

---

#### 293. CVE-2002-1491

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:vpn_5000_client

**漏洞描述 / Description**:
The Cisco VPN 5000 Client for MacOS before 5.2.2 records the most recently used login password in plaintext when saving "Default Connection" settings, which could allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/vpn5k-client-multiple-vuln-pub.shtml.

---

#### 294. CVE-2003-0171

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
DirectoryServices in MacOS X trusts the PATH environment variable to locate and execute the touch command, which allows local users to execute arbitrary commands by modifying the PATH to point to a directory containing a malicious touch program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00028.html.

---

#### 295. CVE-2003-0490

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: dantz:retrospect_client

**漏洞描述 / Description**:
The installation of Dantz Retrospect Client 5.0.540 on MacOS X 10.2.6, and possibly other versions, creates critical directories and files with world-writable permissions, which allows local users to gain privileges as other users by replacing programs with malicious code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=105579526026992&w=2.

---

#### 296. CVE-2003-0518

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The screen saver in MacOS X allows users with physical access to cause the screen saver to crash and gain access to the underlying session via a large number of characters in the password field, possibly triggering a buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-07/0034.html.

---

#### 297. CVE-2001-1412

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
nidump on MacOS X before 10.3 allows local users to read the encrypted passwords from the password file by specifying passwd as a command line argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00038.html.

---

#### 298. CVE-2004-0169

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:darwin_streaming_server

**漏洞描述 / Description**:
QuickTime Streaming Server in MacOS X 10.2.8 and 10.3.2 allows remote attackers to cause a denial of service (crash) via DESCRIBE requests with long User-Agent fields, which causes an Assert error to be triggered in the BufferIsFull function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

---

#### 299. CVE-2007-3184

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: cisco:trust_agent, apple:mac_os_x

**漏洞描述 / Description**:
Cisco Trust Agent (CTA) before 2.1.104.0, when running on MacOS X, allows attackers with physical access to bypass authentication and modify System Preferences, including passwords, by invoking the Apple Menu when the Access Control Server (ACS) produces a user notification message after posture validation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/25598.

---

#### 300. CVE-2007-6456

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: planamesa:neooffice

**漏洞描述 / Description**:
Unspecified vulnerability in OpenOffice.org code in Planamesa NeoOffice 2.2.2 before Patch 4 has unknown impact and attack vectors related to MacOS 10.3.9 .odb files.  NOTE: it is not clear whether this issue is a vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://neowiki.neooffice.org/index.php/NeoOffice_Release_Notes.

---

#### 301. CVE-2016-4617

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves a sandbox escape related to launchctl process spawning in the "libxpc" component.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/96329.

---

#### 302. CVE-2016-4660

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "FontParser" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

---

#### 303. CVE-2016-4661

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ntfs" component, which misparses disk images and allows attackers to cause a denial of service via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 304. CVE-2016-4662

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleGraphicsControl" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 305. CVE-2016-4663

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "NVIDIA Graphics Drivers" component. It allows attackers to cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 306. CVE-2016-4667

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 307. CVE-2016-4669

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (MIG code mishandling and system crash) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/158874/Safari-Webkit-For-iOS-7.1.2-JIT-Optimization-Bug.html.

---

#### 308. CVE-2016-4670

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "Security" component. It allows local users to discover lengths of arbitrary passwords by reading a log.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94433.

---

#### 309. CVE-2016-4671

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds write and application crash) via a crafted PDF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 310. CVE-2016-4673

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "CoreGraphics" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

---

#### 311. CVE-2016-4674

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ATS" component. It allows local users to gain privileges or cause a denial of service (memory corruption and application crash) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 312. CVE-2016-4675

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libxpc" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

---

#### 313. CVE-2016-4678

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "AppleSMC" component. It allows local users to gain privileges or cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 314. CVE-2016-4679

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "libarchive" component, which allows remote attackers to write to arbitrary files via a crafted archive containing a symlink.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93849.

---

#### 315. CVE-2016-4681

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Core Image" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94431.

---

#### 316. CVE-2016-4682

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted SGI file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93852.

---

#### 317. CVE-2016-4683

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (out-of-bounds memory access and application crash) via a crafted SGI file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94431.

---

#### 318. CVE-2016-4688

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:tvos, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94572.

---

#### 319. CVE-2016-4691

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 320. CVE-2016-4693

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which makes it easier for attackers to bypass cryptographic protection mechanisms by leveraging use of the 3DES cipher.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 321. CVE-2016-4721

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "IDS - Connectivity" component, which allows man-in-the-middle attackers to spoof calls via a "switch caller" notification.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94429.

---

#### 322. CVE-2016-4780

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.1 is affected. The issue involves the "Thunderbolt" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207275.

---

#### 323. CVE-2016-7577

**严重程度 / Severity**: LOW | CVSS: 3.7
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. The issue involves the "FaceTime" component, which allows remote attackers to trigger memory corruption and obtain audio data from a call that appeared to have ended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94429.

---

#### 324. CVE-2016-7579

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. The issue involves the "CFNetwork Proxies" component, which allows man-in-the-middle attackers to spoof a proxy password authentication requirement and obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/93856.

---

#### 325. CVE-2016-7580

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Mail" component, which allows remote web servers to cause a denial of service via a crafted URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94434.

---

#### 326. CVE-2016-7582

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94435.

---

#### 327. CVE-2016-7584

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "AppleMobileFileIntegrity" component, which allows remote attackers to spoof signed code by using a matching team ID.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94571.

---

#### 328. CVE-2016-7588

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreMedia Playback" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted MP4 file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 329. CVE-2016-7591

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOHIDFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 330. CVE-2016-7594

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ICU" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 331. CVE-2016-7595

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreText" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 332. CVE-2016-7596

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 333. CVE-2016-7600

**严重程度 / Severity**: MEDIUM | CVSS: 6.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "OpenPAM" component, which allows local users to obtain sensitive information by leveraging mishandling of failed PAM authentication by a sandboxed app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 334. CVE-2016-7602

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 335. CVE-2016-7603

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreStorage" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 336. CVE-2016-7604

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "CoreCapture" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 337. CVE-2016-7605

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 338. CVE-2016-7606

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 339. CVE-2016-7607

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows attackers to obtain sensitive information from kernel memory via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 340. CVE-2016-7608

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOFireWireFamily" component, which allows local users to obtain sensitive information from kernel memory via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 341. CVE-2016-7609

**严重程度 / Severity**: MEDIUM | CVSS: 6.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "AppleGraphicsPowerManagement" component. It allows local users to cause a denial of service (NULL pointer dereference) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 342. CVE-2016-7612

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 343. CVE-2016-7613

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x, apple:safari

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.1 is affected. macOS before 10.12.1 is affected. tvOS before 10.0.1 is affected. watchOS before 3.1 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app that leverages object-lifetime mishandling during process spawning.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94116.

---

#### 344. CVE-2016-7615

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component, which allows local users to cause a denial of service via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 345. CVE-2016-7616

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Disk Images" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 346. CVE-2016-7617

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (type confusion) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 347. CVE-2016-7618

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Foundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 348. CVE-2016-7619

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "libarchive" component, which allows local users to write to arbitrary files via vectors related to symlinks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 349. CVE-2016-7620

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOSurface" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 350. CVE-2016-7621

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:watchos, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 351. CVE-2016-7622

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Grapher" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .gcx file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 352. CVE-2016-7624

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOAcceleratorFamily" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 353. CVE-2016-7625

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 354. CVE-2016-7627

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreGraphics" component. It allows attackers to cause a denial of service (NULL pointer dereference and application crash) via a crafted font.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 355. CVE-2016-7628

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Assets" component, which allows local users to bypass intended permission restrictions and change a downloaded mobile asset via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 356. CVE-2016-7629

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "kext tools" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 357. CVE-2016-7633

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "Directory Services" component. It allows local users to gain privileges or cause a denial of service (use-after-free) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94903.

---

#### 358. CVE-2016-7636

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows man-in-the-middle attackers to cause a denial of service (application crash) via vectors related to OCSP responder URLs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 359. CVE-2016-7637

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows local users to gain privileges or cause a denial of service (memory corruption) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 360. CVE-2016-7643

**严重程度 / Severity**: HIGH | CVSS: 8.1
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "ImageIO" component. It allows remote attackers to obtain sensitive information from process memory or cause a denial of service (out-of-bounds read and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 361. CVE-2016-7644

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94904.

---

#### 362. CVE-2016-7655

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreMedia External Displays" component. It allows local users to gain privileges or cause a denial of service (type confusion) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94906.

---

#### 363. CVE-2016-7657

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows attackers to obtain sensitive information from kernel memory via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 364. CVE-2016-7658

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 365. CVE-2016-7659

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 366. CVE-2016-7660

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "syslog" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 367. CVE-2016-7661

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "Power Management" component. It allows local users to gain privileges via unspecified vectors related to Mach port name references.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94906.

---

#### 368. CVE-2016-7662

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "Security" component, which allows remote attackers to spoof certificates via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 369. CVE-2016-7663

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "CoreFoundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/94905.

---

#### 370. CVE-2016-7667

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to cause a denial of service via a crafted string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207422.

---

#### 371. CVE-2016-7714

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2 is affected. macOS before 10.12.2 is affected. watchOS before 3.1.3 is affected. The issue involves the "IOKit" component. It allows local users to obtain sensitive kernel memory-layout information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207422.

---

#### 372. CVE-2016-7742

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "xar" component, which allows remote attackers to execute arbitrary code via a crafted archive that triggers use of uninitialized memory locations.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207423.

---

#### 373. CVE-2016-7761

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.2 is affected. The issue involves the "WiFi" component, which allows local users to obtain sensitive network-configuration information by leveraging global storage.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://support.apple.com/HT207423.

---

#### 374. CVE-2017-2353

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

---

#### 375. CVE-2017-2357

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "IOAudioFamily" component. It allows attackers to obtain sensitive kernel memory-layout information via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

---

#### 376. CVE-2017-2358

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Graphics Drivers" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

---

#### 377. CVE-2017-2360

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, webkitgtk:webkitgtk\+, apple:tvos, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2.1 is affected. macOS before 10.12.3 is affected. tvOS before 10.1.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95729.

---

#### 378. CVE-2017-2361

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.3 is affected. The issue involves the "Help Viewer" component, which allows XSS attacks via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95723.

---

#### 379. CVE-2017-2370

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:watchos, apple:iphone_os, apple:mac_os_x, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.2.1 is affected. macOS before 10.12.3 is affected. tvOS before 10.1.1 is affected. watchOS before 3.1.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (buffer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/95731.

---

#### 380. CVE-2016-9892

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: eset:endpoint_antivirus, eset:endpoint_security

**漏洞描述 / Description**:
The esets_daemon service in ESET Endpoint Antivirus for macOS before 6.4.168.0 and Endpoint Security for macOS before 6.4.168.0 does not properly verify X.509 certificates from the edf.eset.com SSL server, which allows man-in-the-middle attackers to spoof this server and provide crafted responses to license activation requests via a self-signed certificate.  NOTE: this issue can be combined with CVE-2016-0718 to execute arbitrary code remotely as root.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://packetstormsecurity.com/files/141350/ESET-Endpoint-Antivirus-6-Remote-Code-Execution.html.

---

#### 381. CVE-2016-7585

**严重程度 / Severity**: MEDIUM | CVSS: 6.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves mishandling of DMA in the "EFI" component. It allows physically proximate attackers to discover the FileVault 2 encryption password via a crafted Thunderbolt adapter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 382. CVE-2017-2379

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Carbon" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted .dfont file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 383. CVE-2017-2381

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "sudo" component. It allows remote authenticated users to gain privileges by leveraging membership in the admin group on a network directory server.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 384. CVE-2017-2382

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_server

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS Server before 5.3 is affected. The issue involves the "Wiki Server" component. It allows remote attackers to enumerate user accounts via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97128.

---

#### 385. CVE-2017-2388

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireFamily" component. It allows attackers to cause a denial of service (NULL pointer dereference) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 386. CVE-2017-2390

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves symlink mishandling in the "libarchive" component. It allows local users to change arbitrary directory permissions via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 387. CVE-2017-2391

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: apple:pages, apple:keynote, apple:numbers

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. Pages before 6.1, Numbers before 4.1, and Keynote before 7.1 on macOS and Pages before 3.1, Numbers before 3.1, and Keynote before 3.1 on iOS are affected. The issue involves the "Export" component. It allows users to bypass iWork PDF password protection by leveraging use of 40-bit RC4.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97126.

---

#### 388. CVE-2017-2398

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97147.

---

#### 389. CVE-2017-2401

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 390. CVE-2017-2402

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves mishandling of profile uninstall actions in the "MCX Client" component when a profile has multiple payloads. It allows remote attackers to bypass intended access restrictions by leveraging Active Directory certificate trust that should not have remained.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 391. CVE-2017-2403

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Printing" component. A format-string vulnerability allows remote attackers to execute arbitrary code via a crafted ipp: or ipps: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 392. CVE-2017-2406

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 393. CVE-2017-2407

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 394. CVE-2017-2408

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOATAFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 395. CVE-2017-2409

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Menus" component. It allows attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 396. CVE-2017-2410

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 397. CVE-2017-2413

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "QuickTime" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted media file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 398. CVE-2017-2416

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted image file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 399. CVE-2017-2417

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreGraphics" component. It allows remote attackers to cause a denial of service (infinite recursion) via a crafted image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 400. CVE-2017-2418

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Hypervisor" component. It allows guest OS users to obtain sensitive information from the CR8 control register via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 401. CVE-2017-2420

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 402. CVE-2017-2421

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "AppleGraphicsPowerManagement" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 403. CVE-2017-2422

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Multi-Touch" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 404. CVE-2017-2423

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. The issue involves the "Security" component. It allows remote attackers to bypass intended access restrictions by leveraging a successful result from a SecKeyRawVerify API call with an empty signature.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97147.

---

#### 405. CVE-2017-2425

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "SecurityFoundation" component. A double free vulnerability allows remote attackers to execute arbitrary code via a crafted certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 406. CVE-2017-2426

**严重程度 / Severity**: LOW | CVSS: 3.3
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "iBooks" component. It allows remote attackers to obtain sensitive information from local files via a file: URL in an iBooks file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 407. CVE-2017-2427

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 408. CVE-2017-2428

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves nghttp2 before 1.17.0 in the "HTTPProtocol" component. It allows remote HTTP/2 servers to have an unspecified impact via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97146.

---

#### 409. CVE-2017-2429

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "FinderKit" component. It allows remote attackers to bypass intended access restrictions in opportunistic circumstances by leveraging unexpected permission changes during an iCloud Sharing Send Link action.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 410. CVE-2017-2430

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 411. CVE-2017-2431

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "CoreMedia" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted .mov file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 412. CVE-2017-2432

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 413. CVE-2017-2435

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 414. CVE-2017-2436

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireAVC" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 415. CVE-2017-2437

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "IOFireWireAVC" component. It allows local users to gain privileges or cause a denial of service (memory corruption) via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 416. CVE-2017-2438

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "AppleRAID" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 417. CVE-2017-2439

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 418. CVE-2017-2440

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (integer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 419. CVE-2017-2441

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "libc++abi" component. A use-after-free vulnerability allows remote attackers to execute arbitrary code via a crafted C++ app that is mishandled during demangling.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 420. CVE-2017-2443

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 421. CVE-2017-2448

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. The issue involves the "Keychain" component. It allows man-in-the-middle attackers to bypass an iCloud Keychain secret protection mechanism by leveraging lack of authentication for OTR packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97134.

---

#### 422. CVE-2017-2449

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

---

#### 423. CVE-2017-2450

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 424. CVE-2017-2451

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Security" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (buffer overflow) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 425. CVE-2017-2456

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:tvos, apple:iphone_os, apple:mac_os_x, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

---

#### 426. CVE-2001-0102

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:macos

**漏洞描述 / Description**:
"Multiple Users" Control Panel in Mac OS 9 allows Normal users to gain Owner privileges by removing the Users & Groups Data File, which effectively removes the Owner password and allows the Normal user to log in as the Owner account without a password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-12/0497.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0497.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5830
- http://archives.neohapsis.com/archives/bugtraq/2000-12/0497.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5830

---

#### 427. CVE-2001-0438

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: netopia:timbuktu_mac

**漏洞描述 / Description**:
Preview version of Timbuktu for Mac OS X allows local users to modify System Preferences without logging in via the About Timbuktu menu.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-04/0337.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0337.html
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0337.html

---

#### 428. CVE-2001-1446

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Find-By-Content in Mac OS X 10.0 through 10.0.4 creates world-readable index files named .FBCIndex in every directory, which allows remote attackers to learn the contents of files in web accessible directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-09/0085.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-09/0085.html
- http://www.kb.cert.org/vuls/id/177243
- http://www.securityfocus.com/bid/3325
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7103
- http://archives.neohapsis.com/archives/bugtraq/2001-09/0085.html

---

#### 429. CVE-2001-1447

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
NetInfo Manager for Mac OS X 10.0 through 10.1 allows local users to gain root privileges by opening applications using the (1) "recent items" and (2) "services" menus, which causes the applications to run with root privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-10/0121.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0121.html
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0130.html
- http://www.ciac.org/ciac/bulletins/m-007.shtml
- http://www.kb.cert.org/vuls/id/945747
- http://www.securityfocus.com/bid/3439

---

#### 430. CVE-2001-0720

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Internet Explorer 5.1 for Macintosh on Mac OS X allows remote attackers to execute arbitrary commands by causing a BinHex or MacBinary file type to be downloaded, which causes the files to be executed if automatic decoding is enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-013.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-013.shtml
- http://www.securityfocus.com/bid/3471
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-053
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7336
- http://www.ciac.org/ciac/bulletins/m-013.shtml

---

#### 431. CVE-2002-0529

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: hp:photosmart_print_driver

**漏洞描述 / Description**:
HP Photosmart printer driver for Mac OS X installs the hp_imaging_connectivity program and the hp_imaging_connectivity.app directory with world-writable permissions, which allows local users to gain privileges of other Photosmart users by replacing hp_imaging_connectivity with a Trojan horse.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-04/0169.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-04/0169.html
- http://www.iss.net/security_center/static/8856.php
- http://www.securityfocus.com/bid/4518
- http://archives.neohapsis.com/archives/bugtraq/2002-04/0169.html
- http://www.iss.net/security_center/static/8856.php

---

#### 432. CVE-2002-1266

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.2.2 allows local users to gain privileges by mounting a disk image file that was created on another system, aka "Local User Privilege Elevation via Disk Image File."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.info.apple.com/usen/security/security_updates.html.

**参考链接 / References**:
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7057
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10818
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7057

---

#### 433. CVE-2002-1267

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.2.2 allows remote attackers to cause a denial of service by accessing the CUPS Printing Web Administration utility, aka "CUPS Printing Web Administration is Remotely Accessible."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.info.apple.com/usen/security/security_updates.html.

**参考链接 / References**:
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7058
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10824
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7058

---

#### 434. CVE-2002-1268

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.2.2 allows local users to gain privileges via a mounted ISO 9600 CD, aka "User Privilege Elevation via Mounting an ISO 9600 CD."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.info.apple.com/usen/security/security_updates.html.

**参考链接 / References**:
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7059
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10828
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7059

---

#### 435. CVE-2002-1269

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in NetInfo Manager application in Mac OS X 10.2.2 allows local users to access restricted parts of a filesystem.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.info.apple.com/usen/security/security_updates.html.

**参考链接 / References**:
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.info.apple.com/usen/security/security_updates.html

---

#### 436. CVE-2002-1270

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.2.2 allows local users to read files that only allow write access via the map_fd() Mach system call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.info.apple.com/usen/security/security_updates.html.

**参考链接 / References**:
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7060
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10829
- http://www.info.apple.com/usen/security/security_updates.html
- http://www.osvdb.org/7060

---

#### 437. CVE-2002-2326

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The default configuration of Mail.app in Mac OS X 10.0 through 10.0.4 and 10.1 through 10.1.5 sends iDisk authentication credentials in cleartext when connecting to Mac.com, which could allow remote attackers to obtain passwords by sniffing network traffic.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-07/0276.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0276.html
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0281.html
- http://www.iss.net/security_center/static/9670.php
- http://www.securityfocus.com/bid/5303
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0276.html

---

#### 438. CVE-2003-0198

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X before 10.2.5 allows guest users to modify the permissions of the DropBox folder and read unauthorized files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00028.html.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00028.html
- http://lists.apple.com/mhonarc/security-announce/msg00028.html

---

#### 439. CVE-2003-0242

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
IPSec in Mac OS X before 10.2.6 does not properly handle certain incoming security policies that match by port, which could allow traffic that is not explicitly allowed by the policies.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://secunia.com/advisories/8798
- http://securitytracker.com/id?1006796
- http://www.kb.cert.org/vuls/id/869548
- http://www.securityfocus.com/bid/7628

---

#### 440. CVE-2003-0378

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The Kerberos login authentication feature in Mac OS X, when used with an LDAPv3 server and LDAP bind authentication, may send cleartext passwords to the LDAP server when the AuthenticationAuthority attribute is not set.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=107579.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=107579
- http://www.kb.cert.org/vuls/id/467828
- http://docs.info.apple.com/article.html?artnum=107579
- http://www.kb.cert.org/vuls/id/467828

---

#### 441. CVE-2003-0871

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in QuickTime Java in Mac OS X v10.3 and Mac OS X Server 10.3 allows attackers to gain "unauthorized access to a system."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00039.html.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00039.html
- http://www.securityfocus.com/bid/8922
- http://lists.apple.com/mhonarc/security-announce/msg00039.html
- http://www.securityfocus.com/bid/8922

---

#### 442. CVE-2003-0876

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Finder in Mac OS X 10.2.8 and earlier sets global read/write/execute permissions on directories when they are dragged (copied) from a mounted volume such as a disk image (DMG), which could cause the directories to have less restrictive permissions than intended.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2003/a102803-1.txt.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2003/a102803-1.txt
- http://www.securityfocus.com/bid/8916
- http://www.securityfocus.com/bid/8917
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13537
- http://www.atstake.com/research/advisories/2003/a102803-1.txt

---

#### 443. CVE-2003-0877

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X before 10.3 with core files enabled allows local users to overwrite arbitrary files and read core files via a symlink attack on core files that are created with predictable names in the /cores directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2003/a102803-1.txt.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2003/a102803-1.txt
- http://www.securityfocus.com/bid/8914
- http://www.securityfocus.com/bid/8917
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13542
- http://www.atstake.com/research/advisories/2003/a102803-1.txt

---

#### 444. CVE-2003-0878

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
slpd daemon in Mac OS X before 10.3 allows local users to overwrite arbitrary files via a symlink attack on a temporary file, a different vulnerability than CVE-2003-0875.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 445. CVE-2003-0880

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in Mac OS X before 10.3 allows local users to access Dock functions from behind Screen Effects when Full Keyboard Access is enabled using the Keyboard pane in System Preferences.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 446. CVE-2003-0881

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mail in Mac OS X before 10.3, when configured to use MD5 Challenge Response, uses plaintext authentication if the CRAM-MD5 hashed login fails, which could allow remote attackers to gain privileges by sniffing the password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 447. CVE-2003-0882

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X before 10.3 initializes the TCP timestamp with a constant number, which allows remote attackers to determine the system's uptime via the ID field in a TCP packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 448. CVE-2003-0883

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The System Preferences capability in Mac OS X before 10.3 allows local users to access secure Preference Panes for a short period after an administrator has authenticated to the system.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 449. CVE-2003-0895

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the Mac OS X kernel 10.2.8 and earlier allows local users, and possibly remote attackers, to cause a denial of service (crash), access portions of memory, and possibly execute arbitrary code via a long command line argument (argv[]).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00038.html.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://www.atstake.com/research/advisories/2003/a102803-3.txt
- http://www.securityfocus.com/bid/8913
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13541
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 450. CVE-2001-1411

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Format string vulnerability in gm4 (aka m4) on Mac OS X may allow local users to gain privileges if gm4 is called by setuid programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00038.html.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00038.html
- http://marc.info/?l=bugtraq&m=100368233714229&w=2
- http://www.iss.net/security_center/static/10174.php
- http://www.kb.cert.org/vuls/id/147587
- http://lists.apple.com/mhonarc/security-announce/msg00038.html

---

#### 451. CVE-2003-0804

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x, openbsd:openbsd, freebsd:freebsd

**漏洞描述 / Description**:
The arplookup function in FreeBSD 5.1 and earlier, Mac OS X before 10.2.8, and possibly other BSD-based systems, allows remote attackers on a local subnet to cause a denial of service (resource starvation and panic) via a flood of spoofed ARP requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-03:14.arp.asc.

**参考链接 / References**:
- ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-03:14.arp.asc
- ftp://patches.sgi.com/support/free/security/advisories/20040502-01-P.asc
- http://docs.info.apple.com/article.html?artnum=61798
- ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-03:14.arp.asc
- ftp://patches.sgi.com/support/free/security/advisories/20040502-01-P.asc

---

#### 452. CVE-2003-0913

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the Terminal application for Mac OS X 10.3 (Client and Server) may allow "unauthorized access."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=120269.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=120269
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00040.html
- http://www.securityfocus.com/bid/8979
- https://exchange.xforce.ibmcloud.com/vulnerabilities/13620

---

#### 453. CVE-2003-1005

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
The PKI functionality in Mac OS X 10.2.8 and 10.3.2 allows remote attackers to cause a denial of service (service crash) via malformed ASN.1 sequences.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2003/Dec/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2003/Dec/msg00001.html
- http://secunia.com/advisories/10474/
- http://www.auscert.org.au/render.html?it=3704
- http://www.securityfocus.com/bid/9266
- http://lists.apple.com/archives/security-announce/2003/Dec/msg00001.html

---

#### 454. CVE-2004-1082

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apache:http_server, avaya:communication_manager, avaya:mn100, hp:virtualvault, openbsd:openbsd

**漏洞描述 / Description**:
mod_digest_apple for Apache 1.3.31 and 1.3.32 on Mac OS X Server does not properly verify the nonce of a client response, which allows remote attackers to replay credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Dec/msg00000.html
- http://www.ciac.org/ciac/bulletins/p-049.shtml
- http://www.securityfocus.com/bid/9571
- http://www.securitytracker.com/alerts/2004/Dec/1012414.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18347

---

#### 455. CVE-2004-0085

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the Mail application for Mac OS X 10.1.5 and 10.2.8 with unknown impact, a different vulnerability than CVE-2004-0086.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14992
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504

---

#### 456. CVE-2004-0086

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the Mail application for Mac OS X 10.3.2 has unknown impact and attack vectors, a different vulnerability than CVE-2004-0085.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504

---

#### 457. CVE-2004-0087

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The System Configuration subsystem in Mac OS 10.2.8 and 10.3.2 allows local users to modify network settings, a different vulnerability than CVE-2004-0088.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.osvdb.org/6819
- http://www.securityfocus.com/bid/9504
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14997
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html

---

#### 458. CVE-2004-0088

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The System Configuration subsystem in Mac OS 10.2.8 allows local users to modify network settings, a different vulnerability than CVE-2004-0087.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.osvdb.org/6820
- http://www.securityfocus.com/bid/9504
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.osvdb.org/6820

---

#### 459. CVE-2004-0089

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in TruBlueEnvironment in Mac OS X 10.3.x and 10.2.x allows local users to gain privileges via a long environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.atstake.com/research/advisories/2004/a012704-1.txt
- http://www.kb.cert.org/vuls/id/902374
- http://www.osvdb.org/6821
- http://www.securityfocus.com/bid/9509

---

#### 460. CVE-2004-0092

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in Safari web browser in Mac OS X 10.2.8 and 10.3.2, with unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://www.securityfocus.com/bid/9504

---

#### 461. CVE-2004-0165

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Format string vulnerability in Point-to-Point Protocol (PPP) daemon (pppd) 2.4.0 for Mac OS X 10.3.2 and earlier allows remote attackers to read arbitrary pppd process data, including PAP or CHAP authentication credentials, to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://www.atstake.com/research/advisories/2004/a022304-1.txt
- http://www.kb.cert.org/vuls/id/841742
- http://www.osvdb.org/6822
- http://www.securityfocus.com/bid/9730

---

#### 462. CVE-2004-0166

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in Safari web browser for Mac OS X 10.2.8 related to "the display of URLs in the status bar."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://secunia.com/advisories/10959
- http://www.kb.cert.org/vuls/id/194238
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14993
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html

---

#### 463. CVE-2004-0167

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
DiskArbitration in Mac OS X 10.2.8 and 10.3.2 does not properly initialize writeable removable media.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://secunia.com/advisories/10959
- http://www.kb.cert.org/vuls/id/578886
- http://www.osvdb.org/6824
- http://www.securityfocus.com/bid/9731

---

#### 464. CVE-2004-0168

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in CoreFoundation for Mac OS X 10.3.2, related to "notification logging."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://secunia.com/advisories/10959/
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15299
- http://lists.apple.com/archives/security-announce/2004/Feb/msg00000.html
- http://secunia.com/advisories/10959/

---

#### 465. CVE-2004-0171

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: freebsd:freebsd, openbsd:openbsd

**漏洞描述 / Description**:
FreeBSD 5.1 and earlier, and Mac OS X before 10.3.4, allows remote attackers to cause a denial of service (resource exhaustion of memory buffers and system crash) via a large number of out-of-sequence TCP packets, which prevents the operating system from creating new connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-04:04.tcp.asc.

**参考链接 / References**:
- ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-04:04.tcp.asc
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://www.idefense.com/application/poi/display?id=78&type=vulnerabilities
- http://www.kb.cert.org/vuls/id/395670
- http://www.osvdb.org/4124

---

#### 466. CVE-2003-1008

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in Mac OS X 10.2.8 and 10.3.2 allows local users to bypass the screen saver login window and write a text clipping to the desktop or another application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14195
- http://docs.info.apple.com/article.html?artnum=61798
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14195

---

#### 467. CVE-1999-1306

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 9.1 and earlier does not properly handle extended IP access lists when the IP route cache is enabled and the "established" keyword is set, which could allow attackers to bypass filters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-1992-20.html.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-1992-20.html
- http://www.cert.org/advisories/CA-1992-20.html

---

#### 468. CVE-1999-0161

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
In Cisco IOS 10.3, with the tacacs-ds or tacacs keyword, an extended IP access control list could bypass filtering.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/797.

**参考链接 / References**:
- http://www.osvdb.org/797
- http://www.osvdb.org/797

---

#### 469. CVE-1999-0160

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Some classic Cisco IOS devices have a vulnerability in the PPP CHAP authentication to establish unauthorized PPP connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1099.

**参考链接 / References**:
- http://www.osvdb.org/1099
- http://www.osvdb.org/1099

---

#### 470. CVE-1999-0159

**严重程度 / Severity**: LOW | CVSS: 3.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Attackers can crash a Cisco IOS router or device, provided they can get to an interactive prompt (such as a login).  This applies to some IOS 9.x, 10.x, and 11.x releases.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0159.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0159
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0159

---

#### 471. CVE-1999-0162

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The "established" keyword in some Cisco IOS software allowed an attacker to bypass filtering.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0162.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0162
- https://www.cve.org/CVERecord?id=CVE-1999-0162

---

#### 472. CVE-1999-0063

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 and other versions can be crashed by malicious UDP packets to the syslog port.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0063.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0063
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0063

---

#### 473. CVE-1999-0222

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:router

**漏洞描述 / Description**:
Denial of service in Cisco IOS web server allows attackers to reboot the router using a long URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/60159.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/60159
- http://www.securityfocus.com/archive/1/60159

---

#### 474. CVE-1999-0445

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
In Cisco routers under some versions of IOS 12.0 running NAT, some packets may not be filtered by input access list filters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1104.

**参考链接 / References**:
- http://www.osvdb.org/1104
- http://www.osvdb.org/1104

---

#### 475. CVE-1999-0775

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco Gigabit Switch routers running IOS allow remote attackers to forward unauthorized packets due to improper handling of the "established" keyword in an access list.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0775.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0775
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0775

---

#### 476. CVE-1999-1175

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Web Cache Control Protocol (WCCP) in Cisco Cache Engine for Cisco IOS 11.2 and earlier does not use authentication, which allows remote attackers to redirect HTTP traffic to arbitrary hosts via WCCP packets to UDP port 2048.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/i-054.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/i-054.shtml
- http://www.cisco.com/warp/public/770/wccpauth-pub.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1577
- http://www.ciac.org/ciac/bulletins/i-054.shtml
- http://www.cisco.com/warp/public/770/wccpauth-pub.shtml

---

#### 477. CVE-1999-1464

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Vulnerability in Cisco IOS 11.1CC and 11.1CT with distributed fast switching (DFS) enabled allows remote attackers to bypass certain access control lists when the router switches traffic from a DFS-enabled interface to an interface that does not have DFS enabled, as described by Cisco bug CSCdk35564.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/j-016.shtml.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/j-016.shtml
- http://www.cisco.com/warp/public/770/iosdfsacl-pub.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1401
- http://ciac.llnl.gov/ciac/bulletins/j-016.shtml
- http://www.cisco.com/warp/public/770/iosdfsacl-pub.shtml

---

#### 478. CVE-1999-1465

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Vulnerability in Cisco IOS 11.1 through 11.3 with distributed fast switching (DFS) enabled allows remote attackers to bypass certain access control lists when the router switches traffic from a DFS-enabled input interface to an output interface with a logical subinterface, as described by Cisco bug CSCdk43862.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/j-016.shtml.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/j-016.shtml
- http://www.cisco.com/warp/public/770/iosdfsacl-pub.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1401
- http://ciac.llnl.gov/ciac/bulletins/j-016.shtml
- http://www.cisco.com/warp/public/770/iosdfsacl-pub.shtml

---

#### 479. CVE-2000-0268

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:7500_router, cisco:ubr7200, cisco:system_controller_3640, cisco:7100_router, cisco:as5800

**漏洞描述 / Description**:
Cisco IOS 11.x and 12.x allows remote attackers to cause a denial of service by sending the ENVIRON option to the Telnet daemon before it is ready to accept it, which causes the system to reboot.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/iostelnetopt-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/iostelnetopt-pub.shtml
- http://www.osvdb.org/1289
- http://www.securityfocus.com/bid/1123
- http://www.cisco.com/warp/public/707/iostelnetopt-pub.shtml
- http://www.osvdb.org/1289

---

#### 480. CVE-2000-0380

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The IOS HTTP service in Cisco routers and switches running IOS 11.1 through 12.1 allows remote attackers to cause a denial of service by requesting a URL that contains a %% string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-04/0261.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0261.html
- http://www.cisco.com/warp/public/707/ioshttpserver-pub.shtml
- http://www.osvdb.org/1302
- http://www.securityfocus.com/bid/1154
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0261.html

---

#### 481. CVE-2000-0700

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:gigabit_switch_router_12008, cisco:ios, cisco:gigabit_switch_router_12016, cisco:gigabit_switch_router_12012

**漏洞描述 / Description**:
Cisco Gigabit Switch Routers (GSR) with Fast Ethernet / Gigabit Ethernet cards, from IOS versions 11.2(15)GS1A up to 11.2(19)GS0.2 and some versions of 12.0, do not properly handle line card failures, which allows remote attackers to bypass ACLs or force the interface to stop forwarding packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/gsraclbypassdos-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/gsraclbypassdos-pub.shtml
- http://www.osvdb.org/793
- http://www.osvdb.org/798
- http://www.securityfocus.com/bid/1541
- http://www.cisco.com/warp/public/707/gsraclbypassdos-pub.shtml

---

#### 482. CVE-2000-0984

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The HTTP server in Cisco IOS 12.0 through 12.1 allows local users to cause a denial of service (crash and reload) via a URL containing a "?/" string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ioshttpserverquery-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ioshttpserverquery-pub.shtml
- http://www.securityfocus.com/bid/1838
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5412
- http://www.cisco.com/warp/public/707/ioshttpserverquery-pub.shtml
- http://www.securityfocus.com/bid/1838

---

#### 483. CVE-2001-1434

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0(5)XU through 12.1(2) allows remote attackers to read system administration and topology information via an "snmp-server host" command, which creates a readable "community" community string if one has not been previously created.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml
- http://www.kb.cert.org/vuls/id/848944
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6178
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml
- http://www.kb.cert.org/vuls/id/848944

---

#### 484. CVE-2004-1776

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1(3) and 12.1(3)T allows remote attackers to read and modify device configuration data via the cable-docsis read-write community string used by the Data Over Cable Service Interface Specification (DOCSIS) standard.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml
- http://www.kb.cert.org/vuls/id/840665
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6180
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml
- http://www.kb.cert.org/vuls/id/840665

---

#### 485. CVE-2000-0368

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Classic Cisco IOS 9.1 and later allows attackers with access to the login prompt to obtain portions of the command history of previous users, which may allow the attacker to access sensitive data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/j-009.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/j-009.shtml
- http://www.cisco.com/warp/public/770/ioshist-pub.shtml
- http://www.ciac.org/ciac/bulletins/j-009.shtml
- http://www.cisco.com/warp/public/770/ioshist-pub.shtml

---

#### 486. CVE-2001-0288

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco switches and routers running IOS 12.1 and earlier produce predictable TCP Initial Sequence Numbers (ISNs), which allows remote attackers to spoof or hijack TCP connections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-tcp-isn-random-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-tcp-isn-random-pub.shtml
- http://www.cisco.com/warp/public/707/ios-tcp-isn-random-pub.shtml

---

#### 487. CVE-2001-1183

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
PPTP implementation in Cisco IOS 12.1 and 12.2 allows remote attackers to cause a denial of service (crash) via a malformed packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/PPTP-vulnerability-pub.html.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/PPTP-vulnerability-pub.html
- http://www.kb.cert.org/vuls/id/656315
- http://www.osvdb.org/802
- http://www.securityfocus.com/bid/3022
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6835

---

#### 488. CVE-2001-0537

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
HTTP server for Cisco IOS 11.3 to 12.2 allows attackers to bypass authentication and execute arbitrary commands, when local authorization is being used, by specifying a high access level in the URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2001-14.html.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2001-14.html
- http://www.ciac.org/ciac/bulletins/l-106.shtml
- http://www.cisco.com/warp/public/707/IOS-httplevel-pub.html
- http://www.osvdb.org/578
- http://www.securityfocus.com/archive/1/1601227034.20010702112207%40olympos.org

---

#### 489. CVE-2001-1097

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco routers and switches running IOS 12.0 through 12.2.1 allows a remote attacker to cause a denial of service via a flood of UDP packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99749327219189&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99749327219189&w=2
- http://www.securityfocus.com/archive/1/199558
- http://www.securityfocus.com/bid/3096
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6913
- http://marc.info/?l=bugtraq&m=99749327219189&w=2

---

#### 490. CVE-2001-0711

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 11.x and 12.0 with ATM support allows attackers to cause a denial of service via the undocumented Interim Local Management Interface (ILMI) SNMP community string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-snmp-ilmi-vuln-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-snmp-ilmi-vuln-pub.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6169
- http://www.cisco.com/warp/public/707/ios-snmp-ilmi-vuln-pub.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6169

---

#### 491. CVE-2001-0650

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco devices IOS 12.0 and earlier allow a remote attacker to cause a crash, or bad route updates, via malformed BGP updates with unrecognized transitive attribute.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-082.shtml.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-082.shtml
- http://www.cisco.com/warp/public/707/ios-bgp-attr-corruption-pub.shtml
- http://www.kb.cert.org/vuls/id/106392
- http://www.osvdb.org/1830
- http://www.securityfocus.com/bid/2733

---

#### 492. CVE-2001-1071

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios, cisco:catos

**漏洞描述 / Description**:
Cisco IOS 12.2 and earlier running Cisco Discovery Protocol (CDP) allows remote attackers to cause a denial of service (memory consumption) via a flood of CDP neighbor announcements.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/139491.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/139491
- http://www.osvdb.org/1969
- http://www.securityfocus.com/archive/1/219257
- http://www.securityfocus.com/archive/1/219305
- http://www.securityfocus.com/bid/3412

---

#### 493. CVE-2001-0750

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1(2)T, 12.1(3)T allow remote attackers to cause a denial of service (reload) via a connection to TCP ports 3100-3999, 5100-5999, 7100-7999 and 10100-10999.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-tcp-scanner-reload-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-tcp-scanner-reload-pub.shtml
- http://www.osvdb.org/800
- http://www.securityfocus.com/bid/2804
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6589
- http://www.cisco.com/warp/public/707/ios-tcp-scanner-reload-pub.shtml

---

#### 494. CVE-2001-0929

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS Firewall Feature set, aka Context Based Access Control (CBAC) or Cisco Secure Integrated Software, for IOS 11.2P through 12.2T does not properly check the IP protocol type, which could allow remote attackers to bypass access control lists.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/IOS-cbac-dynacl-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/IOS-cbac-dynacl-pub.shtml
- http://www.kb.cert.org/vuls/id/362483
- http://www.osvdb.org/808
- http://www.securityfocus.com/bid/3588
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7614

---

#### 495. CVE-2001-0861

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 and earlier allows remote attackers to cause a denial of service (CPU consumption) by flooding the router with traffic that generates a large number of ICMP Unreachable replies.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-unreachables-pub.shtml
- http://www.osvdb.org/794
- http://www.securityfocus.com/bid/3534
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7536

---

#### 496. CVE-2001-0862

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not block non-initial packet fragments, which allows remote attackers to bypass the ACL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.osvdb.org/1985
- http://www.securityfocus.com/bid/3535
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7550

---

#### 497. CVE-2001-0863

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not handle the "fragment" keyword in a compiled ACL (Turbo ACL) for packets that are sent to the router, which allows remote attackers to cause a denial of service via a flood of fragments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.osvdb.org/1987
- http://www.securityfocus.com/bid/3539
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7551

---

#### 498. CVE-2001-0864

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not properly handle the implicit "deny ip any any" rule in an outgoing ACL when the ACL contains exactly 448 entries, which can allow some outgoing packets to bypass access restrictions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.osvdb.org/1986
- http://www.securityfocus.com/bid/3536
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7553

---

#### 499. CVE-2001-0865

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not support the "fragment" keyword in an outgoing ACL, which could allow fragmented packets in violation of the intended access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.osvdb.org/1988
- http://www.securityfocus.com/bid/3540
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7552

---

#### 500. CVE-2001-0866

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and lines card based on Engine 2 does not properly handle an outbound ACL when an input ACL is not configured on all the interfaces of a multi port line card, which could allow remote attackers to bypass the intended access controls.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.iss.net/security_center/static/7554.php
- http://www.osvdb.org/1984
- http://www.securityfocus.com/bid/3537

---

#### 501. CVE-2001-0867

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:12000_router

**漏洞描述 / Description**:
Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not properly filter does not properly filter packet fragments even when the "fragment" keyword is used in an ACL, which allows remote attackers to bypass the intended access controls.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-018.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-018.shtml
- http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml
- http://www.osvdb.org/1989
- http://www.securityfocus.com/bid/3538
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7555

---

#### 502. CVE-2002-0339

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 11.1CC through 12.2 with Cisco Express Forwarding (CEF) enabled includes portions of previous packets in the padding of a MAC level packet when the MAC packet's length is less than the IP level packet length.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/IOS-CEF-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/IOS-CEF-pub.shtml
- http://www.iss.net/security_center/static/8296.php
- http://www.kb.cert.org/vuls/id/310387
- http://www.osvdb.org/806
- http://www.securityfocus.com/bid/4191

---

#### 503. CVE-2002-0813

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Heap-based buffer overflow in the TFTP server capability in Cisco IOS 11.1, 11.2, and 11.3 allows remote attackers to cause a denial of service (reset) or modify configuration via a long filename.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103002169829669&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103002169829669&w=2
- http://online.securityfocus.com/archive/1/284634
- http://www.cisco.com/warp/public/707/ios-tftp-long-filename-pub.shtml
- http://www.iss.net/security_center/static/9700.php
- http://www.osvdb.org/854

---

#### 504. CVE-2002-1024

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:css11000_content_services_switch, cisco:ios, cisco:catos, cisco:pix_firewall_software

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.2, when supporting SSH, allows remote attackers to cause a denial of service (CPU consumption) via a large packet that was designed to exploit the SSH CRC32 attack detection overflow (CVE-2001-0144).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/SSH-scanning.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/SSH-scanning.shtml
- http://www.iss.net/security_center/static/9437.php
- http://www.kb.cert.org/vuls/id/290140
- http://www.securityfocus.com/bid/5114
- http://www.cisco.com/warp/public/707/SSH-scanning.shtml

---

#### 505. CVE-2002-1706

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ubr7100, cisco:ios, cisco:ubr7200

**漏洞描述 / Description**:
Cisco IOS software 11.3 through 12.2 running on Cisco uBR7200 and uBR7100 series Universal Broadband Routers allows remote attackers to modify Data Over Cable Service Interface Specification (DOCSIS) settings via a DOCSIS file without a Message Integrity Check (MIC) signature, which is approved by the router.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cmts-MD5-bypass-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cmts-MD5-bypass-pub.shtml
- http://www.securityfocus.com/bid/5041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9368
- http://www.cisco.com/warp/public/707/cmts-MD5-bypass-pub.shtml
- http://www.securityfocus.com/bid/5041

---

#### 506. CVE-2002-1768

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 11.1 through 12.2, when HSRP support is not enabled, allows remote attackers to cause a denial of service (CPU consumption) via randomly sized UDP packets to the Hot Standby Routing Protocol (HSRP) port 1985.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0050.html
- http://www.securityfocus.com/bid/4948
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9282
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html

---

#### 507. CVE-2002-2052

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco 2611 router running IOS 12.1(6.5), possibly an interim release, allows remote attackers to cause a denial of service via port scans such as (1) scanning all ports on a single host and (2) scanning a network of hosts for a single open port through the router.  NOTE: the vendor could not reproduce this issue, saying that the original reporter was using an interim release of the software.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0050.html
- http://www.iss.net/security_center/static/9281.php
- http://www.securityfocus.com/bid/4947
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html

---

#### 508. CVE-2002-2053

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The design of the Hot Standby Routing Protocol (HSRP), as implemented on Cisco IOS 12.1, when using IRPAS, allows remote attackers to cause a denial of service (CPU consumption) via a router with the same IP address as the interface on which HSRP is running, which causes a loop.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0050.html
- http://www.iss.net/security_center/static/9283.php
- http://www.securityfocus.com/bid/4949
- http://archives.neohapsis.com/archives/bugtraq/2002-06/0027.html

---

#### 509. CVE-2002-2208

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: extended_interior_gateway_routing_protocol:extended_interior_gateway_routing_protocol, cisco:ios

**漏洞描述 / Description**:
Extended Interior Gateway Routing Protocol (EIGRP), as implemented in Cisco IOS 11.3 through 12.2 and other products, allows remote attackers to cause a denial of service (flood) by sending a large number of spoofed EIGRP neighbor announcements, which results in an ARP storm on the local network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040330.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040330.html
- http://marc.info/?l=full-disclosure&m=113504451523186&w=2
- http://secunia.com/advisories/7766
- http://securitytracker.com/id?1005840
- http://www.cisco.com/en/US/tech/tk365/technologies_security_notice09186a008011c5e1.html

---

#### 510. CVE-2002-2239

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:catalyst_7600, cisco:ios, cisco:catalyst_6500

**漏洞描述 / Description**:
The Cisco Optical Service Module (OSM) for the Catalyst 6500 and 7600 series running Cisco IOS 12.1(8)E through 12.1(13.4)E allows remote attackers to cause a denial of service (hang) via a malformed packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/osm-lc-ios-pkt-vuln-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/osm-lc-ios-pkt-vuln-pub.shtml
- http://www.securityfocus.com/bid/6358
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10823
- http://www.cisco.com/warp/public/707/osm-lc-ios-pkt-vuln-pub.shtml
- http://www.securityfocus.com/bid/6358

---

#### 511. CVE-2002-2315

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 11.2.x and 12.0.x does not limit the size of its redirect table, which allows remote attackers to cause a denial of service (memory consumption) via spoofed ICMP redirect packets to the router.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/273421.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/273421
- http://online.securityfocus.com/archive/1/273488
- http://www.iss.net/security_center/static/9129.php
- http://www.securityfocus.com/bid/4786
- http://online.securityfocus.com/archive/1/273421

---

#### 512. CVE-2002-2379

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:as5350

**漏洞描述 / Description**:
Cisco AS5350 IOS 12.2(11)T with access control lists (ACLs) applied and possibly with ssh running allows remote attackers to cause a denial of service (crash) via a port scan, possibly due to an ssh bug. NOTE: this issue could not be reproduced by the vendor

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2002/10/msg00397.html.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2002/10/msg00397.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2002/10/msg00411.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2002/10/msg00413.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2002/10/msg00420.html
- http://www.cisco.com/en/US/products/hw/univgate/ps501/products_security_notice09186a008024dba2.html

---

#### 513. CVE-2003-0100

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Buffer overflow in Cisco IOS 11.2.x to 12.0.x allows remote attackers to cause a denial of service and possibly execute commands via a large number of OSPF neighbor announcements.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=104576100719090&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=104576100719090&w=2
- http://marc.info/?l=bugtraq&m=104587206702715&w=2
- http://www.iss.net/security_center/static/11373.php
- http://www.securityfocus.com/bid/6895
- http://marc.info/?l=bugtraq&m=104576100719090&w=2

---

#### 514. CVE-2003-0305

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Service Assurance Agent (SAA) in Cisco IOS 12.0 through 12.2, aka Response Time Reporter (RTR), allows remote attackers to cause a denial of service (crash) via malformed RTR packets to port 1967.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20030515-saa.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20030515-saa.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5608
- http://www.cisco.com/warp/public/707/cisco-sa-20030515-saa.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5608

---

#### 515. CVE-2003-0567

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ons_15454_optical_transport_platform, cisco:ios, cisco:optical_networking_systems_software

**漏洞描述 / Description**:
Cisco IOS 11.x and 12.0 through 12.2 allows remote attackers to cause a denial of service (traffic block) by sending a particular sequence of IPv4 packets to an interface on the device, causing the input queue on that interface to be marked as full.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2003-July/006743.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2003-July/006743.html
- http://www.cert.org/advisories/CA-2003-15.html
- http://www.cert.org/advisories/CA-2003-17.html
- http://www.cisco.com/warp/public/707/cisco-sa-20030717-blocked.shtml
- http://www.kb.cert.org/vuls/id/411332

---

#### 516. CVE-2003-0511

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The web server for Cisco Aironet AP1x00 Series Wireless devices running certain versions of IOS 12.2 allow remote attackers to cause a denial of service (reload) via a malformed URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0055.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0055.html
- http://www.cisco.com/warp/public/707/cisco-sa-20030728-ap1x00.shtml
- http://www.vigilante.com/inetsecurity/advisories/VIGILANTE-2003001.htm
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5834
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0055.html

---

#### 517. CVE-2017-2458

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Keyboards" component. A buffer overflow allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 518. CVE-2017-2461

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "CoreText" component. It allows remote attackers to cause a denial of service (resource consumption) via a crafted text message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 519. CVE-2017-2462

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Audio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- http://zerodayinitiative.com/advisories/ZDI-17-189/
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602

---

#### 520. CVE-2017-2467

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "ImageIO" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 521. CVE-2017-2472

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (use-after-free) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 522. CVE-2017-2473

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 523. CVE-2017-2474

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. An off-by-one error allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 524. CVE-2017-2477

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "libxslt" component. It allows remote attackers to cause a denial of service (memory corruption) or possibly have unspecified other impact via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97303.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97303
- https://support.apple.com/HT207615
- http://www.securityfocus.com/bid/97303
- https://support.apple.com/HT207615

---

#### 525. CVE-2017-2478

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 526. CVE-2017-2482

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. A buffer overflow allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 527. CVE-2017-2483

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. A buffer overflow allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 528. CVE-2017-2485

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Security" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted X.509 certificate file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97132.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97132
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 529. CVE-2017-2487

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "FontParser" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted font file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97137.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97137
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615

---

#### 530. CVE-2017-2489

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to obtain sensitive information from kernel memory via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97300.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97300
- https://support.apple.com/HT207615
- https://www.exploit-db.com/exploits/41798/
- http://www.securityfocus.com/bid/97300
- https://support.apple.com/HT207615

---

#### 531. CVE-2017-2490

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3 is affected. macOS before 10.12.4 is affected. tvOS before 10.2 is affected. watchOS before 3.2 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97301.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97301
- https://support.apple.com/HT207601
- https://support.apple.com/HT207602
- https://support.apple.com/HT207615
- https://support.apple.com/HT207617

---

#### 532. CVE-2017-6974

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.4 is affected. The issue involves the system-installation subsystem of the "System Integrity Protection" component. It allows attackers to modify the contents of a protected disk location via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/97140.

**参考链接 / References**:
- http://www.securityfocus.com/bid/97140
- http://www.securitytracker.com/id/1038138
- https://support.apple.com/HT207615
- http://www.securityfocus.com/bid/97140
- http://www.securitytracker.com/id/1038138

---

#### 533. CVE-2017-2494

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 534. CVE-2017-2497

**严重程度 / Severity**: MEDIUM | CVSS: 6.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. The issue involves the "iBooks" component. It allows remote attackers to trigger visits to arbitrary URLs via a crafted book.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 535. CVE-2017-2501

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "Kernel" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 536. CVE-2017-2502

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "CoreAudio" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 537. CVE-2017-2503

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 538. CVE-2017-2507

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 539. CVE-2017-2509

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://www.exploit-db.com/exploits/42046/
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 540. CVE-2017-2512

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Sandbox" component. It allows attackers to conduct sandbox-escape attacks or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 541. CVE-2017-2513

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "SQLite" component. A use-after-free vulnerability allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted SQL statement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 542. CVE-2017-2516

**严重程度 / Severity**: MEDIUM | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://www.exploit-db.com/exploits/42047/
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 543. CVE-2017-2518

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:tvos, debian:debian_linux, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted SQL statement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://lists.debian.org/debian-lts-announce/2019/01/msg00009.html
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798

---

#### 544. CVE-2017-2519

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:tvos, debian:debian_linux, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted SQL statement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://lists.debian.org/debian-lts-announce/2019/01/msg00009.html
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798

---

#### 545. CVE-2017-2520

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:tvos, debian:debian_linux, apple:watchos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted SQL statement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://lists.debian.org/debian-lts-announce/2019/01/msg00009.html
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798

---

#### 546. CVE-2017-2522

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "CoreFoundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via crafted data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98588.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98588
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800
- https://support.apple.com/HT207801

---

#### 547. CVE-2017-2523

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "Foundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via crafted data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98584.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98584
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800
- https://support.apple.com/HT207801

---

#### 548. CVE-2017-2524

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "TextInput" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via crafted data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 549. CVE-2017-2527

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "CoreAnimation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory consumption and application crash) via crafted data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://www.exploit-db.com/exploits/42052/
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 550. CVE-2017-2533

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "DiskArbitration" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- http://www.zerodayinitiative.com/advisories/ZDI-17-357/
- https://phoenhex.re/2017-06-09/pwn2own-diskarbitrationd-privesc
- https://support.apple.com/HT207797
- https://www.exploit-db.com/exploits/42146/

---

#### 551. CVE-2017-2534

**严重程度 / Severity**: HIGH | CVSS: 8.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Speech Framework" component. It allows attackers to conduct sandbox-escape attacks via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 552. CVE-2017-2535

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Security" component. It allows attackers to conduct sandbox-escape attacks or cause a denial of service (resource consumption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 553. CVE-2017-2537

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "WindowServer" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 554. CVE-2017-2540

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "WindowServer" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 555. CVE-2017-2541

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "WindowServer" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 556. CVE-2017-2542

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Multi-Touch" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 557. CVE-2017-2543

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Multi-Touch" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 558. CVE-2017-2545

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "IOGraphics" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 559. CVE-2017-2546

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 560. CVE-2017-2548

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "WindowServer" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 561. CVE-2017-6977

**严重程度 / Severity**: HIGH | CVSS: 8.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Speech Framework" component. It allows attackers to conduct sandbox-escape attacks or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 562. CVE-2017-6978

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "Accessibility Framework" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://www.exploit-db.com/exploits/42056/
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 563. CVE-2017-6979

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:watchos, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "IOSurface" component. A race condition allows attackers to execute arbitrary code in a privileged context via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 564. CVE-2017-6981

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. The issue involves the "iBooks" component. It allows attackers to execute arbitrary code in a privileged context via a crafted app that uses symlinks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 565. CVE-2017-6983

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://source.android.com/security/bulletin/2017-09-01
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- http://www.securitytracker.com/id/1038484

---

#### 566. CVE-2017-6985

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "NVIDIA Graphics Drivers" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 567. CVE-2003-1010

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in fs_usage in Mac OS X 10.2.8 and 10.3.2 and Mac OS X Server 10.2.8 and 10.3.2 allows local users to gain privileges via unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.securityfocus.com/bid/9265
- https://exchange.xforce.ibmcloud.com/vulnerabilities/14193
- http://docs.info.apple.com/article.html?artnum=61798
- http://www.securityfocus.com/bid/9265

---

#### 568. CVE-2004-0428

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in CoreFoundation in Mac OS X 10.3.3 and Mac OS X 10.3.3 Server, related to "the handling of an environment variable," has unknown attack vectors and unknown impact.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.virus.org/macsec-0405/msg00000.html.

**参考链接 / References**:
- http://lists.virus.org/macsec-0405/msg00000.html
- http://secunia.com/advisories/11539
- http://securitytracker.com/id?1010045
- http://www.auscert.org.au/render.html?it=4070
- http://www.securityfocus.com/bid/10270

---

#### 569. CVE-2004-0382

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the CUPS printing system in Mac OS X 10.3.3 and Mac OS X 10.2.8 with unknown impact, possibly related to a configuration file setting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00047.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15769
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00047.html

---

#### 570. CVE-2004-0383

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in Mail for Mac OS X 10.3.3 and 10.2.8, with unknown impact, related to "the handling of HTML-formatted email."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=61798.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00047.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15768
- http://docs.info.apple.com/article.html?artnum=61798
- http://lists.apple.com/mhonarc/security-announce/msg00047.html

---

#### 571. CVE-2004-0485

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The default protocol helper for the disk: URI on Mac OS X 10.3.3 and 10.2.8 allows remote attackers to write arbitrary files by causing a disk image file (.dmg) to be mounted as a disk volume.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://fundisom.com/owned/warning.

**参考链接 / References**:
- http://fundisom.com/owned/warning
- http://lists.apple.com/mhonarc/security-announce/msg00053.html
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://secunia.com/advisories/11622/
- http://www.kb.cert.org/vuls/id/210606

---

#### 572. CVE-2004-0486

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
HelpViewer in Mac OS X 10.3.3 and 10.2.8 processes scripts that it did not initiate, which can allow attackers to execute arbitrary code, an issue that was originally reported as a directory traversal vulnerability in the Safari web browser using the runscript parameter in a help: URI handler.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2004-05/0837.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2004-05/0837.html
- http://lists.apple.com/mhonarc/security-announce/msg00053.html
- http://secunia.com/advisories/11622/
- http://securitytracker.com/id?1010167
- http://www.fundisom.com/owned/warning

---

#### 573. CVE-2004-0489

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Argument injection vulnerability in the SSH URI handler for Safari on Mac OS 10.3.3 and earlier allows remote attackers to (1) execute arbitrary code via the ProxyCommand option or (2) conduct port forwarding via the -R option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-May/021871.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-May/021871.html
- http://www.insecure.ws/article.php?story=200405222251133
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16242
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-May/021871.html
- http://www.insecure.ws/article.php?story=200405222251133

---

#### 574. CVE-2004-0538

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
LaunchServices in Mac OS X 10.3.4 and 10.2.8 automatically registers and executes new applications, which could allow attackers to execute arbitrary code without warning the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25785.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=25785
- http://docs.info.apple.com/article.html?artnum=25785

---

#### 575. CVE-2004-0539

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The "Show in Finder" button in the Safari web browser in Mac OS X 10.3.4 and 10.2.8 may execute downloaded applications, which could allow remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=25785.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=25785
- http://www.kb.cert.org/vuls/id/773190
- http://docs.info.apple.com/article.html?artnum=25785
- http://www.kb.cert.org/vuls/id/773190

---

#### 576. CVE-2004-0513

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unspecified vulnerability in Mac OS X before 10.3.4 has unknown impact and attack vectors related to "logging when tracing system calls."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/May/msg00005.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/May/msg00005.html
- http://www.securityfocus.com/bid/10432
- http://www.securitytracker.com/alerts/2004/May/1010329.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16291
- http://lists.apple.com/archives/security-announce/2004/May/msg00005.html

---

#### 577. CVE-2004-0514

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in LoginWindow for Mac OS X 10.3.4, related to "handling of directory services lookups."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接 / References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010330
- http://www.kb.cert.org/vuls/id/174790
- http://www.securityfocus.com/bid/10432
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16289

---

#### 578. CVE-2004-0515

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in LoginWindow for Mac OS X 10.3.4, related to "handling of console log files."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接 / References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010330
- http://www.securityfocus.com/bid/10432
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16289
- http://lists.seifried.org/pipermail/security/2004-May/003743.html

---

#### 579. CVE-2004-0516

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Mac OS X 10.3.4, related to "package installation scripts," a different vulnerability than CVE-2004-0517.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接 / References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010331
- http://www.securityfocus.com/bid/10432
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16290
- http://lists.seifried.org/pipermail/security/2004-May/003743.html

---

#### 580. CVE-2004-0517

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Mac OS X 10.3.4, related to "handling of process IDs during package installation," a different vulnerability than CVE-2004-0516.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.seifried.org/pipermail/security/2004-May/003743.html.

**参考链接 / References**:
- http://lists.seifried.org/pipermail/security/2004-May/003743.html
- http://securitytracker.com/id?1010331
- http://www.securityfocus.com/bid/10432
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16290
- http://lists.seifried.org/pipermail/security/2004-May/003743.html

---

#### 581. CVE-2004-0822

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in The Core Foundation framework (CoreFoundation.framework) in Mac OS X 10.2.8, 10.3.4, and 10.3.5 allows local users to execute arbitrary code via a certain environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

**参考链接 / References**:
- http://secunia.com/advisories/12491/
- http://www.ciac.org/ciac/bulletins/o-212.shtml
- http://www.kb.cert.org/vuls/id/545446
- http://www.securityfocus.com/advisories/7148
- http://www.securityfocus.com/bid/11136

---

#### 582. CVE-2004-0743

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Safari in Mac OS X before 10.3.5, after sending form data using the POST method, may re-send the data to a GET method URL if that URL is redirected after the POST data and the user uses the forward or backward buttons, which may cause an information leak.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/mhonarc/security-announce/msg00056.html.

**参考链接 / References**:
- http://lists.apple.com/mhonarc/security-announce/msg00056.html
- http://www.kb.cert.org/vuls/id/128414
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16944
- http://lists.apple.com/mhonarc/security-announce/msg00056.html
- http://www.kb.cert.org/vuls/id/128414

---

#### 583. CVE-2004-0744

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The TCP/IP Networking component in Mac OS X before 10.3.5 allows remote attackers to cause a denial of service (memory and resource consumption) via a "Rose Attack" that involves sending a subset of small IP fragments that do not form a complete, larger packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://digital.net/~gandalf/Rose_Frag_Attack_Explained.txt.

**参考链接 / References**:
- http://digital.net/~gandalf/Rose_Frag_Attack_Explained.txt
- http://marc.info/?l=bugtraq&m=108075899619193&w=2
- http://marc.info/?l=bugtraq&m=108308604119618&w=2
- http://www.auscert.org.au/render.html?it=4291
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16946

---

#### 584. CVE-2004-0090

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Windows File Sharing for Mac OS X 10.1.5 through 10.3.2 does not "shutdown properly," which has unknown impact and attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html
- http://secunia.com/advisories/10723/
- http://www.auscert.org.au/render.html?it=3791&cid=1
- http://www.securityfocus.com/bid/9504
- http://lists.apple.com/archives/security-announce/2004/Jan/msg00000.html

---

#### 585. CVE-2004-0821

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The CFPlugIn in Core Foundation framework in Mac OS X allows user supplied libraries to be loaded, which could allow local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12491/.

**参考链接 / References**:
- http://secunia.com/advisories/12491/
- http://www.auscert.org.au/render.html?it=4363
- http://www.auscert.org.au/render.html?it=4363
- http://www.ciac.org/ciac/bulletins/o-212.shtml
- http://www.kb.cert.org/vuls/id/704110

---

#### 586. CVE-2004-0824

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
PPPDialer for Mac OS X 10.2.8 through 10.3.5 allows local users to overwrite system files via a symlink attack on PPPDialer log files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1011175.

**参考链接 / References**:
- http://securitytracker.com/id?1011175
- http://www.auscert.org.au/render.html?it=4363
- http://www.ciac.org/ciac/bulletins/o-212.shtml
- http://www.securityfocus.com/advisories/7148
- http://www.securityfocus.com/bid/11139

---

#### 587. CVE-2004-0825

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
QuickTime Streaming Server in Mac OS X Server 10.2.8, 10.3.4, and 10.3.5 allows remote attackers to cause a denial of service (application deadlock) via a certain sequence of operations.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=109467471617466&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=109467471617466&w=2
- http://secunia.com/advisories/12491
- http://securitytracker.com/id?1011176
- http://www.ciac.org/ciac/bulletins/o-212.shtml
- http://www.kb.cert.org/vuls/id/914870

---

#### 588. CVE-2004-1481

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: realnetworks:helix_player, realnetworks:realplayer, realnetworks:realone_player

**漏洞描述 / Description**:
Integer overflow in pnen3260.dll in RealPlayer 8 through 10.5 (6.0.12.1040) and earlier, and RealOne Player 1 or 2 on Windows or Mac OS, allows remote attackers to execute arbitrary code via a SMIL file and a .rm movie file with a large length field for the data chunk, which leads to a heap-based buffer overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=109708374115061&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=109708374115061&w=2
- http://secunia.com/advisories/12672
- http://www.securityfocus.com/bid/11309
- http://www.service.real.com/help/faq/security/040928_player/EN/
- https://exchange.xforce.ibmcloud.com/vulnerabilities/17549

---

#### 589. CVE-2004-1832

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in the GUI admin service in Mac OS X Server 10.3 allows remote attackers to cause a denial of service (crash and restart) via a large amount of data to TCP port 660.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=107965605008575&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=107965605008575&w=2
- http://marc.info/?l=bugtraq&m=107971225327629&w=2
- http://www.securityfocus.com/bid/9914
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15533
- http://marc.info/?l=bugtraq&m=107965605008575&w=2

---

#### 590. CVE-2004-2228

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: mozilla:firefox

**漏洞描述 / Description**:
Mozilla Firefox before 1.0 is installed with world-writable permissions on Mac OS X, which allows local users to gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/13144.

**参考链接 / References**:
- http://secunia.com/advisories/13144
- http://secunia.com/advisories/13724
- http://security.gentoo.org/glsa/glsa-200501-03.xml
- http://www.osvdb.org/11592
- http://www.securityfocus.com/bid/11644

---

#### 591. CVE-2004-2335

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: macromedia:contribute, macromedia:studio

**漏洞描述 / Description**:
The Macromedia installers and e-licensing client on Mac OS X, as used for Macromedia Contribute 2, Director, Dreamweaver, Fireworks, Flash, and Studio, install the AuthenticationService setuid and writable by other users, which allows local users to gain privileges by modifying the program.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/11123.

**参考链接 / References**:
- http://secunia.com/advisories/11123
- http://www.macromedia.com/devnet/security/security_zone/mpsb04-03.html
- http://www.securityfocus.com/bid/9862
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15465
- http://secunia.com/advisories/11123

---

#### 592. CVE-2004-1199

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:safari

**漏洞描述 / Description**:
Safari 1.2.4 on Mac OS X 10.3.6 allows remote attackers to cause a denial of service (application crash from memory exhaustion), as demonstrated using Javascript code that continuously creates nested arrays and then sorts the newly created arrays.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029458.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029458.html
- http://www.securityfocus.com/bid/11759
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18282
- http://lists.grok.org.uk/pipermail/full-disclosure/2004-November/029458.html
- http://www.securityfocus.com/bid/11759

---

#### 593. CVE-2005-0193

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: isync:mrouter

**漏洞描述 / Description**:
Buffer overflow in the (1) -v and (2) -a switches in mRouter in iSync 1.5 in Mac OS X 10.3.7 and earlier allows local users to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00001.html
- http://marc.info/?l=bugtraq&m=110642400018425&w=2
- http://secunia.com/advisories/13965
- http://securitytracker.com/id?1012974
- http://www.securityfocus.com/bid/12334

---

#### 594. CVE-2004-0921

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:quicktime, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server on Mac OS X 10.3.x to 10.3.5, when a guest has mounted an AFP volume, allows the guest to "terminate authenticated user mounts" via modified SessionDestroy packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322

---

#### 595. CVE-2004-0922

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:quicktime, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server on Mac OS X 10.3.x to 10.3.5, under certain conditions, does not properly set the guest group ID, which causes AFP to change a write-only AFP Drop Box to be read-write when the Drop Box is on a share that is mounted by a guest, which allows attackers to read the Drop Box.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322

---

#### 596. CVE-2004-0924

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: easy_software_products:cups, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
NetInfo Manager on Mac OS X 10.3.x through 10.3.5, after an initial root login, reports the root account as being disabled, even when it has not.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322

---

#### 597. CVE-2004-0925

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Postfix on Mac OS X 10.3.x through 10.3.5, with SMTPD AUTH enabled, does not properly clear the username between authentication attempts, which allows users with the longest username to prevent other valid users from being able to authenticate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html

---

#### 598. CVE-2004-0927

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: easy_software_products:cups, apple:mac_os_x_server, apple:mac_os_x

**漏洞描述 / Description**:
ServerAdmin in Mac OS X 10.2.8 through 10.3.5 uses the same example self-signed certificate on each system, which allows remote attackers to decrypt sessions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322
- http://lists.apple.com/archives/security-announce/2004/Oct/msg00000.html
- http://www.securityfocus.com/bid/11322

---

#### 599. CVE-2004-1021

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:ical

**漏洞描述 / Description**:
iCal before 1.5.4 on Mac OS X 10.2.3, and other later versions, does not alert the user when handling calendars that use alarms, which allows attackers to execute programs and send e-mail via alarms.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce//2004/Nov/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce//2004/Nov/msg00000.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18209
- http://lists.apple.com/archives/security-announce//2004/Nov/msg00000.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18209

---

#### 600. CVE-2005-0713

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The Bluetooth Setup Assistant for Mac OS X before 10.3.8 can be launched without a keyboard or Bluetooth device, which allows local users to bypass access restrictions and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

---

#### 601. CVE-2005-0715

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AFP Server in Mac OS X before 10.3.8 uses insecure permissions for "Drop Boxes," which allows local users to read the contents of a Drop Box.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

---

#### 602. CVE-2005-0716

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in the Core Foundation Library in Mac OS X 10.3.5 and 10.3.6, and possibly earlier versions, allows local users to execute arbitrary code via a long CF_CHARSET_PATH environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://www.idefense.com/application/poi/display?id=219&type=vulnerabilities
- http://www.securityfocus.com/bid/13224
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://www.idefense.com/application/poi/display?id=219&type=vulnerabilities

---

#### 603. CVE-2005-0125

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The "at" commands on Mac OS X 10.3.7 and earlier do not properly drop privileges, which allows local users to (1) delete arbitrary files via atrm, (2) execute arbitrary programs via the -f argument to batch, or (3) read arbitrary files via the -f argument to batch, which generates a job file that is readable by the local user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html
- http://marc.info/?l=bugtraq&m=110685027017411&w=2
- http://www.digitalmunition.com/DMA%5B2005-0127a%5D.txt
- http://www.kb.cert.org/vuls/id/678150
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18981

---

#### 604. CVE-2005-0126

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
ColorSync on Mac OS X 10.3.7 and 10.3.8 allows attackers to execute arbitrary code via malformed ICC color profiles that modify the heap.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html
- http://securitytracker.com/id?1013000
- http://www.kb.cert.org/vuls/id/980078
- http://www.securityfocus.com/bid/12367
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19083

---

#### 605. CVE-2005-0127

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Mail in Mac OS X 10.3.7, when generating a Message-ID header, generates a GUUID that includes information that identifies the Ethernet hardware being used, which allows remote attackers to link mail messages to a particular machine.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jan/msg00001.html
- http://secunia.com/advisories/14005
- http://securitytracker.com/id?1013001
- http://www.kb.cert.org/vuls/id/464662
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19085

---

#### 606. CVE-2005-0342

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The Finder in Mac OS X and earlier allows local users to overwrite arbitrary files and gain privileges by creating a hard link from the .DS_Store file to an arbitrary file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://marc.info/?l=bugtraq&m=110780124707975&w=2
- http://secunia.com/advisories/14188
- http://www.securityfocus.com/bid/12458
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19253

---

#### 607. CVE-2005-0418

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:j2se

**漏洞描述 / Description**:
Argument injection vulnerability in Java Web Start for J2SE 1.4.2 up to 1.4.2_06, on Mac OS X, allows untrusted applications to gain privileges via the value parameter of a property tag in a JNLP file. NOTE: it is highly likely that this item will be MERGED with CVE-2005-0836.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00001.html

---

#### 608. CVE-2005-0712

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X before 10.3.8 users world-writable permissions for certain directories, which may allow local users to gain privileges, possibly via the receipt cache or ColorSync profiles.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Mar/msg00000.html

---

#### 609. CVE-2005-0970

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.3.9 and earlier allows users to install, create, and execute setuid/setgid scripts, contrary to the intended design, which may allow attackers to conduct unauthorized activities with escalated privileges via vulnerable scripts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html

---

#### 610. CVE-2005-0975

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: opendarwin:darwin_kernel, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer signedness error in the parse_machfile function in the mach-o loader (mach_loader.c) for the Darwin Kernel as used in Mac OS X 10.3.7, and other versions before 10.3.9, allows local users to cause a denial of service (CPU consumption) via a crafted mach-o header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://felinemenace.org/advisories/macosx.txt.

**参考链接 / References**:
- http://felinemenace.org/advisories/macosx.txt
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://marc.info/?l=bugtraq&m=110616533903671&w=2
- http://secunia.com/advisories/13902
- http://securitytracker.com/id?1012941

---

#### 611. CVE-2005-1343

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Stack-based buffer overflow in the VPN daemon (vpnd) for Mac OS X before 10.3.9 allows local users to execute arbitrary code via a long -i (Server_id) argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.kb.cert.org/vuls/id/706838
- http://www.us-cert.gov/cas/techalerts/TA05-136A.html
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

---

#### 612. CVE-2005-1387

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: kristofer_szymanski:cocktail

**漏洞描述 / Description**:
Cocktail 3.5.4 and possibly earlier in Mac OS X passes the administrative password on the command line to sudo in cleartext, which allows local users to gain sensitive information by running listing processes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=111480898530362&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=111480898530362&w=2
- http://secunia.com/advisories/15201
- http://www.osvdb.org/16046
- http://www.securityfocus.com/bid/13449
- http://marc.info/?l=bugtraq&m=111480898530362&w=2

---

#### 613. CVE-2005-1430

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Mac OS X 10.3.x and earlier uses insecure permissions for a pseudo terminal tty (pty) that is managed by a non-setuid program, which allows local users to read or modify sessions of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.security-focus.com/archive/1/397306.

**参考链接 / References**:
- http://www.security-focus.com/archive/1/397306
- http://www.security-focus.com/archive/1/397306

---

#### 614. CVE-2005-1330

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AppKit in Mac OS X 10.3.9 allows attackers to cause a denial of service (Cocoa application crash) via a malformed TIFF image that causes the NXSeek to use an incorrect offset, leading to an unhandled exception.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

---

#### 615. CVE-2005-1332

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Bluetooth-enabled systems in Mac OS X 10.3.9 enables the Bluetooth file exchange service by default, which allows remote attackers to access files without the user being notified, and local users to access files via the default directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://docs.info.apple.com/article.html?artnum=301381.

**参考链接 / References**:
- http://docs.info.apple.com/article.html?artnum=301381
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.digitalmunition.com/DMA%5B2005-0502a%5D.txt
- http://www.kb.cert.org/vuls/id/258390
- http://www.us-cert.gov/cas/techalerts/TA05-136A.html

---

#### 616. CVE-2005-1333

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Directory traversal vulnerability in the Bluetooth file and object exchange (OBEX) services in Mac OS X 10.3.9 allows remote attackers to read arbitrary files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.digitalmunition.com/DMA%5B2005-0502a%5D.txt
- http://www.securityfocus.com/bid/13491
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

---

#### 617. CVE-2005-1335

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in Mac OS X 10.3.9 allows local users to gain privileges via (1) chfn, (2) chpass, and (3) chsh, which "use external helper programs in an insecure manner."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.kb.cert.org/vuls/id/331694
- http://www.us-cert.gov/cas/techalerts/TA05-136A.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.kb.cert.org/vuls/id/331694

---

#### 618. CVE-2005-1336

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in the Foundation framework for Mac OS X 10.3.9 allows local users to execute arbitrary code via a long environment variable.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.kb.cert.org/vuls/id/582934
- http://www.us-cert.gov/cas/techalerts/TA05-136A.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://www.kb.cert.org/vuls/id/582934

---

#### 619. CVE-2005-1338

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Mac OS X 10.3.9, when using an LDAP server that does not use ldap_extended_operation, may store initial LDAP passwords for new accounts in plaintext.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

---

#### 620. CVE-2005-1339

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
lukemftpd in Mac OS X 10.3.9 allows remote authenticated users to escape the chroot environment by logging in with their full name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

---

#### 621. CVE-2005-1340

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
The HTTP proxy service in Server Admin for Mac OS X 10.3.9 does not restrict access when it is enabled, which allows remote attackers to use the proxy.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/May/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00001.html

---

#### 622. CVE-2005-1505

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mail

**漏洞描述 / Description**:
The new account wizard in Mail.app 2.0 in Mac OS 10.4, when configuring an IMAP mail account and checking the credentials, does not prompt the user to use SSL until after the password has already been sent, which causes the password to be sent in plaintext.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=111539448630095&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=111539448630095&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/20670
- http://marc.info/?l=bugtraq&m=111539448630095&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/20670

---

#### 623. CVE-2005-0969

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Heap-based buffer overflow in the syscall emulation functionality in Mac OS X before 10.3.9 allows local users to cause a denial of service (kernel panic) and possibly execute arbitrary code via crafted parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html

---

#### 624. CVE-2005-0971

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Stack-based buffer overflow in the semop system call in Mac OS X 10.3.9 and earlier allows local users to gain privileges via crafted arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://www.kb.cert.org/vuls/id/212190
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://www.kb.cert.org/vuls/id/212190

---

#### 625. CVE-2005-0972

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in the searchfs system call in Mac OS X 10.3.9 and earlier allows local users to execute arbitrary code via crafted parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://www.kb.cert.org/vuls/id/185702
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://www.kb.cert.org/vuls/id/185702

---

#### 626. CVE-2005-0973

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the setsockopt system call in Mac OS X 10.3.9 and earlier allows local users to cause a denial of service (memory exhaustion) via crafted arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html

---

#### 627. CVE-2005-0974

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Unknown vulnerability in the nfs_mount call in Mac OS X 10.3.9 and earlier allows local users to gain privileges via crafted arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html
- http://www.kb.cert.org/vuls/id/713614
- http://lists.apple.com/archives/security-announce/2005/Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/May/msg00004.html

---

#### 628. CVE-2005-1307

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: adobe:version_cue, apple:mac_os_x

**漏洞描述 / Description**:
The (1) stopserver.sh and (2) startserver.sh scripts in Adobe Version Cue on Mac OS X uses the current working directory to find and execute the productname.sh script, which allows local users to execute arbitrary code by copying and calling the scripts from a user-controlled directory.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2004-12/0040.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2004-12/0040.html
- http://marc.info/?l=bugtraq&m=111627622403544&w=2
- http://secunia.com/advisories/13399
- http://securitytracker.com/id?1012446
- http://www.adobe.com/support/techdocs/331621.html

---

#### 629. CVE-2005-1795

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: clam_anti-virus:clamav

**漏洞描述 / Description**:
The filecopy function in misc.c in Clam AntiVirus (ClamAV) before 0.85, on Mac OS, allows remote attackers to execute arbitrary code via a virus in a filename that contains shell metacharacters, which are not properly handled when HFS permissions prevent the file from being deleted and ditto is invoked.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1014070.

**参考链接 / References**:
- http://securitytracker.com/id?1014070
- http://www.sentinelchicken.com/advisories/clamav
- http://securitytracker.com/id?1014070
- http://www.sentinelchicken.com/advisories/clamav

---

#### 630. CVE-2005-1720

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
AFP Server for Mac OS X 10.4.1, when using an ACL enabled volume, does not properly remove an ACL when a file is copied to a directory that does not use ACLs, which will override the POSIX file permissions for that ACL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

---

#### 631. CVE-2005-1721

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:afp_server

**漏洞描述 / Description**:
Buffer overflow in the legacy client support for AFP Server for Mac OS X 10.4.1 allows attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014138
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://securitytracker.com/id?1014138

---

#### 632. CVE-2005-1722

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Unknown vulnerability in the CoreGraphics Window Server for Mac OS X 10.4.x up to 10.4.1 allows local users to inject arbitrary commands into root sessions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html
- http://lists.apple.com/archives/security-announce/2005/Jun/msg00000.html

---

#### 633. CVE-2005-2501

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in AppKit for Mac OS X 10.3.9 and 10.4.2 allows external user-assisted attackers to execute arbitrary code via a crafted Rich Text Format (RTF) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://securitytracker.com/id?1014695
- http://www.kb.cert.org/vuls/id/435188
- http://www.us-cert.gov/cas/techalerts/TA05-229A.html

---

#### 634. CVE-2005-2502

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Buffer overflow in AppKit for Mac OS X 10.3.9 and 10.4.2, as used in applications such as TextEdit, allows external user-assisted attackers to execute arbitrary code via a crafted Microsoft Word file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://securitytracker.com/id?1014695
- http://www.kb.cert.org/vuls/id/172948
- http://www.us-cert.gov/cas/techalerts/TA05-229A.html

---

#### 635. CVE-2005-2503

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
AppKit for Mac OS X 10.3.9 and 10.4.2 allows attackers with physical access to create local accounts by forcing a particular error to occur at the login window.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://securitytracker.com/id?1014696
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html

---

#### 636. CVE-2005-2504

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
The System Profiler in Mac OS X 10.4.2 labels a Bluetooth device with "Requires Authentication: No" even when the user has selected the "Require pairing for security" option, which could confuse users about which setting is valid.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html

---

#### 637. CVE-2005-2505

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
Buffer overflow in CoreFoundation in Mac OS X 10.3.9 allows attackers to execute arbitrary code via command line arguments to an application that uses CoreFoundation.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html
- http://securitytracker.com/id?1014697
- http://lists.apple.com/archives/security-announce/2005//Aug/msg00001.html
- http://lists.apple.com/archives/security-announce/2005/Aug/msg00000.html

---

#### 638. [Apple] iOS 26.4.2 and iPadOS 26.4.2

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/127002

---

#### 639. [Apple] iOS 18.7.8 and iPadOS 18.7.8

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/127003

---

#### 640. [Apple] iOS 18.7.7 and iPadOS 18.7.7

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126793

---

#### 641. [Apple] iOS 26.4 and iPadOS 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126792

---

#### 642. [Apple] macOS Tahoe 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126794

---

#### 643. [Apple] macOS Sequoia 15.7.5

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126795

---

#### 644. [Apple] macOS Sonoma 14.8.5

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126796

---

#### 645. [Apple] tvOS 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126797

---

#### 646. [Apple] watchOS 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126798

---

#### 647. [Apple] visionOS 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126799

---

#### 648. [Apple] Safari 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126800

---

#### 649. [Apple] Xcode 26.4

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126801

---

#### 650. [Apple] iOS 16.7.15 and iPadOS 16.7.15

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126646

---

#### 651. [Apple] iOS 15.8.7 and iPadOS 15.8.7

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126632

---

#### 652. [Apple] iOS 26.3 and iPadOS 26.3

**严重程度 / Severity**: UPDATE
**受影响产品 / Affected Products**: macOS, iOS, iPadOS, watchOS, tvOS

**漏洞描述 / Description**:
Apple security update. Refer to support article for affected products and patch instructions.

**补丁信息 / Patch Info**:
Update to the latest Apple software version via System Settings > Software Update.

**参考链接 / References**:
- https://support.apple.com/en-us/126346

---

#### 653. CVE-2003-0512

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 and earlier generates a "% Login invalid" message instead of prompting for a password when an invalid username is provided, which allows remote attackers to identify valid usernames on the system and conduct brute force password guessing, as reported for the Aironet Bridge.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0056.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2003-q3/0056.html
- http://www.cisco.com/warp/public/707/cisco-sn-20030724-ios-enum.shtml
- http://www.kb.cert.org/vuls/id/886796
- http://www.vigilante.com/inetsecurity/advisories/VIGILANTE-2003002.htm
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5824

---

#### 654. CVE-2003-0647

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Buffer overflow in the HTTP server for Cisco IOS 12.2 and earlier allows remote attackers to execute arbitrary code via an extremely long (2GB) HTTP GET request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sn-20030730-ios-2gb-get.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sn-20030730-ios-2gb-get.shtml
- http://www.kb.cert.org/vuls/id/579324
- http://www.cisco.com/warp/public/707/cisco-sn-20030730-ios-2gb-get.shtml
- http://www.kb.cert.org/vuls/id/579324

---

#### 655. CVE-2003-1109

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ip_phone_7940, cisco:pix_firewall_software, cisco:ip_phone_7960, cisco:ios

**漏洞描述 / Description**:
The Session Initiation Protocol (SIP) implementation in multiple Cisco products including IP Phone models 7940 and 7960, IOS versions in the 12.2 train, and Secure PIX 5.2.9 to 6.2.2 allows remote attackers to cause a denial of service and possibly execute arbitrary code via crafted INVITE messages, as demonstrated by the OUSPG PROTOS c07-sip test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2003-06.html.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2003-06.html
- http://www.cisco.com/warp/public/707/cisco-sa-20030221-protos.shtml
- http://www.ee.oulu.fi/research/ouspg/protos/testing/c07/sip/
- http://www.kb.cert.org/vuls/id/528719
- http://www.securityfocus.com/bid/6904

---

#### 656. CVE-2003-1398

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.2, when IP routing is disabled, accepts false ICMP redirect messages, which allows remote attackers to cause a denial of service (network routing modification).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2003-02/0131.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2003-02/0131.html
- http://securitytracker.com/id?1006075
- http://www.securityfocus.com/bid/6823
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11306
- http://archives.neohapsis.com/archives/bugtraq/2003-02/0131.html

---

#### 657. CVE-2004-0054

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Multiple vulnerabilities in the H.323 protocol implementation for Cisco IOS 11.3T through 12.2T allow remote attackers to cause a denial of service and possibly execute arbitrary code, as demonstrated by the NISCC/OUSPG PROTOS test suite for the H.225 protocol.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2004-01.html.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2004-01.html
- http://www.cisco.com/warp/public/707/cisco-sa-20040113-h323.shtml
- http://www.kb.cert.org/vuls/id/749342
- http://www.securityfocus.com/bid/9406
- http://www.securitytracker.com/id?1008685

---

#### 658. CVE-2004-0710

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
IP Security VPN Services Module (VPNSM) in Cisco Catalyst 6500 Series Switch and the Cisco 7600 Series Internet Routers running IOS before 12.2(17b)SXA, before 12.2(17d)SXB, or before 12.2(14)SY03 could allow remote attackers to cause a denial of service (device crash and reload) via a malformed Internet Key Exchange (IKE) packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20040408-vpnsm.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20040408-vpnsm.shtml
- http://www.kb.cert.org/vuls/id/904310
- http://www.securityfocus.com/bid/10083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/15797
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5696

---

#### 659. CVE-2004-0589

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 11.1(x) through 11.3(x) and 12.0(x) through 12.2(x), when configured for BGP routing, allows remote attackers to cause a denial of service (device reload) via malformed BGP (1) OPEN or (2) UPDATE messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20040616-bgp.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20040616-bgp.shtml
- http://www.kb.cert.org/vuls/id/784540
- https://exchange.xforce.ibmcloud.com/vulnerabilities/16427
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A4948
- http://www.cisco.com/warp/public/707/cisco-sa-20040616-bgp.shtml

---

#### 660. CVE-2004-1454

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0S, 12.2, and 12.3, with Open Shortest Path First (OSPF) enabled, allows remote attackers to cause a denial of service (device reload) via a malformed OSPF packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12322.

**参考链接 / References**:
- http://secunia.com/advisories/12322
- http://www.ciac.org/ciac/bulletins/o-199.shtml
- http://www.cisco.com/warp/public/707/cisco-sa-20040818-ospf.shtml
- http://www.kb.cert.org/vuls/id/989406
- http://www.securityfocus.com/bid/10971

---

#### 661. CVE-2004-1464

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2(15) and earlier allows remote attackers to cause a denial of service (refused VTY (virtual terminal) connections), via a crafted TCP connection to the Telnet or reverse Telnet port.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/12395/.

**参考链接 / References**:
- http://secunia.com/advisories/12395/
- http://securitytracker.com/id?1011079
- http://www.cisco.com/warp/public/707/cisco-sa-20040827-telnet.shtml
- http://www.kb.cert.org/vuls/id/384230
- http://www.securityfocus.com/bid/11060

---

#### 662. CVE-2004-1775

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:catos, cisco:ios

**漏洞描述 / Description**:
Cisco VACM (View-based Access Control MIB) for Catalyst Operating Software (CatOS) 5.5 and 6.1 and IOS 12.0 and 12.1 allows remote attackers to read and modify device configuration via the read-write community string.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml
- http://www.kb.cert.org/vuls/id/645400
- http://www.securityfocus.com/bid/5030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6179
- http://www.cisco.com/warp/public/707/ios-snmp-community-vulns-pub.shtml

---

#### 663. CVE-2004-1111

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios, cisco:multiservice_platform_2651, cisco:7300_router, cisco:7500_router, cisco:catalyst_7600

**漏洞描述 / Description**:
Cisco IOS 2.2(18)EW, 12.2(18)EWA, 12.2(14)SZ, 12.2(18)S, 12.2(18)SE, 12.2(18)SV, 12.2(18)SW, and other versions without the "no service dhcp" command, keep undeliverable DHCP packets in the queue instead of dropping them, which allows remote attackers to cause a denial of service (dropped traffic) via multiple undeliverable DHCP packets that exceed the input queue size.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/p-034.shtml.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/p-034.shtml
- http://www.cisco.com/warp/public/707/cisco-sa-20041110-dhcp.shtml
- http://www.kb.cert.org/vuls/id/630104
- http://www.us-cert.gov/cas/techalerts/TA04-316A.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18021

---

#### 664. CVE-2005-0186

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1YD, 12.2T, 12.3 and 12.3T, when configured for the IOS Telephony Service (ITS), CallManager Express (CME) or Survivable Remote Site Telephony (SRST), allows remote attackers to cause a denial of service (device reboot) via a malformed packet to the SCCP port.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/13913.

**参考链接 / References**:
- http://secunia.com/advisories/13913
- http://securitytracker.com/id?1012945
- http://www.cisco.com/warp/public/707/cisco-sa-20050119-itscme.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/18956
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A4849

---

#### 665. CVE-2005-0195

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0S through 12.3YH allows remote attackers to cause a denial of service (device restart) via a crafted IPv6 packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20050126-ipv6.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20050126-ipv6.shtml
- http://www.kb.cert.org/vuls/id/472582
- http://www.us-cert.gov/cas/techalerts/TA05-026A.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19072
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5813

---

#### 666. CVE-2005-0196

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.3YL, with BGP enabled and running the bgp log-neighbor-changes command, allows remote attackers to cause a denial of service (device reload) via a malformed BGP packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14034.

**参考链接 / References**:
- http://secunia.com/advisories/14034
- http://securitytracker.com/id?1013013
- http://www.cisco.com/warp/public/707/cisco-sa-20050126-bgp.shtml
- http://www.kb.cert.org/vuls/id/689326
- http://www.us-cert.gov/cas/techalerts/TA05-026A.html

---

#### 667. CVE-2005-0197

**严重程度 / Severity**: N/A | CVSS: 6.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1T, 12.2, 12.2T, 12.3 and 12.3T, with Multi Protocol Label Switching (MPLS) installed but disabled, allows remote attackers to cause a denial of service (device reload) via a crafted packet sent to the disabled interface.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14031.

**参考链接 / References**:
- http://secunia.com/advisories/14031
- http://securitytracker.com/id?1013015
- http://www.cisco.com/warp/public/707/cisco-sa-20050126-les.shtml
- http://www.kb.cert.org/vuls/id/583638
- http://www.securityfocus.com/bid/12369

---

#### 668. CVE-2005-1020

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Secure Shell (SSH) 2 in Cisco IOS 12.0 through 12.3 allows remote attackers to cause a denial of service (device reload) (1) via a username that contains a domain name when using a TACACS+ server to authenticate, (2) when a new SSH session is in the login phase and a currently logged in user issues a send command, or (3) when IOS is logging messages and an SSH session is terminated while the server is sending data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14854.

**参考链接 / References**:
- http://secunia.com/advisories/14854
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-ssh.shtml
- http://www.securityfocus.com/bid/13043
- http://www.securitytracker.com/alerts/2005/Apr/1013655.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/19987

---

#### 669. CVE-2005-1021

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in Secure Shell (SSH) in Cisco IOS 12.0 through 12.3, when authenticating against a TACACS+ server, allows remote attackers to cause a denial of service (memory consumption) via an incorrect username or password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/14854.

**参考链接 / References**:
- http://secunia.com/advisories/14854
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-ssh.shtml
- http://www.osvdb.org/15303
- http://www.securityfocus.com/bid/13042
- http://www.securitytracker.com/alerts/2005/Apr/1013655.html

---

#### 670. CVE-2005-1057

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2T, 12.3 and 12.3T, when using Easy VPN Server XAUTH version 6 authentication, allows remote attackers to bypass authentication via a "malformed packet."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5852
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5852

---

#### 671. CVE-2005-1058

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2T, 12.3 and 12.3T, when processing an ISAKMP profile that specifies XAUTH authentication after Phase 1 negotiation, may not process certain attributes in the ISAKMP profile that specifies XAUTH, which allows remote attackers to bypass XAUTH and move to Phase 2 negotiations.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5738
- http://www.cisco.com/warp/public/707/cisco-sa-20050406-xauth.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5738

---

#### 672. CVE-2005-2105

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2T through 12.4 allows remote attackers to bypass Authentication, Authorization, and Accounting (AAA) RADIUS authentication, if the fallback method is set to none, via a long username.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20050629-aaa.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20050629-aaa.shtml
- http://www.securitytracker.com/alerts/2005/Jun/1014330.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/21190
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5756
- http://www.cisco.com/warp/public/707/cisco-sa-20050629-aaa.shtml

---

#### 673. CVE-2005-2451

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: cisco:ios_xr, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 and IOS XR before 3.2, with IPv6 enabled, allows remote attackers on a local network segment to cause a denial of service (device reload) and possibly execute arbitrary code via a crafted IPv6 packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/fulldisclosure/2005-07/0663.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2005-07/0663.html
- http://secunia.com/advisories/16272
- http://securitytracker.com/id?1014598
- http://www.cisco.com/warp/public/707/cisco-sa-20050729-ipv6.shtml
- http://www.kb.cert.org/vuls/id/930892

---

#### 674. CVE-2005-2841

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Buffer overflow in Firewall Authentication Proxy for FTP and/or Telnet Sessions for Cisco IOS 12.2ZH and 12.2ZL, 12.3 and 12.3T, and 12.4 and 12.4T allows remote attackers to cause a denial of service and possibly execute arbitrary code via crafted user authentication credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/707/cisco-sa-20050907-auth_proxy.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/707/cisco-sa-20050907-auth_proxy.shtml
- http://www.kb.cert.org/vuls/id/236045
- http://www.vupen.com/english/advisories/2005/1669
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5317
- http://www.cisco.com/warp/public/707/cisco-sa-20050907-auth_proxy.shtml

---

#### 675. CVE-2005-3427

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: cisco:ciscoworks_management_center_for_ips_sensors

**漏洞描述 / Description**:
The Cisco Management Center (MC) for IPS Sensors (IPS MC) 2.1 can omit port field values while generating the Cisco IOS IPS configuration file, wich can cause some signatures to be disabled and makes it easier for attackers to escape detection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17397.

**参考链接 / References**:
- http://secunia.com/advisories/17397
- http://securityreason.com/securityalert/137
- http://securitytracker.com/id?1015133
- http://www.cisco.com/warp/public/707/cisco-sa-20051101-ipsmc.shtml
- http://www.kb.cert.org/vuls/id/154883

---

#### 676. CVE-2005-3481

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 to 12.4 might allow remote attackers to execute arbitrary code via a heap-based buffer overflow in system timers. NOTE: this issue does not correspond to a specific vulnerability, rather a general weakness that only increases the feasibility of exploitation of any vulnerabilities that might exist.  Such design-level weaknesses normally are not included in CVE, so perhaps this issue should be REJECTed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17413.

**参考链接 / References**:
- http://secunia.com/advisories/17413
- http://securitytracker.com/id?1015139
- http://www.cisco.com/warp/public/707/cisco-sa-20051102-timers.shtml
- http://www.kb.cert.org/vuls/id/562945
- http://www.securityfocus.com/bid/15275

---

#### 677. CVE-2005-3921

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Cisco IOS Web Server for IOS 12.0(2a) allows remote attackers to inject arbitrary web script or HTML by (1) packets containing HTML that an administrator views via an HTTP interface to the contents of memory buffers, as demonstrated by the URI /level/15/exec/-/buffers/assigned/dump; or (2) sending the router Cisco Discovery Protocol (CDP) packets with HTML payload that an administrator views via the CDP status pages.  NOTE: these vectors were originally reported as being associated with the dump and packet options in /level/15/exec/-/show/buffers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/17780.

**参考链接 / References**:
- http://secunia.com/advisories/17780
- http://secunia.com/advisories/18528
- http://securityreason.com/securityalert/227
- http://securitytracker.com/id?1015275
- http://www.cisco.com/warp/public/707/cisco-sa-20051201-http.shtml

---

#### 678. CVE-2005-4436

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: extended_interior_gateway_routing_protocol:extended_interior_gateway_routing_protocol

**漏洞描述 / Description**:
Extended Interior Gateway Routing Protocol (EIGRP) 1.2, as implemented in Cisco IOS after 12.3(2), 12.3(3)B, and 12.3(2)T and other products, allows remote attackers to cause a denial of service by sending a "spoofed neighbor announcement" with (1) mismatched k values or (2) "goodbye message" Type-Length-Value (TLV).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040330.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040330.html
- http://marc.info/?l=full-disclosure&m=113504451523186&w=2
- http://securitytracker.com/id?1015382
- http://www.securityfocus.com/archive/1/419898/100/0/threaded
- http://www.securityfocus.com/bid/15978

---

#### 679. CVE-2005-4437

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: extended_interior_gateway_routing_protocol:extended_interior_gateway_routing_protocol

**漏洞描述 / Description**:
MD5 Neighbor Authentication in Extended Interior Gateway Routing Protocol (EIGRP) 1.2, as implemented in Cisco IOS 11.3 and later, does not include the Message Authentication Code (MAC) in the checksum, which allows remote attackers to sniff message hashes and (1) replay EIGRP HELLO messages or (2) cause a denial of service by sending a large number of spoofed EIGRP neighbor announcements, which results in an ARP storm on the local network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040332.html.

**参考链接 / References**:
- http://lists.grok.org.uk/pipermail/full-disclosure/2005-December/040332.html
- http://marc.info/?l=full-disclosure&m=113504451523186&w=2
- http://securityreason.com/securityalert/274
- http://securitytracker.com/id?1015382
- http://www.securityfocus.com/archive/1/419830/100/0/threaded

---

#### 680. CVE-2005-4826

**严重程度 / Severity**: N/A | CVSS: 6.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the VLAN Trunking Protocol (VTP) feature in Cisco IOS 12.1(22)EA3 on Catalyst 2950T switches allows remote attackers to cause a denial of service (device reboot) via a crafted Subset-Advert message packet, a different issue than CVE-2006-4774, CVE-2006-4775, and CVE-2006-4776.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/33013.

**参考链接 / References**:
- http://osvdb.org/33013
- http://secunia.com/advisories/23892
- http://securitytracker.com/id?1017568
- http://www.blackhat.com/html/bh-europe-05/bh-eu-05-speakers.html#Berrueta
- http://www.cisco.com/en/US/products/products_security_response09186a00807d1a81.html

---

#### 681. CVE-2006-0340

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Stack Group Bidding Protocol (SGBP) support in Cisco IOS 12.0 through 12.4 running on various Cisco products, when SGBP is enabled, allows remote attackers on the local network to cause a denial of service (device hang and network traffic loss) via a crafted UDP packet to port 9900.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/18490.

**参考链接 / References**:
- http://secunia.com/advisories/18490
- http://securityreason.com/securityalert/358
- http://securitytracker.com/id?1015501
- http://www.cisco.com/warp/public/707/cisco-sa-20060118-sgbp.shtml
- http://www.osvdb.org/22624

---

#### 682. CVE-2006-0354

**严重程度 / Severity**: N/A | CVSS: 5.5
**受影响产品 / Affected Products**: cisco:aironet_ap350, cisco:aironet_ap1240ag, cisco:aironet_ap1300, cisco:aironet_ap1400, cisco:aironet_ap1130ag

**漏洞描述 / Description**:
Cisco IOS before 12.3-7-JA2 on Aironet Wireless Access Points (WAP) allows remote authenticated users to cause a denial of service (termination of packet passing or termination of client connections) by sending the management interface a large number of spoofed ARP packets, which creates a large ARP table that exhausts memory, aka Bug ID CSCsc16644.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/18430.

**参考链接 / References**:
- http://secunia.com/advisories/18430
- http://securityreason.com/securityalert/339
- http://securitytracker.com/id?1015483
- http://www.cisco.com/warp/public/707/cisco-sa-20060112-wireless.shtml
- http://www.osvdb.org/22375

---

#### 683. CVE-2006-0485

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The TCL shell in Cisco IOS 12.2(14)S before 12.2(14)S16, 12.2(18)S before 12.2(18)S11, and certain other releases before 25 January 2006 does not perform Authentication, Authorization, and Accounting (AAA) command authorization checks, which may allow local users to execute IOS EXEC commands that were prohibited via the AAA configuration, aka Bug ID CSCeh73049.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/18613.

**参考链接 / References**:
- http://secunia.com/advisories/18613
- http://securitytracker.com/id?1015543
- http://www.cisco.com/warp/public/707/cisco-response-20060125-aaatcl.shtml
- http://www.osvdb.org/34892
- http://www.securityfocus.com/bid/16383

---

#### 684. CVE-2006-0486

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Certain Cisco IOS releases in 12.2S based trains with maintenance release number 25 and later, 12.3T based trains, and 12.4 based trains reuse a Tcl Shell process across login sessions of different local users on the same terminal if the first user does not use tclquit before exiting, which may cause subsequent local users to execute unintended commands or bypass AAA command authorization checks, aka Bug ID CSCef77770.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/18613.

**参考链接 / References**:
- http://secunia.com/advisories/18613
- http://securitytracker.com/id?1015543
- http://www.cisco.com/warp/public/707/cisco-response-20060125-aaatcl.shtml
- http://www.osvdb.org/22723
- https://exchange.xforce.ibmcloud.com/vulnerabilities/24308

---

#### 685. CVE-2006-1927

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR, when configured for Multi Protocol Label Switching (MPLS) and running on Cisco CRS-1 or Cisco 12000 series routers, allows remote attackers to cause a denial of service (Line card crash) via certain MPLS packets, as identified by Cisco bug ID CSCsc77475.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19740.

**参考链接 / References**:
- http://secunia.com/advisories/19740
- http://securitytracker.com/id?1015964
- http://www.cisco.com/warp/public/707/cisco-sa-20060419-xr.shtml
- http://www.securityfocus.com/bid/17607
- http://www.vupen.com/english/advisories/2006/1433

---

#### 686. CVE-2006-1928

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR, when configured for Multi Protocol Label Switching (MPLS) and running on Cisco CRS-1 routers, allows remote attackers to cause a denial of service (Modular Services Cards (MSC) crash or "MPLS packet handling problems") via certain MPLS packets, as identified by Cisco bug IDs (1) CSCsd15970 and (2) CSCsd55531.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/19740.

**参考链接 / References**:
- http://secunia.com/advisories/19740
- http://securitytracker.com/id?1015964
- http://www.cisco.com/warp/public/707/cisco-sa-20060419-xr.shtml
- http://www.osvdb.org/24811
- http://www.securityfocus.com/bid/17607

---

#### 687. CVE-2006-3291

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The web interface on Cisco IOS 12.3(8)JA and 12.3(8)JA1, as used on the Cisco Wireless Access Point and Wireless Bridge, reconfigures itself when it is changed to use the "Local User List Only (Individual Passwords)" setting, which removes all security and password configurations and allows remote attackers to access the system.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/20860.

**参考链接 / References**:
- http://secunia.com/advisories/20860
- http://securitytracker.com/id?1016399
- http://www.cisco.com/warp/public/707/cisco-sa-20060628-ap.shtml
- http://www.kb.cert.org/vuls/id/544484
- http://www.osvdb.org/26878

---

#### 688. CVE-2006-3595

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:router_web_setup

**漏洞描述 / Description**:
The default configuration of IOS HTTP server in Cisco Router Web Setup (CRWS) before 3.3.0 build 31 does not require credentials, which allows remote attackers to access the server with arbitrary privilege levels, aka bug CSCsa78190.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21028.

**参考链接 / References**:
- http://secunia.com/advisories/21028
- http://securitytracker.com/id?1016476
- http://www.cisco.com/warp/public/707/cisco-sa-20060712-crws.shtml
- http://www.kb.cert.org/vuls/id/205225
- http://www.osvdb.org/27159

---

#### 689. CVE-2006-3906

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:vpn_3080_concentrator, cisco:pix_firewall_501, cisco:pix_firewall_506, cisco:pix_firewall_515, cisco:pix_firewall_software

**漏洞描述 / Description**:
Internet Key Exchange (IKE) version 1 protocol, as implemented on Cisco IOS, VPN 3000 Concentrators, and PIX firewalls, allows remote attackers to cause a denial of service (resource exhaustion) via a flood of IKE Phase-1 packets that exceed the session expiration rate. NOTE: it has been argued that this is due to a design weakness of the IKE version 1 protocol, in which case other vendors and implementations would also be affected.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2006-07/0531.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2006-07/0531.html
- http://securityreason.com/securityalert/1293
- http://securitytracker.com/id?1016582
- http://www.cisco.com/en/US/tech/tk583/tk372/tsd_technology_security_response09186a00806f33d4.html
- http://www.nta-monitor.com/posts/2006/07/cisco-concentrator-dos.html

---

#### 690. CVE-2006-4032

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:callmanager_express

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS CallManager Express (CME) allows remote attackers to gain sensitive information (user names) from the Session Initiation Protocol (SIP) user directory via certain SIP messages, aka bug CSCse92417.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21335.

**参考链接 / References**:
- http://secunia.com/advisories/21335
- http://securitytracker.com/id?1016627
- http://www.blackhat.com/html/bh-usa-06/bh-usa-06-speakers.html#Endler
- http://www.cisco.com/warp/public/707/cisco-sr-20060802-sip.shtml
- http://www.osvdb.org/27760

---

#### 691. CVE-2006-4650

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0, 12.1, and 12.2, when GRE IP tunneling is used and the RFC2784 compliance fixes are missing, does not verify the offset field of a GRE packet during decapsulation, which leads to an integer overflow that references data from incorrect memory locations, which allows remote attackers to inject crafted packets into the routing queue, possibly bypassing intended router ACLs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21783.

**参考链接 / References**:
- http://secunia.com/advisories/21783
- http://securityreason.com/securityalert/1526
- http://securitytracker.com/id?1016799
- http://www.cisco.com/en/US/tech/tk827/tk369/tsd_technology_security_response09186a008072cd7b.html
- http://www.osvdb.org/28590

---

#### 692. CVE-2006-4774

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The VLAN Trunking Protocol (VTP) feature in Cisco IOS 12.1(19) allows remote attackers to cause a denial of service by sending a VTP version 1 summary frame with a VTP version field value of 2.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21896.

**参考链接 / References**:
- http://secunia.com/advisories/21896
- http://securitytracker.com/id?1016843
- http://www.cisco.com/warp/public/707/cisco-sr-20060913-vtp.shtml
- http://www.kb.cert.org/vuls/id/821420
- http://www.osvdb.org/28775

---

#### 693. CVE-2006-4775

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:catos, cisco:ios

**漏洞描述 / Description**:
The VLAN Trunking Protocol (VTP) feature in Cisco IOS 12.1(19) and CatOS allows remote attackers to cause a denial of service by sending a VTP update with a revision value of 0x7FFFFFFF, which is incremented to 0x80000000 and is interpreted as a negative number in a signed context.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21896.

**参考链接 / References**:
- http://secunia.com/advisories/21896
- http://secunia.com/advisories/21902
- http://securitytracker.com/id?1016843
- http://www.cisco.com/warp/public/707/cisco-sr-20060913-vtp.shtml
- http://www.kb.cert.org/vuls/id/175148

---

#### 694. CVE-2006-4776

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Heap-based buffer overflow in the VLAN Trunking Protocol (VTP) feature in Cisco IOS 12.1(19) allows remote attackers to execute arbitrary code via a long VLAN name in a VTP type 2 summary advertisement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21896.

**参考链接 / References**:
- http://secunia.com/advisories/21896
- http://securitytracker.com/id?1016843
- http://www.cisco.com/warp/public/707/cisco-sr-20060913-vtp.shtml
- http://www.kb.cert.org/vuls/id/542108
- http://www.osvdb.org/28777

---

#### 695. CVE-2006-4950

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 through 12.4 before 20060920, as used by Cisco IAD2430, IAD2431, and IAD2432 Integrated Access Devices, the VG224 Analog Phone Gateway, and the MWR 1900 and 1941 Mobile Wireless Edge Routers, is incorrectly identified as supporting DOCSIS, which allows remote attackers to gain read-write access via a hard-coded cable-docsis community string and read or modify arbitrary SNMP variables.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/21974.

**参考链接 / References**:
- http://secunia.com/advisories/21974
- http://securitytracker.com/id?1016899
- http://www.cisco.com/warp/public/707/cisco-sa-20060920-docsis.shtml
- http://www.kb.cert.org/vuls/id/123140
- http://www.osvdb.org/29034

---

#### 696. CVE-2007-0199

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Data-link Switching (DLSw) feature in Cisco IOS 11.0 through 12.4 allows remote attackers to cause a denial of service (device reload) via "an invalid value in a DLSw message... during the capabilities exchange."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/32683.

**参考链接 / References**:
- http://osvdb.org/32683
- http://secunia.com/advisories/23697
- http://securitytracker.com/id?1017498
- http://www.cisco.com/warp/public/707/cisco-sa-20070110-dlsw.shtml
- http://www.securityfocus.com/bid/21990

---

#### 697. CVE-2007-0479

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_transmission_control_protocol

**漏洞描述 / Description**:
Memory leak in the TCP listener in Cisco IOS 9.x, 10.x, 11.x, and 12.x allows remote attackers to cause a denial of service by sending crafted TCP traffic to an IPv4 address on the IOS device.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/32093.

**参考链接 / References**:
- http://osvdb.org/32093
- http://secunia.com/advisories/23867
- http://securitytracker.com/id?1017551
- http://www.cisco.com/en/US/products/products_security_advisory09186a00807cb0e4.shtml
- http://www.kb.cert.org/vuls/id/217912

---

#### 698. CVE-2007-0480

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios_transmission_control_protocol

**漏洞描述 / Description**:
Cisco IOS 9.x, 10.x, 11.x, and 12.x and IOS XR 2.0.x, 3.0.x, and 3.2.x allows remote attackers to cause a denial of service or execute arbitrary code via a crafted IP option in the IP header in a (1) ICMP, (2) PIMv2, (3) PGM, or (4) URD packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/32092.

**参考链接 / References**:
- http://osvdb.org/32092
- http://secunia.com/advisories/23867
- http://securitytracker.com/id?1017555
- http://www.cisco.com/en/US/products/products_security_advisory09186a00807cb157.shtml
- http://www.kb.cert.org/vuls/id/341288

---

#### 699. CVE-2007-0481

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_transmission_control_protocol

**漏洞描述 / Description**:
Cisco IOS allows remote attackers to cause a denial of service (crash) via a crafted IPv6 Type 0 Routing header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/32091.

**参考链接 / References**:
- http://osvdb.org/32091
- http://secunia.com/advisories/23867
- http://securitytracker.com/id?1017550
- http://www.cisco.com/en/US/products/products_security_advisory09186a00807cb0fd.shtml
- http://www.kb.cert.org/vuls/id/274760

---

#### 700. CVE-2007-0648

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS after 12.3(14)T, 12.3(8)YC1, 12.3(8)YG, and 12.4, with voice support and without Session Initiated Protocol (SIP) configured, allows remote attackers to cause a denial of service (crash) by sending a crafted packet to port 5060/UDP.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/23978.

**参考链接 / References**:
- http://secunia.com/advisories/23978
- http://securitytracker.com/id?1017575
- http://www.cisco.com/warp/public/707/cisco-air-20070131-sip.shtml
- http://www.cisco.com/warp/public/707/cisco-sa-20070131-sip.shtml
- http://www.kb.cert.org/vuls/id/438176

---

#### 701. CVE-2007-0917

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Intrusion Prevention System (IPS) feature for Cisco IOS 12.4XE to 12.3T allows remote attackers to bypass IPS signatures that use regular expressions via fragmented packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/33052.

**参考链接 / References**:
- http://osvdb.org/33052
- http://secunia.com/advisories/24142
- http://www.cisco.com/en/US/products/products_security_advisory09186a00807e0a5b.shtml
- http://www.cisco.com/en/US/products/products_security_response09186a00807e0a5e.html
- http://www.securityfocus.com/bid/22549

---

#### 702. CVE-2007-0918

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The ATOMIC.TCP signature engine in the Intrusion Prevention System (IPS) feature for Cisco IOS 12.4XA, 12.3YA, 12.3T, and other trains allows remote attackers to cause a denial of service (IPS crash and traffic loss) via unspecified manipulations that are not properly handled by the regular expression feature, as demonstrated using the 3123.0 (Netbus Pro Traffic) signature.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/33053.

**参考链接 / References**:
- http://osvdb.org/33053
- http://secunia.com/advisories/24142
- http://www.cisco.com/en/US/products/products_security_advisory09186a00807e0a5b.shtml
- http://www.cisco.com/en/US/products/products_security_response09186a00807e0a5e.html
- http://www.securityfocus.com/bid/22549

---

#### 703. CVE-2007-1258

**严重程度 / Severity**: N/A | CVSS: 6.1
**受影响产品 / Affected Products**: cisco:catalyst_7600, cisco:ios, cisco:catalyst_6500, cisco:catalyst_6000

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2SXA, SXB, SXD, and SXF; and the MSFC2, MSFC2a and MSFC3 running in Hybrid Mode on Cisco Catalyst 6000, 6500 and Cisco 7600 series systems; allows remote attackers on a local network segment to cause a denial of service (software reload) via a certain MPLS packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/33067.

**参考链接 / References**:
- http://osvdb.org/33067
- http://secunia.com/advisories/24348
- http://www.cisco.com/warp/public/707/cisco-sa-20070228-mpls.shtml
- http://www.securitytracker.com/id?1017709
- http://www.vupen.com/english/advisories/2007/0782

---

#### 704. CVE-2007-2586

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The FTP Server in Cisco IOS 11.3 through 12.4 does not properly check user authorization, which allows remote attackers to execute arbitrary code, and have other impact including reading startup-config, as demonstrated by a crafted MKD command that involves access to a VTY device and overflows a buffer, aka bug ID CSCek55259.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://seclists.org/bugtraq/2009/Jan/0183.html.

**参考链接 / References**:
- http://seclists.org/bugtraq/2009/Jan/0183.html
- http://secunia.com/advisories/25199
- http://www.cisco.com/en/US/products/products_security_advisory09186a00808399d0.shtml
- http://www.exploit-db.com/exploits/6155
- http://www.osvdb.org/35334

---

#### 705. CVE-2007-2587

**严重程度 / Severity**: N/A | CVSS: 6.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The IOS FTP Server in Cisco IOS 11.3 through 12.4 allows remote authenticated users to cause a denial of service (IOS reload) via unspecified vectors involving transferring files (aka bug ID CSCse29244).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/25199.

**参考链接 / References**:
- http://secunia.com/advisories/25199
- http://www.cisco.com/en/US/products/products_security_advisory09186a00808399d0.shtml
- http://www.osvdb.org/35335
- http://www.securityfocus.com/bid/23885
- http://www.securitytracker.com/id?1018030

---

#### 706. CVE-2007-2688

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios, cisco:ips_sensor_software

**漏洞描述 / Description**:
The Cisco Intrusion Prevention System (IPS) and IOS with Firewall/IPS Feature Set do not properly handle certain full-width and half-width Unicode character encodings, which might allow remote attackers to evade detection of HTTP traffic.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/25285.

**参考链接 / References**:
- http://secunia.com/advisories/25285
- http://www.cisco.com/en/US/products/products_security_response09186a008083f82e.html
- http://www.gamasec.net/english/gs07-01.html
- http://www.kb.cert.org/vuls/id/739224
- http://www.osvdb.org/35336

---

#### 707. CVE-2007-2813

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_transmission_control_protocol

**漏洞描述 / Description**:
Cisco IOS 12.4 and earlier, when using the crypto packages and SSL support is enabled, allows remote attackers to cause a denial of service via a malformed (1) ClientHello, (2) ChangeCipherSpec, or (3) Finished message during an SSL session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/25361.

**参考链接 / References**:
- http://secunia.com/advisories/25361
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080847c49.shtml
- http://www.osvdb.org/35339
- http://www.securityfocus.com/bid/24097
- http://www.securitytracker.com/id?1018094

---

#### 708. CVE-2007-4263

**严重程度 / Severity**: N/A | CVSS: 8.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the server side of the Secure Copy (SCP) implementation in Cisco 12.2-based IOS allows remote authenticated users to read, write or overwrite any file on the device's filesystem via unknown vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36694.

**参考链接 / References**:
- http://osvdb.org/36694
- http://secunia.com/advisories/26361
- http://www.cisco.com/warp/public/707/cisco-sa-20070808-scp.shtml
- http://www.securityfocus.com/bid/25240
- http://www.securitytracker.com/id?1018534

---

#### 709. CVE-2007-4285

**严重程度 / Severity**: N/A | CVSS: 9.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS and Cisco IOS XR 12.x up to 12.3, including some versions before 12.3(15) and 12.3(14)T, allows remote attackers to obtain sensitive information (partial packet contents) or cause a denial of service (router or component crash) via crafted IPv6 packets with a Type 0 routing header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/26359.

**参考链接 / References**:
- http://secunia.com/advisories/26359
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080899647.shtml
- http://www.securitytracker.com/id?1018542
- http://www.vupen.com/english/advisories/2007/2819
- https://exchange.xforce.ibmcloud.com/vulnerabilities/35906

---

#### 710. CVE-2007-4286

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Buffer overflow in the Next Hop Resolution Protocol (NHRP) functionality in Cisco IOS 12.0 through 12.4 allows remote attackers to cause a denial of service (restart) and execute arbitrary code via a crafted NHRP packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/26360.

**参考链接 / References**:
- http://secunia.com/advisories/26360
- http://www.cisco.com/en/US/products/products_security_advisory09186a008089963b.shtml
- http://www.kb.cert.org/vuls/id/201984
- http://www.securityfocus.com/archive/1/475931/100/0/threaded
- http://www.securityfocus.com/bid/25238

---

#### 711. CVE-2007-4291

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 allows remote attackers to cause a denial of service via (1) a malformed MGCP packet, which causes a device hang, aka CSCsf08998; a malformed H.323 packet, which causes a device crash, as identified by (2) CSCsi60004 with Proxy Unregistration and (3) CSCsg70474; and a malformed Real-time Transport Protocol (RTP) packet, which causes a device crash, as identified by (4) CSCse68138, related to VOIP RTP Lib, and (5) CSCse05642, related to I/O memory corruption.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36677.

**参考链接 / References**:
- http://osvdb.org/36677
- http://osvdb.org/36678
- http://osvdb.org/36679
- http://osvdb.org/36680
- http://osvdb.org/36681

---

#### 712. CVE-2007-4292

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Multiple memory leaks in Cisco IOS 12.0 through 12.4 allow remote attackers to cause a denial of service (device crash) via a malformed SIP packet, aka (1) CSCsf11855, (2) CSCeb21064, (3) CSCse40276, (4) CSCse68355, (5) CSCsf30058, (6) CSCsb24007, and (7) CSCsc60249.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36670.

**参考链接 / References**:
- http://osvdb.org/36670
- http://osvdb.org/36671
- http://osvdb.org/36672
- http://osvdb.org/36673
- http://osvdb.org/36674

---

#### 713. CVE-2007-4293

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 allows remote attackers to cause a denial of service (device crash) via (1) "abnormal" MGCP messages, aka CSCsd81407; and (2) a large facsimile packet, aka CSCej20505.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36668.

**参考链接 / References**:
- http://osvdb.org/36668
- http://osvdb.org/36669
- http://secunia.com/advisories/26363
- http://securitytracker.com/id?1018533
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080899653.shtml

---

#### 714. CVE-2007-4294

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco Unified Communications Manager (CUCM) 5.0, 5.1, and 6.0, and IOS 12.0 through 12.4, allows remote attackers to execute arbitrary code via a malformed SIP packet, aka CSCsi80102.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36693.

**参考链接 / References**:
- http://osvdb.org/36693
- http://secunia.com/advisories/26362
- http://securitytracker.com/id?1018538
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080899653.shtml
- http://www.securityfocus.com/bid/25239

---

#### 715. CVE-2007-4295

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4 allows remote attackers to execute arbitrary code via a malformed SIP packet, aka CSCsi80749.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/36667.

**参考链接 / References**:
- http://osvdb.org/36667
- http://secunia.com/advisories/26363
- http://securitytracker.com/id?1018533
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080899653.shtml
- http://www.securityfocus.com/bid/25239

---

#### 716. CVE-2007-4430

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios_xr, cisco:ios, cisco:cli, cisco:ids, cisco:cbos

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4 allows context-dependent attackers to cause a denial of service (device restart and BGP routing table rebuild) via certain regular expressions in a "show ip bgp regexp" command.  NOTE: unauthenticated remote attacks are possible in environments with anonymous telnet and Looking Glass access.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://forum.cisco.com/eforum/servlet/NetProf?page=netprof&forum=Network%20Infrastructure&topic=WAN%2C%20Routing%20and%20Switching&CommCmd=MB%3Fcmd%3Ddisplay_location%26location%3D.1ddf7bc9.

**参考链接 / References**:
- http://forum.cisco.com/eforum/servlet/NetProf?page=netprof&forum=Network%20Infrastructure&topic=WAN%2C%20Routing%20and%20Switching&CommCmd=MB%3Fcmd%3Ddisplay_location%26location%3D.1ddf7bc9
- http://secunia.com/advisories/26798
- http://www.cisco.com/en/US/products/products_security_response09186a00808bb91c.html
- http://www.heise-security.co.uk/news/94526/
- http://www.securityfocus.com/bid/25352

---

#### 717. CVE-2007-4632

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2E, 12.2F, and 12.2S places a "no login" line into the VTY configuration when an administrator makes certain changes to a (1) VTY/AUX or (2) CONSOLE setting on a device without AAA enabled, which allows remote attackers to bypass authentication and obtain a terminal session, a different vulnerability than CVE-1999-0293 and CVE-2005-2105.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_response09186a00808ae4ca.html.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_response09186a00808ae4ca.html
- http://www.securityfocus.com/bid/25482
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5866
- http://www.cisco.com/en/US/products/products_security_response09186a00808ae4ca.html
- http://www.securityfocus.com/bid/25482

---

#### 718. CVE-2007-5381

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Stack-based buffer overflow in the Line Printer Daemon (LPD) in Cisco IOS before 12.2(18)SXF11, 12.4(16a), and 12.4(2)T6 allow remote attackers to execute arbitrary code by setting a long hostname on the target system, then causing an error message to be printed, as demonstrated by a telnet session to the LPD from a source port other than 515.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/37935.

**参考链接 / References**:
- http://osvdb.org/37935
- http://secunia.com/advisories/27169
- http://www.cisco.com/en/US/products/products_security_response09186a00808d72e3.html
- http://www.irmplc.com/index.php/155-Advisory-024
- http://www.kb.cert.org/vuls/id/230505

---

#### 719. CVE-2007-5421

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: Multiple stack-based buffer overflows in Cisco IOS 12.x and IOS XR allow attackers to execute arbitrary code, as demonstrated via the "Bind Shell", "Reverse Shell", and "Two byte rootshell (Tiny Shell)" attacks.  NOTE: the vendor and researcher agree that this issue does not cross privilege boundaries, saying they do not "represent a vulnerability."  The disclosure was intended to demonstrate techniques for exploitation, which is not covered by CVE

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor vendor advisory.

---

#### 720. CVE-2007-5547

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Cisco IOS allows remote attackers to inject arbitrary web script or HTML, and execute IOS commands, via unspecified vectors, aka PSIRT-2022590358.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/43742.

**参考链接 / References**:
- http://osvdb.org/43742
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://osvdb.org/43742
- http://www.irmplc.com/index.php/111-Vendor-Alerts

---

#### 721. CVE-2007-5548

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Multiple stack-based buffer overflows in Command EXEC in Cisco IOS allow local users to gain privileges via unspecified vectors, aka (1) PSIRT-0474975756 and (2) PSIRT-0388256465.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information.  However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/45360.

**参考链接 / References**:
- http://osvdb.org/45360
- http://osvdb.org/45361
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://osvdb.org/45360
- http://osvdb.org/45361

---

#### 722. CVE-2007-5549

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Command EXEC in Cisco IOS allows local users to bypass command restrictions and obtain sensitive information via an unspecified "variation of an IOS command" involving "two different methods", aka CSCsk16129.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/45363.

**参考链接 / References**:
- http://osvdb.org/45363
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://osvdb.org/45363
- http://www.irmplc.com/index.php/111-Vendor-Alerts

---

#### 723. CVE-2007-5550

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS allows remote attackers to obtain the IOS version via unspecified vectors involving a "common network service", aka PSIRT-1255024833.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information.  However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.irmplc.com/index.php/111-Vendor-Alerts.

**参考链接 / References**:
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://www.irmplc.com/index.php/111-Vendor-Alerts

---

#### 724. CVE-2007-5551

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Off-by-one error in Cisco IOS allows remote attackers to execute arbitrary code via unspecified vectors that trigger a heap-based buffer overflow.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.irmplc.com/index.php/111-Vendor-Alerts.

**参考链接 / References**:
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://www.irmplc.com/index.php/111-Vendor-Alerts

---

#### 725. CVE-2007-5552

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Integer overflow in Cisco IOS allows remote attackers to execute arbitrary code via unspecified vectors.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.irmplc.com/index.php/111-Vendor-Alerts.

**参考链接 / References**:
- http://www.irmplc.com/index.php/111-Vendor-Alerts
- http://www.irmplc.com/index.php/111-Vendor-Alerts

---

#### 726. CVE-2007-5651

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:catos, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Extensible Authentication Protocol (EAP) implementation in Cisco IOS 12.3 and 12.4 on Cisco Access Points and 1310 Wireless Bridges (Wireless EAP devices), IOS 12.1 and 12.2 on Cisco switches (Wired EAP devices), and CatOS 6.x through 8.x on Cisco switches allows remote attackers to cause a denial of service (device reload) via a crafted EAP Response Identity packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/27329.

**参考链接 / References**:
- http://secunia.com/advisories/27329
- http://www.cisco.com/en/US/products/products_security_response09186a00808de8bb.html
- http://www.securityfocus.com/bid/26139
- http://www.securitytracker.com/id?1018842
- http://www.vupen.com/english/advisories/2007/3566

---

#### 727. CVE-2008-1153

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios, cisco:cisco_ios

**漏洞描述 / Description**:
Cisco IOS 12.1, 12.2, 12.3, and 12.4, with IPv4 UDP services and the IPv6 protocol enabled, allows remote attackers to cause a denial of service (device crash and possible blocked interface) via a crafted IPv6 packet to the device.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/29507.

**参考链接 / References**:
- http://secunia.com/advisories/29507
- http://www.cisco.com/warp/public/707/cisco-sa-20080326-IPv4IPv6.shtml
- http://www.kb.cert.org/vuls/id/936177
- http://www.securityfocus.com/bid/28461
- http://www.securitytracker.com/id?1019713

---

#### 728. CVE-2008-1156

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: cisco:ios, cisco:cisco_ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Multicast Virtual Private Network (MVPN) implementation in Cisco IOS 12.0, 12.2, 12.3, and 12.4 allows remote attackers to create "extra multicast states on the core routers" via a crafted Multicast Distribution Tree (MDT) Data Join message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/29507.

**参考链接 / References**:
- http://secunia.com/advisories/29507
- http://www.cisco.com/warp/public/707/cisco-sa-20080326-mvpn.shtml
- http://www.securityfocus.com/bid/28464
- http://www.securitytracker.com/id?1019715
- http://www.us-cert.gov/cas/techalerts/TA08-087B.html

---

#### 729. CVE-2008-1150

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The virtual private dial-up network (VPDN) component in Cisco IOS before 12.3 allows remote attackers to cause a denial of service (resource exhaustion) via a series of PPTP sessions, related to the persistence of interface descriptor block (IDB) data structures after process termination, aka bug ID CSCdv59309.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/29507.

**参考链接 / References**:
- http://secunia.com/advisories/29507
- http://securitytracker.com/id?1019714
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080969862.shtml
- http://www.securityfocus.com/bid/28460
- http://www.us-cert.gov/cas/techalerts/TA08-087B.html

---

#### 730. CVE-2008-1151

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the virtual private dial-up network (VPDN) component in Cisco IOS before 12.3 allows remote attackers to cause a denial of service (memory consumption) via a series of PPTP sessions, related to "dead memory" that remains allocated after process termination, aka bug ID CSCsj58566.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/29507.

**参考链接 / References**:
- http://secunia.com/advisories/29507
- http://securitytracker.com/id?1019714
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080969862.shtml
- http://www.securityfocus.com/bid/28460
- http://www.us-cert.gov/cas/techalerts/TA08-087B.html

---

#### 731. CVE-2008-1152

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios, cisco:cisco_ios

**漏洞描述 / Description**:
The data-link switching (DLSw) component in Cisco IOS 12.0 through 12.4 allows remote attackers to cause a denial of service (device restart or memory consumption) via crafted (1) UDP port 2067 or (2) IP protocol 91 packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/29507.

**参考链接 / References**:
- http://secunia.com/advisories/29507
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080969866.shtml
- http://www.securityfocus.com/bid/28465
- http://www.securitytracker.com/id?1019712
- http://www.us-cert.gov/cas/techalerts/TA08-087B.html

---

#### 732. CVE-2008-1159

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios_t, cisco:ios_xr, cisco:ios_s

**漏洞描述 / Description**:
Multiple unspecified vulnerabilities in the SSH server in Cisco IOS 12.4 allow remote attackers to cause a denial of service (device restart) via unknown vectors, aka Bug ID (1) CSCsk42419, (2) CSCsk60020, and (3) CSCsh51293.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/30322.

**参考链接 / References**:
- http://secunia.com/advisories/30322
- http://securitytracker.com/id?1020073
- http://www.cisco.com/en/US/products/products_security_advisory09186a008099567f.shtml
- http://www.securityfocus.com/bid/29314
- http://www.vupen.com/english/advisories/2008/1605/references

---

#### 733. CVE-2008-2515

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: ibm:aix

**漏洞描述 / Description**:
Unspecified vulnerability in iostat in IBM AIX 5.2, 5.3, and 6.1 allows local users to gain privileges via unknown vectors related to an "environment variable handling error."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://aix.software.ibm.com/aix/efixes/security/iostat_advisory.asc.

**参考链接 / References**:
- http://aix.software.ibm.com/aix/efixes/security/iostat_advisory.asc
- http://secunia.com/advisories/30349
- http://securitytracker.com/id?1020085
- http://www.ibm.com/support/docview.wss?uid=isg1IZ20635
- http://www.ibm.com/support/docview.wss?uid=isg1IZ21506

---

#### 734. CVE-2008-0960

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:nx_os, cisco:ace_10_6504_bundle_with_4_gbps_throughput, cisco:mds_9120, cisco:ace_20_6509_bundle_with_8gbps_throughput, cisco:ace_10_6509_bundle_with_8_gbps_throughput

**漏洞描述 / Description**:
SNMPv3 HMAC verification in (1) Net-SNMP 5.2.x before 5.2.4.1, 5.3.x before 5.3.2.1, and 5.4.x before 5.4.1.1; (2) UCD-SNMP; (3) eCos; (4) Juniper Session and Resource Control (SRC) C-series 1.0.0 through 2.0.0; (5) NetApp (aka Network Appliance) Data ONTAP 7.3RC1 and 7.3RC2; (6) SNMP Research before 16.2; (7) multiple Cisco IOS, CatOS, ACE, and Nexus products; (8) Ingate Firewall 3.1.0 and later and SIParator 3.1.0 and later; (9) HP OpenView SNMP Emanate Master Agent 15.x; and possibly other products relies on the client to specify the HMAC length, which makes it easier for remote attackers to bypass SNMP authentication via a length value of 1, which only checks the first byte.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2008//Jun/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2008//Jun/msg00002.html
- http://lists.ingate.com/pipermail/productinfo/2008/000021.html
- http://lists.opensuse.org/opensuse-security-announce/2008-08/msg00000.html
- http://marc.info/?l=bugtraq&m=127730470825399&w=2
- http://rhn.redhat.com/errata/RHSA-2008-0528.html

---

#### 735. CVE-2008-4128

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios, cisco:871_integrated_services_router

**漏洞描述 / Description**:
Multiple cross-site request forgery (CSRF) vulnerabilities in the HTTP Administration component in Cisco IOS 12.4 on the 871 Integrated Services Router allow remote attackers to execute arbitrary commands via (1) a certain "show privilege" command to the /level/15/exec/- URI, and (2) a certain "alias exec" command to the /level/15/exec/-/configure/http URI.  NOTE: some of these details are obtained from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jbrownsec.blogspot.com/2008/09/cisco-0day-released.html.

**参考链接 / References**:
- http://jbrownsec.blogspot.com/2008/09/cisco-0day-released.html
- http://www.securityfocus.com/bid/31218
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45226
- https://www.exploit-db.com/exploits/6476
- https://www.exploit-db.com/exploits/6477

---

#### 736. CVE-2008-2739

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The SERVICE.DNS signature engine in the Intrusion Prevention System (IPS) in Cisco IOS 12.3 and 12.4 allows remote attackers to cause a denial of service (device crash or hang) via network traffic that triggers unspecified IPS signatures, a different vulnerability than CVE-2008-1447.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01556.shtml
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A6058
- http://secunia.com/advisories/31990

---

#### 737. CVE-2008-3798

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.4 allows remote attackers to cause a denial of service (device crash) via a normal, properly formed SSL packet that occurs during termination of an SSL session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0146c.shtml
- http://www.securitytracker.com/id?1020930
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A6087

---

#### 738. CVE-2008-3799

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the Session Initiation Protocol (SIP) implementation in Cisco IOS 12.2 through 12.4, when VoIP is configured, allows remote attackers to cause a denial of service (memory consumption and voice-service outage) via unspecified valid SIP messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01562.shtml
- http://www.securitytracker.com/id?1020939
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5927

---

#### 739. CVE-2008-3800

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:unified_callmanager, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Session Initiation Protocol (SIP) implementation in Cisco IOS 12.2 through 12.4 and Unified Communications Manager 4.1 through 6.1, when VoIP is configured, allows remote attackers to cause a denial of service (device or process reload) via unspecified valid SIP messages, aka Cisco Bug ID CSCsu38644, a different vulnerability than CVE-2008-3801 and CVE-2008-3802.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://secunia.com/advisories/32013
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01562.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0156a.shtml
- http://www.securityfocus.com/bid/31367

---

#### 740. CVE-2008-3801

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:unified_callmanager, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Session Initiation Protocol (SIP) implementation in Cisco IOS 12.2 through 12.4 and Unified Communications Manager 4.1 through 6.1, when VoIP is configured, allows remote attackers to cause a denial of service (device or process reload) via unspecified valid SIP messages, aka Cisco Bug ID CSCsm46064, a different vulnerability than CVE-2008-3800 and CVE-2008-3802.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://secunia.com/advisories/32013
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01562.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0156a.shtml
- http://www.securityfocus.com/bid/31367

---

#### 741. CVE-2008-3802

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Session Initiation Protocol (SIP) implementation in Cisco IOS 12.2 through 12.4, when VoIP is configured, allows remote attackers to cause a denial of service (device reload) via unspecified valid SIP messages, aka Cisco bug ID CSCsk42759, a different vulnerability than CVE-2008-3800 and CVE-2008-3801.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01562.shtml
- http://www.securitytracker.com/id?1020939
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5889

---

#### 742. CVE-2008-3803

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
A "logic error" in Cisco IOS 12.0 through 12.4, when a Multiprotocol Label Switching (MPLS) VPN with extended communities is configured, sometimes causes a corrupted route target (RT) to be used, which allows remote attackers to read traffic from other VPNs in opportunistic circumstances.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a014a9.shtml
- http://www.securityfocus.com/bid/31366
- http://www.securitytracker.com/id?1020940
- http://www.vupen.com/english/advisories/2008/2670

---

#### 743. CVE-2008-3804

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Multi Protocol Label Switching (MPLS) Forwarding Infrastructure (MFI) in Cisco IOS 12.2 and 12.4 allows remote attackers to cause a denial of service (memory corruption) via crafted packets for which the software path is used.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a014ac.shtml
- http://www.securitytracker.com/id?1020934
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5619

---

#### 744. CVE-2008-3805

**严重程度 / Severity**: N/A | CVSS: 8.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 on Cisco 10000, uBR10012 and uBR7200 series devices handles external UDP packets that are sent to 127.0.0.0/8 addresses intended for IPC communication within the device, which allows remote attackers to cause a denial of service (device or linecard reload) via crafted UDP packets, a different vulnerability than CVE-2008-3806.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://tools.cisco.com/security/center/viewAlert.x?alertId=16646
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a014ae.shtml
- http://www.securitytracker.com/id?1020935
- http://www.vupen.com/english/advisories/2008/2670

---

#### 745. CVE-2008-3806

**严重程度 / Severity**: N/A | CVSS: 8.5
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 on Cisco 10000, uBR10012 and uBR7200 series devices handles external UDP packets that are sent to 127.0.0.0/8 addresses intended for IPC communication within the device, which allows remote attackers to cause a denial of service (device or linecard reload) via crafted UDP packets, a different vulnerability than CVE-2008-3805.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://tools.cisco.com/security/center/viewAlert.x?alertId=16646
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a014ae.shtml
- https://exchange.xforce.ibmcloud.com/vulnerabilities/45592
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A7123

---

#### 746. CVE-2008-3807

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 and 12.3 on Cisco uBR10012 series devices, when linecard redundancy is configured, enables a read/write SNMP service with "private" as the community, which allows remote attackers to obtain administrative access by guessing this community and sending SNMP requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a014b1.shtml
- http://www.securitytracker.com/id?1020941
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5452

---

#### 747. CVE-2008-3808

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4 allows remote attackers to cause a denial of service (device reload) via a crafted Protocol Independent Multicast (PIM) packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01491.shtml
- http://www.securityfocus.com/bid/31356
- http://www.securitytracker.com/id?1020936
- http://www.vupen.com/english/advisories/2008/2670

---

#### 748. CVE-2008-3809

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4 on Gigabit Switch Router (GSR) devices (aka 12000 Series routers) allows remote attackers to cause a denial of service (device crash) via a malformed Protocol Independent Multicast (PIM) packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://tools.cisco.com/security/center/viewAlert.x?alertId=16638
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01491.shtml
- http://www.securityfocus.com/bid/31356
- http://www.securitytracker.com/id?1020936

---

#### 749. CVE-2008-3810

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 and 12.4, when NAT Skinny Call Control Protocol (SCCP) Fragmentation Support is enabled, allows remote attackers to cause a denial of service (device reload) via segmented SCCP messages, aka CSCsg22426, a different vulnerability than CVE-2008-3811.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0148e.shtml
- http://www.securityfocus.com/bid/31359
- http://www.securitytracker.com/id?1020937
- http://www.vupen.com/english/advisories/2008/2670

---

#### 750. CVE-2008-3811

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 and 12.4, when NAT Skinny Call Control Protocol (SCCP) Fragmentation Support is enabled, allows remote attackers to cause a denial of service (device reload) via segmented SCCP messages, aka Cisco Bug ID CSCsi17020, a different vulnerability than CVE-2008-3810.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0148e.shtml
- http://www.securityfocus.com/bid/31359
- http://www.securitytracker.com/id?1020937
- http://www.vupen.com/english/advisories/2008/2670

---

#### 751. CVE-2008-3812

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.4, when IOS firewall Application Inspection Control (AIC) with HTTP Deep Packet Inspection is enabled, allows remote attackers to cause a denial of service (device reload) via a malformed HTTP transit packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://tools.cisco.com/security/center/viewAlert.x?alertId=16661
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a01545.shtml
- http://www.securityfocus.com/bid/31354
- http://www.securitytracker.com/id?1020929

---

#### 752. CVE-2008-3813

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2 and 12.4, when the L2TP mgmt daemon process is enabled, allows remote attackers to cause a denial of service (device reload) via a crafted L2TP packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/31990.

**参考链接 / References**:
- http://secunia.com/advisories/31990
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a0157a.shtml
- http://www.securitytracker.com/id?1020938
- http://www.vupen.com/english/advisories/2008/2670
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5362

---

#### 753. CVE-2008-4963

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:catos, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the VLAN Trunking Protocol (VTP) implementation on Cisco IOS and CatOS, when the VTP operating mode is not transparent, allows remote attackers to cause a denial of service (device reload or hang) via a crafted VTP packet sent to a switch interface configured as a trunk port.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/49601.

**参考链接 / References**:
- http://osvdb.org/49601
- http://secunia.com/advisories/32573
- http://securitytracker.com/id?1021143
- http://www.cisco.com/en/US/products/products_security_response09186a0080a231cf.html
- http://www.securityfocus.com/bid/32120

---

#### 754. CVE-2008-3821

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the HTTP server in Cisco IOS 11.0 through 12.4 allow remote attackers to inject arbitrary web script or HTML via (1) the query string to the ping program or (2) unspecified other aspects of the URI.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jvn.jp/en/jp/JVN28344798/index.html.

**参考链接 / References**:
- http://jvn.jp/en/jp/JVN28344798/index.html
- http://osvdb.org/51393
- http://osvdb.org/51394
- http://secunia.com/advisories/33461
- http://securityreason.com/securityalert/4916

---

#### 755. CVE-2009-0470

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the HTTP server in Cisco IOS 12.4(23) allow remote attackers to inject arbitrary web script or HTML via the PATH_INFO to the default URI under (1) level/15/exec/-/ or (2) exec/, a different vulnerability than CVE-2008-3821.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/33844.

**参考链接 / References**:
- http://secunia.com/advisories/33844
- http://www.securityfocus.com/archive/1/500674/100/0/threaded
- http://www.securityfocus.com/bid/33625
- http://secunia.com/advisories/33844
- http://www.securityfocus.com/archive/1/500674/100/0/threaded

---

#### 756. CVE-2009-0471

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cross-site request forgery (CSRF) vulnerability in the HTTP server in Cisco IOS 12.4(23) allows remote attackers to execute arbitrary commands, as demonstrated by executing the hostname command with a level/15/configure/-/hostname request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/33844.

**参考链接 / References**:
- http://secunia.com/advisories/33844
- http://www.securityfocus.com/archive/1/500674/100/0/threaded
- http://secunia.com/advisories/33844
- http://www.securityfocus.com/archive/1/500674/100/0/threaded

---

#### 757. CVE-2009-0631

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4, when configured with (1) IP Service Level Agreements (SLAs) Responder, (2) Session Initiation Protocol (SIP), (3) H.323 Annex E Call Signaling Transport, or (4) Media Gateway Control Protocol (MGCP) allows remote attackers to cause a denial of service (blocked input queue on the inbound interface) via a crafted UDP packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90426.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90426.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34245
- http://www.securitytracker.com/id?1021904
- https://exchange.xforce.ibmcloud.com/vulnerabilities/49419

---

#### 758. CVE-2009-0626

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The SSLVPN feature in Cisco IOS 12.3 through 12.4 allows remote attackers to cause a denial of service (device reload or hang) via a crafted HTTPS packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021896
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90424.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34239

---

#### 759. CVE-2009-0628

**严重程度 / Severity**: N/A | CVSS: 9.0
**受影响产品 / Affected Products**: cisco:cisco_ios

**漏洞描述 / Description**:
Memory leak in the SSLVPN feature in Cisco IOS 12.3 through 12.4 allows remote attackers to cause a denial of service (memory consumption and device crash) by disconnecting an SSL session in an abnormal manner, leading to a Transmission Control Block (TCB) leak.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021896
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90424.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34239

---

#### 760. CVE-2009-0629

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: cisco:ios_xr, cisco:ios

**漏洞描述 / Description**:
The (1) Airline Product Set (aka ALPS), (2) Serial Tunnel Code (aka STUN), (3) Block Serial Tunnel Code (aka BSTUN), (4) Native Client Interface Architecture (NCIA) support, (5) Data-link switching (aka DLSw), (6) Remote Source-Route Bridging (RSRB), (7) Point to Point Tunneling Protocol (PPTP), (8) X.25 for Record Boundary Preservation (RBP), (9) X.25 over TCP (XOT), and (10) X.25 Routing features in Cisco IOS 12.2 and 12.4 allows remote attackers to cause a denial of service (device reload) via a series of crafted TCP packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021903
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a904cb.shtml
- http://www.securityfocus.com/bid/34238

---

#### 761. CVE-2009-0630

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The (1) Cisco Unified Communications Manager Express; (2) SIP Gateway Signaling Support Over Transport Layer Security (TLS) Transport; (3) Secure Signaling and Media Encryption; (4) Blocks Extensible Exchange Protocol (BEEP); (5) Network Admission Control HTTP Authentication Proxy; (6) Per-user URL Redirect for EAPoUDP, Dot1x, and MAC Authentication Bypass; (7) Distributed Director with HTTP Redirects; and (8) TCP DNS features in Cisco IOS 12.0 through 12.4 do not properly handle IP sockets, which allows remote attackers to cause a denial of service (outage or resource consumption) via a series of crafted TCP packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021897
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a904c6.shtml
- http://www.securityfocus.com/bid/34242

---

#### 762. CVE-2009-0633

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:cisco_ios

**漏洞描述 / Description**:
Multiple unspecified vulnerabilities in the (1) Mobile IP NAT Traversal feature and (2) Mobile IPv6 subsystem in Cisco IOS 12.3 through 12.4 allow remote attackers to cause a denial of service (input queue wedge and interface outage) via MIPv6 packets, aka Bug ID CSCsm97220.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021898
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a9042f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34241

---

#### 763. CVE-2009-0634

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:cisco_ios

**漏洞描述 / Description**:
Multiple unspecified vulnerabilities in the home agent (HA) implementation in the (1) Mobile IP NAT Traversal feature and (2) Mobile IPv6 subsystem in Cisco IOS 12.3 through 12.4 allow remote attackers to cause a denial of service (input queue wedge and interface outage) via an ICMP packet, aka Bug ID CSCso05337.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021898
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a9042f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34241

---

#### 764. CVE-2009-0635

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the Cisco Tunneling Control Protocol (cTCP) encapsulation feature in Cisco IOS 12.4, when an Easy VPN (aka EZVPN) server is enabled, allows remote attackers to cause a denial of service (memory consumption and device crash) via a sequence of TCP packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90459.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.securityfocus.com/bid/34246
- http://www.securitytracker.com/id?1021895

---

#### 765. CVE-2009-0636

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4, when SIP voice services are enabled, allows remote attackers to cause a denial of service (device crash) via a valid SIP message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021902
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a904c0.shtml
- http://www.securityfocus.com/bid/34243

---

#### 766. CVE-2009-0637

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios_xr, cisco:ios

**漏洞描述 / Description**:
The SCP server in Cisco IOS 12.2 through 12.4, when Role-Based CLI Access is enabled, does not enforce the CLI view configuration for file transfers, which allows remote authenticated users with an attached CLI view to (1) read or (2) overwrite arbitrary files via an SCP command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/34438.

**参考链接 / References**:
- http://secunia.com/advisories/34438
- http://securitytracker.com/id?1021899
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a90469.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080a904c8.shtml
- http://www.securityfocus.com/bid/34247

---

#### 767. CVE-2009-1168

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0(32)S12 through 12.0(32)S13 and 12.0(33)S3 through 12.0(33)S4, 12.0(32)SY8 through 12.0(32)SY9, 12.2(33)SXI1, 12.2XNC before 12.2(33)XNC2, 12.2XND before 12.2(33)XND1, and 12.4(24)T1; and IOS XE 2.3 through 2.3.1t and 2.4 through 2.4.0; when RFC4893 BGP routing is enabled, allows remote attackers to cause a denial of service (memory corruption and device reload) by using an RFC4271 peer to send an update with a long series of AS numbers, aka Bug ID CSCsy86021.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/36046.

**参考链接 / References**:
- http://secunia.com/advisories/36046
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080aea4c9.shtml
- http://www.securityfocus.com/bid/35862
- http://www.securitytracker.com/id?1022619
- http://www.vupen.com/english/advisories/2009/2082

---

#### 768. CVE-2009-2049

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0(32)S12 through 12.0(32)S13 and 12.0(33)S3 through 12.0(33)S4, 12.0(32)SY8 through 12.0(32)SY9, 12.2(33)SXI1 through 12.2(33)SXI2, 12.2XNC before 12.2(33)XNC2, 12.2XND before 12.2(33)XND1, and 12.4(24)T1; and IOS XE 2.3 through 2.3.1t and 2.4 through 2.4.0; when RFC4893 BGP routing is enabled, allows remote attackers to cause a denial of service (device reload) by using an RFC4271 peer to send a malformed update, aka Bug ID CSCta33973.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/36046.

**参考链接 / References**:
- http://secunia.com/advisories/36046
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080aea4c9.shtml
- http://www.securityfocus.com/bid/35860
- http://www.securitytracker.com/id?1022619
- http://www.vupen.com/english/advisories/2009/2082

---

#### 769. CVE-2009-2055

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.4.0 through 3.8.1 allows remote attackers to cause a denial of service (session reset) via a BGP UPDATE message with an invalid attribute, as demonstrated in the wild on 17 August 2009.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://mailman.nanog.org/pipermail/nanog/2009-August/012719.html.

**参考链接 / References**:
- http://mailman.nanog.org/pipermail/nanog/2009-August/012719.html
- http://securitytracker.com/id?1022739
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af150f.shtml
- http://mailman.nanog.org/pipermail/nanog/2009-August/012719.html
- http://securitytracker.com/id?1022739

---

#### 770. CVE-2009-1154

**严重程度 / Severity**: N/A | CVSS: 3.3
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.8.1 and earlier allows remote attackers to cause a denial of service (process crash) via a long BGP UPDATE message, as demonstrated by a message with many AS numbers in the AS Path Attribute.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1022756.

**参考链接 / References**:
- http://securitytracker.com/id?1022756
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af150f.shtml
- http://securitytracker.com/id?1022756
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af150f.shtml

---

#### 771. CVE-2009-2056

**严重程度 / Severity**: N/A | CVSS: 3.3
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.8.1 and earlier allows remote authenticated users to cause a denial of service (process crash) via vectors involving a BGP UPDATE message with many AS numbers prepended to the AS path.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://securitytracker.com/id?1022756.

**参考链接 / References**:
- http://securitytracker.com/id?1022756
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af150f.shtml
- http://securitytracker.com/id?1022756
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af150f.shtml

---

#### 772. CVE-2009-2051

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 through 12.4 and 15.0 through 15.1, Cisco IOS XE 2.5.x and 2.6.x before 2.6.1, and Cisco Unified Communications Manager (aka CUCM, formerly CallManager) 4.x, 5.x before 5.1(3g), 6.x before 6.1(4), and 7.x before 7.1(2) allow remote attackers to cause a denial of service (device reload or voice-services outage) via a malformed SIP INVITE message that triggers an improper call to the sipSafeStrlen function, aka Bug IDs CSCsz40392 and CSCsz43987.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/57453.

**参考链接 / References**:
- http://osvdb.org/57453
- http://secunia.com/advisories/36498
- http://secunia.com/advisories/36499
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af2d11.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml

---

#### 773. CVE-2009-2862

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Object Groups for Access Control Lists (ACLs) feature in Cisco IOS 12.2XNB, 12.2XNC, 12.2XND, 12.4MD, 12.4T, 12.4XZ, and 12.4YA allows remote attackers to bypass intended access restrictions via crafted requests, aka Bug IDs CSCsx07114, CSCsu70214, CSCsw47076, CSCsv48603, CSCsy54122, and CSCsu50252.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58338.

**参考链接 / References**:
- http://osvdb.org/58338
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18876
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8119.shtml
- http://www.securityfocus.com/bid/36495
- http://www.securitytracker.com/id?1022933

---

#### 774. CVE-2009-2863

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Race condition in the Firewall Authentication Proxy feature in Cisco IOS 12.0 through 12.4 allows remote attackers to bypass authentication, or bypass the consent web page, via a crafted request, aka Bug ID CSCsy15227.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58340.

**参考链接 / References**:
- http://osvdb.org/58340
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18882
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8132.shtml
- http://www.securityfocus.com/bid/36491
- http://www.securitytracker.com/id?1022935

---

#### 775. CVE-2009-2865

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: cisco:unified_communications_manager_express, cisco:ios

**漏洞描述 / Description**:
Buffer overflow in the login implementation in the Extension Mobility feature in the Unified Communications Manager Express (CME) component in Cisco IOS 12.4XW, 12.4XY, 12.4XZ, and 12.4YA allows remote attackers to execute arbitrary code or cause a denial of service via crafted HTTP requests, aka Bug ID CSCsq58779.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58335.

**参考链接 / References**:
- http://osvdb.org/58335
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18884
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8116.shtml
- http://www.securityfocus.com/bid/36498
- http://www.securitytracker.com/id?1022932

---

#### 776. CVE-2009-2866

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2 through 12.4 allows remote attackers to cause a denial of service (device reload) via a crafted H.323 packet, aka Bug ID CSCsz38104.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58337.

**参考链接 / References**:
- http://osvdb.org/58337
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18885
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af811a.shtml
- http://www.securityfocus.com/bid/36494
- http://www.securitytracker.com/id?1022930

---

#### 777. CVE-2009-2867

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2XNA, 12.2XNB, 12.2XNC, 12.2XND, 12.4T, 12.4XZ, and 12.4YA, when Zone-Based Policy Firewall SIP Inspection is enabled, allows remote attackers to cause a denial of service (device reload) via a crafted SIP transit packet, aka Bug ID CSCsr18691.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=18886.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18886
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8130.shtml
- http://www.securitytracker.com/id?1022930
- http://www.vupen.com/english/advisories/2009/2759
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A7254

---

#### 778. CVE-2009-2868

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2 through 12.4, when certificate-based authentication is enabled for IKE, allows remote attackers to cause a denial of service (Phase 1 SA exhaustion) via crafted requests, aka Bug IDs CSCsy07555 and CSCee72997.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=18887.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18887
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8117.shtml
- http://www.vupen.com/english/advisories/2009/2759
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18887
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8117.shtml

---

#### 779. CVE-2009-2869

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2XNA, 12.2XNB, 12.2XNC, 12.2XND, 12.4MD, 12.4T, 12.4XZ, and 12.4YA allows remote attackers to cause a denial of service (device reload) via a crafted NTPv4 packet, aka Bug IDs CSCsu24505 and CSCsv75948.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58342.

**参考链接 / References**:
- http://osvdb.org/58342
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18889
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8131.shtml
- http://www.securitytracker.com/id?1022930
- http://www.vupen.com/english/advisories/2009/2759

---

#### 780. CVE-2009-2870

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2 through 12.4, when the Cisco Unified Border Element feature is enabled, allows remote attackers to cause a denial of service (device reload) via crafted SIP messages, aka Bug ID CSCsx25880.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=18891.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18891
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af811b.shtml
- http://www.securitytracker.com/id?1022930
- http://www.vupen.com/english/advisories/2009/2759
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18891

---

#### 781. CVE-2009-2871

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2 and 12.4, when SSLVPN sessions, SSH sessions, or IKE encrypted nonces are enabled, allows remote attackers to cause a denial of service (device reload) via a crafted encrypted packet, aka Bug ID CSCsq24002.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=18892.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18892
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af811c.shtml
- http://www.securitytracker.com/id?1022930
- http://www.vupen.com/english/advisories/2009/2759
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18892

---

#### 782. CVE-2009-2872

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4, when IP-based tunnels and the Cisco Express Forwarding feature are enabled, allows remote attackers to cause a denial of service (device reload) via a malformed packet that is not properly handled during switching from one tunnel to a second tunnel, aka Bug IDs CSCsh97579 and CSCsq31776.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58333.

**参考链接 / References**:
- http://osvdb.org/58333
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18893
- http://www.cisco.com/en/US/products/products_applied_mitigation_bulletin09186a0080af8113.html
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8115.shtml
- http://www.cisco.com/web/about/security/intelligence/Cisco_ERP_sep09.html

---

#### 783. CVE-2009-2873

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.0 through 12.4, when IP-based tunnels and the Cisco Express Forwarding feature are enabled, allows remote attackers to cause a denial of service (device reload) via malformed packets, aka Bug ID CSCsx70889.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/58334.

**参考链接 / References**:
- http://osvdb.org/58334
- http://tools.cisco.com/security/center/viewAlert.x?alertId=18895
- http://www.cisco.com/en/US/products/products_applied_mitigation_bulletin09186a0080af8113.html
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080af8115.shtml
- http://www.cisco.com/web/about/security/intelligence/Cisco_ERP_sep09.html

---

#### 784. CVE-2010-0137

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Unspecified vulnerability in the sshd_child_handler process in the SSH server in Cisco IOS XR 3.4.1 through 3.7.0 allows remote attackers to cause a denial of service (process crash and memory consumption) via a crafted SSH2 packet, aka Bug ID CSCsu10574.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/38227.

**参考链接 / References**:
- http://secunia.com/advisories/38227
- http://securitytracker.com/id?1023480
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b13512.shtml
- http://www.securityfocus.com/bid/37878
- http://www.vupen.com/english/advisories/2010/0183

---

#### 785. CVE-2010-0576

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios_xr, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.0 through 12.4, IOS XE 2.1.x through 2.3.x before 2.3.2, and IOS XR 3.2.x through 3.4.3, when Multiprotocol Label Switching (MPLS) and Label Distribution Protocol (LDP) are enabled, allows remote attackers to cause a denial of service (device reload or process restart) via a crafted LDP packet, aka Bug IDs CSCsz45567 and CSCsj25893.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63188.

**参考链接 / References**:
- http://osvdb.org/63188
- http://secunia.com/advisories/39065
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20ee2.shtml
- http://www.securityfocus.com/bid/38938
- http://www.securitytracker.com/id?1023740

---

#### 786. CVE-2010-0577

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 through 12.4, when certain PMTUD, SNAT, or window-size configurations are used, allows remote attackers to cause a denial of service (infinite loop, and device reload or hang) via a TCP segment with crafted options, aka Bug ID CSCsz75186.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63178.

**参考链接 / References**:
- http://osvdb.org/63178
- http://secunia.com/advisories/39078
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f34.shtml
- http://www.securityfocus.com/bid/38930
- http://www.securitytracker.com/id?1023743

---

#### 787. CVE-2010-0578

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:router_7200, cisco:7200_router, cisco:7301_router, cisco:ios

**漏洞描述 / Description**:
The IKE implementation in Cisco IOS 12.2 through 12.4 on Cisco 7200 and 7301 routers with VAM2+ allows remote attackers to cause a denial of service (device reload) via a malformed IKE packet, aka Bug ID CSCtb13491.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63182.

**参考链接 / References**:
- http://osvdb.org/63182
- http://secunia.com/advisories/39057
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20ee5.shtml
- http://www.securityfocus.com/bid/38932
- http://www.securitytracker.com/id?1023741

---

#### 788. CVE-2010-0579

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The SIP implementation in Cisco IOS 12.3 and 12.4 allows remote attackers to cause a denial of service (device reload) via a malformed SIP message, aka Bug ID CSCtb93416, the "SIP Message Handling Denial of Service Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39068.

**参考链接 / References**:
- http://secunia.com/advisories/39068
- http://securitytracker.com/id?1023744
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20063
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f32.shtml
- http://secunia.com/advisories/39068

---

#### 789. CVE-2010-0580

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the SIP implementation in Cisco IOS 12.3 and 12.4 allows remote attackers to execute arbitrary code via a malformed SIP message, aka Bug ID CSCsz48680, the "SIP Message Processing Arbitrary Code Execution Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39068.

**参考链接 / References**:
- http://secunia.com/advisories/39068
- http://securitytracker.com/id?1023744
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20064
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f32.shtml
- http://secunia.com/advisories/39068

---

#### 790. CVE-2010-0581

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the SIP implementation in Cisco IOS 12.3 and 12.4 allows remote attackers to execute arbitrary code via a malformed SIP message, aka Bug ID CSCsz89904, the "SIP Packet Parsing Arbitrary Code Execution Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39068.

**参考链接 / References**:
- http://secunia.com/advisories/39068
- http://securitytracker.com/id?1023744
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20065
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f32.shtml
- http://secunia.com/advisories/39068

---

#### 791. CVE-2010-0582

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1 through 12.4, and 15.0M before 15.0(1)M1, allows remote attackers to cause a denial of service (interface queue wedge) via malformed H.323 packets, aka Bug ID CSCta19962.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39067.

**参考链接 / References**:
- http://secunia.com/advisories/39067
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20ee4.shtml
- http://www.securitytracker.com/id?1023742
- http://www.vupen.com/english/advisories/2010/0706
- http://secunia.com/advisories/39067

---

#### 792. CVE-2010-0583

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the H.323 implementation in Cisco IOS 12.1 through 12.4, and 15.0M before 15.0(1)M1, allows remote attackers to cause a denial of service (memory consumption and device reload) via malformed H.323 packets, aka Bug ID CSCtb93855.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63181.

**参考链接 / References**:
- http://osvdb.org/63181
- http://secunia.com/advisories/39067
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20ee4.shtml
- http://www.securityfocus.com/bid/38934
- http://www.securitytracker.com/id?1023742

---

#### 793. CVE-2010-0584

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.4, when NAT SCCP fragmentation support is enabled, allows remote attackers to cause a denial of service (device reload) via crafted Skinny Client Control Protocol (SCCP) packets, aka Bug ID CSCsy09250.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63187.

**参考链接 / References**:
- http://osvdb.org/63187
- http://secunia.com/advisories/39062
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20ee6.shtml
- http://www.securitytracker.com/id?1023739
- http://www.vupen.com/english/advisories/2010/0708

---

#### 794. CVE-2010-0585

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1 through 12.4, when Cisco Unified Communications Manager Express (CME) or Cisco Unified Survivable Remote Site Telephony (SRST) is enabled, allows remote attackers to cause a denial of service (device reload) via a malformed Skinny Client Control Protocol (SCCP) message, aka Bug ID CSCsz48614, the "SCCP Packet Processing Denial of Service Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/39069.

**参考链接 / References**:
- http://secunia.com/advisories/39069
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20069
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f33.shtml
- http://secunia.com/advisories/39069
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20069

---

#### 795. CVE-2010-0586

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.1 through 12.4, when Cisco Unified Communications Manager Express (CME) or Cisco Unified Survivable Remote Site Telephony (SRST) is enabled, allows remote attackers to cause a denial of service (device reload) via a malformed Skinny Client Control Protocol (SCCP) message, aka Bug ID CSCsz49741, the "SCCP Request Handling Denial of Service Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/63177.

**参考链接 / References**:
- http://osvdb.org/63177
- http://secunia.com/advisories/39069
- http://tools.cisco.com/security/center/viewAlert.x?alertId=20070
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b20f33.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A6625

---

#### 796. CVE-2010-1387

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Use-after-free vulnerability in JavaScriptCore in WebKit in Apple iTunes before 9.2 on Windows, and Apple iOS before 4 on the iPhone and iPod touch, allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via vectors related to page transitions, a different vulnerability than CVE-2010-1763 and CVE-2010-1769.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Jun/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Jun/msg00002.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/40196

---

#### 797. CVE-2010-1769

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:itunes, microsoft:windows_xp, microsoft:windows_vista, microsoft:windows_7

**漏洞描述 / Description**:
WebKit in Apple iTunes before 9.2 on Windows, and Apple iOS before 4 on the iPhone and iPod touch, accesses out-of-bounds memory during the handling of tables, which allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted HTML document, a different vulnerability than CVE-2010-1387 and CVE-2010-1763.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Jun/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Jun/msg00002.html
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/40196
- http://secunia.com/advisories/43068

---

#### 798. CVE-2010-1407

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
WebKit in Apple iOS before 4 on the iPhone and iPod touch does not properly implement the history.replaceState method in certain situations involving IFRAME elements, which allows remote attackers to obtain sensitive information via a crafted HTML document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/41856
- http://secunia.com/advisories/42314

---

#### 799. CVE-2010-1751

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Application Sandbox in Apple iOS before 4 on the iPhone and iPod touch does not prevent photo-library access, which might allow remote attackers to obtain location information via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/59630
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html

---

#### 800. CVE-2010-1752

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Stack-based buffer overflow in CFNetwork in Apple iOS before 4 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via vectors related to URL handling.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00000.html
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://support.apple.com/kb/HT4435
- http://www.securityfocus.com/bid/41016

---

#### 801. CVE-2010-1753

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
ImageIO in Apple iOS before 4 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted JPEG image.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/59632
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html

---

#### 802. CVE-2010-1754

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Passcode Lock in Apple iOS before 4 on the iPhone and iPod touch does not properly handle alert-based unlocks in conjunction with subsequent Remote Lock operations through MobileMe, which allows physically proximate attackers to bypass intended passcode requirements via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/59633
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html

---

#### 803. CVE-2010-1755

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Safari in Apple iOS before 4 on the iPhone and iPod touch does not properly implement the Accept Cookies preference, which makes it easier for remote web servers to track users via a cookie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/59634
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html

---

#### 804. CVE-2010-1756

**严重程度 / Severity**: N/A | CVSS: 5.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
The Settings application in Apple iOS before 4 on the iPhone and iPod touch does not properly report the wireless network that is in use, which might make it easier for remote attackers to trick users into communicating over an unintended network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225

---

#### 805. CVE-2010-1757

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
WebKit in Apple iOS before 4 on the iPhone and iPod touch does not enforce the expected boundary restrictions on content display by an IFRAME element, which allows remote attackers to spoof the user interface via a crafted HTML document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/42314
- http://secunia.com/advisories/43068

---

#### 806. CVE-2010-1775

**严重程度 / Severity**: N/A | CVSS: 1.9
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Race condition in Passcode Lock in Apple iOS before 4 on the iPhone and iPod touch allows physically proximate attackers to bypass intended passcode requirements, and pair a locked device with a computer and access arbitrary data, via vectors involving the initial boot.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html
- http://support.apple.com/kb/HT4225
- http://www.securityfocus.com/bid/41016
- https://exchange.xforce.ibmcloud.com/vulnerabilities/59637
- http://lists.apple.com/archives/security-announce/2010/Jun/msg00003.html

---

#### 807. CVE-2010-1574

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:industrial_ethernet_3000, cisco:ios

**漏洞描述 / Description**:
IOS 12.2(52)SE and 12.2(52)SE1 on Cisco Industrial Ethernet (IE) 3000 series switches has (1) a community name of public for RO access and (2) a community name of private for RW access, which makes it easier for remote attackers to modify the configuration or obtain potentially sensitive information via SNMP requests, aka Bug ID CSCtf25589.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/66120.

**参考链接 / References**:
- http://osvdb.org/66120
- http://secunia.com/advisories/40407
- http://securitytracker.com/id?1024173
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b3891f.shtml
- http://www.kb.cert.org/vuls/id/732671

---

#### 808. CVE-2010-2913

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: citibank:citi_mobile, apple:iphone_os

**漏洞描述 / Description**:
The Citibank Citi Mobile app before 2.0.3 for iOS stores account data in a file, which allows local users to obtain sensitive information via vectors involving (1) the mobile device or (2) a synchronized computer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://itunes.apple.com/us/app/citi-mobile-sm/id301724680.

**参考链接 / References**:
- http://itunes.apple.com/us/app/citi-mobile-sm/id301724680
- http://news.cnet.com/8301-27080_3-20011664-245.html
- http://securitytracker.com/id?1024249
- https://exchange.xforce.ibmcloud.com/vulnerabilities/60855
- http://itunes.apple.com/us/app/citi-mobile-sm/id301724680

---

#### 809. CVE-2010-2973

**严重程度 / Severity**: N/A | CVSS: 6.9
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os, apple:ipad

**漏洞描述 / Description**:
Integer overflow in IOSurface in Apple iOS before 4.0.2 on the iPhone and iPod touch, and before 3.2.2 on the iPad, allows local users to gain privileges via vectors involving IOSurface properties, as demonstrated by JailbreakMe.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Aug/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Aug/msg00000.html
- http://lists.apple.com/archives/security-announce/2010//Aug/msg00001.html
- http://osvdb.org/66827
- http://secunia.com/advisories/40807
- http://support.apple.com/kb/HT4291

---

#### 810. CVE-2010-1797

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Multiple stack-based buffer overflows in the cff_decoder_parse_charstrings function in the CFF Type2 CharStrings interpreter in cff/cffgload.c in FreeType before 2.4.2, as used in Apple iOS before 4.0.2 on the iPhone and iPod touch and before 3.2.2 on the iPad, allow remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via crafted CFF opcodes in embedded fonts in a PDF document, as demonstrated by JailbreakMe. NOTE: some of these details are obtained from third party information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://freetype.sourceforge.net/index2.html#release-freetype-2.4.2.

**参考链接 / References**:
- http://freetype.sourceforge.net/index2.html#release-freetype-2.4.2
- http://git.savannah.gnu.org/cgit/freetype/freetype2.git/commit/?id=018f5c27813dd7eef4648fe254632ecea0c85a50
- http://git.savannah.gnu.org/cgit/freetype/freetype2.git/commit/?id=11d65e8a1f1f14e56148fd991965424d9bd1cdbc
- http://lists.apple.com/archives/security-announce/2010//Aug/msg00000.html
- http://lists.apple.com/archives/security-announce/2010//Aug/msg00001.html

---

#### 811. CVE-2010-2827

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 15.1(2)T allows remote attackers to cause a denial of service (resource consumption and TCP outage) via spoofed TCP packets, related to embryonic TCP connections that remain in the SYN_RCVD or SYN_SENT state, aka Bug ID CSCti18193.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4095e.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4095e.shtml
- http://www.securityfocus.com/bid/42426
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4095e.shtml
- http://www.securityfocus.com/bid/42426

---

#### 812. CVE-2010-3035

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.4.0 through 3.9.1, when BGP is enabled, does not properly handle unrecognized transitive attributes, which allows remote attackers to cause a denial of service (peering reset) via a crafted prefix announcement, as demonstrated in the wild in August 2010 with attribute type code 99, aka Bug ID CSCti62211.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://mailman.nanog.org/pipermail/nanog/2010-August/024837.html.

**参考链接 / References**:
- http://mailman.nanog.org/pipermail/nanog/2010-August/024837.html
- http://osvdb.org/67696
- http://secunia.com/advisories/41190
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4411f.shtml
- http://www.securitytracker.com/id?1024371

---

#### 813. CVE-2010-1781

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os, canonical:ubuntu_linux

**漏洞描述 / Description**:
Double free vulnerability in WebKit in Apple iOS before 4.1 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via vectors related to the rendering of an inline element.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2010-10/msg00000.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/41856

---

#### 814. CVE-2010-1809

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
The Accessibility component in Apple iOS before 4.1 on the iPhone and iPod touch does not perform the expected VoiceOver announcement associated with the location services icon, which has unspecified impact and attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334
- https://exchange.xforce.ibmcloud.com/vulnerabilities/61694
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334

---

#### 815. CVE-2010-1810

**严重程度 / Severity**: N/A | CVSS: 3.5
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
FaceTime in Apple iOS before 4.1 on the iPhone and iPod touch does not properly handle invalid X.509 certificates, which allows man-in-the-middle attackers to redirect calls via a crafted certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334
- https://exchange.xforce.ibmcloud.com/vulnerabilities/61695
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334

---

#### 816. CVE-2010-1811

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
ImageIO in Apple iOS before 4.1 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted TIFF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00000.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4334

---

#### 817. CVE-2010-1812

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, webkitgtk:webkitgtk, apple:iphone_os, canonical:ubuntu_linux

**漏洞描述 / Description**:
Use-after-free vulnerability in WebKit in Apple iOS before 4.1 on the iPhone and iPod touch, and webkitgtk before 1.2.6, allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via vectors involving selections.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/41856

---

#### 818. CVE-2010-1813

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
WebKit in Apple iOS before 4.1 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via vectors involving HTML object outlines.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/42314

---

#### 819. CVE-2010-1814

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, webkitgtk:webkitgtk, apple:iphone_os, canonical:ubuntu_linux

**漏洞描述 / Description**:
WebKit in Apple iOS before 4.1 on the iPhone and iPod touch, and webkitgtk before 1.2.6, allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via vectors involving form menus.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/41856

---

#### 820. CVE-2010-1815

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, webkitgtk:webkitgtk, apple:iphone_os, canonical:ubuntu_linux

**漏洞描述 / Description**:
Use-after-free vulnerability in WebKit in Apple iOS before 4.1 on the iPhone and iPod touch, and webkitgtk before 1.2.6, allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via vectors involving scrollbars.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00002.html
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/41856

---

#### 821. CVE-2010-1817

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Buffer overflow in ImageIO in Apple iOS before 4.1 on the iPhone and iPod touch allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted GIF file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334
- https://exchange.xforce.ibmcloud.com/vulnerabilities/61697
- http://lists.apple.com/archives/security-announce/2010//Sep/msg00002.html
- http://support.apple.com/kb/HT4334

---

#### 822. CVE-2010-2828

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the H.323 implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 2.5.x before 2.5.2 and 2.6.x before 2.6.1, allows remote attackers to cause a denial of service (device reload) via crafted H.323 packets, aka Bug ID CSCtc73759.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml

---

#### 823. CVE-2010-2829

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the H.323 implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 2.5.x before 2.5.2 and 2.6.x before 2.6.1, allows remote attackers to cause a denial of service (traceback and device reload) via crafted H.323 packets, aka Bug ID CSCtd33567.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a300.shtml

---

#### 824. CVE-2010-2830

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
The IGMPv3 implementation in Cisco IOS 12.2, 12.3, 12.4, and 15.0 and IOS XE 2.5.x before 2.5.2, when PIM is enabled, allows remote attackers to cause a denial of service (device reload) via a malformed IGMP packet, aka Bug ID CSCte14603.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a310.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a310.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a310.shtml

---

#### 825. CVE-2010-2831

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT for SIP implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1 allows remote attackers to cause a denial of service (device reload) via transit traffic on UDP port 5060, aka Bug ID CSCtf17624.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml

---

#### 826. CVE-2010-2832

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT for H.323 implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1 allows remote attackers to cause a denial of service (device reload) via transit traffic, aka Bug ID CSCtf91428.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml

---

#### 827. CVE-2010-2833

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT for H.225.0 implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1 allows remote attackers to cause a denial of service (device reload) via transit traffic, aka Bug ID CSCtd86472.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a311.shtml

---

#### 828. CVE-2010-2834

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 through 12.4 and 15.0 through 15.1, Cisco IOS XE 2.5.x and 2.6.x before 2.6.1, and Cisco Unified Communications Manager (aka CUCM, formerly CallManager) 6.x before 6.1(5)SU1, 7.x before 7.1(5), and 8.0 before 8.0(2) allow remote attackers to cause a denial of service (device reload or voice-services outage) via crafted SIP registration traffic over UDP, aka Bug IDs CSCtf72678 and CSCtf14987.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a313.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a313.shtml

---

#### 829. CVE-2010-2835

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2 through 12.4 and 15.0 through 15.1, Cisco IOS XE 2.5.x and 2.6.x before 2.6.1, and Cisco Unified Communications Manager (aka CUCM, formerly CallManager) 6.x before 6.1(5), 7.0 before 7.0(2a)su3, 7.1su before 7.1(3b)su2, 7.1 before 7.1(5), and 8.0 before 8.0(1) allow remote attackers to cause a denial of service (device reload or voice-services outage) via a SIP REFER request with an invalid Refer-To header, aka Bug IDs CSCta20040 and CSCta31358.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a313.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a30f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a313.shtml

---

#### 830. CVE-2010-2836

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the SSL VPN feature in Cisco IOS 12.4, 15.0, and 15.1, when HTTP port redirection is enabled, allows remote attackers to cause a denial of service (memory consumption) by improperly disconnecting SSL sessions, leading to connections that remain in the CLOSE-WAIT state, aka Bug ID CSCtg21685.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a312.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a312.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b4a312.shtml

---

#### 831. CVE-2010-4211

**严重程度 / Severity**: N/A | CVSS: 2.9
**受影响产品 / Affected Products**: ebay:paypal, apple:iphone_os

**漏洞描述 / Description**:
The PayPal app before 3.0.1 for iOS does not verify that the server hostname matches the domain name of the subject of an X.509 certificate, which allows man-in-the-middle attackers to spoof a PayPal web server via an arbitrary certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://itunes.apple.com/us/app/paypal/id283646709.

**参考链接 / References**:
- http://itunes.apple.com/us/app/paypal/id283646709
- http://news.cnet.com/8301-27080_3-20021730-245.html
- http://online.wsj.com/article/SB10001424052748703506904575592782874885808.html
- http://viaforensics.com/press-releases/viaforensics-uncovers-paypal-application-vulnerability.html
- http://viaforensics.com/security/viaforensics-uncovers-significant-vulnerability-paypal-iphone.html

---

#### 832. CVE-2010-3827

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Apple iOS before 4.2 does not properly validate signatures before displaying a configuration profile in the configuration installation utility, which allows remote attackers to spoof profiles via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4456
- http://www.securitytracker.com/id?1024768
- http://www.vupen.com/english/advisories/2010/3046

---

#### 833. CVE-2010-3828

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
iAd Content Display in Apple iOS before 4.2 allows man-in-the-middle attackers to make calls via a crafted URL in an ad.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4456
- http://www.securitytracker.com/id?1024768
- http://www.vupen.com/english/advisories/2010/3046

---

#### 834. CVE-2010-3829

**严重程度 / Severity**: N/A | CVSS: 5.8
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
WebKit in Apple iOS before 4.2 allows remote attackers to bypass the remote image loading setting in Mail via an HTML LINK element with a DNS prefetching property, as demonstrated by an HTML e-mail message that uses a LINK element for X-Confirm-Reading-To functionality, a related issue to CVE-2010-3813.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00002.html
- http://lists.opensuse.org/opensuse-security-announce/2011-01/msg00006.html
- http://secunia.com/advisories/42314
- http://secunia.com/advisories/43068

---

#### 835. CVE-2010-3830

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Networking in Apple iOS before 4.2 accesses an invalid pointer during the processing of packet filter rules, which allows local users to gain privileges via unspecified vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4456
- http://www.securitytracker.com/id?1024772
- http://www.vupen.com/english/advisories/2010/3046

---

#### 836. CVE-2010-3831

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Photos in Apple iOS before 4.2 enables support for HTTP Basic Authentication over an unencrypted connection, which allows man-in-the-middle attackers to read MobileMe account passwords by spoofing a MobileMe Gallery server during a "Send to MobileMe" action.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4456
- http://www.securitytracker.com/id?1024771
- http://www.vupen.com/english/advisories/2010/3046

---

#### 837. CVE-2010-3832

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:ipad

**漏洞描述 / Description**:
Heap-based buffer overflow in the GSM mobility management implementation in Telephony in Apple iOS before 4.2 on the iPhone and iPad allows remote attackers to execute arbitrary code on the baseband processor via a crafted Temporary Mobile Subscriber Identity (TMSI) field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2010//Nov/msg00003.html
- http://secunia.com/advisories/42314
- http://support.apple.com/kb/HT4456
- http://www.securitytracker.com/id?1024770
- http://www.vupen.com/english/advisories/2010/3046

---

#### 838. CVE-2010-4012

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Race condition in Apple iOS 4.0 through 4.1 for iPhone 3G and later allows physically proximate attackers to bypass the passcode lock by making a call from the Emergency Call screen, then quickly pressing the Sleep/Wake button.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.apple.com/kb/HT4456.

**参考链接 / References**:
- http://support.apple.com/kb/HT4456
- http://support.apple.com/kb/HT4456

---

#### 839. CVE-2010-4671

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Neighbor Discovery (ND) protocol implementation in the IPv6 stack in Cisco IOS before 15.0(1)XA5 allows remote attackers to cause a denial of service (CPU consumption and device hang) by sending many Router Advertisement (RA) messages with different source addresses, as demonstrated by the flood_router6 program in the thc-ipv6 package, aka Bug ID CSCti33534.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://events.ccc.de/congress/2010/Fahrplan/events/3957.en.html.

**参考链接 / References**:
- http://events.ccc.de/congress/2010/Fahrplan/events/3957.en.html
- http://mirror.fem-net.de/CCC/27C3/mp3-audio-only/27c3-3957-en-ipv6_insecurities.mp3
- http://mirror.fem-net.de/CCC/27C3/mp4-h264-HQ/27c3-3957-en-ipv6_insecurities.mp4
- http://www.ciscosystems.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45760

---

#### 840. CVE-2009-5038

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS before 15.0(1)XA does not properly handle IRC traffic during a specific time period after an initial reload, which allows remote attackers to cause a denial of service (device reload) via an attempted connection to a certain IRC server, related to a "corrupted magic value," aka Bug ID CSCso05336.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45764
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64682
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45764

---

#### 841. CVE-2009-5039

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in the gk_circuit_info_do_in_acf function in the H.323 implementation in Cisco IOS before 15.0(1)XA allows remote attackers to cause a denial of service (memory consumption) via a large number of calls over a long duration, as demonstrated by InterZone Clear Token (IZCT) test traffic, aka Bug ID CSCsz72535.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64731
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64731

---

#### 842. CVE-2009-5040

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
CallManager Express (CME) on Cisco IOS before 15.0(1)XA allows remote authenticated users to cause a denial of service (device crash) by using an extension mobility (EM) phone to interact with the menu for SNR number changes, aka Bug ID CSCta63555.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45765
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64681
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45765

---

#### 843. CVE-2010-4683

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in Cisco IOS before 15.0(1)XA5 might allow remote attackers to cause a denial of service (memory consumption) by sending a crafted SIP REGISTER message over UDP, aka Bug ID CSCtg41733.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45786
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64588
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45786

---

#### 844. CVE-2010-4684

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS before 15.0(1)XA1, when certain TFTP debugging is enabled, allows remote attackers to cause a denial of service (device crash) via a TFTP copy over IPv6, aka Bug ID CSCtb28877.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64587
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769

---

#### 845. CVE-2010-4685

**严重程度 / Severity**: N/A | CVSS: 4.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS before 15.0(1)XA1 does not clear the public key cache upon a change to a certificate map, which allows remote authenticated users to bypass a certificate ban by connecting with a banned certificate that had previously been valid, aka Bug ID CSCta79031.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64586
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769

---

#### 846. CVE-2010-4686

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
CallManager Express (CME) on Cisco IOS before 15.0(1)XA1 does not properly handle SIP TRUNK traffic that contains rate bursts and a "peculiar" request size, which allows remote attackers to cause a denial of service (memory consumption) by sending this traffic over a long duration, aka Bug ID CSCtb47950.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64585
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769

---

#### 847. CVE-2010-4687

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
STCAPP (aka the SCCP telephony control application) on Cisco IOS before 15.0(1)XA1 does not properly handle multiple calls to a shared line, which allows remote attackers to cause a denial of service (port hang) by simultaneously ending two calls that were controlled by CallManager Express (CME), aka Bug ID CSCtd42552.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769
- https://exchange.xforce.ibmcloud.com/vulnerabilities/64584
- http://www.cisco.com/en/US/docs/ios/15_0/15_0x/15_01_XA/rn800xa.pdf
- http://www.securityfocus.com/bid/45769

---

#### 848. CVE-2011-0348

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: cisco:content_services_gateway_second_generation, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.4(11)MD, 12.4(15)MD, 12.4(22)MD, 12.4(24)MD before 12.4(24)MD3, 12.4(22)MDA before 12.4(22)MDA5, and 12.4(24)MDA before 12.4(24)MDA3 on the Cisco Content Services Gateway Second Generation (aka CSG2) allows remote attackers to bypass intended access restrictions and intended billing restrictions by sending HTTP traffic to a restricted destination after sending HTTP traffic to an unrestricted destination, aka Bug ID CSCtk35917.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/70720.

**参考链接 / References**:
- http://osvdb.org/70720
- http://secunia.com/advisories/43052
- http://securitytracker.com/id?1024992
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b6791d.shtml
- http://www.securityfocus.com/bid/46022

---

#### 849. CVE-2011-0349

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:content_services_gateway_second_generation, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.4(24)MD before 12.4(24)MD2 on the Cisco Content Services Gateway Second Generation (aka CSG2) allows remote attackers to cause a denial of service (device hang or reload) via crafted TCP packets, aka Bug ID CSCth17178, a different vulnerability than CVE-2011-0350.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/70721.

**参考链接 / References**:
- http://osvdb.org/70721
- http://secunia.com/advisories/43052
- http://securitytracker.com/id?1024992
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b6791d.shtml
- http://www.securityfocus.com/bid/46026

---

#### 850. CVE-2011-0350

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:content_services_gateway_second_generation, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.4(24)MD before 12.4(24)MD2 on the Cisco Content Services Gateway Second Generation (aka CSG2) allows remote attackers to cause a denial of service (device hang or reload) via crafted TCP packets, aka Bug ID CSCth41891, a different vulnerability than CVE-2011-0349.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/70722.

**参考链接 / References**:
- http://osvdb.org/70722
- http://secunia.com/advisories/43052
- http://securitytracker.com/id?1024992
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b6791d.shtml
- http://www.securityfocus.com/bid/46028

---

#### 851. CVE-2011-0154

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:iphone_os

**漏洞描述 / Description**:
WebKit, as used in Apple iTunes before 10.2 on Windows and Apple iOS, does not properly implement the .sort function for JavaScript arrays, which allows man-in-the-middle attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via vectors related to iTunes Store browsing, a different vulnerability than other CVEs listed in APPLE-SA-2011-03-02-1.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00004.html
- http://lists.apple.com/archives/security-announce/2011/Mar/msg00000.html
- http://support.apple.com/kb/HT4554
- http://support.apple.com/kb/HT4564

---

#### 852. CVE-2011-1344

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:iphone, apple:ipad, apple:safari, apple:ipod_touch, apple:iphone_os

**漏洞描述 / Description**:
Use-after-free vulnerability in WebKit, as used in Apple Safari before 5.0.5; iOS before 4.3.2 for iPhone, iPod, and iPad; iOS before 4.2.7 for iPhone 4 (CDMA); and possibly other products allows remote attackers to execute arbitrary code by adding children to a WBR tag and then removing the tag, related to text nodes, as demonstrated by Chaouki Bekrar during a Pwn2Own competition at CanSecWest 2011.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://dvlabs.tippingpoint.com/blog/2011/02/02/pwn2own-2011.

**参考链接 / References**:
- http://dvlabs.tippingpoint.com/blog/2011/02/02/pwn2own-2011
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00001.html
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00002.html
- http://secunia.com/advisories/44151

---

#### 853. CVE-2011-1417

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
Integer overflow in QuickLook, as used in Apple Mac OS X before 10.6.7 and MobileSafari in Apple iOS before 4.2.7 and 4.3.x before 4.3.2, allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a Microsoft Office document with a crafted size field in the OfficeArtMetafileHeader, related to OfficeArtBlip, as demonstrated on the iPhone by Charlie Miller and Dion Blazakis during a Pwn2Own competition at CanSecWest 2011.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://dvlabs.tippingpoint.com/blog/2011/02/02/pwn2own-2011.

**参考链接 / References**:
- http://dvlabs.tippingpoint.com/blog/2011/02/02/pwn2own-2011
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00005.html
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00001.html
- http://lists.apple.com/archives/security-announce/2011/Mar/msg00006.html

---

#### 854. CVE-2011-0157

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:iphone_os, apple:webkit

**漏洞描述 / Description**:
WebKit, as used in Apple iOS before 4.3, allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site, a different vulnerability than other CVEs listed in APPLE-SA-2011-03-09-1.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://support.apple.com/kb/HT4564
- http://www.securityfocus.com/bid/46807
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66007
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html

---

#### 855. CVE-2011-0158

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
MobileSafari in Apple iOS before 4.3 does not properly implement application launching through URL handlers, which allows remote attackers to cause a denial of service (persistent application crash) via crafted JavaScript code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://support.apple.com/kb/HT4564
- http://www.securityfocus.com/bid/46806
- http://www.securitytracker.com/id?1025182
- https://exchange.xforce.ibmcloud.com/vulnerabilities/66002

---

#### 856. CVE-2011-0159

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The Safari Settings feature in Safari in Apple iOS 4.x before 4.3 does not properly implement the clearing of cookies during execution of the Safari application, which might make it easier for remote web servers to track users by setting a cookie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://support.apple.com/kb/HT4564
- http://www.securityfocus.com/bid/46810
- http://www.securitytracker.com/id?1025182
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html

---

#### 857. CVE-2011-0160

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:iphone_os, apple:webkit, apple:safari

**漏洞描述 / Description**:
WebKit, as used in Apple Safari before 5.0.4 and iOS before 4.3, does not properly handle redirects in conjunction with HTTP Basic Authentication, which might allow remote web servers to capture credentials by logging the Authorization HTTP header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00004.html
- http://support.apple.com/kb/HT4564
- http://support.apple.com/kb/HT4566
- http://www.securitytracker.com/id?1025182

---

#### 858. CVE-2011-0161

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:webkit, apple:safari

**漏洞描述 / Description**:
WebKit, as used in Apple Safari before 5.0.4 and iOS before 4.3, does not properly handle the Attr.style accessor, which allows remote attackers to bypass the Same Origin Policy and inject Cascading Style Sheets (CSS) token sequences via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00004.html
- http://support.apple.com/kb/HT4564
- http://support.apple.com/kb/HT4566
- http://www.securityfocus.com/bid/46814

---

#### 859. CVE-2011-0162

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: apple:apple_tv, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
Wi-Fi in Apple iOS before 4.3 and Apple TV before 4.2 does not properly perform bounds checking for Wi-Fi frames, which allows remote attackers to cause a denial of service (device reset) via unspecified traffic on the local wireless network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00005.html
- http://support.apple.com/kb/HT4564
- http://support.apple.com/kb/HT4565
- http://www.securityfocus.com/bid/46813

---

#### 860. CVE-2011-0163

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:webkit, apple:safari

**漏洞描述 / Description**:
WebKit, as used in Apple Safari before 5.0.4 and iOS before 4.3, does not properly handle unspecified "cached resources," which allows remote attackers to cause a denial of service (resource unavailability) via a crafted web site that conducts a cache-poisoning attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00004.html
- http://support.apple.com/kb/HT4564
- http://support.apple.com/kb/HT4566
- http://www.securitytracker.com/id?1025182

---

#### 861. CVE-2011-1418

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:apple_tv, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
The stateless address autoconfiguration (aka SLAAC) functionality in the IPv6 networking implementation in Apple iOS before 4.3 and Apple TV before 4.2 places the MAC address into the IPv6 address, which makes it easier for remote IPv6 servers to track users by logging source IPv6 addresses.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00005.html
- http://support.apple.com/kb/HT4564
- http://support.apple.com/kb/HT4565
- http://lists.apple.com/archives/security-announce/2011//Mar/msg00003.html

---

#### 862. CVE-2011-0935

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The PKI functionality in Cisco IOS 15.0 and 15.1 does not prevent permanent caching of certain public keys, which allows remote attackers to bypass authentication and have unspecified other impact by leveraging an IKE peer relationship in which a key was previously valid but later revoked, aka Bug ID CSCth82164, a different vulnerability than CVE-2010-4685.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/ios/15_1/release/notes/151-2TCAVS.html.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/ios/15_1/release/notes/151-2TCAVS.html
- http://www.cisco.com/en/US/docs/ios/15_1s/release/notes/15_1s_caveats_15_1_1s.html
- http://www.securityfocus.com/bid/47407
- http://www.cisco.com/en/US/docs/ios/15_1/release/notes/151-2TCAVS.html
- http://www.cisco.com/en/US/docs/ios/15_1s/release/notes/15_1s_caveats_15_1_1s.html

---

#### 863. CVE-2011-0195

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The generate-id XPath function in libxslt in Apple iOS 4.3.x before 4.3.2 allows remote attackers to obtain potentially sensitive information about heap memory addresses via a crafted web site.  NOTE: this may overlap CVE-2011-1202.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Apr/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Apr/msg00000.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00002.html
- http://lists.apple.com/archives/security-announce/2011//Jun/msg00000.html
- http://support.apple.com/kb/HT4723
- http://support.apple.com/kb/HT4808

---

#### 864. CVE-2011-0943

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.8.3, 3.8.4, and 3.9.1 allows remote attackers to cause a denial of service (NetIO process restart or device reload) via a crafted IPv4 packet, aka Bug ID CSCth44147.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18e.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18e.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18e.shtml

---

#### 865. CVE-2011-0949

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.6.x, 3.8.x before 3.8.3, and 3.9.x before 3.9.1 does not properly remove sshd_lock files from /tmp/, which allows remote attackers to cause a denial of service (disk consumption) by making many SSHv1 connections, aka Bug ID CSCtd64417.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18f.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18f.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f18f.shtml

---

#### 866. CVE-2011-1651

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xr

**漏洞描述 / Description**:
Cisco IOS XR 3.9.x and 4.0.x before 4.0.3 and 4.1.x before 4.1.1, when an SPA interface processor is installed, allows remote attackers to cause a denial of service (device reload) via a crafted IPv4 packet, aka Bug ID CSCto45095.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f191.shtml.

**参考链接 / References**:
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f191.shtml
- http://www.securitytracker.com/id?1025567
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b7f191.shtml
- http://www.securitytracker.com/id?1025567

---

#### 867. CVE-2011-2395

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
The Neighbor Discovery (ND) protocol implementation in Cisco IOS on unspecified switches allows remote attackers to bypass the Router Advertisement Guarding functionality via a fragmented IPv6 packet in which the Router Advertisement (RA) message is contained in the second fragment, as demonstrated by (1) a packet in which the first fragment contains a long Destination Options extension header or (2) a packet in which the first fragment contains an ICMPv6 Echo Request message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://seclists.org/fulldisclosure/2011/May/446.

**参考链接 / References**:
- http://seclists.org/fulldisclosure/2011/May/446
- http://securityreason.com/securityalert/8271
- https://exchange.xforce.ibmcloud.com/vulnerabilities/67940
- http://seclists.org/fulldisclosure/2011/May/446
- http://securityreason.com/securityalert/8271

---

#### 868. CVE-2011-2064

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:content_services_gateway_second_generation, cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.4MDA before 12.4(24)MDA5 on the Cisco Content Services Gateway - Second Generation (CSG2) allows remote attackers to cause a denial of service (device reload) via crafted ICMP packets, aka Bug ID CSCtl79577.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/73657.

**参考链接 / References**:
- http://osvdb.org/73657
- http://secunia.com/advisories/45148
- http://securitytracker.com/id?1025748
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b86503.shtml
- http://www.securityfocus.com/bid/48581

---

#### 869. CVE-2011-0226

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: apple:iphone_os, freetype:freetype

**漏洞描述 / Description**:
Integer signedness error in psaux/t1decode.c in FreeType before 2.4.6, as used in CoreGraphics in Apple iOS before 4.2.9 and 4.3.x before 4.3.4 and other products, allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted Type 1 font in a PDF document, as exploited in the wild in July 2011.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00003.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00003.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00000.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00001.html
- http://lists.nongnu.org/archive/html/freetype-devel/2011-07/msg00014.html
- http://lists.nongnu.org/archive/html/freetype-devel/2011-07/msg00015.html

---

#### 870. CVE-2011-0227

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The queueing primitives in IOMobileFrameBuffer in Apple iOS before 4.2.9 and 4.3.x before 4.3.4 do not properly perform type conversion, which allows local users to gain privileges via a crafted application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Jul/msg00000.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00000.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00001.html
- http://support.apple.com/kb/HT4802
- http://support.apple.com/kb/HT4803
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00000.html

---

#### 871. CVE-2011-2549

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:asr_9006_router, cisco:asr_9010_router, cisco:ios_xr

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS XR 4.1.x before 4.1.1 on Cisco Aggregation Services Routers (ASR) 9000 series devices allows remote attackers to cause a denial of service (line-card reload) via an IPv4 packet, aka Bug ID CSCtr26695.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://secunia.com/advisories/45333.

**参考链接 / References**:
- http://secunia.com/advisories/45333
- http://securitytracker.com/id?1025811
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b89155.shtml
- http://www.securityfocus.com/bid/48811
- https://exchange.xforce.ibmcloud.com/vulnerabilities/68733

---

#### 872. CVE-2011-1624

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2(58)SE, when a login banner is configured, allows remote attackers to cause a denial of service (device reload) by establishing two SSH2 sessions, aka Bug ID CSCto62631.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/switches/lan/cisco_ie3000/software/release/12.2_58_se/release/notes/OL24335.html.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/switches/lan/cisco_ie3000/software/release/12.2_58_se/release/notes/OL24335.html
- https://supportforums.cisco.com/message/3356210
- http://www.cisco.com/en/US/docs/switches/lan/cisco_ie3000/software/release/12.2_58_se/release/notes/OL24335.html
- https://supportforums.cisco.com/message/3356210

---

#### 873. CVE-2011-1625

**严重程度 / Severity**: N/A | CVSS: 5.4
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.2, 12.3, 12.4, 15.0, and 15.1, when the data-link switching (DLSw) feature is configured, allows remote attackers to cause a denial of service (device crash) by sending a sequence of malformed packets and leveraging a "narrow timing window," aka Bug ID CSCtf74999, a different vulnerability than CVE-2007-0199, CVE-2008-1152, and CVE-2009-0629.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/en/US/docs/cable/cmts/release/notes/12_2sc/uBR7200/122_33_SCF/caveats.html.

**参考链接 / References**:
- http://www.cisco.com/en/US/docs/cable/cmts/release/notes/12_2sc/uBR7200/122_33_SCF/caveats.html
- http://www.cisco.com/en/US/docs/cable/cmts/release/notes/12_2sc/uBR7200/122_33_SCF/caveats.html

---

#### 874. CVE-2011-0228

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The Data Security component in Apple iOS before 4.2.10 and 4.3.x before 4.3.5 does not check the basicConstraints parameter during validation of X.509 certificate chains, which allows man-in-the-middle attackers to spoof an SSL server by using a non-CA certificate to sign a certificate for an arbitrary domain.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/security-announce/2011//Jul/msg00004.html.

**参考链接 / References**:
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00004.html
- http://lists.apple.com/archives/security-announce/2011//Jul/msg00005.html
- http://secunia.com/advisories/45369
- http://securityreason.com/securityalert/8361
- http://securitytracker.com/id?1025837

---

#### 875. CVE-2011-0939

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.4, 15.0, and 15.1, and IOS XE 2.5.x through 3.2.x, allows remote attackers to cause a denial of service (device reload) via a crafted SIP message, aka Bug ID CSCth03022.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24127.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24127
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d5a.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24127
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d5a.shtml

---

#### 876. CVE-2011-0944

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Cisco IOS 12.4, 15.0, and 15.1 allows remote attackers to cause a denial of service (device reload) via malformed IPv6 packets, aka Bug ID CSCtj41194.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24131.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24131
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d59.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24131
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d59.shtml

---

#### 877. CVE-2011-0945

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Memory leak in the Data-link switching (aka DLSw) feature in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xS before 3.1.3S and 3.2.xS before 3.2.1S, when implemented over Fast Sequence Transport (FST), allows remote attackers to cause a denial of service (memory consumption and device reload or hang) via a crafted IP protocol 91 packet, aka Bug ID CSCth69364.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24116.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24116
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4e.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24116
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4e.shtml

---

#### 878. CVE-2011-0946

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
The NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (device reload or hang) via malformed NetMeeting Directory (aka Internet Locator Service or ILS) LDAP traffic, aka Bug ID CSCtd10712.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24117.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24117
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24117
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 879. CVE-2011-2072

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:unified_communications_manager, cisco:ios

**漏洞描述 / Description**:
Memory leak in Cisco IOS 12.4, 15.0, and 15.1, Cisco IOS XE 2.5.x through 3.2.x, and Cisco Unified Communications Manager (CUCM) 6.x and 7.x before 7.1(5b)su4, 8.x before 8.5(1)su2, and 8.6 before 8.6(1) allows remote attackers to cause a denial of service (memory consumption and device reload or process failure) via a malformed SIP message, aka Bug IDs CSCtl86047 and CSCto88686.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20110928-cucm.

**参考链接 / References**:
- http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20110928-cucm
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24129
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d58.shtml
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d5a.shtml
- http://www.securitytracker.com/id?1026110

---

#### 880. CVE-2011-3270

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:10008_router, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2SB before 12.2(33)SB10 and 15.0S before 15.0(1)S3a on Cisco 10000 series routers allows remote attackers to cause a denial of service (device reload) via a sequence of crafted ICMP packets, aka Bug ID CSCtk62453.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24114.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24114
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d50.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24114
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d50.shtml

---

#### 881. CVE-2011-3271

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the Smart Install functionality in Cisco IOS 12.2 and 15.1 allows remote attackers to execute arbitrary code or cause a denial of service (device crash) via crafted TCP packets to port 4786, aka Bug ID CSCto10165.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24115.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24115
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4f.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24115
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4f.shtml

---

#### 882. CVE-2011-3272

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
The IP Service Level Agreement (IP SLA) functionality in Cisco IOS 15.1, and IOS XE 2.1.x through 3.3.x, allows remote attackers to cause a denial of service (memory corruption and device reload) via malformed IP SLA packets, aka Bug ID CSCtk67073.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24122.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24122
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4c.shtml
- http://www.securitytracker.com/id?1026120
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24122
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4c.shtml

---

#### 883. CVE-2011-3273

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Memory leak in Cisco IOS 15.0 through 15.1, when IPS or Zone-Based Firewall (aka ZBFW) is configured, allows remote attackers to cause a denial of service (memory consumption or device crash) via vectors that trigger many session creation flows, aka Bug ID CSCti79848.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24123.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24123
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d57.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24123
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d57.shtml

---

#### 884. CVE-2011-3274

**严重程度 / Severity**: N/A | CVSS: 6.1
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2SRE before 12.2(33)SRE4, 15.0, and 15.1, and IOS XE 2.1.x through 3.3.x, when an MPLS domain is configured, allows remote attackers to cause a denial of service (device crash) via a crafted IPv6 packet, related to an expired MPLS TTL, aka Bug ID CSCto07919.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24125.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24125
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d52.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24125
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d52.shtml

---

#### 885. CVE-2011-3275

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Memory leak in Cisco IOS 12.4, 15.0, and 15.1, and IOS XE 2.5.x through 3.2.x, allows remote attackers to cause a denial of service (memory consumption) via a crafted SIP message, aka Bug ID CSCti48504.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24130.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24130
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d5a.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24130
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d5a.shtml

---

#### 886. CVE-2011-3276

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (device reload or hang) by sending crafted SIP packets to TCP port 5060, aka Bug ID CSCso02147.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24118.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24118
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24118
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 887. CVE-2011-3277

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (device reload) by sending crafted H.323 packets to TCP port 1720, aka Bug ID CSCth11006.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24119.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24119
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24119
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 888. CVE-2011-3278

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in the NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (device reload) by sending crafted SIP packets to UDP port 5060, aka Bug ID CSCti48483.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24120.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24120
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24120
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 889. CVE-2011-3279

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
The provider-edge MPLS NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (device reload) via a malformed SIP packet to UDP port 5060, aka Bug ID CSCti98219.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24121.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24121
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A13781
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24121
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 890. CVE-2011-3280

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Memory leak in the NAT implementation in Cisco IOS 12.1 through 12.4 and 15.0 through 15.1, and IOS XE 3.1.xSG, allows remote attackers to cause a denial of service (memory consumption or device reload) by sending crafted SIP packets to UDP port 5060, aka Bug ID CSCtj04672.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24120.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24120
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24120
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d4d.shtml

---

#### 891. CVE-2011-3281

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 15.0 through 15.1, in certain HTTP Layer 7 Application Control and Inspection configurations, allows remote attackers to cause a denial of service (device reload or hang) via a crafted HTTP packet, aka Bug ID CSCto68554.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24124.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24124
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d57.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24124
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d57.shtml

---

#### 892. CVE-2011-3282

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: cisco:ios_xe, cisco:ios

**漏洞描述 / Description**:
Unspecified vulnerability in Cisco IOS 12.2SRE before 12.2(33)SRE4, 15.0, and 15.1, and IOS XE 2.1.x through 3.3.x, when an MPLS domain is configured, allows remote attackers to cause a denial of service (device reload) via an ICMPv6 packet, related to an expired MPLS TTL, aka Bug ID CSCtj30155.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://tools.cisco.com/security/center/viewAlert.x?alertId=24126.

**参考链接 / References**:
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24126
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d52.shtml
- http://tools.cisco.com/security/center/viewAlert.x?alertId=24126
- http://www.cisco.com/en/US/products/products_security_advisory09186a0080b95d52.shtml

---

#### 893. CVE-2011-3243

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os, apple:safari

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in WebKit, as used in Apple iOS before 5 and Safari before 5.1.1, allows remote attackers to inject arbitrary web script or HTML via vectors involving inactive DOM windows.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00004.html
- http://osvdb.org/76353
- http://support.apple.com/kb/HT4999
- http://support.apple.com/kb/HT5000

---

#### 894. CVE-2011-3245

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The Keyboards component in Apple iOS before 5 displays the final character of an entered password during a subsequent use of a keyboard, which allows physically proximate attackers to obtain sensitive information by reading this character.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://osvdb.org/76329
- http://support.apple.com/kb/HT4999
- https://exchange.xforce.ibmcloud.com/vulnerabilities/70555
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html

---

#### 895. CVE-2011-3246

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:iphone_os, apple:mac_os_x, apple:mac_os_x_server

**漏洞描述 / Description**:
CFNetwork in Apple iOS before 5.0.1 and Mac OS X 10.7 before 10.7.2 does not properly parse URLs, which allows remote attackers to trigger visits to unintended web sites, and transmission of cookies to unintended web sites, via a crafted (1) http or (2) https URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00003.html
- http://lists.apple.com/archives/Security-announce/2011/Nov/msg00001.html
- http://lists.apple.com/archives/security-announce/2012/Feb/msg00000.html
- http://support.apple.com/kb/HT4999

---

#### 896. CVE-2011-3253

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
CalDAV in Apple iOS before 5 does not validate X.509 certificates for SSL sessions, which allows man-in-the-middle attackers to spoof calendar servers and obtain sensitive information via an arbitrary certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999

---

#### 897. CVE-2011-3254

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in Calendar in Apple iOS before 5 allows remote attackers to inject arbitrary web script or HTML via an invitation note.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999

---

#### 898. CVE-2011-3255

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
CFNetwork in Apple iOS before 5 stores AppleID credentials in an unspecified file, which makes it easier for remote attackers to obtain sensitive information via a crafted application.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999
- https://exchange.xforce.ibmcloud.com/vulnerabilities/70550
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999

---

#### 899. CVE-2011-3256

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
FreeType 2 before 2.4.7, as used in CoreGraphics in Apple iOS before 5, Mandriva Enterprise Server 5, and possibly other products, allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted font, a different vulnerability than CVE-2011-0226.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://lists.apple.com/archives/security-announce/2012/Feb/msg00000.html
- http://lists.fedoraproject.org/pipermail/package-announce/2011-November/069100.html
- http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00008.html
- http://lists.opensuse.org/opensuse-security-announce/2012-01/msg00003.html

---

#### 900. CVE-2011-3257

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
The Data Access component in Apple iOS before 5 does not properly handle the existence of multiple user accounts on the same mail server, which allows local users to bypass intended access restrictions in opportunistic circumstances by leveraging a different account's cookie.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://osvdb.org/76325
- http://support.apple.com/kb/HT4999
- https://exchange.xforce.ibmcloud.com/vulnerabilities/70553
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html

---

#### 901. CVE-2011-3259

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: apple:apple_tv, apple:iphone_os

**漏洞描述 / Description**:
The kernel in Apple iOS before 5 and Apple TV before 4.4 does not properly recover memory allocated for incomplete TCP connections, which allows remote attackers to cause a denial of service (resource consumption) by making many connection attempts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00002.html
- http://support.apple.com/kb/HT4999
- http://support.apple.com/kb/HT5001
- http://www.securityfocus.com/bid/50087

---

#### 902. CVE-2011-3260

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: apple:iphone_os

**漏洞描述 / Description**:
Buffer overflow in OfficeImport in Apple iOS before 5 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted Microsoft Word document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html.

**参考链接 / References**:
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999
- https://exchange.xforce.ibmcloud.com/vulnerabilities/70556
- http://lists.apple.com/archives/Security-announce/2011//Oct/msg00001.html
- http://support.apple.com/kb/HT4999

---

#### 903. CVE-2017-6986

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "iBooks" component. It allows attackers to conduct sandbox-escape attacks or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 904. CVE-2017-6987

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/98468.

**参考链接 / References**:
- http://www.securityfocus.com/bid/98468
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- https://support.apple.com/HT207800

---

#### 905. CVE-2017-6988

**严重程度 / Severity**: MEDIUM | CVSS: 5.9
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "802.1X" component. It allows remote attackers to discover the network credentials of arbitrary users by operating a crafted network that requires 802.1X authentication, because EAP-TLS certificate validation mishandles certificate changes.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 906. CVE-2017-6990

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.5 is affected. The issue involves the "HFS" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 907. CVE-2017-6991

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted web site.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securitytracker.com/id/1038484.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797
- https://support.apple.com/HT207798
- http://www.securitytracker.com/id/1038484
- https://support.apple.com/HT207797

---

#### 908. CVE-2017-9977

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:macos, avg:anti-virus

**漏洞描述 / Description**:
AVG AntiVirus for MacOS with scan engine before 4668 might allow remote attackers to bypass malware detection by leveraging failure to scan inside disk image (aka DMG) files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://wwws.nightwatchcybersecurity.com/2017/07/06/avg-antivirus-for-macos-doesnt-scan-inside-disk-images-cve-2017-9977/.

**参考链接 / References**:
- https://wwws.nightwatchcybersecurity.com/2017/07/06/avg-antivirus-for-macos-doesnt-scan-inside-disk-images-cve-2017-9977/
- https://wwws.nightwatchcybersecurity.com/2017/07/06/avg-antivirus-for-macos-doesnt-scan-inside-disk-images-cve-2017-9977/

---

#### 909. CVE-2017-2240

**严重程度 / Severity**: MEDIUM | CVSS: 6.5
**受影响产品 / Affected Products**: hammock:assetview, apple:mac_os_x

**漏洞描述 / Description**:
Directory traversal vulnerability in AssetView for MacOS Ver.9.2.0 and earlier versions allows remote attackers to read arbitrary files via "File Transfer Web Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jvn.jp/en/vu/JVNVU93377948/index.html.

**参考链接 / References**:
- http://jvn.jp/en/vu/JVNVU93377948/index.html
- https://www.hammock.jp/assetview/info/170714.html
- http://jvn.jp/en/vu/JVNVU93377948/index.html
- https://www.hammock.jp/assetview/info/170714.html

---

#### 910. CVE-2017-2241

**严重程度 / Severity**: MEDIUM | CVSS: 6.3
**受影响产品 / Affected Products**: hammock:assetview, apple:mac_os_x

**漏洞描述 / Description**:
SQL injection vulnerability in the AssetView for MacOS Ver.9.2.0 and earlier versions allows remote attackers to execute arbitrary SQL commands via "File Transfer Web Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://jvn.jp/en/vu/JVNVU93377948/index.html.

**参考链接 / References**:
- http://jvn.jp/en/vu/JVNVU93377948/index.html
- https://www.hammock.jp/assetview/info/170714.html
- http://jvn.jp/en/vu/JVNVU93377948/index.html
- https://www.hammock.jp/assetview/info/170714.html

---

#### 911. CVE-2017-7008

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. The issue involves the "CoreAudio" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted movie file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99880.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99880
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 912. CVE-2017-7009

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "IOUSBFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 913. CVE-2017-7010

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:iphone_os, apple:mac_os_x, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. iCloud before 6.2.2 on Windows is affected. iTunes before 12.6.2 on Windows is affected. tvOS before 10.2.2 is affected. The issue involves the "libxml2" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted XML file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99889.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99889
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 914. CVE-2017-7013

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:watchos, apple:iphone_os, apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. iCloud before 6.2.2 on Windows is affected. iTunes before 12.6.2 on Windows is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "libxml2" component. It allows remote attackers to obtain sensitive information or cause a denial of service (out-of-bounds read and application crash) via a crafted XML file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99879.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99879
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 915. CVE-2017-7014

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 916. CVE-2017-7015

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Audio" component. It allows remote attackers to obtain sensitive information from process memory or cause a denial of service (memory corruption) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 917. CVE-2017-7016

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "afclip" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 918. CVE-2017-7017

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 919. CVE-2017-7021

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "AppleGraphicsPowerManagement" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 920. CVE-2017-7022

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:safari, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 921. CVE-2017-7023

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:safari, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 922. CVE-2017-7024

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:safari, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 923. CVE-2017-7025

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows, apple:itunes, apple:safari, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 924. CVE-2017-7026

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 925. CVE-2017-7027

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 926. CVE-2017-7028

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 927. CVE-2017-7029

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 928. CVE-2017-7031

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Foundation" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 929. CVE-2017-7032

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "kext tools" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 930. CVE-2017-7033

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "afclip" component. It allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted audio file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 931. CVE-2017-7035

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 932. CVE-2017-7036

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 933. CVE-2017-7044

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 934. CVE-2017-7045

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Intel Graphics Driver" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 935. CVE-2017-7047

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "libxpc" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 936. CVE-2017-7050

**严重程度 / Severity**: HIGH | CVSS: 8.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 937. CVE-2017-7051

**严重程度 / Severity**: HIGH | CVSS: 8.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 938. CVE-2017-7054

**严重程度 / Severity**: HIGH | CVSS: 8.0
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Bluetooth" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 939. CVE-2017-7062

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Contacts" component. A buffer overflow allows remote attackers to execute arbitrary code or cause a denial of service (application crash).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 940. CVE-2017-7067

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.12.6 is affected. The issue involves the "Kernel" component. It allows attackers to bypass intended memory-read restrictions via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99882.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951
- https://support.apple.com/HT207922
- http://www.securityfocus.com/bid/99882
- http://www.securitytracker.com/id/1038951

---

#### 941. CVE-2017-7068

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "libarchive" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted archive file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 942. CVE-2017-7069

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 10.3.3 is affected. macOS before 10.12.6 is affected. tvOS before 10.2.2 is affected. watchOS before 3.2.3 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99883.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99883
- http://www.securitytracker.com/id/1038950
- https://support.apple.com/HT207922
- https://support.apple.com/HT207923
- https://support.apple.com/HT207924

---

#### 943. CVE-2017-8665

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:xamarin.ios, apple:macos

**漏洞描述 / Description**:
The Xamarin.iOS update component on systems running macOS allows an attacker to run arbitrary code as root, aka "Xamarin.iOS Elevation Of Privilege Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100308.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100308
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8665
- https://www.exploit-db.com/exploits/42454/
- http://www.securityfocus.com/bid/100308
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8665

---

#### 944. CVE-2017-7074

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.13 is affected. The issue involves the "AppSandbox" component. It allows attackers to cause a denial of service via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100993.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208144
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427

---

#### 945. CVE-2017-7077

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.13 is affected. The issue involves the "IOFireWireFamily" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100993.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208144
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427

---

#### 946. CVE-2017-7078

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: apple:mac_os_x, apple:iphone_os

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 11 is affected. macOS before 10.13 is affected. The issue involves the "Mail Drafts" component. It allows remote attackers to obtain sensitive information by reading unintended cleartext transmissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100999.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100999
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208112
- https://support.apple.com/HT208144
- http://www.securityfocus.com/bid/100999

---

#### 947. CVE-2017-7080

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 11 is affected. macOS before 10.13 is affected. tvOS before 11 is affected. watchOS before 4 is affected. The issue involves the "Security" component. It allows remote attackers to bypass intended certificate-trust restrictions via a revoked X.509 certificate.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100992.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100992
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208112
- https://support.apple.com/HT208113
- https://support.apple.com/HT208115

---

#### 948. CVE-2017-7082

**严重程度 / Severity**: LOW | CVSS: 2.4
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.13 is affected. The issue involves the "Screen Lock" component. It allows physically proximate attackers to read Application Firewall prompts.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100993.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208144
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427

---

#### 949. CVE-2017-7083

**严重程度 / Severity**: MEDIUM | CVSS: 4.9
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 11 is affected. macOS before 10.13 is affected. tvOS before 11 is affected. watchOS before 4 is affected. The issue involves the "CFNetwork Proxies" component. It allows remote attackers to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100992.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100992
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208112
- https://support.apple.com/HT208113
- https://support.apple.com/HT208115

---

#### 950. CVE-2017-7084

**严重程度 / Severity**: LOW | CVSS: 3.7
**受影响产品 / Affected Products**: apple:mac_os_x

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. macOS before 10.13 is affected. The issue involves the "Application Firewall" component. It allows remote attackers to bypass intended settings in opportunistic circumstances by leveraging incorrect handling of a denied setting after an upgrade.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100993.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208144
- http://www.securityfocus.com/bid/100993
- http://www.securitytracker.com/id/1039427

---

#### 951. CVE-2017-7086

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 11 is affected. macOS before 10.13 is affected. tvOS before 11 is affected. watchOS before 4 is affected. The issue involves the "libc" component. It allows remote attackers to cause a denial of service (resource consumption) via a crafted string that is mishandled by the glob function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100990.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100990
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208112
- https://support.apple.com/HT208113
- https://support.apple.com/HT208115

---

#### 952. CVE-2017-7114

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: apple:mac_os_x, apple:watchos, apple:iphone_os, apple:tvos

**漏洞描述 / Description**:
An issue was discovered in certain Apple products. iOS before 11 is affected. macOS before 10.13 is affected. tvOS before 11 is affected. watchOS before 4 is affected. The issue involves the "Kernel" component. It allows attackers to execute arbitrary code in a privileged context or cause a denial of service (memory corruption) via a crafted app.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/100990.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100990
- http://www.securitytracker.com/id/1039427
- https://support.apple.com/HT208112
- https://support.apple.com/HT208113
- https://support.apple.com/HT208115

---
