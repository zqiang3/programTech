## smembers

当 KEYS 命令被用于处理一个大的数据库时， 又或者 SMEMBERS 命令被用于处理一个大的集合键时， 它们可能会阻塞服务器达数秒之久。

## hgetall

时间复杂度为O(n)。

## slowlog

edis的slowlog是redis用于记录记录慢查询执行时间的日志系统。由于slowlog只保存在内存中，因此slowlog的效率很高，完全不用担心会影响到redis的性能。

在redis.conf中有关于slowlog的设置：

```bash
# 单位microseconds, 10000表示10ms(millisecond)
slowlog-log-slower-than 10000  
slowlog-max-len 128
```

其中slowlog-log-slower-than表示slowlog的划定界限，只有query执行时间大于slowlog-log-slower-than的才会定义成慢查询，才会被slowlog进行记录。slowlog-log-slower-than设置的单位是微妙，默认是10000微妙，也就是10ms 
slowlog-max-len表示慢查询最大的条数，当slowlog超过设定的最大值后，会将最早的slowlog删除，是个FIFO队列

```bash
slowlog len
slowlog reset                 # 清空慢查询日志
SLOWLOG GET
# 获取指定的条数
SLOWLOG GET N
1) (integer) 26               # slowlog 编号
2) (integer) 1440057815       # 时间戳
3）(integer) 47               # 耗时（微秒）
4）1）"SLOWLOG"                # 查询命令
   2) "GET"
```

