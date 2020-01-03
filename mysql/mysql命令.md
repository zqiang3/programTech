```bash 
# 连接mysql
mysql -h host -P port -u user -p

# ----------------库相关命令--------------
# 显示数据库列表
show databases;

# 显示当前使用的数据库
select database();

# 使用某个数据库
use 库名;

# 建库
create [if not exists] database 库名

# 删库
drop database 库名

# 更改
alter database

# 查看数据库定义
show create database 库名

# 显示可用的存储引擎
show engines;
# --------------------------------------

# ----------------表相关命令--------------
# 显示数据表
show tables

# 显示表的结构
desc 表名

#
show create table 表名

# 建表
mysql> create table student
    -> (
    -> sid varchar(20) not null primary key,
    -> name varchar(20) not null,
    -> address varchar(50)
    -> );

# 删表
drop table 表名

# 删除表中的所有内容
# 不带where参数的delete语句可以删除mysql表中所有内容
delete from 表名
# --------------------------------------

# ----------------查询命令--------------
# 查询
select * from 表名;
select * from 表名 limit 1;

# 模糊查询
SELECT * FROM table_name WHERE column_1 LIKE '%三'

# 统计行数
select count(*) from table_name;


select id, created_time from 表名 where user_id = 6729061087028707336;


# 排序
ORDER BY FIELD1 [ASC [DESC][默认 ASC]], [field2...] [ASC [DESC][默认 ASC]]

# 删字段
alter table TABLENAME drop columnnane;

# 查看表中的索引
SHOW INDEX FROM tablename

# 添加字段
alter table TABLENAME 

# 添加索引

CREATE TABLE mytable(  
    ID INT NOT NULL,   
    username VARCHAR(16) NOT NULL,  
    INDEX [indexName] (username(length))  
);
ALTER TABLE my_table ADD [UNIQUE] INDEX index_name(column_name);
或者
CREATE INDEX index_name ON my_table(column_name);

# 主键索引
ALTER TABLE 'table_name' ADD PRIMARY KEY pk_index('col')；

# 唯一索引
ALTER TABLE `t_user` ADD unique(`username`);
ALTER TABLE 'table_name' ADD UNIQUE index_name('col')；

# 组合索引
ALTER TABLE mail_tenant ADD UNIQUE uniq_idx_mail_domain_tenant_id (`mail_domain`(100), `tenant_id`(20)) using BTREE;
ALTER TABLE 'table_name' ADD INDEX index_name('col1','col2','col3')；

# 显示索引
alter table `person` add index idx_name(`name`);
ALTER TABLE 'table_name' ADD INDEX index_name('col')；

# 添加索引时指定长度
CREATE INDEX index_name ON table_name (column_name(length), clolumn_name(length)…)；

# 删除索引

DROP INDEX my_index ON tablename；
或者
ALTER TABLE table_name DROP INDEX index_name;
```



## 参考语句

```mysql
# 使用to_days
select id, created_time from 表名 where user_id = 6729061087028707336 AND to_days(created_time) >= to_days(now());
```







## 执行计划

```bash
explain select * from person where name = 'sql';
```



## mysql数据类型

https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html

类型声明中括号中的数字是*显示宽度*，它与可以存储在数据类型中的值的范围无关。只是因为你可以声明`Int(20)`并不意味着你可以存储高达10 ^ 20的值：

> [...]这个可选的显示宽度可以被应用程序用来显示宽度小于为该列指定的宽度的整数值，方法是用空格填充它们。... **显示宽度不限制可存储在列中的值的范围，也不限制显示宽度超过为列指定的值的位数。**例如，指定为SMALLINT（3）的列具有通常的SMALLINT范围-32768至32767，并且三个字符所允许的范围之外的值使用三个以上的字符显示。





## 组合索引的字段太长怎么办？

在使用组合索引的时候可能因为列名长度过长而导致索引的key太大，导致效率降低，在允许的情况下，可以只取col1和col2的前几个字符作为索引

```go
ALTER TABLE 'table_name' ADD INDEX index_name(col1(4),col2（3))；
```

