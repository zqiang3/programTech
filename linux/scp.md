

## scp命令

**scp命令**用于在Linux下进行远程拷贝文件的命令，和它类似的命令有[cp](http://man.linuxde.net/cp)，不过cp只是在本机进行拷贝不能跨服务器，而且scp传输是加密的。可能会稍微影响一下速度。当你服务器硬盘变为只读[read](http://man.linuxde.net/read) only system时，用scp可以帮你把文件移出来。另外，scp还非常不占资源，不会提高多少系统负荷，在这一点上，[rsync](http://man.linuxde.net/rsync)就远远不及它了。虽然 rsync比scp会快一点，但当小文件众多的情况下，rsync会导致硬盘I/O非常高，而scp基本不影响系统正常使用。



## 语法

```bash
scp(选项)(参数)
```



## 选项

```bash
-1：使用ssh协议版本1；
-2：使用ssh协议版本2；
-4：使用ipv4；
-6：使用ipv6；
-B：以批处理模式运行；
-C：使用压缩；
-F：指定ssh配置文件；
-l：指定宽带限制；
-o：指定使用的ssh选项；
-P：指定远程主机的端口号；
-p：保留文件的最后修改时间，最后访问时间和权限模式；
-q：不显示复制进度；
-r：以递归方式复制。

```





## 参数

- 源文件：指定要复制的源文件。
- 目标文件：目标文件。格式为`user@host：filename`（文件名为目标文件的名称）。

从远程复制到本地的scp命令与上面的命令雷同，只要将从本地复制到远程的命令后面2个参数互换顺序就行了。

## Usage

### 把远程的文件复制到本地

```bash
scp root@www.test.com:/val/test/test.tar.gz /val/test/test.tar.gz
```

###把本地的文件复制到远程主机

```bash
scp /val/test.tar.gz root@www.test.com:/val/test.tar.gz
```

###把远程的目录复制到本地

```bash
scp -r root@www.test.com:/val/test/ /val/test/
```

###把本地的目录复制到远程主机上

```bash
scp -r ./ubuntu_env/ root@192.168.0.111:/home/pipi
```



