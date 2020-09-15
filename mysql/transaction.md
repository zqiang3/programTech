##事务的特点

* atomicity
* consistency
* isolation
* durability

##典型例子

银行账户转账

小明给小红转账10元，有两个操作

a. 小明的账户减少10元

b. 小红的账户增加10元

原子性是指，这两个操作要么都执行，要么都不执行



事务的隔离性是通过锁、MVCC等实现

事务的原子性、一致性和持久性则是通过事务日志实现



## 命令

1. 建表

```
create table t (name char(20), unique (name)) engine = InnoDB;
```

2. 利用事务在表里添加多行

```
start transaction;
insert into t set name = 'zq';
insert into t set name = 'zw';
commit;
select * from t;
```

