## Intn

```go
import  "math/rand"
// Intn returns, as an int, a non-negative pseudo-random number in [0,n)
// from the default Source.
// It panics if n <= 0.
func Intn(n int) int
```



## 获取当前时间戳 Unix()   UnixNano()

```go
// Unix returns t as a Unix time, the number of seconds elapsed
// since January 1, 1970 UTC. The result does not depend on the
// location associated with t.
func (t Time) Unix() int64 {
   return t.unixSec()
}

// UnixNano returns t as a Unix time, the number of nanoseconds elapsed
// since January 1, 1970 UTC. The result is undefined if the Unix time
// in nanoseconds cannot be represented by an int64 (a date before the year
// 1678 or after 2262). Note that this means the result of calling UnixNano
// on the zero Time is undefined. The result does not depend on the
// location associated with t.
func (t Time) UnixNano() int64 {
	return (t.unixSec())*1e9 + int64(t.nsec())
}
```



## EncodeToString()

```go 
import "encoding/base64"
// EncodeToString returns the base64 encoding of src.
func (enc *Encoding) EncodeToString(src []byte) string {
   buf := make([]byte, enc.EncodedLen(len(src)))
   enc.Encode(buf, src)
   return string(buf)
}
```



## ReadFile()

```go
// ReadFile reads the file named by filename and returns the contents.
// A successful call returns err == nil, not err == EOF. Because ReadFile
// reads the whole file, it does not treat an EOF from Read as an error
// to be reported.
func ReadFile(filename string) ([]byte, error)
```