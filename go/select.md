

## 概述

A "select" statement chooses which of a set of possible send or receive operations will proceed. It looks similar to a "switch" statement but with the cases all referring to communication operations.

`select`的用法 与`switch`非常类似，由`select`开始一个新的选择块，每个选择条件由case语句来描述。但switch语句可以选择任何可使用相等比较，select有比较多的限制，其中最大的一条限制就是每个case语句里必须是一个IO操作，确切地说，应该是一个面向channel的IO操作。



golang 的 select 的功能和 `select, poll, epoll` 相似， 就是监听 IO 操作，当 IO 操作发生时，触发相应的动作。



同步模式下，发送方和接收方要同步就绪，只有在两者都 ready 的情况下，数据才能在两者间传输（后面会看到，实际上就是内存拷贝）。否则，任意一方先行进行发送或接收操作，都会被挂起，等待另一方的出现才能被唤醒。



## select的执行过程

1. For all the cases in the statement, the channel operands of receive operations and the channel and right-hand-side expressions of send statements are evaluated exactly once, in source order, upon entering the `select` statement.
2. If one or more of the communications can proceed, a single one that can proceed is chosen via a uniform pseudo-random selection. Otherwise, if there is a default case, that case is chosen. If there is no default case, the select statement blocks until at lease one of the communications can proceed.



## Usage

### usage

```go
select {
case SendStmt:
  // statements
case RecvStmt:
  // statements
  default:
  // statements
}
// SendStmt: channelVariable <- value
// RecvStmt: variable <-channelVariable

```

###ex1

```go
package main
import(
  "fmt"
  "time"
)

func f1(ch chan int) {
  time.Sleep(time.Second * 5)
  ch <- 1
}

func f2(ch chan int) {
  time.Sleep(time.Second * 10)
  ch <- 2
}

func main() {
  var ch1 = make(chan int)
  var ch2 = make(chan int)
  go f1(ch1)
  fo f2(ch2)
  
  select {
    case <-ch1:
    	fmt.Println("The first case is selected.")
    case <-ch2:
    	fmt.Println("The second case is selected.")
  }
}
```



### ex2

```go
var ch1 chan int
var ch2 chan int
var chs = []chan int {ch1, ch2}

var numbers = []int{1, 2, 3, 4, 5}

func getNumber(i int) int {
  fmt.Printf("numbers [%d]\n", i)
  return numbers[i]
}

func getChan(i int) chan int {
  fmt.Printf("chs[%d]\n", i)
  return chs[i]
}

func main() {
  select {
    case getChan(0) <- getNumber(2):
    	fmt.Println("1th case is selected")
    case getChan(1) <- getNumber(3):
      fmt.Println("2th case is selected")
    default:
    	fmt.Println("default!")
  }
}
```

上面的例子会输出`default!`.是因为chs[0]和chs[1]都是空值channel，和空值channel通信永远都不会成功。

