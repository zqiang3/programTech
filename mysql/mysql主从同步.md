## Link

https://blog.csdn.net/helloxiaozhe/article/details/79548186?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase



## 1、什么是mysql主从同步？

当master(主)库的数据发生变化的时候，变化会实时的同步到slave(从)库。

------

## 2、主从同步有什么好处？

- 水平扩展数据库的负载能力。
- 容错，高可用。Failover(失败切换)/High Availability
- 数据备份。

## 3、主从同步原理

slave连接到master时，开启binlog dump线程

开启主从同步时，从机开启两个线程，io线程从主节点接收binlog日志，写到relaylog；sql线程读取relaylog，在从库上做数据更改。