```bash
pgrep -fl supervisor
```



Linux grep命令用于查找文件里符合条件的字符串。

grep指令用于查找内容包含指定的范本样式的文件，如果发现某文件的内容符合所指定的范本样式，预设grep指令会把含有范本样式的那一列显示出来。若不指定任何文件名称，或是所给予的文件名为"-"，则grep指令会从标准输入设备读取数据。



## 参数说明

-c

-C <显示行数>: 除了显示符合样式的那一行之外，并显示该行之前的内容



## example

```bash
grep -r pattern dir/   # 递归搜索
grep -i pattern file   # 忽略大小写
```

