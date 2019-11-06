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
create database 库名

# 删库
drop database 库名
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


select id, created_time from 表名 where user_id = 6729061087028707336;
# 使用to_days
select id, created_time from 表名 where user_id = 6729061087028707336 AND to_days(created_time) >= to_days(now());
```





```
# 统计行数
select count(*) from table_name;


```



## mysql数据类型

https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html

类型声明中括号中的数字是*显示宽度*，它与可以存储在数据类型中的值的范围无关。只是因为你可以声明`Int(20)`并不意味着你可以存储高达10 ^ 20的值：

> [...]这个可选的显示宽度可以被应用程序用来显示宽度小于为该列指定的宽度的整数值，方法是用空格填充它们。... **显示宽度不限制可存储在列中的值的范围，也不限制显示宽度超过为列指定的值的位数。**例如，指定为SMALLINT（3）的列具有通常的SMALLINT范围-32768至32767，并且三个字符所允许的范围之外的值使用三个以上的字符显示。

