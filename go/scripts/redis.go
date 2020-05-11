package main

import (
    "fmt"
    "github.com/go-redis/redis/v7"
    "time"
)

var (
    redisClient *redis.Client
    key string
    value string
)

func init() {
    redisClient = redis.NewClient(&redis.Options{
        Addr: "localhost:6379",
        Password: "",
        DB: 0,
    })

    key = "test_key"
    value = "test_val"
}


func testSet() {
    result := redisClient.Set(key, value, time.Second * 30)
    fmt.Println(result.Val())
    fmt.Println(result.Result())
}

func testGet() {
    result := redisClient.Get(key)
    fmt.Println(result.Val())
    fmt.Println(result.Result())
}

func testIncr() {
    result := redisClient.Del(key)
    fmt.Printf("del keys", result.Val())
    fmt.Println(result.Result())
    result = redisClient.Incr(key)
    fmt.Println(result.Result())
}

func main() {

    //testSet()
    //testGet()
    testIncr()
    fmt.Println("all finished")
}