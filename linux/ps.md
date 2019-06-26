### 实例

```
# 查看某个服务的cpu和内存占用
 ps aux | grep mentactivity | grep -v 'grep' |head -10 |  awk '{print $2 " cpu:" $3 " mem:" $4"%" " time:" $9}'
```





```bash
ps axf   # 主要用于查看当前系统中进程的 PID 以及执行终端(tty)和状态等信息，更重要的是它能显示出进程的父子关系。
ps axj   # 主要用于查看当前系统中进程的 PPID、PID、PGID、SID、TTY 等信息。
ps axm   # 显示进程的详细信息，PID 列下面的减号(-)是这个进程中的线程。
ps ax -L # 以 Linux 的形式显示当前系统中的进程列表。
# man ps
To get info about threads:
ps -eLf
ps axms

To print a process tree:
ps -ejH
ps axjf

To see every process on the system using BSD syntax:
ps ax
ps axu
```

## man ps

x: This option causes ps to list all processes owned by you (same EUID as ps), or to list all processes when used together with the a option.

m, -m: Show threads after processes.

j, -j: Jobs format.

l, -l: long format.

f, --forest: ASCII art process hierarchy

## ps

ps 是process status的缩写，ps用来显示当前系统中的进程。ps是最基本同时也是非常强大的进程查看命令使用该命令可以查看正在运行的进程和进程的状态、进程是否结束、进程有没有僵死，进程占用多少资源等等。

## 进程的5种状态

1. 运行（正在运行或在运行队列中等待）
2. 中断（休眠中, 受阻, 在等待某个条件的形成或接受到信号）
3. 不可中断
4. 僵死（进程已终止，但进程描述符存在，直到父进程回收）
5. 停止（进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行运行）

D 不可中断的休眠状态（通常 IO 的进程）

R 运行

S 中断

T 停止或被追踪

Z 僵死

< 优先级高的进程
N 优先级较低的进程
L 有些页被锁进内存；
s 进程的领导者（在它之下有子进程）；
l 多进程的（使用 CLONE_THREAD, 类似 NPTL pthreads）；

`+` 位于后台的进程组；

## 状态位解释

F 代表这个程序的旗标 (flag)，4 代表使用者为 super user

S 代表这个程序的状态 (STAT)

UID 程序被该 UID 所拥有

USER   进程的属主；
PID      进程的ID；
PPID    父进程；

C CPU 使用的资源百分比

%CPU   进程占用的CPU百分比；
%MEM  占用内存的百分比；

PRI 这个是 Priority (优先执行序) 的缩写

NI         进程的NICE值，数值大，表示较少占用CPU时间；

ADDR 这个是 kernel function，指出该程序在内存的那个部分。如果是个 running的程序，一般就是 "-"

SZ 使用掉的内存大小

WCHAN 目前这个程序是否正在运作当中，若为 - 表示正在运作

VSZ       該进程使用的虚拟內存量（KB）；
RSS        該進程占用的固定內存量（KB）（驻留中页的数量）；
TTY       登入者的终端机
WCHAN   當前進程是否正在進行，若為-表示正在進行；
START     該進程被觸發启动时间；
TIME       进程实际使用的CPU时间；
CMD   命令的名称和参数；


## 两种风格

BSD与UNIX

因此，ps aux与ps -aux是不同的。

## 查看进程的运行时间

```bash
ps -eo pid,tty,user,comm,lstart,etime | grep 17674
```

**参数说明**：

pid：进程ID

tty：终端

user：用户

comm：进程名

lstart：开始时间

etime：运行时间

## 参数

### BSD风格

T  显示跟当前终端关联的所有进程

a  显示跟任意终端关联的所有进程（显示所有用户的进程，但必须是跟终端关联）

x 显示所有的进程，包括未分配终端的进程(只显示当前用户的，但不必跟终端关联)

u 基于用户的格式 (类似于UNIX风格的-f)

ax ax组合就可以显示所有用户的所有进程（包括未分配终端的进程）

**aux** 加上u可以显示完整的格式输出

U userlist  显示在用户列表中的进程

p pidlist  显示在进程列表中的进程

t ttylist  显示在终端列表中的进程

r 仅显示运行中的进程



### UNIX风格

-e 显示所有进程

-a 显示所有进程，排除控制进程和无终端进程

-L 显示进程中的线程

-U userlist  属主用户id在列表中

-u userlist  有效用户id在列表中



## 查看所有进程

```bash
ps ax
ps -e
```

加上-f 或者 u参数可以显示进程的详细信息

```bash
ps aux
ps -ef
```

注：当用户名超过8个字符时，以uid显示；小于等于8字符时，以用户名显示。

## 显示某个用户的进程

```
ps -f -u sparkfly,root
```

## 显示某个进程名或进程id的进程

```bash
ps -f -C nginx
ps -f -p 3150,7298,6544
```

## 利用 cpu 或者内存使用量对进程排序

```
ps aux --sort=-pcpu,+pmem
```

## 显示进程树

```bash
ps -f --forest -C nginx
```

## 显示某个进程的所有子进程

```bash
ps -o pid,uname,comm -C nginx
ps --ppid 9293
```

## 显示进程中的线程

```
ps -p 12974 -L
```

## 显示进程已运行的时间

```bash
ps -e -o pid,comm,etime
```

## 实时显示进程信息

```bash
watch -n 1 'ps au'
```

## 自定义输出列

```bash
 ps -o pid,ppid,pgid,sid,comm
```

## 显示某个进程启动时间

```bash
ps -p PID -o lstart
```



## 参考

参数： 
-A ：所有的进程均显示出来，与 -e 具有同样的效用； 
-a ： 显示现行终端机下的所有进程f，包括其他用户的进程； 
-u ：以用户为主的进程状态 ； 
x ：通常与 a 这个参数一起使用，可列出较完整信息。 
输出格式规划： 
l ：较长、较详细的将该 PID 的的信息列出； 
j ：工作的格式 (jobs format) 
-f ：做一个更为完整的输出。 

特别说明： 
由于 ps 能够支持的系统类型相当的多，所以他的参数多的离谱！ 
而且有没有加上 - 差很多！详细的用法应该要参考 man ps 喔！