# link

https://github.com/go-redis/redis



## 使用

使用过程中需要避免一定的坑，目的是节省内存和防止慢查询

与memcached的区别，数据可以持久化





## ttl

```
ttl key
# -1  表示key永不过期
ttl key
# -2  表示key不存在
```

