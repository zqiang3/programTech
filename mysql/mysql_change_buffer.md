## 缓冲池中的页，什么时候刷到磁盘？

定期刷磁盘

## change buffer解决什么问题

写优化

对页进行写操作，并不会立刻从磁盘加载数据到缓冲池，而仅仅记录数据变更，等到未来数据需要被读取时，再合并数据结果



## change buffer与buffer pool区别

buffer pool是优化读磁盘性能，change buffer是优化写磁盘性能



## 是否会出现一致性问题呢？

