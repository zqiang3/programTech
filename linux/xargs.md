管道可以实现：将前面的标准输出作为后面的标准输入
管道不能实现：将前面的标准输出作为后面的命令参数

xargs -0 选项 处理特殊字符

-p -n选项

-E 碰到某个参数，就立即终止退出



examples

```bash
git b | grep -v master | xargs git b -D
```