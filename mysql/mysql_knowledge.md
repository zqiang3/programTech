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



## 数据类型

**数值型**

| 类型名称         | 含义         | 存储空间   |
| ---------------- | ------------ | ---------- |
| TINYINT          |              | 1个字节    |
| SMALLINT         |              | 2          |
| MEDIUMINT        |              | 3          |
| INT              | 标准的整数   | 4          |
| BIGINT           | 大整数       | 8          |
| DECIMAL ([M[D]]) | 定点数       | 取决于M和D |
| FLOAT            | 单精度浮点数 | 4          |
| DOUBLE           | 双精度浮点数 | 8          |
| BIT ([M])        | 位域         | 取决于M    |



**字符型数据类型**

| 类型名称   | 含义                              |
| ---------- | --------------------------------- |
| CHAR       | 固定长度的非二进制字符串          |
| VARCHAR    | 可变长度的非二进制串              |
| BINARY     | 固定彻底的二进制串                |
| VARBINARY  | 可变长度的二进制串                |
| TINYBLOB   | 非常小型的BLOB（二进制大对象）    |
| BLOB       |                                   |
| MEDIUMBLOB |                                   |
| LONGBLOB   |                                   |
| TINYTEXT   | 非常小型的非二进制串，最大长度255 |
| TEXT       |                                   |
| MEDIUMTEXT |                                   |
| LONGTEXT   |                                   |
| ENUM       | 枚举集合                          |
| SET        | 集合                              |



**时间数据类型**

| 类型名称  | 含义                             |
| --------- | -------------------------------- |
| DATE      | 日期值 CCYY-MM-DD                |
| TIME      | 时间值 hh:mm:ss                  |
| DATETIME  | 日期加时间值 CCYY-MM-DD hh:mm:ss |
| TIMESTAMP | 时间戳值 CCYY-MM-DD hh:mm:ss     |
| YEAR      | 年份值 CCYY或YY                  |
|           |                                  |
|           |                                  |
|           |                                  |



每个列都有一个名字，一个类型，以及一些可能有的可选属性。

col_name col_type [type_attrs] [general_attrs]

如果使用了保留字，要用反引号将其引起来。

数字类型有UNSIGNED 和 ZEROFULL属性，非二进制串才有CHARACTER SET 和 COLLATE属性。

NULL 和 NOT NULL指定某列是否允许NULL值

DEFAULT子句用来指定列的默认值



### 列的默认值

如果某个列没有显式包含DEFAULT子句，并且该列允许为NULL值，其默认值就是NULL。如果没有默认值，而且也没有启用SQL的严格模式，那么该列将被设置成其数据类型的隐含默认值。

列的隐含默认值

数字列的默认值为0，对于AUTO_INCREMENT列，默认值是下一个列序号

时态类型列，默认值为该类型的零值，'0000-00-00'。对于TIMESTAMP列，自动初始化规则比较特殊。

字符串类型，默认值为空串

对于ENUM列，默认值为枚举值里的第一个元素

对于SET列，如果不允许包含NULL值，默认值是一个空集，不过它等价于空串。

### 存储空间

见上面的表

类型DECIMAL的存储空间取决于小数点左右两侧的数字个数。对于每一侧，每9位数字需要4个字节，最后剩下的数字需要1~4个字节。每一个值的存储空间等于小数点左右两边字节存储占用总和，是小数点左右两侧数值所需存储空间的总和。



定义整数列时，可以为它指定一个可选的显示宽度M，该值必须是1~255的整数。



### BIT类型

如果要以二进制显示位域值，可使用BIN()函数

```
select BIN(b) from t;
```

对于八进制和十六进制，可以分别使用OCT()和HEX()。

### UNSIGNED

UNSIGNED属性可以防止出现负值。

将整型列设为UNSIGNED会将其取值范围向右平移，而给DECIMAL或浮点加上UNSIGNED属性，取值范围并不会朝正数方向平移，相反，取值范围的上端不变，下端会变为0，整个取值范围被“砍掉”了一半。

### 字符型

二进制串类型和非二进制串类型之间的对应关系 

| 二进制串类型 | 非二进制串类型 |
| ------------ | -------------- |
| BINARY       | CHAR           |
| VARBINARY    | VARCHAR        |
| BLOB         | TEXT           |

每一种非二进制串类型，以及ENUM和SET类型，都可以指定具体的字符集和排序规则。对于不同的列，可以指定不同的字符集。