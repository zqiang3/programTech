## client

```go
package main

import (
	"fmt"
	"github.com/go-redis/redis/v7"
)

func main() {
	options := redis.Options{
		Addr:               "localhost:6379",
		Password:           "",
		DB:                 0,
	}
	rdb := redis.NewClient(&options)

	pong, err := rdb.Ping().Result()
	fmt.Println(pong, err)
}
```

