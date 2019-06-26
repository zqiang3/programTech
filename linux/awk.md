## introduction

awk是Linux系统下强大的文本分析工具，相对于grep的查找、sed的编辑，awk在对数据分析并生成报告方面非常强大。它把文件逐行读入，以空格为默认分隔符（也可以任意字符作分隔符）将每行切片，再对切片各部分进行分析和处理，可进行脚本式编程。

## 例子：分析Access文件 

```bash
awk -F',' '{print $5}' nginx_access.log | sort | uniq -c | sort -nr

ps -aux |grep 10001 |awk print > file. ?

ps -ef |grep -a mobilelink|grep -v grep|awk '{print $2}'

last -10 | awk '{print $0}'

```

