# Windows 网络安全漏洞 | Windows Network Security

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 161**

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
