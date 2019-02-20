## 函数

**多值返回**：多值返回是Go的一大特性，python其实也可以返回多个值，只不过返回值被组合在一个元组了。

按值传递与按引用传递

有些函数没有返回值，我们只是利用函数的副作用，这种函数通常也称为方法。

**命名返回值**

** 尽量使用命名返回值：会使代码更清晰、更简短，同时更加容易读懂 **

```go
func Foo(input int) (a int, b int) {
    a = 2 * input
    b = 3 * input
    return
}

```

空白符：空白符用来匹配不需要的值，然后丢弃掉

改变外部变量：采用传递指针的方式

传递变长参数：参数类型相同，参数类型不同

```go
func min(a ...int) int {  // a 的类型是 []int
    if len(a) == 0 {
        return 0
    }

    min := a[0]
    for _, v := range a {
        if v < min {
            min = v
        }
    }
    return min
}
```

**defer**

关键字defer允许我们执行一些收尾工作

合理使用defer可以使代码更简洁

