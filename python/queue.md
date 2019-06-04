## Queue

Queue是python标准库中的线程安全的队列（FIFO）实现,提供了一个适用于多线程编程的先进先出的数据结构，即队列，用来在生产者和消费者线程之间的信息传递



## Reference

```python
class Queue.Queue(maxsize=0)          # FIFO
class Queue.LifoQueue(maxsize=0)      # LIFO
class Queue.PriorityQueue(maxsize=0)  # priority queue
```

## Queue Objects

```
Queue.put(item[, block][, timeout])
/* Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. */
Queue.get(item[, block][, timeout])
/* Remove and return an item from the queue. If optional args block is true and timeout is None (the default), block if necessary until an item is available. */
```

