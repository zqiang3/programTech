

## Link

https://coolshell.cn/articles/9070.html



## DESCRIPTION

Awk scans each input file for lines that match any of a set of patterns specified
       literally in prog or in one or more files specified as -f  progfile.   With  each
       pattern there can be an associated action that will be performed when a line of a
       file matches the pattern.  Each line is matched against the  pattern  portion  of
       every  pattern-action  statement;  the  associated  action  is performed for each
       matched pattern.  The file name - means the standard input.  Any file of the form
       var=value  is  treated  as  an assignment, not a filename, and is executed at the
       time it would have been opened if it were a filename.  The option -v followed  by
       var=value  is  an assignment to be done before prog is executed; any number of -v
       options may be present.  The -F fs option defines the input field separator to be
       the regular expression fs.





## introduction

awk是Linux系统下强大的文本分析工具，相对于grep的查找、sed的编辑，awk在对数据分析并生成报告方面非常强大。它把文件逐行读入，以空格为默认分隔符（也可以任意字符作分隔符）将每行切片，再对切片各部分进行分析和处理，可进行脚本式编程。

awk逐行处理文本，安装指定的分隔符，将行分割为多个字段，如果没有指定分隔符，默认以空格为分隔符，每个字段按照顺序，分别对应到awk的内置变量中，比如，分割完后的第一个字段为![1,第二个字段为](https://math.jianshu.com/math?formula=1%2C%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%AD%97%E6%AE%B5%E4%B8%BA)2，以此类推，用$0表示当前处理的整个一行。



## Usage

```bash
awk  [options]  'Pattern{Action}' file
awk '条件1 {动作 1} 条件 2 {动作 2} …' 文件名


  这里的action最常用的是： print 和 printf。


awk是逐行处理文本的。
```



## ACTION

An action is a sequence of statements.  A statement can be one of the following:

              if( expression ) statement [ else statement ]
              while( expression ) statement
              for( expression ; expression ; expression ) statement
              for( var in array ) statement
              do statement while( expression )
              break
              continue
              { [ statement ... ] }
              expression              # commonly var = expression
              print [ expression-list ] [ > expression ]
              printf format [ , expression-list ] [ > expression ]
              return [ expression ]
              next                    # skip remaining patterns on this input line
              nextfile                # skip rest of this file, open next, start at top
              delete array[ expression ]# delete an array element
              delete array            # delete all elements of array
              exit [ expression ]     # exit immediately; status is expression


## EXAMPLES




     
     
     
     length($0) > 72
                  Print lines longer than 72 characters.  
      { print $2, $1 }
              Print first two fields in opposite order.
    
       BEGIN { FS = ",[ \t]*|[ \t]+" }
             { print $2, $1 }
              Same, with input fields separated by comma and/or blanks and tabs.
    
            { s += $1 }
       END  { print "sum is", s, " average is", s/NR }
              Add up first column, print sum and average.
    
       /start/, /stop/
              Print all lines between start/stop pairs.
    
       BEGIN     {    # Simulate echo(1)
            for (i = 1; i < ARGC; i++) printf "%s ", ARGV[i]
            printf "\n"
            exit }
##  内置变量

- $0 代表一整行
- $N 代表第 N 个字段
- NF 每一行拥有的 **字段** 数量
- NR 当前所处的行数
- FS 目前的分割字符，默认为空格键或 Tab 键
- OFS 输出的字段分割符号，默认为空格
- RS 记录分割符，默认为换行符
- ORS 输出的记录分割符，默认为换行符
- FILENAME 当前输入文件的名字

## 示例

```bash
 1. awk  '{print}' testfile 

   把testfile文件中的内容输出。


   2. awk  '{print  $1,$2}' testfile


   ps -aux | grep warehouseMS.jar  |  awk 'NR==1{print $2}' 

   取出文件中的某一行：  NR==行号

   例如： 获取testfile文件的第一行的第二列

   ps -aux | grep warehouseMS.jar  |  awk 'NR==1{print $2}' 
```



## 例子：分析Access文件 

```bash
awk -F',' '{print $5}' nginx_access.log | sort | uniq -c | sort -nr

ps -aux |grep 10001 |awk print > file. ?

ps -ef |grep -a mobilelink|grep -v grep|awk '{print $2}'

last -10 | awk '{print $0}'

```

