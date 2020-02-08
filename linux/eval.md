```bash
#!/bin/bash
a='my'
b='site'
my_site='my site www.361.com'
echo a_b is "$a"_"$b"
echo $("$a"_"$b")
web="$a"_"$b"
echo web is $web
eval echo '$'"$a"_"$b"
eval echo '$'{"$a"_"$b"}
```



## eval作用

eval 命令将会首先扫描命令行进行所有的置换，然后再执行该命令。该命令适用于那些一次扫描无法实现其功能的变量，该命令对变量进行两次扫描。这些需要进行两次扫描的变量有时被称为复杂变量。eval命令既可以用于回显简单变量，也可以用于回显复杂变量。