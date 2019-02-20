redis比memcache作为缓存数据库强大的地方，一个是支持的数据类型比较多，另一个就是redis持久化功能 



## 启动、停止、重启

```bash
/etc/init.d/redis-server stop
/etc/init.d/redis-server start
/etc/init.d/redis-server restart
redis-cli shutdown
kill -9 PID

```

## 查看端口

```bash
netstat -lntp | grep 6379
```



# RDB是什么

在指定的时间间隔内将内存中的数据集快照写入磁盘，也就是行话讲的Snapshot快照，它恢复时是将快照文件直接读到内存里，Redis会单独创建一个子进程（fork）来进行持久化，会先将数据写入到。这种是合用bgsave的方式。另一种是直接执行save，这个命令不需要创建子进程。

一个临时文件中，待持久化过程都结束了，再用这个临时文件替换上次持久化好的文件。整个过程中，主进程是不进行任何IO操作的，这就确保了极高的性能。如果需要进行大规模数据的恢复，且对于数据恢复的完整性不是非常敏感，那RDB方式要比AOF方式更加的高效。RDB的缺点是最后一次持久化后的数据可能丢失。

**save**: save时只管保存，其它不管，全部阻塞  

**bgsave**: Redis会在后台异步进行快照操作，快照同时还可以响应客户端请求。可以通过lastsave  命令获取最后一次成功执行快照的时间 