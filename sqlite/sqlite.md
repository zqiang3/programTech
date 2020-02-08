```bash
# 同时查看表头
sqlite>.headers ON

# 删除
sqlite>delete from table;

.databases
.tables
.quit
```



## 创建一个新的数据库

```bash
sqlite3 test.db
```



## 创建表

```bash
create table company(
   ...> id int primary key not null,
   ...> name text not null,
   ...> age int not null,
   ...> address char(50),
   ...> salary real);
```



## insert

```bash
insert into company(id, name, age, address, salary) values (1, 'Paul', 32, 'California', 2000.00);
```



## select 

```bash
select * from company;
```

