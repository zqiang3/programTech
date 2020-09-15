```bash 
# 连接mysql
mysql -h host -P port -u user -p

# 显示可用的存储引擎
show engines;


# ----------------表相关命令--------------
# 显示数据表
show tables

# 显示表的结构
desc 表名

#
show create table 表名

# 建表


mysql> create table api_inline_image (                                                                -> `id` bigint(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    -> `app_id` varchar(255) NOT NULL,
    -> `from_email_address` VARCHAR(255) NOT NULL,
    -> `content_id` VARCHAR(255) NOT NULL,
    -> `file_key` TEXT NOT NULL,
    -> `file_size` BIGINT(20) NOT NULL DEFAULT '0'
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



# 查看表中的索引
SHOW INDEX FROM tablename

# 添加字段

alter table api_inline_image add `created_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) comment '创建时间';
alter table api_inline_image add created_time timestamp(6) not null default current_timestamp(6);

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

## 数组库级语句

```
show databases;
SHOW CREATE DABASE db_name;
select database();
USE db_name;
CREATE DATABASE [IF NOT EXIST] db_name;
DROP DATABASE db_name;
ALTER DATABASE  // 更改数据库的全局属性

show full processlist;

show engine innodb status;

select @@tx_isolation;

select @@global.tx_isolation;

```

建库

```
CREATE DATABASE mydb CHARACTER SET utf8 COLLATE utf8_icelandic_ci;
```

一个数据库就是MYSQL数据目录里的一个目录，这个目录主要用于存放对象，如表，视图和触发器。



## 表级语句

```
SHOW TABLES;
SHOW TABLES FROM db_name;
SHOW CREATE TABLE tbl_name;
SHOW COLUMNS FROM tbl_name;  // 同 DESCRIBE tbl_name;
SHOW INDEX FROM tbl_name;
SHOW TABLE STATUS;
SHOW TABLE STATUS FROM db_name;
SHOW COLUMNS FROM student LIKE 's%';
SHOW TABLES LIKE `tbl_name`;
```



## 存储引擎

```
show engines;
```

| 存储引擎 |                                                        |      |
| -------- | ------------------------------------------------------ | ---- |
| InnoDB   | supports transactions, row-level locking, foreign keys |      |
|          |                                                        |      |
|          |                                                        |      |



## 建表

```bash 
mysql> create table `person` (
    -> `id` bigint(20) not null auto_increment,
    -> `name` varchar(255) not null,
    -> `score` int(11) not null,
    -> `create_time` timestamp not null default current_timestamp on update current_timestamp,
    -> primary key (`id`),
    -> key `name_score` (`name`(191), `score`),
    -> key `create_time` (`create_time`)
    -> ) engine=innodb default charset=utf8mb4;


CREATE TABLE table_name
(
	name CHAR(20),
	birth DATE NOT NULL,
	weight INT,
	sex ENUM('F', 'M')
);

create table t (name char(20), unique (name)) engine = InnoDB;

create table api_inline_image ( `id` bigint(20) NOT NULL PRIMARY KEY AUTO_INCREMENT, `app_id` varchar(255) NOT NULL, `from_email_address` VARCHAR(255) NOT NULL, `content_id` VARCHAR(255) NOT NULL,`file_key` TEXT NOT NULL, `file_size` BIGINT(20) NOT NULL DEFAULT '0');
```

## 删表

```
drop table [TABLE]
```



## 插入

**方法一**

```
insert into table_name (field1, field2, ... fieldN)
values
(value1, value2, ...valueN)
```

如果数据类型是字符型，必须使用单引号或双引号

**方法二**

```
insert into tablename set column_name1 = value1, column_name2 = value2, ...
```

**两者区别**

* 使用了set，必须至少为一列赋值。
* insert允许插入多条语句，set不行。

## 索引

### 创建索引

可以在使用`CREATE TABLE`时包含索引定义。

为已有表添加索引，可以使用`ALTER TABLE`或`CREATE INDEX`, MySQL会在其内部把`CREATE INDEX`语句映射为`ALTER TABLE`操作。

**方式一**

```
ALTER TABLE table_name ADD INDEX index_name (index_columns);
ALTER TABLE table_name ADD UNIQUE index_name (index_columns);
ALTER TABLE table_name ADD PRIMARY KEY (index_columns);
ALTER TABLE table_name ADD SPATIAL KEY (index_columns);
alter table tenant_domain add index `idx_is_dns_verified_by_cronjob` (`is_dns_verified_by_cronjob`);
```

index_name是可选的，如果没指定，MySQL会根据第一个索引列的名字选取一个名字。

**方式二**

除PRIMARY KEY以外，大部分索引类型都可以用CREATE INDEX语句来添加。

```
CREATE INDEX index_name ON tbl_name (index_columns);
CREATE UNIQUE INDEX index_name ON tbl_name (index_columns);
CREATE FULLTEXT INDEX index_name ON tbl_name (index_columns);
CREATE SPATIAL INDEX index_name ON tbl_name (index_columns);
```

**方式三**

```
CREATE TABLE tbl_name
(
	INDEX index_name (index_columns),
	UNIQUE index_name (index_columns),
	PRIMARY KEY (index_columns),
	SPATIAL index_name (index_columns),
	...
);
```

下面两条语句是等价的

```
CREATE TABLE mytbl
(
	i INT NOT NULL PRIMARY KEY,
	j CHAR(10) NOT NULL UNIQUE
);

CREATE TABLE mytbl
(
	i INT NOT NULL,
	j CHAR(10) NOT NULL,
	PRIMARY KEY (i),
	UNIQUE (j)
);
```

USING BTREE

```
CREATE TABLE tbl
(
	id INT NOT NULL,
	name CHAR(100),
	INDEX (id) USING BTREE
) ENGINE = MEMORY;
```

### 删除索引

```
DROP INDEX index_name ON tbl_name;
DROP INDEX `PRIMARY` ON tbl_name;
```

DROP INDEX语句会被内部处理成ALTER TABLE语句。

```
ALTER TABLE tbl_name DROP INDEX index_name;
ALTER TABLE tbl_name DROP PRIMARY KEY;
```

## SELECT 语句

is null

```
select * from tenant_domain where verification_code is NULL;
```



## ALTER 语句

```
ALTER TABLE tbl_name action [, action] ...;
```

1. 更改列的数据类型

可以使用CHANGE子句或MODIFY子句，CHANGE可以将该列重命名

```
ALTER TALBE my_tbl MODIFY i MEDIUMINT UNSIGNED;
ALTER TABLE myj_tbl CHANGE old_name new_name MEDIUMINT UNSIGNED;
```

2. 改用另一种存储引擎

```
ALTER TALBE tbl_name ENGINE = engine_name;
```

3. 重新命名表

```
ALTER TABLE tbl_name RENAME TO new_name
RENAME TABLE tbl_name TO new_name
```

4. 添加字段

```
ALTER TABLE `app_id_user_ref` ADD username VARCHAR(255) DEFAULT '' COMMENT '用户名';
alter table tenant_domain add dns_check_type tinyint(1) not null default '0' comment 'dns check type';
```



5. 删除字段

```
alter table TABLENAME drop columnnane;
```



## UPDATE 语句

```
UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
```



## DELETE 语句

```
delete from table_name where;
```



## 排序

```
CREATE TABLE `t` (
  `id` int(11) NOT NULL,
  `city` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  `age` int(11) NOT NULL,
  `addr` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `city` (`city`)
) ENGINE=InnoDB;

select city,name,age from t where city='杭州' order by name limit 1000  ;
```



## 事务

```
# 每个语句是一个事务，自动提交
set autocommit = 1

# 开启事务
begin;
或start transaction

# 立即开启事务
start transaction with consistent snapshot
# 提交事务
commit;

start transaction;
savepoint example_savepoint;  // 事务保存点
rollback to savepoint example_savepoint;

# select 加读锁（共享锁）也是当前读
select k from t where id=1 lock in share mode;
# select 加写锁（排他锁）也是当前读
select k from t where id=1 for update;
```

## 锁

查看锁表情况

```
show status like 'Table%'
```

全局锁

```
flush tables with read lock
```

表级锁

```
lock tables t1 read, t2 write
```

死锁检测会消耗大量的cpu资源



共享锁

```
select * from t where c = 7 lock in share mode;
```

排他锁

```
select * from t where c = 7 for udpate;
```



## 存储过程

```
create procedure insert_person()
begin
	declare c_id integer default 1,
	while c_id <= 100000 do
	insert into person values(c_id, concat('name', c_id), c_id+100, date_sub(NOW(), interval c_id second));
	set c_id = c_id + 1
	end while
end
```





## 参考语句

```mysql
# 使用to_days
select id, created_time from 表名 where user_id = 6729061087028707336 AND to_days(created_time) >= to_days(now());

# 高级
UPDATE user_mail 
SET mail_address = CASE mail_address WHEN '' THEN NULL ELSE mail_address END,
mail_prefix = CASE mail_prefix WHEN '' THEN NULL ELSE mail_prefix END where user_id != 0
```



## 执行计划

```bash
explain select * from person where name = 'sql';
```



## mysql数据类型

https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html

book: 《MySQL必知必会》附录D

类型声明中括号中的数字是*显示宽度*，它与可以存储在数据类型中的值的范围无关。只是因为你可以声明`Int(20)`并不意味着你可以存储高达10 ^ 20的值：

> [...]这个可选的显示宽度可以被应用程序用来显示宽度小于为该列指定的宽度的整数值，方法是用空格填充它们。... **显示宽度不限制可存储在列中的值的范围，也不限制显示宽度超过为列指定的值的位数。**例如，指定为SMALLINT（3）的列具有通常的SMALLINT范围-32768至32767，并且三个字符所允许的范围之外的值使用三个以上的字符显示。



### 1. The CHAR and VARCHAR Types

Link: https://dev.mysql.com/doc/refman/8.0/en/char.html

有两种基本的串类型，分别为定长串和变长串。

CHAR是定长串类型, 长度是0-255

VARCHAR是变长串，长度可以是0-65535字节

TEXT属于变长串类型

变长数据类型这样灵活，为什么还要使用定长数据类型？原因是因为性能，MySQL处理定长列比处理变长列快得多。此外，MySQL不允许对变长列（或一个列的可变部分）进行索引，这也会极大地影响性能。

### 2. Integer Types

Link: https://dev.mysql.com/doc/refman/8.0/en/integer-types.html



## 组合索引的字段太长怎么办？

在使用组合索引的时候可能因为列名长度过长而导致索引的key太大，导致效率降低，在允许的情况下，可以只取col1和col2的前几个字符作为索引

```go
ALTER TABLE 'table_name' ADD INDEX index_name(col1(4),col2（3))；
```

## 存储引擎是以什么为单位？

mysql的一大特色，是可以自由选择存储引擎。每个表都是一个文件，都可以自由选择存储引擎。

是以库为单位，还是以表为单位