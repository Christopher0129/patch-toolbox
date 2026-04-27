# Linux 常见故障及解决方法 | Linux Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 02:13:52 UTC_

## 中文 🇨🇳
**Linux 常见故障及解决方法**

本页面每小时自动从 Stack Exchange 社区抓取 LINUX 平台常见故障及解决方法。

### LINUX 常见故障及解决方法

#### 1. How do I make `ls` show file sizes in megabytes?

**故障现象**: How do I make `ls` show file sizes in megabytes?
**标签 / 来源**: Tags: linux, ls | unix | 👍 936 | 💬 2 answers

**问题描述**:
Tags: linux, ls | Score: 936 | Views: 2451279 | Answers: 2

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
Tags: linux, process, ip, netstat | Score: 831 | Views: 2194648 | Answers: 8

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
Tags: ubuntu, centos, ssh, sshd, key-authentication | Score: 745 | Views: 1428792 | Answers: 32

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
Tags: linux, permissions, directory | Score: 536 | Views: 403914 | Answers: 9

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
Tags: linux, x11, wayland | Score: 514 | Views: 702754 | Answers: 15

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
Tags: linux, backup, tar | Score: 505 | Views: 1359503 | Answers: 2

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
Tags: linux, kernel, performance, cache, ram | Score: 419 | Views: 985957 | Answers: 1

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
Tags: linux, cpu | Score: 384 | Views: 815326 | Answers: 12

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
Tags: linux, permissions, directory | Score: 379 | Views: 714955 | Answers: 5

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
Tags: linux, disk | Score: 378 | Views: 1059518 | Answers: 11

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
Tags: linux, filesystems, find, rm | Score: 318 | Views: 291413 | Answers: 2

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
Tags: linux, hardware, devices, hard-disk | Score: 313 | Views: 1391057 | Answers: 16

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
Tags: linux, memory, top, meminfo | Score: 309 | Views: 477595 | Answers: 9

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
Tags: linux, storage | Score: 303 | Views: 1002557 | Answers: 13

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
Tags: linux, hard-disk, block-device, ssd | Score: 302 | Views: 448328 | Answers: 10

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
Tags: linux, command-line, files, rm | Score: 297 | Views: 507560 | Answers: 24

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
Tags: linux, cpu, arm, x86 | Score: 283 | Views: 215280 | Answers: 6

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
Tags: linux, kernel, inotify | Score: 282 | Views: 226435 | Answers: 2

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
Tags: linux, cpu, top | Score: 273 | Views: 460224 | Answers: 3

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
Tags: linux, filesystems, mount | Score: 264 | Views: 1131822 | Answers: 5

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
Tags: linux, memory, ulimit | Score: 263 | Views: 436682 | Answers: 12

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
Tags: linux, ps | Score: 260 | Views: 542981 | Answers: 4

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
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622620 | Answers: 21

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
Tags: linux, command-line, logs, dmesg | Score: 243 | Views: 336443 | Answers: 7

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
Tags: linux, command-line, memory, hardware | Score: 237 | Views: 284544 | Answers: 5

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
Tags: linux, files, diff | Score: 228 | Views: 325424 | Answers: 6

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
Tags: linux, permissions, su, conventions | Score: 221 | Views: 135871 | Answers: 4

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
Tags: linux, unix, history | Score: 213 | Views: 116072 | Answers: 9

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
Tags: linux, filesystems, io, async | Score: 209 | Views: 118843 | Answers: 8

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
Tags: linux, filesystems, ln | Score: 202 | Views: 505510 | Answers: 6

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
Tags: linux, desktop, freeze | Score: 202 | Views: 673972 | Answers: 10

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
Tags: linux, data-recovery, deleted-files | Score: 202 | Views: 1208038 | Answers: 14

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


---

## English 🇺🇸
**Linux Common Issues & Solutions**

Auto-updated hourly from Stack Exchange: common LINUX issues and community-verified solutions.

### LINUX Common Issues & Solutions

#### 1. How do I make `ls` show file sizes in megabytes?

**Issue**: How do I make `ls` show file sizes in megabytes?
**Tags / Source**: Tags: linux, ls | unix | 👍 936 | 💬 2 answers

**Description**:
Tags: linux, ls | Score: 936 | Views: 2451279 | Answers: 2

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
Tags: linux, process, ip, netstat | Score: 831 | Views: 2194648 | Answers: 8

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
Tags: ubuntu, centos, ssh, sshd, key-authentication | Score: 745 | Views: 1428792 | Answers: 32

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
Tags: linux, permissions, directory | Score: 536 | Views: 403914 | Answers: 9

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
Tags: linux, x11, wayland | Score: 514 | Views: 702754 | Answers: 15

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
Tags: linux, backup, tar | Score: 505 | Views: 1359503 | Answers: 2

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
Tags: linux, kernel, performance, cache, ram | Score: 419 | Views: 985957 | Answers: 1

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
Tags: linux, cpu | Score: 384 | Views: 815326 | Answers: 12

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
Tags: linux, permissions, directory | Score: 379 | Views: 714955 | Answers: 5

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
Tags: linux, disk | Score: 378 | Views: 1059518 | Answers: 11

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
Tags: linux, filesystems, find, rm | Score: 318 | Views: 291413 | Answers: 2

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
Tags: linux, hardware, devices, hard-disk | Score: 313 | Views: 1391057 | Answers: 16

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
Tags: linux, memory, top, meminfo | Score: 309 | Views: 477595 | Answers: 9

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
Tags: linux, storage | Score: 303 | Views: 1002557 | Answers: 13

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
Tags: linux, hard-disk, block-device, ssd | Score: 302 | Views: 448328 | Answers: 10

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
Tags: linux, command-line, files, rm | Score: 297 | Views: 507560 | Answers: 24

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
Tags: linux, cpu, arm, x86 | Score: 283 | Views: 215280 | Answers: 6

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
Tags: linux, kernel, inotify | Score: 282 | Views: 226435 | Answers: 2

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
Tags: linux, cpu, top | Score: 273 | Views: 460224 | Answers: 3

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
Tags: linux, filesystems, mount | Score: 264 | Views: 1131822 | Answers: 5

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
Tags: linux, memory, ulimit | Score: 263 | Views: 436682 | Answers: 12

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
Tags: linux, ps | Score: 260 | Views: 542981 | Answers: 4

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
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622620 | Answers: 21

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
Tags: linux, command-line, logs, dmesg | Score: 243 | Views: 336443 | Answers: 7

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
Tags: linux, command-line, memory, hardware | Score: 237 | Views: 284544 | Answers: 5

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
Tags: linux, files, diff | Score: 228 | Views: 325424 | Answers: 6

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
Tags: linux, permissions, su, conventions | Score: 221 | Views: 135871 | Answers: 4

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
Tags: linux, unix, history | Score: 213 | Views: 116072 | Answers: 9

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
Tags: linux, filesystems, io, async | Score: 209 | Views: 118843 | Answers: 8

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
Tags: linux, filesystems, ln | Score: 202 | Views: 505510 | Answers: 6

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
Tags: linux, desktop, freeze | Score: 202 | Views: 673972 | Answers: 10

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
Tags: linux, data-recovery, deleted-files | Score: 202 | Views: 1208038 | Answers: 14

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

---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
