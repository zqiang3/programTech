## 工作模式

单进程多线程

## 简单查询

**语法**

```bash
select <列名>, <列名> from <表名> where <查询条件>;
星号(*): 查询全部列
as: 为列设定别名
select distinct 学号, 姓名 from student;
```

示例

```
select * from t;
select id, name from t;
select distinct id, name from student;
select name as student_name from student;
select * form t where name = '猴子';
```





## SQL书写规则

* 列名不能加单引号，不然认为是字符串
* 列名命名时不能有空格
* 符号只能使用英文符号

## SQL执行顺序

select子句最后执行，其他子句按书写顺序执行

```
3 select id, name
1 from student
2 where name = 'monkey';
```

## 运算符

```bash
select 学号, 成绩, 成绩/100 as '百分比成绩' from student;
```



## binlog

https://www.jianshu.com/p/c16686b35807



## 主从同步

主库数据发生变化，同步变化到从库。

三种格式：statement, row 和mixed

1. statement: 会将sql命令写入到binlog
2. row: 将每一条数据的变化写入到binlog
3. mixed: statement与row的混合，由mysql决定

## 数据库设计

核心设计思想

* 计算存储分离
  * 可以动态调整计算节点数量
  * 支持存储容量独立扩展，不影响计算层的实例分布
* 日志与数据分离
  * 读写分离架构
  * 分布式数据存储引擎
  * 分布式日志引擎
* 100%兼容MySQL

特性：

* 生态兼容性，100%兼容MySQL
* 高扩展：单库容量，单表容量，计算存储按需扩展
* 高性能：1主多备，上百万只读QPS，备机滞后1秒以内
* 高可用：数据冗余，热备



## 疑难问题

从节点出现延迟原因及解决办法。

出现原因：

1. 从服务器性能角度考虑，主从节点的硬件配置过低
2. 参数配置不合理
3. 主节点运行大事务，日志格式为row，产生大量的binlog日志需要同步到从节点
4. 主节点慢查询影响

解决办法：

性能问题，如MEM不足，IO性能差，调整配置参数

定位到是sql_thread

io_thread 可以从网络方面解决，使用压缩传输

查看是否有慢查询，优化慢查询sql

缺少主键导致所有的sql_thread扫描全表造成同步延迟





