## NAME
find -- walk a file hierarchy

## DESCRIPTION

The find utility recursively descends the directory tree for each path listed, evaluating an expression (composed of the ``primaries'' and ``operands'' listed below) in terms of each file in the tree.

## SYNOPSIS   

```bash
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
```



在某个路径下查找所有包含“hello abcserver”字符串的文件。

```bash
find . -name “*.py” | xargs grep “hello world”

# 将目前目录及其子目录下所有延伸档名是 c 的文件列出来。
find . -name "*.c"

# 将目前目录其其下子目录中所有一般文件列出
find . -type f

# 将目前目录及其子目录下所有最近 20 天内更新过的文件列出
find .-ctime -20

# 查找/var/log目录中更改时间在7日以前的普通文件，并在删除之前询问它们：
find /var/log -type f -mtime +7 -ok rm {} \;

# 查找前目录中文件属主具有读、写权限，并且文件所属组的用户和其他用户具有读权限的文件：
find . -type f -perm 644 -exec ls -l {} \;

# 为了查找系统中所有文件长度为0的普通文件，并列出它们的完整路径：
find / -type f -size 0 -exec ls -l {} \;
```

-print： find命令将匹配的文件输出到标准输出