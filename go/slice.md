## link

https://blog.golang.org/slices-intro

https://golang.org/doc/effective_go.html#slices

## array

几乎所有计算机语言，数组的实现都是相似的：一段连续的内存，Go语言也一样，Go语言的数组底层实现就是一段连续的内存空间。

Go语言的数组不同于C语言或者其他语言的数组，C语言的数组变量是指向数组第一个元素的指针；而Go语言的数组是一个值，Go语言中的数组是值类型，一个数组变量就表示着整个数组，意味着Go语言的数组在传递的时候，传递的是原数组的拷贝。你可以理解为Go语言的数组是一种有序的`struct`。go中的数组变量指代整个数组，并不表示数组的地址。



Go's arrays are values. An array variable denotes the entire array; it is not a pointer to the first array element (as would be the case in C). This means that when you assign or pass around an array value you will make a copy of its contents. (To avoid the copy you could pass a *pointer* to the array, but then that's a pointer to an array, not an array.) One way to think about arrays is as a sort of struct but with indexed rather than named fields: a fixed-size composite value.



## slice

切片是一个很小的对象，是对数组进行了抽象，并提供相关的操作方法。切片有三个属性字段：长度、容量和指向数组的指针。

`nil`切片和`空`切片是不太一样的，空切片即`s := make([]byte, 0)`或者`s := []byte{}`出来的切片。但是，不管是空切片还是nil切片，对其调用内置函数`append()`、`len`和`cap`的效果都是一样的，感受不到任何区别。

nil切片：var s []int  指针为nil，并不分配空间

空切片：s := []byte{}, 指针不为nil，数据并不分配空间



## slice 原理

Slices hold references to an underlying array. 切片引用了一个底层的数组。

我们先来介绍如何使用字面量的方式创建新的切片结构，`[]int{1, 2, 3}` 其实会在编译期间由 `slicelit` 转换成如下所示的代码：

```go
var vstat [3]int
vstat[0] = 1
vstat[1] = 2
vstat[2] = 3
var vauto *[3]int = new([3]int)
*vauto = vstat
slice := vauto[:]
```

1. 根据切片中的元素数量对底层数组的大小进行推断并创建一个数组；
2. 将这些字面量元素存储到初始化的数组中；
3. 创建一个同样指向 `[3]int` 类型的数组指针；
4. 将静态存储区的数组 `vstat` 赋值给 `vauto` 指针所在的地址；
5. 通过 `[:]` 操作获取一个底层使用 `vauto` 的切片；

`[:]` 以及类似的操作 `[:10]` 其实都会在 [SSA 代码生成](https://draveness.me/golang/compile/golang-ir-ssa.html) 阶段被转换成 `OpSliceMake` 操作，这个操作会接受四个参数创建一个新的切片，切片元素类型、数组指针、切片大小和容量。

go中的slice不仅可以通过切片操作使长度变短，还可以使长度变长。

```
	a := [...]int{1, 2, 3, 4, 5}
	s := a[1:3]
	s = s[:cap(s)]
```





## 扩容

slice这种数据结构便于使用和管理数据集合，可以理解为是一种“动态数组”，`slice`也是围绕动态数组的概念来构建的。既然是动态数组，那么slice是如何扩容的呢？

请记住以下两条规则：

- 如果切片的容量小于1024个元素，那么扩容的时候slice的cap就翻番，乘以2；一旦元素个数超过1024个元素，增长因子就变成1.25，即每次增加原来容量的四分之一。
- 如果扩容之后，还没有触及原数组的容量，那么，切片中的指针指向的位置，就还是原数组，如果扩容之后，超过了原数组的容量，那么，Go就会开辟一块新的内存，把原来的值拷贝过来，这种情况丝毫不会影响到原数组。

**copy**

```
t := make([]byte, len(s), (cap(s) + 1) * 2)
for i := range s {
	t[i] = s[i]
}
```

copy copies data from a source slice to a destination slice. It returns the number of elements copied.

```
func copy(dst, src []T) int
```

The `copy` function supports copying between slices of different lengths (it will copy only up to the smaller number of elements). In addition, `copy` can handle source and destination slices that share the same underlying array, handling overlapping slices correctly.

```go
t := make([]byte, len(s), (cap(s)+1) * 2)
copy(t, s)
s = t
```



## nil slice

Since the zero value of a slice (`nil`) acts like a zero-length slice, you can declare a slice variable and then append to it in a loop:

```go
// Filter returns a new slice holding only
// the elements of s that satisfy fn()
func Filter(s []int, fn func(int) bool) []int {
    var p []int // == nil
    for _, v := range s {
        if fn(v) {
            p = append(p, v)
        }
    }
    return p
}
```

## slice会导致原数组一直被引用

This code behaves as advertised, but the returned `[]byte` points into an array containing the entire file. Since the slice references the original array, as long as the slice is kept around the garbage collector can't release the array; the few useful bytes of the file keep the entire contents in memory.

```go 
var digitRegexp = regexp.MustCompile("[0-9]+")

func FindDigits(filename string) []byte {
    b, _ := ioutil.ReadFile(filename)
    return digitRegexp.Find(b)
}
```

To fix this problem one can copy the interesting data to a new slice before returning it:

```go
func CopyDigits(filename string) []byte {
    b, _ := ioutil.ReadFile(filename)
    b = digitRegexp.Find(b)
    c := make([]byte, len(b))
    copy(c, b)
    return c
}
```

## effective go中的说明

The length of a slice may be changed as long as it still fits within the limits of the underlying array; just assign it to a slice of itself. The *capacity* of a slice, accessible by the built-in function `cap`, reports the maximum length the slice may assume. Here is a function to append data to a slice. If the data exceeds the capacity, the slice is reallocated. The resulting slice is returned. The function uses the fact that `len` and `cap` are legal when applied to the `nil` slice, and return 0.

```go
func Append(slice, data []byte) []byte {
    l := len(slice)
    if l + len(data) > cap(slice) {  // reallocate
        // Allocate double what's needed, for future growth.
        newSlice := make([]byte, (l+len(data))*2)
        // The copy function is predeclared and works for any slice type.
        copy(newSlice, slice)
        slice = newSlice
    }
    slice = slice[0:l+len(data)]
    copy(slice[l:], data)
    return slice
}
```



We must return the slice afterwards because, although `Append` can modify the elements of `slice`, the slice itself (the run-time data structure holding the pointer, length, and capacity) is **passed by value.**

The idea of appending to a slice is so useful it's captured by the `append` built-in function. To understand that function's design, though, we need a little more information, so we'll return to it later.