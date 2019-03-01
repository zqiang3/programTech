内核和任何程序都可通过syslog系统记录事件消息。
内核使用printk()功能将消息记录到内核空间中的环形缓冲区中。sys/klog.h提供了系统调用sys_syslog，它从内核的printk环形缓冲区读取消息。后台进程klogd调用sys_syslog读取内核的消息，并将其发送到syslogd守护程序。
在用户空间中有syslogd。这是一个监听许多UNIX域套接字的守护进程，并且可从UDP端口514接收消息。也可从klogd接收消息。然后将这些消息写入特定文件，或将其发送到一些远程主机。
syslog是一种RFC标准协议，其实现是平台无关的，syslogd是最传统的syslog协议服务器端的实现，由于其安全性差，语法太自由而导致了很多的问题。
rsyslog应该是目前最强大的syslog处理程序。支持输出日志到各种数据库，如 MySQL，PostgreSQL，MongoDB，ElasticSearch等；可以实现数据的可靠传输；精细的输出格式控制以及对消息的强大过滤能力；高精度时间戳；队列操作（内存，磁盘以及混合模式等）； 支持数据的加密和压缩传输等。

## 模块加载

模块相关的配置和功能仅在 相应的模块被加载（$ModLoad）后才可用。

```bash
imuxsock – UNIX socket
imudp    – 通过 UDP 接收日志
imfile   – 转换文本文件为日志
omfile   – 输出到文件
ommail   – 发送邮件
ommysql  – MySQL
```

## 规则部分

FACILITY 是生成日志的程序模块。取值范围为 auth，authpriv，cron， daemon，kern，lpr，mail，news，syslog，user，uucp，local0 到 local7。
PRIORITY 表示日志的级别，取值范围为（从低到高，数值对应 7-0） debug，info，notice，warning，err，crit，alert，emerg。在级别前可以增加相应的修饰符，例如加 = 表示仅选择该优先级的日志，加 ! 表示选择不等于优先级的所有日志，不加任何符号则表示选择该优先级及之上的日志。 * 可以用来表示所有的日志子系统和/或消息级别。关键字 none 表示未指定级别的日志（不记录）。如果要定义多个设置/优先级，使用 , 分隔即可。 如果要定义多个过滤条件，则使用 ; 分隔。 示例如下：
kern.* # 选择所有级别的内核日志
mail.crit # 选择所有级别为 crit 及之上的邮件系统相关日志
cron.!info,!debug # 选择所有 cron 日志信息，排除优先级为 info 和 debug 的日志
*.=debug # 选择所有的调试级别日志
*.*;auth,authpriv.none # 选择所有级别的日志，以及认证相关无级别的日志

*.info;mail.none;authpriv.none;cron.none 表示所有模块的info级别以上，mail，authpriv，cron不记录（他们有自己的记录日志），如果不写后面这几个级别为none的，他们的日志在写到指定文件的时候也会全部写到messages！

**动作**
保存日志到指定文件
例如：
cron.* -/var/log/cron.log
如果文件路径前有 “-” 则表示每次输出日志时不同步（sync，有缓冲区，不等待实际写磁盘）指定日志文件。 文件路径既可以是静态文件也可以是动态文件。动态文件由模板前加 ? 定义。
通过网络发送日志
格式如下：
@[()]:[]
@ 表示使用 UDP 协议。@@ 表示使用 TCP 协议。 可以为： z 表示使用 zlib 压缩，NUMBER 表示压缩级别。多个选项 使用 , 分隔。
例如：
*.* @192.168.0.1 # 使用 UDP 发送日志到 192.168.0.1
*.* @@example.com:18 # 使用 TCP 发送到 “example.com” 的 18 端口
*.* @(z9)[2001::1] # 使用 UDP 发送消息到 2001::1，启用 zlib 9 级压缩
发送消息到特定用户
例如
:msg,contains,”error” liuzx
发送包含 error 的日志到用户 liuzx。多个用户则用 , 分隔，* 表示所有用户。

更深一步，rsyslog的工作方式，队列原理，这部分暂时没懂

## 打开UDP支持

```bash
# Provides UDP syslog reception
$ModLoad imudp #打开udp模块
$UDPServerRun 514 #打开udp服务，并监听514端口
# Provides TCP syslog reception
$ModLoad imtcp #打开tcp模块
$InputTCPServerRun 514 #打开tcp服务，并监听514端口
```

