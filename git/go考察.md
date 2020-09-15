### 1. 下面代码能运行吗？为什么

```
type Param map[string]interface{}

type Show struct {
    Param
}

func main1() {
    s := new(Show)
    s.Param["RMB"] = 10000
}
```

### 2. 请说出下面代码存在什么问题

```
type student struct {
    Name string
}

func f(v interface{}) {
    switch msg := v.(type) {
        case *student, student:
            msg.Name
    }
}
```

### 3. 写出打印的结果。

```
type People struct {
    name string `json:"name"`
}

func main() {
    js := `{
        "name":"11"
    }`
    var p People
    err := json.Unmarshal([]byte(js), &p)
    if err != nil {
        fmt.Println("err: ", err)
        return
    }
    fmt.Println("people: ", p)
}
```

### 4. 下面的代码是有问题的，请说明原因。

```
package main

import "fmt"

type People struct {
    Name string
}

func (p *People) String() string {
    return fmt.Sprintf("print: %v", p)
}

func main() {
    p := &People{}
    p.String()
}
```

### 5. 请找出下面代码的问题所在。

```
package main

import (
    "fmt"
    "time"
)

func main() {
    ch := make(chan int, 1000)
    go func() {
        for i := 0; i < 10; i++ {
            ch <- i
        }
    }()
    go func() {
        for {
            a, ok := <-ch
            if !ok {
                fmt.Println("close")
                return
            }
            fmt.Println("a: ", a)
        }
    }()
    close(ch)
    fmt.Println("ok")
    time.Sleep(time.Second * 100)
}
```

### 6. 请说明下面代码书写是否正确。

```
var value int32

func SetValue(delta int32) {
    for {
        v := value
        if atomic.CompareAndSwapInt32(&value, v(v+delta)) {
            break
        }
    }
}
```

### 7. 下面的程序运行后为什么会报异常。

```
package main

import (
    "fmt"
    "time"
)

type Project struct{}

func (p *Project) deferError() {
    if err := recover(); err != nil {
        fmt.Println("recover: ", err)
    }
}

func (p *Project) exec(msgchan chan interface{}) {
    for msg := range msgchan {
        m := msg.(int)
        fmt.Println("msg: ", m)
    }
}

func (p *Project) run(msgchan chan interface{}) {
    for {
        defer p.deferError()
        go p.exec(msgchan)
        time.Sleep(time.Second * 2)
    }
}

func (p *Project) Main() {
    a := make(chan interface{}, 100)
    go p.run(a)
    go func() {
        for {
            a <- "1"
            time.Sleep(time.Second)
        }
    }()
    time.Sleep(time.Second * 100)
}

func main() {
    p := new(Project)
    p.Main()
}
```



### 8. 请说出下面代码哪里写错了。

```
func main() {
    abc := make(chan int, 1000)
    for i := 0; i < 10; i++ {
        abc <- i
    }
    go func() {
        for {
            a := <-abc
            fmt.Println("a: ", a)
        }
    }()
    close(abc)
    fmt.Println("close")
    time.Sleep(time.Second * 100)
}
```

### 9. 请说出下面代码，执行时为什么会报错

```
type Student struct {
    name string
}

func main() {
    m := map[string]Student{"people": {"liyuechun"}}
    m["people"].name = "wuyanzu"
}
```

### 10. 请说出下面的代码存在什么问题

```
type query func(string) string

func exec(name string, vs ...query) string {
    ch := make(chan string)
    fn := func(i int) {
        ch <- vs[i](name)
    }
    for i, _ := range vs {
        go fn(i)
    }
    return <-ch
}

func main() {
    ret := exec("111", func(n string) string {
        return n + "func1"
    }, func(n string) string {
        return n + "func2"
    }, func(n string) string {
        return n + "func3"
    }, func(n string) string {
        return n + "func4"
    })
    fmt.Println(ret)
}
```



11. 

```go
package main

import "fmt"

func foo(a []int) {
	a[0] = 99
	for i := 0; i < 100; i++ {
		a = append(a, i)
	}
}

func main() {
	a := [3]int{1, 2, 3}
	b := a[1:3]
	foo(b)
	fmt.Println(b)
}
```

12 

```go


// 一
func main() {
    for i := 0; i < 5; i++ {
        go func(i int) {
            time.Sleep(10 * time.Second)
            fmt.Printf("%d\n", i)
        }(i)
    }

    fmt.Println("Exit")
}

// 二
func main() {
    wg := sync.WaitGroup{}

    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func(wg sync.WaitGroup, i int) {
            time.Sleep(10 * time.Second)
            fmt.Printf("%d\n", i)
            wg.Done()
        }(wg, i)
    }

    wg.Wait()
    fmt.Println("Exit")
}
```

