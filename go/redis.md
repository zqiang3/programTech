# go-redis

## Install

```bash
go get -u github.com/go-redis/redis
```



## Usage

```go
package main

import (
	"fmt"
	"github.com/go-redis/redis"
)

func main() {
	client := redis.NewClient(&redis.Options{
		Addr:               "127.0.0.1:6379",
	})
	pong, err := client.Ping().Result()
	fmt.Println(pong, err)

	err = client.Set("name", "examples", 0).Err()
	if err != nil {
		panic(err)
	}
}
```

## Install

```bash
go get github.com/go-redis/redis/v7
```

## Usage

