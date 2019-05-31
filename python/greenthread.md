## 什么是greenthread？

> Green threads emulate multi-threaded environment without relying on any native OS capabilities, and they are managed in user space instead of kernel space, enabling them to work in environments that do not have native thread support.



由于全局解释器锁(GIL)的存在，python一次只运行一个线程。

### 一个进程可以支持多少greenlets？

**开销**

常规线程仍然具有较高的上下文切换开销，greenlets没有这些相关的开销。基于gevent的服务器可以spawn上千个greenlets，wigh almost no overhead. 即使阻塞某些greenlets，也不会影响服务器接收新请求的能力，并发连接数实际上是无限的。

> While threads are cheap compared to processes (forks), they are still expensive to create for each new connection.
>
> Greenlets behave similar to traditional threads, but are very cheap to create. 

## spawn

> Execution control returns immediately to the caller; the created greenthread is merely scheduled to be run at the next available opportunity.

从源码注释可以看出，绿线程在spwan后只是加入到调度队列，真正运行要等到合适的时机。