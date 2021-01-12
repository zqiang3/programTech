## Description

在 Go 语言中，我们可以把函数作为一种变量，用 type 去定义它，那么这个函数类型就可以作为值传递，甚至可以实现方法，这一特性是在太灵活了，有时候我们甚至可以利用这一特性进行类型转换。作为值传递的条件是类型具有相同的参数以及相同的返回值。

## 定义

```go
type Method func(int, int) int
```



## 代码示例

```go
package main

import "fmt"

func add(a, b int) int {
	return a + b
}

func del(a, b int) int {
	return a - b
}

type Method func(int, int) int

func main() {
	var a Method
	a = del
	fmt.Println(a(3, 3))
}
```

