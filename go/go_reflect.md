## 链接

https://juejin.im/post/5c2040d76fb9a049c643d9bd

## 反射的目标

反射的目标之一是获取变量的类型信息，例如这个类型的名称、占用字节数、所有的方法列表、所有的内部字段结构、它的底层存储类型等等。

反射的目标之二是动态的修改变量内部字段值。比如 json 的反序列化，你有的是对象内部字段的名称和相应的值，你需要把这些字段的值循环填充到对象相应的字段里。

## 反射的基础代码

reflect 包提供了两个基础反射方法，分别是 TypeOf() 和 ValueOf() 方法，分别用于获取变量的类型和值，定义如下

```go
func TypeOf(v interface{}) Type
func ValueOf(v interface{}) Value
```



Value 这个结构体虽然很简单，但是附着在 Value 上的方法非常之多，主要是用来方便用户读写 ptr 字段指向的数据内存。虽然我们也可以通过 unsafe 包来精细操控内存，但是使用过于繁琐，使用 Value 结构体提供的方法会更加简单直接。

```go
func (v Value) SetLen(n int)  // 修改切片的 len 属性
 func (v Value) SetCap(n int) // 修改切片的 cap 属性
 func (v Value) SetMapIndex(key, val Value) // 修改字典 kv
 func (v Value) Send(x Value) // 向通道发送一个值
 func (v Value) Recv() (x Value, ok bool) // 从通道接受一个值
 // Send 和 Recv 的非阻塞版本
 func (v Value) TryRecv() (x Value, ok bool)
 func (v Value) TrySend(x Value) bool
 
 // 获取切片、字符串、数组的具体位置的值进行读写
 func (v Value) Index(i int) Value
 // 根据名称获取结构体的内部字段值进行读写
 func (v Value) FieldByName(name string) Value
 // 将接口变量装成数组，一个是类型指针，一个是数据指针
 func (v Value) InterfaceData() [2]uintptr
 // 根据名称获取结构体的方法进行调用
 // Value 结构体的数据指针 ptr 可以指向方法体
 func (v Value) MethodByName(name string) Value
 ...

作者：老錢
链接：https://juejin.im/post/5c2040d76fb9a049c643d9bd
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

