## 安装

```bash
pip2.7 install psutil
```

## 使用

```python
import psutil
psutil.Process().memory_full_info()
>>> pfullmem(rss=12554240, vms=46788608, shared=6656000, text=3264512, lib=0, data=5730304, dirty=0, uss=6275072, pss=7517184, swap=0)

```

##  指标

**术语解释**

1. VSS – Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）

2. RSS – Resident Set Size 实际使用物理内存（包含共享库占用的内存）

3. PSS – Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存）

4. USS – Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）

RSS（Resident set size）: 驻留集大小。这个内存耗用指标会大大高估内存和耗用情况。因为它同时包含了进程独一无二的内存和与其他进程共享的内存。将各进程的RSS值相加，通常会超出整个系统的内存消耗，因为RSS中包含了各进程间共享的内存。

USS(Unique set size ): 进程独自占用的内存大小，不包含任何共享的部分。进程被终止时，该部分内存立即被释放。（在psutil4.0.0引入）

PSS（Proportional set size）: 所有使用某共享库的程序均分该共享库占用的内存，每个进程占用的内存量。显然所有进程的PSS之和就是系统的内存使用量。它会更准确一些，它将**共享内存的大小进行平均后，再分摊到各进程上去。PSS这个指标衡量了耗用内存在每个共享内存区的“公平分配”，给出了一个切合实际的衡量指标。如果一个进程有10 MB都归自己（USS），并与另一个进程共享10 MB，那么其PSS将是15 MB。

swap: 交换内存的概念很简单，就是被交换到磁盘的内存量。

## linux的虚拟内存

Linux使用到了虚拟内存（virtual memory），因此要准确的计算一个进程实际使用的物理内存就不是那么简单。只知道进程的虚拟内存大小也并没有太大的用处，因为还是无法获取到实际分配的物理内存大小。