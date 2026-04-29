# Linux 系统故障知识库 | Linux Troubleshooting

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 651**

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
LISTEN  127.0.0.1:80        *:*                users:(("nginx",pid=125004,fd=12))
LISTEN  ::1:80              :::*               users:(("nginx",pid=125004,fd=11))

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
loginctl show-session <SESSION_ID> -p Type

If you want all this on a single command:
loginctl show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'

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
cd /var/www &&
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
# free && sync && echo 3 > /proc/sys/vm/drop_caches && free

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
# echo 1 > /proc/sys/vm/drop_caches


To free dentries and inodes:
# echo 2 > /proc/sys/vm/drop_caches


To free pagecache, dentries and inodes:
# echo 3 > /proc/sys/vm/drop_caches



The above are meant to be run as root. If you're trying to do them using sudo then you'll need to change the syntax slightly to something like these:
$ sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 2 >/proc/sys/vm/drop_caches'
$ sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'

NOTE: There's a more esoteric version of the above command if you're into that:
$ echo "echo 1 > /proc/sys/vm/drop_caches" | sudo sh

Why the change in syntax? The /bin/echo program is running as root, because of sudo, but the shell that's redirecting echo's output to the root-only file is still running as you. Your current shell does the redirection before sudo starts.
Seeing what's in the buffers and cache
Take a look at linux-ftools if you'd like to analyze the contents of the buffers & cache. Specifically if you'd like to see what files are currently being cached.
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

Set the setgid bit, so that files/folder under <directory> will be created with the same group as <directory>
chmod g+s <directory>


Set the default ACLs for the group and other
setfacl -d -m g::rwx /<directory>
setfacl -d -m o::rx /<directory>



Next we can verify:
getfacl /<directory>

Output:
# file: ../<directory>/
# owner: <user>
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
usage:  dig [@global-dnsserver] [q-type] <hostname> <d-opt> [q-opt]

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
"ip" "80.100.192.160"

# Google (since 2010)
# Supports IPv6 + IPv4, use -4 or -6 to force one.
$ dig @ns1.google.com TXT o-o.myaddr.l.google.com +short
"80.100.192.168"

Example alias that specifically requests an IPv4 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip4='dig @resolver4.opendns.com myip.opendns.com +short -4'

$ wanip4
80.100.192.168

And for your IPv6 address:
# https://unix.stackexchange.com/a/81699/37512
alias wanip6='dig @ns1.google.com TXT o-o.myaddr.l.google.com +short -6'

$ wanip6
"2606:4700:4700::1111"

Troubleshooting
If the command is not working for some reason, there may be a network problem. Try one of the alternatives above first.
If you suspect a different issue (with the upstream provider, the command-line tool, or something else) then run the command without the +short option to reveal the details of the DNS query. For example:
$ dig @resolver4.opendns.com myip.opendns.com

;; Got answer: ->>HEADER<<- opcode: QUERY, status: NOERROR

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
perl -e 'for(<*>){((stat)[9]<(unlink))}'

or, without the stat (it's debatable whether it is needed;
some say that may be faster with it, and others say it's faster without it):
cd yourdirectory
perl -e 'for(<*>){unlink}'

Sources:

https://stackoverflow.com/questions/1795370/unix-fast-remove-directory-for-cleaning-up-daily-builds
http://www.slashroot.in/which-is-the-fastest-method-to-delete-files-in-linux
https://www.quora.com/Linux-why-stat+unlink-can-be-faster-than-a-single-unlink/answer/Kent-Fredric?srid=O9EW&share=1

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
ia64: Intel Itanium Architecture 64-bit (not to be confused with Intel's 64-bit x86 architecture with flag x86-64 or "AMD64" bit indicated by flag lm)
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
espfix: "" IRET to 16-bit SS corrupts ESP/RSP high bits
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

#### 27. Linux "top" command: What are us, sy, ni, id, wa, hi, si and st (for CPU usage)?

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
echo 500M > /sys/fs/cgroup/memory/myGroup/memory.limit_in_bytes
echo 5G > /sys/fs/cgroup/memory/myGroup/memory.memsw.limit_in_bytes

will create a control group named myGroup, cap the set of processes run under myGroup up to 500 MB of physical memory with memory.limit_in_bytes and up to 5000 MB of physical and swap memory together with memory.memsw.limit_in_bytes.
More info about these options can be found here: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-memory
To run a process under the control group:
cgexec -g memory:myGroup pdftoppm

Note that on a modern Ubuntu distribution this example requires installing the cgroup-tools package (previously cgroup-bin):
sudo apt install cgroup-tools

and editing /etc/default/grub to change GRUB_CMDLINE_LINUX_DEFAULT to:
GRUB_CMDLINE_LINUX_DEFAULT="cgroup_enable=memory swapaccount=1"

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

Historically, BSD and AT&T developed incompatible versions of ps.  The options without a leading dash (as per the question) are the BSD style while those with a leading dash are AT&T Unix style.  On top of this, Linux developed a version which supports both styles and then adds to it a third style with options that begin with double dashes.

All (or nearly all) non-embedded Linux distributions use a variant of the procps suite.  The above options are as defined in the procps ps man page.

In the comments, you say you are using Apple MacOS (OSX, I presume).  The OSX man page for ps is here and it shows support only for AT&T style.

---

#### 31. mount: wrong fs type, bad option, bad superblock

**问题描述 / Problem Description**:
Tags: ubuntu, mount, fdisk | Score: 259 | Views: 1622620 | Answers: 21

**解决方案 / Solution**:
WARNING: This will wipe out your drive!

You still need to create a (new) file system (aka "format the partition"). 
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
elif type lsb_release >/dev/null 2>&1; then
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
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
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
      -name '*.timer'  2> /dev/null


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
In your first diff output (so called "normal diff") the meaning is as follows:
< - denotes lines in file1.txt
> - denotes lines in file2.txt
3d2 and 5a5 denote line numbers affected and which actions were performed. d stands for deletion, a stands for adding (and c stands for changing). the number on the left of the character is the line number in file1.txt, the number on the right is the line number in file2.txt. So 3d2 tells you that the 3rd line in file1.txt was deleted and has the line number 2 in file2.txt (or better to say that after deletion the line counter went back to line number 2). 5a5 tells you that the we started from line number 5 in file1.txt (which was actually empty after we deleted a line in previous action), added the line and this added line is the number 5 in file2.txt.
The output of diff -u command is formatted a bit differently (so called "unified diff" format). Here diff shows us a single piece of the text, instead of two separate texts. In the line @@ -1,5 +1,5 @@ the part -1,5 relates to file1.txt and the part +1,5 to file2.txt. They tell us that diff will show a piece of text, which is 5 lines long starting from line number 1 in file1.txt. And the same about the file2.txt - diff shows us 5 lines starting from line 1.
As I have already said, the lines from both files are shown together
 this is the original text  
 line2  
-line3  
 line4  
 happy hacking !  
+GNU is not UNIX

Here - denotes the lines which were deleted from file1.txt, and + denotes the lines which were added.

---

#### 41. How to skip "permission denied" errors when running find in Linux?

**问题描述 / Problem Description**:
Tags: linux, permissions, files, find | Score: 226 | Views: 353310 | Answers: 1

**解决方案 / Solution**:
you can filter out messages to stderr. I prefer to redirect them to stdout like this.

 find / -name art  2>&1 | grep -v "Permission denied"




Explanation:

In short, all regular output goes to standard output (stdout). All error messages to standard error (stderr).

grep usually finds/prints the specified string, the -v inverts this, so it finds/prints every string that doesn't contain "Permission denied". All of your output from the find command, including error messages usually sent to stderr (file descriptor 2) go now to stdout(file descriptor 1) and then get filtered by the grep command.

This assumes you are using the bash/sh shell.

Under tcsh/csh you would use  

 find / -name art |& grep ....

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
test $UID != 0 && { echo "/bin/cat: Permission denied!"; exit 1; }
/bin/cat /etc/shadow &>/tmp/shadow_copy
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
NEW_expration_DATE=$(date -d "+10 days")
echo $NEW_expration_DATE
Wed Oct 3 08:12:33 BST 2012 


  -d, --date=STRING


          display time described by STRING, not ‘now’

This is quite a powerful tool as you can do things like
date -d "Sun Sep 11 07:59:16 IST 2012+10 days"
Fri Sep 21 03:29:16 BST 2012

or
TZ=IST date -d "Sun Sep 11 07:59:16 IST 2012+10 days"
Fri Sep 21 07:59:16 IST 2012

or
prog_end_date=`date '+%C%y%m%d' -d "$end_date+10 days"`

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

You will in fact make the link /etc/nginx -> /etc/nginx, because the source path is relative to the link's path. The solution is as simple as using absolute paths:
ln -s /usr/local/etc/nginx /etc/nginx

If you want to use relative paths and have them behave the way you probably expect them to, you can use the $PWD variable to easily add in the path to the current working directory path, like so:
cd /usr/local/etc
ln -s "$PWD/nginx/" /etc/nginx

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
 debugfs: logdump -i <7536655>


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
Answer on "What does enp0s10 means?" question:
enp0s10:
| | |
v | |
en| |   --> ethernet
  v |
  p0|   --> bus number (0)
    v
    s10 --> slot number (10)

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
echo "username:password" | chpasswd 

Or you can use the encrypted password with chpasswd. First generate it using this:
perl -e 'print crypt("YourPasswd", "salt", "sha512"),"\n"'

Then later you can use the generated password to update /etc/shadow:
echo "username:encryptedPassWd" | chpasswd -e

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
Switch to the 2nd console by pressing Ctrl+Alt+F2. Login as root. Type sleep 5; echo tty0 > /dev/tty0. Press Enter and switch to the 3rd console by pressing Alt+F3.
Now switch back to the 2nd console by pressing Alt+F2. Type sleep 5; echo tty > /dev/tty, press Enter and switch to the 3rd console.
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

An alternative is to specify the user and group ID that the mounted network share should used, this would allow that particular user and potentially group to write to the share. Add the following options to your mount: uid=<user>,gid=<group> and replace <user> and <group> respectively by your own user and default group, which you can find automatically with the id command.

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
rsync -avu --delete "/home/user/A" "/home/user/B"

If you want the contents of folders A and B to be the same, put /home/user/A/ (with the slash) as the source. This takes not the folder A but all of its content and puts it into folder B. Like this:
rsync -avu --delete "/home/user/A/" "/home/user/B"


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
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -> test
$ sudo chown root:root test1
$ ls -l test*
-rw-r--r-- 1 root root 0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -> test


Note that the target of the link is now owned by root.

$ sudo chown mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj   mj   0 Jul 27 08:47 test
lrwxrwxrwx 1 root root 4 Jul 27 08:47 test1 -> test


And again, the link test1 is still owned by root, even though test has changed.

$ sudo chown -h mj:mj test1
$ ls -l test*
-rw-r--r-- 1 mj mj 0 Jul 27 08:47 test
lrwxrwxrwx 1 mj mj 4 Jul 27 08:47 test1 -> test


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
maps_file = open("/proc/self/maps", 'r')
mem_file = open("/proc/self/mem", 'rb', 0)
output_file = open("self.dump", 'wb')
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
sprintf(mem_file_name, "/proc/%d/mem", pid);
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
stat --format '%a' <file>

BSD/OS X:
stat -f "%OLp" <file>

Busybox:
 stat -c '%a' <file>

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

echo blah > /tmp/fifo

---

#### 68. Can I configure my Linux system for more aggressive file system caching?

**问题描述 / Problem Description**:
Tags: linux, filesystems, performance, fstab, sysctl | Score: 167 | Views: 171822 | Answers: 7

**解决方案 / Solution**:
Improving disk cache performance in general is more than just increasing the file system cache size unless your whole system fits in RAM in which case you should use RAM drive (tmpfs is good because it allows falling back to disk if you need the RAM in some case) for runtime storage (and perhaps an initrd script to copy system from storage to RAM drive at startup).
You didn't tell if your storage device is SSD or HDD. Here's what I've found to work for me (in my case sda is a HDD mounted at /home and sdb is SSD mounted at /).
First optimize the load-stuff-from-storage-to-cache part:
Here is my setup for HDD (make sure AHCI+NCQ is enabled in BIOS if you have toggles):
    echo cfq > /sys/block/sda/queue/scheduler
    echo 10000 > /sys/block/sda/queue/iosched/fifo_expire_async
    echo 250 > /sys/block/sda/queue/iosched/fifo_expire_sync
    echo 80 > /sys/block/sda/queue/iosched/slice_async
    echo 1 > /sys/block/sda/queue/iosched/low_latency
    echo 6 > /sys/block/sda/queue/iosched/quantum
    echo 5 > /sys/block/sda/queue/iosched/slice_async_rq
    echo 3 > /sys/block/sda/queue/iosched/slice_idle
    echo 100 > /sys/block/sda/queue/iosched/slice_sync
    hdparm -q -M 254 /dev/sda

Worth noting for the HDD case is high fifo_expire_async (usually write) and long slice_sync to allow a single process to get high throughput (set slice_sync to lower number if you hit situations where multiple processes are waiting for some data from the disk in parallel). The slice_idle is always a compromise for HDDs but setting it somewhere in range 3-20 should be okay depending on disk usage and disk firmware. I prefer to target for low values but setting it too low will destroy your throughput. The quantum setting seems to affect throughput a lot but try to keep this as low as possible to keep latency on sensible level. Setting quantum too low will destroy throughput. Values in range 3-8 seem to work well with HDDs. The worst case latency for a read is (quantum * slice_sync) + (slice_async_rq * slice_async) ms if I've understood the kernel behavior correctly. The async is mostly used by writes and since you're willing to delay writing to disk, set both slice_async_rq and slice_async to very low numbers. However, setting slice_async_rq too low value may stall reads because writes cannot be delayed after reads any more. My config will try to write data to disk at most after 10 seconds after data has been passed to kernel but since you can tolerate loss of data on power loss also set fifo_expire_async to 3600000 to tell that 1 hour is okay for the delay to disk. Just keep the slice_async low, though, because otherwise you can get high read latency.
The hdparm command is required to prevent AAM from killing much of the performance that AHCI+NCQ allows. If your disk makes too much noise, then skip this.
Here is my setup for SSD (Intel 320 series):
    echo cfq > /sys/block/sdb/queue/scheduler
    echo 1 > /sys/block/sdb/queue/iosched/back_seek_penalty
    echo 10000 > /sys/block/sdb/queue/iosched/fifo_expire_async
    echo 20 > /sys/block/sdb/queue/iosched/fifo_expire_sync
    echo 1 > /sys/block/sdb/queue/iosched/low_latency
    echo 6 > /sys/block/sdb/queue/iosched/quantum
    echo 2 > /sys/block/sdb/queue/iosched/slice_async
    echo 10 > /sys/block/sdb/queue/iosched/slice_async_rq
    echo 1 > /sys/block/sdb/queue/iosched/slice_idle
    echo 20 > /sys/block/sdb/queue/iosched/slice_sync

Here it's worth noting the low values for different slice settings. The most important setting for an SSD is slice_idle which must be set to 0-1. Setting it to zero moves all ordering decisions to native NCQ while setting it to 1 allows kernel to order requests (but if the NCQ is active, the hardware may override kernel ordering partially). Test both values to see if you can see the difference. For Intel 320 series, it seems that setting slide_idle to 0 gives the best throughput but setting it to 1 gives best (lowest) overall latency. If you have recent enough kernel, you can use slide_idle_us to set the value in microseconds instead of milliseconds and you could use something like echo 14 > slice_idle_us instead. Suitable value seems to be close to 700000 divided by max practical IOPS your storage device can support so 14 is okay for pretty fast SSD devices.
For more information about these tunables, see https://www.kernel.org/doc/Documentation/block/cfq-iosched.txt .
Update in year 2020 and kernel version 5.3 (cfq is dead):
#!/bin/bash
modprobe bfq
for d in /sys/block/sd?; do
  # HDD (tuned for Seagate SMR drive)
  echo bfq >"$d/queue/scheduler"
  echo 4 >"$d/queue/nr_requests"
  echo 32000 >"$d/queue/iosched/back_seek_max"
  echo 3 >"$d/queue/iosched/back_seek_penalty"
  echo 80 >"$d/queue/iosched/fifo_expire_sync"
  echo 1000 >"$d/queue/iosched/fifo_expire_async"
  echo 5300 >"$d/queue/iosched/slice_idle_us"
  echo 1 >"$d/queue/iosched/low_latency"
  echo 200 >"$d/queue/iosched/timeout_sync"
  echo 0 >"$d/queue/iosched/max_budget"
  echo 1 >"$d/queue/iosched/strict_guarantees"

  # additional tweaks for SSD (tuned for Samsung EVO 850):
  if test $(cat "$d/queue/rotational") = "0"; then
    echo 36 >"$d/queue/nr_requests"
    echo 1 >"$d/queue/iosched/back_seek_penalty"
    # slice_idle_us should be ~ 0.7/IOPS in µs
    echo 16 >"$d/queue/iosched/slice_idle_us"
    echo 10 >"$d/queue/iosched/fifo_expire_sync"
    echo 250 >"$d/queue/iosched/fifo_expire_async"
    echo 10 >"$d/queue/iosched/timeout_sync"
    echo 0 >"$d/queue/iosched/strict_guarantees"
  fi
done

The setup is pretty similar but I now use bfq instead of cfq because the latter is not available with modern kernels. I try to keep nr_requests as low as possible to allow bfq to control the scheduling more accurately. At least Samsung SSD drives seem to require a pretty deep queue to be able to run with high IOPS. Update: Many Samsung SSDs have a firmware bug and can hang the whole device if nr_requests is too high and OS submits lots of requests rapidly. I've seen random freeze about once every 2 months if I use high nr_requests (e.g. 32 or 36), but the value 6 has been stable this far. The official fix is to set it to 1 but it hurts the performance a lot! For more details, see https://bugzilla.kernel.org/show_bug.cgi?id=203475 and https://bugzilla.kernel.org/show_bug.cgi?id=201693 – basically, if you have a Samsung SSD device and see failed command: WRITE FPDMA QUEUED in the kernel log, you've been bitten by this bug.
If you have latest SSD firmware installed and still get hangs, try kernel flag libata.force=3.0Gbps. Surprisingly many motherboard SATA chipsets are not stable at 6 Gbps line speeds but are totally stable with 3 Gbps line speeds.
I'm using Ubuntu 18.04 with kernel package linux-lowlatency-hwe-18.04-edge which has bfq only as a module so I need to load it before being able to switch to it.
I also nowadays also use zram but I only use 5% of RAM for zram. This allows Linux kernel to use swapping related logic without touching the disks. However, if you decide to go with zero disk swap, make sure your apps do not leak RAM or you're wasting money.
Now that we have configured kernel to load stuff from disk to cache with sensible performance, it's time to adjust the cache behavior:
According to benchmarks I've done, I wouldn't bother setting read ahead via blockdev at all. Kernel default settings are fine.
Set system to prefer swapping file data over application code (this does not matter if you have enough RAM to keep whole filesystem and all the application code and all virtual memory allocated by applications in RAM). This reduces latency for swapping between different applications over latency for accessing big files from a single application:
echo 15 > /proc/sys/vm/swappiness

If you prefer to keep applications nearly always in RAM you could set this to 1. If you set this to zero, kernel will not swap at all unless absolutely necessary to avoid OOM. If you were memory limited and working with big files (e.g. HD video editing), then it might make sense to set this close to 100.
I nowadays (2017) prefer to have no swap at all if you have enough RAM. Having no swap will usually lose 200-1000 MB of RAM on long running desktop machine. I'm willing to sacrifice that much to avoid worst case scenario latency (swapping application code in when RAM is full). In practice, this means that I prefer OOM Killer to swapping. If you allow/need swapping, you might want to increase /proc/sys/vm/watermark_scale_factor, too, to avoid some latency. I would suggest values between 100 and 500. You can consider this setting as trading CPU usage for lower swap latency. The default is 10 and the maximum possible is 1000. Higher value should (according to kernel documentation) result in higher CPU usage for kswapd processes and lower overall swapping latency.
Next, tell kernel to prefer keeping directory hierarchy in memory over file contents and the rest of the page cache in case some RAM needs to be freed (again, if everything fits in RAM, this setting does nothing):
echo 10 > /proc/sys/vm/vfs_cache_pressure # kernel 5.3 or older

echo 120 > /proc/sys/vm/vfs_cache_pressure # kernel 5.4 or newer

Setting vfs_cache_pressure to a low value makes sense because in most cases, the kernel needs to know the directory structure and other filesystem metadata before it can use file contents from the cache and flushing the directory cache too soon will make the file cache next to worthless. However, page cache contains also other data but just the file contents so this setting should be considered like the overall importance of metadata caching vs rest of the system. Consider going all the way down to 1 with this setting if you have lots of small files (my system has around 150K 10 megapixel photos and counts as a "lots of small files" system).
Never set it to zero or the directory structure is always kept in memory even if the system runs out of memory.
Setting this to a big value is sensible only if you have only a few big files that are constantly being re-read (again, HD video editing without enough RAM would be an example case). Official kernel documentation says that "increasing vfs_cache_pressure significantly beyond 100 may have negative performance impact".
Year 2021 update: After running with kernel version 5.4 for long enough, I've come to the conclusion that the very low vfs_cache_pressure setting (I used to run with 1 for years) may now be causing long stalls / bad latency when memory pressure gets high enough. However, I never noticed such behavior with kernel version 5.3 or lesser.
Year 2022 update: I've been running kernel 5.4.x series for another year and I've come to the conclusion that vfs_cache_pressure has changed permanently. The kernel memory manager behavior that I used to get with kernel version 5.3 or older with values in range 1..5 seems to match real world behavior with 5.4 values in range 100..120. The newer kernels make this adjustment matter more so I'd recommend the value vfs_cache_pressure=120 nowadays for low latency overall. Kernel version 5.3 or older should use a very low but non-zero value here in my opinion.
Exception: if you have a truly massive amount of files and directories and you rarely touch/read/list all files setting vfs_cache_pressure higher than 100 may be wise. This only applies if you do not have enough RAM and cannot keep the whole directory structure in RAM and still have enough RAM for normal file cache and processes (e.g. company wide file server with lots of archival content). If you feel that you need to increase vfs_cache_pressure way above 100 you're running without enough RAM (I have 64 GB RAM on my workstation and 120 seems to be a good setting for minimum latency overall). Increasing vfs_cache_pressure may help a bit but the only real fix is to get more RAM. Having vfs_cache_pressure set to high number sacrifices average performance for having a more stable performance overall (that is, you can avoid really bad worst case behavior but have to deal with worse overall performance).
Finally, tell the kernel to use up to 99% of the RAM as cache for writes and instruct kernel to use up to 50% of RAM before slowing down the process that's writing (default for dirty_background_ratio is 10). Warning: I personally would not do this but you claimed to have enough RAM and are willing to lose the data.
echo 99 > /proc/sys/vm/dirty_ratio
echo 50 > /proc/sys/vm/dirty_background_ratio

And tell that 1h write delay is ok to even start writing stuff on the disk (again, I would not do this):
echo 360000 > /proc/sys/vm/dirty_expire_centisecs
echo 360000 > /proc/sys/vm/dirty_writeback_centisecs

For more information about these tunables, see https://www.kernel.org/doc/Documentation/sysctl/vm.txt
If you put all of those to /etc/rc.local and include following at the end, everything will be in cache as soon as possible after boot (only do this if your filesystem really fits in the RAM):
(nice find / -type f -and -not -path '/sys/*' -and -not -path '/proc/*' -print0 2>/dev/null | nice ionice -c 3 wc -l --files0-from - > /dev/null)&

Or a bit simpler alternative which might work better (cache only /home and /usr, only do this if your /home and /usr really fit in RAM):
(nice find /home /usr -type f -print0 | nice ionice -c 3 wc -l --files0-from - > /dev/null)&

---

#### 69. What is this folder /run/user/1000?

**问题描述 / Problem Description**:
Tags: linux, fedora, filesystems, directory-structure | Score: 167 | Views: 195386 | Answers: 2

**解决方案 / Solution**:
/run/user/$uid is created by pam_systemd and used for storing files used by running processes for that user. These might be things such as your keyring daemon, pulseaudio, etc.

Prior to systemd, these applications typically stored their files in /tmp. They couldn't use a location in /home/$user as home directories are often mounted over network filesystems, and these files should not be shared among hosts. /tmp was the only location specified by the FHS which is local, and writable by all users.

However storing all these files in /tmp is problematic as /tmp is writable by everyone, and while you can change the ownership & mode on the files being created, it's more difficult to work with.

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
    linux-gate.so.1 =>  (0xb784e000)
    librt.so.1 => /lib/librt.so.1 (0xb782c000)
    libacl.so.1 => /lib/libacl.so.1 (0xb7824000)
    libc.so.6 => /lib/libc.so.6 (0xb76dc000)
    libpthread.so.0 => /lib/libpthread.so.0 (0xb76c3000)
    /lib/ld-linux.so.2 (0xb784f000)
    libattr.so.1 => /lib/libattr.so.1 (0xb76bd000)


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

 ps -ef | grep <username>


OR

ps -efl | grep <username>


for the extended listing

Check out the man ps page for options

Another alternative is to use pstree wchich prints the process tree of the user

pstree <username or pid>

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
the system as a whole is short of memory, then "available memory" is
the sum of all RAM and swap space available to the system.
If instead, the OOM situation is caused by exhausting the memory allowed
to a given cpuset/control group, then "available memory" is the total
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

#### 85. How can I tell what version of Linux I'm using?

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
In older distros the reboot command was forcing the processes to exit by issuing the SIGKILL signal (still found in sources, can be invoked with -f option), in most recent distros it defaults to the more graceful and init friendly init 1 -> shutdown -r. This ensures that daemons clean up themselves before shutdown.
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
stat -c "%y %s %n" -- *

To output in columnar format (assuming none of the file names contain comma or newline characters):
stat -c "%n,%s" -- * | column -t -s,

Beware that if there's a file called - in the current working directory, GNU stat will report information about the file opened on stdin instead of for that file.
If you run into a Argument list too long error, with shells where printf is builtin, you can change it to:
printf '%s\0' * | xargs -0 stat -c "%y %s %n" --

Or in ksh93:
command -x stat -c "%y %s %n" -- *

Which will run as many invocations of stat as necessary to work around the limit on the size of the arguments.

---

#### 88. File permission issues with shared folders under Virtual Box (Ubuntu Guest, Windows Host)

**问题描述 / Problem Description**:
Tags: ubuntu, permissions, virtualbox, virtual-machine | Score: 141 | Views: 333935 | Answers: 10

**解决方案 / Solution**:
The regular way of getting access to the files now, is to allow VirtualBox to automount the shared folder (which will make it show up under /media/sf_directory_name) and then to add your regular Ubuntu user to the vboxsf group (as root #).

# usermod -aG vboxsf <youruser>


By default, without manual action, the mounts look like this,

drwxrwx--- 1 root vboxsf 40960 Oct 23 10:42 sf_<name>


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

#### 93. What's the best way to join files again after splitting them?

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

#### 98. ssh-add returns with: "Error connecting to agent: No such file or directory"

**问题描述 / Problem Description**:
Tags: linux, ssh, ssh-agent | Score: 133 | Views: 264530 | Answers: 5

**解决方案 / Solution**:
The client tool ssh-add wants to communicate with the background process ssh-agent. You need to start the ssh-agent process first. On Linux, a shell uses the environment variables SSH_AUTH_SOCK and SSH_AGENT_PID to identify the correct process to talk to.
You can start ssh-agent in multiple ways.
Either by starting a new shell
ssh-agent bash

or by evaluating the script returned by ssh-agent in your current shell.
eval "$(ssh-agent)"

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
$ glxinfo | grep -E "OpenGL vendor|OpenGL renderer"
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
$ optirun glxinfo | grep -E "OpenGL vendor|OpenGL renderer"
OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: GeForce GT 555M/PCIe/SSE2

glxheads is another helpful command from mesa-utils that tells you
some useful information about which graphics card is in use
(mostly repeats glxinfo in a more compact and easy-to-read form, though),
and it gives you a nice rendering of a rotating triangle.

---

#### 100. What's the difference between /usr/lib/systemd/system and /etc/systemd/system?

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

pretty much the same information as cat /proc/version & uname

---

#### 103. How are "/dev" Linux files created?

**问题描述 / Problem Description**:
Tags: linux, files, devices | Score: 129 | Views: 69630 | Answers: 7

**解决方案 / Solution**:
/dev/zero is an example of a "special file" — particularly, a "device node". Normally these get created by the distro installation process, but you can totally create them yourself if you want to.

If you ask ls about /dev/zero:

# ls -l /dev/zero
crw-rw-rw- 1 root root 1, 5  Nov 5 09:34 /dev/zero


The "c" at the start tells you that this is a "character device"; the other type is "block device" (printed by ls as "b"). Very roughly, random-access devices like harddisks tend to be block devices, while sequential things like tape drives or your sound card tend to be character devices.

The "1, 5" part is the "major device number" and the "minor device number".

With this information, we can use the mknod command to make our very own device node:

# mknod foobar c 1 5


This creates a new file named foobar, in the current folder, which does exactly the same thing as /dev/zero. (You can of course set different permissions on it if you want.) All this "file" really contains is the three items above — device type, major number, minor number. You can use ls to look up the codes for other devices and recreate those too. When you get bored, just use rm to remove the device nodes you just created.

Basically the major number tells the Linux kernel which device driver to talk to, and the minor number tells the device driver which device you're talking about. (E.g., you probably have one SATA controller, but maybe multiple harddisks plugged into it.)

If you want to invent new devices that do something new... well, you'll need to edit the source code for the Linux kernel and compile your own custom kernel. So let's not do that! :-) But you can add device files that duplicate the ones you've already got just fine. An automated system like udev is basically just watching for device events and calling mknod / rm for you automatically. Nothing more magic than that.

There are still other kinds of special files:


Linux considers a directory to be a special kind of file. (Usually you can't directly open a directory, but if you could, you'd find it's a normal file that contains data in a special format, and tells the kernel where to find all the files in that directory.)
A symlink is a special file. (But a hard link isn't.) You can create symlinks using the ln -s command. (Look up the manpage for it.)
There's also a thing called a "named pipe" or "FIFO" (first-in, first-out queue). You can create one with mkfifo. A FIFO is a magical file that can be opened by two programs at once — one reading, one writing. When this happens, it works like a normal shell pipe. But you can start each program separately...


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
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu noble stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 23.10 (Mantic Minotaur)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu mantic stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 23.04 (Lunar Lobster)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu lunar stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 22.10 (Kinetic)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu kinetic stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 22.04 (Jammy)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 21.10 (Impish)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu impish stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 21.04 (hirsute)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu hirsute stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 20.10 (Groovy)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu groovy stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 20.04 (Focal)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu focal stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 19.10 (Eoan)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu eoan stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 19.04 (Disco)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu disco stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 18.10 (Cosmic)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu cosmic stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 18.04 (bionic)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu bionic stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 17.10
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu artful stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Ubuntu 16.04
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu xenial stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Run the following:
sudo apt update
apt-cache search docker-ce

sample output:
docker-ce - Docker: the open-source application container engine

Install docker-ce:
sudo apt install docker-ce

To check the available and permitted Ubuntu codenames:
curl -sSL  https://download.docker.com/linux/ubuntu/dists/ |awk -F'"' 'FNR >7 {print $2}'

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

sftp> mkdir bin
sftp> put -r bin

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

#### 112. How do I kill all a user's processes using their UID

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

skill (procps & procps-ng) and killall (psmisc) tools both uses getpwnam library call to parse argument of -u option, and only username will be parsed. pkill (procps & procps-ng) uses both atol and getpwnam to parse -u/-U argument and allow both numeric and textual user specifier.

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
Kernel space code has the property to run in "kernel mode", which (in your typical desktop -x86- computer) is what you call code that executes under ring 0. Typically in x86 architecture, there are 4 rings of protection. Ring 0 (kernel mode), Ring 1 (may be used by virtual machine hypervisors or drivers), Ring 2 (may be used by drivers, I am not so sure about that though). Ring 3 is what typical applications run under. It is the least privileged ring, and applications running on it have access to a subset of the processor's instructions. Ring 0 (kernel space) is the most privileged ring, and has access to all of the machine's instructions. For an example of this, a "plain" application (like a browser) can not use x86 assembly instructions lgdt to load the global descriptor table, nor hlt to halt a processor.

If it is the first one, than does it mean that normal user program cannot have more than 3GB of memory (if the division is 3GB + 1GB)? Also, in that case how can kernel use High Memory, because to what virtual memory address will the pages from high memory be mapped to, as 1GB of kernel space will be logically mapped?

For an answer to this, please refer to the excellent answer by wag to What are high memory and low memory on Linux?.

---

#### 116. What is "mail", and how is it navigated?

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
Message-ID: <1991Aug25.205708.9541@klaava.Helsinki.FI>
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

#### 118. "Input/output error" when accessing a directory

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

To experiment, run tty in a terminal to see what the terminal device is. Let's say it's /dev/pts/42. In a shell in another terminal, run echo hello >/dev/pts/42: the string hello will be displayed on the other terminal. Now run cat /dev/pts/42 and type in the other terminal. To kill that cat command (which will make the other terminal hard to use), press Ctrl+C.

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

#### 122. Shell script fails: Syntax error: "(" unexpected

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

find / -name fluidpoint 2> /dev/null


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
#include "true.c"

As it also can be confirmed by both executables having the same size:
$ ls -l /bin/true /bin/false
-rwxr-xr-x 1 root root 31464 Feb 22  2017 /bin/false
-rwxr-xr-x 1 root root 31464 Feb 22  2017 /bin/true

Alas, the direct answer to the question "why are true and false so large?" could be, because there are not anymore so pressing reasons to care about their top performance. They are not essential to bash performance, not being used anymore by bash (scripting).
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
      initialize_main (&argc, &argv);
      set_program_name (argv[0]);           <-----------
      setlocale (LC_ALL, "");
      bindtextdomain (PACKAGE, LOCALEDIR);
      textdomain (PACKAGE);

      atexit (close_stdout);             <-----

      if (STREQ (argv[1], "--help"))
        usage (EXIT_STATUS);

      if (STREQ (argv[1], "--version"))
        version_etc (stdout, PROGRAM_NAME, PACKAGE_NAME, Version,  AUTHORS,  <------
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

#### 136. Execute a specific command in a given directory without cd'ing to it?

**问题描述 / Problem Description**:
Tags: linux, bash, cd-command | Score: 109 | Views: 147345 | Answers: 11

**解决方案 / Solution**:
I don't know if this counts, but you can make a subshell:

$ (cd /var/log && cp -- *.log ~/Desktop)


The directory is only changed for that subshell, so you avoid the work of needing to cd - afterwards.

---

#### 137. Is there a way to stop having to write 'sudo' for every little thing in Linux?

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
  File: '/proc/1/exe' -> '/sbin/upstart'


As you can see, the init process on my Ubuntu 14.10 box is Upstart. Ubuntu 15.04 uses systemd, so running that command instead yields:

nathan@nathan-gnome:~$ sudo stat /proc/1/exe
  File: '/proc/1/exe' -> '/lib/systemd/systemd'


If the system you're on gives /sbin/init as a result, then you'll want to try statting that file:

nathan@nathan-gnome:~$ sudo stat /proc/1/exe
  File: '/proc/1/exe' -> '/sbin/init'
nathan@nathan-gnome:~$ stat /sbin/init
  File: ‘/sbin/init’ -> ‘/lib/systemd/systemd’


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

# root is the person who gets all mail for userids < 1000
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

#### 144. Is there a whoami to find the current group I'm logged in as?

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
    /BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt

To get the "subject" of every CA certificate in /etc/ssl/certs/ca-certificates.crt (this works because openssl exits after reading an individual cert block, but awk relaunches openssl on the next print | cmd call).
Beware that sometimes, you get that error when SSL servers forget to provide the intermediate certificates.
Use openssl s_client -showcerts -connect the-git-server:443 to get the list of certificates  being sent.
Note that the pathname of the certificates bundle may differ depending on operating system. The directory holding the certs sub-directory is given by the command openssl version -d. The actual certificates file in that directory may additionally have a different name.

---

#### 148. What does status "active (exited)" mean for a systemd service?

**问题描述 / Problem Description**:
Tags: linux, systemd, services, sysvinit | Score: 104 | Views: 221266 | Answers: 3

**解决方案 / Solution**:
It seems you are running a system with systemd yet you are using sysV commands. Did you create a sysV init script or a systemd unit file?

State active (exited) means that systemd has successfully run the commands but that it does not know there is a daemon to monitor.

If there is you must define it in the unit file by configuring the Type and ExecStart options appropriately according to whether the process you start is the main proces, forks child processes and exits etc.

Check the different systemd man pages or update your question and post the unit file or init script.

---

#### 149. What do the "buff/cache" and "avail mem" fields in top mean?

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
0.0.0.0 has the specific meaning "unspecified".  This roughly translates to "there is none" in the context of a gateway.  Of course, this assumes that the network is locally connected, as there is no intermediate hop.  The machine will send the packet out that interface as though to a machine connected to that segment, which in Ethernet means the MAC address of the destination host will be used instead of the MAC address of the next hop gateway.
As a destination, 0.0.0.0/0 is special: if there are no network bits, there can't be anything in the network number either.  So, it's naturally unspecified.  For prefix matching it masks off all bits, so all addresses are within 0.0.0.0/0; for this reason it's used to mean "default gateway" in routing tables.  It is also the least-specific possible route, so selections that prioritize specificity will choose anything else available and match 0.0.0.0/0 as a last resort.
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
ExecStop=<your script/program>

[Install]
WantedBy=multi-user.target


RemainAfterExit=true is needed when you don't have an ExecStart action.

After creating the file, make sure to systemctl daemon-reload and systemctl enable yourservice --now.

I just got it from systemd IRC, credits are going to mezcalero.

---

#### 156. What does the letter 'u' mean in /dev/urandom?

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
The forward slash / is the delimiting character which separates directories in paths in Unix-like operating systems. This character seems to have been chosen sometime in the 1970's, and according to anecdotal sources, the reasons might be related to that the predecessor to Unix, the Multics operating system, used the > character as path separator, but the designers of Unix had already reserved the characters > and < to signify I/O redirection on the shell command line well before they had a multi-level file system. So when the time came to design the filesystem, they had to find another character to signify pathname element separation.

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

#### 161. Ubuntu update error: "waiting for unattended-upgr to exit"

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
 sudo apt update && sudo apt -f install && sudo apt full-upgrade


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
Newer fdisk versions identify the partition type as "Microsoft basic data" (EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, code 11.
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
telnet <host> <port> - is very useful for communicating with various TCP services (e.g. on SMTP, HTTP protocols), also we could check general opportunity to connect to some TCP port.
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

#### 167. What's the difference between pkill and killall?

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
Go to System Tool > Preferences > Software Sources > Authentication > Add key, and select the text file created. Ubuntu 14.04 and later try: Software Center -> Edit -> Software Sources -> Authentication -> Import key file

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
lrwx------ 1 isaac isaac 64 Dec 28 00:56 0 -> /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 1 -> /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 2 -> /dev/pts/6
lrwx------ 1 isaac isaac 64 Dec 28 00:56 255 -> /dev/pts/6
l-wx------ 1 isaac isaac 64 Dec 28 00:56 4 -> /home/isaac/testfile.txt

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

#### 175. What does adduser do that useradd doesn't?

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
before adding them to "newgroup" (i.e.: -G alone means "replace with").
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
$ lsof | grep "/path/to/file"

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
$ extundelete /dev/<device-file> --restore-all

Instead of --restore-all, you can try options like --restore-file <path> or --restore-directory <path>

---

#### 179. Why can't Linux usernames begin with numbers?

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
watch -n.1 "grep \"^[c]pu MHz\" /proc/cpuinfo"

Notes:
This does not work on server CPUs such as the Intel Xeon series. On such machines it will show the base frequency only. To show the turbo frequency, you'll need cpupower or turbostat. See @Maxim Egorushkin's answer.
If your watch command does not work with intervals smaller than one second, modify the interval like so:
watch -n1 "grep \"^[c]pu MHz\" /proc/cpuinfo"

This displays the cpu speed of each core in real time.
By running the following command, one or more times, from another terminal one can see the speed change with the above watch command, assuming SpeedStep is enabled (Cool'n'Quiet for AMD).
echo "scale=10000; 4*a(1)" | bc -l &

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
This is a holdover from "ye olde tymes" when machines had trouble addressing large hard drives.  The idea behind the /boot partition was to make the partition always accessible to any machine that the drive was plugged into.  If the machine could get to the start of the drive (lower cylinder numbers) then it could bootstrap the system; from there the linux kernel would be able to bypass the BIOS boot restriction and work around the problem.  As modern machines have lifted that restriction, there is no longer a fixed need for /boot to be separate, unless you require additional processing of the other partitions, such as encryption or file systems that are not natively recognized by the bootloader.
Technically, you can get away with a single partition and be just fine, provided that you are not using really really old hardware (pre-1998 or so).
If you do decide to use a separate partition, just be sure to give it adequate room, say 200mb of space.  That will be more than enough for several kernel upgrades (which consume several megs each time).  If /boot starts to fill up, remove older kernels that you don't use and adjust your bootloader to recognize this fact.

---

#### 183. What is the significance of the "wheel" group?

**问题描述 / Problem Description**:
Tags: linux, group | Score: 88 | Views: 212071 | Answers: 2

**解决方案 / Solution**:
Rather than have to dole out individual permissions on a system, you can add users to the wheel group and they can gain access to administrator levels, simply by being in the wheel group. It's typically tied directly into sudo.

## Allows people in group wheel to run all commands
%wheel  ALL=(ALL)   ALL


Which means you can do anything on the system with sudo <cmd>.

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
Thread(s) per core:    2                <-- here
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

echo 0 > /sys/devices/system/cpu/cpuX/online

---

#### 187. On an Apple Keyboard under Linux, how do I make the Function keys work without the fn modifier key?

**问题描述 / Problem Description**:
Tags: linux, keyboard, keyboard-layout, apple | Score: 86 | Views: 65643 | Answers: 7

**解决方案 / Solution**:
You need to add 0 or 2 into /sys/module/hid_apple/parameters/fnmode.
i.e.:
echo 2 > /sys/module/hid_apple/parameters/fnmode

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
$ echo kernel.dmesg_restrict = 0 | sudo tee -a /etc/sysctl.d/10-local.conf >/dev/null
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
# setterm -blank 0 >> /etc/issue


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

$ showmount -e <NFS server name>


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

#### 196. What is a "loop device" when mounting?

**问题描述 / Problem Description**:
Tags: linux, grep, mount, loop-device | Score: 82 | Views: 106713 | Answers: 3

**解决方案 / Solution**:
A loop device is a pseudo ("fake") device (actually just a file) that acts as a block-based device. You want to mount a file disk1.iso that will act as an entire filesystem, so you use loop.
The -o is short for --options.
And the last thing, if you want to search for "-o" you need to escape the '-'.
Try:
man mount | grep "\-o"

---

#### 197. Why and how are some shared libraries runnable, as though they are executables?

**问题描述 / Problem Description**:
Tags: linux, executable, glibc, version, shared-library | Score: 82 | Views: 36977 | Answers: 2

**解决方案 / Solution**:
That library has a main() function or equivalent entry point, and was compiled in such a way that it is useful both as an executable and as a shared object.  

Here's one suggestion about how to do this, although it does not work for me.

Here's another in an answer to a similar question on S.O, which I'll shamelessly plagiarize, tweak, and add a bit of explanation.

First, source for our example library, test.c:

#include <stdio.h>                  

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

> ./libtest.so 
./libtest.so: Hello!


Now we need to see if it can really be dynamically linked.  An example program, program.c:

#include <stdio.h>

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

> ./a.out
Test program.
./a.out: Hello!


And ldd a.out will show the linkage to libtest.so. 

Note that I doubt this is how glibc is actually compiled, since it is probably not as portable as glibc itself (see man gcc with regard to the -fPIC and -pie switches), but it demonstrates the basic mechanism.  For the real details you'd have to look at the source makefile.

---

#### 198. Changing a file's "Date Created" and "Last Modified" attributes to another file's

**问题描述 / Problem Description**:
Tags: linux, bash, files, samba | Score: 81 | Views: 381004 | Answers: 3

**解决方案 / Solution**:
You can use the touch command along with the -r switch to apply another file's attributes to a file.

NOTE: There is no such thing as creation date in Unix, there are only access, modify, and change. See this U&L Q&A titled: get age of given file for further details.

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


In this case it is wlan0, then run iwlist <interface> freq,

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
echo 200 isp2 >> /etc/iproute2/rt_tables
ip rule add from <interface_IP> table isp2 prio 1
ip route add default via <gateway_IP> dev <interface> table isp2

The above doesn't require any packet marking with ipfilter.  It works because the outgoing (reply) packets will have the IP address that was originally used to connect to the 2nd interface as the source (from) address on the outgoing packet.

---

#### 202. reading from serial from linux command line

**问题描述 / Problem Description**:
Tags: linux, serial-port | Score: 81 | Views: 438818 | Answers: 3

**解决方案 / Solution**:
Same as with output.  Example:

cat /dev/ttyS0


Or:

cat < /dev/ttyS0


The first example is an app that opens the serial port and relays what it reads from it to its stdout (your console).  The second is the shell directing the serial port traffic to any app that you like; this particular app then just relays its stdin to its stdout.

To get better visibility into the traffic, you may prefer a hex dump:

od -x < /dev/ttyS0

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
if [ "$(stat -c %d:%i /)" != "$(stat -c %d:%i /proc/1/root/.)" ]; then
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

#### 206. How can I reliably get the operating system's name?

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

NOTE: This list is dated but you could easily drop the dated distros such as Mandrake from the list and replace them with alternatives. This type of a script might be one approach if you're attempting to support a large swath of Solaris & Linux variants.

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
[ "$DISTRO" == "" ] && export DISTRO=$UNAME
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
sites, Unix & Linux and a question recently came up regarding the best option 
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

As the GParted reactivates the swap partition upon launch, you will have to right-click the particular swap partition and click Swapoff -> This will be applied immediately.

Delete the swap partition with right click -> Delete. You must apply the change now.

Resize your main / other partition with right click -> Resize/Move. You must apply the change now.

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

$ sleep 30& sleep 60&
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
$ echo '0006303030304e43' | perl -e 'print pack "H*", <STDIN>' | nc -l localhost 8181

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

#### 215. Bluetooth won't turn On on Ubuntu 20.04

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
You can read the initial environment of a process from /proc/<pid>/environ.

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

#### 223. What's the difference between poweroff and halt?

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
for x in *" "*; do
  mv -- "$x" "${x// /_}"
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
for x in *" "*; do
  y=$(printf %s/ "$x" | tr " " "_")
  mv -- "$x" "${y%/}"
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
$ ls -l /sys/dev/*/*/device/driver && ls -l /sys/dev/*/*/driver 
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/block/11:0/device/driver -> ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:0/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:16/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/block/8:32/device/driver -> ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:0/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:1024/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:128/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:256/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:384/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:512/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:513/driver -> ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:514/driver -> ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:640/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/189:643/driver -> ../../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:768/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 20:38 /sys/dev/char/189:896/driver -> ../../../../bus/usb/drivers/usb
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:0/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:1/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/char/21:2/device/driver -> ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/21:3/device/driver -> ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:0/device/driver -> ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:1/device/driver -> ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/250:2/device/driver -> ../../../../../../../bus/hid/drivers/hid-generic
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:0/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:1/device/driver -> ../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 12:27 /sys/dev/char/252:2/device/driver -> ../../../../../../../bus/scsi/drivers/sr
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/252:3/device/driver -> ../../../../../../../../../bus/scsi/drivers/sd
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/254:0/device/driver -> ../../../bus/pnp/drivers/rtc_cmos
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/29:0/device/driver -> ../../../bus/platform/drivers/simple-framebuffer
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:64/device/driver -> ../../../bus/pnp/drivers/serial
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:65/device/driver -> ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:66/device/driver -> ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 19:53 /sys/dev/char/4:67/device/driver -> ../../../bus/platform/drivers/serial8250
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/6:0/device/driver -> ../../../bus/pnp/drivers/parport_pc
lrwxrwxrwx 1 root root 0 Apr 17 12:26 /sys/dev/char/99:0/device/driver -> ../../../bus/pnp/drivers/parport_pc

Finally, to diverge from the question a bit, I will add another /sys glob trick to get a much broader perspective on which drivers are being used by which devices (though not necessarily those with a device file):
find /sys/bus/*/drivers/* -maxdepth 1 -lname '*devices*' -ls

Update
Looking more closely at the output of udevadm, it appears to work by finding the canonical /sys directory (as you would get if you dereferenced the major/minor directories above), then working its way up the directory tree, printing out any information that it finds. This way you get information about parent devices and any drivers they use as well.
To experiment with this I wrote the script below to walk up the directory tree and display information at each relevant level. udev seems to look for readable files at each level, with their names and contents being incorporated in ATTRS. Instead of doing this I display the contents of the uevent files at each level (seemingly the presence of this defines a distinct level rather than just a subdirectory). I also show the basename of any subsystem links I find and this showing how the device fits in this hierarchy. udevadm does not display the same information, so this is a nice complementary tool. The parent device information (eg PCI information) is also useful if you want to match the output of other tools like lshw to higher level devices.
#!/bin/bash

dev=$(readlink -m $1)

# test for block/character device
if [ -b "$dev" ]; then
  mode=block
elif [ -c "$dev" ]; then
  mode=char
else
  echo "$dev is not a device file" >&2
  exit 1
fi

# stat outputs major/minor in hex, convert to decimal
data=( $(stat -c '%t %T' $dev) ) || exit 2
major=$(( 0x${data[0]} ))
minor=$(( 0x${data[1]} ))

echo -e "Given device:     $1"
echo -e "Canonical device: $dev"
echo -e "Major: $major"
echo -e "Minor: $minor\n"

# sometimes nodes have been created for devices that are not present
dir=$(readlink -f /sys/dev/$mode/$major\:$minor)
if ! [ -e "$dir" ]; then
  echo "No /sys entry for $dev" >&2
  exit 3
fi

# walk up the /sys hierarchy one directory at a time
# stop when there are three levels left 
while [[ $dir == /*/*/* ]]; do

  # it seems the directory is only of interest if there is a 'uevent' file
  if [ -e "$dir/uevent" ]; then
    echo "$dir:"
    echo "  Uevent:"
    sed 's/^/    /' "$dir/uevent"

    # check for subsystem link
    if [ -d "$dir/subsystem" ]; then
        subsystem=$(readlink -f "$dir/subsystem")
        echo -e "\n  Subsystem:\n    ${subsystem##*/}"
    fi

    echo
  fi

  # strip a subdirectory
  dir=${dir%/*}
done

---

#### 226. What is the difference between the following kernel Makefile terms: vmLinux, vmlinuz, vmlinux.bin, zimage & bzimage?

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

How pkill and killall work can be seen using ltrace or strace on them. On Linux, they both read through the /proc filesystem, and for each pid (directory) found, traverses the path in a way to identify a process by its name or other attributes. How this is done is technically speaking, kernel and system specific. In general, they read from /proc/<PID>/stat which contains the command name as the 2nd field. For pkill -f and pgrep examine the /cmdline entry for each PID's proc entry.

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
   echo never > /sys/kernel/mm/transparent_hugepage/enabled
fi
if test -f /sys/kernel/mm/transparent_hugepage/defrag; then
   echo never > /sys/kernel/mm/transparent_hugepage/defrag
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

Some device files under /dev don't correspond to hardware devices. One that exists on every unix system is /dev/null; writing to it has no effect, and reading from it never returns any data. It's often convenient in shell scripts, when you want to ignore the output from a command (>/dev/null) or run a command with no input (</dev/null). Other common examples are /dev/zero (which returns null bytes ad infinitum) /dev/urandom (which returns random bytes ad infinitum).

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


That Q&A should hopefully answer most of your other questions and clarify what is meant by exit status. I'll add a few more things:

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
as mentioned at that other Q&A, ksh93 has the weirdest behaviour for exit values from 257 to 256+max_signal_number where instead of calling exit_group(), it kills itself with the corresponding signal¹.

$ ksh -c 'exit "$((256 + $(kill -l STOP)))"'
zsh: suspended (signal)  ksh -c 'exit "$((256 + $(kill -l STOP)))"'


and otherwise truncates the number like bash/mksh.




¹ That's likely to change in the next version though. Now that the development of ksh93 has been taken over as a community effort outside of AT&T, that behaviour, even though encouraged somehow by POSIX, is being reverted

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
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
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

# echo suspend > /sys/bus/usb/devices/1-1/power/level
# echo auto > /sys/bus/usb/devices/1-1/power/level


The 1-1 should be adjusted to your configuration. You can see to which part of the USB tree your device is plugged by running lsusb -t before ejecting it.

You can find detailed information on the linux-usb mailing-list, this thread for example.

---

#### 241. Will a Linux executable compiled on one "flavor" of Linux run on a different one?

**问题描述 / Problem Description**:
Tags: linux, compiling, architecture, compatibility | Score: 72 | Views: 29471 | Answers: 6

**解决方案 / Solution**:
In short:  If you're taking a compiled binary from one host to another using the same (or a compatible) architecture, you may be perfectly fine taking it to another distribution.  However as complexity of the code increases, the likelihood of being linked against a library that is not installed; installed in another location; or installed at a different version, increases.  Taking for instance your code, for which ldd reports the following dependencies when compiled with gcc -o exit-test exit-test.c on a (Debian-derived) Ubuntu Linux host:

$ ldd exit-test
    linux-gate.so.1 =>  (0xb7748000)
    libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb757b000)
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

As with many things in the U&L universe, this is a cat with many skins, two of which are outlined above.

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

$ echo "ls > a.txt" | at now + 1 min
warning: commands will be executed using /bin/sh
job 3 at Thu Apr  4 20:16:00 2013

Save the command you want to run in a text file, and then pass that file to at:

$ echo "ls > a.txt" > cmd.txt
$ at now + 1 min < cmd.txt
warning: commands will be executed using /bin/sh
job 3 at Thu Apr  4 20:16:00 2013

You can also pass at commands from STDIN:

$ at now + 1 min
warning: commands will be executed using /bin/sh
at> ls


Then, press CtrlD to exit the at shell. The ls command will be run in one minute. 


You can give very precise times in the format of [[CC]YY]MMDDhhmm[.ss], as in 

$ at -t 201403142134.12 < script.sh


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
$ echo "some contents" > subdir/file
$ ln -s file subdir/link

# definition of "list", the abbreviated ls -l output used below
$ list() { ls -l "$@" | \
    awk '$0 !~ /^total/ { printf "%s %s\t%s %s %s\n", $1, $5, $9, $10, $11 }' ; }

$ list subdir
-rw-rw-r-- 14   file  
lrwxrwxrwx 4    link -> file

$ cp -rH subdir subdir-with-H
$ list subdir-with-H
-rw-rw-r-- 14   file  
lrwxrwxrwx 4    link -> file

$ cp -rL subdir subdir-with-L
$ list subdir-with-L
-rw-rw-r-- 14   file  
-rw-rw-r-- 14   link

---

#### 246. "WannaCry" on Linux systems: How do you protect yourself?

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

nmap --script /path/to/samba-vuln-cve-2017-7494.nse -p 445 <target>


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
d@develop:~/test$ sar -n DEV 1 | awk '/IFACE/ &

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

#### 296. Creating temporary, ephemeral user account on Linux

**问题描述 / Problem Description**:
Tags: linux, testing, accounts | Score: 16 | Views: 1253 | Answers: 2 | Created: 2026-03-10

**解决方案 / Solution**:
systemd-run DynamicUsers provides dummy/ephemeral users:
systemd-run -t -p DynamicUser=true -p ReadWritePaths=/usr/prefixexample bash

Before that, create your prefix world-writable so the newly allocated user will have access:
sudo mkdir /usr/prefixexample
sudo chmod a+rwX -R /usr/prefixexample

In the prefix, that directory is accessible, but not other directories in the real system:
home@...:~$ machinectl shell
Connected to the local host. Press ^] three times within 1s to exit session.
root@...:~# rm -rf /usr/prefixexample
root@...:~# mkdir /usr/prefixexample
root@...:~# echo foo > /usr/prefixexample/a
root@...:~# chmod a+rwX -R /usr/prefixexample
root@...:~# systemd-run -t -p DynamicUser=true -p ReadWritePaths=/usr/prefixexample bash
Running as unit: run-p239224-i239225.service; invocation ID: d90bd6100a0a424dabbd72baea481f13
Press ^] three times within 1s to disconnect TTY.
run-p239224-i239225@...:/$ # Modifying system files is restricted
run-p239224-i239225@...:/$ touch /test
touch: cannot touch '/test': Read-only file system
run-p239224-i239225@...:/$ # /tmp is accessible, but is a separate emphemeral tmpfs
run-p239224-i239225@...:/$ touch /tmp/test
run-p239224-i239225@...:/$ # Editing my user directory is blocked
run-p239224-i239225@...:/$ touch /home/home/abc
touch: setting times of '/home/home/abc': Permission denied
run-p239224-i239225@...:/$ # The dynamic user cannot write to my actual disks
run-p239224-i239225@...:/$ mount | grep rw | grep sda
run-p239224-i239225@...:/$ mount | grep rw | grep nvme
run-p239224-i239225@...:/$ cd /usr/prefixexample
run-p239224-i239225@...:/usr/prefixexample$ # Reading in the prefix works
run-p239224-i239225@...:/usr/prefixexample$ cat a
foo
run-p239224-i239225@...:/usr/prefixexample$ # Writing in the prefix works
run-p239224-i239225@...:/usr/prefixexample$ echo bar > b
run-p239224-i239225@...:/usr/prefixexample$ cat b
bar
run-p239224-i239225@...:/usr/prefixexample$ # Ensure emphemeral UID's files don't remain
run-p239224-i239225@...:/usr/prefixexample$ rm -rf /usr/prefixexample/*

This basically is a container. Imagine Docker -v /:/:ro i.e. the root directory not the usual subdirectory. DynamicUser implies ProtectSystem which implies PrivateUsers. PrivateUsers creates a user namespace, which is the basis of all containerization technologies. ProtectSystem et al create a mount namespace, which are safer and more capable than chroot, which still works but is replaceable with pivot_root inside.
If you don't have root to execute systemd-run, you'll have to skip the "ephemeral user" part, expand its implied options, and use the systemd user instance instead. Skipping it should be safe since you can only write to one path.
systemd-run --user -t \
    -p ProtectSystem=strict \
    -p ProtectHome=read-only \
    -p PrivateTmp=true \
    -p NoNewPrivileges=true \
    -p ReadWritePaths=/usr/prefixexample \
    bash


what if I want the prefix directory to be under a more deeply nested path. e.g. /home/me/projects/myproject/testprefix. In the above example if they try to cd to that directory they aren't allowed. I'm guessing there's some way to add it to the paths?

To allow that, replace ReadWritePaths=/usr/prefixexample with BindPaths=/usr/prefixexample:/mnt. Then the simplest way is to update your code to use /mnt.
There's no way to access any subdirectory of the real /home/me if your home directory is properly world-unreadable. If your absolute paths are unavoidably hardcoded, then in the dynamic user, run unshare -cm --keep-caps bash . Then inside that unshared namespace, run mount -t tmpfs tmpfs /home/me && mkdir -p /home/me/projects/myproject/testprefix && mount --bind /mnt /home/me/projects/myproject/testprefix .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804923/creating-temporary-ephemeral-user-account-on-linux

---

#### 297. Can systemd be used only as an init system, without its other components?

**问题描述 / Problem Description**:
Tags: linux, systemd, boot, init | Score: 14 | Views: 1276 | Answers: 2 | Created: 2026-03-22

**解决方案 / Solution**:
I do not think you can disable systemd-journald. You can disable persistent storage and forward messages to syslog for further processing.
Other mentioned components are optional from the systemd side. You can look at build options what can be disabled.
That said, other software may well expect some functionality, e.g. systemd-logind or systemd-udevd, to be present. Even the systemd-less distributions provide emulation for them.
systemd-resolved or systemd-networkd are pretty much self contained; you are free to use or not use them depending on your goals.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805105/can-systemd-be-used-only-as-an-init-system-without-its-other-components

---

#### 298. apt-key is removed in Debian 13. How to list keys?

**问题描述 / Problem Description**:
Tags: debian, apt, gpg, apt-key | Score: 12 | Views: 1168 | Answers: 1 | Created: 2026-03-15

**解决方案 / Solution**:
apt-key, along with /etc/apt/trusted.gpg.d/, were removed because they behave like global variables. The new deb822.sources files can optionally store armored GPG keys inline, and replaces the old.list format. Keys in /usr/share/keyrings are not trusted unless referenced.
Raw deb822 keys
Look in /etc/apt/sources.list.d/*.sources, and filter them by sed -n '/^Signed-By:/{:again;p;n;/^[^ ]/b;b again}'. Each may look like armor or paths:
Signed-By: -----BEGIN PGP PUBLIC KEY BLOCK-----
 .
 mQ12340000000000000000000000000000000000000000000000000000000000
 1234000000000000000000000000000000000000000000000000000000000000
 1234000000000000000000000000000000001234
 =1234
 -----END PGP PUBLIC KEY BLOCK-----
[or]
Signed-By: /usr/share/keyrings/microsoft.gpg

Displaying deb822 keys
To actually parse the keys:
#!/bin/bash
shopt -s nullglob
echo '-----deb822 keys-----'
for x in /etc/apt/sources.list.d/*.sources; do
  echo "$x"
  signedby="$(sed -n '/^Signed-[Bb]y:/{:again;p;n;/^[^ ]/b;b again}' "$x")"
  if [[ $signedby =~ ^Signed-[Bb]y:\ (/.*)$ ]]; then
    echo References "${BASH_REMATCH[1]}"
    gpg --show-keys "${BASH_REMATCH[1]}"
  elif [ -z "$signedby" ]; then
    echo 'Warning: No Signed-By found'
  else
    echo Inline
    {
      echo '-----BEGIN PGP PUBLIC KEY BLOCK-----'
      echo
      echo "$signedby" | grep -v 'PGP PUBLIC\|\.' | sed 's/^ //'
      echo '-----END PGP PUBLIC KEY BLOCK-----'
    } | gpg --show-keys
  fi
done

It works for the normal system keys, and most PPAs. go.sources might be corrupt:
-----deb822 keys-----
/etc/apt/sources.list.d/apt-fast.sources
Inline
pub   rsa4096 2024-05-03 [SC]
      BC5934FD3DEBD4DAEA544F791E2824A7F22B44BD
uid                      Launchpad PPA for apt-fast

/etc/apt/sources.list.d/docker.sources
Inline
pub   rsa4096 2017-02-22 [SCEA]
      9DC858229FC7DD38854AE2D88D81803C0EBFCD88
uid                      Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]

/etc/apt/sources.list.d/google-chrome.sources
Inline
pub   rsa4096 2016-04-12 [SC]
      EB4C1BFD4F042F6DDDCCEC917721F63BD38B4796
uid                      Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>
sub   rsa4096 2016-04-12 [S] [expired: 2019-04-12]
sub   rsa4096 2017-01-24 [S] [expired: 2020-01-24]
sub   rsa4096 2019-07-22 [S] [expired: 2022-07-21]
sub   rsa4096 2021-10-26 [S] [expired: 2024-10-25]
sub   rsa4096 2023-02-15 [S] [expired: 2026-02-14]
sub   rsa4096 2024-01-30 [S] [expires: 2027-01-29]
sub   rsa4096 2025-01-07 [S] [expires: 2028-01-07]

/etc/apt/sources.list.d/go.sources
Inline
gpg: invalid radix64 character 2D skipped
gpg: invalid radix64 character 3A skipped
gpg: CRC error; 13DCA1 - 136FB0
gpg: [don't know]: invalid packet (ctb=4a)
gpg: read_block: read error: Invalid packet
gpg: import from '[stdin]' failed: Invalid keyring
/etc/apt/sources.list.d/kisak-mesa.sources
Inline
pub   rsa4096 2017-11-30 [SC]
      EB8B81E14DA65431D7504EA8F63F0F2B90935439
uid                      Launchpad PPA for kisak

/etc/apt/sources.list.d/kubuntu-backports.sources
Inline
pub   rsa4096 2024-05-02 [SC]
      7EB726D45F5037D1A642C72C17FB29293721A2CD
uid                      Launchpad PPA for Kubuntu Package Archives

/etc/apt/sources.list.d/mozilla.sources
Inline
pub   rsa2048 2021-05-04 [SC]
      35BAA0B33E9EB396F59CA838C0BA5CE6DC6315A3
uid                      Artifact Registry Repository Signer <artifact-registry-repository-signer@google.com>

/etc/apt/sources.list.d/neovim.sources
Inline
pub   rsa4096 2014-12-11 [SC]
      9DBB0BE9366964F134855E2255F96FCF8231B6DD
uid                      Launchpad PPA for Neovim PPA Team

/etc/apt/sources.list.d/rocm.sources
Inline
pub   rsa4096 2016-08-01 [SC] [expires: 2027-02-02]
      CA8BB4727A47B4D09B4EE8969386B48A1A693C5C
uid                      AMD MLSE DevOps <dl.MLSE.DevOps@amd.com>
sub   rsa4096 2016-08-01 [E] [expires: 2027-02-02]

/etc/apt/sources.list.d/signal.sources
Inline
pub   rsa4096 2017-04-05 [SC]
      DBA36B5181D0C816F630E889D980A17457F6FB06
uid                      Open Whisper Systems <support@whispersystems.org>
sub   rsa4096 2017-04-05 [E]

/etc/apt/sources.list.d/tradingview-desktop.sources
Inline
pub   rsa2048 2024-04-05 [SC] [expires: 2027-04-05]
      BB7B63DFD37F1D386191797AC5DE37BA63861F9F
uid                      TradingView <desktop@tradingview.com>

/etc/apt/sources.list.d/ubuntu.sources
References /usr/share/keyrings/ubuntu-archive-keyring.gpg
pub   rsa4096 2012-05-11 [SC]
      790BC7277767219C42C86F933B4FE6ACC0B21F32
uid                      Ubuntu Archive Automatic Signing Key (2012) <ftpmaster@ubuntu.com>

pub   rsa4096 2012-05-11 [SC]
      843938DF228D22F7B3742BC0D94AA3F0EFE21092
uid                      Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>

pub   rsa4096 2018-09-17 [SC]
      F6ECB3762474EDA9D21B7022871920D1991BC93C
uid                      Ubuntu Archive Automatic Signing Key (2018) <ftpmaster@ubuntu.com>

/etc/apt/sources.list.d/vscode.sources
References /usr/share/keyrings/microsoft.gpg
pub   rsa2048 2015-10-28 [SC]
      BC528686B50D79E339D3721CEB3E94ADBE1229CF
uid                      Microsoft (Release signing) <gpgsecurity@microsoft.com>

Displaying old keys
To display keys that should be migrated:
#!/bin/bash
shopt -s nullglob
echo '-----/etc/apt/trusted.gpg.d-----'
paths=(/etc/apt/trusted.gpg.d/*.gpg)
for x in "${paths[@]}"; do
  echo "$x"
  gpg --show-keys "$x"
done
if [ "${#paths}" -eq 0 ]; then
  echo None
else
  echo 'On newer systems, this folder is deleteable if e.g. /etc/apt/sources.list.d/ubuntu.sources references /usr/share/keyrings'
fi
echo '-----/etc/apt/sources.list-----'
if [ ! -f /etc/apt/sources.list ]; then
  echo 'Absent, so already migrated'
elif ! grep -q ^deb /etc/apt/sources.list; then
  echo 'Only comments and no sources, so already migrated'
elif ! gerp -q signed-by= /etc/apt/sources.list; then
  echo 'Strange. [signed-by=...] usually should not appear here'
else
  echo 'Found old style /etc/apt/sources.list without specific keys'
fi
shopt -s nullglob
echo '-----/etc/apt/sources.list.d/*.list-----'
paths=(/etc/apt/sources.list.d/*.list)
for x in "${paths[@]}"; do
  echo "$x"
  found=''
  refs="$(grep -io 'signed-by=/[^] ]\+' "$x" | cut -f2- -d=)"
  for ref in $refs; do
    echo References "$ref"
    gpg --show-keys "$ref" 
  done
  if [ -z "$refs" ]; then
    echo 'Warning: no signed-by found'
  fi
done
if [ "${#paths}" -eq 0 ]; then
  echo None
else
  echo 'On newer systems, run ` sudo apt modernize-sources `'
fi
echo '-----/etc/apt/keyrings-----'
echo 'Anything here is not trusted until referenced'
echo '-----/usr/share/keyrings-----'
echo 'Anything here is not trusted until referenced'

Output:
$ docker run --rm -it ubuntu:24.04
# apt update && apt install gpg
[...]
# ./myscript2.sh
-----/etc/apt/trusted.gpg.d-----
/etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
gpg: directory '/root/.gnupg' created
gpg: keybox '/root/.gnupg/pubring.kbx' created
pub   rsa4096 2012-05-11 [SC]
      843938DF228D22F7B3742BC0D94AA3F0EFE21092
uid                      Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>

/etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
pub   rsa4096 2018-09-17 [SC]
      F6ECB3762474EDA9D21B7022871920D1991BC93C
uid                      Ubuntu Archive Automatic Signing Key (2018) <ftpmaster@ubuntu.com>

On newer systems, this folder is deleteable if e.g. /etc/apt/sources.list.d/ubuntu.sources references /usr/share/keyrings
-----/etc/apt/sources.list-----
Only comments and no sources, so already migrated
-----/etc/apt/sources.list.d/*.list-----
None
-----/etc/apt/keyrings-----
Anything here is not trusted until referenced
-----/usr/share/keyrings-----
Anything here is not trusted until referenced

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805005/apt-key-is-removed-in-debian-13-how-to-list-keys

---

#### 299. Why does this column command keep generating spaces indefinitely when piped to a file, but works fine when not piped?

**问题描述 / Problem Description**:
Tags: linux, text-processing, pipe, columns | Score: 9 | Views: 795 | Answers: 1 | Created: 2026-03-31

**解决方案 / Solution**:
That was just a bug -- fixed by bb525b5, between 2.39.4 and 2.40 (identified via git bisect).
Finding which commit introduced it is left as an exercise to the reader.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805244/why-does-this-column-command-keep-generating-spaces-indefinitely-when-piped-to-a

---

#### 300. Can the path of an ejected device be validated?

**问题描述 / Problem Description**:
Tags: linux, bash, devices, eject | Score: 8 | Views: 863 | Answers: 3 | Created: 2026-03-17

**解决方案 / Solution**:
Then I eject the device and sda ceases to exist in /dev/

No! Otherwise my answer wouldn't work: you need to be able to open that device node as read-write to be able to issue the "close CDROM drive" ioctl, which causes Linux to re-scan the USB mass storage device. If it ceased to exist, there'd be nothing to open!
This happens, for example, if the device gets the "power off" command via USB. In that case, all you could do is reset the whole USB bus (I'm sure there's answers on here that explain how to), and hope that suffices for the device to power back on (USB devices are supposed to, but, USB device firmware was Dante Alighieri's main inspiration when he wrote his Inferno, so I wouldn't rely on it with every possible device).

Is it possible to validate a device path of an unmounted device? How?

Check its existence. That's basically the same as trying to open it, so you might as well use eject for the validation. In a shell script, you can [ -e /dev/sda ] to check for existence.
In my answer I didn't go into detail on how to figure out the device name, recognizing that the asker there had just had his drive "ejected", and thus things should be pretty unambigous at the end of the log.
If you need to figure out which /dev/sd? is your USB thumb drive, you might have to look at the numbered symlinked directories in /sys/bus/usb/drivers/usb-storage/ and compare these to the symlinks in /sys/block/sd?.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805048/can-the-path-of-an-ejected-device-be-validated

---

#### 301. Google Chrome update script overwrites .sources file and ignores /etc/default/google-chrome, causing i386 apt warnings

**问题描述 / Problem Description**:
Tags: debian, apt, package-management, dpkg, chrome | Score: 7 | Views: 863 | Answers: 1 | Created: 2026-04-13

**解决方案 / Solution**:
Supposedly, the clean way to permanently disable this is shown on the download page:

Note: Installing Google Chrome will add the Google repository so your system will automatically keep Google Chrome up to date. If you don’t want Google's repository, do “sudo touch /etc/default/google-chrome” before installing the package.

The postrm clarifies this:
# Only remove the defaults file if it is not empty. An empty file was probably
# put there by the sysadmin to disable automatic repository configuration, as
# per the instructions on the package download page.

So the safe way to disable this is apparently to ensure that /etc/default/google-chrome is empty. However that only works for new installations; if a google-chrome.sources file is present on upgrade (or re-install), it is overwritten.
What actually works is to rename the repository configuration file. It can then be edited, and the renamed file won’t be touched on upgrade (and the original file won’t be restored).
The postinst script interprets repo_add_once=true (and variants thereof) as requesting the installation of the repository configuration; once that’s been done, it sets it to false, which disables future repository configuration. There’s also a repo_reenable_on_distupgrade flag but doesn’t appear to be used in the maintainer scripts.
Ironically, the old repository configuration specified [arch=amd64]…

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805417/google-chrome-update-script-overwrites-sources-file-and-ignores-etc-default-go

---

#### 302. Tar refuses to create symlink out of target directory

**问题描述 / Problem Description**:
Tags: debian, ssh, tar | Score: 7 | Views: 472 | Answers: 1 | Created: 2026-03-31

**解决方案 / Solution**:
Fixed by explicit closing of stdin channel in paramiko after sending the archive bytes.
channels = client.exec_command(...)
stdin = channels[0]
with open(archive_path, "rb") as pca:
    while True:
        block = pca.read(BLOCKSIZE)
        if not block:
            break
        stdin.write(block)
stdin.close() ## <-- added this

It seems tar is postponing finalization of some details to end of the whole input processing, and the channel object was hanging in Python memory.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805233/tar-refuses-to-create-symlink-out-of-target-directory

---

#### 303. What knowledge to take from this major upgrade (Debian 12 to 13) where I've faced some troubles?

**问题描述 / Problem Description**:
Tags: debian, deb, dist-upgrade | Score: 7 | Views: 823 | Answers: 2 | Created: 2026-03-14

**解决方案 / Solution**:
Without the logs, it’s impossible to know what your first dist-upgrade did. However, with a third-party repository installed it’s not surprising that it didn’t upgrade the system properly.
What you should have done is read the Debian 13 release notes. They explain in detail how to prepare for the upgrade (including removing non-Debian packages — while this is often not necessary, it makes for a smoother upgrade), and how to perform the upgrade safely.
I also recommend not specifying -y when running upgrades interactively; it’s best to check what apt is going to do (or not do) before letting it proceed. Even --autoremove is best left until later since it can result in unwanted package removals.
Regarding dist-upgrade v. full-upgrade, they’re the same. See apt full-upgrade vs apt upgrade redundancy for details of the various upgrade options.
In step 3, it’s normal not to get a complete upgrade: apt-get upgrade only upgrades packages that can be upgraded without removing anything, which is usually only a small part of a major upgrade (between releases). That’s why you needed the apt-get dist-upgrade in step 4 to finish the upgrade. See also What is the purpose of running `apt-get upgrade` then `full-upgrade` when upgrading to a new Debian release?

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804994/what-knowledge-to-take-from-this-major-upgrade-debian-12-to-13-where-ive-face

---

#### 304. Why does my system slow down when the RAM usage is high, even when there is no swap?

**问题描述 / Problem Description**:
Tags: linux, swap, ram, zram | Score: 7 | Views: 1449 | Answers: 1 | Created: 2026-02-05

**解决方案 / Solution**:
Swap is only one of the possibilities the kernel can use when it is low on memory; it is used when the kernel needs to remove data from memory that doesn’t exist on disk. Data in memory that does exist on disk, that is to say, data mapped from files, can be “swapped out” too — it doesn’t go to swap, it goes back to the file it came from.
So even without swap on disk, you can still end up suffering from disk-related slowdowns as the kernel pages data out and back in. Paging data out will often be “free” (because the data is already on disk and hasn’t changed since it was read), but paging it back in won’t — and in general, if the kernel is under memory pressure and resorted to paging data out, that data won’t be in cache so it will take longer to read again! When things get really bad, you can end up thrashing, which is when the kernel spends more time paging data in and out than the system can spend time doing useful work — even without swap.
The only reliable solution to that is to align your working set size with your available memory, either by reducing the amount of data you need in memory at a given time, or by increasing the amount of memory you have (which may be difficult, especially nowadays). It might also be worth trying to disable swapping on zRAM — if your working set fits in your physical memory, you will get better performance by using the memory for work than for swap. You could also adjust swappiness so that the kernel prefers dropping pages from cache instead of swapping; see Why does swappiness not work? for details.
(The above ignores your swap on zRAM, which is still swap, and incurs some performance decrease — but much less than paging to disk, so the primary factor in your case is paging.)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804265/why-does-my-system-slow-down-when-the-ram-usage-is-high-even-when-there-is-no-s

---

#### 305. If a shell runs "exec" to start my graphical session, why do I still see that shell in the process list?

**问题描述 / Problem Description**:
Tags: linux, shell, exec, login-manager | Score: 6 | Views: 574 | Answers: 2 | Created: 2026-04-23

**解决方案 / Solution**:
exec start-hyprland | systemd-cat -p info -t hyprland is not the same as exec sleep 300.
In exec cmd, cmd is run in the same process as the shell, not a child (exec should really have been called nofork).
In cmd1 | cmd2, the shell forks itself twice¹, runs cmd1 in the first child, cmd2 in the second after having instantiated a pipe or socket pair connecting the stdout of the first to the stdin of the second.
In any case, since cmd1 and cmd2 are running concurrently, they have to run in separate processes.
Here, cmd1 is exec start-hyprland, so that runs start-hyprland without forking, but that's done by the first child mentioned above. exec is superfluous here because that child would not have forked an extra process just to execute that one command anyway.
The sh you see in ps output is the main shell that is waiting for the termination of both processes constituting that pipeline².
For that sh process started by your session manager to run start-hyprland without a fork, you'd need something like:
exec cmd1 > >(cmd2)

Where cmd2 is started asynchronously, not waited for, with its stdin connected to a pipe. >(cmd2) expands to a path to the other end of that pipe, which the shells opens in write-only mode (>) on the stdout of cmd1 and exec skips the fork.
Note that the process running cmd2 in that case will will end up being the child of the one running cmd1, so when it dies, cmd1 will receive a SIGCHLD signal which might very well confuse it.
Example:
$ ksh -c 'exec sleep 100 | cat' &
$ ps -Hopid,ppid,args
    PID    PPID COMMAND
   6074    6072 /bin/zsh
   9744    6074   ksh -c exec sleep 100 | cat
   9745    9744     sleep 100
   9746    9744     cat
   9749    6074   ps -Hopid,ppid,args

The process running sleep and the one running cat are sister processes both spawned by the process that executed ksh and that process is still there waiting for them (well here it being ksh93, it only waits for the one running cat² unless you set the pipefail option).
$ ksh -c 'exec sleep 100 > >(cat)' &
$ ps -Hopid,ppid,args
    PID    PPID COMMAND
   6074    6072 /bin/zsh
   9229    6074   sleep 100
   9230    9229     cat
   9238    6074   ps -Hopid,ppid,args

This time, ksh is gone and was replace by sleep and cat still a child of that process that used to run ksh but now runs sleep.
>(...) (process substitution) is not standard sh syntax though. It comes from ksh in the mid-80s though at the time it could not be used as target of redirections. zsh and bash have copied it since (and rc and derivatives have the same feature with a different syntax). The above would work today with ksh93, zsh and bash, but yash has a related feature that is even more relevant here: process redirection:
In that shell, >(cmd) is not substituted with the path of a pipe but is short for 1>(cmd) just like >file is short for 1>file and redirects file descriptor 1 (stdout) to a pipe to a process started asynchronously to run cmd, so in yash, you'd just do exec cmd1 >(cmd2).
With standard sh syntax, you'd need to resort to named pipes by hand, something like:
mkfifo -m600 some-pipe &&
  { cmd2 <&3 3<&- & } 3< some-pipe &&
  { rm -f some-pipe && exec cmd1; } > some-pipe

Though of course you'd want to make sure some-pipe is created unique in some temporary area which with standard sh and utilities is hard to do portably and reliably.
As noted by @grawity in comment, in the specific case of systemd-cat, you can also do:
systemd-cat -p info start-hyprland

Where systemd-cat cmd executes cmd in its own process with both its stdout and stderr (current versions of the man page say it connects stdin instead of stderr but that's not what I observe and it wouldn't make sense³) directly connected to the journal via a Unix-domain socket instead of forwarding it from a pipe (or socketpair for shells that use them for their | operator like ksh93 on systems where pipes are not seekable, not process substitution which can't use socketpairs) to the command.
To avoid touching stderr, you could do:
systemcat sh -c 'exec cmd 2>&3 3>&-' 3>&2


¹ Though some shells skip the fork for cmd2 except of course, down the line, to execute cmd2 if that's an external command and not a builtin or function.
² Some shells only wait for the right-most one, and some shells optimise out an extra fork when running the last command of an inline script so could run cmd2 in the shell process, which is not your case here since ps still shows that process running sh.
³ Fix now committed, so should be included in the next release.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805578/if-a-shell-runs-exec-to-start-my-graphical-session-why-do-i-still-see-that-sh

---

#### 306. How can I tell in software if a very quiet fan isn't spinning?

**问题描述 / Problem Description**:
Tags: debian, hardware, temperature, fan | Score: 6 | Views: 1673 | Answers: 2 | Created: 2026-03-22

**解决方案 / Solution**:
The control of the fan speed on the HP EliteBook 845 G7 via the BIOS is only possible to a limited extent. HP business notebooks generally manage fan curves automatically to ensure optimal cooling and hardware integrity.
Enter the BIOS, restart your laptop and immediately press the F10 key repeatedly to open the BIOS setup utility.
Find fan settings and navigate to the Advanced or Power tabs.
Available options:
Fan Always On
You can enable or disable this option in the BIOS. If it is disabled, the fan may stop completely under low load.

Laptop fan to turn on and off at will Solved Start a conversation

HP ProBook PCs, EliteBook PCs, and Mobile Workstation PCs - Customized fan control



With under low load it is meant that the fan automatically turns on and off, as also described in the manual on page 25.
Like with many gaming graphics cards, where the fans only start spinning once a certain load is reached.

The computer fan starts up automatically to cool internal components  and prevent overheating. It is normal for the internal fan to cycle on and off during routine operation.


To reduce the possibility of heat-related injuries or of overheating the computer, do not place
the computer directly on your lap or obstruct the computer air vents. Use the computer only on a hard, at
surface. Do not allow another hard surface, such as an adjoining optional printer, or a soft surface, such as
pillows or rugs or clothing, to block airfow. Also, do not allow the AC adapter to come into contact with the
skin or a soft surface, such as pillows or rugs or clothing, during operation. The computer and the AC adapter
comply with the user-accessible surface temperature limits dened by applicable safety standards


HP EliteBook 845 G7 Maintenance and Service Guide


TjMax = 105 °C is the official maximum temperature of the CPU. This is exactly the value that everything refers to (throttling, etc.).

AMD Ryzen 5 PRO 4650U Processor 


International safety standards for IT and AV equipment, relevant for laptops, tablets, monitors, etc.
Accessible surfaces shall not reach temperatures that could cause burns to the user under normal operating conditions.


CPU Health and Testing
Component Tests: Inside the diagnostics menu, navigate to Component Tests to find specific tests for the processor, including a "Processor Check" to verify functionality.
System Information: The BIOS "Main" tab displays processor type and speed.
Temperature Management: Users have reported high operating temperatures (100°C - 105°C) on the EliteBook 845 G7 during heavy loads, which can be managed by adjusting the Windows Power Plan's "Processor performance boost mode" to disabled if overheating is detected.


HP Elitebook 845 g7 overheating? 


Take a look at your CPU temperature, thermal throttling starts at around 95 °C, and beyond that it can become critical.
Dust always builds up in the fans, and if the device previously belonged to a smoker and wasn’t properly cleaned, a lot of grime can accumulate as well.
You can try cleaning the laptop again from the outside using a can of compressed air / Anti-dust spray to blow out as much dirt as possible.
Otherwise, if it’s possible and you feel confident, open the device and check what’s going on, then clean it from the inside with a brush and a cloth.
If the fan is broken, get a replacement on eBay or a similar site, You can find used fans for between €15 and €25. Here’s also a video showing how to open it, otherwise
take it to someone who knows how to do it.

HP Elitebook 845 G7 parts installation and disassembly

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805113/how-can-i-tell-in-software-if-a-very-quiet-fan-isnt-spinning

---

#### 307. How can I change the Bluetooth sound profiles for my headset so they are easy to understand?

**问题描述 / Problem Description**:
Tags: ubuntu, audio, pulseaudio, bluetooth, pipewire | Score: 6 | Views: 360 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
I can tell you where these names come from: the Bluetooth standards' profile names. Maybe knowing that "handsfree" comes from the time that phones with bluetooth were new, and refers to making phone calls while driving a car helps make remembering easier? That's not calling for a lot of audio quality, but for things like "hangup" and "louder" buttons and low latency. (Background often helps me remember stuff.) Headset Profile, on the other hand, is call-center headset centric (monoaural headsets for people with hands on keyboards and a strained smile on their face).
(By the way, neither is "hifi", so I'm a bit confused: You would want to listen to music using the "advanced audio distribution" profile (A2DP).)
Both Pulseaudio and Pipewire use GNU Gettext to allow for strings to be translated to other languages than the software was written in. So, to change these strings for, say, German, you'd just need to change the .po file, listing the translations of the English texts, to contain a better translation; then, rebuild the machine-readable translation file (.mo) and replace the old one with it. (you'll find these in /usr/share/local/{LANGUAGE}/LC_MESSAGES/pipewire.mo, and the originals on Freedesktop's git repository)
However, in your case, just guessing from the location you state in your profile, you're probably at odds with the untranslated "original", you'll probably have to change to original source code, recompile, reinstall.
I suspect the specific occurrence is of https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/spa/plugins/bluez5/bluez5-device.c (and if you change e.g. _("Handsfree") there, you will have to change all the .po files for other languages, as well, because that's the "key" to lookup the translations!)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804603/how-can-i-change-the-bluetooth-sound-profiles-for-my-headset-so-they-are-easy-to

---

#### 308. What is the keycode of the Compose key in Linux (kernel)?

**问题描述 / Problem Description**:
Tags: linux, keyboard-layout, compose-key | Score: 6 | Views: 791 | Answers: 2 | Created: 2026-02-11

**解决方案 / Solution**:
There is none. Compose processing happens in the layer above keycodes. You use loadkeys to map any keycode (or a combination of keycode and modifiers) to a Compose "character".
So, you would need to find out the correct keycode for the physical key and use loadkeys to assign Compose to it. Like:
echo 'alt keycode 52 = Compose' | loadkeys -

There is keycode with the name KEY_COMPOSE; it is 127. But it is just a name; you still need to explicitly assign to it the meaning of "compose character" using loadkeys.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804397/what-is-the-keycode-of-the-compose-key-in-linux-kernel

---

#### 309. How to debug silent server crashes?

**问题描述 / Problem Description**:
Tags: ubuntu, freeze, gpu | Score: 6 | Views: 877 | Answers: 2 | Created: 2025-12-16

**解决方案 / Solution**:
Sometimes logging to another machine over the network works when logging to hard disk doesn't (because udp is fast, and the network stack sometimes dies last or at least after the kernel's various filesystem and disk IO layers).
So if you have one machine which either doesn't crash or crashes less frequently than others (if you've set up a cluster with slurm or similar, this would probably be the main cluster management node rather than the compute nodes), try setting it up to receive logs over the LAN from the other servers, and configure at least some of the other servers (the ones that crash most often, if there's any difference between them) to send a copy of kernel log entries to the logging server.
How to do this depends on whether you're using rsyslogd or systemd journal.  See either man rsyslogd or man systemd-journal-remote.service.
For example, with rsyslogd:
My systems use journald but are also configured to log everything with rsyslogd.
I have the following in my logging server's rsyslog config:
$ModLoad imudp              # provides UDP syslog reception 
$UDPServerAddress x.x.x.x   # my logging server's IP address
$UDPServerRun 514

and in my other machines:
if $fromhost-ip == '127.0.0.1' and $syslogfacility-text == 'kern' then @logserver

(where "logserver" is the hostname of my log server)
Actually, I have it set up so that each machine sends kernel logs to at least one other machine on my LAN, and receives log messages from at least one machine.  i.e. they all log to each other, which is why the if $fromhost-ip == '127.0.0.1' test is required, so they don't forward received messages in a never-ending loop.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803068/how-to-debug-silent-server-crashes

---

#### 310. Need help/confirmation on formatting a Debian install to use two drives

**问题描述 / Problem Description**:
Tags: debian, partition, system-installation, debian-installer, partition-table | Score: 5 | Views: 433 | Answers: 3 | Created: 2026-03-26

**解决方案 / Solution**:
Agreeing with John: put your personal data on the SSD; that's where the speed at which you can access random bytes and store data really makes a difference.
And: a fully set-up debian system comes nowhere close to filling 256 GB, so you'll be fine, completely without the HDD, which you can add to your storage if needed, later.
Contrary to what John says, there's not really any flexibility won by having /home on its own partition. You can always just copy or move the files contained in a directory, just as easily as you clone the full partition, with the difference that in the file case, you'll not be copying empty space on a partition. So. There's that.
Frankly, I'd approach this differently. You are (probably) using the graphical debian installer. Go back to the step where you decide how to partition your hard drive (misnomer in the installer, most systems don't even have a hard drive anymore): Select, "guided – whole disk with LVM" instead of "manual", do that on your SSD, and from there on, just defaults. (You can also use the "encrypted + LVM" option, which is what I'd recommend, especially if this is for a laptop that might get lost.)
That's it, and it's pretty future-proof: With an LVM setup, you can always just plug in more storage, extend the LVM volume group (in other storage management systems, that'd be called a "pool"), increase the size of the volumes on that, do things like move volumes off aging disks to new disks … while in use. So, if you later find yourself short on space, you can just add the HDD to your LVM volume group, say, hey, I want to simply enlargen my single volume-for-everything, do that, or, you can say, hey, I have a lot of movies on my /home/leonardo/Videos directory, let me just make a new volume on the HDD, move all the movies there and mount it automatically at /home/leonardo/Videos. Same with anything else – you don't need to decide this now forever, it's possible, with little effort, to change later. (You can also do much fancier stuff, if you need the space, like using your HDD as "large" storage and using the SSD as "hot" cache, if you do use LVM here. It's not something I'd recommend in your case, though: your HDD is not very large compared to the SSD, and you get data loss if any of these two fail, and your HDD might already be 10 years old, just guessing from the name? That'd make it both very slow and rather likely to fail, compared to the SSD.)
In that light, the less you use physical partitions now the more flexible you are. Your approach is one that I'd have done in the year 2000 – and I would have misestimated how much space my system and my /home need, to the effect that one would be running full while the other still had space on it.
Don't do that to yourself. Putting everything on the SSD will be fine until you amass massive amounts of data, and with LVM, you can then, very flexibly, just shift data to additional storage. At that point in time, storage prices are quite likely to have normalized a bit, too. So, start with the SSD, and then when things get full, do decisions on the data you then actually have vs the one you project you might have at some point.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805175/need-help-confirmation-on-formatting-a-debian-install-to-use-two-drives

---

#### 311. Build a minimal i686 Ubuntu live image (no GUI) with hardware detection similar to the Ubuntu installer?

**问题描述 / Problem Description**:
Tags: ubuntu, live-usb, 32bit, live-build | Score: 5 | Views: 396 | Answers: 1 | Created: 2026-03-08

**解决方案 / Solution**:
To the best of my knowledge, Ubuntu has stopped doing 32 bit releases for about 8 years now; so, I don't think you'll be able to pull together a working Ubuntu that works in i686 and is not hopelessly antique and unlikely to work on modern hardware.
Best guess here is that you want to instead go the debian route – I've asked that in the comments, but realistically, if this is about things being a minimal system, the functional differences between the two distros aren't that large. Mostly, you don't get someone nagging you about buying a subscription if you go for debian ;)
There is a pretty fundamental difference in installation: the default debian installer is really, really bad (imho) in user-friendliness compared to the Ubuntu installer. Luckily, that won't matter much to you.

Ability to boot on both legacy BIOS and UEFI systems

and

ave the USB use VFAT instead of iso9660

sound like you don't really want to have something like a Live CD image that just happens to also be bootable from a thumb drive and might or might not also have a volume for persistent storage.
You just want to install a Linux distro on a USB drive, make sure everything inside is portable (e.g. UUIDs in fstab, not device names), and set it up in a way that the USB drive both has a valid MBR as well as a UEFI system partition. (doing both can be tricky, but I think installers still try to do both on most distros)
Note that USB booting on pre-64 bit system was (in my memory) always fickle. The "ISO 9660-on-USB-with-isolinux" trickery was mostly owed to the fact that systems were very varied in what they'd do when faced with a thumb drive, while distros still wanted to maintain only one installation image for both optical media and USB thumb drives; Matthew Garrett has written more about booting in the EFI-switchover era. My memory from that time is more varied, motherboard firmwares would decide to boot or not boot, sometimes based on whatever the motherboard vendor thought Seemed Like A Good Idea At The TimeTM.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804878/build-a-minimal-i686-ubuntu-live-image-no-gui-with-hardware-detection-similar

---

#### 312. Understanding VIRT, RES and SHR in htop

**问题描述 / Problem Description**:
Tags: linux, virtual-memory | Score: 5 | Views: 713 | Answers: 2 | Created: 2026-02-27

**解决方案 / Solution**:
VIRT only shows the virtual memory allocation; it doesn’t necessarily correspond to pages at all. Processes can allocate memory without ever using it.
RES as you say is resident memory, that is to say, pages present in physical memory allocated for the process.
SHR counts memory that’s shared between processes. This happens for example with shared libraries: their read-only pages are mapped in memory once, and every process relying on them gets the same pages. See How to know shared memory between two processes?
This is documented in more detail in the htop manual.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804734/understanding-virt-res-and-shr-in-htop

---

#### 313. Create and verify a large single file in parallel-mode

**问题描述 / Problem Description**:
Tags: linux, hashsum, parallelism | Score: 5 | Views: 609 | Answers: 3 | Created: 2026-02-18

**解决方案 / Solution**:
Most hashing algorithms these days are not bound by how much CPU you can throw at them - but by how much memory bandwidth you have. Your md5 implementation might be an outlier in its slowness. Something's wrong there; it's really slow.
Hashes like the xxHash family will saturate your 3Gb/s link easily. Once you've saturated that, no way to get faster, especially not with parallelism.
So, just go and install xxhash's xxhsum. In its xxhsum -H3 implementation it reaches 15914.4 MB/s – that's nearly 64 Gb/s – single-threadedly on my phone (on which im typing this) (as installed via Termux's pkg). (You can benchmark with xxhsum -b.)
Note that "splitting a file and hashing its parts with md5" is not at all the same as "calculating the md5 hash of the full file", so you'll need to do something custom anyways. This is a clear case for just not doing md5, then.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804535/create-and-verify-a-large-single-file-in-parallel-mode

---

#### 314. Querying application versions in Debian-style Linux versions

**问题描述 / Problem Description**:
Tags: debian, ubuntu, repository, version | Score: 5 | Views: 504 | Answers: 2 | Created: 2025-12-08

**解决方案 / Solution**:
Marcus Müller’s answer shows how to get version information for any distribution release or container image.
For Debian (and Ubuntu), you can use rmadison instead (in the devscripts package):
$ rmadison qemu
qemu       | 1:5.2+dfsg-11+deb11u3         | oldoldstable                      | source, amd64, arm64, armhf, i386
qemu       | 1:5.2+dfsg-11+deb11u3         | oldoldstable-debug                | source
qemu       | 1:7.2+dfsg-7+deb12u16         | oldstable                         | source
qemu       | 1:7.2+dfsg-7+deb12u16         | oldstable-debug                   | source
qemu       | 1:7.2+dfsg-7+deb12u16         | oldstable-proposed-updates-debug  | source
qemu       | 1:7.2+dfsg-7+deb12u17         | buildd-oldstable-proposed-updates | source
qemu       | 1:7.2+dfsg-7+deb12u17         | oldstable-proposed-updates        | source
qemu       | 1:7.2+dfsg-7+deb12u17         | oldstable-proposed-updates-debug  | source
qemu       | 1:10.0.2+ds-2+deb13u1~bpo12+1 | oldstable-backports               | source
qemu       | 1:10.0.2+ds-2+deb13u1~bpo12+1 | oldstable-backports-debug         | source
qemu       | 1:10.0.6+ds-0+deb13u2         | stable                            | source
qemu       | 1:10.0.6+ds-0+deb13u2         | stable-debug                      | source
qemu       | 1:10.0.6+ds-0+deb13u2         | unstable                          | source
qemu       | 1:10.1.2+ds-1                 | testing                           | source
qemu       | 1:10.1.2+ds-3                 | unstable                          | source
qemu       | 1:10.1.2+ds-3                 | unstable-debug                    | source
qemu       | 1:10.2.0~rc1+ds-1             | experimental                      | source
qemu       | 1:10.2.0~rc1+ds-1             | experimental-debug                | source

On a Debian system (or similar), this will show results for currently-supported releases of Debian by default; on a Ubuntu system (or derivative), it will show results for Ubuntu. The -u option can be used to switch sources (-u debian or -u ubuntu).
One benefit of this approach is that it shows all available versions, including backports, regardless of the repositories configured on the querying system or in the container image.
For Debian specifically, you can get information on older releases as well by querying the archived releases instead:
$ rmadison -u archive qemu
 qemu | 0.6.1+20050407-1sarge1        | debian/sarge              | i386, powerpc
 qemu | 0.6.1+20050407-1sarge1        | debian/sarge-security     | source, i386, powerpc
 qemu | 0.8.2-4                       | debian/etch-m68k          | source
 qemu | 0.8.2-4etch3                  | debian/etch               | source, amd64, i386, powerpc
 qemu | 0.8.2-4etch3                  | debian/etch-security      | source, amd64, i386, powerpc
 qemu | 0.9.1-10lenny1~bpo40+1        | debian/etch-backports     | source, amd64, i386, powerpc, sparc
 qemu | 0.9.1-10lenny1                | debian/lenny              | source, amd64, i386, powerpc, sparc
 qemu | 0.9.1-10lenny1                | debian/lenny-security     | source, amd64, i386, powerpc, sparc
 qemu | 0.12.5+dfsg-3squeeze4         | debian/squeeze            | source, amd64, armel, i386, kfreebsd-amd64, kfreebsd-i386, mips, mipsel, powerpc, sparc   
 qemu | 0.12.5+dfsg-3squeeze4         | debian/squeeze-security   | source, amd64, armel, i386, kfreebsd-amd64, kfreebsd-i386, mips, mipsel, powerpc, sparc   
 qemu | 0.12.5+dfsg-3squeeze5         | debian/squeeze-lts        | source, amd64, i386
 qemu | 1.1.2+dfsg-2~bpo60+1          | debian/squeeze-backports  | source, armel, ia64, kfreebsd-amd64, kfreebsd-i386, mips, powerpc
 qemu | 1.1.2+dfsg-6a+deb7u7~bpo60+1  | debian/squeeze-backports  | source, amd64, i386, mipsel, sparc
 qemu | 1.1.2+dfsg-6a+deb7u12         | debian/wheezy             | source, amd64, armel, armhf, i386, ia64, kfreebsd-amd64, kfreebsd-i386, mips, mipsel, powerpc, s390x, sparc
 qemu | 1.1.2+dfsg-6+deb7u25          | debian/wheezy-security    | source, amd64, armel, armhf, i386
 qemu | 2.0.0+dfsg-4~bpo70+1          | debian/wheezy-backports   | source, s390x
 qemu | 2.1+dfsg-5~bpo70+1            | debian/wheezy-backports   | source, sparc
 qemu | 1:2.1+dfsg-11                 | debian/jessie-kfreebsd    | source, kfreebsd-amd64, kfreebsd-i386
 qemu | 1:2.1+dfsg-12+deb8u5a~bpo70+1 | debian/wheezy-backports   | source, amd64, armel, armhf, i386, ia64, kfreebsd-amd64, kfreebsd-i386, mips, mipsel, powerpc
 qemu | 1:2.1+dfsg-12+deb8u6          | debian/jessie             | source, amd64, arm64, armel, armhf, i386, mips, mipsel, powerpc, ppc64el, s390x
 qemu | 1:2.1+dfsg-12+deb8u15         | debian/jessie-security    | source, amd64, armel, armhf, i386
 qemu | 1:2.8+dfsg-3~bpo8+1           | debian/jessie-backports   | source, amd64, arm64, armel, armhf, i386, mips, mipsel, powerpc, ppc64el, s390x
 qemu | 1:2.8+dfsg-6+deb9u9           | debian/stretch            | source, amd64, arm64, armel, armhf, i386, mips, mipsel, ppc64el, s390x
 qemu | 1:2.8+dfsg-6+deb9u17          | debian/stretch-security   | source, amd64, arm64, armel, armhf, i386
 qemu | 1:3.1+dfsg-8+deb10u8          | debian/buster             | source, amd64, arm64, armel, armhf, i386, mips, mips64el, mipsel, ppc64el, s390x
 qemu | 1:3.1+dfsg-8+deb10u12         | debian/buster-security    | source, amd64, arm64, armhf, i386
 qemu | 1:5.2+dfsg-9~bpo10+1          | debian/buster-backports   | source, amd64, arm64, armel, armhf, i386, mips64el, mipsel, ppc64el, s390x
 qemu | 1:5.2+dfsg-11+deb11u3         | debian/bullseye           | source, amd64, arm64, armel, armhf, i386, mips64el, mipsel, ppc64el, s390x
 qemu | 1:7.2+dfsg-7+deb12u2~bpo11+1  | debian/bullseye-backports | source

The UDD can also be used as a source:
$ rmadison -u udd qemu
 qemu | 1:5.2+dfsg-11+deb11u3         | bullseye           | source, amd64, arm64, armhf, i386
 qemu | 1:5.2+dfsg-11+deb11u5         | bullseye-security  | source, amd64, arm64, armhf, i386
 qemu | 1:7.2+dfsg-7+deb12u15         | bookworm-security  | source
 qemu | 1:7.2+dfsg-7+deb12u16         | bookworm           | source
 qemu | 1:7.2+dfsg-7+deb12u17         | bookworm-p-u       | source
 qemu | 1:10.0.2+ds-2+deb13u1~bpo12+1 | bookworm-backports | source
 qemu | 1:10.0.2+ds-2+deb13u1         | trixie-security    | source
 qemu | 1:10.0.6+ds-0+deb13u2         | trixie             | source
 qemu | 1:10.0.6+ds-0+deb13u2         | sid                | source
 qemu | 1:10.1.2+ds-1                 | forky              | source
 qemu | 1:10.1.2+ds-3                 | sid                | source
 qemu | 1:10.2.0~rc1+ds-1             | experimental       | source

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801912/querying-application-versions-in-debian-style-linux-versions

---

#### 315. Can a single physical server boot and run two Debian systems from different partitions?

**问题描述 / Problem Description**:
Tags: debian, system-installation | Score: 4 | Views: 972 | Answers: 5 | Created: 2026-04-14

**解决方案 / Solution**:
If I understood your question correctly, you want to run two Debian instances simultaneously on one computer, that’s not possible unless you use a container or a virtualization system on your main OS/System.
I would install Debian as the main system and then use Debian with Docker.
This way, you can run as many Debian instances as your hardware setup allows, so at least two for sure.

Install Docker Engine on Debian

debian - Docker Official Image


This way, you can also try out different configurations and easily export the containers to use them on other operating systems/systems.
Of course, security aspects and hardening must be considered if you want to use it in production and not just as a test or lab environment.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805434/can-a-single-physical-server-boot-and-run-two-debian-systems-from-different-part

---

#### 316. Why is Unix socket still there despite not referred by process file descriptor?

**问题描述 / Problem Description**:
Tags: linux, unix-sockets | Score: 4 | Views: 104 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
Educated guess is file descriptor passing (SCM_RIGHTS message). It creates the copy of file descriptor (which now remains open), but until the destination consumed the SCM_RIGHTS message it will not appear in the destination's file table. Consider the example of /tmp/scm simply creating a sink socket where /tmp/server can send its created "production" socket:

Launch /tmp/scm that creates @SCM socket that is used as a sink for passing file descriptor:


bor@ThinkPad-E16-Gen3:~$ /tmp/scm &
[3] 24854
bor@ThinkPad-E16-Gen3:~$ sudo netstat -pax | grep SCM
unix  2      [ ]         DGRAM                    293467   24854/scm            @SCM
bor@ThinkPad-E16-Gen3:~$ LANG=C ls -l /proc/24854/fd
total 0
lrwx------ 1 bor bor 64 Feb 21 17:53 0 -> /dev/pts/1
lrwx------ 1 bor bor 64 Feb 21 17:53 1 -> /dev/pts/1
lrwx------ 1 bor bor 64 Feb 21 17:53 2 -> /dev/pts/1
lrwx------ 1 bor bor 64 Feb 21 17:53 3 -> 'socket:[293467]'
bor@ThinkPad-E16-Gen3:~$ 


Now launch /tmp/server which creates the abstract socket @SOCKET and passes its descriptor to the @SCM socket:

bor@ThinkPad-E16-Gen3:~$ /tmp/server
passing fd 3
bor@ThinkPad-E16-Gen3:~$ sudo netstat -pax | grep SOCKET
unix  2      [ ]         DGRAM                    304790   24870/server         @SOCKET
bor@ThinkPad-E16-Gen3:~$ LANG=C ls -l /proc/24870/fd
total 0
lrwx------ 1 bor bor 64 Feb 21 17:55 0 -> /dev/pts/0
lrwx------ 1 bor bor 64 Feb 21 17:55 1 -> /dev/pts/0
lrwx------ 1 bor bor 64 Feb 21 17:55 2 -> /dev/pts/0
lrwx------ 1 bor bor 64 Feb 21 17:55 3 -> 'socket:[304790]'
lrwx------ 1 bor bor 64 Feb 21 17:55 4 -> 'socket:[304791]'
bor@ThinkPad-E16-Gen3:~$ LANG=C ls -l /proc/24854/fd
итого 0
lrwx------ 1 bor bor 64 Feb 21 17:53 0 -> /dev/pts/1
lrwx------ 1 bor bor 64 Feb 21 17:53 1 -> /dev/pts/1
lrwx------ 1 bor bor 64 Feb 21 17:53 2 -> /dev/pts/1
lrwx------ 1 bor bor 64 фев 21 17:53 3 -> 'socket:[293467]'
bor@ThinkPad-E16-Gen3:~$ 

Notice that although the /tmp/server has sent the file descriptor, it is not visible in the /tmp/scm file table.

Kill /tmp/server.

bor@ThinkPad-E16-Gen3:~$ sudo netstat -pax | grep SOCKET
unix  2      [ ]         DGRAM                    304790   -                    @SOCKET
bor@ThinkPad-E16-Gen3:~$ 

At this point you have open reference to the @SOCKET somewhere in the socket @SCM buffers. I do not know whether it is possible to show it and how. I suppose it is possible by directly crawling memory, but I could not find netstat/ss options to show pending control messages (as opposed to the actual data).
The only way to destroy it is to either consume the SCM_RIGHTS message and close the resulting file descriptor or to terminate the process that listens on the @SCM socket.
bor@ThinkPad-E16-Gen3:~$ fg
/tmp/scm
^C
bor@ThinkPad-E16-Gen3:~$ sudo netstat -pax | grep SOCKET
bor@ThinkPad-E16-Gen3:~$ 

For the sake of completeness, the code.
The /tmp/scm.c:
       #define SOCKET_NAME "\0SCM"
       #define BUFFER_SIZE 12

       #include <stdio.h>
       #include <stdlib.h>
       #include <string.h>
       #include <sys/socket.h>
       #include <sys/un.h>
       #include <unistd.h>

       int
       main(void)
       {
           int                 down_flag = 0;
           int                 ret;
           int                 connection_socket;
           int                 data_socket;
           int                 result;
           ssize_t             r, w;
           struct sockaddr_un  name;
           char                buffer[BUFFER_SIZE];

           /* Create local socket. */

           connection_socket = socket(AF_UNIX, SOCK_DGRAM, 0);
           if (connection_socket == -1) {
               perror("socket");
               exit(EXIT_FAILURE);
           }

           /*
            * For portability clear the whole structure, since some
            * implementations have additional (nonstandard) fields in
            * the structure.
            */

           memset(&name, 0, sizeof(name));

           /* Bind socket to socket name. */

           name.sun_family = AF_UNIX;
           memcpy(name.sun_path, SOCKET_NAME, sizeof(SOCKET_NAME));

           ret = bind(connection_socket, (const struct sockaddr *) &name,
                      sizeof(name) - (sizeof(name.sun_path) - sizeof(SOCKET_NAME) + 1));
           if (ret == -1) {
               perror("bind");
               exit(EXIT_FAILURE);
           }

       sleep (60*60*24);

           exit(EXIT_SUCCESS);
       }

The /tmp/server.c:
       #define SOCKET_NAME "\0SOCKET"
       #define SCM_SOCKET_NAME "\0SCM"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <unistd.h>

ssize_t
sock_fd_write(int sock, void *buf, ssize_t buflen, int fd)
{
    ssize_t     size;
    struct msghdr   msg;
    struct iovec    iov;
    union {
        struct cmsghdr  cmsghdr;
        char        control[CMSG_SPACE(sizeof (int))];
    } cmsgu;
    struct cmsghdr  *cmsg;

    iov.iov_base = buf;
    iov.iov_len = buflen;

    msg.msg_name = NULL;
    msg.msg_namelen = 0;
    msg.msg_iov = &iov;
    msg.msg_iovlen = 1;

    if (fd != -1) {
        msg.msg_control = cmsgu.control;
        msg.msg_controllen = sizeof(cmsgu.control);

        cmsg = CMSG_FIRSTHDR(&msg);
        cmsg->cmsg_len = CMSG_LEN(sizeof (int));
        cmsg->cmsg_level = SOL_SOCKET;
        cmsg->cmsg_type = SCM_RIGHTS;

        printf ("passing fd %d\n", fd);
        *((int *) CMSG_DATA(cmsg)) = fd;
    } else {
        msg.msg_control = NULL;
        msg.msg_controllen = 0;
        printf ("not passing fd\n");
    }

    size = sendmsg(sock, &msg, 0);

    if (size < 0)
        perror ("sendmsg");
    return size;
}

       int
       main(void)
       {
           int                 ret;
           int                 connection_socket;
           int                 scm_socket;
           struct sockaddr_un  name;

           /* Create local socket.  */

           connection_socket = socket(AF_UNIX, SOCK_DGRAM, 0);
           if (connection_socket == -1) {
               perror("socket");
               exit(EXIT_FAILURE);
           }

           /*
            * For portability clear the whole structure, since some
            * implementations have additional (nonstandard) fields in
            * the structure.
            */

           memset(&name, 0, sizeof(name));

           /* Bind socket to socket name.  */

           name.sun_family = AF_UNIX;
           memcpy(name.sun_path, SOCKET_NAME, sizeof(SOCKET_NAME));

           ret = bind(connection_socket, (const struct sockaddr *) &name,
                      sizeof(name) - (sizeof(name.sun_path) - sizeof(SOCKET_NAME) + 1));
           if (ret == -1) {
               perror("bind");
               exit(EXIT_FAILURE);
           }

           /* Create SCM socket.  */

           scm_socket = socket(AF_UNIX, SOCK_DGRAM, 0);
           if (scm_socket == -1) {
               perror("socket scm");
               exit(EXIT_FAILURE);
           }

           /*
            * For portability clear the whole structure, since some
            * implementations have additional (nonstandard) fields in
            * the structure.
            */

           memset(&name, 0, sizeof(name));

           /* Bind socket to socket name.  */

           name.sun_family = AF_UNIX;
           memcpy(name.sun_path, SCM_SOCKET_NAME, sizeof(SCM_SOCKET_NAME));

           ret = connect(scm_socket, (const struct sockaddr *) &name,
                      sizeof(name) - (sizeof(name.sun_path) - sizeof(SCM_SOCKET_NAME) + 1));
           if (ret == -1) {
               perror("connect scm");
               exit(EXIT_FAILURE);
           }

           sock_fd_write(scm_socket, 0, 0, connection_socket);

       sleep (60 * 60 * 24);

           exit(EXIT_SUCCESS);
       }

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804617/why-is-unix-socket-still-there-despite-not-referred-by-process-file-descriptor

---

#### 317. Change what kernel is being booted in Grub

**问题描述 / Problem Description**:
Tags: debian, kernel, grub2, kernel-modules | Score: 4 | Views: 592 | Answers: 3 | Created: 2026-02-20

**解决方案 / Solution**:
I'd uninstall the newer kernel package and set a hold on the linux kernel package (e.g. using aptitude).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804604/change-what-kernel-is-being-booted-in-grub

---

#### 318. Getting parent device node from partition device node

**问题描述 / Problem Description**:
Tags: linux, udev, block-device | Score: 3 | Views: 220 | Answers: 3 | Created: 2026-04-16

**解决方案 / Solution**:
On Linux, with lsblk, you can get the parent kernel name with lsblk -o pkname:
$ ls -ld foo
brw-rw---- 1 root disk 8, 6 Apr 17 06:54 foo
$ lsblk -no pkname foo
sda
$ lsblk -no name foo
sda6

AFAICT, it's only documented in the output of lsblk -H aka --list-columns:
$ lsblk -H | grep -i parent
      PKNAME <string>        internal parent kernel device name

With zsh:
$ zmodload zsh/stat
$ stat -A d +rdev foo &&
    print -r -- /sys/dev/block/$(( d >> 8 )):$(( d & 0xff ))(:P:h:t)
sda

Where we do it by hand by extracting the major:minor from the rdev field of the stat structure, locate the device in /sys via the /sys/dev/block/major:minor symlink (assuming it's a block device in the first place), then use modifiers in glob qualifiers, to get its real Path, then the head (dirname, so parent) of that path (assuming it is a partition in the first place), then the tail (basename).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805499/getting-parent-device-node-from-partition-device-node

---

#### 319. Installing HopToDesk on Debian 13 (trixie) or LMDE 7 (gigi) error /var/lib/dpkg/info/hoptodesk.postinst: No such file or directory

**问题描述 / Problem Description**:
Tags: debian, software-installation, package-management | Score: 3 | Views: 212 | Answers: 1 | Created: 2026-04-07

**解决方案 / Solution**:
I tried to run the post-installation script:
$ sudo /var/lib/dpkg/info/hoptodesk.postinst

sudo: unable to execute /var/lib/dpkg/info/hoptodesk.postinst: No such file or directory

I have found that /var/lib/dpkg/info/hoptodesk.postinst exists, and is an executable as it should be, just it's in DOS CRLF (line terminators) format:
$ file /var/lib/dpkg/info/hoptodesk.postinst

/var/lib/dpkg/info/hoptodesk.postinst: Bourne-Again shell script, Unicode text, UTF-8 text executable, with CRLF line terminators


So, to resolve the issue is as easy as to convert to Unix LF format, and re-running dpkg:
$ sudo dos2unix /var/lib/dpkg/info/hoptodesk.postinst

dos2unix: converting file /var/lib/dpkg/info/hoptodesk.postinst to Unix format...

and finally, finishing the installation with:
$ sudo dpkg --configure --pending

Setting up hoptodesk (1.45.10) ...
Created symlink '/etc/systemd/system/multi-user.target.wants/hoptodesk.service' → '/etc/systemd/system/hoptodesk.service'.

Hope it helps.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805343/installing-hoptodesk-on-debian-13-trixie-or-lmde-7-gigi-error-var-lib-dpkg

---

#### 320. Upgrade to grub 2.14 from 2.12 on Debian can no longer load Linux initrd

**问题描述 / Problem Description**:
Tags: debian, boot, grub2, initrd | Score: 3 | Views: 440 | Answers: 1 | Created: 2026-03-05

**解决方案 / Solution**:
GRUB 2.14 is using native EFI load image instead of legacy handover if

Kernel is built with EFI stub
shim supports LoadImage protocol (as of version 16.1).

In this case GRUB tries to install LoadFile2 protocol on the loaded initrd image, later kernel stub will call this protocol to get initrd.
The first error comes from installing LoadFile2 protocol and the second - from calling LoadImage when booting kernel. The first is completely inside the firmware. The second is between GRUB and shim.
There is no way to force legacy handover protocol. You can try installing older shim (pre-16.1) to see if it changes anything but it is not an option in the long run.
Consider reporting it to the grub developers.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804824/upgrade-to-grub-2-14-from-2-12-on-debian-can-no-longer-load-linux-initrd

---

#### 321. Ubuntu system returns "killed" on nearly all commands

**问题描述 / Problem Description**:
Tags: ubuntu, nginx, node.js, out-of-memory, deployment | Score: 3 | Views: 170 | Answers: 2 | Created: 2026-02-16

**解决方案 / Solution**:
It definitely looks like a crypto miner malware, which has arranged a higher priority for itself and is trying to kill any commands that would kill it before they can take effect.
  │ └─809 /bin/softirq --randomx-1gb-pages -o 45.125.66.100:444 -u react -p 3cthDeQ5 --tls -o 45.94.31.89:443 -u react -p 3cthDeQ5 --tls -B

This is clearly a fake name: a real softirq process would have a name like [ksoftirqd/0] and it would have no reason to have IP addresses and ports as parameters.
Maybe you're using a weak password (use SSH key authentication for internet-accessible servers) or the software you're running has a vulnerability that allows the attacker to plant malware to the system.
In the comments, eyoung100 already identified PeerBlight (CVE-2025-55182) as the possible vulnerability, if the application is using React Server Function endpoints or React Server Components. If you are using the vulnerable versions (anything older than versions 19.0.1, 19.1.2 or 19.2.1), you'll need to update those componets before redeploying your application.
Anyway, the link in Robo's answer seems to indicate this malware is part of the RondoDox botnet.
Because the malware attempts to protect itself, you may have to stop the VPS, create a new "clean" one, and then connect the disk of the infected VPS as a secondary disk to the clean VPS to recover your data and to possibly inspect the malware. Unless you know how to check, assume any executables on the disk of the infected VPS are contaminated by malware - so don't reuse them. Before redeploying, check if the application (or any components you used in it, if the application is custom-built by yourself) for security notices and update as necessary.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804521/ubuntu-system-returns-killed-on-nearly-all-commands

---

#### 322. Resizing encrypted system partition on Linux Ubuntu

**问题描述 / Problem Description**:
Tags: ubuntu, partition, encryption, luks, gparted | Score: 3 | Views: 398 | Answers: 1 | Created: 2025-11-14

**解决方案 / Solution**:
This solution looks at a convenient GUI option, using the KDE Partition Manager.

Unlock the LUKS-encrypted partition.
Resize the ext4 filesystem or another supported filesystem inside the partition. This also has the intended effect that it shrinks the encrypted partition.
Finally, apply changes.

Here is a CLI solution derived from the commands KDE Partition Manager executes.

Unlock the LUKS-encrypted partition: cryptsetup open --type luks2 /dev/[device_name] [device_name]_crypt. This will allow you to see the filesystem inside on /dev/mapper/[device_name]_crypt
Check the filesystem for errors. For an ext4 filesystem, use e2fsck -v /dev/mapper/[device_name]_crypt to check for any errors. e2fsck -vf /dev/mapper/[device_name]_crypt can be used to repair those errors. For btrfs, use btrfs check instead and btrfs check --repair to repair errors. It is advised to backup data before repairing the filesystem.
Execute resize2fs /dev/mapper/[device_name]_crypt [new_size] to shrink the filesystem. This will not shrink the LUKS partition. [new_size] should be 32768 512-bytes (16777216 bytes or 16 megabytes) smaller than [new_size] in the next step to allow for room for the LUKS header. For btrfs, mount /dev/mapper/[device_name]_crypt first and then run btrfs filesystem resize [new_size] [mounted_path].
To shrink the LUKS partition, run cryptsetup --size [new_size] resize /dev/mapper/[device_name]_crypt. Note [new_size] is in 512-byte units (divide bytes by 512 or megabytes by 2 to obtain this)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801335/resizing-encrypted-system-partition-on-linux-ubuntu

---

#### 323. How to debug uninformative email received at startup

**问题描述 / Problem Description**:
Tags: linux, startup | Score: 2 | Views: 81 | Answers: 1 | Created: 2026-04-26

**解决方案 / Solution**:
Thanks for all the comments. I am confident that the email originated from an at command, but I am unable to find any details of which command or what, in more detail, went wrong.
There does not seem to be much error processing capability in at. The solution I devised is to create a file, called, say, at.script containing:

echo "First comment”
Command
echo "Ending comment”

and use it like:
at -f at.script HH:mm
which sends an email if the command fails:

First comment
[error message]
Ending comment

To always send an email, use
at -m -f at.script HH:mm

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805641/how-to-debug-uninformative-email-received-at-startup

---

#### 324. Get debug symbols for ubuntu kernel

**问题描述 / Problem Description**:
Tags: ubuntu, linux-kernel, debugging | Score: 2 | Views: 85 | Answers: 1 | Created: 2026-04-18

**解决方案 / Solution**:
So apparently they are in the linux-image-unsigned package (linux-image-unsigned-6.17.0-19-generic-dbgsym)
$ dpkg --listfiles linux-image-unsigned-6.17.0-19-generic-dbgsym | grep /usr/lib/debug/boot
/usr/lib/debug/boot
/usr/lib/debug/boot/vmlinux-6.17.0-19-generic

$ file /usr/lib/debug/boot/vmlinux-6.17.0-19-generic
/usr/lib/debug/boot/vmlinux-6.17.0-19-generic: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=3aca328be7c4b1bc5cbb857c1483d4ac6e979e45, with debug_info, not stripped

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805516/get-debug-symbols-for-ubuntu-kernel

---

#### 325. Cinnamon - I can't get my laptop to power off when lid is closed

**问题描述 / Problem Description**:
Tags: debian, systemd, cinnamon | Score: 2 | Views: 46 | Answers: 1 | Created: 2026-04-17

**解决方案 / Solution**:
The handling of lid switch is blocked by the csd-power which has its own logic. Looking at cinnamon-settings-daemon sources you should be able to disable it with
gsettings set org.cinnamon.settings-daemon.plugins.power inhibit-lid-switch false

You should also be able to tell csd-power to power off instead of suspending with
gsettings set org.cinnamon.settings-daemon.plugins.power lid-close-battery-action shutdown
gsettings set org.cinnamon.settings-daemon.plugins.power lid-close-ac-action shutdown

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805509/cinnamon-i-cant-get-my-laptop-to-power-off-when-lid-is-closed

---

#### 326. Unable to login with normal user via SSH after upgrading to Debian Bookworm

**问题描述 / Problem Description**:
Tags: debian, ssh, arm, putty | Score: 2 | Views: 48 | Answers: 1 | Created: 2026-04-07

**解决方案 / Solution**:
Apr 06 23:00:35 odroidhc4 sshd-session[780237]: User ricky from 192.168.0.X not allowed because none of user's groups are listed in AllowGroups

This would be the source of the problem.   Check the definition of AllowGroups and DenyGroups in your /etc/ssh/sshd_config.   Either add user ricky to one of the allowed groups or comment out that definition in the config.
From man sshd_config:

AllowGroups
This keyword can be followed by a list of group name patterns, separated by
spaces.  If specified, login is allowed only for users whose primary group
or supplementary group list matches one of the patterns.  Only group names
are valid; a numerical group ID is not recognized.  By default, login is
allowed for all groups.  The allow/deny groups directives are processed in
the following order: DenyGroups, AllowGroups.
See PATTERNS in ssh_config(5) for more information on patterns.  This keyword
may appear multiple times in sshd_config with each instance appending to the
list.

and

DenyGroups
This keyword can be followed by a list of group name patterns, separated by
spaces.  Login is disallowed for users whose primary group or supplementary
group list matches one of the patterns.  Only group names are valid; a
numerical group ID is not recognized.  By default, login is allowed for all
groups.  The allow/deny groups directives are processed in the following
order: DenyGroups, AllowGroups.
See PATTERNS in ssh_config(5) for more information on patterns.  This keyword
may appear multiple times in sshd_config with each instance appending to the
list.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805337/unable-to-login-with-normal-user-via-ssh-after-upgrading-to-debian-bookworm

---

#### 327. Debian 13 display issue with notebook

**问题描述 / Problem Description**:
Tags: debian, display, debian-installer, firmware, radeon | Score: 2 | Views: 181 | Answers: 2 | Created: 2026-04-03

**解决方案 / Solution**:
What is going on?

Laptop's not working without firmware; in this case probably especially GPU firmware, which would be in the non-free firmware-amd-graphics-* package.

Is it possible to fix this without installing non-free firmware?

no. Unless you can write that firmware yourself. That's not practically possible.

Curiously, Debian 12 LXDE with firmware=never doesn't have this issue: after installation I can access both LXDE and CLI normally.

Unless the installation of Debian 13 with non-free firmware also fails, I suspect it's falling back to VESA graphics, which is probably not what you want on a laptop. (or you, at some point, installed the non-free firmware and forgot about it – always take the human factor into account!)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805270/debian-13-display-issue-with-notebook

---

#### 328. How to set GET_EVENT_STATUS_NOTIFICATION interval for CD drive in Linux

**问题描述 / Problem Description**:
Tags: linux, configuration, block-device, data-cd | Score: 2 | Views: 125 | Answers: 1 | Created: 2026-03-24

**解决方案 / Solution**:
The interval at which Linux kernel polls removable block devices is set by the events_dfl_poll_msecs setting. You can set it by e.g.
echo 60000 > /sys/module/block/parameters/events_dfl_poll_msecs

to increase the interval to 60 seconds. Setting it to 0 will disable polling entirely and newly inserted discs will only be detected when you try to access the drive.
There is also per-device setting events_poll_msecs. When set to -1, the device uses the global setting above.
echo -1 > /sys/block/sr0/events_poll_msecs

The kernel default is actually 0 (polling disabled), but on most distributions udev rule in /usr/lib/udev/rules.d/60-block.rules overrides this:
# enable in-kernel media-presence polling
ACTION=="add", SUBSYSTEM=="module", KERNEL=="block", ATTR{parameters/events_dfl_poll_msecs}=="0", \
   ATTR{parameters/events_dfl_poll_msecs}="2000"

If you wanted to permanently modify the setting (rather than just for testing), creating an override file in /etc/udev/rules.d would be the cleanest way.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805135/how-to-set-get-event-status-notification-interval-for-cd-drive-in-linux

---

#### 329. Overmounts behave differently between / and other mount points

**问题描述 / Problem Description**:
Tags: linux, mount, cd-command, namespace | Score: 2 | Views: 136 | Answers: 1 | Created: 2026-03-13

**解决方案 / Solution**:
A leading / is handled specially by basically jumping to /proc/self/root. That can be changed by chroot or pivot_root but not cd. Mounts are only considered for each path component e.g. subdirectory, and there are none in cd /.
To actually see the tmpfs mounted over /, use ls /... To exclude interference by the shell, use cd -P /...
hostname:~$ unshare -cm --keep-caps
hostname:~$ mount -t tmpfs tmpfs /
hostname:~$ cd /
hostname:/$ ls
bin   cdrom  etc   lib    lib64   lost+found  mnt  old  proc  run   srv  tmp  var
boot  dev    home  lib32  libx32  media       new  opt  root  sbin  sys  usr
hostname:/$ ls ..
hostname:/$ touch test
touch: cannot touch 'test': Permission denied
hostname:/$ touch ../test
hostname:/$ ls ..
test
hostname:/$ ls
bin   cdrom  etc   lib    lib64   lost+found  mnt  old  proc  run   srv  tmp  var
boot  dev    home  lib32  libx32  media       new  opt  root  sbin  sys  usr
hostname:/$ cd .. # Bash swallows the `..`
hostname:/$ ls
bin   cdrom  etc   lib    lib64   lost+found  mnt  old  proc  run   srv  tmp  var
boot  dev    home  lib32  libx32  media       new  opt  root  sbin  sys  usr
hostname:/$ cd -P ..
hostname:/$ ls
test
hostname:/$ mkdir bin
hostname:/$ cp /bin/busybox bin
hostname:/$ chroot . busybox ash


BusyBox v1.37.0 (Ubuntu 1:1.37.0-4ubuntu1) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/ $ ls
bin
/ $ cd / # Jumps to, i.e. stays at, the new `/` since we chrooted
/ $ ls
bin
/ $ 
hostname:/$ ls
bin
hostname:/$ cd / # Jumps to real `/` when outside chroot
hostname:/$ ls
bin   cdrom  etc   lib    lib64   lost+found  mnt  old  proc  run   srv  tmp  var
boot  dev    home  lib32  libx32  media       new  opt  root  sbin  sys  usr
hostname:/$ ls usr/.. # Any (attempted) directory change triggers mountpoint lookup
bin


Notably, if I switch into the shell's mount namespace and run ls from another terminal using nsenter --target $PID_OF_FIRST_SHELL -m ls, then I get the error message

man setns, used by nsenter, says:

Changing the mount  namespace  requires  that  the  caller  possess  both  CAP_SYS_CHROOT [...]

So the setns probably performs a chroot internally.


Are you saying that chdir("..") doesn't get resolved to the root directory?

.. means ./.. which grabs the cwd and resolves to /... Linux prevents escaping the root directory, so /.. still resolves to the old /. Since .. is usually not the current directory, Linux takes the time to check whether there's a mountpoint i.e. DCACHE_MOUNTED. Now the mountpoint code replaces the old / with the new /.
You can replace ls /.. with ls /usr/...
I needed /.. to force a non-simple path component that resolves to the root directory. Otherwise, Linux is too lazy to check for mountpoints. ls //, ls ///, ls /./, and ls //./. all make Linux lazy. Linux just blindly skips the slashes and single dots. Symlinks basically just replace the prefix, so ln -s . /test doesn't stop Linux from being too lazy to check the mountpoint.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804976/overmounts-behave-differently-between-and-other-mount-points

---

#### 330. Sunshine + Moonlight on Linux (RTX 3060) – how to enable YUV 4:4:4 / RGB streaming?

**问题描述 / Problem Description**:
Tags: ubuntu, nvidia, ffmpeg, video-encoding | Score: 2 | Views: 186 | Answers: 1 | Created: 2026-03-10

**解决方案 / Solution**:
YUV 4:4:4 with NvENC encoding will outright not work on Linux as of now and that message will be shown by sunshine.
This is because Sunshine has not implemented 4:4:4 NvENC support for Linux yet. The discussion around implementing it (LizardByte discussion #220) latest comment (made on Jan 10th, 2025) is:

Is there any update on native/recombined YUV4:4:4 host support on Linux? I couldn't see any MR or discussion related to it around the repos or in the discord.

And the PR that implemented it (Sunshine PR #2533)  explicitly mentions:

linux support may be possible through ffmpeg, but not yet implemented or even investigated

Windows support was added in release 2025.118.151840 and no other release until today mentions 4:4:4 at all. So the reason it doesn't work is because the host is Linux and it's still not implemented for it.
If you prioritize 4:4:4 over NvENC GPU Encoding, 4:4:4 works on Linux as of now with x264 encoding but is apparently currently not available for x265 encoding because it jumps from wanting yuv444p10le or yuv420p10le to deciding to use x264 if Main10 is not available. Issue #4836 demonstrates this:

[2026-03-10 16:14:17.056]: Info: Creating encoder [libx264]
[2026-03-10 16:14:17.056]: Info: Color coding: SDR (Rec. 601)
[2026-03-10 16:14:17.056]: Info: Color depth: 8-bit
[2026-03-10 16:14:17.056]: Info: Color range: JPEG
[2026-03-10 16:14:17.056]: Info: Streaming bitrate is 1000000
[2026-03-10 16:14:17.057]: Info: [libx264 @ 0x7712a53fed80] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2
[2026-03-10 16:14:17.058]: Info: [libx264 @ 0x7712a53fed80] profile High 4:4:4 Predictive, level 4.2, 4:4:4, 8-bit
[2026-03-10 16:14:17.081]: Warning: [libx264 @ 0x7712a53fed80] VBV underflow (frame 0, -43076 bits)
[2026-03-10 16:14:17.081]: Info: [libx264 @ 0x7712a53fed80] frame I:1     Avg QP:47.00  size:  8197
[2026-03-10 16:14:17.081]: Info: [libx264 @ 0x7712a53fed80] mb I  I16..4: 100.0%  0.0%  0.0%
[2026-03-10 16:14:17.081]: Info: [libx264 @ 0x7712a53fed80] coded y,u,v intra: 0.0% 0.0% 0.0%
[2026-03-10 16:14:17.081]: Info: [libx264 @ 0x7712a53fed80] i16 v,h,dc,p: 88%  0% 12%  0%
[2026-03-10 16:14:17.081]: Info: [libx264 @ 0x7712a53fed80] kb/s:3934.56
[2026-03-10 16:14:17.082]: Info: Screencasting with X11
[2026-03-10 16:14:17.083]: Info: Creating encoder [libx265]
[2026-03-10 16:14:17.083]: Info: Color coding: SDR (Rec. 709)
[2026-03-10 16:14:17.083]: Info: Color depth: 10-bit
[2026-03-10 16:14:17.083]: Info: Color range: JPEG
[2026-03-10 16:14:17.083]: Info: Streaming bitrate is 1000000
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140] Specified pixel format yuv444p10le is not supported by the libx265 encoder.
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140] Supported pixel formats:
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv420p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj420p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv422p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj422p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv444p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj444p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   gbrp
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   gray
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuva420p
[2026-03-10 16:14:17.083]: Error: Could not open codec [libx265]: Invalid argument
[2026-03-10 16:14:17.083]: Info: Creating encoder [libx265]
[2026-03-10 16:14:17.083]: Info: Color coding: SDR (Rec. 709)
[2026-03-10 16:14:17.083]: Info: Color depth: 10-bit
[2026-03-10 16:14:17.083]: Info: Color range: JPEG
[2026-03-10 16:14:17.083]: Info: Streaming bitrate is 1000000
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140] Specified pixel format yuv420p10le is not supported by the libx265 encoder.
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140] Supported pixel formats:
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv420p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj420p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv422p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj422p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuv444p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuvj444p
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   gbrp
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   gray
[2026-03-10 16:14:17.083]: Error: [libx265 @ 0x7712a53ff140]   yuva420p
[2026-03-10 16:14:17.083]: Error: Could not open codec [libx265]: Invalid argument
[2026-03-10 16:14:17.083]: Warning: Encoder [software] does not support HEVC Main10 on this system

x264 encoding succeeds but x265 is dropped due to Main10 not being available while yuv444p was reported by libx265 to be available.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804918/sunshine-moonlight-on-linux-rtx-3060-how-to-enable-yuv-444-rgb-streami

---

#### 331. Debian software RAID1 Over my head: I'm looking for pointers concerning UEFI booting alternate EFI locations if the either one fails

**问题描述 / Problem Description**:
Tags: debian, uefi, firmware, software-raid | Score: 2 | Views: 190 | Answers: 1 | Created: 2026-03-09

**解决方案 / Solution**:
The UEFI hard drive media device paths are using partition GUID. It can be shown e.g. with lsblk -o +partuuid.
UEFI boot entries are normally managed by the efibootmgr --create. You pass the Linux device node and efibootmgr will compute the necessary GUID, partition offset and partition size for you. For Linux MD RAID1 you will need to create two boot entries, one for each physical partition. I do not think Debian does it automatically in this case.
Debian actually supports having two independent copies of ESP (without RAID) and will install bootloader on each of them when updating grub. For this you set grub-efi/install_devices option of the grub-efi-amd64 package:
bor@ThinkPad-E16-Gen3:~/tmp$ sudo debconf-show grub-efi-amd64 | grep grub-efi/install_devices:
* grub-efi/install_devices: /dev/disk/by-id/nvme-eui.ace42e005580d4a9-part1
bor@ThinkPad-E16-Gen3:~/tmp$

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804885/debian-software-raid1-over-my-head-im-looking-for-pointers-concerning-uefi-boo

---

#### 332. Cant get the static ip to connect to the CUPS server

**问题描述 / Problem Description**:
Tags: ubuntu, cups, printing | Score: 2 | Views: 55 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
As default, CUPS would listen only to local host. If you want CUPS to listen to your static IP, you must configure it in /etc/cups/cupsd.conf. Make sure that the lines marked with <---- are in there (remove the arrows of course..)
# Listen on external interfaces for connections
Listen <dnsnameofyourserver>:631    <--------
Listen /var/run/cups/cups.sock

# Show shared printers on the local network.
Browsing On
BrowseOrder allow,deny
BrowseAllow all
BrowseAddress All         <-------

# Restrict access to the server...
<Location />
  Order allow,deny
  Allow localhost
  Allow All               <---------
</Location>

# Restrict access to the admin pages...
<Location /admin>
  Order allow,deny
  Allow All                <---------
</Location>


# Restrict access to configuration files...
<Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
  Allow All                       <---------
</Location>

and restart cups.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804597/cant-get-the-static-ip-to-connect-to-the-cups-server

---

#### 333. How to enable/disable Airplane Mode on Debian 13 or Ubuntu 24.04 with GNOME 48+?

**问题描述 / Problem Description**:
Tags: debian, ubuntu, wifi, gnome, networkmanager | Score: 2 | Views: 284 | Answers: 1 | Created: 2026-02-10

**解决方案 / Solution**:
On modern GNOME systems Airplane Mode is controlled by kernel rfkill, not by nmcli alone.
Enable Airplane Mode (WiFi, WWAN, Bluetooth OFF):
rfkill block all
nmcli radio all off

Disable Airplane Mode (WiFi, WWAN, Bluetooth ON):
rfkill unblock all
nmcli radio all on

Airplane Mode while keeping Bluetooth separate:
Enable (WiFi and WWAN OFF, Bluetooth unchanged):
rfkill block wifi
rfkill block wwan
nmcli radio wifi off
nmcli radio wwan off

Disable (WiFi and WWAN ON, Bluetooth unchanged):
rfkill unblock wifi
rfkill unblock wwan
nmcli radio wifi on
nmcli radio wwan on

Notes:

GNOME derives Airplane Mode state from rfkill
nmcli alone may disable radios without updating the GNOME UI
Using both tools keeps CLI and desktop state consistent

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804380/how-to-enable-disable-airplane-mode-on-debian-13-or-ubuntu-24-04-with-gnome-48

---

#### 334. How to use a "grep" result as an input of another grep, resulting in multiple lines?

**问题描述 / Problem Description**:
Tags: ubuntu, command-line, grep, pipe, windows-subsystem-for-linux | Score: 2 | Views: 924 | Answers: 5 | Created: 2025-10-29

**解决方案 / Solution**:
If you're already using awk, you don't need to use grep.  awk can do Extended Regular Expression (ERE) matches like grep -E.
And just as importantly, awk can use boolean operators (!, &&, ||, and even parentheses) with conditions/patterns, which grep can't do (although you can make a regex with alternations using | which is an OR operation).
For example:
awk -F- '/Rebuild All started/ && 
         /: (fatal|error)/ { print $1 }' build_output.txt | 
  sort -n |
  uniq

You could even write the awk script so that it stored the matches in an associative array, then sorted and printed the the output in an END block, avoiding the need for piping to sort -n | uniq.
BTW, egrep is deprecated. use grep -E instead for ERE.  With GNU grep you also have the option of using -P for PCRE

If you're not using awk, then piping the output of grep into another grep is effectively an AND operation.  If needed, you can use grep's -v option for negation.
e.g. using cut instead of awk.
grep 'Rebuild All started' build_output.txt |
  grep -E ': (fatal|error)/' |
  cut -d- -f1 |
  sort -n |
  uniq

This is objectively worse than just using awk. Every program in a pipeline has startup overhead and requires more resources (CPU time, RAM, and I/O bandwidth)...this is not as big a problem as it was a decade or two ago, we have much faster computers and storage devices now, but that's not really a good excuse to be wasteful in how we use them.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800857/how-to-use-a-grep-result-as-an-input-of-another-grep-resulting-in-multiple-li

---

#### 335. apt-get upgrade fails: a 20220329.git681281e4-0ubuntu3.40 package is missing from our jammy-updates pool. How can we catch it?

**问题描述 / Problem Description**:
Tags: ubuntu, apt, upgrade | Score: 2 | Views: 381 | Answers: 1 | Created: 2025-10-28

**解决方案 / Solution**:
The error indicates that your Artifactory repository is inconsistent — it’s referencing a package version in its indices that’s not present in its pool. The package should be in the pool, it was uploaded to the 22.04 repositories on September 18.
As far as the upgrade itself, only you can know — the rest of apt’s output should tell you what it did. A quick check is to run apt-get upgrade again; if it reports fewer than 514 packages to upgrade (I assume they were upgraded, not installed — the latter would be extremely surprising), then the upgrade did process packages other than the one it couldn’t download.
Incidentally, 514 packages to upgrade, and in particular 32 held back, is unusual for an upgrade that doesn’t involve bumping releases. But whether that indicates a problem or not depends on how the system has been maintained so far.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800826/apt-get-upgrade-fails-a-20220329-git681281e4-0ubuntu3-40-package-is-missing-fro

---

#### 336. Can AppArmor deny access to file metadata with stat()?

**问题描述 / Problem Description**:
Tags: linux, apparmor | Score: 1 | Views: 69 | Answers: 1 | Created: 2026-04-20

**解决方案 / Solution**:
AppArmor can’t fully hide a file the way chmod 000 would, because even with a deny rule the kernel may still allow metadata lookups (stat/inode info) unless you block broader filesystem access paths. what you can do is tighten the profile by denying not just read/execute but also **all filesystem access to that subtree using deny /secret/** rwmklx, plus restricting open and limiting directory traversal (and avoid giving /{,**} rwix which is way too permissive). but honestly AppArmor is not designed for “stealth filesystem” behavior, so even with tuning you may still see partial metadata leaks like stat, becuase that’s handled at VFS layer not just path access.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805542/can-apparmor-deny-access-to-file-metadata-with-stat

---

#### 337. Inkscape shows multiple ICC profile duplicated

**问题描述 / Problem Description**:
Tags: debian, duplicate-files, inkscape | Score: 1 | Views: 32 | Answers: 1 | Created: 2026-04-11

**解决方案 / Solution**:
To figure out where files come from, use dpkg -S (or dlocate -S if you have dlocate installed):
$ dpkg -S /usr/share/color/icc/colord/AdobeRGB1998.icc /usr/share/color/icc/compatibleWithAdobeRGB1998.icc
colord-data: /usr/share/color/icc/colord/AdobeRGB1998.icc
icc-profiles-free: /usr/share/color/icc/compatibleWithAdobeRGB1998.icc

Some of them are duplicated inside single packages:
$ dpkg -S /usr/share/color/icc/ghostscript/default_gray.icc /usr/share/color/icc/ghostscript/sgray.icc
libgs-common: /usr/share/color/icc/ghostscript/default_gray.icc
libgs-common: /usr/share/color/icc/ghostscript/sgray.icc

although the files themselves have very different sizes.
In some cases, file can show an embedded timestamp (along with other information):
$ file /usr/share/color/icc/colord/AdobeRGB1998.icc /usr/share/color/icc/compatibleWithAdobeRGB1998.icc /usr/share/color/icc/ghostscript/default_gray.icc /usr/share/color/icc/ghostscript/sgray.icc
/usr/share/color/icc/colord/AdobeRGB1998.icc:        ColorSync color profile 4.4, type lcms, RGB/XYZ-mntr device by lcms, 3196 bytes, 3-3-2025 17:37:57, 0xf18a476c271ccdb3 MD5 'r'
/usr/share/color/icc/compatibleWithAdobeRGB1998.icc: Microsoft color profile 2.2, type argl, RGB/XYZ-mntr device by argl, 580 bytes, 8-7-2006 3:28:47 "Compatible with Adobe RGB (1998)"
/usr/share/color/icc/ghostscript/default_gray.icc:   ColorSync color profile 2.1, GRAY/XYZ-mntr device, 2460 bytes "Artifex Software sGray ICC Profile"
/usr/share/color/icc/ghostscript/sgray.icc:          ColorSync color profile 2.1, GRAY/XYZ-mntr device, 416 bytes "Artifex Software sGray ICC Profile"

So AdobeRGB1998.icc is newer than compatibleWithAdobeRGB1998.icc; as its name suggests, the latter is a free re-implementation of the Adobe profile, but the Adobe profile has been updated since.
Some ICC v2 profiles can be viewed using tools in the argyll package. Copy the profiles to a directory where you can write, then run iccgamut to convert them to gamut files, and viewgam to produce an HTML file allowing them to be explored.
If the duplicate names really bother you, you can fix some of them by removing packages if you don’t need them (for example icc-profiles-free). In libgs-common’s case, you could report this as a bug — I don’t think it should ship profiles with duplicate names.
In any case you shouldn’t rename files shipped by packages, the renamed files will no longer be managed by the package manager.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805390/inkscape-shows-multiple-icc-profile-duplicated

---

#### 338. Dockerfile with Airflow base image wont build in Gitlab

**问题描述 / Problem Description**:
Tags: debian, docker, gitlab | Score: 1 | Views: 74 | Answers: 2 | Created: 2026-03-31

**解决方案 / Solution**:
Perhaps there's a caching problem as apt-get update works locally and Docker doesn't pull newer images unless necessary. You can use the digest of your apache/airflow:slim-2.11.2-python3.10 to ensure both computers have the same version. It's surprising that your sudo apt-get update works because I get "sudo: a terminal is required to read the password" on the latest version. You can use the Dockerfile command USER to switch to root and back:
FROM apache/airflow@sha256:32ef1c1927c47e55fd05f65e7da7b60ff7c431d0cca5c27972c7f436fff9cb56
USER root

# Debug 1
RUN sha256sum /etc/apt/sources.list.d/debian.sources /usr/share/keyrings/debian-archive-keyring.gpg
# You should see:
# fba4b66c95952e28af3fda06211991a51dc83d5448c2a4d262ec736b12323edb  /etc/apt/sources.list.d/debian.sources
# 506b815cbb32d9b6066b4a2aa524071e071761e7e7f68c3ac74f3061ba852017  /usr/share/keyrings/debian-archive-keyring.gpg

# Debug 2
RUN curl http://deb.debian.org/debian/dists/bookworm/InRelease
# Then check that the PGP SIGNATURE section printed in the GitLab Runner
# is the same as the one you see in a broswser

RUN apt-get update && \
    apt-get install -y neofetch # example
USER airflow

The other possibility is that your GitLab Runner has the wrong configuration. Let's print the Dockerfile using cat. Your entire .gitlab-ci.yml should look like:
# Replace this first half with no-tls-docker-runner is you're using that
default:
  image: docker:24.0.5-cli
  services:
    - docker:24.0.5-dind
  before_script:
    - docker info
variables:
  DOCKER_TLS_CERTDIR: "/certs"

build:
  stage: build
  tags:
    - tls-docker-runner
  script:
    - cat Dockerfile
    - docker build --no-cache --progress=plain -t my-docker-image .
    - docker run --rm -i my-docker-image bash -c neofetch
# Then verify the printed Dockerfile contents are exactly what you saved

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805238/dockerfile-with-airflow-base-image-wont-build-in-gitlab

---

#### 339. How to create launcher for an app started with command arguments - tor browser launcher does not work

**问题描述 / Problem Description**:
Tags: debian, kde, launcher, desktop-shortcuts | Score: 1 | Views: 78 | Answers: 1 | Created: 2026-03-21

**解决方案 / Solution**:
As Andrei answered above: start-tor-browser.desktop is using a relative path so the command in the answer actually only works after cd ing into the right directory first (cd /home/dir/tor-browser).
The app launcher needs to be changed like so:

Program: sh
Arguments: -c 'cd /home/dir/tor-browser && /usr/bin/firejail --profile=/etc/firejail/start-tor-browser.profile /home/dir/tor-browser/start-tor-browser.desktop'

This solved my problem. If you know of a better one or find this has a problem, write an answer or a comment instead of downvoting.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805091/how-to-create-launcher-for-an-app-started-with-command-arguments-tor-browser-l

---

#### 340. Apt refusing to download new releaseinfo after refusing once

**问题描述 / Problem Description**:
Tags: debian, apt, software-updates | Score: 1 | Views: 57 | Answers: 1 | Created: 2026-03-15

**解决方案 / Solution**:
My fix for this type of situation is to delete the relevant repository indices from /var/lib/apt/lists. Files there start with the repository hostname, so for a third-party repository deleting all files starting with the appropriate hostname should do the trick.
After removing the old indices, run apt update to download the current ones; apt won’t complain about changes in the release information.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805013/apt-refusing-to-download-new-releaseinfo-after-refusing-once

---

#### 341. How do I find out when my system last beeped?

**问题描述 / Problem Description**:
Tags: debian, audio, modprobe | Score: 1 | Views: 80 | Answers: 1 | Created: 2026-03-12

**解决方案 / Solution**:
No, I don't think there's such a log.
Have you checked if there is a fire alarm with a low battery somewhere nearby?
And an external hard drive can indeed make a beep-like sound if it moves its read/write heads around violently enough... like if it encounters a low-level read error and its firmware tells it to recalibrate its head positioning subsystem. There are even projects to make music using floppy & hard drives (and other electromechanical devices): see The Floppotron 3.0 for a very extravagant example.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804970/how-do-i-find-out-when-my-system-last-beeped

---

#### 342. How to make networking work in UML 6.18.16?

**问题描述 / Problem Description**:
Tags: debian, networking, kernel, user-mode-linux | Score: 1 | Views: 42 | Answers: 1 | Created: 2026-03-11

**解决方案 / Solution**:
eth0=tuntap syntax had been marked as obsolete that's why you see Netdevice 0.
Try replacing eth0=tuntap,umltap0 with vec0:transport=tap,ifname=umltap0,depth=128

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804936/how-to-make-networking-work-in-uml-6-18-16

---

#### 343. Display scaling of LMDE resets to default after screen resize

**问题描述 / Problem Description**:
Tags: debian, linux-mint, display-settings, gnome-boxes | Score: 1 | Views: 32 | Answers: 1 | Created: 2026-03-10

**解决方案 / Solution**:
This happens because Cinnamon is using automatic scaling instead of a fixed scale. In my case, resizing the Boxes window changed the virtual display geometry, and Cinnamon recalculated DPI and dropped effective scaling back to 100%.
Check the current setting:
gsettings get org.cinnamon.desktop.interface scaling-factor
If it returns uint32 0, that means “automatic”.
Force Cinnamon to use a fixed 200% scale instead:
gsettings set org.cinnamon.desktop.interface scaling-factor 2
You can verify it with:
gsettings get org.cinnamon.desktop.interface scaling-factor
It should now return:
uint32 2
After that, resizing the GNOME Boxes window should still change the guest resolution, but Cinnamon should keep the UI at 200% instead of reverting to 100%.
Extra note: in this setup, spice-vdagent and the virtual display resize were working normally. The real problem was Cinnamon auto-scaling (scaling-factor = 0), not Boxes itself.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804919/display-scaling-of-lmde-resets-to-default-after-screen-resize

---

#### 344. MDADM Raid 5 reading speed is slow

**问题描述 / Problem Description**:
Tags: debian, dd, io, mdadm | Score: 1 | Views: 81 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
I found a solution: I installed trixie-backport kernel.
I just double-checked an old bookworm Live CD, it worked. I tested also a brandnew trixie Live CD, it didn't worked. Conclusion: there must be something wrong in current trixie kernel.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804613/mdadm-raid-5-reading-speed-is-slow

---

#### 345. OpenBox Display Scaler

**问题描述 / Problem Description**:
Tags: ubuntu, openbox | Score: 1 | Views: 61 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
To change the screen scaling in Openbox to something more readable on the GPD's small screen:

Start a terminal emulator in Openbox and run xranadr -q | head, which will give you the display name on the start of the second line of output. On my GPD Pocket 2, the name is eDP-1.

Edit the ~/.config/openbox/autostart file to include the following line at the start:
xrandr --output <display-name> --scale 0.6


Replace <display-name> with the name of your display.
I found a scaling of 0.6 to be right for me, but you can adjust this to your liking. The lower the value, the larger everything will appear.

Close and restart Openbox.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804600/openbox-display-scaler

---

#### 346. [V2EX] Linux 桌面环境 orWM 推荐

**问题描述 / Problem Description**:
RT ，当前在用 kde plasma ，但是感觉设置项太多，我也不喜欢 QT ，想换一下
主要是想有鼠标时可以鼠标操作，出差时使用触控板进行操作，似乎 gnome 不错，但是不知道现在还稳定不，几年前用的时候动不动插件就用不了了....当然，我也只用一些基础插件。
有人用 hyprland 吗？操作体验怎么样，桌面似乎是不能显示文件吗？鼠标和触控板操作不知道怎么样，有没有老哥解答一下，我的机器是 thinkbook 14+ 2024 ultra7 版本

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1203303#reply47

---

#### 347. [V2EX] 请教一个 unraid 的 docker 网络问题

**问题描述 / Problem Description**:
unraid 系统网关指向旁路由，但是 docker 里的 qb 和 tr 用什么方法可以不走旁路由吗？ docker 的网关可以指向主路由吗？只有一个网口并没有 vlan 交换机

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1198708#reply17

---

#### 348. [V2EX] Linux 格式化 fat32/exfat 分区避坑

**问题描述 / Problem Description**:
在 linux 下把 U 盘/tf 卡格式化为 fat32 或 exfat 格式，插入手机或 windows 不能识别。因为这是 Linux 下的 fat 格式，要转换为 windows 的。！！！更改前先保存数据！！！！！！更改前先保存数据！！！！！！更改前先保存数据！！！查看原来的fdisk /dev/sdc按 p, 看到 Type 显示为 LinuxDevice     Boot Start      End  Sectors  Size Id Type/dev/sdc1        2048 31293439 31291392 14.9G 83 Linux更改为"通用"格式按 t ，

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1198633#reply24

---

#### 349. [V2EX] Linux 服务器上有多个 ip，程序本身不能指定接口，有第三方程序可以强制让程序使用指定接口吗？

**问题描述 / Problem Description**:
像 libbind 、proxychains 、部分 tsocks 这类基于 LD_PRELOAD 劫持 libc 的办法，不适合 golang 编写的程序
有比较便捷的解决方案吗？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1197941#reply17

---

#### 350. [V2EX] Ubuntu 26.04 LTS 关键变化解读

**问题描述 / Problem Description**:
Ubuntu 26.04 LTS （代号 Resolute Raccoon ）预计于 2026 年 4 月 23 日发布，作为下一代长期支持版本，它将成为未来数年企业与服务器环境的重要基础系统。相比 24.04 LTS ，本次版本的变化并不只是界面升级，而是涉及 内核、桌面架构、软件栈、应用分发和系统安全机制等多个底层领域。参考 https://mp.weixin.qq.com/s/1D2OZ3SPDU0NZcvRidAiTw

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1196785#reply5

---

#### 351. [V2EX] win11 对比 ubuntu，是真的拉胯

**问题描述 / Problem Description**:
最近购入一台 8845hs CPU 的笔记本，win11 下经常出现以下情况:win11 内置安全扫描，自动扫病毒，风扇狂转win11 自动后台更新，风扇狂转win11 什么也没做，但是 cpu 有工作，风扇会转win11 是进到桌面就开始风扇转，开浏览器看视频什么的也是会有较大风扇声音。而 ubuntu 下就安静多了，日常使用/浏览器看视频风扇几乎不转，完全听不到声音。cpu 温度也很低，当前室温 22 度，cpu 温度只有 37 度。不比不知道原来 win11 这么拉胯

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1196703#reply83

---

#### 352. [V2EX] PVELXC 容器报错 Failed to receive program message: WebSocket connection closed unexpectedly

**问题描述 / Problem Description**:
环境是双路 7K62 加上 32G*16 内存运行了 PVE 系统创建了 LXC 容器LXC 容器使用了官方的 Ubuntu 22 模板创建容器的时候默认勾选了无特权容器容器的硬件配置为 4 核心，4G 内存 8G 硬盘 8G 缓冲区然后用这个创建好的容器做了模板，复制出来 22 个容器复制的时候硬盘自动选择了链接模式这个操作是找了 GPT 写的代码复制以上 22 个容器都运行同一个计算程序，程序始终访问网络，获取数据，计算，上交数据就和挖矿那种差不多现在问题是 22 个容器同时运行几个小时里面的程序就会崩溃报错Failed to receive program message: WebSoc

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1089807#reply4

---

#### 353. [V2EX] 记录一下今天的坑： snap hostfs

**问题描述 / Problem Description**:
今天帮人看故障，现象是 firefox 无法把/opt/data/ （一个单独 mount 的 RAID 卷）作为下载目录错误信息是刚访问到/opt/层就已经 permission denied 了首先 777 ，没修复然后看日志，发现是 apparmor修改了 snap.firefox.firefox 的 apparmor profile ，加 rw ，加 audit ，能捕捉到 firefox 访问/opt/的痕迹，并且授权，但浏览器看不到里面现有的文件想了好久，终于去看了一下/proc/XXX/mounts发现这个 RAID 卷居然 mount 在了/var/lib/snapd/host

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1086841#reply7

---

#### 354. [V2EX] ubuntu22.04 热点求救

**问题描述 / Problem Description**:
nuc11atck4 装了个 ubuntu22.04一开始连接热点失败，降级 wpasupplicant 到 2.9.0 可以了现在能连上热点了，但是网络不通。。完全搜不到解决方案，求救

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1086157#reply7

---

#### 355. [V2EX] 有精简版 ubuntu 吗？

**问题描述 / Problem Description**:
大家都怎么用那种 10G 硬盘的 VPS 的，自带系统装个 ubutnu 就还剩 4G 多点，docker 镜像都下载不了几个。
保证系统必要功能，应该 2G 硬盘空间就能做到了吧，印象中 debian 就是这个值。我这边有的工具只有 ubuntu 才能直接使用，debian 有点问题。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1080458#reply13

---

#### 356. [V2EX] 求助： ubuntu 现在 ssh 不能直接 root 账户登录了？

**问题描述 / Problem Description**:
服务器一直用 24 年以前的 20.04 版本，为了不同设备登录方便不想用密钥，所以都设置成了直接 root 用户密码登录。在之前就发现用新版 22/24 的就无法直接设置 root 密码登录，设置点登录一直重复弹输入密码，这两天新安装 20.04 发现也不能直接用 root 登录了。。。搜了好半天好像没有讲过这个的，有遇到一样情况的吗？是否新版设置了什么权限需要多修改哪些地方呢？之前一直是在/etc/ssh/sshd_config 里面修改PermitRootLogin yesPasswordAuthentication yes然后重启 ssh ，就可以直接设置 root 和密码登录了，但现

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1078064#reply17

---

#### 357. [V2EX] Droidian 在 redmi note7 上，使用 docker，老是重启

**问题描述 / Problem Description**:
用旧手安装 Droidian ，安装 docker 。安装 dockge ，只要访问 dockge 页面，手机就重启。不访问 dockge 页面，正常得很，不会重启。大佬们还有有什么排查手段嘛？1. 查看重启记录last reboot 没有重启的记录2. dmesg -w 查看内核的打印，没有看出异常。3. docker logs 也没有异常。还有其他思路嘛？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1019336#reply4

---

#### 358. [V2EX] debian12 关不了机

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1018014#reply7

---

#### 359. [V2EX] debian 11 安装很慢是怎么回事？

**问题描述 / Problem Description**:
在 vmware 上安装 debian11 ，这一步总是卡很长时间，上一步尝试选择华为云源也卡在这里。这一步是在干什么？用的是 3.7G 的完整版镜像，按理说不用联网啊。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1006490#reply3

---

#### 360. [V2EX] apt install 安装的东西附带的依赖 为什么在 purge 之后 autoremove 删不掉

**问题描述 / Problem Description**:
是有其他组件依赖吗  为什么总感觉 debian 删东西删不干净

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1000277#reply3

---

#### 361. [V2EX] 求 Linux 系统资源探针

**问题描述 / Problem Description**:
如题，现在有一个 Debian12 ，轻度使用，挂了一些服务，想挂个探针，提供 web 界面，方便查看。
看了一下哪吒探针之类的，挺麻烦的，要部署两端。试了试 netdata ，内存占用太大了，不好。
求助 v 友有没有合适的探针软件，要求：

单台部署，部署不要太复杂，最好傻瓜式装上就能用，可以接受一点点折腾。
自身资源占用别太离谱，内存最好别超 100m
web 界面支持，能看、方便看就行

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/994208#reply11

---

#### 362. [V2EX] GLM 的稳定性是不是太离谱了？

**问题描述 / Problem Description**:
刚刚续费了季度 Pro 套餐，就开始疯狂报错
API Error: 400 {"type":"error","error":{"message":"网络错误，错误 id 20260427233129a7ee7f005e494d82 ，请稍后重试。","code":"1234"},"request_id":"20260427233129a7ee7f005e494d82"}   *  10  
续费季度之前都很少碰到这个，就离谱。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208961#reply3

---

#### 363. [V2EX] 买 mac 还是转 Linux 系统

**问题描述 / Problem Description**:
CPU                                          

Intel Core i7-8550U @ 1.80GHz （睿频 4.0GHz ）                                
4 核 8 线程, 8MB L3 缓存                                                    

内存                                                                          

16GB DDR4 （已用 4.4GB ，可用 11G

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208943#reply22

---

#### 364. [V2EX] opencode go 的 DeepSeek 是官方直连吗

**问题描述 / Problem Description**:
今天看了下 DeepSeekV4 的次数涨了不少，估算了下 token 好像吃上折上折了？
预估了一下 token 量，算上缓存的话
一个 go 套餐里，DeepSeek V4 Flash 已经约等于	10,923,420,500     token 了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208931#reply1

---

#### 365. [V2EX] 为什么我感觉 Codex 审美好差

**问题描述 / Problem Description**:
我之前用 Flutter ，通过 Gemini 写了一个学英语的 App ，最近想迭代功能，感觉 Flutter 很多细节上不太满意，决定换成 macOS 原生开发了。找 Codex 开发，GPT-5.5 + Extra High ，重构是比较顺利，可以跑起来，但是真的，太丑了。
然后 macOS 左上角那三个按钮，就是长得像红绿灯的东西，和顶栏其它的元素（ 2 个收起/展开按钮，标题），让 Codex 反复改，几个小时过去了还是各种问题。最后给我整崩溃了，换成 Gemini ，虽然也是磕磕绊绊，但肉眼可见地方向正确，最后花了一个多小时调好了。
后续我又花了几个小时通过 Gemini 把丑到爆

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208925#reply8

---

#### 366. [V2EX] 你们有没有遇到过，通过梯子看 youtube 高清视频的时候，竟然会导致全家的 wifi 异常断开

**问题描述 / Problem Description**:
只要一开梯子看高清就这样，这是什么原理，电脑开的，手机 wifi 居然也显示异常

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208916#reply8

---

#### 367. [V2EX] 全新未拆封 Sandisk 256G SD 卡转让

**问题描述 / Problem Description**:
全新未拆封, 因为买错了, dji action6 好像用不了这个卡, 有意者联系 VX:SGVybWl0aXN0

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208912#reply4

---

#### 368. [V2EX] 公司开始严查访问境外网络，如何破局

**问题描述 / Problem Description**:
1. 办公电脑为 window11 ，上面装有公司的 EDR2. 办公电脑访问的公司的网络有办法绕过公司的检测么？各位大神出出招

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208909#reply54

---

#### 369. [V2EX] 不同 AI 平台的历史记录聚合，有什么好方法吗

**问题描述 / Problem Description**:
因为没有固定用某个 AI 的习惯，都是一阵子用这家，一阵子用那家，导致历史记录散落在各个平台。有时候想找一个以前问过的东西，但不记得在哪问的了，还得每个平台都找一遍。有的像 deepseek 官网连搜索都没有，更麻烦。不知道有没有什么办法可以把各家官网的历史记录聚合到一处管理。虽然可以用三方客户端+API 来统一入口，但那样就要花钱，感觉没啥必要。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208907#reply3

---

#### 370. [V2EX] 这么多年了微信的开发文档还是当年那个味道

**问题描述 / Problem Description**:
很多年前就已经见识了微信的开发文档,解决方案全靠社区踩坑,今天因为一个业务需要看下文档,还是当年的味道,通知消息还只支持 xml,各种含糊不清楚,到处超链接,有没有社区整理的文档

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208886#reply0

---

#### 371. [V2EX] 最近配了一台新的台式电脑，我想在外面笔记本上可以远程回去直接玩游戏，求方案

**问题描述 / Problem Description**:
求各位大佬指点一下，来个方案，不要远程软件，例如：向日葵，todesk 等

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208878#reply29

---

#### 372. [V2EX] 目前用国模 vibe coding 现状

**问题描述 / Problem Description**:
glm 买不到
kimi 高峰算力不足，高峰算力不足，。。。
deepseek 没有 coding plan 兜底，怕扣钱太快。
mimo 感觉实力不行，用的欲望不大，也没有性价比。
Qwen 没有用过，大家有用过的评价下。
minimax  你是谁？？？
各位大佬们，可以提供一些国模的购买渠道吗？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208875#reply3

---

#### 373. [V2EX] 貌似 Raycast 要改成 Web 套壳了，有平替吗

**问题描述 / Problem Description**:
https://x.com/ktiays/status/2048304683916423244
看了这个帖子，特么一个常驻工具内存占用快 2G ，实在受不了，自带的 AI 更是依托
当我发现他发布 windows 版后就该清楚有这一天的
其实我用 raycast 的功能很少，但是可以集中在一起：

剪贴板：可以搜索，显示复制来源，富文本也能显示
Snippets：这个主要可以设置一些占位符，比如 {copy}, {time} 这些，根据当前复制内容自动应用，这个我感觉要找平替可能很困难
Window Management：这个在我使用 Raycast 之前用的是 Magnet
Quicklin

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208869#reply14

---

#### 374. [V2EX] 基于 clangd 的函数定义查找，不能找第三方库代码的实现吗？ 用的 vtk

**问题描述 / Problem Description**:
vscode 自带的 intelliSense 感觉有时找到的函数定义不对试了下 clangd ，发现找不到第三方库代码的实现吗？  用的 vtk改成 cl.exe 或 clang-cl.exe 都找不到第二层函数实现，只能找到我的函数调用的第一层vscode 设置    "cmake.generator": "Ninja",    "cmake.configureSettings": {        "CMAKE_C_COMPILER": "clang-cl",        "CMAKE_CXX_COMPILER": "clang-cl",        "CMAKE_EXPORT_CO

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208859#reply1

---

#### 375. [V2EX] 字节这 Code Plan 诈骗吧

**问题描述 / Problem Description**:
每 5 小时：最多约 1,200 次请求

就问了 2 两个问题额度就耗光了，第 2 个问题刚好卡中间浪费时间。总共估计 100 次请求左右，它这是怎么计算的，10 倍吗！
卖不起就别卖，标的很高骗人进去，挂羊头卖狗肉

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208842#reply12

---

#### 376. [V2EX] 求稳定 GLM-5.1 接口推荐

**问题描述 / Problem Description**:
目前在用 OpenCode Go 的 GLM-5.1 套餐，整体响应速度和稳定性都不错，体验挺好。
但用量消耗很快，才使用一周就已经耗掉 65%~70% 额度，眼看就要不够用了。
之前也试过百度、火山引擎的相关套餐，同样是跑 GLM-5 ，体验很差，基本没法正常使用。智谱官网的 Coding 套餐长期缺货，完全抢不到。
想问问各位大佬有没有合适的替代方案：
优先海外站点，国内平台普遍网络卡顿严重；
预算控制在 20 美元以内；
主打稳定流畅跑 GLM5 系列，性价比高。
求靠谱海外 AI 接口 / 套餐推荐，感谢～

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208841#reply7

---

#### 377. [V2EX] 求推荐一个玩 hermes 或者 openclaw 的大模型

**问题描述 / Problem Description**:
大家来推荐一下给我玩 hermes 和 openclaw 的相关的模型呀，要聪明的，费用适中

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208810#reply19

---

#### 378. [V2EX] [开源分享] Worktree Manager - 多 Repo 的工作区管理工具，多 Repo 场景一定要看一下

**问题描述 / Problem Description**:
前置话题是一个来自 2024 年的问题： https://www.v2ex.com/t/1046409原文如下：-----最近任务交叉进行开发，经常在开发 A 任务的时候，B 任务有点问题要改或者需要优化。这个时候需要切换分支，重新编译，然后重新打开页面开始开发。但是有的任务是单项目，有的任务是多项目，这么一套流程下来手速快一点慢倒是不慢，就是单纯的感觉在浪费时间。所以我在想有没有这么一个东西，可以直接把当前系统打开的应用/浏览器页面以及位置和窗口大小都给保存下来，有点类似 VMware 的快照，除此之外还可以来回切换，像 git 的分支管理那样，切到 B 任务快照开发完提交后可以继续切回主时

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208798#reply2

---

#### 379. [V2EX] 现在还有什么 gpt 账号 plus 的渠道吗？号商别再内斗了

**问题描述 / Problem Description**:
之前 7 块钱一个月的 plus 是真的香有的话偷偷说别再发帖直接掀桌子了

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208785#reply33

---

#### 380. [V2EX] 家人们 cursor 与 windsurf 二选一怎么选呢？

**问题描述 / Problem Description**:
背景
Claude 账号被 ban 了，目前手上只剩 Codex 还在服役。这段时间跟 Claude 斗智斗勇属实心累，不想再折腾了，想着干脆转 Cursor 或者 Windsurf 算了。
纠结点
Cursor 和 Windsurf 看起来都还行，想问问老哥们哪个更耐用点
Cursor 我看有 Pro+ 是 3x 的用量
Windsurf 只有 pro 上一层就是 Max 了

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208781#reply30

---

#### 381. [V2EX] 话说怎么重置 coding plan 的使用指针能够最大化在白天使用 token?

**问题描述 / Problem Description**:
比如 GLM 的 coding plan 是 5 小时重置一次，我假设让 cc 接 GLM api 在早上 6 点发出第一个请求，那么我能使用的区间是 06:00 → 11:00,然后 11:00 → 16:00 ，最后是 16:00 到 18:00 能够最大化使用，但是我 vibe 了很久，都没法让 claude 去请求一次 api ，好像是因为是交互式的，有没有佬出个主意

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208766#reply4

---

#### 382. Valve announces the Steam Controller will go on sale on May 4th at $99 USD

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sxfq2b/valve_announces_the_steam_controller_will_go_on/

---

#### 383. Why didn't I switch to Linux earlier... my PC is running like butter

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sxfopo/why_didnt_i_switch_to_linux_earlier_my_pc_is/

---

#### 384. Ubuntu Linux Will Begin Landing AI Features Throughout The Next Year

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sxc748/ubuntu_linux_will_begin_landing_ai_features/

---

#### 385. Kdenlive 26.04.0 is out, featuring contributions from more developers than ever before. This release focuses on stability, usability, and workflow improvements and comes with new features like animated transition previews and monitor mirroring.

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx1rhh/kdenlive_26040_is_out_featuring_contributions/

---

#### 386. The future of AI in Ubuntu

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx1795/the_future_of_ai_in_ubuntu/

---

#### 387. I wrote documentation about compiling the kernel

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx9gvb/i_wrote_documentation_about_compiling_the_kernel/

---

#### 388. The Linux Kernel Tree About To Hit 40 Million Lines, AMD Driver Above 6 Million Lines

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swhvgd/the_linux_kernel_tree_about_to_hit_40_million/

---

#### 389. The RADV Vulkan driver is adding memory protection using AMD Trusted Memory Zone

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sxh5tf/the_radv_vulkan_driver_is_adding_memory/

---

#### 390. Linux 7.1 enables PREEMPT_RT on 32-bit ARM

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx4qp8/linux_71_enables_preempt_rt_on_32bit_arm/

---

#### 391. XWayland 24.1.11 Brings Crash Fixes

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx4pok/xwayland_24111_brings_crash_fixes/

---

#### 392. Trinity Desktop Environment R14.1.6 released

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swxvgh/trinity_desktop_environment_r1416_released/

---

#### 393. Pack2TheRoot (CVE-2026-41651): Cross-Distro Local Privilege Escalation Vulnerability

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sww9u0/pack2theroot_cve202641651_crossdistro_local/

---

#### 394. Linux 7.1-rc1 is released with the new NTFS driver, Intel FRED by default and much more

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swvqif/linux_71rc1_is_released_with_the_new_ntfs_driver/

---

#### 395. Created an OSD app for wayland compositors.

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx2rip/created_an_osd_app_for_wayland_compositors/

---

#### 396. Asahi Linux Progress Report: Linux 7.0

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swbzo3/asahi_linux_progress_report_linux_70/

---

#### 397. Wayland-Wheeltani : Small Rust daemon for middle-click scroll on linux Wayland

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sxh5ga/waylandwheeltani_small_rust_daemon_for/

---

#### 398. The new Linux kernel AI bot uncovering bugs is a local LLM on Framework Desktop + AMD Ryzen AI Max

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sw5jvn/the_new_linux_kernel_ai_bot_uncovering_bugs_is_a/

---

#### 399. Spent a weekend getting postmarketOS on a OnePlus 6T as a proper daily driver – here's what actually works

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sx3lt4/spent_a_weekend_getting_postmarketos_on_a_oneplus/

---

#### 400. [Announcement] CachyOS April 2026 Release Changelog

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swcbfg/announcement_cachyos_april_2026_release_changelog/

---

#### 401. Transparent Proxy Matrix: Mullvad over obfs4 Tor Transport

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1swuv8i/transparent_proxy_matrix_mullvad_over_obfs4_tor/

---

#### 402. LEKTRA - High performance Document and Image Viewer, v0.7.0 released!

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sw3ahj/lektra_high_performance_document_and_image_viewer/

---

#### 403. I added 12VHPWR/12V-2x6 power connector monitoring to LACT (Linux GPU tool)

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1sw85kq/i_added_12vhpwr12v2x6_power_connector_monitoring/

---

#### 404. Colorado Open Source Exemption Could Save Linux From Age Verification Rules

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1svch3p/colorado_open_source_exemption_could_save_linux/

---

#### 405. Microsoft Reportedly Looking At Rebasing Azure Linux On Fedora

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1svdqcd/microsoft_reportedly_looking_at_rebasing_azure/

---

#### 406. niri v26.04, with blur

**问题描述 / Problem Description**:
Reddit r/linux discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux/comments/1svkhl2/niri_v2604_with_blur/

---

#### 407. Teams guest access stuck in the loop

**问题描述 / Problem Description**:
Reddit r/sysadmin discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/sysadmin/comments/1sxijk1/teams_guest_access_stuck_in_the_loop/

---

#### 408. Any advice for choosing a good KVM Switch for my PC/Laptop setup with three monitors?

**问题描述 / Problem Description**:
Reddit r/sysadmin discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/sysadmin/comments/1sxij64/any_advice_for_choosing_a_good_kvm_switch_for_my/

---

#### 409. Sudo insults

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxh8w2/sudo_insults/

---

#### 410. Best way to learn Linux from the very low level. Need help 🙏

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxcoag/best_way_to_learn_linux_from_the_very_low_level/

---

#### 411. Which terminal emulator features are you actually using?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1swzphp/which_terminal_emulator_features_are_you_actually/

---

#### 412. Why is people still afraid of Linux?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1swv68m/why_is_people_still_afraid_of_linux/

---

#### 413. Find HW Information about networked device

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxd0ag/find_hw_information_about_networked_device/

---

#### 414. How good do MediaTek chipsets work with Linux?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxf4wb/how_good_do_mediatek_chipsets_work_with_linux/

---

#### 415. Problem with DaVinci Resolve

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxi1j2/problem_with_davinci_resolve/

---

#### 416. Best way to get into using Linux as a daily driver? (From PoV of a semi-power user)

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx98rd/best_way_to_get_into_using_linux_as_a_daily/

---

#### 417. Chromebook doesn’t detect usb that has Linux mint on it

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxdkbh/chromebook_doesnt_detect_usb_that_has_linux_mint/

---

#### 418. How to set wifi CA certificate to do not validate/problems connecting to wpa3 wifi

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxgxwa/how_to_set_wifi_ca_certificate_to_do_not/

---

#### 419. I have a MacBook, what distro should I use?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxa4gy/i_have_a_macbook_what_distro_should_i_use/

---

#### 420. A small question on VMs

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxcp35/a_small_question_on_vms/

---

#### 421. [Arch/Wayland] Android Studio (Flatpak version) crashes on start

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxbxrz/archwayland_android_studio_flatpak_version/

---

#### 422. Random freezing that forces me to fully power off and on my computer (CachyOS)

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxfkm8/random_freezing_that_forces_me_to_fully_power_off/

---

#### 423. having trouble with ipod

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxf8da/having_trouble_with_ipod/

---

#### 424. Seemingly random full freezes, only "fixed" by a reboot

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxda7e/seemingly_random_full_freezes_only_fixed_by_a/

---

#### 425. Melhor OS para um notebook antigo?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sximzb/melhor_os_para_um_notebook_antigo/

---

#### 426. Wishlist for a linux/Mac dual-boot

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx8a75/wishlist_for_a_linuxmac_dualboot/

---

#### 427. Meta+Letter doesn't work as a keyboard shortcut

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxi8i4/metaletter_doesnt_work_as_a_keyboard_shortcut/

---

#### 428. How to get a linux server distro on a Ideapad 110

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxhwdl/how_to_get_a_linux_server_distro_on_a_ideapad_110/

---

#### 429. What's a good video tool that's really basic, for cropping and trimming gifs and videos?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sxa8fw/whats_a_good_video_tool_thats_really_basic_for/

---

#### 430. Elgato button on my keyboard - what can I do with it??

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx66lf/elgato_button_on_my_keyboard_what_can_i_do_with_it/

---

#### 431. Is there anything I should configure on my Acer Laptop before switching?

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx5yh4/is_there_anything_i_should_configure_on_my_acer/

---

#### 432. Laptop internal microphone picks up loud fan and speaker noise. Doesn't happen on Windows.

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx4fgk/laptop_internal_microphone_picks_up_loud_fan_and/

---

#### 433. Need some advice regarding linux distros

**问题描述 / Problem Description**:
Reddit r/linuxquestions discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxquestions/comments/1sx1paa/need_some_advice_regarding_linux_distros/

---

#### 434. Upvote this post if your install of Ubuntu 26.04 went technically well

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1svap68/upvote_this_post_if_your_install_of_ubuntu_2604/

---

#### 435. Ubuntu 26.04 ("Resolute Raccoon") LTS released

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1stutc8/ubuntu_2604_resolute_raccoon_lts_released/

---

#### 436. Ubuntu 26.04 is amazing!

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxc074/ubuntu_2604_is_amazing/

---

#### 437. Windows 7 is that you?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxe6og/windows_7_is_that_you/

---

#### 438. Ubuntu 26.04 installed

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx4q1i/ubuntu_2604_installed/

---

#### 439. Just update it 26.04

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sws3o4/just_update_it_2604/

---

#### 440. The future of AI in Ubuntu

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx22ve/the_future_of_ai_in_ubuntu/

---

#### 441. Why am I facing this again and again

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxahh8/why_am_i_facing_this_again_and_again/

---

#### 442. Overnight Canonical pushed out a PackageKit fix for a 8.8 CVE for 26.04

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx2l64/overnight_canonical_pushed_out_a_packagekit_fix/

---

#### 443. How are AMD drivers for games?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxd2lo/how_are_amd_drivers_for_games/

---

#### 444. Just upgraded to Ubuntu 26.04, wow...

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swynlt/just_upgraded_to_ubuntu_2604_wow/

---

#### 445. Firefox starting very slowly on 26.04

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxfzla/firefox_starting_very_slowly_on_2604/

---

#### 446. Ubuntu 26.04 - clean install - ssh username messed up...

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxc46l/ubuntu_2604_clean_install_ssh_username_messed_up/

---

#### 447. What is the meaning of "3"?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swm2t0/what_is_the_meaning_of_3/

---

#### 448. 26.06 LTS and Microsoft Intune support

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx49fb/2606_lts_and_microsoft_intune_support/

---

#### 449. Would you recommend switching from Debian 13 to Ubuntu 26.04 for better laptop battery life?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxiojl/would_you_recommend_switching_from_debian_13_to/

---

#### 450. Operation Progress extension

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxiliu/operation_progress_extension/

---

#### 451. Lagging when compile angular app

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxigwf/lagging_when_compile_angular_app/

---

#### 452. Ubuntu 26.04

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sxhzrx/ubuntu_2604/

---

#### 453. Updated finally to 26.04 LTS and its amazing in resource utilization

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swtyrb/updated_finally_to_2604_lts_and_its_amazing_in/

---

#### 454. error when launching an appimage file

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx0i0o/error_when_launching_an_appimage_file/

---

#### 455. Kubuntu 26.04 (Plasma 6.6, Wayland) — Clipboard truncates long text when pasting between apps. Anyone found a fix?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swz489/kubuntu_2604_plasma_66_wayland_clipboard/

---

#### 456. Just installed 26.04 - experiencing micro stuttering

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swtmbk/just_installed_2604_experiencing_micro_stuttering/

---

#### 457. Will Ubuntu 26.04get Gnome 50.1?

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1swt757/will_ubuntu_2604get_gnome_501/

---

#### 458. Help: Eth0 On/Off switch button defaults to Off after every reboot

**问题描述 / Problem Description**:
Reddit r/Ubuntu discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/Ubuntu/comments/1sx4opx/help_eth0_onoff_switch_button_defaults_to_off/

---

#### 459. Still on Windows 7? Don't want Windows 10? Consider switching to Linux (and specifically, Ubuntu). A Guide.

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/ejsz3v/still_on_windows_7_dont_want_windows_10_consider/

---

#### 460. Distrochooser: "Welcome! This test will help you to choose a suitable Linux distribution for you"

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/hd1ghl/distrochooser_welcome_this_test_will_help_you_to/

---

#### 461. If you have an old laptop and a kid in your life, here's a simple project I built

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sx0c4o/if_you_have_an_old_laptop_and_a_kid_in_your_life/

---

#### 462. Win 11 user here, I want to switch to linux

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxcjqw/win_11_user_here_i_want_to_switch_to_linux/

---

#### 463. So pissed of Windows, I want to go back to Linux : should I go on Ubuntu 26.04 despite its increased RAM requirements, or is there better RAM and resources friendly alternatives Linux distros ?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxgagw/so_pissed_of_windows_i_want_to_go_back_to_linux/

---

#### 464. I'm super done with windows. Considerig either Mint or CashyOS

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxhazh/im_super_done_with_windows_considerig_either_mint/

---

#### 465. Difference between "normal" distro and LTS version?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxhkxm/difference_between_normal_distro_and_lts_version/

---

#### 466. What's up with 100% GPU usage drawing 50% power?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxg0n0/whats_up_with_100_gpu_usage_drawing_50_power/

---

#### 467. Newbie Updates Mint-Oops

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxfsqv/newbie_updates_mintoops/

---

#### 468. Thoughts on installing on lenovo IdeaPad duet 3 for light dev work on the go

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sx6byo/thoughts_on_installing_on_lenovo_ideapad_duet_3/

---

#### 469. How to back up a flatpak? (including the executable)

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxihfz/how_to_back_up_a_flatpak_including_the_executable/

---

#### 470. New Linux user on HP2133

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sxifdu/new_linux_user_on_hp2133/

---

#### 471. Brightness issue on LG Gram OLED screen

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sx90cz/brightness_issue_on_lg_gram_oled_screen/

---

#### 472. Whats the point of using ssh keys with passphrases?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swod0o/whats_the_point_of_using_ssh_keys_with_passphrases/

---

#### 473. CachyOS Issues

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sx7wuu/cachyos_issues/

---

#### 474. Disable power on/wake up on key press (No BIOS option available)

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swxkjg/disable_power_onwake_up_on_key_press_no_bios/

---

#### 475. I think mi laptop doesn't let me install any linux

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swoym1/i_think_mi_laptop_doesnt_let_me_install_any_linux/

---

#### 476. Photo Station Uploader on Linux?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swyucg/photo_station_uploader_on_linux/

---

#### 477. BleachBit 6.0 for Linux finally adds selective cookie control and deeper browser cleaning

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swix5u/bleachbit_60_for_linux_finally_adds_selective/

---

#### 478. Why Does This Work

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swqrsk/why_does_this_work/

---

#### 479. Failed to update APT cache. While l am trying to install makedeb (l am on linux mint 21.3 xfce as l remember l start using linux 2 days ago)

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1sx16jf/failed_to_update_apt_cache_while_l_am_trying_to/

---

#### 480. Hide run0 message

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swyjke/hide_run0_message/

---

#### 481. Best practices for switching distros?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swp1y2/best_practices_for_switching_distros/

---

#### 482. Distro ?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swt8yg/distro/

---

#### 483. I want a customizable computer, what Linux distribution should i go for?

**问题描述 / Problem Description**:
Reddit r/linux4noobs discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linux4noobs/comments/1swdza8/i_want_a_customizable_computer_what_linux/

---

#### 484. envocabulary — find which file:line set every variable in your shell

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1swy57w/envocabulary_find_which_fileline_set_every/

---

#### 485. kotofetch: Customizable Japanese quotes in the terminal with translation and Anki import

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sw5x90/kotofetch_customizable_japanese_quotes_in_the/

---

#### 486. Project Yellow Olive - Pokemon Yellow inspired Kubernetes TUI game

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sw6kl4/project_yellow_olive_pokemon_yellow_inspired/

---

#### 487. Spark ( Standard Python Ascii RPG Kit) Ascii RPG Python Game Engine.

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sw9xjj/spark_standard_python_ascii_rpg_kit_ascii_rpg/

---

#### 488. What is a CLI tool or script that you use that you sometimes wish had a GUI for yourself, or to share with less tech savvy friends and co-workers?

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1swuca3/what_is_a_cli_tool_or_script_that_you_use_that/

---

#### 489. A minimal, lightning-fast typing TUI for your terminal

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sv7thb/a_minimal_lightningfast_typing_tui_for_your/

---

#### 490. Jumping to recently used directories

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1svavr9/jumping_to_recently_used_directories/

---

#### 491. Yazi plugin for some nice deluxe coloring

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1svg0jj/yazi_plugin_for_some_nice_deluxe_coloring/

---

#### 492. zsh-sage: A smarter autosuggestions that learn from your habits [zsh plugin]

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sv5ivz/zshsage_a_smarter_autosuggestions_that_learn_from/

---

#### 493. Advice on CLI creation in python

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1svftek/advice_on_cli_creation_in_python/

---

#### 494. I created a small tool to save, manage, and quickly run frequently used commands.

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1svbiv2/i_created_a_small_tool_to_save_manage_and_quickly/

---

#### 495. parfit — a codebase-aware comment reflow tool written in Rust

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1stzv2x/parfit_a_codebaseaware_comment_reflow_tool/

---

#### 496. Directory bookmarking in Rust (looking for feedback)

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1stjetf/directory_bookmarking_in_rust_looking_for_feedback/

---

#### 497. R2 D2 Monitor - TUI for monitoring on Windows

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1st5v1w/r2_d2_monitor_tui_for_monitoring_on_windows/

---

#### 498. I made a browser based Command line game to learn basics of Linux.

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1ssl20t/i_made_a_browser_based_command_line_game_to_learn/

---

#### 499. So I noticed that OSC 12 (cursor color) isn’t being applied correctly in my setup.

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1ssujfd/so_i_noticed_that_osc_12_cursor_color_isnt_being/

---

#### 500. New rule: List similar and alternative software & how yours is different (if applicable)

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1ss58x6/new_rule_list_similar_and_alternative_software/

---

#### 501. Pushing a Linux shell experience further in a static website

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sryqja/pushing_a_linux_shell_experience_further_in_a/

---

#### 502. Bifrost: Transfer files between devices via QR code from the terminal

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sr8enj/bifrost_transfer_files_between_devices_via_qr/

---

#### 503. typing-game-cli@7.1.0 - CLI game to practice your typing speed by competing against typer-robot or against your best result

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1srdtws/typinggamecli710_cli_game_to_practice_your_typing/

---

#### 504. The future of Saul...

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sqt3du/the_future_of_saul/

---

#### 505. Zen - A MacOS tool to reduce distractions when working or studying.

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sqtwkn/zen_a_macos_tool_to_reduce_distractions_when/

---

#### 506. What are your terminal editor of choice?

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1spxkri/what_are_your_terminal_editor_of_choice/

---

#### 507. gitoverit: status all your repos at once, and more! (OSS, MIT)

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sp1k3k/gitoverit_status_all_your_repos_at_once_and_more/

---

#### 508. repolyze CLI analyzes source code pain points (bugs and security hotspots) from git history

**问题描述 / Problem Description**:
Reddit r/commandline discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/commandline/comments/1sp3i9h/repolyze_cli_analyzes_source_code_pain_points/

---

#### 509. It is no longer Microsoft Monday

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1kl80ch/it_is_no_longer_microsoft_monday/

---

#### 510. Desktop Screenshot Megathread

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rtz4wc/desktop_screenshot_megathread/

---

#### 511. archarcharcharcharch

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sxdq52/archarcharcharcharch/

---

#### 512. Built for a hostile internet: Canonical VP of Engineering on Ubuntu 26.04 LTS

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sx4j8l/built_for_a_hostile_internet_canonical_vp_of/

---

#### 513. HELP!!! Annoying errors from Appimage flooding my system notifications

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1swz2ne/help_annoying_errors_from_appimage_flooding_my/

---

#### 514. Linus Torvalds uses Fedora

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1suo6gs/linus_torvalds_uses_fedora/

---

#### 515. Why so ignorant bro?

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1srdsdp/why_so_ignorant_bro/

---

#### 516. They've come to accept it

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1so9i29/theyve_come_to_accept_it/

---

#### 517. People saying that never even tried. The best Photoshop alternative for Linux is Krita

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1skyi89/people_saying_that_never_even_tried_the_best/

---

#### 518. "tell it that amd is better anyways"

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sklfef/tell_it_that_amd_is_better_anyways/

---

#### 519. I'm not going to be an unpaid tech support employee for somebody that is not willing to learn

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sgul15/im_not_going_to_be_an_unpaid_tech_support/

---

#### 520. Only tierlist you’ll ever need

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sgymli/only_tierlist_youll_ever_need/

---

#### 521. Librebooting and decking out a ThinkPad T430

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sey1xb/librebooting_and_decking_out_a_thinkpad_t430/

---

#### 522. Trying Linux Mint on my Thinkcentre Tiny M75Q-1. Got this to use when I do not require my gaming pc in order to reduce energy usage and heat in my home office as summer is about to get going here. Pretty good so far uses about 40W vs 300+ for gaming rig. cheaper and less hot when not gaming.

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1sfamna/trying_linux_mint_on_my_thinkcentre_tiny_m75q1/

---

#### 523. Is the distro idiot proof? Then it's for me

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1se2h3v/is_the_distro_idiot_proof_then_its_for_me/

---

#### 524. It's pretty solid to be honest

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1s9jwsy/its_pretty_solid_to_be_honest/

---

#### 525. Linux kernel czar says AI bug reports aren't slop anymore

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1s6biiv/linux_kernel_czar_says_ai_bug_reports_arent_slop/

---

#### 526. I see. Don't worry. That's because an idiot recommended that distro as your first experience

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1s3auxz/i_see_dont_worry_thats_because_an_idiot/

---

#### 527. Don't worry, dad, you will learn and be glad you did

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rzt9dg/dont_worry_dad_you_will_learn_and_be_glad_you_did/

---

#### 528. Goodbye, old machine.

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rx3ukk/goodbye_old_machine/

---

#### 529. Ukraine is using Linux (Ubuntu) for their anti-drone systems

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rwm441/ukraine_is_using_linux_ubuntu_for_their_antidrone/

---

#### 530. Like opening a can of worms

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rvx8tw/like_opening_a_can_of_worms/

---

#### 531. Why spend when I can enjoy suffering for free? (It's part of the experience)

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rtwjli/why_spend_when_i_can_enjoy_suffering_for_free_its/

---

#### 532. Nanny state vs. Linux: show us your ID, kid

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rssjcz/nanny_state_vs_linux_show_us_your_id_kid/

---

#### 533. Be glad that you are free. Free to change your mind. Free to go most anywhere anytime.

**问题描述 / Problem Description**:
Reddit r/linuxmasterrace discussion

**解决方案 / Solution**:
See Reddit thread for community solutions and troubleshooting steps.

**参考链接 / References**:
- https://www.reddit.com/r/linuxmasterrace/comments/1rr3oxl/be_glad_that_you_are_free_free_to_change_your/

---

#### 534. [V2EX] AI 中转站避坑指南：立刻停用"无缓存"中转，钱烧得比正常快 4 倍以上

**问题描述 / Problem Description**:
最近在评测一些 Claude 中转站，发现一个大坑，写出来给大家避一避。先说结论：选中转站，必须确认它真正支持提示词缓存。不支持的、或者用"假缓存"的，单价再便宜也是陷阱。为什么这是个坑？Claude 官方接口有个特性叫提示词缓存：把长系统提示词、长上下文缓存住，5 分钟内复用，缓存读取价格只有正常输入的十分之一（ Sonnet 是每百万 token 0.3 美元 vs 3 美元）。写入缓存本身比正常输入略贵（每百万 token 3.75 美元），但只要后续命中，平摊下来非常划算。为什么有些中转站会一直在写缓存？我研究了一下，主要有三种情况：1：号池不稳定，频繁切换账号。每换一个账号，缓存就重

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208975#reply1

---

#### 535. [V2EX] 买 mac 还是转 Linux 系统

**问题描述 / Problem Description**:
CPU                                          

Intel Core i7-8550U @ 1.80GHz （睿频 4.0GHz ）                                
4 核 8 线程, 8MB L3 缓存                                                    

内存                                                                          

16GB DDR4 （已用 4.4GB ，可用 11G

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208943#reply25

---

#### 536. [V2EX] opencode go 的 DeepSeek 是官方直连吗

**问题描述 / Problem Description**:
今天看了下 DeepSeekV4 的次数涨了不少，估算了下 token 好像吃上折上折了？
预估了一下 token 量，算上缓存的话
一个 go 套餐里，DeepSeek V4 Flash 已经约等于	10,923,420,500     token 了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208931#reply3

---

#### 537. [V2EX] 为什么我感觉 Codex 审美好差

**问题描述 / Problem Description**:
我之前用 Flutter ，通过 Gemini 写了一个学英语的 App ，最近想迭代功能，感觉 Flutter 很多细节上不太满意，决定换成 macOS 原生开发了。找 Codex 开发，GPT-5.5 + Extra High ，重构是比较顺利，可以跑起来，但是真的，太丑了。
然后 macOS 左上角那三个按钮，就是长得像红绿灯的东西，和顶栏其它的元素（ 2 个收起/展开按钮，标题），让 Codex 反复改，几个小时过去了还是各种问题。最后给我整崩溃了，换成 Gemini ，虽然也是磕磕绊绊，但肉眼可见地方向正确，最后花了一个多小时调好了。
后续我又花了几个小时通过 Gemini 把丑到爆

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208925#reply14

---

#### 538. [V2EX] 你们有没有遇到过，通过梯子看 youtube 高清视频的时候，竟然会导致全家的 wifi 异常断开

**问题描述 / Problem Description**:
只要一开梯子看高清就这样，这是什么原理，电脑开的，手机 wifi 居然也显示异常

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208916#reply9

---

#### 539. [V2EX] 公司开始严查访问境外网络，如何破局

**问题描述 / Problem Description**:
1. 办公电脑为 window11 ，上面装有公司的 EDR2. 办公电脑访问的公司的网络有办法绕过公司的检测么？各位大神出出招

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208909#reply65

---

#### 540. [V2EX] 不同 AI 平台的历史记录聚合，有什么好方法吗

**问题描述 / Problem Description**:
因为没有固定用某个 AI 的习惯，都是一阵子用这家，一阵子用那家，导致历史记录散落在各个平台。有时候想找一个以前问过的东西，但不记得在哪问的了，还得每个平台都找一遍。有的像 deepseek 官网连搜索都没有，更麻烦。不知道有没有什么办法可以把各家官网的历史记录聚合到一处管理。虽然可以用三方客户端+API 来统一入口，但那样就要花钱，感觉没啥必要。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208907#reply4

---

#### 541. [V2EX] 这么多年了微信的开发文档还是当年那个味道

**问题描述 / Problem Description**:
很多年前就已经见识了微信的开发文档,解决方案全靠社区踩坑,今天因为一个业务需要看下文档,还是当年的味道,通知消息还只支持 xml,各种含糊不清楚,到处超链接,有没有社区整理的文档

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208886#reply1

---

#### 542. [V2EX] 最近配了一台新的台式电脑，我想在外面笔记本上可以远程回去直接玩游戏，求方案

**问题描述 / Problem Description**:
求各位大佬指点一下，来个方案，不要远程软件，例如：向日葵，todesk 等

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208878#reply30

---

#### 543. [V2EX] 字节这 Code Plan 诈骗吧

**问题描述 / Problem Description**:
每 5 小时：最多约 1,200 次请求

就问了 2 两个问题额度就耗光了，第 2 个问题刚好卡中间浪费时间。总共估计 100 次请求左右，它这是怎么计算的，10 倍吗！
卖不起就别卖，标的很高骗人进去，挂羊头卖狗肉

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208842#reply13

---

#### 544. [V2EX] 家人们 cursor 与 windsurf 二选一怎么选呢？

**问题描述 / Problem Description**:
背景
Claude 账号被 ban 了，目前手上只剩 Codex 还在服役。这段时间跟 Claude 斗智斗勇属实心累，不想再折腾了，想着干脆转 Cursor 或者 Windsurf 算了。
纠结点
Cursor 和 Windsurf 看起来都还行，想问问老哥们哪个更耐用点
Cursor 我看有 Pro+ 是 3x 的用量
Windsurf 只有 pro 上一层就是 Max 了

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208781#reply31

---

#### 545. What knowledge to take from this major upgrade (Debian 12 to 13) where I've faced some troubles?

**问题描述 / Problem Description**:
Tags: debian, deb, dist-upgrade | Score: 7 | Views: 825 | Answers: 2 | Created: 2026-03-14

**解决方案 / Solution**:
Without the logs, it’s impossible to know what your first dist-upgrade did. However, with a third-party repository installed it’s not surprising that it didn’t upgrade the system properly. What you should have done is read the Debian 13 release notes . They explain in detail how to prepare for the upgrade (including removing non-Debian packages — while this is often not necessary, it makes for a smoother upgrade), and how to perform the upgrade safely. I also recommend not specifying -y when running upgrades interactively; it’s best to check what apt is going to do (or not do) before letting it proceed. Even --autoremove is best left until later since it can result in unwanted package removals. Regarding dist-upgrade v. full-upgrade , they’re the same. See apt full-upgrade vs apt upgrade redundancy for details of the various upgrade options. In step 3, it’s normal not to get a complete upgrade: apt-get upgrade only upgrades packages that can be upgraded without removing anything, which is usually only a small part of a major upgrade (between releases). That’s why you needed the apt-get dist-upgrade in step 4 to finish the upgrade. See also What is the purpose of running `apt-get upgrade` then `full-upgrade` when upgrading to a new Debian release?

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804994/what-knowledge-to-take-from-this-major-upgrade-debian-12-to-13-where-ive-face

---

#### 546. df with a given filename return a filesystem name which is not in the list of all filesystems given by df without any parameter

**问题描述 / Problem Description**:
Tags: centos, disk-usage, luks | Score: 7 | Views: 638 | Answers: 2 | Created: 2025-10-16

**解决方案 / Solution**:
The output you’re seeing with no parameters is the result of special handling of device names ending in UUIDs : if (process_all && has_uuid_suffix (dev_name) && (resolved_dev = canonicalize_filename_mode (dev_name, CAN_EXISTING))) This is explained in the comment just above: On some systems, dev_name is a long-named symlink like /dev/disk/by-uuid/828fc648-9f30-43d8-a0b1-f7196a2edb66 pointing to a much shorter and more useful name like /dev/sda1 . It may also look like /dev/mapper/luks-828fc648-9f30-43d8-a0b1-f7196a2edb66 and point to /dev/dm-0 . When process_all is true and dev_name is a symlink whose name ends with a UUID use the resolved name instead. Device names are processed in this way only when all devices are shown, that it to say when df is invoked without arguments (other than options). Furthermore, this processing can’t be disabled, so you can’t ask df with no arguments to show the longer device name instead of the short one. If you want similar behaviour in both situations, you’d have to post-process the output; something like df . | awk '{ "readlink " $1 " > /dev/null && readlink -f " $1 | getline replacement; if (replacement != "") $1 = sprintf("%-" length($1) "s", replacement) } 1' Another possibility is to use findmnt instead of df : findmnt --df produces results similar to df , but without post-processing UUID-suffixed device names, and findmnt --df -T / works similarly to df / (and works for any kind of file, same as df ).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800511/df-with-a-given-filename-return-a-filesystem-name-which-is-not-in-the-list-of-al

---

#### 547. If a shell runs "exec" to start my graphical session, why do I still see that shell in the process list?

**问题描述 / Problem Description**:
Tags: linux, shell, exec, login-manager | Score: 6 | Views: 582 | Answers: 2 | Created: 2026-04-23

**解决方案 / Solution**:
exec start-hyprland | systemd-cat -p info -t hyprland is not the same as exec sleep 300 . In exec cmd , cmd is run in the same process as the shell, not a child ( exec should really have been called nofork ). In cmd1 | cmd2 , the shell forks itself twice¹, runs cmd1 in the first child, cmd2 in the second after having instantiated a pipe or socket pair connecting the stdout of the first to the stdin of the second. In any case, since cmd1 and cmd2 are running concurrently, they have to run in separate processes. Here, cmd1 is exec start-hyprland , so that runs start-hyprland without forking, but that's done by the first child mentioned above. exec is superfluous here because that child would not have forked an extra process just to execute that one command anyway. The sh you see in ps output is the main shell that is waiting for the termination of both processes constituting that pipeline². For that sh process started by your session manager to run start-hyprland without a fork, you'd need something like: exec cmd1 > >(cmd2) Where cmd2 is started asynchronously, not waited for, with its stdin connected to a pipe. >(cmd2) expands to a path to the other end of that pipe, which the shells opens in write-only mode ( > ) on the stdout of cmd1 and exec skips the fork. Note that the process running cmd2 in that case will will end up being the child of the one running cmd1 , so when it dies, cmd1 will receive a SIGCHLD signal which might very well confuse it. Example: $ ksh -c 'exec sleep 100 | cat' & $ ps -Hopid,ppid,args PID PPID COMMAND 6074 6072 /bin/zsh 9744 6074 ksh -c exec sleep 100 | cat 9745 9744 sleep 100 9746 9744 cat 9749 6074 ps -Hopid,ppid,args The process running sleep and the one running cat are sister processes both spawned by the process that executed ksh and that process is still there waiting for them (well here it being ksh93, it only waits for the one running cat ² unless you set the pipefail option). $ ksh -c 'exec sleep 100 > >(cat)' & $ ps -Hopid,ppid,args PID PPID COMMAND 6074 6072 /bin/zsh 9229 6074 sleep 100 9230 9229 cat 9238 6074 ps -Hopid,ppid,args This time, ksh is gone and was replace by sleep and cat still a child of that process that used to run ksh but now runs sleep . >(...) ( process substitution ) is not standard sh syntax though. It comes from ksh in the mid-80s though at the time it could not be used as target of redirections. zsh and bash have copied it since (and rc and derivatives have the same feature with a different syntax). The above would work today with ksh93, zsh and bash, but yash has a related feature that is even more relevant here: process redirection : In that shell, >(cmd) is not substituted with the path of a pipe but is short for 1>(cmd) just like >file is short for 1>file and redirects file descriptor 1 (stdout) to a pipe to a process started asynchronously to run cmd , so in yash, you'd just do exec cmd1 >(cmd2) . With standard sh syntax, you'd need to resort to named pipes by hand, something like: mkfifo -m600 some-pipe && { cmd2 <&3 3<&- & } 3< some-pipe && { rm -f some-pipe && exec cmd1; } > some-pipe Though of course you'd want to make sure some-pipe is created unique in some temporary area which with standard sh and utilities is hard to do portably and reliably. As noted by @grawity in comment, in the specific case of systemd-cat , you can also do: systemd-cat -p info start-hyprland Where systemd-cat cmd executes cmd in its own process with both its stdout and stderr ( current versions of the man page say it connects stdin instead of stderr but that's not what I observe and it wouldn't make sense³) directly connected to the journal via a Unix-domain socket instead of forwarding it from a pipe (or socketpair for shells that use them for their | operator like ksh93 on systems where pipes are not seekable, not process substitution which can't use socketpairs) to the command. To avoid touching stderr, you could do: systemcat sh -c 'exec cmd 2>&3 3>&-' 3>&2 ¹ Though some shells skip the fork for cmd2 except of course, down the line, to execute cmd2 if that's an external command and not a builtin or function. ² Some shells only wait for the right-most one, and some shells optimise out an extra fork when running the last command of an inline script so could run cmd2 in the shell process, which is not your case here since ps still shows that process running sh . ³ Fix now committed, so should be included in the next release.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805578/if-a-shell-runs-exec-to-start-my-graphical-session-why-do-i-still-see-that-sh

---

#### 548. How can I tell in software if a very quiet fan isn't spinning?

**问题描述 / Problem Description**:
Tags: debian, hardware, temperature, fan | Score: 6 | Views: 1673 | Answers: 2 | Created: 2026-03-22

**解决方案 / Solution**:
The control of the fan speed on the HP EliteBook 845 G7 via the BIOS is only possible to a limited extent. HP business notebooks generally manage fan curves automatically to ensure optimal cooling and hardware integrity. Enter the BIOS, restart your laptop and immediately press the F10 key repeatedly to open the BIOS setup utility. Find fan settings and navigate to the Advanced or Power tabs. Available options: Fan Always On You can enable or disable this option in the BIOS. If it is disabled, the fan may stop completely under low load . Laptop fan to turn on and off at will Solved Start a conversation HP ProBook PCs, EliteBook PCs, and Mobile Workstation PCs - Customized fan control With under low load it is meant that the fan automatically turns on and off, as also described in the manual on page 25. Like with many gaming graphics cards, where the fans only start spinning once a certain load is reached. The computer fan starts up automatically to cool internal components and prevent overheating. It is normal for the internal fan to cycle on and off during routine operation. To reduce the possibility of heat-related injuries or of overheating the computer, do not place the computer directly on your lap or obstruct the computer air vents. Use the computer only on a hard, at surface. Do not allow another hard surface, such as an adjoining optional printer, or a soft surface, such as pillows or rugs or clothing, to block airfow. Also, do not allow the AC adapter to come into contact with the skin or a soft surface, such as pillows or rugs or clothing, during operation. The computer and the AC adapter comply with the user-accessible surface temperature limits dened by applicable safety standards HP EliteBook 845 G7 Maintenance and Service Guide TjMax = 105 °C is the official maximum temperature of the CPU. This is exactly the value that everything refers to (throttling, etc.). AMD Ryzen 5 PRO 4650U Processor International safety standards for IT and AV equipment, relevant for laptops, tablets, monitors, etc. Accessible surfaces shall not reach temperatures that could cause burns to the user under normal operating conditions. CPU Health and Testing Component Tests: Inside the diagnostics menu, navigate to Component Tests to find specific tests for the processor, including a "Processor Check" to verify functionality. System Information: The BIOS "Main" tab displays processor type and speed. Temperature Management: Users have reported high operating temperatures (100°C - 105°C) on the EliteBook 845 G7 during heavy loads , which can be managed by adjusting the Windows Power Plan's "Processor performance boost mode" to disabled if overheating is detected. HP Elitebook 845 g7 overheating? Take a look at your CPU temperature, thermal throttling starts at around 95 °C , and beyond that it can become critical. Dust always builds up in the fans, and if the device previously belonged to a smoker and wasn’t properly cleaned, a lot of grime can accumulate as well. You can try cleaning the laptop again from the outside using a can of compressed air / Anti-dust spray to blow out as much dirt as possible. Otherwise, if it’s possible and you feel confident, open the device and check what’s going on, then clean it from the inside with a brush and a cloth. If the fan is broken, get a replacement on eBay or a similar site, You can find used fans for between €15 and €25. Here’s also a video showing how to open it, otherwise take it to someone who knows how to do it. HP Elitebook 845 G7 parts installation and disassembly

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805113/how-can-i-tell-in-software-if-a-very-quiet-fan-isnt-spinning

---

#### 549. Ubuntu system returns "killed" on nearly all commands

**问题描述 / Problem Description**:
Tags: ubuntu, nginx, node.js, out-of-memory, deployment | Score: 3 | Views: 173 | Answers: 2 | Created: 2026-02-16

**解决方案 / Solution**:
It definitely looks like a crypto miner malware, which has arranged a higher priority for itself and is trying to kill any commands that would kill it before they can take effect. │ └─809 /bin/softirq --randomx-1gb-pages -o 45.125.66.100:444 -u react -p 3cthDeQ5 --tls -o 45.94.31.89:443 -u react -p 3cthDeQ5 --tls -B This is clearly a fake name: a real softirq process would have a name like [ksoftirqd/0] and it would have no reason to have IP addresses and ports as parameters. Maybe you're using a weak password (use SSH key authentication for internet-accessible servers) or the software you're running has a vulnerability that allows the attacker to plant malware to the system. In the comments, eyoung100 already identified PeerBlight (CVE-2025-55182) as the possible vulnerability, if the application is using React Server Function endpoints or React Server Components. If you are using the vulnerable versions (anything older than versions 19.0.1, 19.1.2 or 19.2.1), you'll need to update those componets before redeploying your application. Anyway, the link in Robo's answer seems to indicate this malware is part of the RondoDox botnet . Because the malware attempts to protect itself, you may have to stop the VPS, create a new "clean" one, and then connect the disk of the infected VPS as a secondary disk to the clean VPS to recover your data and to possibly inspect the malware. Unless you know how to check, assume any executables on the disk of the infected VPS are contaminated by malware - so don't reuse them. Before redeploying, check if the application (or any components you used in it, if the application is custom-built by yourself) for security notices and update as necessary.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804521/ubuntu-system-returns-killed-on-nearly-all-commands

---

#### 550. Centos maximum CPU frequency discrepancy

**问题描述 / Problem Description**:
Tags: centos, cpu-frequency | Score: 3 | Views: 181 | Answers: 1 | Created: 2026-01-21

**解决方案 / Solution**:
You can't. if you read the product page for your processor , you'll notice that 6200 MHz is just the upper end of the turbo range, i.e, not something you can configure as regular clock frequency. (Things get a lot more complicated under the hood; your processor can and does handle frequency scaling itself, and the role of the intel_pstate driver is to tell the processor how to decide which frequencies to use when. For more details, see the kernel documentation . But none of that changes that a Turbo frequency is not something you can just set as frequency. It can only be done for short bursts of time, before parts of your CPU package get too hot. And thus, it will only be activated when the CPU load is briefly high, to get that workload done ASAP, before temperature builds up.) (and yeah, you told me to not ask about CentOS 7, but I can still remark: performance tuning a system frequency-wise, although you're using a software platform that's as old as CentOS 7, that's um, let's say that's a creative way to invest your time. The software compiled for CentOS 7 can only use acceleration and architectural features present in CPUs from ca. 2004. Finding the time to get the software you're depending on CentOS 7 for in a version compiled for RHEL 10, and then running it on AlmaLinux 10 or RockyLinux 10 would very likely increase the performance a lot more than a few percents of processor clock would.)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803941/centos-maximum-cpu-frequency-discrepancy

---

#### 551. How to extend a logical volume mounted on /home directory?

**问题描述 / Problem Description**:
Tags: centos, lvm, disk, fdisk | Score: 3 | Views: 293 | Answers: 1 | Created: 2025-03-19

**解决方案 / Solution**:
Since I am new to disk management, does it make sense? yes, (my first reaction was, wait there's a fourth mini partition, if this is MSDOS partition tabling, then it might not be possible to create more partitions, but this is GPT!). I'd add a -r to your lvextend command line: if your /home runs on a file system that can be enlarged while mounted, this will automatically do that; otherwise you're missing the step where you make the filesystem actually fill the (now larger) volume.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/792697/how-to-extend-a-logical-volume-mounted-on-home-directory

---

#### 552. RAID array reverts to the old disk after reboot

**问题描述 / Problem Description**:
Tags: centos, storage, raid1 | Score: 3 | Views: 269 | Answers: 2 | Created: 2024-11-27

**解决方案 / Solution**:
Once a drive is removed from an array, its metadata is no longer updated. So the last metadata state is that of before it was removed, so it "looks good" unless another drive claims a newer update time and the like. So in the case where you remove RAID-1 drives and expect the array to continue on two other drives, can lead to some confusion. Inherently this is a weakness of mdadm metadata format. Furthermore, your mdadm.conf is too verbose . Remove metadata= , name= , and spares= in particular. Such entries might cause your new array to be ignored (in this example, if no spares are present). If you wish to keep both arrays around, at minimum you should change the UUID for one ( mdadm --assemble --update=uuid ) and also change UUIDs of whatever is on that array. You should also consider --update=super-minor and/or --update=name . If you do not wish to keep the array for the old drives around, --stop the wrong array then --zero-superblock its drives. You can also re-create, however, do not expect data on these drives to be available afterwards. This is only the case under the right conditions, see Should I use mdadm --create to recover my RAID?

**参考链接 / References**:
- https://unix.stackexchange.com/questions/787286/raid-array-reverts-to-the-old-disk-after-reboot

---

#### 553. What is the correct procedure to load a kernel module at boot in RHEL/CentOS 2.1 (kernel 2.4.x)?

**问题描述 / Problem Description**:
Tags: centos, rhel, kernel-modules, sata | Score: 3 | Views: 435 | Answers: 1 | Created: 2024-10-02

**解决方案 / Solution**:
I think your /etc/modules.conf file may already have a line like alias scsi_hostadapter ata_piix That covers the controller for your primary disk. To tell the system to load a second storage controller driver, add this line: alias scsi_hostadapter1 sata_sil to the same file. This tells the system to load the sata_sil module automatically very early in the boot process. (If there is no existing alias scsi_hostadapter ... line, omit the 1 from the new line.) Then rebuild your initrd: mkinitrd -f /boot/initrd-$(uname -r).img $(uname -r) After these steps, the sata_sil module should load automatically on boot. Note that with the old 2.4 series kernel, the (P)ATA disks will appear as /dev/hd[a-d] but sata_sil is treated like a SCSI device driver, so the SATA disks should appear as `/dev/sd[a-z]*' RHEL 2.1 might also have a lsscsi command (possibly as a separate package) which might be useful with any "SCSI-like" devices.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/784372/what-is-the-correct-procedure-to-load-a-kernel-module-at-boot-in-rhel-centos-2-1

---

#### 554. Unnecessary error traces after systemd path unit exits

**问题描述 / Problem Description**:
Tags: debian, systemd, services | Score: 2 | Views: 25 | Answers: 1 | Created: 2026-04-29

**解决方案 / Solution**:
Do not misuse PathExists= . Add a udev rule that sets SYSTEMD_WANTS=your.service variable for your device(s). You can find examples in the standard rules, like SUBSYSTEM=="leds", KERNEL=="*kbd_backlight*", TAG+="systemd", IMPORT{builtin}="path_id", ENV{SYSTEMD_WANTS}+="systemd-backlight@leds:$name.service" The unit(s) from the SYSTEMD_WANTS will be activated when the device(s) appear. The devices must be tagged with TAG+="systemd" , otherwise systemd will ignore them.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805697/unnecessary-error-traces-after-systemd-path-unit-exits

---

#### 555. Cinnamon - I can't get my laptop to power off when lid is closed

**问题描述 / Problem Description**:
Tags: debian, systemd, cinnamon | Score: 2 | Views: 48 | Answers: 1 | Created: 2026-04-17

**解决方案 / Solution**:
The handling of lid switch is blocked by the csd-power which has its own logic. Looking at cinnamon-settings-daemon sources you should be able to disable it with gsettings set org.cinnamon.settings-daemon.plugins.power inhibit-lid-switch false You should also be able to tell csd-power to power off instead of suspending with gsettings set org.cinnamon.settings-daemon.plugins.power lid-close-battery-action shutdown gsettings set org.cinnamon.settings-daemon.plugins.power lid-close-ac-action shutdown

**参考链接 / References**:
- https://unix.stackexchange.com/questions/805509/cinnamon-i-cant-get-my-laptop-to-power-off-when-lid-is-closed

---

#### 556. Debian software RAID1 Over my head: I'm looking for pointers concerning UEFI booting alternate EFI locations if the either one fails

**问题描述 / Problem Description**:
Tags: debian, uefi, firmware, software-raid | Score: 2 | Views: 190 | Answers: 1 | Created: 2026-03-09

**解决方案 / Solution**:
The UEFI hard drive media device paths are using partition GUID. It can be shown e.g. with lsblk -o +partuuid . UEFI boot entries are normally managed by the efibootmgr --create . You pass the Linux device node and efibootmgr will compute the necessary GUID, partition offset and partition size for you. For Linux MD RAID1 you will need to create two boot entries, one for each physical partition. I do not think Debian does it automatically in this case. Debian actually supports having two independent copies of ESP (without RAID) and will install bootloader on each of them when updating grub. For this you set grub-efi/install_devices option of the grub-efi-amd64 package: bor@ThinkPad-E16-Gen3:~/tmp$ sudo debconf-show grub-efi-amd64 | grep grub-efi/install_devices: * grub-efi/install_devices: /dev/disk/by-id/nvme-eui.ace42e005580d4a9-part1 bor@ThinkPad-E16-Gen3:~/tmp$

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804885/debian-software-raid1-over-my-head-im-looking-for-pointers-concerning-uefi-boo

---

#### 557. How to use a "grep" result as an input of another grep, resulting in multiple lines?

**问题描述 / Problem Description**:
Tags: ubuntu, command-line, grep, pipe, windows-subsystem-for-linux | Score: 2 | Views: 925 | Answers: 5 | Created: 2025-10-29

**解决方案 / Solution**:
If you're already using awk , you don't need to use grep . awk can do Extended Regular Expression (ERE) matches like grep -E . And just as importantly, awk can use boolean operators ( ! , && , || , and even parentheses) with conditions/patterns, which grep can't do (although you can make a regex with alternations using | which is an OR operation). For example: awk -F- '/Rebuild All started/ && /: (fatal|error)/ { print $1 }' build_output.txt | sort -n | uniq You could even write the awk script so that it stored the matches in an associative array, then sorted and printed the the output in an END block, avoiding the need for piping to sort -n | uniq . BTW, egrep is deprecated. use grep -E instead for ERE. With GNU grep you also have the option of using -P for PCRE If you're not using awk , then piping the output of grep into another grep is effectively an AND operation. If needed, you can use grep's -v option for negation. e.g. using cut instead of awk . grep 'Rebuild All started' build_output.txt | grep -E ': (fatal|error)/' | cut -d- -f1 | sort -n | uniq This is objectively worse than just using awk . Every program in a pipeline has startup overhead and requires more resources (CPU time, RAM, and I/O bandwidth)...this is not as big a problem as it was a decade or two ago, we have much faster computers and storage devices now, but that's not really a good excuse to be wasteful in how we use them.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800857/how-to-use-a-grep-result-as-an-input-of-another-grep-resulting-in-multiple-li

---

#### 558. Are the historical Linux device namespace limits (e.g. the 15-partition limit per /dev/sdX) still applicable when using GPT on modern Linux kernels?

**问题描述 / Problem Description**:
Tags: linux, partition, namespace, gpt | Score: 14 | Views: 1304 | Answers: 1 | Created: 2026-01-10

**解决方案 / Solution**:
include/linux/blkdev.h:53:#define DISK_MAX_PARTS 256 The linked answer is technically correct and describes the new system but is easy to misinterpret. The maximum number of partition sub-devices per block device is 255 regardless of disk type (the main device itself effectively takes up slot 0, which makes a total of 256). A block device driver can provide a major number and interval (maximum minor numbers), in which case the kernel uses the traditional scheme where the initial N partitions will have device numbers within the specified range. But this scheme does not cause any limits, as subsequent partitions starting with Linux 2.6.28 will have minor numbers dynamically allocated from the "extended" 259:xxx major, still up to 256 per disk. For example, the SCSI disk sd driver provides major=8 and minors=16, so the first disk and its partitions get 8:0 to 8:15 and then "overflow" into 259:xxx (this being BLOCK_EXT_MAJOR). The loop driver uses major=7 and minors=0 (as originally it had no partition support) so the main device is 7:0 but all its partitions immediately use 259:xxx. If the driver doesn't provide a major number, then all partitions will be allocated dynamically. For example, nvme uses dynamic allocation and all of its device nodes are 259:xxx (even the "whole disk" device), sharing the major number with my loop partitions in this example. The minor number is an 18-bit value on Linux so the scheme allows up to 262144 "overflow" device nodes, which is 1024 NVMe devices partitioned to the brim (or 1092 SCSI devices). $ sudo partx /dev/loop0 -- directly dumps partition table NR START END SECTORS SIZE NAME UUID 1 2048 4095 2048 1M 8c9066af-375f-41dd-96c3-6c423f756a8e 2 4096 6143 2048 1M 630dac95-e5cd-41f1-a5c7-d2ee3589a8cc [...] 509 1042432 1044479 2048 1M 38e1647b-4bae-4cfd-bf47-7b26bede4d15 510 1044480 1046527 2048 1M 63809e27-8607-4103-ba38-76a1bcf0a9ed 511 1046528 1048575 2048 1M 3804fcf2-c75b-443a-80ea-a0d7b804683c $ lsblk NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS loop0 7:0 0 1G 0 loop ├─loop0p1 259:4 0 1M 0 part ├─loop0p2 259:5 0 1M 0 part ├─loop0p3 259:6 0 1M 0 part ├─[...] ├─loop0p253 259:256 0 1M 0 part ├─loop0p254 259:257 0 1M 0 part └─loop0p255 259:258 0 1M 0 part nvme0n1 259:0 0 931.5G 0 disk ├─nvme0n1p1 259:1 0 512M 0 part /boot ├─nvme0n1p2 259:2 0 923G 0 part │ └─sys 253:1 0 923G 0 crypt / └─nvme0n1p3 259:3 0 8G 0 part └─swap 253:0 0 8G 0 crypt [SWAP] Note how the loop device's partitions continue directly after the NVMe partitions, so if I were to add a partition to my NVMe disk, it would get 259:259 instead – the extended minors are not contiguous. (Also note that two devices here are device-mapper devices which use 253:x – the whole major number used by dm is dynamically-allocated. The limit on Linux is 2 14 or 16384 majors if you're curious.) Finally, it is possible to bypass even the 255 partition limit by using device-mapper instead, e.g. using kpartx to read the partition table and set up dm-linear devices that represent individual partitions. This was commonly done in the past for loop devices which originally did not have native support for being partitioned. Since device-mapper has a single major (and doesn't use the overflow system since it is already dynamically-allocated anyway), the theoretical limit would be 262144 total DM-based "partitions" – which can all be configured over the same disk (alongside its 255 native partitions) or spread out across all your 1024 NVMe disks.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803659/are-the-historical-linux-device-namespace-limits-e-g-the-15-partition-limit-pe

---

#### 559. Why can I browse this Windows share using smbclient, but cannot mount it with mount.cifs?

**问题描述 / Problem Description**:
Tags: ubuntu, windows, samba, cifs, smb | Score: 10 | Views: 890 | Answers: 1 | Created: 2025-09-24

**解决方案 / Solution**:
You're connecting to a domain‑based DFS namespace: \\ad.company.com\Shared\Sites\BLAH smbclient follows DFS referrals in user space, so it happily walks from the DFS root ( \\ad.company.com\Shared ) to the real fileserver that actually hosts Sites\BLAH . The kernel CIFS client used by mount.cifs must follow that DFS referral too, but on Linux it relies on keyutils + cifs.upcall for the DFS DNS resolver/SPNEGO upcalls. When those helpers aren’t available or not configured, you get: mount error(126): Required key not available : the kernel asked the keyring for a dns_resolver /SPNEGO key and none was provided (ENOKEY). mount error(2): No such file or directory : you reached the DFS root on the domain controller, but since the referral wasn’t followed the subpath Sites/BLAH doesn’t exist on that server. That matches your symptoms exactly and also explains why other non‑DFS shares mount fine. Whether you hit (126) or (2) depends on how far the mount got before the missing upcall bit it. With DFS upcalls enabled, the kernel will resolve the referral and both errors should disappear.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/799953/why-can-i-browse-this-windows-share-using-smbclient-but-cannot-mount-it-with-mo

---

#### 560. Ubuntu gives the message "You are in emergency mode."

**问题描述 / Problem Description**:
Tags: ubuntu, boot | Score: 8 | Views: 3381 | Answers: 1 | Created: 2025-07-20

**解决方案 / Solution**:
The error messages indicate the system has tried and failed to mount a filesystem with UUID 5cb90862-8d25-4ba9-b71b-fa56a76c7ee8 to /home . The mount attempt failed because the pre-requisite of running a filesystem check on it first had also failed. The exit status 4 from the filesystem checker suggests the filesystem is there, but it contained some errors that could not be fixed in a fully automatic way. In this situation, the first thing to do is to run the filesystem check manually: fsck -C UUID=5cb90862-8d25-4ba9-b71b-fa56a76c7ee8 (The -C option tells the checker to display a progress bar/status, if possible.) You can then see the errors the filesystem checker has found, and the checker might ask you questions about what to do with them. In most cases, the questions will be just "yes"(fix it)/"no"(leave it alone), but in some cases, the questions might be about how to fix a particular error: for example, if the checker finds a "lost chain" of blocks (i.e. an incompletely-deleted file), the options might be to either restore it to a normal file again, or to complete the deletion. If you are using Ubuntu's default filesystem type ( ext4 ), the filesystem checker for it is very well-known and reliable. However, if it tells you it would need to perform repairs on a very important file, e.g. /home/syiem/my_thesis_research_data.csv , then you probably should interrupt the checker, mount the /home filesystem manually in read-only mode, and try and make an extra copy of the important file to some other filesystem, just to be safe: <press Control+C to interrupt the filesystem checker> mount -o ro UUID=5cb90862-8d25-4ba9-b71b-fa56a76c7ee8 /home cp /home/syiem/my_thesis_research_data.csv /root/my_thesis_research_data_backup.csv` Once your important file is safely copied to a separate filesystem, you can then unmount the filesystem and re-run the checker: umount /home fsck -C UUID=5cb90862-8d25-4ba9-b71b-fa56a76c7ee8 Once the filesystem check is successfully completed, you can reboot, and the system should again come up normally.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798107/ubuntu-gives-the-message-you-are-in-emergency-mode

---

#### 561. How to convert .HEIC files to jpg or otherwise view on Debian Linux

**问题描述 / Problem Description**:
Tags: debian, ffmpeg, imagemagick, iphone | Score: 7 | Views: 1288 | Answers: 2 | Created: 2026-02-01

**解决方案 / Solution**:
There are issues with photos taken on devices running iOS 18: ImageMagick on Fedora will not read HEIC images created with iOS 18 https://askubuntu.com/questions/1531719/how-to-view-iphone-heic-images-after-ios-18-update-in-ubuntu-24-04 You should be able to install libheif-plugin-libde265 from bookworm-backports to get it fixed. As for the viewer itself, I like nomacs for browsing galleries. According to this issue , nomacs can understand image/heic via kimageformat-plugins . I can confirm on Ubuntu 24.04, you can install the plug-ins: sudo apt install kimageformat-plugins qt5-avif-image-plugin Your mileage may vary for Debian, but it should be similar.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804162/how-to-convert-heic-files-to-jpg-or-otherwise-view-on-debian-linux

---

#### 562. Fool a program it has a pty of specific size

**问题描述 / Problem Description**:
Tags: linux, terminal, tty, serial-console, pty | Score: 6 | Views: 727 | Answers: 1 | Created: 2025-11-27

**解决方案 / Solution**:
That's script that actively updates the tty size upon receiving the SIGWINCH signal (as sent by the terminal line discipline when the host terminal emulator tells it its new size¹) which in turn causes a SIGWINCH to be delivered to the foreground process group of the slave pty, and nethack in that process group queries that new size upon reception of that signal like full-screen TUI applications typically do. On the system I try it on, script (from util-linux ) installs that handler² on SIGWINCH even when SIGWINCH was ignored on startup, so doing something like (trap '' WINCH && script...) won't work. You could use something else that doesn't have that feature though such as socat : socat stdio,raw,echo=0 \ 'system:"stty rows 24 cols 80; exec nethack",pty,setsid,ctty,stderr' That's doing the same as what script does except for that SIGWINCH handling and the saving of the data into a typescript file (though socat has some options to save the exchanged traffic): puts the host terminal in raw mode with echo disabled forks a process, starts new session ( setsid ), with new pty , gets control of the slave side there ( ctty ) and runs a shell in there (which will be the session leader) to interpret that shell code with stdin, stdout and stderr connected to that slave side. then reads from the host terminal (for what you type) and forward to slave via master side while at the same time, read from master (from what the shell and the applications it runs output) and send that to the host terminal for display. Another option is to run script or your ttyrec in a new session. Then it won't get the SIGWINCH when the host tty is resized since it's no longer controlled by that terminal (so a fortiori not in its foreground process group). setsid -w ttyrec -e 'stty cols 80 rows 24; exec nethack' In the ps output, you'll see that ttyrec no longer has a controlling terminal: $ ps -jp 467606 PID PGID SID TTY TIME CMD 467606 467606 467606 ? 00:00:00 ttyrec Though its stdin/stdout/stderr still go to the host terminal: $ readlink /proc/467606/fd/[0-2] /dev/pts/15 /dev/pts/15 /dev/pts/15 ¹ Via a TIOCSWINSZ ioctl() on the master side of the pseudo-terminal. That terminal size changing kernel API with those ioctls and the SIGWINCH signal was apparently first added in BSDs in late 1984 ; I wonder what sort of terminal from the time could be resized. It might have been for the VT220 which came out in late 1983 and could switch between 80 and 132 columns . ² Technically, in current versions at least, not a traditional signal() handler, as it uses a signalfd() instead, which is processed as part of the pty handling event loop , but the effect is the same.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801678/fool-a-program-it-has-a-pty-of-specific-size

---

#### 563. NeoMutt and incomplete email addresses

**问题描述 / Problem Description**:
Tags: debian, postfix, neomutt | Score: 5 | Views: 302 | Answers: 1 | Created: 2026-02-01

**解决方案 / Solution**:
From the manpage for neomuttrc use_domain Type: boolean Default: yes When set , NeoMutt will qualify all local addresses (ones without the "@host" portion) with the value of $hostname. If unset , no addresses will be qualified. So I would suggest trying unset use_domain in your configuration file. Related is the hostname variable where you can specify what hostname gets appended.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804174/neomutt-and-incomplete-email-addresses

---

#### 564. How to check for IPv6 address collisions in Linux

**问题描述 / Problem Description**:
Tags: linux, ipv6 | Score: 5 | Views: 816 | Answers: 2 | Created: 2025-11-29

**解决方案 / Solution**:
The kernel automatically performs Duplicate Address Detection any time an IPv6 address is added to an interface. There is nothing special that the program needs to do in order to activate DAD. If I have some software that wants to add an IP to the host, how could that software discover that the IP is taken. Eg using the ip CLI? The same way it adds the IP address: If the program uses Netlink ( rtnl ) as most Linux networking tools do, then after adding the rtnl_addr object it can get (RTM_GETADDR) the same object and check its IFA_FLAGS: having IFA_F_TENTATIVE means it is still undergoing Duplicate Address Detection (and in fact the kernel won't allow you to use it, unless Optimistic DAD is enabled), IFA_F_DADFAILED means DAD finished and found a collision (the tentative flag may remain set as well), absence of both flags means DAD finished and no collisions were found. The program doesn't need to wait for a specific time. The kernel's DAD code already has the necessary timers (which may vary depending on whether the kernel has optimistic_dad or enhanced_dad enabled). The program only needs to keep checking (e.g. every second) until either the 'tentative' flag disappears or 'dadfailed' appears, whichever happens first. Netlink also provides change notifications (like in ip monitor addr ) so the program will automatically keep receiving the address object every time its flags change, without needing any poll interval. If the program uses the ip CLI, then to begin with, it should stop using the ip CLI and start using interfaces meant for machine use, namely Netlink. But if that's not possible then the program should use ip -json to query the addresses, parsing the output as JSON and using the same logic as for Netlink (i.e. wait until .tentative has disappeared and/or .dadfailed has appeared). ip -j -6 addr ls mlx0 | jq '.[].addr_info[] | {local, tentative, dadfailed}' The iproute2 ip CLI itself uses Netlink, so it is not problematic in itself – it has access to all of the same information, and you can run it manually to check the same flags. But it is an interface for human consumption first and foremost. If the program uses the ip CLI on a platform where there's no -json option (either because it's an ancient iproute2 version or because it's the Busybox imitation), then sorry but that's already in the "works on my computer" territory. And if the program uses the old Linux 2.4 era IPv6-specific ioctl and /proc/net interfaces, then AFAIK it has no way to obtain this information, and it should be ported to Netlink – although even ip -json would already be an upgrade. (This specifically includes the net-tools ifconfig , as nobody has ported it to the modern Linux 2.6 ways yet. Avoid net-tools.)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801732/how-to-check-for-ipv6-address-collisions-in-linux

---

#### 565. suppress stderr when inputting a file to a variable

**问题描述 / Problem Description**:
Tags: bash, ubuntu | Score: 5 | Views: 365 | Answers: 2 | Created: 2025-10-24

**解决方案 / Solution**:
What you can do: { var="$(< no-exists)"; } 2>/dev/null The curly braces { ...; } run the command in the current shell as a group. 2>/dev/null after the group sends the group's STDERR to /dev/null So when < no-exists fails, its error is discarded and var becomes empty (no error shown). Another version closing the STDERR F ile D escriptor: exec 9>&2 # save stderr on FD 9 exec 2>&- # close stderr var="$(< no-exists)" exec 2>&9 # restore stderr from FD 9 exec 9>&- # close FD9 (cleanup) Simplified version: exec 9>&2 2>&- var="$(< no-exists)" exec 2>&9 9>&-

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800732/suppress-stderr-when-inputting-a-file-to-a-variable

---

#### 566. Making `apt-get` read answers from stdin on graphical Ubuntu

**问题描述 / Problem Description**:
Tags: ubuntu, scripting, apt, stdin | Score: 5 | Views: 384 | Answers: 1 | Created: 2025-09-19

**解决方案 / Solution**:
This doesn’t answer your question as summarised in the title, but for well-designed packages that use debconf for configuration, the correct way to pick answers non-interactively is to set them ahead of time (“pre-seeding”). For postfix , that’s: debconf-set-selections <<<"postfix postfix/main_mailer_type select No configuration" The parameters are, in order, the package name, the configuration key, the configuration type, and the value. To find the appropriate values to give, you need to install the package or at least extract its contents, and look at /var/lib/dpkg/info/postfix.templates (replacing postfix as appropriate). This will show all the available configuration settings with their types and default values. In this instance: Template: postfix/main_mailer_type Type: select Choices: No configuration, Internet Site, Internet with smarthost, Satellite system, Local only […] Default: Internet Site […] The default value is “Internet Site”, so a non-interactive setup will use that value. Since that isn’t what you want, you need to change the setting ahead of time as described above. For best results, you should also set DEBIAN_FRONTEND=noninteractive , since you want a non-interactive installation anyway. Some packages add a layer on top of debconf ; one example is dbconfig-common , which is the recommended way for packages requiring a database to configure their database connections, but which doesn’t work with debconf pre-seeding. The defaults for dbconfig-common are to use a local database (on localhost ), so if that’s appropriate, DEBIAN_FRONTEND=noninteractive will do the right thing. Otherwise, you need to provide a configuration file in /etc/dbconfig-common , named after the package you want to configure; for example, /etc/dbconfig-common/bacula-director-pgsql.conf . The simplest way to construct this is to install the package once and answer the debconf prompts; dbconfig-common will then write a configuration file that can be re-used elsewhere (possibly removing the password).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/799796/making-apt-get-read-answers-from-stdin-on-graphical-ubuntu

---

#### 567. Unable to disconnect pool due to ghost tailscale process

**问题描述 / Problem Description**:
Tags: linux, mount, docker, nas, freenas | Score: 4 | Views: 328 | Answers: 1 | Created: 2025-12-27

**解决方案 / Solution**:
TrueNAS these days is a Debian GNU/Linux based system with a custom Linux kernel and like when it was based on FreeBSD leveraging the ZFS file system for storage. Exporting a ZFS pool implies unmounting all its datasets. And to be able to unmount a dataset, like for any filesystem, it must not be in use (no file opened or mmapped by any process or used as loop device backend, etc). The TrueNAS "apps" these days are implemented as docker containers, and like for kubernetes before, those are just a management interface around the Linux container/namespace features. Those complicate things as you have processes running in different and unshared mount namespaces, which means lsof and zpool export / umount won't work properly. So you need to make sure all processes in separate namespaces that may use datasets in a zpool are terminated before you can export that zpool . For TrueNAS apps, that means stopping those apps via their WUI or API. If you have started unmounting datasets and killing random processes under TrueNAS/ docker feet, it's likely the system will be in a bad state hard to recover from and your best bet may be to reboot the appliance. You can try to identify the processes still running in those containers by looking at their mount namespaces (with ps -HAo mntns,pid,args ) and/or /proc/<pid>/mounts for each <pid> . Those processes won't have tailscale in their name but might have in /proc/<pid>/mounts .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803340/unable-to-disconnect-pool-due-to-ghost-tailscale-process

---

#### 568. Asynchronous execution of sudo in parallel breaks terminal

**问题描述 / Problem Description**:
Tags: linux, sudo | Score: 4 | Views: 217 | Answers: 1 | Created: 2025-12-01

**解决方案 / Solution**:
Because the authors of sudo take special precautions to ensure that it sends prompts to, and receives input from, an actual interactive terminal. This is sudo functioning as designed. For more information, read man sudo sudoers . For even more information, you can download, and read, the source.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801771/asynchronous-execution-of-sudo-in-parallel-breaks-terminal

---

#### 569. How to achieve persistent quicklaunch behaviour with Gnome on Ubuntu?

**问题描述 / Problem Description**:
Tags: ubuntu, gnome, desktop-environment, desktop, gnome-panel | Score: 4 | Views: 270 | Answers: 1 | Created: 2025-10-03

**解决方案 / Solution**:
Some things can be changed manually or with add-ons (widgets), while others can’t be changed at all, or only with great difficulty or to a minimal extent. You could also try doing it with custom programming and configuration, but the effort wouldn’t really be worth it. Gnome Desktop Ubuntu with the default GNOME interface works fundamentally differently out of the box. Normally, there is no such permanent, visible quick launch bar in the taskbar. Dash to Panel mixes some of the concepts of Windows and GNOME, combining the Dash and the application bar into a Windows-like taskbar. But even though you now have a Windows-like panel, the behavior of favorites and other elements still follows GNOME’s logic, icons disappear or switch within the running applications area. I’d suggest trying Isolate Favorites , in the Dash to Panel settings under Advanced Settings > Isolate Favorites and see if changing the options there makes any difference. Otherwise, you can try these three other extensions, but you’ll still face some limitations due to the GNOME design. Dash to Panel will probably remain the option that gets you closest to a proper solution. Arc Menu: Replaces the standard menu with a Windows-like start menu Features include: various menu layouts, built in GNOME search, quick access to system shortcuts, and much more! Arc Menu Just Perfection It also allows you to modify dozens of small aspects of GNOME Just Perfection Frippery Applications Menu A simpler alternative to Arc Menu Replace Activities button with an Applications menu Frippery Applications Menu Personally, I liked the implementation and performance of GNOME in Tails the most. However, whether Tails is suitable for everyday use is something everyone has to decide for themselves. Alternative desktop environments Since I do some desktop hardening for client systems used in development and office environments, this is my personal opinion and experience from the past few years with Debian 8–12 . The problem with some desktop environments at the moment is that they only run on X11 , while support for Wayland is still experimental . I’ve already mentioned this in several posts, so I don’t have to repeat it again. Wayland vs. X11 (Part..) Cinnamon Desktop The Cinnamon desktop is, in my opinion, one of the best when it comes to customization options. It allows a lot of adjustments and is also one of the most similar to Windows. The current dilemma, however, is that Wayland support is still experimental, and in the past, I often experienced freezes, hangs, or screen artifacts after various updates, upgrades, and software installations. KDE Desktop A very powerful and excellent desktop environment that I also use, but some settings sometimes don’t work properly or are a bit clunky, especially when it comes to the start menu and the taskbar. Additionally, when using external themes or widgets, they can sometimes slow down the system, the desktop environment itself. XFCE Lightweight and fast, but I miss many of the features that are standard in KDE. Wayland support is still experimental at the moment. You can customize this desktop environment to achieve a Windows-like look and feel, but it can also be a bit finicky at times when trying to change certain settings. Openbox A window manager that lets you build your entire desktop from scratch . You start with a blank canvas, just the background and windows and you place and configure each element manually by adding/installing various components. These are the most common ones, but there are many others like LXDE , LXQt , MATE , etc. Graphical Desktop Environment Three Components Working Together in a Graphical Desktop Environment. Display Server (X11, Wayland, etc.): Handles communication between applications and the graphics card/display Desktop Environment (KDE Plasma, GNOME, XFCE, etc.): Provides the user interface including windows, panels, system menus, etc Display Manager (SDDM, GDM, LightDM, etc.): Is the login screen, graphical login, that authenticates the user and then starts the session, the Desktop Environment ( However, it is not indispensable, as one could also log in via console (TTY) and starts a session ) Some combinations harmonize very well, while others are only experimental and can cause errors in the past and at the moment! If you want to try them all, you can test most of them using live systems, or you can install, for example, Debian with all the available desktop environments and try them out. This takes a lot of time, and in the end, you should consider functionality and security depending on your use case when choosing a desktop environment.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800178/how-to-achieve-persistent-quicklaunch-behaviour-with-gnome-on-ubuntu

---

#### 570. How to check and rerun an apt-upgrade command when you find you're out of disk space?

**问题描述 / Problem Description**:
Tags: ubuntu, apt | Score: 4 | Views: 1524 | Answers: 2 | Created: 2025-10-01

**解决方案 / Solution**:
apt logs the changes it makes in /var/log/apt/history.log . You should find your upgrade there, with the list of packages involved. However if you suspect that packages may be missing files, a better option is to check package contents using debsums . See apt-get update with https sources broken for details; the command to use is (assuming the default value of $IFS ): sudo apt reinstall $( LC_ALL=C.UTF-8 dpkg -S $(sudo debsums -c) | sed '/^diversion by /d; s/:.*//; s/, /\n/g' | sort -u ) If you have packages that are installed but not configured, run sudo dpkg --configure --pending to configure them. Recent versions of apt now check available disk space before starting an operation, but that doesn’t help if something else uses disk space while apt is running.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800123/how-to-check-and-rerun-an-apt-upgrade-command-when-you-find-youre-out-of-disk-s

---

#### 571. Proper way to power off a Ubuntu 22.04-5 desktop from single user mode

**问题描述 / Problem Description**:
Tags: ubuntu, shutdown | Score: 4 | Views: 1041 | Answers: 2 | Created: 2025-08-13

**解决方案 / Solution**:
Try poweroff -f . The -f flag should also work for reboot and halt . Try Alt-SysRq-o Note that either way, you should unmount everything you can first. At the very least, everything you mounted yourself.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798785/proper-way-to-power-off-a-ubuntu-22-04-5-desktop-from-single-user-mode

---

#### 572. How may I install a specific version of a package only if the installed version is not higher

**问题描述 / Problem Description**:
Tags: ubuntu, apt, software-installation, version | Score: 4 | Views: 417 | Answers: 1 | Created: 2025-07-31

**解决方案 / Solution**:
Not yet fully tested but it appears that: apt satisfy "percona-server-server (>= 8.4.5-5)" may solve my actual problem. (I don't care what version is installed, I care that at least a min version is installed.) Where this may introduce unexpected behavior: This will not install the required version. It will only try to install the most current version and fail if it cannot do that. To test this, I downgraded to: aptitude install percona-server-server=8.4.0-1-1.noble ( aptitude allows downgrading, apt / apt-get would error on the dependency versions.) If at one point the most current version changes, one may run into an error like this: DEBIAN_FRONTEND=noninteractive apt satisfy -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" "percona-server-server (>= 8.4.0), percona-server-server (<=8.4.4)" Reading package lists... Done Building dependency tree... Done Reading state information... Done Some packages could not be installed. This may mean that you have requested an impossible situation or if you are using the unstable distribution that some required packages have not yet been created or been moved out of Incoming. The following information may help to resolve the situation: The following packages have unmet dependencies: satisfy:command-line : Depends: percona-server-server (<= 8.4.4) but 8.4.5-5-1.noble is to be installed E: Unable to correct problems, you have held broken packages.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798406/how-may-i-install-a-specific-version-of-a-package-only-if-the-installed-version

---

#### 573. How can show the CJK character whose unicode is "02B6A5" in terminal?

**问题描述 / Problem Description**:
Tags: debian, fonts, unicode | Score: 3 | Views: 119 | Answers: 2 | Created: 2026-02-06

**解决方案 / Solution**:
Noto Sans Mono CJK SC doesn't have the U+2B6A5 character, which you can confirm with: $ fc-match --format='%{file} [%{fullname}]:\n%{charset}\n' 'Noto Sans Mono CJK SC' /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc [Noto Sans Mono CJK SC]: 20-7e [...] 2b689 2b695-2b696 2b6ad 2b6ed 2b746 [...] You can tell which font on your system covers that codepoint with fc-list :charset=2b6a5 . On my Debian system after installing a few TrueType font packages that have CJK in their description (see aptitude search '^fonts- ~d CJK' ): $ fc-list :charset=2b6a5 /usr/share/fonts/truetype/babelstone/BabelStoneHan.ttf: BabelStone Han:style=Regular You can tell which package it comes from with dpkg -S : $ dpkg -S /usr/share/fonts/truetype/babelstone/BabelStoneHan.ttf fonts-babelstone-han: /usr/share/fonts/truetype/babelstone/BabelStoneHan.ttf lxterminal is VTE based like gnome-terminal , so does support font fallback via pango -> fontconfig. It should just be a matter of installing that fonts-babelstone-han package. Your version of Linux kernel suggests you're using Debian 12. I've installed all the fonts-* packages on a Debian 12 incus container with: apt-get install --mark-auto '^fonts-.' After which I find more fonts with that character: debian-12:~# fc-list :charset=2b6a5 /usr/share/fonts/truetype/cns11643/TW-Sung-Ext-B-98_1.ttf: TW\-Sung\-Ext\-B,全字庫正宋體 Ext\-B:style=Regular /usr/share/fonts/truetype/hanazono/HanaMinB.ttf: HanaMinB,花園明朝B:style=Regular /usr/share/fonts/truetype/cns11643/TW-Kai-Ext-B-98_1.ttf: TW\-Kai\-Ext\-B,全字庫正楷體 Ext\-B:style=Regular /usr/share/fonts/truetype/babelstone/BabelStoneHan.ttf: BabelStone Han:style=Regular That's from these packages: debian-12:~# fc-list :charset=2b6a5 | cut -d: -f1 | xargs dpkg -S fonts-cns11643-sung: /usr/share/fonts/truetype/cns11643/TW-Sung-Ext-B-98_1.ttf fonts-hanazono: /usr/share/fonts/truetype/hanazono/HanaMinB.ttf fonts-cns11643-kai: /usr/share/fonts/truetype/cns11643/TW-Kai-Ext-B-98_1.ttf fonts-babelstone-han: /usr/share/fonts/truetype/babelstone/BabelStoneHan.ttf

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804295/how-can-show-the-cjk-character-whose-unicode-is-02b6a5-in-terminal

---

#### 574. pass-otp fails on second device

**问题描述 / Problem Description**:
Tags: linux, password-store | Score: 3 | Views: 151 | Answers: 1 | Created: 2025-12-29

**解决方案 / Solution**:
Usually 6-digit 'TOTP' 2FA codes are generated from the current Unix timestamp divided by 30 (30 seconds being the interval). This relies on the device knowing the correct UTC time. If the device runs Linux, check date -u to make sure the kernel clock is correct; it should show the same UTC time ( not local time) on both devices. (The linked website will also this automatically.) You can also run date +%s to compare the Unix timestamps directly. Normally the kernel clock runs on UTC, and programs use the timezone to offset timestamps into your local time for display purposes. It could be that the second device has it backwards, i.e. had its timezone set to GMT/UTC but the kernel clock directly set to your local time instead, which would cause the Unix timestamps to be off by several hours despite appearing correct in the GUI clock. Install oath-toolkit and run oathtool --totp --base32 with the same secret key taken from pass . It automatically uses the current Unix timestamp. If oathtool shows the correct result but pass-otp is wrong, then the problem is likely with pass-otp.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803376/pass-otp-fails-on-second-device

---

#### 575. Detect if any ping succeeds

**问题描述 / Problem Description**:
Tags: linux, networking, ping | Score: 3 | Views: 975 | Answers: 6 | Created: 2025-11-26

**解决方案 / Solution**:
You don't need the separate script (or the bash shell). Shell code can also be given as argument with the -c option (that's what the system("shell code") function of most languages use): if echo host1 host2 host3 | xargs -n1 -P0 sh -c '! "$0" "$@"' ping -c1 -w2 then echo 'They all failed' else echo 'At least one succeeded' fi In: sh -u -ce -o xtrace -- 'shell code' 'script name' 'arg 1' 'arg 2' (here -u , e and -o xtrace to show you can have more options before or after -c ) the first non-option argument (here shell code ) is the code to interpret the second ( script name ) a name you want to give to that inline script (the equivalent of the file name for a script in a file). It has these effects: it's used for instance in error messages that the shell generates to tell the user the error is coming from that script. it's what the $0 special parameter expands to. and the remaining arguments make up the arguments of the inline script, so are available in the shell code as $1 , $2 ... with "$@" the verbatim list of them all. So, here with sh -c '! "$0" "$@"' ping -c1 -w2 , we're creating an inline script which we call ping . xargs will pass -c1 , -w2 and one word read from stdin at a time as arguments to that script, and that script runs the command called ping with those arguments and the exit status reversed with ! . You may argue that shell error messages if any showing as "ping" error messages, may be confusing to the user, so you could change it to sh -c '! "$@"' sh ping -c1 -w2 for the inline script's name to be sh instead. But here I'd argue that to scan networks, you'd rather use things like nmap than ping in a loop.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801633/detect-if-any-ping-succeeds

---

#### 576. How do you get PCI-1 NVMe expansion cards to allow SSD to act as boot device?

**问题描述 / Problem Description**:
Tags: ubuntu, hard-disk, hardware | Score: 3 | Views: 550 | Answers: 1 | Created: 2025-10-25

**解决方案 / Solution**:
The only thing that is a downer about those adapters is that it says that the SSD you install on them cannot act as a boot device. Why exactly is that? Is there a workaround for that? That's because nothing, because not true: If your system supports booting from an nvme depends on your system's firmware, not on some passive adapter. I used a similar one and it just works fine as boot device; the system bootloader cares not the least to which PCIe complex port the nvme it boots from is connected. If it doesn't work, that's a limitation of your server's firmware, and can at best be worked around by putting the EFI system partition on some other device and just booting from that while keeping the actual data on your nvme. Frankly, I wouldn't see why a server wouldn't boot from an nvme; this isn't exactly a new thing in the server world; I'd expect any server with firmware written in the last 10 years to support nvme SSDs out of the box, on any PCIe port, whether it's directly connected to an on-board M.2 slot, plugged in to a full-size PCIe port, SATA Express, OCuLink, ePCIe…: PCIe is in the end pretty much like Ethernet in that regard: for using any device for any purpose, it really doesn't matter into which port on your switch it's plugged, or whether it's plugged into a second switch attached to your first, and whether the link is 10 Gb/s ethernet or Ethernet-over-Wet-String (DSL).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800762/how-do-you-get-pci-1-nvme-expansion-cards-to-allow-ssd-to-act-as-boot-device

---

#### 577. Why and how were KVM modules unexpectedly enabled in Ubuntu 24.04?

**问题描述 / Problem Description**:
Tags: ubuntu, virtualbox, kernel-modules, kvm | Score: 3 | Views: 3440 | Answers: 3 | Created: 2025-07-21

**解决方案 / Solution**:
In version 6.12 of the Linux kernel, kvm module initialisation was changed — it now takes place as soon as the modules are loaded, and not the first time they are used. This prevents VirtualBox from working, as you discovered. This is documented in the VirtualBox 7.1.4 release notes . Since your system was upgraded from 6.11 to 6.14, that explains the sudden appearance of the symptoms. To return to the previous situation (where KVM modules can be loaded without preventing VirtualBox from working), you can add kvm.enable_virt_at_load=0 to the kernel boot parameters. If you’re using Grub on a Debian derivative, that’s done by adding the parameter to the GRUB_CMDLINE_LINUX_DEFAULT= line in /etc/default/grub , then running sudo update-grub . After a reboot, this will allow VirtualBox to work, without preventing any other KVM-based tool from working either. The other option is to disable the KVM modules entirely; this is safe, but will prevent any KVM-based tool from working. See cas’ answer for details.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798132/why-and-how-were-kvm-modules-unexpectedly-enabled-in-ubuntu-24-04

---

#### 578. ThinkPad T14 Gen1 - Trackpoint - Wayland - Stops working during usage

**问题描述 / Problem Description**:
Tags: ubuntu, wayland, thinkpad, trackpoint | Score: 3 | Views: 1100 | Answers: 1 | Created: 2025-07-19

**解决方案 / Solution**:
Try to solve the problem with psmouse.synaptics_intertouch -- either as a kernel parameter in GRUB or via a config file in /etc/modprobe.d/psmouse.conf as described here. psmouse` failing to initialize after suspend/hibernate - help for possible workaround needed Touchpad Synaptics Try alternative drivers. Install libinput as a replacement for synaptics, or check if you can update the Elan-TrackPoint firmware. libinput libinput Touchpad LibinputTouchpad Elan-TrackPoint TPPS/2 Elan Trackpoint on Thinkpad T495 with Kubuntu 20.04 ThinkPad Elan TrackPoint sensitivity adjustment on Linux (Fedora)? TrackPoint Check this post to: This is solution, that has worked for me: sudo rmmod psmouse sudo modprobe psmouse proto=imps or sudo modprobe -r psmouse && sudo modprobe psmouse proto=imps Make it permanent: sudo gedit /etc/modprobe.d/options Add line: options psmouse proto=imps This fix will make the touchpad be recognized as a mouse instead, which might remove some features specific to touchpads such as disable while typing and scroll gestures. Touchpad stopped working 20.04 VSC and touchpad: Mostly I get it when using VSC or solitaire... If touchpad stops working in VSC on Ubuntu, it's more a general touchpad issue rather than a VSC problem. VS Code touchpad scrolling moving cursor instead of page touch pad randomly stopped working on ubuntu desktop Trackpad stopped working suddenly on Ubuntu and Windows after installing Ubuntu 22.04 LTS Visual Studio Code and Arduino IDE stopped working It's a linux driver issue. In the terminal, find out what hardware you have. Do lshw . Find the touch-pad and see what drivers it is using.... Touchpad isn't working properly

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798083/thinkpad-t14-gen1-trackpoint-wayland-stops-working-during-usage

---

#### 579. How can I resolve a dependency conflict for installing GDB?

**问题描述 / Problem Description**:
Tags: debian, apt, gdb | Score: 2 | Views: 290 | Answers: 1 | Created: 2026-02-18

**解决方案 / Solution**:
You’ve installed packages from backports, but you’re trying to install gdb and its missing dependencies from the main release — that’s what’s causing the problems. Assuming you really wanted to install libelf1t64 etc. from backports, you might as well install gdb from backports too: sudo apt install -t trixie-backports gdb Since you’re new (again) to Debian, it would be better to stick to the main release, but fixing that at this stage is likely to be more complex than continuing to pull related packages from backports. Whatever you do though, don’t enable backports for all package installations; only do so when necessary.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804557/how-can-i-resolve-a-dependency-conflict-for-installing-gdb

---

#### 580. apt remove does not fail upon removing a package that is a dependency of another

**问题描述 / Problem Description**:
Tags: debian, apt, package-management, dependencies | Score: 2 | Views: 306 | Answers: 1 | Created: 2026-02-17

**解决方案 / Solution**:
APT is a resolver: it does whatever is necessary to achieve the state requested by whatever commands it’s given, while ensuring that the overall state of packages is consistent (all installed packages have their dependencies installed too). So apt remove librsvg2-common means “starting from the current package state of the system, find me a package state such that librsvg2-common is no longer installed”. Achieving that involves removing packages that depend on librsvg2-common , unless another package can be installed to satisfy the dependency. If you want a tool where you can try removing a package to see whether doing so would also remove dependent packages, you need to use the -s option ( --simulate ), as you’ve already found. Even without -s , by default apt will show you what it wants to do, and ask for confirmation before proceeding. I don’t know about many other package managers in detail, but DNF also behaves in this way. There’s a slight difference between APT and DNF however: DNF allows packages to be protected from removal, and it will refuse to remove a package if that would involve removing a protected package. APT has a similar feature, holding a package, but that also prevents the package from being upgraded.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804528/apt-remove-does-not-fail-upon-removing-a-package-that-is-a-dependency-of-another

---

#### 581. GRUB changes don't take effect

**问题描述 / Problem Description**:
Tags: debian, grub | Score: 2 | Views: 397 | Answers: 1 | Created: 2026-02-10

**解决方案 / Solution**:
You firmware is configured to first execute grub from the TuxedoOS. Two installed Linux systems each have their own bootloader ( grub ) with independent configuration . You were changing the configuration of Debian grub which is not what TuxedoOS grub is using. The GRUB_DEFAULT refers to the menu entry inside grub.cfg , not to the firmware boot entries. To change firmware boot order and set Debian as the primary boot option either use your BIOS Setup or run from Linux efibootmgr -o 0001,0002,0003,0000,0004,0005,0006 This command reverses the position of Debian and TuxedoOS; you can use any order that suits you. Keep in mind that some systems simply refuse to remember the efibootmgr settings (they appear OK until reboot and then revert to the previous values), so BIOS Setup is usually better option. And yes, if you want to keep TuxedoOS grub as default you can change the default menu entry in the TuxedoOS grub.cfg in the usual way as you have found (setting GRUB_DEFAULT ).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804368/grub-changes-dont-take-effect

---

#### 582. How to migrate xsession/xinitrc sessions to display managers?

**问题描述 / Problem Description**:
Tags: debian, login, startup, session, display-manager | Score: 2 | Views: 116 | Answers: 1 | Created: 2026-02-06

**解决方案 / Solution**:
The startx invokes xinit which will start Xserver and run the command you have given. With no command some distribution dependent xinitrc is executed which may perform quite some distribution-dependent initialization before finally calling your ~/.xsession . Invoking ~/.xsession directly will skip all these steps. Using xdm as display manager should behave identically to startx without any explicit setup on your side. While xdm is not integrated with systemd-logind , neither was your solution so far. More modern display managers do use the session definitions you listed. But for the reasons I mentioned it makes sense to find out the "master" xinit script and invoke it instead of ~/.xsession directly. Your session must be in /usr/share/xsessions in this case - it is very unlikely that your ~/.xsession will work under Wayland. If the only thing your ~/.xsession does is starting the window environment of your choice, then it is probably already handled by the distribution. On Debian the i3-wm package installs /usr/share/xsessions/i3.desktop which you can simply chose in your Display Manager greeter. E.g. on Ubuntu 24.04: It does bypass all the scripts in /etc/X11/Xsession.d , but if something is missing compared with statrx it is a topic for a bug report. Actually, no ~/.xsession was needed with startx either. The standard xinit processing will by default start the /usr/bin/x-session-manager which is configured using update-alternatives and i3-wm also installs itself (and if this is the only window manager it will be used without any explicit step): bor@numbat:~$ update-alternatives --display x-session-manager x-session-manager - manual mode link best version is /usr/bin/gnome-session link currently points to /usr/bin/i3 link x-session-manager is /usr/bin/x-session-manager slave x-session-manager.1.gz is /usr/share/man/man1/x-session-manager.1.gz /usr/bin/gnome-session - priority 50 slave x-session-manager.1.gz: /usr/share/man/man1/gnome-session.1.gz /usr/bin/i3 - priority 30 slave x-session-manager.1.gz: /usr/share/man/man1/i3.1.gz bor@numbat:~$ It is also possible to setup session using full processing, like bor@numbat:~$ cat /usr/share/xsessions/xinit.desktop [Desktop Entry] Name=Generic xinit Comment=XDM compatibility Exec=/etc/X11/xinit/xinitrc TryExec=/etc/X11/xinit/xinitrc Type=Application X-LightDM-DesktopName=xinit DesktopNames=xinit Keywords=wm;windowmanager;window;manager; bor@numbat:~$ Specifically on Ubuntu the funny effect is that when x-session-manager is set to GNOME, it starts the vanilla GNOME, while selecting Ubuntu session will start Ubuntu branded.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804296/how-to-migrate-xsession-xinitrc-sessions-to-display-managers

---

#### 583. Is it possible in x11 to make the application border invisible?

**问题描述 / Problem Description**:
Tags: linux, x11, window-manager, window-decorations, emulators | Score: 2 | Views: 85 | Answers: 2 | Created: 2026-01-31

**解决方案 / Solution**:
In the X Window System, window borders are usually drawn by window managers. Since you don’t have a window manager, the border you see here is entirely controlled by Mini vMac. You end up seeing it because your display ratio doesn’t match the Mac’s: 512×342 for a Mac Plus, 4:3 for a Mac II (512×384, 640×480 etc.). (I’m only counting pixels here, and ignoring physical aspect ratios.) Given typical widescreen displays nowadays, there isn’t much you can do about this if you want accurate emulation. If you switch to a 4:3 display you’ll be able to set up a Mac II emulation with no lost screen space, but still not a Mac Plus. Mini vMac can emulate arbitrary resolutions, as long as the display fits in VRAM; you could use that to set up an emulated display matching your real display (with magnification), but that could cause issues with Mac software. See the Mini vMac documentation for details .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804157/is-it-possible-in-x11-to-make-the-application-border-invisible

---

#### 584. How to fix /bin/sh: can't access tty; job control turned off .I am building minimal linux os

**问题描述 / Problem Description**:
Tags: linux, linux-kernel, tty, initramfs, busybox | Score: 2 | Views: 696 | Answers: 1 | Created: 2026-01-17

**解决方案 / Solution**:
run cttyhack . Or script -c /bin/sh /dev/null , if your system has the script(1) utility[1] (which is simply creating a new pseudoterminal in the same manner as sshd, and so it's a more robust and general solution). [1] most Linux systems, including e.g. my $100 Android phone, my OpenWRT router and my Ubuntu system do include script by default, but YMMV wrt its availability, OK.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803846/how-to-fix-bin-sh-cant-access-tty-job-control-turned-off-i-am-building-mini

---

#### 585. Install minimal gnome in debian 13

**问题描述 / Problem Description**:
Tags: debian, gnome, gui, desktop-environment, desktop | Score: 2 | Views: 1180 | Answers: 1 | Created: 2026-01-14

**解决方案 / Solution**:
I don’t know what exactly your goal is, but this here should probably be one of the most minimal GNOME installations. apt install gnome-shell mutter You get these automatically installed: GTK libraries GNOME Settings Daemon GNOME Control Center dependencies Wayland components Graphics driver interfaces D-Bus services 1. gnome-shell This is the actual GNOME interface that you see and use. Top bar Activities overview App overview Workspaces Extensions Controls which GNOME services start at login Appears in the login manager (GDM) as GNOME or GNOME Wayland 2. Mutter GNOME’s window manager and compositor. manages windows (move, maximize, minimize) Provides animations and visual effects Communicates with the graphics card Is also the Wayland compositor If it is not already present and you don’t want to start the desktop session via the shell, but instead through a display manager with a login screen, that would be gdm3 . apt install gdm3 This gives you a minimal installation. If you now also need a file manager such as Dolphin , Thunar , or Nautilus along with the required packages, you can look here. Debian LUKS error with Dolphin, Thunar, and Nautilus: 'bd_crypto_luks_open_blob called but not implemented', cannot open LUKS partition/device Now you can check what you might still need, such as Firefox , Gedit , etc., and install them as well. In my opinion, this is one of the most minimal installations. It also doesn't feel quite complete or adequate when you're used to the standard desktop installation in Debian or Ubuntu. Here is another list, then it fills in better. sudo apt install \ gnome-shell \ mutter \ gnome-control-center \ gnome-terminal \ gdm3 \ nautilus \ network-manager \ gnome-settings-daemon \ xdg-desktop-portal \ xdg-desktop-portal-gnome \ pipewire wireplumber \ firefox-esr \ gedit With this approach, I would then try to harden my system and/or remove additional packages. There will always be packages that other packages need, i.e. dependencies, which you can’t simply uninstall or choose not to install. But you’ll have to experiment with that yourself as well.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803746/install-minimal-gnome-in-debian-13

---

#### 586. Debsums result "dpkg-query: no path found matching pattern /lib/x86_64-linux-gnu/libgcc_s.so.1"

**问题描述 / Problem Description**:
Tags: debian, security, libraries | Score: 2 | Views: 100 | Answers: 1 | Created: 2026-01-11

**解决方案 / Solution**:
The message means that debsums has a hash for /lib/x86_64-linux-gnu/libgcc_s.so.1 but that dpkg doesn’t know about it, probably because it knows it as /usr/lib/x86_64-linux-gnu/libgcc_s.so.1 . This shouldn’t happen since both sources of information are maintained by dpkg , but it’s possible that you have an old .md5sums file left over. grep -F lib/x86_64-linux-gnu/libgcc_s.so.1 /var/lib/dpkg/info/*.md5sums will find all files referencing the library in either of its paths ( /lib or /usr/lib ). To fix this, remove obsolete .md5sums file(s) (if any) and reinstall libgcc-s1 .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803674/debsums-result-dpkg-query-no-path-found-matching-pattern-lib-x86-64-linux-gnu

---

#### 587. Trying to install MinGW means I can no longer install GCC

**问题描述 / Problem Description**:
Tags: ubuntu, gcc, mingw | Score: 2 | Views: 238 | Answers: 1 | Created: 2025-09-16

**解决方案 / Solution**:
Running ../configure --host=x86_64-w64-mingw32 isn’t sufficient; as indicated in the build instructions , you need to specify the target triplet in the prefix: ../configure --host=x86_64-w64-mingw32 --prefix=/usr/local/x86_64-w64-mingw32 Otherwise the header files end up being installed in /usr/local/include , as you found, and pulled in by the regular C compiler. To fix this, you should uninstall the MinGW-w64 headers; in your existing build tree, run sudo make uninstall or, if that doesn’t work, delete the contents of /usr/local/include . If you end up having to do that you’ll also have to reinstall whatever was previously installed there.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/799718/trying-to-install-mingw-means-i-can-no-longer-install-gcc

---

#### 588. Monitor continuous blanking issue on Ubuntu 20.04

**问题描述 / Problem Description**:
Tags: ubuntu, xorg, nvidia, multi-monitor | Score: 2 | Views: 424 | Answers: 2 | Created: 2025-08-27

**解决方案 / Solution**:
Try connecting the second monitor with a direct DisplayPort-to-HDMI or DP-to-DP cable instead of using the HDMI-to-DP adapter. Often the problem lies in the signal conversion in the adapter, which can become unstable, especially with KVM switches or older GPUs. My guess would be, the KVM is a purely passive device that supports and supports only the DP standard (including dual-mode, a.k.a. DP++), therefore it will work with: connection involve DP and DP only (obviously) a DP++ source (PC) and a TMDS sink (Monitor), i.e. [PC]DP->DP[KVM]DP->HDMI/DVI[Monitor] Displayport KVM switch not passing signal if Adaptive HDMI to Displayport Cable/Adapter and Displayport to DVI cable used Problems with second monitor with HDMI to DisplayPort converter What could be the reason that my "Displayport To HDMI Adapter" does not work? DisplayPort vs HDMI: Which Cable Is Best for Your Setup? If that doesn’t help, a firmware update for the KVM switch or a newer GPU driver might also improve stability. Or, if possible, try a different switch. Some switches have problems with certain resolutions, refresh rates, or signal conversions (e.g., from DP to HDMI). Otherwise, you'll have to accept it as is.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/799212/monitor-continuous-blanking-issue-on-ubuntu-20-04

---

#### 589. Do special (language specific) characters keep a hidden trace when deleted in a physical tty? Looking for explanation of failed logins into tty

**问题描述 / Problem Description**:
Tags: ubuntu, tty, keyboard-layout | Score: 2 | Views: 150 | Answers: 1 | Created: 2025-08-20

**解决方案 / Solution**:
It sounds like your Virtual Console (VC) keymap is not set correctly, since your localectl status says that the value is (unset) . This will cause Linux to use the default keymap , which probably doesn't match your physical keyboard, and can result in regular keys sending anything imaginable including Ctrl-C . For a US keyboard, you should be able to localectl set-keymap us or localectl set-keymap us-intl . There is also a de-us you could try, which might be what you're referring to from the installation process. If those don't work, you can see all available keymaps with localectl list-keymaps . DEBIAN EDIT: It seems that while Debian does package and install localectl by default, they want you to use dpkg to set these settings. All of the other below technical concepts still apply, just not using localectl to change the settings. Background info There are 3 pieces of information that can change depending on where you are in the world: 1. LANG LANG is known as the "locale" (hence localectl ). This controls what language is used for multi-lingual ("internationalized") apps, and also controls things like how money and dates are formatted. LANG can be set with localectl set-locale , and the list of options is at localectl list-locales . Under the hood, localectl set-locale is calling setlocale(3) . See also: locale(7) . Note that technically a locale has many different pieces of information which can be configured independently (for example, you could use USA dates but DE money formats). localectl treats them as one big setting since that's what most people want. 2. The Virtual Console ("VC") keymap At the hardware level, a keyboard just sends messages like "button number 83 was pressed." A keymap is how the kernel translates these button presses into characters that match what's printed on the keys. The VC keymap is used for Linux's "text mode". This is what you're using when you Ctrl-Alt-F3 . The VC keymap is set with localectl set-keymap , and the list of options is at localectl list-keymaps . Under the hood, localectl set-keymap is calling loadkeys(1) . See also: keymaps(5) . 3. The X11 keymap Way back in history, X11 was the "graphical mode" of Linux and it too needed a keymap, but the VC and X11 keymaps couldn't be shared so they are completely separate settings. (You can, for example, use "us-dvorak" on the virtual console and "de" in X11.) This is because the X11 keymap can store several additional pieces of information such as the keyboard model to determine the final keymap. Note that the X11 setting is also referenced by most Wayland systems, so it's still relevant. To set the X11 keymap, you can use localectl set-x11-keymap <LAYOUT> <MODEL> <VARIANT> <OPTIONS> . Only the LAYOUT is mandatory - everything else can be omitted unless needed. Note on keymap translation In modern times, localectl can usually translate from a VC keymap to an X11 keymap, or vice-versa. So setting one will attempt to set the other at the same time so they match. (You can disable this by passing the --no-convert flag to set only one or the other.) Since it might be a part of your story here, note that this conversion can fail, and they are in fact two separate settings. localectl will tell you if this conversion fails. DEBIAN EDIT : According to keyboard(5) , there is only a single setting in the config file but it is applied separately to X11 and VC by two different programs. How to fix your locale if you can't log into the console There are several ways to get around being unable to use the virtual console. The VC Keymap is a system-wide setting, meaning that even if you set this setting from the GUI or other places, it will take effect on the virtual console ("physical" text mode). Here are some options, roughly in increasing levels of difficulty: 1. Use the GUI Your GUI might have the correct keyboard settings while the text terminal does not. If you can log into the GUI and open a terminal window, you should be able to issue these commands. 2. Use a keyboard that matches the existing keymap This one might be obvious, but if you have a physical keyboard that does work correctly, just use that long enough to set the settings to match the other keyboard. 3. Use SSH If you can ssh into the machine from another machine, you very likely have the necessary permissions to run setlocale from an SSH session. 4. Set kernel options at boot time When you turn on your computer, a "boot loader" helps get Linux started. Just like a regular program on the CLI, the Linux kernal can take command-line options, and it's your boot loader's job to set these up. There are many different boot loaders, and they all operate differently, but perhaps one of the most-common is grub2. See: " How do I add a kernel boot parameter? ". The option you need to set is vconsole.keymap=de or similar. 5. Boot into single-user mode You might need to combine this with option 2 and/or 4. In short, getting past login is often the hardest part. Depending on your system config, it may be possible to tell your boot loader to boot in "single-user" mode and bypass the login process. You'll find yourself at a bash terminal as root, as though you had logged in. You then might be able to issue enough commands to fully correct the problem. See: boot into single user mode . 6. Boot a live distro and edit the config file Your system almost certainly sets the VC settings at boot time by looking at /etc/vconsole.conf(5) . If you can boot a live distro (probably from USB stick) then you should be able to mount your root volume and edit this file. For reference, here is a default US config: KEYMAP=us FONT=eurlatgr XKBLAYOUT=us DEBIAN EDIT: On Debian systems this is /etc/default/keyboard(5) Finding the right keymap If you manage to set keymaps but are unsure as to the correct one, you can use showkey(1) to see what keycodes are being emitted by your keyboard. You can then look at the keymap files (typically in /usr/lib/kbd/keymaps ) to see how each map translates these into characters.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/799021/do-special-language-specific-characters-keep-a-hidden-trace-when-deleted-in-a

---

#### 590. SSH from Windows into Linux using Pubkey, getting Permission Denied (publickey)

**问题描述 / Problem Description**:
Tags: ubuntu, ssh, windows | Score: 2 | Views: 252 | Answers: 1 | Created: 2025-08-13

**解决方案 / Solution**:
As steeldriver stated, I needed to have the Private key on the Windows side. The reason it kept working locally on the Raspberry Pi was because both files were in there. A classic "works on my machine" situation. :D

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798816/ssh-from-windows-into-linux-using-pubkey-getting-permission-denied-publickey

---

#### 591. How to disable Journald's ForwardToSyslog=yes on Ubuntu 24.04?

**问题描述 / Problem Description**:
Tags: ubuntu, systemd, rsyslog, syslog, systemd-journald | Score: 2 | Views: 182 | Answers: 1 | Created: 2025-08-13

**解决方案 / Solution**:
After reading more Systemd docs I found the answer. https://www.freedesktop.org/software/systemd/man/latest/systemd-system.conf.html In addition to the main configuration file, drop-in configuration snippets are read from /usr/lib/systemd/ .conf.d/, /usr/local/lib/systemd/ .conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files. The default syslog.conf was sorted after my override.conf so it took precedence. After renaming my file to x-override.conf it took effect after restaring systemd-journald.service .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798801/how-to-disable-journalds-forwardtosyslog-yes-on-ubuntu-24-04

---

#### 592. Ubuntu server keeps shutting down after 15 minutes

**问题描述 / Problem Description**:
Tags: ubuntu, shutdown | Score: 2 | Views: 557 | Answers: 2 | Created: 2025-08-05

**解决方案 / Solution**:
Repeated the failure Having installed AlmaLinux 10.1 on a Dell Optiplex XE4 desktop I started having the same problem. When switched the PC on and connected remotely using ssh -X , then after 15 minutes of up-time the PC was suspended. The first thing I tried was when logged onto the console as a normal user under Settings -> Power -> Power Saving was to set Automatic Suspend to Off . The following, when run as my normal user, confirmed that sleep-inactive-ac-type was 'nothing' : $ gsettings list-recursively org.gnome.settings-daemon.plugins.power org.gnome.settings-daemon.plugins.power ambient-enabled true org.gnome.settings-daemon.plugins.power idle-brightness 30 org.gnome.settings-daemon.plugins.power idle-dim true org.gnome.settings-daemon.plugins.power power-button-action 'suspend' org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery true org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing' org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'suspend' However, when not logged in remotely via ssh, with no console login, after 15 minutes of up-time the PC was still suspended. Just prior to the PC suspending a message of the following form was seen on the the ssh sessions: Broadcast message from gdm@alder-lake-alma on tty1 (Sat 2025-12-27 10:08:44 GMT): The system will suspend now! Initial work-around attempt to mask the sleep and suspend services As suggested by the answer Ubuntu 22.04 is sleeping even though I changed the power settings so it shouldn't sleep masked the following sleep / suspend related services: $ sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target Created symlink '/etc/systemd/system/sleep.target' → '/dev/null'. Created symlink '/etc/systemd/system/suspend.target' → '/dev/null'. Created symlink '/etc/systemd/system/hibernate.target' → '/dev/null'. Created symlink '/etc/systemd/system/hybrid-sleep.target' → '/dev/null'. That did stop the PC from actually suspending after 15 minutes of up time with no console login. However, after 15 minutes of up time the following was broadcast on the ssh sessions: Broadcast message from gdm@alder-lake-alma on tty1 (Sat 2025-12-27 21:05:36 GMT): The system will suspend now! Therefore, while masking the services did prevent the PC from actually suspending it didn't prevent gdm from attempting to suspend. I.e. still resulted in confusing broadcast message. Reverted the masking of the services, to look for a different solution: $ sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target [sudo] password for mr_halfword: Removed '/etc/systemd/system/sleep.target'. Removed '/etc/systemd/system/suspend.target'. Removed '/etc/systemd/system/hibernate.target'. Removed '/etc/systemd/system/hybrid-sleep.target' Applying power settings for the user which runs the display manager The Reddit how to disable automatic suspend on GDM gave the idea to look for the power settings used by the gdm user, since AlmaLinux 10.1 is using the gdm display manager. For the gdm user sleep-inactive-ac-type was 'suspend' : $ sudo -u gdm gsettings list-recursively org.gnome.settings-daemon.plugins.power org.gnome.settings-daemon.plugins.power ambient-enabled true org.gnome.settings-daemon.plugins.power idle-brightness 30 org.gnome.settings-daemon.plugins.power idle-dim true org.gnome.settings-daemon.plugins.power power-button-action 'suspend' org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery true org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'suspend' org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'suspend' For the gdm user changed sleep-inactive-ac-type from 'suspend' to nothing : $ sudo -u gdm gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type nothing The above needs to be run when logged into the console, otherwise got a Failed to execute child process “dbus-launch” (No such file or directory) error. Rebooted after the above change, and checked for the gdm user sleep-inactive-ac-type was still 'nothing' : $ sudo -u gdm gsettings list-recursively org.gnome.settings-daemon.plugins.power [sudo] password for mr_halfword: org.gnome.settings-daemon.plugins.power ambient-enabled true org.gnome.settings-daemon.plugins.power idle-brightness 30 org.gnome.settings-daemon.plugins.power idle-dim true org.gnome.settings-daemon.plugins.power power-button-action 'suspend' org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery true org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing' org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 900 org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'suspend' This has fixed the issue for the AlmaLinux 10.1 installation. Are now at 1 hour of up time with no console login and: Without the PC suspending. There have been no The system will suspend now! broadcast messages on the ssh sessions. Different user to apply the power settings to for the lightdm display manager The self-answer by the original poster says they are using the lightdm display manager with Ubuntu server 24.04. For lightdm the command to disable the suspend should be: $ sudo -u lightdm gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type nothing

**参考链接 / References**:
- https://unix.stackexchange.com/questions/798542/ubuntu-server-keeps-shutting-down-after-15-minutes

---

#### 593. List all members of a group, where the group is primary?

**问题描述 / Problem Description**:
Tags: bash, debian, users, group | Score: 1 | Views: 121 | Answers: 1 | Created: 2026-02-18

**解决方案 / Solution**:
Yes, the primary group ID is a property of the user from the passwd database, while the group database gives names to gids (and several groups can have the same gid like several users can have the same uids) as well as listing additional users, so there's no other way than to: query group database for the gid for the group name, which you can do with getent -- group "$groupname" | cut -d: -f3 ¹ or: perl -le ' $name = shift; $gid = getgrnam $name or die "Cannot find group $name\n"; print $gid' -- "$groupname" both being interfaces to the standard getgrnam() function. query the passwd database for users with the corresponding gid as their primary gid. There is no standard getpw???() function to do that query, so you're left with listing all DB entries and filter by fourth field: getent passwd | awk -v gid="$gid" -F: '$4 == gid {print $1}' Or: perl -le ' $gid = shift; while (@user = getpwent) { print $user[0] if $user[3] == $gid }' -- "$gid" Both being interfaces to the standard getpwent() function. If you know what database is being used in the backend, you could query it directly, but there's no standard interface for doing that. That only works for passwd database backends that can be enumerated. That will be the case if it's file based, like with /etc/passwd but not necessarily for networked ones like LDAP/SQL-backed ones. Put together, that becomes: #! /bin/sh - set -o pipefail # needs a sh compliant to POSIX2024 die() { [ "$#" -eq 0 ] || printf>&2 '%s\n' "$@" exit 1 } [ "$#" -eq 1 ] || die "Usage: $0 <groupname>" groupname=$1 gid=$(getent -- group "$groupname" | cut -d: -f3) || die "Can't find group $groupname" getent passwd | awk -v gid="$gid" '$4 == gid {print $1}' Or: #! /usr/bin/perl @ARGV == 1 or die "Usage: $0 <groupname>"; $groupname = $ARGV[0]; $gid = getgrnam $groupname or die "Cannot find group $groupname\n"; while (@user = getpwent) { print "$user[0]\n" if $user[3] == $gid; } If you run members -p users under ltrace -e 'getpw*' -e 'getgr*' , you'll see it's exactly what it does: $ ltrace -e 'getpw*' -e 'getgr*' members -p users members->getgrnam("users") = 0x7f296a1fee00 members->getpwent(0, 0, -128, 0x7f296a1ff380) = 0x7f296a1ff380 members->getpwent(0, 0, -128, 0x7f296a1ff380) = 0x7f296a1ff380 members->getpwent(0, 0, -128, 0x7f296a1ff380) = 0x7f296a1ff380 members->getpwent(0, 0, -128, 0x7f296a1ff380) = 0x7f296a1ff380 [...] members->getpwent(0x55860a626188, 0x7f296a1f3790, 0x7f296a46c2f0, 2) = 0x7f296a1ff380 members->getpwent(0x55860a626188, 0x7f296a1f3790, 0x7f296a46c2f0, 2) = 0x7f296a1ff380 members->getpwent(0x55860a626188, 0x7f296a1f3790, 0x7f296a46c2f0, 2) = 0 user1 user2 user3 ¹ with the caveat that for all-numeric group names, that gives you the entry for the group by the given id, so returning the same number. But it would be a very bad idea to have all-numeric group names especially if the number is different from their gid.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804559/list-all-members-of-a-group-where-the-group-is-primary

---

#### 594. Additional integration of FUSE in Debian for the file managers Dolphin, Thunar, and Nautilus

**问题描述 / Problem Description**:
Tags: debian, nautilus, fuse, dolphin, thunar | Score: 1 | Views: 94 | Answers: 1 | Created: 2026-02-13

**解决方案 / Solution**:
In addition to the standard packages mentioned in that answer , install the additional packages kio-fuse for Dolphin and gvfs-fuse for Nautilus and Thunar . They expose KIO and GVFS mounts as FUSE filesystems, based on libfuse3 , which improves compatibility with external applications. For Dolphin apt install kio-fuse For Nautilus and Thunar apt install gvfs-fuse

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804438/additional-integration-of-fuse-in-debian-for-the-file-managers-dolphin-thunar

---

#### 595. What is the difference between GPU reset modes in amdgpu?

**问题描述 / Problem Description**:
Tags: linux, amd-graphics | Score: 1 | Views: 107 | Answers: 1 | Created: 2026-02-11

**解决方案 / Solution**:
Here's a link to the comment in amdgpu.h of the current master branch of the linux source that describes the amd_reset_method enum. It says /** * enum amd_reset_method - Methods for resetting AMD GPU devices * * @AMD_RESET_METHOD_NONE: The device will not be reset. * @AMD_RESET_LEGACY: Method reserved for SI, CIK and VI ASICs. * @AMD_RESET_MODE0: Reset the entire ASIC. Not currently available for the * any device. * @AMD_RESET_MODE1: Resets all IP blocks on the ASIC (SDMA, GFX, VCN, etc.) * individually. Suitable only for some discrete GPU, not * available for all ASICs. * @AMD_RESET_MODE2: Resets a lesser level of IPs compared to MODE1. Which IPs * are reset depends on the ASIC. Notably doesn't reset IPs * shared with the CPU on APUs or the memory controllers (so * VRAM is not lost). Not available on all ASICs. * @AMD_RESET_LINK: Triggers SW-UP link reset on other GPUs * @AMD_RESET_BACO: BACO (Bus Alive, Chip Off) method powers off and on the card * but without powering off the PCI bus. Suitable only for * discrete GPUs. * @AMD_RESET_PCI: Does a full bus reset using core Linux subsystem PCI reset * and does a secondary bus reset or FLR, depending on what the * underlying hardware supports. * * Methods available for AMD GPU driver for resetting the device. Not all * methods are suitable for every device. User can override the method using * module parameter `reset_method`. */

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804404/what-is-the-difference-between-gpu-reset-modes-in-amdgpu

---

#### 596. live-build - How to remove the superfluous /boot directory from the squashFS?

**问题描述 / Problem Description**:
Tags: debian, initrd, live-build | Score: 1 | Views: 131 | Answers: 2 | Created: 2026-02-11

**解决方案 / Solution**:
To omit files in chroot from the resulting filesystem.squashfs create the file config/rootfs/excludes and list files there (each file name on separate line): bor@ThinkPad-E16-Gen3:~/tmp/lb$ cat config/binary_rootfs/excludes boot/initrd.img boot/initrd.img-6.8.0-100-generic boot/initrd.img.old boot/vmlinuz boot/vmlinuz-6.8.0-100-generic boot/vmlinuz.old bor@ThinkPad-E16-Gen3:~/tmp/lb$ The live-build scripts call mksquashfs with -wildcards option, so you can also use wildcards, see mksquashfs documentation. EDIT: In the past the exclude file was called config/binary_rootfs/excludes and some Debian derivatives may include versions still using this name. According to GIT log, the change happened in the version 3.0.0 and e.g. Ubuntu 24.04 still has 3.0~a57 . Of course, alternative is to add chroot hook script that can do anything and remove any file you want form the root filesystem before live-build will pack it into SquashFS. live-build comes with a couple of examples, one of them removes some packages to free up space.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804389/live-build-how-to-remove-the-superfluous-boot-directory-from-the-squashfs

---

#### 597. Connecting Joy-Con 2 Controllers to Debian via Bluetooth

**问题描述 / Problem Description**:
Tags: debian, bluetooth | Score: 1 | Views: 664 | Answers: 1 | Created: 2026-02-10

**解决方案 / Solution**:
Joy-Con You can connect the Joy-Cons via Bluetooth on Debian. Enable Bluetooth (BlueZ), put the Joy-Con into pairing mode (Sync button), and pair it using bluetoothctl. Also check out the hid-nintendo , kms-hid-nintendo driver or the joycond tool. After that, most emulators should work without any problems. On Windows, I paired and used Joy-Cons and PS4 controllers with DS4Windows, see if there’s a similar solution available on Linux. emilyst / hid-nx-dkms nicman23 / dkms-hid-nintendo DanielOgorchock / joycond Using Nintendo Switch controllers on Linux Nintendo Joy-Con, NSO, and Pro Controller support Using Nintendo Switch controllers on Linux Joy-Con 2 So it’s still in development, but it seems that a solution will be available soon. Check the various posts about manual udev rules or the Steam Beta 2. As soon as a final solution for Debian is available, I will update the answer. An official driver for the Linux kernel is currently in the review phase. Without it, they are often recognized only as generic input devices. Features such as HD Rumble or the full combination of both Joy-Cons into a single controller pair only work reliably under Debian once the next version of the hid-nintendo driver is included in the kernel. Device init and polling works, but I haven't translated the packets yet since the public code doesn't line up with the automatic mappings and I'm intentionally avoiding doing any further reverse engineering myself. Happy to add patches to get this PR working though! udev rule for Linux: SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTRS{idVendor}=="057e", ATTRS{idProduct}=="2073", MODE="0666" CC @Nohzockt: If you have a preferred name/email for Co-authored-by I'll apply it to the patch that implements the init/polling work. Switch 2 Controller Support #13327 As far as I can tell, they are actively working on it. Review Switch2 linux Kernel Any Switch 2 Pro Controller support on linux yet? I've really been enjoying my Switch 2 Pro Controller and wanted to use it on steam but it doesn't seem to have good support right now. < Apperently Steam added support for it in the steam beta via a USB connection but I haven't been able to get it working other than using ProCon2. Has anyone else got it working? Or is it just a windows feature right now. I'm on Debian 13 if thats useful SOLVED: First apply udev rules in terminal: sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"057e\", ATTR{idProduct}==\"2069\", MODE=\"0666\"" > /etc/udev/rules.d/99-nintendo-pro-controller.rules' sudo udevadm control --reload-rules sudo udevadm trigger Then in terminal launch steam with -enablepro2 or steam -enablepro2 option, You must be on the steam beta for it to work at the moment as of December 27th, 2025. Any Switch 2 Pro Controller support on linux yet? Steam Beta It looks like the currently simplest way is through the Steam Beta. Valve has already added initial udev rules and support for the Joy-Con 2 and the Switch 2 Pro Controller. Valve temporarily disabled support for the Pro 2 and Joy-Con 2 in December 2025 due to crashes. Currently, you need to use the launch parameter -enablepro2 in the Steam beta so that inputs are processed correctly. If you’re using the Joy-Con 2 with emulators, set the API to SDL2 in the settings (e.g., Ryujinx or Cemu), as this is the most stable interface for the new Nintendo controllers on Debian. It seems as though Nintendo Switch 2 Pro Controller support has been temporarily disabled on all versions of SteamOS and the Steam Client as of today, December 24th, 2025. I just received one as a Christmas present, as was looking forward to using it, and now have found that it's useless until an update comes out. Not even the beta branches allow use of this feature. I understand that it was causing crashes with other controllers, but I'd like to accept the risks to be able to use my new controller. It seems that the Stable branch was updated to disable this on December 19th, and the Beta branch was updated on December 24th to disable this feature. I am unable to switch to the Preview branch on Steam Deck to check if that would change anything, due to another issue that's already been listed on this GitHub. Nintendo Switch 2 Pro Controller Support #12585 Steam Beta Update Adds Switch 2 Controller Support with New Gyro Defaults How To Use Nintendo Switch 2 Pro Controller on Steam (PC Setup Guide) The Steam Client Beta has been updated with the following changes: Note: This update was re-released December 28th to fix a Steam client crash on macOS and Linux when playing some games. Steam Input Add launch option to conditionally enable Nintendo Switch 2 and GameCube adapter support. To use, launch Steam with the -enablepro2 option. Steam Client Beta - December 26th They have just updated it. You can enable the pro controller by launching steam client through a terminal with -enablepro2 as a option Switch 2 Pro Controller not connecting to steam.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804363/connecting-joy-con-2-controllers-to-debian-via-bluetooth

---

#### 598. SSH 8.9 disables ssh-rsa but breaks connections to Cisco routers

**问题描述 / Problem Description**:
Tags: ubuntu, openssh | Score: 1 | Views: 85 | Answers: 1 | Created: 2026-02-05

**解决方案 / Solution**:
sshd.conf is the wrong file, it seems you edited the config file for the ssh daemon , not the ssh client (although the actual filename for that is /etc/ssh/sshd_config not sshd.conf in some unspecified directory). You need to edit the config for the ssh client , e.g. either /etc/ssh/ssh_config (global, for all users) or ~/.ssh/config (for the user running the ssh client). BTW, it would be best to add Host entries to change the encryption algorithms for your cisco routers ONLY rather than as the default for all hosts. Also worth noting, 8.9 is not the latest version of ssh. That's from February 2022. The most recent version is 10.2p1 from October 2025.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804282/ssh-8-9-disables-ssh-rsa-but-breaks-connections-to-cisco-routers

---

#### 599. What calls mkinitramfs on Debian on a kernel upgrade?

**问题描述 / Problem Description**:
Tags: debian, initramfs | Score: 1 | Views: 79 | Answers: 1 | Created: 2026-02-05

**解决方案 / Solution**:
When you update the Linux kernel on Debian GNU/Linux, the postinst script of the new linux-image-<version>-<arch> package (with possible variants) generally pulled as a dependency of a new version of the linux-image-<arch> package calls: linux-run-hooks image postinst $version $image_path -- "$@" This call to /usr/bin/linux-run-hooks is a shorthand to call all the "hooks" in /etc/kernel/postinst.d/ . One of those hooks, if the initramfs-tools package (as opposed to the dracut or tiny-initramfs alternatives) is installed, /etc/kernel/postinst.d/initramfs-tools calls update-initramfs -c -k "${version}" ${bootopt} >&2 And, /usr/sbin/update-initramfs is a shell script which calls mkinitramfs in its generate_initramfs() .

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804270/what-calls-mkinitramfs-on-debian-on-a-kernel-upgrade

---

#### 600. Trouble installing software through terminal on Debian

**问题描述 / Problem Description**:
Tags: debian, terminal, apt, software-installation, command-not-found | Score: 1 | Views: 305 | Answers: 3 | Created: 2026-02-03

**解决方案 / Solution**:
To replicate the behaviour you see on Ubuntu etc., you need to install command-not-found : sudo apt install command-not-found Then restart your shell, and you’ll get information about packages providing missing commands (if any) when you try to run them. Even without that, you can install packages, as you noticed for Wine. The difficulty is finding the package name; to do that, you can either search package descriptions using apt search , or install apt-file and search package contents. As the other answers explain, neofetch isn’t available in Debian.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804203/trouble-installing-software-through-terminal-on-debian

---

#### 601. How Insecure is allow-discards on LUKS

**问题描述 / Problem Description**:
Tags: linux, security, encryption, luks | Score: 1 | Views: 130 | Answers: 1 | Created: 2026-01-31

**解决方案 / Solution**:
Discard commands the drive that certain blocks are free and can be erased. Even if the OS encrypts the volume, the size and offsets of erased blocks could provide hints as to how much data is stored and what the file system type could be. Let us assume someone wants to recover a LUKS encrypted drive, for your benefit or theirs. And they can get professional data recovery services. At a minimum, I would expect recovery to have access to low level reads that allow access to blocks that have been discarded but not yet erased. For data that was only written to the encrypted volume, it should not be readable without the secrets. Discarding the blocks is not security critical, the cipher text is unreadable anyway because of LUKS. Even though TRIM doesn't guarantee the data is gone to even regular reads, unless the drive supports some kind of Deterministic read ZEROs after TRIM feature. If most of a physical drive has been discarded, the file system on top is presumably empty space, and the drive can start erasing. Recovery will be very difficult, or there was little data stored on it to begin with. For a lot of people, revealing this with discard on is not a big deal. An attacker knows a LUKS volume is half empty but may have say an ext4 file system given some block sizes and offsets. But without the key its modern encryption and is not likely to be cracked. Worth appreciating that there may be people with far more stringent security requirements that don't want even this revealed, even if that is not you. Of course without disk encryption, LUKS in this case, writes leave plain text blocks everywhere. Discarding blocks will eventually be deleted, but unclear as to when the drive will actually erase them. Before disposing of or encrypting a drive with unencrypted data on it, consider a secure erase command.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804143/how-insecure-is-allow-discards-on-luks

---

#### 602. Why does "seq 1000000 | tee /dev/stdout" produce more single-digit numbers than expected?

**问题描述 / Problem Description**:
Tags: linux, bash, stdout, tee, seq | Score: 15 | Views: 1693 | Answers: 2 | Created: 2025-10-08

**解决方案 / Solution**:
Having both of tee's outputs going to the same pipe creates tearing within lines because they don't start/end at the boundaries of read/write blocks.

tee, reads its input and writes its output by blocks of usually some amount of bytes that is a power of 2, though could read and write fewer if that's all there was to read from the pipe on its stdin at a given time.
Here:
$ seq 10000 | strace -e read,write tee /dev/stdout | cat > /dev/null
read(0, "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14"..., 8192) = 8192
write(1, "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14"..., 8192) = 8192
write(3, "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14"..., 8192) = 8192
read(0, "\n1861\n1862\n1863\n1864\n1865\n1866\n1"..., 8192) = 8192
write(1, "\n1861\n1862\n1863\n1864\n1865\n1866\n1"..., 8192) = 8192
write(3, "\n1861\n1862\n1863\n1864\n1865\n1866\n1"..., 8192) = 8192
read(0, "499\n3500\n3501\n3502\n3503\n3504\n350"..., 8192) = 8192
write(1, "499\n3500\n3501\n3502\n3503\n3504\n350"..., 8192) = 8192
write(3, "499\n3500\n3501\n3502\n3503\n3504\n350"..., 8192) = 8192
read(0, "7\n5138\n5139\n5140\n5141\n5142\n5143\n"..., 8192) = 8192
write(1, "7\n5138\n5139\n5140\n5141\n5142\n5143\n"..., 8192) = 8192
write(3, "7\n5138\n5139\n5140\n5141\n5142\n5143\n"..., 8192) = 8192
read(0, "6776\n6777\n6778\n6779\n6780\n6781\n67"..., 8192) = 8192
write(1, "6776\n6777\n6778\n6779\n6780\n6781\n67"..., 8192) = 8192
write(3, "6776\n6777\n6778\n6779\n6780\n6781\n67"..., 8192) = 8192
read(0, "14\n8415\n8416\n8417\n8418\n8419\n8420"..., 8192) = 7934
write(1, "14\n8415\n8416\n8417\n8418\n8419\n8420"..., 7934) = 7934
write(3, "14\n8415\n8416\n8417\n8418\n8419\n8420"..., 7934) = 7934

Where fd 1 is stdout (the pipe to cat > /dev/null) and fd 3 the one opened on /dev/stdout, which in this particular case of stdout being a pipe is equivalent to being a duplicate of fd 1¹
Here, you can see it making read()s and write()s of 8KiB. The second block ended in ...3498\n3 which you can infer from the third starting with 499\n3500....
It outputs it twice which means you get \n1861\n1862...3498\n3\n1861\n1862...3498\n3, and thus a line containing 3 between those 2 blocks even though that's for numbers ranging from 1861 to 6776.
You could avoid that if you could convince tee to output one line at a time on each of those fds, but I find that using stdbuf -oL (which injects code into applications to change stdio buffering) doesn't work for GNU tee at least (presumably because it doesn't use stdio for output), and GNU tee has no equivalent of GNU grep's --line-buffered option.
To force line-based output, you could replace seq which something that outputs one line at a time and does it slowly enough that tee would read() them one at a time.
A shell loop might be enough:
i=0
while [ "$i" -lt 10000 ]; do
  /bin/echo "$(( i += 1 ))"
done | tee /dev/stdout | grep -x .

Does it for me, where running the external echo command in a separate process for each line slows it down enough that I see:
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9

If I strace tee, I see:
read(0, "1\n2\n3\n", 8192)              = 6
write(1, "1\n2\n3\n", 6)                = 6
write(3, "1\n2\n3\n", 6)                = 6
read(0, "4\n", 8192)                    = 2
write(1, "4\n", 2)                      = 2
write(3, "4\n", 2)                      = 2
read(0, "5\n", 8192)                    = 2
write(1, "5\n", 2)                      = 2
write(3, "5\n", 2)                      = 2
read(0, "6\n", 8192)                    = 2
write(1, "6\n", 2)                      = 2

It did read 3 lines at once the first time (it took it more time to get to the point of doing the first read() than it took for the shell to run 3 echos), but then subsequent read()s read one line at a time.
Though if it's just about duplicating each line of the input, you can just use sed p instead.
Making sure that all lines have the same size (including the line delimiter) that is a power of 2 (like with seq -f %07g 10000) would also reduce the risk of any being broken in the middle at a block boundary.
$ seq -f %07g 10000 | tee /dev/stdout | grep  '000000[0-9]' | sort | uniq -c
      2 0000001
      2 0000002
      2 0000003
      2 0000004
      2 0000005
      2 0000006
      2 0000007
      2 0000008
      2 0000009


¹ but in general isn't on Cygwin or systems using Linux as their kernel where opening /dev/stdout is not like doing a dup(1) like it is on other systems.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800331/why-does-seq-1000000-tee-dev-stdout-produce-more-single-digit-numbers-than

---

#### 603. How can I make sudo apt install warn me that I'm about to pull from Debian Unstable?

**问题描述 / Problem Description**:
Tags: debian, apt, virtualbox | Score: 10 | Views: 735 | Answers: 3 | Created: 2025-12-27

**解决方案 / Solution**:
Pin unstable to a negative priority, which will prevent apt from installing anything from that source unless manually overridden with -t.
It would be interesting to review the output of apt-cache policy virtualbox to see if your pinning configuration is correct.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803343/how-can-i-make-sudo-apt-install-warn-me-that-im-about-to-pull-from-debian-unsta

---

#### 604. Which Linux file system should I use for compatibility with Windows programs?

**问题描述 / Problem Description**:
Tags: linux, filesystems, ext4, ntfs | Score: 9 | Views: 2295 | Answers: 2 | Created: 2025-10-31

**解决方案 / Solution**:
I suspect the tool that you need on your Linux-based server will be "Samba", which presents part(s) of the filesystem as Windows SMB Network Shares. Do not be tempted to share /, but instead take a section of the filesystem and share that.
In my experience Samba works best (reliability, efficiency) when underpinned by a native Linux filesystem rather than NTFS.
If your Windows applications can work with files being saved to a Windows SMB Network filesystem they will work with Samba, and therefore can be saved on your Linux-based system. This is the decision that underpins the whole migration process, so it's important that you satisfy yourself that your applications can work in this way (most can, but I've encountered a few - particularly in the professional Language Translation segment - that cannot).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800919/which-linux-file-system-should-i-use-for-compatibility-with-windows-programs

---

#### 605. How do I add a text editor to my (debian-based) initramfs?

**问题描述 / Problem Description**:
Tags: debian, initramfs, debugging | Score: 7 | Views: 475 | Answers: 1 | Created: 2025-12-05

**解决方案 / Solution**:
Debian-based distributions including Ubuntu and Mint use initramfs-tools to generate their initramfs'es. To add an executable such as nano and some terminfo database entries, place the following script in /etc/initramfs-tools/hooks/nano.sh:
#!/bin/sh    
# See `man initramfs-tools` for details

PREREQ=""
prereqs()
{
        echo "$PREREQ"
}
case $1 in
prereqs)
        prereqs
        exit 0
        ;;
esac
. /usr/share/initramfs-tools/hook-functions

# Begin real processing below this line
copy_exec /usr/bin/nano /usr/bin/nano

# copy_exec includes library dependencies, but not the terminfo database, so we need to add that manually
# The "terminfo_db" argument is just for logging.
# These entries are just the most common ones, with vt220 as fallback. See the $TERM
# variable (in the terminal where your initramfs runs in, which is usually not an xterm).
copy_file terminfo_db /usr/share/terminfo/x/xterm-256color
copy_file terminfo_db /usr/share/terminfo/x/xterm
copy_file terminfo_db /usr/share/terminfo/l/linux
copy_file terminfo_db /usr/share/terminfo/v/vt220

Make the script executable:
sudo chmod +x /etc/initramfs-tools/hooks/nano.sh

And rebuild your initramfs:
sudo update-initramfs -u

nano and most other terminal-based editors need a terminfo database with the right description of your terminal. In the above hook script I've added the most common ones, and vt220 is a fallback with which most terminals are compatible. If your editor complains about not being able to open your terminal, print the TERM environment variable: echo $TERM, and add the matching terminfo entry to the hook script. Note that you need to check the TERM in the actual terminal the initramfs runs in, that is usually not the xterm on your desktop. Usually this will be the Linux framebuffer which has linux  as $TERM.
To add any other executable to the initramfs, change the line with copy_exec in the hook script to point to it. The copy_exec helper function automatically includes any necessary libraries.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801855/how-do-i-add-a-text-editor-to-my-debian-based-initramfs

---

#### 606. after Debian 13 upgrade sshd not starting after reboot

**问题描述 / Problem Description**:
Tags: debian, sshd, ipv6 | Score: 6 | Views: 913 | Answers: 3 | Created: 2025-12-24

**解决方案 / Solution**:
Unless specified otherwise, all services under systemd start in parallel. On Debian, 'ssh.service' has After=network.target and ifupdown's 'ifup@.service' has Before=network.target… but those are "passive" parameters which only become effective if 'network.target' is already part of the whole boot process, i.e. something needs to actively depend on 'network.target' using Wants=.
It seems to me that neither sshd nor ifupdown have such a dependency, and as a result, both processes are run in parallel. Since IPv6 address configuration is not instant due to mandatory Duplicate Address Detection, it always takes longer for ifupdown to configure the interface than it takes for sshd to run.
(By convention, the network "provider" like ifupdown is the side that should have both Before + Wants for network.target, while the "consumer" like sshd should only need After.)
You have several options:

Bind to :: instead. This covers all IPv6 addresses, current and future.
ListenAddress ::

I would generally choose this option, as binding to a specific address does not actually mean incoming connections will be limited to only through that interface, i.e. it is not very effective at all as a security measure. (That is to say, you'd need iptables/nft rules to make it work – and once you have iptables/nft rules, you don't need the specific ListenAddress anymore.)

Use "socket activation" with ssh.socket. This takes over socket configuration from sshd, but it can have the additional option FreeBind= which allows it to bind to not-yet-available local addresses.
systemctl edit --full ssh.socket
  [Socket]
  ListenStream=[2XXX:XXXX:0:10a::1]:22
  FreeBind=true
systemctl enable ssh.socket


Add a dependency Wants=network.target to ifup@.service + networking.service so that the .target will be able to do its job as a barrier.
systemctl add-wants ifup@.service network.target
systemctl add-wants networking.service network.target


Add a direct dependency on ifupdown to ssh.service, as it indeed depends on ifupdown having done its job:
Edit: I had forgotten that systemctl add-wants doesn't imply After unless the first unit is a target. For the previous suggestion with network.target that is fine as the relevant units already have a Before or After for it. For this case however you need to define both Wants/Requires and Before/After, so systemctl edit is more suitable.
systemctl edit ssh.service
  [Unit]
  Requires=ifup@ens192.service
  After=ifup@ens192.service
  -or (see note)-
  Requires=networking.service
  After=networking.service


systemctl add-wants ssh.service ifup@ens192.service
-or (see note)-
systemctl add-wants ssh.service networking.service


Note: I don't remember whether auto interfaces are all handled by networking.service or whether they are split into ifup@ services. Check the active services on your system.
Note: If you use Requires=, then restarting networking will also restart sshd. In this case that might be useful. If you don't want that, use Wants=.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803277/after-debian-13-upgrade-sshd-not-starting-after-reboot

---

#### 607. Encrypted swap with FDE?

**问题描述 / Problem Description**:
Tags: debian, security, encryption, swap, disk-encryption | Score: 6 | Views: 708 | Answers: 3 | Created: 2025-12-17

**解决方案 / Solution**:
The Debian installation manual documents this, albeit indirectly. See the section on partitioning, in particular the section on guided partitioning. It says

When using LVM or encrypted LVM, the installer will create most partitions inside one big partition; the advantage of this method is that partitions inside this big partition can be resized relatively easily later. In the case of encrypted LVM the big partition will not be readable without knowing a special key phrase, thus providing extra security of your (personal) data.

and further down,

The other partitions, including the swap partition, will be created inside the LVM partition.

Your lsblk output confirms that you’re using LVM and that your swap partition is inside the encrypted LVM partition.
I don’t know how far back your “years ago” goes, but as far as I’m aware the above has always been true when using encrypted LVM.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803076/encrypted-swap-with-fde

---

#### 608. X11 forwarding cannot type single or double quotes

**问题描述 / Problem Description**:
Tags: debian, x11, windows, xforwarding | Score: 5 | Views: 440 | Answers: 1 | Created: 2025-12-30

**解决方案 / Solution**:
You're probably using a keyboard layout with dead keys which are used to type diacritics, the first key press is "dead" which means nothing will be shown, but the key will modify the character on the second key press, for example ^+e → ê. It has nothing to do with X11 or Windows. The " and ' dead keys are used to type umlaut and acute accent respectively, similar to how  ` is used for the grave accent
To solve this you have 2 ways

Change to keyboard layout to one that doesn't use dead keys. For example from US International to US

Or type space after the dead key if you have to use that layout. "+Space → ", and '+Space → '
When you press the dead keys twice many systems will interpret as "the user wants the accent mark itself" and give you ¨ or ´.


See also https://kbdlayout.info/features/deadkeys

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803391/x11-forwarding-cannot-type-single-or-double-quotes

---

#### 609. NVMe: Unable to change power state from D3cold to D0, device inaccessible

**问题描述 / Problem Description**:
Tags: linux, drivers, pci, nvme | Score: 5 | Views: 893 | Answers: 1 | Created: 2025-10-16

**解决方案 / Solution**:
I found a solution. By removing the device from the PCIe tree and then rescanning the bus, it comes back up:
root@rtrbox:~# lsblk
NAME              MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
loop0               7:0    0   4.1G  1 loop  /rtr/primary/squashfs/root
zram0             253:0    0  16.8G  0 disk  [SWAP]
root@rtrbox:~# rmmod nvme
root@rtrbox:~# rmmod nvme-core
root@rtrbox:~# echo 1 > /sys/devices/pci0000:00/0000:00:03.0/remove
root@rtrbox:~# echo 1 > /sys/bus/pci/rescan
root@rtrbox:~# lsblk
NAME              MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
loop0               7:0    0   4.1G  1 loop  /rtr/primary/squashfs/root
zram0             253:0    0  16.8G  0 disk  [SWAP]
nvme0n1           259:0    0 931.5G  0 disk
└─nvme0n1p1       259:1    0    64G  0 part

From the kernel logs:
[138759.380378] pci 0000:03:00.0: [144d:a80c] type 00 class 0x010802 PCIe Endpoint
[138759.381686] pci 0000:03:00.0: BAR 0 [mem 0xffffffffffffc000-0xffffffffffffffff 64bit]
[138759.382215] pci 0000:03:00.0: Max Payload Size set to 256 (was 16384, max 512)
[138759.383176] pci 0000:03:00.0: Adding to iommu group 15
[138759.383824] pcieport 0000:00:02.4: ASPM: current common clock configuration is inconsistent, reconfiguring
[138759.391544] pci 0000:03:00.0: BAR 0 [mem 0xfce00000-0xfce03fff 64bit]: assigned
[138759.392408] nvme 0000:03:00.0: platform quirk: setting simple suspend
[138759.393216] nvme nvme0: pci function 0000:03:00.0
[138759.395956] nvme nvme0: D3 entry latency set to 10 seconds
[138759.401342] nvme nvme0: 16/0/0 default/read/poll queues
[138759.407779]  nvme0n1: p1

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800501/nvme-unable-to-change-power-state-from-d3cold-to-d0-device-inaccessible

---

#### 610. Which Linux distributions bind TTYs to Control + Alt + F13 to F24 keys?

**问题描述 / Problem Description**:
Tags: linux, tty | Score: 5 | Views: 601 | Answers: 1 | Created: 2025-10-02

**解决方案 / Solution**:
In Linux, if the kernel supports VTs, they are allocated as necessary, up to the maximum number of supported VTs (MAX_NR_CONSOLES, which is 63). In most systems there is always at least one allocated VT.
So you’ll find a VT allocated for a given function key if something has caused one to be allocated! Your display server is capable of allocating VTs, as are various other tools including openvt. Function keys, with CtrlAlt, can be used to access VTs directly, up to at least F20, if there is a corresponding VT. On some systems you can also use CtrlAlt← and CtrlAlt→ to move from one VT to the next.
It is also possible to deallocate unused VTs, using deallocvt. The VT_OPENQRY ioctl gives the first available (unused) VT, but I’m not aware of a user program which gives that information — programs using that ioctl do so because they want to open a VT.
Linux distributions using sysvinit typically start gettys on the first six VTs; X or Wayland then get VT 7 and onwards, or in some setups, take over the VT they’re started from (with startx). This is configured in /etc/inittab. Distributions using systemd spawn gettys on demand on the first six VTs, but apart from VT 6, any unused VT can be requisitioned instead by a graphical display. Thus in a typical desktop setup with a display manager, VT 1 is used for the display manager (the component that displays the login screen), and VTs 2 and onwards are used for login sessions. Without a display manager, VT 1 is used for the first getty. This is configured in logind.conf (see in particular NAutoVTs= and ReserveVT=) and with the getty@ service.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800146/which-linux-distributions-bind-ttys-to-control-alt-f13-to-f24-keys

---

#### 611. Can someone explain this apparent btrfs confusion?

**问题描述 / Problem Description**:
Tags: debian, btrfs, snapshot, snapper, raspberry-pi-os | Score: 4 | Views: 504 | Answers: 2 | Created: 2025-12-22

**解决方案 / Solution**:
The output and path selection of btrfs subvolume list can be quite confusing. You might also be interested in this answer: https://unix.stackexchange.com/a/752374/573555
Relevant part for your question is, that an btrfs filesystem can have multiple independent directory hierarchies in the form of subvolume and is flexible in what is mounted as root fs. In contrast the path parameter to the list command is merely a selector for what filesystem to inspect.
You should also try the -a option as btrfs subvolume list -a /.
I'm not using snapper myself but in your case it is likely that one of the snapshots is mounted as rootfs. You can check what subvolume is mounted by default with btrfs subvolume get-default / and see what is currently mounted as root with findmnt -o SOURCE /.
For the second you will get the device path followed by square brackets which contain the subvolume path which is in your case most likely more than a single /.
So you can have a directory hierarchy outside your mounted root which btrfs list will show like regular paths but is not directly accessible through your mounted root fs.
As a side note you might be interested, that btrfs has an option to in-place convert an existing filesystem into btrfs. (as usual you should still have an backup of your files) https://btrfs.readthedocs.io/en/latest/Convert.html
Also at least one variant of the Debian installer also supports installing to btrfs directly.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803216/can-someone-explain-this-apparent-btrfs-confusion

---

#### 612. Hardware encryption on Samsung SSD using Debian

**问题描述 / Problem Description**:
Tags: linux, dual-boot, encryption, ssd | Score: 4 | Views: 935 | Answers: 1 | Created: 2025-11-12

**解决方案 / Solution**:
Set up debian installation with LVM and encryption.

That "encryption" there means software-side encryption :)
Which you can at least verify works; hardware encryption is the drive firmware telling "trust me bro, I've encrypted that safely" with no information on how it did that whatsoever. That goes about as well as you'd expect, i.e., not at all.
Oh, and usually these drives remain unlocked until their power is cut. Which practically means you need a diode and a supercapacitor to be put in your SSD's power supply lines (no protections against that on the hardware side), and then I have a couple of hours to days between the point where you think you've turned off your PC and when your drive cannot simply be removed and put in a different PC. This happening might not be within your threat model, but "attacker enters office and removes storage device or thief steals whole PC" is why I am encrypting my desktop SSDs.
So, you got the safe option there. I'm not sure whether you need anything else!

During installation, SSD gets written with random data.

Hm? no.
You could probably have done all this without the Samsung specific tools just by enabling hardware encryption; that stuff's standardized (imagine a datacenter person having to go and do what you do on the shipment of 10000 SSDs they just received. They'd just buy some other SSDs).
Your vendor tool seems to have enabled self-encryption capabilities (I bet it didn't need to do that, that's just really really standard these days, it just wanted you to take a backup, and helps you prepare a bootable stick to do the encryption dance, and didn't want to explain the finer parts of the procedure, but make sure that users follow a reproducible path). Then, it enabled locking (which is dangerous, and hence a separate step: locking and forgetting the key means your drive is toast; which is the point).
Quick check: Install sedutil and run
sudo sedutil-cli --isValidSED /dev/nvme0n1

(replace nvme0n1 with the device name (not partition name!) of your drive, check lsblk's top level entries if in doubt)
This should print the device name.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801276/hardware-encryption-on-samsung-ssd-using-debian

---

#### 613. Are there any options for the nmcli command that outputs the SSID of a wifi including, if present, trailing spaces?

**问题描述 / Problem Description**:
Tags: linux, wifi, nmcli | Score: 4 | Views: 416 | Answers: 3 | Created: 2025-10-08

**解决方案 / Solution**:
By this post I have found the option --get-value of the command nmcli. For an explanation of the option see the documentation of the command nmcli.
By this option I can specify what fields must be present in the output, and each field value is separated from the others by a colon character (':'). In this way, the command output shows the Wi-Fi network SSID complete with all leading and trailing spaces.
So the command nmcli can be used as showed below:
> nmcli --get-value SSID,SECURITY dev wifi list

An example of the output of the command is the followed (there are 2 columns SSID and SECURITY seprated by : char):
TPLINK-8853:WPA2
TPLINK-9910 :WPA2
GUESTS:
:WPA2 802.1X
...

The second line of the output is TPLINK-9910 :WPA2 and it is easy to get the SSID of the Wifi because it is located between the beginning of the line and the character :.
In the output the fourth line (:WPA2 802.1X) shows an hidden wifi network (the SSID is empty).
This method solve also the problem of the leading spaces.

EDIT
As suggested by @Hans-Martin Mosner It is necessary to handle the case where the : character is contained in the SSID.
On my project the output of the nmcli command is processed by a script Python so by the split(':') method it is not difficult to get the SSID containing the character : possibly present.
Thank you to all

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800304/are-there-any-options-for-the-nmcli-command-that-outputs-the-ssid-of-a-wifi-incl

---

#### 614. How can I find common prefixes in file names to group them?

**问题描述 / Problem Description**:
Tags: linux, bash, text-processing, find, filenames | Score: 4 | Views: 561 | Answers: 4 | Created: 2025-10-07

**解决方案 / Solution**:
With perl:
$ find . -print0 | perl -C -l -0ne '
  if (m{/([^/]{4,}?\w)\b[^/]*\z}) {
    push @{$list{$1}}, $_;
  }
  END {
    while (($part, $list) = each(%list)) {
      if (($count = @$list) > 1) {
        print "There are $count files with \"$part\" in common at the start:";
        print " - \"$_\"" for @$list;
        print "";
      }
    }
  }'
There are 2 files with "small" in common at the start:
 - "./subdir/small picture.jpg"
 - "./small video.mp4"

There are 2 files with "very big" in common at the start:
 - "./very big picture.jpg"
 - "./subdir/very big video.mkv"


Where [^/]{4,}?\w\b matches at least 4 non-/ characters, as few as possible followed by a word character (alnum or underscore) followed by a word boundary (here same as (?!\w)), so a list of at least 5 characters ending in a delimited word.
In this case, that \w also matches on underscore (and \b matches boundary of such words) is unfortunate as it's common to separate words in filenames with underscore. You could however change it to: m{/([^/]{4,}?[[:alnum:]])(?![[:alnum:]])[^/]*\z} to work around it.
To match on the first two words instead of 1 or more words making up at least 5 characters, use:
m{/([^\w/]*\w+[^\w/]+\w+)[^/]*\z}

Or excluding _ from the definition of word:
m{/([^[:alnum:]/]*[[:alnum:]]+[^[:alnum:]/]+[[:alnum:]]+)[^/]*\z}

Add ! -type d before -print0 to exclude files of type directory, or ! -xtype d (assuming GNU find) to also exclude symlinks to directories, or -type f for regular files only or -xtype f to also include symlinks to regular files.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800287/how-can-i-find-common-prefixes-in-file-names-to-group-them

---

#### 615. How can I list all supported architectures of a package by apt command?

**问题描述 / Problem Description**:
Tags: ubuntu, apt, architecture | Score: 4 | Views: 1359 | Answers: 2 | Created: 2025-05-12

**解决方案 / Solution**:
With a few exceptions (apt update of course, and in recent years apt changelog), apt only operates on information available locally (local copies of repository catalogs, which are published separately for each architecture). To limit the amount of information it needs to download and process, apt only retrieves repository indexes for architectures dpkg cares about: the system’s main architecture and any foreign architectures that have been enabled. So the only way to determine all the architectures a given package is available for, using only apt, is to enable all architectures (with dpkg --add-architecture, then apt update). Then apt list will show all available architectures:
$ apt list stress-ng
stress-ng/noble 0.17.06-1build1 amd64
stress-ng/noble 0.17.06-1build1 arm64
stress-ng/noble 0.17.06-1build1 armhf
stress-ng/noble 0.17.06-1build1 ppc64el
stress-ng/noble 0.17.06-1build1 riscv64
stress-ng/noble 0.17.06-1build1 s390x

In any case, if you want to use apt download for a given architecture, you need to enable that architecture.
A simpler option is to use rmadison from the devscripts package:
$ sudo apt install --no-install-recommends devscripts
[…]
$ rmadison stress-ng
 stress-ng | 0.03.15-1~ubuntu14.04.1 | trusty-backports/universe | source, amd64, arm64, armhf, i386, powerpc, ppc64el
 stress-ng | 0.05.23-1               | xenial/universe           | source, amd64, arm64, armhf, i386, powerpc, ppc64el, s390x
 stress-ng | 0.05.23-1ubuntu2        | xenial-updates/universe   | source, amd64, arm64, armhf, i386, powerpc, ppc64el, s390x
 stress-ng | 0.09.25-1               | bionic/universe           | source, amd64, arm64, armhf, i386, ppc64el, s390x
 stress-ng | 0.09.25-1ubuntu9        | bionic-updates/universe   | source, amd64, arm64, armhf, i386, ppc64el, s390x
 stress-ng | 0.11.07-1               | focal/universe            | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.11.07-1ubuntu2        | focal-updates/universe    | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.13.12-2               | jammy/universe            | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.13.12-2ubuntu1        | jammy-updates/universe    | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.17.06-1build1         | noble/universe            | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.18.04-1               | oracular/universe         | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.18.11-1               | plucky/universe           | source, amd64, arm64, armhf, ppc64el, riscv64, s390x
 stress-ng | 0.19.00-1               | questing/universe         | source, amd64, arm64, armhf, ppc64el, riscv64, s390x

**参考链接 / References**:
- https://unix.stackexchange.com/questions/794756/how-can-i-list-all-supported-architectures-of-a-package-by-apt-command

---

#### 616. Deleted all partitions in a drive, now the drive won't show up in Dolphin

**问题描述 / Problem Description**:
Tags: debian, partition, kde, dolphin | Score: 3 | Views: 611 | Answers: 1 | Created: 2025-12-24

**解决方案 / Solution**:
how to access the drive to create the partition, since it doesn't show up anymore in Dolphin

Use the "KDE Partition Manager" program that's in your screenshot. It's available in the KDE application list. It might also be named partitionmanager. Open the program and select the device, then add a maximum size partition. Probably choose "ext4" or "btrfs" as the filesystem.
There are many other partitioning tools, such as GParted, gnome-disks, or fdisk. Some of them will offer to make a filesystem within the newly created partition, others (like fdisk) require you to separately use mkfs.<type> (mkfs.ext4, mkfs.btrfs, etc) to do so.
Meanwhile Dolphin is ultimately a file manager so it only shows partitions that contain a recognized filesystem – it doesn't really care about disks in themselves. (Which isn't any different from Windows, where Explorer also won't show an unpartitioned disk; you'd have to open DiskMgmt to create a partition first.)
(As a side note, it's technically possible to just directly format (mkfs) an unpartitioned disk, but in most cases I would not recommend doing so. It can make sense for virtual machines, but no advantage in doing that for a physical HDD/SSD. Create a partition and let it take 100% of the unallocated space, and format that.)

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803290/deleted-all-partitions-in-a-drive-now-the-drive-wont-show-up-in-dolphin

---

#### 617. Syntax Error on ssed for Regex Subroutine definitions

**问题描述 / Problem Description**:
Tags: linux, sed, regular-expression, perl, pcre | Score: 3 | Views: 229 | Answers: 2 | Created: 2025-10-26

**解决方案 / Solution**:
tl;dr: Forget about ssed. Use perl.
Here's why:

ssed is abandonware.  It was last updated in Oct 2005.  Its home page on sourceforge is gone (and I can't find any replacement on github or gitlab).
Various distros have kept on packaging it and making minor patches (mostly packaging related or to ensure it actually compiles with modern libraries & tools), but the program itself hasn't been updated for 20 years.

ssed doesn't use perl regular expressions, it uses Perl Compatible Regular Expressions (PCRE) which are based on and very similar to perl REs but have some significant differences.

It doesn't even use a recent version of PCRE.  The ssed source code bundles an ancient version of PCRE from August 2000.  It can't use any perlre features implemented since around that time, so you'll have to find and install an ancient copy of the perlre and related man pages if you want documentation (but don't forget that ancient PCRE wasn't 100% compatible with ancient perlre either).

If you can install and use an ancient abandoned software package from 20 years ago to do perlish sed search & replace operations, there's no reason you can't use perl for the same tasks (but note that anything that uses other sed language features like branching, conditionals, hold space, append, insert, delete, etc will have to be re-written to use perl equivalents.  This isn't terribly difficult.  If all you use ssed for is s/// operations then they'll work without a problem).
If you have lots of scripts which use ssed and don't want to have to edit them, write a wrapper script (e.g. /usr/local/bin/ssed) that first processes all options to:

Remove or replace any ssed options that are incompatible with perl (-l/--line-length, -r/--regexp-extended, -R/--regexp-perl, --posix, -s/--separate and -u/--unbuffered need attention).

-r, -R, and --posix aren't needed and can just be removed from the args

-l is incompatible with perl's -l option (which turns on automatic handling of line-endings, e.g. \n).  Either remove it from the args or get used to it having the perl meaning.  If you need to limit the line length, then pipe the output into fmt or fold or par to re-format it. Or add a rule like s/(^.{80}).*/$1/; or $_ = substr($_,0,79); to remove excess characters from each input line.

-u is unlikely to be needed. If you really need unbuffered output for some reason, add something like BEGIN { $| = 1 }; to the beginning of your ssed-but-really-perl script. See $| in perldoc perlvar

-s is the only ssed option that presents any difficulty.  Perl's -n and -p options treat all input as a single continuous stream unless you're using -i (in which case, it edits each file individually).
If you need to emulate --separate for other purposes, it's probably easiest to just write a perl one-liner without using either -n or -p but with its own while (<<>>) { ... } loop and a continue { if eof { do something here }; ... } block for that loop.
There are many possible uses for and things you can do in a continue block, but the main reason I ever use one is to reset perl's input line counter variable ($. - see $. in perldoc perlvar) after each file by close-ing the current file when it reaches eof, e.g. while (<<>>) { ... } continue { close ARGV if eof };.   See perldoc -f continue



Execute perl with either -n or -p depending on how ssed was called, and pass all other args on to perl.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800772/syntax-error-on-ssed-for-regex-subroutine-definitions

---

#### 618. What is the best way to detect busy CPU cores for blk-mq request steering in Linux kernel?

**问题描述 / Problem Description**:
Tags: linux, filesystems, linux-kernel, io, storage | Score: 3 | Views: 91 | Answers: 1 | Created: 2025-10-16

**解决方案 / Solution**:
Disclaimer: I am not familiar with this kind of problem.
It seems that the number of I/O requests per CPU core is not the only influence on I/O perfomance. Having more on the same core may be advantageous up to some point (cache hits).
Another influence is the overall load of that core. There is no point in having fewer I/O requests on a core if these have to wait longer for being processed on a core with high load.
You could assign all I/O to just one core (unless you really need several hardware queues for the full device performance) and use this core mainly for I/O (block it for userspace processes). Or add the overall load of the cores to your assignment algorithm. Of course, checking this must be very quick.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800527/what-is-the-best-way-to-detect-busy-cpu-cores-for-blk-mq-request-steering-in-lin

---

#### 619. How do I autosource path and venvs in /bin/sh (posix sh) for docker pods

**问题描述 / Problem Description**:
Tags: ubuntu, shell, docker | Score: 3 | Views: 222 | Answers: 2 | Created: 2025-07-01

**解决方案 / Solution**:
I've added the source to ~$HOME/.profile but it does not autorun.

you probably mean $HOME/.profile. That is never autorun. It is read by your shell when you start an interactive login shell.
You don't start a login shell, but simply a shell.
multiple approaches here:

if you just want environment variables to be set for any process you launch the container with (not only /bin/sh, but also python, which seems to be what you actually need), then use the ENV directive in your Dockerfile. This is very likely the correct thing to do.
if you want sh to act as if it was a login shell, append  --login to your /bin/sh invocation.
if you want to specify an arbitrary file to be sourced at shell initializtation, add  --rcfile /path/to/file -i to /bin/sh.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/797577/how-do-i-autosource-path-and-venvs-in-bin-sh-posix-sh-for-docker-pods

---

#### 620. unattended-upgrades uses wrong hostname after switching from msmtp to Postfix

**问题描述 / Problem Description**:
Tags: ubuntu, postfix, unattended-upgrades | Score: 3 | Views: 174 | Answers: 1 | Created: 2025-05-05

**解决方案 / Solution**:
Found the answer after reading this answer to a similar question: I recently created reverse DNS entries for the server, which contained the base domain, and Python's socket.getfqdn() function used these instead of the hostname configured locally.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/794523/unattended-upgrades-uses-wrong-hostname-after-switching-from-msmtp-to-postfix

---

#### 621. What out-of-the-box options exist for quickly shutting down KDE Plasma, using only the keyboard?

**问题描述 / Problem Description**:
Tags: debian, kde, keyboard-shortcuts, shutdown, plasma | Score: 2 | Views: 1430 | Answers: 5 | Created: 2025-12-26

**解决方案 / Solution**:
By default, CTRL + ALT + DEL brings up the How do you want to end your session popup?, from which point you can use the arrow keys and ENTER to select your option (which in this case is Shutdown).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803307/what-out-of-the-box-options-exist-for-quickly-shutting-down-kde-plasma-using-on

---

#### 622. LibreOffice looks old and ugly in Debian/KDE - how to make it use the proper dark breeze theme and look normal again?

**问题描述 / Problem Description**:
Tags: debian, kde, gui, theme, libreoffice | Score: 2 | Views: 577 | Answers: 1 | Created: 2025-12-10

**解决方案 / Solution**:
You most likely lack the appropriate QT integration package. Install libreoffice-kf6 if you are on Debian 13 or libreoffice-kf5 if you still use Debian 12. This problem likely happened because you installed a very minimal KDE installation. On my system I see that the libreoffice-kf6 package is installed through recommended packages of task-kde-desktop.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801955/libreoffice-looks-old-and-ugly-in-debian-kde-how-to-make-it-use-the-proper-dar

---

#### 623. Inadvertently installed texlive-base and texlive-binaries while a TeX Live installation is already present on my system

**问题描述 / Problem Description**:
Tags: debian, apt, latex | Score: 2 | Views: 252 | Answers: 2 | Created: 2025-11-26

**解决方案 / Solution**:
The xournalpp package does not Depend on or even Recommend either the texlive-base or texlive-binaries packages.  It only Suggests them.
Have you configured apt on your system to auto-install Suggested packages?  apt normally won't install Suggested packages.
Anyway, it should be safe to just remove the texlive packages, and you shouldn't need to remove xournalpp if you don't want to. e.g. with:
sudo apt purge texlive-base texlive-binaries

You may need to regenerate any .dvi, .pdf etc output files you've generated while the Debian texlive packages were installed....but probably not, it depends on your PATH and other environment variables (which I presume you had configured correctly for your /usr/local install of texlive)

If you want to prevent the Debian texlive packages from being auto-installed in future, you can use the equivs package to create a dummy package to satisfy package dependencies via Provides: lines. From the package description:

Description-en: Circumvent Debian package dependencies
This package provides a tool to create trivial Debian packages.
Typically these packages contain only dependency information, but they
can also include normal installed files like other packages do.
One use for this is to create a metapackage: a package whose sole
purpose is to declare dependencies and conflicts on other packages so
that these will be automatically installed, upgraded, or removed.
Another use is to circumvent dependency checking: by letting dpkg
think a particular package name and version is installed when it
isn't, you can work around bugs in other packages' dependencies.
(Please do still file such bugs, though.)


Alternatively, you might want to consider using the Debian packages and not bothering to install it yourself in /usr/local - but that really depends on your reason for doing that in the first place.
Unless you have a good reason (i.e. something more specific than just wanting the latest, shiniest version number without having a need or problem that's solved by a newer version), that's what I'd recommend.
I'm not even remotely close to an expert with texlive (just a not-completely-incompetent amateur who can usually make it do what I want with some effort and a lot of RTFM-ing) but I do use it every so often to produce documentation. I've never run into any problem with the Debian packages that would make me consider compiling and installing it myself.  Or using a non-packaged version of it.  Which is a fancy way of saying "It works for me".  YMMV.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/801618/inadvertently-installed-texlive-base-and-texlive-binaries-while-a-tex-live-insta

---

#### 624. Find laptop internal keyboard Controller model/vendor/Product #

**问题描述 / Problem Description**:
Tags: linux, keyboard, input | Score: 2 | Views: 182 | Answers: 2 | Created: 2025-10-20

**解决方案 / Solution**:
Is internal keyboard controller sitting on pci or usb bus?

No, as the anachronistic labeling as "i8042" (intel i8042, the keyboard controller of the IBM PC-AT, from 41 years ago) says, this is an emulated peripheral. It's almost certainly emulated by the "Advanced Integrated Peripheral", which on a laptop CPU might be part of a the CPU or one of its directly attached peripheral chips, I'm not too sure; I'd tend towards it being in the platform controller. In any case, no, it does not directly nor indirectly sit on USB, and at best indirectly reside within the PCI hierarchy (but probably not; these are the things that you addressed with special IO instructions directly from the CPU, and CPUs, forty years ago, had their own port just for this controller!). What might be the case is that your system's firmware has been told to emulate a PS/2 peripheral, and could be told to not do that and instead present the keyboard as USB device. Some laptops have such an option in their firmware setups. Look for "legacy OS support" or something and disable it.
Your output points to this being an ACPI-PnP-connected peripheral. That won't help you at all, because that just means status information is literally exchanged using the x86 inb operation; what that does internally to the CPU: not of Linux' concern. It just means it doesn't fall under the categories "PCI device" nor "attached to a USB bus (which typically is attached via a PCI device)" at all.
There's no specific driver code in Linux to drive that (emulated) keyboard controller; this is all quite standard.
Experience also tells me that the things that laptop keyboards do are often extremely quirky. I had to do with one acer laptop whose keyboard controller would send duplicate reports; that was solved in software in a acer-provided driver for windows (on a DVD, no less!); so you had a maximum typing speed for words with consecutive letters on this machine. So, I would not preemptively blame Linux here. The same driver works beautifully on thousands of other, standards-compliant keyboards.
Note that if you look into the Linux kernel's i8042-acpipnpio.h, you'll find a table with 157 entries for "i8042 implementation quirks". In other words, this is so very common for mainboard firmware suppliers to mess up (and frankly, i8042 is one of the least complex legacy peripherals), that there's 157 hotfixes in the Linux kernel for mainboards that just don't work with a correct implementation. Great!
Anyways, you ask how

to find internal keyboard controller model/vendor/Product

and that's easy: look up your laptop's platform controller and CPU. That's where the controller lives. It's not its own chip (and hasn't been for > 30 years).

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800614/find-laptop-internal-keyboard-controller-model-vendor-product

---

#### 625. How to forget running but canceled transactions in a btrfs recovery?

**问题描述 / Problem Description**:
Tags: linux, data-recovery, btrfs, journaling | Score: 2 | Views: 212 | Answers: 1 | Created: 2025-10-11

**解决方案 / Solution**:
To forget a running transaction in btrfs you need to need to zero the log.
To do so:
sudo btrfs rescue zero-log path/to/partition
From man pages:

zero-log: Clear the filesystem log tree.


This command will clear the filesystem log tree. This may fix a specific set of problem when the filesystem mount fails during log replay. See below for sample stack traces that may show up in system log.


NOTE:
Clearing the log may lead to loss of changes that were made since the last transaction commit. This may be up to 30 seconds (default commit period) or less if the commit was implied by other filesystem activity.

Note: Be sure to run this on a image of the damaged drive/partition!
Edit: based on new information
You could try try to rebalance the data block groups:

To rebalance data block groups which are less than 85% utilized, running the operation in the background:

sudo btrfs balance start --bg -dusage=85 <path_to_btrfs_fs>
This will free up the "eaten" space and you will have rebalanced the FS.  Also the disbalanced FS is more prone to data corruption.
You could also try to mount the broken btrfs FS (again, do that on a copy of the original FS)

mount -t btrfs -o recovery,nospace_cache,clear_cache <device> <mount point>

If it gives you a bad fs message you can try to do a restore

btrfs restore <device> <dir_to_dump_data_to>

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800394/how-to-forget-running-but-canceled-transactions-in-a-btrfs-recovery

---

#### 626. Tool to display DDR5 RAM SPD timings/MT profiles

**问题描述 / Problem Description**:
Tags: linux, software-rec, ram | Score: 2 | Views: 918 | Answers: 1 | Created: 2025-10-06

**解决方案 / Solution**:
To access the SPD timings, you'll first need the i2c bus driver for your chipset. For AMD Ryzen chipsets, it is (perhaps surprisingly) i2c-piix4.
Once that is loaded, the ee1004 module for DDR4 or spd5118 for DDR5 should automatically find the DIMM SPDs if they are using the usual i2c addresses for SPDs. (With DDR4, you'll need the additional jc42 module for memory temperature info if your memory modules have the sensor for it; with DDR5, the spd5118 will handle both the temperature and the SPD information.)
The Ryzen chipsets may also include a i2c-designware-platform i2c bus, but that is apparently not SMBus compliant and so not easily autoprobeable.
On DDR5 memory modules, the SPD data format differs from older memory types. As of this writing, the decode-dimms tool needs this patch set applied to it to interpret DDR5 SPDs.
To apply, create a work directory somewhere convenient, and move to it.
Then, download the patches in text form. For some reason, the raw links in that mail archive output each mail twice (with & without full headers), so a bit of sed magic to remove the extra copy:
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-1-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 1.patch
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-2-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 2.patch
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-3-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 3.patch
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-4-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 4.patch
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-5-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 5.patch
curl -s https://lore.kernel.org/all/20241114-decode-ddr5-v1-6-0ed2db8ef30f@outlook.com.au/raw \
  | sed -n '/^-- $/q;p' > 6.patch

Then get the source code for i2c-tools:
git clone git://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git

(Alternatively, if you are reading this much later and i2c-tools has received other changes to make the patches incompatible with the latest version, get the i2c-tools-4.4.tar.gz release package, extract it, and follow the next steps.)
Move to the i2c-tools sub-directory, and apply the patches:
cd i2c-tools
patch -p1 < ../1.patch
patch -p1 < ../2.patch
patch -p1 < ../3.patch
patch -p1 < ../4.patch
patch -p1 < ../5.patch
patch -p1 < ../6.patch

Ideally, the patch commands should produce just one line of output each: patching file eeprom/decode-dimms. If patch indicates that a patch is applied with an offset, that is probably fine too. But if it says that a patch is being rejected or that "reversed (or already applied) patch is detected", stop; in that case, something is wrong, or the patches have finally been applied to the Git repository.
Build the i2c-tools:
make

And now you should have a DDR5-capable eeprom/decode-dimms. Test it:
sudo eeprom/decode-dimms

If it works to your satisfaction, copy it to /usr/local/sbin or wherever you want:
sudo cp eeprom/decode-dimms /usr/local/sbin/

And you are done.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800257/tool-to-display-ddr5-ram-spd-timings-mt-profiles

---

#### 627. Disable wakeup on plugging in USB-C power

**问题描述 / Problem Description**:
Tags: linux, usb, power-management, suspend, acpi | Score: 2 | Views: 262 | Answers: 1 | Created: 2025-10-03

**解决方案 / Solution**:
It seems that writing a 1 to /sys/module/acpi/parameters/ec_no_wakeup fixes the issue, which makes me think that maybe the kernel parameter I tried, acpi.ec_no_wake=1 is a typo I found in some documentation, and should actually be acpi.ec_no_wakeup=1.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/800189/disable-wakeup-on-plugging-in-usb-c-power

---

#### 628. How can I get Linux console output on both iGPU (HDMI) and IPMI (AST) simultaneously?

**问题描述 / Problem Description**:
Tags: ubuntu, grub2, tty, console, framebuffer | Score: 2 | Views: 473 | Answers: 2 | Created: 2025-06-19

**解决方案 / Solution**:
GRUB_CMDLINE_LINUX_DEFAULT="fbcon=map:1,0 console=tty1 console=tty2"
→ Only IPMI (fb1) works, HDMI stays black.

GRUB_CMDLINE_LINUX_DEFAULT="fbcon=map:0,1 console=tty1 console=tty2"
→ Only HDMI (fb0) works, IPMI stays black.

GRUB_CMDLINE_LINUX_DEFAULT="fbcon=map:both console=tty1 console=tty2"
→ Nothing appears on either display.



In configurations 1) and 2), I think the active display might switch as you switch from one virtual console to another (e.g. Ctrl-Alt-F1 / Ctrl-Alt-F2). But this won't help you achieve what you want, and you would have to wait a few seconds for the new display to wake up and sync each time you switch between the two.
In configuration 3), both  does not seem to be a valid parameter for fbcon=map: (in function fb_console_setup() located in drivers/video/fbdev/core/fbcon.c).
Also, Documentation/admin-guide/serial-console.rst goes into detail on various console= option values and tells me "The behavior is well defined when each device type (i.e. virtual console, serial port, parallel port,... USB serial?) is mentioned only once" and further explains that specifying two virtual consoles (tty1 and tty2) as consoles simultaneously is likely to not behave as expected.

What I Want
Ideally: Same console output mirrored on both HDMI and IPMI
Acceptable: Separate virtual terminals (e.g., tty1 on IPMI, tty2 on HDMI)

As far as I know, the Linux kernel's virtual console subsystem is designed to use just one display device (either a framebuffer or a classic VGA text mode) at a time. There seems to be no abstraction layer that would allow sending the console output to two different video devices simultaneously, or even making the console extend to two video displays usable in parallel using just kernel functionality.
You might get the kernel's virtual console on one framebuffer display, and a separate user-space terminal emulator like fbterm on another, but it seems to me that what you want to do is simply not possible using just the kernel's current virtual console and framebuffer functionalities. Sorry.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/797204/how-can-i-get-linux-console-output-on-both-igpu-hdmi-and-ipmi-ast-simultaneo

---

#### 629. Try netconsole in single machine, but not working

**问题描述 / Problem Description**:
Tags: ubuntu, kernel, kernel-modules, udp | Score: 2 | Views: 259 | Answers: 1 | Created: 2025-06-09

**解决方案 / Solution**:
You're running netconsole on a single machine and directing messages to 127.0.0.1, but netconsole doesn’t transmit logs over the loopback interface (lo), even when targeting localhost.
Assign a proper IP address to your device if not already done, and try using that IP instead.
Also check if your firewall, if active is blocking traffic to the port. You can also use socat or tcpdump to test whether the traffic is getting through/reaching its destination.

Linux Configure Netconsole To Log Messages Over UDP Network

Netconsole | Wiki Ubuntu

Netconsole set but no udp packet seen

Netconsole won't start, says "wlan0 doesn't exist, aborting"

11.9. Configuring netconsole

**参考链接 / References**:
- https://unix.stackexchange.com/questions/796825/try-netconsole-in-single-machine-but-not-working

---

#### 630. docker can't access to some tagged images

**问题描述 / Problem Description**:
Tags: ubuntu, docker, repository, docker-compose, tagging | Score: 2 | Views: 230 | Answers: 1 | Created: 2025-05-24

**解决方案 / Solution**:
This typically happens when there is a mismatch between how the image is stored locally and how you're trying to reference it.
That's why  Docker can't find it when you try to inspect it with ios-xr/xrd-control-plane.
For me, the same thing happens with some images, when I try to execute a command on an image using only the repository stored name, without the tag. There are two possible solutions.
Include the tag in your inspect
docker inspect ios-xr/xrd-control-plane:7.11.2
Using the image ID
docker inspect 58b64211c345

docker image tag

Three Ways to Check a Docker Image Exists In Registry

Docker Inspect Explained: The Essential Guide



docker inspect command was resulting into failure as I hadn't completed docker pull completely. In order to succeed docker inspect, you first need to pull image completely.


docker inspect results into Error: No such object even if image exists

Update

As far as I can tell, ios-xr/xrd-control-plane is a "combined" repository name split into iox-xr namespace and xrd-control-plane repository. The default registry location should be docker.io since nothing else was told. ios-xr/xrd-control-plane:7.11:2 image is not pulled from docker hub but using docker load -i <filename.tgz>. Could this be the root cause of the problem seen ?

The info would have been good to include in the question :) | Yes, that could very well be the root cause of the problem.
Since the image was loaded manually via docker load -i <namefile.tgz> rather than pulled from Docker Hub (docker.io), there might be inconsistencies in how Docker is handling the image metadata, particularly with the repository name and tag.
Docker might list the image under its original repository name (ios-xr/xrd-control-plane) in docker images, but the internal metadata could be incomplete or misconfigured.
Inspect the image by id instead of the repository name. If this works, the issue is specifically with the repository tag.
If the image is accessible by ID, retag it and try inspecting it again by name.

What is the difference between import and load in Docker?

Should I use save/load or export/import for my application using Docker? And an additional uncertainty

How to load a Docker image from a tar file

Docker image load vs. import



Sorry, from the output of docker images is the content of the first column REPOSITORY actually relevant w.r.t. the Docker Hub (docker.io) registry ?

No, the REPOSITORY column in docker images does not mean that the image is from docker Hub/docker.io. It just shows the image name + tag, regardless of origin, loaded via docker load, built locally, or pulled from any registry.
Since you loaded it via docker load, the name lists it but can’t fully track it like a pulled image.
The IMAGE ID is always the real key, it uniquely identifies the image.

The image ID is a unique identifier for each Docker image, similar to the container ID for containers. You can use this ID to reference and interact with the image.


The Challenges of Uniquely Identifying Your Images

What's the difference between a Docker image's Image ID and its Digest?




Tagging Docker Images Explained

How to identify Docker container IDs, images, and names?

**参考链接 / References**:
- https://unix.stackexchange.com/questions/796234/docker-cant-access-to-some-tagged-images

---

#### 631. Cannot set valid_lft to forever in Ubuntu 24.04 with diskless network boot, causes freeze

**问题描述 / Problem Description**:
Tags: ubuntu, freeze, netboot | Score: 2 | Views: 176 | Answers: 1 | Created: 2025-04-25

**解决方案 / Solution**:
/etc/netplan/00-installer-config.yaml or /etc/netplan/*.yaml
change
use-lifetime: false
sudo netplan apply

**参考链接 / References**:
- https://unix.stackexchange.com/questions/794181/cannot-set-valid-lft-to-forever-in-ubuntu-24-04-with-diskless-network-boot-caus

---

#### 632. How do you fix "no protocol specified" during wake from sleep in Linux?

**问题描述 / Problem Description**:
Tags: linux, xrandr, suspend | Score: 1 | Views: 49 | Answers: 1 | Created: 2026-01-29

**解决方案 / Solution**:
X server normally requires authentication and the necessary information is not easily available outside of the user's login session. On a modern system reasonably portable way for root to run commands in the user's session context is
systemd-run --user -M user@.host xrandr --output eDP-1 --off

here user is your logged in user's name, .host is the literal string.
It will work only if user is logged in in GUI session using X11. Also, on suspend systemd attempts to freeze user's sessions, so it may be the next problem.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/804111/how-do-you-fix-no-protocol-specified-during-wake-from-sleep-in-linux

---

#### 633. How can I exclude a single BSSID from a wireless network while allowing multiple others?

**问题描述 / Problem Description**:
Tags: linux, networking, wifi, mac-address, netplan | Score: 1 | Views: 99 | Answers: 1 | Created: 2026-01-21

**解决方案 / Solution**:
Based on "netplan" I assume you are using Ubuntu. I see two possibilities.

Use NetworkManager and create several connections with the same SSID bound to a different BSSID each. It can be done using netplan or (at least on Ubuntu 24.04 and above) by configuring directly in NetworkManager. Ubuntu now stores NetworkManager configuration in netplan instead of in the default keyfile format. Like

root@quokka:/etc/netplan# cat 02-conn-1.yaml 
network:
  version: 2
  wifis:
    connection-1:
      renderer: NetworkManager
      match: {}
      access-points:
        "SSID-foo":
          bssid: "11:11:11:11:11:11"
root@quokka:/etc/netplan# cat 02-conn-2.yaml 
network:
  version: 2
  wifis:
    connection-2:
      renderer: NetworkManager
      match: {}
      access-points:
        "SSID-foo":
          bssid: "22:22:22:22:22:22"
root@quokka:/etc/netplan# 

which ends up in
bor@quokka:~$ nmcli connection  | cat
NAME                           UUID                                  TYPE    DEVICE 
netplan-enp0s2                 d0ec664b-1176-38d1-abd4-71d76a4c1087  ethernet  enp0s2 
lo                             fc60ea63-4b78-4a3d-a48f-1b22a00e70e4  loopback  lo     
netplan-connection-1-SSID-foo  d943b426-b377-3d61-8516-ba562a71fb34  wifi      --     
netplan-connection-2-SSID-foo  41cacf27-378f-3989-a158-6090266cf074  wifi      --     
bor@quokka:~$ 


Use systemd-networkd and set bssid_ignore in the wpa_supplicant.conf. The systemd-networkd does not handle WiFi directly, you need to configure wpa_supplicant manually. Like

network={
        ssid="example"
        psk="very secret passphrase"
        bssid_ignore=02:11:22:33:44:55 02:22:aa:44:55:66
}

The heavily commented example wpa_supplicant.conf is installed as /usr/share/doc/wpa_supplicant/examples/wpa_supplicant.conf.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803933/how-can-i-exclude-a-single-bssid-from-a-wireless-network-while-allowing-multiple

---

#### 634. Systemd `greetd` service being replaced with masked `gdm3` service after every update

**问题描述 / Problem Description**:
Tags: debian, systemd, gnome, display-manager | Score: 1 | Views: 121 | Answers: 1 | Created: 2026-01-19

**解决方案 / Solution**:
The display-manager.service points to the package that owns shared/default-x-display-manager debconf key
bor@ThinkPad-E16-Gen3:~$ sudo debconf-show gdm3
  gdm3/daemon_name: /usr/sbin/gdm3
* shared/default-x-display-manager: gdm3
bor@ThinkPad-E16-Gen3:~$ echo metaget shared/default-x-display-manager owners | sudo debconf-communicate
0 gdm3, lightdm
bor@ThinkPad-E16-Gen3:~$ 

You can only select one of packages that owns this key. The display-manager.service is also statically WantedBy the graphical.target:
bor@ThinkPad-E16-Gen3:~$ systemctl cat graphical.target 
# /usr/lib/systemd/system/graphical.target
#  SPDX-License-Identifier: LGPL-2.1-or-later
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

[Unit]
Description=Graphical Interface
Documentation=man:systemd.special(7)
Requires=multi-user.target
Wants=display-manager.service
...

What you could do, is to mask the display-manager.service
systemctl mask --force display-manager.service

It will link it to the /dev/null and the gdm3 and lightdm scripts will not attempt to link it.
I believe systemd will log on startup about attempt to activate masked unit, but is as best as you can get.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803886/systemd-greetd-service-being-replaced-with-masked-gdm3-service-after-every-u

---

#### 635. upower: how to enforce charging start & end thresholds?

**问题描述 / Problem Description**:
Tags: debian, power-management, laptop, battery | Score: 1 | Views: 360 | Answers: 1 | Created: 2026-01-18

**解决方案 / Solution**:
The thresholds are taken from the CHARGE_LIMIT device udev property. It is by default initialized form the hwdb. The default settings are in the file 60-upower-battery.hwdb:
battery:*:*:dmi:*
 CHARGE_LIMIT=75,80

upowerd always reads these values, but it only actually applies them if charging thresholds are enabled. The only way to enable thresholds is via D-Bus method EnableChargeThreshold on the org.freedesktop.UPower.Device interface. See D-Bus API reference.
GNOME as of version 48 adds the UI to enable thresholds via upowerd.
You only need to enable it once, the setting is remembered by the upowerd. You could try to

stop upowerd
edit (or create) the file /var/lib/upower/charging-threshold-status with the content 1 (single digit without new line)
start upowerd

Note that at least on iPhone even if you limit charging to 80% iPhone will still perform full charge every now and then.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803869/upower-how-to-enforce-charging-start-end-thresholds

---

#### 636. How can I require a password before allowing USB flash drives on Ubuntu?

**问题描述 / Problem Description**:
Tags: ubuntu, mount, security, usb, usb-drive | Score: 1 | Views: 175 | Answers: 1 | Created: 2026-01-17

**解决方案 / Solution**:
On modern distributions the most simple solution is udev rule:
bor@ThinkPad-E16-Gen3:~$ cat /etc/udev/rules.d/99-usb-mount-auth.rules 
ACTION!="remove", SUBSYSTEM=="block", DRIVERS=="usb-storage|uas", ENV{UDISKS_SYSTEM}="1"
bor@ThinkPad-E16-Gen3:~$ 

It sets HintSystem for any mass storage device and the default policy for mounting "system" devices requires authentication as administrator.
On Ubuntu 24.04 the default polkit rules allow mouting of "system" devices without explicit authentication for users in the sudo group. But such users can run mount as root anyway, so I do not think it conflicts with your requirement.
This approach will require authorization for all actions related to this drive. The full list is
bor@ThinkPad-E16-Gen3:~$ pkaction | grep udisks2 | grep system\$
org.freedesktop.udisks2.ata-standby-system
org.freedesktop.udisks2.eject-media-system
org.freedesktop.udisks2.encrypted-change-passphrase-system
org.freedesktop.udisks2.encrypted-unlock-system
org.freedesktop.udisks2.filesystem-mount-system
org.freedesktop.udisks2.modify-device-system
org.freedesktop.udisks2.open-device-system
org.freedesktop.udisks2.power-off-drive-system
bor@ThinkPad-E16-Gen3:~$ 

If you only want to restrict some of them, you would need need to remove the udev rule and write a polkit rule. Rules are in JavaScript. Here is the example for mounting:
bor@ThinkPad-E16-Gen3:~$ sudo cat /etc/polkit-1/rules.d/00-usb-mount-auth.rules
// Mounting of removable drives
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.udisks2.filesystem-mount" ) {
            return polkit.Result.AUTH_SELF;
    }
});
bor@ThinkPad-E16-Gen3:~$ 

This rule requires that all users enter their own password when mounting removable drives. All other actions remain on their default settings, so ejecting will be allowed.
AUTH_SELF means that user needs to enter own password. You may consider AUTH_ADMIN which will require users to authenticate as administrator (root or other user(s) configured in polkit as administrative users. On Ubuntu the first user created during installation is the administrative user. Technically it is user in the sudo or admin groups).
More details on the rule syntax is in man polkit. The full list of actions for UDisks2 (which performs the actual mounting) can be listed with
pkaction | grep -F org.freedesktop.udisks2.

and you can get some description including the default policy with
bor@ThinkPad-E16-Gen3:~$ pkaction --action-id org.freedesktop.udisks2.filesystem-mount --verbose
org.freedesktop.udisks2.filesystem-mount:
  description:       Mount a filesystem
  message:           Authentication is required to mount the filesystem
  vendor:            The Udisks Project
  vendor_url:        https://github.com/storaged-project/udisks
  icon:              drive-removable-media
  implicit any:      auth_admin
  implicit inactive: auth_admin
  implicit active:   yes

bor@ThinkPad-E16-Gen3:~$ 

Actions with -system suffix are used when device is marked with HintSystem achieved by setting the UDISKS_SYSTEM udev property. The rules provided by distribution are installed in the /usr/share/polkit-1/rules.d and can be used as examples.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803833/how-can-i-require-a-password-before-allowing-usb-flash-drives-on-ubuntu

---

#### 637. Bluetooth Audio Device Not Recognized in Playback Devices

**问题描述 / Problem Description**:
Tags: debian, pulseaudio, bluetooth, jack | Score: 1 | Views: 194 | Answers: 2 | Created: 2026-01-15

**解决方案 / Solution**:
Check this post for more solutions:

Bluetooth speaker/headphones stop playing when Bluetooth keyboard is connected


Try to disabling the internal bluetooth and restarting the bluetooth.service.
sudo /sbin/modprobe -r btusb
sudo /sbin/modprobe btusb disable_ertm=1
sudo systemctl restart bluetooth.service


Bluetooth Inactive (dead) Module btusb not found in directory /lib/modules/5.15.0-56

And/or try creating a new /etc/bluetooth/main.conf.

Bluetooth main.conf is ignored – no way to apply settings

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803757/bluetooth-audio-device-not-recognized-in-playback-devices

---

#### 638. Ubuntu 24.04.3 - no audio on Gigabyte GA-720-US3

**问题描述 / Problem Description**:
Tags: ubuntu, audio | Score: 1 | Views: 40 | Answers: 1 | Created: 2026-01-14

**解决方案 / Solution**:
A later reboot fixed it. Why the previous reboots didn’t work, I really don’t know.
The only difference was that the later reboot happened after an overnight break, when everything was completely powered off, whereas the previous ones were just restarts.
There may be a clue there.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803743/ubuntu-24-04-3-no-audio-on-gigabyte-ga-720-us3

---

#### 639. Intel AX211 Wi-Fi repeatedly soft-blocked on Linux with iwlwifi firmware crashes after long period of inactivity

**问题描述 / Problem Description**:
Tags: linux, kernel, wifi, intel | Score: 1 | Views: 110 | Answers: 1 | Created: 2026-01-13

**解决方案 / Solution**:
I've had the exact same issue with both the AX210 card that I bought first, then assuming a defect, replaced with one with an AX211. So,

Does this pattern indicate a kernel + iwlwifi firmware regression for AX211 rather than faulty hardware?

I think it's a multi-device affecting firmware issue, and the fact that it had been like that for a year suggests intel doesn't have the resources or priority to fix that, because if it also fails for you in a HP (first-tier OEM to intel) laptop means that they're very very likely aware.
There's only been the temporarily fix to remove the device from the PCIe bus, wait a moment, then re-initialize it. It usually failed a few minutes after again, but it gave enough time to warn conference partners that I'll be offline for a minute while my system does a full reboot.
sudo sh -c "echo 1 > /sys/bus/pci/devices/0000:06:00.0/remove; sleep 0.5; echo 1 > /sys/bus/pci/rescan"

(adjust 06:00.0 for what lspci says)
Tried to debug how much of that is driver, and how much is firmware, but had to ration my time, and at the point debugging my wokrstation kernel via serial didn't suffice, I gave up; I need this computer to just work.
Bought a mediatek MT7925-based card instead; drivers for these are upstream in modern kernels. Has been running stably so far.

Is it plausible that a firmware update (e.g. linux-firmware) or cold reinitialization after long inactivity could trigger this without an explicit kernel upgrade?

I've not seen a firmware update yet, and while I saw the same as you, i.e., crashes during inactivity, I also lost the device suddenly during video calls occasionally. So, no, I don't think so.

downgrading / pinning the kernel (e.g. 6.5 LTS), or

depends on whether that is a viable option for you and actually fixes the issue, I'd say!

waiting for an upstream fix?

I waited for more than a year. My crystal ball is quite cloudy on this one, but I'd not assume it'd get fixed soon.

want to understand whether this is expected behavior for a bad kernel/firmware combination.

the firmware you're loading is the one supplied by intel for exactly your kernel version, so I don't think it's "worse" than any other.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803720/intel-ax211-wi-fi-repeatedly-soft-blocked-on-linux-with-iwlwifi-firmware-crashes

---

#### 640. How to see all debsums results that are not OK and not about files in /opt/?

**问题描述 / Problem Description**:
Tags: debian, grep, security | Score: 1 | Views: 81 | Answers: 2 | Created: 2026-01-08

**解决方案 / Solution**:
Those errors are sent on stderr (fd 2), not stdout (fd 1), so you need something like:
debsums -s 2>&1 | grep -v /opt/

-s to skip printing anything for OK files, 2>&1 so the fd 2 goes to the same as fd 1 (the pipe to grep).
With (t)csh, zsh or recent versions of bash, you can also write it:
debsums -s |& grep -v /opt/

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803625/how-to-see-all-debsums-results-that-are-not-ok-and-not-about-files-in-opt

---

#### 641. additional steps required to send synology btrfs snapshots to debian?

**问题描述 / Problem Description**:
Tags: debian, btrfs, synology | Score: 1 | Views: 131 | Answers: 1 | Created: 2026-01-07

**解决方案 / Solution**:
Adding the -v option to btrfs receive shows many error messages like:
ERROR: lsetxattr  [...] failed: Operation not supported

which led me to a Reddit post which suggests that the attribute 15 error is due to Synology using a proprietary ACL implementation which debian does not support.
The suggested workaround is to use an undocumented option btrfs send --without-syno-features. This does not work on my DSM version but may be useful to people running more recent versions.

Another suggestion I found was to add -E0 to the receive command.
Although this seems to allow the receive to complete, the "Received UUID"
is not set and the subvolume is not marked as readonly (presumably because of the errors), which then makes subsequent incremental sends fail. It is possible to do btrfs property set DST-SNAP ro true to set the property; and then find the appropriate Received UUID with btrfs subvolume show SRC-SNAP and set it on the destination subvolume using a python script
but personally I would not trust this as part of a disaster recovery system.

It looks like the rsync failure I was seeing can be avoided by not using -i (or by using an --out-format that does not include %L). Since I was only using -i for debugging, as long as the system has enough memory to let -H work, using rsync may be the reliable approach.

pro: portable backups - no Synology lock-in;
con: Synology ACLs are lost (not important in my case); incremental rsync is extremely inefficient compared to incremental btrfs snapshot

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803598/additional-steps-required-to-send-synology-btrfs-snapshots-to-debian

---

#### 642. Stuck troubleshooting ALSA and pipewire on Debian 13 (Trixie) - "Host is Down"; pipewire likely not running

**问题描述 / Problem Description**:
Tags: debian, audio, alsa, pipewire | Score: 1 | Views: 1099 | Answers: 1 | Created: 2026-01-05

**解决方案 / Solution**:
Based on the error message by running pipewire as root:
[E][15:30:19.465626] mod.protocol-native | [module-protocol-:  756 init_socket_name()] server 0x5593821ee280: name pipewire-0 is not an absolute path and no runtime dir found. Set one of PIPEWIRE_RUNTIME_DIR, XDG_RUNTIME_DIR or USERPROFILE in the environment

The solution is to run pipewire as a regular user since XDG_RUNTIME_DIR should be set there.
The same error can be easily reproduced with sudo pipewire.
Alternatively, if a user environment is not available, setting XDG_RUNTIME_DIR manually should fix the issue:
export XDG_RUNTIME_DIR=/run/user/$UID

Reference: https://voidforums.com/viewtopic.php?t=796

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803534/stuck-troubleshooting-alsa-and-pipewire-on-debian-13-trixie-host-is-down

---

#### 643. Why is my userID 1001 instead of 1000 on my new system

**问题描述 / Problem Description**:
Tags: ubuntu, passwd, uid | Score: 1 | Views: 347 | Answers: 2 | Created: 2026-01-02

**解决方案 / Solution**:
By default, Ubuntu and a few other distros define the starting user ID as 1000, and it has not changed in some time.  Defined as UID_MIN in file /etc/login.defs.  As distinct from a system user ID, a service account for software, not a human.
Most things do not care what your UID is and look up by name. However yes file ownership gets annoying when UIDs are not consistent.
id 1000  is another way to query the name of UID 1000. The program also takes names to go the other way.
Possible reasons another user may have existed at some point:

The system was installed by copying in an image that already had some user 1000.
Some software created a service user without doing the equivalent of  useradd --system
You have some other user directory other than  /etc/passwd file, unlikely but id or getent program will resolve user names however it is set up.

As to changing this:
 usermod --uid 1000 stephen

usermod program from shadow-utils can change a UID, and so  take over 1000 that does not exist.  Substitute your actual user name to select the login, that part does not take numeric IDs.
  find "$HOME" /var/mail -uid 1001
  find "$HOME" /var/mail -uid 1001 -print0 | xargs -r0 chown 1000

usermod --uid fixes file permissions in your home directory.  Review any files with the wrong owner, before changing their ownership.  Also run this on your external drive volumes.
Or, change owner to the new UID and use that going forward.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803454/why-is-my-userid-1001-instead-of-1000-on-my-new-system

---

#### 644. Is there a way to tell if a Mac connected via USB (in device mode) is itself in "Device Firmware Update" (DFU) mode?

**问题描述 / Problem Description**:
Tags: debian, macos | Score: 1 | Views: 109 | Answers: 2 | Created: 2025-12-31

**解决方案 / Solution**:
If you have a Mac available then I'd strongly urge people to follow the official documentation. That workflow is supported, where other options are not supported by apple themselves.
According to this, you should see the DFU window in the Finder on the attached machine.
There is further information available on how to identify the DFU port.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803417/is-there-a-way-to-tell-if-a-mac-connected-via-usb-in-device-mode-is-itself-in

---

#### 645. idevicerestore: never completes "Sending filesystem now"

**问题描述 / Problem Description**:
Tags: debian, macos, libimobiledevice | Score: 1 | Views: 158 | Answers: 1 | Created: 2025-12-31

**解决方案 / Solution**:
Build idevicerestore from git
This is unfortunately a lot more work.
For me after already building usbmuxd it required,

libimobiledevice
libirecovery
libtatsu

Then I could build,

idevicerestore


After you upgrade idevicerestore, you'll get,
Done sending SystemVolume
Unmounting filesystems (29)
Unmounting filesystems (29)
Unmounting filesystems (29)
Unmounting filesystems (29)
Unmounting filesystems (29)
Sealing System Volume (77)
Unmounting filesystems (29)
Unmounting filesystems (29)
Got status message
Status: Restore Finished

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803415/idevicerestore-never-completes-sending-filesystem-now

---

#### 646. Debian preseed partman-auto: expert_recipe with dynamic early_command is ignored / rebalanced (dynamic partition sizing based on hdd sda size)

**问题描述 / Problem Description**:
Tags: debian, partition, system-installation, debian-installer, preseed | Score: 1 | Views: 190 | Answers: 1 | Created: 2025-12-31

**解决方案 / Solution**:
For those who are wondering about automatic resizes I have used this modified version that actually works:
d-i partman/early_command string \
  set -e; \
  LOG="/var/log/partman-early.log"; \
  mkdir -p /var/log; \
  : > "$LOG"; \
  exec >>"$LOG" 2>&1; \
  \
  echo "=== partman early_command start ==="; \
  date; \
  \
  DISK=""; \
  for d in /sys/block/sd[a-z] /sys/block/vd[a-z] /sys/block/xvd[a-z] /sys/block/nvme*n1; do \
    [ -e "$d/size" ] || continue; \
    DISK="/dev/${d##*/}"; break; \
  done; \
  [ -z "$DISK" ] && DISK="/dev/sda"; \
  echo "DISK=$DISK"; \
  echo "partman-auto/disk string $DISK" | debconf-set-selections; \
  \
  b="${DISK##*/}"; \
  read SECTORS < "/sys/block/$b/size"; \
  HDD_MB=$((SECTORS * 512 / 1000000)); \
  echo "SECTORS=$SECTORS HDD_MB=$HDD_MB"; \
  \
  if   [ "$HDD_MB" -lt 17179 ]; then SWAP_MB=537; \
  elif [ "$HDD_MB" -lt 25769 ]; then SWAP_MB=805; \
  elif [ "$HDD_MB" -lt 34359 ]; then SWAP_MB=1074; \
  elif [ "$HDD_MB" -lt 45779 ]; then SWAP_MB=1611; \
  elif [ "$HDD_MB" -lt 68719 ]; then SWAP_MB=2147; \
  elif [ "$HDD_MB" -lt 137438 ]; then SWAP_MB=4295; \
  else SWAP_MB=4295; fi; \
  echo "SWAP_MB=$SWAP_MB"; \
  \
  EXTRA=""; \
  if [ "$HDD_MB" -lt 137440 ]; then \
    ROOT_MB=$((HDD_MB - SWAP_MB)); \
    ROOT_MAX=$ROOT_MB; \
  else \
    ROOT_MB=137439; \
    ROOT_MAX=137439; \
    EXTRA=" \
      1 1 1000000000 ext4 \
        \$primary{ } \
        method{ format } format{ } \
        use_filesystem{ } filesystem{ ext4 } \
        mountpoint{ /storage } ."; \
  fi; \
  echo "ROOT_MB=$ROOT_MB ROOT_MAX=$ROOT_MAX"; \
  echo "EXTRA=$EXTRA"; \
  \
  RECIPE="custom :: \
    ${ROOT_MB} ${ROOT_MB} ${ROOT_MAX} ext4 \
      \$primary{ } \$bootable{ } \
      method{ format } format{ } \
      use_filesystem{ } filesystem{ ext4 } \
      mountpoint{ / } . \
    ${SWAP_MB} ${SWAP_MB} ${SWAP_MB} linux-swap \
      \$primary{ } \
      method{ swap } format{ } . \
    $EXTRA"; \
  \
  echo "FINAL RECIPE:"; \
  echo "$RECIPE"; \
  debconf-set partman-auto/expert_recipe "$RECIPE"; \
  echo "=== partman early_command end ==="

d-i partman-auto/method string regular
d-i partman-auto/choose_recipe select custom
d-i partman-partitioning/confirm_write_new_label boolean true
d-i partman/confirm boolean true
d-i partman/confirm_nooverwrite boolean true
d-i partman/choose_partition select finish

What it does:
if the HDD size is:
<= 16 GiB - SWAP is 512 MiB
>= 24 GiB - SWAP is 768 MiB
>= 32 GiB - SWAP is 1024 MiB
>= 48 GiB - SWAP is 1536 MiB
>= 64 GiB - SWAP is 2048 MiB
>= 128 GiB - SWAP is 4096 MiB and also a /storage partition is added aswell the root size is capped to 128 GiB

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803408/debian-preseed-partman-auto-expert-recipe-with-dynamic-early-command-is-ignored

---

#### 647. What does Gnome notification that app is ready mean?

**问题描述 / Problem Description**:
Tags: linux, gnome, window-switching | Score: 1 | Views: 190 | Answers: 2 | Created: 2025-12-30

**解决方案 / Solution**:
The notification is part of the startup notification and indicates that an application is ready for use. It’s intended for cases where an application takes time to start and/or does so in a way that’s not obvious (without a new window taking the focus).
In the scenarios you describe, this happens because the desktop entry referenced by an icon in the dock corresponds to an application that detaches itself from the process that starts it. The “dock” doesn’t always work as an application switcher; if a running application doesn’t have a dot next to its icon, the dock isn’t aware that it’s running and will start it again instead of switching to it. So when you click on the VS Code icon, a new VS Code process starts, finds the existing VS Code instance, and completes the startup notification process; that’s why there’s a delay, and then the notification.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803389/what-does-gnome-notification-that-app-is-ready-mean

---

#### 648. Spotify client window style is like old Windows on Debian 13

**问题描述 / Problem Description**:
Tags: debian, window | Score: 1 | Views: 578 | Answers: 1 | Created: 2025-12-27

**解决方案 / Solution**:
I had the same issue with Ubuntu 25.10 + Wayland. It looks like Spotify use the wrong theme when running on Wayland (it’s very likely related to Electron).
I found the solution from Hypixely on Reddit.
We need to change the options passed when launching Spotify.

Copy the .desktop file in the home directory:
cp -v /usr/share/spotify/spotify.desktop ~/.local/share/applications/spotify.desktop


Open the file ~/.local/share/applications/spotify.desktop and replace Exec=spotify %U with this:
Exec=spotify --enable-features=UseOzonePlatform --ozone-platform=x11 %U



Now launch Spotify from GNOME Shell and it should use the theme of your desktop.

Here are the commands to do it directly:
cp -v /usr/share/spotify/spotify.desktop ~/.local/share/applications/spotify.desktop
sed --in-place \
's/Exec=spotify %U/Exec=spotify --enable-features=UseOzonePlatform --ozone-platform=x11 %U/' \
~/.local/share/applications/spotify.desktop

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803332/spotify-client-window-style-is-like-old-windows-on-debian-13

---

#### 649. Suspending sometimes does not turn off the system and freezes

**问题描述 / Problem Description**:
Tags: debian, suspend | Score: 1 | Views: 271 | Answers: 1 | Created: 2025-12-22

**解决方案 / Solution**:
Suspending, sleep, and freezing are, in my opinion, still things that have never worked consistently, everywhere, and 100% reliably with Linux on laptops for as long as I can remember. So, buggy and laggy. I've already written this in several answers, but many people disagree. That's why it's only a comment ^^

My comment was too general but too accurate for certain setups.
Suspend/Sleep under Linux can indeed be very problematic, and this is due to the complexity of the components involved.
For many users and hardware combinations, suspend/hibernate under Linux has been working flawlessly for years. The community and kernel developers are constantly working on improvements for specific hardware, but for much old and new hardware, it still doesn't work because of this complexity of the involved components.
Unfortunately, Windows does this better in this regard because it is better supported by hardware manufacturers. They usually test ACPI and Modern Standby primarily with Windows, and bugs are more often fixed for Windows, while Linux is often left unaddressed.

Involved Components:

Kernel (PM-Subsystem, Freezer, s2idle vs. S3)

Hardware and driver support, particularly on consumer laptops (NVMe, GPU, WLAN, USB, ACPI). Here, a single non-cooperative driver can block or cause the entire suspend process to fail.

Firmware / BIOS / UEFI (often Windows-centric)

Userspace (systemd, cryptsetup, running processes)

The ACPI implementations (Advanced Configuration and Power Interface) from many manufacturers, especially on laptops are often buggy or not fully documented. Linux has to work around or correct this firmware, which doesn't always work perfectly.


If one of these layers doesn't cooperate properly, the suspend process hangs.

S2idle vs. S3 (Deep Sleep):
A key sticking point is s2idle (Modern Standby).
Many current Lenovo Ideapads no longer support true S3 (deep sleep) and force s2idle.
Modern laptops (like your Lenovo) often use the very shallow s2idle state instead of the deep S3 (Suspend-to-RAM). s2idle is less energy-efficient (higher battery drain) and more prone to disruptions from background processes or hardware that doesn't enter the sleep state correctly.

Hybrid sleep w/ S2idle/S0 instead of S3

Changing suspend method

System Sleep States

Support suspend modes "s2idle", "shallow", and "deep" #13451

The only issue is that s2idle drains the battery like crazy compared to S3

Do other linux distros have the same quality sleep function as what's on Steam OS? Is it proton that provides this functionality, or is there something specific to Steam OS? 



Here are further sources of error:

Processes that do not respond to the freeze signal in time. The suspend procedure freezes processes and I/O. If a process is in a kernel context waiting for slow I/O, performing heavy I/O, or has blocked I/O waits, this can delay or block the freeze step.

cryptsetup/LUKS, which waits for open block devices, or cryptsetup-suspend adds another, potentially critical layer. Unlocking the LUKS container on wake-up can be another point of failure.

The hanging state during suspend entry strongly suggests that the kernel may be waiting for a hardware event specifically, for a component to signal it is ready for sleep, which never occurs.



Personally, I've gotten into the habit of disabling it completely on certain hardware setups because the process is always buggy, and I've had the same problems as you on those systems and couldn't fix them.

Keep the PC in low power, but not sleeping, disable sleep, disable suspend, disable lid close, disable monitor sleep

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803237/suspending-sometimes-does-not-turn-off-the-system-and-freezes

---

#### 650. How to best protect against bit rot on a frequently powered-on SSD?

**问题描述 / Problem Description**:
Tags: linux, raid, storage, ssd, data-recovery | Score: 1 | Views: 350 | Answers: 2 | Created: 2025-12-21

**解决方案 / Solution**:
The solution you're looking for has nothing to do with what filesystem you use, or RAID, or LVM.  It's called backup your data regularly.
Software
You'll need to use appropriate backup software, there are dozens to choose from starting from basic tools like tar or rsync, to incremental snapshot-like tools like rdiff-backup or backuppc.
The exact software you use doesn't matter much as long as a) it's easy to restore to bare metal in case of disaster where you don't have your usual system & environment & notes etc available (practice restores to make sure it works and so that you are familiar with the procedure), and b) you use it regularly or set it up to run regularly with cron.
Search your distro's package database for backup software and experiment with a few to find out which ones suit your needs and you feel comfortably using.
IMO, simplest is best.  The more complicated and fancy the backup software, the more things can go wrong and the less likely it is to be useful during an emergency.
Make a "Live" system on a USB flash drive with all the software and information (e.g. remote login passwords, encryption keys, personal notes on how to perform the restore, etc) you need to successfully restore.  Start with an existing Live USB like Clonezilla, gparted or System Rescue and add whatever you need.  Test that you are able to successfully restore your backups using it. Make several copies of it, and keep at least one of them off-site.
BTW, Clonezilla ("CZ") makes a great image backup system, and you should consider using it in addition to regular file-based backups. It can image your entire drive, including partition tables, and store compressed and minimised (i.e. skipping empty/unused space in your filesystems) images to either another drive (e.g. USB) or to a file-server/NAS via NFS or Samba.  If you make, say, a monthly CZ image of your system then you can restore that in case of emergency and only need to do a file restore of whatever changed since the last CZ backup.
Worth noting: a backup you haven't tested is a backup in theory only. It may fail you when you need it.
Every so often, perform test restores to make sure that a) the process works and you're familiar with it, and b) you're backing up everything you need to backup - realising that you forgot to backup an important directory or you changed something on your system but didn't update your backup configuration to match is a terrible thing to discover when you need to recover from disaster.
Hardware
Unfortunately tape backup isn't practical for most people these days (tape drives and tape media are both too expensive, and there's not enough storage capacity on the tapes to cope with modern drive sizes), so your best bet is either:

Another machine on the LAN (or somewhere on the internet) to send backups to. If you backup to "the cloud" (i.e. computers not owned by you), you'll need to use backup software which can encrypt your backups.  Note that restoring from remote backups will be more difficult as you'll need a working network AND a copy of your remote logins and passwords and the decryption key, as well as a bootable system with the restore software on it.

Two or more (preferably many more) external drives, plugged in to USB.  Preferably use an external drive dock which allows you to swap standalone SATA drives rather than pre-made brand-name external drives.   Read up on backup rotation strategies, but the gist is that you should cycle through whatever number of backup drives you have, so you always have multiple backups (some of which should be offsite).

a combination of both - e.g. a NAS (pre-built name-brand ones are fine but you will get much better value for money by DIY-ing it with an old PC with lots of drives) for local backups and some USB drives for offsite backups.



BTW, there's no reason NOT to use either btrfs or zfs.

I personally don't use btrfs because I don't trust it (it still has occasional fs-destroying bugs which can not be attributed to faulty hardware or user-error) but most people consider btrfs to be safe enough for single-drive or RAID-1 like mirroring.

ZFS being "out-of-tree" is no big deal.  Most distros have dkms packages for it, which automate the process of compiling the kernel module - installing and updating it is trivial.


However, even if you use one of them, you will still need to backup regularly.
NEITHER BTRFS, ZFS, OR RAID ARE A SUBSTITUTE FOR REGULAR BACKUPS.
Both btrfs and zfs have features (snapshot, send, and receive) which make backing up easy and fast....much faster than any file or image based backup because the snapshots tell zfs send or btrfs send exactly which blocks have changed, so it doesn't need to compare file timestamps or checksums.  BTW, many DIY "NAS" solutions like FreeNAS use ZFS so you can zfs send backups to them.
Running btrfs scrub or zfs scrub regularly will protect against bit-rot (although with only one drive in the pool, they can only detect errors, not correct them)....but bit-rot is nowhere near the huge problem you imagine it is.  Yes, it happens, but it's extremely rare - far more rare than drives dying, fire, flood, earthquakes, theft, sabotage, or user-error accidentally deleting or overwriting important files.
They also offer features which are useful in day-to-day usage, including transparent compression.
My recommendation: get over your worry about "out-of-tree" kernel modules and just use ZFS.
You can use it for your data partitions like /home (or "datasets" in zfs terminology) AND you can use it for the root filesystem.  You can even start with using zfs for your data partitions, and optionally convert the rootfs to zfs later.
With rootfs on ZFS, I recommend either a) having an ext4 or xfs /boot partition that's big enough to boot a rescue image via grub's memdisk or b) setting up a tftp server on your LAN so you can netboot a rescue image or c) as I do, both a and b.  The more ways you prepare in advance to recover from disaster, the better.

Finally, I can only second what Marcus said about using LVM (or any form of RAID or RAID-like software) on multiple partitions on the same drive: DON'T DO IT.   Performance will suck and you'll massively increase the write wear on your drive, reducing its lifetime.
It really is a terrible idea.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803202/how-to-best-protect-against-bit-rot-on-a-frequently-powered-on-ssd

---

#### 651. Nat prerouting rule not working for WiFi builtin module

**问题描述 / Problem Description**:
Tags: linux, networking, vpn, nftables, tor | Score: 1 | Views: 43 | Answers: 1 | Created: 2025-12-20

**解决方案 / Solution**:
iif $LAN_IF tcp dport 1-65535 redirect to 9040

does change the destination address but NOT the ingress interface. Nothing from the outside can be moved to lo – that is part of the IP definition.
As iif is still wlan0
iif "lo" accept

does not catch the packets, they run into policy drop.
These can never work:
iif $LAN_IF oif "lo" accept
iif "lo" oif $VPN_IF accept

There is no forwarding from or to lo.

**参考链接 / References**:
- https://unix.stackexchange.com/questions/803182/nat-prerouting-rule-not-working-for-wifi-builtin-module

---
