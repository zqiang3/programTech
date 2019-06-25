```redis
redis-cli monitor > out.log
```

MONITOR是一个调试命令，可把redis处理的每个命令打印出来，帮助我们了解数据库在发生什么。



## 统计频率最高的命令

```bash
cut -d " " -f 4,5 cc_ap_mobile8.log > result.log
grep GET result.log > get.log
grep SET result.log > set.log

cut -d " " -f 2 set.log > set2.log
cut -d '"' -f 2 set2.log > set3.log

cut -d " " -f 2 get.log > get2.log
cut -d '"' -f 2 get2.log > get3.log
```

