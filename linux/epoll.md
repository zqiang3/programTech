## link

https://zhuanlan.zhihu.com/p/36764771

https://blog.csdn.net/libaineu2004/article/details/70197825



## 同步阻塞概念

内核为IO设计了内核缓冲区

缓冲区满、缓冲区空、缓冲区非满、缓冲区非空

**阻塞I/O**

在阻塞I/O模式下，一个线程只能处理一个流的I/O事件。如果要处理多个流，要么多开进程，要么多开线程，这两种方式都会带来额外的开销

**非阻塞忙轮询**

不停地把所有流都从头到尾问一遍，如果有I/O事件，就处理，如果没有，再从头开始。这样可以处理多个流了，但非常浪费CPU。

**非阻塞轮询**

我们使用select 或 poll这样的代理

如果没有IO事件，就阻塞，有I/O事件，就唤醒线程，然后程序轮询一遍所有的流，找到有事件的流进行处理

```go
while true {
  select(streams[])
  for i in streams[] {
    if i hasdata
    read until unavailabel
  }
}
```

使用select 时间复杂度是O(N)

## epoll

### epoll讲解

epoll与select的区别，在于不需要轮询。epoll会把哪个流发生怎样的I/O事件通知线程，线程收到通知，直接处理相应的流就可以了。时间复杂度是O(k), k是产生I/O的流的个数

epoll_create创建一个epoll对象

epoll_ctl(epoll_add/epoll_del)，往epoll对象增加/删除某个流的某个事件

```
epoll_ctl(epollfd, EPOLL_CTL_ADD, socket, EPOLLIN);//有缓冲区内有数据时epoll_wait返回
epoll_ctl(epollfd, EPOLL_CTL_DEL, socket, EPOLLOUT);//缓冲区可写入时epoll_wait返回
```

epoll_wait(epollfd, ...) 等待直到注册的事件发生

一个epoll模式的代码大概是这个样子

```
while true {
	active_stream[] = epoll_wait(epollfd)
	for i in active_stream[] {
		read or write until unavailable
	}
}
```

### 触发方式

**epoll边缘触发和水平触发的区别**

边缘触发是高速工作模式，新的事件到来，可以从epoll_wait调用中获取事件，但如果缓冲区数据没处理完，并且没有新的事件到来，从epoll_wait不能获取到事件。水平触发刚好相反，只要缓冲区数据没处理完，就可以通过epoll_wait获取到事件。

### 数据结构

红黑树