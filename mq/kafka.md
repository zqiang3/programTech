## kafka如何保证消息有序



追加写、offset读



发往同一partition的消息保证有序

指定同一key的消息，会发住同一个partition





消费端不能并行消费，即不能多个客户端同1个partition，kafka一个partition只能由一个客户端线程消费，反过来没有限制，一个客户端可以消费多个partition

发送端不能并发异步发送，不然某条消息发送失败，就不能保证消息有序

存储端，不能分区，如果分区有多个队列，同一个topic的消息，会分散到多个分区里，自然不能保证顺序

即使只有1个队列，机器挂了，切换到其他机器时，也不能保证消息有序。要想保证，一方面要同步复制，不能异步复制；切机器时，挂掉的机器上，所有的消息必须消费完，不能有残留。



## 如何保证消息不丢失

生产端丢失：

发送消息之后回调函数，如果失败要有重发逻辑

producer一直等待缓冲区直至变为可用，生产过快耗尽缓冲区，抛出异常，缓冲区满就阻塞。

acks = all 同步给所有follower

使用回调函数处理发送失败



消息至少要写入多副本才算成功





消费者拉取到分区的某个消息后，自动提交offset。带来的问题是，自动提交后，可能没有被真正消费，进程突然挂掉，但消息没有被消费。

关闭自动提交，消费完后手动提交。这样同样有问题，会带来消息被重新消费的问题，消费完，但没提交offset，结果进程挂掉，消息可能被消费两次。

多副本，leader，follower 同步。

生产者和消费者只与leader进行交互。

leader挂掉，但follower没有同步数据，就会导致消息丢失。

保证不丢失，acks = all 所有副本都要同步

## kafka与rocketmq异同

每个topic的每个partition对应一个文件，顺序写入，定时刷盘。但partition过多会退化为随机写，性能大幅下降

rocketmq采用CommitLog+ConsumeQueue, 单个broker所有topic在CommitLog中顺序写

kafka只有异步刷盘，异步复制

都仅支持单topic分区有序。

rocketmq可运行延时消息

消息过滤，rocketmq支持tag过滤及自定义过滤

rocketmq支持定时重试，kafka不支持重试

rocketmq自己实现了namesvr，kafka使用zookeeper

高可用的区别，kafka高可用的粒度是分区，每个topic的leader分区和replica分区都可以在所有broker上负载均衡地存储。所有broker都可以收发消息，分区选举自动做的。RockerMQ高可用的设计只控制在broker，通过master-slave主从复制来解决。