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