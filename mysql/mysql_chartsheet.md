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

