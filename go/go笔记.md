## go程序的执行过程

1. 按顺序导入所有被 main 包引用的其它包，然后在每个包中执行如下流程：
2. 如果该包又导入了其它的包，则从第一步开始递归执行，但是每个包只会被导入一次。
3. 然后以相反的顺序在每个包中初始化常量和变量，如果该包含有 init 函数的话，则调用该函数。
4. 在完成这一切之后，main 也执行同样的过程，最后调用 main 函数开始执行程序。

## 特殊规定

左大括号 `{` 必须与方法的声明放在同一行，这是编译器的强制规定 

**Go 语言虽然看起来不使用分号作为语句的结束，但实际上这一过程是由编译器自动完成** 

## 注释

单行注释：//

多行注释：/* */

## 命名空间、包

如果main 包的源代码没有包含main函数，则会引发构建错误 `undefined: main.main` 

main 函数即没有参数，也没有返回类型（与 C 家族中的其它语言恰好相反）。如果你不小心为 main 函数添加了参数或者返回类型，将会引发构建错误

## 数据类型

int float bool string

struct array slice map channel

## 类型转换

```go
a := 5.0
b := int(a)
```

## 常量 变量

常量：const，变量：var

在 Go 语言中，你可以省略类型说明符 `[type]`，因为编译器可以根据变量的值来推断其类型

```go
const b string = "abc"
const b = "abc"
```

 ## iota

`iota` 也可以用在表达式中，如：`iota + 50`。在每遇到一个新的常量块或单个常量声明时， `iota` 都会重置为 0（ **简单地讲，每遇到一次 const 关键字，iota 就重置为 0** ） 

```go
type Color int

const (
    RED Color = iota
    ORANGE
    YELLO
    GREEN
    BLUE
)
```



## 函数

只有当某个函数需要被外部包调用的时候才使用大写字母开头 

```go
func FunctionName(a typea, b typeb) typeFunc
```

