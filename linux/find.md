find 查找目录 -name 文件名



在某个路径下查找所有包含“hello abcserver”字符串的文件。

```bash
find . -name “*.py” | xargs grep “hello world”
```

-print： find命令将匹配的文件输出到标准输出