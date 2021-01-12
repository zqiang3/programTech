## 参考资料

https://golang.org/doc/effective_go.html

https://golang.org/ref/mem

https://golang.org/ref/spec

https://dave.cheney.net/high-performance-go-workshop/gophercon-2019.html



## defer

执行顺序为LIFO, 参数的值在语句执行时就已经确定。

```go
for i := 0; i < 5; i++ {
  defer fmt.Printf("%d ", i)
}
```



## array

array的长度是类型的一部分

```go
[3]int 和 [4]int 是不同的类型
```

array是传值的



## slice

slice本质也是传值，golang都是传值的。

src/runtime/slice.go

```go
type slice struct {
  array unsafe.Pointer
  len int
  cap int
}
```

slice 不能作为map对象的key，因为slice没有完全实现`==`操作符，但array可以。

slice只能使用`==`判断是否为nil。

两个slice a、b是否存在竞态，与a、b是否为同一slice无关，只与a与b是否指向同一块内存区域有关。

```go
func main() {
  a := []int{1, 2}
  b := a[1:]
  go func() {
    a[1] = 0
  }()
  fmt.Println(b[0])
}
```

slice引用底层数组而造成内存泄露

例如，使用`ioutil.ReadAll`读取了一个10M的文件，并将其前512K切片给另外一个slice b使用。只要b还在使用，那么底层数组也不会被释放。

## append

append不是线程安全的

```go
var s []int
var wg sync.WaitGroup
for i := 0; i < 10; i++ {
  wg.Add(1)
  go func(i int) {
    s = append(s, i)
    wg.Done()
  }(i)
}
wg.Wait()
fmt.Println(s)
```

复制数据时使用copy比append性能更优。

## Reader

如果知道Reader里的数据大小，使用`ReadFull`而不是`ioutil.ReadAll`

## for range

如果每个元素比较大，循环时使用range取值的方式遍历，性能较差。