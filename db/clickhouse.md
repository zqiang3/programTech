## 链接

https://clickhouse.tech/docs/zh/getting-started/tutorial/



## Install

```bash
sudo apt-get install apt-transport-https ca-certificates dirmngr
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4

echo "deb https://repo.clickhouse.tech/deb/stable/ main/" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update

sudo apt-get install -y clickhouse-server clickhouse-client

sudo service clickhouse-server start
clickhouse-client
```



## start

```

```



## 基本使用

```
CREATE DATABASE IF NOT EXISTS indexsysdb;
-- use indexsysdb;
CREATE TABLE indexsysdb.keyword1h \
(keyword String,\
dtime DateTime('Asia/Shanghai'),\
source1 String,\
source2 String,\
mood Int8,\
category Int8,\
amount UInt64) \
ENGINE = SummingMergeTree(amount) \
PARTITION BY toYYYYMM(dtime) \
ORDER BY (dtime, keyword, source1, source2,mood,category)
```





OLAP: online analytical processing

列式数据库管理系统

支持SQL



## 不擅长的场景

select * from table where user in (xxx, xxx, xxx) 此类查询场景推荐使用abase

blob or document storage

