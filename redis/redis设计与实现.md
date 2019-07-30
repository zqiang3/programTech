# 第2章 简单动态字符串

redis是使用标准c编写的key-value数据库，但是redis中的字符串与标准c的字符串类型并不一样，redis使用了一种**简单动态字符串**的抽象类型，我们将它称为SDS

SDS除了可以保存字符串外，SDS还被用作AOF模块中的AOF缓冲区。

SDS的结构

```c
struct sdshdr {
    // buf中已占用空间的长度
    int len;
    // buf中剩余可用空间的长度
    int free;
    
    // 数据空间
    char buf[];
}
```

**与c字符串的区别**

1. 获取字符串长度: SDS O(1) / C O(n)
2. api不安全，c字符串容易产生缓冲区溢出；api安全，SDS在修改数据之前，会先检查空间是否足够，不够会先拓展空间，再执行操作
3. SDS采用内存预分配策略，修改字符串长度N次需要执行N次内存重分配；最多执行N次内存重分配
4. SDS采用惰性空间释放
5. 二进制安全，c字符采用0字符标识末尾，因此不能保存图片，音视频，压缩文件，SDS采用len记录长度，不存在这种问题，因此可以保存各种各样的格式。
6. SDS仍保留了以空字符结尾的惯例。

c字符串除了末尾之外，不能包含空字符，这种限制使得c字符串只能保存文本数据，而不能保存像图片、音频、视频、压缩文件这样的二进制数据。

redis的SDS的API都会以二进制的方式来处理存放在buf数组里的数据，因此把SDS的buf属性称为**字节数组**，可以用它来保存一系列二进制数据。SDS使用len属性的值而不是空字符来判断字符串是否结束。

## 底层数据结构的类型

1. 简单动态字符串
2. 链表
3. 字典
4. 跳跃表
5. 整数集合
6. 压缩列表
7. 对象

## 链表

链表在redis中的应用非常广泛，比如列表键的底层实现之一就是链表。

每个链表节点使用一个listNode结构表示

```c
typedef struct listNode {
    struct listNode *prev;
    struct listNode *next;
    void *value;
}
```

双端链表

```c
typedef struct list {
    listNode *head;
    listNode *tail;
    unsigned long len;
    void *(*dup) (void *ptr);
    void (*free) (void *ptr);
    int (*match) (void *ptr, void *key);
}
```

无环的双端链表

特点：

* 双端，带有prev和next指针
* 无环，表头节点的 prev 指针和表尾节点的next 都指向NULL
* 有表头和表尾指针
* 保存了链表长度
* 多态：链表节点使用void*指针来保存节点值，并且可以通过list结构的dup、free、match三个属性为节点值设置类型特定函数



# 第4章 字典

**字典**

```c
typedef struct dict {
    // 类型特定函数
    dictType *type;
    // 私有数据
    void *privedata;
    // 哈希表
    dictht ht[2];
    // rehash索引
    int rehashidx;
}
```



哈希表**

```c
typedef struct dictht {
    // 哈希表数组
    dictEntry **table;
    // 哈希表大小
    unsigned long size;
    
    // 哈希表大小掩码，用于计算索引值
    unsigned long sizemask;
    // 已有节点的数量
    unsigned long used;
    
}
```

**哈希表节点**

```c
typedef struct dictEntry {
    void *key;
    
    union {
        void *val;
        uint64_t u64;
        int64_t s64;
    } v;
    
    struct dictEntry *next;
} dictEntry;
```

next属性可以将多个哈希值相同的键值对连接在一起，以此来解决键冲突的问题。

redis使用链地址法来解决哈希冲突。在插入一条新的数据时，会进行哈希值的计算，如果出现了hash值相同的情况，redis采用了链地址法来解决冲突。每个哈希表节点都有一个next指针，多个节点可以使用next构成一个单向链表，被分配到同一索引上的多个节点可使用这个单向链表连接起来（表头插入）。

链地址法：将哈希地址相同的元素构成一个链表，将链表的头指针放在哈希表的第i个单元。

哈希桶：

负载因子：

**rehash**

随着对哈希表的不断操作，哈希表保存的键值对会逐渐的发生改变，为了让哈希表的负载因子维持在一个合理的范围之内，我们需要对哈希表的大小进行相应的扩展或者压缩，这时候，我们可以通过 rehash（重新散列）操作来完成。



### serverCron

* 更新服务器的各类统计信息，比如时间、内存占用、数据库占用情况等
* 清理数据库中的过期键值对
* 对不合理的数据库进行大小调整
* 关闭和清理连接失效的客户端
* 尝试进行 AOF 或 RDB 持久化操作
* 如果服务器是主节点的话，对附属节点进行定期同步
* 如果处于集群模式的话，对集群进行定期同步和连接测试

Redis 将 `serverCron` 作为时间事件来运行， 从而确保它每隔一段时间就会自动运行一次， 又因为  `serverCron` 需要在 Redis 服务器运行期间一直定期运行， 所以它是一个循环时间事件：  `serverCron` 会一直定期执行，直到服务器关闭为止。

这个定时任务中会调用activeExpireCycle函数，针对每个db在限制的时间REDIS_EXPIRELOOKUPS_TIME_LIMIT内迟可能多的删除过期key，之所以要限制时间是为了防止过长时间 的阻塞影响redis的正常运行。这种主动删除策略弥补了被动删除策略在内存上的不友好。 被动删除策略对内存是不友好的，因为可能有些过期的键永远不再使用但一直占据内存。定时删除对内存友好但对CPU不友好，有可能会大量占用CPU。