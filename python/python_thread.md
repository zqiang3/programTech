## 概述

线程有一个指令指针，记录自己运行到什么地方。

线程的运行可能被中断，或暂时的被挂起。

同一进程中的各个线程共享同一片数据空间。

数据共享可能带来数据结果不一致的问题，这叫做race condition。

线程库带有一系列的同步原主，用来控制线程的执行和数据的访问。

python调用外部代码时，GIL将会被锁定，直到这个函数结束为止。

GIL会在I/O调用前释放

对源代码，解释器主循环和GIL感兴趣，可以看看python/ceval.c文件。

## threading.Thread

```
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
# 调用时应该始终用关键字参数
start()  # 只能调用一次
run()
join([timeout])
# Wait until the thread terminates. This blocks the calling thread until the thread whose join() method is called terminates-eigher normally or through an unhandled exception - or until the optional timeout occurs.
```

## 例子

```python
import threading
import time

def foo(nloop, nsec):
    print 'start foo', nloop, 'at: ', time.ctime()
    time.sleep(nsec)
    print 'loop', nloop, 'done at: ', time.ctime()


def main():
    print 'starting at: ', time.ctime()

    t = threading.Thread(target=foo, args=(3, 5))

    t.start()

    t.join()

    print 'all DONE'


main()

```

