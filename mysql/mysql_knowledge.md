##link

https://www.zhihu.com/question/28385400/answer/87729818



## 时间

MySQL有三种时间类型：

- `DATE：`用于只包含日期不包含时间的时候，`MySQL`会将格式转换为`YYYY-MM-DD`，合法范围为`1000-01-01 - 9999-12-31`。
- `DATETIME：`用于包含日期`+`时间的时候，格式为`YYYY-MM-DD HH:MM:SS`，合法范围为`1000-01-01 00:00:00 - 9999-12-31 23:59:59`。
- `TIMESTAMP：`用于包含日期`+`时间的时候，格式为`YYYY-MM-DD HH:MM:SS`，合法范围为`1997-01-01 00:00:01 - 2038-01-19 03:14:07 UTC`。

同时，`DATETIME`和`TIMESTAMP`还都支持一个`6`位微秒的数据支持，格式为`YYYY-MM-DD HH:MM:SS[.fraction]`，合法范围为`.000000 - .999999`。

对于`TIMESTAMP`类型，`MySQL`会在存储时**将数据值转换为`UTC`标准时间来存储**，读取时再转为当前时间。如果你的时区没有发生改变，则该值就是你存储的值，如果你改变了时区，读取到的值就会发生变化。这个特性不会对`DATETIME`生效。



## 查看时区

```bash 
show variables like '%zone%';
```



## 非法时间的问题

经过查询资料，发现原因是在`MySQL`中，`timestamp`类型的合法区间是`1970-01-01 00:00:01 - 2038-01-19 03:14:07 UTC`，而在存储是，会先将你插入的数据转换为`UTC`时间，然后存储起来，读取的时候，再转换为你的本地时间。由于我的时区为东八区，因此转换后就变为了`1970-01-01 00:00:00 UTC`，成为了非法时间。



MySQL严格模式

```bash
show variables like 'sql_mode';
select @@global.sql_mode;

| sql_mode      | ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
```

