## 链接

<https://blog.csdn.net/violet_echo_0908/article/details/52056071>

## 作用

**在当前bash环境下读取并执行file中的命令**

## 命令用法

```bash
source FileName
```

在当前bash环境下读取并执行FileName中的命令

source命令（从 C Shell 而来）是bash shell的内置命令。点命令，就是个点符号，（从Bourne Shell而来）是source的另一名称。

source（或点）命令通常用于重新执行刚修改的初始化文档，如 .bash_profile 和 .profile 等等。

例如，假如在登录后对 .bash_profile 中的 EDITER 和 TERM 变量做了修改，则能够用source命令重新执行 .bash_profile 中的命令而不用注销并重新登录。比如您在一个脚本里`export $KKK=111` ,假如您用./a.sh执行该脚本，执行完毕后，您运行 `echo $KKK`，发现没有值，假如您用source来执行 ，然后再echo，就会发现KKK=111。因为调用./a.sh来执行shell是在一个子shell里运行的，所以执行后，结构并没有反应到父shell里，但是source不同他就是在本shell中执行的，所以能够看到结果。



## source的妙用

在编译核心时，常常要反复输入一长串命令，如

```bash
make mrproper
make menuconfig
make dep
make clean
make bzImage
```

这些命令既长，又繁琐。而且有时候容易输错，浪费你的时间和精力。如果把这些命令做成一个文件，让它自动按顺序执行，对于需要多次反复编译核心的用户来说，会很方便。

用source命令可以办到这一点。它的作用就是把一个文件的内容当成是shell来执行。

先在/usr/src/linux-2.4.20目录下建立一个文件，取名为make_command，在其中输入如下内容：

```bash
make mrproper &&
make menuconfig &&
make dep &&
make clean &&
make bzImage &&
make modules &&
make modules_install &&
cp arch/i386/boot/bzImge /boot/vmlinuz_new &&
cp System.map /boot &&
vi /etc/lilo.conf &&
lilo -v
```

shell编程中的命令有时和C语言是一样的。&&表示与，||表示或。把两个命令用&&联接起来，如 make mrproper && make menuconfig，表示要第一个命令执行成功才能执行第二个命令。对执行顺序有要求的命令能保证一旦有错误发生，下面的命令不会盲目地继续执行。

文件建立好之后，以后每次编译核心，只需要在/usr/src/linux-2.4.20下输入source make_command 就行了。这个文件也完全可以做成脚本，只需稍加改动即可。

## source filename 与 sh filename 及./filename执行脚本的区别
当shell脚本具有可执行权限时，用sh filename与./filename执行脚本是没有区别得。./filename是因为当前目录没有在PATH中，所有”.”是用来表示当前目录的。
sh filename 重新建立一个子shell，在子shell中执行脚本里面的语句，该子shell继承父shell的环境变量，但子shell新建的、改变的变量不会被带回父shell。
source filename：这个命令其实只是简单地读取脚本里面的语句依次在当前shell里面执行，没有建立新的子shell。那么脚本里面所有新建、改变变量的语句都会保存在当前shell里面。