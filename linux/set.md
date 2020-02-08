## link

http://www.ruanyifeng.com/blog/2017/11/bash-set.html



## set -x

默认情况下，脚本执行后，屏幕只显示运行结果，没有其他内容。如果多个命令连续执行，它们的运行结果就会连续输出。有时会分不清，某一段内容是什么命令产生的。

`set -x`用来在运行结果之前，先输出执行的那一行命令。

> ```bash
> #!/usr/bin/env bash
> set -x
> 
> echo bar
> ```

执行上面的脚本，结果如下。

> ```bash
> $ bash script.sh
> + echo bar
> bar
> ```

可以看到，执行`echo bar`之前，该命令会先打印出来，行首以`+`表示。这对于调试复杂的脚本是很有用的。

`-x`还有另一种写法`-o xtrace`。

> ```bash
> set -o xtrace
> ```