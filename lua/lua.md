## 安装

```bash
curl -R -O http://www.lua.org/ftp/lua-5.3.0.tar.gz
tar zxf lua-5.3.0.tar.gz
cd lua-5.3.0
make linux test
make install
```

## 语法

Lua是动态类型语言

单行注释：两个减号 --

多行注释：

```lua
-- 单行注释
--[[
    多行注释
--]]
```

标识符：字母或下划线开头，大小写敏感。最好不要使用下划线加大写字母的标示符，因为Lua的保留字也是这样的

## 变量 数据类型

Lua 变量有三种类型：全局变量、局部变量、表中的域。

Lua中的变量默认是全局变量，除非用local显示声明为局部变量

变量不需要类型定义,只需要为变量赋值

变量默认是全局的，如果你想删除一个全局变量，只需要将变量赋值为nil

**数据类型**

Lua中有8个基本类型分别为：nil、boolean、number、string、userdata、function、thread和table

我们可以使用type函数测试给定变量或者值的类型

**number**: Lua 默认只有一种 number 类型 -- double（双精度）类型

**字符串**由一对双引号或单引号来表示，可以用 2 个方括号 "[[]]" 来表示"一块"字符串

在对一个数字字符串上进行算术操作时，Lua 会尝试将这个数字字符串转成一个数字

字符串连接使用的是 .. 

使用 # 来计算字符串的长度，放在字符串前面

**表**

最简单构造表达式是{}，用来创建一个空表。也可以在表里添加一些数据，直接初始化表

在 Lua 里表的默认初始索引一般以 1 开始

Lua 也提供了 . 操作。

```lua
t.i                 -- 当索引为字符串类型时的一种简化写法
```

**赋值**

Lua可以对多个变量同时赋值

```lua
a, b = 10, 2*x
```

遇到赋值语句Lua会先计算右边所有的值然后再执行赋值操作，所以我们可以这样进行交换变量的值

当变量个数和值的个数不一致时，Lua会一直以变量个数为基础采取以下策略：

```
a. 变量个数 > 值的个数             按变量个数补足nil
b. 变量个数 < 值的个数             多余的值会被忽略
```

## 流程控制

```lua
-- while
while(condition)
do
   statements
end

-- repeat until
repeat
   statements
until( condition )

-- if
if(0)
then
    print("0 为 true")
end
```

## 函数

在 Lua 中，函数是被看作是"第一类值（First-Class Value）"，函数可以存在变量里

```lua
function foo(n)
    if n == 0 then
        return 1
    else
        return n * foo(n - 1)
    end
end


print(foo(5))
```

**多返回值**: Lua函数中，在return后列出要返回的值的列表即可返回多值

## 迭代器

```lua
for k,v in pairs(t) do
   	xxx
end
```



## 协程

在 Lua 里，最主要的线程是协同程序（coroutine）。它跟线程（thread）差不多，拥有自己独立的栈、局部变量和指令指针，可以跟其他协同程序共享全局变量和其他大部分东西。

线程跟协程的区别：线程可以同时多个运行，而协程任意时刻只能运行一个，并且处于运行状态的协程只有被挂起（suspend）时才会暂停