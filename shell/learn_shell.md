



## ref

| $0   | 当前脚本的文件名                                             |
| ---- | ------------------------------------------------------------ |
| $n   | 传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。 |
| $#   | 传递给脚本或函数的参数个数。                                 |
| $*   | 传递给脚本或函数的所有参数。                                 |
| $@   | 传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。 |
| $?   | 上个命令的退出状态，或函数的返回值。                         |
| $$   | 当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID。 |



| 运算符 | 说明                                 |
| ------ | ------------------------------------ |
| =      | 两个字符串是否相等                   |
| !=     | 是否不相等                           |
| -z     | 检测字符串长度是否为0，为0返回true   |
| -n     | 检测字符串长度是否为0，不为0返回true |
| str    | 检测字符串是否为空，不为空返回true   |



## 快速入门

**变量赋值**

等号两边不能有空格

```bash
# 在控制台打印变量的值
echo $variable 或者 ${variable}

# 清除变量
unset variable

# 如何把一个命令的输出赋值给一个变量
` ` 这个叫飘号
A=``里面放命令，就是把这个命令输出的结果赋值给a

# 环境变量
环境变量简称全局变量，按照惯例需要大写
export VAR
注意，可以被所有的shell访问

# 位置参数
```



cat /etc/shells
echo $SHELL

chsh -s 修改的就是/etc/passwd文件中和我们所登录的用户名相对应的那一行

## 第一个shell脚本

```shell
!/bin/bash

echo 'hello, world'
```



运行shell脚本
chmod +x test.sh  # 使脚本具有可执行权限
./test.sh

注意，一定要写成./test.sh，而不是test.sh，运行其它二进制的程序也一样，直接写test.sh，linux系统会去PATH里寻找有没有叫test.sh的，而只有/bin, /sbin, /usr/bin，/usr/sbin等在PATH里，你的当前目录通常不在PATH里，所以写成test.sh是会找不到命令的，要用./test.sh告诉系统说，就在当前目录找。

2、作为解释器参数
这种运行方式是，直接运行解释器，其参数就是shell脚本的文件名，如：
/bin/sh test.sh
/bin/php test.php



## 语法

```bash
# 注释
# 以#开头的行就是注释
# echo
echo "hello world"
# 变量
NAME="ZQ"      # 等号两边不能有空格
echo ${NAME}   # 大括号是可选的
readonly NAME  # 只读
unset NAME     # 删除变量，不能删除只读变量
# 变量类型
局部变量、环境变量、shell变量
# 字符串
str='this is a string'
str="hello, I know you are \"$your_name\"!"  # 双引号里可以有变量，可以出现转义字符
greeting="hello, "$your_name" !"             # 字符串拼接
echo ${#str}  # 输出字符串长度
# 数组
数组名=(值1 值2 ... 值n)  # 定义数组
echo ${数组名[下标]}      # 读取数组
echo ${array_name[@]}   # 读取数组所有元素
length=${#array_name[@]}  # 获取数组长度
length=${#array_name[*]}
```



## 变量

### 定义变量

定义变量时，变量名不加美元符号

```bash
your_name="qinjx"
```

注意，变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。

```bash
r=${a-b}   # 当变量a为null时var=b
r=${a:-b}  # 当变量a为null或为空字符串时var=b
r=${1:-b}  # 当第一个参数为null或为空字符串时var=b
```

### 使用变量

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：

```
your_name="qinjx"
echo $your_name
echo ${your_name}
```

如果变量与其他字符相连的话，需要使用大括号`{}`

推荐给所有变量加上花括号，这是个好的编程习惯。IntelliJ IDEA编写shell script时，IDE就会提示加花括号。

## 字符串

字符串可以用单引号，也可以用双引号，也可以不用引号。

###单引号的限制

单引号里的任何字符都会**原样输出**，单引号字符串中的变量是无效的；单引号字符串中不能出现单引号。

###双引号的优点

双引号里可以有变量，双引号里可以出现转义字符

### 获取字符串长度

```shell 
string="abcd"
echo ${#string}  # 输出4
```

### 提取子字符串

```shell
string="aibaba is nb"
echo ${string:1:4}  # 输出 liba
```

## shell展开

link: https://www.jianshu.com/p/403f3554e2c1

## printf

```shell
printf "%d %s\n" 1 "abc"  # arguments 使用空格分隔，不用逗号。
printf '%d %s\n' 1 "abc"  # 单引号与双引号效果一样
printf %s abcde  # 没有引号也可以输出
printf %s abc def # 参数多于格式控制符时，format-string可以被重用
printf "%s and %d \n"  # 如果没有 arguments，那么 %s 用 NULL 代替，%d 用0代替
```



## 数组

```shell
array_name=(value0 value1 value2)  # 定义数组

# 或者
array_name=( value0
value1
value2
value3 )

# 还可以单独定义数组的各个分量
array_name[0]=value0 
array_name[1]=value1 
array_name[2]=value2

# 读取数组元素
valuen=${array_name[2]}

# 使用@或*可以获取数组中的所有元素
${array_name[*]}
${array_name[@]}

# 取得数组元素的个数
length=${#array_name[@]} 
# 或者
length=${#array_name[*]} 
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```



##Shell 条件语句

if 语句通过关系运算符判断表达式的真假来决定执行哪个分支。Shell 有三种 if ... else 语句：

- if ... fi 语句；
- if ... else ... fi 语句；
- if ... elif ... else ... fi 语句。

### if ... else 语句

if ... else 语句的语法：

```
if [ expression ]
then
   Statement(s) to be executed if expression is true
fi
```

最后必须以 fi 来结尾闭合 if，fi 就是 if 倒过来拼写，后面也会遇见。

注意：expression 和方括号([ ])之间必须有空格，否则会有语法错误。

举个例子：

```
#!/bin/sh

a=10
b=20

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi
```

### if ... else ... fi 语句

```shell
if [ expression ] 
then
Statement(s) to be executed if expression is true 
else
Statement(s) to be executed if expression is not true 
fi
```

### if ... elif ... fi语句

```shell
if [ expression 1 ] 
then
Statement(s) to be executed if expression 1 is true 
elif [ expression 2 ]
then
Statement(s) to be executed if expression 2 is true 
elif [ expression 3 ]
then
Statement(s) to be executed if expression 3 is true 
else
Statement(s) to be executed if no expression is true 
fi
```

## test

test 命令用于检查某个条件是否成立，与方括号([ ])类似。

```shell
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2] 
then
echo 'The two numbers are equal!' 
else
echo 'The two numbers are not equal!' 
fi
```



## for

for循环一般格式为

```shell
for 变量 in 列表
do 
	command1
	command2
	...
	commandN
done
	
```

## while

```shell
COUNTER=0
while [ $COUNTER -lt 5 ] 
do
COUNTER='expr $COUNTER+1'
echo $COUNTER 
done
```



while 循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按结束循环。



```shell
echo 'type <CTRL-D> to terminate' 
echo -n 'enter your most liked film: ' 
while read FILM
do
echo "Yeah! great film the $FILM" 
done
```

## 函数

定义

```bash
function function_name() {
	list of commands
	[return value]
}
```

函数返回值，可以显式增加 return 语句;如果不加，会将最后一条命令运行结果作为返回值。

hell 函数返回值只能是整数



example

```shell
#!/bin/bash
# Define your function here
Hello () {
	echo "Url is http://see.xidian.edu.cn/cpp/shell/"
}
# Invoke your function
Hello
```

调用函数只需要给出函数名，不需要加括号。

函数返回值在调用该函数后通过 $? 来获得

像删除变量一样，删除函数也可以使用 unset 命令，不过要加上 .f 选项

## 注释

以`#`开头的行就是注释，会被解释器忽略

## 链接

https://juejin.im/post/59f92f22f265da43356212a8

## 2.4.1 程序执行

Shell负责执行你在终端中指定的所有程序。每次输入一行内容，Shell就会分析该行，然后决定执行什么操作。就Shell而言，每一行都遵循以下基本格式：

```bash
program-name arguments
```



Shell使用一些特殊字符来确定程序名称及每个参数的起止。这些字符统称为空白字符（whitespace characters），它们包括空格符、水平制表符和行尾符（更正式的叫法是换行符）。连续的多个空白字符会被Shell忽略。



## 2.4.2 I/O重定向

```bash
echo Remember to record > reminder
```

Shell会识别出特殊的输出重定向字符`>`，然后将命令行中的下一个单词作为输出重定向所指向的文件名。在本例中，这个文件名为`reminder`。如果`reminder`已经存在且用户具有写权限，那么文件中已有的内容会被覆盖掉。如果没有该文件或其所在目录的写权限，Shell会产生错误信息。

```bash
$ wc -l users
      5 users
$ wc -l < users
      5
$
```

在第一个例子中，Shell解析命令行，确定要执行的程序名称是`wc`并为其传入两个参数：`-l`和`users`

当`wc`执行时，会看到传入的两个参数。第一个参数是`-l`，告诉它需要统计行数。第二个参数指定了待统计行数的文件。因此`wc`会打开文件`users`，统计行数，然后打印出结果及对应的文件名。

第二个例子中的`wc`操作略有不同。Shell在扫描命令行时发现了输入重定向字符`<`，其后的单词就被解释成从中重定向输入的文件名。从命令行中提取出了“`< users`”之后，Shell就开始执行`wc`程序，将其标准输入重定向为文件`users`并传入单个参数`-l`

这次当`wc`执行时，它会看到传入的单个参数`-l`。因为没有指定文件名，`wc`会转而去统计标准输入中内容的行数。因此`wc -l`在统计行数时，并不知道它实际上是在对文件`users`进行统计。最后的显示结果和平时一样，但是缺少了文件名，因为我们并没有为`wc`指定。

要理解两条命令在执行上的不同，这一点非常重要。

## 2.4.4 管道

```bash
who | wc -l
```

Shell在扫描命令行时，除了重定向符号之外还会查找管道字符|。每找到一个，就会将之前命令的标准输出连接到之后命令的标准输入，然后执行这两个命令。

Shell会查找分隔了命令`who`和`wc`的管道符号。它将上一个命令的标准输出连接到下一个命令的标准输入，然后执行两者。`who`命令执行时会生成已登录用户列表并将结果写入标准输出，它并不知道输出内容并没有出现在终端而是进入了另一个命令。

当`wc`命令执行时，它发现并没有指定文件名，因此就对标准输入内容进行统计，并没有意识到标准输入并非来自终端，而是来自于`who`命令的输出。

管道中并不仅限于有两条命令，你可以在复杂的管道中将3条、4条、5条甚至更多的命令串联在一起。这多少有点不好理解，但却是UNIX系统强大威力的所在。

## 2.4.6 解释型编程语言

Shell有自己内建的编程语言。这种语言是解释型的，也就是说，Shell会分析所遇到的每一条语句，然后执行所发现的有效的命令。这与C++及Swift这类编程语言不同，在这些语言中，程序语句在执行之前通常会被编译成可由机器执行的形式。

相较于编译型语言，由解释型语言所编写的程序一般要更易于调试和修改。然而，所花费的时间要比实现相同功能的编译型语言程序更长。

