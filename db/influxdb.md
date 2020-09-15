## 简介

InfluxDB是针对时间序列数据进行了优化的数据库。时间序列数据通常是一次写入，很少更新。

## 开发语言

go



## 安装

```
brew update
brew install influxdb
```



## 启动

```bash 
ln -sfv /usr/local/opt/influxdb/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.influxdb.plist
```

没有做第一个步骤的话，启动文件在：**/usr/local/opt/influxdb/**

## 停止

```
launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.influxdb.plist
```



## 使用

**连接**

```
influx -precision rfc3339
```



> InfluxDB的HTTP接口默认起在`8086`上，所以`influx`默认也是连的本地的`8086`端口，你可以通过`influx --help`来看怎么修改默认值。
>
> `-precision`参数表明了任何返回的时间戳的格式和精度，在上面的例子里，`rfc3339`是让InfluxDB返回[RFC339](https://www.ietf.org/rfc/rfc3339.txt)格式(YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ)的时间戳。



**数据库**

```
exit
create database <db-name>
show databases
use <db-name>
```



**读写数据**

```
INSERT cpu,host=serverA,region=us_west value=0.64
SELECT "host", "region", "value" FROM "cpu"
```

> 说明：我们在写入的时候没有包含时间戳，当没有带时间戳的时候，InfluxDB会自动添加本地的当前时间作为它的时间戳。



再写入一笔数据

```
INSERT temperature,machine=unit42,type=assembly external=25,internal=37
SELECT * FROM "temperature"
```

**查询数据**

```
curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=test" --data-urlencode "q=SELECT * FROM \"cpu\" "
```



**时间格式**

```
epoch=s
```

**最大行限制**

可选参数`max-row-limit`允许使用者限制返回结果的数目，以保护InfluxDB不会在聚合结果的时候导致的内存耗尽。



## 示例

```
SELECT * FROM "foodships" WHERE "planet" = 'Saturn' AND time > '2015-04-16 12:00:01'
```



| u或µ | 微秒 |
| ---- | ---- |
| ms   | 毫秒 |
| s    | 秒   |
| m    | 分钟 |
| h    | 小时 |
| d    | 天   |
| w    | 星期 |



## 使用建议



- 把你经常查询的字段作为tag
- 如果你要对其使用`GROUP BY()`，也要放在tag中
- 如果你要对其使用InfluxQL函数，则将其放到field中
- 如果你需要存储的值不是字符串，则需要放到field中，因为tag value只能是字符串



请注意，如果查询中包含除[A-z，_]以外的字符，则还需要将它们用双引号括起来

## 核心概念

database相当于mysql中的database

measurement相当于mysql中的表

point相当于mysql中的行

tag相当于mysql中的索引，只支持字符串类型

field相当于mysql中的列，支持多种类型



## 数据库命令

```bash
show databases
create database grafana
use grafana
drop database db_name
show measurements
drop measurement tb_name

# 创建用户
create user grafana with password 'grafana' with all privileges
show users

insert cpu,host=192.168.1.1 load=0.1,usage=0.2
select * from cpu
select host, load, usage from cpu
select host from cpu where host="192.168.1.1"
```

## HTTP API

```
# 创建数据库
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE test"

#写入单条
curl -i -XPOST http://localhost:8086/write?db=test --data-binary "cpu,host=192.168.1.3 load=0.1,usage=0.33"

curl -i -XPOST http://localhost:8086/write?db=test --data-binary "cpu,host=192.168.1.3 load=0.1,usage=0.33 6666666666666666666"

#写入多条
curl -i -XPOST http://localhost:8086/write?db=test --data-binary "cpu,host=192.168.1.2 load=0.1,usage=0.22 1666666666666666661 
cpu,host=192.168.1.3 load=0.1,usage=0.33 1666666666666666661 
cpu,host=192.168.1.2 load=0.2,usage=0.22 1666666666666666662 
cpu,host=192.168.1.3 load=0.2,usage=0.33 1666666666666666662"

curl -G http://localhost:8086/query?db=test --data-urlencode "q=SELECT * FROM  \"cpu\""
```

