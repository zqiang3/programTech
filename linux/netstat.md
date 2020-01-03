## link

https://linux.cn/article-2434-1.html





```bash


-p,
	Show the PID and name of the program to which each socket belongs.
-l,
	Show only listening sockets.
-a,

-t 仅显示tcp相关选项
-n 能显示数字的全部转化成数字
```

### 实例

```bash
netstat -a
netstat -at
netstat -au
netstat -l
netstat -lt
netstat -lu
netstat -lx  # 只列出所有监听 UNIX 端口
netstat -s  # 显示所有端口的统计信息
netstat -st 或 -su
netstat -p  在 netstat 输出中显示 PID 和进程名称
netstat -p 可以与其它开关一起使用，就可以添加 “PID/进程名称” 到 netstat 输出中
netstat -n 当你不想让主机，端口和用户名显示，使用 netstat -n。将会使用数字代替那些名称
如果只是不想让这三个名称中的一个被显示，使用以下命令
# netsat -a --numeric-ports
# netsat -a --numeric-hosts
# netsat -a --numeric-users

netstat -c  # 持续输出netstat信息
netstat -r  # 显示核心路由信息
netstat -ap | grep ssh
```

## 安装

```bash
apt-get install net-tools
```

## 详细说明

默认情况下 netstat 会通过反向域名解析技术查找每个 IP 地址对应的主机名。这会降低查找速度。如果你觉得 IP 地址已经足够，而没有必要知道主机名，就使用 **-n** 选项禁用域名解析功能。

```bash
$ netstat -ant
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.1.1:53            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN     
tcp        0      0 192.168.1.2:49058       173.255.230.5:80        ESTABLISHED
tcp        0      0 192.168.1.2:33324       173.194.36.117:443      ESTABLISHED
tcp6       0      0 ::1:631                 :::*                    LISTEN
```

