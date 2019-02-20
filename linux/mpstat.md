## 命令说明

mpstat是 Multiprocessor Statistics的缩写，是实时系统监控工具.其报告与CPU的一些统计信息，这些信息存放在/proc/stat文件中。

参数：

-P：指定cpu号码，ALL表示监测所有cpu



vmstat和mpstat 命令的差别：mpstat 可以显示每个处理器的统计，而 vmstat 显示所有处理器的统计。因此，编写糟糕的应用程序（不使用多线程体系结构）可能会运行在一个多处理器机器上，而不使用所有处理器。从而导致一个 CPU 过载，而其他 CPU 却很空闲。通过 mpstat 可以轻松诊断这些类型的问题。



## 实例1

监控所有cpu，每5s产生一个报告，总共产生2个，然后输出平均值

```bash
mpstat -P ALL 5 2
```


