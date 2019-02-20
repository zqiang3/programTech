/proc实际上是linux的一个虚拟文件系统，用于内核空间与用户空间之间的通信。

## interrupts

/proc/interrupts提供了一个只读的中断使用情况。

```bash
watch -d cat /proc/interrupts
```

