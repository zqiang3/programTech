package main

import (
    "io"
    "log"
)

func main() {
    foo("Go")
}

func foo(s string) (n int, err error) {
    defer func() {
        log.Printf("foo(%q) = %d, %v", s, n, err)
    }()
    return 7, io.EOF
}
