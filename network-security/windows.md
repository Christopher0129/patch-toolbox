# Windows 网络安全漏洞 | Windows Network Security

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 834**

> 技术细节（漏洞描述、缓解方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, mitigations) remain in original language for accuracy; structural text is bilingual.

---

#### 1. CVE-1999-0012

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Some web servers under Microsoft Windows allow remote attackers to bypass access restrictions for files with long file names.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0012

---

#### 2. CVE-1999-1556

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft SQL Server 6.5 uses weak encryption for the password for the SQLExecutiveCmdExec account and stores it in an accessible portion of the registry, which could allow local users to gain privileges by reading and decrypting the CmdExecAccount value.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=90222453431645&w=2
- http://www.securityfocus.com/bid/109
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7354
- http://marc.info/?l=ntbugtraq&m=90222453431645&w=2
- http://www.securityfocus.com/bid/109

---

#### 3. CVE-1999-0288

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The WINS server in Microsoft Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service (process termination) via invalid UDP frames to port 137 (NETBIOS Name Service), as demonstrated via a flood of random packets.

**参考链接 / References**:
- http://safenetworks.com/Windows/wins.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1233
- http://safenetworks.com/Windows/wins.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1233

---

#### 4. CVE-1999-1291

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
TCP/IP implementation in Microsoft Windows 95, Windows NT 4.0, and possibly others, allows remote attackers to reset connections by forcing a reset (RST) via a PSH ACK or other means, obtaining the target's last sequence number from the resulting packet, then spoofing a reset to the target.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/10789
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1383
- http://www.securityfocus.com/archive/1/10789
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1383

---

#### 5. CVE-1999-0364

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Access 97 stores a database password as plaintext in a foreign mdb, allowing access to data.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91816470220259&w=2
- http://marc.info/?l=bugtraq&m=91816470220259&w=2

---

#### 6. CVE-1999-1544

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in FTP server in Microsoft IIS 3.0 and 4.0 allows local and sometimes remote attackers to cause a denial of service via a long NLST (ls) command.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91722115016183&w=2
- http://marc.info/?l=bugtraq&m=91722115016183&w=2

---

#### 7. CVE-1999-0379

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Taskpads allows remote web sites to execute commands on the visiting user's machine via certain methods that are marked as Safe for Scripting.

**参考链接 / References**:
- http://www.osvdb.org/1019
- http://www.securityfocus.com/bid/498
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-007
- http://www.osvdb.org/1019
- http://www.securityfocus.com/bid/498

---

#### 8. CVE-1999-0386

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Personal Web Server and FrontPage Personal Web Server in some Windows systems allows a remote attacker to read files on the server by using a nonstandard URL.

**参考链接 / References**:
- http://www.osvdb.org/111
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-010
- http://www.osvdb.org/111
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-010

---

#### 9. CVE-1999-0419

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
When the Microsoft SMTP service attempts to send a message to a server and receives a 4xx error code, it quickly and repeatedly attempts to redeliver the message, causing a denial of service.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0419

---

#### 10. CVE-1999-0468

**严重程度 / Severity**: HIGH | CVSS: 8.2

**漏洞描述 / Description**:
Internet Explorer 5.0 allows a remote server to read arbitrary files on the client's file system using the Microsoft Scriptlet Component.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-012

---

#### 11. CVE-1999-1097

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Microsoft NetMeeting 2.1 allows one client to read the contents of another client's clipboard via a CTRL-C in the chat box when the box is empty.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92586457816446&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2187
- http://marc.info/?l=bugtraq&m=92586457816446&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2187

---

#### 12. CVE-1999-0717

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
A remote attacker can disable the virus warning mechanism in Microsoft Excel 97.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-014
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231304
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-014

---

#### 13. CVE-1999-1033

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook Express before 4.72.3612.1700 allows a malicious user to send a message that contains a .., which can inadvertently cause Outlook to re-enter POP3 command mode and cause the POP3 session to hang.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92647407427342&w=2
- http://marc.info/?l=bugtraq&m=92663402004275&w=2
- http://www.securityfocus.com/bid/252
- http://marc.info/?l=bugtraq&m=92647407427342&w=2
- http://marc.info/?l=bugtraq&m=92663402004275&w=2

---

#### 14. CVE-1999-1520

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
A configuration problem in the Ad Server Sample directory (AdSamples) in Microsoft Site Server 3.0 allows an attacker to obtain the SITE.CSC file, which exposes sensitive SQL database information.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=92647407227303&w=2
- http://www.securityfocus.com/bid/256
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2270
- http://marc.info/?l=bugtraq&m=92647407227303&w=2
- http://www.securityfocus.com/bid/256

---

#### 15. CVE-1999-1368

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
AV Option for MS Exchange Server option for InoculateIT 4.53, and possibly other versions, only scans the Inbox folder tree of a Microsoft Exchange server, which could allow viruses to escape detection if a user's rules cause the message to be moved to a different mailbox.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92652152723629&w=2
- http://marc.info/?l=ntbugtraq&m=97439568517355&w=2
- http://marc.info/?l=ntbugtraq&m=92652152723629&w=2
- http://marc.info/?l=ntbugtraq&m=97439568517355&w=2

---

#### 16. CVE-1999-1164

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook client allows remote attackers to cause a denial of service by sending multiple email messages with the same X-UIDL headers, which causes Outlook to hang.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93041631215856&w=2
- http://marc.info/?l=bugtraq&m=93041631215856&w=2

---

#### 17. CVE-1999-1011

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Remote Data Service (RDS) DataFactory component of Microsoft Data Access Components (MDAC) in IIS 3.x and 4.x exposes unsafe methods, which allows remote attackers to execute arbitrary commands.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/j-054.shtml
- http://www.osvdb.org/272
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-004
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-025
- https://www.securityfocus.com/bid/529

---

#### 18. CVE-2000-0323

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to modify text files via a database query, aka the "Text I-ISAM" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030
- https://web.archive.org/web/20000819203059/http://xforce.iss.net:80/alerts/vol-4_num-7.php#jet-text-isam
- https://www.securityfocus.com/bid/595
- http://www.securityfocus.com/templates/archive.pike?list=1&date=1999-08-22&msg=19990729195531.25108.qmail%40underground.org

---

#### 19. CVE-1999-0700

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Dialer (dialer.exe), via a malformed dialer entry in the dialer.ini file.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-026
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237185
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-026

---

#### 20. CVE-1999-0682

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange 5.5 allows a remote attacker to relay email (i.e. spam) using encapsulated SMTP addresses, even if the anti-relaying features are enabled.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927
- http://www.ciac.org/ciac/bulletins/j-056.shtml
- http://www.securityfocus.com/bid/567
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-027
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237927

---

#### 21. CVE-1999-0749

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Buffer overflow in Microsoft Telnet client in Windows 95 and Windows 98 via a malformed Telnet argument.

**参考链接 / References**:
- http://www.securityfocus.com/bid/586
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-033
- http://www.securityfocus.com/bid/586
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-033

---

#### 22. CVE-2000-0325

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Microsoft Jet database engine allows an attacker to execute commands via a database query, aka the "VBA Shell" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/548
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3155
- http://www.securityfocus.com/bid/548
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-030

---

#### 23. CVE-1999-1052

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft FrontPage stores form results in a default location in /_private/form_results.txt, which is world-readable and accessible in the document root, which allows remote attackers to read possibly sensitive information submitted by other users.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93582550911564&w=2
- http://marc.info/?l=bugtraq&m=93582550911564&w=2

---

#### 24. CVE-1999-1016

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft HTML control as used in (1) Internet Explorer 5.0, (2) FrontPage Express, (3) Outlook Express 5, and (4) Eudora, and possibly others, allows remote malicious web site or HTML emails to cause a denial of service (100% CPU consumption) via large HTML form fields such as text inputs in a table cell.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=93578772920970&w=2
- http://www.securityfocus.com/bid/606
- http://marc.info/?l=ntbugtraq&m=93578772920970&w=2
- http://www.securityfocus.com/bid/606

---

#### 25. CVE-1999-0910

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Site Server and Commercial Internet System (MCIS) do not set an expiration for a cookie, which could then be cached by a proxy and inadvertently used by a different user.

**参考链接 / References**:
- http://www.securityfocus.com/bid/625
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-035
- http://www.securityfocus.com/bid/625
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-035

---

#### 26. CVE-1999-0794

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Excel does not warn a user when a macro is present in a Symbolic Link (SYLK) format file.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241901
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241902
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-044
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ241900

---

#### 27. CVE-1999-0766

**严重程度 / Severity**: N/A | CVSS: 9.3

**漏洞描述 / Description**:
The Microsoft Java Virtual Machine allows a malicious Java applet to execute arbitrary commands outside of the sandbox environment.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-031
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ240346
- http://www.securityfocus.com/bid/600

---

#### 28. CVE-2000-0327

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
Microsoft Virtual Machine (VM) allows remote attackers to escape the Java sandbox and execute commands via an applet containing an illegal cast operation, aka the "Virtual Machine Verifier" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045
- http://marc.info/?l=bugtraq&m=93993545118416&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-045

---

#### 29. CVE-2000-0329

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
A Microsoft ActiveX control allows a remote attacker to execute a malicious cabinet file via an attachment and an embedded script in an HTML mail, aka the "Active Setup Control" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-048

---

#### 30. CVE-2000-0073

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Rich Text Format (RTF) reader allows attackers to cause a denial of service via a malformed control word.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973
- http://xforce.iss.net/search.php3?type=2&pattern=win-malformed-rtf-control-word
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-005
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249973
- http://xforce.iss.net/search.php3?type=2&pattern=win-malformed-rtf-control-word

---

#### 31. CVE-1999-0999

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Microsoft SQL 7.0 server allows a remote attacker to cause a denial of service via a malformed TDS packet.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749
- http://www.securityfocus.com/bid/817
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-059
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248749
- http://www.securityfocus.com/bid/817

---

#### 32. CVE-1999-0993

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Modifications to ACLs (Access Control Lists) in Microsoft Exchange  5.5 do not take effect until the directory store cache is refreshed.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0993

---

#### 33. CVE-1999-1043

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 and 5.0 does not properly handle (1) malformed NNTP data, or (2) malformed SMTP data, which allows remote attackers to cause a denial of service (application error).

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-007

---

#### 34. CVE-1999-1055

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Excel 97 does not warn the user before executing worksheet functions, which could allow attackers to execute arbitrary commands by using the CALL function to execute a malicious DLL, aka the Excel "CALL Vulnerability."

**参考链接 / References**:
- http://www.securityfocus.com/bid/179
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-018
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1737
- http://www.securityfocus.com/bid/179
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-018

---

#### 35. CVE-1999-1246

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Direct Mailer feature in Microsoft Site Server 3.0 saves user domain names and passwords in plaintext in the TMLBQueue network share, which has insecure default permissions, allowing remote attackers to read the passwords and gain privileges.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q229/9/72.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2068
- http://support.microsoft.com/support/kb/articles/Q229/9/72.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2068

---

#### 36. CVE-1999-1259

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Office 98, Macintosh Edition, does not properly initialize the disk space used by Office 98 files and effectively inserts data from previously deleted files into the Office file, which could allow attackers to obtain sensitive information.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q189/5/29.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1780
- http://support.microsoft.com/support/kb/articles/q189/5/29.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1780

---

#### 37. CVE-1999-1279

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
An interaction between the AS/400 shared folders feature and Microsoft SNA Server 3.0 and earlier allows users to view each other's folders when the users share the same Local APPC LU.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q138/0/01.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1548
- http://support.microsoft.com/support/kb/articles/q138/0/01.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1548

---

#### 38. CVE-1999-1591

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Information Services (IIS) server 4.0 SP4, without certain hotfixes released for SP4, does not require authentication credentials under certain conditions, which allows remote attackers to bypass authentication requirements, as demonstrated by connecting via Microsoft Visual InterDev 6.0.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00277.html
- http://www.securityfocus.com/bid/190
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00276.html
- http://archives.neohapsis.com/archives/ntbugtraq/1998-1999/msg00277.html

---

#### 39. CVE-2000-0053

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Commercial Internet System (MCIS) IMAP server allows remote attackers to cause a denial of service via a malformed IMAP request.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731
- http://www.securityfocus.com/bid/912
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-001
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246731
- http://www.securityfocus.com/bid/912

---

#### 40. CVE-2000-0097

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The WebHits ISAPI filter in Microsoft Index Server allows remote attackers to read arbitrary files, aka the "Malformed Hit-Highlighting Argument" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/1210
- http://www.securityfocus.com/bid/950
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- http://www.osvdb.org/1210
- http://www.securityfocus.com/bid/950

---

#### 41. CVE-2000-0098

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to determine the real path for a web directory via a request to an Internet Data Query file that does not exist.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006

---

#### 42. CVE-2000-0132

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Microsoft Java Virtual Machine allows remote attackers to read files via the getSystemResourceAsStream function.

**参考链接 / References**:
- http://www.securityfocus.com/bid/957
- http://www.securityfocus.com/bid/957

---

#### 43. CVE-2000-0089

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The rdisk utility in Microsoft Terminal Server Edition and Windows NT 4.0 stores registry hive information in a temporary file with permissions that allow local users to read it, aka the "RDISK Registry Enumeration File" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108
- http://www.securityfocus.com/bid/947
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-004
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ249108
- http://www.securityfocus.com/bid/947

---

#### 44. CVE-2000-0161

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Sample web sites on Microsoft Site Server 3.0 Commerce Edition do not validate an identification number, which allows remote attackers to execute SQL commands.

**参考链接 / References**:
- http://www.securityfocus.com/bid/994
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-010
- http://www.securityfocus.com/bid/994
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-010

---

#### 45. CVE-2000-0162

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The Microsoft virtual machine (VM) in Internet Explorer 4.x and 5.x allows a remote attacker to read files via a malicious Java applet that escapes the Java sandbox, aka the "VM File Reading" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-011

---

#### 46. CVE-2000-0160

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The Microsoft Active Setup ActiveX component in Internet Explorer 4.x and 5.x allows a remote attacker to install software components without prompting the user by stating that the software's manufacturer is Microsoft.

**参考链接 / References**:
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=20000221103938.T21312%40securityfocus.com

---

#### 47. CVE-2000-0216

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft email clients in Outlook, Exchange, and Windows Messaging automatically respond to Read Receipt and Delivery Receipt tags, which could allow an attacker to flood a mail system with responses by forging a Read Receipt request that is redirected to a large distribution list.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q1/0176.html

---

#### 48. CVE-2000-0201

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The window.showHelp() method in Internet Explorer 5.x does not restrict HTML help files (.chm) to be executed from the local host, which allows remote attackers to execute arbitrary commands via Microsoft Networking.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1033
- http://www.securityfocus.com/bid/1033

---

#### 49. CVE-2000-0168

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 9x operating systems allow an attacker to cause a denial of service via a pathname that includes file device names, aka the "DOS Device in Path Name" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1043
- http://www.securityfocus.com/templates/advisory.html?id=2126
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=NCBBKFKDOLAGKIAPMILPCENECCAA.labs%40ussrback.com
- http://www.securityfocus.com/bid/1043
- http://www.securityfocus.com/templates/advisory.html?id=2126

---

#### 50. [webapps] HAX CMS 24.x - Stored Cross-Site Scripting (XSS)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] HAX CMS 24.x - Stored Cross-Site Scripting (XSS)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52526

---

#### 51. [webapps] Craft CMS 5.6.16 - RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Craft CMS 5.6.16 - RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52525

---

#### 52. [local] GNU InetUtils 2.6 - Telnetd Remote Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GNU InetUtils 2.6 - Telnetd Remote Privilege Escalation

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52524

---

#### 53. [webapps] phpMyFAQ  4.0.16 - Improper Authorization

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] phpMyFAQ 4.0.16 - Improper Authorization

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52523

---

#### 54. [webapps] GeographicLib v2.5.1 - stack buffer overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GeographicLib v2.5.1 - stack buffer overflow

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52522

---

#### 55. [local] OpenWrt 23.05 - Authenticated Remote Code Execution (RCE)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] OpenWrt 23.05 - Authenticated Remote Code Execution (RCE)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52521

---

#### 56. [webapps] OpenKM 6.3.12 - Multiple

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] OpenKM 6.3.12 - Multiple

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52520

---

#### 57. [webapps] GUnet OpenEclass E-learning platform < 4.2 - Remote Code Execution (RCE)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] GUnet OpenEclass E-learning platform < 4.2 - Remote Code Execution (RCE)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52519

---

#### 58. [webapps] JuzaWeb CMS 3.4.2 - Authenticated Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] JuzaWeb CMS 3.4.2 - Authenticated Remote Code Execution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52518

---

#### 59. [webapps] FacturaScripts 2025.43 - XSS

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FacturaScripts 2025.43 - XSS

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52517

---

#### 60. [webapps] Xibo CMS  4.3.0 - RCE via SSTI

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Xibo CMS 4.3.0 - RCE via SSTI

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52516

---

#### 61. [local] Fedora - Local Privilege Escalation

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Fedora - Local Privilege Escalation

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52515

---

#### 62. [webapps] LangChain Core 1.2.4 - SSTI/RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] LangChain Core 1.2.4 - SSTI/RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52514

---

#### 63. [local] Atlona ATOMERX21 - Authenticated Command Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Atlona ATOMERX21 - Authenticated Command Injection

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52513

---

#### 64. CVE-2000-0200

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Buffer overflow in Microsoft Clip Art Gallery allows remote attackers to cause a denial of service or execute commands via a malformed CIL (clip art library) file, aka the "Clip Art Buffer Overrun" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1034
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-015
- http://www.securityfocus.com/bid/1034
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-015

---

#### 65. CVE-2000-0202

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and Microsoft Data Engine (MSDE) 1.0 allow remote attackers to gain privileges via a malformed Select statement in an SQL query.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-014
- http://www.securityfocus.com/bid/1041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-014

---

#### 66. CVE-2000-0199

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
When a new SQL Server is registered in Enterprise Manager for Microsoft SQL Server 7.0 and the "Always prompt for login name and password" option is not set, then the Enterprise Manager uses weak encryption to store the login ID and password.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1055
- http://www.securityfocus.com/bid/1055

---

#### 67. CVE-2000-0228

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media License Manager allows remote attackers to cause a denial of service by sending a malformed request that causes the manager to halt, aka the "Malformed Media License Request" Vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1058
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-016
- http://www.securityfocus.com/bid/1058
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-016

---

#### 68. CVE-2000-0232

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft TCP/IP Printing Services, aka Print Services for Unix, allows an attacker to cause a denial of service via a malformed TCP/IP print request.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html
- http://www.securityfocus.com/bid/1082
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-021
- http://archives.neohapsis.com/archives/bugtraq/2000-03/0306.html
- http://www.securityfocus.com/bid/1082

---

#### 69. CVE-2000-0302

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server allows remote attackers to view the source code of ASP files by appending a %20 to the filename in the CiWebHitsFile argument to the null.htw URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=95453598317340&w=2
- http://www.osvdb.org/271
- http://www.securityfocus.com/bid/1084
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-006
- http://marc.info/?l=bugtraq&m=95453598317340&w=2

---

#### 70. CVE-2000-0277

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 does not warn the user when executing Excel Macro Language (XLM) macros in external text files, which could allow an attacker to execute a macro virus, aka the "XLM Text Macro" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/1272
- http://www.securityfocus.com/bid/1087
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-022
- http://www.osvdb.org/1272
- http://www.securityfocus.com/bid/1087

---

#### 71. CVE-2000-0260

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the dvwssr.dll DLL in Microsoft Visual Interdev 1.0 allows users to cause a denial of service or execute commands, aka the "Link View Server-Side Component" vulnerability.

**参考链接 / References**:
- http://www.osvdb.org/282
- http://www.securityfocus.com/bid/1109
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-025
- http://www.osvdb.org/282
- http://www.securityfocus.com/bid/1109

---

#### 72. CVE-2000-1218

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The default configuration for the domain name resolver for Microsoft Windows 98, NT 4.0, 2000, and XP sets the QueryIpMatching parameter to 0, which causes Windows to accept DNS updates from hosts that it did not query, which allows remote attackers to poison the DNS cache.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/458659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4280
- http://www.kb.cert.org/vuls/id/458659
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4280

---

#### 73. CVE-2000-0331

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft command processor (CMD.EXE) for Windows NT and Windows 2000 allows a local user to cause a denial of service via a long environment variable, aka the "Malformed Environment Variable" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html
- http://www.securityfocus.com/bid/1135
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-027
- http://archives.neohapsis.com/archives/bugtraq/2000-04/0147.html
- http://www.securityfocus.com/bid/1135

---

#### 74. CVE-2000-0304

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS 4.0 and 5.0 with the IISADMPWD virtual directory installed allows a remote attacker to cause a denial of service via a malformed request to the inetinfo.exe program, aka the "Undelimited .HTR Request" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1191
- http://xforce.iss.net/alerts/advise52.php3
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-031
- http://www.securityfocus.com/bid/1191
- http://xforce.iss.net/alerts/advise52.php3

---

#### 75. CVE-2000-0400

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Active Movie ActiveX Control in Internet Explorer 5 does not restrict which file types can be downloaded, which allows an attacker to download any type of file to a user's system by encoding it within an email message or news post.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=95868514521257&w=2
- http://www.securityfocus.com/bid/1221
- http://marc.info/?l=bugtraq&m=95868514521257&w=2
- http://www.securityfocus.com/bid/1221

---

#### 76. CVE-2000-0402

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Mixed Mode authentication capability in Microsoft SQL Server 7.0 stores the System Administrator (sa) account in plaintext in a log file which is readable by any user, aka the "SQL Server 7.0 Service Pack Password" vulnerability.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=263968
- http://www.securityfocus.com/bid/1281
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-035
- http://www.microsoft.com/technet/support/kb.asp?ID=263968
- http://www.securityfocus.com/bid/1281

---

#### 77. CVE-2000-0485

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft SQL Server allows local users to obtain database passwords via the Data Transformation Service (DTS) package Properties dialog, aka the "DTS Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/62771
- http://www.securityfocus.com/bid/1292
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4582
- http://www.securityfocus.com/archive/1/62771

---

#### 78. CVE-2000-0495

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media Encoder allows remote attackers to cause a denial of service via a malformed request, aka the "Malformed Windows Media Encoder Request" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1282
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-038
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4585
- http://www.securityfocus.com/bid/1282
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-038

---

#### 79. CVE-2000-0524

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook and Outlook Express allow remote attackers to cause a denial of service by sending email messages with blank fields such as BCC, Reply-To, Return-Path, or From.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html
- http://www.securityfocus.com/bid/1333
- http://archives.neohapsis.com/archives/bugtraq/2000-06/0045.html
- http://www.securityfocus.com/bid/1333

---

#### 80. CVE-2000-0596

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.x does not warn a user before opening a Microsoft Access database file that is referenced within ActiveX OBJECT tags in an HTML document, which could allow remote attackers to execute arbitrary commands, aka the "IE Script" vulnerability.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2000-16.html
- http://www.securityfocus.com/bid/1398
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=000d01bfe0fb%24418f59b0%2496217aa8%40src.bu.edu
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589359.762392DB%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-049

---

#### 81. CVE-2000-0597

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Office 2000 (Excel and PowerPoint) and PowerPoint 97 are marked as safe for scripting, which allows remote attackers to force Internet Explorer or some email clients to save files to arbitrary locations via the Visual Basic for Applications (VBA) SaveAs function, aka the "Office HTML Script" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1399
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589349.ED9DBCAB%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-049
- http://www.securityfocus.com/bid/1399
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=39589349.ED9DBCAB%40nat.bg

---

#### 82. CVE-2000-0603

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 allows a local user to bypass permissions for stored procedures by referencing them via a temporary stored procedure, aka the "Stored Procedure Permissions" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1444
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-048
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4921
- http://www.securityfocus.com/bid/1444
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-048

---

#### 83. CVE-2000-0654

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Enterprise Manager allows local users to obtain database passwords via the Data Transformation Service (DTS) package Registered Servers Dialog dialog, aka a variant of the "DTS Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1466
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4582
- http://www.securityfocus.com/bid/1466
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-041

---

#### 84. CVE-2000-0662

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Internet Explorer 5.x and Microsoft Outlook allows remote attackers to read arbitrary files by redirecting the contents of an IFRAME using the DHTML Edit Control (DHTMLED).

**参考链接 / References**:
- http://www.securityfocus.com/bid/1474
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396EF9D5.62EEC625%40nat.bg
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5107
- http://www.securityfocus.com/bid/1474
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396EF9D5.62EEC625%40nat.bg

---

#### 85. CVE-2000-0567

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Outlook and Outlook Express allows remote attackers to execute arbitrary commands via a long Date field in an email header, aka the "Malformed E-mail Header" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1481
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-043
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4953
- http://www.securityfocus.com/bid/1481
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-043

---

#### 86. CVE-2000-0621

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Outlook 98 and 2000, and Outlook Express 4.0x and 5.0x, allow remote attackers to read files on the client's system via a malformed HTML message that stores files outside of the cache, aka the "Cache Bypass" vulnerability.

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2000-14.html
- http://www.securityfocus.com/bid/1501
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-046
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5013
- http://www.cert.org/advisories/CA-2000-14.html

---

#### 87. CVE-2000-0653

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook Express allows remote attackers to monitor a user's email by creating a persistent browser link to the Outlook Express windows, aka the "Persistent Mail-Browser Link" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1502
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-045
- http://www.securityfocus.com/bid/1502
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-045

---

#### 88. CVE-2000-0637

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Excel 97 and 2000 allows an attacker to execute arbitrary commands by specifying a malicious .dll using the Register.ID function, aka the "Excel REGISTER.ID Function" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1451
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=396B3F8F.9244D290%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-051
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5016
- http://www.securityfocus.com/bid/1451

---

#### 89. CVE-2000-1079

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Interactions between the CIFS Browser Protocol and NetBIOS as implemented in Microsoft Windows 95, 98, NT, and 2000 allow remote attackers to modify dynamic NetBIOS name cache entries via a spoofed Browse Frame Request in a unicast or UDP broadcast datagram.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0116.html
- http://www.nai.com/research/covert/advisories/045.asp
- http://www.securityfocus.com/bid/1620
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5168
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1079

---

#### 90. CVE-2000-0709

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to cause a denial of service in some components by requesting a URL whose name includes a standard DOS device name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp
- http://www.securityfocus.com/bid/1608
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp

---

#### 91. CVE-2000-0710

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The shtml.exe component of Microsoft FrontPage 2000 Server Extensions 1.1 allows remote attackers to determine the physical path of the server components by requesting an invalid URL whose name includes a standard DOS device name.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp
- http://www.securityfocus.com/bid/1608
- http://archives.neohapsis.com/archives/bugtraq/2000-08/0288.html
- http://msdn.microsoft.com/workshop/languages/fp/2000/sr12.asp

---

#### 92. CVE-2000-0742

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The IPX protocol implementation in Microsoft Windows 95 and 98 allows remote attackers to cause a denial of service by sending a ping packet with a source IP address that is a broadcast address, aka the "Malformed IPX Ping Packet" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1544
- http://www.securityfocus.com/templates/archive.pike?list=1&mid=63120
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-054
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5079
- http://www.securityfocus.com/bid/1544

---

#### 93. CVE-2000-0753

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Outlook mail client identifies the physical path of the sender's machine within a winmail.dat attachment to Rich Text Format (RTF) files.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/201422
- http://www.securityfocus.com/archive/1/78240
- http://www.securityfocus.com/bid/1631
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5508
- http://www.securityfocus.com/archive/1/201422

---

#### 94. CVE-2000-0756

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook 2000 does not properly process long or malformed fields in vCard (.vcf) files, which allows attackers to cause a denial of service.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1633
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Springmail.105.967737080.0.16997300%40www.springmail.com
- http://www.securityfocus.com/bid/1633
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Springmail.105.967737080.0.16997300%40www.springmail.com

---

#### 95. CVE-2000-0765

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Buffer overflow in the HTML interpreter in Microsoft Office 2000 allows an attacker to execute arbitrary commands via a long embedded object tag, aka the "Microsoft Office HTML Object Tag" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1561
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-056
- http://www.securityfocus.com/bid/1561
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-056

---

#### 96. CVE-2000-0771

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to cause a denial of service by corrupting the local security policy via malformed RPC traffic, aka the "Local Security Policy Corruption" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1613
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-062
- http://www.securityfocus.com/bid/1613
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-062

---

#### 97. CVE-2000-0777

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The password protection feature of Microsoft Money can store the password in plaintext, which allows attackers with physical access to the system to obtain the password, aka the "Money Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1615
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-061
- http://www.securityfocus.com/bid/1615
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-061

---

#### 98. CVE-2000-0788

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Mail Merge tool in Microsoft Word does not prompt the user before executing Visual Basic (VBA) scripts in an Access database, which could allow an attacker to execute arbitrary commands.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1566
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=398EB9CA.27E03A9C%40nat.bg
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-071
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5322
- http://www.securityfocus.com/bid/1566

---

#### 99. CVE-2000-0790

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The web-based folder display capability in Microsoft Internet Explorer 5.5 on Windows 98 allows local users to insert Trojan horse programs by modifying the Folder.htt file and using the InvokeVerb method in the ShellDefView ActiveX control to specify a default execute option for the first file that is listed in the folder.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1571
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3998370D.732A03F1%40nat.bg
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5097
- http://www.securityfocus.com/bid/1571
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=3998370D.732A03F1%40nat.bg

---

#### 100. CVE-2000-0849

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Race condition in Microsoft Windows Media server allows remote attackers to cause a denial of service in the Windows Media Unicast Service via a malformed request, aka the "Unicast Service Race Condition" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1655
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-064
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5193
- http://www.securityfocus.com/bid/1655
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-064

---

#### 101. CVE-2000-0854

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
When a Microsoft Office 2000 document is launched, the directory of that document is first used to locate DLL's such as riched20.dll and msi.dll, which could allow an attacker to execute arbitrary commands by inserting a Trojan Horse DLL into the same directory as the document.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0277.html
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q3/0155.html
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q3/0117.html
- http://www.securityfocus.com/bid/1699
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5263

---

#### 102. CVE-2000-0858

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerability in Microsoft Windows NT 4.0 allows remote attackers to cause a denial of service in IIS by sending it a series of malformed requests which cause INETINFO.EXE to fail, aka the "Invalid URL" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html
- http://www.securityfocus.com/archive/1/80413
- http://www.securityfocus.com/bid/1642
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5202
- http://archives.neohapsis.com/archives/vendor/2000-q3/0065.html

---

#### 103. CVE-2000-1217

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows 2000 before Service Pack 2 (SP2), when running in a non-Windows 2000 domain and using NTLM authentication, and when credentials of an account are locally cached, allows local users to bypass account lockout policies and make an unlimited number of login attempts, aka the "Domain Account Lockout" vulnerability.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/818496
- http://www.securityfocus.com/bid/1973
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-089
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5585
- http://www.kb.cert.org/vuls/id/818496

---

#### 104. CVE-2000-1006

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange Server 5.5 does not properly handle a MIME header with a blank charset specified, which allows remote attackers to cause a denial of service via a charset="" command, aka the "Malformed MIME Header" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1869
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-082
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5448
- http://www.securityfocus.com/bid/1869
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-082

---

#### 105. CVE-2000-0817

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the HTTP protocol parser for Microsoft Network Monitor (Netmon) allows remote attackers to execute arbitrary commands via malformed data, aka the "Netmon Protocol Parsing" vulnerability.

**参考链接 / References**:
- http://xforce.iss.net/alerts/index.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399
- http://xforce.iss.net/alerts/index.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083

---

#### 106. CVE-2000-0885

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Microsoft Network Monitor (Netmon) allow remote attackers to execute arbitrary commands via a long Browser Name in a CIFS Browse Frame, a long SNMP community name, or a long username or filename in an SMB session, aka the "Netmon Protocol Parsing" vulnerability.  NOTE: It is highly likely that this candidate will be split into multiple candidates.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-083
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5399

---

#### 107. CVE-2000-0929

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 allows attackers to cause a denial of service in RTF-enabled email clients via an embedded OCX control that is not closed properly, aka the "OCX Attachment" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97024839222747&w=2
- http://www.securityfocus.com/bid/1714
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-068
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5309
- http://marc.info/?l=bugtraq&m=97024839222747&w=2

---

#### 108. CVE-2000-0942

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The CiWebHitsFile component in Microsoft Indexing Services for Windows 2000 allows remote attackers to conduct a cross site scripting (CSS) attack via a CiRestriction parameter in a .htw request, aka the "Indexing Services Cross Site Scripting" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/141903
- http://www.securityfocus.com/bid/1861
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-084
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5441
- http://www.securityfocus.com/archive/1/141903

---

#### 109. CVE-2000-0980

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
NMPI (Name Management Protocol on IPX) listener in Microsoft NWLink does not properly filter packets from a broadcast address, which allows remote attackers to cause a broadcast storm and flood the network.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1781
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-073
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5357
- http://www.securityfocus.com/bid/1781
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-073

---

#### 110. CVE-2000-0983

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft NetMeeting with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service (CPU utilization) via a sequence of null bytes to the NetMeeting port, aka the "NetMeeting Desktop Sharing" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ273854
- http://www.securityfocus.com/archive/1/140341
- http://www.securityfocus.com/bid/1798
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-077
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5368

---

#### 111. CVE-2000-1081

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_displayparamstmt function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2030
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A231
- http://marc.info/?l=bugtraq&m=97570878710037&w=2

---

#### 112. CVE-2000-1082

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_enumresultset function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2031
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2031

---

#### 113. CVE-2000-1083

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The xp_showcolv function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2038
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2038

---

#### 114. CVE-2000-1084

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_updatecolvbm function in SQL Server and Microsoft SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2039
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570878710037&w=2
- http://www.securityfocus.com/bid/2039

---

#### 115. CVE-2000-1085

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_peekqueue function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2040
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2040

---

#### 116. CVE-2000-1086

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_printstatements function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2041
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2041

---

#### 117. CVE-2000-1087

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_proxiedmetadata function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2042
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2042

---

#### 118. CVE-2000-1088

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The xp_SetSQLSecurity function in Microsoft SQL Server 2000 and SQL Server Desktop Engine (MSDE) does not properly restrict the length of a buffer before calling the srv_paraminfo function in the SQL Server API for Extended Stored Procedures (XP), which allows an attacker to cause a denial of service or execute arbitrary commands, aka the "Extended Stored Procedure Parameter Parsing" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2043
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-092
- http://marc.info/?l=bugtraq&m=97570884410184&w=2
- http://www.securityfocus.com/bid/2043

---

#### 119. CVE-2000-1089

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft Phone Book Service allows local users to execute arbitrary commands, aka the "Phone Book Service Buffer Overflow" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2048
- http://www.stake.com/research/advisories/2000/a120400-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-094
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5623
- http://www.securityfocus.com/bid/2048

---

#### 120. CVE-2000-1112

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows Media Player 7 executes scripts in custom skin (.WMS) files, which could allow remote attackers to gain privileges via a skin that contains a malicious script, aka the ".WMS Script Execution" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1976
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5575
- http://www.securityfocus.com/bid/1976
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090

---

#### 121. CVE-2000-1113

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player allows remote attackers to execute arbitrary commands via a malformed Active Stream Redirector (.ASX) file, aka the ".ASX Buffer Overrun" vulnerability.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a112300-1.txt
- http://www.securityfocus.com/bid/1980
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-090
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5574
- http://www.atstake.com/research/advisories/2000/a112300-1.txt

---

#### 122. CVE-2000-1139

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The installation of Microsoft Exchange 2000 before Rev. A creates a user account with a known password, which could allow attackers to gain privileges, aka the "Exchange User Account" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1958
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-088
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5537
- http://www.securityfocus.com/bid/1958
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-088

---

#### 123. CVE-2000-1090

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS for Far East editions 4.0 and 5.0 allows remote attackers to read source code for parsed pages via a malformed URL that uses the lead-byte of a double-byte character.

**参考链接 / References**:
- http://www.nsfocus.com/english/homepage/sa_08.htm
- http://www.securityfocus.com/bid/2100
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5729
- http://www.nsfocus.com/english/homepage/sa_08.htm
- http://www.securityfocus.com/bid/2100

---

#### 124. CVE-2001-0003

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Web Extender Client (WEC) in Microsoft Office 2000, Windows 2000, and Windows Me does not properly process Internet Explorer security settings for NTLM authentication, which allows attackers to obtain NTLM credentials and possibly obtain the password, aka the "Web Client NTLM Authentication" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2199
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-001
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5920
- http://www.securityfocus.com/bid/2199
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-001

---

#### 125. CVE-2001-0005

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
Buffer overflow in the parsing mechanism of the file loader in Microsoft PowerPoint 2000 allows attackers to execute arbitrary commands.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2001/a012301-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-002
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5996
- http://www.atstake.com/research/advisories/2001/a012301-1.txt
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-002

---

#### 126. CVE-2001-0048

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The "Configure Your Server" tool in Microsoft 2000 domain controllers installs a blank password for the Directory Service Restore Mode, which allows attackers with physical access to the controller to install malicious programs, aka the "Directory Service Restore Mode Password" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-099
- http://www.securityfocus.com/bid/2133
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-099

---

#### 127. CVE-2001-0047

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The default permissions for the MTS Package Administration registry key in Windows NT 4.0 allows local users to install or modify arbitrary Microsoft Transaction Server (MTS) packages and gain privileges, aka one of the "Registry Permissions" vulnerabilities.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2065
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5673
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A140
- http://www.securityfocus.com/bid/2065

---

#### 128. CVE-1999-0681

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Microsoft FrontPage Server Extensions (PWS) 3.0.2.926 on Windows 95, and possibly other versions, allows remote attackers to cause a denial of service via a long URL.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html
- http://www.securityfocus.com/bid/568
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3117
- http://archives.neohapsis.com/archives/bugtraq/1999-q3/0381.html
- http://www.securityfocus.com/bid/568

---

#### 129. CVE-1999-0945

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Service (IMS) for Microsoft Exchange 5.5 and 5.0 allows remote attackers to conduct a denial of service via AUTH or AUTHINFO commands.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174
- http://www.ciac.org/ciac/bulletins/i-080.shtml
- http://xforce.iss.net/alerts/advise4.php
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1223
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ169174

---

#### 130. CVE-2001-1450

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.0 through 6.0 allows attackers to cause a denial of service (browser crash) via a crafted FTP URL such as "/.#./".

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html
- http://www.kb.cert.org/vuls/id/199408
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10117
- http://cert.uni-stuttgart.de/archive/vuln-dev/2001/05/msg00029.html
- http://www.kb.cert.org/vuls/id/199408

---

#### 131. CVE-2001-1326

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Eudora 5.1 allows remote attackers to execute arbitrary code when the "Use Microsoft Viewer" option is enabled and the "allow executables in HTML content" option is disabled, via an HTML email with a form that is activated from an image that the attacker spoofs as a link, which causes the user to execute the form and access embedded attachments.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/187128
- http://www.securityfocus.com/bid/2796
- http://www.securityfocus.com/archive/1/187128
- http://www.securityfocus.com/bid/2796

---

#### 132. CVE-2001-0146

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
IIS 5.0 and Microsoft Exchange 2000 allow remote attackers to cause a denial of service (memory allocation error) by repeatedly sending a series of specially formatted URL's.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/796584
- http://www.securityfocus.com/bid/2440
- http://www.securityfocus.com/bid/2441
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-014
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6171

---

#### 133. CVE-2001-0261

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 Encrypted File System does not properly destroy backups of files that are encrypted, which allows a local attacker to recover the text of encrypted files.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97992179925715&w=2
- http://marc.info/?l=bugtraq&m=98027311214976&w=2
- http://www.securityfocus.com/bid/2243
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5973
- http://marc.info/?l=bugtraq&m=97992179925715&w=2

---

#### 134. CVE-2001-1088

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Outlook 8.5 and earlier, and Outlook Express 5 and earlier, with the "Automatically put people I reply to in my address book" option enabled, do not notify the user when the "Reply-To" address is different than the "From" address, which could allow an untrusted remote attacker to spoof legitimate addresses and intercept email from the client that is intended for another user.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241
- http://www.securityfocus.com/archive/1/188752
- http://www.securityfocus.com/bid/2823
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6655
- http://support.microsoft.com/default.aspx?scid=kb%3BEN-US%3Bq234241

---

#### 135. CVE-2001-0237

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in Microsoft 2000 domain controller allows remote attackers to cause a denial of service by repeatedly connecting to the Kerberos service and then disconnecting without sending any data.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-079.shtml
- http://marc.info/?l=bugtraq&m=98942093221908&w=2
- http://www.securityfocus.com/bid/2707
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-024
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6506

---

#### 136. CVE-2001-0240

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Word before Word 2002 allows attackers to automatically execute macros without warning the user via a Rich Text Format (RTF) document that links to a template with the embedded macro.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2753
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-028
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6571
- http://www.securityfocus.com/bid/2753
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-028

---

#### 137. CVE-2001-0242

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Microsoft Windows Media Player 7 and earlier allow remote attackers to execute arbitrary commands via (1) a long version tag in an .ASX file, or (2) a long banner tag, a variant of the ".ASX Buffer Overrun" vulnerability as discussed in MS:MS00-090.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/187528
- http://www.securityfocus.com/archive/1/181419
- http://www.securityfocus.com/archive/1/183906
- http://www.securityfocus.com/bid/2677
- http://www.securityfocus.com/bid/2686

---

#### 138. CVE-2001-0244

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Index Server 2.0 allows remote attackers to execute arbitrary commands via a long search parameter.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2709
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6517
- http://www.securityfocus.com/bid/2709
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025

---

#### 139. CVE-2001-0245

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Index Server 2.0 in Windows NT 4.0, and Indexing Service in Windows 2000, allows remote attackers to read server-side include files via a malformed search request, aka a new variant of the "Malformed Hit-Highlighting" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6518
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-025
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6518

---

#### 140. CVE-2001-0336

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft MS00-060 patch for IIS 5.0 and earlier introduces an error which allows attackers to cause a denial of service via a malformed request.

**参考链接 / References**:
- http://www.osvdb.org/5693
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6858
- http://www.osvdb.org/5693
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026

---

#### 141. CVE-2001-0337

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft MS01-014 and MS01-016 patches for IIS 5.0 and earlier introduce a memory leak which allows attackers to cause a denial of service via a series of requests.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-026

---

#### 142. CVE-2001-0365

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Eudora before 5.1 allows a remote attacker to execute arbitrary code, when the 'Use Microsoft Viewer' and 'allow executables in HTML content' options are enabled, via an HTML email message containing Javascript, with ActiveX controls and malicious code within IMG tags.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98503741910995&w=2
- http://www.securityfocus.com/bid/2490
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6262
- http://marc.info/?l=bugtraq&m=98503741910995&w=2
- http://www.securityfocus.com/bid/2490

---

#### 143. CVE-2001-0238

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Data Access Component Internet Publishing Provider 8.103.2519.0 and earlier allows remote attackers to bypass Security Zone restrictions via WebDAV requests.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-074.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-022
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6405
- http://www.ciac.org/ciac/bulletins/l-074.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-022

---

#### 144. CVE-2001-0239

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Security and Acceleration (ISA) Server 2000 Web Proxy allows remote attackers to cause a denial of service via a long web request with a specific type.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-073.shtml
- http://www.securityfocus.com/archive/1/176912
- http://www.securityfocus.com/archive/1/177160
- http://www.securityfocus.com/archive/1/179986
- http://www.securityfocus.com/bid/2600

---

#### 145. CVE-2001-1243

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Scripting.FileSystemObject in asp.dll for Microsoft IIS 4.0 and 5.0 allows local or remote attackers to cause a denial of service (crash) via (1) creating an ASP program that uses Scripting.FileSystemObject to open a file with an MS-DOS device name, or (2) remotely injecting the device name into ASP programs that internally use Scripting.FileSystemObject.

**参考链接 / References**:
- http://www.iss.net/security_center/static/6800.php
- http://www.securityfocus.com/archive/1/194919
- http://www.securityfocus.com/bid/2973
- http://www.iss.net/security_center/static/6800.php
- http://www.securityfocus.com/archive/1/194919

---

#### 146. CVE-2001-1319

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Exchange 5.5 2000 allows remote attackers to cause a denial of service (hang) via exceptional BER encodings for the LDAP filter type field, as demonstrated by the PROTOS LDAPv3 test suite.

**参考链接 / References**:
- http://ciac.llnl.gov/ciac/bulletins/l-116.shtml
- http://www.cert.org/advisories/CA-2001-18.html
- http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/ldapv3/
- http://www.kb.cert.org/vuls/id/763400
- http://www.kb.cert.org/vuls/id/CFCN-4YAQC7

---

#### 147. CVE-2001-0340

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
An interaction between the Outlook Web Access (OWA) service in Microsoft Exchange 2000 Server and Internet Explorer allows attackers to execute malicious script code against a user's mailbox via a message attachment that contains HTML code, which is executed automatically.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-091.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6652
- http://www.ciac.org/ciac/bulletins/l-091.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-030

---

#### 148. CVE-2001-0341

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Visual Studio RAD Support sub-component of FrontPage Server Extensions allows remote attackers to execute arbitrary commands via a long registration request (URL) to fp30reg.dll.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99348216322147&w=2
- http://www.osvdb.org/577
- http://www.securityfocus.com/bid/2906
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-035
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6730

---

#### 149. CVE-2001-0344

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
An SQL query method in Microsoft SQL Server 2000 Gold and 7.0 using Mixed Mode allows local database users to gain privileges by reusing a cached connection of the sa administrator account.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-095.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-032
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6684
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A71
- http://www.ciac.org/ciac/bulletins/l-095.shtml

---

#### 150. CVE-2001-0345

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to prevent idle Telnet sessions from timing out, causing a denial of service by creating a large number of idle sessions.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2843
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6667
- http://www.securityfocus.com/bid/2843
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031

---

#### 151. CVE-2001-0346

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Handle leak in Microsoft Windows 2000 telnet service allows attackers to cause a denial of service by starting a large number of sessions and terminating them.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6668
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6668

---

#### 152. CVE-2001-0347

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Information disclosure vulnerability in Microsoft Windows 2000 telnet service allows remote attackers to determine the existence of user accounts such as Guest, or log in to the server without specifying the domain name, via a malformed userid.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.osvdb.org/5686
- http://www.securityfocus.com/bid/2847
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6665

---

#### 153. CVE-2001-0348

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows attackers to cause a denial of service (crash) via a long logon command that contains a backspace.

**参考链接 / References**:
- http://razor.bindview.com/publish/advisories/adv_mstelnet.html
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.securityfocus.com/bid/2838
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6666

---

#### 154. CVE-2001-0349

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the first of two variants of this vulnerability.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/587587
- http://www.securityfocus.com/bid/2849
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664
- http://www.kb.cert.org/vuls/id/587587

---

#### 155. CVE-2001-0350

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service creates named pipes with predictable names and does not properly verify them, which allows local users to execute arbitrary commands by creating a named pipe with the predictable name and associating a malicious program with it, the second of two variants of this vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6664

---

#### 156. CVE-2001-0351

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Windows 2000 telnet service allows a local user to make a certain system call that allows the user to terminate a Telnet session and cause a denial of service.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-092.shtml
- http://www.securityfocus.com/bid/2846
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6669
- http://www.ciac.org/ciac/bulletins/l-092.shtml

---

#### 157. CVE-2001-0501

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Word 2002 and earlier allows attackers to automatically execute macros without warning the user by embedding the macros in a manner that escapes detection by the security scanner.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99325144322224&w=2
- http://www.securityfocus.com/bid/2876
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-034
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6732
- http://marc.info/?l=bugtraq&m=99325144322224&w=2

---

#### 158. CVE-2001-0503

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft NetMeeting 3.01 with Remote Desktop Sharing enabled allows remote attackers to cause a denial of service via a malformed string to the NetMeeting service port, aka a variant of the "NetMeeting Desktop Sharing" vulnerability.

**参考链接 / References**:
- http://www.iss.net/security_center/static/5368.php
- http://www.osvdb.org/5608
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-077
- http://www.iss.net/security_center/static/5368.php
- http://www.osvdb.org/5608

---

#### 159. CVE-2001-1055

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Windows network stack allows remote attackers to cause a denial of service (CPU consumption) via a flood of malformed ARP request packets with random source IP and MAC addresses, as demonstrated by ARPNuke.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/200323
- http://www.securityfocus.com/bid/3113
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6924
- http://www.securityfocus.com/archive/1/200323
- http://www.securityfocus.com/bid/3113

---

#### 160. CVE-2001-0504

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in authentication process for SMTP service in Microsoft Windows 2000 allows remote attackers to use incorrect credentials to gain privileges and conduct activities such as mail relaying.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-107.shtml
- http://www.kb.cert.org/vuls/id/435963
- http://www.securityfocus.com/bid/2988
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-037
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6803

---

#### 161. CVE-2001-0538

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Outlook View ActiveX Control in Microsoft Outlook 2002 and earlier allows remote attackers to execute arbitrary commands via a malicious HTML e-mail message or web page.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99496431214078&w=2
- http://www.ciac.org/ciac/bulletins/l-113.shtml
- http://www.kb.cert.org/vuls/id/131569
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind0107&L=ntbugtraq&F=P&S=&P=862
- http://www.securityfocus.com/bid/3025

---

#### 162. CVE-2001-0628

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Word 2000 does not check AutoRecovery (.asd) files for macros, which allows a local attacker to execute arbitrary macros with the user ID of the Word user.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q274/2/28.asp
- http://www.securityfocus.com/bid/2760
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6614
- http://support.microsoft.com/support/kb/articles/Q274/2/28.asp
- http://www.securityfocus.com/bid/2760

---

#### 163. CVE-2001-1099

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The default configuration of Norton AntiVirus for Microsoft Exchange 2000 2.x allows remote attackers to identify the recipient's INBOX file path by sending an email with an attachment containing malicious content, which includes the path in the rejection notice.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/212724
- http://www.securityfocus.com/archive/1/213762
- http://www.securityfocus.com/bid/3305
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7093
- http://www.securityfocus.com/archive/1/212724

---

#### 164. CVE-2001-0986

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
SQLQHit.asp sample file in Microsoft Index Server 2.0 allows remote attackers to obtain sensitive information such as the physical path, file attributes, or portions of source code by directly calling sqlqhit.asp with a CiScope parameter set to (1) webinfo, (2) extended_fileinfo, (3) extended_webinfo, or (4) fileinfo.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/214217
- http://www.securityfocus.com/bid/3339
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7125
- http://www.securityfocus.com/archive/1/214217
- http://www.securityfocus.com/bid/3339

---

#### 165. CVE-2001-0509

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Vulnerabilities in RPC servers in (1) Microsoft Exchange Server 2000 and earlier, (2) Microsoft SQL Server 2000 and earlier, (3) Windows NT 4.0, and (4) Windows 2000 allow remote attackers to cause a denial of service via malformed inputs.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-041
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A82
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-041
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A82

---

#### 166. CVE-2001-0541

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 7.1 and earlier allows remote attackers to execute arbitrary commands via a malformed Windows Media Station (.NSC) file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/187001
- http://www.securityfocus.com/bid/3105
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-042
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6907
- http://www.securityfocus.com/archive/1/187001

---

#### 167. CVE-2001-0709

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS 4.0 and before, when installed on a FAT partition, allows a remote attacker to obtain source code of ASP files via a URL encoded with Unicode.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/192802
- http://www.securityfocus.com/bid/2909
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6742
- http://www.securityfocus.com/archive/1/192802
- http://www.securityfocus.com/bid/2909

---

#### 168. CVE-2001-0505

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Multiple memory leaks in Microsoft Services for Unix 2.0 allow remote attackers to cause a denial of service (memory exhaustion) via a large number of malformed requests to (1) the Telnet service, or (2) the NFS service.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/581603
- http://www.kb.cert.org/vuls/id/994851
- http://www.securityfocus.com/bid/3089
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-039
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6882

---

#### 169. CVE-2001-0660

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5, SP4 and earlier, allows remote attackers to identify valid user email addresses by directly accessing a back-end function that processes the global address list (GAL).

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q307/1/95.ASP
- http://www.securityfocus.com/bid/3301
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-047
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7089
- http://support.microsoft.com/support/kb/articles/Q307/1/95.ASP

---

#### 170. CVE-2001-0666

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 2000 allows an authenticated user to cause a denial of service (CPU consumption) via a malformed OWA request for a deeply nested folder within the user's mailbox.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3368
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-049
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7168
- http://www.securityfocus.com/bid/3368
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-049

---

#### 171. CVE-2001-0718

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Vulnerability in (1) Microsoft Excel 2002 and earlier and (2) Microsoft PowerPoint 2002 and earlier allows attackers to bypass macro restrictions and execute arbitrary commands by modifying the data stream in the document.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/218802
- http://www.cert.org/advisories/CA-2001-28.html
- http://www.kb.cert.org/vuls/id/287067
- http://www.securityfocus.com/bid/3402
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-050

---

#### 172. CVE-2001-0902

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to spoof web log entries via an HTTP request that includes hex-encoded newline or form-feed characters.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100626531103946&w=2
- http://marc.info/?l=ntbugtraq&m=100627497122247&w=2
- http://www.securityfocus.com/bid/6795
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7613
- http://marc.info/?l=bugtraq&m=100626531103946&w=2

---

#### 173. CVE-2001-0909

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in helpctr.exe program in Microsoft Help Center for Windows XP allows remote attackers to execute arbitrary code via a long hcp: URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100638955422011&w=2
- http://www.securityfocus.com/bid/6802
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7605
- http://marc.info/?l=bugtraq&m=100638955422011&w=2
- http://www.securityfocus.com/bid/6802

---

#### 174. CVE-2001-0719

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Windows Media Player 6.4 allows remote attackers to execute arbitrary code via a malformed Advanced Streaming Format (ASF) file.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/202470
- http://www.iss.net/security_center/static/6962.php
- http://www.osvdb.org/5558
- http://www.securityfocus.com/bid/3156
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-056

---

#### 175. CVE-2001-0726

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Outlook Web Access (OWA) in Microsoft Exchange 5.5 Server, when used with Internet Explorer, does not properly detect certain inline script, which can allow remote attackers to perform arbitrary actions on a user's Exchange mailbox via an HTML e-mail message.

**参考链接 / References**:
- http://www.osvdb.org/5557
- http://www.securityfocus.com/bid/3650
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-057
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7663
- http://www.osvdb.org/5557

---

#### 176. CVE-2001-1186

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft IIS 5.0 allows remote attackers to cause a denial of service via an HTTP request with a content-length value that is larger than the size of the request, which prevents IIS from timing out the connection.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/244931
- http://online.securityfocus.com/archive/1/245100
- http://www.iss.net/security_center/static/7691.php
- http://www.securityfocus.com/archive/1/244892
- http://www.securityfocus.com/bid/3667

---

#### 177. CVE-2001-1200

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Microsoft Windows XP allows local users to bypass a locked screen and run certain programs that are associated with Hot Keys.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7713.php
- http://www.securityfocus.com/archive/1/246014
- http://www.securityfocus.com/bid/3703
- http://www.iss.net/security_center/static/7713.php
- http://www.securityfocus.com/archive/1/246014

---

#### 178. CVE-2001-0542

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in Microsoft SQL Server 7.0 and 2000 allow attackers with access to SQL Server to execute arbitrary code through the functions (1) raiserror, (2) formatmessage, or (3) xp_sprintf.  NOTE: the C runtime format string vulnerability reported in MS01-060 is identified by CVE-2001-0879.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100891252317406&w=2
- http://www.atstake.com/research/advisories/2001/a122001-1.txt
- http://www.kb.cert.org/vuls/id/700575
- http://www.securityfocus.com/bid/3733
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-060

---

#### 179. CVE-2001-1218

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Internet Explorer for Unix 5.0SP1 allows local users to possibly cause a denial of service (crash) in CDE or the X server on Solaris 2.6 by rapidly scrolling Chinese characters or maximizing the window.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/246611
- http://www.securityfocus.com/bid/3729
- http://www.securityfocus.com/archive/1/246611
- http://www.securityfocus.com/bid/3729

---

#### 180. CVE-2001-1219

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows malicious website operators to cause a denial of service (client crash) via JavaScript that continually refreshes the window via self.location.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/246649
- http://www.securityfocus.com/bid/3730
- http://www.securityfocus.com/archive/1/246649
- http://www.securityfocus.com/bid/3730

---

#### 181. CVE-2001-1489

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 6 allows remote attackers to cause a denial of service (CPU consumption and memory leak) via a web page with a large number of images.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/245152
- http://www.securityfocus.com/bid/3684
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7709
- http://www.securityfocus.com/archive/1/245152
- http://www.securityfocus.com/bid/3684

---

#### 182. CVE-2001-1497

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Microsoft Internet Explorer 4.0 through 6.0 could allow local users to differentiate between alphanumeric and non-alphanumeric characters used in a password by pressing certain control keys that jump between non-alphanumeric characters, which makes it easier to conduct a brute-force password guessing attack.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7592.php
- http://www.securityfocus.com/archive/1/241323
- http://www.securityfocus.com/archive/1/241400
- http://www.securityfocus.com/bid/3563
- http://www.iss.net/security_center/static/7592.php

---

#### 183. CVE-2002-0077

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 treats objects invoked on an HTML page with the codebase property as part of Local Computer zone, which allows remote attackers to invoke executables present on the local system through objects such as the popup object, aka the "Local Executable Invocation via Object tag" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101103188711920&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-015
- http://marc.info/?l=bugtraq&m=101103188711920&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-015

---

#### 184. CVE-2002-0018

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
In Microsoft Windows NT and Windows 2000, a trusting domain that receives authorization information from a trusted domain does not verify that the trusted domain is authoritative for all listed SIDs, which allows remote attackers to gain Domain Administrator privileges on the trusting domain by injecting SIDs from untrusted domains into the authorization data that comes from from the trusted domain.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3997
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-001
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8023
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A159
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A64

---

#### 185. CVE-2002-0021

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Network Product Identification (PID) Checker in Microsoft Office v. X for Mac allows remote attackers to cause a denial of service (crash) via a malformed product announcement.

**参考链接 / References**:
- http://www.osvdb.org/2041
- http://www.securityfocus.com/bid/4045
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-002
- http://www.osvdb.org/2041
- http://www.securityfocus.com/bid/4045

---

#### 186. CVE-2002-0049

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Microsoft Exchange Server 2000 System Attendant gives "Everyone" group privileges to the WinReg key, which could allow remote attackers to read or modify registry keys.

**参考链接 / References**:
- http://www.osvdb.org/2042
- http://www.securityfocus.com/bid/4053
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-003
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8092
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1022

---

#### 187. CVE-2002-0050

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 allows remote attackers to execute arbitrary code via long authentication data.

**参考链接 / References**:
- http://www.securityfocus.com/bid/4157
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-010
- http://www.securityfocus.com/bid/4157
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-010

---

#### 188. CVE-2002-0054

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SMTP service in (1) Microsoft Windows 2000 and (2) Internet Mail Connector (IMC) in Exchange Server 5.5 does not properly handle responses to NTLM authentication, which allows remote attackers to perform mail relaying via an SMTP AUTH command using null session credentials.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101501580409373&w=2
- http://www.securityfocus.com/bid/4205
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-011
- http://marc.info/?l=bugtraq&m=101501580409373&w=2
- http://www.securityfocus.com/bid/4205

---

#### 189. CVE-2002-0055

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
SMTP service in Microsoft Windows 2000, Windows XP Professional, and Exchange 2000 allows remote attackers to cause a denial of service via a command with a malformed data transfer (BDAT) request.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101558498401274&w=2
- http://www.iss.net/security_center/static/8307.php
- http://www.securityfocus.com/bid/4204
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-012
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A30

---

#### 190. CVE-2002-0057

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
XMLHTTP control in Microsoft XML Core Services 2.6 and later does not properly handle IE Security Zone settings, which allows remote attackers to read arbitrary files by specifying a local file as an XML Data Source.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-12/0152.html
- http://marc.info/?l=bugtraq&m=101366383408821&w=2
- http://www.osvdb.org/3032
- http://www.securityfocus.com/bid/3699
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-008

---

#### 191. CVE-2002-0101

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 6.0 and earlier allows local users to cause a denial of service via an infinite loop for modeless dialogs showModelessDialog, which causes CPU usage while the focus for the dialog is not released.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101039104608083&w=2
- http://www.iss.net/security_center/static/7826.php
- http://www.securityfocus.com/bid/3789
- http://marc.info/?l=bugtraq&m=101039104608083&w=2
- http://www.iss.net/security_center/static/7826.php

---

#### 192. CVE-2002-0136

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 on Windows 98 allows remote web pages to cause a denial of service (hang) via extremely long values for form fields such as INPUT and TEXTAREA, which can be automatically filled via Javascript.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/250592
- http://www.securityfocus.com/bid/3892
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7938
- http://online.securityfocus.com/archive/1/250592
- http://www.securityfocus.com/bid/3892

---

#### 193. CVE-2002-0078

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The zone determination function in Microsoft Internet Explorer 5.5 and 6.0 allows remote attackers to run scripts in the Local Computer zone by embedding the script in a cookie, aka the "Cookie-based Script Execution" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101781180528301&w=2
- http://www.iss.net/security_center/static/8701.php
- http://www.osvdb.org/3029
- http://www.securityfocus.com/bid/4392
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-015

---

#### 194. CVE-2002-0151

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflow in Multiple UNC Provider (MUP) in Microsoft Windows operating systems allows local users to cause a denial of service or possibly gain SYSTEM privileges via a long UNC request.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101793727306282&w=2
- http://www.iss.net/security_center/static/8752.php
- http://www.securityfocus.com/bid/4426
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-017
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A145

---

#### 195. CVE-2002-0152

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in various Microsoft applications for Macintosh allows remote attackers to cause a denial of service (crash) or execute arbitrary code by invoking the file:// directive with a large number of / characters, which affects Internet Explorer 5.1, Outlook Express 5.0 through 5.0.2, Entourage v. X and 2001, PowerPoint v. X, 2001, and 98, and Excel v. X and 2001 for Macintosh.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101897994314015&w=2
- http://www.iss.net/security_center/static/8850.php
- http://www.osvdb.org/5357
- http://www.securityfocus.com/bid/4517
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-019

---

#### 196. CVE-2002-0154

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflows in extended stored procedures for Microsoft SQL Server 7.0 and 2000 allow remote attackers to cause a denial of service or execute arbitrary code via a database query with certain long arguments.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101535353331625&w=2
- http://www.cert.org/advisories/CA-2002-22.html
- http://www.kb.cert.org/vuls/id/627275
- http://www.securityfocus.com/archive/1/261775
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-020

---

#### 197. CVE-2002-0224

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The MSDTC (Microsoft Distributed Transaction Service Coordinator) for Microsoft Windows 2000, Microsoft IIS 5.0 and SQL Server 6.5 through SQL 2000 0.0 allows remote attackers to cause a denial of service (crash or hang) via malformed (random) input.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/253360
- http://online.securityfocus.com/archive/1/268593
- http://www.iss.net/security_center/static/8046.php
- http://www.securityfocus.com/bid/4006
- http://online.securityfocus.com/archive/1/253360

---

#### 198. CVE-2002-0228

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft MSN Messenger allows remote attackers to use Javascript that references an ActiveX object to obtain sensitive information such as display names and web site navigation, and possibly more when the user is connected to certain Microsoft sites (or DNS-spoofed sites).

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/254021
- http://www.iss.net/security_center/static/8084.php
- http://www.securityfocus.com/bid/4028
- http://online.securityfocus.com/archive/1/254021
- http://www.iss.net/security_center/static/8084.php

---

#### 199. CVE-2002-1056

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Outlook 2000 and 2002, when configured to use Microsoft Word as the email editor, does not block scripts that are used while editing email messages in HTML or Rich Text Format (RTF), which could allow remote attackers to execute arbitrary scripts via an email that the user forwards or replies to.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101760380418890&w=2
- http://online.securityfocus.com/archive/1/265621
- http://www.iss.net/security_center/static/8708.php
- http://www.securityfocus.com/bid/4397
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-021

---

#### 200. CVE-2002-0155

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft MSN Chat ActiveX Control, as used in MSN Messenger 4.5 and 4.6, and Exchange Instant Messenger 4.5 and 4.6, allows remote attackers to execute arbitrary code via a long ResDLL parameter in the MSNChat OCX.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102089960531919&w=2
- http://www.cert.org/advisories/CA-2002-13.html
- http://www.iss.net/security_center/static/9041.php
- http://www.securityfocus.com/bid/4707
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-022

---

#### 201. CVE-2002-0188

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the second variant of the "Content Disposition" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-05/0126.html
- http://www.iss.net/security_center/static/9086.php
- http://www.lac.co.jp/security/english/snsadv_e/48_e.html
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-023
- http://archives.neohapsis.com/archives/bugtraq/2002-05/0126.html

---

#### 202. CVE-2002-0190

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to execute arbitrary code under fewer security restrictions via a malformed web page that requires NetBIOS connectivity, aka "Zone Spoofing through Malformed Web Page" vulnerability.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9084.php
- http://www.kb.cert.org/vuls/id/242891
- http://www.securityfocus.com/bid/4753
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-023
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A923

---

#### 203. CVE-2002-0191

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5 and 6.0 allows remote attackers to view arbitrary files that contain the "{" character via script containing the cssText property of the stylesheet object, aka "Local Information Disclosure through HTML Object" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101778302030981&w=2
- http://www.iss.net/security_center/static/8740.php
- http://www.securityfocus.com/bid/4411
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-023
- http://marc.info/?l=bugtraq&m=101778302030981&w=2

---

#### 204. CVE-2002-0193

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 6.0 allow remote attackers to execute arbitrary code via malformed Content-Disposition and Content-Type header fields that cause the application for the spoofed file type to pass the file back to the operating system for handling rather than raise an error message, aka the first variant of the "Content Disposition" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/4752
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-023
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9085
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A27
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A99

---

#### 205. CVE-2002-0368

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Store Service in Microsoft Exchange 2000 allows remote attackers to cause a denial of service (CPU consumption) via a mail message with a malformed RFC message attribute, aka "Malformed Mail Attribute can Cause Exchange 2000 to Exhaust CPU Resources."

**参考链接 / References**:
- http://www.iss.net/security_center/static/9195.php
- http://www.securityfocus.com/bid/4881
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-025
- http://www.iss.net/security_center/static/9195.php
- http://www.securityfocus.com/bid/4881

---

#### 206. CVE-2002-0597

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
LANMAN service on Microsoft Windows 2000 allows remote attackers to cause a denial of service (CPU/memory exhaustion) via a stream of malformed data to microsoft-ds port 445.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0025.html
- http://online.securityfocus.com/archive/1/268066
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ320751
- http://www.iss.net/security_center/static/8867.php
- http://www.kb.cert.org/vuls/id/693099

---

#### 207. CVE-2002-0186

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the SQLXML ISAPI extension of Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code via data queries with a long content-type parameter, aka "Unchecked Buffer in SQLXML ISAPI Extension."

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html
- http://marc.info/?l=bugtraq&m=102397345410856&w=2
- http://www.iss.net/security_center/static/9328.php
- http://www.kb.cert.org/vuls/id/811371
- http://www.osvdb.org/5347

---

#### 208. CVE-2002-0187

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Cross-site scripting vulnerability in the SQLXML component of Microsoft SQL Server 2000 allows an attacker to execute arbitrary script via the root parameter as part of an XML SQL query, aka "Script Injection via XML Tag."

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html
- http://marc.info/?l=bugtraq&m=102397345410856&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-030
- http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0100.html
- http://marc.info/?l=bugtraq&m=102397345410856&w=2

---

#### 209. CVE-2002-0371

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in gopher client for Microsoft Internet Explorer 5.1 through 6.0, Proxy Server 2.0, or ISA Server 2000 allows remote attackers to execute arbitrary code via a gopher:// URL that redirects the user to a real or simulated gopher server that sends a long response.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102320516707940&w=2
- http://marc.info/?l=bugtraq&m=102397955217618&w=2
- http://online.securityfocus.com/archive/1/276848
- http://www.iss.net/security_center/static/9247.php
- http://www.kb.cert.org/vuls/id/440275

---

#### 210. CVE-2002-0372

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Windows Media Player versions 6.4 and 7.1 and Media Player for Windows XP allow remote attackers to bypass Internet Explorer's (IE) security mechanisms and run code via an executable .wma media file with a license installation requirement stored in the IE cache, aka the "Cache Path Disclosure via Windows Media Player".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9420.php
- http://www.securityfocus.com/bid/5107
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-032
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A281
- http://www.iss.net/security_center/static/9420.php

---

#### 211. CVE-2002-0373

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Windows Media Device Manager (WMDM) Service in Microsoft Windows Media Player 7.1 on Windows 2000 systems allows local users to obtain LocalSystem rights via a program that calls the WMDM service to connect to an invalid local storage device, aka "Privilege Elevation through Windows Media Device Manager Service".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9421.php
- http://www.securityfocus.com/bid/5109
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-032
- http://www.iss.net/security_center/static/9421.php
- http://www.securityfocus.com/bid/5109

---

#### 212. CVE-2002-0615

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Windows Media Active Playlist in Microsoft Windows Media Player 7.1 stores information in a well known location on the local file system, allowing attackers to execute HTML scripts in the Local Computer zone, aka "Media Playback Script Invocation".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9422.php
- http://www.securityfocus.com/bid/5110
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-032
- http://www.iss.net/security_center/static/9422.php
- http://www.securityfocus.com/bid/5110

---

#### 213. CVE-2002-0620

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in the Profile Service of Microsoft Commerce Server 2000 allows remote attackers to cause the server to fail or run arbitrary code in the LocalSystem security context via an input field using an affected API.

**参考链接 / References**:
- http://www.securityfocus.com/bid/4853
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-033
- http://www.securityfocus.com/bid/4853
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-033

---

#### 214. CVE-2002-0621

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in the Office Web Components (OWC) package installer used by Microsoft Commerce Server 2000 allows remote attackers to cause the process to fail or run arbitrary code in the LocalSystem security context via certain input to the OWC package installer.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9424.php
- http://www.osvdb.org/5172
- http://www.securityfocus.com/bid/5108
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-033
- http://www.iss.net/security_center/static/9424.php

---

#### 215. CVE-2002-0622

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Office Web Components (OWC) package installer for Microsoft Commerce Server 2000 allows remote attackers to execute commands by passing the commands as input to the OWC package installer, aka "OWC Package Command Execution".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9425.php
- http://www.osvdb.org/5170
- http://www.securityfocus.com/bid/5111
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-033
- http://www.iss.net/security_center/static/9425.php

---

#### 216. CVE-2002-0623

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in AuthFilter ISAPI filter on Microsoft Commerce Server 2000 and 2002 allows remote attackers to execute arbitrary code via long authentication data, aka "New Variant of the ISAPI Filter Buffer Overrun".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9426.php
- http://www.osvdb.org/5163
- http://www.securityfocus.com/bid/5112
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-033
- http://www.iss.net/security_center/static/9426.php

---

#### 217. CVE-2002-0624

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the password encryption function of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows remote attackers to gain control of the database and execute arbitrary code via SQL Server Authentication, aka "Unchecked Buffer in Password Encryption Procedure."

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2002-22.html
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-034
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A291
- http://www.cert.org/advisories/CA-2002-22.html
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-034

---

#### 218. CVE-2002-0641

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in bulk insert procedure of Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, allows attackers with database administration privileges to execute arbitrary code via a long filename in the BULK INSERT query.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102639885223746&w=2
- http://www.kb.cert.org/vuls/id/682620
- http://www.ngssoftware.com/advisories/ms-sqlbi.txt
- http://www.securityfocus.com/bid/4847
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-034

---

#### 219. CVE-2002-0642

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The registry key containing the SQL Server service account information in Microsoft SQL Server 2000, including Microsoft SQL Server Desktop Engine (MSDE) 2000, has insecure permissions, which allows local users to gain privileges, aka "Incorrect Permission on SQL Server Service Account Registry Key."

**参考链接 / References**:
- http://www.cert.org/advisories/CA-2002-22.html
- http://www.iss.net/security_center/static/9523.php
- http://www.kb.cert.org/vuls/id/796313
- http://www.securityfocus.com/bid/5205
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-034

---

#### 220. CVE-2002-0643

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The installation of Microsoft Data Engine 1.0 (MSDE 1.0), and Microsoft SQL Server 2000 creates setup.iss files with insecure permissions and does not delete them after installation, which allows local users to obtain sensitive data, including weakly encrypted passwords, to gain privileges, aka "SQL Server Installation Process May Leave Passwords on System."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102640092826731&w=2
- http://marc.info/?l=vuln-dev&m=102640394131103&w=2
- http://www.kb.cert.org/vuls/id/338195
- http://www.securityfocus.com/bid/5203
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-035

---

#### 221. CVE-2002-0409

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
orderdetails.aspx, as made available to Microsoft .NET developers as example code and demonstrated on www.ibuyspystore.com, allows remote attackers to view the orders of other users by modifying the OrderID parameter.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101518860823788&w=2
- http://marc.info/?l=bugtraq&m=101518860823788&w=2

---

#### 222. CVE-2002-0443

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows 2000 allows local users to bypass the policy that prohibits reusing old passwords by changing the current password before it expires, which does not enable the check for previous passwords.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/260704
- http://www.iss.net/security_center/static/8402.php
- http://www.securityfocus.com/bid/4256
- http://online.securityfocus.com/archive/1/260704
- http://www.iss.net/security_center/static/8402.php

---

#### 223. CVE-2002-0444

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Windows 2000 running the Terminal Server 90-day trial version, and possibly other versions, does not apply group policies to incoming users when the number of connections to the SYSVOL share exceeds the maximum, e.g. with a maximum number of licenses, which can allow remote authenticated users to bypass group policies.

**参考链接 / References**:
- http://www.iss.net/security_center/static/8813.php
- http://www.securityfocus.com/archive/1/266729
- http://www.securityfocus.com/bid/4464
- http://www.iss.net/security_center/static/8813.php
- http://www.securityfocus.com/archive/1/266729

---

#### 224. CVE-2000-1209

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The "sa" account is installed with a default null password on (1) Microsoft SQL Server 2000, (2) SQL Server 7.0, and (3) Data Engine (MSDE) 1.0, including third party packages that use these products such as (4) Tumbleweed Secure Mail (MMS) (5) Compaq Insight Manager, and (6) Visio 2000, which allows remote attackers to gain privileges, as exploited by worms such as Voyager Alpha Force and Spida.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=96333895000350&w=2
- http://marc.info/?l=bugtraq&m=96593218804850&w=2
- http://marc.info/?l=bugtraq&m=96644570412692&w=2
- http://online.securityfocus.com/archive/1/273639
- http://security-archive.merton.ox.ac.uk/bugtraq-200008/0233.html

---

#### 225. CVE-2002-0507

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
An interaction between Microsoft Outlook Web Access (OWA) with RSA SecurID allows local users to bypass the SecurID authentication for a previous user via several submissions of an OWA Authentication request with the proper OWA password for the previous user, which is eventually accepted by OWA.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/264705
- http://www.iss.net/security_center/static/8681.php
- http://www.securityfocus.com/bid/4390
- http://online.securityfocus.com/archive/1/264705
- http://www.iss.net/security_center/static/8681.php

---

#### 226. CVE-2002-0616

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by attaching an inline macro to an object within an Excel workbook, aka the "Excel Inline Macros Vulnerability."

**参考链接 / References**:
- http://www.iss.net/security_center/static/9397.php
- http://www.securityfocus.com/bid/5063
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-031
- http://www.iss.net/security_center/static/9397.php
- http://www.securityfocus.com/bid/5063

---

#### 227. CVE-2002-0617

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code by creating a hyperlink on a drawing shape in a source workbook that points to a destination workbook containing an autoexecute macro, aka "Hyperlinked Excel Workbook Macro Bypass."

**参考链接 / References**:
- http://www.osvdb.org/5175
- http://www.securityfocus.com/bid/5064
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-031
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9398
- http://www.osvdb.org/5175

---

#### 228. CVE-2002-0618

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Macro Security Model in Microsoft Excel 2000 and 2002 for Windows allows remote attackers to execute code in the Local Computer zone by embedding HTML scripts within an Excel workbook that contains an XSL stylesheet, aka "Excel XSL Stylesheet Script Execution".

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=102256054320377&w=2
- http://www.guninski.com/ex%24el2.html
- http://www.iss.net/security_center/static/9399.php
- http://www.securityfocus.com/bid/4821
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-031

---

#### 229. CVE-2002-0619

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Mail Merge Tool in Microsoft Word 2002 for Windows, when Microsoft Access is present on a system, allows remote attackers to execute Visual Basic (VBA) scripts within a mail merge document that is saved in HTML format, aka a "Variant of MS00-071, Word Mail Merge Vulnerability" (CVE-2000-0788).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102139136019862&w=2
- http://www.iss.net/security_center/static/9077.php
- http://www.securityfocus.com/bid/5066
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-031
- http://marc.info/?l=bugtraq&m=102139136019862&w=2

---

#### 230. CVE-2002-0644

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in several Database Consistency Checkers (DBCCs) for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows members of the db_owner and db_ddladmin roles to execute arbitrary code.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038

---

#### 231. CVE-2002-0645

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SQL injection vulnerability in stored procedures for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 may allow authenticated users to execute arbitrary commands.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-038

---

#### 232. CVE-2002-0649

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Multiple buffer overflows in the Resolution Service for Microsoft SQL Server 2000 and Microsoft Desktop Engine 2000 (MSDE) allow remote attackers to cause a denial of service or execute arbitrary code via UDP packets to port 1434 in which (1) a 0x04 byte that causes the SQL Monitor thread to generate a long registry key name, or (2) a 0x08 byte with a long string causes heap corruption, as exploited by the Slammer/Sapphire worm.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102760196931518&w=2
- http://marc.info/?l=ntbugtraq&m=102760479902411&w=2
- http://secunia.com/advisories/7945
- http://www.cert.org/advisories/CA-2002-22.html
- http://www.cert.org/advisories/CA-2003-04.html

---

#### 233. CVE-2002-0650

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The keep-alive mechanism for Microsoft SQL Server 2000 allows remote attackers to cause a denial of service (bandwidth consumption) via a "ping" style packet to the Resolution Service (UDP port 1434) with a spoofed IP address of another SQL Server system, which causes the two servers to exchange packets in an infinite loop.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102760196931518&w=2
- http://marc.info/?l=ntbugtraq&m=102760479902411&w=2
- http://www.iss.net/security_center/static/9662.php
- http://www.osvdb.org/878
- http://www.securityfocus.com/bid/5312

---

#### 234. CVE-2002-0695

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the Transact-SQL (T-SQL) OpenRowSet component of Microsoft Data Access Components (MDAC) 2.5 through 2.7 for SQL Server 7.0 or 2000 allows remote attackers to execute arbitrary code via a query that calls the OpenRowSet command.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9734.php
- http://www.nextgenss.com/advisories/mssql-ors.txt
- http://www.securityfocus.com/bid/5372
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-040
- http://www.iss.net/security_center/static/9734.php

---

#### 235. CVE-2002-0697

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft Metadirectory Services (MMS) 2.2 allows remote attackers to bypass authentication and modify sensitive data by using an LDAP client to directly connect to MMS and bypass the checks for MMS credentials.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9657.php
- http://www.securityfocus.com/bid/5308
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-036
- http://www.iss.net/security_center/static/9657.php
- http://www.securityfocus.com/bid/5308

---

#### 236. CVE-2002-0698

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Internet Mail Connector (IMC) for Microsoft Exchange Server 5.5 allows remote attackers to execute arbitrary code via an EHLO request from a system with a long name as obtained through a reverse DNS lookup, which triggers the overflow in IMC's hello response.

**参考链接 / References**:
- http://bvlive01.iss.net/issEn/delivery/xforce/alertdetail.jsp?oid=20759
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ326322
- http://www.iss.net/security_center/static/9658.php
- http://www.securityfocus.com/bid/5306
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-037

---

#### 237. CVE-2002-0700

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in a system function that performs user authentication for Microsoft Content Management Server (MCMS) 2001 allows attackers to execute code in the Local System context by authenticating to a web page that calls the function, aka "Unchecked Buffer in MDAC Function Could Enable SQL Server Compromise."

**参考链接 / References**:
- http://www.iss.net/security_center/static/9783.php
- http://www.osvdb.org/4862
- http://www.securityfocus.com/bid/5420
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-041
- http://www.iss.net/security_center/static/9783.php

---

#### 238. CVE-2002-0718

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Web authoring command in Microsoft Content Management Server (MCMS) 2001 allows attackers to authenticate and upload executable content, by modifying the upload location, aka "Program Execution via MCMS Authoring Function."

**参考链接 / References**:
- http://www.iss.net/security_center/static/9784.php
- http://www.securityfocus.com/bid/5421
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-041
- http://www.iss.net/security_center/static/9784.php
- http://www.securityfocus.com/bid/5421

---

#### 239. CVE-2002-0719

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SQL injection vulnerability in the function that services for Microsoft Content Management Server (MCMS) 2001 allows remote attackers to execute arbitrary commands via an MCMS resource request for image files or other files.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9785.php
- http://www.securityfocus.com/bid/5422
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-041
- http://www.iss.net/security_center/static/9785.php
- http://www.securityfocus.com/bid/5422

---

#### 240. CVE-2002-0729

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft SQL Server 2000 allows remote attackers to cause a denial of service via a malformed 0x08 packet that is missing a colon separator.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102760196931518&w=2
- http://marc.info/?l=ntbugtraq&m=102760479902411&w=2
- http://marc.info/?l=bugtraq&m=102760196931518&w=2
- http://marc.info/?l=ntbugtraq&m=102760479902411&w=2

---

#### 241. CVE-2002-0736

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft BackOffice 4.0 and 4.5, when configured to be accessible by other systems, allows remote attackers to bypass authentication and access the administrative ASP pages via an HTTP request with an authorization type (auth_type) that is not blank.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-04/0208.html
- http://support.microsoft.com/support/kb/articles/q316/8/38.asp
- http://www.iss.net/security_center/static/8862.php
- http://www.securityfocus.com/bid/4528
- http://archives.neohapsis.com/archives/bugtraq/2002-04/0208.html

---

#### 242. CVE-2002-0721

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000 installs with weak permissions for extended stored procedures that are associated with helper functions, which could allow unprivileged users, and possibly remote attackers, to run stored procedures with administrator privileges via (1) xp_execresultset, (2) xp_printstatements, or (3) xp_displayparamstmt.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2002-q3/0087.html
- http://marc.info/?l=bugtraq&m=102950473002959&w=2
- http://marc.info/?l=ntbugtraq&m=102950792606475&w=2
- http://www.kb.cert.org/vuls/id/399531
- http://www.kb.cert.org/vuls/id/818939

---

#### 243. CVE-2002-0859

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the OpenDataSource function of the Jet engine on Microsoft SQL Server 2000 allows remote attackers to execute arbitrary code.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102450188620081&w=2
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ282010
- http://www.iss.net/security_center/static/9375.php
- http://www.nextgenss.com/advisories/mssql-ods.txt
- http://www.securityfocus.com/bid/5057

---

#### 244. CVE-2002-0647

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in a legacy ActiveX control used to display specially formatted text in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to execute arbitrary code, aka "Buffer Overrun in Legacy Text Formatting ActiveX Control".

**参考链接 / References**:
- http://www.iss.net/security_center/static/9935.php
- http://www.securityfocus.com/bid/5558
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-047
- http://www.iss.net/security_center/static/9935.php
- http://www.securityfocus.com/bid/5558

---

#### 245. CVE-2002-0648

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The legacy <script> data-island capability for XML in Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to read arbitrary XML files, and portions of other files, via a URL whose "src" attribute redirects to a local file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103011639524314&w=2
- http://www.iss.net/security_center/static/9936.php
- http://www.securityfocus.com/bid/5560
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-047
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1026

---

#### 246. CVE-2002-0691

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01 and 5.5 allows remote attackers to execute scripts in the Local Computer zone via a URL that references a local HTML resource file, a variant of "Cross-Site Scripting in Local HTML Resource" as identified by CAN-2002-0189.

**参考链接 / References**:
- http://www.iss.net/security_center/static/9938.php
- http://www.securityfocus.com/bid/5561
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-047
- http://www.iss.net/security_center/static/9938.php
- http://www.securityfocus.com/bid/5561

---

#### 247. CVE-2002-0722

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.01, 5.5, and 6.0 allows remote attackers to misrepresent the source of a file in the File Download dialogue box to trick users into thinking that the file type is safe to download, aka "File Origin Spoofing."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103054692223380&w=2
- http://www.iss.net/security_center/static/9937.php
- http://www.osvdb.org/5129
- http://www.securityfocus.com/bid/5559
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-047

---

#### 248. CVE-2002-0723

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Internet Explorer 5.5 and 6.0 does not properly verify the domain of a frame within a browser window, which allows remote attackers to read client files or invoke executable objects via the Object tag, aka "Cross Domain Verification in Object Tag."

**参考链接 / References**:
- http://www.iss.net/security_center/static/9537.php
- http://www.securityfocus.com/bid/5196
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-047
- http://www.iss.net/security_center/static/9537.php
- http://www.securityfocus.com/bid/5196

---

#### 249. CVE-2002-0724

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in SMB (Server Message Block) protocol in Microsoft Windows NT, Windows 2000, and Windows XP allows attackers to cause a denial of service (crash) via a SMB_COM_TRANSACTION packet with a request for the (1) NetShareEnum, (2) NetServerEnum2, or (3) NetServerEnum3, aka "Unchecked Buffer in Network Share Provider Can Lead to Denial of Service".

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103011556323184&w=2
- http://www.kb.cert.org/vuls/id/250635
- http://www.kb.cert.org/vuls/id/311619
- http://www.kb.cert.org/vuls/id/342243
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-045

---

#### 250. CVE-2002-0726

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft Terminal Services Advanced Client (TSAC) ActiveX control allows remote attackers to execute arbitrary code via a long server name field.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2002/a082802-1.txt
- http://www.iss.net/security_center/static/9934.php
- http://www.securityfocus.com/bid/5554
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-046
- http://www.atstake.com/research/advisories/2002/a082802-1.txt

---

#### 251. CVE-2002-0727

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Host function in Microsoft Office Web Components (OWC) 2000 and 2002 is exposed in components that are marked as safe for scripting, which allows remote attackers to execute arbitrary commands via the setTimeout method.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101829645415486&w=2
- http://www.iss.net/security_center/static/8777.php
- http://www.osvdb.org/3006
- http://www.securityfocus.com/bid/4449
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-044

---

#### 252. CVE-2002-0860

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The LoadText method in the spreadsheet component in Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to read arbitrary files through Internet Explorer via a URL that redirects to the target file.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101829911018463&w=2
- http://www.iss.net/security_center/static/8778.php
- http://www.osvdb.org/3007
- http://www.securityfocus.com/bid/4453
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-044

---

#### 253. CVE-2002-0861

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Office Web Components (OWC) 2000 and 2002 allows remote attackers to bypass the "Allow paste operations via script" setting, even when it is disabled, via the (1) Copy method of the Cell object or (2) the Paste method of the Range object.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101829726516346&w=2
- http://www.iss.net/security_center/static/8779.php
- http://www.securityfocus.com/bid/4457
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-044
- http://marc.info/?l=bugtraq&m=101829726516346&w=2

---

#### 254. CVE-2002-0975

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft DirectX Files Viewer ActiveX control (xweb.ocx) 2.0.6.15 and earlier allows remote attackers to execute arbitrary via a long File parameter.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102953851705859&w=2
- http://www.iss.net/security_center/static/9877.php
- http://www.securityfocus.com/bid/5489
- http://marc.info/?l=bugtraq&m=102953851705859&w=2
- http://www.iss.net/security_center/static/9877.php

---

#### 255. CVE-2002-0977

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to execute arbitrary code via a long TS value.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html
- http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html

---

#### 256. [webapps] Python-Multipart 0.0.22 - Path Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Python-Multipart 0.0.22 - Path Traversal

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52543

---

#### 257. [local] Google Chrome  145.0.7632.75 - CSSFontFeatureValuesMap

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Google Chrome 145.0.7632.75 - CSSFontFeatureValuesMap

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52542

---

#### 258. [local] Windows 11 23H2 - Denial of Service (DoS)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Windows 11 23H2 - Denial of Service (DoS)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52541

---

#### 259. [webapps] Repetier-Server 1.4.10 - Path Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Repetier-Server 1.4.10 - Path Traversal

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52540

---

#### 260. [webapps] HUSTOJ Zip-Slip v26.01.24 -  RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] HUSTOJ Zip-Slip v26.01.24 - RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52539

---

#### 261. [webapps] BusyBox 1.37.0 - Path Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] BusyBox 1.37.0 - Path Traversal

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52538

---

#### 262. [local] Windows 11 25H2  - Heap Overflow

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Windows 11 25H2 - Heap Overflow

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52537

---

#### 263. [webapps] JUNG Smart Visu Server 1.1.1050 - Dos

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] JUNG Smart Visu Server 1.1.1050 - Dos

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52536

---

#### 264. [webapps] SumatraPDF 3.5.2 - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] SumatraPDF 3.5.2 - Remote Code Execution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52535

---

#### 265. [webapps] NiceGUI 3.6.1 - Path Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] NiceGUI 3.6.1 - Path Traversal

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52534

---

#### 266. [webapps] Frigate NVR 0.16.3 - Remote Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Frigate NVR 0.16.3 - Remote Code Execution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52533

---

#### 267. [webapps] Js2Py 0.74 -  RCE

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Js2Py 0.74 - RCE

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52532

---

#### 268. [webapps] Camaleon CMS  v2.9.0 - Path Traversal

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Camaleon CMS v2.9.0 - Path Traversal

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52531

---

#### 269. [webapps] Cybersecurity AI (CAI) Framework 0.5.10 - Command Injection

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Cybersecurity AI (CAI) Framework 0.5.10 - Command Injection

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52530

---

#### 270. [webapps] Erugo  0.2.14 - Remote Code Execution (RCE)

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] Erugo 0.2.14 - Remote Code Execution (RCE)

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52529

---

#### 271. [webapps] deephas 1.0.7 - Prototype Pollution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] deephas 1.0.7 - Prototype Pollution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52528

---

#### 272. [webapps] SUSE Manager 4.3.15 - Code Execution

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] SUSE Manager 4.3.15 - Code Execution

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52527

---

#### 273. CVE-2002-0978

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft File Transfer Manager (FTM) ActiveX control before 4.0 allows remote attackers to upload or download arbitrary files to arbitrary locations via a man-in-the-middle attack with modified TGT and TGN parameters in a call to the "Persist" function.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html
- http://archives.neohapsis.com/archives/bugtraq/2002-08/0189.html

---

#### 274. CVE-2002-0982

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft SQL Server 2000 SP2, when configured as a distributor, allows attackers to execute arbitrary code via the @scriptfile parameter to the sp_MScopyscript stored procedure.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103004505027360&w=2
- http://marc.info/?l=bugtraq&m=103004505027360&w=2

---

#### 275. CVE-2002-1123

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the authentication function for Microsoft SQL Server 2000 and Microsoft Desktop Engine (MSDE) 2000 allows remote attackers to execute arbitrary code via a long request to TCP port 1433, aka the "Hello" overflow.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102873609025020&w=2
- http://online.securityfocus.com/archive/1/286220
- http://www.ciac.org/ciac/bulletins/n-003.shtml
- http://www.iss.net/security_center/static/9788.php
- http://www.securityfocus.com/bid/5411

---

#### 276. CVE-2002-0696

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Visual FoxPro 6.0 does not register its associated files with Internet Explorer, which allows remote attackers to execute Visual FoxPro applications without warning via HTML that references specially-crafted filenames.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/m-120.shtml
- http://www.iss.net/security_center/static/10035.php
- http://www.securityfocus.com/bid/5633
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-049
- http://www.ciac.org/ciac/bulletins/m-120.shtml

---

#### 277. CVE-2002-0699

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Unknown vulnerability in the Certificate Enrollment ActiveX Control in Microsoft Windows 98, Windows 98 Second Edition, Windows Millennium, Windows NT 4.0, Windows 2000, and Windows XP allow remote attackers to delete digital certificates on a user's system via HTML.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-048
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A190
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-048
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A190

---

#### 278. CVE-2002-0862

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
The (1) CertGetCertificateChain, (2) CertVerifyCertificateChainPolicy, and (3) WinVerifyTrust APIs within the CryptoAPI for Microsoft products including Microsoft Windows 98 through XP, Office for Mac, Internet Explorer for Mac, and Outlook Express for Mac, do not properly verify the Basic Constraints of intermediate CA-signed X.509 certificates, which allows remote attackers to spoof the certificates of trusted sites via a man-in-the-middle attack for SSL sessions, as originally reported for Internet Explorer and IIS.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=102866120821995&w=2
- http://marc.info/?l=bugtraq&m=102918200405308&w=2
- http://marc.info/?l=bugtraq&m=102976967730450&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-050
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9776

---

#### 279. CVE-2002-1015

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
RealJukebox 2 1.0.2.340 and 1.0.2.379, and RealOne Player Gold 6.0.10.505, allows remote attackers to execute arbitrary script in the Local computer zone by inserting the script into the skin.ini file of an RJS archive, then referencing skin.ini from a web page after it has been extracted, which is parsed as HTML by Internet Explorer or other Microsoft-based web readers.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2002-07/0130.html
- http://service.real.com/help/faq/security/bufferoverrun07092002.html
- http://www.iss.net/security_center/static/9539.php
- http://www.kb.cert.org/vuls/id/888547
- http://www.securityfocus.com/bid/5210

---

#### 280. CVE-2002-1117

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Veritas Backup Exec 8.5 and earlier requires that the "RestrictAnonymous" registry key for Microsoft Exchange 2000 must be set to 0, which enables anonymous listing of the SAM database and shares.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103134395124579&w=2
- http://marc.info/?l=bugtraq&m=103134930629683&w=2
- http://seer.support.veritas.com/docs/238618.htm
- http://www.osvdb.org/8230
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10093

---

#### 281. CVE-2002-0370

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the ZIP capability for multiple products allows remote attackers to cause a denial of service or execute arbitrary code via ZIP files containing entries with long filenames, including (1) Microsoft Windows 98 with Plus! Pack, (2) Windows XP, (3) Windows ME, (4) Lotus Notes R4 through R6 (pre-gold), (5) Verity KeyView, and (6) Stuffit Expander before 7.0.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0009.html
- http://marc.info/?l=bugtraq&m=103428193409223&w=2
- http://securityreason.com/securityalert/587
- http://www.info-zip.org/FAQ.html
- http://www.info.apple.com/usen/security/security_updates.html

---

#### 282. CVE-2002-0692

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in SmartHTML Interpreter (shtml.dll) in Microsoft FrontPage Server Extensions (FPSE) 2000 and 2002 allows remote attackers to cause a denial of service (CPU consumption) or run arbitrary code, respectively, via a certain type of web file request.

**参考链接 / References**:
- http://www.iss.net/security_center/static/10194.php
- http://www.iss.net/security_center/static/10195.php
- http://www.kb.cert.org/vuls/id/723537
- http://www.securityfocus.com/bid/5804
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-053

---

#### 283. CVE-2002-0693

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the HTML Help ActiveX Control (hhctrl.ocx) in Microsoft Windows 98, 98 Second Edition, Millennium Edition, NT 4.0, NT 4.0 Terminal Server Edition, Windows 2000, and Windows XP allows remote attackers to execute code via (1) a long parameter to the Alink function, or (2) script containing a long argument to the showHelp function.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103365849505409&w=2
- http://marc.info/?l=bugtraq&m=103419115517344&w=2
- http://marc.info/?l=bugtraq&m=103435279404182&w=2
- http://www.iss.net/security_center/static/10253.php
- http://www.securityfocus.com/bid/5874

---

#### 284. CVE-2002-0863

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Remote Data Protocol (RDP) version 5.0 in Microsoft Windows 2000 and RDP 5.1 in Windows XP does not encrypt the checksums of plaintext session data, which could allow a remote attacker to determine the contents of encrypted sessions via sniffing, aka "Weak Encryption in RDP Protocol."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103235960119404&w=2
- http://marc.info/?l=bugtraq&m=103236181522253&w=2
- http://www.iss.net/security_center/static/10121.php
- http://www.iss.net/security_center/static/10122.php
- http://www.kb.cert.org/vuls/id/865833

---

#### 285. CVE-2002-0864

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Remote Data Protocol (RDP) version 5.1 in Microsoft Windows XP allows remote attackers to cause a denial of service (crash) when Remote Desktop is enabled via a PDU Confirm Active data packet that does not set the Pattern BLT command, aka "Denial of Service in Remote Desktop."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103235745116592&w=2
- http://marc.info/?l=bugtraq&m=103236181522253&w=2
- http://www.iss.net/security_center/static/10120.php
- http://www.securityfocus.com/bid/5713
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-051

---

#### 286. CVE-2002-1137

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the Database Console Command (DBCC) that handles user inputs in Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, allows attackers to execute arbitrary code via a long SourceDB argument in a "non-SQL OLEDB data source" such as FoxPro, a variant of CAN-2002-0644.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/n-003.shtml
- http://www.cisco.com/warp/public/707/cisco-sa-20030126-ms02-061.shtml
- http://www.scan-associates.net/papers/foxpro.txt
- http://www.securityfocus.com/bid/5877
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-056

---

#### 287. CVE-2002-1138

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft SQL Server 7.0 and 2000, including Microsoft Data Engine (MSDE) 1.0 and Microsoft Desktop Engine (MSDE) 2000, writes output files for scheduled jobs under its own privileges instead of the entity that launched it, which allows attackers to overwrite system files, aka "Flaw in Output File Handling for Scheduled Jobs."

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/n-003.shtml
- http://www.iss.net/security_center/static/10257.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-056
- http://www.ciac.org/ciac/bulletins/n-003.shtml
- http://www.iss.net/security_center/static/10257.php

---

#### 288. CVE-2002-1139

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Compressed Folders feature in Microsoft Windows 98 with Plus! Pack, Windows Me, and Windows XP does not properly check the destination folder during the decompression of ZIP files, which allows attackers to place an executable file in a known location on a user's system, aka "Incorrect Target Path for Zipped File Decompression."

**参考链接 / References**:
- http://www.iss.net/security_center/static/10252.php
- http://www.securityfocus.com/bid/5876
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-054
- http://www.iss.net/security_center/static/10252.php
- http://www.securityfocus.com/bid/5876

---

#### 289. CVE-2002-1140

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service (service hang) via malformed packet fragments, aka "Improper parameter size check leading to denial of service."

**参考链接 / References**:
- http://www.iss.net/security_center/static/10258.php
- http://www.securityfocus.com/bid/5879
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-057
- http://www.iss.net/security_center/static/10258.php
- http://www.securityfocus.com/bid/5879

---

#### 290. CVE-2002-1141

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
An input validation error in the Sun Microsystems RPC library Services for Unix 3.0 Interix SD, as implemented on Microsoft Windows NT4, 2000, and XP, allows remote attackers to cause a denial of service via malformed fragmented RPC client packets, aka "Denial of service by sending an invalid RPC request."

**参考链接 / References**:
- http://www.iss.net/security_center/static/10259.php
- http://www.securityfocus.com/bid/5880
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-057
- http://www.iss.net/security_center/static/10259.php
- http://www.securityfocus.com/bid/5880

---

#### 291. CVE-2002-1150

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Remote Desktop Sharing (RDS) Screen Saver Protection capability for Microsoft NetMeeting 3.01 through SP2 (4.4.3396) allows attackers with physical access to hijack remote sessions by entering certain logoff or shutdown sequences (such as CTRL-ALT-DEL) and canceling out of the resulting user confirmation prompts, such as when the remote user is editing a document.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103228375116204&w=2
- http://www.iss.net/security_center/static/10119.php
- http://www.securityfocus.com/bid/5715
- http://marc.info/?l=bugtraq&m=103228375116204&w=2
- http://www.iss.net/security_center/static/10119.php

---

#### 292. CVE-2001-1451

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in the SNMP LAN Manager (LANMAN) MIB extension for Microsoft Windows 2000 before SP3, when the Print Spooler is not running, allows remote attackers to cause a denial of service (memory consumption) via a large number of GET or GETNEXT requests.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B296815
- http://www.kb.cert.org/vuls/id/887393
- http://www.securityfocus.com/bid/6030
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10431
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B296815

---

#### 293. CVE-2002-1145

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The xp_runwebtask stored procedure in the Web Tasks component of Microsoft SQL Server 7.0 and 2000, Microsoft Data Engine (MSDE) 1.0, and Microsoft Desktop Engine (MSDE) 2000 can be executed by PUBLIC, which allows an attacker to gain privileges by updating a webtask that is owned by the database owner through the msdb.dbo.mswebtasks table, which does not have strong permissions.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103487044122900&w=2
- http://marc.info/?l=ntbugtraq&m=103486356413404&w=2
- http://www.cisco.com/warp/public/707/cisco-sa-20030126-ms02-061.shtml
- http://www.iss.net/security_center/static/10388.php
- http://www.nextgenss.com/advisories/mssql-webtasks.txt

---

#### 294. CVE-2002-1179

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the S/MIME Parsing capability in Microsoft Outlook Express 5.5 and 6.0 allows remote attackers to execute arbitrary code via a digitally signed email with a long "From" address, which triggers the overflow when the user views or previews the message.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103435413105661&w=2
- http://marc.info/?l=ntbugtraq&m=103429637822920&w=2
- http://marc.info/?l=ntbugtraq&m=103429681123297&w=2
- http://www.iss.net/security_center/static/10338.php
- http://www.securityfocus.com/bid/5944

---

#### 295. CVE-2002-1214

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Microsoft PPTP Service on Windows XP and Windows 2000 allows remote attackers to cause a denial of service (hang) and possibly execute arbitrary code via a certain PPTP packet with malformed control data.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/293146
- http://www.iss.net/security_center/static/10199.php
- http://www.securityfocus.com/bid/5807
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-063
- http://online.securityfocus.com/archive/1/293146

---

#### 296. CVE-2002-0869

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Unknown vulnerability in the hosting process (dllhost.exe) for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allows remote attackers to gain privileges by executing an out of process application that acquires LocalSystem privileges, aka "Out of Process Privilege Elevation."

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0059.html
- http://marc.info/?l=bugtraq&m=103642839205574&w=2
- http://www.ciac.org/ciac/bulletins/n-011.shtml
- http://www.iss.net/security_center/static/10502.php
- http://www.li0n.pe.kr/eng/advisory/ms/iis_impersonation.txt

---

#### 297. CVE-2002-1181

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Multiple cross-site scripting (XSS) vulnerabilities in the administrative web pages for Microsoft Internet Information Server (IIS) 4.0 through 5.1 allow remote attackers to execute HTML script as other users through (1) a certain ASP file in the IISHELP virtual directory, or (2) possibly other unknown attack vectors.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103651224215736&w=2
- http://www.ciac.org/ciac/bulletins/n-011.shtml
- http://www.iss.net/security_center/static/10501.php
- http://www.lac.co.jp/security/intelligence/SNSAdvisory/58.html
- http://www.securityfocus.com/bid/6068

---

#### 298. CVE-2002-1184

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The system root folder of Microsoft Windows 2000 has default permissions of Everyone group with Full access (Everyone:F) and is in the search path when locating programs during login or application launch from the desktop, which could allow attackers to gain privileges as other users via Trojan horse programs.

**参考链接 / References**:
- http://www.securityfocus.com/bid/5415
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-064
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9779
- http://www.securityfocus.com/bid/5415
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-064

---

#### 299. CVE-2002-1142

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Heap-based buffer overflow in the Remote Data Services (RDS) component of Microsoft Data Access Components (MDAC) 2.1 through 2.6, and Internet Explorer 5.01 through 6.0, allows remote attackers to execute code via a malformed HTTP request to the Data Stub.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q4/0082.html
- http://www.cert.org/advisories/CA-2002-33.html
- http://www.foundstone.com/knowledge/randd-advisories-display.html?id=337
- http://www.kb.cert.org/vuls/id/542081
- http://www.securityfocus.com/bid/6214

---

#### 300. CVE-2002-1287

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Stack-based buffer overflow in the Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to cause a denial of service via a long class name through (1) Class.forName or (2) ClassLoader.loadClass.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10580.php
- http://www.securityfocus.com/bid/6134
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

---

#### 301. CVE-2002-1288

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to determine the current directory of the Internet Explorer process via the getAbsolutePath() method in a File() call.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.securityfocus.com/bid/6139
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2

---

#### 302. CVE-2002-1289

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Microsoft Java implementation, as used in Internet Explorer, allows remote attackers to read restricted process memory, cause a denial of service (crash), and possibly execute arbitrary code via the getNativeServices function, which creates an instance of the com.ms.awt.peer.INativeServices (INativeServices) class, whose methods do not verify the memory addresses that are passed as parameters.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=103682630823080&w=2
- http://marc.info/?l=ntbugtraq&m=103684360031565&w=2
- http://www.iss.net/security_center/static/10582.php
- http://www.securityfocus.com/bid/6140
- http://marc.info/?l=bugtraq&m=103682630823080&w=2

---

#### 303. CVE-2002-1183

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Windows 98 and Windows NT 4.0 do not properly verify the Basic Constraints of digital certificates, allowing remote attackers to execute code, aka "New Variant of Certificate Validation Flaw Could Enable Identity Spoofing" (CAN-2002-0862).

**参考链接 / References**:
- http://www.securityfocus.com/bid/5410
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-050
- https://exchange.xforce.ibmcloud.com/vulnerabilities/9776
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1059
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1455

---

#### 304. CVE-2002-1255

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Outlook 2002 allows remote attackers to cause a denial of service (repeated failure) via an email message with a certain invalid header field that is accessed using POP3, IMAP, or WebDAV, aka "E-mail Header Processing Flaw Could Cause Outlook 2002 to Fail."

**参考链接 / References**:
- http://www.securityfocus.com/bid/6319
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-067
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10763
- http://www.securityfocus.com/bid/6319
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-067

---

#### 305. CVE-2002-1256

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The SMB signing capability in the Server Message Block (SMB) protocol in Microsoft Windows 2000 and Windows XP allows attackers to disable the digital signing settings in an SMB session to force the data to be sent unsigned, then inject data into the session without detection, e.g. by modifying group policy information sent from a domain controller.

**参考链接 / References**:
- http://www.securityfocus.com/bid/6367
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-070
- https://exchange.xforce.ibmcloud.com/vulnerabilities/10843
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A277
- http://www.securityfocus.com/bid/6367

---

#### 306. CVE-2002-1327

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the Windows Shell function in Microsoft Windows XP allows remote attackers to execute arbitrary code via an .MP3 or .WMA audio file with a corrupt custom attribute, aka "Unchecked Buffer in Windows Shell Could Enable System Compromise."

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=104025849109384&w=2
- http://www.cert.org/advisories/CA-2002-37.html
- http://www.kb.cert.org/vuls/id/591890
- http://www.securityfocus.com/bid/6427
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-072

---

#### 307. CVE-2002-1670

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Microsoft Windows XP Professional upgrade edition overwrites previously installed patches for Internet Explorer 6.0, leaving Internet Explorer unpatched.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/250596
- http://www.securityfocus.com/bid/3887
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7922
- http://online.securityfocus.com/archive/1/250596
- http://www.securityfocus.com/bid/3887

---

#### 308. CVE-1999-0275

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Windows NT DNS servers by flooding port 53 with too many characters.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0275
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0275

---

#### 309. CVE-1999-0153

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95/NT out of band (OOB) data denial of service through NETBIOS port, aka WinNuke.

**参考链接 / References**:
- http://www.osvdb.org/1666
- http://www.osvdb.org/1666

---

#### 310. CVE-1999-1463

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 before SP3 allows remote attackers to bypass firewall restrictions or cause a denial of service (crash) by sending improperly fragmented IP packets without the first fragment, which the TCP/IP stack incorrectly reassembles into a valid session.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/7219
- https://exchange.xforce.ibmcloud.com/vulnerabilities/528
- http://www.securityfocus.com/archive/1/7219
- https://exchange.xforce.ibmcloud.com/vulnerabilities/528

---

#### 311. CVE-1999-1217

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The PATH in Windows NT includes the current working directory (.), which could allow local users to gain privileges by placing Trojan horse programs with the same name as commonly used system programs into certain directories.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=87602726319426&w=2
- http://marc.info/?l=ntbugtraq&m=87602726319435&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/526
- http://marc.info/?l=ntbugtraq&m=87602726319426&w=2
- http://marc.info/?l=ntbugtraq&m=87602726319435&w=2

---

#### 312. CVE-1999-1133

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
HP-UX 9.x and 10.x running X windows may allow local attackers to gain privileges via (1) vuefile, (2) vuepad, (3) dtfile, or (4) dtpad, which do not authenticate users.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602880019776&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/499
- http://marc.info/?l=bugtraq&m=87602880019776&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/499

---

#### 313. CVE-1999-0967

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in the HTML library used by Internet Explorer, Outlook Express, and Windows Explorer via the res: local resource protocol.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0967
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0967

---

#### 314. CVE-1999-1581

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in Simple Network Management Protocol (SNMP) agent (snmp.exe) for Windows NT 4.0 before Service Pack 4 allows remote attackers to cause a denial of service (memory consumption) via a large number of SNMP packets with Object Identifiers (OIDs) that cannot be decoded.

**参考链接 / References**:
- http://support.microsoft.com/kb/q178381/
- http://www.kb.cert.org/vuls/id/4923
- https://exchange.xforce.ibmcloud.com/vulnerabilities/8231
- http://support.microsoft.com/kb/q178381/
- http://www.kb.cert.org/vuls/id/4923

---

#### 315. CVE-1999-0225

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 allows remote attackers to cause a denial of service via a malformed SMB logon request in which the actual data size does not match the specified size.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=180963
- http://www.nai.com/nai_labs/asp_set/advisory/25_windows_nt_dos_adv.asp
- http://www.microsoft.com/technet/support/kb.asp?ID=180963
- http://www.nai.com/nai_labs/asp_set/advisory/25_windows_nt_dos_adv.asp

---

#### 316. CVE-1999-1361

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
Windows NT 3.51 and 4.0 running WINS (Windows Internet Name Service) allows remote attackers to cause a denial of service (resource exhaustion) via a flood of malformed packets, which causes the server to slow down and fill the event logs with error messages.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90221101925891&w=2
- http://marc.info/?l=bugtraq&m=90221101925891&w=2

---

#### 317. CVE-1999-0158

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Cisco PIX firewall manager (PFM) on Windows NT allows attackers to connect to port 8080 on the PFM server and retrieve any file whose name and location is known.

**参考链接 / References**:
- http://www.cisco.com/warp/public/770/pixmgrfile-pub.shtml
- http://www.osvdb.org/685
- http://www.cisco.com/warp/public/770/pixmgrfile-pub.shtml
- http://www.osvdb.org/685

---

#### 318. CVE-1999-0969

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Windows NT RPC service allows remote attackers to conduct a denial of service using spoofed malformed RPC packets which generate an error message that is sent to the spoofed host, potentially setting up a loop, aka Snork.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ193233
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-014
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ193233
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-014

---

#### 319. CVE-1999-0505

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
A Windows NT domain user or administrator account has a guessable password.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0505
- https://www.cve.org/CVERecord?id=CVE-1999-0505

---

#### 320. CVE-1999-0506

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
A Windows NT domain user or administrator account has a default, null, blank, or missing password.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0506
- https://www.cve.org/CVERecord?id=CVE-1999-0506

---

#### 321. CVE-1999-0546

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Windows NT guest account is enabled.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0546
- https://www.cve.org/CVERecord?id=CVE-1999-0546

---

#### 322. CVE-1999-1289

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
ICQ 98 beta on Windows NT leaks the internal IP address of a client in the TCP data segment of an ICQ packet instead of the public address (e.g. through NAT), which provides remote attackers with potentially sensitive information about the client or the internal network configuration.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/11233
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1398
- http://www.securityfocus.com/archive/1/11233
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1398

---

#### 323. CVE-1999-0200

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT FTP server (WFTP) with the guest account enabled without a password allows an attacker to log into the FTP server using any username and password.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=137853
- http://www.microsoft.com/technet/support/kb.asp?ID=137853

---

#### 324. CVE-1999-0226

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT TCP/IP processes fragmented IP packets improperly, causing a denial of service.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0226
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0226

---

#### 325. CVE-1999-0285

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Denial of service in telnet from the Windows NT Resource Kit, by opening then immediately closing a connection.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0285
- https://www.cve.org/CVERecord?id=CVE-1999-0285

---

#### 326. CVE-1999-0549

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Windows NT automatically logs in an administrator upon rebooting.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0549
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0549

---

#### 327. CVE-1999-0560

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A system-critical Windows NT file or directory has inappropriate permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0560
- https://www.cve.org/CVERecord?id=CVE-1999-0560

---

#### 328. CVE-1999-0570

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT is not using a password filter utility, e.g. PASSFILT.DLL.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0570
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0570

---

#### 329. CVE-1999-0577

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT system's file audit policy does not log an event success or failure for non-critical files or directories.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0577
- https://www.cve.org/CVERecord?id=CVE-1999-0577

---

#### 330. CVE-1999-0579

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT system's registry audit policy does not log an event success or failure for non-critical registry keys.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228
- https://exchange.xforce.ibmcloud.com/vulnerabilities/228

---

#### 331. CVE-1999-0580

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The HKEY_LOCAL_MACHINE key in a Windows NT system has inappropriate, system-critical permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0580
- https://www.cve.org/CVERecord?id=CVE-1999-0580

---

#### 332. CVE-1999-0581

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The HKEY_CLASSES_ROOT key in a Windows NT system has inappropriate, system-critical permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0581
- https://www.cve.org/CVERecord?id=CVE-1999-0581

---

#### 333. CVE-1999-0583

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
There is a one-way or two-way trust relationship between Windows NT domains.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1284
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1284

---

#### 334. CVE-1999-0584

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT file system is not NTFS.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/195
- https://exchange.xforce.ibmcloud.com/vulnerabilities/195

---

#### 335. CVE-1999-0589

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A system-critical Windows NT registry key has inappropriate permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0589
- https://www.cve.org/CVERecord?id=CVE-1999-0589

---

#### 336. CVE-1999-0591

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An event log in Windows NT has inappropriate access permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0591
- https://www.cve.org/CVERecord?id=CVE-1999-0591

---

#### 337. CVE-1999-0592

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The Logon box of a Windows NT system displays the name of the last user who logged in.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1353
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1353

---

#### 338. CVE-1999-0593

**严重程度 / Severity**: N/A | CVSS: 4.9

**漏洞描述 / Description**:
The default setting for the Winlogon key entry ShutdownWithoutLogon in Windows NT allows users with physical access to shut down a Windows NT system without logging in.

**参考链接 / References**:
- http://osvdb.org/59333
- http://technet.microsoft.com/en-us/library/cc722469.aspx
- http://www.microsoft.com/technet/archive/winntas/deploy/confeat/06wntpcc.mspx?mfr=true
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1291
- http://osvdb.org/59333

---

#### 339. CVE-1999-0594

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT system does not restrict access to removable media drives such as a floppy disk drive or CDROM drive.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1294
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1294

---

#### 340. CVE-1999-0596

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT log file has an inappropriate maximum size or retention period.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2577
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2577

---

#### 341. CVE-1999-0597

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A Windows NT account policy does not forcibly disconnect remote users from the server when their logon hours expire.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1343
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1343

---

#### 342. CVE-1999-0603

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
In Windows NT, an inappropriate user is a member of a group, e.g. Administrator, Backup Operators, Domain Admins, Domain Guests, Power Users, Print Operators, Replicators, System Operators, etc.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0603
- https://www.cve.org/CVERecord?id=CVE-1999-0603

---

#### 343. CVE-1999-0611

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
A system-critical Windows NT registry key has an inappropriate value.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0611
- https://www.cve.org/CVERecord?id=CVE-1999-0611

---

#### 344. CVE-1999-0664

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An application-critical Windows NT registry key has inappropriate permissions.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0664
- https://www.cve.org/CVERecord?id=CVE-1999-0664

---

#### 345. CVE-1999-0665

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
An application-critical Windows NT registry key has an inappropriate value.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0665
- https://www.cve.org/CVERecord?id=CVE-1999-0665

---

#### 346. CVE-1999-0391

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The cryptographic challenge of SMB authentication in Windows 95 and Windows 98 can be reused, allowing an attacker to replay the response and impersonate a user.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=91552769809542&w=2
- https://marc.info/?l=bugtraq&m=91552769809542&w=2

---

#### 347. CVE-1999-0119

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT 4.0 beta allows users to read and delete shares.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11
- https://exchange.xforce.ibmcloud.com/vulnerabilities/11

---

#### 348. CVE-1999-0357

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 98 and other operating systems allows remote attackers to cause a denial of service via crafted "oshare" packets, possibly involving invalid fragmentation offsets.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0357
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0357

---

#### 349. CVE-1999-1201

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95 and Windows 98 systems, when configured with multiple TCP/IP stacks bound to the same MAC address, allow remote attackers to cause a denial of service (traffic amplification) via a certain ICMP echo (ping) packet, which causes all stacks to send a ping response, aka TCP Chorusing.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=91849617221319&w=2
- http://www.securityfocus.com/bid/225
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7542
- http://marc.info/?l=ntbugtraq&m=91849617221319&w=2
- http://www.securityfocus.com/bid/225

---

#### 350. CVE-1999-0366

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
In some cases, Service Pack 4 for Windows NT 4.0 can allow access to network shares using a blank password, through a problem with a null NT hash value.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ214840
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-004
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ214840
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-004

---

#### 351. CVE-1999-0404

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in the Mail-Max SMTP server for Windows systems allows remote command execution.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0404
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0404

---

#### 352. CVE-1999-0376

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Local users in Windows NT can obtain administrator privileges by changing the KnownDLLs list to reference malicious programs.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-006
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-006

---

#### 353. CVE-1999-1254

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95, 98, and NT 4.0 allow remote attackers to cause a denial of service by spoofing ICMP redirect messages from a router, which causes Windows to change its routing tables.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92099515709467&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1947
- http://marc.info/?l=ntbugtraq&m=92099515709467&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1947

---

#### 354. CVE-1999-0444

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Remote attackers can perform a denial of service in Windows machines using malicious ARP packets, forcing a message box display for each packet or filling up log files.

**参考链接 / References**:
- https://marc.info/?l=bugtraq&m=92394891221029&w=2
- https://marc.info/?l=bugtraq&m=92394891221029&w=2

---

#### 355. CVE-1999-0229

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Windows NT IIS server using ..\..

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0229
- https://exchange.xforce.ibmcloud.com/vulnerabilities/CVE-1999-0229

---

#### 356. CVE-1999-0716

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in Windows NT 4.0 help file utility via a malformed help file.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231605
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-015
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ231605
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-015

---

#### 357. CVE-1999-0755

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT RRAS and RAS clients cache a user's password even if the user has not selected the "Save password" option.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ230681
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-017
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ230681
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-017

---

#### 358. CVE-1999-0723

**严重程度 / Severity**: N/A | CVSS: 7.1

**漏洞描述 / Description**:
The Windows NT Client Server Runtime Subsystem (CSRSS) can be subjected to a denial of service when all worker threads are waiting for user input.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ233323
- http://www.ciac.org/ciac/bulletins/j-049.shtml
- http://www.securityfocus.com/bid/478
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-021
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ233323

---

#### 359. CVE-1999-1365

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Windows NT searches a user's home directory (%systemroot% by default) before other directories to find critical programs such as NDDEAGNT.EXE, EXPLORER.EXE, USERINIT.EXE or TASKMGR.EXE, which could allow local users to bypass access restrictions or gain privileges by placing a Trojan horse program into the root directory, which is writable by default.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=93069418400856&w=2
- http://marc.info/?l=ntbugtraq&m=93127894731200&w=2
- http://www.securityfocus.com/bid/515
- https://exchange.xforce.ibmcloud.com/vulnerabilities/2336
- http://marc.info/?l=ntbugtraq&m=93069418400856&w=2

---

#### 360. CVE-1999-0726

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
An attacker can conduct a denial of service in Windows NT by executing a program with a malformed file image header.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ234557
- http://www.securityfocus.com/bid/499
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-023
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ234557
- http://www.securityfocus.com/bid/499

---

#### 361. CVE-1999-0918

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Denial of service in various Windows systems via malformed, fragmented IGMP packets.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238329
- http://www.securityfocus.com/bid/514
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-034
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238329
- http://www.securityfocus.com/bid/514

---

#### 362. CVE-1999-0728

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
A Windows NT user can disable the keyboard or mouse by directly calling the IOCTLs which control them.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ236359
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-024
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ236359
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-024

---

#### 363. CVE-1999-0224

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Denial of service in Windows NT messenger service through a long username.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0224
- https://www.cve.org/CVERecord?id=CVE-1999-0224

---

#### 364. CVE-1999-0680

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT Terminal Server performs extra work when a client opens a new connection but before it is authenticated, allowing for a denial of service.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238600
- http://www.ciac.org/ciac/bulletins/j-057.shtml
- http://www.securityfocus.com/bid/571
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-028
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238600

---

#### 365. CVE-2000-0328

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 generates predictable random TCP initial sequence numbers (ISN), which allows remote attackers to perform spoofing and session hijacking.

**参考链接 / References**:
- http://www.securityfocus.com/bid/604
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=4.1.19990824165629.00abcb40%40192.168.124.1
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-046
- http://www.securityfocus.com/bid/604
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=4.1.19990824165629.00abcb40%40192.168.124.1

---

#### 366. CVE-1999-0909

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Multihomed Windows systems allow a remote attacker to bypass IP source routing restrictions via a malformed packet with IP options, aka the "Spoofed Route Pointer" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238453
- http://www.securityfocus.com/bid/646
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-038
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ238453
- http://www.securityfocus.com/bid/646

---

#### 367. CVE-1999-1454

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Macromedia "The Matrix" screen saver on Windows 95 with the "Password protected" option enabled allows attackers with physical access to the machine to bypass the password prompt by pressing the ESC (Escape) key.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93915027622690&w=2
- http://marc.info/?l=bugtraq&m=93915027622690&w=2

---

#### 368. CVE-1999-1234

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
LSA (LSASS.EXE) in Windows NT 4.0 allows remote attackers to cause a denial of service via a NULL policy handle in a call to (1) SamrOpenDomain, (2) SamrEnumDomainUsers, and (3) SamrQueryDomainInfo.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=94096671308565&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3293
- http://marc.info/?l=ntbugtraq&m=94096671308565&w=2
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3293

---

#### 369. CVE-1999-1531

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in IBM HomePagePrint 1.0.7 for Windows98J allows a malicious Web site to execute arbitrary code on a viewer's system via a long IMG_SRC HTML tag.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94157187815629&w=2
- http://www.iss.net/security_center/static/7767.php
- http://www.securityfocus.com/bid/763
- http://marc.info/?l=bugtraq&m=94157187815629&w=2
- http://www.iss.net/security_center/static/7767.php

---

#### 370. CVE-1999-0898

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Buffer overflows in Windows NT 4.0 print spooler allow remote attackers to gain privileges or cause a denial of service via a malformed spooler request.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/768
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-047
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/768

---

#### 371. CVE-1999-0899

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The Windows NT 4.0 print spooler allows a local user to execute arbitrary commands due to inappropriate permissions that allow the user to specify an alternate print provider.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/769
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-047
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ243649
- http://www.securityfocus.com/bid/769

---

#### 372. CVE-1999-1065

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Palm Pilot HotSync Manager 3.0.4 in Windows 98 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long string to port 14238 while the manager is in network mode.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94175465525422&w=2
- http://marc.info/?l=bugtraq&m=94175465525422&w=2

---

#### 373. CVE-2000-0330

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
The networking software in Windows 95 and Windows 98 allows remote attackers to execute commands via a long file name string, aka the "File Access URL" vulnerability.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-049
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-049

---

#### 374. CVE-1999-1110

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows Media Player ActiveX object as used in Internet Explorer 5.0 returns a specific error code when a file does not exist, which allows remote malicious web sites to determine the existence of files on the client.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/34675
- http://www.securityfocus.com/bid/793
- http://www.securityfocus.com/archive/1/34675
- http://www.securityfocus.com/bid/793

---

#### 375. CVE-1999-0987

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Windows NT does not properly download a system policy if the domain user logs into the domain with a space at the end of the domain name.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237923
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ237923

---

#### 376. CVE-2017-9948

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
A stack buffer overflow vulnerability has been discovered in Microsoft Skype 7.2, 7.35, and 7.36 before 7.37, involving MSFTEDIT.DLL mishandling of remote RDP clipboard content within the message box.

**参考链接 / References**:
- http://www.securityfocus.com/bid/99281
- https://www.vulnerability-db.com/?q=articles/2017/05/28/stack-buffer-overflow-zero-day-vulnerability-uncovered-microsoft-skype-v72-v735
- https://www.vulnerability-lab.com/get_content.php?id=2071
- https://www.vulnerability-lab.com/get_content.php?id=2084
- http://www.securityfocus.com/bid/99281

---

#### 377. CVE-2024-26888

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: msft: Fix memory leak

Fix leaking buffer allocated to send MSFT_OP_LE_MONITOR_ADVERTISEMENT.

**参考链接 / References**:
- https://git.kernel.org/stable/c/5987b9f7d9314c7411136005b3a52f61a8cc0911
- https://git.kernel.org/stable/c/5cb93417c93716a5404f762f331f5de3653fd952
- https://git.kernel.org/stable/c/98e9920c75e0790bff947a00d192d24bf1c724e0
- https://git.kernel.org/stable/c/a6e06258f4c31eba0fcd503e19828b5f8fe7b08b
- https://git.kernel.org/stable/c/5987b9f7d9314c7411136005b3a52f61a8cc0911

---

#### 378. CVE-2024-36012

**严重程度 / Severity**: HIGH | CVSS: 7.8

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

**参考链接 / References**:
- https://git.kernel.org/stable/c/10f9f426ac6e752c8d87bf4346930ba347aaabac
- https://git.kernel.org/stable/c/4f1de02de07748da80a8178879bc7a1df37fdf56
- https://git.kernel.org/stable/c/a85a60e62355e3bf4802dead7938966824b23940
- https://git.kernel.org/stable/c/e3880b531b68f98d3941d83f2f6dd11cf4fd6b76
- https://git.kernel.org/stable/c/10f9f426ac6e752c8d87bf4346930ba347aaabac

---

#### 379. CVE-2025-40181

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

**参考链接 / References**:
- https://git.kernel.org/stable/c/0dccbc75e18df85399a71933d60b97494110f559
- https://git.kernel.org/stable/c/34ff466f74d0fe1db8956f9c245e2bb2c67f67bf
- https://git.kernel.org/stable/c/91ab8a21bda2d2d2842b6159ac060d9100433a3c

---

#### 380. CVE-2023-53828

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

**参考链接 / References**:
- https://git.kernel.org/stable/c/81d8e9f59df63b8358751c1ffed9f1cf5c796909
- https://git.kernel.org/stable/c/8d66f7ced51cb924bc90278d6a0a26a52877271a
- https://git.kernel.org/stable/c/a2bcd2b63271a93a695fabbfbf459c603d956d48
- https://git.kernel.org/stable/c/aafda69d4807f5edf3558c9534be9b911774e63a

---

#### 381. CVE-2023-54210

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

**参考链接 / References**:
- https://git.kernel.org/stable/c/0d4d6b083da9b033ddccef72d77f373c819ae3ea
- https://git.kernel.org/stable/c/bf00c2c8f6254f44ac041aa9a311ae9e0caf692b
- https://git.kernel.org/stable/c/de6dfcefd107667ce2dbedf4d9337f5ed557a4a1

---

#### 382. CVE-2008-4787

**严重程度 / Severity**: N/A | CVSS: 5.8

**漏洞描述 / Description**:
Visual truncation vulnerability in Microsoft Internet Explorer 6 allows remote attackers to spoof the address bar via a URL with a hostname containing many   (Non-Blocking Space character) sequences, which are rendered as whitespace, aka MSRC ticket MSRC7899, a related issue to CVE-2003-1025.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/497825/100/0/threaded
- http://www.securityfocus.com/archive/1/497827/100/0/threaded
- http://www.securityfocus.com/bid/31960
- https://exchange.xforce.ibmcloud.com/vulnerabilities/46234
- http://www.securityfocus.com/archive/1/497825/100/0/threaded

---

#### 383. CVE-2008-4788

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 6 omits high-bit URL-encoded characters when displaying the address bar, which allows remote attackers to spoof the address bar via a URL with a domain name that differs from an important domain name only in these characters, as demonstrated by using exam%A9ple.com to spoof example.com, aka MSRC ticket MSRC7900.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/497825/100/0/threaded
- http://www.securityfocus.com/archive/1/497827/100/0/threaded
- https://exchange.xforce.ibmcloud.com/vulnerabilities/46235
- http://www.securityfocus.com/archive/1/497825/100/0/threaded
- http://www.securityfocus.com/archive/1/497827/100/0/threaded

---

#### 384. CVE-2008-5100

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The strong name (SN) implementation in Microsoft .NET Framework 2.0.50727 relies on the digital signature Public Key Token embedded in the pathname of a DLL file instead of the digital signature of this file itself, which makes it easier for attackers to bypass Global Assembly Cache (GAC) and Code Access Security (CAS) protection mechanisms, aka MSRC ticket MSRC8566gs.

**参考链接 / References**:
- http://securityreason.com/securityalert/4605
- http://www.applicationsecurity.co.il/.NET-Framework-Rootkits.aspx
- http://www.applicationsecurity.co.il/LinkClick.aspx?fileticket=ycIS1bewMBI%3d&tabid=161&mid=555
- http://www.securityfocus.com/archive/1/498311/100/0/threaded
- http://securityreason.com/securityalert/4605

---

#### 385. CVE-2009-1335

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
Microsoft Internet Explorer 7 and 8 on Windows XP and Vista allows remote attackers to cause a denial of service (application hang) via a large document composed of unprintable characters, aka MSRC 9011jr.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/fulldisclosure/2009-04/0111.html
- http://www.securityfocus.com/archive/1/502617/100/0/threaded
- http://www.securityfocus.com/bid/34478
- https://exchange.xforce.ibmcloud.com/vulnerabilities/50350
- http://archives.neohapsis.com/archives/fulldisclosure/2009-04/0111.html

---

#### 386. CVE-2013-1450

**严重程度 / Severity**: N/A | CVSS: 4.0

**漏洞描述 / Description**:
Microsoft Internet Explorer 8 and 9, when the Proxy Settings configuration has the same Proxy address and Port values in the HTTP and Secure rows, does not properly reuse TCP sessions to the proxy server, which allows remote attackers to obtain sensitive information intended for a specific host via a crafted HTML document that triggers many HTTPS requests and then triggers an HTTP request to that host, as demonstrated by reading a Cookie header, aka MSRC 12096gd.

**参考链接 / References**:
- http://pastebin.com/raw.php?i=rz9BcBey
- http://www.youtube.com/ChristianHaiderPoC
- http://www.youtube.com/watch?v=TPqagWAvo8U
- http://pastebin.com/raw.php?i=rz9BcBey
- http://www.youtube.com/ChristianHaiderPoC

---

#### 387. CVE-2015-0002

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The AhcVerifyAdminContext function in ahcache.sys in the Application Compatibility component in Microsoft Windows 7 SP1, Windows Server 2008 R2 SP1, Windows 8, Windows 8.1, Windows Server 2012 Gold and R2, and Windows RT Gold and 8.1 does not verify that an impersonation token is associated with an administrative account, which allows local users to gain privileges by running AppCompatCache.exe with a crafted DLL file, aka MSRC ID 20544 or "Microsoft Application Compatibility Infrastructure Elevation of Privilege Vulnerability."

**参考链接 / References**:
- http://secunia.com/advisories/61277
- http://twitter.com/sambowne/statuses/550384131683520512
- http://www.securityfocus.com/bid/71972
- http://www.zdnet.com/article/google-discloses-unpatched-windows-vulnerability/
- https://code.google.com/p/google-security-research/issues/detail?id=118

---

#### 388. CVE-2015-0004

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The User Profile Service (aka ProfSvc) in Microsoft Windows Server 2003 SP2, Windows Vista SP2, Windows Server 2008 SP2 and R2 SP1, Windows 7 SP1, Windows 8, Windows 8.1, Windows Server 2012 Gold and R2, and Windows RT Gold and 8.1 allows local users to gain privileges by conducting a junction attack to load another user's UsrClass.dat registry hive, aka MSRC ID 20674 or "Microsoft User Profile Service Elevation of Privilege Vulnerability."

**参考链接 / References**:
- http://secunia.com/advisories/61927
- http://www.securityfocus.com/bid/71967
- https://code.google.com/p/google-security-research/issues/detail?id=123
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2015/ms15-003
- https://exchange.xforce.ibmcloud.com/vulnerabilities/99519

---

#### 389. CVE-2015-0010

**严重程度 / Severity**: N/A | CVSS: 1.9

**漏洞描述 / Description**:
The CryptProtectMemory function in cng.sys (aka the Cryptography Next Generation driver) in the kernel-mode drivers in Microsoft Windows Server 2003 SP2, Windows Vista SP2, Windows Server 2008 SP2 and R2 SP1, Windows 7 SP1, Windows 8, Windows 8.1, Windows Server 2012 Gold and R2, and Windows RT Gold and 8.1, when the CRYPTPROTECTMEMORY_SAME_LOGON option is used, does not check an impersonation token's level, which allows local users to bypass intended decryption restrictions by leveraging a service that (1) has a named-pipe planting vulnerability or (2) uses world-readable shared memory for encrypted data, aka "CNG Security Feature Bypass Vulnerability" or MSRC ID 20707.

**参考链接 / References**:
- http://code.google.com/p/google-security-research/issues/detail?id=128
- http://www.securityfocus.com/bid/72461
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2015/ms15-010
- http://code.google.com/p/google-security-research/issues/detail?id=128
- http://www.securityfocus.com/bid/72461

---

#### 390. CVE-2021-42306

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
An information disclosure vulnerability manifests when a user or an application uploads unprotected private key data as part of an authentication certificate keyCredential  on an Azure AD Application or Service Principal (which is not recommended). This vulnerability allows a user or service in the tenant with application read access to read the private key data that was added to the application.
Azure AD addressed this vulnerability by preventing disclosure of any private key values added to the application.
Microsoft has identified services that could manifest this vulnerability, and steps that customers should take to be protected. Refer to the FAQ section for more information.
For more details on this issue, please refer to the MSRC Blog Entry.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42306
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42306

---

#### 391. [webapps] FUXA 1.2.8 - Authentication Bypass + RCE Exploit

**严重程度 / Severity**: EXPLOIT

**漏洞描述 / Description**:
[Exploit-DB] FUXA 1.2.8 - Authentication Bypass + RCE Exploit

**参考链接 / References**:
- https://www.exploit-db.com/exploits/52544

---

#### 392. CVE-2006-3230

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Cross-site scripting (XSS) vulnerability in index.tmpl in Azureus Tracker 2.4.0.2 and earlier (Java BitTorrent Client Tracker) allows remote attackers to inject arbitrary web script or HTML via the search parameter.

**参考链接 / References**:
- http://pridels0.blogspot.com/2006/06/azureus-2402-xss-vuln.html
- http://secunia.com/advisories/20755
- http://securitytracker.com/id?1016357
- http://www.osvdb.org/26768
- http://www.securityfocus.com/bid/18596

---

#### 393. CVE-2008-6587

**严重程度 / Severity**: N/A | CVSS: 6.8

**漏洞描述 / Description**:
Cross-site request forgery (CSRF) vulnerability in index.tmpl in Vuze (formerly Azureus HTML WebUI), probably 0.7.6, allows remote attackers to hijack the authentication of users for requests that force the download of arbitrary torrent files via the upurl parameter.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/491066/100/0/threaded
- http://www.securityfocus.com/bid/28848
- https://exchange.xforce.ibmcloud.com/vulnerabilities/41926
- http://www.securityfocus.com/archive/1/491066/100/0/threaded
- http://www.securityfocus.com/bid/28848

---

#### 394. CVE-2011-1068

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Microsoft Windows Azure Software Development Kit (SDK) 1.3.x before 1.3.20121.1237, when Full IIS and a Web Role are used with an ASP.NET application, does not properly support the use of cookies for maintaining state, which allows remote attackers to obtain potentially sensitive information by reading an encrypted cookie and performing unspecified other steps.

**参考链接 / References**:
- http://blogs.msdn.com/b/windowsazure/archive/2011/02/03/windows-azure-software-development-kit-sdk-refresh-released.aspx
- http://secunia.com/advisories/43237
- http://blogs.msdn.com/b/windowsazure/archive/2011/02/03/windows-azure-software-development-kit-sdk-refresh-released.aspx
- http://secunia.com/advisories/43237

---

#### 395. CVE-2011-3649

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
Mozilla Firefox 7.0 and Thunderbird 7.0, when the Direct2D (aka D2D) API is used on Windows in conjunction with the Azure graphics back-end, allow remote attackers to bypass the Same Origin Policy, and obtain sensitive image data from a different domain, by inserting this data into a canvas.  NOTE: this issue exists because of a CVE-2011-2986 regression.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2011-11/msg00020.html
- http://www.mozilla.org/security/announce/2011/mfsa2011-50.html
- http://www.securityfocus.com/bid/50591
- https://bugzilla.mozilla.org/show_bug.cgi?id=655836
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A14025

---

#### 396. CVE-2015-7876

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The escapeLike function in sqlsrv/database.inc in the Drupal 7 driver for SQL Server and SQL Azure 7.x-1.x before 7.x-1.4 does not properly escape certain characters, which allows remote attackers to execute arbitrary SQL commands via vectors involving a module using the db_like function.

**参考链接 / References**:
- http://cgit.drupalcode.org/sqlsrv/commit/?id=2ea0da8
- https://www.drupal.org/node/2569003
- https://www.drupal.org/node/2569005
- https://www.drupal.org/node/2569577
- http://cgit.drupalcode.org/sqlsrv/commit/?id=2ea0da8

---

#### 397. CVE-2016-2084

**严重程度 / Severity**: HIGH | CVSS: 7.4

**漏洞描述 / Description**:
F5 BIG-IP LTM, AFM, Analytics, APM, ASM, Link Controller, and PEM 11.3.x, 11.4.x before 11.4.1 build 685-HF10, 11.5.1 before build 10.104.180, 11.5.2 before 11.5.4 build 0.1.256, 11.6.0 before build 6.204.442, and 12.0.0 before build 1.14.628; BIG-IP AAM 11.4.x before 11.4.1 build 685-HF10, 11.5.1 before build 10.104.180, 11.5.2 before 11.5.4 build 0.1.256, 11.6.0 before build 6.204.442, and 12.0.0 before build 1.14.628; BIG-IP DNS 12.0.0 before build 1.14.628; BIG-IP Edge Gateway, WebAccelerator, and WOM 11.3.0; BIG-IP GTM 11.3.x, 11.4.x before 11.4.1 build 685-HF10, 11.5.1 before build 10.104.180, 11.5.2 before 11.5.4 build 0.1.256, and 11.6.0 before build 6.204.442; BIG-IP PSM 11.3.x and 11.4.x before 11.4.1 build 685-HF10; BIG-IQ Cloud, Device, and Security 4.2.0 through 4.5.0; and BIG-IQ ADC 4.5.0 do not properly regenerate certificates and keys when deploying cloud images in Amazon Web Services (AWS), Azure or Verizon cloud services environments, which allows attackers to obtain sensitive information or cause a denial of service (disruption) by leveraging a target instance configuration.

**参考链接 / References**:
- http://www.securitytracker.com/id/1035520
- https://support.f5.com/kb/en-us/solutions/public/k/11/sol11772107.html
- http://www.securitytracker.com/id/1035520
- https://support.f5.com/kb/en-us/solutions/public/k/11/sol11772107.html

---

#### 398. CVE-2016-7191

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
The Microsoft Azure Active Directory Passport (aka Passport-Azure-AD) library 1.x before 1.4.6 and 2.x before 2.0.1 for Node.js does not recognize the validateIssuer setting, which allows remote attackers to bypass authentication via a crafted token.

**参考链接 / References**:
- http://www.securityfocus.com/bid/93213
- http://www.securitytracker.com/id/1036996
- https://github.com/AzureAD/passport-azure-ad/blob/master/SECURITY-NOTICE.MD
- https://support.microsoft.com/kb/3187742
- http://www.securityfocus.com/bid/93213

---

#### 399. CVE-2017-6506

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In Azure Data Expert Ultimate 2.2.16, the SMTP verification function suffers from a buffer overflow vulnerability, leading to remote code execution. The attack vector is a crafted SMTP daemon that sends a long 220 (aka "Service ready") string.

**参考链接 / References**:
- http://packetstormsecurity.com/files/141502/Azure-Data-Expert-Ultimate-2.2.16-Buffer-Overflow.html
- http://www.securityfocus.com/bid/96824
- https://www.exploit-db.com/exploits/41545/
- http://packetstormsecurity.com/files/141502/Azure-Data-Expert-Ultimate-2.2.16-Buffer-Overflow.html
- http://www.securityfocus.com/bid/96824

---

#### 400. CVE-2017-4964

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Cloud Foundry Foundation BOSH Azure CPI v22 could potentially allow a maliciously crafted stemcell to execute arbitrary code on VMs created by the director, aka a "CPI code injection vulnerability."

**参考链接 / References**:
- https://www.cloudfoundry.org/cve-2017-4964/
- https://www.cloudfoundry.org/cve-2017-4964/

---

#### 401. CVE-2017-6131

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In some circumstances, an F5 BIG-IP version 12.0.0 to 12.1.2 and 13.0.0 Azure cloud instance may contain a default administrative password which could be used to remotely log into the BIG-IP system. The impacted administrative account is the Azure instance administrative user that was created at deployment. The root and admin accounts are not vulnerable. An attacker may be able to remotely access the BIG-IP host via SSH.

**参考链接 / References**:
- http://www.securitytracker.com/id/1038569
- https://support.f5.com/csp/article/K61757346
- http://www.securitytracker.com/id/1038569
- https://support.f5.com/csp/article/K61757346

---

#### 402. CVE-2017-8613

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure AD Connect Password writeback, if misconfigured during enablement, allows an attacker to reset passwords and gain unauthorized access to arbitrary on-premises AD privileged user accounts aka "Azure AD Connect Elevation of Privilege Vulnerability."

**参考链接 / References**:
- http://www.securityfocus.com/bid/99294
- https://technet.microsoft.com/library/security/4033453
- http://www.securityfocus.com/bid/99294
- https://technet.microsoft.com/library/security/4033453

---

#### 403. CVE-2017-9653

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
An Improper Authorization issue was discovered in OSIsoft PI Integrator for Business Analytics before 2016 R2, PI Integrator for Microsoft Azure before 2016 R2 SP1, and PI Integrator for SAP HANA before 2017. An attacker is able to gain privileged access to the system while unauthorized.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100212
- https://ics-cert.us-cert.gov/advisories/ICSA-17-220-01
- https://techsupport.osisoft.com/Troubleshooting/Alerts/AL00324
- http://www.securityfocus.com/bid/100212
- https://ics-cert.us-cert.gov/advisories/ICSA-17-220-01

---

#### 404. CVE-2017-9655

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-Site Scripting issue was discovered in OSIsoft PI Integrator for Business Analytics before 2016 R2, PI Integrator for Microsoft Azure before 2016 R2 SP1, and PI Integrator for SAP HANA before 2017. An attacker may be able to upload a malicious script that attempts to redirect users to a malicious web site.

**参考链接 / References**:
- http://www.securityfocus.com/bid/100212
- https://ics-cert.us-cert.gov/advisories/ICSA-17-220-01
- https://techsupport.osisoft.com/Troubleshooting/Alerts/AL00324
- http://www.securityfocus.com/bid/100212
- https://ics-cert.us-cert.gov/advisories/ICSA-17-220-01

---

#### 405. CVE-2017-1002100

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Default access permissions for Persistent Volumes (PVs) created by the Kubernetes Azure cloud provider in versions 1.6.0 to 1.6.5 are set to "container" which exposes a URI that can be accessed without authentication on the public internet. Access to the URI string requires privileged access to the Kubernetes cluster or authenticated access to the Azure portal.

**参考链接 / References**:
- https://github.com/kubernetes/kubernetes/issues/47611
- https://groups.google.com/d/msg/kubernetes-security-announce/n3VBg_WJZic/-ddIqKXqAAAJ
- https://github.com/kubernetes/kubernetes/issues/47611
- https://groups.google.com/d/msg/kubernetes-security-announce/n3VBg_WJZic/-ddIqKXqAAAJ

---

#### 406. CVE-2018-4862

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In Octopus Deploy versions 3.2.11 - 4.1.5 (fixed in 4.1.6), an authenticated user with ProcessEdit permission could reference an Azure account in such a way as to bypass the scoping restrictions, resulting in a potential escalation of privileges.

**参考链接 / References**:
- https://github.com/OctopusDeploy/Issues/issues/4134
- https://github.com/OctopusDeploy/Issues/issues/4134

---

#### 407. CVE-2018-8119

**严重程度 / Severity**: MEDIUM | CVSS: 5.6

**漏洞描述 / Description**:
A spoofing vulnerability exists when the Azure IoT Device Provisioning AMQP Transport library improperly validates certificates over the AMQP protocol, aka "Azure IoT SDK Spoofing Vulnerability." This affects C# SDK, C SDK, Java SDK.

**参考链接 / References**:
- http://www.securityfocus.com/bid/104070
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8119
- https://tools.cisco.com/security/center/viewAlert.x?alertId=57754&vs_f=Alert%20RSS&vs_cat=Security%20Intelligence&vs_type=RSS&vs_p=Microsoft%20Azure%20IoT%20SDK%20AMQP%20Transport%20Library%20Spoofing%20Vulnerability&vs_k=1
- http://www.securityfocus.com/bid/104070
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8119

---

#### 408. CVE-2018-12089

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
In Octopus Deploy version 2018.5.1 to 2018.5.7, a user with Task View is able to view a password for a Service Fabric Cluster, when the Service Fabric Cluster target is configured in Azure Active Directory security mode and a deployment is executed with OctopusPrintVariables set to True. This is fixed in 2018.6.0.

**参考链接 / References**:
- https://github.com/OctopusDeploy/Issues/issues/4628
- https://github.com/OctopusDeploy/Issues/issues/4628

---

#### 409. CVE-2018-8479

**严重程度 / Severity**: MEDIUM | CVSS: 5.6

**漏洞描述 / Description**:
A spoofing vulnerability exists for the Azure IoT Device Provisioning for the C SDK library using the HTTP protocol on Windows platform, aka "Azure IoT SDK Spoofing Vulnerability." This affects C SDK.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105323
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8479
- http://www.securityfocus.com/bid/105323
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8479

---

#### 410. CVE-2018-3827

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
A sensitive data disclosure flaw was found in the Elasticsearch repository-azure (formerly elasticsearch-cloud-azure) plugin. When the repository-azure plugin is set to log at TRACE level Azure credentials can be inadvertently logged.

**参考链接 / References**:
- https://discuss.elastic.co/t/elastic-stack-6-3-0-and-5-6-10-security-update/135777
- https://www.elastic.co/community/security
- https://discuss.elastic.co/t/elastic-stack-6-3-0-and-5-6-10-security-update/135777
- https://www.elastic.co/community/security

---

#### 411. CVE-2018-8531

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
A remote code execution vulnerability exists in the way that Azure IoT Hub Device Client SDK using MQTT protocol accesses objects in memory, aka "Azure IoT Device Client SDK Memory Corruption Vulnerability." This affects Hub Device Client SDK, Azure IoT Edge.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105472
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8531
- http://www.securityfocus.com/bid/105472
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8531

---

#### 412. CVE-2018-8600

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure App Services on Azure Stack does not properly sanitize user provided input, aka "Azure App Service Cross-site Scripting Vulnerability." This affects Azure App.

**参考链接 / References**:
- http://www.securityfocus.com/bid/105893
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8600
- http://www.securityfocus.com/bid/105893
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8600

---

#### 413. CVE-2018-8652

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Windows Azure Pack does not properly sanitize user-provided input, aka "Windows Azure Pack Cross Site Scripting Vulnerability." This affects Windows Azure Pack Rollup 13.1.

**参考链接 / References**:
- http://www.securityfocus.com/bid/106155
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8652
- http://www.securityfocus.com/bid/106155
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8652

---

#### 414. CVE-2019-0729

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
An Elevation of Privilege vulnerability exists in the way Azure IoT Java SDK generates symmetric keys for encryption, allowing an attacker to predict the randomness of the key, aka 'Azure IoT Java SDK Elevation of Privilege Vulnerability'.

**参考链接 / References**:
- http://www.securityfocus.com/bid/106966
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0729
- http://www.securityfocus.com/bid/106966
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0729

---

#### 415. CVE-2019-0741

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An information disclosure vulnerability exists in the way Azure IoT Java SDK logs sensitive information, aka 'Azure IoT Java SDK Information Disclosure Vulnerability'.

**参考链接 / References**:
- http://www.securityfocus.com/bid/106971
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0741
- http://www.securityfocus.com/bid/106971
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0741

---

#### 416. CVE-2019-1003035

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
An information exposure vulnerability exists in Jenkins Azure VM Agents Plugin 0.8.0 and earlier in src/main/java/com/microsoft/azure/vmagent/AzureVMAgentTemplate.java, src/main/java/com/microsoft/azure/vmagent/AzureVMCloud.java that allows attackers with Overall/Read permission to perform the 'verify configuration' form validation action, thereby obtaining limited information about the Azure configuration.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1330
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1330

---

#### 417. CVE-2019-1003036

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
A data modification vulnerability exists in Jenkins Azure VM Agents Plugin 0.8.0 and earlier in src/main/java/com/microsoft/azure/vmagent/AzureVMAgent.java that allows attackers with Overall/Read permission to attach a public IP address to an Azure VM agent.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1331
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1331

---

#### 418. CVE-2019-1003037

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An information exposure vulnerability exists in Jenkins Azure VM Agents Plugin 0.8.0 and earlier in src/main/java/com/microsoft/azure/vmagent/AzureVMCloud.java that allows attackers with Overall/Read permission to enumerate credentials IDs of credentials stored in Jenkins.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1332
- http://www.securityfocus.com/bid/107476
- https://jenkins.io/security/advisory/2019-03-06/#SECURITY-1332

---

#### 419. CVE-2019-5917

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
azure-umqtt-c (available through GitHub prior to 2017 October 6) allows remote attackers to cause a denial of service via unspecified vectors.

**参考链接 / References**:
- http://jvn.jp/en/jp/JVN05875753/index.html
- http://www.securityfocus.com/bid/107149
- https://github.com/Azure/azure-umqtt-c
- http://jvn.jp/en/jp/JVN05875753/index.html
- http://www.securityfocus.com/bid/107149

---

#### 420. CVE-2019-0804

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An information disclosure vulnerability exists in the way Azure WaLinuxAgent creates swap files on resource disks, aka 'Azure Linux Agent Information Disclosure Vulnerability'.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2020-02/msg00037.html
- https://access.redhat.com/errata/RHSA-2019:1527
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0804
- http://lists.opensuse.org/opensuse-security-announce/2020-02/msg00037.html
- https://access.redhat.com/errata/RHSA-2019:1527

---

#### 421. CVE-2019-0816

**严重程度 / Severity**: MEDIUM | CVSS: 5.1

**漏洞描述 / Description**:
A security feature bypass exists in Azure SSH Keypairs, due to a change in the provisioning logic for some Linux images that use cloud-init, aka 'Azure SSH Keypairs Security Feature Bypass Vulnerability'.

**参考链接 / References**:
- http://lists.opensuse.org/opensuse-security-announce/2019-12/msg00018.html
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0816
- http://lists.opensuse.org/opensuse-security-announce/2019-12/msg00018.html
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0816

---

#### 422. CVE-2019-0857

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
A spoofing vulnerability that could allow a security feature bypass exists in when Azure DevOps Server does not properly sanitize user provided input, aka 'Azure DevOps Server Spoofing Vulnerability'.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107760
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0857
- http://www.securityfocus.com/bid/107760
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0857

---

#### 423. CVE-2019-0866

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0867, CVE-2019-0868, CVE-2019-0870, CVE-2019-0871.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107749
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0866
- http://www.securityfocus.com/bid/107749
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0866

---

#### 424. CVE-2019-0867

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0866, CVE-2019-0868, CVE-2019-0870, CVE-2019-0871.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107752
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0867
- http://www.securityfocus.com/bid/107752
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0867

---

#### 425. CVE-2019-0868

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0866, CVE-2019-0867, CVE-2019-0870, CVE-2019-0871.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107753
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0868
- http://www.securityfocus.com/bid/107753
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0868

---

#### 426. CVE-2019-0869

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A spoofing vulnerability exists in Microsoft Azure DevOps Server when it fails to properly handle web requests, aka 'Azure DevOps Server HTML Injection Vulnerability'.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107768
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0869
- http://www.securityfocus.com/bid/107768
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0869

---

#### 427. CVE-2019-0870

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0866, CVE-2019-0867, CVE-2019-0868, CVE-2019-0871.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107754
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0870
- http://www.securityfocus.com/bid/107754
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0870

---

#### 428. CVE-2019-0871

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0866, CVE-2019-0867, CVE-2019-0868, CVE-2019-0870.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107755
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0871
- http://www.securityfocus.com/bid/107755
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0871

---

#### 429. CVE-2019-0874

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server does not properly sanitize user provided input, aka 'Azure DevOps Server Cross-site Scripting Vulnerability'.

**参考链接 / References**:
- http://www.securityfocus.com/bid/107759
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0874
- http://www.securityfocus.com/bid/107759
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0874

---

#### 430. CVE-2019-0875

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists when Azure DevOps Server 2019 does not properly enforce project permissions, aka 'Azure DevOps Server Elevation of Privilege Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0875
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0875

---

#### 431. CVE-2019-10303

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Jenkins Azure PublisherSettings Credentials Plugin 1.2 and earlier stored credentials unencrypted in the credentials.xml file on the Jenkins master where they could be viewed by users with access to the master file system.

**参考链接 / References**:
- http://www.securityfocus.com/bid/108045
- https://jenkins.io/security/advisory/2019-04-17/#SECURITY-844
- http://www.securityfocus.com/bid/108045
- https://jenkins.io/security/advisory/2019-04-17/#SECURITY-844

---

#### 432. CVE-2019-10318

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Jenkins Azure AD Plugin 0.3.3 and earlier stored the client secret unencrypted in the global config.xml configuration file on the Jenkins master where it could be viewed by users with access to the master file system.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2019/04/30/5
- http://www.securityfocus.com/bid/108159
- https://jenkins.io/security/advisory/2019-04-30/#SECURITY-1390
- http://www.openwall.com/lists/oss-security/2019/04/30/5
- http://www.securityfocus.com/bid/108159

---

#### 433. CVE-2019-0872

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0979.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0872
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0872

---

#### 434. CVE-2019-0971

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
An information disclosure vulnerability exists when Azure DevOps Server and Microsoft Team Foundation Server do not properly sanitize a specially crafted authentication request to an affected server, aka 'Azure DevOps Server and Team Foundation Server Information Disclosure Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0971
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0971

---

#### 435. CVE-2019-0979

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server and Team Foundation Server do not properly sanitize user provided input, aka 'Azure DevOps Server and Team Foundation Server Cross-site Scripting Vulnerability'. This CVE ID is unique from CVE-2019-0872.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0979
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0979

---

#### 436. CVE-2019-1000

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists in Microsoft Azure Active Directory Connect build 1.3.20.0, which allows an attacker to execute two PowerShell cmdlets in context of a privileged account, and perform privileged actions.To exploit this, an attacker would need to authenticate to the AzureÃ‚Â AD Connect server, aka 'Microsoft Azure AD Connect Elevation of Privilege Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1000
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1000

---

#### 437. CVE-2019-0996

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
A spoofing vulnerability exists in Azure DevOps Server when it improperly handles requests to authorize applications, resulting in a cross-site request forgery. An attacker who successfully exploited this vulnerability could bypass OAuth protections and register an application on behalf of the targeted user.
To exploit this vulnerability, an attacker would need to create a page specifically designed to cause a cross-site request. The attacker would then need to convince a targeted user to click a link to the malicious page.
The update addresses the vulnerability by modifying how Azure DevOps Server protects application registration requests.

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-0996
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0996

---

#### 438. CVE-2019-0962

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists in Azure Automation "RunAs account" runbooks for users with contributor role, aka 'Azure Automation Elevation of Privilege Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0962
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0962

---

#### 439. CVE-2019-1072

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
A remote code execution vulnerability exists when Azure DevOps Server and Team Foundation Server (TFS) improperly handle user input, aka 'Azure DevOps Server and Team Foundation Server Remote Code Execution Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1072
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1072

---

#### 440. CVE-2019-1172

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
An information disclosure vulnerability exists in Azure Active Directory (AAD) Microsoft Account (MSA) during the login request session. An attacker who successfully exploited the vulnerability could take over a user's account.
To exploit the vulnerability, an attacker would have to trick a user into browsing to a specially crafted website, allowing the attacker to steal the user's token.
The security update addresses the vulnerability by correcting how MSA handles cookies.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1172
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1172

---

#### 441. CVE-2019-1258

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists in Azure Active Directory Authentication Library On-Behalf-Of flow, in the way the library caches tokens. This vulnerability allows an authenticated attacker to perform actions in context of another user.
The authenticated attacker can exploit this vulneraiblity by accessing a service configured for On-Behalf-Of flow that assigns incorrect tokens.
This security update addresses the vulnerability by removing fallback cache look-up for On-Behalf-Of scenarios.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1258
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1258

---

#### 442. CVE-2019-1306

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
A remote code execution vulnerability exists when Azure DevOps Server (ADO) and Team Foundation Server (TFS) fail to validate input properly, aka 'Azure DevOps and Team Foundation Server Remote Code Execution Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1306
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1306

---

#### 443. CVE-2019-16383

**严重程度 / Severity**: CRITICAL | CVSS: 9.4

**漏洞描述 / Description**:
MOVEit.DMZ.WebApi.dll in Progress MOVEit Transfer 2018 SP2 before 10.2.4, 2019 before 11.0.2, and 2019.1 before 11.1.1 allows an unauthenticated attacker to gain unauthorized access to the database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database, or may be able to alter the database via the REST API, aka SQL Injection.

**参考链接 / References**:
- http://packetstormsecurity.com/files/157208/MOVEit-Transfer-11.1.1-SQL-Injection.html
- https://community.ipswitch.com/s/article/SQL-Injection-Vulnerability
- https://docs.ipswitch.com/MOVEit/Transfer2018SP2/ReleaseNotes/en/index.htm#46490.htm
- https://docs.ipswitch.com/MOVEit/Transfer2019/ReleaseNotes/en/index.htm#48648.htm
- https://docs.ipswitch.com/MOVEit/Transfer2019_1/ReleaseNotes/en/index.htm#49443.htm

---

#### 444. CVE-2019-10421

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
Jenkins Azure Event Grid Build Notifier Plugin stores credentials unencrypted in job config.xml files on the Jenkins master where they can be viewed by users with Extended Read permission, or access to the master file system.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2019/09/25/3
- https://jenkins.io/security/advisory/2019-09-25/#SECURITY-1544
- http://www.openwall.com/lists/oss-security/2019/09/25/3
- https://jenkins.io/security/advisory/2019-09-25/#SECURITY-1544

---

#### 445. CVE-2019-1372

**严重程度 / Severity**: CRITICAL | CVSS: 10.0

**漏洞描述 / Description**:
An remote code execution vulnerability exists when Azure App Service/ Antares on Azure Stack fails to check the length of a buffer prior to copying memory to it.An attacker who successfully exploited this vulnerability could allow an unprivileged function run by the user to execute code in the context of NT AUTHORITY\system thereby escaping the Sandbox.The security update addresses the vulnerability by ensuring that Azure App Service sanitizes user inputs., aka 'Azure App Service Remote Code Execution Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1372
- https://research.checkpoint.com/2020/remote-cloud-execution-critical-vulnerabilities-in-azure-cloud-infrastructure-part-ii/
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1372
- https://research.checkpoint.com/2020/remote-cloud-execution-critical-vulnerabilities-in-azure-cloud-infrastructure-part-ii/

---

#### 446. CVE-2019-18464

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In Progress MOVEit Transfer 10.2 before 10.2.6 (2018.3), 11.0 before 11.0.4 (2019.0.4), and 11.1 before 11.1.3 (2019.1.3), multiple SQL Injection vulnerabilities have been found in the REST API that could allow an unauthenticated attacker to gain unauthorized access to the database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database or may be able to alter the database.

**参考链接 / References**:
- https://community.ipswitch.com/s/article/SQL-Injection-Vulnerability-2
- https://docs.ipswitch.com/MOVEit/Transfer2018SP2/ReleaseNotes/en/index.htm#46490.htm
- https://docs.ipswitch.com/MOVEit/Transfer2019/ReleaseNotes/en/index.htm#48648.htm
- https://docs.ipswitch.com/MOVEit/Transfer2019_1/ReleaseNotes/en/index.htm#49443.htm
- https://community.ipswitch.com/s/article/SQL-Injection-Vulnerability-2

---

#### 447. CVE-2019-1234

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
A spoofing vulnerability exists when Azure Stack fails to validate certain requests, aka 'Azure Stack Spoofing Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1234
- https://research.checkpoint.com/2020/remote-cloud-execution-critical-vulnerabilities-in-azure-cloud-infrastructure-part-i/
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1234
- https://research.checkpoint.com/2020/remote-cloud-execution-critical-vulnerabilities-in-azure-cloud-infrastructure-part-i/

---

#### 448. CVE-2019-19316

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
When using the Azure backend with a shared access signature (SAS), Terraform versions prior to 0.12.17 may transmit the token and state snapshot using cleartext HTTP.

**参考链接 / References**:
- https://github.com/hashicorp/terraform/security/advisories/GHSA-4rvg-555h-r626
- https://github.com/hashicorp/terraform/security/advisories/GHSA-4rvg-555h-r626

---

#### 449. CVE-2020-2119

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
Jenkins Azure AD Plugin 1.1.2 and earlier transmits configured credentials in plain text as part of the global Jenkins configuration form, potentially resulting in their exposure.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2020/02/12/3
- https://jenkins.io/security/advisory/2020-02-12/#SECURITY-1717
- http://www.openwall.com/lists/oss-security/2020/02/12/3
- https://jenkins.io/security/advisory/2020-02-12/#SECURITY-1717

---

#### 450. CVE-2020-8611

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In Progress MOVEit Transfer 2019.1 before 2019.1.4 and 2019.2 before 2019.2.1, multiple SQL Injection vulnerabilities have been found in the REST API that could allow an authenticated attacker to gain unauthorized access to MOVEit Transfer's database via the REST API. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database in addition to executing SQL statements that alter or destroy database elements.

**参考链接 / References**:
- https://community.ipswitch.com/s/article/MOVEit-Transfer-Security-Vulnerabilities-Feb-2020
- https://docs.ipswitch.com/MOVEit/Transfer2019_1/ReleaseNotes/en/index.htm#49443.htm
- https://docs.ipswitch.com/MOVEit/Transfer2019_2/ReleaseNotes/en/index.htm#49677.htm
- https://status.moveitcloud.com/
- https://community.ipswitch.com/s/article/MOVEit-Transfer-Security-Vulnerabilities-Feb-2020

---

#### 451. CVE-2019-5160

**严重程度 / Severity**: CRITICAL | CVSS: 9.1

**漏洞描述 / Description**:
An exploitable improper host validation vulnerability exists in the Cloud Connectivity functionality of WAGO PFC200 Firmware versions 03.02.02(14), 03.01.07(13), and 03.00.39(12). A specially crafted HTTPS POST request can cause the software to connect to an unauthorized host, resulting in unauthorized access to firmware update functionality. An attacker can send an authenticated HTTPS POST request to direct the Cloud Connectivity software to connect to an attacker controlled Azure IoT Hub node.

**参考链接 / References**:
- https://talosintelligence.com/vulnerability_reports/TALOS-2019-0953
- https://talosintelligence.com/vulnerability_reports/TALOS-2019-0953

---

#### 452. CVE-2020-0700

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server does not properly sanitize user provided input, aka 'Azure DevOps Server Cross-site Scripting Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0700
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0700

---

#### 453. CVE-2020-0758

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists when Azure DevOps Server and Team Foundation Services improperly handle pipeline job tokens, aka 'Azure DevOps Server and Team Foundation Services Elevation of Privilege Vulnerability'. This CVE ID is unique from CVE-2020-0815.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0758
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0758

---

#### 454. CVE-2020-0815

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
An elevation of privilege vulnerability exists when Azure DevOps Server and Team Foundation Services improperly handle pipeline job tokens, aka 'Azure DevOps Server and Team Foundation Services Elevation of Privilege Vulnerability'. This CVE ID is unique from CVE-2020-0758.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0815
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0815

---

#### 455. CVE-2020-2168

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Jenkins Azure Container Service Plugin 1.0.1 and earlier does not configure its YAML parser to prevent the instantiation of arbitrary types, resulting in a remote code execution vulnerability.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2020/03/25/2
- https://jenkins.io/security/advisory/2020-03-25/#SECURITY-1732
- http://www.openwall.com/lists/oss-security/2020/03/25/2
- https://jenkins.io/security/advisory/2020-03-25/#SECURITY-1732

---

#### 456. CVE-2020-1978

**严重程度 / Severity**: MEDIUM | CVSS: 5.8

**漏洞描述 / Description**:
TechSupport files generated on Palo Alto Networks VM Series firewalls for Microsoft Azure platform configured with high availability (HA) inadvertently collect Azure dashboard service account credentials. These credentials are equivalent to the credentials associated with the Contributor role in Azure. A user with the credentials will be able to manage all the Azure resources in the subscription except for granting access to other resources. These credentials do not allow login access to the VMs themselves. This issue affects VM Series Plugin versions before 1.0.9 for PAN-OS 9.0. This issue does not affect VM Series in non-HA configurations or on other cloud platforms. It does not affect hardware firewall appliances. Since becoming aware of the issue, Palo Alto Networks has safely deleted all the tech support files with the credentials. We now filter and remove these credentials from all TechSupport files sent to us. The TechSupport files uploaded to Palo Alto Networks systems were only accessible by authorized personnel with valid Palo Alto Networks credentials. We do not have any evidence of malicious access or use of these credentials.

**参考链接 / References**:
- https://security.paloaltonetworks.com/CVE-2020-1978
- https://security.paloaltonetworks.com/CVE-2020-1978

---

#### 457. CVE-2020-1327

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
A spoofing vulnerability exists in Microsoft Azure DevOps Server when it fails to properly handle web requests, aka 'Azure DevOps Server HTML Injection Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1327
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1327

---

#### 458. CVE-2020-1326

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
A Cross-site Scripting (XSS) vulnerability exists when Azure DevOps Server does not properly sanitize user provided input, aka 'Azure DevOps Server Cross-site Scripting Vulnerability'.

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1326
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1326

---

#### 459. CVE-2019-11252

**严重程度 / Severity**: MEDIUM | CVSS: 5.9

**漏洞描述 / Description**:
The Kubernetes kube-controller-manager in versions v1.0-v1.17 is vulnerable to a credential leakage via error messages in mount failure logs and events for AzureFile and CephFS volumes.

**参考链接 / References**:
- https://github.com/kubernetes/kubernetes/pull/88684
- https://github.com/kubernetes/kubernetes/pull/88684

---

#### 460. CVE-2020-24566

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
In Octopus Deploy 2020.3.x before 2020.3.4 and 2020.4.x before 2020.4.1, if an authenticated user creates a deployment or runbook process using Azure steps and sets the step's execution location to run on the server/worker, then (under certain circumstances) the account password is exposed in cleartext in the verbose task logs output.

**参考链接 / References**:
- https://github.com/OctopusDeploy/Issues/issues/6563
- https://github.com/OctopusDeploy/Issues/issues/6564
- https://github.com/OctopusDeploy/Issues/issues/6563
- https://github.com/OctopusDeploy/Issues/issues/6564

---

#### 461. CVE-2020-16904

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
<p>An elevation of privilege vulnerability exists in the way Azure Functions validate access keys.</p>
<p>An unauthenticated attacker who successfully exploited this vulnerability could invoke an HTTP Function without proper authorization.</p>
<p>This security update addresses the vulnerability by correctly validating access keys used to access HTTP Functions.</p>

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16904
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16904

---

#### 462. CVE-2020-2313

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
A missing permission check in Jenkins Azure Key Vault Plugin 2.0 and earlier allows attackers with Overall/Read permission to enumerate credentials IDs of credentials stored in Jenkins.

**参考链接 / References**:
- https://www.jenkins.io/security/advisory/2020-11-04/#SECURITY-2110
- https://www.jenkins.io/security/advisory/2020-11-04/#SECURITY-2110

---

#### 463. CVE-2020-16970

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16970
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1118
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16970
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1118

---

#### 464. CVE-2020-16981

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16981
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16981

---

#### 465. CVE-2020-16982

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16982
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1131
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1132
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16982
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1131

---

#### 466. CVE-2020-16983

**严重程度 / Severity**: MEDIUM | CVSS: 5.7

**漏洞描述 / Description**:
Azure Sphere Tampering Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16983
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16983

---

#### 467. CVE-2020-16984

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16984
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1128
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16984
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1128

---

#### 468. CVE-2020-16985

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16985
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1130
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16985
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1130

---

#### 469. CVE-2020-16986

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
Azure Sphere Denial of Service Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16986
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1129
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16986
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1129

---

#### 470. CVE-2020-16987

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16987
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1138
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16987
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1138

---

#### 471. CVE-2020-16988

**严重程度 / Severity**: MEDIUM | CVSS: 6.9

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16988
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16988

---

#### 472. CVE-2020-16989

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16989
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16989

---

#### 473. CVE-2020-16990

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16990
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1089
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16990
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1089

---

#### 474. CVE-2020-16991

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16991
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1090
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16991
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1090

---

#### 475. CVE-2020-16992

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16992
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1133
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16992
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1133

---

#### 476. CVE-2020-16993

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16993
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1137
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16993
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1137

---

#### 477. CVE-2020-16994

**严重程度 / Severity**: HIGH | CVSS: 7.3

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16994
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1093
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16994
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1093

---

#### 478. CVE-2020-1325

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
Azure DevOps Server and Team Foundation Services Spoofing Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1325
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1325

---

#### 479. CVE-2020-16971

**严重程度 / Severity**: HIGH | CVSS: 7.4

**漏洞描述 / Description**:
Azure SDK for Java Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-16971
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16971

---

#### 480. CVE-2020-17002

**严重程度 / Severity**: HIGH | CVSS: 7.4

**漏洞描述 / Description**:
Azure SDK for C Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17002
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-17002

---

#### 481. CVE-2020-17135

**严重程度 / Severity**: MEDIUM | CVSS: 6.4

**漏洞描述 / Description**:
Azure DevOps Server Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17135
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-17135

---

#### 482. CVE-2020-17145

**严重程度 / Severity**: MEDIUM | CVSS: 5.4

**漏洞描述 / Description**:
Azure DevOps Server and Team Foundation Services Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17145
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-17145

---

#### 483. CVE-2020-35608

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
A code execution vulnerability exists in the normal world’s signed code execution functionality of Microsoft Azure Sphere 20.07. A specially crafted AF_PACKET socket can cause a process to create an executable memory mapping with controllable content. An attacker can execute a shellcode that uses the PACKET_MMAP functionality to trigger this vulnerability.

**参考链接 / References**:
- https://talosintelligence.com/vulnerability_reports/TALOS-2020-1134
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1134
- https://talosintelligence.com/vulnerability_reports/TALOS-2020-1134
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1134

---

#### 484. CVE-2020-35609

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
A denial-of-service vulnerability exists in the asynchronous ioctl functionality of Microsoft Azure Sphere 20.05. A sequence of specially crafted ioctl calls can cause a denial of service. An attacker can write shellcode to trigger this vulnerability.

**参考链接 / References**:
- https://talosintelligence.com/vulnerability_reports/TALOS-2020-1117
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1117
- https://talosintelligence.com/vulnerability_reports/TALOS-2020-1117
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2020-1117

---

#### 485. CVE-2021-1677

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Azure Active Directory Pod Identity Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1677
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-1677

---

#### 486. CVE-2020-8567

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Kubernetes Secrets Store CSI Driver Vault Plugin prior to v0.0.6, Azure Plugin prior to v0.0.10, and GCP Plugin prior to v0.2.0 allow an attacker who can create specially-crafted SecretProviderClass objects to write to arbitrary file paths on the host filesystem, including /var/lib/kubelet/pods.

**参考链接 / References**:
- https://github.com/kubernetes-sigs/secrets-store-csi-driver/issues/384
- https://groups.google.com/g/kubernetes-secrets-store-csi-driver/c/BI2qisiNXHY
- https://github.com/kubernetes-sigs/secrets-store-csi-driver/issues/384
- https://groups.google.com/g/kubernetes-secrets-store-csi-driver/c/BI2qisiNXHY

---

#### 487. CVE-2021-20327

**严重程度 / Severity**: MEDIUM | CVSS: 6.4

**漏洞描述 / Description**:
A specific version of the Node.js mongodb-client-encryption module does not perform correct validation of the KMS server’s certificate. This vulnerability in combination with a privileged network position active MITM attack could result in interception of traffic between the Node.js driver and the KMS service rendering client-side field level encryption (CSFLE) ineffective. This issue was discovered during internal testing and affects mongodb-client-encryption module version 1.2.0, which was available from 2021-Jan-29 and deprecated in the NPM Registry on 2021-Feb-04. This vulnerability does not impact driver traffic payloads with CSFLE-supported key services from applications residing inside the AWS, GCP, and Azure nework fabrics due to compensating controls in these environments. This issue does not impact driver workloads that don’t use Field Level Encryption. This issue affect MongoDB Node.js Driver mongodb-client-encryption module version 1.2.0

**参考链接 / References**:
- https://jira.mongodb.org/browse/NODE-3125
- https://jira.mongodb.org/browse/NODE-3125

---

#### 488. CVE-2021-20328

**严重程度 / Severity**: MEDIUM | CVSS: 6.4

**漏洞描述 / Description**:
Specific versions of the Java driver that support client-side field level encryption (CSFLE) fail to perform correct host name verification on the KMS server’s certificate. This vulnerability in combination with a privileged network position active MITM attack could result in interception of traffic between the Java driver and the KMS service rendering Field Level Encryption ineffective. This issue was discovered during internal testing and affects all versions of the Java driver that support CSFLE. The Java async, Scala, and reactive streams drivers are not impacted. This vulnerability does not impact driver traffic payloads with CSFLE-supported key services originating from applications residing inside the AWS, GCP, and Azure network fabrics due to compensating controls in these environments. This issue does not impact driver workloads that don’t use Field Level Encryption.

**参考链接 / References**:
- https://jira.mongodb.org/browse/JAVA-4017
- https://jira.mongodb.org/browse/JAVA-4017

---

#### 489. CVE-2021-24087

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Azure IoT CLI extension Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-24087
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-24087

---

#### 490. CVE-2021-24109

**严重程度 / Severity**: MEDIUM | CVSS: 6.8

**漏洞描述 / Description**:
Microsoft Azure Kubernetes Service Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-24109
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-24109

---

#### 491. CVE-2021-27074

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27074
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2021-1247
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2021-1249
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27074
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2021-1247

---

#### 492. CVE-2021-27075

**严重程度 / Severity**: MEDIUM | CVSS: 6.8

**漏洞描述 / Description**:
Azure Virtual Machine Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27075
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27075

---

#### 493. CVE-2021-27080

**严重程度 / Severity**: CRITICAL | CVSS: 9.3

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27080
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2021-1250
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27080
- https://www.talosintelligence.com/vulnerability_reports/TALOS-2021-1250

---

#### 494. CVE-2021-3413

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
A flaw was found in Red Hat Satellite in tfm-rubygem-foreman_azure_rm in versions before 2.2.0. A credential leak was identified which will expose Azure Resource Manager's secret key through JSON of the API output. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**参考链接 / References**:
- https://bugzilla.redhat.com/show_bug.cgi?id=1930352
- https://bugzilla.redhat.com/show_bug.cgi?id=1930352

---

#### 495. CVE-2021-27067

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure DevOps Server and Team Foundation Server Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27067
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27067

---

#### 496. CVE-2021-27092

**严重程度 / Severity**: MEDIUM | CVSS: 6.8

**漏洞描述 / Description**:
Azure AD Web Sign-in Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27092
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-27092

---

#### 497. CVE-2021-28458

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure ms-rest-nodeauth Library Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-28458
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-28458

---

#### 498. CVE-2021-28459

**严重程度 / Severity**: MEDIUM | CVSS: 6.1

**漏洞描述 / Description**:
Azure DevOps Server Spoofing Vulnerability

**参考链接 / References**:
- http://packetstormsecurity.com/files/162190/Microsoft-Azure-DevOps-Server-2020.0.1-Cross-Site-Scripting.html
- http://seclists.org/fulldisclosure/2021/Apr/25
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-28459
- http://packetstormsecurity.com/files/162190/Microsoft-Azure-DevOps-Server-2020.0.1-Cross-Site-Scripting.html
- http://seclists.org/fulldisclosure/2021/Apr/25

---

#### 499. CVE-2021-28460

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure Sphere Unsigned Code Execution Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-28460
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-28460

---

#### 500. CVE-2021-21505

**严重程度 / Severity**: HIGH | CVSS: 8.0

**漏洞描述 / Description**:
Dell EMC Integrated System for Microsoft Azure Stack Hub, versions 1906 – 2011, contain an undocumented default iDRAC account. A remote unauthenticated attacker, with the knowledge of the default credentials, could potentially exploit this to log in to the system to gain root privileges.

**参考链接 / References**:
- https://www.dell.com/support/kbdoc/en-us/000186008/dsa-2021-020-dell-emc-integrated-system-for-microsoft-azure-stack-hub-security-update-for-an-idrac-undocumented-account-vulnerability
- https://www.dell.com/support/kbdoc/en-us/000186008/dsa-2021-020-dell-emc-integrated-system-for-microsoft-azure-stack-hub-security-update-for-an-idrac-undocumented-account-vulnerability

---

#### 501. CVE-2021-31827

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In Progress MOVEit Transfer before 2021.0 (13.0), a SQL injection vulnerability has been found in the MOVEit Transfer web app that could allow an authenticated attacker to gain unauthorized access to MOVEit Transfer's database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database in addition to executing SQL statements that alter or destroy database elements. This is in MOVEit.DMZ.WebApp in SILHuman.vb.

**参考链接 / References**:
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-April-2021
- https://docs.ipswitch.com/MOVEit/Transfer2021/ReleaseNotes/en/index.htm
- https://www.progress.com/moveit
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-April-2021
- https://docs.ipswitch.com/MOVEit/Transfer2021/ReleaseNotes/en/index.htm

---

#### 502. CVE-2021-33894

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In Progress MOVEit Transfer before 2019.0.6 (11.0.6), 2019.1.x before 2019.1.5 (11.1.5), 2019.2.x before 2019.2.2 (11.2.2), 2020.x before 2020.0.5 (12.0.5), 2020.1.x before 2020.1.4 (12.1.4), and 2021.x before 2021.0.1 (13.0.1), a SQL injection vulnerability exists in SILUtility.vb in MOVEit.DMZ.WebApp in the MOVEit Transfer web app. This could allow an authenticated attacker to gain unauthorized access to the database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database and/or execute SQL statements that alter or delete database elements.

**参考链接 / References**:
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-June-2021
- https://www.progress.com/moveit
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-June-2021
- https://www.progress.com/moveit

---

#### 503. CVE-2021-33781

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure AD Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33781
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33781

---

#### 504. CVE-2021-37614

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
In certain Progress MOVEit Transfer versions before 2021.0.3 (aka 13.0.3), SQL injection in the MOVEit Transfer web application could allow an authenticated remote attacker to gain access to the database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database, or execute SQL statements that alter or delete database elements, via crafted strings sent to unique MOVEit Transfer transaction types. The fixed versions are 2019.0.7 (11.0.7), 2019.1.6 (11.1.6), 2019.2.3 (11.2.3), 2020.0.6 (12.0.6), 2020.1.5 (12.1.5), and 2021.0.3 (13.0.3).

**参考链接 / References**:
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-August-2021
- https://docs.ipswitch.com/MOVEit/Transfer2019/ReleaseNotes/en/index.htm#48648.htm
- https://docs.ipswitch.com/MOVEit/Transfer2020/ReleaseNotes/en/index.htm#50951.htm
- https://docs.ipswitch.com/MOVEit/Transfer2021/ReleaseNotes/en/index.htm#link8
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-August-2021

---

#### 505. CVE-2021-38159

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In certain Progress MOVEit Transfer versions before 2021.0.4 (aka 13.0.4), SQL injection in the MOVEit Transfer web application could allow an unauthenticated remote attacker to gain access to the database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database, or execute SQL statements that alter or delete database elements, via crafted strings sent to unique MOVEit Transfer transaction types. The fixed versions are 2019.0.8 (11.0.8), 2019.1.7 (11.1.7), 2019.2.4 (11.2.4), 2020.0.7 (12.0.7), 2020.1.6 (12.1.6), and 2021.0.4 (13.0.4).

**参考链接 / References**:
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-August-6-2021
- https://www.progress.com/moveit
- https://community.progress.com/s/article/MOVEit-Transfer-Vulnerability-August-6-2021
- https://www.progress.com/moveit

---

#### 506. CVE-2021-26428

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26428
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26428

---

#### 507. CVE-2021-26429

**严重程度 / Severity**: HIGH | CVSS: 7.7

**漏洞描述 / Description**:
Azure Sphere Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26429
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26429

---

#### 508. CVE-2021-26430

**严重程度 / Severity**: MEDIUM | CVSS: 6.0

**漏洞描述 / Description**:
Azure Sphere Denial of Service Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26430
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26430

---

#### 509. CVE-2021-33762

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Azure CycleCloud Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33762
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33762

---

#### 510. CVE-2021-36943

**严重程度 / Severity**: MEDIUM | CVSS: 4.0

**漏洞描述 / Description**:
Azure CycleCloud Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36943
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36943

---

#### 511. CVE-2021-36949

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
Microsoft Azure Active Directory Connect Authentication Bypass Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36949
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36949

---

#### 512. CVE-2021-37705

**严重程度 / Severity**: CRITICAL | CVSS: 10.0

**漏洞描述 / Description**:
OneFuzz is an open source self-hosted Fuzzing-As-A-Service platform. Starting with OneFuzz 2.12.0 or greater, an incomplete authorization check allows an authenticated user from any Azure Active Directory tenant to make authorized API calls to a vulnerable OneFuzz instance. To be vulnerable, a OneFuzz deployment must be both version 2.12.0 or greater and deployed with the non-default --multi_tenant_domain option. This can result in read/write access to private data such as software vulnerability and crash information, security testing tools and proprietary code and symbols. Via authorized API calls, this also enables tampering with existing data and unauthorized code execution on Azure compute resources. This issue is resolved starting in release 2.31.0, via the addition of application-level check of the bearer token's `issuer` against an administrator-configured allowlist. As a workaround users can restrict access to the tenant of a deployed OneFuzz instance < 2.31.0 by redeploying in the default configuration, which omits the `--multi_tenant_domain` option.

**参考链接 / References**:
- https://github.com/microsoft/onefuzz/commit/2fcb4998887959b4fa11894a068d689189742cb1
- https://github.com/microsoft/onefuzz/pull/1153
- https://github.com/microsoft/onefuzz/releases/tag/2.31.0
- https://github.com/microsoft/onefuzz/security/advisories/GHSA-q5vh-6whw-x745
- https://pypi.org/project/onefuzz/

---

#### 513. CVE-2021-21679

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Jenkins Azure AD Plugin 179.vf6841393099e and earlier allows attackers to craft URLs that would bypass the CSRF protection of any target URL in Jenkins.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2021/08/31/1
- https://www.jenkins.io/security/advisory/2021-08-31/#SECURITY-2470
- http://www.openwall.com/lists/oss-security/2021/08/31/1
- https://www.jenkins.io/security/advisory/2021-08-31/#SECURITY-2470

---

#### 514. CVE-2021-36956

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36956
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36956

---

#### 515. CVE-2021-35494

**严重程度 / Severity**: MEDIUM | CVSS: 5.7

**漏洞描述 / Description**:
The Rest API component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for ActiveMatrix BPM, and TIBCO JasperReports Server for Microsoft Azure contain a race condition that allows a low privileged authenticated attacker via the REST API to obtain read access to temporary objects created by other users on the affected system. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 7.2.1 and below, TIBCO JasperReports Server: versions 7.5.0 and 7.5.1, TIBCO JasperReports Server: version 7.8.0, TIBCO JasperReports Server: version 7.9.0, TIBCO JasperReports Server - Community Edition: versions 7.8.0 and below, TIBCO JasperReports Server - Developer Edition: versions 7.9.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 7.9.0 and below, TIBCO JasperReports Server for ActiveMatrix BPM: versions 7.9.0 and below, and TIBCO JasperReports Server for Microsoft Azure: version 7.8.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2021/10/tibco-security-advisory-october-12-2021-tibco-jasperreports-server-2021-35494
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2021/10/tibco-security-advisory-october-12-2021-tibco-jasperreports-server-2021-35494

---

#### 516. CVE-2021-35495

**严重程度 / Severity**: CRITICAL | CVSS: 9.0

**漏洞描述 / Description**:
The Scheduler Connection component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for ActiveMatrix BPM, and TIBCO JasperReports Server for Microsoft Azure contains an easily exploitable vulnerability that allows an authenticated attacker with network access to obtain FTP server passwords for other users of the affected system. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 7.2.1 and below, TIBCO JasperReports Server: versions 7.5.0 and 7.5.1, TIBCO JasperReports Server: version 7.8.0, TIBCO JasperReports Server: version 7.9.0, TIBCO JasperReports Server - Community Edition: versions 7.8.0 and below, TIBCO JasperReports Server - Developer Edition: versions 7.9.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 7.9.0 and below, TIBCO JasperReports Server for ActiveMatrix BPM: versions 7.9.0 and below, and TIBCO JasperReports Server for Microsoft Azure: version 7.8.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2021/10/tibco-security-advisory-october-12-2021-tibco-jasperreports-server-2021-35495
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2021/10/tibco-security-advisory-october-12-2021-tibco-jasperreports-server-2021-35495

---

#### 517. CVE-2021-35496

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
The XMLA Connections component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for ActiveMatrix BPM, and TIBCO JasperReports Server for Microsoft Azure contains a difficult to exploit vulnerability that allows a low privileged attacker with network access to interfere with XML processing in the affected component. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 7.2.1 and below, TIBCO JasperReports Server: versions 7.5.0 and 7.5.1, TIBCO JasperReports Server: version 7.8.0, TIBCO JasperReports Server: version 7.9.0, TIBCO JasperReports Server - Community Edition: versions 7.8.0 and below, TIBCO JasperReports Server - Developer Edition: versions 7.9.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 7.9.0 and below, TIBCO JasperReports Server for ActiveMatrix BPM: versions 7.9.0 and below, and TIBCO JasperReports Server for Microsoft Azure: version 7.8.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/services/support/advisories

---

#### 518. CVE-2021-40371

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Gridpro Request Management for Windows Azure Pack before 2.0.7912 allows Directory Traversal for remote code execution, as demonstrated by ..\\ in a scriptName JSON value to ServiceManagerTenant/GetVisibilityMap.

**参考链接 / References**:
- http://packetstormsecurity.com/files/164621/GridPro-Request-Management-For-Windows-Azure-Pack-2.0.7905-Directory-Traversal.html
- http://seclists.org/fulldisclosure/2021/Oct/33
- https://www.gridprosoftware.com/products/requestmanagement/
- http://packetstormsecurity.com/files/164621/GridPro-Request-Management-For-Windows-Azure-Pack-2.0.7905-Directory-Traversal.html
- http://seclists.org/fulldisclosure/2021/Oct/33

---

#### 519. CVE-2021-26444

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
Azure RTOS Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26444
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26444

---

#### 520. CVE-2021-41374

**严重程度 / Severity**: MEDIUM | CVSS: 6.7

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41374
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41374

---

#### 521. CVE-2021-41375

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41375
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41375

---

#### 522. CVE-2021-41376

**严重程度 / Severity**: LOW | CVSS: 2.3

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41376
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41376

---

#### 523. CVE-2021-42300

**严重程度 / Severity**: MEDIUM | CVSS: 6.0

**漏洞描述 / Description**:
Azure Sphere Tampering Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42300
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42300

---

#### 524. CVE-2021-42301

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
Azure RTOS Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42301
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42301

---

#### 525. CVE-2021-42302

**严重程度 / Severity**: MEDIUM | CVSS: 6.6

**漏洞描述 / Description**:
Azure RTOS Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42302
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42302

---

#### 526. CVE-2021-42303

**严重程度 / Severity**: MEDIUM | CVSS: 6.6

**漏洞描述 / Description**:
Azure RTOS Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42303
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42303

---

#### 527. CVE-2021-42304

**严重程度 / Severity**: MEDIUM | CVSS: 6.6

**漏洞描述 / Description**:
Azure RTOS Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42304
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42304

---

#### 528. CVE-2021-42323

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
Azure RTOS Information Disclosure Vulnerability

**参考链接 / References**:
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42323
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42323

---

#### 529. CVE-2021-34423

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
A buffer overflow vulnerability was discovered in Zoom Client for Meetings (for Android, iOS, Linux, macOS, and Windows) before version 5.8.4, Zoom Client for Meetings for Blackberry (for Android and iOS) before version 5.8.1, Zoom Client for Meetings for intune (for Android and iOS) before version 5.8.4, Zoom Client for Meetings for Chrome OS before version 5.0.1, Zoom Rooms for Conference Room (for Android, AndroidBali, macOS, and Windows) before version 5.8.3, Controllers for Zoom Rooms (for Android, iOS, and Windows) before version 5.8.3, Zoom VDI Windows Meeting Client before version 5.8.4, Zoom VDI Azure Virtual Desktop Plugins (for Windows x86 or x64, IGEL x64, Ubuntu x64, HP ThinPro OS x64) before version 5.8.4.21112, Zoom VDI Citrix Plugins (for Windows x86 or x64, Mac Universal Installer & Uninstaller, IGEL x64, eLux RP6 x64, HP ThinPro OS x64, Ubuntu x64, CentOS x 64, Dell ThinOS) before version 5.8.4.21112, Zoom VDI VMware Plugins (for Windows x86 or x64, Mac Universal Installer & Uninstaller, IGEL x64, eLux RP6 x64, HP ThinPro OS x64, Ubuntu x64, CentOS x 64, Dell ThinOS) before version 5.8.4.21112, Zoom Meeting SDK for Android before version 5.7.6.1922, Zoom Meeting SDK for iOS before version 5.7.6.1082, Zoom Meeting SDK for macOS before version 5.7.6.1340, Zoom Meeting SDK for Windows before version 5.7.6.1081, Zoom Video SDK (for Android, iOS, macOS, and Windows) before version 1.1.2, Zoom On-Premise Meeting Connector Controller before version 4.8.12.20211115, Zoom On-Premise Meeting Connector MMR before version 4.8.12.20211115, Zoom On-Premise Recording Connector before version 5.1.0.65.20211116, Zoom On-Premise Virtual Room Connector before version 4.4.7266.20211117, Zoom On-Premise Virtual Room Connector Load Balancer before version 2.5.5692.20211117, Zoom Hybrid Zproxy before version 1.0.1058.20211116, and Zoom Hybrid MMR before version 4.6.20211116.131_x86-64. This can potentially allow a malicious actor to crash the service or application, or leverage this vulnerability to execute arbitrary code.

**参考链接 / References**:
- http://packetstormsecurity.com/files/165417/Zoom-Chat-Message-Processing-Buffer-Overflow.html
- https://explore.zoom.us/en/trust/security/security-bulletin
- http://packetstormsecurity.com/files/165417/Zoom-Chat-Message-Processing-Buffer-Overflow.html
- https://explore.zoom.us/en/trust/security/security-bulletin

---

#### 530. CVE-2021-34424

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
A vulnerability was discovered in the Zoom Client for Meetings (for Android, iOS, Linux, macOS, and Windows) before version 5.8.4, Zoom Client for Meetings for Blackberry (for Android and iOS) before version 5.8.1, Zoom Client for Meetings for intune (for Android and iOS) before version 5.8.4, Zoom Client for Meetings for Chrome OS before version 5.0.1, Zoom Rooms for Conference Room (for Android, AndroidBali, macOS, and Windows) before version 5.8.3, Controllers for Zoom Rooms (for Android, iOS, and Windows) before version 5.8.3, Zoom VDI Windows Meeting Client before version 5.8.4, Zoom VDI Azure Virtual Desktop Plugins (for Windows x86 or x64, IGEL x64, Ubuntu x64, HP ThinPro OS x64) before version 5.8.4.21112, Zoom VDI Citrix Plugins (for Windows x86 or x64, Mac Universal Installer & Uninstaller, IGEL x64, eLux RP6 x64, HP ThinPro OS x64, Ubuntu x64, CentOS x 64, Dell ThinOS) before version 5.8.4.21112, Zoom VDI VMware Plugins (for Windows x86 or x64, Mac Universal Installer & Uninstaller, IGEL x64, eLux RP6 x64, HP ThinPro OS x64, Ubuntu x64, CentOS x 64, Dell ThinOS) before version 5.8.4.21112, Zoom Meeting SDK for Android before version 5.7.6.1922, Zoom Meeting SDK for iOS before version 5.7.6.1082, Zoom Meeting SDK for macOS before version 5.7.6.1340, Zoom Meeting SDK for Windows before version 5.7.6.1081, Zoom Video SDK (for Android, iOS, macOS, and Windows) before version 1.1.2, Zoom on-premise Meeting Connector before version 4.8.12.20211115, Zoom on-premise Meeting Connector MMR before version 4.8.12.20211115, Zoom on-premise Recording Connector before version 5.1.0.65.20211116, Zoom on-premise Virtual Room Connector before version 4.4.7266.20211117, Zoom on-premise Virtual Room Connector Load Balancer before version 2.5.5692.20211117, Zoom Hybrid Zproxy before version 1.0.1058.20211116, and Zoom Hybrid MMR before version 4.6.20211116.131_x86-64 which potentially allowed for the exposure of the state of process memory. This issue could be used to potentially gain insight into arbitrary areas of the product's memory.

**参考链接 / References**:
- http://packetstormsecurity.com/files/165419/Zoom-MMR-Server-Information-Leak.html
- https://explore.zoom.us/en/trust/security/security-bulletin
- http://packetstormsecurity.com/files/165419/Zoom-MMR-Server-Information-Leak.html
- https://explore.zoom.us/en/trust/security/security-bulletin

---

#### 531. CVE-2022-23256

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure Data Explorer Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-23256
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23256

---

#### 532. CVE-2021-36302

**严重程度 / Severity**: CRITICAL | CVSS: 9.9

**漏洞描述 / Description**:
All Dell EMC Integrated System for Microsoft Azure Stack Hub versions contain a privilege escalation vulnerability. A remote malicious user with standard level JEA credentials may potentially exploit this vulnerability to elevate privileges and take over the system.

**参考链接 / References**:
- https://www.dell.com/support/kbdoc/en-us/000191165/dsa-2021-178-dell-emc-integrated-solution-for-microsoft-azure-stack-hub-security-update-for-a-just-enough-administration-jea-vulnerability
- https://www.dell.com/support/kbdoc/en-us/000191165/dsa-2021-178-dell-emc-integrated-solution-for-microsoft-azure-stack-hub-security-update-for-a-just-enough-administration-jea-vulnerability

---

#### 533. CVE-2022-23232

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
StorageGRID (formerly StorageGRID Webscale) versions prior to 11.6.0 are susceptible to a vulnerability which when successfully exploited could allow disabled, expired, or locked external user accounts to access S3 data to which they previously had access. StorageGRID 11.6.0 obtains the user account status from Active Directory or Azure and will block S3 access for disabled user accounts during the subsequent background synchronization. User accounts that are expired or locked for Active Directory or Azure, or user accounts that are disabled, expired, or locked in identity sources other than Active Directory or Azure must be manually removed from group memberships or have their S3 keys manually removed from Tenant Manager in all versions of StorageGRID (formerly StorageGRID Webscale).

**参考链接 / References**:
- https://security.netapp.com/advisory/NTAP-20220303-0009/
- https://security.netapp.com/advisory/NTAP-20220303-0009/

---

#### 534. CVE-2022-24467

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24467
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24467

---

#### 535. CVE-2022-24468

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24468
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24468

---

#### 536. CVE-2022-24469

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24469
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24469

---

#### 537. CVE-2022-24470

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24470
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24470

---

#### 538. CVE-2022-24471

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24471
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24471

---

#### 539. CVE-2022-24506

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24506
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24506

---

#### 540. CVE-2022-24515

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24515
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24515

---

#### 541. CVE-1999-1189

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Netscape Navigator/Communicator 4.7 for Windows 95 and Windows 98 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long argument after the ? character in a URL that references an .asp, .cgi, .html, or .pl file.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/36306
- http://www.securityfocus.com/archive/1/36608
- http://www.securityfocus.com/bid/822
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7884
- http://www.securityfocus.com/archive/1/36306

---

#### 542. CVE-1999-0387

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
A legacy credential caching mechanism used in Windows 95 and Windows 98 systems allows attackers to read plaintext network passwords.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ168115
- http://www.securityfocus.com/bid/829
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-052
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ168115
- http://www.securityfocus.com/bid/829

---

#### 543. CVE-1999-0839

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Windows NT Task Scheduler installed with Internet Explorer 5 allows a user to gain privileges by modifying the job after it has been scheduled.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246972
- http://www.securityfocus.com/bid/828
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-051
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246972
- http://www.securityfocus.com/bid/828

---

#### 544. CVE-1999-0824

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
A Windows NT user can use SUBST to map a drive letter to a folder, which is not unmapped after the user logs off, potentially allowing that user to modify the location of folders accessed by later users.

**参考链接 / References**:
- http://www.securityfocus.com/bid/833
- http://www.securityfocus.com/bid/833

---

#### 545. CVE-1999-0975

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Windows help system can allow a local user to execute commands as another user by editing a table of contents metafile with a .CNT extension and modifying the topic action to include the commands to be executed when the .hlp file is accessed.

**参考链接 / References**:
- http://www.securityfocus.com/bid/868
- http://www.securityfocus.com/bid/868

---

#### 546. CVE-1999-0994

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT with SYSKEY reuses the keystream that is used for encrypting SAM password hashes, allowing an attacker to crack passwords.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248183
- http://www.securityfocus.com/bid/873
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-056
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248183
- http://www.securityfocus.com/bid/873

---

#### 547. CVE-2000-0119

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configurations for McAfee Virus Scan and Norton Anti-Virus virus checkers do not check files in the RECYCLED folder that is used by the Windows Recycle Bin utility, which allows attackers to store malicious code without detection.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=94936267131123&w=2
- http://marc.info/?l=bugtraq&m=94936267131123&w=2

---

#### 548. CVE-1999-0815

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in SNMP agent in Windows NT 4.0 before SP5 allows remote attackers to conduct a denial of service (memory exhaustion) via a large number of queries.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q196/2/70.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1974
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A952
- http://support.microsoft.com/support/kb/articles/q196/2/70.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/1974

---

#### 549. CVE-1999-1104

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Windows 95 uses weak encryption for the password list (.pwl) file used when password caching is enabled, which allows local users to gain privileges by decrypting the passwords.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=87602167418931&w=2
- http://marc.info/?l=bugtraq&m=88536273725787&w=2
- http://marc.info/?l=ntbugtraq&m=88540877601866&w=2
- http://support.microsoft.com/support/kb/articles/q140/5/57.asp
- http://www.iss.net/security_center/static/71.php

---

#### 550. CVE-1999-1105

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95, when Remote Administration and File Sharing for NetWare Networks is enabled, creates a share (C$) when an administrator logs in remotely, which allows remote attackers to read arbitrary files by mapping the network drive.

**参考链接 / References**:
- http://www.iss.net/security_center/static/7231.php
- http://www.net-security.sk/bugs/NT/netware1.html
- http://www.zdnet.com/eweek/reviews/1016/tr42bug.html
- http://www.iss.net/security_center/static/7231.php
- http://www.net-security.sk/bugs/NT/netware1.html

---

#### 551. CVE-1999-1127

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Windows NT 4.0 does not properly shut down invalid named pipe RPC connections, which allows remote attackers to cause a denial of service (resource exhaustion) via a series of connections containing malformed data, aka the "Named Pipes Over RPC" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q195/7/33.asp
- http://www.iss.net/security_center/static/523.php
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1998/ms98-017
- http://support.microsoft.com/support/kb/articles/Q195/7/33.asp
- http://www.iss.net/security_center/static/523.php

---

#### 552. CVE-1999-1132

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 allows remote attackers to cause a denial of service (crash) via extra source routing data such as (1) a Routing Information Field (RIF) field with a hop count greater than 7, or (2) a list containing duplicate Token Ring IDs.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=90763508011966&w=2
- http://marc.info/?l=ntbugtraq&m=90760603030452&w=2
- http://support.microsoft.com/support/kb/articles/Q179/1/57.asp
- http://www.iss.net/security_center/static/1399.php
- http://marc.info/?l=bugtraq&m=90763508011966&w=2

---

#### 553. CVE-1999-1157

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Tcpip.sys in Windows NT 4.0 before SP4 allows remote attackers to cause a denial of service via an ICMP Subnet Mask Address Request packet, when certain multiple IP addresses are bound to the same network interface.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q192/7/74.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3894
- http://support.microsoft.com/support/kb/articles/Q192/7/74.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3894

---

#### 554. CVE-1999-1206

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
SystemSoft SystemWizard package in HP Pavilion PC with Windows 98, and possibly other platforms and operating systems, installs two ActiveX controls that are marked as safe for scripting, which allows remote attackers to execute arbitrary commands via a malicious web page that references (1) the Launch control, or (2) the RegObj control.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=93336970231857&w=2
- http://www.securityfocus.com/bid/555
- http://www.systemsoft.com/l-2/l-3/support-systemwizard.htm
- http://marc.info/?l=bugtraq&m=93336970231857&w=2
- http://www.securityfocus.com/bid/555

---

#### 555. CVE-1999-1222

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Netbt.sys in Windows NT 4.0 allows remote malicious DNS servers to cause a denial of service (crash) by returning 0.0.0.0 as the IP address for a DNS host name lookup.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q188/5/71.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3893
- http://support.microsoft.com/support/kb/articles/Q188/5/71.ASP
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3893

---

#### 556. CVE-1999-1294

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Office Shortcut Bar (OSB) in Windows 3.51 enables backup and restore permissions, which are inherited by programs such as File Manager that are started from the Shortcut Bar, which could allow local users to read folders for which they do not have permission.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q146/6/04.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/562
- http://support.microsoft.com/support/kb/articles/q146/6/04.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/562

---

#### 557. CVE-1999-1316

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Passfilt.dll in Windows NT SP2 allows users to create a password that contains the user's name, which could make it easier for an attacker to guess.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/Q247/9/75.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7391
- http://support.microsoft.com/support/kb/articles/Q247/9/75.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7391

---

#### 558. CVE-1999-1317

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Windows NT 4.0 SP4 and earlier allows local users to gain privileges by modifying the symbolic link table in the \?? object folder using a different case letter (upper or lower) to point to a different device.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=92127046701349&w=2
- http://marc.info/?l=ntbugtraq&m=92162979530341&w=2
- http://support.microsoft.com/support/kb/articles/q222/1/59.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7398
- http://marc.info/?l=ntbugtraq&m=92127046701349&w=2

---

#### 559. CVE-1999-1358

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
When an administrator in Windows NT or Windows 2000 changes a user policy, the policy is not properly updated if the local ntconfig.pol is not writable by the user, which could allow local users to bypass restrictions that would otherwise be enforced by the policy, possibly by changing the policy file to be read-only.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q157/6/73.asp
- http://www.iss.net/security_center/static/7400.php
- http://support.microsoft.com/support/kb/articles/q157/6/73.asp
- http://www.iss.net/security_center/static/7400.php

---

#### 560. CVE-1999-1359

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
When the Ntconfig.pol file is used on a server whose name is longer than 13 characters, Windows NT does not properly enforce policies for global groups, which could allow users to bypass restrictions that were intended by those policies.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/8/75.asp
- http://www.iss.net/security_center/static/7401.php
- http://support.microsoft.com/support/kb/articles/q163/8/75.asp
- http://www.iss.net/security_center/static/7401.php

---

#### 561. CVE-1999-1360

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows NT 4.0 allows local users to cause a denial of service via a user mode application that closes a handle that was opened in kernel mode, which causes a crash when the kernel attempts to close the handle.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q160/6/50.asp
- http://www.iss.net/security_center/static/7402.php
- http://support.microsoft.com/support/kb/articles/q160/6/50.asp
- http://www.iss.net/security_center/static/7402.php

---

#### 562. CVE-1999-1362

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Win32k.sys in Windows NT 4.0 before SP2 allows local users to cause a denial of service (crash) by calling certain WIN32K functions with incorrect parameters.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q160/6/01.asp
- http://www.iss.net/security_center/static/7403.php
- http://support.microsoft.com/support/kb/articles/q160/6/01.asp
- http://www.iss.net/security_center/static/7403.php

---

#### 563. CVE-1999-1363

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows NT 3.51 and 4.0 allow local users to cause a denial of service (crash) by running a program that creates a large number of locks on a file, which exhausts the NonPagedPool.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/1/43.asp
- http://www.iss.net/security_center/static/7405.php
- http://support.microsoft.com/support/kb/articles/q163/1/43.asp
- http://www.iss.net/security_center/static/7405.php

---

#### 564. CVE-1999-1364

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows NT 4.0 allows local users to cause a denial of service (crash) via an illegal kernel mode address to the functions (1) GetThreadContext or (2) SetThreadContext.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q142/6/53.asp
- http://www.iss.net/security_center/static/7421.php
- http://support.microsoft.com/support/kb/articles/q142/6/53.asp
- http://www.iss.net/security_center/static/7421.php

---

#### 565. CVE-1999-1452

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
GINA in Windows NT 4.0 allows attackers with physical access to display a portion of the clipboard of the user who has locked the workstation by pasting (CTRL-V) the contents into the username prompt.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=91788829326419&w=2
- http://marc.info/?l=ntbugtraq&m=91764169410814&w=2
- http://marc.info/?l=ntbugtraq&m=91822011021558&w=2
- http://support.microsoft.com/support/kb/articles/q214/8/02.asp
- http://www.securityfocus.com/bid/198

---

#### 566. CVE-1999-1455

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
RSH service utility RSHSVC in Windows NT 3.5 through 4.0 does not properly restrict access as specified in the .Rhosts file when a user comes from an authorized host, which could allow unauthorized users to access the service by logging in from an authorized host.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q158/3/20.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7422
- http://support.microsoft.com/support/kb/articles/q158/3/20.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7422

---

#### 567. CVE-1999-1476

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
A bug in Intel Pentium processor (MMX and Overdrive) allows local users to cause a denial of service (hang) in Intel-based operating systems such as Windows NT and Windows 95, via an invalid instruction, aka the "Invalid Operand with Locked CMPXCHG8B Instruction" problem.

**参考链接 / References**:
- http://support.microsoft.com/support/kb/articles/q163/8/52.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/704
- http://support.microsoft.com/support/kb/articles/q163/8/52.asp
- https://exchange.xforce.ibmcloud.com/vulnerabilities/704

---

#### 568. CVE-1999-1584

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Unknown vulnerability in (1) loadmodule, and (2) modload if modload is installed with setuid/setgid privileges, in SunOS 4.1.1 through 4.1.3c, and Open Windows 3.0, allows local users to gain root privileges via environment variables, a different vulnerability than CVE-1999-1586.

**参考链接 / References**:
- http://sunsolve.sun.com/search/document.do?assetkey=1-22-00124-1
- http://www.cert.org/advisories/CA-1993-18.html
- http://sunsolve.sun.com/search/document.do?assetkey=1-22-00124-1
- http://www.cert.org/advisories/CA-1993-18.html

---

#### 569. CVE-2000-0070

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
NtImpersonateClientOfPort local procedure call in Windows NT 4.0 allows local users to gain privileges, aka "Spoofed LPC Port Request."

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ247869
- http://www.bindview.com/security/advisory/adv_NtImpersonate.html
- http://www.securityfocus.com/bid/934
- http://xforce.iss.net/search.php3?type=2&pattern=nt-spoofed-lpc-port
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-003

---

#### 570. CVE-1999-0595

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
A Windows NT system does not clear the system page file during shutdown, which might allow sensitive information to be recorded.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/216
- https://exchange.xforce.ibmcloud.com/vulnerabilities/216

---

#### 571. CVE-2000-0121

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
The Recycle Bin utility in Windows NT and Windows 2000 allows local users to read or modify files by creating a subdirectory with the victim's SID in the recycler directory, aka the "Recycle Bin Creation" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248399
- http://www.securityfocus.com/bid/963
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-007
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ248399
- http://www.securityfocus.com/bid/963

---

#### 572. CVE-2000-0197

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Windows NT scheduler uses the drive mapping of the interactive user who is currently logged onto the system, which allows the local user to gain privileges by providing a Trojan horse batch file in place of the original batch file.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/current/0202.html
- http://www.securityfocus.com/bid/1050
- http://archives.neohapsis.com/archives/ntbugtraq/current/0202.html
- http://www.securityfocus.com/bid/1050

---

#### 573. CVE-2000-0222

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The installation for Windows 2000 does not activate the Administrator password until the system has rebooted, which allows remote attackers to connect to the ADMIN$ share without a password until the reboot occurs.

**参考链接 / References**:
- http://www.securityfocus.com/bid/990
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000215155750.M4500%40safe.hsc.fr
- http://www.securityfocus.com/bid/990
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=20000215155750.M4500%40safe.hsc.fr

---

#### 574. CVE-2000-0155

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Windows NT Autorun executes the autorun.inf file on non-removable media, which allows local attackers to specify an alternate program to execute when other users access a drive.

**参考链接 / References**:
- http://www.securityfocus.com/bid/993
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=000701bf79cd%24fdb5a620%244c4342a6%40mightye.org
- http://www.securityfocus.com/bid/993
- http://www.securityfocus.com/templates/archive.pike?list=1&date=2000-02-15&msg=000701bf79cd%24fdb5a620%244c4342a6%40mightye.org

---

#### 575. CVE-2000-0211

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Windows Media server allows remote attackers to cause a denial of service via a series of client handshake packets that are sent in an improper sequence, aka the "Misordered Windows Media Services Handshake" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1000
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-013
- http://www.securityfocus.com/bid/1000
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-013

---

#### 576. CVE-2000-0298

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The unattended installation of Windows 2000 with the OEMPreinstall option sets insecure permissions for the All Users and Default Users directories.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0027.html
- http://www.securityfocus.com/bid/1758
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4278
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0027.html
- http://www.securityfocus.com/bid/1758

---

#### 577. CVE-1999-0701

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
After an unattended installation of Windows NT 4.0, an installation file could include sensitive information such as the local Administrator password.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ173039
- http://www.securityfocus.com/bid/626
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-036
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ173039
- http://www.securityfocus.com/bid/626

---

#### 578. CVE-2000-0259

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default permissions for the Cryptography\Offload registry key used by the OffloadModExpo in Windows NT 4.0 allows local users to obtain compromise the cryptographic keys of other users.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1105
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-024
- http://www.securityfocus.com/bid/1105
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-024

---

#### 579. CVE-2000-0311

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The Windows 2000 domain controller allows a malicious user to modify Active Directory information by modifying an unprotected attribute, aka the "Mixed Object Access" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1145
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-026
- http://www.securityfocus.com/bid/1145
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-026

---

#### 580. CVE-2000-0347

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95 and Windows 98 allow a remote attacker to cause a denial of service via a NetBIOS session request packet with a NULL source name.

**参考链接 / References**:
- http://marc.info/?l=ntbugtraq&m=95737580922397&w=2
- http://www.securityfocus.com/bid/1163
- http://marc.info/?l=ntbugtraq&m=95737580922397&w=2
- http://www.securityfocus.com/bid/1163

---

#### 581. CVE-2000-0420

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
The default configuration of SYSKEY in Windows 2000 stores the startup key in the registry, which could allow an attacker tor ecover it and use it to decrypt Encrypted File System (EFS) data.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0112.html
- http://www.securityfocus.com/bid/1198
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0112.html
- http://www.securityfocus.com/bid/1198

---

#### 582. CVE-1999-0980

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT Service Control Manager (SCM) allows remote attackers to cause a denial of service via a malformed argument in a resource enumeration request.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246045
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-055
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ246045
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/1999/ms99-055

---

#### 583. CVE-2000-0305

**严重程度 / Severity**: N/A | CVSS: 7.8

**漏洞描述 / Description**:
Windows 95, Windows 98, Windows 2000, Windows NT 4.0, and Terminal Server systems allow a remote attacker to cause a denial of service by sending a large number of identical fragmented IP packets, aka jolt2 or the "IP Fragment Reassembly" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1236
- http://www.securityfocus.com/templates/advisory.html?id=2240
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-029
- http://www.securityfocus.com/bid/1236
- http://www.securityfocus.com/templates/advisory.html?id=2240

---

#### 584. CVE-2000-0403

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The CIFS Computer Browser service on Windows NT 4.0 allows a remote attacker to cause a denial of service by sending a large number of host announcement requests to the master browse tables, aka the "HostAnnouncement Flooding" or "HostAnnouncement Frame" vulnerability.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=263307
- http://www.securityfocus.com/bid/1261
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-036
- http://www.microsoft.com/technet/support/kb.asp?ID=263307
- http://www.securityfocus.com/bid/1261

---

#### 585. CVE-2000-0505

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Apache 1.3.x HTTP server for Windows platforms allows remote attackers to list directory contents by requesting a URL containing a large number of / characters.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1284
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.BSF.4.20.0006031912360.45740-100000%40alive.znep.com
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4575
- https://lists.apache.org/thread.html/r5419c9ba0951ef73a655362403d12bb8d10fab38274deb3f005816f5%40%3Ccvs.httpd.apache.org%3E
- https://lists.apache.org/thread.html/r5f9c22f9c28adbd9f00556059edc7b03a5d5bb71d4bb80257c0d34e4%40%3Ccvs.httpd.apache.org%3E

---

#### 586. CVE-2000-0487

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
The Protected Store in Windows 2000 does not properly select the strongest encryption when available, which causes it to use a default of 40-bit encryption instead of 56-bit DES encryption, aka the "Protected Store Key Length" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1295
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-032
- http://www.securityfocus.com/bid/1295
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-032

---

#### 587. CVE-2000-0544

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT and Windows 2000 hosts allow a remote attacker to cause a denial of service via malformed DCE/RPC SMBwriteX requests that contain an invalid data length.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0231.html
- http://www.securityfocus.com/bid/1304
- http://archives.neohapsis.com/archives/ntbugtraq/2000-q2/0231.html
- http://www.securityfocus.com/bid/1304

---

#### 588. CVE-2000-0377

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Remote Registry server in Windows NT 4.0 allows local authenticated users to cause a denial of service via a malformed request, which causes the winlogon process to fail, aka the "Remote Registry Access Authentication" vulnerability.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=264684
- http://www.securityfocus.com/bid/1331
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-040
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A1021
- http://www.microsoft.com/technet/support/kb.asp?ID=264684

---

#### 589. CVE-2000-0475

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Windows 2000 allows a local user process to access another user's desktop within the same windows station, aka the "Desktop Separation" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1350
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-020
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4714
- http://www.securityfocus.com/bid/1350
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-020

---

#### 590. CVE-2000-0612

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 95 and Windows 98 do not properly process spoofed ARP packets, which allows remote attackers to overwrite static entries in the cache table.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1406
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=395B7E64.9FB3D4DB%40starzetz.de
- http://www.securityfocus.com/bid/1406
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=395B7E64.9FB3D4DB%40starzetz.de

---

#### 591. CVE-2000-0580

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 2000 Server allows remote attackers to cause a denial of service by sending a continuous stream of binary zeros to various TCP and UDP ports, which significantly increases the CPU utilization.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1415
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161935.4619B-100000%40fjord.fscinternet.com
- http://www.securityfocus.com/bid/1415
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161935.4619B-100000%40fjord.fscinternet.com

---

#### 592. CVE-2000-0581

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 2000 Telnet Server allows remote attackers to cause a denial of service by sending a continuous stream of binary zeros, which causes the server to crash.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1414
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161841.4619A-100000%40fjord.fscinternet.com
- http://www.securityfocus.com/bid/1414
- http://www.securityfocus.com/templates/archive.pike?list=1&msg=Pine.LNX.3.96.1000630161841.4619A-100000%40fjord.fscinternet.com

---

#### 593. CVE-1999-0585

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
A Windows NT administrator account has the default name of Administrator.

**参考链接 / References**:
- https://www.cve.org/CVERecord?id=CVE-1999-0585
- https://www.cve.org/CVERecord?id=CVE-1999-0585

---

#### 594. CVE-2000-0663

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The registry entry for the Windows Shell executable (Explorer.exe) in Windows NT and Windows 2000 uses a relative path name, which allows local users to execute arbitrary commands by inserting a Trojan Horse named Explorer.exe into the %Systemdrive% directory, aka the "Relative Shell Path" vulnerability.

**参考链接 / References**:
- http://www.microsoft.com/technet/support/kb.asp?ID=269049
- http://www.securityfocus.com/bid/1507
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-052
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5040
- http://www.microsoft.com/technet/support/kb.asp?ID=269049

---

#### 595. CVE-2000-0737

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Service Control Manager (SCM) in Windows 2000 creates predictable named pipes, which allows a local user with console access to gain administrator privileges, aka the "Service Control Manager Named Pipe Impersonation" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1535
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-053
- http://www.securityfocus.com/bid/1535
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-053

---

#### 596. CVE-2000-0830

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
annclist.exe in webTV for Windows allows remote attackers to cause a denial of service by via a large, malformed UDP packet to ports 22701 through 22705.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/81852
- http://www.securityfocus.com/bid/1671
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-074
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5216
- http://www.securityfocus.com/archive/1/81852

---

#### 597. CVE-2000-0834

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The Windows 2000 telnet client attempts to perform NTLM authentication by default, which allows remote attackers to capture and replay the NTLM challenge/response via a telnet:// URL that points to the malicious server, aka the "Windows 2000 Telnet Client NTLM Authentication" vulnerability.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a091400-1.txt
- http://www.securityfocus.com/bid/1683
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-067
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5242
- http://www.atstake.com/research/advisories/2000/a091400-1.txt

---

#### 598. CVE-2000-0851

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Buffer overflow in the Still Image Service in Windows 2000 allows local users to gain additional privileges via a long WM_USER message, aka the "Still Image Service Privilege Escalation" vulnerability.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a090700-1.txt
- http://www.securityfocus.com/bid/1651
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-065
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5203
- http://www.atstake.com/research/advisories/2000/a090700-1.txt

---

#### 599. CVE-2000-1003

**严重程度 / Severity**: N/A | CVSS: 2.6

**漏洞描述 / Description**:
NETBIOS client in Windows 95 and Windows 98 allows a remote attacker to cause a denial of service by changing a file sharing service to return an unknown driver type, which causes the client to crash.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/139511
- http://www.securityfocus.com/bid/1794
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5370
- http://www.securityfocus.com/archive/1/139511
- http://www.securityfocus.com/bid/1794

---

#### 600. CVE-2000-1034

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in the System Monitor ActiveX control in Windows 2000 allows remote attackers to execute arbitrary commands via a long LogFileName parameter in HTML source code, aka the "ActiveX Parameter Validation" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97349782305448&w=2
- http://www.securityfocus.com/bid/1899
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-085
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5467
- http://marc.info/?l=bugtraq&m=97349782305448&w=2

---

#### 601. CVE-2000-1060

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The default configuration of XFCE 3.5.1 bypasses the Xauthority access control mechanism with an "xhost + localhost" command in the xinitrc program, which allows local users to sniff X Windows traffic and gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0022.html
- http://www.securityfocus.com/bid/1736
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5305
- http://archives.neohapsis.com/archives/bugtraq/2000-10/0022.html
- http://www.securityfocus.com/bid/1736

---

#### 602. CVE-2000-1071

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The GUI installation for iCal 2.1 Patch 2 disables access control for the X server using an "xhost +" command, which allows remote attackers to monitor X Windows events and gain privileges.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2000/a100900-1.txt
- http://www.osvdb.org/7213
- http://www.securityfocus.com/bid/1767
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5752
- http://www.atstake.com/research/advisories/2000/a100900-1.txt

---

#### 603. CVE-1999-1579

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Cenroll ActiveX control (xenroll.dll) for Terminal Server Editions of Windows NT 4.0 and Windows NT Server 4.0 before SP6 allows remote attackers to cause a denial of service (resource consumption) by creating a large number of arbitrary files on the target machine.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B242366
- http://www.kb.cert.org/vuls/id/3062
- http://www.securityfocus.com/bid/6827
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7107
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3B242366

---

#### 604. CVE-2000-0933

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The Input Method Editor (IME) in the Simplified Chinese version of Windows 2000 does not disable access to privileged functionality that should normally be restricted, which allows local users to gain privileges, aka the "Simplified Chinese IME State Recognition" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1729
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-069
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5301
- http://www.securityfocus.com/bid/1729
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-069

---

#### 605. CVE-2000-0979

**严重程度 / Severity**: N/A | CVSS: 6.4

**漏洞描述 / Description**:
File and Print Sharing service in Windows 95, Windows 98, and Windows Me does not properly check the password for a file share, which allows remote attackers to bypass share access controls by sending a 1-byte password that matches the first character of the real password, aka the "Share Level Password" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=97147777618139&w=2
- http://www.securityfocus.com/bid/1780
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-072
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5395
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A996

---

#### 606. CVE-2000-0991

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Hilgraeve, Inc. HyperTerminal client on Windows 98, ME, and 2000 allows remote attackers to execute arbitrary commands via a long telnet URL, aka the "HyperTerminal Buffer Overflow" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/1815
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-079
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5387
- http://www.securityfocus.com/bid/1815
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-079

---

#### 607. CVE-2000-1227

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT 4.0 and Windows 2000 hosts allow remote attackers to cause a denial of service (unavailable connections) by sending multiple SMB SMBnegprots requests but not reading the response that is sent back.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/63322
- http://www.securityfocus.com/bid/1301
- http://www.securityfocus.com/archive/1/63322
- http://www.securityfocus.com/bid/1301

---

#### 608. CVE-2000-1105

**严重程度 / Severity**: N/A | CVSS: 4.3

**漏洞描述 / Description**:
The ixsso.query ActiveX Object is marked as safe for scripting, which allows malicious web site operators to embed a script that remotely determines the existence of files on visiting Windows 2000 systems that have Indexing Services enabled.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0074.html
- http://www.securityfocus.com/archive/1/144270
- http://www.securityfocus.com/bid/1933
- http://archives.neohapsis.com/archives/win2ksecadvice/2000-q4/0074.html
- http://www.securityfocus.com/archive/1/144270

---

#### 609. CVE-2000-1111

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Telnet Service for Windows 2000 Professional does not properly terminate incomplete connection attempts, which allows remote attackers to cause a denial of service by connecting to the server and not providing any input.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/147914
- http://www.securityfocus.com/bid/2018
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5598
- http://www.securityfocus.com/archive/1/147914
- http://www.securityfocus.com/bid/2018

---

#### 610. CVE-2000-1149

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in RegAPI.DLL used by Windows NT 4.0 Terminal Server allows remote attackers to execute arbitrary commands via a long username, aka the "Terminal Server Login Buffer Overflow" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/143991
- http://www.securityfocus.com/bid/1924
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-087
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5489
- http://www.securityfocus.com/archive/1/143991

---

#### 611. CVE-2001-0006

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
The Winsock2ProtocolCatalogMutex mutex in Windows NT 4.0 has inappropriate Everyone/Full Control permissions, which allows local users to modify the permissions to "No Access" and disable Winsock network connectivity to cause a denial of service, aka the "Winsock Mutex" vulnerability.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98075221915234&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-003
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6006
- http://marc.info/?l=bugtraq&m=98075221915234&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-003

---

#### 612. CVE-2001-0014

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Remote Data Protocol (RDP) in Windows 2000 Terminal Service does not properly handle certain malformed packets, which allows remote attackers to cause a denial of service, aka the "Invalid RDP Data" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2326
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-006
- http://www.securityfocus.com/bid/2326
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-006

---

#### 613. CVE-2001-0083

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows Media Unicast Service in Windows Media Services 4.0 and 4.1 does not properly shut down some types of connections, producing a memory leak that allows remote attackers to cause a denial of service via a series of severed connections, aka the "Severed Windows Media Server Connection" vulnerability.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ281256
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-097
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5785
- http://support.microsoft.com/default.aspx?scid=kb%3B%5BLN%5D%3BQ281256
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-097

---

#### 614. CVE-2001-0045

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
The default permissions for the RAS Administration key in Windows NT 4.0 allows local users to execute arbitrary commands by changing the value to point to a malicious DLL, aka one of the "Registry Permissions" vulnerabilities.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2064
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5671
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A500
- http://www.securityfocus.com/bid/2064

---

#### 615. CVE-2001-0046

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
The default permissions for the SNMP Parameters registry key in Windows NT 4.0 allows remote attackers to read and possibly modify the SNMP community strings to obtain sensitive information or modify network configuration, aka one of the "Registry Permissions" vulnerabilities.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2066
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/ms00-095
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5672
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A139
- http://www.securityfocus.com/bid/2066

---

#### 616. CVE-1999-0718

**严重程度 / Severity**: N/A | CVSS: 6.2

**漏洞描述 / Description**:
IBM GINA, when used for OS/2 domain authentication of Windows NT users, allows local users to gain administrator privileges by changing the GroupMapping registry key.

**参考链接 / References**:
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind9908&L=ntbugtraq&F=&S=&P=5534
- http://www.securityfocus.com/bid/608
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3166
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind9908&L=ntbugtraq&F=&S=&P=5534
- http://www.securityfocus.com/bid/608

---

#### 617. CVE-2022-24517

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24517
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24517

---

#### 618. CVE-2022-24518

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24518
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24518

---

#### 619. CVE-2022-24519

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24519
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24519

---

#### 620. CVE-2022-24520

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24520
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24520

---

#### 621. CVE-2022-22771

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
The Server component of TIBCO Software Inc.'s TIBCO JasperReports Library, TIBCO JasperReports Library for ActiveMatrix BPM, TIBCO JasperReports Server, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for ActiveMatrix BPM, and TIBCO JasperReports Server for Microsoft Azure contains a directory-traversal vulnerability that may theoretically allow web server users to access contents of the host system. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Library: version 7.9.0, TIBCO JasperReports Library for ActiveMatrix BPM: version 7.9.0, TIBCO JasperReports Server: versions 7.9.0 and 7.9.1, TIBCO JasperReports Server for AWS Marketplace: versions 7.9.0 and 7.9.1, TIBCO JasperReports Server for ActiveMatrix BPM: versions 7.9.0 and 7.9.1, and TIBCO JasperReports Server for Microsoft Azure: version 7.9.1.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/03/tibco-security-advisory-march-15-2022-tibco-jasperreports-library-2022-22771
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/03/tibco-security-advisory-march-15-2022-tibco-jasperreports-library-2022-22771

---

#### 622. CVE-2022-26896

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26896
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26896

---

#### 623. CVE-2022-26897

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26897
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26897

---

#### 624. CVE-2022-26898

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26898
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26898

---

#### 625. CVE-2022-26907

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
Azure SDK for .NET Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26907
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26907

---

#### 626. CVE-2022-29556

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
The iot-manager microservice 1.0.0 in Northern.tech Mender Enterprise before 3.2.2 allows SSRF because the Azure IoT Hub integration provides several SSRF primitives that can execute cross-tenant actions via internal API endpoints.

**参考链接 / References**:
- https://mender.io/blog/cve-2022-29555-and-cve-2022-29556-vulnerabilities-in-iot-manager-and-deviceconnect
- https://northern.tech
- https://mender.io/blog/cve-2022-29555-and-cve-2022-29556-vulnerabilities-in-iot-manager-and-deviceconnect
- https://northern.tech

---

#### 627. CVE-2022-22773

**严重程度 / Severity**: HIGH | CVSS: 7.7

**漏洞描述 / Description**:
The REST API component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for ActiveMatrix BPM, and TIBCO JasperReports Server for Microsoft Azure contains difficult to exploit Reflected Cross Site Scripting (XSS) vulnerabilities that allow a low privileged attacker with network access to execute scripts targeting the affected system or the victim's local system. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 8.0.1 and below, TIBCO JasperReports Server - Community Edition: versions 8.0.1 and below, TIBCO JasperReports Server - Developer Edition: versions 8.0.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 8.0.1 and below, TIBCO JasperReports Server for ActiveMatrix BPM: versions 7.9.2 and below, and TIBCO JasperReports Server for Microsoft Azure: versions 8.0.1 and below.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/05/tibco-security-advisory-may-17-2022-tibco-jasperreports-server-cve-2022-22773
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/05/tibco-security-advisory-may-17-2022-tibco-jasperreports-server-cve-2022-22773

---

#### 628. CVE-2022-29223

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Azure RTOS USBX is a USB host, device, and on-the-go (OTG) embedded stack. In versions prior to 6.1.10, an attacker can cause a buffer overflow by providing the Azure RTOS USBX host stack a HUB descriptor with `bNbPorts` set to a value greater than `UX_MAX_TT` which defaults to 8. For a `bNbPorts` value of 255, the implementation of `ux_host_class_hub_descriptor_get` function will modify the contents of `hub` -> `ux_host_class_hub_device` -> `ux_device_hub_tt` array violating the end boundary by 255 - `UX_MAX_TT` items. The USB host stack needs to validate the number of ports reported by the hub, and if the value is larger than UX_MAX_TT, USB stack needs to reject the request. This fix has been included in USBX release 6.1.10.

**参考链接 / References**:
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.10_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-2qc5-385m-x862
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.10_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-2qc5-385m-x862

---

#### 629. CVE-2022-29246

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Azure RTOS USBX is a USB host, device, and on-the-go (OTG) embedded stack. Prior to version 6.1.11, he USBX DFU UPLOAD functionality may be utilized to introduce a buffer overflow resulting in overwrite of memory contents. In particular cases this may allow an attacker to bypass security features or execute arbitrary code. The implementation of `ux_device_class_dfu_control_request` function does not assure that a buffer overflow will not occur during handling of the DFU UPLOAD command. When an attacker issues the `UX_SLAVE_CLASS_DFU_COMMAND_UPLOAD` control transfer request with `wLenght` larger than the buffer size (`UX_SLAVE_REQUEST_CONTROL_MAX_LENGTH`, 256 bytes), depending on the actual implementation of `dfu -> ux_slave_class_dfu_read`, a buffer overflow may occur. In example `ux_slave_class_dfu_read` may read 4096 bytes (or more up to 65k) to a 256 byte buffer ultimately resulting in an overflow. Furthermore in case an attacker has some control over the read flash memory, this may result in execution of arbitrary code and platform compromise. A fix for this issue has been included in USBX release 6.1.11. As a workaround, align request and buffer size to assure that buffer boundaries are respected.

**参考链接 / References**:
- https://github.com/azure-rtos/usbx/blob/master/common/usbx_device_classes/src/ux_device_class_dfu_control_request.c
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.11_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-hh5p-x584-j8hv
- https://github.com/azure-rtos/usbx/blob/master/common/usbx_device_classes/src/ux_device_class_dfu_control_request.c
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.11_rel

---

#### 630. CVE-2022-30177

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30177
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-30177

---

#### 631. CVE-2022-30178

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30178
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-30178

---

#### 632. CVE-2022-30179

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30179
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-30179

---

#### 633. CVE-2022-30180

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30180
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-30180

---

#### 634. CVE-2022-30181

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30181
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30181

---

#### 635. CVE-2022-30187

**严重程度 / Severity**: MEDIUM | CVSS: 4.7

**漏洞描述 / Description**:
Azure Storage Library Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30187
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30187

---

#### 636. CVE-2022-33641

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33641
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33641

---

#### 637. CVE-2022-33642

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33642
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33642

---

#### 638. CVE-2022-33643

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33643
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33643

---

#### 639. CVE-2022-33650

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33650
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33650

---

#### 640. CVE-2022-33651

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33651
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33651

---

#### 641. CVE-2022-33652

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33652
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33652

---

#### 642. CVE-2022-33653

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33653
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33653

---

#### 643. CVE-2022-33654

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33654
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33654

---

#### 644. CVE-2022-33655

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33655
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33655

---

#### 645. CVE-2022-33656

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33656
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33656

---

#### 646. CVE-2022-33657

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33657
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33657

---

#### 647. CVE-2022-33658

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33658
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33658

---

#### 648. CVE-2022-33659

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33659
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33659

---

#### 649. CVE-2022-33660

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33660
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33660

---

#### 650. CVE-2022-33661

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33661
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33661

---

#### 651. CVE-2022-33662

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33662
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33662

---

#### 652. CVE-2022-33663

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33663
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33663

---

#### 653. CVE-2022-33664

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33664
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33664

---

#### 654. CVE-2022-33665

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33665
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33665

---

#### 655. CVE-2022-33666

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33666
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33666

---

#### 656. CVE-2022-33667

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33667
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33667

---

#### 657. CVE-2022-33668

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33668
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33668

---

#### 658. CVE-2022-33669

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33669
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33669

---

#### 659. CVE-2022-33671

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33671
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33671

---

#### 660. CVE-2022-33672

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33672
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33672

---

#### 661. CVE-2022-33673

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33673
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33673

---

#### 662. CVE-2022-33674

**严重程度 / Severity**: HIGH | CVSS: 8.3

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33674
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33674

---

#### 663. CVE-2022-33675

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33675
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33675

---

#### 664. CVE-2022-33676

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33676
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33676

---

#### 665. CVE-2022-33677

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33677
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33677

---

#### 666. CVE-2022-33678

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33678
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33678

---

#### 667. CVE-2022-30175

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30175
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30175

---

#### 668. CVE-2022-30176

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30176
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30176

---

#### 669. CVE-2022-33646

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Azure Batch Node Agent Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33646
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33646

---

#### 670. CVE-2022-34685

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34685
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34685

---

#### 671. CVE-2022-34686

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34686
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34686

---

#### 672. CVE-2022-34687

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34687
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34687

---

#### 673. CVE-2022-35772

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35772
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35772

---

#### 674. CVE-2022-35773

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35773
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35773

---

#### 675. CVE-2022-35774

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35774
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35774

---

#### 676. CVE-2022-35775

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35775
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35775

---

#### 677. CVE-2022-35776

**严重程度 / Severity**: MEDIUM | CVSS: 6.2

**漏洞描述 / Description**:
Azure Site Recovery Denial of Service Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35776
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35776

---

#### 678. CVE-2022-35779

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35779
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35779

---

#### 679. CVE-2022-35780

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35780
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35780

---

#### 680. CVE-2022-35781

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35781
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35781

---

#### 681. CVE-2022-35782

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35782
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35782

---

#### 682. CVE-2022-35783

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35783
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35783

---

#### 683. CVE-2022-35784

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35784
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35784

---

#### 684. CVE-2022-35785

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35785
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35785

---

#### 685. CVE-2022-35786

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35786
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35786

---

#### 686. CVE-2022-35787

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35787
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35787

---

#### 687. CVE-2022-35788

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35788
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35788

---

#### 688. CVE-2022-35789

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35789
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35789

---

#### 689. CVE-2022-35790

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35790
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35790

---

#### 690. CVE-2022-35791

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35791
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35791

---

#### 691. CVE-2022-35799

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35799
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35799

---

#### 692. CVE-2022-35800

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35800
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35800

---

#### 693. CVE-2022-35801

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35801
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35801

---

#### 694. CVE-2022-35802

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35802
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35802

---

#### 695. CVE-2022-35806

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35806
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35806

---

#### 696. CVE-2022-35807

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35807
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35807

---

#### 697. CVE-2022-35808

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35808
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35808

---

#### 698. CVE-2022-35809

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35809
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35809

---

#### 699. CVE-2022-35810

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35810
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35810

---

#### 700. CVE-2022-35811

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35811
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35811

---

#### 701. CVE-2022-35812

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35812
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35812

---

#### 702. CVE-2022-35813

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35813
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35813

---

#### 703. CVE-2022-35814

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35814
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35814

---

#### 704. CVE-2022-35815

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35815
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35815

---

#### 705. CVE-2022-35816

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35816
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35816

---

#### 706. CVE-2022-35817

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35817
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35817

---

#### 707. CVE-2022-35818

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35818
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35818

---

#### 708. CVE-2022-35819

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Site Recovery Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35819
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35819

---

#### 709. CVE-2022-35821

**严重程度 / Severity**: MEDIUM | CVSS: 4.4

**漏洞描述 / Description**:
Azure Sphere Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35821
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35821

---

#### 710. CVE-2022-35824

**严重程度 / Severity**: HIGH | CVSS: 7.2

**漏洞描述 / Description**:
Azure Site Recovery Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35824
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35824

---

#### 711. CVE-2022-22490

**严重程度 / Severity**: MEDIUM | CVSS: 4.9

**漏洞描述 / Description**:
IBM Robotic Process Automation 21.0.0, 21.0.1, and 21.0.2 could allow a privileged user to obtain sensitive Azure bot credential information. IBM X-Force ID: 226342.

**参考链接 / References**:
- https://exchange.xforce.ibmcloud.com/vulnerabilities/226342
- https://www.ibm.com/support/pages/node/6610397
- https://exchange.xforce.ibmcloud.com/vulnerabilities/226342
- https://www.ibm.com/support/pages/node/6610397

---

#### 712. CVE-2021-3590

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
A flaw was found in Foreman project. A credential leak was identified which will expose Azure Compute Profile password through JSON of the API output. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**参考链接 / References**:
- https://access.redhat.com/security/cve/CVE-2021-3590
- https://bugzilla.redhat.com/show_bug.cgi?id=1969258
- https://access.redhat.com/security/cve/CVE-2021-3590
- https://bugzilla.redhat.com/show_bug.cgi?id=1969258

---

#### 713. CVE-2022-38007

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure Guest Configuration and Azure Arc-enabled servers Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38007
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-38007

---

#### 714. CVE-2022-36063

**严重程度 / Severity**: HIGH | CVSS: 7.6

**漏洞描述 / Description**:
Azure RTOS USBx is a USB host, device, and on-the-go (OTG) embedded stack, fully integrated with Azure RTOS ThreadX and available for all Azure RTOS ThreadX–supported processors. Azure RTOS USBX implementation of host support for USB CDC ECM includes an integer underflow and a buffer overflow in the `_ux_host_class_cdc_ecm_mac_address_get` function which may be potentially exploited to achieve remote code execution or denial of service. Setting mac address string descriptor length to a `0` or `1` allows an attacker to introduce an integer underflow followed (string_length) by a buffer overflow of the `cdc_ecm -> ux_host_class_cdc_ecm_node_id` array. This may allow one to redirect the code execution flow or introduce a denial of service. The fix has been included in USBX release [6.1.12](https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel). Improved mac address string descriptor length validation to check for unexpectedly small values may be used as a workaround.

**参考链接 / References**:
- https://github.com/azure-rtos/usbx/blob/master/common/usbx_host_classes/src/ux_host_class_cdc_ecm_mac_address_get.c#L264
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-chpp-5fv9-6368
- https://github.com/azure-rtos/usbx/blob/master/common/usbx_host_classes/src/ux_host_class_cdc_ecm_mac_address_get.c#L264
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel

---

#### 715. CVE-2022-37968

**严重程度 / Severity**: CRITICAL | CVSS: 10.0

**漏洞描述 / Description**:
Microsoft has identified a vulnerability affecting the cluster connect feature of Azure Arc-enabled Kubernetes clusters. This vulnerability could allow an unauthenticated user to elevate their privileges and potentially gain administrative control over the Kubernetes cluster. Additionally, because Azure Stack Edge allows customers to deploy Kubernetes workloads on their devices via Azure Arc, Azure Stack Edge devices are also vulnerable to this vulnerability.

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37968
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-37968

---

#### 716. CVE-2022-39293

**严重程度 / Severity**: HIGH | CVSS: 8.6

**漏洞描述 / Description**:
Azure RTOS USBX is a high-performance USB host, device, and on-the-go (OTG) embedded stack, that is fully integrated with Azure RTOS ThreadX. The case is, in [_ux_host_class_pima_read](https://github.com/azure-rtos/usbx/blob/master/common/usbx_host_classes/src/ux_host_class_pima_read.c), there is data length from device response, returned in the very first packet, and read by [L165 code](https://github.com/azure-rtos/usbx/blob/082fd9db09a3669eca3358f10b8837a5c1635c0b/common/usbx_host_classes/src/ux_host_class_pima_read.c#L165), as header_length. Then in [L178 code](https://github.com/azure-rtos/usbx/blob/082fd9db09a3669eca3358f10b8837a5c1635c0b/common/usbx_host_classes/src/ux_host_class_pima_read.c#L178), there is a “if” branch, which check the expression of “(header_length - UX_HOST_CLASS_PIMA_DATA_HEADER_SIZE) > data_length” where if header_length is smaller than UX_HOST_CLASS_PIMA_DATA_HEADER_SIZE, calculation could overflow and then [L182 code](https://github.com/azure-rtos/usbx/blob/082fd9db09a3669eca3358f10b8837a5c1635c0b/common/usbx_host_classes/src/ux_host_class_pima_read.c#L182) the calculation of data_length is also overflow, this way the later [while loop start from L192](https://github.com/azure-rtos/usbx/blob/082fd9db09a3669eca3358f10b8837a5c1635c0b/common/usbx_host_classes/src/ux_host_class_pima_read.c#L192) can move data_pointer to unexpected address and cause write buffer overflow. The fix has been included in USBX release [6.1.12](https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel). The following can be used as a workaround: Add check of `header_length`: 1. It must be greater than `UX_HOST_CLASS_PIMA_DATA_HEADER_SIZE`. 1. It should be greater or equal to the current returned data length (`transfer_request -> ux_transfer_request_actual_length`).

**参考链接 / References**:
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-gg76-h537-xq48
- https://github.com/azure-rtos/usbx/releases/tag/v6.1.12_rel
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-gg76-h537-xq48

---

#### 717. CVE-2001-0015

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Network Dynamic Data Exchange (DDE) in Windows 2000 allows local users to gain SYSTEM privileges via a "WM_COPYDATA" message to an invisible window that is running with the privileges of the WINLOGON process.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2001/a020501-1.txt
- http://www.securityfocus.com/bid/2341
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-007
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6062
- http://www.atstake.com/research/advisories/2001/a020501-1.txt

---

#### 718. CVE-2001-0017

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in PPTP server in Windows NT 4.0 allows remote attackers to cause a denial of service via a malformed data packet, aka the "Malformed PPTP Packet Stream" vulnerability.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2368
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-009
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6103
- http://www.securityfocus.com/bid/2368
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-009

---

#### 719. CVE-2001-1325

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Internet Explorer 5.0 and 5.5, and Outlook Express 5.0 and 5.5, allow remote attackers to execute scripts when Active Scripting is disabled by including the scripts in XML stylesheets (XSL) that are referenced using an IFRAME tag, possibly due to a vulnerability in Windows Scripting Host (WSH).

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/3AE02004.57FDF958%40guninski.com
- http://www.securityfocus.com/bid/2633
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6448
- http://www.securityfocus.com/archive/1/3AE02004.57FDF958%40guninski.com
- http://www.securityfocus.com/bid/2633

---

#### 720. CVE-2001-0147

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Windows 2000 event viewer snap-in allows attackers to execute arbitrary commands via a malformed field that is improperly handled during the detailed view of event records.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-013
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-013

---

#### 721. CVE-2001-0152

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The password protection option for the Compressed Folders feature in Plus! for Windows 98 and Windows Me writes password information to a file, which allows local users to recover the passwords and read the compressed folders.

**参考链接 / References**:
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-019
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-019

---

#### 722. CVE-2001-0191

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
gnuserv before 3.12, as shipped with XEmacs, does not properly check the specified length of an X Windows MIT-MAGIC-COOKIE cookie, which allows remote attackers to execute arbitrary commands via a buffer overflow, or brute force authentication by using a short cookie length.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0030.html
- http://www.linux-mandrake.com/en/security/2001/MDKSA-2001-019.php3
- http://www.redhat.com/support/errata/RHSA-2001-010.html
- http://www.redhat.com/support/errata/RHSA-2001-011.html
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6056

---

#### 723. CVE-2001-0281

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Format string vulnerability in DbgPrint function, used in debug messages for some Windows NT drivers (possibly when called through DebugMessage), may allow local users to gain privileges.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0379.html
- http://archives.neohapsis.com/archives/bugtraq/2001-02/0379.html

---

#### 724. CVE-2001-1342

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apache before 1.3.20 on Windows and OS/2 systems allows remote attackers to cause a denial of service (GPF) via an HTTP request for a URI that contains a large number of / (slash) or other characters, which causes certain functions to dereference a null pointer.

**参考链接 / References**:
- http://bugs.apache.org/index.cgi/full/7522
- http://marc.info/?l=bugtraq&m=99054258728748&w=2
- http://online.securityfocus.com/archive/1/176144
- http://www.apacheweek.com/issues/01-05-25
- http://www.iss.net/security_center/static/6527.php

---

#### 725. CVE-2001-1347

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Windows 2000 allows local users to cause a denial of service and possibly gain privileges by setting a hardware breakpoint that is handled using global debug registers, which could cause other processes to terminate due to an exception, and allow hijacking of resources such as named pipes.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0232.html
- http://www.iss.net/security_center/static/6590.php
- http://www.securityfocus.com/bid/2764
- http://archives.neohapsis.com/archives/bugtraq/2001-05/0232.html
- http://www.iss.net/security_center/static/6590.php

---

#### 726. CVE-2001-0148

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
The WMP ActiveX Control in Windows Media Player 7 allows remote attackers to execute commands in Internet Explorer via javascript URLs, a variant of the "Frame Domain Verification" vulnerability.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0000.html
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6227
- http://archives.neohapsis.com/archives/bugtraq/2001-01/0000.html
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-015

---

#### 727. CVE-2001-0149

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows Scripting Host in Internet Explorer 5.5 and earlier allows remote attackers to read arbitrary files via the GetObject Javascript function and the htmlfile ActiveX object.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2000-09/0305.html
- http://marc.info/?l=ntbugtraq&m=96999020527583&w=2
- http://www.securityfocus.com/bid/1718
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-015
- https://exchange.xforce.ibmcloud.com/vulnerabilities/5293

---

#### 728. CVE-2001-0265

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
ASCII Armor parser in Windows PGP 7.0.3 and earlier allows attackers to create files in arbitrary locations via a malformed ASCII armored file.

**参考链接 / References**:
- http://www.atstake.com/research/advisories/2001/a040901-1.txt
- http://www.osvdb.org/1782
- http://www.securityfocus.com/bid/2556
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6643
- http://www.atstake.com/research/advisories/2001/a040901-1.txt

---

#### 729. CVE-2001-0373

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
The default configuration of the Dr. Watson program in Windows NT and Windows 2000 generates user.dmp crash dump files with world-readable permissions, which could allow a local user to gain access to sensitive information.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-03/0336.html
- http://www.osvdb.org/5683
- http://www.securityfocus.com/bid/2501
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6275
- http://archives.neohapsis.com/archives/bugtraq/2001-03/0336.html

---

#### 730. CVE-2001-0382

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Computer Associates CCC\Harvest 5.0 for Windows NT/2000 uses weak encryption for passwords, which allows a remote attacker to gain privileges on the application.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/ntbugtraq/2001-q2/0001.html
- http://archives.neohapsis.com/archives/ntbugtraq/2001-q2/0001.html

---

#### 731. CVE-2001-0241

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in Internet Printing ISAPI extension in Windows 2000 allows remote attackers to gain root privileges via a long print request that is passed to the extension through IIS 5.0.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=98874912915948&w=2
- http://www.cert.org/advisories/CA-2001-10.html
- http://www.osvdb.org/3323
- http://www.securityfocus.com/bid/2674
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-023

---

#### 732. CVE-2001-0243

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows Media Player 7 and earlier stores Internet shortcuts in a user's Temporary Files folder with a fixed filename instead of in the Internet Explorer cache, which causes the HTML in those shortcuts to run in the Local Computer Zone instead of the Internet Zone, which allows remote attackers to read certain files.

**参考链接 / References**:
- http://www.securityfocus.com/bid/2765
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-029
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6584
- http://www.securityfocus.com/bid/2765
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-029

---

#### 733. CVE-2001-1238

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Task Manager in Windows 2000 does not allow local users to end processes with uppercase letters named (1) winlogon.exe, (2) csrss.exe, (3) smss.exe and (4) services.exe via the Process tab which could allow local users to install Trojan horses that cannot be stopped with the Task Manager.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/197195
- http://www.securityfocus.com/bid/3033
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6919
- http://www.securityfocus.com/archive/1/197195
- http://www.securityfocus.com/bid/3033

---

#### 734. CVE-2001-0018

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 2000 domain controller in Windows 2000 Server, Advanced Server, or Datacenter Server allows remote attackers to cause a denial of service via a flood of malformed service requests.

**参考链接 / References**:
- http://online.securityfocus.com/archive/82/148411
- http://www.ciac.org/ciac/bulletins/l-049.shtml
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-011
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6136
- http://online.securityfocus.com/archive/82/148411

---

#### 735. CVE-2001-0502

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Running Windows 2000 LDAP Server over SSL, a function does not properly check the permissions of a user request when the directory principal is a domain user and the data attribute is the domain password, which allows local users to modify the login password of other users.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-101.shtml
- http://www.securityfocus.com/bid/2929
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-036
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6745
- http://www.ciac.org/ciac/bulletins/l-101.shtml

---

#### 736. CVE-2001-0513

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Oracle listener process on Windows NT redirects connection requests to another port and creates a separate thread to process the request, which allows remote attackers to cause a denial of service by repeatedly connecting to the Oracle listener but not connecting to the redirected port.

**参考链接 / References**:
- http://www.kb.cert.org/vuls/id/105259
- http://www.osvdb.org/5600
- http://xforce.iss.net/alerts/advise81.php
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6717
- http://www.kb.cert.org/vuls/id/105259

---

#### 737. CVE-2001-1288

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows 2000 and Windows NT allows local users to cause a denial of service (reboot) by executing a command at the command prompt and pressing the F7 and enter keys several times while the command is executing, possibly related to an exception handling error in csrss.exe.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99640583014377&w=2
- http://marc.info/?l=vuln-dev&m=99651044701417&w=2
- http://online.securityfocus.com/archive/1/200118
- http://online.securityfocus.com/archive/1/200985
- http://online.securityfocus.com/archive/1/201151

---

#### 738. CVE-2001-1116

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
Identix BioLogon 2.03 and earlier does not lock secondary displays on a multi-monitor system running Windows 98 or ME, which allows an attacker with physical access to the system to bypass authentication through a secondary display.

**参考链接 / References**:
- http://ntbugtraq.ntadvice.com/default.asp?pid=36&sid=1&A2=IND0108&L=NTBUGTRAQ&F=P&S=&P=71
- http://ntbugtraq.ntadvice.com/default.asp?pid=36&sid=1&A2=ind0108&L=ntbugtraq&F=P&S=&P=724
- http://www.osvdb.org/5453
- http://www.securityfocus.com/bid/3140
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6948

---

#### 739. CVE-2001-1122

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows NT 4.0 SP 6a allows a local user with write access to winnt/system32 to cause a denial of service (crash in lsass.exe) by running the NT4ALL exploit program in 'SPECIAL' mode.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/201722
- http://www.securityfocus.com/bid/3144
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6943
- http://www.securityfocus.com/archive/1/201722
- http://www.securityfocus.com/bid/3144

---

#### 740. CVE-2000-1200

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows NT allows remote attackers to list all users in a domain by obtaining the domain SID with the LsaQueryInformationPolicy policy function via a null session and using the SID to list the users.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/44430
- http://www.securityfocus.com/bid/959
- https://exchange.xforce.ibmcloud.com/vulnerabilities/4015
- http://www.securityfocus.com/archive/1/44430
- http://www.securityfocus.com/bid/959

---

#### 741. CVE-2001-1452

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
By default, DNS servers on Windows NT 4.0 and Windows 2000 Server cache glue records received from non-delegated name servers, which allows remote attackers to poison the DNS cache via spoofed DNS responses.

**参考链接 / References**:
- http://support.microsoft.com/default.aspx?scid=KB%3Ben-us%3Bq241352
- http://www.kb.cert.org/vuls/id/109475
- http://www.securityfocus.com/bid/6791
- https://exchange.xforce.ibmcloud.com/vulnerabilities/3675
- http://support.microsoft.com/default.aspx?scid=KB%3Ben-us%3Bq241352

---

#### 742. CVE-2001-0543

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in NNTP service in Windows NT 4.0 and Windows 2000 allows remote attackers to cause a denial of service (memory exhaustion) via a large number of malformed posts.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3183
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-043
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6977
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A334
- http://www.securityfocus.com/bid/3183

---

#### 743. CVE-2001-0659

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Buffer overflow in IrDA driver providing infrared data exchange on Windows 2000 allows attackers who are physically close to the machine to cause a denial of service (reboot) via a malformed IrDA packet.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/209385
- http://www.securityfocus.com/bid/3215
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-046
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7008
- http://online.securityfocus.com/archive/1/209385

---

#### 744. CVE-2001-0675

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Rit Research Labs The Bat! 1.51 for Windows allows a remote attacker to cause a denial of service by sending an email to a user's account containing a carriage return <CR> that is not followed by a line feed <LF>.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0345.html
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0381.html
- http://archives.neohapsis.com/archives/bugtraq/2001-04/0410.html
- http://www.securityfocus.com/bid/2636
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6423

---

#### 745. CVE-2001-0678

**严重程度 / Severity**: N/A | CVSS: 4.6

**漏洞描述 / Description**:
A buffer overflow in reggo.dll file used by Trend Micro InterScan VirusWall prior to 3.51 build 1349 for Windows NT 3.5 and InterScan WebManager 1.2 allows a local attacker to execute arbitrary code.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/185383
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6575
- http://www.securityfocus.com/archive/1/185383
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6575

---

#### 746. CVE-2001-0687

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Broker FTP server 5.9.5 for Windows NT and 9x allows a remote attacker to retrieve privileged web server system information by (1) issuing a CD command (CD C:) followed by the LS command, (2) specifying arbitrary paths in the UNC format (\\computername\sharename).

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/190032
- http://www.securityfocus.com/bid/2853
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6674
- http://www.securityfocus.com/archive/1/190032
- http://www.securityfocus.com/bid/2853

---

#### 747. CVE-2001-0791

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Trend Micro InterScan VirusWall for Windows NT allows remote attackers to make configuration changes by directly calling certain CGI programs, which do not restrict access.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00006.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00006.html

---

#### 748. CVE-2001-0540

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Memory leak in Terminal servers in Windows NT and Windows 2000 allows remote attackers to cause a denial of service (memory exhaustion) via a large number of malformed Remote Desktop Protocol (RDP) requests to port 3389.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3099
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-040
- https://exchange.xforce.ibmcloud.com/vulnerabilities/6912
- http://www.securityfocus.com/bid/3099
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-040

---

#### 749. CVE-2001-0662

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
RPC endpoint mapper in Windows NT 4.0 allows remote attackers to cause a denial of service (loss of RPC services) via a malformed request.

**参考链接 / References**:
- http://www.ciac.org/ciac/bulletins/l-142.shtml
- http://www.securityfocus.com/bid/3313
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-048
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7105
- http://www.ciac.org/ciac/bulletins/l-142.shtml

---

#### 750. CVE-2001-0669

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Various Intrusion Detection Systems (IDS) including (1) Cisco Secure Intrusion Detection System, (2) Cisco Catalyst 6000 Intrusion Detection System Module, (3) Dragon Sensor 4.x, (4) Snort before 1.8.1, (5) ISS RealSecure Network Sensor 5.x and 6.x before XPU 3.2, and (6) ISS RealSecure Server Sensor 5.5 and 6.0 for Windows, allow remote attackers to evade detection of HTTP attacks via non-standard "%u" Unicode encoding of ASCII characters in the requested URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=99972950200602&w=2
- http://www.cisco.com/warp/public/707/cisco-intrusion-detection-obfuscation-vuln-pub.shtml
- http://www.kb.cert.org/vuls/id/548515
- http://www.securityfocus.com/bid/3292
- http://xforce.iss.net/alerts/advise95.php

---

#### 751. CVE-2001-0729

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Apache 1.3.20 on Windows servers allows remote attackers to bypass the default index page and list directory contents via a URL with a large number of / (slash) characters.

**参考链接 / References**:
- http://secunia.com/advisories/23794
- http://securitytracker.com/id?1017522
- http://www.apacheweek.com/issues/01-09-28#security
- http://www.oracle.com/technetwork/topics/security/cpujan2007-101493.html
- http://www.securityfocus.com/bid/22083

---

#### 752. CVE-2001-0919

**严重程度 / Severity**: N/A | CVSS: 5.1

**漏洞描述 / Description**:
Internet Explorer 5.50.4134.0100 on Windows ME with "Prompt to allow cookies to be stored on your machine" enabled does not warn a user when a cookie is set using Javascript.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100679857614967&w=2
- http://marc.info/?l=bugtraq&m=100679857614967&w=2

---

#### 753. CVE-2001-0663

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Terminal Server in Windows NT and Windows 2000 allows remote attackers to cause a denial of service via a sequence of invalid Remote Desktop Protocol (RDP) packets.

**参考链接 / References**:
- http://www.securityfocus.com/bid/3445
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-052
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7302
- http://www.securityfocus.com/bid/3445
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-052

---

#### 754. CVE-2001-0721

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Universal Plug and Play (UPnP) in Windows 98, 98SE, ME, and XP allows remote attackers to cause a denial of service (memory consumption or crash) via a malformed UPnP request.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100467787323377&w=2
- http://marc.info/?l=bugtraq&m=100528449024158&w=2
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-054
- http://marc.info/?l=bugtraq&m=100467787323377&w=2
- http://marc.info/?l=bugtraq&m=100528449024158&w=2

---

#### 755. CVE-2001-0860

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Terminal Services Manager MMC in Windows 2000 and XP trusts the Client Address (IP address) that is provided by the client instead of obtaining it from the packet headers, which allows clients to spoof their public IP address, e.g. through a Network Address Translation (NAT).

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100578220002083&w=2
- http://www.securityfocus.com/bid/3541
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7538
- http://marc.info/?l=bugtraq&m=100578220002083&w=2
- http://www.securityfocus.com/bid/3541

---

#### 756. CVE-2001-0951

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows 2000 allows remote attackers to cause a denial of service (CPU consumption) by flooding Internet Key Exchange (IKE) UDP port 500 with packets that contain a large number of dot characters.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100774842520403&w=2
- http://marc.info/?l=bugtraq&m=100813081913496&w=2
- http://www.securityfocus.com/bid/3652
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7667
- http://marc.info/?l=bugtraq&m=100774842520403&w=2

---

#### 757. CVE-2001-1192

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Citrix Independent Computing Architecture (ICA) Client for Windows 6.1 allows remote malicious web sites to execute arbitrary code via a .ICA file, which is downloaded and automatically executed by the client.

**参考链接 / References**:
- http://www.securityfocus.com/archive/1/245342
- http://www.securityfocus.com/cgi-bin/vulns-item.pl?section=info&id=3688
- https://exchange.xforce.ibmcloud.com/vulnerabilities/7697
- http://www.securityfocus.com/archive/1/245342
- http://www.securityfocus.com/cgi-bin/vulns-item.pl?section=info&id=3688

---

#### 758. CVE-2001-0876

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in Universal Plug and Play (UPnP) on Windows 98, 98SE, ME, and XP allows remote attackers to execute arbitrary code via a NOTIFY directive with a long Location URL.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100887440810532&w=2
- http://marc.info/?l=ntbugtraq&m=100887271006313&w=2
- http://www.cert.org/advisories/CA-2001-37.html
- http://www.ciac.org/ciac/bulletins/m-030.shtml
- http://www.kb.cert.org/vuls/id/951555

---

#### 759. CVE-2001-0877

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Universal Plug and Play (UPnP) on Windows 98, 98SE, ME, and XP allows remote attackers to cause a denial of service via (1) a spoofed SSDP advertisement that causes the client to connect to a service on another machine that generates a large amount of traffic (e.g., chargen), or (2) via a spoofed SSDP announcement to broadcast or multicast addresses, which could cause all UPnP clients to send traffic to a single target system.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=100887440810532&w=2
- http://marc.info/?l=ntbugtraq&m=100887271006313&w=2
- http://www.cert.org/advisories/CA-2001-37.html
- http://www.ciac.org/ciac/bulletins/m-030.shtml
- http://www.kb.cert.org/vuls/id/411059

---

#### 760. CVE-2001-1515

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Macintosh clients, when using NT file system volumes on Windows 2000 SP1, create subdirectories and automatically modify the inherited NTFS permissions, which may cause the directories to have less restrictive permissions than intended.

**参考链接 / References**:
- http://securitytracker.com/id?1002626
- http://www.securityfocus.com/bid/3479
- http://securitytracker.com/id?1002626
- http://www.securityfocus.com/bid/3479

---

#### 761. CVE-2001-1517

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
RunAs (runas.exe) in Windows 2000 stores cleartext authentication information in memory, which could allow attackers to obtain usernames and passwords by executing a process that is allocated the same memory page after termination of a RunAs command.  NOTE: the vendor disputes this issue, saying that administrative privileges are already required to exploit it, and the original researcher did not respond to requests for additional information

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2001-q4/0041.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00100.html
- http://www.iss.net/security_center/static/7531.php
- http://www.securityfocus.com/bid/3184
- http://archives.neohapsis.com/archives/vulnwatch/2001-q4/0041.html

---

#### 762. CVE-2001-1518

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
RunAs (runas.exe) in Windows 2000 only creates one session instance at a time, which allows local users to cause a denial of service (RunAs hang) by creating a named pipe session with the authentication server without any request for service.  NOTE: the vendor disputes this vulnerability, however the vendor also presents a scenario in which other users could be affected if running on a Terminal Server. Therefore this is a vulnerability.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00100.html
- http://online.securityfocus.com/archive/1/236113
- http://www.iss.net/security_center/static/7533.php
- http://www.securityfocus.com/bid/3291
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/11/msg00100.html

---

#### 763. CVE-2001-1519

**严重程度 / Severity**: N/A | CVSS: 3.6

**漏洞描述 / Description**:
RunAs (runas.exe) in Windows 2000 allows local users to create a spoofed named pipe when the service is stopped, then capture cleartext usernames and passwords when clients connect to the service.  NOTE: the vendor disputes this issue, saying that administrative privileges are already required to exploit it

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/236111
- http://online.securityfocus.com/archive/1/240136
- http://www.iss.net/security_center/static/7532.php
- http://www.securityfocus.com/bid/3185
- http://online.securityfocus.com/archive/1/236111

---

#### 764. CVE-2001-1552

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ssdpsrv.exe in Windows ME allows remote attackers to cause a denial of service by sending multiple newlines in a Simple Service Discovery Protocol (SSDP) message.  NOTE: multiple replies to the original post state that the problem could not be reproduced.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0133.html
- http://www.iss.net/security_center/static/7318.php
- http://www.securityfocus.com/bid/3442
- http://archives.neohapsis.com/archives/bugtraq/2001-10/0133.html
- http://www.iss.net/security_center/static/7318.php

---

#### 765. CVE-2001-1560

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Win32k.sys (aka Graphics Device Interface (GDI)) in Windows 2000 and XP allows local users to cause a denial of service (system crash) by calling the ShowWindow function after receiving a WM_NCCREATE message.

**参考链接 / References**:
- http://www.derkeiler.com/Mailing-Lists/NT-Bugtraq/2001-10/0066.html
- http://www.iss.net/security_center/static/7409.php
- http://www.securityfocus.com/bid/3481
- http://www.derkeiler.com/Mailing-Lists/NT-Bugtraq/2001-10/0066.html
- http://www.iss.net/security_center/static/7409.php

---

#### 766. CVE-2001-1570

**严重程度 / Severity**: N/A | CVSS: 2.1

**漏洞描述 / Description**:
Windows XP with fast user switching and account lockout enabled allows local users to deny user account access by setting the fast user switch to the same user (self) multiple times, which causes other accounts to be locked out.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-12/0213.html
- http://www.iss.net/security_center/static/7731.php
- http://www.securityfocus.com/bid/3717
- http://archives.neohapsis.com/archives/bugtraq/2001-12/0213.html
- http://www.iss.net/security_center/static/7731.php

---

#### 767. CVE-2001-1571

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The Remote Desktop client in Windows XP sends the most recent user account name in cleartext, which could allow remote attackers to obtain terminal server user account names via sniffing.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/bugtraq/2001-12/0213.html
- http://www.iss.net/security_center/static/7732.php
- http://www.securityfocus.com/bid/3720
- http://archives.neohapsis.com/archives/bugtraq/2001-12/0213.html
- http://www.iss.net/security_center/static/7732.php

---

#### 768. CVE-2001-1573

**严重程度 / Severity**: N/A | CVSS: 10.0

**漏洞描述 / Description**:
Buffer overflow in smtpscan.dll for Trend Micro InterScan VirusWall 3.51 for Windows NT has allows remote attackers to execute arbitrary code via a certain configuration parameter.

**参考链接 / References**:
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00407.html
- http://cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00407.html

---

#### 769. CVE-2002-0020

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in telnet server in Windows 2000 and Interix 2.2 allows remote attackers to execute arbitrary code via malformed protocol options.

**参考链接 / References**:
- http://www.iss.net/security_center/static/8094.php
- http://www.securityfocus.com/bid/4061
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-004
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A424
- http://www.iss.net/security_center/static/8094.php

---

#### 770. CVE-2002-0053

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Buffer overflow in SNMP agent service in Windows 95/98/98SE, Windows NT 4.0, Windows 2000, and Windows XP allows remote attackers to cause a denial of service or execute arbitrary code via a malformed management request.  NOTE: this candidate may be split or merged with other candidates.  This and other PROTOS-related candidates, especially CVE-2002-0012 and CVE-2002-0013, will be updated when more accurate information is available.

**参考链接 / References**:
- http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0012
- http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0013
- http://www.cert.org/advisories/CA-2002-03.html
- http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/snmpv1/index.html
- http://www.kb.cert.org/vuls/id/107186

---

#### 771. CVE-2002-0070

**严重程度 / Severity**: N/A | CVSS: 7.6

**漏洞描述 / Description**:
Buffer overflow in Windows Shell (used as the Windows Desktop) allows local and possibly remote attackers to execute arbitrary code via a custom URL handler that has not been removed for an application that has been improperly uninstalled.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101594127017290&w=2
- http://www.iss.net/security_center/static/8384.php
- http://www.ntbugtraq.com/default.asp?pid=36&sid=1&A2=ind0203&L=ntbugtraq&F=P&S=&P=2404
- http://www.securityfocus.com/bid/4248
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-014

---

#### 772. CVE-2002-0142

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
CGI handler in John Roy Pi3Web for Windows 2.0 beta 1 and 2 allows remote attackers to cause a denial of service (crash) via a series of requests whose physical path is exactly 260 characters long and ends in a series of . (dot) characters.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101164598828093&w=2
- http://marc.info/?l=ntbugtraq&m=101102275316307&w=2
- http://online.securityfocus.com/archive/1/250126
- http://sourceforge.net/tracker/index.php?func=detail&aid=505583&group_id=17753&atid=317753
- http://www.iss.net/security_center/static/7880.php

---

#### 773. CVE-2002-0051

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Windows 2000 allows local users to prevent the application of new group policy settings by opening Group Policy files with exclusive-read access.

**参考链接 / References**:
- http://online.securityfocus.com/archive/1/244329
- http://www.securityfocus.com/bid/4438
- https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-016
- https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A38
- http://online.securityfocus.com/archive/1/244329

---

#### 774. CVE-2002-0065

**严重程度 / Severity**: N/A | CVSS: 7.2

**漏洞描述 / Description**:
Funk Software Proxy Host 3.x uses weak encryption for the Proxy Host password, which allows local users to gain privileges by recovering the passwords from the PHOST.INI file or the Windows registry.

**参考链接 / References**:
- http://razor.bindview.com/publish/advisories/adv_FunkProxy.html
- http://www.iss.net/security_center/static/8792.php
- http://www.securityfocus.com/bid/4459
- http://razor.bindview.com/publish/advisories/adv_FunkProxy.html
- http://www.iss.net/security_center/static/8792.php

---

#### 775. CVE-2002-0159

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Format string vulnerability in the administration function in Cisco Secure Access Control Server (ACS) for Windows, 2.6.x and earlier and 3.x through 3.01 (build 40), allows remote attackers to crash the CSADMIN  module only (denial of service of administration function) or execute arbitrary code via format strings in the URL to port 2002.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101787248913611&w=2
- http://www.cisco.com/warp/public/707/ACS-Win-Web.shtml
- http://www.iss.net/security_center/static/8742.php
- http://www.osvdb.org/2062
- http://www.securityfocus.com/bid/4416

---

#### 776. CVE-2002-0160

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
The administration function in Cisco Secure Access Control Server (ACS) for Windows, 2.6.x and earlier and 3.x through 3.01 (build 40), allows remote attackers to read HTML, Java class, and image files outside the web root via a ..\.. (modified ..) in the URL to port 2002.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101786689128667&w=2
- http://www.cisco.com/warp/public/707/ACS-Win-Web.shtml
- http://www.osvdb.org/5352
- http://marc.info/?l=bugtraq&m=101786689128667&w=2
- http://www.cisco.com/warp/public/707/ACS-Win-Web.shtml

---

#### 777. CVE-2002-0200

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Cyberstop Web Server for Windows 0.1 allows remote attackers to cause a denial of service via an HTTP request for an MS-DOS device name.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101174569103289&w=2
- http://www.iss.net/security_center/static/7959.php
- http://www.securityfocus.com/bid/3929
- http://marc.info/?l=bugtraq&m=101174569103289&w=2
- http://www.iss.net/security_center/static/7959.php

---

#### 778. CVE-2002-0201

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Cyberstop Web Server for Windows 0.1 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request, possibly triggering a buffer overflow.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101174569103289&w=2
- http://www.iss.net/security_center/static/7960.php
- http://www.securityfocus.com/bid/3930
- http://marc.info/?l=bugtraq&m=101174569103289&w=2
- http://www.iss.net/security_center/static/7960.php

---

#### 779. CVE-2002-0249

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
PHP for Windows, when installed on Apache 2.0.28 beta as a standalone CGI module, allows remote attackers to obtain the physical path of the php.exe via a request with malformed arguments such as /123, which leaks the pathname in the error message.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101311698909691&w=2
- http://www.iss.net/security_center/static/8121.php
- http://www.securityfocus.com/bid/4056
- http://marc.info/?l=bugtraq&m=101311698909691&w=2
- http://www.iss.net/security_center/static/8121.php

---

#### 780. CVE-2002-0283

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
Windows XP with port 445 open allows remote attackers to cause a denial of service (CPU consumption) via a flood of TCP SYN packets containing possibly malformed data.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101408718030099&w=2
- http://marc.info/?l=bugtraq&m=101408718030099&w=2

---

#### 781. CVE-2002-0285

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Outlook Express 5.5 and 6.0 on Windows treats a carriage return ("CR") in a message header as if it were a valid carriage return/line feed combination (CR/LF), which could allow remote attackers to bypass virus protection and or other filtering mechanisms via a mail message with headers that only contain the CR, which causes Outlook to create separate headers.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101362077701164&w=2
- http://www.iss.net/security_center/static/8198.php
- http://www.securityfocus.com/bid/4092
- http://marc.info/?l=bugtraq&m=101362077701164&w=2
- http://www.iss.net/security_center/static/8198.php

---

#### 782. CVE-2002-0576

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
ColdFusion 5.0 and earlier on Windows systems allows remote attackers to determine the absolute pathname of .cfm or .dbm files via an HTTP request that contains an MS-DOS device name such as NUL, which leaks the pathname in an error message.

**参考链接 / References**:
- http://archives.neohapsis.com/archives/vulnwatch/2002-q2/0028.html
- http://online.securityfocus.com/archive/1/268263
- http://www.iss.net/security_center/static/8866.php
- http://www.macromedia.com/v1/handlers/index.cfm?ID=22906
- http://www.osvdb.org/3337

---

#### 783. CVE-2002-0314

**严重程度 / Severity**: N/A | CVSS: 5.0

**漏洞描述 / Description**:
fasttrack p2p, as used in (1) KaZaA before 1.5, (2) grokster, and (3) morpheus allows remote attackers to cause a denial of service (memory exhaustion) via a series of client-to-client messages, which pops up new windows per message.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101441689224760&w=2
- http://www.iss.net/security_center/static/8273.php
- http://www.securityfocus.com/bid/4122
- http://marc.info/?l=bugtraq&m=101441689224760&w=2
- http://www.iss.net/security_center/static/8273.php

---

#### 784. CVE-2002-0340

**严重程度 / Severity**: N/A | CVSS: 7.5

**漏洞描述 / Description**:
Windows Media Player (WMP) 8.00.00.4477, and possibly other versions, automatically detects and executes .wmf and other content, even when the file's extension or content type does not specify .wmf, which could make it easier for attackers to conduct unauthorized activities via Trojan horse files containing .wmf content.

**参考链接 / References**:
- http://marc.info/?l=bugtraq&m=101447771102582&w=2
- http://marc.info/?l=bugtraq&m=101447771102582&w=2

---

#### 785. CVE-2022-39327

**严重程度 / Severity**: HIGH | CVSS: 8.1

**漏洞描述 / Description**:
Azure CLI is the command-line interface for Microsoft Azure. In versions previous to 2.40.0, Azure CLI contains a vulnerability for potential code injection. Critical scenarios are where a hosting machine runs an Azure CLI command where parameter values have been provided by an external source. The vulnerability is only applicable when the Azure CLI command is run on a Windows machine and with any version of PowerShell and when the parameter value contains the `&` or `|` symbols. If any of these prerequisites are not met, this vulnerability is not applicable. Users should upgrade to version 2.40.0 or greater to receive a a mitigation for the vulnerability.

**参考链接 / References**:
- https://github.com/Azure/azure-cli/pull/23514
- https://github.com/Azure/azure-cli/pull/24015
- https://github.com/Azure/azure-cli/security/advisories/GHSA-47xc-9rr2-q7p4
- https://github.com/Azure/azure-cli/pull/23514
- https://github.com/Azure/azure-cli/pull/24015

---

#### 786. CVE-2022-39344

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
Azure RTOS USBX is a USB host, device, and on-the-go (OTG) embedded stack, that is fully integrated with Azure RTOS ThreadX. Prior to version 6.1.12, the USB DFU UPLOAD functionality may be utilized to introduce a buffer overflow resulting in overwrite of memory contents. In particular cases this may allow an attacker to bypass security features or execute arbitrary code. The implementation of `ux_device_class_dfu_control_request` function prevents buffer overflow during handling of DFU UPLOAD command when current state is `UX_SYSTEM_DFU_STATE_DFU_IDLE`. This issue has been patched, please upgrade to version 6.1.12. As a workaround, add the `UPLOAD_LENGTH` check in all possible states.

**参考链接 / References**:
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-m9p8-xrp7-vvqp
- https://github.com/azure-rtos/usbx/security/advisories/GHSA-m9p8-xrp7-vvqp

---

#### 787. CVE-2022-39343

**严重程度 / Severity**: MEDIUM | CVSS: 5.6

**漏洞描述 / Description**:
Azure RTOS FileX is a FAT-compatible file system that’s fully integrated with Azure RTOS ThreadX. In versions before 6.2.0, the Fault Tolerant feature of Azure RTOS FileX includes integer under and overflows which may be exploited to achieve buffer overflow and modify memory contents. When a valid log file with correct ID and checksum is detected by the `_fx_fault_tolerant_enable` function an attempt to recover the previous failed write operation is taken by call of `_fx_fault_tolerant_apply_logs`. This function iterates through the log entries and performs required recovery operations. When properly crafted a log including entries of type `FX_FAULT_TOLERANT_DIR_LOG_TYPE` may be utilized to introduce unexpected behavior. This issue has been patched in version 6.2.0. A workaround to fix line 218 in fx_fault_tolerant_apply_logs.c is documented in the GHSA.

**参考链接 / References**:
- https://github.com/azure-rtos/filex/blob/master/common/src/fx_fault_tolerant_apply_logs.c#L218
- https://github.com/azure-rtos/filex/security/advisories/GHSA-8jqf-wjhq-4w9f
- https://github.com/azure-rtos/filex/blob/master/common/src/fx_fault_tolerant_apply_logs.c#L218
- https://github.com/azure-rtos/filex/security/advisories/GHSA-8jqf-wjhq-4w9f

---

#### 788. CVE-2022-41051

**严重程度 / Severity**: HIGH | CVSS: 7.8

**漏洞描述 / Description**:
Azure RTOS GUIX Studio Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41051
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41051

---

#### 789. CVE-2022-41085

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Azure CycleCloud Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41085
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41085

---

#### 790. CVE-2022-45306

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
Insecure permissions in Chocolatey Azure-Pipelines-Agent package v2.211.1 and below grants all users in the Authenticated Users group write privileges for the subfolder C:\agent and all files located in that folder.

**参考链接 / References**:
- https://github.com/ycdxsb/Vuln/blob/main/azure-pipelines-agent-weak-permission-vuln/azure-pipelines-agent-weak-permission-vuln.md
- https://github.com/ycdxsb/Vuln/blob/main/azure-pipelines-agent-weak-permission-vuln/azure-pipelines-agent-weak-permission-vuln.md

---

#### 791. CVE-2022-3641

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Elevation of privilege in the Azure SQL Data Source in Devolutions Remote Desktop Manager 2022.3.13 to 2022.3.24 allows an authenticated user to spoof a privileged account.

**参考链接 / References**:
- https://devolutions.net/security/advisories/DEVO-2022-0010
- https://devolutions.net/security/advisories/DEVO-2022-0010

---

#### 792. CVE-2022-41561

**严重程度 / Severity**: CRITICAL | CVSS: 9.1

**漏洞描述 / Description**:
The JNDI Data Sources component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for Microsoft Azure, and TIBCO JasperReports Server for Microsoft Azure contains an easily exploitable vulnerability that allows a privileged/administrative attacker with network access to execute Remote Code Execution to obtain a reverse shell on the affected system. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 8.0.2 and below, TIBCO JasperReports Server: version 8.1.0, TIBCO JasperReports Server - Community Edition: versions 8.1.0 and below, TIBCO JasperReports Server - Developer Edition: versions 8.1.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 8.0.2 and below, TIBCO JasperReports Server for AWS Marketplace: version 8.1.0, TIBCO JasperReports Server for Microsoft Azure: versions 8.0.2 and below, and TIBCO JasperReports Server for Microsoft Azure: version 8.1.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41561
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41561

---

#### 793. CVE-2022-41562

**严重程度 / Severity**: HIGH | CVSS: 8.4

**漏洞描述 / Description**:
The HTML escaping component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Community Edition, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for Microsoft Azure, and TIBCO JasperReports Server for Microsoft Azure contains an easily exploitable vulnerability that allows a privileged/administrative attacker with network access to execute an XSS attack on the affected system. A successful attack using this vulnerability requires human interaction from a person other than the attacker. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 8.0.2 and below, TIBCO JasperReports Server: version 8.1.0, TIBCO JasperReports Server - Community Edition: versions 8.1.0 and below, TIBCO JasperReports Server - Developer Edition: versions 8.1.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 8.0.2 and below, TIBCO JasperReports Server for AWS Marketplace: version 8.1.0, TIBCO JasperReports Server for Microsoft Azure: versions 8.0.2 and below, and TIBCO JasperReports Server for Microsoft Azure: version 8.1.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41562
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41562

---

#### 794. CVE-2022-41563

**严重程度 / Severity**: CRITICAL | CVSS: 9.0

**漏洞描述 / Description**:
The Dashboard component of TIBCO Software Inc.'s TIBCO JasperReports Server, TIBCO JasperReports Server, TIBCO JasperReports Server - Developer Edition, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for AWS Marketplace, TIBCO JasperReports Server for Microsoft Azure, and TIBCO JasperReports Server for Microsoft Azure contains an easily exploitable vulnerability that allows a low privileged attacker with network access to execute Stored Cross Site Scripting (XSS) on the affected system. A successful attack using this vulnerability requires human interaction from a person other than the attacker. Affected releases are TIBCO Software Inc.'s TIBCO JasperReports Server: versions 8.0.2 and below, TIBCO JasperReports Server: version 8.1.0, TIBCO JasperReports Server - Developer Edition: versions 8.1.0 and below, TIBCO JasperReports Server for AWS Marketplace: versions 8.0.2 and below, TIBCO JasperReports Server for AWS Marketplace: version 8.1.0, TIBCO JasperReports Server for Microsoft Azure: versions 8.0.2 and below, and TIBCO JasperReports Server for Microsoft Azure: version 8.1.0.

**参考链接 / References**:
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41563
- https://www.tibco.com/services/support/advisories
- https://www.tibco.com/support/advisories/2022/12/tibco-security-advisory-december-13-2022-tibco-jasperreports-server-cve-2022-41563

---

#### 795. CVE-2022-44699

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Azure Network Watcher Agent Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44699
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44699

---

#### 796. CVE-2022-23551

**严重程度 / Severity**: MEDIUM | CVSS: 5.3

**漏洞描述 / Description**:
aad-pod-identity assigns Azure Active Directory identities to Kubernetes applications and has now been deprecated as of 24 October 2022. The NMI component in AAD Pod Identity intercepts and validates token requests based on regex. In this case, a token request made with backslash in the request (example: `/metadata/identity\oauth2\token/`) would bypass the NMI validation and be sent to IMDS allowing a pod in the cluster to access identities that it shouldn't have access to. This issue has been fixed and has been included in AAD Pod Identity release version 1.8.13. If using the AKS pod-managed identities add-on, no action is required. The clusters should now be running the version 1.8.13 release.

**参考链接 / References**:
- https://github.com/Azure/aad-pod-identity/commit/7e01970391bde6c360d077066ca17d059204cb5d
- https://github.com/Azure/aad-pod-identity/releases/tag/v1.8.13
- https://github.com/Azure/aad-pod-identity/security/advisories/GHSA-p82q-rxpm-hjpc
- https://github.com/Azure/aad-pod-identity/commit/7e01970391bde6c360d077066ca17d059204cb5d
- https://github.com/Azure/aad-pod-identity/releases/tag/v1.8.13

---

#### 797. CVE-2023-21531

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Azure Service Fabric Container Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21531
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21531

---

#### 798. CVE-2023-24426

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Jenkins Azure AD Plugin 303.va_91ef20ee49f and earlier does not invalidate the previous session on login.

**参考链接 / References**:
- https://www.jenkins.io/security/advisory/2023-01-24/#SECURITY-2980
- https://www.jenkins.io/security/advisory/2023-01-24/#SECURITY-2980

---

#### 799. CVE-2023-21564

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
Azure DevOps Server Cross-Site Scripting Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21564
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21564

---

#### 800. CVE-2023-21703

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Data Box Gateway Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21703
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21703

---

#### 801. CVE-2023-21777

**严重程度 / Severity**: HIGH | CVSS: 8.7

**漏洞描述 / Description**:
Azure App Service on Azure Stack Hub Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21777
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21777

---

#### 802. CVE-2023-23382

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Machine Learning Compute Instance Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23382
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23382

---

#### 803. CVE-2023-21553

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Azure DevOps Server Remote Code Execution Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21553
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21553

---

#### 804. CVE-2023-25766

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
A missing permission check in Jenkins Azure Credentials Plugin 253.v887e0f9e898b and earlier allows attackers with Overall/Read permission to enumerate credentials IDs of credentials stored in Jenkins.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1757
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1757

---

#### 805. CVE-2023-25767

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
A cross-site request forgery (CSRF) vulnerability in Jenkins Azure Credentials Plugin 253.v887e0f9e898b and earlier allows attackers to connect to an attacker-specified web server.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1756
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1756

---

#### 806. CVE-2023-25768

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
A missing permission check in Jenkins Azure Credentials Plugin 253.v887e0f9e898b and earlier allows attackers with Overall/Read permission to connect to an attacker-specified web server.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1756
- http://www.openwall.com/lists/oss-security/2023/02/15/4
- https://www.jenkins.io/security/advisory/2023-02-15/#SECURITY-1756

---

#### 807. CVE-2023-23939

**严重程度 / Severity**: LOW | CVSS: 3.9

**漏洞描述 / Description**:
Azure/setup-kubectl is a GitHub Action for installing Kubectl. This vulnerability only impacts versions before version 3. An insecure temporary creation of a file allows other actors on the Actions runner to replace the Kubectl binary created by this action because it is world writable. This Kubectl tool installer runs `fs.chmodSync(kubectlPath, 777)` to set permissions on the Kubectl binary, however, this allows any local user to replace the Kubectl binary. This allows privilege escalation to the user that can also run kubectl, most likely root. This attack is only possible if an attacker somehow breached the GitHub actions runner or if a user is utilizing an Action that maliciously executes this attack. This has been fixed and released in all versions `v3` and later. 775 permissions are used instead. Users are advised to upgrade. There are no known workarounds for this issue.

**参考链接 / References**:
- https://github.com/Azure/setup-kubectl/commit/d449d75495d2b9d1463555bb00ca3dca77a42ab6
- https://github.com/Azure/setup-kubectl/security/advisories/GHSA-p756-rfxh-x63h
- https://github.com/Azure/setup-kubectl/commit/d449d75495d2b9d1463555bb00ca3dca77a42ab6
- https://github.com/Azure/setup-kubectl/security/advisories/GHSA-p756-rfxh-x63h

---

#### 808. CVE-2023-23408

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
Azure Apache Ambari Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23408
- http://packetstormsecurity.com/files/173134/Azure-Apache-Ambari-2302250400-Spoofing.html
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23408

---

#### 809. CVE-2023-25722

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
A credential-leak issue was discovered in related Veracode products before 2023-03-27. Veracode Scan Jenkins Plugin before 23.3.19.0, when configured for remote agent jobs, invokes the Veracode Java API Wrapper in a manner that allows local users (with OS-level access of the Jenkins remote) to discover Veracode API credentials by listing the process and its arguments. Veracode Scan Jenkins Plugin before 23.3.19.0, when configured for remote agent jobs and when the "Connect using proxy" option is enabled and configured with proxy credentials, allows local users of the Jenkins remote to discover proxy credentials by listing the process and its arguments. Veracode Azure DevOps Extension before 3.20.0 invokes the Veracode Java API Wrapper in a manner that allows local users (with OS-level access to the Azure DevOps Services cloud infrastructure or Azure DevOps Server) to discover Veracode API credentials by listing the process and its arguments. Veracode Azure DevOps Extension before 3.20.0, when configured with proxy credentials, allows users (with shell access to the Azure DevOps Services cloud infrastructure or Azure DevOps Server) to discover proxy credentials by listing the process and its arguments.

**参考链接 / References**:
- https://docs.veracode.com/updates/r/c_all_int#veracode-jenkins-plugin-233190
- https://veracode.com
- https://docs.veracode.com/updates/r/c_all_int#veracode-jenkins-plugin-233190
- https://veracode.com

---

#### 810. CVE-2023-28300

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Azure Service Connector Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28300
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28300

---

#### 811. CVE-2023-28312

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Machine Learning Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28312
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28312

---

#### 812. CVE-2023-30514

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Jenkins Azure Key Vault Plugin 187.va_cd5fecd198a_ and earlier does not properly mask (i.e., replace with asterisks) credentials in the build log when push mode for durable task logging is enabled.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2023/04/13/3
- https://www.jenkins.io/security/advisory/2023-04-12/#SECURITY-3075
- http://www.openwall.com/lists/oss-security/2023/04/13/3
- https://www.jenkins.io/security/advisory/2023-04-12/#SECURITY-3075

---

#### 813. CVE-2023-32988

**严重程度 / Severity**: MEDIUM | CVSS: 4.3

**漏洞描述 / Description**:
A missing permission check in Jenkins Azure VM Agents Plugin 852.v8d35f0960a_43 and earlier allows attackers with Overall/Read permission to enumerate credentials IDs of credentials stored in Jenkins.

**参考链接 / References**:
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(1)
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(1)

---

#### 814. CVE-2023-32989

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
A cross-site request forgery (CSRF) vulnerability in Jenkins Azure VM Agents Plugin 852.v8d35f0960a_43 and earlier allows attackers to connect to an attacker-specified Azure Cloud server using attacker-specified credentials IDs obtained through another method.

**参考链接 / References**:
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(2)
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(2)

---

#### 815. CVE-2023-32990

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
A missing permission check in Jenkins Azure VM Agents Plugin 852.v8d35f0960a_43 and earlier allows attackers with Overall/Read permission to connect to an attacker-specified Azure Cloud server using attacker-specified credentials IDs obtained through another method.

**参考链接 / References**:
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(2)
- https://www.jenkins.io/security/advisory/2023-05-16/#SECURITY-2855%20(2)

---

#### 816. CVE-2022-35798

**严重程度 / Severity**: LOW | CVSS: 3.3

**漏洞描述 / Description**:
Azure Arc Jumpstart Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35798
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35798

---

#### 817. CVE-2023-22648

**严重程度 / Severity**: HIGH | CVSS: 8.0

**漏洞描述 / Description**:
A Improper Privilege Management vulnerability in SUSE Rancher causes permission changes in Azure AD not to be reflected to users 
while they are logged in the Rancher UI. This would cause the users to 
retain their previous permissions in Rancher, even if they change groups
 on Azure AD, for example, to a lower privileged group, or are removed 
from a group, thus retaining their access to Rancher instead of losing 
it.
This issue affects Rancher: from >= 2.6.7 before < 2.6.13, from >= 2.7.0 before < 2.7.4.

**参考链接 / References**:
- https://bugzilla.suse.com/show_bug.cgi?id=CVE-2023-22648
- https://github.com/rancher/rancher/security/advisories/GHSA-vf6j-6739-78m8
- https://bugzilla.suse.com/show_bug.cgi?id=CVE-2023-22648
- https://github.com/rancher/rancher/security/advisories/GHSA-vf6j-6739-78m8

---

#### 818. CVE-2023-34362

**严重程度 / Severity**: CRITICAL | CVSS: 9.8

**漏洞描述 / Description**:
In Progress MOVEit Transfer before 2021.0.6 (13.0.6), 2021.1.4 (13.1.4), 2022.0.4 (14.0.4), 2022.1.5 (14.1.5), and 2023.0.1 (15.0.1), a SQL injection vulnerability has been found in the MOVEit Transfer web application that could allow an unauthenticated attacker to gain access to MOVEit Transfer's database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database, and execute SQL statements that alter or delete database elements. NOTE: this is exploited in the wild in May and June 2023; exploitation of unpatched systems can occur via HTTP or HTTPS. All versions (e.g., 2020.0 and 2019x) before the five explicitly mentioned versions are affected, including older unsupported versions.

**参考链接 / References**:
- http://packetstormsecurity.com/files/172883/MOVEit-Transfer-SQL-Injection-Remote-Code-Execution.html
- http://packetstormsecurity.com/files/173110/MOVEit-SQL-Injection.html
- https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023
- http://packetstormsecurity.com/files/172883/MOVEit-Transfer-SQL-Injection-Remote-Code-Execution.html
- http://packetstormsecurity.com/files/173110/MOVEit-SQL-Injection.html

---

#### 819. CVE-2023-21565

**严重程度 / Severity**: HIGH | CVSS: 7.1

**漏洞描述 / Description**:
Azure DevOps Server Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21565
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21565

---

#### 820. CVE-2023-21569

**严重程度 / Severity**: MEDIUM | CVSS: 5.5

**漏洞描述 / Description**:
Azure DevOps Server Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21569
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21569

---

#### 821. CVE-2023-3128

**严重程度 / Severity**: CRITICAL | CVSS: 9.4

**漏洞描述 / Description**:
Grafana is validating Azure AD accounts based on the email claim. 

On Azure AD, the profile email field is not unique and can be easily modified. 

This leads to account takeover and authentication bypass when Azure AD OAuth is configured with a multi-tenant app.

**参考链接 / References**:
- https://github.com/grafana/bugbounty/security/advisories/GHSA-gxh2-6vvc-rrgp
- https://grafana.com/security/security-advisories/cve-2023-3128/
- https://security.netapp.com/advisory/ntap-20230714-0004/
- https://github.com/grafana/bugbounty/security/advisories/GHSA-gxh2-6vvc-rrgp
- https://grafana.com/security/security-advisories/cve-2023-3128/

---

#### 822. CVE-2023-37261

**严重程度 / Severity**: CRITICAL | CVSS: 9.6

**漏洞描述 / Description**:
OpenComputers is a Minecraft mod that adds programmable computers and robots to the game. This issue affects every version of OpenComputers with the Internet Card feature enabled; that is, OpenComputers 1.2.0 until 1.8.3 in their most common, default configurations. If the OpenComputers mod is installed as part of a Minecraft server hosted on a popular cloud hosting provider, such as AWS, GCP and Azure, those metadata services' API endpoints are not forbidden (aka "blacklisted") by default. As such, any player can gain access to sensitive information exposed via those metadata servers, potentially allowing them to pivot or privilege escalate into the hosting provider. In addition, IPv6 addresses are not correctly filtered at all, allowing broader access into the local IPv6 network. This can allow a player on a server using an OpenComputers computer to access parts of the private IPv4 address space, as well as the whole IPv6 address space, in order to retrieve sensitive information.

OpenComputers v1.8.3 for Minecraft 1.7.10 and 1.12.2 contains a patch for this issue. Some workarounds are also available. One may disable the Internet Card feature completely. If using OpenComputers 1.3.0 or above, using the allow list (`opencomputers.internet.whitelist` option) will prohibit connections to any IP addresses and/or domains not listed; or one may add entries to the block list (`opencomputers.internet.blacklist` option). More information about mitigations is available in the GitHub Security Advisory.

**参考链接 / References**:
- https://github.com/MightyPirates/OpenComputers/blob/5b2ba76a4c242b369b9b6ac6196fd04d96580ad0/src/main/resources/application.conf#L966-L986
- https://github.com/MightyPirates/OpenComputers/blob/5b2ba76a4c242b369b9b6ac6196fd04d96580ad0/src/main/scala/li/cil/oc/Settings.scala#L614-L637
- https://github.com/MightyPirates/OpenComputers/commit/d13c015357fd6c42e0a1bdd6e1ef9462f0450a15
- https://github.com/MightyPirates/OpenComputers/issues/2365
- https://github.com/MightyPirates/OpenComputers/releases/tag/1.12.2-forge%2F1.8.3

---

#### 823. CVE-2023-37262

**严重程度 / Severity**: CRITICAL | CVSS: 9.6

**漏洞描述 / Description**:
CC: Tweaked is a mod for Minecraft which adds programmable computers, turtles, and more to the game. Prior to versions 1.20.1-1.106.0, 1.19.4-1.106.0, 1.19.2-1.101.3, 1.18.2-1.101.3, and 1.16.5-1.101.3, if the cc-tweaked plugin is running on a Minecraft server hosted on a popular cloud hosting providers, like AWS, GCP, and Azure, those metadata services API endpoints are not forbidden (aka "blacklisted") by default. As such, any player can gain access to sensitive information exposed via those metadata servers, potentially allowing them to pivot or privilege escalate into the hosting provider. Versions 1.20.1-1.106.0, 1.19.4-1.106.0, 1.19.2-1.101.3, 1.18.2-1.101.3, and 1.16.5-1.101.3 contain a fix for this issue.

**参考链接 / References**:
- https://github.com/MightyPirates/OpenComputers/security/advisories/GHSA-vvfj-xh7c-j2cm
- https://github.com/cc-tweaked/CC-Tweaked/blob/96847bb8c28df51e5e49f2dd2978ff6cc4e2821b/projects/core/src/main/java/dan200/computercraft/core/apis/http/options/AddressPredicate.java#L116-L126
- https://github.com/cc-tweaked/CC-Tweaked/commit/4bbde8c50c00bc572578ab2cff609b3443d10ddf
- https://github.com/cc-tweaked/CC-Tweaked/security/advisories/GHSA-7p4w-mv69-2wm2
- https://github.com/dan200/ComputerCraft/issues/170

---

#### 824. CVE-2023-36868

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Service Fabric on Windows Information Disclosure Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36868
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36868

---

#### 825. CVE-2023-36871

**严重程度 / Severity**: MEDIUM | CVSS: 6.5

**漏洞描述 / Description**:
Azure Active Directory Security Feature Bypass Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36871
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36871

---

#### 826. CVE-2023-35393

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
Azure Apache Hive Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35393
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35393

---

#### 827. CVE-2023-35394

**严重程度 / Severity**: MEDIUM | CVSS: 4.6

**漏洞描述 / Description**:
Azure HDInsight Jupyter Notebook Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35394
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35394

---

#### 828. CVE-2023-36869

**严重程度 / Severity**: MEDIUM | CVSS: 6.3

**漏洞描述 / Description**:
Azure DevOps Server Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36869
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36869

---

#### 829. CVE-2023-36877

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
Azure Apache Oozie Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36877
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36877

---

#### 830. CVE-2023-36881

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
Azure Apache Ambari Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36881
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36881

---

#### 831. CVE-2023-38176

**严重程度 / Severity**: HIGH | CVSS: 7.0

**漏洞描述 / Description**:
Azure Arc-Enabled Servers Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38176
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38176

---

#### 832. CVE-2023-38188

**严重程度 / Severity**: MEDIUM | CVSS: 4.5

**漏洞描述 / Description**:
Azure Apache Hadoop Spoofing Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38188
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38188

---

#### 833. CVE-2023-41935

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Jenkins Azure AD Plugin 396.v86ce29279947 and earlier, except 378.380.v545b_1154b_3fb_, uses a non-constant time comparison function when checking whether the provided and expected CSRF protection nonce are equal, potentially allowing attackers to use statistical methods to obtain a valid nonce.

**参考链接 / References**:
- http://www.openwall.com/lists/oss-security/2023/09/06/9
- https://www.jenkins.io/security/advisory/2023-09-06/#SECURITY-3227
- http://www.openwall.com/lists/oss-security/2023/09/06/9
- https://www.jenkins.io/security/advisory/2023-09-06/#SECURITY-3227

---

#### 834. CVE-2023-29332

**严重程度 / Severity**: HIGH | CVSS: 7.5

**漏洞描述 / Description**:
Microsoft Azure Kubernetes Service Elevation of Privilege Vulnerability

**参考链接 / References**:
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29332
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29332

---
