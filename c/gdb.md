```sh
gcc -g test.c -o test // -g选项告诉gcc在编译程序时加入调试信息

// 进入调试模式
gdb test
// 或
gdb -q test
// 或先进入gdb模式，再加载文件
gdb -q
file test
set args xxx xxx  // 命令行参数
```



| 命令            | 说明     |      |
| --------------- | -------- | ---- |
| b               | 设置断点 |      |
| clear <linenum> | 清除断点 |      |
|                 |          |      |

