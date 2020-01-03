1.  

   ```go
   package main
   
   import (
   	"fmt"
   )
   
   func main() {
   	defer func() {
   		fmt.Println("aaa")
   	}()
   
   	defer func() {
   		fmt.Println("bbb")
   	}()
   
   	defer func() {
   		if err := recover(); err != nil {
   			fmt.Println("recover", err)
   		}
   		fmt.Println("ccc")
   	}()
   
   	panic("panic")
   	fmt.Println("end")
   }
   ```

   

2. 下面的代码输出是什么，并说明原因

   ```go
   package main
   
   import (
   	"fmt"
   )
   
   type student struct {
   	Name string
   	Age int
   }
   
   func parseStudent() map[string]*student {
   	m := make(map[string]*student)
   	stus := []student {
   		{Name: "zhou", Age: 24},
   		{Name: "li", Age: 26},
   		{Name: "wang", Age: 22},
   	}
   
   	for _, stu := range stus {
   		m[stu.Name] = &stu
   	}
   
   	return m
   }
   
   func main() {
   	students := parseStudent()
   	for k, v := range students {
   		fmt.Printf("key=%s, value=%v\n", k, v)
   	}
   
   	fmt.Println("end")
   }
   ```

3. 下面的代码输出是什么

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

4. 下面代码的输出

   ```go
   
   package main
   
   import (
   	"fmt"
   	"runtime"
   	"sync"
   	"time"
   )
   
   func init() {
   	fmt.Println("Current Go Version: ", runtime.Version())
   }
   
   
   func main() {
   	runtime.GOMAXPROCS(1)
   
   	count := 10
   
   	wg := sync.WaitGroup{}
   	wg.Add(count * 2)
   	for i := 0; i < count; i++ {
   		go func() {
   			time.Sleep(100 * time.Millisecond)
   			fmt.Printf("[%d]", i)
   			wg.Done()
   		}()
   	}
   
   	for i := 0; i < count; i++ {
   		go func(i int) {
   			time.Sleep(100 * time.Millisecond)
   			fmt.Printf("-%d-", i)
   			wg.Done()
   		}(i)
   	}
   	wg.Wait()
   }
   ```

   

5. 写出下列程序的输出

   ```go
   package main
   
   import (
   	"fmt"
   )
   
   
   type People struct{}
   
   func (p * People) ShowA() {
   	fmt.Println("ShowA")
   	p.ShowB()
   }
   
   func (p *People) ShowB() {
   	fmt.Println("ShowB")
   }
   
   type Teacher struct {
   	People
   }
   
   func (t *Teacher) ShowB() {
   	fmt.Println("teacher ShowB")
   }
   
   func main() {
   	t := Teacher{}
   	t.ShowA()
   }
   ```

   

6. 写出下列程序的输出

   ```go
   package main
   
   import (
   	"fmt"
   	"runtime"
   )
   
   func main() {
   	runtime.GOMAXPROCS(1)
   	int_chan := make(chan int, 1)
   	string_chan := make(chan string, 1)
   	int_chan <- 1
   	string_chan <- "hello"
   	select {
   	case value := <- int_chan:
   		fmt.Println(value)
   	case  value := <-string_chan:
   		panic(value)
   	}
   }
   ```

   

7. 分析以下程序

   ```go
   package main
   
   import (
   	"fmt"
   )
   
   func main() {
   	s := make([]int, 5)
   	fmt.Printf("%p\n", s)
   	fmt.Println(s)
   
   	s = append(s, 1, 2, 3)
   	fmt.Printf("%p\n", s)
   	fmt.Println(s)
   }
   ```

   

8. 以下代码有什么错误？

   ```go
   package main
   
   import (
   	"fmt"
   )
   
   type People interface {
   	Speak(string) string
   }
   
   type Student struct {
   
   }
   
   func (stu *Student) Speak(think string) (talk string) {
   	if think == "bitch" {
   		talk = "You are a good boy"
   	} else {
   		talk = "hi"
   	}
   	return
   }
   
   func main() {
   	var peo People = Student{}
   	think := "bitch"
   	fmt.Println(peo.Speak(think))
   }
   ```

   