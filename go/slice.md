## 切片初始化

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