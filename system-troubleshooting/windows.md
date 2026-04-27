# Windows 常见故障及解决方法 | Windows Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 04:27:43 UTC_

## 中文 🇨🇳
**Windows 常见故障及解决方法**

本页面每小时自动从 Stack Exchange 社区抓取 WINDOWS 平台常见故障及解决方法。

### WINDOWS 常见故障及解决方法

#### 1. Find out which process is locking a file or folder in Windows

**故障现象**: Find out which process is locking a file or folder in Windows
**标签 / 来源**: Tags: windows, filesystems, process, community-faq-proposed | superuser | 👍 1331 | 💬 16 answers

**问题描述**:
Tags: windows, filesystems, process, community-faq-proposed | Score: 1331 | Views: 2068503 | Answers: 16

**解决方法 / 社区答案**:
You can use the Resource Monitor for this which comes built-in with Windows 7, 8, 10 and 11!

Open Resource Monitor, which can be found

By searching for Resource Monitor or  resmon.exe in the start menu, or
As a button on the Performance tab in your Task Manager


Go to the CPU tab
In the Processes section, select all processes by clicking the checkbox next to &quot;Image&quot; in the headers.
Use the search field in the Associated Handles section

See blue arrow in screen shot below



When you've found the handle, you can identify the process by looking at the Image and/or PID column.
You can then try to close the application as you normally would, or, if that's not possible, just right-click the handle and kill the process directly from there. Easy peasy!

**参考链接**: https://superuser.com/questions/117902/find-out-which-process-is-locking-a-file-or-folder-in-windows

> 📎 来源 / Source: https://superuser.com/questions/117902/find-out-which-process-is-locking-a-file-or-folder-in-windows

#### 2. What are the Windows A: and B: drives used for?

**故障现象**: What are the Windows A: and B: drives used for?
**标签 / 来源**: Tags: windows, hard-drive | superuser | 👍 1006 | 💬 20 answers

**问题描述**:
Tags: windows, hard-drive | Score: 1006 | Views: 531718 | Answers: 20

**解决方法 / 社区答案**:
Short Version: A: &amp; B: are reserved by floppy disk drives, so C: is used by hard drives for backwards compatibility reasons.



Once upon a time, the early CP/M and IBM PC style computers had no hard drive.  You had one floppy drive, and that was it.  Unless you spent another $1k or so on a second floppy drive, then your system was smokin'!  If you only had one drive it was common to boot from one disk, put in the other disk with your programs and data, then run the program.  Once the program finished, the computer would request that you reinsert the boot disk so you could use the command line again.  Copying data from one disk to the other was a series of

Please insert source disk into drive A:...
Please insert destination disk into drive A:...
Please insert source disk into drive A:...


By the time hard drives became cheap, the "expensive" computers typically had two floppy drives (one to boot and run common programs, one to save data and run specific programs). And so it was common for the motherboard hardware to support two floppy drives at fixed system addresses.  Since it was built into the hardware, it was thought that building the same requirement into the OS was acceptable, and any hard drives added to the machine would start with disk C: and so forth.

During the transition from 5.25" disks (which were actually, physically floppy) to 3.5" disks (which were encased in a harder plastic shell) it was common to have both drives in one system, and again it was supported on the motherboard with hardware, and in the OS at fixed addresses.  As very few systems ran out of drive letters, it was not thought to be important to consider making those drives re-assignable in the OS until much later when drives were abstracted along with addresses due to the plug'n'play standard.

A lot of software was developed since that time, and unfortunately much of it expected to see long-term storage on the C: drive.  This includes the BIOS software that boots the computer.  You can still attach two floppy drives, boot into DOS 6.1, and use it as you would have in the early 90's, with floppy drives A: and B:.

So largely the reason for starting the hard drive at C is for backwards compatibility.  While the OS has abstracted data storage to some degree, it still treats A: and B: differently, in such a way that allows them to be removed from the system without altering the OS, caching them differently, and due to early viruses treating their boot sector with more caution than the hard drive's boot sector.

For Windows specifically, it's worth mentioning that you can use A: and B: as the names for volumes, be it a flash drive or an internal hard drive.

**参考链接**: https://superuser.com/questions/231273/what-are-the-windows-a-and-b-drives-used-for

> 📎 来源 / Source: https://superuser.com/questions/231273/what-are-the-windows-a-and-b-drives-used-for

#### 3. How can I display the contents of an environment variable from the command prompt in Windows 7?

**故障现象**: How can I display the contents of an environment variable from the command prompt in Windows 7?
**标签 / 来源**: Tags: windows-7, windows, command-line, environment-variables | superuser | 👍 833 | 💬 8 answers

**问题描述**:
Tags: windows-7, windows, command-line, environment-variables | Score: 833 | Views: 3005018 | Answers: 8

**解决方法 / 社区答案**:
In Windows Command-Prompt the syntax is echo %PATH%
To get a list of all environment variables enter the command set without any parameters.
To send those variables to a text file enter the command set &gt; filename.txt

Related

How to list global environment variables separately from user-specific environment variables?

**参考链接**: https://superuser.com/questions/341192/how-can-i-display-the-contents-of-an-environment-variable-from-the-command-promp

> 📎 来源 / Source: https://superuser.com/questions/341192/how-can-i-display-the-contents-of-an-environment-variable-from-the-command-promp

#### 4. How to *disable* automatic reboots in Windows 10?

**故障现象**: How to *disable* automatic reboots in Windows 10?
**标签 / 来源**: Tags: windows-10, windows-update, reboot | superuser | 👍 676 | 💬 20 answers

**问题描述**:
Tags: windows-10, windows-update, reboot | Score: 676 | Views: 402626 | Answers: 20

**解决方法 / 社区答案**:
Note: Unfortunately this appears to not work on Windows 10 Home, and I'm not sure of a workable solution for users of this edition.

I posted this as an answer on another question, but as that appears to be a duplicate of this question I'll provide it here too:
You can edit your local group policy settings to force Windows update to only download updates, but wait for your input to install (and therefore reboot.)
Open your start menu and type Group, then click Edit group policy
Expand either (depending on Windows 10 or 11 version):

Computer Configuration \ Administrative Templates \ Windows Components \ Windows Update
or: Computer Configuration \ Administrative Templates \ Windows Components \ Manage end user experiences \ Windows Update
or: Computer Configuration \ Administrative Templates \ All Settings


Double click Configure Automatic Updates and enable the policy, and configure it as needed.

Head back to Windows Update and click Check for updates. Once it is done, click on the Advanced options
You should see your new settings being 'enforced.'

After applying this setting on a test VM, I left Windows Update open and noticed it started downloading.

When it finishes downloading, you get a toast notification that there are updates and you need to install them.

Note that you must click install now. Restarting or shutting down from the start menu does not appear to trigger the install process.

More info:
I'm not sure if editing Local Group Policy is an option in the Home edition of Windows 10, but the same result should be possible through the registry (I haven't tested this as I used the policy method myself). Including this in case non-pro users come looking for an answer too.

Press Win + R and type regedit then hit Enter

Navigate to HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU
(you may need to create the keys manually if they don't exist)

Create a new DWORD value called AUOptions and enter a value of either 2 or 3.
2 = Notify before download
3 = Automatically download and notify of installation

Restart PC

Check for updates

Inspect Advanced Settings



Update following Anniversary Update (1607):
I've seen a lot a few comments lately from people saying this no longer works after the Anniversary Update.
I've been running some tests, detailed in the two blog posts here:

Validating Prevention of Automatic Reboots on Windows 10, Version 1607
Update on Windows Update... Up Time

These tests have been running for nearly three weeks and I have yet to see any forced reboots.
In light of these results, it appears that this does still work.

Things to keep in mind:

I did not set any settings around Active Hours or the Reboot Options.
DO NOT click the 'Install now' button within the Windows Update UI unless you're ready to install and reboot. Once the updates are installed, there is no stopping Windows from deciding to reboot.
Windows will nag you with Toasts, Action Center alerts and banners across your screen. As long as you don't install the updates you're fine (but do do them eventually.)

**参考链接**: https://superuser.com/questions/957267/how-to-disable-automatic-reboots-in-windows-10

> 📎 来源 / Source: https://superuser.com/questions/957267/how-to-disable-automatic-reboots-in-windows-10

#### 5. &quot;directory junction&quot; vs &quot;directory symbolic link&quot;?

**故障现象**: &quot;directory junction&quot; vs &quot;directory symbolic link&quot;?
**标签 / 来源**: Tags: windows, filesystems, ntfs, symbolic-link | superuser | 👍 609 | 💬 3 answers

**问题描述**:
Tags: windows, filesystems, ntfs, symbolic-link | Score: 609 | Views: 462514 | Answers: 3

**解决方法 / 社区答案**:
A junction is definitely not the same thing as a directory symbolic link, although they behave similarly.  The main difference is that, if you are looking at a remote server, junctions are processed at the server and directory symbolic links are processed at the client.  Also see Matthew's comment on the fact that this means symbolic links on the local file system can point to remote file systems.

Suppose that on a machine named Alice you were to put a junction point c:\myjp and a directory symbolic link c:\mysymlink, both pointing to c:\targetfolder.  While you're using Alice you won't notice much difference between them.  But if you're using another machine named Bob, then the junction point

\\Alice\c$\myjp will point to \\Alice\c$\targetfolder

but the symbolic link

\\Alice\c$\mysymlink will point to \\Bob\c$\targetfolder

(Caveat: by default, the system doesn't follow symlinks on remote volumes, so in most cases the second example will actually result in either "File Not Found" or "The symbolic link cannot be followed because its type is disabled.")

The difference between a directory symbolic link and a file symbolic link is simply that one represents a directory and one represents a file.  Since the target of the link doesn't need to exist when the link is created, the file system needs to know whether to tell applications that it is a directory or not.

It should also be noted that creating a symbolic link requires special privilege (by default, only available to elevated processes) whereas creating a junction only requires access to the file system.

**参考链接**: https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link

> 📎 来源 / Source: https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link

#### 6. How do I run multiple commands on one line in PowerShell?

**故障现象**: How do I run multiple commands on one line in PowerShell?
**标签 / 来源**: Tags: windows, command-line, powershell | superuser | 👍 603 | 💬 5 answers

**问题描述**:
Tags: windows, command-line, powershell | Score: 603 | Views: 893175 | Answers: 5

**解决方法 / 社区答案**:
Use a semicolon to chain commands in PowerShell:

ipconfig /release; ipconfig /renew

**参考链接**: https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell

> 📎 来源 / Source: https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell

#### 7. Windows 7 SP1 Windows Update stuck checking for updates

**故障现象**: Windows 7 SP1 Windows Update stuck checking for updates
**标签 / 来源**: Tags: windows-7, windows, windows-update | superuser | 👍 561 | 💬 13 answers

**问题描述**:
Tags: windows-7, windows, windows-update | Score: 561 | Views: 3337928 | Answers: 13

**解决方法 / 社区答案**:
Fix

Microsoft released a Windows Update Client Update which is part of the July 2016 Update Rollup to fix the long hang at Windows Update scan.


  This update contains some improvements to Windows Update Client in
  Windows 7 Service Pack 1 (SP1). This includes the following:
  
  
  An optimization that addresses long scan time for updates that's reported on some computers.
  



Download:


32 Bit
64 Bit

Stop Windows Update service. This speeds up the setup of MSU updates and the useless steps from Moab are not required (reboot causes that the WU service is stopped until it gets started via trigger when Internet is available). This can be done from the command line, or from the Service Manager window.
Try the downloaded update and see if it speeds up the installation of Updates.


To be able to install the update you first need to install the April 2015 servicing stack update for Windows 7 and Windows Server 2008 R2 update (again, stop WU service before trying to install the MSU).

Download (April 2015 servicing stack update): 


32 Bit
64 Bit


Workaround 1

If this is still not helping to search for new updates, use WSUSOffline to get all the updates.

**参考链接**: https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates

> 📎 来源 / Source: https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates

#### 8. What is the home directory on Windows Subsystem for Linux?

**故障现象**: What is the home directory on Windows Subsystem for Linux?
**标签 / 来源**: Tags: windows-10, bash, windows-subsystem-for-linux | superuser | 👍 526 | 💬 11 answers

**问题描述**:
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 526 | Views: 1498445 | Answers: 11

**解决方法 / 社区答案**:
In the latest versions [2025 WSL2], the file system is accessed from:
# \\wsl.localhost\&lt;distro name&gt;
shortcut:
# \\wsl$\&lt;Distribution&gt;:
ex:
\\wsl$\Ubuntu

You can also find this path by starting the distro then running $ wslpath -w $HOME
The files themselves seem to be stored within a .vhdx file in a similar location to 2020's solution.
%LOCALAPPDATA%\wsl\&lt;a unique uuid&gt;\ext4.vhdx

For older WSL2 installs [2020] it would be a file like:
%LOCALAPPDATA%\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\ext4.vhdx

For example with Debian the file would be a file that is an ext4 virtual disk:
%LOCALAPPDATA%\Packages\YourDistroName-ID\LocalState, you can see a file named ext4.vhdx

You can find the exact filenames by referencing the registry, ex: powershell:
(Get-ChildItem HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | ForEach-Object {Get-ItemProperty $_.PSPath}) | select DistributionName,BasePath,VhdFileName

Also useful if a distro isn't installed in the standard directory, doesn't seem possible to get using wsl command from the command prompt.
Previously, in 2018, The root Linux path was related to which distribution you had installed from the Microsoft Store rather than one global path; for Ubuntu, it was located at:
%LOCALAPPDATA%\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs

but with the files stored directly on the NTFS file system.

**参考链接**: https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux

> 📎 来源 / Source: https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux

#### 9. Can I delete the folder C:\ProgramData\Package Cache\?

**故障现象**: Can I delete the folder C:\ProgramData\Package Cache\?
**标签 / 来源**: Tags: windows, disk-space | superuser | 👍 523 | 💬 10 answers

**问题描述**:
Tags: windows, disk-space | Score: 523 | Views: 870931 | Answers: 10

**解决方法 / 社区答案**:
TL;DR: Do NOT delete this folder
(see below for workarounds)

Why Not?
There have been conflicting reports about whether the absence of this folder (as a consequence of deleting it) will actually and in all cases cause issues with the visual studio installation, i.e. during normal operation, during reinstall, patch/upgrade, repair install, or uninstall.  However, the recommendation from MICROSOFT is clearly to NOT DELETE IT.
From Microsoft Developer Tools Blogs → HERE

When repairing, modifying, or uninstalling a product or when
installing or uninstalling a patch, if source media is required the
package cache is used automatically and most users will never see a
prompt. Only if the package cache is missing or incomplete will Visual
Studio setup prompt to download (if connected) or locate media as
shown in the screenshot below.

Users who have installed from media even get the option to download
(if connected). So while very few customers should ever see this
dialog, we wanted to make sure the experience was easy.
Even though we
will prompt to download packages to the cache if missing, we recommend
users do not remove the package cache. Not only is the cached used by
many other products that are installed with Burn and may not provide the same download experience, there are scenarios when
Windows Installer may require source that we cannot handle because our
code is not running.


Solution/Work-Around:#
If you need to reclaim this space, your safest bet is to avoid &quot;deleting&quot; anything, but to instead, move this folder and all it's files.  You can safely do this following the instructions below to any local/live, online, near-line, or offline storage as long as that storage system that can be mounted to a drive letter or any mount point on the NTFS file system.  Any of the following will work:

another live (mounted) partition
an optical disc (CD, DVD, etc.) with a live filesystem like FAT, or NTFS
an external hard drive
a USB drive
a network drive

Whenever you are prompted for the media/receive any errors about missing files/missing location, you simply make sure to remount/reinsert your drive/media if it's not already a live partition.
Once moved, in order to &quot;link&quot; the old mount point/location (in most cases C:\ProgramData\Package Cache\), you simply create a directory junction to it.
Junctions are recognized at the file system level as an alias entry in the FSTAB.  Therefore, it's transparent to all programs, including the OS itself.  In other words, it is NOT seen as a file that simply points to another location (like a shortcut) and therefore always works without incident.

You would move the folder(s) in question to its new location

Create the junction

Option 1. (natively): Just issue the built-in Windows Vista / 7 / 8 command and the cmd prompt:
  mklink /J link-(new location) target-(original folder)



NOTE:  If you make the newpath absolute, you'll be able to move link without breaking the pointer to the newpath. If you make the newpath relative, you'll be able prevent breaking the link, as long as you move BOTH the link and target TOGETHER and maintain their relative paths.

Option 2. (using a tool):  Another GREAT alternative is a free handy utility I've been using for years called &quot;Link Shell Extension&quot;.  LSE is free and you can find it here (or Google for it): http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html
LSE allows you to create symlinks, hardlinks, junctions, smartcopies, smartclones, smart mirrors, smart moves, splices, multiple sources, and bunch of other stuff I found too confusing to read, frankly.  But, it's a brilliant free product that creates a Windows Explorer context menu that allows you right-click on your LINK-TARGET folder then drag it to where you'd like to create the actual link. You can of course rename the link to anything you'd like.

**参考链接**: https://superuser.com/questions/455853/can-i-delete-the-folder-c-programdata-package-cache

> 📎 来源 / Source: https://superuser.com/questions/455853/can-i-delete-the-folder-c-programdata-package-cache

#### 10. How to check if a binary is 32- or 64-bit on Windows?

**故障现象**: How to check if a binary is 32- or 64-bit on Windows?
**标签 / 来源**: Tags: windows, binary-files, 32-vs-64-bit | superuser | 👍 522 | 💬 32 answers

**问题描述**:
Tags: windows, binary-files, 32-vs-64-bit | Score: 522 | Views: 509026 | Answers: 32

**解决方法 / 社区答案**:
After examining header values from Richard's answer, I came up with a solution which is fast, easy, and only requires a text editor. Even Windows' default notepad.exe would work.

Open the executable in a text editor. You might have to drag-and-drop or use
the editor's Open... dialog, because Windows doesn't show Open with... option in the context menu for executables.

Check the first printable characters after the first occurrence of PE. This part is most likely to be surrounded by at least some whitespace (could be a lot of it), so it can be easily done visually.


Here is what you're going to find:
32-bit:
PE  L

64-bit:
PE  d†

A word of warning: using default Notepad on big files can be very slow, so better not use it for files larger than a megabyte or a few. In my case, it took about 30 seconds to display a 12 MiB file. Notepad++, however, was able to display a 120 MiB executable almost instantly.
This is solution might be useful in case you need to inspect a file on a machine you can't install any additional software on.
Additional info:
If you have a HEX-Editor available, the location of PE Signature is located at offset 0x3C. The signature is PE\0\0 (letters &quot;P&quot; and &quot;E&quot; followed by two null bytes), followed by a two-byte Machine Type in Little Endian.
The signature is usually further ahead in MZ files.
The relevant values are 0x8664 for a 64-bit executable and 0x014c for a 32-bit one (64 86 and 4c 01 respectively when adjusted for endianness, but any decent hex editor will automatically handle endianness when you search for a hex value). There are a lot more possible values, but you probably won't ever encounter any of these, or be able to run such executables on your Windows PC.
Full list of machine types, along with the rest of .exe specifications, can be found in Microsoft PE and COFF Specification Machine Types section.

**参考链接**: https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows

> 📎 来源 / Source: https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows

#### 11. Create/rename a file/folder that begins with a dot in Windows?

**故障现象**: Create/rename a file/folder that begins with a dot in Windows?
**标签 / 来源**: Tags: windows | superuser | 👍 520 | 💬 12 answers

**问题描述**:
Tags: windows | Score: 520 | Views: 316540 | Answers: 12

**解决方法 / 社区答案**:
To create/rename on windows explorer, just rename to .name. - The additional dot at the end is necessary, and will be removed by Windows Explorer.

To create a new file begins with a dot, on command prompt:

echo testing &gt; .name

**参考链接**: https://superuser.com/questions/64471/create-rename-a-file-folder-that-begins-with-a-dot-in-windows

> 📎 来源 / Source: https://superuser.com/questions/64471/create-rename-a-file-folder-that-begins-with-a-dot-in-windows

#### 12. Is there any &#39;sudo&#39; command for Windows?

**故障现象**: Is there any &#39;sudo&#39; command for Windows?
**标签 / 来源**: Tags: windows, command-line, privileges | superuser | 👍 518 | 💬 19 answers

**问题描述**:
Tags: windows, command-line, privileges | Score: 518 | Views: 916657 | Answers: 19

**解决方法 / 社区答案**:
The runas command.

runas [{/profile|/noprofile}] [/env] [/netonly] [/smartcard] [/showtrustlevels] [/trustlevel] /user:UserAccountName program


Just run:

runas /noprofile /user:Administrator cmd 


to start a command shell as a administrator

**参考链接**: https://superuser.com/questions/42537/is-there-any-sudo-command-for-windows

> 📎 来源 / Source: https://superuser.com/questions/42537/is-there-any-sudo-command-for-windows

#### 13. How do I exit telnet?

**故障现象**: How do I exit telnet?
**标签 / 来源**: Tags: windows, telnet | superuser | 👍 512 | 💬 6 answers

**问题描述**:
Tags: windows, telnet | Score: 512 | Views: 910606 | Answers: 6

**解决方法 / 社区答案**:
It should have printed something along the lines of:

Escape character is '^]'.


Since ^X is  CtrlX, try Ctrl] for ^]. 

You should then enter the telnet console, where you can enter quit to leave telnet.

**参考链接**: https://superuser.com/questions/486496/how-do-i-exit-telnet

> 📎 来源 / Source: https://superuser.com/questions/486496/how-do-i-exit-telnet

#### 14. Windows SSH: Permissions for &#39;private-key&#39; are too open

**故障现象**: Windows SSH: Permissions for &#39;private-key&#39; are too open
**标签 / 来源**: Tags: windows, ssh, permissions, openssh, private-key | superuser | 👍 498 | 💬 18 answers

**问题描述**:
Tags: windows, ssh, permissions, openssh, private-key | Score: 498 | Views: 1047407 | Answers: 18

**解决方法 / 社区答案**:
You locate the file in Windows Explorer, right-click on it then select "Properties". Navigate to the "Security" tab and click "Advanced".

Change the owner to you, disable inheritance and delete all permissions. Then grant yourself "Full control" and save the permissions. Now SSH won't complain about file permission too open anymore.

It should end up looking like this:

**参考链接**: https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

> 📎 来源 / Source: https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

#### 15. How to download files from command line in Windows like wget or curl

**故障现象**: How to download files from command line in Windows like wget or curl
**标签 / 来源**: Tags: windows, wget, curl | superuser | 👍 490 | 💬 21 answers

**问题描述**:
Tags: windows, wget, curl | Score: 490 | Views: 1880087 | Answers: 21

**解决方法 / 社区答案**:
An alternative I discovered recently, using PowerShell:

$client = new-object System.Net.WebClient
$client.DownloadFile("http://www.xyz.net/file.txt","C:\tmp\file.txt")


It works as well with GET queries.

If you need to specify credentials to download the file, add the following line in between:

$client.Credentials =  Get-Credential                


A standard windows credentials prompt will pop up. The credentials you enter there will be used to download the file. You only need to do this once for all the time you will be using the $client object.

**参考链接**: https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl

> 📎 来源 / Source: https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl

#### 16. How can I free up drive space from the Windows installer folder without killing Windows?

**故障现象**: How can I free up drive space from the Windows installer folder without killing Windows?
**标签 / 来源**: Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | superuser | 👍 486 | 💬 8 answers

**问题描述**:
Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | Score: 486 | Views: 1073383 | Answers: 8

**解决方法 / 社区答案**:
I created "PatchCleaner" to clean the windows installer directory of all orphaned files in one easy click. If you don't trust the app to do the right thing, use the move feature to put them somewhere safe in case you need them back in the future. I have run it on multiple machines and saved up to 15Gb of space :-)

Run PatchCleaner after windows updates to find newly orphaned files.

I recommend you use the Move action, and move the orphaned patches to external storage, just to be safe

PatchCleaner @ HomeDev

Known Issues (full details on website)


Adobe Reader can fail to update after running PatchCleaner.


NOTE: as @ Feb-2016 version 1.4.1.0 is out that has a fix to allow customisable filters to exclude adobe reader from being incorrectly detected.

**参考链接**: https://superuser.com/questions/707767/how-can-i-free-up-drive-space-from-the-windows-installer-folder-without-killing

> 📎 来源 / Source: https://superuser.com/questions/707767/how-can-i-free-up-drive-space-from-the-windows-installer-folder-without-killing

#### 17. How can I remove malicious spyware, malware, adware, viruses, trojans or rootkits from my PC?

**故障现象**: How can I remove malicious spyware, malware, adware, viruses, trojans or rootkits from my PC?
**标签 / 来源**: Tags: windows, anti-virus, virus, malware, community-faq | superuser | 👍 474 | 💬 18 answers

**问题描述**:
Tags: windows, anti-virus, virus, malware, community-faq | Score: 474 | Views: 333616 | Answers: 18

**解决方法 / 社区答案**:
Here's the thing: Malware in recent years has become both sneakier and nastier:
Sneakier, not only because it's better at hiding with rootkits or EEPROM hacks, but also because it travels in packs. Subtle malware can hide behind more obvious infections. There are lots of good tools listed in answers here that can find 99% of malware, but there's always that 1% they can't find yet. Mostly, that 1% is stuff that is new: the malware tools can't find it because it just came out and is using some new exploit or technique to hide itself that the tools don't know about yet.
Malware also has a short shelf-life. If you're infected, something from that new 1% is very likely to be one part of your infection. It won't be the whole infection: just a part of it. Security tools will help you find and remove the more obvious and well-known malware, and most likely remove all of the visible symptoms (because you can keep digging until you get that far), but they can leave little pieces behind, like a keylogger or rootkit hiding behind some new exploit that the security tool doesn't yet know how to check. In this way, malware can be extra sneaky and survive even skilled and persistent attempts to purge it. The anti-malware tools still have their place, but I'll get to that later.
Nastier, in that it won't just show ads, install a toolbar, or use your computer as a zombie anymore. Modern malware is likely to go right for the banking or credit card information. The people building this stuff are no longer just script kiddies looking for fame; they are now organized professionals motivated by profit, and if they can't steal from you directly, they'll look for something they can turn around and sell. This might be processing or network resources in your computer, but it might also be your social security number or encrypting your files and holding them for ransom.

Put these two factors together, and it's no longer worthwhile to even attempt to remove malware from an installed operating system. I used to be very good at removing this stuff, to the point where I made a significant part of my living that way, and I no longer even make the attempt. I'm not saying it can't be done, but I am saying that the cost/benefit and risk analysis results have changed: it's just not worth it anymore. There's too much at stake, and it's too easy to get results that only seem to be effective.
Lots of people will disagree with me on this, but I challenge they are not weighing consequences of failure strongly enough. Are you willing to wager your life savings, your good credit, even your identity, that you're better at this than crooks who make millions doing it every day?  If you try to remove malware and then keep running the old system, that's exactly what you're doing.
I know there are people out there reading this thinking, &quot;Hey, I've removed several infections from various machines and nothing bad ever happened.&quot; Me too, friend. Me too. In days past I have cleaned my share of infected systems. Nevertheless, I suggest we now need to add &quot;yet&quot; to the end of that statement. You might be 99% effective, but you only have to be wrong one time, and the consequences of failure are much higher than they once were; the cost of just one failure can easily outweigh all of the other successes. You might even have a machine already out there that still has a ticking time bomb inside, just waiting to be activated or to collect the right information before reporting it back. Even if you have a 100% effective process now, this stuff changes all the time. Remember: you have to be perfect every time; the bad guys only have to get lucky once.
In summary, it's unfortunate, but if you have a confirmed malware infection, a complete re-pave of the computer should be the first place you turn instead of the last.

Here's how to accomplish that:
Before you're infected, make sure you have a way to re-install any purchased software, including the operating system, that does not depend on anything stored on your internal hard disk. For this purpose, that normally just means hanging onto cd/dvds or product keys, but the operating system may require you to create recovery disks yourself.1 Don't rely on a recovery partition for this. If you wait until after an infection to ensure you have what you need to re-install, you may find yourself paying for the same software again. With the rise of ransomware, it's also extremely important to take regular backups of your data (plus, you know, regular non-malicious things like hard drive failure).
When you suspect you have malware, look to other answers here. There are a lot of good tools suggested. My only issue is the best way to use them: I only rely on them for the detection. Install and run the tool, but as soon as it finds evidence of a real infection (more than just &quot;tracking cookies&quot;) just stop the scan: the tool has done its job and confirmed your infection.2
At the time of a confirmed infection, take the following steps:

Check your credit and bank accounts. By the time you find out about the infection, real damage may have already been done. Take any steps necessary to secure your cards, bank account, and identity.
Change passwords at any web site you accessed from the compromised computer. Do not use the compromised computer to do any of this.
Take a backup of your data (even better if you already have one).
Re-install the operating system using original media obtained directly from the OS publisher. Make sure the re-install includes a complete re-format of your disk; a system restore or system recovery operation is not enough.
Re-install your applications.
Make sure your operating system and software is fully patched and up to date.
Run a complete anti-virus scan to clean the backup from step three.
Restore the backup.

If done properly, this is likely to take between two and six real hours of your time, spread out over two to three days (or even longer) while you wait for things like apps to install, windows updates to download, or large backup files to transfer... but it's better than finding out later that crooks drained your bank account. Unfortunately, this is something you should do yourself, or a have a techy friend do for you. At a typical consulting rate of around $100/hr, it can be cheaper to buy a new machine than pay a shop to do this. If you have a friend do it for you, do something nice to show your appreciation. Even geeks who love helping you set up new things or fix broken hardware often hate the tedium of clean-up work. It's also best if you take your own backup... your friends aren't going to know where you put what files, or which ones are really important to you. You're in a better position to take a good backup than they are.
Soon even all of this may not be enough, as there is now malware capable of infecting firmware. Even replacing the hard drive may not remove the infection, and buying a new computer will be the only option. Thankfully, at the time I'm writing this we're not to that point yet, but the day is definitely approaching fast.

If you absolutely insist, beyond all reason, you really want to clean your existing install rather than start over, then for the love of God make sure whatever method you use involves one of the following two procedures:

Remove the hard drive and connect it as a guest disk in a different (clean!) computer to run the scan.

OR

Boot from a CD/USB key with its own set of tools running its own kernel. Make sure the image for this is obtained and burned on a clean computer. If necessary, have a friend make the disk for you.

Under no circumstances should you try to clean an infected operating system using software running as a guest process of the compromised operating system. That's just plain dumb.

Of course, the best way to fix an infection is to avoid it in the first place, and there are some things you can do to help with that:

Keep your system patched. Make sure you promptly install Windows Updates, Adobe Updates, Java Updates, Apple Updates, etc. This is far more important even than anti-virus software, and for the most part it's not that hard, as long as you keep current. Most of those companies have informally settled on all releasing new patches on the same day each month, so if you keep current it doesn't interrupt you that often. Forced Windows Update reboots typically only happen when you ignore the notices for too long. If this happens to you often, it's on you to change your behavior. These are important, and it's not okay to continually just choose the &quot;install later&quot; option, even if it's easier in the moment.

Do not run as administrator by default. In recent versions of Windows, it's as simple as leaving the UAC feature turned on. Keeping an second administrator account distinct from your normal day to day account is even better.

Use a good firewall tool. These days the default firewall in Windows is actually good enough. You may want to supplement this layer with something like WinPatrol that helps stop malicious activity on the front end. Windows Defender works in this capacity to some extent as well. Basic Ad-Blocker browser plugins are also becoming increasingly useful at this level as a security tool.

Set most browser plug-ins (especially Flash and Java) to &quot;Ask to Activate&quot;.

Run current anti-virus software. This is a distant fifth to the other options, as traditional A/V software often just isn't that effective anymore. It's also important to emphasize the &quot;current&quot;. You could have the best antivirus software in the world, but if it's not up to date, you may just as well uninstall it.
For this reason, I currently recommend Microsoft Defender. There are likely far better scanning engines out there, but Microsoft Defender is built into Windows and will keep itself up to date via the normal Windows Update mechanism, without ever risking an expired registration. AVG and Avast also work well in this way. I just can't recommend any anti-virus software you have to actually pay for, because it's just far too common a paid subscription lapses and you end up with out-of-date definitions.
It's also worth noting here that Mac users now need to run antivirus software, too. The days when they could get away without it are long gone. As an aside, I think it's hilarious I now must recommend Mac users buy anti-virus software, but advise Windows users against it.

Avoid torrent sites, warez, pirated software, and pirated movies/videos. This stuff is often injected with malware by the person who cracked or posted it — not always, but often enough to avoid the whole mess. It's part of why a cracker would do this: often they will get a cut of any profits.

Use your head when browsing the web. You are the weakest link in the security chain. If something sounds too good to be true, it probably is. The most obvious download button is rarely the one you want to use any more when downloading new software, so make sure to read and understand everything on the web page before you click that link. If you see a pop up or hear an audible message asking you to call Microsoft or install some security tool, it's a fake.
Also, prefer to download the software and updates/upgrades directly from vendor or developer rather than third party file hosting websites.



1 Microsoft now publishes the Windows 10 install media so you can legally download and write to an 8GB or larger flash drive for free. You still need a valid license, but you don't need a separate recovery disk for the basic operating system any more.
2 This is a good time to point out I have softened my approach somewhat. Today, most &quot;infections&quot; fall under the category of PUPs (Potentially Unwanted Programs) and browser extensions included with other downloads. Often these PUPs/extensions can safely be removed through traditional means, and they are now a large enough percentage of malware that I may stop at this point and simply try the Add/Remove Programs feature or normal browser option to remove an extension. However, at the first sign of something deeper — any hint the software won't just uninstall normally — and it's back to repaving the machine.

**参考链接**: https://superuser.com/questions/100360/how-can-i-remove-malicious-spyware-malware-adware-viruses-trojans-or-rootkit

> 📎 来源 / Source: https://superuser.com/questions/100360/how-can-i-remove-malicious-spyware-malware-adware-viruses-trojans-or-rootkit

#### 18. How to rename the User folder in Windows 10?

**故障现象**: How to rename the User folder in Windows 10?
**标签 / 来源**: Tags: windows, windows-10, microsoft-onedrive | superuser | 👍 468 | 💬 11 answers

**问题描述**:
Tags: windows, windows-10, microsoft-onedrive | Score: 468 | Views: 1824063 | Answers: 11

**解决方法 / 社区答案**:
Microsoft has actually documented a very simple and clean way to rename a user profile folder.
EDIT Feb 2022: If you plan to use winget to manage your Windows installations at any point, note that Microsoft now warns against using this procedure under Windows 10 or later as it can stop winget working. Information about winget
There is no need to create a new user account, so all the settings associated with the existing user profile are preserved. And the only registry change required is to edit a single string value (the one that tells Windows the path of the user profile folder):


Log in by using another administrative account.

Note. You may need to create a new Administrative account at first.

Go to the C:\users\ folder and rename the subfolder with the original user name to the new user name.
Go to the registry and modify the registry value ProfileImagePath to the new path name.HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\&lt;User SID&gt;\


That's it!
The procedure quoted above was provided by Microsoft (here) in relation to a perceived issue with Windows 7, and continues to work in Windows 10.

Notes
&lt;User SID&gt;
The ProfileList registry key contains a number of sub-keys. To find out which one to change, click on each sub-key and examine the values, to find the sub-key with the right ProfileImagePath:

For example, let's say we want to get rid of the space in a user profile folder name. So in step 2, we use File Explorer to navigate to C:\Users and rename the John Smith subfolder JohnSmith. And in step 3, we click on the &lt;User SID&gt; sub-keys until we find the one with ProfileImagePath C:\Users\John Smith, and change it to C:\Users\JohnSmith.
Administrative login
You may find you have to restart instead of just logging out and logging back in. Otherwise, when you try to rename the folder, Windows may report that it is being used by another program.
Environment variables (info)
Some applications create env vars with the user profile path fully expanded, so it's advisable to check for these and reboot if any needed fixing.

**参考链接**: https://superuser.com/questions/890812/how-to-rename-the-user-folder-in-windows-10

> 📎 来源 / Source: https://superuser.com/questions/890812/how-to-rename-the-user-folder-in-windows-10

#### 19. Rebooting Ubuntu on Windows without rebooting Windows?

**故障现象**: Rebooting Ubuntu on Windows without rebooting Windows?
**标签 / 来源**: Tags: windows-10, windows-subsystem-for-linux | superuser | 👍 453 | 💬 9 answers

**问题描述**:
Tags: windows-10, windows-subsystem-for-linux | Score: 453 | Views: 990462 | Answers: 9

**解决方法 / 社区答案**:
You cannot reboot a distro with a single command. You must shut down and boot up the distro with two commands. If you run wsl.exe instead of wsl, then it works both in WSL Bash &amp; CMD.
View the list of distros and their current state:
wsl.exe -l -v

Shutdown everything: Build 18917+
wsl.exe --shutdown

Terminate a specific distro: Windows 1903+
wsl.exe -t &lt;DistroName&gt;

Boot up the default distro (marked with *):
wsl.exe

Boot up a specific distro:
wsl.exe -d &lt;DistroName&gt;


Older versions
# PowerShell (admin)
Restart-Service LxssManager

# or CMD (admin)
net stop LxssManager
net start LxssManager

**参考链接**: https://superuser.com/questions/1126721/rebooting-ubuntu-on-windows-without-rebooting-windows

> 📎 来源 / Source: https://superuser.com/questions/1126721/rebooting-ubuntu-on-windows-without-rebooting-windows

#### 20. How can I delete a symbolic link in Windows?

**故障现象**: How can I delete a symbolic link in Windows?
**标签 / 来源**: Tags: windows, windows-7, symbolic-link | superuser | 👍 439 | 💬 13 answers

**问题描述**:
Tags: windows, windows-7, symbolic-link | Score: 439 | Views: 575992 | Answers: 13

**解决方法 / 社区答案**:
Be very careful.
If you have a symbolic link that is a directory (made with mklink /d) then using del will delete all of the files in the target directory (the directory that the link points to), rather than just the link.
SOLUTION: rmdir on the other hand will only delete the directory link, not what the link points to.

**参考链接**: https://superuser.com/questions/167076/how-can-i-delete-a-symbolic-link-in-windows

> 📎 来源 / Source: https://superuser.com/questions/167076/how-can-i-delete-a-symbolic-link-in-windows

#### 21. How to delete directories with path/names too long for normal delete

**故障现象**: How to delete directories with path/names too long for normal delete
**标签 / 来源**: Tags: windows, file-management | superuser | 👍 433 | 💬 25 answers

**问题描述**:
Tags: windows, file-management | Score: 433 | Views: 568440 | Answers: 25

**解决方法 / 社区答案**:
Use the 7-Zip File Manager to delete them.  

If you are still having trouble, ensure that you utilize Shift+Delete inside the 7-Zip File Manager. Otherwise, Windows tries to move them to the Recycle Bin (which will fail again).

**参考链接**: https://superuser.com/questions/78434/how-to-delete-directories-with-path-names-too-long-for-normal-delete

> 📎 来源 / Source: https://superuser.com/questions/78434/how-to-delete-directories-with-path-names-too-long-for-normal-delete

#### 22. What is the Windows equivalent of the Unix command cat?

**故障现象**: What is the Windows equivalent of the Unix command cat?
**标签 / 来源**: Tags: windows, command-line, unix, cat | superuser | 👍 433 | 💬 4 answers

**问题描述**:
Tags: windows, command-line, unix, cat | Score: 433 | Views: 1180582 | Answers: 4

**解决方法 / 社区答案**:
type
It works across command.com, cmd, and PowerShell (though in the latter it's an alias for Get-Content, so is cat, so you could use either).
From the Wikipedia article (emphasis mine):

In computing, type is a command in various VMS. AmigaDOS, CP/M, DOS, OS/2 and Microsoft Windows command line interpreters (shells) such as COMMAND.COM, cmd.exe, 4DOS/4NT and Windows PowerShell. It is used to display the contents of specified files. It is analogous to the Unix cat command.

C:\&gt;echo hi &gt; a.txt
C:\&gt;echo bye &gt; b.txt
C:\&gt;type a.txt b.txt &gt; c.txt
C:\&gt;type c.txt
hi
bye

**参考链接**: https://superuser.com/questions/434870/what-is-the-windows-equivalent-of-the-unix-command-cat

> 📎 来源 / Source: https://superuser.com/questions/434870/what-is-the-windows-equivalent-of-the-unix-command-cat

#### 23. Mouse pointer moving on arrow keys pressed in Windows?

**故障现象**: Mouse pointer moving on arrow keys pressed in Windows?
**标签 / 来源**: Tags: windows-10, mouse | superuser | 👍 399 | 💬 1 answers

**问题描述**:
Tags: windows-10, mouse | Score: 399 | Views: 212010 | Answers: 1

**解决方法 / 社区答案**:
Tried killing all running processes on my PC till the problem went away and I can now say for sure the culprit was...
Microsoft Paint
(classic Win32 one)
Apparently it's got a feature that allows moving the mouse pointer using arrow keys, and for some reason sometimes it doesn't stop listening when the window loses focus, so Paint was running in the background since I often use it and it was still doing its job of moving the mouse.
This also explains why the problem can persist after a reboot: when you reboot Windows while Paint is running, Windows will automatically &quot;save your work&quot; and reopen Paint at system boot, causing the bug again!

**参考链接**: https://superuser.com/questions/1467313/mouse-pointer-moving-on-arrow-keys-pressed-in-windows

> 📎 来源 / Source: https://superuser.com/questions/1467313/mouse-pointer-moving-on-arrow-keys-pressed-in-windows

#### 24. How to disable the &quot;Get Windows 10&quot; icon shown in the notification area (tray)?

**故障现象**: How to disable the &quot;Get Windows 10&quot; icon shown in the notification area (tray)?
**标签 / 来源**: Tags: windows, windows-10-upgrade | superuser | 👍 394 | 💬 14 answers

**问题描述**:
Tags: windows, windows-10-upgrade | Score: 394 | Views: 552675 | Answers: 14

**解决方法 / 社区答案**:
If you just want to remove the tray icon until the next restart you can terminate the GWX.exe process using Task Manager.
To get rid of the icon permanently, uninstall KB3035583 which is responsible for these notifications:
Control panel, windows update, installed updates, sort by name, &quot;Update for Microsoft Windows KB3035583&quot; (not a Security Update), uninstall, reboot.
(Alternative: open CMD and enter wusa /uninstall /KB:3035583)
When you're offered the same again via Windows Update remember to hide it.
After uninstalling, if remnants of the update's files are still in Windows\System32\GWX, just delete that directory, although first you may need to take ownership of it.

**参考链接**: https://superuser.com/questions/922068/how-to-disable-the-get-windows-10-icon-shown-in-the-notification-area-tray

> 📎 来源 / Source: https://superuser.com/questions/922068/how-to-disable-the-get-windows-10-icon-shown-in-the-notification-area-tray

#### 25. How do you list all processes on the command line in Windows?

**故障现象**: How do you list all processes on the command line in Windows?
**标签 / 来源**: Tags: windows, command-line | superuser | 👍 387 | 💬 15 answers

**问题描述**:
Tags: windows, command-line | Score: 387 | Views: 1322569 | Answers: 15

**解决方法 / 社区答案**:
Working with cmd.exe:

tasklist

If you have Powershell:

get-process

Via WMI:

wmic process

(you can query remote machines as well with /node:ComputerOrIP, and there are a LOT more ways to customize this command: link)

**参考链接**: https://superuser.com/questions/914782/how-do-you-list-all-processes-on-the-command-line-in-windows

> 📎 来源 / Source: https://superuser.com/questions/914782/how-do-you-list-all-processes-on-the-command-line-in-windows

#### 26. How to recursively delete directory from command line in windows?

**故障现象**: How to recursively delete directory from command line in windows?
**标签 / 来源**: Tags: windows, command-line, cmd.exe | superuser | 👍 385 | 💬 8 answers

**问题描述**:
Tags: windows, command-line, cmd.exe | Score: 385 | Views: 958891 | Answers: 8

**解决方法 / 社区答案**:
deltree if I remember my DOS. 



It seems it's been updated... this is what you want:


  RMDIR /S


This removes the directory C:\test, with prompts :

rmdir c:\test /s


This does the same, without prompts :

rmdir c:\test /s /q


Regarding the sudo part of your question, if you need more priviliges, you can first open a new shell as another user account using the runas command, like this:

runas /user:Administrator cmd
rmdir c:\test /s /q

**参考链接**: https://superuser.com/questions/179660/how-to-recursively-delete-directory-from-command-line-in-windows

> 📎 来源 / Source: https://superuser.com/questions/179660/how-to-recursively-delete-directory-from-command-line-in-windows

#### 27. How to read ext4 partitions on Windows?

**故障现象**: How to read ext4 partitions on Windows?
**标签 / 来源**: Tags: windows, filesystems, ext4 | superuser | 👍 377 | 💬 12 answers

**问题描述**:
Tags: windows, filesystems, ext4 | Score: 377 | Views: 1033431 | Answers: 12

**解决方法 / 社区答案**:
Ext2Read works well. It can also open &amp; read disk images ( eg: Wubi disk images)


  Ext2Read is an explorer like utility
  to explore ext2/ext3/ext4 files. It
  now supports LVM2 and EXT4 extents. It
  can be used to view and copy files and
  folders. It can recursively copy
  entire folders. It can also be used to
  view and copy disk and file

**参考链接**: https://superuser.com/questions/37512/how-to-read-ext4-partitions-on-windows

> 📎 来源 / Source: https://superuser.com/questions/37512/how-to-read-ext4-partitions-on-windows

#### 28. Native alternative to wget in Windows PowerShell?

**故障现象**: Native alternative to wget in Windows PowerShell?
**标签 / 来源**: Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | superuser | 👍 362 | 💬 12 answers

**问题描述**:
Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | Score: 362 | Views: 684504 | Answers: 12

**解决方法 / 社区答案**:
Here's a simple PS 3.0 and later one-liner that works and doesn't involve much PS barf:

wget http://blog.stackexchange.com/ -OutFile out.html


Note that:


wget is an alias for Invoke-WebRequest
Invoke-WebRequest returns a HtmlWebResponseObject, which contains a lot of useful HTML parsing properties such as Links, Images, Forms, InputFields, etc., but in this case we're just using the raw Content
The file contents are stored in memory before writing to disk, making this approach unsuitable for downloading large files
On Windows Server Core installations, you'll need to write this as

wget http://blog.stackexchange.com/ -UseBasicParsing -OutFile out.html

Prior to Sep 20 2014, I suggested

(wget http://blog.stackexchange.com/).Content &gt;out.html


as an answer.  However, this doesn't work in all cases, as the &gt; operator (which is an alias for Out-File) converts the input to Unicode.


If you are using Windows 7, you will need to install version 4 or newer of the Windows Management Framework.

You may find that doing a $ProgressPreference = "silentlyContinue" before Invoke-WebRequest will significantly improve download speed with large files; this variable controls whether the progress UI is rendered.

**参考链接**: https://superuser.com/questions/362152/native-alternative-to-wget-in-windows-powershell

> 📎 来源 / Source: https://superuser.com/questions/362152/native-alternative-to-wget-in-windows-powershell

#### 29. Keyboard language keeps changing in Windows 10

**故障现象**: Keyboard language keeps changing in Windows 10
**标签 / 来源**: Tags: windows, windows-10, keyboard-layout | superuser | 👍 349 | 💬 9 answers

**问题描述**:
Tags: windows, windows-10, keyboard-layout | Score: 349 | Views: 543257 | Answers: 9

**解决方法 / 社区答案**:
In Windows 10, by default, pressing CTRL+SHIFT (or for some ALT+SHIFT - thanks madmenyo ) will cycle through any keyboard layouts that you might have mapped and it's surprisingly easy to do this by mistake.

If you keep pressing CTRL+SHIFT (or whatever you might have changed it to) then soon you should get back to the correct setting. (alternatively reboot which is what I did first time ;-) ) 

(Updated Aug 2019) You can change/disable this by

&gt; Settings &gt; search for 'typing' &gt; Advanced keyboard settings &gt; Language
&gt; Bar options &gt; Advanced Key Settings (tab) &gt; Change Key Sequence


Be warned, the above doesn't always work - Restarts and Sleep mode can both change keyboard default (usually to US) - I've found no cast-iron solution though creating a new profile can help, though not a particularly satisfactory answer IMHO.

In an emergency

WIN+R  
osk


to bring up the On Screen Keyboard might help temporarily.

Also note that it's possible to disable this so that no key combination will change the language - change the keys to "Not Assigned" - see answer below from Mort for more info

**参考链接**: https://superuser.com/questions/976947/keyboard-language-keeps-changing-in-windows-10

> 📎 来源 / Source: https://superuser.com/questions/976947/keyboard-language-keeps-changing-in-windows-10

#### 30. Why does virtualbox only have 32-bit option, no 64-bit option on Windows 7?

**故障现象**: Why does virtualbox only have 32-bit option, no 64-bit option on Windows 7?
**标签 / 来源**: Tags: windows, windows-7, virtualbox | superuser | 👍 349 | 💬 7 answers

**问题描述**:
Tags: windows, windows-7, virtualbox | Score: 349 | Views: 1389529 | Answers: 7

**解决方法 / 社区答案**:
Take a look: http://www.fixedbyvonnie.com/2014/11/virtualbox-showing-32-bit-guest-versions-64-bit-host-os/

If VirtualBox is only showing 32-bit versions in the Version list make sure:


You have an x64 CPU installed. (Optimally, a 64-bit OS should also be installed to receive acceptable virtualization performance.)
Hardware virtualization is enabled in the BIOS. (Your CPU must support it.)


For Intel x64: VT-x (Intel Virtualization Technology) and VT-d are both enabled
For AMD x64: AMD SVM (Secure Virtual Machine) is enabled

Hyper-V (or any other form of bare-metal hypervisor) is not installed

**参考链接**: https://superuser.com/questions/866962/why-does-virtualbox-only-have-32-bit-option-no-64-bit-option-on-windows-7

> 📎 来源 / Source: https://superuser.com/questions/866962/why-does-virtualbox-only-have-32-bit-option-no-64-bit-option-on-windows-7

#### 31. How to pin either a Shortcut or a Batch file to the new Windows 7, 8 and 10 Taskbar and start menu?

**故障现象**: How to pin either a Shortcut or a Batch file to the new Windows 7, 8 and 10 Taskbar and start menu?
**标签 / 来源**: Tags: windows-7, windows-8, windows-10, taskbar, shortcuts | superuser | 👍 344 | 💬 7 answers

**问题描述**:
Tags: windows-7, windows-8, windows-10, taskbar, shortcuts | Score: 344 | Views: 286084 | Answers: 7

**解决方法 / 社区答案**:
Create a shortcut to your batch file.
Get into shortcut property and change target to something like: cmd.exe /C "path-to-your-batch".
Simply drag your new shortcut to the taskbar. It should now be pinnable.

**参考链接**: https://superuser.com/questions/100249/how-to-pin-either-a-shortcut-or-a-batch-file-to-the-new-windows-7-8-and-10-task

> 📎 来源 / Source: https://superuser.com/questions/100249/how-to-pin-either-a-shortcut-or-a-batch-file-to-the-new-windows-7-8-and-10-task

#### 32. Conclusively stop wake timers from waking Windows 10 desktop

**故障现象**: Conclusively stop wake timers from waking Windows 10 desktop
**标签 / 来源**: Tags: windows-10, sleep, wake-on-lan | superuser | 👍 331 | 💬 3 answers

**问题描述**:
Tags: windows-10, sleep, wake-on-lan | Score: 331 | Views: 181507 | Answers: 3

**解决方法 / 社区答案**:
Summary
April 2022: I have made a new PowerShell script that will disable Windows' scheduled tasks to wake a device automatically. Use it alongside the other parts of this guide. Download it at:
https://github.com/seagull/disable-scheduledWaking
There are a number of things that can affect this. I'm aware there are posts all over this site detailing various different ways to approach the issue; this post aims to consolidate them and add my own insight into the issue as someone affected by it themselves.
The fix outlined in Step 2 can also be used to stop Windows 10 from rebooting the machine after installing Windows Updates.
This fix works for the Fall Update (1709) as well. You will need to disable the 'Reboot' task again and re-configure the security permissions, though, because the update process replaces it.
Step 1: Disable wake timers for all power profiles
Lazy tech-bloggers would have you believe this is the end of your search. While it's true that this step will eliminate a few errant shutdowns, there are a number of settings and configurations, particularly in Windows 10, that fail to respect this setting regardless of user intervention. Go to the Control Panel → Power Options. From here, pick whatever power profile is first on the list and disable 'Wake timers'. Work through all profiles.

Thanks to StackExchange user olee22 for the image.
On Windows 10, it is strongly recommended you fix this setting for all power profiles, not just the one you have chosen to use. Various Windows faculties will use different profiles; this improves your chances of not being woken up.
Step 2: Disable the unruly reboot scheduled task
Windows 10's UpdateOrchestrator scheduled task folder contains a task called &quot;reboot&quot;. This task will wake your computer up to install updates regardless of whether or not any are available. Simply removing its permission to wake the computer is not sufficient; Windows will just edit it to give itself permission again after you leave the Task Scheduler.
From your Control Panel, enter Administrative Tools, then view your Task Scheduler.


This is the task you want - under Task Scheduler Library → Microsoft → Windows → UpdateOrchestrator. The most important things you want to do are:


From here, you will need to alter the permissions for the task so that Windows cannot molest it. The task is located in C:\Windows\System32\Tasks\Microsoft\Windows\UpdateOrchestrator. It's called Reboot without a file extension. Right-click it, enter properties and make yourself the owner. Finally, configure it so that the following is shown:

Here the file is shown with read-only permissions for SYSTEM. Make it so that no account has write access, not even your own (you can always change permissions later if you need to). Please also ensure you disable any inherited permissions for the file from the Advanced button on this screen, to override any existing permissions on the root folder. This will 100% STOP Windows from messing with your changes after you've implemented them.
Once this has been set, you won't need to worry about that scheduled task any more.
If you don't have the Permissions to alter UpdateOrchestrator Tasks

Altering the UpdateOrchestrator's tasks now requires SYSTEM permissions, neither administrator nor TrustedInstaller permissions.

One of the ways of going around this is by:

Installing Microsoft's own PsTools.
Opening Command Prompt as and administrator and cd into your local PsTools folder.
Executing:
psexec.exe -i -s %windir%\system32\mmc.exe /s taskschd.msc


Going to the UpdateOrchestrator and disabling the Reboot task(s), as previously mentioned.

Note for Windows 1709 (Fall Creators' Update)
The Windows installation process changes permissions for files, so make sure you go through this guide again after upgrading.
I have heard reports that a new task is made called AC Power Install which requires the same steps applied to it, but I have not seen this task produced on my own device after installing the 16299.192 (2018-01 Meltdown patch) update so I cannot advise with absolute certainty. The same steps as performed above should work on any task that has been introduced.
Step 3: Check Wake Timers in PowerShell
You have disabled wake timer functionality, but Windows 10 has a habit of not respecting that setting, so to be safe, we're going to run a PowerShell command to weed out all tasks that can, feasibly, wake your PC. Open an Administrative PowerShell command prompt (Start, type 'Powershell', Ctrl+Shift+Enter) and place this command in the window:
Get-ScheduledTask | where {$_.settings.waketorun}

Go through all the tasks it lists and remove their permission to wake your computer. You shouldn't need to worry about permissions like we did with Reboot; that was an outlying case.
Step 4: Check what hardware can wake your PC
Lots of USB hardware, when engaged, has the ability to wake your PC (keyboards often do when keys are pressed for example); wake-on-LAN is typically also an issue in this scenario. For the uninitiated, a common and useful feature of modern hardware is called 'Wake on LAN'. If your device is attached to a local network by way of a wired Ethernet cable (it doesn't work for Wi-Fi) you can send communications through that will wake your PC up when received. It's a feature I use often but it must be brought into line, as its default behaviour is far too overzealous.
Enter the following command into an administrative command prompt:
powercfg -devicequery wake_armed


From here, find the devices in your Device Manager (Control Panel) and, under the Power Management tab, remove their ability to wake your computer up. If you have network interface cards that you want to keep Wake-on-LAN for, enable Only wake this device if it receives a magic packet as opposed to waking up for all traffic sent its way.
Step 5: Check the Group Policy just to be completely sure
Right-click your Start menu and select Run. Type in GPEdit.MSC. Find the following setting under Computer Configuration → Administrative Templates → Windows Components → Windows Updates → Enabling Windows Update Power Management to automatically wake up the system to install scheduled updates. Double-click it and set it to Disabled.

Step 6: Disable waking your machine up for automatic maintenance
Someone at Microsoft has a sense of humour for this one. If you're woken at night by your PC, the one thing you want to hear more than anything else is the hard drive crunching and grinding as it does a nightly defragmentation. Disable this feature by finding the Security and Maintenance section of the Control Panel. From there, expand Maintenance and look for the link to Change Maintenance settings.

Set the time to something more sociable (7PM is fine) and disable the machine's ability to wake itself up for the task.

**参考链接**: https://superuser.com/questions/973009/conclusively-stop-wake-timers-from-waking-windows-10-desktop

> 📎 来源 / Source: https://superuser.com/questions/973009/conclusively-stop-wake-timers-from-waking-windows-10-desktop

#### 33. Menu select item stuck on screen after context or command menu has closed

**故障现象**: Menu select item stuck on screen after context or command menu has closed
**标签 / 来源**: Tags: windows-7, windows, user-interface | superuser | 👍 327 | 💬 11 answers

**问题描述**:
Tags: windows-7, windows, user-interface | Score: 327 | Views: 324992 | Answers: 11

**解决方法 / 社区答案**:
The problem was introduced back in Windows 2000 when fading menu items were added. Originally, the feature was added in kernel-mode code and was tightly integrated into portions of the UI. Since it worked so well, it ended up staying there. The problem has appeared from time to time, but no one has had a reliable way to reproduce it in the kernel debugger to get it fixed.

The same effect can be achieved without changing the screen resolution or color depth.  Go to Start -> Run -> and type tskill dwm.  This command will reset the desktop window manager without the need to change the screen resolution.  

Changing the screen resolution or color depth also resets the desktop window manager, so it's always been a workaround for the bug when it appears. Either of these solutions will fix the problem.

**参考链接**: https://superuser.com/questions/57016/menu-select-item-stuck-on-screen-after-context-or-command-menu-has-closed

> 📎 来源 / Source: https://superuser.com/questions/57016/menu-select-item-stuck-on-screen-after-context-or-command-menu-has-closed

#### 34. How can I visualize the file system usage on Windows?

**故障现象**: How can I visualize the file system usage on Windows?
**标签 / 来源**: Tags: windows, file-management, disk-space, community-faq | superuser | 👍 321 | 💬 23 answers

**问题描述**:
Tags: windows, file-management, disk-space, community-faq | Score: 321 | Views: 215820 | Answers: 23

**解决方法 / 社区答案**:
WinDirStat is a port of KDirStat for Linux. It's free, lightweight, small (650kb installer), fast, portable (as a standalone .exe file), and works on multiple versions of Windows. Besides showing folders and percentages (for the entire disk or any subset of folders), it also displays an (optional) graphical usage map. Works well with NTFS Junction folders, avoiding counting folders multiple times.

**参考链接**: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

> 📎 来源 / Source: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

#### 35. Equivalent of cmd&#39;s &quot;where&quot; in powershell

**故障现象**: Equivalent of cmd&#39;s &quot;where&quot; in powershell
**标签 / 来源**: Tags: windows, powershell | superuser | 👍 318 | 💬 6 answers

**问题描述**:
Tags: windows, powershell | Score: 318 | Views: 257708 | Answers: 6

**解决方法 / 社区答案**:
Use the Get-Command commandlet passing it the name of the executable. It populates the Path property of the returned object (of type ApplicationInfo) with the fully resolved path to the executable. 

# ~&gt; (get-command notepad.exe).Path
C:\WINDOWS\system32\notepad.exe

**参考链接**: https://superuser.com/questions/675837/equivalent-of-cmds-where-in-powershell

> 📎 来源 / Source: https://superuser.com/questions/675837/equivalent-of-cmds-where-in-powershell

#### 36. Setting and getting Windows environment variables from the command prompt?

**故障现象**: Setting and getting Windows environment variables from the command prompt?
**标签 / 来源**: Tags: windows, command-line, environment-variables | superuser | 👍 317 | 💬 5 answers

**问题描述**:
Tags: windows, command-line, environment-variables | Score: 317 | Views: 1038784 | Answers: 5

**解决方法 / 社区答案**:
To make the environment variable accessible globally you need to set it in the registry. As you've realised by just using:


  set NEWVAR=SOMETHING


you are just setting it in the current process space.

According to this page you can use the setx command:


  setx NEWVAR SOMETHING


setx is built into Windows 7, but for older versions may only be available if you install the Windows Resource Kit

**参考链接**: https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt

> 📎 来源 / Source: https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt

#### 37. Is there a list of Windows special directories/shortcuts (like %TEMP%)?

**故障现象**: Is there a list of Windows special directories/shortcuts (like %TEMP%)?
**标签 / 来源**: Tags: windows, shortcuts, environment-variables, special-locations | superuser | 👍 314 | 💬 6 answers

**问题描述**:
Tags: windows, shortcuts, environment-variables, special-locations | Score: 314 | Views: 344813 | Answers: 6

**解决方法 / 社区答案**:
There are 156 run commands at mypchell.com.
Here is a more complete list including the Windows Environment Commands (e.g. %temp%, %HomeDrive%, etc)

Windows Environment Path Variables

%AllUsersProfile% - Open the All User's Profile C:\ProgramData
%AppData% - Opens AppData folder C:\Users\{username}\AppData\Roaming
%CommonProgramFiles% - C:\Program Files\Common Files
%CommonProgramFiles(x86)% - C:\Program Files (x86)\Common Files
%HomeDrive% - Opens your home drive C:\
%LocalAppData% - Opens local AppData folder C:\Users\{username}\AppData\Local
%ProgramData% - C:\ProgramData
%ProgramFiles% -  C:\Program Files or C:\Program Files (x86)
%ProgramFiles(x86)% - C:\Program Files (x86)
%Public% - C:\Users\Public
%SystemDrive% - C:
%SystemRoot% - Opens Windows folder C:\Windows
%Temp% - Opens temporary file Folder C:\Users\{Username}\AppData\Local\Temp
%UserProfile% - Opens your user's profile C:\Users\{username}
%AppData%\Microsoft\Windows\Start Menu\Programs\Startup - Opens Windows 10 Startup location for program shortcuts



Win+R

Run commands

Calc - Calculator
Cfgwiz32 - ISDN Configuration Wizard
Charmap - Character Map
Chkdisk - Repair damaged files
Cleanmgr - Cleans up hard drives
Clipbrd - Windows Clipboard viewer
Cmd - Opens a new Command Window (cmd.exe)
Control - Displays Control Panel
Dcomcnfg - DCOM user security
Debug - Assembly language programming tool
Defrag - Defragmentation tool
Drwatson - Records programs crash &amp; snapshots
Dxdiag - DirectX Diagnostic Utility
Explorer - Windows Explorer
Fontview - Graphical font viewer
Ftp - ftp.exe program
Hostname - Returns Computer's name
Ipconfig - Displays IP configuration for all network adapters
Jview - Microsoft Command-line Loader for Java classes
MMC - Microsoft Management Console
Msconfig - Configuration to edit startup files
Msinfo32 - Microsoft System Information Utility
Nbtstat - Displays stats and current connections using NetBios over TCP/IP
Netstat - Displays all active network connections
Nslookup - Returns your local DNS server
Odbcad32 - ODBC Data Source Administrator
Ping - Sends data to a specified host/IP
Regedit - registry Editor
Regsvr32 - register/de-register DLL/OCX/ActiveX
Regwiz - Registration wizard
Sfc /scannow - System File Checker
Sndrec32 - Sound Recorder
Sndvol32 - Volume control for soundcard
Sysedit - Edit system startup files (config.sys, autoexec.bat, win.ini, etc.)
Systeminfo - display various system information in text console
Taskmgr - Task manager
Telnet - Telnet program
Taskkill - kill processes using command line interface
Tskill - reduced version of Taskkill from Windows XP Home
Tracert - Traces and displays all paths required to reach an internet host
Winchat - simple chat program for Windows networks
Winipcfg - Displays IP configuration  

Microsoft Office suite

winword - Microsoft Word
excel - Microsoft Excel
powerpnt - Microsoft PowerPoint
msaccess - Microsoft Access
outlook - Microsoft Outlook
ois - Microsoft Picture Manager
winproj - Microsoft Project 

Management Consoles

certmgr.msc - Certificate Manager
ciadv.msc - Indexing Service
compmgmt.msc - Computer management
devmgmt.msc - Device Manager
dfrg.msc - Defragment
diskmgmt.msc - Disk Management
fsmgmt.msc - Folder Sharing Management
eventvwr.msc - Event Viewer
gpedit.msc - Group Policy (&lt; XP Pro)
iis.msc - Internet Information Services
lusrmgr.msc - Local Users and Groups
mscorcfg.msc - Net configurations
ntmsmgr.msc - Removable Storage
perfmon.msc - Performance Manager
secpol.msc - Local Security Policy
services.msc - System Services
wmimgmt.msc - Windows Management   

Control Panel utilities

access.cpl - Accessibility Options
hdwwiz.cpl - Add New Hardware Wizard
appwiz.cpl - Add/Remove Programs
timedate.cpl - Date and Time Properties
desk.cpl - Display Properties
inetcpl.cpl - Internet Properties
joy.cpl - Joystick Properties
main.cpl keyboard - Keyboard Properties
main.cpl - Mouse Properties
ncpa.cpl - Network Connections
ncpl.cpl - Network Properties
telephon.cpl - Phone and Modem options
powercfg.cpl - Power Management
intl.cpl - Regional settings
mmsys.cpl sounds - Sound Properties
mmsys.cpl - Sounds and Audio Device Properties
sysdm.cpl - System Properties
nusrmgr.cpl - User settings
firewall.cpl - Firewall Settings (sp2)
wscui.cpl - Security Center (sp2)
Wupdmgr - Takes you to Microsoft Windows Update   

Thanks to The New Tech for the original forum posting.

**参考链接**: https://superuser.com/questions/217504/is-there-a-list-of-windows-special-directories-shortcuts-like-temp

> 📎 来源 / Source: https://superuser.com/questions/217504/is-there-a-list-of-windows-special-directories-shortcuts-like-temp

#### 38. Can I completely disable Cortana on Windows 10?

**故障现象**: Can I completely disable Cortana on Windows 10?
**标签 / 来源**: Tags: windows-10, cortana | superuser | 👍 314 | 💬 9 answers

**问题描述**:
Tags: windows-10, cortana | Score: 314 | Views: 1744192 | Answers: 9

**解决方法 / 社区答案**:
Update 2018: Warning about Taskbar Breakage

I just reinstalled Windows 10 Pro and followed all the prescribed steps (both removing Cortana and removing all store apps) and it still works as prescribed. 

It bears mentioning that removing Cortana will break the Default Taskbar in weird ways. It doesn't break Windows Search - so Explorer search still works in my experience.

I've, personally, always replaced the default taskbar with Classic Start (linked via Ninite installer) and have no issues in day-to-day Windows usage otherwise.

Update: Remove Cortana via "TakeOwn"

Apparently, this trick stopped working at some point. I've used @Meferdati's link at some point successfully: winaero: how to uninstall Cortona. It contains a script that does all the work for you, as well as an explanation of how it works.

Below are the steps I've been using, which are very similar to @MC10's answer, except I've always had to "TakeOwn" to get permissions and I move my files to a different folder (instead of deleting - in case I decide to revert):


add TakeOwn to the context menu or (use takeown from the command line).
Navigate to C:\Windows
Create folder SystemApps.bak
Use Takeown to gain ownership of c:\windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy
(Gain ownership of anything else you want to move)
Cut/Paste the folder(s) from SystemApps to SystemApps.bak
When the "Permissions" pop-up appears, switch to Task Manager
Kill SearchUI.exe process
Switch back and give permission to move the folder


The folder is now in SystemsApps.bak - and you can simply move it back if the need arises.

Original: Remove Cortana via Powershell RemoveAppPackage

First disable it, then uninstall the Cortana app.

Disable it in the search settings:


Click the search icon/box in the bottom left
click the gear on the left bar
Click off next to Cortana/Web Searches




Then uninstall it, as listed here:

In elevated PowerShell:

Get-AppxPackage | Select Name, PackageFullName
Remove-AppxPackage Microsoft.Windows.Cortana_1.4.8.176_neutral_neutral_cw5n1h2txyewy


This is similar to MC10's answer, except that I'm sure the OS will be more accepting of uninstalling it via the "proper channels" (powershell) instead of renaming the folder.

Windows has fixed it so now you cannot remove "...Cortana_1.6.1.52_ ...". When this is attempted it states this is part of Windows now and cannot be removed. I guess I will go back to renaming the folder.

I'm using the same uninstall to remove other "features" like BingNews, BingSports, Etc

Edit: Likewise, you can remove the "Provisioned" applications (aka: crap that gets installed per user) via this method

Get-AppxProvisionedPackage -Online | Select DisplayName, PackageName
Remove-AppxProvisionedPackage  Microsoft.ZuneMusic_2019.6.11821.0_neutral_~_8wekyb3d8bbwe


Or... to remove ALL Apps that you can, app or provisionedapp, you can do this:

Just a warning: This will uninstall the Windows Store. That's not an issue for me, but uninstalling everything isn't for the faint of heart.

Get-AppxPackage | Remove-AppxPackage
Get-AppxProvisionedPackage -Online | Remove-AppxProvisionedPackage -online


As mentioned in comments, it's probably wise not to completely remove the Windows Store. I haven't tried this yet, but this (in the comments) looks to be ballpark of what I'd use:

Get-AppxPackage -AllUsers | where-object {$_.name –notlike "*store*"} | Remove-AppxPackage
Get-appxprovisionedpackage –online | where-object {$_.packagename –notlike "*store*"} | Remove-AppxProvisionedPackage -online


Further resource: Delete Windows 10 Apps and Restore Default Windows 10 Apps

**参考链接**: https://superuser.com/questions/949569/can-i-completely-disable-cortana-on-windows-10

> 📎 来源 / Source: https://superuser.com/questions/949569/can-i-completely-disable-cortana-on-windows-10

#### 39. Using cd command in Windows command line, can&#39;t navigate to D:\

**故障现象**: Using cd command in Windows command line, can&#39;t navigate to D:\
**标签 / 来源**: Tags: windows, command-line, path, cd | superuser | 👍 311 | 💬 9 answers

**问题描述**:
Tags: windows, command-line, path, cd | Score: 311 | Views: 1488450 | Answers: 9

**解决方法 / 社区答案**:
Going back to the days of DOS, there's a separate "current directory" for each drive.  cd D:\foldername changes D:'s current directory to the foldername specified, but does not change the fact that you're still working on the C: drive.

What you want is simple:

D:


Here you can see how the "separate current directory for each drive" thing works:

C:\Users\coneslayer&gt;e:

E:\&gt;c:

C:\Users\coneslayer&gt;cd e:\software

C:\Users\coneslayer&gt;e:

e:\Software&gt;

**参考链接**: https://superuser.com/questions/135214/using-cd-command-in-windows-command-line-cant-navigate-to-d

> 📎 来源 / Source: https://superuser.com/questions/135214/using-cd-command-in-windows-command-line-cant-navigate-to-d

#### 40. How to move windows that open up offscreen?

**故障现象**: How to move windows that open up offscreen?
**标签 / 来源**: Tags: windows, multiple-monitors, window-manager | superuser | 👍 309 | 💬 24 answers

**问题描述**:
Tags: windows, multiple-monitors, window-manager | Score: 309 | Views: 728598 | Answers: 24

**解决方法 / 社区答案**:
I use this approach:


Use Alt+Tab to switch to the off-screen application.
Press Alt+SPACE to bring up the system menu (you won't see it because it is off screen)
Press R to select the "Restore" menu choice to ensure the windows isn't maximized (you cannot move it if it is maximized)
Press Alt+SPACE again, then M to select the "Move" menu choice.
Press one of the arrow keys to initiate the movement.
Now just use the mouse  to place the window where you want.


If you are using a non-English version of Windows, the "R" and "M" menu choices will probably be different.

**参考链接**: https://superuser.com/questions/53585/how-to-move-windows-that-open-up-offscreen

> 📎 来源 / Source: https://superuser.com/questions/53585/how-to-move-windows-that-open-up-offscreen

#### 41. How to quickly move current window to another Task View / desktop in Windows 10?

**故障现象**: How to quickly move current window to another Task View / desktop in Windows 10?
**标签 / 来源**: Tags: windows, windows-10 | superuser | 👍 305 | 💬 17 answers

**问题描述**:
Tags: windows, windows-10 | Score: 305 | Views: 291045 | Answers: 17

**解决方法 / 社区答案**:
I think for a quicker switch this should be in the titlebar, so I created a tool for that:

https://github.com/Eun/MoveToDesktop



You can also move windows by using WIN+ALT+Left/Right or change the shortcut as needed.

**参考链接**: https://superuser.com/questions/950452/how-to-quickly-move-current-window-to-another-task-view-desktop-in-windows-10

> 📎 来源 / Source: https://superuser.com/questions/950452/how-to-quickly-move-current-window-to-another-task-view-desktop-in-windows-10

#### 42. How to mess up a PC running Windows 7?

**故障现象**: How to mess up a PC running Windows 7?
**标签 / 来源**: Tags: windows-7, windows, security | superuser | 👍 303 | 💬 27 answers

**问题描述**:
Tags: windows-7, windows, security | Score: 303 | Views: 118517 | Answers: 27

**解决方法 / 社区答案**:
A few major problems for you, 


In bios disable the processors L2 cache - Machine crawls
Windows+break-->advanced system settings --> hardware tab --> Device Manager, right click disable mouse (make sure you can get here with just your keyboard so you can undo this!)
ctrl+alt + Arrow key - on some graphics cards this rotates the screen. (usually with no method of undoing this unless you know this shortcut)
Make a floppy boot disc/usb Key/CD Rom, pop it in the floppy drive and ensure its set to first in the boot order in bios (bonus points for removing the hdd from boot list and creating all 3 boot discs with a different os on each so they fix one then get the next!)
Use a partitioning tool to shrink the hdd partition to a few mb more than is currently in use
Do the opposite and fill up available space with multiple copies of large files.  Combined with a startup script to start the copies would keep the hard drive filled if they first attempted cleanup by deleting files.


And a few irritations to garnish the pc with


If it had internet access - Open Internet Properties --> connections Tab -->Lan Settings, Check use a proxy server, set the address to 127.0.0.1 (prevents them googling for solutions :P)
Right click on desktop - View - uncheck show desktop icons (irritating but not tough to fix)
sticky tape on the bottom of the mouse can disrupt the laser stopping the mouse working (couple this with the major disabling of the mouse in device manager to add confusion).
if the connectors are ps2, swap the mouse and keyboard, obvious if you're used to hardware but passes a quick glance from a noob
In word Office button -->Word Options --> proofing --> AutoCorrect Options --> add a few entries for common words, subtlety is your friend, is --> was the --> teh etc (2k7 instructions but can be done via different route in most versions)


Reverse the steps to undo the problems and ask in comments if you have trouble!

Edit - as we may have had our beastly BIOS tricks taken from us here's a couple more windows based ones

Put the shutdown command into autoexec.bat Command syntax here (you've talked about putting similar functionality in the startup folder, so this should confuse em by doing the same thing from a different spot)

Fork bomb! Create a .bat file containing the following text and make it autorun (either call from autoexec.bat or drop the .bat in startup folder)

:s
start %0
goto s


This will spawn huge numbers of processes untill the machine grinds to a halt (The code is untested but looks viable)

**参考链接**: https://superuser.com/questions/275894/how-to-mess-up-a-pc-running-windows-7

> 📎 来源 / Source: https://superuser.com/questions/275894/how-to-mess-up-a-pc-running-windows-7

#### 43. How to automatically reload modified files in Notepad++

**故障现象**: How to automatically reload modified files in Notepad++
**标签 / 来源**: Tags: windows, notepad++, text-editors | superuser | 👍 295 | 💬 6 answers

**问题描述**:
Tags: windows, notepad++, text-editors | Score: 295 | Views: 247823 | Answers: 6

**解决方法 / 社区答案**:
You can disable the confirmation in the settings:

Settings -&gt; Preferences -&gt; MISC. -&gt; Update silently

**参考链接**: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

> 📎 来源 / Source: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

#### 44. Equivalent of Linux `touch` to create an empty file with PowerShell

**故障现象**: Equivalent of Linux `touch` to create an empty file with PowerShell
**标签 / 来源**: Tags: windows, windows-8, powershell, powershell-3.0 | superuser | 👍 293 | 💬 14 answers

**问题描述**:
Tags: windows, windows-8, powershell, powershell-3.0 | Score: 293 | Views: 420048 | Answers: 14

**解决方法 / 社区答案**:
Using the append redirector ">>" resolves the issue where an existing file is deleted:

echo $null &gt;&gt; filename

**参考链接**: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

> 📎 来源 / Source: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

#### 45. How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?

**故障现象**: How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?
**标签 / 来源**: Tags: windows, windows-10, windows-explorer, windows-10-preview | superuser | 👍 291 | 💬 5 answers

**问题描述**:
Tags: windows, windows-10, windows-explorer, windows-10-preview | Score: 291 | Views: 256078 | Answers: 5

**解决方法 / 社区答案**:
As of build 9926 (at least - it may have been an earlier build), this is configurable via the GUI.

Open Explorer and go to View, then click Options (or Change folder and search options). In General tab you can change Open File Explorer to This PC

**参考链接**: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

> 📎 来源 / Source: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

#### 46. How can I reduce the consumption of the `vmmem` process?

**故障现象**: How can I reduce the consumption of the `vmmem` process?
**标签 / 来源**: Tags: windows-10, memory, docker, resources | superuser | 👍 273 | 💬 15 answers

**问题描述**:
Tags: windows-10, memory, docker, resources | Score: 273 | Views: 569297 | Answers: 15

**解决方法 / 社区答案**:
Daniiel B is on the money. To turn off Vmmem simply go into Powershell or whatever terminal you like to use under admin rights and enter the command wsl --shutdown, when your done with playing in wsl1/2.

**参考链接**: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

> 📎 来源 / Source: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

#### 47. How can I execute a Windows command line in background?

**故障现象**: How can I execute a Windows command line in background?
**标签 / 来源**: Tags: windows, command-line | superuser | 👍 270 | 💬 12 answers

**问题描述**:
Tags: windows, command-line | Score: 270 | Views: 889339 | Answers: 12

**解决方法 / 社区答案**:
This is a little late but I just ran across this question while searching for the answer myself and I found this:

START /B program


which, on Windows, is the closest to the Linux command:

program &amp;


From the console HELP system:

C:\&gt;HELP START

Starts a separate window to run a specified program or command.

START ["title"] [/D path] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
      [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
      [/NODE &lt;NUMA node&gt;] [/AFFINITY &lt;hex affinity mask&gt;] [/WAIT] [/B]
      [command/program] [parameters]

    "title"     Title to display in window title bar.
    path        Starting directory.
    B           Start application without creating a new window. The
                application has ^C handling ignored. Unless the application
                enables ^C processing, ^Break is the only way to interrupt
                the application.


One problem I saw with it is that  you have more than one program writing to the console window, it gets a little confusing and jumbled.

To make it not interact with the user, you can redirect the output to a file:

START /B program &gt; somefile.txt

**参考链接**: https://superuser.com/questions/198525/how-can-i-execute-a-windows-command-line-in-background

> 📎 来源 / Source: https://superuser.com/questions/198525/how-can-i-execute-a-windows-command-line-in-background

#### 48. How do I change the language of all Powerpoint slides at once?

**故障现象**: How do I change the language of all Powerpoint slides at once?
**标签 / 来源**: Tags: windows, microsoft-office, microsoft-powerpoint, language, microsoft-powerpoint-2010 | superuser | 👍 268 | 💬 9 answers

**问题描述**:
Tags: windows, microsoft-office, microsoft-powerpoint, language, microsoft-powerpoint-2010 | Score: 268 | Views: 572691 | Answers: 9

**解决方法 / 社区答案**:
To change the language of the entire PowerPoint easily, open the View tab and select the Outline view.

Now press


Ctrl+A to select all.
Tools → Language → Choose your language to set.


Likewise while you have everything selected you can change other things like fonts, colours etc. Although of course in many case this is better done by changing the slide master, a presentation that has had many editors may have lots of 'hard' formatting set which deviates from the underlying master and needs resetting to be consistent. You can also reset individual slides to the master style, but this may result in placeholders moving as well, which may be undesirable in some situations.

PowerPoint 2013


View → Outline → select all slides (in a left menu) via Ctrl+A.
Review → Language → Set Proofing Language... → Choose your language to set.


As for me - PowerPoint restart was needed. 
Probably because I also did changed Editing Language:


Review → Language → Set Proofing Language... → Language Preferences → Choose Editing Languages.

**参考链接**: https://superuser.com/questions/432366/how-do-i-change-the-language-of-all-powerpoint-slides-at-once

> 📎 来源 / Source: https://superuser.com/questions/432366/how-do-i-change-the-language-of-all-powerpoint-slides-at-once

#### 49. How can I check the temperature of my CPU in Windows?

**故障现象**: How can I check the temperature of my CPU in Windows?
**标签 / 来源**: Tags: windows, cpu, temperature | superuser | 👍 267 | 💬 10 answers

**问题描述**:
Tags: windows, cpu, temperature | Score: 267 | Views: 2706360 | Answers: 10

**解决方法 / 社区答案**:
Actually this information is given to OS by the BIOS, but you will need an application to expose the information. You can find a lot of applications to do this:

Realtemp
CPU thermomether
Core Temp

**参考链接**: https://superuser.com/questions/395434/how-can-i-check-the-temperature-of-my-cpu-in-windows

> 📎 来源 / Source: https://superuser.com/questions/395434/how-can-i-check-the-temperature-of-my-cpu-in-windows

#### 50. How to list Chocolatey packages already installed and newer version available from the command line

**故障现象**: How to list Chocolatey packages already installed and newer version available from the command line
**标签 / 来源**: Tags: windows, command-line, chocolatey | superuser | 👍 267 | 💬 4 answers

**问题描述**:
Tags: windows, command-line, chocolatey | Score: 267 | Views: 312130 | Answers: 4

**解决方法 / 社区答案**:
Note: You likely need to do the following commands in an administrative cmd/powershell prompt.

If you have choco 0.9.9.6+, you can use the outdated command.

choco outdated


If you have 0.9.9+ installed:

choco upgrade all --noop


If you have version 0.9.8.33 or below installed:

choco version all


Following that, if you actually want to upgrade - you can follow with:

cup all -y


Note: -y will only work with 0.9.8.33+.

**参考链接**: https://superuser.com/questions/890251/how-to-list-chocolatey-packages-already-installed-and-newer-version-available-fr

> 📎 来源 / Source: https://superuser.com/questions/890251/how-to-list-chocolatey-packages-already-installed-and-newer-version-available-fr

#### 51. Why is Google so much faster than a hard-drive search?

**故障现象**: Why is Google so much faster than a hard-drive search?
**标签 / 来源**: Tags: windows, hard-drive, windows-search, google-search | superuser | 👍 265 | 💬 10 answers

**问题描述**:
Tags: windows, hard-drive, windows-search, google-search | Score: 265 | Views: 43966 | Answers: 10

**解决方法 / 社区答案**:
Google is not searching the internet: it is searching an index. Google has huge server farms which are constantly scanning and indexing the internet. This process takes a lot of time, just like the search of your unindexed hard drive. In Windows 7, there is an option to index your hard drives. This process takes some time at first but once it is up and running the results of a search will be instantaneous.

If you want to know more about how the Google search works you can read Google's article "How Search Works" or read the article "How Stuff Works: How Google Works".

**参考链接**: https://superuser.com/questions/577502/why-is-google-so-much-faster-than-a-hard-drive-search

> 📎 来源 / Source: https://superuser.com/questions/577502/why-is-google-so-much-faster-than-a-hard-drive-search

#### 52. Windows equivalent of whereis?

**故障现象**: Windows equivalent of whereis?
**标签 / 来源**: Tags: windows, command-line | superuser | 👍 259 | 💬 11 answers

**问题描述**:
Tags: windows, command-line | Score: 259 | Views: 243680 | Answers: 11

**解决方法 / 社区答案**:
The where command does what you want and goes back at least to the resource kit for Windows 98, and is included by default in Server 2003, Vista, and newer:

C:\&gt;where csc
C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe
C:\Windows\Microsoft.NET\Framework\v2.0.50727\csc.exe


If executed with no arguments (on Vista), it results in one of my favorite messages:

C:\&gt;where
ERROR: The operation completed successfully.


If executing in PowerShell, be sure to include '.exe' to distinguish from any 'where' aliases or scripts along the path. ('where' is a typical alias for Where-Object.ps1)

C:\&gt; where.exe where.exe
C:\Windows\System32\where.exe

**参考链接**: https://superuser.com/questions/21067/windows-equivalent-of-whereis

> 📎 来源 / Source: https://superuser.com/questions/21067/windows-equivalent-of-whereis

#### 53. Windows equivalent of the Linux command &#39;touch&#39;?

**故障现象**: Windows equivalent of the Linux command &#39;touch&#39;?
**标签 / 来源**: Tags: windows, file-attributes, touch | superuser | 👍 257 | 💬 32 answers

**问题描述**:
Tags: windows, file-attributes, touch | Score: 257 | Views: 532320 | Answers: 32

**解决方法 / 社区答案**:
If you want to touch the date stamp of a file using windows, use the following command at the command prompt:
copy /b filename.ext +,,

(where filename.ext is your file's name). The +,, is a special flag to copy telling it to simply update the date/time on the file:

* Changing the time and date of a file
If you want to assign the current time and date to a file without modifying the file, use the following syntax:
copy /b Source+,,
The commas indicate the omission of the Destination parameter.

Edit based on comments by Lumi and Justin: put this in a batch file, eg. touch.cmd
@COPY /B %1+,, %1

This works even if the file is not in the current directory (tested on Windows 7).

**参考链接**: https://superuser.com/questions/10426/windows-equivalent-of-the-linux-command-touch

> 📎 来源 / Source: https://superuser.com/questions/10426/windows-equivalent-of-the-linux-command-touch

#### 54. How to search inside files on Windows 7?

**故障现象**: How to search inside files on Windows 7?
**标签 / 来源**: Tags: windows-7, windows, windows-search, file-filter | superuser | 👍 255 | 💬 13 answers

**问题描述**:
Tags: windows-7, windows, windows-search, file-filter | Score: 255 | Views: 833086 | Answers: 13

**解决方法 / 社区答案**:
To get to the Indexing Options:  

Start --> Control Panel --> Indexing Options 

See Change advanced indexing options for more information.

If you click on the Advanced button in Indexing Options and go to the File Types tab, you will get a list of file types and the way they are indexed. For the file types you want, you can specify that you want the file contents indexed, and not just the file properties.

Or you can just do a normal search, and after the search is finished you can click on the "File Contents" button under the "Search again in" field (which is located after the end of the search results list, if you scroll to the bottom).

Based on this page, the "File Contents" option won't always show up - only when the folder being searched is not marked for file content indexing; in that case, file contents are supposedly searched automatically, without having to specify this option explicitly.

**参考链接**: https://superuser.com/questions/60173/how-to-search-inside-files-on-windows-7

> 📎 来源 / Source: https://superuser.com/questions/60173/how-to-search-inside-files-on-windows-7

#### 55. Refresh Icon Cache Without Rebooting

**故障现象**: Refresh Icon Cache Without Rebooting
**标签 / 来源**: Tags: windows, windows-explorer, icons, cache | superuser | 👍 251 | 💬 13 answers

**问题描述**:
Tags: windows, windows-explorer, icons, cache | Score: 251 | Views: 408444 | Answers: 13

**解决方法 / 社区答案**:
Yes.

You can just run the following command to clear the icon cache:

ie4uinit.exe -ClearIconCache


For Windows 10, use:

ie4uinit.exe -show




Check this video for a demo.

[tip credit]

**参考链接**: https://superuser.com/questions/499078/refresh-icon-cache-without-rebooting

> 📎 来源 / Source: https://superuser.com/questions/499078/refresh-icon-cache-without-rebooting

#### 56. Kill a process which says &quot;Access denied&quot;

**故障现象**: Kill a process which says &quot;Access denied&quot;
**标签 / 来源**: Tags: windows-7, windows, 64-bit | superuser | 👍 251 | 💬 11 answers

**问题描述**:
Tags: windows-7, windows, 64-bit | Score: 251 | Views: 1111843 | Answers: 11

**解决方法 / 社区答案**:
Kill a protected process?

http://processhacker.sourceforge.net/index.php

Works on Windows Server without admin rights! Yammie! :)

**参考链接**: https://superuser.com/questions/109010/kill-a-process-which-says-access-denied

> 📎 来源 / Source: https://superuser.com/questions/109010/kill-a-process-which-says-access-denied

#### 57. Troubleshoot High CPU usage by the &quot;System&quot; process

**故障现象**: Troubleshoot High CPU usage by the &quot;System&quot; process
**标签 / 来源**: Tags: windows, windows-8, performance, troubleshooting, cpu-usage | superuser | 👍 243 | 💬 6 answers

**问题描述**:
Tags: windows, windows-8, performance, troubleshooting, cpu-usage | Score: 243 | Views: 753727 | Answers: 6

**解决方法 / 社区答案**:
Introduction
High CPU usage by the &quot;System&quot; process can often be caused by a hardware driver issue (bug, old version, incompatility etc).
The System process loads (or hosts) multiple hardware drivers from different vendors that require higher level of memory access.   This is why diagnosing the specific culprit can require a bit of detective work as described below.
Diagnosing the issue
To diagnose the CPU usage issues, you should use Event Tracing for Windows (ETW) to capture CPU Sampling data / Profile.
To capture the data, install the Windows Performance Toolkit, which is part of the Windows SDK.
The Windows 10 WPT can be used on Windows 8/Server 2012, Windows 8.1/Server 2012R2 and Windows 10/Server 2016. If you still use Windows 7, use the SDK/WPT with Build 15086.

(all other entries can be unselected)
Now run WPRUI.exe, select First Level, under  Resource select CPU usage and click on start.

Now capture 1 minute of the CPU usage. After 1 minute, click on Save.
Now analyze the generated ETL file with the Windows Performance Analyzer by dragging and dropping the CPU Usage (sampled) graph to the analysis pane and ordering the columns like you see in the picture:

Inside WPA, load the debug symbols and expand Stack of the SYSTEM process. In this demo, the CPU usage comes from the nVIDIA driver.

In the following demo, the CPU usage comes from the Realtek NIC driver:


When you see calls like ntoskrnl.exe!ViKeTrimWorkerThreadRoutine, ntoskrnl.exe!MmVerifierTrimMemory, ntoskrnl.exe!VerifierKeLeaveCriticalRegion, this means you have Driver Verifier enabled. This also hurts performance a lot and causes high SYSTEM usage. Disable Driver Verifier and reboot.


In this demo, the driver iai2ce.sys (Intel Serial IO GPIO Controller driver) causes it:


In this example, the CPU usage comes from the file rtsuvc.sys which seems to be the Realtek UVC webcam Driver


This demo shows that Bitdefender driver ignis.sys


In the following example, the CPU usage is casued by the broadcom network driver bcmwl664.sys


When you see ntoskrnl.exe!MiZeroWorkerPages as cause, it is trickier. This means the function of the kernel which zeros the memory before it can be used again causes the high CPU usage:

There is no real way to detect which process causes it, but I know that Chrome can cause it if you have hardware acceleration enabled in Chrome. So if you see this and use Chrome, turn hardware acceleration in Chrome off.

When you see those ntoskrnl.exe!RtlpGenericRandomPatternWorker, ntoskrnl.exe!RtlpTestMemoryRandomUp calls

the CPU usage comes from the Kernel to test memory for issues (memtest). This usage is triggered via the idle maintenance task of Windows 8.1/10. You can use Task Scheduler to disable the idle task.

In Windows 10, the task is called RunFullMemoryDiagnostics under Microsoft &gt; Windows &gt; MemoryDiagnostic &gt; RunFullMemoryDiagnostic.


In this case, the CPU usage seems to come from the Data Deduplication Feature (dedup.sys!DdpPostCreate) of Windows Server:


In this demo, the CPU usage is caused by the WIFI card driver athrx.sys

Search for a driver update if you see this.

In the following demo, a citrix driver is involved:

So contact your IT for how to solve Citrix issues.

In this demo, the function usbhub.sys!UsbhPortRecycle causes the CPU usage:

Changing USB2.0 ports to 1.1 speed or connecting USB drives to other USB 2.0 ports helped for some users.

In this case, a small amount of SYSTEM usage comes from the Acronis driver tdrpm251.sys:


In this demo, the CPU usage ntoskrnl.exe!KeAcquireSpinLockRaiseToDpc and ntoskrnl.exe!KeReleaseSpinLock.

so a driver is using SpinLocks very heavily. Disable some devices/drivers until you see one which causes it.

In this case, the CPU usage is caused by the driver L1C62x64.sys

This is the qualcomm atheros AR8171/8175 PCI-E gigabit Ethernet driver. So update the driver if you see it in the stack.

Here, the CPU usage comes from scanning the host file (netbt.sys!DelayedScanLmHostFile)

make sure your hosts file is not too large to avoid this usage.

In this case, the CPU usage comes from SRTSP64.SYS from symantec.

Update your used symantec product to the latest version.

Here, the CPU usage comes from the AMD GPU driver (atikmdag.sys)

if you see this, go to AMD site and get the latest driver for your AMD card.

Here, the drivers TMXPFlt.sys and  VsapiNt.sys cause the high CPU usage.

From what I see, those files are part of Trend Micro AV suite. Update the tool or remove it.

In this example, the CPU usage comes from the function ntoskrnl.exe!MmGetPageFileInformation

This function gets information about the pagefile.

Routine Description:
This routine returns information about the currently active paging
files.

Disable the pagefile, reboot and enable it again and see if this fixes it. Also, removing Intel services (e.g Intel Content Protection HECI Service) seems to fixed it for a user.

Here, you can see that the driver Netwtw04.sys (Intel Wifi driver) calls the function flushCompleteAllPendingFlushRequests and this causes a high CPU usage.

Because the debug symbols get loaded the Windows inbox driver is used. Only here we can get debug symbols to see the callstack with the function name flushCompleteAllPendingFlushRequests.
Here, you should install the latest driver from Intel to fix it.

The most complicated case of SYSTEM usage is ACPI.sys usage in the callstack:
Line #, DPC/ISR, Module, Stack, Count, Process, Weight (in view) (ms), TimeStamp (s), % Weight
6, , ,   |    |- ACPI.sys!ACPIWorkerThread, 40246, , 39.992,941063, , 4,13
7, , ,   |    |    ACPI.sys!RestartCtxtPassive, 40246, , 39.992,941063, , 4,13
8, , ,   |    |    ACPI.sys!InsertReadyQueue, 40246, , 39.992,941063, , 4,13
9, , ,   |    |    ACPI.sys!RunContext, 40246, , 39.992,941063, , 4,13
10, , ,   |    |    ntoskrnl.exe!KeReleaseSpinLock, 40246, , 39.992,941063, , 4,13
11, , ,   |    |    ntoskrnl.exe!KiDpcInterrupt, 40246, , 39.992,941063, , 4,13
12, , ,   |    |    ntoskrnl.exe!KiDispatchInterruptContinue, 40246, , 39.992,941063, , 4,13
13, , ,   |    |    ntoskrnl.exe!KxRetireDpcList, 40246, , 39.992,941063, , 4,13
14, , ,   |    |    ntoskrnl.exe!KiRetireDpcList, 40246, , 39.992,941063, , 4,13
15, , ,   |    |    |- ntoskrnl.exe!KiExecuteAllDpcs, 40198, , 39.945,173325, , 4,13
16, , ,   |    |    |    |- ACPI.sys!ACPIInterruptDispatchEventDpc, 27565, , 27.408,930428, , 2,83
17, , ,   |    |    |    |    |- ACPI.sys!ACPIGpeEnableDisableEvents, 24525, , 24.384,921620, , 2,52
18, , ,   |    |    |    |    |    ACPI.sys!ACPIWriteGpeEnableRegister, 24525, , 24.384,921620, , 2,52
19, , ,   |    |    |    |    |    |- hal.dll!HalpAcpiPmRegisterWrite, 24421, , 24.281,015516, , 2,51
20, , ,   |    |    |    |    |    |    |- hal.dll!HalpAcpiPmRegisterWritePort, 24166, , 24.027,316013, , 2,48

this is extremely difficult to debug. In a sysinternals topic, I listed some advice:

make sure the CPU doesn't overheat because of dust in the CPU fan
update or re-flash the (same) BIOS/UEFI
load default BIOS/UEFI settings
make sure the battery is not damaged, remove the battery from the notebook or disable the battery in device manager.
change jumper on HDD caddy if you have replaced the DVD/Blue-Ray Drive with a Caddy to install an SSD next to your old HDD



disable some devices as advised by this user
if you use an Intel chipset, try to install Intel Rapid storage Technology (RST) to replace the standard AHCI driver from Windows. This also seems to helped.
the user Shayna figured out, that using Process Hacker (started as admin) to suspend the threads of the ACPI.sys issues &quot;fixes&quot; the issue for him. So try his workaround if all other steps don't fix it for you.


In the following demo, the Intel HD driver igdkmd64.sys in version .4574 for the Intel HD 630 causes the issue:

The solution is to update to driver with version of at least .4590.

In the following case, the CPU usage of the SYSTEM process is caused by the driver stdriverx64.sys

This seems to be an audio streaming driver. So update this software/driver if you see this in WPA.

If you see a driver called risdxc64.sys in callstack of SYSTEM that causes the high CPU usage, update the Ricoh PCIe SDXC/MMC Host Controller driver or disable the SD card reader in device manager if no driver update fixes it.

This SD card reader seems to be built-in to many Lenovo devices.

The user @stevemidgley showed a new issue of higher CPU usage with Wdf01000.sys!FxSystemWorkItem::_WorkItemThunk

Here you can see a driver UDE.sys causing it.
In symbol hub

I can see it belongs to Modem driver and PNP data of the trace shows Fibocom L850-GL (LTE Modem) as possible device:

And the solution is to disable the modem and USB composite device in device manager.

The user @fajar provided the following case:

Here the cpu usage is small, but if you change the view to DPC/ISR usage

you can see that the avgNetHub.sys driver causes a lof of DPC usage

The name indicates that this driver is part of AVG anti virus software. So update the software or remove it if you see this in your trace.

**参考链接**: https://superuser.com/questions/527401/troubleshoot-high-cpu-usage-by-the-system-process

> 📎 来源 / Source: https://superuser.com/questions/527401/troubleshoot-high-cpu-usage-by-the-system-process

#### 58. How do I set system environment variables in Windows 10?

**故障现象**: How do I set system environment variables in Windows 10?
**标签 / 来源**: Tags: windows, windows-10 | superuser | 👍 239 | 💬 9 answers

**问题描述**:
Tags: windows, windows-10 | Score: 239 | Views: 1539780 | Answers: 9

**解决方法 / 社区答案**:
Note: After seeing lots of comments about setting environment variables without administrator rights in Windows 10, I think I have found a way. I was not administrator and could use PowerShell.
PowerShell method
You can list all environment variables with: Get-ChildItem Env:.
To get the value of a specific variable: $Env:PATH, where PATH is the name of the variable.
To set a variable: [Environment]::SetEnvironmentVariable(&quot;PATH&quot;, &quot;C:\TestPath&quot;, &quot;User&quot;), the first parameter is the name of the variable, the second is the value, the third is the level of.
There are different ways to work with environment variables and certain quirks with them in PowerShell so consult the link for details.
Old method (no longer available in newer Windows 10 updates, use PowerShell or see other answers)
Go into Settings and click on System.

Then on the left side click About and select System info at the bottom.

In the new Control Panel window that opens, click Advanced system settings on the left.

Now in the new window that comes up, select Environment Variables... at the bottom.

**参考链接**: https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10

> 📎 来源 / Source: https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10

#### 59. How to supress &quot;Terminate batch job (Y/N)&quot; confirmation?

**故障现象**: How to supress &quot;Terminate batch job (Y/N)&quot; confirmation?
**标签 / 来源**: Tags: windows, command-line, batch | superuser | 👍 236 | 💬 21 answers

**问题描述**:
Tags: windows, command-line, batch | Score: 236 | Views: 199305 | Answers: 21

**解决方法 / 社区答案**:
At this site, I found an effective solution:

script2.cmd &lt; nul


To not have to type this out every time I made a second script called script.cmd in the same folder with the line above.  I've tested this technique on XP only, but others have confirmed it on Win 7.

Nathan adds:  another option is to put the following code at the top of script.cmd which does the same thing in one file:

rem Bypass "Terminate Batch Job" prompt.
if "%~1"=="-FIXED_CTRL_C" (
   REM Remove the -FIXED_CTRL_C parameter
   SHIFT
) ELSE (
   REM Run the batch with &lt;NUL and -FIXED_CTRL_C
   CALL &lt;NUL %0 -FIXED_CTRL_C %*
   GOTO :EOF
)

**参考链接**: https://superuser.com/questions/35698/how-to-supress-terminate-batch-job-y-n-confirmation

> 📎 来源 / Source: https://superuser.com/questions/35698/how-to-supress-terminate-batch-job-y-n-confirmation

#### 60. How to compare the differences between two PDF files on Windows?

**故障现象**: How to compare the differences between two PDF files on Windows?
**标签 / 来源**: Tags: windows, pdf, file-comparison | superuser | 👍 234 | 💬 19 answers

**问题描述**:
Tags: windows, pdf, file-comparison | Score: 234 | Views: 484912 | Answers: 19

**解决方法 / 社区答案**:
On Linux and Windows you can use diffpdf (which differs from diff-pdf mentioned in this thread).

On Ubuntu install using:
sudo apt-get install diffpdf

See further this UbuntuGeek page on comparing pds textually or visually.
For Windows, this Diffpdf Windows version works really great. You can download from http://soft.rubypdf.com/software/diffpdf (scroll down to Win32 static version).
You can also install it on Windows in an automated manner via the https://scoop.sh/ package manager - install the package manager first per instructions on the homepage and then:
scoop bucket add extras
scoop install extras/diffpdf

This does not require administrator privileges on your account, so it can be installed on externally managed systems (e.g. work computers).

**参考链接**: https://superuser.com/questions/46123/how-to-compare-the-differences-between-two-pdf-files-on-windows

> 📎 来源 / Source: https://superuser.com/questions/46123/how-to-compare-the-differences-between-two-pdf-files-on-windows

#### 61. How to make SUBST mapping persistent across reboots?

**故障现象**: How to make SUBST mapping persistent across reboots?
**标签 / 来源**: Tags: windows, subst | superuser | 👍 232 | 💬 11 answers

**问题描述**:
Tags: windows, subst | Score: 232 | Views: 287015 | Answers: 11

**解决方法 / 社区答案**:
Well Wikipedia mentions:

C:\&gt;SUBST /?
Associates a path with a drive letter.

SUBST [drive1: [drive2:]path]
SUBST drive1: /D

  drive1:        Specifies a virtual drive to which you want to assign a path.
  [drive2:]path  Specifies a physical drive and path you want to assign to
                 a virtual drive.
  /D             Deletes a substituted (virtual) drive.

Type SUBST with no parameters to display a list of current virtual drives.


So you can associate paths with drive letters using subst. The Persistent SUBST command (psubst) software seems to be darn handy, and they provide a solution to run it from startup:
https://github.com/ildar-shaimordanov/psubst#Inconstancy

Inconstancy
However restart of a system destroys a virtual disk. What to do? A
disk can be created after startup. But what to do, when a disk is
needed on early steps of a startup? For example, to run services?
There is system feature to start a virtual disk from the system
registry:
REGEDIT4 

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\DOS Devices] 
&quot;Z:&quot;=&quot;\\??\\C:\\Documents and Settings\\All Users\\Shared Documents&quot;

It is enough to create a text file with the extension .REG and run
it. When the next starting up of a system, the virtual disk will be
exist at logon. It needs to define a name of disk and path. Note that
each backslash in the path is doubled.

In Windows, you can run the registry editor as follows:

Start » Run... (or hit Win+R)
Type: regedit
In Windows Vista and above, UAC will pop up, click &quot;Yes&quot;.

**参考链接**: https://superuser.com/questions/29072/how-to-make-subst-mapping-persistent-across-reboots

> 📎 来源 / Source: https://superuser.com/questions/29072/how-to-make-subst-mapping-persistent-across-reboots

#### 62. PowerShell equivalent to the Unix `which` command?

**故障现象**: PowerShell equivalent to the Unix `which` command?
**标签 / 来源**: Tags: windows, unix, powershell, which | superuser | 👍 231 | 💬 11 answers

**问题描述**:
Tags: windows, unix, powershell, which | Score: 231 | Views: 192989 | Answers: 11

**解决方法 / 社区答案**:
This was asked and answered on Stack Overflow: Equivalent of *Nix 'which' command in PowerShell?


  The very first alias I made once I started customizing my profile in PowerShell was 'which'.
  
  New-Alias which get-command
  
  To add this to your profile, type this:
  
  "`nNew-Alias which get-command" | add-content $profile
  
  The `n at the start of the last line is to ensure it will start as a new line.

**参考链接**: https://superuser.com/questions/34492/powershell-equivalent-to-the-unix-which-command

> 📎 来源 / Source: https://superuser.com/questions/34492/powershell-equivalent-to-the-unix-which-command

#### 63. Browse an UNC path using Windows CMD without mapping it to a network drive

**故障现象**: Browse an UNC path using Windows CMD without mapping it to a network drive
**标签 / 来源**: Tags: windows, command-line, network-drive, unc | superuser | 👍 230 | 💬 8 answers

**问题描述**:
Tags: windows, command-line, network-drive, unc | Score: 230 | Views: 521023 | Answers: 8

**解决方法 / 社区答案**:
If you use pushd and popd instead of cd you won't get that UNC error.
pushd &lt;UNC path&gt; will create a temporary virtual drive and get into it.
popd will delete the temporary drive and get you back to the path you were when you entered pushd.
Example:
C:\a\local\path&gt; pushd \\network_host\a\network\path

U:\a\network\path&gt; REM a temporary U: virtual drive has been created

U:\a\network\path&gt; popd

C:\a\local\path&gt; REM the U: drive has been deleted

C:\a\local\path&gt;

**参考链接**: https://superuser.com/questions/282963/browse-an-unc-path-using-windows-cmd-without-mapping-it-to-a-network-drive

> 📎 来源 / Source: https://superuser.com/questions/282963/browse-an-unc-path-using-windows-cmd-without-mapping-it-to-a-network-drive

#### 64. How do I know what proxy server I&#39;m using?

**故障现象**: How do I know what proxy server I&#39;m using?
**标签 / 来源**: Tags: windows, windows-xp, networking, proxy | superuser | 👍 229 | 💬 15 answers

**问题描述**:
Tags: windows, windows-xp, networking, proxy | Score: 229 | Views: 1026134 | Answers: 15

**解决方法 / 社区答案**:
The auto proxy detection system works by downloading a file called wpad.dat from the host wpad.  First confirm this host exists from a command prompt:

ping wpad


If it doesn't exist, you may have to put the correct DNS suffix.  In the same command prompt, type

ipconfig /all


You should see a Primary DNS Suffix and a DNS Suffix Search List

Try appending each of these with a . to wpad:

ping wpad.&lt;primary dns suffix&gt;


If any of these work, then in your browser enter http://wpad.&lt;suffix&gt;/wpad.dat.  This will download the proxy auto configuration file you can open in notepad.exe

Toward the bottom of this file, you should see a line saying 

PROXY &lt;host:port&gt;;


It might be repeated if you have multiple proxies available.  The host and port are what you need.

If this file doesn't exist, then either there is no proxy server, or the proxy server is being provided by dhcp (note that this would only work with IE, so if firefox can surf, this is not the method being used).  If you don't have access to the dhcp server to see what it is sending, the easiest way would be to open a site in ie, then go to a command prompt.  Type

netstat -ban


This will provide a list of connections made with the process id of each process.  Go to Task Manager, and select View/Select Columns and enable PID (Process Identifier).  Look for the PID of iexplore.exe in the list returned by netstat -ban  This will reveal the proxy ip and port.

**参考链接**: https://superuser.com/questions/346372/how-do-i-know-what-proxy-server-im-using

> 📎 来源 / Source: https://superuser.com/questions/346372/how-do-i-know-what-proxy-server-im-using

#### 65. PowerShell equivalent of curl

**故障现象**: PowerShell equivalent of curl
**标签 / 来源**: Tags: windows, powershell, curl | superuser | 👍 229 | 💬 9 answers

**问题描述**:
Tags: windows, powershell, curl | Score: 229 | Views: 723773 | Answers: 9

**解决方法 / 社区答案**:
PowerShell 3.0 has the new command Invoke-RestMethod:

http://technet.microsoft.com/en-us/library/hh849971.aspx

more detail:  

https://discoposse.com/2012/06/30/powershell-invoke-restmethod-putting-the-curl-in-your-shell/

**参考链接**: https://superuser.com/questions/344927/powershell-equivalent-of-curl

> 📎 来源 / Source: https://superuser.com/questions/344927/powershell-equivalent-of-curl

#### 66. Typing “python” on Windows 10 (version 1903) command prompt opens Microsoft store

**故障现象**: Typing “python” on Windows 10 (version 1903) command prompt opens Microsoft store
**标签 / 来源**: Tags: windows-10, command-line, python, cmd.exe, unattended | superuser | 👍 229 | 💬 8 answers

**问题描述**:
Tags: windows-10, command-line, python, cmd.exe, unattended | Score: 229 | Views: 175078 | Answers: 8

**解决方法 / 社区答案**:
Fixed it by removing it automatically on the settings page.  Under Apps and Features, there are an application execution aliases.

I am running the latest 1903 update.

**参考链接**: https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor

> 📎 来源 / Source: https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor

#### 67. Windows 10 - disable reopening programs after restart/startup

**故障现象**: Windows 10 - disable reopening programs after restart/startup
**标签 / 来源**: Tags: windows, windows-10, boot | superuser | 👍 228 | 💬 7 answers

**问题描述**:
Tags: windows, windows-10, boot | Score: 228 | Views: 347803 | Answers: 7

**解决方法 / 社区答案**:
Good news! It has been somewhat &quot;fixed.&quot;
I was interested in clickbangdead's solution, but unfortunately I could not make it work no matter what I tried. Then I went back to the Microsoft Answers thread where he originally posted his solution, because maybe someone could have found a new solution in the subsequent pages. And voilà, indeed. Navigate to the following location:
Settings &gt; Accounts &gt; Sign-In Options
Scroll down to Privacy on the right and then set the following to Off:

Use my sign-in info to automatically finish setting up my device after an update or restart.


I was skeptical, because that doesn't seem like it has much to do with reopening my Google Chrome upon restart, but I tested and it (finally) works!

Update:  with the release of Windows 10 version 1803 (the April 2018 Update), Microsoft modified the wording within that Privacy option to emphasize that it will &quot;reopen my apps&quot; if it is configured to be On.

Use my sign-in info to automatically finish setting up my device and reopen my apps after an update or restart.

**参考链接**: https://superuser.com/questions/1229963/windows-10-disable-reopening-programs-after-restart-startup

> 📎 来源 / Source: https://superuser.com/questions/1229963/windows-10-disable-reopening-programs-after-restart-startup

#### 68. Change default code page of Windows console to UTF-8

**故障现象**: Change default code page of Windows console to UTF-8
**标签 / 来源**: Tags: windows-7, windows, encoding, console | superuser | 👍 226 | 💬 9 answers

**问题描述**:
Tags: windows-7, windows, encoding, console | Score: 226 | Views: 563116 | Answers: 9

**解决方法 / 社区答案**:
To change the codepage for the console only, do the following:

Start -&gt; Run -&gt; regedit
Go to [HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\Autorun]
Change the value to @chcp 65001&gt;nul

If Autorun is not present, you can add a New String

**参考链接**: https://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8

> 📎 来源 / Source: https://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8

#### 69. How to prevent Windows 10 from automatically adding keyboard layouts (i.e. US keyboard)

**故障现象**: How to prevent Windows 10 from automatically adding keyboard layouts (i.e. US keyboard)
**标签 / 来源**: Tags: windows, windows-10, keyboard, language, input-languages | superuser | 👍 223 | 💬 12 answers

**问题描述**:
Tags: windows, windows-10, keyboard, language, input-languages | Score: 223 | Views: 268606 | Answers: 12

**解决方法 / 社区答案**:
To fix this issue, delete the Preload registry folder and sign out or restart the computer:

HKEY_USERS\.DEFAULT\Keyboard Layout\Preload


This folder seems to be some legacy remnant that contains non-user-specified keyboard layouts to be added to the list of languages when the user signs in. While the fix itself works through restarts, at time of writing there's things that bring back that pesky folder, here's a few that I bumped into personally:


Remote desktop to a computer with US layout
Using the same Microsoft account on another PC that still has this
issue


Whenever the problem comes back, that registry folder needs to be deleted again.

Edit 2:
Thanks to @Lu55's suggestion, here's a handy one-liner to use on a command prompt with admin privileges:

reg delete "HKEY_USERS\.DEFAULT\Keyboard Layout\Preload" /f


Edit:
I have created a RemovePreload.reg text file with the following content, this way this fix can easily be re-applied every time without navigating the registry:

Windows Registry Editor Version 5.00

[-HKEY_USERS\.DEFAULT\Keyboard Layout\Preload]


To use this, save it in a text file and change the extension from .txt to .reg. Then whenever it comes back, you can just double click it and restart or sign out.

**参考链接**: https://superuser.com/questions/1092246/how-to-prevent-windows-10-from-automatically-adding-keyboard-layouts-i-e-us-ke

> 📎 来源 / Source: https://superuser.com/questions/1092246/how-to-prevent-windows-10-from-automatically-adding-keyboard-layouts-i-e-us-ke

#### 70. Disable &quot;These files might be harmful to your computer&quot; warning?

**故障现象**: Disable &quot;These files might be harmful to your computer&quot; warning?
**标签 / 来源**: Tags: windows, networking, windows-explorer | superuser | 👍 223 | 💬 14 answers

**问题描述**:
Tags: windows, networking, windows-explorer | Score: 223 | Views: 365744 | Answers: 14

**解决方法 / 社区答案**:
I found a fix by changing &quot;internet options&quot; -- so I guess Windows is detecting the &quot;internet&quot; as my own network.. sigh.

Click Start / Control Panel / Internet Options
Click Security tab.
Click Local Intranet
Click Sites button.
Click Advanced button.
Enter the IP Address of the other machine or server (wildcards are allowed) and click Add
Click Close, then OK, then OK again.
Disconnect, and reconnect the network drive


This worked for me, but it's a bummer I have to manually enter IPs here.. it would be nice if Windows could detect this is a local network file copy and skip the irritating (and pointless) warning about &quot;dangerous&quot; files.
Sidenotes:

If you are using a DNS name (i.e. FQDN) to map the network drive, adding the IP address of the server to the zone will not work. You will need to add the DNS name (i.e. FQDN), and vice-versa.
When adding an IP address, you can use wildcards like so: 192.168.1.*
When adding a DNS name (i.e. FQDN), you can use wildcards like so: *.example.com

**参考链接**: https://superuser.com/questions/149056/disable-these-files-might-be-harmful-to-your-computer-warning

> 📎 来源 / Source: https://superuser.com/questions/149056/disable-these-files-might-be-harmful-to-your-computer-warning

#### 71. What are CLOSE_WAIT and TIME_WAIT states?

**故障现象**: What are CLOSE_WAIT and TIME_WAIT states?
**标签 / 来源**: Tags: windows, networking, port, tcpip | superuser | 👍 221 | 💬 3 answers

**问题描述**:
Tags: windows, networking, port, tcpip | Score: 221 | Views: 610666 | Answers: 3

**解决方法 / 社区答案**:
Due to the way TCP/IP works, connections can not be closed immediately.  Packets may arrive out of order or be retransmitted after the connection has been closed.

CLOSE_WAIT indicates that the remote endpoint (other side of the connection) has closed the connection.
TIME_WAIT indicates that local endpoint (this side) has closed the connection.

The connection is being kept around so that any delayed packets can be matched to the connection and handled appropriately.  The connections will be removed when they time out within four minutes. See http://en.wikipedia.org/wiki/Transmission_Control_Protocol for more details.

**参考链接**: https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states

> 📎 来源 / Source: https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states

#### 72. Preventing applications from stealing focus

**故障现象**: Preventing applications from stealing focus
**标签 / 来源**: Tags: windows, window-focus | superuser | 👍 220 | 💬 7 answers

**问题描述**:
Tags: windows, window-focus | Score: 220 | Views: 130694 | Answers: 7

**解决方法 / 社区答案**:
This is not possible without extensive manipulation of Windows internals and you need to get over it.

There are moments in daily computer use when it is really important that you make one action before the operating system allows you to do another. To do that, it needs to lock your focus on certain windows. In Windows, control over this behavior is largely left to the developers of the individual programs that you use.

Not every developer makes the right decisions when it comes to this topic.

I know that this is very frustrating and annoying, but you can't have your cake and eat it too. There are probably many cases throughout your daily life where you're perfectly fine with the focus being moved to a certain UI element or an application requesting that the focus remains locked on it. But most applications are somewhat equal when it comes to deciding who is the lead right now and the system can never be perfect.

A while ago I did extensive research on solving this issue once and for all (and failed). The result of my research can be found on the annoyance project page.

The project also includes an application that repeatedly tries to grab focus by calling:

switch( message ) {
  case WM_TIMER:
    if( hWnd != NULL ) {
      // Start off easy
      // SetForegroundWindow will not move the window to the foreground,
      // but it will invoke FlashWindow internally and, thus, show the
      // taskbar.
      SetForegroundWindow( hWnd );

      // Our application is awesome! It must have your focus!
      SetActiveWindow( hWnd );

      // Flash that button!
      FlashWindow( hWnd, TRUE );
    }
    break;


As we can see from this snippet, my research was also focused on other aspects of user interface behavior I don't like.

The way I tried to solve this was to load a DLL into every new process and hook the API calls that cause another windows to be activated.
The last part is the easy one, thanks to awesome API hooking libraries out there. I used the very great mhook library:

#include "stdafx.h"
#include "mhook-2.2/mhook-lib/mhook.h"

typedef NTSTATUS( WINAPI* PNT_QUERY_SYSTEM_INFORMATION ) ( 
  __in       SYSTEM_INFORMATION_CLASS SystemInformationClass,     
  __inout    PVOID SystemInformation, 
  __in       ULONG SystemInformationLength, 
  __out_opt  PULONG ReturnLength    
);

// Originals
PNT_QUERY_SYSTEM_INFORMATION OriginalFlashWindow   = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "FlashWindow" );

PNT_QUERY_SYSTEM_INFORMATION OriginalFlashWindowEx = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "FlashWindowEx" );

PNT_QUERY_SYSTEM_INFORMATION OriginalSetForegroundWindow = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "SetForegroundWindow" );

// Hooks
BOOL WINAPI
HookedFlashWindow(
  __in  HWND hWnd,
  __in  BOOL bInvert
  ) {
  return 0;
}

BOOL WINAPI 
HookedFlashWindowEx(
  __in  PFLASHWINFO pfwi
  ) {
  return 0;
}

BOOL WINAPI 
HookedSetForegroundWindow(
  __in  HWND hWnd
  ) {
  // Pretend window was brought to foreground
  return 1;
}


BOOL APIENTRY 
DllMain( 
  HMODULE hModule,
  DWORD   ul_reason_for_call,
  LPVOID  lpReserved
  ) {
  switch( ul_reason_for_call ) {
    case DLL_PROCESS_ATTACH:
      Mhook_SetHook( (PVOID*)&amp;OriginalFlashWindow,         HookedFlashWindow );
      Mhook_SetHook( (PVOID*)&amp;OriginalFlashWindowEx,       HookedFlashWindowEx );
      Mhook_SetHook( (PVOID*)&amp;OriginalSetForegroundWindow, HookedSetForegroundWindow );
      break;

    case DLL_PROCESS_DETACH:
      Mhook_Unhook( (PVOID*)&amp;OriginalFlashWindow );
      Mhook_Unhook( (PVOID*)&amp;OriginalFlashWindowEx );
      Mhook_Unhook( (PVOID*)&amp;OriginalSetForegroundWindow );
      break;
  }
  return TRUE;
}


From my tests back then, this worked great. Except for the part of loading the DLL into every new process. As one might imagine, that's nothing to take too lightly. I used the AppInit_DLLs approach back then (which is simply not sufficient).

Basically, this works great. But I never found the time to write something that properly injects my DLL into new processes. And the time invested in this largely overshadows the annoyance the focus stealing causes me.

In addition to the DLL injection problem, there is also a focus-stealing method which I didn't cover in the implementation on Google Code. A co-worker actually did some additional research and covered that method. The problem was discussed on SO: https://stackoverflow.com/questions/7430864/windows-7-prevent-application-from-losing-focus

**参考链接**: https://superuser.com/questions/18383/preventing-applications-from-stealing-focus

> 📎 来源 / Source: https://superuser.com/questions/18383/preventing-applications-from-stealing-focus

#### 73. Why are there directories called Local, LocalLow, and Roaming under \Users\&lt;username&gt;\AppData?

**故障现象**: Why are there directories called Local, LocalLow, and Roaming under \Users\&lt;username&gt;\AppData?
**标签 / 来源**: Tags: windows, thunderbird, user-profiles | superuser | 👍 213 | 💬 3 answers

**问题描述**:
Tags: windows, thunderbird, user-profiles | Score: 213 | Views: 134967 | Answers: 3

**解决方法 / 社区答案**:
Roaming is the folder that would be synchronized with a server if you logged into a domain with a roaming profile (enabling you to log into any computer in a domain and access your favorites, documents, etc. Firefox stores its information here, so you could even have the same bookmarks between computers with a roaming profile.
Local is the folder that is specific to that computer - any information here would not be synchronized with a server. This folder is equivalent in Windows XP to C:\Documents and Settings\User\Local Settings\Application Data.
LocalLow is the same folder as local, but it has a lower integrity level. For example, Internet Explorer 8 can only write to the LocalLow folder (when protected mode is on).
This document from Microsoft (&quot;Managing Roaming User Data Deployment Guide&quot;) has a long explanation for what these three folder areas are and how they are used, as well as the changes implemented between Windows XP and Vista (Windows 7 retains the Vista structure).

**参考链接**: https://superuser.com/questions/21458/why-are-there-directories-called-local-locallow-and-roaming-under-users-user

> 📎 来源 / Source: https://superuser.com/questions/21458/why-are-there-directories-called-local-locallow-and-roaming-under-users-user

#### 74. How to disable internet search results in start menu post Creators Update?

**故障现象**: How to disable internet search results in start menu post Creators Update?
**标签 / 来源**: Tags: windows-10, windows-10-v1703, cortana, windows-10-v1803 | superuser | 👍 212 | 💬 4 answers

**问题描述**:
Tags: windows-10, windows-10-v1703, cortana, windows-10-v1803 | Score: 212 | Views: 144810 | Answers: 4

**解决方法 / 社区答案**:
The article
The Windows 10 spring update no longer lets you disable web search in Start - workaround reports that the following registry update
is required in Windows 10 version 1803 :
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search]
&quot;BingSearchEnabled&quot;=dword:00000000
&quot;AllowSearchToUseLocation&quot;=dword:00000000
&quot;CortanaConsent&quot;=dword:00000000

It remarks :

those entries are completely missing from the &quot;Search&quot; registry key, so you can safely delete them should you want to revert.

I would still recommend to at least create a system restore point before doing
any registry modifications.
A reboot might be required.
User @mtd has contributed below these commands for applying the updates to
the registry:
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v BingSearchEnabled /t REG_DWORD /d 0
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v AllowSearchToUseLocation /t REG_DWORD /d 0
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v CortanaConsent /t REG_DWORD /d 0


EDIT1 : There are reports that Windows 10 version 2004 has broken the above fix.
The article
Disable Web Search in Taskbar in Windows 10 Version 2004
has a summary of the current state of the problem.
The current solution seems to be to download and run this
PowerShell script
as Administrator:
Set-ExecutionPolicy Unrestricted -Scope Process
.\disable-web-search.ps1

As only a workaround, this PowerShell script blocks the online search using
Windows Firewall rules, so forcing the search to operate in offline mode.

EDIT2: Reports now say that these registry modification are working for
Windows versions 2004 and 20H2 without reboot.

EDIT3: Windows 11 21H2 - it has been reported that it is
also required to create in the registry key
HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer,
a DWORD32 value named DisableSearchBoxSuggestions
and set its value to 1.
More information in the article
How to Disable Web Search Results in Start Menu on Windows 11.

**参考链接**: https://superuser.com/questions/1196618/how-to-disable-internet-search-results-in-start-menu-post-creators-update

> 📎 来源 / Source: https://superuser.com/questions/1196618/how-to-disable-internet-search-results-in-start-menu-post-creators-update

#### 75. How to delete a file in Windows with a too long filename?

**故障现象**: How to delete a file in Windows with a too long filename?
**标签 / 来源**: Tags: windows, path, filenames | superuser | 👍 211 | 💬 8 answers

**问题描述**:
Tags: windows, path, filenames | Score: 211 | Views: 406543 | Answers: 8

**解决方法 / 社区答案**:
When you want to completely delete a directory and it contains long paths, robocopy does a VERY good job:

mkdir empty_dir
robocopy empty_dir the_dir_to_delete /mir
rmdir empty_dir
rmdir the_dir_to_delete


This works because robocopy internally uses the Unicode-aware versions of Win32 functions, with the \\?\ prefix for file paths; those functions have a limit of 2¹⁶-1 (32,767) characters instead of 259.

You may need to go through this process more than once to get rid of all of the files.

**参考链接**: https://superuser.com/questions/45697/how-to-delete-a-file-in-windows-with-a-too-long-filename

> 📎 来源 / Source: https://superuser.com/questions/45697/how-to-delete-a-file-in-windows-with-a-too-long-filename

#### 76. How to copy text from Console2?

**故障现象**: How to copy text from Console2?
**标签 / 来源**: Tags: windows, console, copy-paste, console2 | superuser | 👍 210 | 💬 10 answers

**问题描述**:
Tags: windows, console, copy-paste, console2 | Score: 210 | Views: 46862 | Answers: 10

**解决方法 / 社区答案**:
Open Console2 menu Edit -> Settings, and in the Hotkeys / Mouse settings configure the selection and copy actions. The defaults are a bit wonky. 

I use: 


Left mouse button = select
Ctrl+C = copy
Ctrl+V = paste
ESC = clear selection


Make sure you press 'Assign' after each change you make otherwise it won't take effect.

Last note: Beware if you use ESC or Ctrl+V in vim, or in any other app.

**参考链接**: https://superuser.com/questions/132711/how-to-copy-text-from-console2

> 📎 来源 / Source: https://superuser.com/questions/132711/how-to-copy-text-from-console2

#### 77. How can I create a symbolic link on Windows 10?

**故障现象**: How can I create a symbolic link on Windows 10?
**标签 / 来源**: Tags: windows-10, symbolic-link | superuser | 👍 210 | 💬 6 answers

**问题描述**:
Tags: windows-10, symbolic-link | Score: 210 | Views: 618994 | Answers: 6

**解决方法 / 社区答案**:
It seems like the junction command has been retired in Windows 10.
You can download junction from Windows SysInternals (which is part of Microsoft):

Junction not only allows you to create NTFS junctions, it allows you to see if files or directories are actually reparse points. Reparse points are the mechanism on which NTFS junctions are based, and they are used by Windows' Remote Storage Service (RSS), as well as volume mount points.
Please read this Microsoft KB article for tips on using junctions.
Note that Windows does not support junctions to directories on remote shares.


So how do I create junctions or directory symbolic links in Windows 10?
Download junction as instructed above.
Now you can use the following commands.
Create a junction:
junction &quot;C:\Documents and Settings\UserName\My Documents\My Dropbox\My Games&quot; &quot;C:\Documents and Settings\UserName\My Documents\My Games&quot;

Create a directory symbolic link:
mklink /D &quot;C:\Documents and Settings\UserName\My Documents\My Dropbox\My Games&quot; &quot;C:\Documents and Settings\UserName\My Documents\My Games&quot;

You can use either mklink /j or junction in Windows 10 and upwards to create junctions.
You can use mklink /d in Windows 10 and upwards to create directory symbolic links.
Notes:

junction can also list junctions and determine if a file is a junction unlike mklink.

mklink is an internal command only available within a cmd shell.

By default Administrator privileges are required to create symbolic links.
It can also be granted to other users. The security setting &quot;Create symbolic links&quot; can be granted at:
  Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\




Examples
Using mklink to create a directory symbolic link:
F:\test&gt;mklink /d test-dir-sym-link test
symbolic link created for test-dir-sym-link &lt;&lt;===&gt;&gt; test

Using mklink to create a junction:
F:\test&gt;mklink /j test-junction test
Junction created for test-junction &lt;&lt;===&gt;&gt; test

Using junction to create a junction:
F:\test&gt;C:\apps\NirSoft\SysinternalsSuite\junction.exe test-junction test

Junction v1.06 - Windows junction creator and reparse point viewer
Copyright (C) 2000-2010 Mark Russinovich
Sysinternals - www.sysinternals.com

Created: F:\test\test-junction
Targetted at: F:\test\test


Further Reading

An A-Z Index of the Windows CMD command line - An excellent reference for all things Windows cmd line related.
mklink - Create a symbolic link to a directory or a file, or create a hard file link or directory junction.

**参考链接**: https://superuser.com/questions/1020821/how-can-i-create-a-symbolic-link-on-windows-10

> 📎 来源 / Source: https://superuser.com/questions/1020821/how-can-i-create-a-symbolic-link-on-windows-10

#### 78. &quot;This file came from another computer...&quot; - how can I unblock all the files in a folder without having to unblock them individually?

**故障现象**: &quot;This file came from another computer...&quot; - how can I unblock all the files in a folder without having to unblock them individually?
**标签 / 来源**: Tags: windows, security, ntfs | superuser | 👍 209 | 💬 15 answers

**问题描述**:
Tags: windows, security, ntfs | Score: 209 | Views: 301626 | Answers: 15

**解决方法 / 社区答案**:
If you download a .ZIP and unzip it, the individual files will be marked as the same zone as the .ZIP.  Almost every time I have a folder full of "blocked" files, this is how I got them.

Before unzipping, click the Unblock button on the .ZIP.

**参考链接**: https://superuser.com/questions/38476/this-file-came-from-another-computer-how-can-i-unblock-all-the-files-in-a

> 📎 来源 / Source: https://superuser.com/questions/38476/this-file-came-from-another-computer-how-can-i-unblock-all-the-files-in-a

#### 79. How do I edit text files in the Windows command prompt?

**故障现象**: How do I edit text files in the Windows command prompt?
**标签 / 来源**: Tags: windows, command-line, ssh, text-editors | superuser | 👍 209 | 💬 14 answers

**问题描述**:
Tags: windows, command-line, ssh, text-editors | Score: 209 | Views: 1380568 | Answers: 14

**解决方法 / 社区答案**:
The simplest solution on all versions of Windows is:

C:\&gt; notepad somefile.txt


And, no extra software required.

**参考链接**: https://superuser.com/questions/186857/how-do-i-edit-text-files-in-the-windows-command-prompt

> 📎 来源 / Source: https://superuser.com/questions/186857/how-do-i-edit-text-files-in-the-windows-command-prompt

#### 80. How can I put the computer to sleep from Command Prompt/Run menu?

**故障现象**: How can I put the computer to sleep from Command Prompt/Run menu?
**标签 / 来源**: Tags: windows, command-line, sleep, shutdown, run-dialog | superuser | 👍 209 | 💬 14 answers

**问题描述**:
Tags: windows, command-line, sleep, shutdown, run-dialog | Score: 209 | Views: 792670 | Answers: 14

**解决方法 / 社区答案**:
You will find shutdown.exe to be your friend.
Other handy commands see this post:
Sleep Computer (read more at https://superuser.com/a/463652/249349 )
Lock Workstation
Hibernate Computer - see answers by Scott Chamberlain and Eric L.
Restart Computer
Shutdown.exe -r -t 00

Shutdown Computer
Shutdown.exe -s -t 00

EDIT/UPDATE:
It seems that sleeping a computer is problematic if hibernate is turned on.
Copying from other answers:
You can either try PsShutdown
or:

The command rundll32.exe powrprof.dll,SetSuspendState 0,1,0 for sleep
is correct - however, it will hibernate instead of sleep if you don't
turn the hibernation off.
Here's how to do that:
Go to the Start Menu and open an elevated Command Prompt by typing
cmd.exe, right clicking and choosing Run as administrator. Type the
following command:

powercfg -hibernate off

**参考链接**: https://superuser.com/questions/42124/how-can-i-put-the-computer-to-sleep-from-command-prompt-run-menu

> 📎 来源 / Source: https://superuser.com/questions/42124/how-can-i-put-the-computer-to-sleep-from-command-prompt-run-menu

#### 81. How do I view the contents of a PFX file on Windows?

**故障现象**: How do I view the contents of a PFX file on Windows?
**标签 / 来源**: Tags: windows, security, certificate, client-certificate | superuser | 👍 206 | 💬 6 answers

**问题描述**:
Tags: windows, security, certificate, client-certificate | Score: 206 | Views: 450692 | Answers: 6

**解决方法 / 社区答案**:
Some options to view PFX file details:


Open a command prompt and type: certutil -dump &lt;path to cert&gt;
Install OpenSSL and use the commands to view the details, such as: openssl pkcs12 -info -in &lt;path to cert&gt;

**参考链接**: https://superuser.com/questions/580697/how-do-i-view-the-contents-of-a-pfx-file-on-windows

> 📎 来源 / Source: https://superuser.com/questions/580697/how-do-i-view-the-contents-of-a-pfx-file-on-windows

#### 82. How to access Windows folders from Bash on Ubuntu on Windows

**故障现象**: How to access Windows folders from Bash on Ubuntu on Windows
**标签 / 来源**: Tags: windows-10, bash, shell, windows-subsystem-for-linux | superuser | 👍 202 | 💬 2 answers

**问题描述**:
Tags: windows-10, bash, shell, windows-subsystem-for-linux | Score: 202 | Views: 353691 | Answers: 2

**解决方法 / 社区答案**:
You'll find the Windows C:\ structure at /mnt/c/ in the Bash environment.

Therefore, my Documents folder is at /mnt/c/Users/Ben/Documents/.

**参考链接**: https://superuser.com/questions/1066261/how-to-access-windows-folders-from-bash-on-ubuntu-on-windows

> 📎 来源 / Source: https://superuser.com/questions/1066261/how-to-access-windows-folders-from-bash-on-ubuntu-on-windows

#### 83. How do I create a GIF screencast in Windows?

**故障现象**: How do I create a GIF screencast in Windows?
**标签 / 来源**: Tags: windows, software-rec, screen-capture, animated-gif | superuser | 👍 201 | 💬 10 answers

**问题描述**:
Tags: windows, software-rec, screen-capture, animated-gif | Score: 201 | Views: 161751 | Answers: 10

**解决方法 / 社区答案**:
I've been using licecap in various Super&nbsp;User answers. It's dead simple to use as you can see from this animated GIF image - just extend it over your recording area, hit record, set a save file, do your thing and hit stop. It's free, works pretty well, and seems simpler than most of the alternatives. It's entirely free and has Windows and OS X ports.



On Windows 8.1 and hdpi displays, you'll need to turn off per app display scaling to get it to work normally without turning off global display scaling. I have a walkthrough on it here (Fixed as of version 1.26.)

**参考链接**: https://superuser.com/questions/81826/how-do-i-create-a-gif-screencast-in-windows

> 📎 来源 / Source: https://superuser.com/questions/81826/how-do-i-create-a-gif-screencast-in-windows

#### 84. Windows 10 Search can&#39;t find ANY applications. Even calculator

**故障现象**: Windows 10 Search can&#39;t find ANY applications. Even calculator
**标签 / 来源**: Tags: windows, search, windows-10 | superuser | 👍 201 | 💬 13 answers

**问题描述**:
Tags: windows, search, windows-10 | Score: 201 | Views: 390409 | Answers: 13

**解决方法 / 社区答案**:
I have no idea why or what I have broken in the process.
But here is what worked for me.


Ctrl+Shift+Right-click on an empty part of the taskbar and clicking "Exit Explorer" (or kill it via Task Manager if that doesn't work).
Delete this registry key.



  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderTypes\{ef87b4cb-f2ce-4785-8658-4ca6c63e38c6}\TopViews\{00000000-0000-0000-0000-000000000000}



Start process Explorer.exe via Task Manager.


This is one of many answers posted here. Feel free to try other people's suggestions. If you combine all answers in one I'll accept your answer.





Method for Creator's update
Check out this answer.

**参考链接**: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator

> 📎 来源 / Source: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator

#### 85. How can I make the Windows VPN route selective traffic (by destination network)?

**故障现象**: How can I make the Windows VPN route selective traffic (by destination network)?
**标签 / 来源**: Tags: windows, networking, vpn, routing | superuser | 👍 200 | 💬 13 answers

**问题描述**:
Tags: windows, networking, vpn, routing | Score: 200 | Views: 430954 | Answers: 13

**解决方法 / 社区答案**:
You can turn off taking over your entire connection by going to the properties of the VPN, Networking tab, Internet Protocol (TCP/IP) properties, Advanced, untick Use default gateway on remote network. This may or may not leave a route to 192.168.123.0/24 depending on the VPN server's setup. If it doesn't, you'll have to manually add the route each time, although you could put it in a batch file.

In order to manually add the route, run (as administrator):

route -p add 192.168.0.12 mask 255.255.255.255 10.100.100.254


This example will make a persistent (it's not necessary to run the command after a reboot) route to the IP 192.168.0.12 through the VPN gateway 10.100.100.254.

More about this at http://technet.microsoft.com/en-us/library/bb878117.aspx

**参考链接**: https://superuser.com/questions/12022/how-can-i-make-the-windows-vpn-route-selective-traffic-by-destination-network

> 📎 来源 / Source: https://superuser.com/questions/12022/how-can-i-make-the-windows-vpn-route-selective-traffic-by-destination-network

#### 86. Why is &#39;ping&#39; unable to resolve a name when &#39;nslookup&#39; works fine?

**故障现象**: Why is &#39;ping&#39; unable to resolve a name when &#39;nslookup&#39; works fine?
**标签 / 来源**: Tags: windows, networking, dns | superuser | 👍 200 | 💬 24 answers

**问题描述**:
Tags: windows, networking, dns | Score: 200 | Views: 453478 | Answers: 24

**解决方法 / 社区答案**:
I believe that nslookup opens a winsock connection on the DNS port and issues a query, whereas ping uses the DNS Client service. You could try and stop this service and see whether this makes a difference.
Some commands that will reinitialize various network states :
Reset WINSOCK entries to installation defaults : netsh winsock reset catalog
Reset TCP/IP stack to installation defaults : netsh int ip reset reset.log
Flush DNS resolver cache : ipconfig /flushdns
Renew DNS client registration and refresh DHCP leases : ipconfig /registerdns
Flush routing table : route /f
(Caution: this will remove all your routes and gateways until you restart!)

**参考链接**: https://superuser.com/questions/495759/why-is-ping-unable-to-resolve-a-name-when-nslookup-works-fine

> 📎 来源 / Source: https://superuser.com/questions/495759/why-is-ping-unable-to-resolve-a-name-when-nslookup-works-fine

#### 87. Hyper-V VM won&#39;t boot from Cd, error: &quot;unsigned image&#39;s hash is not allowed&quot;

**故障现象**: Hyper-V VM won&#39;t boot from Cd, error: &quot;unsigned image&#39;s hash is not allowed&quot;
**标签 / 来源**: Tags: windows-10, hyper-v, bootable-media | superuser | 👍 200 | 💬 5 answers

**问题描述**:
Tags: windows-10, hyper-v, bootable-media | Score: 200 | Views: 169855 | Answers: 5

**解决方法 / 社区答案**:
This error is a consequence of having Secure Boot enabled on the VM. Secure Boot prevents the system from getting hijacked at boot time by only allowing specifically authorized boot images to load. In Hyper-V client, the list is rather short.

To disable Secure Boot, power off the VM and then open the VM settings. Under Secure Boot, uncheck the box "Enable Secure Boot" and then click "OK". This will allow the VM to boot the "unauthorized" CD image.

Update: 
As mentioned by Itai Bar-Haim in the comments, and Thee Gamefanatic said in their answer, you can also select a different template depending on the OS image you're attempting to boot. Be aware that these templates are mutually exclusive - this means that you will not be able to boot a Windows OS image if you select the "Microsoft UEFI Certificate Authority" template.

Microsoft has a thorough deep dive into Secure Boot and how it works available on this blog:
https://blogs.technet.microsoft.com/dubaisec/2016/03/14/diving-into-secure-boot/

**参考链接**: https://superuser.com/questions/1026190/hyper-v-vm-wont-boot-from-cd-error-unsigned-images-hash-is-not-allowed

> 📎 来源 / Source: https://superuser.com/questions/1026190/hyper-v-vm-wont-boot-from-cd-error-unsigned-images-hash-is-not-allowed

#### 88. Remote Desktop intermittently freezing

**故障现象**: Remote Desktop intermittently freezing
**标签 / 来源**: Tags: windows-10, remote-desktop, windows-10-v1903 | superuser | 👍 200 | 💬 8 answers

**问题描述**:
Tags: windows-10, remote-desktop, windows-10-v1903 | Score: 200 | Views: 369955 | Answers: 8

**解决方法 / 社区答案**:
I also ran into this issue since July 2019 on a Windows 10 1903 acting as the client machine. The following workaround on the client works for me, so that RDP no longer freezes.

Start an elevated command prompt (run cmd.exe as administrator), and
then run:
reg add &quot;HKLM\software\policies\microsoft\windows nt\Terminal
Services\Client&quot; /v fClientDisableUDP /d 1 /t REG_DWORD

After that, close and reopen all your RDP sessions on your client computer to restart the Remote Desktop Client (mstsc.exe, aka Microsoft Terminal Services Client) application.
I'm waiting for a final fix to this issue.
Follow-up: I am not sure, but it looks like fixed in 21H1 (both client and server must run 21H1 or higher). For me I no longer see freezes without the disable UDP workaround.

**参考链接**: https://superuser.com/questions/1481191/remote-desktop-intermittently-freezing

> 📎 来源 / Source: https://superuser.com/questions/1481191/remote-desktop-intermittently-freezing

#### 89. How to stop Microsoft from gathering telemetry data from Windows 7, 8, and 8.1

**故障现象**: How to stop Microsoft from gathering telemetry data from Windows 7, 8, and 8.1
**标签 / 来源**: Tags: windows-7, windows, windows-8, windows-8.1 | superuser | 👍 199 | 💬 2 answers

**问题描述**:
Tags: windows-7, windows, windows-8, windows-8.1 | Score: 199 | Views: 323021 | Answers: 2

**解决方法 / 社区答案**:
Is there a way to disable the telemetry through some setting(s)?

Some telemetry can be disabled through settings.

This can be done manually.
There are also 3rd-party utilities such as Windows 10 Privacy Fixer and O&amp;O ShutUp10 which fix these settings in Windows 10.

Is it necessary to dig up which update patches are involved in the data gathering, and remove those?


Some telemetry disabling requires removal of (or not installing) patches.


Manually disabling Telemetry through settings (Windows 7, 8, and 8.1)

Disable the Windows Customer Experience Improvement Program (CEIP)
Note:
Disabling CEIP and the  related Task Scheduler tasks that control this program can improve Windows system performance.



Start &quot;Control Panel&quot; &gt; &quot;Action Center&quot; &gt; &quot;Change Action Center settings&quot;.







Click &quot;Customer Experience Improvement Program settings&quot;.







Select &quot;No, I don't want to participate in the program&quot; then click &quot;Save changes&quot;.







Start &gt; &quot;Control Panel&quot; &gt; &quot;Administrative Tools&quot; &gt; &quot;Task Scheduler&quot;.

In the Task Scheduler (Local) pane of the Task Scheduler dialog box,  expand &quot;Task Scheduler Library&quot; &gt; &quot;Microsoft&quot; &gt; &quot;Windows&quot; and open  the &quot;Application Experience&quot; folder.

Disable the &quot;AITAgent&quot; and &quot;ProgramDataUpdater&quot; tasks.

In &quot;Task Scheduler Library&quot; &gt; &quot;Microsoft&quot; &gt; &quot;Windows&quot;, open the  &quot;Customer Experience Improvement Program&quot; folder.

Disable the &quot;Consolidator&quot;, &quot;KernelCeipTask&quot;, and &quot;UsbCeip&quot; tasks.






Source Privacy Windows 10, Windows 7, Linux MINT - How do they compare?

Disabling Telemetry through patch removal (Windows 7, 8, and 8.1)
As Anixx has pointed out, there are some telemetry services that cannot be disabled through settings:


Telemetry-4xd,
refreshgwxconfig-B,
WSRefreshBannedAppsListTask,
Time-5d,
refreshgwxconfigandcontent,
Logon-5d,
MachineUnlock-5d,
OutOfIdle-5d,
OutOfSleep-5d,
Secure-Boot-Update, and
Tpm-Maintenance.

Also on any program crash the system reports the crash data to a server (although it is not connected with any scheduled task)


Stop Windows Telemetry/Tracking/Upgrading to Windows 10

Below are instructions for disabling the unwanted telemetry/tracking
in Windows 7 and 8.1 and removing all updates associated with
upgrading to Windows 10.




Here is the list of Windows updates to remove.




Before uninstalling them and rebooting make sure that you have Windows Update set to not automatically install updates:


KB3065988 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: July 2015 more info
KB3083325 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: September 2015 more info
KB3083324 Windows Update Client for Windows 7 and Windows Server 2008 R2: September 2015 more info
KB2976978 Compatibility update for Windows 8.1 and Windows 8 more info
KB3075853 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: August 2015 more info
KB3065987 Windows Update Client for Windows 7 and Windows Server 2008 R2: July 2015 more info
KB3050265 Windows Update Client for Windows 7: June 2015 more info
KB3050267 Windows Update Client for Windows 8.1: June 2015 more info
KB3075851 Windows Update Client for Windows 7 and Windows Server 2008 R2: August 2015 more info
KB2902907 MS Security Essentials/Windows Defender related update [no description/information available]
KB3068708 Update for customer experience and diagnostic telemetry more info
KB3022345 Update for customer experience and diagnostic telemetry more info
KB2952664 Compatibility update for upgrading Windows 7 more info
KB2990214 Update that enables you to upgrade from Windows 7 to a later version of Windows more info
KB3035583 Update installs Get Windows 10 app in Windows 8.1 and Windows 7 SP1 more info
KB971033 Description of the update for Windows Activation Technologies more info
KB3021917 Update to Windows 7 SP1 for performance improvements more info
KB3044374 Update that enables you to upgrade from Windows 8.1 to a later version of Windows more info
KB3046480 Update helps to determine whether to migrate the .NET Framework 1.1 when you upgrade Windows 8.1 or Windows 7 more info
KB3075249 Update that adds telemetry points to consent.exe in Windows 8.1 and Windows 7 more info
KB3080149 Update for customer experience and diagnostic telemetry more info
KB3083324 Windows Update Client for Windows 7 and Windows Server 2008 R2: September 2015 more info
KB3083325 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: September 2015 more info
KB3083710 Windows Update Client for Windows 7 and Windows Server 2008 R2: October 2015 more info
KB3083711 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: October 2015 more info
KB3112336 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: December 2015 more info
KB3123862 Updated capabilities to upgrade Windows 8.1 and Windows 7


They can be uninstalled manually via elevated command prompt with the following commands:

wusa /uninstall /kb:3065988 /quiet /norestart
wusa /uninstall /kb:3083325 /quiet /norestart
wusa /uninstall /kb:3083324 /quiet /norestart
wusa /uninstall /kb:2976978 /quiet /norestart
wusa /uninstall /kb:3075853 /quiet /norestart
wusa /uninstall /kb:3065987 /quiet /norestart
wusa /uninstall /kb:3050265 /quiet /norestart
wusa /uninstall /kb:3050267 /quiet /norestart
wusa /uninstall /kb:3075851 /quiet /norestart
wusa /uninstall /kb:2902907 /quiet /norestart
wusa /uninstall /kb:3068708 /quiet /norestart
wusa /uninstall /kb:3022345 /quiet /norestart
wusa /uninstall /kb:2952664 /quiet /norestart
wusa /uninstall /kb:2990214 /quiet /norestart
wusa /uninstall /kb:3035583 /quiet /norestart
wusa /uninstall /kb:971033 /quiet /norestart
wusa /uninstall /kb:3021917 /quiet /norestart
wusa /uninstall /kb:3044374 /quiet /norestart
wusa /uninstall /kb:3046480 /quiet /norestart
wusa /uninstall /kb:3075249 /quiet /norestart
wusa /uninstall /kb:3080149 /quiet /norestart
wusa /uninstall /kb:2977759 /quiet /norestart
wusa /uninstall /kb:3083710 /quiet /norestart
wusa /uninstall /kb:3083711 /quiet /norestart
wusa /uninstall /kb:3112336 /quiet /norestart
wusa /uninstall /kb:3123862 /quiet /norestart


Don’t forget to reboot afterwards. You can proceed to finish the next steps before rebooting.




The following services should be removed:




In an elevated command prompt run the following:


sc stop DiagTrack
sc stop dmwappushservice
sc delete DiagTrack
sc delete dmwappushservice
echo &quot;&quot; &gt; C:\ProgramData\Microsoft\Diagnosis\ETLLogs\AutoLogger\AutoLogger-Diagtrack-Listener.etl




Open the Task Scheduler (Win key then type &quot;sched&quot;). Under Task Scheduler Library -&gt; Microsoft -&gt; Windows delete the following items:


Everything under &quot;Application Experience&quot;

Everything under &quot;Autochk&quot;

Everything under &quot;Customer Experience Improvement Program&quot;

Under &quot;Disk Diagnostic&quot; delete only the &quot;Microsoft-Windows-DiskDiagnosticDataCollector&quot;

Under &quot;Maintenance&quot; &quot;WinSAT&quot; &quot;Media Center&quot; and click the &quot;status&quot; column, then select all non-disabled entries and disable them.

Now you can reboot. When you open Windows Update again it will ask to install whichever updates above were removed. Right-click on each one and select &quot;hide&quot;.






Finally, log in to your broadband router and look for an option like &quot;content filtering&quot; or &quot;block sites&quot;.




Add the following hosts to be blocked. On a Netgear router each host is a keyword that must be added.


Note, as Matthew Steeples has pointed out, a-0001.a-msedge.net is a CDN endpoint and has uses in non-telemetry scenarios.
134.170.30.202
137.116.81.24
204.79.197.200
23.218.212.69
65.39.117.230
65.55.108.23
a-0001.a-msedge.net
choice.microsoft.com
choice.microsoft.com.nsatc.net
compatexchange.cloudapp.net
corp.sts.microsoft.com
corpext.msitadfs.glbdns2.microsoft.com
cs1.wpc.v0cdn.net
df.telemetry.microsoft.com
diagnostics.support.microsoft.com
fe2.update.microsoft.com.akadns.net
feedback.microsoft-hohm.com
feedback.search.microsoft.com
feedback.windows.com
i1.services.social.microsoft.com
i1.services.social.microsoft.com.nsatc.net
oca.telemetry.microsoft.com
oca.telemetry.microsoft.com.nsatc.net
pre.footprintpredict.com
redir.metaservices.microsoft.com
reports.wes.df.telemetry.microsoft.com
services.wes.df.telemetry.microsoft.com
settings-sandbox.data.microsoft.com
sls.update.microsoft.com.akadns.net
sqm.df.telemetry.microsoft.com
sqm.telemetry.microsoft.com
sqm.telemetry.microsoft.com.nsatc.net
statsfe1.ws.microsoft.com
statsfe2.update.microsoft.com.akadns.net
statsfe2.ws.microsoft.com
survey.watson.microsoft.com
telecommand.telemetry.microsoft.com
telecommand.telemetry.microsoft.com.nsatc.net
telemetry.appex.bing.net
telemetry.appex.bing.net:443
telemetry.microsoft.com
telemetry.urs.microsoft.com
vortex.data.microsoft.com
vortex-sandbox.data.microsoft.com
vortex-win.data.microsoft.com
watson.live.com
watson.microsoft.com
watson.ppe.telemetry.microsoft.com
watson.telemetry.microsoft.com
watson.telemetry.microsoft.com.nsatc.net
wes.df.telemetry.microsoft.com

Source Stop Windows Telemetry/Tracking/Upgrading to Win10

Disabling Telemetry using 3rd-party utilities (Windows 10)
Windows 10 Privacy Fixer
Windows 10 Privacy Fixer provides a privacy check with options to fix a number of settings, including those related to Telemetry.



Source Windows 10 Privacy Fixer.
O&amp;O ShutUp10

O&amp;O ShutUp10 is a tiny portable tool which makes it easy to tweak
Windows 10's many privacy settings.
Launching the program displays almost 50 options, organised into
various categories: Security (telemetry, wifi sense, DRM), Privacy
(Cortana, input personalisation, app permissions), Windows Update
(disable peer-to-peer updates, disable automatic updates) and more.
These aren't always clearly described, but clicking any item displays
more details on what it does.
There are options to disable only the worst offenders (turn off
telemetry, peer-to-peer updates, keep Windows Update and SmartScreen),
turn off everything, or tweak individual settings.
ShutUp10 offers to create a system restore point before it makes any
changes, useful if your tweaking breaks something important and you
need an &quot;undo&quot;.
There's also a separate option to restore Windows 10's default privacy
settings, which might also be handy if they're generally messed up and
you'd like to start again.

Source O&amp;O ShutUp10.



Image source Windows 10 Is Watching: Should You Be Worried?

Disclaimer
I am not affiliated with 10 Privacy Fixer or O&amp;O ShutUp10.

**参考链接**: https://superuser.com/questions/972501/how-to-stop-microsoft-from-gathering-telemetry-data-from-windows-7-8-and-8-1

> 📎 来源 / Source: https://superuser.com/questions/972501/how-to-stop-microsoft-from-gathering-telemetry-data-from-windows-7-8-and-8-1

#### 90. On my Windows machine, I had a folder with a name of four dots that acted like some kind of rabbit hole - how did that happen?

**故障现象**: On my Windows machine, I had a folder with a name of four dots that acted like some kind of rabbit hole - how did that happen?
**标签 / 来源**: Tags: windows, filesystems | superuser | 👍 196 | 💬 5 answers

**问题描述**:
Tags: windows, filesystems | Score: 196 | Views: 40751 | Answers: 5

**解决方法 / 社区答案**:
Win32 doesn't let you create files or folders with names ending in . – all dots are stripped from the end. Trying to create test. makes test appear instead. (This is for compatibility with 8.3 names in old DOS/Win9x era software.)

As a result, whenever you try to access a folder named ...., its name gets reduced to the empty string, and you're back to the folder you were in before.

The NT kernel, however, does allow such names. There are various mechanisms which bypass filename limitations imposed by Win32 APIs – for example, WSL (Windows Subsystem for Linux) doesn't run on top of Win32 and is unaffected by it. There is also the \\?\ bypass method, a deliberate "backdoor" left in for programs which know what they're doing. Even though you cannot create C:\Example\....\, you can create \\?\C:\Example\....\ just fine.

Likewise you can delete such directories with rmdir \\?\C:\path\... from Cmd (I haven't tested with PowerShell yet).

Various file managers, archivers, etc. might use the \\?\ method in order to be able to use longer path names than usual – and by doing so, they're also unaffected by the compatibility code within Win32; they bypass dot stripping, as well as translation of magic filenames like CON or NUL.

So it could be that one of your programs:


always uses \\?\ to access files, 
accidentally tried to create a folder named .... – but it's not really possible to know for sure after the fact.

**参考链接**: https://superuser.com/questions/1371527/on-my-windows-machine-i-had-a-folder-with-a-name-of-four-dots-that-acted-like-s

> 📎 来源 / Source: https://superuser.com/questions/1371527/on-my-windows-machine-i-had-a-folder-with-a-name-of-four-dots-that-acted-like-s

#### 91. How to access linux/Ubuntu files from Windows 10 WSL?

**故障现象**: How to access linux/Ubuntu files from Windows 10 WSL?
**标签 / 来源**: Tags: windows-10, windows-10-v1607, windows-subsystem-for-linux | superuser | 👍 196 | 💬 15 answers

**问题描述**:
Tags: windows-10, windows-10-v1607, windows-subsystem-for-linux | Score: 196 | Views: 440334 | Answers: 15

**解决方法 / 社区答案**:
PM for Windows Command-Line here:

Updated October 2019: Updating the response below to reflect the newly added ability to directly access distros' Linux files via the newly integrated P9 server in Win10 1903 (and later).
IMPORTANT: Spelunking through the Windows filesystem to access Linux files has and will continue to be unsupported and STRONGLY recommended against! To understand why, please read this post

So how does one access Linux files using Windows tools (e.g. notepad, VS/VScode, etc.)? Previously, you couldn't, but starting in Windows 10 1903 we (finally!) expose your distros' filesystems to Windows via a P9 fileserver. We've also published an in-depth video discussing how this works! You can also read a summary of this new feature in this blog post

Look forward to hearing how you get on with this feature. If you find any problems, please file issues on the WSL GitHub repo here: https://github.com/Microsoft/wsl.

**参考链接**: https://superuser.com/questions/1110974/how-to-access-linux-ubuntu-files-from-windows-10-wsl

> 📎 来源 / Source: https://superuser.com/questions/1110974/how-to-access-linux-ubuntu-files-from-windows-10-wsl

#### 92. How can I determine file type without an extension on Windows?

**故障现象**: How can I determine file type without an extension on Windows?
**标签 / 来源**: Tags: windows, file-management, file-extension | superuser | 👍 194 | 💬 7 answers

**问题描述**:
Tags: windows, file-management, file-extension | Score: 194 | Views: 322511 | Answers: 7

**解决方法 / 社区答案**:
You can use the TrID tool which has a growing library of file type definitions for identifying files with.



Wildcards are supported, so in your example you could just put all the images to be examined in a folder, e.g. C:\verifyimages - then you can use the command:

trid C:\verifyimages\*


This will examine all files in the verifyimages folder.



There is also a GUI version available, TrIDNet:



There is documentation available on how you can you can easily integrate TrID or TrIDNet into Windows Explorer and Total Commander:

Windows Explorer


Integrate TrID
Integrate TrIDNet


Total Commander


Integrate TrID
Integrate TrIDNet

**参考链接**: https://superuser.com/questions/274734/how-can-i-determine-file-type-without-an-extension-on-windows

> 📎 来源 / Source: https://superuser.com/questions/274734/how-can-i-determine-file-type-without-an-extension-on-windows

#### 93. How can I prevent a policy-enforced screen lock in Windows?

**故障现象**: How can I prevent a policy-enforced screen lock in Windows?
**标签 / 来源**: Tags: windows, screensaver, security-policy | superuser | 👍 192 | 💬 18 answers

**问题描述**:
Tags: windows, screensaver, security-policy | Score: 192 | Views: 754710 | Answers: 18

**解决方法 / 社区答案**:
If Windows Media Player is still installed, you can play a video on loop and minimize it (the sample "Wildlife" videos work fine for this).  By default, as long as a video is playing, the screen won't lock.

**参考链接**: https://superuser.com/questions/329758/how-can-i-prevent-a-policy-enforced-screen-lock-in-windows

> 📎 来源 / Source: https://superuser.com/questions/329758/how-can-i-prevent-a-policy-enforced-screen-lock-in-windows

#### 94. How do I delete a folder that&#39;s in use?

**故障现象**: How do I delete a folder that&#39;s in use?
**标签 / 来源**: Tags: windows, file-management | superuser | 👍 191 | 💬 18 answers

**问题描述**:
Tags: windows, file-management | Score: 191 | Views: 655536 | Answers: 18

**解决方法 / 社区答案**:
There's a native GUI for Windows:

Start>>All Programs>>Accessories>>System Tools>>Resource Monitor (or Run resmon.exe)

You can search for the "Associated Handles" using the searchbox (circled in red), and right click the process you want to end.



As an example, in the image below I could not delete my Eclipse directory. Searching for the Eclipse associated handles showed that the adb.exe had a handle to the directory. After ending the adb process, I could then delete the Eclipse directory.

**参考链接**: https://superuser.com/questions/2937/how-do-i-delete-a-folder-thats-in-use

> 📎 来源 / Source: https://superuser.com/questions/2937/how-do-i-delete-a-folder-thats-in-use

#### 95. Create .zip folder from the command line - (Windows)

**故障现象**: Create .zip folder from the command line - (Windows)
**标签 / 来源**: Tags: windows | superuser | 👍 190 | 💬 12 answers

**问题描述**:
Tags: windows | Score: 190 | Views: 728995 | Answers: 12

**解决方法 / 社区答案**:
Tar
Windows 10 includes tar.exe:
# example 1
tar.exe -a -c -f out.zip in.txt
# example 2
tar.exe -x -f out.zip

If you have older Windows, you can still download from
libarchive/libarchive.
PowerShell
PowerShell has Compress-Archive:
# example 1
Compress-Archive in.txt out.zip
# example 2
Expand-Archive out.zip

Directory
For both tools, you can use a file or directory for the input.

**参考链接**: https://superuser.com/questions/201371/create-zip-folder-from-the-command-line-windows

> 📎 来源 / Source: https://superuser.com/questions/201371/create-zip-folder-from-the-command-line-windows

#### 96. How to run a batch file in a completely hidden way?

**故障现象**: How to run a batch file in a completely hidden way?
**标签 / 来源**: Tags: windows, command-line, batch-file | superuser | 👍 189 | 💬 20 answers

**问题描述**:
Tags: windows, command-line, batch-file | Score: 189 | Views: 809378 | Answers: 20

**解决方法 / 社区答案**:
Solution 1:
Save this one line of text as file invisible.vbs:
CreateObject(&quot;Wscript.Shell&quot;).Run &quot;&quot;&quot;&quot; &amp; WScript.Arguments(0) &amp; &quot;&quot;&quot;&quot;, 0, False

To run any program or batch file invisibly, use it like this:
wscript.exe &quot;C:\Wherever\invisible.vbs&quot; &quot;C:\Some Other Place\MyBatchFile.bat&quot;

To also be able to pass-on/relay a list of arguments use only two double quotes
CreateObject(&quot;Wscript.Shell&quot;).Run &quot;&quot; &amp; WScript.Arguments(0) &amp; &quot;&quot;, 0, False

Example: Invisible.vbs &quot;Kill.vbs ME.exe&quot;
Solution 2:
Use a command line tool to silently launch a process : Quiet, hidecon or hideexec.

**参考链接**: https://superuser.com/questions/62525/how-to-run-a-batch-file-in-a-completely-hidden-way

> 📎 来源 / Source: https://superuser.com/questions/62525/how-to-run-a-batch-file-in-a-completely-hidden-way

#### 97. Apostrophes and double quotes don&#39;t show up until I type the next letter

**故障现象**: Apostrophes and double quotes don&#39;t show up until I type the next letter
**标签 / 来源**: Tags: windows, windows-xp, keyboard | superuser | 👍 188 | 💬 12 answers

**问题描述**:
Tags: windows, windows-xp, keyboard | Score: 188 | Views: 407550 | Answers: 12

**解决方法 / 社区答案**:
The reason is because you are using US-international keyboard. 

Here is how to change this:


In the Windows run box (Windows+R) type control intl.cpl or control international.
Click the "Keyboards and Languages" tab
Click "Change Keyboards..."
AT THIS POINT MAKE SURE YOU ARE USING "English (United Kingdom) - US" as the default input language, meaning you set the keyboard to US, not US-international

**参考链接**: https://superuser.com/questions/122625/apostrophes-and-double-quotes-dont-show-up-until-i-type-the-next-letter

> 📎 来源 / Source: https://superuser.com/questions/122625/apostrophes-and-double-quotes-dont-show-up-until-i-type-the-next-letter

#### 98. Why does 64-bit Windows need a separate &quot;Program Files (x86)&quot; folder?

**故障现象**: Why does 64-bit Windows need a separate &quot;Program Files (x86)&quot; folder?
**标签 / 来源**: Tags: windows, 64-bit | superuser | 👍 184 | 💬 11 answers

**问题描述**:
Tags: windows, 64-bit | Score: 184 | Views: 106592 | Answers: 11

**解决方法 / 社区答案**:
Short answer: To ensure legacy 32-bit applications continue to work the same way they used to without imposing ugly rules on 64-bit applications that would create a permanent mess.

It is not necessary. It's just more convenient than other possible solutions such as requiring every application to create its own way to separate 32-bit DLLs and executables  from 64-bit DLLs and executables.

The main reason is to make 32-bit applications that don't even know 64-bit systems exist "just work", even if 64-bit DLLs are installed in places the applications might look. A 32-bit application won't be able to load a 64-bit DLL, so a method was needed to ensure that a 32-bit application (that might pre-date 64-bit systems and thus have no idea 64-bit files even exist) wouldn't find a 64-bit DLL, try to load it, fail, and then generate an error message.

The simplest solution to this is consistently separate directories. Really the only alternative is to require every 64-bit application to "hide" its executable files somewhere a 32-bit application wouldn't look, such as a bin64 directory inside that application. But that would impose permanent ugliness on 64-bit systems just to support legacy applications.

**参考链接**: https://superuser.com/questions/442246/why-does-64-bit-windows-need-a-separate-program-files-x86-folder

> 📎 来源 / Source: https://superuser.com/questions/442246/why-does-64-bit-windows-need-a-separate-program-files-x86-folder

#### 99. Why does the /winsxs folder grow so large, and can it be made smaller?

**故障现象**: Why does the /winsxs folder grow so large, and can it be made smaller?
**标签 / 来源**: Tags: windows, disk-space, winsxs | superuser | 👍 183 | 💬 12 answers

**问题描述**:
Tags: windows, disk-space, winsxs | Score: 183 | Views: 128714 | Answers: 12

**解决方法 / 社区答案**:
There is a nice command that cleans up after a Windows 7 SP1 installation (it saved me around 3&nbsp;GB):

DISM /online /cleanup-Image /spsuperseded


Must be executed from an elevated command prompt

**参考链接**: https://superuser.com/questions/1/why-does-the-winsxs-folder-grow-so-large-and-can-it-be-made-smaller

> 📎 来源 / Source: https://superuser.com/questions/1/why-does-the-winsxs-folder-grow-so-large-and-can-it-be-made-smaller

#### 100. What utility can move my Windows boot partition over to another hard drive?

**故障现象**: What utility can move my Windows boot partition over to another hard drive?
**标签 / 来源**: Tags: windows, hard-drive, boot, backup, partitioning | superuser | 👍 182 | 💬 18 answers

**问题描述**:
Tags: windows, hard-drive, boot, backup, partitioning | Score: 182 | Views: 440315 | Answers: 18

**解决方法 / 社区答案**:
DriveImage XML
DriveImage XML will do the job.  It runs from within Windows and it can copy directly from drive to drive.  A lot of people rave about it after good experiences with the software.


DriveImage XML is an easy to use and reliable program for imaging and backing up partitions and logical drives.
Image creation uses Microsoft's Volume Shadow Services (VSS), allowing you to create safe &quot;hot images&quot; even from drives currently in use. Images are stored in XML files, allowing you to process them with 3rd party tools. Never again be stuck with a useless backup! Restore images to drives without having to reboot. DriveImage XML is now faster than ever, offering two different compression levels.


EASEUS Disk Copy
EASEUS Disk Copy is a great alternative if you don't want to go for a 'hot' backup that runs from within Windows.  Good review at lifehacker and on a par with DriveImage XML.  They quite clearly state that it is ideal for moving from one disk to a larger one.  Like other suggestions, this requires that you create a boot CD.

EASEUS Disk Copy is a potent freeware
providing sector-by-sector
disk/partition clone regardless of
your operating system, file systems
and partition scheme by creating a
bootable CD. The sector-by-sector
method assures you a copy 100%
identical to the original. Disk Copy
can be used for copy, cloning, or
upgrading your original small hard
drive to a new larger drive. Simply
speaking, it can copy anything from
the old hard drive including the
deleted, lost files and inaccessible
data. So, the freeware is a perfect
tool for Data Recovery Wizard to
recover files from a backup disk.

**参考链接**: https://superuser.com/questions/32164/what-utility-can-move-my-windows-boot-partition-over-to-another-hard-drive

> 📎 来源 / Source: https://superuser.com/questions/32164/what-utility-can-move-my-windows-boot-partition-over-to-another-hard-drive


---

## English 🇺🇸
**Windows Common Issues & Solutions**

Auto-updated hourly from Stack Exchange: common WINDOWS issues and community-verified solutions.

### WINDOWS Common Issues & Solutions

#### 1. Find out which process is locking a file or folder in Windows

**Issue**: Find out which process is locking a file or folder in Windows
**Tags / Source**: Tags: windows, filesystems, process, community-faq-proposed | superuser | 👍 1331 | 💬 16 answers

**Description**:
Tags: windows, filesystems, process, community-faq-proposed | Score: 1331 | Views: 2068503 | Answers: 16

**Solution / Community Answer**:
You can use the Resource Monitor for this which comes built-in with Windows 7, 8, 10 and 11!

Open Resource Monitor, which can be found

By searching for Resource Monitor or  resmon.exe in the start menu, or
As a button on the Performance tab in your Task Manager


Go to the CPU tab
In the Processes section, select all processes by clicking the checkbox next to &quot;Image&quot; in the headers.
Use the search field in the Associated Handles section

See blue arrow in screen shot below



When you've found the handle, you can identify the process by looking at the Image and/or PID column.
You can then try to close the application as you normally would, or, if that's not possible, just right-click the handle and kill the process directly from there. Easy peasy!

**Reference**: https://superuser.com/questions/117902/find-out-which-process-is-locking-a-file-or-folder-in-windows

> 📎 Source: https://superuser.com/questions/117902/find-out-which-process-is-locking-a-file-or-folder-in-windows

#### 2. What are the Windows A: and B: drives used for?

**Issue**: What are the Windows A: and B: drives used for?
**Tags / Source**: Tags: windows, hard-drive | superuser | 👍 1006 | 💬 20 answers

**Description**:
Tags: windows, hard-drive | Score: 1006 | Views: 531718 | Answers: 20

**Solution / Community Answer**:
Short Version: A: &amp; B: are reserved by floppy disk drives, so C: is used by hard drives for backwards compatibility reasons.



Once upon a time, the early CP/M and IBM PC style computers had no hard drive.  You had one floppy drive, and that was it.  Unless you spent another $1k or so on a second floppy drive, then your system was smokin'!  If you only had one drive it was common to boot from one disk, put in the other disk with your programs and data, then run the program.  Once the program finished, the computer would request that you reinsert the boot disk so you could use the command line again.  Copying data from one disk to the other was a series of

Please insert source disk into drive A:...
Please insert destination disk into drive A:...
Please insert source disk into drive A:...


By the time hard drives became cheap, the "expensive" computers typically had two floppy drives (one to boot and run common programs, one to save data and run specific programs). And so it was common for the motherboard hardware to support two floppy drives at fixed system addresses.  Since it was built into the hardware, it was thought that building the same requirement into the OS was acceptable, and any hard drives added to the machine would start with disk C: and so forth.

During the transition from 5.25" disks (which were actually, physically floppy) to 3.5" disks (which were encased in a harder plastic shell) it was common to have both drives in one system, and again it was supported on the motherboard with hardware, and in the OS at fixed addresses.  As very few systems ran out of drive letters, it was not thought to be important to consider making those drives re-assignable in the OS until much later when drives were abstracted along with addresses due to the plug'n'play standard.

A lot of software was developed since that time, and unfortunately much of it expected to see long-term storage on the C: drive.  This includes the BIOS software that boots the computer.  You can still attach two floppy drives, boot into DOS 6.1, and use it as you would have in the early 90's, with floppy drives A: and B:.

So largely the reason for starting the hard drive at C is for backwards compatibility.  While the OS has abstracted data storage to some degree, it still treats A: and B: differently, in such a way that allows them to be removed from the system without altering the OS, caching them differently, and due to early viruses treating their boot sector with more caution than the hard drive's boot sector.

For Windows specifically, it's worth mentioning that you can use A: and B: as the names for volumes, be it a flash drive or an internal hard drive.

**Reference**: https://superuser.com/questions/231273/what-are-the-windows-a-and-b-drives-used-for

> 📎 Source: https://superuser.com/questions/231273/what-are-the-windows-a-and-b-drives-used-for

#### 3. How can I display the contents of an environment variable from the command prompt in Windows 7?

**Issue**: How can I display the contents of an environment variable from the command prompt in Windows 7?
**Tags / Source**: Tags: windows-7, windows, command-line, environment-variables | superuser | 👍 833 | 💬 8 answers

**Description**:
Tags: windows-7, windows, command-line, environment-variables | Score: 833 | Views: 3005018 | Answers: 8

**Solution / Community Answer**:
In Windows Command-Prompt the syntax is echo %PATH%
To get a list of all environment variables enter the command set without any parameters.
To send those variables to a text file enter the command set &gt; filename.txt

Related

How to list global environment variables separately from user-specific environment variables?

**Reference**: https://superuser.com/questions/341192/how-can-i-display-the-contents-of-an-environment-variable-from-the-command-promp

> 📎 Source: https://superuser.com/questions/341192/how-can-i-display-the-contents-of-an-environment-variable-from-the-command-promp

#### 4. How to *disable* automatic reboots in Windows 10?

**Issue**: How to *disable* automatic reboots in Windows 10?
**Tags / Source**: Tags: windows-10, windows-update, reboot | superuser | 👍 676 | 💬 20 answers

**Description**:
Tags: windows-10, windows-update, reboot | Score: 676 | Views: 402626 | Answers: 20

**Solution / Community Answer**:
Note: Unfortunately this appears to not work on Windows 10 Home, and I'm not sure of a workable solution for users of this edition.

I posted this as an answer on another question, but as that appears to be a duplicate of this question I'll provide it here too:
You can edit your local group policy settings to force Windows update to only download updates, but wait for your input to install (and therefore reboot.)
Open your start menu and type Group, then click Edit group policy
Expand either (depending on Windows 10 or 11 version):

Computer Configuration \ Administrative Templates \ Windows Components \ Windows Update
or: Computer Configuration \ Administrative Templates \ Windows Components \ Manage end user experiences \ Windows Update
or: Computer Configuration \ Administrative Templates \ All Settings


Double click Configure Automatic Updates and enable the policy, and configure it as needed.

Head back to Windows Update and click Check for updates. Once it is done, click on the Advanced options
You should see your new settings being 'enforced.'

After applying this setting on a test VM, I left Windows Update open and noticed it started downloading.

When it finishes downloading, you get a toast notification that there are updates and you need to install them.

Note that you must click install now. Restarting or shutting down from the start menu does not appear to trigger the install process.

More info:
I'm not sure if editing Local Group Policy is an option in the Home edition of Windows 10, but the same result should be possible through the registry (I haven't tested this as I used the policy method myself). Including this in case non-pro users come looking for an answer too.

Press Win + R and type regedit then hit Enter

Navigate to HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU
(you may need to create the keys manually if they don't exist)

Create a new DWORD value called AUOptions and enter a value of either 2 or 3.
2 = Notify before download
3 = Automatically download and notify of installation

Restart PC

Check for updates

Inspect Advanced Settings



Update following Anniversary Update (1607):
I've seen a lot a few comments lately from people saying this no longer works after the Anniversary Update.
I've been running some tests, detailed in the two blog posts here:

Validating Prevention of Automatic Reboots on Windows 10, Version 1607
Update on Windows Update... Up Time

These tests have been running for nearly three weeks and I have yet to see any forced reboots.
In light of these results, it appears that this does still work.

Things to keep in mind:

I did not set any settings around Active Hours or the Reboot Options.
DO NOT click the 'Install now' button within the Windows Update UI unless you're ready to install and reboot. Once the updates are installed, there is no stopping Windows from deciding to reboot.
Windows will nag you with Toasts, Action Center alerts and banners across your screen. As long as you don't install the updates you're fine (but do do them eventually.)

**Reference**: https://superuser.com/questions/957267/how-to-disable-automatic-reboots-in-windows-10

> 📎 Source: https://superuser.com/questions/957267/how-to-disable-automatic-reboots-in-windows-10

#### 5. &quot;directory junction&quot; vs &quot;directory symbolic link&quot;?

**Issue**: &quot;directory junction&quot; vs &quot;directory symbolic link&quot;?
**Tags / Source**: Tags: windows, filesystems, ntfs, symbolic-link | superuser | 👍 609 | 💬 3 answers

**Description**:
Tags: windows, filesystems, ntfs, symbolic-link | Score: 609 | Views: 462514 | Answers: 3

**Solution / Community Answer**:
A junction is definitely not the same thing as a directory symbolic link, although they behave similarly.  The main difference is that, if you are looking at a remote server, junctions are processed at the server and directory symbolic links are processed at the client.  Also see Matthew's comment on the fact that this means symbolic links on the local file system can point to remote file systems.

Suppose that on a machine named Alice you were to put a junction point c:\myjp and a directory symbolic link c:\mysymlink, both pointing to c:\targetfolder.  While you're using Alice you won't notice much difference between them.  But if you're using another machine named Bob, then the junction point

\\Alice\c$\myjp will point to \\Alice\c$\targetfolder

but the symbolic link

\\Alice\c$\mysymlink will point to \\Bob\c$\targetfolder

(Caveat: by default, the system doesn't follow symlinks on remote volumes, so in most cases the second example will actually result in either "File Not Found" or "The symbolic link cannot be followed because its type is disabled.")

The difference between a directory symbolic link and a file symbolic link is simply that one represents a directory and one represents a file.  Since the target of the link doesn't need to exist when the link is created, the file system needs to know whether to tell applications that it is a directory or not.

It should also be noted that creating a symbolic link requires special privilege (by default, only available to elevated processes) whereas creating a junction only requires access to the file system.

**Reference**: https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link

> 📎 Source: https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link

#### 6. How do I run multiple commands on one line in PowerShell?

**Issue**: How do I run multiple commands on one line in PowerShell?
**Tags / Source**: Tags: windows, command-line, powershell | superuser | 👍 603 | 💬 5 answers

**Description**:
Tags: windows, command-line, powershell | Score: 603 | Views: 893175 | Answers: 5

**Solution / Community Answer**:
Use a semicolon to chain commands in PowerShell:

ipconfig /release; ipconfig /renew

**Reference**: https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell

> 📎 Source: https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell

#### 7. Windows 7 SP1 Windows Update stuck checking for updates

**Issue**: Windows 7 SP1 Windows Update stuck checking for updates
**Tags / Source**: Tags: windows-7, windows, windows-update | superuser | 👍 561 | 💬 13 answers

**Description**:
Tags: windows-7, windows, windows-update | Score: 561 | Views: 3337928 | Answers: 13

**Solution / Community Answer**:
Fix

Microsoft released a Windows Update Client Update which is part of the July 2016 Update Rollup to fix the long hang at Windows Update scan.


  This update contains some improvements to Windows Update Client in
  Windows 7 Service Pack 1 (SP1). This includes the following:
  
  
  An optimization that addresses long scan time for updates that's reported on some computers.
  



Download:


32 Bit
64 Bit

Stop Windows Update service. This speeds up the setup of MSU updates and the useless steps from Moab are not required (reboot causes that the WU service is stopped until it gets started via trigger when Internet is available). This can be done from the command line, or from the Service Manager window.
Try the downloaded update and see if it speeds up the installation of Updates.


To be able to install the update you first need to install the April 2015 servicing stack update for Windows 7 and Windows Server 2008 R2 update (again, stop WU service before trying to install the MSU).

Download (April 2015 servicing stack update): 


32 Bit
64 Bit


Workaround 1

If this is still not helping to search for new updates, use WSUSOffline to get all the updates.

**Reference**: https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates

> 📎 Source: https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates

#### 8. What is the home directory on Windows Subsystem for Linux?

**Issue**: What is the home directory on Windows Subsystem for Linux?
**Tags / Source**: Tags: windows-10, bash, windows-subsystem-for-linux | superuser | 👍 526 | 💬 11 answers

**Description**:
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 526 | Views: 1498445 | Answers: 11

**Solution / Community Answer**:
In the latest versions [2025 WSL2], the file system is accessed from:
# \\wsl.localhost\&lt;distro name&gt;
shortcut:
# \\wsl$\&lt;Distribution&gt;:
ex:
\\wsl$\Ubuntu

You can also find this path by starting the distro then running $ wslpath -w $HOME
The files themselves seem to be stored within a .vhdx file in a similar location to 2020's solution.
%LOCALAPPDATA%\wsl\&lt;a unique uuid&gt;\ext4.vhdx

For older WSL2 installs [2020] it would be a file like:
%LOCALAPPDATA%\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\ext4.vhdx

For example with Debian the file would be a file that is an ext4 virtual disk:
%LOCALAPPDATA%\Packages\YourDistroName-ID\LocalState, you can see a file named ext4.vhdx

You can find the exact filenames by referencing the registry, ex: powershell:
(Get-ChildItem HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | ForEach-Object {Get-ItemProperty $_.PSPath}) | select DistributionName,BasePath,VhdFileName

Also useful if a distro isn't installed in the standard directory, doesn't seem possible to get using wsl command from the command prompt.
Previously, in 2018, The root Linux path was related to which distribution you had installed from the Microsoft Store rather than one global path; for Ubuntu, it was located at:
%LOCALAPPDATA%\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs

but with the files stored directly on the NTFS file system.

**Reference**: https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux

> 📎 Source: https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux

#### 9. Can I delete the folder C:\ProgramData\Package Cache\?

**Issue**: Can I delete the folder C:\ProgramData\Package Cache\?
**Tags / Source**: Tags: windows, disk-space | superuser | 👍 523 | 💬 10 answers

**Description**:
Tags: windows, disk-space | Score: 523 | Views: 870931 | Answers: 10

**Solution / Community Answer**:
TL;DR: Do NOT delete this folder
(see below for workarounds)

Why Not?
There have been conflicting reports about whether the absence of this folder (as a consequence of deleting it) will actually and in all cases cause issues with the visual studio installation, i.e. during normal operation, during reinstall, patch/upgrade, repair install, or uninstall.  However, the recommendation from MICROSOFT is clearly to NOT DELETE IT.
From Microsoft Developer Tools Blogs → HERE

When repairing, modifying, or uninstalling a product or when
installing or uninstalling a patch, if source media is required the
package cache is used automatically and most users will never see a
prompt. Only if the package cache is missing or incomplete will Visual
Studio setup prompt to download (if connected) or locate media as
shown in the screenshot below.

Users who have installed from media even get the option to download
(if connected). So while very few customers should ever see this
dialog, we wanted to make sure the experience was easy.
Even though we
will prompt to download packages to the cache if missing, we recommend
users do not remove the package cache. Not only is the cached used by
many other products that are installed with Burn and may not provide the same download experience, there are scenarios when
Windows Installer may require source that we cannot handle because our
code is not running.


Solution/Work-Around:#
If you need to reclaim this space, your safest bet is to avoid &quot;deleting&quot; anything, but to instead, move this folder and all it's files.  You can safely do this following the instructions below to any local/live, online, near-line, or offline storage as long as that storage system that can be mounted to a drive letter or any mount point on the NTFS file system.  Any of the following will work:

another live (mounted) partition
an optical disc (CD, DVD, etc.) with a live filesystem like FAT, or NTFS
an external hard drive
a USB drive
a network drive

Whenever you are prompted for the media/receive any errors about missing files/missing location, you simply make sure to remount/reinsert your drive/media if it's not already a live partition.
Once moved, in order to &quot;link&quot; the old mount point/location (in most cases C:\ProgramData\Package Cache\), you simply create a directory junction to it.
Junctions are recognized at the file system level as an alias entry in the FSTAB.  Therefore, it's transparent to all programs, including the OS itself.  In other words, it is NOT seen as a file that simply points to another location (like a shortcut) and therefore always works without incident.

You would move the folder(s) in question to its new location

Create the junction

Option 1. (natively): Just issue the built-in Windows Vista / 7 / 8 command and the cmd prompt:
  mklink /J link-(new location) target-(original folder)



NOTE:  If you make the newpath absolute, you'll be able to move link without breaking the pointer to the newpath. If you make the newpath relative, you'll be able prevent breaking the link, as long as you move BOTH the link and target TOGETHER and maintain their relative paths.

Option 2. (using a tool):  Another GREAT alternative is a free handy utility I've been using for years called &quot;Link Shell Extension&quot;.  LSE is free and you can find it here (or Google for it): http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html
LSE allows you to create symlinks, hardlinks, junctions, smartcopies, smartclones, smart mirrors, smart moves, splices, multiple sources, and bunch of other stuff I found too confusing to read, frankly.  But, it's a brilliant free product that creates a Windows Explorer context menu that allows you right-click on your LINK-TARGET folder then drag it to where you'd like to create the actual link. You can of course rename the link to anything you'd like.

**Reference**: https://superuser.com/questions/455853/can-i-delete-the-folder-c-programdata-package-cache

> 📎 Source: https://superuser.com/questions/455853/can-i-delete-the-folder-c-programdata-package-cache

#### 10. How to check if a binary is 32- or 64-bit on Windows?

**Issue**: How to check if a binary is 32- or 64-bit on Windows?
**Tags / Source**: Tags: windows, binary-files, 32-vs-64-bit | superuser | 👍 522 | 💬 32 answers

**Description**:
Tags: windows, binary-files, 32-vs-64-bit | Score: 522 | Views: 509026 | Answers: 32

**Solution / Community Answer**:
After examining header values from Richard's answer, I came up with a solution which is fast, easy, and only requires a text editor. Even Windows' default notepad.exe would work.

Open the executable in a text editor. You might have to drag-and-drop or use
the editor's Open... dialog, because Windows doesn't show Open with... option in the context menu for executables.

Check the first printable characters after the first occurrence of PE. This part is most likely to be surrounded by at least some whitespace (could be a lot of it), so it can be easily done visually.


Here is what you're going to find:
32-bit:
PE  L

64-bit:
PE  d†

A word of warning: using default Notepad on big files can be very slow, so better not use it for files larger than a megabyte or a few. In my case, it took about 30 seconds to display a 12 MiB file. Notepad++, however, was able to display a 120 MiB executable almost instantly.
This is solution might be useful in case you need to inspect a file on a machine you can't install any additional software on.
Additional info:
If you have a HEX-Editor available, the location of PE Signature is located at offset 0x3C. The signature is PE\0\0 (letters &quot;P&quot; and &quot;E&quot; followed by two null bytes), followed by a two-byte Machine Type in Little Endian.
The signature is usually further ahead in MZ files.
The relevant values are 0x8664 for a 64-bit executable and 0x014c for a 32-bit one (64 86 and 4c 01 respectively when adjusted for endianness, but any decent hex editor will automatically handle endianness when you search for a hex value). There are a lot more possible values, but you probably won't ever encounter any of these, or be able to run such executables on your Windows PC.
Full list of machine types, along with the rest of .exe specifications, can be found in Microsoft PE and COFF Specification Machine Types section.

**Reference**: https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows

> 📎 Source: https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows

#### 11. Create/rename a file/folder that begins with a dot in Windows?

**Issue**: Create/rename a file/folder that begins with a dot in Windows?
**Tags / Source**: Tags: windows | superuser | 👍 520 | 💬 12 answers

**Description**:
Tags: windows | Score: 520 | Views: 316540 | Answers: 12

**Solution / Community Answer**:
To create/rename on windows explorer, just rename to .name. - The additional dot at the end is necessary, and will be removed by Windows Explorer.

To create a new file begins with a dot, on command prompt:

echo testing &gt; .name

**Reference**: https://superuser.com/questions/64471/create-rename-a-file-folder-that-begins-with-a-dot-in-windows

> 📎 Source: https://superuser.com/questions/64471/create-rename-a-file-folder-that-begins-with-a-dot-in-windows

#### 12. Is there any &#39;sudo&#39; command for Windows?

**Issue**: Is there any &#39;sudo&#39; command for Windows?
**Tags / Source**: Tags: windows, command-line, privileges | superuser | 👍 518 | 💬 19 answers

**Description**:
Tags: windows, command-line, privileges | Score: 518 | Views: 916657 | Answers: 19

**Solution / Community Answer**:
The runas command.

runas [{/profile|/noprofile}] [/env] [/netonly] [/smartcard] [/showtrustlevels] [/trustlevel] /user:UserAccountName program


Just run:

runas /noprofile /user:Administrator cmd 


to start a command shell as a administrator

**Reference**: https://superuser.com/questions/42537/is-there-any-sudo-command-for-windows

> 📎 Source: https://superuser.com/questions/42537/is-there-any-sudo-command-for-windows

#### 13. How do I exit telnet?

**Issue**: How do I exit telnet?
**Tags / Source**: Tags: windows, telnet | superuser | 👍 512 | 💬 6 answers

**Description**:
Tags: windows, telnet | Score: 512 | Views: 910606 | Answers: 6

**Solution / Community Answer**:
It should have printed something along the lines of:

Escape character is '^]'.


Since ^X is  CtrlX, try Ctrl] for ^]. 

You should then enter the telnet console, where you can enter quit to leave telnet.

**Reference**: https://superuser.com/questions/486496/how-do-i-exit-telnet

> 📎 Source: https://superuser.com/questions/486496/how-do-i-exit-telnet

#### 14. Windows SSH: Permissions for &#39;private-key&#39; are too open

**Issue**: Windows SSH: Permissions for &#39;private-key&#39; are too open
**Tags / Source**: Tags: windows, ssh, permissions, openssh, private-key | superuser | 👍 498 | 💬 18 answers

**Description**:
Tags: windows, ssh, permissions, openssh, private-key | Score: 498 | Views: 1047407 | Answers: 18

**Solution / Community Answer**:
You locate the file in Windows Explorer, right-click on it then select "Properties". Navigate to the "Security" tab and click "Advanced".

Change the owner to you, disable inheritance and delete all permissions. Then grant yourself "Full control" and save the permissions. Now SSH won't complain about file permission too open anymore.

It should end up looking like this:

**Reference**: https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

> 📎 Source: https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

#### 15. How to download files from command line in Windows like wget or curl

**Issue**: How to download files from command line in Windows like wget or curl
**Tags / Source**: Tags: windows, wget, curl | superuser | 👍 490 | 💬 21 answers

**Description**:
Tags: windows, wget, curl | Score: 490 | Views: 1880087 | Answers: 21

**Solution / Community Answer**:
An alternative I discovered recently, using PowerShell:

$client = new-object System.Net.WebClient
$client.DownloadFile("http://www.xyz.net/file.txt","C:\tmp\file.txt")


It works as well with GET queries.

If you need to specify credentials to download the file, add the following line in between:

$client.Credentials =  Get-Credential                


A standard windows credentials prompt will pop up. The credentials you enter there will be used to download the file. You only need to do this once for all the time you will be using the $client object.

**Reference**: https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl

> 📎 Source: https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl

#### 16. How can I free up drive space from the Windows installer folder without killing Windows?

**Issue**: How can I free up drive space from the Windows installer folder without killing Windows?
**Tags / Source**: Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | superuser | 👍 486 | 💬 8 answers

**Description**:
Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | Score: 486 | Views: 1073383 | Answers: 8

**Solution / Community Answer**:
I created "PatchCleaner" to clean the windows installer directory of all orphaned files in one easy click. If you don't trust the app to do the right thing, use the move feature to put them somewhere safe in case you need them back in the future. I have run it on multiple machines and saved up to 15Gb of space :-)

Run PatchCleaner after windows updates to find newly orphaned files.

I recommend you use the Move action, and move the orphaned patches to external storage, just to be safe

PatchCleaner @ HomeDev

Known Issues (full details on website)


Adobe Reader can fail to update after running PatchCleaner.


NOTE: as @ Feb-2016 version 1.4.1.0 is out that has a fix to allow customisable filters to exclude adobe reader from being incorrectly detected.

**Reference**: https://superuser.com/questions/707767/how-can-i-free-up-drive-space-from-the-windows-installer-folder-without-killing

> 📎 Source: https://superuser.com/questions/707767/how-can-i-free-up-drive-space-from-the-windows-installer-folder-without-killing

#### 17. How can I remove malicious spyware, malware, adware, viruses, trojans or rootkits from my PC?

**Issue**: How can I remove malicious spyware, malware, adware, viruses, trojans or rootkits from my PC?
**Tags / Source**: Tags: windows, anti-virus, virus, malware, community-faq | superuser | 👍 474 | 💬 18 answers

**Description**:
Tags: windows, anti-virus, virus, malware, community-faq | Score: 474 | Views: 333616 | Answers: 18

**Solution / Community Answer**:
Here's the thing: Malware in recent years has become both sneakier and nastier:
Sneakier, not only because it's better at hiding with rootkits or EEPROM hacks, but also because it travels in packs. Subtle malware can hide behind more obvious infections. There are lots of good tools listed in answers here that can find 99% of malware, but there's always that 1% they can't find yet. Mostly, that 1% is stuff that is new: the malware tools can't find it because it just came out and is using some new exploit or technique to hide itself that the tools don't know about yet.
Malware also has a short shelf-life. If you're infected, something from that new 1% is very likely to be one part of your infection. It won't be the whole infection: just a part of it. Security tools will help you find and remove the more obvious and well-known malware, and most likely remove all of the visible symptoms (because you can keep digging until you get that far), but they can leave little pieces behind, like a keylogger or rootkit hiding behind some new exploit that the security tool doesn't yet know how to check. In this way, malware can be extra sneaky and survive even skilled and persistent attempts to purge it. The anti-malware tools still have their place, but I'll get to that later.
Nastier, in that it won't just show ads, install a toolbar, or use your computer as a zombie anymore. Modern malware is likely to go right for the banking or credit card information. The people building this stuff are no longer just script kiddies looking for fame; they are now organized professionals motivated by profit, and if they can't steal from you directly, they'll look for something they can turn around and sell. This might be processing or network resources in your computer, but it might also be your social security number or encrypting your files and holding them for ransom.

Put these two factors together, and it's no longer worthwhile to even attempt to remove malware from an installed operating system. I used to be very good at removing this stuff, to the point where I made a significant part of my living that way, and I no longer even make the attempt. I'm not saying it can't be done, but I am saying that the cost/benefit and risk analysis results have changed: it's just not worth it anymore. There's too much at stake, and it's too easy to get results that only seem to be effective.
Lots of people will disagree with me on this, but I challenge they are not weighing consequences of failure strongly enough. Are you willing to wager your life savings, your good credit, even your identity, that you're better at this than crooks who make millions doing it every day?  If you try to remove malware and then keep running the old system, that's exactly what you're doing.
I know there are people out there reading this thinking, &quot;Hey, I've removed several infections from various machines and nothing bad ever happened.&quot; Me too, friend. Me too. In days past I have cleaned my share of infected systems. Nevertheless, I suggest we now need to add &quot;yet&quot; to the end of that statement. You might be 99% effective, but you only have to be wrong one time, and the consequences of failure are much higher than they once were; the cost of just one failure can easily outweigh all of the other successes. You might even have a machine already out there that still has a ticking time bomb inside, just waiting to be activated or to collect the right information before reporting it back. Even if you have a 100% effective process now, this stuff changes all the time. Remember: you have to be perfect every time; the bad guys only have to get lucky once.
In summary, it's unfortunate, but if you have a confirmed malware infection, a complete re-pave of the computer should be the first place you turn instead of the last.

Here's how to accomplish that:
Before you're infected, make sure you have a way to re-install any purchased software, including the operating system, that does not depend on anything stored on your internal hard disk. For this purpose, that normally just means hanging onto cd/dvds or product keys, but the operating system may require you to create recovery disks yourself.1 Don't rely on a recovery partition for this. If you wait until after an infection to ensure you have what you need to re-install, you may find yourself paying for the same software again. With the rise of ransomware, it's also extremely important to take regular backups of your data (plus, you know, regular non-malicious things like hard drive failure).
When you suspect you have malware, look to other answers here. There are a lot of good tools suggested. My only issue is the best way to use them: I only rely on them for the detection. Install and run the tool, but as soon as it finds evidence of a real infection (more than just &quot;tracking cookies&quot;) just stop the scan: the tool has done its job and confirmed your infection.2
At the time of a confirmed infection, take the following steps:

Check your credit and bank accounts. By the time you find out about the infection, real damage may have already been done. Take any steps necessary to secure your cards, bank account, and identity.
Change passwords at any web site you accessed from the compromised computer. Do not use the compromised computer to do any of this.
Take a backup of your data (even better if you already have one).
Re-install the operating system using original media obtained directly from the OS publisher. Make sure the re-install includes a complete re-format of your disk; a system restore or system recovery operation is not enough.
Re-install your applications.
Make sure your operating system and software is fully patched and up to date.
Run a complete anti-virus scan to clean the backup from step three.
Restore the backup.

If done properly, this is likely to take between two and six real hours of your time, spread out over two to three days (or even longer) while you wait for things like apps to install, windows updates to download, or large backup files to transfer... but it's better than finding out later that crooks drained your bank account. Unfortunately, this is something you should do yourself, or a have a techy friend do for you. At a typical consulting rate of around $100/hr, it can be cheaper to buy a new machine than pay a shop to do this. If you have a friend do it for you, do something nice to show your appreciation. Even geeks who love helping you set up new things or fix broken hardware often hate the tedium of clean-up work. It's also best if you take your own backup... your friends aren't going to know where you put what files, or which ones are really important to you. You're in a better position to take a good backup than they are.
Soon even all of this may not be enough, as there is now malware capable of infecting firmware. Even replacing the hard drive may not remove the infection, and buying a new computer will be the only option. Thankfully, at the time I'm writing this we're not to that point yet, but the day is definitely approaching fast.

If you absolutely insist, beyond all reason, you really want to clean your existing install rather than start over, then for the love of God make sure whatever method you use involves one of the following two procedures:

Remove the hard drive and connect it as a guest disk in a different (clean!) computer to run the scan.

OR

Boot from a CD/USB key with its own set of tools running its own kernel. Make sure the image for this is obtained and burned on a clean computer. If necessary, have a friend make the disk for you.

Under no circumstances should you try to clean an infected operating system using software running as a guest process of the compromised operating system. That's just plain dumb.

Of course, the best way to fix an infection is to avoid it in the first place, and there are some things you can do to help with that:

Keep your system patched. Make sure you promptly install Windows Updates, Adobe Updates, Java Updates, Apple Updates, etc. This is far more important even than anti-virus software, and for the most part it's not that hard, as long as you keep current. Most of those companies have informally settled on all releasing new patches on the same day each month, so if you keep current it doesn't interrupt you that often. Forced Windows Update reboots typically only happen when you ignore the notices for too long. If this happens to you often, it's on you to change your behavior. These are important, and it's not okay to continually just choose the &quot;install later&quot; option, even if it's easier in the moment.

Do not run as administrator by default. In recent versions of Windows, it's as simple as leaving the UAC feature turned on. Keeping an second administrator account distinct from your normal day to day account is even better.

Use a good firewall tool. These days the default firewall in Windows is actually good enough. You may want to supplement this layer with something like WinPatrol that helps stop malicious activity on the front end. Windows Defender works in this capacity to some extent as well. Basic Ad-Blocker browser plugins are also becoming increasingly useful at this level as a security tool.

Set most browser plug-ins (especially Flash and Java) to &quot;Ask to Activate&quot;.

Run current anti-virus software. This is a distant fifth to the other options, as traditional A/V software often just isn't that effective anymore. It's also important to emphasize the &quot;current&quot;. You could have the best antivirus software in the world, but if it's not up to date, you may just as well uninstall it.
For this reason, I currently recommend Microsoft Defender. There are likely far better scanning engines out there, but Microsoft Defender is built into Windows and will keep itself up to date via the normal Windows Update mechanism, without ever risking an expired registration. AVG and Avast also work well in this way. I just can't recommend any anti-virus software you have to actually pay for, because it's just far too common a paid subscription lapses and you end up with out-of-date definitions.
It's also worth noting here that Mac users now need to run antivirus software, too. The days when they could get away without it are long gone. As an aside, I think it's hilarious I now must recommend Mac users buy anti-virus software, but advise Windows users against it.

Avoid torrent sites, warez, pirated software, and pirated movies/videos. This stuff is often injected with malware by the person who cracked or posted it — not always, but often enough to avoid the whole mess. It's part of why a cracker would do this: often they will get a cut of any profits.

Use your head when browsing the web. You are the weakest link in the security chain. If something sounds too good to be true, it probably is. The most obvious download button is rarely the one you want to use any more when downloading new software, so make sure to read and understand everything on the web page before you click that link. If you see a pop up or hear an audible message asking you to call Microsoft or install some security tool, it's a fake.
Also, prefer to download the software and updates/upgrades directly from vendor or developer rather than third party file hosting websites.



1 Microsoft now publishes the Windows 10 install media so you can legally download and write to an 8GB or larger flash drive for free. You still need a valid license, but you don't need a separate recovery disk for the basic operating system any more.
2 This is a good time to point out I have softened my approach somewhat. Today, most &quot;infections&quot; fall under the category of PUPs (Potentially Unwanted Programs) and browser extensions included with other downloads. Often these PUPs/extensions can safely be removed through traditional means, and they are now a large enough percentage of malware that I may stop at this point and simply try the Add/Remove Programs feature or normal browser option to remove an extension. However, at the first sign of something deeper — any hint the software won't just uninstall normally — and it's back to repaving the machine.

**Reference**: https://superuser.com/questions/100360/how-can-i-remove-malicious-spyware-malware-adware-viruses-trojans-or-rootkit

> 📎 Source: https://superuser.com/questions/100360/how-can-i-remove-malicious-spyware-malware-adware-viruses-trojans-or-rootkit

#### 18. How to rename the User folder in Windows 10?

**Issue**: How to rename the User folder in Windows 10?
**Tags / Source**: Tags: windows, windows-10, microsoft-onedrive | superuser | 👍 468 | 💬 11 answers

**Description**:
Tags: windows, windows-10, microsoft-onedrive | Score: 468 | Views: 1824063 | Answers: 11

**Solution / Community Answer**:
Microsoft has actually documented a very simple and clean way to rename a user profile folder.
EDIT Feb 2022: If you plan to use winget to manage your Windows installations at any point, note that Microsoft now warns against using this procedure under Windows 10 or later as it can stop winget working. Information about winget
There is no need to create a new user account, so all the settings associated with the existing user profile are preserved. And the only registry change required is to edit a single string value (the one that tells Windows the path of the user profile folder):


Log in by using another administrative account.

Note. You may need to create a new Administrative account at first.

Go to the C:\users\ folder and rename the subfolder with the original user name to the new user name.
Go to the registry and modify the registry value ProfileImagePath to the new path name.HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\&lt;User SID&gt;\


That's it!
The procedure quoted above was provided by Microsoft (here) in relation to a perceived issue with Windows 7, and continues to work in Windows 10.

Notes
&lt;User SID&gt;
The ProfileList registry key contains a number of sub-keys. To find out which one to change, click on each sub-key and examine the values, to find the sub-key with the right ProfileImagePath:

For example, let's say we want to get rid of the space in a user profile folder name. So in step 2, we use File Explorer to navigate to C:\Users and rename the John Smith subfolder JohnSmith. And in step 3, we click on the &lt;User SID&gt; sub-keys until we find the one with ProfileImagePath C:\Users\John Smith, and change it to C:\Users\JohnSmith.
Administrative login
You may find you have to restart instead of just logging out and logging back in. Otherwise, when you try to rename the folder, Windows may report that it is being used by another program.
Environment variables (info)
Some applications create env vars with the user profile path fully expanded, so it's advisable to check for these and reboot if any needed fixing.

**Reference**: https://superuser.com/questions/890812/how-to-rename-the-user-folder-in-windows-10

> 📎 Source: https://superuser.com/questions/890812/how-to-rename-the-user-folder-in-windows-10

#### 19. Rebooting Ubuntu on Windows without rebooting Windows?

**Issue**: Rebooting Ubuntu on Windows without rebooting Windows?
**Tags / Source**: Tags: windows-10, windows-subsystem-for-linux | superuser | 👍 453 | 💬 9 answers

**Description**:
Tags: windows-10, windows-subsystem-for-linux | Score: 453 | Views: 990462 | Answers: 9

**Solution / Community Answer**:
You cannot reboot a distro with a single command. You must shut down and boot up the distro with two commands. If you run wsl.exe instead of wsl, then it works both in WSL Bash &amp; CMD.
View the list of distros and their current state:
wsl.exe -l -v

Shutdown everything: Build 18917+
wsl.exe --shutdown

Terminate a specific distro: Windows 1903+
wsl.exe -t &lt;DistroName&gt;

Boot up the default distro (marked with *):
wsl.exe

Boot up a specific distro:
wsl.exe -d &lt;DistroName&gt;


Older versions
# PowerShell (admin)
Restart-Service LxssManager

# or CMD (admin)
net stop LxssManager
net start LxssManager

**Reference**: https://superuser.com/questions/1126721/rebooting-ubuntu-on-windows-without-rebooting-windows

> 📎 Source: https://superuser.com/questions/1126721/rebooting-ubuntu-on-windows-without-rebooting-windows

#### 20. How can I delete a symbolic link in Windows?

**Issue**: How can I delete a symbolic link in Windows?
**Tags / Source**: Tags: windows, windows-7, symbolic-link | superuser | 👍 439 | 💬 13 answers

**Description**:
Tags: windows, windows-7, symbolic-link | Score: 439 | Views: 575992 | Answers: 13

**Solution / Community Answer**:
Be very careful.
If you have a symbolic link that is a directory (made with mklink /d) then using del will delete all of the files in the target directory (the directory that the link points to), rather than just the link.
SOLUTION: rmdir on the other hand will only delete the directory link, not what the link points to.

**Reference**: https://superuser.com/questions/167076/how-can-i-delete-a-symbolic-link-in-windows

> 📎 Source: https://superuser.com/questions/167076/how-can-i-delete-a-symbolic-link-in-windows

#### 21. How to delete directories with path/names too long for normal delete

**Issue**: How to delete directories with path/names too long for normal delete
**Tags / Source**: Tags: windows, file-management | superuser | 👍 433 | 💬 25 answers

**Description**:
Tags: windows, file-management | Score: 433 | Views: 568440 | Answers: 25

**Solution / Community Answer**:
Use the 7-Zip File Manager to delete them.  

If you are still having trouble, ensure that you utilize Shift+Delete inside the 7-Zip File Manager. Otherwise, Windows tries to move them to the Recycle Bin (which will fail again).

**Reference**: https://superuser.com/questions/78434/how-to-delete-directories-with-path-names-too-long-for-normal-delete

> 📎 Source: https://superuser.com/questions/78434/how-to-delete-directories-with-path-names-too-long-for-normal-delete

#### 22. What is the Windows equivalent of the Unix command cat?

**Issue**: What is the Windows equivalent of the Unix command cat?
**Tags / Source**: Tags: windows, command-line, unix, cat | superuser | 👍 433 | 💬 4 answers

**Description**:
Tags: windows, command-line, unix, cat | Score: 433 | Views: 1180582 | Answers: 4

**Solution / Community Answer**:
type
It works across command.com, cmd, and PowerShell (though in the latter it's an alias for Get-Content, so is cat, so you could use either).
From the Wikipedia article (emphasis mine):

In computing, type is a command in various VMS. AmigaDOS, CP/M, DOS, OS/2 and Microsoft Windows command line interpreters (shells) such as COMMAND.COM, cmd.exe, 4DOS/4NT and Windows PowerShell. It is used to display the contents of specified files. It is analogous to the Unix cat command.

C:\&gt;echo hi &gt; a.txt
C:\&gt;echo bye &gt; b.txt
C:\&gt;type a.txt b.txt &gt; c.txt
C:\&gt;type c.txt
hi
bye

**Reference**: https://superuser.com/questions/434870/what-is-the-windows-equivalent-of-the-unix-command-cat

> 📎 Source: https://superuser.com/questions/434870/what-is-the-windows-equivalent-of-the-unix-command-cat

#### 23. Mouse pointer moving on arrow keys pressed in Windows?

**Issue**: Mouse pointer moving on arrow keys pressed in Windows?
**Tags / Source**: Tags: windows-10, mouse | superuser | 👍 399 | 💬 1 answers

**Description**:
Tags: windows-10, mouse | Score: 399 | Views: 212010 | Answers: 1

**Solution / Community Answer**:
Tried killing all running processes on my PC till the problem went away and I can now say for sure the culprit was...
Microsoft Paint
(classic Win32 one)
Apparently it's got a feature that allows moving the mouse pointer using arrow keys, and for some reason sometimes it doesn't stop listening when the window loses focus, so Paint was running in the background since I often use it and it was still doing its job of moving the mouse.
This also explains why the problem can persist after a reboot: when you reboot Windows while Paint is running, Windows will automatically &quot;save your work&quot; and reopen Paint at system boot, causing the bug again!

**Reference**: https://superuser.com/questions/1467313/mouse-pointer-moving-on-arrow-keys-pressed-in-windows

> 📎 Source: https://superuser.com/questions/1467313/mouse-pointer-moving-on-arrow-keys-pressed-in-windows

#### 24. How to disable the &quot;Get Windows 10&quot; icon shown in the notification area (tray)?

**Issue**: How to disable the &quot;Get Windows 10&quot; icon shown in the notification area (tray)?
**Tags / Source**: Tags: windows, windows-10-upgrade | superuser | 👍 394 | 💬 14 answers

**Description**:
Tags: windows, windows-10-upgrade | Score: 394 | Views: 552675 | Answers: 14

**Solution / Community Answer**:
If you just want to remove the tray icon until the next restart you can terminate the GWX.exe process using Task Manager.
To get rid of the icon permanently, uninstall KB3035583 which is responsible for these notifications:
Control panel, windows update, installed updates, sort by name, &quot;Update for Microsoft Windows KB3035583&quot; (not a Security Update), uninstall, reboot.
(Alternative: open CMD and enter wusa /uninstall /KB:3035583)
When you're offered the same again via Windows Update remember to hide it.
After uninstalling, if remnants of the update's files are still in Windows\System32\GWX, just delete that directory, although first you may need to take ownership of it.

**Reference**: https://superuser.com/questions/922068/how-to-disable-the-get-windows-10-icon-shown-in-the-notification-area-tray

> 📎 Source: https://superuser.com/questions/922068/how-to-disable-the-get-windows-10-icon-shown-in-the-notification-area-tray

#### 25. How do you list all processes on the command line in Windows?

**Issue**: How do you list all processes on the command line in Windows?
**Tags / Source**: Tags: windows, command-line | superuser | 👍 387 | 💬 15 answers

**Description**:
Tags: windows, command-line | Score: 387 | Views: 1322569 | Answers: 15

**Solution / Community Answer**:
Working with cmd.exe:

tasklist

If you have Powershell:

get-process

Via WMI:

wmic process

(you can query remote machines as well with /node:ComputerOrIP, and there are a LOT more ways to customize this command: link)

**Reference**: https://superuser.com/questions/914782/how-do-you-list-all-processes-on-the-command-line-in-windows

> 📎 Source: https://superuser.com/questions/914782/how-do-you-list-all-processes-on-the-command-line-in-windows

#### 26. How to recursively delete directory from command line in windows?

**Issue**: How to recursively delete directory from command line in windows?
**Tags / Source**: Tags: windows, command-line, cmd.exe | superuser | 👍 385 | 💬 8 answers

**Description**:
Tags: windows, command-line, cmd.exe | Score: 385 | Views: 958891 | Answers: 8

**Solution / Community Answer**:
deltree if I remember my DOS. 



It seems it's been updated... this is what you want:


  RMDIR /S


This removes the directory C:\test, with prompts :

rmdir c:\test /s


This does the same, without prompts :

rmdir c:\test /s /q


Regarding the sudo part of your question, if you need more priviliges, you can first open a new shell as another user account using the runas command, like this:

runas /user:Administrator cmd
rmdir c:\test /s /q

**Reference**: https://superuser.com/questions/179660/how-to-recursively-delete-directory-from-command-line-in-windows

> 📎 Source: https://superuser.com/questions/179660/how-to-recursively-delete-directory-from-command-line-in-windows

#### 27. How to read ext4 partitions on Windows?

**Issue**: How to read ext4 partitions on Windows?
**Tags / Source**: Tags: windows, filesystems, ext4 | superuser | 👍 377 | 💬 12 answers

**Description**:
Tags: windows, filesystems, ext4 | Score: 377 | Views: 1033431 | Answers: 12

**Solution / Community Answer**:
Ext2Read works well. It can also open &amp; read disk images ( eg: Wubi disk images)


  Ext2Read is an explorer like utility
  to explore ext2/ext3/ext4 files. It
  now supports LVM2 and EXT4 extents. It
  can be used to view and copy files and
  folders. It can recursively copy
  entire folders. It can also be used to
  view and copy disk and file

**Reference**: https://superuser.com/questions/37512/how-to-read-ext4-partitions-on-windows

> 📎 Source: https://superuser.com/questions/37512/how-to-read-ext4-partitions-on-windows

#### 28. Native alternative to wget in Windows PowerShell?

**Issue**: Native alternative to wget in Windows PowerShell?
**Tags / Source**: Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | superuser | 👍 362 | 💬 12 answers

**Description**:
Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | Score: 362 | Views: 684504 | Answers: 12

**Solution / Community Answer**:
Here's a simple PS 3.0 and later one-liner that works and doesn't involve much PS barf:

wget http://blog.stackexchange.com/ -OutFile out.html


Note that:


wget is an alias for Invoke-WebRequest
Invoke-WebRequest returns a HtmlWebResponseObject, which contains a lot of useful HTML parsing properties such as Links, Images, Forms, InputFields, etc., but in this case we're just using the raw Content
The file contents are stored in memory before writing to disk, making this approach unsuitable for downloading large files
On Windows Server Core installations, you'll need to write this as

wget http://blog.stackexchange.com/ -UseBasicParsing -OutFile out.html

Prior to Sep 20 2014, I suggested

(wget http://blog.stackexchange.com/).Content &gt;out.html


as an answer.  However, this doesn't work in all cases, as the &gt; operator (which is an alias for Out-File) converts the input to Unicode.


If you are using Windows 7, you will need to install version 4 or newer of the Windows Management Framework.

You may find that doing a $ProgressPreference = "silentlyContinue" before Invoke-WebRequest will significantly improve download speed with large files; this variable controls whether the progress UI is rendered.

**Reference**: https://superuser.com/questions/362152/native-alternative-to-wget-in-windows-powershell

> 📎 Source: https://superuser.com/questions/362152/native-alternative-to-wget-in-windows-powershell

#### 29. Keyboard language keeps changing in Windows 10

**Issue**: Keyboard language keeps changing in Windows 10
**Tags / Source**: Tags: windows, windows-10, keyboard-layout | superuser | 👍 349 | 💬 9 answers

**Description**:
Tags: windows, windows-10, keyboard-layout | Score: 349 | Views: 543257 | Answers: 9

**Solution / Community Answer**:
In Windows 10, by default, pressing CTRL+SHIFT (or for some ALT+SHIFT - thanks madmenyo ) will cycle through any keyboard layouts that you might have mapped and it's surprisingly easy to do this by mistake.

If you keep pressing CTRL+SHIFT (or whatever you might have changed it to) then soon you should get back to the correct setting. (alternatively reboot which is what I did first time ;-) ) 

(Updated Aug 2019) You can change/disable this by

&gt; Settings &gt; search for 'typing' &gt; Advanced keyboard settings &gt; Language
&gt; Bar options &gt; Advanced Key Settings (tab) &gt; Change Key Sequence


Be warned, the above doesn't always work - Restarts and Sleep mode can both change keyboard default (usually to US) - I've found no cast-iron solution though creating a new profile can help, though not a particularly satisfactory answer IMHO.

In an emergency

WIN+R  
osk


to bring up the On Screen Keyboard might help temporarily.

Also note that it's possible to disable this so that no key combination will change the language - change the keys to "Not Assigned" - see answer below from Mort for more info

**Reference**: https://superuser.com/questions/976947/keyboard-language-keeps-changing-in-windows-10

> 📎 Source: https://superuser.com/questions/976947/keyboard-language-keeps-changing-in-windows-10

#### 30. Why does virtualbox only have 32-bit option, no 64-bit option on Windows 7?

**Issue**: Why does virtualbox only have 32-bit option, no 64-bit option on Windows 7?
**Tags / Source**: Tags: windows, windows-7, virtualbox | superuser | 👍 349 | 💬 7 answers

**Description**:
Tags: windows, windows-7, virtualbox | Score: 349 | Views: 1389529 | Answers: 7

**Solution / Community Answer**:
Take a look: http://www.fixedbyvonnie.com/2014/11/virtualbox-showing-32-bit-guest-versions-64-bit-host-os/

If VirtualBox is only showing 32-bit versions in the Version list make sure:


You have an x64 CPU installed. (Optimally, a 64-bit OS should also be installed to receive acceptable virtualization performance.)
Hardware virtualization is enabled in the BIOS. (Your CPU must support it.)


For Intel x64: VT-x (Intel Virtualization Technology) and VT-d are both enabled
For AMD x64: AMD SVM (Secure Virtual Machine) is enabled

Hyper-V (or any other form of bare-metal hypervisor) is not installed

**Reference**: https://superuser.com/questions/866962/why-does-virtualbox-only-have-32-bit-option-no-64-bit-option-on-windows-7

> 📎 Source: https://superuser.com/questions/866962/why-does-virtualbox-only-have-32-bit-option-no-64-bit-option-on-windows-7

#### 31. How to pin either a Shortcut or a Batch file to the new Windows 7, 8 and 10 Taskbar and start menu?

**Issue**: How to pin either a Shortcut or a Batch file to the new Windows 7, 8 and 10 Taskbar and start menu?
**Tags / Source**: Tags: windows-7, windows-8, windows-10, taskbar, shortcuts | superuser | 👍 344 | 💬 7 answers

**Description**:
Tags: windows-7, windows-8, windows-10, taskbar, shortcuts | Score: 344 | Views: 286084 | Answers: 7

**Solution / Community Answer**:
Create a shortcut to your batch file.
Get into shortcut property and change target to something like: cmd.exe /C "path-to-your-batch".
Simply drag your new shortcut to the taskbar. It should now be pinnable.

**Reference**: https://superuser.com/questions/100249/how-to-pin-either-a-shortcut-or-a-batch-file-to-the-new-windows-7-8-and-10-task

> 📎 Source: https://superuser.com/questions/100249/how-to-pin-either-a-shortcut-or-a-batch-file-to-the-new-windows-7-8-and-10-task

#### 32. Conclusively stop wake timers from waking Windows 10 desktop

**Issue**: Conclusively stop wake timers from waking Windows 10 desktop
**Tags / Source**: Tags: windows-10, sleep, wake-on-lan | superuser | 👍 331 | 💬 3 answers

**Description**:
Tags: windows-10, sleep, wake-on-lan | Score: 331 | Views: 181507 | Answers: 3

**Solution / Community Answer**:
Summary
April 2022: I have made a new PowerShell script that will disable Windows' scheduled tasks to wake a device automatically. Use it alongside the other parts of this guide. Download it at:
https://github.com/seagull/disable-scheduledWaking
There are a number of things that can affect this. I'm aware there are posts all over this site detailing various different ways to approach the issue; this post aims to consolidate them and add my own insight into the issue as someone affected by it themselves.
The fix outlined in Step 2 can also be used to stop Windows 10 from rebooting the machine after installing Windows Updates.
This fix works for the Fall Update (1709) as well. You will need to disable the 'Reboot' task again and re-configure the security permissions, though, because the update process replaces it.
Step 1: Disable wake timers for all power profiles
Lazy tech-bloggers would have you believe this is the end of your search. While it's true that this step will eliminate a few errant shutdowns, there are a number of settings and configurations, particularly in Windows 10, that fail to respect this setting regardless of user intervention. Go to the Control Panel → Power Options. From here, pick whatever power profile is first on the list and disable 'Wake timers'. Work through all profiles.

Thanks to StackExchange user olee22 for the image.
On Windows 10, it is strongly recommended you fix this setting for all power profiles, not just the one you have chosen to use. Various Windows faculties will use different profiles; this improves your chances of not being woken up.
Step 2: Disable the unruly reboot scheduled task
Windows 10's UpdateOrchestrator scheduled task folder contains a task called &quot;reboot&quot;. This task will wake your computer up to install updates regardless of whether or not any are available. Simply removing its permission to wake the computer is not sufficient; Windows will just edit it to give itself permission again after you leave the Task Scheduler.
From your Control Panel, enter Administrative Tools, then view your Task Scheduler.


This is the task you want - under Task Scheduler Library → Microsoft → Windows → UpdateOrchestrator. The most important things you want to do are:


From here, you will need to alter the permissions for the task so that Windows cannot molest it. The task is located in C:\Windows\System32\Tasks\Microsoft\Windows\UpdateOrchestrator. It's called Reboot without a file extension. Right-click it, enter properties and make yourself the owner. Finally, configure it so that the following is shown:

Here the file is shown with read-only permissions for SYSTEM. Make it so that no account has write access, not even your own (you can always change permissions later if you need to). Please also ensure you disable any inherited permissions for the file from the Advanced button on this screen, to override any existing permissions on the root folder. This will 100% STOP Windows from messing with your changes after you've implemented them.
Once this has been set, you won't need to worry about that scheduled task any more.
If you don't have the Permissions to alter UpdateOrchestrator Tasks

Altering the UpdateOrchestrator's tasks now requires SYSTEM permissions, neither administrator nor TrustedInstaller permissions.

One of the ways of going around this is by:

Installing Microsoft's own PsTools.
Opening Command Prompt as and administrator and cd into your local PsTools folder.
Executing:
psexec.exe -i -s %windir%\system32\mmc.exe /s taskschd.msc


Going to the UpdateOrchestrator and disabling the Reboot task(s), as previously mentioned.

Note for Windows 1709 (Fall Creators' Update)
The Windows installation process changes permissions for files, so make sure you go through this guide again after upgrading.
I have heard reports that a new task is made called AC Power Install which requires the same steps applied to it, but I have not seen this task produced on my own device after installing the 16299.192 (2018-01 Meltdown patch) update so I cannot advise with absolute certainty. The same steps as performed above should work on any task that has been introduced.
Step 3: Check Wake Timers in PowerShell
You have disabled wake timer functionality, but Windows 10 has a habit of not respecting that setting, so to be safe, we're going to run a PowerShell command to weed out all tasks that can, feasibly, wake your PC. Open an Administrative PowerShell command prompt (Start, type 'Powershell', Ctrl+Shift+Enter) and place this command in the window:
Get-ScheduledTask | where {$_.settings.waketorun}

Go through all the tasks it lists and remove their permission to wake your computer. You shouldn't need to worry about permissions like we did with Reboot; that was an outlying case.
Step 4: Check what hardware can wake your PC
Lots of USB hardware, when engaged, has the ability to wake your PC (keyboards often do when keys are pressed for example); wake-on-LAN is typically also an issue in this scenario. For the uninitiated, a common and useful feature of modern hardware is called 'Wake on LAN'. If your device is attached to a local network by way of a wired Ethernet cable (it doesn't work for Wi-Fi) you can send communications through that will wake your PC up when received. It's a feature I use often but it must be brought into line, as its default behaviour is far too overzealous.
Enter the following command into an administrative command prompt:
powercfg -devicequery wake_armed


From here, find the devices in your Device Manager (Control Panel) and, under the Power Management tab, remove their ability to wake your computer up. If you have network interface cards that you want to keep Wake-on-LAN for, enable Only wake this device if it receives a magic packet as opposed to waking up for all traffic sent its way.
Step 5: Check the Group Policy just to be completely sure
Right-click your Start menu and select Run. Type in GPEdit.MSC. Find the following setting under Computer Configuration → Administrative Templates → Windows Components → Windows Updates → Enabling Windows Update Power Management to automatically wake up the system to install scheduled updates. Double-click it and set it to Disabled.

Step 6: Disable waking your machine up for automatic maintenance
Someone at Microsoft has a sense of humour for this one. If you're woken at night by your PC, the one thing you want to hear more than anything else is the hard drive crunching and grinding as it does a nightly defragmentation. Disable this feature by finding the Security and Maintenance section of the Control Panel. From there, expand Maintenance and look for the link to Change Maintenance settings.

Set the time to something more sociable (7PM is fine) and disable the machine's ability to wake itself up for the task.

**Reference**: https://superuser.com/questions/973009/conclusively-stop-wake-timers-from-waking-windows-10-desktop

> 📎 Source: https://superuser.com/questions/973009/conclusively-stop-wake-timers-from-waking-windows-10-desktop

#### 33. Menu select item stuck on screen after context or command menu has closed

**Issue**: Menu select item stuck on screen after context or command menu has closed
**Tags / Source**: Tags: windows-7, windows, user-interface | superuser | 👍 327 | 💬 11 answers

**Description**:
Tags: windows-7, windows, user-interface | Score: 327 | Views: 324992 | Answers: 11

**Solution / Community Answer**:
The problem was introduced back in Windows 2000 when fading menu items were added. Originally, the feature was added in kernel-mode code and was tightly integrated into portions of the UI. Since it worked so well, it ended up staying there. The problem has appeared from time to time, but no one has had a reliable way to reproduce it in the kernel debugger to get it fixed.

The same effect can be achieved without changing the screen resolution or color depth.  Go to Start -> Run -> and type tskill dwm.  This command will reset the desktop window manager without the need to change the screen resolution.  

Changing the screen resolution or color depth also resets the desktop window manager, so it's always been a workaround for the bug when it appears. Either of these solutions will fix the problem.

**Reference**: https://superuser.com/questions/57016/menu-select-item-stuck-on-screen-after-context-or-command-menu-has-closed

> 📎 Source: https://superuser.com/questions/57016/menu-select-item-stuck-on-screen-after-context-or-command-menu-has-closed

#### 34. How can I visualize the file system usage on Windows?

**Issue**: How can I visualize the file system usage on Windows?
**Tags / Source**: Tags: windows, file-management, disk-space, community-faq | superuser | 👍 321 | 💬 23 answers

**Description**:
Tags: windows, file-management, disk-space, community-faq | Score: 321 | Views: 215820 | Answers: 23

**Solution / Community Answer**:
WinDirStat is a port of KDirStat for Linux. It's free, lightweight, small (650kb installer), fast, portable (as a standalone .exe file), and works on multiple versions of Windows. Besides showing folders and percentages (for the entire disk or any subset of folders), it also displays an (optional) graphical usage map. Works well with NTFS Junction folders, avoiding counting folders multiple times.

**Reference**: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

> 📎 Source: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

#### 35. Equivalent of cmd&#39;s &quot;where&quot; in powershell

**Issue**: Equivalent of cmd&#39;s &quot;where&quot; in powershell
**Tags / Source**: Tags: windows, powershell | superuser | 👍 318 | 💬 6 answers

**Description**:
Tags: windows, powershell | Score: 318 | Views: 257708 | Answers: 6

**Solution / Community Answer**:
Use the Get-Command commandlet passing it the name of the executable. It populates the Path property of the returned object (of type ApplicationInfo) with the fully resolved path to the executable. 

# ~&gt; (get-command notepad.exe).Path
C:\WINDOWS\system32\notepad.exe

**Reference**: https://superuser.com/questions/675837/equivalent-of-cmds-where-in-powershell

> 📎 Source: https://superuser.com/questions/675837/equivalent-of-cmds-where-in-powershell

#### 36. Setting and getting Windows environment variables from the command prompt?

**Issue**: Setting and getting Windows environment variables from the command prompt?
**Tags / Source**: Tags: windows, command-line, environment-variables | superuser | 👍 317 | 💬 5 answers

**Description**:
Tags: windows, command-line, environment-variables | Score: 317 | Views: 1038784 | Answers: 5

**Solution / Community Answer**:
To make the environment variable accessible globally you need to set it in the registry. As you've realised by just using:


  set NEWVAR=SOMETHING


you are just setting it in the current process space.

According to this page you can use the setx command:


  setx NEWVAR SOMETHING


setx is built into Windows 7, but for older versions may only be available if you install the Windows Resource Kit

**Reference**: https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt

> 📎 Source: https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt

#### 37. Is there a list of Windows special directories/shortcuts (like %TEMP%)?

**Issue**: Is there a list of Windows special directories/shortcuts (like %TEMP%)?
**Tags / Source**: Tags: windows, shortcuts, environment-variables, special-locations | superuser | 👍 314 | 💬 6 answers

**Description**:
Tags: windows, shortcuts, environment-variables, special-locations | Score: 314 | Views: 344813 | Answers: 6

**Solution / Community Answer**:
There are 156 run commands at mypchell.com.
Here is a more complete list including the Windows Environment Commands (e.g. %temp%, %HomeDrive%, etc)

Windows Environment Path Variables

%AllUsersProfile% - Open the All User's Profile C:\ProgramData
%AppData% - Opens AppData folder C:\Users\{username}\AppData\Roaming
%CommonProgramFiles% - C:\Program Files\Common Files
%CommonProgramFiles(x86)% - C:\Program Files (x86)\Common Files
%HomeDrive% - Opens your home drive C:\
%LocalAppData% - Opens local AppData folder C:\Users\{username}\AppData\Local
%ProgramData% - C:\ProgramData
%ProgramFiles% -  C:\Program Files or C:\Program Files (x86)
%ProgramFiles(x86)% - C:\Program Files (x86)
%Public% - C:\Users\Public
%SystemDrive% - C:
%SystemRoot% - Opens Windows folder C:\Windows
%Temp% - Opens temporary file Folder C:\Users\{Username}\AppData\Local\Temp
%UserProfile% - Opens your user's profile C:\Users\{username}
%AppData%\Microsoft\Windows\Start Menu\Programs\Startup - Opens Windows 10 Startup location for program shortcuts



Win+R

Run commands

Calc - Calculator
Cfgwiz32 - ISDN Configuration Wizard
Charmap - Character Map
Chkdisk - Repair damaged files
Cleanmgr - Cleans up hard drives
Clipbrd - Windows Clipboard viewer
Cmd - Opens a new Command Window (cmd.exe)
Control - Displays Control Panel
Dcomcnfg - DCOM user security
Debug - Assembly language programming tool
Defrag - Defragmentation tool
Drwatson - Records programs crash &amp; snapshots
Dxdiag - DirectX Diagnostic Utility
Explorer - Windows Explorer
Fontview - Graphical font viewer
Ftp - ftp.exe program
Hostname - Returns Computer's name
Ipconfig - Displays IP configuration for all network adapters
Jview - Microsoft Command-line Loader for Java classes
MMC - Microsoft Management Console
Msconfig - Configuration to edit startup files
Msinfo32 - Microsoft System Information Utility
Nbtstat - Displays stats and current connections using NetBios over TCP/IP
Netstat - Displays all active network connections
Nslookup - Returns your local DNS server
Odbcad32 - ODBC Data Source Administrator
Ping - Sends data to a specified host/IP
Regedit - registry Editor
Regsvr32 - register/de-register DLL/OCX/ActiveX
Regwiz - Registration wizard
Sfc /scannow - System File Checker
Sndrec32 - Sound Recorder
Sndvol32 - Volume control for soundcard
Sysedit - Edit system startup files (config.sys, autoexec.bat, win.ini, etc.)
Systeminfo - display various system information in text console
Taskmgr - Task manager
Telnet - Telnet program
Taskkill - kill processes using command line interface
Tskill - reduced version of Taskkill from Windows XP Home
Tracert - Traces and displays all paths required to reach an internet host
Winchat - simple chat program for Windows networks
Winipcfg - Displays IP configuration  

Microsoft Office suite

winword - Microsoft Word
excel - Microsoft Excel
powerpnt - Microsoft PowerPoint
msaccess - Microsoft Access
outlook - Microsoft Outlook
ois - Microsoft Picture Manager
winproj - Microsoft Project 

Management Consoles

certmgr.msc - Certificate Manager
ciadv.msc - Indexing Service
compmgmt.msc - Computer management
devmgmt.msc - Device Manager
dfrg.msc - Defragment
diskmgmt.msc - Disk Management
fsmgmt.msc - Folder Sharing Management
eventvwr.msc - Event Viewer
gpedit.msc - Group Policy (&lt; XP Pro)
iis.msc - Internet Information Services
lusrmgr.msc - Local Users and Groups
mscorcfg.msc - Net configurations
ntmsmgr.msc - Removable Storage
perfmon.msc - Performance Manager
secpol.msc - Local Security Policy
services.msc - System Services
wmimgmt.msc - Windows Management   

Control Panel utilities

access.cpl - Accessibility Options
hdwwiz.cpl - Add New Hardware Wizard
appwiz.cpl - Add/Remove Programs
timedate.cpl - Date and Time Properties
desk.cpl - Display Properties
inetcpl.cpl - Internet Properties
joy.cpl - Joystick Properties
main.cpl keyboard - Keyboard Properties
main.cpl - Mouse Properties
ncpa.cpl - Network Connections
ncpl.cpl - Network Properties
telephon.cpl - Phone and Modem options
powercfg.cpl - Power Management
intl.cpl - Regional settings
mmsys.cpl sounds - Sound Properties
mmsys.cpl - Sounds and Audio Device Properties
sysdm.cpl - System Properties
nusrmgr.cpl - User settings
firewall.cpl - Firewall Settings (sp2)
wscui.cpl - Security Center (sp2)
Wupdmgr - Takes you to Microsoft Windows Update   

Thanks to The New Tech for the original forum posting.

**Reference**: https://superuser.com/questions/217504/is-there-a-list-of-windows-special-directories-shortcuts-like-temp

> 📎 Source: https://superuser.com/questions/217504/is-there-a-list-of-windows-special-directories-shortcuts-like-temp

#### 38. Can I completely disable Cortana on Windows 10?

**Issue**: Can I completely disable Cortana on Windows 10?
**Tags / Source**: Tags: windows-10, cortana | superuser | 👍 314 | 💬 9 answers

**Description**:
Tags: windows-10, cortana | Score: 314 | Views: 1744192 | Answers: 9

**Solution / Community Answer**:
Update 2018: Warning about Taskbar Breakage

I just reinstalled Windows 10 Pro and followed all the prescribed steps (both removing Cortana and removing all store apps) and it still works as prescribed. 

It bears mentioning that removing Cortana will break the Default Taskbar in weird ways. It doesn't break Windows Search - so Explorer search still works in my experience.

I've, personally, always replaced the default taskbar with Classic Start (linked via Ninite installer) and have no issues in day-to-day Windows usage otherwise.

Update: Remove Cortana via "TakeOwn"

Apparently, this trick stopped working at some point. I've used @Meferdati's link at some point successfully: winaero: how to uninstall Cortona. It contains a script that does all the work for you, as well as an explanation of how it works.

Below are the steps I've been using, which are very similar to @MC10's answer, except I've always had to "TakeOwn" to get permissions and I move my files to a different folder (instead of deleting - in case I decide to revert):


add TakeOwn to the context menu or (use takeown from the command line).
Navigate to C:\Windows
Create folder SystemApps.bak
Use Takeown to gain ownership of c:\windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy
(Gain ownership of anything else you want to move)
Cut/Paste the folder(s) from SystemApps to SystemApps.bak
When the "Permissions" pop-up appears, switch to Task Manager
Kill SearchUI.exe process
Switch back and give permission to move the folder


The folder is now in SystemsApps.bak - and you can simply move it back if the need arises.

Original: Remove Cortana via Powershell RemoveAppPackage

First disable it, then uninstall the Cortana app.

Disable it in the search settings:


Click the search icon/box in the bottom left
click the gear on the left bar
Click off next to Cortana/Web Searches




Then uninstall it, as listed here:

In elevated PowerShell:

Get-AppxPackage | Select Name, PackageFullName
Remove-AppxPackage Microsoft.Windows.Cortana_1.4.8.176_neutral_neutral_cw5n1h2txyewy


This is similar to MC10's answer, except that I'm sure the OS will be more accepting of uninstalling it via the "proper channels" (powershell) instead of renaming the folder.

Windows has fixed it so now you cannot remove "...Cortana_1.6.1.52_ ...". When this is attempted it states this is part of Windows now and cannot be removed. I guess I will go back to renaming the folder.

I'm using the same uninstall to remove other "features" like BingNews, BingSports, Etc

Edit: Likewise, you can remove the "Provisioned" applications (aka: crap that gets installed per user) via this method

Get-AppxProvisionedPackage -Online | Select DisplayName, PackageName
Remove-AppxProvisionedPackage  Microsoft.ZuneMusic_2019.6.11821.0_neutral_~_8wekyb3d8bbwe


Or... to remove ALL Apps that you can, app or provisionedapp, you can do this:

Just a warning: This will uninstall the Windows Store. That's not an issue for me, but uninstalling everything isn't for the faint of heart.

Get-AppxPackage | Remove-AppxPackage
Get-AppxProvisionedPackage -Online | Remove-AppxProvisionedPackage -online


As mentioned in comments, it's probably wise not to completely remove the Windows Store. I haven't tried this yet, but this (in the comments) looks to be ballpark of what I'd use:

Get-AppxPackage -AllUsers | where-object {$_.name –notlike "*store*"} | Remove-AppxPackage
Get-appxprovisionedpackage –online | where-object {$_.packagename –notlike "*store*"} | Remove-AppxProvisionedPackage -online


Further resource: Delete Windows 10 Apps and Restore Default Windows 10 Apps

**Reference**: https://superuser.com/questions/949569/can-i-completely-disable-cortana-on-windows-10

> 📎 Source: https://superuser.com/questions/949569/can-i-completely-disable-cortana-on-windows-10

#### 39. Using cd command in Windows command line, can&#39;t navigate to D:\

**Issue**: Using cd command in Windows command line, can&#39;t navigate to D:\
**Tags / Source**: Tags: windows, command-line, path, cd | superuser | 👍 311 | 💬 9 answers

**Description**:
Tags: windows, command-line, path, cd | Score: 311 | Views: 1488450 | Answers: 9

**Solution / Community Answer**:
Going back to the days of DOS, there's a separate "current directory" for each drive.  cd D:\foldername changes D:'s current directory to the foldername specified, but does not change the fact that you're still working on the C: drive.

What you want is simple:

D:


Here you can see how the "separate current directory for each drive" thing works:

C:\Users\coneslayer&gt;e:

E:\&gt;c:

C:\Users\coneslayer&gt;cd e:\software

C:\Users\coneslayer&gt;e:

e:\Software&gt;

**Reference**: https://superuser.com/questions/135214/using-cd-command-in-windows-command-line-cant-navigate-to-d

> 📎 Source: https://superuser.com/questions/135214/using-cd-command-in-windows-command-line-cant-navigate-to-d

#### 40. How to move windows that open up offscreen?

**Issue**: How to move windows that open up offscreen?
**Tags / Source**: Tags: windows, multiple-monitors, window-manager | superuser | 👍 309 | 💬 24 answers

**Description**:
Tags: windows, multiple-monitors, window-manager | Score: 309 | Views: 728598 | Answers: 24

**Solution / Community Answer**:
I use this approach:


Use Alt+Tab to switch to the off-screen application.
Press Alt+SPACE to bring up the system menu (you won't see it because it is off screen)
Press R to select the "Restore" menu choice to ensure the windows isn't maximized (you cannot move it if it is maximized)
Press Alt+SPACE again, then M to select the "Move" menu choice.
Press one of the arrow keys to initiate the movement.
Now just use the mouse  to place the window where you want.


If you are using a non-English version of Windows, the "R" and "M" menu choices will probably be different.

**Reference**: https://superuser.com/questions/53585/how-to-move-windows-that-open-up-offscreen

> 📎 Source: https://superuser.com/questions/53585/how-to-move-windows-that-open-up-offscreen

#### 41. How to quickly move current window to another Task View / desktop in Windows 10?

**Issue**: How to quickly move current window to another Task View / desktop in Windows 10?
**Tags / Source**: Tags: windows, windows-10 | superuser | 👍 305 | 💬 17 answers

**Description**:
Tags: windows, windows-10 | Score: 305 | Views: 291045 | Answers: 17

**Solution / Community Answer**:
I think for a quicker switch this should be in the titlebar, so I created a tool for that:

https://github.com/Eun/MoveToDesktop



You can also move windows by using WIN+ALT+Left/Right or change the shortcut as needed.

**Reference**: https://superuser.com/questions/950452/how-to-quickly-move-current-window-to-another-task-view-desktop-in-windows-10

> 📎 Source: https://superuser.com/questions/950452/how-to-quickly-move-current-window-to-another-task-view-desktop-in-windows-10

#### 42. How to mess up a PC running Windows 7?

**Issue**: How to mess up a PC running Windows 7?
**Tags / Source**: Tags: windows-7, windows, security | superuser | 👍 303 | 💬 27 answers

**Description**:
Tags: windows-7, windows, security | Score: 303 | Views: 118517 | Answers: 27

**Solution / Community Answer**:
A few major problems for you, 


In bios disable the processors L2 cache - Machine crawls
Windows+break-->advanced system settings --> hardware tab --> Device Manager, right click disable mouse (make sure you can get here with just your keyboard so you can undo this!)
ctrl+alt + Arrow key - on some graphics cards this rotates the screen. (usually with no method of undoing this unless you know this shortcut)
Make a floppy boot disc/usb Key/CD Rom, pop it in the floppy drive and ensure its set to first in the boot order in bios (bonus points for removing the hdd from boot list and creating all 3 boot discs with a different os on each so they fix one then get the next!)
Use a partitioning tool to shrink the hdd partition to a few mb more than is currently in use
Do the opposite and fill up available space with multiple copies of large files.  Combined with a startup script to start the copies would keep the hard drive filled if they first attempted cleanup by deleting files.


And a few irritations to garnish the pc with


If it had internet access - Open Internet Properties --> connections Tab -->Lan Settings, Check use a proxy server, set the address to 127.0.0.1 (prevents them googling for solutions :P)
Right click on desktop - View - uncheck show desktop icons (irritating but not tough to fix)
sticky tape on the bottom of the mouse can disrupt the laser stopping the mouse working (couple this with the major disabling of the mouse in device manager to add confusion).
if the connectors are ps2, swap the mouse and keyboard, obvious if you're used to hardware but passes a quick glance from a noob
In word Office button -->Word Options --> proofing --> AutoCorrect Options --> add a few entries for common words, subtlety is your friend, is --> was the --> teh etc (2k7 instructions but can be done via different route in most versions)


Reverse the steps to undo the problems and ask in comments if you have trouble!

Edit - as we may have had our beastly BIOS tricks taken from us here's a couple more windows based ones

Put the shutdown command into autoexec.bat Command syntax here (you've talked about putting similar functionality in the startup folder, so this should confuse em by doing the same thing from a different spot)

Fork bomb! Create a .bat file containing the following text and make it autorun (either call from autoexec.bat or drop the .bat in startup folder)

:s
start %0
goto s


This will spawn huge numbers of processes untill the machine grinds to a halt (The code is untested but looks viable)

**Reference**: https://superuser.com/questions/275894/how-to-mess-up-a-pc-running-windows-7

> 📎 Source: https://superuser.com/questions/275894/how-to-mess-up-a-pc-running-windows-7

#### 43. How to automatically reload modified files in Notepad++

**Issue**: How to automatically reload modified files in Notepad++
**Tags / Source**: Tags: windows, notepad++, text-editors | superuser | 👍 295 | 💬 6 answers

**Description**:
Tags: windows, notepad++, text-editors | Score: 295 | Views: 247823 | Answers: 6

**Solution / Community Answer**:
You can disable the confirmation in the settings:

Settings -&gt; Preferences -&gt; MISC. -&gt; Update silently

**Reference**: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

> 📎 Source: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

#### 44. Equivalent of Linux `touch` to create an empty file with PowerShell

**Issue**: Equivalent of Linux `touch` to create an empty file with PowerShell
**Tags / Source**: Tags: windows, windows-8, powershell, powershell-3.0 | superuser | 👍 293 | 💬 14 answers

**Description**:
Tags: windows, windows-8, powershell, powershell-3.0 | Score: 293 | Views: 420048 | Answers: 14

**Solution / Community Answer**:
Using the append redirector ">>" resolves the issue where an existing file is deleted:

echo $null &gt;&gt; filename

**Reference**: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

> 📎 Source: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

#### 45. How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?

**Issue**: How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?
**Tags / Source**: Tags: windows, windows-10, windows-explorer, windows-10-preview | superuser | 👍 291 | 💬 5 answers

**Description**:
Tags: windows, windows-10, windows-explorer, windows-10-preview | Score: 291 | Views: 256078 | Answers: 5

**Solution / Community Answer**:
As of build 9926 (at least - it may have been an earlier build), this is configurable via the GUI.

Open Explorer and go to View, then click Options (or Change folder and search options). In General tab you can change Open File Explorer to This PC

**Reference**: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

> 📎 Source: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

#### 46. How can I reduce the consumption of the `vmmem` process?

**Issue**: How can I reduce the consumption of the `vmmem` process?
**Tags / Source**: Tags: windows-10, memory, docker, resources | superuser | 👍 273 | 💬 15 answers

**Description**:
Tags: windows-10, memory, docker, resources | Score: 273 | Views: 569297 | Answers: 15

**Solution / Community Answer**:
Daniiel B is on the money. To turn off Vmmem simply go into Powershell or whatever terminal you like to use under admin rights and enter the command wsl --shutdown, when your done with playing in wsl1/2.

**Reference**: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

> 📎 Source: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

#### 47. How can I execute a Windows command line in background?

**Issue**: How can I execute a Windows command line in background?
**Tags / Source**: Tags: windows, command-line | superuser | 👍 270 | 💬 12 answers

**Description**:
Tags: windows, command-line | Score: 270 | Views: 889339 | Answers: 12

**Solution / Community Answer**:
This is a little late but I just ran across this question while searching for the answer myself and I found this:

START /B program


which, on Windows, is the closest to the Linux command:

program &amp;


From the console HELP system:

C:\&gt;HELP START

Starts a separate window to run a specified program or command.

START ["title"] [/D path] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
      [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
      [/NODE &lt;NUMA node&gt;] [/AFFINITY &lt;hex affinity mask&gt;] [/WAIT] [/B]
      [command/program] [parameters]

    "title"     Title to display in window title bar.
    path        Starting directory.
    B           Start application without creating a new window. The
                application has ^C handling ignored. Unless the application
                enables ^C processing, ^Break is the only way to interrupt
                the application.


One problem I saw with it is that  you have more than one program writing to the console window, it gets a little confusing and jumbled.

To make it not interact with the user, you can redirect the output to a file:

START /B program &gt; somefile.txt

**Reference**: https://superuser.com/questions/198525/how-can-i-execute-a-windows-command-line-in-background

> 📎 Source: https://superuser.com/questions/198525/how-can-i-execute-a-windows-command-line-in-background

#### 48. How do I change the language of all Powerpoint slides at once?

**Issue**: How do I change the language of all Powerpoint slides at once?
**Tags / Source**: Tags: windows, microsoft-office, microsoft-powerpoint, language, microsoft-powerpoint-2010 | superuser | 👍 268 | 💬 9 answers

**Description**:
Tags: windows, microsoft-office, microsoft-powerpoint, language, microsoft-powerpoint-2010 | Score: 268 | Views: 572691 | Answers: 9

**Solution / Community Answer**:
To change the language of the entire PowerPoint easily, open the View tab and select the Outline view.

Now press


Ctrl+A to select all.
Tools → Language → Choose your language to set.


Likewise while you have everything selected you can change other things like fonts, colours etc. Although of course in many case this is better done by changing the slide master, a presentation that has had many editors may have lots of 'hard' formatting set which deviates from the underlying master and needs resetting to be consistent. You can also reset individual slides to the master style, but this may result in placeholders moving as well, which may be undesirable in some situations.

PowerPoint 2013


View → Outline → select all slides (in a left menu) via Ctrl+A.
Review → Language → Set Proofing Language... → Choose your language to set.


As for me - PowerPoint restart was needed. 
Probably because I also did changed Editing Language:


Review → Language → Set Proofing Language... → Language Preferences → Choose Editing Languages.

**Reference**: https://superuser.com/questions/432366/how-do-i-change-the-language-of-all-powerpoint-slides-at-once

> 📎 Source: https://superuser.com/questions/432366/how-do-i-change-the-language-of-all-powerpoint-slides-at-once

#### 49. How can I check the temperature of my CPU in Windows?

**Issue**: How can I check the temperature of my CPU in Windows?
**Tags / Source**: Tags: windows, cpu, temperature | superuser | 👍 267 | 💬 10 answers

**Description**:
Tags: windows, cpu, temperature | Score: 267 | Views: 2706360 | Answers: 10

**Solution / Community Answer**:
Actually this information is given to OS by the BIOS, but you will need an application to expose the information. You can find a lot of applications to do this:

Realtemp
CPU thermomether
Core Temp

**Reference**: https://superuser.com/questions/395434/how-can-i-check-the-temperature-of-my-cpu-in-windows

> 📎 Source: https://superuser.com/questions/395434/how-can-i-check-the-temperature-of-my-cpu-in-windows

#### 50. How to list Chocolatey packages already installed and newer version available from the command line

**Issue**: How to list Chocolatey packages already installed and newer version available from the command line
**Tags / Source**: Tags: windows, command-line, chocolatey | superuser | 👍 267 | 💬 4 answers

**Description**:
Tags: windows, command-line, chocolatey | Score: 267 | Views: 312130 | Answers: 4

**Solution / Community Answer**:
Note: You likely need to do the following commands in an administrative cmd/powershell prompt.

If you have choco 0.9.9.6+, you can use the outdated command.

choco outdated


If you have 0.9.9+ installed:

choco upgrade all --noop


If you have version 0.9.8.33 or below installed:

choco version all


Following that, if you actually want to upgrade - you can follow with:

cup all -y


Note: -y will only work with 0.9.8.33+.

**Reference**: https://superuser.com/questions/890251/how-to-list-chocolatey-packages-already-installed-and-newer-version-available-fr

> 📎 Source: https://superuser.com/questions/890251/how-to-list-chocolatey-packages-already-installed-and-newer-version-available-fr

#### 51. Why is Google so much faster than a hard-drive search?

**Issue**: Why is Google so much faster than a hard-drive search?
**Tags / Source**: Tags: windows, hard-drive, windows-search, google-search | superuser | 👍 265 | 💬 10 answers

**Description**:
Tags: windows, hard-drive, windows-search, google-search | Score: 265 | Views: 43966 | Answers: 10

**Solution / Community Answer**:
Google is not searching the internet: it is searching an index. Google has huge server farms which are constantly scanning and indexing the internet. This process takes a lot of time, just like the search of your unindexed hard drive. In Windows 7, there is an option to index your hard drives. This process takes some time at first but once it is up and running the results of a search will be instantaneous.

If you want to know more about how the Google search works you can read Google's article "How Search Works" or read the article "How Stuff Works: How Google Works".

**Reference**: https://superuser.com/questions/577502/why-is-google-so-much-faster-than-a-hard-drive-search

> 📎 Source: https://superuser.com/questions/577502/why-is-google-so-much-faster-than-a-hard-drive-search

#### 52. Windows equivalent of whereis?

**Issue**: Windows equivalent of whereis?
**Tags / Source**: Tags: windows, command-line | superuser | 👍 259 | 💬 11 answers

**Description**:
Tags: windows, command-line | Score: 259 | Views: 243680 | Answers: 11

**Solution / Community Answer**:
The where command does what you want and goes back at least to the resource kit for Windows 98, and is included by default in Server 2003, Vista, and newer:

C:\&gt;where csc
C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe
C:\Windows\Microsoft.NET\Framework\v2.0.50727\csc.exe


If executed with no arguments (on Vista), it results in one of my favorite messages:

C:\&gt;where
ERROR: The operation completed successfully.


If executing in PowerShell, be sure to include '.exe' to distinguish from any 'where' aliases or scripts along the path. ('where' is a typical alias for Where-Object.ps1)

C:\&gt; where.exe where.exe
C:\Windows\System32\where.exe

**Reference**: https://superuser.com/questions/21067/windows-equivalent-of-whereis

> 📎 Source: https://superuser.com/questions/21067/windows-equivalent-of-whereis

#### 53. Windows equivalent of the Linux command &#39;touch&#39;?

**Issue**: Windows equivalent of the Linux command &#39;touch&#39;?
**Tags / Source**: Tags: windows, file-attributes, touch | superuser | 👍 257 | 💬 32 answers

**Description**:
Tags: windows, file-attributes, touch | Score: 257 | Views: 532320 | Answers: 32

**Solution / Community Answer**:
If you want to touch the date stamp of a file using windows, use the following command at the command prompt:
copy /b filename.ext +,,

(where filename.ext is your file's name). The +,, is a special flag to copy telling it to simply update the date/time on the file:

* Changing the time and date of a file
If you want to assign the current time and date to a file without modifying the file, use the following syntax:
copy /b Source+,,
The commas indicate the omission of the Destination parameter.

Edit based on comments by Lumi and Justin: put this in a batch file, eg. touch.cmd
@COPY /B %1+,, %1

This works even if the file is not in the current directory (tested on Windows 7).

**Reference**: https://superuser.com/questions/10426/windows-equivalent-of-the-linux-command-touch

> 📎 Source: https://superuser.com/questions/10426/windows-equivalent-of-the-linux-command-touch

#### 54. How to search inside files on Windows 7?

**Issue**: How to search inside files on Windows 7?
**Tags / Source**: Tags: windows-7, windows, windows-search, file-filter | superuser | 👍 255 | 💬 13 answers

**Description**:
Tags: windows-7, windows, windows-search, file-filter | Score: 255 | Views: 833086 | Answers: 13

**Solution / Community Answer**:
To get to the Indexing Options:  

Start --> Control Panel --> Indexing Options 

See Change advanced indexing options for more information.

If you click on the Advanced button in Indexing Options and go to the File Types tab, you will get a list of file types and the way they are indexed. For the file types you want, you can specify that you want the file contents indexed, and not just the file properties.

Or you can just do a normal search, and after the search is finished you can click on the "File Contents" button under the "Search again in" field (which is located after the end of the search results list, if you scroll to the bottom).

Based on this page, the "File Contents" option won't always show up - only when the folder being searched is not marked for file content indexing; in that case, file contents are supposedly searched automatically, without having to specify this option explicitly.

**Reference**: https://superuser.com/questions/60173/how-to-search-inside-files-on-windows-7

> 📎 Source: https://superuser.com/questions/60173/how-to-search-inside-files-on-windows-7

#### 55. Refresh Icon Cache Without Rebooting

**Issue**: Refresh Icon Cache Without Rebooting
**Tags / Source**: Tags: windows, windows-explorer, icons, cache | superuser | 👍 251 | 💬 13 answers

**Description**:
Tags: windows, windows-explorer, icons, cache | Score: 251 | Views: 408444 | Answers: 13

**Solution / Community Answer**:
Yes.

You can just run the following command to clear the icon cache:

ie4uinit.exe -ClearIconCache


For Windows 10, use:

ie4uinit.exe -show




Check this video for a demo.

[tip credit]

**Reference**: https://superuser.com/questions/499078/refresh-icon-cache-without-rebooting

> 📎 Source: https://superuser.com/questions/499078/refresh-icon-cache-without-rebooting

#### 56. Kill a process which says &quot;Access denied&quot;

**Issue**: Kill a process which says &quot;Access denied&quot;
**Tags / Source**: Tags: windows-7, windows, 64-bit | superuser | 👍 251 | 💬 11 answers

**Description**:
Tags: windows-7, windows, 64-bit | Score: 251 | Views: 1111843 | Answers: 11

**Solution / Community Answer**:
Kill a protected process?

http://processhacker.sourceforge.net/index.php

Works on Windows Server without admin rights! Yammie! :)

**Reference**: https://superuser.com/questions/109010/kill-a-process-which-says-access-denied

> 📎 Source: https://superuser.com/questions/109010/kill-a-process-which-says-access-denied

#### 57. Troubleshoot High CPU usage by the &quot;System&quot; process

**Issue**: Troubleshoot High CPU usage by the &quot;System&quot; process
**Tags / Source**: Tags: windows, windows-8, performance, troubleshooting, cpu-usage | superuser | 👍 243 | 💬 6 answers

**Description**:
Tags: windows, windows-8, performance, troubleshooting, cpu-usage | Score: 243 | Views: 753727 | Answers: 6

**Solution / Community Answer**:
Introduction
High CPU usage by the &quot;System&quot; process can often be caused by a hardware driver issue (bug, old version, incompatility etc).
The System process loads (or hosts) multiple hardware drivers from different vendors that require higher level of memory access.   This is why diagnosing the specific culprit can require a bit of detective work as described below.
Diagnosing the issue
To diagnose the CPU usage issues, you should use Event Tracing for Windows (ETW) to capture CPU Sampling data / Profile.
To capture the data, install the Windows Performance Toolkit, which is part of the Windows SDK.
The Windows 10 WPT can be used on Windows 8/Server 2012, Windows 8.1/Server 2012R2 and Windows 10/Server 2016. If you still use Windows 7, use the SDK/WPT with Build 15086.

(all other entries can be unselected)
Now run WPRUI.exe, select First Level, under  Resource select CPU usage and click on start.

Now capture 1 minute of the CPU usage. After 1 minute, click on Save.
Now analyze the generated ETL file with the Windows Performance Analyzer by dragging and dropping the CPU Usage (sampled) graph to the analysis pane and ordering the columns like you see in the picture:

Inside WPA, load the debug symbols and expand Stack of the SYSTEM process. In this demo, the CPU usage comes from the nVIDIA driver.

In the following demo, the CPU usage comes from the Realtek NIC driver:


When you see calls like ntoskrnl.exe!ViKeTrimWorkerThreadRoutine, ntoskrnl.exe!MmVerifierTrimMemory, ntoskrnl.exe!VerifierKeLeaveCriticalRegion, this means you have Driver Verifier enabled. This also hurts performance a lot and causes high SYSTEM usage. Disable Driver Verifier and reboot.


In this demo, the driver iai2ce.sys (Intel Serial IO GPIO Controller driver) causes it:


In this example, the CPU usage comes from the file rtsuvc.sys which seems to be the Realtek UVC webcam Driver


This demo shows that Bitdefender driver ignis.sys


In the following example, the CPU usage is casued by the broadcom network driver bcmwl664.sys


When you see ntoskrnl.exe!MiZeroWorkerPages as cause, it is trickier. This means the function of the kernel which zeros the memory before it can be used again causes the high CPU usage:

There is no real way to detect which process causes it, but I know that Chrome can cause it if you have hardware acceleration enabled in Chrome. So if you see this and use Chrome, turn hardware acceleration in Chrome off.

When you see those ntoskrnl.exe!RtlpGenericRandomPatternWorker, ntoskrnl.exe!RtlpTestMemoryRandomUp calls

the CPU usage comes from the Kernel to test memory for issues (memtest). This usage is triggered via the idle maintenance task of Windows 8.1/10. You can use Task Scheduler to disable the idle task.

In Windows 10, the task is called RunFullMemoryDiagnostics under Microsoft &gt; Windows &gt; MemoryDiagnostic &gt; RunFullMemoryDiagnostic.


In this case, the CPU usage seems to come from the Data Deduplication Feature (dedup.sys!DdpPostCreate) of Windows Server:


In this demo, the CPU usage is caused by the WIFI card driver athrx.sys

Search for a driver update if you see this.

In the following demo, a citrix driver is involved:

So contact your IT for how to solve Citrix issues.

In this demo, the function usbhub.sys!UsbhPortRecycle causes the CPU usage:

Changing USB2.0 ports to 1.1 speed or connecting USB drives to other USB 2.0 ports helped for some users.

In this case, a small amount of SYSTEM usage comes from the Acronis driver tdrpm251.sys:


In this demo, the CPU usage ntoskrnl.exe!KeAcquireSpinLockRaiseToDpc and ntoskrnl.exe!KeReleaseSpinLock.

so a driver is using SpinLocks very heavily. Disable some devices/drivers until you see one which causes it.

In this case, the CPU usage is caused by the driver L1C62x64.sys

This is the qualcomm atheros AR8171/8175 PCI-E gigabit Ethernet driver. So update the driver if you see it in the stack.

Here, the CPU usage comes from scanning the host file (netbt.sys!DelayedScanLmHostFile)

make sure your hosts file is not too large to avoid this usage.

In this case, the CPU usage comes from SRTSP64.SYS from symantec.

Update your used symantec product to the latest version.

Here, the CPU usage comes from the AMD GPU driver (atikmdag.sys)

if you see this, go to AMD site and get the latest driver for your AMD card.

Here, the drivers TMXPFlt.sys and  VsapiNt.sys cause the high CPU usage.

From what I see, those files are part of Trend Micro AV suite. Update the tool or remove it.

In this example, the CPU usage comes from the function ntoskrnl.exe!MmGetPageFileInformation

This function gets information about the pagefile.

Routine Description:
This routine returns information about the currently active paging
files.

Disable the pagefile, reboot and enable it again and see if this fixes it. Also, removing Intel services (e.g Intel Content Protection HECI Service) seems to fixed it for a user.

Here, you can see that the driver Netwtw04.sys (Intel Wifi driver) calls the function flushCompleteAllPendingFlushRequests and this causes a high CPU usage.

Because the debug symbols get loaded the Windows inbox driver is used. Only here we can get debug symbols to see the callstack with the function name flushCompleteAllPendingFlushRequests.
Here, you should install the latest driver from Intel to fix it.

The most complicated case of SYSTEM usage is ACPI.sys usage in the callstack:
Line #, DPC/ISR, Module, Stack, Count, Process, Weight (in view) (ms), TimeStamp (s), % Weight
6, , ,   |    |- ACPI.sys!ACPIWorkerThread, 40246, , 39.992,941063, , 4,13
7, , ,   |    |    ACPI.sys!RestartCtxtPassive, 40246, , 39.992,941063, , 4,13
8, , ,   |    |    ACPI.sys!InsertReadyQueue, 40246, , 39.992,941063, , 4,13
9, , ,   |    |    ACPI.sys!RunContext, 40246, , 39.992,941063, , 4,13
10, , ,   |    |    ntoskrnl.exe!KeReleaseSpinLock, 40246, , 39.992,941063, , 4,13
11, , ,   |    |    ntoskrnl.exe!KiDpcInterrupt, 40246, , 39.992,941063, , 4,13
12, , ,   |    |    ntoskrnl.exe!KiDispatchInterruptContinue, 40246, , 39.992,941063, , 4,13
13, , ,   |    |    ntoskrnl.exe!KxRetireDpcList, 40246, , 39.992,941063, , 4,13
14, , ,   |    |    ntoskrnl.exe!KiRetireDpcList, 40246, , 39.992,941063, , 4,13
15, , ,   |    |    |- ntoskrnl.exe!KiExecuteAllDpcs, 40198, , 39.945,173325, , 4,13
16, , ,   |    |    |    |- ACPI.sys!ACPIInterruptDispatchEventDpc, 27565, , 27.408,930428, , 2,83
17, , ,   |    |    |    |    |- ACPI.sys!ACPIGpeEnableDisableEvents, 24525, , 24.384,921620, , 2,52
18, , ,   |    |    |    |    |    ACPI.sys!ACPIWriteGpeEnableRegister, 24525, , 24.384,921620, , 2,52
19, , ,   |    |    |    |    |    |- hal.dll!HalpAcpiPmRegisterWrite, 24421, , 24.281,015516, , 2,51
20, , ,   |    |    |    |    |    |    |- hal.dll!HalpAcpiPmRegisterWritePort, 24166, , 24.027,316013, , 2,48

this is extremely difficult to debug. In a sysinternals topic, I listed some advice:

make sure the CPU doesn't overheat because of dust in the CPU fan
update or re-flash the (same) BIOS/UEFI
load default BIOS/UEFI settings
make sure the battery is not damaged, remove the battery from the notebook or disable the battery in device manager.
change jumper on HDD caddy if you have replaced the DVD/Blue-Ray Drive with a Caddy to install an SSD next to your old HDD



disable some devices as advised by this user
if you use an Intel chipset, try to install Intel Rapid storage Technology (RST) to replace the standard AHCI driver from Windows. This also seems to helped.
the user Shayna figured out, that using Process Hacker (started as admin) to suspend the threads of the ACPI.sys issues &quot;fixes&quot; the issue for him. So try his workaround if all other steps don't fix it for you.


In the following demo, the Intel HD driver igdkmd64.sys in version .4574 for the Intel HD 630 causes the issue:

The solution is to update to driver with version of at least .4590.

In the following case, the CPU usage of the SYSTEM process is caused by the driver stdriverx64.sys

This seems to be an audio streaming driver. So update this software/driver if you see this in WPA.

If you see a driver called risdxc64.sys in callstack of SYSTEM that causes the high CPU usage, update the Ricoh PCIe SDXC/MMC Host Controller driver or disable the SD card reader in device manager if no driver update fixes it.

This SD card reader seems to be built-in to many Lenovo devices.

The user @stevemidgley showed a new issue of higher CPU usage with Wdf01000.sys!FxSystemWorkItem::_WorkItemThunk

Here you can see a driver UDE.sys causing it.
In symbol hub

I can see it belongs to Modem driver and PNP data of the trace shows Fibocom L850-GL (LTE Modem) as possible device:

And the solution is to disable the modem and USB composite device in device manager.

The user @fajar provided the following case:

Here the cpu usage is small, but if you change the view to DPC/ISR usage

you can see that the avgNetHub.sys driver causes a lof of DPC usage

The name indicates that this driver is part of AVG anti virus software. So update the software or remove it if you see this in your trace.

**Reference**: https://superuser.com/questions/527401/troubleshoot-high-cpu-usage-by-the-system-process

> 📎 Source: https://superuser.com/questions/527401/troubleshoot-high-cpu-usage-by-the-system-process

#### 58. How do I set system environment variables in Windows 10?

**Issue**: How do I set system environment variables in Windows 10?
**Tags / Source**: Tags: windows, windows-10 | superuser | 👍 239 | 💬 9 answers

**Description**:
Tags: windows, windows-10 | Score: 239 | Views: 1539780 | Answers: 9

**Solution / Community Answer**:
Note: After seeing lots of comments about setting environment variables without administrator rights in Windows 10, I think I have found a way. I was not administrator and could use PowerShell.
PowerShell method
You can list all environment variables with: Get-ChildItem Env:.
To get the value of a specific variable: $Env:PATH, where PATH is the name of the variable.
To set a variable: [Environment]::SetEnvironmentVariable(&quot;PATH&quot;, &quot;C:\TestPath&quot;, &quot;User&quot;), the first parameter is the name of the variable, the second is the value, the third is the level of.
There are different ways to work with environment variables and certain quirks with them in PowerShell so consult the link for details.
Old method (no longer available in newer Windows 10 updates, use PowerShell or see other answers)
Go into Settings and click on System.

Then on the left side click About and select System info at the bottom.

In the new Control Panel window that opens, click Advanced system settings on the left.

Now in the new window that comes up, select Environment Variables... at the bottom.

**Reference**: https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10

> 📎 Source: https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10

#### 59. How to supress &quot;Terminate batch job (Y/N)&quot; confirmation?

**Issue**: How to supress &quot;Terminate batch job (Y/N)&quot; confirmation?
**Tags / Source**: Tags: windows, command-line, batch | superuser | 👍 236 | 💬 21 answers

**Description**:
Tags: windows, command-line, batch | Score: 236 | Views: 199305 | Answers: 21

**Solution / Community Answer**:
At this site, I found an effective solution:

script2.cmd &lt; nul


To not have to type this out every time I made a second script called script.cmd in the same folder with the line above.  I've tested this technique on XP only, but others have confirmed it on Win 7.

Nathan adds:  another option is to put the following code at the top of script.cmd which does the same thing in one file:

rem Bypass "Terminate Batch Job" prompt.
if "%~1"=="-FIXED_CTRL_C" (
   REM Remove the -FIXED_CTRL_C parameter
   SHIFT
) ELSE (
   REM Run the batch with &lt;NUL and -FIXED_CTRL_C
   CALL &lt;NUL %0 -FIXED_CTRL_C %*
   GOTO :EOF
)

**Reference**: https://superuser.com/questions/35698/how-to-supress-terminate-batch-job-y-n-confirmation

> 📎 Source: https://superuser.com/questions/35698/how-to-supress-terminate-batch-job-y-n-confirmation

#### 60. How to compare the differences between two PDF files on Windows?

**Issue**: How to compare the differences between two PDF files on Windows?
**Tags / Source**: Tags: windows, pdf, file-comparison | superuser | 👍 234 | 💬 19 answers

**Description**:
Tags: windows, pdf, file-comparison | Score: 234 | Views: 484912 | Answers: 19

**Solution / Community Answer**:
On Linux and Windows you can use diffpdf (which differs from diff-pdf mentioned in this thread).

On Ubuntu install using:
sudo apt-get install diffpdf

See further this UbuntuGeek page on comparing pds textually or visually.
For Windows, this Diffpdf Windows version works really great. You can download from http://soft.rubypdf.com/software/diffpdf (scroll down to Win32 static version).
You can also install it on Windows in an automated manner via the https://scoop.sh/ package manager - install the package manager first per instructions on the homepage and then:
scoop bucket add extras
scoop install extras/diffpdf

This does not require administrator privileges on your account, so it can be installed on externally managed systems (e.g. work computers).

**Reference**: https://superuser.com/questions/46123/how-to-compare-the-differences-between-two-pdf-files-on-windows

> 📎 Source: https://superuser.com/questions/46123/how-to-compare-the-differences-between-two-pdf-files-on-windows

#### 61. How to make SUBST mapping persistent across reboots?

**Issue**: How to make SUBST mapping persistent across reboots?
**Tags / Source**: Tags: windows, subst | superuser | 👍 232 | 💬 11 answers

**Description**:
Tags: windows, subst | Score: 232 | Views: 287015 | Answers: 11

**Solution / Community Answer**:
Well Wikipedia mentions:

C:\&gt;SUBST /?
Associates a path with a drive letter.

SUBST [drive1: [drive2:]path]
SUBST drive1: /D

  drive1:        Specifies a virtual drive to which you want to assign a path.
  [drive2:]path  Specifies a physical drive and path you want to assign to
                 a virtual drive.
  /D             Deletes a substituted (virtual) drive.

Type SUBST with no parameters to display a list of current virtual drives.


So you can associate paths with drive letters using subst. The Persistent SUBST command (psubst) software seems to be darn handy, and they provide a solution to run it from startup:
https://github.com/ildar-shaimordanov/psubst#Inconstancy

Inconstancy
However restart of a system destroys a virtual disk. What to do? A
disk can be created after startup. But what to do, when a disk is
needed on early steps of a startup? For example, to run services?
There is system feature to start a virtual disk from the system
registry:
REGEDIT4 

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\DOS Devices] 
&quot;Z:&quot;=&quot;\\??\\C:\\Documents and Settings\\All Users\\Shared Documents&quot;

It is enough to create a text file with the extension .REG and run
it. When the next starting up of a system, the virtual disk will be
exist at logon. It needs to define a name of disk and path. Note that
each backslash in the path is doubled.

In Windows, you can run the registry editor as follows:

Start » Run... (or hit Win+R)
Type: regedit
In Windows Vista and above, UAC will pop up, click &quot;Yes&quot;.

**Reference**: https://superuser.com/questions/29072/how-to-make-subst-mapping-persistent-across-reboots

> 📎 Source: https://superuser.com/questions/29072/how-to-make-subst-mapping-persistent-across-reboots

#### 62. PowerShell equivalent to the Unix `which` command?

**Issue**: PowerShell equivalent to the Unix `which` command?
**Tags / Source**: Tags: windows, unix, powershell, which | superuser | 👍 231 | 💬 11 answers

**Description**:
Tags: windows, unix, powershell, which | Score: 231 | Views: 192989 | Answers: 11

**Solution / Community Answer**:
This was asked and answered on Stack Overflow: Equivalent of *Nix 'which' command in PowerShell?


  The very first alias I made once I started customizing my profile in PowerShell was 'which'.
  
  New-Alias which get-command
  
  To add this to your profile, type this:
  
  "`nNew-Alias which get-command" | add-content $profile
  
  The `n at the start of the last line is to ensure it will start as a new line.

**Reference**: https://superuser.com/questions/34492/powershell-equivalent-to-the-unix-which-command

> 📎 Source: https://superuser.com/questions/34492/powershell-equivalent-to-the-unix-which-command

#### 63. Browse an UNC path using Windows CMD without mapping it to a network drive

**Issue**: Browse an UNC path using Windows CMD without mapping it to a network drive
**Tags / Source**: Tags: windows, command-line, network-drive, unc | superuser | 👍 230 | 💬 8 answers

**Description**:
Tags: windows, command-line, network-drive, unc | Score: 230 | Views: 521023 | Answers: 8

**Solution / Community Answer**:
If you use pushd and popd instead of cd you won't get that UNC error.
pushd &lt;UNC path&gt; will create a temporary virtual drive and get into it.
popd will delete the temporary drive and get you back to the path you were when you entered pushd.
Example:
C:\a\local\path&gt; pushd \\network_host\a\network\path

U:\a\network\path&gt; REM a temporary U: virtual drive has been created

U:\a\network\path&gt; popd

C:\a\local\path&gt; REM the U: drive has been deleted

C:\a\local\path&gt;

**Reference**: https://superuser.com/questions/282963/browse-an-unc-path-using-windows-cmd-without-mapping-it-to-a-network-drive

> 📎 Source: https://superuser.com/questions/282963/browse-an-unc-path-using-windows-cmd-without-mapping-it-to-a-network-drive

#### 64. How do I know what proxy server I&#39;m using?

**Issue**: How do I know what proxy server I&#39;m using?
**Tags / Source**: Tags: windows, windows-xp, networking, proxy | superuser | 👍 229 | 💬 15 answers

**Description**:
Tags: windows, windows-xp, networking, proxy | Score: 229 | Views: 1026134 | Answers: 15

**Solution / Community Answer**:
The auto proxy detection system works by downloading a file called wpad.dat from the host wpad.  First confirm this host exists from a command prompt:

ping wpad


If it doesn't exist, you may have to put the correct DNS suffix.  In the same command prompt, type

ipconfig /all


You should see a Primary DNS Suffix and a DNS Suffix Search List

Try appending each of these with a . to wpad:

ping wpad.&lt;primary dns suffix&gt;


If any of these work, then in your browser enter http://wpad.&lt;suffix&gt;/wpad.dat.  This will download the proxy auto configuration file you can open in notepad.exe

Toward the bottom of this file, you should see a line saying 

PROXY &lt;host:port&gt;;


It might be repeated if you have multiple proxies available.  The host and port are what you need.

If this file doesn't exist, then either there is no proxy server, or the proxy server is being provided by dhcp (note that this would only work with IE, so if firefox can surf, this is not the method being used).  If you don't have access to the dhcp server to see what it is sending, the easiest way would be to open a site in ie, then go to a command prompt.  Type

netstat -ban


This will provide a list of connections made with the process id of each process.  Go to Task Manager, and select View/Select Columns and enable PID (Process Identifier).  Look for the PID of iexplore.exe in the list returned by netstat -ban  This will reveal the proxy ip and port.

**Reference**: https://superuser.com/questions/346372/how-do-i-know-what-proxy-server-im-using

> 📎 Source: https://superuser.com/questions/346372/how-do-i-know-what-proxy-server-im-using

#### 65. PowerShell equivalent of curl

**Issue**: PowerShell equivalent of curl
**Tags / Source**: Tags: windows, powershell, curl | superuser | 👍 229 | 💬 9 answers

**Description**:
Tags: windows, powershell, curl | Score: 229 | Views: 723773 | Answers: 9

**Solution / Community Answer**:
PowerShell 3.0 has the new command Invoke-RestMethod:

http://technet.microsoft.com/en-us/library/hh849971.aspx

more detail:  

https://discoposse.com/2012/06/30/powershell-invoke-restmethod-putting-the-curl-in-your-shell/

**Reference**: https://superuser.com/questions/344927/powershell-equivalent-of-curl

> 📎 Source: https://superuser.com/questions/344927/powershell-equivalent-of-curl

#### 66. Typing “python” on Windows 10 (version 1903) command prompt opens Microsoft store

**Issue**: Typing “python” on Windows 10 (version 1903) command prompt opens Microsoft store
**Tags / Source**: Tags: windows-10, command-line, python, cmd.exe, unattended | superuser | 👍 229 | 💬 8 answers

**Description**:
Tags: windows-10, command-line, python, cmd.exe, unattended | Score: 229 | Views: 175078 | Answers: 8

**Solution / Community Answer**:
Fixed it by removing it automatically on the settings page.  Under Apps and Features, there are an application execution aliases.

I am running the latest 1903 update.

**Reference**: https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor

> 📎 Source: https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor

#### 67. Windows 10 - disable reopening programs after restart/startup

**Issue**: Windows 10 - disable reopening programs after restart/startup
**Tags / Source**: Tags: windows, windows-10, boot | superuser | 👍 228 | 💬 7 answers

**Description**:
Tags: windows, windows-10, boot | Score: 228 | Views: 347803 | Answers: 7

**Solution / Community Answer**:
Good news! It has been somewhat &quot;fixed.&quot;
I was interested in clickbangdead's solution, but unfortunately I could not make it work no matter what I tried. Then I went back to the Microsoft Answers thread where he originally posted his solution, because maybe someone could have found a new solution in the subsequent pages. And voilà, indeed. Navigate to the following location:
Settings &gt; Accounts &gt; Sign-In Options
Scroll down to Privacy on the right and then set the following to Off:

Use my sign-in info to automatically finish setting up my device after an update or restart.


I was skeptical, because that doesn't seem like it has much to do with reopening my Google Chrome upon restart, but I tested and it (finally) works!

Update:  with the release of Windows 10 version 1803 (the April 2018 Update), Microsoft modified the wording within that Privacy option to emphasize that it will &quot;reopen my apps&quot; if it is configured to be On.

Use my sign-in info to automatically finish setting up my device and reopen my apps after an update or restart.

**Reference**: https://superuser.com/questions/1229963/windows-10-disable-reopening-programs-after-restart-startup

> 📎 Source: https://superuser.com/questions/1229963/windows-10-disable-reopening-programs-after-restart-startup

#### 68. Change default code page of Windows console to UTF-8

**Issue**: Change default code page of Windows console to UTF-8
**Tags / Source**: Tags: windows-7, windows, encoding, console | superuser | 👍 226 | 💬 9 answers

**Description**:
Tags: windows-7, windows, encoding, console | Score: 226 | Views: 563116 | Answers: 9

**Solution / Community Answer**:
To change the codepage for the console only, do the following:

Start -&gt; Run -&gt; regedit
Go to [HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\Autorun]
Change the value to @chcp 65001&gt;nul

If Autorun is not present, you can add a New String

**Reference**: https://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8

> 📎 Source: https://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8

#### 69. How to prevent Windows 10 from automatically adding keyboard layouts (i.e. US keyboard)

**Issue**: How to prevent Windows 10 from automatically adding keyboard layouts (i.e. US keyboard)
**Tags / Source**: Tags: windows, windows-10, keyboard, language, input-languages | superuser | 👍 223 | 💬 12 answers

**Description**:
Tags: windows, windows-10, keyboard, language, input-languages | Score: 223 | Views: 268606 | Answers: 12

**Solution / Community Answer**:
To fix this issue, delete the Preload registry folder and sign out or restart the computer:

HKEY_USERS\.DEFAULT\Keyboard Layout\Preload


This folder seems to be some legacy remnant that contains non-user-specified keyboard layouts to be added to the list of languages when the user signs in. While the fix itself works through restarts, at time of writing there's things that bring back that pesky folder, here's a few that I bumped into personally:


Remote desktop to a computer with US layout
Using the same Microsoft account on another PC that still has this
issue


Whenever the problem comes back, that registry folder needs to be deleted again.

Edit 2:
Thanks to @Lu55's suggestion, here's a handy one-liner to use on a command prompt with admin privileges:

reg delete "HKEY_USERS\.DEFAULT\Keyboard Layout\Preload" /f


Edit:
I have created a RemovePreload.reg text file with the following content, this way this fix can easily be re-applied every time without navigating the registry:

Windows Registry Editor Version 5.00

[-HKEY_USERS\.DEFAULT\Keyboard Layout\Preload]


To use this, save it in a text file and change the extension from .txt to .reg. Then whenever it comes back, you can just double click it and restart or sign out.

**Reference**: https://superuser.com/questions/1092246/how-to-prevent-windows-10-from-automatically-adding-keyboard-layouts-i-e-us-ke

> 📎 Source: https://superuser.com/questions/1092246/how-to-prevent-windows-10-from-automatically-adding-keyboard-layouts-i-e-us-ke

#### 70. Disable &quot;These files might be harmful to your computer&quot; warning?

**Issue**: Disable &quot;These files might be harmful to your computer&quot; warning?
**Tags / Source**: Tags: windows, networking, windows-explorer | superuser | 👍 223 | 💬 14 answers

**Description**:
Tags: windows, networking, windows-explorer | Score: 223 | Views: 365744 | Answers: 14

**Solution / Community Answer**:
I found a fix by changing &quot;internet options&quot; -- so I guess Windows is detecting the &quot;internet&quot; as my own network.. sigh.

Click Start / Control Panel / Internet Options
Click Security tab.
Click Local Intranet
Click Sites button.
Click Advanced button.
Enter the IP Address of the other machine or server (wildcards are allowed) and click Add
Click Close, then OK, then OK again.
Disconnect, and reconnect the network drive


This worked for me, but it's a bummer I have to manually enter IPs here.. it would be nice if Windows could detect this is a local network file copy and skip the irritating (and pointless) warning about &quot;dangerous&quot; files.
Sidenotes:

If you are using a DNS name (i.e. FQDN) to map the network drive, adding the IP address of the server to the zone will not work. You will need to add the DNS name (i.e. FQDN), and vice-versa.
When adding an IP address, you can use wildcards like so: 192.168.1.*
When adding a DNS name (i.e. FQDN), you can use wildcards like so: *.example.com

**Reference**: https://superuser.com/questions/149056/disable-these-files-might-be-harmful-to-your-computer-warning

> 📎 Source: https://superuser.com/questions/149056/disable-these-files-might-be-harmful-to-your-computer-warning

#### 71. What are CLOSE_WAIT and TIME_WAIT states?

**Issue**: What are CLOSE_WAIT and TIME_WAIT states?
**Tags / Source**: Tags: windows, networking, port, tcpip | superuser | 👍 221 | 💬 3 answers

**Description**:
Tags: windows, networking, port, tcpip | Score: 221 | Views: 610666 | Answers: 3

**Solution / Community Answer**:
Due to the way TCP/IP works, connections can not be closed immediately.  Packets may arrive out of order or be retransmitted after the connection has been closed.

CLOSE_WAIT indicates that the remote endpoint (other side of the connection) has closed the connection.
TIME_WAIT indicates that local endpoint (this side) has closed the connection.

The connection is being kept around so that any delayed packets can be matched to the connection and handled appropriately.  The connections will be removed when they time out within four minutes. See http://en.wikipedia.org/wiki/Transmission_Control_Protocol for more details.

**Reference**: https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states

> 📎 Source: https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states

#### 72. Preventing applications from stealing focus

**Issue**: Preventing applications from stealing focus
**Tags / Source**: Tags: windows, window-focus | superuser | 👍 220 | 💬 7 answers

**Description**:
Tags: windows, window-focus | Score: 220 | Views: 130694 | Answers: 7

**Solution / Community Answer**:
This is not possible without extensive manipulation of Windows internals and you need to get over it.

There are moments in daily computer use when it is really important that you make one action before the operating system allows you to do another. To do that, it needs to lock your focus on certain windows. In Windows, control over this behavior is largely left to the developers of the individual programs that you use.

Not every developer makes the right decisions when it comes to this topic.

I know that this is very frustrating and annoying, but you can't have your cake and eat it too. There are probably many cases throughout your daily life where you're perfectly fine with the focus being moved to a certain UI element or an application requesting that the focus remains locked on it. But most applications are somewhat equal when it comes to deciding who is the lead right now and the system can never be perfect.

A while ago I did extensive research on solving this issue once and for all (and failed). The result of my research can be found on the annoyance project page.

The project also includes an application that repeatedly tries to grab focus by calling:

switch( message ) {
  case WM_TIMER:
    if( hWnd != NULL ) {
      // Start off easy
      // SetForegroundWindow will not move the window to the foreground,
      // but it will invoke FlashWindow internally and, thus, show the
      // taskbar.
      SetForegroundWindow( hWnd );

      // Our application is awesome! It must have your focus!
      SetActiveWindow( hWnd );

      // Flash that button!
      FlashWindow( hWnd, TRUE );
    }
    break;


As we can see from this snippet, my research was also focused on other aspects of user interface behavior I don't like.

The way I tried to solve this was to load a DLL into every new process and hook the API calls that cause another windows to be activated.
The last part is the easy one, thanks to awesome API hooking libraries out there. I used the very great mhook library:

#include "stdafx.h"
#include "mhook-2.2/mhook-lib/mhook.h"

typedef NTSTATUS( WINAPI* PNT_QUERY_SYSTEM_INFORMATION ) ( 
  __in       SYSTEM_INFORMATION_CLASS SystemInformationClass,     
  __inout    PVOID SystemInformation, 
  __in       ULONG SystemInformationLength, 
  __out_opt  PULONG ReturnLength    
);

// Originals
PNT_QUERY_SYSTEM_INFORMATION OriginalFlashWindow   = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "FlashWindow" );

PNT_QUERY_SYSTEM_INFORMATION OriginalFlashWindowEx = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "FlashWindowEx" );

PNT_QUERY_SYSTEM_INFORMATION OriginalSetForegroundWindow = 
  (PNT_QUERY_SYSTEM_INFORMATION)::GetProcAddress( 
  ::GetModuleHandle( L"user32" ), "SetForegroundWindow" );

// Hooks
BOOL WINAPI
HookedFlashWindow(
  __in  HWND hWnd,
  __in  BOOL bInvert
  ) {
  return 0;
}

BOOL WINAPI 
HookedFlashWindowEx(
  __in  PFLASHWINFO pfwi
  ) {
  return 0;
}

BOOL WINAPI 
HookedSetForegroundWindow(
  __in  HWND hWnd
  ) {
  // Pretend window was brought to foreground
  return 1;
}


BOOL APIENTRY 
DllMain( 
  HMODULE hModule,
  DWORD   ul_reason_for_call,
  LPVOID  lpReserved
  ) {
  switch( ul_reason_for_call ) {
    case DLL_PROCESS_ATTACH:
      Mhook_SetHook( (PVOID*)&amp;OriginalFlashWindow,         HookedFlashWindow );
      Mhook_SetHook( (PVOID*)&amp;OriginalFlashWindowEx,       HookedFlashWindowEx );
      Mhook_SetHook( (PVOID*)&amp;OriginalSetForegroundWindow, HookedSetForegroundWindow );
      break;

    case DLL_PROCESS_DETACH:
      Mhook_Unhook( (PVOID*)&amp;OriginalFlashWindow );
      Mhook_Unhook( (PVOID*)&amp;OriginalFlashWindowEx );
      Mhook_Unhook( (PVOID*)&amp;OriginalSetForegroundWindow );
      break;
  }
  return TRUE;
}


From my tests back then, this worked great. Except for the part of loading the DLL into every new process. As one might imagine, that's nothing to take too lightly. I used the AppInit_DLLs approach back then (which is simply not sufficient).

Basically, this works great. But I never found the time to write something that properly injects my DLL into new processes. And the time invested in this largely overshadows the annoyance the focus stealing causes me.

In addition to the DLL injection problem, there is also a focus-stealing method which I didn't cover in the implementation on Google Code. A co-worker actually did some additional research and covered that method. The problem was discussed on SO: https://stackoverflow.com/questions/7430864/windows-7-prevent-application-from-losing-focus

**Reference**: https://superuser.com/questions/18383/preventing-applications-from-stealing-focus

> 📎 Source: https://superuser.com/questions/18383/preventing-applications-from-stealing-focus

#### 73. Why are there directories called Local, LocalLow, and Roaming under \Users\&lt;username&gt;\AppData?

**Issue**: Why are there directories called Local, LocalLow, and Roaming under \Users\&lt;username&gt;\AppData?
**Tags / Source**: Tags: windows, thunderbird, user-profiles | superuser | 👍 213 | 💬 3 answers

**Description**:
Tags: windows, thunderbird, user-profiles | Score: 213 | Views: 134967 | Answers: 3

**Solution / Community Answer**:
Roaming is the folder that would be synchronized with a server if you logged into a domain with a roaming profile (enabling you to log into any computer in a domain and access your favorites, documents, etc. Firefox stores its information here, so you could even have the same bookmarks between computers with a roaming profile.
Local is the folder that is specific to that computer - any information here would not be synchronized with a server. This folder is equivalent in Windows XP to C:\Documents and Settings\User\Local Settings\Application Data.
LocalLow is the same folder as local, but it has a lower integrity level. For example, Internet Explorer 8 can only write to the LocalLow folder (when protected mode is on).
This document from Microsoft (&quot;Managing Roaming User Data Deployment Guide&quot;) has a long explanation for what these three folder areas are and how they are used, as well as the changes implemented between Windows XP and Vista (Windows 7 retains the Vista structure).

**Reference**: https://superuser.com/questions/21458/why-are-there-directories-called-local-locallow-and-roaming-under-users-user

> 📎 Source: https://superuser.com/questions/21458/why-are-there-directories-called-local-locallow-and-roaming-under-users-user

#### 74. How to disable internet search results in start menu post Creators Update?

**Issue**: How to disable internet search results in start menu post Creators Update?
**Tags / Source**: Tags: windows-10, windows-10-v1703, cortana, windows-10-v1803 | superuser | 👍 212 | 💬 4 answers

**Description**:
Tags: windows-10, windows-10-v1703, cortana, windows-10-v1803 | Score: 212 | Views: 144810 | Answers: 4

**Solution / Community Answer**:
The article
The Windows 10 spring update no longer lets you disable web search in Start - workaround reports that the following registry update
is required in Windows 10 version 1803 :
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search]
&quot;BingSearchEnabled&quot;=dword:00000000
&quot;AllowSearchToUseLocation&quot;=dword:00000000
&quot;CortanaConsent&quot;=dword:00000000

It remarks :

those entries are completely missing from the &quot;Search&quot; registry key, so you can safely delete them should you want to revert.

I would still recommend to at least create a system restore point before doing
any registry modifications.
A reboot might be required.
User @mtd has contributed below these commands for applying the updates to
the registry:
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v BingSearchEnabled /t REG_DWORD /d 0
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v AllowSearchToUseLocation /t REG_DWORD /d 0
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /f /v CortanaConsent /t REG_DWORD /d 0


EDIT1 : There are reports that Windows 10 version 2004 has broken the above fix.
The article
Disable Web Search in Taskbar in Windows 10 Version 2004
has a summary of the current state of the problem.
The current solution seems to be to download and run this
PowerShell script
as Administrator:
Set-ExecutionPolicy Unrestricted -Scope Process
.\disable-web-search.ps1

As only a workaround, this PowerShell script blocks the online search using
Windows Firewall rules, so forcing the search to operate in offline mode.

EDIT2: Reports now say that these registry modification are working for
Windows versions 2004 and 20H2 without reboot.

EDIT3: Windows 11 21H2 - it has been reported that it is
also required to create in the registry key
HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer,
a DWORD32 value named DisableSearchBoxSuggestions
and set its value to 1.
More information in the article
How to Disable Web Search Results in Start Menu on Windows 11.

**Reference**: https://superuser.com/questions/1196618/how-to-disable-internet-search-results-in-start-menu-post-creators-update

> 📎 Source: https://superuser.com/questions/1196618/how-to-disable-internet-search-results-in-start-menu-post-creators-update

#### 75. How to delete a file in Windows with a too long filename?

**Issue**: How to delete a file in Windows with a too long filename?
**Tags / Source**: Tags: windows, path, filenames | superuser | 👍 211 | 💬 8 answers

**Description**:
Tags: windows, path, filenames | Score: 211 | Views: 406543 | Answers: 8

**Solution / Community Answer**:
When you want to completely delete a directory and it contains long paths, robocopy does a VERY good job:

mkdir empty_dir
robocopy empty_dir the_dir_to_delete /mir
rmdir empty_dir
rmdir the_dir_to_delete


This works because robocopy internally uses the Unicode-aware versions of Win32 functions, with the \\?\ prefix for file paths; those functions have a limit of 2¹⁶-1 (32,767) characters instead of 259.

You may need to go through this process more than once to get rid of all of the files.

**Reference**: https://superuser.com/questions/45697/how-to-delete-a-file-in-windows-with-a-too-long-filename

> 📎 Source: https://superuser.com/questions/45697/how-to-delete-a-file-in-windows-with-a-too-long-filename

#### 76. How to copy text from Console2?

**Issue**: How to copy text from Console2?
**Tags / Source**: Tags: windows, console, copy-paste, console2 | superuser | 👍 210 | 💬 10 answers

**Description**:
Tags: windows, console, copy-paste, console2 | Score: 210 | Views: 46862 | Answers: 10

**Solution / Community Answer**:
Open Console2 menu Edit -> Settings, and in the Hotkeys / Mouse settings configure the selection and copy actions. The defaults are a bit wonky. 

I use: 


Left mouse button = select
Ctrl+C = copy
Ctrl+V = paste
ESC = clear selection


Make sure you press 'Assign' after each change you make otherwise it won't take effect.

Last note: Beware if you use ESC or Ctrl+V in vim, or in any other app.

**Reference**: https://superuser.com/questions/132711/how-to-copy-text-from-console2

> 📎 Source: https://superuser.com/questions/132711/how-to-copy-text-from-console2

#### 77. How can I create a symbolic link on Windows 10?

**Issue**: How can I create a symbolic link on Windows 10?
**Tags / Source**: Tags: windows-10, symbolic-link | superuser | 👍 210 | 💬 6 answers

**Description**:
Tags: windows-10, symbolic-link | Score: 210 | Views: 618994 | Answers: 6

**Solution / Community Answer**:
It seems like the junction command has been retired in Windows 10.
You can download junction from Windows SysInternals (which is part of Microsoft):

Junction not only allows you to create NTFS junctions, it allows you to see if files or directories are actually reparse points. Reparse points are the mechanism on which NTFS junctions are based, and they are used by Windows' Remote Storage Service (RSS), as well as volume mount points.
Please read this Microsoft KB article for tips on using junctions.
Note that Windows does not support junctions to directories on remote shares.


So how do I create junctions or directory symbolic links in Windows 10?
Download junction as instructed above.
Now you can use the following commands.
Create a junction:
junction &quot;C:\Documents and Settings\UserName\My Documents\My Dropbox\My Games&quot; &quot;C:\Documents and Settings\UserName\My Documents\My Games&quot;

Create a directory symbolic link:
mklink /D &quot;C:\Documents and Settings\UserName\My Documents\My Dropbox\My Games&quot; &quot;C:\Documents and Settings\UserName\My Documents\My Games&quot;

You can use either mklink /j or junction in Windows 10 and upwards to create junctions.
You can use mklink /d in Windows 10 and upwards to create directory symbolic links.
Notes:

junction can also list junctions and determine if a file is a junction unlike mklink.

mklink is an internal command only available within a cmd shell.

By default Administrator privileges are required to create symbolic links.
It can also be granted to other users. The security setting &quot;Create symbolic links&quot; can be granted at:
  Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\




Examples
Using mklink to create a directory symbolic link:
F:\test&gt;mklink /d test-dir-sym-link test
symbolic link created for test-dir-sym-link &lt;&lt;===&gt;&gt; test

Using mklink to create a junction:
F:\test&gt;mklink /j test-junction test
Junction created for test-junction &lt;&lt;===&gt;&gt; test

Using junction to create a junction:
F:\test&gt;C:\apps\NirSoft\SysinternalsSuite\junction.exe test-junction test

Junction v1.06 - Windows junction creator and reparse point viewer
Copyright (C) 2000-2010 Mark Russinovich
Sysinternals - www.sysinternals.com

Created: F:\test\test-junction
Targetted at: F:\test\test


Further Reading

An A-Z Index of the Windows CMD command line - An excellent reference for all things Windows cmd line related.
mklink - Create a symbolic link to a directory or a file, or create a hard file link or directory junction.

**Reference**: https://superuser.com/questions/1020821/how-can-i-create-a-symbolic-link-on-windows-10

> 📎 Source: https://superuser.com/questions/1020821/how-can-i-create-a-symbolic-link-on-windows-10

#### 78. &quot;This file came from another computer...&quot; - how can I unblock all the files in a folder without having to unblock them individually?

**Issue**: &quot;This file came from another computer...&quot; - how can I unblock all the files in a folder without having to unblock them individually?
**Tags / Source**: Tags: windows, security, ntfs | superuser | 👍 209 | 💬 15 answers

**Description**:
Tags: windows, security, ntfs | Score: 209 | Views: 301626 | Answers: 15

**Solution / Community Answer**:
If you download a .ZIP and unzip it, the individual files will be marked as the same zone as the .ZIP.  Almost every time I have a folder full of "blocked" files, this is how I got them.

Before unzipping, click the Unblock button on the .ZIP.

**Reference**: https://superuser.com/questions/38476/this-file-came-from-another-computer-how-can-i-unblock-all-the-files-in-a

> 📎 Source: https://superuser.com/questions/38476/this-file-came-from-another-computer-how-can-i-unblock-all-the-files-in-a

#### 79. How do I edit text files in the Windows command prompt?

**Issue**: How do I edit text files in the Windows command prompt?
**Tags / Source**: Tags: windows, command-line, ssh, text-editors | superuser | 👍 209 | 💬 14 answers

**Description**:
Tags: windows, command-line, ssh, text-editors | Score: 209 | Views: 1380568 | Answers: 14

**Solution / Community Answer**:
The simplest solution on all versions of Windows is:

C:\&gt; notepad somefile.txt


And, no extra software required.

**Reference**: https://superuser.com/questions/186857/how-do-i-edit-text-files-in-the-windows-command-prompt

> 📎 Source: https://superuser.com/questions/186857/how-do-i-edit-text-files-in-the-windows-command-prompt

#### 80. How can I put the computer to sleep from Command Prompt/Run menu?

**Issue**: How can I put the computer to sleep from Command Prompt/Run menu?
**Tags / Source**: Tags: windows, command-line, sleep, shutdown, run-dialog | superuser | 👍 209 | 💬 14 answers

**Description**:
Tags: windows, command-line, sleep, shutdown, run-dialog | Score: 209 | Views: 792670 | Answers: 14

**Solution / Community Answer**:
You will find shutdown.exe to be your friend.
Other handy commands see this post:
Sleep Computer (read more at https://superuser.com/a/463652/249349 )
Lock Workstation
Hibernate Computer - see answers by Scott Chamberlain and Eric L.
Restart Computer
Shutdown.exe -r -t 00

Shutdown Computer
Shutdown.exe -s -t 00

EDIT/UPDATE:
It seems that sleeping a computer is problematic if hibernate is turned on.
Copying from other answers:
You can either try PsShutdown
or:

The command rundll32.exe powrprof.dll,SetSuspendState 0,1,0 for sleep
is correct - however, it will hibernate instead of sleep if you don't
turn the hibernation off.
Here's how to do that:
Go to the Start Menu and open an elevated Command Prompt by typing
cmd.exe, right clicking and choosing Run as administrator. Type the
following command:

powercfg -hibernate off

**Reference**: https://superuser.com/questions/42124/how-can-i-put-the-computer-to-sleep-from-command-prompt-run-menu

> 📎 Source: https://superuser.com/questions/42124/how-can-i-put-the-computer-to-sleep-from-command-prompt-run-menu

#### 81. How do I view the contents of a PFX file on Windows?

**Issue**: How do I view the contents of a PFX file on Windows?
**Tags / Source**: Tags: windows, security, certificate, client-certificate | superuser | 👍 206 | 💬 6 answers

**Description**:
Tags: windows, security, certificate, client-certificate | Score: 206 | Views: 450692 | Answers: 6

**Solution / Community Answer**:
Some options to view PFX file details:


Open a command prompt and type: certutil -dump &lt;path to cert&gt;
Install OpenSSL and use the commands to view the details, such as: openssl pkcs12 -info -in &lt;path to cert&gt;

**Reference**: https://superuser.com/questions/580697/how-do-i-view-the-contents-of-a-pfx-file-on-windows

> 📎 Source: https://superuser.com/questions/580697/how-do-i-view-the-contents-of-a-pfx-file-on-windows

#### 82. How to access Windows folders from Bash on Ubuntu on Windows

**Issue**: How to access Windows folders from Bash on Ubuntu on Windows
**Tags / Source**: Tags: windows-10, bash, shell, windows-subsystem-for-linux | superuser | 👍 202 | 💬 2 answers

**Description**:
Tags: windows-10, bash, shell, windows-subsystem-for-linux | Score: 202 | Views: 353691 | Answers: 2

**Solution / Community Answer**:
You'll find the Windows C:\ structure at /mnt/c/ in the Bash environment.

Therefore, my Documents folder is at /mnt/c/Users/Ben/Documents/.

**Reference**: https://superuser.com/questions/1066261/how-to-access-windows-folders-from-bash-on-ubuntu-on-windows

> 📎 Source: https://superuser.com/questions/1066261/how-to-access-windows-folders-from-bash-on-ubuntu-on-windows

#### 83. How do I create a GIF screencast in Windows?

**Issue**: How do I create a GIF screencast in Windows?
**Tags / Source**: Tags: windows, software-rec, screen-capture, animated-gif | superuser | 👍 201 | 💬 10 answers

**Description**:
Tags: windows, software-rec, screen-capture, animated-gif | Score: 201 | Views: 161751 | Answers: 10

**Solution / Community Answer**:
I've been using licecap in various Super&nbsp;User answers. It's dead simple to use as you can see from this animated GIF image - just extend it over your recording area, hit record, set a save file, do your thing and hit stop. It's free, works pretty well, and seems simpler than most of the alternatives. It's entirely free and has Windows and OS X ports.



On Windows 8.1 and hdpi displays, you'll need to turn off per app display scaling to get it to work normally without turning off global display scaling. I have a walkthrough on it here (Fixed as of version 1.26.)

**Reference**: https://superuser.com/questions/81826/how-do-i-create-a-gif-screencast-in-windows

> 📎 Source: https://superuser.com/questions/81826/how-do-i-create-a-gif-screencast-in-windows

#### 84. Windows 10 Search can&#39;t find ANY applications. Even calculator

**Issue**: Windows 10 Search can&#39;t find ANY applications. Even calculator
**Tags / Source**: Tags: windows, search, windows-10 | superuser | 👍 201 | 💬 13 answers

**Description**:
Tags: windows, search, windows-10 | Score: 201 | Views: 390409 | Answers: 13

**Solution / Community Answer**:
I have no idea why or what I have broken in the process.
But here is what worked for me.


Ctrl+Shift+Right-click on an empty part of the taskbar and clicking "Exit Explorer" (or kill it via Task Manager if that doesn't work).
Delete this registry key.



  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderTypes\{ef87b4cb-f2ce-4785-8658-4ca6c63e38c6}\TopViews\{00000000-0000-0000-0000-000000000000}



Start process Explorer.exe via Task Manager.


This is one of many answers posted here. Feel free to try other people's suggestions. If you combine all answers in one I'll accept your answer.





Method for Creator's update
Check out this answer.

**Reference**: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator

> 📎 Source: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator

#### 85. How can I make the Windows VPN route selective traffic (by destination network)?

**Issue**: How can I make the Windows VPN route selective traffic (by destination network)?
**Tags / Source**: Tags: windows, networking, vpn, routing | superuser | 👍 200 | 💬 13 answers

**Description**:
Tags: windows, networking, vpn, routing | Score: 200 | Views: 430954 | Answers: 13

**Solution / Community Answer**:
You can turn off taking over your entire connection by going to the properties of the VPN, Networking tab, Internet Protocol (TCP/IP) properties, Advanced, untick Use default gateway on remote network. This may or may not leave a route to 192.168.123.0/24 depending on the VPN server's setup. If it doesn't, you'll have to manually add the route each time, although you could put it in a batch file.

In order to manually add the route, run (as administrator):

route -p add 192.168.0.12 mask 255.255.255.255 10.100.100.254


This example will make a persistent (it's not necessary to run the command after a reboot) route to the IP 192.168.0.12 through the VPN gateway 10.100.100.254.

More about this at http://technet.microsoft.com/en-us/library/bb878117.aspx

**Reference**: https://superuser.com/questions/12022/how-can-i-make-the-windows-vpn-route-selective-traffic-by-destination-network

> 📎 Source: https://superuser.com/questions/12022/how-can-i-make-the-windows-vpn-route-selective-traffic-by-destination-network

#### 86. Why is &#39;ping&#39; unable to resolve a name when &#39;nslookup&#39; works fine?

**Issue**: Why is &#39;ping&#39; unable to resolve a name when &#39;nslookup&#39; works fine?
**Tags / Source**: Tags: windows, networking, dns | superuser | 👍 200 | 💬 24 answers

**Description**:
Tags: windows, networking, dns | Score: 200 | Views: 453478 | Answers: 24

**Solution / Community Answer**:
I believe that nslookup opens a winsock connection on the DNS port and issues a query, whereas ping uses the DNS Client service. You could try and stop this service and see whether this makes a difference.
Some commands that will reinitialize various network states :
Reset WINSOCK entries to installation defaults : netsh winsock reset catalog
Reset TCP/IP stack to installation defaults : netsh int ip reset reset.log
Flush DNS resolver cache : ipconfig /flushdns
Renew DNS client registration and refresh DHCP leases : ipconfig /registerdns
Flush routing table : route /f
(Caution: this will remove all your routes and gateways until you restart!)

**Reference**: https://superuser.com/questions/495759/why-is-ping-unable-to-resolve-a-name-when-nslookup-works-fine

> 📎 Source: https://superuser.com/questions/495759/why-is-ping-unable-to-resolve-a-name-when-nslookup-works-fine

#### 87. Hyper-V VM won&#39;t boot from Cd, error: &quot;unsigned image&#39;s hash is not allowed&quot;

**Issue**: Hyper-V VM won&#39;t boot from Cd, error: &quot;unsigned image&#39;s hash is not allowed&quot;
**Tags / Source**: Tags: windows-10, hyper-v, bootable-media | superuser | 👍 200 | 💬 5 answers

**Description**:
Tags: windows-10, hyper-v, bootable-media | Score: 200 | Views: 169855 | Answers: 5

**Solution / Community Answer**:
This error is a consequence of having Secure Boot enabled on the VM. Secure Boot prevents the system from getting hijacked at boot time by only allowing specifically authorized boot images to load. In Hyper-V client, the list is rather short.

To disable Secure Boot, power off the VM and then open the VM settings. Under Secure Boot, uncheck the box "Enable Secure Boot" and then click "OK". This will allow the VM to boot the "unauthorized" CD image.

Update: 
As mentioned by Itai Bar-Haim in the comments, and Thee Gamefanatic said in their answer, you can also select a different template depending on the OS image you're attempting to boot. Be aware that these templates are mutually exclusive - this means that you will not be able to boot a Windows OS image if you select the "Microsoft UEFI Certificate Authority" template.

Microsoft has a thorough deep dive into Secure Boot and how it works available on this blog:
https://blogs.technet.microsoft.com/dubaisec/2016/03/14/diving-into-secure-boot/

**Reference**: https://superuser.com/questions/1026190/hyper-v-vm-wont-boot-from-cd-error-unsigned-images-hash-is-not-allowed

> 📎 Source: https://superuser.com/questions/1026190/hyper-v-vm-wont-boot-from-cd-error-unsigned-images-hash-is-not-allowed

#### 88. Remote Desktop intermittently freezing

**Issue**: Remote Desktop intermittently freezing
**Tags / Source**: Tags: windows-10, remote-desktop, windows-10-v1903 | superuser | 👍 200 | 💬 8 answers

**Description**:
Tags: windows-10, remote-desktop, windows-10-v1903 | Score: 200 | Views: 369955 | Answers: 8

**Solution / Community Answer**:
I also ran into this issue since July 2019 on a Windows 10 1903 acting as the client machine. The following workaround on the client works for me, so that RDP no longer freezes.

Start an elevated command prompt (run cmd.exe as administrator), and
then run:
reg add &quot;HKLM\software\policies\microsoft\windows nt\Terminal
Services\Client&quot; /v fClientDisableUDP /d 1 /t REG_DWORD

After that, close and reopen all your RDP sessions on your client computer to restart the Remote Desktop Client (mstsc.exe, aka Microsoft Terminal Services Client) application.
I'm waiting for a final fix to this issue.
Follow-up: I am not sure, but it looks like fixed in 21H1 (both client and server must run 21H1 or higher). For me I no longer see freezes without the disable UDP workaround.

**Reference**: https://superuser.com/questions/1481191/remote-desktop-intermittently-freezing

> 📎 Source: https://superuser.com/questions/1481191/remote-desktop-intermittently-freezing

#### 89. How to stop Microsoft from gathering telemetry data from Windows 7, 8, and 8.1

**Issue**: How to stop Microsoft from gathering telemetry data from Windows 7, 8, and 8.1
**Tags / Source**: Tags: windows-7, windows, windows-8, windows-8.1 | superuser | 👍 199 | 💬 2 answers

**Description**:
Tags: windows-7, windows, windows-8, windows-8.1 | Score: 199 | Views: 323021 | Answers: 2

**Solution / Community Answer**:
Is there a way to disable the telemetry through some setting(s)?

Some telemetry can be disabled through settings.

This can be done manually.
There are also 3rd-party utilities such as Windows 10 Privacy Fixer and O&amp;O ShutUp10 which fix these settings in Windows 10.

Is it necessary to dig up which update patches are involved in the data gathering, and remove those?


Some telemetry disabling requires removal of (or not installing) patches.


Manually disabling Telemetry through settings (Windows 7, 8, and 8.1)

Disable the Windows Customer Experience Improvement Program (CEIP)
Note:
Disabling CEIP and the  related Task Scheduler tasks that control this program can improve Windows system performance.



Start &quot;Control Panel&quot; &gt; &quot;Action Center&quot; &gt; &quot;Change Action Center settings&quot;.







Click &quot;Customer Experience Improvement Program settings&quot;.







Select &quot;No, I don't want to participate in the program&quot; then click &quot;Save changes&quot;.







Start &gt; &quot;Control Panel&quot; &gt; &quot;Administrative Tools&quot; &gt; &quot;Task Scheduler&quot;.

In the Task Scheduler (Local) pane of the Task Scheduler dialog box,  expand &quot;Task Scheduler Library&quot; &gt; &quot;Microsoft&quot; &gt; &quot;Windows&quot; and open  the &quot;Application Experience&quot; folder.

Disable the &quot;AITAgent&quot; and &quot;ProgramDataUpdater&quot; tasks.

In &quot;Task Scheduler Library&quot; &gt; &quot;Microsoft&quot; &gt; &quot;Windows&quot;, open the  &quot;Customer Experience Improvement Program&quot; folder.

Disable the &quot;Consolidator&quot;, &quot;KernelCeipTask&quot;, and &quot;UsbCeip&quot; tasks.






Source Privacy Windows 10, Windows 7, Linux MINT - How do they compare?

Disabling Telemetry through patch removal (Windows 7, 8, and 8.1)
As Anixx has pointed out, there are some telemetry services that cannot be disabled through settings:


Telemetry-4xd,
refreshgwxconfig-B,
WSRefreshBannedAppsListTask,
Time-5d,
refreshgwxconfigandcontent,
Logon-5d,
MachineUnlock-5d,
OutOfIdle-5d,
OutOfSleep-5d,
Secure-Boot-Update, and
Tpm-Maintenance.

Also on any program crash the system reports the crash data to a server (although it is not connected with any scheduled task)


Stop Windows Telemetry/Tracking/Upgrading to Windows 10

Below are instructions for disabling the unwanted telemetry/tracking
in Windows 7 and 8.1 and removing all updates associated with
upgrading to Windows 10.




Here is the list of Windows updates to remove.




Before uninstalling them and rebooting make sure that you have Windows Update set to not automatically install updates:


KB3065988 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: July 2015 more info
KB3083325 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: September 2015 more info
KB3083324 Windows Update Client for Windows 7 and Windows Server 2008 R2: September 2015 more info
KB2976978 Compatibility update for Windows 8.1 and Windows 8 more info
KB3075853 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: August 2015 more info
KB3065987 Windows Update Client for Windows 7 and Windows Server 2008 R2: July 2015 more info
KB3050265 Windows Update Client for Windows 7: June 2015 more info
KB3050267 Windows Update Client for Windows 8.1: June 2015 more info
KB3075851 Windows Update Client for Windows 7 and Windows Server 2008 R2: August 2015 more info
KB2902907 MS Security Essentials/Windows Defender related update [no description/information available]
KB3068708 Update for customer experience and diagnostic telemetry more info
KB3022345 Update for customer experience and diagnostic telemetry more info
KB2952664 Compatibility update for upgrading Windows 7 more info
KB2990214 Update that enables you to upgrade from Windows 7 to a later version of Windows more info
KB3035583 Update installs Get Windows 10 app in Windows 8.1 and Windows 7 SP1 more info
KB971033 Description of the update for Windows Activation Technologies more info
KB3021917 Update to Windows 7 SP1 for performance improvements more info
KB3044374 Update that enables you to upgrade from Windows 8.1 to a later version of Windows more info
KB3046480 Update helps to determine whether to migrate the .NET Framework 1.1 when you upgrade Windows 8.1 or Windows 7 more info
KB3075249 Update that adds telemetry points to consent.exe in Windows 8.1 and Windows 7 more info
KB3080149 Update for customer experience and diagnostic telemetry more info
KB3083324 Windows Update Client for Windows 7 and Windows Server 2008 R2: September 2015 more info
KB3083325 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: September 2015 more info
KB3083710 Windows Update Client for Windows 7 and Windows Server 2008 R2: October 2015 more info
KB3083711 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: October 2015 more info
KB3112336 Windows Update Client for Windows 8.1 and Windows Server 2012 R2: December 2015 more info
KB3123862 Updated capabilities to upgrade Windows 8.1 and Windows 7


They can be uninstalled manually via elevated command prompt with the following commands:

wusa /uninstall /kb:3065988 /quiet /norestart
wusa /uninstall /kb:3083325 /quiet /norestart
wusa /uninstall /kb:3083324 /quiet /norestart
wusa /uninstall /kb:2976978 /quiet /norestart
wusa /uninstall /kb:3075853 /quiet /norestart
wusa /uninstall /kb:3065987 /quiet /norestart
wusa /uninstall /kb:3050265 /quiet /norestart
wusa /uninstall /kb:3050267 /quiet /norestart
wusa /uninstall /kb:3075851 /quiet /norestart
wusa /uninstall /kb:2902907 /quiet /norestart
wusa /uninstall /kb:3068708 /quiet /norestart
wusa /uninstall /kb:3022345 /quiet /norestart
wusa /uninstall /kb:2952664 /quiet /norestart
wusa /uninstall /kb:2990214 /quiet /norestart
wusa /uninstall /kb:3035583 /quiet /norestart
wusa /uninstall /kb:971033 /quiet /norestart
wusa /uninstall /kb:3021917 /quiet /norestart
wusa /uninstall /kb:3044374 /quiet /norestart
wusa /uninstall /kb:3046480 /quiet /norestart
wusa /uninstall /kb:3075249 /quiet /norestart
wusa /uninstall /kb:3080149 /quiet /norestart
wusa /uninstall /kb:2977759 /quiet /norestart
wusa /uninstall /kb:3083710 /quiet /norestart
wusa /uninstall /kb:3083711 /quiet /norestart
wusa /uninstall /kb:3112336 /quiet /norestart
wusa /uninstall /kb:3123862 /quiet /norestart


Don’t forget to reboot afterwards. You can proceed to finish the next steps before rebooting.




The following services should be removed:




In an elevated command prompt run the following:


sc stop DiagTrack
sc stop dmwappushservice
sc delete DiagTrack
sc delete dmwappushservice
echo &quot;&quot; &gt; C:\ProgramData\Microsoft\Diagnosis\ETLLogs\AutoLogger\AutoLogger-Diagtrack-Listener.etl




Open the Task Scheduler (Win key then type &quot;sched&quot;). Under Task Scheduler Library -&gt; Microsoft -&gt; Windows delete the following items:


Everything under &quot;Application Experience&quot;

Everything under &quot;Autochk&quot;

Everything under &quot;Customer Experience Improvement Program&quot;

Under &quot;Disk Diagnostic&quot; delete only the &quot;Microsoft-Windows-DiskDiagnosticDataCollector&quot;

Under &quot;Maintenance&quot; &quot;WinSAT&quot; &quot;Media Center&quot; and click the &quot;status&quot; column, then select all non-disabled entries and disable them.

Now you can reboot. When you open Windows Update again it will ask to install whichever updates above were removed. Right-click on each one and select &quot;hide&quot;.






Finally, log in to your broadband router and look for an option like &quot;content filtering&quot; or &quot;block sites&quot;.




Add the following hosts to be blocked. On a Netgear router each host is a keyword that must be added.


Note, as Matthew Steeples has pointed out, a-0001.a-msedge.net is a CDN endpoint and has uses in non-telemetry scenarios.
134.170.30.202
137.116.81.24
204.79.197.200
23.218.212.69
65.39.117.230
65.55.108.23
a-0001.a-msedge.net
choice.microsoft.com
choice.microsoft.com.nsatc.net
compatexchange.cloudapp.net
corp.sts.microsoft.com
corpext.msitadfs.glbdns2.microsoft.com
cs1.wpc.v0cdn.net
df.telemetry.microsoft.com
diagnostics.support.microsoft.com
fe2.update.microsoft.com.akadns.net
feedback.microsoft-hohm.com
feedback.search.microsoft.com
feedback.windows.com
i1.services.social.microsoft.com
i1.services.social.microsoft.com.nsatc.net
oca.telemetry.microsoft.com
oca.telemetry.microsoft.com.nsatc.net
pre.footprintpredict.com
redir.metaservices.microsoft.com
reports.wes.df.telemetry.microsoft.com
services.wes.df.telemetry.microsoft.com
settings-sandbox.data.microsoft.com
sls.update.microsoft.com.akadns.net
sqm.df.telemetry.microsoft.com
sqm.telemetry.microsoft.com
sqm.telemetry.microsoft.com.nsatc.net
statsfe1.ws.microsoft.com
statsfe2.update.microsoft.com.akadns.net
statsfe2.ws.microsoft.com
survey.watson.microsoft.com
telecommand.telemetry.microsoft.com
telecommand.telemetry.microsoft.com.nsatc.net
telemetry.appex.bing.net
telemetry.appex.bing.net:443
telemetry.microsoft.com
telemetry.urs.microsoft.com
vortex.data.microsoft.com
vortex-sandbox.data.microsoft.com
vortex-win.data.microsoft.com
watson.live.com
watson.microsoft.com
watson.ppe.telemetry.microsoft.com
watson.telemetry.microsoft.com
watson.telemetry.microsoft.com.nsatc.net
wes.df.telemetry.microsoft.com

Source Stop Windows Telemetry/Tracking/Upgrading to Win10

Disabling Telemetry using 3rd-party utilities (Windows 10)
Windows 10 Privacy Fixer
Windows 10 Privacy Fixer provides a privacy check with options to fix a number of settings, including those related to Telemetry.



Source Windows 10 Privacy Fixer.
O&amp;O ShutUp10

O&amp;O ShutUp10 is a tiny portable tool which makes it easy to tweak
Windows 10's many privacy settings.
Launching the program displays almost 50 options, organised into
various categories: Security (telemetry, wifi sense, DRM), Privacy
(Cortana, input personalisation, app permissions), Windows Update
(disable peer-to-peer updates, disable automatic updates) and more.
These aren't always clearly described, but clicking any item displays
more details on what it does.
There are options to disable only the worst offenders (turn off
telemetry, peer-to-peer updates, keep Windows Update and SmartScreen),
turn off everything, or tweak individual settings.
ShutUp10 offers to create a system restore point before it makes any
changes, useful if your tweaking breaks something important and you
need an &quot;undo&quot;.
There's also a separate option to restore Windows 10's default privacy
settings, which might also be handy if they're generally messed up and
you'd like to start again.

Source O&amp;O ShutUp10.



Image source Windows 10 Is Watching: Should You Be Worried?

Disclaimer
I am not affiliated with 10 Privacy Fixer or O&amp;O ShutUp10.

**Reference**: https://superuser.com/questions/972501/how-to-stop-microsoft-from-gathering-telemetry-data-from-windows-7-8-and-8-1

> 📎 Source: https://superuser.com/questions/972501/how-to-stop-microsoft-from-gathering-telemetry-data-from-windows-7-8-and-8-1

#### 90. On my Windows machine, I had a folder with a name of four dots that acted like some kind of rabbit hole - how did that happen?

**Issue**: On my Windows machine, I had a folder with a name of four dots that acted like some kind of rabbit hole - how did that happen?
**Tags / Source**: Tags: windows, filesystems | superuser | 👍 196 | 💬 5 answers

**Description**:
Tags: windows, filesystems | Score: 196 | Views: 40751 | Answers: 5

**Solution / Community Answer**:
Win32 doesn't let you create files or folders with names ending in . – all dots are stripped from the end. Trying to create test. makes test appear instead. (This is for compatibility with 8.3 names in old DOS/Win9x era software.)

As a result, whenever you try to access a folder named ...., its name gets reduced to the empty string, and you're back to the folder you were in before.

The NT kernel, however, does allow such names. There are various mechanisms which bypass filename limitations imposed by Win32 APIs – for example, WSL (Windows Subsystem for Linux) doesn't run on top of Win32 and is unaffected by it. There is also the \\?\ bypass method, a deliberate "backdoor" left in for programs which know what they're doing. Even though you cannot create C:\Example\....\, you can create \\?\C:\Example\....\ just fine.

Likewise you can delete such directories with rmdir \\?\C:\path\... from Cmd (I haven't tested with PowerShell yet).

Various file managers, archivers, etc. might use the \\?\ method in order to be able to use longer path names than usual – and by doing so, they're also unaffected by the compatibility code within Win32; they bypass dot stripping, as well as translation of magic filenames like CON or NUL.

So it could be that one of your programs:


always uses \\?\ to access files, 
accidentally tried to create a folder named .... – but it's not really possible to know for sure after the fact.

**Reference**: https://superuser.com/questions/1371527/on-my-windows-machine-i-had-a-folder-with-a-name-of-four-dots-that-acted-like-s

> 📎 Source: https://superuser.com/questions/1371527/on-my-windows-machine-i-had-a-folder-with-a-name-of-four-dots-that-acted-like-s

#### 91. How to access linux/Ubuntu files from Windows 10 WSL?

**Issue**: How to access linux/Ubuntu files from Windows 10 WSL?
**Tags / Source**: Tags: windows-10, windows-10-v1607, windows-subsystem-for-linux | superuser | 👍 196 | 💬 15 answers

**Description**:
Tags: windows-10, windows-10-v1607, windows-subsystem-for-linux | Score: 196 | Views: 440334 | Answers: 15

**Solution / Community Answer**:
PM for Windows Command-Line here:

Updated October 2019: Updating the response below to reflect the newly added ability to directly access distros' Linux files via the newly integrated P9 server in Win10 1903 (and later).
IMPORTANT: Spelunking through the Windows filesystem to access Linux files has and will continue to be unsupported and STRONGLY recommended against! To understand why, please read this post

So how does one access Linux files using Windows tools (e.g. notepad, VS/VScode, etc.)? Previously, you couldn't, but starting in Windows 10 1903 we (finally!) expose your distros' filesystems to Windows via a P9 fileserver. We've also published an in-depth video discussing how this works! You can also read a summary of this new feature in this blog post

Look forward to hearing how you get on with this feature. If you find any problems, please file issues on the WSL GitHub repo here: https://github.com/Microsoft/wsl.

**Reference**: https://superuser.com/questions/1110974/how-to-access-linux-ubuntu-files-from-windows-10-wsl

> 📎 Source: https://superuser.com/questions/1110974/how-to-access-linux-ubuntu-files-from-windows-10-wsl

#### 92. How can I determine file type without an extension on Windows?

**Issue**: How can I determine file type without an extension on Windows?
**Tags / Source**: Tags: windows, file-management, file-extension | superuser | 👍 194 | 💬 7 answers

**Description**:
Tags: windows, file-management, file-extension | Score: 194 | Views: 322511 | Answers: 7

**Solution / Community Answer**:
You can use the TrID tool which has a growing library of file type definitions for identifying files with.



Wildcards are supported, so in your example you could just put all the images to be examined in a folder, e.g. C:\verifyimages - then you can use the command:

trid C:\verifyimages\*


This will examine all files in the verifyimages folder.



There is also a GUI version available, TrIDNet:



There is documentation available on how you can you can easily integrate TrID or TrIDNet into Windows Explorer and Total Commander:

Windows Explorer


Integrate TrID
Integrate TrIDNet


Total Commander


Integrate TrID
Integrate TrIDNet

**Reference**: https://superuser.com/questions/274734/how-can-i-determine-file-type-without-an-extension-on-windows

> 📎 Source: https://superuser.com/questions/274734/how-can-i-determine-file-type-without-an-extension-on-windows

#### 93. How can I prevent a policy-enforced screen lock in Windows?

**Issue**: How can I prevent a policy-enforced screen lock in Windows?
**Tags / Source**: Tags: windows, screensaver, security-policy | superuser | 👍 192 | 💬 18 answers

**Description**:
Tags: windows, screensaver, security-policy | Score: 192 | Views: 754710 | Answers: 18

**Solution / Community Answer**:
If Windows Media Player is still installed, you can play a video on loop and minimize it (the sample "Wildlife" videos work fine for this).  By default, as long as a video is playing, the screen won't lock.

**Reference**: https://superuser.com/questions/329758/how-can-i-prevent-a-policy-enforced-screen-lock-in-windows

> 📎 Source: https://superuser.com/questions/329758/how-can-i-prevent-a-policy-enforced-screen-lock-in-windows

#### 94. How do I delete a folder that&#39;s in use?

**Issue**: How do I delete a folder that&#39;s in use?
**Tags / Source**: Tags: windows, file-management | superuser | 👍 191 | 💬 18 answers

**Description**:
Tags: windows, file-management | Score: 191 | Views: 655536 | Answers: 18

**Solution / Community Answer**:
There's a native GUI for Windows:

Start>>All Programs>>Accessories>>System Tools>>Resource Monitor (or Run resmon.exe)

You can search for the "Associated Handles" using the searchbox (circled in red), and right click the process you want to end.



As an example, in the image below I could not delete my Eclipse directory. Searching for the Eclipse associated handles showed that the adb.exe had a handle to the directory. After ending the adb process, I could then delete the Eclipse directory.

**Reference**: https://superuser.com/questions/2937/how-do-i-delete-a-folder-thats-in-use

> 📎 Source: https://superuser.com/questions/2937/how-do-i-delete-a-folder-thats-in-use

#### 95. Create .zip folder from the command line - (Windows)

**Issue**: Create .zip folder from the command line - (Windows)
**Tags / Source**: Tags: windows | superuser | 👍 190 | 💬 12 answers

**Description**:
Tags: windows | Score: 190 | Views: 728995 | Answers: 12

**Solution / Community Answer**:
Tar
Windows 10 includes tar.exe:
# example 1
tar.exe -a -c -f out.zip in.txt
# example 2
tar.exe -x -f out.zip

If you have older Windows, you can still download from
libarchive/libarchive.
PowerShell
PowerShell has Compress-Archive:
# example 1
Compress-Archive in.txt out.zip
# example 2
Expand-Archive out.zip

Directory
For both tools, you can use a file or directory for the input.

**Reference**: https://superuser.com/questions/201371/create-zip-folder-from-the-command-line-windows

> 📎 Source: https://superuser.com/questions/201371/create-zip-folder-from-the-command-line-windows

#### 96. How to run a batch file in a completely hidden way?

**Issue**: How to run a batch file in a completely hidden way?
**Tags / Source**: Tags: windows, command-line, batch-file | superuser | 👍 189 | 💬 20 answers

**Description**:
Tags: windows, command-line, batch-file | Score: 189 | Views: 809378 | Answers: 20

**Solution / Community Answer**:
Solution 1:
Save this one line of text as file invisible.vbs:
CreateObject(&quot;Wscript.Shell&quot;).Run &quot;&quot;&quot;&quot; &amp; WScript.Arguments(0) &amp; &quot;&quot;&quot;&quot;, 0, False

To run any program or batch file invisibly, use it like this:
wscript.exe &quot;C:\Wherever\invisible.vbs&quot; &quot;C:\Some Other Place\MyBatchFile.bat&quot;

To also be able to pass-on/relay a list of arguments use only two double quotes
CreateObject(&quot;Wscript.Shell&quot;).Run &quot;&quot; &amp; WScript.Arguments(0) &amp; &quot;&quot;, 0, False

Example: Invisible.vbs &quot;Kill.vbs ME.exe&quot;
Solution 2:
Use a command line tool to silently launch a process : Quiet, hidecon or hideexec.

**Reference**: https://superuser.com/questions/62525/how-to-run-a-batch-file-in-a-completely-hidden-way

> 📎 Source: https://superuser.com/questions/62525/how-to-run-a-batch-file-in-a-completely-hidden-way

#### 97. Apostrophes and double quotes don&#39;t show up until I type the next letter

**Issue**: Apostrophes and double quotes don&#39;t show up until I type the next letter
**Tags / Source**: Tags: windows, windows-xp, keyboard | superuser | 👍 188 | 💬 12 answers

**Description**:
Tags: windows, windows-xp, keyboard | Score: 188 | Views: 407550 | Answers: 12

**Solution / Community Answer**:
The reason is because you are using US-international keyboard. 

Here is how to change this:


In the Windows run box (Windows+R) type control intl.cpl or control international.
Click the "Keyboards and Languages" tab
Click "Change Keyboards..."
AT THIS POINT MAKE SURE YOU ARE USING "English (United Kingdom) - US" as the default input language, meaning you set the keyboard to US, not US-international

**Reference**: https://superuser.com/questions/122625/apostrophes-and-double-quotes-dont-show-up-until-i-type-the-next-letter

> 📎 Source: https://superuser.com/questions/122625/apostrophes-and-double-quotes-dont-show-up-until-i-type-the-next-letter

#### 98. Why does 64-bit Windows need a separate &quot;Program Files (x86)&quot; folder?

**Issue**: Why does 64-bit Windows need a separate &quot;Program Files (x86)&quot; folder?
**Tags / Source**: Tags: windows, 64-bit | superuser | 👍 184 | 💬 11 answers

**Description**:
Tags: windows, 64-bit | Score: 184 | Views: 106592 | Answers: 11

**Solution / Community Answer**:
Short answer: To ensure legacy 32-bit applications continue to work the same way they used to without imposing ugly rules on 64-bit applications that would create a permanent mess.

It is not necessary. It's just more convenient than other possible solutions such as requiring every application to create its own way to separate 32-bit DLLs and executables  from 64-bit DLLs and executables.

The main reason is to make 32-bit applications that don't even know 64-bit systems exist "just work", even if 64-bit DLLs are installed in places the applications might look. A 32-bit application won't be able to load a 64-bit DLL, so a method was needed to ensure that a 32-bit application (that might pre-date 64-bit systems and thus have no idea 64-bit files even exist) wouldn't find a 64-bit DLL, try to load it, fail, and then generate an error message.

The simplest solution to this is consistently separate directories. Really the only alternative is to require every 64-bit application to "hide" its executable files somewhere a 32-bit application wouldn't look, such as a bin64 directory inside that application. But that would impose permanent ugliness on 64-bit systems just to support legacy applications.

**Reference**: https://superuser.com/questions/442246/why-does-64-bit-windows-need-a-separate-program-files-x86-folder

> 📎 Source: https://superuser.com/questions/442246/why-does-64-bit-windows-need-a-separate-program-files-x86-folder

#### 99. Why does the /winsxs folder grow so large, and can it be made smaller?

**Issue**: Why does the /winsxs folder grow so large, and can it be made smaller?
**Tags / Source**: Tags: windows, disk-space, winsxs | superuser | 👍 183 | 💬 12 answers

**Description**:
Tags: windows, disk-space, winsxs | Score: 183 | Views: 128714 | Answers: 12

**Solution / Community Answer**:
There is a nice command that cleans up after a Windows 7 SP1 installation (it saved me around 3&nbsp;GB):

DISM /online /cleanup-Image /spsuperseded


Must be executed from an elevated command prompt

**Reference**: https://superuser.com/questions/1/why-does-the-winsxs-folder-grow-so-large-and-can-it-be-made-smaller

> 📎 Source: https://superuser.com/questions/1/why-does-the-winsxs-folder-grow-so-large-and-can-it-be-made-smaller

#### 100. What utility can move my Windows boot partition over to another hard drive?

**Issue**: What utility can move my Windows boot partition over to another hard drive?
**Tags / Source**: Tags: windows, hard-drive, boot, backup, partitioning | superuser | 👍 182 | 💬 18 answers

**Description**:
Tags: windows, hard-drive, boot, backup, partitioning | Score: 182 | Views: 440315 | Answers: 18

**Solution / Community Answer**:
DriveImage XML
DriveImage XML will do the job.  It runs from within Windows and it can copy directly from drive to drive.  A lot of people rave about it after good experiences with the software.


DriveImage XML is an easy to use and reliable program for imaging and backing up partitions and logical drives.
Image creation uses Microsoft's Volume Shadow Services (VSS), allowing you to create safe &quot;hot images&quot; even from drives currently in use. Images are stored in XML files, allowing you to process them with 3rd party tools. Never again be stuck with a useless backup! Restore images to drives without having to reboot. DriveImage XML is now faster than ever, offering two different compression levels.


EASEUS Disk Copy
EASEUS Disk Copy is a great alternative if you don't want to go for a 'hot' backup that runs from within Windows.  Good review at lifehacker and on a par with DriveImage XML.  They quite clearly state that it is ideal for moving from one disk to a larger one.  Like other suggestions, this requires that you create a boot CD.

EASEUS Disk Copy is a potent freeware
providing sector-by-sector
disk/partition clone regardless of
your operating system, file systems
and partition scheme by creating a
bootable CD. The sector-by-sector
method assures you a copy 100%
identical to the original. Disk Copy
can be used for copy, cloning, or
upgrading your original small hard
drive to a new larger drive. Simply
speaking, it can copy anything from
the old hard drive including the
deleted, lost files and inaccessible
data. So, the freeware is a perfect
tool for Data Recovery Wizard to
recover files from a backup disk.

**Reference**: https://superuser.com/questions/32164/what-utility-can-move-my-windows-boot-partition-over-to-another-hard-drive

> 📎 Source: https://superuser.com/questions/32164/what-utility-can-move-my-windows-boot-partition-over-to-another-hard-drive



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
