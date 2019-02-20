## 链接

https://blog.csdn.net/u010353408/article/details/78283309

### 1.前言

Logstash是一款由ruby编写的开源数据采集工具。其支持对多种不同的数据源进行采集，并进行自定义处理，然后传输到指定位置。为后续的数据分析、可视化等应用提供支持。

Logstash is an open source data collection engine with real-time pipelining capabilities.



### 2.Logstash

从数据源到存储端，Logstash的工作共分为三个过程：数据采集、数据处理（可选）、数据输出。对应的三个插件Input、Filter(可选)、Output来完成相应的工作。

