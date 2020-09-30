## install

```bash
$ curl -O http://ftp.gnu.org/gnu/gdb/gdb-7.3.1.tar.gz
$ tar -xzf gdb-3.7.1.tar.gzma
$ cd gdb-7.3.1
$ ./configure
$ make
$ [sudo] make install 
```



## go程序

```go
package main

import ( 
    "fmt" 
)

func main() { 
    for i := 0; i < 5; i++ {
        fmt.Println("looping") 
    } 
    fmt.Println("Done") 
}
```

## gdb

```bash
$ go build -gcflags "-N -l" -o gdb_sandbox main.go 
$ ls
gdb_sandbox  main.go  README.md
$ gdb gdb_sandbox
....
(gdb) source /usr/local/src/go/src/runtime/runtime-gdb.py
Loading Go Runtime support.
```

