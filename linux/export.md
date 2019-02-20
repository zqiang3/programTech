## Introduction

是bash shell内建的命令之一。export命令使用起来非常简单，因为它只有三个命令选项，语法简单直接。

子进程并不继承父进程的变量。这就是export命令的来由，可以在父子进程间共享环境变量。

export命令的作用是，在创建一个新的子进程时，保证父进程中export的变量在子进程中有效。

除了init进程，任何进程都可以是父进程，又同时是子进程。

## Using export command

```bash
export 
export MYVAR=10
export PATH=$PATH:/usr/local/bin
```

## Frequently Used Options

- **-p**
  List of all names that are exported in the current shell
- **-n**
  Remove names from export list
- **-f**
  Names are exported as functions

## 环境变量

显示所有环境变量 env
env | grep TEST
unset $TEST
env | grep TEST
readonly TEST 将环境变量设置为只读

export声明的变量中关闭shell时失效

设置环境变量的三种方法
在/etc/profile文件中添加变量 对所有用户永久生效
export CLASSPATH=./JAVA_HOME/lib;
修改文件后马上生效 source /etc/profile

在~/.bash_profile中增加变量 对当前用户永久生效