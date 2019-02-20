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
s := ""
var s string
var s = ""
var s string = ""
```

## for loop

```go
for initialization; condition; post {
    // statements
}
for condition {
    //
}
for {
    //
}
```

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

