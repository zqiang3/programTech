使`interface{}`有更大的发挥余地。

可以大大提高程序的灵活性，使得interface{}有更大的发挥余地

反射使用TypeOf和ValueOf函数从接口中获取目标对象信息

反射会将匿名字段作为独立字段(匿名字段的本质)

想要利用反射修改对象状态，前提是interface.data是settable，即pointer-interface

通过反射可以"动态" 调用方法



```go
func TypeOf(i interface{}) Type

type Type interface {
  Align() int
  FieldAlign() int
  Method(int) Method
  /*
  type Method struct {
  	Name string
  	PkgPath string
  	Type Type
  	Func Value
  	Index int
  }
  */
  
  // Elem returns a type's element type.
	// It panics if the type's Kind is not Array, Chan, Map, Ptr, or Slice.
	Elem() Type
  
}
func ValueOf(i interface{}) Value

type Value struct {
  
}

// 返回结构体v中的第i个字段。如果v的类型不是结构体或者i超出了结构体的范围，则会出现panic
func (v Value) Field(i int) Value

// 以接口类型返回v的当前值
func (v Value) Interface() (i interface{})

// 通过反射方式修改结构体对象的一些方法

func (v Value) Elem() Value

// Set assigns x to the value v.
// It panics if CanSet returns false.
// As in Go, x's value must be assignable to v's type.
func (v Value) Set(x Value) {
}

func (v Value) Kind() Kind
type Kind uint
const (
  Invalid Kind = iota
  Bool
  Int
  Int8
  Int16
  Int32
  Int64
  Uint8
  Uint16
  Uint32
  Uint64
  Uintptr
  Float32
  Float64
  Complex64
  Complex128
  Array
  Chan
  Func
  Interface
  Map
  Ptr
  Slice
  String
  Struct
  UnsafePointer
)
```

## 反射 基本操作