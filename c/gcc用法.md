## 基本用法 
gcc -c test.c
gcc -o hello test.o

gcc又是一个交叉平台编译器
.c C原始程序
.i 已经过预处理的c原始程序
.s/.S 汇编语言原始程序
.h  预处理文件
.o 目标文件
.a/.so 编译后的库文件

## 准备文件

main.c

```c
#include "hello.h"

int main(void)
{
    hello();
    return 0;
}
```

hello.h

```c
#ifndef HELLO
#define HELLO
void hello();

#endif
```

hello.c

```c
#include <stdio.h>

void hello()
{
    printf("hello, world\n");
}
```

假设我们一共有三个文件：main.c,hello.c和hello.h. 其中hello.c中有一个打印HelloWorld的程序并在.h文件中声明，main.c通过包含.h文件调用打印HelloWorld程序。

## 一次编译多个文件

```sh
gcc main.chello.c -o hello
```

## 分别编译和链接

```sh
gcc -c main.c
gcc -c hello.c
gcc main.o hello.o -o hello
```

除了生成一个可执行文件hello外，还会生成两个中间文件main.o和hello.o



## -w -W -Wall

https://blog.csdn.net/m7548352/article/details/49520069




# gcc的编译流程
分为四个步骤
预处理、编译、汇编、链接


（1）预处理阶段

在该阶段，编译器将上述代码中的stdio.h编译进来，并且用户可以使用Gcc的选项”-E”进行查看，该选项的作用是让Gcc在预处理结束后停止编译过程。
gcc指令的一般格式为 gcc [选项] 要编译的文件 [选项] 目标文件

gcc -E hello.c -o hello.i

gcc确实进行了预处理，它把stdio.h的内容插入到hello.i文件中

（2）编译阶段

接下来进行的是编译阶段，在这个阶段中，Gcc首先要检查代码的规范性、是否有语法错误等，以确定代码的实际要做的工作，在检查无误后，Gcc把代码翻译成汇编语言。用户可以使用”-S”选项来进行查看，该选项只进行编译而不进行汇编，生成汇编代码。


（3）汇编阶段

汇编阶段是把编译阶段生成的”.s”文件转成目标文件，读者在此可使用选项”-c”就可看到汇编代码已转化为”.o”的二进制目标代码了、


（4）链接阶段

在成功编译之后，就进入了链接阶段。在这里涉及到一个重要的概念：函数库。

读者可以重新查看这个小程序，在这个程序中并没有定义”printf”的函数实现，且在预编译中包含进的”stdio.h”中也只有该函数的声明，而没有定义函数的实现，那么，是在哪里实现”printf”函数的呢？最后的答案是：系统把这些函数实现都被做到名为libc.so.6的库文件中去了，在没有特别指定时，Gcc会到系统默认的搜索路径”/usr/lib”下进行查找，也就是链接到libc.so.6库函数中去，这样就能实现函数”printf”了，而这也就是链接的作用。

函数库一般分为静态库和动态库两种。静态库是指编译链接时，把库文件的代码全部加入到可执行文件中，因此生成的文件比较大，但在运行时也就不再需要库文件了。其后缀名一般为”.a”。动态库与之相反，在编译链接时并没有把库文件的代码加入到可执行文件中，而是在程序执行时由运行时链接文件加载库，这样可以节省系统的开销。动态库一般后缀名为”.so”，如前面所述的libc.so.6就是动态库。Gcc在编译时默认使用动态库。



# Gcc总体选项列表

-c

只是编译不链接，生成目标文件“.o”

-S

只是编译不汇编，生成汇编代码

-E

只进行预编译，不做其他处理

-g

在可执行程序中包含标准调试信息

-o file

把输出文件输出到file里

-v

打印出编译器内部编译各过程的命令行信息和编译器的版本

-I dir

在头文件的搜索路径列表中添加dir目录

-L dir

在库文件的搜索路径列表中添加dir目录

-static

链接静态库

-llibrary

连接名为library的库文件


对于“-c”、“-E”、“-o”、“-S”选项在前一小节中已经讲解了其使用方法，在此主要讲解另外两个非常常用的库依赖选项“-I dir”和“-L dir”。

· “-I dir”

正如上表中所述，“-I dir”选项可以在头文件的搜索路径列表中添加dir目录。由于Linux中头文件都默认放到了“/usr/include/”目录下，因此，当用户希望添加放置在其他位置的头文件时，就可以通过“-I dir”选项来指定，这样，Gcc就会到相应的位置查找对应的目录。
这样，就可在Gcc命令行中加入“-I”选项：

 

[root@localhost Gcc] Gcc hello1.c –I /root/workplace/Gcc/ -o hello1


这样，Gcc就能够执行出正确结果。

 

小知识

在include语句中，“<>”表示在标准路径中搜索头文件，““””表示在本目录中搜索。故在上例中，可把hello1.c的“#include<my.h>”改为“#include “my.h””，就不需要加上“-I”选项了。

 

· “-L dir”

选项“-L dir”的功能与“-I dir”类似，能够在库文件的搜索路径列表中添加dir目录。例如有程序hello_sq.c需要用到目录“/root/workplace/Gcc/lib”下的一个动态库libsunq.so，则只需键入如下命令即可：

 

[root@localhost Gcc] Gcc hello_sq.c –L /root/workplace/Gcc/lib –lsunq –o hello_sq

 

需要注意的是，“-I dir”和“-L dir”都只是指定了路径，而没有指定文件，因此不能在路径中包含文件名。

另外值得详细解释一下的是“-l”选项，它指示Gcc去连接库文件libsunq.so。由于在Linux下的库文件命名时有一个规定：必须以lib三个字母开头。因此在用-l选项指定链接的库文件名时可以省去lib三个字母。也就是说Gcc在对”-lsunq”进行处理时，会自动去链接名为libsunq.so的文件。