# Windows 常见故障及解决方法 | Windows Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 03:00:27 UTC_

## 中文 🇨🇳
**Windows 常见故障及解决方法**

本页面每小时自动从 Stack Exchange 社区抓取 WINDOWS 平台常见故障及解决方法。

### WINDOWS 常见故障及解决方法

#### 1. Find out which process is locking a file or folder in Windows

**故障现象**: Find out which process is locking a file or folder in Windows
**标签 / 来源**: Tags: windows, filesystems, process, community-faq-proposed | superuser | 👍 1331 | 💬 16 answers

**问题描述**:
Tags: windows, filesystems, process, community-faq-proposed | Score: 1331 | Views: 2068492 | Answers: 16

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
Tags: windows, hard-drive | Score: 1006 | Views: 531717 | Answers: 20

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
Tags: windows-7, windows, command-line, environment-variables | Score: 833 | Views: 3005012 | Answers: 8

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
Tags: windows, filesystems, ntfs, symbolic-link | Score: 609 | Views: 462513 | Answers: 3

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
Tags: windows, command-line, powershell | Score: 603 | Views: 893171 | Answers: 5

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
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 526 | Views: 1498428 | Answers: 11

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
Tags: windows, disk-space | Score: 523 | Views: 870925 | Answers: 10

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
Tags: windows, telnet | Score: 512 | Views: 910605 | Answers: 6

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
Tags: windows, ssh, permissions, openssh, private-key | Score: 498 | Views: 1047404 | Answers: 18

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
Tags: windows, wget, curl | Score: 490 | Views: 1880079 | Answers: 21

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
Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | Score: 486 | Views: 1073378 | Answers: 8

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
Tags: windows, windows-10, microsoft-onedrive | Score: 468 | Views: 1824060 | Answers: 11

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
Tags: windows-10, windows-subsystem-for-linux | Score: 453 | Views: 990460 | Answers: 9

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
Tags: windows, windows-7, symbolic-link | Score: 439 | Views: 575986 | Answers: 13

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
Tags: windows, command-line, unix, cat | Score: 433 | Views: 1180581 | Answers: 4

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
Tags: windows-10, mouse | Score: 399 | Views: 212007 | Answers: 1

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
Tags: windows, windows-10-upgrade | Score: 394 | Views: 552674 | Answers: 14

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
Tags: windows, command-line | Score: 387 | Views: 1322568 | Answers: 15

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
Tags: windows, filesystems, ext4 | Score: 377 | Views: 1033426 | Answers: 12

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
Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | Score: 362 | Views: 684501 | Answers: 12

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
Tags: windows, windows-10, keyboard-layout | Score: 349 | Views: 543256 | Answers: 9

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
Tags: windows, windows-7, virtualbox | Score: 349 | Views: 1389528 | Answers: 7

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
Tags: windows-7, windows, user-interface | Score: 327 | Views: 324991 | Answers: 11

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
Tags: windows, file-management, disk-space, community-faq | Score: 321 | Views: 215817 | Answers: 23

**解决方法 / 社区答案**:
WinDirStat is a port of KDirStat for Linux. It's free, lightweight, small (650kb installer), fast, portable (as a standalone .exe file), and works on multiple versions of Windows. Besides showing folders and percentages (for the entire disk or any subset of folders), it also displays an (optional) graphical usage map. Works well with NTFS Junction folders, avoiding counting folders multiple times.

**参考链接**: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

> 📎 来源 / Source: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

#### 35. Equivalent of cmd&#39;s &quot;where&quot; in powershell

**故障现象**: Equivalent of cmd&#39;s &quot;where&quot; in powershell
**标签 / 来源**: Tags: windows, powershell | superuser | 👍 318 | 💬 6 answers

**问题描述**:
Tags: windows, powershell | Score: 318 | Views: 257705 | Answers: 6

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
Tags: windows, command-line, environment-variables | Score: 317 | Views: 1038783 | Answers: 5

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
Tags: windows, command-line, path, cd | Score: 311 | Views: 1488445 | Answers: 9

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
Tags: windows, multiple-monitors, window-manager | Score: 309 | Views: 728597 | Answers: 24

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
Tags: windows, windows-10 | Score: 305 | Views: 291043 | Answers: 17

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
Tags: windows, notepad++, text-editors | Score: 295 | Views: 247822 | Answers: 6

**解决方法 / 社区答案**:
You can disable the confirmation in the settings:

Settings -&gt; Preferences -&gt; MISC. -&gt; Update silently

**参考链接**: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

> 📎 来源 / Source: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

#### 44. Equivalent of Linux `touch` to create an empty file with PowerShell

**故障现象**: Equivalent of Linux `touch` to create an empty file with PowerShell
**标签 / 来源**: Tags: windows, windows-8, powershell, powershell-3.0 | superuser | 👍 293 | 💬 14 answers

**问题描述**:
Tags: windows, windows-8, powershell, powershell-3.0 | Score: 293 | Views: 420047 | Answers: 14

**解决方法 / 社区答案**:
Using the append redirector ">>" resolves the issue where an existing file is deleted:

echo $null &gt;&gt; filename

**参考链接**: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

> 📎 来源 / Source: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

#### 45. How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?

**故障现象**: How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?
**标签 / 来源**: Tags: windows, windows-10, windows-explorer, windows-10-preview | superuser | 👍 291 | 💬 5 answers

**问题描述**:
Tags: windows, windows-10, windows-explorer, windows-10-preview | Score: 291 | Views: 256077 | Answers: 5

**解决方法 / 社区答案**:
As of build 9926 (at least - it may have been an earlier build), this is configurable via the GUI.

Open Explorer and go to View, then click Options (or Change folder and search options). In General tab you can change Open File Explorer to This PC

**参考链接**: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

> 📎 来源 / Source: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

#### 46. How can I reduce the consumption of the `vmmem` process?

**故障现象**: How can I reduce the consumption of the `vmmem` process?
**标签 / 来源**: Tags: windows-10, memory, docker, resources | superuser | 👍 273 | 💬 15 answers

**问题描述**:
Tags: windows-10, memory, docker, resources | Score: 273 | Views: 569293 | Answers: 15

**解决方法 / 社区答案**:
Daniiel B is on the money. To turn off Vmmem simply go into Powershell or whatever terminal you like to use under admin rights and enter the command wsl --shutdown, when your done with playing in wsl1/2.

**参考链接**: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

> 📎 来源 / Source: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

#### 47. How can I execute a Windows command line in background?

**故障现象**: How can I execute a Windows command line in background?
**标签 / 来源**: Tags: windows, command-line | superuser | 👍 270 | 💬 12 answers

**问题描述**:
Tags: windows, command-line | Score: 270 | Views: 889338 | Answers: 12

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
Tags: windows, cpu, temperature | Score: 267 | Views: 2706355 | Answers: 10

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
Tags: windows, command-line, chocolatey | Score: 267 | Views: 312128 | Answers: 4

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


---

## English 🇺🇸
**Windows Common Issues & Solutions**

Auto-updated hourly from Stack Exchange: common WINDOWS issues and community-verified solutions.

### WINDOWS Common Issues & Solutions

#### 1. Find out which process is locking a file or folder in Windows

**Issue**: Find out which process is locking a file or folder in Windows
**Tags / Source**: Tags: windows, filesystems, process, community-faq-proposed | superuser | 👍 1331 | 💬 16 answers

**Description**:
Tags: windows, filesystems, process, community-faq-proposed | Score: 1331 | Views: 2068492 | Answers: 16

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
Tags: windows, hard-drive | Score: 1006 | Views: 531717 | Answers: 20

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
Tags: windows-7, windows, command-line, environment-variables | Score: 833 | Views: 3005012 | Answers: 8

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
Tags: windows, filesystems, ntfs, symbolic-link | Score: 609 | Views: 462513 | Answers: 3

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
Tags: windows, command-line, powershell | Score: 603 | Views: 893171 | Answers: 5

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
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 526 | Views: 1498428 | Answers: 11

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
Tags: windows, disk-space | Score: 523 | Views: 870925 | Answers: 10

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
Tags: windows, telnet | Score: 512 | Views: 910605 | Answers: 6

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
Tags: windows, ssh, permissions, openssh, private-key | Score: 498 | Views: 1047404 | Answers: 18

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
Tags: windows, wget, curl | Score: 490 | Views: 1880079 | Answers: 21

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
Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | Score: 486 | Views: 1073378 | Answers: 8

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
Tags: windows, windows-10, microsoft-onedrive | Score: 468 | Views: 1824060 | Answers: 11

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
Tags: windows-10, windows-subsystem-for-linux | Score: 453 | Views: 990460 | Answers: 9

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
Tags: windows, windows-7, symbolic-link | Score: 439 | Views: 575986 | Answers: 13

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
Tags: windows, command-line, unix, cat | Score: 433 | Views: 1180581 | Answers: 4

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
Tags: windows-10, mouse | Score: 399 | Views: 212007 | Answers: 1

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
Tags: windows, windows-10-upgrade | Score: 394 | Views: 552674 | Answers: 14

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
Tags: windows, command-line | Score: 387 | Views: 1322568 | Answers: 15

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
Tags: windows, filesystems, ext4 | Score: 377 | Views: 1033426 | Answers: 12

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
Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | Score: 362 | Views: 684501 | Answers: 12

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
Tags: windows, windows-10, keyboard-layout | Score: 349 | Views: 543256 | Answers: 9

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
Tags: windows, windows-7, virtualbox | Score: 349 | Views: 1389528 | Answers: 7

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
Tags: windows-7, windows, user-interface | Score: 327 | Views: 324991 | Answers: 11

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
Tags: windows, file-management, disk-space, community-faq | Score: 321 | Views: 215817 | Answers: 23

**Solution / Community Answer**:
WinDirStat is a port of KDirStat for Linux. It's free, lightweight, small (650kb installer), fast, portable (as a standalone .exe file), and works on multiple versions of Windows. Besides showing folders and percentages (for the entire disk or any subset of folders), it also displays an (optional) graphical usage map. Works well with NTFS Junction folders, avoiding counting folders multiple times.

**Reference**: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

> 📎 Source: https://superuser.com/questions/8248/how-can-i-visualize-the-file-system-usage-on-windows

#### 35. Equivalent of cmd&#39;s &quot;where&quot; in powershell

**Issue**: Equivalent of cmd&#39;s &quot;where&quot; in powershell
**Tags / Source**: Tags: windows, powershell | superuser | 👍 318 | 💬 6 answers

**Description**:
Tags: windows, powershell | Score: 318 | Views: 257705 | Answers: 6

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
Tags: windows, command-line, environment-variables | Score: 317 | Views: 1038783 | Answers: 5

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
Tags: windows, command-line, path, cd | Score: 311 | Views: 1488445 | Answers: 9

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
Tags: windows, multiple-monitors, window-manager | Score: 309 | Views: 728597 | Answers: 24

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
Tags: windows, windows-10 | Score: 305 | Views: 291043 | Answers: 17

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
Tags: windows, notepad++, text-editors | Score: 295 | Views: 247822 | Answers: 6

**Solution / Community Answer**:
You can disable the confirmation in the settings:

Settings -&gt; Preferences -&gt; MISC. -&gt; Update silently

**Reference**: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

> 📎 Source: https://superuser.com/questions/274961/how-to-automatically-reload-modified-files-in-notepad

#### 44. Equivalent of Linux `touch` to create an empty file with PowerShell

**Issue**: Equivalent of Linux `touch` to create an empty file with PowerShell
**Tags / Source**: Tags: windows, windows-8, powershell, powershell-3.0 | superuser | 👍 293 | 💬 14 answers

**Description**:
Tags: windows, windows-8, powershell, powershell-3.0 | Score: 293 | Views: 420047 | Answers: 14

**Solution / Community Answer**:
Using the append redirector ">>" resolves the issue where an existing file is deleted:

echo $null &gt;&gt; filename

**Reference**: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

> 📎 Source: https://superuser.com/questions/502374/equivalent-of-linux-touch-to-create-an-empty-file-with-powershell

#### 45. How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?

**Issue**: How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?
**Tags / Source**: Tags: windows, windows-10, windows-explorer, windows-10-preview | superuser | 👍 291 | 💬 5 answers

**Description**:
Tags: windows, windows-10, windows-explorer, windows-10-preview | Score: 291 | Views: 256077 | Answers: 5

**Solution / Community Answer**:
As of build 9926 (at least - it may have been an earlier build), this is configurable via the GUI.

Open Explorer and go to View, then click Options (or Change folder and search options). In General tab you can change Open File Explorer to This PC

**Reference**: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

> 📎 Source: https://superuser.com/questions/819521/how-do-i-make-windows-10s-file-explorer-open-this-pc-by-default

#### 46. How can I reduce the consumption of the `vmmem` process?

**Issue**: How can I reduce the consumption of the `vmmem` process?
**Tags / Source**: Tags: windows-10, memory, docker, resources | superuser | 👍 273 | 💬 15 answers

**Description**:
Tags: windows-10, memory, docker, resources | Score: 273 | Views: 569293 | Answers: 15

**Solution / Community Answer**:
Daniiel B is on the money. To turn off Vmmem simply go into Powershell or whatever terminal you like to use under admin rights and enter the command wsl --shutdown, when your done with playing in wsl1/2.

**Reference**: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

> 📎 Source: https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process

#### 47. How can I execute a Windows command line in background?

**Issue**: How can I execute a Windows command line in background?
**Tags / Source**: Tags: windows, command-line | superuser | 👍 270 | 💬 12 answers

**Description**:
Tags: windows, command-line | Score: 270 | Views: 889338 | Answers: 12

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
Tags: windows, cpu, temperature | Score: 267 | Views: 2706355 | Answers: 10

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
Tags: windows, command-line, chocolatey | Score: 267 | Views: 312128 | Answers: 4

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



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
