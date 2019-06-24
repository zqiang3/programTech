vmstat是一个常用的系统性能分析工具，主要用来分析系统的内存使用情况，也常用来分析CPU上下文切换和中断的次数。

```bash
# 每5秒输出一组数据
vmstat 5
```

* cs(context switch) 每秒上下文切换次数
* in(interrupt) 每秒中断次数
* r(running or runnable) 就绪队列，正在运行和等待CPU的进程数
* b(blocked) 不可中断睡眠状态的进程数。

