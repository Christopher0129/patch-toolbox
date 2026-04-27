# Windows 系统漏洞知识库 | Windows System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 306**

> 技术细节（漏洞描述、补丁信息等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, patch info) remain in original language for accuracy; structural text is bilingual.

---

#### 1. CVE-1999-0280

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Remote command execution in Microsoft Internet Explorer using .lnk and .url files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0280.

**参考链接 / References**:
- N/A

---

#### 2. CVE-1999-0012

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: netscape:fasttrack_server, microsoft:personal_web_server, netscape:enterprise_server, microsoft:frontpage, microsoft:internet_information_server

**漏洞描述 / Description**:
Some web servers under Microsoft Windows allow remote attackers to bypass access restrictions for files with long file names.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012.

**参考链接 / References**:
- N/A

---

#### 3. CVE-1999-1556

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 6.5 uses weak encryption for the password for the SQLExecutiveCmdExec account and stores it in an accessible portion of the registry, which could allow local users to gain privileges by reading and decrypting the CmdExecAccount value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=90222453431645&w=2.

**参考链接 / References**:
- N/A

---

#### 4. CVE-1999-0288

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The WINS server in Microsoft Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service (process termination) via invalid UDP frames to port 137 (NETBIOS Name Service), as demonstrated via a flood of random packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://safenetworks.com/Windows/wins.html.

**参考链接 / References**:
- N/A

---

#### 5. CVE-1999-1291

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_nt

**漏洞描述 / Description**:
TCP/IP implementation in Microsoft Windows 95, Windows NT 4.0, and possibly others, allows remote attackers to reset connections by forcing a reset (RST) via a PSH ACK or other means, obtaining the target's last sequence number from the resulting packet, then spoofing a reset to the target.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/10789.

**参考链接 / References**:
- N/A

---

#### 6. CVE-1999-0364

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:access, fms_inc.:total_vb_sourcebook

**漏洞描述 / Description**:
Microsoft Access 97 stores a database password as plaintext in a foreign mdb, allowing access to data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91816470220259&w=2.

**参考链接 / References**:
- N/A

---

#### 7. CVE-1999-1544

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Buffer overflow in FTP server in Microsoft IIS 3.0 and 4.0 allows local and sometimes remote attackers to cause a denial of service via a long NLST (ls) command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91722115016183&w=2.

**参考链接 / References**:
- N/A

---

#### 8. CVE-1999-0379

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:backoffice_resource_kit

**漏洞描述 / Description**:
Microsoft Taskpads allows remote web sites to execute commands on the visiting user's machine via certain methods that are marked as Safe for Scripting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1019.

**参考链接 / References**:
- N/A

---

#### 9. CVE-1999-0386

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:personal_web_server, microsoft:frontpage

**漏洞描述 / Description**:
Microsoft Personal Web Server and FrontPage Personal Web Server in some Windows systems allows a remote attacker to read files on the server by using a nonstandard URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/111.

**参考链接 / References**:
- N/A

---

#### 10. CVE-1999-0419

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
When the Microsoft SMTP service attempts to send a message to a server and receives a 4xx error code, it quickly and repeatedly attempts to redeliver the message, causing a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419.

**参考链接 / References**:
- N/A

---

#### 11. CVE-1999-0468

**严重程度 / Severity**: HIGH | CVSS: 8.2
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.0 allows a remote server to read arbitrary files on the client's file system using the Microsoft Scriptlet Component.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012.

**参考链接 / References**:
- N/A

---

#### 12. CVE-1999-1097

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting 2.1 allows one client to read the contents of another client's clipboard via a CTRL-C in the chat box when the box is empty.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92586457816446&w=2.

**参考链接 / References**:
- N/A

---

#### 13. CVE-1999-0717

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:excel, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_nt

**漏洞描述 / Description**:
A remote attacker can disable the virus warning mechanism in Microsoft Excel 97.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304.

**参考链接 / References**:
- N/A

---

#### 14. CVE-1999-1033

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook Express before 4.72.3612.1700 allows a malicious user to send a message that contains a .., which can inadvertently cause Outlook to re-enter POP3 command mode and cause the POP3 session to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92647407427342&w=2.

**参考链接 / References**:
- N/A

---

#### 15. CVE-1999-1520

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
A configuration problem in the Ad Server Sample directory (AdSamples) in Microsoft Site Server 3.0 allows an attacker to obtain the SITE.CSC file, which exposes sensitive SQL database information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92647407227303&w=2.

**参考链接 / References**:
- N/A

---

#### 16. CVE-1999-1368

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: broadcom:inoculateit

**漏洞描述 / Description**:
AV Option for MS Exchange Server option for InoculateIT 4.53, and possibly other versions, only scans the Inbox folder tree of a Microsoft Exchange server, which could allow viruses to escape detection if a user's rules cause the message to be moved to a different mailbox.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=92652152723629&w=2.

**参考链接 / References**:
- N/A

---

#### 17. CVE-1999-1164

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook client allows remote attackers to cause a denial of service by sending multiple email messages with the same X-UIDL headers, which causes Outlook to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93041631215856&w=2.

**参考链接 / References**:
- N/A

---

#### 18. CVE-1999-1011

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:site_server, microsoft:internet_information_server, microsoft:data_access_components, microsoft:index_server

**漏洞描述 / Description**:
The Remote Data Service (RDS) DataFactory component of Microsoft Data Access Components (MDAC) in IIS 3.x and 4.x exposes unsafe methods, which allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/j-054.shtml.

**参考链接 / References**:
- N/A

---

#### 19. CVE-2000-0323

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:jet

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to modify text files via a database query, aka the "Text I-ISAM" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org.

**参考链接 / References**:
- N/A

---

#### 20. CVE-1999-0700

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Dialer (dialer.exe), via a malformed dialer entry in the dialer.ini file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185.

**参考链接 / References**:
- N/A

---

#### 21. CVE-1999-0682

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange 5.5 allows a remote attacker to relay email (i.e. spam) using encapsulated SMTP addresses, even if the anti-relaying features are enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927.

**参考链接 / References**:
- N/A

---

#### 22. CVE-1999-0749

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Buffer overflow in Microsoft Telnet client in Windows 95 and Windows 98 via a malformed Telnet argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/586.

**参考链接 / References**:
- N/A

---

#### 23. CVE-2000-0325

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:jet

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to execute commands via a database query, aka the "VBA Shell" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/548.

**参考链接 / References**:
- N/A

---

#### 24. CVE-1999-1052

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
Microsoft FrontPage stores form results in a default location in /_private/form_results.txt, which is world-readable and accessible in the document root, which allows remote attackers to read possibly sensitive information submitted by other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93582550911564&w=2.

**参考链接 / References**:
- N/A

---

#### 25. CVE-1999-1016

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:internet_explorer, qualcomm:eudora, microsoft:frontpage

**漏洞描述 / Description**:
Microsoft HTML control as used in (1) Internet Explorer 5.0, (2) FrontPage Express, (3) Outlook Express 5, and (4) Eudora, and possibly others, allows remote malicious web site or HTML emails to cause a denial of service (100% CPU consumption) via large HTML form fields such as text inputs in a table cell.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=93578772920970&w=2.

**参考链接 / References**:
- N/A

---

#### 26. CVE-1999-0910

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commercial_internet_system, microsoft:site_server, microsoft:site_server_commerce

**漏洞描述 / Description**:
Microsoft Site Server and Commercial Internet System (MCIS) do not set an expiration for a cookie, which could then be cached by a proxy and inadvertently used by a different user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/625.

**参考链接 / References**:
- N/A

---

#### 27. CVE-1999-0794

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:office, microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel does not warn a user when a macro is present in a Symbolic Link (SYLK) format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900.

**参考链接 / References**:
- N/A

---

#### 28. CVE-1999-0766

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346.

**参考链接 / References**:
- N/A

---

#### 29. CVE-2000-0327

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93993545118416&w=2.

**参考链接 / References**:
- N/A

---

#### 30. CVE-2000-0329

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:outlook, microsoft:outlook_express, microsoft:ie

**漏洞描述 / Description**:
A Microsoft ActiveX control allows a remote attacker to execute a malicious cabinet file via an attachment and an embedded script in an HTML mail, aka the "Active Setup Control" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048.

**参考链接 / References**:
- N/A

---

#### 31. CVE-2000-0073

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft Rich Text Format (RTF) reader allows attackers to cause a denial of service via a malformed control word.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973.

**参考链接 / References**:
- N/A

---

#### 32. CVE-1999-0999

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL 7.0 server allows a remote attacker to cause a denial of service via a malformed TDS packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749.

**参考链接 / References**:
- N/A

---

#### 33. CVE-1999-0993

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Modifications to ACLs (Access Control Lists) in Microsoft Exchange  5.5 do not take effect until the directory store cache is refreshed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993.

**参考链接 / References**:
- N/A

---

#### 34. CVE-1999-1043

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 and 5.0 does not properly handle (1) malformed NNTP data, or (2) malformed SMTP data, which allows remote attackers to cause a denial of service (application error).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007.

**参考链接 / References**:
- N/A

---

#### 35. CVE-1999-1055

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 does not warn the user before executing worksheet functions, which could allow attackers to execute arbitrary commands by using the CALL function to execute a malicious DLL, aka the Excel "CALL Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/179.

**参考链接 / References**:
- N/A

---

#### 36. CVE-1999-1246

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
Direct Mailer feature in Microsoft Site Server 3.0 saves user domain names and passwords in plaintext in the TMLBQueue network share, which has insecure default permissions, allowing remote attackers to read the passwords and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q229/9/72.asp.

**参考链接 / References**:
- N/A

---

#### 37. CVE-1999-1259

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
Microsoft Office 98, Macintosh Edition, does not properly initialize the disk space used by Office 98 files and effectively inserts data from previously deleted files into the Office file, which could allow attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q189/5/29.asp.

**参考链接 / References**:
- N/A

---

#### 38. CVE-1999-1279

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sna_server

**漏洞描述 / Description**:
An interaction between the AS/400 shared folders feature and Microsoft SNA Server 3.0 and earlier allows users to view each other's folders when the users share the same Local APPC LU.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q138/0/01.asp.

**参考链接 / References**:
- N/A

---

#### 39. CVE-1999-1591

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:visual_interdev

**漏洞描述 / Description**:
Microsoft Internet Information Services (IIS) server 4.0 SP4, without certain hotfixes released for SP4, does not require authentication credentials under certain conditions, which allows remote attackers to bypass authentication requirements, as demonstrated by connecting via Microsoft Visual InterDev 6.0.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html.

**参考链接 / References**:
- N/A

---

#### 40. CVE-2000-0053

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commercial_internet_system

**漏洞描述 / Description**:
Microsoft Commercial Internet System (MCIS) IMAP server allows remote attackers to cause a denial of service via a malformed IMAP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731.

**参考链接 / References**:
- N/A

---

#### 41. CVE-2000-0097

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
The WebHits ISAPI filter in Microsoft Index Server allows remote attackers to read arbitrary files, aka the "Malformed Hit-Highlighting Argument" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1210.

**参考链接 / References**:
- N/A

---

#### 42. CVE-2000-0098

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to determine the real path for a web directory via a request to an Internet Data Query file that does not exist.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006.

**参考链接 / References**:
- N/A

---

#### 43. CVE-2000-0132

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Java Virtual Machine allows remote attackers to read files via the getSystemResourceAsStream function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/957.

**参考链接 / References**:
- N/A

---

#### 44. CVE-2000-0089

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The rdisk utility in Microsoft Terminal Server Edition and Windows NT 4.0 stores registry hive information in a temporary file with permissions that allow local users to read it, aka the "RDISK Registry Enumeration File" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108.

**参考链接 / References**:
- N/A

---

#### 45. CVE-2000-0161

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
Sample web sites on Microsoft Site Server 3.0 Commerce Edition do not validate an identification number, which allows remote attackers to execute SQL commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/994.

**参考链接 / References**:
- N/A

---

#### 46. CVE-2000-0162

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:visual_studio, microsoft:internet_explorer, microsoft:ie

**漏洞描述 / Description**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011.

**参考链接 / References**:
- N/A

---

#### 47. CVE-2000-0160

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:outlook, microsoft:ie

**漏洞描述 / Description**:
The Microsoft Active Setup ActiveX component in Internet Explorer 4.x and 5.x allows a remote attacker to install software components without prompting the user by stating that the software's manufacturer is Microsoft.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com.

**参考链接 / References**:
- N/A

---

#### 48. CVE-2000-0216

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_messaging, microsoft:outlook, microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft email clients in Outlook, Exchange, and Windows Messaging automatically respond to Read Receipt and Delivery Receipt tags, which could allow an attacker to flood a mail system with responses by forging a Read Receipt request that is redirected to a large distribution list.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html.

**参考链接 / References**:
- N/A

---

#### 49. CVE-2000-0201

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The window.showHelp() method in Internet Explorer 5.x does not restrict HTML help files (.chm) to be executed from the local host, which allows remote attackers to execute arbitrary commands via Microsoft Networking.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1033.

**参考链接 / References**:
- N/A

---

#### 50. CVE-2000-0168

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98se, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Windows 9x operating systems allow an attacker to cause a denial of service via a pathname that includes file device names, aka the "DOS Device in Path Name" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1043.

**参考链接 / References**:
- N/A

---

#### 51. CVE-2000-0200

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:home_publishing, microsoft:clip_art, microsoft:greetings

**漏洞描述 / Description**:
Buffer overflow in Microsoft Clip Art Gallery allows remote attackers to cause a denial of service or execute commands via a malformed CIL (clip art library) file, aka the "Clip Art Buffer Overrun" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1034.

**参考链接 / References**:
- N/A

---

#### 52. CVE-2000-0202

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and Microsoft Data Engine (MSDE) 1.0 allow remote attackers to gain privileges via a malformed Select statement in an SQL query.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1041.

**参考链接 / References**:
- N/A

---

#### 53. CVE-2000-0199

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
When a new SQL Server is registered in Enterprise Manager for Microsoft SQL Server 7.0 and the "Always prompt for login name and password" option is not set, then the Enterprise Manager uses weak encryption to store the login ID and password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1055.

**参考链接 / References**:
- N/A

---

#### 54. CVE-2000-0228

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_rights_manager

**漏洞描述 / Description**:
Microsoft Windows Media License Manager allows remote attackers to cause a denial of service by sending a malformed request that causes the manager to halt, aka the "Malformed Media License Request" Vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1058.

**参考链接 / References**:
- N/A

---

#### 55. CVE-2000-0232

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:terminal_server, microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft TCP/IP Printing Services, aka Print Services for Unix, allows an attacker to cause a denial of service via a malformed TCP/IP print request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html.

**参考链接 / References**:
- N/A

---

#### 56. CVE-2000-0302

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to view the source code of ASP files by appending a %20 to the filename in the CiWebHitsFile argument to the null.htw URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=95453598317340&w=2.

**参考链接 / References**:
- N/A

---

#### 57. CVE-2000-0277

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 does not warn the user when executing Excel Macro Language (XLM) macros in external text files, which could allow an attacker to execute a macro virus, aka the "XLM Text Macro" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1272.

**参考链接 / References**:
- N/A

---

#### 58. CVE-2000-0260

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:frontpage, microsoft:visual_interdev

**漏洞描述 / Description**:
Buffer overflow in the dvwssr.dll DLL in Microsoft Visual Interdev 1.0 allows users to cause a denial of service or execute commands, aka the "Link View Server-Side Component" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/282.

**参考链接 / References**:
- N/A

---

#### 59. CVE-2000-1218

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: microsoft:windows_98se, microsoft:windows_xp, microsoft:windows_98, microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The default configuration for the domain name resolver for Microsoft Windows 98, NT 4.0, 2000, and XP sets the QueryIpMatching parameter to 0, which causes Windows to accept DNS updates from hosts that it did not query, which allows remote attackers to poison the DNS cache.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/458659.

**参考链接 / References**:
- N/A

---

#### 60. CVE-2000-0331

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:terminal_server, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft command processor (CMD.EXE) for Windows NT and Windows 2000 allows a local user to cause a denial of service via a long environment variable, aka the "Malformed Environment Variable" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html.

**参考链接 / References**:
- N/A

---

#### 61. CVE-2000-0304

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS 4.0 and 5.0 with the IISADMPWD virtual directory installed allows a remote attacker to cause a denial of service via a malformed request to the inetinfo.exe program, aka the "Undelimited .HTR Request" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1191.

**参考链接 / References**:
- N/A

---

#### 62. CVE-2000-0400

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The Microsoft Active Movie ActiveX Control in Internet Explorer 5 does not restrict which file types can be downloaded, which allows an attacker to download any type of file to a user's system by encoding it within an email message or news post.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=95868514521257&w=2.

**参考链接 / References**:
- N/A

---

#### 63. CVE-2000-0402

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
The Mixed Mode authentication capability in Microsoft SQL Server 7.0 stores the System Administrator (sa) account in plaintext in a log file which is readable by any user, aka the "SQL Server 7.0 Service Pack Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=263968.

**参考链接 / References**:
- N/A

---

#### 64. CVE-2000-0485

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server allows local users to obtain database passwords via the Data Transformation Service (DTS) package Properties dialog, aka the "DTS Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/62771.

**参考链接 / References**:
- N/A

---

#### 65. CVE-2000-0495

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
Microsoft Windows Media Encoder allows remote attackers to cause a denial of service via a malformed request, aka the "Malformed Windows Media Encoder Request" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1282.

**参考链接 / References**:
- N/A

---

#### 66. CVE-2000-0524

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Outlook and Outlook Express allow remote attackers to cause a denial of service by sending email messages with blank fields such as BCC, Reply-To, Return-Path, or From.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html.

**参考链接 / References**:
- N/A

---

#### 67. CVE-2000-0596

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.x does not warn a user before opening a Microsoft Access database file that is referenced within ActiveX OBJECT tags in an HTML document, which could allow remote attackers to execute arbitrary commands, aka the "IE Script" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-16.html.

**参考链接 / References**:
- N/A

---

#### 68. CVE-2000-0597

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Microsoft Office 2000 (Excel and PowerPoint) and PowerPoint 97 are marked as safe for scripting, which allows remote attackers to force Internet Explorer or some email clients to save files to arbitrary locations via the Visual Basic for Applications (VBA) SaveAs function, aka the "Office HTML Script" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1399.

**参考链接 / References**:
- N/A

---

#### 69. CVE-2000-0603

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 allows a local user to bypass permissions for stored procedures by referencing them via a temporary stored procedure, aka the "Stored Procedure Permissions" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1444.

**参考链接 / References**:
- N/A

---

#### 70. CVE-2000-0654

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft Enterprise Manager allows local users to obtain database passwords via the Data Transformation Service (DTS) package Registered Servers Dialog dialog, aka a variant of the "DTS Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1466.

**参考链接 / References**:
- N/A

---

#### 71. CVE-2000-0662

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.x and Microsoft Outlook allows remote attackers to read arbitrary files by redirecting the contents of an IFRAME using the DHTML Edit Control (DHTMLED).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1474.

**参考链接 / References**:
- N/A

---

#### 72. CVE-2000-0567

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Buffer overflow in Microsoft Outlook and Outlook Express allows remote attackers to execute arbitrary commands via a long Date field in an email header, aka the "Malformed E-mail Header" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1481.

**参考链接 / References**:
- N/A

---

#### 73. CVE-2000-0621

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 98 and 2000, and Outlook Express 4.0x and 5.0x, allow remote attackers to read files on the client's system via a malformed HTML message that stores files outside of the cache, aka the "Cache Bypass" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-14.html.

**参考链接 / References**:
- N/A

---

#### 74. CVE-2000-0653

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook Express allows remote attackers to monitor a user's email by creating a persistent browser link to the Outlook Express windows, aka the "Persistent Mail-Browser Link" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1502.

**参考链接 / References**:
- N/A

---

#### 75. CVE-2000-0637

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 allows an attacker to execute arbitrary commands by specifying a malicious .dll using the Register.ID function, aka the "Excel REGISTER.ID Function" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1451.

**参考链接 / References**:
- N/A

---

#### 76. CVE-2000-1079

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_nt, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Interactions between the CIFS Browser Protocol and NetBIOS as implemented in Microsoft Windows 95, 98, NT, and 2000 allow remote attackers to modify dynamic NetBIOS name cache entries via a spoofed Browse Frame Request in a unicast or UDP broadcast datagram.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0116.html.

**参考链接 / References**:
- N/A

---

#### 77. CVE-2000-0563

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_runtime_for_java

**漏洞描述 / Description**:
The URLConnection function in MacOS Runtime Java (MRJ) 2.1 and earlier and the Microsoft virtual machine (VM) for MacOS allows a malicious web site operator to connect to arbitrary hosts using a HTTP redirection, in violation of the Java security model.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0056.html.

**参考链接 / References**:
- N/A

---

#### 78. CVE-2000-0709

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to cause a denial of service in some components by requesting a URL whose name includes a standard DOS device name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html.

**参考链接 / References**:
- N/A

---

#### 79. CVE-2000-0710

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to determine the physical path of the server components by requesting an invalid URL whose name includes a standard DOS device name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html.

**参考链接 / References**:
- N/A

---

#### 80. CVE-2000-0742

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
The IPX protocol implementation in Microsoft Windows 95 and 98 allows remote attackers to cause a denial of service by sending a ping packet with a source IP address that is a broadcast address, aka the "Malformed IPX Ping Packet" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1544.

**参考链接 / References**:
- N/A

---

#### 81. CVE-2000-0753

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
The Microsoft Outlook mail client identifies the physical path of the sender's machine within a winmail.dat attachment to Rich Text Format (RTF) files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/201422.

**参考链接 / References**:
- N/A

---

#### 82. CVE-2000-0756

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 2000 does not properly process long or malformed fields in vCard (.vcf) files, which allows attackers to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1633.

**参考链接 / References**:
- N/A

---

#### 83. CVE-2000-0765

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:word, microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Buffer overflow in the HTML interpreter in Microsoft Office 2000 allows an attacker to execute arbitrary commands via a long embedded object tag, aka the "Microsoft Office HTML Object Tag" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1561.

**参考链接 / References**:
- N/A

---

#### 84. CVE-2000-0771

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to cause a denial of service by corrupting the local security policy via malformed RPC traffic, aka the "Local Security Policy Corruption" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1613.

**参考链接 / References**:
- N/A

---

#### 85. CVE-2000-0777

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:money

**漏洞描述 / Description**:
The password protection feature of Microsoft Money can store the password in plaintext, which allows attackers with physical access to the system to obtain the password, aka the "Money Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1615.

**参考链接 / References**:
- N/A

---

#### 86. CVE-2000-0788

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:access, microsoft:word

**漏洞描述 / Description**:
The Mail Merge tool in Microsoft Word does not prompt the user before executing Visual Basic (VBA) scripts in an Access database, which could allow an attacker to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1566.

**参考链接 / References**:
- N/A

---

#### 87. CVE-2000-0790

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_98se, microsoft:windows_2000

**漏洞描述 / Description**:
The web-based folder display capability in Microsoft Internet Explorer 5.5 on Windows 98 allows local users to insert Trojan horse programs by modifying the Folder.htt file and using the InvokeVerb method in the ShellDefView ActiveX control to specify a default execute option for the first file that is listed in the folder.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1571.

**参考链接 / References**:
- N/A

---

#### 88. CVE-2000-0849

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
Race condition in Microsoft Windows Media server allows remote attackers to cause a denial of service in the Windows Media Unicast Service via a malformed request, aka the "Unicast Service Race Condition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1655.

**参考链接 / References**:
- N/A

---

#### 89. CVE-2000-0854

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
When a Microsoft Office 2000 document is launched, the directory of that document is first used to locate DLL's such as riched20.dll and msi.dll, which could allow an attacker to execute arbitrary commands by inserting a Trojan Horse DLL into the same directory as the document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-09/0277.html.

**参考链接 / References**:
- N/A

---

#### 90. CVE-2000-0858

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:internet_information_server

**漏洞描述 / Description**:
Vulnerability in Microsoft Windows NT 4.0 allows remote attackers to cause a denial of service in IIS by sending it a series of malformed requests which cause INETINFO.EXE to fail, aka the "Invalid URL" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html.

**参考链接 / References**:
- N/A

---

#### 91. CVE-2000-1217

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 before Service Pack 2 (SP2), when running in a non-Windows 2000 domain and using NTLM authentication, and when credentials of an account are locally cached, allows local users to bypass account lockout policies and make an unlimited number of login attempts, aka the "Domain Account Lockout" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/818496.

**参考链接 / References**:
- N/A

---

#### 92. CVE-2000-1006

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 does not properly handle a MIME header with a blank charset specified, which allows remote attackers to cause a denial of service via a charset="" command, aka the "Malformed MIME Header" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1869.

**参考链接 / References**:
- N/A

---

#### 93. CVE-2000-1061

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) in Internet Explorer 4.x and 5.x allows an unsigned applet to create and use ActiveX controls, which allows a remote attacker to bypass Internet Explorer's security settings and execute arbitrary commands via a malicious web page or email, aka the "Microsoft VM ActiveX Component" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075.

**参考链接 / References**:
- N/A

---

#### 94. CVE-2000-0817

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:network_monitor

**漏洞描述 / Description**:
Buffer overflow in the HTTP protocol parser for Microsoft Network Monitor (Netmon) allows remote attackers to execute arbitrary commands via malformed data, aka the "Netmon Protocol Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://xforce.iss.net/alerts/index.php.

**参考链接 / References**:
- N/A

---

#### 95. CVE-2000-0885

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:systems_management_server

**漏洞描述 / Description**:
Buffer overflows in Microsoft Network Monitor (Netmon) allow remote attackers to execute arbitrary commands via a long Browser Name in a CIFS Browse Frame, a long SNMP community name, or a long username or filename in an SMB session, aka the "Netmon Protocol Parsing" vulnerability.  NOTE: It is highly likely that this candidate will be split into multiple candidates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083.

**参考链接 / References**:
- N/A

---

#### 96. CVE-2000-0929

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 allows attackers to cause a denial of service in RTF-enabled email clients via an embedded OCX control that is not closed properly, aka the "OCX Attachment" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97024839222747&w=2.

**参考链接 / References**:
- N/A

---

#### 97. CVE-2000-0942

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:indexing_service

**漏洞描述 / Description**:
The CiWebHitsFile component in Microsoft Indexing Services for Windows 2000 allows remote attackers to conduct a cross site scripting (CSS) attack via a CiRestriction parameter in a .htw request, aka the "Indexing Services Cross Site Scripting" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/141903.

**参考链接 / References**:
- N/A

---

#### 98. CVE-2000-0980

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98se, microsoft:windows_me, microsoft:windows_98

**漏洞描述 / Description**:
NMPI (Name Management Protocol on IPX) listener in Microsoft NWLink does not properly filter packets from a broadcast address, which allows remote attackers to cause a broadcast storm and flood the network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1781.

**参考链接 / References**:
- N/A

---

#### 99. CVE-2000-0983

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service (CPU utilization) via a sequence of null bytes to the NetMeeting port, aka the "NetMeeting Desktop Sharing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ273854.

**参考链接 / References**:
- N/A

---

#### 100. CVE-2000-1081

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_displayparamstmt function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

**参考链接 / References**:
- N/A

---

#### 101. CVE-2000-1082

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_enumresultset function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

**参考链接 / References**:
- N/A

---

#### 102. CVE-2000-1083

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_showcolv function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

**参考链接 / References**:
- N/A

---

#### 103. CVE-2000-1084

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_updatecolvbm function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

**参考链接 / References**:
- N/A

---

#### 104. CVE-2000-1085

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_peekqueue function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

**参考链接 / References**:
- N/A

---

#### 105. CVE-2000-1086

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_printstatements function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

**参考链接 / References**:
- N/A

---

#### 106. CVE-2000-1087

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_proxiedmetadata function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

**参考链接 / References**:
- N/A

---

#### 107. CVE-2000-1088

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_SetSQLSecurity function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

**参考链接 / References**:
- N/A

---

#### 108. CVE-2000-1089

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Book Service allows local users to execute arbitrary commands, aka the "Phone Book Service Buffer Overflow" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2048.

**参考链接 / References**:
- N/A

---

#### 109. CVE-2000-1112

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 executes scripts in custom skin (.WMS) files, which could allow remote attackers to gain privileges via a skin that contains a malicious script, aka the ".WMS Script Execution" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1976.

**参考链接 / References**:
- N/A

---

#### 110. CVE-2000-1113

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player allows remote attackers to execute arbitrary commands via a malformed Active Stream Redirector (.ASX) file, aka the ".ASX Buffer Overrun" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2000/a112300-1.txt.

**参考链接 / References**:
- N/A

---

#### 111. CVE-2000-1139

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
The installation of Microsoft Exchange 2000 before Rev. A creates a user account with a known password, which could allow attackers to gain privileges, aka the "Exchange User Account" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1958.

**参考链接 / References**:
- N/A

---

#### 112. CVE-2000-1090

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS for Far East editions 4.0 and 5.0 allows remote attackers to read source code for parsed pages via a malformed URL that uses the lead-byte of a double-byte character.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.nsfocus.com/english/homepage/sa_08.htm.

**参考链接 / References**:
- N/A

---

#### 113. CVE-2001-0003

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:office, microsoft:windows_me

**漏洞描述 / Description**:
Web Extender Client (WEC) in Microsoft Office 2000, Windows 2000, and Windows Me does not properly process Internet Explorer security settings for NTLM authentication, which allows attackers to obtain NTLM credentials and possibly obtain the password, aka the "Web Client NTLM Authentication" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2199.

**参考链接 / References**:
- N/A

---

#### 114. CVE-2001-0005

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: microsoft:powerpoint

**漏洞描述 / Description**:
Buffer overflow in the parsing mechanism of the file loader in Microsoft PowerPoint 2000 allows attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2001/a012301-1.txt.

**参考链接 / References**:
- N/A

---

#### 115. CVE-2001-0048

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The "Configure Your Server" tool in Microsoft 2000 domain controllers installs a blank password for the Directory Service Restore Mode, which allows attackers with physical access to the controller to install malicious programs, aka the "Directory Service Restore Mode Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2133.

**参考链接 / References**:
- N/A

---

#### 116. CVE-2001-0047

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The default permissions for the MTS Package Administration registry key in Windows NT 4.0 allows local users to install or modify arbitrary Microsoft Transaction Server (MTS) packages and gain privileges, aka one of the "Registry Permissions" vulnerabilities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2065.

**参考链接 / References**:
- N/A

---

#### 117. CVE-1999-0681

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:personal_web_server, microsoft:frontpage

**漏洞描述 / Description**:
Buffer overflow in Microsoft FrontPage Server Extensions (PWS) 3.0.2.926 on Windows 95, and possibly other versions, allows remote attackers to cause a denial of service via a long URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html.

**参考链接 / References**:
- N/A

---

#### 118. CVE-1999-0945

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Service (IMS) for Microsoft Exchange 5.5 and 5.0 allows remote attackers to conduct a denial of service via AUTH or AUTHINFO commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174.

**参考链接 / References**:
- N/A

---

#### 119. CVE-2001-1450

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.0 through 6.0 allows attackers to cause a denial of service (browser crash) via a crafted FTP URL such as "/.#./".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html.

**参考链接 / References**:
- N/A

---

#### 120. CVE-2001-1326

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: qualcomm:eudora

**漏洞描述 / Description**:
Eudora 5.1 allows remote attackers to execute arbitrary code when the "Use Microsoft Viewer" option is enabled and the "allow executables in HTML content" option is disabled, via an HTML email with a form that is activated from an image that the attacker spoofs as a link, which causes the user to execute the form and access embedded attachments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/187128.

**参考链接 / References**:
- N/A

---

#### 121. CVE-2001-0146

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:internet_information_services

**漏洞描述 / Description**:
IIS 5.0 and Microsoft Exchange 2000 allow remote attackers to cause a denial of service (memory allocation error) by repeatedly sending a series of specially formatted URL's.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/796584.

**参考链接 / References**:
- N/A

---

#### 122. CVE-2001-0261

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 Encrypted File System does not properly destroy backups of files that are encrypted, which allows a local attacker to recover the text of encrypted files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97992179925715&w=2.

**参考链接 / References**:
- N/A

---

#### 123. CVE-2001-1088

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook 8.5 and earlier, and Outlook Express 5 and earlier, with the "Automatically put people I reply to in my address book" option enabled, do not notify the user when the "Reply-To" address is different than the "From" address, which could allow an untrusted remote attacker to spoof legitimate addresses and intercept email from the client that is intended for another user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241.

**参考链接 / References**:
- N/A

---

#### 124. CVE-2001-0237

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Memory leak in Microsoft 2000 domain controller allows remote attackers to cause a denial of service by repeatedly connecting to the Kerberos service and then disconnecting without sending any data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-079.shtml.

**参考链接 / References**:
- N/A

---

#### 125. CVE-2001-0240

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word before Word 2002 allows attackers to automatically execute macros without warning the user via a Rich Text Format (RTF) document that links to a template with the embedded macro.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2753.

**参考链接 / References**:
- N/A

---

#### 126. CVE-2001-0242

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflows in Microsoft Windows Media Player 7 and earlier allow remote attackers to execute arbitrary commands via (1) a long version tag in an .ASX file, or (2) a long banner tag, a variant of the ".ASX Buffer Overrun" vulnerability as discussed in MS:MS00-090.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/187528.

**参考链接 / References**:
- N/A

---

#### 127. CVE-2001-0244

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Buffer overflow in Microsoft Index Server 2.0 allows remote attackers to execute arbitrary commands via a long search parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2709.

**参考链接 / References**:
- N/A

---

#### 128. CVE-2001-0245

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server, microsoft:indexing_service

**漏洞描述 / Description**:
Microsoft Index Server 2.0 in Windows NT 4.0, and Indexing Service in Windows 2000, allows remote attackers to read server-side include files via a malformed search request, aka a new variant of the "Malformed Hit-Highlighting" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025.

**参考链接 / References**:
- N/A

---

#### 129. CVE-2001-0336

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
The Microsoft MS00-060 patch for IIS 5.0 and earlier introduces an error which allows attackers to cause a denial of service via a malformed request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5693.

**参考链接 / References**:
- N/A

---

#### 130. CVE-2001-0337

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
The Microsoft MS01-014 and MS01-016 patches for IIS 5.0 and earlier introduce a memory leak which allows attackers to cause a denial of service via a series of requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026.

**参考链接 / References**:
- N/A

---

#### 131. CVE-2001-0365

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: qualcomm:eudora

**漏洞描述 / Description**:
Eudora before 5.1 allows a remote attacker to execute arbitrary code, when the 'Use Microsoft Viewer' and 'allow executables in HTML content' options are enabled, via an HTML email message containing Javascript, with ActiveX controls and malicious code within IMG tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98503741910995&w=2.

**参考链接 / References**:
- N/A

---

#### 132. CVE-2001-0238

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_98, microsoft:windows_95, microsoft:windows_nt, microsoft:windows_me

**漏洞描述 / Description**:
Microsoft Data Access Component Internet Publishing Provider 8.103.2519.0 and earlier allows remote attackers to bypass Security Zone restrictions via WebDAV requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-074.shtml.

**参考链接 / References**:
- N/A

---

#### 133. CVE-2001-0239

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 Web Proxy allows remote attackers to cause a denial of service via a long web request with a specific type.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-073.shtml.

**参考链接 / References**:
- N/A

---

#### 134. CVE-2001-1243

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:internet_information_server

**漏洞描述 / Description**:
Scripting.FileSystemObject in asp.dll for Microsoft IIS 4.0 and 5.0 allows local or remote attackers to cause a denial of service (crash) via (1) creating an ASP program that uses Scripting.FileSystemObject to open a file with an MS-DOS device name, or (2) remotely injecting the device name into ASP programs that internally use Scripting.FileSystemObject.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/6800.php.

**参考链接 / References**:
- N/A

---

#### 135. CVE-2001-1319

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange 5.5 2000 allows remote attackers to cause a denial of service (hang) via exceptional BER encodings for the LDAP filter type field, as demonstrated by the PROTOS LDAPv3 test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-116.shtml.

**参考链接 / References**:
- N/A

---

#### 136. CVE-2001-0340

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
An interaction between the Outlook Web Access (OWA) service in Microsoft Exchange 2000 Server and Internet Explorer allows attackers to execute malicious script code against a user's mailbox via a message attachment that contains HTML code, which is executed automatically.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-091.shtml.

**参考链接 / References**:
- N/A

---

#### 137. CVE-2001-0341

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:frontpage_server_extensions, microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in Microsoft Visual Studio RAD Support sub-component of FrontPage Server Extensions allows remote attackers to execute arbitrary commands via a long registration request (URL) to fp30reg.dll.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99348216322147&w=2.

**参考链接 / References**:
- N/A

---

#### 138. CVE-2001-0344

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
An SQL query method in Microsoft SQL Server 2000 Gold and 7.0 using Mixed Mode allows local database users to gain privileges by reusing a cached connection of the sa administrator account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-095.shtml.

**参考链接 / References**:
- N/A

---

#### 139. CVE-2001-0345

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to prevent idle Telnet sessions from timing out, causing a denial of service by creating a large number of idle sessions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2843.

**参考链接 / References**:
- N/A

---

#### 140. CVE-2001-0346

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Handle leak in Microsoft Windows 2000 telnet service allows attackers to cause a denial of service by starting a large number of sessions and terminating them.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031.

**参考链接 / References**:
- N/A

---

#### 141. CVE-2001-0347

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Information disclosure vulnerability in Microsoft Windows 2000 telnet service allows remote attackers to determine the existence of user accounts such as Guest, or log in to the server without specifying the domain name, via a malformed userid.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-092.shtml.

**参考链接 / References**:
- N/A

---

#### 142. CVE-2001-0348

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to cause a denial of service (crash) via a long logon command that contains a backspace.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://razor.bindview.com/publish/advisories/adv_mstelnet.html.

**参考链接 / References**:
- N/A

---

#### 143. CVE-2001-0349

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the first of two variants of this vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/587587.

**参考链接 / References**:
- N/A

---

#### 144. CVE-2001-0350

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the second of two variants of this vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031.

**参考链接 / References**:
- N/A

---

#### 145. CVE-2001-0351

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows a local user to make a certain system call that allows the user to terminate a Telnet session and cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-092.shtml.

**参考链接 / References**:
- N/A

---

#### 146. CVE-2001-0501

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word 2002 and earlier allows attackers to automatically execute macros without warning the user by embedding the macros in a manner that escapes detection by the security scanner.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99325144322224&w=2.

**参考链接 / References**:
- N/A

---

#### 147. CVE-2001-0503

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting 3.01 with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service via a malformed string to the NetMeeting service port, aka a variant of the "NetMeeting Desktop Sharing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/5368.php.

**参考链接 / References**:
- N/A

---

#### 148. CVE-2001-1055

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_98se

**漏洞描述 / Description**:
The Microsoft Windows network stack allows remote attackers to cause a denial of service (CPU consumption) via a flood of malformed ARP request packets with random source IP and MAC addresses, as demonstrated by ARPNuke.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/200323.

**参考链接 / References**:
- N/A

---

#### 149. CVE-2001-0504

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Vulnerability in authentication process for SMTP service in Microsoft Windows 2000 allows remote attackers to use incorrect credentials to gain privileges and conduct activities such as mail relaying.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-107.shtml.

**参考链接 / References**:
- N/A

---

#### 150. CVE-2001-0538

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook View ActiveX Control in Microsoft Outlook 2002 and earlier allows remote attackers to execute arbitrary commands via a malicious HTML e-mail message or web page.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99496431214078&w=2.

**参考链接 / References**:
- N/A

---

#### 151. CVE-2001-0628

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word 2000 does not check AutoRecovery (.asd) files for macros, which allows a local attacker to execute arbitrary macros with the user ID of the Word user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q274/2/28.asp.

**参考链接 / References**:
- N/A

---

#### 152. CVE-2001-1099

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, symantec:norton_antivirus

**漏洞描述 / Description**:
The default configuration of Norton AntiVirus for Microsoft Exchange 2000 2.x allows remote attackers to identify the recipient's INBOX file path by sending an email with an attachment containing malicious content, which includes the path in the rejection notice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/212724.

**参考链接 / References**:
- N/A

---

#### 153. CVE-2001-0986

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
SQLQHit.asp sample file in Microsoft Index Server 2.0 allows remote attackers to obtain sensitive information such as the physical path, file attributes, or portions of source code by directly calling sqlqhit.asp with a CiScope parameter set to (1) webinfo, (2) extended_fileinfo, (3) extended_webinfo, or (4) fileinfo.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/214217.

**参考链接 / References**:
- N/A

---

#### 154. CVE-2001-0509

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:exchange_server, microsoft:windows_2000, microsoft:sql_server

**漏洞描述 / Description**:
Vulnerabilities in RPC servers in (1) Microsoft Exchange Server 2000 and earlier, (2) Microsoft SQL Server 2000 and earlier, (3) Windows NT 4.0, and (4) Windows 2000 allow remote attackers to cause a denial of service via malformed inputs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-041.

**参考链接 / References**:
- N/A

---

#### 155. CVE-2001-0541

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 7.1 and earlier allows remote attackers to execute arbitrary commands via a malformed Windows Media Station (.NSC) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/187001.

**参考链接 / References**:
- N/A

---

#### 156. CVE-2001-0546

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Memory leak in H.323 Gatekeeper Service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service (resource exhaustion) via a large amount of malformed H.323 data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3196.

**参考链接 / References**:
- N/A

---

#### 157. CVE-2001-0547

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Memory leak in the proxy service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows local attackers to cause a denial of service (resource exhaustion).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3197.

**参考链接 / References**:
- N/A

---

#### 158. CVE-2001-0658

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Cross-site scripting (CSS) vulnerability in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause other clients to execute certain script or read cookies via malicious script in an invalid URL that is not properly quoted in an error message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3198.

**参考链接 / References**:
- N/A

---

#### 159. CVE-2001-0709

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS 4.0 and before, when installed on a FAT partition, allows a remote attacker to obtain source code of ASP files via a URL encoded with Unicode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/192802.

**参考链接 / References**:
- N/A

---

#### 160. CVE-2001-0505

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
Multiple memory leaks in Microsoft Services for Unix 2.0 allow remote attackers to cause a denial of service (memory exhaustion) via a large number of malformed requests to (1) the Telnet service, or (2) the NFS service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/581603.

**参考链接 / References**:
- N/A

---

#### 161. CVE-2001-0660

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5, SP4 and earlier, allows remote attackers to identify valid user email addresses by directly accessing a back-end function that processes the global address list (GAL).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q307/1/95.ASP.

**参考链接 / References**:
- N/A

---

#### 162. CVE-2001-0666

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 2000 allows an authenticated user to cause a denial of service (CPU consumption) via a malformed OWA request for a deeply nested folder within the user's mailbox.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3368.

**参考链接 / References**:
- N/A

---

#### 163. CVE-2001-0718

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Vulnerability in (1) Microsoft Excel 2002 and earlier and (2) Microsoft PowerPoint 2002 and earlier allows attackers to bypass macro restrictions and execute arbitrary commands by modifying the data stream in the document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/218802.

**参考链接 / References**:
- N/A

---

#### 164. CVE-2001-0902

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_services

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to spoof web log entries via an HTTP request that includes hex-encoded newline or form-feed characters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100626531103946&w=2.

**参考链接 / References**:
- N/A

---

#### 165. CVE-2001-0909

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in helpctr.exe program in Microsoft Help Center for Windows XP allows remote attackers to execute arbitrary code via a long hcp: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100638955422011&w=2.

**参考链接 / References**:
- N/A

---

#### 166. CVE-2001-0719

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 6.4 allows remote attackers to execute arbitrary code via a malformed Advanced Streaming Format (ASF) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/202470.

**参考链接 / References**:
- N/A

---

#### 167. CVE-2001-0726

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5 Server, when used with Internet Explorer, does not properly detect certain inline script, which can allow remote attackers to perform arbitrary actions on a user's Exchange mailbox via an HTML e-mail message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5557.

**参考链接 / References**:
- N/A

---

#### 168. CVE-2001-1186

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to cause a denial of service via an HTTP request with a content-length value that is larger than the size of the request, which prevents IIS from timing out the connection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/244931.

**参考链接 / References**:
- N/A

---

#### 169. CVE-2001-1200

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Microsoft Windows XP allows local users to bypass a locked screen and run certain programs that are associated with Hot Keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7713.php.

**参考链接 / References**:
- N/A

---

#### 170. CVE-2001-0542

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflows in Microsoft SQL Server 7.0 and 2000 allow attackers with access to SQL Server to execute arbitrary code through the functions (1) raiserror, (2) formatmessage, or (3) xp_sprintf.  NOTE: the C runtime format string vulnerability reported in MS01-060 is identified by CVE-2001-0879.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100891252317406&w=2.

**参考链接 / References**:
- N/A

---

#### 171. CVE-2001-1218

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Internet Explorer for Unix 5.0SP1 allows local users to possibly cause a denial of service (crash) in CDE or the X server on Solaris 2.6 by rapidly scrolling Chinese characters or maximizing the window.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/246611.

**参考链接 / References**:
- N/A

---

#### 172. CVE-2001-1219

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows malicious website operators to cause a denial of service (client crash) via JavaScript that continually refreshes the window via self.location.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/246649.

**参考链接 / References**:
- N/A

---

#### 173. CVE-2001-1489

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Internet Explorer 6 allows remote attackers to cause a denial of service (CPU consumption and memory leak) via a web page with a large number of images.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/245152.

**参考链接 / References**:
- N/A

---

#### 174. CVE-2001-1497

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:ie, microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 4.0 through 6.0 could allow local users to differentiate between alphanumeric and non-alphanumeric characters used in a password by pressing certain control keys that jump between non-alphanumeric characters, which makes it easier to conduct a brute-force password guessing attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7592.php.

**参考链接 / References**:
- N/A

---

#### 175. CVE-2001-1533

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service via a flood of fragmented UDP packets.  NOTE: the vendor disputes this issue, saying that it requires high bandwidth to exploit, and the server does not experience any instability.  Therefore this "laws of physics" issue might not be included in CVE

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00018.html.

**参考链接 / References**:
- N/A

---

#### 176. CVE-2002-0077

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 treats objects invoked on an HTML page with the codebase property as part of Local Computer zone, which allows remote attackers to invoke executables present on the local system through objects such as the popup object, aka the "Local Executable Invocation via Object tag" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101103188711920&w=2.

**参考链接 / References**:
- N/A

---

#### 177. CVE-2002-0018

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
In Microsoft Windows NT and Windows 2000, a trusting domain that receives authorization information from a trusted domain does not verify that the trusted domain is authoritative for all listed SIDs, which allows remote attackers to gain Domain Administrator privileges on the trusting domain by injecting SIDs from untrusted domains into the authorization data that comes from from the trusted domain.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3997.

**参考链接 / References**:
- N/A

---

#### 178. CVE-2002-0021

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
Network Product Identification (PID) Checker in Microsoft Office v. X for Mac allows remote attackers to cause a denial of service (crash) via a malformed product announcement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/2041.

**参考链接 / References**:
- N/A

---

#### 179. CVE-2002-0049

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 2000 System Attendant gives "Everyone" group privileges to the WinReg key, which could allow remote attackers to read or modify registry keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/2042.

**参考链接 / References**:
- N/A

---

#### 180. CVE-2002-0050

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 allows remote attackers to execute arbitrary code via long authentication data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4157.

**参考链接 / References**:
- N/A

---

#### 181. CVE-2002-0054

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:windows_2000

**漏洞描述 / Description**:
SMTP service in (1) Microsoft Windows 2000 and (2) Internet Mail Connector (IMC) in Exchange Server 5.5 does not properly handle responses to NTLM authentication, which allows remote attackers to perform mail relaying via an SMTP AUTH command using null session credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101501580409373&w=2.

**参考链接 / References**:
- N/A

---

#### 182. CVE-2002-0055

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
SMTP service in Microsoft Windows 2000, Windows XP Professional, and Exchange 2000 allows remote attackers to cause a denial of service via a command with a malformed data transfer (BDAT) request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101558498401274&w=2.

**参考链接 / References**:
- N/A

---

#### 183. CVE-2002-0057

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:xml_core_services, microsoft:sql_server, microsoft:internet_explorer, microsoft:windows_xp

**漏洞描述 / Description**:
XMLHTTP control in Microsoft XML Core Services 2.6 and later does not properly handle IE Security Zone settings, which allows remote attackers to read arbitrary files by specifying a local file as an XML Data Source.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-12/0152.html.

**参考链接 / References**:
- N/A

---

#### 184. CVE-2002-0058

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:sdk, sun:jdk, microsoft:virtual_machine, sun:jre

**漏洞描述 / Description**:
Vulnerability in Java Runtime Environment (JRE) allows remote malicious web sites to hijack or sniff a web client's sessions, when an HTTP proxy is being used, via a Java applet that redirects the session to another server, as seen in (1) Netscape 6.0 through 6.1 and 4.79 and earlier, (2) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, and possibly other implementations that use vulnerable versions of SDK or JDK.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101534535304228&w=2.

**参考链接 / References**:
- N/A

---

#### 185. CVE-2002-0076

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:sdk, sun:jre, sun:jdk, microsoft:virtual_machine, hp:java_jre-jdk

**漏洞描述 / Description**:
Java Runtime Environment (JRE) Bytecode Verifier allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, as seen in (1) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, (2) Netscape 6.2.1 and earlier, and possibly other implementations that use vulnerable versions of SDK or JDK, aka a variant of the "Virtual Machine Verifier" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218.

**参考链接 / References**:
- N/A

---

#### 186. CVE-2002-0101

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows local users to cause a denial of service via an infinite loop for modeless dialogs showModelessDialog, which causes CPU usage while the focus for the dialog is not released.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101039104608083&w=2.

**参考链接 / References**:
- N/A

---

#### 187. CVE-2002-0136

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 on Windows 98 allows remote web pages to cause a denial of service (hang) via extremely long values for form fields such as INPUT and TEXTAREA, which can be automatically filled via Javascript.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250592.

**参考链接 / References**:
- N/A

---

#### 188. CVE-2002-0078

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The zone determination function in Microsoft Internet Explorer 5.5 and 6.0 allows remote attackers to run scripts in the Local Computer zone by embedding the script in a cookie, aka the "Cookie-based Script Execution" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101781180528301&w=2.

**参考链接 / References**:
- N/A

---

#### 189. CVE-2002-0151

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_xp, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Multiple UNC Provider (MUP) in Microsoft Windows operating systems allows local users to cause a denial of service or possibly gain SYSTEM privileges via a long UNC request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101793727306282&w=2.

**参考链接 / References**:
- N/A

---

#### 190. CVE-2002-0152

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:entourage, microsoft:office, microsoft:ie, microsoft:excel, microsoft:powerpoint

**漏洞描述 / Description**:
Buffer overflow in various Microsoft applications for Macintosh allows remote attackers to cause a denial of service (crash) or execute arbitrary code by invoking the file:// directive with a large number of / characters, which affects Internet Explorer 5.1, Outlook Express 5.0 through 5.0.2, Entourage v. X and 2001, PowerPoint v. X, 2001, and 98, and Excel v. X and 2001 for Macintosh.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101897994314015&w=2.

**参考链接 / References**:
- N/A

---

#### 191. CVE-2002-0154

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflows in extended stored procedures for Microsoft SQL Server 7.0 and 2000 allow remote attackers to cause a denial of service or execute arbitrary code via a database query with certain long arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101535353331625&w=2.

**参考链接 / References**:
- N/A

---

#### 192. CVE-2002-0224

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:windows_2000, microsoft:sql_server

**漏洞描述 / Description**:
The MSDTC (Microsoft Distributed Transaction Service Coordinator) for Microsoft Windows 2000, Microsoft IIS 5.0 and SQL Server 6.5 through SQL 2000 0.0 allows remote attackers to cause a denial of service (crash or hang) via malformed (random) input.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/253360.

**参考链接 / References**:
- N/A

---

#### 193. CVE-2002-0228

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:msn_messenger

**漏洞描述 / Description**:
Microsoft MSN Messenger allows remote attackers to use Javascript that references an ActiveX object to obtain sensitive information such as display names and web site navigation, and possibly more when the user is connected to certain Microsoft sites (or DNS-spoofed sites).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/254021.

**参考链接 / References**:
- N/A

---

#### 194. CVE-2002-1056

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:word

**漏洞描述 / Description**:
Microsoft Outlook 2000 and 2002, when configured to use Microsoft Word as the email editor, does not block scripts that are used while editing email messages in HTML or Rich Text Format (RTF), which could allow remote attackers to execute arbitrary scripts via an email that the user forwards or replies to.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101760380418890&w=2.

**参考链接 / References**:
- N/A

---

#### 195. CVE-2002-0155

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:msn_messenger_service_for_exchange, microsoft:msn_messenger, microsoft:msn_chat_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft MSN Chat ActiveX Control, as used in MSN Messenger 4.5 and 4.6, and Exchange Instant Messenger 4.5 and 4.6, allows remote attackers to execute arbitrary code via a long ResDLL parameter in the MSNChat OCX.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102089960531919&w=2.

**参考链接 / References**:
- N/A

---

#### 196. CVE-2002-0188

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the second variant of the "Content Disposition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-05/0126.html.

**参考链接 / References**:
- N/A

---

#### 197. CVE-2002-0190

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to execute arbitrary code under fewer security restrictions via a malformed web page that requires NetBIOS connectivity, aka "Zone Spoofing through Malformed Web Page" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9084.php.

**参考链接 / References**:
- N/A

---

#### 198. CVE-2002-0191

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to view arbitrary files that contain the "{" character via script containing the cssText property of the stylesheet object, aka "Local Information Disclosure through HTML Object" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101778302030981&w=2.

**参考链接 / References**:
- N/A

---

#### 199. CVE-2002-0193

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the first variant of the "Content Disposition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4752.

**参考链接 / References**:
- N/A

---

#### 200. CVE-2002-0368

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
The Store Service in Microsoft Exchange 2000 allows remote attackers to cause a denial of service (CPU consumption) via a mail message with a malformed RFC message attribute, aka "Malformed Mail Attribute can Cause Exchange 2000 to Exhaust CPU Resources."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9195.php.

**参考链接 / References**:
- N/A

---

#### 201. CVE-2002-0597

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
LANMAN service on Microsoft Windows 2000 allows remote attackers to cause a denial of service (CPU/memory exhaustion) via a stream of malformed data to microsoft-ds port 445.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0025.html.

**参考链接 / References**:
- N/A

---

#### 202. CVE-2002-0186

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the SQLXML ISAPI extension of Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code via data queries with a long content-type parameter, aka "Unchecked Buffer in SQLXML ISAPI Extension."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html.

**参考链接 / References**:
- N/A

---

#### 203. CVE-2002-0187

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Cross-site scripting vulnerability in the SQLXML component of Microsoft SQL Server 2000 allows an attacker to execute arbitrary script via the root parameter as part of an XML SQL query, aka "Script Injection via XML Tag."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html.

**参考链接 / References**:
- N/A

---

#### 204. CVE-2002-0371

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:proxy_server, microsoft:internet_explorer, university_of_minnesota:gopher, microsoft:isa_server

**漏洞描述 / Description**:
Buffer overflow in gopher client for Microsoft Internet Explorer 5.1 through 6.0, Proxy Server 2.0, or ISA Server 2000 allows remote attackers to execute arbitrary code via a gopher:// URL that redirects the user to a real or simulated gopher server that sends a long response.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102320516707940&w=2.

**参考链接 / References**:
- N/A

---

#### 205. CVE-2002-0372

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player versions 6.4 and 7.1 and Media Player for Windows XP allow remote attackers to bypass Internet Explorer's (IE) security mechanisms and run code via an executable .wma media file with a license installation requirement stored in the IE cache, aka the "Cache Path Disclosure via Windows Media Player".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9420.php.

**参考链接 / References**:
- N/A

---

#### 206. CVE-2002-0373

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
The Windows Media Device Manager (WMDM) Service in Microsoft Windows Media Player 7.1 on Windows 2000 systems allows local users to obtain LocalSystem rights via a program that calls the WMDM service to connect to an invalid local storage device, aka "Privilege Elevation through Windows Media Device Manager Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9421.php.

**参考链接 / References**:
- N/A

---

#### 207. CVE-2002-0615

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Windows Media Active Playlist in Microsoft Windows Media Player 7.1 stores information in a well known location on the local file system, allowing attackers to execute HTML scripts in the Local Computer zone, aka "Media Playback Script Invocation".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9422.php.

**参考链接 / References**:
- N/A

---

#### 208. CVE-2002-0620

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in the Profile Service of Microsoft Commerce Server 2000 allows remote attackers to cause the server to fail or run arbitrary code in the LocalSystem security context via an input field using an affected API.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4853.

**参考链接 / References**:
- N/A

---

#### 209. CVE-2002-0621

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in the Office Web Components (OWC) package installer used by Microsoft Commerce Server 2000 allows remote attackers to cause the process to fail or run arbitrary code in the LocalSystem security context via certain input to the OWC package installer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9424.php.

**参考链接 / References**:
- N/A

---

#### 210. CVE-2002-0622

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
The Office Web Components (OWC) package installer for Microsoft Commerce Server 2000 allows remote attackers to execute commands by passing the commands as input to the OWC package installer, aka "OWC Package Command Execution".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9425.php.

**参考链接 / References**:
- N/A

---

#### 211. CVE-2002-0623

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 and 2002 allows remote attackers to execute arbitrary code via long authentication data, aka "New Variant of the ISAPI Filter Buffer Overrun".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9426.php.

**参考链接 / References**:
- N/A

---

#### 212. CVE-2002-0624

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
Buffer overflow in the password encryption function of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows remote attackers to gain control of the database and execute arbitrary code via SQL Server Authentication, aka "Unchecked Buffer in Password Encryption Procedure."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2002-22.html.

**参考链接 / References**:
- N/A

---

#### 213. CVE-2002-0641

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
Buffer overflow in bulk insert procedure of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows attackers with database administration privileges to execute arbitrary code via a long filename in the BULK INSERT query.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102639885223746&w=2.

**参考链接 / References**:
- N/A

---

#### 214. CVE-2002-0642

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
The registry key containing the SQL Server service account information in Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, has insecure permissions, which allows local users to gain privileges, aka "Incorrect Permission on SQL Server Service Account Registry Key."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2002-22.html.

**参考链接 / References**:
- N/A

---

#### 215. CVE-2002-0643

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
The installation of Microsoft Data Engine 1.0 (MSDE 1.0), and Microsoft SQL Server 2000 creates setup.iss files with insecure permissions and does not delete them after installation, which allows local users to obtain sensitive data, including weakly encrypted passwords, to gain privileges, aka "SQL Server Installation Process May Leave Passwords on System."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102640092826731&w=2.

**参考链接 / References**:
- N/A

---

#### 216. CVE-2002-0409

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:.net_framework

**漏洞描述 / Description**:
orderdetails.aspx, as made available to Microsoft .NET developers as example code and demonstrated on www.ibuyspystore.com, allows remote attackers to view the orders of other users by modifying the OrderID parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101518860823788&w=2.

**参考链接 / References**:
- N/A

---

#### 217. CVE-2002-0443

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to bypass the policy that prohibits reusing old passwords by changing the current password before it expires, which does not enable the check for previous passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/260704.

**参考链接 / References**:
- N/A

---

#### 218. CVE-2002-0444

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services

**漏洞描述 / Description**:
Microsoft Windows 2000 running the Terminal Server 90-day trial version, and possibly other versions, does not apply group policies to incoming users when the number of connections to the SYSVOL share exceeds the maximum, e.g. with a maximum number of licenses, which can allow remote authenticated users to bypass group policies.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8813.php.

**参考链接 / References**:
- N/A

---

#### 219. CVE-2000-1209

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: compaq:insight_manager_xe, compaq:insight_manager, microsoft:msde, microsoft:data_engine

**漏洞描述 / Description**:
The "sa" account is installed with a default null password on (1) Microsoft SQL Server 2000, (2) SQL Server 7.0, and (3) Data Engine (MSDE) 1.0, including third party packages that use these products such as (4) Tumbleweed Secure Mail (MMS) (5) Compaq Insight Manager, and (6) Visio 2000, which allows remote attackers to gain privileges, as exploited by worms such as Voyager Alpha Force and Spida.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=96333895000350&w=2.

**参考链接 / References**:
- N/A

---

#### 220. CVE-2002-0507

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:exchange_server, rsa:securid

**漏洞描述 / Description**:
An interaction between Microsoft Outlook Web Access (OWA) with RSA SecurID allows local users to bypass the SecurID authentication for a previous user via several submissions of an OWA Authentication request with the proper OWA password for the previous user, which is eventually accepted by OWA.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/264705.

**参考链接 / References**:
- N/A

---

#### 221. CVE-2002-0616

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by attaching an inline macro to an object within an Excel workbook, aka the "Excel Inline Macros Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9397.php.

**参考链接 / References**:
- N/A

---

#### 222. CVE-2002-0617

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by creating a hyperlink on a drawing shape in a source workbook that points to a destination workbook containing an autoexecute macro, aka "Hyperlinked Excel Workbook Macro Bypass."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5175.

**参考链接 / References**:
- N/A

---

#### 223. CVE-2002-0618

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code in the Local Computer zone by embedding HTML scripts within an Excel workbook that contains an XSL stylesheet, aka "Excel XSL Stylesheet Script Execution".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=102256054320377&w=2.

**参考链接 / References**:
- N/A

---

#### 224. CVE-2002-0619

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
The Mail Merge Tool in Microsoft Word 2002 for Windows, when Microsoft Access is present on a system, allows remote attackers to execute Visual Basic (VBA) scripts within a mail merge document that is saved in HTML format, aka a "Variant of MS00-071, Word Mail Merge Vulnerability" (CVE-2000-0788).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102139136019862&w=2.

**参考链接 / References**:
- N/A

---

#### 225. CVE-2002-0644

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in several Database Consistency Checkers (DBCCs) for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows members of the db_owner and db_ddladmin roles to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038.

**参考链接 / References**:
- N/A

---

#### 226. CVE-2002-0645

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
SQL injection vulnerability in stored procedures for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 may allow authenticated users to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038.

**参考链接 / References**:
- N/A

---

#### 227. CVE-2002-0649

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Multiple buffer overflows in the Resolution Service for Microsoft SQL Server 2000 and Microsoft Desktop Engine 2000 (MSDE) allow remote attackers to cause a denial of service or execute arbitrary code via UDP packets to port 1434 in which (1) a 0x04 byte that causes the SQL Monitor thread to generate a long registry key name, or (2) a 0x08 byte with a long string causes heap corruption, as exploited by the Slammer/Sapphire worm.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

**参考链接 / References**:
- N/A

---

#### 228. CVE-2002-0650

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
The keep-alive mechanism for Microsoft SQL Server 2000 allows remote attackers to cause a denial of service (bandwidth consumption) via a "ping" style packet to the Resolution Service (UDP port 1434) with a spoofed IP address of another SQL Server system, which causes the two servers to exchange packets in an infinite loop.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

**参考链接 / References**:
- N/A

---

#### 229. CVE-2002-0695

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:microsoft_data_access_components, microsoft:data_access_components

**漏洞描述 / Description**:
Buffer overflow in the Transact-SQL (T-SQL) OpenRowSet component of Microsoft Data Access Components (MDAC) 2.5 through 2.7 for SQL Server 7.0 or 2000 allows remote attackers to execute arbitrary code via a query that calls the OpenRowSet command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9734.php.

**参考链接 / References**:
- N/A

---

#### 230. CVE-2002-0697

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:metadirectory_services

**漏洞描述 / Description**:
Microsoft Metadirectory Services (MMS) 2.2 allows remote attackers to bypass authentication and modify sensitive data by using an LDAP client to directly connect to MMS and bypass the checks for MMS credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9657.php.

**参考链接 / References**:
- N/A

---

#### 231. CVE-2002-0698

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Connector (IMC) for Microsoft Exchange Server 5.5 allows remote attackers to execute arbitrary code via an EHLO request from a system with a long name as obtained through a reverse DNS lookup, which triggers the overflow in IMC's hello response.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bvlive01.iss.net/issEn/delivery/xforce/alertdetail.jsp?oid=20759.

**参考链接 / References**:
- N/A

---

#### 232. CVE-2002-0700

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
Buffer overflow in a system function that performs user authentication for Microsoft Content Management Server (MCMS) 2001 allows attackers to execute code in the Local System context by authenticating to a web page that calls the function, aka "Unchecked Buffer in MDAC Function Could Enable SQL Server Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9783.php.

**参考链接 / References**:
- N/A

---

#### 233. CVE-2002-0718

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
Web authoring command in Microsoft Content Management Server (MCMS) 2001 allows attackers to authenticate and upload executable content, by modifying the upload location, aka "Program Execution via MCMS Authoring Function."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9784.php.

**参考链接 / References**:
- N/A

---

#### 234. CVE-2002-0719

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
SQL injection vulnerability in the function that services for Microsoft Content Management Server (MCMS) 2001 allows remote attackers to execute arbitrary commands via an MCMS resource request for image files or other files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9785.php.

**参考链接 / References**:
- N/A

---

#### 235. CVE-2002-0729

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 2000 allows remote attackers to cause a denial of service via a malformed 0x08 packet that is missing a colon separator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

**参考链接 / References**:
- N/A

---

#### 236. CVE-2002-0736

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:backoffice

**漏洞描述 / Description**:
Microsoft BackOffice 4.0 and 4.5, when configured to be accessible by other systems, allows remote attackers to bypass authentication and access the administrative ASP pages via an HTTP request with an authorization type (auth_type) that is not blank.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-04/0208.html.

**参考链接 / References**:
- N/A

---

#### 237. CVE-2002-0721

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000 installs with weak permissions for extended stored procedures that are associated with helper functions, which could allow unprivileged users, and possibly remote attackers, to run stored procedures with administrator privileges via (1) xp_execresultset, (2) xp_printstatements, or (3) xp_displayparamstmt.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2002-q3/0087.html.

**参考链接 / References**:
- N/A

---

#### 238. CVE-2002-0859

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:jet, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the OpenDataSource function of the Jet engine on Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102450188620081&w=2.

**参考链接 / References**:
- N/A

---

#### 239. CVE-2002-0647

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Buffer overflow in a legacy ActiveX control used to display specially formatted text in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to execute arbitrary code, aka "Buffer Overrun in Legacy Text Formatting ActiveX Control".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9935.php.

**参考链接 / References**:
- N/A

---

#### 240. CVE-2002-0648

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The legacy <script> data-island capability for XML in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to read arbitrary XML files, and portions of other files, via a URL whose "src" attribute redirects to a local file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103011639524314&w=2.

**参考链接 / References**:
- N/A

---

#### 241. CVE-2002-0691

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 5.5 allows remote attackers to execute scripts in the Local Computer zone via a URL that references a local HTML resource file, a variant of "Cross-Site Scripting in Local HTML Resource" as identified by CAN-2002-0189.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9938.php.

**参考链接 / References**:
- N/A

---

#### 242. CVE-2002-0722

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to misrepresent the source of a file in the File Download dialogue box to trick users into thinking that the file type is safe to download, aka "File Origin Spoofing."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103054692223380&w=2.

**参考链接 / References**:
- N/A

---

#### 243. CVE-2002-0723

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 and 6.0 does not properly verify the domain of a frame within a browser window, which allows remote attackers to read client files or invoke executable objects via the Object tag, aka "Cross Domain Verification in Object Tag."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9537.php.

**参考链接 / References**:
- N/A

---

#### 244. CVE-2002-0724

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in SMB (Server Message Block) protocol in Microsoft Windows NT, Windows 2000, and Windows XP allows attackers to cause a denial of service (crash) via a SMB_COM_TRANSACTION packet with a request for the (1) NetShareEnum, (2) NetServerEnum2, or (3) NetServerEnum3, aka "Unchecked Buffer in Network Share Provider Can Lead to Denial of Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103011556323184&w=2.

**参考链接 / References**:
- N/A

---

#### 245. CVE-2002-0726

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:tsac_activex_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft Terminal Services Advanced Client (TSAC) ActiveX control allows remote attackers to execute arbitrary code via a long server name field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2002/a082802-1.txt.

**参考链接 / References**:
- N/A

---

#### 246. CVE-2002-0727

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
The Host function in Microsoft Office Web Components (OWC) 2000 and 2002 is exposed in components that are marked as safe for scripting, which allows remote attackers to execute arbitrary commands via the setTimeout method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829645415486&w=2.

**参考链接 / References**:
- N/A

---

#### 247. CVE-2002-0860

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
The LoadText method in the spreadsheet component in Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to read arbitrary files through Internet Explorer via a URL that redirects to the target file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829911018463&w=2.

**参考链接 / References**:
- N/A

---

#### 248. CVE-2002-0861

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to bypass the "Allow paste operations via script" setting, even when it is disabled, via the (1) Copy method of the Cell object or (2) the Paste method of the Range object.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829726516346&w=2.

**参考链接 / References**:
- N/A

---

#### 249. CVE-2002-0975

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:directx_files_viewer_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft DirectX Files Viewer ActiveX control (xweb.ocx) 2.0.6.15 and earlier allows remote attackers to execute arbitrary via a long File parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102953851705859&w=2.

**参考链接 / References**:
- N/A

---

#### 250. CVE-2002-0977

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:file_transfer_manager

**漏洞描述 / Description**:
Buffer overflow in Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to execute arbitrary code via a long TS value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html.

**参考链接 / References**:
- N/A

---

#### 251. CVE-2002-0978

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:file_transfer_manager

**漏洞描述 / Description**:
Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to upload or download arbitrary files to arbitrary locations via a man-in-the-middle attack with modified TGT and TGN parameters in a call to the "Persist" function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html.

**参考链接 / References**:
- N/A

---

#### 252. CVE-2002-0982

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 2000 SP2, when configured as a distributor, allows attackers to execute arbitrary code via the @scriptfile parameter to the sp_MScopyscript stored procedure.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103004505027360&w=2.

**参考链接 / References**:
- N/A

---

#### 253. CVE-2002-1123

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the authentication function for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows remote attackers to execute arbitrary code via a long request to TCP port 1433, aka the "Hello" overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102873609025020&w=2.

**参考链接 / References**:
- N/A

---

#### 254. CVE-2002-0696

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:visual_foxpro

**漏洞描述 / Description**:
Microsoft Visual FoxPro 6.0 does not register its associated files with Internet Explorer, which allows remote attackers to execute Visual FoxPro applications without warning via HTML that references specially-crafted filenames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-120.shtml.

**参考链接 / References**:
- N/A

---

#### 255. CVE-2002-0699

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98, microsoft:windows_98se

**漏洞描述 / Description**:
Unknown vulnerability in the Certificate Enrollment ActiveX Control in Microsoft Windows 98, Windows 98 Second Edition, Windows Millennium, Windows NT 4.0, Windows 2000, and Windows XP allow remote attackers to delete digital certificates on a user's system via HTML.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-048.

**参考链接 / References**:
- N/A

---

#### 256. CVE-2002-0862

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:outlook_express, microsoft:windows_2000, microsoft:office

**漏洞描述 / Description**:
The (1) CertGetCertificateChain, (2) CertVerifyCertificateChainPolicy, and (3) WinVerifyTrust APIs within the CryptoAPI for Microsoft products including Microsoft Windows 98 through XP, Office for Mac, Internet Explorer for Mac, and Outlook Express for Mac, do not properly verify the Basic Constraints of intermediate CA-signed X.509 certificates, which allows remote attackers to spoof the certificates of trusted sites via a man-in-the-middle attack for SSL sessions, as originally reported for Internet Explorer and IIS.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102866120821995&w=2.

**参考链接 / References**:
- N/A

---

#### 257. CVE-2002-1015

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: realnetworks:realjukebox_2_plus, realnetworks:realone_player, realnetworks:realjukebox_2

**漏洞描述 / Description**:
RealJukebox 2 1.0.2.340 and 1.0.2.379, and RealOne Player Gold 6.0.10.505, allows remote attackers to execute arbitrary script in the Local computer zone by inserting the script into the skin.ini file of an RJS archive, then referencing skin.ini from a web page after it has been extracted, which is parsed as HTML by Internet Explorer or other Microsoft-based web readers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-07/0130.html.

**参考链接 / References**:
- N/A

---

#### 258. CVE-2002-1117

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: symantec_veritas:backup_exec

**漏洞描述 / Description**:
Veritas Backup Exec 8.5 and earlier requires that the "RestrictAnonymous" registry key for Microsoft Exchange 2000 must be set to 0, which enables anonymous listing of the SAM database and shares.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103134395124579&w=2.

**参考链接 / References**:
- N/A

---

#### 259. CVE-2002-0370

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_me, winzip:winzip, microsoft:windows_98_plus_pack, verity:keyview_viewing_sdk, allume_systems_division:stuffit_expander

**漏洞描述 / Description**:
Buffer overflow in the ZIP capability for multiple products allows remote attackers to cause a denial of service or execute arbitrary code via ZIP files containing entries with long filenames, including (1) Microsoft Windows 98 with Plus! Pack, (2) Windows XP, (3) Windows ME, (4) Lotus Notes R4 through R6 (pre-gold), (5) Verity KeyView, and (6) Stuffit Expander before 7.0.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0009.html.

**参考链接 / References**:
- N/A

---

#### 260. CVE-2002-0692

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp, microsoft:windows_2000, microsoft:frontpage_server_extensions

**漏洞描述 / Description**:
Buffer overflow in SmartHTML Interpreter (shtml.dll) in Microsoft FrontPage Server Extensions (FPSE) 2000 and 2002 allows remote attackers to cause a denial of service (CPU consumption) or run arbitrary code, respectively, via a certain type of web file request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10194.php.

**参考链接 / References**:
- N/A

---

#### 261. CVE-2002-0693

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Buffer overflow in the HTML Help ActiveX Control (hhctrl.ocx) in Microsoft Windows 98, 98 Second Edition, Millennium Edition, NT 4.0, NT 4.0 Terminal Server Edition, Windows 2000, and Windows XP allows remote attackers to execute code via (1) a long parameter to the Alink function, or (2) script containing a long argument to the showHelp function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103365849505409&w=2.

**参考链接 / References**:
- N/A

---

#### 262. CVE-2002-0694

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
The HTML Help facility in Microsoft Windows 98, 98 Second Edition, Millennium Edition, NT 4.0, NT 4.0 Terminal Server Edition, Windows 2000, and Windows XP uses the Local Computer Security Zone when opening .chm files from the Temporary Internet Files folder, which allows remote attackers to execute arbitrary code via HTML mail that references or inserts a malicious .chm file containing shortcuts that can be executed, aka "Code Execution via Compiled HTML Help File."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10254.php.

**参考链接 / References**:
- N/A

---

#### 263. CVE-2002-0863

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:.net_windows_server, microsoft:windows_xp

**漏洞描述 / Description**:
Remote Data Protocol (RDP) version 5.0 in Microsoft Windows 2000 and RDP 5.1 in Windows XP does not encrypt the checksums of plaintext session data, which could allow a remote attacker to determine the contents of encrypted sessions via sniffing, aka "Weak Encryption in RDP Protocol."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103235960119404&w=2.

**参考链接 / References**:
- N/A

---

#### 264. CVE-2002-0864

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:.net_windows_server

**漏洞描述 / Description**:
The Remote Data Protocol (RDP) version 5.1 in Microsoft Windows XP allows remote attackers to cause a denial of service (crash) when Remote Desktop is enabled via a PDU Confirm Active data packet that does not set the Pattern BLT command, aka "Denial of Service in Remote Desktop."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103235745116592&w=2.

**参考链接 / References**:
- N/A

---

#### 265. CVE-2002-0865

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
A certain class that supports XML (Extensible Markup Language) in Microsoft Virtual Machine (VM) 5.0.3805 and earlier, probably com.ms.osp.ospmrshl, exposes certain unsafe methods, which allows remote attackers to execute unsafe code via a Java applet, aka "Inappropriate Methods Exposed in XML Support Classes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10135.php.

**参考链接 / References**:
- N/A

---

#### 266. CVE-2002-0866

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Java Database Connectivity (JDBC) classes in Microsoft Virtual Machine (VM) up to and including 5.0.3805 allow remote attackers to load and execute DLLs (dynamic link libraries) via a Java applet that calls the constructor for com.ms.jdbc.odbc.JdbcOdbc with the desired DLL terminated by a null string, aka "DLL Execution via JDBC Classes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html.

**参考链接 / References**:
- N/A

---

#### 267. CVE-2002-0867

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to cause a denial of service (crash) in Internet Explorer via invalid handle data in a Java applet, aka "Handle Validation Flaw."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10134.php.

**参考链接 / References**:
- N/A

---

#### 268. CVE-2002-1137

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the Database Console Command (DBCC) that handles user inputs in Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, allows attackers to execute arbitrary code via a long SourceDB argument in a "non-SQL OLEDB data source" such as FoxPro, a variant of CAN-2002-0644.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-003.shtml.

**参考链接 / References**:
- N/A

---

#### 269. CVE-2002-1138

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, writes output files for scheduled jobs under its own privileges instead of the entity that launched it, which allows attackers to overwrite system files, aka "Flaw in Output File Handling for Scheduled Jobs."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-003.shtml.

**参考链接 / References**:
- N/A

---

#### 270. CVE-2002-1139

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_me, microsoft:windows_xp, microsoft:windows_98_plus_pack

**漏洞描述 / Description**:
The Compressed Folders feature in Microsoft Windows 98 with Plus! Pack, Windows Me, and Windows XP does not properly check the destination folder during the decompression of ZIP files, which allows attackers to place an executable file in a known location on a user's system, aka "Incorrect Target Path for Zipped File Decompression."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10252.php.

**参考链接 / References**:
- N/A

---

#### 271. CVE-2002-1140

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
The Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service (service hang) via malformed packet fragments, aka "Improper parameter size check leading to denial of service."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10258.php.

**参考链接 / References**:
- N/A

---

#### 272. CVE-2002-1141

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
An input validation error in the Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service via malformed fragmented RPC client packets, aka "Denial of service by sending an invalid RPC request."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10259.php.

**参考链接 / References**:
- N/A

---

#### 273. CVE-2002-1150

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
The Remote Desktop Sharing (RDS) Screen Saver Protection capability for Microsoft NetMeeting 3.01 through SP2 (4.4.3396) allows attackers with physical access to hijack remote sessions by entering certain logoff or shutdown sequences (such as CTRL-ALT-DEL) and canceling out of the resulting user confirmation prompts, such as when the remote user is editing a document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103228375116204&w=2.

**参考链接 / References**:
- N/A

---

#### 274. CVE-2001-1451

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Memory leak in the SNMP LAN Manager (LANMAN) MIB extension for Microsoft Windows 2000 before SP3, when the Print Spooler is not running, allows remote attackers to cause a denial of service (memory consumption) via a large number of GET or GETNEXT requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B296815.

**参考链接 / References**:
- N/A

---

#### 275. CVE-2002-1145

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
The xp_runwebtask stored procedure in the Web Tasks component of Microsoft SQL Server 7.0 and 2000, Microsoft Data Engine (MSDE) 1.0, and Microsoft Desktop Engine (MSDE) 2000 can be executed by PUBLIC, which allows an attacker to gain privileges by updating a webtask that is owned by the database owner through the msdb.dbo.mswebtasks table, which does not have strong permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103487044122900&w=2.

**参考链接 / References**:
- N/A

---

#### 276. CVE-2002-1179

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Buffer overflow in the S/MIME Parsing capability in Microsoft Outlook Express 5.5 and 6.0 allows remote attackers to execute arbitrary code via a digitally signed email with a long "From" address, which triggers the overflow when the user views or previews the message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103435413105661&w=2.

**参考链接 / References**:
- N/A

---

#### 277. CVE-2002-1214

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in Microsoft PPTP Service on Windows XP and Windows 2000 allows remote attackers to cause a denial of service (hang) and possibly execute arbitrary code via a certain PPTP packet with malformed control data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293146.

**参考链接 / References**:
- N/A

---

#### 278. CVE-2002-0869

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:internet_information_services

**漏洞描述 / Description**:
Unknown vulnerability in the hosting process (dllhost.exe) for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allows remote attackers to gain privileges by executing an out of process application that acquires LocalSystem privileges, aka "Out of Process Privilege Elevation."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0059.html.

**参考链接 / References**:
- N/A

---

#### 279. CVE-2002-1181

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:internet_information_services

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the administrative web pages for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allow remote attackers to execute HTML script as other users through (1) a certain ASP file in the IISHELP virtual directory, or (2) possibly other unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103651224215736&w=2.

**参考链接 / References**:
- N/A

---

#### 280. CVE-2002-1184

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The system root folder of Microsoft Windows 2000 has default permissions of Everyone group with Full access (Everyone:F) and is in the search path when locating programs during login or application launch from the desktop, which could allow attackers to gain privileges as other users via Trojan horse programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5415.

**参考链接 / References**:
- N/A

---

#### 281. CVE-2002-1142

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:ie, microsoft:data_access_components, microsoft:internet_explorer

**漏洞描述 / Description**:
Heap-based buffer overflow in the Remote Data Services (RDS) component of Microsoft Data Access Components (MDAC) 2.1 through 2.6, and Internet Explorer 5.01 through 6.0, allows remote attackers to execute code via a malformed HTTP request to the Data Stub.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0082.html.

**参考链接 / References**:
- N/A

---

#### 282. CVE-2002-1286

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to steal cookies and execute script in a different security context via a URL that contains a colon in the domain portion, which is not properly parsed and loads an applet from a malicious site within the security context of the site that is being visited by the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 283. CVE-2002-1287

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
Stack-based buffer overflow in the Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service via a long class name through (1) Class.forName or (2) ClassLoader.loadClass.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 284. CVE-2002-1288

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to determine the current directory of the Internet Explorer process via the getAbsolutePath() method in a File() call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 285. CVE-2002-1289

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read restricted process memory, cause a denial of service (crash), and possibly execute arbitrary code via the getNativeServices function, which creates an instance of the com.ms.awt.peer.INativeServices (INativeServices) class, whose methods do not verify the memory addresses that are passed as parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 286. CVE-2002-1290

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read and modify the contents of the Clipboard via an applet that accesses the (1) ClipBoardGetText and (2) ClipBoardSetText methods of the INativeServices class.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 287. CVE-2002-1291

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read arbitrary local files and network shares via an applet tag with a codebase set to a "file://%00" (null character) URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 288. CVE-2002-1292

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java virtual machine (VM) build 5.0.3805 and earlier, as used in Internet Explorer, allows remote attackers to extend the Standard Security Manager (SSM) class (com.ms.security.StandardSecurityManager) and bypass intended StandardSecurityManager restrictions by modifying the (1) deniedDefinitionPackages or (2) deniedAccessPackages settings, causing a denial of service by adding Java applets to the list of applets that are prevented from running.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 289. CVE-2002-1293

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, provides a public load0() method for the CabCracker class (com.ms.vm.loader.CabCracker), which allows remote attackers to bypass the security checks that are performed by the load() method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 290. CVE-2002-1294

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, can provide HTML object references to applets via Javascript, which allows remote attackers to cause a denial of service (crash due to illegal memory accesses) and possibly conduct other unauthorized activities via an applet that uses those references to access proprietary Microsoft methods.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 291. CVE-2002-1295

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service (crash) and possibly conduct other unauthorized activities via applet tags in HTML that bypass Java class restrictions (such as private constructors) by providing the class name in the code parameter, aka "Incomplete Java Object Instantiation Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

**参考链接 / References**:
- N/A

---

#### 292. CVE-2002-1183

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_98se, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Windows 98 and Windows NT 4.0 do not properly verify the Basic Constraints of digital certificates, allowing remote attackers to execute code, aka "New Variant of Certificate Validation Flaw Could Enable Identity Spoofing" (CAN-2002-0862).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5410.

**参考链接 / References**:
- N/A

---

#### 293. CVE-2002-1255

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 2002 allows remote attackers to cause a denial of service (repeated failure) via an email message with a certain invalid header field that is accessed using POP3, IMAP, or WebDAV, aka "E-mail Header Processing Flaw Could Cause Outlook 2002 to Fail."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6319.

**参考链接 / References**:
- N/A

---

#### 294. CVE-2002-1256

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
The SMB signing capability in the Server Message Block (SMB) protocol in Microsoft Windows 2000 and Windows XP allows attackers to disable the digital signing settings in an SMB session to force the data to be sent unsigned, then inject data into the session without detection, e.g. by modifying group policy information sent from a domain controller.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6367.

**参考链接 / References**:
- N/A

---

#### 295. CVE-2002-1257

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to execute arbitrary code by including a Java applet that invokes COM (Component Object Model) objects in a web site or an HTML mail.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6371.

**参考链接 / References**:
- N/A

---

#### 296. CVE-2002-1258

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Two vulnerabilities in Microsoft Virtual Machine (VM) up to and including build 5.0.3805, as used in Internet Explorer and other applications, allow remote attackers to read files via a Java applet with a spoofed location in the CODEBASE parameter in the APPLET tag, possibly due to a parsing error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069.

**参考链接 / References**:
- N/A

---

#### 297. CVE-2002-1260

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
The Java Database Connectivity (JDBC) APIs in Microsoft Virtual Machine (VM) 5.0.3805 and earlier allow remote attackers to bypass security checks and access database contents via an untrusted Java applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-026.shtml.

**参考链接 / References**:
- N/A

---

#### 298. CVE-2002-1325

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) build 5.0.3805 and earlier allows remote attackers to determine a local user's username via a Java applet that accesses the user.dir system property, aka "User.dir Exposure Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6380.

**参考链接 / References**:
- N/A

---

#### 299. CVE-2002-1327

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in the Windows Shell function in Microsoft Windows XP allows remote attackers to execute arbitrary code via an .MP3 or .WMA audio file with a corrupt custom attribute, aka "Unchecked Buffer in Windows Shell Could Enable System Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=104025849109384&w=2.

**参考链接 / References**:
- N/A

---

#### 300. CVE-2002-1670

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:windows_xp

**漏洞描述 / Description**:
Microsoft Windows XP Professional upgrade edition overwrites previously installed patches for Internet Explorer 6.0, leaving Internet Explorer unpatched.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250596.

**参考链接 / References**:
- N/A

---

#### 301. CVE-2017-9948

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: microsoft:skype

**漏洞描述 / Description**:
A stack buffer overflow vulnerability has been discovered in Microsoft Skype 7.2, 7.35, and 7.36 before 7.37, involving MSFTEDIT.DLL mishandling of remote RDP clipboard content within the message box.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99281.

**参考链接 / References**:
- N/A

---

#### 302. CVE-2024-26888

**严重程度 / Severity**: MEDIUM | CVSS: 5.5
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: msft: Fix memory leak

Fix leaking buffer allocated to send MSFT_OP_LE_MONITOR_ADVERTISEMENT.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://git.kernel.org/stable/c/5987b9f7d9314c7411136005b3a52f61a8cc0911.

**参考链接 / References**:
- N/A

---

#### 303. CVE-2024-36012

**严重程度 / Severity**: HIGH | CVSS: 7.8
**受影响产品 / Affected Products**: linux:linux_kernel

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: msft: fix slab-use-after-free in msft_do_close()

Tying the msft->data lifetime to hdev by freeing it in
hci_release_dev() to fix the following case:

[use]
msft_do_close()
  msft = hdev->msft_data;
  if (!msft)                      ...(1) <- passed.
    return;
  mutex_lock(&msft->filter_lock); ...(4) <- used after freed.

[free]
msft_unregister()
  msft = hdev->msft_data;
  hdev->msft_data = NULL;         ...(2)
  kfree(msft);                    ...(3) <- msft is freed.

==================================================================
BUG: KASAN: slab-use-after-free in __mutex_lock_common
kernel/locking/mutex.c:587 [inline]
BUG: KASAN: slab-use-after-free in __mutex_lock+0x8f/0xc30
kernel/locking/mutex.c:752
Read of size 8 at addr ffff888106cbbca8 by task kworker/u5:2/309

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://git.kernel.org/stable/c/10f9f426ac6e752c8d87bf4346930ba347aaabac.

**参考链接 / References**:
- N/A

---

#### 304. CVE-2025-40181

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

x86/kvm: Force legacy PCI hole to UC when overriding MTRRs for TDX/SNP

When running as an SNP or TDX guest under KVM, force the legacy PCI hole,
i.e. memory between Top of Lower Usable DRAM and 4GiB, to be mapped as UC
via a forced variable MTRR range.

In most KVM-based setups, legacy devices such as the HPET and TPM are
enumerated via ACPI.  ACPI enumeration includes a Memory32Fixed entry, and
optionally a SystemMemory descriptor for an OperationRegion, e.g. if the
device needs to be accessed via a Control Method.

If a SystemMemory entry is present, then the kernel's ACPI driver will
auto-ioremap the region so that it can be accessed at will.  However, the
ACPI spec doesn't provide a way to enumerate the memory type of
SystemMemory regions, i.e. there's no way to tell software that a region
must be mapped as UC vs. WB, etc.  As a result, Linux's ACPI driver always
maps SystemMemory regions using ioremap_cache(), i.e. as WB on x86.

The dedicated device drivers however, e.g. the HPET driver and TPM driver,
want to map their associated memory as UC or WC, as accessing PCI devices
using WB is unsupported.

On bare metal and non-CoCO, the conflicting requirements "work" as firmware
configures the PCI hole (and other device memory) to be UC in the MTRRs.
So even though the ACPI mappings request WB, they are forced to UC- in the
kernel's tracking due to the kernel properly handling the MTRR overrides,
and thus are compatible with the drivers' requested WC/UC-.

With force WB MTRRs on SNP and TDX guests, the ACPI mappings get their
requested WB if the ACPI mappings are established before the dedicated
driver code attempts to initialize the device.  E.g. if acpi_init()
runs before the corresponding device driver is probed, ACPI's WB mapping
will "win", and result in the driver's ioremap() failing because the
existing WB mapping isn't compatible with the requested WC/UC-.

E.g. when a TPM is emulated by the hypervisor (ignoring the security
implications of relying on what is allegedly an untrusted entity to store
measurements), the TPM driver will request UC and fail:

  [  1.730459] ioremap error for 0xfed40000-0xfed45000, requested 0x2, got 0x0
  [  1.732780] tpm_tis MSFT0101:00: probe with driver tpm_tis failed with error -12

Note, the '0x2' and '0x0' values refer to "enum page_cache_mode", not x86's
memtypes (which frustratingly are an almost pure inversion; 2 == WB, 0 == UC).
E.g. tracing mapping requests for TPM TIS yields:

 Mapping TPM TIS with req_type = 0
 WARNING: CPU: 22 PID: 1 at arch/x86/mm/pat/memtype.c:530 memtype_reserve+0x2ab/0x460
 Modules linked in:
 CPU: 22 UID: 0 PID: 1 Comm: swapper/0 Tainted: G        W           6.16.0-rc7+ #2 VOLUNTARY
 Tainted: [W]=WARN
 Hardware name: Google Google Compute Engine/Google Compute Engine, BIOS Google 05/29/2025
 RIP: 0010:memtype_reserve+0x2ab/0x460
  __ioremap_caller+0x16d/0x3d0
  ioremap_cache+0x17/0x30
  x86_acpi_os_ioremap+0xe/0x20
  acpi_os_map_iomem+0x1f3/0x240
  acpi_os_map_memory+0xe/0x20
  acpi_ex_system_memory_space_handler+0x273/0x440
  acpi_ev_address_space_dispatch+0x176/0x4c0
  acpi_ex_access_region+0x2ad/0x530
  acpi_ex_field_datum_io+0xa2/0x4f0
  acpi_ex_extract_from_field+0x296/0x3e0
  acpi_ex_read_data_from_field+0xd1/0x460
  acpi_ex_resolve_node_to_value+0x2ee/0x530
  acpi_ex_resolve_to_value+0x1f2/0x540
  acpi_ds_evaluate_name_path+0x11b/0x190
  acpi_ds_exec_end_op+0x456/0x960
  acpi_ps_parse_loop+0x27a/0xa50
  acpi_ps_parse_aml+0x226/0x600
  acpi_ps_execute_method+0x172/0x3e0
  acpi_ns_evaluate+0x175/0x5f0
  acpi_evaluate_object+0x213/0x490
  acpi_evaluate_integer+0x6d/0x140
  acpi_bus_get_status+0x93/0x150
  acpi_add_single_object+0x43a/0x7c0
  acpi_bus_check_add+0x149/0x3a0
  acpi_bus_check_add_1+0x16/0x30
  acpi_ns_walk_namespace+0x22c/0x360
  acpi_walk_namespace+0x15c/0x170
  acpi_bus_scan+0x1dd/0x200
  acpi_scan_init+0xe5/0x2b0
  acpi_init+0x264/0x5b0
  do_one_i
---truncated---

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://git.kernel.org/stable/c/0dccbc75e18df85399a71933d60b97494110f559.

**参考链接 / References**:
- N/A

---

#### 305. CVE-2023-53828

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: hci_sync: Avoid use-after-free in dbg for hci_add_adv_monitor()

KSAN reports use-after-free in hci_add_adv_monitor().

While adding an adv monitor,
    hci_add_adv_monitor() calls ->
    msft_add_monitor_pattern() calls ->
    msft_add_monitor_sync() calls ->
    msft_le_monitor_advertisement_cb() calls in an error case ->
    hci_free_adv_monitor() which frees the *moniter.

This is referenced by bt_dev_dbg() in hci_add_adv_monitor().

Fix the bt_dev_dbg() by using handle instead of monitor->handle.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://git.kernel.org/stable/c/81d8e9f59df63b8358751c1ffed9f1cf5c796909.

**参考链接 / References**:
- N/A

---

#### 306. CVE-2023-54210

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: hci_sync: Avoid use-after-free in dbg for hci_remove_adv_monitor()

KASAN reports that there's a use-after-free in
hci_remove_adv_monitor(). Trawling through the disassembly, you can
see that the complaint is from the access in bt_dev_dbg() under the
HCI_ADV_MONITOR_EXT_MSFT case. The problem case happens because
msft_remove_monitor() can end up freeing the monitor
structure. Specifically:
  hci_remove_adv_monitor() ->
  msft_remove_monitor() ->
  msft_remove_monitor_sync() ->
  msft_le_cancel_monitor_advertisement_cb() ->
  hci_free_adv_monitor()

Let's fix the problem by just stashing the relevant data when it's
still valid.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://git.kernel.org/stable/c/0d4d6b083da9b033ddccef72d77f373c819ae3ea.

**参考链接 / References**:
- N/A

---
