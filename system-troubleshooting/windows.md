# Windows 系统故障知识库 | Windows Troubleshooting

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 316**

> 技术细节（问题描述、解决方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, solutions) remain in original language for accuracy; structural text is bilingual.

---

#### 1. Find out which process is locking a file or folder in Windows

**问题描述 / Problem Description**:
Tags: windows, filesystems, process, community-faq-proposed | Score: 1331 | Views: 2068492 | Answers: 16

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 2. What are the Windows A: and B: drives used for?

**问题描述 / Problem Description**:
Tags: windows, hard-drive | Score: 1006 | Views: 531717 | Answers: 20

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 3. How can I display the contents of an environment variable from the command prompt in Windows 7?

**问题描述 / Problem Description**:
Tags: windows-7, windows, command-line, environment-variables | Score: 833 | Views: 3005012 | Answers: 8

**解决方案 / Solution**:
In Windows Command-Prompt the syntax is echo %PATH%
To get a list of all environment variables enter the command set without any parameters.
To send those variables to a text file enter the command set &gt; filename.txt

Related

How to list global environment variables separately from user-specific environment variables?

**参考链接 / References**:
- N/A

---

#### 4. How to *disable* automatic reboots in Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, windows-update, reboot | Score: 676 | Views: 402626 | Answers: 20

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 5. &quot;directory junction&quot; vs &quot;directory symbolic link&quot;?

**问题描述 / Problem Description**:
Tags: windows, filesystems, ntfs, symbolic-link | Score: 609 | Views: 462513 | Answers: 3

**解决方案 / Solution**:
A junction is definitely not the same thing as a directory symbolic link, although they behave similarly.  The main difference is that, if you are looking at a remote server, junctions are processed at the server and directory symbolic links are processed at the client.  Also see Matthew's comment on the fact that this means symbolic links on the local file system can point to remote file systems.

Suppose that on a machine named Alice you were to put a junction point c:\myjp and a directory symbolic link c:\mysymlink, both pointing to c:\targetfolder.  While you're using Alice you won't notice much difference between them.  But if you're using another machine named Bob, then the junction point

\\Alice\c$\myjp will point to \\Alice\c$\targetfolder

but the symbolic link

\\Alice\c$\mysymlink will point to \\Bob\c$\targetfolder

(Caveat: by default, the system doesn't follow symlinks on remote volumes, so in most cases the second example will actually result in either "File Not Found" or "The symbolic link cannot be followed because its type is disabled.")

The difference between a directory symbolic link and a file symbolic link is simply that one represents a directory and one represents a file.  Since the target of the link doesn't need to exist when the link is created, the file system needs to know whether to tell applications that it is a directory or not.

It should also be noted that creating a symbolic link requires special privilege (by default, only available to elevated processes) whereas creating a junction only requires access to the file system.

**参考链接 / References**:
- N/A

---

#### 6. How do I run multiple commands on one line in PowerShell?

**问题描述 / Problem Description**:
Tags: windows, command-line, powershell | Score: 603 | Views: 893171 | Answers: 5

**解决方案 / Solution**:
Use a semicolon to chain commands in PowerShell:

ipconfig /release; ipconfig /renew

**参考链接 / References**:
- N/A

---

#### 7. Windows 7 SP1 Windows Update stuck checking for updates

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-update | Score: 561 | Views: 3337928 | Answers: 13

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 8. What is the home directory on Windows Subsystem for Linux?

**问题描述 / Problem Description**:
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 526 | Views: 1498428 | Answers: 11

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 9. Can I delete the folder C:\ProgramData\Package Cache\?

**问题描述 / Problem Description**:
Tags: windows, disk-space | Score: 523 | Views: 870925 | Answers: 10

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 10. How to check if a binary is 32- or 64-bit on Windows?

**问题描述 / Problem Description**:
Tags: windows, binary-files, 32-vs-64-bit | Score: 522 | Views: 509026 | Answers: 32

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 11. Create/rename a file/folder that begins with a dot in Windows?

**问题描述 / Problem Description**:
Tags: windows | Score: 520 | Views: 316540 | Answers: 12

**解决方案 / Solution**:
To create/rename on windows explorer, just rename to .name. - The additional dot at the end is necessary, and will be removed by Windows Explorer.

To create a new file begins with a dot, on command prompt:

echo testing &gt; .name

**参考链接 / References**:
- N/A

---

#### 12. Is there any &#39;sudo&#39; command for Windows?

**问题描述 / Problem Description**:
Tags: windows, command-line, privileges | Score: 518 | Views: 916657 | Answers: 19

**解决方案 / Solution**:
The runas command.

runas [{/profile|/noprofile}] [/env] [/netonly] [/smartcard] [/showtrustlevels] [/trustlevel] /user:UserAccountName program


Just run:

runas /noprofile /user:Administrator cmd 


to start a command shell as a administrator

**参考链接 / References**:
- N/A

---

#### 13. How do I exit telnet?

**问题描述 / Problem Description**:
Tags: windows, telnet | Score: 512 | Views: 910605 | Answers: 6

**解决方案 / Solution**:
It should have printed something along the lines of:

Escape character is '^]'.


Since ^X is  CtrlX, try Ctrl] for ^]. 

You should then enter the telnet console, where you can enter quit to leave telnet.

**参考链接 / References**:
- N/A

---

#### 14. Windows SSH: Permissions for &#39;private-key&#39; are too open

**问题描述 / Problem Description**:
Tags: windows, ssh, permissions, openssh, private-key | Score: 498 | Views: 1047404 | Answers: 18

**解决方案 / Solution**:
You locate the file in Windows Explorer, right-click on it then select "Properties". Navigate to the "Security" tab and click "Advanced".

Change the owner to you, disable inheritance and delete all permissions. Then grant yourself "Full control" and save the permissions. Now SSH won't complain about file permission too open anymore.

It should end up looking like this:

**参考链接 / References**:
- N/A

---

#### 15. How to download files from command line in Windows like wget or curl

**问题描述 / Problem Description**:
Tags: windows, wget, curl | Score: 490 | Views: 1880079 | Answers: 21

**解决方案 / Solution**:
An alternative I discovered recently, using PowerShell:

$client = new-object System.Net.WebClient
$client.DownloadFile("http://www.xyz.net/file.txt","C:\tmp\file.txt")


It works as well with GET queries.

If you need to specify credentials to download the file, add the following line in between:

$client.Credentials =  Get-Credential                


A standard windows credentials prompt will pop up. The credentials you enter there will be used to download the file. You only need to do this once for all the time you will be using the $client object.

**参考链接 / References**:
- N/A

---

#### 16. How can I free up drive space from the Windows installer folder without killing Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-10, windows-8.1, disk-space, windows-installer | Score: 486 | Views: 1073378 | Answers: 8

**解决方案 / Solution**:
I created "PatchCleaner" to clean the windows installer directory of all orphaned files in one easy click. If you don't trust the app to do the right thing, use the move feature to put them somewhere safe in case you need them back in the future. I have run it on multiple machines and saved up to 15Gb of space :-)

Run PatchCleaner after windows updates to find newly orphaned files.

I recommend you use the Move action, and move the orphaned patches to external storage, just to be safe

PatchCleaner @ HomeDev

Known Issues (full details on website)


Adobe Reader can fail to update after running PatchCleaner.


NOTE: as @ Feb-2016 version 1.4.1.0 is out that has a fix to allow customisable filters to exclude adobe reader from being incorrectly detected.

**参考链接 / References**:
- N/A

---

#### 17. How can I remove malicious spyware, malware, adware, viruses, trojans or rootkits from my PC?

**问题描述 / Problem Description**:
Tags: windows, anti-virus, virus, malware, community-faq | Score: 474 | Views: 333616 | Answers: 18

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 18. How to rename the User folder in Windows 10?

**问题描述 / Problem Description**:
Tags: windows, windows-10, microsoft-onedrive | Score: 468 | Views: 1824060 | Answers: 11

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 19. Rebooting Ubuntu on Windows without rebooting Windows?

**问题描述 / Problem Description**:
Tags: windows-10, windows-subsystem-for-linux | Score: 453 | Views: 990460 | Answers: 9

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 20. How can I delete a symbolic link in Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-7, symbolic-link | Score: 439 | Views: 575986 | Answers: 13

**解决方案 / Solution**:
Be very careful.
If you have a symbolic link that is a directory (made with mklink /d) then using del will delete all of the files in the target directory (the directory that the link points to), rather than just the link.
SOLUTION: rmdir on the other hand will only delete the directory link, not what the link points to.

**参考链接 / References**:
- N/A

---

#### 21. How to delete directories with path/names too long for normal delete

**问题描述 / Problem Description**:
Tags: windows, file-management | Score: 433 | Views: 568440 | Answers: 25

**解决方案 / Solution**:
Use the 7-Zip File Manager to delete them.  

If you are still having trouble, ensure that you utilize Shift+Delete inside the 7-Zip File Manager. Otherwise, Windows tries to move them to the Recycle Bin (which will fail again).

**参考链接 / References**:
- N/A

---

#### 22. What is the Windows equivalent of the Unix command cat?

**问题描述 / Problem Description**:
Tags: windows, command-line, unix, cat | Score: 433 | Views: 1180581 | Answers: 4

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 23. Mouse pointer moving on arrow keys pressed in Windows?

**问题描述 / Problem Description**:
Tags: windows-10, mouse | Score: 399 | Views: 212007 | Answers: 1

**解决方案 / Solution**:
Tried killing all running processes on my PC till the problem went away and I can now say for sure the culprit was...
Microsoft Paint
(classic Win32 one)
Apparently it's got a feature that allows moving the mouse pointer using arrow keys, and for some reason sometimes it doesn't stop listening when the window loses focus, so Paint was running in the background since I often use it and it was still doing its job of moving the mouse.
This also explains why the problem can persist after a reboot: when you reboot Windows while Paint is running, Windows will automatically &quot;save your work&quot; and reopen Paint at system boot, causing the bug again!

**参考链接 / References**:
- N/A

---

#### 24. How to disable the &quot;Get Windows 10&quot; icon shown in the notification area (tray)?

**问题描述 / Problem Description**:
Tags: windows, windows-10-upgrade | Score: 394 | Views: 552674 | Answers: 14

**解决方案 / Solution**:
If you just want to remove the tray icon until the next restart you can terminate the GWX.exe process using Task Manager.
To get rid of the icon permanently, uninstall KB3035583 which is responsible for these notifications:
Control panel, windows update, installed updates, sort by name, &quot;Update for Microsoft Windows KB3035583&quot; (not a Security Update), uninstall, reboot.
(Alternative: open CMD and enter wusa /uninstall /KB:3035583)
When you're offered the same again via Windows Update remember to hide it.
After uninstalling, if remnants of the update's files are still in Windows\System32\GWX, just delete that directory, although first you may need to take ownership of it.

**参考链接 / References**:
- N/A

---

#### 25. How do you list all processes on the command line in Windows?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 387 | Views: 1322568 | Answers: 15

**解决方案 / Solution**:
Working with cmd.exe:

tasklist

If you have Powershell:

get-process

Via WMI:

wmic process

(you can query remote machines as well with /node:ComputerOrIP, and there are a LOT more ways to customize this command: link)

**参考链接 / References**:
- N/A

---

#### 26. How to recursively delete directory from command line in windows?

**问题描述 / Problem Description**:
Tags: windows, command-line, cmd.exe | Score: 385 | Views: 958891 | Answers: 8

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 27. How to read ext4 partitions on Windows?

**问题描述 / Problem Description**:
Tags: windows, filesystems, ext4 | Score: 377 | Views: 1033426 | Answers: 12

**解决方案 / Solution**:
Ext2Read works well. It can also open &amp; read disk images ( eg: Wubi disk images)


  Ext2Read is an explorer like utility
  to explore ext2/ext3/ext4 files. It
  now supports LVM2 and EXT4 extents. It
  can be used to view and copy files and
  folders. It can recursively copy
  entire folders. It can also be used to
  view and copy disk and file

**参考链接 / References**:
- N/A

---

#### 28. Native alternative to wget in Windows PowerShell?

**问题描述 / Problem Description**:
Tags: windows, powershell, powershell-2.0, powershell-3.0, powershell-4.0 | Score: 362 | Views: 684501 | Answers: 12

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 29. Keyboard language keeps changing in Windows 10

**问题描述 / Problem Description**:
Tags: windows, windows-10, keyboard-layout | Score: 349 | Views: 543256 | Answers: 9

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 30. Why does virtualbox only have 32-bit option, no 64-bit option on Windows 7?

**问题描述 / Problem Description**:
Tags: windows, windows-7, virtualbox | Score: 349 | Views: 1389528 | Answers: 7

**解决方案 / Solution**:
Take a look: http://www.fixedbyvonnie.com/2014/11/virtualbox-showing-32-bit-guest-versions-64-bit-host-os/

If VirtualBox is only showing 32-bit versions in the Version list make sure:


You have an x64 CPU installed. (Optimally, a 64-bit OS should also be installed to receive acceptable virtualization performance.)
Hardware virtualization is enabled in the BIOS. (Your CPU must support it.)


For Intel x64: VT-x (Intel Virtualization Technology) and VT-d are both enabled
For AMD x64: AMD SVM (Secure Virtual Machine) is enabled

Hyper-V (or any other form of bare-metal hypervisor) is not installed

**参考链接 / References**:
- N/A

---

#### 31. How to pin either a Shortcut or a Batch file to the new Windows 7, 8 and 10 Taskbar and start menu?

**问题描述 / Problem Description**:
Tags: windows-7, windows-8, windows-10, taskbar, shortcuts | Score: 344 | Views: 286084 | Answers: 7

**解决方案 / Solution**:
Create a shortcut to your batch file.
Get into shortcut property and change target to something like: cmd.exe /C "path-to-your-batch".
Simply drag your new shortcut to the taskbar. It should now be pinnable.

**参考链接 / References**:
- N/A

---

#### 32. Conclusively stop wake timers from waking Windows 10 desktop

**问题描述 / Problem Description**:
Tags: windows-10, sleep, wake-on-lan | Score: 331 | Views: 181507 | Answers: 3

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 33. Menu select item stuck on screen after context or command menu has closed

**问题描述 / Problem Description**:
Tags: windows-7, windows, user-interface | Score: 327 | Views: 324991 | Answers: 11

**解决方案 / Solution**:
The problem was introduced back in Windows 2000 when fading menu items were added. Originally, the feature was added in kernel-mode code and was tightly integrated into portions of the UI. Since it worked so well, it ended up staying there. The problem has appeared from time to time, but no one has had a reliable way to reproduce it in the kernel debugger to get it fixed.

The same effect can be achieved without changing the screen resolution or color depth.  Go to Start -> Run -> and type tskill dwm.  This command will reset the desktop window manager without the need to change the screen resolution.  

Changing the screen resolution or color depth also resets the desktop window manager, so it's always been a workaround for the bug when it appears. Either of these solutions will fix the problem.

**参考链接 / References**:
- N/A

---

#### 34. How can I visualize the file system usage on Windows?

**问题描述 / Problem Description**:
Tags: windows, file-management, disk-space, community-faq | Score: 321 | Views: 215817 | Answers: 23

**解决方案 / Solution**:
WinDirStat is a port of KDirStat for Linux. It's free, lightweight, small (650kb installer), fast, portable (as a standalone .exe file), and works on multiple versions of Windows. Besides showing folders and percentages (for the entire disk or any subset of folders), it also displays an (optional) graphical usage map. Works well with NTFS Junction folders, avoiding counting folders multiple times.

**参考链接 / References**:
- N/A

---

#### 35. Equivalent of cmd&#39;s &quot;where&quot; in powershell

**问题描述 / Problem Description**:
Tags: windows, powershell | Score: 318 | Views: 257705 | Answers: 6

**解决方案 / Solution**:
Use the Get-Command commandlet passing it the name of the executable. It populates the Path property of the returned object (of type ApplicationInfo) with the fully resolved path to the executable. 

# ~&gt; (get-command notepad.exe).Path
C:\WINDOWS\system32\notepad.exe

**参考链接 / References**:
- N/A

---

#### 36. Setting and getting Windows environment variables from the command prompt?

**问题描述 / Problem Description**:
Tags: windows, command-line, environment-variables | Score: 317 | Views: 1038783 | Answers: 5

**解决方案 / Solution**:
To make the environment variable accessible globally you need to set it in the registry. As you've realised by just using:


  set NEWVAR=SOMETHING


you are just setting it in the current process space.

According to this page you can use the setx command:


  setx NEWVAR SOMETHING


setx is built into Windows 7, but for older versions may only be available if you install the Windows Resource Kit

**参考链接 / References**:
- N/A

---

#### 37. Is there a list of Windows special directories/shortcuts (like %TEMP%)?

**问题描述 / Problem Description**:
Tags: windows, shortcuts, environment-variables, special-locations | Score: 314 | Views: 344813 | Answers: 6

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 38. Can I completely disable Cortana on Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, cortana | Score: 314 | Views: 1744192 | Answers: 9

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 39. Using cd command in Windows command line, can&#39;t navigate to D:\

**问题描述 / Problem Description**:
Tags: windows, command-line, path, cd | Score: 311 | Views: 1488445 | Answers: 9

**解决方案 / Solution**:
Going back to the days of DOS, there's a separate "current directory" for each drive.  cd D:\foldername changes D:'s current directory to the foldername specified, but does not change the fact that you're still working on the C: drive.

What you want is simple:

D:


Here you can see how the "separate current directory for each drive" thing works:

C:\Users\coneslayer&gt;e:

E:\&gt;c:

C:\Users\coneslayer&gt;cd e:\software

C:\Users\coneslayer&gt;e:

e:\Software&gt;

**参考链接 / References**:
- N/A

---

#### 40. How to move windows that open up offscreen?

**问题描述 / Problem Description**:
Tags: windows, multiple-monitors, window-manager | Score: 309 | Views: 728597 | Answers: 24

**解决方案 / Solution**:
I use this approach:


Use Alt+Tab to switch to the off-screen application.
Press Alt+SPACE to bring up the system menu (you won't see it because it is off screen)
Press R to select the "Restore" menu choice to ensure the windows isn't maximized (you cannot move it if it is maximized)
Press Alt+SPACE again, then M to select the "Move" menu choice.
Press one of the arrow keys to initiate the movement.
Now just use the mouse  to place the window where you want.


If you are using a non-English version of Windows, the "R" and "M" menu choices will probably be different.

**参考链接 / References**:
- N/A

---

#### 41. How to quickly move current window to another Task View / desktop in Windows 10?

**问题描述 / Problem Description**:
Tags: windows, windows-10 | Score: 305 | Views: 291043 | Answers: 17

**解决方案 / Solution**:
I think for a quicker switch this should be in the titlebar, so I created a tool for that:

https://github.com/Eun/MoveToDesktop



You can also move windows by using WIN+ALT+Left/Right or change the shortcut as needed.

**参考链接 / References**:
- N/A

---

#### 42. How to mess up a PC running Windows 7?

**问题描述 / Problem Description**:
Tags: windows-7, windows, security | Score: 303 | Views: 118517 | Answers: 27

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 43. How to automatically reload modified files in Notepad++

**问题描述 / Problem Description**:
Tags: windows, notepad++, text-editors | Score: 295 | Views: 247822 | Answers: 6

**解决方案 / Solution**:
You can disable the confirmation in the settings:

Settings -&gt; Preferences -&gt; MISC. -&gt; Update silently

**参考链接 / References**:
- N/A

---

#### 44. Equivalent of Linux `touch` to create an empty file with PowerShell

**问题描述 / Problem Description**:
Tags: windows, windows-8, powershell, powershell-3.0 | Score: 293 | Views: 420047 | Answers: 14

**解决方案 / Solution**:
Using the append redirector ">>" resolves the issue where an existing file is deleted:

echo $null &gt;&gt; filename

**参考链接 / References**:
- N/A

---

#### 45. How do I make Windows 10&#39;s File Explorer open &quot;This PC&quot; by default?

**问题描述 / Problem Description**:
Tags: windows, windows-10, windows-explorer, windows-10-preview | Score: 291 | Views: 256077 | Answers: 5

**解决方案 / Solution**:
As of build 9926 (at least - it may have been an earlier build), this is configurable via the GUI.

Open Explorer and go to View, then click Options (or Change folder and search options). In General tab you can change Open File Explorer to This PC

**参考链接 / References**:
- N/A

---

#### 46. How can I reduce the consumption of the `vmmem` process?

**问题描述 / Problem Description**:
Tags: windows-10, memory, docker, resources | Score: 273 | Views: 569293 | Answers: 15

**解决方案 / Solution**:
Daniiel B is on the money. To turn off Vmmem simply go into Powershell or whatever terminal you like to use under admin rights and enter the command wsl --shutdown, when your done with playing in wsl1/2.

**参考链接 / References**:
- N/A

---

#### 47. How can I execute a Windows command line in background?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 270 | Views: 889338 | Answers: 12

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 48. How do I change the language of all Powerpoint slides at once?

**问题描述 / Problem Description**:
Tags: windows, microsoft-office, microsoft-powerpoint, language, microsoft-powerpoint-2010 | Score: 268 | Views: 572691 | Answers: 9

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 49. How can I check the temperature of my CPU in Windows?

**问题描述 / Problem Description**:
Tags: windows, cpu, temperature | Score: 267 | Views: 2706355 | Answers: 10

**解决方案 / Solution**:
Actually this information is given to OS by the BIOS, but you will need an application to expose the information. You can find a lot of applications to do this:

Realtemp
CPU thermomether
Core Temp

**参考链接 / References**:
- N/A

---

#### 50. How to list Chocolatey packages already installed and newer version available from the command line

**问题描述 / Problem Description**:
Tags: windows, command-line, chocolatey | Score: 267 | Views: 312128 | Answers: 4

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 51. Why is Google so much faster than a hard-drive search?

**问题描述 / Problem Description**:
Tags: windows, hard-drive, windows-search, google-search | Score: 265 | Views: 43966 | Answers: 10

**解决方案 / Solution**:
Google is not searching the internet: it is searching an index. Google has huge server farms which are constantly scanning and indexing the internet. This process takes a lot of time, just like the search of your unindexed hard drive. In Windows 7, there is an option to index your hard drives. This process takes some time at first but once it is up and running the results of a search will be instantaneous.

If you want to know more about how the Google search works you can read Google's article "How Search Works" or read the article "How Stuff Works: How Google Works".

**参考链接 / References**:
- N/A

---

#### 52. Windows equivalent of whereis?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 259 | Views: 243680 | Answers: 11

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 53. Windows equivalent of the Linux command &#39;touch&#39;?

**问题描述 / Problem Description**:
Tags: windows, file-attributes, touch | Score: 257 | Views: 532320 | Answers: 32

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 54. How to search inside files on Windows 7?

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-search, file-filter | Score: 255 | Views: 833086 | Answers: 13

**解决方案 / Solution**:
To get to the Indexing Options:  

Start --> Control Panel --> Indexing Options 

See Change advanced indexing options for more information.

If you click on the Advanced button in Indexing Options and go to the File Types tab, you will get a list of file types and the way they are indexed. For the file types you want, you can specify that you want the file contents indexed, and not just the file properties.

Or you can just do a normal search, and after the search is finished you can click on the "File Contents" button under the "Search again in" field (which is located after the end of the search results list, if you scroll to the bottom).

Based on this page, the "File Contents" option won't always show up - only when the folder being searched is not marked for file content indexing; in that case, file contents are supposedly searched automatically, without having to specify this option explicitly.

**参考链接 / References**:
- N/A

---

#### 55. Refresh Icon Cache Without Rebooting

**问题描述 / Problem Description**:
Tags: windows, windows-explorer, icons, cache | Score: 251 | Views: 408444 | Answers: 13

**解决方案 / Solution**:
Yes.

You can just run the following command to clear the icon cache:

ie4uinit.exe -ClearIconCache


For Windows 10, use:

ie4uinit.exe -show




Check this video for a demo.

[tip credit]

**参考链接 / References**:
- N/A

---

#### 56. Kill a process which says &quot;Access denied&quot;

**问题描述 / Problem Description**:
Tags: windows-7, windows, 64-bit | Score: 251 | Views: 1111843 | Answers: 11

**解决方案 / Solution**:
Kill a protected process?

http://processhacker.sourceforge.net/index.php

Works on Windows Server without admin rights! Yammie! :)

**参考链接 / References**:
- N/A

---

#### 57. Troubleshoot High CPU usage by the &quot;System&quot; process

**问题描述 / Problem Description**:
Tags: windows, windows-8, performance, troubleshooting, cpu-usage | Score: 243 | Views: 753727 | Answers: 6

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 58. How do I set system environment variables in Windows 10?

**问题描述 / Problem Description**:
Tags: windows, windows-10 | Score: 239 | Views: 1539780 | Answers: 9

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 59. How to supress &quot;Terminate batch job (Y/N)&quot; confirmation?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch | Score: 236 | Views: 199305 | Answers: 21

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 60. How to compare the differences between two PDF files on Windows?

**问题描述 / Problem Description**:
Tags: windows, pdf, file-comparison | Score: 234 | Views: 484912 | Answers: 19

**解决方案 / Solution**:
On Linux and Windows you can use diffpdf (which differs from diff-pdf mentioned in this thread).

On Ubuntu install using:
sudo apt-get install diffpdf

See further this UbuntuGeek page on comparing pds textually or visually.
For Windows, this Diffpdf Windows version works really great. You can download from http://soft.rubypdf.com/software/diffpdf (scroll down to Win32 static version).
You can also install it on Windows in an automated manner via the https://scoop.sh/ package manager - install the package manager first per instructions on the homepage and then:
scoop bucket add extras
scoop install extras/diffpdf

This does not require administrator privileges on your account, so it can be installed on externally managed systems (e.g. work computers).

**参考链接 / References**:
- N/A

---

#### 61. How to make SUBST mapping persistent across reboots?

**问题描述 / Problem Description**:
Tags: windows, subst | Score: 232 | Views: 287015 | Answers: 11

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 62. PowerShell equivalent to the Unix `which` command?

**问题描述 / Problem Description**:
Tags: windows, unix, powershell, which | Score: 231 | Views: 192989 | Answers: 11

**解决方案 / Solution**:
This was asked and answered on Stack Overflow: Equivalent of *Nix 'which' command in PowerShell?


  The very first alias I made once I started customizing my profile in PowerShell was 'which'.
  
  New-Alias which get-command
  
  To add this to your profile, type this:
  
  "`nNew-Alias which get-command" | add-content $profile
  
  The `n at the start of the last line is to ensure it will start as a new line.

**参考链接 / References**:
- N/A

---

#### 63. Browse an UNC path using Windows CMD without mapping it to a network drive

**问题描述 / Problem Description**:
Tags: windows, command-line, network-drive, unc | Score: 230 | Views: 521023 | Answers: 8

**解决方案 / Solution**:
If you use pushd and popd instead of cd you won't get that UNC error.
pushd &lt;UNC path&gt; will create a temporary virtual drive and get into it.
popd will delete the temporary drive and get you back to the path you were when you entered pushd.
Example:
C:\a\local\path&gt; pushd \\network_host\a\network\path

U:\a\network\path&gt; REM a temporary U: virtual drive has been created

U:\a\network\path&gt; popd

C:\a\local\path&gt; REM the U: drive has been deleted

C:\a\local\path&gt;

**参考链接 / References**:
- N/A

---

#### 64. How do I know what proxy server I&#39;m using?

**问题描述 / Problem Description**:
Tags: windows, windows-xp, networking, proxy | Score: 229 | Views: 1026134 | Answers: 15

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 65. PowerShell equivalent of curl

**问题描述 / Problem Description**:
Tags: windows, powershell, curl | Score: 229 | Views: 723773 | Answers: 9

**解决方案 / Solution**:
PowerShell 3.0 has the new command Invoke-RestMethod:

http://technet.microsoft.com/en-us/library/hh849971.aspx

more detail:  

https://discoposse.com/2012/06/30/powershell-invoke-restmethod-putting-the-curl-in-your-shell/

**参考链接 / References**:
- N/A

---

#### 66. Typing “python” on Windows 10 (version 1903) command prompt opens Microsoft store

**问题描述 / Problem Description**:
Tags: windows-10, command-line, python, cmd.exe, unattended | Score: 229 | Views: 175078 | Answers: 8

**解决方案 / Solution**:
Fixed it by removing it automatically on the settings page.  Under Apps and Features, there are an application execution aliases.

I am running the latest 1903 update.

**参考链接 / References**:
- N/A

---

#### 67. Windows 10 - disable reopening programs after restart/startup

**问题描述 / Problem Description**:
Tags: windows, windows-10, boot | Score: 228 | Views: 347803 | Answers: 7

**解决方案 / Solution**:
Good news! It has been somewhat &quot;fixed.&quot;
I was interested in clickbangdead's solution, but unfortunately I could not make it work no matter what I tried. Then I went back to the Microsoft Answers thread where he originally posted his solution, because maybe someone could have found a new solution in the subsequent pages. And voilà, indeed. Navigate to the following location:
Settings &gt; Accounts &gt; Sign-In Options
Scroll down to Privacy on the right and then set the following to Off:

Use my sign-in info to automatically finish setting up my device after an update or restart.


I was skeptical, because that doesn't seem like it has much to do with reopening my Google Chrome upon restart, but I tested and it (finally) works!

Update:  with the release of Windows 10 version 1803 (the April 2018 Update), Microsoft modified the wording within that Privacy option to emphasize that it will &quot;reopen my apps&quot; if it is configured to be On.

Use my sign-in info to automatically finish setting up my device and reopen my apps after an update or restart.

**参考链接 / References**:
- N/A

---

#### 68. Change default code page of Windows console to UTF-8

**问题描述 / Problem Description**:
Tags: windows-7, windows, encoding, console | Score: 226 | Views: 563116 | Answers: 9

**解决方案 / Solution**:
To change the codepage for the console only, do the following:

Start -&gt; Run -&gt; regedit
Go to [HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\Autorun]
Change the value to @chcp 65001&gt;nul

If Autorun is not present, you can add a New String

**参考链接 / References**:
- N/A

---

#### 69. How to prevent Windows 10 from automatically adding keyboard layouts (i.e. US keyboard)

**问题描述 / Problem Description**:
Tags: windows, windows-10, keyboard, language, input-languages | Score: 223 | Views: 268606 | Answers: 12

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 70. Disable &quot;These files might be harmful to your computer&quot; warning?

**问题描述 / Problem Description**:
Tags: windows, networking, windows-explorer | Score: 223 | Views: 365744 | Answers: 14

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 71. What are CLOSE_WAIT and TIME_WAIT states?

**问题描述 / Problem Description**:
Tags: windows, networking, port, tcpip | Score: 221 | Views: 610666 | Answers: 3

**解决方案 / Solution**:
Due to the way TCP/IP works, connections can not be closed immediately.  Packets may arrive out of order or be retransmitted after the connection has been closed.

CLOSE_WAIT indicates that the remote endpoint (other side of the connection) has closed the connection.
TIME_WAIT indicates that local endpoint (this side) has closed the connection.

The connection is being kept around so that any delayed packets can be matched to the connection and handled appropriately.  The connections will be removed when they time out within four minutes. See http://en.wikipedia.org/wiki/Transmission_Control_Protocol for more details.

**参考链接 / References**:
- N/A

---

#### 72. Preventing applications from stealing focus

**问题描述 / Problem Description**:
Tags: windows, window-focus | Score: 220 | Views: 130694 | Answers: 7

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 73. Why are there directories called Local, LocalLow, and Roaming under \Users\&lt;username&gt;\AppData?

**问题描述 / Problem Description**:
Tags: windows, thunderbird, user-profiles | Score: 213 | Views: 134967 | Answers: 3

**解决方案 / Solution**:
Roaming is the folder that would be synchronized with a server if you logged into a domain with a roaming profile (enabling you to log into any computer in a domain and access your favorites, documents, etc. Firefox stores its information here, so you could even have the same bookmarks between computers with a roaming profile.
Local is the folder that is specific to that computer - any information here would not be synchronized with a server. This folder is equivalent in Windows XP to C:\Documents and Settings\User\Local Settings\Application Data.
LocalLow is the same folder as local, but it has a lower integrity level. For example, Internet Explorer 8 can only write to the LocalLow folder (when protected mode is on).
This document from Microsoft (&quot;Managing Roaming User Data Deployment Guide&quot;) has a long explanation for what these three folder areas are and how they are used, as well as the changes implemented between Windows XP and Vista (Windows 7 retains the Vista structure).

**参考链接 / References**:
- N/A

---

#### 74. How to disable internet search results in start menu post Creators Update?

**问题描述 / Problem Description**:
Tags: windows-10, windows-10-v1703, cortana, windows-10-v1803 | Score: 212 | Views: 144810 | Answers: 4

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 75. How to delete a file in Windows with a too long filename?

**问题描述 / Problem Description**:
Tags: windows, path, filenames | Score: 211 | Views: 406543 | Answers: 8

**解决方案 / Solution**:
When you want to completely delete a directory and it contains long paths, robocopy does a VERY good job:

mkdir empty_dir
robocopy empty_dir the_dir_to_delete /mir
rmdir empty_dir
rmdir the_dir_to_delete


This works because robocopy internally uses the Unicode-aware versions of Win32 functions, with the \\?\ prefix for file paths; those functions have a limit of 2¹⁶-1 (32,767) characters instead of 259.

You may need to go through this process more than once to get rid of all of the files.

**参考链接 / References**:
- N/A

---

#### 76. How to copy text from Console2?

**问题描述 / Problem Description**:
Tags: windows, console, copy-paste, console2 | Score: 210 | Views: 46862 | Answers: 10

**解决方案 / Solution**:
Open Console2 menu Edit -> Settings, and in the Hotkeys / Mouse settings configure the selection and copy actions. The defaults are a bit wonky. 

I use: 


Left mouse button = select
Ctrl+C = copy
Ctrl+V = paste
ESC = clear selection


Make sure you press 'Assign' after each change you make otherwise it won't take effect.

Last note: Beware if you use ESC or Ctrl+V in vim, or in any other app.

**参考链接 / References**:
- N/A

---

#### 77. How can I create a symbolic link on Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, symbolic-link | Score: 210 | Views: 618994 | Answers: 6

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 78. &quot;This file came from another computer...&quot; - how can I unblock all the files in a folder without having to unblock them individually?

**问题描述 / Problem Description**:
Tags: windows, security, ntfs | Score: 209 | Views: 301626 | Answers: 15

**解决方案 / Solution**:
If you download a .ZIP and unzip it, the individual files will be marked as the same zone as the .ZIP.  Almost every time I have a folder full of "blocked" files, this is how I got them.

Before unzipping, click the Unblock button on the .ZIP.

**参考链接 / References**:
- N/A

---

#### 79. How do I edit text files in the Windows command prompt?

**问题描述 / Problem Description**:
Tags: windows, command-line, ssh, text-editors | Score: 209 | Views: 1380568 | Answers: 14

**解决方案 / Solution**:
The simplest solution on all versions of Windows is:

C:\&gt; notepad somefile.txt


And, no extra software required.

**参考链接 / References**:
- N/A

---

#### 80. How can I put the computer to sleep from Command Prompt/Run menu?

**问题描述 / Problem Description**:
Tags: windows, command-line, sleep, shutdown, run-dialog | Score: 209 | Views: 792670 | Answers: 14

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 81. How do I view the contents of a PFX file on Windows?

**问题描述 / Problem Description**:
Tags: windows, security, certificate, client-certificate | Score: 206 | Views: 450692 | Answers: 6

**解决方案 / Solution**:
Some options to view PFX file details:


Open a command prompt and type: certutil -dump &lt;path to cert&gt;
Install OpenSSL and use the commands to view the details, such as: openssl pkcs12 -info -in &lt;path to cert&gt;

**参考链接 / References**:
- N/A

---

#### 82. How to access Windows folders from Bash on Ubuntu on Windows

**问题描述 / Problem Description**:
Tags: windows-10, bash, shell, windows-subsystem-for-linux | Score: 202 | Views: 353691 | Answers: 2

**解决方案 / Solution**:
You'll find the Windows C:\ structure at /mnt/c/ in the Bash environment.

Therefore, my Documents folder is at /mnt/c/Users/Ben/Documents/.

**参考链接 / References**:
- N/A

---

#### 83. How do I create a GIF screencast in Windows?

**问题描述 / Problem Description**:
Tags: windows, software-rec, screen-capture, animated-gif | Score: 201 | Views: 161751 | Answers: 10

**解决方案 / Solution**:
I've been using licecap in various Super&nbsp;User answers. It's dead simple to use as you can see from this animated GIF image - just extend it over your recording area, hit record, set a save file, do your thing and hit stop. It's free, works pretty well, and seems simpler than most of the alternatives. It's entirely free and has Windows and OS X ports.



On Windows 8.1 and hdpi displays, you'll need to turn off per app display scaling to get it to work normally without turning off global display scaling. I have a walkthrough on it here (Fixed as of version 1.26.)

**参考链接 / References**:
- N/A

---

#### 84. Windows 10 Search can&#39;t find ANY applications. Even calculator

**问题描述 / Problem Description**:
Tags: windows, search, windows-10 | Score: 201 | Views: 390409 | Answers: 13

**解决方案 / Solution**:
I have no idea why or what I have broken in the process.
But here is what worked for me.


Ctrl+Shift+Right-click on an empty part of the taskbar and clicking "Exit Explorer" (or kill it via Task Manager if that doesn't work).
Delete this registry key.



  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderTypes\{ef87b4cb-f2ce-4785-8658-4ca6c63e38c6}\TopViews\{00000000-0000-0000-0000-000000000000}



Start process Explorer.exe via Task Manager.


This is one of many answers posted here. Feel free to try other people's suggestions. If you combine all answers in one I'll accept your answer.





Method for Creator's update
Check out this answer.

**参考链接 / References**:
- N/A

---

#### 85. How can I make the Windows VPN route selective traffic (by destination network)?

**问题描述 / Problem Description**:
Tags: windows, networking, vpn, routing | Score: 200 | Views: 430954 | Answers: 13

**解决方案 / Solution**:
You can turn off taking over your entire connection by going to the properties of the VPN, Networking tab, Internet Protocol (TCP/IP) properties, Advanced, untick Use default gateway on remote network. This may or may not leave a route to 192.168.123.0/24 depending on the VPN server's setup. If it doesn't, you'll have to manually add the route each time, although you could put it in a batch file.

In order to manually add the route, run (as administrator):

route -p add 192.168.0.12 mask 255.255.255.255 10.100.100.254


This example will make a persistent (it's not necessary to run the command after a reboot) route to the IP 192.168.0.12 through the VPN gateway 10.100.100.254.

More about this at http://technet.microsoft.com/en-us/library/bb878117.aspx

**参考链接 / References**:
- N/A

---

#### 86. Why is &#39;ping&#39; unable to resolve a name when &#39;nslookup&#39; works fine?

**问题描述 / Problem Description**:
Tags: windows, networking, dns | Score: 200 | Views: 453478 | Answers: 24

**解决方案 / Solution**:
I believe that nslookup opens a winsock connection on the DNS port and issues a query, whereas ping uses the DNS Client service. You could try and stop this service and see whether this makes a difference.
Some commands that will reinitialize various network states :
Reset WINSOCK entries to installation defaults : netsh winsock reset catalog
Reset TCP/IP stack to installation defaults : netsh int ip reset reset.log
Flush DNS resolver cache : ipconfig /flushdns
Renew DNS client registration and refresh DHCP leases : ipconfig /registerdns
Flush routing table : route /f
(Caution: this will remove all your routes and gateways until you restart!)

**参考链接 / References**:
- N/A

---

#### 87. Hyper-V VM won&#39;t boot from Cd, error: &quot;unsigned image&#39;s hash is not allowed&quot;

**问题描述 / Problem Description**:
Tags: windows-10, hyper-v, bootable-media | Score: 200 | Views: 169855 | Answers: 5

**解决方案 / Solution**:
This error is a consequence of having Secure Boot enabled on the VM. Secure Boot prevents the system from getting hijacked at boot time by only allowing specifically authorized boot images to load. In Hyper-V client, the list is rather short.

To disable Secure Boot, power off the VM and then open the VM settings. Under Secure Boot, uncheck the box "Enable Secure Boot" and then click "OK". This will allow the VM to boot the "unauthorized" CD image.

Update: 
As mentioned by Itai Bar-Haim in the comments, and Thee Gamefanatic said in their answer, you can also select a different template depending on the OS image you're attempting to boot. Be aware that these templates are mutually exclusive - this means that you will not be able to boot a Windows OS image if you select the "Microsoft UEFI Certificate Authority" template.

Microsoft has a thorough deep dive into Secure Boot and how it works available on this blog:
https://blogs.technet.microsoft.com/dubaisec/2016/03/14/diving-into-secure-boot/

**参考链接 / References**:
- N/A

---

#### 88. Remote Desktop intermittently freezing

**问题描述 / Problem Description**:
Tags: windows-10, remote-desktop, windows-10-v1903 | Score: 200 | Views: 369955 | Answers: 8

**解决方案 / Solution**:
I also ran into this issue since July 2019 on a Windows 10 1903 acting as the client machine. The following workaround on the client works for me, so that RDP no longer freezes.

Start an elevated command prompt (run cmd.exe as administrator), and
then run:
reg add &quot;HKLM\software\policies\microsoft\windows nt\Terminal
Services\Client&quot; /v fClientDisableUDP /d 1 /t REG_DWORD

After that, close and reopen all your RDP sessions on your client computer to restart the Remote Desktop Client (mstsc.exe, aka Microsoft Terminal Services Client) application.
I'm waiting for a final fix to this issue.
Follow-up: I am not sure, but it looks like fixed in 21H1 (both client and server must run 21H1 or higher). For me I no longer see freezes without the disable UDP workaround.

**参考链接 / References**:
- N/A

---

#### 89. How to stop Microsoft from gathering telemetry data from Windows 7, 8, and 8.1

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-8, windows-8.1 | Score: 199 | Views: 323021 | Answers: 2

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 90. On my Windows machine, I had a folder with a name of four dots that acted like some kind of rabbit hole - how did that happen?

**问题描述 / Problem Description**:
Tags: windows, filesystems | Score: 196 | Views: 40751 | Answers: 5

**解决方案 / Solution**:
Win32 doesn't let you create files or folders with names ending in . – all dots are stripped from the end. Trying to create test. makes test appear instead. (This is for compatibility with 8.3 names in old DOS/Win9x era software.)

As a result, whenever you try to access a folder named ...., its name gets reduced to the empty string, and you're back to the folder you were in before.

The NT kernel, however, does allow such names. There are various mechanisms which bypass filename limitations imposed by Win32 APIs – for example, WSL (Windows Subsystem for Linux) doesn't run on top of Win32 and is unaffected by it. There is also the \\?\ bypass method, a deliberate "backdoor" left in for programs which know what they're doing. Even though you cannot create C:\Example\....\, you can create \\?\C:\Example\....\ just fine.

Likewise you can delete such directories with rmdir \\?\C:\path\... from Cmd (I haven't tested with PowerShell yet).

Various file managers, archivers, etc. might use the \\?\ method in order to be able to use longer path names than usual – and by doing so, they're also unaffected by the compatibility code within Win32; they bypass dot stripping, as well as translation of magic filenames like CON or NUL.

So it could be that one of your programs:


always uses \\?\ to access files, 
accidentally tried to create a folder named .... – but it's not really possible to know for sure after the fact.

**参考链接 / References**:
- N/A

---

#### 91. How to access linux/Ubuntu files from Windows 10 WSL?

**问题描述 / Problem Description**:
Tags: windows-10, windows-10-v1607, windows-subsystem-for-linux | Score: 196 | Views: 440334 | Answers: 15

**解决方案 / Solution**:
PM for Windows Command-Line here:

Updated October 2019: Updating the response below to reflect the newly added ability to directly access distros' Linux files via the newly integrated P9 server in Win10 1903 (and later).
IMPORTANT: Spelunking through the Windows filesystem to access Linux files has and will continue to be unsupported and STRONGLY recommended against! To understand why, please read this post

So how does one access Linux files using Windows tools (e.g. notepad, VS/VScode, etc.)? Previously, you couldn't, but starting in Windows 10 1903 we (finally!) expose your distros' filesystems to Windows via a P9 fileserver. We've also published an in-depth video discussing how this works! You can also read a summary of this new feature in this blog post

Look forward to hearing how you get on with this feature. If you find any problems, please file issues on the WSL GitHub repo here: https://github.com/Microsoft/wsl.

**参考链接 / References**:
- N/A

---

#### 92. How can I determine file type without an extension on Windows?

**问题描述 / Problem Description**:
Tags: windows, file-management, file-extension | Score: 194 | Views: 322511 | Answers: 7

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 93. How can I prevent a policy-enforced screen lock in Windows?

**问题描述 / Problem Description**:
Tags: windows, screensaver, security-policy | Score: 192 | Views: 754710 | Answers: 18

**解决方案 / Solution**:
If Windows Media Player is still installed, you can play a video on loop and minimize it (the sample "Wildlife" videos work fine for this).  By default, as long as a video is playing, the screen won't lock.

**参考链接 / References**:
- N/A

---

#### 94. How do I delete a folder that&#39;s in use?

**问题描述 / Problem Description**:
Tags: windows, file-management | Score: 191 | Views: 655536 | Answers: 18

**解决方案 / Solution**:
There's a native GUI for Windows:

Start>>All Programs>>Accessories>>System Tools>>Resource Monitor (or Run resmon.exe)

You can search for the "Associated Handles" using the searchbox (circled in red), and right click the process you want to end.



As an example, in the image below I could not delete my Eclipse directory. Searching for the Eclipse associated handles showed that the adb.exe had a handle to the directory. After ending the adb process, I could then delete the Eclipse directory.

**参考链接 / References**:
- N/A

---

#### 95. Create .zip folder from the command line - (Windows)

**问题描述 / Problem Description**:
Tags: windows | Score: 190 | Views: 728995 | Answers: 12

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 96. How to run a batch file in a completely hidden way?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch-file | Score: 189 | Views: 809378 | Answers: 20

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 97. Apostrophes and double quotes don&#39;t show up until I type the next letter

**问题描述 / Problem Description**:
Tags: windows, windows-xp, keyboard | Score: 188 | Views: 407550 | Answers: 12

**解决方案 / Solution**:
The reason is because you are using US-international keyboard. 

Here is how to change this:


In the Windows run box (Windows+R) type control intl.cpl or control international.
Click the "Keyboards and Languages" tab
Click "Change Keyboards..."
AT THIS POINT MAKE SURE YOU ARE USING "English (United Kingdom) - US" as the default input language, meaning you set the keyboard to US, not US-international

**参考链接 / References**:
- N/A

---

#### 98. Why does 64-bit Windows need a separate &quot;Program Files (x86)&quot; folder?

**问题描述 / Problem Description**:
Tags: windows, 64-bit | Score: 184 | Views: 106592 | Answers: 11

**解决方案 / Solution**:
Short answer: To ensure legacy 32-bit applications continue to work the same way they used to without imposing ugly rules on 64-bit applications that would create a permanent mess.

It is not necessary. It's just more convenient than other possible solutions such as requiring every application to create its own way to separate 32-bit DLLs and executables  from 64-bit DLLs and executables.

The main reason is to make 32-bit applications that don't even know 64-bit systems exist "just work", even if 64-bit DLLs are installed in places the applications might look. A 32-bit application won't be able to load a 64-bit DLL, so a method was needed to ensure that a 32-bit application (that might pre-date 64-bit systems and thus have no idea 64-bit files even exist) wouldn't find a 64-bit DLL, try to load it, fail, and then generate an error message.

The simplest solution to this is consistently separate directories. Really the only alternative is to require every 64-bit application to "hide" its executable files somewhere a 32-bit application wouldn't look, such as a bin64 directory inside that application. But that would impose permanent ugliness on 64-bit systems just to support legacy applications.

**参考链接 / References**:
- N/A

---

#### 99. Why does the /winsxs folder grow so large, and can it be made smaller?

**问题描述 / Problem Description**:
Tags: windows, disk-space, winsxs | Score: 183 | Views: 128714 | Answers: 12

**解决方案 / Solution**:
There is a nice command that cleans up after a Windows 7 SP1 installation (it saved me around 3&nbsp;GB):

DISM /online /cleanup-Image /spsuperseded


Must be executed from an elevated command prompt

**参考链接 / References**:
- N/A

---

#### 100. What utility can move my Windows boot partition over to another hard drive?

**问题描述 / Problem Description**:
Tags: windows, hard-drive, boot, backup, partitioning | Score: 182 | Views: 440315 | Answers: 18

**解决方案 / Solution**:
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

**参考链接 / References**:
- N/A

---

#### 101. How does Windows know if a program is not responding?

**问题描述 / Problem Description**:
Tags: windows | Score: 181 | Views: 40330 | Answers: 5

**解决方案 / Solution**:
An application gets the events from a queue provided by Windows. 

If the application doesn't poll the eventqueue for a while (5 seconds), for example when doing a long calculation, then Windows assumes that the application is hung and alerts the user.

To avoid that applications should push expensive calculations to worker threads or split up processing and make sure the queue gets polled regularly.

**参考链接 / References**:
- N/A

---

#### 102. How can I provoke Windows to hang (freeze)?

**问题描述 / Problem Description**:
Tags: windows, freeze | Score: 180 | Views: 43842 | Answers: 13

**解决方案 / Solution**:
Maybe this can help:
Forcing a System Crash from the Keyboard


  With USB keyboards, you must enable the keyboard-initiated crash in
  the registry. In the registry key
  HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\kbdhid\Parameters,
  create a value named CrashOnCtrlScroll, and set it equal to a
  REG_DWORD value of 0x01.
  
  You must restart the system for these settings to take effect.
  
  After this is completed, the keyboard crash can be initiated by using
  the following hotkey sequence: Hold down the rightmost CTRL key, and
  press the SCROLL LOCK key twice.


Or you could start a fork bomb: see this SO question

There is also NotMyFault


  Notmyfault is a tool that you can use to crash, hang, and cause kernel memory leaks on your Windows system. It’s useful for learning how to identify and diagnose device driver and hardware problems, and you can also use it to generate blue screen dump files on misbehaving systems.

**参考链接 / References**:
- N/A

---

#### 103. How can I clear the output from Window&#39;s Command Prompt using a keyboard shortcut?

**问题描述 / Problem Description**:
Tags: windows, command-line, keyboard-shortcuts | Score: 179 | Views: 692160 | Answers: 3

**解决方案 / Solution**:
NO, But you can use CLS command to clear the whole screen, Esc (Escape) key will clear the input line.
In addition, pressing Ctrl + C will move the cursor to a new blank line.

**参考链接 / References**:
- N/A

---

#### 104. What is the purpose/function of &quot;.&#223;&#223;&#223;&quot; files?

**问题描述 / Problem Description**:
Tags: windows, file-transfer | Score: 177 | Views: 22594 | Answers: 1

**解决方案 / Solution**:
Most likely these aren't actual files but the result of filesystem corruption.


It is normally not possible to have multiple identically named files.
Their names (ßßßßßßßß.ßßß) correspond to hexadecimal bytes E1 E1 E1&hellip; in code page 437 (which was the default MS-DOS code page, and therefore the default FAT/FAT32 code page when long file names aren't in use).
(The character is not the Greek beta but the German lowercase sharp S. The dot isn't actually stored in the FAT, but added by the OS when reading, so it doesn't get corrupted.)
Their sizes are close to 3&thinsp;789&thinsp;677&thinsp;025 bytes, which is again 0xE1&thinsp;E1&thinsp;E1&thinsp;E1 in hex.
(That's approximately 3&thinsp;700&thinsp;856.469 kilobytes; Windows probably rounds up.)


All signs point to part of your filesystem's master file table being filled with the byte 0xE1, which may be caused by software (such as unplugging mid-write),  but may also indicate that the flash memory itself is dying.

Software-induced corruption can often be cleaned up by using Windows' disk error checking (chkdsk). Or just reformat the drive (after copying your real files out of it).

But especially for cheaper and/or heavily-used drives, bad flash memory is very likely. Don't use this drive for important files anymore.

**参考链接 / References**:
- N/A

---

#### 105. How to disable Ctrl+Shift keyboard layout switch (for the same input language) in Windows?

**问题描述 / Problem Description**:
Tags: windows, keyboard-shortcuts, keyboard-layout | Score: 177 | Views: 393524 | Answers: 13

**解决方案 / Solution**:
You were very close to the solution of your problem ;)
In Windows XP, Vista or 7:
Control Panel -&gt; Regional and Language Options -&gt; Languages tab -&gt; Details...
There, you can edit the hotkeys to change input languages. If you press the Change Key Sequence... button, you will be able to change (disable) the hotkey which switches keyboard layouts (that Ctrl+Shift combination you mentioned).

**参考链接 / References**:
- N/A

---

#### 106. Two blue arrows at top right of icons

**问题描述 / Problem Description**:
Tags: windows-10, windows-explorer, icons, microsoft-office-2007 | Score: 177 | Views: 788666 | Answers: 10

**解决方案 / Solution**:
I archived the folder and the text went blue as expected...


Blue text in Explorer = NTFS compression is enabled via the properties (this has been standard in Windows for many versions now).



Two blue arrows is Windows 10's new way of showing the same thing, at the icon-level.



Reference/More info:


Compress or Uncompress Files and Folders in Windows 10
Properties dialog image source


edit:


  When I just recently installed Office 2007, I noticed the same arrows on the icons for the programs.


That's kind of weird, and is may be just a matter of icon cache corruption.

For that, here's a couple things to try:

Ensure the EXEs are not actually compressed.

Try creating new shortcuts to the EXEs and see if they appear as expected.

Try clearing Windows' icon cache and see if that corrects the icons. For that, see this existing SU question: Refresh Icon Cache Without Rebooting

**参考链接 / References**:
- N/A

---

#### 107. Change name of Virtual Desktop in Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, virtual-desktop, virtual-desktop-manager | Score: 177 | Views: 90590 | Answers: 7

**解决方案 / Solution**:
It seems at this time, you can not rename the virtual desktops in Windows 10. It is a feature that I would love to have though.
EDIT: It seems you can now rename virtual desktops.

**参考链接 / References**:
- N/A

---

#### 108. What can I do if I forgot my Windows password?

**问题描述 / Problem Description**:
Tags: windows-7, windows, passwords, community-faq | Score: 176 | Views: 295094 | Answers: 17

**解决方案 / Solution**:
If you have an Ubuntu live CD you can reset it using chntpw application
You can use Bart's PE + Password Renew to reset the password
You can use Offline NT Password Editor to reset the password.


Detailed instructions on using any of the 3 are available over here.

**参考链接 / References**:
- N/A

---

#### 109. How to disable the screen orientation hotkeys in Windows (XP)?

**问题描述 / Problem Description**:
Tags: windows, display, keyboard-shortcuts, hotkeys, nvidia-graphics-card | Score: 176 | Views: 100682 | Answers: 4

**解决方案 / Solution**:
I have not tested on AMD/ATI graphics, but I know for a fact that all Intel drivers do this and some Nvidia drivers.

Simply go in to the configuration tool of your driver and look under a section called hotkeys and disable it.

For Intel:

**参考链接 / References**:
- N/A

---

#### 110. How to delete a keyboard layout in Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, keyboard-layout | Score: 176 | Views: 488230 | Answers: 9

**解决方案 / Solution**:
To remove a keyboard under Windows 10 is done this way :
Method 1 : Settings

Select the Start button
Go to Settings &gt; Time &amp; Language &gt; Region &amp; language
Under Languages, click your language

Click Options
Under Keyboards click your keyboard
Click Remove


Method 2 : Preloaded

Use regedit to navigate to following registry keys, where
you will find there the list of keyboards that are preloaded at boot.


HKEY_USERS\.DEFAULT\Keyboard Layout\Preload
HKEY_CURRENT_USER\Keyboard Layout\Preload
HKEY_USERS\.DEFAULT\Control Panel\International\User Profile
HKEY_USERS\.DEFAULT\Control Panel\International\User Profile System Backup


Find the keyboard identifier among the list of
Keyboard Identifiers

Delete the key.



Update January 2022:
The language settings are now found in
Settings &gt; Time &amp; Language &gt; Language.

**参考链接 / References**:
- N/A

---

#### 111. Is there a convenient way to edit PATH in Windows 7?

**问题描述 / Problem Description**:
Tags: windows, path | Score: 174 | Views: 70489 | Answers: 10

**解决方案 / Solution**:
There is always the Rapid Environment Editor which claims full support for all major OS versions, including 64-bit.


  Editable tree
  
  Show environment variables and values as an editable tree.
  
  Portable mode
  
  RapidEE doesn't require installation and could be run as a "portable application". View details.
  
  


There is also the older (but still useful) and more light-weight Path Editor. (Note that the site is dead as of 2015-08-07, but still exists as an archive.org snapshot from 2013-03-27 — direct link to the installer). It works just fine on Windows 7 and, though it comes only as an installer, also works as a portable/stand-alone executable if you extract it.


  Path Editor is a small utility that makes path management very straightforward with its intuitive user interface and drag-and-drop simplicity. Path Editor can clean your path of missing and duplicate entries with a single click of the mouse.

**参考链接 / References**:
- N/A

---

#### 112. How do I get back unused disk space from Ubuntu on WSL2?

**问题描述 / Problem Description**:
Tags: windows-10, windows-subsystem-for-linux, disk-space, wsl2, ubuntu-20.04 | Score: 173 | Views: 338315 | Answers: 10

**解决方案 / Solution**:
There are a few options here, but I'm moving things around in this edit. My &quot;original&quot; answer is back to being the preferred method.  See the bottom of this answer for an alternative, experimental method.
&quot;Original&quot; Answer (Preferred)
There's a WSL Github issue open on this topic.  WSL will automatically grow the virtual disk (ext4.vhdx), but shrinking it to reclaim unused space is something that must currently be done manually.
The first thing you'll need to do is know the location of your ext4.vhdx.  For a default Ubuntu installation, it should be in something like %USERPROFILE%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\
Then there are several techniques that you can use to remove the unused space.  I recommend you start with a wsl --shutdown and copy the vhdx as a backup to start.  If you are running Docker Desktop, also shut it down, otherwise it may inadvertently attempt to restart WSL after your --shutdown.

If you are on Windows Professional or higher, you can install Hyper-V and use the Optimize-VHD commandlet as described in the original issue.
.

On Windows Home (and higher) you can use diskpart as described in this comment.

Exporting the WSL distro and re-importing it into a new WSL instance (as in this comment) will also reclaim the space.  Note that you will need to reset the default username after an import. See here (and here for alternative options).


I have tested and confirmed both the second and third techniques personally.

Alternative (Warning)
The following feature remains in &quot;Experimental&quot; status a year after its appearance, and while I'm sure it works well for many, too many users continue to report corruption of their WSL Distributions and sometimes even the Windows host filesystem when using it.
Thanks to comments from @MarkCh and @willnode, I've edited the answer to both move this method under the original answer as well as highlight this warning.
In September, 2023, a pre-release of WSL (2.0.0) enabled a new &quot;sparse&quot; mode for disk images which is intended to automatically shrink the image when files are removed. (Especially given the warning above) Always maintain good backups, especially when using newer features that affect the entire virtual drive. I have not tested this personally yet.
While that said, from the DevBlog announcement, you can convert an existing disk image to sparse with the following command from PowerShell:
wsl --manage &lt;distro&gt; --set-sparse true

You can also add the following to your .wslconfig (located in your Windows profile directory, not inside WSL) to have any newly created distro image be sparse:
[experimental]
sparseVhd=true

**参考链接 / References**:
- N/A

---

#### 113. How to run a batch file without launching a &quot;command window&quot;?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch-file, shortcuts | Score: 172 | Views: 638958 | Answers: 9

**解决方案 / Solution**:
Save the following as wscript, for instance, hidecmd.vbs after replacing "testing.bat" with your batch file's name.

Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c testing.bat"
oShell.Run strArgs, 0, false


The second parameter of oShell.Run is intWindowStyle value indicating the appearance of the program's window and zero value is for hidden window.

The reference is here http://msdn.microsoft.com/en-us/library/d5fk67ky.aspx

**参考链接 / References**:
- N/A

---

#### 114. How do I paste the Windows clipboard into my PuTTY session, using only the keyboard?

**问题描述 / Problem Description**:
Tags: windows, keyboard-shortcuts, putty, clipboard | Score: 171 | Views: 437716 | Answers: 3

**解决方案 / Solution**:
You can use Shift+Ins to paste text.

From PuTTY documentation:


Pasting is done using the right button (or the middle mouse button, if you have a three-button mouse and have set it up; see section 4.11.2). (Pressing Shift-Ins, or selecting ‘Paste’ from the Ctrl+right-click context menu, have the same effect.) When you click the right mouse button, PuTTY will read whatever is in the Windows clipboard and paste it into your session, exactly as if it had been typed at the keyboard.

**参考链接 / References**:
- N/A

---

#### 115. How do I remove Candy Crush Saga from Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, uninstall | Score: 171 | Views: 134542 | Answers: 8

**解决方案 / Solution**:
I was able to uninstall simply by right-clicking on the app in the Start Menu and selecting uninstall.

Typing Get-AppxPackage -Name king.com.CandyCrushSaga into PowerShell confirmed it is completely gone from the system, not just from the start menu.

**参考链接 / References**:
- N/A

---

#### 116. Windows on second monitor moves to primary monitor after sleep/lock

**问题描述 / Problem Description**:
Tags: windows, windows-10, display, multiple-monitors, visual-studio | Score: 170 | Views: 473586 | Answers: 9

**解决方案 / Solution**:
A similar case on Microsoft Community mentioned a workaround, have a try.


Start Control Panel --&gt; Device Manager
Select View --&gt; Show hidden devices
Expand Computer --&gt; Monitors*

When you expand the Monitors you will see your current monitor (highlighted) and all the disconnected monitors (greyed out).   You may see monitors with &quot;non-PNP&quot; and &quot;PNP&quot; listed as well.  I believe these are aliases to your current monitor (at a lower resolution) before Windows installed drivers for it.
I uninstalled ALL the greyed out monitors.  Right-click on these monitors and select uninstall.  Keep only the highlighted monitor you are currently using.

Uninstall all greyed out monitors (even non-PNP and PNP monitors)
Reboot your system.

After doing this my windows don't resize after my monitor goes to sleep.  You can quickly test this by temporarily setting your monitor sleep time to 1 minute.
Settings --&gt; System --&gt; Power &amp; Sleep --&gt; Screen [1 minute]

Source: https://answers.microsoft.com/en-us/windows/forum/windows_10-hardware-winpc/windows-10-multiple-display-windows-are-moved-and/2b9d5a18-45cc-4c50-b16e-fd95dbf27ff3

**参考链接 / References**:
- N/A

---

#### 117. What is a &quot;Magic Packet&quot; for waking a computer?

**问题描述 / Problem Description**:
Tags: windows, networking, wireless-networking, wake-on-lan | Score: 168 | Views: 129708 | Answers: 2

**解决方案 / Solution**:
Sam3000's answer is very nice. I'll add some technical details.

Wake on Magic Packet causes the network card to awaken the computer when it receives a magic packet. A packet is considered "magic" when it contains FF FF FF FF FF FF (six instances of the largest possible byte value) followed by sixteen instances of the card's six-byte MAC address. That sequence can appear anywhere within the frame, so the packet can be sent over any higher-level protocol. Usually, UDP is used, but sometimes raw frames with EtherType 0x0842 are used. (Source: Wikipedia.)

Wake on Pattern Match is a superset of the previous. It will cause the card to wake the machine when various things come in, including a magic packet, a NetBIOS name query, a TCP SYN packet (either TCPv4 or TCPv6), etc. Those last ones may require ARP offload to be enabled. (Source: TechNet.)

If you don't want/need your computer to be woken up from anywhere else, you can disable both of those options.

**参考链接 / References**:
- N/A

---

#### 118. Notepad++ is unable to load langs.xml, why?

**问题描述 / Problem Description**:
Tags: windows-7, windows, notepad++ | Score: 168 | Views: 120116 | Answers: 6

**解决方案 / Solution**:
Somehow, your langs.xml has errors in it. Perhaps while exploring various Notepad++ options you accidentally made unintended changes to it. That's what happened to me.
Go to the installation folder for Notepad++ and rename langs.xml to langs.xml.bad. Then, in that same folder, find langs.model.xml, make a copy of it, and rename the copy to langs.xml. DO NOT simply rename the file or you will not have it available the next time you need it.
also replace this file in the folder C:\users\(user)\appdata\roaming\notepad++
You will want to then compare the langs.xml to langs.xml.bad and see if there is anything legitimate that you want back.
If you are missing the langs.model.xml file, you can download the current version from the master branch of the official github repo.

**参考链接 / References**:
- N/A

---

#### 119. How can I determine which process owns a hotkey in Windows?

**问题描述 / Problem Description**:
Tags: windows, keyboard-shortcuts | Score: 168 | Views: 103271 | Answers: 6

**解决方案 / Solution**:
This works for me in Win10 (and probably all other even vaguely-recent versions of Windows)... also copied here from https://stackoverflow.com/a/43645062/995048 since this page seems to come up first in search results:

One possible way is to use the Visual Studio tool Spy++.
Give this a try:

Run the tool (for me, it's at C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\spyxx_amd64.exe, or use spyxx.exe to monitor 32-bit processes)
In the menu bar, select Spy -&gt; Log messages... (or hit Ctrl + M)
Check All Windows in System in the Additional Windows frame
Switch to the Messages tab
Click the Clear All button
Select WM_HOTKEY in the listbox, or check Keyboard in Message Groups (if you're OK with more potential noise)
Click the OK button
Press the hotkey in question (Win + R, for example)
Select the WM_HOTKEY line in the Messages (All Windows) window, right click, and select Properties... in the context menu
In the Message Properties dialog, click the Window Handle link (this will be the handle for the window that received the message)
Click the Synchronize button on the Window Properties dialog.  This will show the window in the main Spy++ window treeview.
On the Window Properties dialog, select the Process tab
Click the Process ID link.  This will show you the process (In my Win + R case: EXPLORER)

**参考链接 / References**:
- N/A

---

#### 120. Windows 10 - How to move window to other monitor by using keyboard shortcuts?

**问题描述 / Problem Description**:
Tags: windows, windows-10, multiple-monitors, keyboard-shortcuts | Score: 168 | Views: 791822 | Answers: 5

**解决方案 / Solution**:
I solved it by unchecking the box which you can see in the following screenshot.

Go to Control Panel &gt; Ease of Access Center &gt; Make the Keyboard Easier to Use
Then search for the setting &quot;Make it easier to manage windows&quot; and un-check the option &quot;Prevent windows from being automatically arranged when moved to the edge of the screen&quot;
After unchecking this option, it works again.

**参考链接 / References**:
- N/A

---

#### 121. Items unpinned from taskbar are back after restart/sign out on Windows 10

**问题描述 / Problem Description**:
Tags: windows, windows-10, taskbar | Score: 167 | Views: 277107 | Answers: 7

**解决方案 / Solution**:
I had the same problem. Nothing works.

Finally, I found the XML file in my profile:

%LOCALAPPDATA%\Microsoft\Windows\Shell\LayoutModification.xml


The items were listed here in this section:

  &lt;/DefaultLayoutOverride&gt;
    &lt;CustomTaskbarLayoutCollection PinListPlacement="Replace"&gt;
    &lt;defaultlayout:TaskbarLayout&gt;
      &lt;taskbar:TaskbarPinList&gt;
-- items were here - removed
      &lt;/taskbar:TaskbarPinList&gt;
    &lt;/defaultlayout:TaskbarLayout&gt;
  &lt;/CustomTaskbarLayoutCollection&gt;


Maybe this will help someone.

**参考链接 / References**:
- N/A

---

#### 122. What is the difference between “Size” and “Size on disk?”

**问题描述 / Problem Description**:
Tags: windows, filesystems | Score: 167 | Views: 292808 | Answers: 6

**解决方案 / Solution**:
Size is the actual size of the file in bytes.
Size on disk is the actual amount of space being taken up on the disk. They differ because the disk is divided into tracks and sectors, and can allocate blocks of discrete size.
For a more detailed explanation, see this text which I copied from another site:

We know that a disk is made up of Tracks and Sectors. In Windows that
means the OS allocates space for files in &quot;clusters&quot; or &quot;allocation
units&quot;.
The size of a cluster can vary, but typical ranges are from 512 bytes
to 32K or more. For example, on my C:\ drive, the allocation unit is
4096 bytes. This means that Windows will allocate 4096 bytes for any
file or portion of a file that is from 1 to 4096 bytes in length.
If I have a file that is 17KB (kilo bytes), then the Size on disk
would be 20.48 KB (or 20480 bytes). The calculation would be 4096 (1
allocation unit) x 5 = 20480 bytes. It takes 5 allocation units to
hold a 17KB file.
Another example would be if I have a file that is 2000 bytes in size.
The file size on disk would be 4096 bytes. The reason is, because even
though the entire file can fit inside one allocation unit, it still
takes up 4096 of space (one allocation unit) on disk (only one file
can use an allocation unit and cannot be shared with other files).
So the size on disk is the space of all those sectors in which the
file is saved. That means,usually, the size on disk is always greater
than the actual size.
So the actual size of a file(s) or folder(s) should always be taken
from the Size value when viewing the properties window.

Source: What's The Difference Between Size And Size On Disk In Windows Folder Properties.

**参考链接 / References**:
- N/A

---

#### 123. VT-x is not available, but is enabled in BIOS

**问题描述 / Problem Description**:
Tags: windows-10, bios, virtualization, vt-x | Score: 166 | Views: 460731 | Answers: 14

**解决方案 / Solution**:
There are three common culprits for the type of error the user is seeing:


VT-x is not enabled in the BIOS
The CPU doesn't support VT-x
Hyper-V virtualization is enabled in Windows


Since the user already eliminated the first two possible culprits, the next step is to open a command prompt as administrator and run the following command:

dism.exe /Online /Disable-Feature:Microsoft-Hyper-V


Afterwards, reboot the PC and try VirtualBox again.

**参考链接 / References**:
- N/A

---

#### 124. Force a program to run *without* administrator privileges or UAC?

**问题描述 / Problem Description**:
Tags: windows, administrator, uac | Score: 165 | Views: 860398 | Answers: 11

**解决方案 / Solution**:
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\forcerunasinvoker]
@="Run without privilege elevation"

[HKEY_CLASSES_ROOT\*\shell\forcerunasinvoker\command]
@="cmd /min /C \"set __COMPAT_LAYER=RUNASINVOKER &amp;&amp; start \"\" \"%1\"\""


Save this text in &lt;name_of_file&gt;.reg and add it to the Windows Registry. (Double-clicking on it should do the trick.)

Afterwards, right-click the app you'd like to run without administrative privileges and select "Run without privilege elevation".

In some cases - small amount 0.1% of programs may ask twice about UAC prompt.

**参考链接 / References**:
- N/A

---

#### 125. What does CTRL+WIN+SHIFT+B do in Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-10, keyboard-shortcuts | Score: 165 | Views: 530893 | Answers: 4

**解决方案 / Solution**:
The Ctrl+Shift+Win+B key sequence will restart your graphics driver.

**参考链接 / References**:
- N/A

---

#### 126. How can I read my hard drive’s SMART status in Windows 7?

**问题描述 / Problem Description**:
Tags: windows-7, windows, hard-drive, smart | Score: 164 | Views: 418845 | Answers: 16

**解决方案 / Solution**:
HDTune works on Windows 7 too.



A blog-post reference.

**参考链接 / References**:
- N/A

---

#### 127. Pseudo English looking characters used in Windows 10 Insider Preview

**问题描述 / Problem Description**:
Tags: windows, windows-10-preview, security-center | Score: 164 | Views: 14849 | Answers: 1

**解决方案 / Solution**:
I wanted to know if anyone else has seen this or, even better, knows what is up?

First the good news, it's not a virus.
You are seeing the effects of something called Pseudo-Localization, and it is a known thing with some insider preview builds that have the language set to something other than en-us.
To fix the issue change your language to en-us.


That's pseudolocalization used to test compatibility across different
languages. Microsoft and others have been doing it for years now.
During most development, the only language that has 100% coverage is
en-us because 100% of primary development on Windows is done in
Redmond.
Running non-US locales on insider builds, especially in Skip Ahead and
Fast Ring, are only shipped with en-US and Pseudoloc'd locales. OP is
definitely using en-UK (&quot;programme&quot;) which means that a large number
of strings are probably pseudoloc'd. This helps identify non-localized
strings
it's weird enough that it won't make it into retail through an
automated check (there's a lot of zero-width spaces in there, too,
which aren't allowed in normal translations for the most part).

Source Strange font/characters in some apps : windowsinsiders

My name is Miki Albertson and I’m a Program Manager from Windows
Localization team. Today I would like to give you a behind-the-scenes
look at how WDG products are made available to Windows Insiders in
their language. By the way, we call this process “Localization”.
Second, we use a process known as “pseudo enhancement” within the
existing localized builds to allow us to mark new or changed UI
strings that have been exposed to localization, but have not yet been
localized. For some non-Latin based languages, this can involve adding
some random localized characters at the start of the unlocalized
string as an identifier; or in the case of Latin-based languages we
replace the existing characters in the string with accented versions.
If there are unlocalized (i.e. English) strings in the build that
don’t have those characters, this is potentially a bug and could
potentially delay the project. (Please see below for examples of
“Pseudo Enhancement”)

With Windows as a Service, validation through the Pseudo Localization
Tool is often done parallel to our translation work. Once those
resources have been translated, Pseudo-enhanced characters that were
added to the resources will be removed. Also, for those resources that
are not yet localized, the process is to turn off Pseudo Localization
tool before we release to Insiders, but sometimes due to this not
being done as expected, you might see the pseudo strings in the
Insider Preview builds.

(emphasis mine)
Source Inside WDG – Localization Process – W10FG

Further Reading

Inside WDG – Localization Process – W10FG
Localizability Testing - Globalization | Microsoft Docs
What is Pseudo-Localization?
A brief and also incomplete history of Windows localization | The Old New Thing

**参考链接 / References**:
- N/A

---

#### 128. Path to current desktop backgrounds in Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10 | Score: 164 | Views: 1070781 | Answers: 8

**解决方案 / Solution**:
Built-in wallpapers
A copy of the current wallpaper can be found by entering one of the below paths in Windows File Explorer address bar.
Some of the paths below may not exist on your PC, and that's OK; move on to the next path.
Path 1 -
%AppData%\Microsoft\Windows\Themes\CachedFiles

Path 2 -
%AppData%\Microsoft\Windows\Themes\TranscodedWallpaper
Note: TranscodedWallpaper does not have a file extension, even though it is a JPEG image file.
To view the image in a imager viewer,

Right click on the file and use &quot;Open With&quot; option
(or)
select the image and press Enter
This will bring up the &quot;Select an app to open...&quot; or &quot;How do you want to open this file?&quot; dialogue box.
Any popular image viewer should work - such as the &quot;Windows Photo Viewer&quot; (built-in), Microsoft Photos app, PicView, qView, etc..

Alternatively, drag and drop the file into a Firefox tab or mspaint window to view/edit.
Note for Windows 10/11: The above wallpaper paths comes with limitations.
For example, if the wallpaper you're looking for is no longer visible in the 'Background' tab in the Settings app, you can't recover it. It will work for your last five wallpapers but nothing older. [1]

Path 3: Default Windows wallpapers -
%SystemRoot%\Web
Check in one of the below folders  -

&quot;4K&quot; for 4K wallpapers
&quot;Screen&quot; for lock screen backgrounds
&quot;touchkeyboard&quot; for colorful abstract backdrops in Windows 11 [2]
&quot;Wallpapers&quot; for default Windows wallpapers


Path 4: Wallpapers from installed themes (Aero, etc.) -
%SystemRoot%\Resources\Themes
Path 5: Wallpapers from per-user installed themes (including pre-installed themes from OEM) -
%LocalAppData%\Microsoft\Windows\Themes

Desktop background set by Windows Photo Viewer
Path 6 - [21]
%AppData%\Microsoft\Windows Photo Viewer\
Note 1: The image file in above path will be named Windows Photo Viewer Wallpaper.jpg and is a copy of the original image used to set the desktop wallpaper. I am unaware of a easy method to find the location of the original image (an file/image duplicate comparison tool might be an option).
Note 2: If desktop background was NOT set by Windows Photo Viewer, the above path might sometimes redirect to %AppData%\Microsoft\Windows instead. This is not unexpected. Dismiss the window, and move on to one of the below scripts to find correct wallpaper location.

Desktop background set by Slideshow or other methods
If the wallpaper is set by Windows Slideshow, 3rd party app or manually set by a user, try one of the below scripts.
The code will attempt to extract the original location of the image by decoding binary data from below key in the Windows Registry.
Key Name: HKEY_CURRENT_USER\Control Panel\Desktop
Value Name: TranscodedImageCache
Windows Slideshow -

Manually set wallpaper - e.g., right click on image file and select &quot;Set as desktop background&quot;


Script 1 - VBScript

To decode the registry key and view the image in Windows Explorer, follow the instructions listed on ElevenForum.com;
(or)
Open Notepad to save below code in a .vbs file and run it.

Only ASCII compatible.
Read the warning written below the code for more information.
The contents of .vbs file - [5]
Const HKCU = &amp;H80000001 'HKEY_CURRENT_USER

sComputer = &quot;.&quot;  

Set oReg=GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; _
            &amp; sComputer &amp; &quot;\root\default:StdRegProv&quot;)

sKeyPath = &quot;Control Panel\Desktop\&quot;
sValueName = &quot;TranscodedImageCache&quot;
oReg.GetBinaryValue HKCU, sKeyPath, sValueName, sValue


sContents = &quot;&quot;

For i = 24 To UBound(sValue)
  vByte = sValue(i)
  If vByte &lt;&gt; 0 And vByte &lt;&gt; &quot;&quot; Then
    sContents = sContents &amp; Chr(vByte)
  End If
Next

CreateObject(&quot;Wscript.Shell&quot;).Run &quot;explorer.exe /select,&quot;&quot;&quot; &amp; sContents &amp; &quot;&quot;&quot;&quot;

Note: The vbs didn't work for me when I first set up the Slideshow, but it worked after changing to the next image in the Slideshow.
Warning: This vbs code does not work if the file name contains non-ASCII characters, i.e., if Unicode characters (like Δ, Й, ק ,م, ๗, あ, 叶, 葉, 말) are present in the file name, then the vbs code above will fail to locate the image in Windows Explorer.

Script 2 - PowerShell [8]
ASCII + Unicode compatible

Option A:
Run below code in a PowerShell window.

Open/select Windows PowerShell using the Start menu or Win + X shortcut.
(Admin) privilege is not required.
Paste below code and press Enter.
$TIC=(Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache
Paste below code (a second time) and press Enter.
[System.Text.Encoding]::Unicode.GetString($TIC) -replace '(.+)([A-Z]:[0-9a-zA-Z\\])+','$2'

Location of the wallpaper will displayed.




Option B:
Save below code as .ps1 file and run

Open Notepad and paste the three lines of code mentioned below.
Save the new document as Wallpaper_path.ps1 file.
Note: Under 'Save as type:' option, select &quot;All types&quot; (see screenshot below).
Go to the file, right click on the file and select &quot;Run with PowerShell&quot;

Location of the wallpaper will be generated and copied to clipboard.


$TIC = (Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache
$result = [System.Text.Encoding]::Unicode.GetString($TIC) -replace '(.+)([A-Z]:[0-9a-zA-Z\\])+','$2'
Set-Clipboard -Value $result

Save .ps1 file -

Run .ps1 file -


Script 3 - AutoHotkey
ASCII + Unicode compatible

Download and install AutoHotkey.
Open Notepad and save below code as .ahk file.
Run .ahk file.
Press Win + W and the location of the wallpaper will be displayed in a message box.

#Requires AutoHotkey v2.0
#SingleInstance force

; #HotIf WinActive(&quot;ahk_class WorkerW ahk_exe explorer.exe&quot;)
; commented out - enable shortcut on desktop only

#W::{ ; Win + W
MsgBox &quot;WallpaperPath_v5`n&quot; WallpaperPath_v5(ThisHotkey),, 262144 ; 262144 = Always-on-top
}

; #HotIf

;-------
; User-defined functions

WallpaperPath_v5(key := A_ThisHotkey) {

; modified from https://www.autohotkey.com/docs/v2/lib/ComObject.htm#ExWallpaper
AD := ComObject(&quot;{75048700-EF1F-11D0-9888-006097DEACF9}&quot;, &quot;{F490EB00-1240-11D1-9888-006097DEACF9}&quot;)
wszWallpaper := Buffer(260 * 2)
ComCall(4, AD, &quot;ptr&quot;, wszWallpaper, &quot;uint&quot;, 260, &quot;uint&quot;, 0x00000002)
wallpaperPath := StrGet(wszWallpaper, &quot;UTF-16&quot;)
If wallpaperPath != A_AppData &quot;\Microsoft\Windows\Themes\TranscodedWallpaper&quot; {
    If FileExist(wallpaperPath)
        Return wallpaperPath
    ; Else ; invalid path ; proceed to get correct path from the registry
    }
; Else ; path = C:\Users\&lt;UserName&gt;\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper
; proceed to get correct path from the registry

wallpaperPath := &quot;&quot; ; clear variable that stores path

; modified from AHK v1 code - https://gist.github.com/raveren/bac5196d2063665d2154#file-aio-ahk-L741
; This source has code for multi-monitor setups that is not included here.
; Look for `openWallpaperUnderMouse()` and `getMonitorUnderMouse()` functions over there if you need it.

; Read the binary value from the registry
regBinary := RegRead(&quot;HKEY_CURRENT_USER\Control Panel\Desktop&quot;, &quot;TranscodedImageCache&quot;) ; 1600 characters
; alternative: regBinary := RegRead(&quot;HKEY_CURRENT_USER\Control Panel\Desktop&quot;, &quot;TranscodedImageCache_000&quot;)

; remove first 48 characters and create array
regArr := StrSplit(SubStr(regBinary, 49))

Loop regArr.Length {
    char := Chr(&quot;0x&quot; regArr[A_Index + 2] regArr[A_Index + 3] regArr[A_Index] regArr[A_Index + 1])
            ; &quot;Word&quot; format = 4 numbers per character
            ; use &quot;0x&quot; [] [] [] [] instead of &quot;0x00&quot; [] [] to allow for converting Unicode characters

    If char = &quot;&quot;                ; char := Chr(&quot;0x&quot; 0 0 0 0) consecutive zeroes results in empty string
        Break                   ; End Loop
    Else {
        A_Index += 3            ; skip 3 subsequent characters - Loop A_Index 2 3 4, (not 5) 6 7 8, (not 9)…
        wallpaperPath .= char   ; add generated string to path - Chr(&quot;0x&quot; [3] [4] [1] [2]), Chr(&quot;0x&quot; [7] [8] [5] [6])… and so on
        }
    }
If FileExist(wallpaperPath)
    Return wallpaperPath        ; Return path to desktop wallpaper
Else {
    MsgBox( key &quot;:: WallpaperPath_v5() is not valid!&quot;   &quot;`n&quot;
        .   &quot;wallpaperPath: &quot; wallpaperPath             &quot;`n`n&quot;
        .   &quot;TranscodedImageCache:`n&quot; regBinary             ,, 262144) ; 262144 = Always-on-top
    Exit
    }
}

Example of message box containing wallpaper path -

For other iterations of this code, visit this AHK v2 script on GitHub.

Bonus Info
If you are looking for the location of Lock Screen images, visit this SuperUser question.
Note on 3rd party apps
When 3rd party apps like John's Background Switcher are used to manage desktop backgrounds (which I used on my older Win10 PC), they typically provide an option to view the current/previous desktop background (if set by the app itself). Check the app's help file to know more.

To activate Windows Photo Viewer in Windows 10, visit this article on HowToGeek.
To download default wallpapers from every Windows version, visit this article on XDA.
To download every Bing wallpaper in 4K, visit this page on GitHub.

**参考链接 / References**:
- N/A

---

#### 129. AltGr randomly stops working on windows 10

**问题描述 / Problem Description**:
Tags: windows-10, keyboard, keyboard-layout | Score: 163 | Views: 171925 | Answers: 7

**解决方案 / Solution**:
The issue happens when you open a RDP connection. Just bring the RDP window in foreground and press Alt+Enter.

The issue will disappear on all other windows too

Source: How to Fix Alt Gr Key Not Working.

**参考链接 / References**:
- N/A

---

#### 130. Combine/merge PDF files in Windows?

**问题描述 / Problem Description**:
Tags: windows, pdf, software-rec | Score: 162 | Views: 298746 | Answers: 9

**解决方案 / Solution**:
There are quite a few free options, as well as some good commercial ones:
Web-based (Free)

BCL Premium PDF Merge Merge 2 PDF documents. Max 10MB/file. Limit of 20 merges/day
MergePDF. Merge up to 10 files. Max limit of 5MB/file. (Registration required)

Desktop tools (free)

Booklet Creater. Merges files to create a booklet. Rearranges pages to that you can print and fold to create a simple booklet.

PDF Sam. Also known as &quot;PDF Split &amp; Merge&quot;. FOSS tool for splitting and merging PDFs. Windows &amp; Mac. Console and GUI interfaces. On Windows, the installer by default installs Ad-Aware Security Toolbar, sets Lavasoft SecureSearch as homepage, new tabs, and default search provider.

Swift PDF. Combines multiple images (JPG, GIF, etc.) into a single PDF.
Editor's note, 5/1/2017: Swift PDF was last updated in 2006 and was compatible with Windows 95.  The original link is dead and the product appears to no longer be supported.  However, it is still downloadable at https://swift-pdf.en.softonic.com/

pdftk. FOSS power tool. Command line only. Windows, Mac, Linux, FreeBSD. Windows GUI versions exist, including a portable version and the official free version.


There are also a lot of commercial tools.

**参考链接 / References**:
- N/A

---

#### 131. How to delete the Recovery Partition in Windows 10?

**问题描述 / Problem Description**:
Tags: windows, windows-10, partitioning, recovery-partition | Score: 161 | Views: 538902 | Answers: 4

**解决方案 / Solution**:
There is plenty of space on the disk. You are getting this error for a different reason. If your machine is anything but a desktop then you would get the error you have.
https://technet.microsoft.com/library/354e5163-f388-4354-984c-ea4e4206694c
You aren't able to delete the recovery partition because it EFI protected. You should be able to force by using the override command.
https://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx
I would try using diskpart (from an elevated command prompt) to delete the partition.
DISKPART&gt; list disk
DISKPART&gt; select disk 4

Disk 4 is now the selected disk.

DISKPART&gt; list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    Primary            223 GB  1024 KB
  Partition 3    Recovery           450 MB   223 GB
  
DISKPART&gt; select partition 3

Partition 3 is now the selected partition.

DISKPART&gt; list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    Primary            223 GB  1024 KB
* Partition 3    Recovery           450 MB   223 GB
  
DISKPART&gt; delete partition override

DiskPart successfully deleted the selected partition.

DISKPART&gt; list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    Primary            223 GB  1024 KB

After that you should be able to convert to dynamic disk.
Usually I re-purpose drives so I don't worry about data loss, but back up your data and use a desktop.

**参考链接 / References**:
- N/A

---

#### 132. How can the font size be changed in Notepad++?

**问题描述 / Problem Description**:
Tags: windows, fonts, notepad++ | Score: 161 | Views: 300740 | Answers: 9

**解决方案 / Solution**:
Ctrl and NUMPAD +/NUMPAD - or mouse wheel to zoom in/out

Edit: Or to achieve exactly what you asked for...

Settings > Style Configurator. Under Font Style you can set the font and size

**参考链接 / References**:
- N/A

---

#### 133. Windows Disk I/O 100% at boot for 20 Minutes

**问题描述 / Problem Description**:
Tags: windows, hard-drive, boot | Score: 161 | Views: 260129 | Answers: 3

**解决方案 / Solution**:
You can disable the scheduled tasks that starts CompatTelTunner.exe by looking in the Task Scheduler.
Computer Management – System Tools – Task Schedule Library – Microsoft – Windows – Application Experience
or
Start - Run - taskschd.msc
Name: Microsoft Compatibility Appraiser
Location: \Microsoft\Windows\Application Experience
Collects program telemetry information if opted-in to the Microsoft Customer Experience Improvement Program.
Right click on “Microsoft Compatibility Appraiser” and select “Disable”
By default, it is set to start if there is ANY network connection.

The executable is located here:
C:\Windows\System32\CompatTelRunner.exe  

You may also want to look at the following:
Customer Experience Improvement Program states


  If the user has consented to participate in the Windows
  Customer Experience Improvement Program, this job collects and sends
  usage data to Microsoft. However, it is set to run even if opted out
  Siuf (under Feedback)

**参考链接 / References**:
- N/A

---

#### 134. Why are there no odd Windows process IDs?

**问题描述 / Problem Description**:
Tags: windows, process | Score: 161 | Views: 20929 | Answers: 1

**解决方案 / Solution**:
&quot;Why are there no odd Windows process Ids?&quot;

The same code that allocates kernel handles is also used to
allocate process and thread IDs. Since kernel handles are a multiple
of four, so too are process and thread IDs.


Why are process and thread IDs multiples of four?

On Windows NT-based operating systems, process and thread IDs happen
always to be a multiple of four. Is this just a coincidence?
Yes, it's just a coincidence, and you shouldn't rely on it since it is
not part of the programming contract. For example, Windows 95 process
and thread IDs were not always multiples of four. (By comparison, the
reason that kernel handles are always a multiple of four is part of
the specification and will be guaranteed for the foreseeable future.)
Process and thread IDs are multiples of four as a side-effect of code
re-use. The same code that allocates kernel handles is also used to
allocate process and thread IDs. Since kernel handles are a multiple
of four, so too are process and thread IDs. This is an implementation
detail, so don't write code that relies on it. I'm just telling you to
satisfy your curiosity.

Source Why are process and thread IDs multiples of four?

Why are kernel HANDLEs always a multiple of four?

Not very well known is that the bottom two bits of kernel HANDLEs are
always zero; in other words, their numeric value is always a multiple
of 4. Note that this applies only to kernel HANDLEs; it does not apply
to pseudo-handles or to any other type of handle (USER handles, GDI
handles, multimedia handles...) Kernel handles are things you can pass
to the CloseHandle function.
The availability of the bottom two bits is buried in the ntdef.h
header file:
//
// Low order two bits of a handle are ignored by the system and available
// for use by application code as tag bits.  The remaining bits are opaque
// and used to store a serial number and table index.
//

#define OBJ_HANDLE_TAGBITS  0x00000003L

That at least the bottom bit of kernel HANDLEs is always zero is
implied by the GetQueuedCompletionStatus function, which indicates
that you can set the bottom bit of the event handle to suppress
completion port notification. In order for this to work, the bottom
bit must normally be zero.
This information is not useful for most application writers, which
should continue to treat HANDLEs as opaque values. The people who
would be interested in tag bits are those who are implementing
low-level class libraries or are wrapping kernel objects inside a
larger framework.

Source Why are kernel HANDLEs always a multiple of four?

Further reading

The Old New Thing: Practical Development Throughout the Evolution of Windows by Raymond Chen (Principal Software Design Engineer at Microsoft).

**参考链接 / References**:
- N/A

---

#### 135. See available drives from Windows CLI?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 160 | Views: 761513 | Answers: 12

**解决方案 / Solution**:
&gt; wmic logicaldisk get caption

Caption
C:
D:
E:


if probably the easiest one. Doesn't need administrative privileges, doesn't return more or less than what's needed, etc.

If you want to use it in a script, then wrap it in for /f with the skip=1 option:

for /f "skip=1 delims=" %%x in ('wmic logicaldisk get caption') do @echo.%%x

**参考链接 / References**:
- N/A

---

#### 136. How to set the default program for opening files without an extension in Windows?

**问题描述 / Problem Description**:
Tags: windows, file-management | Score: 159 | Views: 121995 | Answers: 11

**解决方案 / Solution**:
With the command line:
assoc .=&quot;No_Extension&quot;
ftype &quot;No_Extension&quot;=&quot;C:\path\to\my editor.exe&quot; &quot;%1&quot;

Restart the computer for the changes to take effect.
To give credit, I learned this from the vim wikia here and here
Extra info:
Instead of &quot;C:\path\to\...&quot;, the following macros may be useful:

%SystemDrive% - drive windows is installed on, i.e. C:\
%ProgramFiles% - e.g. &quot;C:\Program Files\&quot;
%ProgramFiles(x86)% - e.g. &quot;C:\Program Files (x86)\&quot;

You will need to properly escape them though:
ftype &quot;No_Extension&quot;=^&quot;^%ProgramFiles(x86)^%\Notepad++\notepad++.exe^&quot; &quot;%1&quot;

To set the icon to be the same as .txt files (I didn't do this, since it automatically made the files' icons display as Notepad++ files):
assoc &quot;No_Extension&quot;\DefaultIcon=%SystemRoot%\System32\imageres.dll,-102

To undo, you can read the assoc /? or ftype /? information, e.g.:
ftype &quot;No_Extension&quot;=
assoc &quot;No_Extension&quot;\DefaultIcon=
assoc .=

**参考链接 / References**:
- N/A

---

#### 137. What is Windows&#39; equivalent of the &quot;which&quot; command in Unix? Is there an equivalent PowerShell command?

**问题描述 / Problem Description**:
Tags: windows, command-line, powershell, which | Score: 159 | Views: 119758 | Answers: 6

**解决方案 / Solution**:
Newer versions of Windows (I think Windows 2003 and up) have the where command:

C:\&gt;where ping
C:\Windows\System32\PING.EXE


And for PowerShell, explicitly add the .exe suffix:

PS C:\&gt;where.exe ping
C:\Windows\System32\PING.EXE

**参考链接 / References**:
- N/A

---

#### 138. Windows Linux Subsystem - Accessing Files outside of Ubuntu

**问题描述 / Problem Description**:
Tags: windows-10, bash, windows-subsystem-for-linux | Score: 157 | Views: 267627 | Answers: 8

**解决方案 / Solution**:
I'm not sure if I'm misunderstanding your question, but your ubuntu bash (top right window) should have access to your Windows-based disks under /mnt.  For example, on my machine /mnt/c/Users/Scott/Desktop is my Windows desktop and I can read/write files there from vi for ex.  I don't believe the opposite is true just yet.  That is, I don't think you can explore into your bash world from Windows explorer.

What I've been doing as a developer is to host projects on my d: and point the linux-based tools to that /mnt/d/projects/someproject/ folder.

Make sure you update your Windows builds periodically as they seem to be fixing a lot of issues with each build, especially around sym-links and crossing FS boundaries between Linux/Windows.

**参考链接 / References**:
- N/A

---

#### 139. How to prove the authenticity of a screenshot?

**问题描述 / Problem Description**:
Tags: windows, screen-capture, image-processing | Score: 156 | Views: 73561 | Answers: 14

**解决方案 / Solution**:
You cannot prove that. They were on your PC, fully under your control for some time. You could have tampered with them.  Therefore you cannot prove that you did not tamper with them.

If you need to set up a legally safe solution then look for an independent third party and a way to have them store information in such a way that you can only trigger a store or read (e.g., a screenshot on a Citrix server to a write-once location).

**参考链接 / References**:
- N/A

---

#### 140. Mass deleting files in Windows

**问题描述 / Problem Description**:
Tags: windows, file-management | Score: 156 | Views: 155701 | Answers: 14

**解决方案 / Solution**:
WARNING: if you have symlinks to directories then del will delete actual directories and not symlinks. Be very careful with this and do not run these commands unless you know there are no symlinks inside target directory.



I regularly need to delete lots of files and directories from a WinXP encrypted drive, typically around 22 GB of 500,000 files in 45,000 folders.

Deleting with Windows Explorer is rubbish because it wastes lots of time enumerating the files. I usually move the stuff I need to delete to C:\stufftodelete and have a deletestuff.bat batch file to rmdir /s/q C:\stufftodelete. This is scheduled to run at night, but sometimes I need to run it during the day so the quicker the better.

Here's the results of a quick time test of a small 5.85 MB sample of 960 files in 303 folders. I ran method 1 followed by method 2, then reset the test directories. 

Method 1  removes the files and directory structure in one pass: 

rmdir /s/q foldername


Method 2 has a first pass to delete files and outputs to nul to avoid the overhead of writing to screen for every singe file. A second pass then cleans up the remaining directory structure: 

del /f/s/q foldername &gt; nul
rmdir /s/q foldername



Method 1: 17.5s, 14.9s, 13.9s, 14.8s, 13.8s: average 14.98 seconds
Method 2: 14.3s, 12.1s, 11.7s, 14.2s, 11.8s: average 12.82 seconds


Here's results of another test using 404 MB of 19,521 files in 3,243 folders:


Method 1: 2 minutes 20 seconds
Method 2: 2 minutes 33 seconds


So there's not much in it, probably too close to judge on a single test.



Edit: I've retested with much more data, this is a typical case for me: 28.3 GB of 1,159,211 files in 146,918 folders:


Method 1: 2h 15m, 2h 34m: average: 2 hours 25 minutes
Method 2: 49m, 57m: average: 53 minutes


Wow, method 2 is nearly three times faster than method 1! I'll be updating my deletestuff.bat!

**参考链接 / References**:
- N/A

---

#### 141. How do I disable Aero Shake in Windows 7?

**问题描述 / Problem Description**:
Tags: windows-7, windows, aero | Score: 156 | Views: 54362 | Answers: 5

**解决方案 / Solution**:
The best way to do this is to use the Group Policy editor. Go into the start menu, type in gpedit.msc, and hit enter. When it comes up, go into User Configuration -> Administratrive Templates -> Desktop.

In here you'll see a settings called "Turn off Aero Shake window minimizing mouse gesture". Set this to enabled and no more Aero Shake.

Here's a picture of the Group Policy Editor, with the setting highlighted:



Another option is to edit a key in the registry. If you don't have Group Policy Editor for some reason (lower end Windows 7 edition), this might be your only option. There's a downloadable reg file that will handle this automatically from the How-To Geek.

**参考链接 / References**:
- N/A

---

#### 142. What Tiling Window Manager for Windows do you recommend?

**问题描述 / Problem Description**:
Tags: windows, window-manager, awesome-wm | Score: 156 | Views: 136682 | Answers: 3

**解决方案 / Solution**:
bug.n is nice, and Open Source. :-)

**参考链接 / References**:
- N/A

---

#### 143. Is there a shortcut command in Windows command prompt to get to the current user&#39;s home directory like there is in Linux?

**问题描述 / Problem Description**:
Tags: windows, windows-vista, command-line | Score: 154 | Views: 299074 | Answers: 14

**解决方案 / Solution**:
Yes, you can use %HOMEPATH%, and %HOMEDRIVE%. These contain the full path of the user's home directory (without drive letter), and the drive letter, respectively.

There are quite a few other useful variables available, such as %OS% (Operating System), or %WINDIR% (Windows system directory). See Wikipedia: Environment Variables for a list.



Notes:

Actually, things are a bit complicated (as usual). There is also%USERPROFILE%, which does contain the drive letter, and is usually the same directory as %HOMEPATH% plus %HOMEDRIVE%. 

The values of these variables, and which one is right for you, will depend on the Windows version and any changes by an administrator, as their values may be different (see e.g. the question Difference between profile and home path ).

**参考链接 / References**:
- N/A

---

#### 144. Hex editors for Windows?

**问题描述 / Problem Description**:
Tags: windows, hex-editor | Score: 154 | Views: 306981 | Answers: 9

**解决方案 / Solution**:
Free Hex Editor (frhed), small and fast.

**参考链接 / References**:
- N/A

---

#### 145. How do I find out command line arguments of a running program?

**问题描述 / Problem Description**:
Tags: windows-7, windows, command-line-arguments | Score: 152 | Views: 255178 | Answers: 8

**解决方案 / Solution**:
You can do it without Process Explorer, too, using Windows' WMI service.  Run the following from the command prompt:

WMIC path win32_process get Caption,Processid,Commandline


If you want to dump the output to a file (makes it a bit easier to read), use the /OUTPUT switch:

WMIC /OUTPUT:C:\Process.txt path win32_process get Caption,Processid,Commandline

**参考链接 / References**:
- N/A

---

#### 146. How to disable sticky corners in Windows 10

**问题描述 / Problem Description**:
Tags: multiple-monitors, mouse, windows-10 | Score: 152 | Views: 161275 | Answers: 11

**解决方案 / Solution**:
The thread
How to disable sticky corners in Windows 10?
from answers.microsoft.com treats this same problem :

When moving the mouse from the left monitor to to the top left of the
right monitor the 6 pixel corner will catch your mouse.
I have similar problem in windows 8.1 and changing
MouseCornerClipLength in registry to 0 from 6 and disable Corner
Navigation in Taskbar and Start menu properties helped.
Anyway in Win10 i can't find MouseCornerClipLength, Corner Navigation
disabled at all and adding same registry keys won't help.

The answer on June 4, 2015, by a Microsoft Support Engineer named Vijay B was :

We are aware of this issue and it is currently being investigated.
Stay tuned and we will update this thread when additional information
becomes available.
If any other posters experiencing this have not submitted this through
the Windows Feedback App, please do so. This article
http://answers.microsoft.com/en-us/insider/forum/insider_apps-insider_feedback/how-to-share-feedback-on-windows-10-technical/5e501781-a580-43e3-8926-40ae19343805 explains using the Windows Feedback App.

It seems that your only option is currently to wait for a future improvement,
or for some hacker to come up with the right hack.
Adding your voice to the Windows Feedback App might help.
[EDIT1] The open-source application Non Stick Mouse is said to offer
a solution in the case of multiple monitors.
The developer states:

What it does is hop the mouse over the sticking corners, as well as
the screen edges when moving windows. Thus it allows the dragging of
windows through screens without your mouse getting hijacked by the
Snap Assist.
[...]
This application does not read or write to any drive, it does not
access the registry or connect to the Internet.

Warning: It has been noted in the comments that
virustotal finds malware in the latest version of &quot;non stick mouse&quot;.
[EDIT2]
I have found a
source
that gives a solution for Windows 10 (which I'm unable to test now):

Disable Snap
In Settings &gt; System &gt; Multitasking, set Snap to Off.

Registry modification
Create and execute the following .reg file:
 Windows Registry Editor Version 5.00

 [HKEY_CURRENT_USER\Control Panel\Desktop]
 &quot;MouseMonitorEscapeSpeed&quot;=dword:00000001

 [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell\EdgeUI]
 &quot;MouseMonitorEscapeSpeed&quot;=-



[EDIT3] Microsoft might have finally disabled this in its
latest versions.

**参考链接 / References**:
- N/A

---

#### 147. Windows 10 Search not loading, showing blank window

**问题描述 / Problem Description**:
Tags: windows-10, windows-search | Score: 151 | Views: 53370 | Answers: 3

**解决方案 / Solution**:
This problem was the result of a temporary server-side malfunction on Microsoft's side. It has since been resolved, and affected systems should operate normally after a reboot.


  We are aware of a temporary server-side issue causing Windows search to show a blank box. This issue has been resolved for most users and in some cases, you might need to restart your device. We are working diligently to fully resolve the issue and will provide an update once resolved. 
  
  This issue was resolved at 12:00 PM PST. If you are still experiencing issues, please restart your device. In rare cases, you may need to manually end the SearchUI.exe or SearchApp.exe process via Task Manager. (To locate these processes, select CTRL + Shift + Esc then select the Details tab.)


- source

The problem seemed to be related to certain online-enabled features tied to the search menu, namely Bing Search and Cortana. Disabling these features allowed other features of the search menu to begin functioning again.

The following steps explain how to disable Bing Search and Cortana in the search menu.


Open Regedit and navigate to   HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search



 2. Right-click the Search icon and choose New > DWORD (32-bit) Value. Name the new value BingSearchEnabled


 3. Double-click the new BingSearchEnabled value to open its properties dialog. The number in the “Value data” box should already be 0—just ensure it’s still 0. Click OK to continue


 4. Below BingSearchEnabled, you should see  CortanaConsent. Double-click this value to open its properties dialog. Change its “Value Data” box to “0”.

If you don’t see CortanaConsent, create it by following the same steps you used to create BingSearchEnabled.



Restart Explorer.Exe or PC and allgood

Source How to Disable Bing in the Windows 10 Start Menu

**参考链接 / References**:
- N/A

---

#### 148. How can I unzip a .tar.gz in one step (using 7-Zip)?

**问题描述 / Problem Description**:
Tags: windows, tar, 7-zip | Score: 150 | Views: 295447 | Answers: 8

**解决方案 / Solution**:
Not really.  A .tar.gz or .tgz file really is two formats: .tar is the archive, and .gz is the compression.  So the first step decompresses, and the second step extracts the archive.

To do it all in one step, you need the tar program.  Cygwin includes this.

tar xzvf foobaz.tar.gz

; x = eXtract 
; z = filter through gZip
; v = be Verbose (show activity)
; f = filename


You could also do it "in one step" by opening the file in the 7-zip GUI: Open the .tar.gz file, double click the included .tar file, then extract those files to your location of choice.

There's a long running thread here of people asking/voting for one-step handling of tgz and bz2 files. The lack action thus far indicates it's not going to happen until someone steps and contributes meaningfully (code, money, something).

**参考链接 / References**:
- N/A

---

#### 149. Is it safe to delete from C:\Windows\Installer?

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-10, windows-xp, disk-space | Score: 149 | Views: 205679 | Answers: 9

**解决方案 / Solution**:
No, it's not. Windows Installer uses that to cache installation files for anything installed on the machine using Windows Installer. At a minimum, you could lose the ability to add or remove programs, at the worst, you may lose the ability to run some programs.

Since Windows Update can also deploy Windows Installer patches, you could also prevent your machine from receiving Windows and Office updates.

**参考链接 / References**:
- N/A

---

#### 150. Windows 10 &quot;Enable NTFS long paths policy&quot; option missing

**问题描述 / Problem Description**:
Tags: windows, windows-10, ntfs, filenames, windows-10-v1607 | Score: 149 | Views: 319508 | Answers: 2

**解决方案 / Solution**:
The value has moved from NTFS directly into Local Computer Policy &gt; Computer Configuration &gt; Administrative Templates &gt; System &gt; Filesystem in the RTM version of the Version 1607.

**参考链接 / References**:
- N/A

---

#### 151. How to set an alias in Windows Command Line?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 148 | Views: 448249 | Answers: 9

**解决方案 / Solution**:
As Christian.K said in his comment, the DOSKEY command can be used to define macros, which are  analogous to aliases.

doskey macroName=macroDefinition


Macro parameters are referenced in the definition via $ prefixed positions: $1 through $9 and $* for all.

See the doskey technet documentation, or type doskey /? or help doskey from the command line for more information.

But there are serious limitations with DOSKEY macros:


The macros only work on the interactive command line - they do not work within a batch script.
They cannot be used on either side of a pipe: Both someMacro|findstr '^' and dir|someMacro fail.
They cannot be used within a FOR /F commands: for /f %A in ('someMacro') do ... fails


The limitations are so severe that I rarely use DOSKEY macros.

Obviously you can create batch scripts instead of macros, and make sure the script locations are in your PATH. But then you must prefix each script with CALL if you want to use the script within another script.

You could create simple variable "macros" for long and oft used commands, but syntax is a bit awkward to type, since you need to expand the "macro" when you want to use it.

Definition:

set "cdMe=cd a_very_long_path"


Usage (from command line or script)

%cdMe%

**参考链接 / References**:
- N/A

---

#### 152. Setting and using variable within same command line in Windows cmd.exe

**问题描述 / Problem Description**:
Tags: windows, command-line, shell | Score: 148 | Views: 178646 | Answers: 5

**解决方案 / Solution**:
Note that cmd /C &quot;set &quot;EDITOR=vim&quot; &amp;&amp; echo %EDITOR%&quot; would not work.
Nor would cmd /C &quot;setlocal ENABLEDELAYEDEXPANSION &amp;&amp; set &quot;EDITOR=vim&quot; &amp;&amp; echo !EDITOR!&quot;
You would need:

the /V option, to enable delayed environment variable expansion using ! as delimiter.
no space between a command and the &amp;&amp; (or add quotes)

That is:
C:\&gt; cmd /V /C &quot;set EDITOR=vim&amp;&amp; echo '!EDITOR!'&quot;
'vim'
# or
C:\&gt; cmd /V /C &quot;set &quot;EDITOR=vim&quot; &amp;&amp; echo '!EDITOR!'&quot;
'vim'

As noted below by maoizm, it is cmd /V /C, not cmd /C /V (which would not work)


I can't think of any practical reason you'd ever actually want this within the context of a single command

Typically, you need this when you have to replace a value used multiple times in a long command line.
For instance, to deploy a file to Nexus (in multiple lines for readability):
cmd /v /c &quot;set g=com.agroup&amp;&amp; set a=anArtifact&amp;&amp; set v=1.1.0&amp;&amp; \
           mvn deploy:deploy-file -Dfile=C:\path\!a!-!v!.jar \
           -Dpackaging=jar -DgroupId=!g! -DartifactId=!a! -Dversion=!v! \
           -DrepositoryId=nexus 
           -Durl=http://myserver/nexus/content/repositories/my-repo/&quot;

Instead of having to replace group, artifact (used 2 times) and version in a long and complex command line, you can edit them at the beginning of said command. It is clearer/easier to manipulate and change the parameter values.

**参考链接 / References**:
- N/A

---

#### 153. Ubuntu crashes on windows: 0x80040326 Wsl error

**问题描述 / Problem Description**:
Tags: windows, ubuntu, windows-subsystem-for-linux | Score: 147 | Views: 37397 | Answers: 10

**解决方案 / Solution**:
I had a same problem, but just solved it.
Update your wsl system.
wsl --update

**参考链接 / References**:
- N/A

---

#### 154. How can I add an item to the &#39;new&#39; context menu?

**问题描述 / Problem Description**:
Tags: windows, context-menu | Score: 145 | Views: 171286 | Answers: 11

**解决方案 / Solution**:
One more thing:

If you want to add a file as a template for the new item, use

Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\.html\ShellNew]
"FileName"="html.html"


and then place the file (html.html) in:


For your own profile: %Userprofile%\Templates
For all users: %Allusersprofile%\Templates
For the whole system: %Systemroot%\ShellNew




One more detail: if you want to delete the "Windows Live Call" entry, use:

[-HKEY_CLASSES_ROOT\.wlcshrtctv2\LiveCall\ShellNew]

**参考链接 / References**:
- N/A

---

#### 155. How do you shutdown or restart a Windows computer over a Remote Desktop connection?

**问题描述 / Problem Description**:
Tags: windows, remote-desktop, reboot, remote-shutdown | Score: 143 | Views: 394745 | Answers: 5

**解决方案 / Solution**:
Open a command window (or Windows Key + R) and type the following...

...to restart:

shutdown /r /t 0 


...to shutdown:

shutdown /s /t 0

**参考链接 / References**:
- N/A

---

#### 156. What is the Windows equivalent of &quot;wc -l&quot;?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 143 | Views: 254623 | Answers: 4

**解决方案 / Solution**:
The Linux/Unix &quot;line count&quot; command, wc -l, has a Windows equivalent find /c /v &quot;&quot;.
How does this work?
According to Raymond Chen of the The Old New Thing, this functions as such since

It is a special quirk of the find command that the null string is treated as never matching.

The inverted (/v) count (/c) thus effectively counts all the lines;
hence, the line count.
Example usage
To count the number of modified files in a subversion working copy:
svn status -q | find /c /v &quot;&quot;

Such a command can be used to mark a build as &quot;dirty&quot; if the count is not 0, i.e. there are uncommitted changes in the working copy.
To obtain a line count of all your Java files:
(for /r %f in (*.java) do @type &quot;%f&quot;) | find /c /v &quot;&quot;

The command find /c /v &quot;&quot; can also be added to a batch file if required. 
Remember to duplicate the % characters (%%f) in batch files.

PowerShell
A working PowerShell equivalent is Measure-Object -line — some additional formatting is required though, e.g. a directory listing for simplicity:
(ls | Measure-Object -line).Lines

**参考链接 / References**:
- N/A

---

#### 157. Why do damaged hard drives freeze the entire system?

**问题描述 / Problem Description**:
Tags: windows, hard-drive, freeze, bad-sectors | Score: 143 | Views: 84805 | Answers: 4

**解决方案 / Solution**:
This is one of those areas where SATA is suboptimal. The problem is at the storage device interconnect protocol level, and thus not related to what software you are running. Using another file copier or another operating system won't magically make things better, except that it might try to set different timeout values to reduce the impact of the problem (which may or may not be possible depending on the hardware and firmware; see below).

There are a few important points here:


With SATA, if the drive stops responding, this can tie up the whole storage system, not just the one drive that is having problems. It certainly has the potential to tie up the whole controller, and since most consumer systems have only a single disk controller (the one integrated on the motherboard), this means all storage. It's even worse if the drive fails in some non-standard and/or unexpected way, which can certainly happen if the drive is marginal. You may be interested in How can a single disk in a hardware SATA RAID-10 array bring the entire array to a screeching halt? on Server Fault.
Most consumer SATA drives have long default timeout periods (on the order of minutes) and many consumer SATA drives lack configurable error recovery control. So-called "NAS" drives often have configurable ERC, and high-end drives virtually always do; such drives may also have shorter default timeouts (7 seconds being a common value). Long timeout periods are advantageous if the drive holds the only copy of the data, which unfortunately is common on consumer systems; they are a disadvantage in a redundant configuration or where you simply want to get as much as possible off the drive before it deteriorates further.
A drive will keep trying to read a bad sector until it reaches its timeout threshold or until an abort is signalled by the host. Since the SATA bus can be tied up by the wait for the read to finish, it might not be possible for the OS to signal a storage-level command abort, and in extreme cases, drives might not even respond well to a SATA bus reset in such a situation.


Point #1 is one of the main selling points for SAS on servers; SAS has significantly better error handling than SATA. Point #2 is a drive firmware limitation, and #3 becomes a problem really only because of #2.

So what happens is that the OS issues a "read sectors" command to the disk, and the particular sectors are somehow damaged. Thus, the disk goes into retry mode to try to get the data off the platters, trying the read again and again until it gets good enough data that the disk's own error correction (FEC) is able to correct for the remaining errors. If you are unlucky, this might be never, but the drive will keep trying for some fairly long period of time before deciding that this read isn't going to succeed.

Because the operating system is waiting for the read, this will at the very least slow down the copying process to a crawl, and depending on the exact OS architecture can cause the OS to become jerky or even freeze for the duration. The disk, at this point, is busy with the original read and won't respond to further read commands until the one that is currently executing ends (successfully or unsuccessfully), and other software generally won't do better than the operating system it is running on.

Hence, anything that triggers a read elsewhere (ideally, only on the damaged drive) is going to have to wait in line until the damaged drive either successfully reads the sector in question, or determines that it cannot be read. Because of SATA's less than optimal handling of nonresponsive drives, this can mean that not only the drive you are copying from is going to have its I/O delayed. This can very easily cause other software to become slow or unresponsive as well, as that software waits for a different I/O request to finish, even if the operating system is able to cope.

It's also important to note here that disk I/O can happen even though you aren't explicitly accessing any files on disk. The two main causes for this would be load-on-demand executable code, and swap. Since swap is sometimes used even when the system is not under memory pressure, and load-on-demand executable code is common on modern systems and with modern executable file formats, unintended disk read activity during normal use is a very real possibility.

As pointed out in a comment to the question by Matteo Italia, one mitigative strategy is to use a different storage interconnect, which is a complicated way of saying "put the disk in a USB enclosure". By abstracting through the USB mass storage protocol, this isolates the problematic SATA portion from the rest of your system, which means that in theory, only I/O on that specific disk should be affected by I/O problems on that disk.

As a bit of an aside, this is pretty much why SATA (particularly, SATA without drive-level ERC) is often discouraged for RAID (especially RAID levels with redundancy, which among the standard ones is all except RAID 0); the long timeout periods and poor error handling can easily cause a whole device to be thrown out of the array for a single bad sector, which the RAID controller could handle just fine if redundancy exists and the storage controller simply knows that this is the problem. SAS was designed for large storage arrays, and thus with the expectation that there will be problems on various drives occasionally, which led to it being designed to handle the case of a single problematic drive or I/O request gracefully even if the drive doesn't. Problematic disks are not very common in consumer systems simply because those tend to not have many disks installed, and the ones that are installed virtually never have redundancy; since SATA aimed to replace PATA/IDE not SCSI (the latter being the niche SAS aimed for), it is likely that its error handling features and demands (or guarantees) were considered adequate for its intended use case.

**参考链接 / References**:
- N/A

---

#### 158. Map capslock to control in Windows 10

**问题描述 / Problem Description**:
Tags: keyboard-layout, windows-10, remapping, key-binding, capslock | Score: 143 | Views: 239495 | Answers: 13

**解决方案 / Solution**:
In case anyone needed this done via PowerShell:
$hexified = &quot;00,00,00,00,00,00,00,00,02,00,00,00,1d,00,3a,00,00,00,00,00&quot;.Split(',') | % { &quot;0x$_&quot;};
$kbLayout = 'HKLM:\System\CurrentControlSet\Control\Keyboard Layout';    
New-ItemProperty -Path $kbLayout -Name &quot;Scancode Map&quot; -PropertyType Binary -Value ([byte[]]$hexified);

Run it as Administrator and reboot.

**参考链接 / References**:
- N/A

---

#### 159. Can you zip a file from the command prompt using ONLY Windows&#39; built-in capability to zip files?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch, zip | Score: 142 | Views: 499677 | Answers: 12

**解决方案 / Solution**:
Here is an all batch file solution (a variation of my other answer) that will zip a file named c:\ue_english.txt and put it in C:\someArchive.zip:

set FILETOZIP=c:\ue_english.txt

set TEMPDIR=C:\temp738
rmdir %TEMPDIR%
mkdir %TEMPDIR%
xcopy /s %FILETOZIP% %TEMPDIR%

echo Set objArgs = WScript.Arguments &gt; _zipIt.vbs
echo InputFolder = objArgs(0) &gt;&gt; _zipIt.vbs
echo ZipFile = objArgs(1) &gt;&gt; _zipIt.vbs
echo CreateObject("Scripting.FileSystemObject").CreateTextFile(ZipFile, True).Write "PK" ^&amp; Chr(5) ^&amp; Chr(6) ^&amp; String(18, vbNullChar) &gt;&gt; _zipIt.vbs
echo Set objShell = CreateObject("Shell.Application") &gt;&gt; _zipIt.vbs
echo Set source = objShell.NameSpace(InputFolder).Items &gt;&gt; _zipIt.vbs
echo objShell.NameSpace(ZipFile).CopyHere(source) &gt;&gt; _zipIt.vbs
echo wScript.Sleep 2000 &gt;&gt; _zipIt.vbs

CScript  _zipIt.vbs  %TEMPDIR%  C:\someArchive.zip

pause


Write access is required to the parent of the folder stored in TEMPDIR. As this is often not the case for the root of drive C TEMPDIR may have to be changed.

Write access is also required for the folder the .bat script is in (as it generates a file there).

Also, please note that the file extension for the compressed file must be .zip. Attempts to use another extension may result in a script error. Instead, generate the .zip file and rename it.

**参考链接 / References**:
- N/A

---

#### 160. How can I mass rename files?

**问题描述 / Problem Description**:
Tags: windows, command-line, file-management | Score: 141 | Views: 402252 | Answers: 24

**解决方案 / Solution**:
I know in your title you say "in dos" but I get the impression you are just looking for a way to do this and are wondering if that is the best way.

The absolute best tool I have found for this is Bulk Rename Utility.  



It isn't a command line tool, but they do have a command line version if you really want to use it that way.

I've used the GUI version a lot, and it is very powerful, very fast and extremely easy to use.

Oh, and it is FREE for personal use.

**参考链接 / References**:
- N/A

---

#### 161. Restart a Windows service from the command line

**问题描述 / Problem Description**:
Tags: windows-7, windows, command-line | Score: 140 | Views: 754896 | Answers: 6

**解决方案 / Solution**:
You can use net stop [service name] to stop it and net start [service name] to start it up again basically restarting the service.

To combine them just do this - net stop [service name] &amp;&amp; net start [service name].



There is also a command built specifically for messing with services: sc


DESCRIPTION:
        SC is a command line program used for communicating with the
        Service Control Manager and services.
USAGE:
        sc  [command] [service name]  ...


        The option  has the form "\\ServerName"
        Further help on commands can be obtained by typing: "sc [command]"
        Commands:
          query-----------Queries the status for a service, or
                          enumerates the status for types of services.
          queryex---------Queries the extended status for a service, or
                          enumerates the status for types of services.
          start-----------Starts a service.
          pause-----------Sends a PAUSE control request to a service.
          interrogate-----Sends an INTERROGATE control request to a service.
          continue--------Sends a CONTINUE control request to a service.
          stop------------Sends a STOP request to a service.
          config----------Changes the configuration of a service (persistent).
          description-----Changes the description of a service.
          failure---------Changes the actions taken by a service upon failure.
          failureflag-----Changes the failure actions flag of a service.
          sidtype---------Changes the service SID type of a service.
          privs-----------Changes the required privileges of a service.
          managedaccount--Changes the service to mark the service account
                          password as managed by LSA.
          qc--------------Queries the configuration information for a service.
          qdescription----Queries the description for a service.
          qfailure--------Queries the actions taken by a service upon failure.
          qfailureflag----Queries the failure actions flag of a service.
          qsidtype--------Queries the service SID type of a service.
          qprivs----------Queries the required privileges of a service.
          qtriggerinfo----Queries the trigger parameters of a service.
          qpreferrednode--Queries the preferred NUMA node of a service.
          qrunlevel-------Queries the run level of a service.
          qmanagedaccount-Queries whether a services uses an account with a
                          password managed by LSA.
          qprotection-----Queries the process protection level of a service.
          delete----------Deletes a service (from the registry).
          create----------Creates a service. (adds it to the registry).
          control---------Sends a control to a service.
          sdshow----------Displays a service's security descriptor.
          sdset-----------Sets a service's security descriptor.
          showsid---------Displays the service SID string corresponding to an arbitrary name.
          triggerinfo-----Configures the trigger parameters of a service.
          preferrednode---Sets the preferred NUMA node of a service.
          runlevel--------Sets the run level of a service.
          GetDisplayName--Gets the DisplayName for a service.
          GetKeyName------Gets the ServiceKeyName for a service.
          EnumDepend------Enumerates Service Dependencies.

        The following commands don't require a service name:
        sc   
          boot------------(ok | bad) Indicates whether the last boot should
                          be saved as the last-known-good boot configuration
          Lock------------Locks the Service Database
          QueryLock-------Queries the LockStatus for the SCManager Database
EXAMPLE:
        sc start MyService

QUERY and QUERYEX OPTIONS:
        If the query command is followed by a service name, the status
        for that service is returned.  Further options do not apply in
        this case.  If the query command is followed by nothing or one of
        the options listed below, the services are enumerated.
    type=    Type of services to enumerate (driver, service, all)
             (default = service)
    state=   State of services to enumerate (inactive, all)
             (default = active)
    bufsize= The size (in bytes) of the enumeration buffer
             (default = 4096)
    ri=      The resume index number at which to begin the enumeration
             (default = 0)
    group=   Service group to enumerate
             (default = all groups)

SYNTAX EXAMPLES
sc query                - Enumerates status for active services & drivers
sc query eventlog       - Displays status for the eventlog service
sc queryex eventlog     - Displays extended status for the eventlog service
sc query type= driver   - Enumerates only active drivers
sc query type= service  - Enumerates only Win32 services
sc query state= all     - Enumerates all services & drivers
sc query bufsize= 50    - Enumerates with a 50 byte buffer
sc query ri= 14         - Enumerates with resume index = 14
sc queryex group= ""    - Enumerates active services not in a group
sc query type= interact - Enumerates all interactive services
sc query type= driver group= NDIS     - Enumerates all NDIS drivers

**参考链接 / References**:
- N/A

---

#### 162. Keyboard shortcuts to arrange Chrome tabs on Windows?

**问题描述 / Problem Description**:
Tags: windows, google-chrome, keyboard, keyboard-shortcuts | Score: 140 | Views: 67229 | Answers: 8

**解决方案 / Solution**:
Ctrl+Shift+PgUp
Ctrl+Shift+PgDn

**参考链接 / References**:
- N/A

---

#### 163. What is the difference between SETX and SET in environment variables in Windows

**问题描述 / Problem Description**:
Tags: windows, environment-variables | Score: 140 | Views: 159899 | Answers: 4

**解决方案 / Solution**:
I'm afraid it's not quite that simple. Environment variables are not limited by scope, as you suggest, but you are right that the lifetime of the value in the variable is different when comparing the verbs. 

set modifies the current shell's (the window's) environment values, and the change is available immediately, but it is temporary.  The change will not affect other shells that are running, and as soon as you close the shell, the new value is lost until such time as you run set again. 

setx modifies the value permanently, which affects all future shells, but does not modify the environment of the shells already running.  You have to exit the shell and reopen it before the change will be available, but the value will remain modified until you change it again. 

See here for an example: http://batcheero.blogspot.com/2008/02/set-and-setx.html

**参考链接 / References**:
- N/A

---

#### 164. Delete all files from a folder and its sub folders

**问题描述 / Problem Description**:
Tags: windows, script, powershell, batch-file, vbscript | Score: 139 | Views: 555882 | Answers: 16

**解决方案 / Solution**:
Short and sweet PowerShell.  Not sure what the lowest version of PS it will work with.
Remove-Item c:\Tmp\* -Recurse -Force

**参考链接 / References**:
- N/A

---

#### 165. Disable Narrator shortcut key in Windows

**问题描述 / Problem Description**:
Tags: windows, windows-8, hotkeys | Score: 139 | Views: 180666 | Answers: 11

**解决方案 / Solution**:
I have not tried it personally but here's what I found.

Navigate to %systemroot%\System32
In this folder a file called Narrator.exe is to be found
Right click the file and choose Properties
Choose the Security tab and press Advanced
In the top of the window press Change to change the Owner permissions
In the text field write your username and press OK to all the dialogs

Now you should be able to change the permissions of the file, this is where we remove all the permissions from your user and change the owner back to SYSTESM; this way your user will not be able to start the Narrator.

Right-click the Narrator file again and choose Properties and Security
Press Advanced
Now that you are the owner you can change permissions for other users. Choose your own user and press Edit
Remove the Read &amp; Execute and Read permissions and press OK
Now press Change in the top under Owner and write system in the text field
Press OK to all dialogs

Source

**参考链接 / References**:
- N/A

---

#### 166. How to move the recovery partition on Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, diskpart | Score: 139 | Views: 268011 | Answers: 5

**解决方案 / Solution**:
According to MS's documentation, capture-and-apply-windows-system-and-recovery-partitions, the recovery partition can be captured and applied to a new partition. I have made it to work on my windows 10 PC.
Warning 1: You must know what the following commands do before you execute them. Check the link above and MS's documentation for diskpart, dism and reagentc.
Warning 2: Check disk numbers, partition numbers and volume letters carefully before executing commands.

Use diskpart to find current recovery partition and assign a driver letter(eg. O) to it:

DISKPART&gt; list disk
DISKPART&gt; select disk &lt;the-number-of-disk-where-current-recovery-partition-locate&gt;
DISKPART&gt; list partition
DISKPART&gt; select partition &lt;the-number-of-current-recovery-partition&gt;
DISKPART&gt; assign letter=O


Create an image file from current recovery partition:

Dism /Capture-Image /ImageFile:C:\recovery-partition.wim /CaptureDir:O:\ /Name:&quot;Recovery&quot;


Apply the created image file to another partition(eg. N) that will become the new recovery partition:

Dism /Apply-Image /ImageFile:C:\recovery-partition.wim /Index:1 /ApplyDir:N:\


Register the location of the recovery tools:

reagentc /disable
reagentc /setreimage /path N:\Recovery\WindowsRE
reagentc /enable


Use diskpart to hide the recovery partition:

For UEFI:

DISKPART&gt; select volume N
DISKPART&gt; set id=&quot;de94bba4-06d1-4d40-a16a-bfd50179d6ac&quot;
DISKPART&gt; gpt attributes=0x8000000000000001
DISKPART&gt; remove


For BIOS:

DISKPART&gt; select volume N
DISKPART&gt; set id=27
DISKPART&gt; remove


Reboot the computer, now the new recovery partition should be working
(Optional) Delete the old recovery partition:

DISKPART&gt; select volume O
DISKPART&gt; delete partition override


(Optional) Check if the recovery partition is working:

Show the current status:
reagentc /info


Specifies that Windows RE starts automatically the next time the system starts:
reagentc /boottore


Reboot the computer and do your stuff in Windows RE (eg. enter CMD and run some tools)

**参考链接 / References**:
- N/A

---

#### 167. Where does Putty store known_hosts information on Windows?

**问题描述 / Problem Description**:
Tags: windows, ssh, putty, known-hosts | Score: 138 | Views: 202114 | Answers: 3

**解决方案 / Solution**:
Putty stores known hosts under a registry key:  HKEY_CURRENT_USER\SoftWare\SimonTatham\PuTTY\SshHostKeys.

**参考链接 / References**:
- N/A

---

#### 168. Why can&#39;t VirtualBox or VMware run with Hyper-V enabled on Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, virtualbox, virtual-machine, virtualization, vmware | Score: 137 | Views: 170569 | Answers: 4

**解决方案 / Solution**:
VirtualBox and VMware Workstation (and VMware Player) are "level 2 hypervisors." Hyper-V and VMware ESXi are "level 1 hypervisors."

The main difference is that a level 2 hypervisor is an application running inside an existing OS, while a level 1 hypervisor is the OS itself.

This means that when you enable Hyper-V, your Windows 10 "host" becomes a virtual machine. A special one, but nonetheless a virtual machine.

So your question would more aptly be: "Why don't VirtualBox and VMware Workstation work inside a Hyper-V virtual machine?" One can answer because as a VM, the Intel VT-X instruction are no longer accessible from your virtual machine, only the host has access to it.

QEMU works because it does not do virtualization but emulation, which is completely different and explains why QEMU is painfully slow. Virtualization is the process of running a complete isolated machine inside another, but with the help of the processor. This requires the virtual machine and the host to be instruction compatible.

Emulation is the process of running any machine inside a running OS, there is no platform restriction, and is why QEMU can run an ARM machine on an amd64 platform.

Note: QEMU has 2 operating modes:


it can work as an emulator, this is the mode explained above
it can work as virtualization software with the help of KVM if the guest architecture is compatible with the host's and if the VT instruction is present of course.

**参考链接 / References**:
- N/A

---

#### 169. How to open a .tar.gz file in Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-7, tar, gz | Score: 136 | Views: 691920 | Answers: 10

**解决方案 / Solution**:
You can use 7-zip to untar the .tar file as well. 


Right-click the file
Select 7-zip -> Extract Here / Extract To

**参考链接 / References**:
- N/A

---

#### 170. How do I install a VSIX file in Visual Studio?

**问题描述 / Problem Description**:
Tags: windows, visual-studio-2010, visual-studio | Score: 136 | Views: 417791 | Answers: 11

**解决方案 / Solution**:
VSIX is a Visual Studio extension installer.  You must have Visual Studio 2010 or newer in order to install them, but you should be able to install it by double-clicking the .vsix file.  Alternatively you should be able to install it from within the VS Extension Manager (Tools->Extension Manger)

See more about VSIX files at Quan To's Visual Studio Extensibility blog

**参考链接 / References**:
- N/A

---

#### 171. Recursively delete empty directories in Windows

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 135 | Views: 240097 | Answers: 13

**解决方案 / Solution**:
You can use Remove Empty Directories utility.

Alternatively you can use this one-liner batch file (from DownloadSquad):

for /f "delims=" %d in ('dir /s /b /ad ^| sort /r') do rd "%d"


(if used inside a batch file, replace %d with %%d)

This works because rd will not remove a directory that contains files.

**参考链接 / References**:
- N/A

---

#### 172. How can I open a command prompt in current folder with a keyboard shortcut?

**问题描述 / Problem Description**:
Tags: windows, command-line, keyboard-shortcuts, autohotkey | Score: 133 | Views: 308592 | Answers: 12

**解决方案 / Solution**:
Press Alt+D, type cmd and press Enter. For more details see blog post here.

**参考链接 / References**:
- N/A

---

#### 173. A command-line or batch cmd to concatenate multiple files

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 133 | Views: 697261 | Answers: 6

**解决方案 / Solution**:
I don't want to type the name of all
  files.


That's easy to be avoided. Open a command prompt in this folder and type the following command:

copy /b *.txt newfile.txt


Press Enter.

Now you will have all text files in this folder ordered by date ascending merged into a single file called newfile.txt.


  My ultimate aim is to store the
  contents of each text file in a separate
  column of an Excel sheet.


Here's a tutorial that may help you to achieve your "ultimate aim":

Merge all CSV or TXT files in a folder in one worksheet

**参考链接 / References**:
- N/A

---

#### 174. Run a script on start up on Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, boot | Score: 133 | Views: 548126 | Answers: 6

**解决方案 / Solution**:
The startup folder is still there and functions as normal.

To access it, press Windows+R, then type shell:startup.

You should be able to do what you were previously doing in Windows 7 from there.

**参考链接 / References**:
- N/A

---

#### 175. How to prevent Windows 10 waking from sleep when traveling in bag?

**问题描述 / Problem Description**:
Tags: windows-10, sleep, hibernate, windows-task-scheduler | Score: 133 | Views: 132715 | Answers: 10

**解决方案 / Solution**:
This has worked for me so far. Go to:
Control Panel\Hardware and Sound\Power Options\Edit Plan Settings
Click &quot;Change advanced power settings&quot;
Go to &quot;Sleep-&gt;Allow wake timers&quot; and change the setting to Disable.

UPDATE: As Erik pointed out, there can be two options:

Disable them both.
UPDATE #2:
In addition to wake timers, peripheral devices can also wake your computer. See Rosdi's answer for network interfaces. It reminded me of something I had to change recently as my computer was waking again when peripherals were attached. First I disconnected the mouse, but it turned out to be the keyboard.
Open the Device Manager and expand Keyboards - or whatever your problematic device category is - and find the suspect, e.g. &quot;HID Keyboard Device&quot;. Right-click that and select Properties, then go to the Power Management tab and uncheck &quot;Allow this device to wake the computer&quot;.

**参考链接 / References**:
- N/A

---

#### 176. Change default action on connecting a USB device

**问题描述 / Problem Description**:
Tags: windows, usb | Score: 132 | Views: 354443 | Answers: 1

**解决方案 / Solution**:
Microsoft explains all about autoplay here.


Open AutoPlay by clicking the Start button , and then clicking Control Panel. In the search box, type autoplay, and then click AutoPlay. 
In the list next to the device or type of media, click the new action you want to use.

**参考链接 / References**:
- N/A

---

#### 177. Display the taskbar clock on multiple screens in Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-8, taskbar, clock | Score: 132 | Views: 196308 | Answers: 7

**解决方案 / Solution**:
You can't display the clock on both taskbar. It is possible to drag your primary taskbar to the second monitor providing they are unlocked first.

**参考链接 / References**:
- N/A

---

#### 178. How to set default user for manually installed WSL distro?

**问题描述 / Problem Description**:
Tags: linux, windows, user-accounts, windows-subsystem-for-linux | Score: 131 | Views: 257638 | Answers: 8

**解决方案 / Solution**:
There are a few possible methods of changing/setting the default user in an imported WSL instance.  While the two that were mentioned in other answers still work, there are two &quot;official&quot; ways now.
Method 1 - wsl --manage --set-default-user (WSL 2.4.10 and later)
As of February 2025, the latest release of WSL (2.4.10.0) includes a built-in flag for setting the default user. If needed, you can (assuming you are running on a release in the last few years) update via:
wsl --update

And then:
wsl --manage &lt;distro&gt; --set-default-user &lt;username&gt;

This queries the user id (via usr/bin/id and perhaps other methods) in the distribution and then sets the returned UID in the registry as in Method #3 below.  It does require that the username/id already exists. See the &quot;For readers who need to create a new user&quot; section below if needed.
Method 2 - /etc/wsl.conf
The current Microsoft recommended way of setting the username in an instance is to create a /etc/wsl.conf in the instance with the following setting:
[user]
default=username

Changing, of course, username to be your default username.
Exit your distro/instance, then issue a wsl --terminate &lt;distroname&gt; from PowerShell or CMD.  When you restart, the default user should be set.
This is safer and less error-prone than the registry-based methods.
Method 3 - Registry Key
Setting the registry key per @harrymc's answer.
Method 4 - LxRunOffline
Using LxRunOffline to set the registry entry, as described in @Jaime's answer.  Ultimately this has the same effect as Method 3 above.
Semi-method 5 - Runtime user selection via wsl commandline argument
The username can be selected when starting any WSL instance by:
wsl -u username or wsl -d distroname -u username, etc.
For instance, wsl -d Ubuntu -u root.

Side Note: This question was specifically about setting the default username in an imported instance.
However, for completeness, you can also set the default username for a distro that was installed from the Store (or wsl --install) with:
&lt;distro&gt;.exe config --default-user &lt;username&gt;

For instance, if you installed &quot;Ubuntu 20.04&quot; from the Store, you would use:
ubuntu2004.exe config --default-user &lt;username&gt;

The .exe here is an &quot;App Execution Alias&quot; in Windows.  You can check the name by going to &quot;Manage app execution aliases&quot; in the Windows System Settings.

For readers who need to create a new user
@ndemou made a good point in the comments last year that I, in hindsight, dismissed improperly.  Two other users have now mentioned in the comments that @ndemou's information was helpful.  My belated apologies!  Here's the additional information based on @ndemou's advice ...
Some users who find this answer may be starting up as root not because they --import'd a distribution, but possibly because the default user was never created during installation in the first place.  This can happen when the distribution installation is stopped prematurely, and likely for other reasons as well.
Under Ubuntu, the default distribution for WSL, you can create your user by starting with:
wsl ~ -u root

If you need to, add the -d &lt;distribution&gt; option.
Then run:
NEWUSER=&lt;your_username&gt;
useradd --create-home --shell /usr/bin/bash --user-group --groups  adm,dialout,cdrom,floppy,sudo,audio,dip,video,plugdev,netdev --password $(read -sp Password: pw ; echo $pw | openssl passwd -1 -stdin) $NEWUSER

Then set the user as the default using the /etc/wsl.conf as mentioned above.
If you've already created the user, or are using a different distribution, as @ndemou points out, make sure to also add the user either to a group that is in sudoers or directly to sudoers via visudo.  See the answers to this question for additional details.

**参考链接 / References**:
- N/A

---

#### 179. How can I shrink a Windows 10 partition?

**问题描述 / Problem Description**:
Tags: windows, hard-drive, partitioning, mirroring | Score: 131 | Views: 295566 | Answers: 13

**解决方案 / Solution**:
There seems to be absolutely no need for any third party software.

I have followed the instructions here, and I successfully shrank my OS partition in about 10 minutes.
Running under Windows 10, but I doubt it makes a difference here.

The steps are:


Disable hibernation.

At a an elevated (admin) command prompt, run the command

powercfg /h off

Disable pagefile.

Open the System page in Control Panel (from “This PC”/“My computer”, open the Properties). Click “Advanced System Settings”, then in the “System Properties” dialog's “Advanced” tab, open the “Performance” settings, go to the “Advanced” tab, click “Change...” under “Virtual memory”, untick “Automatically manage paging file size for all drives”, select the drive you want to shrink, select “No paging file” and click the “Set” button.
Disable system protection.

In the “System Properties” dialog as above, go to the “System Protection” tab, click “Configure...” and select “Disable system protection”.
Restart.


Now the three files that were preventing partition reduction are gone. Reduce partition size, and then restore the three items.

If Disk Management complains that “There is not enough space available on the disk(s) to complete this operation.” even though you entered a size that should work according to Disk Management's own figures, see Cannot shrink C: partition: Not enough space

I have later found similar instructions at other places, all of them mentioning only these 3 items.

**参考链接 / References**:
- N/A

---

#### 180. How to add command line options to shortcut?

**问题描述 / Problem Description**:
Tags: windows, windows-xp, shortcuts, command-line-arguments | Score: 130 | Views: 485255 | Answers: 4

**解决方案 / Solution**:
Have you tried to add in the Target field


"c:\path\to\exe\program.exe" -option1 -option2


Only the program path and name need to be enclosed in quotes.

**参考链接 / References**:
- N/A

---

#### 181. Unable to install fonts on Windows 10

**问题描述 / Problem Description**:
Tags: windows, fonts, windows-10, uac | Score: 129 | Views: 170795 | Answers: 2

**解决方案 / Solution**:
After a week of trying everything. The answer as weird as it sounds is to enable the windows firewall. I know, makes no sense right? It's not connected to font settings, however once "On" I was able to fix my issue with installing fonts on windows 10 and without an error message!

**参考链接 / References**:
- N/A

---

#### 182. How to make Outlook Calendar reminders stay on top in Windows 7

**问题描述 / Problem Description**:
Tags: windows, microsoft-outlook, calendar, popups, reminder | Score: 129 | Views: 234341 | Answers: 11

**解决方案 / Solution**:
I had the same problem with Outlook 2010. Use the steps mentioned below, it works like a charm. Don't forget to enable all macros: Trust Center > Macro Settings.


Create a Digital certificate for later: Hit Start and type
'certificate', select 'Digital Certificate for VBA Projects'
Enter a name for your certificate. Click OK. Open Outlook and hit Alt + F11 to
start the VBA editor. 
In the tree on the left, expand 'Microsoft Office Outlook Objects' and double click on 'ThisOutlookSession'
Paste in this code:

Private Declare PtrSafe Function FindWindowA Lib "user32" _
(ByVal lpClassName As String, ByVal lpWindowName As String) As Long

Private Declare PtrSafe Function SetWindowPos Lib "user32" ( _
ByVal hwnd As Long, ByVal hWndInsertAfter As Long, _
ByVal X As Long, ByVal Y As Long, ByVal cx As Long, _
ByVal cy As Long, ByVal wFlags As Long) As Long

Private Const SWP_NOSIZE = &amp;H1
Private Const SWP_NOMOVE = &amp;H2
Private Const FLAGS As Long = SWP_NOMOVE Or SWP_NOSIZE
Private Const HWND_TOPMOST = -1

Private Sub Application_Reminder(ByVal Item As Object)
Dim ReminderWindowHWnd As Variant
On Error Resume Next
ReminderWindowHWnd = FindWindowA(vbNullString, "1 Reminder")
SetWindowPos ReminderWindowHWnd, HWND_TOPMOST, 0, 0, 0, 0, FLAGS

End Sub

Sign the Macro so it will run: Tools > Digital Signature... and choose the certificate you created earlier
Close the VBA window
Enable all macros in File > Options > Trust Center > Trust Center Settings > Macro Settings

**参考链接 / References**:
- N/A

---

#### 183. View past notifications in Windows 10 and 11?

**问题描述 / Problem Description**:
Tags: windows, windows-10, windows-11, notifications, action-center | Score: 129 | Views: 304443 | Answers: 4

**解决方案 / Solution**:
tldr; No there's not.

The action center is the same as found on the Microsoft Phones running Windows 10 Mobile.  These actions (notifications) are meant to be displayed to the user until they take action.  There are two ways a user can interact with an action:


Dismiss the notification (clears the action)
Select the notification (respond to the action)


Once one of these interactions takes place, the notification and therefore the action is no longer displayed.  No history is maintained of these notifications and cannot be retrieved.  This is done on purpose as that history could (and most likely would) become very large.  

If you are worried that the notification has system-wide consequences it could be worth looking into the System logs instead; here separate messages about system events are stored.



Update: It appears that some applications will additionally add events into the event viewer.  This can be done by:


Open Event Viewer 
Expand Applications and Services Logs 
Drill down to the app or service you are interested in, e.g. for Windows Defender you might go to: Microsoft -&gt; Windows -&gt; Windows Defender -&gt; Operational log. 
Review the log and look for the notification you were interested in.


This is NOT the notification history, but additional information provided by the application and as such, there's no guarantee that the notification was logged.  It also requires that a user knows which application whose notification they're looking for.

**参考链接 / References**:
- N/A

---

#### 184. Set shortcuts to change keyboard layout in Windows 10

**问题描述 / Problem Description**:
Tags: keyboard, windows-10, keyboard-layout, input-languages | Score: 129 | Views: 367310 | Answers: 12

**解决方案 / Solution**:
Go to Control Panel → Clock, Language, and Region → Change input methods (under Language) → Advanced settings → Change language bar hot keys.

**参考链接 / References**:
- N/A

---

#### 185. Windows 10 Ubuntu Bash Shell: How Do I Mount Other Windows Drives?

**问题描述 / Problem Description**:
Tags: windows-10, bash, mount | Score: 129 | Views: 242241 | Answers: 6

**解决方案 / Solution**:
Good news, it is now possible to mount USB media (including formatted as FAT) and network shares with drvfs on Windows 10:

Mount removable media: (e.g. D:)

$ sudo mkdir /mnt/d
$ sudo mount -t drvfs D: /mnt/d


To safely unmount

$ sudo umount /mnt/d


You can also mount network shares without smbfs:

$ sudo mount -t drvfs '\\server\share' /mnt/share


You need at least Build 16176 so you might have to opt-in to the Windows Insider programm and then update Windows. Source: https://blogs.msdn.microsoft.com/wsl/2017/04/18/file-system-improvements-to-the-windows-subsystem-for-linux/

**参考链接 / References**:
- N/A

---

#### 186. How do I type the tick and backtick characters on Windows?

**问题描述 / Problem Description**:
Tags: windows, typing | Score: 128 | Views: 561545 | Answers: 14

**解决方案 / Solution**:
Backtick (grave accent)
QWERTY
Key that’s been marked with red border. It’s a dead key by default.



This also applies to the Slovak QWERTZ layout.

QWERTZ Germany &amp; Austria
Shift + Key that's been marked with red border




QWERTZ Switzerland
Shift + Key that's been marked with a red border




QWERTZ Czech Republic and South Slavic Latin (Bosnian, Croatian, Serbian, Slovene)
Alt Gr + Key that's been marked with red border




QWERTZ Hungary
Alt Gr + Key that's been marked with red border




AZERTY France
Alt Gr + Key that’s been marked with red border




AZERTY Belgium
Alt Gr + Key that’s been marked with red border




Forwardtick (acute accent)
AZERTY Belgium
Alt Gr + Key that’s been marked with red border




Alt codes
There may not be forwardtick keys available for the other keyboards, however an alt code exists (Hold left Alt and type the numbers on your num pad).
The below codes should work on any keyboard.

Alt + 96 = `
Alt + 0180 = ´
Alt + 39 = '

So if you want an ', you do the following: Hold left Alt, press
3, release 3 but still hold Alt, press
9, release 9, release Alt.
Unicode Character 'ACUTE ACCENT'

**参考链接 / References**:
- N/A

---

#### 187. What does &quot;delayed start&quot; do in startup type for a Windows service?

**问题描述 / Problem Description**:
Tags: windows, boot, windows-services | Score: 128 | Views: 321771 | Answers: 5

**解决方案 / Solution**:
A service marked as Automatic (Delayed Start) will start shortly after all other services designated as Automatic have been started. In my experience, this means that they are started 1-2 minutes after the computer boots.

The setting is most useful in lessening the "mad rush" for resources when a machine boots.

Note that when you have 20 services all being started at the same time, each will start up slower as it competes with the others for slices of the machine's precious resources (CPU/RAM/Disk/Network). That is, each service takes longer to become available!

If you have a few services that are critical, then you may want to set those few to Automatic and set as many of the others as you can to Automatic (Delayed Start). This will ensure that the critical services get the most resources early and become available sooner, while the non-critical services start a bit later (which by definition is ok).

**参考链接 / References**:
- N/A

---

#### 188. How can I SSH into &quot;Bash on Ubuntu on Windows 10&quot;?

**问题描述 / Problem Description**:
Tags: windows-10, bash, ssh, windows-10-v1607, windows-subsystem-for-linux | Score: 128 | Views: 232533 | Answers: 5

**解决方案 / Solution**:
I got it to work; here's how.

Uninstalled ssh-server, reinstalled it and made sure it's started with

sudo service ssh --full-restart


Make sure you turned off root access and added another user in the config file.

I was able to connect to the subsystem on 127.0.0.1:22 as expected. 
I hope this will help you.




sudo apt-get purge openssh-server
sudo apt-get install openssh-server
sudo nano /etc/ssh/sshd_config and disallow root login by setting PermitRootLogin no
Then add a line beneath it that says:

AllowUsers yourusername

and make sure PasswordAuthentication is set to yes if you want to login using a password.
Disable privilege separation by adding/modifying : UsePrivilegeSeparation no
sudo service ssh --full-restart
Connect to your Linux subsystem from Windows using a ssh client like PuTTY.

**参考链接 / References**:
- N/A

---

#### 189. Should I defragment my SSD?

**问题描述 / Problem Description**:
Tags: windows-10, ssd, defragment | Score: 128 | Views: 73296 | Answers: 8

**解决方案 / Solution**:
Let Windows do its job. Once per month it does a real full defrag, also on a SSD, to optimize the internal meta data.


  The short answer is, yes, Windows does sometimes defragment SSDs, yes,
  it's important to intelligently and appropriately defrag SSDs, and
  yes, Windows is smart about how it treats your SSD.


Here is a reply from Microsoft:


  Storage Optimizer will defrag an SSD once a month if volume snapshots are enabled. This is by design and necessary due to slow
  volsnap copy on write performance on fragmented SSD volumes. It’s
  also somewhat of a misconception that fragmentation is not a problem
  on SSDs. If an SSD gets too fragmented you can hit maximum file
  fragmentation (when the metadata can’t represent any more file
  fragments) which will result in errors when you try to write/extend a
  file. Furthermore, more file fragments means more metadata to process
  while reading/writing a file, which can lead to slower performance.
  
  As far as Retrim is concerned, this command should run on the schedule
  specified in the dfrgui UI. Retrim is necessary because of the way
  TRIM is processed in the file systems. Due to the varying performance
  of hardware responding to TRIM, TRIM is processed asynchronously by
  the file system. When a file is deleted or space is otherwise freed,
  the file system queues the trim request to be processed. To limit the
  peek resource usage this queue may only grow to a maximum number of
  trim requests. If the queue is of max size, incoming TRIM requests may
  be dropped. This is okay because we will periodically come through and
  do a Retrim with Storage Optimizer. The Retrim is done at a
  granularity that should avoid hitting the maximum TRIM request queue
  size where TRIMs are dropped.


So install Windows on the SSD and forget it. Windows will do everything on its own.

**参考链接 / References**:
- N/A

---

#### 190. How to access a BitLocker-encrypted drive in Linux?

**问题描述 / Problem Description**:
Tags: linux, windows, encryption, multi-boot, bitlocker | Score: 126 | Views: 493008 | Answers: 10

**解决方案 / Solution**:
You can access the BitLocker partition under Linux using Dislocker, an open-source driver that is using FUSE (or not).
Note: You need the file on a USB key (the one with the .bek extension) or the recovery password.

**参考链接 / References**:
- N/A

---

#### 191. How do I create a right-click context menu entry to open Git Bash at a given folder within ConEmu?

**问题描述 / Problem Description**:
Tags: windows, bash, git, conemu | Score: 126 | Views: 71770 | Answers: 6

**解决方案 / Solution**:
There are a number of ways this can be done in ConEmu as it is so highly configurable, but here's the way I do it.


In ConEmu, hit WinAltp to open the settings dialog.
Select the Tasks subsection under the Startup node and click the + icon to add a new 'Task'
In the Task Name field enter Git Bash, leave Task Parameters blank and add "C:\Program Files\Git\bin\sh.exe" --login -i to the Commands section. It should look something like this:





Now select the Integration node and enter the following under the ConEmu Here - Explorer menu integration section: 


Menu item: ConEmu Here [Git Bash]
Command: /single /cmd {Git Bash}
Icon file: C:\Program Files\Git\mingw64\share\git\git-for-windows.ico

Click the Register button




This should add an entry in your right-click context menu (complete with icon). In the Command field you can use any of the ConEmu.exe switches (worth checking out for more complete documentation of what you can do - it's pretty powerful).

Note: If you'd like a Git for Windows icon to appear at the top left of the ConEmu window, use the /icon switch; e.g.,

/icon "C:\Program Files\Git\mingw64\share\git\git-for-windows.ico" /single /cmd {Git Bash}


This only seems to work if it's the first tab open, though.

**参考链接 / References**:
- N/A

---

#### 192. How do I modify my Git Bash profile in Windows?

**问题描述 / Problem Description**:
Tags: windows, bashrc, .bash-profile, git-bash | Score: 125 | Views: 331804 | Answers: 6

**解决方案 / Solution**:
When you open up your Git Bash, you should be in your home directory by default.
Now create the .bashrc file (if on Windows&nbsp;7 the file should be named .bashrc.).

If you're not in the home directory, change into it by typing:


  cd


and pressing Enter. cd, without any other parameters listed after, will always return the home directory.

You can create the file by typing:


  touch .bashrc


Then edit it with Vim or you could try doing it with some Windows editor, but I don't recommend it, because of some text formatting issues.


  vim .bashrc


Change to Insert Mode by hitting the i key.

Add your alias by typing:


  alias gs='git status'


Exit the insert mode by hitting the Esc key.

Save and close your file by typing the following :wqEnter.

:wEnter will only save your file.

:q!Enter will quit the editor without saving your file.

Finally, update the file to use your new changes by typing:


  source .bashrc

**参考链接 / References**:
- N/A

---

#### 193. How do I stop Windows 10 going to sleep after locking with Win+L key

**问题描述 / Problem Description**:
Tags: windows, sleep, power | Score: 125 | Views: 176449 | Answers: 7

**解决方案 / Solution**:
After running PowerCfg /q and reviewing this page, I believe I have determined the solution to this problem.

There appear to be many power settings that just don't show up in my advanced power options window.  One is Sleep &rarr; System unattended sleep timeout.
To make it visible, I opened regedit.exe and found this key:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\238C9FA8-0AAD-41ED-83F4-97BE242C8F20\7bc4a2f9-d8fc-4469-b07b-33eb785aaca0


Set its Attributes DWORD value to 2.  This will make it show up in your advanced settings.  Go there and configure it to be zero minutes if you don't want it to sleep when you lock your screen.

**参考链接 / References**:
- N/A

---

#### 194. Can I use my laptop as a second monitor?

**问题描述 / Problem Description**:
Tags: windows, laptop, multiple-monitors | Score: 125 | Views: 112209 | Answers: 9

**解决方案 / Solution**:
Here's an interesting freeware solution:

ZoneScreen

**参考链接 / References**:
- N/A

---

#### 195. Multi-tab command prompt in Windows?

**问题描述 / Problem Description**:
Tags: windows, command-line, tabs | Score: 124 | Views: 195577 | Answers: 11

**解决方案 / Solution**:
Sorry for the self-promotion, I'm the author of another Console Emulator, not mentioned here.



ConEmu is opensource console emulator with tabs, which represents multiple consoles and simple GUI applications as one customizable GUI window.

Initially, the program was designed to work with Far Manager (my favorite shell replacement - file and archive management, command history and completion, powerful editor). But ConEmu can be used with any other console application or simple GUI tools (like PuTTY for example). ConEmu is a live project, open to suggestions.

A brief excerpt from the long list of options:


Use any font installed in the system, or copied to a folder of the program (ttf, otf, fon, bdf)
Run selected tabs as Administrator (Vista+) or as selected user
Windows 7 Jump lists and Progress on taskbar
Integration with DosBox (useful in 64bit systems to run DOS applications)
Smooth resize, maximized and fullscreen window modes
Scrollbar initially hidden, may be revealed by mouseover or checkbox in settings
Optional settings (e.g. pallette) for selected applications
User friendly text and block selection (from keyboard or mouse), copy, paste, text search in console
ANSI X3.64 and Xterm 256 color
Quake/Tilda style
Change cursor position in command prompt (cmd, powershell) with mouse click (build 120618+)
Works on Chinese editions of Windows :)


Far Manager users will acquire shell style drag-n-drop, thumbnails and tiles in panles, tabs for editors and viewers, true colors and font styles (italic/bold/underline).

Try it. You may read some comments on StackOverflow.

**参考链接 / References**:
- N/A

---

#### 196. What is the $WINDOWS.~BT folder?

**问题描述 / Problem Description**:
Tags: windows | Score: 124 | Views: 363926 | Answers: 2

**解决方案 / Solution**:
This seems to be Windows update logs &amp; files.
It includes files to upgrade Windows, and also, once you do upgrade, the old OS goes into that folder
It should be perfectly safe to delete it, as long as you don't want to upgrade or downgrade Windows.
However, you can't do it the normal way.
Instead,

a)      Press Windows key + R
b)      Type: %windir%\system32\cleanmgr.exe
c)       Hit Enter on your keyboard

Edit: This method seems to only delete some things in this folder, some may be left over. See the other answer for a more complete removal method, though that isn't perfect, either. Additionally, this may help: How to delete trustedinstaller files on Windows 8
Sources:

http://answers.microsoft.com/en-us/windows/forum/windows_8-windows_install/how-do-i-delete-windowsbt-after-failed-windows-8/d15416e8-fd5a-4d4e-b04b-5907a4f6c623
John (see comments)
FranKee (see comments)

**参考链接 / References**:
- N/A

---

#### 197. Cortana Search is not finding applications on Windows 10

**问题描述 / Problem Description**:
Tags: windows-10 | Score: 124 | Views: 133915 | Answers: 17

**解决方案 / Solution**:
Found a solution here: Cortana not finding Desktop apps when searching for them

Here is the relevant part:

I reinstalled Cortana using the following procedure:


Open an elevated Command Prompt window (press win + X, and then press A)
Type start powershell and press enter
Run the command (in one line):



  Get-AppXPackage -Name Microsoft.Windows.Cortana | Foreach
  {Add-AppxPackage -DisableDevelopmentMode -Register
  "$($_.InstallLocation)\AppXManifest.xml"}


After 30 seconds the problem was solved on my machine. Incredible.

**参考链接 / References**:
- N/A

---

#### 198. How can I control the master volume in Windows?

**问题描述 / Problem Description**:
Tags: windows, audio, keyboard-shortcuts, macros | Score: 123 | Views: 401600 | Answers: 14

**解决方案 / Solution**:
I just did this with my laptop. I used AutoHotKey

Here is the script

#PgUp::Send {Volume_Up 1}
#PgDn::Send {Volume_Down 1}


so doing Win+PgUp Win+PgDown changes the master volume. If you prefer Ctrl+PgUp, use ^PgUp::Send.


If you don't have it installed already, http://www.autohotkey.com/
Once installed, right click your Desktop, and choose new AutoHotKey file
Make sure to title the file ending with .ahk  (for example, I used "controls.ahk")
Paste the code in from above
Save it, and double click the script in windows explorer


To run it at startup


Use the AHK provided "Convert to exe" utility (or you can right click the file and select "compile script")
Create the .exe in "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

**参考链接 / References**:
- N/A

---

#### 199. If DOS is single-tasking, how was multitasking possible in old version of Windows?

**问题描述 / Problem Description**:
Tags: windows, multitasking | Score: 123 | Views: 31469 | Answers: 7

**解决方案 / Solution**:
Windows 95
Windows 95 was far more than &quot;just a wrapper&quot; for MS-DOS. Quoting Raymond Chen:

MS-DOS served two purposes in Windows 95.

It served as the boot loader.
It acted as the 16-bit legacy device driver layer.


Windows 95 actually hooked/overrode just about all of MS-DOS, keeping it as a compatibility layer while doing all the heavy lifting itself. It also implemented preemptive multitasking for 32-bit programs.

Pre-Windows 95
Windows 3.x and older were mostly 16-bit (with the exception of Win32s, a kinda compatibility layer that bridges 16 and 32, but we'll ignore that here), were more dependent on DOS, and used only cooperative multitasking - that's the one where they don't force a running program to switch out; they wait for the running program to yield control (basically, say &quot;I'm done&quot; by telling the OS to run the next program that's waiting).

Multitasking was cooperative, just like in old versions of MacOS (though unlike Multitasking DOS 4.x, which sported preemptive multitasking). A task had to yield to the OS in order to schedule a different task. The yields were built into certain API calls, notably message processing. As long as a task processed messages in a timely manner, everything was great. If a task stopped processing messages and was busy executing some processing loop, multitasking was no more.

Windows 3.x architecture
As for how early Windows programs would yield control:

Windows 3.1 uses cooperative multitasking - meaning that each application that is in the process of running is instructed to periodically check a message queue to find out if any other application is asking for use of the CPU and, if so, to yield control to that application. However, many Windows 3.1 applications would check the message queue only infrequently, or not at all, and monopolize control of the CPU for as much time as they required. A preemptive multitasking system like Windows 95 will take CPU control away from a running application and distribute it to those that have a higher priority based on the system's needs.

source
All DOS would see is this single application (Windows or other) running, which would pass control around without exiting. In theory, preemptive multitasking can possibly be implemented on top of DOS anyway with the use of a real-time clock and hardware interrupts to forcibly give control to the scheduler. As Tonny comments, this was actually done by some OSes running on top of DOS.
386 enhanced mode?
Note: there have been some comments on 386 enhanced mode of Windows 3.x being 32-bit, and supporting preemptive multitasking.
This is an interesting case. To summarise the linked blog post, 386 enhanced mode was basically a 32-bit hypervisor, which ran virtual machines. Inside one of those virtual machines ran Windows 3.x standard mode, which does all the stuff listed above.
MS-DOS would also run inside those virtual machines, and apparently they were preemptively multitasked - so it seems that the 386 enhanced mode hypervisor will share CPU time slices between the virtual machines (one of which ran normal 3.x and others which ran MS-DOS), and each VM will do its own thing - 3.x would cooperatively multitask, while MS-DOS would be single-tasked.

MS-DOS
DOS itself was single-tasking on paper, but it did have support for TSR programs, that would stay in the background until triggered by a hardware interrupt. Far from true multitasking, but not fully single-tasked either.

All this talk of bit-ness? I asked about multitasking!
Well, strictly speaking the bit-ness and multitasking are not dependent on each other. It should be possible top implement any multitasking mode in any bit-ness. However, the move from 16-bit processors to 32-bit processors also introduced other hardware functionality that could have made preemptive multitasking easier to implement.
Also, since 32-bit programs were new, it was easier to get them to work when they're forcibly switched out - which might have broken some legacy 16-bit programs.
Of course, this is all speculation. If you really want to know why MS didn't implement preemptive multitasking in Windows 3.x (386 enhanced mode notwithstanding), you'll have to ask someone who worked there.
Also, I wanted to correct your assumption that Windows 95 was jsut a wrapper for DOS ;)

**参考链接 / References**:
- N/A

---

#### 200. Why does Windows use backslashes for paths and Unix forward slashes?

**问题描述 / Problem Description**:
Tags: windows, unix, path | Score: 122 | Views: 83967 | Answers: 2

**解决方案 / Solution**:
Unix introduced / as the directory separator sometime around 1970. I don't know why exactly this character was chosen; the ancestor system Multics used &gt;, but the designers of Unix had already used &gt; together with &lt; for redirection in the shell (see Why is the root directory denoted by a / sign?).
MS-DOS 2.0 introduced \ as the directory separator in the early 1980s. The reason / was not used is that MS-DOS 1.0 (which did not support directories at all) was already using / to introduce command-line options. It probably took this usage of / from VMS (which had a more complicated syntax for directories). You can read a more detailed explanation of why that choice was made on Larry Osterman's blog. MS-DOS even briefly had an option to change the option character to - and the directory separator to /, but it didn't stick.
/ it is recognized by most programmer-level APIs (in all versions of DOS and Windows). So you can often, but not always get away with using / as a directory separator under Windows. A notable exception is that you can't use / as a separator after the \\? prefix which (even in Windows 7) is the only way to specify a path using Unicode or containing more than 260 characters.
Some user interface elements support / as a directory separator under Windows, but not all. Some programs just pass filenames through to the underlying API, so they support / and \ indifferently. In the command interpreter (in command.com or cmd), you can use / in many cases, but not always; this is partly dependent on the version of Windows (for example, cd /windows works in XP and 7 but did not in Windows 9x). The Explorer path entry box accepts / (at least from XP up; probably because it also accepts URLs). On the other hand, the standard file open dialog rejects slashes.

**参考链接 / References**:
- N/A

---

#### 201. How to add more commands to Git Bash?

**问题描述 / Problem Description**:
Tags: windows, git-bash | Score: 122 | Views: 225512 | Answers: 12

**解决方案 / Solution**:
There are two versions of Git that you are likely to be using - the msysgit distribution or Cygwin.
Installing Additional Utilities For Cygwin
Although you might have only installed Git as a part of your Cygwin install (if you used Cygwin), Cygwin has a program called setup.exe which you can use to add packages. Essentially, all you have to do is run setup.exe and pick out what programs you want installed when you get to the Select Packages window. The introduction here provides a good overview with images that detail the process.
Cygwin's installer is smart enough to figure out that you have a preexisting installation, and it will add packages to your installation (instead of nuking it and starting over).
MSYS
The other version of Git you are probably using (if not Cygwin) is msysgit. Because msysgit installs a minimal Unix environment which is not really compatible with MinGW, you'll end up having to install the MinGW suite beside msysgit. The MinGW Getting Started page gives a detailed overview on how to go about getting MinGW installed - since I have no experience with MinGW personally, all I can really do is refer you to their instructions.
You'll then have to migrate your msysgit installation into MinGW. This can be accomplished by doing the following (taken from here). After the following sequence is done, MinGW should find your Git installation.
cd GITDIR # Where GITDIR is wherever inside Program Files you put Git
cp bin/git* /MINGW/bin # Where MINGW is wherever you put MinGW
cp -r libexec/git* /MINGW/libexec
cp -r share/git* /MINGW/share

**参考链接 / References**:
- N/A

---

#### 202. Diskpart - Can&#39;t delete a partition without the force protected parameter set

**问题描述 / Problem Description**:
Tags: windows, windows-10, partitioning, diskpart | Score: 121 | Views: 628650 | Answers: 2

**解决方案 / Solution**:
Is my disk locked in a permanent way?

You need to add the override option:

delete partition override



  override
  
  Enables DiskPart to delete any partition regardless of type. Normally,
  DiskPart enables you to delete only known data partitions.


Source DiskPart Command-Line Options 



How to delete an OEM partition


  "Cannot delete a protected partition without the force protection parameter set."
  
  This is a warning from Windows that you need to be doubly sure that
  you want to delete this partition. 
  
  If you see this error when trying to delete a partition then use:

delete partition override



Source How to delete an OEM partition

**参考链接 / References**:
- N/A

---

#### 203. How to monitor a folder and trigger a command-line action when a file is created or edited?

**问题描述 / Problem Description**:
Tags: windows, windows-vista, automation, scheduled-tasks | Score: 121 | Views: 401901 | Answers: 8

**解决方案 / Solution**:
At work we use Powershell to monitor folders.
It can be used since Windows Vista (.NET and PowerShell is preinstalled) without any additional tools.

This script monitors a certain folder and writes a logfile. You can replace the action and do whatever you want e.g  call an external tool

Example log file


11/23/2014 19:22:04, Created, D:\source\New Text Document.txt
11/23/2014 19:22:09, Changed, D:\source\New Text Document.txt
11/23/2014 19:22:09, Changed, D:\source\New Text Document.txt
11/23/2014 19:22:14, Deleted, D:\source\New Text Document.txt


StartMonitoring.ps1

### SET FOLDER TO WATCH + FILES TO WATCH + SUBFOLDERS YES/NO
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = "D:\source"
    $watcher.Filter = "*.*"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true  

### DEFINE ACTIONS AFTER AN EVENT IS DETECTED
    $action = { $path = $Event.SourceEventArgs.FullPath
                $changeType = $Event.SourceEventArgs.ChangeType
                $logline = "$(Get-Date), $changeType, $path"
                Add-content "D:\log.txt" -value $logline
              }    
### DECIDE WHICH EVENTS SHOULD BE WATCHED 
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
    Register-ObjectEvent $watcher "Deleted" -Action $action
    Register-ObjectEvent $watcher "Renamed" -Action $action
    while ($true) {sleep 5}


How to use


Create a new text file 
Copy &amp; paste the above code
Change the following settings to your own needs: 


folder to monitor: $watcher.Path = "D:\source"
file filter to include only certain file types: $watcher.Filter = "*.*"
include subdirectories yes/no: $watcher.IncludeSubdirectories = $true

Save and rename it to StartMonitoring.ps1
Start monitoring by Right click » Execute with PowerShell


To stop monitoring, it's enough to close your PowerShell window

Further reading


Documentation for PowerShell's FileSystemWatcher 
Documentation for PowerShell's Register-Event
Inspirations for script

**参考链接 / References**:
- N/A

---

#### 204. How do I run Java apps upscaled on a high-DPI display?

**问题描述 / Problem Description**:
Tags: windows-10, java, high-dpi | Score: 121 | Views: 251126 | Answers: 9

**解决方案 / Solution**:
Just found an easy solution on my Windows 10 machine:


Find java.exe you installed.
Right click -> Properties
Go to Compatibility tab
Check Override high DPI scaling behavior.
Choose System for Scaling performed by:

**参考链接 / References**:
- N/A

---

#### 205. Quick way to tell if an installed application is 64-bit or 32-bit

**问题描述 / Problem Description**:
Tags: windows, 64-bit, 32-bit | Score: 120 | Views: 240393 | Answers: 12

**解决方案 / Solution**:
If you run the application, in Task Manager it should have a *32 beside it to indicate it's 32-bit. I'm pretty sure they had this implemented in Server 2003, not positive though, hopefully someone can clarify.

You could also run it through PEiD. PEiD does not support 64-bit PEs, so it will choke if it's 64-bit.

There is also the famous GNU file for Windows. It will tell you all sorts of information about an executable.

Example:

$ file winrar-x64-392b1.exe
winrar-x64-392b1.exe: PE32+ executable for MS Windows (GUI)

$ file display.exe
display.exe: PE32 executable for MS Windows (GUI) Intel 80386 32-bit&lt;/pre&gt;


As you can see, the 64-bit WinRAR installer is classified as PE32+, which signifies a 64-bit executable. The 32-bit application is simply PE32, a 32-bit executable.

**参考链接 / References**:
- N/A

---

#### 206. Hyper-V vs Virtual Machine Platform vs Windows Hypervisor Platform settings in Programs and Features?

**问题描述 / Problem Description**:
Tags: windows, windows-10, virtual-machine, virtualization, hypervisor | Score: 120 | Views: 158766 | Answers: 1

**解决方案 / Solution**:
How do they correlate?

They are separate independent features and do not directly correlate with one another.

What does each setting do exactly?


Hyper-V is Microsoft's Hypervisor.

Virtual Machine Platform - &quot;Enables platform support for virtual machines&quot; and is required for WSL2.  Virtual Machine Platform can be used to create MSIX Application packages for an App-V or MSI.

Windows Hypervisor Platform - &quot;Enables virtualization software to run on the Windows hypervisor&quot; and at one time was required for Docker on Windows.  The Hypervisor platform is an API that third-party developers can use in order to use Hyper-V.  Oracle VirtualBox, Docker, and QEMU are examples of these projects.



The Windows Hypervisor Platform adds an extended user-mode API for
third-party virtualization stacks and applications to create and
manage partitions at the hypervisor level, configure memory mappings
for the partition, and create and control the execution of virtual
processors.

Sources:

Windows Hypervisor Platform

MSIX documentation

Why can't VirtualBox or VMware run with Hyper-V enabled on Windows 10

**参考链接 / References**:
- N/A

---

#### 207. Getting WGET to display a less verbose output

**问题描述 / Problem Description**:
Tags: windows, linux, wget | Score: 119 | Views: 110770 | Answers: 4

**解决方案 / Solution**:
You can use:
wget --no-verbose ...
wget -nv ...

to make wget less verbose. When I saw &quot;less verbose&quot; I mean that you get:

one printed line of text with the file name for each download
no progress bar

**参考链接 / References**:
- N/A

---

#### 208. Where are the shortcuts for the Windows 7 Taskbar stored on disk?

**问题描述 / Problem Description**:
Tags: windows-7, windows, taskbar | Score: 118 | Views: 277321 | Answers: 5

**解决方案 / Solution**:
Taskbar shortcuts are located in: %AppData%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar.

You can also add the "Quick Launch" folder to your task bar as a toolbar to re-enable the quick launch feature.

**参考链接 / References**:
- N/A

---

#### 209. How to order windows of the same program on taskbar

**问题描述 / Problem Description**:
Tags: windows, windows-8, firefox, taskbar | Score: 118 | Views: 75241 | Answers: 1

**解决方案 / Solution**:
Figured I'd share how I got this solved.

Scott's comment pointed me to this question: Reorder Windows 7 taskbar items The accepted answer to that points to a program now called 7+ Taskbar Tweaker, which as it turns out works with Windows 8 as well as 7 now. It not only offers options for easily reordering windows within a taskbar group (either by right-clicking and dragging the taskbar tabs themselves or by dragging the preview windows), but also a whole lot of further options for customizations and conveniences. So for anyone else frustrated with this, that program is exactly what you're looking for and more.

**参考链接 / References**:
- N/A

---

#### 210. Where are ALL locations of Start Menu folders in Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, start-menu | Score: 118 | Views: 546183 | Answers: 14

**解决方案 / Solution**:
You can find it here :

%ProgramData%\Microsoft\Windows\Start Menu\Programs
%AppData%\Microsoft\Windows\Start Menu\Programs


which, in a standard installation, refer to

C:\ProgramData\Microsoft\Windows\Start Menu\Programs
C:\Users\&lt;User&gt;\AppData\Roaming\Microsoft\Windows\Start Menu\Programs


To me that includes all folders and files in the start screen. 

But maybe you installed programs, then uninstalled them- but the folders remained there hence the extra folders or files.

In my case all that was in that folder existed in the Start menu.

**参考链接 / References**:
- N/A

---

#### 211. How to make a shortcut from CMD?

**问题描述 / Problem Description**:
Tags: windows, windows-xp, command-line, shortcuts | Score: 117 | Views: 477261 | Answers: 9

**解决方案 / Solution**:
There is some very useful information on this site: http://ss64.com/nt/shortcut.html
Seems like there is some shortcut.exe in some resource kit which I don't have.
As many other sites mention, there is no built-in way to do it from a batch file.
But you can do it from a VB script:

Optional sections in the VBscript below are commented out:

Set oWS = WScript.CreateObject(&quot;WScript.Shell&quot;)
sLinkFile = &quot;C:\MyShortcut.LNK&quot;
Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = &quot;C:\Program Files\MyApp\MyProgram.EXE&quot;
 '  oLink.Arguments = &quot;&quot;
 '  oLink.Description = &quot;MyProgram&quot;   
 '  oLink.HotKey = &quot;ALT+CTRL+F&quot;
 '  oLink.IconLocation = &quot;C:\Program Files\MyApp\MyProgram.EXE, 2&quot;
 '  oLink.WindowStyle = &quot;1&quot;   
 '  oLink.WorkingDirectory = &quot;C:\Program Files\MyApp&quot;
oLink.Save

So, if you really must do it, then you could make your batch file write the VB script to disk, invoke it and then remove it again. For example, like so:
@echo off
echo Set oWS = WScript.CreateObject(&quot;WScript.Shell&quot;) &gt; CreateShortcut.vbs
echo sLinkFile = &quot;%HOMEDRIVE%%HOMEPATH%\Desktop\Hello.lnk&quot; &gt;&gt; CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) &gt;&gt; CreateShortcut.vbs
echo oLink.TargetPath = &quot;C:\Windows\notepad.exe&quot; &gt;&gt; CreateShortcut.vbs
echo oLink.Save &gt;&gt; CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs

Running the above script results in a new shortcut on my desktop:

Here's a more complete snippet from an anonymous contributor (updated with a minor fix):
@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
SET LinkName=Hello
SET Esc_LinkDest=%%HOMEDRIVE%%%%HOMEPATH%%\Desktop\!LinkName!.lnk
SET Esc_LinkTarget=%%SYSTEMROOT%%\notepad.exe
SET cSctVBS=CreateShortcut.vbs
SET LOG=&quot;.\%~N0_runtime.log&quot;
((
  echo Set oWS = WScript.CreateObject^(&quot;WScript.Shell&quot;^) 
  echo sLinkFile = oWS.ExpandEnvironmentStrings^(&quot;!Esc_LinkDest!&quot;^)
  echo Set oLink = oWS.CreateShortcut^(sLinkFile^) 
  echo oLink.TargetPath = oWS.ExpandEnvironmentStrings^(&quot;!Esc_LinkTarget!&quot;^)
  echo oLink.Save
)1&gt;!cSctVBS!
cscript //nologo .\!cSctVBS!
DEL !cSctVBS! /f /q
)1&gt;&gt;!LOG! 2&gt;&gt;&amp;1

**参考链接 / References**:
- N/A

---

#### 212. Windows 10 high memory usage (unknown reason)

**问题描述 / Problem Description**:
Tags: windows, memory, performance, troubleshooting, windows-10 | Score: 117 | Views: 450914 | Answers: 4

**解决方案 / Solution**:
You have a memory leak caused by a driver. Look at the high value of nonpaged kernel memory. In your case this is over 3.7 GB. You can use poolmon to see which driver is causing the high usage.
Install the Windows WDK, run poolmon, sort it via P after pool type so that non paged is on top and via B after bytes to see the tag which uses most memory. Run poolmon by going to the folder where WDK is installed, go to Tools (or C:\Program Files (x86)\Windows Kits\10\Tools\x64) and click poolmon.exe.
Now see which pooltag uses most memory as shown here:

Now open a cmd prompt and run the findstr command. To do this, open cmd prompt and type cd C:\Windows\System32\drivers. Then type findstr /s __ *.*, where __ is the tag (left-most name in poolmon).
Do this to see which driver uses this tag:

Now, go to the drivers folder (C:\Windows\System32\drivers) and right-click the driver in question (intmsd.sys in the above image example). Click Properties, go to the details tab to find the Product Name. Look for an update for that product.
If the pooltag only shows Windows drivers or is listed in the pooltag.txt (&quot;C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\triage\pooltag.txt&quot;)
you have use xperf to trace what causes the usage. Install the WPT from the Windows SDK, open a cmd.exe as admin and run this:

xperf -on PROC_THREAD+LOADER+POOL -stackwalk
PoolAlloc+PoolFree+PoolAllocSession+PoolFreeSession -BufferSize 2048
-MaxFile 1024 -FileMode Circular &amp;&amp; timeout -1 &amp;&amp; xperf -d C:\pool.etl

capture 30 -60s of the grow. Open the ETL with WPA.exe, add the Pool graphs to the analysis pane.
Put the pooltag column at first place and add the stack column. Now load the symbols inside WPA.exe and expand the stack of the tag that you saw in poolmon.

Now find other 3rd party drivers which you can see in the stack. Here the Thre tag (Thread) is used by AVKCl.exe from G-Data. Look for driver/program updates to fix it.

The user Hristo Hristov provided a trace with a high FMfn usage during unzipping files:

The tag is used by the driver WiseFs64.sys which is part of the &quot;Wise Folder Hider&quot; program. Removing it fixes the leak.

The user Samuil Dichev provided a trace with a high FMic and Irp usage


The tags are used by the program Razor Cortex.
In the sample of the user chr0n0ss the FMic and Irp usage is caused by  F-Secure Antivirus Suite:

Removing it and using Windows Defender fixed the issue for him.

**参考链接 / References**:
- N/A

---

#### 213. How to echo contents of file in a DOS/Windows command prompt

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 117 | Views: 286059 | Answers: 3

**解决方案 / Solution**:
3 Answers
3
Sorted by:
Reset to default
Highest score (default)
Date modified (newest first)
Date created (oldest first)

**参考链接 / References**:
- N/A

---

#### 214. Keep cmd.exe command history between sessions?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 117 | Views: 72512 | Answers: 5

**解决方案 / Solution**:
I've found 2 ways, neither of which require switching to PowerShell.

Install Clink, which enhances cmd.exe with persistent history and much more. Just install it and then open cmd as normal.

Install TCC/LE free version, which is a separate program, again providing an enhanced version of cmd.exe.

**参考链接 / References**:
- N/A

---

#### 215. Is there a way to fake a dual (second) monitor

**问题描述 / Problem Description**:
Tags: windows, multiple-monitors, desktop | Score: 117 | Views: 465196 | Answers: 11

**解决方案 / Solution**:
I made Windows think I had two connected displays like this:


Right click on the desktop, click 'Screen Resolution'
Click 'Detect' on the next screen
Click 'Another display not detected' and under the multiple displays option select 'Try to connect anyway on: VGA'
Click 'Apply'
You can now enable your desktop to be extended as if you have a second screen plugged into your computer.


To view the second screen. This can be done via LogMeIn or TeamViewer on iOS, Android, Windows, Mac and I believe Linux:

I used TeamViewer as I already use it, so already have it installed


Opened TeamViewer on iPad
Connect to the computer setup previously
Using a 'Monitor' button at the bottom, select and show screen number 2.
iPad now shows screen 2 from PC.

**参考链接 / References**:
- N/A

---

#### 216. Local taskbar visible during remote desktop fullscreen

**问题描述 / Problem Description**:
Tags: windows, windows-10, remote-desktop, taskbar, always-on-top | Score: 116 | Views: 283419 | Answers: 7

**解决方案 / Solution**:
Try restarting explorer.exe process as mentioned in fixing remote desktop taskbar

**参考链接 / References**:
- N/A

---

#### 217. Way to limit bandwidth of programs on Windows?

**问题描述 / Problem Description**:
Tags: windows, bandwidth | Score: 116 | Views: 280750 | Answers: 5

**解决方案 / Solution**:
I use Net Limiter, which has a free version, but unfortunately you'll need to pay for the limitation feature.

NetLimiter is an ultimate internet traffic control and monitoring tool designed for Windows. You can use NetLimiter to set download/upload transfer rate limits for applications or even single connection and monitor their internet traffic.
Along with this unique feature, Netlimiter offers comprehensive set of internet statistical tools. It includes real-time traffic measurement and long-term per-application internet traffic statistics

**参考链接 / References**:
- N/A

---

#### 218. Does Windows 10 support UTC as BIOS time?

**问题描述 / Problem Description**:
Tags: windows-10, utc | Score: 116 | Views: 183249 | Answers: 2

**解决方案 / Solution**:
Yep, I had success. Don't forget disabling the &quot;internet update&quot; for the time!
I used the way described in the ArchWiki using a QWORD on a 64bit Win10.
The NTP is done on Arch and not on Windows, but the latter isnt getting booted so often anyway.
Here's the .reg file:
RealTimeIsUniversal.reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation]
     &quot;RealTimeIsUniversal&quot;=hex(b):01,00,00,00,00,00,00,00

From ArchWiki: UTC in Windows

Using regedit, add a DWORD value with hexadecimal value 1 to the
registry:
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation\RealTimeIsUniversal

Alternatively, create a *.reg file (on the desktop) with the following
content and double-click it to import it into registry:
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation]
 &quot;RealTimeIsUniversal&quot;=dword:00000001

If the above appears to have no affect, and a 64-bit variant of
Windows is being used, using a QWORD value instead of a DWORD value
may resolve the issue.

**参考链接 / References**:
- N/A

---

#### 219. How to stop jucheck from running? Java won&#39;t remember &quot;Check for Updates Automatically&quot; setting

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-vista, java | Score: 115 | Views: 259895 | Answers: 10

**解决方案 / Solution**:
Refer to the following answer at Server Fault - Can’t seem to disable Java Automatic Update:


  Actually this problem is due to the
  control panel requiring Admin
  Privileges to allow the java control
  panel to save your settings (hasn't
  been fixed for ages, thanks to sun
  micro).
  
  Basically find the java control panel
  javacpl.exe here:
  
  C:\Program Files\Java\jre6\bin\javacpl.exe
  
  ...right click > run with admin
  privileges.
  
  Uncheck java update, save and then
  reopen it to check that the setting is
  sticking.


My added tip:  Windows Vista x64 or Windows 7 x64 users should instead look for:

C:\Program Files (x86)\Java\jre6\bin\javacpl.exe

Update: For Java 7 (32-bit), look instead for:

C:\Program Files (x86)\Java\jre7\bin\javacpl.exe .. and yes, Java 7 still has this problem &ndash; after all these years they didn't fix it to work properly, so this workaround is still required.

**参考链接 / References**:
- N/A

---

#### 220. Windows 10: Rename pinned items in Windows Explorer&#39;s Quick Access

**问题描述 / Problem Description**:
Tags: windows-explorer, windows-10 | Score: 115 | Views: 50685 | Answers: 6

**解决方案 / Solution**:
Sort of a hack, but I ended up using mklink to create Directory Junctions with the names I wanted, since they took away my beloved Favorites.

So, if I have a directory "c:\dir1", which I want to be named "Directory 1" in the Quick Access list, I would run:

mklink /J "c:\whatever\Directory 1" "c:\dir1"


Then you'll see "Directory 1" in "c:\whatever", which you can add to Quick Access, and it will be named "Directory 1".

**参考链接 / References**:
- N/A

---

#### 221. How to pick a color from an image

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-xp, images, colors | Score: 113 | Views: 245794 | Answers: 12

**解决方案 / Solution**:
In Windows, there is an easier way that doesn't need any software.


Capture the screen in an image file (use something like the Snipping Tool to grab the desired area)
Open the file with MS Paint
Use Paint's pick color and pick the color
Press "Edit Colors" button
You have the RGB values!

**参考链接 / References**:
- N/A

---

#### 222. Good on-screen ruler application for Windows?

**问题描述 / Problem Description**:
Tags: windows, ruler | Score: 113 | Views: 128714 | Answers: 4

**解决方案 / Solution**:
I have been using Ruler from Codeplex for ages now (I removed the old link because it was considered harmful by Chrome). Very easy to use, a simple program with simple options:


Always on top
The vertical and horizontal measurement 
Option to show ToolTip for smaller dimensions.
Resizable by dragging
Can open multiple instances
No installation required 


Forked and improved on GitHub and enhanced https://github.com/andrijac/ruler

**参考链接 / References**:
- N/A

---

#### 223. Use VPN connection only for selected applications

**问题描述 / Problem Description**:
Tags: windows, networking, vpn, internet, privacy | Score: 113 | Views: 325391 | Answers: 12

**解决方案 / Solution**:
It is possible to accomplish this, at least on Linux (and I'm thinking on BSD and OS X as well). You can do so by:


Create an exra user for all VPN traffic.
Create an extra routing table with 1 default route via the VPN.
Configure Netfilter through Iptables to use the other routing table for all traffic originating from a specific User ID.
Run the applications that should use the VPN under their own user. For example with 'sudo'.


There are scripts for accomplishing the above steps here or there is another guide here.

Here is a detailed guide for routing Transmission via a VPN (using a VPN server that you own.

**参考链接 / References**:
- N/A

---

#### 224. recursively change owner windows 7

**问题描述 / Problem Description**:
Tags: windows-7, windows-10, permissions, ownership | Score: 113 | Views: 126502 | Answers: 6

**解决方案 / Solution**:
To fix really broken permissions, the best is to run these two commands one after the other:

takeown /f "C:\path\to\folder" /r
icacls "C:\path\to\folder" /reset /T


The first one will give you ownership of all the files, however that might not be enough, for example if all the files have the read/write/exec permissions set to "deny". You own the files but still cannot do anything with them.

In that case, run the second command, which will fix the broken permissions.

**参考链接 / References**:
- N/A

---

#### 225. Show the date on the System Tray in Windows 10

**问题描述 / Problem Description**:
Tags: taskbar, windows-10 | Score: 113 | Views: 310726 | Answers: 11

**解决方案 / Solution**:
I found out the same problem in my horizontal Taskbar. It turns out that when "Use small taskbar buttons" is checked, the taskbar height is not enough to house the time and the date strings, so the date string is dropped.

Unchecking "Use small taskbar buttons" or doubling the taskbar height are the two solutions I found... but they neutralize my initial intention of a smaller taskbar taking up less space.

[EDIT]
After reading Why you should use a vertical taskbar I tried it and also realized that you get the full time and date already from the smallest size of the vertical taskbar, even with small taskbar buttons. So it might have changed since the time the question was asked. Now, this might be your solution if you like the side bar, or you are willing to try and reap some of the benefits that article claims.

**参考链接 / References**:
- N/A

---

#### 226. Starting Outlook automatically in Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, microsoft-outlook | Score: 113 | Views: 258742 | Answers: 6

**解决方案 / Solution**:
You should be able to add a shortcut to Outlook in the Startup folder.  To open the Startup folder:
Using the Run dialog:

Bring up Run dialog Win+R
Type shell:startup


Copy the shortcut to Outlook to the Startup folder:

Right click on the Outlook shortcut from your start menu
Select Open file location
Copy the shortcut for Outlook to the Startup folder

**参考链接 / References**:
- N/A

---

#### 227. Should I disable swap file if I have lots of RAM or should I move it to a virtual RAM drive?

**问题描述 / Problem Description**:
Tags: windows, memory, performance, virtual-memory, pagefile | Score: 112 | Views: 144168 | Answers: 15

**解决方案 / Solution**:
No matter how much RAM you have, you want the system to be able to use it efficiently. Having no paging file at all forces the operating system to use RAM inefficiently for two reasons. First, it can't make pages discardable, even if they haven't been either accessed or modified in a very long time, which forces the disk cache to be smaller. Second, it has to reserve physical RAM to back allocations that are very unlikely to ever require it (for example, a private, modifiable file mapping), leading to a case where you can have plenty of free physical RAM and yet allocations are refused to avoid overcommitting.

Consider, for example, if a program makes a writable, private memory mapping of a 4GB file. The OS has to reserve 4GB of RAM for this mapping, because the program could conceivably modify every byte and there's no place but RAM to store it. So immediately, 4GB of RAM is basically wasted (it can be used to cache clean disk pages, but that's about it).

You need to have a page file if you want to get the most out of your RAM, even if it's never used. It acts as an insurance policy that allows the operating system to actually use the RAM it has, rather than having to reserve it for possibilities that are extraordinarily unlikely.

The people who designed your operating system's behavior are not fools. Having a paging file gives the operating system more choices, and it won't make bad ones.

There's no point in trying to put a paging file in RAM. And if you have lots of RAM, the paging file is very unlikely to be used (it just needs to be there) so it doesn't particularly matter how fast the device it is on is.

**参考链接 / References**:
- N/A

---

#### 228. How to rearrange virtual desktops in Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, virtual-desktop | Score: 112 | Views: 54627 | Answers: 6

**解决方案 / Solution**:
This is not possible in the current version of Windows 10 (20H2) or earlier versions.
However, the recent Windows 10 Insider Preview Build 21337 mentions this feature.
We can only hope that this feature will be rolled out to Windows 10 in an upcoming update.

**参考链接 / References**:
- N/A

---

#### 229. Unable to Install ClickOnce Application due to Security Settings (Windows 10)

**问题描述 / Problem Description**:
Tags: windows-10, clickonce | Score: 112 | Views: 233617 | Answers: 2

**解决方案 / Solution**:
This is caused by the "ClickOnce Trust Prompt Behavior": https://msdn.microsoft.com/en-us/library/ee308453.aspx

To adjust this, simply change the values in the Registry and you should be able to install the application.


  To enable the ClickOnce trust prompt by using the registry editor Open
  the registry editor:
  
  Click Start, and then click Run.
  
  In the Open box, type regedit, and then click OK.
  
  Find the following registry key:
  
  \HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\.NETFramework\Security\TrustManager\PromptingLevel
  
  If the key does not exist, create it.
  
  Add the following subkeys as String Value, if they do not already
  exist, with the associated values shown in the following table.




On my computer, the values were set to "Disabled" and I have no clue which application did that. I changed the values to default and now everything works again like it should.

Or you can just delete the key "TrustManager" itself and everything is working as well.

**参考链接 / References**:
- N/A

---

#### 230. How to stop Skype from starting automatically when booting Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, skype, autostart, skype-for-windows-10 | Score: 112 | Views: 292819 | Answers: 2

**解决方案 / Solution**:
Preventing the classic Skype application from starting

With the classic Skype application window open, do the following:  


Navigate to Tools > Options.
Highlight the General settings section on the upper-left.
Uncheck the option to Start Skype when I start Windows on the right.
Click the Save button.  






Preventing Skype for Windows 10 (Skype UWP) from starting

On the other hand, if this is the Skype UWP app those options won't be available.  Based upon a similar question on the Microsoft Answers web page, their Skype Community Moderator explained what needs to be done:  


  The new Microsoft Skype for Windows 10 (Skype UWP) application has
  never been present in the Startup tab. Windows apps are not managed
  the same way as a Win32 application. The classic Skype for Windows
  Desktop is a Win32 application, Skype UWP is not.
  
  If you close your computer without signing out of the Skype UWP
  application, then on next computer boot, Skype will auto run in the
  background. To maximize Skype UWP you will just need to click on the
  application icon.
  
  If you prefer not to be signed in automatically on Skype for Windows
  10, you can sign out from the app. We won't sign you in automatically
  after that.  


In other words, Skype UWP users simply need to logoff from within the app to prevent it from starting automatically during a subsequent Windows 10 login.  

As a potentially viable alternative to the Skype Community Moderator's advice, you can turn off the background app functionality for Skype. Navigate to the following location:  

Start &gt; Settings &gt; Privacy  


Ensure that you have selected Background apps on the left-hand side, scroll down on the right until you find the entry for Skype and change the slider to Off.  

  

That being said, in addition to the obvious advantages there are minor drawbacks to using this method:  


  Bear in mind that there’s a downside to this. If you prevent the
  Alarms app from running in the background, for example, any alarms you
  set won’t go off. If you prevent the Mail app from running in the
  background, it won’t notify you of new emails. Apps normally run in
  the background to update their live tiles, download new data, and
  receive notifications. If you want an app to continue performing these
  functions, you should allow it to continue running in the background.
  If you don’t care, feel free to prevent the app from running in the
  background. You can still use the app normally, but you may have to
  wait for it to fetch new data after you launch it.




Uninstalling the classic Skype application

Taking it a step further, if you want remove the application entirely, the classic Skype Win32 application will be listed within the Programs and Features applet in the Control Panel. Simply highlight the Skype entry in the Name column and select the Uninstall button near the top.  

  



Uninstalling Skype for Windows 10 (Skype UWP)

In contrast, the Skype UWP app won't be found in Programs and Features. As a result, if you want remove that particular version, navigate to the following location:  

Start &gt; Settings &gt; Apps  


Ensure that you have selected Apps &amp; features on the upper-left, scroll down on the right and left-click Skype to select Uninstall.  

Notably, if the Skype UWP application is already running, before attempting the Uninstall you may need to first select Advanced options, then choose Terminate to "Immediately terminate this app and its related processes." After that, select Uninstall as desired.

  



Additional reading: Download Skype for More Features Than Windows 10’s Built-In Version

**参考链接 / References**:
- N/A

---

#### 231. Turn off display in Windows on command

**问题描述 / Problem Description**:
Tags: windows-7, windows, command-line, display | Score: 111 | Views: 370150 | Answers: 8

**解决方案 / Solution**:
A couple more options:

Turn Off LCD - just place the executable on your desktop
NirCmd - you'll need to copy nircmd.exe to your Windows system directory, or add its location to the PATH environment variable. Then just run nircmd monitor off from the command line. More information at the link.

**参考链接 / References**:
- N/A

---

#### 232. How do I access MTP devices on the command line in Windows?

**问题描述 / Problem Description**:
Tags: windows, command-line, mtp | Score: 111 | Views: 117881 | Answers: 5

**解决方案 / Solution**:
Unfortunately, APIs exposed by MTP are very different from a normal filesystem APIs. Therefore exposing MTP device as a read/write filesystem is not possible. The main reason:

Wikipedia says:


  Neither the MTP nor the PTP standards allow for direct modification of objects. Instead, modified objects must be reuploaded in their entirety, which can take a long time for large objects. With PTP/MTP, the file size must be known at the opening stage.


Your common file copy program just opens a source and a target file, and copies data in chunks from the source file to the target. This won't work with MTP, since you need to use MTP special functions, and generic filesystem primitives (read, seek, write) are not available.

There are also other limitations. For example, the number of files that can be read or written simultaneously on an MTP device is severely limited. The device simply does not behave like a filesystem. 

I suppose read-only filesystem driver for an MTP device might be possible, but because of the problems outlined above, it will be of very little use, so nobody bothered to create it.

**参考链接 / References**:
- N/A

---

#### 233. Assigning a virtual desktop to a monitor in Windows 10

**问题描述 / Problem Description**:
Tags: multiple-monitors, windows-10, virtual-desktop | Score: 111 | Views: 123566 | Answers: 5

**解决方案 / Solution**:
I may be late to the party, but there is a workaround that can get near what you want to do:  

Type Win + Tab to show up the Multiple Desktops panel also showing windows of the current desktop. Right click on one of them and you can choose either "Show this window on all desktops" or "Show windows from this app on all desktops".
You can now switch desktop and they'll stick to the screen.
Afaik, if you choose the 2nd option, it will remember your choice even if you close all windows from the app at one point.

hope it helps

**参考链接 / References**:
- N/A

---

#### 234. Securely erasing all data from a hard drive

**问题描述 / Problem Description**:
Tags: windows, mac, security, secure-erase | Score: 110 | Views: 23450 | Answers: 11

**解决方案 / Solution**:
Look into Darik's Boot and Nuke. It's a bootable CD which lets you securely erase your hard drives.

**参考链接 / References**:
- N/A

---

#### 235. How do I add Python to the Windows PATH?

**问题描述 / Problem Description**:
Tags: windows, python, path | Score: 110 | Views: 745011 | Answers: 5

**解决方案 / Solution**:
For Windows 10/8/7:


Open System Properties (Right click Computer in the start menu, or use the keyboard shortcut Win+Pause)
Click Advanced system settings in the sidebar.
Click Environment Variables...
Select PATH in the System variables section
Click Edit
Add Python's path to the end of the list (the paths are separated by semicolons). For example:

C:\Windows;C:\Windows\System32;C:\Python27



For Windows XP:


Open System Properties (Type it in the start menu, or use the keyboard shortcut Win+Pause)
Switch to the Advanced tab
Click Environment Variables...
Select PATH in the System variables section
Click Edit
Add Python's path to the end of the list (the paths are separated by semicolons). For example:

C:\Windows;C:\Windows\System32;C:\Python27

Test on a new terminal window or if using an integrated terminal within a 
  text editor, close and restart your editor or the changes won't be applied.

**参考链接 / References**:
- N/A

---

#### 236. Dual monitors on Windows - How do I set a different DPI or text size on each monitor?

**问题描述 / Problem Description**:
Tags: windows, multiple-monitors, resolution, dpi | Score: 110 | Views: 241324 | Answers: 11

**解决方案 / Solution**:
DPI settings affect the entire desktop, regardless of number or arrangement of monitors. You cannot have two different DPI settings on two monitors. 

Update:

This is untrue as of Windows 8.1, which adds many DPI scaling enhancements, including per-display DPI settings. Although some may not find the implementation offers enough control.

**参考链接 / References**:
- N/A

---

#### 237. How do I change the DNS settings for WSL2?

**问题描述 / Problem Description**:
Tags: windows-10, ubuntu, dns, windows-subsystem-for-linux | Score: 110 | Views: 207996 | Answers: 6

**解决方案 / Solution**:
The process I documented above is correct - this is how you change the DNS settings under WSL2.

My mistake was in using the well known public DNS Servers for CloudFlare (1.1.1.1) and Google (8.8.8.8 &amp; 8.8.4.4) for testing purposes. It turns out that my local network blocks me from using public DNS. 

When I tested the above process with the correct internal DNS server IP address, everything worked properly.

**参考链接 / References**:
- N/A

---

#### 238. Extremely simple web server for Windows?

**问题描述 / Problem Description**:
Tags: windows, webserver, software-rec, http | Score: 109 | Views: 180922 | Answers: 10

**解决方案 / Solution**:
I recently used mongoose for this purpose. It supports Windows. From the homepage:

Mongoose executable does not depend on any external library or configuration. If it is copied to any directory and executed, it starts to serve that directory on port 8080. If some additional config is required - for example, different listening port or IP-based access control, then a mongoose.conf file with respective options (see example) can be created in the same directory where executable lives. This makes Mongoose perfect for all sorts of demos, quick tests, file sharing, and Web programming.

**参考链接 / References**:
- N/A

---

#### 239. Can I move hiberfil.sys to another drive?

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-10, windows-8, hibernate | Score: 109 | Views: 165424 | Answers: 6

**解决方案 / Solution**:
I don't think it is possible to "redirect" the path of your hiberfil.sys from "C:\hiberfil.sys" to "D:\hiberfil.sys" for example. 

I did some research on Google and in the Windows registry, and found nothing but the option to disable it (and consequently delete hiberfil.sys file):


  
  Click Start, and then type cmd in the Start Search box.
  In the search results list, right-click Command Prompt, and then click Run as Administrator.
  When you are prompted by User Account Control, click Continue.
  At the command prompt, type powercfg.exe /hibernate off, and then press ENTER.
  Type exit and then press ENTER to close the Command Prompt window.

**参考链接 / References**:
- N/A

---

#### 240. Docker on Hyper-V vs WSL 2

**问题描述 / Problem Description**:
Tags: windows-10, docker, hyper-v, wsl2 | Score: 109 | Views: 217620 | Answers: 4

**解决方案 / Solution**:
Please read this: https://www.docker.com/blog/docker-hearts-wsl-2/

We will replace the Hyper-V VM we currently use by a WSL 2 integration package. This package will provide the same features as the current Docker Desktop VM: Kubernetes 1-click setup, automatic updates, transparent HTTP proxy configuration, access to the daemon from Windows, transparent bind mounts of Windows files, and more.


A technical preview of Docker Desktop for WSL 2 will be available for download in July. It will run side by side with the current version of Docker Desktop, so you can continue to work safely on your existing projects. If you are running the latest Windows Insider build, you will be able to experience this first hand. In the coming months, we will add more features until the WSL 2 architecture is used in Docker Desktop for everyone running a compatible version of Windows.

Additionally I recommend to watch this video: https://www.youtube.com/watch?v=lwhMThePdIo
Good comparison you will find here: https://blog.logrocket.com/working-with-node-js-on-hyper-v-and-wsl2/
cite:

Comparing Hyper-V to WSL2


The biggest difference between running Ubuntu Linux in a Hyper-V virtual machine versus running the operating system in WSL2 lies in the ability to access the Ubuntu user interface in Hyper-V.


The user interface allows you to install and use more than just command-line tools.


Depending on your system’s hardware performance, you likely found that WSL2 is the faster option. To expedite the process of running Ubuntu Linux on Hyper-V, you could set up SSH access to the virtual machine.


This speeds up command-line access. However, WSL2 may still have the upper hand since it does not require SSH to enable access.

**参考链接 / References**:
- N/A

---

#### 241. How can I delete all files/subfolders in a given folder via the command prompt?

**问题描述 / Problem Description**:
Tags: windows, windows-7, command-line, batch-file | Score: 108 | Views: 875880 | Answers: 21

**解决方案 / Solution**:
You can do this using del and the /S flag (to tell it to remove all files from all subdirectories):

del /S C:\Path\to\directory\*

**参考链接 / References**:
- N/A

---

#### 242. Is there Windows equivalent to the .bashrc file in Linux?

**问题描述 / Problem Description**:
Tags: windows, bashrc | Score: 108 | Views: 128315 | Answers: 12

**解决方案 / Solution**:
This is a very good question. I found this. I suppose you could make a cmd script and have it run when starting cmd :-?

; Run a command when CMD.exe starts
[HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor]
"AutoRun"=-


EDIT:
I just tried it. I have AutoRun=C:\mini\bashrc.cmd and bashrc.cmd is

@echo off
set TEST_VAR=something


when I start cmd and enter echo %TEST_VAR% it says something. So it works :)

**参考链接 / References**:
- N/A

---

#### 243. Windows equivalent to UNIX &quot;time&quot; command

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 108 | Views: 144396 | Answers: 13

**解决方案 / Solution**:
Use Powershell

Measure-Command {start-process whateveryouwantexecute -Wait}


Edited to your need @efficiencylsBliss:

Measure-Command {start-process java -argumentlist "whateverargumentisneeded" -wait}

**参考链接 / References**:
- N/A

---

#### 244. How do I escape spaces in command line in Windows without using quotation marks?

**问题描述 / Problem Description**:
Tags: windows, command-line, escape-characters | Score: 108 | Views: 379548 | Answers: 8

**解决方案 / Solution**:
It almost all works for me, but have you perhaps tried line5..  escaping the space with a caret symbol (^)

1 C:\Documents and Settings\user&gt;cd ..

2 C:\Documents and Settings&gt;cd ..

3 C:\&gt;cd Documents and Settings

4 C:\Documents and Settings&gt;cd..

5 C:\&gt;cd Documents^ and^ Settings

6 C:\Documents and Settings&gt;cd..

7 C:\&gt;cd C:\documents and settings

8 C:\Documents and Settings&gt;cd..

9 C:\&gt;


Or e.g. below where the caret really makes all the difference.

Looks from below like the caret symbol may be your answer, see line 3 below.

1 C:\&gt;"c:\Documents and Settings\a.bat"
gaga

2 C:\&gt;c:\Documents and Settings\a.bat
'c:\Documents' is not recognized as an internal or external command,
operable program or batch file.

3 C:\&gt;c:\Documents^ and^ Settings\a.bat
gaga

C:\&gt;

**参考链接 / References**:
- N/A

---

#### 245. Can&#39;t copy and paste in Remote Desktop Connection session

**问题描述 / Problem Description**:
Tags: windows, remote-desktop, copy-paste | Score: 107 | Views: 377423 | Answers: 9

**解决方案 / Solution**:
Even when you have the &quot;Clipboard&quot; option enabled, you may still have problems!
If that's the case, use Task Manager to kill and restart the rdpclip.exe process on local and remote machines.
More details on this blog post …

The only way I really knew to fix the clipboard transfer was to close my session and restart it. That meant closing the tools I was using like Visual Studio, Management Studio and the other ancillary processes I have running as I work and then restarting all of it just to restore the clipboard. But today I found a good link on the Terminal Services Blog explaining that what is really happening. The clipboard viewer chain is somehow becoming unresponsive on the local or remote system and events on the clipboards are not being relayed between systems. It is not necessarily a lock being put in place but some sort of failed data transmission. It then goes on to explain the 2 steps you can take to restore the clipboard without restarting your session.
Use Task Manager to kill the rdpclip.exe process
Run rdpclip.exe to restart it

… and a pretty ridculous &quot;explanation&quot; from Microsoft.

Summary
If you have a shared clipboard problem, see if the following troubleshooting guide helps:
+--------------------------+-------------------------+------------------------------+
| Symptom                  | Possible Cause          | Possible Solution            |
+--------------------------+-------------------------+------------------------------+
| Remote-to-local copy and | RDPCLIP is not in the   | Kill and restart RDPCLIP.    |
| paste broken.            | clipboard viewer chain. |                              |
+--------------------------+-------------------------+------------------------------+
| Local-to-remote copy and | TS client is not in the | Close the TS client and      |
| paste broken.            | clipboard viewer chain. | reconnect to the session.    |
+--------------------------+-------------------------+------------------------------+
| RDPCLIP or the TS client | There is a loop in the  | Kill and restart RDPCLIP.    |
| is using excessive CPU.  | local or remote         | If this does not fix the     |
|                          | clipboard viewer chain. | problem, close the TS client |
|                          |                         | and reconnect to the session.|
+--------------------------+-------------------------+------------------------------+

**参考链接 / References**:
- N/A

---

#### 246. Mapping drive letters to local folders

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-8 | Score: 107 | Views: 204786 | Answers: 6

**解决方案 / Solution**:
Alternative:


  net use x: \\localhost\c$\Folder\Example


The difference between net use &amp; subst below break



subst

When a share becomes unavailable subst will try over and over again to re-connect severely impacting performance of your PC as it tries to re-connect. This is less common when mapping local files as it will only occur if you say re-name the folders in the path. The resolution if this does occur is subst x: /d

net use

net use was introduced in win2k/xp to provide an alternative to this. When net use is used to connect to a location and that location becomes unreachable windows will report drive as disconnected and not try to re-connect until user tries to re-connect to resources on the mapped drive. This resolves the performance issues noted in subst



For more information on both commands you can query via the command line with /?

net use /? &amp; subst /?

**参考链接 / References**:
- N/A

---

#### 247. How can I open Google Chrome via command-line with a URL, in incognito mode?

**问题描述 / Problem Description**:
Tags: windows, command-line, google-chrome, private-browsing | Score: 107 | Views: 561824 | Answers: 6

**解决方案 / Solution**:
You might want to try and give it another try.  I just tried it with the following command  

chrome.exe google.com -incognito


This gave me the following window, notice that it is in incognito mode (little icon on top left) and it is also at google.com (or whatever url you pass).  It works, maybe you were just typing it in wrong.

If you have a window open Chrome will default to the currently running application and add a new tab to that, it saves time (of app startup) and memory. In this case, try 

chrome.exe -incognito --app=google.com

**参考链接 / References**:
- N/A

---

#### 248. What is the difference between Symbolic Link and Shortcut?

**问题描述 / Problem Description**:
Tags: windows, shortcuts, symbolic-link | Score: 107 | Views: 90739 | Answers: 5

**解决方案 / Solution**:
I think the important point is that shortcuts are just a file. They have a size (A small one, that just references where they point) and they require an application to support that filetype in order to be used.

A symbolic link is filesystem level, and everything sees it as the original file. An application needs no special support to use a symbolic link.

**参考链接 / References**:
- N/A

---

#### 249. What is the keyboard shortcut for pasting without formatting in MS Word?

**问题描述 / Problem Description**:
Tags: windows, windows-10, microsoft-word, copy-paste, microsoft-word-2019 | Score: 106 | Views: 253682 | Answers: 10

**解决方案 / Solution**:
Or, you can simply set the keyboard shortcut for PasteTextOnly to Ctrl+Shift+V, then it works like before again.

That shortcut is a bit hidden though, so here's the steps how to get there:


File > Options > Customize Ribbon > Keyboard shortcuts: Customize...
Under Categories, select All Commands
Under Commands, look for PasteTextOnly
Set the keyboard shortcut for PasteTextOnly to Ctrl+Shift+V

**参考链接 / References**:
- N/A

---

#### 250. How does the Windows RENAME command interpret wildcards?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch-file, cmd.exe, rename | Score: 106 | Views: 216255 | Answers: 6

**解决方案 / Solution**:
These rules were discovered after extensive testing on a Vista machine. No tests were done with unicode in file names.
RENAME requires 2 parameters - a sourceMask, followed by a targetMask. Both the sourceMask and targetMask can contain * and/or ? wildcards. The behavior of the wildcards changes slightly between source and target masks.
Note - REN can be used to rename a folder, but wildcards are not allowed in either the sourceMask or targetMask when renaming a folder. If the sourceMask matches at least one file, then the file(s) will be renamed and folders will be ignored. If the sourceMask matches only folders and not files, then a syntax error is generated if wildcards appear in source or target. If the sourceMask does not match anything, then a &quot;file not found&quot; error results.
Also, when renaming files, wildcards are only allowed in the file name portion of the sourceMask. Wildcards are not allowed in the path leading up to the file name.
sourceMask
The sourceMask works as a filter to determine which files are renamed. The wildcards work here the same as with any other command that filters file names.

? - Matches any 0 or 1 character except .  This wildcard is greedy - it always consumes the next character if it is not a .  However it will match nothing without failure if at name end or if the next character is a .

* - Matches any 0 or more characters including . (with one exception below).  This wildcard is not greedy. It will match as little or as much as is needed to enable subsequent characters to match.


All non-wildcard characters must match themselves, with a few special case exceptions.

. - Matches itself or it can match the end of name (nothing) if no more characters remain. (Note - a valid Windows name cannot end with .)

{space} - Matches itself or it can match the end of name (nothing) if no more characters remain. (Note - a valid Windows name cannot end with {space})

*. at the end - Matches any 0 or more characters except .  The terminating . can actually be any combination of . and {space} as long as the very last character in the mask is .  This is the one and only exception where * does not simply match any set of characters.


The above rules are not that complex. But there is one more very important rule that makes the situation confusing: The sourceMask is compared against both the long name and the short 8.3 name (if it exists). This last rule can make interpretation of the results very tricky, because it is not always obvious when the mask is matching via the short name.
It is possible to use RegEdit to disable the generation of short 8.3 names on NTFS volumes, at which point interpretation of file mask results is much more straight forward. Any short names that were generated before disabling short names will remain.
targetMask
Note - I haven't done any rigorous testing, but it appears these same rules also work for the target name of the COPY commmand
The targetMask specifies the new name. It is always applied to the full long name; The targetMask is never applied to the short 8.3 name, even if the sourceMask matched the short 8.3 name.
The presence or absence of wildcards in the sourceMask has no impact on how wildcards are processed in the targetMask.
In the following discussion - c represents any character that is not *, ?, or .
The targetMask is processed against the source name strictly from left to right with no back-tracking.

c - Advances the position within the source name only if the source character is not ., and always appends c to the target name. (Replaces the character that was in source with c, but never replaces .)

? - Matches the next character from the source long name and appends it to the target name as long as the source character is not .  If the next character is . or if at the end of the source name then no character is added to the result and the current position within the source name is unchanged.

* at end of targetMask - Appends all remaining characters from source to the target. If already at the end of source, then does nothing.

*c - Matches all source characters from current position through the last occurance of c (case sensitive greedy match) and appends the matched set of characters to the target name. If c is not found, then all remaining characters from source are appended, followed by c  This is the only situation I am aware of where Windows file pattern matching is case sensitive.

*. - Matches all source characters from current position through the last occurance of . (greedy match) and appends the matched set of characters to the target name. If . is not found, then all remaining characters from source are appended, followed by .

*? - Appends all remaining characters from source to the target. If already at end of source then does nothing.

. without * in front - Advances the position in source through the first occurance of . without copying any characters, and appends . to the target name. If . is not found in the source, then advances to the end of source and appends . to the target name.


After the targetMask has been exhausted, any trailing . and {space} are trimmed off the end of the resulting target name because Windows file names cannot end with . or {space}
Some practical examples
Substitute a character in the 1st and 3rd positions prior to any extension (adds a 2nd or 3rd character if it doesn't exist yet)
ren  *  A?Z*
  1        -&gt; AZ
  12       -&gt; A2Z
  1.txt    -&gt; AZ.txt
  12.txt   -&gt; A2Z.txt
  123      -&gt; A2Z
  123.txt  -&gt; A2Z.txt
  1234     -&gt; A2Z4
  1234.txt -&gt; A2Z4.txt

Change the (final) extension of every file
ren  *  *.txt
  a     -&gt; a.txt
  b.dat -&gt; b.txt
  c.x.y -&gt; c.x.txt

Append an extension to every file
ren  *  *?.bak
  a     -&gt; a.bak
  b.dat -&gt; b.dat.bak
  c.x.y -&gt; c.x.y.bak

Remove any extra extension after the initial extension. Note that adequate ? must be used to preserve the full existing name and initial extension.
ren  *  ?????.?????
  a     -&gt; a
  a.b   -&gt; a.b
  a.b.c -&gt; a.b
  part1.part2.part3    -&gt; part1.part2
  123456.123456.123456 -&gt; 12345.12345   (note truncated name and extension because not enough `?` were used)

Same as above, but filter out files with initial name and/or extension longer than 5 chars so that they are not truncated. (Obviously could add an additional ? on either end of targetMask to preserve names and extensions up to 6 chars long)
ren  ?????.?????.*  ?????.?????
  a      -&gt;  a
  a.b    -&gt;  a.b
  a.b.c  -&gt;  a.b
  part1.part2.part3  -&gt;  part1.part2
  123456.123456.123456  (Not renamed because doesn't match sourceMask)

Change characters after last _ in name and attempt to preserve extension. (Doesn't work properly if _ appears in extension)
ren  *_*  *_NEW.*
  abcd_12345.txt  -&gt;  abcd_NEW.txt
  abc_newt_1.dat  -&gt;  abc_newt_NEW.dat
  abcdef.jpg          (Not renamed because doesn't match sourceMask)
  abcd_123.a_b    -&gt;  abcd_123.a_NEW  (not desired, but no simple RENAME form will work in this case)

Any name can be broken up into components that are delimited by .  Characters may only be appended to or deleted from the end of each component. Characters cannot be deleted from or added to the beginning or middle of a component while preserving the remainder with wildcards. Substitutions are allowed anywhere.
ren  ??????.??????.??????  ?x.????999.*rForTheCourse
  part1.part2            -&gt;  px.part999.rForTheCourse
  part1.part2.part3      -&gt;  px.part999.parForTheCourse
  part1.part2.part3.part4   (Not renamed because doesn't match sourceMask)
  a.b.c                  -&gt;  ax.b999.crForTheCourse
  a.b.CarPart3BEER       -&gt;  ax.b999.CarParForTheCourse

If short names are enabled, then a sourceMask with at least 8 ? for the name and at least 3 ? for the extension will match all files because it will always match the short 8.3 name.
ren ????????.???  ?x.????999.*rForTheCourse
  part1.part2.part3.part4  -&gt;  px.part999.part3.parForTheCourse


Useful quirk/bug? for deleting name prefixes
This SuperUser post describes how a set of forward slashes (/) can be used to delete leading characters (except .) from a file name. One slash is required for each character to be deleted. I've confirmed the behavior on a Windows 10 machine.
ren &quot;abc-*.txt&quot; &quot;////*.txt&quot;
  abc-123.txt        --&gt; 123.txt
  abc-HelloWorld.txt --&gt; HelloWorld.txt

Unfortunately leading / cannot remove . in a name. So the technique cannot be used to remove a prefix that contains .. For example:
ren &quot;abc.xyz.*.txt&quot; &quot;////////*.txt&quot;
  abc.xyz.123.txt        --&gt; .xyz.123.txt
  abc.xyz.HelloWorld.txt --&gt; .xyz.HelloWorld.txt

This technique only works if both the source and target masks are enclosed in double quotes. All of the following forms without the requisite quotes fail with this error: The syntax of the command is incorrect
REM - All of these forms fail with a syntax error.
ren abc-*.txt &quot;////*.txt&quot;
ren &quot;abc-*.txt&quot; ////*.txt
ren abc-*.txt ////*.txt

The / cannot be used to remove any characters in the middle or end of a file name. It can only remove leading (prefix) characters. Also note this technique does not work with folder names.
Technically the / is not functioning as a wildcard. Rather it is doing a simple character substitution following the c target mask rule. But then after the substitution, the REN command recognizes that / is not valid in a file name, and strips the leading / slashes from the name. REN gives a syntax error if it detects / in the middle of a target name.

Possible RENAME bug - a single command may rename the same file twice!
Starting in an empty test folder:
C:\test&gt;copy nul 123456789.123
        1 file(s) copied.

C:\test&gt;dir /x
 Volume in drive C is OS
 Volume Serial Number is EE2C-5A11

 Directory of C:\test

09/15/2012  07:42 PM    &lt;DIR&gt;                       .
09/15/2012  07:42 PM    &lt;DIR&gt;                       ..
09/15/2012  07:42 PM                 0 123456~1.123 123456789.123
               1 File(s)              0 bytes
               2 Dir(s)  327,237,562,368 bytes free

C:\test&gt;ren *1* 2*3.?x

C:\test&gt;dir /x
 Volume in drive C is OS
 Volume Serial Number is EE2C-5A11

 Directory of C:\test

09/15/2012  07:42 PM    &lt;DIR&gt;                       .
09/15/2012  07:42 PM    &lt;DIR&gt;                       ..
09/15/2012  07:42 PM                 0 223456~1.XX  223456789.123.xx
               1 File(s)              0 bytes
               2 Dir(s)  327,237,562,368 bytes free

REM Expected result = 223456789.123.x

I believe the sourceMask *1* first matches the long file name, and the file is renamed to the expected result of 223456789.123.x. RENAME then continues to look for more files to process and finds the newly named file via the new short name of 223456~1.X. The file is then renamed again giving the final result of 223456789.123.xx.
If I disable 8.3 name generation then the RENAME gives the expected result.
I haven't fully worked out all of the trigger conditions that must exist to induce this odd behavior. I was concerned that it might be possible to create a never ending recursive RENAME, but I was never able to induce one.
I believe all of the following must be true to induce the bug. Every bugged case I saw had the following conditions, but not all cases that met the following conditions were bugged.

Short 8.3 names must be enabled
The sourceMask must match the original long name.
The initial rename must generate a short name that also matches the sourceMask
The initial renamed short name must sort later than the original short name (if it existed?)

**参考链接 / References**:
- N/A

---

#### 251. Windows 10 deletes lots of tiny files super slowly. Can anything be done to speed it up?

**问题描述 / Problem Description**:
Tags: windows-10, file-management | Score: 106 | Views: 91313 | Answers: 12

**解决方案 / Solution**:
From the image it looks like you are deleting the files through
Explorer, which is the slowest method possible.
What you can do to improve:

Delete the files using Shift+Del so the
deleted files are not moved to the Recycle Bin
(no recovery possible)

Issue the delete from inside a Command prompt using a command
similar to (use del /? to see all parameters):
  del /f /q *.*           (del in current folder, add `/s` to traverse sub-folders)
  del /f /q /s folder

**参考链接 / References**:
- N/A

---

#### 252. What is the Windows analog of the Linux watch command?

**问题描述 / Problem Description**:
Tags: windows, linux, command-line | Score: 105 | Views: 118690 | Answers: 17

**解决方案 / Solution**:
Write your own. Let's say file watch.bat contains :

@ECHO OFF
:loop
  cls
  %*
  timeout /t 5 &gt; NUL
goto loop


and call it via, for example:

watch echo test


will echo test every 5 seconds.

**参考链接 / References**:
- N/A

---

#### 253. Turning off the cmd window beep sound

**问题描述 / Problem Description**:
Tags: windows, powershell, cmd.exe | Score: 105 | Views: 87047 | Answers: 9

**解决方案 / Solution**:
The Windows command line command net stop beep will turn off the beeping, and net start beep will turn on the beeping.
Source
It should be noted that the instruction stops the beep globally on windows and not on just for within the windows command shell. Also, the service will run again when you reboot your computer.
@Ady's answer will suffice. But if you want to just disable it per instance, you can always put this method into a batch file (but it's so short you can just type it) and run it.

**参考链接 / References**:
- N/A

---

#### 254. What is the equivalent of Linux&#39;s &quot;~&quot; (tilde) shell expansion to home directory in Windows?

**问题描述 / Problem Description**:
Tags: windows, linux, command-line | Score: 105 | Views: 69083 | Answers: 9

**解决方案 / Solution**:
You can use cd /d %USERPROFILE% if you use cmd.

or you can use cd ~ if you use PowerShell.

**参考链接 / References**:
- N/A

---

#### 255. How to change shortcut key for switching between virtual desktops in windows 10 or windows 11?

**问题描述 / Problem Description**:
Tags: windows-10, keyboard-shortcuts, windows-11, windows-10-preview, windows-11-22h2 | Score: 105 | Views: 189778 | Answers: 10

**解决方案 / Solution**:
What you need is as follows:


Snapping window: WIN+LEFT or RIGHT
(can be used with UP or DOWN to get into
quadrants)
Switch to recent window: Alt+Tab (unchanged) –
Hold shows new Task view window view, let go and switches to app.
Task view: WIN+Tab – New Task view opens up and
stays open.
Create new virtual desktop:
WIN+Ctrl+d
Close current virtual desktop:
WIN+Ctrl+F4
Switch virtual desktop:
WIN+Ctrl+LEFT or RIGHT

**参考链接 / References**:
- N/A

---

#### 256. How can I change the timestamp on a file?

**问题描述 / Problem Description**:
Tags: windows, timestamp, sysinternals | Score: 104 | Views: 302437 | Answers: 5

**解决方案 / Solution**:
Due to William Jackson's answer, I found a similar question on Stack Overflow.

The accepted answer states to use Powershell and these commands:

$(Get-Item ).creationtime=$(Get-Date "mm/dd/yyyy hh:mm am/pm")
$(Get-Item ).lastaccesstime=$(Get-Date "mm/dd/yyyy hh:mm am/pm")
$(Get-Item ).lastwritetime=$(Get-Date "mm/dd/yyyy hh:mm am/pm")


Edit

Two examples:

(This one is from the comments:) Set the last-access time for a file aaa.csv to the current time:

$(Get-Item aaa.csv).lastwritetime=$(Get-Date)


Set the creation time of a file foo.txt to November 24, 2015, at 6:00am:

$(Get-Item foo.txt).creationtime=$(Get-Date "11/24/2015 06:00 am")

**参考链接 / References**:
- N/A

---

#### 257. OpenVPN: Only route a specific IP addresses through VPN?

**问题描述 / Problem Description**:
Tags: windows, routing, openvpn, tunnel | Score: 104 | Views: 277462 | Answers: 5

**解决方案 / Solution**:
The correct configuration for OpenVpn is:
route-nopull 
route 192.168.0.0 255.255.255.0

These entries belong in your .ovpn file and will direct all 192.168.0.* subnet traffic through the VPN.
For one IP only (192.168.0.1):
route-nopull 
route 192.168.0.1 255.255.255.255

BTW: route-nopull means &quot;don't pull routes from the server&quot;

**参考链接 / References**:
- N/A

---

#### 258. Commmand line command to copy entire directory (including directory folder) to another directory

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 104 | Views: 563354 | Answers: 12

**解决方案 / Solution**:
Try using XCOPY with the /E switch. More info here.
I haven't had to access this information from my brain in years!
UPDATE
The documentation says that it copies all files and subdirectories from the source directory (meaning that the parent directory is not created), so you would have to create test in C:\test2 first and then use XCOPY.

**参考链接 / References**:
- N/A

---

#### 259. Fake broken pixel on Windows 10

**问题描述 / Problem Description**:
Tags: windows, video, display | Score: 104 | Views: 18449 | Answers: 6

**解决方案 / Solution**:
That's not even a fake broken pixel. It's a 1&times;1px window &ndash; it even has the same Windows&nbsp;10-style shadow that windows usually have.

It might be a window that is supposed to remain hidden (programs often use invisible windows because that's required for receiving e.g. global keyboard shortcuts or other system events), yet sometimes &ndash; due to bugs in the software &ndash; such windows end up being listed in Alt+Tab or even shown on-screen anyway.

Various "Task Manager replacement" tools (such as Process&nbsp;Explorer) have a function  where you can just point at a window and the corresponding process will be highlighted. This will narrow it down to a specific program.

The regular Windows 10 Task Manager also has a "Startup" tab where all the startup programs can be disabled. Try disabling them all; if the pixel disappears, re-enable one, or half of them¹, repeating until you find the one that's showing the window. (Although there is a small chance that it's launched by a service and not by a startup program.)

¹ (Systems tend to accumulate so much cruft in the "Startup" list that I suspect you should just keep the remaining half permanently disabled anyway...)

**参考链接 / References**:
- N/A

---

#### 260. What are all the Windows 7/8/8.1 updates (KBs) I must skip to avoid Windows 10 upgrading -and nags-?

**问题描述 / Problem Description**:
Tags: windows, windows-update | Score: 104 | Views: 84384 | Answers: 6

**解决方案 / Solution**:
Attempting to block the upgrade to Windows 10 by not installing certain updates is the incorrect approach of permanently preventing the upgrade to Windows 10.  By setting the DisableOSUpgrade registry key, you block the upgrade entirely, despite any prompts to upgrade.

As outline in this support article:  How to manage Windows 10 notification and upgrade options


  To block the upgrade to Windows 10 through Windows Update, specify the
  following registry value:
  
  Subkey: HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate 
  
  DWORD value: DisableOSUpgrade = 1


In order to disable the Get Windows 10 notification icon do the following:


  For non-Enterprise versions of Windows, the notification icon can be
  suppressed through the Windows registry. To do this, set the following
  registry value:
  
  Subkey: HKLM\Software\Policies\Microsoft\Windows\Gwx 
  
  DWORD value: DisableGwx = 1


It is worth pointing out the upgrade itself will automatically be blocked in the following condition:


  The computer or device is serviced through WSUS and has not had update
  3035583 applied.


The group policy changes requires these updates:

Windows Update Client for Windows 7 and Windows Server 2008 R2: July 2015

Windows Update Client for Windows 8.1 and Windows Server 2012 R2: July 2015

**参考链接 / References**:
- N/A

---

#### 261. Why the heck does NTFS allow invisible executables?

**问题描述 / Problem Description**:
Tags: windows, ntfs, virus, alternate-data-stream | Score: 104 | Views: 4152 | Answers: 5

**解决方案 / Solution**:
There are two sides to this question. The first is why does this feature exist at all, and the second is why doesn't the GUI (or the command prompt) make it easier to see and manage the feature.

It exists because it's useful. Several other platforms support multiple data streams per file. On the Mac, they were called forks, for example. I'm reasonably sure that similar things existed in the mainframe world, but can't put my fingers on any explicit examples today.

On modern Windows, it is used to hold extra attributes for a file. You might notice that the Properties box available from Windows Explorer has a Summary tab that in Simple view (I'm on Windows XP, your mileage will differ on the other flavors) includes a bunch of useful fields like Title, Subject, Author, and so forth. That data is stored in an alternate stream, rather than creating some kind of side-car database to hold it all that would get separated from the file too easily.

An alternate stream is also used to hold the marker that says the file came from an untrusted network source that is applied by both Internet Explorer and Firefox on downloads.

The hard question is why there isn't a better user interface for noticing that the streams exist at all, and why it is possible to put executable content in them and worse, execute it later. If there is a bug and security risk here, this is it.

Edit: 

Inspired by a comment to another answer, here is one way to find out if your anti-virus and/or anti-malware protection is aware of alternate streams.

Get a copy of the EICAR test file. It is 68 bytes of ASCII text that happens to also be a valid x86 executable. Although completely harmless, it has been agreed by the anti-virus industry to be detected as if it were a real virus. The originators thought that testing AV software with a real virus would be a little too much like testing the fire alarm by lighting the wastebasket on fire...

The EICAR file is:

X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*


Save it with the extension .COM and it will execute (unless your AV is paying attention) and print a greeting.

It would be informative to save it in an alternate data stream and run a scan...

**参考链接 / References**:
- N/A

---

#### 262. What is Git Bash for Windows anyway?

**问题描述 / Problem Description**:
Tags: windows, bash, rsync, git-bash, mingw | Score: 104 | Views: 173266 | Answers: 2

**解决方案 / Solution**:
Summary

You are correct, Git Bash for Windows is not just bash compiled for Windows. It's package that contains bash (which is a command-line shell) and a collection of other, separate *nix utilities like ssh, scp, cat, find and others (which you run using the shell), compiled for Windows, and a new command-line interface terminal window called mintty.

In a nutshell

On Windows you might run commands like ipconfig /all or format G: using cmd.exe. These commands are actual executable files under C:\Windows\system32, stored as ipconfig.exe and format.com files. cmd.exe is separate from both and loads and runs them on user's request.

ssh, scp, cat, find are run using bash in exactly the same way. They are usually stored under /usr/bin rather than in C:\Windows\system32 on *nix systems, because Windows and *nix have their system file structure organised differently.

In the case of Git Bash for Windows these programs are located in the Git installation folder: C:\Program Files\Git\usr\bin, which can also be found in the emulated Linux environment under /usr/bin.

Just like being able to just run cmd.exe on *nix doesn't allow you to do much without the other system utilities, just being able to run Bash on Windows is not very useful either. This means that all these extra commands have to be bundled together with Bash to create a usable software package.

Details: POSIX applications on Windows

Normally those extra commands would be found on *nix systems and not on Windows, because they have been programmed against the POSIX programming API (which is what *nix uses), and not the Win32 APIs (which is what Windows uses). POSIX API documentation is openly available, so some people have ported it to other systems, including Windows. Windows implementation of POSIX APIs/libraries are provided by Cygwin and MSYS.

This is kind of similar to what the Wine project does, but it converts POSIX->Windows rather than Windows->POSIX like Wine does.

mintty

mintty is included because cmd.exe, the default Windows command line window, is missing some important features which are normally available on most *nix systems. In most cases, mintty is a better choice for running commands (certainly for the utilities that come with the Git Bash for Windows package), but occasionally a Windows system application may work better with cmd.exe.

**参考链接 / References**:
- N/A

---

#### 263. Is it possible to disable smooth movement of the cursor in Office 2013/windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, microsoft-office-2013, cursor | Score: 104 | Views: 74190 | Answers: 5

**解决方案 / Solution**:
Well, yes. There are two ways of doing this.
One is described in many places (here, for one) and goes like this:

In regedit, navigate to HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Common
If there's no Graphics key under that Common key, right-click on the Common key and select New &gt; Key. Type in Graphics for the key name.
With the Graphics key selected, right-click on the right side of the editor and create a new DWORD value. Name it DisableAnimation.
Finally, double-click the DisableAnimation value and change the value to 1. Hit OK and exit the editor, then restart Windows for it to take effect.

Note that for Office 2016, the DWORD key is under HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Graphics and it should be called DisableAnimations (plural).
The other way is through the System Performance Settings.

Open &quot;System&quot; (by typing Win+Pause)
Click the &quot;Advanced system settings&quot; in the top left.
In the &quot;System Properties&quot; window (don't you just love consistency?), go to the &quot;Advanced&quot; tab and click the &quot;Settings&quot; button in the first section, &quot;Performance&quot;.
In the &quot;Performance Options&quot; window, on the &quot;Visual Effects&quot; tab, deselect the first option, &quot;Animate controls and elements inside windows&quot;. You may want to disable a bunch of other useless animations here, too, but don't disable the &quot;Smooth edges of screen fonts&quot;. Curiously, you don't have to restart Windows if you do it this way.

Edit: The latter method may look very different on Windows 10, sorry I missed that part.

**参考链接 / References**:
- N/A

---

#### 264. How can I make a Windows PC bullet-proof for home users?

**问题描述 / Problem Description**:
Tags: windows, security, virus, malware | Score: 103 | Views: 17814 | Answers: 23

**解决方案 / Solution**:
Probably the best advice I've ever heard on the topic is: Stop running as an administrator.

**参考链接 / References**:
- N/A

---

#### 265. How can I take a screenshot that includes the mouse cursor?

**问题描述 / Problem Description**:
Tags: windows, screenshot, mouse-cursor | Score: 103 | Views: 127773 | Answers: 16

**解决方案 / Solution**:
IrfanView has an option to include the cursor while taking screenshots. Press C to configure options and the hotkey.
It is free for private, educational, and non-commercial use.

**参考链接 / References**:
- N/A

---

#### 266. How do I press Ctrl+Alt+Delete in VirtualBox?

**问题描述 / Problem Description**:
Tags: windows, virtualbox, ctrl-alt-delete | Score: 102 | Views: 389324 | Answers: 3

**解决方案 / Solution**:
Usually there is an entry in a menu somewhere. Host key+Del1 should work too, though.

If you're using Remote Desktop, then use Ctrl+Alt+End instead.



1 You should know what your host key is, but it's configurable. Mine usually was Right Ctrl.

If you want to know what your Host Key is, open VirtualBox and go to File → Preferences → Input. If you don't like the current key, you can change it to whatever you wish.

**参考链接 / References**:
- N/A

---

#### 267. Are there solutions that can limit the CPU usage of a process?

**问题描述 / Problem Description**:
Tags: windows-7, windows, cpu | Score: 102 | Views: 299241 | Answers: 11

**解决方案 / Solution**:
A search over the net brings some programs that may help. They are all freeware.

BES - Battle Encoder Shirase


  BES is a small tool which limits the
  CPU usage for a specified process: for
  instance, you can limit the CPU usage
  of a process which would use CPU 100%,
  down to 50% (or any percentage you
  like). With this, you can use other
  programs comfortably while doing
  something CPU-intensive in the
  background. By limiting the CPU load,
  you can also cool down your CPU
  immediately when it happens to get too
  hot. Of course the processing speed
  will slow down proportionally if you
  limit the CPU usage, but it should be
  much better than crashing because of
  heat or (in the worst scenario) having
  your computer broken with a burned
  CPU.


Process Tamer


  Process Tamer is a tiny (140k) and
  super efficient utility for Microsoft
  Windows XP/2K/NT/Vista/Win7 that runs
  in your system tray and constantly
  monitors the cpu usage of other
  processes. When it sees a process that
  is overloading your cpu, it reduces
  the priority of that process
  temporarily, until its cpu usage
  returns to a reasonable level.


Process Lasso


  Process Lasso is a unique new
  technology that will improve your PC's
  responsiveness and stability during
  periods of high CPU load. Windows, by
  design, allows programs to monopolize
  your CPU without restraint -- leading
  to freezes, hangs, and micro-lags.
  Process Lasso's ProBalance (Process
  Balance) technology intelligently
  adjusts the priorities of running
  programs so that badly behaved
  processes won't negatively impact the
  responsiveness of your PC.

**参考链接 / References**:
- N/A

---

#### 268. How to unzip a file using the cmd?

**问题描述 / Problem Description**:
Tags: windows, command-line, zip | Score: 101 | Views: 615492 | Answers: 6

**解决方案 / Solution**:
On Windows 10 build 17063 or later you can use tar.exe (similar to the *nix one). This is also available in the nanoserver docker container
C:\&gt; tar -xf archive.zip

Note: zip support is not well documented
ref: https://www.freebsd.org/cgi/man.cgi?query=bsdtar&amp;sektion=1&amp;manpath=FreeBSD+5.3-stable

**参考链接 / References**:
- N/A

---

#### 269. run powershell command from cmd

**问题描述 / Problem Description**:
Tags: windows, command-line, powershell, cmd.exe, process | Score: 101 | Views: 447352 | Answers: 2

**解决方案 / Solution**:
powershell -command "get-process | ? {$_.Description -eq 'Sysinter Process Explorer'} | select processname | out-file $env:APPDATA\example.txt"


basically you have a powershell command and paste it in between these quotes to call it from CMD

powershell -command " #PasteCodeHere " 

inside these quotes you have to work with ' otherwise it will interrupt your command parameter. 

Edit: Additional Information:

quite often you will encounter this: powershell -command "&amp; 'somestuff'" 

the &amp; is used to call a File. when you're only using a command &amp; is unnessecary, when you want to call a script, you should use it. 

powershell -command "&amp; 'C:\foobar.ps1'" 

You could also use powershell -file C:\file.ps1 to call a script

**参考链接 / References**:
- N/A

---

#### 270. Insert Unicode characters via the keyboard

**问题描述 / Problem Description**:
Tags: windows-7, windows, characters | Score: 101 | Views: 159610 | Answers: 10

**解决方案 / Solution**:
According John D. Cook, there are three ways:


In Microsoft Word you can insert Unicode characters by typing the hex
value of the character then typing
Alt-x. You can also see the Unicode
value of a character by placing the
cursor immediately after the character
and pressing Alt-x. This also works in
applications that use the Windows rich
edit control such as WordPad and
Outlook.
Another approach which works with more applications is as follows. First
create a registry value under key
HKEY_CURRENT_USER\Control Panel\Input Method of type REG_SZ
called EnableHexNumpad, set its
value to 1, and reboot. Then you can
enter Unicode symbols by holding down
the Alt key and typing the plus sign
on the numeric keypad followed by the
character value. When you release the
Alt key, the symbol will appear. This
approach worked with most applications
I tried, including Firefox and Safari,
but did not with Internet Explorer.
Another option is to install the UnicodeInput utility. This worked
with every application I tried,
including Internet Explorer. Once
installed, the window below pops up
whenever you hold down the Alt key and
type the plus sign on the numeric
keypad. Type the numeric value of the
character in the box, click the Send
button, and the character will be
inserted into the window that had
focus when you clicked Alt-plus.


I would go for the second option, because it integrates nicely with your current usage.

**参考链接 / References**:
- N/A

---

#### 271. How do I set Notepad++ as the default editor?

**问题描述 / Problem Description**:
Tags: windows-7, windows, notepad++, file-association | Score: 101 | Views: 147890 | Answers: 5

**解决方案 / Solution**:
Start Notepad++ with elevated privileges.


In Notepad++, go to Settings, Preferences...
Go to the File Association tab.
Select fortran,TeX,SQL and then .sql and add it to the registered extensions:  


Click Close.

**参考链接 / References**:
- N/A

---

#### 272. How do I mount a network drive to a folder?

**问题描述 / Problem Description**:
Tags: windows, network-shares, shared-folders | Score: 100 | Views: 290708 | Answers: 7

**解决方案 / Solution**:
In Windows Vista or Windows 7, you can create a "junction folder"/"Symbolic link" to redirect the contents of one to another.

Simply type:

mklink /d "c:\data\network docs" "\\server\shareddata\"


I have not tested it with a FQDN, but as far as I can tell, it should work. I have tested it with a network mapped drive, and this works perfectly... so at a last resort, you can map first, then do this.

The /d creates a directory (c:\data\network docs in this example) and it must not exist. It will be created by this command.

You must have admin privileges when you run CMD.  You can do this under an admin account by pressing ctrl-shift-enter instead of enter when you run CMD.

The end result is also achievable in Windows XP, but it is not as easy. Guide here

**参考链接 / References**:
- N/A

---

#### 273. How to avoid keyboard layout automatically changing on Windows?

**问题描述 / Problem Description**:
Tags: windows, windows-xp, keyboard, keyboard-layout | Score: 100 | Views: 210078 | Answers: 12

**解决方案 / Solution**:
By default ALT+LEFT SHIFT is used to switch between languages. Far too easy to press these by mistake, especially if you're like me and prefer the keyboard to the mouse.

To change this, go into Control Panel/Regional Settings/Languages/Details and there is a button that allows you to configure the shortcuts to switch languages - I just disable it altogether.

In Windows 7 this is Control Panel/Region and Language/Keyboards and Languages/Change Keyboards/Advanced Key Settings.

You may also want to disable automatic detection of languages in Word (Tools/Languages). I think this may switch the keyboard layout to match the detected language.

**参考链接 / References**:
- N/A

---

#### 274. Why can&#39;t you uninstall multiple programs at once in Windows?

**问题描述 / Problem Description**:
Tags: windows-7, windows, uninstall | Score: 100 | Views: 28508 | Answers: 4

**解决方案 / Solution**:
If you read anything about how the Windows installer system works, it's obvious they applied some ideas from transactional databases to program installation and maintenance, not to mention the .msi files themselves are a database.

There is always the question in designing any database - do you want speed or accuracy/safety?  Given that installers can modify system configuration and that a mishap could render the system inoperable, safety has been given a priority over speed.  One of the reasons why .msi installers are so slow is because rollback files are made for each file, etc. that will be modified, and then deleted afterwards - allowing any changes to be "rolled back" if something goes wrong in the middle of things (such as a power outage or system crash).

Now, I believe the MSI engine itself enforces installing, modifying, or removing only one program at a time - if you try to run an .msi while another is uninstalling, for example, it either won't run or will wait for the currently running uninstall to finish.  Non-MSI installers may not behave this way - since they don't use the MSI engine.  But because of this safety design decision, this is probably why appwiz.cpl insists on only letting one uninstaller be called at once.

CCleaner allows you to kick off uninstallers without waiting for previously running ones to finish.  MSI installers will likely still not work in parallel due to the above.

**参考链接 / References**:
- N/A

---

#### 275. Equivalent of chmod to change file permissions in Windows

**问题描述 / Problem Description**:
Tags: windows, chmod, file-attributes | Score: 100 | Views: 655210 | Answers: 9

**解决方案 / Solution**:
Greg mentions attrib - but attrib  isn't anywhere close to chmod - attrib can set Read-only/Hidden attributes of a single file - it doesn't provide fine-grained controls like icacls does.
icacls sets/resets the access control lists, so you can grant/deny rights for individual SIDs &amp; groups. It is fairly complicated though.
Here's an example I have saved in my github gist; it resets the ownership and access control list for all files in a folder and is particularly useful to fix those annoying &quot;You need permissions from .. to perform this action&quot; especially when moving files over from a previous install:
icacls * /reset /t /c /q 

Here, we have that

/reset replaces the existing one with the default list. 
/t acts recursively on all files, folders &amp; subfolders 
/q doesn't display any success messages 
/c continues with remaining files even in an error occurs.

You can also do things like backup the existing ACLs &amp; apply them across all. Have a look at ss64 which explains the different options &amp; switches very well.

**参考链接 / References**:
- N/A

---

#### 276. Stopping all automatic updates Windows 10

**问题描述 / Problem Description**:
Tags: windows-update, windows-10 | Score: 100 | Views: 36032 | Answers: 17

**解决方案 / Solution**:
if you have the Pro Edition, open group policy editor (gpedit.msc) search for the Configure automatic updates entry, located at:
computer configuration → administrative templates → windows components → windows update


and select Notify for download and notify for install.
When Windows detects new updates it shows a toast notification.

You can also use the troubleshooter from Update KB3073930 to disable some problematic updates, so that they are not installed again.


This is the official way from Microsoft to prevent setup of unwanted updates and drivers.
But there is a 3rd party tool called Windows Update MiniTool which allows to select which updates can be installed and allows to block updates like you could in former Windows versions.


An alternative to the standard Windows Update What you can do: • Check
for updates  • Download updates • Installing Updates •
Deleting installed updates • Hiding unwanted updates • Get
direct links to the *.cab / *.Exe / *.Psf update files • View update
history • Configure Automatic Updates • This tool is like the
external powershell module PSWindowsUpdate, but much more advanced and
user-friendly features • The tool relies and use same WU
infrastructure, all downloading are through WU it's not a
downloader

The user slavanap posted a 2nd tool in a comment which allows you to selectively install updates. It is called Windows10 Manual Update and is available on github:
.
In the Windows 10 creators Update, there is an option to stop Windows Updates for 35 days:





under Settings App where the Windows Update options are.

**参考链接 / References**:
- N/A

---

#### 277. How to remove read-only attribute recursively on Windows

**问题描述 / Problem Description**:
Tags: windows, command-line, batch, file-attributes | Score: 99 | Views: 256895 | Answers: 5

**解决方案 / Solution**:
I would use the ATTRIB command, for example:

attrib -r c:\folder\*.* /s


attrib is the command
-r is the flag for removing read-only attributes
c:\folder\*.* is the folder you are running it on, plus wildcards for all files
/s is the flag for doing all sub directories and files

Here is some more documentation and examples for the attrib command: 
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/attrib

**参考链接 / References**:
- N/A

---

#### 278. Can I delete MSOCache?

**问题描述 / Problem Description**:
Tags: windows, microsoft-office | Score: 99 | Views: 296913 | Answers: 8

**解决方案 / Solution**:
Short answer: no. You would most likely no longer be able to perform a repair or install additional components.
I have tried it myself on a virtual machine running Windows 7 with Office 2007–I imagine it would have the same effect on Office 2010.
A safer option (as suggested here) is to burn the folder itself to DVD or move it to a USB drive, and change all references to it in the Windows registry.
From that page:

Solution, what I did recently:

Burn that whole folder to a CD-R or DVD (the filesize of that folder
depends upon your Office version).
Delete that folder.
Search the registry in RegEdit for C:\MSOCache and change all references
to point to your CD/DVD drive,
example:
E:\MSOCache (will of course require the disc when something Office related needs those cache files.)

**参考链接 / References**:
- N/A

---

#### 279. How can I find out the command line options for git-bash.exe?

**问题描述 / Problem Description**:
Tags: windows, command-line, git-bash | Score: 99 | Views: 92459 | Answers: 4

**解决方案 / Solution**:
I found this commit from 2015 that introduced new command line options:
https://github.com/git/git/commit/ac6b03cb4197311b055dc5f46ab10bf37c591ae6

Here is the list from the commit description:

--command=&lt;command-line&gt;::
    Executes `&lt;command-line&gt;` instead of the embedded string resource

--[no-]minimal-search-path::
    Ensures that only `/cmd/` is added to the `PATH` instead of
    `/mingw??/bin` and `/usr/bin/`, or not

--[no-]needs-console::
    Ensures that there is a Win32 console associated with the spawned
    process, or not

--[no-]hide::
    Hides the console window, or not


You can read the full information in the URL above.

**参考链接 / References**:
- N/A

---

#### 280. Pin applications to multiple desktops in Windows 10

**问题描述 / Problem Description**:
Tags: multiple-monitors, windows-10, virtual-desktop | Score: 99 | Views: 56621 | Answers: 3

**解决方案 / Solution**:
The feature has now been released as one of several "Virtual Desktop Improvements" in the Windows 10 Anniversary Update (Build 14316):


  You can now pin a window so it’s available on every desktop. To do this, launch Task View then right-click on the window you want to pin and choose “Show this window on all desktops”. Try pinning Skype or Groove Music so they’re always at your fingertips. And if you have a multi-mon setup, you might enjoy the ability to have your email app on the second monitor no matter which desktop you switch to.

**参考链接 / References**:
- N/A

---

#### 281. What&#39;s the difference between stereo and hands free?

**问题描述 / Problem Description**:
Tags: windows-10, audio, bluetooth | Score: 99 | Views: 501110 | Answers: 3

**解决方案 / Solution**:
The "Stereo" device is technically known in Bluetooth jargon as "Advanced Audio Distribution Profile", or with an acronym A2DP. It is optimized for transferring 2-channel stereo sound with good quality in one direction only.

The "Hands-free" device corresponds, respectively, to either the "Hands-Free Profile" (HFP) or "Headset Profile" (HSP). Both of them are older than A2DP, and were initially designed to pass telephone-quality sound (2-directional mono sound, limited frequency response, optimized for speech only). Both of them, and in particular the HSP profile, are designed to minimize the processing power requirements. This was important for wireless Bluetooth hands-free devices, which usually had, and still have, an extremely limited amount of battery power available because of limitations of physical size.

Since then, HFP has been expanded with optional better-quality sound codecs, as newer high-efficiency processors have made it easier to implement more complicated protocols and sound codecs in low-power devices. HSP has remained the minimalist implementation, to be used when every milliwatt-second of battery capacity needs to be used efficiently, and as a fallback to be used if the more advanced protocols aren't compatible.

The reason why the A2DP device gets disabled when two-way communications is required is probably again related to processing power requirements. Running both HFP/HSP and A2DP simultaneously would require running two potentially very different codec modules simultaneously, and then mixing their outputs either in digital or analog form. Digital mixing would increase processing power requirements still further, while analog mixing would make the device hardware design more complicated. 

Disabling A2DP while HFP or HSP is active is the easy way out: it will reduce both technical complexity and the power budget of the device.

**参考链接 / References**:
- N/A

---

#### 282. Option to Turn Bluetooth on or off is Missing

**问题描述 / Problem Description**:
Tags: bluetooth, windows-10 | Score: 99 | Views: 1435568 | Answers: 15

**解决方案 / Solution**:
Bring up the start menu. Search for "Device Manager".
Go to "View" and click "Show hidden devices"
In Device Manager, expand Bluetooth.
Right click on Bluetooth Generic Adapter and update the driver.
Restart.


Worked for me. :)

**参考链接 / References**:
- N/A

---

#### 283. How do I determine if my Windows is 32-bit or 64-bit using a command?

**问题描述 / Problem Description**:
Tags: windows, command-line | Score: 98 | Views: 359661 | Answers: 5

**解决方案 / Solution**:
From an elevated command prompt, type wmic os get osarchitecture.  The output is pretty obvious, I think - it'll return either "32-bit" or "64-bit".

**参考链接 / References**:
- N/A

---

#### 284. How can I check a system&#39;s current NTP configuration?

**问题描述 / Problem Description**:
Tags: windows, command-line, batch-file, date-time, ntp | Score: 98 | Views: 1811121 | Answers: 6

**解决方案 / Solution**:
In the command line, type 

w32tm /query /configuration
w32tm /query /status
Time /T 


w32tm /query /configuration gives you the configuration you have set up.

w32tm /query /status gives you information such as:


stratum
leap indicator
precision
last sync
NTP server
poll interval


time /T outputs the current system time.

Note: w32tm /query was first made available in the Windows Time client versions of Windows Vista, and Windows Server 2008. See Windows Time Service Tools and Settings

**参考链接 / References**:
- N/A

---

#### 285. Virtual Box - not filling entire screen

**问题描述 / Problem Description**:
Tags: windows-7, windows, virtualbox, virtual-machine, virtualization | Score: 98 | Views: 333253 | Answers: 8

**解决方案 / Solution**:
You must install guest additions.
In the "Devices" menu in the virtual machine's menu bar, VirtualBox has a handy menu item named "Install guest additions", which mounts the Guest Additions ISO file inside your virtual machine. A Windows guest should then automatically start the Guest Additions installer, which installs the Guest Additions into your Windows guest.
After that your virtual OS scren will be automatically change resolution to fill entire screen.

**参考链接 / References**:
- N/A

---

#### 286. How to remove items from the right click (context) menu in Windows?

**问题描述 / Problem Description**:
Tags: windows, context-menu | Score: 98 | Views: 220979 | Answers: 5

**解决方案 / Solution**:
I've written a lengthy explanation of how to clean up a messy context menu, using either the registry editor:

If you want to clean things up the truly geeky way, you can open up regedit.exe through the start menu search or run box, and then browse down to one of the following keys…
Most of the menu items that used for all files and folders can be found by looking at one of these keys:
HKEY_CLASSES_ROOT\*\shell

HKEY_CLASSES_ROOT\*\shellex\ContextMenuHandlers

HKEY_CLASSES_ROOT\AllFileSystemObjects\ShellEx

Items that are specific to folders can usually be found in one of these keys instead:
HKEY_CLASSES_ROOT\Directory\shell

HKEY_CLASSES_ROOT\Directory\shellex\ContextMenuHandlers


You can read more at: How to Clean Up Your Messy Windows Context Menu
Or use some freeware NirSoft tools like ShellMenuView or ShellExView.

**参考链接 / References**:
- N/A

---

#### 287. Disable Win + Space keyboard layout switch in Windows 10

**问题描述 / Problem Description**:
Tags: windows-10, keyboard-shortcuts, keyboard-layout | Score: 98 | Views: 115966 | Answers: 9

**解决方案 / Solution**:
You can also use the new PowerToys for Windows 10 to remap it.  In my case, I remapped it so that it brings up PowerToys Run when I press Win + Space.

**参考链接 / References**:
- N/A

---

#### 288. Disable automatic restarts of Windows 11 (Pro)

**问题描述 / Problem Description**:
Tags: windows, windows-11 | Score: 97 | Views: 127173 | Answers: 5

**解决方案 / Solution**:
You can disable automatic restart after installing updates in the Group Policy Editor.

Open the Group Policy Editor (gpedit.msc).
Go to Administrative Templates &gt; Windows Components &gt; Windows Update &gt; Manage end user experience.
Double-click on “No auto-restart with logged on users for scheduled automatic updates installations”.
Select Enabled, and then select OK.

Note: See comments, you also need to enable 'Configure Automatic Updates'

**参考链接 / References**:
- N/A

---

#### 289. Why is DNS apparently involved in issuing &quot;dir&quot; on Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, command-line, dns, cmd.exe, dir | Score: 97 | Views: 10740 | Answers: 2

**解决方案 / Solution**:
The second cmd.exe fails to locate and subsequently load the localized strings from the cmd.exe.mui satellite resource library.

Here is what it really attempts to say, taken from a 10.0.18362.1 (160101.0800):


0x235F: "Volume in drive %1 is %2"
0x235B: "Volume Serial Number is %1"
0x2339: "Directory of %1"


This is actually the first three lines of a plain dir command output.

This is a funny one. There are no entries for messages numbers 0x235F and 0x235B in the default system message table. So for the first two outputs, you get that cryptic message as shown in @harrymc's console screenshot.

But for 0x2339, there is an entry in the default system message table, physically stored in KernelBase.dll.mui pointing to the text "DNS bad key":



It just so happens to share the number of the "Directory of %1" line of the command processor's resources: a fallback not anticipated by the developers of cmd.exe. So the DNS reference is just a coincidence, it could be anything.

Note that the proper message contains a variable argument (the directory name), while the DNS message doesn't. I guess that's why there is no more output after that - it might just terminate.

**参考链接 / References**:
- N/A

---

#### 290. What is the best way to remove 100% of a software that is not yet installed?

**问题描述 / Problem Description**:
Tags: windows, uninstall | Score: 96 | Views: 15067 | Answers: 13

**解决方案 / Solution**:
No extra hardware required:

The &quot;probably good enough&quot; approach would be to make a System Restore point before installing the software and rollback to it later. Some configuration and temporary files etc. can remain after this, as System Restore is preserving user files and only restoring executables to the earlier state, but without anything to make use of them these files will be harmless. They can take up a (probably insignificant) amount of disk space, but they won't make a difference security- and privacy-wise.

Extra disk required:

You can take a full disk image (or OS partition image) to an external drive before installing software in question and restore the image later. This will undo everything that happened on that disk in the meantime, including changes in user files, so if you're using a password manager etc. make sure you have an independent copy on another media.

If you have a second internal disk of at least the same size and without anything important on it, you can clone the system disk to that one, swap them and install the software on the cloned disk. Once you're done just repartition &amp; format the clone. Your original disk stays untouched the entire time.


Some extra disk space required:

The ultimate approach would be to install a throwaway OS just for this purpose. The advantage of this method is that it will protect all your data from being accessed by potentially rogue software, assuming that you're using a separate/clean disk or other partitions are not mounted. Combine this with a full disk image and you can do without actually swapping any hardware and without a spare disk (except for an external disk for the image).

USB flash drive or external drive required:

A variant of the &quot;throwaway OS&quot; approach is to use a live system on a USB flash drive/external drive, namely the Windows To Go feature. You could use Rufus to create a Windows To Go flash drive from an official ISO downloaded from Microsoft (also possible with Rufus). You can then boot from that USB media to a clean Windows install without affecting your main OS. Make sure that your disk partitions are not mounted for privacy. (Thanks to @MechMK1 and @Akeo for suggesting this in the comments!)

Possible alternatives:

There's also software that makes sure the disk is restored to a previous snapshot on each boot. I've never used it though, so I don't know how effective it would be for your use case.

**参考链接 / References**:
- N/A

---

#### 291. View a list of symbolic links on system?

**问题描述 / Problem Description**:
Tags: windows, ntfs, symbolic-link | Score: 96 | Views: 228796 | Answers: 7

**解决方案 / Solution**:
Try the following command:

dir /AL /S C:\



/A displays all files with a specific attribute, and L specifies reparse points (symlinks and directory junctions)
/S makes the command recursive
replace C:\ with the drive letter you want to scan, or with a path if you don't want to scan an entire drive

**参考链接 / References**:
- N/A

---

#### 292. Using robocopy and excluding multiple directories

**问题描述 / Problem Description**:
Tags: windows, windows-server-2008-r2, robocopy | Score: 96 | Views: 436615 | Answers: 8

**解决方案 / Solution**:
I figured it out with a little trial and error and the /L (to test the command before doing it for real). The command I end up with is:

robocopy G: C:\backup /MIR /XD G:\dir1 "G:\dir 2" G:\dir3 ...


Apparently, including trailing slashes keeps robocopy from parsing the list of directories correctly, so be sure not to include trailing slashes on directory names and remember to put quotes around directories with spaces in the name.

The /MIR option maintains the same directory structure while copying the files.

Edit: After some more research, I improved the command a bit:

robocopy G: C:\backup /MIR /Z /LOG:C:\todaysdate-backup.log /XF *.iso *.log *.au /XD G:\dir1 ...


The additions are as follows:


/Z allows the job to be restarted
/LOG:&lt;logfile path&gt; is pretty self-explanatory.
/XF is being used to exclude certain filetypes so it doesn't take so long

**参考链接 / References**:
- N/A

---

#### 293. How to search for only folders in Windows 7 instead of folders AND files

**问题描述 / Problem Description**:
Tags: windows-7, windows, windows-search | Score: 95 | Views: 162071 | Answers: 8

**解决方案 / Solution**:
From the Windows Search Advanced Query Syntax page, use the following search items:

To restrict by file type    Use            Example
------------------------    ---            -------
Folders                     folders        kind:folders
Folder name                 foldername     foldername:mydocs

**参考链接 / References**:
- N/A

---

#### 294. How to convert .img to usable VirtualBox format

**问题描述 / Problem Description**:
Tags: windows, virtualbox, virtual-machine, iso-image, virtual-disk | Score: 95 | Views: 403957 | Answers: 2

**解决方案 / Solution**:
Select a virtual machine by clicking its name in the VirtualBox window
Click the Machine menu at the top of the VirtualBox window, and click Settings
Click the Storage category in the Settings window
Right-click in the storage tree pane, and click Add Floppy Controller
Right-click the Floppy Controller device, and click Add Floppy Device
Click the Choose Disk button in the prompt window that appears
Navigate to the floppy disk image file (.IMG) on your computer and double-click it


If that doesn't work, try renaming the .IMG as .ISO and mount it.

If that too doesn't work, use VBoxManage's convertfromraw command as follows:

VBoxManage convertfromraw --format VDI [filename].img [filename].vdi


Mount the VDI as a hard disk.

**参考链接 / References**:
- N/A

---

#### 295. What&#39;s the difference between &#39;C&#39; and &#39;CE&#39; functions on Windows calculator?

**问题描述 / Problem Description**:
Tags: windows, windows-7, terminology, calculator | Score: 95 | Views: 246950 | Answers: 2

**解决方案 / Solution**:
According to Vintage Technology, both buttons are a way to clear or cancel an entry. The C button will clear all input to the calculator. The CE button clears the most recent entry, so if you make a mistake in a long computation, you don't need to start all over again.

Source
Example

If I now press the CE button, only the 5 is erased. The rest of my computation is still stored.

If I press the C button, my whole computation will be cleared:

History
One might ask why we have these specific keys on our Windows calculator? Why are they not labeled differently?
Luckily, the guys over at Vintage Calculators have an amazing collection of information on the subject.
According to their site, the first electronic calculator was released by Bell Punch Co., Uxbridge, England in 1961. This were the Anita Mk VII and the Anita Mk 8.
Anita Mk VII

Source
Anita Mk 8

Source
For the Mk 8 we get an additional schema:

Source
We can see it has a Clear Register and Clear Keyboard button. Please keep in mind, to my knowledge, this is one of the first electronic calculators that was ever designed.
The terminology was also used in later models, like the Sanyo ICC-0081, which seemed to have a CK (Clear Keyboard) and CA (Clear All) button.

Source
Later models just continue the pattern. For example, the
Canon Pocketronic

Source
We can see a C (Clear) and CI (Cancel Input) button.

**参考链接 / References**:
- N/A

---

#### 296. Why does Windows only show about 3.5 GB of my 4 GB of RAM?

**问题描述 / Problem Description**:
Tags: windows, memory, 32-bit, community-faq | Score: 95 | Views: 38681 | Answers: 9

**解决方案 / Solution**:
You can't:

See Dude, Where's My 4 Gigabytes of RAM?


  if you want to fit memory and devices into a 32-bit address range: not all of the available 4GB of address space can be given over to memory.
  So what actually happens if you go out and buy 4GB of memory for your PC?
  There's a hole in your memory map for the IO. (Now it's only 25% of the total address space, but it's still a big hole.) So the bottom 3GB of your memory will be available, but there's an issue with that last 1GB.


The only practical solution is to install a 64-bit operating system. In Windows Vista and later, 32-bit and 64-bit license keys are interchangeable. If you can get Windows installation media for the 64-bit version of your operating system, you can reinstall using your original license key.

**参考链接 / References**:
- N/A

---

#### 297. How to bring back Photo Viewer in Windows 10?

**问题描述 / Problem Description**:
Tags: windows-10, windows-photo-viewer | Score: 95 | Views: 282189 | Answers: 7

**解决方案 / Solution**:
I think because of your first attempt to run the .dll directly, the entry "Windows Photo Viewer" still points to the .dll instead of rundll32, which of course you can't run directly.

Try adding the following to the registry:

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll]

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell]

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open]
"MuiVerb"="@photoviewer.dll,-3043"

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\command]
@=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\
00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\
6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\
00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\
25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\
00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\
6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\
00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\
5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\
00,31,00,00,00

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\DropTarget]
"Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\print]

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\print\command]
@=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\
00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\
6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\
00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\
25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\
00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\
6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\
00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\
5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\
00,31,00,00,00

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\print\DropTarget]
"Clsid"="{60fd46de-f830-4894-a628-6fa81bc0190d}"


(Source)

If that doesn't work, try searching the registry for Windows Photo Viewer and photoviewer.dll to see if there are any references to photoviewer.dll being called directly (without rundll32).

**参考链接 / References**:
- N/A

---

#### 298. Disable a Windows service from the command line

**问题描述 / Problem Description**:
Tags: windows, services, windows-services | Score: 94 | Views: 415499 | Answers: 4

**解决方案 / Solution**:
sc config "Name of Service" start= disabled
sc stop "Name of Service"


The space after the "start=" is important

You can see service name by double clicking a service on Services screen:

**参考链接 / References**:
- N/A

---

#### 299. Verifying USB connection speed (USB 3 or USB 2?)

**问题描述 / Problem Description**:
Tags: windows, usb-storage, usb-3, usb-2 | Score: 94 | Views: 374020 | Answers: 7

**解决方案 / Solution**:
Another way to check whether you are using a USB 3.0 connection or not is to use USBView.exe from Windows Driver Kit (WDK)
You could also use USB Device Tree Viewer, which is very similar to USBView.exe and you won't have to download the huge WDK to use it.
EDITED: in the screenshot below, H is for high-speed (480 Mbit/s) so USB 2.0. F is for full-speed (12 Mbit/s), which can be USB 1.1 or 2.0.

When you run USB Device Tree Viewer, you'll see a list of USB Host Controllers (there are 3 on my notebook). You could cycle through each port of the USB Root Hubs attached to these controllers to see what's connected to that port. You'll find that each USB device connected to your computer (mouse, WiFi or Bluetooth adapter, webcam, etc.) show up on one of those ports.
Detach all flash drives and external hard disks from your computer and look for a USB controller that has no devices attached to any of its ports (on my computer, it is USB xHCI Compliant Host Controller). Now attach a flash drive or external HDD that you wish to test and you'll notice that it is connected to one of the ports of the USB Root Hub attached to that controller.
If you attached a flash drive, it would show up as:
USB Mass Storage Device - [ASSIGNED_DRIVELETTER]
Click on it and look for the Connection Information section on the information pane to the right.

If the device is connected in USB 3.0 SuperSpeed mode, it will show:
Device Bus Speed         : 0x03 (SuperSpeed)
For USB 2.0, it will show:
Device Bus Speed         : 0x02 (High-Speed)
For USB 1.1, it will show:
Device Bus Speed         : 0x01 (Full-Speed)
Besides this, there are also several other methods that are explained in great detail here

**参考链接 / References**:
- N/A

---

#### 300. How can I remap a keyboard key?

**问题描述 / Problem Description**:
Tags: windows, keyboard, remapping | Score: 94 | Views: 300776 | Answers: 9

**解决方案 / Solution**:
Here is a good article from Howtogeek about using a utility called SharpKeys:

##Map Any Key to Any Key on Windows 10, 8, 7, or Vista
If you are tired of the way certain keys on your system work, such as the Caps Lock key, you can re-map them to function as a different key by using a registry hack. But there should be an easier way, right?
This is where SharpKeys comes into the picture: It’s a small utility that will let you easily map one key to another key easily, or even turn the key off, without having to enter the registry at all.
For instance, I used the key mapping to just turn off my Caps Lock key, since I never use it.

(source: howtogeek.com)


You can click the Add button to bring up the Add New Key Mapping dialog, where you can either select the keys to map from the lists, or just click the Type Key button and press the key manually (which I find much more intuitive)

(source: howtogeek.com)


Once you are done, click the Write to Registry button and you’ll be told to log off or reboot for the changes to take effect.

(source: howtogeek.com)


If you want all the technical details on how the registry keys work, you can read about how to map keys using registry hacks.

Link for reference

**参考链接 / References**:
- N/A

---

#### 301. [V2EX] 各位大佬们，你们 win 系统安装了什么杀毒软件？

**问题描述 / Problem Description**:
是微软自带的还是第三方的？免费的还是付费的？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 302. [V2EX] Windows Update 开始推送无限暂停体验

**问题描述 / Problem Description**:
Windows Update 新体验已经开始逐步推送，Windows 更新的暂停功能现在引入了新的日历体验，用户可以选择具体日期暂停更新，最长可达 35 天，便于围绕旅行、会议、考试或繁忙周期进行规划。如果需要更长的暂停时间，用户可以多次延长暂停截止日期，每次最多 35 天，且无延长次数限制。
具体👉🔗 Windows Update 体验重大改进：更多控制权与更少打扰

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 303. [V2EX] Win 11/10 重装系统、保留数据、初始化

**问题描述 / Problem Description**:
完整版：
GitHub 、B 站 
摘要
常见软件的配置与数据迁移方法
Windows 系统设置
7-Zip 设置
OOBE 设置：装驱动、禁用 BitLocker
重新激活系统
卸载禁用广告组件  
重装前的思考
我被微软偷袭了，不能登录微软帐户，详情见《 微软！我只是想更新 BIOS ，结果被迫重装系统？！ 》  
重装与保留数据的思路
Windows 设置
Windows 官方云同步只支持部分设置，具体看文档：
[] 图：Windows 备份设置目录 （中文是机翻， 英文版 ）
而且由于网络问题，不一定能同步成功。我建议使用截图与文本保存修改过的配置。  
控制面板
在 Win11 系统

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 304. [V2EX] windows 更新这么离谱吗

**问题描述 / Problem Description**:
本来电脑安装的是 win10 专业版。昨晚睡觉之前关机，发现有更新。顺手就点了更新并关机，结果早上一开机变成 win11le ???要不要这么不要脸

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 305. [V2EX] 想用 Windows 系统作为游戏服务器，系统选什么

**问题描述 / Problem Description**:
比较旧的一台零氪 ser5配置: CPU: 5800H内存: 16G DDR4现在是安装了 Debian 13docker 跑 GameServerManager 作为 MC 和幸福工程的服务器现在遇到了有部分游戏服务器仅支持 Windows 系统，想换成 Windows ，根据 CPU ，考虑选择 Windows 10 ，请问我选择 server 或者 ltsc ，还是直接安装专业版。如果选择 server 会不会显卡驱动安装会有问题。有更好的结果 11 也是可以考虑的

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 306. [V2EX] Windows 上面有类似 TimeMachine 的备份软件吗

**问题描述 / Problem Description**:
rt主要诉求是文件历史版本。以前用 mac 的时候，我记得一份文件从创造开始，每次变更保存，time machine 都会有一个单独的备份。看了 windows 上面的备份软件，要么是单纯的备份，有增量备份的，需要定时运行。我记得 time machine 好像是后台一直再运行，保存在本地硬盘里，等跟 time machine 的硬盘链接的时候再转移过去。想请问一下大佬，windows 上面有类似的软件吗？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 307. [V2EX] 微软无预警封禁 VeraCrypt 和 WireGuard 的开发者账号

**问题描述 / Problem Description**:
发不了链接
来自 VC 开发者的已知信息:
①目前找不到人工客服
②如果在 2026 年 06 月无法解封账号,再叠加微软要更新驱动签名 CA 这一因素,则 VERACRYPT“事实上被判了死刑”
不懂 WIN 开发,居然被巨硬卡脖子这么严重吗?

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 308. [V2EX] Win11 23H2 无线网卡（AX211）有 DNS 残留，经常需要手工干预的问题...

**问题描述 / Problem Description**:
已问过 4 ，5 个模型，无非也就是这两三种说法，“DNS 幽灵”（解释这个是微软屎前 BUG ，需要手工干预）,“intel 网卡驱动有问题，你要接受事实”，“给你一个脚本，每次运行”，就这么这些了；   
OK,现象是这样的：   （以下也就是我向 AI 问出的问题)
Windows 11 的无线网卡所连接到无线 SSID 网络里，DNS 使用有这样情况：  
虽然我任何 SSID 都不会去手工设定 DNS ，以往全部，包括现有记忆的 SSID ，设置是通过 DHCP 获取 DNS 并使用它，但是，laptop 冷开机后进入系统，AX211 网卡自动连接到 SSID 内，此 SSID 内使

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 309. [V2EX] Windows 桌面版 EULA 里面有一条很有意思

**问题描述 / Problem Description**:
...您不得:
将软件用作服务器软件，用于商业托管服务，通过网络提供该软件以供多个用户同时使用，将软件安装在服务器上并允许用户远程访问，或将软件安装在设备上仅供远程用户使用。

「将软件安装在设备上仅供远程用户使用」也就是说，Windows 桌面版作无头系统就违反 EULA 了，甚至插着键盘鼠标显示器但是不用，只通过远程桌面使用，也违反 EULA 。
「将软件用作服务器软件」这个边界在哪里，是不是局域网建房开把 CS1.6/Minecraft 也违反 EULA 了？在互联网上呢？我的游戏忘记关了，别人一直可以连进我的游戏房间呢？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 310. [V2EX] 发现 WinServer(2025)才是最轻量的 Win，胜过 LTSC，很适合虚拟机

**问题描述 / Problem Description**:
预装的组件比 LTSC 还少，默认甚至连 Windows Search 都没装（不会在后台索引占资源）。想要什么组件自己再装，最重要的是能一键卸载 Windows Defender
Uninstall-WindowsFeature Windows-Defender

（桌面版 Win 没有办法关 Defender ，至少没有官方正统的办法，只有 https://github.com/ionuttbara/windows-defender-remover 这种脚本直接干文件干注册表暴力拆。）
关 Windows 防火墙也不会像桌面版 Win 那样，老在右下角弹防火墙已关闭警告。
试了在虚拟机里面

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://github.com/ionuttbara/windows-defender-remover

---

#### 311. [V2EX] 资源占用最低的 windows 杀毒软件是？

**问题描述 / Problem Description**:
有一个老软件需要在 windows 上跑
手上有一台小鸡 但内存只有 2 个 G  
所以想把 windows defender 替换成更轻量的杀毒软件 多腾点资源出来
有人折腾过吗?

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 312. [V2EX] win11 经常系统信息的储存 显示 0GB

**问题描述 / Problem Description**:
系统是 25H2(26200.8039),开机有时候风扇呼呼转，cpu 很高，有时候 100%，平常用很卡

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 313. [V2EX] bitwarden 的数据在 Windows 内存中是明文吗？

**问题描述 / Problem Description**:
bitwarden Windows 桌面版本的数据在内存中是不是明文？其他程序能直接获取到各种密码吗？  那主密码会直接明文保存在内存吗？  如果关闭 uac 和各种安全软件防护，并且直接使用内置管理员账户 Administrator 进行登录，这样是不是任何程序都能直接读取 bitwarden 的内存并获取到各种明文密码？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 314. [V2EX] windows 11 现在问题还多吗

**问题描述 / Problem Description**:
前段时间遇到的是，win11 下，突然没有声音，后来又是 win11 chrome 下，mp4 视频卡顿，变声的问题。想问下各位，最近修复了没

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 315. [V2EX] Windows 文件路径长度限制是多少个字符？ 244、255、256、260？「启用长路径」有用吗？

**问题描述 / Problem Description**:
到底是多少个字符？
256
微软文档《 最大路径长度限制 》（ Maximum Path Length Limitation ）：
在 Windows API 中，路径的最大长度为 MAX_PATH ，为 260 个字符。
系统按以下顺序构建本地路径：驱动器号、冒号、反斜杠、用反斜杠分隔的路径和终止 null 字符。
例如，驱动器 D 上的最大路径为：
D:\某个 256 个字符的路径字符串&lt;NUL&gt;
其中 &lt;NUL&gt; 表示当前系统代码页的不可见终止 null 字符。（&lt;&gt; 字符在此用于醒目用途，不能作为有效路径字符串的一部分。）  
文档到这里的意思是：路

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---

#### 316. [V2EX] 各位大佬们，你们 win 系统安装了什么杀毒软件？

**问题描述 / Problem Description**:
是微软自带的还是第三方的？免费的还是付费的？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- N/A

---
