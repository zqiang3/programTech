go的上下文库



context可以在中途取消或停止一个操作。



**为什么需要取消？**

我们需要用取消来防止我们的系统做不需要的工作。



**监听取消事件**





## chan + select

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    stop := make(chan bool)

    go func() {
        for {
            select {
                case <-stop:
                    fmt.Println("monitor stop, stop it...")
                    return
                default:
                    fmt.Println("goroutine monitor...")
                    time.Sleep(2 * time.Second)
            }
        }
    }()

    time.Sleep(10 * time.Second)
    fmt.Println("ok, stop monitor")
    stop<- true
    time.Sleep(5 * time.Second)
}
```

可以比较优雅地结束一个goroutine



## Context

```go
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, localCancle := context.WithCancel(context.Background())
	go func(ctx context.Context) {
		for {
			select {
			case <-ctx.Done():
				fmt.Println("monitor stop")
				return
			default:
				fmt.Println("goroutine running")
				time.Sleep(2 * time.Second)
			}
		}
	}(ctx)

	time.Sleep(10 * time.Second)
	fmt.Println("ok, stop monitor")
	localCancle()
	time.Sleep(5 * time.Second)
}
```

重写比较简单，就是把原来的chan `stop` 换成Context，使用Context跟踪goroutine，以便进行控制，比如结束等。

`context.Background()` 返回一个空的Context，这个空的Context一般用于整个Context树的根节点。然后我们使用`context.WithCancel(parent)`函数，创建一个可取消的子Context，然后当作参数传给goroutine使用，这样就可以使用这个子Context跟踪这个goroutine。

在goroutine中，使用select调用`<-ctx.Done()`判断是否要结束，如果接受到值的话，就可以返回结束goroutine了；如果接收不到，就会继续进行监控。

那么是如何发送结束指令的呢？这就是示例中的`cancel`函数啦，它是我们调用`context.WithCancel(parent)`函数生成子Context的时候返回的，第二个返回值就是这个取消函数，它是`CancelFunc`类型的。我们调用它就可以发出取消指令，然后我们的监控goroutine就会收到信号，就会返回结束。