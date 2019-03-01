## 第一个go程序

```go
package main
import "fmt"

func main() {
    fmt.Println("Hello, world")
}

$ go run hello.go
$ go build hello.go
$ ./hello
```

## package

package main is special

import exactly the packages you need

## func

function declaration: func

函数名, 括号，参数列表，函数体

## 变量

```go
var name [type] [= exp]
var s string = "abc"
var s string
var s = "abc"

var i, j, k int
var a, b, c = true, 2.3, "four"
var f, err = os.Open(name)

s := ""  // := is declaration
i, j := 0, 1
f, err := os.Open(name)
out, err := os.Open(name)
f, err = os.Create(outfile)


```

## 整型和浮点型

整数：

- int8（-128 -> 127）

- int16（-32768 -> 32767）

- int32（-2,147,483,648 -> 2,147,483,647）

- int64（-9,223,372,036,854,775,808 -> 9,223,372,036,854,775,807）

- uint8（0 -> 255）

- uint16（0 -> 65,535）

- uint32（0 -> 4,294,967,295）

- uint64（0 -> 18,446,744,073,709,551,615）

  

浮点型（IEEE-754 标准）：

- float32（+- 1e-45 -> +- 3.4 * 1e38）
- float64（+- 5 * 1e-324 -> 107 * 1e308）

基于架构的类型：`int` 和 `uint` 在 32 位操作系统上，它们均使用 32 位（4 个字节），在 64 位操作系统上，它们均使用 64 位（8 个字节） 

可以通过增加前缀 0 来表示 8 进制数（如：077），增加前缀 0x 来表示 16 进制数（如：0xFF） 

float32 精确到小数点后 7 位，float64 精确到小数点后 15 位。 

**类型别名**

type TZ int

**字符类型**

```
var ch byte = 65 或 var ch byte = '\x41'
var ch int = '\u0041'
var ch2 int = '\U00101234'
```

## strings

```
strings.HasPrefix(str, prefix string) bool
strings.Contains(s, substr string) bool
strings.Index(s, str string) int
strings.LastIndex(s, str string) int
strings.Replace(str, old, new, n) string
strings.Count(s, str string) int
strings.Repeat(s, count int) string
strings.ToLower(s) string
strings.ToUpper(s) string
strings.TrimSpace(s)
strings.Trim(s, "cut")
strings.Fields(s)
strings.Split(s, sep)
strings.Join(s1 []string, sep string)
```

## strconv

```
strconv.Itoa(i int) string
strconv.Atoi(s string) (i int, err error)
strconv.ParseFloat(s string, bitSize int) (f flaot64, err error)
```



## 格式化说明符

在格式化字符串里，`%d` 用于格式化整数（`%x` 和 `%X` 用于格式化 16 进制表示的数字），`%g` 用于格式化浮点型（`%f` 输出浮点数，`%e` 输出科学计数表示法），`%0d` 用于规定输出定长的整数，其中开头的数字 0 是必须的。

`%n.mg` 用于表示数字 n 并精确到小数点后 m 位，除了使用 g 之外，还可以使用 e 或者 f，例如：使用格式化字符串`%5.2e` 来输出 3.4 的结果为 `3.40e+00`

## 运算符

带有 `++` 和 `--` 的只能作为语句，而非表达式，因此 `n = i++` 这种写法是无效的 。其它像 `f(i++)` 或者`a[i]=b[i++]` 这些可以用于 C、C++ 和 Java 中的写法在 Go 中也是不允许的。 

## 运算符优先级

```
优先级   运算符
 7      ^ !
 6      * / % << >> & &^
 5      + - | ^
 4      == != < <= >= >
 3      <-
 2      &&
 1      ||
```

## 控制结构

```go
if condition1 {
    // do something 
} else if condition2 {
    // do something else    
}else {
    // catch-all or default
}

switch var1 {
    case v1:
        ...
    case v2:
        ...
    default:
    	...    
}

switch initialization  {
    case condition1:
        f1()
    case condition2:
        f2()
    default:
        f3()
}

for initialization; condition; post {
    // statements
}
for condition {
    //
}
for {
    //
}
for pos, char := range str {
...
}

os.Exit(1)
```

## 函数

```go
func name(parameter-list) (result-list) {
    body
}
```

go不支持函数重载

## range

_, arg := range os.Args[1:]  // :=是简略写法，自动判断类型；range返回index, value

## Args

import os

os.Args

## Join

```go
import "strings"
strings.Joint(s, ",")
```

## rand

`rand.Float32` 和 `rand.Float64` 返回介于 [0.0, 1.0) 之间的伪随机数，其中包括 0.0 但不包括 1.0。函数 `rand.Intn`返回介于 [0, n) 之间的伪随机数。 