* 可重复读(repeatable-read)

  什么是REPEATABLE-READ？就是当你开启一个事务,读一个数据,而后再次读，再读，再读……只要这个事务没结束，那么读取的数据就是一致的。

* 提交读(read-committed)

  就是只要事务提交了，那你就能读到修改的数据。



## autocommit

autocommit=OFF

python是自动开启新事务的，autocommit=OFF