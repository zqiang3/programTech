**strace命令**是一个集诊断、调试、统计与一体的工具，我们可以使用strace对应用的系统调用和信号传递的跟踪结果来对应用进行分析，以达到解决问题或者是了解应用工作过程的目的。当然strace与专业的调试工具比如说[gdb](http://man.linuxde.net/gdb)之类的是没法相比的，因为它不是一个专业的调试器。

strace的最简单的用法就是执行一个指定的命令，在指定的命令结束之后它也就退出了。在命令执行的过程中，strace会记录和解析命令进程的所有系统调用以及这个进程所接收到的所有的信号值。

##  语法

```
strace  [  -dffhiqrtttTvxx  ] [ -acolumn ] [ -eexpr ] ...
    [ -ofile ] [-ppid ] ...  [ -sstrsize ] [ -uusername ]
    [ -Evar=val ] ...  [ -Evar  ]...
    [ command [ arg ...  ] ]

strace  -c  [ -eexpr ] ...  [ -Ooverhead ] [ -Ssortby ]
    [ command [ arg...  ] ]
```



## 实例

```c

```





```
strace -p xxx
```

