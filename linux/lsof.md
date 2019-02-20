## 命令说明

参考链接：https://linux.cn/article-4099-1.html

lsof(list open file) 是一个列出当前系统打开的文件描述符的工具，通过它我们可以了解哪些进程打开了哪些文件描述符。

对于我，lsof替代了netstat和ps的全部工作。它可以带来那些工具所能带来的一切，而且要比那些工具多得多。

当给lsof传递选项时，默认行为是对结果进行“或”运算。因此，如果你正是用-i来拉出一个端口列表，同时又用-p来拉出一个进程列表，那么默认情况下你会获得两者的结果。

有些人喜欢用netstat来获取网络连接，但是我更喜欢使用lsof来进行此项工作。

可打开的**文件类型**：

1. 普通文件
2. 目录
3. 网络文件系统的文件
4. 字符或设备文件
5. 函数共享库
6. 管道，命名管道
7. 符号连接
8. 网络文件（如：NFS file、网络socket，unix域名socket）
9. 其他类型的文件

**常用选项**：

-c <进程名>

-p <进程号>

-i <条件> 4、6、协议、端口、@ip



## 使用实例

```bash
lsof              # 如果不加任何参数，就会打开所有被打开的文件

lsof /path/file   # 查看谁在使用某个文件

lsof -u username  # 列出某个用户打开的文件信息

lsof -c nginx    

lsof -c nginx -c apache

lsof -p 1

lsof -p 1, 2, 3

lsof -d 2-3

lsof -i         # 列出所有网络连接

lsof -i 4       # 仅显示ipv6连接

lsof -i tcp     # 仅显示tcp连接

lsof -i :3306   # 显示与端口相关的网络信息

lsof -i udp:55

lsof -i tcp:80

lsof -i@172.16.12.5    # 显示与特定主机的连接
lsof -i@172.16.12.5:22
lsof -i | grep LISTEN       # 找出等待连接的端口
lsof -i | grep ESTABLISHED  # 找出等待连接的端口
```

