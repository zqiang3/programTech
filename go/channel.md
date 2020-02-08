## 概述

Channel是Go中的一个核心类型，你可以把它看成一个管道，通过它并发核心单元就可以发送或者接收数据进行通讯(communication)。

channel的操作符是箭头，箭头的指向就是数据的流向。

你可以在多个goroutine从/往 一个channel 中 receive/send 数据, 不必考虑额外的同步措施。

Channel可以作为一个先入先出(FIFO)的队列，接收的数据和发送的数据的顺序是一致的。



## Go Channel详解

```go
chan T          // 可以接收和发送类型为 T 的数据
chan<- float64  // 只可以用来发送 float64 类型的数据
<-chan int      // 只可以用来接收 int 类型的数据
```

`<-`总是优先和最左边的类型结合。(The <- operator associates with the leftmost chan possible)



```go
make(chan int, 100)
```

容量(capacity)代表Channel容纳的最多的元素的数量，代表Channel的缓存的大小。
如果没有设置容量，或者容量设置为0, 说明Channel没有缓存，只有sender和receiver都准备好了后它们的通讯(communication)才会发生(Blocking)。如果设置了缓存，就有可能不发生阻塞， 只有buffer满了后 send才会阻塞， 而只有缓存空了后receive才会阻塞。一个nil channel不会通信。

可以通过内建的`close`方法可以关闭Channel。

你可以在多个goroutine从/往 一个channel 中 receive/send 数据, 不必考虑额外的同步措施。

Channel可以作为一个先入先出(FIFO)的队列，接收的数据和发送的数据的顺序是一致的。

```go
v, ok := <-ch
```





Channel 分为两种：带缓冲、不带缓冲。对不带缓冲的 channel 进行的操作实际上可以看作 “同步模式”，带缓冲的则称为 “异步模式”。



## Usage

### 定义

```go
ChannelType = ("chan" | "chan" "<-" | "<-" "chan")
```

它包括三种类型的定义。可选的`<-`代表channel的方向。如果没有指定方向，那么Channel就是双向的.

```go
chan T          // 可以接收和发送类型为 T 的数据
chan<- float64  // 只可以用来发送 float64 类型的数据
<-chan int      // 只可以用来接收 int 类型的数据
```



### <-运算符

`<-`总是优先和最左边的类型结合

```go
// 看晕了_^_
chan<- chan int    // 等价 chan<- (chan int)
chan<- <-chan int  // 等价 chan<- (<-chan int)
<-chan <-chan int  // 等价 <-chan (<-chan int)
chan (<-chan int)
```

### capacity

容量(capacity)代表Channel容纳的最多的元素的数量，代表Channel的缓存的大小。
如果没有设置容量，或者容量设置为0, 说明Channel没有缓存，只有sender和receiver都准备好了后它们的通讯(communication)才会发生(Blocking)。如果设置了缓存，就有可能不发生阻塞， 只有buffer满了后 send才会阻塞， 而只有缓存空了后receive才会阻塞。一个nil channel不会通信。



### close

可以通过内建的`close`方法可以关闭Channel。

往一个已经被close的channel中继续发送数据会导致**run-time panic**。

从一个被close的channel中接收数据不会被阻塞，而是立即返回，接收完已发送的数据后会返回元素类型的零值(zero value)。

可以使用一个额外的返回参数来检查channel是否关闭。

```go
x, ok := <-ch
x, ok = <-ch
var x, ok = <-ch
```

如果OK 是false，表明接收的x是产生的零值，这个channel被关闭了或者为空。



### 从关闭的channel读数据会怎样

但是从这个关闭的channel中不但可以读取出已发送的数据，还可以不断的读取零值

```go
c := make(chan int, 10)
c <- 1
c <- 2
close(c)
fmt.Println(<-c) //1
fmt.Println(<-c) //2
fmt.Println(<-c) //0
fmt.Println(<-c) //0
```



### multi-valued assignment

channel的 receive支持 *multi-valued assignment*



###发送值到Channel

```go
ch <- v
```

###从Channel中接收数据

```go
v := <-ch
```



### 无缓存channel

```go
c := make(chan int)
defer close(c)
go func() { c <- 3 + 4 }()
i := <-c
fmt.Println(i)
```

send被执行前(proceed)通讯(communication)一直被阻塞着。如前所言，无缓存的channel只有在receiver准备好后send才被执行。如果有缓存，并且缓存未满，则send会被执行。

往nil channel中发送数据会一致被阻塞着

从一个nil channel中接收数据会一直被block



### timeout

```go
import "time"
import "fmt"
func main() {
    c1 := make(chan string, 1)
    go func() {
        time.Sleep(time.Second * 2)
        c1 <- "result 1"
    }()
    select {
    case res := <-c1:
        fmt.Println(res)
    case <-time.After(time.Second * 1):
        fmt.Println("timeout 1")
    }
}
```

其实它利用的是`time.After`方法，它返回一个类型为`<-chan Time`的单向的channel，在指定的时间发送一个当前时间给返回的channel中。

### fibonacci

```go
import "fmt"
func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}
func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c)
		}
		quit <- 0
	}()
	fibonacci(c, quit)
}
```

