1. iota只能在常量表达式中使用
2. 每次 const 出现时，都会让 iota 初始化为0

```go
const a = iota // a=0 
const ( 
  b = iota     //b=0 
  c            //c=1 
)
```

3. 使用下划线跳过不想要的值

```go
type AudioOutput int

const ( 
    OutMute AudioOutput = iota // 0 
    OutMono                    // 1 
    OutStereo                  // 2 
    _ 
    _ 
    OutSurround                // 5 
)

```

