

## link

https://juejin.im/entry/5aa8ebe46fb9a028de4467bd



example

```go
package main

import (
	"fmt"
	"net"
	"strings"
)

func handleConn(conn net.Conn) {
	if conn == nil {
		fmt.Println("conn is nil")
		return
	}
	buf := make([]byte, 1024)
	for {
		cnt, err := conn.Read(buf)
		if err != nil || cnt == 0 {
			fmt.Printf("err->%v, count->%d\n", err, cnt)
			return
		}
		cmd := string(buf[:cnt])
		cmd = strings.TrimSpace(cmd)
		fmt.Println(cmd)
		inputs := strings.Split(cmd, " ")
		switch inputs[0] {
		case "ping":
			conn.Write([]byte("pong\n"))
		case "echo":
			res := strings.Join(inputs[1:], " ") + "\n"
			conn.Write([]byte(res))
		case "quit":
			conn.Close()
			break
		}
	}
	fmt.Printf("connection from %v closed\n", conn.RemoteAddr())
}


func main() {
	server, err := net.Listen("tcp", ":1208")
	if err != nil {
		fmt.Printf("Listen got err->%s", err)
		return
	}

	for {
		conn, err := server.Accept()
		if err != nil {
			fmt.Printf("Accept got err->%s", err)
			break
		}
		go handleConn(conn)
	}
}
```

