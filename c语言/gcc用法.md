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