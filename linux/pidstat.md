



## pidstat命令

```bash
pidstat -u 5 1
```

pidstat是sysstat工具的一个命令，用于监控全部或指定进程的cpu、内存、设备IO等系统资源的占用情况

常用的参数：

-u: 默认的参数，显示各个进程的cpu使用统计

-r：显示各个进程的内存使用统计

-d：显示各个进程的IO使用情况

-p：指定进程号



```bash
pidstat -u
```

输出说明：

%usr：进程在用户空间占用cpu的百分比

%system：进程在内核空间占用cpu的百分比

%guest：进程在虚拟机占用cpu的百分比

%CPU：进程占用cpu的百分比

CPU：处理进程的cpu编号





```bash
pidstat -r
```

输出说明：

minflt/s：进程每秒钟出现的小错误的条数

majflt/s：进程每秒钟出现较大错误的条数

VSZ：进程使用的虚拟内存的大小（Kb）

RSS：进程使用的不可交换的物理内存（Kb）

%MEM：进程占用的物理内存百分比



```bash
pidstat -d
```

输出说明：

KB_rd/s：进程从硬盘读取数据的速度

KB_wr/s：进程向硬盘写入数据的速度

KB_cc/s：进程写入硬盘杯取消的速度

```
# -wt 参数表示输出线程的上下文切换指标
pidstat -wt 1
# -w 参数表示输出进程切换指标，而-u参数则表示输出CPU使用指标
pidstat -w -u 1
```

