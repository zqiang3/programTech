## 简介

Monkey是Golang的一个猴子补丁框架，在运行时通过汇编语句重写可执行文件，将待打桩函数或方法的实现转到桩实现，原理和热补丁类似。

Monkey的工作原理：http://bouk.co/blog/monkey-patching-in-go/。

通过Monkey，我们可以解决函数或方法的打桩问题，但Monkey不是线程安全的，不要将Monkey用于并发的测试中。



## 安装

```bash
go get github.com/bouk/monkey
go get github.com/agiledragon/gomonkey
```



## 使用场景

1. 基本场景：为一个函数打桩
2. 基本场景：为一个过程打桩
3. 基本场景：为一个方法打桩
4. 复合场景：由任意相同或不同的基本场景组合而成
5. 特殊场景：桩中桩的一个案例





## ApplyFunc

```go
func ApplyFunc(target, double interface{}) *Patches
func (this *Patches) ApplyFunc(target, double interface{}) *Patches
```

