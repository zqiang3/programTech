## Instatllation

### Downlad and install

```bash
brew update
brew install grafana
```

###Start Grafana

```bash
brew services start grafana
```

###restart Grafana

```
brew services restart grafana
```





## new



## 一、grafana简介

### 官方介绍



### 到底什么是grafana

经常被用于时间序列数据的展示，监控可视化

### 特性

支持多种数据源

Graphite, InfluxDB, OpenTSDB, Prometheus, Elasticsearch, CloudWatch和KairosDB



## 二、部署grafana

### 1. 安装grafana



### 2. 安装插件

```bash
# 查看都有什么插件可以安装
grafana-cli plugins list-remote | grep zabbix

# 安装grafana-zabbix 插件
grafana-cli plugins install alexanderzobnin-zabbix-app

# 安装时钟插件
grafana-cli plugins install grafana-clock-panel

# 安装后重启grafana
brew services restart grafana
```

## 三、登录

### 登录grafana

grafana的默认端口是3000

```bash
http://localhost:3000
```



### 用户名和密码

```
admin/admin
```



## 四、grafana使用

### 添加数据源

