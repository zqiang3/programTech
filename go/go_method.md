

## 定义

```go
type user struct {
        name  string,
        email string,
}

//这是函数的定义
func notify(email string) {
        fmt.Println("Email is %s", email)
}

//这是方法的定义
func (u user) notify(email string) {
        fmt.Println("Email is %d", email)
}
```



## 接收者

接收者有两种，一种是值接收者，一种是指针接收者。顾名思义，值接收者，是接收者的类型是一个值，是一个副本，方法内部无法对其真正的接收者做更改；指针接收者，接收者的类型是一个指针，是接收者的引用，对这个引用的修改之间影响真正的接收者。



## 隐式转换

关于值接收者和指针接收者，其实 Go 在编译的时候有一个隐式转换，将其转换为正确的接收者类型。

```
//daryl.changeEmail("daryl@example.com")
(&daryl).changeEmail("daryl@example.com")

wife := &daryl
//wife.notify()
(*wife).notify()
```







