# Linux 系统故障知识库 | Linux Troubleshooting

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 295**

> 技术细节（问题描述、解决方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, solutions) remain in original language for accuracy; structural text is bilingual.

---

#### 1. How do I make `ls` show file sizes in megabytes?

**问题描述 / Problem Description**:
Tags: linux, ls | Score: 936 | Views: 2451279 | Answers: 2

**解决方案 / Solution**:
ls -l --block-size=M will give you a long format listing (needed to actually see the file size) and round file sizes up to the nearest MiB.

If you want MB (10^6 bytes) rather than MiB (2^20 bytes) units, use --block-size=MB instead.

If you don't want the M suffix attached to the file size, you can use something like --block-size=1M. Thanks Stéphane Chazelas for suggesting this.

If you simply want file sizes in "reasonable" units, rather than specifically megabytes, then you can use -lh to get a long format listing and human readable file size presentation. This will use units of file size to keep file sizes presented with about 1-3 digits (so you'll see file sizes like 6.1K, 151K, 7.1M, 15M, 1.5G and so on.

The --block-size parameter is described in the man page for ls; man ls and search for SIZE. It allows for units other than MB/MiB as well, and from the looks of it (I didn't try that) arbitrary block sizes as well (so you could see the file size as a number of 429-byte blocks if you want to).

Note that both --block-size and -h are GNU extensions on top of the Open Group's ls, so this may not work if you don't have a GNU userland (which most Linux installations do). The ls from GNU Coreutils 8.5 does support --block-size and -h as described above. Thanks to kojiro for pointing this out.

---

#### 2. Finding the PID of the process using a specific port?

**问题描述 / Problem Description**:
Tags: linux, process, ip, netstat | Score: 831 | Views: 2194648 | Answers: 8

**解决方案 / Solution**:
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

---

#### 3. Why am I still getting a password prompt with ssh with public key authentication?

**问题描述 / Problem Description**:
Tags: ubuntu, centos, ssh, sshd, key-authentication | Score: 745 | Views: 1428792 | Answers: 32

**解决方案 / Solution**:
Make sure the permissions on the ~/.ssh directory and its contents are proper. When I first set up my ssh key auth, I didn't have the ~/.ssh folder properly set up, and it yelled at me.


Your home directory ~, your ~/.ssh directory and the ~/.ssh/authorized_keys file on the remote machine must be writable only by you: rwx------ and rwxr-xr-x are fine, but rwxrwx--- is no good¹, even if you are the only user in your group (if you prefer numeric modes: 700 or 755, not 775).
If ~/.ssh or authorized_keys is a symbolic link, the canonical path (with symbolic links expanded) is checked.
Your ~/.ssh/authorized_keys file (on the remote machine) must be readable (at least 400), but you'll need it to be also writable (600) if you will add any more keys to it.
Your private key file (on the local machine) must be readable and writable only by you: rw-------, i.e. 600.
Also, if SELinux is set to enforcing, you may need to run restorecon -R -v ~/.ssh (see e.g. Ubuntu bug 965663 and Debian bug report #658675; this is patched in CentOS 6).


¹  Except on some distributions (Debian and derivatives) which have patched the code to allow group writability if you are the only user in your group.

---

#### 4. How can I resolve a hostname to an IP address in a Bash script?

**问题描述 / Problem Description**:
Tags: linux, bash, networking, dns | Score: 635 | Views: 995011 | Answers: 29

**解决方案 / Solution**:
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

---

#### 5. Execute vs Read bit. How do directory permissions in Linux work?

**问题描述 / Problem Description**:
Tags: linux, permissions, directory | Score: 536 | Views: 403914 | Answers: 9

**解决方案 / Solution**:
When applying permissions to directories on Linux, the permission bits have different meanings than on regular files.


The read bit (r) allows the affected user to list the files within the directory
The write bit (w) allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes
The execute bit (x) allows the affected user to enter the directory, and access files and directories inside
The sticky bit (T, or t if the execute bit is set for others) states that files and directories within that directory may only be deleted or renamed by their owner (or root)

---

#### 6. How to know whether Wayland or X11 is being used

**问题描述 / Problem Description**:
Tags: linux, x11, wayland | Score: 514 | Views: 702754 | Answers: 15

**解决方案 / Solution**:
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

---

#### 7. Compress a folder with tar?

**问题描述 / Problem Description**:
Tags: linux, backup, tar | Score: 505 | Views: 1359503 | Answers: 2

**解决方案 / Solution**:
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

---

#### 8. When should I not kill -9 a process?

**问题描述 / Problem Description**:
Tags: linux, command-line, kill, process-management | Score: 436 | Views: 209582 | Answers: 9

**解决方案 / Solution**:
Generally, you should use kill (short for kill -s TERM, or on most systems kill -15) before kill -9 (kill -s KILL) to give the target process a chance to clean up after itself.  (Processes can't catch or ignore SIGKILL, but they can and often do catch SIGTERM.)  If you don't give the process a chance to finish what it's doing and clean up, it may leave corrupted files (or other state) around that it won't be able to understand once restarted.

strace/truss, ltrace and gdb are generally good ideas for looking at why a stuck process is stuck.   (truss -u on Solaris is particularly helpful; I find ltrace too often presents arguments to library calls in an unusable format.)  Solaris also has useful /proc-based tools, some of which have been ported to Linux.  (pstack is often helpful).

---

#### 9. How do you empty the buffers and cache on a Linux system?

**问题描述 / Problem Description**:
Tags: linux, kernel, performance, cache, ram | Score: 419 | Views: 985957 | Answers: 1

**解决方案 / Solution**:
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

---

#### 10. How to check OS and version using a Linux command

**问题描述 / Problem Description**:
Tags: linux, shell | Score: 400 | Views: 1968359 | Answers: 3

**解决方案 / Solution**:
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

---

#### 11. How to list all files ordered by size

**问题描述 / Problem Description**:
Tags: linux, files, ls | Score: 386 | Views: 734387 | Answers: 14

**解决方案 / Solution**:
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

---

#### 12. How to know number of cores of a system in Linux?

**问题描述 / Problem Description**:
Tags: linux, cpu | Score: 384 | Views: 815326 | Answers: 12

**解决方案 / Solution**:
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

---

#### 13. How to set default file permissions for all folders/files in a directory?

**问题描述 / Problem Description**:
Tags: linux, permissions, directory | Score: 379 | Views: 714955 | Answers: 5

**解决方案 / Solution**:
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

---

#### 14. How can I monitor disk io?

**问题描述 / Problem Description**:
Tags: linux, disk | Score: 378 | Views: 1059518 | Answers: 11

**解决方案 / Solution**:
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

---

#### 15. Change the Python3 default version in Ubuntu

**问题描述 / Problem Description**:
Tags: ubuntu, python, python3 | Score: 378 | Views: 1239818 | Answers: 10

**解决方案 / Solution**:
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

---

#### 16. How can I update to a newer version of Git using apt-get?

**问题描述 / Problem Description**:
Tags: ubuntu, apt, upgrade, git | Score: 360 | Views: 464951 | Answers: 5

**解决方案 / Solution**:
Here are the commands you need to run, if you just want to get it done:
sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com A1715D88E1DF1F24 40976EAF437D05B5 3B4FE6ACC0B21F32 A6616109451BBBF2
sudo apt-get update
sudo apt-get install git -y
git --version

As of Dec 2018, I got git 2.20.1 that way, while the version in the Ubuntu Xenial repositories was 2.7.4.
If your system doesn't have add-apt-repository, you can install it via:
sudo apt-get install python-software-properties software-properties-common

---

#### 17. How can I get my external IP address in a shell script?

**问题描述 / Problem Description**:
Tags: linux, shell-script, ip | Score: 355 | Views: 497757 | Answers: 27

**解决方案 / Solution**:
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

---

#### 18. how can I recursively delete empty directories in my home directory?

**问题描述 / Problem Description**:
Tags: linux, filesystems, find, rm | Score: 318 | Views: 291413 | Answers: 2

**解决方案 / Solution**:
The find command is the primary tool for recursive file system operations.
Use the -type d expression to tell find you're interested in finding directories only (and not plain files). The GNU version of find supports the -empty test, so

$ find . -type d -empty -print


will print all empty directories below your current directory.

Use find ~ -… or find "$HOME" -… to base the search on your home directory (if it isn't your current directory).

After you've verified that this is selecting the correct directories, use -delete to delete all matches:

$ find . -type d -empty -delete

---

#### 19. How do I find out what hard disks are in the system?

**问题描述 / Problem Description**:
Tags: linux, hardware, devices, hard-disk | Score: 313 | Views: 1391057 | Answers: 16

**解决方案 / Solution**:
This is highly platform-dependent. Also different methods may treat edge cases differently (“fake” disks of various kinds, RAID volumes, …).

On modern udev installations, there are symbolic links to storage media in subdirectories of /dev/disk, that let you look up a disk or a partition by serial number (/dev/disk/by-id/), by UUID (/dev/disk/by-uuid), by filesystem label (/dev/disk/by-label/) or by hardware connectivity (/dev/disk/by-path/).

Under Linux 2.6, each disk and disk-like device has an entry in /sys/block. Under Linux since the dawn of time, disks and partitions are listed in /proc/partitions. Alternatively, you can use lshw: lshw -class disk.

Linux also provides the lsblk utility which displays a nice tree view of the storage volumes (since util-linux 2.19, not present on embedded devices with BusyBox).

If you have an fdisk or disklabel utility, it might be able to tell you what devices it's able to work on.

You will find utility names for many unix variants on the Rosetta Stone for Unix, in particular the “list hardware configuration” and “read a disk label” lines.

---

#### 20. How to display meminfo in megabytes in top?

**问题描述 / Problem Description**:
Tags: linux, memory, top, meminfo | Score: 309 | Views: 477595 | Answers: 9

**解决方案 / Solution**:
When in top, typing capital "E" cycles through different memory units (KiB, MiB, GiB, etc., which are different from kB, MB and GB) in the total memory info:



While lower-case "e" does the same individual process lines:



From the manpage:

2c. MEMORY Usage
    This  portion  consists of two lines which may express values in kibibytes
    (KiB) through exbibytes (EiB) depending on  the  scaling  factor  enforced
    with the 'E' interactive command.


Version Information: top -version: procps-ng version 3.3.9
System: CentOS 7

---

#### 21. linux: How can I view all UUIDs for all available disks on my system?

**问题描述 / Problem Description**:
Tags: linux, storage | Score: 303 | Views: 1002557 | Answers: 13

**解决方案 / Solution**:
There's a tool called blkid (use it as root or with sudo), 

# blkid /dev/sda1
/dev/sda1: LABEL="/" UUID="ee7cf0a0-1922-401b-a1ae-6ec9261484c0" SEC_TYPE="ext2" TYPE="ext3"


you can check this link for more info

---

#### 22. How to know if a disk is an SSD or an HDD

**问题描述 / Problem Description**:
Tags: linux, hard-disk, block-device, ssd | Score: 302 | Views: 448328 | Answers: 10

**解决方案 / Solution**:
Linux automatically detects SSD, and since kernel version 2.6.29, you may verify sda with:
cat /sys/block/sda/queue/rotational

You should get 1 for hard disks and 0 for a SSD.
It will probably not work if your disk is a logical device emulated by hardware (like a RAID controller).
See this answer for more information about SSD partitioning, filesystem...

---

#### 23. Efficiently delete large directory containing thousands of files

**问题描述 / Problem Description**:
Tags: linux, command-line, files, rm | Score: 297 | Views: 507560 | Answers: 24

**解决方案 / Solution**:
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

---

#### 24. What do the flags in /proc/cpuinfo mean?

**问题描述 / Problem Description**:
Tags: linux, cpu, arm, x86 | Score: 283 | Views: 215280 | Answers: 6

**解决方案 / Solution**:
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

---

#### 25. Kernel inotify watch limit reached

**问题描述 / Problem Description**:
Tags: linux, kernel, inotify | Score: 282 | Views: 226435 | Answers: 2

**解决方案 / Solution**:
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

---

#### 26. Difference between cp -r and cp -a

**问题描述 / Problem Description**:
Tags: linux, cp, recursive | Score: 276 | Views: 593565 | Answers: 3

**解决方案 / Solution**:
Recursive means that cp copies the contents of directories, and if a directory has subdirectories they are copied (recursively) too. Without -R, the cp command skips directories. -r is identical with -R on Linux, it differs in some edge cases on some other unix variants.

By default, cp creates a new file which has the same content as the old file, and the same permissions but restricted by the umask; the copy is dated from the time of the copy, and belongs to the user doing the copy. With the -p option, the copy has the same modification time, the same access time, and the same permissions as the original. It also has the same owner and group as the original, if the user doing the copy has the permission to create such files.

The -a option means -R and -p, plus a few other preservation options. It attempts to make a copy that's as close to the original as possible: same directory tree, same file types, same contents, same metadata (times, permissions, extended attributes, etc.).

---

#### 27. Linux &quot;top&quot; command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?

**问题描述 / Problem Description**:
Tags: linux, cpu, top | Score: 273 | Views: 460224 | Answers: 3

**解决方案 / Solution**:
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

---

#### 28. How to get the complete and exact list of mounted filesystems in Linux?

**问题描述 / Problem Description**:
Tags: linux, filesystems, mount | Score: 264 | Views: 1131822 | Answers: 5

**解决方案 / Solution**:
The definitive list of mounted filesystems is in /proc/mounts.

If you have any form of containers on your system, /proc/mounts only lists the filesystems that are in your present container. For example, in a chroot, /proc/mounts lists only the filesystems whose mount point is within the chroot. (There are ways to escape the chroot, mind.)

There's also a list of mounted filesystems in /etc/mtab. This list is maintained by the mount and umount commands. That means that if you don't use these commands (which is pretty rare), your action (mount or unmount) won't be recorded. In practice, it's mostly in a chroot that you'll find /etc/mtab files that differ wildly from the state of the system. Also, mounts performed in the chroot will be reflected in the chroot's /etc/mtab but not in the main /etc/mtab. Actions performed while /etc/mtab is on a read-only filesystem are also not recorded there.

The reason why you'd sometimes want to consult /etc/mtab in preference to or in addition to /proc/mounts is that because it has access to the mount command line, it's sometimes able to present information in a way that's easier to understand; for example you see mount options as requested (whereas /proc/mounts lists the mount and kernel defaults as well), and bind mounts appear as such in /etc/mtab.

---

#### 29. Limit memory usage for a single Linux process

**问题描述 / Problem Description**:
Tags: linux, memory, ulimit | Score: 263 | Views: 436682 | Answers: 12

**解决方案 / Solution**:
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

---

#### 30. What does aux mean in `ps aux`?

**问题描述 / Problem Description**:
Tags: linux, ps | Score: 260 | Views: 542981 | Answers: 4

**解决方案 / Solution**:
a = show processes for all users
u = display the process's user/owner
x = also show processes not attached to a terminal

By the way, man ps is a good resource.

Historically, BSD and AT&amp;T developed incompatible versions of ps.  The options without a leading dash (as per the question) are the BSD style while those with a leading dash are AT&amp;T Unix style.  On top of this, Linux developed a version which supports both styles and then adds to it a third style with options that begin with double dashes.

All (or nearly all) non-embedded Linux distributions use a variant of the procps suite.  The above options are as defined in the procps ps man page.

In the comments, you say you are using Apple MacOS (OSX, I presume).  The OSX man page for ps is here and it shows support only for AT&amp;T style.

---

#### 31. mount: wrong fs type, bad option, bad superblock

**问题描述 / Problem Description**:
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622620 | Answers: 21

**解决方案 / Solution**:
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

---

#### 32. How can I get distribution name and version number in a simple shell script?

**问题描述 / Problem Description**:
Tags: linux, shell-script, distributions | Score: 257 | Views: 364821 | Answers: 21

**解决方案 / Solution**:
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

---

#### 33. How can I edit multiple files in Vim?

**问题描述 / Problem Description**:
Tags: linux, command-line, vim, files | Score: 253 | Views: 353754 | Answers: 11

**解决方案 / Solution**:
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

---

#### 34. How to determine Linux kernel architecture?

**问题描述 / Problem Description**:
Tags: linux, command-line, x86, cpu-architecture | Score: 247 | Views: 751761 | Answers: 14

**解决方案 / Solution**:
i386 and i686 are both 32-bit.
x86_64 is 64-bit  

example for 64 bit:  

behrooz@behrooz:~$ uname -a  
Linux behrooz 2.6.32-5-amd64 #1 SMP Mon Mar 7 21:35:22 UTC 2011 **x86_64** GNU/Linux


EDIT:
See is my linux ARM 32 or 64 bit? for ARM

---

#### 35. How can get a list of all scheduled cron jobs on my machine?

**问题描述 / Problem Description**:
Tags: linux, cron, scheduling | Score: 246 | Views: 603353 | Answers: 4

**解决方案 / Solution**:
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

---

#### 36. How to download portion of video with youtube-dl command?

**问题描述 / Problem Description**:
Tags: linux, youtube-dl | Score: 243 | Views: 300449 | Answers: 22

**解决方案 / Solution**:
I don't believe youtube-dl alone will do what you want. However you can combine it with a command line utility like ffmpeg.

First acquire the actual URL using youtube-dl:

youtube-dl -g "https://www.youtube.com/watch?v=V_f2QkBdbRI"


Copy the output of the command and paste it as part of the -i parameter of the next command:

ffmpeg -ss 00:00:15.00 -i "OUTPUT-OF-FIRST URL" -t 00:00:10.00 -c copy out.mp4


The -ss parameter in this position states to discard all input up until 15 seconds into the video. The -t option states to capture for 10 seconds. The rest of the command tells it to store as an mp4.

ffmpeg is a popular tool and should be in any of the popular OS repositories/package managers.

---

#### 37. How can I see dmesg output as it changes?

**问题描述 / Problem Description**:
Tags: linux, command-line, logs, dmesg | Score: 243 | Views: 336443 | Answers: 7

**解决方案 / Solution**:
Relatively recent dmesg versions provide a follow option (-w, --follow) which works analogously to tail -f.

Thus, just use following command:

$ dmesg -wH


(-H, --human enables user-friendly features like colors, relative time)

Those options are available for example in Fedora 19.

---

#### 38. How do I determine the number of RAM slots in use?

**问题描述 / Problem Description**:
Tags: linux, command-line, memory, hardware | Score: 237 | Views: 284544 | Answers: 5

**解决方案 / Solution**:
Since you don't mention, I'm assuming this is on Linux. Any of the following should show you (with root):
dmidecode -t memory


dmidecode -t 16


lshw -class memory

---

#### 39. How to copy-merge two directories?

**问题描述 / Problem Description**:
Tags: ubuntu, directory, file-copy | Score: 232 | Views: 318596 | Answers: 10

**解决方案 / Solution**:
This is a job for rsync. There's no benefit to doing this manually with a shell loop unless you want to move the file rather than copy them.

rsync -a /path/to/source/ /path/to/destination


In your case:

rsync -a /images2/ /images/


(Note trailing slash on images2, otherwise it would copy to /images/images2.)

If images with the same name exist in both directories, the command above will overwrite /images/SOMEPATH/SOMEFILE with /images2/SOMEPATH/SOMEFILE. If you want to replace only older files, add the option -u. If you want to always keep the version in /images, add the option --ignore-existing.

If you want to move the files from /images2, with rsync, you can pass the option --remove-source-files. Then rsync copies all the files in turn, and removes each file when it's done. This is a lot slower than moving if the source and destination directories are on the same filesystem.

---

#### 40. Understanding of diff output

**问题描述 / Problem Description**:
Tags: linux, files, diff | Score: 228 | Views: 325424 | Answers: 6

**解决方案 / Solution**:
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

---

#### 41. How to skip &quot;permission denied&quot; errors when running find in Linux?

**问题描述 / Problem Description**:
Tags: linux, permissions, files, find | Score: 226 | Views: 353310 | Answers: 1

**解决方案 / Solution**:
you can filter out messages to stderr. I prefer to redirect them to stdout like this.

 find / -name art  2&gt;&amp;1 | grep -v "Permission denied"




Explanation:

In short, all regular output goes to standard output (stdout). All error messages to standard error (stderr).

grep usually finds/prints the specified string, the -v inverts this, so it finds/prints every string that doesn't contain "Permission denied". All of your output from the find command, including error messages usually sent to stderr (file descriptor 2) go now to stdout(file descriptor 1) and then get filtered by the grep command.

This assumes you are using the bash/sh shell.

Under tcsh/csh you would use  

 find / -name art |&amp; grep ....

---

#### 42. Why do we use su - and not just su?

**问题描述 / Problem Description**:
Tags: linux, permissions, su, conventions | Score: 221 | Views: 135871 | Answers: 4

**解决方案 / Solution**:
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

---

#### 43. Is Linux a Unix?

**问题描述 / Problem Description**:
Tags: linux, unix, history | Score: 213 | Views: 116072 | Answers: 9

**解决方案 / Solution**:
That depends on what you mean by “Unix”, and by “Linux”.


UNIX is a registered trade mark of The Open Group. The trade mark has had an eventful history, and it's not completely clear that it's not genericized due to the widespread usage of “Unix” refering to Unix-like systems (see below). Currently the Open Group grants use of the trade mark to any system that passes a Single UNIX certification. See also Why is there a * When There is Mention of Unix Throughout the Internet?.
Unix is an operating system that was born in 1969 at Bell Labs. Various companies sold, and still sell, code derived from this original system, for example AIX, HP-UX, Solaris. See also Evolution of Operating systems from Unix.
There are many systems that are Unix-like, in that they offer similar interfaces to programmers, users and administrators. The oldest production system is the Berkeley Software Distribution, which gradually evolved from Unix-based (i.e. containing code derived from the original implementation) to Unix-like (i.e. having a similar interface). There are many BSD-based or BSD-derived operating systems: FreeBSD, NetBSD, OpenBSD, Mac OS X, etc. Other examples include OSF/1 (now discontinued, it was a commercial Unix-like non-Unix-based system), Minix (originally a toy Unix-like operating system used as a teaching tool, now a production embedded Unix-like system), and most famously Linux.





Strictly speaking, Linux is an operating system kernel that is designed like Unix's kernel.
Linux is most commonly used as a name of Unix-like operating systems that use Linux as their kernel. As many of the tools outside the kernel are part of the GNU project, such systems are often known as GNU/Linux. All major Linux distributions consist of GNU/Linux and other software.
There are Linux-based Unix-like systems that don't use many GNU tools, especially in the embedded world, but I don't think any of them does away with GNU development tools, in particular GCC.
There are operating systems that have Linux as their kernel but are not Unix-like. The most well-known is Android, which doesn't have a Unix-like user experience (though you can install a Unix-like command line) or administrator experience or (mostly) programmer experience (“native” Android programs use an API that is completely different from Unix).

---

#### 44. How do I add X days to date and get new date?

**问题描述 / Problem Description**:
Tags: linux, bash, shell-script, date | Score: 210 | Views: 475824 | Answers: 5

**解决方案 / Solution**:
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

---

#### 45. Can I watch the progress of a `sync` operation?

**问题描述 / Problem Description**:
Tags: linux, filesystems, io, async | Score: 209 | Views: 118843 | Answers: 8

**解决方案 / Solution**:
Looking at /proc/meminfo will show the Dirty number shrinking over time as all the data spools out; some of it may spill into Writeback as well.  That will be a summary against all devices, but in the cases where one device on the system is much slower than the rest you'll usually end up where everything in that queue is related to it.  You'll probably find the Dirty number large when you start and the sync finishes about the same time it approaches 0.  Try this to get an interactive display:

watch -d grep -e Dirty: -e Writeback: /proc/meminfo


With regular disks I can normally ignore Writeback, but I'm not sure if it's involved more often in the USB transfer path.  If it just bounces up and down without a clear trend to it, you can probably just look at the Dirty number.

---

#### 46. Too many levels of symbolic links

**问题描述 / Problem Description**:
Tags: linux, filesystems, ln | Score: 202 | Views: 505510 | Answers: 6

**解决方案 / Solution**:
As Dubu points out in a comment, the issue lies in your relative paths. I had a similar problem symlinking my nginx configuration from /usr/local/etc/nginx to /etc/nginx. If you create your symlink like this:
cd /usr/local/etc
ln -s nginx/ /etc/nginx

You will in fact make the link /etc/nginx -&gt; /etc/nginx, because the source path is relative to the link's path. The solution is as simple as using absolute paths:
ln -s /usr/local/etc/nginx /etc/nginx

If you want to use relative paths and have them behave the way you probably expect them to, you can use the $PWD variable to easily add in the path to the current working directory path, like so:
cd /usr/local/etc
ln -s &quot;$PWD/nginx/&quot; /etc/nginx

Make sure that the path is in double quotes, to make sure things like spaces in your current path are escaped. Note that you must use double quotes when doing this, as $PWD will not be substituted if you use single quotes.

---

#### 47. What to do when a Linux desktop freezes?

**问题描述 / Problem Description**:
Tags: linux, desktop, freeze | Score: 202 | Views: 673972 | Answers: 10

**解决方案 / Solution**:
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

---

#### 48. Recover deleted files on Linux

**问题描述 / Problem Description**:
Tags: linux, data-recovery, deleted-files | Score: 202 | Views: 1208038 | Answers: 14

**解决方案 / Solution**:
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

---

#### 49. Determine the size of a block device

**问题描述 / Problem Description**:
Tags: linux, size | Score: 196 | Views: 336781 | Answers: 21

**解决方案 / Solution**:
blockdev --getsize64 /dev/sda returns size in bytes.

blockdev --getsz /dev/sda returns size in 512-byte sectors.

Deprecated: blockdev --getsize /dev/sda returns size in sectors.

blockdev is part of util-linux.

---

#### 50. Why would someone choose FreeBSD over Linux?

**问题描述 / Problem Description**:
Tags: linux, freebsd, distribution-choice | Score: 194 | Views: 211667 | Answers: 9

**解决方案 / Solution**:
If you want to know what's different so you can use the system more efficiently, here is a commonly referenced introduction to BSD to people coming from a Linux background.

If you want more of the historical context for this decision, I'll just take a guess as to why they chose FreeBSD. Around the time of the first dot-com bubble, FreeBSD 4 was extremely popular with ISPs. This may or may not have been related to the addition of kqueue. The Wikipedia page describes the feelings for FreeBSD 4 thusly: "…widely regarded as one of the most stable and high performance operating systems of the whole Unix lineage." FreeBSD in particular has added other features over time which would appeal to hosting providers, such as jail and ZFS support.

Personally, I really like the BSD systems because they just feel like they fit together better than most Linux distros I've used. Also, the documentation provided directly in the various handbooks, etc. is outstanding. If you're going to be using FreeBSD, I highly recommend the FreeBSD Handbook.

---

#### 51. How can I find the hardware model in Linux?

**问题描述 / Problem Description**:
Tags: linux, hardware, system-information, smbios, dmidecode | Score: 191 | Views: 492416 | Answers: 10

**解决方案 / Solution**:
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

---

#### 52. Why is my ethernet interface called enp0s10 instead of eth0?

**问题描述 / Problem Description**:
Tags: linux, networking, udev, ethernet | Score: 189 | Views: 292794 | Answers: 5

**解决方案 / Solution**:
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

---

#### 53. Manually generate password for /etc/shadow

**问题描述 / Problem Description**:
Tags: linux, password, shadow | Score: 188 | Views: 450016 | Answers: 10

**解决方案 / Solution**:
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

---

#### 54. Linux: Difference between /dev/console, /dev/tty and /dev/tty0

**问题描述 / Problem Description**:
Tags: linux, tty, console | Score: 187 | Views: 204991 | Answers: 3

**解决方案 / Solution**:
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

---

#### 55. Timezone setting in Linux

**问题描述 / Problem Description**:
Tags: linux, date, time, timezone | Score: 184 | Views: 717820 | Answers: 3

**解决方案 / Solution**:
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

---

#### 56. Mount cifs Network Drive: write permissions and chown

**问题描述 / Problem Description**:
Tags: linux, permissions, mount, chown, cifs | Score: 184 | Views: 550029 | Answers: 3

**解决方案 / Solution**:
You are mounting the CIFS share as root (because you used sudo), so you cannot write as normal user. If your Linux Distribution and its kernel are recent enough that you could mount the network share as a normal user (but under a folder that the user own), you will have the proper credentials to write file (e.g. mount the shared folder somewhere under your home directory, like for instance $HOME/netshare/. Obviously, you would need to create the folder before mounting it).

An alternative is to specify the user and group ID that the mounted network share should used, this would allow that particular user and potentially group to write to the share. Add the following options to your mount: uid=&lt;user&gt;,gid=&lt;group&gt; and replace &lt;user&gt; and &lt;group&gt; respectively by your own user and default group, which you can find automatically with the id command.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g) //server-address/folder /mount/path/on/ubuntu


If the server is sending ownership information, you may need to add the forceuid and forcegid options.

sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g),forceuid,forcegid, //server-address/folder /mount/path/on/ubuntu

---

#### 57. Trying to SSH to local VM Ubuntu with Putty

**问题描述 / Problem Description**:
Tags: ubuntu, virtualbox, putty | Score: 183 | Views: 600105 | Answers: 6

**解决方案 / Solution**:
VirtualBox will create a private network (10.0.2.x) which will be connected to your host network using NAT. (Unless configured otherwise.)

This means that you cannot directly access any host of the private network from the host network. To do so, you need some port forwarding. In the network preferences of your VM you can, for example, configure VirtualBox to open port 22 on 127.0.1.1 (a loopback address of your host) and forward any traffic to port 22 of 10.0.2.1 (the internal address of your VM)

This way, you can point putty to Port 22 of 127.0.1.1 and VirtualBox will redirect this connection to your VM where its ssh daemon will answer it, allowing you to log in.

---

#### 58. Sorting down processes by memory usage

**问题描述 / Problem Description**:
Tags: linux, memory | Score: 182 | Views: 494008 | Answers: 9

**解决方案 / Solution**:
Use the following command:

ps aux --sort -rss


Check here for more Linux process memory usage

---

#### 59. How to sync two folders with command line tools?

**问题描述 / Problem Description**:
Tags: linux, files, file-copy, synchronization | Score: 182 | Views: 338370 | Answers: 9

**解决方案 / Solution**:
This puts folder A into folder B:
rsync -avu --delete &quot;/home/user/A&quot; &quot;/home/user/B&quot;

If you want the contents of folders A and B to be the same, put /home/user/A/ (with the slash) as the source. This takes not the folder A but all of its content and puts it into folder B. Like this:
rsync -avu --delete &quot;/home/user/A/&quot; &quot;/home/user/B&quot;


-a archive mode; equals -rlptgoD (no -H, -A, -X)
-v run verbosely
-u only copy files with a newer modification time (or size difference if the times are equal)
--delete delete the files in target folder that do not exist in the source

Manpage: https://download.samba.org/pub/rsync/rsync.html

---

#### 60. How to move all files and folders via mv command

**问题描述 / Problem Description**:
Tags: linux, command, rename | Score: 182 | Views: 876725 | Answers: 7

**解决方案 / Solution**:
Try with this:

mv /path/sourcefolder/* /path/destinationfolder/

---

#### 61. How to change ownership of symbolic links?

**问题描述 / Problem Description**:
Tags: linux, permissions, rhel, symlink, ln | Score: 179 | Views: 251905 | Answers: 3

**解决方案 / Solution**:
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

---

#### 62. How do I read from /proc/$pid/mem under Linux?

**问题描述 / Problem Description**:
Tags: linux, kernel, process, memory, proc | Score: 176 | Views: 190951 | Answers: 6

**解决方案 / Solution**:
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

---

#### 63. Zip everything in current directory

**问题描述 / Problem Description**:
Tags: ubuntu, packaging, compression, zip | Score: 176 | Views: 300258 | Answers: 2

**解决方案 / Solution**:
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

---

#### 64. Get the chmod numerical value for a file

**问题描述 / Problem Description**:
Tags: linux, freebsd, chmod | Score: 172 | Views: 269466 | Answers: 4

**解决方案 / Solution**:
You can get the value directly using a stat output format, e.g.
Linux:
stat --format '%a' &lt;file&gt;

BSD/OS X:
stat -f &quot;%OLp&quot; &lt;file&gt;

Busybox:
 stat -c '%a' &lt;file&gt;

---

#### 65. What are pseudo terminals (pty/tty)?

**问题描述 / Problem Description**:
Tags: linux, terminal, pty | Score: 172 | Views: 129984 | Answers: 3

**解决方案 / Solution**:
What is a pseudo terminal? (tty/pty)

A device that has the functions of a physical terminal without actually being one. Created by terminal emulators such as xterm. More detail is in the manpage pty(7).

Why do we need them? How they got introduced and what was the need for it?

Traditionally, UNIX has a concept of a controlling terminal for a group of processes, and many I/O functions are built with terminals in mind. Pseudoterminals handle, for example, some control characters like ^C.

Are they outdated? Do we not need them anymore? Is there anything that replaced them?

They are not outdated and are used in many programs, including ssh.

Any useful use-case?

ssh.

---

#### 66. How to make log-rotate change take effect

**问题描述 / Problem Description**:
Tags: linux, syslog, logrotate | Score: 169 | Views: 400685 | Answers: 4

**解决方案 / Solution**:
logrotate uses crontab to work. It's scheduled work, not a daemon, so no need to reload its configuration.
When the crontab executes logrotate, it will use your new config file automatically.
If you need to test your config you can also execute logrotate on your own  with the command:
logrotate /etc/logrotate.d/your-logrotate-config

If you want to have a debug output use argument  -d
logrotate -d /etc/logrotate.d/your-logrotate-config

You may need to be root or a specific user to run this command.
Or as mentioned in comments, identify the logrotate line in the output of the command crontab -l and execute the command line refer to slm's answer to have a precise cron.daily explanation

---

#### 67. How do I attach a terminal to a detached process?

**问题描述 / Problem Description**:
Tags: linux, shell, command-line, terminal, process | Score: 167 | Views: 300559 | Answers: 5

**解决方案 / Solution**:
Yes, it is. First, create a pipe:
mkfifo /tmp/fifo.
 Use gdb to attach to the process:
gdb -p PID

Then close stdin: call close (0); and open it again: call open ("/tmp/fifo", 0600)

Finally, write away (from a different terminal, as gdb will probably hang):

echo blah &gt; /tmp/fifo

---

#### 68. Can I configure my Linux system for more aggressive file system caching?

**问题描述 / Problem Description**:
Tags: linux, filesystems, performance, fstab, sysctl | Score: 167 | Views: 171822 | Answers: 7

**解决方案 / Solution**:
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

---

#### 69. What is this folder /run/user/1000?

**问题描述 / Problem Description**:
Tags: linux, fedora, filesystems, directory-structure | Score: 167 | Views: 195386 | Answers: 2

**解决方案 / Solution**:
/run/user/$uid is created by pam_systemd and used for storing files used by running processes for that user. These might be things such as your keyring daemon, pulseaudio, etc.

Prior to systemd, these applications typically stored their files in /tmp. They couldn't use a location in /home/$user as home directories are often mounted over network filesystems, and these files should not be shared among hosts. /tmp was the only location specified by the FHS which is local, and writable by all users.

However storing all these files in /tmp is problematic as /tmp is writable by everyone, and while you can change the ownership &amp; mode on the files being created, it's more difficult to work with.

So systemd came along and created /run/user/$uid. This directory is local to the system and only accessible by the target user. So applications looking to store their files locally no longer have to worry about access control.
It also keeps things nice and organized. When a user logs out, and no active sessions remain, pam_systemd will wipe the /run/user/$uid directory out. With various files scattered around /tmp, you couldn't do this.

---

#### 70. How is Mono magical?

**问题描述 / Problem Description**:
Tags: linux, executable, cross-compilation, mono | Score: 165 | Views: 11848 | Answers: 1

**解决方案 / Solution**:
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

---

#### 71. Difference between pts and tty

**问题描述 / Problem Description**:
Tags: linux, tty, terminology, who | Score: 164 | Views: 176362 | Answers: 3

**解决方案 / Solution**:
A tty is a native terminal device, the backend is either hardware or kernel-emulated.
A pty (pseudo terminal device) is a terminal device which is emulated by another program (example: xterm, screen, or ssh are such programs). A pts is the slave part of a pty.
(More info can be found in man pty.)
Short summary:
A pty is created by a process through posix_openpt() (which usually opens the special device /dev/ptmx), and is constituted by a pair of bidirectional character devices:

The master part, which is the file descriptor obtained by this process through this call, is used to emulate a terminal. After some initialization, the second part can be unlocked with unlockpt(), and the master is used to receive or send characters to this second part (slave).

The slave part, which is anchored in the filesystem as /dev/pts/x (the real name can be obtained by the master through ptsname()) behaves like a native terminal device (/dev/ttyx). In most cases, a shell is started that uses it as a controlling terminal.

---

#### 72. How to show the filesystem type via the terminal?

**问题描述 / Problem Description**:
Tags: linux, filesystems | Score: 163 | Views: 380005 | Answers: 2

**解决方案 / Solution**:
Yes, according to man df you can:


-T, --print-type      print file system type



Another way is to use the mount command. Without parameters it lists the currently mounted devices, including their file systems.

In case you need to find out only one certain file system, is easier to use the stat command's -f option instead of parsing out one value from the above mentioned commands' output.

---

#### 73. How do SO (shared object) numbers work?

**问题描述 / Problem Description**:
Tags: linux, dynamic-linking | Score: 163 | Views: 123963 | Answers: 4

**解决方案 / Solution**:
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

---

#### 74. How to output only file names (with spaces) in ls -Al?

**问题描述 / Problem Description**:
Tags: linux, command-line, ls | Score: 162 | Views: 448811 | Answers: 10

**解决方案 / Solution**:
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

---

#### 75. How to see process created by specific user in Unix/linux

**问题描述 / Problem Description**:
Tags: linux, process, ps | Score: 161 | Views: 478947 | Answers: 3

**解决方案 / Solution**:
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

---

#### 76. Long line wrapping in Nano

**问题描述 / Problem Description**:
Tags: ubuntu, nano | Score: 160 | Views: 189904 | Answers: 8

**解决方案 / Solution**:
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

---

#### 77. List partition labels from the command line

**问题描述 / Problem Description**:
Tags: linux, command-line, partition, disk | Score: 158 | Views: 326238 | Answers: 14

**解决方案 / Solution**:
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

---

#### 78. Why does /etc/resolv.conf point at 127.0.0.53?

**问题描述 / Problem Description**:
Tags: linux, dns, resolv.conf | Score: 158 | Views: 318752 | Answers: 3

**解决方案 / Solution**:
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

---

#### 79. How does the OOM killer decide which process to kill first?

**问题描述 / Problem Description**:
Tags: linux, memory, out-of-memory | Score: 157 | Views: 189916 | Answers: 1

**解决方案 / Solution**:
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

---

#### 80. Show top five CPU consuming processes with `ps`

**问题描述 / Problem Description**:
Tags: linux, ps | Score: 156 | Views: 520011 | Answers: 13

**解决方案 / Solution**:
Why use ps when you can do it easily with the top command?

If you must use ps, try this:

ps aux | sort -nrk 3,3 | head -n 5


If you want something that's truly 'top'esq with constant updates, use watch

watch "ps aux | sort -nrk 3,3 | head -n 5"

---

#### 81. How do I kill all screens?

**问题描述 / Problem Description**:
Tags: linux, bash, gnu-screen, kill | Score: 153 | Views: 467444 | Answers: 8

**解决方案 / Solution**:
You can use :

pkill screen


Or 

killall screen




In OSX the process is called SCREEN in all caps. So, use:

pkill SCREEN


Or

killall SCREEN

---

#### 82. How can I look up a username by id in linux?

**问题描述 / Problem Description**:
Tags: linux, ubuntu, users, uuid | Score: 146 | Views: 362675 | Answers: 8

**解决方案 / Solution**:
You might enjoy this little ditty. 

$ id -nu [number]


3.17.3-1-ARCH #1 SMP PREEMPT Fri Nov 14 22:56:01 CET 2014 i686 GNU/Linux

I can confirm that it returns a corresponding user name, if one exists, on Arch Linux. I can also confirm that it does not work on Ubuntu when run as a normal user, although I have not tested this as the superuser. It also does not work on Alpine Linux. Maybe a security feature prevents this from working on some systems.

---

#### 83. Difference between /bin and /usr/bin

**问题描述 / Problem Description**:
Tags: linux, directory, fhs | Score: 144 | Views: 160721 | Answers: 5

**解决方案 / Solution**:
What? no /bin/ is not a symlink to /usr/bin on any FHS compliant system. Note that there are still popular Unices and Linuxes that ignore this - for example, /bin and /sbin are symlinked to /usr/bin on Arch Linux (the reasoning being that you don't need /bin for rescue/single-user-mode, since you'd just boot a live CD).

/bin

contains commands that may be used by both the system administrator and by users, but which are required when no other filesystems are mounted (e.g. in single user mode). It may also contain commands which are used indirectly by scripts

/usr/bin/

This is the primary directory of executable commands on the system.

essentially, /bin contains executables which are required by the system for emergency repairs, booting, and single user mode. /usr/bin contains any binaries that aren't required.

I will note, that they can be on separate disks/partitions, /bin must be on the same disk as /. /usr/bin can be on another disk - although note that this configuration has been kind of broken for a while (this is why e.g. systemd warns about this configuration on boot).

For full correctness, some unices may ignore FHS, as I believe it is only a Linux Standard, I'm not aware that it has yet been included in SUS, Posix or any other UNIX standard, though it should be IMHO. It is a part of the LSB standard though.

---

#### 84. How do I know if a partition is ext2, ext3, or ext4?

**问题描述 / Problem Description**:
Tags: linux, ext4, ext3, ext2 | Score: 143 | Views: 229365 | Answers: 12

**解决方案 / Solution**:
How do I tell what sort of data (what data format) is in a file?
→ Use the file utility.

Here, you want to know the format of data in a device file, so you need to pass the -s flag to tell file not just to say that it's a device file but look at the content. Sometimes you'll need the -L flag as well, if the device file name is a symbolic link. You'll see output like this:

# file -sL /dev/sd*
/dev/sda1: Linux rev 1.0 ext4 filesystem data, UUID=63fa0104-4aab-4dc8-a50d-e2c1bf0fb188 (extents) (large files) (huge files)
/dev/sdb1: Linux rev 1.0 ext2 filesystem data, UUID=b3c82023-78e1-4ad4-b6e0-62355b272166
/dev/sdb2: Linux/i386 swap file (new style), version 1 (4K pages), size 4194303 pages, no label, UUID=3f64308c-19db-4da5-a9a0-db4d7defb80f


Given this sample output, the first disk has one partition and the second disk has two partitions. /dev/sda1 is an ext4 filesystem, /dev/sdb1 is an ext2 filesystem, and /dev/sdb2 is some swap space (about 4GB).

You must run this command as root, because ordinary users may not read disk partitions directly: if needed, add sudo in front.

---

#### 85. How can I tell what version of Linux I&#39;m using?

**问题描述 / Problem Description**:
Tags: linux, ssh, version, info, system-information | Score: 142 | Views: 175458 | Answers: 13

**解决方案 / Solution**:
If I need to know what it is say Linux/Unix , 32/64 bit

uname -a 


This would give me almost all information that I need, 

If I further need to know what release it is say (Centos 5.4, or 5.5 or 5.6)
on a Linux box I would further check the file /etc/issue to see its release info ( or for Debian / Ubuntu /etc/lsb-release )

Alternative way is to use the lsb_release utility:

lsb_release -a


Or do a rpm -qa | grep centos-release or redhat-release for RHEL derived systems

---

#### 86. What is the difference between reboot , init 6 and shutdown -r now?

**问题描述 / Problem Description**:
Tags: linux, shutdown, init, reboot | Score: 142 | Views: 415220 | Answers: 4

**解决方案 / Solution**:
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

---

#### 87. Linux ls to show only file name, date, and size

**问题描述 / Problem Description**:
Tags: linux, command-line, files, ls | Score: 141 | Views: 248431 | Answers: 15

**解决方案 / Solution**:
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

---

#### 88. File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)

**问题描述 / Problem Description**:
Tags: ubuntu, permissions, virtualbox, virtual-machine | Score: 141 | Views: 333935 | Answers: 10

**解决方案 / Solution**:
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

---

#### 89. Set the default kernel in GRUB

**问题描述 / Problem Description**:
Tags: linux, kernel, boot, grub | Score: 140 | Views: 428583 | Answers: 11

**解决方案 / Solution**:
After struggling for 2 hours, I have found a much easier way to achieve this. I just RTFM. ;)
Add two lines to /etc/default/grub
GRUB_SAVEDEFAULT=true
GRUB_DEFAULT=saved

Do the sudo update-grub, reboot, get into your grub menu and select whichever menu or submenu item you need. The choice will be saved every time and then your computer will boot into it automatically. When you manually choose a different entry, that becomes the new default.

---

#### 90. How do I find how long ago a Linux system was installed?

**问题描述 / Problem Description**:
Tags: linux, system-installation | Score: 139 | Views: 151247 | Answers: 18

**解决方案 / Solution**:
sudo tune2fs -l /dev/sda1 **OR** /dev/sdb1*  | grep 'Filesystem created:'

This will tell you when the file system was created.
* = In the first column of df / you can find the exact partition to use.

---

#### 91. timestamp, modification time, and created time of a file

**问题描述 / Problem Description**:
Tags: linux, filesystems, files | Score: 138 | Views: 352604 | Answers: 2

**解决方案 / Solution**:
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

---

#### 92. Easy way to determine the virtualization technology of a Linux machine?

**问题描述 / Problem Description**:
Tags: linux, command-line, virtual-machine | Score: 137 | Views: 130239 | Answers: 17

**解决方案 / Solution**:
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

---

#### 93. What&#39;s the best way to join files again after splitting them?

**问题描述 / Problem Description**:
Tags: linux, command-line, files, iso, split | Score: 135 | Views: 214610 | Answers: 6

**解决方案 / Solution**:
That's just what cat was made for. Since it is one of the oldest GNU tools, I think it's very unlikely that any other tool does that faster/better. And it's not piping - it's only redirecting output.

---

#### 94. Linux: set date through command line

**问题描述 / Problem Description**:
Tags: linux, date, clock | Score: 134 | Views: 757612 | Answers: 7

**解决方案 / Solution**:
Use date -s:

date -s '2014-12-25 12:34:56'


Run that as root or under sudo. Changing only one of the year/month/day is more of a challenge and will involve repeating bits of the current date. There are also GUI date tools built in to the major desktop environments, usually accessed through the clock.

To change only part of the time, you can use command substitution in the date string:

date -s "2014-12-25 $(date +%H:%M:%S)"


will change the date, but keep the time. See man date for formatting details to construct other combinations: the individual components are %Y, %m, %d, %H, %M, and %S.

---

#### 95. How can I find available network interfaces?

**问题描述 / Problem Description**:
Tags: linux, networking, devices, systemd, udev | Score: 134 | Views: 512358 | Answers: 6

**解决方案 / Solution**:
The simplest method I know to list all of your interfaces is

ifconfig -a


EDIT

If you're on a system where that has been made obsolete, you can use

ip link show

---

#### 96. Setting /proc/sys/vm/drop_caches to clear cache

**问题描述 / Problem Description**:
Tags: linux, virtual-memory | Score: 134 | Views: 307376 | Answers: 2

**解决方案 / Solution**:
It isn't sticky - you just write to the file to make it drop the caches and then it immediately starts caching again.

Basically when you write to that file you aren't really changing a setting, you are issuing a command to the kernel. The kernel acts on that command (by dropping the caches) then carries on as before.

---

#### 97. What is a tainted Linux kernel?

**问题描述 / Problem Description**:
Tags: linux, linux-kernel, kernel-modules, troubleshooting, proprietary-drivers | Score: 134 | Views: 207611 | Answers: 2

**解决方案 / Solution**:
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

---

#### 98. ssh-add returns with: &quot;Error connecting to agent: No such file or directory&quot;

**问题描述 / Problem Description**:
Tags: linux, ssh, ssh-agent | Score: 133 | Views: 264530 | Answers: 5

**解决方案 / Solution**:
The client tool ssh-add wants to communicate with the background process ssh-agent. You need to start the ssh-agent process first. On Linux, a shell uses the environment variables SSH_AUTH_SOCK and SSH_AGENT_PID to identify the correct process to talk to.
You can start ssh-agent in multiple ways.
Either by starting a new shell
ssh-agent bash

or by evaluating the script returned by ssh-agent in your current shell.
eval &quot;$(ssh-agent)&quot;

I suggest using the second method, because you keep all your history and variables.

---

#### 99. How to check which GPU is active in Linux?

**问题描述 / Problem Description**:
Tags: linux, hardware, graphics | Score: 133 | Views: 454435 | Answers: 12

**解决方案 / Solution**:
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

---

#### 100. What&#39;s the difference between /usr/lib/systemd/system and /etc/systemd/system?

**问题描述 / Problem Description**:
Tags: debian, ubuntu, centos, systemd | Score: 133 | Views: 116937 | Answers: 3

**解决方案 / Solution**:
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

---

#### 101. Systemd service - what is `multi-user.target`

**问题描述 / Problem Description**:
Tags: ubuntu, systemd, services | Score: 133 | Views: 162825 | Answers: 5

**解决方案 / Solution**:
multi-user.target means that the systemd-service will start when the system reach runlevel 2.

To complement the answer, here's a table of the targets and their run levels:

Run Lvl Target Units                        Description
0       runlevel0.target, poweroff.target   Shut down and power off
1       runlevel1.target, rescue.target     Set up a rescue shell
2,3,4   runlevel[234].target,               Set up a non-gfx multi-user shell
        multi-user.target
5       runlevel5.target, graphical.target  Set up a gfx multi-user shell
6       runlevel6.target, reboot.target     Shut down and reboot the system

---

#### 102. How do I identify which Linux distro is running?

**问题描述 / Problem Description**:
Tags: linux, version | Score: 132 | Views: 245068 | Answers: 3

**解决方案 / Solution**:
A question very close to this one was posted on Unix.Stackexchange HERE
Giles has a pretty complete | cool answer for the ways he describes.

# cat /proc/version

Linux version 2.6.32-71.el6.x86_64 (mockbuild@c6b6.centos.org) (gcc version 4.4.4 20100726 (Red Hat 4.4.4-13) (GCC) ) #1 SMP Fri May 20 03:51:51 BST 2011  


# uname -a

Linux system1.doofus.local 2.6.32-71.el6.x86_64 #1 SMP Fri May 20 03:51:51 BST 2011 x86_64 x86_64 x86_64 GNU/Linux

# cat /etc/issue

CentOS Linux release 6.0 (Final)
Kernel \r on an \m


cat /proc/config.gz cat /usr/src/linux/config.gz cat /boot/config*

Though I did some checking and this was not very reliable except on SUSE.

# zcat /proc/config.gz | grep -i kernel
CONFIG_SUSE_KERNEL=y
# CONFIG_KERNEL_DESKTOP is not set
CONFIG_LOCK_KERNEL=y

Release Files in /etc (from Unix.com)


Novell SuSE---> /etc/SuSE-release    
Red Hat--->/etc/redhat-release, /etc/redhat_version  
Fedora-->/etc/fedora-release    
Slackware--->/etc/slackware-release, /etc/slackware-version    
Old Debian--->/etc/debian_release, /etc/debian_version 
New Debian--->/etc/os-release
Mandrake--->/etc/mandrake-release  
Yellow dog-->/etc/yellowdog-release     
Sun JDS--->/etc/sun-release  
Solaris/Sparc--->/etc/release      
Gentoo--->/etc/gentoo-release


There is also a bash script at the Unix.com link someone wrote to automate checking.

Figuring out what package manager you have is a good clue.

rpm yum apt-get zypper +many more

Though this is by no means foolproof as the vendor could use anything they want. It really just gives you a place to start.

# dmesg | less

Linux version 2.6.32.12-0.7-default (geeko@buildhost) (gcc version 4.3.4 [gcc-4_3-branch revision 152973] (SUSE Linux) ) #1 SMP 2010-05-20 11:14:20 +0200

pretty much the same information as cat /proc/version &amp; uname

---

#### 103. How are &quot;/dev&quot; Linux files created?

**问题描述 / Problem Description**:
Tags: linux, files, devices | Score: 129 | Views: 69630 | Answers: 7

**解决方案 / Solution**:
/dev/zero is an example of a "special file" &mdash; particularly, a "device node". Normally these get created by the distro installation process, but you can totally create them yourself if you want to.

If you ask ls about /dev/zero:

# ls -l /dev/zero
crw-rw-rw- 1 root root 1, 5  Nov 5 09:34 /dev/zero


The "c" at the start tells you that this is a "character device"; the other type is "block device" (printed by ls as "b"). Very roughly, random-access devices like harddisks tend to be block devices, while sequential things like tape drives or your sound card tend to be character devices.

The "1, 5" part is the "major device number" and the "minor device number".

With this information, we can use the mknod command to make our very own device node:

# mknod foobar c 1 5


This creates a new file named foobar, in the current folder, which does exactly the same thing as /dev/zero. (You can of course set different permissions on it if you want.) All this "file" really contains is the three items above &mdash; device type, major number, minor number. You can use ls to look up the codes for other devices and recreate those too. When you get bored, just use rm to remove the device nodes you just created.

Basically the major number tells the Linux kernel which device driver to talk to, and the minor number tells the device driver which device you're talking about. (E.g., you probably have one SATA controller, but maybe multiple harddisks plugged into it.)

If you want to invent new devices that do something new... well, you'll need to edit the source code for the Linux kernel and compile your own custom kernel. So let's not do that! :-) But you can add device files that duplicate the ones you've already got just fine. An automated system like udev is basically just watching for device events and calling mknod / rm for you automatically. Nothing more magic than that.

There are still other kinds of special files:


Linux considers a directory to be a special kind of file. (Usually you can't directly open a directory, but if you could, you'd find it's a normal file that contains data in a special format, and tells the kernel where to find all the files in that directory.)
A symlink is a special file. (But a hard link isn't.) You can create symlinks using the ln -s command. (Look up the manpage for it.)
There's also a thing called a "named pipe" or "FIFO" (first-in, first-out queue). You can create one with mkfifo. A FIFO is a magical file that can be opened by two programs at once &mdash; one reading, one writing. When this happens, it works like a normal shell pipe. But you can start each program separately...


A file that isn't "special" in any way is called a "regular file". You will occasionally see mention of this in Unix documentation. That's what it means; a file that isn't a device node or a symlink or whatever. Just a normal, every day file with no magical properties.

---

#### 104. Unable to locate package `docker-ce` on a 64bit ubuntu

**问题描述 / Problem Description**:
Tags: ubuntu, apt, software-installation, docker | Score: 129 | Views: 229593 | Answers: 5

**解决方案 / Solution**:
Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

Ubuntu 24.04 (Noble Numbat)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu noble stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 23.10 (Mantic Minotaur)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu mantic stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 23.04 (Lunar Lobster)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu lunar stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 22.10 (Kinetic)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu kinetic stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 22.04 (Jammy)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 21.10 (Impish)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu impish stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 21.04 (hirsute)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu hirsute stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 20.10 (Groovy)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu groovy stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 20.04 (Focal)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu focal stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 19.10 (Eoan)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu eoan stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 19.04 (Disco)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu disco stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 18.10 (Cosmic)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu cosmic stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 18.04 (bionic)
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu bionic stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 17.10
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu artful stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Ubuntu 16.04
echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu xenial stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null

Run the following:
sudo apt update
apt-cache search docker-ce

sample output:
docker-ce - Docker: the open-source application container engine

Install docker-ce:
sudo apt install docker-ce

To check the available and permitted Ubuntu codenames:
curl -sSL  https://download.docker.com/linux/ubuntu/dists/ |awk -F'&quot;' 'FNR &gt;7 {print $2}'

sample output (Results may be different after the directory updates):
../
artful/
bionic/
cosmic/
disco/
eoan/
focal/
groovy/
hirsute/
impish/
jammy/
kinetic/
lunar/
trusty/
xenial/
yakkety/
zesty/

Docker , OS requirements

---

#### 105. Why is video tearing such a problem in Linux?

**问题描述 / Problem Description**:
Tags: linux, graphics, monitors, composite | Score: 127 | Views: 101435 | Answers: 8

**解决方案 / Solution**:
This is all due to the fact that the X server is out-dated, ill-suitable for today's graphics hardware and basically all the direct video card communication is done as an extension ("patch") over the ancient bloated core. The X server provides no builtin means of synchronization between user rendering the window and the screen displaying a window, so the content changes in the middle of rendering. This is one of the well-known issues of the X server (it has many, the entire model of what the server does and is outdated - event handling in subwindows, metadata about windows, graphical primitives for direct drawing...). Widget toolkits mostly want to gloss over all this, but tearing is still a problem because there is no mechanism to handle that. Additional problems arise when you have multiple cards that require different drivers, and on top of all this, opengl library has a hard-wired dependency on xlib, so you can't really use it independently without going through X.

Wayland, which is somewhat unenthusiastically trying to replace X, supports a pedantic vsync synchronization in its core, and is advertised to have every frame exactly perfect.

If you quickly google "wayland video tearing" you'll find more information on everything.

---

#### 106. Uploading directories with sftp?

**问题描述 / Problem Description**:
Tags: linux, ssh, sftp | Score: 126 | Views: 309988 | Answers: 11

**解决方案 / Solution**:
I don't know why sftp does this but you can only recursive copy if the destination directory already exists. So do this...

sftp&gt; mkdir bin
sftp&gt; put -r bin

---

#### 107. SSH login with clear text password as a parameter?

**问题描述 / Problem Description**:
Tags: linux, ubuntu, ssh, security, login | Score: 125 | Views: 663177 | Answers: 3

**解决方案 / Solution**:
On Ubuntu, install the sshpass package, then use it like this: 

sshpass -p 'YourPassword' ssh user@host


sshpass also supports passing the keyboard-interactive password from a file or an environment variable, which might be a more appropriate option in any situation where security is relevant. See man sshpass for the details.

---

#### 108. Why is swappiness set to 60 by default?

**问题描述 / Problem Description**:
Tags: linux, kernel, swap | Score: 124 | Views: 73648 | Answers: 3

**解决方案 / Solution**:
Since kernel 2.6.28, Linux uses a Split Least Recently Used (LRU) page replacement strategy. Pages with a filesystem source, such as program text or shared libraries belong to the file cache. Pages without filesystem backing are called anonymous pages, and consist of runtime data such as the stack space reserved for applications etc. Typically pages belonging to the file cache are cheaper to evict from memory (as these can simple be read back from disk when needed). Since anonymous pages have no filesystem backing, they must remain in memory as long as they are needed by a program unless there is swap space to store them to. 

It is a common misconception that a swap partition would somehow slow down your system. Not having a swap partition does not mean that the kernel won't evict pages from memory, it just means that the kernel has fewer choices in regards to which pages to evict. The amount of swap available will not affect how much it is used.

Linux can cope with the absence of a swap space because, by default, the kernel memory accounting policy may overcommit memory. The downside is that when physical memory is exhausted, and the kernel cannot swap anonymous pages to disk, the out-of-memory-killer (OOM-killer) mechanism will start killing off memory-hogging "rogue" processes to free up memory for other processes.

The vm.swappiness option is a modifier that changes the balance between swapping out file cache pages in favour of anonymous pages. The file cache is given an arbitrary priority value of 200 from which vm.swappiness modifier is deducted (file_prio=200-vm.swappiness). Anonymous pages, by default, start out with 60 (anon_prio=vm.swappiness). This means that, by default, the priority weights stand moderately in favour of anonymous pages (anon_prio=60, file_prio=200-60=140). The behaviour is defined in mm/vmscan.c in the kernel source tree.

Given a vm.swappiness of 100, the priorities would be equal (file_prio=200-100=100, anon_prio=100). This would make sense for an I/O heavy system if it is not wanted that pages from the file cache being evicted in favour of anonymous pages.

Conversely setting the vm.swappiness to 0 will prevent the kernel from evicting anonymous pages in favour of pages from the file cache. This might be useful if programs do most of their caching themselves, which might be the case with some databases. In desktop systems this might improve interactivity, but the downside is that I/O performance will likely take a hit.

The default value has most likely been chosen as an approximate middleground between these two extremes. As with any performance parameter, adjusting vm.swappiness should be based on  benchmark data comparable to real workloads, not just a gut feeling.

---

#### 109. Show the year while listing files in the current directory

**问题描述 / Problem Description**:
Tags: linux, shell-script, date | Score: 123 | Views: 215366 | Answers: 7

**解决方案 / Solution**:
You can use man ls and here you can find the --time-style parameter. Or you can use:



Command
Sample Output




ls --full-time
2024-04-09 13:24:44.108466043 -0500


ls -l --time-style=long-iso
2024-04-09 08:58

---

#### 110. Creating a user without a password

**问题描述 / Problem Description**:
Tags: ubuntu, users, git, non-root-user | Score: 122 | Views: 450156 | Answers: 8

**解决方案 / Solution**:
The --disabled-password option will not set a password, meaning no password is legal, but  login  is still possible (for example with SSH RSA keys).

To create an user without a password, use passwd -d $username after the user is created to make the password empty. Note not all systems allow users with empty password to log in.

---

#### 111. Block network access of a process?

**问题描述 / Problem Description**:
Tags: linux, networking, process, iptables | Score: 121 | Views: 87708 | Answers: 11

**解决方案 / Solution**:
With Linux 2.6.24+ (considered experimental until 2.6.29), you can use network namespaces for that. You need to have the 'network namespaces' enabled in your kernel (CONFIG_NET_NS=y) and util-linux with the unshare tool.

Then, starting a process without network access is as simple as:

unshare -n program ...


This creates an empty network namespace for the process. That is, it is run with no network interfaces, including no loopback. In below example we add -r to run the program only after the current effective user and group IDs have been mapped to  the  superuser ones (avoid sudo):

$ unshare -r -n ping 127.0.0.1
connect: Network is unreachable


If your app needs a network interface you can set a new one up:

$ unshare -n -- sh -c 'ip link set dev lo up; ping 127.0.0.1'
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=32 time=0.066 ms


Note that this will create a new, local loopback. That is, the spawned process won't be able to access open ports of the host's 127.0.0.1.



If you need to gain access to the original networking inside the namespace, you can use nsenter to enter the other namespace.

The following example runs ping with network namespace that is used by PID 1 (it is specified through -t 1):

$ nsenter -n -t 1 -- ping -c4 example.com
PING example.com (93.184.216.119) 56(84) bytes of data.
64 bytes from 93.184.216.119: icmp_seq=1 ttl=50 time=134 ms
64 bytes from 93.184.216.119: icmp_seq=2 ttl=50 time=134 ms
64 bytes from 93.184.216.119: icmp_seq=3 ttl=50 time=134 ms
64 bytes from 93.184.216.119: icmp_seq=4 ttl=50 time=139 ms

--- example.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 134.621/136.028/139.848/2.252 ms

---

#### 112. How do I kill all a user&#39;s processes using their UID

**问题描述 / Problem Description**:
Tags: c, linux, proc | Score: 121 | Views: 499467 | Answers: 6

**解决方案 / Solution**:
Use pkill -U UID or pkill -u UID or username instead of UID. Sometimes skill -u USERNAME may work, another tool is killall -u USERNAME.

Skill was a linux-specific and is now outdated, and pkill is more portable (Linux, Solaris, BSD).

pkill allow both numberic and symbolic UIDs, effective and real http://man7.org/linux/man-pages/man1/pkill.1.html


  pkill  -  ... signal processes based on name and other attributes

    -u, --euid euid,...
         Only match processes whose effective user ID is listed.
         Either the numerical or symbolical value may be used.
    -U, --uid uid,...
         Only match processes whose real user ID is listed.  Either the
         numerical or symbolical value may be used.



Man page of skill says is it allowed only to use username, not user id: http://man7.org/linux/man-pages/man1/skill.1.html


  skill, snice ...  These tools are obsolete and unportable.  The command syntax is poorly defined.  Consider using the killall, pkill

  -u, --user user
         The next expression is a username.



killall is not marked as outdated in Linux, but it also will not work with numberic UID; only username: http://man7.org/linux/man-pages/man1/killall.1.html


  killall - kill processes by name

   -u, --user
         Kill only processes the specified user owns.  Command names
         are optional.



I think, any utility used to find process in Linux/Solaris style /proc (procfs) will use full list of processes (doing some readdir of /proc). I think, they will iterate over /proc digital subfolders and check every found process for match.

To get list of users, use getpwent (it will get one user per call).

skill (procps &amp; procps-ng) and killall (psmisc) tools both uses getpwnam library call to parse argument of -u option, and only username will be parsed. pkill (procps &amp; procps-ng) uses both atol and getpwnam to parse -u/-U argument and allow both numeric and textual user specifier.

---

#### 113. What are high memory and low memory on Linux?

**问题描述 / Problem Description**:
Tags: linux, kernel, memory | Score: 121 | Views: 126866 | Answers: 7

**解决方案 / Solution**:
On a 32-bit architecture, the address space range for addressing RAM is: 

0x00000000 - 0xffffffff


or 4'294'967'295 (4 GB).

The linux kernel splits that up 3/1 (could also be 2/2, or 1/3 1) into user space (high memory) and kernel space (low memory) respectively.

The user space range: 

0x00000000 - 0xbfffffff


Every newly spawned user process gets an address (range) inside this area. User processes are generally untrusted and therefore are forbidden to access the kernel space. Further, they are considered non-urgent, as a general rule, the kernel tries to defer the allocation of memory to those processes.

The kernel space range: 

0xc0000000 - 0xffffffff


A kernel processes gets its address (range) here. The kernel can directly access this 1 GB of addresses (well, not the full 1 GB, there are 128 MB reserved for high memory access).

Processes spawned in kernel space are trusted, urgent and assumed error-free, the memory request gets processed instantaneously.

Every kernel process can also access the user space range if it wishes to. And to achieve this, the kernel maps an address from the user space (the high memory) to its kernel space (the low memory), the 128 MB mentioned above are especially reserved for this.



1 Whether the split is 3/1, 2/2, or 1/3 is controlled by the CONFIG_VMSPLIT_... option; you can probably check under /boot/config* to see which option was selected for your kernel.

---

#### 114. ssh_exchange_identification: Connection closed by remote host (not using hosts.deny)

**问题描述 / Problem Description**:
Tags: linux, ssh, key-authentication | Score: 121 | Views: 683618 | Answers: 13

**解决方案 / Solution**:
Originally posted on Ask Ubuntu

If you have ruled out any "external" factors, the following set of steps usually helps to narrow it down. So while this doesn't directly answer your question, it may help tracking down the error cause.

Troubleshooting sshd

What I find generally very useful in any such cases is to start sshd without letting it daemonize. The problem in my case was that neither syslog nor auth.log showed anything meaningful.

When I started it from the terminal I got:

# $(which sshd) -Ddp 10222
/etc/ssh/sshd_config line 8: address family must be specified before ListenAddress.


Much better! This error message allowed me to see what's wrong and fix it. Neither of the log files contained this output.

NB: at least on Ubuntu the $(which sshd) is the best method to satisfy sshd requirement of an absolute path. Otherwise you'll get the following error: sshd re-exec requires execution with an absolute path. The -p 10222 makes sshd listen on that alternative port, overriding the configuration file - this is so that it doesn't clash with potentially running sshd instances. Make sure to choose a free port here.

Finally: connect to the alternative port (ssh -p 10222 user@server).

This method has helped me many many times in finding issues, be it authentication issues or other types. To get really verbose output to stdout, use $(which sshd) -Ddddp 10222 (note the added dd to increase verbosity). For more debugging goodness check man sshd.



The main advantage of this method is that it allows you to check the sshd configuration without having to restart the sshd on the default port. Normally this should not interfere with existing SSH-connections, but I've seen it. So this allows one to validate the configuration file prior to - potentially - cutting off ones access to a remote server (for example I have that for some VPS and even for physical servers where I need to pay extra to get out-of-band access to the machine).

---

#### 115. What is difference between User space and Kernel space?

**问题描述 / Problem Description**:
Tags: linux, kernel, drivers | Score: 120 | Views: 190364 | Answers: 3

**解决方案 / Solution**:
Is Kernel space used when Kernel is executing on the behalf of the user program i.e. System Call? Or is it the address space for all the Kernel threads (for example scheduler)?

Yes and yes.
Before we go any further, we should state this about memory.
Memory gets divided into two distinct areas:

The user space, which is a set of locations where normal user processes run (i.e everything other than the kernel). The role of the kernel is to manage applications running in this space from messing with each other, and the machine.
The kernel space, which is the location where the code and data of the kernel is stored, and executes under.

Processes running under the user space have access only to a limited part of memory, whereas the kernel has access to all of the memory. Processes running in user space also don't have access to the kernel space. User space processes can only access a small part of the kernel via an interface exposed by the kernel - the system calls. If a process performs a system call, a software interrupt is sent to the kernel, which then dispatches the appropriate interrupt handler and continues its work after the handler has finished.
Kernel space code has the property to run in &quot;kernel mode&quot;, which (in your typical desktop -x86- computer) is what you call code that executes under ring 0. Typically in x86 architecture, there are 4 rings of protection. Ring 0 (kernel mode), Ring 1 (may be used by virtual machine hypervisors or drivers), Ring 2 (may be used by drivers, I am not so sure about that though). Ring 3 is what typical applications run under. It is the least privileged ring, and applications running on it have access to a subset of the processor's instructions. Ring 0 (kernel space) is the most privileged ring, and has access to all of the machine's instructions. For an example of this, a &quot;plain&quot; application (like a browser) can not use x86 assembly instructions lgdt to load the global descriptor table, nor hlt to halt a processor.

If it is the first one, than does it mean that normal user program cannot have more than 3GB of memory (if the division is 3GB + 1GB)? Also, in that case how can kernel use High Memory, because to what virtual memory address will the pages from high memory be mapped to, as 1GB of kernel space will be logically mapped?

For an answer to this, please refer to the excellent answer by wag to What are high memory and low memory on Linux?.

---

#### 116. What is &quot;mail&quot;, and how is it navigated?

**问题描述 / Problem Description**:
Tags: linux, mail-command | Score: 120 | Views: 182106 | Answers: 3

**解决方案 / Solution**:
This page describes the interactive command in detail, and is in fact a fairly thorough tutorial. Describes commands such as z and z- :

If there is more than a screenful of messages, then z will
show the next screenful, and z- will show the previous screenful.

---

#### 117. If Linux is only a kernel, then how were its first versions used (without distribution)?

**问题描述 / Problem Description**:
Tags: linux, kernel, linux-kernel, history | Score: 118 | Views: 24470 | Answers: 6

**解决方案 / Solution**:
In the early stages of Linux, Linus Torvalds released the Linux kernel source in an alpha state to signal to others that work towards a new Unix-like kernel was in development. By that time, as @RalfFriedi stated, the Linux kernel was cross-compiled in Minix.

As for usable software, Linus Torvalds also ported utilities to distribute along with the Linux kernel in order for others to test it. These programs were mainly bash and gcc, as described by LINUX's History by Linus Torvalds. Per the the Usenet post:


From: torvalds@klaava.Helsinki.FI (Linus Benedict Torvalds)  
Newsgroups: comp.os.minix
Subject: What would you like to see most in minix?
Summary: small poll for my new operating system  
Message-ID: &lt;1991Aug25.205708.9541@klaava.Helsinki.FI&gt;
Date: 25 Aug 91 20:57:08 GMT
Organization: University of Helsinki

  
  Hello everybody out there using minix -
  
  I'm doing a (free) operating system (just a hobby, won't be big and 
  professional like gnu) for 386(486) AT clones.  This has been brewing 
  since april, and is starting to get ready.  I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat
  (same physical layout of the file-system (due to practical reasons) among other things).
  
  I've currently ported bash(1.08) and gcc(1.40), and things seem to
  work.   This implies that I'll get something practical within a few
  months, and   I'd like to know what features most people would want. 
  Any suggestions   are welcome, but I won't promise I'll implement them
  :-)


Linus distributed the kernel and core utility programs in a diskette format for users to try it and possibly to contribute to it.

Afterwards, there were  H.J. Lu's Boot-root floppy diskettes. If this could be called a distribution, then it would gain the fame of being the first distribution capable of being installed on hard disk.


  These were two 5¼" diskette images containing the Linux kernel and the
  minimum tools required to get started. So minimal were these tools
  that to be able to boot from a hard drive required editing its master
  boot record with a hex editor.




Eventually the number of utilities grew larger than the maximum size of a diskette.

MCC Interim Linux was the first Linux distribution to be used by people with slightly less technical skills by introducing an automated installation and new utilities such as fdisk.


  MCC Interim Linux was a Linux distribution first released in February
  1992 by Owen Le Blanc of the Manchester Computing Centre (MCC), part
  of the University of Manchester.
  
  The first release of MCC Interim Linux was based on Linux 0.12 and
  made use of Theodore Ts'o's ramdisk code to copy a small root image to
  memory, freeing the floppy drive for additional utilities
  diskettes.[2]
  
  He also stated his distributions were "unofficial experiments",
  describing the goals of his releases as being:
  
  
  To provide a simple installation procedure.  
  To provide a more complete installation procedure.  
  To provide a backup/recovery service.  
  To back up his (then) current system.  
  To compile, link, and test every binary file under the current versions of the kernel, gcc, and libraries.  
  To provide a stable base system, which can be installed in a short time, and to which other software can be added with relatively little
  effort.  
  


After the MCC precursor, SLS was the first distribution offering the X Window System in May of 1992. Notably, the competitor to SLS, the mythical Yggdrasil, debuted in December of 1992.



Other major distributors followed as we know them today, notably Slackware in July of 1993 (based on SLS) and Debian in December of 1993 until the first official version 1.1 release in December of 1995. 

Image credits:
* Boot/Root diskettes image from: https://www.maketecheasier.com/
* yggdrasil diskette image from: https://yggdrasilblog.wordpress.com/

---

#### 118. &quot;Input/output error&quot; when accessing a directory

**问题描述 / Problem Description**:
Tags: ubuntu, directory, ntfs | Score: 117 | Views: 855860 | Answers: 8

**解决方案 / Solution**:
Input/Output errors during filesystem access attempts generally mean hardware issues.

Type dmesg and check the last few lines of output. If the disc or the connection to it is failing, it'll be noted there.

EDIT Are you mounting it via ntfs or ntfs-3g ? As I recall, the legacy ntfs driver  had no stable write support and was largely abandoned when it turned out ntfs-3g was significantly more stable and secure.

---

#### 119. What is stored in /dev/pts files and can we open them?

**问题描述 / Problem Description**:
Tags: linux, terminal, devices, pty | Score: 116 | Views: 155272 | Answers: 3

**解决方案 / Solution**:
Nothing is stored in /dev/pts. This filesystem lives purely in memory.

Entries in /dev/pts are pseudo-terminals (pty for short). Unix kernels have a generic notion of terminals. A terminal provides a way for applications to display output and to receive input through a terminal device. A process may have a controlling terminal — for a text mode application, this is how it interacts with the user.

Terminals can be either hardware terminals (“tty”, short for “teletype”) or pseudo-terminals (“pty”). Hardware terminals are connected over some interface such as a serial port (ttyS0, …) or USB (ttyUSB0, …) or over a PC screen and keyboard (tty1, …). Pseudo-terminals are provided by a terminal emulator, which is an application. Some types of pseudo-terminals are:


GUI applications such as xterm, gnome-terminal, konsole, … transform keyboard and mouse events into text input and display output graphically in some font.
Multiplexer applications such as screen and tmux relay input and output from and to another terminal, to decouple text mode applications from the actual terminal.
Remote shell applications such as sshd, telnetd, rlogind, … relay input and output between a remote terminal on the client and a pty on the server.


If a program opens a terminal for writing, the output from that program appears on the terminal. It is common to have several programs outputting to a terminal at the same time, though this can be confusing at times as there is no way to tell which part of the output came from which program. Background processes that try to write to their controlling terminal may be automatically suspended by a SIGTTOU signal.

If a program opens a terminal for reading, the input from the user is passed to that program. If multiple programs are reading from the same terminal, each character is routed independently to one of the programs; this is not recommended. Normally there is only a single program actively reading from the terminal at a given time; programs that try to read from their controlling terminal while they are not in the foreground are automatically suspended by a SIGTTIN signal.

To experiment, run tty in a terminal to see what the terminal device is. Let's say it's /dev/pts/42. In a shell in another terminal, run echo hello &gt;/dev/pts/42: the string hello will be displayed on the other terminal. Now run cat /dev/pts/42 and type in the other terminal. To kill that cat command (which will make the other terminal hard to use), press Ctrl+C.

Writing to another terminal is occasionally useful to display a notification; for example the write command does that. Reading from another terminal is not normally done.

---

#### 120. What is the benefit of compiling your own linux kernel?

**问题描述 / Problem Description**:
Tags: linux, kernel, compiling | Score: 116 | Views: 49846 | Answers: 13

**解决方案 / Solution**:
In my mind, the only benefit you really get from compiling your own linux kernel is:

You learn how to compile your own linux kernel.

It's not something you need to do for more speed / memory / xxx whatever.  It is a valuable thing to do if that's the stage you feel you are at in your development.  If you want to have a deeper understanding of what this whole "open source" thing is about, about how and what the different parts of the kernel are, then you should give it a go.  If you are just looking to speed up your boot time by 3 seconds, then... what's the point... go buy an ssd.   If you are curious, if you want to learn, then compiling your own kernel is a great idea and you will likely get a lot out of it.  

With that said, there are some specific reasons when it would be appropriate to compile your own kernel (as several people have pointed out in the other answers).  Generally these arise out of a specific need you have for a specific outcome, for example:


I need to get the system to boot/run on hardware with limited resources
I need to test out a patch and provide feedback to the developers
I need to disable something that is causing a conflict
I need to develop the linux kernel
I need to enable support for my unsupported hardware
I need to improve performance of x because I am hitting the current limits of the system (and I know what I'm doing)


The issue lies in thinking that there's some intrinsic benefit to compiling your own kernel when everything is already working the way it should be, and I don't think that there is.  Though you can spend countless hours disabling things you don't need and tweaking the things that are tweakable, the fact is the linux kernel is already pretty well tuned (by your distribution) for most user situations.

---

#### 121. How to mount a device in Linux?

**问题描述 / Problem Description**:
Tags: linux, mount | Score: 116 | Views: 1052927 | Answers: 10

**解决方案 / Solution**:
You can use fdisk to have an idea of what kind of partitions you have, for example:

fdisk -l


Shows:

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *          63   204796619   102398278+   7  HPFS/NTFS
/dev/sda2       204797952   205821951      512000   83  Linux
/dev/sda3       205821952   976773119   385475584   8e  Linux LVM


That way you know that you have sda1,2 and 3 partitions. The -t option is the filesystem type; it can be NTFS, FAT, EXT. In my example, sda1 is ntfs, so it should be something like:

mount -t ntfs /dev/sda1  /mnt/


USB devices are usually vfat and Linux are usually ext.

---

#### 122. Shell script fails: Syntax error: &quot;(&quot; unexpected

**问题描述 / Problem Description**:
Tags: bash, shell, ubuntu, shell-script | Score: 116 | Views: 485044 | Answers: 7

**解决方案 / Solution**:
The script does not begin with a shebang line, so the system executes it with /bin/sh. On Ubuntu, /bin/sh is dash, a shell designed for fast startup and execution with only standard features. When dash reaches line 68, it sees a syntax error: that parenthesis doesn't mean anything to it in context.

Since dash (like all other shells) is an interpreter, it won't complain until the execution reaches the problematic line. So even if the script successfully started at some point in your testing, it would have aborted once line 68 was reached.

The shebang line must be the very first thing in the file. Since you use bash features, the first line of the file must be #!/bin/bash or #!/usr/bin/env bash.

---

#### 123. How to find out which interface am I using for connecting to the internet?

**问题描述 / Problem Description**:
Tags: linux, routing | Score: 115 | Views: 197863 | Answers: 13

**解决方案 / Solution**:
You can use route to find your default route:

$ route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
192.168.1.0     *               255.255.255.0   U     1      0        0 eth0
link-local      *               255.255.0.0     U     1000   0        0 eth0
default         192.168.1.1     0.0.0.0         UG    0      0        0 eth0


The Iface column in the line with destination default tells you which interface is used.

---

#### 124. How to find the installation path for a software under linux?

**问题描述 / Problem Description**:
Tags: linux, software-installation | Score: 115 | Views: 668040 | Answers: 10

**解决方案 / Solution**:
You can use:

which fluidpoint


to see where it is executing from (if it's in your $PATH). Or:

find / -name fluidpoint 2&gt; /dev/null


to look for a file named fluipoint and redirect errors on virtual filesystems.

Usually they are in /sbin, /usr/sbin, /usr/local/bin or ~ as a hidden directory.

From Manual:

NAME
       which - shows the full path of (shell) commands.

SYNOPSIS
       which [options] [--] programname [...]


Full manual: https://linux.die.net/man/1/which

---

#### 125. Creating a ram disk on Linux

**问题描述 / Problem Description**:
Tags: linux, ramdisk | Score: 114 | Views: 178020 | Answers: 8

**解决方案 / Solution**:
The best way to create a ram disk on linux is tmpfs. It's a filesystem living in ram, so there is no need for ext2. You can create a tmpfs of 16Gb size with:

mount -o size=16G -t tmpfs none /mnt/tmpfs

---

#### 126. What is meant by mounting a device in Linux?

**问题描述 / Problem Description**:
Tags: linux, mount | Score: 114 | Views: 150384 | Answers: 4

**解决方案 / Solution**:
Unix systems have a single directory tree. All accessible storage must have an associated location in this single directory tree. This is unlike Windows where (in the most common syntax for file paths) there is one directory tree per storage component (drive).
Mounting is the act of associating a storage device to a particular location in the directory tree. For example, when the system boots, a particular storage device (commonly called the root partition) is associated with the root of the directory tree, i.e., that storage device is mounted on / (the root directory).
It's worth noting that mounting not only associates the device containing the data with a directory, but also with a filesystem driver, which is a piece of code that understands how the data on the device is organized and presents it as files and directories.
Let's say you now want to access files on a CD-ROM. You must mount the CD-ROM on a location in the directory tree (this may be done automatically when you insert the CD). Let's say the CD-ROM device is /dev/cdrom and the chosen mount point is /media/cdrom. The corresponding command is
mount /dev/cdrom /media/cdrom

After that command is run, a file whose location on the CD-ROM is /dir/file is now accessible on your system as /media/cdrom/dir/file. When you've finished using the CD, you run the command umount /dev/cdrom or umount /media/cdrom (both will work; typical desktop environments will do this when you click on the “eject” or ”safely remove” button).
Mounting applies to anything that is made accessible as files, not just actual storage devices. For example, all Linux systems have a special filesystem mounted under /proc. That filesystem (called proc) does not have underlying storage: the files in it give information about running processes and various other system information; the information is provided directly by the kernel from its in-memory data structures.

---

#### 127. How to limit network bandwidth?

**问题描述 / Problem Description**:
Tags: linux, networking, bandwidth, qos | Score: 113 | Views: 240133 | Answers: 6

**解决方案 / Solution**:
You can throttle the network bandwidth on the interface using the command called tc Man page available at http://man7.org/linux/man-pages/man8/tc.8.html

For a simple script, try wondershaper.

An example from using tc:
tc qdisc add dev eth0 root tbf rate 1024kbit latency 50ms burst 1540

---

#### 128. Why are true and false so large?

**问题描述 / Problem Description**:
Tags: linux, reverse-engineering | Score: 112 | Views: 27867 | Answers: 5

**解决方案 / Solution**:
In the past, /bin/true and /bin/false in the shell were actually scripts.
For instance, in a PDP/11 Unix System 7:
$ ls -la /bin/true /bin/false
-rwxr-xr-x 1 bin         7 Jun  8  1979 /bin/false
-rwxr-xr-x 1 bin         0 Jun  8  1979 /bin/true
$
$ cat /bin/false
exit 1
$
$ cat /bin/true
$  

Nowadays, at least in bash, the trueand false commands are implemented as shell built-in commands. Thus no executable binary files are invoked by default, both when using the false and true directives in the bash command line and inside shell scripts.
From the bashsource, builtins/mkbuiltins.c:
char *posix_builtins[] =
    {
      "alias", "bg", "cd", "command", "false", "fc", "fg", "getopts", "jobs",
      "kill", "newgrp", "pwd", "read", "true", "umask", "unalias", "wait",
      (char *)NULL
    };

Also per @meuh comments:
$ command -V true false
true is a shell builtin
false is a shell builtin

So it can be said with a high degree of certainty the trueand false executable files exist mainly for being called from other programs.
From now on, the answer will focus on the /bin/true binary from the coreutilspackage in Debian 9 / 64 bits. (/usr/bin/true running RedHat. RedHat and Debian use both the  coreutils package, analysed the compiled version of the latter having it more at hand).
As it can be seen in the source file false.c, /bin/false is compiled with (almost) the same source code as /bin/true, just returning EXIT_FAILURE (1) instead, so this answer can be applied for both binaries.
#define EXIT_STATUS EXIT_FAILURE
#include &quot;true.c&quot;

As it also can be confirmed by both executables having the same size:
$ ls -l /bin/true /bin/false
-rwxr-xr-x 1 root root 31464 Feb 22  2017 /bin/false
-rwxr-xr-x 1 root root 31464 Feb 22  2017 /bin/true

Alas, the direct answer to the question &quot;why are true and false so large?&quot; could be, because there are not anymore so pressing reasons to care about their top performance. They are not essential to bash performance, not being used anymore by bash (scripting).
Similar comments apply to their size, 26KB for the kind of hardware we have nowadays is insignificant. Space is not at premium for the typical server/desktop anymore, and they do not even bother anymore to use the same binary for false and true, as it is just deployed twice in distributions using coreutils.
Focusing, however, in the real spirit of the question, why something that should be so simple and small, gets so large?
The real distribution of the sections of /bin/true is as these charts shows; the main code+data amounts to roughly 3KB out of a 26KB binary, which amounts to 12% of the size of /bin/true.
The true utility got indeed more cruft code over the years, most notably the standard support for --version and --help.
However, that it is not the (only) main justification for it being so big, but rather, while being dynamically linked (using shared libs), also having part of a generic library commonly used by coreutils binaries linked as a static library.  The metada for building an elf executable file also amounts for a significant part of the binary, being it a relatively small file by today´s standards.
The rest of the answer is for explaining how we got to build the following charts detailing the composition of the /bin/true executable binary file and how we arrived to that conclusion.


As @Maks says, the binary was compiled from C; as per my comment also, it is also confirmed it is from coreutils. We are pointing directly to the author(s) git https://github.com/wertarbyte/coreutils/blob/master/src/true.c, instead of the gnu git as @Maks  (same sources, different repositories - this repository was selected as it has the full source of the coreutils libraries)
We can see the various building blocks of the /bin/truebinary here (Debian 9 - 64 bits from coreutils):
$ file /bin/true
/bin/true: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=9ae82394864538fa7b23b7f87b259ea2a20889c4, stripped

$ size /bin/true
    text       data     bss     dec     hex filename
   24583       1160     416   26159    662f true

Of those:

text (usually code) is around 24KB
data (initialised variables, mostly strings) are around 1KB
bss (uninitialized  data) 0.5KB

Of the 24KB, around 1KB is for fixing up the 58 external functions.
That still leaves around roughly 23KB for rest of the code. We will show down bellow that the actual main file - main()+usage() code is around 1KB compiled, and explain what the other 22KB are used for.
Drilling further down the binary with readelf -S true, we can see that while the binary is 26159 bytes, the actual compiled code is 13017 bytes, and the rest is assorted data/initialisation code.
However, true.c is not the whole story and 13KB seems pretty much excessive if it were only that file; we can see functions called in main() that are not listed in the external functions seen in the elf with objdump -T true ; functions that are present at:

https://github.com/coreutils/gnulib/blob/master/lib/progname.c
https://github.com/coreutils/gnulib/blob/master/lib/closeout.c
https://github.com/coreutils/gnulib/blob/master/lib/version-etc.c

Those extra functions not linked externally in main() are:

set_program_name()
close_stdout()
version_etc()

So my first suspicion was partly correct, whilst the library is using dynamic libraries, the /bin/true binary is big because it has some static libraries included with it (but that is not the only cause).
Compiling C code is not usually that inefficient for having such space unaccounted for, hence my initial suspicion something was amiss.
The extra space, almost 90% of the size of the binary, is indeed extra libraries/elf metadata.
While using Hopper for disassembling/decompiling the binary to understand where functions are, it can be seen the compiled binary code of true.c/usage() function is actually 833 bytes, and of the true.c/main() function is 225 bytes, which is roughly slightly less than 1KB. The logic for version functions, which is buried in the static libraries, is around 1KB.
The actual compiled main()+usage()+version()+strings+vars are only using up around 3KB to 3.5KB.
It is indeed ironic, such small and humble utilities have became bigger in size for the reasons explained above.
related question: Understanding what a Linux binary is doing
true.c main() with the offending function calls:
int
main (int argc, char **argv)
{
  /* Recognize --help or --version only if it's the only command-line
     argument.  */
  if (argc == 2)
    {
      initialize_main (&amp;argc, &amp;argv);
      set_program_name (argv[0]);           &lt;-----------
      setlocale (LC_ALL, &quot;&quot;);
      bindtextdomain (PACKAGE, LOCALEDIR);
      textdomain (PACKAGE);

      atexit (close_stdout);             &lt;-----

      if (STREQ (argv[1], &quot;--help&quot;))
        usage (EXIT_STATUS);

      if (STREQ (argv[1], &quot;--version&quot;))
        version_etc (stdout, PROGRAM_NAME, PACKAGE_NAME, Version,  AUTHORS,  &lt;------
                     (char *) NULL);
    }

  exit (EXIT_STATUS);
}

The decimal size of the various sections of the binary:
$ size -A -t true 
true  :
section               size      addr
.interp                 28       568
.note.ABI-tag           32       596
.note.gnu.build-id      36       628
.gnu.hash               60       664
.dynsym               1416       728
.dynstr                676      2144
.gnu.version           118      2820
.gnu.version_r          96      2944
.rela.dyn              624      3040
.rela.plt             1104      3664
.init                   23      4768
.plt                   752      4800
.plt.got                 8      5552
.text                13017      5568
.fini                    9     18588
.rodata               3104     18624
.eh_frame_hdr          572     21728
.eh_frame             2908     22304
.init_array              8   2125160
.fini_array              8   2125168
.jcr                     8   2125176
.data.rel.ro            88   2125184
.dynamic               480   2125272
.got                    48   2125752
.got.plt               392   2125824
.data                  128   2126240
.bss                   416   2126368
.gnu_debuglink          52         0
Total                26211

Output of readelf -S true
$ readelf -S true
There are 30 section headers, starting at offset 0x7368:

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000000238  00000238
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.ABI-tag     NOTE             0000000000000254  00000254
       0000000000000020  0000000000000000   A       0     0     4
  [ 3] .note.gnu.build-i NOTE             0000000000000274  00000274
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .gnu.hash         GNU_HASH         0000000000000298  00000298
       000000000000003c  0000000000000000   A       5     0     8
  [ 5] .dynsym           DYNSYM           00000000000002d8  000002d8
       0000000000000588  0000000000000018   A       6     1     8
  [ 6] .dynstr           STRTAB           0000000000000860  00000860
       00000000000002a4  0000000000000000   A       0     0     1
  [ 7] .gnu.version      VERSYM           0000000000000b04  00000b04
       0000000000000076  0000000000000002   A       5     0     2
  [ 8] .gnu.version_r    VERNEED          0000000000000b80  00000b80
       0000000000000060  0000000000000000   A       6     1     8
  [ 9] .rela.dyn         RELA             0000000000000be0  00000be0
       0000000000000270  0000000000000018   A       5     0     8
  [10] .rela.plt         RELA             0000000000000e50  00000e50
       0000000000000450  0000000000000018  AI       5    25     8
  [11] .init             PROGBITS         00000000000012a0  000012a0
       0000000000000017  0000000000000000  AX       0     0     4
  [12] .plt              PROGBITS         00000000000012c0  000012c0
       00000000000002f0  0000000000000010  AX       0     0     16
  [13] .plt.got          PROGBITS         00000000000015b0  000015b0
       0000000000000008  0000000000000000  AX       0     0     8
  [14] .text             PROGBITS         00000000000015c0  000015c0
       00000000000032d9  0000000000000000  AX       0     0     16
  [15] .fini             PROGBITS         000000000000489c  0000489c
       0000000000000009  0000000000000000  AX       0     0     4
  [16] .rodata           PROGBITS         00000000000048c0  000048c0
       0000000000000c20  0000000000000000   A       0     0     32
  [17] .eh_frame_hdr     PROGBITS         00000000000054e0  000054e0
       000000000000023c  0000000000000000   A       0     0     4
  [18] .eh_frame         PROGBITS         0000000000005720  00005720
       0000000000000b5c  0000000000000000   A       0     0     8
  [19] .init_array       INIT_ARRAY       0000000000206d68  00006d68
       0000000000000008  0000000000000008  WA       0     0     8
  [20] .fini_array       FINI_ARRAY       0000000000206d70  00006d70
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .jcr              PROGBITS         0000000000206d78  00006d78
       0000000000000008  0000000000000000  WA       0     0     8
  [22] .data.rel.ro      PROGBITS         0000000000206d80  00006d80
       0000000000000058  0000000000000000  WA       0     0     32
  [23] .dynamic          DYNAMIC          0000000000206dd8  00006dd8
       00000000000001e0  0000000000000010  WA       6     0     8
  [24] .got              PROGBITS         0000000000206fb8  00006fb8
       0000000000000030  0000000000000008  WA       0     0     8
  [25] .got.plt          PROGBITS         0000000000207000  00007000
       0000000000000188  0000000000000008  WA       0     0     8
  [26] .data             PROGBITS         00000000002071a0  000071a0
       0000000000000080  0000000000000000  WA       0     0     32
  [27] .bss              NOBITS           0000000000207220  00007220
       00000000000001a0  0000000000000000  WA       0     0     32
  [28] .gnu_debuglink    PROGBITS         0000000000000000  00007220
       0000000000000034  0000000000000000           0     0     1
  [29] .shstrtab         STRTAB           0000000000000000  00007254
       000000000000010f  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)

Output of objdump -T true (external functions dynamically linked on run-time)
$ objdump -T true

true:     file format elf64-x86-64

DYNAMIC SYMBOL TABLE:
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __uflow
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 getenv
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 free
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 abort
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __errno_location
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 strncmp
0000000000000000  w   D  *UND*  0000000000000000              _ITM_deregisterTMCloneTable
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 _exit
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __fpending
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 textdomain
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fclose
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 bindtextdomain
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 dcgettext
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __ctype_get_mb_cur_max
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 strlen
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.4   __stack_chk_fail
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 mbrtowc
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 strrchr
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 lseek
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 memset
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fscanf
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 close
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __libc_start_main
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 memcmp
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fputs_unlocked
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 calloc
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 strcmp
0000000000000000  w   D  *UND*  0000000000000000              __gmon_start__
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.14  memcpy
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fileno
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 malloc
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fflush
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 nl_langinfo
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 ungetc
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __freading
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 realloc
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fdopen
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 setlocale
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.3.4 __printf_chk
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 error
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 open
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fseeko
0000000000000000  w   D  *UND*  0000000000000000              _Jv_RegisterClasses
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 __cxa_atexit
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 exit
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 fwrite
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.3.4 __fprintf_chk
0000000000000000  w   D  *UND*  0000000000000000              _ITM_registerTMCloneTable
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 mbsinit
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.2.5 iswprint
0000000000000000  w   DF *UND*  0000000000000000  GLIBC_2.2.5 __cxa_finalize
0000000000000000      DF *UND*  0000000000000000  GLIBC_2.3   __ctype_b_loc
0000000000207228 g    DO .bss   0000000000000008  GLIBC_2.2.5 stdout
0000000000207220 g    DO .bss   0000000000000008  GLIBC_2.2.5 __progname
0000000000207230  w   DO .bss   0000000000000008  GLIBC_2.2.5 program_invocation_name
0000000000207230 g    DO .bss   0000000000000008  GLIBC_2.2.5 __progname_full
0000000000207220  w   DO .bss   0000000000000008  GLIBC_2.2.5 program_invocation_short_name
0000000000207240 g    DO .bss   0000000000000008  GLIBC_2.2.5 stderr

---

#### 129. What is this new /run filesystem?

**问题描述 / Problem Description**:
Tags: linux, filesystems, directory-structure | Score: 112 | Views: 132435 | Answers: 2

**解决方案 / Solution**:
Apparently, many tools (among them udev) will soon require a /run/ directory that is mounted early (as tmpfs). Arch developers introduced /run last month to prepare for this.

The udev runtime data moved from /dev/.udev/ to /run/udev/. The /run mountpoint is supposed to be a tmpfs mounted during early boot, available and writable to for all tools at any time during bootup, it replaces /var/run/, which should become a symlink some day.(1)

 
There is more detail here (now dead, link to archive).
(1) From thread on the Arch Projects ML

---

#### 130. Recover cron jobs accidently removed with crontab -r

**问题描述 / Problem Description**:
Tags: linux, cron | Score: 112 | Views: 107293 | Answers: 5

**解决方案 / Solution**:
crontab -r removes the only file containing the cron jobs. 

So if you did not make a backup, your only recovery options are:


On RedHat/CentOS, if your jobs have been triggered before, you can find the cron log in /var/log/cron. The file will help you rewrite the jobs again. 
Another option is to recover the file using a file recovery tool. This is less likely to be successful though, since the system partition is usually a busy one and corresponding sectors probably have already been overwritten.
On Ubuntu/Debian, if your task has run before, try grep CRON /var/log/syslog

---

#### 131. A list of available D-Bus services

**问题描述 / Problem Description**:
Tags: linux, d-bus, ipc | Score: 111 | Views: 122640 | Answers: 6

**解决方案 / Solution**:
On QT setups (short commands and clean, human readable output) you can run:
qdbus

will list list the services available on the session bus and
qdbus --system

will list list the services available on the system bus.

On any setup you can use dbus-send
dbus-send --print-reply --dest=org.freedesktop.DBus  /org/freedesktop/DBus org.freedesktop.DBus.ListNames

Just like qdbus, if --session or no message bus is specified, dbus will send to the login session message bus. So the above will list the services available on the session bus.
Use --system if you want instead to use the system wide message bus:
dbus-send --system --print-reply --dest=org.freedesktop.DBus  /org/freedesktop/DBus org.freedesktop.DBus.ListNames

---

#### 132. How to use command line to change volume?

**问题描述 / Problem Description**:
Tags: linux, command-line, audio, alsa | Score: 111 | Views: 271823 | Answers: 7

**解决方案 / Solution**:
You can use amixer. It's in the alsa-utils package on Ubuntu and Debian.
Run amixer without parameters to get an overview about your controls for the default device.
You can also use alsamixer without parameters (from the same package) to get a more visual overview. Use F6 to see and switch between devices. Commonly, you might have PulseAudio and a hardware sound card to select from.
Then use amixer with the set command to set the volume.
For example, to set the master channel to 50%:
amixer set Master 50%

Master is the control name and should match one that you see when running without parameters.
Note the % sign, without it, it will treat the value as a 0 - 65536 level.
If PulseAudio is not your default device, you can use the -D switch:
amixer -D pulse set Master 50%

Other useful commands pointed out in the comments:
To increase/decrease the volume use +/- after the number, use
amixer set Master 10%+
amixer set Master 10%-

To mute, unmute or toggle between muted/unmuted state, use
amixer set Master mute
amixer set Master unmute
amixer set Master toggle

Also note that there might be two different percentage scales, the default raw and for some devices a more natural scale based on decibel, which is also used by alsamixer. Use -M to use the latter.
Finally, if you're interested only in PulseAudio, you might want to check out pactl (see one of the other answers).

---

#### 133. Easy command line method to determine specific ARM architecture string?

**问题描述 / Problem Description**:
Tags: debian, ubuntu, scripting, architecture, cpu-architecture | Score: 111 | Views: 232891 | Answers: 2

**解决方案 / Solution**:
On Debian and derivatives,
dpkg --print-architecture

will output the primary architecture of the machine it’s run on. This will be armhf on a machine running 32-bit ARM Debian or Ubuntu (or a derivative), arm64 on a machine running 64-bit ARM.
On RPM-based systems,
rpm --eval '%{_arch}'

will output the current architecture name (which may be influenced by other parameters, e.g. --target).
Note that the running architecture may be different from the hardware architecture or even the kernel architecture. It’s possible to run i386 Debian on a 64-bit Intel or AMD CPU, and I believe it’s possible to run armhf on a 64-bit ARM CPU. It’s also possible to have mostly i386 binaries (so the primary architecture is i386) on an amd64 kernel, or even binaries from an entirely different architecture if it’s supported by QEMU (a common use for this is debootstrap chroots used for cross-compiling).

---

#### 134. Does `sl` ever show the current directory?

**问题描述 / Problem Description**:
Tags: linux | Score: 110 | Views: 23222 | Answers: 10

**解决方案 / Solution**:
As far as I know, the only condition under which sl shows the current directory is when you mistype it as ls.

---

#### 135. How to turn off Wireless power management permanently

**问题描述 / Problem Description**:
Tags: linux, wifi, power-management | Score: 109 | Views: 275990 | Answers: 5

**解决方案 / Solution**:
Open this file with your favorite text editor, I use nano here:
sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf

By default there is:
[connection]
wifi.powersave = 3

Change the value to 2.

Possible values for the wifi.powersave field are:
NM_SETTING_WIRELESS_POWERSAVE_DEFAULT (0): use the default value
NM_SETTING_WIRELESS_POWERSAVE_IGNORE  (1): don't touch existing setting
NM_SETTING_WIRELESS_POWERSAVE_DISABLE (2): disable powersave
NM_SETTING_WIRELESS_POWERSAVE_ENABLE  (3): enable powersave

(Informal source on GitHub for these values.)

To take effect, just run:
sudo systemctl restart NetworkManager

---

#### 136. Execute a specific command in a given directory without cd&#39;ing to it?

**问题描述 / Problem Description**:
Tags: linux, bash, cd-command | Score: 109 | Views: 147345 | Answers: 11

**解决方案 / Solution**:
I don't know if this counts, but you can make a subshell:

$ (cd /var/log &amp;&amp; cp -- *.log ~/Desktop)


The directory is only changed for that subshell, so you avoid the work of needing to cd - afterwards.

---

#### 137. Is there a way to stop having to write &#39;sudo&#39; for every little thing in Linux?

**问题描述 / Problem Description**:
Tags: linux, permissions, sudo | Score: 109 | Views: 371243 | Answers: 11

**解决方案 / Solution**:
Two options come to my mind:

Own the directory you want by using chown:
sudo chown your_username directory 

(replace your_username with your username and directory with the directory you want.)

The other thing you can do is work as root as long as you KNOW WHAT YOU ARE DOING. To use root do:
sudo -s



and then you can do anything without having to type sudo before every command.
To exit this sudo -s shell terminal, type exit and you will be returned to the previous shell terminal.

---

#### 138. Difference between cp -r and cp -R (copy command)

**问题描述 / Problem Description**:
Tags: linux, cp | Score: 109 | Views: 156009 | Answers: 5

**解决方案 / Solution**:
While -R is posix well-defined, -r is not portable!

On Linux, in the GNU and BusyBox implementations of cp, -r and -R are equivalent. 

On the other side, as you can read in the POSIX manual page of cp, -r behavior  is implementation-defined.


    * If  neither  the  -R  nor  -r  options were specified, cp shall take
      actions based on the type and contents of the file referenced by the
      symbolic link, and not by the symbolic link itself.

    * If the -R option was specified:

       * If  none  of  the  options  -H,  -L, nor -P were specified, it is
         unspecified which of -H, -L, or -P will be used as a default.

       * If the -H option was specified, cp shall take  actions based on
         the type and contents of the file referenced by any symbolic link
         specified as a source_file operand.

       * If the -L option was specified, cp shall take  actions based  on
         the type and contents of the file referenced by any symbolic link
         specified as a source_file operand or any symbolic links encoun-
         tered during traversal of a file hierarchy.

       * If  the  -P option was specified, cp shall copy any symbolic link
         specified as a source_file operand and any symbolic links encoun-
         tered  during traversal of a file hierarchy, and shall not follow
         any symbolic links.

    * If the -r option was  specified,  the  behavior  is implementation-
      defined.

---

#### 139. How to find out if a system uses SysV, Upstart or Systemd initsystem

**问题描述 / Problem Description**:
Tags: linux, systemd, init, upstart, sysvinit | Score: 108 | Views: 128579 | Answers: 5

**解决方案 / Solution**:
The init process is always assigned PID 1. The /proc filesystem provides a way to obtain the path to an executable given a PID.

In other words:

nathan@nathan-desktop:~$ sudo stat /proc/1/exe
  File: '/proc/1/exe' -&gt; '/sbin/upstart'


As you can see, the init process on my Ubuntu 14.10 box is Upstart. Ubuntu 15.04 uses systemd, so running that command instead yields:

nathan@nathan-gnome:~$ sudo stat /proc/1/exe
  File: '/proc/1/exe' -&gt; '/lib/systemd/systemd'


If the system you're on gives /sbin/init as a result, then you'll want to try statting that file:

nathan@nathan-gnome:~$ sudo stat /proc/1/exe
  File: '/proc/1/exe' -&gt; '/sbin/init'
nathan@nathan-gnome:~$ stat /sbin/init
  File: ‘/sbin/init’ -&gt; ‘/lib/systemd/systemd’


You can also execute it to find out more:

[user@centos ~]$ /sbin/init --version
init (upstart 0.6.5)
Copyright (C) 2010 Canonical Ltd.

---

#### 140. How to see disk details like manufacturer in Linux

**问题描述 / Problem Description**:
Tags: linux, hard-disk, sfdisk | Score: 108 | Views: 255767 | Answers: 9

**解决方案 / Solution**:
Try these commands:

lshw -class disk  

hwinfo --disk


You may have to install hwinfo.

Concerning hdparm:
hdparm(8) says:  

Although this utility is intended primarily for use with SATA/IDE hard disk 
devices, several of the options are also valid (and permitted) for use with 
SCSI hard disk devices and MFM/RLL hard disks with XT interfaces.


and:

Some options (eg. -r for SCSI) may not work with old kernels as necessary 
ioctl()´s were not supported.

---

#### 141. Can I set up system mail to use an external SMTP server?

**问题描述 / Problem Description**:
Tags: linux, smtp, email | Score: 108 | Views: 391910 | Answers: 7

**解决方案 / Solution**:
I found sSMTP very simple to use.

In Debian based systems:

apt-get install ssmtp


Then edit the configuration file in /etc/ssmtp/ssmtp.conf

A sample configuration to use your gmail for sending e-mails:

# root is the person who gets all mail for userids &lt; 1000
root=your@email.com

# Here is the gmail configuration (or change it to your private smtp server)
mailhub=smtp.gmail.com:587
AuthUser=your@gmail.com
AuthPass=yourGmailPass
UseTLS=YES
UseSTARTTLS=YES


Note: Make sure the "mail" command is present in your system. mailutils package should provide this one in Debian based systems.

Update: There are people (and bug reports for different Linux distributions) reporting that sSMTP will not accept passwords with a 'space' or '#' character. If sSMTP is not working for you, this may be the case.

---

#### 142. How can I restart the SSH daemon on Ubuntu?

**问题描述 / Problem Description**:
Tags: ubuntu, services, sshd, upstart | Score: 108 | Views: 396953 | Answers: 2

**解决方案 / Solution**:
Ubuntu calls the service ssh, not sshd.

service ssh restart


The service is also controlled by upstart, and not sysvinit. So you'll find it at /etc/init/ssh.conf instead of /etc/init.d/ssh.

---

#### 143. Linux: How to find the device driver used for a device?

**问题描述 / Problem Description**:
Tags: linux, linux-kernel | Score: 107 | Views: 494262 | Answers: 12

**解决方案 / Solution**:
Just use /sys.

Example. I want to find the driver for my Ethernet card:

$ sudo lspci
...
02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express Gigabit Ethernet controller (rev 01)
$ find /sys | grep drivers.*02:00
/sys/bus/pci/drivers/r8169/0000:02:00.0


That is r8169.

First I need to find coordinates of the device using lspci; then I find driver that is used for the devices with these coordinates.

---

#### 144. Is there a whoami to find the current group I&#39;m logged in as?

**问题描述 / Problem Description**:
Tags: linux, users, group | Score: 107 | Views: 114828 | Answers: 2

**解决方案 / Solution**:
I figured I can use the following. 

id -g


To get all the groups I belong

id -G


And to get the actual names, instead of the ids, just pass the flag -n.

id -Gn


This last command will yield the same result as executing

groups

---

#### 145. Understanding UNIX permissions and file types

**问题描述 / Problem Description**:
Tags: linux, permissions, ls, chmod | Score: 106 | Views: 117704 | Answers: 6

**解决方案 / Solution**:
I’ll answer your questions in three parts: file types, permissions, and use cases for the various forms of chmod.

File types

The first character in ls -l output represents the file type; d means it’s a directory. It can’t be set or unset, it depends on how the file was created. You can find the complete list of file types in the ls documentation; those you’re likely to come across are


-: “regular” file, created with any program which can write a file
b: block special file, typically disk or partition devices, can be created with mknod
c: character special file, can also be created with mknod (see /dev for examples)
d: directory, can be created with mkdir
l: symbolic link, can be created with ln -s
p: named pipe, can be created with mkfifo
s: socket, can be created with nc -U
D: door, created by some server processes on Solaris/openindiana.


Permissions

chmod 0777 is used to set all the permissions in one chmod execution, rather than combining changes with u+ etc. Each of the four digits is an octal value representing a set of permissions:


suid, sgid and “sticky” (see below)
user permissions
group permissions
“other” permissions


The octal value is calculated as the sum of the permissions:


“read” is 4
“write” is 2
“execute” is 1


For the first digit:


suid is 4; binaries with this bit set run as their owner user (commonly root)
sgid is 2; binaries with this bit set run as their owner group (this was used for games so high scores could be shared, but it’s often a security risk when combined with vulnerabilities in the games), and files created in directories with this bit set belong to the directory’s owner group by default (this is handy for creating shared folders)
“sticky” (or “restricted deletion”) is 1; files in directories with this bit set can only be deleted by their owner, the directory’s owner, or root (see /tmp for a common example of this).


See the chmod manpage for details. Note that in all this I’m ignoring other security features which can alter users’ permissions on files (SELinux, file ACLs...).

Special bits are handled differently depending on the type of file (regular file or directory) and the underlying system. (This is mentioned in the chmod manpage.) On the system I used to test this (with coreutils 8.23 on an ext4 filesystem, running Linux kernel 3.16.7-ckt2), the behaviour is as follows. For a file, the special bits are always cleared unless explicitly set, so chmod 0777 is equivalent to chmod 777, and both commands clear the special bits and give everyone full permissions on the file. For a directory, the special bits are never fully cleared using the four-digit numeric form, so in effect chmod 0777 is also equivalent to chmod 777 but it’s misleading since some of the special bits will remain as-is. (A previous version of this answer got this wrong.) To clear special bits on directories you need to use u-s, g-s and/or o-t explicitly or specify a negative numeric value, so chmod -7000 will clear all the special bits on a directory.

In ls -l output, suid, sgid and “sticky” appear in place of the x entry: suid is s or S instead of the user’s x, sgid is s or S instead of the group’s x, and “sticky” is t or T instead of others’ x. A lower-case letter indicates that both the special bit and the executable bit are set; an upper-case letter indicates that only the special bit is set.

The various forms of chmod

Because of the behaviour described above, using the full four digits in chmod can be confusing (at least it turns out I was confused). It’s useful when you want to set special bits as well as permission bits; otherwise the bits are cleared if you’re manipulating a file, preserved if you’re manipulating a directory. So chmod 2750 ensures you’ll get at least sgid and exactly u=rwx,g=rx,o=; but chmod 0750 won’t necessarily clear the special bits.

Using numeric modes instead of text commands ([ugo][=+-][rwxXst]) is probably more a case of habit and the aim of the command. Once you’re used to using numeric modes, it’s often easier to just specify the full mode that way; and it’s useful to be able to think of permissions using numeric modes, since many other commands can use them (install, mknod...).

Some text variants can come in handy: if you simply want to ensure a file can be executed by anyone, chmod a+x will do that, regardless of what the other permissions are. Likewise, +X adds the execute permission only if one of the execute permissions is already set or the file is a directory; this can be handy for restoring permissions globally without having to special-case files v. directories. Thus, chmod -R ug=rX,u+w,o= is equivalent to applying chmod -R 750 to all directories and executable files and chmod -R 640 to all other files.

---

#### 146. What are the alternatives for checking open ports, besides telnet?

**问题描述 / Problem Description**:
Tags: linux, networking, curl, telnet | Score: 105 | Views: 272487 | Answers: 9

**解决方案 / Solution**:
Netcat (nc) is one option.
nc -zv kafka02 6667


-z = sets nc to simply scan for listening daemons, without actually sending any data to them
-v = enables verbose mode

---

#### 147. List all available ssl ca certificates

**问题描述 / Problem Description**:
Tags: linux, openssl | Score: 104 | Views: 581877 | Answers: 8

**解决方案 / Solution**:
It's not SSL keys you want, it's certificate authorities, and more precisely their certificates.
You could try:
awk -v cmd='openssl x509 -noout -subject' '
    /BEGIN/{close(cmd)};{print | cmd}' &lt; /etc/ssl/certs/ca-certificates.crt

To get the &quot;subject&quot; of every CA certificate in /etc/ssl/certs/ca-certificates.crt (this works because openssl exits after reading an individual cert block, but awk relaunches openssl on the next print | cmd call).
Beware that sometimes, you get that error when SSL servers forget to provide the intermediate certificates.
Use openssl s_client -showcerts -connect the-git-server:443 to get the list of certificates  being sent.
Note that the pathname of the certificates bundle may differ depending on operating system. The directory holding the certs sub-directory is given by the command openssl version -d. The actual certificates file in that directory may additionally have a different name.

---

#### 148. What does status &quot;active (exited)&quot; mean for a systemd service?

**问题描述 / Problem Description**:
Tags: linux, systemd, services, sysvinit | Score: 104 | Views: 221266 | Answers: 3

**解决方案 / Solution**:
It seems you are running a system with systemd yet you are using sysV commands. Did you create a sysV init script or a systemd unit file?

State active (exited) means that systemd has successfully run the commands but that it does not know there is a daemon to monitor.

If there is you must define it in the unit file by configuring the Type and ExecStart options appropriately according to whether the process you start is the main proces, forks child processes and exits etc.

Check the different systemd man pages or update your question and post the unit file or init script.

---

#### 149. What do the &quot;buff/cache&quot; and &quot;avail mem&quot; fields in top mean?

**问题描述 / Problem Description**:
Tags: linux, memory, top | Score: 102 | Views: 185264 | Answers: 3

**解决方案 / Solution**:
top’s manpage doesn’t describe the fields, but free’s does:

buffers
Memory used by kernel buffers (Buffers in /proc/meminfo)
cache
Memory used by the page cache and slabs (Cached and
SReclaimable in /proc/meminfo)
buff/cache
Sum of buffers and cache
available
Estimation of how much memory is available for starting new
applications, without swapping. Unlike the data provided by
the cache or free fields, this field takes into account page
cache and also that not all reclaimable memory slabs will be
reclaimed due to items being in use (MemAvailable in
/proc/meminfo, available on kernels 3.14, emulated on kernels
2.6.27+, otherwise the same as free)

Basically, “buff/cache” counts memory used for data that’s on disk or should end up there soon, and as a result is potentially usable (the corresponding memory can be made available immediately, if it hasn’t been modified since it was read, or given enough time, if it has); “available” measures the amount of memory which can be allocated and used without causing more swapping (see How can I get the amount of available memory portably across distributions? for a lot more detail on that).

---

#### 150. What is kernel ip forwarding?

**问题描述 / Problem Description**:
Tags: linux, kernel, ip, routing | Score: 102 | Views: 119877 | Answers: 2

**解决方案 / Solution**:
"IP forwarding" is a synonym for "routing."  It is called "kernel IP forwarding" because it is a feature of the Linux kernel.

A router has multiple network interfaces.  If traffic comes in on one interface that matches a subnet of another network interface, a router then forwards that traffic to the other network interface.

So, let's say you have two NICs, one (NIC 1) is at address 192.168.2.1/24, and the other (NIC 2) is 192.168.3.1/24.  If forwarding is enabled, and a packet comes in on NIC 1 with a "destination address" of 192.168.3.8, the router will resend that packet out of the NIC 2.

It's common for routers functioning as gateways to the Internet to have a default route whereby any traffic that doesn't match any NICs will go through the default route's NIC.  So in the above example, if you have an internet connection on NIC 2, you'd set NIC 2 as your default route and then any traffic coming in from NIC 1 that isn't destined for something on 192.168.2.0/24 will go through NIC 2.  Hopefully there's other routers past NIC 2 that can further route it (in the case of the Internet, the next hop would be your ISP's router, and then their providers upstream router, etc.)

Enabling ip_forward tells your Linux system to do this.  For it to be meaningful, you need two network interfaces (any 2 or more of wired NIC cards, Wifi cards or chipsets, PPP links over a 56k modem or serial, etc.).  

When doing routing, security is important and that's where Linux's packet filter, iptables, gets involved.  So you will need an iptables configuration consistent with your needs.

Note that enabling forwarding with iptables disabled and/or without taking firewalling and security into account could leave you open to vulnerabilites if one of the NICs is facing the Internet or a subnet you don't have control over.

---

#### 151. How to limit a process to one CPU core in Linux?

**问题描述 / Problem Description**:
Tags: linux, process, cpu, limit | Score: 102 | Views: 129693 | Answers: 2

**解决方案 / Solution**:
Under Linux, execute the sched_setaffinity system call. The affinity of a process is the set of processors on which it can run. There's a standard shell wrapper: taskset. For example, to pin a process to CPU #0 (you need to choose a specific CPU):

taskset -c 0 mycommand --option  # start a command with the given affinity
taskset -c -pa 0 1234            # set the affinity of a running process




There are third-party modules for both Perl (Sys::CpuAffinity) and Python (affinity) to set a process's affinity. Both of these work on both Linux and Windows (Windows may require other third-party modules with Sys::CpuAffinity); Sys::CpuAffinity also works on several other unix variants.

If you want to set a process's affinity from the time of its birth, set the current process's affinity immediately before calling execve. Here's a trivial wrapper that forces a process to execute on CPU 0.

#!/usr/bin/env perl
use POSIX;
use Sys::CPUAffinity;
Sys::CpuAffinity::setAffinity(getpid(), [0]);
exec $ARGV[0] @ARGV

---

#### 152. Use shared libraries in /usr/local/lib

**问题描述 / Problem Description**:
Tags: ubuntu, libraries | Score: 102 | Views: 219636 | Answers: 3

**解决方案 / Solution**:
For the current session you can


export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib


or to make the change permanent you can add /usr/local/lib to /etc/ld.so.conf (or something it includes) and run ldconfig as root.

If you're still having problems, running ldd [executable name] will show you the libraries it's trying to find, and which ones can't be found.

---

#### 153. What is the meaning of 0.0.0.0 as a gateway?

**问题描述 / Problem Description**:
Tags: linux, networking, routing | Score: 101 | Views: 205460 | Answers: 4

**解决方案 / Solution**:
0.0.0.0 has the specific meaning &quot;unspecified&quot;.  This roughly translates to &quot;there is none&quot; in the context of a gateway.  Of course, this assumes that the network is locally connected, as there is no intermediate hop.  The machine will send the packet out that interface as though to a machine connected to that segment, which in Ethernet means the MAC address of the destination host will be used instead of the MAC address of the next hop gateway.
As a destination, 0.0.0.0/0 is special: if there are no network bits, there can't be anything in the network number either.  So, it's naturally unspecified.  For prefix matching it masks off all bits, so all addresses are within 0.0.0.0/0; for this reason it's used to mean &quot;default gateway&quot; in routing tables.  It is also the least-specific possible route, so selections that prioritize specificity will choose anything else available and match 0.0.0.0/0 as a last resort.
However, sticking to your question, yes, it does have a special meaning.  It means that the network is locally connected on that interface and no more hops are needed to get to it.

---

#### 154. How to configure systemd-resolved and systemd-networkd to use local DNS server for resolving local domains and remote DNS server for remote domains?

**问题描述 / Problem Description**:
Tags: linux, systemd, dns, systemd-networkd, systemd-resolved | Score: 100 | Views: 292954 | Answers: 4

**解决方案 / Solution**:
In the configuration file for local network interface (a file matching the name pattern /etc/systemd/network/*.network) we have to either specify we want to obtain local DNS server address from DHCP server using DHCP= option:

[Network]
DHCP=yes


or specify its address explicitly using DNS= option:

[Network]
DNS=10.0.0.1


In addition we need to specify (in the same section) local domains using Domains= option

Domains=domainA.example domainB.example ~example


We specify local domains domainA.example domainB.example to get the following behavior (from systemd-resolved.service, systemd-resolved man page):


  Lookups for a hostname ending in one of the per-interface domains are
  exclusively routed to the matching interfaces.


This way hostX.domainA.example will be resolved exclusively by our local DNS server.

We specify with ~example that all domains ending in example are to be treated as route-only domains to get the following behavior (from description of this commit) :


  DNS servers which have route-only domains should only be used for the
  specified domains.


This way hostY.on.the.internet will be resolved exclusively by our global, remote DNS server.

Note

Ideally, when using DHCP protocol, local domain names should be obtained from DHCP server instead of being specified explicitly in configuration file of network interface above. See UseDomains= option. However there are still outstanding issues with this feature – see systemd-networkd DHCP search domains option issue.

We need to specify remote DNS server as our global, system-wide DNS server. We can do this in /etc/systemd/resolved.conf file: 

[Resolve]
DNS=8.8.8.8 8.8.4.4 2001:4860:4860::8888 2001:4860:4860::8844


Don't forget to reload configuration and to restart services:

$ sudo systemctl daemon-reload
$ sudo systemctl restart systemd-networkd
$ sudo systemctl restart systemd-resolved


Caution! 

Above guarantees apply only when names are being resolved by systemd-resolved – see man page for nss-resolve, libnss_resolve.so.2 and man page for systemd-resolved.service, systemd-resolved.

See also: 


Description of routing lookup requests in systemd related man pages is unclear 
How to troubleshoot DNS with systemd-resolved?   


References:


Man page for systemd-resolved.service, systemd-resolved
Man page for resolved.conf, resolved.conf.d
Man page for systemd-network

---

#### 155. How to run a script with systemd right before shutdown?

**问题描述 / Problem Description**:
Tags: linux, shutdown, systemd | Score: 99 | Views: 179623 | Answers: 5

**解决方案 / Solution**:
The suggested solution is to run the service unit as a normal service - have a look at the [Install] section. So everything has to be thought reverse, dependencies too. Because the shutdown order is the reverse startup order. That's why the script has to be placed in ExecStop=.

The following solution is working for me:

[Unit]
Description=...

[Service]
Type=oneshot
RemainAfterExit=true
ExecStop=&lt;your script/program&gt;

[Install]
WantedBy=multi-user.target


RemainAfterExit=true is needed when you don't have an ExecStart action.

After creating the file, make sure to systemctl daemon-reload and systemctl enable yourservice --now.

I just got it from systemd IRC, credits are going to mezcalero.

---

#### 156. What does the letter &#39;u&#39; mean in /dev/urandom?

**问题描述 / Problem Description**:
Tags: linux, devices, history, random | Score: 98 | Views: 16971 | Answers: 3

**解决方案 / Solution**:
Unlimited.

In Linux, comparing the kernel functions named random_read and random_read_unlimited
 indicates that the etymology of the letter u in urandom isunlimited. 

This is confirmed by line 114:


  The /dev/urandom device does not have this limit [...]


Update:

Regarding which came first for Linux, /dev/random or /dev/urandom, @Stéphane Chazelas gave the post with the original patch and @StephenKitt showed they were both introduced simultaneously.

---

#### 157. Why is the root directory denoted by a / sign?

**问题描述 / Problem Description**:
Tags: linux, directory-structure, history | Score: 97 | Views: 23188 | Answers: 3

**解决方案 / Solution**:
The forward slash / is the delimiting character which separates directories in paths in Unix-like operating systems. This character seems to have been chosen sometime in the 1970's, and according to anecdotal sources, the reasons might be related to that the predecessor to Unix, the Multics operating system, used the &gt; character as path separator, but the designers of Unix had already reserved the characters &gt; and &lt; to signify I/O redirection on the shell command line well before they had a multi-level file system. So when the time came to design the filesystem, they had to find another character to signify pathname element separation.

A thing to note here is that in the Lear-Siegler ADM-3A terminal in common use during the 1970's, from which amongst other things the practice of using the ~ character to represent the home directory originates, the / key is next to the > key:



As for why the root directory is denoted by a single /, it is a convention most likely influenced by the fact that the root directory is the top-level directory of the directory hierarchy, and while other directories may be beneath it, there usually isn't a reason to refer to anything outside the root directory. Similarly the directory entry itself has no name, because it's the boundary of the visible directory tree.

---

#### 158. How to remove all the files in a directory?

**问题描述 / Problem Description**:
Tags: linux, directory, rm, recursive | Score: 97 | Views: 531269 | Answers: 14

**解决方案 / Solution**:
If your top-level directory is called images, then run rm -r images/*. This uses the shell glob operator * to run rm -r on every file or directory within images.

---

#### 159. What is the difference between kernel drivers and kernel modules?

**问题描述 / Problem Description**:
Tags: linux, kernel, kernel-modules, drivers | Score: 97 | Views: 108519 | Answers: 6

**解决方案 / Solution**:
A kernel module is a bit of compiled code that can be inserted into the kernel at run-time, such as with insmod or modprobe.

A driver is a bit of code that runs in the kernel to talk to some hardware device. It "drives" the hardware. Most every bit of hardware in your computer has an associated driver.¹ A large part of a running kernel is driver code.²

A driver may be built statically into the kernel file on disk.³ A driver may also be built as a kernel module so that it can be dynamically loaded later. (And then maybe unloaded.)

Standard practice is to build drivers as kernel modules where possible, rather than link them statically to the kernel, since that gives more flexibility. There are good reasons not to, however:


Sometimes a given driver is absolutely necessary to help the system boot up. That doesn't happen as often as you might imagine, due to the initrd feature.
Statically built drivers may be exactly what you want in a system that is statically scoped, such as an embedded system. That is to say, if you know in advance exactly which drivers will always be needed and that this will never change, you have a good reason not to bother with dynamic kernel modules.
If you build your kernel statically and disable Linux's dynamic module loading feature, you prevent run-time modification of the kernel code. This provides additional security and stability at the expense of flexibility.


Not all kernel modules are drivers. For example, a relatively recent feature in the Linux kernel is that you can load a different process scheduler. Another example is that the more complex types of hardware often have multiple generic layers that sit between the low-level hardware driver and userland, such as the USB HID driver, which implements a particular element of the USB stack, independent of the underlying hardware.



Asides:


One exception to this broad statement is the CPU chip, which has no "driver" per se. Your computer may also contain hardware for which you have no driver.
The rest of the code in an OS kernel provides generic services like memory management, IPC, scheduling, etc. These services may primarily serve userland applications, as with the examples linked previously, or they may be internal services used by drivers or other intra-kernel infrastructure.
The one in /boot, loaded into RAM at boot time by the boot loader early in the boot process.

---

#### 160. How to display the Linux kernel command line parameters given for the current boot?

**问题描述 / Problem Description**:
Tags: linux, linux-kernel | Score: 96 | Views: 135219 | Answers: 2

**解决方案 / Solution**:
$ cat /proc/cmdline
root=/dev/xvda xencons=tty console=tty1 console=hvc0 nosep nodevfs ramdisk_size=32768 ip_conntrack.hashsize=8192 nf_conntrack.hashsize=8192 ro  devtmpfs.mount=1 
$

---

#### 161. Ubuntu update error: &quot;waiting for unattended-upgr to exit&quot;

**问题描述 / Problem Description**:
Tags: ubuntu, upgrade | Score: 96 | Views: 281007 | Answers: 8

**解决方案 / Solution**:
I would first try a softer way.

Stop the automatic updater:
 sudo dpkg-reconfigure -plow unattended-upgrades



At the first prompt, choose not to download and install updates.
Make a reboot.

Make sure any packages in an unclean state are installed correctly:
 sudo dpkg --configure -a


Get your system up-to-date:
 sudo apt update &amp;&amp; sudo apt -f install &amp;&amp; sudo apt full-upgrade


Turn the automatic updater back on, now that the blockage is cleared:
 sudo dpkg-reconfigure -plow unattended-upgrades

Select the package unattended-upgrades again.

---

#### 162. Create and format exFAT partition from Linux

**问题描述 / Problem Description**:
Tags: linux, filesystems | Score: 95 | Views: 291254 | Answers: 11

**解决方案 / Solution**:
Yes, there is a project implementing exfat and the related utilities at relan/exfat.
To format a partition, use mkexfatfs / mkfs.exfat like with most filesystems, e.g.:
mkfs.exfat /dev/sdX1

As for creating the partition in the first place, this is the same as for any other filesystem. Create a partition in your favourite partition manager. If you have an MBR partition table, set the partition type to NTFS (that is, code 7).
Newer fdisk versions identify the partition type as &quot;Microsoft basic data&quot; (EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, code 11.
Note, that some distributions only package the fuse module, so you may have to build it yourself.

---

#### 163. What is the purpose of -e in sed command?

**问题描述 / Problem Description**:
Tags: linux, shell, text, sed, command | Score: 95 | Views: 155535 | Answers: 4

**解决方案 / Solution**:
From the man page:

-e script, --expression=script

    add the script to the commands to be executed


So you can use multiple -e options to build up a script out of many parts.

$ sed -e "s/foo/bar/" -e "/FOO/d"


Would first replace foo with bar and then delete every line containing FOO.

---

#### 164. What is the difference between procfs and sysfs?

**问题描述 / Problem Description**:
Tags: linux, filesystems, proc, sysfs | Score: 94 | Views: 55877 | Answers: 4

**解决方案 / Solution**:
In the beginning (way back in Unix), the way that programs found out about the running processes on the system was via directly reading process structures from the kernel memory (opening /dev/mem, and interpreting the raw data directly).  This is how the very first 'ps' commands worked.  Over time, some information was made available via system calls.

However, it is bad form to expose system data directly to user-space via /dev/mem, and obnoxious to be constantly creating new system calls every time you wanted to export some new piece of process data, and so a newer method was created to access structured data for user-space applications to find out about process attributes.  This was the /proc filesystem.  With /proc, the interfaces and structures (directories and files) could be kept the same, even as the underlying data structures in the kernel changed.  This was much less fragile than the earlier system, and it scaled better.

The /proc filesystem was originally designed to publish process information and a few key system attributes, required by 'ps', 'top', 'free' and a few other system utilities.  However, because it was easy to use (both from the kernel side and the user-space side), it became a dumping ground for a whole range of system information.  Also, it started to gain read/write files, to be used to adjust settings and control the operation of the kernel or its various subsystems.  However, the methodology of implementing control interfaces was ad-hoc, and /proc soon grew into a tangled mess.

The sysfs (or /sys filesystem) was designed to add structure to this mess and provide a uniform way to expose system information and control points (settable system and driver attributes) to user-space from the kernel.  Now, the driver framework in the kernel automatically creates directories under /sys when drivers are registered, based on the driver type and the values in their data structures.  This means that drivers of a particular type will all have the same elements exposed via sysfs.

Many of the legacy system information and control points are still accessible in /proc, but all new busses and drivers should expose their info and control points via sysfs.

---

#### 165. Are threads implemented as processes on Linux?

**问题描述 / Problem Description**:
Tags: linux, linux-kernel, process, c, thread | Score: 94 | Views: 39778 | Answers: 7

**解决方案 / Solution**:
I think this part of the clone(2) man page may clear up the difference re. the PID:


  CLONE_THREAD (since Linux 2.4.0-test8)
                If CLONE_THREAD is set, the child is placed in the same thread
                group as the calling process.
  Thread groups were a feature added in Linux 2.4 to support the
                POSIX threads notion of a set of threads that share a single
                PID.  Internally, this shared PID is the so-called thread
                group identifier (TGID) for the thread group.  Since Linux
                2.4, calls to getpid(2) return the TGID of the caller.


The "threads are implemented as processes" phrase refers to the issue of threads having had separate PIDs in the past. Basically, Linux originally didn't have threads within a process, just separate processes (with separate PIDs) that might have had some shared resources, like virtual memory or file descriptors. CLONE_THREAD and the separation of process ID(*) and thread ID make the Linux behaviour look more like other systems and more like the POSIX requirements in this sense. Though technically the OS still doesn't have separate implementations for threads and processes.  

Signal handling was another problematic area with the old implementation, this is described in more detail in the paper @FooF refers to in their answer. 

As noted in the comments, Linux 2.4 was also released in 2001, the same year as the book, so it's not surprising the news didn't get to that print.

---

#### 166. Linux network troubleshooting and debugging

**问题描述 / Problem Description**:
Tags: linux, networking, debugging, troubleshooting | Score: 93 | Views: 141934 | Answers: 3

**解决方案 / Solution**:
I think, general principles of network troubleshooting are:

Find out at what level of the TCP/IP stack (or some other stack) the problem occurs.
Understand what the correct system behavior is and what the deviation from the normal system state is.
Try to express the problem in one sentence or in several words.
Using obtained information from the buggy system, your own experience, and experience of other people (Google, various forums, etc.), try to solve the problem until success (or failure).
If you fail, ask other people about help or some advice.

As for me, I usually obtain all required information using all needed tools, and try to match this information to my experience. Deciding what level of the network stack contains the bug helps to cut off unlikely variants. Using experience of other people helps to solve the problems quickly, but often it leads to a situation, where I can solve some problem without its understanding and if this problem occurs again, it's impossible for me to tackle it again without the Internet.
And in general, I don't know how I solve network problems. It seems that there is some magic function in my brain named SolveNetworkProblem(information_about_system_state, my_experience, people_experience), which could sometimes return exactly the right answer, and also could sometimes fail (like here TCP dies on a Linux laptop).
I usually use utils from this set for network debugging:

ifconfig (or ip link, ip addr) - for obtaining information about network interfaces
ping - for validating if the target host is accessible from my machine. ping could also be used for basic DNS diagnostics - we could ping a host by its IP address or by its hostname and then decide if DNS works at all. And then traceroute or tracepath or mtr to look what's going on on the way there.
dig - diagnose everything DNS
dmesg | less or dmesg | tail or dmesg | grep -i error - for understanding what the Linux kernel thinks about some trouble.
netstat -antp + | grep smth - my most popular usage of the netstat command, which shows information about TCP connections. Often I perform some filtering using grep. See also the new ss command (from iproute2 the new standard suite of Linux networking tools) and lsof as in lsof -ai tcp -c some-cmd.
telnet &lt;host&gt; &lt;port&gt; - is very useful for communicating with various TCP services (e.g. on SMTP, HTTP protocols), also we could check general opportunity to connect to some TCP port.
iptables-save (on Linux) - to dump the full iptables tables
ethtool - get all the network interface card parameters (status of the link, speed, offload parameters...)
socat - the Swiss army tool to test all network protocols (UDP, multicast, SCTP...). Especially useful (more so than telnet) with a few -d options.
iperf - to test bandwidth availability
openssl (s_client, ocsp, x509...) to debug all SSL/TLS/PKI issues.
wireshark - the powerful tool for capturing and analyzing network traffic, which allows you to analyze and catch many network bugs.
iftop - show big users on the network/router.
iptstate (on Linux) - current view of the firewall's connection tracking.
arp (or the new ip neigh in Linux) - show the ARP table status.
route or the newer (on Linux) ip route - show the routing table status.
strace (or truss, dtrace or tusc depending on the system) - is a useful tool that shows which system calls the problematic process performs. It also shows error codes (errno) when system calls fail. This information often says enough for understanding the system behavior and solving a problem. Alternatively, using breakpoints on some networking functions in gdb can let you find out when they are made and with which arguments.
to investigate firewall issues on Linux: iptables -nvL shows how many packets are matched by each rule (iptables -Z to zero the counters). The LOG target inserted in the firewall chains is useful to see which packets reach them and how they have already been transformed when they get there. To get further, NFLOG (associated with ulogd) will log the full packet.

---

#### 167. What&#39;s the difference between pkill and killall?

**问题描述 / Problem Description**:
Tags: linux, process, kill, process-management | Score: 91 | Views: 47958 | Answers: 5

**解决方案 / Solution**:
The pgrep and pkill utilities were introduced in Sun's Solaris 7 and, as g33klord noted, they take a pattern as argument which is matched against the names of running processes. While pgrep merely prints a list of matching processes, pkill will send the specified signal (or SIGTERM by default) to the processes. The common options and semantics between pgrep and pkill comes in handy when you want to be careful and first review the list matching processes with pgrep, then proceed to kill them with pkill. pgrep and pkill are provided by the the procps package, which also provides other /proc file system utilities, such as ps, top, free, uptime among others.

The killall command is provided by the psmisc package, and differs from pkill in that, by default, it matches the argument name exactly (up to the first 15 characters) when determining the processes signals will be sent to. The -e, --exact option can be specified to also require exact matches for names longer than 15 characters. This makes killall somewhat safer to use compared to pkill. If the specified argument contains slash (/) characters, the argument is interpreted as a file name and processes running that particular file will be selected as signal recipients. killall also supports regular expression matching of process names, via the -r, --regexp option.

There are other differences as well. The killall command for instance has options for matching processes by age (-o, --older-than and -y, --younger-than), while pkill can be told to only kill processes on a specific terminal (via the -t option). Clearly then, the two commands have specific niches.

Note that the killall command on systems descendant from Unix System V (notably Sun's Solaris, IBM's AIX and HP's HP-UX) kills all processes killable by a particular user, effectively shutting down the system if run by root.

The Linux psmisc utilities have been ported to BSD (and in extension Mac OS X), hence killall there follows the "kill processes by name" semantics.

---

#### 168. keyserver timed out when trying to add a GPG public key

**问题描述 / Problem Description**:
Tags: bash, ubuntu, gpg | Score: 91 | Views: 218082 | Answers: 9

**解决方案 / Solution**:
This is usually caused by your firewall blocking the port 11371. You could unblock the port in your firewall. In case you don't have access to the firewall you could:
Force it to use port 80 instead of 11371
$ sudo gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 94558F59

-or alternatively omitting the port-
$ sudo gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 94558F59

Alternatively

Find and open the key from the key server.
Copy it's contents into a text file.
Go to System Tool &gt; Preferences &gt; Software Sources &gt; Authentication &gt; Add key, and select the text file created. Ubuntu 14.04 and later try: Software Center -&gt; Edit -&gt; Software Sources -&gt; Authentication -&gt; Import key file

---

#### 169. How to disable `apt-daily.service` on Ubuntu cloud VM image?

**问题描述 / Problem Description**:
Tags: ubuntu, systemd, cloud-init | Score: 91 | Views: 108751 | Answers: 9

**解决方案 / Solution**:
Yes, there was something obvious that I was missing.

Systemd is all about concurrent start of services, so the cloud-init script is
run at the same time the apt-daily.service is triggered. By the time
cloud-init gets to execute the user-specified payload, apt-get update is
already running. So the attempts 2. and 3. failed not because of some namespace
magic, but because they altered the system too late for apt.systemd.daily to
pick the changes up.

This also means that there is basically no way of preventing
apt.systemd.daily from running -- one can only kill it after it's started.

This "user data" script takes this route::

#!/bin/bash

systemctl stop apt-daily.service
systemctl kill --kill-who=all apt-daily.service

# wait until `apt-get updated` has been killed
while ! (systemctl list-units --all apt-daily.service | egrep -q '(dead|failed)')
do
  sleep 1;
done

# now proceed with own APT tasks
apt install -y python


There is still a time window during which SSH logins are possible yet apt-get
will not run, but I cannot imagine another solution that can works on the stock
Ubuntu 16.04 cloud image.

---

#### 170. How do I shorten the current directory path shown on terminal?

**问题描述 / Problem Description**:
Tags: linux, files, terminal, directory | Score: 90 | Views: 151197 | Answers: 10

**解决方案 / Solution**:
Since bash 4, to shorten the depth of directory in command-line is done by using PROMPT_DIRTRIM in the .bashrc file. Just remember to reopen your terminal.
PROMPT_DIRTRIM=1

See the Bash Manual for more information.
Example
bob@bob-ubuntu:~/Desktop/Dropbox/School/2017/C/A3/$
will be trimmed to
bob@bob-ubuntu:.../A3/$

---

#### 171. Allowing a regular user to listen to a port below 1024

**问题描述 / Problem Description**:
Tags: linux, networking, tcp, privileges, authbind | Score: 90 | Views: 172726 | Answers: 7

**解决方案 / Solution**:
setcap 'cap_net_bind_service=+ep' /path/to/program

this will work for specific processes. But to allow a particular user to bind to ports below 1024 you will have to add him to sudoers. 

Have a look at this discussion for more.

---

#### 172. How to list the open file descriptors (and the files they refer to) in my current bash session

**问题描述 / Problem Description**:
Tags: linux, bash, file-descriptors, open-files | Score: 90 | Views: 256830 | Answers: 5

**解决方案 / Solution**:
Yes, this will list all open file descriptors:
$ ls -l /proc/$$/fd
total 0
lrwx------ 1 isaac isaac 64 Dec 28 00:56 0 -&gt; /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 1 -&gt; /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 2 -&gt; /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 255 -&gt; /dev/pts/6
l-wx------ 1 isaac isaac 64 Dec 28 00:56 4 -&gt; /home/isaac/testfile.txt

Of course, as usual: 0 is stdin, 1 is stdout and 2 is stderr.
The 4th is an open file (to write) in this case.

---

#### 173. show gateway IP address when performing ifconfig command

**问题描述 / Problem Description**:
Tags: linux, ip | Score: 90 | Views: 285897 | Answers: 4

**解决方案 / Solution**:
You can with the ip command, and given that ifconfig is in the process of being deprecated by most distributions it's now the preferred tool.  An example:

$ ip route show
212.13.197.0/28 dev eth0  proto kernel  scope link  src 212.13.197.13
default via 212.13.197.1 dev eth0

---

#### 174. Shell: how to go to the beginning of line when you are inside a screen?

**问题描述 / Problem Description**:
Tags: linux, gnu-screen, keyboard-shortcuts | Score: 90 | Views: 99378 | Answers: 3

**解决方案 / Solution**:
Use Ctrl-a a, or change screen's escape keystroke (option -e).

---

#### 175. What does adduser do that useradd doesn&#39;t?

**问题描述 / Problem Description**:
Tags: debian, ubuntu, users, useradd | Score: 90 | Views: 79330 | Answers: 4

**解决方案 / Solution**:
First off, the respective man page snippets highlight the differences between the two commands and give some indication of what is going on. For adduser:

adduser  and  addgroup add users and groups to the system according to command line options and configuration information in /etc/adduser.conf.  They are friendlier front ends to
the low level tools like useradd, groupadd and usermod programs, by default choosing Debian policy conformant UID and GID values, creating a home directory with skeletal configuration, running a custom script, and other features.

Then for useradd:

useradd is a low level utility for adding users. On Debian, administrators should usually use adduser(8) instead.

Further investigation of adduser reveals that it is a perl script providing a high level interface to, and thus offering some of the functionality of, the following commands:

useradd
groupadd
passwd - used to add/change users passwords.
gpasswd - used to add/change group passwords.
usermod - used to change various user associated parameters.
chfn - used to add/change additional information held on a user.
chage - used to change password expiry information.
edquota - used to change disk usage quotas.

A basic run of the adduser command is as follows:
adduser username

This simple command will do a number of things:

Create the user named username.
Create the user's home directory (default is /home/username and copy the files from /etc/skel into it.
Create a group with the same name as the user and place the user in it.
Prompt for a password for the user.
Prompt for additional information on the user.

The useradd program can most of accomplish most of this, however it does not do so by default and needs additional options. Some of the information requires more commands:
useradd -m -U username
passwd username
chfn username

Note that adduser ensures that created UIDs and GIDs conform with the Debian policy. Creating normal users with useradd seems to be ok, provided UID_MIN/UID_MAX in /etc/login.defs matches the Debian policy. What is a problem though is that Debian specifies a particular range for system user UIDs which only seems to be supported in /etc/adduser.conf, so naively adding a system user with useradd and not specifying a UID/GUID in the correct range leaves the potential for serious problems.
Another common use for adduser is to simplify the process of adding a user to a group. Here, the following command:
adduser username newgroup

is equivalent to the following usermod command:
usermod -a -G newgroup username

The main drawback from usermod in this case is that forgetting to pass the
append option (i.e.: -a) would end up removing the user from all groups
before adding them to &quot;newgroup&quot; (i.e.: -G alone means &quot;replace with&quot;).
One downside to using adduser here though is that you can only specify one group at a time.

---

#### 176. How to run a script on screen lock/unlock?

**问题描述 / Problem Description**:
Tags: linux, x11, gnome | Score: 89 | Views: 56520 | Answers: 12

**解决方案 / Solution**:
Gnome-screensaver emits some signals on dbus when something happens.

Here the documentation (with some examples).

You could write a scripts that runs:

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'"


and that does what you need anytime dbus-monitor prints a line about the screen being locked/unlocked.



Here a bash command to do what you need:

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" |
  while read x; do
    case "$x" in 
      *"boolean true"*) echo SCREEN_LOCKED;;
      *"boolean false"*) echo SCREEN_UNLOCKED;;  
    esac
  done


Just replace echo SCREEN_LOCKED and echo SCREEN_UNLOCKED with what you need.

---

#### 177. Can I connect to Windows machine from Linux shell?

**问题描述 / Problem Description**:
Tags: linux, ssh, windows | Score: 89 | Views: 247106 | Answers: 8

**解决方案 / Solution**:
It depends on how you want to connect. You can create shares on the Windows machine and use smb/cifs to connect to the share.

The syntax would depend based on if you are in a domain or not.

# mount -t cifs //server/share /mnt/server --verbose -o user=UserName,dom=DOMAIN


You also have the ability to mount the $IPC and administrative shares. You can look into Inter-Process Communication for what you can do via the $IPC share.

There is always:


RDP
VNC
telnet
ssh
Linux on Windows


With the last 3 you need to install additional software.


Kpym (telnet / ssh server)
MobaSSH (ssh server)
Cygwin (run a Linux environment inside Windows)
DamnSmall Linux - inside Windows (like Cygwin run DSL inside Windows)


VNC can be run from a stand-alone binary or installed.


RealVNC
TightVNC


For RDP most Linux systems either already have rdesktop installed or it is available in the package manager. Using rdesktop you only have to enable RDP connections to your Windows system and then you will be able to use RDP for a full GUI Windows console.

---

#### 178. How to recover files I deleted now by running rm *?

**问题描述 / Problem Description**:
Tags: ubuntu, rm, data-recovery | Score: 89 | Views: 586070 | Answers: 2

**解决方案 / Solution**:
If a running program still has the deleted file open, you can recover the file through the open file descriptor in /proc/[pid]/fd/[num]. To determine if this is the case, you can attempt the following:
$ lsof | grep &quot;/path/to/file&quot;

If the above gives output of the form:
progname 5383 user 22r REG 8,1 16791251 265368 /path/to/file               

take note of the PID in the second column, and the file descriptor number in the fourth column. Using this information you can recover the file by issuing the command:
$ cp /proc/5383/fd/22 /path/to/restored/file

If you're not able to find the file with lsof, you should immediately remount the file system which housed the file read-only:
$ mount -o remount,ro /dev/[partition]

or unmount the file system altogether:
$ umount /dev/[partition]

The reason for this is that as soon as the file has been unlinked, and there are no remaining hard links to the file in question, the underlying file system may free the blocks previously allocated for the deleted file, at which point the blocks may be allocated to another file and their contents overwritten. Ceasing any further writes to the file system is therefore time critical if any recovery is to be possible. If the file system is the root file system or cannot be made read-only or unmounted for some other reason, it might be necessary to shutdown the system (if possible) and continue the recovery from a live environment where you can leave the target file system read-only.
After writes to the file system have been prevented, there is no immediate hurry to attempt the actual recovery. To play it safe, you might want to make a backup of the file system to perform the actual recovery on:
$ dd bs=4M if=/dev/[partition] of=/path/to/backup

The next steps now depend on the file system type. Assuming a typical Ubuntu installation, you most likely have a ext3 or ext4 file system. In this case, you may attempt recovery using extundelete. Recovery may be attempted safely on either the backup, or the raw device, as long as it is not mounted (or it is mounted read-only). DO NOT ATTEMPT RECOVERY FROM A LIVE FILE SYSTEM. This will most likely bring the file system to an inconsistent state.
extundelete will attempt restore any files it finds to a subdirectory of the current directory named RECOVERED_FILES. Typical usage to restore all deleted files from a backup would be:
With older versions:
$ extundelete /path/to/backup --restore-all 

With newer versions (e.g. 0.2.4), don't mount the device you're trying to recover from (thanks to Ryan Lue) :
$ extundelete /dev/&lt;device-file&gt; --restore-all

Instead of --restore-all, you can try options like --restore-file &lt;path&gt; or --restore-directory &lt;path&gt;

---

#### 179. Why can&#39;t Linux usernames begin with numbers?

**问题描述 / Problem Description**:
Tags: linux, users, history | Score: 88 | Views: 33968 | Answers: 6

**解决方案 / Solution**:
Some commands (eg chown) can accept either a username or a numeric user ID, so allowing all-numeric usernames would break that.

A rule to allow names that start with a number and contain some alpha was probably considered not worth the effort; instead there is just a requirement to start with an alpha character.

Edit:

It appears from the other responses that some distro's have subverted this limitation; in this case, according to the GNU Core Utils documentation:


  POSIX requires that these commands first attempt to resolve the specified
  string as a name, and only once that fails, then try to interpret it as
  an ID.


$ useradd 1000   # on most systems this will fail with:
                 # useradd: invalid user name '1000'
$ mkdir /home/1000
$ chown -R 1000 /home/1000   # This will first try to map
    # to username "1000", but this may easily be misinterpreted.


Adding a user named '0' would just be asking for trouble (UID 0 == root user). However, note that group/user ID arguments can be preceded by a '+' to force their interpretation as an integer.

---

#### 180. What is the correct way to view your CPU speed on Linux?

**问题描述 / Problem Description**:
Tags: linux, cpu | Score: 88 | Views: 345987 | Answers: 6

**解决方案 / Solution**:
To see the current speed of each core I do this:
watch -n.1 &quot;grep \&quot;^[c]pu MHz\&quot; /proc/cpuinfo&quot;

Notes:
This does not work on server CPUs such as the Intel Xeon series. On such machines it will show the base frequency only. To show the turbo frequency, you'll need cpupower or turbostat. See @Maxim Egorushkin's answer.
If your watch command does not work with intervals smaller than one second, modify the interval like so:
watch -n1 &quot;grep \&quot;^[c]pu MHz\&quot; /proc/cpuinfo&quot;

This displays the cpu speed of each core in real time.
By running the following command, one or more times, from another terminal one can see the speed change with the above watch command, assuming SpeedStep is enabled (Cool'n'Quiet for AMD).
echo &quot;scale=10000; 4*a(1)&quot; | bc -l &amp;

(This command uses bc to calculate pi to 10000 places.)

---

#### 181. How to determine the maximum number to pass to make -j option?

**问题描述 / Problem Description**:
Tags: linux, make, cpu, parallelism, multiprocessor | Score: 88 | Views: 118025 | Answers: 6

**解决方案 / Solution**:
nproc gives the number of CPU cores/threads available to the current process, for example 8 on a quad-core CPU supporting two-way SMT assuming no other limitations (cgroups etc.).
The number of jobs you can run in parallel with make using the -j option depends on a number of factors:

the amount of available memory
the amount of memory used by each make job
the extent to which make jobs are I/O- or CPU-bound

make -j$(nproc) is a decent place to start, but you can usually use higher values, as long as you don't exhaust your available memory and start thrashing.
For really fast builds, if you have enough memory, I recommend using a tmpfs, that way most jobs will be CPU-bound and make -j$(nproc) will work as fast as possible.
Now that high-CPU-count systems are common, and thus the amount of memory available per CPU core is typically lower than it used to be, and many builds now require a lot of memory, the equation is changing. There’s been some discussion of these issues on the Debian development mailing list, starting with this bug asking for a “new option to reduce emitted processors by system memory” in nproc and culminating in a Python script which supports specifying the amount of memory required per core. This will provide a better value for -j if you know how much memory is required. In Debian 13, Ubuntu 25.10, and later (and derivatives), this is packaged as guess-concurrency.

---

#### 182. Is it good to make a separate partition for /boot?

**问题描述 / Problem Description**:
Tags: linux, partition, system-installation | Score: 88 | Views: 73794 | Answers: 11

**解决方案 / Solution**:
This is a holdover from &quot;ye olde tymes&quot; when machines had trouble addressing large hard drives.  The idea behind the /boot partition was to make the partition always accessible to any machine that the drive was plugged into.  If the machine could get to the start of the drive (lower cylinder numbers) then it could bootstrap the system; from there the linux kernel would be able to bypass the BIOS boot restriction and work around the problem.  As modern machines have lifted that restriction, there is no longer a fixed need for /boot to be separate, unless you require additional processing of the other partitions, such as encryption or file systems that are not natively recognized by the bootloader.
Technically, you can get away with a single partition and be just fine, provided that you are not using really really old hardware (pre-1998 or so).
If you do decide to use a separate partition, just be sure to give it adequate room, say 200mb of space.  That will be more than enough for several kernel upgrades (which consume several megs each time).  If /boot starts to fill up, remove older kernels that you don't use and adjust your bootloader to recognize this fact.

---

#### 183. What is the significance of the &quot;wheel&quot; group?

**问题描述 / Problem Description**:
Tags: linux, group | Score: 88 | Views: 212071 | Answers: 2

**解决方案 / Solution**:
Rather than have to dole out individual permissions on a system, you can add users to the wheel group and they can gain access to administrator levels, simply by being in the wheel group. It's typically tied directly into sudo.

## Allows people in group wheel to run all commands
%wheel  ALL=(ALL)   ALL


Which means you can do anything on the system with sudo &lt;cmd&gt;.

Previously you needed to be in the wheel group if you wanted to have access to use certain commands, such as su.

excerpt - Wheel on Wikipedia


  Modern Unix systems use user groups to control access privileges. The
  wheel group is a special user group used on some Unix systems to
  control access to the su command, which allows a user to masquerade as
  another user (usually the super user).

---

#### 184. how to redirect output to multiple log files

**问题描述 / Problem Description**:
Tags: linux, io-redirection, tee | Score: 87 | Views: 162818 | Answers: 7

**解决方案 / Solution**:
See man tee:

NAME: tee  - read from standard input and write to standard output and files
SYNOPSIS: tee [OPTION]... [FILE]...

Accordingly – this will overwrite the files:
echo test | tee file1 file2 file3

If you want to only append to multiple files, use tee --append file1 file2 or tee -a file1 file2.

---

#### 185. top command on multi core processor

**问题描述 / Problem Description**:
Tags: linux, top, parallelism, cpu-usage | Score: 87 | Views: 323223 | Answers: 3

**解决方案 / Solution**:
I'm not entirely sure what you're asking here. Yes, top shows CPU usage as a percentage of a single CPU by default. That's why you can have percentages that are >100. On a system with 4 cores, you can see up to 400% CPU usage. 

You can change this behavior by pressing I (that's Shift + i and toggles "Irix mode") while top is running. That will cause it to show the pecentage of available CPU power being used. As explained in man top:

    1. %CPU  --  CPU Usage
       The task's share of the elapsed CPU time since the last screen
       update, expressed as a percentage of total  CPU  time.   In  a
       true  SMP environment, if 'Irix mode' is Off, top will operate
       in 'Solaris mode' where a task's cpu usage will be divided  by
       the  total  number  of  CPUs.  You toggle 'Irix/Solaris' modes
       with the 'I' interactive command.


Alternatively, you can press 1 which will show you a breakdown of CPU usage per CPU:

top - 13:12:58 up 21:11, 17 users,  load average: 0.69, 0.50, 0.43
Tasks: 248 total,   3 running, 244 sleeping,   0 stopped,   1 zombie
%Cpu0  : 33.3 us, 33.3 sy,  0.0 ni, 33.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  : 16.7 us,  0.0 sy,  0.0 ni, 83.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  : 60.0 us,  0.0 sy,  0.0 ni, 40.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   8186416 total,  6267232 used,  1919184 free,   298832 buffers
KiB Swap:  8191996 total,        0 used,  8191996 free,  2833308 cached

---

#### 186. Checking if HyperThreading is enabled or not?

**问题描述 / Problem Description**:
Tags: linux, cpu, hyperthreading | Score: 86 | Views: 234510 | Answers: 15

**解决方案 / Solution**:
I have always just used the following and looked at 'Thread(s) per core:'. 

hostname:~ # lscpu
Architecture:          x86_64
CPU(s):                24
Thread(s) per core:    2                &lt;-- here
Core(s) per socket:    6
CPU socket(s):         2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 44
Stepping:              2
CPU MHz:               1596.000
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              12288K


Note, however, this technique will fail if any logical processor has been turned off with a simple

echo 0 &gt; /sys/devices/system/cpu/cpuX/online

---

#### 187. On an Apple Keyboard under Linux, how do I make the Function keys work without the fn modifier key?

**问题描述 / Problem Description**:
Tags: linux, keyboard, keyboard-layout, apple | Score: 86 | Views: 65643 | Answers: 7

**解决方案 / Solution**:
You need to add 0 or 2 into /sys/module/hid_apple/parameters/fnmode.
i.e.:
echo 2 &gt; /sys/module/hid_apple/parameters/fnmode

There seems to be some confusion regarding what the difference between the two values might be. Quoting the Ubuntu documentation:


0 = disabled : Disable the 'fn' key. Pressing 'fn'+'F8' will behave
like you only press 'F8'
1 = fkeyslast : Function keys are used as
last key. Pressing 'F8' key will act as a special key. Pressing
'fn'+'F8' will behave like a F8.
2 = fkeysfirst : Function keys are
used as first key. Pressing 'F8' key will behave like a F8. Pressing
'fn'+'F8' will act as special key (play/pause).


Note that this also works for me on Fedora.

As several people have commented, this change is temporary. You can stick it in your login shell's RC file or into cron so that you don't have to worry about it.
You can also change your driver settings to make this change permanent, like so:
echo options hid_apple fnmode=2 | sudo tee -a /etc/modprobe.d/hid_apple.conf
sudo update-initramfs -u -k all
# reboot when convenient

credits to https://askubuntu.com/a/7553

---

#### 188. dmesg: read kernel buffer failed: Permission denied

**问题描述 / Problem Description**:
Tags: linux, debian, dmesg, sysctl | Score: 86 | Views: 163847 | Answers: 1

**解决方案 / Solution**:
So it was actually trivial, looking at the very last message from the bug report:

Re: Bug#842226: dmesg: read kernel buffer failed: Operation not permitted


Part of the changelog from the aforementioned kernel:

security,printk: Enable SECURITY_DMESG_RESTRICT, preventing non-root   users reading the kernel log by default (sysctl:
kernel.dmesg_restrict)


So the solution is simply to run once:
% sudo sysctl kernel.dmesg_restrict=0
kernel.dmesg_restrict = 0

Then your local user can start using dmesg again. This apply to any user, instead of a group which I initially assumed.
Everything is back to what I wanted:
% dmesg|wc
   1307   11745   93652

and
% cat /dev/kmsg|head|wc
     10      82     857

And to make it persists across reboots, simply save it as conf file:
$ echo kernel.dmesg_restrict = 0 | sudo tee -a /etc/sysctl.d/10-local.conf &gt;/dev/null
$ cat /etc/sysctl.d/10-local.conf 
kernel.dmesg_restrict = 0

If you are on Ubuntu, for release 20.10 onwards there is already a line to persist this setting in /etc/sysctl.d/10-kernel-hardening.conf. After changing the file, to make the changes effective the user either needs to reboot or run sudo service procps restart .

---

#### 189. rsync all files of remote machine over SSH without root user?

**问题描述 / Problem Description**:
Tags: ubuntu, ssh, backup, rsync | Score: 86 | Views: 142124 | Answers: 8

**解决方案 / Solution**:
I would recommend that you just use the root account in the first place. If you set it up like this:


Configure your sshd_config on the target machine to PermitRootLogin without-password.
Use ssh-keygen on the machine that pulls the backup to create an SSH private key (only if you don't already have an SSH key). Do not set a passphrase. Google a tutorial if you need details for this, there should be plenty.
Append the contents of /root/.ssh/id_rsa.pub of the backup machine to the /root/.ssh/authorized_keys of your target machine.
Now your backup machine has root access to your target machine, without having to use password authentication.


then the resulting setup should be pretty safe.



sudo, especially combined with NOPASSWD as recommended in the comments, has no security benefits over just using the root account. For example this suggestion:


  add the following to your /etc/sudoers file: rsyncuser ALL= NOPASSWD:/usr/bin/rsync


essentially gives rsyncuser root permissions anyway. You ask:


  @MartinvonWittich Easy to gain a full root shell because rsync executed with sudo? Walk [m]e [through] that please.


Well, simple. With the recommended configuration, rsyncuser may now run rsync as root without even being asked for a password. rsync is a very powerful tool to manipulate files, so now rsyncuser has a very powerful tool to manipulate files with root permissions. Finding a way to exploit this took me just a few minutes (tested on Ubuntu 13.04, requires dash, bash didn't work):

martin@martin ~ % sudo rsync --perms --chmod u+s /bin/dash /bin/rootdash
martin@martin ~ % rootdash
# whoami
root
# touch /etc/evil
# tail -n1 /etc/shadow
dnsmasq:*:15942:0:99999:7:::


As you can see, I have created myself a root shell; whoami identifies my account as root, I can create files in /etc, and I can read from /etc/shadow. My exploit was to set the setuid bit on the dash binary; it causes Linux to always run that binary with the permissions of the owner, in this case root.


  Having a real root is not [recommended] for good reasons. – redanimalwar 15 hours ago


No, clumsily working around the root account in situations where it is absolutely appropriate to use it is not for good reasons. This is just another form of cargo cult programming - you don't really understand the concept behind sudo vs root, you just blindly apply the belief "root is bad, sudo is good" because you've read that somewhere.

On the one hand, there are situations where sudo is definitely the right tool for the job. For example, when you're interactively working on a graphical Linux desktop, let's say Ubuntu, then having to use sudo is fine in those rare cases where you sometimes need root access. Ubuntu intentionally has a disabled root account and forces you to use sudo by default to prevent users from just always using the root account to log in. When the user just wants to use e.g. the web browser, then logging in as root would be a dangerous thing, and therefore not having a root account by default prevents stupid people from doing this.

On the other hand, there are situations like yours, where an automated script requires root permissions to something, for example to make a backup. Now using sudo to work around the root account is not only pointless, it's also dangerous: at first glance rsyncuser looks like an ordinary unprivileged account. But as I've already explained, it would be very easy for an attacker to gain full root access if he had already gained rsyncuser access. So essentially, you now have an additional root account that doesn't look like a root account at all, which is not a good thing.

---

#### 190. How to change default new window directory from within the tmux

**问题描述 / Problem Description**:
Tags: linux, tmux, gnu-screen | Score: 85 | Views: 44605 | Answers: 2

**解决方案 / Solution**:
tl;dr

Ctrl+b
:

attach -c desired/directory/path


Long Answer

Start tmux as follows:
 (cd /aaa/bbb; tmux)



Now, any new windows (or panes) you create will start in directory /aaa/bbb, regardless of the current directory of the current pane.

If you want to change the default directory once tmux is up and running,  use attach-session with -c.

Quoting from the tmux man page for attach-session:
    -c will set the session working directory (used for new windows)
    to working-directory.

For example:

Ctrl+b
:

attach -c /ddd/eee


New windows (or panes) will now start in directory /ddd/eee, regardless of the directory of the current pane.

---

#### 191. Disable screen blanking on text console

**问题描述 / Problem Description**:
Tags: linux, terminal, suse, console | Score: 84 | Views: 126042 | Answers: 11

**解决方案 / Solution**:
You can verify what timeout the kernel uses for virtual console blanking via:
$ cat /sys/module/kernel/parameters/consoleblank
600

This file is read-only and the timeout is specified in seconds. The current default seems to be 10 minutes.
You can change that value with entering the following command on a virtual console (if you are inside an xterm you have to change to a virtual console via hitting e.g. Ctrl+Alt+F1).
$ setterm -blank VALUE

Where the new VALUE is specified in minutes. A value of 0 disables blanking:
$ cat /sys/module/kernel/parameters/consoleblank
600
$ setterm -blank 0
$ cat /sys/module/kernel/parameters/consoleblank
0

setterm has other powersaving related options, the most useful combination seems to be:
$ setterm -blank 0 -powersave off

Thus to permanently/automatically disable virtual console blanking on startup you can either:

add the consoleblank=0 kernel parameter to the kernel command line (i.e. edit and update your boot loader configuration)

add the setterm -blank 0 command to an rc-local or equivalent startup script

add the setterm output to /etc/issue since /etc/issue is output on every virtual console:
# setterm -blank 0 &gt;&gt; /etc/issue


Choose one alternative from the above.

---

#### 192. How to restrict an SSH user to only allow SSH-tunneling?

**问题描述 / Problem Description**:
Tags: linux, ssh, account-restrictions | Score: 84 | Views: 77258 | Answers: 4

**解决方案 / Solution**:
On the server side, you can restrict this by setting their user shell to /bin/true. This will allow them to authenticate, but not actually run anything since they don't get a shell to run it in. This means they will be limited to whatever subset of things SSH is able to offer them. If it offers port forwarding, they will still be able to do that.

On the client side, you will probably want to connect with the -N. This stops the client from ASKING for a remote command such as a shell, it just stops after the authentication part is done. Thanks to commentors for pointhing this out.

---

#### 193. How to find power draw in watts?

**问题描述 / Problem Description**:
Tags: linux, power-management | Score: 84 | Views: 339456 | Answers: 4

**解决方案 / Solution**:
If your computer actually keeps track of power (e.g. notebook), than on kernel 3.8.11 you can use the command below. It returns power measured in microwatts.

cat /sys/class/power_supply/BAT0/power_now


This works on kernel 3.8.11 (Ubuntu Quantal mainline generic).

---

#### 194. Backspace, Tab not working in terminal (using ssh)

**问题描述 / Problem Description**:
Tags: linux, debian, terminal | Score: 82 | Views: 223761 | Answers: 12

**解决方案 / Solution**:
Beside "stty" solution, you may try the "TERM" solution.

You ssh to your Debian from some terminal (putty, solaris dterm, debain xterm, you-name-it), this termninal announce capabilities (which includes keys such as Backspace and Tab) via TERM environment variable.

So, after ssh to unix host (it doesn't depend debian it or other host) set the TERM variable according to your terminal. Consider you're using bash as shell and vt100 as terminal:

export TERM=vt100


ps: TERM should be announced via ssh automagically, but in some circumstances this magic fails.

---

#### 195. mount.nfs: access denied by server while mounting on Ubuntu machines?

**问题描述 / Problem Description**:
Tags: linux, ubuntu, mount, nfs | Score: 82 | Views: 503634 | Answers: 15

**解决方案 / Solution**:
exportfs

When you create a /etc/exports file on a server you need to make sure that you export it. Typically you'll want to run this command:

$ exportfs -a


This will export all the entries in the exports file.

showmount

The other thing I'll often do is from other machines I'll check any machine that's exporting NFS shares to the network using the showmount command.

$ showmount -e &lt;NFS server name&gt;


Example

Say for example I'm logged into scully.

$ showmount -e mulder
Export list for mulder:
/export/raid1/isos     192.168.1.0/24
/export/raid1/proj     192.168.1.0/24
/export/raid1/data     192.168.1.0/24
/export/raid1/home     192.168.1.0/24
/export/raid1/packages 192.168.1.0/24


fstab

To mount these upon boots you'd add this line to your client machines that want to consume the NFS mounts.

server:/shared/dir /opt/mounted/dir nfs rsize=8192,wsize=8192,timeo=14,intr


automounting

If you're going to be rebooting these servers then I highly suggest you look into setting up automounting (autofs) instead of adding these entries to /etc/fstab. It's a bit more work but is well worth the effort. 

Doing so will allow you to reboot the servers more independently from one another and also will only create the NFS mount when it's actually needed and/or being used. When it goes idle it will get unmounted.

References


18.2. NFS Client Configuration - CentOS 5 Deployment Guide

---

#### 196. What is a &quot;loop device&quot; when mounting?

**问题描述 / Problem Description**:
Tags: linux, grep, mount, loop-device | Score: 82 | Views: 106713 | Answers: 3

**解决方案 / Solution**:
A loop device is a pseudo (&quot;fake&quot;) device (actually just a file) that acts as a block-based device. You want to mount a file disk1.iso that will act as an entire filesystem, so you use loop.
The -o is short for --options.
And the last thing, if you want to search for &quot;-o&quot; you need to escape the '-'.
Try:
man mount | grep &quot;\-o&quot;

---

#### 197. Why and how are some shared libraries runnable, as though they are executables?

**问题描述 / Problem Description**:
Tags: linux, executable, glibc, version, shared-library | Score: 82 | Views: 36977 | Answers: 2

**解决方案 / Solution**:
That library has a main() function or equivalent entry point, and was compiled in such a way that it is useful both as an executable and as a shared object.  

Here's one suggestion about how to do this, although it does not work for me.

Here's another in an answer to a similar question on S.O, which I'll shamelessly plagiarize, tweak, and add a bit of explanation.

First, source for our example library, test.c:

#include &lt;stdio.h&gt;                  

void sayHello (char *tag) {         
    printf("%s: Hello!\n", tag);    
}                                   

int main (int argc, char *argv[]) { 
    sayHello(argv[0]);              
    return 0;                       
}                   


Compile that:

gcc -fPIC -pie -o libtest.so test.c -Wl,-E


Here, we are compiling a shared library (-fPIC), but telling the linker that it's a regular executable (-pie), and to make its symbol table exportable (-Wl,-E), such that it can be usefully linked against.

And, although file will say it's a shared object, it does work as an executable:

&gt; ./libtest.so 
./libtest.so: Hello!


Now we need to see if it can really be dynamically linked.  An example program, program.c:

#include &lt;stdio.h&gt;

extern void sayHello (char*);

int main (int argc, char *argv[]) {
    puts("Test program.");
    sayHello(argv[0]);
    return 0;
}


Using extern saves us having to create a header.  Now compile that:

gcc program.c -L. -ltest


Before we can execute it, we need to add the path of libtest.so for the dynamic loader:

export LD_LIBRARY_PATH=./


Now:

&gt; ./a.out
Test program.
./a.out: Hello!


And ldd a.out will show the linkage to libtest.so. 

Note that I doubt this is how glibc is actually compiled, since it is probably not as portable as glibc itself (see man gcc with regard to the -fPIC and -pie switches), but it demonstrates the basic mechanism.  For the real details you'd have to look at the source makefile.

---

#### 198. Changing a file&#39;s &quot;Date Created&quot; and &quot;Last Modified&quot; attributes to another file&#39;s

**问题描述 / Problem Description**:
Tags: linux, bash, files, samba | Score: 81 | Views: 381004 | Answers: 3

**解决方案 / Solution**:
You can use the touch command along with the -r switch to apply another file's attributes to a file.

NOTE: There is no such thing as creation date in Unix, there are only access, modify, and change. See this U&amp;L Q&amp;A titled: get age of given file for further details.

$ touch -r goldenfile newfile


Example

For example purposes here's a goldenfile that was created with some arbitrary timestamp.

$ touch -d 20120101 goldenfile
$ ls -l goldenfile 
-rw-rw-r--. 1 saml saml 0 Jan  1  2012 goldenfile


Now I make some new file:

$ touch newfile
$ ls -l newfile 
-rw-rw-r--. 1 saml saml 0 Mar  7 09:06 newfile


Now apply goldenfile's attributes to newfile.

$ touch -r goldenfile newfile 
$ ls -l goldenfile newfile
-rw-rw-r--. 1 saml saml 0 Jan  1  2012 newfile
-rw-rw-r--. 1 saml saml 0 Jan  1  2012 goldenfile


Now newfile has the same attributes.

Modify via Samba

I just confirmed that I'm able to do this using my Fedora 19 laptop which includes version 1.16.3-2 connected to a Thecus N12000 NAS (uses a modified version of CentOS 5.x).

I was able to touch a file as I mentioned above and it worked as I described. Your issue is likely a problem with the either the mounting options being used, which may be omitting the tracking of certain time attributes, or perhaps it's related to one of these bugs:


Bug 461505 - can't set timestamp on samba shares
Bug 693491 - Unable to set attributes/timestamps on CIFS/Samba share

---

#### 199. Correctly determining memory usage in Linux

**问题描述 / Problem Description**:
Tags: linux, memory | Score: 81 | Views: 182580 | Answers: 9

**解决方案 / Solution**:
Shamelessly copy/pasting my answer from serverfault just the other day :-)
The linux virtual memory system isn't quite so simple. You can't just add up all the RSS fields and get the value reported used by free. There are many reasons for this, but I'll hit a couple of the biggest ones.

When a process forks, both the parent and the child will show with the same RSS. However linux employs copy-on-write so that both processes are really using the same memory. Only when one of the processes modifies the memory will it actually be duplicated.
This will cause the free number to be smaller than the top RSS sum.

The RSS value doesn't include shared memory. Because shared memory isn't owned by any one process, top doesn't include it in RSS.
This will cause the free number to be larger than the top RSS sum.


There are many other reasons the numbers might not add up. This answer is just trying to make the point that memory management is very complex, and you cant just add/subtract individual values to get total memory usage.

---

#### 200. How do I find out if my wireless card supports 5 GHz?

**问题描述 / Problem Description**:
Tags: linux, wifi, 802.1x | Score: 81 | Views: 113585 | Answers: 3

**解决方案 / Solution**:
Find out the interface name, by running iwconfig

$ iwconfig
eth0      no wireless extensions.

lo        no wireless extensions.

wlan0     IEEE 802.11bgn  ESSID:"EvanCarroll"  
          Mode:Managed  Frequency:2.437 GHz  Access Point: D8:50:E6:44:B2:C8   
          Bit Rate=19.5 Mb/s   Tx-Power=15 dBm   
          Retry  long limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=61/70  Signal level=-49 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:1  Invalid misc:80   Missed beacon:0


In this case it is wlan0, then run iwlist &lt;interface&gt; freq,

$ iwlist wlan0 freq
wlan0     13 channels in total; available frequencies :
          Channel 01 : 2.412 GHz
          Channel 02 : 2.417 GHz
          Channel 03 : 2.422 GHz
          Channel 04 : 2.427 GHz
          Channel 05 : 2.432 GHz
          Channel 06 : 2.437 GHz
          Channel 07 : 2.442 GHz
          Channel 08 : 2.447 GHz
          Channel 09 : 2.452 GHz
          Channel 10 : 2.457 GHz
          Channel 11 : 2.462 GHz
          Channel 12 : 2.467 GHz
          Channel 13 : 2.472 GHz
          Current Frequency:2.437 GHz (Channel 6)


None of these channels are outside of 2.4 GHz. It does not support 5 GHz.

---

#### 201. Reply on same interface as incoming?

**问题描述 / Problem Description**:
Tags: linux, iptables, routing | Score: 81 | Views: 115256 | Answers: 4

**解决方案 / Solution**:
echo 200 isp2 &gt;&gt; /etc/iproute2/rt_tables
ip rule add from &lt;interface_IP&gt; table isp2 prio 1
ip route add default via &lt;gateway_IP&gt; dev &lt;interface&gt; table isp2

The above doesn't require any packet marking with ipfilter.  It works because the outgoing (reply) packets will have the IP address that was originally used to connect to the 2nd interface as the source (from) address on the outgoing packet.

---

#### 202. reading from serial from linux command line

**问题描述 / Problem Description**:
Tags: linux, serial-port | Score: 81 | Views: 438818 | Answers: 3

**解决方案 / Solution**:
Same as with output.  Example:

cat /dev/ttyS0


Or:

cat &lt; /dev/ttyS0


The first example is an app that opens the serial port and relays what it reads from it to its stdout (your console).  The second is the shell directing the serial port traffic to any app that you like; this particular app then just relays its stdin to its stdout.

To get better visibility into the traffic, you may prefer a hex dump:

od -x &lt; /dev/ttyS0

---

#### 203. Shebang line with `#!/usr/bin/env command --argument` fails on Linux

**问题描述 / Problem Description**:
Tags: linux, scripting, executable, env | Score: 81 | Views: 34305 | Answers: 3

**解决方案 / Solution**:
Looks like this is because Linux (unlike BSD) only passes a single argument to the shebang command (in this case env).

This has been extensively discussed on StackOverflow.

---

#### 204. How do I run 32-bit programs on a 64-bit Debian/Ubuntu?

**问题描述 / Problem Description**:
Tags: ubuntu, debian, virtual-machine, 64bit, 32bit | Score: 81 | Views: 142224 | Answers: 4

**解决方案 / Solution**:
For current releases
Current Debian and Ubuntu have multiarch support: You can mix x86_32 (i386) and x86_64 (amd64) packages on the same system in a straightforward way. This is known as multiarch support -
see Ubuntu or Debian wiki more information.
See warl0ck's answer for a simple, up-to-date answer.

For old releases
In older releases, Debian and Ubuntu ship with a number of 32-bit libraries on amd64. Install the ia32-libs  package to have a basic set of 32-bit libraries, and possibly other packages that depend on this one. Your 32-bit executables should simply run if you have all the required libraries. For development, install gcc-multilib , and again possibly other packages that depend on it such as g++-multilib. You may find binutils-multiarch  useful as well, and ia32-libs-dev on Debian. Pass the -m32 option to gcc to compile for ix86.
Note that uname -m will still show x64_64 if you're running a 64-bit kernel, regardless of what 32-bit user mode components you have installed. Schroot described below takes care of this.
Schroot
This section is a guide to installing a Debian-like distribution “inside” another Linux distribution. It is worded in terms of installing a 32-bit Ubuntu inside a 64-bit Ubuntu, but should apply with minor modifications to other situations, such as installing Debian unstable inside Debian stable or vice versa.
Introduction
The idea is to install an alternate distribution in a subtree and run from that. You can install a 32-bit system on a 64-bit system that way, or a different release of your distribution, or a testing environment with different sets of packages installed.
The chroot command and system call starts a process with a view of the filesystem that's restricted to a subtree of the directory tree. Debian and Ubuntu ship schroot, a utility that wraps around this feature to create a more usable sub-environment.
Install the schroot package  (Debian) and the debootstrap package  (Debian). Debootstrap is only needed for the installation of the alternate distribution and can be removed afterwards.
Set up schroot
This example describes how to set up a 32-bit Ubuntu 10.04LTS (lucid lynx) alternate environment. A similar setup should work with other releases of Debian and Ubuntu. Create a file /etc/schroot/chroot.d/lucid32 with the following contents:
[lucid32]
description=Ubuntu 10.04LTS 32-bit
directory=/32
type=directory
personality=linux32
users=yourusername
groups=users,admin

The line directory=/32 tells schroot where we'll put the files of the 32-bit installation. The line  username=yourusername says the user yourusername will be allowed to use the schroot. The line groups=users,admin says that users in either group will be allowed to use the schroot; you can also put a users=… directive.
Install the new distribution
Create the directory and start populating it with debootstrap. Debootstrap downloads and installs a core set of packages for the specified distribution and architecture.
mkdir /32
debootstrap --arch i386 lucid /32 http://archive.ubuntu.com/ubuntu

You almost have a working system already; what follows is minor enhancements. Schroot automatically overwrites several files in /32/etc when you run it, in particular the DNS configuration in /etc/resolv.conf and the user database in /etc/passwd and other files (this can be overridden, see the documentation). There are a few more files you may want to copy manually once and for all:
cp -p /etc/apt/apt.conf /32/etc/apt/      # for proxy settings
cp -p /etc/apt/sources.list /32/etc/apt/  # for universe, security, etc
cp -p /etc/environment /32/etc/           # for proxy and locale settings
cp -p /etc/sudoers /32/etc/               # for custom sudo settings

There won't be a file /etc/mtab or /etc/fstab in the chroot. I don't recommend using the mount command manually in the chroot, do it from outside. But do create a good-enough /etc/mtab to make commands such as df work reasonably.
ln -s /proc/mounts /32/etc/mtab

With the directory type, schroot will perform bind mounts of a number of directories, i.e. those directories will be shared with the parent installation: /proc, /dev, /home, /tmp.
Services in the chroot
As described here, a schroot is not suitable for running daemons. Programs in the schroot will be killed when you exit the schroot. Use a “plain” schroot instead of a “directory” schroot if you want it to be more permanent, and set up permanent bind mounts in /etc/fstab on the parent installation.
On Debian and Ubuntu, services start automatically on installation. To avoid this (which could disrupt the services running outside the chroot, in particular because network ports are shared), establish a policy of not running services in the chroot. Put the following script as /32/usr/sbin/policy-rc.d and make it executable (chmod a+rx /32/usr/sbin/policy-rc.d).
#!/bin/sh
## Don't start any service if running in a chroot.
## See /usr/share/doc/sysv-rc/README.policy-rc.d.gz
if [ &quot;$(stat -c %d:%i /)&quot; != &quot;$(stat -c %d:%i /proc/1/root/.)&quot; ]; then
  exit 101
fi

Populate the new system
Now we can start using the chroot. You'll want to install a few more packages at this point.
schroot -c lucid32
sudo apt-get update
apt-get install lsb-core nano
...

You may need to generate a few locales, e.g.
locale-gen en_US en_US.utf8

If the schroot is for an older release of Ubuntu such as 8.04 (hardy), note that the package ubuntu-standard pulls in an MTA. Select nullmailer instead of the default postfix (you may want your chroot to send mail but you definitely don't want it to receive any).
Going further
For more information, see the schroot manual, the schroot FAQ and the
schroot.conf manual. Schroot is part of the Debian autobuilder (buildd) project. There may be additional useful tips on the Ubuntu community page about debootstrap.
Virtual machine
If you need complete isolation of the alternate environment, use a virtual machine such as KVM (qemu-kvm ) or VirtualBox.

---

#### 205. How to bind USB device under a static name?

**问题描述 / Problem Description**:
Tags: linux, arch-linux, usb, serial-port, arduino | Score: 80 | Views: 206370 | Answers: 10

**解决方案 / Solution**:
As suggested, you can add some udev rules. I edited the /etc/udev/rules.d/10-local.rules to contain:

ACTION=="add", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="my_uart"


You can check for the variables of your device by running

udevadm info -a -p  $(udevadm info -q path -n /dev/ttyUSB0)


There is a more in depth guide you can read on http://www.reactivated.net/writing_udev_rules.html

---

#### 206. How can I reliably get the operating system&#39;s name?

**问题描述 / Problem Description**:
Tags: linux, distributions | Score: 80 | Views: 90644 | Answers: 11

**解决方案 / Solution**:
lsb_release -a is likely going to be your best option for finding this information out, and being able to do so in a consistent way. 

History of LSB

The lsb in that command stands for the project Linux Standards Base which is an umbrella project sponsored by the Linux Foundation to provide generic methods for doing basic kinds of things on various Linux distros. 

The project is voluntary and vendors can participate within the project as just a user and also as facilitators of the various specifications around different modules that help to drive standardization within the different Linux distributions.

excerpt from the charter


  The LSB workgroup has, as its core goal, to address these two
  concerns. We publish a standard that describes the minimum set of APIs
  a distribution must support, in consultation with the major
  distribution vendors. We also provide tests and tools which measure
  support for the standard, and enable application developers to target
  the common set. Finally, through our testing work, we seek to prevent
  unnecessary divergence between the distributions.


Useful links related to LSB


LSB Charter
LSB Workgroup
LSB Roadmap
LSB Mailing List (current activity is here!)
List of certified LSB products
LSB Wikipedia page


Criticisms

There are a number of problems with LSB that make it problematic for distros such as Debian. The forced usage of RPM being one. See the Wikipedia article for more on the matter.

Novell

If you search you'll possibly come across a fairly dated looking page titled: Detecting Underlying Linux Distro from Novell. This is one of the few places I"ve seen an actual list that shows several of the major distros and how you can detect what underlying one you're using.

excerpt

Novell SUSE         /etc/SUSE-release
Red Hat             /etc/redhat-release, /etc/redhat_version
Fedora              /etc/fedora-release
Slackware           /etc/slackware-release, /etc/slackware-version
Debian              /etc/debian_release, /etc/debian_version,
Mandrake            /etc/mandrake-release
Yellow dog          /etc/yellowdog-release
Sun JDS             /etc/sun-release
Solaris/Sparc       /etc/release
Gentoo              /etc/gentoo-release
UnitedLinux         /etc/UnitedLinux-release
ubuntu              /etc/lsb-release


This same page also includes a handy script which attempts to codify for the above using just vanilla uname commands, and the presence of one of the above files.

NOTE: This list is dated but you could easily drop the dated distros such as Mandrake from the list and replace them with alternatives. This type of a script might be one approach if you're attempting to support a large swath of Solaris &amp; Linux variants.

Linux Mafia

More searching will turn up the following page maintained on Linuxmafia.com, titled:  /etc/release equivalents for sundry Linux (and other Unix) distributions. This is probably the most exhaustive list to date that I've seen. You could codify this list with a case/switch statement and include it as part of your software distribution.

In fact there is a script at the bottom of that page that does exactly that. So you could simply download and use the script as 3rd party to your software distribution.

script

#!/bin/sh
# Detects which OS and if it is Linux then it will detect which Linux
# Distribution.

OS=`uname -s`
REV=`uname -r`
MACH=`uname -m`

GetVersionFromFile()
{
    VERSION=`cat $1 | tr "\n" ' ' | sed s/.*VERSION.*=\ // `
}

if [ "${OS}" = "SunOS" ] ; then
    OS=Solaris
    ARCH=`uname -p` 
    OSSTR="${OS} ${REV}(${ARCH} `uname -v`)"
elif [ "${OS}" = "AIX" ] ; then
    OSSTR="${OS} `oslevel` (`oslevel -r`)"
elif [ "${OS}" = "Linux" ] ; then
    KERNEL=`uname -r`
    if [ -f /etc/redhat-release ] ; then
        DIST='RedHat'
        PSUEDONAME=`cat /etc/redhat-release | sed s/.*\(// | sed s/\)//`
        REV=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//`
    elif [ -f /etc/SuSE-release ] ; then
        DIST=`cat /etc/SuSE-release | tr "\n" ' '| sed s/VERSION.*//`
        REV=`cat /etc/SuSE-release | tr "\n" ' ' | sed s/.*=\ //`
    elif [ -f /etc/mandrake-release ] ; then
        DIST='Mandrake'
        PSUEDONAME=`cat /etc/mandrake-release | sed s/.*\(// | sed s/\)//`
        REV=`cat /etc/mandrake-release | sed s/.*release\ // | sed s/\ .*//`
    elif [ -f /etc/debian_version ] ; then
        DIST="Debian `cat /etc/debian_version`"
        REV=""

    fi
    if [ -f /etc/UnitedLinux-release ] ; then
        DIST="${DIST}[`cat /etc/UnitedLinux-release | tr "\n" ' ' | sed s/VERSION.*//`]"
    fi

    OSSTR="${OS} ${DIST} ${REV}(${PSUEDONAME} ${KERNEL} ${MACH})"

fi

echo ${OSSTR}


NOTE: This script should look familiar, it's an up to date version of the Novell one!

Legroom script

Another method I've seen employed is to roll your own script, similar to the above Novell method but making use of LSB instead. This article titled: Generic Method to Determine Linux (or UNIX) Distribution Name, shows one such method.

# Determine OS platform
UNAME=$(uname | tr "[:upper:]" "[:lower:]")
# If Linux, try to determine specific distribution
if [ "$UNAME" == "linux" ]; then
    # If available, use LSB to identify distribution
    if [ -f /etc/lsb-release -o -d /etc/lsb-release.d ]; then
        export DISTRO=$(lsb_release -i | cut -d: -f2 | sed s/'^\t'//)
    # Otherwise, use release info file
    else
        export DISTRO=$(ls -d /etc/[A-Za-z]*[_-][rv]e[lr]* | grep -v "lsb" | cut -d'/' -f3 | cut -d'-' -f1 | cut -d'_' -f1)
    fi
fi
# For everything else (or if above failed), just use generic identifier
[ "$DISTRO" == "" ] &amp;&amp; export DISTRO=$UNAME
unset UNAME


This chunk of code could be included into a system's /etc/bashrc or some such file which would then set the environment variable $DISTRO.

gcc

Believe it or not another method is to make use of gcc. If you query the command gcc --version you'll get the distro that gcc was built for, which is invaribly the same as the system it's running on.

Fedora 14

$ gcc --version
gcc (GCC) 4.5.1 20100924 (Red Hat 4.5.1-4)
Copyright (C) 2010 Free Software Foundation, Inc.


CentOS 5.x

$ gcc --version
gcc (GCC) 4.1.2 20080704 (Red Hat 4.1.2-54)
Copyright (C) 2006 Free Software Foundation, Inc.


CentOS 6.x

$ gcc --version
gcc (GCC) 4.4.7 20120313 (Red Hat 4.4.7-3)
Copyright (C) 2010 Free Software Foundation, Inc.


Ubuntu 12.04

$ gcc --version
gcc (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
Copyright (C) 2011 Free Software Foundation, Inc.


TL;DR;

So which one should I use? I would tend to go with lsb_release -a for any Linux distributions that I would frequent (RedHat, Debian, Ubuntu, etc.). For situations where you're supporting systems that don't provide lsb_release I'd roll my own as part of the distribution of software that I'm providing, similar to one of the above scripts.

UPDATE #1: Follow-up with SuSE

In speaking with @Nils in the comments below it was determined that for whatever reason, SLES11 appeared to drop LSB from being installed by default. It was only an optional installation, which seemed counter for a package that provides this type of key feature.

So I took the opportunity to contact someone from the OpenSuSE project to get a sense of why.

excerpt of email

Hi Rob,

I hope you don't mind me contacting you directly but I found your info here: 
https://en.opensuse.org/User:Rjschwei. I participate on one of the StackExchange 
sites, Unix &amp; Linux and a question recently came up regarding the best option 
for determining the underlying OS.

http://unix.stackexchange.com/questions/92199/how-can-i-reliably-get-the-operating-systems-name/92218?noredirect=1#comment140840_92218

In my answer I suggested using lsb_release, but one of the other users mentioned 
that this command wasn't installed as part of SLES11 which kind of surprised me. 
Anyway we were looking for some way to confirm whether this was intentionally 
dropped from SLES or it was accidental.

Would you know how we could go about confirming this one way or another?

Thanks for reading this, appreciate any help and/or guidance on this.

-Sam Mingolelli
http://unix.stackexchange.com/users/7453/slm


Here's Rob's response

Hi,

On 10/01/2013 09:31 AM, Sam Mingo wrote:
- show quoted text -

lsb_release was not dropped in SLES 11. SLES 11 is LSB certified. However, it 
is not installed by default, which is consistent with pretty much every other
distribution. The lsb_release command is part of the lsb-release package.

At present almost every distribution has an entry in /etc such as 
/etc/SuSE-release for SLES and openSUSE. Since this is difficult for ISVs and 
others there is a standardization effort going on driven by the convergence to 
systemd. The standard location for distribution information in the future will 
be /etc/os-release, although Ubuntu will probably do something different.

HTH,    
Robert

--  Robert Schweikert                           MAY THE SOURCE BE WITH YOU    
SUSE-IBM Software Integration Center                   LINUX    
Tech Lead    
Public Cloud Architect

---

#### 207. How to safely turn off swap permanently and reclaim the space? (on Debian Jessie)

**问题描述 / Problem Description**:
Tags: linux, debian, filesystems, partition, swap | Score: 79 | Views: 170071 | Answers: 5

**解决方案 / Solution**:
If you have GParted open, close it. Its Swapoff feature does not appear to to be permanent.

Open terminal and become root (su); if you have sudo enabled, you may also do for example sudo -i; see man sudo for all options):
 sudo -i


Turn off the particular swap partition and / or all of the swaps:
 swapoff --all


Make 100% sure the particular swap partition partition is off:
 cat /proc/swaps


Open a text editor you are skilled in with this file, e.g. nano if unsure:
 nano /etc/fstab


Comment out / remove the swap partition's UUID, e.g.:
 # UUID=1d3c29bb-d730-4ad0-a659-45b25f60c37d    none    swap    sw    0    0


Open a text editor you are skilled in with this file, e.g. nano if unsure:
 nano /etc/initramfs-tools/conf.d/resume


Comment out / remove the previously identified swap partition's UUID, e.g.:
 # RESUME=UUID=1d3c29bb-d730-4ad0-a659-45b25f60c37d


If your swap is encrypted, do the same with /etc/crypttab.

Don't close the terminal as you will need it later anyway.


Note: The next steps differ depending on, whether you rely on CLI or GUI.

GUI:

Open up GParted, either from menu, or more conveniently from the terminal we have opened:
 gparted


If you don't have it installed, you may do so; afterwards run the previous command again:
 apt-get install gparted


Choose your drive from top-right menu.

As the GParted reactivates the swap partition upon launch, you will have to right-click the particular swap partition and click Swapoff -&gt; This will be applied immediately.

Delete the swap partition with right click -&gt; Delete. You must apply the change now.

Resize your main / other partition with right click -&gt; Resize/Move. You must apply the change now.

Back to the terminal, let's recreate the boot images:
 update-initramfs -u -k all


Update GRUB:
 update-grub


You may reboot now if you wish to test that the machine boots up.


Encryption note: If your swap partition is encrypted, then you also need to comment out the related line in /etc/crypttab, otherwise CryptSetup will keep you waiting for 90 seconds during boot time. Thanks frank for this addition.

CLI:
I will check in VMs if my solution works, then I will share it. In the meantime, see this answer.

---

#### 208. Linux LXC vs FreeBSD jail

**问题描述 / Problem Description**:
Tags: linux, freebsd, virtualization, lxc, jails | Score: 79 | Views: 63189 | Answers: 1

**解决方案 / Solution**:
No matter the fancy name used here, both are solutions to a specific problem: A better segregation solution than classic Unix chroot. Operating system-level virtualization, containers, zones, or even "chroot with steroids" are names or commercial titles that define the same concept of userspace separation, but with different features.

Chroot was introduced on 18 March 1982, months before the release of 4.2 BSD, as a tool to test its installation and build system, but today it still has its flaws. Since the first objective of chroot was only to provide a newroot path, other aspects of system that needed to be isolated or controlled got uncovered (network, process view, I/O throughput). This is where the first containers (User-level virtualization) appeared.

Both technologies (FreeBSD Jails and LXC) make use of userspace isolation to provide another layer of security. This compartmentalization will ensure that a determined process will communicate only with other processes in the same container on the same host, and if using any network resource to achieve "outside world" communication, all will be forwarded to the assigned interface/channel that this container has.

Features

FreeBSD Jails:


Considered stable technology, since it is a feature inside FreeBSD since 4.0;
It takes the best of ZFS filesystem at the point where you could clone jails and create jail templates to easily deploy more jails. Some more ZFS madness;
Well documented, and evolving;
Hierarchical Jails allow you to create jails inside a jail (we need to go deeper!). Combine with allow.mount.zfs to achieve more power, and other variables like children.max do define max children jails.
rctl(8) will handle resource limits of jails (memory, CPU, disk, ...);
FreeBSD jails handle Linux userspace;
Network isolation with vnet, allowing each jail to have its own network stack, interfaces, addressing and routing tables;
nullfs to help linking folders to ones that are located on the real server to inside a jail;
ezjail utility to help mass deployments and management of jails;
Lots of kernel tunables (sysctl). security.jail.allow.* parameters will limit the actions of the root user of that jail.
Maybe, FreeBSD jails will extend some of the VPS project features like live migration in a near future.
There is some effort of ZFS and Docker integration running. Still experimental.
FreeBSD 12 supports bhyve inside a jail and pf inside a jail, creating further isolation to those tools
Lots of interesting tools were developed during the last years. Some of them are indexed on this blog post.
Alternatives: FreeBSD VPS project


Linux Containers (LXC):


New "in kernel" technology but being endorsed by big ones(specially Canonical);
Unprivileged containers starting from LXC 1.0, makes a big step into security inside containers;
UID and GID mapping inside containers;
Kernel namespaces, to make separation of IPC, mount, pid, network and users. These namespaces can be handled in a detached way, where a process that uses a different network namespace will not necessarily be isolated on other aspects like storage;
Control Groups (cgroups) to manage resources and grouping them. CGManager is the guy to achieve that.
Apparmor/SELinux profiles and Kernel capabilities for better enforcing Kernel features accessible by containers. Seccomp is also available on lxc containers to filter system calls. Other security aspects here.
Live migration functionality being developed. It’s really hard to say when it will be ready for production use, since docker/lxc will have to deal with userspace process pause, snapshot, migrate and consolidate - ref1, ref2. Live migration is working with basic containers(no device passthrough neither complex network services or special storage configurations).
APIs bindings to enable development in python3 and 2, lua, Go, Ruby and Haskell
Centralized "What's new" area. Pretty useful whenever you need to check if some bug was fixed or a new feature got committed. Here.
An interesting alternative could be lxd, that under the hood works with lxc but, it has some nice features like a REST api, OpenStack integration, etc.
Another interesting thing is that Ubuntu seems to be shipping zfs as the default filesystem for containers on 16.04. To keep projects aligned, lxd launched it's 2.0 version, and some of the features are zfs related.
Alternatives: OpenVZ, Docker
Docker. Note here that Docker uses namespaces, cgroups creating "per app"/"per software" isolation. Key differences here. While LXC creates containers with multiple processes, Docker reduces a container as much as possible to a single process and then manage that through Docker.
Effort on integrating Docker with SELinux and reducing capabilities inside a container to make it more secure - Docker and SELinux, Dan Walsh
What is the difference between Docker, LXD, and LXC


Docker no longer uses lxc. They now have a specific lib called runc that handles the integration with low-level Kernel namespace and cgroups features directly.

Neither technology is a security panacea, but both are pretty good ways to isolate an environment that doesn’t require Full Virtualization due to mixed operating systems infrastructure. Security will come after a lot of documentation reading and implementation of kernel tunables, MAC and isolations that those OS-Level virt offer to you.

See Also:


Hand-crafted containers
BSD Now: Everything you need to know about Jails
ezjail – Jail administration framework
A Brief History of Containers: From the 1970s to 2017
Docker Considered Harmful - Good article about the security circus around container technologies.

---

#### 209. Linux: Kill process based on arguments

**问题描述 / Problem Description**:
Tags: linux, kill | Score: 79 | Views: 38120 | Answers: 4

**解决方案 / Solution**:
pgrep/pkill take a -f flag. From the man page:

-f    The pattern is normally only matched against the process name.
      When -f is set, the full command line is used.


For example:

$ sleep 30&amp; sleep 60&amp;
[1] 8007
[2] 8008

$ pkill -f 'sleep 30'
[1]  - terminated  sleep 30

$ pgrep sleep
8008

---

#### 210. Need explanation on Resident Set Size/Virtual Size

**问题描述 / Problem Description**:
Tags: linux, process, memory | Score: 79 | Views: 104085 | Answers: 2

**解决方案 / Solution**:
RSS is how much memory this process currently has in main memory (RAM). VSZ is how much virtual memory the process has in total. This includes all types of memory, both in RAM and swapped out. These numbers can get skewed because they also include shared libraries and other types of memory. You can have five hundred instances of bash running, and the total size of their memory footprint won't be the sum of their RSS or VSZ values.

If you need to get a more detailed idea about the memory footprint of a process, you have some options. You can go through /proc/$PID/map and weed out the stuff you don't like. If it's shared libraries, the calculation could get complex depending on your needs (which I think I remember).

If you only care about the heap size of the process, you can always just parse the [heap] entry in the map file. The size the kernel has allocated for the process heap may or may not reflect the exact number of bytes the process has asked to be allocated. There are minute details, kernel internals and optimisations which can throw this off. In an ideal world, it'll be as much as your process needs, rounded up to the nearest multiple of the system page size (getconf PAGESIZE will tell you what it is — on PCs, it's probably 4,096 bytes).

If you want to see how much memory a process has allocated, one of the best ways is to forgo the kernel-side metrics. Instead, you instrument the C library's heap memory (de)allocation functions with the LD_PRELOAD mechanism. Personally, I slightly abuse valgrind to get information about this sort of thing. (Note that applying the instrumentation will require restarting the process.)

Please note, since you may also be benchmarking runtimes, that valgrind will make your programs very slightly slower (but probably within your tolerances).

---

#### 211. convert a hex string to binary and send with netcat

**问题描述 / Problem Description**:
Tags: linux, binary, netcat | Score: 78 | Views: 164954 | Answers: 4

**解决方案 / Solution**:
I used the -r and -p switches for xxd:
$ echo '0006303030304e43' | xxd -r -p | nc -l localhost 8181

Thanks to inspiration from @Gilles' answer, here's a Perl version:
$ echo '0006303030304e43' | perl -e 'print pack &quot;H*&quot;, &lt;STDIN&gt;' | nc -l localhost 8181

---

#### 212. How to allow non-superusers to mount any filesystem?

**问题描述 / Problem Description**:
Tags: linux, mount, non-root-user | Score: 78 | Views: 254454 | Answers: 8

**解决方案 / Solution**:
There are a couple approaches, some of them mostly secure, others not at all.

The insecure way

Let any use run mount, e.g., through sudo. You might as well give them root; it's the same thing. The user could mount a filesystem with a suid root copy of bash—running that instantly gives root (likely without any logging, beyond the fact that mount was run).

Alternatively, a user could mount his own filesystem on top of /etc, containing his/her own copy of /etc/shadow or /etc/sudoers, then obtain root with either su or sudo. Or possibly bind-mount (mount --bind) over one of those two files. Or a new file into /etc/sudoers.d.

Similar attacks could be pulled off over /etc/pam.d and many other places.

Remember that filesystems need not even be on a device, -o loop will mount a file which is owned (and thus modifiable) by the user.

The mostly secure way: udisks or similar

The various desktop environments have actually already built solutions to this, to allow users to mount removable media. They work by mounting in a subdirectory of /media only and by turning off set-user/group-id support via kernel options. Options here include udisks, udisks2, pmount, usbmount, 

If you must, you could write your own script to do something similar, and invoke it through sudo—but you have to be really careful writing this script to not leave root exploits. If you don't want your users to have to remember sudo, you can do something like this in a script:

#!/bin/bash
if [ $UID -ne 0 ]; then       # or `id -u`
    exec sudo -- "$0" "$@"
fi

# rest of script goes here 


The will-be-secure someday way: user namespaces

Linux namespaces are a very lightweight form of virtualization (containers, to be more specific). In particular, with user namespaces, any user on the system can create their own environment in which they are root. This would allow them to mount filesystems, except that has been explicitly blocked except for a few virtual filesystems. Eventually, FUSE filesystems will probably be allowed, but the most recent patches I could find don't cover block devices, only things like sshfs.

Further, many distro kernels have (for security reasons) defaulted to not allowing unprivileged users to use user namespaces; for example Debian has a kernel.unprivileged_userns_clone that defaults to 0. Other distros have similar settings, though often with slightly different names.

The best documentation I know of about user namespaces is an LWN article 
Namespaces in operation, part 5: User namespaces.

For now, I'd go with udisks2.

---

#### 213. Will Linux start killing my processes without asking me if memory gets short?

**问题描述 / Problem Description**:
Tags: linux, memory, kill, segmentation-fault | Score: 78 | Views: 57950 | Answers: 2

**解决方案 / Solution**:
It can.

There are two different out of memory conditions you can encounter in Linux. Which you encounter depends on the value of sysctl vm.overcommit_memory (/proc/sys/vm/overcommit_memory)

Introduction:
The kernel can perform what is called 'memory overcommit'. This is when the kernel allocates programs more memory than is really present in the system. This is done in the hopes that the programs won't actually use all the memory they allocated, as this is a quite common occurrence.

overcommit_memory = 2

When overcommit_memory is set to 2, the kernel does not perform any overcommit at all. Instead when a program is allocated memory, it is guaranteed access to have that memory. If the system does not have enough free memory to satisfy an allocation request, the kernel will just return a failure for the request. It is up to the program to gracefully handle the situation. If it does not check that the allocation succeeded when it really failed, the application will often encounter a segfault.

In the case of the segfault, you should find a line such as this in the output of dmesg:

[1962.987529] myapp[3303]: segfault at 0 ip 00400559 sp 5bc7b1b0 error 6 in myapp[400000+1000]


The at 0 means that the application tried to access an uninitialized pointer, which can be the result of a failed memory allocation call (but it is not the only way).

overcommit_memory = 0 and 1

When overcommit_memory is set to 0 or 1, overcommit is enabled, and programs are allowed to allocate more memory than is really available.

However, when a program wants to  use the memory it was allocated, but the kernel finds that it doesn't actually have enough memory to satisfy it, it needs to get some memory back.
It first tries to perform various memory cleanup tasks, such as flushing caches, but if this is not enough it will then terminate a process. This termination is performed by the OOM-Killer. The OOM-Killer looks at the system to see what programs are using what memory, how long they've been running, who's running them, and a number of other factors to determine which one gets killed.

After the process has been killed, the memory it was using is freed up, and the program which just caused the out-of-memory condition now has the memory it needs.

However, even in this mode, programs can still be denied allocation requests.
When overcommit_memory is 0, the kernel tries to take a best guess at when it should start denying allocation requests.
When it is set to 1, I'm not sure what determination it uses to determine when it should deny a request but it can deny very large requests.

You can see if the OOM-Killer is involved by looking at the output of dmesg, and finding a messages such as:

[11686.043641] Out of memory: Kill process 2603 (flasherav) score 761 or sacrifice child
[11686.043647] Killed process 2603 (flasherav) total-vm:1498536kB, anon-rss:721784kB, file-rss:4228kB

---

#### 214. How do I choose a graphics card for Linux?

**问题描述 / Problem Description**:
Tags: linux, xorg, graphics, hardware-compatibility | Score: 78 | Views: 77672 | Answers: 9

**解决方案 / Solution**:
Open source drivers are getting pretty good  these days.  I haven't had any problem with Intel or AMD hardware.

Intel
I hear the old ones are pretty bad, but my G4500HD does everything I need well.  Video acceleration could be better though.  There isn't a proprietary driver for Intel either, your only choice is open source.  The composited 3D desktop in KDE works great on my laptop which has an Intel chip.

AMD/ATi
Right now the older cards are better supported than the new ones.  If you could somehow get an x1800 or something from the same generation that would probably be the best.  The r300g driver is getting more development work than r600g.  That's not to say r600g is bad, in fact it's great!  It's just somewhat behind the driver for the older hardware.  AMD has a proprietary driver for the new hardware, but in my experience you want to avoid it; it's pretty bad.  The hardware covered by r300g isn't supported by that driver, so the open driver is your only option there.  And like the Intel chip I have, my Radeon 4850 runs the composited desktop in KDE well.

At the moment, I wouldn't recommend an HD6000 series.  The 6900s have no support at all in the open driver, and the others have basic support.  Go for an HD5000 or an HD4000.

Nvidia
They have a really good proprietary driver, but the open driver is struggling along.  It's getting better all the time, but Nvidia is doing nothing to help the developers.  At least AMD helps out a little bit for their hardware.

The advantage to having an open driver is that it will work out of the box in any distro.  If you install Fedora, everything will work including dual screen and 3D.  The proprietary ones are painful to setup.  Neither of them properly set up my dual screens.  It was easier to setup with Nvidia which isn't saying much because the AMD blob was just awful at this.  Also, anytime you update the kernel, you have to reinstall the driver.  Most distros take care of this if you install the in-repo version, but if you don't it's annoying to boot up one morning and realize you updated the kernel and now X.org doesn't work.

If you aren't planning on playing 3D games, either the Intel or AMD drivers are the best.  The AMD driver is more modern than the Intel one, it uses the Gallium3D architecture within Mesa (that's what the g stands for in r600g), but they both get the job done.

---

#### 215. Bluetooth won&#39;t turn On on Ubuntu 20.04

**问题描述 / Problem Description**:
Tags: ubuntu, drivers, bluetooth | Score: 78 | Views: 149204 | Answers: 13

**解决方案 / Solution**:
It's a bug: Bluetooth unavailable after updates - Reading Intel version information failed (-110)
Cold boot as in powering off from the PC's source button (taking electricity off the mother board) worked for me.
Just shutting down and having the motherboard LEDs on didn't work.

---

#### 216. How to read environment variables of a process

**问题描述 / Problem Description**:
Tags: linux, process, environment-variables | Score: 77 | Views: 122276 | Answers: 7

**解决方案 / Solution**:
You can read the initial environment of a process from /proc/&lt;pid&gt;/environ.

If a process changes its environment, then in order to read the environment you must have the symbol table for the process and use the ptrace system call (for example by using gdb) to read the environment from the global char **__environ variable. There isn't any other way to get the value of any variable from a running Linux process.

That's the answer. Now for some notes.

The above assumes that the process is POSIX compliant, meaning that the process manages its environment using a global variable char **__environ as specified in the Ref Spec. 

The initial environment for a process is passed to the process in a fixed-length buffer on the process's stack. (The usual mechanism that does this is linux//fs/exec.c:do_execve_common(...).) Since the size of the buffer is calculated to be no more than the size required for the initial environment, you can't add new variables without erasing existing variables or smashing the stack. So, any reasonable scheme to allow changes in a process's environment would use the heap, where memory in arbitrary sizes can be allocated and freed, which is exactly what GNU libc (glibc) does for you.

If the process uses glibc, then it is POSIX compliant, with __environ being declared in glibc//posix/environ.c Glibc initializes __environ with a pointer to memory that it mallocs from the process's heap, then copies the initial environment from the stack into this heap area. Each time the process uses the setenv function, glibc does a realloc to adjust the size of the area that __environ points to to accommodate the new value or variable. (You can download the glibc source code with git clone git://sourceware.org/git/glibc.git glibc). To really understand the mechanism you will also have to read the Hurd code in hurd//init/init.c:frob_kernel_process() (git clone git://git.sv.gnu.org/hurd/hurd.git hurd).

Now if the new process is only forked, without a subsequent exec overwriting the stack, then the argument and environment copying magic is done in linux//kernel/fork.c:do_fork(...), where the copy_process routine calls dup_task_struct that allocates the new process's stack by calling alloc_thread_info_node, which
calls setup_thread_stack (linux//include/linux/sched.h) for the new process using alloc_thread_info_node.

Finally, the POSIX __environ convention is a user-space convention. It has no connection with anything in the Linux kernel. You can write a userspace program without using glibc and without the __environ global and then manage the environment variables however you like. No one will arrest you for doing this but you will have to write your own environment management functions (setenv/getenv) and your own wrappers for sys_exec and it is likely that no one will be able to guess where you put the changes to your environment.

---

#### 217. How to create /dev/null?

**问题描述 / Problem Description**:
Tags: linux, devices | Score: 77 | Views: 50397 | Answers: 3

**解决方案 / Solution**:
mknod /dev/null c 1 3
chmod 666 /dev/null


Use these command to create /dev/null or use null(4) manpage for further help.

---

#### 218. How can I write to dmesg from command line?

**问题描述 / Problem Description**:
Tags: linux, command-line, kernel, logs, dmesg | Score: 77 | Views: 84764 | Answers: 6

**解决方案 / Solution**:
Write to /dev/kmsg (not /proc/kmsg as suggested by @Nils).  See linux/kernel/printk/printk.c devkmsg_writev for the kernel-side implementation and systemd/src/journal/journald-kmsg.c server_forward_kmsg for an example of usage.

---

#### 219. What is the equivalent of Active Directory on Linux

**问题描述 / Problem Description**:
Tags: linux, file-server | Score: 77 | Views: 170009 | Answers: 6

**解决方案 / Solution**:
You either build your own Active Directory-equivalent from Kerberos and OpenLDAP (Active Directory basically is Kerberos and LDAP, anyway) and use a tool like Puppet (or OpenLDAP itself) for something resembling policies, or you use FreeIPA as an integrated solution.

There's also a wide range of commercially supported LDAP servers for Linux, like Red Hat Directory Server. RHDS (like 389 Server, which is the free version of RHDS) has a nice Java GUI for management of the directory. It does neither Kerberos nor policies though. 

Personally, I really like the FreeIPA project and I think it has a lot of potential. A commercially supported version of FreeIPA is included in standard RHEL6 subscriptions, I believe.

That said, what your are asking about is more like a fileserver solution than an authentication solution (which is what AD is). If you want your files on all machines you log into, you have to set up an NFS server and export an NFS share from your fileserver to your network. NFSv3 has IP-range based ACL's, NFSv4 would be able to do proper authentication with Kerberos and combines nicely with the authentication options I described above.

If you have Windows boxes on your network, you will want to setup a Samba server, which can share out your files to Linux and Windows boxes alike. Samba3 can also function as an NT4 style domain controller, whereas Samba4 is able to mimic a Windows 2003 style domain controller.

---

#### 220. File system compatible with all OSes?

**问题描述 / Problem Description**:
Tags: linux, filesystems, osx, windows | Score: 77 | Views: 70250 | Answers: 5

**解决方案 / Solution**:
UDF is a candidate. It works out-of-the-box on linux >= 2.6.31, Windows >= Vista, MacOS >= 9 and on many BSDs.

Note: UDF comes in different versions, which are not equally supported on all platforms, see Wikipedia - Compatibility.

UDF can be created on Linux with the tool mkudffs from the package udftools.

---

#### 221. A tool for automatically applying RandR configuration when external display is plugged in

**问题描述 / Problem Description**:
Tags: linux, xorg, udev, xrandr | Score: 76 | Views: 75485 | Answers: 11

**解决方案 / Solution**:
Regarding a tool which can store monitor configuration profiles on a per-user and per-display basis, autorandr will do exactly that.

My laptop has an NVIDIA card, so I use the disper backend instead of xrandr. Autorandr will use disper as the backend to manage your monitors if you call it as autodisper. For the rest of this post though, I'll refer to it as autorandr for consistency.

You can save profiles with autorandr --save profile_name. Running autorandr by itself will then give you a list of profiles, and identify which one is detected as the current configuration.

For instance:

$ autorandr
laptop
syncmaster19 (detected)


You can tell it to automatically load the appropriate profile for the current configuration with autorandr --change. This command, paired with a udev rule to run it when it is hotplugged, would do what you requested.

As an added precaution I've appended --default laptop to that command, which will make it default to the laptop's display if there is no saved profile that matches the current configuration. So the full command I use to switch displays is:

autorandr --change --default laptop


Unfortunately my machine doesn't give any udev output when I hotplug my monitor. I'm using the NVIDIA proprietary drivers, so that isn't surprising. So I have bound it to the XF68Display key (Fn-F8) for now, which is almost as good.

---

#### 222. How to find all hard links to a given file?

**问题描述 / Problem Description**:
Tags: linux, hard-link | Score: 76 | Views: 70628 | Answers: 1

**解决方案 / Solution**:
If the given file is called /path/to/file and you want to find all hard links to it that exist under the current directory, then use:
find . -samefile /path/to/file 

The above was tested on GNU find.  Although -samefile is not POSIX, it is also supported by Mac OSX find and FreeBSD find.
Documentation
From GNU man find:

-samefile name
       File refers to the same inode as name.   When -L is in effect, this can include symbolic links.

Differences between find and ls
ls -l lists the number of hard links to a file or directory.  For directories, this number is larger than the number of results shown by find . -samefile.  The reason for this is explained in the GNU find manual:

A directory normally has at least two hard links: the entry named in
its parent directory, and the . entry inside of the directory. If a
directory has subdirectories, each of those also has a hard link
called .. to its parent directory.
The . and .. directory entries are not normally searched unless they
are mentioned on the find command line.

In sum, ls -l counts the . and .. directories as separate hard links but find . -samefile does not.

---

#### 223. What&#39;s the difference between poweroff and halt?

**问题描述 / Problem Description**:
Tags: linux | Score: 76 | Views: 102406 | Answers: 1

**解决方案 / Solution**:
halt terminates all processes and shuts down the cpu.
poweroff is exactly like halt, but it also turns off the unit itself (lights and everything on a PC). It sends an ACPI command to the board, then to the PSU, to cut the power.
shutdown is like poweroff, but it also runs shutdown scripts which should stop things gracefully. Examples include giving programs a chance to close files, delete their lock files and unmount drives properly.
Sources:
https://serverfault.com/questions/191537/shutdown-what-is-difference-between-power-off-and-halt
http://osdir.com/ml/os.solaris.managers.summaries/2001-10/msg00027.html
A comment by Peter White

---

#### 224. How to replace one char with another in all filenames of the current directories?

**问题描述 / Problem Description**:
Tags: linux, bash, rename | Score: 75 | Views: 155244 | Answers: 9

**解决方案 / Solution**:
In any shell, you can loop over the files whose name contains a space. Replacing the spaces with underscores is easy in bash, ksh and zsh with the ${VARIABLE//PATTERN/REPLACEMENT} construct.
for x in *&quot; &quot;*; do
  mv -- &quot;$x&quot; &quot;${x// /_}&quot;
done

On Debian, Ubuntu and derivatives, you can use the Perl rename (other distributions ship a different program as rename, and that program isn't helpful here).
rename 's/ /_/g' ./*

An obligatory zsh solution:
autoload zmv
zmv '(*)' '${1// /_}'

Or:
autoload zmv
zmv '*' '${f// /_}'

An obligatory POSIX solution:
for x in *&quot; &quot;*; do
  y=$(printf %s/ &quot;$x&quot; | tr &quot; &quot; &quot;_&quot;)
  mv -- &quot;$x&quot; &quot;${y%/}&quot;
done

---

#### 225. How to find the driver (module) associated with a device on Linux?

**问题描述 / Problem Description**:
Tags: linux, drivers, kernel-modules | Score: 75 | Views: 107405 | Answers: 4

**解决方案 / Solution**:
To get this information from sysfs for a device file, first determine the major/minor number by looking at the output of ls -l, eg
 $ ls -l /dev/sda
 brw-rw---- 1 root disk 8, 0 Apr 17 12:26 /dev/sda

The 8, 0 tells us that major number is 8 and the minor is 0. The b at the start of the listing also tells us that it is a block device. Other devices may have a c for character device at the start.
If you then look under /sys/dev, you will see there are two directories. One called block and one called char. The no-brainer here is that these are for block and character devices respectively. Each device is then accessible by its major/minor number is this directory. If there is a driver available for the device, it can be found by reading the target of the driver link in this or the device sub-directory. Eg, for my /dev/sda I can simply do:
$ readlink /sys/dev/block/8\:0/device/driver
../../../../../../../bus/scsi/drivers/sd

This shows that the sd driver is used for the device. If you are unsure if the device is a block or character device, in the shell you could simply replace this part with a *. This works just as well:
$ readlink /sys/dev/*/8\:0/device/driver
../../../../../../../bus/scsi/drivers/sd

Block devices can also be accessed directly through their name via either /sys/block or /sys/class/block. Eg:
$ readlink /sys/block/sda/device/driver
../../../../../../../bus/scsi/drivers/sd

Note that the existence of various directories in /sys may change depending on the kernel configuration. Also not all devices have a device subfolder. For example, this is the case for partition device files like /dev/sda1. Here you have to access the device for the whole disk (unfortunately there are no sys links for this).
A final thing which can be useful to do is to list the drivers for all devices for which they are available. For this you can use globs to select all the directories in which the driver links are present. Eg:
$ ls -l /sys/dev/*/*/device/driver &amp;&amp; ls -l /sys/dev/*/*/driver 
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/block/11:0/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:0/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:16/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:32/device/driver -&gt; ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:0/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:1024/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:128/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:256/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:384/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:512/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:513/driver -&gt; ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:514/driver -&gt; ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:640/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:643/driver -&gt; ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:768/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:896/driver -&gt; ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:0/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:1/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/char/21:2/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:3/device/driver -&gt; ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:0/device/driver -&gt; ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:1/device/driver -&gt; ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:2/device/driver -&gt; ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:0/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:1/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/char/252:2/device/driver -&gt; ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:3/device/driver -&gt; ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/254:0/device/driver -&gt; ../../../bus/pnp/drivers/rtc_cmos
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/29:0/device/driver -&gt; ../../../bus/platform/drivers/simple-framebuffer
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:64/device/driver -&gt; ../../../bus/pnp/drivers/serial
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:65/device/driver -&gt; ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:66/device/driver -&gt; ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:67/device/driver -&gt; ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/6:0/device/driver -&gt; ../../../bus/pnp/drivers/parport_pc
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/99:0/device/driver -&gt; ../../../bus/pnp/drivers/parport_pc

Finally, to diverge from the question a bit, I will add another /sys glob trick to get a much broader perspective on which drivers are being used by which devices (though not necessarily those with a device file):
find /sys/bus/*/drivers/* -maxdepth 1 -lname '*devices*' -ls

Update
Looking more closely at the output of udevadm, it appears to work by finding the canonical /sys directory (as you would get if you dereferenced the major/minor directories above), then working its way up the directory tree, printing out any information that it finds. This way you get information about parent devices and any drivers they use as well.
To experiment with this I wrote the script below to walk up the directory tree and display information at each relevant level. udev seems to look for readable files at each level, with their names and contents being incorporated in ATTRS. Instead of doing this I display the contents of the uevent files at each level (seemingly the presence of this defines a distinct level rather than just a subdirectory). I also show the basename of any subsystem links I find and this showing how the device fits in this hierarchy. udevadm does not display the same information, so this is a nice complementary tool. The parent device information (eg PCI information) is also useful if you want to match the output of other tools like lshw to higher level devices.
#!/bin/bash

dev=$(readlink -m $1)

# test for block/character device
if [ -b &quot;$dev&quot; ]; then
  mode=block
elif [ -c &quot;$dev&quot; ]; then
  mode=char
else
  echo &quot;$dev is not a device file&quot; &gt;&amp;2
  exit 1
fi

# stat outputs major/minor in hex, convert to decimal
data=( $(stat -c '%t %T' $dev) ) || exit 2
major=$(( 0x${data[0]} ))
minor=$(( 0x${data[1]} ))

echo -e &quot;Given device:     $1&quot;
echo -e &quot;Canonical device: $dev&quot;
echo -e &quot;Major: $major&quot;
echo -e &quot;Minor: $minor\n&quot;

# sometimes nodes have been created for devices that are not present
dir=$(readlink -f /sys/dev/$mode/$major\:$minor)
if ! [ -e &quot;$dir&quot; ]; then
  echo &quot;No /sys entry for $dev&quot; &gt;&amp;2
  exit 3
fi

# walk up the /sys hierarchy one directory at a time
# stop when there are three levels left 
while [[ $dir == /*/*/* ]]; do

  # it seems the directory is only of interest if there is a 'uevent' file
  if [ -e &quot;$dir/uevent&quot; ]; then
    echo &quot;$dir:&quot;
    echo &quot;  Uevent:&quot;
    sed 's/^/    /' &quot;$dir/uevent&quot;

    # check for subsystem link
    if [ -d &quot;$dir/subsystem&quot; ]; then
        subsystem=$(readlink -f &quot;$dir/subsystem&quot;)
        echo -e &quot;\n  Subsystem:\n    ${subsystem##*/}&quot;
    fi

    echo
  fi

  # strip a subdirectory
  dir=${dir%/*}
done

---

#### 226. What is the difference between the following kernel Makefile terms: vmLinux, vmlinuz, vmlinux.bin, zimage &amp; bzimage?

**问题描述 / Problem Description**:
Tags: linux, kernel, file-format | Score: 75 | Views: 64077 | Answers: 5

**解决方案 / Solution**:
vmlinux

This is the Linux kernel in an statically linked executable file format. Generally, you don't have to worry about this file, it's just a intermediate step in the boot procedure.

The raw vmlinux file may be useful for debugging purposes.

vmlinux.bin

The same as vmlinux, but in a bootable raw binary file format. All symbols and relocation information is discarded. Generated from vmlinux by objcopy -O binary vmlinux vmlinux.bin.

vmlinuz

The vmlinux file usually gets compressed with zlib. Since 2.6.30 LZMA and bzip2 are also available. By adding further boot and decompression capabilities to vmlinuz, the image can be used to boot a system with the vmlinux kernel.  The compression of vmlinux can occur with zImage or bzImage.

The function decompress_kernel() handles the decompression of vmlinuz at bootup, a message indicates this:

Decompressing Linux... done
Booting the kernel.


zImage (make zImage)

This is the old format for small kernels (compressed, below 512KB). At boot, this image gets loaded low in memory (the first 640KB of the RAM).

bzImage (make bzImage)

The big zImage (this has nothing to do with bzip2), was created while the kernel grew and handles bigger images (compressed, over 512KB). The image gets loaded high in memory (above 1MB RAM).  As today's kernels are way over 512KB, this is usually the preferred way.



An inspection on Ubuntu 10.10 shows:

ls -lh /boot/vmlinuz-$(uname -r)
-rw-r--r-- 1 root root 4.1M 2010-11-24 12:21 /boot/vmlinuz-2.6.35-23-generic

file /boot/vmlinuz-$(uname -r)
/boot/vmlinuz-2.6.35-23-generic: Linux kernel x86 boot executable bzImage, version 2.6.35-23-generic (buildd@rosea, RO-rootFS, root_dev 0x6801, swap_dev 0x4, Normal VGA

---

#### 227. Moving Linux install to a new computer

**问题描述 / Problem Description**:
Tags: linux, cloning, migration | Score: 75 | Views: 119749 | Answers: 5

**解决方案 / Solution**:
Moving or cloning a Linux installation is pretty easy, assuming the source and target processors are the same architecture (e.g. both x86, both x64, both arm…).
Moving
When moving, you have to take care of hardware dependencies. However most users won't encounter any difficulty other than xorg.conf (and even then modern distributions tend not to need it) and perhaps the bootloader.

If the disk configuration is different, you may need to reconfigure the bootloader and filesystem tables (/etc/fstab, /etc/crypttab if you use cryptography, /etc/mdadm.conf if you use md RAID). For the bootloader, the easiest way is to pop the disk into the new machine, boot your distribution's live CD/USB and use its bootloader reparation tool.
Note that if you're copying the data rather than physically moving the disk (for example because one or both systems dual boot with Windows), it's faster and easier to copy whole partitions (with (G)Parted or dd).

If you have an xorg.conf file to declare display-related options (e.g. in relation with a proprietary driver), it will need to be modified if the target system has a different graphics card or a different monitor setup. You should also install the proprietary driver for the target system's graphics card before moving, if applicable.

If you've declared module options or blacklists in /etc/modprobe.d, they may need to be adjusted for the target system.


Cloning
Cloning an installation involves the same hardware-related issues as moving, but there are a few more things to take care of to give the new machine a new identity.

Edit /etc/hostname to give the new machine a new name.
Search for other occurrences of the host name under /etc. Common locations are /etc/hosts (alias for 127.0.0.1) and /etc/mailname or other mail system configuration.

Regenerate the ssh host key.

Make any necessary change to the networking configuration (such as a static IP address).

Change the UUID of RAID volumes (not necessary, but recommended to avoid confusion), e.g., mdadm -U uuid.


See also a step-by-step cloning guide targeted at Ubuntu.
My current desktop computer installation was cloned from its predecessor by unplugging one of two RAID-1 mirrored disks, moving it into the new computer, creating a RAID-1 volume on the already present disk, letting the mirror resynchronize, and making the changes outlined above where applicable.

---

#### 228. What is the difference between kill , pkill and killall?

**问题描述 / Problem Description**:
Tags: linux, bash, shell-script, kill | Score: 75 | Views: 85342 | Answers: 4

**解决方案 / Solution**:
The kill command is a very simple wrapper to the kill system call, which knows only about process IDs (PIDs). pkill and killall are also wrappers to the kill system call, (actually, to the libc library which directly invokes the system call), but can determine the PIDs for you, based on things like, process name, owner of the process, session id, etc. 

How pkill and killall work can be seen using ltrace or strace on them. On Linux, they both read through the /proc filesystem, and for each pid (directory) found, traverses the path in a way to identify a process by its name or other attributes. How this is done is technically speaking, kernel and system specific. In general, they read from /proc/&lt;PID&gt;/stat which contains the command name as the 2nd field. For pkill -f and pgrep examine the /cmdline entry for each PID's proc entry.

pkill and pgrep use the readproc system call, whereas killall does not. I couldn't say if there's a performance difference: you'll have to benchmark that on your own.

---

#### 229. Which process is `/proc/self/` for?

**问题描述 / Problem Description**:
Tags: linux, process, proc | Score: 74 | Views: 76099 | Answers: 6

**解决方案 / Solution**:
This has nothing to do with foreground and background processes; it only has to do with the currently running process. When the kernel has to answer the question “What does /proc/self point to?”, it simply picks the currently-scheduled pid, i.e. the currently running process (on the current logical CPU). The effect is that /proc/self always points to the asking program's pid; if you run
ls -l /proc/self

you'll see ls's pid, if you write code which uses /proc/self that code will see its own pid, etc.

---

#### 230. Limit SSH access to specific clients by IP address

**问题描述 / Problem Description**:
Tags: linux, firewall, sshd | Score: 74 | Views: 310438 | Answers: 6

**解决方案 / Solution**:
You can limit which hosts can connect by configuring TCP wrappers or filtering network traffic (firewalling) using iptables. If you want to use different authentication methods depending on the client IP address, configure SSH daemon instead (option 3).
Option 1: Filtering with IPTABLES
Iptables rules are evaluated in order, until first match.
For example, to allow traffic from 192.168.0.0/24 network and otherwise drop the traffic (to port 22). The DROP rule is not required if your iptables default policy is configured to DROP.
iptables -A INPUT -p tcp --dport 22 --source 192.168.0.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP

You can add more rules before the drop rule to match more networks/hosts. If you have a lot of networks or host addresses, you should use ipset module. There is also iprange module which allows using any arbitrary range of IP addresses.
Iptables are not persistent across reboots. You need to configure some mechanism to restore iptables on boot.
iptables apply only to IPv4 traffic. Systems which have ssh listening to IPv6 address the necessary configuration can be done with ip6tables.
Option 2: Using TCP wrappers
Note: this might not be an option on modern distributions, as support for tcpwrappers was removed from OpenSSH 6.7
You can also configure which hosts can connect using TCP wrappers. With TCP wrappers, in addition to IP addresses you can also use hostnames in rules.
By default, deny all hosts.
/etc/hosts.deny:
sshd : ALL

Then list allowed hosts in hosts.allow. For example to allow network 192.168.0.0/24 and localhost.
/etc/hosts.allow:
sshd : 192.168.0.0/24
sshd : 127.0.0.1
sshd : [::1]

Option 3: SSH daemon configuration
You can configure ssh daemon in sshd_config to use different authentication method depending on the client address/hostname. If you only want to block other hosts from connecting, you should use iptables or TCP wrappers instead.
First remove default authentication methods:
PasswordAuthentication no
PubkeyAuthentication no

Then add desired authentication methods after a Match Address in the end of the file. Placing Match in the end of the file is important, since all the configuration lines after it are placed inside the conditional block until the next Match line. For example:
Match Address 127.0.0.*
    PubkeyAuthentication yes

Other clients are still able to connect, but logins will fail because there is no available authentication methods.
Match arguments and allowed conditional configuration options are documented in  sshd_config man page. Match patterns are documented in ssh_config man page.

---

#### 231. Is there any (good) SQLite GUI for Linux?

**问题描述 / Problem Description**:
Tags: linux, software-rec, gui, sqlite | Score: 74 | Views: 74590 | Answers: 6

**解决方案 / Solution**:
I've been using sqlitebrowser, it is a really good option. Though probably not the only one!
On Ubuntu, it is available in the default package repositories.
sudo apt-get install sqlitebrowser

or as Snap package:
snap install sqlitebrowser

---

#### 232. disable transparent hugepages

**问题描述 / Problem Description**:
Tags: linux, kernel, sysctl | Score: 74 | Views: 168451 | Answers: 11

**解决方案 / Solution**:
To make options such as this permanent you'll typically add them to the file /etc/sysctl.conf. You can see a full list of the options available using this command:

$ sysctl -a


Example

$ sudo sysctl -a | head -5
kernel.sched_child_runs_first = 0
kernel.sched_min_granularity_ns = 6000000
kernel.sched_latency_ns = 18000000
kernel.sched_wakeup_granularity_ns = 3000000
kernel.sched_shares_ratelimit = 750000


You can look for hugepage in the output like so:

$ sudo sysctl -a | grep hugepage
vm.nr_hugepages = 0
vm.nr_hugepages_mempolicy = 0
vm.hugepages_treat_as_movable = 0
vm.nr_overcommit_hugepages = 0


It's not there?

However looking through the output I did not see transparent_hugepage. Googling a bit more I did come across this Oracle page which discusses this very topic. The page is titled: Configuring HugePages for Oracle on Linux (x86-64).

Specifically on that page they mention how to disable the hugepage feature.

excerpt


  The preferred method to disable Transparent HugePages is to add "transparent_hugepage=never" to the kernel boot line in the "/etc/grub.conf" file.

   title Oracle Linux Server (2.6.39-400.24.1.el6uek.x86_64)
            root (hd0,0)
            kernel /vmlinuz-2.6.39-400.24.1.el6uek.x86_64 ro root=/dev/mapper/vg_ol6112-lv_root rd_NO_LUKS  KEYBOARDTYPE=pc KEYTABLE=uk
    LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16  rd_NO_DM rd_LVM_LV=vg_ol6112/lv_swap rd_LVM_LV=vg_ol6112/lv_root rhgb quiet numa=off
    transparent_hugepage=never
            initrd /initramfs-2.6.39-400.24.1.el6uek.x86_64.img

  
  The server must be rebooted for this to take effect.


Alternatively you can add the command to your /etc/rc.local file.

if test -f /sys/kernel/mm/transparent_hugepage/enabled; then
   echo never &gt; /sys/kernel/mm/transparent_hugepage/enabled
fi
if test -f /sys/kernel/mm/transparent_hugepage/defrag; then
   echo never &gt; /sys/kernel/mm/transparent_hugepage/defrag
fi


I think I would go with the 2nd option, since the first will be at risk of getting unset when you upgrade from one kernel to the next.

You can confirm that it worked with the following command after rebooting:

$ cat /sys/kernel/mm/transparent_hugepage/enabled
always madvise [never]

---

#### 233. Understanding /dev and its subdirs and files

**问题描述 / Problem Description**:
Tags: linux, devices, file-descriptors | Score: 74 | Views: 71565 | Answers: 3

**解决方案 / Solution**:
Almost all the files under /dev are device files. Whereas reading and writing to a regular file stores data on a disk or other filesystem, accessing a device file communicates with a driver in the kernel, which generally in turn communicates with a piece of hardware (a hardware device, hence the name).

There are two types of device files: block devices (indicated by b as the first character in the output of ls -l), and character devices (indicated by c). The distinction between block and character devices is not completely universal. Block devices are things like disks, which behave like large, fixed-size files: if you write a byte at a certain offset, and later read from the device at that offset, you get that byte back. Character devices are just about anything else, where writing a byte has some immediate effect (e.g. it's emitted on a serial line) and reading a byte also has some immediate effect (e.g. it's read from the serial port).

The meaning of a device file is determined by its number, not by its name (the name matters to applications, but not to the kernel). The number is actually two numbers: the major number indicates which driver is responsible for this device, and the minor number allows a driver to drive several devices¹. These numbers appear in the ls -l listing, where you would normally find the file size. E.g. brw-rw---- 1 root disk 8, 0 Jul 12 15:54 /dev/sda → this device is major 8, minor 0.

Some device files under /dev don't correspond to hardware devices. One that exists on every unix system is /dev/null; writing to it has no effect, and reading from it never returns any data. It's often convenient in shell scripts, when you want to ignore the output from a command (&gt;/dev/null) or run a command with no input (&lt;/dev/null). Other common examples are /dev/zero (which returns null bytes ad infinitum) /dev/urandom (which returns random bytes ad infinitum).

A few device files have a meaning that depends on the process that accesses it. For example, /dev/stdin designates the standard input of the current process; opening from has approximately the same effect as opening the original file that was opened as the process's standard input. Somewhat similarly, /dev/tty designates the terminal to which the process is connected. Under Linux, nowadays, /dev/stdin and friends are not implemented as character devices, but instead as symbolic links to a more general mechanism that allows every file descriptor to be referenced (as opposed to only 0, 1 and 2 under the traditional method); for example /dev/stdin is a symbolic link to /proc/self/fd/0. See How does /dev/fd relate to /proc/self/fd/?.

You'll find a number of symbolic links under /dev. This can occur for historical reasons: a device file was moved from one name to another, but some applications still use the old name. For example, /dev/scd0 is a symbolic link to /dev/sr0 under Linux; both designate the first CD device. Another reason for symbolic links is organization: under Linux, you'll find your hard disks and partitions in several places: /dev/sda and /dev/sda1 and friends (each disk designated by an arbitrary letter, and partitions according to the partition layout), /dev/disk/by-id/* (disks designated by a unique serial number), /dev/disk/by-label/* (partitions with a filesystem, designated by a human-chosen label); and more. Symbolic links are also used when a generic device name could be one of several; for example /dev/dvd might be a symbolic link to /dev/sr0, or it might be a link to /dev/sr1 if you have two CD readers and the second one is to be the default DVD reader.

Finally, there are a few other files that you might find under /dev, for traditional reasons. You won't find the same on every system. On most unices, /dev/log is a socket that programs use to emit log messages. /dev/MAKEDEV is a script that creates entries in /dev. On modern Linux systems, entries in /dev/ are created automatically by udev, obsoleting MAKEDEV.


¹ This is actually no longer true under Linux, but this detail only matters to device driver writers.

---

#### 234. What is the min and max values of exit codes in Linux?

**问题描述 / Problem Description**:
Tags: linux, executable, function, exit-status | Score: 74 | Views: 37284 | Answers: 4

**解决方案 / Solution**:
The number passed to the _exit()/exit_group() system call (sometimes referred as the exit code to avoid the ambiguity with exit status which is also referring to an encoding of either the exit code or signal number and additional info depending on whether the process was killed or exited normally) is of type int, so on Unix-like systems like Linux, typically a 32bit integer with values from -2147483648 (-231) to 2147483647 (231-1).

However, on all systems, when the parent process (or the child subreaper or init if the parent died) uses the wait(), waitpid(), wait3(), wait4() system calls to retrieve it, only the lower 8 bits of it are available (values 0 to 255 (28-1)).

When using the waitid() API (or a signal handler on SIGCHLD), on most systems (and as POSIX now more clearly requires in the 2016 edition of the standard (see _exit() specification)), the full number is available (in the si_status field of the returned structure). That is not the case on Linux yet though which also truncates the number to 8 bits with the waitid() API, though that's likely to change in the future.

Generally, you'd want to only use values 0 (generally meaning success) to 125 only, as many shells use values above 128 in their $? representation of the exit status to encode the signal number of a process being killed and 126 and 127 for special conditions.

You may want to use 126 to 255 on exit() to mean the same thing as they do for the shell's $? (like when a script does ret=$?; ...; exit "$ret"). Using values outside 0 -> 255 is generally not useful. You'd generally only do that if you know the parent will use the waitid() API on systems that don't truncate and you happen to have a need for the 32bit range of values. Note that if you do a exit(2048) for instance, that will be seen as success by parents using the traditional wait*() APIs.

More info at:


Default exit code when process is terminated?


That Q&amp;A should hopefully answer most of your other questions and clarify what is meant by exit status. I'll add a few more things:

A process cannot terminate unless it's killed or calls the _exit()/exit_group() system calls. When you return from main() in C, the libc calls that system call with the return value.

Most languages have a exit() function that wraps that system call, and the value they take, if any is generally passed as is to the system call. (note that those generally do more things like the clean-up done by C's exit() function that flushes the stdio buffers, runs the atexit() hooks...)

That's the case of at least:

$ strace -e exit_group awk 'BEGIN{exit(1234)}'
exit_group(1234)                        = ?
$ strace -e exit_group mawk 'BEGIN{exit(1234)}'
exit_group(1234)                        = ?
$ strace -e exit_group busybox awk 'BEGIN{exit(1234)}'
exit_group(1234)                        = ?
$ echo | strace -e exit_group sed 'Q1234'
exit_group(1234)                        = ?
$ strace -e exit_group perl -e 'exit(1234)'
exit_group(1234)                        = ?
$ strace -e exit_group python -c 'exit(1234)'
exit_group(1234)                        = ?
$ strace -e exit_group expect -c 'exit 1234'
exit_group(1234)                        = ?
$ strace -e exit_group php -r 'exit(1234);'
exit_group(1234)                        = ?
$ strace -e exit_group zsh -c 'exit 1234'
exit_group(1234)


You occasionaly see some that complain when you use a value outside of 0-255:

$ echo 'm4exit(1234)' | strace -e exit_group m4
m4:stdin:1: exit status out of range: `1234'
exit_group(1)                           = ?


Some shells complain when you use a negative value:

$ strace -e exit_group dash -c 'exit -1234'
dash: 1: exit: Illegal number: -1234
exit_group(2)                           = ?
$ strace -e exit_group yash -c 'exit -- -1234'
exit: `-1234' is not a valid integer
exit_group(2)                           = ?


POSIX leaves the behaviour undefined if the value passed to the exit special builtin is outside 0->255.

Some shells show some unexpected behaviours if you do:


bash (and mksh but not pdksh on which it is based) takes upon itself to truncate the value to 8 bits:

$ strace -e exit_group bash -c 'exit 1234'
exit_group(210)                         = ?


So in those shells, if you do want to exit with a value outside of 0-255, you have to do something like:

exec zsh -c 'exit -- -12345'
exec perl -e 'exit(-12345)'


That is execute another command in the same process that can call the system call with the value you want.
as mentioned at that other Q&amp;A, ksh93 has the weirdest behaviour for exit values from 257 to 256+max_signal_number where instead of calling exit_group(), it kills itself with the corresponding signal¹.

$ ksh -c 'exit "$((256 + $(kill -l STOP)))"'
zsh: suspended (signal)  ksh -c 'exit "$((256 + $(kill -l STOP)))"'


and otherwise truncates the number like bash/mksh.




¹ That's likely to change in the next version though. Now that the development of ksh93 has been taken over as a community effort outside of AT&amp;T, that behaviour, even though encouraged somehow by POSIX, is being reverted

---

#### 235. linux + g++: command not found

**问题描述 / Problem Description**:
Tags: linux, g++ | Score: 74 | Views: 196493 | Answers: 2

**解决方案 / Solution**:
Install the suite of development tools first. Then go back to compile the software.
yum groupinstall 'Development Tools'

You could need much more than just the compiler. The Development Tools package includes the core development tools like automake, gcc, perl, python, flex, make, gdb, bison, and many more. To list all of the software in the package group, use yum as follows.
yum group info 'Development Tools'

For Fedora 20 (at least), you'll additionally need to install gcc-c++.
For Debian-based systems, install the suite of development tools as follows.
apt-get install build-essential

In Void Linux, it's xbps-install -Su base-devel, which provides m4, autoconf, automake, bc, binutils, bison, ed, libfl-devel, flex, libgcc-devel, kernel-libc-headers, glibc-devel, isl, cloog, mpfr, libmpc, gcc, libstdc++-devel, gcc-c++, gettext-libs, gettext, groff, libtool, make, patch, pkg-config, texinfo, unzip, and xz.

---

#### 236. Access to original contents of mount point

**问题描述 / Problem Description**:
Tags: linux, debian, mount | Score: 74 | Views: 38173 | Answers: 3

**解决方案 / Solution**:
mkdir /mnt/root
mount --bind / /mnt/root
ls /mnt/root/home/foo/.ssh


As long as you use --bind (as opposed to --rbind), you get a clone of the mount without the stuff mounted on top of it.

---

#### 237. What is /lib64/ld-linux-x86-64.so.2 and why can it be used to execute file?

**问题描述 / Problem Description**:
Tags: linux, files, libraries | Score: 74 | Views: 116146 | Answers: 1

**解决方案 / Solution**:
That’s the dynamic linker; if you run it on its own, it will tell you what it does:

Usage: ld.so [OPTION]... EXECUTABLE-FILE [ARGS-FOR-PROGRAM...]


You have invoked ‘ld.so’, the helper program for shared library executables.
This program usually lives in the file /lib/ld.so, and special directives
in executable files using ELF shared libraries tell the system's program
loader to load the helper program from this file.  This helper program loads
the shared libraries needed by the program executable, prepares the program
to run, and runs it.  You may invoke this helper program directly from the
command line to load and run an ELF executable file; this is like executing
that file itself, but always uses this helper program from the file you
specified, instead of the helper program file specified in the executable
file you run.  This is mostly of use for maintainers to test new versions
of this helper program; chances are you did not intend to run this program.

The linker is used to run dynamically-linked programs. When you run chmod, the kernel effectively runs the equivalent of /lib64/ld-linux-x86-64.so.2 /bin/chmod, as you did manually; the latter works even if the chmod binary isn’t executable because the check for execute permission is done by the execve() system call on the file that it is being told to execute and in the /lib64/ld-linux-x86-64.so.2 /bin/chmod shell command line, the path passed by the shell to execve() is /lib64/ld-linux-x86-64.so.2, not /bin/chmod, and it’s the one that is checked for execute permission, /bin/chmod is only passed as an argument to the linker. It's the same thing in /bin/sh ./some-script where ./some-script doesn't need to be executable.
You’ll find much more detail on this in the excellent How programs get run: ELF binaries article.

---

#### 238. How to find which process is regularly writing to disk?

**问题描述 / Problem Description**:
Tags: linux, debian, logs, hard-disk | Score: 73 | Views: 157726 | Answers: 9

**解决方案 / Solution**:
Did you tried to examin what programs like iotop is showing? It will tell you exacly what kind of process is currently writing to the disk.

example output:

Total DISK READ: 0.00 B/s | Total DISK WRITE: 0.00 B/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO&gt;    COMMAND
    1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % init
    2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
    3 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/0]
    6 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/0]
    7 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [watchdog/0]
    8 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/1]
 1033 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [flush-8:0]
   10 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/1]

---

#### 239. Is there any reason why I get ^[[A when I press up arrow at the console login screen?

**问题描述 / Problem Description**:
Tags: linux, keyboard, login, console, escape-characters | Score: 73 | Views: 90970 | Answers: 7

**解决方案 / Solution**:
TLDR

You're probably running sh which outputs the raw keycodes generated when you press the Up arrow key.

A more advanced shell like bash intercepts these keycodes and does something with them. E.g. show the last command in its history.

To fix your issue, type bash to enter a bash shell. Then use the up/down arrow commands (note, your history would start afresh in the new shell).

---

#### 240. How to reconnect a logically disconnected USB device?

**问题描述 / Problem Description**:
Tags: linux, usb, usb-drive | Score: 73 | Views: 122263 | Answers: 10

**解决方案 / Solution**:
It is sometimes possible to do a power cycle on branch of the USB bus where the device is plugged :

# echo suspend &gt; /sys/bus/usb/devices/1-1/power/level
# echo auto &gt; /sys/bus/usb/devices/1-1/power/level


The 1-1 should be adjusted to your configuration. You can see to which part of the USB tree your device is plugged by running lsusb -t before ejecting it.

You can find detailed information on the linux-usb mailing-list, this thread for example.

---

#### 241. Will a Linux executable compiled on one &quot;flavor&quot; of Linux run on a different one?

**问题描述 / Problem Description**:
Tags: linux, compiling, architecture, compatibility | Score: 72 | Views: 29471 | Answers: 6

**解决方案 / Solution**:
In short:  If you're taking a compiled binary from one host to another using the same (or a compatible) architecture, you may be perfectly fine taking it to another distribution.  However as complexity of the code increases, the likelihood of being linked against a library that is not installed; installed in another location; or installed at a different version, increases.  Taking for instance your code, for which ldd reports the following dependencies when compiled with gcc -o exit-test exit-test.c on a (Debian-derived) Ubuntu Linux host:

$ ldd exit-test
    linux-gate.so.1 =&gt;  (0xb7748000)
    libc.so.6 =&gt; /lib/i386-linux-gnu/libc.so.6 (0xb757b000)
    /lib/ld-linux.so.2 (0x8005a000)


Obviously this binary won't run if I kick it over to, say, a Mac (./exit-test: cannot execute binary file: Exec format error).  Let's try moving it to a RHEL box:

$ ./exit-test
-bash: ./exit-test: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory


Oh dear.  Why might this be?

$ ls /lib/ld-l* # reference the `ldd` output above
ls: cannot access /lib/ld-l*: No such file or directory


Even for this use-case, forklifting it failed due to missing shared libraries.

However, if I compile it with gcc -static exit-test-static exit-test.c, porting it to the system without the libraries works just fine.  At the expense, of course, of disk space:

$ ls -l ./exit-test{,-static}
-rwxr-xr-x  1 username  groupname    7312 Jan 29 14:18 ./exit-test
-rwxr-xr-x  1 username  groupname  728228 Jan 29 14:27 ./exit-test-static


Another viable solution would be to install the requisite libraries on the new host.  

As with many things in the U&amp;L universe, this is a cat with many skins, two of which are outlined above.

---

#### 242. How to start a windows partition from the Grub command line

**问题描述 / Problem Description**:
Tags: linux, grub | Score: 72 | Views: 399100 | Answers: 10

**解决方案 / Solution**:
The following worked for me with a GPT partitioned disk.

insmod part_gpt
insmod chain
set root=(hd0,gpt1)
chainloader /EFI/Microsoft/Boot/bootmgfw.efi
boot


Note that you can enter a command line from the grub boot menu and just type commands as above to test out different combinations.

You need to enter the id of the EFI boot partition (not the windows partition) for the set root= command.

In the command line grub mode  ls will list the hard drive partitions, help lists available commands.

Once you have set the root correctly you can ls / to view files and directories to find the correct path to the windows boot manager if it is not in the default location.

---

#### 243. Finding files that use the most disk space

**问题描述 / Problem Description**:
Tags: linux, disk-usage | Score: 72 | Views: 359911 | Answers: 13

**解决方案 / Solution**:
With standard available tools: 

To list the top 10 largest files from the current directory: du . | sort -nr | head -n10

To list the largest directories from the current directory: du -s * | sort -nr | head -n10

UPDATE These days I usually use a more readable form (as Jay Chakra explains in another answer and leave off the | head -n10, simply let it scroll off the screen. The last line has the largest file or directory (tree).

Sometimes, eg. when you have lots of mount points in the current directory,  instead of using -x or multiple --exclude=PATTERN, it is handier to mount the filesystem on an unused mount point (often /mnt) and work from there.

Mind you that when working with large (NFS) volumes, you can cause a substantial load on the storage backend (filer) when running du over lots of (sub)directories. In that case it is better to consider setting quota on the volume.

---

#### 244. How to shutdown Linux at specific datetime from terminal?

**问题描述 / Problem Description**:
Tags: linux, shutdown, scheduling | Score: 72 | Views: 206534 | Answers: 5

**解决方案 / Solution**:
You can do this directly from the shutdown command, see man shutdown:

SYNOPSIS
   /sbin/shutdown [-akrhPHfFnc] [-t sec] time [warning message]

[...]

   time   When to shutdown.


So, for example:

shutdown -h 21:45


That will run shutdown -h at 21:45. 



For commands that don't offer this functionality, you can try one of: 

A. Using at

The at daemon is designed for precisely this. Depending on your OS, you may need to install it. On Debian based systems, this can be done with:

sudo apt-get install at


There are three ways of giving a command to at:


Pipe it:

$ echo "ls &gt; a.txt" | at now + 1 min
warning: commands will be executed using /bin/sh
job 3 at Thu Apr  4 20:16:00 2013

Save the command you want to run in a text file, and then pass that file to at:

$ echo "ls &gt; a.txt" &gt; cmd.txt
$ at now + 1 min &lt; cmd.txt
warning: commands will be executed using /bin/sh
job 3 at Thu Apr  4 20:16:00 2013

You can also pass at commands from STDIN:

$ at now + 1 min
warning: commands will be executed using /bin/sh
at&gt; ls


Then, press CtrlD to exit the at shell. The ls command will be run in one minute. 


You can give very precise times in the format of [[CC]YY]MMDDhhmm[.ss], as in 

$ at -t 201403142134.12 &lt; script.sh


This will run the script script.sh at 21:34 and 12 seconds on the 14th of March 2014.

B. Using cron (though this not a good idea for shutdown)

The other approach is using the cron scheduler which is designed to perform tasks at specific times. It is usually used for tasks that will be repeated but you can also give a specific time. Each user has their own "crontabs" which control what jobs are executed and when. The general format of a crontab is:

*     *     *     *     *  command to be executed
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- day of week (0 - 6) (Sunday=0)
|     |     |     +------- month (1 - 12)
|     |     +--------- day of month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)


So, for example, this will run ls every day at 14:04:

04 14 * * * ls


To set up a cronjob for a specific date:


Create a new crontab by running crontab -e. This will bring up a window of your favorite text editor.
Add this line to the file that just opened. This particular example will run at 14:34 on the 15th of March 2014 if that day is a Friday (so, OK, it might run more than once):

34 14 15 5  /path/to/command        

Save the file and exit the editor.


This SO answer suggests a way to have it run only once but I have never used it so I can't vouch for it.

---

#### 245. cp -L vs. cp -H

**问题描述 / Problem Description**:
Tags: linux, command-line, cp, options, coreutils | Score: 72 | Views: 163787 | Answers: 2

**解决方案 / Solution**:
With symlinks, tools have two things they can do:


Treat the symlink as a symlink ("preserving its nature"), or
Treat the symlink as the type of file that it points to.


Saying that -H "preserves its nature" is not a contradiction.  Consider the alternative.  If you use -L, any symlinks cp finds will be opened, and their contents copied to the target file name.  So the source was a symlink, but its copy is not a symlink.  So it "lost its nature as a symlink".

Consider

$ mkdir subdir
$ echo "some contents" &gt; subdir/file
$ ln -s file subdir/link

# definition of "list", the abbreviated ls -l output used below
$ list() { ls -l "$@" | \
    awk '$0 !~ /^total/ { printf "%s %s\t%s %s %s\n", $1, $5, $9, $10, $11 }' ; }

$ list subdir
-rw-rw-r-- 14   file  
lrwxrwxrwx 4    link -&gt; file

$ cp -rH subdir subdir-with-H
$ list subdir-with-H
-rw-rw-r-- 14   file  
lrwxrwxrwx 4    link -&gt; file

$ cp -rL subdir subdir-with-L
$ list subdir-with-L
-rw-rw-r-- 14   file  
-rw-rw-r-- 14   link

---

#### 246. &quot;WannaCry&quot; on Linux systems: How do you protect yourself?

**问题描述 / Problem Description**:
Tags: linux, security, linux-kernel, samba | Score: 72 | Views: 23779 | Answers: 2

**解决方案 / Solution**:
This Samba new vulnerability is already being called "Sambacry", while the exploit itself mentions "Eternal Red Samba", announced in twitter (sensationally) as:


  Samba bug, the metasploit one-liner to trigger is just:
  simple.create_pipe("/path/to/target.so")


Potentially affected Samba versions are from Samba 3.5.0 to 4.5.4/4.5.10/4.4.14. 

If your Samba installation meets the configurations described bellow, the fix/upgrade should be done ASAP as there are already exploits, other exploit in python and
metasploit modules out there.

More interestingly enough, there are already add-ons to a know honeypot from the honeynet project, dionaea both to WannaCry and SambaCry plug-ins. 

Samba cry seems to be already being (ab)used to install more crypto-miners "EternalMiner" or double down as a malware dropper in the future.


  honeypots set up by the team of researchers from Kaspersky Lab have
  captured a malware campaign that is exploiting SambaCry vulnerability
  to infect Linux computers with cryptocurrency mining software. Another
  security researcher, Omri Ben Bassat‏, independently discovered the
  same campaign and named it "EternalMiner."


The advised workaround for systems with Samba installed (which also is present in the CVE notice) before updating it, is adding to smb.conf:

nt pipe support = no


(and restarting the Samba service)

This is supposed to disable a setting that turns on/off the ability to make anonymous connections to the windows IPC named pipes service.  From man samba:


  This global option is used by developers to allow or disallow Windows
  NT/2000/XP clients the ability to make connections to NT-specific SMB
  IPC$ pipes. As a user, you should never need to override the default.


However from our internal experience, it seems the fix is not compatible with older? Windows versions ( at least some? Windows 7 clients seem to not work with the nt pipe support = no), and as such the remediation route can go in extreme cases into installing or even compiling Samba.

More specifically, this fix  disable shares listing from Windows clients, and if applied they have to manually specify the full path of the share to be able to use it.

Other known workaround is to make sure Samba shares are mounted with the noexec option. This will prevent the execution of binaries residing on the mounted filesystem.

The official security source code patch is here from the samba.org security page. 

Debian already pushed yesterday (24/5) an update out the door, and the corresponding security notice DSA-3860-1 samba 

To verify in if the vulnerability is corrected in Centos/RHEL/Fedora and derivates, do:

#rpm -q –changelog samba | grep -i CVE
– resolves: #1450782 – Fix CVE-2017-7494
– resolves: #1405356 – CVE-2016-2125 CVE-2016-2126
– related: #1322687 – Update CVE patchset


There is now an nmap detection script :samba-vuln-cve-2017-7494.nse  for detecting Samba versions, or a much better nmap script that checks if the service is vulnerable at http://seclists.org/nmap-dev/2017/q2/att-110/samba-vuln-cve-2017-7494.nse , copy it to /usr/share/nmap/scripts and then update the nmap database , or run it as follows:

nmap --script /path/to/samba-vuln-cve-2017-7494.nse -p 445 &lt;target&gt;


About long term measures to protect the SAMBA service:  The SMB protocol should never be offered directly to the Internet at large.

It goes also without saying that SMB has always been a convoluted protocol, and that these kind of services ought to be firewalled and restricted to the internal networks [to which they are being served]. 

When remote access is needed, either to home or specially to corporate networks, those accesses should be better done using VPN technology. 

As usual, on this situations the Unix principle of only installing and activating the minimum services required does pay off.

Taken from the exploit itself:


  Eternal Red Samba Exploit -- CVE-2017-7494.
          Causes vulnerable Samba server to load a shared library in root context.
          Credentials are not required if the server has a guest account.
          For remote exploit you must have write permissions to at least one share.
          Eternal Red will scan the Samba server for shares it can write to.
          It will also determine the fullpath of the remote share.  

    For local exploit provide the full path to your shared library to load.  

    Your shared library should look something like this

    extern bool change_to_root_user(void);
    int samba_init_module(void)
    {
        change_to_root_user();
        /* Do what thou wilt */
    }



It is also known systems with SELinux enabled are not vulnerable to the exploit.

See 7-Year-Old Samba Flaw Lets Hackers Access Thousands of Linux PCs Remotely


  According to the Shodan computer search engine, more than 485,000
  Samba-enabled computers exposed port 445 on the Internet, and
  according to researchers at Rapid7, more than 104,000 internet-exposed
  endpoints appeared to be running vulnerable versions of Samba, out of
  which 92,000 are running unsupported versions of Samba. 
  
  Since Samba is
  the SMB protocol implemented on Linux and UNIX systems, so some
  experts are saying it is "Linux version of EternalBlue," used by the
  WannaCry ransomware. 
  
  ...or should I say SambaCry? 
  
  Keeping in mind the
  number of vulnerable systems and ease of exploiting this
  vulnerability, the Samba flaw could be exploited at large scale with
  wormable capabilities. 
  
  Home networks with network-attached storage
  (NAS) devices [that also run Linux] could also be vulnerable to this flaw.


See also A wormable code-execution bug has lurked in Samba for 7 years. Patch now!


  The seven-year-old flaw, indexed as CVE-2017-7494, can be reliably
  exploited with just one line of code to execute malicious code, as
  long as a few conditions are met. Those requirements include
  vulnerable computers that:
  
  (a) make file- and printer-sharing port 445
  reachable on the Internet,
  (b) configure shared files to have write
  privileges, and
  (c) use known or guessable server paths for those
  files.
  
  When those conditions are satisfied, remote attackers can
  upload any code of their choosing and cause the server to execute it,
  possibly with unfettered root privileges, depending on the vulnerable
  platform.
  
  Given the ease and reliability of exploits, this hole is worth
  plugging as soon as possible. It's likely only a matter of time until
  attackers begin actively targeting it.


Also Rapid 7 - Patching CVE-2017-7494 in Samba: It’s the Circle of Life

And more SambaCry: The Linux Sequel to WannaCry.


  Need-to-Know Facts
  
  CVE-2017-7494 has a CVSS Score of 7.5
  (CVSS:3.0/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H)3.
  
  Threat Scope
  
  A shodan.io query of "port:445 !os:windows" shows approximately one
  million non-Windows hosts that have tcp/445 open to the Internet, more
  than half of which exist in the United Arab Emirates (36%) and the
  U.S. (16%).   While many of these may be running patched versions,
  have SELinux protections, or otherwise don't match the necessary
  criteria for running the exploit, the possible attack surface for this
  vulnerability is large.


P.S. The commit fix in the SAMBA github project appear to be commit 02a76d86db0cbe79fcaf1a500630e24d961fa149

---

#### 247. fork: retry: Resource temporarily unavailable

**问题描述 / Problem Description**:
Tags: linux, fork | Score: 72 | Views: 270452 | Answers: 5

**解决方案 / Solution**:
This could be due to some resource limit, either on the server itself (or) specific to your user account. Limits in your shell could be checked via ulimit -a. Esp check for ulimit -u max user processes, if you have reached max processes, fork is unable to create any new and failing with that error. This could also be due to swap/memory resource issue

---

#### 248. Using grep in conditional statement in bash

**问题描述 / Problem Description**:
Tags: bash, shell-script, ubuntu | Score: 72 | Views: 271111 | Answers: 3

**解决方案 / Solution**:
You're almost there. Just omit the exclamation mark:

OUTPUT='blah blah (Status: 200)'
if echo "$OUTPUT" | grep -q "(Status:\s200)"; then
    echo "MATCH"
fi


Result:

MATCH


The if condition is fulfilled if grep returns with exit code 0 (which means a match). The ! exclamation mark will negate this.

---

#### 249. Can we get compiler information from an elf binary?

**问题描述 / Problem Description**:
Tags: linux, debugging, executable, elf, compiler | Score: 71 | Views: 108901 | Answers: 9

**解决方案 / Solution**:
There isn't a universal way, but you can make an educated guess by looking for things only done by one compiler.

GCC is the easiest; it writes a .comment section that contains the GCC version string (the same string you get if you run gcc --version). I don't know if there's a way to display it with readelf, but with objdump it's:

objdump -s --section .comment /path/binary




I just realized I ignored the rest of your question. Flags aren't generally saved anywhere; they would be in a comment section most likely, but I've never seen that done. There's a spot in the COFF header for a timestamp, but there's no equivalent in ELF, so I don't think the compile time is available either

---

#### 250. What is the difference between `ls` and `l`?

**问题描述 / Problem Description**:
Tags: linux, command-line, ubuntu, ls, alias | Score: 71 | Views: 65335 | Answers: 5

**解决方案 / Solution**:
SHORT ANSWER: understand what exactly this alias does, you can check out the ~/.bashrc file and search for the term "alias l=". It is nothing but ls -CF

LONG ANSWER
A good way to inspect what a command is:

type l


If it's a program or a script, it will give you its location, if it is an alias, it will tell you what it's aliased to, if it's a function, it will print the funciton; otherwise, it will tell you if it is a built-in or a keyword.

Examples:

$ type l
l is aliased to `ls -CF'
$ type find
find is /usr/bin/find
$ type connecthome
connecthome is hashed (/usr/local/bin/connecthome)
$ type grep
grep is aliased to `grep --color=auto --binary-files=without-match --devices=skip'
$ type hello_se
hello_se is a function
hello_se () 
{ 
  echo 'Hello, Stack Exchangers!'
}
$ type type
type is a shell builtin
$ type for
for is a shell keyword
$ type nosuchthing
-bash: type: nosuchthing: not found

---

#### 251. [V2EX] Gnome 桌面下截图上传到 imgur 的 extension

**问题描述 / Problem Description**:
Gnome50/Debian13 上测试通过的特别方便 V2EX 上发图片，就像我现在这样     https://github.com/wuruxu/gnome-shell-extension-imgur

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://github.com/wuruxu/gnome-shell-extension-imgur

---

#### 252. [V2EX] Manjaro 真不错

**问题描述 / Problem Description**:
本来打算直接 ubuntu 的，但这个时间节点有点尴尬，26.04LTS 快发又还没发。试了下 Manjaro ，几乎开箱即用了~linux 没有微信语音输入有点难受 = =

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 253. [V2EX] 写了个 lottie 动画在 Linux 桌面上顶层播放的小东西

**问题描述 / Problem Description**:
写了个 lottie 动画在 linux 桌面上顶层播放的小东西，可以用在和 codex/claude 回复结束后，播放一个小动画提示，没什么用的玩具
https://github.com/xxyangyoulin/linux-lottie-salute

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://github.com/xxyangyoulin/linux-lottie-salute

---

#### 254. [V2EX] LXC veth 桥接网络模式下如何避免发送的数据包被拆成小包？

**问题描述 / Problem Description**:
网卡是 rtl8127, 用 iperf3 测速，在 host 上测速可以达到 9.42 Gbits/sec ，在 lxc 里测速只有 3.25 Gbits/sec ，造成这么大差异的原因是在 lxc 里发送的数据包被拆成了 1.5KB 的小包（也就是 mtu 的大小），而在 host 上发送的数据包是几十 KB 的大包，我想知道如何让 lxc 里发送的数据包也是几十 KB 的大包，有 v 友对这个问题感兴趣愿意一起研究一下吗？
在 host 上运行 iperf3 发包时 sar 的输出如下：
d@develop:~/test$ sar -n DEV 1 | awk '/IFACE/ &amp

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 255. [V2EX] 使用 auto-cpufreq 平衡 Linux 性能功耗

**问题描述 / Problem Description**:
在 Fedora Linux 下，调整系统使用 auto-cpufreq 速度和功耗优化器。

搭载 Intel Core Ultra 7 255H 处理器的设备，离电状态进行日常网页浏览、写作和听音乐等轻度任务时的功耗表现，基本维持在 10W 左右。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 256. [V2EX] 我的硬盘 Memblaze Pblaze 5 Linux 下不识别，给 Linux 内核提交了补丁， AI 说有望被合并

**问题描述 / Problem Description**:
几年前在咸鱼上淘到几块国产硬盘，型号是 Memblaze Pblaze 516
Windows 下使用没有问题，但是在折腾 PVE 的时候遇到了问题，压根不识别这块硬盘。
然后我又试了好几个 Linux 发行版，某些旧内核版本反而能识别，
我根据 dmesg 信息和 pci 信息搜索，发现 bugzilla 上有类似的案例，
Bug 205679 - not able to recognize NVME's partition
https://bugzilla.kernel.org/show_bug.cgi?id=205679
我通过里面讨论的信息，自己写了个补丁（其实就加了 2 行设备信息）

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://bugzilla.kernel.org/show_bug.cgi?id=205679

---

#### 257. [V2EX] Linux nfs 客户端如何快速删除大量小文件

**问题描述 / Problem Description**:
linux 下有个程序每天在 NFS 共享目录（生成一个当天日期的文件夹）下缓存 100 万左右的文件，大小差不多 3-5T ，这个程序处理完成后可以删除，如何在 Linux 下快速删除它们呢。
按照网上的这个同步空目录的方法，差不多耗时 7 个小时。
rsync --delete-before -d -H -O --progress /tmp/empty/ 2026-04-02/

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 258. [V2EX] 写了个 Nautilus Extension: Copy File Path

**问题描述 / Problem Description**:
Gnome50/Debian 环境中测试通过的，方便我在 Nautilus 文件管理器中复制路径      AI 时代，软件可以按个人定制      https://github.com/wuruxu/nautilus-copypath

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://github.com/wuruxu/nautilus-copypath

---

#### 259. [V2EX] Linux /Ubuntu 上如何实现连接两个不同的 wifi 解决实际需求。

**问题描述 / Problem Description**:
背景：

自用电脑是联想小新 pro 14 ，装有 ubuntu24.04, 支持 wifi6
公司有 wifi A 和 wifi B ，wifi A 是国内的普通宽带，wifi B 是连接香港的专线。
服务器 ssh 连接限定了必须是使用 wifi A 
wifi B 由于是香港专线，可以自由访问谷歌等网站，无需翻墙。 使用 wifi A 则需要借助 Clash(虽然公司有订阅套餐)

目前我的需求是

指定某些软件/程序，例如是 teams,ssh 等使用 wifi A; 指定浏览器使用 Wifi A/B 

求助大佬们，我应该如何实现上述需求？是否需要增购 USB wifi ？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 260. [V2EX] 115 网盘如何多端稳定挂载？

**问题描述 / Problem Description**:
修复了存储状态不一致的问题，加强了稳定性
更新了安全提示



115 网盘的挂载功能存在一个严重限制：当你有两个 VPS 想挂载同一个 115 网盘账号时，你会发现：一边刚挂载成功，另一边就被踢下线。
这种报错，本质上是 115 网盘的防盗机制：当刷新 token 的时候会导致此应用获取的旧 token 失效。对于同一 app 的不同挂载，同样成立。 


如果没有防盗链：当有人窃取了你的 refreshtoken 之后，黑客就可以获取你的数据长达一年（除非你手动去吊销你的 token ，并重新获取） 这种方式诚然会提高安全性，但是在多端挂载的场景下反而成为了使用的阻碍。 

因此我搓了一个

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 261. [V2EX] Linux 桌面环境 orWM 推荐

**问题描述 / Problem Description**:
RT ，当前在用 kde plasma ，但是感觉设置项太多，我也不喜欢 QT ，想换一下
主要是想有鼠标时可以鼠标操作，出差时使用触控板进行操作，似乎 gnome 不错，但是不知道现在还稳定不，几年前用的时候动不动插件就用不了了....当然，我也只用一些基础插件。
有人用 hyprland 吗？操作体验怎么样，桌面似乎是不能显示文件吗？鼠标和触控板操作不知道怎么样，有没有老哥解答一下，我的机器是 thinkbook 14+ 2024 ultra7 版本

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 262. [V2EX] 如何解决 eBPF sockmap 重定向转发中背压缺失带来的 OOM ？

**问题描述 / Problem Description**:
我在尝试使用 eBPF 的 BPF_PROG_TYPE_SK_SKB 与 BPF_MAP_TYPE_SOCKHASH 实现 socket 的铰接转发，目标是基于 bpf_sk_redirect_hash 将一个 socket 的 ingress 队列数据转发到另一个 socket 的 egress 队列，但是在实际的吞吐量测试时出现了系统 OOM 。
具体的环境如下：

Linux Kernel 6.8
2 个 socket 所处网络接口不同，且 2 个网络接口带宽不一致，转发源 socket 所处接口 (测试用的 loopback) 带宽高于目标 socket 所处带宽
吞吐测试是在 loo

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 263. [V2EX] 还是要用 ubuntu

**问题描述 / Problem Description**:
过去一直用 windows 开发，编码问题，行尾问题，使用 docker 绑定目录也会有同步问题。


后来就转到 wsl 中开发，但是不好说是 wsl 的 bug 还是 docker 的 bug ，经常出现磁盘读写 100%，
磁盘完全占满后所有 app 都不能正常工作了。


然后就转 linux ，选的三个 mint ，debian/kde ，ubuntu
先用 live 模式尝试，ubuntu 出现了一点卡顿就放弃了，尝试 mint 发现官方网站上列了很多已知问题，
我不敢用，debian 暂时没有发现问题，就安装了，用了之后才发现这个 debian 反而经常出现 freeze 的情况

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 264. [V2EX] nfs mv 的操作是原子的么？ A 节点 move， B 节点要么完全可见，要么完全不可见？

**问题描述 / Problem Description**:
比如机器 A 、B 的/data 挂载了同一个 nfs 挂载点，A 机器/data 目录下有一个文件夹 a 下有 10000 个文件，我把/data/a 移动到/data/b ，对于机器 B 而言，如果节点 A 上已经看到 move 完成了，那么节点 B 上由于 nfs 异步延迟的存储，可能前几秒看不到这个移动的操作，过几秒之后可以看到/data/a 变成了/data/b ，那么存不存在一个中间状态，我能看到/data/b ，但是/data/b 下只有比如 2000 个文件

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 265. [V2EX] 求助 Linux 桌面环境软件

**问题描述 / Problem Description**:
马上要转过去了。麒麟信安 kylinSEC OS   arm ，看了下好像是类红帽的，rpm 包。昨晚翻吐了没找到几个软件。有经验的前辈推荐些常用软件吧。目前有 idea 、redis 、dbeaver ，没找到离线翻译的，有道官网没 arm 版。另外现在 idea 还能离线 2099 吗，好久没折腾了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 266. [V2EX] ubuntu 上有没有基于 OpenGL 的原生 3d 游戏

**问题描述 / Problem Description**:
记得很多年前玩过一款，通过 .deb 安装的，3D 飞行躲避障碍的，想在想不起来名字了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 267. [V2EX] ubuntu 下的风扇转速控制？

**问题描述 / Problem Description**:
家里的电脑装的 pc 用的水冷。
在 win 下面，因为装了厂商的驱动，貌似正常办公的时候，风扇转速很低，没有声音。但是 ubuntu 下面，貌似已启动就是高速。。。不知道各位佬们在 ubuntu 下面可以怎样也控制下显卡和水冷风扇的转速嘛？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 268. [V2EX] 求推荐 Ubuntu 好用的 ssh 工具

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 269. [V2EX] ubuntu 26.04 有人体验了吗, 有国内的可用镜像吗

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 270. [V2EX] 15 年前的 ubuntu 官方安装盘有人要么

**问题描述 / Problem Description**:
[有图有真相]( https://aifeixiang.feishu.cn/wiki/C6IcwFfMnirMX7kpz33cUASknDc)9.10 ，10.04, 10.10  整理书柜找到的，保存完好。 大学的时候申请的，没人要就扔掉了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://aifeixiang.feishu.cn/wiki/C6IcwFfMnirMX7kpz33cUASknDc)9.10

---

#### 271. [V2EX] 该装服务器了，装 Ubuntu24.04.2 还是 Ubuntu22.04.5

**问题描述 / Problem Description**:
预计要用个四五年，预计部署网站和 MCP 服务端，用最新的 24.04.2 还是上个稳定版本 22.04.5 ？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 272. [V2EX] ubuntu 加显卡后感觉动画卡顿

**问题描述 / Problem Description**:
升级之前使用 GTX 950 2G


升级成 GTX 950 2G + 4060TI16G 


xorg 配置系统使用 950 ，4060 留作炼丹


按 win 键时 950 负载很高，动画卡顿，加之前没有这个感觉


为啥不用 Wayland, vscode 在 wayland 下使用感受很差


vscode gpu 加速已经送了，不然显存要炸


求大佬解惑

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 273. [V2EX] vmware17 安装 ubuntu22.04.5，最后一步报错

**问题描述 / Problem Description**:
我的硬件是 e5-2697v4 双路，请问如何解决？具体情况，如图：

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 274. [V2EX] 求 Ubuntu 台式机指纹 USB 识别器推荐

**问题描述 / Problem Description**:
最近使用 Ubuntu 22.04 台式机作为主力机，需要一个指纹 USB 识别器，主要用于指纹登录和 sudo 密码验证。之前咸鱼过一个 Kensington VeriMark Desktop Fingerprint Key ，发现 libfprint 不支持，请问大佬们有推荐的吗？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 275. [V2EX] ubuntun 下 docker 拉取镜像失败，配置了镜像源，但是无效

**问题描述 / Problem Description**:
已在 daemon.json 配置了多个镜像源：
DaoCloud 镜像站： https://docker.m.daocloud.io
腾讯云公共镜像库： https://mirror.ccs.tencentyun.com
华为云镜像服务： https://developer.huaweicloud.com/dm/mirrors
1Panel 镜像源： https://docker.1panel.live
Unsee 镜像源： https://docker-0.unsee.tech
1ms.run 镜像源： https://docker.1ms.run
Azure 中国镜像： http://m

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://docker.m.daocloud.io

---

#### 276. [V2EX] 我的 ubantu 服务器是不是被人植入了恶意代码了

**问题描述 / Problem Description**:
我的 ubantu 服务器是不是被人植入了恶意代码。。。。
我上面只跑了我的博客，都是 nodejs ，nginx ，mysql 和 Let's Encrypt 证书管理，没有跑过其他服务。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 277. [V2EX] ubuntu 用 vbetool dpms off 了再 on 后，显示乱码

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 278. [V2EX] WIN11 访问 UBUNTU 的 webdav 记不住账号

**问题描述 / Problem Description**:
我之前由于/目录所有者换成了用户，没办法只好重装了电脑，安装的还是 UBUNTU24
开了 webdav 共享，在 WIN11 上面用映射的方式访问。
但是每次访问，默认登录的用户名都是微软账号，无论我怎么选择保存，都是这样，好像跟我登录 windows 的账号一样，可我在 webdav 上设置了用户名和密码。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 279. [V2EX] Linux 安装完系统后默认是安装好显卡驱动吗？

**问题描述 / Problem Description**:
以前安装 WINDOWS 系统后，开机第一件事是安装各种驱动，包括最重要的显卡驱动使用过 linux ，发现安装完系统后好像都是各种 sudo apt update,貌似都不需要安装各类驱动的说法，今天打开 AMD 的官网，才发现 AMD 官网就有提供显卡驱动，用 LINUX 这么久了，貌似以前就没有主动安装显卡驱动，安装完 LINUX 后都是开箱即用，几条命令更新后就开始使用了，汗。所以想问下，linux 全新安装完系统后不需要安装各类驱动吗，包括显卡驱动。最近用 Ubuntu ，发现文件夹经常会卡住没反应，是没安装驱动的锅吗

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 280. [V2EX] 闯了大祸,根目录权限变成我自己了。

**问题描述 / Problem Description**:
我的磁盘空间不够了，之前分区的时候没搞好，根目录给了 1.7T 一直闲置，为了下载一个 700 多 G 的文件，我简单的 mount 到了一个下载目录下，transmission 下载的时候报错说权限问题，我直接 chown -R uuair:www-data 了，我还纳闷，一个空目录，怎么会卡住了。。。结果 sudo 的时候发现错误，然后，./目录下大部分文件都不是 root 的了，尤其是/etc 下，所有的都是我了。
好了，现在怎么办？  
第一：/home文件夹下有 3.2T 的文件，我没有其他的硬盘可以备份。
第二：我运行了 12 个 docker ，其中有几个配置了很久，可能我自己都

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 281. [V2EX] 各大镜像站不再提供 Debian12 下载？

**问题描述 / Problem Description**:
今天很多国内镜像站（清华 中科大等）的 Debian 12 ISO 下载链接变成了 404 （例如 debian-cd 目录下的 12.x ISO ）。
据说是因为 Debian 13 今天正式成为 stable 
是不是我搞错了？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 282. [V2EX] Debian 26 届年会现在可以开始报名注册啦！

**问题描述 / Problem Description**:
大家好！
Debian 26 届年会现在可以开始报名注册啦！
https://debconf26.debconf.org/
这次年会在 阿根廷 的 圣达菲（ Santa Fe ） 举行。
（一）飞机
目前国内上海有到阿根廷首都布宜诺斯艾利斯的直飞航班（机场代码：EZE ），经停 新西兰 的 奥克兰。
全程 25 个多小时，全国联运。
去程（上海→布宜诺斯艾利斯）：MU745 ，每周一、周四执行，北京时间 02:00 从上海浦东机场起飞，当地时间 16:55 抵达。‌‌
回程（布宜诺斯艾利斯→上海）：MU746 ，每周二、周五执行，当地时间 02:00 起飞，北京时间次日 18:00 抵达。‌‌

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://debconf26.debconf.org/

---

#### 283. [V2EX] debian13 有必要升级吗？感觉 12 还能坚持好几年

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 284. [V2EX] Debian 龙芯 移植进度

**问题描述 / Problem Description**:
base-files_14_loong64.changes ACCEPTED into unstable Debian FTP Masters
dpkg_1.22.21_loong64.changes ACCEPTED into unstable Debian FTP Masters
make-dfsg_4.4.1-3_loong64.changes ACCEPTED into unstable Debian FTP Masters
binutils_2.45.50.20251209-1_loong64.changes ACCEPTED into unstable Debian FTP Mas

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 285. [V2EX] Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁

**问题描述 / Problem Description**:
Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁
https://www.reddit.com/r/zfs/comments/1oivqx1/debian_13_root_on_zfs_with_native_encryption_and/

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.reddit.com/r/zfs/comments/1oivqx1/debian_13_root_on_zfs_with_native_encryption_and/

---

#### 286. [V2EX] 香橙派 5Plus 小服务器已升级 Debian13

**问题描述 / Problem Description**:
香橙派 5Plus RK3588 16G ，作家庭服务器用的，内核是 6.1.43-rockchip-rk3588 。已升级 Debian13 ，先用着了，看看有没有问题。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 287. [V2EX] Debian 13 “trixie” released

**问题描述 / Problem Description**:
https://www.debian.org/News/2025/20250809
正式新闻终于出了

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.debian.org/News/2025/20250809

---

#### 288. [V2EX] 安装 debian 的时候如何跳过创建普通用户？

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 289. [V2EX] debian 12 的体验真的很糟糕

**问题描述 / Problem Description**:
各种小问题最让人受不了的是 ibus 输入法。无论我是清除本地数据文件，还是 remove 再 reinstall ，都解决不了这只是我的个案吗？看起来 debian 13 也快来了不然我都想切换到 fedora

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 290. [V2EX] debian12.8 的 preseed 自动安装方式，封装 iso 的正确方式？?

**问题描述 / Problem Description**:
先做了这些事情(debian-12.8.0-amd64-DVD-1.iso 是官网下载的)
apt install debian-cd isolinux genisoimage
mount -o loop /opt/mkiso/debian-12.8.0-amd64-DVD-1.iso /mnt
mkdir /opt/debian_custom
cp -r /mnt/* /opt/debian_custom/
cp /opt/preseed.cfg /opt/debian_custom/preseed.cfg
chmod +w /opt/debian_custom/isolinux/txt.c

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 291. [V2EX] Debian12 VNC 连接时怎么才能以 Root 的身份登录桌面环境

**问题描述 / Problem Description**:
已具备条件：
桌面环境已具备
Root 可以通过桌面环境正常登录
普通用户已经具备 sudo
防火墙没有开启
vncserver 搭建成功了，且普通用户能正常登录桌面环境，但是为普通用户身份
希望达成的目标：
以 vnc 的方式连接上 debian 后，能切换至 root 身份进行可视化操作（非终端命令切换）

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 292. [V2EX] 我成功申请成为 Debian 正式成员， id 是 atzlinux

**问题描述 / Problem Description**:
在中国大陆这边，目前还不到 10 个人。比印度少哈，目前 印度有 16 ，17 个吧。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 293. [V2EX] Debian 这个系统你们一般怎么读？

**问题描述 / Problem Description**:
我一般读：德编
有的人读：呆边
还听说有人就说大便系统。（戏谑说法）
今天听到有个人读：得（ dei3 ）变

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 294. [V2EX] 真心求教 Debian 双网卡如何指定出入站

**问题描述 / Problem Description**:
Debian12 双网卡 有各自网段和网关
如何指定 A 网卡入站 B 网卡出站呢
A 网卡有公网 ip 可以联通 B 网卡没有公网 ip
试了路由表还是搞不定 希望大佬指点

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 295. [V2EX] 现在的 gnome 这么难用了吗

**问题描述 / Problem Description**:
许久没用桌面了，昨天看有人炫耀 Ubuntu 22.04 的桌面，个人现在偏爱 Debian ，就用虚拟机下载安装了 Debian 12.5 ，桌面选的 gnome 。
进入桌面后显示了两个工作区，点击后直接全屏，然后要打开应用就要点击左上角活动-再点击屏幕下方启动台-再点击想要的应用，这操作链路也太长了吧。切换应用也是，点击左上角-再点已经打开的应用。
然后貌似多窗口不见了？我新建一个窗口但是不知道咋切换，各种操作都找出不来。
是现在流行这个我跟不上时代了吗，还是有啥新姿势，比如手势、快捷键我没掌握？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---
