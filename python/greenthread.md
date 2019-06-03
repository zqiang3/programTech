## 链接

<https://blog.csdn.net/u014745194/article/details/71657575>

<http://luckylau.tech/2017/03/06/Python%E7%9A%84eventlet%E4%BD%BF%E7%94%A8%E4%B8%8E%E7%90%86%E8%A7%A3/>



## 什么是greenthread？

> Green threads emulate multi-threaded environment without relying on any native OS capabilities, and they are managed in user space instead of kernel space, enabling them to work in environments that do not have native thread support.



由于全局解释器锁(GIL)的存在，python一次只运行一个线程。

### 一个进程可以支持多少greenlets？

**开销**

常规线程仍然具有较高的上下文切换开销，greenlets没有这些相关的开销。基于gevent的服务器可以spawn上千个greenlets，wigh almost no overhead. 即使阻塞某些greenlets，也不会影响服务器接收新请求的能力，并发连接数实际上是无限的。

> While threads are cheap compared to processes (forks), they are still expensive to create for each new connection.
>
> Greenlets behave similar to traditional threads, but are very cheap to create. 

## spawn()

> Execution control returns immediately to the caller; the created greenthread is merely scheduled to be run at the next available opportunity.

从源码注释可以看出，绿线程在spwan后只是加入到调度队列，真正运行要等到合适的时机。

## GreenThread

> The GreenThread class is a type of Greenlet which has the additional property of being able to retrieve the return value of the main function. Do not construct GreenThread objects directly; call spawn() to get one.

## wait()

返回GreenThread主函数的结果

## eventlet

Eventlet是一个python网络库，通过协程的方式来实现并发。Eventlet协程又称作GreenThread（绿色线程）。

eventlet主要依赖另外2个python package：greenlet python-epoll

## eventlet是如何实现协程的

eventlet对python的几个网络相关的标准库函数进行了改写，可以以补丁的方式导入到程序中。pyton的库函数只支持普通线程，不支持协程。eventlet将其“绿化”实现协程。

## 协程之间何时切换，如何切换

目前的协程框架一般都是设计成 1:N 模式。所谓 1:N 就是一个线程作为一个容器里面放置多个协程。 那么谁来适时的切换这些协程？答案是有协程自己主动让出CPU，也就是每个协程池里面有一个调度器， 这个调度器是被动调度的。意思就是他不会主动调度。而且当一个协程发现自己执行不下去了(比如异步等待网络的数据回来，但是当前还没有数据到)， 这个时候就可以由这个协程通知调度器，这个时候执行到调度器的代码，调度器根据事先设计好的调度算法找到当前最需要CPU的协程。 切换这个协程的CPU上下文把CPU的运行权交个这个协程，直到这个协程出现执行不下去需要等等的情况，或者它调用主动让出CPU的API之类，触发下一次调度。

## 使用协程的好处

在IO密集型的程序中由于IO操作远远慢于CPU的操作，所以往往需要CPU去等IO操作。 同步IO下系统需要切换线程，让操作系统可以在IO过程中执行其他的东西。 这样虽然代码是符合人类的思维习惯但是由于大量的线程切换带来了大量的性能的浪费，尤其是IO密集型的程序。

所以人们发明了异步IO。就是当数据到达的时候触发我的回调。来减少线程切换带来性能损失。 但是这样的坏处也是很大的，主要的坏处就是操作被 “分片” 了，代码写的不是 “一气呵成” 这种。 而是每次来段数据就要判断 数据够不够处理哇，够处理就处理吧，不够处理就在等等吧。这样代码的可读性很低，其实也不符合人类的习惯。

但是协程可以很好解决这个问题。比如 把一个IO操作 写成一个协程。当触发IO操作的时候就自动让出CPU给其他协程。要知道协程的切换很轻的。 协程通过这种对异步IO的封装 既保留了性能也保证了代码的容易编写和可读性。在高IO密集型的程序下很好。但是高CPU密集型的程序下没啥好处。

## 一个简单的协程案例

## epoll

epoll是linux实现的一个基于事件的异步IO库，在之前类似的异步IO库poll上改进而来。

下面的例子会演示如何用epoll将阻塞的IO操改写为异步非阻塞。