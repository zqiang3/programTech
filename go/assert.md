golang中的所有程序都实现了interface{}的接口，这意味着，所有的类型如string,int,int64甚至是自定义的struct类型都拥有interface{}的接口，这种做法和java中的Object类型比较类似。

```go
func funcName(a interface{}) string {
     return string(a)
}
```

编译器将会返回：

cannot convert a (type interface{}) to type string: need type assertion

此时，意味着整个转化的过程需要类型断言。类型断言有以下几种形式：

1. 直接断言使用

var a interface{}

fmt.Println("Where are you,Jonny?", a.(string))

但是如果断言失败一般会导致panic的发生。所以为了防止panic的发生，我们需要在断言前进行一定的判断

value, ok := a.(string)



2. 进行判断

```go
value, ok := a.(string)
if !ok {
    fmt.Println("It's not ok for type string")
    return
}
fmt.Println("The value is ", value)
```



3. switch

   ```go
   var t interface{}
   t = functionOfSomeType()
   switch t := t.(type) {
   default:
       fmt.Printf("unexpected type %T", t)       // %T prints whatever type t has
   case bool:
       fmt.Printf("boolean %t\n", t)             // t has type bool
   case int:
       fmt.Printf("integer %d\n", t)             // t has type int
   case *bool:
       fmt.Printf("pointer to boolean %t\n", *t) // t has type *bool
   case *int:
       fmt.Printf("pointer to integer %d\n", *t) // t has type *int
   }
   ```

   

## Tips

补充几个go语言编程的技巧

1）如果不符合要求可以尽快的return（return as fast as you can），而减少else语句的使用，这样可以更加直观一些。

2）转换类型的时候如果是string可以不用断言，使用fmt.Sprint()函数可以达到想要的效果

3）变量的定义和申明可以用组的方式，如：

```
var (
   a string
   b int
   c int64
   ...
)


import (
    "fmt"
    "strings"
    "net/http"
   ...
)
```


4) 函数逻辑比较复杂，可以把一些逻辑封装成一个函数，提高可读性。

5）使用net/http包和net/url包的函数，可能会带有url encode功能，需要注意