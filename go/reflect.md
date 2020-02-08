## overview

在Go语言中，reflect实现了运行时反射。`reflect` 包会帮助识别 `interface{}` 变量的底层具体类型和具体值。这正是我们所需要的。

## reflect.Type和reflect.Value

参数 `interface{}` 的具体类型由 `reflect.Type` 表示，而 `reflect.Value` 表示它的具体值。[reflect.TypeOf()](https://golang.org/pkg/reflect/#TypeOf) 和 [reflect.ValueOf()](https://golang.org/pkg/reflect/#ValueOf) 两个函数可以分别返回 `reflect.Type` 和 `reflect.Value`。

## reflect.Kind

`reflect`包中还有一个重要的类型：[Kind](https://golang.org/pkg/reflect/#Kind)。

Kind和Type的类型可能看起来很相似，但它们之间存在差异。

Kind表示该类型的特定种类。



## NumField()和Field()方法

[NumField()](https://golang.org/pkg/reflect/#Value.NumField) 方法返回结构体中字段的数量，而 [Field(i int)](https://golang.org/pkg/reflect/#Value.Field) 方法返回字段 `i` 的 `reflect.Value`。



## New()

```go
// New returns a Value representing a pointer to a new zero value
// for the specified type. That is, the returned Value's Type is PtrTo(typ).
func New(typ Type) Value {
  
}
```




## Interface()

```go
// Interface returns v's current value as an interface{}.
// It is equivalent to:
//	var i interface{} = (v's underlying value)
// It panics if the Value was obtained by accessing
// unexported struct fields.
func (v Value) Interface() (i interface{}) {
  
}
```





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