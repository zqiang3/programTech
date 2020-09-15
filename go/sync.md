## Once

- **init** 函数是在文件包首次被加载的时候执行，且只执行一次
- **sync.Once** 是在代码运行中需要的时候执行，且只执行一次





## WaitGroup

为了等待goroutine运行完毕，最简单的方法，可以使用time.Sleep()来睡眠一段时间，等待其他线程充分运行。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	for i := 0; i < 100; i++ {
		go fmt.Println(i)
	}
	
	time.Sleep(time.Second)
}
```



也可以考虑使用管道来完成上述操作

```
func main() {
	c := make(chan bool, 100)
	for i := 0; i < 100; i++ {
		go func(i int) {
			fmt.Println(i)
			c <- true
		}(i)
	}
	
	for i := 0; i < 100; i++ {
		<- c
	}
}
```

使用管道能完美的达到目的，但使用管道有些大材小用。



使用WaitGroup

Add(n) 将计数器设为n

Done()每次把计数器减1

Wait()会阻塞代码运行，直到计数器值为0

```
func main() {
	wg := sync.WaitGroup{}
	wg.Add(100)
	for i := 0; i < 100; i++ {
		go func(i int) {
			fmt.Println(i)
			wg.Done()
		}(i)
	}
	
	wg.Wait()
}
```

这里首先把`wg` 计数设置为100， 每个for循环运行完毕都把计数器减一，主函数中使用`Wait()` 一直阻塞，直到wg为零——也就是所有的100个for循环都运行完毕。相对于使用管道来说，`WaitGroup` 轻巧了许多。