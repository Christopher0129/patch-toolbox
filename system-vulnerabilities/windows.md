# Windows 系统漏洞知识库 | Windows System Vulnerabilities

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 498**

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

---

#### 2. CVE-1999-0012

**严重程度 / Severity**: HIGH | CVSS: 7.0
**受影响产品 / Affected Products**: netscape:fasttrack_server, microsoft:personal_web_server, netscape:enterprise_server, microsoft:frontpage, microsoft:internet_information_server

**漏洞描述 / Description**:
Some web servers under Microsoft Windows allow remote attackers to bypass access restrictions for files with long file names.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012.

---

#### 3. CVE-1999-1556

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 6.5 uses weak encryption for the password for the SQLExecutiveCmdExec account and stores it in an accessible portion of the registry, which could allow local users to gain privileges by reading and decrypting the CmdExecAccount value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=90222453431645&w=2.

---

#### 4. CVE-1999-0288

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The WINS server in Microsoft Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service (process termination) via invalid UDP frames to port 137 (NETBIOS Name Service), as demonstrated via a flood of random packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://safenetworks.com/Windows/wins.html.

---

#### 5. CVE-1999-1291

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_nt

**漏洞描述 / Description**:
TCP/IP implementation in Microsoft Windows 95, Windows NT 4.0, and possibly others, allows remote attackers to reset connections by forcing a reset (RST) via a PSH ACK or other means, obtaining the target's last sequence number from the resulting packet, then spoofing a reset to the target.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/10789.

---

#### 6. CVE-1999-0364

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:access, fms_inc.:total_vb_sourcebook

**漏洞描述 / Description**:
Microsoft Access 97 stores a database password as plaintext in a foreign mdb, allowing access to data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91816470220259&w=2.

---

#### 7. CVE-1999-1544

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Buffer overflow in FTP server in Microsoft IIS 3.0 and 4.0 allows local and sometimes remote attackers to cause a denial of service via a long NLST (ls) command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91722115016183&w=2.

---

#### 8. CVE-1999-0379

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:backoffice_resource_kit

**漏洞描述 / Description**:
Microsoft Taskpads allows remote web sites to execute commands on the visiting user's machine via certain methods that are marked as Safe for Scripting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1019.

---

#### 9. CVE-1999-0386

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:personal_web_server, microsoft:frontpage

**漏洞描述 / Description**:
Microsoft Personal Web Server and FrontPage Personal Web Server in some Windows systems allows a remote attacker to read files on the server by using a nonstandard URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/111.

---

#### 10. CVE-1999-0419

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
When the Microsoft SMTP service attempts to send a message to a server and receives a 4xx error code, it quickly and repeatedly attempts to redeliver the message, causing a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419.

---

#### 11. CVE-1999-0468

**严重程度 / Severity**: HIGH | CVSS: 8.2
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.0 allows a remote server to read arbitrary files on the client's file system using the Microsoft Scriptlet Component.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012.

---

#### 12. CVE-1999-1097

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting 2.1 allows one client to read the contents of another client's clipboard via a CTRL-C in the chat box when the box is empty.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92586457816446&w=2.

---

#### 13. CVE-1999-0717

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:excel, microsoft:windows_2000, microsoft:windows_95, microsoft:windows_98, microsoft:windows_nt

**漏洞描述 / Description**:
A remote attacker can disable the virus warning mechanism in Microsoft Excel 97.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304.

---

#### 14. CVE-1999-1033

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook Express before 4.72.3612.1700 allows a malicious user to send a message that contains a .., which can inadvertently cause Outlook to re-enter POP3 command mode and cause the POP3 session to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92647407427342&w=2.

---

#### 15. CVE-1999-1520

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
A configuration problem in the Ad Server Sample directory (AdSamples) in Microsoft Site Server 3.0 allows an attacker to obtain the SITE.CSC file, which exposes sensitive SQL database information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=92647407227303&w=2.

---

#### 16. CVE-1999-1368

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: broadcom:inoculateit

**漏洞描述 / Description**:
AV Option for MS Exchange Server option for InoculateIT 4.53, and possibly other versions, only scans the Inbox folder tree of a Microsoft Exchange server, which could allow viruses to escape detection if a user's rules cause the message to be moved to a different mailbox.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=92652152723629&w=2.

---

#### 17. CVE-1999-1164

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook client allows remote attackers to cause a denial of service by sending multiple email messages with the same X-UIDL headers, which causes Outlook to hang.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93041631215856&w=2.

---

#### 18. CVE-1999-1011

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:site_server, microsoft:internet_information_server, microsoft:data_access_components, microsoft:index_server

**漏洞描述 / Description**:
The Remote Data Service (RDS) DataFactory component of Microsoft Data Access Components (MDAC) in IIS 3.x and 4.x exposes unsafe methods, which allows remote attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/j-054.shtml.

---

#### 19. CVE-2000-0323

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:jet

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to modify text files via a database query, aka the "Text I-ISAM" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org.

---

#### 20. CVE-1999-0700

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Dialer (dialer.exe), via a malformed dialer entry in the dialer.ini file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185.

---

#### 21. CVE-1999-0682

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange 5.5 allows a remote attacker to relay email (i.e. spam) using encapsulated SMTP addresses, even if the anti-relaying features are enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927.

---

#### 22. CVE-1999-0749

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Buffer overflow in Microsoft Telnet client in Windows 95 and Windows 98 via a malformed Telnet argument.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/586.

---

#### 23. CVE-2000-0325

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:jet

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to execute commands via a database query, aka the "VBA Shell" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/548.

---

#### 24. CVE-1999-1052

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
Microsoft FrontPage stores form results in a default location in /_private/form_results.txt, which is world-readable and accessible in the document root, which allows remote attackers to read possibly sensitive information submitted by other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93582550911564&w=2.

---

#### 25. CVE-1999-1016

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:internet_explorer, qualcomm:eudora, microsoft:frontpage

**漏洞描述 / Description**:
Microsoft HTML control as used in (1) Internet Explorer 5.0, (2) FrontPage Express, (3) Outlook Express 5, and (4) Eudora, and possibly others, allows remote malicious web site or HTML emails to cause a denial of service (100% CPU consumption) via large HTML form fields such as text inputs in a table cell.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=93578772920970&w=2.

---

#### 26. CVE-1999-0910

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commercial_internet_system, microsoft:site_server, microsoft:site_server_commerce

**漏洞描述 / Description**:
Microsoft Site Server and Commercial Internet System (MCIS) do not set an expiration for a cookie, which could then be cached by a proxy and inadvertently used by a different user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/625.

---

#### 27. CVE-1999-0794

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:office, microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel does not warn a user when a macro is present in a Symbolic Link (SYLK) format file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900.

---

#### 28. CVE-1999-0766

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346.

---

#### 29. CVE-2000-0327

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93993545118416&w=2.

---

#### 30. CVE-2000-0329

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:outlook, microsoft:outlook_express, microsoft:ie

**漏洞描述 / Description**:
A Microsoft ActiveX control allows a remote attacker to execute a malicious cabinet file via an attachment and an embedded script in an HTML mail, aka the "Active Setup Control" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048.

---

#### 31. CVE-2000-0073

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft Rich Text Format (RTF) reader allows attackers to cause a denial of service via a malformed control word.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973.

---

#### 32. CVE-1999-0999

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL 7.0 server allows a remote attacker to cause a denial of service via a malformed TDS packet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749.

---

#### 33. CVE-1999-0993

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Modifications to ACLs (Access Control Lists) in Microsoft Exchange  5.5 do not take effect until the directory store cache is refreshed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993.

---

#### 34. CVE-1999-1043

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 and 5.0 does not properly handle (1) malformed NNTP data, or (2) malformed SMTP data, which allows remote attackers to cause a denial of service (application error).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007.

---

#### 35. CVE-1999-1055

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 does not warn the user before executing worksheet functions, which could allow attackers to execute arbitrary commands by using the CALL function to execute a malicious DLL, aka the Excel "CALL Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/179.

---

#### 36. CVE-1999-1246

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
Direct Mailer feature in Microsoft Site Server 3.0 saves user domain names and passwords in plaintext in the TMLBQueue network share, which has insecure default permissions, allowing remote attackers to read the passwords and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q229/9/72.asp.

---

#### 37. CVE-1999-1259

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
Microsoft Office 98, Macintosh Edition, does not properly initialize the disk space used by Office 98 files and effectively inserts data from previously deleted files into the Office file, which could allow attackers to obtain sensitive information.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q189/5/29.asp.

---

#### 38. CVE-1999-1279

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sna_server

**漏洞描述 / Description**:
An interaction between the AS/400 shared folders feature and Microsoft SNA Server 3.0 and earlier allows users to view each other's folders when the users share the same Local APPC LU.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q138/0/01.asp.

---

#### 39. CVE-1999-1591

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:visual_interdev

**漏洞描述 / Description**:
Microsoft Internet Information Services (IIS) server 4.0 SP4, without certain hotfixes released for SP4, does not require authentication credentials under certain conditions, which allows remote attackers to bypass authentication requirements, as demonstrated by connecting via Microsoft Visual InterDev 6.0.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html.

---

#### 40. CVE-2000-0053

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commercial_internet_system

**漏洞描述 / Description**:
Microsoft Commercial Internet System (MCIS) IMAP server allows remote attackers to cause a denial of service via a malformed IMAP request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731.

---

#### 41. CVE-2000-0097

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
The WebHits ISAPI filter in Microsoft Index Server allows remote attackers to read arbitrary files, aka the "Malformed Hit-Highlighting Argument" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1210.

---

#### 42. CVE-2000-0098

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to determine the real path for a web directory via a request to an Internet Data Query file that does not exist.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006.

---

#### 43. CVE-2000-0132

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Java Virtual Machine allows remote attackers to read files via the getSystemResourceAsStream function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/957.

---

#### 44. CVE-2000-0089

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The rdisk utility in Microsoft Terminal Server Edition and Windows NT 4.0 stores registry hive information in a temporary file with permissions that allow local users to read it, aka the "RDISK Registry Enumeration File" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108.

---

#### 45. CVE-2000-0161

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:site_server

**漏洞描述 / Description**:
Sample web sites on Microsoft Site Server 3.0 Commerce Edition do not validate an identification number, which allows remote attackers to execute SQL commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/994.

---

#### 46. CVE-2000-0162

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:visual_studio, microsoft:internet_explorer, microsoft:ie

**漏洞描述 / Description**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011.

---

#### 47. CVE-2000-0160

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:outlook, microsoft:ie

**漏洞描述 / Description**:
The Microsoft Active Setup ActiveX component in Internet Explorer 4.x and 5.x allows a remote attacker to install software components without prompting the user by stating that the software's manufacturer is Microsoft.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com.

---

#### 48. CVE-2000-0216

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_messaging, microsoft:outlook, microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft email clients in Outlook, Exchange, and Windows Messaging automatically respond to Read Receipt and Delivery Receipt tags, which could allow an attacker to flood a mail system with responses by forging a Read Receipt request that is redirected to a large distribution list.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html.

---

#### 49. CVE-2000-0201

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The window.showHelp() method in Internet Explorer 5.x does not restrict HTML help files (.chm) to be executed from the local host, which allows remote attackers to execute arbitrary commands via Microsoft Networking.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1033.

---

#### 50. CVE-2000-0168

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98se, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Windows 9x operating systems allow an attacker to cause a denial of service via a pathname that includes file device names, aka the "DOS Device in Path Name" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1043.

---

#### 51. CVE-2000-0200

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:home_publishing, microsoft:clip_art, microsoft:greetings

**漏洞描述 / Description**:
Buffer overflow in Microsoft Clip Art Gallery allows remote attackers to cause a denial of service or execute commands via a malformed CIL (clip art library) file, aka the "Clip Art Buffer Overrun" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1034.

---

#### 52. CVE-2000-0202

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and Microsoft Data Engine (MSDE) 1.0 allow remote attackers to gain privileges via a malformed Select statement in an SQL query.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1041.

---

#### 53. CVE-2000-0199

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
When a new SQL Server is registered in Enterprise Manager for Microsoft SQL Server 7.0 and the "Always prompt for login name and password" option is not set, then the Enterprise Manager uses weak encryption to store the login ID and password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1055.

---

#### 54. CVE-2000-0228

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_rights_manager

**漏洞描述 / Description**:
Microsoft Windows Media License Manager allows remote attackers to cause a denial of service by sending a malformed request that causes the manager to halt, aka the "Malformed Media License Request" Vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1058.

---

#### 55. CVE-2000-0232

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:terminal_server, microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft TCP/IP Printing Services, aka Print Services for Unix, allows an attacker to cause a denial of service via a malformed TCP/IP print request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html.

---

#### 56. CVE-2000-0302

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to view the source code of ASP files by appending a %20 to the filename in the CiWebHitsFile argument to the null.htw URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=95453598317340&w=2.

---

#### 57. CVE-2000-0277

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 does not warn the user when executing Excel Macro Language (XLM) macros in external text files, which could allow an attacker to execute a macro virus, aka the "XLM Text Macro" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1272.

---

#### 58. CVE-2000-0260

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:frontpage, microsoft:visual_interdev

**漏洞描述 / Description**:
Buffer overflow in the dvwssr.dll DLL in Microsoft Visual Interdev 1.0 allows users to cause a denial of service or execute commands, aka the "Link View Server-Side Component" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/282.

---

#### 59. CVE-2000-1218

**严重程度 / Severity**: CRITICAL | CVSS: 9.8
**受影响产品 / Affected Products**: microsoft:windows_98se, microsoft:windows_xp, microsoft:windows_98, microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The default configuration for the domain name resolver for Microsoft Windows 98, NT 4.0, 2000, and XP sets the QueryIpMatching parameter to 0, which causes Windows to accept DNS updates from hosts that it did not query, which allows remote attackers to poison the DNS cache.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/458659.

---

#### 60. CVE-2000-0331

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:terminal_server, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Microsoft command processor (CMD.EXE) for Windows NT and Windows 2000 allows a local user to cause a denial of service via a long environment variable, aka the "Malformed Environment Variable" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html.

---

#### 61. CVE-2000-0304

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS 4.0 and 5.0 with the IISADMPWD virtual directory installed allows a remote attacker to cause a denial of service via a malformed request to the inetinfo.exe program, aka the "Undelimited .HTR Request" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1191.

---

#### 62. CVE-2000-0400

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The Microsoft Active Movie ActiveX Control in Internet Explorer 5 does not restrict which file types can be downloaded, which allows an attacker to download any type of file to a user's system by encoding it within an email message or news post.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=95868514521257&w=2.

---

#### 63. CVE-2000-0402

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
The Mixed Mode authentication capability in Microsoft SQL Server 7.0 stores the System Administrator (sa) account in plaintext in a log file which is readable by any user, aka the "SQL Server 7.0 Service Pack Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=263968.

---

#### 64. CVE-2000-0485

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server allows local users to obtain database passwords via the Data Transformation Service (DTS) package Properties dialog, aka the "DTS Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/62771.

---

#### 65. CVE-2000-0495

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
Microsoft Windows Media Encoder allows remote attackers to cause a denial of service via a malformed request, aka the "Malformed Windows Media Encoder Request" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1282.

---

#### 66. CVE-2000-0524

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Outlook and Outlook Express allow remote attackers to cause a denial of service by sending email messages with blank fields such as BCC, Reply-To, Return-Path, or From.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html.

---

#### 67. CVE-2000-0596

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.x does not warn a user before opening a Microsoft Access database file that is referenced within ActiveX OBJECT tags in an HTML document, which could allow remote attackers to execute arbitrary commands, aka the "IE Script" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-16.html.

---

#### 68. CVE-2000-0597

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Microsoft Office 2000 (Excel and PowerPoint) and PowerPoint 97 are marked as safe for scripting, which allows remote attackers to force Internet Explorer or some email clients to save files to arbitrary locations via the Visual Basic for Applications (VBA) SaveAs function, aka the "Office HTML Script" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1399.

---

#### 69. CVE-2000-0603

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 allows a local user to bypass permissions for stored procedures by referencing them via a temporary stored procedure, aka the "Stored Procedure Permissions" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1444.

---

#### 70. CVE-2000-0654

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft Enterprise Manager allows local users to obtain database passwords via the Data Transformation Service (DTS) package Registered Servers Dialog dialog, aka a variant of the "DTS Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1466.

---

#### 71. CVE-2000-0662

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 5.x and Microsoft Outlook allows remote attackers to read arbitrary files by redirecting the contents of an IFRAME using the DHTML Edit Control (DHTMLED).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1474.

---

#### 72. CVE-2000-0567

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Buffer overflow in Microsoft Outlook and Outlook Express allows remote attackers to execute arbitrary commands via a long Date field in an email header, aka the "Malformed E-mail Header" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1481.

---

#### 73. CVE-2000-0621

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 98 and 2000, and Outlook Express 4.0x and 5.0x, allow remote attackers to read files on the client's system via a malformed HTML message that stores files outside of the cache, aka the "Cache Bypass" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2000-14.html.

---

#### 74. CVE-2000-0653

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook Express allows remote attackers to monitor a user's email by creating a persistent browser link to the Outlook Express windows, aka the "Persistent Mail-Browser Link" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1502.

---

#### 75. CVE-2000-0637

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:excel

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 allows an attacker to execute arbitrary commands by specifying a malicious .dll using the Register.ID function, aka the "Excel REGISTER.ID Function" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1451.

---

#### 76. CVE-2000-1079

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_nt, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Interactions between the CIFS Browser Protocol and NetBIOS as implemented in Microsoft Windows 95, 98, NT, and 2000 allow remote attackers to modify dynamic NetBIOS name cache entries via a spoofed Browse Frame Request in a unicast or UDP broadcast datagram.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0116.html.

---

#### 77. CVE-2000-0563

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: apple:mac_os_runtime_for_java

**漏洞描述 / Description**:
The URLConnection function in MacOS Runtime Java (MRJ) 2.1 and earlier and the Microsoft virtual machine (VM) for MacOS allows a malicious web site operator to connect to arbitrary hosts using a HTTP redirection, in violation of the Java security model.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-06/0056.html.

---

#### 78. CVE-2000-0709

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to cause a denial of service in some components by requesting a URL whose name includes a standard DOS device name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html.

---

#### 79. CVE-2000-0710

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:frontpage

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to determine the physical path of the server components by requesting an invalid URL whose name includes a standard DOS device name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html.

---

#### 80. CVE-2000-0742

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
The IPX protocol implementation in Microsoft Windows 95 and 98 allows remote attackers to cause a denial of service by sending a ping packet with a source IP address that is a broadcast address, aka the "Malformed IPX Ping Packet" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1544.

---

#### 81. CVE-2000-0753

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
The Microsoft Outlook mail client identifies the physical path of the sender's machine within a winmail.dat attachment to Rich Text Format (RTF) files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/201422.

---

#### 82. CVE-2000-0756

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 2000 does not properly process long or malformed fields in vCard (.vcf) files, which allows attackers to cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1633.

---

#### 83. CVE-2000-0765

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:word, microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Buffer overflow in the HTML interpreter in Microsoft Office 2000 allows an attacker to execute arbitrary commands via a long embedded object tag, aka the "Microsoft Office HTML Object Tag" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1561.

---

#### 84. CVE-2000-0771

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to cause a denial of service by corrupting the local security policy via malformed RPC traffic, aka the "Local Security Policy Corruption" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1613.

---

#### 85. CVE-2000-0777

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:money

**漏洞描述 / Description**:
The password protection feature of Microsoft Money can store the password in plaintext, which allows attackers with physical access to the system to obtain the password, aka the "Money Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1615.

---

#### 86. CVE-2000-0788

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:access, microsoft:word

**漏洞描述 / Description**:
The Mail Merge tool in Microsoft Word does not prompt the user before executing Visual Basic (VBA) scripts in an Access database, which could allow an attacker to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1566.

---

#### 87. CVE-2000-0790

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_98se, microsoft:windows_2000

**漏洞描述 / Description**:
The web-based folder display capability in Microsoft Internet Explorer 5.5 on Windows 98 allows local users to insert Trojan horse programs by modifying the Folder.htt file and using the InvokeVerb method in the ShellDefView ActiveX control to specify a default execute option for the first file that is listed in the folder.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1571.

---

#### 88. CVE-2000-0849

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
Race condition in Microsoft Windows Media server allows remote attackers to cause a denial of service in the Windows Media Unicast Service via a malformed request, aka the "Unicast Service Race Condition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1655.

---

#### 89. CVE-2000-0854

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
When a Microsoft Office 2000 document is launched, the directory of that document is first used to locate DLL's such as riched20.dll and msi.dll, which could allow an attacker to execute arbitrary commands by inserting a Trojan Horse DLL into the same directory as the document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-09/0277.html.

---

#### 90. CVE-2000-0858

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:internet_information_server

**漏洞描述 / Description**:
Vulnerability in Microsoft Windows NT 4.0 allows remote attackers to cause a denial of service in IIS by sending it a series of malformed requests which cause INETINFO.EXE to fail, aka the "Invalid URL" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html.

---

#### 91. CVE-2000-1217

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 before Service Pack 2 (SP2), when running in a non-Windows 2000 domain and using NTLM authentication, and when credentials of an account are locally cached, allows local users to bypass account lockout policies and make an unlimited number of login attempts, aka the "Domain Account Lockout" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/818496.

---

#### 92. CVE-2000-1006

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 does not properly handle a MIME header with a blank charset specified, which allows remote attackers to cause a denial of service via a charset="" command, aka the "Malformed MIME Header" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1869.

---

#### 93. CVE-2000-1061

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) in Internet Explorer 4.x and 5.x allows an unsigned applet to create and use ActiveX controls, which allows a remote attacker to bypass Internet Explorer's security settings and execute arbitrary commands via a malicious web page or email, aka the "Microsoft VM ActiveX Component" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-075.

---

#### 94. CVE-2000-0817

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:network_monitor

**漏洞描述 / Description**:
Buffer overflow in the HTTP protocol parser for Microsoft Network Monitor (Netmon) allows remote attackers to execute arbitrary commands via malformed data, aka the "Netmon Protocol Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://xforce.iss.net/alerts/index.php.

---

#### 95. CVE-2000-0885

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:systems_management_server

**漏洞描述 / Description**:
Buffer overflows in Microsoft Network Monitor (Netmon) allow remote attackers to execute arbitrary commands via a long Browser Name in a CIFS Browse Frame, a long SNMP community name, or a long username or filename in an SMB session, aka the "Netmon Protocol Parsing" vulnerability.  NOTE: It is highly likely that this candidate will be split into multiple candidates.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083.

---

#### 96. CVE-2000-0929

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 allows attackers to cause a denial of service in RTF-enabled email clients via an embedded OCX control that is not closed properly, aka the "OCX Attachment" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97024839222747&w=2.

---

#### 97. CVE-2000-0942

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:indexing_service

**漏洞描述 / Description**:
The CiWebHitsFile component in Microsoft Indexing Services for Windows 2000 allows remote attackers to conduct a cross site scripting (CSS) attack via a CiRestriction parameter in a .htw request, aka the "Indexing Services Cross Site Scripting" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/141903.

---

#### 98. CVE-2000-0980

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98se, microsoft:windows_me, microsoft:windows_98

**漏洞描述 / Description**:
NMPI (Name Management Protocol on IPX) listener in Microsoft NWLink does not properly filter packets from a broadcast address, which allows remote attackers to cause a broadcast storm and flood the network.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1781.

---

#### 99. CVE-2000-0983

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service (CPU utilization) via a sequence of null bytes to the NetMeeting port, aka the "NetMeeting Desktop Sharing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ273854.

---

#### 100. CVE-2000-1081

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_displayparamstmt function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

---

#### 101. CVE-2000-1082

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_enumresultset function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

---

#### 102. CVE-2000-1083

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_showcolv function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

---

#### 103. CVE-2000-1084

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_updatecolvbm function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570878710037&w=2.

---

#### 104. CVE-2000-1085

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_peekqueue function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

---

#### 105. CVE-2000-1086

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_printstatements function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

---

#### 106. CVE-2000-1087

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_proxiedmetadata function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

---

#### 107. CVE-2000-1088

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:data_engine

**漏洞描述 / Description**:
The xp_SetSQLSecurity function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97570884410184&w=2.

---

#### 108. CVE-2000-1089

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Book Service allows local users to execute arbitrary commands, aka the "Phone Book Service Buffer Overflow" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2048.

---

#### 109. CVE-2000-1112

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 executes scripts in custom skin (.WMS) files, which could allow remote attackers to gain privileges via a skin that contains a malicious script, aka the ".WMS Script Execution" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1976.

---

#### 110. CVE-2000-1113

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player allows remote attackers to execute arbitrary commands via a malformed Active Stream Redirector (.ASX) file, aka the ".ASX Buffer Overrun" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2000/a112300-1.txt.

---

#### 111. CVE-2000-1139

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
The installation of Microsoft Exchange 2000 before Rev. A creates a user account with a known password, which could allow attackers to gain privileges, aka the "Exchange User Account" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1958.

---

#### 112. CVE-2000-1090

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS for Far East editions 4.0 and 5.0 allows remote attackers to read source code for parsed pages via a malformed URL that uses the lead-byte of a double-byte character.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.nsfocus.com/english/homepage/sa_08.htm.

---

#### 113. CVE-2001-0003

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:office, microsoft:windows_me

**漏洞描述 / Description**:
Web Extender Client (WEC) in Microsoft Office 2000, Windows 2000, and Windows Me does not properly process Internet Explorer security settings for NTLM authentication, which allows attackers to obtain NTLM credentials and possibly obtain the password, aka the "Web Client NTLM Authentication" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2199.

---

#### 114. CVE-2001-0005

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: microsoft:powerpoint

**漏洞描述 / Description**:
Buffer overflow in the parsing mechanism of the file loader in Microsoft PowerPoint 2000 allows attackers to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2001/a012301-1.txt.

---

#### 115. CVE-2001-0048

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The "Configure Your Server" tool in Microsoft 2000 domain controllers installs a blank password for the Directory Service Restore Mode, which allows attackers with physical access to the controller to install malicious programs, aka the "Directory Service Restore Mode Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2133.

---

#### 116. CVE-2001-0047

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The default permissions for the MTS Package Administration registry key in Windows NT 4.0 allows local users to install or modify arbitrary Microsoft Transaction Server (MTS) packages and gain privileges, aka one of the "Registry Permissions" vulnerabilities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2065.

---

#### 117. CVE-1999-0681

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:personal_web_server, microsoft:frontpage

**漏洞描述 / Description**:
Buffer overflow in Microsoft FrontPage Server Extensions (PWS) 3.0.2.926 on Windows 95, and possibly other versions, allows remote attackers to cause a denial of service via a long URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html.

---

#### 118. CVE-1999-0945

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Service (IMS) for Microsoft Exchange 5.5 and 5.0 allows remote attackers to conduct a denial of service via AUTH or AUTHINFO commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174.

---

#### 119. CVE-2001-1450

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.0 through 6.0 allows attackers to cause a denial of service (browser crash) via a crafted FTP URL such as "/.#./".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html.

---

#### 120. CVE-2001-1326

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: qualcomm:eudora

**漏洞描述 / Description**:
Eudora 5.1 allows remote attackers to execute arbitrary code when the "Use Microsoft Viewer" option is enabled and the "allow executables in HTML content" option is disabled, via an HTML email with a form that is activated from an image that the attacker spoofs as a link, which causes the user to execute the form and access embedded attachments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/187128.

---

#### 121. CVE-2001-0146

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:internet_information_services

**漏洞描述 / Description**:
IIS 5.0 and Microsoft Exchange 2000 allow remote attackers to cause a denial of service (memory allocation error) by repeatedly sending a series of specially formatted URL's.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/796584.

---

#### 122. CVE-2001-0261

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 Encrypted File System does not properly destroy backups of files that are encrypted, which allows a local attacker to recover the text of encrypted files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97992179925715&w=2.

---

#### 123. CVE-2001-1088

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:outlook_express

**漏洞描述 / Description**:
Microsoft Outlook 8.5 and earlier, and Outlook Express 5 and earlier, with the "Automatically put people I reply to in my address book" option enabled, do not notify the user when the "Reply-To" address is different than the "From" address, which could allow an untrusted remote attacker to spoof legitimate addresses and intercept email from the client that is intended for another user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241.

---

#### 124. CVE-2001-0237

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Memory leak in Microsoft 2000 domain controller allows remote attackers to cause a denial of service by repeatedly connecting to the Kerberos service and then disconnecting without sending any data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-079.shtml.

---

#### 125. CVE-2001-0240

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word before Word 2002 allows attackers to automatically execute macros without warning the user via a Rich Text Format (RTF) document that links to a template with the embedded macro.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2753.

---

#### 126. CVE-2001-0242

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflows in Microsoft Windows Media Player 7 and earlier allow remote attackers to execute arbitrary commands via (1) a long version tag in an .ASX file, or (2) a long banner tag, a variant of the ".ASX Buffer Overrun" vulnerability as discussed in MS:MS00-090.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/187528.

---

#### 127. CVE-2001-0244

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
Buffer overflow in Microsoft Index Server 2.0 allows remote attackers to execute arbitrary commands via a long search parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2709.

---

#### 128. CVE-2001-0245

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server, microsoft:indexing_service

**漏洞描述 / Description**:
Microsoft Index Server 2.0 in Windows NT 4.0, and Indexing Service in Windows 2000, allows remote attackers to read server-side include files via a malformed search request, aka a new variant of the "Malformed Hit-Highlighting" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025.

---

#### 129. CVE-2001-0336

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
The Microsoft MS00-060 patch for IIS 5.0 and earlier introduces an error which allows attackers to cause a denial of service via a malformed request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5693.

---

#### 130. CVE-2001-0337

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
The Microsoft MS01-014 and MS01-016 patches for IIS 5.0 and earlier introduce a memory leak which allows attackers to cause a denial of service via a series of requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026.

---

#### 131. CVE-2001-0365

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: qualcomm:eudora

**漏洞描述 / Description**:
Eudora before 5.1 allows a remote attacker to execute arbitrary code, when the 'Use Microsoft Viewer' and 'allow executables in HTML content' options are enabled, via an HTML email message containing Javascript, with ActiveX controls and malicious code within IMG tags.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98503741910995&w=2.

---

#### 132. CVE-2001-0238

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_98, microsoft:windows_95, microsoft:windows_nt, microsoft:windows_me

**漏洞描述 / Description**:
Microsoft Data Access Component Internet Publishing Provider 8.103.2519.0 and earlier allows remote attackers to bypass Security Zone restrictions via WebDAV requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-074.shtml.

---

#### 133. CVE-2001-0239

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 Web Proxy allows remote attackers to cause a denial of service via a long web request with a specific type.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-073.shtml.

---

#### 134. CVE-2001-1243

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:internet_information_server

**漏洞描述 / Description**:
Scripting.FileSystemObject in asp.dll for Microsoft IIS 4.0 and 5.0 allows local or remote attackers to cause a denial of service (crash) via (1) creating an ASP program that uses Scripting.FileSystemObject to open a file with an MS-DOS device name, or (2) remotely injecting the device name into ASP programs that internally use Scripting.FileSystemObject.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/6800.php.

---

#### 135. CVE-2001-1319

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange 5.5 2000 allows remote attackers to cause a denial of service (hang) via exceptional BER encodings for the LDAP filter type field, as demonstrated by the PROTOS LDAPv3 test suite.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://ciac.llnl.gov/ciac/bulletins/l-116.shtml.

---

#### 136. CVE-2001-0340

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
An interaction between the Outlook Web Access (OWA) service in Microsoft Exchange 2000 Server and Internet Explorer allows attackers to execute malicious script code against a user's mailbox via a message attachment that contains HTML code, which is executed automatically.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-091.shtml.

---

#### 137. CVE-2001-0341

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:frontpage_server_extensions, microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in Microsoft Visual Studio RAD Support sub-component of FrontPage Server Extensions allows remote attackers to execute arbitrary commands via a long registration request (URL) to fp30reg.dll.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99348216322147&w=2.

---

#### 138. CVE-2001-0344

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
An SQL query method in Microsoft SQL Server 2000 Gold and 7.0 using Mixed Mode allows local database users to gain privileges by reusing a cached connection of the sa administrator account.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-095.shtml.

---

#### 139. CVE-2001-0345

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to prevent idle Telnet sessions from timing out, causing a denial of service by creating a large number of idle sessions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2843.

---

#### 140. CVE-2001-0346

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Handle leak in Microsoft Windows 2000 telnet service allows attackers to cause a denial of service by starting a large number of sessions and terminating them.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031.

---

#### 141. CVE-2001-0347

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Information disclosure vulnerability in Microsoft Windows 2000 telnet service allows remote attackers to determine the existence of user accounts such as Guest, or log in to the server without specifying the domain name, via a malformed userid.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-092.shtml.

---

#### 142. CVE-2001-0348

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to cause a denial of service (crash) via a long logon command that contains a backspace.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://razor.bindview.com/publish/advisories/adv_mstelnet.html.

---

#### 143. CVE-2001-0349

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the first of two variants of this vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/587587.

---

#### 144. CVE-2001-0350

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the second of two variants of this vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031.

---

#### 145. CVE-2001-0351

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows a local user to make a certain system call that allows the user to terminate a Telnet session and cause a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-092.shtml.

---

#### 146. CVE-2001-0501

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word 2002 and earlier allows attackers to automatically execute macros without warning the user by embedding the macros in a manner that escapes detection by the security scanner.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99325144322224&w=2.

---

#### 147. CVE-2001-0503

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
Microsoft NetMeeting 3.01 with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service via a malformed string to the NetMeeting service port, aka a variant of the "NetMeeting Desktop Sharing" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/5368.php.

---

#### 148. CVE-2001-1055

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_98se

**漏洞描述 / Description**:
The Microsoft Windows network stack allows remote attackers to cause a denial of service (CPU consumption) via a flood of malformed ARP request packets with random source IP and MAC addresses, as demonstrated by ARPNuke.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/200323.

---

#### 149. CVE-2001-0504

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Vulnerability in authentication process for SMTP service in Microsoft Windows 2000 allows remote attackers to use incorrect credentials to gain privileges and conduct activities such as mail relaying.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/l-107.shtml.

---

#### 150. CVE-2001-0538

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook View ActiveX Control in Microsoft Outlook 2002 and earlier allows remote attackers to execute arbitrary commands via a malicious HTML e-mail message or web page.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=99496431214078&w=2.

---

#### 151. CVE-2001-0628

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:word

**漏洞描述 / Description**:
Microsoft Word 2000 does not check AutoRecovery (.asd) files for macros, which allows a local attacker to execute arbitrary macros with the user ID of the Word user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q274/2/28.asp.

---

#### 152. CVE-2001-1099

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, symantec:norton_antivirus

**漏洞描述 / Description**:
The default configuration of Norton AntiVirus for Microsoft Exchange 2000 2.x allows remote attackers to identify the recipient's INBOX file path by sending an email with an attachment containing malicious content, which includes the path in the rejection notice.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/212724.

---

#### 153. CVE-2001-0986

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:index_server

**漏洞描述 / Description**:
SQLQHit.asp sample file in Microsoft Index Server 2.0 allows remote attackers to obtain sensitive information such as the physical path, file attributes, or portions of source code by directly calling sqlqhit.asp with a CiScope parameter set to (1) webinfo, (2) extended_fileinfo, (3) extended_webinfo, or (4) fileinfo.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/214217.

---

#### 154. CVE-2001-0509

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:exchange_server, microsoft:windows_2000, microsoft:sql_server

**漏洞描述 / Description**:
Vulnerabilities in RPC servers in (1) Microsoft Exchange Server 2000 and earlier, (2) Microsoft SQL Server 2000 and earlier, (3) Windows NT 4.0, and (4) Windows 2000 allow remote attackers to cause a denial of service via malformed inputs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-041.

---

#### 155. CVE-2001-0541

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 7.1 and earlier allows remote attackers to execute arbitrary commands via a malformed Windows Media Station (.NSC) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/187001.

---

#### 156. CVE-2001-0546

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Memory leak in H.323 Gatekeeper Service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service (resource exhaustion) via a large amount of malformed H.323 data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3196.

---

#### 157. CVE-2001-0547

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Memory leak in the proxy service in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows local attackers to cause a denial of service (resource exhaustion).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3197.

---

#### 158. CVE-2001-0658

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Cross-site scripting (CSS) vulnerability in Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause other clients to execute certain script or read cookies via malicious script in an invalid URL that is not properly quoted in an error message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3198.

---

#### 159. CVE-2001-0709

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Microsoft IIS 4.0 and before, when installed on a FAT partition, allows a remote attacker to obtain source code of ASP files via a URL encoded with Unicode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/192802.

---

#### 160. CVE-2001-0505

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
Multiple memory leaks in Microsoft Services for Unix 2.0 allow remote attackers to cause a denial of service (memory exhaustion) via a large number of malformed requests to (1) the Telnet service, or (2) the NFS service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.kb.cert.org/vuls/id/581603.

---

#### 161. CVE-2001-0660

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5, SP4 and earlier, allows remote attackers to identify valid user email addresses by directly accessing a back-end function that processes the global address list (GAL).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q307/1/95.ASP.

---

#### 162. CVE-2001-0666

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 2000 allows an authenticated user to cause a denial of service (CPU consumption) via a malformed OWA request for a deeply nested folder within the user's mailbox.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3368.

---

#### 163. CVE-2001-0718

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:powerpoint, microsoft:excel

**漏洞描述 / Description**:
Vulnerability in (1) Microsoft Excel 2002 and earlier and (2) Microsoft PowerPoint 2002 and earlier allows attackers to bypass macro restrictions and execute arbitrary commands by modifying the data stream in the document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/218802.

---

#### 164. CVE-2001-0902

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_services

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to spoof web log entries via an HTTP request that includes hex-encoded newline or form-feed characters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100626531103946&w=2.

---

#### 165. CVE-2001-0909

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in helpctr.exe program in Microsoft Help Center for Windows XP allows remote attackers to execute arbitrary code via a long hcp: URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100638955422011&w=2.

---

#### 166. CVE-2001-0719

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 6.4 allows remote attackers to execute arbitrary code via a malformed Advanced Streaming Format (ASF) file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/202470.

---

#### 167. CVE-2001-0726

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5 Server, when used with Internet Explorer, does not properly detect certain inline script, which can allow remote attackers to perform arbitrary actions on a user's Exchange mailbox via an HTML e-mail message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5557.

---

#### 168. CVE-2001-1186

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to cause a denial of service via an HTTP request with a content-length value that is larger than the size of the request, which prevents IIS from timing out the connection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/244931.

---

#### 169. CVE-2001-1200

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Microsoft Windows XP allows local users to bypass a locked screen and run certain programs that are associated with Hot Keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7713.php.

---

#### 170. CVE-2001-0542

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflows in Microsoft SQL Server 7.0 and 2000 allow attackers with access to SQL Server to execute arbitrary code through the functions (1) raiserror, (2) formatmessage, or (3) xp_sprintf.  NOTE: the C runtime format string vulnerability reported in MS01-060 is identified by CVE-2001-0879.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=100891252317406&w=2.

---

#### 171. CVE-2001-1218

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Internet Explorer for Unix 5.0SP1 allows local users to possibly cause a denial of service (crash) in CDE or the X server on Solaris 2.6 by rapidly scrolling Chinese characters or maximizing the window.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/246611.

---

#### 172. CVE-2001-1219

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows malicious website operators to cause a denial of service (client crash) via JavaScript that continually refreshes the window via self.location.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/246649.

---

#### 173. CVE-2001-1489

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Microsoft Internet Explorer 6 allows remote attackers to cause a denial of service (CPU consumption and memory leak) via a web page with a large number of images.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/245152.

---

#### 174. CVE-2001-1497

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:ie, microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 4.0 through 6.0 could allow local users to differentiate between alphanumeric and non-alphanumeric characters used in a password by pressing certain control keys that jump between non-alphanumeric characters, which makes it easier to conduct a brute-force password guessing attack.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7592.php.

---

#### 175. CVE-2001-1533

**严重程度 / Severity**: MEDIUM | CVSS: 5.3
**受影响产品 / Affected Products**: microsoft:isa_server

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 allows remote attackers to cause a denial of service via a flood of fragmented UDP packets.  NOTE: the vendor disputes this issue, saying that it requires high bandwidth to exploit, and the server does not experience any instability.  Therefore this "laws of physics" issue might not be included in CVE

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00018.html.

---

#### 176. CVE-2002-0077

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 treats objects invoked on an HTML page with the codebase property as part of Local Computer zone, which allows remote attackers to invoke executables present on the local system through objects such as the popup object, aka the "Local Executable Invocation via Object tag" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101103188711920&w=2.

---

#### 177. CVE-2002-0018

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
In Microsoft Windows NT and Windows 2000, a trusting domain that receives authorization information from a trusted domain does not verify that the trusted domain is authoritative for all listed SIDs, which allows remote attackers to gain Domain Administrator privileges on the trusting domain by injecting SIDs from untrusted domains into the authorization data that comes from from the trusted domain.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/3997.

---

#### 178. CVE-2002-0021

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
Network Product Identification (PID) Checker in Microsoft Office v. X for Mac allows remote attackers to cause a denial of service (crash) via a malformed product announcement.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/2041.

---

#### 179. CVE-2002-0049

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Microsoft Exchange Server 2000 System Attendant gives "Everyone" group privileges to the WinReg key, which could allow remote attackers to read or modify registry keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/2042.

---

#### 180. CVE-2002-0050

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 allows remote attackers to execute arbitrary code via long authentication data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4157.

---

#### 181. CVE-2002-0054

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:windows_2000

**漏洞描述 / Description**:
SMTP service in (1) Microsoft Windows 2000 and (2) Internet Mail Connector (IMC) in Exchange Server 5.5 does not properly handle responses to NTLM authentication, which allows remote attackers to perform mail relaying via an SMTP AUTH command using null session credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101501580409373&w=2.

---

#### 182. CVE-2002-0055

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
SMTP service in Microsoft Windows 2000, Windows XP Professional, and Exchange 2000 allows remote attackers to cause a denial of service via a command with a malformed data transfer (BDAT) request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101558498401274&w=2.

---

#### 183. CVE-2002-0057

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:xml_core_services, microsoft:sql_server, microsoft:internet_explorer, microsoft:windows_xp

**漏洞描述 / Description**:
XMLHTTP control in Microsoft XML Core Services 2.6 and later does not properly handle IE Security Zone settings, which allows remote attackers to read arbitrary files by specifying a local file as an XML Data Source.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2001-12/0152.html.

---

#### 184. CVE-2002-0058

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: sun:sdk, sun:jdk, microsoft:virtual_machine, sun:jre

**漏洞描述 / Description**:
Vulnerability in Java Runtime Environment (JRE) allows remote malicious web sites to hijack or sniff a web client's sessions, when an HTTP proxy is being used, via a Java applet that redirects the session to another server, as seen in (1) Netscape 6.0 through 6.1 and 4.79 and earlier, (2) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, and possibly other implementations that use vulnerable versions of SDK or JDK.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101534535304228&w=2.

---

#### 185. CVE-2002-0076

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: sun:sdk, sun:jre, sun:jdk, microsoft:virtual_machine, hp:java_jre-jdk

**漏洞描述 / Description**:
Java Runtime Environment (JRE) Bytecode Verifier allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, as seen in (1) Microsoft VM build 3802 and earlier as used in Internet Explorer 4.x and 5.x, (2) Netscape 6.2.1 and earlier, and possibly other implementations that use vulnerable versions of SDK or JDK, aka a variant of the "Virtual Machine Verifier" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/pub-cgi/retrieve.pl?doctype=coll&doc=secbull/218.

---

#### 186. CVE-2002-0101

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows local users to cause a denial of service via an infinite loop for modeless dialogs showModelessDialog, which causes CPU usage while the focus for the dialog is not released.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101039104608083&w=2.

---

#### 187. CVE-2002-0136

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 on Windows 98 allows remote web pages to cause a denial of service (hang) via extremely long values for form fields such as INPUT and TEXTAREA, which can be automatically filled via Javascript.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250592.

---

#### 188. CVE-2002-0078

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The zone determination function in Microsoft Internet Explorer 5.5 and 6.0 allows remote attackers to run scripts in the Local Computer zone by embedding the script in a cookie, aka the "Cookie-based Script Execution" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101781180528301&w=2.

---

#### 189. CVE-2002-0151

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_xp, microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in Multiple UNC Provider (MUP) in Microsoft Windows operating systems allows local users to cause a denial of service or possibly gain SYSTEM privileges via a long UNC request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101793727306282&w=2.

---

#### 190. CVE-2002-0152

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:entourage, microsoft:office, microsoft:ie, microsoft:excel, microsoft:powerpoint

**漏洞描述 / Description**:
Buffer overflow in various Microsoft applications for Macintosh allows remote attackers to cause a denial of service (crash) or execute arbitrary code by invoking the file:// directive with a large number of / characters, which affects Internet Explorer 5.1, Outlook Express 5.0 through 5.0.2, Entourage v. X and 2001, PowerPoint v. X, 2001, and 98, and Excel v. X and 2001 for Macintosh.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101897994314015&w=2.

---

#### 191. CVE-2002-0154

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflows in extended stored procedures for Microsoft SQL Server 7.0 and 2000 allow remote attackers to cause a denial of service or execute arbitrary code via a database query with certain long arguments.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101535353331625&w=2.

---

#### 192. CVE-2002-0224

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_services, microsoft:windows_2000, microsoft:sql_server

**漏洞描述 / Description**:
The MSDTC (Microsoft Distributed Transaction Service Coordinator) for Microsoft Windows 2000, Microsoft IIS 5.0 and SQL Server 6.5 through SQL 2000 0.0 allows remote attackers to cause a denial of service (crash or hang) via malformed (random) input.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/253360.

---

#### 193. CVE-2002-0228

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:msn_messenger

**漏洞描述 / Description**:
Microsoft MSN Messenger allows remote attackers to use Javascript that references an ActiveX object to obtain sensitive information such as display names and web site navigation, and possibly more when the user is connected to certain Microsoft sites (or DNS-spoofed sites).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/254021.

---

#### 194. CVE-2002-1056

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook, microsoft:word

**漏洞描述 / Description**:
Microsoft Outlook 2000 and 2002, when configured to use Microsoft Word as the email editor, does not block scripts that are used while editing email messages in HTML or Rich Text Format (RTF), which could allow remote attackers to execute arbitrary scripts via an email that the user forwards or replies to.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101760380418890&w=2.

---

#### 195. CVE-2002-0155

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:msn_messenger_service_for_exchange, microsoft:msn_messenger, microsoft:msn_chat_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft MSN Chat ActiveX Control, as used in MSN Messenger 4.5 and 4.6, and Exchange Instant Messenger 4.5 and 4.6, allows remote attackers to execute arbitrary code via a long ResDLL parameter in the MSNChat OCX.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102089960531919&w=2.

---

#### 196. CVE-2002-0188

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the second variant of the "Content Disposition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-05/0126.html.

---

#### 197. CVE-2002-0190

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to execute arbitrary code under fewer security restrictions via a malformed web page that requires NetBIOS connectivity, aka "Zone Spoofing through Malformed Web Page" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9084.php.

---

#### 198. CVE-2002-0191

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to view arbitrary files that contain the "{" character via script containing the cssText property of the stylesheet object, aka "Local Information Disclosure through HTML Object" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101778302030981&w=2.

---

#### 199. CVE-2002-0193

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the first variant of the "Content Disposition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4752.

---

#### 200. CVE-2002-0368

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
The Store Service in Microsoft Exchange 2000 allows remote attackers to cause a denial of service (CPU consumption) via a mail message with a malformed RFC message attribute, aka "Malformed Mail Attribute can Cause Exchange 2000 to Exhaust CPU Resources."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9195.php.

---

#### 201. CVE-2002-0597

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
LANMAN service on Microsoft Windows 2000 allows remote attackers to cause a denial of service (CPU/memory exhaustion) via a stream of malformed data to microsoft-ds port 445.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0025.html.

---

#### 202. CVE-2002-0186

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the SQLXML ISAPI extension of Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code via data queries with a long content-type parameter, aka "Unchecked Buffer in SQLXML ISAPI Extension."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html.

---

#### 203. CVE-2002-0187

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Cross-site scripting vulnerability in the SQLXML component of Microsoft SQL Server 2000 allows an attacker to execute arbitrary script via the root parameter as part of an XML SQL query, aka "Script Injection via XML Tag."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html.

---

#### 204. CVE-2002-0371

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:proxy_server, microsoft:internet_explorer, university_of_minnesota:gopher, microsoft:isa_server

**漏洞描述 / Description**:
Buffer overflow in gopher client for Microsoft Internet Explorer 5.1 through 6.0, Proxy Server 2.0, or ISA Server 2000 allows remote attackers to execute arbitrary code via a gopher:// URL that redirects the user to a real or simulated gopher server that sends a long response.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102320516707940&w=2.

---

#### 205. CVE-2002-0372

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
Microsoft Windows Media Player versions 6.4 and 7.1 and Media Player for Windows XP allow remote attackers to bypass Internet Explorer's (IE) security mechanisms and run code via an executable .wma media file with a license installation requirement stored in the IE cache, aka the "Cache Path Disclosure via Windows Media Player".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9420.php.

---

#### 206. CVE-2002-0373

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_media_player

**漏洞描述 / Description**:
The Windows Media Device Manager (WMDM) Service in Microsoft Windows Media Player 7.1 on Windows 2000 systems allows local users to obtain LocalSystem rights via a program that calls the WMDM service to connect to an invalid local storage device, aka "Privilege Elevation through Windows Media Device Manager Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9421.php.

---

#### 207. CVE-2002-0615

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Windows Media Active Playlist in Microsoft Windows Media Player 7.1 stores information in a well known location on the local file system, allowing attackers to execute HTML scripts in the Local Computer zone, aka "Media Playback Script Invocation".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9422.php.

---

#### 208. CVE-2002-0620

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in the Profile Service of Microsoft Commerce Server 2000 allows remote attackers to cause the server to fail or run arbitrary code in the LocalSystem security context via an input field using an affected API.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/4853.

---

#### 209. CVE-2002-0621

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in the Office Web Components (OWC) package installer used by Microsoft Commerce Server 2000 allows remote attackers to cause the process to fail or run arbitrary code in the LocalSystem security context via certain input to the OWC package installer.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9424.php.

---

#### 210. CVE-2002-0622

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
The Office Web Components (OWC) package installer for Microsoft Commerce Server 2000 allows remote attackers to execute commands by passing the commands as input to the OWC package installer, aka "OWC Package Command Execution".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9425.php.

---

#### 211. CVE-2002-0623

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:commerce_server

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 and 2002 allows remote attackers to execute arbitrary code via long authentication data, aka "New Variant of the ISAPI Filter Buffer Overrun".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9426.php.

---

#### 212. CVE-2002-0624

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
Buffer overflow in the password encryption function of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows remote attackers to gain control of the database and execute arbitrary code via SQL Server Authentication, aka "Unchecked Buffer in Password Encryption Procedure."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2002-22.html.

---

#### 213. CVE-2002-0641

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
Buffer overflow in bulk insert procedure of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows attackers with database administration privileges to execute arbitrary code via a long filename in the BULK INSERT query.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102639885223746&w=2.

---

#### 214. CVE-2002-0642

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:sql_server, microsoft:msde

**漏洞描述 / Description**:
The registry key containing the SQL Server service account information in Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, has insecure permissions, which allows local users to gain privileges, aka "Incorrect Permission on SQL Server Service Account Registry Key."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cert.org/advisories/CA-2002-22.html.

---

#### 215. CVE-2002-0643

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
The installation of Microsoft Data Engine 1.0 (MSDE 1.0), and Microsoft SQL Server 2000 creates setup.iss files with insecure permissions and does not delete them after installation, which allows local users to obtain sensitive data, including weakly encrypted passwords, to gain privileges, aka "SQL Server Installation Process May Leave Passwords on System."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102640092826731&w=2.

---

#### 216. CVE-2002-0409

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:.net_framework

**漏洞描述 / Description**:
orderdetails.aspx, as made available to Microsoft .NET developers as example code and demonstrated on www.ibuyspystore.com, allows remote attackers to view the orders of other users by modifying the OrderID parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101518860823788&w=2.

---

#### 217. CVE-2002-0443

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to bypass the policy that prohibits reusing old passwords by changing the current password before it expires, which does not enable the check for previous passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/260704.

---

#### 218. CVE-2002-0444

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services

**漏洞描述 / Description**:
Microsoft Windows 2000 running the Terminal Server 90-day trial version, and possibly other versions, does not apply group policies to incoming users when the number of connections to the SYSVOL share exceeds the maximum, e.g. with a maximum number of licenses, which can allow remote authenticated users to bypass group policies.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/8813.php.

---

#### 219. CVE-2000-1209

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: compaq:insight_manager_xe, compaq:insight_manager, microsoft:msde, microsoft:data_engine

**漏洞描述 / Description**:
The "sa" account is installed with a default null password on (1) Microsoft SQL Server 2000, (2) SQL Server 7.0, and (3) Data Engine (MSDE) 1.0, including third party packages that use these products such as (4) Tumbleweed Secure Mail (MMS) (5) Compaq Insight Manager, and (6) Visio 2000, which allows remote attackers to gain privileges, as exploited by worms such as Voyager Alpha Force and Spida.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=96333895000350&w=2.

---

#### 220. CVE-2002-0507

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:exchange_server, rsa:securid

**漏洞描述 / Description**:
An interaction between Microsoft Outlook Web Access (OWA) with RSA SecurID allows local users to bypass the SecurID authentication for a previous user via several submissions of an OWA Authentication request with the proper OWA password for the previous user, which is eventually accepted by OWA.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/264705.

---

#### 221. CVE-2002-0616

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by attaching an inline macro to an object within an Excel workbook, aka the "Excel Inline Macros Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9397.php.

---

#### 222. CVE-2002-0617

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by creating a hyperlink on a drawing shape in a source workbook that points to a destination workbook containing an autoexecute macro, aka "Hyperlinked Excel Workbook Macro Bypass."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/5175.

---

#### 223. CVE-2002-0618

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:excel, microsoft:office

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code in the Local Computer zone by embedding HTML scripts within an Excel workbook that contains an XSL stylesheet, aka "Excel XSL Stylesheet Script Execution".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=102256054320377&w=2.

---

#### 224. CVE-2002-0619

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office

**漏洞描述 / Description**:
The Mail Merge Tool in Microsoft Word 2002 for Windows, when Microsoft Access is present on a system, allows remote attackers to execute Visual Basic (VBA) scripts within a mail merge document that is saved in HTML format, aka a "Variant of MS00-071, Word Mail Merge Vulnerability" (CVE-2000-0788).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102139136019862&w=2.

---

#### 225. CVE-2002-0644

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in several Database Consistency Checkers (DBCCs) for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows members of the db_owner and db_ddladmin roles to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038.

---

#### 226. CVE-2002-0645

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
SQL injection vulnerability in stored procedures for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 may allow authenticated users to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038.

---

#### 227. CVE-2002-0649

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Multiple buffer overflows in the Resolution Service for Microsoft SQL Server 2000 and Microsoft Desktop Engine 2000 (MSDE) allow remote attackers to cause a denial of service or execute arbitrary code via UDP packets to port 1434 in which (1) a 0x04 byte that causes the SQL Monitor thread to generate a long registry key name, or (2) a 0x08 byte with a long string causes heap corruption, as exploited by the Slammer/Sapphire worm.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

---

#### 228. CVE-2002-0650

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
The keep-alive mechanism for Microsoft SQL Server 2000 allows remote attackers to cause a denial of service (bandwidth consumption) via a "ping" style packet to the Resolution Service (UDP port 1434) with a spoofed IP address of another SQL Server system, which causes the two servers to exchange packets in an infinite loop.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

---

#### 229. CVE-2002-0695

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:microsoft_data_access_components, microsoft:data_access_components

**漏洞描述 / Description**:
Buffer overflow in the Transact-SQL (T-SQL) OpenRowSet component of Microsoft Data Access Components (MDAC) 2.5 through 2.7 for SQL Server 7.0 or 2000 allows remote attackers to execute arbitrary code via a query that calls the OpenRowSet command.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9734.php.

---

#### 230. CVE-2002-0697

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:metadirectory_services

**漏洞描述 / Description**:
Microsoft Metadirectory Services (MMS) 2.2 allows remote attackers to bypass authentication and modify sensitive data by using an LDAP client to directly connect to MMS and bypass the checks for MMS credentials.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9657.php.

---

#### 231. CVE-2002-0698

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:exchange_server

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Connector (IMC) for Microsoft Exchange Server 5.5 allows remote attackers to execute arbitrary code via an EHLO request from a system with a long name as obtained through a reverse DNS lookup, which triggers the overflow in IMC's hello response.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://bvlive01.iss.net/issEn/delivery/xforce/alertdetail.jsp?oid=20759.

---

#### 232. CVE-2002-0700

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
Buffer overflow in a system function that performs user authentication for Microsoft Content Management Server (MCMS) 2001 allows attackers to execute code in the Local System context by authenticating to a web page that calls the function, aka "Unchecked Buffer in MDAC Function Could Enable SQL Server Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9783.php.

---

#### 233. CVE-2002-0718

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
Web authoring command in Microsoft Content Management Server (MCMS) 2001 allows attackers to authenticate and upload executable content, by modifying the upload location, aka "Program Execution via MCMS Authoring Function."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9784.php.

---

#### 234. CVE-2002-0719

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:content_management_server

**漏洞描述 / Description**:
SQL injection vulnerability in the function that services for Microsoft Content Management Server (MCMS) 2001 allows remote attackers to execute arbitrary commands via an MCMS resource request for image files or other files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9785.php.

---

#### 235. CVE-2002-0729

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 2000 allows remote attackers to cause a denial of service via a malformed 0x08 packet that is missing a colon separator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102760196931518&w=2.

---

#### 236. CVE-2002-0736

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:backoffice

**漏洞描述 / Description**:
Microsoft BackOffice 4.0 and 4.5, when configured to be accessible by other systems, allows remote attackers to bypass authentication and access the administrative ASP pages via an HTTP request with an authorization type (auth_type) that is not blank.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-04/0208.html.

---

#### 237. CVE-2002-0721

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000 installs with weak permissions for extended stored procedures that are associated with helper functions, which could allow unprivileged users, and possibly remote attackers, to run stored procedures with administrator privileges via (1) xp_execresultset, (2) xp_printstatements, or (3) xp_displayparamstmt.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2002-q3/0087.html.

---

#### 238. CVE-2002-0859

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:jet, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the OpenDataSource function of the Jet engine on Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102450188620081&w=2.

---

#### 239. CVE-2002-0647

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Buffer overflow in a legacy ActiveX control used to display specially formatted text in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to execute arbitrary code, aka "Buffer Overrun in Legacy Text Formatting ActiveX Control".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9935.php.

---

#### 240. CVE-2002-0648

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
The legacy <script> data-island capability for XML in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to read arbitrary XML files, and portions of other files, via a URL whose "src" attribute redirects to a local file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103011639524314&w=2.

---

#### 241. CVE-2002-0691

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 5.5 allows remote attackers to execute scripts in the Local Computer zone via a URL that references a local HTML resource file, a variant of "Cross-Site Scripting in Local HTML Resource" as identified by CAN-2002-0189.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9938.php.

---

#### 242. CVE-2002-0722

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to misrepresent the source of a file in the File Download dialogue box to trick users into thinking that the file type is safe to download, aka "File Origin Spoofing."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103054692223380&w=2.

---

#### 243. CVE-2002-0723

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 and 6.0 does not properly verify the domain of a frame within a browser window, which allows remote attackers to read client files or invoke executable objects via the Object tag, aka "Cross Domain Verification in Object Tag."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/9537.php.

---

#### 244. CVE-2002-0724

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in SMB (Server Message Block) protocol in Microsoft Windows NT, Windows 2000, and Windows XP allows attackers to cause a denial of service (crash) via a SMB_COM_TRANSACTION packet with a request for the (1) NetShareEnum, (2) NetServerEnum2, or (3) NetServerEnum3, aka "Unchecked Buffer in Network Share Provider Can Lead to Denial of Service".

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103011556323184&w=2.

---

#### 245. CVE-2002-0726

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:tsac_activex_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft Terminal Services Advanced Client (TSAC) ActiveX control allows remote attackers to execute arbitrary code via a long server name field.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2002/a082802-1.txt.

---

#### 246. CVE-2002-0727

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
The Host function in Microsoft Office Web Components (OWC) 2000 and 2002 is exposed in components that are marked as safe for scripting, which allows remote attackers to execute arbitrary commands via the setTimeout method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829645415486&w=2.

---

#### 247. CVE-2002-0860

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
The LoadText method in the spreadsheet component in Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to read arbitrary files through Internet Explorer via a URL that redirects to the target file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829911018463&w=2.

---

#### 248. CVE-2002-0861

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:office_web_components, microsoft:project

**漏洞描述 / Description**:
Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to bypass the "Allow paste operations via script" setting, even when it is disabled, via the (1) Copy method of the Cell object or (2) the Paste method of the Range object.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=101829726516346&w=2.

---

#### 249. CVE-2002-0975

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:directx_files_viewer_control

**漏洞描述 / Description**:
Buffer overflow in Microsoft DirectX Files Viewer ActiveX control (xweb.ocx) 2.0.6.15 and earlier allows remote attackers to execute arbitrary via a long File parameter.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102953851705859&w=2.

---

#### 250. CVE-2002-0977

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:file_transfer_manager

**漏洞描述 / Description**:
Buffer overflow in Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to execute arbitrary code via a long TS value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html.

---

#### 251. CVE-2002-0978

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:file_transfer_manager

**漏洞描述 / Description**:
Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to upload or download arbitrary files to arbitrary locations via a man-in-the-middle attack with modified TGT and TGN parameters in a call to the "Persist" function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html.

---

#### 252. CVE-2002-0982

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 2000 SP2, when configured as a distributor, allows attackers to execute arbitrary code via the @scriptfile parameter to the sp_MScopyscript stored procedure.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103004505027360&w=2.

---

#### 253. CVE-2002-1123

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the authentication function for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows remote attackers to execute arbitrary code via a long request to TCP port 1433, aka the "Hello" overflow.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102873609025020&w=2.

---

#### 254. CVE-2002-0696

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:visual_foxpro

**漏洞描述 / Description**:
Microsoft Visual FoxPro 6.0 does not register its associated files with Internet Explorer, which allows remote attackers to execute Visual FoxPro applications without warning via HTML that references specially-crafted filenames.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/m-120.shtml.

---

#### 255. CVE-2002-0699

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98, microsoft:windows_98se

**漏洞描述 / Description**:
Unknown vulnerability in the Certificate Enrollment ActiveX Control in Microsoft Windows 98, Windows 98 Second Edition, Windows Millennium, Windows NT 4.0, Windows 2000, and Windows XP allow remote attackers to delete digital certificates on a user's system via HTML.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-048.

---

#### 256. CVE-2002-0862

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:outlook_express, microsoft:windows_2000, microsoft:office

**漏洞描述 / Description**:
The (1) CertGetCertificateChain, (2) CertVerifyCertificateChainPolicy, and (3) WinVerifyTrust APIs within the CryptoAPI for Microsoft products including Microsoft Windows 98 through XP, Office for Mac, Internet Explorer for Mac, and Outlook Express for Mac, do not properly verify the Basic Constraints of intermediate CA-signed X.509 certificates, which allows remote attackers to spoof the certificates of trusted sites via a man-in-the-middle attack for SSL sessions, as originally reported for Internet Explorer and IIS.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=102866120821995&w=2.

---

#### 257. CVE-2002-1015

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: realnetworks:realjukebox_2_plus, realnetworks:realone_player, realnetworks:realjukebox_2

**漏洞描述 / Description**:
RealJukebox 2 1.0.2.340 and 1.0.2.379, and RealOne Player Gold 6.0.10.505, allows remote attackers to execute arbitrary script in the Local computer zone by inserting the script into the skin.ini file of an RJS archive, then referencing skin.ini from a web page after it has been extracted, which is parsed as HTML by Internet Explorer or other Microsoft-based web readers.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-07/0130.html.

---

#### 258. CVE-2002-1117

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: symantec_veritas:backup_exec

**漏洞描述 / Description**:
Veritas Backup Exec 8.5 and earlier requires that the "RestrictAnonymous" registry key for Microsoft Exchange 2000 must be set to 0, which enables anonymous listing of the SAM database and shares.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103134395124579&w=2.

---

#### 259. CVE-2002-0370

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_me, winzip:winzip, microsoft:windows_98_plus_pack, verity:keyview_viewing_sdk, allume_systems_division:stuffit_expander

**漏洞描述 / Description**:
Buffer overflow in the ZIP capability for multiple products allows remote attackers to cause a denial of service or execute arbitrary code via ZIP files containing entries with long filenames, including (1) Microsoft Windows 98 with Plus! Pack, (2) Windows XP, (3) Windows ME, (4) Lotus Notes R4 through R6 (pre-gold), (5) Verity KeyView, and (6) Stuffit Expander before 7.0.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0009.html.

---

#### 260. CVE-2002-0692

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp, microsoft:windows_2000, microsoft:frontpage_server_extensions

**漏洞描述 / Description**:
Buffer overflow in SmartHTML Interpreter (shtml.dll) in Microsoft FrontPage Server Extensions (FPSE) 2000 and 2002 allows remote attackers to cause a denial of service (CPU consumption) or run arbitrary code, respectively, via a certain type of web file request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10194.php.

---

#### 261. CVE-2002-0693

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Buffer overflow in the HTML Help ActiveX Control (hhctrl.ocx) in Microsoft Windows 98, 98 Second Edition, Millennium Edition, NT 4.0, NT 4.0 Terminal Server Edition, Windows 2000, and Windows XP allows remote attackers to execute code via (1) a long parameter to the Alink function, or (2) script containing a long argument to the showHelp function.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103365849505409&w=2.

---

#### 262. CVE-2002-0694

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_me, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
The HTML Help facility in Microsoft Windows 98, 98 Second Edition, Millennium Edition, NT 4.0, NT 4.0 Terminal Server Edition, Windows 2000, and Windows XP uses the Local Computer Security Zone when opening .chm files from the Temporary Internet Files folder, which allows remote attackers to execute arbitrary code via HTML mail that references or inserts a malicious .chm file containing shortcuts that can be executed, aka "Code Execution via Compiled HTML Help File."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10254.php.

---

#### 263. CVE-2002-0863

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:.net_windows_server, microsoft:windows_xp

**漏洞描述 / Description**:
Remote Data Protocol (RDP) version 5.0 in Microsoft Windows 2000 and RDP 5.1 in Windows XP does not encrypt the checksums of plaintext session data, which could allow a remote attacker to determine the contents of encrypted sessions via sniffing, aka "Weak Encryption in RDP Protocol."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103235960119404&w=2.

---

#### 264. CVE-2002-0864

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_xp, microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:.net_windows_server

**漏洞描述 / Description**:
The Remote Data Protocol (RDP) version 5.1 in Microsoft Windows XP allows remote attackers to cause a denial of service (crash) when Remote Desktop is enabled via a PDU Confirm Active data packet that does not set the Pattern BLT command, aka "Denial of Service in Remote Desktop."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103235745116592&w=2.

---

#### 265. CVE-2002-0865

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
A certain class that supports XML (Extensible Markup Language) in Microsoft Virtual Machine (VM) 5.0.3805 and earlier, probably com.ms.osp.ospmrshl, exposes certain unsafe methods, which allows remote attackers to execute unsafe code via a Java applet, aka "Inappropriate Methods Exposed in XML Support Classes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10135.php.

---

#### 266. CVE-2002-0866

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Java Database Connectivity (JDBC) classes in Microsoft Virtual Machine (VM) up to and including 5.0.3805 allow remote attackers to load and execute DLLs (dynamic link libraries) via a Java applet that calls the constructor for com.ms.jdbc.odbc.JdbcOdbc with the desired DLL terminated by a null string, aka "DLL Execution via JDBC Classes."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2002-09/0271.html.

---

#### 267. CVE-2002-0867

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:virtual_machine

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to cause a denial of service (crash) in Internet Explorer via invalid handle data in a Java applet, aka "Handle Validation Flaw."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10134.php.

---

#### 268. CVE-2002-1137

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Buffer overflow in the Database Console Command (DBCC) that handles user inputs in Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, allows attackers to execute arbitrary code via a long SourceDB argument in a "non-SQL OLEDB data source" such as FoxPro, a variant of CAN-2002-0644.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-003.shtml.

---

#### 269. CVE-2002-1138

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, writes output files for scheduled jobs under its own privileges instead of the entity that launched it, which allows attackers to overwrite system files, aka "Flaw in Output File Handling for Scheduled Jobs."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-003.shtml.

---

#### 270. CVE-2002-1139

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_me, microsoft:windows_xp, microsoft:windows_98_plus_pack

**漏洞描述 / Description**:
The Compressed Folders feature in Microsoft Windows 98 with Plus! Pack, Windows Me, and Windows XP does not properly check the destination folder during the decompression of ZIP files, which allows attackers to place an executable file in a known location on a user's system, aka "Incorrect Target Path for Zipped File Decompression."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10252.php.

---

#### 271. CVE-2002-1140

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
The Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service (service hang) via malformed packet fragments, aka "Improper parameter size check leading to denial of service."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10258.php.

---

#### 272. CVE-2002-1141

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:services

**漏洞描述 / Description**:
An input validation error in the Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service via malformed fragmented RPC client packets, aka "Denial of service by sending an invalid RPC request."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/10259.php.

---

#### 273. CVE-2002-1150

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:netmeeting

**漏洞描述 / Description**:
The Remote Desktop Sharing (RDS) Screen Saver Protection capability for Microsoft NetMeeting 3.01 through SP2 (4.4.3396) allows attackers with physical access to hijack remote sessions by entering certain logoff or shutdown sequences (such as CTRL-ALT-DEL) and canceling out of the resulting user confirmation prompts, such as when the remote user is editing a document.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103228375116204&w=2.

---

#### 274. CVE-2001-1451

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Memory leak in the SNMP LAN Manager (LANMAN) MIB extension for Microsoft Windows 2000 before SP3, when the Print Spooler is not running, allows remote attackers to cause a denial of service (memory consumption) via a large number of GET or GETNEXT requests.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B296815.

---

#### 275. CVE-2002-1145

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:data_engine, microsoft:sql_server

**漏洞描述 / Description**:
The xp_runwebtask stored procedure in the Web Tasks component of Microsoft SQL Server 7.0 and 2000, Microsoft Data Engine (MSDE) 1.0, and Microsoft Desktop Engine (MSDE) 2000 can be executed by PUBLIC, which allows an attacker to gain privileges by updating a webtask that is owned by the database owner through the msdb.dbo.mswebtasks table, which does not have strong permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103487044122900&w=2.

---

#### 276. CVE-2002-1179

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:outlook_express

**漏洞描述 / Description**:
Buffer overflow in the S/MIME Parsing capability in Microsoft Outlook Express 5.5 and 6.0 allows remote attackers to execute arbitrary code via a digitally signed email with a long "From" address, which triggers the overflow when the user views or previews the message.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103435413105661&w=2.

---

#### 277. CVE-2002-1214

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in Microsoft PPTP Service on Windows XP and Windows 2000 allows remote attackers to cause a denial of service (hang) and possibly execute arbitrary code via a certain PPTP packet with malformed control data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/293146.

---

#### 278. CVE-2002-0869

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:internet_information_services

**漏洞描述 / Description**:
Unknown vulnerability in the hosting process (dllhost.exe) for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allows remote attackers to gain privileges by executing an out of process application that acquires LocalSystem privileges, aka "Out of Process Privilege Elevation."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0059.html.

---

#### 279. CVE-2002-1181

**严重程度 / Severity**: N/A | CVSS: 6.8
**受影响产品 / Affected Products**: microsoft:internet_information_server, microsoft:internet_information_services

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the administrative web pages for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allow remote attackers to execute HTML script as other users through (1) a certain ASP file in the IISHELP virtual directory, or (2) possibly other unknown attack vectors.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103651224215736&w=2.

---

#### 280. CVE-2002-1184

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The system root folder of Microsoft Windows 2000 has default permissions of Everyone group with Full access (Everyone:F) and is in the search path when locating programs during login or application launch from the desktop, which could allow attackers to gain privileges as other users via Trojan horse programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5415.

---

#### 281. CVE-2002-1142

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:ie, microsoft:data_access_components, microsoft:internet_explorer

**漏洞描述 / Description**:
Heap-based buffer overflow in the Remote Data Services (RDS) component of Microsoft Data Access Components (MDAC) 2.1 through 2.6, and Internet Explorer 5.01 through 6.0, allows remote attackers to execute code via a malformed HTTP request to the Data Stub.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0082.html.

---

#### 282. CVE-2002-1286

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to steal cookies and execute script in a different security context via a URL that contains a colon in the domain portion, which is not properly parsed and loads an applet from a malicious site within the security context of the site that is being visited by the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 283. CVE-2002-1287

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
Stack-based buffer overflow in the Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service via a long class name through (1) Class.forName or (2) ClassLoader.loadClass.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 284. CVE-2002-1288

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to determine the current directory of the Internet Explorer process via the getAbsolutePath() method in a File() call.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 285. CVE-2002-1289

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read restricted process memory, cause a denial of service (crash), and possibly execute arbitrary code via the getNativeServices function, which creates an instance of the com.ms.awt.peer.INativeServices (INativeServices) class, whose methods do not verify the memory addresses that are passed as parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 286. CVE-2002-1290

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read and modify the contents of the Clipboard via an applet that accesses the (1) ClipBoardGetText and (2) ClipBoardSetText methods of the INativeServices class.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 287. CVE-2002-1291

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read arbitrary local files and network shares via an applet tag with a codebase set to a "file://%00" (null character) URL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 288. CVE-2002-1292

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java virtual machine (VM) build 5.0.3805 and earlier, as used in Internet Explorer, allows remote attackers to extend the Standard Security Manager (SSM) class (com.ms.security.StandardSecurityManager) and bypass intended StandardSecurityManager restrictions by modifying the (1) deniedDefinitionPackages or (2) deniedAccessPackages settings, causing a denial of service by adding Java applets to the list of applets that are prevented from running.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 289. CVE-2002-1293

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, provides a public load0() method for the CabCracker class (com.ms.vm.loader.CabCracker), which allows remote attackers to bypass the security checks that are performed by the load() method.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 290. CVE-2002-1294

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, can provide HTML object references to applets via Javascript, which allows remote attackers to cause a denial of service (crash due to illegal memory accesses) and possibly conduct other unauthorized activities via an applet that uses those references to access proprietary Microsoft methods.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 291. CVE-2002-1295

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:java_virtual_machine

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service (crash) and possibly conduct other unauthorized activities via applet tags in HTML that bypass Java class restrictions (such as private constructors) by providing the class name in the code parameter, aka "Incomplete Java Object Instantiation Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=103682630823080&w=2.

---

#### 292. CVE-2002-1183

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_98se, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Windows 98 and Windows NT 4.0 do not properly verify the Basic Constraints of digital certificates, allowing remote attackers to execute code, aka "New Variant of Certificate Validation Flaw Could Enable Identity Spoofing" (CAN-2002-0862).

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/5410.

---

#### 293. CVE-2002-1255

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:outlook

**漏洞描述 / Description**:
Microsoft Outlook 2002 allows remote attackers to cause a denial of service (repeated failure) via an email message with a certain invalid header field that is accessed using POP3, IMAP, or WebDAV, aka "E-mail Header Processing Flaw Could Cause Outlook 2002 to Fail."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6319.

---

#### 294. CVE-2002-1256

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000_terminal_services, microsoft:windows_2000, microsoft:windows_xp

**漏洞描述 / Description**:
The SMB signing capability in the Server Message Block (SMB) protocol in Microsoft Windows 2000 and Windows XP allows attackers to disable the digital signing settings in an SMB session to force the data to be sent unsigned, then inject data into the session without detection, e.g. by modifying group policy information sent from a domain controller.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6367.

---

#### 295. CVE-2002-1257

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) up to and including build 5.0.3805 allows remote attackers to execute arbitrary code by including a Java applet that invokes COM (Component Object Model) objects in a web site or an HTML mail.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6371.

---

#### 296. CVE-2002-1258

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Two vulnerabilities in Microsoft Virtual Machine (VM) up to and including build 5.0.3805, as used in Internet Explorer and other applications, allow remote attackers to read files via a Java applet with a spoofed location in the CODEBASE parameter in the APPLET tag, possibly due to a parsing error.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-069.

---

#### 297. CVE-2002-1260

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
The Java Database Connectivity (JDBC) APIs in Microsoft Virtual Machine (VM) 5.0.3805 and earlier allow remote attackers to bypass security checks and access database contents via an untrusted Java applet.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ciac.org/ciac/bulletins/n-026.shtml.

---

#### 298. CVE-2002-1325

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000_terminal_services, microsoft:windows_me, microsoft:windows_2000, microsoft:windows_98

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) build 5.0.3805 and earlier allows remote attackers to determine a local user's username via a Java applet that accesses the user.dir system property, aka "User.dir Exposure Vulnerability."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/6380.

---

#### 299. CVE-2002-1327

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_xp

**漏洞描述 / Description**:
Buffer overflow in the Windows Shell function in Microsoft Windows XP allows remote attackers to execute arbitrary code via an .MP3 or .WMA audio file with a corrupt custom attribute, aka "Unchecked Buffer in Windows Shell Could Enable System Compromise."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=104025849109384&w=2.

---

#### 300. CVE-2002-1670

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:internet_explorer, microsoft:windows_xp

**漏洞描述 / Description**:
Microsoft Windows XP Professional upgrade edition overwrites previously installed patches for Internet Explorer 6.0, leaving Internet Explorer unpatched.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://online.securityfocus.com/archive/1/250596.

---

#### 301. CVE-2017-9948

**严重程度 / Severity**: HIGH | CVSS: 8.8
**受影响产品 / Affected Products**: microsoft:skype

**漏洞描述 / Description**:
A stack buffer overflow vulnerability has been discovered in Microsoft Skype 7.2, 7.35, and 7.36 before 7.37, involving MSFTEDIT.DLL mishandling of remote RDP clipboard content within the message box.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/99281.

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

---

#### 307. CVE-1999-0241

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:solaris, xfree86_project:x11r6, sun:sunos, sgi:irix

**漏洞描述 / Description**:
Guessable magic cookies in X Windows allows remote attackers to execute commands, e.g. through xterm.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0241.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0241
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0241

---

#### 308. CVE-1999-0179

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_95

**漏洞描述 / Description**:
Windows NT crashes or locks up when a Samba client executes a "cd .." command on a file share.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ140818.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ140818
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ140818

---

#### 309. CVE-1999-0249

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT RSHSVC program allows remote users to execute arbitrary commands.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0249.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0249
- https://www.cve.org/CVERecord?id=CVE-1999-0249

---

#### 310. CVE-1999-0274

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in Windows NT DNS servers through malicious packet which contains a response to a query that wasn't made.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0274.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0274
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0274

---

#### 311. CVE-1999-0345

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ibm:aix, sun:sunos, freebsd:freebsd, sco:open_desktop, sco:internet_faststart

**漏洞描述 / Description**:
Jolt ICMP attack causes a denial of service in Windows 95 and Windows NT systems.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/62170.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/62170
- http://www.securityfocus.com/archive/1/62170

---

#### 312. CVE-1999-0496

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT 4.0 user can gain administrative rights by forcing NtOpenProcessToken to succeed regardless of the user's permissions, aka GetAdmin.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ146965.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ146965
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ146965

---

#### 313. CVE-1999-0503

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT local user or administrator account has a guessable password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0503.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0503
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0503

---

#### 314. CVE-1999-0504

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT local user or administrator account has a default, null, blank, or missing password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0504.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0504
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0504

---

#### 315. CVE-1999-0534

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT user has inappropriate rights or privileges, e.g. Act as System, Add Workstation, Backup, Change System Time, Create Pagefile, Create Permanent Object, Create Token Name, Debug, Generate Security Audit, Increase Priority, Increase Quota, Load Driver, Lock Memory, Profile Single Process, Remote Shutdown, Replace Process Token, Restore, System Environment, Take Ownership, or Unsolicited Input.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0534.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0534
- https://www.cve.org/CVERecord?id=CVE-1999-0534

---

#### 316. CVE-1999-0535

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT account policy for passwords has inappropriate, security-critical settings, e.g. for password length, password age, or uniqueness.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0535.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0535
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0535

---

#### 317. CVE-1999-0562

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
The registry in Windows NT can be accessed remotely by users who are not administrators.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1023.

**参考链接 / References**:
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1023
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1023

---

#### 318. CVE-1999-0572

**严重程度 / Severity**: N/A | CVSS: 9.3
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
.reg files are associated with the Windows NT registry editor (regedit), making the registry susceptible to Trojan Horse attacks.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/178.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/178
- https://exchange.xforce.ibmcloud.com/vulnerabilities/178

---

#### 319. CVE-1999-0575

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system's user audit policy does not log an event success or failure, e.g. for Logon and Logoff, File and Object Access, Use of User Rights, User and Group Management, Security Policy Changes, Restart, Shutdown, and System, and Process Tracking.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0575.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0575
- https://www.cve.org/CVERecord?id=CVE-1999-0575

---

#### 320. CVE-1999-0576

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system's file audit policy does not log an event success or failure for security-critical files or directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0576.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0576
- https://www.cve.org/CVERecord?id=CVE-1999-0576

---

#### 321. CVE-1999-0582

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT account policy has inappropriate, security-critical settings for lockout, e.g. lockout duration, lockout after bad logon attempts, etc.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0582.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0582
- https://www.cve.org/CVERecord?id=CVE-1999-0582

---

#### 322. CVE-1999-0228

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in RPCSS.EXE program (RPC Locator) in Windows NT.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ162567.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ162567
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ162567

---

#### 323. CVE-1999-1128

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Internet Explorer 3.01 on Windows 95 allows remote malicious web sites to execute arbitrary commands via a .isp file, which is automatically downloaded and executed without prompting the user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://members.tripod.com/~unibyte/iebug3.htm.

**参考链接 / References**:
- http://members.tripod.com/~unibyte/iebug3.htm
- http://oliver.efri.hr/~crv/security/bugs/NT/ie3.html
- http://members.tripod.com/~unibyte/iebug3.htm
- http://oliver.efri.hr/~crv/security/bugs/NT/ie3.html

---

#### 324. CVE-1999-1380

**严重程度 / Severity**: N/A | CVSS: 5.1
**受影响产品 / Affected Products**: symantec:norton_utilities

**漏洞描述 / Description**:
Symantec Norton Utilities 2.0 for Windows 95 marks the TUNEOCX.OCX ActiveX control as safe for scripting, which allows remote attackers to execute arbitrary commands via the run option through malicious web pages that are accessed by browsers such as Internet Explorer 3.0.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://mlarchive.ima.com/win95/1997/May/0342.html.

**参考链接 / References**:
- http://mlarchive.ima.com/win95/1997/May/0342.html
- http://news.zdnet.co.uk/story/0%2C%2Cs2065518%2C00.html
- http://www.iss.net/security_center/static/7188.php
- http://www.net-security.sk/bugs/NT/nu20.html
- http://mlarchive.ima.com/win95/1997/May/0342.html

---

#### 325. CVE-1999-0227

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Access violation in LSASS.EXE (LSA/LSARPC) program in Windows NT allows a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ154087.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ154087
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ154087

---

#### 326. CVE-1999-0275

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in Windows NT DNS servers by flooding port 53 with too many characters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0275.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0275
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0275

---

#### 327. CVE-1999-0153

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_95, sco:openserver, microsoft:windows_nt

**漏洞描述 / Description**:
Windows 95/NT out of band (OOB) data denial of service through NETBIOS port, aka WinNuke.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.osvdb.org/1666.

**参考链接 / References**:
- http://www.osvdb.org/1666
- http://www.osvdb.org/1666

---

#### 328. CVE-1999-1463

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 before SP3 allows remote attackers to bypass firewall restrictions or cause a denial of service (crash) by sending improperly fragmented IP packets without the first fragment, which the TCP/IP stack incorrectly reassembles into a valid session.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/7219.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/7219
- https://exchange.xforce.ibmcloud.com/vulnerabilities/528
- http://www.securityfocus.com/archive/1/7219
- https://exchange.xforce.ibmcloud.com/vulnerabilities/528

---

#### 329. CVE-1999-1217

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The PATH in Windows NT includes the current working directory (.), which could allow local users to gain privileges by placing Trojan horse programs with the same name as commonly used system programs into certain directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=87602726319426&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=87602726319426&w=2
- http://marc.info/?l=ntbugtraq&m=87602726319435&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/526
- http://marc.info/?l=ntbugtraq&m=87602726319426&w=2
- http://marc.info/?l=ntbugtraq&m=87602726319435&w=2

---

#### 330. CVE-1999-1133

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: hp:hp-ux

**漏洞描述 / Description**:
HP-UX 9.x and 10.x running X windows may allow local attackers to gain privileges via (1) vuefile, (2) vuepad, (3) dtfile, or (4) dtpad, which do not authenticate users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602880019776&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602880019776&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/499
- http://marc.info/?l=bugtraq&m=87602880019776&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/499

---

#### 331. CVE-1999-0967

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:outlook_express, microsoft:internet_explorer, microsoft:windows_explorer

**漏洞描述 / Description**:
Buffer overflow in the HTML library used by Internet Explorer, Outlook Express, and Windows Explorer via the res: local resource protocol.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0967.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0967
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0967

---

#### 332. CVE-1999-1581

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Memory leak in Simple Network Management Protocol (SNMP) agent (snmp.exe) for Windows NT 4.0 before Service Pack 4 allows remote attackers to cause a denial of service (memory consumption) via a large number of SNMP packets with Object Identifiers (OIDs) that cannot be decoded.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/kb/q178381/.

**参考链接 / References**:
- http://support.microsoft.com/kb/q178381/
- http://www.kb.cert.org/vuls/id/4923
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8231
- http://support.microsoft.com/kb/q178381/
- http://www.kb.cert.org/vuls/id/4923

---

#### 333. CVE-1999-0225

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 allows remote attackers to cause a denial of service via a malformed SMB logon request in which the actual data size does not match the specified size.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=180963.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=180963
- http://www.nai.com/nai_labs/asp_set/advisory/25_windows_nt_dos_adv.asp
- http://www.microsoft.com/technet/support/kb.asp?ID=180963
- http://www.nai.com/nai_labs/asp_set/advisory/25_windows_nt_dos_adv.asp

---

#### 334. CVE-1999-1361

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 3.51 and 4.0 running WINS (Windows Internet Name Service) allows remote attackers to cause a denial of service (resource exhaustion) via a flood of malformed packets, which causes the server to slow down and fill the event logs with error messages.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90221101925891&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221101925891&w=2
- http://marc.info/?l=bugtraq&m=90221101925891&w=2

---

#### 335. CVE-1999-0158

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: cisco:pix_firewall_software

**漏洞描述 / Description**:
Cisco PIX firewall manager (PFM) on Windows NT allows attackers to connect to port 8080 on the PFM server and retrieve any file whose name and location is known.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.cisco.com/warp/public/770/pixmgrfile-pub.shtml.

**参考链接 / References**:
- http://www.cisco.com/warp/public/770/pixmgrfile-pub.shtml
- http://www.osvdb.org/685
- http://www.cisco.com/warp/public/770/pixmgrfile-pub.shtml
- http://www.osvdb.org/685

---

#### 336. CVE-1999-0969

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Windows NT RPC service allows remote attackers to conduct a denial of service using spoofed malformed RPC packets which generate an error message that is sent to the spoofed host, potentially setting up a loop, aka Snork.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ193233.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ193233
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-014
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ193233
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-014

---

#### 337. CVE-1999-0505

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT domain user or administrator account has a guessable password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0505.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0505
- https://www.cve.org/CVERecord?id=CVE-1999-0505

---

#### 338. CVE-1999-0506

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT domain user or administrator account has a default, null, blank, or missing password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0506.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0506
- https://www.cve.org/CVERecord?id=CVE-1999-0506

---

#### 339. CVE-1999-0546

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Windows NT guest account is enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0546.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0546
- https://www.cve.org/CVERecord?id=CVE-1999-0546

---

#### 340. CVE-1999-1289

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: mirabilis:icq

**漏洞描述 / Description**:
ICQ 98 beta on Windows NT leaks the internal IP address of a client in the TCP data segment of an ICQ packet instead of the public address (e.g. through NAT), which provides remote attackers with potentially sensitive information about the client or the internal network configuration.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/11233.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/11233
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1398
- http://www.securityfocus.com/archive/1/11233
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1398

---

#### 341. CVE-1999-0200

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT FTP server (WFTP) with the guest account enabled without a password allows an attacker to log into the FTP server using any username and password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=137853.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=137853
- http://www.microsoft.com/technet/support/kb.asp?ID=137853

---

#### 342. CVE-1999-0226

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT TCP/IP processes fragmented IP packets improperly, causing a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0226.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0226
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0226

---

#### 343. CVE-1999-0285

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in telnet from the Windows NT Resource Kit, by opening then immediately closing a connection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0285.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0285
- https://www.cve.org/CVERecord?id=CVE-1999-0285

---

#### 344. CVE-1999-0549

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT automatically logs in an administrator upon rebooting.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0549.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0549
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0549

---

#### 345. CVE-1999-0560

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A system-critical Windows NT file or directory has inappropriate permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0560.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0560
- https://www.cve.org/CVERecord?id=CVE-1999-0560

---

#### 346. CVE-1999-0570

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT is not using a password filter utility, e.g. PASSFILT.DLL.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0570.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0570
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0570

---

#### 347. CVE-1999-0577

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system's file audit policy does not log an event success or failure for non-critical files or directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0577.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0577
- https://www.cve.org/CVERecord?id=CVE-1999-0577

---

#### 348. CVE-1999-0578

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system's registry audit policy does not log an event success or failure for security-critical registry keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/228.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228

---

#### 349. CVE-1999-0579

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system's registry audit policy does not log an event success or failure for non-critical registry keys.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/228.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228

---

#### 350. CVE-1999-0580

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The HKEY_LOCAL_MACHINE key in a Windows NT system has inappropriate, system-critical permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0580.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0580
- https://www.cve.org/CVERecord?id=CVE-1999-0580

---

#### 351. CVE-1999-0581

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The HKEY_CLASSES_ROOT key in a Windows NT system has inappropriate, system-critical permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0581.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0581
- https://www.cve.org/CVERecord?id=CVE-1999-0581

---

#### 352. CVE-1999-0583

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
There is a one-way or two-way trust relationship between Windows NT domains.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/1284.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1284
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1284

---

#### 353. CVE-1999-0584

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT file system is not NTFS.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/195.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/195
- https://exchange.xforce.ibmcloud.com/vulnerabilities/195

---

#### 354. CVE-1999-0589

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A system-critical Windows NT registry key has inappropriate permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0589.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0589
- https://www.cve.org/CVERecord?id=CVE-1999-0589

---

#### 355. CVE-1999-0591

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An event log in Windows NT has inappropriate access permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0591.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0591
- https://www.cve.org/CVERecord?id=CVE-1999-0591

---

#### 356. CVE-1999-0592

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Logon box of a Windows NT system displays the name of the last user who logged in.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/1353.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1353
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1353

---

#### 357. CVE-1999-0593

**严重程度 / Severity**: N/A | CVSS: 4.9
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The default setting for the Winlogon key entry ShutdownWithoutLogon in Windows NT allows users with physical access to shut down a Windows NT system without logging in.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://osvdb.org/59333.

**参考链接 / References**:
- http://osvdb.org/59333
- http://technet.microsoft.com/en-us/library/cc722469.aspx
- http://www.microsoft.com/technet/archive/winntas/deploy/confeat/06wntpcc.mspx?mfr=true
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1291
- http://osvdb.org/59333

---

#### 358. CVE-1999-0594

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT system does not restrict access to removable media drives such as a floppy disk drive or CDROM drive.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/1294.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1294
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1294

---

#### 359. CVE-1999-0596

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT log file has an inappropriate maximum size or retention period.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/2577.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2577
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2577

---

#### 360. CVE-1999-0597

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT account policy does not forcibly disconnect remote users from the server when their logon hours expire.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/1343.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1343
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1343

---

#### 361. CVE-1999-0603

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
In Windows NT, an inappropriate user is a member of a group, e.g. Administrator, Backup Operators, Domain Admins, Domain Guests, Power Users, Print Operators, Replicators, System Operators, etc.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0603.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0603
- https://www.cve.org/CVERecord?id=CVE-1999-0603

---

#### 362. CVE-1999-0611

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A system-critical Windows NT registry key has an inappropriate value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0611.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0611
- https://www.cve.org/CVERecord?id=CVE-1999-0611

---

#### 363. CVE-1999-0623

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "The X Windows service is running.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor vendor advisory.

---

#### 364. CVE-1999-0659

**严重程度 / Severity**: N/A

**漏洞描述 / Description**:
Rejected reason: DO NOT USE THIS CANDIDATE NUMBER.  ConsultIDs: None.  Reason: this candidate is solely about a configuration that does not directly introduce security vulnerabilities, so it is more appropriate to cover under the Common Configuration Enumeration (CCE).  Notes: the former description is: "A Windows NT Primary Domain Controller (PDC) or Backup Domain Controller (BDC) is present.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor vendor advisory.

---

#### 365. CVE-1999-0664

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An application-critical Windows NT registry key has inappropriate permissions.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0664.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0664
- https://www.cve.org/CVERecord?id=CVE-1999-0664

---

#### 366. CVE-1999-0665

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An application-critical Windows NT registry key has an inappropriate value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0665.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0665
- https://www.cve.org/CVERecord?id=CVE-1999-0665

---

#### 367. CVE-1999-0391

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt, microsoft:terminal_server

**漏洞描述 / Description**:
The cryptographic challenge of SMB authentication in Windows 95 and Windows 98 can be reused, allowing an attacker to replay the response and impersonate a user.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://marc.info/?l=bugtraq&m=91552769809542&w=2.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=91552769809542&w=2
- https://marc.info/?l=bugtraq&m=91552769809542&w=2

---

#### 368. CVE-1999-0119

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 beta allows users to read and delete shares.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/11.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11

---

#### 369. CVE-1999-0357

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98

**漏洞描述 / Description**:
Windows 98 and other operating systems allows remote attackers to cause a denial of service via crafted "oshare" packets, possibly involving invalid fragmentation offsets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0357.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0357
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0357

---

#### 370. CVE-1999-1201

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Windows 95 and Windows 98 systems, when configured with multiple TCP/IP stacks bound to the same MAC address, allow remote attackers to cause a denial of service (traffic amplification) via a certain ICMP echo (ping) packet, which causes all stacks to send a ping response, aka TCP Chorusing.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=91849617221319&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=91849617221319&w=2
- http://www.securityfocus.com/bid/225
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7542
- http://marc.info/?l=ntbugtraq&m=91849617221319&w=2
- http://www.securityfocus.com/bid/225

---

#### 371. CVE-1999-0366

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
In some cases, Service Pack 4 for Windows NT 4.0 can allow access to network shares using a blank password, through a problem with a null NT hash value.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ214840.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ214840
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-004
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ214840
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-004

---

#### 372. CVE-1999-0404

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: smartmax_software:mailmax

**漏洞描述 / Description**:
Buffer overflow in the Mail-Max SMTP server for Windows systems allows remote command execution.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0404.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0404
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0404

---

#### 373. CVE-1999-0376

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Local users in Windows NT can obtain administrator privileges by changing the KnownDLLs list to reference malicious programs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-006.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-006
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-006

---

#### 374. CVE-1999-1254

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Windows 95, 98, and NT 4.0 allow remote attackers to cause a denial of service by spoofing ICMP redirect messages from a router, which causes Windows to change its routing tables.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=92099515709467&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92099515709467&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1947
- http://marc.info/?l=ntbugtraq&m=92099515709467&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1947

---

#### 375. CVE-1999-0382

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The screen saver in Windows NT does not verify that its security context has been changed properly, allowing attackers to run programs with elevated privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-008.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-008
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-008

---

#### 376. CVE-1999-0444

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Remote attackers can perform a denial of service in Windows machines using malicious ARP packets, forcing a message box display for each packet or filling up log files.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://marc.info/?l=bugtraq&m=92394891221029&w=2.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=92394891221029&w=2
- https://marc.info/?l=bugtraq&m=92394891221029&w=2

---

#### 377. CVE-1999-0229

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_information_server

**漏洞描述 / Description**:
Denial of service in Windows NT IIS server using ..\..

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0229.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0229
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0229

---

#### 378. CVE-1999-0716

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in Windows NT 4.0 help file utility via a malformed help file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231605.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231605
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-015
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231605
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-015

---

#### 379. CVE-1999-0755

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT RRAS and RAS clients cache a user's password even if the user has not selected the "Save password" option.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ230681.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ230681
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-017
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ230681
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-017

---

#### 380. CVE-1999-0723

**严重程度 / Severity**: N/A | CVSS: 7.1
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
The Windows NT Client Server Runtime Subsystem (CSRSS) can be subjected to a denial of service when all worker threads are waiting for user input.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ233323.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ233323
- http://www.ciac.org/ciac/bulletins/j-049.shtml
- http://www.securityfocus.com/bid/478
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-021
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ233323

---

#### 381. CVE-1999-1365

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT searches a user's home directory (%systemroot% by default) before other directories to find critical programs such as NDDEAGNT.EXE, EXPLORER.EXE, USERINIT.EXE or TASKMGR.EXE, which could allow local users to bypass access restrictions or gain privileges by placing a Trojan horse program into the root directory, which is writable by default.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=93069418400856&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=93069418400856&w=2
- http://marc.info/?l=ntbugtraq&m=93127894731200&w=2
- http://www.securityfocus.com/bid/515
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2336
- http://marc.info/?l=ntbugtraq&m=93069418400856&w=2

---

#### 382. CVE-1999-0726

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
An attacker can conduct a denial of service in Windows NT by executing a program with a malformed file image header.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ234557.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ234557
- http://www.securityfocus.com/bid/499
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-023
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ234557
- http://www.securityfocus.com/bid/499

---

#### 383. CVE-1999-0918

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt, microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
Denial of service in various Windows systems via malformed, fragmented IGMP packets.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238329.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238329
- http://www.securityfocus.com/bid/514
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-034
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238329
- http://www.securityfocus.com/bid/514

---

#### 384. CVE-1999-0728

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT user can disable the keyboard or mouse by directly calling the IOCTLs which control them.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ236359.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ236359
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-024
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ236359
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-024

---

#### 385. CVE-1999-0721

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in Windows NT Local Security Authority (LSA) through a malformed LSA request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231457.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231457
- http://www.ciac.org/ciac/bulletins/j-049.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-020
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231457
- http://www.ciac.org/ciac/bulletins/j-049.shtml

---

#### 386. CVE-1999-0224

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Denial of service in Windows NT messenger service through a long username.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0224.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0224
- https://www.cve.org/CVERecord?id=CVE-1999-0224

---

#### 387. CVE-1999-0680

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:terminal_server

**漏洞描述 / Description**:
Windows NT Terminal Server performs extra work when a client opens a new connection but before it is authenticated, allowing for a denial of service.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238600.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238600
- http://www.ciac.org/ciac/bulletins/j-057.shtml
- http://www.securityfocus.com/bid/571
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-028
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238600

---

#### 388. CVE-2000-0328

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 generates predictable random TCP initial sequence numbers (ISN), which allows remote attackers to perform spoofing and session hijacking.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/604.

**参考链接 / References**:
- http://www.securityfocus.com/bid/604
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=4.1.19990824165629.00abcb40%40192.168.124.1
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-046
- http://www.securityfocus.com/bid/604
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=4.1.19990824165629.00abcb40%40192.168.124.1

---

#### 389. CVE-1999-1356

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: compaq:smartstart

**漏洞描述 / Description**:
Compaq Integration Maintenance Utility as used in Compaq Insight Manager agent before SmartStart 4.50 modifies the legal notice caption (LegalNoticeCaption) and text (LegalNoticeText) in Windows NT, which could produce a legal notice that is in violation of the security policy.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93646669500991&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93646669500991&w=2
- http://marc.info/?l=ntbugtraq&m=93637792706047&w=2
- http://marc.info/?l=ntbugtraq&m=93759822830815&w=2
- http://www.iss.net/security_center/static/7763.php
- http://marc.info/?l=bugtraq&m=93646669500991&w=2

---

#### 390. CVE-1999-0886

**严重程度 / Severity**: N/A | CVSS: 9.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The security descriptor for RASMAN allows users to point to an alternate location via the Windows NT Service Control Manager.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ242294.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ242294
- http://www.securityfocus.com/bid/645
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-041
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ242294
- http://www.securityfocus.com/bid/645

---

#### 391. CVE-1999-0909

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_95, microsoft:windows_98se, microsoft:terminal_server

**漏洞描述 / Description**:
Multihomed Windows systems allow a remote attacker to bypass IP source routing restrictions via a malformed packet with IP options, aka the "Spoofed Route Pointer" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238453.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238453
- http://www.securityfocus.com/bid/646
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-038
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238453
- http://www.securityfocus.com/bid/646

---

#### 392. CVE-1999-1454

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: macromedia:matrix_screen_saver

**漏洞描述 / Description**:
Macromedia "The Matrix" screen saver on Windows 95 with the "Password protected" option enabled allows attackers with physical access to the machine to bypass the password prompt by pressing the ESC (Escape) key.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93915027622690&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93915027622690&w=2
- http://marc.info/?l=bugtraq&m=93915027622690&w=2

---

#### 393. CVE-1999-1234

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
LSA (LSASS.EXE) in Windows NT 4.0 allows remote attackers to cause a denial of service via a NULL policy handle in a call to (1) SamrOpenDomain, (2) SamrEnumDomainUsers, and (3) SamrQueryDomainInfo.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=94096671308565&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=94096671308565&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3293
- http://marc.info/?l=ntbugtraq&m=94096671308565&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3293

---

#### 394. CVE-1999-1531

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: ibm:homepageprint

**漏洞描述 / Description**:
Buffer overflow in IBM HomePagePrint 1.0.7 for Windows98J allows a malicious Web site to execute arbitrary code on a viewer's system via a long IMG_SRC HTML tag.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94157187815629&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94157187815629&w=2
- http://www.iss.net/security_center/static/7767.php
- http://www.securityfocus.com/bid/763
- http://marc.info/?l=bugtraq&m=94157187815629&w=2
- http://www.iss.net/security_center/static/7767.php

---

#### 395. CVE-1999-0898

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflows in Windows NT 4.0 print spooler allow remote attackers to gain privileges or cause a denial of service via a malformed spooler request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/768
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-047
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/768

---

#### 396. CVE-1999-0899

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Windows NT 4.0 print spooler allows a local user to execute arbitrary commands due to inappropriate permissions that allow the user to specify an alternate print provider.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/769
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-047
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/769

---

#### 397. CVE-1999-1065

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: palm_pilot:hotsync_manager

**漏洞描述 / Description**:
Palm Pilot HotSync Manager 3.0.4 in Windows 98 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long string to port 14238 while the manager is in network mode.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94175465525422&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94175465525422&w=2
- http://marc.info/?l=bugtraq&m=94175465525422&w=2

---

#### 398. CVE-2000-0330

**严重程度 / Severity**: N/A | CVSS: 7.6
**受影响产品 / Affected Products**: microsoft:windows_95, microsoft:windows_98

**漏洞描述 / Description**:
The networking software in Windows 95 and Windows 98 allows remote attackers to execute commands via a long file name string, aka the "File Access URL" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-049.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-049
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-049

---

#### 399. CVE-1999-1110

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:internet_explorer

**漏洞描述 / Description**:
Windows Media Player ActiveX object as used in Internet Explorer 5.0 returns a specific error code when a file does not exist, which allows remote malicious web sites to determine the existence of files on the client.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/34675.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/34675
- http://www.securityfocus.com/bid/793
- http://www.securityfocus.com/archive/1/34675
- http://www.securityfocus.com/bid/793

---

#### 400. CVE-1999-0987

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT does not properly download a system policy if the domain user logs into the domain with a space at the end of the domain name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237923.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237923
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237923

---

#### 401. CVE-1999-1189

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: netscape:navigator, netscape:communicator

**漏洞描述 / Description**:
Buffer overflow in Netscape Navigator/Communicator 4.7 for Windows 95 and Windows 98 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long argument after the ? character in a URL that references an .asp, .cgi, .html, or .pl file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/36306.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/36306
- http://www.securityfocus.com/archive/1/36608
- http://www.securityfocus.com/bid/822
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7884
- http://www.securityfocus.com/archive/1/36306

---

#### 402. CVE-1999-0387

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_95

**漏洞描述 / Description**:
A legacy credential caching mechanism used in Windows 95 and Windows 98 systems allows attackers to read plaintext network passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ168115.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ168115
- http://www.securityfocus.com/bid/829
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-052
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ168115
- http://www.securityfocus.com/bid/829

---

#### 403. CVE-1999-0839

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:ie

**漏洞描述 / Description**:
Windows NT Task Scheduler installed with Internet Explorer 5 allows a user to gain privileges by modifying the job after it has been scheduled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246972.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246972
- http://www.securityfocus.com/bid/828
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-051
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246972
- http://www.securityfocus.com/bid/828

---

#### 404. CVE-1999-0824

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT user can use SUBST to map a drive letter to a folder, which is not unmapped after the user logs off, potentially allowing that user to modify the location of folders accessed by later users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/833.

**参考链接 / References**:
- http://www.securityfocus.com/bid/833
- http://www.securityfocus.com/bid/833

---

#### 405. CVE-1999-0975

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_95, microsoft:windows_nt

**漏洞描述 / Description**:
The Windows help system can allow a local user to execute commands as another user by editing a table of contents metafile with a .CNT extension and modifying the topic action to include the commands to be executed when the .hlp file is accessed.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/868.

**参考链接 / References**:
- http://www.securityfocus.com/bid/868
- http://www.securityfocus.com/bid/868

---

#### 406. CVE-1999-0994

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT with SYSKEY reuses the keystream that is used for encrypting SAM password hashes, allowing an attacker to crack passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248183.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248183
- http://www.securityfocus.com/bid/873
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-056
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248183
- http://www.securityfocus.com/bid/873

---

#### 407. CVE-1999-0995

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT Local Security Authority (LSA) allows remote attackers to cause a denial of service via malformed arguments to the LsaLookupSids function which looks up the SID, aka "Malformed Security Identifier Request."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248185.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248185
- http://www.securityfocus.com/bid/875
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-057
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248185
- http://www.securityfocus.com/bid/875

---

#### 408. CVE-2000-0119

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: symantec:norton_antivirus, mcafee:virusscan

**漏洞描述 / Description**:
The default configurations for McAfee Virus Scan and Norton Anti-Virus virus checkers do not check files in the RECYCLED folder that is used by the Windows Recycle Bin utility, which allows attackers to store malicious code without detection.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=94936267131123&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94936267131123&w=2
- http://marc.info/?l=bugtraq&m=94936267131123&w=2

---

#### 409. CVE-1999-0815

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Memory leak in SNMP agent in Windows NT 4.0 before SP5 allows remote attackers to conduct a denial of service (memory exhaustion) via a large number of queries.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q196/2/70.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q196/2/70.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1974
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A952
- http://support.microsoft.com/support/kb/articles/q196/2/70.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1974

---

#### 410. CVE-1999-1104

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_95

**漏洞描述 / Description**:
Windows 95 uses weak encryption for the password list (.pwl) file used when password caching is enabled, which allows local users to gain privileges by decrypting the passwords.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=87602167418931&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602167418931&w=2
- http://marc.info/?l=bugtraq&m=88536273725787&w=2
- http://marc.info/?l=ntbugtraq&m=88540877601866&w=2
- http://support.microsoft.com/support/kb/articles/q140/5/57.asp
- http://www.iss.net/security_center/static/71.php

---

#### 411. CVE-1999-1105

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_95

**漏洞描述 / Description**:
Windows 95, when Remote Administration and File Sharing for NetWare Networks is enabled, creates a share (C$) when an administrator logs in remotely, which allows remote attackers to read arbitrary files by mapping the network drive.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.iss.net/security_center/static/7231.php.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7231.php
- http://www.net-security.sk/bugs/NT/netware1.html
- http://www.zdnet.com/eweek/reviews/1016/tr42bug.html
- http://www.iss.net/security_center/static/7231.php
- http://www.net-security.sk/bugs/NT/netware1.html

---

#### 412. CVE-1999-1127

**严重程度 / Severity**: HIGH | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 does not properly shut down invalid named pipe RPC connections, which allows remote attackers to cause a denial of service (resource exhaustion) via a series of connections containing malformed data, aka the "Named Pipes Over RPC" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q195/7/33.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q195/7/33.asp
- http://www.iss.net/security_center/static/523.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-017
- http://support.microsoft.com/support/kb/articles/Q195/7/33.asp
- http://www.iss.net/security_center/static/523.php

---

#### 413. CVE-1999-1132

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 allows remote attackers to cause a denial of service (crash) via extra source routing data such as (1) a Routing Information Field (RIF) field with a hop count greater than 7, or (2) a list containing duplicate Token Ring IDs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=90763508011966&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90763508011966&w=2
- http://marc.info/?l=ntbugtraq&m=90760603030452&w=2
- http://support.microsoft.com/support/kb/articles/Q179/1/57.asp
- http://www.iss.net/security_center/static/1399.php
- http://marc.info/?l=bugtraq&m=90763508011966&w=2

---

#### 414. CVE-1999-1157

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Tcpip.sys in Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service via an ICMP Subnet Mask Address Request packet, when certain multiple IP addresses are bound to the same network interface.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q192/7/74.ASP.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q192/7/74.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3894
- http://support.microsoft.com/support/kb/articles/Q192/7/74.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3894

---

#### 415. CVE-1999-1206

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: systemsoft:systemwizard

**漏洞描述 / Description**:
SystemSoft SystemWizard package in HP Pavilion PC with Windows 98, and possibly other platforms and operating systems, installs two ActiveX controls that are marked as safe for scripting, which allows remote attackers to execute arbitrary commands via a malicious web page that references (1) the Launch control, or (2) the RegObj control.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=93336970231857&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93336970231857&w=2
- http://www.securityfocus.com/bid/555
- http://www.systemsoft.com/l-2/l-3/support-systemwizard.htm
- http://marc.info/?l=bugtraq&m=93336970231857&w=2
- http://www.securityfocus.com/bid/555

---

#### 416. CVE-1999-1222

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Netbt.sys in Windows NT 4.0 allows remote malicious DNS servers to cause a denial of service (crash) by returning 0.0.0.0 as the IP address for a DNS host name lookup.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q188/5/71.ASP.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q188/5/71.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3893
- http://support.microsoft.com/support/kb/articles/Q188/5/71.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3893

---

#### 417. CVE-1999-1294

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Office Shortcut Bar (OSB) in Windows 3.51 enables backup and restore permissions, which are inherited by programs such as File Manager that are started from the Shortcut Bar, which could allow local users to read folders for which they do not have permission.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q146/6/04.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q146/6/04.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/562
- http://support.microsoft.com/support/kb/articles/q146/6/04.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/562

---

#### 418. CVE-1999-1316

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Passfilt.dll in Windows NT SP2 allows users to create a password that contains the user's name, which could make it easier for an attacker to guess.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/Q247/9/75.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q247/9/75.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7391
- http://support.microsoft.com/support/kb/articles/Q247/9/75.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7391

---

#### 419. CVE-1999-1317

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 SP4 and earlier allows local users to gain privileges by modifying the symbolic link table in the \?? object folder using a different case letter (upper or lower) to point to a different device.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=92127046701349&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92127046701349&w=2
- http://marc.info/?l=ntbugtraq&m=92162979530341&w=2
- http://support.microsoft.com/support/kb/articles/q222/1/59.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7398
- http://marc.info/?l=ntbugtraq&m=92127046701349&w=2

---

#### 420. CVE-1999-1358

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
When an administrator in Windows NT or Windows 2000 changes a user policy, the policy is not properly updated if the local ntconfig.pol is not writable by the user, which could allow local users to bypass restrictions that would otherwise be enforced by the policy, possibly by changing the policy file to be read-only.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q157/6/73.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q157/6/73.asp
- http://www.iss.net/security_center/static/7400.php
- http://support.microsoft.com/support/kb/articles/q157/6/73.asp
- http://www.iss.net/security_center/static/7400.php

---

#### 421. CVE-1999-1359

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
When the Ntconfig.pol file is used on a server whose name is longer than 13 characters, Windows NT does not properly enforce policies for global groups, which could allow users to bypass restrictions that were intended by those policies.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q163/8/75.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/8/75.asp
- http://www.iss.net/security_center/static/7401.php
- http://support.microsoft.com/support/kb/articles/q163/8/75.asp
- http://www.iss.net/security_center/static/7401.php

---

#### 422. CVE-1999-1360

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 allows local users to cause a denial of service via a user mode application that closes a handle that was opened in kernel mode, which causes a crash when the kernel attempts to close the handle.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q160/6/50.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q160/6/50.asp
- http://www.iss.net/security_center/static/7402.php
- http://support.microsoft.com/support/kb/articles/q160/6/50.asp
- http://www.iss.net/security_center/static/7402.php

---

#### 423. CVE-1999-1362

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Win32k.sys in Windows NT 4.0 before SP2 allows local users to cause a denial of service (crash) by calling certain WIN32K functions with incorrect parameters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q160/6/01.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q160/6/01.asp
- http://www.iss.net/security_center/static/7403.php
- http://support.microsoft.com/support/kb/articles/q160/6/01.asp
- http://www.iss.net/security_center/static/7403.php

---

#### 424. CVE-1999-1363

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 3.51 and 4.0 allow local users to cause a denial of service (crash) by running a program that creates a large number of locks on a file, which exhausts the NonPagedPool.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q163/1/43.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/1/43.asp
- http://www.iss.net/security_center/static/7405.php
- http://support.microsoft.com/support/kb/articles/q163/1/43.asp
- http://www.iss.net/security_center/static/7405.php

---

#### 425. CVE-1999-1364

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT 4.0 allows local users to cause a denial of service (crash) via an illegal kernel mode address to the functions (1) GetThreadContext or (2) SetThreadContext.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q142/6/53.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q142/6/53.asp
- http://www.iss.net/security_center/static/7421.php
- http://support.microsoft.com/support/kb/articles/q142/6/53.asp
- http://www.iss.net/security_center/static/7421.php

---

#### 426. CVE-1999-1452

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
GINA in Windows NT 4.0 allows attackers with physical access to display a portion of the clipboard of the user who has locked the workstation by pasting (CTRL-V) the contents into the username prompt.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=91788829326419&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91788829326419&w=2
- http://marc.info/?l=ntbugtraq&m=91764169410814&w=2
- http://marc.info/?l=ntbugtraq&m=91822011021558&w=2
- http://support.microsoft.com/support/kb/articles/q214/8/02.asp
- http://www.securityfocus.com/bid/198

---

#### 427. CVE-1999-1455

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
RSH service utility RSHSVC in Windows NT 3.5 through 4.0 does not properly restrict access as specified in the .Rhosts file when a user comes from an authorized host, which could allow unauthorized users to access the service by logging in from an authorized host.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q158/3/20.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q158/3/20.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7422
- http://support.microsoft.com/support/kb/articles/q158/3/20.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7422

---

#### 428. CVE-1999-1476

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: intel:pentium, intel:pentuim

**漏洞描述 / Description**:
A bug in Intel Pentium processor (MMX and Overdrive) allows local users to cause a denial of service (hang) in Intel-based operating systems such as Windows NT and Windows 95, via an invalid instruction, aka the "Invalid Operand with Locked CMPXCHG8B Instruction" problem.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/support/kb/articles/q163/8/52.asp.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/8/52.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/704
- http://support.microsoft.com/support/kb/articles/q163/8/52.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/704

---

#### 429. CVE-1999-1584

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: sun:sunos, sun:openwindows

**漏洞描述 / Description**:
Unknown vulnerability in (1) loadmodule, and (2) modload if modload is installed with setuid/setgid privileges, in SunOS 4.1.1 through 4.1.3c, and Open Windows 3.0, allows local users to gain root privileges via environment variables, a different vulnerability than CVE-1999-1586.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://sunsolve.sun.com/search/document.do?assetkey=1-22-00124-1.

**参考链接 / References**:
- http://sunsolve.sun.com/search/document.do?assetkey=1-22-00124-1
- http://www.cert.org/advisories/CA-1993-18.html
- http://sunsolve.sun.com/search/document.do?assetkey=1-22-00124-1
- http://www.cert.org/advisories/CA-1993-18.html

---

#### 430. CVE-2000-0070

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
NtImpersonateClientOfPort local procedure call in Windows NT 4.0 allows local users to gain privileges, aka "Spoofed LPC Port Request."

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ247869.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ247869
- http://www.bindview.com/security/advisory/adv_NtImpersonate.html
- http://www.securityfocus.com/bid/934
- http://xforce.iss.net/search.php3?type=2&pattern=nt-spoofed-lpc-port
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-003

---

#### 431. CVE-1999-0595

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000, microsoft:windows_nt

**漏洞描述 / Description**:
A Windows NT system does not clear the system page file during shutdown, which might allow sensitive information to be recorded.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://exchange.xforce.ibmcloud.com/vulnerabilities/216.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/216
- https://exchange.xforce.ibmcloud.com/vulnerabilities/216

---

#### 432. CVE-2000-0121

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Recycle Bin utility in Windows NT and Windows 2000 allows local users to read or modify files by creating a subdirectory with the victim's SID in the recycler directory, aka the "Recycle Bin Creation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248399.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248399
- http://www.securityfocus.com/bid/963
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-007
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248399
- http://www.securityfocus.com/bid/963

---

#### 433. CVE-2000-0197

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Windows NT scheduler uses the drive mapping of the interactive user who is currently logged onto the system, which allows the local user to gain privileges by providing a Trojan horse batch file in place of the original batch file.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/current/0202.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/current/0202.html
- http://www.securityfocus.com/bid/1050
- http://archives.neohapsis.com/archives/ntbugtraq/current/0202.html
- http://www.securityfocus.com/bid/1050

---

#### 434. CVE-2000-0222

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The installation for Windows 2000 does not activate the Administrator password until the system has rebooted, which allows remote attackers to connect to the ADMIN$ share without a password until the reboot occurs.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/990.

**参考链接 / References**:
- http://www.securityfocus.com/bid/990
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000215155750.M4500%40safe.hsc.fr
- http://www.securityfocus.com/bid/990
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000215155750.M4500%40safe.hsc.fr

---

#### 435. CVE-2000-0155

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_95, microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT Autorun executes the autorun.inf file on non-removable media, which allows local attackers to specify an alternate program to execute when other users access a drive.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/993.

**参考链接 / References**:
- http://www.securityfocus.com/bid/993
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=000701bf79cd%24fdb5a620%244c4342a6%40mightye.org
- http://www.securityfocus.com/bid/993
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=000701bf79cd%24fdb5a620%244c4342a6%40mightye.org

---

#### 436. CVE-2000-0211

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
The Windows Media server allows remote attackers to cause a denial of service via a series of client handshake packets that are sent in an improper sequence, aka the "Misordered Windows Media Services Handshake" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1000.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1000
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-013
- http://www.securityfocus.com/bid/1000
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-013

---

#### 437. CVE-2000-0298

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The unattended installation of Windows 2000 with the OEMPreinstall option sets insecure permissions for the All Users and Default Users directories.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0027.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0027.html
- http://www.securityfocus.com/bid/1758
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4278
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0027.html
- http://www.securityfocus.com/bid/1758

---

#### 438. CVE-1999-0701

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
After an unattended installation of Windows NT 4.0, an installation file could include sensitive information such as the local Administrator password.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ173039.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ173039
- http://www.securityfocus.com/bid/626
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-036
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ173039
- http://www.securityfocus.com/bid/626

---

#### 439. CVE-2000-0259

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:terminal_server

**漏洞描述 / Description**:
The default permissions for the Cryptography\Offload registry key used by the OffloadModExpo in Windows NT 4.0 allows local users to obtain compromise the cryptographic keys of other users.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1105.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1105
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-024
- http://www.securityfocus.com/bid/1105
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-024

---

#### 440. CVE-2000-0311

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The Windows 2000 domain controller allows a malicious user to modify Active Directory information by modifying an unprotected attribute, aka the "Mixed Object Access" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1145.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1145
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-026
- http://www.securityfocus.com/bid/1145
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-026

---

#### 441. CVE-2000-0347

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_95

**漏洞描述 / Description**:
Windows 95 and Windows 98 allow a remote attacker to cause a denial of service via a NetBIOS session request packet with a NULL source name.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=ntbugtraq&m=95737580922397&w=2.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=95737580922397&w=2
- http://www.securityfocus.com/bid/1163
- http://marc.info/?l=ntbugtraq&m=95737580922397&w=2
- http://www.securityfocus.com/bid/1163

---

#### 442. CVE-2000-0420

**严重程度 / Severity**: N/A | CVSS: 7.2
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The default configuration of SYSKEY in Windows 2000 stores the startup key in the registry, which could allow an attacker tor ecover it and use it to decrypt Encrypted File System (EFS) data.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0112.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0112.html
- http://www.securityfocus.com/bid/1198
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0112.html
- http://www.securityfocus.com/bid/1198

---

#### 443. CVE-1999-0980

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Windows NT Service Control Manager (SCM) allows remote attackers to cause a denial of service via a malformed argument in a resource enumeration request.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246045.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246045
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-055
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246045
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-055

---

#### 444. CVE-2000-0305

**严重程度 / Severity**: N/A | CVSS: 7.8
**受影响产品 / Affected Products**: be:beos, microsoft:windows_nt, microsoft:windows_2000, microsoft:windows_98, microsoft:windows_95

**漏洞描述 / Description**:
Windows 95, Windows 98, Windows 2000, Windows NT 4.0, and Terminal Server systems allow a remote attacker to cause a denial of service by sending a large number of identical fragmented IP packets, aka jolt2 or the "IP Fragment Reassembly" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1236.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1236
- http://www.securityfocus.com/templates/advisory.html?id=2240
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-029
- http://www.securityfocus.com/bid/1236
- http://www.securityfocus.com/templates/advisory.html?id=2240

---

#### 445. CVE-2000-0403

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The CIFS Computer Browser service on Windows NT 4.0 allows a remote attacker to cause a denial of service by sending a large number of host announcement requests to the master browse tables, aka the "HostAnnouncement Flooding" or "HostAnnouncement Frame" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=263307.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=263307
- http://www.securityfocus.com/bid/1261
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-036
- http://www.microsoft.com/technet/support/kb.asp?ID=263307
- http://www.securityfocus.com/bid/1261

---

#### 446. CVE-2000-0505

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: ibm:http_server, apache:http_server

**漏洞描述 / Description**:
The Apache 1.3.x HTTP server for Windows platforms allows remote attackers to list directory contents by requesting a URL containing a large number of / characters.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1284.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1284
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.BSF.4.20.0006031912360.45740-100000%40alive.znep.com
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4575
- https://lists.apache.org/thread.html/r5419c9ba0951ef73a655362403d12bb8d10fab38274deb3f005816f5%40%3Ccvs.httpd.apache.org%3E
- https://lists.apache.org/thread.html/r5f9c22f9c28adbd9f00556059edc7b03a5d5bb71d4bb80257c0d34e4%40%3Ccvs.httpd.apache.org%3E

---

#### 447. CVE-2000-0487

**严重程度 / Severity**: N/A | CVSS: 3.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The Protected Store in Windows 2000 does not properly select the strongest encryption when available, which causes it to use a default of 40-bit encryption instead of 56-bit DES encryption, aka the "Protected Store Key Length" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1295.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1295
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-032
- http://www.securityfocus.com/bid/1295
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-032

---

#### 448. CVE-2000-0544

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Windows NT and Windows 2000 hosts allow a remote attacker to cause a denial of service via malformed DCE/RPC SMBwriteX requests that contain an invalid data length.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0231.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0231.html
- http://www.securityfocus.com/bid/1304
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0231.html
- http://www.securityfocus.com/bid/1304

---

#### 449. CVE-2000-0377

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Remote Registry server in Windows NT 4.0 allows local authenticated users to cause a denial of service via a malformed request, which causes the winlogon process to fail, aka the "Remote Registry Access Authentication" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=264684.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=264684
- http://www.securityfocus.com/bid/1331
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-040
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1021
- http://www.microsoft.com/technet/support/kb.asp?ID=264684

---

#### 450. CVE-2000-0475

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Windows 2000 allows a local user process to access another user's desktop within the same windows station, aka the "Desktop Separation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1350.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1350
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-020
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4714
- http://www.securityfocus.com/bid/1350
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-020

---

#### 451. CVE-2000-0612

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_98, microsoft:windows_95

**漏洞描述 / Description**:
Windows 95 and Windows 98 do not properly process spoofed ARP packets, which allows remote attackers to overwrite static entries in the cache table.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1406.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1406
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=395B7E64.9FB3D4DB%40starzetz.de
- http://www.securityfocus.com/bid/1406
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=395B7E64.9FB3D4DB%40starzetz.de

---

#### 452. CVE-2000-0580

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Windows 2000 Server allows remote attackers to cause a denial of service by sending a continuous stream of binary zeros to various TCP and UDP ports, which significantly increases the CPU utilization.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1415.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1415
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161935.4619B-100000%40fjord.fscinternet.com
- http://www.securityfocus.com/bid/1415
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161935.4619B-100000%40fjord.fscinternet.com

---

#### 453. CVE-2000-0581

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Windows 2000 Telnet Server allows remote attackers to cause a denial of service by sending a continuous stream of binary zeros, which causes the server to crash.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1414.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1414
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161841.4619A-100000%40fjord.fscinternet.com
- http://www.securityfocus.com/bid/1414
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161841.4619A-100000%40fjord.fscinternet.com

---

#### 454. CVE-1999-0585

**严重程度 / Severity**: N/A | CVSS: 2.1
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
A Windows NT administrator account has the default name of Administrator.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor https://www.cve.org/CVERecord?id=CVE-1999-0585.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0585
- https://www.cve.org/CVERecord?id=CVE-1999-0585

---

#### 455. CVE-2000-0663

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The registry entry for the Windows Shell executable (Explorer.exe) in Windows NT and Windows 2000 uses a relative path name, which allows local users to execute arbitrary commands by inserting a Trojan Horse named Explorer.exe into the %Systemdrive% directory, aka the "Relative Shell Path" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.microsoft.com/technet/support/kb.asp?ID=269049.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=269049
- http://www.securityfocus.com/bid/1507
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-052
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5040
- http://www.microsoft.com/technet/support/kb.asp?ID=269049

---

#### 456. CVE-2000-0737

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The Service Control Manager (SCM) in Windows 2000 creates predictable named pipes, which allows a local user with console access to gain administrator privileges, aka the "Service Control Manager Named Pipe Impersonation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1535.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1535
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-053
- http://www.securityfocus.com/bid/1535
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-053

---

#### 457. CVE-2000-0830

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:webtv

**漏洞描述 / Description**:
annclist.exe in webTV for Windows allows remote attackers to cause a denial of service by via a large, malformed UDP packet to ports 22701 through 22705.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/81852.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/81852
- http://www.securityfocus.com/bid/1671
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-074
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5216
- http://www.securityfocus.com/archive/1/81852

---

#### 458. CVE-2000-0834

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The Windows 2000 telnet client attempts to perform NTLM authentication by default, which allows remote attackers to capture and replay the NTLM challenge/response via a telnet:// URL that points to the malicious server, aka the "Windows 2000 Telnet Client NTLM Authentication" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2000/a091400-1.txt.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a091400-1.txt
- http://www.securityfocus.com/bid/1683
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-067
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5242
- http://www.atstake.com/research/advisories/2000/a091400-1.txt

---

#### 459. CVE-2000-0851

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in the Still Image Service in Windows 2000 allows local users to gain additional privileges via a long WM_USER message, aka the "Still Image Service Privilege Escalation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2000/a090700-1.txt.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a090700-1.txt
- http://www.securityfocus.com/bid/1651
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-065
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5203
- http://www.atstake.com/research/advisories/2000/a090700-1.txt

---

#### 460. CVE-2000-1003

**严重程度 / Severity**: N/A | CVSS: 2.6
**受影响产品 / Affected Products**: microsoft:windows_98se, microsoft:windows_98, microsoft:windows_95

**漏洞描述 / Description**:
NETBIOS client in Windows 95 and Windows 98 allows a remote attacker to cause a denial of service by changing a file sharing service to return an unknown driver type, which causes the client to crash.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/139511.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/139511
- http://www.securityfocus.com/bid/1794
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5370
- http://www.securityfocus.com/archive/1/139511
- http://www.securityfocus.com/bid/1794

---

#### 461. CVE-2000-1034

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Buffer overflow in the System Monitor ActiveX control in Windows 2000 allows remote attackers to execute arbitrary commands via a long LogFileName parameter in HTML source code, aka the "ActiveX Parameter Validation" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97349782305448&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97349782305448&w=2
- http://www.securityfocus.com/bid/1899
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-085
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5467
- http://marc.info/?l=bugtraq&m=97349782305448&w=2

---

#### 462. CVE-2000-1060

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: xfree86_project:xfce

**漏洞描述 / Description**:
The default configuration of XFCE 3.5.1 bypasses the Xauthority access control mechanism with an "xhost + localhost" command in the xinitrc program, which allows local users to sniff X Windows traffic and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/bugtraq/2000-10/0022.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0022.html
- http://www.securityfocus.com/bid/1736
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5305
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0022.html
- http://www.securityfocus.com/bid/1736

---

#### 463. CVE-2000-1071

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: netscape:iplanet_ical

**漏洞描述 / Description**:
The GUI installation for iCal 2.1 Patch 2 disables access control for the X server using an "xhost +" command, which allows remote attackers to monitor X Windows events and gain privileges.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.atstake.com/research/advisories/2000/a100900-1.txt.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a100900-1.txt
- http://www.osvdb.org/7213
- http://www.securityfocus.com/bid/1767
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5752
- http://www.atstake.com/research/advisories/2000/a100900-1.txt

---

#### 464. CVE-1999-1579

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Cenroll ActiveX control (xenroll.dll) for Terminal Server Editions of Windows NT 4.0 and Windows NT Server 4.0 before SP6 allows remote attackers to cause a denial of service (resource consumption) by creating a large number of arbitrary files on the target machine.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B242366.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B242366
- http://www.kb.cert.org/vuls/id/3062
- http://www.securityfocus.com/bid/6827
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7107
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B242366

---

#### 465. CVE-2000-0933

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
The Input Method Editor (IME) in the Simplified Chinese version of Windows 2000 does not disable access to privileged functionality that should normally be restricted, which allows local users to gain privileges, aka the "Simplified Chinese IME State Recognition" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1729.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1729
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-069
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5301
- http://www.securityfocus.com/bid/1729
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-069

---

#### 466. CVE-2000-0979

**严重程度 / Severity**: N/A | CVSS: 6.4
**受影响产品 / Affected Products**: microsoft:windows_98se, microsoft:windows_98, microsoft:windows_me, microsoft:windows_95

**漏洞描述 / Description**:
File and Print Sharing service in Windows 95, Windows 98, and Windows Me does not properly check the password for a file share, which allows remote attackers to bypass share access controls by sending a 1-byte password that matches the first character of the real password, aka the "Share Level Password" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=97147777618139&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97147777618139&w=2
- http://www.securityfocus.com/bid/1780
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-072
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5395
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A996

---

#### 467. CVE-2000-0991

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: hilgraeve:hyperterminal

**漏洞描述 / Description**:
Buffer overflow in Hilgraeve, Inc. HyperTerminal client on Windows 98, ME, and 2000 allows remote attackers to execute arbitrary commands via a long telnet URL, aka the "HyperTerminal Buffer Overflow" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/1815.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1815
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-079
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5387
- http://www.securityfocus.com/bid/1815
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-079

---

#### 468. CVE-2000-1227

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
Windows NT 4.0 and Windows 2000 hosts allow remote attackers to cause a denial of service (unavailable connections) by sending multiple SMB SMBnegprots requests but not reading the response that is sent back.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/63322.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/63322
- http://www.securityfocus.com/bid/1301
- http://www.securityfocus.com/archive/1/63322
- http://www.securityfocus.com/bid/1301

---

#### 469. CVE-2000-1105

**严重程度 / Severity**: N/A | CVSS: 4.3
**受影响产品 / Affected Products**: microsoft:indexing_service

**漏洞描述 / Description**:
The ixsso.query ActiveX Object is marked as safe for scripting, which allows malicious web site operators to embed a script that remotely determines the existence of files on visiting Windows 2000 systems that have Indexing Services enabled.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0074.html.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0074.html
- http://www.securityfocus.com/archive/1/144270
- http://www.securityfocus.com/bid/1933
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0074.html
- http://www.securityfocus.com/archive/1/144270

---

#### 470. CVE-2000-1111

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Telnet Service for Windows 2000 Professional does not properly terminate incomplete connection attempts, which allows remote attackers to cause a denial of service by connecting to the server and not providing any input.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/147914.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/147914
- http://www.securityfocus.com/bid/2018
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5598
- http://www.securityfocus.com/archive/1/147914
- http://www.securityfocus.com/bid/2018

---

#### 471. CVE-2000-1149

**严重程度 / Severity**: N/A | CVSS: 7.5
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
Buffer overflow in RegAPI.DLL used by Windows NT 4.0 Terminal Server allows remote attackers to execute arbitrary commands via a long username, aka the "Terminal Server Login Buffer Overflow" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/archive/1/143991.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/143991
- http://www.securityfocus.com/bid/1924
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-087
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5489
- http://www.securityfocus.com/archive/1/143991

---

#### 472. CVE-2001-0006

**严重程度 / Severity**: HIGH | CVSS: 7.1
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The Winsock2ProtocolCatalogMutex mutex in Windows NT 4.0 has inappropriate Everyone/Full Control permissions, which allows local users to modify the permissions to "No Access" and disable Winsock network connectivity to cause a denial of service, aka the "Winsock Mutex" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://marc.info/?l=bugtraq&m=98075221915234&w=2.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98075221915234&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-003
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6006
- http://marc.info/?l=bugtraq&m=98075221915234&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-003

---

#### 473. CVE-2001-0014

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_2000

**漏洞描述 / Description**:
Remote Data Protocol (RDP) in Windows 2000 Terminal Service does not properly handle certain malformed packets, which allows remote attackers to cause a denial of service, aka the "Invalid RDP Data" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2326.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2326
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-006
- http://www.securityfocus.com/bid/2326
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-006

---

#### 474. CVE-2001-0083

**严重程度 / Severity**: N/A | CVSS: 5.0
**受影响产品 / Affected Products**: microsoft:windows_media_services

**漏洞描述 / Description**:
Windows Media Unicast Service in Windows Media Services 4.0 and 4.1 does not properly shut down some types of connections, producing a memory leak that allows remote attackers to cause a denial of service via a series of severed connections, aka the "Severed Windows Media Server Connection" vulnerability.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ281256.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ281256
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-097
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5785
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ281256
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-097

---

#### 475. CVE-2001-0045

**严重程度 / Severity**: N/A | CVSS: 10.0
**受影响产品 / Affected Products**: microsoft:windows_nt

**漏洞描述 / Description**:
The default permissions for the RAS Administration key in Windows NT 4.0 allows local users to execute arbitrary commands by changing the value to point to a malicious DLL, aka one of the "Registry Permissions" vulnerabilities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2064.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2064
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5671
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A500
- http://www.securityfocus.com/bid/2064

---

#### 476. CVE-2001-0046

**严重程度 / Severity**: N/A | CVSS: 4.6
**受影响产品 / Affected Products**: microsoft:windows_nt, microsoft:windows_2000

**漏洞描述 / Description**:
The default permissions for the SNMP Parameters registry key in Windows NT 4.0 allows remote attackers to read and possibly modify the SNMP community strings to obtain sensitive information or modify network configuration, aka one of the "Registry Permissions" vulnerabilities.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.securityfocus.com/bid/2066.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2066
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5672
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A139
- http://www.securityfocus.com/bid/2066

---

#### 477. CVE-1999-0718

**严重程度 / Severity**: N/A | CVSS: 6.2
**受影响产品 / Affected Products**: ibm:gina

**漏洞描述 / Description**:
IBM GINA, when used for OS/2 domain authentication of Windows NT users, allows local users to gain administrator privileges by changing the GroupMapping registry key.

**补丁信息 / Patch Info**:
Apply patch from vendor. Monitor http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind9908&L=ntbugtraq&F=&S=&P=5534.

**参考链接 / References**:
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind9908&L=ntbugtraq&F=&S=&P=5534
- http://www.securityfocus.com/bid/608
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3166
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind9908&L=ntbugtraq&F=&S=&P=5534
- http://www.securityfocus.com/bid/608

---

#### 478. [Microsoft] CVE-2026-7355 - Chromium: CVE-2026-7355 Use after free in Media

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7355

---

#### 479. [Microsoft] CVE-2026-7340 - Chromium: CVE-2026-7340 Integer overflow in ANGLE

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7340

---

#### 480. [Microsoft] CVE-2026-7339 - Chromium: CVE-2026-7339 Heap buffer overflow in WebRTC

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7339

---

#### 481. [Microsoft] CVE-2026-7341 - Chromium: CVE-2026-7341 Use after free in WebRTC

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7341

---

#### 482. [Microsoft] CVE-2026-7338 - Chromium: CVE-2026-7338 Use after free in Cast

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7338

---

#### 483. [Microsoft] CVE-2026-7345 - Chromium: CVE-2026-7345 Insufficient validation of untrusted input in Feedback

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7345

---

#### 484. [Microsoft] CVE-2026-7346 - Chromium: CVE-2026-7346 Inappropriate implementation in Tint

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7346

---

#### 485. [Microsoft] CVE-2026-7347 - Chromium: CVE-2026-7347 Use after free in Chromoting

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7347

---

#### 486. [Microsoft] CVE-2026-7337 - Chromium: CVE-2026-7337 Type Confusion in V8

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7337

---

#### 487. [Microsoft] CVE-2026-7336 - Chromium: CVE-2026-7336 Use after free in WebRTC

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7336

---

#### 488. [Microsoft] CVE-2026-7335 - Chromium: CVE-2026-7335 Use after free in media

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7335

---

#### 489. [Microsoft] CVE-2026-7348 - Chromium: CVE-2026-7348 Use after free in Codecs

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7348

---

#### 490. [Microsoft] CVE-2026-7349 - Chromium: CVE-2026-7349 Use after free in Cast

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7349

---

#### 491. [Microsoft] CVE-2026-7350 - Chromium: CVE-2026-7350 Use after free in WebMIDI

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7350

---

#### 492. [Microsoft] CVE-2026-7351 - Chromium: CVE-2026-7351 Race in MHTML

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7351

---

#### 493. [Microsoft] CVE-2026-7353 - Chromium: CVE-2026-7353 Heap buffer overflow in Skia

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7353

---

#### 494. [Microsoft] CVE-2026-7354 - Chromium: CVE-2026-7354 Out of bounds read and write in Angle

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7354

---

#### 495. [Microsoft] CVE-2026-7356 - Chromium: CVE-2026-7356 Use after free in Navigation

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7356

---

#### 496. [Microsoft] CVE-2026-7357 - Chromium: CVE-2026-7357 Use after free in GPU

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7357

---

#### 497. [Microsoft] CVE-2026-7334 - Chromium: CVE-2026-7334 Use after free in Views

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Microsoft Edge (Chromium-based)

**漏洞描述 / Description**:
[Microsoft] This CVE was assigned by Chrome.  Microsoft Edge (Chromium-based) ingests Chromium, which addresses this vulnerability. Please see [Google Chrome Releases](https://chromereleases.googleblog.com/2025) for more information.

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-7334

---

#### 498. [Microsoft] CVE-2026-31533 - net/tls: fix use-after-free in -EBUSY error path of tls_do_encryption

**严重程度 / Severity**: N/A
**受影响产品 / Affected Products**: Mariner

**漏洞描述 / Description**:
[Microsoft]

**补丁信息 / Patch Info**:
Install Microsoft security update KB. Use Windows Update or download from Microsoft Update Catalog.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-2026-31533

---
