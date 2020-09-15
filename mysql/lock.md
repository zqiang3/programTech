## 悲观锁

### 使用场景举例

```
create table t
(
	id int primary key auto_increment;
	name char(10),
	status int
);
```



**不使用锁**

```
select status from t where id = 1;
insert into t (name, status) values ('zq', 10);
update t set status = 2;
```

**使用悲观锁**

```
begin;
select status from t where id = 1 for update;
insert into t (name, status) values ('zq', 10);
update t set status = 2;
commit;
```

**悲观锁的条件**

1. 其中一个操作要使用事务
2. 使用`for update`锁住数据
3. 查询条件指定主键会执行行锁，指定非主键会执行表锁
4. 查询指定主键，但
5. 查询主键不存在的数据，不会锁住（因为执行的是表锁）

必须是使用`for update`的语句才会等待其他事务结束后才执行，如果不使用for update，则能正常查出数据，不受第一个事务的影响。

innodb默认是行级别锁，只有明确指定主键，才会执行行锁，否则会执行表锁。