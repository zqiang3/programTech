

## 第一种方法

```go
func testMd5() {
   str1 := "abc123"
   d := []byte(str1)
   has := md5.Sum(d)
   md5r := fmt.Sprintf("%x", has)
   fmt.Printf("r= %v", md5r)
}
```





## 第二种方法

```go
func testMd5() {
	str1 := "hello world"
	w := md5.New()
	_, err := io.WriteString(w, str1)  // write str1 to w
	if err != nil {
		fmt.Println(err)
		return
	}
	md5r := fmt.Sprintf("%x", w.Sum(nil))
	fmt.Printf("r= %v", md5r)
}
```

