# macOS 常见故障及解决方法 | macOS Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 04:29:12 UTC_

## 中文 🇨🇳
**macOS 常见故障及解决方法**

本页面每小时自动从 Stack Exchange 社区抓取 MACOS 平台常见故障及解决方法。

### MACOS 常见故障及解决方法

#### 1. Why am I getting an “invalid active developer path” when attempting to use Git after upgrading to macOS Tahoe?

**故障现象**: Why am I getting an “invalid active developer path” when attempting to use Git after upgrading to macOS Tahoe?
**标签 / 来源**: Tags: xcode, development, git, macos | apple | 👍 3062 | 💬 8 answers

**问题描述**:
Tags: xcode, development, git, macos | Score: 3062 | Views: 2593657 | Answers: 8

**解决方法 / 社区答案**:
Solution
Open Terminal, and run the following:
xcode-select --install

This will pop a dialogue box, Select &quot;Install&quot;, and it will download and install the Command Line Tools package and fix the problem.
(The popped Window may be behind other windows.)
You do not need Xcode, you can install only the Command Line Tools here, it is about 130 MB (600 MB as of Xcode v14.1).
If the above alone doesn't do it, then also run:
sudo xcode-select --reset

Further reading
The problem is that one needs to explicitly agree to the license agreement.  As a follow on step, you may need to reset the path to Xcode if you have several versions or want the command line tools to run without Xcode.
sudo xcode-select --switch /Applications/Xcode.app
sudo xcode-select --switch /Library/Developer/CommandLineTools

I found the solution in this question, Command Line Tools not working.
You may get an error message: &quot;Can't install the software because it is not currently available from the Software Update server&quot;. In this case xcode-select --reset works as pointed by akozin.

**参考链接**: https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a

> 📎 来源 / Source: https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a

#### 2. List of all packages installed using Homebrew

**故障现象**: List of all packages installed using Homebrew
**标签 / 来源**: Tags: macos, command-line, homebrew, open-source | apple | 👍 1068 | 💬 11 answers

**问题描述**:
Tags: macos, command-line, homebrew, open-source | Score: 1068 | Views: 1439806 | Answers: 11

**解决方法 / 社区答案**:
brew list and brew list --cask
Running brew list will show a list of all your installed Homebrew formulae and casks.

If you wish to list casks only, brew list --cask will provide the items installed using Homebrew Cask.

**参考链接**: https://apple.stackexchange.com/questions/101090/list-of-all-packages-installed-using-homebrew

> 📎 来源 / Source: https://apple.stackexchange.com/questions/101090/list-of-all-packages-installed-using-homebrew

#### 3. How to find cause of high kernel_task cpu usage?

**故障现象**: How to find cause of high kernel_task cpu usage?
**标签 / 来源**: Tags: macos, kernel | apple | 👍 712 | 💬 16 answers

**问题描述**:
Tags: macos, kernel | Score: 712 | Views: 615533 | Answers: 16

**解决方法 / 社区答案**:
TLDR; If your MacBook Pro runs hot or shows a high % CPU for the kernel task, try charging on the right and not on the left.

High kernel_task CPU Usage is due to high chassis temperature caused by charging. In particular Left Thunderbolt port usage.
Solutions include:

Move charging from the left to the right side. If you have a second charger then plug it in on the right side. Avoid plugging everything on the right side (see last paragraph below).
Unplug something from the left side. Either power or another accessory until the battery is full.
Force fans to max before plugging in. iStatMenus has an easy Sensors -&gt; Fans menu item to do so. This only helps in marginal conditions.
Move to a cooler room.
If using both laptop display and external display try switching to just one or the other (I switched to external only, laptop lid closed). Some MBP (eg 15&quot; Intel touchbar models) have a design quirk where this config can get hotter than it should.

Proof:
Actual CPU temperature or application CPU usage is uncorrelated with kernel_task. A hot CPU is throttled by reducing its clock speed, not by scheduling fake no-op load.
The graphs below are from iStatMenus. The machine had been used on battery then plugged in.
State A a USB-C hub (a mouse and keyboard, plus power) and a USB-C HDMI 2.0 adapter, both on the left side. You can see the Thunderbolt Left Proximity temperature sensor rise quickly. About 3-4 minutes later the dreaded kernel_task high CPU usage starts.
State B cures the kernel_task problem by moving power from the left ports to the right. The left side temperature drops and the kernel_task goes away within about 15 seconds.
This is causal. Moving power back to the left side, restoring State A, quickly restores the temperatures and kernel_task again comes back after 3-4 minutes. Again moving power back to the right side, restoring State B, resolves the problem immediately.
State C shows that simply having stuff plugged in to TB ports raises their temperature significantly. Both the hub (mouse and keyboard ONLY) and HDMI adapter individually raise the temperature about 10 degrees, and 15 degrees together.

(all other temperatures were both low and flat. Under 55 degrees.)
Note that high temperature on the right side appears to be ignored by the OS. Plugging everything into the two right ports instead of the left raised the Right temperatures to over 100 degrees, without the fans coming on. No kernel_task either, but the machine becomes unusable from something throttling.
Ergo, high CPU usage by kernel_task is caused by high Thunderbolt Left Proximity temperature, which is caused by charging and having normal peripherals plugged in at the same time.
2017 15&quot; Macbook Pro, MacOS 10.14.5

To actually answer the question:

How can I find out what this process is doing?

The only way to actually ask the kernel what it's doing is to attach a kernel debugger. That means getting a debug kernel from Apple, rebooting, then using a second Mac to attach to the debugged machine. You can then examine stack traces and guess what they mean.
Otherwise guessing and testing is the only way. Of course that leads to false conclusions more often than not.

**参考链接**: https://apple.stackexchange.com/questions/363337/how-to-find-cause-of-high-kernel-task-cpu-usage

> 📎 来源 / Source: https://apple.stackexchange.com/questions/363337/how-to-find-cause-of-high-kernel-task-cpu-usage

#### 4. Shortcut for toggling between different windows of same app?

**故障现象**: Shortcut for toggling between different windows of same app?
**标签 / 来源**: Tags: macos, keyboard, google-chrome | apple | 👍 654 | 💬 15 answers

**问题描述**:
Tags: macos, keyboard, google-chrome | Score: 654 | Views: 935240 | Answers: 15

**解决方法 / 社区答案**:
UK Keyboard
[see below for other languages]
 Cmd ⌘   ` 
 Cmd ⌘   Shift ⇧    `  to go the other way.
Left of z on a UK keyboard [non-shifted ~ ]

Note: This only works if all windows are in the same Space, not if they are spread over multiple Spaces, or if any are fullscreen.
To overcome this for non-fullscreen window, use Cmd ⌘Tab as usual and on the icon of the application you want to switch windows in press the down arrow key (with Cmd ⌘ still pressed). Then use left/right keys to navigate to the desired window across spaces and desktops. To emphasise, This fails for any fullscreened windows, whilst continuing to work for any that are not.
You can also achieve this by right-clicking the app's icon in the Dock - this is the only method that will also switch to fullscreen windows, the other methods will not.
From comments - You can check which key command it is for your language by switching to Finder, then look at the Window menu for 'Cycle through windows'...

BTW, specifically in Chrome, Safari &amp; Firefox, but no other app I know of on Mac,  Cmd ⌘   (number)  will select individual tabs on the frontmost window.
It also would appear that  Cmd ⌘   `   is yet another of those language-specific shortcuts; so if anyone finds any more variants, please specify for which language &amp; keyboard type.
If anybody finds new combos for different languages, please check Keyboard layout here - This is a mirror of the very useful old Apple KB page, now gone from Apple How to identify keyboard localizations - &amp; add that as well as which Input Source you use in System Prefs &gt; Keyboard &gt; Input Sources.
Add a keyboard picture from the KB page too, if that would help.
That will make it easier for future Googlers.
Further info:
You can change the keys in System Settings… &gt; Keyboard &gt; Keyboard Shortcuts… &gt; Keyboard
though it doesn't list the reverse direction, it does still work when you add shift to that new combo. I tested by moving mine from  `   (and  ~ ) to  §  (and  ± )

You can use the alternative of  Ctrl ⌃   F4  [visible in the prefs window above] but that almost indiscriminately marches through every single open window on all Spaces, without switching to the correct Space each time. It's really not too useful unless you use a single Space, just included here for completeness.

**参考链接**: https://apple.stackexchange.com/questions/193937/shortcut-for-toggling-between-different-windows-of-same-app

> 📎 来源 / Source: https://apple.stackexchange.com/questions/193937/shortcut-for-toggling-between-different-windows-of-same-app

#### 5. Please share your hidden macOS features or tips and tricks

**故障现象**: Please share your hidden macOS features or tips and tricks
**标签 / 来源**: Tags: macos | apple | 👍 612 | 💬 159 answers

**问题描述**:
Tags: macos | Score: 612 | Views: 346412 | Answers: 159

**解决方法 / 社区答案**:
In any Finder window or Open/Save dialog, you can hit ⌘&#x21E7;G (just '/' also works in Open/Save) to get a location bar from which you can directly type in the directory to go to. It even supports ~ for home and tab completion.

The Open/Save dialog has several other useful shortcuts:


⌘  R -
Reveals the selected item in a new
Finder window.
⌘  I - Info window shows for the selected item.
⌘  &#x21E7;  > - Shows/Hides hidden files in the dialog
⌘  F - cursor jumps to the Find text field
/ or ~ - Opens a Go To Folder dialogue. 
⌘  D or ⌘  &#x21E7; D - selects the ~/Desktop folder as a destination
⌘  &#x2325;  L - selects ~/Downloads folder as a destination
⌘  &#x21E7; O - selects ~/Documents folder as a destination
⌘  &#x2325;  S - Shows/Hides sidebar
⌘  . or esc - Cancels and closes the dialog window

**参考链接**: https://apple.stackexchange.com/questions/400/please-share-your-hidden-macos-features-or-tips-and-tricks

> 📎 来源 / Source: https://apple.stackexchange.com/questions/400/please-share-your-hidden-macos-features-or-tips-and-tricks

#### 6. Remap &quot;Home&quot; and &quot;End&quot; to beginning and end of line

**故障现象**: Remap &quot;Home&quot; and &quot;End&quot; to beginning and end of line
**标签 / 来源**: Tags: macos, keyboard | apple | 👍 587 | 💬 13 answers

**问题描述**:
Tags: macos, keyboard | Score: 587 | Views: 228305 | Answers: 13

**解决方法 / 社区答案**:
The default shortcuts for moving to beginning or end of (wrapped) lines are ⌘← and ⌘→. ⌥↑ and ⌥↓ or ⌃A and ⌃E move to the beginning or end of unwrapped lines (or paragraphs). ⌥← and ⌥→ move backwards/forward by words, and all of these are compatible with holding Shift to select during the corresponding moves.
You could remap home and end by creating ~/Library/KeyBindings/ and saving a property list like this as DefaultKeyBinding.dict:
{
    &quot;\UF729&quot;  = moveToBeginningOfLine:; // home
    &quot;\UF72B&quot;  = moveToEndOfLine:; // end
    &quot;$\UF729&quot; = moveToBeginningOfLineAndModifySelection:; // shift-home
    &quot;$\UF72B&quot; = moveToEndOfLineAndModifySelection:; // shift-end
}

Most of the keybindings for editing text in OS X are defined in /System/Library/Frameworks/AppKit.framework/Resources/StandardKeyBinding.dict.
Applying changes requires reopening applications. DefaultKeyBinding.dict is ignored by some old versions of Xcode (works with latest version 6.3.1), Terminal, and many cross-platform applications.
See Cocoa Text System for more information about the customizable keybindings.
Terminal's keybindings can be customized in Preferences &gt; Profiles &gt; Settings &gt; Keyboard. \033OH moves to the beginning of a line and \033OF to the end of a line.
In Eclipse, key bindings should be modified in Preferences &gt; General &gt; Keys. You need to modify default bindings for commands Line Start and Line End (replace ⌘← by ↖ and ⌘→ by ↘). For selection to work, also modify Select Line Start and Select Line End.
PS: You may need to logout and login again for the ~/Library/KeyBindings/DefaultKeyBinding.dict change to take effect.

**参考链接**: https://apple.stackexchange.com/questions/16135/remap-home-and-end-to-beginning-and-end-of-line

> 📎 来源 / Source: https://apple.stackexchange.com/questions/16135/remap-home-and-end-to-beginning-and-end-of-line

#### 7. How to prevent Mac from changing the order of Desktops/Spaces

**故障现象**: How to prevent Mac from changing the order of Desktops/Spaces
**标签 / 来源**: Tags: macos, mac, spaces, mission-control | apple | 👍 539 | 💬 2 answers

**问题描述**:
Tags: macos, mac, spaces, mission-control | Score: 539 | Views: 207135 | Answers: 2

**解决方法 / 社区答案**:
General Solution

System Settings/Preferences &gt; Search for &quot;Spaces&quot; &gt; Uncheck Automatically rearrange Spaces based on most recent use

Newer MacOS Ventura (v13)

System Settings &gt; Desktop &amp; Dock &gt; Scroll down to Mission Control section &gt; Uncheck Automatically rearrange Spaces based on most recent use



Older macOS (v12 and older)
System Preferences &gt; Mission Control
Uncheck Automatically rearrange Spaces based on most recent use.

This will fix the order of all your regular Spaces - but not Fullscreen spaces, which always go to the right of existing numbered Spaces.

From comments: Note this cannot fix the Mac confusing which external screen is which. That's not user-controlled at all, &amp; seems to occur mainly [though not always] when the external screens are identical.
Late note:
This echoes the behaviour of Cmd/Tab or equivalent in most operating systems, so could be considered a 'sensible' default.
 just to save this attracting even more comments on why it was a good/bad choice of default.

**参考链接**: https://apple.stackexchange.com/questions/214348/how-to-prevent-mac-from-changing-the-order-of-desktops-spaces

> 📎 来源 / Source: https://apple.stackexchange.com/questions/214348/how-to-prevent-mac-from-changing-the-order-of-desktops-spaces

#### 8. How do I launch Finder from terminal or command line

**故障现象**: How do I launch Finder from terminal or command line
**标签 / 来源**: Tags: macos, applications, command-line | apple | 👍 508 | 💬 1 answers

**问题描述**:
Tags: macos, applications, command-line | Score: 508 | Views: 865921 | Answers: 1

**解决方法 / 社区答案**:
To open your current directory in Finder from Terminal, type open .
So, if you want Documents: open ~/Documents
Library: open ~/Library
Downloads: open ~/Downloads
And so on.

**参考链接**: https://apple.stackexchange.com/questions/101432/how-do-i-launch-finder-from-terminal-or-command-line

> 📎 来源 / Source: https://apple.stackexchange.com/questions/101432/how-do-i-launch-finder-from-terminal-or-command-line

#### 9. Why does my dock keep moving back to my other monitor?

**故障现象**: Why does my dock keep moving back to my other monitor?
**标签 / 来源**: Tags: macbook-pro, macos, display, dock | apple | 👍 492 | 💬 8 answers

**问题描述**:
Tags: macbook-pro, macos, display, dock | Score: 492 | Views: 525765 | Answers: 8

**解决方法 / 社区答案**:
You can summon the Dock on a different display by moving the cursor to the bottom of the desired display, and then continuing moving down. It may be possible that this is occurring when you inadvertently perform that action.

I answered a similar question: cmd-tab behavior on Mavericks with multiple displays.

**参考链接**: https://apple.stackexchange.com/questions/169719/why-does-my-dock-keep-moving-back-to-my-other-monitor

> 📎 来源 / Source: https://apple.stackexchange.com/questions/169719/why-does-my-dock-keep-moving-back-to-my-other-monitor

#### 10. How can I create a symbolic link in Terminal?

**故障现象**: How can I create a symbolic link in Terminal?
**标签 / 来源**: Tags: macos, command-line, file, symlink | apple | 👍 484 | 💬 7 answers

**问题描述**:
Tags: macos, command-line, file, symlink | Score: 484 | Views: 724804 | Answers: 7

**解决方法 / 社区答案**:
┌── ln(1) link, ln -- make links
│   ┌── Create a symbolic link.
│   │                         ┌── the optional path to the intended symlink
│   │                         │   if omitted, symlink is in . named as destination
│   │                         │   can use . or ~ or other relative paths
│   │                   ┌─────┴────────┐
ln -s /path/to/original /path/to/symlink
      └───────┬───────┘
              └── the path to the original file/folder
                  can use . or ~ or other relative paths


$ echo content &gt; original
$ ln -s original symlink
$ ls -la original symlink
-rw-r--r--  1 grgarside  staff    8 28 Jan 18:44 original
lrwxr-xr-x  1 grgarside  staff    8 28 Jan 18:44 symlink -&gt; original
$ cat symlink
content

For more information about ln(1) see the man page:
$ man ln

The path to the symlink is optional; if omitted, ln defaults to making a link with the same name as the destination, in the current directory:
$ cd ~/Documents
$ ln -s ../Pictures
$ ls -l Pictures
lrwxr-xr-x  1 user  staff  11 Feb  1 17:05 Pictures -&gt; ../Pictures

To create a symlink to replace a system directory (e.g. if you want to have /Users pointing to another disk drive), you need to disable System Integrity Protection. You can re-enable it after the symlink is set up.

**参考链接**: https://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal

#### 11. How do I find my IP Address from the command line?

**故障现象**: How do I find my IP Address from the command line?
**标签 / 来源**: Tags: macos, network, command-line | apple | 👍 451 | 💬 11 answers

**问题描述**:
Tags: macos, network, command-line | Score: 451 | Views: 1668077 | Answers: 11

**解决方法 / 社区答案**:
Local IP address
Use ipconfig getifaddr en0 or ipconfig getifaddr en1, depending on what network adapter your machine is using.
Public IP address
dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com

Output, e.g.:
172.79.136.120

Command explanation
The command you provided, dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com, is a command-line instruction that uses the dig utility to perform a DNS (Domain Name System) lookup. Let's break down the components of the command:

dig: dig stands for &quot;domain information groper,&quot; and it is a command-line tool commonly available on Unix-like systems for querying DNS servers.

-4: This option specifies that the command should use IPv4 protocol for the DNS lookup. It ensures that the query is sent using IPv4 instead of IPv6.

TXT: This indicates the type of DNS record being requested. In this case, the command is asking for the TXT record.

+short: This option is used to display only the relevant information from the DNS response, providing a concise output.

o-o.myaddr.l.google.com: This is the hostname used for the DNS lookup. It is a special hostname that Google uses to provide information about the IP address from which the DNS query originates.

@ns1.google.com: This specifies the DNS server to which the query is sent. In this case, it is set to ns1.google.com, which is one of Google's public DNS servers.


When you run this command, it queries the ns1.google.com DNS server for the TXT record associated with o-o.myaddr.l.google.com. The response will contain the TXT record, which typically includes information about the IP address of the client making the DNS query. The +short option ensures that only the relevant information is displayed, making it easier to read the output.

**参考链接**: https://apple.stackexchange.com/questions/20547/how-do-i-find-my-ip-address-from-the-command-line

> 📎 来源 / Source: https://apple.stackexchange.com/questions/20547/how-do-i-find-my-ip-address-from-the-command-line

#### 12. mds and mds_stores constantly consuming cpu

**故障现象**: mds and mds_stores constantly consuming cpu
**标签 / 来源**: Tags: macbook-pro, spotlight, cpu | apple | 👍 450 | 💬 15 answers

**问题描述**:
Tags: macbook-pro, spotlight, cpu | Score: 450 | Views: 679869 | Answers: 15

**解决方法 / 社区答案**:
As you know, the mds and mds_stores are Spotlight activities.
The reason why your Spotlight is so active could be a number of things; it could be you have an app or multiple apps constantly changing some folder contents.
First let's check whether Spotlight is the cause of the fans running so much. To test this, run the following in your terminal:
sudo mdutil -a -i off

This will turn off indexing of files, and should result in a clear slow down of the fans if mds and/or mds_stores are to blame.
To turn indexing back on, run
sudo mdutil -a -i on

After this you could run the complete re-indexing of your hard drive (be aware this could be an over night job), it will delete your Spotlight data base forcing it to start over.
sudo rm -rf /System/Volumes/Data/.Spotlight-V100/*

The next and final step would be to add others to your (do not scan), privacy settings.

**参考链接**: https://apple.stackexchange.com/questions/144474/mds-and-mds-stores-constantly-consuming-cpu

> 📎 来源 / Source: https://apple.stackexchange.com/questions/144474/mds-and-mds-stores-constantly-consuming-cpu

#### 13. How can I trigger a Notification Center notification from an AppleScript or shell script?

**故障现象**: How can I trigger a Notification Center notification from an AppleScript or shell script?
**标签 / 来源**: Tags: terminal, applescript, macos, notifications, command-line | apple | 👍 422 | 💬 13 answers

**问题描述**:
Tags: terminal, applescript, macos, notifications, command-line | Score: 422 | Views: 267265 | Answers: 13

**解决方法 / 社区答案**:
With Mavericks and later, you can do this using AppleScript's 'display notification':

display notification "Lorem ipsum dolor sit amet" with title "Title"


                          

That's it—literally that simple! No 3rd-party libraries or apps required and is completely portable for use on other systems. 10.9 notification on the top, 10.10 DP in the middle, 10.10 on the bottom.

AppleScript can be run from the shell using /usr/bin/osascript:

osascript -e 'display notification "Lorem ipsum dolor sit amet" with title "Title"'


You can also customise the alert further by adding…


a subtitle

Append 'subtitle' followed by the string or variable containing the subtitle.

display notification "message" with title "title" subtitle "subtitle"


The above example produces the following notification:


sound

Append 'sound name' followed by the name of a sound that will be played along with the notification.

display notification "message" sound name "Sound Name"


Valid sound names are the names of sounds located in…


~/Library/Sounds
/System/Library/Sounds





Posting notifications can be wrapped as a command-line script. The following code can be run in Terminal and will add a script to /usr/local/bin (must exist, add to $PATH) called notify.

cd /usr/local/bin &amp;&amp; echo -e "#!/bin/bash\n/usr/bin/osascript -e \"display notification \\\"\$*\\\"\"" &gt; notify &amp;&amp; chmod +x notify;cd -


This is the script that the above will add to notify.

#!/bin/bash
/usr/bin/osascript -e "display notification \"$*\""


Now to display a notification:

notify Lorem ipsum dolor sit amet
sleep 5; notify Slow command finished

**参考链接**: https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel

> 📎 来源 / Source: https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel

#### 14. Got any tips or tricks for Terminal in Mac OS X?

**故障现象**: Got any tips or tricks for Terminal in Mac OS X?
**标签 / 来源**: Tags: mac, terminal, macos | apple | 👍 404 | 💬 133 answers

**问题描述**:
Tags: mac, terminal, macos | Score: 404 | Views: 249648 | Answers: 133

**解决方法 / 社区答案**:
You can hold option and click a position in the current line to move your cursor to that position.

**参考链接**: https://apple.stackexchange.com/questions/5435/got-any-tips-or-tricks-for-terminal-in-mac-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/5435/got-any-tips-or-tricks-for-terminal-in-mac-os-x

#### 15. How can I configure Mac Terminal to have color ls output?

**故障现象**: How can I configure Mac Terminal to have color ls output?
**标签 / 来源**: Tags: macos, terminal | apple | 👍 397 | 💬 13 answers

**问题描述**:
Tags: macos, terminal | Score: 397 | Views: 336045 | Answers: 13

**解决方法 / 社区答案**:
Edit:

~/.bash_profile


or

~/.profile


and add the following line to simply enable color output via ls:

export CLICOLOR=1


To customize the coloring shown by ls you can optionally add this variable, LSCOLORS.

Examples


Default

export LSCOLORS=ExFxCxDxBxegedabagacad

You can use this if you are using a black background

export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx

If you'd like to mimic the colors of a typical Linux terminal:

export LSCOLORS=ExGxBxDxCxEgEdxbxgxcxd



Once you've add the above to either ~/.bash_profile or ~/.profile you can either logout/login or source the file in your shell, for eg:

$ . ~/.bash_profile


NOTE: If you need help in selecting colors to use you can use this online tool called LSCOLORS Generator.

**参考链接**: https://apple.stackexchange.com/questions/33677/how-can-i-configure-mac-terminal-to-have-color-ls-output

> 📎 来源 / Source: https://apple.stackexchange.com/questions/33677/how-can-i-configure-mac-terminal-to-have-color-ls-output

#### 16. What are the practical differences between Bash and Zsh?

**故障现象**: What are the practical differences between Bash and Zsh?
**标签 / 来源**: Tags: terminal, bash, zsh, macos | apple | 👍 389 | 💬 4 answers

**问题描述**:
Tags: terminal, bash, zsh, macos | Score: 389 | Views: 337246 | Answers: 4

**解决方法 / 社区答案**:
First, some important things:

Bash isn't going away. If you're already using bash, nothing will change for you. All that changes is that zsh will be the default login shell for new accounts, and even then, you can select bash instead.
Scripts are not affected. What changes is the shell for interactive use, i.e. the shell in terminals (and also a few other things that use the login shell, such as crontabs). If you have a script in a file with execution permissions, starting with a shebang line such as #!/bin/bash or #!/bin/sh or #!/usr/bin/env bash, it'll keep working exactly as before.
Zsh's syntax is not completely compatible with bash, but it's close. A lot of code will keep working, for example typical aliases and functions. The main differences are in interactive configuration features.

Now, assuming you're considering switching to zsh, which has been a possibility for years, here are the main differences you'll encounter. This is not an exhaustive list!
Main differences for interactive use
Configuration files: bash reads (mainly) .bashrc in non-login interactive shells (but macOS starts a login shell in terminals by default), .profile or .bash_profile in login shells, and .inputrc. Zsh reads (mainly) .zshrc (in all interactive shells) and .zprofile (in login shells). This means that none of your bash customizations will apply: you'll need to port them over. You can't just copy the files because many things will need tweaking.
Key bindings use completely different syntax. Bash uses .inputrc and the bind builtin to bind keys to readline commands. Zsh uses the bindkey builtin to bind keys to zle widgets. Most readline commands have a zsh equivalent, but it isn't always a perfect equivalence.
Speaking of key bindings, if you use Vi(m) as your in-terminal editor but not as your command line mode in the shell, you'll notice zsh defaults to vi editing mode (i.e. with command and insert modes) if EDITOR or VISUAL is set to vi or vim. bindkey -e switches to emacs mode (i.e. where you can always type directly).
Prompt: bash sets the prompt (mainly) from PS1 which contains backslash escapes. Zsh sets the prompt mainly from PS1 which contains percent escapes. Although the concepts are similar, the escape codes are completely different. The functionality of bash's PROMPT_COMMAND is available in zsh via the precmd and preexec hook functions. Zsh has more convenience mechanisms to build fancy prompts including a prompt theme mechanism.
The basic command line history mechanisms (navigation with Up/Down, search with Ctrl+R, history expansion with !! and friends, last argument recall with Alt+. or $_) work in the same way, but there are a lot of differences in the details, too many to list here. You can copy your .bash_history to .zsh_history if you haven't changed a shell option that changes the file format.
Completion: both shells default to a basic completion mode that mostly completes command and file names, and switch to a fancy mode by including bash_completion on bash or by running compinit in zsh. You'll find some commands that bash handles better and some that zsh handles better. Zsh is usually more precise, but sometimes gives up where bash does something that isn't correct but is sensible. To specify possible completions for a command, zsh has three mechanisms:

The “old” completion mechanism with compctl which you can forget about.
The “new” completion mechanism with compadd and lots of functions that begin with underscore and a powerful but complex user configuration mechanism.
An emulation to support bash completion functions which you can enable by running bashcompinit. The emulation isn't 100% perfect but it usually works.

Many of bash's shopt settings have a corresponding setopt in zsh.
Zsh doesn't treat # as a comment start on the command line by default, only in scripts (including .zshrc and such). To enable interactive comments, run setopt interactive_comments.
Main differences for scripting
(and for power users on the command line of course)
In bash, $foo takes the value of foo, splits it at whitespace characters, and for each whitespace-separated part, if it contains wildcard characters and matches an existing file, replaces the pattern by the list of matches. To just get the value of foo, you need &quot;$foo&quot;. The same applies to command substitution $(foo). In zsh, $foo is the value of foo and $(foo) is the output of foo minus its final newlines, with two exceptions. If a word becomes empty due to expanding empty unquoted variables, it's removed (e.g. a=; b=; printf &quot;%s\n&quot; one &quot;$a$b&quot; three $a$b five prints one, an empty line, three, five). The result of an unquoted command substitution is split at whitespace but the pieces don't undergo wildcard matching.
Bash arrays are indexed from 0 to (length-1). Zsh arrays are indexed from 1 to length. You can make 0-indexing the default with setopt ksh_arrays. Zsh requires fewer braces (unless ksh_arrays is enabled). For example, suppose a=(first second third &quot;&quot; last).




Functionality
Bash syntax
Idiomatic zsh syntax
Expansion




First element
${a[0]}
$a[1]
first


Second element
${a[1]}
$a[2]
second


Last element
${a[${#a[@]}-1]}
$a[-1]
last


Length
${#a[@]}
$#a
5


All the elements
&quot;${a[@]}&quot;
&quot;${a[@]}&quot; or &quot;${(@)a}&quot;
first second third (empty word) last


All the non-empty elements

$a
first second third last




Bash has extra wildcard patterns such as @(foo|bar) to match foo or bar, which are only enabled with shopt -s extglob. In zsh, you can enable these patterns with setopt ksh_glob, but there's also a simpler-to-type native syntax such as (foo|bar), some of which requires setopt extended_glob (do put that in your .zshrc, and it's on by default in completion functions). Zsh has **/ for recursive directory traversal (as does modern bash but not the bash 3.2 that ships with macOS).
In bash, by default, if a wildcard pattern doesn't match any file, it's left unchanged. In zsh, by default, you'll get an error, which is usually the safest setting. If you want to pass a wildcard parameter to a command, use quotes. You can switch to the bash behavior with setopt no_nomatch. You can make non-matching wildcard patterns expand to an empty list instead with setopt null_glob.
In bash, the right-hand side of a pipeline runs in a subshell. In zsh, it runs in the parent shell, so you can write things like somecommand | read output.
Some nice zsh features
Here are a few nice zsh features that bash doesn't have (at least not without some serious elbow grease). Once again, this is just a selection of the ones I consider the most useful.
Glob qualifiers allow matching files based on metadata such as their time stamp, their size, etc. They also allow tweaking the output. The syntax is rather cryptic, but it's extremely convenient. Here are a few examples:

foo*(.): only regular files matching foo* and symbolic links to regular files, not directories and other special files.
foo*(*.): only executable regular files matching foo*.
foo*(-.): only regular files matching foo*, not symbolic links and other special files.
foo*(-@): only dangling symbolic links matching foo*.
foo*(om): the files matching foo*, sorted by last modification date, most recent first. Note that if you pass this to ls, it'll do its own sorting. This is especially useful in…
foo*(om[1,10]): the 10 most recent files matching foo*, most recent first.
foo*(Lm+1): files matching foo* whose size is at least 1MB.
foo*(N): same as foo*, but if this doesn't match any file, produce an empty list regardless of the setting of the null_glob option (see above).
*(D): match all files including dot files (except . and ..).
foo/bar/*(:t) (using a history modifier): the files in foo/bar, but with only the base name of the file. E.g. if there is a foo/bar/qux.txt, it's expanded as qux.txt.
foo/bar/*(.:r): take regular files under foo/bar and remove the extension. E.g. foo/bar/qux.txt is expanded as foo/bar/qux.
foo*.odt(e\''REPLY=$REPLY:r.pdf'\'): take the list of files matching foo*.odt, and replace .odt by .pdf (regardless of whether the PDF file exists).

Here are a few useful zsh-specific wildcard patterns.

foo*.txt~foobar*: all .txt files whose name starts with foo but not foobar.
image&lt;-&gt;.jpg(n): all .jpg files whose base name is image followed by a number, e.g. image3.jpg and image22.jpg but not image-backup.jpg. The glob qualifier (n) causes the files to be listed in numerical order, i.e. image9.jpg comes before image10.jpg (you can make this the default even without -n with setopt numeric_glob_sort).

To mass-rename files, zsh provides a very convenient tool: the zmv function. Suggested for your .zshrc:
autoload zmv
alias zcp='zmv -C' zln='zmv -L'

Example:
zmv '(*).jpeg' '$1.jpg'
zmv '(*)-backup.(*)' 'backups/$1.$2'

Bash has a few ways to apply transformations when taking the value of a variable. Zsh has some of the same and many more.
Zsh has a number of little convenient features to change directories. Turn on setopt auto_cd to change to a directory when you type its name without having to type cd (bash also has this nowadays). You can use the two-argument form to cd to change to a directory whose name is close to the current directory. For example, if you're in /some/where/foo-old/deeply/nested/inside and you want to go to /some/where/foo-new/deeply/nested/inside, just type cd old new.
To assign a value to a variable, you of course write VARIABLE=VALUE. To edit the value of a variable interactively, just run vared VARIABLE.
Final advice
Zsh comes with a configuration interface that supports a few of the most common settings, including canned recipes for things like case-insensitive completion. To (re)run this interface (the first line is not needed if you're using a configuration file that was edited by zsh-newuser-install):
autoload -U zsh-newuser-install
zsh-newuser-install

Out of the box, with no configuration file at all, many of zsh's useful features are disabled for backward compatibility with 1990's versions. zsh-newuser-install suggests some recommended features to turn on.
There are many zsh configuration frameworks on the web (many of them are on Github). They can be a convenient way to get started with some powerful features. The flip side of the coin is they often lock you in doing things the way the author does, so sometimes they'll prevent you from doing things the way you want. Use them at your own risk.
The zsh manual has a lot of information, but it's often written in a way that's terse and hard to follow, and has few examples. Don't hesitate to search for explanations and examples online: if you only use the part of zsh that's easy to understand in the manual, you'll miss out. Two good resources are the zsh-users mailing list and Unix Stack Exchange.
An extensive collection of articles on switching to zsh on the mac can be found on scriptingosx.com and a useful Ruby script to bring your command history with you, can be found on Github.

**参考链接**: https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh

> 📎 来源 / Source: https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh

#### 17. How can I list my open network ports with netstat?

**故障现象**: How can I list my open network ports with netstat?
**标签 / 来源**: Tags: macos, network, command-line | apple | 👍 375 | 💬 7 answers

**问题描述**:
Tags: macos, network, command-line | Score: 375 | Views: 1062787 | Answers: 7

**解决方法 / 社区答案**:
netstat -anvp tcp | awk 'NR&lt;3 || /LISTEN/'
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)     rhiwat shiwat    pid   epid  state    options
tcp46      0      0  *.62981                *.*                    LISTEN      131072 131072  34548      0 0x0100 0x00000006
…


sudo lsof -PiTCP -sTCP:LISTEN
COMMAND     PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
BetterTou 34548 grgarside   20u  IPv4 0xa42a1d0ade5d3585      0t0  TCP *:62981 (LISTEN)
BetterTou 34548 grgarside   21u  IPv6 0xa42a1d0ad67f7a5d      0t0  TCP *:62981 (LISTEN)
…

**参考链接**: https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat

> 📎 来源 / Source: https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat

#### 18. How do I recompile Bash to avoid Shellshock (the remote exploit CVE-2014-6271 and CVE-2014-7169)?

**故障现象**: How do I recompile Bash to avoid Shellshock (the remote exploit CVE-2014-6271 and CVE-2014-7169)?
**标签 / 来源**: Tags: macos, security, bash | apple | 👍 371 | 💬 7 answers

**问题描述**:
Tags: macos, security, bash | Score: 371 | Views: 269147 | Answers: 7

**解决方法 / 社区答案**:
Status

Apple has released Bash security fixes for Shellshock and related vulnerabilities as "OS X bash Update 1.0". They can be installed through normal system update for people using OS X Mountain Lion v10.8.5 or OS X Mavericks v10.9.5 (they are included in Security Update 2014-005) and can also be installed manually. Official Apple fixes are also available for OS X Lion v10.7.5 and OS X Lion Server v10.7.5 but those are only available via manual download. The security fixes are available via different URLs based on the operating system version:


http://support.apple.com/kb/DL1769 - Mavericks (10.9.5 and above)
http://support.apple.com/kb/DL1768 - Mountain Lion (10.8.5)
http://support.apple.com/kb/DL1767 - Lion &amp; Lion Server (10.7.5)


(If new patches are released, put them here but please keep these existing ones as well for reference.)

The Apple patch takes care of Shellshock and several other vulnerabilities and is fine for most people. tl;dr people can stop reading here.

HOWEVER, the attention drawn to bash by the Shellshock bug has caused many researchers to take a hard look at bash and more and more (hard to exploit) vulnerabilities keep being found. If you are highly concerned about security (because maybe you are running OS X Server to host a publicly available web site) then you may want to (try to) keep up with the vulnerabilities and patches as they keep rolling in by compiling bash yourself. Otherwise, don't worry about it.

Look for Apple to release another update to bash some time in the future when the dust settles on finding further vulnerabilities. 



An official set of patches of bash itself for bash 3.2, patches 52, 53, and 54 (which correspond to Bash 4.3 patches 25, 26, and 27) are available which fix both CVE-2014-6271 and CVE-2014-7169, as well as the 'Game over' displayed below. This has been tested by me (@alblue) and the post has been updated accordingly (and then additional updates were made: see revision 41 for the post that stops at patch 54). 

Many additional vulnerabilities have been reported against bash. According to Michal Zalewski's post if you have patch 54 (and presumably Apple's official patch) "there's no point in obsessing about the status of these individual bugs, because they should no longer pose a security risk:"


CVE-2014-6271 - original RCE found by Stephane. Fixed by bash43-025
and corresponding Sep 24 entries for other versions.
CVE-2014-7169 - file creation / token consumption bug found by
Tavis. Fixed by bash43-026 &amp; co (Sep 26)
CVE-2014-7186 - a probably no-sec-risk 10+ here-doc crash found by
Florian and Todd. Fixed by bash43-028 &amp; co (Oct 1).
CVE-2014-7187 - a non-crashing, probably no-sec-risk off-by-one
found by Florian.  Fixed by bash43-028 &amp; co (Oct 1).
CVE-2014-6277 - uninitialized memory issue, almost certainly RCE
found by Michal Zalewski. No specific patch yet.
CVE-2014-6278 - command injection RCE found by Michal Zalewski. No specific patch yet.


It gets pretty confusing. Fortunately Chet Ramey, the official bash maintainer, posted a CVE to patch mapping. His post refers to patches for bash 4.3, I (@OldPro) have translated them to patches for bash 3.2, which is what is applicable to OS X. Also, since this post he has released patch 57, so I added that below:

 bash32-052      CVE-2014-6271                           2014-09-24
 bash32-053      CVE-2014-7169                           2014-09-26
 bash32-054      exported function namespace change      2014-09-27 ("Game Over")
 bash32-055      CVE-2014-7186/CVE-2014-7187             2014-10-01
 bash32-056      CVE-2014-6277                           2014-10-02
 bash32-057      CVE-2014-6278                           2014-10-05


See David A. Wheeler's post for a timeline and greater detail. 

@alblue posted build instructions through patch 55. I (@OldPro) added patch 56 and 57 to the instructions but have not tested it.

Testing for the original Vulnerability

You can determine if you are vulnerable to the original problem in CVE-2014-6271 by executing this test:

$ env x='() { :;}; echo vulnerable' bash -c 'echo hello'
bash: warning: x: ignoring function definition attempt
bash: error importing function definition for `x'
hello


The above output is an example of a non-vulnerable bash version. If you see the word vulnerable in the output of that command your bash is vulnerable and you should update. Below is a vulnerable version from OS X 10.8.5:



Testing for the new Vulnerability

There has been an update to the original post and Bash 3.2.52(1) is still vulnerable to a variation of the vulnerability, defined in CVE-2014-7169 

$ rm -f echo
$ env X='() { (a)=&gt;\' sh -c "echo date"; cat echo
sh: X: line 1: syntax error near unexpected token `='
sh: X: line 1: `'
sh: error importing function definition for `X'
Thu 25 Sep 2014 08:50:18 BST


The above output is an example of a vulnerable bash version. If you see a date in the output of that command your bash is vulnerable.

Disabling auto-imported functions to prevent "Game Over"

Researchers noted, without classifying it as a vulnerability, that a script could hijack a function in a subshell using auto-imported functions:

$ env ls="() { echo 'Game Over'; }" bash -c ls
Game over


The above code on an affected system would display Game Over instead of the directory listing you would expect from ls. Obviously, echo 'Game Over' could be replaced by any nefarious code you want. This became know as the "Game Over" bug.

Prior to the availability of patch 54, both NetBSD and FreeBSD disabled auto-importing bash functions by default, partly to prevent "Game Over" but mainly to contain any further errors in the parser (such as CVE-2014-7169) as they were continuing to be discovered, and added a new command line flag --import-functions to re-enable the old default behavior. I (@alblue) have prepared a patch (against 3.2.53) for others to use if they want to adopt this behaviour as well and have included it below. By default this patch is not enabled in the build script below. I (@OldPro) believe this patch is no longer necessary or a good idea, because it breaks backwards compatibility and the vulnerabilities it protects against are very well addressed by patch 54 and earlier patches, and enabling this unofficial patch prevents future patches from being applied. 

(Note to question editors; please do not enable this by default, as it is an unofficial patch.)

a0c5c4d66742fddd0a35001cb91798a5fbf8a2f5  import_functions.patch

The patch can be enabled by running export ADD_IMPORT_FUNCTIONS_PATCH=YES before running the build. Note that enabling this patch will disable patch 54 and any future patches because future patches cannot be guaranteed to be compatible with the unofficial patch.

Apple Patch has Game Over vulnerability, sort of

As pointed out by @ake_____ on twitter the official Apple patch is still vulnerable to environment clobbering of executables:

$ env '__BASH_FUNC&lt;ls&gt;()'="() { echo Game Over; }" bash -c ls
Game Over


Users should decide for themselves how important this is. I (@OldPro) think it is nothing to worry about because there is no known exploit for this behavior (it was not even given a CVE identifier) because in general unprivileged remote attackers cannot set the name of an environment variable and attackers with privileges cannot use this to gain privileges they do not already have (at least not without exploiting an additional vulnerabiltiy). 

To provide a little background, bash allows you to define functions, and furthermore allows you to export those functions to subshells via the export -f command. This used to be implemented by creating an environment variable with the same name as the function with its value set to the function definition. So

$ ls () { echo 'Game Over'; }
$ export -f ls
$ echo $ls
Game Over


This happened because export -f ls created an environment variable named ls. The "Game Over" vulnerability was that you could directly create this environment variable without having to first define the function, which meant if you could inject the right variable name you could hijack a command. Apple tried to fix this by making it hard to create a variable with the right name. The official bash patch 54 actually makes it impossible to create a variable with the right name by using variable names that include % which is a character not allowed in a variable name, effectively putting exported function definitions in a different, reserved namespace.

If none of the above makes sense to you, don't worry about it. You are fine with the Apple patch for now.

System Binaries

OS X 10.9.5 (the latest stable release at the moment) ships with Bash v3.2.51:

$ bash --version
GNU bash, version 3.2.51(1)-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.


You can obtain and recompile Bash as follows, providing that you have Xcode installed (and have run xcodebuild at least once before to accept the license):

$ # If you want to disable auto-imported functions, uncomment the following
$ # export ADD_IMPORT_FUNCTIONS_PATCH=YES
$ mkdir bash-fix
$ cd bash-fix
$ curl https://opensource.apple.com/tarballs/bash/bash-92.tar.gz | tar zxf -
$ cd bash-92/bash-3.2
$ curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-052 | patch -p0    
$ curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-053 | patch -p0  
$ # See note above about ADD_IMPORT_FUNCTIONS_PATCH
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] &amp;&amp; curl http://alblue.bandlem.com/import_functions.patch | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-054 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-055 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-056 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-057 | patch -p0
$ cd ..
$ # Note: DO NOT ADD SUDO TO XCODEBUILD HERE
$ xcodebuild
$ build/Release/bash --version # GNU bash, version 3.2.57-release
$ build/Release/sh --version   # GNU bash, version 3.2.57-release
$ sudo cp /bin/bash /bin/bash.old
$ sudo cp /bin/sh /bin/sh.old
$ sudo cp build/Release/bash /bin
$ sudo cp build/Release/sh /bin


(Note: you can run this by copy-and-pasting the above code block, going into Terminal and then running pbpaste | cut -c 2- | sh. Always take care when running random scripts from the internet though ...)

After this, the Bash version should be v3.2.57:

$ bash --version
GNU bash, version 3.2.57-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.


For security, and after testing, I recommend that you chmod -x the old versions to ensure they aren't re-used, or move them to a backup site.

$ sudo chmod a-x /bin/bash.old /bin/sh.old


Other answers have solutions for those using MacPorts or Homebrew; these don't fix the problem, they just install additional versions of Bash. Please see those answers if you want to upgrade those specifically.

Thanks

Thanks to Chet, who looks after bash, and has been making these patches available. Thanks to everyone else who has commented on this and improved it over time.

Now Apple has released the real fix, though this might still be useful. Because they only released a fix for Lion and up, and the official patch provides GNU bash, version 3.2.53(1)-release (x86_64-apple-darwin13), however, the Game over bug is still somewhat vulnerable. At this point, rebuilding your own version of Bash against 3.2.57 is probably more secure than relying on Apple's patch, unless you do it wrong.

**参考链接**: https://apple.stackexchange.com/questions/146849/how-do-i-recompile-bash-to-avoid-shellshock-the-remote-exploit-cve-2014-6271-an

> 📎 来源 / Source: https://apple.stackexchange.com/questions/146849/how-do-i-recompile-bash-to-avoid-shellshock-the-remote-exploit-cve-2014-6271-an

#### 19. How to combine two images into one on a Mac?

**故障现象**: How to combine two images into one on a Mac?
**标签 / 来源**: Tags: macos, software-recommendation, image-editing | apple | 👍 365 | 💬 19 answers

**问题描述**:
Tags: macos, software-recommendation, image-editing | Score: 365 | Views: 884014 | Answers: 19

**解决方法 / 社区答案**:
I often have to do this with images of plots of data.  I use the command line tools that come in the Imagemagick package; I think I installed it on my system with MacPorts. You could also choose to install with brew (brew install imagemagick).
The actual tool you want to use from Imagemagick is the convert tool.  If you have your two 320x428 images, say a.png and b.png, you can do
convert +append a.png b.png c.png

to create a new file, c.png, that has the a.png on the left and b.png on the right.  Alternatively, you append them vertically with -append (instead of +) and a.png will be on top of b.png.  With convert, you can do a ton of other things.  For example, you can switch to a different image format for the output
convert +append a.png b.jpg c.tif

This isn't a GUI application, but maybe some others might have a better solution.  Alternatively, you could put this in some sort of automator script.
2020-12-10：
I used it on 2020-12-10 and now the correct code is
convert +append a.png b.jpg +append c.tif

**参考链接**: https://apple.stackexchange.com/questions/52879/how-to-combine-two-images-into-one-on-a-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/52879/how-to-combine-two-images-into-one-on-a-mac

#### 20. How do I downgrade node or install a specific previous version using homebrew?

**故障现象**: How do I downgrade node or install a specific previous version using homebrew?
**标签 / 来源**: Tags: macos, homebrew | apple | 👍 362 | 💬 13 answers

**问题描述**:
Tags: macos, homebrew | Score: 362 | Views: 676196 | Answers: 13

**解决方法 / 社区答案**:
These days if you want to install a different version of node you do it this way:
First search for your desired package:
brew search node

This might give you the follow results:
heroku/brew/heroku-node ✔
node ✔
node@10
node_exporter
nodenv
libbitcoin-node
node-build
node@12 ✔
node@14 ✔
...

And then install the desired version:
brew install node@14

Also remember that you can install more than 1 node package at the same time, but you cannot have them available at the same time. So if you have the latest/generic node package already installed you need to unlink it first:
brew unlink node

And then you can link a different version:
brew link node@14

Sometimes it might be required to link them with the --force and --overwrite options:
brew link --force --overwrite node@14

However, when new node version comes out and you’ll update to it by running brew upgrade, the link will be removed and the most recent node version will be linked instead. To remedy that you might consider adding your desired node version to PATH instead (and restart the shell):
echo 'export PATH=&quot;/usr/local/opt/node@14/bin:$PATH&quot;' &gt;&gt; ~/.zshrc

(replace .zshrc with .bashrc or similar, depending on which $SHELL you use)

**参考链接**: https://apple.stackexchange.com/questions/171530/how-do-i-downgrade-node-or-install-a-specific-previous-version-using-homebrew

> 📎 来源 / Source: https://apple.stackexchange.com/questions/171530/how-do-i-downgrade-node-or-install-a-specific-previous-version-using-homebrew

#### 21. How can I disable animation when switching desktops in Lion?

**故障现象**: How can I disable animation when switching desktops in Lion?
**标签 / 来源**: Tags: macos, spaces | apple | 👍 352 | 💬 6 answers

**问题描述**:
Tags: macos, spaces | Score: 352 | Views: 135252 | Answers: 6

**解决方法 / 社区答案**:
I posted a bug on Radar#28495374 and here is the response from Apple:

Fixed in 10.12.  Go to Accessibility and Turn on Reduce Motion…
Please let us know whether the issue is resolved for you by updating your bug report.

**参考链接**: https://apple.stackexchange.com/questions/17929/how-can-i-disable-animation-when-switching-desktops-in-lion

> 📎 来源 / Source: https://apple.stackexchange.com/questions/17929/how-can-i-disable-animation-when-switching-desktops-in-lion

#### 22. How to change computer name so terminal displays it in Mac OS X Mountain Lion?

**故障现象**: How to change computer name so terminal displays it in Mac OS X Mountain Lion?
**标签 / 来源**: Tags: sharing, macos, hosts | apple | 👍 326 | 💬 8 answers

**问题描述**:
Tags: sharing, macos, hosts | Score: 326 | Views: 761810 | Answers: 8

**解决方法 / 社区答案**:
If you use:
sudo scutil --set HostName name-you-want

it will work a bit better. From the scutil(8) man page:

--get pref
    Retrieves the specified preference.  The current value will be
    reported on standard output.

    Supported preferences include:
          ComputerName   The user-friendly name for the system.
          LocalHostName  The local (Bonjour) host name.
          HostName       The name associated with hostname(1) and gethostname(3).

--set pref [newval]
    Updates the specified preference with the new value.  If the new value is not
    specified on the command line then it will be read from standard input.

    Supported preferences include: ComputerName LocalHostName HostName

    The --set option requires super-user access.

**参考链接**: https://apple.stackexchange.com/questions/66611/how-to-change-computer-name-so-terminal-displays-it-in-mac-os-x-mountain-lion

> 📎 来源 / Source: https://apple.stackexchange.com/questions/66611/how-to-change-computer-name-so-terminal-displays-it-in-mac-os-x-mountain-lion

#### 23. Can I get the CPU temperature and fan speed from the command line in OS X?

**故障现象**: Can I get the CPU temperature and fan speed from the command line in OS X?
**标签 / 来源**: Tags: macos, temperature, command-line, monitoring | apple | 👍 324 | 💬 14 answers

**问题描述**:
Tags: macos, temperature, command-line, monitoring | Score: 324 | Views: 574589 | Answers: 14

**解决方法 / 社区答案**:
Option #1) you may consider using inbuilt utility powermetrics to get the cpu and gpu temperature and lot more other details.
To get CPU temperature:
sudo powermetrics --samplers smc |grep -i &quot;CPU die temperature&quot;


To get GPU temperature:
sudo powermetrics --samplers smc |grep -i &quot;GPU die temperature&quot;

To get lot more details:
sudo powermetrics

This has been tested on macbook pro with macOS mojave.
Option #2)
Install Intel® Power Gadget officially provided by Intel from here
Intel® Power Gadget and then launch Intel Power Gadget from the launchpad.

Result Screen:

**参考链接**: https://apple.stackexchange.com/questions/54329/can-i-get-the-cpu-temperature-and-fan-speed-from-the-command-line-in-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/54329/can-i-get-the-cpu-temperature-and-fan-speed-from-the-command-line-in-os-x

#### 24. Hotkey to show hidden files and folders in File Open dialog?

**故障现象**: Hotkey to show hidden files and folders in File Open dialog?
**标签 / 来源**: Tags: macos | apple | 👍 323 | 💬 3 answers

**问题描述**:
Tags: macos | Score: 323 | Views: 200603 | Answers: 3

**解决方法 / 社区答案**:
⌘ CMD+⇧ SHIFT+. reveals hidden files in Finder and Open/Save dialogs.

If you are using an AZERTY keyboard, you'll need to press fn too, so ⇧ SHIFT is taken into consideration as you already need it to make the ..



You can also press ⌘ CMD+⇧ SHIFT+G and type the path to the hidden folder, just like in Terminal (⇥ TAB autocompletion also works).

Editing hidden files can be dangerous if you don't know what you're doing.

**参考链接**: https://apple.stackexchange.com/questions/186376/hotkey-to-show-hidden-files-and-folders-in-file-open-dialog

> 📎 来源 / Source: https://apple.stackexchange.com/questions/186376/hotkey-to-show-hidden-files-and-folders-in-file-open-dialog

#### 25. How to create a text file in a folder

**故障现象**: How to create a text file in a folder
**标签 / 来源**: Tags: macos, finder, file | apple | 👍 321 | 💬 32 answers

**问题描述**:
Tags: macos, finder, file | Score: 321 | Views: 609448 | Answers: 32

**解决方法 / 社区答案**:
You can also do this in Terminal. Go to the directory where you want to create the file, then run the following:

touch file.txt


Or redirect 'nothing' to a text file

&gt; file.txt

**参考链接**: https://apple.stackexchange.com/questions/84309/how-to-create-a-text-file-in-a-folder

> 📎 来源 / Source: https://apple.stackexchange.com/questions/84309/how-to-create-a-text-file-in-a-folder

#### 26. Applications Don&#39;t Show Up in Spotlight

**故障现象**: Applications Don&#39;t Show Up in Spotlight
**标签 / 来源**: Tags: macos, spotlight | apple | 👍 319 | 💬 7 answers

**问题描述**:
Tags: macos, spotlight | Score: 319 | Views: 141991 | Answers: 7

**解决方法 / 社区答案**:
Update Oct 1, 2021
In 10.12 (macOS Sierra) and newer, it appears to be enough to disable and reenable indexing:
sudo mdutil -a -i off
sudo mdutil -a -i on

Original Answer
Loading the metadata plist worked for me:
Turn off spotlight:
sudo mdutil -a -i off

Unload it:
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist

Load It:
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist

Turn on spotlight again:
sudo mdutil -a -i on

Now everything is being reindexed as expected.

**参考链接**: https://apple.stackexchange.com/questions/62715/applications-dont-show-up-in-spotlight

> 📎 来源 / Source: https://apple.stackexchange.com/questions/62715/applications-dont-show-up-in-spotlight

#### 27. What do I type to produce the command symbol (⌘) in Mac OS X?

**故障现象**: What do I type to produce the command symbol (⌘) in Mac OS X?
**标签 / 来源**: Tags: macos, internationalization, keyboard | apple | 👍 303 | 💬 17 answers

**问题描述**:
Tags: macos, internationalization, keyboard | Score: 303 | Views: 354805 | Answers: 17

**解决方法 / 社区答案**:
If you're just looking for the Unicode versions of Mac OS X keys, you can use this Apple support document to copy and paste them:

Mac keyboard shortcuts
https://support.apple.com/en-us/HT201236


⌘ Command (or Cmd)
⇧ Shift
⌥ Option (or Alt)
⌃ Control (or Ctrl)


More generally, Mac OS X provides a pane to insert special characters. You'll find it under Edit -&gt; Emoji and Symbols in any program that takes text input. The Command key symbol can be found by searching for it's name &quot;place of interest&quot;. To insert the character, double click it.


If you're really hardcore and are looking for a way to type the character by entering the Unicode hex code, this is possible:

Go into System Preferences -&gt; Keyboard -&gt; Input Sources, click &quot;+&quot;, scroll to &quot;others&quot;, select &quot;Unicode Hex Input&quot; and click &quot;Add&quot;


From the input source selector in the menu bar, select &quot;Unicode Hex Input&quot;


To enter a Unicode character, hold down option and type the 4-digit hex code for the character and it will be inserted. In this case, it would be option+2318.

**参考链接**: https://apple.stackexchange.com/questions/4074/what-do-i-type-to-produce-the-command-symbol-in-mac-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/4074/what-do-i-type-to-produce-the-command-symbol-in-mac-os-x

#### 28. How to Retrieve the Wi-Fi Password of a Connected Network on a Mac

**故障现象**: How to Retrieve the Wi-Fi Password of a Connected Network on a Mac
**标签 / 来源**: Tags: macos, macbook-pro, mac | apple | 👍 282 | 💬 5 answers

**问题描述**:
Tags: macos, macbook-pro, mac | Score: 282 | Views: 1562491 | Answers: 5

**解决方法 / 社区答案**:
If the password is stored, you can find it using the program Keychain Access.

If you open /Applications/Utilities/Keychain Access, it will show you a list of stored entries. If you click the Kind column header, it will sort by kind, go to the section where AirPort network passwords are stored. On Yosemite, you may have to select "Local Items" rather than "login" under Keychains in the upper left.

Double-click the name of the network you are using (if you don't know the name of the network, you can find it in the WiFi menulet (the concentric quarter circles toward the right side of your menu bar).



Check the Show password box, enter your system password, and click the Allow button.

That should show you the password for the wireless network you are on, if it is stored on your computer. If no such entry appears, it means the password is not stored on your computer.

Note that you can also use this technique to find saved passwords for websites or other passwords that you computer has stored but you have forgotten.

**参考链接**: https://apple.stackexchange.com/questions/56130/how-to-retrieve-the-wi-fi-password-of-a-connected-network-on-a-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/56130/how-to-retrieve-the-wi-fi-password-of-a-connected-network-on-a-mac

#### 29. &quot;File Open&quot; dialog is missing sidebar items

**故障现象**: &quot;File Open&quot; dialog is missing sidebar items
**标签 / 来源**: Tags: finder, macos, sidebar | apple | 👍 280 | 💬 7 answers

**问题描述**:
Tags: finder, macos, sidebar | Score: 280 | Views: 132876 | Answers: 7

**解决方法 / 社区答案**:
Go to your user library in Finder. Hold down ⌥ while opening the Go menu and click Library. 
Navigate to the Preferences folder.
Remove any files that are or contain com.apple.finder.plist. (The removal of those files will very likely reset your Favourites list in Finder.)
Restart or log out and log back in again then empty the trash and try again. 

Restarting might not be necessary. As madpoet says:


  You can also relaunch Finder if you don't want to reboot or log out. Right click on Finder icon while you're pressing ⌥ and you'll see the Relaunch option there.
  
  





Alternatively, you can use this Bash oneliner by Christophe Marois:

cd ~/Library/Preferences &amp;&amp; sudo find com.apple.finder.plist* -exec rm {} \; &amp;&amp; killall Finder

**参考链接**: https://apple.stackexchange.com/questions/208205/file-open-dialog-is-missing-sidebar-items

> 📎 来源 / Source: https://apple.stackexchange.com/questions/208205/file-open-dialog-is-missing-sidebar-items

#### 30. Where can I find the installed package path via brew

**故障现象**: Where can I find the installed package path via brew
**标签 / 来源**: Tags: macos, homebrew | apple | 👍 279 | 💬 15 answers

**问题描述**:
Tags: macos, homebrew | Score: 279 | Views: 651616 | Answers: 15

**解决方法 / 社区答案**:
Use the following to show the installation path of a package:

brew info hping


Example output:

pcre: stable 8.35 (bottled)
http://www.pcre.org/
/usr/local/Cellar/pcre/8.35 (146 files, 5.8M) *
  Poured from bottle
From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/pcre.rb
==&gt; Options
--universal
    Build a universal binary

**参考链接**: https://apple.stackexchange.com/questions/145437/where-can-i-find-the-installed-package-path-via-brew

> 📎 来源 / Source: https://apple.stackexchange.com/questions/145437/where-can-i-find-the-installed-package-path-via-brew

#### 31. How to replace Mac OS X utilities with GNU core utilities?

**故障现象**: How to replace Mac OS X utilities with GNU core utilities?
**标签 / 来源**: Tags: macos, command-line, unix, utilities | apple | 👍 278 | 💬 7 answers

**问题描述**:
Tags: macos, command-line, unix, utilities | Score: 278 | Views: 215463 | Answers: 7

**解决方法 / 社区答案**:
This adds symlinks for GNU utilities with g prefix to /usr/local/bin/:

brew install coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent gnu-getopt grep


See brew search gnu for other packages. If you want to use the commands without a g prefix add for example /usr/local/opt/coreutils/libexec/gnubin before other directories on your PATH.

$ brew info coreutils
coreutils: stable 8.21
http://www.gnu.org/software/coreutils
Depends on: xz
/usr/local/Cellar/coreutils/8.20 (208 files, 9.4M)
/usr/local/Cellar/coreutils/8.21 (210 files, 9.6M) *
https://github.com/mxcl/homebrew/commits/master/Library/Formula/coreutils.rb
==&gt; Caveats
All commands have been installed with the prefix 'g'.

If you really need to use these commands with their normal names, you
can add a "gnubin" directory to your PATH from your bashrc like:

    PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

Additionally, you can access their man pages with normal names if you add
the "gnuman" directory to your MANPATH from your bashrc as well:

    MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"

**参考链接**: https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

> 📎 来源 / Source: https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

#### 32. Why are dot underscore ._ files created, and how can I avoid them?

**故障现象**: Why are dot underscore ._ files created, and how can I avoid them?
**标签 / 来源**: Tags: macos, file | apple | 👍 275 | 💬 14 answers

**问题描述**:
Tags: macos, file | Score: 275 | Views: 394183 | Answers: 14

**解决方法 / 社区答案**:
You can't avoid them (but see the dot_clean answer by Saeid Zebardast --they can be removed from a directory if that is what you need).  They're created to store file information that would otherwise go into an extended attribute on HFS+ (Apple native) or Unix/UFS volumes; in earlier Mac OS this would be the resource fork.  Finder file operations will create them automatically to store the icon information, plus Time Machine stores some information in them so if you copy a file backed up via TM it will have that information copied as well.

(This is nothing new; I've noticed that XP and later leave various turds around as well, although not quite as many.)

**参考链接**: https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them

> 📎 来源 / Source: https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them

#### 33. Can I open files in TextEdit from the Terminal in Mac OS X?

**故障现象**: Can I open files in TextEdit from the Terminal in Mac OS X?
**标签 / 来源**: Tags: macos, command-line, terminal, textedit | apple | 👍 273 | 💬 5 answers

**问题描述**:
Tags: macos, command-line, terminal, textedit | Score: 273 | Views: 538175 | Answers: 5

**解决方法 / 社区答案**:
open -a TextEdit filename should do the trick.
The -a flag specifies any application you want, so it's applicable to any number of situations, including ones where TextEdit isn't the default editor.
Other relevant options

-t  opens in the default editor (i.e. if you use BBEdit, TextMate, etc.)
-e will open the file specifically in TextEdit

**参考链接**: https://apple.stackexchange.com/questions/25844/can-i-open-files-in-textedit-from-the-terminal-in-mac-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/25844/can-i-open-files-in-textedit-from-the-terminal-in-mac-os-x

#### 34. Can Touch ID on Mac authenticate sudo in Terminal?

**故障现象**: Can Touch ID on Mac authenticate sudo in Terminal?
**标签 / 来源**: Tags: macos, mac, password, sudo, touch-id | apple | 👍 272 | 💬 14 answers

**问题描述**:
Tags: macos, mac, password, sudo, touch-id | Score: 272 | Views: 118535 | Answers: 14

**解决方法 / 社区答案**:
To allow TouchID on your Mac to authenticate you for sudo access instead of a password you need to do the following.

Open Terminal

Switch to the root user with sudo su -

Edit the /etc/pam.d/sudo file with a command-line editor such as vim or nano

The contents of this file should look like one of the following examples:


# sudo: auth account password session
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so



# sudo: auth account password session
auth       sufficient     pam_smartcard.so
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so




You need to add an additional auth line to the top so it now looks like this:
# sudo: auth account password session
auth       sufficient     pam_tid.so
auth       sufficient     pam_smartcard.so
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so


Save the file. (Note: this file is normally read-only so saving your changes may require you to force the save, e.g. vim will require you to use wq! when saving)

Also note that pam_smartcard.so may not be present on older MacOS versions.

Exit from the root user or start a new terminal session.

Try to use sudo, and you should be prompted to authenticate with TouchID as shown below.


If you click 'Cancel,' you can just enter your password at the terminal prompt. If you click 'Use Password' you can enter your password in the dialog box.

If you SSH into your machine it will fall back to just use your password, since you can't send your TouchID fingerprints over SSH.


Note:
See answer by user Pierz below if you're using iTerm, as there's a setting you need to explicitly change to enable this feature.
Note:
Recent MacOS updates may remove the entry. If TouchID stops working for sudo then check if the entry was removed and add it back in, following these instructions again.

**参考链接**: https://apple.stackexchange.com/questions/259093/can-touch-id-on-mac-authenticate-sudo-in-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/259093/can-touch-id-on-mac-authenticate-sudo-in-terminal

#### 35. How can I manually delete old backups to free space for Time Machine?

**故障现象**: How can I manually delete old backups to free space for Time Machine?
**标签 / 来源**: Tags: macos, time-machine, backup, time-capsule, maintenance | apple | 👍 266 | 💬 8 answers

**问题描述**:
Tags: macos, time-machine, backup, time-capsule, maintenance | Score: 266 | Views: 754833 | Answers: 8

**解决方法 / 社区答案**:
Be careful with sudo and making sure you pick the correct Mac's files since there is no undo or confirmation of the following command:
sudo tmutil delete /Volumes/drive_name/Backups.backupdb/old_mac_name

The sudo command needs your password (and it won't echo to the screen, so just type it and pause to be sure you're dating the correct files before pressing enter). If you want to be safer, you can pick one snapshot to delete first to be sure the command works as intended. This is nice since it could take hours to clean up some larger backup sets and you want to leave the Mac confident it's deleting the correct information store.
You can use the tmutil tool to delete backups one by one.
sudo tmutil delete /Volumes/drive_name/Backups.backupdb/mac_name/YYYY-MM-DD-hhmmss

Since tmutil was introduced with Lion, this will not work on earlier OS versions.
If you want to get the current directory of backups (there can be multiple destinations defined and only one will be &quot;current&quot;)
sudo tmutil machinedirectory

If you back up to a network share, you may have sparse bundle storage and if so, that needs to be compacted as well.
sudo hdiutil compact /Volumes/drive_name/Backups.backupdb/mac_name.sparsebundle

**参考链接**: https://apple.stackexchange.com/questions/39287/how-can-i-manually-delete-old-backups-to-free-space-for-time-machine

> 📎 来源 / Source: https://apple.stackexchange.com/questions/39287/how-can-i-manually-delete-old-backups-to-free-space-for-time-machine

#### 36. What is the &quot;rootless&quot; feature in El Capitan, really?

**故障现象**: What is the &quot;rootless&quot; feature in El Capitan, really?
**标签 / 来源**: Tags: macos, unix, root, sip | apple | 👍 265 | 💬 3 answers

**问题描述**:
Tags: macos, unix, root, sip | Score: 265 | Views: 186445 | Answers: 3

**解决方法 / 社区答案**:
First: the name &quot;rootless&quot; is misleading, since there's still a root account, and you can still access it (the official name, &quot;System Integrity Protection&quot;, is more accurate). What it really does is limit the power of the root account, so that even if you become root, you don't have full control over the system. Essentially, the idea is that it's too easy for malware to get root access (e.g. by presenting an auth dialog to the user, which will cause the user to reflexively enter the admin password). SIP adds another layer of protection, which malware can't penetrate even if it gets root. The bad part of this, of course, it that it must also apply to things you're doing intentionally. But the restrictions it places on root aren't that bad; they don't prevent most &quot;normal&quot; system customization.
Here's what it restricts, even from root:

You can't modify anything in /System, /bin, /sbin, or /usr (except /usr/local); or any of the built-in apps and utilities. Only Installer and software update can modify these areas, and even they only do it when installing Apple-signed packages. But since normal OS X-style customizations go in /Library (or ~/Library, or /Applications), and unix-style customizations (e.g. Homebrew) go in /usr/local (or sometimes /etc or /opt), this shouldn't be a big deal. It also prevents block-level writes to the startup disk, so you can't bypass it that way.
The full list of restricted directories (and exceptions like /usr/local and a few others) is in /System/Library/Sandbox/rootless.conf. Of course, this file is itself in a restricted area.
When you upgrade to El Capitan, it moves any &quot;unauthorized&quot; files from restricted areas to /Library/SystemMigration/History/Migration-(some UUID)/QuarantineRoot/.

You can't attach to system processes (e.g. those running from those system locations) for things like debugging (or changing what dynamic libraries they load, or some other things). Again, not too much of a big deal; developers can still debug their own programs.
This does block some significant things like injecting code into the built-in Apple apps (notably the Finder). It also means that dtrace-based tools for system monitoring (e.g. opensnoop) will not be able to monitor &amp; report on many system processes.

You can't load kernel extensions (kexts) unless they're properly signed (i.e. by Apple or an Apple-approved developer). Note that this replaces the old system for enforcing kext signing (and the old ways of bypassing it). But since v10.10.4 Apple has had a way to enable trim support for third-party SSDs, the #1 reason to use unsigned kexts has gone away.

Starting in Sierra (10.12), some launchd configuration settings cannot be changed (for example, some launch daemons cannot be unloaded).

Starting in Mojave (10.14), access to users' personal information (email, contacts, etc) is restricted to apps that the user has approved to access that info. This is generally considered a separate feature (called Personal Information Protection, or TCC), but it's based on SIP and disabling SIP disables it as well. See: &quot;What and how does macOS Mojave implement to restrict applications access to personal data?&quot;

Starting in Catalina (10.15), protection of most system files is strengthened by storing them on a separate read-only volume. This is not strictly part of SIP, and is not disabled by disabling SIP. See: WWDC presentation on &quot;What's New in Apple [Catalina] File Systems&quot; and &quot;What's /System/Volumes/Data?&quot;.

Starting in Big Sur (11.x), the read-only system volume is now a &quot;Sealed System Volume&quot; (a mounted snapshot rather than a regular volume), so making changes to it is even more complicated. See: the Eclectic Light Company article &quot;Big Sur boot volume layout&quot;.


If you don't want these restrictions -- either because you want to modify your system beyond what this allows, or because you're developing &amp; debugging something like kexts that aren't practical under these restrictions, you can turn SIP off. Currently this requires rebooting into recovery mode and running the command csrutil disable (and you can similarly re-enable it with csrutil enable).
Modifying the system volume in Catalina requires disabling SIP, then mounting the volume with write access (and then rebooting and turning SIP back on is recommended). In Big Sur, additional steps are required to disable authentication of the system volume before changes, and afterward create a new snapshot.
You can also selectively disable parts of SIP. For example, csrutil enable --without kext will disable SIP's kernel extension restriction, but leave its other protections in place.
But please stop and think before disabling SIP, even temporarily or partially: do you really need to disable it, or is there a better (SIP-compliant) way to do what you want? Do you really need to modify something in /System/Library or /bin or whatever, or could it go in a better place like /Library or /usr/local/bin etc? SIP may &quot;feel&quot; constraining if you aren't used to it, and there are some legitimate reasons to disable it, but a lot of what it enforces it really just best practice anyway.
To underscore the importance of leaving as much of SIP enabled as much of the time as possible, consider the events of September 23, 2019. Google released an update to Chrome that tried to replace the symbolic link from /var to /private/var. On most systems, SIP blocked this and there were no bad effects. On systems with SIP disabled, it rendered macOS broken and unbootable. The most common reason for disabling SIP was to load unapproved (/improperly signed) kernel extensions (specifically video drivers); if they'd only disabled the kext restriction, they would not have been affected. See the official Google support thread, a superuser Q&amp;A on it, and an Ars Technica article.
References and further info: WWDC presentation on &quot;Security and Your Apps&quot;, a good explanation by Eldad Eilam on quora.com, the Ars Technica review of El Capitan, and an Apple support article on SIP, and a deep dive by Rich Trouton (who also posted an answer to this question).

**参考链接**: https://apple.stackexchange.com/questions/193368/what-is-the-rootless-feature-in-el-capitan-really

> 📎 来源 / Source: https://apple.stackexchange.com/questions/193368/what-is-the-rootless-feature-in-el-capitan-really

#### 37. How can I make Safari show the URL when I hover over a link?

**故障现象**: How can I make Safari show the URL when I hover over a link?
**标签 / 来源**: Tags: macos, safari | apple | 👍 261 | 💬 3 answers

**问题描述**:
Tags: macos, safari | Score: 261 | Views: 126089 | Answers: 3

**解决方法 / 社区答案**:
There are two options. One is a setting, and the other is a workaround.

Here are instructions on how to toggle the setting using the Menu Bar:


Go into the View menu.
Select "Show status bar".
Now, there will be a URL that pops up when you hover over a link, and also tells you if it's going to be in a new tab:




You can also press ⌘ + / to toggle this setting at ease.

The second option is a workaround for when you drag links. Here's how to get this feature to appear:


Click and drag the link out of where it will originally appear.
At your mouse will be a small box telling you the title of the new window and its URL, although it may be shortened.
You can also drag the link to the plus sign in your tab list, out of the window, or in a folder/the desktop to open that URL in a new tab, new window or save it to your computer, respectively.

**参考链接**: https://apple.stackexchange.com/questions/16759/how-can-i-make-safari-show-the-url-when-i-hover-over-a-link

> 📎 来源 / Source: https://apple.stackexchange.com/questions/16759/how-can-i-make-safari-show-the-url-when-i-hover-over-a-link

#### 38. Is there a keyboard shortcut to move a window from one monitor to another?

**故障现象**: Is there a keyboard shortcut to move a window from one monitor to another?
**标签 / 来源**: Tags: macos, keyboard, display, window-manager | apple | 👍 258 | 💬 18 answers

**问题描述**:
Tags: macos, keyboard, display, window-manager | Score: 258 | Views: 419833 | Answers: 18

**解决方法 / 社区答案**:
There is yet another option that's completely free and requires no third-party app. Be aware that I've only tested this on MacOS latest version Catalina (as of now). For other OS versions see Create keyboard shortcuts for apps on Mac

Go to System Preferences
Select Keyboard and then the Shortcuts tab
Then on the list that appears select App Shortcuts
Add new shortcuts like this:

Click on the plus sign to add a new one, the Menu Title field has to match exactly the text that appears on the Window menu in every application: &quot;Move to DISPLAY NAME&quot; (To find the text just open the Window menu on any application)
Finally on the Keyboard Shortcut field enter the shortcut you'd like to use
Add as many shortcuts as you need to move any window between your displays!

**参考链接**: https://apple.stackexchange.com/questions/28569/is-there-a-keyboard-shortcut-to-move-a-window-from-one-monitor-to-another

> 📎 来源 / Source: https://apple.stackexchange.com/questions/28569/is-there-a-keyboard-shortcut-to-move-a-window-from-one-monitor-to-another

#### 39. Make the green full screen window icon on Yosemite maximize windows

**故障现象**: Make the green full screen window icon on Yosemite maximize windows
**标签 / 来源**: Tags: macos, fullscreen | apple | 👍 249 | 💬 7 answers

**问题描述**:
Tags: macos, fullscreen | Score: 249 | Views: 136963 | Answers: 7

**解决方法 / 社区答案**:
As the below mentioned solution is application-based (i.e. only works for apps like Google Chrome), another way to approach this problem is to ignore the maximize button entirely and to install the open source app spectacle which offers the keyboard shortcut:

⌘ + ⌥ + F

It also has some other nice features, too. And it works for all apps.



In order to maximize the window so that it fills the visible window content, use:

⌥ + Click on green icon

In order to maximize the window both in width and height to the current desktop for applications like Google Chrome use:

⌥ + ⇧ + Click on green icon

You notice the change of behaviour of the button in the way it changes its content from two the arrows to a plus sign.

**参考链接**: https://apple.stackexchange.com/questions/139884/make-the-green-full-screen-window-icon-on-yosemite-maximize-windows

> 📎 来源 / Source: https://apple.stackexchange.com/questions/139884/make-the-green-full-screen-window-icon-on-yosemite-maximize-windows

#### 40. macOS Sierra doesn’t seem to remember SSH keys between reboots

**故障现象**: macOS Sierra doesn’t seem to remember SSH keys between reboots
**标签 / 来源**: Tags: terminal, password, ssh, macos | apple | 👍 230 | 💬 11 answers

**问题描述**:
Tags: terminal, password, ssh, macos | Score: 230 | Views: 175526 | Answers: 11

**解决方法 / 社区答案**:
As of macOS Sierra 10.12.2 Apple added an ssh_config option called UseKeychain which allows a 'proper' resolution to the problem. Add the following to your ~/.ssh/config file:
Host *
   AddKeysToAgent yes
   UseKeychain yes     

From the ssh_config man page on 10.12.2:

UseKeychain
On macOS, specifies whether the system should search for passphrases in the user's keychain when attempting to use a particular key. When the passphrase is provided by the user, this option also specifies whether the passphrase should be stored into the keychain once it has been verified to be correct.  The argument must be 'yes' or 'no'.  The default is 'no'.

**参考链接**: https://apple.stackexchange.com/questions/254468/macos-sierra-doesn-t-seem-to-remember-ssh-keys-between-reboots

> 📎 来源 / Source: https://apple.stackexchange.com/questions/254468/macos-sierra-doesn-t-seem-to-remember-ssh-keys-between-reboots

#### 41. How can I rename Desktops / Spaces in macOS?

**故障现象**: How can I rename Desktops / Spaces in macOS?
**标签 / 来源**: Tags: macos, high-sierra, spaces | apple | 👍 229 | 💬 21 answers

**问题描述**:
Tags: macos, high-sierra, spaces | Score: 229 | Views: 262533 | Answers: 21

**解决方法 / 社区答案**:
Refer to the original page for detailed solutions and community answers.

**参考链接**: https://apple.stackexchange.com/questions/211954/how-can-i-rename-desktops-spaces-in-macos

> 📎 来源 / Source: https://apple.stackexchange.com/questions/211954/how-can-i-rename-desktops-spaces-in-macos

#### 42. Keyboard shortcut for restoring applications from the Mac OS X Dock?

**故障现象**: Keyboard shortcut for restoring applications from the Mac OS X Dock?
**标签 / 来源**: Tags: macos, keyboard | apple | 👍 225 | 💬 11 answers

**问题描述**:
Tags: macos, keyboard | Score: 225 | Views: 117988 | Answers: 11

**解决方法 / 社区答案**:
Command + Tab until you get the app's icon.
Before releasing the Command key, press and hold the Option key.





You must switch to another app and let it take focus first. In other words, you can't just Command + Tab to another app and before actually selecting that app (by releasing the Command and Tab keys), switch right back to your minimized app, which you might attempt to do if you minimized it by accident or just simply changed your mind shortly after minimizing.
Both the Command and left Option keys must be pressed on the same side (left or right) of the keyboard.

**参考链接**: https://apple.stackexchange.com/questions/55432/keyboard-shortcut-for-restoring-applications-from-the-mac-os-x-dock

> 📎 来源 / Source: https://apple.stackexchange.com/questions/55432/keyboard-shortcut-for-restoring-applications-from-the-mac-os-x-dock

#### 43. How do I run a .sh or .command file in Terminal

**故障现象**: How do I run a .sh or .command file in Terminal
**标签 / 来源**: Tags: macos, terminal, command-line, bash | apple | 👍 224 | 💬 6 answers

**问题描述**:
Tags: macos, terminal, command-line, bash | Score: 224 | Views: 1264164 | Answers: 6

**解决方法 / 社区答案**:
Open Terminal, type in sh /path/to/file and press enter. 

Faster is to type sh and a space and then drag the file to the window and release the icon anywhere on the window.

**参考链接**: https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal

#### 44. How do I combine two or more images to get a single pdf file?

**故障现象**: How do I combine two or more images to get a single pdf file?
**标签 / 来源**: Tags: pdf, graphics, macos | apple | 👍 222 | 💬 8 answers

**问题描述**:
Tags: pdf, graphics, macos | Score: 222 | Views: 1502201 | Answers: 8

**解决方法 / 社区答案**:
Here are the steps to save multiple images in Preview into a single multi-page PDF.

Select all of the images you want in your PDF, right-click and choose open with Preview

In Preview's Sidebar drag the images into the order you want them to appear in your PDF

Select/highlight all the images to be included in the PDF document; otherwise only a single image may end up the PDF document

Then from the &quot;File&quot; menu choose &quot;Export Selected Images&quot; (or &quot;Export as PDF...&quot; in recent OS X versions) and then &quot;PDF &gt; Save as PDF&quot;

**参考链接**: https://apple.stackexchange.com/questions/11163/how-do-i-combine-two-or-more-images-to-get-a-single-pdf-file

> 📎 来源 / Source: https://apple.stackexchange.com/questions/11163/how-do-i-combine-two-or-more-images-to-get-a-single-pdf-file

#### 45. Suppressing &quot;The default interactive shell is now zsh&quot; message in macOS Catalina

**故障现象**: Suppressing &quot;The default interactive shell is now zsh&quot; message in macOS Catalina
**标签 / 来源**: Tags: terminal, command-line, macos, bash | apple | 👍 216 | 💬 5 answers

**问题描述**:
Tags: terminal, command-line, macos, bash | Score: 216 | Views: 100044 | Answers: 5

**解决方法 / 社区答案**:
I found the solution on reddit. The solution is also mentioned in the &quot;How to use a different shell without changing the default&quot; section of the Apple support article mentioned in the bash warning: https://support.apple.com/en-us/HT208050/.
Add:
export BASH_SILENCE_DEPRECATION_WARNING=1

to $HOME/.bash_profile, $HOME/.profile or $HOME/.bashrc and restart iTerm. After that, the warning message will be gone.

**参考链接**: https://apple.stackexchange.com/questions/371997/suppressing-the-default-interactive-shell-is-now-zsh-message-in-macos-catalina

> 📎 来源 / Source: https://apple.stackexchange.com/questions/371997/suppressing-the-default-interactive-shell-is-now-zsh-message-in-macos-catalina

#### 46. I included emoji in my password and now I can&#39;t log in to my Account on Yosemite

**故障现象**: I included emoji in my password and now I can&#39;t log in to my Account on Yosemite
**标签 / 来源**: Tags: macos, keyboard, password, filevault, emoji | apple | 👍 213 | 💬 8 answers

**问题描述**:
Tags: macos, keyboard, password, filevault, emoji | Score: 213 | Views: 96836 | Answers: 8

**解决方法 / 社区答案**:
If you have "Other Input Sources" available at the top right of your login screen, select the one called Unicode Hex Input.  This can be used to input emoji (or any other character) into the password field, as long as you know the Unicode Hex number of the character.  This number can be found in the Character Viewer or on the internet.

Some items you find in the  "emoji" category have Unicode hex numbers with just 4 characters, such as Airplane U+2708 ✈.  With the Unicode Hex Input keyboard, you input this by holding down the Option key while you type 2708.  

Other emoji have Unicode hex numbers with 5 characters, such as Grinning Face U+1F600 😀.  For these you need to find the two corresponding UTF-16 Hex codes (sometimes called "surrogates") by consulting Character Viewer or using an internet source like fileformat.info.  For 1F600 these are D83D and DE00.  You can input 1F600 by holding down the option key while typing D83DDE00.  You may see two dots in the field, but it is still just one character.

**参考链接**: https://apple.stackexchange.com/questions/202143/i-included-emoji-in-my-password-and-now-i-cant-log-in-to-my-account-on-yosemite

> 📎 来源 / Source: https://apple.stackexchange.com/questions/202143/i-included-emoji-in-my-password-and-now-i-cant-log-in-to-my-account-on-yosemite

#### 47. List USB devices on OSX command line

**故障现象**: List USB devices on OSX command line
**标签 / 来源**: Tags: macos, usb | apple | 👍 212 | 💬 2 answers

**问题描述**:
Tags: macos, usb | Score: 212 | Views: 565191 | Answers: 2

**解决方法 / 社区答案**:
In addition to system_profiler SPUSBDataType (suggested by @kjs), you can also use ioreg -p IOUSB:

$ ioreg -p IOUSB 
+-o Root  &lt;class IORegistryEntry, id 0x100000100, retain 10&gt;
  +-o EHCI Root Hub Simulation@1A,7  &lt;class IOUSBRootHubDevice, id 0x100000227,$
  | +-o HubDevice@fa100000  &lt;class IOUSBHubDevice, id 0x10000027a, registered, $
  | | +-o Apple Internal Keyboard / Trackpad@fa120000  &lt;class IOUSBDevice, id 0$
  | | +-o BRCM2070 Hub@fa110000  &lt;class IOUSBHubDevice, id 0x1000002b4, registe$
  | |   +-o Bluetooth USB Host Controller@fa113000  &lt;class IOUSBDevice, id 0x10$
  | +-o FaceTime HD Camera (Built-in)@fa200000  &lt;class IOUSBDevice, id 0x100000$
  +-o EHCI Root Hub Simulation@1D,7  &lt;class IOUSBRootHubDevice, id 0x100000228,$
    +-o HubDevice@fd100000  &lt;class IOUSBHubDevice, id 0x10000027b, registered, $
      +-o IR Receiver@fd110000  &lt;class IOUSBDevice, id 0x100000288, registered,$


By default it clips to the window's width (80 chars in the example above), so you may want to add -w0 to get a full-width display. Also, adding -l will show details (probably more than you need) about each of the devices:

$ ioreg -p IOUSB -w0 -l
    +-o Root  &lt;class IORegistryEntry, id 0x100000100, retain 10&gt;
  | {
  |   "IOKitBuildVersion" = "Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64"
  |   "OS Build Version" = "14B25"
  |   "OSKernelCPUSubtype" = 3
  |   "OSKernelCPUType" = 16777223
  |   "OSPrelinkKextCount" = 185
  |   "IOConsoleLocked" = No
  |   "IORegistryPlanes" = {"IOACPIPlane"="IOACPIPlane","IOPower"="IOPower","IODeviceTree"="IODeviceTree","IOService"="IOService","IOUSB"="IOUSB","IOFireWire"="IOFireWire"}
[...etc...]


[EDIT]: If you just want the device names, you can filter the basic list to trim the junk:

$ ioreg -p IOUSB -w0 | sed 's/[^o]*o //; s/@.*$//' | grep -v '^Root.*'
EHCI Root Hub Simulation
HubDevice
Apple Internal Keyboard / Trackpad
BRCM2070 Hub
Bluetooth USB Host Controller
FaceTime HD Camera (Built-in)
EHCI Root Hub Simulation
HubDevice
IR Receiver

**参考链接**: https://apple.stackexchange.com/questions/170105/list-usb-devices-on-osx-command-line

> 📎 来源 / Source: https://apple.stackexchange.com/questions/170105/list-usb-devices-on-osx-command-line

#### 48. Why is it not possible to use the &quot;cut&quot; command to manipulate a file in the Finder?

**故障现象**: Why is it not possible to use the &quot;cut&quot; command to manipulate a file in the Finder?
**标签 / 来源**: Tags: macos, finder, switching, contextual-menu | apple | 👍 212 | 💬 12 answers

**问题描述**:
Tags: macos, finder, switching, contextual-menu | Score: 212 | Views: 200052 | Answers: 12

**解决方法 / 社区答案**:
Keyboard method: Cmd-C then Opt-Cmd-V does the cut&amp;paste for files on Mac. 

Mouse method: Drag the file from one folder to the parent of the target folder (ie, if moving to Documents:Financial, drag to Documents). Hover on the parent folder for a few seconds, and it will spring open. Then you can continue dragging the file to the target folder. (note, the mouse method may result in very long hover times, if you're dragging a huge number of files, eg 1,000 files)

Menu method: It's not part of the Apple menu system to 'cut' files.  The menu Cut option is grayed out, and becomes enabled when text is selected.  But not files. Here is an in-depth discussion on Apple's discussion forum.

**参考链接**: https://apple.stackexchange.com/questions/12391/why-is-it-not-possible-to-use-the-cut-command-to-manipulate-a-file-in-the-find

> 📎 来源 / Source: https://apple.stackexchange.com/questions/12391/why-is-it-not-possible-to-use-the-cut-command-to-manipulate-a-file-in-the-find

#### 49. Is it safe to delete ~/Library/Caches?

**故障现象**: Is it safe to delete ~/Library/Caches?
**标签 / 来源**: Tags: macos, hard-drive, file | apple | 👍 211 | 💬 6 answers

**问题描述**:
Tags: macos, hard-drive, file | Score: 211 | Views: 761138 | Answers: 6

**解决方法 / 社区答案**:
It's generally safe, though a little dangerous depending, to do it but often not worth the effort.
The caches in /System/Library/Caches are generally small and useful, the ones in /Library/Caches are less system caches and much more readily cleared.
If you have a look in ~/Library/Caches you will find a bunch of applications have a cache in there, none of them particularly large though dropbox sometimes has a fair sized cache. This folder can run quite large just because so many apps cache something in there.
If the cache /Library/Caches folder is over 3Gb then you have something that is caching quite a lot. On the three machines I just checked none had a /Library/Caches folder over .75 Gb so I'd go right ahead and remove some of it.
Don't worry about age, I'd worry about size.
In the terminal run the following to sort all of the files in that directory by size (ascending):
du -sh /Library/Caches/* | sort -h

Of course the best way to clear the caches is to install AppleJack and do it with that in single user mode. Doing it with the System fully up can be a little dangerous. If you do it then I'd reboot immediately afterwards.

**参考链接**: https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches

> 📎 来源 / Source: https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches

#### 50. ZSH: .zprofile, .zshrc, .zlogin - What goes where?

**故障现象**: ZSH: .zprofile, .zshrc, .zlogin - What goes where?
**标签 / 来源**: Tags: macos, zsh, environment-variables | apple | 👍 209 | 💬 1 answers

**问题描述**:
Tags: macos, zsh, environment-variables | Score: 209 | Views: 274066 | Answers: 1

**解决方法 / 社区答案**:
This is an attempt to write a canonical QA for this issue, as per the Meta post:  Where is the list of canonical questions stored for Ask Different? I expect it to be periodically edited with the goal of becoming a comprehensive information resource.
What should be used in ZSH on a Mac
I posted a more narrowly scoped question on Unix &amp; Linux and got some clarification on how these files &quot;work.&quot;  Here's the summary of that answer and what I've learned in my research as to what, in my opinion should be used in a ZSH environment on a Mac.

.zprofile
.zlogin and .zprofile are basically the same thing - they set the environment for login shells1; they just get loaded at different times (see below).  .zprofile is based on the Bash's .bash_profile while .zlogin is a derivative of CSH's .login.  Since Bash was the default shell for everything up to Mojave, stick with .zprofile.

.zshrc
This sets the environment for interactive shells2.  This gets loaded after .zprofile.  It's typically a place where you &quot;set it and forget it&quot; type of parameters like $PATH, $PROMPT, aliases, and functions you would like to have in both login and interactive shells.

.zshenv (Optional)
This is read first and read every time.  This is where you set environment variables.  I say this is optional because is geared more toward advanced users where having your $PATH, $PAGER, or $EDITOR variables may be important for things like scripts that get called by launchd.  Those run under a non-interactive shell 3 so anything in .zprofile or .zshrc won't get loaded.  Personally, I don't use this one because I set the PATH variable in my script itself to ensure portability.

.zlogout (Optional)
But very useful!  This is read when you log out of a session and is very good for cleaning things up when you leave (like resetting the Terminal Window Title)


For an excellent, in-depth explanation of what these files do, see What should/shouldn't go in .zshenv, .zshrc, .zlogin, .zprofile, on Unix/Linux.

Some Caveats
Apple does things a little differently so it's best to be aware of this.  Specifically,  Terminal initially opens both a login and interactive shell even though you don't authenticate (enter login credentials).  However, any subsequent shells that are opened are only interactive.
You can test this out by putting an alias or setting a variable in .zprofile, then opening Terminal and seeing if that variable/alias exists.  Then open another shell (type zsh); that variable won't be accessible anymore.
SSH sessions are login and interactive so they'll behave just like your initial Terminal session and read both .zprofile and .zshrc
Order of Operations
This is the order in which these files get read.  Keep in mind that it reads first from the system-wide file (i.e. /etc/zshenv) then from the file in your home directory (~/.zshenv) as it goes through the following order.
.zshenv → .zprofile → .zshrc → .zlogin → .zlogout

1 A login shell is simply a shell, whether local or remote, that allows a user to authenticate to the system.  These shells are typically interactive shells.
2 In interactive mode, they [the shell] accept input typed from the keyboard.  (GNU Bash Reference Manual, 1.2 What is a Shell?)
3 When executing non-interactively, shells execute commands read from a file. (Ibid.)

**参考链接**: https://apple.stackexchange.com/questions/388622/zsh-zprofile-zshrc-zlogin-what-goes-where

> 📎 来源 / Source: https://apple.stackexchange.com/questions/388622/zsh-zprofile-zshrc-zlogin-what-goes-where

#### 51. Open Finder window from current Terminal location?

**故障现象**: Open Finder window from current Terminal location?
**标签 / 来源**: Tags: macos, terminal, finder, path | apple | 👍 207 | 💬 7 answers

**问题描述**:
Tags: macos, terminal, finder, path | Score: 207 | Views: 83985 | Answers: 7

**解决方法 / 社区答案**:
Typing open . in Terminal will open the current working directory in a Finder window.

**参考链接**: https://apple.stackexchange.com/questions/19375/open-finder-window-from-current-terminal-location

> 📎 来源 / Source: https://apple.stackexchange.com/questions/19375/open-finder-window-from-current-terminal-location

#### 52. Need a cli to check the sha256 hash of a file

**故障现象**: Need a cli to check the sha256 hash of a file
**标签 / 来源**: Tags: macos, command-line, encryption | apple | 👍 205 | 💬 4 answers

**问题描述**:
Tags: macos, command-line, encryption | Score: 205 | Views: 151884 | Answers: 4

**解决方法 / 社区答案**:
You can use

openssl dgst -sha256 &lt;file&gt;


Tested on LibreSSL 2.6.4 on macOS 10.14 (Mojave).



Prior to Mojave you can use openssl sha -sha256 &lt;file&gt; or openssl sha256 &lt;file&gt;.

To check command line options for the openssl sha command: openssl sha -help.

**参考链接**: https://apple.stackexchange.com/questions/230917/need-a-cli-to-check-the-sha256-hash-of-a-file

> 📎 来源 / Source: https://apple.stackexchange.com/questions/230917/need-a-cli-to-check-the-sha256-hash-of-a-file

#### 53. How can I make auto-hide/show for the dock faster?

**故障现象**: How can I make auto-hide/show for the dock faster?
**标签 / 来源**: Tags: dock, macos | apple | 👍 204 | 💬 12 answers

**问题描述**:
Tags: dock, macos | Score: 204 | Views: 253798 | Answers: 12

**解决方法 / 社区答案**:
To make the Dock instantly leap back into view when it’s needed, rather than slide, open a Terminal window and type the following:
defaults write com.apple.dock autohide-time-modifier -int 0; killall Dock


I find this useful, but if you’d like the animation for the dock to reappear to last for a split-second, try the following:
defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock

To explain, changing &quot;0.15&quot; with any number can let you tailor things as it represents the time in seconds taken for the dock to reappear fully.

To revert back to the default sliding effect, open a Terminal window and type the following:
defaults delete com.apple.dock autohide-time-modifier; killall Dock

**参考链接**: https://apple.stackexchange.com/questions/33600/how-can-i-make-auto-hide-show-for-the-dock-faster

> 📎 来源 / Source: https://apple.stackexchange.com/questions/33600/how-can-i-make-auto-hide-show-for-the-dock-faster

#### 54. How to move files to trash from command line?

**故障现象**: How to move files to trash from command line?
**标签 / 来源**: Tags: macos, command-line | apple | 👍 202 | 💬 17 answers

**问题描述**:
Tags: macos, command-line | Score: 202 | Views: 111071 | Answers: 17

**解决方法 / 社区答案**:
The trash command line tool can be installed via brew install trash or port install trash.
It allows you to restore trashed files via command line or the Finder.

**参考链接**: https://apple.stackexchange.com/questions/50844/how-to-move-files-to-trash-from-command-line

> 📎 来源 / Source: https://apple.stackexchange.com/questions/50844/how-to-move-files-to-trash-from-command-line

#### 55. Restarting sound service?

**故障现象**: Restarting sound service?
**标签 / 来源**: Tags: macbook-pro, audio | apple | 👍 202 | 💬 8 answers

**问题描述**:
Tags: macbook-pro, audio | Score: 202 | Views: 272560 | Answers: 8

**解决方法 / 社区答案**:
sudo pkill coreaudiod
On older OSes:
You can kill the CoreAudio process by opening Terminal and running:
sudo kill -9 `ps ax|grep 'coreaudio[a-z]' | awk '{print $1}'`

It will restart automatically after a couple seconds.
That fixes some problems my aging MBP has been having, where it sometimes fails to detect headphones or decides the speakers aren't connected. No guarantees it will work for every audio problem, but it's worth a shot.
Source: zakgreant on macosxhints forums.

**参考链接**: https://apple.stackexchange.com/questions/16842/restarting-sound-service

> 📎 来源 / Source: https://apple.stackexchange.com/questions/16842/restarting-sound-service

#### 56. How do I disable System Integrity Protection (SIP) AKA &quot;rootless&quot; on macOS?

**故障现象**: How do I disable System Integrity Protection (SIP) AKA &quot;rootless&quot; on macOS?
**标签 / 来源**: Tags: macos, sip | apple | 👍 197 | 💬 6 answers

**问题描述**:
Tags: macos, sip | Score: 197 | Views: 499215 | Answers: 6

**解决方法 / 社区答案**:
Note: disabling System Integrity Protection is dangerous, and makes your system more vulnerable to malware.
As Apple puts it in the developer documentation about SIP:

Warning
Disable SIP only temporarily to perform necessary tasks, and reenable it as soon as possible. Failure to reenable SIP when you are done testing leaves your computer vulnerable to malicious code.

If you are simply trying to configure system development tools such as vim, python2, ruby and so on, you almost certainly want to be just installing community-maintained versions from Homebrew and configuring those instead.  The system-provided tools may be convenient to bootstrap, but if you require SIP exceptions for your daily workflow you are almost certainly doing things in a way which will break in a future version of the operating system, and may break applications and other system functionality in the meanwhile.
Valid reasons to disable SIP yourself might be:

if you're doing research on malware yourself in a disposable environment, such as in a macOS virtual machine
if you are attempting to modify core operating system functionality for deployment in a highly-specialized environment such as a public-facing kiosk
if you require a legacy kernel extension such as MacFUSE on an M1 mac

Also important beyond the security implications is the fact that anything you do on a mac with SIP disabled will not work on anyone else's mac unless they also disable it first. If you're developing mac apps, then your system becomes less useful as a testbed because you don't know if your code only works because you hacked your system. If you're developing for another platform such as deployment to a web server, then you can't share your development environment setup with other developers on your team without compromising their security as well.
Here's how to do it if you really need to:
Apple's documentation covers disabling SIP, About System Integrity Protection on your Mac and Configuring System Integrity Protection.
An article on lifehacker.com lists these steps:


Reboot your Mac into Recovery Mode by restarting your computer and holding down Command+R until the Apple logo appears on your screen.
Click Utilities &gt; Terminal.
In the Terminal window, type in csrutil disable and press Enter.
Restart your Mac.


You can verify whether a file or folder is restricted by issuing this ls command using the capital O (and not zero 0) to modify the long listing flag:
ls -lO /System /usr 

Look for the restricted text to indicate where SIP is enforced.
By default (=SIP enabled), the following folders are restricted (see Apple Support page):
/System
/usr
/bin
/sbin
Apps that are pre-installed with OS X

... and the following folders are free:
/Applications
/Library
/usr/local

**参考链接**: https://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-macos

> 📎 来源 / Source: https://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-macos

#### 57. Cmd+Tab does not work on hidden or minimized windows

**故障现象**: Cmd+Tab does not work on hidden or minimized windows
**标签 / 来源**: Tags: macos, application-switcher | apple | 👍 192 | 💬 17 answers

**问题描述**:
Tags: macos, application-switcher | Score: 192 | Views: 144145 | Answers: 17

**解决方法 / 社区答案**:
This one is a bit tricky :

press ⌘ Cmd + ⇥ Tab to show your running apps. Keep holding ⌘ Cmd.

press ⇥ Tab until you've selected the app

press the ⌥ Option, and let go of the ⌘ Cmd. 
( You must release ⌘ Cmd after pressing ⌥ Option ! )
( You must release ⌘ Cmd before release ⌥ Option ! )

**参考链接**: https://apple.stackexchange.com/questions/112350/cmdtab-does-not-work-on-hidden-or-minimized-windows

> 📎 来源 / Source: https://apple.stackexchange.com/questions/112350/cmdtab-does-not-work-on-hidden-or-minimized-windows

#### 58. Move through images in a folder with Preview.app

**故障现象**: Move through images in a folder with Preview.app
**标签 / 来源**: Tags: macos, preview | apple | 👍 192 | 💬 12 answers

**问题描述**:
Tags: macos, preview | Score: 192 | Views: 200585 | Answers: 12

**解决方法 / 社区答案**:
If you are just skimming the pictures do this:
Instead of opening a picture in Preview.app by double-clicking it, press space to preview the picture in Quick Look when selected in Finder.

Quick Look offers a fast, full-size preview of nearly any kind of file without opening the file. You can rotate photos, trim audio and video clips, and use Markup — directly in the Quick Look window.
https://support.apple.com/en-gb/guide/mac-help/mh14119/mac

This way you can still use the arrow keys to navigate between the pictures.

↑ and ↓ in list view
↑,↓,← and → in icon view

You can still open the picture in Preview.app when needed (top right corner).

**参考链接**: https://apple.stackexchange.com/questions/37914/move-through-images-in-a-folder-with-preview-app

> 📎 来源 / Source: https://apple.stackexchange.com/questions/37914/move-through-images-in-a-folder-with-preview-app

#### 59. How to turn off all animations on OS X

**故障现象**: How to turn off all animations on OS X
**标签 / 来源**: Tags: macos | apple | 👍 192 | 💬 6 answers

**问题描述**:
Tags: macos | Score: 192 | Views: 194509 | Answers: 6

**解决方法 / 社区答案**:
I have only enabled the first four of these, but here are all hidden preferences for disabling animations I have found.

# opening and closing windows and popovers
defaults write -g NSAutomaticWindowAnimationsEnabled -bool false

# smooth scrolling
defaults write -g NSScrollAnimationEnabled -bool false

# showing and hiding sheets, resizing preference windows, zooming windows
# float 0 doesn't work
defaults write -g NSWindowResizeTime -float 0.001

# opening and closing Quick Look windows
defaults write -g QLPanelAnimationDuration -float 0

# rubberband scrolling (doesn't affect web views)
defaults write -g NSScrollViewRubberbanding -bool false

# resizing windows before and after showing the version browser
# also disabled by NSWindowResizeTime -float 0.001
defaults write -g NSDocumentRevisionsWindowTransformAnimation -bool false

# showing a toolbar or menu bar in full screen
defaults write -g NSToolbarFullScreenAnimationDuration -float 0

# scrolling column views
defaults write -g NSBrowserColumnAnimationSpeedMultiplier -float 0

# showing the Dock
defaults write com.apple.dock autohide-time-modifier -float 0
defaults write com.apple.dock autohide-delay -float 0

# showing and hiding Mission Control, command+numbers
defaults write com.apple.dock expose-animation-duration -float 0

# showing and hiding Launchpad
defaults write com.apple.dock springboard-show-duration -float 0
defaults write com.apple.dock springboard-hide-duration -float 0

# changing pages in Launchpad
defaults write com.apple.dock springboard-page-duration -float 0

# at least AnimateInfoPanes
defaults write com.apple.finder DisableAllAnimations -bool true

# sending messages and opening windows for replies
defaults write com.apple.Mail DisableSendAnimations -bool true
defaults write com.apple.Mail DisableReplyAnimations -bool true

**参考链接**: https://apple.stackexchange.com/questions/14001/how-to-turn-off-all-animations-on-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/14001/how-to-turn-off-all-animations-on-os-x

#### 60. Homebrew: Your CLT does not support macOS 11.0

**故障现象**: Homebrew: Your CLT does not support macOS 11.0
**标签 / 来源**: Tags: command-line, homebrew, macos | apple | 👍 191 | 💬 5 answers

**问题描述**:
Tags: command-line, homebrew, macos | Score: 191 | Views: 121880 | Answers: 5

**解决方法 / 社区答案**:
Simplest solution that worked when upgrading to Big Sur. A clean install may not require the solution below. There is inconsistency with the way CLT is upgraded to 12.2.
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install

Worked with the following versions (post-install)
❯ /usr/bin/xcodebuild -version
Xcode 12.2
Build version 12B45b

❯ pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
package-id: com.apple.pkg.CLTools_Executables
version: 12.2.0.0.1.1603499215
volume: /
location: /
install-time: 1605632122
groups: com.apple.FindSystemFiles.pkg-group

Big Sur
11.0.1 (20B29)

**参考链接**: https://apple.stackexchange.com/questions/401899/homebrew-your-clt-does-not-support-macos-11-0

> 📎 来源 / Source: https://apple.stackexchange.com/questions/401899/homebrew-your-clt-does-not-support-macos-11-0

#### 61. Is there a quick way to lock my Mac?

**故障现象**: Is there a quick way to lock my Mac?
**标签 / 来源**: Tags: macos, keyboard, security, screen-lock | apple | 👍 186 | 💬 26 answers

**问题描述**:
Tags: macos, keyboard, security, screen-lock | Score: 186 | Views: 63048 | Answers: 26

**解决方法 / 社区答案**:
On macOS High Sierra, there is a standard key sequence and Apple menu item to lock your screen. 


Control-Command-Q or ^+⌘+Q






For older OS, ⇧+⌃+⏏ puts the display (only the display, not the whole computer) to sleep and will then prompt you for a password if you have enabled Require password [amount of time] after sleep or screen saver begins under System Preferences &gt; Security.

If your Mac does not have an &#x23CF; (eject) key, you can use ⇧+⌃+⌽ (power).

**参考链接**: https://apple.stackexchange.com/questions/64/is-there-a-quick-way-to-lock-my-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/64/is-there-a-quick-way-to-lock-my-mac

#### 62. How to fix brew after OSX upgrade to Yosemite?

**故障现象**: How to fix brew after OSX upgrade to Yosemite?
**标签 / 来源**: Tags: macos, homebrew | apple | 👍 183 | 💬 5 answers

**问题描述**:
Tags: macos, homebrew | Score: 183 | Views: 105182 | Answers: 5

**解决方法 / 社区答案**:
I decided to look this up and found that there is an issue. The issue is closed but it is not possible to simply run brew update because you will still get the same error.

So here is what you need to do:

cd /usr/local/Library
git pull origin master


In case you have changes in the directory (/usr/local/Library), the git pull will throw an error. In that case, you'll have to fetch the master branch and set it forcibly as master:

git fetch --all
git reset --hard origin/master


This will upgrade your homebrew and you can use brew again.

If you installed Homebrew as a non-root user, you'll need to cd to /Users/yourusername/homebrew/Library instead of /usr/local/Library.

**参考链接**: https://apple.stackexchange.com/questions/153790/how-to-fix-brew-after-osx-upgrade-to-yosemite

> 📎 来源 / Source: https://apple.stackexchange.com/questions/153790/how-to-fix-brew-after-osx-upgrade-to-yosemite

#### 63. Is there a `lsblk` equivalent for macOS that lists all attached storage devices?

**故障现象**: Is there a `lsblk` equivalent for macOS that lists all attached storage devices?
**标签 / 来源**: Tags: macos, command-line, hardware, storage | apple | 👍 183 | 💬 6 answers

**问题描述**:
Tags: macos, command-line, hardware, storage | Score: 183 | Views: 480009 | Answers: 6

**解决方法 / 社区答案**:
diskutil list will list all disks with their identifiers, even if unmounted.

/dev/disk0
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *251.0 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                  Apple_HFS Mac SSD                 150.0 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
   4:       Microsoft Basic Data Windows 8               100.1 GB   disk0s4
/dev/disk1
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *500.1 GB   disk1
   1:                  Apple_HFS George Garside          300.2 GB   disk1s1
   2:               Windows_NTFS GRGARSIDE               199.9 GB   disk1s2




For mounted disks only…

To find the raw device name (i.e. /dev/disk0s1) you can run df.

You can limit the results to locally-mounted filesystems, use df -Hl.
This results in a list of partitions and their raw device names, as shown below:

Filesystem     Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk0s2   150G   130G    20G    87% 31761475  4859615   87%   /
/dev/disk0s4   100G    83G    17G    83%   184667 17015601    1%   /Volumes/Windows 8
/dev/disk1s1   300G   282G    19G    94% 68771109  4529660   94%   /Volumes/George Garside
/dev/disk1s2   200G   172G    27G    87%   144125 26731127    1%   /Volumes/GRGARSIDE

**参考链接**: https://apple.stackexchange.com/questions/107953/is-there-a-lsblk-equivalent-for-macos-that-lists-all-attached-storage-devices

> 📎 来源 / Source: https://apple.stackexchange.com/questions/107953/is-there-a-lsblk-equivalent-for-macos-that-lists-all-attached-storage-devices

#### 64. Which OS X Applications do you find indispensable?

**故障现象**: Which OS X Applications do you find indispensable?
**标签 / 来源**: Tags: macos, software-recommendation | apple | 👍 180 | 💬 239 answers

**问题描述**:
Tags: macos, software-recommendation | Score: 180 | Views: 49806 | Answers: 239

**解决方法 / 社区答案**:
Dropbox
Put your files into your Dropbox on one computer, and they'll be instantly available on any of your other computers that you've installed Dropbox on.

**参考链接**: https://apple.stackexchange.com/questions/82/which-os-x-applications-do-you-find-indispensable

> 📎 来源 / Source: https://apple.stackexchange.com/questions/82/which-os-x-applications-do-you-find-indispensable

#### 65. What tiny thing in Lion makes you smile or has caught you off guard?

**故障现象**: What tiny thing in Lion makes you smile or has caught you off guard?
**标签 / 来源**: Tags: macos | apple | 👍 180 | 💬 107 answers

**问题描述**:
Tags: macos | Score: 180 | Views: 56548 | Answers: 107

**解决方法 / 社区答案**:
Using the FaceTime camera to add signatures to PDFs in Preview. 

Click the annotations button in the toolbar and use the drop down menu next to the signature icon to grab your signature from a piece of paper you have written it on. Then just click and drag in the document to place it. Haven't really needed it yet, but it's implemented so nicely that I did it just for fun.

**参考链接**: https://apple.stackexchange.com/questions/17759/what-tiny-thing-in-lion-makes-you-smile-or-has-caught-you-off-guard

> 📎 来源 / Source: https://apple.stackexchange.com/questions/17759/what-tiny-thing-in-lion-makes-you-smile-or-has-caught-you-off-guard

#### 66. Add images to existing PDF with Preview

**故障现象**: Add images to existing PDF with Preview
**标签 / 来源**: Tags: macos, photos, pdf, preview | apple | 👍 180 | 💬 9 answers

**问题描述**:
Tags: macos, photos, pdf, preview | Score: 180 | Views: 327358 | Answers: 9

**解决方法 / 社区答案**:
Do as follows:

Open the image you want to paste in Preview.app
Select All (Command-A)
Copy (Command-C)
Paste (Command-V)

Now you have a copy of your image pasted above your old image. This is apparently meaningless, but the new copy is not just an image, but an object.

Click on the new image (round blue corners appear, no marching ants)
Copy (Command-C)
Paste on your PDF document. The image is an object, moveable and resizable. The original PDF is still a PDF, editable and all.

**参考链接**: https://apple.stackexchange.com/questions/378888/add-images-to-existing-pdf-with-preview

> 📎 来源 / Source: https://apple.stackexchange.com/questions/378888/add-images-to-existing-pdf-with-preview

#### 67. How to arrange two windows easily to left and right side?

**故障现象**: How to arrange two windows easily to left and right side?
**标签 / 来源**: Tags: macos, mac, windows, window-manager | apple | 👍 180 | 💬 21 answers

**问题描述**:
Tags: macos, mac, windows, window-manager | Score: 180 | Views: 423807 | Answers: 21

**解决方法 / 社区答案**:
Original Answer (Update below):
Apple has provided this functionality as part of its OS X El Capitan. Here are the steps:

Click and hold on the green maximize button of an active window (for example, a Safari window);
When the window shrinks slightly and the background becomes highlighted, you’re about to enter Split View, while continuing to hold the green button drag the active window into either the left or right panel to place it full screen there;
As soon as you place the first window into the Split View panel, the other side of the screen turns into a mini-Expose much like Mission Control, simply click the window tile you want to open into Split View for the other side here to immediately send it side by side into Split Full Screen Mode.

The answer has been taken from osxdaily.com website's page.

Update:
Many people commented that they wish there was a shortcut for it. I figured a way to create a shortcut for that from another answer on AskDifferent which I cannot find the link to. This is how:

Open System Preferences;
Go to 'Keyboard' settings;
Go to 'Shortcuts' tab;
In the left pane, select 'App Shortcuts';

In this section you can add app specific shortcuts, as well as shortcuts that you want available for all apps.


Click on the '+' sign below right pane to add a new shortcut;
A new drop down will open. In this drop-down:

In the 'Application:' keep it for 'All Applications';
In the 'Menu Title:' type 'Tile Window to Right of Screen'. Better that you copy-paste it because it has to match letter by letter;
In the 'Keyboard Shortcut:' press the keys you want to use as shortcut for tiling an application window to the right. On my machine, I've set† it to ⎇⌘→.
Repeat the same for tiling to left by putting 'Tile Window to Left of Screen' in the 'Menu Title:' and adding your desired keys for left-tiling shortcut.



You should now have the shortcuts available for any application window that supports tiling. Now, you can press your shortcut keys to tile the first window to left or right. Then the other side will turn into a mini-Expose from which you can select the second window using your mouse.


†I have a dual monitor setup. So other than the one listed above, I have also set the shortcut to move a window to another monitor. The 'Menu Title's are: 
1. &quot;Move to Built-in Retina Display&quot;, with shortcut ⌃⎇⌘→;
2. &quot;Move to LG UltraFine&quot;, with shortcut ⌃⎇⌘←;
To remember the shortcuts, notice that all they keys, are next to each other. All you do is use arrow keys differently. Further, moving to another monitor has an extra key in the shortcut, while putting the windows in split view is on the same monitor, therefore it has one less key.
Hint:
The shortcut name depends on the MacOS system language, e.g.:
english:
'Tile Window to Left of Screen'
german : 'Fenster auf der linken Bildschirmseite anordnen'
or a different title: 'Fenster auf die linke Seite des Bildschirms bewegen'
Phrases for left / right can be found on the green &quot;full screen&quot; button:

**参考链接**: https://apple.stackexchange.com/questions/50330/how-to-arrange-two-windows-easily-to-left-and-right-side

> 📎 来源 / Source: https://apple.stackexchange.com/questions/50330/how-to-arrange-two-windows-easily-to-left-and-right-side

#### 68. What is the `installd` process, and why is it eating my CPU?

**故障现象**: What is the `installd` process, and why is it eating my CPU?
**标签 / 来源**: Tags: activity-monitor, macos | apple | 👍 179 | 💬 7 answers

**问题描述**:
Tags: activity-monitor, macos | Score: 179 | Views: 243455 | Answers: 7

**解决方法 / 社区答案**:
This is a daemon which is part of PackageKit framework and it's usually running as a background process for the "Software Update" GUI application.
For example, if you open the Software Update application and check for updates, take a look at the Activity Monitor--you'll see the "installd" process doing a bunch of work.

The reason it pegs your CPU is because it must compile the current list of software installed on your computer, and compare with the current version list received from Apple's servers.

You can set the frequency of Software Update checks in System Preferences and Software Update.

The default settings are both to "Check for updates" and "Download updates automatically".
You may adjust either setting, but I would not recommend turning it off altogether.

There's nothing wicked about this process - it's just set to download updates.

You can solve your CPU problem by lowering the priority of the process or by just killing the process in Activity Monitor.



Technical information:

The location in Lion OSX is in:
/System/Library/PrivateFrameworks/PackageKit.framework/Resources/installd

(if you have locate configured correctly, run: locate installd to find the right location).

**参考链接**: https://apple.stackexchange.com/questions/87109/what-is-the-installd-process-and-why-is-it-eating-my-cpu

> 📎 来源 / Source: https://apple.stackexchange.com/questions/87109/what-is-the-installd-process-and-why-is-it-eating-my-cpu

#### 69. What is this qemu-system-aarch64 process and why is it using almost 3 GB of RAM on my M1 Mac

**故障现象**: What is this qemu-system-aarch64 process and why is it using almost 3 GB of RAM on my M1 Mac
**标签 / 来源**: Tags: mac-mini, macos, activity-monitor, apple-silicon | apple | 👍 178 | 💬 3 answers

**问题描述**:
Tags: mac-mini, macos, activity-monitor, apple-silicon | Score: 178 | Views: 155253 | Answers: 3

**解决方法 / 社区答案**:
This process belongs to an application you've installed yourself.
To find out more, select the process in Activity Monitor and press Cmd-I to open the Process Information window. You should see the name of the process which started it at the top, and the path to the binary itself near the top of the 3rd tab (open files and ports).

**参考链接**: https://apple.stackexchange.com/questions/420445/what-is-this-qemu-system-aarch64-process-and-why-is-it-using-almost-3-gb-of-ram

> 📎 来源 / Source: https://apple.stackexchange.com/questions/420445/what-is-this-qemu-system-aarch64-process-and-why-is-it-using-almost-3-gb-of-ram

#### 70. How can I mount an ext4 file system on OS X?

**故障现象**: How can I mount an ext4 file system on OS X?
**标签 / 来源**: Tags: macos, unix | apple | 👍 178 | 💬 11 answers

**问题描述**:
Tags: macos, unix | Score: 178 | Views: 372061 | Answers: 11

**解决方法 / 社区答案**:
The answer depends on you willingness to invest in commercial software:
If you don’t mind spending some money on a commercial product, Paragon’s extFS for Mac will give you read and write access to ext2 / ext3 / ext4 file systems. The current version supports all versions of OS X / macOS from 10.10 upwards.
If you are looking for a free solution, you can setup a Linux virtual machine, mount your volume(s) there and share it / them via Samba or (S)FTP. This post has some details on how to achieve this using VirtualBox, a free virtual machine application. Note this is not exactly a lightweight solution, even if using a prebuilt VirtualBox VM will spare you installing and configuring a Linux distro from scratch.

**参考链接**: https://apple.stackexchange.com/questions/29842/how-can-i-mount-an-ext4-file-system-on-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/29842/how-can-i-mount-an-ext4-file-system-on-os-x

#### 71. Convert .mov to .mp4

**故障现象**: Convert .mov to .mp4
**标签 / 来源**: Tags: macos, video, imovie, mp4, mov | apple | 👍 177 | 💬 6 answers

**问题描述**:
Tags: macos, video, imovie, mp4, mov | Score: 177 | Views: 134269 | Answers: 6

**解决方法 / 社区答案**:
I personally find using ffmpeg shell program (available through Brew using brew install ffmpeg) the most convenient way to do the conversions.

It includes tons of options for nearly any single thing you could possibly do with a movie.

In your case though, for a conversion, you can simply type:

ffmpeg -i /path/to/input/file /path/to/output.mp4

The .mp4 extension in the output path serves as a cue for the program to do the proper conversion -- no more options are necessary.

**参考链接**: https://apple.stackexchange.com/questions/232910/convert-mov-to-mp4

> 📎 来源 / Source: https://apple.stackexchange.com/questions/232910/convert-mov-to-mp4

#### 72. How can I prevent an SSH session from hanging in OS X Terminal?

**故障现象**: How can I prevent an SSH session from hanging in OS X Terminal?
**标签 / 来源**: Tags: macos, terminal, wifi, ssh | apple | 👍 175 | 💬 7 answers

**问题描述**:
Tags: macos, terminal, wifi, ssh | Score: 175 | Views: 189533 | Answers: 7

**解决方法 / 社区答案**:
For keeping the connection alive, you can check in /etc/ssh/ssh_config the line where it says ServerAliveInterval, that tells you how often (in seconds) your computer is gonna send a null packet to keep the connection alive. If you have a 0 in there that indicates that your computer is not trying to keep the connection alive (it is disabled), otherwise it tells you how often (in seconds) it is sending the aforementioned packet. Try putting in 120 or 240, if it is still killing your connection, you can go lower, maybe to 5, if with that number it doesn't happen, maybe it is your router who is dumping the connection to free memory.

For killing it when it gets hang up, you can use the ssh escape character:

~.


That is, press the tilde and then the period, if it doesn't work, press Enter before you press that, that will kill the connection immediately.

**参考链接**: https://apple.stackexchange.com/questions/36690/how-can-i-prevent-an-ssh-session-from-hanging-in-os-x-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/36690/how-can-i-prevent-an-ssh-session-from-hanging-in-os-x-terminal

#### 73. OS X computer name not matching what shows on terminal

**故障现象**: OS X computer name not matching what shows on terminal
**标签 / 来源**: Tags: macos, xcode | apple | 👍 174 | 💬 12 answers

**问题描述**:
Tags: macos, xcode | Score: 174 | Views: 187601 | Answers: 12

**解决方法 / 社区答案**:
It's perfectly normal for this to occur; when you login Terminal remotely bash does a reverse DNS lookup. It will only be the same if the hostname is not specified on the network you're connecting from and there is no reply from the DHCP server, or the reverse lookup against the remote DNS server fails to resolve.
You can easily over-ride the default setting by using this command in Terminal:
sudo scutil --set HostName archos

You can check it by using:
nslookup nn.nn.nn.nn

( or )
host nn.nn.nn.nn

(where nn signifies your Mac's ip address)

**参考链接**: https://apple.stackexchange.com/questions/30552/os-x-computer-name-not-matching-what-shows-on-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/30552/os-x-computer-name-not-matching-what-shows-on-terminal

#### 74. What happens if you plug more than one charger in the new MacBook Pro (2016)?

**故障现象**: What happens if you plug more than one charger in the new MacBook Pro (2016)?
**标签 / 来源**: Tags: macbook-pro, usb, charger, charging | apple | 👍 173 | 💬 3 answers

**问题描述**:
Tags: macbook-pro, usb, charger, charging | Score: 173 | Views: 163463 | Answers: 3

**解决方法 / 社区答案**:
The system will choose the power source that provides the most power, and it will not draw power from the others.
Apple has released a support article (and another one) describing this:


Your MacBook Pro draws power from only one power supply, even if more
than one is attached—so using multiple power supplies will not speed
up charging.

If you connect multiple power supplies to your MacBook
Pro, the one that provides the most power will be used, regardless of
the order in which you connected them.

You should not connect any
power supply that exceeds 100W, as it might damage your Mac.

**参考链接**: https://apple.stackexchange.com/questions/259744/what-happens-if-you-plug-more-than-one-charger-in-the-new-macbook-pro-2016

> 📎 来源 / Source: https://apple.stackexchange.com/questions/259744/what-happens-if-you-plug-more-than-one-charger-in-the-new-macbook-pro-2016

#### 75. How to simulate slow internet connections on the mac

**故障现象**: How to simulate slow internet connections on the mac
**标签 / 来源**: Tags: macos, mac, network, performance, internet | apple | 👍 172 | 💬 10 answers

**问题描述**:
Tags: macos, mac, network, performance, internet | Score: 172 | Views: 179944 | Answers: 10

**解决方法 / 社区答案**:
Apple’s official tool to slow down the network connections on you Mac for testing purposes is Network Link Conditioner

Additional Tools for Xcode [version].

Additionally, iOS has similar function accessible from within Xcode and iOS 6 or later.

Older versions of Xcode before version 4.3.2 embedded a copy of this tool. This SO thread documents some history of the tool in a similar manner to the iOS simulators and developer documentation.
There are 11 built in profiles from a Lossy Edge network with 400ms delay to a cable modem. If you need other limits, you can create custom profiles with your own settings or you can also use ipfw yourself as described in Craig Hockenberry's article slow ride, make it easy It also mentions the Speed Limit panel by Mike Schrag that is a smaller download than Xcode, but has fewer options than Apple's tool.
It slows down the entire network stack, so you can't throttle on a per app basis without doing things like install lion in a virtual machine and set that VM with a throttled stack.

**参考链接**: https://apple.stackexchange.com/questions/24066/how-to-simulate-slow-internet-connections-on-the-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/24066/how-to-simulate-slow-internet-connections-on-the-mac

#### 76. Using The Terminal Command to Shutdown, Restart and Sleep My Mac?

**故障现象**: Using The Terminal Command to Shutdown, Restart and Sleep My Mac?
**标签 / 来源**: Tags: macos, terminal, sleep-wake, shutdown, restart | apple | 👍 172 | 💬 4 answers

**问题描述**:
Tags: macos, terminal, sleep-wake, shutdown, restart | Score: 172 | Views: 551481 | Answers: 4

**解决方法 / 社区答案**:
The command you are after is shutdown.
This  informs all users that the machine is going to be shutdown and tells all apps to close files etc.
The command takes a parameter -h, -r or -s to shut down, restart or sleep the Mac.
The command has to be run as root so you need to use sudo.
e.g. to reboot the machine immediately
sudo shutdown -r now

e.g. to shutdown the machine in 60 minutes
sudo shutdown -h +60

From comments there are two things to be addressed
How shutdown works is by sending a sigterm to all processes which should then deal with that e.g. save open files etc. If they don't exit then they will get sent a SIGKILL which forces them to die with no chance to respond. The signals are not sent via the normal key message queue so Apps have to deal with this separately to the code that gets called from quit on the menu. A good app should call common code from both.
This other answer shows how to shutdown as if you hit the menu options. But note that apps can cancel this shutdown

**参考链接**: https://apple.stackexchange.com/questions/103571/using-the-terminal-command-to-shutdown-restart-and-sleep-my-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/103571/using-the-terminal-command-to-shutdown-restart-and-sleep-my-mac

#### 77. How to get the chrome tabs to always show when in full screen mode?

**故障现象**: How to get the chrome tabs to always show when in full screen mode?
**标签 / 来源**: Tags: macos, google-chrome, fullscreen, tabs | apple | 👍 170 | 💬 9 answers

**问题描述**:
Tags: macos, google-chrome, fullscreen, tabs | Score: 170 | Views: 357321 | Answers: 9

**解决方法 / 社区答案**:
With latest version of Chrome, there is the option to show the Toolbar (which includes tabs) in the View menu.

**参考链接**: https://apple.stackexchange.com/questions/94737/how-to-get-the-chrome-tabs-to-always-show-when-in-full-screen-mode

> 📎 来源 / Source: https://apple.stackexchange.com/questions/94737/how-to-get-the-chrome-tabs-to-always-show-when-in-full-screen-mode

#### 78. Task Switcher moves to non-primary display on Mavericks-Catalina

**故障现象**: Task Switcher moves to non-primary display on Mavericks-Catalina
**标签 / 来源**: Tags: macos, display, application-switcher | apple | 👍 170 | 💬 5 answers

**问题描述**:
Tags: macos, display, application-switcher | Score: 170 | Views: 46640 | Answers: 5

**解决方法 / 社区答案**:
I answered a similar question here - cmd-tab behavior on Mavericks with multiple displays

The Task Switcher does follow the Dock.  If the Dock is on screen 1, the Task Switcher will appear on screen 1.  If the Dock is on screen 3, the Task Switcher will appear on screen 3.  Etc.

To make your Dock appear on a screen you can use a couple of methods.

Method 1 - Move your mouse to the bottom of the desired display.  Don't stop once you reach the bottom of the display though, try to move it further down, as if you're pushing down on the bottom of the display with your cursor.  This action tells the Dock to move to this display.  This is temporary however, meaning the Dock will stay on this display until you perform this action on another display or reboot your Mac.

Method 2 - This will change the default starting point for your Dock.  In System Preferences > Displays > Arrangement you can drag the menu bar from one display to another in this windows display icons.  See the attached picture for reference.  This alters the default preference to always show the Dock on the desired display, the one you drag the menu bar to in this preference pane, when you boot and/or login to your user account.  You can still use method 1 to temporarily change the Dock's location but upon a reboot it will return to the display specified here.

**参考链接**: https://apple.stackexchange.com/questions/107419/task-switcher-moves-to-non-primary-display-on-mavericks-catalina

> 📎 来源 / Source: https://apple.stackexchange.com/questions/107419/task-switcher-moves-to-non-primary-display-on-mavericks-catalina

#### 79. WindowServer high CPU on Yosemite

**故障现象**: WindowServer high CPU on Yosemite
**标签 / 来源**: Tags: macos, performance | apple | 👍 170 | 💬 11 answers

**问题描述**:
Tags: macos, performance | Score: 170 | Views: 188761 | Answers: 11

**解决方法 / 社区答案**:
I had a similar issue with high cpu usage in WindowServer which I managed to get back to something more normal by removing any items in my menu bar that were making high frequency drawing updates. 

In my case it was the Network Monitor from Little Snitch that seemed to be the biggest culprit.

**参考链接**: https://apple.stackexchange.com/questions/153397/windowserver-high-cpu-on-yosemite

> 📎 来源 / Source: https://apple.stackexchange.com/questions/153397/windowserver-high-cpu-on-yosemite

#### 80. Keyboard shortcut to switch focus between multiple displays on OS X 10.9+

**故障现象**: Keyboard shortcut to switch focus between multiple displays on OS X 10.9+
**标签 / 来源**: Tags: keyboard, display, macos | apple | 👍 170 | 💬 7 answers

**问题描述**:
Tags: keyboard, display, macos | Score: 170 | Views: 373483 | Answers: 7

**解决方法 / 社区答案**:
Refer to the original page for detailed solutions and community answers.

**参考链接**: https://apple.stackexchange.com/questions/106559/keyboard-shortcut-to-switch-focus-between-multiple-displays-on-os-x-10-9

> 📎 来源 / Source: https://apple.stackexchange.com/questions/106559/keyboard-shortcut-to-switch-focus-between-multiple-displays-on-os-x-10-9

#### 81. How can I install .pkg with a shell on macOS?

**故障现象**: How can I install .pkg with a shell on macOS?
**标签 / 来源**: Tags: macos, command-line, install, pkg | apple | 👍 166 | 💬 3 answers

**问题描述**:
Tags: macos, command-line, install, pkg | Score: 166 | Views: 483177 | Answers: 3

**解决方法 / 社区答案**:
/usr/sbin/installer

The installer command is used to install Mac OS X installer packages to a specified domain or volume.  The
installer command installs a single package per invocation, which is specified with the -package parameter ( -pkg
is accepted as a synonym).  It may be either a single package or a metapackage.  In the case of the metapackage,
the packages which are part of the default install will be installed unless disqualified by a package's check
tool(s).

See man installer for the full functionality. Often
sudo installer -pkg /path/to/package.pkg -target /

is all that's needed. The target is a &quot;device&quot; (see the man page for details or run installer -dominfo). Here / is the main drive, it also accepts devices like &quot;/Volumes/Macintosh HD&quot;, or /dev/disk0.

**参考链接**: https://apple.stackexchange.com/questions/72226/how-can-i-install-pkg-with-a-shell-on-macos

> 📎 来源 / Source: https://apple.stackexchange.com/questions/72226/how-can-i-install-pkg-with-a-shell-on-macos

#### 82. What directory comparison tools can I use on OS X?

**故障现象**: What directory comparison tools can I use on OS X?
**标签 / 来源**: Tags: macos, command-line | apple | 👍 164 | 💬 17 answers

**问题描述**:
Tags: macos, command-line | Score: 164 | Views: 196307 | Answers: 17

**解决方法 / 社区答案**:
FileMerge (free), shipped with Xcode, offers a directory view.
A command line version is available through the Terminal application opendiff.

Here's how you can compare two directories with FileMerge:


⌘+space, type in "FileMerge" and open it.
Click the "left" button and choose the folder you would like to move items FROM. (The "old" folder)
Click the "right" button and choose the folder you would like to move items TO. ("new" folder) and click "Compare" button
In the right panel, choose to exclude: "identical" and "Changed right". This way you will only see files which are missing in the "new" folder and ignore files your may have added in the "new" folder.
Move files manually in Finder or let FileMerge do it, by choosing an option in the "Merge" dropdown in the right panel.

**参考链接**: https://apple.stackexchange.com/questions/10252/what-directory-comparison-tools-can-i-use-on-os-x

> 📎 来源 / Source: https://apple.stackexchange.com/questions/10252/what-directory-comparison-tools-can-i-use-on-os-x

#### 83. Any nice, stable ways to keep a window &#39;Always on top&#39; on the Mac?

**故障现象**: Any nice, stable ways to keep a window &#39;Always on top&#39; on the Mac?
**标签 / 来源**: Tags: macos, window-manager | apple | 👍 163 | 💬 13 answers

**问题描述**:
Tags: macos, window-manager | Score: 163 | Views: 276780 | Answers: 13

**解决方法 / 社区答案**:
Refer to the original page for detailed solutions and community answers.

**参考链接**: https://apple.stackexchange.com/questions/219116/any-nice-stable-ways-to-keep-a-window-always-on-top-on-the-mac

> 📎 来源 / Source: https://apple.stackexchange.com/questions/219116/any-nice-stable-ways-to-keep-a-window-always-on-top-on-the-mac

#### 84. Change location of macOS Notification Center alerts?

**故障现象**: Change location of macOS Notification Center alerts?
**标签 / 来源**: Tags: macos, notifications | apple | 👍 159 | 💬 10 answers

**问题描述**:
Tags: macos, notifications | Score: 159 | Views: 89318 | Answers: 10

**解决方法 / 社区答案**:
Unfortunately, you can't change the screen position of the Notification Center Alerts and Banners. This is a huge gripe of mine as well, and I highly encourage you to complain about this issue to Apple here:
http://www.apple.com/feedback/macos.html

Hopefully they will one day change this. I also have not been able to find or formulate any hacks.

I, too, am annoyed by it covering up controls in my modeling applications, tabs in my browser, etc.

You can move the Notification Center to another screen, however your entire menu bar goes with it. When you have more than one monitor active, open up System Preferences > Displays > Arrangement. Click and drag the white bar inside one of the squares representing your current primary monitor and drag it to another monitor.

For notifications that don't need immediate attention, consider changing the alert style from Alerts to Banners. Banners are automatically dismissed into the notification center where you can find them later.

Good luck, and keep spreading the word that we need to tell Apple to make this experience better.

**参考链接**: https://apple.stackexchange.com/questions/71989/change-location-of-macos-notification-center-alerts

> 📎 来源 / Source: https://apple.stackexchange.com/questions/71989/change-location-of-macos-notification-center-alerts

#### 85. How to stop OS X from writing Spotlight and Trash files to memory cards and USB sticks?

**故障现象**: How to stop OS X from writing Spotlight and Trash files to memory cards and USB sticks?
**标签 / 来源**: Tags: macos, photos, usb, spotlight, trash | apple | 👍 158 | 💬 23 answers

**问题描述**:
Tags: macos, photos, usb, spotlight, trash | Score: 158 | Views: 192282 | Answers: 23

**解决方法 / 社区答案**:
For just a particular mounted volume - like a flash drive called yourUSBstick in this example - these commands will remove existing cruft, stop Spotlight indexing now and in the future, stop the related fsevents logging, and disable the Trash feature.

mdutil -i off /Volumes/yourUSBstick
cd /Volumes/yourUSBstick
rm -rf .{,_.}{fseventsd,Spotlight-V*,Trashes}
mkdir .fseventsd
touch .fseventsd/no_log .metadata_never_index .Trashes
cd -


Other unfamiliar stuff you may still see you probably want to keep, like Apple double "._*" files and other Apple DS cruft relating to icons and window placement.

**参考链接**: https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb

> 📎 来源 / Source: https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb

#### 86. How to switch or close the new split Terminal pane?

**故障现象**: How to switch or close the new split Terminal pane?
**标签 / 来源**: Tags: macos, terminal | apple | 👍 158 | 💬 3 answers

**问题描述**:
Tags: macos, terminal | Score: 158 | Views: 154734 | Answers: 3

**解决方法 / 社区答案**:
The idea behind splitting is that it allows you to keep a certain part of the shell buffer displayed while continuing to enter new commands. So only the lowest split does allow keyboard input. To position the view on the shell buffer use the scroll bar.

You can un-split by pressing Shift-Cmd-D.

**参考链接**: https://apple.stackexchange.com/questions/87202/how-to-switch-or-close-the-new-split-terminal-pane

> 📎 来源 / Source: https://apple.stackexchange.com/questions/87202/how-to-switch-or-close-the-new-split-terminal-pane

#### 87. Can home and end keys be mapped when using Terminal?

**故障现象**: Can home and end keys be mapped when using Terminal?
**标签 / 来源**: Tags: macos, terminal, keyboard, command-line, keybindings | apple | 👍 157 | 💬 11 answers

**问题描述**:
Tags: macos, terminal, keyboard, command-line, keybindings | Score: 157 | Views: 93737 | Answers: 11

**解决方法 / 社区答案**:
This can be set in Terminal.app preferences
Context
To answer the one about how to get the beginning or end of the line, it appears that by default Terminal maps these keys to it:

shift+home → beginning of line, equivalent to the &quot;home&quot; key in normal terminals
shift+end → end of line, equivalent to the &quot;end&quot; key in normal terminals

Instructions
If you want home and end to work the &quot;normal&quot; way (and not require shift), go to the Keyboard tab of the Terminal profile preferences:
[Terminal menu] → Preferences → Profiles tab (or settings on some versions of OS X) → Keyboard sub-tab
Then modify/add these keys to be the following &quot;send string to shell&quot;. Use the code for your shell, Bash or Zsh.
macOS changed the default shell from Bash to Zsh in MacOS Catalina (v10.15) and later versions (BigSur and Monterey). The instructions are different for Bash and Zsh.
Zsh

home: \001
end: \005

You can enter these codes in the edit dialog by pressing ctrl-A for \001 and ctrl-E for \005. Thanks to @JW for the Zsh information.
Another, unrelated, option to map home/end keys for MacOS Catalina (v10.15) and later versions (BigSur and Monterey) is to use bindkey widgets:
sudo echo 'bindkey &quot;\033[H&quot; beginning-of-line; bindkey &quot;\033[F&quot; end-of-line' &gt;&gt; ~/.zshrc

Bash

home: \033[H
end:  \033[F

You can get the \033 part by hitting the escape key within the edit dialog input, if you need to add it.
In later versions of Mac OS X, if the terminal screen shifts up or down when you press the home/end key, the home key may need to be set to \033[1~ and the end key to \033[4~ to get the results you want (no shift needed).
Conclusion
Then home and end will work like normal again (phew).
Also note that alt+← and alt+→ by default in terminal map to word left and word right, another handy combo to remember.
Feel free to modify this answer to add more useful key bindings, as it is a community wiki.

**参考链接**: https://apple.stackexchange.com/questions/12997/can-home-and-end-keys-be-mapped-when-using-terminal

> 📎 来源 / Source: https://apple.stackexchange.com/questions/12997/can-home-and-end-keys-be-mapped-when-using-terminal

#### 88. Remember window sizes and placement when unplugging and replugging second monitor

**故障现象**: Remember window sizes and placement when unplugging and replugging second monitor
**标签 / 来源**: Tags: macos, windows, display, window-manager, productivity | apple | 👍 157 | 💬 13 answers

**问题描述**:
Tags: macos, windows, display, window-manager, productivity | Score: 157 | Views: 68974 | Answers: 13

**解决方法 / 社区答案**:
Have a look at Stay by Cordless Dog. I believe it does exactly what you're looking for.

**参考链接**: https://apple.stackexchange.com/questions/126351/remember-window-sizes-and-placement-when-unplugging-and-replugging-second-monito

> 📎 来源 / Source: https://apple.stackexchange.com/questions/126351/remember-window-sizes-and-placement-when-unplugging-and-replugging-second-monito

#### 89. Is there a way to convert audio files in Mac OS X or the command line without using iTunes?

**故障现象**: Is there a way to convert audio files in Mac OS X or the command line without using iTunes?
**标签 / 来源**: Tags: macos, audio, unix | apple | 👍 156 | 💬 9 answers

**问题描述**:
Tags: macos, audio, unix | Score: 156 | Views: 137510 | Answers: 9

**解决方法 / 社区答案**:
I installed ffmpeg via MacPorts, although it also available via Homebrew (brew install ffmpeg) or download the binary.
To convert something like that, (without worrying about audio quality, which I know nothing about), I just use:
ffmpeg -i input.mp4 output.mp3

Here is an example of how you would convert a .wav file to .mp3 from their website:
ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3 

Here is an example of how to find all .wav files larger than 50M, convert them to mp3 and then delete the original wav file (aka, batch mode -- alter the find command to create your 'batch')
find . -size +50M -iname '*.wav' -type f -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}.mp3 -y \; -exec /bin/rm {} \;

If you don't want to delete the source file, say in case the conversion fails or you want to have both:
find . -size +50M -iname '*.wav' -type f -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}.mp3 -y \;

Note that the -y overwrites existing files without prompting so if you want to not have that you can remove it.

**参考链接**: https://apple.stackexchange.com/questions/26099/is-there-a-way-to-convert-audio-files-in-mac-os-x-or-the-command-line-without-us

> 📎 来源 / Source: https://apple.stackexchange.com/questions/26099/is-there-a-way-to-convert-audio-files-in-mac-os-x-or-the-command-line-without-us

#### 90. How do I start the docker daemon on macOS?

**故障现象**: How do I start the docker daemon on macOS?
**标签 / 来源**: Tags: macos, daemons, docker | apple | 👍 154 | 💬 9 answers

**问题描述**:
Tags: macos, daemons, docker | Score: 154 | Views: 547378 | Answers: 9

**解决方法 / 社区答案**:
An alternative solution is to use other runtime for docker. For example
colima
brew install colima
colima start
docker ps -a

Since docker desktop isn't free for enterprise usage, the alternative runtime is a good option.
NOTE: if you've previously used Docker Desktop for launching Docker daemon and had an export of DOCKER_HOST defined in your user's shell configuration (.bash_profile, .zsh_profile etc.), you need to re-specify DOCKER_HOST to make sure it points to .colima directory and commands like docker-compose up -d work properly.
Example:
export DOCKER_HOST=unix:///$HOME/.colima/docker.sock

**参考链接**: https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos

> 📎 来源 / Source: https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos

#### 91. Update bash to version 4.0 on OSX

**故障现象**: Update bash to version 4.0 on OSX
**标签 / 来源**: Tags: macos, terminal, bash, command-line | apple | 👍 154 | 💬 6 answers

**问题描述**:
Tags: macos, terminal, bash, command-line | Score: 154 | Views: 138259 | Answers: 6

**解决方法 / 社区答案**:
As @William said in his answer, Apple does not provide bash 4 due to GPL restrictions. You can install bash 4+ however and also can make it your default shell (including for Terminal and iTerm2) by doing the following.

Install Bash 4 via Homebrew

First install the newer version of bash. There are various ways of doing that, I prefer Homebrew.


Install Homebrew as described at http://brew.sh.  
Install bash using brew install bash.


Bash 4 is now available on your PATH (assuming Homebrew bin is on your path). However, it is not yet your default shell. You can find where it is located by running which bash. In my case it is at /usr/local/bin/bash. 

Using Bash 4

Since it is on your PATH, you can start a Bash 4 session with just bash or it can be used in scripts by using a Shebang.

For example, this will use a specific bash instance.

#!/usr/local/bin/bash
...your script...


This will use the first bash on the PATH.

#!/usr/bin/env bash
...your script...


You can also set the bash path for specific profiles in Terminal/iTerm2 using the steps described in @user136952's answer.

Making Bash 4 the default

As mentioned above, after installing Bash 4 is still not the default shell. To make bash the default you need to do two more steps.

First, add the Bash 4 path to your /etc/shells file so that it is an allowed login shell. As described in /etc/shells, this file has the list of valid login shells. After adding the new bash path my /etc/shells looks like the following:

# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
/usr/local/bin/bash


Next we use chsh to make it your default shell. So any sessions for that user will use that shell. You can read more about this in Change the Shell in Mac OS X Terminal, but the actual command is very straightforward.

chsh -s /usr/local/bin/bash


Now the new bash is our default login shell. If you open Terminal or iTerm2 and run bash --version you should see the new version. Note the "License GPLv3+" which is why Apple doesn't bundle it with macOS.

$ bash --version
GNU bash, version 4.4.12(1)-release (x86_64-apple-darwin16.6.0)
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;

**参考链接**: https://apple.stackexchange.com/questions/193411/update-bash-to-version-4-0-on-osx

> 📎 来源 / Source: https://apple.stackexchange.com/questions/193411/update-bash-to-version-4-0-on-osx

#### 92. cmd-tab behavior on Mavericks with multiple displays

**故障现象**: cmd-tab behavior on Mavericks with multiple displays
**标签 / 来源**: Tags: macos, display, application-switcher | apple | 👍 153 | 💬 5 answers

**问题描述**:
Tags: macos, display, application-switcher | Score: 153 | Views: 87913 | Answers: 5

**解决方法 / 社区答案**:
I believe this coincides with the Dock's location.  Just tested it on my MacBook Air, connected to a non-Apple external display, and whenever I moved the Dock from screen to screen the Application Switcher would follow.

You can summon the Dock on your big display by dragging the cursor to the bottom of it's display, essentially dragging down at the bottom.  After a second the Dock should pop up.  Once the Dock is on the desired display press commandtab to summon the Application Switcher.

**参考链接**: https://apple.stackexchange.com/questions/106405/cmd-tab-behavior-on-mavericks-with-multiple-displays

> 📎 来源 / Source: https://apple.stackexchange.com/questions/106405/cmd-tab-behavior-on-mavericks-with-multiple-displays

#### 93. macOS notifications on dual monitors: how can I specify which monitor?

**故障现象**: macOS notifications on dual monitors: how can I specify which monitor?
**标签 / 来源**: Tags: macos, notifications, dual-screen | apple | 👍 152 | 💬 3 answers

**问题描述**:
Tags: macos, notifications, dual-screen | Score: 152 | Views: 96074 | Answers: 3

**解决方法 / 社区答案**:
You should be able to do this by choosing the monitor on which the menu bar is active.
Try:

System Settings -&gt; Displays -&gt; Arrangement

and drag the little white bar to the monitor where you want the notifications to show up.
In the picture below, the bar is being dragged from the left to the right window.

**参考链接**: https://apple.stackexchange.com/questions/157260/macos-notifications-on-dual-monitors-how-can-i-specify-which-monitor

> 📎 来源 / Source: https://apple.stackexchange.com/questions/157260/macos-notifications-on-dual-monitors-how-can-i-specify-which-monitor

#### 94. Restricting Command+tab options to only apps that are in the current space

**故障现象**: Restricting Command+tab options to only apps that are in the current space
**标签 / 来源**: Tags: macos, spaces | apple | 👍 152 | 💬 12 answers

**问题描述**:
Tags: macos, spaces | Score: 152 | Views: 67784 | Answers: 12

**解决方法 / 社区答案**:
Refer to the original page for detailed solutions and community answers.

**参考链接**: https://apple.stackexchange.com/questions/5668/restricting-commandtab-options-to-only-apps-that-are-in-the-current-space

> 📎 来源 / Source: https://apple.stackexchange.com/questions/5668/restricting-commandtab-options-to-only-apps-that-are-in-the-current-space

#### 95. Is there a command line program for macOS that can access serial ports?

**故障现象**: Is there a command line program for macOS that can access serial ports?
**标签 / 来源**: Tags: macos, command-line | apple | 👍 151 | 💬 16 answers

**问题描述**:
Tags: macos, command-line | Score: 151 | Views: 675404 | Answers: 16

**解决方法 / 社区答案**:
You can use the terminal command screen to do this!!!

As seen on ServerFault:


  I love using [screen] for connecting to serial consoles, i.e.

screen /dev/ttyS0 19200



Or, if you prefer Mac OS X hints...


  I often have to do router configuration via a console port, so I use a
  Keyspan Serial Adapter to get access. Two problems then present
  themselves: ZTerm is a horrible Mac OS X app. It hasn't been updated
  in five years or so, and isn't a Universal Binary. The developer
  doesn't seem in any hurry to rectify the situation. It is not worth
  the shareware fee in its current form. Minicom requires installation
  of Fink or MacPorts and is overly complex. Solution: Use screen,
  Terminal, and a little AppleScripting.
  
  First, launch Script Editor and type/paste in the following code:

tell application "Terminal"
  do script with command "screen /dev/tty.KeySerial1"
  set number of rows of window 1 to 100
  set number of columns of window 1 to 80
  set background color of window 1 to "black"
  set normal text color of window 1 to "green"
  set custom title of window 1 to "SerialOut"
end tell

  
  Compile and save as an app from within Script Editor, and you have a
  double-clickable application to launch a serial Terminal session. You
  may want to customize this slightly -- you can change the screen
  colors or number of columns or rows. You may also need to customize
  the screen command with a different device name if you are using
  something other than the Keyspan Serial Adapter (do an ls tty* of the
  /dev/ directory to get the right name). 
  
  screen uses Control-A to take commands directed to it. So type
  Control-A followed by Control-\ to exit your screen session. If you
  fail to do this and exit a Terminal session, you'll leave the screen
  session alive and the serial resource unavailable until you kill the
  screen session manually. man screen will show you further commands to
  send to a screen session. 
  
  If anyone can reply with a link to a tutorial on how to wrap an
  interactive Unix App in Cocoa, that would be the next step -- it would
  be nice to do this without involving Terminal. If you prefer to use
  Minicom, you could still use the AppleScript to wrap it into a nice
  launchable app -- use this older hint to find the right command line
  commands.


Many USB-Serial adapters use the chip from FTDI. Install the "Virtual COM Port" driver and look for the proper TTY name in /dev. For example, on a PowerBook G4 it came up as /dev/tty.usbserial-FTALKY8I.

**参考链接**: https://apple.stackexchange.com/questions/32834/is-there-a-command-line-program-for-macos-that-can-access-serial-ports

> 📎 来源 / Source: https://apple.stackexchange.com/questions/32834/is-there-a-command-line-program-for-macos-that-can-access-serial-ports

#### 96. How do I sync the Visual Studio Code (vscode) theme to use my OS light/dark color scheme?

**故障现象**: How do I sync the Visual Studio Code (vscode) theme to use my OS light/dark color scheme?
**标签 / 来源**: Tags: macos, system-settings, visual-studio-code | apple | 👍 151 | 💬 3 answers

**问题描述**:
Tags: macos, system-settings, visual-studio-code | Score: 151 | Views: 54183 | Answers: 3

**解决方法 / 社区答案**:
Enable Auto Detect (Search in Settings: window.autoDetectColorScheme)
Customize Color Themes (Search in Settings: workbench preferred color theme)


More Detail (Visual Studio Code Themes):

Auto switch based on OS color scheme Windows and macOS support light and dark color schemes. There is a setting, window.autoDetectColorScheme, that instructs VS Code to listen to changes to the OS's color scheme and switch to a matching theme accordingly.
To customize the themes that are used when a color scheme changes, you can set the preferred light, dark, and high contrast themes with the settings:
workbench.preferredLightColorTheme - defaults to &quot;Default Light+&quot;
workbench.preferredDarkColorTheme - defaults to &quot;Default Dark+&quot;
workbench.preferredHighContrastColorTheme - defaults to &quot;Default High Contrast&quot;
workbench.preferredHighContrastLightColorTheme - defaults to &quot;Default High Contrast Light&quot;

**参考链接**: https://apple.stackexchange.com/questions/381962/how-do-i-sync-the-visual-studio-code-vscode-theme-to-use-my-os-light-dark-colo

> 📎 来源 / Source: https://apple.stackexchange.com/questions/381962/how-do-i-sync-the-visual-studio-code-vscode-theme-to-use-my-os-light-dark-colo

#### 97. How to record both screen and sound with Quicktime on El Capitan?

**故障现象**: How to record both screen and sound with Quicktime on El Capitan?
**标签 / 来源**: Tags: macos, quicktime, screen-capture | apple | 👍 150 | 💬 12 answers

**问题描述**:
Tags: macos, quicktime, screen-capture | Score: 150 | Views: 438170 | Answers: 12

**解决方法 / 社区答案**:
You  need to install Soundflower in order to run it on El Capitan. El Capitan requires kext to be signed in order to load them. This one gets its kext installed in /Library/Extensions/.

This is due to System Integrity Protection

Then, you have to create a multi-output device with: Audio MIDI Setup.app, which is found in /Applications/Utilities/ :



Finally, when you want to do the actual recording, make sure you use this multi-output device, and capture from the same Soundflower device used in this multi-output device. Otherwise, you can't both listen to and capture the sound, because it goes directly to soundflower without being copied to the built-in output.

alt/option + right clicking on volume gives you this menu:



and Quicktime now looks like this:

**参考链接**: https://apple.stackexchange.com/questions/212829/how-to-record-both-screen-and-sound-with-quicktime-on-el-capitan

> 📎 来源 / Source: https://apple.stackexchange.com/questions/212829/how-to-record-both-screen-and-sound-with-quicktime-on-el-capitan

#### 98. Should I disconnect my MacBook Pro&#39;s power cord when the battery is fully charged?

**故障现象**: Should I disconnect my MacBook Pro&#39;s power cord when the battery is fully charged?
**标签 / 来源**: Tags: macbook-pro, battery, charging | apple | 👍 149 | 💬 12 answers

**问题描述**:
Tags: macbook-pro, battery, charging | Score: 149 | Views: 263777 | Answers: 12

**解决方法 / 社区答案**:
You do not need to disconnect your MacBook Pro's battery. Your battery will stop charging once it is full. Apple's modern batteries are much smarter than previous designs.

To get the most out of your MacBook Pro's battery, follow the Notebook Battery advice from Apple: unplug and use your battery until empty about once a month, then charge back up to full.

At the time of answering, Apple's advice read:


  For proper maintenance of a lithium-based battery, it’s important to keep the electrons in it moving occasionally. Apple does not recommend leaving your portable plugged in all the time. An ideal use would be a commuter who uses her notebook on the train, then plugs it in at the office to charge. This keeps the battery juices flowing.


If you need help following Apple's advice, use Battery Guardian; it is free and will remind you when to deplete your battery.

**参考链接**: https://apple.stackexchange.com/questions/12271/should-i-disconnect-my-macbook-pros-power-cord-when-the-battery-is-fully-charge

> 📎 来源 / Source: https://apple.stackexchange.com/questions/12271/should-i-disconnect-my-macbook-pros-power-cord-when-the-battery-is-fully-charge

#### 99. Is there a keyboard shortcut to navigate one level up in Finder?

**故障现象**: Is there a keyboard shortcut to navigate one level up in Finder?
**标签 / 来源**: Tags: macos, finder | apple | 👍 148 | 💬 1 answers

**问题描述**:
Tags: macos, finder | Score: 148 | Views: 91953 | Answers: 1

**解决方法 / 社区答案**:
The one you're probably looking for is the command ⬆︎ keyboard shortcut, as this is the one that takes you back to the parent folder. 

To do the same thing, but within a new window, use command control ⬆︎.

However, some views offer additional options. For example, in Columns view you can just use the ⬅︎ key to go back to the parent folder.

In addition, you can use the command [ keyboard shortcut to take you back to the previous folder you were actually in (which may not necessarily be the parent folder).

You can also right-click on the title in the Finder's window to select anywhere in the file's path to go straight to that location.

Finally, you can also customise the Toolbar to add the Path button.

**参考链接**: https://apple.stackexchange.com/questions/307930/is-there-a-keyboard-shortcut-to-navigate-one-level-up-in-finder

> 📎 来源 / Source: https://apple.stackexchange.com/questions/307930/is-there-a-keyboard-shortcut-to-navigate-one-level-up-in-finder

#### 100. How to investigate high kernel task memory usage?

**故障现象**: How to investigate high kernel task memory usage?
**标签 / 来源**: Tags: macos, memory, performance, kernel-panic, kernel | apple | 👍 147 | 💬 2 answers

**问题描述**:
Tags: macos, memory, performance, kernel-panic, kernel | Score: 147 | Views: 233652 | Answers: 2

**解决方法 / 社区答案**:
There are many things that go wrong with high kernel task usage. Usually this is related to faulty or heavy process which overusing system resources (such as indexing storage, running VMs, too many tabs in the web browser or some other background processes). 

Here are some methods which help to investigate OS X kernel usage issues:

Basic methods


Run Console.app and check on 'All Messages' to see if anything unusual currently is happening.
Use Activity Monitor to read system memory and determine how much CPU, RAM and Disk is being used.

Alternatively run top in Terminal and hold Space to refresh - easier to find the cause problem (swapins/swapouts/disks?).
Run sudo fs_usage in Terminal to report system calls and page faults related to filesystem activity in real-time (I think this is the best option from all other). Then hit Control-C to stop it.

Action: Consider killing apps which appears frequently on the list, but you're not using them.

Learn more at: How do I debug an out-of-control “kernel_task” process?
Run sudo syscallbypid.d (or syscallbyproc.d), wait a bit, hit Control-C. Now check which process generated the most system calls in that given time (last column) and if you recognise it, consider kill it. If not, Google it and learn more about it.


Advanced methods


Use sysdiagnose command (can be triggered by hitting Shift-Control-⌥-⌘-. (period) to quickly gather system-wide diagnostic information helpful in investigating system memory/performance issues (will appear in /var/tmp) either by you or Apple guys. During analysis, try to not do anything, when done - consider uncompressing the generated file and analyse the logs.

See: How do you get system diagnostic files from OS X?
Run footprint to gather detailed memory information on a per-VM-region type level and swapped bytes:

sudo footprint -a


Older version:

sudo footprint -all -categories -swapped -collapseSharing

Use spindump to profile entire system, it'll generate /tmp/spindump.txt file (including kernel and its extensions).
Use vm_stat to show virtual memory statistics. E.g.

vm_stat 1 # to display every second.

Use zprint to check information about kernel usage, it's possible by:

sudo zprint -t -s | head -n20


It'll show the most wasting kernel zones.
Use newproc.d to snoop new processes as they are executed, creatbyproc.d for files:

sudo newproc.d
sudo creatbyproc.d


Note: On newer OS X (10.11 or above) this may not work when integrity protection is enabled (check by csrutil status). 
Try sar - system activity reporter which can sample and report various cumulative statistic counters maintained by the operating system.


For more useful debugging tools, check for dtrace scripts (grep dtrace /usr/bin/*). If you know the faulty process which causing the problem, you may use dtruss to debug it.



Actions

Here are some suggestions which can help you with the operating system issues.


Free up some inactive memory. In order to do this, you've to flush cache first and force disk cache to be purged:

sync &amp;&amp; sudo purge



  sync - force completion of pending disk writes (flush cache)
  
  purge - force disk cache to be purged (flushed and emptied)


Its function is basically to terminate all the I/O pending operations which are using disk cache and then to free all the occupied disk cache, so it should free disk space to ease paging out and swapping out of main memory. It is safe to use, as it does not affect anonymous memory that has been allocated through malloc, vm_allocate, etc.
Use some 3rd party apps to clear up some overused memory such as iBoostUp, SystemPal, etc.
You may also disable temporary Spotlight:

sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist 


And consider other services by:

sudo launchctl list | grep ^[0-9]
sudo launchctl bslist | grep ^A

Quit your web browser and check if that helps. For example using Chrome is very resourceful, especially when there is some front-end processing going on in the background (e.g. Javascript) or advert-like animations are constantly rendering the content.

**参考链接**: https://apple.stackexchange.com/questions/178281/how-to-investigate-high-kernel-task-memory-usage

> 📎 来源 / Source: https://apple.stackexchange.com/questions/178281/how-to-investigate-high-kernel-task-memory-usage


---

## English 🇺🇸
**macOS Common Issues & Solutions**

Auto-updated hourly from Stack Exchange: common MACOS issues and community-verified solutions.

### MACOS Common Issues & Solutions

#### 1. Why am I getting an “invalid active developer path” when attempting to use Git after upgrading to macOS Tahoe?

**Issue**: Why am I getting an “invalid active developer path” when attempting to use Git after upgrading to macOS Tahoe?
**Tags / Source**: Tags: xcode, development, git, macos | apple | 👍 3062 | 💬 8 answers

**Description**:
Tags: xcode, development, git, macos | Score: 3062 | Views: 2593657 | Answers: 8

**Solution / Community Answer**:
Solution
Open Terminal, and run the following:
xcode-select --install

This will pop a dialogue box, Select &quot;Install&quot;, and it will download and install the Command Line Tools package and fix the problem.
(The popped Window may be behind other windows.)
You do not need Xcode, you can install only the Command Line Tools here, it is about 130 MB (600 MB as of Xcode v14.1).
If the above alone doesn't do it, then also run:
sudo xcode-select --reset

Further reading
The problem is that one needs to explicitly agree to the license agreement.  As a follow on step, you may need to reset the path to Xcode if you have several versions or want the command line tools to run without Xcode.
sudo xcode-select --switch /Applications/Xcode.app
sudo xcode-select --switch /Library/Developer/CommandLineTools

I found the solution in this question, Command Line Tools not working.
You may get an error message: &quot;Can't install the software because it is not currently available from the Software Update server&quot;. In this case xcode-select --reset works as pointed by akozin.

**Reference**: https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a

> 📎 Source: https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a

#### 2. List of all packages installed using Homebrew

**Issue**: List of all packages installed using Homebrew
**Tags / Source**: Tags: macos, command-line, homebrew, open-source | apple | 👍 1068 | 💬 11 answers

**Description**:
Tags: macos, command-line, homebrew, open-source | Score: 1068 | Views: 1439806 | Answers: 11

**Solution / Community Answer**:
brew list and brew list --cask
Running brew list will show a list of all your installed Homebrew formulae and casks.

If you wish to list casks only, brew list --cask will provide the items installed using Homebrew Cask.

**Reference**: https://apple.stackexchange.com/questions/101090/list-of-all-packages-installed-using-homebrew

> 📎 Source: https://apple.stackexchange.com/questions/101090/list-of-all-packages-installed-using-homebrew

#### 3. How to find cause of high kernel_task cpu usage?

**Issue**: How to find cause of high kernel_task cpu usage?
**Tags / Source**: Tags: macos, kernel | apple | 👍 712 | 💬 16 answers

**Description**:
Tags: macos, kernel | Score: 712 | Views: 615533 | Answers: 16

**Solution / Community Answer**:
TLDR; If your MacBook Pro runs hot or shows a high % CPU for the kernel task, try charging on the right and not on the left.

High kernel_task CPU Usage is due to high chassis temperature caused by charging. In particular Left Thunderbolt port usage.
Solutions include:

Move charging from the left to the right side. If you have a second charger then plug it in on the right side. Avoid plugging everything on the right side (see last paragraph below).
Unplug something from the left side. Either power or another accessory until the battery is full.
Force fans to max before plugging in. iStatMenus has an easy Sensors -&gt; Fans menu item to do so. This only helps in marginal conditions.
Move to a cooler room.
If using both laptop display and external display try switching to just one or the other (I switched to external only, laptop lid closed). Some MBP (eg 15&quot; Intel touchbar models) have a design quirk where this config can get hotter than it should.

Proof:
Actual CPU temperature or application CPU usage is uncorrelated with kernel_task. A hot CPU is throttled by reducing its clock speed, not by scheduling fake no-op load.
The graphs below are from iStatMenus. The machine had been used on battery then plugged in.
State A a USB-C hub (a mouse and keyboard, plus power) and a USB-C HDMI 2.0 adapter, both on the left side. You can see the Thunderbolt Left Proximity temperature sensor rise quickly. About 3-4 minutes later the dreaded kernel_task high CPU usage starts.
State B cures the kernel_task problem by moving power from the left ports to the right. The left side temperature drops and the kernel_task goes away within about 15 seconds.
This is causal. Moving power back to the left side, restoring State A, quickly restores the temperatures and kernel_task again comes back after 3-4 minutes. Again moving power back to the right side, restoring State B, resolves the problem immediately.
State C shows that simply having stuff plugged in to TB ports raises their temperature significantly. Both the hub (mouse and keyboard ONLY) and HDMI adapter individually raise the temperature about 10 degrees, and 15 degrees together.

(all other temperatures were both low and flat. Under 55 degrees.)
Note that high temperature on the right side appears to be ignored by the OS. Plugging everything into the two right ports instead of the left raised the Right temperatures to over 100 degrees, without the fans coming on. No kernel_task either, but the machine becomes unusable from something throttling.
Ergo, high CPU usage by kernel_task is caused by high Thunderbolt Left Proximity temperature, which is caused by charging and having normal peripherals plugged in at the same time.
2017 15&quot; Macbook Pro, MacOS 10.14.5

To actually answer the question:

How can I find out what this process is doing?

The only way to actually ask the kernel what it's doing is to attach a kernel debugger. That means getting a debug kernel from Apple, rebooting, then using a second Mac to attach to the debugged machine. You can then examine stack traces and guess what they mean.
Otherwise guessing and testing is the only way. Of course that leads to false conclusions more often than not.

**Reference**: https://apple.stackexchange.com/questions/363337/how-to-find-cause-of-high-kernel-task-cpu-usage

> 📎 Source: https://apple.stackexchange.com/questions/363337/how-to-find-cause-of-high-kernel-task-cpu-usage

#### 4. Shortcut for toggling between different windows of same app?

**Issue**: Shortcut for toggling between different windows of same app?
**Tags / Source**: Tags: macos, keyboard, google-chrome | apple | 👍 654 | 💬 15 answers

**Description**:
Tags: macos, keyboard, google-chrome | Score: 654 | Views: 935240 | Answers: 15

**Solution / Community Answer**:
UK Keyboard
[see below for other languages]
 Cmd ⌘   ` 
 Cmd ⌘   Shift ⇧    `  to go the other way.
Left of z on a UK keyboard [non-shifted ~ ]

Note: This only works if all windows are in the same Space, not if they are spread over multiple Spaces, or if any are fullscreen.
To overcome this for non-fullscreen window, use Cmd ⌘Tab as usual and on the icon of the application you want to switch windows in press the down arrow key (with Cmd ⌘ still pressed). Then use left/right keys to navigate to the desired window across spaces and desktops. To emphasise, This fails for any fullscreened windows, whilst continuing to work for any that are not.
You can also achieve this by right-clicking the app's icon in the Dock - this is the only method that will also switch to fullscreen windows, the other methods will not.
From comments - You can check which key command it is for your language by switching to Finder, then look at the Window menu for 'Cycle through windows'...

BTW, specifically in Chrome, Safari &amp; Firefox, but no other app I know of on Mac,  Cmd ⌘   (number)  will select individual tabs on the frontmost window.
It also would appear that  Cmd ⌘   `   is yet another of those language-specific shortcuts; so if anyone finds any more variants, please specify for which language &amp; keyboard type.
If anybody finds new combos for different languages, please check Keyboard layout here - This is a mirror of the very useful old Apple KB page, now gone from Apple How to identify keyboard localizations - &amp; add that as well as which Input Source you use in System Prefs &gt; Keyboard &gt; Input Sources.
Add a keyboard picture from the KB page too, if that would help.
That will make it easier for future Googlers.
Further info:
You can change the keys in System Settings… &gt; Keyboard &gt; Keyboard Shortcuts… &gt; Keyboard
though it doesn't list the reverse direction, it does still work when you add shift to that new combo. I tested by moving mine from  `   (and  ~ ) to  §  (and  ± )

You can use the alternative of  Ctrl ⌃   F4  [visible in the prefs window above] but that almost indiscriminately marches through every single open window on all Spaces, without switching to the correct Space each time. It's really not too useful unless you use a single Space, just included here for completeness.

**Reference**: https://apple.stackexchange.com/questions/193937/shortcut-for-toggling-between-different-windows-of-same-app

> 📎 Source: https://apple.stackexchange.com/questions/193937/shortcut-for-toggling-between-different-windows-of-same-app

#### 5. Please share your hidden macOS features or tips and tricks

**Issue**: Please share your hidden macOS features or tips and tricks
**Tags / Source**: Tags: macos | apple | 👍 612 | 💬 159 answers

**Description**:
Tags: macos | Score: 612 | Views: 346412 | Answers: 159

**Solution / Community Answer**:
In any Finder window or Open/Save dialog, you can hit ⌘&#x21E7;G (just '/' also works in Open/Save) to get a location bar from which you can directly type in the directory to go to. It even supports ~ for home and tab completion.

The Open/Save dialog has several other useful shortcuts:


⌘  R -
Reveals the selected item in a new
Finder window.
⌘  I - Info window shows for the selected item.
⌘  &#x21E7;  > - Shows/Hides hidden files in the dialog
⌘  F - cursor jumps to the Find text field
/ or ~ - Opens a Go To Folder dialogue. 
⌘  D or ⌘  &#x21E7; D - selects the ~/Desktop folder as a destination
⌘  &#x2325;  L - selects ~/Downloads folder as a destination
⌘  &#x21E7; O - selects ~/Documents folder as a destination
⌘  &#x2325;  S - Shows/Hides sidebar
⌘  . or esc - Cancels and closes the dialog window

**Reference**: https://apple.stackexchange.com/questions/400/please-share-your-hidden-macos-features-or-tips-and-tricks

> 📎 Source: https://apple.stackexchange.com/questions/400/please-share-your-hidden-macos-features-or-tips-and-tricks

#### 6. Remap &quot;Home&quot; and &quot;End&quot; to beginning and end of line

**Issue**: Remap &quot;Home&quot; and &quot;End&quot; to beginning and end of line
**Tags / Source**: Tags: macos, keyboard | apple | 👍 587 | 💬 13 answers

**Description**:
Tags: macos, keyboard | Score: 587 | Views: 228305 | Answers: 13

**Solution / Community Answer**:
The default shortcuts for moving to beginning or end of (wrapped) lines are ⌘← and ⌘→. ⌥↑ and ⌥↓ or ⌃A and ⌃E move to the beginning or end of unwrapped lines (or paragraphs). ⌥← and ⌥→ move backwards/forward by words, and all of these are compatible with holding Shift to select during the corresponding moves.
You could remap home and end by creating ~/Library/KeyBindings/ and saving a property list like this as DefaultKeyBinding.dict:
{
    &quot;\UF729&quot;  = moveToBeginningOfLine:; // home
    &quot;\UF72B&quot;  = moveToEndOfLine:; // end
    &quot;$\UF729&quot; = moveToBeginningOfLineAndModifySelection:; // shift-home
    &quot;$\UF72B&quot; = moveToEndOfLineAndModifySelection:; // shift-end
}

Most of the keybindings for editing text in OS X are defined in /System/Library/Frameworks/AppKit.framework/Resources/StandardKeyBinding.dict.
Applying changes requires reopening applications. DefaultKeyBinding.dict is ignored by some old versions of Xcode (works with latest version 6.3.1), Terminal, and many cross-platform applications.
See Cocoa Text System for more information about the customizable keybindings.
Terminal's keybindings can be customized in Preferences &gt; Profiles &gt; Settings &gt; Keyboard. \033OH moves to the beginning of a line and \033OF to the end of a line.
In Eclipse, key bindings should be modified in Preferences &gt; General &gt; Keys. You need to modify default bindings for commands Line Start and Line End (replace ⌘← by ↖ and ⌘→ by ↘). For selection to work, also modify Select Line Start and Select Line End.
PS: You may need to logout and login again for the ~/Library/KeyBindings/DefaultKeyBinding.dict change to take effect.

**Reference**: https://apple.stackexchange.com/questions/16135/remap-home-and-end-to-beginning-and-end-of-line

> 📎 Source: https://apple.stackexchange.com/questions/16135/remap-home-and-end-to-beginning-and-end-of-line

#### 7. How to prevent Mac from changing the order of Desktops/Spaces

**Issue**: How to prevent Mac from changing the order of Desktops/Spaces
**Tags / Source**: Tags: macos, mac, spaces, mission-control | apple | 👍 539 | 💬 2 answers

**Description**:
Tags: macos, mac, spaces, mission-control | Score: 539 | Views: 207135 | Answers: 2

**Solution / Community Answer**:
General Solution

System Settings/Preferences &gt; Search for &quot;Spaces&quot; &gt; Uncheck Automatically rearrange Spaces based on most recent use

Newer MacOS Ventura (v13)

System Settings &gt; Desktop &amp; Dock &gt; Scroll down to Mission Control section &gt; Uncheck Automatically rearrange Spaces based on most recent use



Older macOS (v12 and older)
System Preferences &gt; Mission Control
Uncheck Automatically rearrange Spaces based on most recent use.

This will fix the order of all your regular Spaces - but not Fullscreen spaces, which always go to the right of existing numbered Spaces.

From comments: Note this cannot fix the Mac confusing which external screen is which. That's not user-controlled at all, &amp; seems to occur mainly [though not always] when the external screens are identical.
Late note:
This echoes the behaviour of Cmd/Tab or equivalent in most operating systems, so could be considered a 'sensible' default.
 just to save this attracting even more comments on why it was a good/bad choice of default.

**Reference**: https://apple.stackexchange.com/questions/214348/how-to-prevent-mac-from-changing-the-order-of-desktops-spaces

> 📎 Source: https://apple.stackexchange.com/questions/214348/how-to-prevent-mac-from-changing-the-order-of-desktops-spaces

#### 8. How do I launch Finder from terminal or command line

**Issue**: How do I launch Finder from terminal or command line
**Tags / Source**: Tags: macos, applications, command-line | apple | 👍 508 | 💬 1 answers

**Description**:
Tags: macos, applications, command-line | Score: 508 | Views: 865921 | Answers: 1

**Solution / Community Answer**:
To open your current directory in Finder from Terminal, type open .
So, if you want Documents: open ~/Documents
Library: open ~/Library
Downloads: open ~/Downloads
And so on.

**Reference**: https://apple.stackexchange.com/questions/101432/how-do-i-launch-finder-from-terminal-or-command-line

> 📎 Source: https://apple.stackexchange.com/questions/101432/how-do-i-launch-finder-from-terminal-or-command-line

#### 9. Why does my dock keep moving back to my other monitor?

**Issue**: Why does my dock keep moving back to my other monitor?
**Tags / Source**: Tags: macbook-pro, macos, display, dock | apple | 👍 492 | 💬 8 answers

**Description**:
Tags: macbook-pro, macos, display, dock | Score: 492 | Views: 525765 | Answers: 8

**Solution / Community Answer**:
You can summon the Dock on a different display by moving the cursor to the bottom of the desired display, and then continuing moving down. It may be possible that this is occurring when you inadvertently perform that action.

I answered a similar question: cmd-tab behavior on Mavericks with multiple displays.

**Reference**: https://apple.stackexchange.com/questions/169719/why-does-my-dock-keep-moving-back-to-my-other-monitor

> 📎 Source: https://apple.stackexchange.com/questions/169719/why-does-my-dock-keep-moving-back-to-my-other-monitor

#### 10. How can I create a symbolic link in Terminal?

**Issue**: How can I create a symbolic link in Terminal?
**Tags / Source**: Tags: macos, command-line, file, symlink | apple | 👍 484 | 💬 7 answers

**Description**:
Tags: macos, command-line, file, symlink | Score: 484 | Views: 724804 | Answers: 7

**Solution / Community Answer**:
┌── ln(1) link, ln -- make links
│   ┌── Create a symbolic link.
│   │                         ┌── the optional path to the intended symlink
│   │                         │   if omitted, symlink is in . named as destination
│   │                         │   can use . or ~ or other relative paths
│   │                   ┌─────┴────────┐
ln -s /path/to/original /path/to/symlink
      └───────┬───────┘
              └── the path to the original file/folder
                  can use . or ~ or other relative paths


$ echo content &gt; original
$ ln -s original symlink
$ ls -la original symlink
-rw-r--r--  1 grgarside  staff    8 28 Jan 18:44 original
lrwxr-xr-x  1 grgarside  staff    8 28 Jan 18:44 symlink -&gt; original
$ cat symlink
content

For more information about ln(1) see the man page:
$ man ln

The path to the symlink is optional; if omitted, ln defaults to making a link with the same name as the destination, in the current directory:
$ cd ~/Documents
$ ln -s ../Pictures
$ ls -l Pictures
lrwxr-xr-x  1 user  staff  11 Feb  1 17:05 Pictures -&gt; ../Pictures

To create a symlink to replace a system directory (e.g. if you want to have /Users pointing to another disk drive), you need to disable System Integrity Protection. You can re-enable it after the symlink is set up.

**Reference**: https://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal

> 📎 Source: https://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal

#### 11. How do I find my IP Address from the command line?

**Issue**: How do I find my IP Address from the command line?
**Tags / Source**: Tags: macos, network, command-line | apple | 👍 451 | 💬 11 answers

**Description**:
Tags: macos, network, command-line | Score: 451 | Views: 1668077 | Answers: 11

**Solution / Community Answer**:
Local IP address
Use ipconfig getifaddr en0 or ipconfig getifaddr en1, depending on what network adapter your machine is using.
Public IP address
dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com

Output, e.g.:
172.79.136.120

Command explanation
The command you provided, dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com, is a command-line instruction that uses the dig utility to perform a DNS (Domain Name System) lookup. Let's break down the components of the command:

dig: dig stands for &quot;domain information groper,&quot; and it is a command-line tool commonly available on Unix-like systems for querying DNS servers.

-4: This option specifies that the command should use IPv4 protocol for the DNS lookup. It ensures that the query is sent using IPv4 instead of IPv6.

TXT: This indicates the type of DNS record being requested. In this case, the command is asking for the TXT record.

+short: This option is used to display only the relevant information from the DNS response, providing a concise output.

o-o.myaddr.l.google.com: This is the hostname used for the DNS lookup. It is a special hostname that Google uses to provide information about the IP address from which the DNS query originates.

@ns1.google.com: This specifies the DNS server to which the query is sent. In this case, it is set to ns1.google.com, which is one of Google's public DNS servers.


When you run this command, it queries the ns1.google.com DNS server for the TXT record associated with o-o.myaddr.l.google.com. The response will contain the TXT record, which typically includes information about the IP address of the client making the DNS query. The +short option ensures that only the relevant information is displayed, making it easier to read the output.

**Reference**: https://apple.stackexchange.com/questions/20547/how-do-i-find-my-ip-address-from-the-command-line

> 📎 Source: https://apple.stackexchange.com/questions/20547/how-do-i-find-my-ip-address-from-the-command-line

#### 12. mds and mds_stores constantly consuming cpu

**Issue**: mds and mds_stores constantly consuming cpu
**Tags / Source**: Tags: macbook-pro, spotlight, cpu | apple | 👍 450 | 💬 15 answers

**Description**:
Tags: macbook-pro, spotlight, cpu | Score: 450 | Views: 679869 | Answers: 15

**Solution / Community Answer**:
As you know, the mds and mds_stores are Spotlight activities.
The reason why your Spotlight is so active could be a number of things; it could be you have an app or multiple apps constantly changing some folder contents.
First let's check whether Spotlight is the cause of the fans running so much. To test this, run the following in your terminal:
sudo mdutil -a -i off

This will turn off indexing of files, and should result in a clear slow down of the fans if mds and/or mds_stores are to blame.
To turn indexing back on, run
sudo mdutil -a -i on

After this you could run the complete re-indexing of your hard drive (be aware this could be an over night job), it will delete your Spotlight data base forcing it to start over.
sudo rm -rf /System/Volumes/Data/.Spotlight-V100/*

The next and final step would be to add others to your (do not scan), privacy settings.

**Reference**: https://apple.stackexchange.com/questions/144474/mds-and-mds-stores-constantly-consuming-cpu

> 📎 Source: https://apple.stackexchange.com/questions/144474/mds-and-mds-stores-constantly-consuming-cpu

#### 13. How can I trigger a Notification Center notification from an AppleScript or shell script?

**Issue**: How can I trigger a Notification Center notification from an AppleScript or shell script?
**Tags / Source**: Tags: terminal, applescript, macos, notifications, command-line | apple | 👍 422 | 💬 13 answers

**Description**:
Tags: terminal, applescript, macos, notifications, command-line | Score: 422 | Views: 267265 | Answers: 13

**Solution / Community Answer**:
With Mavericks and later, you can do this using AppleScript's 'display notification':

display notification "Lorem ipsum dolor sit amet" with title "Title"


                          

That's it—literally that simple! No 3rd-party libraries or apps required and is completely portable for use on other systems. 10.9 notification on the top, 10.10 DP in the middle, 10.10 on the bottom.

AppleScript can be run from the shell using /usr/bin/osascript:

osascript -e 'display notification "Lorem ipsum dolor sit amet" with title "Title"'


You can also customise the alert further by adding…


a subtitle

Append 'subtitle' followed by the string or variable containing the subtitle.

display notification "message" with title "title" subtitle "subtitle"


The above example produces the following notification:


sound

Append 'sound name' followed by the name of a sound that will be played along with the notification.

display notification "message" sound name "Sound Name"


Valid sound names are the names of sounds located in…


~/Library/Sounds
/System/Library/Sounds





Posting notifications can be wrapped as a command-line script. The following code can be run in Terminal and will add a script to /usr/local/bin (must exist, add to $PATH) called notify.

cd /usr/local/bin &amp;&amp; echo -e "#!/bin/bash\n/usr/bin/osascript -e \"display notification \\\"\$*\\\"\"" &gt; notify &amp;&amp; chmod +x notify;cd -


This is the script that the above will add to notify.

#!/bin/bash
/usr/bin/osascript -e "display notification \"$*\""


Now to display a notification:

notify Lorem ipsum dolor sit amet
sleep 5; notify Slow command finished

**Reference**: https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel

> 📎 Source: https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel

#### 14. Got any tips or tricks for Terminal in Mac OS X?

**Issue**: Got any tips or tricks for Terminal in Mac OS X?
**Tags / Source**: Tags: mac, terminal, macos | apple | 👍 404 | 💬 133 answers

**Description**:
Tags: mac, terminal, macos | Score: 404 | Views: 249648 | Answers: 133

**Solution / Community Answer**:
You can hold option and click a position in the current line to move your cursor to that position.

**Reference**: https://apple.stackexchange.com/questions/5435/got-any-tips-or-tricks-for-terminal-in-mac-os-x

> 📎 Source: https://apple.stackexchange.com/questions/5435/got-any-tips-or-tricks-for-terminal-in-mac-os-x

#### 15. How can I configure Mac Terminal to have color ls output?

**Issue**: How can I configure Mac Terminal to have color ls output?
**Tags / Source**: Tags: macos, terminal | apple | 👍 397 | 💬 13 answers

**Description**:
Tags: macos, terminal | Score: 397 | Views: 336045 | Answers: 13

**Solution / Community Answer**:
Edit:

~/.bash_profile


or

~/.profile


and add the following line to simply enable color output via ls:

export CLICOLOR=1


To customize the coloring shown by ls you can optionally add this variable, LSCOLORS.

Examples


Default

export LSCOLORS=ExFxCxDxBxegedabagacad

You can use this if you are using a black background

export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx

If you'd like to mimic the colors of a typical Linux terminal:

export LSCOLORS=ExGxBxDxCxEgEdxbxgxcxd



Once you've add the above to either ~/.bash_profile or ~/.profile you can either logout/login or source the file in your shell, for eg:

$ . ~/.bash_profile


NOTE: If you need help in selecting colors to use you can use this online tool called LSCOLORS Generator.

**Reference**: https://apple.stackexchange.com/questions/33677/how-can-i-configure-mac-terminal-to-have-color-ls-output

> 📎 Source: https://apple.stackexchange.com/questions/33677/how-can-i-configure-mac-terminal-to-have-color-ls-output

#### 16. What are the practical differences between Bash and Zsh?

**Issue**: What are the practical differences between Bash and Zsh?
**Tags / Source**: Tags: terminal, bash, zsh, macos | apple | 👍 389 | 💬 4 answers

**Description**:
Tags: terminal, bash, zsh, macos | Score: 389 | Views: 337246 | Answers: 4

**Solution / Community Answer**:
First, some important things:

Bash isn't going away. If you're already using bash, nothing will change for you. All that changes is that zsh will be the default login shell for new accounts, and even then, you can select bash instead.
Scripts are not affected. What changes is the shell for interactive use, i.e. the shell in terminals (and also a few other things that use the login shell, such as crontabs). If you have a script in a file with execution permissions, starting with a shebang line such as #!/bin/bash or #!/bin/sh or #!/usr/bin/env bash, it'll keep working exactly as before.
Zsh's syntax is not completely compatible with bash, but it's close. A lot of code will keep working, for example typical aliases and functions. The main differences are in interactive configuration features.

Now, assuming you're considering switching to zsh, which has been a possibility for years, here are the main differences you'll encounter. This is not an exhaustive list!
Main differences for interactive use
Configuration files: bash reads (mainly) .bashrc in non-login interactive shells (but macOS starts a login shell in terminals by default), .profile or .bash_profile in login shells, and .inputrc. Zsh reads (mainly) .zshrc (in all interactive shells) and .zprofile (in login shells). This means that none of your bash customizations will apply: you'll need to port them over. You can't just copy the files because many things will need tweaking.
Key bindings use completely different syntax. Bash uses .inputrc and the bind builtin to bind keys to readline commands. Zsh uses the bindkey builtin to bind keys to zle widgets. Most readline commands have a zsh equivalent, but it isn't always a perfect equivalence.
Speaking of key bindings, if you use Vi(m) as your in-terminal editor but not as your command line mode in the shell, you'll notice zsh defaults to vi editing mode (i.e. with command and insert modes) if EDITOR or VISUAL is set to vi or vim. bindkey -e switches to emacs mode (i.e. where you can always type directly).
Prompt: bash sets the prompt (mainly) from PS1 which contains backslash escapes. Zsh sets the prompt mainly from PS1 which contains percent escapes. Although the concepts are similar, the escape codes are completely different. The functionality of bash's PROMPT_COMMAND is available in zsh via the precmd and preexec hook functions. Zsh has more convenience mechanisms to build fancy prompts including a prompt theme mechanism.
The basic command line history mechanisms (navigation with Up/Down, search with Ctrl+R, history expansion with !! and friends, last argument recall with Alt+. or $_) work in the same way, but there are a lot of differences in the details, too many to list here. You can copy your .bash_history to .zsh_history if you haven't changed a shell option that changes the file format.
Completion: both shells default to a basic completion mode that mostly completes command and file names, and switch to a fancy mode by including bash_completion on bash or by running compinit in zsh. You'll find some commands that bash handles better and some that zsh handles better. Zsh is usually more precise, but sometimes gives up where bash does something that isn't correct but is sensible. To specify possible completions for a command, zsh has three mechanisms:

The “old” completion mechanism with compctl which you can forget about.
The “new” completion mechanism with compadd and lots of functions that begin with underscore and a powerful but complex user configuration mechanism.
An emulation to support bash completion functions which you can enable by running bashcompinit. The emulation isn't 100% perfect but it usually works.

Many of bash's shopt settings have a corresponding setopt in zsh.
Zsh doesn't treat # as a comment start on the command line by default, only in scripts (including .zshrc and such). To enable interactive comments, run setopt interactive_comments.
Main differences for scripting
(and for power users on the command line of course)
In bash, $foo takes the value of foo, splits it at whitespace characters, and for each whitespace-separated part, if it contains wildcard characters and matches an existing file, replaces the pattern by the list of matches. To just get the value of foo, you need &quot;$foo&quot;. The same applies to command substitution $(foo). In zsh, $foo is the value of foo and $(foo) is the output of foo minus its final newlines, with two exceptions. If a word becomes empty due to expanding empty unquoted variables, it's removed (e.g. a=; b=; printf &quot;%s\n&quot; one &quot;$a$b&quot; three $a$b five prints one, an empty line, three, five). The result of an unquoted command substitution is split at whitespace but the pieces don't undergo wildcard matching.
Bash arrays are indexed from 0 to (length-1). Zsh arrays are indexed from 1 to length. You can make 0-indexing the default with setopt ksh_arrays. Zsh requires fewer braces (unless ksh_arrays is enabled). For example, suppose a=(first second third &quot;&quot; last).




Functionality
Bash syntax
Idiomatic zsh syntax
Expansion




First element
${a[0]}
$a[1]
first


Second element
${a[1]}
$a[2]
second


Last element
${a[${#a[@]}-1]}
$a[-1]
last


Length
${#a[@]}
$#a
5


All the elements
&quot;${a[@]}&quot;
&quot;${a[@]}&quot; or &quot;${(@)a}&quot;
first second third (empty word) last


All the non-empty elements

$a
first second third last




Bash has extra wildcard patterns such as @(foo|bar) to match foo or bar, which are only enabled with shopt -s extglob. In zsh, you can enable these patterns with setopt ksh_glob, but there's also a simpler-to-type native syntax such as (foo|bar), some of which requires setopt extended_glob (do put that in your .zshrc, and it's on by default in completion functions). Zsh has **/ for recursive directory traversal (as does modern bash but not the bash 3.2 that ships with macOS).
In bash, by default, if a wildcard pattern doesn't match any file, it's left unchanged. In zsh, by default, you'll get an error, which is usually the safest setting. If you want to pass a wildcard parameter to a command, use quotes. You can switch to the bash behavior with setopt no_nomatch. You can make non-matching wildcard patterns expand to an empty list instead with setopt null_glob.
In bash, the right-hand side of a pipeline runs in a subshell. In zsh, it runs in the parent shell, so you can write things like somecommand | read output.
Some nice zsh features
Here are a few nice zsh features that bash doesn't have (at least not without some serious elbow grease). Once again, this is just a selection of the ones I consider the most useful.
Glob qualifiers allow matching files based on metadata such as their time stamp, their size, etc. They also allow tweaking the output. The syntax is rather cryptic, but it's extremely convenient. Here are a few examples:

foo*(.): only regular files matching foo* and symbolic links to regular files, not directories and other special files.
foo*(*.): only executable regular files matching foo*.
foo*(-.): only regular files matching foo*, not symbolic links and other special files.
foo*(-@): only dangling symbolic links matching foo*.
foo*(om): the files matching foo*, sorted by last modification date, most recent first. Note that if you pass this to ls, it'll do its own sorting. This is especially useful in…
foo*(om[1,10]): the 10 most recent files matching foo*, most recent first.
foo*(Lm+1): files matching foo* whose size is at least 1MB.
foo*(N): same as foo*, but if this doesn't match any file, produce an empty list regardless of the setting of the null_glob option (see above).
*(D): match all files including dot files (except . and ..).
foo/bar/*(:t) (using a history modifier): the files in foo/bar, but with only the base name of the file. E.g. if there is a foo/bar/qux.txt, it's expanded as qux.txt.
foo/bar/*(.:r): take regular files under foo/bar and remove the extension. E.g. foo/bar/qux.txt is expanded as foo/bar/qux.
foo*.odt(e\''REPLY=$REPLY:r.pdf'\'): take the list of files matching foo*.odt, and replace .odt by .pdf (regardless of whether the PDF file exists).

Here are a few useful zsh-specific wildcard patterns.

foo*.txt~foobar*: all .txt files whose name starts with foo but not foobar.
image&lt;-&gt;.jpg(n): all .jpg files whose base name is image followed by a number, e.g. image3.jpg and image22.jpg but not image-backup.jpg. The glob qualifier (n) causes the files to be listed in numerical order, i.e. image9.jpg comes before image10.jpg (you can make this the default even without -n with setopt numeric_glob_sort).

To mass-rename files, zsh provides a very convenient tool: the zmv function. Suggested for your .zshrc:
autoload zmv
alias zcp='zmv -C' zln='zmv -L'

Example:
zmv '(*).jpeg' '$1.jpg'
zmv '(*)-backup.(*)' 'backups/$1.$2'

Bash has a few ways to apply transformations when taking the value of a variable. Zsh has some of the same and many more.
Zsh has a number of little convenient features to change directories. Turn on setopt auto_cd to change to a directory when you type its name without having to type cd (bash also has this nowadays). You can use the two-argument form to cd to change to a directory whose name is close to the current directory. For example, if you're in /some/where/foo-old/deeply/nested/inside and you want to go to /some/where/foo-new/deeply/nested/inside, just type cd old new.
To assign a value to a variable, you of course write VARIABLE=VALUE. To edit the value of a variable interactively, just run vared VARIABLE.
Final advice
Zsh comes with a configuration interface that supports a few of the most common settings, including canned recipes for things like case-insensitive completion. To (re)run this interface (the first line is not needed if you're using a configuration file that was edited by zsh-newuser-install):
autoload -U zsh-newuser-install
zsh-newuser-install

Out of the box, with no configuration file at all, many of zsh's useful features are disabled for backward compatibility with 1990's versions. zsh-newuser-install suggests some recommended features to turn on.
There are many zsh configuration frameworks on the web (many of them are on Github). They can be a convenient way to get started with some powerful features. The flip side of the coin is they often lock you in doing things the way the author does, so sometimes they'll prevent you from doing things the way you want. Use them at your own risk.
The zsh manual has a lot of information, but it's often written in a way that's terse and hard to follow, and has few examples. Don't hesitate to search for explanations and examples online: if you only use the part of zsh that's easy to understand in the manual, you'll miss out. Two good resources are the zsh-users mailing list and Unix Stack Exchange.
An extensive collection of articles on switching to zsh on the mac can be found on scriptingosx.com and a useful Ruby script to bring your command history with you, can be found on Github.

**Reference**: https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh

> 📎 Source: https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh

#### 17. How can I list my open network ports with netstat?

**Issue**: How can I list my open network ports with netstat?
**Tags / Source**: Tags: macos, network, command-line | apple | 👍 375 | 💬 7 answers

**Description**:
Tags: macos, network, command-line | Score: 375 | Views: 1062787 | Answers: 7

**Solution / Community Answer**:
netstat -anvp tcp | awk 'NR&lt;3 || /LISTEN/'
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)     rhiwat shiwat    pid   epid  state    options
tcp46      0      0  *.62981                *.*                    LISTEN      131072 131072  34548      0 0x0100 0x00000006
…


sudo lsof -PiTCP -sTCP:LISTEN
COMMAND     PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
BetterTou 34548 grgarside   20u  IPv4 0xa42a1d0ade5d3585      0t0  TCP *:62981 (LISTEN)
BetterTou 34548 grgarside   21u  IPv6 0xa42a1d0ad67f7a5d      0t0  TCP *:62981 (LISTEN)
…

**Reference**: https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat

> 📎 Source: https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat

#### 18. How do I recompile Bash to avoid Shellshock (the remote exploit CVE-2014-6271 and CVE-2014-7169)?

**Issue**: How do I recompile Bash to avoid Shellshock (the remote exploit CVE-2014-6271 and CVE-2014-7169)?
**Tags / Source**: Tags: macos, security, bash | apple | 👍 371 | 💬 7 answers

**Description**:
Tags: macos, security, bash | Score: 371 | Views: 269147 | Answers: 7

**Solution / Community Answer**:
Status

Apple has released Bash security fixes for Shellshock and related vulnerabilities as "OS X bash Update 1.0". They can be installed through normal system update for people using OS X Mountain Lion v10.8.5 or OS X Mavericks v10.9.5 (they are included in Security Update 2014-005) and can also be installed manually. Official Apple fixes are also available for OS X Lion v10.7.5 and OS X Lion Server v10.7.5 but those are only available via manual download. The security fixes are available via different URLs based on the operating system version:


http://support.apple.com/kb/DL1769 - Mavericks (10.9.5 and above)
http://support.apple.com/kb/DL1768 - Mountain Lion (10.8.5)
http://support.apple.com/kb/DL1767 - Lion &amp; Lion Server (10.7.5)


(If new patches are released, put them here but please keep these existing ones as well for reference.)

The Apple patch takes care of Shellshock and several other vulnerabilities and is fine for most people. tl;dr people can stop reading here.

HOWEVER, the attention drawn to bash by the Shellshock bug has caused many researchers to take a hard look at bash and more and more (hard to exploit) vulnerabilities keep being found. If you are highly concerned about security (because maybe you are running OS X Server to host a publicly available web site) then you may want to (try to) keep up with the vulnerabilities and patches as they keep rolling in by compiling bash yourself. Otherwise, don't worry about it.

Look for Apple to release another update to bash some time in the future when the dust settles on finding further vulnerabilities. 



An official set of patches of bash itself for bash 3.2, patches 52, 53, and 54 (which correspond to Bash 4.3 patches 25, 26, and 27) are available which fix both CVE-2014-6271 and CVE-2014-7169, as well as the 'Game over' displayed below. This has been tested by me (@alblue) and the post has been updated accordingly (and then additional updates were made: see revision 41 for the post that stops at patch 54). 

Many additional vulnerabilities have been reported against bash. According to Michal Zalewski's post if you have patch 54 (and presumably Apple's official patch) "there's no point in obsessing about the status of these individual bugs, because they should no longer pose a security risk:"


CVE-2014-6271 - original RCE found by Stephane. Fixed by bash43-025
and corresponding Sep 24 entries for other versions.
CVE-2014-7169 - file creation / token consumption bug found by
Tavis. Fixed by bash43-026 &amp; co (Sep 26)
CVE-2014-7186 - a probably no-sec-risk 10+ here-doc crash found by
Florian and Todd. Fixed by bash43-028 &amp; co (Oct 1).
CVE-2014-7187 - a non-crashing, probably no-sec-risk off-by-one
found by Florian.  Fixed by bash43-028 &amp; co (Oct 1).
CVE-2014-6277 - uninitialized memory issue, almost certainly RCE
found by Michal Zalewski. No specific patch yet.
CVE-2014-6278 - command injection RCE found by Michal Zalewski. No specific patch yet.


It gets pretty confusing. Fortunately Chet Ramey, the official bash maintainer, posted a CVE to patch mapping. His post refers to patches for bash 4.3, I (@OldPro) have translated them to patches for bash 3.2, which is what is applicable to OS X. Also, since this post he has released patch 57, so I added that below:

 bash32-052      CVE-2014-6271                           2014-09-24
 bash32-053      CVE-2014-7169                           2014-09-26
 bash32-054      exported function namespace change      2014-09-27 ("Game Over")
 bash32-055      CVE-2014-7186/CVE-2014-7187             2014-10-01
 bash32-056      CVE-2014-6277                           2014-10-02
 bash32-057      CVE-2014-6278                           2014-10-05


See David A. Wheeler's post for a timeline and greater detail. 

@alblue posted build instructions through patch 55. I (@OldPro) added patch 56 and 57 to the instructions but have not tested it.

Testing for the original Vulnerability

You can determine if you are vulnerable to the original problem in CVE-2014-6271 by executing this test:

$ env x='() { :;}; echo vulnerable' bash -c 'echo hello'
bash: warning: x: ignoring function definition attempt
bash: error importing function definition for `x'
hello


The above output is an example of a non-vulnerable bash version. If you see the word vulnerable in the output of that command your bash is vulnerable and you should update. Below is a vulnerable version from OS X 10.8.5:



Testing for the new Vulnerability

There has been an update to the original post and Bash 3.2.52(1) is still vulnerable to a variation of the vulnerability, defined in CVE-2014-7169 

$ rm -f echo
$ env X='() { (a)=&gt;\' sh -c "echo date"; cat echo
sh: X: line 1: syntax error near unexpected token `='
sh: X: line 1: `'
sh: error importing function definition for `X'
Thu 25 Sep 2014 08:50:18 BST


The above output is an example of a vulnerable bash version. If you see a date in the output of that command your bash is vulnerable.

Disabling auto-imported functions to prevent "Game Over"

Researchers noted, without classifying it as a vulnerability, that a script could hijack a function in a subshell using auto-imported functions:

$ env ls="() { echo 'Game Over'; }" bash -c ls
Game over


The above code on an affected system would display Game Over instead of the directory listing you would expect from ls. Obviously, echo 'Game Over' could be replaced by any nefarious code you want. This became know as the "Game Over" bug.

Prior to the availability of patch 54, both NetBSD and FreeBSD disabled auto-importing bash functions by default, partly to prevent "Game Over" but mainly to contain any further errors in the parser (such as CVE-2014-7169) as they were continuing to be discovered, and added a new command line flag --import-functions to re-enable the old default behavior. I (@alblue) have prepared a patch (against 3.2.53) for others to use if they want to adopt this behaviour as well and have included it below. By default this patch is not enabled in the build script below. I (@OldPro) believe this patch is no longer necessary or a good idea, because it breaks backwards compatibility and the vulnerabilities it protects against are very well addressed by patch 54 and earlier patches, and enabling this unofficial patch prevents future patches from being applied. 

(Note to question editors; please do not enable this by default, as it is an unofficial patch.)

a0c5c4d66742fddd0a35001cb91798a5fbf8a2f5  import_functions.patch

The patch can be enabled by running export ADD_IMPORT_FUNCTIONS_PATCH=YES before running the build. Note that enabling this patch will disable patch 54 and any future patches because future patches cannot be guaranteed to be compatible with the unofficial patch.

Apple Patch has Game Over vulnerability, sort of

As pointed out by @ake_____ on twitter the official Apple patch is still vulnerable to environment clobbering of executables:

$ env '__BASH_FUNC&lt;ls&gt;()'="() { echo Game Over; }" bash -c ls
Game Over


Users should decide for themselves how important this is. I (@OldPro) think it is nothing to worry about because there is no known exploit for this behavior (it was not even given a CVE identifier) because in general unprivileged remote attackers cannot set the name of an environment variable and attackers with privileges cannot use this to gain privileges they do not already have (at least not without exploiting an additional vulnerabiltiy). 

To provide a little background, bash allows you to define functions, and furthermore allows you to export those functions to subshells via the export -f command. This used to be implemented by creating an environment variable with the same name as the function with its value set to the function definition. So

$ ls () { echo 'Game Over'; }
$ export -f ls
$ echo $ls
Game Over


This happened because export -f ls created an environment variable named ls. The "Game Over" vulnerability was that you could directly create this environment variable without having to first define the function, which meant if you could inject the right variable name you could hijack a command. Apple tried to fix this by making it hard to create a variable with the right name. The official bash patch 54 actually makes it impossible to create a variable with the right name by using variable names that include % which is a character not allowed in a variable name, effectively putting exported function definitions in a different, reserved namespace.

If none of the above makes sense to you, don't worry about it. You are fine with the Apple patch for now.

System Binaries

OS X 10.9.5 (the latest stable release at the moment) ships with Bash v3.2.51:

$ bash --version
GNU bash, version 3.2.51(1)-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.


You can obtain and recompile Bash as follows, providing that you have Xcode installed (and have run xcodebuild at least once before to accept the license):

$ # If you want to disable auto-imported functions, uncomment the following
$ # export ADD_IMPORT_FUNCTIONS_PATCH=YES
$ mkdir bash-fix
$ cd bash-fix
$ curl https://opensource.apple.com/tarballs/bash/bash-92.tar.gz | tar zxf -
$ cd bash-92/bash-3.2
$ curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-052 | patch -p0    
$ curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-053 | patch -p0  
$ # See note above about ADD_IMPORT_FUNCTIONS_PATCH
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] &amp;&amp; curl http://alblue.bandlem.com/import_functions.patch | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-054 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-055 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-056 | patch -p0
$ [ "$ADD_IMPORT_FUNCTIONS_PATCH" == "YES" ] || curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-057 | patch -p0
$ cd ..
$ # Note: DO NOT ADD SUDO TO XCODEBUILD HERE
$ xcodebuild
$ build/Release/bash --version # GNU bash, version 3.2.57-release
$ build/Release/sh --version   # GNU bash, version 3.2.57-release
$ sudo cp /bin/bash /bin/bash.old
$ sudo cp /bin/sh /bin/sh.old
$ sudo cp build/Release/bash /bin
$ sudo cp build/Release/sh /bin


(Note: you can run this by copy-and-pasting the above code block, going into Terminal and then running pbpaste | cut -c 2- | sh. Always take care when running random scripts from the internet though ...)

After this, the Bash version should be v3.2.57:

$ bash --version
GNU bash, version 3.2.57-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.


For security, and after testing, I recommend that you chmod -x the old versions to ensure they aren't re-used, or move them to a backup site.

$ sudo chmod a-x /bin/bash.old /bin/sh.old


Other answers have solutions for those using MacPorts or Homebrew; these don't fix the problem, they just install additional versions of Bash. Please see those answers if you want to upgrade those specifically.

Thanks

Thanks to Chet, who looks after bash, and has been making these patches available. Thanks to everyone else who has commented on this and improved it over time.

Now Apple has released the real fix, though this might still be useful. Because they only released a fix for Lion and up, and the official patch provides GNU bash, version 3.2.53(1)-release (x86_64-apple-darwin13), however, the Game over bug is still somewhat vulnerable. At this point, rebuilding your own version of Bash against 3.2.57 is probably more secure than relying on Apple's patch, unless you do it wrong.

**Reference**: https://apple.stackexchange.com/questions/146849/how-do-i-recompile-bash-to-avoid-shellshock-the-remote-exploit-cve-2014-6271-an

> 📎 Source: https://apple.stackexchange.com/questions/146849/how-do-i-recompile-bash-to-avoid-shellshock-the-remote-exploit-cve-2014-6271-an

#### 19. How to combine two images into one on a Mac?

**Issue**: How to combine two images into one on a Mac?
**Tags / Source**: Tags: macos, software-recommendation, image-editing | apple | 👍 365 | 💬 19 answers

**Description**:
Tags: macos, software-recommendation, image-editing | Score: 365 | Views: 884014 | Answers: 19

**Solution / Community Answer**:
I often have to do this with images of plots of data.  I use the command line tools that come in the Imagemagick package; I think I installed it on my system with MacPorts. You could also choose to install with brew (brew install imagemagick).
The actual tool you want to use from Imagemagick is the convert tool.  If you have your two 320x428 images, say a.png and b.png, you can do
convert +append a.png b.png c.png

to create a new file, c.png, that has the a.png on the left and b.png on the right.  Alternatively, you append them vertically with -append (instead of +) and a.png will be on top of b.png.  With convert, you can do a ton of other things.  For example, you can switch to a different image format for the output
convert +append a.png b.jpg c.tif

This isn't a GUI application, but maybe some others might have a better solution.  Alternatively, you could put this in some sort of automator script.
2020-12-10：
I used it on 2020-12-10 and now the correct code is
convert +append a.png b.jpg +append c.tif

**Reference**: https://apple.stackexchange.com/questions/52879/how-to-combine-two-images-into-one-on-a-mac

> 📎 Source: https://apple.stackexchange.com/questions/52879/how-to-combine-two-images-into-one-on-a-mac

#### 20. How do I downgrade node or install a specific previous version using homebrew?

**Issue**: How do I downgrade node or install a specific previous version using homebrew?
**Tags / Source**: Tags: macos, homebrew | apple | 👍 362 | 💬 13 answers

**Description**:
Tags: macos, homebrew | Score: 362 | Views: 676196 | Answers: 13

**Solution / Community Answer**:
These days if you want to install a different version of node you do it this way:
First search for your desired package:
brew search node

This might give you the follow results:
heroku/brew/heroku-node ✔
node ✔
node@10
node_exporter
nodenv
libbitcoin-node
node-build
node@12 ✔
node@14 ✔
...

And then install the desired version:
brew install node@14

Also remember that you can install more than 1 node package at the same time, but you cannot have them available at the same time. So if you have the latest/generic node package already installed you need to unlink it first:
brew unlink node

And then you can link a different version:
brew link node@14

Sometimes it might be required to link them with the --force and --overwrite options:
brew link --force --overwrite node@14

However, when new node version comes out and you’ll update to it by running brew upgrade, the link will be removed and the most recent node version will be linked instead. To remedy that you might consider adding your desired node version to PATH instead (and restart the shell):
echo 'export PATH=&quot;/usr/local/opt/node@14/bin:$PATH&quot;' &gt;&gt; ~/.zshrc

(replace .zshrc with .bashrc or similar, depending on which $SHELL you use)

**Reference**: https://apple.stackexchange.com/questions/171530/how-do-i-downgrade-node-or-install-a-specific-previous-version-using-homebrew

> 📎 Source: https://apple.stackexchange.com/questions/171530/how-do-i-downgrade-node-or-install-a-specific-previous-version-using-homebrew

#### 21. How can I disable animation when switching desktops in Lion?

**Issue**: How can I disable animation when switching desktops in Lion?
**Tags / Source**: Tags: macos, spaces | apple | 👍 352 | 💬 6 answers

**Description**:
Tags: macos, spaces | Score: 352 | Views: 135252 | Answers: 6

**Solution / Community Answer**:
I posted a bug on Radar#28495374 and here is the response from Apple:

Fixed in 10.12.  Go to Accessibility and Turn on Reduce Motion…
Please let us know whether the issue is resolved for you by updating your bug report.

**Reference**: https://apple.stackexchange.com/questions/17929/how-can-i-disable-animation-when-switching-desktops-in-lion

> 📎 Source: https://apple.stackexchange.com/questions/17929/how-can-i-disable-animation-when-switching-desktops-in-lion

#### 22. How to change computer name so terminal displays it in Mac OS X Mountain Lion?

**Issue**: How to change computer name so terminal displays it in Mac OS X Mountain Lion?
**Tags / Source**: Tags: sharing, macos, hosts | apple | 👍 326 | 💬 8 answers

**Description**:
Tags: sharing, macos, hosts | Score: 326 | Views: 761810 | Answers: 8

**Solution / Community Answer**:
If you use:
sudo scutil --set HostName name-you-want

it will work a bit better. From the scutil(8) man page:

--get pref
    Retrieves the specified preference.  The current value will be
    reported on standard output.

    Supported preferences include:
          ComputerName   The user-friendly name for the system.
          LocalHostName  The local (Bonjour) host name.
          HostName       The name associated with hostname(1) and gethostname(3).

--set pref [newval]
    Updates the specified preference with the new value.  If the new value is not
    specified on the command line then it will be read from standard input.

    Supported preferences include: ComputerName LocalHostName HostName

    The --set option requires super-user access.

**Reference**: https://apple.stackexchange.com/questions/66611/how-to-change-computer-name-so-terminal-displays-it-in-mac-os-x-mountain-lion

> 📎 Source: https://apple.stackexchange.com/questions/66611/how-to-change-computer-name-so-terminal-displays-it-in-mac-os-x-mountain-lion

#### 23. Can I get the CPU temperature and fan speed from the command line in OS X?

**Issue**: Can I get the CPU temperature and fan speed from the command line in OS X?
**Tags / Source**: Tags: macos, temperature, command-line, monitoring | apple | 👍 324 | 💬 14 answers

**Description**:
Tags: macos, temperature, command-line, monitoring | Score: 324 | Views: 574589 | Answers: 14

**Solution / Community Answer**:
Option #1) you may consider using inbuilt utility powermetrics to get the cpu and gpu temperature and lot more other details.
To get CPU temperature:
sudo powermetrics --samplers smc |grep -i &quot;CPU die temperature&quot;


To get GPU temperature:
sudo powermetrics --samplers smc |grep -i &quot;GPU die temperature&quot;

To get lot more details:
sudo powermetrics

This has been tested on macbook pro with macOS mojave.
Option #2)
Install Intel® Power Gadget officially provided by Intel from here
Intel® Power Gadget and then launch Intel Power Gadget from the launchpad.

Result Screen:

**Reference**: https://apple.stackexchange.com/questions/54329/can-i-get-the-cpu-temperature-and-fan-speed-from-the-command-line-in-os-x

> 📎 Source: https://apple.stackexchange.com/questions/54329/can-i-get-the-cpu-temperature-and-fan-speed-from-the-command-line-in-os-x

#### 24. Hotkey to show hidden files and folders in File Open dialog?

**Issue**: Hotkey to show hidden files and folders in File Open dialog?
**Tags / Source**: Tags: macos | apple | 👍 323 | 💬 3 answers

**Description**:
Tags: macos | Score: 323 | Views: 200603 | Answers: 3

**Solution / Community Answer**:
⌘ CMD+⇧ SHIFT+. reveals hidden files in Finder and Open/Save dialogs.

If you are using an AZERTY keyboard, you'll need to press fn too, so ⇧ SHIFT is taken into consideration as you already need it to make the ..



You can also press ⌘ CMD+⇧ SHIFT+G and type the path to the hidden folder, just like in Terminal (⇥ TAB autocompletion also works).

Editing hidden files can be dangerous if you don't know what you're doing.

**Reference**: https://apple.stackexchange.com/questions/186376/hotkey-to-show-hidden-files-and-folders-in-file-open-dialog

> 📎 Source: https://apple.stackexchange.com/questions/186376/hotkey-to-show-hidden-files-and-folders-in-file-open-dialog

#### 25. How to create a text file in a folder

**Issue**: How to create a text file in a folder
**Tags / Source**: Tags: macos, finder, file | apple | 👍 321 | 💬 32 answers

**Description**:
Tags: macos, finder, file | Score: 321 | Views: 609448 | Answers: 32

**Solution / Community Answer**:
You can also do this in Terminal. Go to the directory where you want to create the file, then run the following:

touch file.txt


Or redirect 'nothing' to a text file

&gt; file.txt

**Reference**: https://apple.stackexchange.com/questions/84309/how-to-create-a-text-file-in-a-folder

> 📎 Source: https://apple.stackexchange.com/questions/84309/how-to-create-a-text-file-in-a-folder

#### 26. Applications Don&#39;t Show Up in Spotlight

**Issue**: Applications Don&#39;t Show Up in Spotlight
**Tags / Source**: Tags: macos, spotlight | apple | 👍 319 | 💬 7 answers

**Description**:
Tags: macos, spotlight | Score: 319 | Views: 141991 | Answers: 7

**Solution / Community Answer**:
Update Oct 1, 2021
In 10.12 (macOS Sierra) and newer, it appears to be enough to disable and reenable indexing:
sudo mdutil -a -i off
sudo mdutil -a -i on

Original Answer
Loading the metadata plist worked for me:
Turn off spotlight:
sudo mdutil -a -i off

Unload it:
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist

Load It:
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist

Turn on spotlight again:
sudo mdutil -a -i on

Now everything is being reindexed as expected.

**Reference**: https://apple.stackexchange.com/questions/62715/applications-dont-show-up-in-spotlight

> 📎 Source: https://apple.stackexchange.com/questions/62715/applications-dont-show-up-in-spotlight

#### 27. What do I type to produce the command symbol (⌘) in Mac OS X?

**Issue**: What do I type to produce the command symbol (⌘) in Mac OS X?
**Tags / Source**: Tags: macos, internationalization, keyboard | apple | 👍 303 | 💬 17 answers

**Description**:
Tags: macos, internationalization, keyboard | Score: 303 | Views: 354805 | Answers: 17

**Solution / Community Answer**:
If you're just looking for the Unicode versions of Mac OS X keys, you can use this Apple support document to copy and paste them:

Mac keyboard shortcuts
https://support.apple.com/en-us/HT201236


⌘ Command (or Cmd)
⇧ Shift
⌥ Option (or Alt)
⌃ Control (or Ctrl)


More generally, Mac OS X provides a pane to insert special characters. You'll find it under Edit -&gt; Emoji and Symbols in any program that takes text input. The Command key symbol can be found by searching for it's name &quot;place of interest&quot;. To insert the character, double click it.


If you're really hardcore and are looking for a way to type the character by entering the Unicode hex code, this is possible:

Go into System Preferences -&gt; Keyboard -&gt; Input Sources, click &quot;+&quot;, scroll to &quot;others&quot;, select &quot;Unicode Hex Input&quot; and click &quot;Add&quot;


From the input source selector in the menu bar, select &quot;Unicode Hex Input&quot;


To enter a Unicode character, hold down option and type the 4-digit hex code for the character and it will be inserted. In this case, it would be option+2318.

**Reference**: https://apple.stackexchange.com/questions/4074/what-do-i-type-to-produce-the-command-symbol-in-mac-os-x

> 📎 Source: https://apple.stackexchange.com/questions/4074/what-do-i-type-to-produce-the-command-symbol-in-mac-os-x

#### 28. How to Retrieve the Wi-Fi Password of a Connected Network on a Mac

**Issue**: How to Retrieve the Wi-Fi Password of a Connected Network on a Mac
**Tags / Source**: Tags: macos, macbook-pro, mac | apple | 👍 282 | 💬 5 answers

**Description**:
Tags: macos, macbook-pro, mac | Score: 282 | Views: 1562491 | Answers: 5

**Solution / Community Answer**:
If the password is stored, you can find it using the program Keychain Access.

If you open /Applications/Utilities/Keychain Access, it will show you a list of stored entries. If you click the Kind column header, it will sort by kind, go to the section where AirPort network passwords are stored. On Yosemite, you may have to select "Local Items" rather than "login" under Keychains in the upper left.

Double-click the name of the network you are using (if you don't know the name of the network, you can find it in the WiFi menulet (the concentric quarter circles toward the right side of your menu bar).



Check the Show password box, enter your system password, and click the Allow button.

That should show you the password for the wireless network you are on, if it is stored on your computer. If no such entry appears, it means the password is not stored on your computer.

Note that you can also use this technique to find saved passwords for websites or other passwords that you computer has stored but you have forgotten.

**Reference**: https://apple.stackexchange.com/questions/56130/how-to-retrieve-the-wi-fi-password-of-a-connected-network-on-a-mac

> 📎 Source: https://apple.stackexchange.com/questions/56130/how-to-retrieve-the-wi-fi-password-of-a-connected-network-on-a-mac

#### 29. &quot;File Open&quot; dialog is missing sidebar items

**Issue**: &quot;File Open&quot; dialog is missing sidebar items
**Tags / Source**: Tags: finder, macos, sidebar | apple | 👍 280 | 💬 7 answers

**Description**:
Tags: finder, macos, sidebar | Score: 280 | Views: 132876 | Answers: 7

**Solution / Community Answer**:
Go to your user library in Finder. Hold down ⌥ while opening the Go menu and click Library. 
Navigate to the Preferences folder.
Remove any files that are or contain com.apple.finder.plist. (The removal of those files will very likely reset your Favourites list in Finder.)
Restart or log out and log back in again then empty the trash and try again. 

Restarting might not be necessary. As madpoet says:


  You can also relaunch Finder if you don't want to reboot or log out. Right click on Finder icon while you're pressing ⌥ and you'll see the Relaunch option there.
  
  





Alternatively, you can use this Bash oneliner by Christophe Marois:

cd ~/Library/Preferences &amp;&amp; sudo find com.apple.finder.plist* -exec rm {} \; &amp;&amp; killall Finder

**Reference**: https://apple.stackexchange.com/questions/208205/file-open-dialog-is-missing-sidebar-items

> 📎 Source: https://apple.stackexchange.com/questions/208205/file-open-dialog-is-missing-sidebar-items

#### 30. Where can I find the installed package path via brew

**Issue**: Where can I find the installed package path via brew
**Tags / Source**: Tags: macos, homebrew | apple | 👍 279 | 💬 15 answers

**Description**:
Tags: macos, homebrew | Score: 279 | Views: 651616 | Answers: 15

**Solution / Community Answer**:
Use the following to show the installation path of a package:

brew info hping


Example output:

pcre: stable 8.35 (bottled)
http://www.pcre.org/
/usr/local/Cellar/pcre/8.35 (146 files, 5.8M) *
  Poured from bottle
From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/pcre.rb
==&gt; Options
--universal
    Build a universal binary

**Reference**: https://apple.stackexchange.com/questions/145437/where-can-i-find-the-installed-package-path-via-brew

> 📎 Source: https://apple.stackexchange.com/questions/145437/where-can-i-find-the-installed-package-path-via-brew

#### 31. How to replace Mac OS X utilities with GNU core utilities?

**Issue**: How to replace Mac OS X utilities with GNU core utilities?
**Tags / Source**: Tags: macos, command-line, unix, utilities | apple | 👍 278 | 💬 7 answers

**Description**:
Tags: macos, command-line, unix, utilities | Score: 278 | Views: 215463 | Answers: 7

**Solution / Community Answer**:
This adds symlinks for GNU utilities with g prefix to /usr/local/bin/:

brew install coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent gnu-getopt grep


See brew search gnu for other packages. If you want to use the commands without a g prefix add for example /usr/local/opt/coreutils/libexec/gnubin before other directories on your PATH.

$ brew info coreutils
coreutils: stable 8.21
http://www.gnu.org/software/coreutils
Depends on: xz
/usr/local/Cellar/coreutils/8.20 (208 files, 9.4M)
/usr/local/Cellar/coreutils/8.21 (210 files, 9.6M) *
https://github.com/mxcl/homebrew/commits/master/Library/Formula/coreutils.rb
==&gt; Caveats
All commands have been installed with the prefix 'g'.

If you really need to use these commands with their normal names, you
can add a "gnubin" directory to your PATH from your bashrc like:

    PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

Additionally, you can access their man pages with normal names if you add
the "gnuman" directory to your MANPATH from your bashrc as well:

    MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"

**Reference**: https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

> 📎 Source: https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

#### 32. Why are dot underscore ._ files created, and how can I avoid them?

**Issue**: Why are dot underscore ._ files created, and how can I avoid them?
**Tags / Source**: Tags: macos, file | apple | 👍 275 | 💬 14 answers

**Description**:
Tags: macos, file | Score: 275 | Views: 394183 | Answers: 14

**Solution / Community Answer**:
You can't avoid them (but see the dot_clean answer by Saeid Zebardast --they can be removed from a directory if that is what you need).  They're created to store file information that would otherwise go into an extended attribute on HFS+ (Apple native) or Unix/UFS volumes; in earlier Mac OS this would be the resource fork.  Finder file operations will create them automatically to store the icon information, plus Time Machine stores some information in them so if you copy a file backed up via TM it will have that information copied as well.

(This is nothing new; I've noticed that XP and later leave various turds around as well, although not quite as many.)

**Reference**: https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them

> 📎 Source: https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them

#### 33. Can I open files in TextEdit from the Terminal in Mac OS X?

**Issue**: Can I open files in TextEdit from the Terminal in Mac OS X?
**Tags / Source**: Tags: macos, command-line, terminal, textedit | apple | 👍 273 | 💬 5 answers

**Description**:
Tags: macos, command-line, terminal, textedit | Score: 273 | Views: 538175 | Answers: 5

**Solution / Community Answer**:
open -a TextEdit filename should do the trick.
The -a flag specifies any application you want, so it's applicable to any number of situations, including ones where TextEdit isn't the default editor.
Other relevant options

-t  opens in the default editor (i.e. if you use BBEdit, TextMate, etc.)
-e will open the file specifically in TextEdit

**Reference**: https://apple.stackexchange.com/questions/25844/can-i-open-files-in-textedit-from-the-terminal-in-mac-os-x

> 📎 Source: https://apple.stackexchange.com/questions/25844/can-i-open-files-in-textedit-from-the-terminal-in-mac-os-x

#### 34. Can Touch ID on Mac authenticate sudo in Terminal?

**Issue**: Can Touch ID on Mac authenticate sudo in Terminal?
**Tags / Source**: Tags: macos, mac, password, sudo, touch-id | apple | 👍 272 | 💬 14 answers

**Description**:
Tags: macos, mac, password, sudo, touch-id | Score: 272 | Views: 118535 | Answers: 14

**Solution / Community Answer**:
To allow TouchID on your Mac to authenticate you for sudo access instead of a password you need to do the following.

Open Terminal

Switch to the root user with sudo su -

Edit the /etc/pam.d/sudo file with a command-line editor such as vim or nano

The contents of this file should look like one of the following examples:


# sudo: auth account password session
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so



# sudo: auth account password session
auth       sufficient     pam_smartcard.so
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so




You need to add an additional auth line to the top so it now looks like this:
# sudo: auth account password session
auth       sufficient     pam_tid.so
auth       sufficient     pam_smartcard.so
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so


Save the file. (Note: this file is normally read-only so saving your changes may require you to force the save, e.g. vim will require you to use wq! when saving)

Also note that pam_smartcard.so may not be present on older MacOS versions.

Exit from the root user or start a new terminal session.

Try to use sudo, and you should be prompted to authenticate with TouchID as shown below.


If you click 'Cancel,' you can just enter your password at the terminal prompt. If you click 'Use Password' you can enter your password in the dialog box.

If you SSH into your machine it will fall back to just use your password, since you can't send your TouchID fingerprints over SSH.


Note:
See answer by user Pierz below if you're using iTerm, as there's a setting you need to explicitly change to enable this feature.
Note:
Recent MacOS updates may remove the entry. If TouchID stops working for sudo then check if the entry was removed and add it back in, following these instructions again.

**Reference**: https://apple.stackexchange.com/questions/259093/can-touch-id-on-mac-authenticate-sudo-in-terminal

> 📎 Source: https://apple.stackexchange.com/questions/259093/can-touch-id-on-mac-authenticate-sudo-in-terminal

#### 35. How can I manually delete old backups to free space for Time Machine?

**Issue**: How can I manually delete old backups to free space for Time Machine?
**Tags / Source**: Tags: macos, time-machine, backup, time-capsule, maintenance | apple | 👍 266 | 💬 8 answers

**Description**:
Tags: macos, time-machine, backup, time-capsule, maintenance | Score: 266 | Views: 754833 | Answers: 8

**Solution / Community Answer**:
Be careful with sudo and making sure you pick the correct Mac's files since there is no undo or confirmation of the following command:
sudo tmutil delete /Volumes/drive_name/Backups.backupdb/old_mac_name

The sudo command needs your password (and it won't echo to the screen, so just type it and pause to be sure you're dating the correct files before pressing enter). If you want to be safer, you can pick one snapshot to delete first to be sure the command works as intended. This is nice since it could take hours to clean up some larger backup sets and you want to leave the Mac confident it's deleting the correct information store.
You can use the tmutil tool to delete backups one by one.
sudo tmutil delete /Volumes/drive_name/Backups.backupdb/mac_name/YYYY-MM-DD-hhmmss

Since tmutil was introduced with Lion, this will not work on earlier OS versions.
If you want to get the current directory of backups (there can be multiple destinations defined and only one will be &quot;current&quot;)
sudo tmutil machinedirectory

If you back up to a network share, you may have sparse bundle storage and if so, that needs to be compacted as well.
sudo hdiutil compact /Volumes/drive_name/Backups.backupdb/mac_name.sparsebundle

**Reference**: https://apple.stackexchange.com/questions/39287/how-can-i-manually-delete-old-backups-to-free-space-for-time-machine

> 📎 Source: https://apple.stackexchange.com/questions/39287/how-can-i-manually-delete-old-backups-to-free-space-for-time-machine

#### 36. What is the &quot;rootless&quot; feature in El Capitan, really?

**Issue**: What is the &quot;rootless&quot; feature in El Capitan, really?
**Tags / Source**: Tags: macos, unix, root, sip | apple | 👍 265 | 💬 3 answers

**Description**:
Tags: macos, unix, root, sip | Score: 265 | Views: 186445 | Answers: 3

**Solution / Community Answer**:
First: the name &quot;rootless&quot; is misleading, since there's still a root account, and you can still access it (the official name, &quot;System Integrity Protection&quot;, is more accurate). What it really does is limit the power of the root account, so that even if you become root, you don't have full control over the system. Essentially, the idea is that it's too easy for malware to get root access (e.g. by presenting an auth dialog to the user, which will cause the user to reflexively enter the admin password). SIP adds another layer of protection, which malware can't penetrate even if it gets root. The bad part of this, of course, it that it must also apply to things you're doing intentionally. But the restrictions it places on root aren't that bad; they don't prevent most &quot;normal&quot; system customization.
Here's what it restricts, even from root:

You can't modify anything in /System, /bin, /sbin, or /usr (except /usr/local); or any of the built-in apps and utilities. Only Installer and software update can modify these areas, and even they only do it when installing Apple-signed packages. But since normal OS X-style customizations go in /Library (or ~/Library, or /Applications), and unix-style customizations (e.g. Homebrew) go in /usr/local (or sometimes /etc or /opt), this shouldn't be a big deal. It also prevents block-level writes to the startup disk, so you can't bypass it that way.
The full list of restricted directories (and exceptions like /usr/local and a few others) is in /System/Library/Sandbox/rootless.conf. Of course, this file is itself in a restricted area.
When you upgrade to El Capitan, it moves any &quot;unauthorized&quot; files from restricted areas to /Library/SystemMigration/History/Migration-(some UUID)/QuarantineRoot/.

You can't attach to system processes (e.g. those running from those system locations) for things like debugging (or changing what dynamic libraries they load, or some other things). Again, not too much of a big deal; developers can still debug their own programs.
This does block some significant things like injecting code into the built-in Apple apps (notably the Finder). It also means that dtrace-based tools for system monitoring (e.g. opensnoop) will not be able to monitor &amp; report on many system processes.

You can't load kernel extensions (kexts) unless they're properly signed (i.e. by Apple or an Apple-approved developer). Note that this replaces the old system for enforcing kext signing (and the old ways of bypassing it). But since v10.10.4 Apple has had a way to enable trim support for third-party SSDs, the #1 reason to use unsigned kexts has gone away.

Starting in Sierra (10.12), some launchd configuration settings cannot be changed (for example, some launch daemons cannot be unloaded).

Starting in Mojave (10.14), access to users' personal information (email, contacts, etc) is restricted to apps that the user has approved to access that info. This is generally considered a separate feature (called Personal Information Protection, or TCC), but it's based on SIP and disabling SIP disables it as well. See: &quot;What and how does macOS Mojave implement to restrict applications access to personal data?&quot;

Starting in Catalina (10.15), protection of most system files is strengthened by storing them on a separate read-only volume. This is not strictly part of SIP, and is not disabled by disabling SIP. See: WWDC presentation on &quot;What's New in Apple [Catalina] File Systems&quot; and &quot;What's /System/Volumes/Data?&quot;.

Starting in Big Sur (11.x), the read-only system volume is now a &quot;Sealed System Volume&quot; (a mounted snapshot rather than a regular volume), so making changes to it is even more complicated. See: the Eclectic Light Company article &quot;Big Sur boot volume layout&quot;.


If you don't want these restrictions -- either because you want to modify your system beyond what this allows, or because you're developing &amp; debugging something like kexts that aren't practical under these restrictions, you can turn SIP off. Currently this requires rebooting into recovery mode and running the command csrutil disable (and you can similarly re-enable it with csrutil enable).
Modifying the system volume in Catalina requires disabling SIP, then mounting the volume with write access (and then rebooting and turning SIP back on is recommended). In Big Sur, additional steps are required to disable authentication of the system volume before changes, and afterward create a new snapshot.
You can also selectively disable parts of SIP. For example, csrutil enable --without kext will disable SIP's kernel extension restriction, but leave its other protections in place.
But please stop and think before disabling SIP, even temporarily or partially: do you really need to disable it, or is there a better (SIP-compliant) way to do what you want? Do you really need to modify something in /System/Library or /bin or whatever, or could it go in a better place like /Library or /usr/local/bin etc? SIP may &quot;feel&quot; constraining if you aren't used to it, and there are some legitimate reasons to disable it, but a lot of what it enforces it really just best practice anyway.
To underscore the importance of leaving as much of SIP enabled as much of the time as possible, consider the events of September 23, 2019. Google released an update to Chrome that tried to replace the symbolic link from /var to /private/var. On most systems, SIP blocked this and there were no bad effects. On systems with SIP disabled, it rendered macOS broken and unbootable. The most common reason for disabling SIP was to load unapproved (/improperly signed) kernel extensions (specifically video drivers); if they'd only disabled the kext restriction, they would not have been affected. See the official Google support thread, a superuser Q&amp;A on it, and an Ars Technica article.
References and further info: WWDC presentation on &quot;Security and Your Apps&quot;, a good explanation by Eldad Eilam on quora.com, the Ars Technica review of El Capitan, and an Apple support article on SIP, and a deep dive by Rich Trouton (who also posted an answer to this question).

**Reference**: https://apple.stackexchange.com/questions/193368/what-is-the-rootless-feature-in-el-capitan-really

> 📎 Source: https://apple.stackexchange.com/questions/193368/what-is-the-rootless-feature-in-el-capitan-really

#### 37. How can I make Safari show the URL when I hover over a link?

**Issue**: How can I make Safari show the URL when I hover over a link?
**Tags / Source**: Tags: macos, safari | apple | 👍 261 | 💬 3 answers

**Description**:
Tags: macos, safari | Score: 261 | Views: 126089 | Answers: 3

**Solution / Community Answer**:
There are two options. One is a setting, and the other is a workaround.

Here are instructions on how to toggle the setting using the Menu Bar:


Go into the View menu.
Select "Show status bar".
Now, there will be a URL that pops up when you hover over a link, and also tells you if it's going to be in a new tab:




You can also press ⌘ + / to toggle this setting at ease.

The second option is a workaround for when you drag links. Here's how to get this feature to appear:


Click and drag the link out of where it will originally appear.
At your mouse will be a small box telling you the title of the new window and its URL, although it may be shortened.
You can also drag the link to the plus sign in your tab list, out of the window, or in a folder/the desktop to open that URL in a new tab, new window or save it to your computer, respectively.

**Reference**: https://apple.stackexchange.com/questions/16759/how-can-i-make-safari-show-the-url-when-i-hover-over-a-link

> 📎 Source: https://apple.stackexchange.com/questions/16759/how-can-i-make-safari-show-the-url-when-i-hover-over-a-link

#### 38. Is there a keyboard shortcut to move a window from one monitor to another?

**Issue**: Is there a keyboard shortcut to move a window from one monitor to another?
**Tags / Source**: Tags: macos, keyboard, display, window-manager | apple | 👍 258 | 💬 18 answers

**Description**:
Tags: macos, keyboard, display, window-manager | Score: 258 | Views: 419833 | Answers: 18

**Solution / Community Answer**:
There is yet another option that's completely free and requires no third-party app. Be aware that I've only tested this on MacOS latest version Catalina (as of now). For other OS versions see Create keyboard shortcuts for apps on Mac

Go to System Preferences
Select Keyboard and then the Shortcuts tab
Then on the list that appears select App Shortcuts
Add new shortcuts like this:

Click on the plus sign to add a new one, the Menu Title field has to match exactly the text that appears on the Window menu in every application: &quot;Move to DISPLAY NAME&quot; (To find the text just open the Window menu on any application)
Finally on the Keyboard Shortcut field enter the shortcut you'd like to use
Add as many shortcuts as you need to move any window between your displays!

**Reference**: https://apple.stackexchange.com/questions/28569/is-there-a-keyboard-shortcut-to-move-a-window-from-one-monitor-to-another

> 📎 Source: https://apple.stackexchange.com/questions/28569/is-there-a-keyboard-shortcut-to-move-a-window-from-one-monitor-to-another

#### 39. Make the green full screen window icon on Yosemite maximize windows

**Issue**: Make the green full screen window icon on Yosemite maximize windows
**Tags / Source**: Tags: macos, fullscreen | apple | 👍 249 | 💬 7 answers

**Description**:
Tags: macos, fullscreen | Score: 249 | Views: 136963 | Answers: 7

**Solution / Community Answer**:
As the below mentioned solution is application-based (i.e. only works for apps like Google Chrome), another way to approach this problem is to ignore the maximize button entirely and to install the open source app spectacle which offers the keyboard shortcut:

⌘ + ⌥ + F

It also has some other nice features, too. And it works for all apps.



In order to maximize the window so that it fills the visible window content, use:

⌥ + Click on green icon

In order to maximize the window both in width and height to the current desktop for applications like Google Chrome use:

⌥ + ⇧ + Click on green icon

You notice the change of behaviour of the button in the way it changes its content from two the arrows to a plus sign.

**Reference**: https://apple.stackexchange.com/questions/139884/make-the-green-full-screen-window-icon-on-yosemite-maximize-windows

> 📎 Source: https://apple.stackexchange.com/questions/139884/make-the-green-full-screen-window-icon-on-yosemite-maximize-windows

#### 40. macOS Sierra doesn’t seem to remember SSH keys between reboots

**Issue**: macOS Sierra doesn’t seem to remember SSH keys between reboots
**Tags / Source**: Tags: terminal, password, ssh, macos | apple | 👍 230 | 💬 11 answers

**Description**:
Tags: terminal, password, ssh, macos | Score: 230 | Views: 175526 | Answers: 11

**Solution / Community Answer**:
As of macOS Sierra 10.12.2 Apple added an ssh_config option called UseKeychain which allows a 'proper' resolution to the problem. Add the following to your ~/.ssh/config file:
Host *
   AddKeysToAgent yes
   UseKeychain yes     

From the ssh_config man page on 10.12.2:

UseKeychain
On macOS, specifies whether the system should search for passphrases in the user's keychain when attempting to use a particular key. When the passphrase is provided by the user, this option also specifies whether the passphrase should be stored into the keychain once it has been verified to be correct.  The argument must be 'yes' or 'no'.  The default is 'no'.

**Reference**: https://apple.stackexchange.com/questions/254468/macos-sierra-doesn-t-seem-to-remember-ssh-keys-between-reboots

> 📎 Source: https://apple.stackexchange.com/questions/254468/macos-sierra-doesn-t-seem-to-remember-ssh-keys-between-reboots

#### 41. How can I rename Desktops / Spaces in macOS?

**Issue**: How can I rename Desktops / Spaces in macOS?
**Tags / Source**: Tags: macos, high-sierra, spaces | apple | 👍 229 | 💬 21 answers

**Description**:
Tags: macos, high-sierra, spaces | Score: 229 | Views: 262533 | Answers: 21

**Solution / Community Answer**:
Refer to the original page for detailed solutions and community answers.

**Reference**: https://apple.stackexchange.com/questions/211954/how-can-i-rename-desktops-spaces-in-macos

> 📎 Source: https://apple.stackexchange.com/questions/211954/how-can-i-rename-desktops-spaces-in-macos

#### 42. Keyboard shortcut for restoring applications from the Mac OS X Dock?

**Issue**: Keyboard shortcut for restoring applications from the Mac OS X Dock?
**Tags / Source**: Tags: macos, keyboard | apple | 👍 225 | 💬 11 answers

**Description**:
Tags: macos, keyboard | Score: 225 | Views: 117988 | Answers: 11

**Solution / Community Answer**:
Command + Tab until you get the app's icon.
Before releasing the Command key, press and hold the Option key.





You must switch to another app and let it take focus first. In other words, you can't just Command + Tab to another app and before actually selecting that app (by releasing the Command and Tab keys), switch right back to your minimized app, which you might attempt to do if you minimized it by accident or just simply changed your mind shortly after minimizing.
Both the Command and left Option keys must be pressed on the same side (left or right) of the keyboard.

**Reference**: https://apple.stackexchange.com/questions/55432/keyboard-shortcut-for-restoring-applications-from-the-mac-os-x-dock

> 📎 Source: https://apple.stackexchange.com/questions/55432/keyboard-shortcut-for-restoring-applications-from-the-mac-os-x-dock

#### 43. How do I run a .sh or .command file in Terminal

**Issue**: How do I run a .sh or .command file in Terminal
**Tags / Source**: Tags: macos, terminal, command-line, bash | apple | 👍 224 | 💬 6 answers

**Description**:
Tags: macos, terminal, command-line, bash | Score: 224 | Views: 1264164 | Answers: 6

**Solution / Community Answer**:
Open Terminal, type in sh /path/to/file and press enter. 

Faster is to type sh and a space and then drag the file to the window and release the icon anywhere on the window.

**Reference**: https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal

> 📎 Source: https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal

#### 44. How do I combine two or more images to get a single pdf file?

**Issue**: How do I combine two or more images to get a single pdf file?
**Tags / Source**: Tags: pdf, graphics, macos | apple | 👍 222 | 💬 8 answers

**Description**:
Tags: pdf, graphics, macos | Score: 222 | Views: 1502201 | Answers: 8

**Solution / Community Answer**:
Here are the steps to save multiple images in Preview into a single multi-page PDF.

Select all of the images you want in your PDF, right-click and choose open with Preview

In Preview's Sidebar drag the images into the order you want them to appear in your PDF

Select/highlight all the images to be included in the PDF document; otherwise only a single image may end up the PDF document

Then from the &quot;File&quot; menu choose &quot;Export Selected Images&quot; (or &quot;Export as PDF...&quot; in recent OS X versions) and then &quot;PDF &gt; Save as PDF&quot;

**Reference**: https://apple.stackexchange.com/questions/11163/how-do-i-combine-two-or-more-images-to-get-a-single-pdf-file

> 📎 Source: https://apple.stackexchange.com/questions/11163/how-do-i-combine-two-or-more-images-to-get-a-single-pdf-file

#### 45. Suppressing &quot;The default interactive shell is now zsh&quot; message in macOS Catalina

**Issue**: Suppressing &quot;The default interactive shell is now zsh&quot; message in macOS Catalina
**Tags / Source**: Tags: terminal, command-line, macos, bash | apple | 👍 216 | 💬 5 answers

**Description**:
Tags: terminal, command-line, macos, bash | Score: 216 | Views: 100044 | Answers: 5

**Solution / Community Answer**:
I found the solution on reddit. The solution is also mentioned in the &quot;How to use a different shell without changing the default&quot; section of the Apple support article mentioned in the bash warning: https://support.apple.com/en-us/HT208050/.
Add:
export BASH_SILENCE_DEPRECATION_WARNING=1

to $HOME/.bash_profile, $HOME/.profile or $HOME/.bashrc and restart iTerm. After that, the warning message will be gone.

**Reference**: https://apple.stackexchange.com/questions/371997/suppressing-the-default-interactive-shell-is-now-zsh-message-in-macos-catalina

> 📎 Source: https://apple.stackexchange.com/questions/371997/suppressing-the-default-interactive-shell-is-now-zsh-message-in-macos-catalina

#### 46. I included emoji in my password and now I can&#39;t log in to my Account on Yosemite

**Issue**: I included emoji in my password and now I can&#39;t log in to my Account on Yosemite
**Tags / Source**: Tags: macos, keyboard, password, filevault, emoji | apple | 👍 213 | 💬 8 answers

**Description**:
Tags: macos, keyboard, password, filevault, emoji | Score: 213 | Views: 96836 | Answers: 8

**Solution / Community Answer**:
If you have "Other Input Sources" available at the top right of your login screen, select the one called Unicode Hex Input.  This can be used to input emoji (or any other character) into the password field, as long as you know the Unicode Hex number of the character.  This number can be found in the Character Viewer or on the internet.

Some items you find in the  "emoji" category have Unicode hex numbers with just 4 characters, such as Airplane U+2708 ✈.  With the Unicode Hex Input keyboard, you input this by holding down the Option key while you type 2708.  

Other emoji have Unicode hex numbers with 5 characters, such as Grinning Face U+1F600 😀.  For these you need to find the two corresponding UTF-16 Hex codes (sometimes called "surrogates") by consulting Character Viewer or using an internet source like fileformat.info.  For 1F600 these are D83D and DE00.  You can input 1F600 by holding down the option key while typing D83DDE00.  You may see two dots in the field, but it is still just one character.

**Reference**: https://apple.stackexchange.com/questions/202143/i-included-emoji-in-my-password-and-now-i-cant-log-in-to-my-account-on-yosemite

> 📎 Source: https://apple.stackexchange.com/questions/202143/i-included-emoji-in-my-password-and-now-i-cant-log-in-to-my-account-on-yosemite

#### 47. List USB devices on OSX command line

**Issue**: List USB devices on OSX command line
**Tags / Source**: Tags: macos, usb | apple | 👍 212 | 💬 2 answers

**Description**:
Tags: macos, usb | Score: 212 | Views: 565191 | Answers: 2

**Solution / Community Answer**:
In addition to system_profiler SPUSBDataType (suggested by @kjs), you can also use ioreg -p IOUSB:

$ ioreg -p IOUSB 
+-o Root  &lt;class IORegistryEntry, id 0x100000100, retain 10&gt;
  +-o EHCI Root Hub Simulation@1A,7  &lt;class IOUSBRootHubDevice, id 0x100000227,$
  | +-o HubDevice@fa100000  &lt;class IOUSBHubDevice, id 0x10000027a, registered, $
  | | +-o Apple Internal Keyboard / Trackpad@fa120000  &lt;class IOUSBDevice, id 0$
  | | +-o BRCM2070 Hub@fa110000  &lt;class IOUSBHubDevice, id 0x1000002b4, registe$
  | |   +-o Bluetooth USB Host Controller@fa113000  &lt;class IOUSBDevice, id 0x10$
  | +-o FaceTime HD Camera (Built-in)@fa200000  &lt;class IOUSBDevice, id 0x100000$
  +-o EHCI Root Hub Simulation@1D,7  &lt;class IOUSBRootHubDevice, id 0x100000228,$
    +-o HubDevice@fd100000  &lt;class IOUSBHubDevice, id 0x10000027b, registered, $
      +-o IR Receiver@fd110000  &lt;class IOUSBDevice, id 0x100000288, registered,$


By default it clips to the window's width (80 chars in the example above), so you may want to add -w0 to get a full-width display. Also, adding -l will show details (probably more than you need) about each of the devices:

$ ioreg -p IOUSB -w0 -l
    +-o Root  &lt;class IORegistryEntry, id 0x100000100, retain 10&gt;
  | {
  |   "IOKitBuildVersion" = "Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64"
  |   "OS Build Version" = "14B25"
  |   "OSKernelCPUSubtype" = 3
  |   "OSKernelCPUType" = 16777223
  |   "OSPrelinkKextCount" = 185
  |   "IOConsoleLocked" = No
  |   "IORegistryPlanes" = {"IOACPIPlane"="IOACPIPlane","IOPower"="IOPower","IODeviceTree"="IODeviceTree","IOService"="IOService","IOUSB"="IOUSB","IOFireWire"="IOFireWire"}
[...etc...]


[EDIT]: If you just want the device names, you can filter the basic list to trim the junk:

$ ioreg -p IOUSB -w0 | sed 's/[^o]*o //; s/@.*$//' | grep -v '^Root.*'
EHCI Root Hub Simulation
HubDevice
Apple Internal Keyboard / Trackpad
BRCM2070 Hub
Bluetooth USB Host Controller
FaceTime HD Camera (Built-in)
EHCI Root Hub Simulation
HubDevice
IR Receiver

**Reference**: https://apple.stackexchange.com/questions/170105/list-usb-devices-on-osx-command-line

> 📎 Source: https://apple.stackexchange.com/questions/170105/list-usb-devices-on-osx-command-line

#### 48. Why is it not possible to use the &quot;cut&quot; command to manipulate a file in the Finder?

**Issue**: Why is it not possible to use the &quot;cut&quot; command to manipulate a file in the Finder?
**Tags / Source**: Tags: macos, finder, switching, contextual-menu | apple | 👍 212 | 💬 12 answers

**Description**:
Tags: macos, finder, switching, contextual-menu | Score: 212 | Views: 200052 | Answers: 12

**Solution / Community Answer**:
Keyboard method: Cmd-C then Opt-Cmd-V does the cut&amp;paste for files on Mac. 

Mouse method: Drag the file from one folder to the parent of the target folder (ie, if moving to Documents:Financial, drag to Documents). Hover on the parent folder for a few seconds, and it will spring open. Then you can continue dragging the file to the target folder. (note, the mouse method may result in very long hover times, if you're dragging a huge number of files, eg 1,000 files)

Menu method: It's not part of the Apple menu system to 'cut' files.  The menu Cut option is grayed out, and becomes enabled when text is selected.  But not files. Here is an in-depth discussion on Apple's discussion forum.

**Reference**: https://apple.stackexchange.com/questions/12391/why-is-it-not-possible-to-use-the-cut-command-to-manipulate-a-file-in-the-find

> 📎 Source: https://apple.stackexchange.com/questions/12391/why-is-it-not-possible-to-use-the-cut-command-to-manipulate-a-file-in-the-find

#### 49. Is it safe to delete ~/Library/Caches?

**Issue**: Is it safe to delete ~/Library/Caches?
**Tags / Source**: Tags: macos, hard-drive, file | apple | 👍 211 | 💬 6 answers

**Description**:
Tags: macos, hard-drive, file | Score: 211 | Views: 761138 | Answers: 6

**Solution / Community Answer**:
It's generally safe, though a little dangerous depending, to do it but often not worth the effort.
The caches in /System/Library/Caches are generally small and useful, the ones in /Library/Caches are less system caches and much more readily cleared.
If you have a look in ~/Library/Caches you will find a bunch of applications have a cache in there, none of them particularly large though dropbox sometimes has a fair sized cache. This folder can run quite large just because so many apps cache something in there.
If the cache /Library/Caches folder is over 3Gb then you have something that is caching quite a lot. On the three machines I just checked none had a /Library/Caches folder over .75 Gb so I'd go right ahead and remove some of it.
Don't worry about age, I'd worry about size.
In the terminal run the following to sort all of the files in that directory by size (ascending):
du -sh /Library/Caches/* | sort -h

Of course the best way to clear the caches is to install AppleJack and do it with that in single user mode. Doing it with the System fully up can be a little dangerous. If you do it then I'd reboot immediately afterwards.

**Reference**: https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches

> 📎 Source: https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches

#### 50. ZSH: .zprofile, .zshrc, .zlogin - What goes where?

**Issue**: ZSH: .zprofile, .zshrc, .zlogin - What goes where?
**Tags / Source**: Tags: macos, zsh, environment-variables | apple | 👍 209 | 💬 1 answers

**Description**:
Tags: macos, zsh, environment-variables | Score: 209 | Views: 274066 | Answers: 1

**Solution / Community Answer**:
This is an attempt to write a canonical QA for this issue, as per the Meta post:  Where is the list of canonical questions stored for Ask Different? I expect it to be periodically edited with the goal of becoming a comprehensive information resource.
What should be used in ZSH on a Mac
I posted a more narrowly scoped question on Unix &amp; Linux and got some clarification on how these files &quot;work.&quot;  Here's the summary of that answer and what I've learned in my research as to what, in my opinion should be used in a ZSH environment on a Mac.

.zprofile
.zlogin and .zprofile are basically the same thing - they set the environment for login shells1; they just get loaded at different times (see below).  .zprofile is based on the Bash's .bash_profile while .zlogin is a derivative of CSH's .login.  Since Bash was the default shell for everything up to Mojave, stick with .zprofile.

.zshrc
This sets the environment for interactive shells2.  This gets loaded after .zprofile.  It's typically a place where you &quot;set it and forget it&quot; type of parameters like $PATH, $PROMPT, aliases, and functions you would like to have in both login and interactive shells.

.zshenv (Optional)
This is read first and read every time.  This is where you set environment variables.  I say this is optional because is geared more toward advanced users where having your $PATH, $PAGER, or $EDITOR variables may be important for things like scripts that get called by launchd.  Those run under a non-interactive shell 3 so anything in .zprofile or .zshrc won't get loaded.  Personally, I don't use this one because I set the PATH variable in my script itself to ensure portability.

.zlogout (Optional)
But very useful!  This is read when you log out of a session and is very good for cleaning things up when you leave (like resetting the Terminal Window Title)


For an excellent, in-depth explanation of what these files do, see What should/shouldn't go in .zshenv, .zshrc, .zlogin, .zprofile, on Unix/Linux.

Some Caveats
Apple does things a little differently so it's best to be aware of this.  Specifically,  Terminal initially opens both a login and interactive shell even though you don't authenticate (enter login credentials).  However, any subsequent shells that are opened are only interactive.
You can test this out by putting an alias or setting a variable in .zprofile, then opening Terminal and seeing if that variable/alias exists.  Then open another shell (type zsh); that variable won't be accessible anymore.
SSH sessions are login and interactive so they'll behave just like your initial Terminal session and read both .zprofile and .zshrc
Order of Operations
This is the order in which these files get read.  Keep in mind that it reads first from the system-wide file (i.e. /etc/zshenv) then from the file in your home directory (~/.zshenv) as it goes through the following order.
.zshenv → .zprofile → .zshrc → .zlogin → .zlogout

1 A login shell is simply a shell, whether local or remote, that allows a user to authenticate to the system.  These shells are typically interactive shells.
2 In interactive mode, they [the shell] accept input typed from the keyboard.  (GNU Bash Reference Manual, 1.2 What is a Shell?)
3 When executing non-interactively, shells execute commands read from a file. (Ibid.)

**Reference**: https://apple.stackexchange.com/questions/388622/zsh-zprofile-zshrc-zlogin-what-goes-where

> 📎 Source: https://apple.stackexchange.com/questions/388622/zsh-zprofile-zshrc-zlogin-what-goes-where

#### 51. Open Finder window from current Terminal location?

**Issue**: Open Finder window from current Terminal location?
**Tags / Source**: Tags: macos, terminal, finder, path | apple | 👍 207 | 💬 7 answers

**Description**:
Tags: macos, terminal, finder, path | Score: 207 | Views: 83985 | Answers: 7

**Solution / Community Answer**:
Typing open . in Terminal will open the current working directory in a Finder window.

**Reference**: https://apple.stackexchange.com/questions/19375/open-finder-window-from-current-terminal-location

> 📎 Source: https://apple.stackexchange.com/questions/19375/open-finder-window-from-current-terminal-location

#### 52. Need a cli to check the sha256 hash of a file

**Issue**: Need a cli to check the sha256 hash of a file
**Tags / Source**: Tags: macos, command-line, encryption | apple | 👍 205 | 💬 4 answers

**Description**:
Tags: macos, command-line, encryption | Score: 205 | Views: 151884 | Answers: 4

**Solution / Community Answer**:
You can use

openssl dgst -sha256 &lt;file&gt;


Tested on LibreSSL 2.6.4 on macOS 10.14 (Mojave).



Prior to Mojave you can use openssl sha -sha256 &lt;file&gt; or openssl sha256 &lt;file&gt;.

To check command line options for the openssl sha command: openssl sha -help.

**Reference**: https://apple.stackexchange.com/questions/230917/need-a-cli-to-check-the-sha256-hash-of-a-file

> 📎 Source: https://apple.stackexchange.com/questions/230917/need-a-cli-to-check-the-sha256-hash-of-a-file

#### 53. How can I make auto-hide/show for the dock faster?

**Issue**: How can I make auto-hide/show for the dock faster?
**Tags / Source**: Tags: dock, macos | apple | 👍 204 | 💬 12 answers

**Description**:
Tags: dock, macos | Score: 204 | Views: 253798 | Answers: 12

**Solution / Community Answer**:
To make the Dock instantly leap back into view when it’s needed, rather than slide, open a Terminal window and type the following:
defaults write com.apple.dock autohide-time-modifier -int 0; killall Dock


I find this useful, but if you’d like the animation for the dock to reappear to last for a split-second, try the following:
defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock

To explain, changing &quot;0.15&quot; with any number can let you tailor things as it represents the time in seconds taken for the dock to reappear fully.

To revert back to the default sliding effect, open a Terminal window and type the following:
defaults delete com.apple.dock autohide-time-modifier; killall Dock

**Reference**: https://apple.stackexchange.com/questions/33600/how-can-i-make-auto-hide-show-for-the-dock-faster

> 📎 Source: https://apple.stackexchange.com/questions/33600/how-can-i-make-auto-hide-show-for-the-dock-faster

#### 54. How to move files to trash from command line?

**Issue**: How to move files to trash from command line?
**Tags / Source**: Tags: macos, command-line | apple | 👍 202 | 💬 17 answers

**Description**:
Tags: macos, command-line | Score: 202 | Views: 111071 | Answers: 17

**Solution / Community Answer**:
The trash command line tool can be installed via brew install trash or port install trash.
It allows you to restore trashed files via command line or the Finder.

**Reference**: https://apple.stackexchange.com/questions/50844/how-to-move-files-to-trash-from-command-line

> 📎 Source: https://apple.stackexchange.com/questions/50844/how-to-move-files-to-trash-from-command-line

#### 55. Restarting sound service?

**Issue**: Restarting sound service?
**Tags / Source**: Tags: macbook-pro, audio | apple | 👍 202 | 💬 8 answers

**Description**:
Tags: macbook-pro, audio | Score: 202 | Views: 272560 | Answers: 8

**Solution / Community Answer**:
sudo pkill coreaudiod
On older OSes:
You can kill the CoreAudio process by opening Terminal and running:
sudo kill -9 `ps ax|grep 'coreaudio[a-z]' | awk '{print $1}'`

It will restart automatically after a couple seconds.
That fixes some problems my aging MBP has been having, where it sometimes fails to detect headphones or decides the speakers aren't connected. No guarantees it will work for every audio problem, but it's worth a shot.
Source: zakgreant on macosxhints forums.

**Reference**: https://apple.stackexchange.com/questions/16842/restarting-sound-service

> 📎 Source: https://apple.stackexchange.com/questions/16842/restarting-sound-service

#### 56. How do I disable System Integrity Protection (SIP) AKA &quot;rootless&quot; on macOS?

**Issue**: How do I disable System Integrity Protection (SIP) AKA &quot;rootless&quot; on macOS?
**Tags / Source**: Tags: macos, sip | apple | 👍 197 | 💬 6 answers

**Description**:
Tags: macos, sip | Score: 197 | Views: 499215 | Answers: 6

**Solution / Community Answer**:
Note: disabling System Integrity Protection is dangerous, and makes your system more vulnerable to malware.
As Apple puts it in the developer documentation about SIP:

Warning
Disable SIP only temporarily to perform necessary tasks, and reenable it as soon as possible. Failure to reenable SIP when you are done testing leaves your computer vulnerable to malicious code.

If you are simply trying to configure system development tools such as vim, python2, ruby and so on, you almost certainly want to be just installing community-maintained versions from Homebrew and configuring those instead.  The system-provided tools may be convenient to bootstrap, but if you require SIP exceptions for your daily workflow you are almost certainly doing things in a way which will break in a future version of the operating system, and may break applications and other system functionality in the meanwhile.
Valid reasons to disable SIP yourself might be:

if you're doing research on malware yourself in a disposable environment, such as in a macOS virtual machine
if you are attempting to modify core operating system functionality for deployment in a highly-specialized environment such as a public-facing kiosk
if you require a legacy kernel extension such as MacFUSE on an M1 mac

Also important beyond the security implications is the fact that anything you do on a mac with SIP disabled will not work on anyone else's mac unless they also disable it first. If you're developing mac apps, then your system becomes less useful as a testbed because you don't know if your code only works because you hacked your system. If you're developing for another platform such as deployment to a web server, then you can't share your development environment setup with other developers on your team without compromising their security as well.
Here's how to do it if you really need to:
Apple's documentation covers disabling SIP, About System Integrity Protection on your Mac and Configuring System Integrity Protection.
An article on lifehacker.com lists these steps:


Reboot your Mac into Recovery Mode by restarting your computer and holding down Command+R until the Apple logo appears on your screen.
Click Utilities &gt; Terminal.
In the Terminal window, type in csrutil disable and press Enter.
Restart your Mac.


You can verify whether a file or folder is restricted by issuing this ls command using the capital O (and not zero 0) to modify the long listing flag:
ls -lO /System /usr 

Look for the restricted text to indicate where SIP is enforced.
By default (=SIP enabled), the following folders are restricted (see Apple Support page):
/System
/usr
/bin
/sbin
Apps that are pre-installed with OS X

... and the following folders are free:
/Applications
/Library
/usr/local

**Reference**: https://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-macos

> 📎 Source: https://apple.stackexchange.com/questions/208478/how-do-i-disable-system-integrity-protection-sip-aka-rootless-on-macos

#### 57. Cmd+Tab does not work on hidden or minimized windows

**Issue**: Cmd+Tab does not work on hidden or minimized windows
**Tags / Source**: Tags: macos, application-switcher | apple | 👍 192 | 💬 17 answers

**Description**:
Tags: macos, application-switcher | Score: 192 | Views: 144145 | Answers: 17

**Solution / Community Answer**:
This one is a bit tricky :

press ⌘ Cmd + ⇥ Tab to show your running apps. Keep holding ⌘ Cmd.

press ⇥ Tab until you've selected the app

press the ⌥ Option, and let go of the ⌘ Cmd. 
( You must release ⌘ Cmd after pressing ⌥ Option ! )
( You must release ⌘ Cmd before release ⌥ Option ! )

**Reference**: https://apple.stackexchange.com/questions/112350/cmdtab-does-not-work-on-hidden-or-minimized-windows

> 📎 Source: https://apple.stackexchange.com/questions/112350/cmdtab-does-not-work-on-hidden-or-minimized-windows

#### 58. Move through images in a folder with Preview.app

**Issue**: Move through images in a folder with Preview.app
**Tags / Source**: Tags: macos, preview | apple | 👍 192 | 💬 12 answers

**Description**:
Tags: macos, preview | Score: 192 | Views: 200585 | Answers: 12

**Solution / Community Answer**:
If you are just skimming the pictures do this:
Instead of opening a picture in Preview.app by double-clicking it, press space to preview the picture in Quick Look when selected in Finder.

Quick Look offers a fast, full-size preview of nearly any kind of file without opening the file. You can rotate photos, trim audio and video clips, and use Markup — directly in the Quick Look window.
https://support.apple.com/en-gb/guide/mac-help/mh14119/mac

This way you can still use the arrow keys to navigate between the pictures.

↑ and ↓ in list view
↑,↓,← and → in icon view

You can still open the picture in Preview.app when needed (top right corner).

**Reference**: https://apple.stackexchange.com/questions/37914/move-through-images-in-a-folder-with-preview-app

> 📎 Source: https://apple.stackexchange.com/questions/37914/move-through-images-in-a-folder-with-preview-app

#### 59. How to turn off all animations on OS X

**Issue**: How to turn off all animations on OS X
**Tags / Source**: Tags: macos | apple | 👍 192 | 💬 6 answers

**Description**:
Tags: macos | Score: 192 | Views: 194509 | Answers: 6

**Solution / Community Answer**:
I have only enabled the first four of these, but here are all hidden preferences for disabling animations I have found.

# opening and closing windows and popovers
defaults write -g NSAutomaticWindowAnimationsEnabled -bool false

# smooth scrolling
defaults write -g NSScrollAnimationEnabled -bool false

# showing and hiding sheets, resizing preference windows, zooming windows
# float 0 doesn't work
defaults write -g NSWindowResizeTime -float 0.001

# opening and closing Quick Look windows
defaults write -g QLPanelAnimationDuration -float 0

# rubberband scrolling (doesn't affect web views)
defaults write -g NSScrollViewRubberbanding -bool false

# resizing windows before and after showing the version browser
# also disabled by NSWindowResizeTime -float 0.001
defaults write -g NSDocumentRevisionsWindowTransformAnimation -bool false

# showing a toolbar or menu bar in full screen
defaults write -g NSToolbarFullScreenAnimationDuration -float 0

# scrolling column views
defaults write -g NSBrowserColumnAnimationSpeedMultiplier -float 0

# showing the Dock
defaults write com.apple.dock autohide-time-modifier -float 0
defaults write com.apple.dock autohide-delay -float 0

# showing and hiding Mission Control, command+numbers
defaults write com.apple.dock expose-animation-duration -float 0

# showing and hiding Launchpad
defaults write com.apple.dock springboard-show-duration -float 0
defaults write com.apple.dock springboard-hide-duration -float 0

# changing pages in Launchpad
defaults write com.apple.dock springboard-page-duration -float 0

# at least AnimateInfoPanes
defaults write com.apple.finder DisableAllAnimations -bool true

# sending messages and opening windows for replies
defaults write com.apple.Mail DisableSendAnimations -bool true
defaults write com.apple.Mail DisableReplyAnimations -bool true

**Reference**: https://apple.stackexchange.com/questions/14001/how-to-turn-off-all-animations-on-os-x

> 📎 Source: https://apple.stackexchange.com/questions/14001/how-to-turn-off-all-animations-on-os-x

#### 60. Homebrew: Your CLT does not support macOS 11.0

**Issue**: Homebrew: Your CLT does not support macOS 11.0
**Tags / Source**: Tags: command-line, homebrew, macos | apple | 👍 191 | 💬 5 answers

**Description**:
Tags: command-line, homebrew, macos | Score: 191 | Views: 121880 | Answers: 5

**Solution / Community Answer**:
Simplest solution that worked when upgrading to Big Sur. A clean install may not require the solution below. There is inconsistency with the way CLT is upgraded to 12.2.
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install

Worked with the following versions (post-install)
❯ /usr/bin/xcodebuild -version
Xcode 12.2
Build version 12B45b

❯ pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
package-id: com.apple.pkg.CLTools_Executables
version: 12.2.0.0.1.1603499215
volume: /
location: /
install-time: 1605632122
groups: com.apple.FindSystemFiles.pkg-group

Big Sur
11.0.1 (20B29)

**Reference**: https://apple.stackexchange.com/questions/401899/homebrew-your-clt-does-not-support-macos-11-0

> 📎 Source: https://apple.stackexchange.com/questions/401899/homebrew-your-clt-does-not-support-macos-11-0

#### 61. Is there a quick way to lock my Mac?

**Issue**: Is there a quick way to lock my Mac?
**Tags / Source**: Tags: macos, keyboard, security, screen-lock | apple | 👍 186 | 💬 26 answers

**Description**:
Tags: macos, keyboard, security, screen-lock | Score: 186 | Views: 63048 | Answers: 26

**Solution / Community Answer**:
On macOS High Sierra, there is a standard key sequence and Apple menu item to lock your screen. 


Control-Command-Q or ^+⌘+Q






For older OS, ⇧+⌃+⏏ puts the display (only the display, not the whole computer) to sleep and will then prompt you for a password if you have enabled Require password [amount of time] after sleep or screen saver begins under System Preferences &gt; Security.

If your Mac does not have an &#x23CF; (eject) key, you can use ⇧+⌃+⌽ (power).

**Reference**: https://apple.stackexchange.com/questions/64/is-there-a-quick-way-to-lock-my-mac

> 📎 Source: https://apple.stackexchange.com/questions/64/is-there-a-quick-way-to-lock-my-mac

#### 62. How to fix brew after OSX upgrade to Yosemite?

**Issue**: How to fix brew after OSX upgrade to Yosemite?
**Tags / Source**: Tags: macos, homebrew | apple | 👍 183 | 💬 5 answers

**Description**:
Tags: macos, homebrew | Score: 183 | Views: 105182 | Answers: 5

**Solution / Community Answer**:
I decided to look this up and found that there is an issue. The issue is closed but it is not possible to simply run brew update because you will still get the same error.

So here is what you need to do:

cd /usr/local/Library
git pull origin master


In case you have changes in the directory (/usr/local/Library), the git pull will throw an error. In that case, you'll have to fetch the master branch and set it forcibly as master:

git fetch --all
git reset --hard origin/master


This will upgrade your homebrew and you can use brew again.

If you installed Homebrew as a non-root user, you'll need to cd to /Users/yourusername/homebrew/Library instead of /usr/local/Library.

**Reference**: https://apple.stackexchange.com/questions/153790/how-to-fix-brew-after-osx-upgrade-to-yosemite

> 📎 Source: https://apple.stackexchange.com/questions/153790/how-to-fix-brew-after-osx-upgrade-to-yosemite

#### 63. Is there a `lsblk` equivalent for macOS that lists all attached storage devices?

**Issue**: Is there a `lsblk` equivalent for macOS that lists all attached storage devices?
**Tags / Source**: Tags: macos, command-line, hardware, storage | apple | 👍 183 | 💬 6 answers

**Description**:
Tags: macos, command-line, hardware, storage | Score: 183 | Views: 480009 | Answers: 6

**Solution / Community Answer**:
diskutil list will list all disks with their identifiers, even if unmounted.

/dev/disk0
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *251.0 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                  Apple_HFS Mac SSD                 150.0 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
   4:       Microsoft Basic Data Windows 8               100.1 GB   disk0s4
/dev/disk1
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *500.1 GB   disk1
   1:                  Apple_HFS George Garside          300.2 GB   disk1s1
   2:               Windows_NTFS GRGARSIDE               199.9 GB   disk1s2




For mounted disks only…

To find the raw device name (i.e. /dev/disk0s1) you can run df.

You can limit the results to locally-mounted filesystems, use df -Hl.
This results in a list of partitions and their raw device names, as shown below:

Filesystem     Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk0s2   150G   130G    20G    87% 31761475  4859615   87%   /
/dev/disk0s4   100G    83G    17G    83%   184667 17015601    1%   /Volumes/Windows 8
/dev/disk1s1   300G   282G    19G    94% 68771109  4529660   94%   /Volumes/George Garside
/dev/disk1s2   200G   172G    27G    87%   144125 26731127    1%   /Volumes/GRGARSIDE

**Reference**: https://apple.stackexchange.com/questions/107953/is-there-a-lsblk-equivalent-for-macos-that-lists-all-attached-storage-devices

> 📎 Source: https://apple.stackexchange.com/questions/107953/is-there-a-lsblk-equivalent-for-macos-that-lists-all-attached-storage-devices

#### 64. Which OS X Applications do you find indispensable?

**Issue**: Which OS X Applications do you find indispensable?
**Tags / Source**: Tags: macos, software-recommendation | apple | 👍 180 | 💬 239 answers

**Description**:
Tags: macos, software-recommendation | Score: 180 | Views: 49806 | Answers: 239

**Solution / Community Answer**:
Dropbox
Put your files into your Dropbox on one computer, and they'll be instantly available on any of your other computers that you've installed Dropbox on.

**Reference**: https://apple.stackexchange.com/questions/82/which-os-x-applications-do-you-find-indispensable

> 📎 Source: https://apple.stackexchange.com/questions/82/which-os-x-applications-do-you-find-indispensable

#### 65. What tiny thing in Lion makes you smile or has caught you off guard?

**Issue**: What tiny thing in Lion makes you smile or has caught you off guard?
**Tags / Source**: Tags: macos | apple | 👍 180 | 💬 107 answers

**Description**:
Tags: macos | Score: 180 | Views: 56548 | Answers: 107

**Solution / Community Answer**:
Using the FaceTime camera to add signatures to PDFs in Preview. 

Click the annotations button in the toolbar and use the drop down menu next to the signature icon to grab your signature from a piece of paper you have written it on. Then just click and drag in the document to place it. Haven't really needed it yet, but it's implemented so nicely that I did it just for fun.

**Reference**: https://apple.stackexchange.com/questions/17759/what-tiny-thing-in-lion-makes-you-smile-or-has-caught-you-off-guard

> 📎 Source: https://apple.stackexchange.com/questions/17759/what-tiny-thing-in-lion-makes-you-smile-or-has-caught-you-off-guard

#### 66. Add images to existing PDF with Preview

**Issue**: Add images to existing PDF with Preview
**Tags / Source**: Tags: macos, photos, pdf, preview | apple | 👍 180 | 💬 9 answers

**Description**:
Tags: macos, photos, pdf, preview | Score: 180 | Views: 327358 | Answers: 9

**Solution / Community Answer**:
Do as follows:

Open the image you want to paste in Preview.app
Select All (Command-A)
Copy (Command-C)
Paste (Command-V)

Now you have a copy of your image pasted above your old image. This is apparently meaningless, but the new copy is not just an image, but an object.

Click on the new image (round blue corners appear, no marching ants)
Copy (Command-C)
Paste on your PDF document. The image is an object, moveable and resizable. The original PDF is still a PDF, editable and all.

**Reference**: https://apple.stackexchange.com/questions/378888/add-images-to-existing-pdf-with-preview

> 📎 Source: https://apple.stackexchange.com/questions/378888/add-images-to-existing-pdf-with-preview

#### 67. How to arrange two windows easily to left and right side?

**Issue**: How to arrange two windows easily to left and right side?
**Tags / Source**: Tags: macos, mac, windows, window-manager | apple | 👍 180 | 💬 21 answers

**Description**:
Tags: macos, mac, windows, window-manager | Score: 180 | Views: 423807 | Answers: 21

**Solution / Community Answer**:
Original Answer (Update below):
Apple has provided this functionality as part of its OS X El Capitan. Here are the steps:

Click and hold on the green maximize button of an active window (for example, a Safari window);
When the window shrinks slightly and the background becomes highlighted, you’re about to enter Split View, while continuing to hold the green button drag the active window into either the left or right panel to place it full screen there;
As soon as you place the first window into the Split View panel, the other side of the screen turns into a mini-Expose much like Mission Control, simply click the window tile you want to open into Split View for the other side here to immediately send it side by side into Split Full Screen Mode.

The answer has been taken from osxdaily.com website's page.

Update:
Many people commented that they wish there was a shortcut for it. I figured a way to create a shortcut for that from another answer on AskDifferent which I cannot find the link to. This is how:

Open System Preferences;
Go to 'Keyboard' settings;
Go to 'Shortcuts' tab;
In the left pane, select 'App Shortcuts';

In this section you can add app specific shortcuts, as well as shortcuts that you want available for all apps.


Click on the '+' sign below right pane to add a new shortcut;
A new drop down will open. In this drop-down:

In the 'Application:' keep it for 'All Applications';
In the 'Menu Title:' type 'Tile Window to Right of Screen'. Better that you copy-paste it because it has to match letter by letter;
In the 'Keyboard Shortcut:' press the keys you want to use as shortcut for tiling an application window to the right. On my machine, I've set† it to ⎇⌘→.
Repeat the same for tiling to left by putting 'Tile Window to Left of Screen' in the 'Menu Title:' and adding your desired keys for left-tiling shortcut.



You should now have the shortcuts available for any application window that supports tiling. Now, you can press your shortcut keys to tile the first window to left or right. Then the other side will turn into a mini-Expose from which you can select the second window using your mouse.


†I have a dual monitor setup. So other than the one listed above, I have also set the shortcut to move a window to another monitor. The 'Menu Title's are: 
1. &quot;Move to Built-in Retina Display&quot;, with shortcut ⌃⎇⌘→;
2. &quot;Move to LG UltraFine&quot;, with shortcut ⌃⎇⌘←;
To remember the shortcuts, notice that all they keys, are next to each other. All you do is use arrow keys differently. Further, moving to another monitor has an extra key in the shortcut, while putting the windows in split view is on the same monitor, therefore it has one less key.
Hint:
The shortcut name depends on the MacOS system language, e.g.:
english:
'Tile Window to Left of Screen'
german : 'Fenster auf der linken Bildschirmseite anordnen'
or a different title: 'Fenster auf die linke Seite des Bildschirms bewegen'
Phrases for left / right can be found on the green &quot;full screen&quot; button:

**Reference**: https://apple.stackexchange.com/questions/50330/how-to-arrange-two-windows-easily-to-left-and-right-side

> 📎 Source: https://apple.stackexchange.com/questions/50330/how-to-arrange-two-windows-easily-to-left-and-right-side

#### 68. What is the `installd` process, and why is it eating my CPU?

**Issue**: What is the `installd` process, and why is it eating my CPU?
**Tags / Source**: Tags: activity-monitor, macos | apple | 👍 179 | 💬 7 answers

**Description**:
Tags: activity-monitor, macos | Score: 179 | Views: 243455 | Answers: 7

**Solution / Community Answer**:
This is a daemon which is part of PackageKit framework and it's usually running as a background process for the "Software Update" GUI application.
For example, if you open the Software Update application and check for updates, take a look at the Activity Monitor--you'll see the "installd" process doing a bunch of work.

The reason it pegs your CPU is because it must compile the current list of software installed on your computer, and compare with the current version list received from Apple's servers.

You can set the frequency of Software Update checks in System Preferences and Software Update.

The default settings are both to "Check for updates" and "Download updates automatically".
You may adjust either setting, but I would not recommend turning it off altogether.

There's nothing wicked about this process - it's just set to download updates.

You can solve your CPU problem by lowering the priority of the process or by just killing the process in Activity Monitor.



Technical information:

The location in Lion OSX is in:
/System/Library/PrivateFrameworks/PackageKit.framework/Resources/installd

(if you have locate configured correctly, run: locate installd to find the right location).

**Reference**: https://apple.stackexchange.com/questions/87109/what-is-the-installd-process-and-why-is-it-eating-my-cpu

> 📎 Source: https://apple.stackexchange.com/questions/87109/what-is-the-installd-process-and-why-is-it-eating-my-cpu

#### 69. What is this qemu-system-aarch64 process and why is it using almost 3 GB of RAM on my M1 Mac

**Issue**: What is this qemu-system-aarch64 process and why is it using almost 3 GB of RAM on my M1 Mac
**Tags / Source**: Tags: mac-mini, macos, activity-monitor, apple-silicon | apple | 👍 178 | 💬 3 answers

**Description**:
Tags: mac-mini, macos, activity-monitor, apple-silicon | Score: 178 | Views: 155253 | Answers: 3

**Solution / Community Answer**:
This process belongs to an application you've installed yourself.
To find out more, select the process in Activity Monitor and press Cmd-I to open the Process Information window. You should see the name of the process which started it at the top, and the path to the binary itself near the top of the 3rd tab (open files and ports).

**Reference**: https://apple.stackexchange.com/questions/420445/what-is-this-qemu-system-aarch64-process-and-why-is-it-using-almost-3-gb-of-ram

> 📎 Source: https://apple.stackexchange.com/questions/420445/what-is-this-qemu-system-aarch64-process-and-why-is-it-using-almost-3-gb-of-ram

#### 70. How can I mount an ext4 file system on OS X?

**Issue**: How can I mount an ext4 file system on OS X?
**Tags / Source**: Tags: macos, unix | apple | 👍 178 | 💬 11 answers

**Description**:
Tags: macos, unix | Score: 178 | Views: 372061 | Answers: 11

**Solution / Community Answer**:
The answer depends on you willingness to invest in commercial software:
If you don’t mind spending some money on a commercial product, Paragon’s extFS for Mac will give you read and write access to ext2 / ext3 / ext4 file systems. The current version supports all versions of OS X / macOS from 10.10 upwards.
If you are looking for a free solution, you can setup a Linux virtual machine, mount your volume(s) there and share it / them via Samba or (S)FTP. This post has some details on how to achieve this using VirtualBox, a free virtual machine application. Note this is not exactly a lightweight solution, even if using a prebuilt VirtualBox VM will spare you installing and configuring a Linux distro from scratch.

**Reference**: https://apple.stackexchange.com/questions/29842/how-can-i-mount-an-ext4-file-system-on-os-x

> 📎 Source: https://apple.stackexchange.com/questions/29842/how-can-i-mount-an-ext4-file-system-on-os-x

#### 71. Convert .mov to .mp4

**Issue**: Convert .mov to .mp4
**Tags / Source**: Tags: macos, video, imovie, mp4, mov | apple | 👍 177 | 💬 6 answers

**Description**:
Tags: macos, video, imovie, mp4, mov | Score: 177 | Views: 134269 | Answers: 6

**Solution / Community Answer**:
I personally find using ffmpeg shell program (available through Brew using brew install ffmpeg) the most convenient way to do the conversions.

It includes tons of options for nearly any single thing you could possibly do with a movie.

In your case though, for a conversion, you can simply type:

ffmpeg -i /path/to/input/file /path/to/output.mp4

The .mp4 extension in the output path serves as a cue for the program to do the proper conversion -- no more options are necessary.

**Reference**: https://apple.stackexchange.com/questions/232910/convert-mov-to-mp4

> 📎 Source: https://apple.stackexchange.com/questions/232910/convert-mov-to-mp4

#### 72. How can I prevent an SSH session from hanging in OS X Terminal?

**Issue**: How can I prevent an SSH session from hanging in OS X Terminal?
**Tags / Source**: Tags: macos, terminal, wifi, ssh | apple | 👍 175 | 💬 7 answers

**Description**:
Tags: macos, terminal, wifi, ssh | Score: 175 | Views: 189533 | Answers: 7

**Solution / Community Answer**:
For keeping the connection alive, you can check in /etc/ssh/ssh_config the line where it says ServerAliveInterval, that tells you how often (in seconds) your computer is gonna send a null packet to keep the connection alive. If you have a 0 in there that indicates that your computer is not trying to keep the connection alive (it is disabled), otherwise it tells you how often (in seconds) it is sending the aforementioned packet. Try putting in 120 or 240, if it is still killing your connection, you can go lower, maybe to 5, if with that number it doesn't happen, maybe it is your router who is dumping the connection to free memory.

For killing it when it gets hang up, you can use the ssh escape character:

~.


That is, press the tilde and then the period, if it doesn't work, press Enter before you press that, that will kill the connection immediately.

**Reference**: https://apple.stackexchange.com/questions/36690/how-can-i-prevent-an-ssh-session-from-hanging-in-os-x-terminal

> 📎 Source: https://apple.stackexchange.com/questions/36690/how-can-i-prevent-an-ssh-session-from-hanging-in-os-x-terminal

#### 73. OS X computer name not matching what shows on terminal

**Issue**: OS X computer name not matching what shows on terminal
**Tags / Source**: Tags: macos, xcode | apple | 👍 174 | 💬 12 answers

**Description**:
Tags: macos, xcode | Score: 174 | Views: 187601 | Answers: 12

**Solution / Community Answer**:
It's perfectly normal for this to occur; when you login Terminal remotely bash does a reverse DNS lookup. It will only be the same if the hostname is not specified on the network you're connecting from and there is no reply from the DHCP server, or the reverse lookup against the remote DNS server fails to resolve.
You can easily over-ride the default setting by using this command in Terminal:
sudo scutil --set HostName archos

You can check it by using:
nslookup nn.nn.nn.nn

( or )
host nn.nn.nn.nn

(where nn signifies your Mac's ip address)

**Reference**: https://apple.stackexchange.com/questions/30552/os-x-computer-name-not-matching-what-shows-on-terminal

> 📎 Source: https://apple.stackexchange.com/questions/30552/os-x-computer-name-not-matching-what-shows-on-terminal

#### 74. What happens if you plug more than one charger in the new MacBook Pro (2016)?

**Issue**: What happens if you plug more than one charger in the new MacBook Pro (2016)?
**Tags / Source**: Tags: macbook-pro, usb, charger, charging | apple | 👍 173 | 💬 3 answers

**Description**:
Tags: macbook-pro, usb, charger, charging | Score: 173 | Views: 163463 | Answers: 3

**Solution / Community Answer**:
The system will choose the power source that provides the most power, and it will not draw power from the others.
Apple has released a support article (and another one) describing this:


Your MacBook Pro draws power from only one power supply, even if more
than one is attached—so using multiple power supplies will not speed
up charging.

If you connect multiple power supplies to your MacBook
Pro, the one that provides the most power will be used, regardless of
the order in which you connected them.

You should not connect any
power supply that exceeds 100W, as it might damage your Mac.

**Reference**: https://apple.stackexchange.com/questions/259744/what-happens-if-you-plug-more-than-one-charger-in-the-new-macbook-pro-2016

> 📎 Source: https://apple.stackexchange.com/questions/259744/what-happens-if-you-plug-more-than-one-charger-in-the-new-macbook-pro-2016

#### 75. How to simulate slow internet connections on the mac

**Issue**: How to simulate slow internet connections on the mac
**Tags / Source**: Tags: macos, mac, network, performance, internet | apple | 👍 172 | 💬 10 answers

**Description**:
Tags: macos, mac, network, performance, internet | Score: 172 | Views: 179944 | Answers: 10

**Solution / Community Answer**:
Apple’s official tool to slow down the network connections on you Mac for testing purposes is Network Link Conditioner

Additional Tools for Xcode [version].

Additionally, iOS has similar function accessible from within Xcode and iOS 6 or later.

Older versions of Xcode before version 4.3.2 embedded a copy of this tool. This SO thread documents some history of the tool in a similar manner to the iOS simulators and developer documentation.
There are 11 built in profiles from a Lossy Edge network with 400ms delay to a cable modem. If you need other limits, you can create custom profiles with your own settings or you can also use ipfw yourself as described in Craig Hockenberry's article slow ride, make it easy It also mentions the Speed Limit panel by Mike Schrag that is a smaller download than Xcode, but has fewer options than Apple's tool.
It slows down the entire network stack, so you can't throttle on a per app basis without doing things like install lion in a virtual machine and set that VM with a throttled stack.

**Reference**: https://apple.stackexchange.com/questions/24066/how-to-simulate-slow-internet-connections-on-the-mac

> 📎 Source: https://apple.stackexchange.com/questions/24066/how-to-simulate-slow-internet-connections-on-the-mac

#### 76. Using The Terminal Command to Shutdown, Restart and Sleep My Mac?

**Issue**: Using The Terminal Command to Shutdown, Restart and Sleep My Mac?
**Tags / Source**: Tags: macos, terminal, sleep-wake, shutdown, restart | apple | 👍 172 | 💬 4 answers

**Description**:
Tags: macos, terminal, sleep-wake, shutdown, restart | Score: 172 | Views: 551481 | Answers: 4

**Solution / Community Answer**:
The command you are after is shutdown.
This  informs all users that the machine is going to be shutdown and tells all apps to close files etc.
The command takes a parameter -h, -r or -s to shut down, restart or sleep the Mac.
The command has to be run as root so you need to use sudo.
e.g. to reboot the machine immediately
sudo shutdown -r now

e.g. to shutdown the machine in 60 minutes
sudo shutdown -h +60

From comments there are two things to be addressed
How shutdown works is by sending a sigterm to all processes which should then deal with that e.g. save open files etc. If they don't exit then they will get sent a SIGKILL which forces them to die with no chance to respond. The signals are not sent via the normal key message queue so Apps have to deal with this separately to the code that gets called from quit on the menu. A good app should call common code from both.
This other answer shows how to shutdown as if you hit the menu options. But note that apps can cancel this shutdown

**Reference**: https://apple.stackexchange.com/questions/103571/using-the-terminal-command-to-shutdown-restart-and-sleep-my-mac

> 📎 Source: https://apple.stackexchange.com/questions/103571/using-the-terminal-command-to-shutdown-restart-and-sleep-my-mac

#### 77. How to get the chrome tabs to always show when in full screen mode?

**Issue**: How to get the chrome tabs to always show when in full screen mode?
**Tags / Source**: Tags: macos, google-chrome, fullscreen, tabs | apple | 👍 170 | 💬 9 answers

**Description**:
Tags: macos, google-chrome, fullscreen, tabs | Score: 170 | Views: 357321 | Answers: 9

**Solution / Community Answer**:
With latest version of Chrome, there is the option to show the Toolbar (which includes tabs) in the View menu.

**Reference**: https://apple.stackexchange.com/questions/94737/how-to-get-the-chrome-tabs-to-always-show-when-in-full-screen-mode

> 📎 Source: https://apple.stackexchange.com/questions/94737/how-to-get-the-chrome-tabs-to-always-show-when-in-full-screen-mode

#### 78. Task Switcher moves to non-primary display on Mavericks-Catalina

**Issue**: Task Switcher moves to non-primary display on Mavericks-Catalina
**Tags / Source**: Tags: macos, display, application-switcher | apple | 👍 170 | 💬 5 answers

**Description**:
Tags: macos, display, application-switcher | Score: 170 | Views: 46640 | Answers: 5

**Solution / Community Answer**:
I answered a similar question here - cmd-tab behavior on Mavericks with multiple displays

The Task Switcher does follow the Dock.  If the Dock is on screen 1, the Task Switcher will appear on screen 1.  If the Dock is on screen 3, the Task Switcher will appear on screen 3.  Etc.

To make your Dock appear on a screen you can use a couple of methods.

Method 1 - Move your mouse to the bottom of the desired display.  Don't stop once you reach the bottom of the display though, try to move it further down, as if you're pushing down on the bottom of the display with your cursor.  This action tells the Dock to move to this display.  This is temporary however, meaning the Dock will stay on this display until you perform this action on another display or reboot your Mac.

Method 2 - This will change the default starting point for your Dock.  In System Preferences > Displays > Arrangement you can drag the menu bar from one display to another in this windows display icons.  See the attached picture for reference.  This alters the default preference to always show the Dock on the desired display, the one you drag the menu bar to in this preference pane, when you boot and/or login to your user account.  You can still use method 1 to temporarily change the Dock's location but upon a reboot it will return to the display specified here.

**Reference**: https://apple.stackexchange.com/questions/107419/task-switcher-moves-to-non-primary-display-on-mavericks-catalina

> 📎 Source: https://apple.stackexchange.com/questions/107419/task-switcher-moves-to-non-primary-display-on-mavericks-catalina

#### 79. WindowServer high CPU on Yosemite

**Issue**: WindowServer high CPU on Yosemite
**Tags / Source**: Tags: macos, performance | apple | 👍 170 | 💬 11 answers

**Description**:
Tags: macos, performance | Score: 170 | Views: 188761 | Answers: 11

**Solution / Community Answer**:
I had a similar issue with high cpu usage in WindowServer which I managed to get back to something more normal by removing any items in my menu bar that were making high frequency drawing updates. 

In my case it was the Network Monitor from Little Snitch that seemed to be the biggest culprit.

**Reference**: https://apple.stackexchange.com/questions/153397/windowserver-high-cpu-on-yosemite

> 📎 Source: https://apple.stackexchange.com/questions/153397/windowserver-high-cpu-on-yosemite

#### 80. Keyboard shortcut to switch focus between multiple displays on OS X 10.9+

**Issue**: Keyboard shortcut to switch focus between multiple displays on OS X 10.9+
**Tags / Source**: Tags: keyboard, display, macos | apple | 👍 170 | 💬 7 answers

**Description**:
Tags: keyboard, display, macos | Score: 170 | Views: 373483 | Answers: 7

**Solution / Community Answer**:
Refer to the original page for detailed solutions and community answers.

**Reference**: https://apple.stackexchange.com/questions/106559/keyboard-shortcut-to-switch-focus-between-multiple-displays-on-os-x-10-9

> 📎 Source: https://apple.stackexchange.com/questions/106559/keyboard-shortcut-to-switch-focus-between-multiple-displays-on-os-x-10-9

#### 81. How can I install .pkg with a shell on macOS?

**Issue**: How can I install .pkg with a shell on macOS?
**Tags / Source**: Tags: macos, command-line, install, pkg | apple | 👍 166 | 💬 3 answers

**Description**:
Tags: macos, command-line, install, pkg | Score: 166 | Views: 483177 | Answers: 3

**Solution / Community Answer**:
/usr/sbin/installer

The installer command is used to install Mac OS X installer packages to a specified domain or volume.  The
installer command installs a single package per invocation, which is specified with the -package parameter ( -pkg
is accepted as a synonym).  It may be either a single package or a metapackage.  In the case of the metapackage,
the packages which are part of the default install will be installed unless disqualified by a package's check
tool(s).

See man installer for the full functionality. Often
sudo installer -pkg /path/to/package.pkg -target /

is all that's needed. The target is a &quot;device&quot; (see the man page for details or run installer -dominfo). Here / is the main drive, it also accepts devices like &quot;/Volumes/Macintosh HD&quot;, or /dev/disk0.

**Reference**: https://apple.stackexchange.com/questions/72226/how-can-i-install-pkg-with-a-shell-on-macos

> 📎 Source: https://apple.stackexchange.com/questions/72226/how-can-i-install-pkg-with-a-shell-on-macos

#### 82. What directory comparison tools can I use on OS X?

**Issue**: What directory comparison tools can I use on OS X?
**Tags / Source**: Tags: macos, command-line | apple | 👍 164 | 💬 17 answers

**Description**:
Tags: macos, command-line | Score: 164 | Views: 196307 | Answers: 17

**Solution / Community Answer**:
FileMerge (free), shipped with Xcode, offers a directory view.
A command line version is available through the Terminal application opendiff.

Here's how you can compare two directories with FileMerge:


⌘+space, type in "FileMerge" and open it.
Click the "left" button and choose the folder you would like to move items FROM. (The "old" folder)
Click the "right" button and choose the folder you would like to move items TO. ("new" folder) and click "Compare" button
In the right panel, choose to exclude: "identical" and "Changed right". This way you will only see files which are missing in the "new" folder and ignore files your may have added in the "new" folder.
Move files manually in Finder or let FileMerge do it, by choosing an option in the "Merge" dropdown in the right panel.

**Reference**: https://apple.stackexchange.com/questions/10252/what-directory-comparison-tools-can-i-use-on-os-x

> 📎 Source: https://apple.stackexchange.com/questions/10252/what-directory-comparison-tools-can-i-use-on-os-x

#### 83. Any nice, stable ways to keep a window &#39;Always on top&#39; on the Mac?

**Issue**: Any nice, stable ways to keep a window &#39;Always on top&#39; on the Mac?
**Tags / Source**: Tags: macos, window-manager | apple | 👍 163 | 💬 13 answers

**Description**:
Tags: macos, window-manager | Score: 163 | Views: 276780 | Answers: 13

**Solution / Community Answer**:
Refer to the original page for detailed solutions and community answers.

**Reference**: https://apple.stackexchange.com/questions/219116/any-nice-stable-ways-to-keep-a-window-always-on-top-on-the-mac

> 📎 Source: https://apple.stackexchange.com/questions/219116/any-nice-stable-ways-to-keep-a-window-always-on-top-on-the-mac

#### 84. Change location of macOS Notification Center alerts?

**Issue**: Change location of macOS Notification Center alerts?
**Tags / Source**: Tags: macos, notifications | apple | 👍 159 | 💬 10 answers

**Description**:
Tags: macos, notifications | Score: 159 | Views: 89318 | Answers: 10

**Solution / Community Answer**:
Unfortunately, you can't change the screen position of the Notification Center Alerts and Banners. This is a huge gripe of mine as well, and I highly encourage you to complain about this issue to Apple here:
http://www.apple.com/feedback/macos.html

Hopefully they will one day change this. I also have not been able to find or formulate any hacks.

I, too, am annoyed by it covering up controls in my modeling applications, tabs in my browser, etc.

You can move the Notification Center to another screen, however your entire menu bar goes with it. When you have more than one monitor active, open up System Preferences > Displays > Arrangement. Click and drag the white bar inside one of the squares representing your current primary monitor and drag it to another monitor.

For notifications that don't need immediate attention, consider changing the alert style from Alerts to Banners. Banners are automatically dismissed into the notification center where you can find them later.

Good luck, and keep spreading the word that we need to tell Apple to make this experience better.

**Reference**: https://apple.stackexchange.com/questions/71989/change-location-of-macos-notification-center-alerts

> 📎 Source: https://apple.stackexchange.com/questions/71989/change-location-of-macos-notification-center-alerts

#### 85. How to stop OS X from writing Spotlight and Trash files to memory cards and USB sticks?

**Issue**: How to stop OS X from writing Spotlight and Trash files to memory cards and USB sticks?
**Tags / Source**: Tags: macos, photos, usb, spotlight, trash | apple | 👍 158 | 💬 23 answers

**Description**:
Tags: macos, photos, usb, spotlight, trash | Score: 158 | Views: 192282 | Answers: 23

**Solution / Community Answer**:
For just a particular mounted volume - like a flash drive called yourUSBstick in this example - these commands will remove existing cruft, stop Spotlight indexing now and in the future, stop the related fsevents logging, and disable the Trash feature.

mdutil -i off /Volumes/yourUSBstick
cd /Volumes/yourUSBstick
rm -rf .{,_.}{fseventsd,Spotlight-V*,Trashes}
mkdir .fseventsd
touch .fseventsd/no_log .metadata_never_index .Trashes
cd -


Other unfamiliar stuff you may still see you probably want to keep, like Apple double "._*" files and other Apple DS cruft relating to icons and window placement.

**Reference**: https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb

> 📎 Source: https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb

#### 86. How to switch or close the new split Terminal pane?

**Issue**: How to switch or close the new split Terminal pane?
**Tags / Source**: Tags: macos, terminal | apple | 👍 158 | 💬 3 answers

**Description**:
Tags: macos, terminal | Score: 158 | Views: 154734 | Answers: 3

**Solution / Community Answer**:
The idea behind splitting is that it allows you to keep a certain part of the shell buffer displayed while continuing to enter new commands. So only the lowest split does allow keyboard input. To position the view on the shell buffer use the scroll bar.

You can un-split by pressing Shift-Cmd-D.

**Reference**: https://apple.stackexchange.com/questions/87202/how-to-switch-or-close-the-new-split-terminal-pane

> 📎 Source: https://apple.stackexchange.com/questions/87202/how-to-switch-or-close-the-new-split-terminal-pane

#### 87. Can home and end keys be mapped when using Terminal?

**Issue**: Can home and end keys be mapped when using Terminal?
**Tags / Source**: Tags: macos, terminal, keyboard, command-line, keybindings | apple | 👍 157 | 💬 11 answers

**Description**:
Tags: macos, terminal, keyboard, command-line, keybindings | Score: 157 | Views: 93737 | Answers: 11

**Solution / Community Answer**:
This can be set in Terminal.app preferences
Context
To answer the one about how to get the beginning or end of the line, it appears that by default Terminal maps these keys to it:

shift+home → beginning of line, equivalent to the &quot;home&quot; key in normal terminals
shift+end → end of line, equivalent to the &quot;end&quot; key in normal terminals

Instructions
If you want home and end to work the &quot;normal&quot; way (and not require shift), go to the Keyboard tab of the Terminal profile preferences:
[Terminal menu] → Preferences → Profiles tab (or settings on some versions of OS X) → Keyboard sub-tab
Then modify/add these keys to be the following &quot;send string to shell&quot;. Use the code for your shell, Bash or Zsh.
macOS changed the default shell from Bash to Zsh in MacOS Catalina (v10.15) and later versions (BigSur and Monterey). The instructions are different for Bash and Zsh.
Zsh

home: \001
end: \005

You can enter these codes in the edit dialog by pressing ctrl-A for \001 and ctrl-E for \005. Thanks to @JW for the Zsh information.
Another, unrelated, option to map home/end keys for MacOS Catalina (v10.15) and later versions (BigSur and Monterey) is to use bindkey widgets:
sudo echo 'bindkey &quot;\033[H&quot; beginning-of-line; bindkey &quot;\033[F&quot; end-of-line' &gt;&gt; ~/.zshrc

Bash

home: \033[H
end:  \033[F

You can get the \033 part by hitting the escape key within the edit dialog input, if you need to add it.
In later versions of Mac OS X, if the terminal screen shifts up or down when you press the home/end key, the home key may need to be set to \033[1~ and the end key to \033[4~ to get the results you want (no shift needed).
Conclusion
Then home and end will work like normal again (phew).
Also note that alt+← and alt+→ by default in terminal map to word left and word right, another handy combo to remember.
Feel free to modify this answer to add more useful key bindings, as it is a community wiki.

**Reference**: https://apple.stackexchange.com/questions/12997/can-home-and-end-keys-be-mapped-when-using-terminal

> 📎 Source: https://apple.stackexchange.com/questions/12997/can-home-and-end-keys-be-mapped-when-using-terminal

#### 88. Remember window sizes and placement when unplugging and replugging second monitor

**Issue**: Remember window sizes and placement when unplugging and replugging second monitor
**Tags / Source**: Tags: macos, windows, display, window-manager, productivity | apple | 👍 157 | 💬 13 answers

**Description**:
Tags: macos, windows, display, window-manager, productivity | Score: 157 | Views: 68974 | Answers: 13

**Solution / Community Answer**:
Have a look at Stay by Cordless Dog. I believe it does exactly what you're looking for.

**Reference**: https://apple.stackexchange.com/questions/126351/remember-window-sizes-and-placement-when-unplugging-and-replugging-second-monito

> 📎 Source: https://apple.stackexchange.com/questions/126351/remember-window-sizes-and-placement-when-unplugging-and-replugging-second-monito

#### 89. Is there a way to convert audio files in Mac OS X or the command line without using iTunes?

**Issue**: Is there a way to convert audio files in Mac OS X or the command line without using iTunes?
**Tags / Source**: Tags: macos, audio, unix | apple | 👍 156 | 💬 9 answers

**Description**:
Tags: macos, audio, unix | Score: 156 | Views: 137510 | Answers: 9

**Solution / Community Answer**:
I installed ffmpeg via MacPorts, although it also available via Homebrew (brew install ffmpeg) or download the binary.
To convert something like that, (without worrying about audio quality, which I know nothing about), I just use:
ffmpeg -i input.mp4 output.mp3

Here is an example of how you would convert a .wav file to .mp3 from their website:
ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3 

Here is an example of how to find all .wav files larger than 50M, convert them to mp3 and then delete the original wav file (aka, batch mode -- alter the find command to create your 'batch')
find . -size +50M -iname '*.wav' -type f -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}.mp3 -y \; -exec /bin/rm {} \;

If you don't want to delete the source file, say in case the conversion fails or you want to have both:
find . -size +50M -iname '*.wav' -type f -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}.mp3 -y \;

Note that the -y overwrites existing files without prompting so if you want to not have that you can remove it.

**Reference**: https://apple.stackexchange.com/questions/26099/is-there-a-way-to-convert-audio-files-in-mac-os-x-or-the-command-line-without-us

> 📎 Source: https://apple.stackexchange.com/questions/26099/is-there-a-way-to-convert-audio-files-in-mac-os-x-or-the-command-line-without-us

#### 90. How do I start the docker daemon on macOS?

**Issue**: How do I start the docker daemon on macOS?
**Tags / Source**: Tags: macos, daemons, docker | apple | 👍 154 | 💬 9 answers

**Description**:
Tags: macos, daemons, docker | Score: 154 | Views: 547378 | Answers: 9

**Solution / Community Answer**:
An alternative solution is to use other runtime for docker. For example
colima
brew install colima
colima start
docker ps -a

Since docker desktop isn't free for enterprise usage, the alternative runtime is a good option.
NOTE: if you've previously used Docker Desktop for launching Docker daemon and had an export of DOCKER_HOST defined in your user's shell configuration (.bash_profile, .zsh_profile etc.), you need to re-specify DOCKER_HOST to make sure it points to .colima directory and commands like docker-compose up -d work properly.
Example:
export DOCKER_HOST=unix:///$HOME/.colima/docker.sock

**Reference**: https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos

> 📎 Source: https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos

#### 91. Update bash to version 4.0 on OSX

**Issue**: Update bash to version 4.0 on OSX
**Tags / Source**: Tags: macos, terminal, bash, command-line | apple | 👍 154 | 💬 6 answers

**Description**:
Tags: macos, terminal, bash, command-line | Score: 154 | Views: 138259 | Answers: 6

**Solution / Community Answer**:
As @William said in his answer, Apple does not provide bash 4 due to GPL restrictions. You can install bash 4+ however and also can make it your default shell (including for Terminal and iTerm2) by doing the following.

Install Bash 4 via Homebrew

First install the newer version of bash. There are various ways of doing that, I prefer Homebrew.


Install Homebrew as described at http://brew.sh.  
Install bash using brew install bash.


Bash 4 is now available on your PATH (assuming Homebrew bin is on your path). However, it is not yet your default shell. You can find where it is located by running which bash. In my case it is at /usr/local/bin/bash. 

Using Bash 4

Since it is on your PATH, you can start a Bash 4 session with just bash or it can be used in scripts by using a Shebang.

For example, this will use a specific bash instance.

#!/usr/local/bin/bash
...your script...


This will use the first bash on the PATH.

#!/usr/bin/env bash
...your script...


You can also set the bash path for specific profiles in Terminal/iTerm2 using the steps described in @user136952's answer.

Making Bash 4 the default

As mentioned above, after installing Bash 4 is still not the default shell. To make bash the default you need to do two more steps.

First, add the Bash 4 path to your /etc/shells file so that it is an allowed login shell. As described in /etc/shells, this file has the list of valid login shells. After adding the new bash path my /etc/shells looks like the following:

# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
/usr/local/bin/bash


Next we use chsh to make it your default shell. So any sessions for that user will use that shell. You can read more about this in Change the Shell in Mac OS X Terminal, but the actual command is very straightforward.

chsh -s /usr/local/bin/bash


Now the new bash is our default login shell. If you open Terminal or iTerm2 and run bash --version you should see the new version. Note the "License GPLv3+" which is why Apple doesn't bundle it with macOS.

$ bash --version
GNU bash, version 4.4.12(1)-release (x86_64-apple-darwin16.6.0)
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;

**Reference**: https://apple.stackexchange.com/questions/193411/update-bash-to-version-4-0-on-osx

> 📎 Source: https://apple.stackexchange.com/questions/193411/update-bash-to-version-4-0-on-osx

#### 92. cmd-tab behavior on Mavericks with multiple displays

**Issue**: cmd-tab behavior on Mavericks with multiple displays
**Tags / Source**: Tags: macos, display, application-switcher | apple | 👍 153 | 💬 5 answers

**Description**:
Tags: macos, display, application-switcher | Score: 153 | Views: 87913 | Answers: 5

**Solution / Community Answer**:
I believe this coincides with the Dock's location.  Just tested it on my MacBook Air, connected to a non-Apple external display, and whenever I moved the Dock from screen to screen the Application Switcher would follow.

You can summon the Dock on your big display by dragging the cursor to the bottom of it's display, essentially dragging down at the bottom.  After a second the Dock should pop up.  Once the Dock is on the desired display press commandtab to summon the Application Switcher.

**Reference**: https://apple.stackexchange.com/questions/106405/cmd-tab-behavior-on-mavericks-with-multiple-displays

> 📎 Source: https://apple.stackexchange.com/questions/106405/cmd-tab-behavior-on-mavericks-with-multiple-displays

#### 93. macOS notifications on dual monitors: how can I specify which monitor?

**Issue**: macOS notifications on dual monitors: how can I specify which monitor?
**Tags / Source**: Tags: macos, notifications, dual-screen | apple | 👍 152 | 💬 3 answers

**Description**:
Tags: macos, notifications, dual-screen | Score: 152 | Views: 96074 | Answers: 3

**Solution / Community Answer**:
You should be able to do this by choosing the monitor on which the menu bar is active.
Try:

System Settings -&gt; Displays -&gt; Arrangement

and drag the little white bar to the monitor where you want the notifications to show up.
In the picture below, the bar is being dragged from the left to the right window.

**Reference**: https://apple.stackexchange.com/questions/157260/macos-notifications-on-dual-monitors-how-can-i-specify-which-monitor

> 📎 Source: https://apple.stackexchange.com/questions/157260/macos-notifications-on-dual-monitors-how-can-i-specify-which-monitor

#### 94. Restricting Command+tab options to only apps that are in the current space

**Issue**: Restricting Command+tab options to only apps that are in the current space
**Tags / Source**: Tags: macos, spaces | apple | 👍 152 | 💬 12 answers

**Description**:
Tags: macos, spaces | Score: 152 | Views: 67784 | Answers: 12

**Solution / Community Answer**:
Refer to the original page for detailed solutions and community answers.

**Reference**: https://apple.stackexchange.com/questions/5668/restricting-commandtab-options-to-only-apps-that-are-in-the-current-space

> 📎 Source: https://apple.stackexchange.com/questions/5668/restricting-commandtab-options-to-only-apps-that-are-in-the-current-space

#### 95. Is there a command line program for macOS that can access serial ports?

**Issue**: Is there a command line program for macOS that can access serial ports?
**Tags / Source**: Tags: macos, command-line | apple | 👍 151 | 💬 16 answers

**Description**:
Tags: macos, command-line | Score: 151 | Views: 675404 | Answers: 16

**Solution / Community Answer**:
You can use the terminal command screen to do this!!!

As seen on ServerFault:


  I love using [screen] for connecting to serial consoles, i.e.

screen /dev/ttyS0 19200



Or, if you prefer Mac OS X hints...


  I often have to do router configuration via a console port, so I use a
  Keyspan Serial Adapter to get access. Two problems then present
  themselves: ZTerm is a horrible Mac OS X app. It hasn't been updated
  in five years or so, and isn't a Universal Binary. The developer
  doesn't seem in any hurry to rectify the situation. It is not worth
  the shareware fee in its current form. Minicom requires installation
  of Fink or MacPorts and is overly complex. Solution: Use screen,
  Terminal, and a little AppleScripting.
  
  First, launch Script Editor and type/paste in the following code:

tell application "Terminal"
  do script with command "screen /dev/tty.KeySerial1"
  set number of rows of window 1 to 100
  set number of columns of window 1 to 80
  set background color of window 1 to "black"
  set normal text color of window 1 to "green"
  set custom title of window 1 to "SerialOut"
end tell

  
  Compile and save as an app from within Script Editor, and you have a
  double-clickable application to launch a serial Terminal session. You
  may want to customize this slightly -- you can change the screen
  colors or number of columns or rows. You may also need to customize
  the screen command with a different device name if you are using
  something other than the Keyspan Serial Adapter (do an ls tty* of the
  /dev/ directory to get the right name). 
  
  screen uses Control-A to take commands directed to it. So type
  Control-A followed by Control-\ to exit your screen session. If you
  fail to do this and exit a Terminal session, you'll leave the screen
  session alive and the serial resource unavailable until you kill the
  screen session manually. man screen will show you further commands to
  send to a screen session. 
  
  If anyone can reply with a link to a tutorial on how to wrap an
  interactive Unix App in Cocoa, that would be the next step -- it would
  be nice to do this without involving Terminal. If you prefer to use
  Minicom, you could still use the AppleScript to wrap it into a nice
  launchable app -- use this older hint to find the right command line
  commands.


Many USB-Serial adapters use the chip from FTDI. Install the "Virtual COM Port" driver and look for the proper TTY name in /dev. For example, on a PowerBook G4 it came up as /dev/tty.usbserial-FTALKY8I.

**Reference**: https://apple.stackexchange.com/questions/32834/is-there-a-command-line-program-for-macos-that-can-access-serial-ports

> 📎 Source: https://apple.stackexchange.com/questions/32834/is-there-a-command-line-program-for-macos-that-can-access-serial-ports

#### 96. How do I sync the Visual Studio Code (vscode) theme to use my OS light/dark color scheme?

**Issue**: How do I sync the Visual Studio Code (vscode) theme to use my OS light/dark color scheme?
**Tags / Source**: Tags: macos, system-settings, visual-studio-code | apple | 👍 151 | 💬 3 answers

**Description**:
Tags: macos, system-settings, visual-studio-code | Score: 151 | Views: 54183 | Answers: 3

**Solution / Community Answer**:
Enable Auto Detect (Search in Settings: window.autoDetectColorScheme)
Customize Color Themes (Search in Settings: workbench preferred color theme)


More Detail (Visual Studio Code Themes):

Auto switch based on OS color scheme Windows and macOS support light and dark color schemes. There is a setting, window.autoDetectColorScheme, that instructs VS Code to listen to changes to the OS's color scheme and switch to a matching theme accordingly.
To customize the themes that are used when a color scheme changes, you can set the preferred light, dark, and high contrast themes with the settings:
workbench.preferredLightColorTheme - defaults to &quot;Default Light+&quot;
workbench.preferredDarkColorTheme - defaults to &quot;Default Dark+&quot;
workbench.preferredHighContrastColorTheme - defaults to &quot;Default High Contrast&quot;
workbench.preferredHighContrastLightColorTheme - defaults to &quot;Default High Contrast Light&quot;

**Reference**: https://apple.stackexchange.com/questions/381962/how-do-i-sync-the-visual-studio-code-vscode-theme-to-use-my-os-light-dark-colo

> 📎 Source: https://apple.stackexchange.com/questions/381962/how-do-i-sync-the-visual-studio-code-vscode-theme-to-use-my-os-light-dark-colo

#### 97. How to record both screen and sound with Quicktime on El Capitan?

**Issue**: How to record both screen and sound with Quicktime on El Capitan?
**Tags / Source**: Tags: macos, quicktime, screen-capture | apple | 👍 150 | 💬 12 answers

**Description**:
Tags: macos, quicktime, screen-capture | Score: 150 | Views: 438170 | Answers: 12

**Solution / Community Answer**:
You  need to install Soundflower in order to run it on El Capitan. El Capitan requires kext to be signed in order to load them. This one gets its kext installed in /Library/Extensions/.

This is due to System Integrity Protection

Then, you have to create a multi-output device with: Audio MIDI Setup.app, which is found in /Applications/Utilities/ :



Finally, when you want to do the actual recording, make sure you use this multi-output device, and capture from the same Soundflower device used in this multi-output device. Otherwise, you can't both listen to and capture the sound, because it goes directly to soundflower without being copied to the built-in output.

alt/option + right clicking on volume gives you this menu:



and Quicktime now looks like this:

**Reference**: https://apple.stackexchange.com/questions/212829/how-to-record-both-screen-and-sound-with-quicktime-on-el-capitan

> 📎 Source: https://apple.stackexchange.com/questions/212829/how-to-record-both-screen-and-sound-with-quicktime-on-el-capitan

#### 98. Should I disconnect my MacBook Pro&#39;s power cord when the battery is fully charged?

**Issue**: Should I disconnect my MacBook Pro&#39;s power cord when the battery is fully charged?
**Tags / Source**: Tags: macbook-pro, battery, charging | apple | 👍 149 | 💬 12 answers

**Description**:
Tags: macbook-pro, battery, charging | Score: 149 | Views: 263777 | Answers: 12

**Solution / Community Answer**:
You do not need to disconnect your MacBook Pro's battery. Your battery will stop charging once it is full. Apple's modern batteries are much smarter than previous designs.

To get the most out of your MacBook Pro's battery, follow the Notebook Battery advice from Apple: unplug and use your battery until empty about once a month, then charge back up to full.

At the time of answering, Apple's advice read:


  For proper maintenance of a lithium-based battery, it’s important to keep the electrons in it moving occasionally. Apple does not recommend leaving your portable plugged in all the time. An ideal use would be a commuter who uses her notebook on the train, then plugs it in at the office to charge. This keeps the battery juices flowing.


If you need help following Apple's advice, use Battery Guardian; it is free and will remind you when to deplete your battery.

**Reference**: https://apple.stackexchange.com/questions/12271/should-i-disconnect-my-macbook-pros-power-cord-when-the-battery-is-fully-charge

> 📎 Source: https://apple.stackexchange.com/questions/12271/should-i-disconnect-my-macbook-pros-power-cord-when-the-battery-is-fully-charge

#### 99. Is there a keyboard shortcut to navigate one level up in Finder?

**Issue**: Is there a keyboard shortcut to navigate one level up in Finder?
**Tags / Source**: Tags: macos, finder | apple | 👍 148 | 💬 1 answers

**Description**:
Tags: macos, finder | Score: 148 | Views: 91953 | Answers: 1

**Solution / Community Answer**:
The one you're probably looking for is the command ⬆︎ keyboard shortcut, as this is the one that takes you back to the parent folder. 

To do the same thing, but within a new window, use command control ⬆︎.

However, some views offer additional options. For example, in Columns view you can just use the ⬅︎ key to go back to the parent folder.

In addition, you can use the command [ keyboard shortcut to take you back to the previous folder you were actually in (which may not necessarily be the parent folder).

You can also right-click on the title in the Finder's window to select anywhere in the file's path to go straight to that location.

Finally, you can also customise the Toolbar to add the Path button.

**Reference**: https://apple.stackexchange.com/questions/307930/is-there-a-keyboard-shortcut-to-navigate-one-level-up-in-finder

> 📎 Source: https://apple.stackexchange.com/questions/307930/is-there-a-keyboard-shortcut-to-navigate-one-level-up-in-finder

#### 100. How to investigate high kernel task memory usage?

**Issue**: How to investigate high kernel task memory usage?
**Tags / Source**: Tags: macos, memory, performance, kernel-panic, kernel | apple | 👍 147 | 💬 2 answers

**Description**:
Tags: macos, memory, performance, kernel-panic, kernel | Score: 147 | Views: 233652 | Answers: 2

**Solution / Community Answer**:
There are many things that go wrong with high kernel task usage. Usually this is related to faulty or heavy process which overusing system resources (such as indexing storage, running VMs, too many tabs in the web browser or some other background processes). 

Here are some methods which help to investigate OS X kernel usage issues:

Basic methods


Run Console.app and check on 'All Messages' to see if anything unusual currently is happening.
Use Activity Monitor to read system memory and determine how much CPU, RAM and Disk is being used.

Alternatively run top in Terminal and hold Space to refresh - easier to find the cause problem (swapins/swapouts/disks?).
Run sudo fs_usage in Terminal to report system calls and page faults related to filesystem activity in real-time (I think this is the best option from all other). Then hit Control-C to stop it.

Action: Consider killing apps which appears frequently on the list, but you're not using them.

Learn more at: How do I debug an out-of-control “kernel_task” process?
Run sudo syscallbypid.d (or syscallbyproc.d), wait a bit, hit Control-C. Now check which process generated the most system calls in that given time (last column) and if you recognise it, consider kill it. If not, Google it and learn more about it.


Advanced methods


Use sysdiagnose command (can be triggered by hitting Shift-Control-⌥-⌘-. (period) to quickly gather system-wide diagnostic information helpful in investigating system memory/performance issues (will appear in /var/tmp) either by you or Apple guys. During analysis, try to not do anything, when done - consider uncompressing the generated file and analyse the logs.

See: How do you get system diagnostic files from OS X?
Run footprint to gather detailed memory information on a per-VM-region type level and swapped bytes:

sudo footprint -a


Older version:

sudo footprint -all -categories -swapped -collapseSharing

Use spindump to profile entire system, it'll generate /tmp/spindump.txt file (including kernel and its extensions).
Use vm_stat to show virtual memory statistics. E.g.

vm_stat 1 # to display every second.

Use zprint to check information about kernel usage, it's possible by:

sudo zprint -t -s | head -n20


It'll show the most wasting kernel zones.
Use newproc.d to snoop new processes as they are executed, creatbyproc.d for files:

sudo newproc.d
sudo creatbyproc.d


Note: On newer OS X (10.11 or above) this may not work when integrity protection is enabled (check by csrutil status). 
Try sar - system activity reporter which can sample and report various cumulative statistic counters maintained by the operating system.


For more useful debugging tools, check for dtrace scripts (grep dtrace /usr/bin/*). If you know the faulty process which causing the problem, you may use dtruss to debug it.



Actions

Here are some suggestions which can help you with the operating system issues.


Free up some inactive memory. In order to do this, you've to flush cache first and force disk cache to be purged:

sync &amp;&amp; sudo purge



  sync - force completion of pending disk writes (flush cache)
  
  purge - force disk cache to be purged (flushed and emptied)


Its function is basically to terminate all the I/O pending operations which are using disk cache and then to free all the occupied disk cache, so it should free disk space to ease paging out and swapping out of main memory. It is safe to use, as it does not affect anonymous memory that has been allocated through malloc, vm_allocate, etc.
Use some 3rd party apps to clear up some overused memory such as iBoostUp, SystemPal, etc.
You may also disable temporary Spotlight:

sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist 


And consider other services by:

sudo launchctl list | grep ^[0-9]
sudo launchctl bslist | grep ^A

Quit your web browser and check if that helps. For example using Chrome is very resourceful, especially when there is some front-end processing going on in the background (e.g. Javascript) or advert-like animations are constantly rendering the content.

**Reference**: https://apple.stackexchange.com/questions/178281/how-to-investigate-high-kernel-task-memory-usage

> 📎 Source: https://apple.stackexchange.com/questions/178281/how-to-investigate-high-kernel-task-memory-usage



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
