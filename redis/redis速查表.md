## 字符串

```bash
# 为键设置值和过期时间
SET key value [EX seconds] 
GET key
# 为键设置新值并返回旧值（原子操作）
GETSET key new - value
# 仅在字符串键尚未有值的情况下，为它设置值（原子操作）
SETNX key val
SETEX key seconds value
# 为键设置值和毫秒级精度的过期时间
PSETEX key milliseconds value 
MSET key value [key value ...]
MGET key [key ...]
# 仅在所有给定字符串键都尚未有值的情况下，为它们设置值
MSETNX key value [key value ...]
# 获取字符串值的撒谎
STRLEN key
SETRANGE key offset value
GETRANGE key start end
APPEND key value
# 为字符串键储存的整数值加一
INCR key
DECR key
INCRBY key increment
DECRBY key decrement
INCRBYFLOAT key increment
```

## 散列

```bash
HSET hash key value
HSETNX hash key value
HGET hash key
HMSET hash key value [key value]
HMGET hash key [KEY ...]
HINCRBY hash key increment
HINCRBYFLOAT hash key increment
HEXISTS hash key
HDEL hash key [key ...]
HKEYS hash
HVALS hash
HGETALL hash
HSCAN hash cursor [MATCH pattern]] [COUNT count]
```

## 列表

```bash
LPUSH list item [item ...]
LPUSHX list item
RPUSH list item [item ...]
RPUSH list item
LPOP list
RPOP list
RPOPLPUSH source_list target_list
LINDEX list index
LLEN list
LRANGE list start end
LINSERT list BEFORE|AFTER target item
LREM list count item
LSET list index item
LTRIM list start end # 对列表进行修剪，只保留指定索引范围内的元素
```

## 集合

```bash
scard set  # 集合包含的元素数量
```



## expire

当 `key` 不存在时，返回 `-2` 。 当 `key` 存在但没有设置剩余生存时间时，返回 `-1` 。 否则，以秒为单位，返回 `key` 的剩余生存时间。

在 Redis 2.8 以前，当 `key` 不存在，或者 `key` 没有设置剩余生存时间时，命令都返回 `-1` 。





## 简单动态字符串

**定义**

```c
struct sdshdr {
  int len;
  int free;
  char buf[];
}
```

**优点**

1. 常数时间复杂度获取字符串长度。
2. 防止缓冲区溢出。
3. 通过空间预分配和惰性空间释放减少内存重分配次数。
4. 二进制安全。
5. 兼容部分C字符串函数。



## 链表

```c
typedef struct listNode {
  struct listNode *prev;
  struct listNode *next;
  void *value;
} listNode;

typedef struct list {
  listNode *head;
  listNode *tail;
  unsigned long len;
  void *(*dup)(void *ptr);
  void *(*free)(void *ptr);
  int (*match)(void *ptr, void *key);
} list;
```

**特性**

1. 双端
2. 无环
3. 带表头和表尾指针
4. 长度计数器
5. 多态。



## 整数集合

整数集合是**集合**键的底层实现之一。

当集合只包含整数元素，并且元素数量不多时。

```c
typedef struct intset {
  uint32_t encoding;
  uint32_t length;
  int8_t contents[];
} intset;
```

整数集合的每个元素都是contents数组的一个数据项，各个项在数据中按值的大小**从小到大**有序地排列，并且数组中**不包含任何重复项**。

contents数组的真正类型取决于encoding属性的值。

encoding为INTSET_ENC_INT16，整数集合底层实现为int16_t类型的数组，集合保存的都是int16_t类型的整数值。



**升级**

添加新元素，并且新元素的类型比整数集合现有所有元素都要长时。

升级要做的是，根据新类型的长度，以及元素的数量，对底层数组进行空间重分配。

**降级**

不支持降级。一旦对数组进行了升级，编码就会一直保持升级后的状态。

## 压缩列表

压缩列表是**列表**键和**哈希**键的底层实现之一。

当列表的元素数目较少，并且每个元素要么是小整数值，要么是短字符串，就会使用压缩列表来做列表键的底层实现。

当哈希键只包含少量键值对，并且每个键和值要么是小整数值，要么是短字符串，就会使用压缩列表来做列表键的底层实现。

压缩列表是为了节约内存而开发，由一系列特殊编码的**连续内存块**组成。每个节点可以保存一个字符数组或者一个整数值。



**数据结构**

```c
zlbytes zltail zllen entry1 entry2 ... entryN zlend
previous_entry_length encoding content
```

previous_entry_length记录了前一个节点的长度，程序可以通过指针运算，根据当前节点的地址计算出前一个节点的起始地址。压缩列表**从表尾向表头**遍历操作就是使用这一原理来实现的。

| 条件                        | previous_entry_length的长度 |
| --------------------------- | --------------------------- |
| 前一节点长度小于254字节     | 1字节                       |
| 前一节点长度大于等于254字节 | 5字节                       |

encoding属性记录了节点保存的数据的类型以及长度。（这里比较复杂，详细了解可参阅<<Redis设计与实现>> )

content属性负责保存节点的值，节点值可以是一个字节数组( "hello world") 或者整数(1009)，值的类型和长度由encoding决定。



**连锁更新**

添加新节点或者删除节点，可能会引发连锁更新操作，但实际操作中出现的几率不高。

出现的条件是：有多个连续的、长度介于250字节到253字节之间的节点e1至eN，再将一个长度大于等于254字节的新节点放在前面时。

e1的previous_entry_length仅为1字节，没办法保存新节点的长度，所以程序对压缩列表执行空间重分配操作 锁更新的最坏复杂度为O(N2)



## 对象

### 结构体定义

```c
typedef struct redisObject {
  unsigned type: 4;
  unsigned encoding: 4;
  void *ptr;
} robj;
```

### 类型

| 类型常量     | 对象名称   |
| ------------ | ---------- |
| REDIS_STRING | 字符串对象 |
| REDIS_LIST   | 列表       |
| REDIS_HASH   | 哈希       |
| REDIS_SET    | 集合       |
| REDIS_ZSET   | 有序集合   |

**TYPE**命令

```bash
rpush alist 1 2 5
TYPE alist  # list
```

### 编码和底层实现

不同类型和编码的对象

| 类型         | 编码                      | 对象                               |
| ------------ | ------------------------- | ---------------------------------- |
| REDIS_STRING | REDIS_ENCODING_INT        |                                    |
| REDIS_STRING | REDIS_ENCODING_EMBSTR     |                                    |
| REDIS_STRING | REDIS_ENCODING_RAW        |                                    |
| REDIS_LIST   | REDIS_ENCODING_ZIPLIST    |                                    |
| REDIS_LIST   | REDIS_ENCODING_LINKEDLIST | 使用双端链表实现的列表对象         |
| REDIS_HASH   | REDIS_ENCODING_ZIPLIST    |                                    |
| REDIS_HASH   | REDIS_ENCODING_HT         | 使用字典实现的哈希对象             |
| REDIS_SET    | REDIS_ENCODING_INTSET     | 使用整数集合实现的集合对象         |
| REDIS_SET    | REDIS_ENCODING_HT         | 使用字典实现的集合对象             |
| REDIS_ZSET   | REDIS_ENCODING_ZIPLIST    |                                    |
| REDIS_ZSET   | REDIS_ENCODING_SKIPLIST   | 使用跳跃表和字典实现的有序集合对象 |

OBJECT ENCODING命令

```bash
set msg "hello world"
OBJECT ENCODING msg
```

| 底层数据结构                  | 编码常量                  | 命令输出   |
| ----------------------------- | ------------------------- | ---------- |
| 整数                          | REDIS_ENCODING_INT        | int        |
| embstr编码的简单动态字符串SDS | REDIS_ENCODING_EMBSTR     | embstr     |
| 简单动态字符串SDS             | REDIS_ENCODING_RAW        | raw        |
| 字典                          | REDIS_ENCODING_HT         | hashtable  |
| 双端链表                      | REDIS_ENCODING_LINKEDLIST | linkedlist |
| 压缩列表                      | REDIS_ENCODING_ZIPLIST    | ziplist    |
| 整数集合                      | REDIS_ENCODING_INTSET     | intset     |
| 跳跃表和字典                  | REDIS_ENCODING_SKIPLIST   | skiplist   |

### 字符串对象

字符串对象的编码可以是int、raw或embstr

**规则**

1. 如果保存的是整数值，并且这个整数值可以用long类型来表示，字符串对象的编码设置为int。
2. 如果保存的是字符串，且字符串值的长度大于39字节，对象编码为raw。
3. 如果保存的是字符串，且字符串值的长度小于等于39字节，对象编码为embstr。

embstr是专门用于保存短字符串的一种优化编码技术。区别是raw编码会调用两次内存分配函数来创建redisObject和sdshdr结构，而embstr只通过一次内存分配函数来分配一块连续的空间，依次包含redisObject结构和sdshdr结构。

| 值                                         | 编码        |
| ------------------------------------------ | ----------- |
| 可以用long类型保存的整数                   | int         |
| 可以用long double类型保存的浮点数          |             |
| 字符串值，但长度太大没办法用long表示的整数 | embstr或raw |

