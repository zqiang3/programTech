# 第2章 简单动态字符串

## 二进制安全

c字符串除了末尾之外，不能包含空字符，这种限制使得c字符串只能保存文本数据，而不能保存像图片、音频、视频、压缩文件这样的二进制数据。

redis的SDS的API都会以二进制的方式来处理存放在buf数组里的数据，因此把SDS的buf属性称为字节数组，可以用它来保存一系列二进制数据。SDS使用len属性的值而不是空字符来判断字符串是否结束。

# 第4章 字典

## 哈希表节点

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

redis使用链地址法来解决键冲突。