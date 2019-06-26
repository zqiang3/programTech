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

