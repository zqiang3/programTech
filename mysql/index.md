## link

版权声明：本文为CSDN博主「万里归来少年心」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liyazhen2011/article/details/82787438



## MySQL索引

在SQL执行计划中，key_len 表示索引长度，经常用于判断复合索引是否被完全使用。先说结论：

在utf8编码方式下，一个字符占3个字节。
如果索引字段可以为null，MySQL会使用1个字节标识。
如果索引字段的类型长度可变，MySQL会使用2个字节标识。
    下面详细分析SQL执行计划中的索引长度。

1.建表、建索引、插入数据
    建立一个person表，仅有非空name列。在name上建立索引，并插入三条数据。相应的SQL语句如下：

```bash
create table pserson
(
	name char(20) not null
)

alter table person add index idx_name(name);
insert into person values("sql");
insert into person values("java");
```

2.SQL执行计划
2.1 索引非空
    在建表时，我们设置name为非空列，现在分析下面一条查询语句的执行计划。

```bash
explain select * from person where name = 'sql';
```


   执行计划如下：

key_len = 60，索引段name的长度是20个字符，key_len = 20*3 = 60。

这验证了第1条结论：在utf8编码方式下，一个字符占3个字节。



2.2索引可空
   现在我们稍作改动，允许name列为空。执行同样的查询语句，看看执行计划会有什么变化？

```bash
alter table person modify name char(20) null;
```


   执行计划如下：

   key_len = 61，索引段name的长度是20个字符，key_len = 20*3 + 1= 61。

   这验证了第2条结论：如果索引字段可以为null，MySQL会使用1个字节标识。

2.3索引可变长度类型
    继续改动，将name列的类型改为可变长度类型varchar(20)，执行上述同样的查询语句，看看执行计划会有什么变化？

```bash
alter table person modify name varchar(20);
```


   执行计划如下：

   key_len = 63，索引段name的长度是20个字符，key_len = 20*3 + 1 + 2= 63。

   这验证了第3条结论：如果索引字段的类型长度可变，MySQL会使用2个字节标识。

2.4复合索引
    给person表增加一列address，address列可以为空。建立复合索引（name,address），查看复合索引下的SQL执行计划。

```bash
alter table person add Column address varchar(20);
alter table person add index idx_name_address(name, address);
explain select * from person where name='';
```


​    执行计划如下：

key_len = 63，说明该SQL查询语句只用了复合索引的前半部分。

```bash
explain select * from person where address = '';
```


   执行计划如下：

key_len = 126，说明该SQL查询语句用了整个复合索引。

综上，key_len 表示索引长度，经常用于判断复合索引是否被完全使用。

注：utf8中一个字符占3个字节；gbk中一个字符占2个字节；latin中一个字符占1个字节。



## 索引的综合知识

### Hash索引

mysql默认存储引擎innodb只显式支持B-Tree( 从技术上来说是B+Tree)索引，对于频繁访问的表，innodb会透明建立自适应hash索引，即在B树索引基础上建立hash索引，可以显著提高查找效率，对于客户端是透明的，不可控制的，隐式的。

### B+Tree索引

是B-Tree的改进版本，同时也是数据库索引索引所采用的存储结构。数据都在叶子节点上，并且增加了顺序访问指针，每个叶子节点都指向相邻的叶子节点的地址。



## 索引的常见问题

### 索引是什么？

索引是排好序的数据结构，可用于快速查询。

### 索引对哪些操作有作用？

where 查找, order by排序

### 索引有哪些种类？

主键索引，普通索引，唯一索引，复合索引

根据数据的物理顺序与逻辑顺序关系，可分为：聚集索引和非聚集索引

