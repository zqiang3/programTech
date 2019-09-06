```bash 
# 连接mysql
mysql -u root -p

# 显示数据库列表
show databases;

# 使用某个数据库
use 库名

# 建库
create database 库名

# 删库
drop database 库名

# 显示数据表
show tables

# 显示表的结构
desc 表名

# 建表
mysql> create table student
    -> (
    -> sid varchar(20) not null primary key,
    -> name varchar(20) not null,
    -> address varchar(50)
    -> );

# 删表
drop table 表名

# 查询
select * from table_name limit 1;

# 统计行数
select count(*) from table_name;
```

