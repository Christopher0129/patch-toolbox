# Linux 常见故障及解决方法 | Linux Common Issues & Solutions

<!-- 语言切换 / Language Switch -->
<p align="center">
  <a href="#-中文-zh">中文 🇨🇳</a> &nbsp;|&nbsp; <a href="#-english-en">English 🇺🇸</a>
</p>

---


_自动更新于 / Auto-updated: 2026-04-27 09:30:57 UTC_

## 中文 🇨🇳
**Linux 常见故障及解决方法**

本页面每6小时自动从 Stack Exchange、Reddit、V2EX 抓取 LINUX 平台常见故障及解决方法。

### LINUX 常见故障及解决方法

#### 1. [V2EX] Gnome 桌面下截图上传到 imgur 的 extension

**故障现象**: [V2EX] Gnome 桌面下截图上传到 imgur 的 extension
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
Gnome50/Debian13 上测试通过的特别方便 V2EX 上发图片，就像我现在这样     https://github.com/wuruxu/gnome-shell-extension-imgur

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1207063#reply3

> 📎 来源 / Source: https://www.v2ex.com/t/1207063#reply3

#### 2. [V2EX] Manjaro 真不错

**故障现象**: [V2EX] Manjaro 真不错
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
本来打算直接 ubuntu 的，但这个时间节点有点尴尬，26.04LTS 快发又还没发。试了下 Manjaro ，几乎开箱即用了~linux 没有微信语音输入有点难受 = =

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1207001#reply32

> 📎 来源 / Source: https://www.v2ex.com/t/1207001#reply32

#### 3. [V2EX] 写了个 lottie 动画在 Linux 桌面上顶层播放的小东西

**故障现象**: [V2EX] 写了个 lottie 动画在 Linux 桌面上顶层播放的小东西
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
写了个 lottie 动画在 linux 桌面上顶层播放的小东西，可以用在和 codex/claude 回复结束后，播放一个小动画提示，没什么用的玩具
https://github.com/xxyangyoulin/linux-lottie-salute

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1206873#reply7

> 📎 来源 / Source: https://www.v2ex.com/t/1206873#reply7

#### 4. [V2EX] LXC veth 桥接网络模式下如何避免发送的数据包被拆成小包？

**故障现象**: [V2EX] LXC veth 桥接网络模式下如何避免发送的数据包被拆成小包？
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
网卡是 rtl8127, 用 iperf3 测速，在 host 上测速可以达到 9.42 Gbits/sec ，在 lxc 里测速只有 3.25 Gbits/sec ，造成这么大差异的原因是在 lxc 里发送的数据包被拆成了 1.5KB 的小包（也就是 mtu 的大小），而在 host 上发送的数据包是几十 KB 的大包，我想知道如何让 lxc 里发送的数据包也是几十 KB 的大包，有 v 友对这个问题感兴趣愿意一起研究一下吗？
在 host 上运行 iperf3 发包时 sar 的输出如下：
d@develop:~/test$ sar -n DEV 1 | awk '/IFACE/ &amp

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1206865#reply13

> 📎 来源 / Source: https://www.v2ex.com/t/1206865#reply13

#### 5. [V2EX] 使用 auto-cpufreq 平衡 Linux 性能功耗

**故障现象**: [V2EX] 使用 auto-cpufreq 平衡 Linux 性能功耗
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
在 Fedora Linux 下，调整系统使用 auto-cpufreq 速度和功耗优化器。

搭载 Intel Core Ultra 7 255H 处理器的设备，离电状态进行日常网页浏览、写作和听音乐等轻度任务时的功耗表现，基本维持在 10W 左右。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1206814#reply3

> 📎 来源 / Source: https://www.v2ex.com/t/1206814#reply3

#### 6. [V2EX] 我的硬盘 Memblaze Pblaze 5 Linux 下不识别，给 Linux 内核提交了补丁， AI 说有望被合并

**故障现象**: [V2EX] 我的硬盘 Memblaze Pblaze 5 Linux 下不识别，给 Linux 内核提交了补丁， AI 说有望被合并
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
几年前在咸鱼上淘到几块国产硬盘，型号是 Memblaze Pblaze 516
Windows 下使用没有问题，但是在折腾 PVE 的时候遇到了问题，压根不识别这块硬盘。
然后我又试了好几个 Linux 发行版，某些旧内核版本反而能识别，
我根据 dmesg 信息和 pci 信息搜索，发现 bugzilla 上有类似的案例，
Bug 205679 - not able to recognize NVME's partition
https://bugzilla.kernel.org/show_bug.cgi?id=205679
我通过里面讨论的信息，自己写了个补丁（其实就加了 2 行设备信息）

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1206374#reply4

> 📎 来源 / Source: https://www.v2ex.com/t/1206374#reply4

#### 7. [V2EX] Linux nfs 客户端如何快速删除大量小文件

**故障现象**: [V2EX] Linux nfs 客户端如何快速删除大量小文件
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
linux 下有个程序每天在 NFS 共享目录（生成一个当天日期的文件夹）下缓存 100 万左右的文件，大小差不多 3-5T ，这个程序处理完成后可以删除，如何在 Linux 下快速删除它们呢。
按照网上的这个同步空目录的方法，差不多耗时 7 个小时。
rsync --delete-before -d -H -O --progress /tmp/empty/ 2026-04-02/

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1206234#reply21

> 📎 来源 / Source: https://www.v2ex.com/t/1206234#reply21

#### 8. [V2EX] 写了个 Nautilus Extension: Copy File Path

**故障现象**: [V2EX] 写了个 Nautilus Extension: Copy File Path
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
Gnome50/Debian 环境中测试通过的，方便我在 Nautilus 文件管理器中复制路径      AI 时代，软件可以按个人定制      https://github.com/wuruxu/nautilus-copypath

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1205636#reply0

> 📎 来源 / Source: https://www.v2ex.com/t/1205636#reply0

#### 9. [V2EX] Linux /Ubuntu 上如何实现连接两个不同的 wifi 解决实际需求。

**故障现象**: [V2EX] Linux /Ubuntu 上如何实现连接两个不同的 wifi 解决实际需求。
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
背景：

自用电脑是联想小新 pro 14 ，装有 ubuntu24.04, 支持 wifi6
公司有 wifi A 和 wifi B ，wifi A 是国内的普通宽带，wifi B 是连接香港的专线。
服务器 ssh 连接限定了必须是使用 wifi A 
wifi B 由于是香港专线，可以自由访问谷歌等网站，无需翻墙。 使用 wifi A 则需要借助 Clash(虽然公司有订阅套餐)

目前我的需求是

指定某些软件/程序，例如是 teams,ssh 等使用 wifi A; 指定浏览器使用 Wifi A/B 

求助大佬们，我应该如何实现上述需求？是否需要增购 USB wifi ？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1204573#reply8

> 📎 来源 / Source: https://www.v2ex.com/t/1204573#reply8

#### 10. [V2EX] 115 网盘如何多端稳定挂载？

**故障现象**: [V2EX] 115 网盘如何多端稳定挂载？
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
修复了存储状态不一致的问题，加强了稳定性
更新了安全提示



115 网盘的挂载功能存在一个严重限制：当你有两个 VPS 想挂载同一个 115 网盘账号时，你会发现：一边刚挂载成功，另一边就被踢下线。
这种报错，本质上是 115 网盘的防盗机制：当刷新 token 的时候会导致此应用获取的旧 token 失效。对于同一 app 的不同挂载，同样成立。 


如果没有防盗链：当有人窃取了你的 refreshtoken 之后，黑客就可以获取你的数据长达一年（除非你手动去吊销你的 token ，并重新获取） 这种方式诚然会提高安全性，但是在多端挂载的场景下反而成为了使用的阻碍。 

因此我搓了一个

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1203862#reply3

> 📎 来源 / Source: https://www.v2ex.com/t/1203862#reply3

#### 11. [V2EX] Linux 桌面环境 orWM 推荐

**故障现象**: [V2EX] Linux 桌面环境 orWM 推荐
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
RT ，当前在用 kde plasma ，但是感觉设置项太多，我也不喜欢 QT ，想换一下
主要是想有鼠标时可以鼠标操作，出差时使用触控板进行操作，似乎 gnome 不错，但是不知道现在还稳定不，几年前用的时候动不动插件就用不了了....当然，我也只用一些基础插件。
有人用 hyprland 吗？操作体验怎么样，桌面似乎是不能显示文件吗？鼠标和触控板操作不知道怎么样，有没有老哥解答一下，我的机器是 thinkbook 14+ 2024 ultra7 版本

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1203303#reply46

> 📎 来源 / Source: https://www.v2ex.com/t/1203303#reply46

#### 12. [V2EX] 如何解决 eBPF sockmap 重定向转发中背压缺失带来的 OOM ？

**故障现象**: [V2EX] 如何解决 eBPF sockmap 重定向转发中背压缺失带来的 OOM ？
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我在尝试使用 eBPF 的 BPF_PROG_TYPE_SK_SKB 与 BPF_MAP_TYPE_SOCKHASH 实现 socket 的铰接转发，目标是基于 bpf_sk_redirect_hash 将一个 socket 的 ingress 队列数据转发到另一个 socket 的 egress 队列，但是在实际的吞吐量测试时出现了系统 OOM 。
具体的环境如下：

Linux Kernel 6.8
2 个 socket 所处网络接口不同，且 2 个网络接口带宽不一致，转发源 socket 所处接口 (测试用的 loopback) 带宽高于目标 socket 所处带宽
吞吐测试是在 loo

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1202372#reply11

> 📎 来源 / Source: https://www.v2ex.com/t/1202372#reply11

#### 13. [V2EX] 还是要用 ubuntu

**故障现象**: [V2EX] 还是要用 ubuntu
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
过去一直用 windows 开发，编码问题，行尾问题，使用 docker 绑定目录也会有同步问题。


后来就转到 wsl 中开发，但是不好说是 wsl 的 bug 还是 docker 的 bug ，经常出现磁盘读写 100%，
磁盘完全占满后所有 app 都不能正常工作了。


然后就转 linux ，选的三个 mint ，debian/kde ，ubuntu
先用 live 模式尝试，ubuntu 出现了一点卡顿就放弃了，尝试 mint 发现官方网站上列了很多已知问题，
我不敢用，debian 暂时没有发现问题，就安装了，用了之后才发现这个 debian 反而经常出现 freeze 的情况

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1201875#reply53

> 📎 来源 / Source: https://www.v2ex.com/t/1201875#reply53

#### 14. [V2EX] nfs mv 的操作是原子的么？ A 节点 move， B 节点要么完全可见，要么完全不可见？

**故障现象**: [V2EX] nfs mv 的操作是原子的么？ A 节点 move， B 节点要么完全可见，要么完全不可见？
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
比如机器 A 、B 的/data 挂载了同一个 nfs 挂载点，A 机器/data 目录下有一个文件夹 a 下有 10000 个文件，我把/data/a 移动到/data/b ，对于机器 B 而言，如果节点 A 上已经看到 move 完成了，那么节点 B 上由于 nfs 异步延迟的存储，可能前几秒看不到这个移动的操作，过几秒之后可以看到/data/a 变成了/data/b ，那么存不存在一个中间状态，我能看到/data/b ，但是/data/b 下只有比如 2000 个文件

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1200802#reply1

> 📎 来源 / Source: https://www.v2ex.com/t/1200802#reply1

#### 15. [V2EX] 求助 Linux 桌面环境软件

**故障现象**: [V2EX] 求助 Linux 桌面环境软件
**标签 / 来源**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
马上要转过去了。麒麟信安 kylinSEC OS   arm ，看了下好像是类红帽的，rpm 包。昨晚翻吐了没找到几个软件。有经验的前辈推荐些常用软件吧。目前有 idea 、redis 、dbeaver ，没找到离线翻译的，有道官网没 arm 版。另外现在 idea 还能离线 2099 吗，好久没折腾了。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1200587#reply21

> 📎 来源 / Source: https://www.v2ex.com/t/1200587#reply21

#### 16. [V2EX] ubuntu 上有没有基于 OpenGL 的原生 3d 游戏

**故障现象**: [V2EX] ubuntu 上有没有基于 OpenGL 的原生 3d 游戏
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
记得很多年前玩过一款，通过 .deb 安装的，3D 飞行躲避障碍的，想在想不起来名字了。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1188348#reply2

> 📎 来源 / Source: https://www.v2ex.com/t/1188348#reply2

#### 17. [V2EX] ubuntu 下的风扇转速控制？

**故障现象**: [V2EX] ubuntu 下的风扇转速控制？
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
家里的电脑装的 pc 用的水冷。
在 win 下面，因为装了厂商的驱动，貌似正常办公的时候，风扇转速很低，没有声音。但是 ubuntu 下面，貌似已启动就是高速。。。不知道各位佬们在 ubuntu 下面可以怎样也控制下显卡和水冷风扇的转速嘛？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1187869#reply5

> 📎 来源 / Source: https://www.v2ex.com/t/1187869#reply5

#### 18. [V2EX] 求推荐 Ubuntu 好用的 ssh 工具

**故障现象**: [V2EX] 求推荐 Ubuntu 好用的 ssh 工具
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:


**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1177713#reply53

> 📎 来源 / Source: https://www.v2ex.com/t/1177713#reply53

#### 19. [V2EX] ubuntu 26.04 有人体验了吗, 有国内的可用镜像吗

**故障现象**: [V2EX] ubuntu 26.04 有人体验了吗, 有国内的可用镜像吗
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:


**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1171076#reply6

> 📎 来源 / Source: https://www.v2ex.com/t/1171076#reply6

#### 20. [V2EX] 15 年前的 ubuntu 官方安装盘有人要么

**故障现象**: [V2EX] 15 年前的 ubuntu 官方安装盘有人要么
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
[有图有真相]( https://aifeixiang.feishu.cn/wiki/C6IcwFfMnirMX7kpz33cUASknDc)9.10 ，10.04, 10.10  整理书柜找到的，保存完好。 大学的时候申请的，没人要就扔掉了。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1150108#reply11

> 📎 来源 / Source: https://www.v2ex.com/t/1150108#reply11

#### 21. [V2EX] 该装服务器了，装 Ubuntu24.04.2 还是 Ubuntu22.04.5

**故障现象**: [V2EX] 该装服务器了，装 Ubuntu24.04.2 还是 Ubuntu22.04.5
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
预计要用个四五年，预计部署网站和 MCP 服务端，用最新的 24.04.2 还是上个稳定版本 22.04.5 ？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1144421#reply95

> 📎 来源 / Source: https://www.v2ex.com/t/1144421#reply95

#### 22. [V2EX] ubuntu 加显卡后感觉动画卡顿

**故障现象**: [V2EX] ubuntu 加显卡后感觉动画卡顿
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
升级之前使用 GTX 950 2G


升级成 GTX 950 2G + 4060TI16G 


xorg 配置系统使用 950 ，4060 留作炼丹


按 win 键时 950 负载很高，动画卡顿，加之前没有这个感觉


为啥不用 Wayland, vscode 在 wayland 下使用感受很差


vscode gpu 加速已经送了，不然显存要炸


求大佬解惑

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1138312#reply7

> 📎 来源 / Source: https://www.v2ex.com/t/1138312#reply7

#### 23. [V2EX] vmware17 安装 ubuntu22.04.5，最后一步报错

**故障现象**: [V2EX] vmware17 安装 ubuntu22.04.5，最后一步报错
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我的硬件是 e5-2697v4 双路，请问如何解决？具体情况，如图：

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1126019#reply23

> 📎 来源 / Source: https://www.v2ex.com/t/1126019#reply23

#### 24. [V2EX] 求 Ubuntu 台式机指纹 USB 识别器推荐

**故障现象**: [V2EX] 求 Ubuntu 台式机指纹 USB 识别器推荐
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
最近使用 Ubuntu 22.04 台式机作为主力机，需要一个指纹 USB 识别器，主要用于指纹登录和 sudo 密码验证。之前咸鱼过一个 Kensington VeriMark Desktop Fingerprint Key ，发现 libfprint 不支持，请问大佬们有推荐的吗？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1117952#reply8

> 📎 来源 / Source: https://www.v2ex.com/t/1117952#reply8

#### 25. [V2EX] ubuntun 下 docker 拉取镜像失败，配置了镜像源，但是无效

**故障现象**: [V2EX] ubuntun 下 docker 拉取镜像失败，配置了镜像源，但是无效
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
已在 daemon.json 配置了多个镜像源：
DaoCloud 镜像站： https://docker.m.daocloud.io
腾讯云公共镜像库： https://mirror.ccs.tencentyun.com
华为云镜像服务： https://developer.huaweicloud.com/dm/mirrors
1Panel 镜像源： https://docker.1panel.live
Unsee 镜像源： https://docker-0.unsee.tech
1ms.run 镜像源： https://docker.1ms.run
Azure 中国镜像： http://m

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1112655#reply23

> 📎 来源 / Source: https://www.v2ex.com/t/1112655#reply23

#### 26. [V2EX] 我的 ubantu 服务器是不是被人植入了恶意代码了

**故障现象**: [V2EX] 我的 ubantu 服务器是不是被人植入了恶意代码了
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我的 ubantu 服务器是不是被人植入了恶意代码。。。。
我上面只跑了我的博客，都是 nodejs ，nginx ，mysql 和 Let's Encrypt 证书管理，没有跑过其他服务。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1107484#reply24

> 📎 来源 / Source: https://www.v2ex.com/t/1107484#reply24

#### 27. [V2EX] ubuntu 用 vbetool dpms off 了再 on 后，显示乱码

**故障现象**: [V2EX] ubuntu 用 vbetool dpms off 了再 on 后，显示乱码
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:


**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1106291#reply2

> 📎 来源 / Source: https://www.v2ex.com/t/1106291#reply2

#### 28. [V2EX] WIN11 访问 UBUNTU 的 webdav 记不住账号

**故障现象**: [V2EX] WIN11 访问 UBUNTU 的 webdav 记不住账号
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我之前由于/目录所有者换成了用户，没办法只好重装了电脑，安装的还是 UBUNTU24
开了 webdav 共享，在 WIN11 上面用映射的方式访问。
但是每次访问，默认登录的用户名都是微软账号，无论我怎么选择保存，都是这样，好像跟我登录 windows 的账号一样，可我在 webdav 上设置了用户名和密码。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1100930#reply1

> 📎 来源 / Source: https://www.v2ex.com/t/1100930#reply1

#### 29. [V2EX] Linux 安装完系统后默认是安装好显卡驱动吗？

**故障现象**: [V2EX] Linux 安装完系统后默认是安装好显卡驱动吗？
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
以前安装 WINDOWS 系统后，开机第一件事是安装各种驱动，包括最重要的显卡驱动使用过 linux ，发现安装完系统后好像都是各种 sudo apt update,貌似都不需要安装各类驱动的说法，今天打开 AMD 的官网，才发现 AMD 官网就有提供显卡驱动，用 LINUX 这么久了，貌似以前就没有主动安装显卡驱动，安装完 LINUX 后都是开箱即用，几条命令更新后就开始使用了，汗。所以想问下，linux 全新安装完系统后不需要安装各类驱动吗，包括显卡驱动。最近用 Ubuntu ，发现文件夹经常会卡住没反应，是没安装驱动的锅吗

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1097632#reply14

> 📎 来源 / Source: https://www.v2ex.com/t/1097632#reply14

#### 30. [V2EX] 闯了大祸,根目录权限变成我自己了。

**故障现象**: [V2EX] 闯了大祸,根目录权限变成我自己了。
**标签 / 来源**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我的磁盘空间不够了，之前分区的时候没搞好，根目录给了 1.7T 一直闲置，为了下载一个 700 多 G 的文件，我简单的 mount 到了一个下载目录下，transmission 下载的时候报错说权限问题，我直接 chown -R uuair:www-data 了，我还纳闷，一个空目录，怎么会卡住了。。。结果 sudo 的时候发现错误，然后，./目录下大部分文件都不是 root 的了，尤其是/etc 下，所有的都是我了。
好了，现在怎么办？  
第一：/home文件夹下有 3.2T 的文件，我没有其他的硬盘可以备份。
第二：我运行了 12 个 docker ，其中有几个配置了很久，可能我自己都

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1095187#reply50

> 📎 来源 / Source: https://www.v2ex.com/t/1095187#reply50

#### 31. [V2EX] 各大镜像站不再提供 Debian12 下载？

**故障现象**: [V2EX] 各大镜像站不再提供 Debian12 下载？
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
今天很多国内镜像站（清华 中科大等）的 Debian 12 ISO 下载链接变成了 404 （例如 debian-cd 目录下的 12.x ISO ）。
据说是因为 Debian 13 今天正式成为 stable 
是不是我搞错了？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1198396#reply2

> 📎 来源 / Source: https://www.v2ex.com/t/1198396#reply2

#### 32. [V2EX] Debian 26 届年会现在可以开始报名注册啦！

**故障现象**: [V2EX] Debian 26 届年会现在可以开始报名注册啦！
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
大家好！
Debian 26 届年会现在可以开始报名注册啦！
https://debconf26.debconf.org/
这次年会在 阿根廷 的 圣达菲（ Santa Fe ） 举行。
（一）飞机
目前国内上海有到阿根廷首都布宜诺斯艾利斯的直飞航班（机场代码：EZE ），经停 新西兰 的 奥克兰。
全程 25 个多小时，全国联运。
去程（上海→布宜诺斯艾利斯）：MU745 ，每周一、周四执行，北京时间 02:00 从上海浦东机场起飞，当地时间 16:55 抵达。‌‌
回程（布宜诺斯艾利斯→上海）：MU746 ，每周二、周五执行，当地时间 02:00 起飞，北京时间次日 18:00 抵达。‌‌

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1192842#reply0

> 📎 来源 / Source: https://www.v2ex.com/t/1192842#reply0

#### 33. [V2EX] debian13 有必要升级吗？感觉 12 还能坚持好几年

**故障现象**: [V2EX] debian13 有必要升级吗？感觉 12 还能坚持好几年
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:


**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1190787#reply3

> 📎 来源 / Source: https://www.v2ex.com/t/1190787#reply3

#### 34. [V2EX] Debian 龙芯 移植进度

**故障现象**: [V2EX] Debian 龙芯 移植进度
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
base-files_14_loong64.changes ACCEPTED into unstable Debian FTP Masters
dpkg_1.22.21_loong64.changes ACCEPTED into unstable Debian FTP Masters
make-dfsg_4.4.1-3_loong64.changes ACCEPTED into unstable Debian FTP Masters
binutils_2.45.50.20251209-1_loong64.changes ACCEPTED into unstable Debian FTP Mas

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1178918#reply3

> 📎 来源 / Source: https://www.v2ex.com/t/1178918#reply3

#### 35. [V2EX] Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁

**故障现象**: [V2EX] Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁
https://www.reddit.com/r/zfs/comments/1oivqx1/debian_13_root_on_zfs_with_native_encryption_and/

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1169507#reply0

> 📎 来源 / Source: https://www.v2ex.com/t/1169507#reply0

#### 36. [V2EX] 香橙派 5Plus 小服务器已升级 Debian13

**故障现象**: [V2EX] 香橙派 5Plus 小服务器已升级 Debian13
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
香橙派 5Plus RK3588 16G ，作家庭服务器用的，内核是 6.1.43-rockchip-rk3588 。已升级 Debian13 ，先用着了，看看有没有问题。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1151947#reply4

> 📎 来源 / Source: https://www.v2ex.com/t/1151947#reply4

#### 37. [V2EX] Debian 13 “trixie” released

**故障现象**: [V2EX] Debian 13 “trixie” released
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
https://www.debian.org/News/2025/20250809
正式新闻终于出了

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1151300#reply4

> 📎 来源 / Source: https://www.v2ex.com/t/1151300#reply4

#### 38. [V2EX] 安装 debian 的时候如何跳过创建普通用户？

**故障现象**: [V2EX] 安装 debian 的时候如何跳过创建普通用户？
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:


**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1141239#reply5

> 📎 来源 / Source: https://www.v2ex.com/t/1141239#reply5

#### 39. [V2EX] debian 12 的体验真的很糟糕

**故障现象**: [V2EX] debian 12 的体验真的很糟糕
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
各种小问题最让人受不了的是 ibus 输入法。无论我是清除本地数据文件，还是 remove 再 reinstall ，都解决不了这只是我的个案吗？看起来 debian 13 也快来了不然我都想切换到 fedora

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1119550#reply14

> 📎 来源 / Source: https://www.v2ex.com/t/1119550#reply14

#### 40. [V2EX] debian12.8 的 preseed 自动安装方式，封装 iso 的正确方式？?

**故障现象**: [V2EX] debian12.8 的 preseed 自动安装方式，封装 iso 的正确方式？?
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
先做了这些事情(debian-12.8.0-amd64-DVD-1.iso 是官网下载的)
apt install debian-cd isolinux genisoimage
mount -o loop /opt/mkiso/debian-12.8.0-amd64-DVD-1.iso /mnt
mkdir /opt/debian_custom
cp -r /mnt/* /opt/debian_custom/
cp /opt/preseed.cfg /opt/debian_custom/preseed.cfg
chmod +w /opt/debian_custom/isolinux/txt.c

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1102156#reply0

> 📎 来源 / Source: https://www.v2ex.com/t/1102156#reply0

#### 41. [V2EX] Debian12 VNC 连接时怎么才能以 Root 的身份登录桌面环境

**故障现象**: [V2EX] Debian12 VNC 连接时怎么才能以 Root 的身份登录桌面环境
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
已具备条件：
桌面环境已具备
Root 可以通过桌面环境正常登录
普通用户已经具备 sudo
防火墙没有开启
vncserver 搭建成功了，且普通用户能正常登录桌面环境，但是为普通用户身份
希望达成的目标：
以 vnc 的方式连接上 debian 后，能切换至 root 身份进行可视化操作（非终端命令切换）

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1093953#reply2

> 📎 来源 / Source: https://www.v2ex.com/t/1093953#reply2

#### 42. [V2EX] 我成功申请成为 Debian 正式成员， id 是 atzlinux

**故障现象**: [V2EX] 我成功申请成为 Debian 正式成员， id 是 atzlinux
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
在中国大陆这边，目前还不到 10 个人。比印度少哈，目前 印度有 16 ，17 个吧。

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1085701#reply6

> 📎 来源 / Source: https://www.v2ex.com/t/1085701#reply6

#### 43. [V2EX] Debian 这个系统你们一般怎么读？

**故障现象**: [V2EX] Debian 这个系统你们一般怎么读？
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
我一般读：德编
有的人读：呆边
还听说有人就说大便系统。（戏谑说法）
今天听到有个人读：得（ dei3 ）变

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1081704#reply72

> 📎 来源 / Source: https://www.v2ex.com/t/1081704#reply72

#### 44. [V2EX] 真心求教 Debian 双网卡如何指定出入站

**故障现象**: [V2EX] 真心求教 Debian 双网卡如何指定出入站
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
Debian12 双网卡 有各自网段和网关
如何指定 A 网卡入站 B 网卡出站呢
A 网卡有公网 ip 可以联通 B 网卡没有公网 ip
试了路由表还是搞不定 希望大佬指点

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1074397#reply16

> 📎 来源 / Source: https://www.v2ex.com/t/1074397#reply16

#### 45. [V2EX] 现在的 gnome 这么难用了吗

**故障现象**: [V2EX] 现在的 gnome 这么难用了吗
**标签 / 来源**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**问题描述**:
许久没用桌面了，昨天看有人炫耀 Ubuntu 22.04 的桌面，个人现在偏爱 Debian ，就用虚拟机下载安装了 Debian 12.5 ，桌面选的 gnome 。
进入桌面后显示了两个工作区，点击后直接全屏，然后要打开应用就要点击左上角活动-再点击屏幕下方启动台-再点击想要的应用，这操作链路也太长了吧。切换应用也是，点击左上角-再点已经打开的应用。
然后貌似多窗口不见了？我新建一个窗口但是不知道咋切换，各种操作都找出不来。
是现在流行这个我跟不上时代了吗，还是有啥新姿势，比如手势、快捷键我没掌握？

**解决方法 / 社区答案**:
See V2EX thread for community solutions.

**参考链接**: https://www.v2ex.com/t/1033871#reply7

> 📎 来源 / Source: https://www.v2ex.com/t/1033871#reply7

#### 46. How do I make `ls` show file sizes in megabytes?

**故障现象**: How do I make `ls` show file sizes in megabytes?
**标签 / 来源**: Tags: linux, ls | unix | StackExchange | 👍 936 | 💬 2 answers

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

#### 47. Finding the PID of the process using a specific port?

**故障现象**: Finding the PID of the process using a specific port?
**标签 / 来源**: Tags: linux, process, ip, netstat | unix | StackExchange | 👍 831 | 💬 8 answers

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

#### 48. Why am I still getting a password prompt with ssh with public key authentication?

**故障现象**: Why am I still getting a password prompt with ssh with public key authentication?
**标签 / 来源**: Tags: ubuntu, centos, ssh, sshd, key-authentication | unix | StackExchange | 👍 745 | 💬 32 answers

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

#### 49. How can I resolve a hostname to an IP address in a Bash script?

**故障现象**: How can I resolve a hostname to an IP address in a Bash script?
**标签 / 来源**: Tags: linux, bash, networking, dns | unix | StackExchange | 👍 635 | 💬 29 answers

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

#### 50. Execute vs Read bit. How do directory permissions in Linux work?

**故障现象**: Execute vs Read bit. How do directory permissions in Linux work?
**标签 / 来源**: Tags: linux, permissions, directory | unix | StackExchange | 👍 536 | 💬 9 answers

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


---

## English 🇺🇸
**Linux Common Issues & Solutions**

Auto-updated every 6 hours from Stack Exchange, Reddit, V2EX: common LINUX issues and community-verified solutions.

### LINUX Common Issues & Solutions

#### 1. [V2EX] Gnome 桌面下截图上传到 imgur 的 extension

**Issue**: [V2EX] Gnome 桌面下截图上传到 imgur 的 extension
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
Gnome50/Debian13 上测试通过的特别方便 V2EX 上发图片，就像我现在这样     https://github.com/wuruxu/gnome-shell-extension-imgur

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1207063#reply3

> 📎 Source: https://www.v2ex.com/t/1207063#reply3

#### 2. [V2EX] Manjaro 真不错

**Issue**: [V2EX] Manjaro 真不错
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
本来打算直接 ubuntu 的，但这个时间节点有点尴尬，26.04LTS 快发又还没发。试了下 Manjaro ，几乎开箱即用了~linux 没有微信语音输入有点难受 = =

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1207001#reply32

> 📎 Source: https://www.v2ex.com/t/1207001#reply32

#### 3. [V2EX] 写了个 lottie 动画在 Linux 桌面上顶层播放的小东西

**Issue**: [V2EX] 写了个 lottie 动画在 Linux 桌面上顶层播放的小东西
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
写了个 lottie 动画在 linux 桌面上顶层播放的小东西，可以用在和 codex/claude 回复结束后，播放一个小动画提示，没什么用的玩具
https://github.com/xxyangyoulin/linux-lottie-salute

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1206873#reply7

> 📎 Source: https://www.v2ex.com/t/1206873#reply7

#### 4. [V2EX] LXC veth 桥接网络模式下如何避免发送的数据包被拆成小包？

**Issue**: [V2EX] LXC veth 桥接网络模式下如何避免发送的数据包被拆成小包？
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
网卡是 rtl8127, 用 iperf3 测速，在 host 上测速可以达到 9.42 Gbits/sec ，在 lxc 里测速只有 3.25 Gbits/sec ，造成这么大差异的原因是在 lxc 里发送的数据包被拆成了 1.5KB 的小包（也就是 mtu 的大小），而在 host 上发送的数据包是几十 KB 的大包，我想知道如何让 lxc 里发送的数据包也是几十 KB 的大包，有 v 友对这个问题感兴趣愿意一起研究一下吗？
在 host 上运行 iperf3 发包时 sar 的输出如下：
d@develop:~/test$ sar -n DEV 1 | awk '/IFACE/ &amp

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1206865#reply13

> 📎 Source: https://www.v2ex.com/t/1206865#reply13

#### 5. [V2EX] 使用 auto-cpufreq 平衡 Linux 性能功耗

**Issue**: [V2EX] 使用 auto-cpufreq 平衡 Linux 性能功耗
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
在 Fedora Linux 下，调整系统使用 auto-cpufreq 速度和功耗优化器。

搭载 Intel Core Ultra 7 255H 处理器的设备，离电状态进行日常网页浏览、写作和听音乐等轻度任务时的功耗表现，基本维持在 10W 左右。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1206814#reply3

> 📎 Source: https://www.v2ex.com/t/1206814#reply3

#### 6. [V2EX] 我的硬盘 Memblaze Pblaze 5 Linux 下不识别，给 Linux 内核提交了补丁， AI 说有望被合并

**Issue**: [V2EX] 我的硬盘 Memblaze Pblaze 5 Linux 下不识别，给 Linux 内核提交了补丁， AI 说有望被合并
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
几年前在咸鱼上淘到几块国产硬盘，型号是 Memblaze Pblaze 516
Windows 下使用没有问题，但是在折腾 PVE 的时候遇到了问题，压根不识别这块硬盘。
然后我又试了好几个 Linux 发行版，某些旧内核版本反而能识别，
我根据 dmesg 信息和 pci 信息搜索，发现 bugzilla 上有类似的案例，
Bug 205679 - not able to recognize NVME's partition
https://bugzilla.kernel.org/show_bug.cgi?id=205679
我通过里面讨论的信息，自己写了个补丁（其实就加了 2 行设备信息）

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1206374#reply4

> 📎 Source: https://www.v2ex.com/t/1206374#reply4

#### 7. [V2EX] Linux nfs 客户端如何快速删除大量小文件

**Issue**: [V2EX] Linux nfs 客户端如何快速删除大量小文件
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
linux 下有个程序每天在 NFS 共享目录（生成一个当天日期的文件夹）下缓存 100 万左右的文件，大小差不多 3-5T ，这个程序处理完成后可以删除，如何在 Linux 下快速删除它们呢。
按照网上的这个同步空目录的方法，差不多耗时 7 个小时。
rsync --delete-before -d -H -O --progress /tmp/empty/ 2026-04-02/

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1206234#reply21

> 📎 Source: https://www.v2ex.com/t/1206234#reply21

#### 8. [V2EX] 写了个 Nautilus Extension: Copy File Path

**Issue**: [V2EX] 写了个 Nautilus Extension: Copy File Path
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
Gnome50/Debian 环境中测试通过的，方便我在 Nautilus 文件管理器中复制路径      AI 时代，软件可以按个人定制      https://github.com/wuruxu/nautilus-copypath

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1205636#reply0

> 📎 Source: https://www.v2ex.com/t/1205636#reply0

#### 9. [V2EX] Linux /Ubuntu 上如何实现连接两个不同的 wifi 解决实际需求。

**Issue**: [V2EX] Linux /Ubuntu 上如何实现连接两个不同的 wifi 解决实际需求。
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
背景：

自用电脑是联想小新 pro 14 ，装有 ubuntu24.04, 支持 wifi6
公司有 wifi A 和 wifi B ，wifi A 是国内的普通宽带，wifi B 是连接香港的专线。
服务器 ssh 连接限定了必须是使用 wifi A 
wifi B 由于是香港专线，可以自由访问谷歌等网站，无需翻墙。 使用 wifi A 则需要借助 Clash(虽然公司有订阅套餐)

目前我的需求是

指定某些软件/程序，例如是 teams,ssh 等使用 wifi A; 指定浏览器使用 Wifi A/B 

求助大佬们，我应该如何实现上述需求？是否需要增购 USB wifi ？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1204573#reply8

> 📎 Source: https://www.v2ex.com/t/1204573#reply8

#### 10. [V2EX] 115 网盘如何多端稳定挂载？

**Issue**: [V2EX] 115 网盘如何多端稳定挂载？
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
修复了存储状态不一致的问题，加强了稳定性
更新了安全提示



115 网盘的挂载功能存在一个严重限制：当你有两个 VPS 想挂载同一个 115 网盘账号时，你会发现：一边刚挂载成功，另一边就被踢下线。
这种报错，本质上是 115 网盘的防盗机制：当刷新 token 的时候会导致此应用获取的旧 token 失效。对于同一 app 的不同挂载，同样成立。 


如果没有防盗链：当有人窃取了你的 refreshtoken 之后，黑客就可以获取你的数据长达一年（除非你手动去吊销你的 token ，并重新获取） 这种方式诚然会提高安全性，但是在多端挂载的场景下反而成为了使用的阻碍。 

因此我搓了一个

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1203862#reply3

> 📎 Source: https://www.v2ex.com/t/1203862#reply3

#### 11. [V2EX] Linux 桌面环境 orWM 推荐

**Issue**: [V2EX] Linux 桌面环境 orWM 推荐
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
RT ，当前在用 kde plasma ，但是感觉设置项太多，我也不喜欢 QT ，想换一下
主要是想有鼠标时可以鼠标操作，出差时使用触控板进行操作，似乎 gnome 不错，但是不知道现在还稳定不，几年前用的时候动不动插件就用不了了....当然，我也只用一些基础插件。
有人用 hyprland 吗？操作体验怎么样，桌面似乎是不能显示文件吗？鼠标和触控板操作不知道怎么样，有没有老哥解答一下，我的机器是 thinkbook 14+ 2024 ultra7 版本

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1203303#reply46

> 📎 Source: https://www.v2ex.com/t/1203303#reply46

#### 12. [V2EX] 如何解决 eBPF sockmap 重定向转发中背压缺失带来的 OOM ？

**Issue**: [V2EX] 如何解决 eBPF sockmap 重定向转发中背压缺失带来的 OOM ？
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
我在尝试使用 eBPF 的 BPF_PROG_TYPE_SK_SKB 与 BPF_MAP_TYPE_SOCKHASH 实现 socket 的铰接转发，目标是基于 bpf_sk_redirect_hash 将一个 socket 的 ingress 队列数据转发到另一个 socket 的 egress 队列，但是在实际的吞吐量测试时出现了系统 OOM 。
具体的环境如下：

Linux Kernel 6.8
2 个 socket 所处网络接口不同，且 2 个网络接口带宽不一致，转发源 socket 所处接口 (测试用的 loopback) 带宽高于目标 socket 所处带宽
吞吐测试是在 loo

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1202372#reply11

> 📎 Source: https://www.v2ex.com/t/1202372#reply11

#### 13. [V2EX] 还是要用 ubuntu

**Issue**: [V2EX] 还是要用 ubuntu
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
过去一直用 windows 开发，编码问题，行尾问题，使用 docker 绑定目录也会有同步问题。


后来就转到 wsl 中开发，但是不好说是 wsl 的 bug 还是 docker 的 bug ，经常出现磁盘读写 100%，
磁盘完全占满后所有 app 都不能正常工作了。


然后就转 linux ，选的三个 mint ，debian/kde ，ubuntu
先用 live 模式尝试，ubuntu 出现了一点卡顿就放弃了，尝试 mint 发现官方网站上列了很多已知问题，
我不敢用，debian 暂时没有发现问题，就安装了，用了之后才发现这个 debian 反而经常出现 freeze 的情况

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1201875#reply53

> 📎 Source: https://www.v2ex.com/t/1201875#reply53

#### 14. [V2EX] nfs mv 的操作是原子的么？ A 节点 move， B 节点要么完全可见，要么完全不可见？

**Issue**: [V2EX] nfs mv 的操作是原子的么？ A 节点 move， B 节点要么完全可见，要么完全不可见？
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
比如机器 A 、B 的/data 挂载了同一个 nfs 挂载点，A 机器/data 目录下有一个文件夹 a 下有 10000 个文件，我把/data/a 移动到/data/b ，对于机器 B 而言，如果节点 A 上已经看到 move 完成了，那么节点 B 上由于 nfs 异步延迟的存储，可能前几秒看不到这个移动的操作，过几秒之后可以看到/data/a 变成了/data/b ，那么存不存在一个中间状态，我能看到/data/b ，但是/data/b 下只有比如 2000 个文件

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1200802#reply1

> 📎 Source: https://www.v2ex.com/t/1200802#reply1

#### 15. [V2EX] 求助 Linux 桌面环境软件

**Issue**: [V2EX] 求助 Linux 桌面环境软件
**Tags / Source**: Tags: linux | v2ex-linux | V2EX | 👍 0 | 💬 0 answers

**Description**:
马上要转过去了。麒麟信安 kylinSEC OS   arm ，看了下好像是类红帽的，rpm 包。昨晚翻吐了没找到几个软件。有经验的前辈推荐些常用软件吧。目前有 idea 、redis 、dbeaver ，没找到离线翻译的，有道官网没 arm 版。另外现在 idea 还能离线 2099 吗，好久没折腾了。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1200587#reply21

> 📎 Source: https://www.v2ex.com/t/1200587#reply21

#### 16. [V2EX] ubuntu 上有没有基于 OpenGL 的原生 3d 游戏

**Issue**: [V2EX] ubuntu 上有没有基于 OpenGL 的原生 3d 游戏
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
记得很多年前玩过一款，通过 .deb 安装的，3D 飞行躲避障碍的，想在想不起来名字了。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1188348#reply2

> 📎 Source: https://www.v2ex.com/t/1188348#reply2

#### 17. [V2EX] ubuntu 下的风扇转速控制？

**Issue**: [V2EX] ubuntu 下的风扇转速控制？
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
家里的电脑装的 pc 用的水冷。
在 win 下面，因为装了厂商的驱动，貌似正常办公的时候，风扇转速很低，没有声音。但是 ubuntu 下面，貌似已启动就是高速。。。不知道各位佬们在 ubuntu 下面可以怎样也控制下显卡和水冷风扇的转速嘛？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1187869#reply5

> 📎 Source: https://www.v2ex.com/t/1187869#reply5

#### 18. [V2EX] 求推荐 Ubuntu 好用的 ssh 工具

**Issue**: [V2EX] 求推荐 Ubuntu 好用的 ssh 工具
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:


**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1177713#reply53

> 📎 Source: https://www.v2ex.com/t/1177713#reply53

#### 19. [V2EX] ubuntu 26.04 有人体验了吗, 有国内的可用镜像吗

**Issue**: [V2EX] ubuntu 26.04 有人体验了吗, 有国内的可用镜像吗
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:


**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1171076#reply6

> 📎 Source: https://www.v2ex.com/t/1171076#reply6

#### 20. [V2EX] 15 年前的 ubuntu 官方安装盘有人要么

**Issue**: [V2EX] 15 年前的 ubuntu 官方安装盘有人要么
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
[有图有真相]( https://aifeixiang.feishu.cn/wiki/C6IcwFfMnirMX7kpz33cUASknDc)9.10 ，10.04, 10.10  整理书柜找到的，保存完好。 大学的时候申请的，没人要就扔掉了。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1150108#reply11

> 📎 Source: https://www.v2ex.com/t/1150108#reply11

#### 21. [V2EX] 该装服务器了，装 Ubuntu24.04.2 还是 Ubuntu22.04.5

**Issue**: [V2EX] 该装服务器了，装 Ubuntu24.04.2 还是 Ubuntu22.04.5
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
预计要用个四五年，预计部署网站和 MCP 服务端，用最新的 24.04.2 还是上个稳定版本 22.04.5 ？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1144421#reply95

> 📎 Source: https://www.v2ex.com/t/1144421#reply95

#### 22. [V2EX] ubuntu 加显卡后感觉动画卡顿

**Issue**: [V2EX] ubuntu 加显卡后感觉动画卡顿
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
升级之前使用 GTX 950 2G


升级成 GTX 950 2G + 4060TI16G 


xorg 配置系统使用 950 ，4060 留作炼丹


按 win 键时 950 负载很高，动画卡顿，加之前没有这个感觉


为啥不用 Wayland, vscode 在 wayland 下使用感受很差


vscode gpu 加速已经送了，不然显存要炸


求大佬解惑

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1138312#reply7

> 📎 Source: https://www.v2ex.com/t/1138312#reply7

#### 23. [V2EX] vmware17 安装 ubuntu22.04.5，最后一步报错

**Issue**: [V2EX] vmware17 安装 ubuntu22.04.5，最后一步报错
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
我的硬件是 e5-2697v4 双路，请问如何解决？具体情况，如图：

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1126019#reply23

> 📎 Source: https://www.v2ex.com/t/1126019#reply23

#### 24. [V2EX] 求 Ubuntu 台式机指纹 USB 识别器推荐

**Issue**: [V2EX] 求 Ubuntu 台式机指纹 USB 识别器推荐
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
最近使用 Ubuntu 22.04 台式机作为主力机，需要一个指纹 USB 识别器，主要用于指纹登录和 sudo 密码验证。之前咸鱼过一个 Kensington VeriMark Desktop Fingerprint Key ，发现 libfprint 不支持，请问大佬们有推荐的吗？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1117952#reply8

> 📎 Source: https://www.v2ex.com/t/1117952#reply8

#### 25. [V2EX] ubuntun 下 docker 拉取镜像失败，配置了镜像源，但是无效

**Issue**: [V2EX] ubuntun 下 docker 拉取镜像失败，配置了镜像源，但是无效
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
已在 daemon.json 配置了多个镜像源：
DaoCloud 镜像站： https://docker.m.daocloud.io
腾讯云公共镜像库： https://mirror.ccs.tencentyun.com
华为云镜像服务： https://developer.huaweicloud.com/dm/mirrors
1Panel 镜像源： https://docker.1panel.live
Unsee 镜像源： https://docker-0.unsee.tech
1ms.run 镜像源： https://docker.1ms.run
Azure 中国镜像： http://m

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1112655#reply23

> 📎 Source: https://www.v2ex.com/t/1112655#reply23

#### 26. [V2EX] 我的 ubantu 服务器是不是被人植入了恶意代码了

**Issue**: [V2EX] 我的 ubantu 服务器是不是被人植入了恶意代码了
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
我的 ubantu 服务器是不是被人植入了恶意代码。。。。
我上面只跑了我的博客，都是 nodejs ，nginx ，mysql 和 Let's Encrypt 证书管理，没有跑过其他服务。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1107484#reply24

> 📎 Source: https://www.v2ex.com/t/1107484#reply24

#### 27. [V2EX] ubuntu 用 vbetool dpms off 了再 on 后，显示乱码

**Issue**: [V2EX] ubuntu 用 vbetool dpms off 了再 on 后，显示乱码
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:


**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1106291#reply2

> 📎 Source: https://www.v2ex.com/t/1106291#reply2

#### 28. [V2EX] WIN11 访问 UBUNTU 的 webdav 记不住账号

**Issue**: [V2EX] WIN11 访问 UBUNTU 的 webdav 记不住账号
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
我之前由于/目录所有者换成了用户，没办法只好重装了电脑，安装的还是 UBUNTU24
开了 webdav 共享，在 WIN11 上面用映射的方式访问。
但是每次访问，默认登录的用户名都是微软账号，无论我怎么选择保存，都是这样，好像跟我登录 windows 的账号一样，可我在 webdav 上设置了用户名和密码。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1100930#reply1

> 📎 Source: https://www.v2ex.com/t/1100930#reply1

#### 29. [V2EX] Linux 安装完系统后默认是安装好显卡驱动吗？

**Issue**: [V2EX] Linux 安装完系统后默认是安装好显卡驱动吗？
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
以前安装 WINDOWS 系统后，开机第一件事是安装各种驱动，包括最重要的显卡驱动使用过 linux ，发现安装完系统后好像都是各种 sudo apt update,貌似都不需要安装各类驱动的说法，今天打开 AMD 的官网，才发现 AMD 官网就有提供显卡驱动，用 LINUX 这么久了，貌似以前就没有主动安装显卡驱动，安装完 LINUX 后都是开箱即用，几条命令更新后就开始使用了，汗。所以想问下，linux 全新安装完系统后不需要安装各类驱动吗，包括显卡驱动。最近用 Ubuntu ，发现文件夹经常会卡住没反应，是没安装驱动的锅吗

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1097632#reply14

> 📎 Source: https://www.v2ex.com/t/1097632#reply14

#### 30. [V2EX] 闯了大祸,根目录权限变成我自己了。

**Issue**: [V2EX] 闯了大祸,根目录权限变成我自己了。
**Tags / Source**: Tags: ubuntu | v2ex-ubuntu | V2EX | 👍 0 | 💬 0 answers

**Description**:
我的磁盘空间不够了，之前分区的时候没搞好，根目录给了 1.7T 一直闲置，为了下载一个 700 多 G 的文件，我简单的 mount 到了一个下载目录下，transmission 下载的时候报错说权限问题，我直接 chown -R uuair:www-data 了，我还纳闷，一个空目录，怎么会卡住了。。。结果 sudo 的时候发现错误，然后，./目录下大部分文件都不是 root 的了，尤其是/etc 下，所有的都是我了。
好了，现在怎么办？  
第一：/home文件夹下有 3.2T 的文件，我没有其他的硬盘可以备份。
第二：我运行了 12 个 docker ，其中有几个配置了很久，可能我自己都

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1095187#reply50

> 📎 Source: https://www.v2ex.com/t/1095187#reply50

#### 31. [V2EX] 各大镜像站不再提供 Debian12 下载？

**Issue**: [V2EX] 各大镜像站不再提供 Debian12 下载？
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
今天很多国内镜像站（清华 中科大等）的 Debian 12 ISO 下载链接变成了 404 （例如 debian-cd 目录下的 12.x ISO ）。
据说是因为 Debian 13 今天正式成为 stable 
是不是我搞错了？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1198396#reply2

> 📎 Source: https://www.v2ex.com/t/1198396#reply2

#### 32. [V2EX] Debian 26 届年会现在可以开始报名注册啦！

**Issue**: [V2EX] Debian 26 届年会现在可以开始报名注册啦！
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
大家好！
Debian 26 届年会现在可以开始报名注册啦！
https://debconf26.debconf.org/
这次年会在 阿根廷 的 圣达菲（ Santa Fe ） 举行。
（一）飞机
目前国内上海有到阿根廷首都布宜诺斯艾利斯的直飞航班（机场代码：EZE ），经停 新西兰 的 奥克兰。
全程 25 个多小时，全国联运。
去程（上海→布宜诺斯艾利斯）：MU745 ，每周一、周四执行，北京时间 02:00 从上海浦东机场起飞，当地时间 16:55 抵达。‌‌
回程（布宜诺斯艾利斯→上海）：MU746 ，每周二、周五执行，当地时间 02:00 起飞，北京时间次日 18:00 抵达。‌‌

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1192842#reply0

> 📎 Source: https://www.v2ex.com/t/1192842#reply0

#### 33. [V2EX] debian13 有必要升级吗？感觉 12 还能坚持好几年

**Issue**: [V2EX] debian13 有必要升级吗？感觉 12 还能坚持好几年
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:


**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1190787#reply3

> 📎 Source: https://www.v2ex.com/t/1190787#reply3

#### 34. [V2EX] Debian 龙芯 移植进度

**Issue**: [V2EX] Debian 龙芯 移植进度
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
base-files_14_loong64.changes ACCEPTED into unstable Debian FTP Masters
dpkg_1.22.21_loong64.changes ACCEPTED into unstable Debian FTP Masters
make-dfsg_4.4.1-3_loong64.changes ACCEPTED into unstable Debian FTP Masters
binutils_2.45.50.20251209-1_loong64.changes ACCEPTED into unstable Debian FTP Mas

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1178918#reply3

> 📎 Source: https://www.v2ex.com/t/1178918#reply3

#### 35. [V2EX] Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁

**Issue**: [V2EX] Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
Debian 13 root on ZFS 解决方案，支持根分区加密、压缩和远程解锁
https://www.reddit.com/r/zfs/comments/1oivqx1/debian_13_root_on_zfs_with_native_encryption_and/

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1169507#reply0

> 📎 Source: https://www.v2ex.com/t/1169507#reply0

#### 36. [V2EX] 香橙派 5Plus 小服务器已升级 Debian13

**Issue**: [V2EX] 香橙派 5Plus 小服务器已升级 Debian13
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
香橙派 5Plus RK3588 16G ，作家庭服务器用的，内核是 6.1.43-rockchip-rk3588 。已升级 Debian13 ，先用着了，看看有没有问题。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1151947#reply4

> 📎 Source: https://www.v2ex.com/t/1151947#reply4

#### 37. [V2EX] Debian 13 “trixie” released

**Issue**: [V2EX] Debian 13 “trixie” released
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
https://www.debian.org/News/2025/20250809
正式新闻终于出了

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1151300#reply4

> 📎 Source: https://www.v2ex.com/t/1151300#reply4

#### 38. [V2EX] 安装 debian 的时候如何跳过创建普通用户？

**Issue**: [V2EX] 安装 debian 的时候如何跳过创建普通用户？
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:


**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1141239#reply5

> 📎 Source: https://www.v2ex.com/t/1141239#reply5

#### 39. [V2EX] debian 12 的体验真的很糟糕

**Issue**: [V2EX] debian 12 的体验真的很糟糕
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
各种小问题最让人受不了的是 ibus 输入法。无论我是清除本地数据文件，还是 remove 再 reinstall ，都解决不了这只是我的个案吗？看起来 debian 13 也快来了不然我都想切换到 fedora

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1119550#reply14

> 📎 Source: https://www.v2ex.com/t/1119550#reply14

#### 40. [V2EX] debian12.8 的 preseed 自动安装方式，封装 iso 的正确方式？?

**Issue**: [V2EX] debian12.8 的 preseed 自动安装方式，封装 iso 的正确方式？?
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
先做了这些事情(debian-12.8.0-amd64-DVD-1.iso 是官网下载的)
apt install debian-cd isolinux genisoimage
mount -o loop /opt/mkiso/debian-12.8.0-amd64-DVD-1.iso /mnt
mkdir /opt/debian_custom
cp -r /mnt/* /opt/debian_custom/
cp /opt/preseed.cfg /opt/debian_custom/preseed.cfg
chmod +w /opt/debian_custom/isolinux/txt.c

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1102156#reply0

> 📎 Source: https://www.v2ex.com/t/1102156#reply0

#### 41. [V2EX] Debian12 VNC 连接时怎么才能以 Root 的身份登录桌面环境

**Issue**: [V2EX] Debian12 VNC 连接时怎么才能以 Root 的身份登录桌面环境
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
已具备条件：
桌面环境已具备
Root 可以通过桌面环境正常登录
普通用户已经具备 sudo
防火墙没有开启
vncserver 搭建成功了，且普通用户能正常登录桌面环境，但是为普通用户身份
希望达成的目标：
以 vnc 的方式连接上 debian 后，能切换至 root 身份进行可视化操作（非终端命令切换）

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1093953#reply2

> 📎 Source: https://www.v2ex.com/t/1093953#reply2

#### 42. [V2EX] 我成功申请成为 Debian 正式成员， id 是 atzlinux

**Issue**: [V2EX] 我成功申请成为 Debian 正式成员， id 是 atzlinux
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
在中国大陆这边，目前还不到 10 个人。比印度少哈，目前 印度有 16 ，17 个吧。

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1085701#reply6

> 📎 Source: https://www.v2ex.com/t/1085701#reply6

#### 43. [V2EX] Debian 这个系统你们一般怎么读？

**Issue**: [V2EX] Debian 这个系统你们一般怎么读？
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
我一般读：德编
有的人读：呆边
还听说有人就说大便系统。（戏谑说法）
今天听到有个人读：得（ dei3 ）变

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1081704#reply72

> 📎 Source: https://www.v2ex.com/t/1081704#reply72

#### 44. [V2EX] 真心求教 Debian 双网卡如何指定出入站

**Issue**: [V2EX] 真心求教 Debian 双网卡如何指定出入站
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
Debian12 双网卡 有各自网段和网关
如何指定 A 网卡入站 B 网卡出站呢
A 网卡有公网 ip 可以联通 B 网卡没有公网 ip
试了路由表还是搞不定 希望大佬指点

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1074397#reply16

> 📎 Source: https://www.v2ex.com/t/1074397#reply16

#### 45. [V2EX] 现在的 gnome 这么难用了吗

**Issue**: [V2EX] 现在的 gnome 这么难用了吗
**Tags / Source**: Tags: debian | v2ex-debian | V2EX | 👍 0 | 💬 0 answers

**Description**:
许久没用桌面了，昨天看有人炫耀 Ubuntu 22.04 的桌面，个人现在偏爱 Debian ，就用虚拟机下载安装了 Debian 12.5 ，桌面选的 gnome 。
进入桌面后显示了两个工作区，点击后直接全屏，然后要打开应用就要点击左上角活动-再点击屏幕下方启动台-再点击想要的应用，这操作链路也太长了吧。切换应用也是，点击左上角-再点已经打开的应用。
然后貌似多窗口不见了？我新建一个窗口但是不知道咋切换，各种操作都找出不来。
是现在流行这个我跟不上时代了吗，还是有啥新姿势，比如手势、快捷键我没掌握？

**Solution / Community Answer**:
See V2EX thread for community solutions.

**Reference**: https://www.v2ex.com/t/1033871#reply7

> 📎 Source: https://www.v2ex.com/t/1033871#reply7

#### 46. How do I make `ls` show file sizes in megabytes?

**Issue**: How do I make `ls` show file sizes in megabytes?
**Tags / Source**: Tags: linux, ls | unix | StackExchange | 👍 936 | 💬 2 answers

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

#### 47. Finding the PID of the process using a specific port?

**Issue**: Finding the PID of the process using a specific port?
**Tags / Source**: Tags: linux, process, ip, netstat | unix | StackExchange | 👍 831 | 💬 8 answers

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

#### 48. Why am I still getting a password prompt with ssh with public key authentication?

**Issue**: Why am I still getting a password prompt with ssh with public key authentication?
**Tags / Source**: Tags: ubuntu, centos, ssh, sshd, key-authentication | unix | StackExchange | 👍 745 | 💬 32 answers

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

#### 49. How can I resolve a hostname to an IP address in a Bash script?

**Issue**: How can I resolve a hostname to an IP address in a Bash script?
**Tags / Source**: Tags: linux, bash, networking, dns | unix | StackExchange | 👍 635 | 💬 29 answers

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

#### 50. Execute vs Read bit. How do directory permissions in Linux work?

**Issue**: Execute vs Read bit. How do directory permissions in Linux work?
**Tags / Source**: Tags: linux, permissions, directory | unix | StackExchange | 👍 536 | 💬 9 answers

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



---

**🔗 导航 / Navigation**

- [返回目录 / Back to Index](index.md)
