## 参考链接

http://python.jobbole.com/87743/

## 作用

**One thread runs python, while N other sleep or await I/O.**

GIL 对程序中线程的影响足够简单，你可以在手背上写下这个原则：“一个线程运行 Python ，而其他 N 个睡眠或者等待 I/O.”（即保证同一时刻只有一个线程对共享资源进行存取）  Python 线程也可以等待**threading.Lock**或者线程模块中的其他同步对象；线程处于这种状态也称之为”睡眠“。

## 协同式多任务处理

当一项任务比如网络 I/O启动，而在长的或不确定的时间，没有运行任何 Python 代码的需要，一个线程便会让出GIL，从而其他线程可以获取 GIL 而运行 Python。这种礼貌行为称为协同式多任务处理，它允许并发；多个线程同时等待不同事件。

**代码**

```python
import socket

def do_connect():
    s = socket.socket()
    s.connect(('python.org', 80))

for i in range(2):
    t = threading.Thread(target=do_connect)
    t.start()
```



## 抢占式多任务处理

## 线程是否安全

如果一个线程可以随时失去 GIL，你必须使让代码线程安全。 然而 Python 程序员对线程安全的看法大不同于 C 或者 Java 程序员，因为许多 Python 操作是原子的。

在列表中调用 sort()，就是原子操作的例子。线程不能在排序期间被打断，其他线程从来看不到列表排序的部分，也不会在列表排序之前看到过期的数据。原子操作简化了我们的生活，但也有意外。例如，+ = 似乎比 sort() 函数简单，但+ =不是原子操作。

看看下面的例子：

```sh
>>> n = 0
>>> def foo():
...     global n
...     n += 1
... 
>>> dis.dis(foo)
  3           0 LOAD_GLOBAL              0 (n)
              3 LOAD_CONST               1 (1)
              6 INPLACE_ADD         
              7 STORE_GLOBAL             0 (n)
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE 
```

代码的一行中， n += 1，被编译成 4 个字节码，进行 4 个基本操作：

1. 将 n 值加载到堆栈上
2. 将常数 1 加载到堆栈上
3. 将堆栈顶部的两个值相加
4. 将总和存储回 n

记住，一个线程每运行 1000 字节码，就会被解释器打断夺走 GIL 。如果运气不好，这（打断）可能发生在线程加载 n 值到堆栈期间，以及把它存储回 n 期间。很容易可以看到这个过程会导致更新丢失。



```python
import threading

n = 0

def foo():
    global n
    n += 1

threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print n
```

通常上面这个程序输出 100，因为 100 个线程每个都递增 n 。但有时你会看到 99 或 98 ，如果一个线程的更新被另一个覆盖。

所以，尽管有 GIL，你仍然需要加锁来保护共享的可变状态。

```python
n = 0
lock = threading.Lock()
 
def foo():
    global n
    with lock:
        n += 1
```





# 并行

每个fork的进程有一个单独的GIL

## 结语

既然你已经打开了音乐盒，看到了它简单的装置，你明白所有你需要知道的如何写出快速运行，线程安全的 Python 代码。**使用线程进行并发 I/O 操作，使用进程进行并行计算。**这个原则足够简单，你甚至不需要把它写在你的手上。