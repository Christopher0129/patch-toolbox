# Linux 常见故障及解决方法 | Linux Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 04:27:55 UTC_

## 中文 🇨🇳
**Linux 常见故障及解决方法**

本页面每小时自动从 Stack Exchange 社区抓取 LINUX 平台常见故障及解决方法。

### LINUX 常见故障及解决方法

#### 1. How do I make `ls` show file sizes in megabytes?

**故障现象**: How do I make `ls` show file sizes in megabytes?
**标签 / 来源**: Tags: linux, ls | unix | 👍 936 | 💬 2 answers

**问题描述**:
Tags: linux, ls | Score: 936 | Views: 2451284 | Answers: 2

**解决方法 / 社区答案**:
ls -l --block-size=M will give you a long format listing (needed to actually see the file size) and round file sizes up to the nearest MiB.

If you want MB (10^6 bytes) rather than MiB (2^20 bytes) units, use --block-size=MB instead.

If you don't want the M suffix attached to the file size, you can use something like --block-size=1M. Thanks Stéphane Chazelas for suggesting this.

If you simply want file sizes in "reasonable" units, rather than specifically megabytes, then you can use -lh to get a long format listing and human readable file size presentation. This will use units of file size to keep file sizes presented with about 1-3 digits (so you'll see file sizes like 6.1K, 151K, 7.1M, 15M, 1.5G and so on.

The --block-size parameter is described in the man page for ls; man ls and search for SIZE. It allows for units other than MB/MiB as well, and from the looks of it (I didn't try that) arbitrary block sizes as well (so you could see the file size as a number of 429-byte blocks if you want to).

Note that both --block-size and -h are GNU extensions on top of the Open Group's ls, so this may not work if you don't have a GNU userland (which most Linux installations do). The ls from GNU Coreutils 8.5 does support --block-size and -h as described above. Thanks to kojiro for pointing this out.

**参考链接**: https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

> 📎 来源 / Source: https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

#### 2. Finding the PID of the process using a specific port?

**故障现象**: Finding the PID of the process using a specific port?
**标签 / 来源**: Tags: linux, process, ip, netstat | unix | 👍 831 | 💬 8 answers

**问题描述**:
Tags: linux, process, ip, netstat | Score: 831 | Views: 2194654 | Answers: 8

**解决方法 / 社区答案**:
Your existing command doesn't work because Linux requires you to either be root or the owner of the process to get the information you desire.
On modern systems, ss is the appropriate tool to use to get this information:
$ sudo ss -lptn 'sport = :80'
State   Local Address:Port  Peer Address:Port              
LISTEN  127.0.0.1:80        *:*                users:((&quot;nginx&quot;,pid=125004,fd=12))
LISTEN  ::1:80              :::*               users:((&quot;nginx&quot;,pid=125004,fd=11))

You can also use the same invocation you're currently using, but you must first elevate with sudo:
$ sudo netstat -nlp | grep :80
tcp  0  0  0.0.0.0:80  0.0.0.0:*  LISTEN  125004/nginx

You can also use lsof:
$ sudo lsof -n -i :80 | grep LISTEN
nginx   125004 nginx    3u  IPv4   6645      0t0  TCP 0.0.0.0:80 (LISTEN)

**参考链接**: https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port

> 📎 来源 / Source: https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port

#### 3. Why am I still getting a password prompt with ssh with public key authentication?

**故障现象**: Why am I still getting a password prompt with ssh with public key authentication?
**标签 / 来源**: Tags: ubuntu, centos, ssh, sshd, key-authentication | unix | 👍 745 | 💬 32 answers

**问题描述**:
Tags: ubuntu, centos, ssh, sshd, key-authentication | Score: 745 | Views: 1428794 | Answers: 32

**解决方法 / 社区答案**:
Make sure the permissions on the ~/.ssh directory and its contents are proper. When I first set up my ssh key auth, I didn't have the ~/.ssh folder properly set up, and it yelled at me.


Your home directory ~, your ~/.ssh directory and the ~/.ssh/authorized_keys file on the remote machine must be writable only by you: rwx------ and rwxr-xr-x are fine, but rwxrwx--- is no good¹, even if you are the only user in your group (if you prefer numeric modes: 700 or 755, not 775).
If ~/.ssh or authorized_keys is a symbolic link, the canonical path (with symbolic links expanded) is checked.
Your ~/.ssh/authorized_keys file (on the remote machine) must be readable (at least 400), but you'll need it to be also writable (600) if you will add any more keys to it.
Your private key file (on the local machine) must be readable and writable only by you: rw-------, i.e. 600.
Also, if SELinux is set to enforcing, you may need to run restorecon -R -v ~/.ssh (see e.g. Ubuntu bug 965663 and Debian bug report #658675; this is patched in CentOS 6).


¹  Except on some distributions (Debian and derivatives) which have patched the code to allow group writability if you are the only user in your group.

**参考链接**: https://unix.stackexchange.com/questions/36540/why-am-i-still-getting-a-password-prompt-with-ssh-with-public-key-authentication

> 📎 来源 / Source: https://unix.stackexchange.com/questions/36540/why-am-i-still-getting-a-password-prompt-with-ssh-with-public-key-authentication

#### 4. How can I resolve a hostname to an IP address in a Bash script?

**故障现象**: How can I resolve a hostname to an IP address in a Bash script?
**标签 / 来源**: Tags: linux, bash, networking, dns | unix | 👍 635 | 💬 29 answers

**问题描述**:
Tags: linux, bash, networking, dns | Score: 635 | Views: 995011 | Answers: 29

**解决方法 / 社区答案**:
You can use getent, which comes with glibc (so you almost certainly have it on Linux). This resolves using gethostbyaddr/gethostbyname2, and so also will check /etc/hosts/NIS/etc:

getent hosts unix.stackexchange.com | awk '{ print $1 }'


Or, as Heinzi said below, you can use dig with the +short argument (queries DNS servers directly, does not look at /etc/hosts/NSS/etc) :

dig +short unix.stackexchange.com


If dig +short is unavailable, any one of the following should work. All of these query DNS directly and ignore other means of resolution:

host unix.stackexchange.com | awk '/has address/ { print $4 }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 }'


If you want to only print one IP, then add the exit command to awk's workflow.

dig +short unix.stackexchange.com | awk '{ print ; exit }'
getent hosts unix.stackexchange.com | awk '{ print $1 ; exit }'
host unix.stackexchange.com | awk '/has address/ { print $4 ; exit }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 ; exit }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 ; exit }'

**参考链接**: https://unix.stackexchange.com/questions/20784/how-can-i-resolve-a-hostname-to-an-ip-address-in-a-bash-script

> 📎 来源 / Source: https://unix.stackexchange.com/questions/20784/how-can-i-resolve-a-hostname-to-an-ip-address-in-a-bash-script

#### 5. Execute vs Read bit. How do directory permissions in Linux work?

**故障现象**: Execute vs Read bit. How do directory permissions in Linux work?
**标签 / 来源**: Tags: linux, permissions, directory | unix | 👍 536 | 💬 9 answers

**问题描述**:
Tags: linux, permissions, directory | Score: 536 | Views: 403915 | Answers: 9

**解决方法 / 社区答案**:
When applying permissions to directories on Linux, the permission bits have different meanings than on regular files.


The read bit (r) allows the affected user to list the files within the directory
The write bit (w) allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes
The execute bit (x) allows the affected user to enter the directory, and access files and directories inside
The sticky bit (T, or t if the execute bit is set for others) states that files and directories within that directory may only be deleted or renamed by their owner (or root)

**参考链接**: https://unix.stackexchange.com/questions/21251/execute-vs-read-bit-how-do-directory-permissions-in-linux-work

> 📎 来源 / Source: https://unix.stackexchange.com/questions/21251/execute-vs-read-bit-how-do-directory-permissions-in-linux-work

#### 6. How to know whether Wayland or X11 is being used

**故障现象**: How to know whether Wayland or X11 is being used
**标签 / 来源**: Tags: linux, x11, wayland | unix | 👍 514 | 💬 15 answers

**问题描述**:
Tags: linux, x11, wayland | Score: 514 | Views: 702757 | Answers: 15

**解决方法 / 社区答案**:
Obtain the session ID to pass in by issuing:
loginctl

That will show you something like:
SESSION  UID USER          SEAT  TTY
     c2 1000 yourusername  seat0    

1 sessions listed.

In that example, c2 is the session ID.
Then:
loginctl show-session &lt;SESSION_ID&gt; -p Type

If you want all this on a single command:
loginctl show-session $(awk '/tty/ {print $1}' &lt;(loginctl)) -p Type | awk -F= '{print $2}'

Use the one corresponding to your user name.
Refer to:
https://fedoraproject.org/wiki/How_to_debug_Wayland_problems
So, for me, I can see Wayland is in use:
$ loginctl show-session c2 -p Type                                                  
Type=wayland

**参考链接**: https://unix.stackexchange.com/questions/202891/how-to-know-whether-wayland-or-x11-is-being-used

> 📎 来源 / Source: https://unix.stackexchange.com/questions/202891/how-to-know-whether-wayland-or-x11-is-being-used

#### 7. Compress a folder with tar?

**故障现象**: Compress a folder with tar?
**标签 / 来源**: Tags: linux, backup, tar | unix | 👍 505 | 💬 2 answers

**问题描述**:
Tags: linux, backup, tar | Score: 505 | Views: 1359515 | Answers: 2

**解决方法 / 社区答案**:
To tar and gzip a folder, the syntax is:
tar czf name_of_archive_file.tar.gz name_of_directory_to_tar

Adding - before the options (czf) is optional with tar. The effect of czf is as follows:

c — create an archive file (as opposed to extract, which is x)
f — filename of the archive file
z — filter archive through gzip (remove this option to create a .tar file)

If you want to tar the current directory, use . to designate that.
To construct filenames dynamically, use the date utility (look at its man page for the available format options). For example:
cd /var/www &amp;&amp;
tar czf ~/www_backups/$(date +%Y%m%d-%H%M%S).tar.gz .

This will create a file named something like 20120902-185558.tar.gz.
On Linux, chances are your tar also supports BZip2 compression with the j rather than z option. And possibly others. Check the man page on your local system.

**参考链接**: https://unix.stackexchange.com/questions/46969/compress-a-folder-with-tar

> 📎 来源 / Source: https://unix.stackexchange.com/questions/46969/compress-a-folder-with-tar

#### 8. When should I not kill -9 a process?

**故障现象**: When should I not kill -9 a process?
**标签 / 来源**: Tags: linux, command-line, kill, process-management | unix | 👍 436 | 💬 9 answers

**问题描述**:
Tags: linux, command-line, kill, process-management | Score: 436 | Views: 209582 | Answers: 9

**解决方法 / 社区答案**:
Generally, you should use kill (short for kill -s TERM, or on most systems kill -15) before kill -9 (kill -s KILL) to give the target process a chance to clean up after itself.  (Processes can't catch or ignore SIGKILL, but they can and often do catch SIGTERM.)  If you don't give the process a chance to finish what it's doing and clean up, it may leave corrupted files (or other state) around that it won't be able to understand once restarted.

strace/truss, ltrace and gdb are generally good ideas for looking at why a stuck process is stuck.   (truss -u on Solaris is particularly helpful; I find ltrace too often presents arguments to library calls in an unusable format.)  Solaris also has useful /proc-based tools, some of which have been ported to Linux.  (pstack is often helpful).

**参考链接**: https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process

> 📎 来源 / Source: https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process

#### 9. How do you empty the buffers and cache on a Linux system?

**故障现象**: How do you empty the buffers and cache on a Linux system?
**标签 / 来源**: Tags: linux, kernel, performance, cache, ram | unix | 👍 419 | 💬 1 answers

**问题描述**:
Tags: linux, kernel, performance, cache, ram | Score: 419 | Views: 985960 | Answers: 1

**解决方法 / 社区答案**:
Emptying the buffers cache
If you ever want to empty it you can use this chain of commands.
# free &amp;&amp; sync &amp;&amp; echo 3 &gt; /proc/sys/vm/drop_caches &amp;&amp; free

             total       used       free     shared    buffers     cached
Mem:       1018916     980832      38084          0      46924     355764
-/+ buffers/cache:     578144     440772
Swap:      2064376        128    2064248
             total       used       free     shared    buffers     cached
Mem:       1018916     685008     333908          0        224     108252
-/+ buffers/cache:     576532     442384
Swap:      2064376        128    2064248

You can signal the Linux Kernel to drop various aspects of cached items by changing the numeric argument to the above command.

To free pagecache:
# echo 1 &gt; /proc/sys/vm/drop_caches


To free dentries and inodes:
# echo 2 &gt; /proc/sys/vm/drop_caches


To free pagecache, dentries and inodes:
# echo 3 &gt; /proc/sys/vm/drop_caches



The above are meant to be run as root. If you're trying to do them using sudo then you'll need to change the syntax slightly to something like these:
$ sudo sh -c 'echo 1 &gt;/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 2 &gt;/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 3 &gt;/proc/sys/vm/drop_caches'

NOTE: There's a more esoteric version of the above command if you're into that:
$ echo &quot;echo 1 &gt; /proc/sys/vm/drop_caches&quot; | sudo sh

Why the change in syntax? The /bin/echo program is running as root, because of sudo, but the shell that's redirecting echo's output to the root-only file is still running as you. Your current shell does the redirection before sudo starts.
Seeing what's in the buffers and cache
Take a look at linux-ftools if you'd like to analyze the contents of the buffers &amp; cache. Specifically if you'd like to see what files are currently being cached.
fincore
With this tool you can see what files are being cached within a give directory.
fincore [options] files...

  --pages=false      Do not print pages
  --summarize        When comparing multiple files, print a summary report
  --only-cached      Only print stats for files that are actually in cache.

For example, /var/lib/mysql/blogindex:
root@xxxxxx:/var/lib/mysql/blogindex# fincore --pages=false --summarize --only-cached * 
stats for CLUSTER_LOG_2010_05_21.MYI: file size=93840384 , total pages=22910 , cached pages=1 , cached size=4096, cached perc=0.004365 
stats for CLUSTER_LOG_2010_05_22.MYI: file size=417792 , total pages=102 , cached pages=1 , cached size=4096, cached perc=0.980392 
stats for CLUSTER_LOG_2010_05_23.MYI: file size=826368 , total pages=201 , cached pages=1 , cached size=4096, cached perc=0.497512 
stats for CLUSTER_LOG_2010_05_24.MYI: file size=192512 , total pages=47 , cached pages=1 , cached size=4096, cached perc=2.127660 
stats for CLUSTER_LOG_2010_06_03.MYI: file size=345088 , total pages=84 , cached pages=43 , cached size=176128, cached perc=51.190476 
stats for CLUSTER_LOG_2010_06_04.MYD: file size=1478552 , total pages=360 , cached pages=97 , cached size=397312, cached perc=26.944444 
stats for CLUSTER_LOG_2010_06_04.MYI: file size=205824 , total pages=50 , cached pages=29 , cached size=118784, cached perc=58.000000 
stats for COMMENT_CONTENT_2010_06_03.MYI: file size=100051968 , total pages=24426 , cached pages=10253 , cached size=41996288, cached perc=41.975764 
stats for COMMENT_CONTENT_2010_06_04.MYD: file size=716369644 , total pages=174894 , cached pages=79821 , cached size=326946816, cached perc=45.639645 
stats for COMMENT_CONTENT_2010_06_04.MYI: file size=56832000 , total pages=13875 , cached pages=5365 , cached size=21975040, cached perc=38.666667 
stats for FEED_CONTENT_2010_06_03.MYI: file size=1001518080 , total pages=244511 , cached pages=98975 , cached size=405401600, cached perc=40.478751 
stats for FEED_CONTENT_2010_06_04.MYD: file size=9206385684 , total pages=2247652 , cached pages=1018661 , cached size=4172435456, cached perc=45.321117 
stats for FEED_CONTENT_2010_06_04.MYI: file size=638005248 , total pages=155763 , cached pages=52912 , cached size=216727552, cached perc=33.969556 
stats for FEED_CONTENT_2010_06_04.frm: file size=9840 , total pages=2 , cached pages=3 , cached size=12288, cached perc=150.000000 
stats for PERMALINK_CONTENT_2010_06_03.MYI: file size=1035290624 , total pages=252756 , cached pages=108563 , cached size=444674048, cached perc=42.951700 
stats for PERMALINK_CONTENT_2010_06_04.MYD: file size=55619712720 , total pages=13579031 , cached pages=6590322 , cached size=26993958912, cached perc=48.533080 
stats for PERMALINK_CONTENT_2010_06_04.MYI: file size=659397632 , total pages=160985 , cached pages=54304 , cached size=222429184, cached perc=33.732335 
stats for PERMALINK_CONTENT_2010_06_04.frm: file size=10156 , total pages=2 , cached pages=3 , cached size=12288, cached perc=150.000000 
---
total cached size: 32847278080

With the above output you can see that there are several *.MYD, *.MYI, and *.frm files that are currently being cached.
Swap
If you want to clear out your swap you can use the following commands.
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7298164     689328          0      30416     457936
-/+ buffers/cache:    6809812    1177680
Swap:      5963772     609452    5354320

Then use this command to disable swap:
$ swapoff -a

You can confirm that it's now empty:
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7777912     209580          0      39332     489864
-/+ buffers/cache:    7248716     738776
Swap:            0          0          0

And to re-enable it:
$ swapon -a

And now reconfirm with free:
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7785572     201920          0      41556     491508
-/+ buffers/cache:    7252508     734984
Swap:      5963772          0    5963772

**参考链接**: https://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system

> 📎 来源 / Source: https://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system

#### 10. How to check OS and version using a Linux command

**故障现象**: How to check OS and version using a Linux command
**标签 / 来源**: Tags: linux, shell | unix | 👍 400 | 💬 3 answers

**问题描述**:
Tags: linux, shell | Score: 400 | Views: 1968359 | Answers: 3

**解决方法 / 社区答案**:
Kernel Version

If you want kernel version information, use uname(1). For example:

$ uname -a
Linux localhost 3.11.0-3-generic #8-Ubuntu SMP Fri Aug 23 16:49:15 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux


Distribution Information

If you want distribution information, it will vary depending on your distribution and whether your system supports the Linux Standard Base. Some ways to check, and some example output, are immediately below.

$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu Saucy Salamander (development branch)
Release:    13.10
Codename:   saucy

$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=13.10
DISTRIB_CODENAME=saucy
DISTRIB_DESCRIPTION="Ubuntu Saucy Salamander (development branch)"

$ cat /etc/issue.net
Ubuntu Saucy Salamander (development branch)

$ cat /etc/debian_version 
wheezy/sid

**参考链接**: https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command

> 📎 来源 / Source: https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command

#### 11. How to list all files ordered by size

**故障现象**: How to list all files ordered by size
**标签 / 来源**: Tags: linux, files, ls | unix | 👍 386 | 💬 14 answers

**问题描述**:
Tags: linux, files, ls | Score: 386 | Views: 734387 | Answers: 14

**解决方法 / 社区答案**:
Simply use something like:

ls -lS /path/to/folder/


Capital S. 

This will sort files by size. 

Also see:

man ls

-S     sort by file size


If you want to sort in reverse order, just add -r switch.

Update:

To exclude directories (and provided none of the file names or symlink targets contain newline characters):

ls -lS | grep -v '^d' 


Update 2:

I see now how it still shows symbolic links, which could be folders. Symbolic links always start with a letter l, as in link.  

Change the command to filter for a -. This should only leave regular files:

ls -lS | grep '^-'


On my system this only shows regular files. 

update 3:

To add recursion, I would leave the sorting of the lines to the sort command and tell it to use the 5th column to sort on. 

ls -lR | grep '^-' | sort -k 5 -rn


-rn means Reverse and numeric to get the biggest files at the top. Down side of this command is that it does not show the full path of the files.

If you do need the full path of the files, use something like this:

find . -type f  -exec du -h {} + | sort -r -h


The find command will recursively find all files in all sub directories of . and call du -h (meaning disk usage -humanreadable) and then sort the output again. If your find/sort doesn't support -h, replace with du -k and sort -rn. Note that size and disk usage are not the same thing.

**参考链接**: https://unix.stackexchange.com/questions/53737/how-to-list-all-files-ordered-by-size

> 📎 来源 / Source: https://unix.stackexchange.com/questions/53737/how-to-list-all-files-ordered-by-size

#### 12. How to know number of cores of a system in Linux?

**故障现象**: How to know number of cores of a system in Linux?
**标签 / 来源**: Tags: linux, cpu | unix | 👍 384 | 💬 12 answers

**问题描述**:
Tags: linux, cpu | Score: 384 | Views: 815327 | Answers: 12

**解决方法 / 社区答案**:
To get a complete picture you need to look at the number of threads per core, cores per socket and sockets. If you multiply these numbers you will get the number of CPUs on your system.


  CPUs = Threads per core X cores per socket X sockets


CPUs are what you see when you run htop (these do not equate to physical CPUs).

Here is an example from a desktop machine:

$ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
CPU(s):                8
Thread(s) per core:    2
Core(s) per socket:    4
Socket(s):             1


And a server:

$ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
CPU(s):                32
Thread(s) per core:    2
Core(s) per socket:    8
Socket(s):             2


The output of nproc corresponds to the CPU count from lscpu. For the desktop machine above this should match the 8 CPU(s) reported by lscpu:

$ nproc --all
8


The output of /proc/cpuinfo should match this information, for example on the desktop system above we can see there are 8 processors (CPUs) and 4 cores (core id 0-3):

$ grep -E 'processor|core id' /proc/cpuinfo
processor   : 0
core id     : 0
processor   : 1
core id     : 0
processor   : 2
core id     : 1
processor   : 3
core id     : 1
processor   : 4
core id     : 2
processor   : 5
core id     : 2
processor   : 6
core id     : 3
processor   : 7
core id     : 3


The cpu cores reported by /proc/cpuinfo corresponds to the Core(s) per socket reported by lscpu. For the desktop machine above this should match the 4 Core(s) per socket reported by lscpu:

$ grep -m 1 'cpu cores' /proc/cpuinfo
cpu cores   : 4


To specifically answer your question you tell how many cores you have by multiplying the number of cores you have per socket by the number of sockets you have.


  Cores = Cores per socket X Sockets


For the example systems above the desktop has 4 cores:

$ echo "Cores = $(( $(lscpu | awk '/^Socket\(s\)/{ print $2 }') * $(lscpu | awk '/^Core\(s\) per socket/{ print $4 }') ))"
Cores = 4


While the server has 16:

$ echo "Cores = $(( $(lscpu | awk '/^Socket\(s\)/{ print $2 }') * $(lscpu | awk '/^Core\(s\) per socket/{ print $4 }') ))"
Cores = 16


Another useful utility is dmidecode which outputs per socket information. In the case of the server system listed above we expect to see 8 cores per socket and 16 threads per socket:

$ sudo dmidecode -t 4 | grep -E 'Socket Designation|Count'
    Socket Designation: CPU1
    Core Count: 8
    Thread Count: 16
    Socket Designation: CPU2
    Core Count: 8
    Thread Count: 16


The lscpu command has a number of useful options that you may like to check out, for example:

$ lscpu --all --extended
$ lscpu --all --parse=CPU,SOCKET,CORE | grep -v '^#'


See man lscpu for details.

In summary:


You need to be aware of sockets, cores and threads
You need to be careful of the term CPU as it means different things in different contexts

**参考链接**: https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux

#### 13. How to set default file permissions for all folders/files in a directory?

**故障现象**: How to set default file permissions for all folders/files in a directory?
**标签 / 来源**: Tags: linux, permissions, directory | unix | 👍 379 | 💬 5 answers

**问题描述**:
Tags: linux, permissions, directory | Score: 379 | Views: 714957 | Answers: 5

**解决方法 / 社区答案**:
I found it: Applying default permissions
From the article:

Set the setgid bit, so that files/folder under &lt;directory&gt; will be created with the same group as &lt;directory&gt;
chmod g+s &lt;directory&gt;


Set the default ACLs for the group and other
setfacl -d -m g::rwx /&lt;directory&gt;
setfacl -d -m o::rx /&lt;directory&gt;



Next we can verify:
getfacl /&lt;directory&gt;

Output:
# file: ../&lt;directory&gt;/
# owner: &lt;user&gt;
# group: media
# flags: -s-
user::rwx
group::rwx
other::r-x
default:user::rwx
default:group::rwx
default:other::r-x

**参考链接**: https://unix.stackexchange.com/questions/1314/how-to-set-default-file-permissions-for-all-folders-files-in-a-directory

> 📎 来源 / Source: https://unix.stackexchange.com/questions/1314/how-to-set-default-file-permissions-for-all-folders-files-in-a-directory

#### 14. How can I monitor disk io?

**故障现象**: How can I monitor disk io?
**标签 / 来源**: Tags: linux, disk | unix | 👍 378 | 💬 11 answers

**问题描述**:
Tags: linux, disk | Score: 378 | Views: 1059519 | Answers: 11

**解决方法 / 社区答案**:
For disk I/O trending there are a few options. My personal favorite is the sar command from sysstat. By default, it gives output like this:

09:25:01 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
09:35:01 AM     all      0.11      0.00      0.01      0.00      0.00     99.88
09:45:01 AM     all      0.12      0.00      0.01      0.00      0.00     99.86
09:55:01 AM     all      0.09      0.00      0.01      0.00      0.00     99.90
10:05:01 AM     all      0.10      0.00      0.01      0.02      0.01     99.86
Average:        all      0.19      0.00      0.02      0.00      0.01     99.78


The %iowait is the time spent waiting on I/O. Using the Debian package, you must enable the stat collector via the /etc/default/sysstat config file after package installation.

To see current utilization broken out by device, you can use the iostat command, also from the sysstat package:

$ iostat -x 1
Linux 3.5.2-x86_64-linode26 (linode)    11/08/2012      _x86_64_        (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.84    0.00    0.08    1.22    0.07   97.80

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
xvda              0.09     1.02    2.58    0.49   112.79    12.11    40.74     0.15   48.56   3.88   1.19
xvdb              1.39     0.43    4.03    1.82    43.33    18.43    10.56     0.66  112.73   1.93   1.13


Some other options that can show disk usage in trending graphs is munin and cacti.

**参考链接**: https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io

> 📎 来源 / Source: https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io

#### 15. Change the Python3 default version in Ubuntu

**故障现象**: Change the Python3 default version in Ubuntu
**标签 / 来源**: Tags: ubuntu, python, python3 | unix | 👍 378 | 💬 10 answers

**问题描述**:
Tags: ubuntu, python, python3 | Score: 378 | Views: 1239818 | Answers: 10

**解决方法 / 社区答案**:
From the comment: 

sudo update-alternatives --config python


Will show you an error:

update-alternatives: error: no alternatives for python3 


You need to update your update-alternatives , then you will be able to set your default python version.

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2


Then run :

sudo update-alternatives --config python


Set python3.6 as default. 

Or use the following command to set python3.6 as default:

sudo update-alternatives  --set python /usr/bin/python3.6

**参考链接**: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

> 📎 来源 / Source: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

#### 16. How can I update to a newer version of Git using apt-get?

**故障现象**: How can I update to a newer version of Git using apt-get?
**标签 / 来源**: Tags: ubuntu, apt, upgrade, git | unix | 👍 360 | 💬 5 answers

**问题描述**:
Tags: ubuntu, apt, upgrade, git | Score: 360 | Views: 464951 | Answers: 5

**解决方法 / 社区答案**:
Here are the commands you need to run, if you just want to get it done:
sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com A1715D88E1DF1F24 40976EAF437D05B5 3B4FE6ACC0B21F32 A6616109451BBBF2
sudo apt-get update
sudo apt-get install git -y
git --version

As of Dec 2018, I got git 2.20.1 that way, while the version in the Ubuntu Xenial repositories was 2.7.4.
If your system doesn't have add-apt-repository, you can install it via:
sudo apt-get install python-software-properties software-properties-common

**参考链接**: https://unix.stackexchange.com/questions/33617/how-can-i-update-to-a-newer-version-of-git-using-apt-get

> 📎 来源 / Source: https://unix.stackexchange.com/questions/33617/how-can-i-update-to-a-newer-version-of-git-using-apt-get

#### 17. How can I get my external IP address in a shell script?

**故障现象**: How can I get my external IP address in a shell script?
**标签 / 来源**: Tags: linux, shell-script, ip | unix | 👍 355 | 💬 27 answers

**问题描述**:
Tags: linux, shell-script, ip | Score: 355 | Views: 497757 | Answers: 27

**解决方法 / 社区答案**:
I'd recommend getting it directly from a DNS server.
Most of the other answers below all involve going over HTTP to a remote server. Some of them required parsing of the output, or relied on the User-Agent header to make the server respond in plain text. Those change quite frequently (go down, change their name, put up ads, might change output format etc.).

The DNS response protocol is standardised (the format will stay compatible).
Historically, DNS services (Akamai, Google Public DNS, OpenDNS, ..) tend to survive much longer and are more stable, more scalable, and generally more looked-after than whatever new hip whatismyip dot-com HTTP service is hot today.
This method is inherently faster (be it only by a few milliseconds!).

Using dig with an OpenDNS resolver:
$ dig @resolver4.opendns.com myip.opendns.com +short

Perhaps alias it in your bashrc so it's easy to remember
# https://unix.stackexchange.com/a/81699/37512
alias wanip='dig @resolver4.opendns.com myip.opendns.com +short' 
alias wanip4='dig @resolver4.opendns.com myip.opendns.com +short -4'
alias wanip6='dig @resolver1.ipv6-sandbox.opendns.com AAAA myip.opendns.com +short -6'

Responds with a plain ip address:
$ wanip # wanip4, or wanip6
80.100.192.168 # or, 2606:4700:4700::1111

How it works
The dig command.
(Abbreviated from https://ss64.com/bash/dig.html. You can read this anytime via man dig):
usage:  dig [@global-dnsserver] [q-type] &lt;hostname&gt; &lt;d-opt&gt; [q-opt]

    q-type   one of (A, ANY, AAAA, TXT, MX, ...). Default: A.

    d-opt    ...
             +[no]short          (Display nothing except short form of answer)
             ...

    q-opt    one of:
             -4                  (use IPv4 query transport only)
             -6                  (use IPv6 query transport only)
             ...

The ANY query type returns either an AAAA or an A record. To prefer IPv4 or IPv6 connection specifically, use the -4 or -6 options accordingly.
To require the response be an IPv4 address, replace ANY with A; for IPv6, replace it with AAAA. Note that it can only return the address used for the connection. For example, when connecting over IPv6, it cannot return the A address.
Alternative servers
Various DNS providers offer this service, including OpenDNS, Akamai, and Google Public DNS:
# OpenDNS (since 2009)
$ dig @resolver3.opendns.com myip.opendns.com +short
$ dig @resolver4.opendns.com myip.opendns.com +short
80.100.192.168

# OpenDNS IPv6
$ dig @resolver1.ipv6-sandbox.opendns.com AAAA myip.opendns.com +short -6
2606:4700:4700::1111

# Akamai (since 2009)
$ dig @ns1-1.akamaitech.net ANY whoami.akamai.net +short
80.100.192.168

# Akamai approximate
# NOTE: This returns only an approximate IP from your block,
# but has the benefit of working even when behind private DNS proxies.
$ dig +short TXT whoami.ds.akahelp.net
&quot;ip&quot; &quot;80.100.192.160&quot;

# Google (since 2010)
# Supports IPv6 + IPv4, use -4 or -6 to force one.
$ dig @ns1.google.com TXT o-o.myaddr.l.google.com +short
&quot;80.100.192.168&quot;

Example alias that specifically requests an IPv4 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip4='dig @resolver4.opendns.com myip.opendns.com +short -4'

$ wanip4
80.100.192.168

And for your IPv6 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip6='dig @ns1.google.com TXT o-o.myaddr.l.google.com +short -6'

$ wanip6
&quot;2606:4700:4700::1111&quot;

Troubleshooting
If the command is not working for some reason, there may be a network problem. Try one of the alternatives above first.
If you suspect a different issue (with the upstream provider, the command-line tool, or something else) then run the command without the +short option to reveal the details of the DNS query. For example:
$ dig @resolver4.opendns.com myip.opendns.com

;; Got answer: -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR

;; QUESTION SECTION:
;myip.opendns.com.      IN  A

;; ANSWER SECTION:
myip.opendns.com.   0   IN  A   80.100.192.168

;; Query time: 4 msec

**参考链接**: https://unix.stackexchange.com/questions/22615/how-can-i-get-my-external-ip-address-in-a-shell-script

> 📎 来源 / Source: https://unix.stackexchange.com/questions/22615/how-can-i-get-my-external-ip-address-in-a-shell-script

#### 18. how can I recursively delete empty directories in my home directory?

**故障现象**: how can I recursively delete empty directories in my home directory?
**标签 / 来源**: Tags: linux, filesystems, find, rm | unix | 👍 318 | 💬 2 answers

**问题描述**:
Tags: linux, filesystems, find, rm | Score: 318 | Views: 291415 | Answers: 2

**解决方法 / 社区答案**:
The find command is the primary tool for recursive file system operations.
Use the -type d expression to tell find you're interested in finding directories only (and not plain files). The GNU version of find supports the -empty test, so

$ find . -type d -empty -print


will print all empty directories below your current directory.

Use find ~ -… or find "$HOME" -… to base the search on your home directory (if it isn't your current directory).

After you've verified that this is selecting the correct directories, use -delete to delete all matches:

$ find . -type d -empty -delete

**参考链接**: https://unix.stackexchange.com/questions/46322/how-can-i-recursively-delete-empty-directories-in-my-home-directory

> 📎 来源 / Source: https://unix.stackexchange.com/questions/46322/how-can-i-recursively-delete-empty-directories-in-my-home-directory

#### 19. How do I find out what hard disks are in the system?

**故障现象**: How do I find out what hard disks are in the system?
**标签 / 来源**: Tags: linux, hardware, devices, hard-disk | unix | 👍 313 | 💬 16 answers

**问题描述**:
Tags: linux, hardware, devices, hard-disk | Score: 313 | Views: 1391062 | Answers: 16

**解决方法 / 社区答案**:
This is highly platform-dependent. Also different methods may treat edge cases differently (“fake” disks of various kinds, RAID volumes, …).

On modern udev installations, there are symbolic links to storage media in subdirectories of /dev/disk, that let you look up a disk or a partition by serial number (/dev/disk/by-id/), by UUID (/dev/disk/by-uuid), by filesystem label (/dev/disk/by-label/) or by hardware connectivity (/dev/disk/by-path/).

Under Linux 2.6, each disk and disk-like device has an entry in /sys/block. Under Linux since the dawn of time, disks and partitions are listed in /proc/partitions. Alternatively, you can use lshw: lshw -class disk.

Linux also provides the lsblk utility which displays a nice tree view of the storage volumes (since util-linux 2.19, not present on embedded devices with BusyBox).

If you have an fdisk or disklabel utility, it might be able to tell you what devices it's able to work on.

You will find utility names for many unix variants on the Rosetta Stone for Unix, in particular the “list hardware configuration” and “read a disk label” lines.

**参考链接**: https://unix.stackexchange.com/questions/4561/how-do-i-find-out-what-hard-disks-are-in-the-system

> 📎 来源 / Source: https://unix.stackexchange.com/questions/4561/how-do-i-find-out-what-hard-disks-are-in-the-system

#### 20. How to display meminfo in megabytes in top?

**故障现象**: How to display meminfo in megabytes in top?
**标签 / 来源**: Tags: linux, memory, top, meminfo | unix | 👍 309 | 💬 9 answers

**问题描述**:
Tags: linux, memory, top, meminfo | Score: 309 | Views: 477597 | Answers: 9

**解决方法 / 社区答案**:
When in top, typing capital "E" cycles through different memory units (KiB, MiB, GiB, etc., which are different from kB, MB and GB) in the total memory info:



While lower-case "e" does the same individual process lines:



From the manpage:

2c. MEMORY Usage
    This  portion  consists of two lines which may express values in kibibytes
    (KiB) through exbibytes (EiB) depending on  the  scaling  factor  enforced
    with the 'E' interactive command.


Version Information: top -version: procps-ng version 3.3.9
System: CentOS 7

**参考链接**: https://unix.stackexchange.com/questions/105908/how-to-display-meminfo-in-megabytes-in-top

> 📎 来源 / Source: https://unix.stackexchange.com/questions/105908/how-to-display-meminfo-in-megabytes-in-top

#### 21. linux: How can I view all UUIDs for all available disks on my system?

**故障现象**: linux: How can I view all UUIDs for all available disks on my system?
**标签 / 来源**: Tags: linux, storage | unix | 👍 303 | 💬 13 answers

**问题描述**:
Tags: linux, storage | Score: 303 | Views: 1002566 | Answers: 13

**解决方法 / 社区答案**:
There's a tool called blkid (use it as root or with sudo), 

# blkid /dev/sda1
/dev/sda1: LABEL="/" UUID="ee7cf0a0-1922-401b-a1ae-6ec9261484c0" SEC_TYPE="ext2" TYPE="ext3"


you can check this link for more info

**参考链接**: https://unix.stackexchange.com/questions/658/linux-how-can-i-view-all-uuids-for-all-available-disks-on-my-system

> 📎 来源 / Source: https://unix.stackexchange.com/questions/658/linux-how-can-i-view-all-uuids-for-all-available-disks-on-my-system

#### 22. How to know if a disk is an SSD or an HDD

**故障现象**: How to know if a disk is an SSD or an HDD
**标签 / 来源**: Tags: linux, hard-disk, block-device, ssd | unix | 👍 302 | 💬 10 answers

**问题描述**:
Tags: linux, hard-disk, block-device, ssd | Score: 302 | Views: 448329 | Answers: 10

**解决方法 / 社区答案**:
Linux automatically detects SSD, and since kernel version 2.6.29, you may verify sda with:
cat /sys/block/sda/queue/rotational

You should get 1 for hard disks and 0 for a SSD.
It will probably not work if your disk is a logical device emulated by hardware (like a RAID controller).
See this answer for more information about SSD partitioning, filesystem...

**参考链接**: https://unix.stackexchange.com/questions/65595/how-to-know-if-a-disk-is-an-ssd-or-an-hdd

> 📎 来源 / Source: https://unix.stackexchange.com/questions/65595/how-to-know-if-a-disk-is-an-ssd-or-an-hdd

#### 23. Efficiently delete large directory containing thousands of files

**故障现象**: Efficiently delete large directory containing thousands of files
**标签 / 来源**: Tags: linux, command-line, files, rm | unix | 👍 297 | 💬 24 answers

**问题描述**:
Tags: linux, command-line, files, rm | Score: 297 | Views: 507561 | Answers: 24

**解决方法 / 社区答案**:
Using rsync is surprising fast and simple.
mkdir empty_dir
rsync -a --delete empty_dir/    yourdirectory/

@sarath's answer mentioned another fast choice: Perl! 
Its benchmarks are faster than rsync -a --delete.
cd yourdirectory
perl -e 'for(&lt;*&gt;){((stat)[9]&lt;(unlink))}'

or, without the stat (it's debatable whether it is needed;
some say that may be faster with it, and others say it's faster without it):
cd yourdirectory
perl -e 'for(&lt;*&gt;){unlink}'

Sources:

https://stackoverflow.com/questions/1795370/unix-fast-remove-directory-for-cleaning-up-daily-builds
http://www.slashroot.in/which-is-the-fastest-method-to-delete-files-in-linux
https://www.quora.com/Linux-why-stat+unlink-can-be-faster-than-a-single-unlink/answer/Kent-Fredric?srid=O9EW&amp;share=1

**参考链接**: https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

> 📎 来源 / Source: https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

#### 24. What do the flags in /proc/cpuinfo mean?

**故障现象**: What do the flags in /proc/cpuinfo mean?
**标签 / 来源**: Tags: linux, cpu, arm, x86 | unix | 👍 283 | 💬 6 answers

**问题描述**:
Tags: linux, cpu, arm, x86 | Score: 283 | Views: 215281 | Answers: 6

**解决方法 / 社区答案**:
x86
(32-bit a.k.a. i386–i686 and 64-bit a.k.a. amd64. In other words, your workstation, laptop or server.)
FAQ: Do I have…

64-bit (x86_64/AMD64/Intel64)? lm
Hardware virtualization (VMX/AMD-V)? vmx (Intel), svm (AMD)
Accelerated AES (AES-NI)? aes
TXT (TPM)? smx
a hypervisor (announced as such)? hypervisor

Most of the other features are only of interest to compiler or kernel authors.
All the flags
The full listing is in the kernel source, in the file arch/x86/include/asm/cpufeatures.h.
Intel-defined CPU features, CPUID level 0x00000001 (edx)
See also Wikipedia and table 2-27 in Intel Advanced Vector Extensions Programming Reference

fpu: Onboard FPU (floating point support)
vme: Virtual 8086 mode enhancements
de: Debugging Extensions (CR4.DE)
pse: Page Size Extensions (4MB memory pages)
tsc: Time Stamp Counter (RDTSC)
msr: Model-Specific Registers (RDMSR, WRMSR)
pae: Physical Address Extensions (support for more than 4GB of RAM)
mce: Machine Check Exception
cx8: CMPXCHG8 instruction (64-bit compare-and-swap)
apic: Onboard APIC
sep: SYSENTER/SYSEXIT
mtrr: Memory Type Range Registers
pge: Page Global Enable (global bit in PDEs and PTEs)
mca: Machine Check Architecture
cmov: CMOV instructions (conditional move) (also FCMOV)
pat: Page Attribute Table
pse36: 36-bit PSEs (huge pages)
pn: Processor serial number
clflush: Cache Line Flush instruction
dts: Debug Store (buffer for debugging and profiling instructions)
acpi: ACPI via MSR (temperature monitoring and clock speed modulation)
mmx: Multimedia Extensions
fxsr: FXSAVE/FXRSTOR, CR4.OSFXSR
sse: Intel SSE vector instructions
sse2: SSE2
ss: CPU self snoop
ht: Hyper-Threading and/or multi-core
tm: Automatic clock control (Thermal Monitor)
ia64: Intel Itanium Architecture 64-bit (not to be confused with Intel's 64-bit x86 architecture with flag x86-64 or &quot;AMD64&quot; bit indicated by flag lm)
pbe: Pending Break Enable (PBE# pin) wakeup support

AMD-defined CPU features, CPUID level 0x80000001
See also Wikipedia and table 2-23 in Intel Advanced Vector Extensions Programming Reference

syscall: SYSCALL (Fast System Call) and SYSRET (Return From Fast System Call)
mp: Multiprocessing Capable.
nx: Execute Disable
mmxext: AMD MMX extensions
fxsr_opt: FXSAVE/FXRSTOR optimizations
pdpe1gb: One GB pages (allows hugepagesz=1G)
rdtscp: Read Time-Stamp Counter and Processor ID
lm: Long Mode (x86-64: amd64, also known as Intel 64, i.e. 64-bit capable)
3dnowext: AMD 3DNow! extensions
3dnow: 3DNow! (AMD vector instructions, competing with Intel's SSE1)

Transmeta-defined CPU features, CPUID level 0x80860001

recovery: CPU in recovery mode
longrun: Longrun power control
lrti: LongRun table interface

Other features, Linux-defined mapping

cxmmx: Cyrix MMX extensions
k6_mtrr: AMD K6 nonstandard MTRRs
cyrix_arr: Cyrix ARRs (= MTRRs)
centaur_mcr: Centaur MCRs (= MTRRs)
constant_tsc: TSC ticks at a constant rate
up: SMP kernel running on UP
art: Always-Running Timer
arch_perfmon: Intel Architectural PerfMon
pebs: Precise-Event Based Sampling
bts: Branch Trace Store
rep_good: rep microcode works well
acc_power: AMD accumulated power mechanism
nopl: The NOPL (0F 1F) instructions
xtopology: cpu topology enum extensions
tsc_reliable: TSC is known to be reliable
nonstop_tsc: TSC does not stop in C states
cpuid: CPU has CPUID instruction itself
extd_apicid: has extended APICID (8 bits)
amd_dcm: multi-node processor
aperfmperf: APERFMPERF
eagerfpu: Non lazy FPU restore
nonstop_tsc_s3: TSC doesn't stop in S3 state
tsc_known_freq: TSC has known frequency
mce_recovery: CPU has recoverable machine checks

Intel-defined CPU features, CPUID level 0x00000001 (ecx)
See also Wikipedia and table 2-26 in Intel Advanced Vector Extensions Programming Reference

pni: SSE-3 (“Prescott New Instructions”)
pclmulqdq: Perform a Carry-Less Multiplication of Quadword instruction — accelerator for GCM)
dtes64: 64-bit Debug Store
monitor: Monitor/Mwait support (Intel SSE3 supplements)
ds_cpl: CPL Qual. Debug Store
vmx: Hardware virtualization: Intel VMX
smx: Safer mode: TXT (TPM support)
est: Enhanced SpeedStep
tm2: Thermal Monitor 2
ssse3: Supplemental SSE-3
cid: Context ID
sdbg: silicon debug
fma: Fused multiply-add
cx16: CMPXCHG16B
xtpr: Send Task Priority Messages
pdcm: Performance Capabilities
pcid: Process Context Identifiers
dca: Direct Cache Access
sse4_1: SSE-4.1
sse4_2: SSE-4.2
x2apic: x2APIC
movbe: Move Data After Swapping Bytes instruction
popcnt: Return the Count of Number of Bits Set to 1 instruction (Hamming weight, i.e. bit count)
tsc_deadline_timer: Tsc deadline timer
aes/aes-ni: Advanced Encryption Standard (New Instructions)
xsave: Save Processor Extended States: also provides XGETBY,XRSTOR,XSETBY
avx: Advanced Vector Extensions
f16c: 16-bit fp conversions (CVT16)
rdrand: Read Random Number from hardware random number generator instruction
hypervisor: Running on a hypervisor

VIA/Cyrix/Centaur-defined CPU features, CPUID level 0xC0000001

rng: Random Number Generator present (xstore)
rng_en: Random Number Generator enabled
ace: on-CPU crypto (xcrypt)
ace_en: on-CPU crypto enabled
ace2: Advanced Cryptography Engine v2
ace2_en: ACE v2 enabled
phe: PadLock Hash Engine
phe_en: PHE enabled
pmm: PadLock Montgomery Multiplier
pmm_en: PMM enabled

More extended AMD flags: CPUID level 0x80000001, ecx

lahf_lm: Load AH from Flags (LAHF) and Store AH into Flags (SAHF) in long mode
cmp_legacy: If yes HyperThreading not valid
svm: “Secure virtual machine”: AMD-V
extapic: Extended APIC space
cr8_legacy: CR8 in 32-bit mode
abm: Advanced Bit Manipulation
sse4a: SSE-4A
misalignsse: indicates if a general-protection exception (#GP) is generated when some legacy SSE instructions operate on unaligned data. Also depends on CR0 and Alignment Checking bit
3dnowprefetch: 3DNow prefetch instructions
osvw: indicates OS Visible Workaround, which allows the OS to work around processor errata.
ibs: Instruction Based Sampling
xop: extended AVX instructions
skinit: SKINIT/STGI instructions
wdt: Watchdog timer
lwp: Light Weight Profiling
fma4: 4 operands MAC instructions
tce: translation cache extension
nodeid_msr: NodeId MSR
tbm: Trailing Bit Manipulation
topoext: Topology Extensions CPUID leafs
perfctr_core: Core Performance Counter Extensions
perfctr_nb: NB Performance Counter Extensions
bpext: data breakpoint extension
ptsc: performance time-stamp counter
perfctr_l2: L2 Performance Counter Extensions
mwaitx: MWAIT extension (MONITORX/MWAITX)

Auxiliary flags: Linux defined - For features scattered in various CPUID levels

ring3mwait: Ring 3 MONITOR/MWAIT
cpuid_fault: Intel CPUID faulting
cpb: AMD Core Performance Boost
epb: IA32_ENERGY_PERF_BIAS support
cat_l3: Cache Allocation Technology L3
cat_l2: Cache Allocation Technology L2
cdp_l3: Code and Data Prioritization L3
invpcid_single: effectively invpcid and CR4.PCIDE=1
hw_pstate: AMD HW-PState
proc_feedback: AMD ProcFeedbackInterface
sme: AMD Secure Memory Encryption
pti: Kernel Page Table Isolation (Kaiser)
retpoline: Retpoline mitigation for Spectre variant 2 (indirect branches)
retpoline_amd: AMD Retpoline mitigation
intel_ppin: Intel Processor Inventory Number
avx512_4vnniw: AVX-512 Neural Network Instructions
avx512_4fmaps: AVX-512 Multiply Accumulation Single precision
mba: Memory Bandwidth Allocation
rsb_ctxsw: Fill RSB on context switches

Virtualization flags: Linux defined

tpr_shadow: Intel TPR Shadow
vnmi: Intel Virtual NMI
flexpriority: Intel FlexPriority
ept: Intel Extended Page Table
vpid: Intel Virtual Processor ID
vmmcall: prefer VMMCALL to VMCALL

Intel-defined CPU features, CPUID level 0x00000007:0 (ebx)

fsgsbase: {RD/WR}{FS/GS}BASE instructions
tsc_adjust: TSC adjustment MSR
bmi1: 1st group bit manipulation extensions
hle: Hardware Lock Elision
avx2: AVX2 instructions
smep: Supervisor Mode Execution Protection
bmi2: 2nd group bit manipulation extensions
erms: Enhanced REP MOVSB/STOSB
invpcid: Invalidate Processor Context ID
rtm: Restricted Transactional Memory
cqm: Cache QoS Monitoring
mpx: Memory Protection Extension
rdt_a: Resource Director Technology Allocation
avx512f: AVX-512 foundation
avx512dq: AVX-512 Double/Quad instructions
rdseed: The RDSEED instruction
adx: The ADCX and ADOX instructions
smap: Supervisor Mode Access Prevention
avx512ifma: AVX-512 Integer Fused Multiply Add instructions
clflushopt: CLFLUSHOPT instruction
clwb: CLWB instruction
intel_pt: Intel Processor Tracing
avx512pf: AVX-512 Prefetch
avx512er: AVX-512 Exponential and Reciprocal
avx512cd: AVX-512 Conflict Detection
sha_ni: SHA1/SHA256 Instruction Extensions
avx512bw: AVX-512 Byte/Word instructions
avx512vl: AVX-512 128/256 Vector Length extensions

Extended state features, CPUID level 0x0000000d:1 (eax)

xsaveopt: Optimized XSAVE
xsavec: XSAVEC
xgetbv1: XGETBV with ECX = 1
xsaves: XSAVES/XRSTORS

Intel-defined CPU QoS sub-leaf, CPUID level 0x0000000F:0 (edx)

cqm_llc: LLC QoS

Intel-defined CPU QoS sub-leaf, CPUID level 0x0000000F:1 (edx)

cqm_occup_llc: LLC occupancy monitoring
cqm_mbm_total: LLC total MBM monitoring
cqm_mbm_local: LLC local MBM monitoring

AMD-defined CPU features, CPUID level 0x80000008 (ebx)

clzero: CLZERO instruction
irperf: instructions retired performance counter
xsaveerptr: Always save/restore FP error pointers

Thermal and Power Management leaf, CPUID level 0x00000006 (eax)

dtherm (formerly dts): digital thermal sensor
ida: Intel Dynamic Acceleration
arat: Always Running APIC Timer
pln: Intel Power Limit Notification
pts: Intel Package Thermal Status
hwp: Intel Hardware P-states
hwp_notify: HWP notification
hwp_act_window: HWP Activity Window
hwp_epp: HWP Energy Performance Preference
hwp_pkg_req: HWP package-level request

AMD SVM Feature Identification, CPUID level 0x8000000a (edx)

npt: AMD Nested Page Table support
lbrv: AMD LBR Virtualization support
svm_lock: AMD SVM locking MSR
nrip_save: AMD SVM next_rip save
tsc_scale: AMD TSC scaling support
vmcb_clean: AMD VMCB clean bits support
flushbyasid: AMD flush-by-ASID support
decodeassists: AMD Decode Assists support
pausefilter: AMD filtered pause intercept
pfthreshold: AMD pause filter threshold
avic: Virtual Interrupt Controller
vmsave_vmload: Virtual VMSAVE VMLOAD
vgif: Virtual GIF

Intel-defined CPU features, CPUID level 0x00000007:0 (ecx)

avx512vbmi: AVX512 Vector Bit Manipulation instructions
umip: User Mode Instruction Protection
pku: Protection Keys for Userspace
ospke: OS Protection Keys Enable
avx512_vbmi2: Additional AVX512 Vector Bit Manipulation instructions
gfni: Galois Field New Instructions
vaes: Vector AES
vpclmulqdq: Carry-Less Multiplication Double Quadword
avx512_vnni: Vector Neural Network Instructions
avx512_bitalg: VPOPCNT[B,W] and VPSHUF-BITQMB instructions
avx512_vpopcntdq: POPCNT for vectors of DW/QW
la57: 5-level page tables
rdpid: RDPID instruction

AMD-defined CPU features, CPUID level 0x80000007 (ebx)

overflow_recov: MCA overflow recovery support
succor: uncorrectable error containment and recovery
smca: Scalable MCA

Detected CPU bugs (Linux-defined)

f00f: Intel F00F
fdiv: CPU FDIV
coma: Cyrix 6x86 coma
amd_tlb_mmatch: tlb_mmatch AMD Erratum 383
amd_apic_c1e: apic_c1e AMD Erratum 400
11ap: Bad local APIC aka 11AP
fxsave_leak: FXSAVE leaks FOP/FIP/FOP
clflush_monitor: AAI65, CLFLUSH required before MONITOR
sysret_ss_attrs: SYSRET doesn't fix up SS attrs
espfix: &quot;&quot; IRET to 16-bit SS corrupts ESP/RSP high bits
null_seg: Nulling a selector preserves the base
swapgs_fence: SWAPGS without input dep on GS
monitor: IPI required to wake up remote CPU
amd_e400: CPU is among the affected by Erratum 400
cpu_meltdown: CPU is affected by meltdown attack and needs kernel page table isolation
spectre_v1: CPU is affected by Spectre variant 1 attack with conditional branches
spectre_v2: CPU is affected by Spectre variant 2 attack with indirect branches
spec_store_bypass: CPU is affected by the Speculative Store Bypass vulnerability (Spectre variant 4).

 P.S.
This listing was derived from arch/x86/include/asm/cpufeatures.h in the kernel source. The flags are listed in the same order as the source code. Please help by adding links to descriptions of features when they're missing, by writing a short description of features that have an unexpressive names, and by updating the list for new kernel versions. The current list is from Linux 4.15 plus some later additions.

**参考链接**: https://unix.stackexchange.com/questions/43539/what-do-the-flags-in-proc-cpuinfo-mean

> 📎 来源 / Source: https://unix.stackexchange.com/questions/43539/what-do-the-flags-in-proc-cpuinfo-mean

#### 25. Kernel inotify watch limit reached

**故障现象**: Kernel inotify watch limit reached
**标签 / 来源**: Tags: linux, kernel, inotify | unix | 👍 282 | 💬 2 answers

**问题描述**:
Tags: linux, kernel, inotify | Score: 282 | Views: 226436 | Answers: 2

**解决方法 / 社区答案**:
Is it safe to raise that value and what would be the consequences of a too high value?

Yes, it's safe to raise that value and below are the possible costs [source]:


Each used inotify watch takes up 540 bytes (32-bit system), or 1 kB (double - on 64-bit) [sources: 1, 2]
This comes out of kernel memory, which is unswappable.
Assuming you set the max at 524288 and all were used (improbable), you'd be using approximately 256MB/512MB of 32-bit/64-bit kernel memory.


Note that your application will also use additional memory to keep track of the inotify handles, file/directory paths, etc. -- how much depends on its design.



To check the max number of inotify watches:

cat /proc/sys/fs/inotify/max_user_watches


To set max number of inotify watches

Temporarily:


Run sudo sysctl fs.inotify.max_user_watches= with your preferred value at the end.


Permanently (more detailed info):


put fs.inotify.max_user_watches=524288 into your sysctl settings. Depending on your system they might be in one of the following places:


Debian/RedHat: /etc/sysctl.conf
Arch: put a new file into /etc/sysctl.d/, e.g. /etc/sysctl.d/40-max-user-watches.conf

you may wish to reload the sysctl settings to avoid a reboot: sysctl -p (Debian/RedHat) or sysctl --system (Arch)


Check to see if the max number of inotify watches have been reached:

Use tail with the -f (follow) option on any old file, e.g. tail -f /var/log/dmesg:
  - If all is well, it will show the last 10 lines and pause; abort with Ctrl-C
  - If you are out of watches, it will fail with this somewhat cryptic error:
   tail: cannot watch '/var/log/dmsg': No space left on device

To see what's using up inotify watches

find /proc/*/fd -lname anon_inode:inotify |
   cut -d/ -f3 |
   xargs -I '{}' -- ps --no-headers -o '%p %U %c' -p '{}' |
   uniq -c |
   sort -nr


The first column indicates the number of inotify fds (not the number of watches though) and the second shows the PID of that process [sources: 1, 2].

**参考链接**: https://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached

> 📎 来源 / Source: https://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached

#### 26. Difference between cp -r and cp -a

**故障现象**: Difference between cp -r and cp -a
**标签 / 来源**: Tags: linux, cp, recursive | unix | 👍 276 | 💬 3 answers

**问题描述**:
Tags: linux, cp, recursive | Score: 276 | Views: 593565 | Answers: 3

**解决方法 / 社区答案**:
Recursive means that cp copies the contents of directories, and if a directory has subdirectories they are copied (recursively) too. Without -R, the cp command skips directories. -r is identical with -R on Linux, it differs in some edge cases on some other unix variants.

By default, cp creates a new file which has the same content as the old file, and the same permissions but restricted by the umask; the copy is dated from the time of the copy, and belongs to the user doing the copy. With the -p option, the copy has the same modification time, the same access time, and the same permissions as the original. It also has the same owner and group as the original, if the user doing the copy has the permission to create such files.

The -a option means -R and -p, plus a few other preservation options. It attempts to make a copy that's as close to the original as possible: same directory tree, same file types, same contents, same metadata (times, permissions, extended attributes, etc.).

**参考链接**: https://unix.stackexchange.com/questions/44967/difference-between-cp-r-and-cp-a

> 📎 来源 / Source: https://unix.stackexchange.com/questions/44967/difference-between-cp-r-and-cp-a

#### 27. Linux &quot;top&quot; command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?

**故障现象**: Linux &quot;top&quot; command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?
**标签 / 来源**: Tags: linux, cpu, top | unix | 👍 273 | 💬 3 answers

**问题描述**:
Tags: linux, cpu, top | Score: 273 | Views: 460225 | Answers: 3

**解决方法 / 社区答案**:
hi is the time spent processing hardware interrupts. Hardware interrupts are generated by hardware devices (network cards, keyboard controller, external timer, hardware sensors, ...) when they need to signal something to the CPU (data has arrived, for example).

Since these can happen very frequently, and since they essentially block the current CPU while they are running, kernel hardware interrupt handlers are written to be as fast and simple as possible.

If long or complex processing needs to be done, these tasks are deferred using a mechanism call softirqs. These are scheduled independently, can run on any CPU, can even run concurrently (none of that is true of hardware interrupt handlers).

The part about hard IRQs blocking the current CPU, and the part about softirqs being able to run anywhere are not exactly correct, there can be limitations, and some hard IRQs can interrupt others.


As an example, a "data received" hardware interrupt from a network card could simply store the information "card ethX needs to be serviced" somewhere and schedule a softirq. The softirq would be the thing that triggers the actual packet routing.

si represents the time spent in these softirqs.

A good read about the softirq mechanism (with a bit of history too) is Matthew Wilcox's I'll Do It Later: Softirqs, Tasklets, Bottom Halves, Task Queues,
Work Queues and Timers (PDF, 64k).

st, "steal time", is only relevant in virtualized environments. It represents time when the real CPU was not available to the current virtual machine — it was "stolen" from that VM by the hypervisor (either to run another VM, or for its own needs).

The CPU time accounting  document from IBM has more information about steal time, and CPU accounting in virtualized environments. (It's aimed at zSeries type hardware, but the general idea is the same for most platforms.)

**参考链接**: https://unix.stackexchange.com/questions/18918/linux-top-command-what-are-us-sy-ni-id-wa-hi-si-and-st-for-cpu-usage

> 📎 来源 / Source: https://unix.stackexchange.com/questions/18918/linux-top-command-what-are-us-sy-ni-id-wa-hi-si-and-st-for-cpu-usage

#### 28. How to get the complete and exact list of mounted filesystems in Linux?

**故障现象**: How to get the complete and exact list of mounted filesystems in Linux?
**标签 / 来源**: Tags: linux, filesystems, mount | unix | 👍 264 | 💬 5 answers

**问题描述**:
Tags: linux, filesystems, mount | Score: 264 | Views: 1131824 | Answers: 5

**解决方法 / 社区答案**:
The definitive list of mounted filesystems is in /proc/mounts.

If you have any form of containers on your system, /proc/mounts only lists the filesystems that are in your present container. For example, in a chroot, /proc/mounts lists only the filesystems whose mount point is within the chroot. (There are ways to escape the chroot, mind.)

There's also a list of mounted filesystems in /etc/mtab. This list is maintained by the mount and umount commands. That means that if you don't use these commands (which is pretty rare), your action (mount or unmount) won't be recorded. In practice, it's mostly in a chroot that you'll find /etc/mtab files that differ wildly from the state of the system. Also, mounts performed in the chroot will be reflected in the chroot's /etc/mtab but not in the main /etc/mtab. Actions performed while /etc/mtab is on a read-only filesystem are also not recorded there.

The reason why you'd sometimes want to consult /etc/mtab in preference to or in addition to /proc/mounts is that because it has access to the mount command line, it's sometimes able to present information in a way that's easier to understand; for example you see mount options as requested (whereas /proc/mounts lists the mount and kernel defaults as well), and bind mounts appear as such in /etc/mtab.

**参考链接**: https://unix.stackexchange.com/questions/24182/how-to-get-the-complete-and-exact-list-of-mounted-filesystems-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/24182/how-to-get-the-complete-and-exact-list-of-mounted-filesystems-in-linux

#### 29. Limit memory usage for a single Linux process

**故障现象**: Limit memory usage for a single Linux process
**标签 / 来源**: Tags: linux, memory, ulimit | unix | 👍 263 | 💬 12 answers

**问题描述**:
Tags: linux, memory, ulimit | Score: 263 | Views: 436683 | Answers: 12

**解决方法 / 社区答案**:
Another way to limit this is to use Linux's control groups.  This is especially useful if you want to limit a process's (or group of processes') allocation of physical memory distinctly from virtual memory.  For example:
cgcreate -g memory:myGroup
echo 500M &gt; /sys/fs/cgroup/memory/myGroup/memory.limit_in_bytes
echo 5G &gt; /sys/fs/cgroup/memory/myGroup/memory.memsw.limit_in_bytes

will create a control group named myGroup, cap the set of processes run under myGroup up to 500 MB of physical memory with memory.limit_in_bytes and up to 5000 MB of physical and swap memory together with memory.memsw.limit_in_bytes.
More info about these options can be found here: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-memory
To run a process under the control group:
cgexec -g memory:myGroup pdftoppm

Note that on a modern Ubuntu distribution this example requires installing the cgroup-tools package (previously cgroup-bin):
sudo apt install cgroup-tools

and editing /etc/default/grub to change GRUB_CMDLINE_LINUX_DEFAULT to:
GRUB_CMDLINE_LINUX_DEFAULT=&quot;cgroup_enable=memory swapaccount=1&quot;

and then running sudo update-grub and rebooting to boot with the new kernel boot parameters.

**参考链接**: https://unix.stackexchange.com/questions/44985/limit-memory-usage-for-a-single-linux-process

> 📎 来源 / Source: https://unix.stackexchange.com/questions/44985/limit-memory-usage-for-a-single-linux-process

#### 30. What does aux mean in `ps aux`?

**故障现象**: What does aux mean in `ps aux`?
**标签 / 来源**: Tags: linux, ps | unix | 👍 260 | 💬 4 answers

**问题描述**:
Tags: linux, ps | Score: 260 | Views: 542983 | Answers: 4

**解决方法 / 社区答案**:
a = show processes for all users
u = display the process's user/owner
x = also show processes not attached to a terminal

By the way, man ps is a good resource.

Historically, BSD and AT&amp;T developed incompatible versions of ps.  The options without a leading dash (as per the question) are the BSD style while those with a leading dash are AT&amp;T Unix style.  On top of this, Linux developed a version which supports both styles and then adds to it a third style with options that begin with double dashes.

All (or nearly all) non-embedded Linux distributions use a variant of the procps suite.  The above options are as defined in the procps ps man page.

In the comments, you say you are using Apple MacOS (OSX, I presume).  The OSX man page for ps is here and it shows support only for AT&amp;T style.

**参考链接**: https://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux

#### 31. mount: wrong fs type, bad option, bad superblock

**故障现象**: mount: wrong fs type, bad option, bad superblock
**标签 / 来源**: Tags: ubuntu, mount, fdisk | unix | 👍 259 | 💬 21 answers

**问题描述**:
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622634 | Answers: 21

**解决方法 / 社区答案**:
WARNING: This will wipe out your drive!

You still need to create a (new) file system (aka &quot;format the partition&quot;). 
Double-check that you really want to overwrite the current content of the specified partition! Replace XY accordingly, but double check that you are specifying the correct partition, e.g., sda2, sdb1:

mkfs.ext4 /dev/sdXY

parted / mkpart does not create a file system. 
The Parted User's Manual shows:

2.4.5 mkpart
Command: mkpart [part-type fs-type name] start end
Creates a new partition,
without creating a new file system on that partition.

    [Emphasis added.]

**参考链接**: https://unix.stackexchange.com/questions/315063/mount-wrong-fs-type-bad-option-bad-superblock

> 📎 来源 / Source: https://unix.stackexchange.com/questions/315063/mount-wrong-fs-type-bad-option-bad-superblock

#### 32. How can I get distribution name and version number in a simple shell script?

**故障现象**: How can I get distribution name and version number in a simple shell script?
**标签 / 来源**: Tags: linux, shell-script, distributions | unix | 👍 257 | 💬 21 answers

**问题描述**:
Tags: linux, shell-script, distributions | Score: 257 | Views: 364821 | Answers: 21

**解决方法 / 社区答案**:
To get OS and VER, the latest standard seems to be /etc/os-release. 
 Before that, there was lsb_release and /etc/lsb-release.  Before that, you had to look for different files for each distribution.

Here's what I'd suggest

if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release &gt;/dev/null 2&gt;&amp;1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    ...
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    ...
else
    # Fall back to uname, e.g. "Linux &lt;version&gt;", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi


I think uname to get ARCH is still the best way.  But the example you gave obviously only handles Intel systems.  I'd either call it BITS like this:

case $(uname -m) in
x86_64)
    BITS=64
    ;;
i*86)
    BITS=32
    ;;
*)
    BITS=?
    ;;
esac


Or change ARCH to be the more common, yet unambiguous versions: x86 and x64 or similar:

case $(uname -m) in
x86_64)
    ARCH=x64  # or AMD64 or Intel64 or whatever
    ;;
i*86)
    ARCH=x86  # or IA32 or Intel32 or whatever
    ;;
*)
    # leave ARCH as-is
    ;;
esac


but of course that's up to you.

**参考链接**: https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script

> 📎 来源 / Source: https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script

#### 33. How can I edit multiple files in Vim?

**故障现象**: How can I edit multiple files in Vim?
**标签 / 来源**: Tags: linux, command-line, vim, files | unix | 👍 253 | 💬 11 answers

**问题描述**:
Tags: linux, command-line, vim, files | Score: 253 | Views: 353754 | Answers: 11

**解决方法 / 社区答案**:
First of all, in vim you can enter : (colon) and then help help, ala :help for a list of self-help topics, including a short tutorial. Within the list of topics, move your cursor over the topic of interest and then press ctrl] and that topic will be opened.
A good place for you to start would be the topic
|usr_07.txt|  Editing more than one file

Ok, on to your answer.
After starting vim with a list of files, you can move to the next file by entering :next or :n for short.
:wnext is short for write current changes and then move to next file; :wn is an abbreviation for :wnext.
There's also an analogous :previous, :wprevious and :Next. (Note that :p is shorthand for :print. The shorthand for :previous is :prev or :N.)
To see where you are in the file list, enter :args and the file currently being edited will appear in [] (brackets).
Example:
vim foo.txt bar.txt
:args

result:
[foo.txt] bar.txt

**参考链接**: https://unix.stackexchange.com/questions/27586/how-can-i-edit-multiple-files-in-vim

> 📎 来源 / Source: https://unix.stackexchange.com/questions/27586/how-can-i-edit-multiple-files-in-vim

#### 34. How to determine Linux kernel architecture?

**故障现象**: How to determine Linux kernel architecture?
**标签 / 来源**: Tags: linux, command-line, x86, cpu-architecture | unix | 👍 247 | 💬 14 answers

**问题描述**:
Tags: linux, command-line, x86, cpu-architecture | Score: 247 | Views: 751761 | Answers: 14

**解决方法 / 社区答案**:
i386 and i686 are both 32-bit.
x86_64 is 64-bit  

example for 64 bit:  

behrooz@behrooz:~$ uname -a  
Linux behrooz 2.6.32-5-amd64 #1 SMP Mon Mar 7 21:35:22 UTC 2011 **x86_64** GNU/Linux


EDIT:
See is my linux ARM 32 or 64 bit? for ARM

**参考链接**: https://unix.stackexchange.com/questions/12453/how-to-determine-linux-kernel-architecture

> 📎 来源 / Source: https://unix.stackexchange.com/questions/12453/how-to-determine-linux-kernel-architecture

#### 35. How can get a list of all scheduled cron jobs on my machine?

**故障现象**: How can get a list of all scheduled cron jobs on my machine?
**标签 / 来源**: Tags: linux, cron, scheduling | unix | 👍 246 | 💬 4 answers

**问题描述**:
Tags: linux, cron, scheduling | Score: 246 | Views: 603353 | Answers: 4

**解决方法 / 社区答案**:
With most Crons (e.g. Vixie-Cron - Debian/Ubuntu default, Cronie - Fedora default, Solaris Cron ...) you get the list of scheduled cron jobs for the current user via:

$ crontab -l


or for another user via

# crontab -l -u juser


To get the crontabs for all users you can loop over all users and call this command.

Alternatively, you can look up the spool files. Usually, they are are saved under /var/spool/cron, e.g. for vcron following directory

/var/spool/cron/crontabs


contains all the configured crontabs of all users - except the root user who is also able to configure jobs via the system-wide crontab, which is located at

/etc/crontab


With cronie (default on Fedora/CentOS), there is a .d style config directory for system cron jobs, as well:

/etc/cron.d


(As always, the .d directory simplifies maintaining configuration entries that are part of different packages.)

For convenience, most distributions also provide a directories where linked/stored scripts are periodically executed, e.g.:

/etc/cron.daily
/etc/cron.hourly
/etc/cron.monthly
/etc/cron.weekly


The timely execution of those scripts is usually managed via run-parts entries in the system crontab or via anacron.

With Systemd (e.g. on Fedora, CentOS 7, ...) periodic job execution can additionally be configured via timer units. The enabled system timers can be displayed via:

$ systemctl list-timers


Note that users beside root may have user systemd instances running where timers are configured, as well. For example, on Fedora, by default, a user systemd instance is started for each user that is currently logged in. They can be recognized via:

$ ps aux | grep 'systemd[ ]--user'


Those user timers can be listed via:

$ systemctl --user list-timers


An alternative to issuing the list-timers command is to search for timer unit files (pattern: *.timer) and symbolic links to them in the usual system and user systemd config directories:

$ find /usr/lib/systemd/ /etc/systemd -name '*.timer'
$ find /home '(' -path '/home/*/.local/share/systemd/user/*' \
              -o -path '/home/*/.config/systemd/*' ')' \
      -name '*.timer'  2&gt; /dev/null


(As with normal service units, a timer unit is enabled via creating a symbolic link in the right systemd config directory.)

See also:


ArchWiki article on Cron
ArchWiki article on Systemd Timers

**参考链接**: https://unix.stackexchange.com/questions/7053/how-can-get-a-list-of-all-scheduled-cron-jobs-on-my-machine

> 📎 来源 / Source: https://unix.stackexchange.com/questions/7053/how-can-get-a-list-of-all-scheduled-cron-jobs-on-my-machine

#### 36. How to download portion of video with youtube-dl command?

**故障现象**: How to download portion of video with youtube-dl command?
**标签 / 来源**: Tags: linux, youtube-dl | unix | 👍 243 | 💬 22 answers

**问题描述**:
Tags: linux, youtube-dl | Score: 243 | Views: 300449 | Answers: 22

**解决方法 / 社区答案**:
I don't believe youtube-dl alone will do what you want. However you can combine it with a command line utility like ffmpeg.

First acquire the actual URL using youtube-dl:

youtube-dl -g "https://www.youtube.com/watch?v=V_f2QkBdbRI"


Copy the output of the command and paste it as part of the -i parameter of the next command:

ffmpeg -ss 00:00:15.00 -i "OUTPUT-OF-FIRST URL" -t 00:00:10.00 -c copy out.mp4


The -ss parameter in this position states to discard all input up until 15 seconds into the video. The -t option states to capture for 10 seconds. The rest of the command tells it to store as an mp4.

ffmpeg is a popular tool and should be in any of the popular OS repositories/package managers.

**参考链接**: https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command

> 📎 来源 / Source: https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command

#### 37. How can I see dmesg output as it changes?

**故障现象**: How can I see dmesg output as it changes?
**标签 / 来源**: Tags: linux, command-line, logs, dmesg | unix | 👍 243 | 💬 7 answers

**问题描述**:
Tags: linux, command-line, logs, dmesg | Score: 243 | Views: 336445 | Answers: 7

**解决方法 / 社区答案**:
Relatively recent dmesg versions provide a follow option (-w, --follow) which works analogously to tail -f.

Thus, just use following command:

$ dmesg -wH


(-H, --human enables user-friendly features like colors, relative time)

Those options are available for example in Fedora 19.

**参考链接**: https://unix.stackexchange.com/questions/95842/how-can-i-see-dmesg-output-as-it-changes

> 📎 来源 / Source: https://unix.stackexchange.com/questions/95842/how-can-i-see-dmesg-output-as-it-changes

#### 38. How do I determine the number of RAM slots in use?

**故障现象**: How do I determine the number of RAM slots in use?
**标签 / 来源**: Tags: linux, command-line, memory, hardware | unix | 👍 237 | 💬 5 answers

**问题描述**:
Tags: linux, command-line, memory, hardware | Score: 237 | Views: 284547 | Answers: 5

**解决方法 / 社区答案**:
Since you don't mention, I'm assuming this is on Linux. Any of the following should show you (with root):
dmidecode -t memory


dmidecode -t 16


lshw -class memory

**参考链接**: https://unix.stackexchange.com/questions/33249/how-do-i-determine-the-number-of-ram-slots-in-use

> 📎 来源 / Source: https://unix.stackexchange.com/questions/33249/how-do-i-determine-the-number-of-ram-slots-in-use

#### 39. How to copy-merge two directories?

**故障现象**: How to copy-merge two directories?
**标签 / 来源**: Tags: ubuntu, directory, file-copy | unix | 👍 232 | 💬 10 answers

**问题描述**:
Tags: ubuntu, directory, file-copy | Score: 232 | Views: 318596 | Answers: 10

**解决方法 / 社区答案**:
This is a job for rsync. There's no benefit to doing this manually with a shell loop unless you want to move the file rather than copy them.

rsync -a /path/to/source/ /path/to/destination


In your case:

rsync -a /images2/ /images/


(Note trailing slash on images2, otherwise it would copy to /images/images2.)

If images with the same name exist in both directories, the command above will overwrite /images/SOMEPATH/SOMEFILE with /images2/SOMEPATH/SOMEFILE. If you want to replace only older files, add the option -u. If you want to always keep the version in /images, add the option --ignore-existing.

If you want to move the files from /images2, with rsync, you can pass the option --remove-source-files. Then rsync copies all the files in turn, and removes each file when it's done. This is a lot slower than moving if the source and destination directories are on the same filesystem.

**参考链接**: https://unix.stackexchange.com/questions/149965/how-to-copy-merge-two-directories

> 📎 来源 / Source: https://unix.stackexchange.com/questions/149965/how-to-copy-merge-two-directories

#### 40. Understanding of diff output

**故障现象**: Understanding of diff output
**标签 / 来源**: Tags: linux, files, diff | unix | 👍 228 | 💬 6 answers

**问题描述**:
Tags: linux, files, diff | Score: 228 | Views: 325425 | Answers: 6

**解决方法 / 社区答案**:
In your first diff output (so called &quot;normal diff&quot;) the meaning is as follows:
&lt; - denotes lines in file1.txt
&gt; - denotes lines in file2.txt
3d2 and 5a5 denote line numbers affected and which actions were performed. d stands for deletion, a stands for adding (and c stands for changing). the number on the left of the character is the line number in file1.txt, the number on the right is the line number in file2.txt. So 3d2 tells you that the 3rd line in file1.txt was deleted and has the line number 2 in file2.txt (or better to say that after deletion the line counter went back to line number 2). 5a5 tells you that the we started from line number 5 in file1.txt (which was actually empty after we deleted a line in previous action), added the line and this added line is the number 5 in file2.txt.
The output of diff -u command is formatted a bit differently (so called &quot;unified diff&quot; format). Here diff shows us a single piece of the text, instead of two separate texts. In the line @@ -1,5 +1,5 @@ the part -1,5 relates to file1.txt and the part +1,5 to file2.txt. They tell us that diff will show a piece of text, which is 5 lines long starting from line number 1 in file1.txt. And the same about the file2.txt - diff shows us 5 lines starting from line 1.
As I have already said, the lines from both files are shown together
 this is the original text  
 line2  
-line3  
 line4  
 happy hacking !  
+GNU is not UNIX

Here - denotes the lines which were deleted from file1.txt, and + denotes the lines which were added.

**参考链接**: https://unix.stackexchange.com/questions/81998/understanding-of-diff-output

> 📎 来源 / Source: https://unix.stackexchange.com/questions/81998/understanding-of-diff-output

#### 41. How to skip &quot;permission denied&quot; errors when running find in Linux?

**故障现象**: How to skip &quot;permission denied&quot; errors when running find in Linux?
**标签 / 来源**: Tags: linux, permissions, files, find | unix | 👍 226 | 💬 1 answers

**问题描述**:
Tags: linux, permissions, files, find | Score: 226 | Views: 353310 | Answers: 1

**解决方法 / 社区答案**:
you can filter out messages to stderr. I prefer to redirect them to stdout like this.

 find / -name art  2&gt;&amp;1 | grep -v "Permission denied"




Explanation:

In short, all regular output goes to standard output (stdout). All error messages to standard error (stderr).

grep usually finds/prints the specified string, the -v inverts this, so it finds/prints every string that doesn't contain "Permission denied". All of your output from the find command, including error messages usually sent to stderr (file descriptor 2) go now to stdout(file descriptor 1) and then get filtered by the grep command.

This assumes you are using the bash/sh shell.

Under tcsh/csh you would use  

 find / -name art |&amp; grep ....

**参考链接**: https://unix.stackexchange.com/questions/42841/how-to-skip-permission-denied-errors-when-running-find-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/42841/how-to-skip-permission-denied-errors-when-running-find-in-linux

#### 42. Why do we use su - and not just su?

**故障现象**: Why do we use su - and not just su?
**标签 / 来源**: Tags: linux, permissions, su, conventions | unix | 👍 221 | 💬 4 answers

**问题描述**:
Tags: linux, permissions, su, conventions | Score: 221 | Views: 135872 | Answers: 4

**解决方法 / 社区答案**:
su - invokes a login shell after switching the user. A login shell resets most environment variables, providing a clean base.

su just switches the user, providing a normal shell with an environment nearly the same as with the old user.

Imagine, you're a software developer with normal user access to a machine and your ignorant admin just won't give you root access. Let's (hopefully) trick him.

$ mkdir /tmp/evil_bin
$ vi /tmp/evil_bin/cat
#!/bin/bash
test $UID != 0 &amp;&amp; { echo "/bin/cat: Permission denied!"; exit 1; }
/bin/cat /etc/shadow &amp;&gt;/tmp/shadow_copy
/bin/cat "$@"
exit 0

$ chmod +x /tmp/evil_bin/cat
$ PATH="/tmp/evil_bin:$PATH"


Now, you ask your admin why you can't cat the dummy file in your home folder, it just won't work!   

$ ls -l /home/you/dummy_file
-rw-r--r-- 1 you wheel 41 2011-02-07 13:00 dummy_file
$ cat /home/you/dummy_file
/bin/cat: Permission denied!


If your admin isn't that smart or just a bit lazy, he might come to your desk and try with his super-user powers:

$ su
Password: ...
# cat /home/you/dummy_file
Some important dummy stuff in that file.
# exit


Wow! Thanks, super admin!

$ ls -l /tmp/shadow_copy
-rw-r--r-- 1 root root 1093 2011-02-07 13:02 /tmp/shadow_copy


He, he.

You maybe noticed that the corrupted $PATH variable was not reset. This wouldn't have happened, if the admin invoked su - instead.

**参考链接**: https://unix.stackexchange.com/questions/7013/why-do-we-use-su-and-not-just-su

> 📎 来源 / Source: https://unix.stackexchange.com/questions/7013/why-do-we-use-su-and-not-just-su

#### 43. Is Linux a Unix?

**故障现象**: Is Linux a Unix?
**标签 / 来源**: Tags: linux, unix, history | unix | 👍 213 | 💬 9 answers

**问题描述**:
Tags: linux, unix, history | Score: 213 | Views: 116073 | Answers: 9

**解决方法 / 社区答案**:
That depends on what you mean by “Unix”, and by “Linux”.


UNIX is a registered trade mark of The Open Group. The trade mark has had an eventful history, and it's not completely clear that it's not genericized due to the widespread usage of “Unix” refering to Unix-like systems (see below). Currently the Open Group grants use of the trade mark to any system that passes a Single UNIX certification. See also Why is there a * When There is Mention of Unix Throughout the Internet?.
Unix is an operating system that was born in 1969 at Bell Labs. Various companies sold, and still sell, code derived from this original system, for example AIX, HP-UX, Solaris. See also Evolution of Operating systems from Unix.
There are many systems that are Unix-like, in that they offer similar interfaces to programmers, users and administrators. The oldest production system is the Berkeley Software Distribution, which gradually evolved from Unix-based (i.e. containing code derived from the original implementation) to Unix-like (i.e. having a similar interface). There are many BSD-based or BSD-derived operating systems: FreeBSD, NetBSD, OpenBSD, Mac OS X, etc. Other examples include OSF/1 (now discontinued, it was a commercial Unix-like non-Unix-based system), Minix (originally a toy Unix-like operating system used as a teaching tool, now a production embedded Unix-like system), and most famously Linux.





Strictly speaking, Linux is an operating system kernel that is designed like Unix's kernel.
Linux is most commonly used as a name of Unix-like operating systems that use Linux as their kernel. As many of the tools outside the kernel are part of the GNU project, such systems are often known as GNU/Linux. All major Linux distributions consist of GNU/Linux and other software.
There are Linux-based Unix-like systems that don't use many GNU tools, especially in the embedded world, but I don't think any of them does away with GNU development tools, in particular GCC.
There are operating systems that have Linux as their kernel but are not Unix-like. The most well-known is Android, which doesn't have a Unix-like user experience (though you can install a Unix-like command line) or administrator experience or (mostly) programmer experience (“native” Android programs use an API that is completely different from Unix).

**参考链接**: https://unix.stackexchange.com/questions/4091/is-linux-a-unix

> 📎 来源 / Source: https://unix.stackexchange.com/questions/4091/is-linux-a-unix

#### 44. How do I add X days to date and get new date?

**故障现象**: How do I add X days to date and get new date?
**标签 / 来源**: Tags: linux, bash, shell-script, date | unix | 👍 210 | 💬 5 answers

**问题描述**:
Tags: linux, bash, shell-script, date | Score: 210 | Views: 475824 | Answers: 5

**解决方法 / 社区答案**:
You can just use the -d switch and provide a date to be calculated
date
Sun Sep 23 08:19:56 BST 2012
NEW_expration_DATE=$(date -d &quot;+10 days&quot;)
echo $NEW_expration_DATE
Wed Oct 3 08:12:33 BST 2012 


  -d, --date=STRING


          display time described by STRING, not ‘now’

This is quite a powerful tool as you can do things like
date -d &quot;Sun Sep 11 07:59:16 IST 2012+10 days&quot;
Fri Sep 21 03:29:16 BST 2012

or
TZ=IST date -d &quot;Sun Sep 11 07:59:16 IST 2012+10 days&quot;
Fri Sep 21 07:59:16 IST 2012

or
prog_end_date=`date '+%C%y%m%d' -d &quot;$end_date+10 days&quot;`

So if $end_date = 20131001 then $prog_end_date = 20131011.

**参考链接**: https://unix.stackexchange.com/questions/49053/how-do-i-add-x-days-to-date-and-get-new-date

> 📎 来源 / Source: https://unix.stackexchange.com/questions/49053/how-do-i-add-x-days-to-date-and-get-new-date

#### 45. Can I watch the progress of a `sync` operation?

**故障现象**: Can I watch the progress of a `sync` operation?
**标签 / 来源**: Tags: linux, filesystems, io, async | unix | 👍 209 | 💬 8 answers

**问题描述**:
Tags: linux, filesystems, io, async | Score: 209 | Views: 118844 | Answers: 8

**解决方法 / 社区答案**:
Looking at /proc/meminfo will show the Dirty number shrinking over time as all the data spools out; some of it may spill into Writeback as well.  That will be a summary against all devices, but in the cases where one device on the system is much slower than the rest you'll usually end up where everything in that queue is related to it.  You'll probably find the Dirty number large when you start and the sync finishes about the same time it approaches 0.  Try this to get an interactive display:

watch -d grep -e Dirty: -e Writeback: /proc/meminfo


With regular disks I can normally ignore Writeback, but I'm not sure if it's involved more often in the USB transfer path.  If it just bounces up and down without a clear trend to it, you can probably just look at the Dirty number.

**参考链接**: https://unix.stackexchange.com/questions/48235/can-i-watch-the-progress-of-a-sync-operation

> 📎 来源 / Source: https://unix.stackexchange.com/questions/48235/can-i-watch-the-progress-of-a-sync-operation

#### 46. Too many levels of symbolic links

**故障现象**: Too many levels of symbolic links
**标签 / 来源**: Tags: linux, filesystems, ln | unix | 👍 202 | 💬 6 answers

**问题描述**:
Tags: linux, filesystems, ln | Score: 202 | Views: 505511 | Answers: 6

**解决方法 / 社区答案**:
As Dubu points out in a comment, the issue lies in your relative paths. I had a similar problem symlinking my nginx configuration from /usr/local/etc/nginx to /etc/nginx. If you create your symlink like this:
cd /usr/local/etc
ln -s nginx/ /etc/nginx

You will in fact make the link /etc/nginx -&gt; /etc/nginx, because the source path is relative to the link's path. The solution is as simple as using absolute paths:
ln -s /usr/local/etc/nginx /etc/nginx

If you want to use relative paths and have them behave the way you probably expect them to, you can use the $PWD variable to easily add in the path to the current working directory path, like so:
cd /usr/local/etc
ln -s &quot;$PWD/nginx/&quot; /etc/nginx

Make sure that the path is in double quotes, to make sure things like spaces in your current path are escaped. Note that you must use double quotes when doing this, as $PWD will not be substituted if you use single quotes.

**参考链接**: https://unix.stackexchange.com/questions/141436/too-many-levels-of-symbolic-links

> 📎 来源 / Source: https://unix.stackexchange.com/questions/141436/too-many-levels-of-symbolic-links

#### 47. What to do when a Linux desktop freezes?

**故障现象**: What to do when a Linux desktop freezes?
**标签 / 来源**: Tags: linux, desktop, freeze | unix | 👍 202 | 💬 10 answers

**问题描述**:
Tags: linux, desktop, freeze | Score: 202 | Views: 673976 | Answers: 10

**解决方法 / 社区答案**:
If all else fails, you Raise The Elephant.  There are Magic SysRq key sequences (Alt+SysRq+?) that the Linux kernel handles specially.
If your Linux box freezes and simply won't yield to any other key-commands, you should definitely try one particular key sequence before a hard reboot.
The key sequence is popularly remembered with the mnemonic:

Raising Elephants Is So Utterly Boring


Alt+SysRq+R switch keyboard to 'raw' mode
Alt+SysRq+E send SIGTERM (termination) signal to all processes except mother init
Alt+SysRq+I send SIGKILL signal to all processes, a little more aggressive
Alt+SysRq+S sync all filesystems to prevent data loss
Alt+SysRq+U remount filesystems as read-only
Alt+SysRq+B forcefully reboot

For the full list of possible commands and additional tips on how to type these commands, see the Wikipedia page.

**参考链接**: https://unix.stackexchange.com/questions/31818/what-to-do-when-a-linux-desktop-freezes

> 📎 来源 / Source: https://unix.stackexchange.com/questions/31818/what-to-do-when-a-linux-desktop-freezes

#### 48. Recover deleted files on Linux

**故障现象**: Recover deleted files on Linux
**标签 / 来源**: Tags: linux, data-recovery, deleted-files | unix | 👍 202 | 💬 14 answers

**问题描述**:
Tags: linux, data-recovery, deleted-files | Score: 202 | Views: 1208040 | Answers: 14

**解决方法 / 社区答案**:
The link someone provided in the comments is likely your best chance.
Linux debugfs Hack: Undelete Files
That write-up though looking a little intimidating is actually fairly straight forward to follow. In general the steps are as follows:

Use debugfs to view a filesystems log
 $ debugfs -w /dev/mapper/wks01-root


At the debugfs prompt
 debugfs: lsdel


Sample output
 Inode  Owner  Mode    Size    Blocks   Time deleted
 23601299      0 120777      3    1/   1 Tue Mar 13 16:17:30 2012
 7536655      0 120777      3    1/   1 Tue May  1 06:21:22 2012
 2 deleted inodes found.


Run the command in debugfs
 debugfs: logdump -i &lt;7536655&gt;


Determine files inode
 ...
 ...
 ....
 output truncated
     Fast_link_dest: bin
     Blocks:  (0+1): 7235938
   FS block 7536642 logged at sequence 38402086, journal block 26711
     (inode block for inode 7536655):
     Inode: 7536655   Type: symlink        Mode:  0777   Flags: 0x0   Generation: 3532221116
     User:     0   Group:     0   Size: 3
     File ACL: 0    Directory ACL: 0
     Links: 0   Blockcount: 0
     Fragment:  Address: 0    Number: 0    Size: 0
     ctime: 0x4f9fc732 -- Tue May  1 06:21:22 2012
     atime: 0x4f9fc730 -- Tue May  1 06:21:20 2012
     mtime: 0x4f9fc72f -- Tue May  1 06:21:19 2012
     dtime: 0x4f9fc732 -- Tue May  1 06:21:22 2012
     Fast_link_dest: bin
     Blocks:  (0+1): 7235938
 No magic number at block 28053: end of journal.


With the above inode info run the following commands
 # dd if=/dev/mapper/wks01-root of=recovered.file.001 bs=4096 count=1 skip=7235938
 # file recovered.file.001
 file: ASCII text, with very long lines



Files been recovered to recovered.file.001.
Other options
If the above isn't for you I've used tools such as photorec to recover files in the past, but it's geared for image files only. I've written about this method extensively on my blog in this article titled:
How to Recover Corrupt jpeg and mov Files from a Digital Camera's SDD Card on Fedora/CentOS/RHEL.

**参考链接**: https://unix.stackexchange.com/questions/80270/recover-deleted-files-on-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/80270/recover-deleted-files-on-linux

#### 49. Determine the size of a block device

**故障现象**: Determine the size of a block device
**标签 / 来源**: Tags: linux, size | unix | 👍 196 | 💬 21 answers

**问题描述**:
Tags: linux, size | Score: 196 | Views: 336781 | Answers: 21

**解决方法 / 社区答案**:
blockdev --getsize64 /dev/sda returns size in bytes.

blockdev --getsz /dev/sda returns size in 512-byte sectors.

Deprecated: blockdev --getsize /dev/sda returns size in sectors.

blockdev is part of util-linux.

**参考链接**: https://unix.stackexchange.com/questions/52215/determine-the-size-of-a-block-device

> 📎 来源 / Source: https://unix.stackexchange.com/questions/52215/determine-the-size-of-a-block-device

#### 50. Why would someone choose FreeBSD over Linux?

**故障现象**: Why would someone choose FreeBSD over Linux?
**标签 / 来源**: Tags: linux, freebsd, distribution-choice | unix | 👍 194 | 💬 9 answers

**问题描述**:
Tags: linux, freebsd, distribution-choice | Score: 194 | Views: 211667 | Answers: 9

**解决方法 / 社区答案**:
If you want to know what's different so you can use the system more efficiently, here is a commonly referenced introduction to BSD to people coming from a Linux background.

If you want more of the historical context for this decision, I'll just take a guess as to why they chose FreeBSD. Around the time of the first dot-com bubble, FreeBSD 4 was extremely popular with ISPs. This may or may not have been related to the addition of kqueue. The Wikipedia page describes the feelings for FreeBSD 4 thusly: "…widely regarded as one of the most stable and high performance operating systems of the whole Unix lineage." FreeBSD in particular has added other features over time which would appeal to hosting providers, such as jail and ZFS support.

Personally, I really like the BSD systems because they just feel like they fit together better than most Linux distros I've used. Also, the documentation provided directly in the various handbooks, etc. is outstanding. If you're going to be using FreeBSD, I highly recommend the FreeBSD Handbook.

**参考链接**: https://unix.stackexchange.com/questions/14489/why-would-someone-choose-freebsd-over-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/14489/why-would-someone-choose-freebsd-over-linux

#### 51. How can I find the hardware model in Linux?

**故障现象**: How can I find the hardware model in Linux?
**标签 / 来源**: Tags: linux, hardware, system-information, smbios, dmidecode | unix | 👍 191 | 💬 10 answers

**问题描述**:
Tags: linux, hardware, system-information, smbios, dmidecode | Score: 191 | Views: 492416 | Answers: 10

**解决方法 / 社区答案**:
using the dmidecode | grep -A3 '^System Information' command. There you'll find all information from BIOS and hardware. These are examples on three different machines (this is an excerpt of the complete output):

System Information
    Manufacturer: Dell Inc.
    Product Name: Precision M4700

System Information
    Manufacturer: MICRO-STAR INTERANTIONAL CO.,LTD
    Product Name: MS-7368

System Information
    Manufacturer: HP
    Product Name: ProLiant ML330 G6

**参考链接**: https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux

#### 52. Why is my ethernet interface called enp0s10 instead of eth0?

**故障现象**: Why is my ethernet interface called enp0s10 instead of eth0?
**标签 / 来源**: Tags: linux, networking, udev, ethernet | unix | 👍 189 | 💬 5 answers

**问题描述**:
Tags: linux, networking, udev, ethernet | Score: 189 | Views: 292794 | Answers: 5

**解决方法 / 社区答案**:
Answer on &quot;What does enp0s10 means?&quot; question:
enp0s10:
| | |
v | |
en| |   --&gt; ethernet
  v |
  p0|   --&gt; bus number (0)
    v
    s10 --&gt; slot number (10)

Source: udev-builtin-net_id.c on GitHub

**参考链接**: https://unix.stackexchange.com/questions/134483/why-is-my-ethernet-interface-called-enp0s10-instead-of-eth0

> 📎 来源 / Source: https://unix.stackexchange.com/questions/134483/why-is-my-ethernet-interface-called-enp0s10-instead-of-eth0

#### 53. Manually generate password for /etc/shadow

**故障现象**: Manually generate password for /etc/shadow
**标签 / 来源**: Tags: linux, password, shadow | unix | 👍 188 | 💬 10 answers

**问题描述**:
Tags: linux, password, shadow | Score: 188 | Views: 450016 | Answers: 10

**解决方法 / 社区答案**:
You can use following commands for the same:
Method 1 (md5, sha256, sha512)
openssl passwd -6 -salt xyz  yourpass

Note: passing -1 will generate an MD5 password, -5 a SHA256 and -6 SHA512 (recommended)
Method 2 (md5, sha256, sha512)
mkpasswd --method=SHA-512 --stdin

The option --method accepts md5, sha-256 and sha-512
Method 3 (des, md5, sha256, sha512)
As @tink suggested, we can update the password using chpasswd using:
echo &quot;username:password&quot; | chpasswd 

Or you can use the encrypted password with chpasswd. First generate it using this:
perl -e 'print crypt(&quot;YourPasswd&quot;, &quot;salt&quot;, &quot;sha512&quot;),&quot;\n&quot;'

Then later you can use the generated password to update /etc/shadow:
echo &quot;username:encryptedPassWd&quot; | chpasswd -e

The encrypted password we can also use to create a new user with this password, for example:
useradd -p 'encryptedPassWd'  username

**参考链接**: https://unix.stackexchange.com/questions/81240/manually-generate-password-for-etc-shadow

> 📎 来源 / Source: https://unix.stackexchange.com/questions/81240/manually-generate-password-for-etc-shadow

#### 54. Linux: Difference between /dev/console, /dev/tty and /dev/tty0

**故障现象**: Linux: Difference between /dev/console, /dev/tty and /dev/tty0
**标签 / 来源**: Tags: linux, tty, console | unix | 👍 187 | 💬 3 answers

**问题描述**:
Tags: linux, tty, console | Score: 187 | Views: 204991 | Answers: 3

**解决方法 / 社区答案**:
From the Linux Kernel documentation on Kernel.org:
/dev/tty        Current TTY device
/dev/console    System console
/dev/tty0       Current virtual console

In the good old days /dev/console was System Administrator console. And TTYs were users' serial devices attached to a server.
Now /dev/console and /dev/tty0 represent current display and usually are the same. You can override it for example by adding console=ttyS0 to grub.conf. After that your /dev/tty0 is a monitor and /dev/console is /dev/ttyS0.
An exercise to show the difference between /dev/tty and /dev/tty0:
Switch to the 2nd console by pressing Ctrl+Alt+F2. Login as root. Type sleep 5; echo tty0 &gt; /dev/tty0. Press Enter and switch to the 3rd console by pressing Alt+F3.
Now switch back to the 2nd console by pressing Alt+F2. Type sleep 5; echo tty &gt; /dev/tty, press Enter and switch to the 3rd console.
You can see that tty is the console where process starts, and tty0 is a always current console.

**参考链接**: https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0

> 📎 来源 / Source: https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0

#### 55. Timezone setting in Linux

**故障现象**: Timezone setting in Linux
**标签 / 来源**: Tags: linux, date, time, timezone | unix | 👍 184 | 💬 3 answers

**问题描述**:
Tags: linux, date, time, timezone | Score: 184 | Views: 717820 | Answers: 3

**解决方法 / 社区答案**:
Take a look at this blog post titled: How To: 2 Methods To Change TimeZone in Linux.

Red Hat distros

If you're using a distribution such as Red Hat then your approach of copying the file would be mostly acceptable.

NOTE: If you're looking for a distro-agnostic solution, this also works on Debian, though there are simpler approaches below if you only need to be concerned with Debian machines.

$ ls /usr/share/zoneinfo/
Africa/      CET          Etc/         Hongkong     Kwajalein    Pacific/     ROK          zone.tab
America/     Chile/       Europe/      HST          Libya        Poland       Singapore    Zulu
Antarctica/  CST6CDT      GB           Iceland      MET          Portugal     Turkey       
Arctic/      Cuba         GB-Eire      Indian/      Mexico/      posix/       UCT          
Asia/        EET          GMT          Iran         MST          posixrules   Universal    
Atlantic/    Egypt        GMT0         iso3166.tab  MST7MDT      PRC          US/          
Australia/   Eire         GMT-0        Israel       Navajo       PST8PDT      UTC          
Brazil/      EST          GMT+0        Jamaica      NZ           right/       WET          
Canada/      EST5EDT      Greenwich    Japan        NZ-CHAT      ROC          W-SU         


I would recommend linking to it rather than copying however.

$ sudo unlink /etc/localtime 
$ sudo ln -s /usr/share/zoneinfo/Etc/GMT+6 /etc/localtime


Now date shows the different timezone:

$ date -u
Thu Jan 23 05:40:31 UTC 2014

$ date 
Wed Jan 22 23:40:38 GMT+6 2014


Ubuntu/Debian Distros

To change the timezone on either of these distros you can use this command:

$ sudo dpkg-reconfigure tzdata


&nbsp;&nbsp;&nbsp;&nbsp;

$ sudo dpkg-reconfigure tzdata

Current default time zone: 'Etc/GMT-6'
Local time is now:      Thu Jan 23 11:52:16 GMT-6 2014.
Universal Time is now:  Thu Jan 23 05:52:16 UTC 2014.


Now when we check it out:

$ date -u
Thu Jan 23 05:53:32 UTC 2014

$ date 
Thu Jan 23 11:53:33 GMT-6 2014


NOTE: There's also this option in Ubuntu 14.04 and higher with a single command (source: Ask Ubuntu - setting timezone from terminal):

$ sudo timedatectl set-timezone Etc/GMT-6


On the use of "Etc/GMT+6"

excerpt from @MattJohnson's answer on SO


  Zones like Etc/GMT+6 are intentionally reversed for backwards compatibility with POSIX standards.  See the comments in this file.
  
  You should almost never need to use these zones.  Instead you should be using a fully named time zone like America/New_York or Europe/London or whatever is appropriate for your location.  Refer to the list here.

**参考链接**: https://unix.stackexchange.com/questions/110522/timezone-setting-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/110522/timezone-setting-in-linux

#### 56. Mount cifs Network Drive: write permissions and chown

**故障现象**: Mount cifs Network Drive: write permissions and chown
**标签 / 来源**: Tags: linux, permissions, mount, chown, cifs | unix | 👍 184 | 💬 3 answers

**问题描述**:
Tags: linux, permissions, mount, chown, cifs | Score: 184 | Views: 550029 | Answers: 3

**解决方法 / 社区答案**:
You are mounting the CIFS share as root (because you used sudo), so you cannot write as normal user. If your Linux Distribution and its kernel are recent enough that you could mount the network share as a normal user (but under a folder that the user own), you will have the proper credentials to write file (e.g. mount the shared folder somewhere under your home directory, like for instance $HOME/netshare/. Obviously, you would need to create the folder before mounting it).

An alternative is to specify the user and group ID that the mounted network share should used, this would allow that particular user and potentially group to write to the share. Add the following options to your mount: uid=&lt;user&gt;,gid=&lt;group&gt; and replace &lt;user&gt; and &lt;group&gt; respectively by your own user and default group, which you can find automatically with the id command.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g) //server-address/folder /mount/path/on/ubuntu


If the server is sending ownership information, you may need to add the forceuid and forcegid options.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g),forceuid,forcegid, //server-address/folder /mount/path/on/ubuntu

**参考链接**: https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

> 📎 来源 / Source: https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

#### 57. Trying to SSH to local VM Ubuntu with Putty

**故障现象**: Trying to SSH to local VM Ubuntu with Putty
**标签 / 来源**: Tags: ubuntu, virtualbox, putty | unix | 👍 183 | 💬 6 answers

**问题描述**:
Tags: ubuntu, virtualbox, putty | Score: 183 | Views: 600105 | Answers: 6

**解决方法 / 社区答案**:
VirtualBox will create a private network (10.0.2.x) which will be connected to your host network using NAT. (Unless configured otherwise.)

This means that you cannot directly access any host of the private network from the host network. To do so, you need some port forwarding. In the network preferences of your VM you can, for example, configure VirtualBox to open port 22 on 127.0.1.1 (a loopback address of your host) and forward any traffic to port 22 of 10.0.2.1 (the internal address of your VM)

This way, you can point putty to Port 22 of 127.0.1.1 and VirtualBox will redirect this connection to your VM where its ssh daemon will answer it, allowing you to log in.

**参考链接**: https://unix.stackexchange.com/questions/145997/trying-to-ssh-to-local-vm-ubuntu-with-putty

> 📎 来源 / Source: https://unix.stackexchange.com/questions/145997/trying-to-ssh-to-local-vm-ubuntu-with-putty

#### 58. Sorting down processes by memory usage

**故障现象**: Sorting down processes by memory usage
**标签 / 来源**: Tags: linux, memory | unix | 👍 182 | 💬 9 answers

**问题描述**:
Tags: linux, memory | Score: 182 | Views: 494008 | Answers: 9

**解决方法 / 社区答案**:
Use the following command:

ps aux --sort -rss


Check here for more Linux process memory usage

**参考链接**: https://unix.stackexchange.com/questions/92493/sorting-down-processes-by-memory-usage

> 📎 来源 / Source: https://unix.stackexchange.com/questions/92493/sorting-down-processes-by-memory-usage

#### 59. How to sync two folders with command line tools?

**故障现象**: How to sync two folders with command line tools?
**标签 / 来源**: Tags: linux, files, file-copy, synchronization | unix | 👍 182 | 💬 9 answers

**问题描述**:
Tags: linux, files, file-copy, synchronization | Score: 182 | Views: 338370 | Answers: 9

**解决方法 / 社区答案**:
This puts folder A into folder B:
rsync -avu --delete &quot;/home/user/A&quot; &quot;/home/user/B&quot;

If you want the contents of folders A and B to be the same, put /home/user/A/ (with the slash) as the source. This takes not the folder A but all of its content and puts it into folder B. Like this:
rsync -avu --delete &quot;/home/user/A/&quot; &quot;/home/user/B&quot;


-a archive mode; equals -rlptgoD (no -H, -A, -X)
-v run verbosely
-u only copy files with a newer modification time (or size difference if the times are equal)
--delete delete the files in target folder that do not exist in the source

Manpage: https://download.samba.org/pub/rsync/rsync.html

**参考链接**: https://unix.stackexchange.com/questions/203846/how-to-sync-two-folders-with-command-line-tools

> 📎 来源 / Source: https://unix.stackexchange.com/questions/203846/how-to-sync-two-folders-with-command-line-tools

#### 60. How to move all files and folders via mv command

**故障现象**: How to move all files and folders via mv command
**标签 / 来源**: Tags: linux, command, rename | unix | 👍 182 | 💬 7 answers

**问题描述**:
Tags: linux, command, rename | Score: 182 | Views: 876725 | Answers: 7

**解决方法 / 社区答案**:
Try with this:

mv /path/sourcefolder/* /path/destinationfolder/

**参考链接**: https://unix.stackexchange.com/questions/50487/how-to-move-all-files-and-folders-via-mv-command

> 📎 来源 / Source: https://unix.stackexchange.com/questions/50487/how-to-move-all-files-and-folders-via-mv-command

#### 61. How to change ownership of symbolic links?

**故障现象**: How to change ownership of symbolic links?
**标签 / 来源**: Tags: linux, permissions, rhel, symlink, ln | unix | 👍 179 | 💬 3 answers

**问题描述**:
Tags: linux, permissions, rhel, symlink, ln | Score: 179 | Views: 251905 | Answers: 3

**解决方法 / 社区答案**:
On a Linux system, when changing the ownership of a symbolic link using chown, by default it changes the target of the symbolic link (ie, whatever the symbolic link is pointing to).

If you'd like to change ownership of the link itself, you need to use the -h option to chown:


  -h, --no-dereference
  affect  each  symbolic  link  instead of any referenced file (useful only on systems that can change the ownership of a symlink)


For example:

$ touch test
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
$ sudo ln -s test test1
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test
$ sudo chown root:root test1
$ ls -l test*
-rw-r--r-- 1 root root 0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test


Note that the target of the link is now owned by root.

$ sudo chown mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test


And again, the link test1 is still owned by root, even though test has changed.

$ sudo chown -h mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj mj 0 Jul 27 08:47 test
lrwxrwxrwx 1 mj mj 4 Jul 27 08:47 test1 -&gt; test


And finally we change the ownership of the link using the -h option.

**参考链接**: https://unix.stackexchange.com/questions/218557/how-to-change-ownership-of-symbolic-links

> 📎 来源 / Source: https://unix.stackexchange.com/questions/218557/how-to-change-ownership-of-symbolic-links

#### 62. How do I read from /proc/$pid/mem under Linux?

**故障现象**: How do I read from /proc/$pid/mem under Linux?
**标签 / 来源**: Tags: linux, kernel, process, memory, proc | unix | 👍 176 | 💬 6 answers

**问题描述**:
Tags: linux, kernel, process, memory, proc | Score: 176 | Views: 190951 | Answers: 6

**解决方法 / 社区答案**:
/proc/$pid/maps
/proc/$pid/mem shows the contents of $pid's memory mapped the same way as in the process, i.e., the byte at offset x in the pseudo-file is the same as the byte at address x in the process. If an address is unmapped in the process, reading from the corresponding offset in the file returns EIO (Input/output error). For example, since the first page in a process is never mapped (so that dereferencing a NULL pointer fails cleanly rather than unintendedly accessing actual memory), reading the first byte of /proc/$pid/mem always yield an I/O error.
The way to find out what parts of the process memory are mapped is to read /proc/$pid/maps. This file contains one line per mapped region, looking like this:
08048000-08054000 r-xp 00000000 08:01 828061     /bin/cat
08c9b000-08cbc000 rw-p 00000000 00:00 0          [heap]

The first two numbers are the boundaries of the region (addresses of the first byte and the byte after last, in hexa). The next column contain the permissions, then there's some information about the file (offset, device, inode and name) if this is a file mapping. See the proc(5) man page or Understanding Linux /proc/id/maps for more information.
Here's a proof-of-concept script that dumps the contents of its own memory.
#! /usr/bin/env python
import re
maps_file = open(&quot;/proc/self/maps&quot;, 'r')
mem_file = open(&quot;/proc/self/mem&quot;, 'rb', 0)
output_file = open(&quot;self.dump&quot;, 'wb')
for line in maps_file.readlines():  # for each mapped region
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    if m.group(3) == 'r':  # if this is a readable region
        start = int(m.group(1), 16)
        end = int(m.group(2), 16)
        mem_file.seek(start)  # seek to region start
        chunk = mem_file.read(end - start)  # read region contents
        output_file.write(chunk)  # dump contents to standard output
maps_file.close()
mem_file.close()
output_file.close()


/proc/$pid/mem
[The following is for historical interest. It does not apply to current kernels.]
Since version 3.3 of the kernel, you can access /proc/$pid/mem normally as long as you access only access it at mapped offsets and you have permission to trace it (same permissions as ptrace for read-only access). But in older kernels, there were some additional complications.
If you try to read from the mem pseudo-file of another process, it doesn't work: you get an ESRCH (No such process) error.
The permissions on /proc/$pid/mem (r--------) are more liberal than what should be the case. For example, you shouldn't be able to read a setuid process's memory. Furthermore, trying to read a process's memory while the process is modifying it could give the reader an inconsistent view of the memory, and worse, there were race conditions that could trace older versions of the Linux kernel (according to this lkml thread, though I don't know the details). So additional checks are needed:

The process that wants to read from /proc/$pid/mem must attach to the process using ptrace with the PTRACE_ATTACH flag. This is what debuggers do when they start debugging a process; it's also what strace does to a process's system calls. Once the reader has finished reading from /proc/$pid/mem, it should detach by calling ptrace with the PTRACE_DETACH flag.
The observed process must not be running. Normally calling ptrace(PTRACE_ATTACH, …) will stop the target process (it sends a STOP signal), but there is a race condition (signal delivery is asynchronous), so the tracer should call wait (as documented in ptrace(2)).

A process running as root can read any process's memory, without needing to call ptrace, but the observed process must be stopped, or the read will still return ESRCH.
In the Linux kernel source, the code providing per-process entries in /proc is in fs/proc/base.c, and the function to read from /proc/$pid/mem is mem_read. The additional check is performed by check_mem_permission.
Here's some sample C code to attach to a process and read a chunk its of mem file (error checking omitted):
sprintf(mem_file_name, &quot;/proc/%d/mem&quot;, pid);
mem_fd = open(mem_file_name, O_RDONLY);
ptrace(PTRACE_ATTACH, pid, NULL, NULL);
waitpid(pid, NULL, 0);
lseek(mem_fd, offset, SEEK_SET);
read(mem_fd, buf, _SC_PAGE_SIZE);
ptrace(PTRACE_DETACH, pid, NULL, NULL);

I've already posted a proof-of-concept script for dumping /proc/$pid/mem on another thread.

**参考链接**: https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

#### 63. Zip everything in current directory

**故障现象**: Zip everything in current directory
**标签 / 来源**: Tags: ubuntu, packaging, compression, zip | unix | 👍 176 | 💬 2 answers

**问题描述**:
Tags: ubuntu, packaging, compression, zip | Score: 176 | Views: 300258 | Answers: 2

**解决方法 / 社区答案**:
Install zip and use

zip -r foo.zip .


You can use the flags -0 (none) to -9 (best) to change compressionrate

Excluding files can be done via the -x flag. From the man-page:

-x files
--exclude files
          Explicitly exclude the specified files, as in:

                 zip -r foo foo -x \*.o

          which  will  include the contents of foo in foo.zip while excluding all the files that end in .o.  The backslash avoids the shell filename substitution, so that the name matching
          is performed by zip at all directory levels.

          Also possible:

                 zip -r foo foo -x@exclude.lst

          which will include the contents of foo in foo.zip while excluding all the files that match the patterns in the file exclude.lst.

          The long option forms of the above are

                 zip -r foo foo --exclude \*.o

          and

                 zip -r foo foo --exclude @exclude.lst

          Multiple patterns can be specified, as in:

                 zip -r foo foo -x \*.o \*.c

          If there is no space between -x and the pattern, just one value is assumed (no list):

                 zip -r foo foo -x\*.o

          See -i for more on include and exclude.

**参考链接**: https://unix.stackexchange.com/questions/27362/zip-everything-in-current-directory

> 📎 来源 / Source: https://unix.stackexchange.com/questions/27362/zip-everything-in-current-directory

#### 64. Get the chmod numerical value for a file

**故障现象**: Get the chmod numerical value for a file
**标签 / 来源**: Tags: linux, freebsd, chmod | unix | 👍 172 | 💬 4 answers

**问题描述**:
Tags: linux, freebsd, chmod | Score: 172 | Views: 269466 | Answers: 4

**解决方法 / 社区答案**:
You can get the value directly using a stat output format, e.g.
Linux:
stat --format '%a' &lt;file&gt;

BSD/OS X:
stat -f &quot;%OLp&quot; &lt;file&gt;

Busybox:
 stat -c '%a' &lt;file&gt;

**参考链接**: https://unix.stackexchange.com/questions/46915/get-the-chmod-numerical-value-for-a-file

> 📎 来源 / Source: https://unix.stackexchange.com/questions/46915/get-the-chmod-numerical-value-for-a-file

#### 65. What are pseudo terminals (pty/tty)?

**故障现象**: What are pseudo terminals (pty/tty)?
**标签 / 来源**: Tags: linux, terminal, pty | unix | 👍 172 | 💬 3 answers

**问题描述**:
Tags: linux, terminal, pty | Score: 172 | Views: 129984 | Answers: 3

**解决方法 / 社区答案**:
What is a pseudo terminal? (tty/pty)

A device that has the functions of a physical terminal without actually being one. Created by terminal emulators such as xterm. More detail is in the manpage pty(7).

Why do we need them? How they got introduced and what was the need for it?

Traditionally, UNIX has a concept of a controlling terminal for a group of processes, and many I/O functions are built with terminals in mind. Pseudoterminals handle, for example, some control characters like ^C.

Are they outdated? Do we not need them anymore? Is there anything that replaced them?

They are not outdated and are used in many programs, including ssh.

Any useful use-case?

ssh.

**参考链接**: https://unix.stackexchange.com/questions/21147/what-are-pseudo-terminals-pty-tty

> 📎 来源 / Source: https://unix.stackexchange.com/questions/21147/what-are-pseudo-terminals-pty-tty

#### 66. How to make log-rotate change take effect

**故障现象**: How to make log-rotate change take effect
**标签 / 来源**: Tags: linux, syslog, logrotate | unix | 👍 169 | 💬 4 answers

**问题描述**:
Tags: linux, syslog, logrotate | Score: 169 | Views: 400685 | Answers: 4

**解决方法 / 社区答案**:
logrotate uses crontab to work. It's scheduled work, not a daemon, so no need to reload its configuration.
When the crontab executes logrotate, it will use your new config file automatically.
If you need to test your config you can also execute logrotate on your own  with the command:
logrotate /etc/logrotate.d/your-logrotate-config

If you want to have a debug output use argument  -d
logrotate -d /etc/logrotate.d/your-logrotate-config

You may need to be root or a specific user to run this command.
Or as mentioned in comments, identify the logrotate line in the output of the command crontab -l and execute the command line refer to slm's answer to have a precise cron.daily explanation

**参考链接**: https://unix.stackexchange.com/questions/116136/how-to-make-log-rotate-change-take-effect

> 📎 来源 / Source: https://unix.stackexchange.com/questions/116136/how-to-make-log-rotate-change-take-effect

#### 67. How do I attach a terminal to a detached process?

**故障现象**: How do I attach a terminal to a detached process?
**标签 / 来源**: Tags: linux, shell, command-line, terminal, process | unix | 👍 167 | 💬 5 answers

**问题描述**:
Tags: linux, shell, command-line, terminal, process | Score: 167 | Views: 300559 | Answers: 5

**解决方法 / 社区答案**:
Yes, it is. First, create a pipe:
mkfifo /tmp/fifo.
 Use gdb to attach to the process:
gdb -p PID

Then close stdin: call close (0); and open it again: call open ("/tmp/fifo", 0600)

Finally, write away (from a different terminal, as gdb will probably hang):

echo blah &gt; /tmp/fifo

**参考链接**: https://unix.stackexchange.com/questions/31824/how-do-i-attach-a-terminal-to-a-detached-process

> 📎 来源 / Source: https://unix.stackexchange.com/questions/31824/how-do-i-attach-a-terminal-to-a-detached-process

#### 68. Can I configure my Linux system for more aggressive file system caching?

**故障现象**: Can I configure my Linux system for more aggressive file system caching?
**标签 / 来源**: Tags: linux, filesystems, performance, fstab, sysctl | unix | 👍 167 | 💬 7 answers

**问题描述**:
Tags: linux, filesystems, performance, fstab, sysctl | Score: 167 | Views: 171822 | Answers: 7

**解决方法 / 社区答案**:
Improving disk cache performance in general is more than just increasing the file system cache size unless your whole system fits in RAM in which case you should use RAM drive (tmpfs is good because it allows falling back to disk if you need the RAM in some case) for runtime storage (and perhaps an initrd script to copy system from storage to RAM drive at startup).
You didn't tell if your storage device is SSD or HDD. Here's what I've found to work for me (in my case sda is a HDD mounted at /home and sdb is SSD mounted at /).
First optimize the load-stuff-from-storage-to-cache part:
Here is my setup for HDD (make sure AHCI+NCQ is enabled in BIOS if you have toggles):
    echo cfq &gt; /sys/block/sda/queue/scheduler
    echo 10000 &gt; /sys/block/sda/queue/iosched/fifo_expire_async
    echo 250 &gt; /sys/block/sda/queue/iosched/fifo_expire_sync
    echo 80 &gt; /sys/block/sda/queue/iosched/slice_async
    echo 1 &gt; /sys/block/sda/queue/iosched/low_latency
    echo 6 &gt; /sys/block/sda/queue/iosched/quantum
    echo 5 &gt; /sys/block/sda/queue/iosched/slice_async_rq
    echo 3 &gt; /sys/block/sda/queue/iosched/slice_idle
    echo 100 &gt; /sys/block/sda/queue/iosched/slice_sync
    hdparm -q -M 254 /dev/sda

Worth noting for the HDD case is high fifo_expire_async (usually write) and long slice_sync to allow a single process to get high throughput (set slice_sync to lower number if you hit situations where multiple processes are waiting for some data from the disk in parallel). The slice_idle is always a compromise for HDDs but setting it somewhere in range 3-20 should be okay depending on disk usage and disk firmware. I prefer to target for low values but setting it too low will destroy your throughput. The quantum setting seems to affect throughput a lot but try to keep this as low as possible to keep latency on sensible level. Setting quantum too low will destroy throughput. Values in range 3-8 seem to work well with HDDs. The worst case latency for a read is (quantum * slice_sync) + (slice_async_rq * slice_async) ms if I've understood the kernel behavior correctly. The async is mostly used by writes and since you're willing to delay writing to disk, set both slice_async_rq and slice_async to very low numbers. However, setting slice_async_rq too low value may stall reads because writes cannot be delayed after reads any more. My config will try to write data to disk at most after 10 seconds after data has been passed to kernel but since you can tolerate loss of data on power loss also set fifo_expire_async to 3600000 to tell that 1 hour is okay for the delay to disk. Just keep the slice_async low, though, because otherwise you can get high read latency.
The hdparm command is required to prevent AAM from killing much of the performance that AHCI+NCQ allows. If your disk makes too much noise, then skip this.
Here is my setup for SSD (Intel 320 series):
    echo cfq &gt; /sys/block/sdb/queue/scheduler
    echo 1 &gt; /sys/block/sdb/queue/iosched/back_seek_penalty
    echo 10000 &gt; /sys/block/sdb/queue/iosched/fifo_expire_async
    echo 20 &gt; /sys/block/sdb/queue/iosched/fifo_expire_sync
    echo 1 &gt; /sys/block/sdb/queue/iosched/low_latency
    echo 6 &gt; /sys/block/sdb/queue/iosched/quantum
    echo 2 &gt; /sys/block/sdb/queue/iosched/slice_async
    echo 10 &gt; /sys/block/sdb/queue/iosched/slice_async_rq
    echo 1 &gt; /sys/block/sdb/queue/iosched/slice_idle
    echo 20 &gt; /sys/block/sdb/queue/iosched/slice_sync

Here it's worth noting the low values for different slice settings. The most important setting for an SSD is slice_idle which must be set to 0-1. Setting it to zero moves all ordering decisions to native NCQ while setting it to 1 allows kernel to order requests (but if the NCQ is active, the hardware may override kernel ordering partially). Test both values to see if you can see the difference. For Intel 320 series, it seems that setting slide_idle to 0 gives the best throughput but setting it to 1 gives best (lowest) overall latency. If you have recent enough kernel, you can use slide_idle_us to set the value in microseconds instead of milliseconds and you could use something like echo 14 &gt; slice_idle_us instead. Suitable value seems to be close to 700000 divided by max practical IOPS your storage device can support so 14 is okay for pretty fast SSD devices.
For more information about these tunables, see https://www.kernel.org/doc/Documentation/block/cfq-iosched.txt .
Update in year 2020 and kernel version 5.3 (cfq is dead):
#!/bin/bash
modprobe bfq
for d in /sys/block/sd?; do
  # HDD (tuned for Seagate SMR drive)
  echo bfq &gt;&quot;$d/queue/scheduler&quot;
  echo 4 &gt;&quot;$d/queue/nr_requests&quot;
  echo 32000 &gt;&quot;$d/queue/iosched/back_seek_max&quot;
  echo 3 &gt;&quot;$d/queue/iosched/back_seek_penalty&quot;
  echo 80 &gt;&quot;$d/queue/iosched/fifo_expire_sync&quot;
  echo 1000 &gt;&quot;$d/queue/iosched/fifo_expire_async&quot;
  echo 5300 &gt;&quot;$d/queue/iosched/slice_idle_us&quot;
  echo 1 &gt;&quot;$d/queue/iosched/low_latency&quot;
  echo 200 &gt;&quot;$d/queue/iosched/timeout_sync&quot;
  echo 0 &gt;&quot;$d/queue/iosched/max_budget&quot;
  echo 1 &gt;&quot;$d/queue/iosched/strict_guarantees&quot;

  # additional tweaks for SSD (tuned for Samsung EVO 850):
  if test $(cat &quot;$d/queue/rotational&quot;) = &quot;0&quot;; then
    echo 36 &gt;&quot;$d/queue/nr_requests&quot;
    echo 1 &gt;&quot;$d/queue/iosched/back_seek_penalty&quot;
    # slice_idle_us should be ~ 0.7/IOPS in µs
    echo 16 &gt;&quot;$d/queue/iosched/slice_idle_us&quot;
    echo 10 &gt;&quot;$d/queue/iosched/fifo_expire_sync&quot;
    echo 250 &gt;&quot;$d/queue/iosched/fifo_expire_async&quot;
    echo 10 &gt;&quot;$d/queue/iosched/timeout_sync&quot;
    echo 0 &gt;&quot;$d/queue/iosched/strict_guarantees&quot;
  fi
done

The setup is pretty similar but I now use bfq instead of cfq because the latter is not available with modern kernels. I try to keep nr_requests as low as possible to allow bfq to control the scheduling more accurately. At least Samsung SSD drives seem to require a pretty deep queue to be able to run with high IOPS. Update: Many Samsung SSDs have a firmware bug and can hang the whole device if nr_requests is too high and OS submits lots of requests rapidly. I've seen random freeze about once every 2 months if I use high nr_requests (e.g. 32 or 36), but the value 6 has been stable this far. The official fix is to set it to 1 but it hurts the performance a lot! For more details, see https://bugzilla.kernel.org/show_bug.cgi?id=203475 and https://bugzilla.kernel.org/show_bug.cgi?id=201693 – basically, if you have a Samsung SSD device and see failed command: WRITE FPDMA QUEUED in the kernel log, you've been bitten by this bug.
If you have latest SSD firmware installed and still get hangs, try kernel flag libata.force=3.0Gbps. Surprisingly many motherboard SATA chipsets are not stable at 6 Gbps line speeds but are totally stable with 3 Gbps line speeds.
I'm using Ubuntu 18.04 with kernel package linux-lowlatency-hwe-18.04-edge which has bfq only as a module so I need to load it before being able to switch to it.
I also nowadays also use zram but I only use 5% of RAM for zram. This allows Linux kernel to use swapping related logic without touching the disks. However, if you decide to go with zero disk swap, make sure your apps do not leak RAM or you're wasting money.
Now that we have configured kernel to load stuff from disk to cache with sensible performance, it's time to adjust the cache behavior:
According to benchmarks I've done, I wouldn't bother setting read ahead via blockdev at all. Kernel default settings are fine.
Set system to prefer swapping file data over application code (this does not matter if you have enough RAM to keep whole filesystem and all the application code and all virtual memory allocated by applications in RAM). This reduces latency for swapping between different applications over latency for accessing big files from a single application:
echo 15 &gt; /proc/sys/vm/swappiness

If you prefer to keep applications nearly always in RAM you could set this to 1. If you set this to zero, kernel will not swap at all unless absolutely necessary to avoid OOM. If you were memory limited and working with big files (e.g. HD video editing), then it might make sense to set this close to 100.
I nowadays (2017) prefer to have no swap at all if you have enough RAM. Having no swap will usually lose 200-1000 MB of RAM on long running desktop machine. I'm willing to sacrifice that much to avoid worst case scenario latency (swapping application code in when RAM is full). In practice, this means that I prefer OOM Killer to swapping. If you allow/need swapping, you might want to increase /proc/sys/vm/watermark_scale_factor, too, to avoid some latency. I would suggest values between 100 and 500. You can consider this setting as trading CPU usage for lower swap latency. The default is 10 and the maximum possible is 1000. Higher value should (according to kernel documentation) result in higher CPU usage for kswapd processes and lower overall swapping latency.
Next, tell kernel to prefer keeping directory hierarchy in memory over file contents and the rest of the page cache in case some RAM needs to be freed (again, if everything fits in RAM, this setting does nothing):
echo 10 &gt; /proc/sys/vm/vfs_cache_pressure # kernel 5.3 or older

echo 120 &gt; /proc/sys/vm/vfs_cache_pressure # kernel 5.4 or newer

Setting vfs_cache_pressure to a low value makes sense because in most cases, the kernel needs to know the directory structure and other filesystem metadata before it can use file contents from the cache and flushing the directory cache too soon will make the file cache next to worthless. However, page cache contains also other data but just the file contents so this setting should be considered like the overall importance of metadata caching vs rest of the system. Consider going all the way down to 1 with this setting if you have lots of small files (my system has around 150K 10 megapixel photos and counts as a &quot;lots of small files&quot; system).
Never set it to zero or the directory structure is always kept in memory even if the system runs out of memory.
Setting this to a big value is sensible only if you have only a few big files that are constantly being re-read (again, HD video editing without enough RAM would be an example case). Official kernel documentation says that &quot;increasing vfs_cache_pressure significantly beyond 100 may have negative performance impact&quot;.
Year 2021 update: After running with kernel version 5.4 for long enough, I've come to the conclusion that the very low vfs_cache_pressure setting (I used to run with 1 for years) may now be causing long stalls / bad latency when memory pressure gets high enough. However, I never noticed such behavior with kernel version 5.3 or lesser.
Year 2022 update: I've been running kernel 5.4.x series for another year and I've come to the conclusion that vfs_cache_pressure has changed permanently. The kernel memory manager behavior that I used to get with kernel version 5.3 or older with values in range 1..5 seems to match real world behavior with 5.4 values in range 100..120. The newer kernels make this adjustment matter more so I'd recommend the value vfs_cache_pressure=120 nowadays for low latency overall. Kernel version 5.3 or older should use a very low but non-zero value here in my opinion.
Exception: if you have a truly massive amount of files and directories and you rarely touch/read/list all files setting vfs_cache_pressure higher than 100 may be wise. This only applies if you do not have enough RAM and cannot keep the whole directory structure in RAM and still have enough RAM for normal file cache and processes (e.g. company wide file server with lots of archival content). If you feel that you need to increase vfs_cache_pressure way above 100 you're running without enough RAM (I have 64 GB RAM on my workstation and 120 seems to be a good setting for minimum latency overall). Increasing vfs_cache_pressure may help a bit but the only real fix is to get more RAM. Having vfs_cache_pressure set to high number sacrifices average performance for having a more stable performance overall (that is, you can avoid really bad worst case behavior but have to deal with worse overall performance).
Finally, tell the kernel to use up to 99% of the RAM as cache for writes and instruct kernel to use up to 50% of RAM before slowing down the process that's writing (default for dirty_background_ratio is 10). Warning: I personally would not do this but you claimed to have enough RAM and are willing to lose the data.
echo 99 &gt; /proc/sys/vm/dirty_ratio
echo 50 &gt; /proc/sys/vm/dirty_background_ratio

And tell that 1h write delay is ok to even start writing stuff on the disk (again, I would not do this):
echo 360000 &gt; /proc/sys/vm/dirty_expire_centisecs
echo 360000 &gt; /proc/sys/vm/dirty_writeback_centisecs

For more information about these tunables, see https://www.kernel.org/doc/Documentation/sysctl/vm.txt
If you put all of those to /etc/rc.local and include following at the end, everything will be in cache as soon as possible after boot (only do this if your filesystem really fits in the RAM):
(nice find / -type f -and -not -path '/sys/*' -and -not -path '/proc/*' -print0 2&gt;/dev/null | nice ionice -c 3 wc -l --files0-from - &gt; /dev/null)&amp;

Or a bit simpler alternative which might work better (cache only /home and /usr, only do this if your /home and /usr really fit in RAM):
(nice find /home /usr -type f -print0 | nice ionice -c 3 wc -l --files0-from - &gt; /dev/null)&amp;

**参考链接**: https://unix.stackexchange.com/questions/30286/can-i-configure-my-linux-system-for-more-aggressive-file-system-caching

> 📎 来源 / Source: https://unix.stackexchange.com/questions/30286/can-i-configure-my-linux-system-for-more-aggressive-file-system-caching

#### 69. What is this folder /run/user/1000?

**故障现象**: What is this folder /run/user/1000?
**标签 / 来源**: Tags: linux, fedora, filesystems, directory-structure | unix | 👍 167 | 💬 2 answers

**问题描述**:
Tags: linux, fedora, filesystems, directory-structure | Score: 167 | Views: 195386 | Answers: 2

**解决方法 / 社区答案**:
/run/user/$uid is created by pam_systemd and used for storing files used by running processes for that user. These might be things such as your keyring daemon, pulseaudio, etc.

Prior to systemd, these applications typically stored their files in /tmp. They couldn't use a location in /home/$user as home directories are often mounted over network filesystems, and these files should not be shared among hosts. /tmp was the only location specified by the FHS which is local, and writable by all users.

However storing all these files in /tmp is problematic as /tmp is writable by everyone, and while you can change the ownership &amp; mode on the files being created, it's more difficult to work with.

So systemd came along and created /run/user/$uid. This directory is local to the system and only accessible by the target user. So applications looking to store their files locally no longer have to worry about access control.
It also keeps things nice and organized. When a user logs out, and no active sessions remain, pam_systemd will wipe the /run/user/$uid directory out. With various files scattered around /tmp, you couldn't do this.

**参考链接**: https://unix.stackexchange.com/questions/162900/what-is-this-folder-run-user-1000

> 📎 来源 / Source: https://unix.stackexchange.com/questions/162900/what-is-this-folder-run-user-1000

#### 70. How is Mono magical?

**故障现象**: How is Mono magical?
**标签 / 来源**: Tags: linux, executable, cross-compilation, mono | unix | 👍 165 | 💬 1 answers

**问题描述**:
Tags: linux, executable, cross-compilation, mono | Score: 165 | Views: 11848 | Answers: 1

**解决方法 / 社区答案**:
This is binfmt_misc in action: it allows the kernel to be told how to run binaries it doesn't know about. Look at the contents of /proc/sys/fs/binfmt_misc; among the files you see there, one should explain how to run Mono binaries:

enabled
interpreter /usr/lib/binfmt-support/run-detectors
flags:
offset 0
magic 4d5a


(on a Debian system). This tells the kernel that binaries starting with MZ (4d5a) should be given to run-detectors. The latter figures out whether to use Mono or Wine to run the binary.

Binary types can be added, removed, enabled and disabled at any time; see the documentation above for details (the semantics are surprising, the virtual filesystem used here doesn't behave entirely like a standard filesystem). /proc/sys/fs/binfmt_misc/status gives the global status, and each binary "descriptor" shows its individual status. Another way of disabling binfmt_misc is to unload its kernel module, if it's built as a module; this also means it's possible to blacklist it to avoid it entirely.

This feature allows new binary types to be supported, such as MZ executables (which include Windows PE and PE+ binaries, but also DOS and OS/2 binaries!), Java JAR files... It also allows known binary types to be supported on new architectures, typically using Qemu; thus, with the appropriate libraries, you can transparently run ARM Linux binaries on an Intel processor!

Your question stemmed from cross-compilation, albeit in the .NET sense, and that brings up a caveat with binfmt_misc: some configuration scripts misbehave when you try to cross-compile on a system which can run the cross-compiled binaries. Typically, detecting cross-compilation involves building a binary and attempting to run it; if it runs, you're not cross-compiling, if it doesn't, you are (or your compiler's broken). autoconf scripts can usually be fixed in this case by explicitly specifying the build and host architectures, but sometimes you'll have to disable binfmt_misc temporarily...

**参考链接**: https://unix.stackexchange.com/questions/259376/how-is-mono-magical

> 📎 来源 / Source: https://unix.stackexchange.com/questions/259376/how-is-mono-magical

#### 71. Difference between pts and tty

**故障现象**: Difference between pts and tty
**标签 / 来源**: Tags: linux, tty, terminology, who | unix | 👍 164 | 💬 3 answers

**问题描述**:
Tags: linux, tty, terminology, who | Score: 164 | Views: 176362 | Answers: 3

**解决方法 / 社区答案**:
A tty is a native terminal device, the backend is either hardware or kernel-emulated.
A pty (pseudo terminal device) is a terminal device which is emulated by another program (example: xterm, screen, or ssh are such programs). A pts is the slave part of a pty.
(More info can be found in man pty.)
Short summary:
A pty is created by a process through posix_openpt() (which usually opens the special device /dev/ptmx), and is constituted by a pair of bidirectional character devices:

The master part, which is the file descriptor obtained by this process through this call, is used to emulate a terminal. After some initialization, the second part can be unlocked with unlockpt(), and the master is used to receive or send characters to this second part (slave).

The slave part, which is anchored in the filesystem as /dev/pts/x (the real name can be obtained by the master through ptsname()) behaves like a native terminal device (/dev/ttyx). In most cases, a shell is started that uses it as a controlling terminal.

**参考链接**: https://unix.stackexchange.com/questions/21280/difference-between-pts-and-tty

> 📎 来源 / Source: https://unix.stackexchange.com/questions/21280/difference-between-pts-and-tty

#### 72. How to show the filesystem type via the terminal?

**故障现象**: How to show the filesystem type via the terminal?
**标签 / 来源**: Tags: linux, filesystems | unix | 👍 163 | 💬 2 answers

**问题描述**:
Tags: linux, filesystems | Score: 163 | Views: 380005 | Answers: 2

**解决方法 / 社区答案**:
Yes, according to man df you can:


-T, --print-type      print file system type



Another way is to use the mount command. Without parameters it lists the currently mounted devices, including their file systems.

In case you need to find out only one certain file system, is easier to use the stat command's -f option instead of parsing out one value from the above mentioned commands' output.

**参考链接**: https://unix.stackexchange.com/questions/53313/how-to-show-the-filesystem-type-via-the-terminal

> 📎 来源 / Source: https://unix.stackexchange.com/questions/53313/how-to-show-the-filesystem-type-via-the-terminal

#### 73. How do SO (shared object) numbers work?

**故障现象**: How do SO (shared object) numbers work?
**标签 / 来源**: Tags: linux, dynamic-linking | unix | 👍 163 | 💬 4 answers

**问题描述**:
Tags: linux, dynamic-linking | Score: 163 | Views: 123963 | Answers: 4

**解决方法 / 社区答案**:
Binaries themselves know which version of a shared library they depend on, and request it specifically. You can use ldd to show the dependencies; mine for ls are:

$ ldd /bin/ls
    linux-gate.so.1 =&gt;  (0xb784e000)
    librt.so.1 =&gt; /lib/librt.so.1 (0xb782c000)
    libacl.so.1 =&gt; /lib/libacl.so.1 (0xb7824000)
    libc.so.6 =&gt; /lib/libc.so.6 (0xb76dc000)
    libpthread.so.0 =&gt; /lib/libpthread.so.0 (0xb76c3000)
    /lib/ld-linux.so.2 (0xb784f000)
    libattr.so.1 =&gt; /lib/libattr.so.1 (0xb76bd000)


As you can see, it points to e.g. libpthread.so.0, not just libpthread.so.



The reason for the symbolic link is for the linker. When you want to link against libpthread.so directly, you give gcc the flag -lpthread, and it adds on the lib prefix and .so suffix automatically. You can't tell it to add on the .so.0 suffix, so the symbolic link points to the newest version of the lib to faciliate that

**参考链接**: https://unix.stackexchange.com/questions/475/how-do-so-shared-object-numbers-work

> 📎 来源 / Source: https://unix.stackexchange.com/questions/475/how-do-so-shared-object-numbers-work

#### 74. How to output only file names (with spaces) in ls -Al?

**故障现象**: How to output only file names (with spaces) in ls -Al?
**标签 / 来源**: Tags: linux, command-line, ls | unix | 👍 162 | 💬 10 answers

**问题描述**:
Tags: linux, command-line, ls | Score: 162 | Views: 448811 | Answers: 10

**解决方法 / 社区答案**:
You really should not parse the output of ls. If this is a homework assignment and you are required to, your professor does not know what they're talking about. Why don't you do something like this:

  The good...

find ./  -printf "%f\n"


or

for n in *; do printf '%s\n' "$n"; done


...the bad...

If you really really want to use ls, you can make it a little bit more robust by doing something like this:

ls -lA | awk -F':[0-9]* ' '/:/{print $2}'


...and the ugly

If you insist on doing it the wrong, dangerous way and just have to use a while loop, do this:

ls -Al | while IFS= read -r string; do echo "$string" | 
    awk -F':[0-9]* ' '/:/{print $2}'; done


Seriously though, just don't.

**参考链接**: https://unix.stackexchange.com/questions/70614/how-to-output-only-file-names-with-spaces-in-ls-al

> 📎 来源 / Source: https://unix.stackexchange.com/questions/70614/how-to-output-only-file-names-with-spaces-in-ls-al

#### 75. How to see process created by specific user in Unix/linux

**故障现象**: How to see process created by specific user in Unix/linux
**标签 / 来源**: Tags: linux, process, ps | unix | 👍 161 | 💬 3 answers

**问题描述**:
Tags: linux, process, ps | Score: 161 | Views: 478947 | Answers: 3

**解决方法 / 社区答案**:
To view only the processes owned by a specific user, use the following command:

top -U [username]


Replace the [username] with the required username

If you want to use ps then

ps -u [username]


OR

 ps -ef | grep &lt;username&gt;


OR

ps -efl | grep &lt;username&gt;


for the extended listing

Check out the man ps page for options

Another alternative is to use pstree wchich prints the process tree of the user

pstree &lt;username or pid&gt;

**参考链接**: https://unix.stackexchange.com/questions/85466/how-to-see-process-created-by-specific-user-in-unix-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/85466/how-to-see-process-created-by-specific-user-in-unix-linux

#### 76. Long line wrapping in Nano

**故障现象**: Long line wrapping in Nano
**标签 / 来源**: Tags: ubuntu, nano | unix | 👍 160 | 💬 8 answers

**问题描述**:
Tags: ubuntu, nano | Score: 160 | Views: 189904 | Answers: 8

**解决方法 / 社区答案**:
To see the word wrapping style you described, use nano's "soft wrapping": Esc+$.

The Esc+L command you (and everyone) tried does "hard wrapping."

Note on keystroke notation - if you are new to Linux, the notation Esc+$ means press and release Esc and then press $.  The full key press sequence then is Esc, Shift+4.

(It does not mean hold down escape while pressing $.)

Source: https://www.nano-editor.org/dist/v2.9/nano.html (search for --softwrap)


Note on softwrap and formatting mistakes - If you are new to nano, be a little careful of softwrap. If you are editing a configuration file or something else that is sensitive to newlines or indents, formatting mistakes can be made. Until you get comfortable with softwrap’s behaviors, I suggest doing a quick check with softwrap off (do the key sequence again) before saving. 

Note on the goodness provided by others in their answers below - because different operating systems and different versions of nano do things a little differently:


If you like softwrap on all of the time, set it in your .nanorc, as described in x0a's answer below, as it is a bit more through than Prashant's.
If you have a Raspberry Pi, note chainsawmascara's answer about needing an extra keystroke for softwrap to go into effect.
If you have a Mac, like lodeOfCode's answer below, you can always update nano and here, and thus bask in the warm glow of softwrap!


nano linewrap

**参考链接**: https://unix.stackexchange.com/questions/122795/long-line-wrapping-in-nano

> 📎 来源 / Source: https://unix.stackexchange.com/questions/122795/long-line-wrapping-in-nano

#### 77. List partition labels from the command line

**故障现象**: List partition labels from the command line
**标签 / 来源**: Tags: linux, command-line, partition, disk | unix | 👍 158 | 💬 14 answers

**问题描述**:
Tags: linux, command-line, partition, disk | Score: 158 | Views: 326238 | Answers: 14

**解决方法 / 社区答案**:
with lsblk
For instance, the command
lsblk -o name,mountpoint,label,size,uuid

outputs:
NAME                           MOUNTPOINT     LABEL         SIZE UUID
sda                                                         1.4T
├─sda1                         /boot          boot          953M f557b9f0-edb5-42bb-94d8-27bc03c3c2c7
├─sda2                                                     46.6G 727fa348-8804-4773-ae3d-f3e176d12dac
│ └─sda2_crypt (dm-0)                                      46.6G P1kvJI-5iqv-s9gJ-8V2H-2EEO-q4aK-sx4aDi
│   ├─debian_crypt-swap (dm-1) [SWAP]                         2G 3f9f24d7-86d1-4e21-93e9-f3c181d05cf0
│   ├─debian_crypt-tmp (dm-2)  /tmp           tmp             5G 93fc8219-f985-45fb-bd5c-2c7940a7512d
│   ├─debian_crypt-home (dm-3) /home          home            6G 12e8566c-8f0f-45ec-8524-6d9d9ee91eae
│   └─debian_crypt-root (dm-4) /              root         33.6G 9685570b-4c9e-43ea-815e-49d10dc7a1bf
├─sda3                                                    651.9G d3e0436c-85f6-45c6-9d8f-28b79ee06102
│ └─crypt_gusto (dm-8)         /media/Gusto   Gusto       651.9G 0c084508-cb8b-4b61-832d-6b85273f33c4
├─sda4                                                        1K
├─sda5                                                      298G 5063da5f-9b68-43de-914c-32b89622bcc8
│ └─crypt_kabi (dm-7)          /media/Kabi    Kabi          298G e6a0b66c-8fe9-4e7b-9d54-7b2b430e109d
├─sda6                                                    213.6G 5129d860-bb41-4393-b4b1-f8af53d9155d
│ └─crypt_zami (dm-6)          /media/Zami    Zami        213.6G 19101155-6070-4f37-b39d-19f28867c66b
├─sda7                         /media/Server  Server       85.6G a9f4dae5-901c-4f49-bb30-592de3000713
└─sda8                                                    100.6G dc7f4586-a33d-4707-98e9-8b55c559b0d2
  └─crypt_grafi (dm-5)         /media/Grafi   Grafi       100.6G 5e3242e1-ec7a-4806-92f7-88a126feea94
sdb                                                        14.5G
├─sdb1                                        DEBIAN_LIVE     3G 6bf4d915-2b62-444e-a2c8-16307769b5c2
├─sdb2                                                        2G 90ec6f73-8fdb-4c8d-aebd-cadd0f51b412
│ └─crypt_sdb2 (dm-10)         /mnt           data            2G 91e779dd-0a3f-40b2-8ad0-257d860541a6
└─sdb3                                        linux         9.5G 14a783a4-96dd-4a85-8de7-6e8eea230594
loop0                                                      1000M a3be80bf-0f2c-44ed-8de5-d60e3b19c01a
└─crypt_dropbox (dm-9)         /media/Dropbox Dropbox       998M 8461e2cf-ae17-449b-8ee5-29cc88688b8b
zram0                          [SWAP]                       250M f8254ae5-5ae6-4fda-b8ef-83f25c405894
zram1                          [SWAP]                       250M 7e7ed90d-731c-422a-bf9b-828f09b80502

You can specify plenty of columns in whatever order you like:
Available output columns:
         NAME  device name
        KNAME  internal kernel device name
         PATH  path to the device node
      MAJ:MIN  major:minor device number
      FSAVAIL  filesystem size available
       FSSIZE  filesystem size
       FSTYPE  filesystem type
       FSUSED  filesystem size used
       FSUSE%  filesystem use percentage
      FSROOTS  mounted filesystem roots
        FSVER  filesystem version
   MOUNTPOINT  where the device is mounted
  MOUNTPOINTS  all locations where device is mounted
        LABEL  filesystem LABEL
         UUID  filesystem UUID
       PTUUID  partition table identifier (usually UUID)
       PTTYPE  partition table type
     PARTTYPE  partition type code or UUID
 PARTTYPENAME  partition type name
    PARTLABEL  partition LABEL
     PARTUUID  partition UUID
    PARTFLAGS  partition flags
           RA  read-ahead of the device
           RO  read-only device
           RM  removable device
      HOTPLUG  removable or hotplug device (usb, pcmcia, ...)
        MODEL  device identifier
       SERIAL  disk serial number
         SIZE  size of the device
        STATE  state of the device
        OWNER  user name
        GROUP  group name
         MODE  device node permissions
    ALIGNMENT  alignment offset
       MIN-IO  minimum I/O size
       OPT-IO  optimal I/O size
      PHY-SEC  physical sector size
      LOG-SEC  logical sector size
         ROTA  rotational device
        SCHED  I/O scheduler name
      RQ-SIZE  request queue size
         TYPE  device type
     DISC-ALN  discard alignment offset
    DISC-GRAN  discard granularity
     DISC-MAX  discard max bytes
    DISC-ZERO  discard zeroes data
        WSAME  write same max bytes
          WWN  unique storage identifier
         RAND  adds randomness
       PKNAME  internal parent kernel device name
         HCTL  Host:Channel:Target:Lun for SCSI
         TRAN  device transport type
   SUBSYSTEMS  de-duplicated chain of subsystems
          REV  device revision
       VENDOR  device vendor
        ZONED  zone model
          DAX  dax-capable device

**参考链接**: https://unix.stackexchange.com/questions/14165/list-partition-labels-from-the-command-line

> 📎 来源 / Source: https://unix.stackexchange.com/questions/14165/list-partition-labels-from-the-command-line

#### 78. Why does /etc/resolv.conf point at 127.0.0.53?

**故障现象**: Why does /etc/resolv.conf point at 127.0.0.53?
**标签 / 来源**: Tags: linux, dns, resolv.conf | unix | 👍 158 | 💬 3 answers

**问题描述**:
Tags: linux, dns, resolv.conf | Score: 158 | Views: 318752 | Answers: 3

**解决方法 / 社区答案**:
You are likely running systemd-resolved as a service.
systemd-resolved generates two configuration files on the fly, for optional use by DNS client libraries (such as the BIND DNS client library in C libraries):

/run/systemd/resolve/stub-resolv.conf tells DNS client libraries to send their queries to 127.0.0.53.  This is where the systemd-resolved process listens for DNS queries, which it then forwards on.
/run/systemd/resolve/resolv.conf tells DNS client libraries to send their queries to IP addresses that systemd-resolved has obtained on the fly from its configuration files and DNS server information contained in DHCP leases.  Effectively, this bypasses the systemd-resolved forwarding step, at the expense of also bypassing all of systemd-resolved's logic for making complex decisions about what to actually forward to, for any given transaction.

In both cases, systemd-resolved configures a search list of domain name suffixes, again derived on the fly from its configuration files and DHCP leases (which it is told about via a mechanism that is beyond the scope of this answer).
/etc/resolv.conf can optionally be:

a symbolic link to either of these;
a symbolic link to a package-supplied static file at /usr/lib/systemd/resolv.conf, which also specifies 127.0.0.53 but no search domains calculated on the fly;
some other file entirely.

It's likely that you have such a symbolic link.
In which case, the thing that knows about the 192.168.1.1 setting, that is (presumably) handed out in DHCP leases by the DHCP server on your LAN, is systemd-resolved, which is forwarding query traffic to it as you have observed.
Your DNS client libraries, in your applications programs, are themselves only talking to systemd-resolved.
Ironically, although it could be that you haven't captured loopback interface traffic to/from 127.0.0.53 properly, it is more likely that you aren't seeing it because systemd-resolved also (optionally) bypasses the BIND DNS Client in your C libraries and generates no such traffic to be captured.
There's an NSS module provided with systemd-resolved, named nss-resolve, that is a plug-in for your C libraries.
Previously, your C libraries would have used another plug-in named nss-dns which uses the BIND DNS Client to make queries using the DNS protocol to the server(s) listed in /etc/resolv.conf, applying the domain suffixes listed therein.
nss-resolve gets listed ahead of nss-dns in your /etc/nsswitch.conf file, causing your C libraries to not use the BIND DNS Client, or the DNS protocol, to perform name→address lookups at all.
Instead, nss-resolve speaks a non-standard and idiosyncratic protocol over the (system-wide) Desktop Bus to systemd-resolved, which again makes back end queries of 192.168.1.1 or whatever your DHCP leases and configuration files say.
To intercept that you have to monitor the Desktop Bus traffic with dbus-monitor or some such tool.
It's not even IP traffic, let alone IP traffic over a loopback network interface. as the Desktop Bus is reached via an AF_LOCAL socket.
If you want to use a third-party resolving proxy DNS server at 1.1.1.1, or some other IP address, you have three choices:

Configure your DHCP server to hand that out instead of handing out 192.168.1.1.  systemd-resolved will learn of that via the DHCP leases and use it.
Configure systemd-resolved via its own configuration mechanisms to use that instead of what it is seeing in the DHCP leases.
Make your own /etc/resolv.conf file, an actual regular file instead of a symbolic link, list 1.1.1.1 there and remember to turn off nss-resolve so that you go back to using nss-dns and the BIND DNS Client.

The systemd-resolved configuration files are a whole bunch of files in various directories that get combined, and how to configure them for the second choice aforementioned is beyond the scope of this answer.
Read the resolved.conf(5) manual page for that.

**参考链接**: https://unix.stackexchange.com/questions/612416/why-does-etc-resolv-conf-point-at-127-0-0-53

> 📎 来源 / Source: https://unix.stackexchange.com/questions/612416/why-does-etc-resolv-conf-point-at-127-0-0-53

#### 79. How does the OOM killer decide which process to kill first?

**故障现象**: How does the OOM killer decide which process to kill first?
**标签 / 来源**: Tags: linux, memory, out-of-memory | unix | 👍 157 | 💬 1 answers

**问题描述**:
Tags: linux, memory, out-of-memory | Score: 157 | Views: 189916 | Answers: 1

**解决方法 / 社区答案**:
If memory is exhaustively used up by processes, to the extent which can possibly threaten the stability of the system, then the OOM killer comes into the picture.
NOTE: It is the task of the OOM Killer to continue killing processes until enough memory is freed for the smooth functioning of the rest of the process that the Kernel is attempting to run.
The OOM Killer has to select the best process(es) to kill. Best here refers to that process which will free up the maximum memory upon killing and is also the least important to the system.
The primary goal is to kill the least number of processes that minimizes the damage done and at the same time maximizing the amount of memory freed.
To facilitate this, the kernel maintains an oom_score for each of the processes. You can see the oom_score of each of the processes in the /proc filesystem under the pid directory.
$ cat /proc/10292/oom_score

The higher the value of oom_score of any process, the higher is its likelihood of getting killed by the OOM Killer in an out-of-memory situation.
How is the OOM_Score calculated?

In David's patch set, the old badness() heuristics are almost entirely
gone. Instead, the calculation turns into a simple question of what
percentage of the available memory is being used by the process. If
the system as a whole is short of memory, then &quot;available memory&quot; is
the sum of all RAM and swap space available to the system.
If instead, the OOM situation is caused by exhausting the memory allowed
to a given cpuset/control group, then &quot;available memory&quot; is the total
amount allocated to that control group. A similar calculation is made
if limits imposed by a memory policy have been exceeded. In each case,
the memory use of the process is deemed to be the sum of its resident
set (the number of RAM pages it is using) and its swap usage.
This calculation produces a percent-times-ten number as a result; a
process which is using every byte of the memory available to it will
have a score of 1000, while a process using no memory at all will get
a score of zero. There are very few heuristic tweaks to this score,
but the code does still subtract a small amount (30) from the score of
root-owned processes on the notion that they are slightly more
valuable than user-owned processes.
One other tweak which is applied is to add the value stored in each
process's oom_score_adj variable, which can be adjusted via /proc.
This knob allows the adjustment of each process's attractiveness to
the OOM killer in user space; setting it to -1000 will disable OOM
kills entirely, while setting to +1000 is the equivalent of painting a
large target on the associated process.

References
http://www.queryhome.com/15491/whats-happening-kernel-starting-killer-choose-which-process
https://serverfault.com/a/571326

**参考链接**: https://unix.stackexchange.com/questions/153585/how-does-the-oom-killer-decide-which-process-to-kill-first

> 📎 来源 / Source: https://unix.stackexchange.com/questions/153585/how-does-the-oom-killer-decide-which-process-to-kill-first

#### 80. Show top five CPU consuming processes with `ps`

**故障现象**: Show top five CPU consuming processes with `ps`
**标签 / 来源**: Tags: linux, ps | unix | 👍 156 | 💬 13 answers

**问题描述**:
Tags: linux, ps | Score: 156 | Views: 520011 | Answers: 13

**解决方法 / 社区答案**:
Why use ps when you can do it easily with the top command?

If you must use ps, try this:

ps aux | sort -nrk 3,3 | head -n 5


If you want something that's truly 'top'esq with constant updates, use watch

watch "ps aux | sort -nrk 3,3 | head -n 5"

**参考链接**: https://unix.stackexchange.com/questions/13968/show-top-five-cpu-consuming-processes-with-ps

> 📎 来源 / Source: https://unix.stackexchange.com/questions/13968/show-top-five-cpu-consuming-processes-with-ps

#### 81. How do I kill all screens?

**故障现象**: How do I kill all screens?
**标签 / 来源**: Tags: linux, bash, gnu-screen, kill | unix | 👍 153 | 💬 8 answers

**问题描述**:
Tags: linux, bash, gnu-screen, kill | Score: 153 | Views: 467444 | Answers: 8

**解决方法 / 社区答案**:
You can use :

pkill screen


Or 

killall screen




In OSX the process is called SCREEN in all caps. So, use:

pkill SCREEN


Or

killall SCREEN

**参考链接**: https://unix.stackexchange.com/questions/94527/how-do-i-kill-all-screens

> 📎 来源 / Source: https://unix.stackexchange.com/questions/94527/how-do-i-kill-all-screens

#### 82. How can I look up a username by id in linux?

**故障现象**: How can I look up a username by id in linux?
**标签 / 来源**: Tags: linux, ubuntu, users, uuid | unix | 👍 146 | 💬 8 answers

**问题描述**:
Tags: linux, ubuntu, users, uuid | Score: 146 | Views: 362675 | Answers: 8

**解决方法 / 社区答案**:
You might enjoy this little ditty. 

$ id -nu [number]


3.17.3-1-ARCH #1 SMP PREEMPT Fri Nov 14 22:56:01 CET 2014 i686 GNU/Linux

I can confirm that it returns a corresponding user name, if one exists, on Arch Linux. I can also confirm that it does not work on Ubuntu when run as a normal user, although I have not tested this as the superuser. It also does not work on Alpine Linux. Maybe a security feature prevents this from working on some systems.

**参考链接**: https://unix.stackexchange.com/questions/36580/how-can-i-look-up-a-username-by-id-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/36580/how-can-i-look-up-a-username-by-id-in-linux

#### 83. Difference between /bin and /usr/bin

**故障现象**: Difference between /bin and /usr/bin
**标签 / 来源**: Tags: linux, directory, fhs | unix | 👍 144 | 💬 5 answers

**问题描述**:
Tags: linux, directory, fhs | Score: 144 | Views: 160721 | Answers: 5

**解决方法 / 社区答案**:
What? no /bin/ is not a symlink to /usr/bin on any FHS compliant system. Note that there are still popular Unices and Linuxes that ignore this - for example, /bin and /sbin are symlinked to /usr/bin on Arch Linux (the reasoning being that you don't need /bin for rescue/single-user-mode, since you'd just boot a live CD).

/bin

contains commands that may be used by both the system administrator and by users, but which are required when no other filesystems are mounted (e.g. in single user mode). It may also contain commands which are used indirectly by scripts

/usr/bin/

This is the primary directory of executable commands on the system.

essentially, /bin contains executables which are required by the system for emergency repairs, booting, and single user mode. /usr/bin contains any binaries that aren't required.

I will note, that they can be on separate disks/partitions, /bin must be on the same disk as /. /usr/bin can be on another disk - although note that this configuration has been kind of broken for a while (this is why e.g. systemd warns about this configuration on boot).

For full correctness, some unices may ignore FHS, as I believe it is only a Linux Standard, I'm not aware that it has yet been included in SUS, Posix or any other UNIX standard, though it should be IMHO. It is a part of the LSB standard though.

**参考链接**: https://unix.stackexchange.com/questions/5915/difference-between-bin-and-usr-bin

> 📎 来源 / Source: https://unix.stackexchange.com/questions/5915/difference-between-bin-and-usr-bin

#### 84. How do I know if a partition is ext2, ext3, or ext4?

**故障现象**: How do I know if a partition is ext2, ext3, or ext4?
**标签 / 来源**: Tags: linux, ext4, ext3, ext2 | unix | 👍 143 | 💬 12 answers

**问题描述**:
Tags: linux, ext4, ext3, ext2 | Score: 143 | Views: 229365 | Answers: 12

**解决方法 / 社区答案**:
How do I tell what sort of data (what data format) is in a file?
→ Use the file utility.

Here, you want to know the format of data in a device file, so you need to pass the -s flag to tell file not just to say that it's a device file but look at the content. Sometimes you'll need the -L flag as well, if the device file name is a symbolic link. You'll see output like this:

# file -sL /dev/sd*
/dev/sda1: Linux rev 1.0 ext4 filesystem data, UUID=63fa0104-4aab-4dc8-a50d-e2c1bf0fb188 (extents) (large files) (huge files)
/dev/sdb1: Linux rev 1.0 ext2 filesystem data, UUID=b3c82023-78e1-4ad4-b6e0-62355b272166
/dev/sdb2: Linux/i386 swap file (new style), version 1 (4K pages), size 4194303 pages, no label, UUID=3f64308c-19db-4da5-a9a0-db4d7defb80f


Given this sample output, the first disk has one partition and the second disk has two partitions. /dev/sda1 is an ext4 filesystem, /dev/sdb1 is an ext2 filesystem, and /dev/sdb2 is some swap space (about 4GB).

You must run this command as root, because ordinary users may not read disk partitions directly: if needed, add sudo in front.

**参考链接**: https://unix.stackexchange.com/questions/60723/how-do-i-know-if-a-partition-is-ext2-ext3-or-ext4

> 📎 来源 / Source: https://unix.stackexchange.com/questions/60723/how-do-i-know-if-a-partition-is-ext2-ext3-or-ext4

#### 85. How can I tell what version of Linux I&#39;m using?

**故障现象**: How can I tell what version of Linux I&#39;m using?
**标签 / 来源**: Tags: linux, ssh, version, info, system-information | unix | 👍 142 | 💬 13 answers

**问题描述**:
Tags: linux, ssh, version, info, system-information | Score: 142 | Views: 175458 | Answers: 13

**解决方法 / 社区答案**:
If I need to know what it is say Linux/Unix , 32/64 bit

uname -a 


This would give me almost all information that I need, 

If I further need to know what release it is say (Centos 5.4, or 5.5 or 5.6)
on a Linux box I would further check the file /etc/issue to see its release info ( or for Debian / Ubuntu /etc/lsb-release )

Alternative way is to use the lsb_release utility:

lsb_release -a


Or do a rpm -qa | grep centos-release or redhat-release for RHEL derived systems

**参考链接**: https://unix.stackexchange.com/questions/23833/how-can-i-tell-what-version-of-linux-im-using

> 📎 来源 / Source: https://unix.stackexchange.com/questions/23833/how-can-i-tell-what-version-of-linux-im-using

#### 86. What is the difference between reboot , init 6 and shutdown -r now?

**故障现象**: What is the difference between reboot , init 6 and shutdown -r now?
**标签 / 来源**: Tags: linux, shutdown, init, reboot | unix | 👍 142 | 💬 4 answers

**问题描述**:
Tags: linux, shutdown, init, reboot | Score: 142 | Views: 415220 | Answers: 4

**解决方法 / 社区答案**:
There is no difference in them. Internally they do exactly the same thing:


reboot uses the shutdown command (with the -r switch). The shutdown command used to kill all the running processes, unmount all the file systems and finally tells the kernel to issue the ACPI power command. The source can be found here.
In older distros the reboot command was forcing the processes to exit by issuing the SIGKILL signal (still found in sources, can be invoked with -f option), in most recent distros it defaults to the more graceful and init friendly init 1 -&gt; shutdown -r. This ensures that daemons clean up themselves before shutdown.
init 6 tells the init process to shutdown all of the spawned processes/daemons as written in the init files (in the inverse order they started) and lastly invoke the shutdown -r now command to reboot the machine


Today there is not much difference as both commands do exactly the same, and they respect the init scripts used to start services/daemons by invoking the shutdown scripts for them. Except for reboot -f -r now as stated below

There is a small explanation taken from manpages of why the reboot -f is not safe:


  -f, --force
    Force immediate halt, power-off, reboot. Don't contact the init system.


Edit:

Forgot to mention, in upcoming RHEL distributions you should use the new systemctl command to issue poweroff/reboot. As stated in the manpages of reboot and shutdown they are "a legacy command available for compatibility only." and the systemctl method will be the only one safe.

**参考链接**: https://unix.stackexchange.com/questions/64280/what-is-the-difference-between-reboot-init-6-and-shutdown-r-now

> 📎 来源 / Source: https://unix.stackexchange.com/questions/64280/what-is-the-difference-between-reboot-init-6-and-shutdown-r-now

#### 87. Linux ls to show only file name, date, and size

**故障现象**: Linux ls to show only file name, date, and size
**标签 / 来源**: Tags: linux, command-line, files, ls | unix | 👍 141 | 💬 15 answers

**问题描述**:
Tags: linux, command-line, files, ls | Score: 141 | Views: 248431 | Answers: 15

**解决方法 / 社区答案**:
Try stat instead of ls. Here with the GNU implementation of stat (beware the BSDs and zsh also have a stat command but with a completely different API):
stat -c &quot;%y %s %n&quot; -- *

To output in columnar format (assuming none of the file names contain comma or newline characters):
stat -c &quot;%n,%s&quot; -- * | column -t -s,

Beware that if there's a file called - in the current working directory, GNU stat will report information about the file opened on stdin instead of for that file.
If you run into a Argument list too long error, with shells where printf is builtin, you can change it to:
printf '%s\0' * | xargs -0 stat -c &quot;%y %s %n&quot; --

Or in ksh93:
command -x stat -c &quot;%y %s %n&quot; -- *

Which will run as many invocations of stat as necessary to work around the limit on the size of the arguments.

**参考链接**: https://unix.stackexchange.com/questions/22218/linux-ls-to-show-only-file-name-date-and-size

> 📎 来源 / Source: https://unix.stackexchange.com/questions/22218/linux-ls-to-show-only-file-name-date-and-size

#### 88. File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)

**故障现象**: File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)
**标签 / 来源**: Tags: ubuntu, permissions, virtualbox, virtual-machine | unix | 👍 141 | 💬 10 answers

**问题描述**:
Tags: ubuntu, permissions, virtualbox, virtual-machine | Score: 141 | Views: 333935 | Answers: 10

**解决方法 / 社区答案**:
The regular way of getting access to the files now, is to allow VirtualBox to automount the shared folder (which will make it show up under /media/sf_directory_name) and then to add your regular Ubuntu user to the vboxsf group (as root #).

# usermod -aG vboxsf &lt;youruser&gt;


By default, without manual action, the mounts look like this,

drwxrwx--- 1 root vboxsf 40960 Oct 23 10:42 sf_&lt;name&gt;


so the vboxsf group has full access.  By adding your user to that group, you gain full access.  So you wouldn't worry about changing their permissions (which don't make sense on the Windows host), you just give yourself access.

In this specific case, this is the automounted Shared Folder,

Ubuntu               214153212  31893804 182259408  15% /media/sf_Ubuntu


and it is that directory that should be used to access to the Shared Folder, by putting the local user into the vboxsf group.  If you want a 'better' link under your user's home directory, you could always create a symbolic link.

ln -s /media/sf_Ubuntu /home/m/Desktop/vbox_shared


You will need to reboot your VM for these changes to take effect

If you manually mount the shared folder, then you need to use the relevant options on the mount command to set the folder with the right ownership (i.e. the gid, uid and umask options to mount).  This is because the Host OS doesn't support the same permission system as Linux, so VirtualBox has no way of knowing who should own the files.

However, I strongly recommend just configuring the shared folder to be auto-mounted (it's a setting on the Shared Folder configuration in VirtualBox itself).


For the avoidance of doubt, I do not believe you can change permissions normally anyway, on that filesystem if it's mounted in the regular way,

tony@jabba:/media/sf_name$ ls -l tst.txt
-rwxrwx--- 1 root vboxsf 2283 Apr  4  2012 tst.txt
tony@jabba:/media/sf_name$ sudo chown tony tst.txt
[sudo] password for tony: 
tony@jabba:/media/sf_name$ ls -l tst.txt
-rwxrwx--- 1 root vboxsf 2283 Apr  4  2012 tst.txt
tony@jabba:/media/sf_name$

**参考链接**: https://unix.stackexchange.com/questions/52667/file-permission-issues-with-shared-folders-under-virtual-box-ubuntu-guest-wind

> 📎 来源 / Source: https://unix.stackexchange.com/questions/52667/file-permission-issues-with-shared-folders-under-virtual-box-ubuntu-guest-wind

#### 89. Set the default kernel in GRUB

**故障现象**: Set the default kernel in GRUB
**标签 / 来源**: Tags: linux, kernel, boot, grub | unix | 👍 140 | 💬 11 answers

**问题描述**:
Tags: linux, kernel, boot, grub | Score: 140 | Views: 428583 | Answers: 11

**解决方法 / 社区答案**:
After struggling for 2 hours, I have found a much easier way to achieve this. I just RTFM. ;)
Add two lines to /etc/default/grub
GRUB_SAVEDEFAULT=true
GRUB_DEFAULT=saved

Do the sudo update-grub, reboot, get into your grub menu and select whichever menu or submenu item you need. The choice will be saved every time and then your computer will boot into it automatically. When you manually choose a different entry, that becomes the new default.

**参考链接**: https://unix.stackexchange.com/questions/198003/set-the-default-kernel-in-grub

> 📎 来源 / Source: https://unix.stackexchange.com/questions/198003/set-the-default-kernel-in-grub

#### 90. How do I find how long ago a Linux system was installed?

**故障现象**: How do I find how long ago a Linux system was installed?
**标签 / 来源**: Tags: linux, system-installation | unix | 👍 139 | 💬 18 answers

**问题描述**:
Tags: linux, system-installation | Score: 139 | Views: 151247 | Answers: 18

**解决方法 / 社区答案**:
sudo tune2fs -l /dev/sda1 **OR** /dev/sdb1*  | grep 'Filesystem created:'

This will tell you when the file system was created.
* = In the first column of df / you can find the exact partition to use.

**参考链接**: https://unix.stackexchange.com/questions/9971/how-do-i-find-how-long-ago-a-linux-system-was-installed

> 📎 来源 / Source: https://unix.stackexchange.com/questions/9971/how-do-i-find-how-long-ago-a-linux-system-was-installed

#### 91. timestamp, modification time, and created time of a file

**故障现象**: timestamp, modification time, and created time of a file
**标签 / 来源**: Tags: linux, filesystems, files | unix | 👍 138 | 💬 2 answers

**问题描述**:
Tags: linux, filesystems, files | Score: 138 | Views: 352604 | Answers: 2

**解决方法 / 社区答案**:
There are 3 kind of "timestamps":


Access - the last time the file was read
Modify - the last time the file was modified (content has been modified)
Change - the last time meta data of the file was changed (e.g. permissions)


To display this information, you can use stat which is part of the coreutils.

stat will show you also some more information like the device, inodes, links, etc.

Remember that this sort of information depends highly on the filesystem and mount options. For example if you mount a partition with the noatime option, no access information will be written.

A utility to change the timestamps would be touch.
There are some arguments to decide which timestamp to change (e.g. -a for access time, -m for modification time) and to influence the parsing of a new given timestamp.
See man touch for more details.

touch can become handy in combination with cp -u ("copy only when the SOURCE file is newer than the destination file or when the destination file is missing") or for the creation of empty marker files.

**参考链接**: https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file

> 📎 来源 / Source: https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file

#### 92. Easy way to determine the virtualization technology of a Linux machine?

**故障现象**: Easy way to determine the virtualization technology of a Linux machine?
**标签 / 来源**: Tags: linux, command-line, virtual-machine | unix | 👍 137 | 💬 17 answers

**问题描述**:
Tags: linux, command-line, virtual-machine | Score: 137 | Views: 130239 | Answers: 17

**解决方法 / 社区答案**:
dmidecode -s system-product-name

I have tested on Vmware Workstation, VirtualBox, QEMU with KVM, standalone QEMU with Ubuntu as the guest OS. Others have added additional platforms that they're familiar with as well.

Virtualization technologies


VMware Workstation

root@router:~# dmidecode -s system-product-name
VMware Virtual Platform

VirtualBox

root@router:~# dmidecode -s system-product-name
VirtualBox

Qemu with KVM

root@router:~# dmidecode -s system-product-name
KVM

Qemu (emulated)

root@router:~# dmidecode -s system-product-name
Bochs

Microsoft VirtualPC

root@router:~# dmidecode | egrep -i 'manufacturer|product'
Manufacturer: Microsoft Corporation
Product Name: Virtual Machine

Virtuozzo

root@router:~# dmidecode
/dev/mem: Permission denied

Xen

root@router:~# dmidecode | grep -i domU
Product Name: HVM domU



On bare metal, this returns an identification of the computer or motherboard model.

/dev/disk/by-id

If you don't have the rights to run dmidecode then you can use:

Virtualization Technology: QEMU

ls -1 /dev/disk/by-id/


Output

[root@host-7-129 ~]# ls -1 /dev/disk/by-id/
ata-QEMU_DVD-ROM_QM00003
ata-QEMU_HARDDISK_QM00001
ata-QEMU_HARDDISK_QM00001-part1
ata-QEMU_HARDDISK_QM00002
ata-QEMU_HARDDISK_QM00002-part1
scsi-SATA_QEMU_HARDDISK_QM00001
scsi-SATA_QEMU_HARDDISK_QM00001-part1
scsi-SATA_QEMU_HARDDISK_QM00002
scsi-SATA_QEMU_HARDDISK_QM00002-part1


References


How to detect virtualization at dmo.ca

**参考链接**: https://unix.stackexchange.com/questions/89714/easy-way-to-determine-the-virtualization-technology-of-a-linux-machine

> 📎 来源 / Source: https://unix.stackexchange.com/questions/89714/easy-way-to-determine-the-virtualization-technology-of-a-linux-machine

#### 93. What&#39;s the best way to join files again after splitting them?

**故障现象**: What&#39;s the best way to join files again after splitting them?
**标签 / 来源**: Tags: linux, command-line, files, iso, split | unix | 👍 135 | 💬 6 answers

**问题描述**:
Tags: linux, command-line, files, iso, split | Score: 135 | Views: 214610 | Answers: 6

**解决方法 / 社区答案**:
That's just what cat was made for. Since it is one of the oldest GNU tools, I think it's very unlikely that any other tool does that faster/better. And it's not piping - it's only redirecting output.

**参考链接**: https://unix.stackexchange.com/questions/24630/whats-the-best-way-to-join-files-again-after-splitting-them

> 📎 来源 / Source: https://unix.stackexchange.com/questions/24630/whats-the-best-way-to-join-files-again-after-splitting-them

#### 94. Linux: set date through command line

**故障现象**: Linux: set date through command line
**标签 / 来源**: Tags: linux, date, clock | unix | 👍 134 | 💬 7 answers

**问题描述**:
Tags: linux, date, clock | Score: 134 | Views: 757612 | Answers: 7

**解决方法 / 社区答案**:
Use date -s:

date -s '2014-12-25 12:34:56'


Run that as root or under sudo. Changing only one of the year/month/day is more of a challenge and will involve repeating bits of the current date. There are also GUI date tools built in to the major desktop environments, usually accessed through the clock.

To change only part of the time, you can use command substitution in the date string:

date -s "2014-12-25 $(date +%H:%M:%S)"


will change the date, but keep the time. See man date for formatting details to construct other combinations: the individual components are %Y, %m, %d, %H, %M, and %S.

**参考链接**: https://unix.stackexchange.com/questions/151547/linux-set-date-through-command-line

> 📎 来源 / Source: https://unix.stackexchange.com/questions/151547/linux-set-date-through-command-line

#### 95. How can I find available network interfaces?

**故障现象**: How can I find available network interfaces?
**标签 / 来源**: Tags: linux, networking, devices, systemd, udev | unix | 👍 134 | 💬 6 answers

**问题描述**:
Tags: linux, networking, devices, systemd, udev | Score: 134 | Views: 512358 | Answers: 6

**解决方法 / 社区答案**:
The simplest method I know to list all of your interfaces is

ifconfig -a


EDIT

If you're on a system where that has been made obsolete, you can use

ip link show

**参考链接**: https://unix.stackexchange.com/questions/125400/how-can-i-find-available-network-interfaces

> 📎 来源 / Source: https://unix.stackexchange.com/questions/125400/how-can-i-find-available-network-interfaces

#### 96. Setting /proc/sys/vm/drop_caches to clear cache

**故障现象**: Setting /proc/sys/vm/drop_caches to clear cache
**标签 / 来源**: Tags: linux, virtual-memory | unix | 👍 134 | 💬 2 answers

**问题描述**:
Tags: linux, virtual-memory | Score: 134 | Views: 307376 | Answers: 2

**解决方法 / 社区答案**:
It isn't sticky - you just write to the file to make it drop the caches and then it immediately starts caching again.

Basically when you write to that file you aren't really changing a setting, you are issuing a command to the kernel. The kernel acts on that command (by dropping the caches) then carries on as before.

**参考链接**: https://unix.stackexchange.com/questions/17936/setting-proc-sys-vm-drop-caches-to-clear-cache

> 📎 来源 / Source: https://unix.stackexchange.com/questions/17936/setting-proc-sys-vm-drop-caches-to-clear-cache

#### 97. What is a tainted Linux kernel?

**故障现象**: What is a tainted Linux kernel?
**标签 / 来源**: Tags: linux, linux-kernel, kernel-modules, troubleshooting, proprietary-drivers | unix | 👍 134 | 💬 2 answers

**问题描述**:
Tags: linux, linux-kernel, kernel-modules, troubleshooting, proprietary-drivers | Score: 134 | Views: 207611 | Answers: 2

**解决方法 / 社区答案**:
A tainted kernel is one that is in an unsupported state because it cannot be guaranteed to function correctly. Most kernel developers will ignore bug reports involving tainted kernels, and community members may ask that you correct the tainting condition before they can proceed with diagnosing problems related to the kernel. In addition, some debugging functionality and API calls may be disabled when the kernel is tainted.
The taint state is indicated by a series of flags which represent the various reasons a kernel cannot be trusted to work properly. The most common reason for the kernel to become tainted is loading a proprietary graphics driver from NVIDIA or AMD, in which case it is generally safe to ignore the condition. However, some scenarios that cause the kernel to become tainted may be indicative of more serious problems such as failing hardware. It is a good idea to examine system logs and the specific taint flags set to determine the underlying cause of the issue.
This feature is intended to identify conditions which may make it difficult to properly troubleshoot a kernel problem. For example, a proprietary driver can cause problems that cannot be debugged reliably because its source code is not available and its effects cannot be determined. Likewise, if a serious kernel or hardware error had previously occurred, the integrity of the kernel space may have been compromised, meaning that any subsequent debug messages generated by the kernel may not be reliable.
Note that correcting the tainting condition alone does not remove the taint state because doing so does not change the fact that the kernel can no longer be relied on to work correctly or produce accurate debugging information. The system must be restarted to clear the taint flags.
More information is available in the Linux kernel documentation, including what each taint flag means and how to troubleshoot a tainted kernel prior to reporting bugs.
A partial list of conditions that can result in the kernel being tainted follows, each with their own flags. Note that some Linux vendors, such as SUSE, add additional taint flags to indicate conditions such as loading a module that is supported by a third party rather than directly by the vendor.

Loading a proprietary (or non-GPL-compatible) kernel module. As noted above, this is the most common reason for the kernel to become tainted.
The use of staging drivers, which are part of the kernel source code but are experimental and not fully tested.
The use of out-of-tree modules that are not included with the Linux kernel source code.
Forcibly loading or unloading modules. This can happen if one is trying to use a module that is not built for the current version of the kernel. (The Linux kernel module ABI is not stable across versions, or even differently-configured builds of the same version.)
Running a kernel on certain hardware configurations that are specifically not supported, such as an SMP (multiprocessor) kernel on early AMD Athlon processors not supporting SMP operation.
Overriding the ACPI DSDT in the kernel. This is sometimes needed to correct for firmware power-management bugs; see this Arch Linux wiki article for details.
Certain critical error conditions, such as machine check exceptions and kernel oopses.
Certain serious bugs in the BIOS, UEFI, or other system firmware which the kernel must work around.

**参考链接**: https://unix.stackexchange.com/questions/118116/what-is-a-tainted-linux-kernel

> 📎 来源 / Source: https://unix.stackexchange.com/questions/118116/what-is-a-tainted-linux-kernel

#### 98. ssh-add returns with: &quot;Error connecting to agent: No such file or directory&quot;

**故障现象**: ssh-add returns with: &quot;Error connecting to agent: No such file or directory&quot;
**标签 / 来源**: Tags: linux, ssh, ssh-agent | unix | 👍 133 | 💬 5 answers

**问题描述**:
Tags: linux, ssh, ssh-agent | Score: 133 | Views: 264530 | Answers: 5

**解决方法 / 社区答案**:
The client tool ssh-add wants to communicate with the background process ssh-agent. You need to start the ssh-agent process first. On Linux, a shell uses the environment variables SSH_AUTH_SOCK and SSH_AGENT_PID to identify the correct process to talk to.
You can start ssh-agent in multiple ways.
Either by starting a new shell
ssh-agent bash

or by evaluating the script returned by ssh-agent in your current shell.
eval &quot;$(ssh-agent)&quot;

I suggest using the second method, because you keep all your history and variables.

**参考链接**: https://unix.stackexchange.com/questions/464574/ssh-add-returns-with-error-connecting-to-agent-no-such-file-or-directory

> 📎 来源 / Source: https://unix.stackexchange.com/questions/464574/ssh-add-returns-with-error-connecting-to-agent-no-such-file-or-directory

#### 99. How to check which GPU is active in Linux?

**故障现象**: How to check which GPU is active in Linux?
**标签 / 来源**: Tags: linux, hardware, graphics | unix | 👍 133 | 💬 12 answers

**问题描述**:
Tags: linux, hardware, graphics | Score: 133 | Views: 454435 | Answers: 12

**解决方法 / 社区答案**:
I've just gone through a hell of a time
trying to get my discrete graphics to work in Ubuntu,
and answering this question was constantly a challenge,
since the lspci method mentioned earlier
can sometimes say that both are [VGA controller].
I think the following command should give you an indication of your active chip:
$ glxinfo | grep -E &quot;OpenGL vendor|OpenGL renderer&quot;
OpenGL vendor string: Intel Open Source Technology Center
OpenGL renderer string: Mesa DRI Intel(R) Sandybridge Mobile

For me, this is telling me that my Intel graphics are running the show.
glxinfo is available from the mesa-utils package,
so you will need to install it if you haven't already. 
On Ubuntu 22.04, for example, run:
sudo apt-get install mesa-utils

If you're using an NVIDIA chip, and you're using the bumblebee package,
you can put optirun in front of that line,
and it should tell you that you're running the NVIDIA chip
(optirun is basically telling the computer
to use the discrete chip to run whatever command follows,
but everything else is still using the integrated chip).
$ optirun glxinfo | grep -E &quot;OpenGL vendor|OpenGL renderer&quot;
OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: GeForce GT 555M/PCIe/SSE2

glxheads is another helpful command from mesa-utils that tells you
some useful information about which graphics card is in use
(mostly repeats glxinfo in a more compact and easy-to-read form, though),
and it gives you a nice rendering of a rotating triangle.

**参考链接**: https://unix.stackexchange.com/questions/16407/how-to-check-which-gpu-is-active-in-linux

> 📎 来源 / Source: https://unix.stackexchange.com/questions/16407/how-to-check-which-gpu-is-active-in-linux

#### 100. What&#39;s the difference between /usr/lib/systemd/system and /etc/systemd/system?

**故障现象**: What&#39;s the difference between /usr/lib/systemd/system and /etc/systemd/system?
**标签 / 来源**: Tags: debian, ubuntu, centos, systemd | unix | 👍 133 | 💬 3 answers

**问题描述**:
Tags: debian, ubuntu, centos, systemd | Score: 133 | Views: 116937 | Answers: 3

**解决方法 / 社区答案**:
This question is already answered in man 7 file-hierarchy which comes with systemd (there is also online version):

        /etc
           System-specific configuration.
 (…)
 VENDOR-SUPPLIED OPERATING SYSTEM RESOURCES
       /usr
            Vendor-supplied operating system resources. 
            Usually read-only, but this is not required. Possibly 
            shared between multiple hosts. This directory should not
            be modified by the administrator, except when installing 
            or removing vendor-supplied packages.


Basically, files that ships in packages downloaded from distribution repository go into /usr/lib/systemd/. Modifications done by system administrator (user) go into /etc/systemd/system/. 

System-specific units override units supplied by vendors. Using drop-ins, you can override only specific parts of unit files, leaving the rest to vendor (drop-ins are available since the very beginning of systemd, but were properly documented only in v219; see man systemd.unit).

**参考链接**: https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system

> 📎 来源 / Source: https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system


---

## English 🇺🇸
**Linux Common Issues & Solutions**

Auto-updated hourly from Stack Exchange: common LINUX issues and community-verified solutions.

### LINUX Common Issues & Solutions

#### 1. How do I make `ls` show file sizes in megabytes?

**Issue**: How do I make `ls` show file sizes in megabytes?
**Tags / Source**: Tags: linux, ls | unix | 👍 936 | 💬 2 answers

**Description**:
Tags: linux, ls | Score: 936 | Views: 2451284 | Answers: 2

**Solution / Community Answer**:
ls -l --block-size=M will give you a long format listing (needed to actually see the file size) and round file sizes up to the nearest MiB.

If you want MB (10^6 bytes) rather than MiB (2^20 bytes) units, use --block-size=MB instead.

If you don't want the M suffix attached to the file size, you can use something like --block-size=1M. Thanks Stéphane Chazelas for suggesting this.

If you simply want file sizes in "reasonable" units, rather than specifically megabytes, then you can use -lh to get a long format listing and human readable file size presentation. This will use units of file size to keep file sizes presented with about 1-3 digits (so you'll see file sizes like 6.1K, 151K, 7.1M, 15M, 1.5G and so on.

The --block-size parameter is described in the man page for ls; man ls and search for SIZE. It allows for units other than MB/MiB as well, and from the looks of it (I didn't try that) arbitrary block sizes as well (so you could see the file size as a number of 429-byte blocks if you want to).

Note that both --block-size and -h are GNU extensions on top of the Open Group's ls, so this may not work if you don't have a GNU userland (which most Linux installations do). The ls from GNU Coreutils 8.5 does support --block-size and -h as described above. Thanks to kojiro for pointing this out.

**Reference**: https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

> 📎 Source: https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

#### 2. Finding the PID of the process using a specific port?

**Issue**: Finding the PID of the process using a specific port?
**Tags / Source**: Tags: linux, process, ip, netstat | unix | 👍 831 | 💬 8 answers

**Description**:
Tags: linux, process, ip, netstat | Score: 831 | Views: 2194654 | Answers: 8

**Solution / Community Answer**:
Your existing command doesn't work because Linux requires you to either be root or the owner of the process to get the information you desire.
On modern systems, ss is the appropriate tool to use to get this information:
$ sudo ss -lptn 'sport = :80'
State   Local Address:Port  Peer Address:Port              
LISTEN  127.0.0.1:80        *:*                users:((&quot;nginx&quot;,pid=125004,fd=12))
LISTEN  ::1:80              :::*               users:((&quot;nginx&quot;,pid=125004,fd=11))

You can also use the same invocation you're currently using, but you must first elevate with sudo:
$ sudo netstat -nlp | grep :80
tcp  0  0  0.0.0.0:80  0.0.0.0:*  LISTEN  125004/nginx

You can also use lsof:
$ sudo lsof -n -i :80 | grep LISTEN
nginx   125004 nginx    3u  IPv4   6645      0t0  TCP 0.0.0.0:80 (LISTEN)

**Reference**: https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port

> 📎 Source: https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port

#### 3. Why am I still getting a password prompt with ssh with public key authentication?

**Issue**: Why am I still getting a password prompt with ssh with public key authentication?
**Tags / Source**: Tags: ubuntu, centos, ssh, sshd, key-authentication | unix | 👍 745 | 💬 32 answers

**Description**:
Tags: ubuntu, centos, ssh, sshd, key-authentication | Score: 745 | Views: 1428794 | Answers: 32

**Solution / Community Answer**:
Make sure the permissions on the ~/.ssh directory and its contents are proper. When I first set up my ssh key auth, I didn't have the ~/.ssh folder properly set up, and it yelled at me.


Your home directory ~, your ~/.ssh directory and the ~/.ssh/authorized_keys file on the remote machine must be writable only by you: rwx------ and rwxr-xr-x are fine, but rwxrwx--- is no good¹, even if you are the only user in your group (if you prefer numeric modes: 700 or 755, not 775).
If ~/.ssh or authorized_keys is a symbolic link, the canonical path (with symbolic links expanded) is checked.
Your ~/.ssh/authorized_keys file (on the remote machine) must be readable (at least 400), but you'll need it to be also writable (600) if you will add any more keys to it.
Your private key file (on the local machine) must be readable and writable only by you: rw-------, i.e. 600.
Also, if SELinux is set to enforcing, you may need to run restorecon -R -v ~/.ssh (see e.g. Ubuntu bug 965663 and Debian bug report #658675; this is patched in CentOS 6).


¹  Except on some distributions (Debian and derivatives) which have patched the code to allow group writability if you are the only user in your group.

**Reference**: https://unix.stackexchange.com/questions/36540/why-am-i-still-getting-a-password-prompt-with-ssh-with-public-key-authentication

> 📎 Source: https://unix.stackexchange.com/questions/36540/why-am-i-still-getting-a-password-prompt-with-ssh-with-public-key-authentication

#### 4. How can I resolve a hostname to an IP address in a Bash script?

**Issue**: How can I resolve a hostname to an IP address in a Bash script?
**Tags / Source**: Tags: linux, bash, networking, dns | unix | 👍 635 | 💬 29 answers

**Description**:
Tags: linux, bash, networking, dns | Score: 635 | Views: 995011 | Answers: 29

**Solution / Community Answer**:
You can use getent, which comes with glibc (so you almost certainly have it on Linux). This resolves using gethostbyaddr/gethostbyname2, and so also will check /etc/hosts/NIS/etc:

getent hosts unix.stackexchange.com | awk '{ print $1 }'


Or, as Heinzi said below, you can use dig with the +short argument (queries DNS servers directly, does not look at /etc/hosts/NSS/etc) :

dig +short unix.stackexchange.com


If dig +short is unavailable, any one of the following should work. All of these query DNS directly and ignore other means of resolution:

host unix.stackexchange.com | awk '/has address/ { print $4 }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 }'


If you want to only print one IP, then add the exit command to awk's workflow.

dig +short unix.stackexchange.com | awk '{ print ; exit }'
getent hosts unix.stackexchange.com | awk '{ print $1 ; exit }'
host unix.stackexchange.com | awk '/has address/ { print $4 ; exit }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 ; exit }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 ; exit }'

**Reference**: https://unix.stackexchange.com/questions/20784/how-can-i-resolve-a-hostname-to-an-ip-address-in-a-bash-script

> 📎 Source: https://unix.stackexchange.com/questions/20784/how-can-i-resolve-a-hostname-to-an-ip-address-in-a-bash-script

#### 5. Execute vs Read bit. How do directory permissions in Linux work?

**Issue**: Execute vs Read bit. How do directory permissions in Linux work?
**Tags / Source**: Tags: linux, permissions, directory | unix | 👍 536 | 💬 9 answers

**Description**:
Tags: linux, permissions, directory | Score: 536 | Views: 403915 | Answers: 9

**Solution / Community Answer**:
When applying permissions to directories on Linux, the permission bits have different meanings than on regular files.


The read bit (r) allows the affected user to list the files within the directory
The write bit (w) allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes
The execute bit (x) allows the affected user to enter the directory, and access files and directories inside
The sticky bit (T, or t if the execute bit is set for others) states that files and directories within that directory may only be deleted or renamed by their owner (or root)

**Reference**: https://unix.stackexchange.com/questions/21251/execute-vs-read-bit-how-do-directory-permissions-in-linux-work

> 📎 Source: https://unix.stackexchange.com/questions/21251/execute-vs-read-bit-how-do-directory-permissions-in-linux-work

#### 6. How to know whether Wayland or X11 is being used

**Issue**: How to know whether Wayland or X11 is being used
**Tags / Source**: Tags: linux, x11, wayland | unix | 👍 514 | 💬 15 answers

**Description**:
Tags: linux, x11, wayland | Score: 514 | Views: 702757 | Answers: 15

**Solution / Community Answer**:
Obtain the session ID to pass in by issuing:
loginctl

That will show you something like:
SESSION  UID USER          SEAT  TTY
     c2 1000 yourusername  seat0    

1 sessions listed.

In that example, c2 is the session ID.
Then:
loginctl show-session &lt;SESSION_ID&gt; -p Type

If you want all this on a single command:
loginctl show-session $(awk '/tty/ {print $1}' &lt;(loginctl)) -p Type | awk -F= '{print $2}'

Use the one corresponding to your user name.
Refer to:
https://fedoraproject.org/wiki/How_to_debug_Wayland_problems
So, for me, I can see Wayland is in use:
$ loginctl show-session c2 -p Type                                                  
Type=wayland

**Reference**: https://unix.stackexchange.com/questions/202891/how-to-know-whether-wayland-or-x11-is-being-used

> 📎 Source: https://unix.stackexchange.com/questions/202891/how-to-know-whether-wayland-or-x11-is-being-used

#### 7. Compress a folder with tar?

**Issue**: Compress a folder with tar?
**Tags / Source**: Tags: linux, backup, tar | unix | 👍 505 | 💬 2 answers

**Description**:
Tags: linux, backup, tar | Score: 505 | Views: 1359515 | Answers: 2

**Solution / Community Answer**:
To tar and gzip a folder, the syntax is:
tar czf name_of_archive_file.tar.gz name_of_directory_to_tar

Adding - before the options (czf) is optional with tar. The effect of czf is as follows:

c — create an archive file (as opposed to extract, which is x)
f — filename of the archive file
z — filter archive through gzip (remove this option to create a .tar file)

If you want to tar the current directory, use . to designate that.
To construct filenames dynamically, use the date utility (look at its man page for the available format options). For example:
cd /var/www &amp;&amp;
tar czf ~/www_backups/$(date +%Y%m%d-%H%M%S).tar.gz .

This will create a file named something like 20120902-185558.tar.gz.
On Linux, chances are your tar also supports BZip2 compression with the j rather than z option. And possibly others. Check the man page on your local system.

**Reference**: https://unix.stackexchange.com/questions/46969/compress-a-folder-with-tar

> 📎 Source: https://unix.stackexchange.com/questions/46969/compress-a-folder-with-tar

#### 8. When should I not kill -9 a process?

**Issue**: When should I not kill -9 a process?
**Tags / Source**: Tags: linux, command-line, kill, process-management | unix | 👍 436 | 💬 9 answers

**Description**:
Tags: linux, command-line, kill, process-management | Score: 436 | Views: 209582 | Answers: 9

**Solution / Community Answer**:
Generally, you should use kill (short for kill -s TERM, or on most systems kill -15) before kill -9 (kill -s KILL) to give the target process a chance to clean up after itself.  (Processes can't catch or ignore SIGKILL, but they can and often do catch SIGTERM.)  If you don't give the process a chance to finish what it's doing and clean up, it may leave corrupted files (or other state) around that it won't be able to understand once restarted.

strace/truss, ltrace and gdb are generally good ideas for looking at why a stuck process is stuck.   (truss -u on Solaris is particularly helpful; I find ltrace too often presents arguments to library calls in an unusable format.)  Solaris also has useful /proc-based tools, some of which have been ported to Linux.  (pstack is often helpful).

**Reference**: https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process

> 📎 Source: https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process

#### 9. How do you empty the buffers and cache on a Linux system?

**Issue**: How do you empty the buffers and cache on a Linux system?
**Tags / Source**: Tags: linux, kernel, performance, cache, ram | unix | 👍 419 | 💬 1 answers

**Description**:
Tags: linux, kernel, performance, cache, ram | Score: 419 | Views: 985960 | Answers: 1

**Solution / Community Answer**:
Emptying the buffers cache
If you ever want to empty it you can use this chain of commands.
# free &amp;&amp; sync &amp;&amp; echo 3 &gt; /proc/sys/vm/drop_caches &amp;&amp; free

             total       used       free     shared    buffers     cached
Mem:       1018916     980832      38084          0      46924     355764
-/+ buffers/cache:     578144     440772
Swap:      2064376        128    2064248
             total       used       free     shared    buffers     cached
Mem:       1018916     685008     333908          0        224     108252
-/+ buffers/cache:     576532     442384
Swap:      2064376        128    2064248

You can signal the Linux Kernel to drop various aspects of cached items by changing the numeric argument to the above command.

To free pagecache:
# echo 1 &gt; /proc/sys/vm/drop_caches


To free dentries and inodes:
# echo 2 &gt; /proc/sys/vm/drop_caches


To free pagecache, dentries and inodes:
# echo 3 &gt; /proc/sys/vm/drop_caches



The above are meant to be run as root. If you're trying to do them using sudo then you'll need to change the syntax slightly to something like these:
$ sudo sh -c 'echo 1 &gt;/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 2 &gt;/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 3 &gt;/proc/sys/vm/drop_caches'

NOTE: There's a more esoteric version of the above command if you're into that:
$ echo &quot;echo 1 &gt; /proc/sys/vm/drop_caches&quot; | sudo sh

Why the change in syntax? The /bin/echo program is running as root, because of sudo, but the shell that's redirecting echo's output to the root-only file is still running as you. Your current shell does the redirection before sudo starts.
Seeing what's in the buffers and cache
Take a look at linux-ftools if you'd like to analyze the contents of the buffers &amp; cache. Specifically if you'd like to see what files are currently being cached.
fincore
With this tool you can see what files are being cached within a give directory.
fincore [options] files...

  --pages=false      Do not print pages
  --summarize        When comparing multiple files, print a summary report
  --only-cached      Only print stats for files that are actually in cache.

For example, /var/lib/mysql/blogindex:
root@xxxxxx:/var/lib/mysql/blogindex# fincore --pages=false --summarize --only-cached * 
stats for CLUSTER_LOG_2010_05_21.MYI: file size=93840384 , total pages=22910 , cached pages=1 , cached size=4096, cached perc=0.004365 
stats for CLUSTER_LOG_2010_05_22.MYI: file size=417792 , total pages=102 , cached pages=1 , cached size=4096, cached perc=0.980392 
stats for CLUSTER_LOG_2010_05_23.MYI: file size=826368 , total pages=201 , cached pages=1 , cached size=4096, cached perc=0.497512 
stats for CLUSTER_LOG_2010_05_24.MYI: file size=192512 , total pages=47 , cached pages=1 , cached size=4096, cached perc=2.127660 
stats for CLUSTER_LOG_2010_06_03.MYI: file size=345088 , total pages=84 , cached pages=43 , cached size=176128, cached perc=51.190476 
stats for CLUSTER_LOG_2010_06_04.MYD: file size=1478552 , total pages=360 , cached pages=97 , cached size=397312, cached perc=26.944444 
stats for CLUSTER_LOG_2010_06_04.MYI: file size=205824 , total pages=50 , cached pages=29 , cached size=118784, cached perc=58.000000 
stats for COMMENT_CONTENT_2010_06_03.MYI: file size=100051968 , total pages=24426 , cached pages=10253 , cached size=41996288, cached perc=41.975764 
stats for COMMENT_CONTENT_2010_06_04.MYD: file size=716369644 , total pages=174894 , cached pages=79821 , cached size=326946816, cached perc=45.639645 
stats for COMMENT_CONTENT_2010_06_04.MYI: file size=56832000 , total pages=13875 , cached pages=5365 , cached size=21975040, cached perc=38.666667 
stats for FEED_CONTENT_2010_06_03.MYI: file size=1001518080 , total pages=244511 , cached pages=98975 , cached size=405401600, cached perc=40.478751 
stats for FEED_CONTENT_2010_06_04.MYD: file size=9206385684 , total pages=2247652 , cached pages=1018661 , cached size=4172435456, cached perc=45.321117 
stats for FEED_CONTENT_2010_06_04.MYI: file size=638005248 , total pages=155763 , cached pages=52912 , cached size=216727552, cached perc=33.969556 
stats for FEED_CONTENT_2010_06_04.frm: file size=9840 , total pages=2 , cached pages=3 , cached size=12288, cached perc=150.000000 
stats for PERMALINK_CONTENT_2010_06_03.MYI: file size=1035290624 , total pages=252756 , cached pages=108563 , cached size=444674048, cached perc=42.951700 
stats for PERMALINK_CONTENT_2010_06_04.MYD: file size=55619712720 , total pages=13579031 , cached pages=6590322 , cached size=26993958912, cached perc=48.533080 
stats for PERMALINK_CONTENT_2010_06_04.MYI: file size=659397632 , total pages=160985 , cached pages=54304 , cached size=222429184, cached perc=33.732335 
stats for PERMALINK_CONTENT_2010_06_04.frm: file size=10156 , total pages=2 , cached pages=3 , cached size=12288, cached perc=150.000000 
---
total cached size: 32847278080

With the above output you can see that there are several *.MYD, *.MYI, and *.frm files that are currently being cached.
Swap
If you want to clear out your swap you can use the following commands.
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7298164     689328          0      30416     457936
-/+ buffers/cache:    6809812    1177680
Swap:      5963772     609452    5354320

Then use this command to disable swap:
$ swapoff -a

You can confirm that it's now empty:
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7777912     209580          0      39332     489864
-/+ buffers/cache:    7248716     738776
Swap:            0          0          0

And to re-enable it:
$ swapon -a

And now reconfirm with free:
$ free
             total       used       free     shared    buffers     cached
Mem:       7987492    7785572     201920          0      41556     491508
-/+ buffers/cache:    7252508     734984
Swap:      5963772          0    5963772

**Reference**: https://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system

> 📎 Source: https://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system

#### 10. How to check OS and version using a Linux command

**Issue**: How to check OS and version using a Linux command
**Tags / Source**: Tags: linux, shell | unix | 👍 400 | 💬 3 answers

**Description**:
Tags: linux, shell | Score: 400 | Views: 1968359 | Answers: 3

**Solution / Community Answer**:
Kernel Version

If you want kernel version information, use uname(1). For example:

$ uname -a
Linux localhost 3.11.0-3-generic #8-Ubuntu SMP Fri Aug 23 16:49:15 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux


Distribution Information

If you want distribution information, it will vary depending on your distribution and whether your system supports the Linux Standard Base. Some ways to check, and some example output, are immediately below.

$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu Saucy Salamander (development branch)
Release:    13.10
Codename:   saucy

$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=13.10
DISTRIB_CODENAME=saucy
DISTRIB_DESCRIPTION="Ubuntu Saucy Salamander (development branch)"

$ cat /etc/issue.net
Ubuntu Saucy Salamander (development branch)

$ cat /etc/debian_version 
wheezy/sid

**Reference**: https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command

> 📎 Source: https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command

#### 11. How to list all files ordered by size

**Issue**: How to list all files ordered by size
**Tags / Source**: Tags: linux, files, ls | unix | 👍 386 | 💬 14 answers

**Description**:
Tags: linux, files, ls | Score: 386 | Views: 734387 | Answers: 14

**Solution / Community Answer**:
Simply use something like:

ls -lS /path/to/folder/


Capital S. 

This will sort files by size. 

Also see:

man ls

-S     sort by file size


If you want to sort in reverse order, just add -r switch.

Update:

To exclude directories (and provided none of the file names or symlink targets contain newline characters):

ls -lS | grep -v '^d' 


Update 2:

I see now how it still shows symbolic links, which could be folders. Symbolic links always start with a letter l, as in link.  

Change the command to filter for a -. This should only leave regular files:

ls -lS | grep '^-'


On my system this only shows regular files. 

update 3:

To add recursion, I would leave the sorting of the lines to the sort command and tell it to use the 5th column to sort on. 

ls -lR | grep '^-' | sort -k 5 -rn


-rn means Reverse and numeric to get the biggest files at the top. Down side of this command is that it does not show the full path of the files.

If you do need the full path of the files, use something like this:

find . -type f  -exec du -h {} + | sort -r -h


The find command will recursively find all files in all sub directories of . and call du -h (meaning disk usage -humanreadable) and then sort the output again. If your find/sort doesn't support -h, replace with du -k and sort -rn. Note that size and disk usage are not the same thing.

**Reference**: https://unix.stackexchange.com/questions/53737/how-to-list-all-files-ordered-by-size

> 📎 Source: https://unix.stackexchange.com/questions/53737/how-to-list-all-files-ordered-by-size

#### 12. How to know number of cores of a system in Linux?

**Issue**: How to know number of cores of a system in Linux?
**Tags / Source**: Tags: linux, cpu | unix | 👍 384 | 💬 12 answers

**Description**:
Tags: linux, cpu | Score: 384 | Views: 815327 | Answers: 12

**Solution / Community Answer**:
To get a complete picture you need to look at the number of threads per core, cores per socket and sockets. If you multiply these numbers you will get the number of CPUs on your system.


  CPUs = Threads per core X cores per socket X sockets


CPUs are what you see when you run htop (these do not equate to physical CPUs).

Here is an example from a desktop machine:

$ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
CPU(s):                8
Thread(s) per core:    2
Core(s) per socket:    4
Socket(s):             1


And a server:

$ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
CPU(s):                32
Thread(s) per core:    2
Core(s) per socket:    8
Socket(s):             2


The output of nproc corresponds to the CPU count from lscpu. For the desktop machine above this should match the 8 CPU(s) reported by lscpu:

$ nproc --all
8


The output of /proc/cpuinfo should match this information, for example on the desktop system above we can see there are 8 processors (CPUs) and 4 cores (core id 0-3):

$ grep -E 'processor|core id' /proc/cpuinfo
processor   : 0
core id     : 0
processor   : 1
core id     : 0
processor   : 2
core id     : 1
processor   : 3
core id     : 1
processor   : 4
core id     : 2
processor   : 5
core id     : 2
processor   : 6
core id     : 3
processor   : 7
core id     : 3


The cpu cores reported by /proc/cpuinfo corresponds to the Core(s) per socket reported by lscpu. For the desktop machine above this should match the 4 Core(s) per socket reported by lscpu:

$ grep -m 1 'cpu cores' /proc/cpuinfo
cpu cores   : 4


To specifically answer your question you tell how many cores you have by multiplying the number of cores you have per socket by the number of sockets you have.


  Cores = Cores per socket X Sockets


For the example systems above the desktop has 4 cores:

$ echo "Cores = $(( $(lscpu | awk '/^Socket\(s\)/{ print $2 }') * $(lscpu | awk '/^Core\(s\) per socket/{ print $4 }') ))"
Cores = 4


While the server has 16:

$ echo "Cores = $(( $(lscpu | awk '/^Socket\(s\)/{ print $2 }') * $(lscpu | awk '/^Core\(s\) per socket/{ print $4 }') ))"
Cores = 16


Another useful utility is dmidecode which outputs per socket information. In the case of the server system listed above we expect to see 8 cores per socket and 16 threads per socket:

$ sudo dmidecode -t 4 | grep -E 'Socket Designation|Count'
    Socket Designation: CPU1
    Core Count: 8
    Thread Count: 16
    Socket Designation: CPU2
    Core Count: 8
    Thread Count: 16


The lscpu command has a number of useful options that you may like to check out, for example:

$ lscpu --all --extended
$ lscpu --all --parse=CPU,SOCKET,CORE | grep -v '^#'


See man lscpu for details.

In summary:


You need to be aware of sockets, cores and threads
You need to be careful of the term CPU as it means different things in different contexts

**Reference**: https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux

#### 13. How to set default file permissions for all folders/files in a directory?

**Issue**: How to set default file permissions for all folders/files in a directory?
**Tags / Source**: Tags: linux, permissions, directory | unix | 👍 379 | 💬 5 answers

**Description**:
Tags: linux, permissions, directory | Score: 379 | Views: 714957 | Answers: 5

**Solution / Community Answer**:
I found it: Applying default permissions
From the article:

Set the setgid bit, so that files/folder under &lt;directory&gt; will be created with the same group as &lt;directory&gt;
chmod g+s &lt;directory&gt;


Set the default ACLs for the group and other
setfacl -d -m g::rwx /&lt;directory&gt;
setfacl -d -m o::rx /&lt;directory&gt;



Next we can verify:
getfacl /&lt;directory&gt;

Output:
# file: ../&lt;directory&gt;/
# owner: &lt;user&gt;
# group: media
# flags: -s-
user::rwx
group::rwx
other::r-x
default:user::rwx
default:group::rwx
default:other::r-x

**Reference**: https://unix.stackexchange.com/questions/1314/how-to-set-default-file-permissions-for-all-folders-files-in-a-directory

> 📎 Source: https://unix.stackexchange.com/questions/1314/how-to-set-default-file-permissions-for-all-folders-files-in-a-directory

#### 14. How can I monitor disk io?

**Issue**: How can I monitor disk io?
**Tags / Source**: Tags: linux, disk | unix | 👍 378 | 💬 11 answers

**Description**:
Tags: linux, disk | Score: 378 | Views: 1059519 | Answers: 11

**Solution / Community Answer**:
For disk I/O trending there are a few options. My personal favorite is the sar command from sysstat. By default, it gives output like this:

09:25:01 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
09:35:01 AM     all      0.11      0.00      0.01      0.00      0.00     99.88
09:45:01 AM     all      0.12      0.00      0.01      0.00      0.00     99.86
09:55:01 AM     all      0.09      0.00      0.01      0.00      0.00     99.90
10:05:01 AM     all      0.10      0.00      0.01      0.02      0.01     99.86
Average:        all      0.19      0.00      0.02      0.00      0.01     99.78


The %iowait is the time spent waiting on I/O. Using the Debian package, you must enable the stat collector via the /etc/default/sysstat config file after package installation.

To see current utilization broken out by device, you can use the iostat command, also from the sysstat package:

$ iostat -x 1
Linux 3.5.2-x86_64-linode26 (linode)    11/08/2012      _x86_64_        (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.84    0.00    0.08    1.22    0.07   97.80

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
xvda              0.09     1.02    2.58    0.49   112.79    12.11    40.74     0.15   48.56   3.88   1.19
xvdb              1.39     0.43    4.03    1.82    43.33    18.43    10.56     0.66  112.73   1.93   1.13


Some other options that can show disk usage in trending graphs is munin and cacti.

**Reference**: https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io

> 📎 Source: https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io

#### 15. Change the Python3 default version in Ubuntu

**Issue**: Change the Python3 default version in Ubuntu
**Tags / Source**: Tags: ubuntu, python, python3 | unix | 👍 378 | 💬 10 answers

**Description**:
Tags: ubuntu, python, python3 | Score: 378 | Views: 1239818 | Answers: 10

**Solution / Community Answer**:
From the comment: 

sudo update-alternatives --config python


Will show you an error:

update-alternatives: error: no alternatives for python3 


You need to update your update-alternatives , then you will be able to set your default python version.

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2


Then run :

sudo update-alternatives --config python


Set python3.6 as default. 

Or use the following command to set python3.6 as default:

sudo update-alternatives  --set python /usr/bin/python3.6

**Reference**: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

> 📎 Source: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

#### 16. How can I update to a newer version of Git using apt-get?

**Issue**: How can I update to a newer version of Git using apt-get?
**Tags / Source**: Tags: ubuntu, apt, upgrade, git | unix | 👍 360 | 💬 5 answers

**Description**:
Tags: ubuntu, apt, upgrade, git | Score: 360 | Views: 464951 | Answers: 5

**Solution / Community Answer**:
Here are the commands you need to run, if you just want to get it done:
sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com A1715D88E1DF1F24 40976EAF437D05B5 3B4FE6ACC0B21F32 A6616109451BBBF2
sudo apt-get update
sudo apt-get install git -y
git --version

As of Dec 2018, I got git 2.20.1 that way, while the version in the Ubuntu Xenial repositories was 2.7.4.
If your system doesn't have add-apt-repository, you can install it via:
sudo apt-get install python-software-properties software-properties-common

**Reference**: https://unix.stackexchange.com/questions/33617/how-can-i-update-to-a-newer-version-of-git-using-apt-get

> 📎 Source: https://unix.stackexchange.com/questions/33617/how-can-i-update-to-a-newer-version-of-git-using-apt-get

#### 17. How can I get my external IP address in a shell script?

**Issue**: How can I get my external IP address in a shell script?
**Tags / Source**: Tags: linux, shell-script, ip | unix | 👍 355 | 💬 27 answers

**Description**:
Tags: linux, shell-script, ip | Score: 355 | Views: 497757 | Answers: 27

**Solution / Community Answer**:
I'd recommend getting it directly from a DNS server.
Most of the other answers below all involve going over HTTP to a remote server. Some of them required parsing of the output, or relied on the User-Agent header to make the server respond in plain text. Those change quite frequently (go down, change their name, put up ads, might change output format etc.).

The DNS response protocol is standardised (the format will stay compatible).
Historically, DNS services (Akamai, Google Public DNS, OpenDNS, ..) tend to survive much longer and are more stable, more scalable, and generally more looked-after than whatever new hip whatismyip dot-com HTTP service is hot today.
This method is inherently faster (be it only by a few milliseconds!).

Using dig with an OpenDNS resolver:
$ dig @resolver4.opendns.com myip.opendns.com +short

Perhaps alias it in your bashrc so it's easy to remember
# https://unix.stackexchange.com/a/81699/37512
alias wanip='dig @resolver4.opendns.com myip.opendns.com +short' 
alias wanip4='dig @resolver4.opendns.com myip.opendns.com +short -4'
alias wanip6='dig @resolver1.ipv6-sandbox.opendns.com AAAA myip.opendns.com +short -6'

Responds with a plain ip address:
$ wanip # wanip4, or wanip6
80.100.192.168 # or, 2606:4700:4700::1111

How it works
The dig command.
(Abbreviated from https://ss64.com/bash/dig.html. You can read this anytime via man dig):
usage:  dig [@global-dnsserver] [q-type] &lt;hostname&gt; &lt;d-opt&gt; [q-opt]

    q-type   one of (A, ANY, AAAA, TXT, MX, ...). Default: A.

    d-opt    ...
             +[no]short          (Display nothing except short form of answer)
             ...

    q-opt    one of:
             -4                  (use IPv4 query transport only)
             -6                  (use IPv6 query transport only)
             ...

The ANY query type returns either an AAAA or an A record. To prefer IPv4 or IPv6 connection specifically, use the -4 or -6 options accordingly.
To require the response be an IPv4 address, replace ANY with A; for IPv6, replace it with AAAA. Note that it can only return the address used for the connection. For example, when connecting over IPv6, it cannot return the A address.
Alternative servers
Various DNS providers offer this service, including OpenDNS, Akamai, and Google Public DNS:
# OpenDNS (since 2009)
$ dig @resolver3.opendns.com myip.opendns.com +short
$ dig @resolver4.opendns.com myip.opendns.com +short
80.100.192.168

# OpenDNS IPv6
$ dig @resolver1.ipv6-sandbox.opendns.com AAAA myip.opendns.com +short -6
2606:4700:4700::1111

# Akamai (since 2009)
$ dig @ns1-1.akamaitech.net ANY whoami.akamai.net +short
80.100.192.168

# Akamai approximate
# NOTE: This returns only an approximate IP from your block,
# but has the benefit of working even when behind private DNS proxies.
$ dig +short TXT whoami.ds.akahelp.net
&quot;ip&quot; &quot;80.100.192.160&quot;

# Google (since 2010)
# Supports IPv6 + IPv4, use -4 or -6 to force one.
$ dig @ns1.google.com TXT o-o.myaddr.l.google.com +short
&quot;80.100.192.168&quot;

Example alias that specifically requests an IPv4 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip4='dig @resolver4.opendns.com myip.opendns.com +short -4'

$ wanip4
80.100.192.168

And for your IPv6 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip6='dig @ns1.google.com TXT o-o.myaddr.l.google.com +short -6'

$ wanip6
&quot;2606:4700:4700::1111&quot;

Troubleshooting
If the command is not working for some reason, there may be a network problem. Try one of the alternatives above first.
If you suspect a different issue (with the upstream provider, the command-line tool, or something else) then run the command without the +short option to reveal the details of the DNS query. For example:
$ dig @resolver4.opendns.com myip.opendns.com

;; Got answer: -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR

;; QUESTION SECTION:
;myip.opendns.com.      IN  A

;; ANSWER SECTION:
myip.opendns.com.   0   IN  A   80.100.192.168

;; Query time: 4 msec

**Reference**: https://unix.stackexchange.com/questions/22615/how-can-i-get-my-external-ip-address-in-a-shell-script

> 📎 Source: https://unix.stackexchange.com/questions/22615/how-can-i-get-my-external-ip-address-in-a-shell-script

#### 18. how can I recursively delete empty directories in my home directory?

**Issue**: how can I recursively delete empty directories in my home directory?
**Tags / Source**: Tags: linux, filesystems, find, rm | unix | 👍 318 | 💬 2 answers

**Description**:
Tags: linux, filesystems, find, rm | Score: 318 | Views: 291415 | Answers: 2

**Solution / Community Answer**:
The find command is the primary tool for recursive file system operations.
Use the -type d expression to tell find you're interested in finding directories only (and not plain files). The GNU version of find supports the -empty test, so

$ find . -type d -empty -print


will print all empty directories below your current directory.

Use find ~ -… or find "$HOME" -… to base the search on your home directory (if it isn't your current directory).

After you've verified that this is selecting the correct directories, use -delete to delete all matches:

$ find . -type d -empty -delete

**Reference**: https://unix.stackexchange.com/questions/46322/how-can-i-recursively-delete-empty-directories-in-my-home-directory

> 📎 Source: https://unix.stackexchange.com/questions/46322/how-can-i-recursively-delete-empty-directories-in-my-home-directory

#### 19. How do I find out what hard disks are in the system?

**Issue**: How do I find out what hard disks are in the system?
**Tags / Source**: Tags: linux, hardware, devices, hard-disk | unix | 👍 313 | 💬 16 answers

**Description**:
Tags: linux, hardware, devices, hard-disk | Score: 313 | Views: 1391062 | Answers: 16

**Solution / Community Answer**:
This is highly platform-dependent. Also different methods may treat edge cases differently (“fake” disks of various kinds, RAID volumes, …).

On modern udev installations, there are symbolic links to storage media in subdirectories of /dev/disk, that let you look up a disk or a partition by serial number (/dev/disk/by-id/), by UUID (/dev/disk/by-uuid), by filesystem label (/dev/disk/by-label/) or by hardware connectivity (/dev/disk/by-path/).

Under Linux 2.6, each disk and disk-like device has an entry in /sys/block. Under Linux since the dawn of time, disks and partitions are listed in /proc/partitions. Alternatively, you can use lshw: lshw -class disk.

Linux also provides the lsblk utility which displays a nice tree view of the storage volumes (since util-linux 2.19, not present on embedded devices with BusyBox).

If you have an fdisk or disklabel utility, it might be able to tell you what devices it's able to work on.

You will find utility names for many unix variants on the Rosetta Stone for Unix, in particular the “list hardware configuration” and “read a disk label” lines.

**Reference**: https://unix.stackexchange.com/questions/4561/how-do-i-find-out-what-hard-disks-are-in-the-system

> 📎 Source: https://unix.stackexchange.com/questions/4561/how-do-i-find-out-what-hard-disks-are-in-the-system

#### 20. How to display meminfo in megabytes in top?

**Issue**: How to display meminfo in megabytes in top?
**Tags / Source**: Tags: linux, memory, top, meminfo | unix | 👍 309 | 💬 9 answers

**Description**:
Tags: linux, memory, top, meminfo | Score: 309 | Views: 477597 | Answers: 9

**Solution / Community Answer**:
When in top, typing capital "E" cycles through different memory units (KiB, MiB, GiB, etc., which are different from kB, MB and GB) in the total memory info:



While lower-case "e" does the same individual process lines:



From the manpage:

2c. MEMORY Usage
    This  portion  consists of two lines which may express values in kibibytes
    (KiB) through exbibytes (EiB) depending on  the  scaling  factor  enforced
    with the 'E' interactive command.


Version Information: top -version: procps-ng version 3.3.9
System: CentOS 7

**Reference**: https://unix.stackexchange.com/questions/105908/how-to-display-meminfo-in-megabytes-in-top

> 📎 Source: https://unix.stackexchange.com/questions/105908/how-to-display-meminfo-in-megabytes-in-top

#### 21. linux: How can I view all UUIDs for all available disks on my system?

**Issue**: linux: How can I view all UUIDs for all available disks on my system?
**Tags / Source**: Tags: linux, storage | unix | 👍 303 | 💬 13 answers

**Description**:
Tags: linux, storage | Score: 303 | Views: 1002566 | Answers: 13

**Solution / Community Answer**:
There's a tool called blkid (use it as root or with sudo), 

# blkid /dev/sda1
/dev/sda1: LABEL="/" UUID="ee7cf0a0-1922-401b-a1ae-6ec9261484c0" SEC_TYPE="ext2" TYPE="ext3"


you can check this link for more info

**Reference**: https://unix.stackexchange.com/questions/658/linux-how-can-i-view-all-uuids-for-all-available-disks-on-my-system

> 📎 Source: https://unix.stackexchange.com/questions/658/linux-how-can-i-view-all-uuids-for-all-available-disks-on-my-system

#### 22. How to know if a disk is an SSD or an HDD

**Issue**: How to know if a disk is an SSD or an HDD
**Tags / Source**: Tags: linux, hard-disk, block-device, ssd | unix | 👍 302 | 💬 10 answers

**Description**:
Tags: linux, hard-disk, block-device, ssd | Score: 302 | Views: 448329 | Answers: 10

**Solution / Community Answer**:
Linux automatically detects SSD, and since kernel version 2.6.29, you may verify sda with:
cat /sys/block/sda/queue/rotational

You should get 1 for hard disks and 0 for a SSD.
It will probably not work if your disk is a logical device emulated by hardware (like a RAID controller).
See this answer for more information about SSD partitioning, filesystem...

**Reference**: https://unix.stackexchange.com/questions/65595/how-to-know-if-a-disk-is-an-ssd-or-an-hdd

> 📎 Source: https://unix.stackexchange.com/questions/65595/how-to-know-if-a-disk-is-an-ssd-or-an-hdd

#### 23. Efficiently delete large directory containing thousands of files

**Issue**: Efficiently delete large directory containing thousands of files
**Tags / Source**: Tags: linux, command-line, files, rm | unix | 👍 297 | 💬 24 answers

**Description**:
Tags: linux, command-line, files, rm | Score: 297 | Views: 507561 | Answers: 24

**Solution / Community Answer**:
Using rsync is surprising fast and simple.
mkdir empty_dir
rsync -a --delete empty_dir/    yourdirectory/

@sarath's answer mentioned another fast choice: Perl! 
Its benchmarks are faster than rsync -a --delete.
cd yourdirectory
perl -e 'for(&lt;*&gt;){((stat)[9]&lt;(unlink))}'

or, without the stat (it's debatable whether it is needed;
some say that may be faster with it, and others say it's faster without it):
cd yourdirectory
perl -e 'for(&lt;*&gt;){unlink}'

Sources:

https://stackoverflow.com/questions/1795370/unix-fast-remove-directory-for-cleaning-up-daily-builds
http://www.slashroot.in/which-is-the-fastest-method-to-delete-files-in-linux
https://www.quora.com/Linux-why-stat+unlink-can-be-faster-than-a-single-unlink/answer/Kent-Fredric?srid=O9EW&amp;share=1

**Reference**: https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

> 📎 Source: https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

#### 24. What do the flags in /proc/cpuinfo mean?

**Issue**: What do the flags in /proc/cpuinfo mean?
**Tags / Source**: Tags: linux, cpu, arm, x86 | unix | 👍 283 | 💬 6 answers

**Description**:
Tags: linux, cpu, arm, x86 | Score: 283 | Views: 215281 | Answers: 6

**Solution / Community Answer**:
x86
(32-bit a.k.a. i386–i686 and 64-bit a.k.a. amd64. In other words, your workstation, laptop or server.)
FAQ: Do I have…

64-bit (x86_64/AMD64/Intel64)? lm
Hardware virtualization (VMX/AMD-V)? vmx (Intel), svm (AMD)
Accelerated AES (AES-NI)? aes
TXT (TPM)? smx
a hypervisor (announced as such)? hypervisor

Most of the other features are only of interest to compiler or kernel authors.
All the flags
The full listing is in the kernel source, in the file arch/x86/include/asm/cpufeatures.h.
Intel-defined CPU features, CPUID level 0x00000001 (edx)
See also Wikipedia and table 2-27 in Intel Advanced Vector Extensions Programming Reference

fpu: Onboard FPU (floating point support)
vme: Virtual 8086 mode enhancements
de: Debugging Extensions (CR4.DE)
pse: Page Size Extensions (4MB memory pages)
tsc: Time Stamp Counter (RDTSC)
msr: Model-Specific Registers (RDMSR, WRMSR)
pae: Physical Address Extensions (support for more than 4GB of RAM)
mce: Machine Check Exception
cx8: CMPXCHG8 instruction (64-bit compare-and-swap)
apic: Onboard APIC
sep: SYSENTER/SYSEXIT
mtrr: Memory Type Range Registers
pge: Page Global Enable (global bit in PDEs and PTEs)
mca: Machine Check Architecture
cmov: CMOV instructions (conditional move) (also FCMOV)
pat: Page Attribute Table
pse36: 36-bit PSEs (huge pages)
pn: Processor serial number
clflush: Cache Line Flush instruction
dts: Debug Store (buffer for debugging and profiling instructions)
acpi: ACPI via MSR (temperature monitoring and clock speed modulation)
mmx: Multimedia Extensions
fxsr: FXSAVE/FXRSTOR, CR4.OSFXSR
sse: Intel SSE vector instructions
sse2: SSE2
ss: CPU self snoop
ht: Hyper-Threading and/or multi-core
tm: Automatic clock control (Thermal Monitor)
ia64: Intel Itanium Architecture 64-bit (not to be confused with Intel's 64-bit x86 architecture with flag x86-64 or &quot;AMD64&quot; bit indicated by flag lm)
pbe: Pending Break Enable (PBE# pin) wakeup support

AMD-defined CPU features, CPUID level 0x80000001
See also Wikipedia and table 2-23 in Intel Advanced Vector Extensions Programming Reference

syscall: SYSCALL (Fast System Call) and SYSRET (Return From Fast System Call)
mp: Multiprocessing Capable.
nx: Execute Disable
mmxext: AMD MMX extensions
fxsr_opt: FXSAVE/FXRSTOR optimizations
pdpe1gb: One GB pages (allows hugepagesz=1G)
rdtscp: Read Time-Stamp Counter and Processor ID
lm: Long Mode (x86-64: amd64, also known as Intel 64, i.e. 64-bit capable)
3dnowext: AMD 3DNow! extensions
3dnow: 3DNow! (AMD vector instructions, competing with Intel's SSE1)

Transmeta-defined CPU features, CPUID level 0x80860001

recovery: CPU in recovery mode
longrun: Longrun power control
lrti: LongRun table interface

Other features, Linux-defined mapping

cxmmx: Cyrix MMX extensions
k6_mtrr: AMD K6 nonstandard MTRRs
cyrix_arr: Cyrix ARRs (= MTRRs)
centaur_mcr: Centaur MCRs (= MTRRs)
constant_tsc: TSC ticks at a constant rate
up: SMP kernel running on UP
art: Always-Running Timer
arch_perfmon: Intel Architectural PerfMon
pebs: Precise-Event Based Sampling
bts: Branch Trace Store
rep_good: rep microcode works well
acc_power: AMD accumulated power mechanism
nopl: The NOPL (0F 1F) instructions
xtopology: cpu topology enum extensions
tsc_reliable: TSC is known to be reliable
nonstop_tsc: TSC does not stop in C states
cpuid: CPU has CPUID instruction itself
extd_apicid: has extended APICID (8 bits)
amd_dcm: multi-node processor
aperfmperf: APERFMPERF
eagerfpu: Non lazy FPU restore
nonstop_tsc_s3: TSC doesn't stop in S3 state
tsc_known_freq: TSC has known frequency
mce_recovery: CPU has recoverable machine checks

Intel-defined CPU features, CPUID level 0x00000001 (ecx)
See also Wikipedia and table 2-26 in Intel Advanced Vector Extensions Programming Reference

pni: SSE-3 (“Prescott New Instructions”)
pclmulqdq: Perform a Carry-Less Multiplication of Quadword instruction — accelerator for GCM)
dtes64: 64-bit Debug Store
monitor: Monitor/Mwait support (Intel SSE3 supplements)
ds_cpl: CPL Qual. Debug Store
vmx: Hardware virtualization: Intel VMX
smx: Safer mode: TXT (TPM support)
est: Enhanced SpeedStep
tm2: Thermal Monitor 2
ssse3: Supplemental SSE-3
cid: Context ID
sdbg: silicon debug
fma: Fused multiply-add
cx16: CMPXCHG16B
xtpr: Send Task Priority Messages
pdcm: Performance Capabilities
pcid: Process Context Identifiers
dca: Direct Cache Access
sse4_1: SSE-4.1
sse4_2: SSE-4.2
x2apic: x2APIC
movbe: Move Data After Swapping Bytes instruction
popcnt: Return the Count of Number of Bits Set to 1 instruction (Hamming weight, i.e. bit count)
tsc_deadline_timer: Tsc deadline timer
aes/aes-ni: Advanced Encryption Standard (New Instructions)
xsave: Save Processor Extended States: also provides XGETBY,XRSTOR,XSETBY
avx: Advanced Vector Extensions
f16c: 16-bit fp conversions (CVT16)
rdrand: Read Random Number from hardware random number generator instruction
hypervisor: Running on a hypervisor

VIA/Cyrix/Centaur-defined CPU features, CPUID level 0xC0000001

rng: Random Number Generator present (xstore)
rng_en: Random Number Generator enabled
ace: on-CPU crypto (xcrypt)
ace_en: on-CPU crypto enabled
ace2: Advanced Cryptography Engine v2
ace2_en: ACE v2 enabled
phe: PadLock Hash Engine
phe_en: PHE enabled
pmm: PadLock Montgomery Multiplier
pmm_en: PMM enabled

More extended AMD flags: CPUID level 0x80000001, ecx

lahf_lm: Load AH from Flags (LAHF) and Store AH into Flags (SAHF) in long mode
cmp_legacy: If yes HyperThreading not valid
svm: “Secure virtual machine”: AMD-V
extapic: Extended APIC space
cr8_legacy: CR8 in 32-bit mode
abm: Advanced Bit Manipulation
sse4a: SSE-4A
misalignsse: indicates if a general-protection exception (#GP) is generated when some legacy SSE instructions operate on unaligned data. Also depends on CR0 and Alignment Checking bit
3dnowprefetch: 3DNow prefetch instructions
osvw: indicates OS Visible Workaround, which allows the OS to work around processor errata.
ibs: Instruction Based Sampling
xop: extended AVX instructions
skinit: SKINIT/STGI instructions
wdt: Watchdog timer
lwp: Light Weight Profiling
fma4: 4 operands MAC instructions
tce: translation cache extension
nodeid_msr: NodeId MSR
tbm: Trailing Bit Manipulation
topoext: Topology Extensions CPUID leafs
perfctr_core: Core Performance Counter Extensions
perfctr_nb: NB Performance Counter Extensions
bpext: data breakpoint extension
ptsc: performance time-stamp counter
perfctr_l2: L2 Performance Counter Extensions
mwaitx: MWAIT extension (MONITORX/MWAITX)

Auxiliary flags: Linux defined - For features scattered in various CPUID levels

ring3mwait: Ring 3 MONITOR/MWAIT
cpuid_fault: Intel CPUID faulting
cpb: AMD Core Performance Boost
epb: IA32_ENERGY_PERF_BIAS support
cat_l3: Cache Allocation Technology L3
cat_l2: Cache Allocation Technology L2
cdp_l3: Code and Data Prioritization L3
invpcid_single: effectively invpcid and CR4.PCIDE=1
hw_pstate: AMD HW-PState
proc_feedback: AMD ProcFeedbackInterface
sme: AMD Secure Memory Encryption
pti: Kernel Page Table Isolation (Kaiser)
retpoline: Retpoline mitigation for Spectre variant 2 (indirect branches)
retpoline_amd: AMD Retpoline mitigation
intel_ppin: Intel Processor Inventory Number
avx512_4vnniw: AVX-512 Neural Network Instructions
avx512_4fmaps: AVX-512 Multiply Accumulation Single precision
mba: Memory Bandwidth Allocation
rsb_ctxsw: Fill RSB on context switches

Virtualization flags: Linux defined

tpr_shadow: Intel TPR Shadow
vnmi: Intel Virtual NMI
flexpriority: Intel FlexPriority
ept: Intel Extended Page Table
vpid: Intel Virtual Processor ID
vmmcall: prefer VMMCALL to VMCALL

Intel-defined CPU features, CPUID level 0x00000007:0 (ebx)

fsgsbase: {RD/WR}{FS/GS}BASE instructions
tsc_adjust: TSC adjustment MSR
bmi1: 1st group bit manipulation extensions
hle: Hardware Lock Elision
avx2: AVX2 instructions
smep: Supervisor Mode Execution Protection
bmi2: 2nd group bit manipulation extensions
erms: Enhanced REP MOVSB/STOSB
invpcid: Invalidate Processor Context ID
rtm: Restricted Transactional Memory
cqm: Cache QoS Monitoring
mpx: Memory Protection Extension
rdt_a: Resource Director Technology Allocation
avx512f: AVX-512 foundation
avx512dq: AVX-512 Double/Quad instructions
rdseed: The RDSEED instruction
adx: The ADCX and ADOX instructions
smap: Supervisor Mode Access Prevention
avx512ifma: AVX-512 Integer Fused Multiply Add instructions
clflushopt: CLFLUSHOPT instruction
clwb: CLWB instruction
intel_pt: Intel Processor Tracing
avx512pf: AVX-512 Prefetch
avx512er: AVX-512 Exponential and Reciprocal
avx512cd: AVX-512 Conflict Detection
sha_ni: SHA1/SHA256 Instruction Extensions
avx512bw: AVX-512 Byte/Word instructions
avx512vl: AVX-512 128/256 Vector Length extensions

Extended state features, CPUID level 0x0000000d:1 (eax)

xsaveopt: Optimized XSAVE
xsavec: XSAVEC
xgetbv1: XGETBV with ECX = 1
xsaves: XSAVES/XRSTORS

Intel-defined CPU QoS sub-leaf, CPUID level 0x0000000F:0 (edx)

cqm_llc: LLC QoS

Intel-defined CPU QoS sub-leaf, CPUID level 0x0000000F:1 (edx)

cqm_occup_llc: LLC occupancy monitoring
cqm_mbm_total: LLC total MBM monitoring
cqm_mbm_local: LLC local MBM monitoring

AMD-defined CPU features, CPUID level 0x80000008 (ebx)

clzero: CLZERO instruction
irperf: instructions retired performance counter
xsaveerptr: Always save/restore FP error pointers

Thermal and Power Management leaf, CPUID level 0x00000006 (eax)

dtherm (formerly dts): digital thermal sensor
ida: Intel Dynamic Acceleration
arat: Always Running APIC Timer
pln: Intel Power Limit Notification
pts: Intel Package Thermal Status
hwp: Intel Hardware P-states
hwp_notify: HWP notification
hwp_act_window: HWP Activity Window
hwp_epp: HWP Energy Performance Preference
hwp_pkg_req: HWP package-level request

AMD SVM Feature Identification, CPUID level 0x8000000a (edx)

npt: AMD Nested Page Table support
lbrv: AMD LBR Virtualization support
svm_lock: AMD SVM locking MSR
nrip_save: AMD SVM next_rip save
tsc_scale: AMD TSC scaling support
vmcb_clean: AMD VMCB clean bits support
flushbyasid: AMD flush-by-ASID support
decodeassists: AMD Decode Assists support
pausefilter: AMD filtered pause intercept
pfthreshold: AMD pause filter threshold
avic: Virtual Interrupt Controller
vmsave_vmload: Virtual VMSAVE VMLOAD
vgif: Virtual GIF

Intel-defined CPU features, CPUID level 0x00000007:0 (ecx)

avx512vbmi: AVX512 Vector Bit Manipulation instructions
umip: User Mode Instruction Protection
pku: Protection Keys for Userspace
ospke: OS Protection Keys Enable
avx512_vbmi2: Additional AVX512 Vector Bit Manipulation instructions
gfni: Galois Field New Instructions
vaes: Vector AES
vpclmulqdq: Carry-Less Multiplication Double Quadword
avx512_vnni: Vector Neural Network Instructions
avx512_bitalg: VPOPCNT[B,W] and VPSHUF-BITQMB instructions
avx512_vpopcntdq: POPCNT for vectors of DW/QW
la57: 5-level page tables
rdpid: RDPID instruction

AMD-defined CPU features, CPUID level 0x80000007 (ebx)

overflow_recov: MCA overflow recovery support
succor: uncorrectable error containment and recovery
smca: Scalable MCA

Detected CPU bugs (Linux-defined)

f00f: Intel F00F
fdiv: CPU FDIV
coma: Cyrix 6x86 coma
amd_tlb_mmatch: tlb_mmatch AMD Erratum 383
amd_apic_c1e: apic_c1e AMD Erratum 400
11ap: Bad local APIC aka 11AP
fxsave_leak: FXSAVE leaks FOP/FIP/FOP
clflush_monitor: AAI65, CLFLUSH required before MONITOR
sysret_ss_attrs: SYSRET doesn't fix up SS attrs
espfix: &quot;&quot; IRET to 16-bit SS corrupts ESP/RSP high bits
null_seg: Nulling a selector preserves the base
swapgs_fence: SWAPGS without input dep on GS
monitor: IPI required to wake up remote CPU
amd_e400: CPU is among the affected by Erratum 400
cpu_meltdown: CPU is affected by meltdown attack and needs kernel page table isolation
spectre_v1: CPU is affected by Spectre variant 1 attack with conditional branches
spectre_v2: CPU is affected by Spectre variant 2 attack with indirect branches
spec_store_bypass: CPU is affected by the Speculative Store Bypass vulnerability (Spectre variant 4).

 P.S.
This listing was derived from arch/x86/include/asm/cpufeatures.h in the kernel source. The flags are listed in the same order as the source code. Please help by adding links to descriptions of features when they're missing, by writing a short description of features that have an unexpressive names, and by updating the list for new kernel versions. The current list is from Linux 4.15 plus some later additions.

**Reference**: https://unix.stackexchange.com/questions/43539/what-do-the-flags-in-proc-cpuinfo-mean

> 📎 Source: https://unix.stackexchange.com/questions/43539/what-do-the-flags-in-proc-cpuinfo-mean

#### 25. Kernel inotify watch limit reached

**Issue**: Kernel inotify watch limit reached
**Tags / Source**: Tags: linux, kernel, inotify | unix | 👍 282 | 💬 2 answers

**Description**:
Tags: linux, kernel, inotify | Score: 282 | Views: 226436 | Answers: 2

**Solution / Community Answer**:
Is it safe to raise that value and what would be the consequences of a too high value?

Yes, it's safe to raise that value and below are the possible costs [source]:


Each used inotify watch takes up 540 bytes (32-bit system), or 1 kB (double - on 64-bit) [sources: 1, 2]
This comes out of kernel memory, which is unswappable.
Assuming you set the max at 524288 and all were used (improbable), you'd be using approximately 256MB/512MB of 32-bit/64-bit kernel memory.


Note that your application will also use additional memory to keep track of the inotify handles, file/directory paths, etc. -- how much depends on its design.



To check the max number of inotify watches:

cat /proc/sys/fs/inotify/max_user_watches


To set max number of inotify watches

Temporarily:


Run sudo sysctl fs.inotify.max_user_watches= with your preferred value at the end.


Permanently (more detailed info):


put fs.inotify.max_user_watches=524288 into your sysctl settings. Depending on your system they might be in one of the following places:


Debian/RedHat: /etc/sysctl.conf
Arch: put a new file into /etc/sysctl.d/, e.g. /etc/sysctl.d/40-max-user-watches.conf

you may wish to reload the sysctl settings to avoid a reboot: sysctl -p (Debian/RedHat) or sysctl --system (Arch)


Check to see if the max number of inotify watches have been reached:

Use tail with the -f (follow) option on any old file, e.g. tail -f /var/log/dmesg:
  - If all is well, it will show the last 10 lines and pause; abort with Ctrl-C
  - If you are out of watches, it will fail with this somewhat cryptic error:
   tail: cannot watch '/var/log/dmsg': No space left on device

To see what's using up inotify watches

find /proc/*/fd -lname anon_inode:inotify |
   cut -d/ -f3 |
   xargs -I '{}' -- ps --no-headers -o '%p %U %c' -p '{}' |
   uniq -c |
   sort -nr


The first column indicates the number of inotify fds (not the number of watches though) and the second shows the PID of that process [sources: 1, 2].

**Reference**: https://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached

> 📎 Source: https://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached

#### 26. Difference between cp -r and cp -a

**Issue**: Difference between cp -r and cp -a
**Tags / Source**: Tags: linux, cp, recursive | unix | 👍 276 | 💬 3 answers

**Description**:
Tags: linux, cp, recursive | Score: 276 | Views: 593565 | Answers: 3

**Solution / Community Answer**:
Recursive means that cp copies the contents of directories, and if a directory has subdirectories they are copied (recursively) too. Without -R, the cp command skips directories. -r is identical with -R on Linux, it differs in some edge cases on some other unix variants.

By default, cp creates a new file which has the same content as the old file, and the same permissions but restricted by the umask; the copy is dated from the time of the copy, and belongs to the user doing the copy. With the -p option, the copy has the same modification time, the same access time, and the same permissions as the original. It also has the same owner and group as the original, if the user doing the copy has the permission to create such files.

The -a option means -R and -p, plus a few other preservation options. It attempts to make a copy that's as close to the original as possible: same directory tree, same file types, same contents, same metadata (times, permissions, extended attributes, etc.).

**Reference**: https://unix.stackexchange.com/questions/44967/difference-between-cp-r-and-cp-a

> 📎 Source: https://unix.stackexchange.com/questions/44967/difference-between-cp-r-and-cp-a

#### 27. Linux &quot;top&quot; command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?

**Issue**: Linux &quot;top&quot; command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?
**Tags / Source**: Tags: linux, cpu, top | unix | 👍 273 | 💬 3 answers

**Description**:
Tags: linux, cpu, top | Score: 273 | Views: 460225 | Answers: 3

**Solution / Community Answer**:
hi is the time spent processing hardware interrupts. Hardware interrupts are generated by hardware devices (network cards, keyboard controller, external timer, hardware sensors, ...) when they need to signal something to the CPU (data has arrived, for example).

Since these can happen very frequently, and since they essentially block the current CPU while they are running, kernel hardware interrupt handlers are written to be as fast and simple as possible.

If long or complex processing needs to be done, these tasks are deferred using a mechanism call softirqs. These are scheduled independently, can run on any CPU, can even run concurrently (none of that is true of hardware interrupt handlers).

The part about hard IRQs blocking the current CPU, and the part about softirqs being able to run anywhere are not exactly correct, there can be limitations, and some hard IRQs can interrupt others.


As an example, a "data received" hardware interrupt from a network card could simply store the information "card ethX needs to be serviced" somewhere and schedule a softirq. The softirq would be the thing that triggers the actual packet routing.

si represents the time spent in these softirqs.

A good read about the softirq mechanism (with a bit of history too) is Matthew Wilcox's I'll Do It Later: Softirqs, Tasklets, Bottom Halves, Task Queues,
Work Queues and Timers (PDF, 64k).

st, "steal time", is only relevant in virtualized environments. It represents time when the real CPU was not available to the current virtual machine — it was "stolen" from that VM by the hypervisor (either to run another VM, or for its own needs).

The CPU time accounting  document from IBM has more information about steal time, and CPU accounting in virtualized environments. (It's aimed at zSeries type hardware, but the general idea is the same for most platforms.)

**Reference**: https://unix.stackexchange.com/questions/18918/linux-top-command-what-are-us-sy-ni-id-wa-hi-si-and-st-for-cpu-usage

> 📎 Source: https://unix.stackexchange.com/questions/18918/linux-top-command-what-are-us-sy-ni-id-wa-hi-si-and-st-for-cpu-usage

#### 28. How to get the complete and exact list of mounted filesystems in Linux?

**Issue**: How to get the complete and exact list of mounted filesystems in Linux?
**Tags / Source**: Tags: linux, filesystems, mount | unix | 👍 264 | 💬 5 answers

**Description**:
Tags: linux, filesystems, mount | Score: 264 | Views: 1131824 | Answers: 5

**Solution / Community Answer**:
The definitive list of mounted filesystems is in /proc/mounts.

If you have any form of containers on your system, /proc/mounts only lists the filesystems that are in your present container. For example, in a chroot, /proc/mounts lists only the filesystems whose mount point is within the chroot. (There are ways to escape the chroot, mind.)

There's also a list of mounted filesystems in /etc/mtab. This list is maintained by the mount and umount commands. That means that if you don't use these commands (which is pretty rare), your action (mount or unmount) won't be recorded. In practice, it's mostly in a chroot that you'll find /etc/mtab files that differ wildly from the state of the system. Also, mounts performed in the chroot will be reflected in the chroot's /etc/mtab but not in the main /etc/mtab. Actions performed while /etc/mtab is on a read-only filesystem are also not recorded there.

The reason why you'd sometimes want to consult /etc/mtab in preference to or in addition to /proc/mounts is that because it has access to the mount command line, it's sometimes able to present information in a way that's easier to understand; for example you see mount options as requested (whereas /proc/mounts lists the mount and kernel defaults as well), and bind mounts appear as such in /etc/mtab.

**Reference**: https://unix.stackexchange.com/questions/24182/how-to-get-the-complete-and-exact-list-of-mounted-filesystems-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/24182/how-to-get-the-complete-and-exact-list-of-mounted-filesystems-in-linux

#### 29. Limit memory usage for a single Linux process

**Issue**: Limit memory usage for a single Linux process
**Tags / Source**: Tags: linux, memory, ulimit | unix | 👍 263 | 💬 12 answers

**Description**:
Tags: linux, memory, ulimit | Score: 263 | Views: 436683 | Answers: 12

**Solution / Community Answer**:
Another way to limit this is to use Linux's control groups.  This is especially useful if you want to limit a process's (or group of processes') allocation of physical memory distinctly from virtual memory.  For example:
cgcreate -g memory:myGroup
echo 500M &gt; /sys/fs/cgroup/memory/myGroup/memory.limit_in_bytes
echo 5G &gt; /sys/fs/cgroup/memory/myGroup/memory.memsw.limit_in_bytes

will create a control group named myGroup, cap the set of processes run under myGroup up to 500 MB of physical memory with memory.limit_in_bytes and up to 5000 MB of physical and swap memory together with memory.memsw.limit_in_bytes.
More info about these options can be found here: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-memory
To run a process under the control group:
cgexec -g memory:myGroup pdftoppm

Note that on a modern Ubuntu distribution this example requires installing the cgroup-tools package (previously cgroup-bin):
sudo apt install cgroup-tools

and editing /etc/default/grub to change GRUB_CMDLINE_LINUX_DEFAULT to:
GRUB_CMDLINE_LINUX_DEFAULT=&quot;cgroup_enable=memory swapaccount=1&quot;

and then running sudo update-grub and rebooting to boot with the new kernel boot parameters.

**Reference**: https://unix.stackexchange.com/questions/44985/limit-memory-usage-for-a-single-linux-process

> 📎 Source: https://unix.stackexchange.com/questions/44985/limit-memory-usage-for-a-single-linux-process

#### 30. What does aux mean in `ps aux`?

**Issue**: What does aux mean in `ps aux`?
**Tags / Source**: Tags: linux, ps | unix | 👍 260 | 💬 4 answers

**Description**:
Tags: linux, ps | Score: 260 | Views: 542983 | Answers: 4

**Solution / Community Answer**:
a = show processes for all users
u = display the process's user/owner
x = also show processes not attached to a terminal

By the way, man ps is a good resource.

Historically, BSD and AT&amp;T developed incompatible versions of ps.  The options without a leading dash (as per the question) are the BSD style while those with a leading dash are AT&amp;T Unix style.  On top of this, Linux developed a version which supports both styles and then adds to it a third style with options that begin with double dashes.

All (or nearly all) non-embedded Linux distributions use a variant of the procps suite.  The above options are as defined in the procps ps man page.

In the comments, you say you are using Apple MacOS (OSX, I presume).  The OSX man page for ps is here and it shows support only for AT&amp;T style.

**Reference**: https://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux

> 📎 Source: https://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux

#### 31. mount: wrong fs type, bad option, bad superblock

**Issue**: mount: wrong fs type, bad option, bad superblock
**Tags / Source**: Tags: ubuntu, mount, fdisk | unix | 👍 259 | 💬 21 answers

**Description**:
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622634 | Answers: 21

**Solution / Community Answer**:
WARNING: This will wipe out your drive!

You still need to create a (new) file system (aka &quot;format the partition&quot;). 
Double-check that you really want to overwrite the current content of the specified partition! Replace XY accordingly, but double check that you are specifying the correct partition, e.g., sda2, sdb1:

mkfs.ext4 /dev/sdXY

parted / mkpart does not create a file system. 
The Parted User's Manual shows:

2.4.5 mkpart
Command: mkpart [part-type fs-type name] start end
Creates a new partition,
without creating a new file system on that partition.

    [Emphasis added.]

**Reference**: https://unix.stackexchange.com/questions/315063/mount-wrong-fs-type-bad-option-bad-superblock

> 📎 Source: https://unix.stackexchange.com/questions/315063/mount-wrong-fs-type-bad-option-bad-superblock

#### 32. How can I get distribution name and version number in a simple shell script?

**Issue**: How can I get distribution name and version number in a simple shell script?
**Tags / Source**: Tags: linux, shell-script, distributions | unix | 👍 257 | 💬 21 answers

**Description**:
Tags: linux, shell-script, distributions | Score: 257 | Views: 364821 | Answers: 21

**Solution / Community Answer**:
To get OS and VER, the latest standard seems to be /etc/os-release. 
 Before that, there was lsb_release and /etc/lsb-release.  Before that, you had to look for different files for each distribution.

Here's what I'd suggest

if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release &gt;/dev/null 2&gt;&amp;1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    ...
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    ...
else
    # Fall back to uname, e.g. "Linux &lt;version&gt;", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi


I think uname to get ARCH is still the best way.  But the example you gave obviously only handles Intel systems.  I'd either call it BITS like this:

case $(uname -m) in
x86_64)
    BITS=64
    ;;
i*86)
    BITS=32
    ;;
*)
    BITS=?
    ;;
esac


Or change ARCH to be the more common, yet unambiguous versions: x86 and x64 or similar:

case $(uname -m) in
x86_64)
    ARCH=x64  # or AMD64 or Intel64 or whatever
    ;;
i*86)
    ARCH=x86  # or IA32 or Intel32 or whatever
    ;;
*)
    # leave ARCH as-is
    ;;
esac


but of course that's up to you.

**Reference**: https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script

> 📎 Source: https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script

#### 33. How can I edit multiple files in Vim?

**Issue**: How can I edit multiple files in Vim?
**Tags / Source**: Tags: linux, command-line, vim, files | unix | 👍 253 | 💬 11 answers

**Description**:
Tags: linux, command-line, vim, files | Score: 253 | Views: 353754 | Answers: 11

**Solution / Community Answer**:
First of all, in vim you can enter : (colon) and then help help, ala :help for a list of self-help topics, including a short tutorial. Within the list of topics, move your cursor over the topic of interest and then press ctrl] and that topic will be opened.
A good place for you to start would be the topic
|usr_07.txt|  Editing more than one file

Ok, on to your answer.
After starting vim with a list of files, you can move to the next file by entering :next or :n for short.
:wnext is short for write current changes and then move to next file; :wn is an abbreviation for :wnext.
There's also an analogous :previous, :wprevious and :Next. (Note that :p is shorthand for :print. The shorthand for :previous is :prev or :N.)
To see where you are in the file list, enter :args and the file currently being edited will appear in [] (brackets).
Example:
vim foo.txt bar.txt
:args

result:
[foo.txt] bar.txt

**Reference**: https://unix.stackexchange.com/questions/27586/how-can-i-edit-multiple-files-in-vim

> 📎 Source: https://unix.stackexchange.com/questions/27586/how-can-i-edit-multiple-files-in-vim

#### 34. How to determine Linux kernel architecture?

**Issue**: How to determine Linux kernel architecture?
**Tags / Source**: Tags: linux, command-line, x86, cpu-architecture | unix | 👍 247 | 💬 14 answers

**Description**:
Tags: linux, command-line, x86, cpu-architecture | Score: 247 | Views: 751761 | Answers: 14

**Solution / Community Answer**:
i386 and i686 are both 32-bit.
x86_64 is 64-bit  

example for 64 bit:  

behrooz@behrooz:~$ uname -a  
Linux behrooz 2.6.32-5-amd64 #1 SMP Mon Mar 7 21:35:22 UTC 2011 **x86_64** GNU/Linux


EDIT:
See is my linux ARM 32 or 64 bit? for ARM

**Reference**: https://unix.stackexchange.com/questions/12453/how-to-determine-linux-kernel-architecture

> 📎 Source: https://unix.stackexchange.com/questions/12453/how-to-determine-linux-kernel-architecture

#### 35. How can get a list of all scheduled cron jobs on my machine?

**Issue**: How can get a list of all scheduled cron jobs on my machine?
**Tags / Source**: Tags: linux, cron, scheduling | unix | 👍 246 | 💬 4 answers

**Description**:
Tags: linux, cron, scheduling | Score: 246 | Views: 603353 | Answers: 4

**Solution / Community Answer**:
With most Crons (e.g. Vixie-Cron - Debian/Ubuntu default, Cronie - Fedora default, Solaris Cron ...) you get the list of scheduled cron jobs for the current user via:

$ crontab -l


or for another user via

# crontab -l -u juser


To get the crontabs for all users you can loop over all users and call this command.

Alternatively, you can look up the spool files. Usually, they are are saved under /var/spool/cron, e.g. for vcron following directory

/var/spool/cron/crontabs


contains all the configured crontabs of all users - except the root user who is also able to configure jobs via the system-wide crontab, which is located at

/etc/crontab


With cronie (default on Fedora/CentOS), there is a .d style config directory for system cron jobs, as well:

/etc/cron.d


(As always, the .d directory simplifies maintaining configuration entries that are part of different packages.)

For convenience, most distributions also provide a directories where linked/stored scripts are periodically executed, e.g.:

/etc/cron.daily
/etc/cron.hourly
/etc/cron.monthly
/etc/cron.weekly


The timely execution of those scripts is usually managed via run-parts entries in the system crontab or via anacron.

With Systemd (e.g. on Fedora, CentOS 7, ...) periodic job execution can additionally be configured via timer units. The enabled system timers can be displayed via:

$ systemctl list-timers


Note that users beside root may have user systemd instances running where timers are configured, as well. For example, on Fedora, by default, a user systemd instance is started for each user that is currently logged in. They can be recognized via:

$ ps aux | grep 'systemd[ ]--user'


Those user timers can be listed via:

$ systemctl --user list-timers


An alternative to issuing the list-timers command is to search for timer unit files (pattern: *.timer) and symbolic links to them in the usual system and user systemd config directories:

$ find /usr/lib/systemd/ /etc/systemd -name '*.timer'
$ find /home '(' -path '/home/*/.local/share/systemd/user/*' \
              -o -path '/home/*/.config/systemd/*' ')' \
      -name '*.timer'  2&gt; /dev/null


(As with normal service units, a timer unit is enabled via creating a symbolic link in the right systemd config directory.)

See also:


ArchWiki article on Cron
ArchWiki article on Systemd Timers

**Reference**: https://unix.stackexchange.com/questions/7053/how-can-get-a-list-of-all-scheduled-cron-jobs-on-my-machine

> 📎 Source: https://unix.stackexchange.com/questions/7053/how-can-get-a-list-of-all-scheduled-cron-jobs-on-my-machine

#### 36. How to download portion of video with youtube-dl command?

**Issue**: How to download portion of video with youtube-dl command?
**Tags / Source**: Tags: linux, youtube-dl | unix | 👍 243 | 💬 22 answers

**Description**:
Tags: linux, youtube-dl | Score: 243 | Views: 300449 | Answers: 22

**Solution / Community Answer**:
I don't believe youtube-dl alone will do what you want. However you can combine it with a command line utility like ffmpeg.

First acquire the actual URL using youtube-dl:

youtube-dl -g "https://www.youtube.com/watch?v=V_f2QkBdbRI"


Copy the output of the command and paste it as part of the -i parameter of the next command:

ffmpeg -ss 00:00:15.00 -i "OUTPUT-OF-FIRST URL" -t 00:00:10.00 -c copy out.mp4


The -ss parameter in this position states to discard all input up until 15 seconds into the video. The -t option states to capture for 10 seconds. The rest of the command tells it to store as an mp4.

ffmpeg is a popular tool and should be in any of the popular OS repositories/package managers.

**Reference**: https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command

> 📎 Source: https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command

#### 37. How can I see dmesg output as it changes?

**Issue**: How can I see dmesg output as it changes?
**Tags / Source**: Tags: linux, command-line, logs, dmesg | unix | 👍 243 | 💬 7 answers

**Description**:
Tags: linux, command-line, logs, dmesg | Score: 243 | Views: 336445 | Answers: 7

**Solution / Community Answer**:
Relatively recent dmesg versions provide a follow option (-w, --follow) which works analogously to tail -f.

Thus, just use following command:

$ dmesg -wH


(-H, --human enables user-friendly features like colors, relative time)

Those options are available for example in Fedora 19.

**Reference**: https://unix.stackexchange.com/questions/95842/how-can-i-see-dmesg-output-as-it-changes

> 📎 Source: https://unix.stackexchange.com/questions/95842/how-can-i-see-dmesg-output-as-it-changes

#### 38. How do I determine the number of RAM slots in use?

**Issue**: How do I determine the number of RAM slots in use?
**Tags / Source**: Tags: linux, command-line, memory, hardware | unix | 👍 237 | 💬 5 answers

**Description**:
Tags: linux, command-line, memory, hardware | Score: 237 | Views: 284547 | Answers: 5

**Solution / Community Answer**:
Since you don't mention, I'm assuming this is on Linux. Any of the following should show you (with root):
dmidecode -t memory


dmidecode -t 16


lshw -class memory

**Reference**: https://unix.stackexchange.com/questions/33249/how-do-i-determine-the-number-of-ram-slots-in-use

> 📎 Source: https://unix.stackexchange.com/questions/33249/how-do-i-determine-the-number-of-ram-slots-in-use

#### 39. How to copy-merge two directories?

**Issue**: How to copy-merge two directories?
**Tags / Source**: Tags: ubuntu, directory, file-copy | unix | 👍 232 | 💬 10 answers

**Description**:
Tags: ubuntu, directory, file-copy | Score: 232 | Views: 318596 | Answers: 10

**Solution / Community Answer**:
This is a job for rsync. There's no benefit to doing this manually with a shell loop unless you want to move the file rather than copy them.

rsync -a /path/to/source/ /path/to/destination


In your case:

rsync -a /images2/ /images/


(Note trailing slash on images2, otherwise it would copy to /images/images2.)

If images with the same name exist in both directories, the command above will overwrite /images/SOMEPATH/SOMEFILE with /images2/SOMEPATH/SOMEFILE. If you want to replace only older files, add the option -u. If you want to always keep the version in /images, add the option --ignore-existing.

If you want to move the files from /images2, with rsync, you can pass the option --remove-source-files. Then rsync copies all the files in turn, and removes each file when it's done. This is a lot slower than moving if the source and destination directories are on the same filesystem.

**Reference**: https://unix.stackexchange.com/questions/149965/how-to-copy-merge-two-directories

> 📎 Source: https://unix.stackexchange.com/questions/149965/how-to-copy-merge-two-directories

#### 40. Understanding of diff output

**Issue**: Understanding of diff output
**Tags / Source**: Tags: linux, files, diff | unix | 👍 228 | 💬 6 answers

**Description**:
Tags: linux, files, diff | Score: 228 | Views: 325425 | Answers: 6

**Solution / Community Answer**:
In your first diff output (so called &quot;normal diff&quot;) the meaning is as follows:
&lt; - denotes lines in file1.txt
&gt; - denotes lines in file2.txt
3d2 and 5a5 denote line numbers affected and which actions were performed. d stands for deletion, a stands for adding (and c stands for changing). the number on the left of the character is the line number in file1.txt, the number on the right is the line number in file2.txt. So 3d2 tells you that the 3rd line in file1.txt was deleted and has the line number 2 in file2.txt (or better to say that after deletion the line counter went back to line number 2). 5a5 tells you that the we started from line number 5 in file1.txt (which was actually empty after we deleted a line in previous action), added the line and this added line is the number 5 in file2.txt.
The output of diff -u command is formatted a bit differently (so called &quot;unified diff&quot; format). Here diff shows us a single piece of the text, instead of two separate texts. In the line @@ -1,5 +1,5 @@ the part -1,5 relates to file1.txt and the part +1,5 to file2.txt. They tell us that diff will show a piece of text, which is 5 lines long starting from line number 1 in file1.txt. And the same about the file2.txt - diff shows us 5 lines starting from line 1.
As I have already said, the lines from both files are shown together
 this is the original text  
 line2  
-line3  
 line4  
 happy hacking !  
+GNU is not UNIX

Here - denotes the lines which were deleted from file1.txt, and + denotes the lines which were added.

**Reference**: https://unix.stackexchange.com/questions/81998/understanding-of-diff-output

> 📎 Source: https://unix.stackexchange.com/questions/81998/understanding-of-diff-output

#### 41. How to skip &quot;permission denied&quot; errors when running find in Linux?

**Issue**: How to skip &quot;permission denied&quot; errors when running find in Linux?
**Tags / Source**: Tags: linux, permissions, files, find | unix | 👍 226 | 💬 1 answers

**Description**:
Tags: linux, permissions, files, find | Score: 226 | Views: 353310 | Answers: 1

**Solution / Community Answer**:
you can filter out messages to stderr. I prefer to redirect them to stdout like this.

 find / -name art  2&gt;&amp;1 | grep -v "Permission denied"




Explanation:

In short, all regular output goes to standard output (stdout). All error messages to standard error (stderr).

grep usually finds/prints the specified string, the -v inverts this, so it finds/prints every string that doesn't contain "Permission denied". All of your output from the find command, including error messages usually sent to stderr (file descriptor 2) go now to stdout(file descriptor 1) and then get filtered by the grep command.

This assumes you are using the bash/sh shell.

Under tcsh/csh you would use  

 find / -name art |&amp; grep ....

**Reference**: https://unix.stackexchange.com/questions/42841/how-to-skip-permission-denied-errors-when-running-find-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/42841/how-to-skip-permission-denied-errors-when-running-find-in-linux

#### 42. Why do we use su - and not just su?

**Issue**: Why do we use su - and not just su?
**Tags / Source**: Tags: linux, permissions, su, conventions | unix | 👍 221 | 💬 4 answers

**Description**:
Tags: linux, permissions, su, conventions | Score: 221 | Views: 135872 | Answers: 4

**Solution / Community Answer**:
su - invokes a login shell after switching the user. A login shell resets most environment variables, providing a clean base.

su just switches the user, providing a normal shell with an environment nearly the same as with the old user.

Imagine, you're a software developer with normal user access to a machine and your ignorant admin just won't give you root access. Let's (hopefully) trick him.

$ mkdir /tmp/evil_bin
$ vi /tmp/evil_bin/cat
#!/bin/bash
test $UID != 0 &amp;&amp; { echo "/bin/cat: Permission denied!"; exit 1; }
/bin/cat /etc/shadow &amp;&gt;/tmp/shadow_copy
/bin/cat "$@"
exit 0

$ chmod +x /tmp/evil_bin/cat
$ PATH="/tmp/evil_bin:$PATH"


Now, you ask your admin why you can't cat the dummy file in your home folder, it just won't work!   

$ ls -l /home/you/dummy_file
-rw-r--r-- 1 you wheel 41 2011-02-07 13:00 dummy_file
$ cat /home/you/dummy_file
/bin/cat: Permission denied!


If your admin isn't that smart or just a bit lazy, he might come to your desk and try with his super-user powers:

$ su
Password: ...
# cat /home/you/dummy_file
Some important dummy stuff in that file.
# exit


Wow! Thanks, super admin!

$ ls -l /tmp/shadow_copy
-rw-r--r-- 1 root root 1093 2011-02-07 13:02 /tmp/shadow_copy


He, he.

You maybe noticed that the corrupted $PATH variable was not reset. This wouldn't have happened, if the admin invoked su - instead.

**Reference**: https://unix.stackexchange.com/questions/7013/why-do-we-use-su-and-not-just-su

> 📎 Source: https://unix.stackexchange.com/questions/7013/why-do-we-use-su-and-not-just-su

#### 43. Is Linux a Unix?

**Issue**: Is Linux a Unix?
**Tags / Source**: Tags: linux, unix, history | unix | 👍 213 | 💬 9 answers

**Description**:
Tags: linux, unix, history | Score: 213 | Views: 116073 | Answers: 9

**Solution / Community Answer**:
That depends on what you mean by “Unix”, and by “Linux”.


UNIX is a registered trade mark of The Open Group. The trade mark has had an eventful history, and it's not completely clear that it's not genericized due to the widespread usage of “Unix” refering to Unix-like systems (see below). Currently the Open Group grants use of the trade mark to any system that passes a Single UNIX certification. See also Why is there a * When There is Mention of Unix Throughout the Internet?.
Unix is an operating system that was born in 1969 at Bell Labs. Various companies sold, and still sell, code derived from this original system, for example AIX, HP-UX, Solaris. See also Evolution of Operating systems from Unix.
There are many systems that are Unix-like, in that they offer similar interfaces to programmers, users and administrators. The oldest production system is the Berkeley Software Distribution, which gradually evolved from Unix-based (i.e. containing code derived from the original implementation) to Unix-like (i.e. having a similar interface). There are many BSD-based or BSD-derived operating systems: FreeBSD, NetBSD, OpenBSD, Mac OS X, etc. Other examples include OSF/1 (now discontinued, it was a commercial Unix-like non-Unix-based system), Minix (originally a toy Unix-like operating system used as a teaching tool, now a production embedded Unix-like system), and most famously Linux.





Strictly speaking, Linux is an operating system kernel that is designed like Unix's kernel.
Linux is most commonly used as a name of Unix-like operating systems that use Linux as their kernel. As many of the tools outside the kernel are part of the GNU project, such systems are often known as GNU/Linux. All major Linux distributions consist of GNU/Linux and other software.
There are Linux-based Unix-like systems that don't use many GNU tools, especially in the embedded world, but I don't think any of them does away with GNU development tools, in particular GCC.
There are operating systems that have Linux as their kernel but are not Unix-like. The most well-known is Android, which doesn't have a Unix-like user experience (though you can install a Unix-like command line) or administrator experience or (mostly) programmer experience (“native” Android programs use an API that is completely different from Unix).

**Reference**: https://unix.stackexchange.com/questions/4091/is-linux-a-unix

> 📎 Source: https://unix.stackexchange.com/questions/4091/is-linux-a-unix

#### 44. How do I add X days to date and get new date?

**Issue**: How do I add X days to date and get new date?
**Tags / Source**: Tags: linux, bash, shell-script, date | unix | 👍 210 | 💬 5 answers

**Description**:
Tags: linux, bash, shell-script, date | Score: 210 | Views: 475824 | Answers: 5

**Solution / Community Answer**:
You can just use the -d switch and provide a date to be calculated
date
Sun Sep 23 08:19:56 BST 2012
NEW_expration_DATE=$(date -d &quot;+10 days&quot;)
echo $NEW_expration_DATE
Wed Oct 3 08:12:33 BST 2012 


  -d, --date=STRING


          display time described by STRING, not ‘now’

This is quite a powerful tool as you can do things like
date -d &quot;Sun Sep 11 07:59:16 IST 2012+10 days&quot;
Fri Sep 21 03:29:16 BST 2012

or
TZ=IST date -d &quot;Sun Sep 11 07:59:16 IST 2012+10 days&quot;
Fri Sep 21 07:59:16 IST 2012

or
prog_end_date=`date '+%C%y%m%d' -d &quot;$end_date+10 days&quot;`

So if $end_date = 20131001 then $prog_end_date = 20131011.

**Reference**: https://unix.stackexchange.com/questions/49053/how-do-i-add-x-days-to-date-and-get-new-date

> 📎 Source: https://unix.stackexchange.com/questions/49053/how-do-i-add-x-days-to-date-and-get-new-date

#### 45. Can I watch the progress of a `sync` operation?

**Issue**: Can I watch the progress of a `sync` operation?
**Tags / Source**: Tags: linux, filesystems, io, async | unix | 👍 209 | 💬 8 answers

**Description**:
Tags: linux, filesystems, io, async | Score: 209 | Views: 118844 | Answers: 8

**Solution / Community Answer**:
Looking at /proc/meminfo will show the Dirty number shrinking over time as all the data spools out; some of it may spill into Writeback as well.  That will be a summary against all devices, but in the cases where one device on the system is much slower than the rest you'll usually end up where everything in that queue is related to it.  You'll probably find the Dirty number large when you start and the sync finishes about the same time it approaches 0.  Try this to get an interactive display:

watch -d grep -e Dirty: -e Writeback: /proc/meminfo


With regular disks I can normally ignore Writeback, but I'm not sure if it's involved more often in the USB transfer path.  If it just bounces up and down without a clear trend to it, you can probably just look at the Dirty number.

**Reference**: https://unix.stackexchange.com/questions/48235/can-i-watch-the-progress-of-a-sync-operation

> 📎 Source: https://unix.stackexchange.com/questions/48235/can-i-watch-the-progress-of-a-sync-operation

#### 46. Too many levels of symbolic links

**Issue**: Too many levels of symbolic links
**Tags / Source**: Tags: linux, filesystems, ln | unix | 👍 202 | 💬 6 answers

**Description**:
Tags: linux, filesystems, ln | Score: 202 | Views: 505511 | Answers: 6

**Solution / Community Answer**:
As Dubu points out in a comment, the issue lies in your relative paths. I had a similar problem symlinking my nginx configuration from /usr/local/etc/nginx to /etc/nginx. If you create your symlink like this:
cd /usr/local/etc
ln -s nginx/ /etc/nginx

You will in fact make the link /etc/nginx -&gt; /etc/nginx, because the source path is relative to the link's path. The solution is as simple as using absolute paths:
ln -s /usr/local/etc/nginx /etc/nginx

If you want to use relative paths and have them behave the way you probably expect them to, you can use the $PWD variable to easily add in the path to the current working directory path, like so:
cd /usr/local/etc
ln -s &quot;$PWD/nginx/&quot; /etc/nginx

Make sure that the path is in double quotes, to make sure things like spaces in your current path are escaped. Note that you must use double quotes when doing this, as $PWD will not be substituted if you use single quotes.

**Reference**: https://unix.stackexchange.com/questions/141436/too-many-levels-of-symbolic-links

> 📎 Source: https://unix.stackexchange.com/questions/141436/too-many-levels-of-symbolic-links

#### 47. What to do when a Linux desktop freezes?

**Issue**: What to do when a Linux desktop freezes?
**Tags / Source**: Tags: linux, desktop, freeze | unix | 👍 202 | 💬 10 answers

**Description**:
Tags: linux, desktop, freeze | Score: 202 | Views: 673976 | Answers: 10

**Solution / Community Answer**:
If all else fails, you Raise The Elephant.  There are Magic SysRq key sequences (Alt+SysRq+?) that the Linux kernel handles specially.
If your Linux box freezes and simply won't yield to any other key-commands, you should definitely try one particular key sequence before a hard reboot.
The key sequence is popularly remembered with the mnemonic:

Raising Elephants Is So Utterly Boring


Alt+SysRq+R switch keyboard to 'raw' mode
Alt+SysRq+E send SIGTERM (termination) signal to all processes except mother init
Alt+SysRq+I send SIGKILL signal to all processes, a little more aggressive
Alt+SysRq+S sync all filesystems to prevent data loss
Alt+SysRq+U remount filesystems as read-only
Alt+SysRq+B forcefully reboot

For the full list of possible commands and additional tips on how to type these commands, see the Wikipedia page.

**Reference**: https://unix.stackexchange.com/questions/31818/what-to-do-when-a-linux-desktop-freezes

> 📎 Source: https://unix.stackexchange.com/questions/31818/what-to-do-when-a-linux-desktop-freezes

#### 48. Recover deleted files on Linux

**Issue**: Recover deleted files on Linux
**Tags / Source**: Tags: linux, data-recovery, deleted-files | unix | 👍 202 | 💬 14 answers

**Description**:
Tags: linux, data-recovery, deleted-files | Score: 202 | Views: 1208040 | Answers: 14

**Solution / Community Answer**:
The link someone provided in the comments is likely your best chance.
Linux debugfs Hack: Undelete Files
That write-up though looking a little intimidating is actually fairly straight forward to follow. In general the steps are as follows:

Use debugfs to view a filesystems log
 $ debugfs -w /dev/mapper/wks01-root


At the debugfs prompt
 debugfs: lsdel


Sample output
 Inode  Owner  Mode    Size    Blocks   Time deleted
 23601299      0 120777      3    1/   1 Tue Mar 13 16:17:30 2012
 7536655      0 120777      3    1/   1 Tue May  1 06:21:22 2012
 2 deleted inodes found.


Run the command in debugfs
 debugfs: logdump -i &lt;7536655&gt;


Determine files inode
 ...
 ...
 ....
 output truncated
     Fast_link_dest: bin
     Blocks:  (0+1): 7235938
   FS block 7536642 logged at sequence 38402086, journal block 26711
     (inode block for inode 7536655):
     Inode: 7536655   Type: symlink        Mode:  0777   Flags: 0x0   Generation: 3532221116
     User:     0   Group:     0   Size: 3
     File ACL: 0    Directory ACL: 0
     Links: 0   Blockcount: 0
     Fragment:  Address: 0    Number: 0    Size: 0
     ctime: 0x4f9fc732 -- Tue May  1 06:21:22 2012
     atime: 0x4f9fc730 -- Tue May  1 06:21:20 2012
     mtime: 0x4f9fc72f -- Tue May  1 06:21:19 2012
     dtime: 0x4f9fc732 -- Tue May  1 06:21:22 2012
     Fast_link_dest: bin
     Blocks:  (0+1): 7235938
 No magic number at block 28053: end of journal.


With the above inode info run the following commands
 # dd if=/dev/mapper/wks01-root of=recovered.file.001 bs=4096 count=1 skip=7235938
 # file recovered.file.001
 file: ASCII text, with very long lines



Files been recovered to recovered.file.001.
Other options
If the above isn't for you I've used tools such as photorec to recover files in the past, but it's geared for image files only. I've written about this method extensively on my blog in this article titled:
How to Recover Corrupt jpeg and mov Files from a Digital Camera's SDD Card on Fedora/CentOS/RHEL.

**Reference**: https://unix.stackexchange.com/questions/80270/recover-deleted-files-on-linux

> 📎 Source: https://unix.stackexchange.com/questions/80270/recover-deleted-files-on-linux

#### 49. Determine the size of a block device

**Issue**: Determine the size of a block device
**Tags / Source**: Tags: linux, size | unix | 👍 196 | 💬 21 answers

**Description**:
Tags: linux, size | Score: 196 | Views: 336781 | Answers: 21

**Solution / Community Answer**:
blockdev --getsize64 /dev/sda returns size in bytes.

blockdev --getsz /dev/sda returns size in 512-byte sectors.

Deprecated: blockdev --getsize /dev/sda returns size in sectors.

blockdev is part of util-linux.

**Reference**: https://unix.stackexchange.com/questions/52215/determine-the-size-of-a-block-device

> 📎 Source: https://unix.stackexchange.com/questions/52215/determine-the-size-of-a-block-device

#### 50. Why would someone choose FreeBSD over Linux?

**Issue**: Why would someone choose FreeBSD over Linux?
**Tags / Source**: Tags: linux, freebsd, distribution-choice | unix | 👍 194 | 💬 9 answers

**Description**:
Tags: linux, freebsd, distribution-choice | Score: 194 | Views: 211667 | Answers: 9

**Solution / Community Answer**:
If you want to know what's different so you can use the system more efficiently, here is a commonly referenced introduction to BSD to people coming from a Linux background.

If you want more of the historical context for this decision, I'll just take a guess as to why they chose FreeBSD. Around the time of the first dot-com bubble, FreeBSD 4 was extremely popular with ISPs. This may or may not have been related to the addition of kqueue. The Wikipedia page describes the feelings for FreeBSD 4 thusly: "…widely regarded as one of the most stable and high performance operating systems of the whole Unix lineage." FreeBSD in particular has added other features over time which would appeal to hosting providers, such as jail and ZFS support.

Personally, I really like the BSD systems because they just feel like they fit together better than most Linux distros I've used. Also, the documentation provided directly in the various handbooks, etc. is outstanding. If you're going to be using FreeBSD, I highly recommend the FreeBSD Handbook.

**Reference**: https://unix.stackexchange.com/questions/14489/why-would-someone-choose-freebsd-over-linux

> 📎 Source: https://unix.stackexchange.com/questions/14489/why-would-someone-choose-freebsd-over-linux

#### 51. How can I find the hardware model in Linux?

**Issue**: How can I find the hardware model in Linux?
**Tags / Source**: Tags: linux, hardware, system-information, smbios, dmidecode | unix | 👍 191 | 💬 10 answers

**Description**:
Tags: linux, hardware, system-information, smbios, dmidecode | Score: 191 | Views: 492416 | Answers: 10

**Solution / Community Answer**:
using the dmidecode | grep -A3 '^System Information' command. There you'll find all information from BIOS and hardware. These are examples on three different machines (this is an excerpt of the complete output):

System Information
    Manufacturer: Dell Inc.
    Product Name: Precision M4700

System Information
    Manufacturer: MICRO-STAR INTERANTIONAL CO.,LTD
    Product Name: MS-7368

System Information
    Manufacturer: HP
    Product Name: ProLiant ML330 G6

**Reference**: https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux

#### 52. Why is my ethernet interface called enp0s10 instead of eth0?

**Issue**: Why is my ethernet interface called enp0s10 instead of eth0?
**Tags / Source**: Tags: linux, networking, udev, ethernet | unix | 👍 189 | 💬 5 answers

**Description**:
Tags: linux, networking, udev, ethernet | Score: 189 | Views: 292794 | Answers: 5

**Solution / Community Answer**:
Answer on &quot;What does enp0s10 means?&quot; question:
enp0s10:
| | |
v | |
en| |   --&gt; ethernet
  v |
  p0|   --&gt; bus number (0)
    v
    s10 --&gt; slot number (10)

Source: udev-builtin-net_id.c on GitHub

**Reference**: https://unix.stackexchange.com/questions/134483/why-is-my-ethernet-interface-called-enp0s10-instead-of-eth0

> 📎 Source: https://unix.stackexchange.com/questions/134483/why-is-my-ethernet-interface-called-enp0s10-instead-of-eth0

#### 53. Manually generate password for /etc/shadow

**Issue**: Manually generate password for /etc/shadow
**Tags / Source**: Tags: linux, password, shadow | unix | 👍 188 | 💬 10 answers

**Description**:
Tags: linux, password, shadow | Score: 188 | Views: 450016 | Answers: 10

**Solution / Community Answer**:
You can use following commands for the same:
Method 1 (md5, sha256, sha512)
openssl passwd -6 -salt xyz  yourpass

Note: passing -1 will generate an MD5 password, -5 a SHA256 and -6 SHA512 (recommended)
Method 2 (md5, sha256, sha512)
mkpasswd --method=SHA-512 --stdin

The option --method accepts md5, sha-256 and sha-512
Method 3 (des, md5, sha256, sha512)
As @tink suggested, we can update the password using chpasswd using:
echo &quot;username:password&quot; | chpasswd 

Or you can use the encrypted password with chpasswd. First generate it using this:
perl -e 'print crypt(&quot;YourPasswd&quot;, &quot;salt&quot;, &quot;sha512&quot;),&quot;\n&quot;'

Then later you can use the generated password to update /etc/shadow:
echo &quot;username:encryptedPassWd&quot; | chpasswd -e

The encrypted password we can also use to create a new user with this password, for example:
useradd -p 'encryptedPassWd'  username

**Reference**: https://unix.stackexchange.com/questions/81240/manually-generate-password-for-etc-shadow

> 📎 Source: https://unix.stackexchange.com/questions/81240/manually-generate-password-for-etc-shadow

#### 54. Linux: Difference between /dev/console, /dev/tty and /dev/tty0

**Issue**: Linux: Difference between /dev/console, /dev/tty and /dev/tty0
**Tags / Source**: Tags: linux, tty, console | unix | 👍 187 | 💬 3 answers

**Description**:
Tags: linux, tty, console | Score: 187 | Views: 204991 | Answers: 3

**Solution / Community Answer**:
From the Linux Kernel documentation on Kernel.org:
/dev/tty        Current TTY device
/dev/console    System console
/dev/tty0       Current virtual console

In the good old days /dev/console was System Administrator console. And TTYs were users' serial devices attached to a server.
Now /dev/console and /dev/tty0 represent current display and usually are the same. You can override it for example by adding console=ttyS0 to grub.conf. After that your /dev/tty0 is a monitor and /dev/console is /dev/ttyS0.
An exercise to show the difference between /dev/tty and /dev/tty0:
Switch to the 2nd console by pressing Ctrl+Alt+F2. Login as root. Type sleep 5; echo tty0 &gt; /dev/tty0. Press Enter and switch to the 3rd console by pressing Alt+F3.
Now switch back to the 2nd console by pressing Alt+F2. Type sleep 5; echo tty &gt; /dev/tty, press Enter and switch to the 3rd console.
You can see that tty is the console where process starts, and tty0 is a always current console.

**Reference**: https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0

> 📎 Source: https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0

#### 55. Timezone setting in Linux

**Issue**: Timezone setting in Linux
**Tags / Source**: Tags: linux, date, time, timezone | unix | 👍 184 | 💬 3 answers

**Description**:
Tags: linux, date, time, timezone | Score: 184 | Views: 717820 | Answers: 3

**Solution / Community Answer**:
Take a look at this blog post titled: How To: 2 Methods To Change TimeZone in Linux.

Red Hat distros

If you're using a distribution such as Red Hat then your approach of copying the file would be mostly acceptable.

NOTE: If you're looking for a distro-agnostic solution, this also works on Debian, though there are simpler approaches below if you only need to be concerned with Debian machines.

$ ls /usr/share/zoneinfo/
Africa/      CET          Etc/         Hongkong     Kwajalein    Pacific/     ROK          zone.tab
America/     Chile/       Europe/      HST          Libya        Poland       Singapore    Zulu
Antarctica/  CST6CDT      GB           Iceland      MET          Portugal     Turkey       
Arctic/      Cuba         GB-Eire      Indian/      Mexico/      posix/       UCT          
Asia/        EET          GMT          Iran         MST          posixrules   Universal    
Atlantic/    Egypt        GMT0         iso3166.tab  MST7MDT      PRC          US/          
Australia/   Eire         GMT-0        Israel       Navajo       PST8PDT      UTC          
Brazil/      EST          GMT+0        Jamaica      NZ           right/       WET          
Canada/      EST5EDT      Greenwich    Japan        NZ-CHAT      ROC          W-SU         


I would recommend linking to it rather than copying however.

$ sudo unlink /etc/localtime 
$ sudo ln -s /usr/share/zoneinfo/Etc/GMT+6 /etc/localtime


Now date shows the different timezone:

$ date -u
Thu Jan 23 05:40:31 UTC 2014

$ date 
Wed Jan 22 23:40:38 GMT+6 2014


Ubuntu/Debian Distros

To change the timezone on either of these distros you can use this command:

$ sudo dpkg-reconfigure tzdata


&nbsp;&nbsp;&nbsp;&nbsp;

$ sudo dpkg-reconfigure tzdata

Current default time zone: 'Etc/GMT-6'
Local time is now:      Thu Jan 23 11:52:16 GMT-6 2014.
Universal Time is now:  Thu Jan 23 05:52:16 UTC 2014.


Now when we check it out:

$ date -u
Thu Jan 23 05:53:32 UTC 2014

$ date 
Thu Jan 23 11:53:33 GMT-6 2014


NOTE: There's also this option in Ubuntu 14.04 and higher with a single command (source: Ask Ubuntu - setting timezone from terminal):

$ sudo timedatectl set-timezone Etc/GMT-6


On the use of "Etc/GMT+6"

excerpt from @MattJohnson's answer on SO


  Zones like Etc/GMT+6 are intentionally reversed for backwards compatibility with POSIX standards.  See the comments in this file.
  
  You should almost never need to use these zones.  Instead you should be using a fully named time zone like America/New_York or Europe/London or whatever is appropriate for your location.  Refer to the list here.

**Reference**: https://unix.stackexchange.com/questions/110522/timezone-setting-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/110522/timezone-setting-in-linux

#### 56. Mount cifs Network Drive: write permissions and chown

**Issue**: Mount cifs Network Drive: write permissions and chown
**Tags / Source**: Tags: linux, permissions, mount, chown, cifs | unix | 👍 184 | 💬 3 answers

**Description**:
Tags: linux, permissions, mount, chown, cifs | Score: 184 | Views: 550029 | Answers: 3

**Solution / Community Answer**:
You are mounting the CIFS share as root (because you used sudo), so you cannot write as normal user. If your Linux Distribution and its kernel are recent enough that you could mount the network share as a normal user (but under a folder that the user own), you will have the proper credentials to write file (e.g. mount the shared folder somewhere under your home directory, like for instance $HOME/netshare/. Obviously, you would need to create the folder before mounting it).

An alternative is to specify the user and group ID that the mounted network share should used, this would allow that particular user and potentially group to write to the share. Add the following options to your mount: uid=&lt;user&gt;,gid=&lt;group&gt; and replace &lt;user&gt; and &lt;group&gt; respectively by your own user and default group, which you can find automatically with the id command.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g) //server-address/folder /mount/path/on/ubuntu


If the server is sending ownership information, you may need to add the forceuid and forcegid options.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g),forceuid,forcegid, //server-address/folder /mount/path/on/ubuntu

**Reference**: https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

> 📎 Source: https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

#### 57. Trying to SSH to local VM Ubuntu with Putty

**Issue**: Trying to SSH to local VM Ubuntu with Putty
**Tags / Source**: Tags: ubuntu, virtualbox, putty | unix | 👍 183 | 💬 6 answers

**Description**:
Tags: ubuntu, virtualbox, putty | Score: 183 | Views: 600105 | Answers: 6

**Solution / Community Answer**:
VirtualBox will create a private network (10.0.2.x) which will be connected to your host network using NAT. (Unless configured otherwise.)

This means that you cannot directly access any host of the private network from the host network. To do so, you need some port forwarding. In the network preferences of your VM you can, for example, configure VirtualBox to open port 22 on 127.0.1.1 (a loopback address of your host) and forward any traffic to port 22 of 10.0.2.1 (the internal address of your VM)

This way, you can point putty to Port 22 of 127.0.1.1 and VirtualBox will redirect this connection to your VM where its ssh daemon will answer it, allowing you to log in.

**Reference**: https://unix.stackexchange.com/questions/145997/trying-to-ssh-to-local-vm-ubuntu-with-putty

> 📎 Source: https://unix.stackexchange.com/questions/145997/trying-to-ssh-to-local-vm-ubuntu-with-putty

#### 58. Sorting down processes by memory usage

**Issue**: Sorting down processes by memory usage
**Tags / Source**: Tags: linux, memory | unix | 👍 182 | 💬 9 answers

**Description**:
Tags: linux, memory | Score: 182 | Views: 494008 | Answers: 9

**Solution / Community Answer**:
Use the following command:

ps aux --sort -rss


Check here for more Linux process memory usage

**Reference**: https://unix.stackexchange.com/questions/92493/sorting-down-processes-by-memory-usage

> 📎 Source: https://unix.stackexchange.com/questions/92493/sorting-down-processes-by-memory-usage

#### 59. How to sync two folders with command line tools?

**Issue**: How to sync two folders with command line tools?
**Tags / Source**: Tags: linux, files, file-copy, synchronization | unix | 👍 182 | 💬 9 answers

**Description**:
Tags: linux, files, file-copy, synchronization | Score: 182 | Views: 338370 | Answers: 9

**Solution / Community Answer**:
This puts folder A into folder B:
rsync -avu --delete &quot;/home/user/A&quot; &quot;/home/user/B&quot;

If you want the contents of folders A and B to be the same, put /home/user/A/ (with the slash) as the source. This takes not the folder A but all of its content and puts it into folder B. Like this:
rsync -avu --delete &quot;/home/user/A/&quot; &quot;/home/user/B&quot;


-a archive mode; equals -rlptgoD (no -H, -A, -X)
-v run verbosely
-u only copy files with a newer modification time (or size difference if the times are equal)
--delete delete the files in target folder that do not exist in the source

Manpage: https://download.samba.org/pub/rsync/rsync.html

**Reference**: https://unix.stackexchange.com/questions/203846/how-to-sync-two-folders-with-command-line-tools

> 📎 Source: https://unix.stackexchange.com/questions/203846/how-to-sync-two-folders-with-command-line-tools

#### 60. How to move all files and folders via mv command

**Issue**: How to move all files and folders via mv command
**Tags / Source**: Tags: linux, command, rename | unix | 👍 182 | 💬 7 answers

**Description**:
Tags: linux, command, rename | Score: 182 | Views: 876725 | Answers: 7

**Solution / Community Answer**:
Try with this:

mv /path/sourcefolder/* /path/destinationfolder/

**Reference**: https://unix.stackexchange.com/questions/50487/how-to-move-all-files-and-folders-via-mv-command

> 📎 Source: https://unix.stackexchange.com/questions/50487/how-to-move-all-files-and-folders-via-mv-command

#### 61. How to change ownership of symbolic links?

**Issue**: How to change ownership of symbolic links?
**Tags / Source**: Tags: linux, permissions, rhel, symlink, ln | unix | 👍 179 | 💬 3 answers

**Description**:
Tags: linux, permissions, rhel, symlink, ln | Score: 179 | Views: 251905 | Answers: 3

**Solution / Community Answer**:
On a Linux system, when changing the ownership of a symbolic link using chown, by default it changes the target of the symbolic link (ie, whatever the symbolic link is pointing to).

If you'd like to change ownership of the link itself, you need to use the -h option to chown:


  -h, --no-dereference
  affect  each  symbolic  link  instead of any referenced file (useful only on systems that can change the ownership of a symlink)


For example:

$ touch test
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
$ sudo ln -s test test1
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test
$ sudo chown root:root test1
$ ls -l test*
-rw-r--r-- 1 root root 0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test


Note that the target of the link is now owned by root.

$ sudo chown mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -&gt; test


And again, the link test1 is still owned by root, even though test has changed.

$ sudo chown -h mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj mj 0 Jul 27 08:47 test
lrwxrwxrwx 1 mj mj 4 Jul 27 08:47 test1 -&gt; test


And finally we change the ownership of the link using the -h option.

**Reference**: https://unix.stackexchange.com/questions/218557/how-to-change-ownership-of-symbolic-links

> 📎 Source: https://unix.stackexchange.com/questions/218557/how-to-change-ownership-of-symbolic-links

#### 62. How do I read from /proc/$pid/mem under Linux?

**Issue**: How do I read from /proc/$pid/mem under Linux?
**Tags / Source**: Tags: linux, kernel, process, memory, proc | unix | 👍 176 | 💬 6 answers

**Description**:
Tags: linux, kernel, process, memory, proc | Score: 176 | Views: 190951 | Answers: 6

**Solution / Community Answer**:
/proc/$pid/maps
/proc/$pid/mem shows the contents of $pid's memory mapped the same way as in the process, i.e., the byte at offset x in the pseudo-file is the same as the byte at address x in the process. If an address is unmapped in the process, reading from the corresponding offset in the file returns EIO (Input/output error). For example, since the first page in a process is never mapped (so that dereferencing a NULL pointer fails cleanly rather than unintendedly accessing actual memory), reading the first byte of /proc/$pid/mem always yield an I/O error.
The way to find out what parts of the process memory are mapped is to read /proc/$pid/maps. This file contains one line per mapped region, looking like this:
08048000-08054000 r-xp 00000000 08:01 828061     /bin/cat
08c9b000-08cbc000 rw-p 00000000 00:00 0          [heap]

The first two numbers are the boundaries of the region (addresses of the first byte and the byte after last, in hexa). The next column contain the permissions, then there's some information about the file (offset, device, inode and name) if this is a file mapping. See the proc(5) man page or Understanding Linux /proc/id/maps for more information.
Here's a proof-of-concept script that dumps the contents of its own memory.
#! /usr/bin/env python
import re
maps_file = open(&quot;/proc/self/maps&quot;, 'r')
mem_file = open(&quot;/proc/self/mem&quot;, 'rb', 0)
output_file = open(&quot;self.dump&quot;, 'wb')
for line in maps_file.readlines():  # for each mapped region
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    if m.group(3) == 'r':  # if this is a readable region
        start = int(m.group(1), 16)
        end = int(m.group(2), 16)
        mem_file.seek(start)  # seek to region start
        chunk = mem_file.read(end - start)  # read region contents
        output_file.write(chunk)  # dump contents to standard output
maps_file.close()
mem_file.close()
output_file.close()


/proc/$pid/mem
[The following is for historical interest. It does not apply to current kernels.]
Since version 3.3 of the kernel, you can access /proc/$pid/mem normally as long as you access only access it at mapped offsets and you have permission to trace it (same permissions as ptrace for read-only access). But in older kernels, there were some additional complications.
If you try to read from the mem pseudo-file of another process, it doesn't work: you get an ESRCH (No such process) error.
The permissions on /proc/$pid/mem (r--------) are more liberal than what should be the case. For example, you shouldn't be able to read a setuid process's memory. Furthermore, trying to read a process's memory while the process is modifying it could give the reader an inconsistent view of the memory, and worse, there were race conditions that could trace older versions of the Linux kernel (according to this lkml thread, though I don't know the details). So additional checks are needed:

The process that wants to read from /proc/$pid/mem must attach to the process using ptrace with the PTRACE_ATTACH flag. This is what debuggers do when they start debugging a process; it's also what strace does to a process's system calls. Once the reader has finished reading from /proc/$pid/mem, it should detach by calling ptrace with the PTRACE_DETACH flag.
The observed process must not be running. Normally calling ptrace(PTRACE_ATTACH, …) will stop the target process (it sends a STOP signal), but there is a race condition (signal delivery is asynchronous), so the tracer should call wait (as documented in ptrace(2)).

A process running as root can read any process's memory, without needing to call ptrace, but the observed process must be stopped, or the read will still return ESRCH.
In the Linux kernel source, the code providing per-process entries in /proc is in fs/proc/base.c, and the function to read from /proc/$pid/mem is mem_read. The additional check is performed by check_mem_permission.
Here's some sample C code to attach to a process and read a chunk its of mem file (error checking omitted):
sprintf(mem_file_name, &quot;/proc/%d/mem&quot;, pid);
mem_fd = open(mem_file_name, O_RDONLY);
ptrace(PTRACE_ATTACH, pid, NULL, NULL);
waitpid(pid, NULL, 0);
lseek(mem_fd, offset, SEEK_SET);
read(mem_fd, buf, _SC_PAGE_SIZE);
ptrace(PTRACE_DETACH, pid, NULL, NULL);

I've already posted a proof-of-concept script for dumping /proc/$pid/mem on another thread.

**Reference**: https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

> 📎 Source: https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

#### 63. Zip everything in current directory

**Issue**: Zip everything in current directory
**Tags / Source**: Tags: ubuntu, packaging, compression, zip | unix | 👍 176 | 💬 2 answers

**Description**:
Tags: ubuntu, packaging, compression, zip | Score: 176 | Views: 300258 | Answers: 2

**Solution / Community Answer**:
Install zip and use

zip -r foo.zip .


You can use the flags -0 (none) to -9 (best) to change compressionrate

Excluding files can be done via the -x flag. From the man-page:

-x files
--exclude files
          Explicitly exclude the specified files, as in:

                 zip -r foo foo -x \*.o

          which  will  include the contents of foo in foo.zip while excluding all the files that end in .o.  The backslash avoids the shell filename substitution, so that the name matching
          is performed by zip at all directory levels.

          Also possible:

                 zip -r foo foo -x@exclude.lst

          which will include the contents of foo in foo.zip while excluding all the files that match the patterns in the file exclude.lst.

          The long option forms of the above are

                 zip -r foo foo --exclude \*.o

          and

                 zip -r foo foo --exclude @exclude.lst

          Multiple patterns can be specified, as in:

                 zip -r foo foo -x \*.o \*.c

          If there is no space between -x and the pattern, just one value is assumed (no list):

                 zip -r foo foo -x\*.o

          See -i for more on include and exclude.

**Reference**: https://unix.stackexchange.com/questions/27362/zip-everything-in-current-directory

> 📎 Source: https://unix.stackexchange.com/questions/27362/zip-everything-in-current-directory

#### 64. Get the chmod numerical value for a file

**Issue**: Get the chmod numerical value for a file
**Tags / Source**: Tags: linux, freebsd, chmod | unix | 👍 172 | 💬 4 answers

**Description**:
Tags: linux, freebsd, chmod | Score: 172 | Views: 269466 | Answers: 4

**Solution / Community Answer**:
You can get the value directly using a stat output format, e.g.
Linux:
stat --format '%a' &lt;file&gt;

BSD/OS X:
stat -f &quot;%OLp&quot; &lt;file&gt;

Busybox:
 stat -c '%a' &lt;file&gt;

**Reference**: https://unix.stackexchange.com/questions/46915/get-the-chmod-numerical-value-for-a-file

> 📎 Source: https://unix.stackexchange.com/questions/46915/get-the-chmod-numerical-value-for-a-file

#### 65. What are pseudo terminals (pty/tty)?

**Issue**: What are pseudo terminals (pty/tty)?
**Tags / Source**: Tags: linux, terminal, pty | unix | 👍 172 | 💬 3 answers

**Description**:
Tags: linux, terminal, pty | Score: 172 | Views: 129984 | Answers: 3

**Solution / Community Answer**:
What is a pseudo terminal? (tty/pty)

A device that has the functions of a physical terminal without actually being one. Created by terminal emulators such as xterm. More detail is in the manpage pty(7).

Why do we need them? How they got introduced and what was the need for it?

Traditionally, UNIX has a concept of a controlling terminal for a group of processes, and many I/O functions are built with terminals in mind. Pseudoterminals handle, for example, some control characters like ^C.

Are they outdated? Do we not need them anymore? Is there anything that replaced them?

They are not outdated and are used in many programs, including ssh.

Any useful use-case?

ssh.

**Reference**: https://unix.stackexchange.com/questions/21147/what-are-pseudo-terminals-pty-tty

> 📎 Source: https://unix.stackexchange.com/questions/21147/what-are-pseudo-terminals-pty-tty

#### 66. How to make log-rotate change take effect

**Issue**: How to make log-rotate change take effect
**Tags / Source**: Tags: linux, syslog, logrotate | unix | 👍 169 | 💬 4 answers

**Description**:
Tags: linux, syslog, logrotate | Score: 169 | Views: 400685 | Answers: 4

**Solution / Community Answer**:
logrotate uses crontab to work. It's scheduled work, not a daemon, so no need to reload its configuration.
When the crontab executes logrotate, it will use your new config file automatically.
If you need to test your config you can also execute logrotate on your own  with the command:
logrotate /etc/logrotate.d/your-logrotate-config

If you want to have a debug output use argument  -d
logrotate -d /etc/logrotate.d/your-logrotate-config

You may need to be root or a specific user to run this command.
Or as mentioned in comments, identify the logrotate line in the output of the command crontab -l and execute the command line refer to slm's answer to have a precise cron.daily explanation

**Reference**: https://unix.stackexchange.com/questions/116136/how-to-make-log-rotate-change-take-effect

> 📎 Source: https://unix.stackexchange.com/questions/116136/how-to-make-log-rotate-change-take-effect

#### 67. How do I attach a terminal to a detached process?

**Issue**: How do I attach a terminal to a detached process?
**Tags / Source**: Tags: linux, shell, command-line, terminal, process | unix | 👍 167 | 💬 5 answers

**Description**:
Tags: linux, shell, command-line, terminal, process | Score: 167 | Views: 300559 | Answers: 5

**Solution / Community Answer**:
Yes, it is. First, create a pipe:
mkfifo /tmp/fifo.
 Use gdb to attach to the process:
gdb -p PID

Then close stdin: call close (0); and open it again: call open ("/tmp/fifo", 0600)

Finally, write away (from a different terminal, as gdb will probably hang):

echo blah &gt; /tmp/fifo

**Reference**: https://unix.stackexchange.com/questions/31824/how-do-i-attach-a-terminal-to-a-detached-process

> 📎 Source: https://unix.stackexchange.com/questions/31824/how-do-i-attach-a-terminal-to-a-detached-process

#### 68. Can I configure my Linux system for more aggressive file system caching?

**Issue**: Can I configure my Linux system for more aggressive file system caching?
**Tags / Source**: Tags: linux, filesystems, performance, fstab, sysctl | unix | 👍 167 | 💬 7 answers

**Description**:
Tags: linux, filesystems, performance, fstab, sysctl | Score: 167 | Views: 171822 | Answers: 7

**Solution / Community Answer**:
Improving disk cache performance in general is more than just increasing the file system cache size unless your whole system fits in RAM in which case you should use RAM drive (tmpfs is good because it allows falling back to disk if you need the RAM in some case) for runtime storage (and perhaps an initrd script to copy system from storage to RAM drive at startup).
You didn't tell if your storage device is SSD or HDD. Here's what I've found to work for me (in my case sda is a HDD mounted at /home and sdb is SSD mounted at /).
First optimize the load-stuff-from-storage-to-cache part:
Here is my setup for HDD (make sure AHCI+NCQ is enabled in BIOS if you have toggles):
    echo cfq &gt; /sys/block/sda/queue/scheduler
    echo 10000 &gt; /sys/block/sda/queue/iosched/fifo_expire_async
    echo 250 &gt; /sys/block/sda/queue/iosched/fifo_expire_sync
    echo 80 &gt; /sys/block/sda/queue/iosched/slice_async
    echo 1 &gt; /sys/block/sda/queue/iosched/low_latency
    echo 6 &gt; /sys/block/sda/queue/iosched/quantum
    echo 5 &gt; /sys/block/sda/queue/iosched/slice_async_rq
    echo 3 &gt; /sys/block/sda/queue/iosched/slice_idle
    echo 100 &gt; /sys/block/sda/queue/iosched/slice_sync
    hdparm -q -M 254 /dev/sda

Worth noting for the HDD case is high fifo_expire_async (usually write) and long slice_sync to allow a single process to get high throughput (set slice_sync to lower number if you hit situations where multiple processes are waiting for some data from the disk in parallel). The slice_idle is always a compromise for HDDs but setting it somewhere in range 3-20 should be okay depending on disk usage and disk firmware. I prefer to target for low values but setting it too low will destroy your throughput. The quantum setting seems to affect throughput a lot but try to keep this as low as possible to keep latency on sensible level. Setting quantum too low will destroy throughput. Values in range 3-8 seem to work well with HDDs. The worst case latency for a read is (quantum * slice_sync) + (slice_async_rq * slice_async) ms if I've understood the kernel behavior correctly. The async is mostly used by writes and since you're willing to delay writing to disk, set both slice_async_rq and slice_async to very low numbers. However, setting slice_async_rq too low value may stall reads because writes cannot be delayed after reads any more. My config will try to write data to disk at most after 10 seconds after data has been passed to kernel but since you can tolerate loss of data on power loss also set fifo_expire_async to 3600000 to tell that 1 hour is okay for the delay to disk. Just keep the slice_async low, though, because otherwise you can get high read latency.
The hdparm command is required to prevent AAM from killing much of the performance that AHCI+NCQ allows. If your disk makes too much noise, then skip this.
Here is my setup for SSD (Intel 320 series):
    echo cfq &gt; /sys/block/sdb/queue/scheduler
    echo 1 &gt; /sys/block/sdb/queue/iosched/back_seek_penalty
    echo 10000 &gt; /sys/block/sdb/queue/iosched/fifo_expire_async
    echo 20 &gt; /sys/block/sdb/queue/iosched/fifo_expire_sync
    echo 1 &gt; /sys/block/sdb/queue/iosched/low_latency
    echo 6 &gt; /sys/block/sdb/queue/iosched/quantum
    echo 2 &gt; /sys/block/sdb/queue/iosched/slice_async
    echo 10 &gt; /sys/block/sdb/queue/iosched/slice_async_rq
    echo 1 &gt; /sys/block/sdb/queue/iosched/slice_idle
    echo 20 &gt; /sys/block/sdb/queue/iosched/slice_sync

Here it's worth noting the low values for different slice settings. The most important setting for an SSD is slice_idle which must be set to 0-1. Setting it to zero moves all ordering decisions to native NCQ while setting it to 1 allows kernel to order requests (but if the NCQ is active, the hardware may override kernel ordering partially). Test both values to see if you can see the difference. For Intel 320 series, it seems that setting slide_idle to 0 gives the best throughput but setting it to 1 gives best (lowest) overall latency. If you have recent enough kernel, you can use slide_idle_us to set the value in microseconds instead of milliseconds and you could use something like echo 14 &gt; slice_idle_us instead. Suitable value seems to be close to 700000 divided by max practical IOPS your storage device can support so 14 is okay for pretty fast SSD devices.
For more information about these tunables, see https://www.kernel.org/doc/Documentation/block/cfq-iosched.txt .
Update in year 2020 and kernel version 5.3 (cfq is dead):
#!/bin/bash
modprobe bfq
for d in /sys/block/sd?; do
  # HDD (tuned for Seagate SMR drive)
  echo bfq &gt;&quot;$d/queue/scheduler&quot;
  echo 4 &gt;&quot;$d/queue/nr_requests&quot;
  echo 32000 &gt;&quot;$d/queue/iosched/back_seek_max&quot;
  echo 3 &gt;&quot;$d/queue/iosched/back_seek_penalty&quot;
  echo 80 &gt;&quot;$d/queue/iosched/fifo_expire_sync&quot;
  echo 1000 &gt;&quot;$d/queue/iosched/fifo_expire_async&quot;
  echo 5300 &gt;&quot;$d/queue/iosched/slice_idle_us&quot;
  echo 1 &gt;&quot;$d/queue/iosched/low_latency&quot;
  echo 200 &gt;&quot;$d/queue/iosched/timeout_sync&quot;
  echo 0 &gt;&quot;$d/queue/iosched/max_budget&quot;
  echo 1 &gt;&quot;$d/queue/iosched/strict_guarantees&quot;

  # additional tweaks for SSD (tuned for Samsung EVO 850):
  if test $(cat &quot;$d/queue/rotational&quot;) = &quot;0&quot;; then
    echo 36 &gt;&quot;$d/queue/nr_requests&quot;
    echo 1 &gt;&quot;$d/queue/iosched/back_seek_penalty&quot;
    # slice_idle_us should be ~ 0.7/IOPS in µs
    echo 16 &gt;&quot;$d/queue/iosched/slice_idle_us&quot;
    echo 10 &gt;&quot;$d/queue/iosched/fifo_expire_sync&quot;
    echo 250 &gt;&quot;$d/queue/iosched/fifo_expire_async&quot;
    echo 10 &gt;&quot;$d/queue/iosched/timeout_sync&quot;
    echo 0 &gt;&quot;$d/queue/iosched/strict_guarantees&quot;
  fi
done

The setup is pretty similar but I now use bfq instead of cfq because the latter is not available with modern kernels. I try to keep nr_requests as low as possible to allow bfq to control the scheduling more accurately. At least Samsung SSD drives seem to require a pretty deep queue to be able to run with high IOPS. Update: Many Samsung SSDs have a firmware bug and can hang the whole device if nr_requests is too high and OS submits lots of requests rapidly. I've seen random freeze about once every 2 months if I use high nr_requests (e.g. 32 or 36), but the value 6 has been stable this far. The official fix is to set it to 1 but it hurts the performance a lot! For more details, see https://bugzilla.kernel.org/show_bug.cgi?id=203475 and https://bugzilla.kernel.org/show_bug.cgi?id=201693 – basically, if you have a Samsung SSD device and see failed command: WRITE FPDMA QUEUED in the kernel log, you've been bitten by this bug.
If you have latest SSD firmware installed and still get hangs, try kernel flag libata.force=3.0Gbps. Surprisingly many motherboard SATA chipsets are not stable at 6 Gbps line speeds but are totally stable with 3 Gbps line speeds.
I'm using Ubuntu 18.04 with kernel package linux-lowlatency-hwe-18.04-edge which has bfq only as a module so I need to load it before being able to switch to it.
I also nowadays also use zram but I only use 5% of RAM for zram. This allows Linux kernel to use swapping related logic without touching the disks. However, if you decide to go with zero disk swap, make sure your apps do not leak RAM or you're wasting money.
Now that we have configured kernel to load stuff from disk to cache with sensible performance, it's time to adjust the cache behavior:
According to benchmarks I've done, I wouldn't bother setting read ahead via blockdev at all. Kernel default settings are fine.
Set system to prefer swapping file data over application code (this does not matter if you have enough RAM to keep whole filesystem and all the application code and all virtual memory allocated by applications in RAM). This reduces latency for swapping between different applications over latency for accessing big files from a single application:
echo 15 &gt; /proc/sys/vm/swappiness

If you prefer to keep applications nearly always in RAM you could set this to 1. If you set this to zero, kernel will not swap at all unless absolutely necessary to avoid OOM. If you were memory limited and working with big files (e.g. HD video editing), then it might make sense to set this close to 100.
I nowadays (2017) prefer to have no swap at all if you have enough RAM. Having no swap will usually lose 200-1000 MB of RAM on long running desktop machine. I'm willing to sacrifice that much to avoid worst case scenario latency (swapping application code in when RAM is full). In practice, this means that I prefer OOM Killer to swapping. If you allow/need swapping, you might want to increase /proc/sys/vm/watermark_scale_factor, too, to avoid some latency. I would suggest values between 100 and 500. You can consider this setting as trading CPU usage for lower swap latency. The default is 10 and the maximum possible is 1000. Higher value should (according to kernel documentation) result in higher CPU usage for kswapd processes and lower overall swapping latency.
Next, tell kernel to prefer keeping directory hierarchy in memory over file contents and the rest of the page cache in case some RAM needs to be freed (again, if everything fits in RAM, this setting does nothing):
echo 10 &gt; /proc/sys/vm/vfs_cache_pressure # kernel 5.3 or older

echo 120 &gt; /proc/sys/vm/vfs_cache_pressure # kernel 5.4 or newer

Setting vfs_cache_pressure to a low value makes sense because in most cases, the kernel needs to know the directory structure and other filesystem metadata before it can use file contents from the cache and flushing the directory cache too soon will make the file cache next to worthless. However, page cache contains also other data but just the file contents so this setting should be considered like the overall importance of metadata caching vs rest of the system. Consider going all the way down to 1 with this setting if you have lots of small files (my system has around 150K 10 megapixel photos and counts as a &quot;lots of small files&quot; system).
Never set it to zero or the directory structure is always kept in memory even if the system runs out of memory.
Setting this to a big value is sensible only if you have only a few big files that are constantly being re-read (again, HD video editing without enough RAM would be an example case). Official kernel documentation says that &quot;increasing vfs_cache_pressure significantly beyond 100 may have negative performance impact&quot;.
Year 2021 update: After running with kernel version 5.4 for long enough, I've come to the conclusion that the very low vfs_cache_pressure setting (I used to run with 1 for years) may now be causing long stalls / bad latency when memory pressure gets high enough. However, I never noticed such behavior with kernel version 5.3 or lesser.
Year 2022 update: I've been running kernel 5.4.x series for another year and I've come to the conclusion that vfs_cache_pressure has changed permanently. The kernel memory manager behavior that I used to get with kernel version 5.3 or older with values in range 1..5 seems to match real world behavior with 5.4 values in range 100..120. The newer kernels make this adjustment matter more so I'd recommend the value vfs_cache_pressure=120 nowadays for low latency overall. Kernel version 5.3 or older should use a very low but non-zero value here in my opinion.
Exception: if you have a truly massive amount of files and directories and you rarely touch/read/list all files setting vfs_cache_pressure higher than 100 may be wise. This only applies if you do not have enough RAM and cannot keep the whole directory structure in RAM and still have enough RAM for normal file cache and processes (e.g. company wide file server with lots of archival content). If you feel that you need to increase vfs_cache_pressure way above 100 you're running without enough RAM (I have 64 GB RAM on my workstation and 120 seems to be a good setting for minimum latency overall). Increasing vfs_cache_pressure may help a bit but the only real fix is to get more RAM. Having vfs_cache_pressure set to high number sacrifices average performance for having a more stable performance overall (that is, you can avoid really bad worst case behavior but have to deal with worse overall performance).
Finally, tell the kernel to use up to 99% of the RAM as cache for writes and instruct kernel to use up to 50% of RAM before slowing down the process that's writing (default for dirty_background_ratio is 10). Warning: I personally would not do this but you claimed to have enough RAM and are willing to lose the data.
echo 99 &gt; /proc/sys/vm/dirty_ratio
echo 50 &gt; /proc/sys/vm/dirty_background_ratio

And tell that 1h write delay is ok to even start writing stuff on the disk (again, I would not do this):
echo 360000 &gt; /proc/sys/vm/dirty_expire_centisecs
echo 360000 &gt; /proc/sys/vm/dirty_writeback_centisecs

For more information about these tunables, see https://www.kernel.org/doc/Documentation/sysctl/vm.txt
If you put all of those to /etc/rc.local and include following at the end, everything will be in cache as soon as possible after boot (only do this if your filesystem really fits in the RAM):
(nice find / -type f -and -not -path '/sys/*' -and -not -path '/proc/*' -print0 2&gt;/dev/null | nice ionice -c 3 wc -l --files0-from - &gt; /dev/null)&amp;

Or a bit simpler alternative which might work better (cache only /home and /usr, only do this if your /home and /usr really fit in RAM):
(nice find /home /usr -type f -print0 | nice ionice -c 3 wc -l --files0-from - &gt; /dev/null)&amp;

**Reference**: https://unix.stackexchange.com/questions/30286/can-i-configure-my-linux-system-for-more-aggressive-file-system-caching

> 📎 Source: https://unix.stackexchange.com/questions/30286/can-i-configure-my-linux-system-for-more-aggressive-file-system-caching

#### 69. What is this folder /run/user/1000?

**Issue**: What is this folder /run/user/1000?
**Tags / Source**: Tags: linux, fedora, filesystems, directory-structure | unix | 👍 167 | 💬 2 answers

**Description**:
Tags: linux, fedora, filesystems, directory-structure | Score: 167 | Views: 195386 | Answers: 2

**Solution / Community Answer**:
/run/user/$uid is created by pam_systemd and used for storing files used by running processes for that user. These might be things such as your keyring daemon, pulseaudio, etc.

Prior to systemd, these applications typically stored their files in /tmp. They couldn't use a location in /home/$user as home directories are often mounted over network filesystems, and these files should not be shared among hosts. /tmp was the only location specified by the FHS which is local, and writable by all users.

However storing all these files in /tmp is problematic as /tmp is writable by everyone, and while you can change the ownership &amp; mode on the files being created, it's more difficult to work with.

So systemd came along and created /run/user/$uid. This directory is local to the system and only accessible by the target user. So applications looking to store their files locally no longer have to worry about access control.
It also keeps things nice and organized. When a user logs out, and no active sessions remain, pam_systemd will wipe the /run/user/$uid directory out. With various files scattered around /tmp, you couldn't do this.

**Reference**: https://unix.stackexchange.com/questions/162900/what-is-this-folder-run-user-1000

> 📎 Source: https://unix.stackexchange.com/questions/162900/what-is-this-folder-run-user-1000

#### 70. How is Mono magical?

**Issue**: How is Mono magical?
**Tags / Source**: Tags: linux, executable, cross-compilation, mono | unix | 👍 165 | 💬 1 answers

**Description**:
Tags: linux, executable, cross-compilation, mono | Score: 165 | Views: 11848 | Answers: 1

**Solution / Community Answer**:
This is binfmt_misc in action: it allows the kernel to be told how to run binaries it doesn't know about. Look at the contents of /proc/sys/fs/binfmt_misc; among the files you see there, one should explain how to run Mono binaries:

enabled
interpreter /usr/lib/binfmt-support/run-detectors
flags:
offset 0
magic 4d5a


(on a Debian system). This tells the kernel that binaries starting with MZ (4d5a) should be given to run-detectors. The latter figures out whether to use Mono or Wine to run the binary.

Binary types can be added, removed, enabled and disabled at any time; see the documentation above for details (the semantics are surprising, the virtual filesystem used here doesn't behave entirely like a standard filesystem). /proc/sys/fs/binfmt_misc/status gives the global status, and each binary "descriptor" shows its individual status. Another way of disabling binfmt_misc is to unload its kernel module, if it's built as a module; this also means it's possible to blacklist it to avoid it entirely.

This feature allows new binary types to be supported, such as MZ executables (which include Windows PE and PE+ binaries, but also DOS and OS/2 binaries!), Java JAR files... It also allows known binary types to be supported on new architectures, typically using Qemu; thus, with the appropriate libraries, you can transparently run ARM Linux binaries on an Intel processor!

Your question stemmed from cross-compilation, albeit in the .NET sense, and that brings up a caveat with binfmt_misc: some configuration scripts misbehave when you try to cross-compile on a system which can run the cross-compiled binaries. Typically, detecting cross-compilation involves building a binary and attempting to run it; if it runs, you're not cross-compiling, if it doesn't, you are (or your compiler's broken). autoconf scripts can usually be fixed in this case by explicitly specifying the build and host architectures, but sometimes you'll have to disable binfmt_misc temporarily...

**Reference**: https://unix.stackexchange.com/questions/259376/how-is-mono-magical

> 📎 Source: https://unix.stackexchange.com/questions/259376/how-is-mono-magical

#### 71. Difference between pts and tty

**Issue**: Difference between pts and tty
**Tags / Source**: Tags: linux, tty, terminology, who | unix | 👍 164 | 💬 3 answers

**Description**:
Tags: linux, tty, terminology, who | Score: 164 | Views: 176362 | Answers: 3

**Solution / Community Answer**:
A tty is a native terminal device, the backend is either hardware or kernel-emulated.
A pty (pseudo terminal device) is a terminal device which is emulated by another program (example: xterm, screen, or ssh are such programs). A pts is the slave part of a pty.
(More info can be found in man pty.)
Short summary:
A pty is created by a process through posix_openpt() (which usually opens the special device /dev/ptmx), and is constituted by a pair of bidirectional character devices:

The master part, which is the file descriptor obtained by this process through this call, is used to emulate a terminal. After some initialization, the second part can be unlocked with unlockpt(), and the master is used to receive or send characters to this second part (slave).

The slave part, which is anchored in the filesystem as /dev/pts/x (the real name can be obtained by the master through ptsname()) behaves like a native terminal device (/dev/ttyx). In most cases, a shell is started that uses it as a controlling terminal.

**Reference**: https://unix.stackexchange.com/questions/21280/difference-between-pts-and-tty

> 📎 Source: https://unix.stackexchange.com/questions/21280/difference-between-pts-and-tty

#### 72. How to show the filesystem type via the terminal?

**Issue**: How to show the filesystem type via the terminal?
**Tags / Source**: Tags: linux, filesystems | unix | 👍 163 | 💬 2 answers

**Description**:
Tags: linux, filesystems | Score: 163 | Views: 380005 | Answers: 2

**Solution / Community Answer**:
Yes, according to man df you can:


-T, --print-type      print file system type



Another way is to use the mount command. Without parameters it lists the currently mounted devices, including their file systems.

In case you need to find out only one certain file system, is easier to use the stat command's -f option instead of parsing out one value from the above mentioned commands' output.

**Reference**: https://unix.stackexchange.com/questions/53313/how-to-show-the-filesystem-type-via-the-terminal

> 📎 Source: https://unix.stackexchange.com/questions/53313/how-to-show-the-filesystem-type-via-the-terminal

#### 73. How do SO (shared object) numbers work?

**Issue**: How do SO (shared object) numbers work?
**Tags / Source**: Tags: linux, dynamic-linking | unix | 👍 163 | 💬 4 answers

**Description**:
Tags: linux, dynamic-linking | Score: 163 | Views: 123963 | Answers: 4

**Solution / Community Answer**:
Binaries themselves know which version of a shared library they depend on, and request it specifically. You can use ldd to show the dependencies; mine for ls are:

$ ldd /bin/ls
    linux-gate.so.1 =&gt;  (0xb784e000)
    librt.so.1 =&gt; /lib/librt.so.1 (0xb782c000)
    libacl.so.1 =&gt; /lib/libacl.so.1 (0xb7824000)
    libc.so.6 =&gt; /lib/libc.so.6 (0xb76dc000)
    libpthread.so.0 =&gt; /lib/libpthread.so.0 (0xb76c3000)
    /lib/ld-linux.so.2 (0xb784f000)
    libattr.so.1 =&gt; /lib/libattr.so.1 (0xb76bd000)


As you can see, it points to e.g. libpthread.so.0, not just libpthread.so.



The reason for the symbolic link is for the linker. When you want to link against libpthread.so directly, you give gcc the flag -lpthread, and it adds on the lib prefix and .so suffix automatically. You can't tell it to add on the .so.0 suffix, so the symbolic link points to the newest version of the lib to faciliate that

**Reference**: https://unix.stackexchange.com/questions/475/how-do-so-shared-object-numbers-work

> 📎 Source: https://unix.stackexchange.com/questions/475/how-do-so-shared-object-numbers-work

#### 74. How to output only file names (with spaces) in ls -Al?

**Issue**: How to output only file names (with spaces) in ls -Al?
**Tags / Source**: Tags: linux, command-line, ls | unix | 👍 162 | 💬 10 answers

**Description**:
Tags: linux, command-line, ls | Score: 162 | Views: 448811 | Answers: 10

**Solution / Community Answer**:
You really should not parse the output of ls. If this is a homework assignment and you are required to, your professor does not know what they're talking about. Why don't you do something like this:

  The good...

find ./  -printf "%f\n"


or

for n in *; do printf '%s\n' "$n"; done


...the bad...

If you really really want to use ls, you can make it a little bit more robust by doing something like this:

ls -lA | awk -F':[0-9]* ' '/:/{print $2}'


...and the ugly

If you insist on doing it the wrong, dangerous way and just have to use a while loop, do this:

ls -Al | while IFS= read -r string; do echo "$string" | 
    awk -F':[0-9]* ' '/:/{print $2}'; done


Seriously though, just don't.

**Reference**: https://unix.stackexchange.com/questions/70614/how-to-output-only-file-names-with-spaces-in-ls-al

> 📎 Source: https://unix.stackexchange.com/questions/70614/how-to-output-only-file-names-with-spaces-in-ls-al

#### 75. How to see process created by specific user in Unix/linux

**Issue**: How to see process created by specific user in Unix/linux
**Tags / Source**: Tags: linux, process, ps | unix | 👍 161 | 💬 3 answers

**Description**:
Tags: linux, process, ps | Score: 161 | Views: 478947 | Answers: 3

**Solution / Community Answer**:
To view only the processes owned by a specific user, use the following command:

top -U [username]


Replace the [username] with the required username

If you want to use ps then

ps -u [username]


OR

 ps -ef | grep &lt;username&gt;


OR

ps -efl | grep &lt;username&gt;


for the extended listing

Check out the man ps page for options

Another alternative is to use pstree wchich prints the process tree of the user

pstree &lt;username or pid&gt;

**Reference**: https://unix.stackexchange.com/questions/85466/how-to-see-process-created-by-specific-user-in-unix-linux

> 📎 Source: https://unix.stackexchange.com/questions/85466/how-to-see-process-created-by-specific-user-in-unix-linux

#### 76. Long line wrapping in Nano

**Issue**: Long line wrapping in Nano
**Tags / Source**: Tags: ubuntu, nano | unix | 👍 160 | 💬 8 answers

**Description**:
Tags: ubuntu, nano | Score: 160 | Views: 189904 | Answers: 8

**Solution / Community Answer**:
To see the word wrapping style you described, use nano's "soft wrapping": Esc+$.

The Esc+L command you (and everyone) tried does "hard wrapping."

Note on keystroke notation - if you are new to Linux, the notation Esc+$ means press and release Esc and then press $.  The full key press sequence then is Esc, Shift+4.

(It does not mean hold down escape while pressing $.)

Source: https://www.nano-editor.org/dist/v2.9/nano.html (search for --softwrap)


Note on softwrap and formatting mistakes - If you are new to nano, be a little careful of softwrap. If you are editing a configuration file or something else that is sensitive to newlines or indents, formatting mistakes can be made. Until you get comfortable with softwrap’s behaviors, I suggest doing a quick check with softwrap off (do the key sequence again) before saving. 

Note on the goodness provided by others in their answers below - because different operating systems and different versions of nano do things a little differently:


If you like softwrap on all of the time, set it in your .nanorc, as described in x0a's answer below, as it is a bit more through than Prashant's.
If you have a Raspberry Pi, note chainsawmascara's answer about needing an extra keystroke for softwrap to go into effect.
If you have a Mac, like lodeOfCode's answer below, you can always update nano and here, and thus bask in the warm glow of softwrap!


nano linewrap

**Reference**: https://unix.stackexchange.com/questions/122795/long-line-wrapping-in-nano

> 📎 Source: https://unix.stackexchange.com/questions/122795/long-line-wrapping-in-nano

#### 77. List partition labels from the command line

**Issue**: List partition labels from the command line
**Tags / Source**: Tags: linux, command-line, partition, disk | unix | 👍 158 | 💬 14 answers

**Description**:
Tags: linux, command-line, partition, disk | Score: 158 | Views: 326238 | Answers: 14

**Solution / Community Answer**:
with lsblk
For instance, the command
lsblk -o name,mountpoint,label,size,uuid

outputs:
NAME                           MOUNTPOINT     LABEL         SIZE UUID
sda                                                         1.4T
├─sda1                         /boot          boot          953M f557b9f0-edb5-42bb-94d8-27bc03c3c2c7
├─sda2                                                     46.6G 727fa348-8804-4773-ae3d-f3e176d12dac
│ └─sda2_crypt (dm-0)                                      46.6G P1kvJI-5iqv-s9gJ-8V2H-2EEO-q4aK-sx4aDi
│   ├─debian_crypt-swap (dm-1) [SWAP]                         2G 3f9f24d7-86d1-4e21-93e9-f3c181d05cf0
│   ├─debian_crypt-tmp (dm-2)  /tmp           tmp             5G 93fc8219-f985-45fb-bd5c-2c7940a7512d
│   ├─debian_crypt-home (dm-3) /home          home            6G 12e8566c-8f0f-45ec-8524-6d9d9ee91eae
│   └─debian_crypt-root (dm-4) /              root         33.6G 9685570b-4c9e-43ea-815e-49d10dc7a1bf
├─sda3                                                    651.9G d3e0436c-85f6-45c6-9d8f-28b79ee06102
│ └─crypt_gusto (dm-8)         /media/Gusto   Gusto       651.9G 0c084508-cb8b-4b61-832d-6b85273f33c4
├─sda4                                                        1K
├─sda5                                                      298G 5063da5f-9b68-43de-914c-32b89622bcc8
│ └─crypt_kabi (dm-7)          /media/Kabi    Kabi          298G e6a0b66c-8fe9-4e7b-9d54-7b2b430e109d
├─sda6                                                    213.6G 5129d860-bb41-4393-b4b1-f8af53d9155d
│ └─crypt_zami (dm-6)          /media/Zami    Zami        213.6G 19101155-6070-4f37-b39d-19f28867c66b
├─sda7                         /media/Server  Server       85.6G a9f4dae5-901c-4f49-bb30-592de3000713
└─sda8                                                    100.6G dc7f4586-a33d-4707-98e9-8b55c559b0d2
  └─crypt_grafi (dm-5)         /media/Grafi   Grafi       100.6G 5e3242e1-ec7a-4806-92f7-88a126feea94
sdb                                                        14.5G
├─sdb1                                        DEBIAN_LIVE     3G 6bf4d915-2b62-444e-a2c8-16307769b5c2
├─sdb2                                                        2G 90ec6f73-8fdb-4c8d-aebd-cadd0f51b412
│ └─crypt_sdb2 (dm-10)         /mnt           data            2G 91e779dd-0a3f-40b2-8ad0-257d860541a6
└─sdb3                                        linux         9.5G 14a783a4-96dd-4a85-8de7-6e8eea230594
loop0                                                      1000M a3be80bf-0f2c-44ed-8de5-d60e3b19c01a
└─crypt_dropbox (dm-9)         /media/Dropbox Dropbox       998M 8461e2cf-ae17-449b-8ee5-29cc88688b8b
zram0                          [SWAP]                       250M f8254ae5-5ae6-4fda-b8ef-83f25c405894
zram1                          [SWAP]                       250M 7e7ed90d-731c-422a-bf9b-828f09b80502

You can specify plenty of columns in whatever order you like:
Available output columns:
         NAME  device name
        KNAME  internal kernel device name
         PATH  path to the device node
      MAJ:MIN  major:minor device number
      FSAVAIL  filesystem size available
       FSSIZE  filesystem size
       FSTYPE  filesystem type
       FSUSED  filesystem size used
       FSUSE%  filesystem use percentage
      FSROOTS  mounted filesystem roots
        FSVER  filesystem version
   MOUNTPOINT  where the device is mounted
  MOUNTPOINTS  all locations where device is mounted
        LABEL  filesystem LABEL
         UUID  filesystem UUID
       PTUUID  partition table identifier (usually UUID)
       PTTYPE  partition table type
     PARTTYPE  partition type code or UUID
 PARTTYPENAME  partition type name
    PARTLABEL  partition LABEL
     PARTUUID  partition UUID
    PARTFLAGS  partition flags
           RA  read-ahead of the device
           RO  read-only device
           RM  removable device
      HOTPLUG  removable or hotplug device (usb, pcmcia, ...)
        MODEL  device identifier
       SERIAL  disk serial number
         SIZE  size of the device
        STATE  state of the device
        OWNER  user name
        GROUP  group name
         MODE  device node permissions
    ALIGNMENT  alignment offset
       MIN-IO  minimum I/O size
       OPT-IO  optimal I/O size
      PHY-SEC  physical sector size
      LOG-SEC  logical sector size
         ROTA  rotational device
        SCHED  I/O scheduler name
      RQ-SIZE  request queue size
         TYPE  device type
     DISC-ALN  discard alignment offset
    DISC-GRAN  discard granularity
     DISC-MAX  discard max bytes
    DISC-ZERO  discard zeroes data
        WSAME  write same max bytes
          WWN  unique storage identifier
         RAND  adds randomness
       PKNAME  internal parent kernel device name
         HCTL  Host:Channel:Target:Lun for SCSI
         TRAN  device transport type
   SUBSYSTEMS  de-duplicated chain of subsystems
          REV  device revision
       VENDOR  device vendor
        ZONED  zone model
          DAX  dax-capable device

**Reference**: https://unix.stackexchange.com/questions/14165/list-partition-labels-from-the-command-line

> 📎 Source: https://unix.stackexchange.com/questions/14165/list-partition-labels-from-the-command-line

#### 78. Why does /etc/resolv.conf point at 127.0.0.53?

**Issue**: Why does /etc/resolv.conf point at 127.0.0.53?
**Tags / Source**: Tags: linux, dns, resolv.conf | unix | 👍 158 | 💬 3 answers

**Description**:
Tags: linux, dns, resolv.conf | Score: 158 | Views: 318752 | Answers: 3

**Solution / Community Answer**:
You are likely running systemd-resolved as a service.
systemd-resolved generates two configuration files on the fly, for optional use by DNS client libraries (such as the BIND DNS client library in C libraries):

/run/systemd/resolve/stub-resolv.conf tells DNS client libraries to send their queries to 127.0.0.53.  This is where the systemd-resolved process listens for DNS queries, which it then forwards on.
/run/systemd/resolve/resolv.conf tells DNS client libraries to send their queries to IP addresses that systemd-resolved has obtained on the fly from its configuration files and DNS server information contained in DHCP leases.  Effectively, this bypasses the systemd-resolved forwarding step, at the expense of also bypassing all of systemd-resolved's logic for making complex decisions about what to actually forward to, for any given transaction.

In both cases, systemd-resolved configures a search list of domain name suffixes, again derived on the fly from its configuration files and DHCP leases (which it is told about via a mechanism that is beyond the scope of this answer).
/etc/resolv.conf can optionally be:

a symbolic link to either of these;
a symbolic link to a package-supplied static file at /usr/lib/systemd/resolv.conf, which also specifies 127.0.0.53 but no search domains calculated on the fly;
some other file entirely.

It's likely that you have such a symbolic link.
In which case, the thing that knows about the 192.168.1.1 setting, that is (presumably) handed out in DHCP leases by the DHCP server on your LAN, is systemd-resolved, which is forwarding query traffic to it as you have observed.
Your DNS client libraries, in your applications programs, are themselves only talking to systemd-resolved.
Ironically, although it could be that you haven't captured loopback interface traffic to/from 127.0.0.53 properly, it is more likely that you aren't seeing it because systemd-resolved also (optionally) bypasses the BIND DNS Client in your C libraries and generates no such traffic to be captured.
There's an NSS module provided with systemd-resolved, named nss-resolve, that is a plug-in for your C libraries.
Previously, your C libraries would have used another plug-in named nss-dns which uses the BIND DNS Client to make queries using the DNS protocol to the server(s) listed in /etc/resolv.conf, applying the domain suffixes listed therein.
nss-resolve gets listed ahead of nss-dns in your /etc/nsswitch.conf file, causing your C libraries to not use the BIND DNS Client, or the DNS protocol, to perform name→address lookups at all.
Instead, nss-resolve speaks a non-standard and idiosyncratic protocol over the (system-wide) Desktop Bus to systemd-resolved, which again makes back end queries of 192.168.1.1 or whatever your DHCP leases and configuration files say.
To intercept that you have to monitor the Desktop Bus traffic with dbus-monitor or some such tool.
It's not even IP traffic, let alone IP traffic over a loopback network interface. as the Desktop Bus is reached via an AF_LOCAL socket.
If you want to use a third-party resolving proxy DNS server at 1.1.1.1, or some other IP address, you have three choices:

Configure your DHCP server to hand that out instead of handing out 192.168.1.1.  systemd-resolved will learn of that via the DHCP leases and use it.
Configure systemd-resolved via its own configuration mechanisms to use that instead of what it is seeing in the DHCP leases.
Make your own /etc/resolv.conf file, an actual regular file instead of a symbolic link, list 1.1.1.1 there and remember to turn off nss-resolve so that you go back to using nss-dns and the BIND DNS Client.

The systemd-resolved configuration files are a whole bunch of files in various directories that get combined, and how to configure them for the second choice aforementioned is beyond the scope of this answer.
Read the resolved.conf(5) manual page for that.

**Reference**: https://unix.stackexchange.com/questions/612416/why-does-etc-resolv-conf-point-at-127-0-0-53

> 📎 Source: https://unix.stackexchange.com/questions/612416/why-does-etc-resolv-conf-point-at-127-0-0-53

#### 79. How does the OOM killer decide which process to kill first?

**Issue**: How does the OOM killer decide which process to kill first?
**Tags / Source**: Tags: linux, memory, out-of-memory | unix | 👍 157 | 💬 1 answers

**Description**:
Tags: linux, memory, out-of-memory | Score: 157 | Views: 189916 | Answers: 1

**Solution / Community Answer**:
If memory is exhaustively used up by processes, to the extent which can possibly threaten the stability of the system, then the OOM killer comes into the picture.
NOTE: It is the task of the OOM Killer to continue killing processes until enough memory is freed for the smooth functioning of the rest of the process that the Kernel is attempting to run.
The OOM Killer has to select the best process(es) to kill. Best here refers to that process which will free up the maximum memory upon killing and is also the least important to the system.
The primary goal is to kill the least number of processes that minimizes the damage done and at the same time maximizing the amount of memory freed.
To facilitate this, the kernel maintains an oom_score for each of the processes. You can see the oom_score of each of the processes in the /proc filesystem under the pid directory.
$ cat /proc/10292/oom_score

The higher the value of oom_score of any process, the higher is its likelihood of getting killed by the OOM Killer in an out-of-memory situation.
How is the OOM_Score calculated?

In David's patch set, the old badness() heuristics are almost entirely
gone. Instead, the calculation turns into a simple question of what
percentage of the available memory is being used by the process. If
the system as a whole is short of memory, then &quot;available memory&quot; is
the sum of all RAM and swap space available to the system.
If instead, the OOM situation is caused by exhausting the memory allowed
to a given cpuset/control group, then &quot;available memory&quot; is the total
amount allocated to that control group. A similar calculation is made
if limits imposed by a memory policy have been exceeded. In each case,
the memory use of the process is deemed to be the sum of its resident
set (the number of RAM pages it is using) and its swap usage.
This calculation produces a percent-times-ten number as a result; a
process which is using every byte of the memory available to it will
have a score of 1000, while a process using no memory at all will get
a score of zero. There are very few heuristic tweaks to this score,
but the code does still subtract a small amount (30) from the score of
root-owned processes on the notion that they are slightly more
valuable than user-owned processes.
One other tweak which is applied is to add the value stored in each
process's oom_score_adj variable, which can be adjusted via /proc.
This knob allows the adjustment of each process's attractiveness to
the OOM killer in user space; setting it to -1000 will disable OOM
kills entirely, while setting to +1000 is the equivalent of painting a
large target on the associated process.

References
http://www.queryhome.com/15491/whats-happening-kernel-starting-killer-choose-which-process
https://serverfault.com/a/571326

**Reference**: https://unix.stackexchange.com/questions/153585/how-does-the-oom-killer-decide-which-process-to-kill-first

> 📎 Source: https://unix.stackexchange.com/questions/153585/how-does-the-oom-killer-decide-which-process-to-kill-first

#### 80. Show top five CPU consuming processes with `ps`

**Issue**: Show top five CPU consuming processes with `ps`
**Tags / Source**: Tags: linux, ps | unix | 👍 156 | 💬 13 answers

**Description**:
Tags: linux, ps | Score: 156 | Views: 520011 | Answers: 13

**Solution / Community Answer**:
Why use ps when you can do it easily with the top command?

If you must use ps, try this:

ps aux | sort -nrk 3,3 | head -n 5


If you want something that's truly 'top'esq with constant updates, use watch

watch "ps aux | sort -nrk 3,3 | head -n 5"

**Reference**: https://unix.stackexchange.com/questions/13968/show-top-five-cpu-consuming-processes-with-ps

> 📎 Source: https://unix.stackexchange.com/questions/13968/show-top-five-cpu-consuming-processes-with-ps

#### 81. How do I kill all screens?

**Issue**: How do I kill all screens?
**Tags / Source**: Tags: linux, bash, gnu-screen, kill | unix | 👍 153 | 💬 8 answers

**Description**:
Tags: linux, bash, gnu-screen, kill | Score: 153 | Views: 467444 | Answers: 8

**Solution / Community Answer**:
You can use :

pkill screen


Or 

killall screen




In OSX the process is called SCREEN in all caps. So, use:

pkill SCREEN


Or

killall SCREEN

**Reference**: https://unix.stackexchange.com/questions/94527/how-do-i-kill-all-screens

> 📎 Source: https://unix.stackexchange.com/questions/94527/how-do-i-kill-all-screens

#### 82. How can I look up a username by id in linux?

**Issue**: How can I look up a username by id in linux?
**Tags / Source**: Tags: linux, ubuntu, users, uuid | unix | 👍 146 | 💬 8 answers

**Description**:
Tags: linux, ubuntu, users, uuid | Score: 146 | Views: 362675 | Answers: 8

**Solution / Community Answer**:
You might enjoy this little ditty. 

$ id -nu [number]


3.17.3-1-ARCH #1 SMP PREEMPT Fri Nov 14 22:56:01 CET 2014 i686 GNU/Linux

I can confirm that it returns a corresponding user name, if one exists, on Arch Linux. I can also confirm that it does not work on Ubuntu when run as a normal user, although I have not tested this as the superuser. It also does not work on Alpine Linux. Maybe a security feature prevents this from working on some systems.

**Reference**: https://unix.stackexchange.com/questions/36580/how-can-i-look-up-a-username-by-id-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/36580/how-can-i-look-up-a-username-by-id-in-linux

#### 83. Difference between /bin and /usr/bin

**Issue**: Difference between /bin and /usr/bin
**Tags / Source**: Tags: linux, directory, fhs | unix | 👍 144 | 💬 5 answers

**Description**:
Tags: linux, directory, fhs | Score: 144 | Views: 160721 | Answers: 5

**Solution / Community Answer**:
What? no /bin/ is not a symlink to /usr/bin on any FHS compliant system. Note that there are still popular Unices and Linuxes that ignore this - for example, /bin and /sbin are symlinked to /usr/bin on Arch Linux (the reasoning being that you don't need /bin for rescue/single-user-mode, since you'd just boot a live CD).

/bin

contains commands that may be used by both the system administrator and by users, but which are required when no other filesystems are mounted (e.g. in single user mode). It may also contain commands which are used indirectly by scripts

/usr/bin/

This is the primary directory of executable commands on the system.

essentially, /bin contains executables which are required by the system for emergency repairs, booting, and single user mode. /usr/bin contains any binaries that aren't required.

I will note, that they can be on separate disks/partitions, /bin must be on the same disk as /. /usr/bin can be on another disk - although note that this configuration has been kind of broken for a while (this is why e.g. systemd warns about this configuration on boot).

For full correctness, some unices may ignore FHS, as I believe it is only a Linux Standard, I'm not aware that it has yet been included in SUS, Posix or any other UNIX standard, though it should be IMHO. It is a part of the LSB standard though.

**Reference**: https://unix.stackexchange.com/questions/5915/difference-between-bin-and-usr-bin

> 📎 Source: https://unix.stackexchange.com/questions/5915/difference-between-bin-and-usr-bin

#### 84. How do I know if a partition is ext2, ext3, or ext4?

**Issue**: How do I know if a partition is ext2, ext3, or ext4?
**Tags / Source**: Tags: linux, ext4, ext3, ext2 | unix | 👍 143 | 💬 12 answers

**Description**:
Tags: linux, ext4, ext3, ext2 | Score: 143 | Views: 229365 | Answers: 12

**Solution / Community Answer**:
How do I tell what sort of data (what data format) is in a file?
→ Use the file utility.

Here, you want to know the format of data in a device file, so you need to pass the -s flag to tell file not just to say that it's a device file but look at the content. Sometimes you'll need the -L flag as well, if the device file name is a symbolic link. You'll see output like this:

# file -sL /dev/sd*
/dev/sda1: Linux rev 1.0 ext4 filesystem data, UUID=63fa0104-4aab-4dc8-a50d-e2c1bf0fb188 (extents) (large files) (huge files)
/dev/sdb1: Linux rev 1.0 ext2 filesystem data, UUID=b3c82023-78e1-4ad4-b6e0-62355b272166
/dev/sdb2: Linux/i386 swap file (new style), version 1 (4K pages), size 4194303 pages, no label, UUID=3f64308c-19db-4da5-a9a0-db4d7defb80f


Given this sample output, the first disk has one partition and the second disk has two partitions. /dev/sda1 is an ext4 filesystem, /dev/sdb1 is an ext2 filesystem, and /dev/sdb2 is some swap space (about 4GB).

You must run this command as root, because ordinary users may not read disk partitions directly: if needed, add sudo in front.

**Reference**: https://unix.stackexchange.com/questions/60723/how-do-i-know-if-a-partition-is-ext2-ext3-or-ext4

> 📎 Source: https://unix.stackexchange.com/questions/60723/how-do-i-know-if-a-partition-is-ext2-ext3-or-ext4

#### 85. How can I tell what version of Linux I&#39;m using?

**Issue**: How can I tell what version of Linux I&#39;m using?
**Tags / Source**: Tags: linux, ssh, version, info, system-information | unix | 👍 142 | 💬 13 answers

**Description**:
Tags: linux, ssh, version, info, system-information | Score: 142 | Views: 175458 | Answers: 13

**Solution / Community Answer**:
If I need to know what it is say Linux/Unix , 32/64 bit

uname -a 


This would give me almost all information that I need, 

If I further need to know what release it is say (Centos 5.4, or 5.5 or 5.6)
on a Linux box I would further check the file /etc/issue to see its release info ( or for Debian / Ubuntu /etc/lsb-release )

Alternative way is to use the lsb_release utility:

lsb_release -a


Or do a rpm -qa | grep centos-release or redhat-release for RHEL derived systems

**Reference**: https://unix.stackexchange.com/questions/23833/how-can-i-tell-what-version-of-linux-im-using

> 📎 Source: https://unix.stackexchange.com/questions/23833/how-can-i-tell-what-version-of-linux-im-using

#### 86. What is the difference between reboot , init 6 and shutdown -r now?

**Issue**: What is the difference between reboot , init 6 and shutdown -r now?
**Tags / Source**: Tags: linux, shutdown, init, reboot | unix | 👍 142 | 💬 4 answers

**Description**:
Tags: linux, shutdown, init, reboot | Score: 142 | Views: 415220 | Answers: 4

**Solution / Community Answer**:
There is no difference in them. Internally they do exactly the same thing:


reboot uses the shutdown command (with the -r switch). The shutdown command used to kill all the running processes, unmount all the file systems and finally tells the kernel to issue the ACPI power command. The source can be found here.
In older distros the reboot command was forcing the processes to exit by issuing the SIGKILL signal (still found in sources, can be invoked with -f option), in most recent distros it defaults to the more graceful and init friendly init 1 -&gt; shutdown -r. This ensures that daemons clean up themselves before shutdown.
init 6 tells the init process to shutdown all of the spawned processes/daemons as written in the init files (in the inverse order they started) and lastly invoke the shutdown -r now command to reboot the machine


Today there is not much difference as both commands do exactly the same, and they respect the init scripts used to start services/daemons by invoking the shutdown scripts for them. Except for reboot -f -r now as stated below

There is a small explanation taken from manpages of why the reboot -f is not safe:


  -f, --force
    Force immediate halt, power-off, reboot. Don't contact the init system.


Edit:

Forgot to mention, in upcoming RHEL distributions you should use the new systemctl command to issue poweroff/reboot. As stated in the manpages of reboot and shutdown they are "a legacy command available for compatibility only." and the systemctl method will be the only one safe.

**Reference**: https://unix.stackexchange.com/questions/64280/what-is-the-difference-between-reboot-init-6-and-shutdown-r-now

> 📎 Source: https://unix.stackexchange.com/questions/64280/what-is-the-difference-between-reboot-init-6-and-shutdown-r-now

#### 87. Linux ls to show only file name, date, and size

**Issue**: Linux ls to show only file name, date, and size
**Tags / Source**: Tags: linux, command-line, files, ls | unix | 👍 141 | 💬 15 answers

**Description**:
Tags: linux, command-line, files, ls | Score: 141 | Views: 248431 | Answers: 15

**Solution / Community Answer**:
Try stat instead of ls. Here with the GNU implementation of stat (beware the BSDs and zsh also have a stat command but with a completely different API):
stat -c &quot;%y %s %n&quot; -- *

To output in columnar format (assuming none of the file names contain comma or newline characters):
stat -c &quot;%n,%s&quot; -- * | column -t -s,

Beware that if there's a file called - in the current working directory, GNU stat will report information about the file opened on stdin instead of for that file.
If you run into a Argument list too long error, with shells where printf is builtin, you can change it to:
printf '%s\0' * | xargs -0 stat -c &quot;%y %s %n&quot; --

Or in ksh93:
command -x stat -c &quot;%y %s %n&quot; -- *

Which will run as many invocations of stat as necessary to work around the limit on the size of the arguments.

**Reference**: https://unix.stackexchange.com/questions/22218/linux-ls-to-show-only-file-name-date-and-size

> 📎 Source: https://unix.stackexchange.com/questions/22218/linux-ls-to-show-only-file-name-date-and-size

#### 88. File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)

**Issue**: File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)
**Tags / Source**: Tags: ubuntu, permissions, virtualbox, virtual-machine | unix | 👍 141 | 💬 10 answers

**Description**:
Tags: ubuntu, permissions, virtualbox, virtual-machine | Score: 141 | Views: 333935 | Answers: 10

**Solution / Community Answer**:
The regular way of getting access to the files now, is to allow VirtualBox to automount the shared folder (which will make it show up under /media/sf_directory_name) and then to add your regular Ubuntu user to the vboxsf group (as root #).

# usermod -aG vboxsf &lt;youruser&gt;


By default, without manual action, the mounts look like this,

drwxrwx--- 1 root vboxsf 40960 Oct 23 10:42 sf_&lt;name&gt;


so the vboxsf group has full access.  By adding your user to that group, you gain full access.  So you wouldn't worry about changing their permissions (which don't make sense on the Windows host), you just give yourself access.

In this specific case, this is the automounted Shared Folder,

Ubuntu               214153212  31893804 182259408  15% /media/sf_Ubuntu


and it is that directory that should be used to access to the Shared Folder, by putting the local user into the vboxsf group.  If you want a 'better' link under your user's home directory, you could always create a symbolic link.

ln -s /media/sf_Ubuntu /home/m/Desktop/vbox_shared


You will need to reboot your VM for these changes to take effect

If you manually mount the shared folder, then you need to use the relevant options on the mount command to set the folder with the right ownership (i.e. the gid, uid and umask options to mount).  This is because the Host OS doesn't support the same permission system as Linux, so VirtualBox has no way of knowing who should own the files.

However, I strongly recommend just configuring the shared folder to be auto-mounted (it's a setting on the Shared Folder configuration in VirtualBox itself).


For the avoidance of doubt, I do not believe you can change permissions normally anyway, on that filesystem if it's mounted in the regular way,

tony@jabba:/media/sf_name$ ls -l tst.txt
-rwxrwx--- 1 root vboxsf 2283 Apr  4  2012 tst.txt
tony@jabba:/media/sf_name$ sudo chown tony tst.txt
[sudo] password for tony: 
tony@jabba:/media/sf_name$ ls -l tst.txt
-rwxrwx--- 1 root vboxsf 2283 Apr  4  2012 tst.txt
tony@jabba:/media/sf_name$

**Reference**: https://unix.stackexchange.com/questions/52667/file-permission-issues-with-shared-folders-under-virtual-box-ubuntu-guest-wind

> 📎 Source: https://unix.stackexchange.com/questions/52667/file-permission-issues-with-shared-folders-under-virtual-box-ubuntu-guest-wind

#### 89. Set the default kernel in GRUB

**Issue**: Set the default kernel in GRUB
**Tags / Source**: Tags: linux, kernel, boot, grub | unix | 👍 140 | 💬 11 answers

**Description**:
Tags: linux, kernel, boot, grub | Score: 140 | Views: 428583 | Answers: 11

**Solution / Community Answer**:
After struggling for 2 hours, I have found a much easier way to achieve this. I just RTFM. ;)
Add two lines to /etc/default/grub
GRUB_SAVEDEFAULT=true
GRUB_DEFAULT=saved

Do the sudo update-grub, reboot, get into your grub menu and select whichever menu or submenu item you need. The choice will be saved every time and then your computer will boot into it automatically. When you manually choose a different entry, that becomes the new default.

**Reference**: https://unix.stackexchange.com/questions/198003/set-the-default-kernel-in-grub

> 📎 Source: https://unix.stackexchange.com/questions/198003/set-the-default-kernel-in-grub

#### 90. How do I find how long ago a Linux system was installed?

**Issue**: How do I find how long ago a Linux system was installed?
**Tags / Source**: Tags: linux, system-installation | unix | 👍 139 | 💬 18 answers

**Description**:
Tags: linux, system-installation | Score: 139 | Views: 151247 | Answers: 18

**Solution / Community Answer**:
sudo tune2fs -l /dev/sda1 **OR** /dev/sdb1*  | grep 'Filesystem created:'

This will tell you when the file system was created.
* = In the first column of df / you can find the exact partition to use.

**Reference**: https://unix.stackexchange.com/questions/9971/how-do-i-find-how-long-ago-a-linux-system-was-installed

> 📎 Source: https://unix.stackexchange.com/questions/9971/how-do-i-find-how-long-ago-a-linux-system-was-installed

#### 91. timestamp, modification time, and created time of a file

**Issue**: timestamp, modification time, and created time of a file
**Tags / Source**: Tags: linux, filesystems, files | unix | 👍 138 | 💬 2 answers

**Description**:
Tags: linux, filesystems, files | Score: 138 | Views: 352604 | Answers: 2

**Solution / Community Answer**:
There are 3 kind of "timestamps":


Access - the last time the file was read
Modify - the last time the file was modified (content has been modified)
Change - the last time meta data of the file was changed (e.g. permissions)


To display this information, you can use stat which is part of the coreutils.

stat will show you also some more information like the device, inodes, links, etc.

Remember that this sort of information depends highly on the filesystem and mount options. For example if you mount a partition with the noatime option, no access information will be written.

A utility to change the timestamps would be touch.
There are some arguments to decide which timestamp to change (e.g. -a for access time, -m for modification time) and to influence the parsing of a new given timestamp.
See man touch for more details.

touch can become handy in combination with cp -u ("copy only when the SOURCE file is newer than the destination file or when the destination file is missing") or for the creation of empty marker files.

**Reference**: https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file

> 📎 Source: https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file

#### 92. Easy way to determine the virtualization technology of a Linux machine?

**Issue**: Easy way to determine the virtualization technology of a Linux machine?
**Tags / Source**: Tags: linux, command-line, virtual-machine | unix | 👍 137 | 💬 17 answers

**Description**:
Tags: linux, command-line, virtual-machine | Score: 137 | Views: 130239 | Answers: 17

**Solution / Community Answer**:
dmidecode -s system-product-name

I have tested on Vmware Workstation, VirtualBox, QEMU with KVM, standalone QEMU with Ubuntu as the guest OS. Others have added additional platforms that they're familiar with as well.

Virtualization technologies


VMware Workstation

root@router:~# dmidecode -s system-product-name
VMware Virtual Platform

VirtualBox

root@router:~# dmidecode -s system-product-name
VirtualBox

Qemu with KVM

root@router:~# dmidecode -s system-product-name
KVM

Qemu (emulated)

root@router:~# dmidecode -s system-product-name
Bochs

Microsoft VirtualPC

root@router:~# dmidecode | egrep -i 'manufacturer|product'
Manufacturer: Microsoft Corporation
Product Name: Virtual Machine

Virtuozzo

root@router:~# dmidecode
/dev/mem: Permission denied

Xen

root@router:~# dmidecode | grep -i domU
Product Name: HVM domU



On bare metal, this returns an identification of the computer or motherboard model.

/dev/disk/by-id

If you don't have the rights to run dmidecode then you can use:

Virtualization Technology: QEMU

ls -1 /dev/disk/by-id/


Output

[root@host-7-129 ~]# ls -1 /dev/disk/by-id/
ata-QEMU_DVD-ROM_QM00003
ata-QEMU_HARDDISK_QM00001
ata-QEMU_HARDDISK_QM00001-part1
ata-QEMU_HARDDISK_QM00002
ata-QEMU_HARDDISK_QM00002-part1
scsi-SATA_QEMU_HARDDISK_QM00001
scsi-SATA_QEMU_HARDDISK_QM00001-part1
scsi-SATA_QEMU_HARDDISK_QM00002
scsi-SATA_QEMU_HARDDISK_QM00002-part1


References


How to detect virtualization at dmo.ca

**Reference**: https://unix.stackexchange.com/questions/89714/easy-way-to-determine-the-virtualization-technology-of-a-linux-machine

> 📎 Source: https://unix.stackexchange.com/questions/89714/easy-way-to-determine-the-virtualization-technology-of-a-linux-machine

#### 93. What&#39;s the best way to join files again after splitting them?

**Issue**: What&#39;s the best way to join files again after splitting them?
**Tags / Source**: Tags: linux, command-line, files, iso, split | unix | 👍 135 | 💬 6 answers

**Description**:
Tags: linux, command-line, files, iso, split | Score: 135 | Views: 214610 | Answers: 6

**Solution / Community Answer**:
That's just what cat was made for. Since it is one of the oldest GNU tools, I think it's very unlikely that any other tool does that faster/better. And it's not piping - it's only redirecting output.

**Reference**: https://unix.stackexchange.com/questions/24630/whats-the-best-way-to-join-files-again-after-splitting-them

> 📎 Source: https://unix.stackexchange.com/questions/24630/whats-the-best-way-to-join-files-again-after-splitting-them

#### 94. Linux: set date through command line

**Issue**: Linux: set date through command line
**Tags / Source**: Tags: linux, date, clock | unix | 👍 134 | 💬 7 answers

**Description**:
Tags: linux, date, clock | Score: 134 | Views: 757612 | Answers: 7

**Solution / Community Answer**:
Use date -s:

date -s '2014-12-25 12:34:56'


Run that as root or under sudo. Changing only one of the year/month/day is more of a challenge and will involve repeating bits of the current date. There are also GUI date tools built in to the major desktop environments, usually accessed through the clock.

To change only part of the time, you can use command substitution in the date string:

date -s "2014-12-25 $(date +%H:%M:%S)"


will change the date, but keep the time. See man date for formatting details to construct other combinations: the individual components are %Y, %m, %d, %H, %M, and %S.

**Reference**: https://unix.stackexchange.com/questions/151547/linux-set-date-through-command-line

> 📎 Source: https://unix.stackexchange.com/questions/151547/linux-set-date-through-command-line

#### 95. How can I find available network interfaces?

**Issue**: How can I find available network interfaces?
**Tags / Source**: Tags: linux, networking, devices, systemd, udev | unix | 👍 134 | 💬 6 answers

**Description**:
Tags: linux, networking, devices, systemd, udev | Score: 134 | Views: 512358 | Answers: 6

**Solution / Community Answer**:
The simplest method I know to list all of your interfaces is

ifconfig -a


EDIT

If you're on a system where that has been made obsolete, you can use

ip link show

**Reference**: https://unix.stackexchange.com/questions/125400/how-can-i-find-available-network-interfaces

> 📎 Source: https://unix.stackexchange.com/questions/125400/how-can-i-find-available-network-interfaces

#### 96. Setting /proc/sys/vm/drop_caches to clear cache

**Issue**: Setting /proc/sys/vm/drop_caches to clear cache
**Tags / Source**: Tags: linux, virtual-memory | unix | 👍 134 | 💬 2 answers

**Description**:
Tags: linux, virtual-memory | Score: 134 | Views: 307376 | Answers: 2

**Solution / Community Answer**:
It isn't sticky - you just write to the file to make it drop the caches and then it immediately starts caching again.

Basically when you write to that file you aren't really changing a setting, you are issuing a command to the kernel. The kernel acts on that command (by dropping the caches) then carries on as before.

**Reference**: https://unix.stackexchange.com/questions/17936/setting-proc-sys-vm-drop-caches-to-clear-cache

> 📎 Source: https://unix.stackexchange.com/questions/17936/setting-proc-sys-vm-drop-caches-to-clear-cache

#### 97. What is a tainted Linux kernel?

**Issue**: What is a tainted Linux kernel?
**Tags / Source**: Tags: linux, linux-kernel, kernel-modules, troubleshooting, proprietary-drivers | unix | 👍 134 | 💬 2 answers

**Description**:
Tags: linux, linux-kernel, kernel-modules, troubleshooting, proprietary-drivers | Score: 134 | Views: 207611 | Answers: 2

**Solution / Community Answer**:
A tainted kernel is one that is in an unsupported state because it cannot be guaranteed to function correctly. Most kernel developers will ignore bug reports involving tainted kernels, and community members may ask that you correct the tainting condition before they can proceed with diagnosing problems related to the kernel. In addition, some debugging functionality and API calls may be disabled when the kernel is tainted.
The taint state is indicated by a series of flags which represent the various reasons a kernel cannot be trusted to work properly. The most common reason for the kernel to become tainted is loading a proprietary graphics driver from NVIDIA or AMD, in which case it is generally safe to ignore the condition. However, some scenarios that cause the kernel to become tainted may be indicative of more serious problems such as failing hardware. It is a good idea to examine system logs and the specific taint flags set to determine the underlying cause of the issue.
This feature is intended to identify conditions which may make it difficult to properly troubleshoot a kernel problem. For example, a proprietary driver can cause problems that cannot be debugged reliably because its source code is not available and its effects cannot be determined. Likewise, if a serious kernel or hardware error had previously occurred, the integrity of the kernel space may have been compromised, meaning that any subsequent debug messages generated by the kernel may not be reliable.
Note that correcting the tainting condition alone does not remove the taint state because doing so does not change the fact that the kernel can no longer be relied on to work correctly or produce accurate debugging information. The system must be restarted to clear the taint flags.
More information is available in the Linux kernel documentation, including what each taint flag means and how to troubleshoot a tainted kernel prior to reporting bugs.
A partial list of conditions that can result in the kernel being tainted follows, each with their own flags. Note that some Linux vendors, such as SUSE, add additional taint flags to indicate conditions such as loading a module that is supported by a third party rather than directly by the vendor.

Loading a proprietary (or non-GPL-compatible) kernel module. As noted above, this is the most common reason for the kernel to become tainted.
The use of staging drivers, which are part of the kernel source code but are experimental and not fully tested.
The use of out-of-tree modules that are not included with the Linux kernel source code.
Forcibly loading or unloading modules. This can happen if one is trying to use a module that is not built for the current version of the kernel. (The Linux kernel module ABI is not stable across versions, or even differently-configured builds of the same version.)
Running a kernel on certain hardware configurations that are specifically not supported, such as an SMP (multiprocessor) kernel on early AMD Athlon processors not supporting SMP operation.
Overriding the ACPI DSDT in the kernel. This is sometimes needed to correct for firmware power-management bugs; see this Arch Linux wiki article for details.
Certain critical error conditions, such as machine check exceptions and kernel oopses.
Certain serious bugs in the BIOS, UEFI, or other system firmware which the kernel must work around.

**Reference**: https://unix.stackexchange.com/questions/118116/what-is-a-tainted-linux-kernel

> 📎 Source: https://unix.stackexchange.com/questions/118116/what-is-a-tainted-linux-kernel

#### 98. ssh-add returns with: &quot;Error connecting to agent: No such file or directory&quot;

**Issue**: ssh-add returns with: &quot;Error connecting to agent: No such file or directory&quot;
**Tags / Source**: Tags: linux, ssh, ssh-agent | unix | 👍 133 | 💬 5 answers

**Description**:
Tags: linux, ssh, ssh-agent | Score: 133 | Views: 264530 | Answers: 5

**Solution / Community Answer**:
The client tool ssh-add wants to communicate with the background process ssh-agent. You need to start the ssh-agent process first. On Linux, a shell uses the environment variables SSH_AUTH_SOCK and SSH_AGENT_PID to identify the correct process to talk to.
You can start ssh-agent in multiple ways.
Either by starting a new shell
ssh-agent bash

or by evaluating the script returned by ssh-agent in your current shell.
eval &quot;$(ssh-agent)&quot;

I suggest using the second method, because you keep all your history and variables.

**Reference**: https://unix.stackexchange.com/questions/464574/ssh-add-returns-with-error-connecting-to-agent-no-such-file-or-directory

> 📎 Source: https://unix.stackexchange.com/questions/464574/ssh-add-returns-with-error-connecting-to-agent-no-such-file-or-directory

#### 99. How to check which GPU is active in Linux?

**Issue**: How to check which GPU is active in Linux?
**Tags / Source**: Tags: linux, hardware, graphics | unix | 👍 133 | 💬 12 answers

**Description**:
Tags: linux, hardware, graphics | Score: 133 | Views: 454435 | Answers: 12

**Solution / Community Answer**:
I've just gone through a hell of a time
trying to get my discrete graphics to work in Ubuntu,
and answering this question was constantly a challenge,
since the lspci method mentioned earlier
can sometimes say that both are [VGA controller].
I think the following command should give you an indication of your active chip:
$ glxinfo | grep -E &quot;OpenGL vendor|OpenGL renderer&quot;
OpenGL vendor string: Intel Open Source Technology Center
OpenGL renderer string: Mesa DRI Intel(R) Sandybridge Mobile

For me, this is telling me that my Intel graphics are running the show.
glxinfo is available from the mesa-utils package,
so you will need to install it if you haven't already. 
On Ubuntu 22.04, for example, run:
sudo apt-get install mesa-utils

If you're using an NVIDIA chip, and you're using the bumblebee package,
you can put optirun in front of that line,
and it should tell you that you're running the NVIDIA chip
(optirun is basically telling the computer
to use the discrete chip to run whatever command follows,
but everything else is still using the integrated chip).
$ optirun glxinfo | grep -E &quot;OpenGL vendor|OpenGL renderer&quot;
OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: GeForce GT 555M/PCIe/SSE2

glxheads is another helpful command from mesa-utils that tells you
some useful information about which graphics card is in use
(mostly repeats glxinfo in a more compact and easy-to-read form, though),
and it gives you a nice rendering of a rotating triangle.

**Reference**: https://unix.stackexchange.com/questions/16407/how-to-check-which-gpu-is-active-in-linux

> 📎 Source: https://unix.stackexchange.com/questions/16407/how-to-check-which-gpu-is-active-in-linux

#### 100. What&#39;s the difference between /usr/lib/systemd/system and /etc/systemd/system?

**Issue**: What&#39;s the difference between /usr/lib/systemd/system and /etc/systemd/system?
**Tags / Source**: Tags: debian, ubuntu, centos, systemd | unix | 👍 133 | 💬 3 answers

**Description**:
Tags: debian, ubuntu, centos, systemd | Score: 133 | Views: 116937 | Answers: 3

**Solution / Community Answer**:
This question is already answered in man 7 file-hierarchy which comes with systemd (there is also online version):

        /etc
           System-specific configuration.
 (…)
 VENDOR-SUPPLIED OPERATING SYSTEM RESOURCES
       /usr
            Vendor-supplied operating system resources. 
            Usually read-only, but this is not required. Possibly 
            shared between multiple hosts. This directory should not
            be modified by the administrator, except when installing 
            or removing vendor-supplied packages.


Basically, files that ships in packages downloaded from distribution repository go into /usr/lib/systemd/. Modifications done by system administrator (user) go into /etc/systemd/system/. 

System-specific units override units supplied by vendors. Using drop-ins, you can override only specific parts of unit files, leaving the rest to vendor (drop-ins are available since the very beginning of systemd, but were properly documented only in v219; see man systemd.unit).

**Reference**: https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system

> 📎 Source: https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
