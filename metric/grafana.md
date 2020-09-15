## 基本概念

* Data Source
* DashBoard
* Row
* Panel
* Query Editor
* Organization
* User



## 特点

展示：快速灵活的客户端图表

多数据源支持：Graphite，InfluxDB，OpenTSDB，Prometheus，Elasticsearch，CloudWatch和KairosDB等

通知提醒

混合展示

注释

过滤器



## 安装

官方下载地址： https://grafana.com/grafana/download

### Installing on macOS

Install Grafana on macOS. You can either install using homebrew or a binary tar file.



```bash
brew update
brew install grafana
```



To upgrade use the reinstall command.

```bash
brew update
brew reinstall grafana
```

## Start Grafana

start Grafana using homebrew services

```bash
brew tap homebrew/services
brew services start grafana
```

## Logging in for the first time

go to http://localhost:3000/

user/password: admin/admin

## How to add a data source